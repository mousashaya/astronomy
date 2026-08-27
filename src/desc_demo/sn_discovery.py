"""Stage 1 of the SN Ia pipeline: find spectroscopically-confirmed SN Ia
that Fink has already cross-matched against the TNS (Transient Name
Server) catalog.

Why TNS instead of Fink's own ML classifier probability: a TNS type is
human-vetted — someone actually took a spectrum and classified the
object — so it's a ground-truth label, and TNS entries also carry a
spectroscopic redshift for free. The cost is sample size: this is a much
smaller, cleaner set than "everything Fink's classifier is >50% confident
about". See the project notes for the full purity-vs-sample-size tradeoff;
this module intentionally takes the small-and-clean side of it for a
first working pipeline.
"""
import hashlib
import json
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import pandas as pd
import requests

from desc_demo.config import FINK_API_URL, FINK_ZTF_API_URL, RAW_DIR, TNS_SN_IA_TYPE

# Columns we actually need downstream, pulled out of Fink's wider "f:*"
# response schema. Keeping this as a list (not just slicing ad hoc) makes
# it obvious at a glance what Stage 2 is allowed to depend on.
_CANDIDATE_COLUMNS = [
    "f:internalname",  # ZTF object ID, e.g. "ZTF22aaaifcx" — what Stage 2 needs
    "f:fullname",       # human-readable TNS name, e.g. "SN 2022and"
    "f:redshift",        # spectroscopic redshift — what Stage 4 (fitting) needs
    "f:ra", "f:declination",
    "f:discoverydate",
]


def _cache_path(nmax: int) -> Path:
    # Cache the raw TNS pull locally (external volume, see config.py) so
    # re-running this — including every time the Streamlit UI reruns the
    # script — doesn't re-hit Fink's API. Same caching pattern as
    # data_access.py's fetch_shape_catalog.
    key = f"tns_catalog_{nmax}"
    digest = hashlib.sha1(key.encode()).hexdigest()[:10]
    return RAW_DIR / f"tns_{digest}.parquet"


def fetch_tns_catalog(nmax: int = 20000, use_cache: bool = True) -> pd.DataFrame:
    """Pull (a slice of) Fink's TNS cross-match catalog.

    The trick this relies on: Fink's /resolver endpoint normally looks up
    ONE name (e.g. "SN 2022and"), but passing an *empty* name_or_id
    returns the whole catalog instead — every TNS object Fink knows
    about, regardless of type. `nmax` caps how many rows come back; the
    full catalog is 200k+ rows, far more than we need for a first pass.
    """
    cache_file = _cache_path(nmax)
    if use_cache and cache_file.exists():
        return pd.read_parquet(cache_file)

    response = requests.post(
        f"{FINK_API_URL}/resolver",
        json={"resolver": "tns", "name_or_id": "", "nmax": nmax},
        timeout=60,
    )
    response.raise_for_status()  # fail loudly if Fink rejects the request

    # Fink's REST API returns a JSON list of row-records — this is the
    # same shape as the cone-search endpoint, so pandas can read it directly.
    catalog = pd.DataFrame(response.json())
    catalog.to_parquet(cache_file)
    return catalog


def find_sn_ia_candidates(nmax: int = 20000, use_cache: bool = True,
                           only_available: bool = True) -> pd.DataFrame:
    """Filter the TNS catalog down to usable, confirmed SN Ia candidates.

    Four filters are applied, each for a distinct reason:
      1. f:type == "SN Ia"            -> spectroscopically confirmed, not
                                          a probabilistic ML guess
      2. f:internalname starts "ZTF"  -> a TNS entry can carry ATLAS/PS/
                                          other survey names too, but we
                                          can only pull photometry from
                                          Fink for objects seen in ZTF
      3. f:redshift is a valid number -> Stage 4's SALT2 fit needs a
                                          redshift; some TNS entries are
                                          typed without one ever recorded
      4. only_available (default True) -> also drops candidates Fink has
                                          zero archived alerts for (see
                                          filter_to_available). Every
                                          later stage needs actual
                                          photometry, so a candidate list
                                          that includes guaranteed dead
                                          ends isn't a useful default —
                                          set False only if you
                                          specifically want to see what
                                          got excluded and why.
    """
    catalog = fetch_tns_catalog(nmax=nmax, use_cache=use_cache)

    # TNS sometimes reports redshift as an empty string rather than a
    # true null, so coerce to numeric and let bad/missing values become
    # NaN — that's what makes the has_redshift filter below work.
    redshift = pd.to_numeric(catalog["f:redshift"], errors="coerce")

    is_sn_ia = catalog["f:type"] == TNS_SN_IA_TYPE
    has_ztf_id = catalog["f:internalname"].str.startswith("ZTF", na=False)
    has_redshift = redshift.notna()

    candidates = catalog.loc[is_sn_ia & has_ztf_id & has_redshift, _CANDIDATE_COLUMNS].copy()
    candidates["f:redshift"] = redshift.loc[candidates.index]

    # Newest discoveries first. This isn't just cosmetic: a TNS cross-match
    # existing is no guarantee Fink actually has archived alerts for that
    # object (its own ZTF archive only starts Nov 2019, and even after
    # that, plenty of objects simply weren't re-observed) — measured
    # directly, ~60% of recent candidates have data vs. ~20% of the oldest
    # ones, so sorting this way meaningfully improves the odds that
    # whichever candidate gets picked in the UI actually has something to
    # show, rather than being an even bet.
    candidates = candidates.sort_values("f:discoverydate", ascending=False).reset_index(drop=True)

    if only_available:
        candidates = filter_to_available(candidates)

    return candidates


_C_KM_S = 299_792.458       # speed of light
_H0_KM_S_MPC = 70.0          # today's expansion rate (Hubble constant), approximate
_MPC_TO_GLY = 3.2616e-3       # 1 megaparsec = 3.2616 million ly = 3.2616e-3 billion ly


def naive_distance_gly(redshift: pd.Series) -> pd.Series:
    """Rough light-travel distance in billions of light-years, via
    Hubble's Law: velocity ~ c*z, distance ~ velocity / H0.

    Deliberately named "naive" — this is only valid for z << 1, because
    it assumes the universe has always expanded at *today's* rate. It
    hasn't; how that rate has changed over time (Ωm, w0) is the entire
    thing this project is trying to measure. This function exists purely
    to give redshift numbers some physical grounding while browsing
    candidates — the real Hubble-diagram stage will compute distance via
    CCL's full cosmological formula instead, and the difference between
    that and this naive estimate at higher z *is* the dark-energy signal.

    Distance and look-back time come out as the *same number* at this
    level of approximation — a light-year is, by definition, the
    distance light travels in a year, so a light-travel distance in
    billions of light-years already *is* a look-back time in billions of
    years, no separate calculation needed. (This stops being exactly
    true for the real CCL-based distance later, since proper distance
    and light-travel time diverge once the expansion history actually
    matters — another place where "the naive answer" and "the real
    answer" splitting apart is itself informative.)
    """
    velocity_km_s = redshift * _C_KM_S
    distance_mpc = velocity_km_s / _H0_KM_S_MPC
    return distance_mpc * _MPC_TO_GLY


_AVAILABILITY_CACHE_FILE = RAW_DIR / "fink_ztf_availability.json"


def _has_archived_data(object_id: str) -> bool:
    """Cheap check: does Fink have ANY archived alert for this ZTF object?

    Uses the plain photometry endpoint (no cutouts), because that one
    returns an empty list gracefully — sn_cutouts.py's fetch_cutouts
    documents why the cutouts endpoint specifically 500s instead on an
    object with zero alerts, which makes it useless for a quick check
    like this one.
    """
    try:
        response = requests.post(
            f"{FINK_ZTF_API_URL}/objects",
            json={"objectId": object_id, "output-format": "json"},
            timeout=15,
        )
        return response.status_code == 200 and len(response.json()) > 0
    except requests.exceptions.RequestException:
        return False


def filter_to_available(candidates: pd.DataFrame, max_workers: int = 16) -> pd.DataFrame:
    """Keep only candidates that actually have archived Fink alert data.

    Measured directly: roughly 20-60% of TNS-confirmed candidates have
    zero archived alerts (older ones worse, recent ones better — see
    find_sn_ia_candidates' sort comment). Without this filter, "confirmed
    SN Ia" is a weaker guarantee than it sounds — this makes the
    candidate list actually match what the UI can show.

    Two things worth knowing about how this works:
      - Checks run in parallel (ThreadPoolExecutor) since this is pure
        network waiting, not computation — checking ~300 objects one at
        a time would take minutes; in parallel it's seconds.
      - Results are cached per-object-id in a small JSON file (not the
        parquet cache used elsewhere) since this needs to grow
        incrementally as new objects get checked, rather than being
        invalidated as one block the way the TNS catalog pull is.
    """
    cache: dict[str, bool] = {}
    if _AVAILABILITY_CACHE_FILE.exists():
        cache = json.loads(_AVAILABILITY_CACHE_FILE.read_text())

    ids = candidates["f:internalname"].tolist()
    to_check = [oid for oid in ids if oid not in cache]

    if to_check:
        with ThreadPoolExecutor(max_workers=max_workers) as pool:
            results = pool.map(_has_archived_data, to_check)
        cache.update(zip(to_check, results))
        _AVAILABILITY_CACHE_FILE.write_text(json.dumps(cache))

    has_data = candidates["f:internalname"].map(cache)
    return candidates.loc[has_data].reset_index(drop=True)


if __name__ == "__main__":
    # Quick manual check: `python -m desc_demo.sn_discovery` from the repo
    # root (with the venv active) runs just this stage in isolation.
    found = find_sn_ia_candidates()
    print(f"Found {len(found)} TNS-confirmed SN Ia with usable ZTF data")
    print(found.head())
