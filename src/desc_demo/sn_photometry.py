"""Stage 2 of the SN Ia pipeline: pull the full light curve (every
archived alert, not just the latest one) for a single object, and shape
it into the format sncosmo's SALT2 fitter expects — that's Stage 4, but
getting the columns right now means Stage 4 needs no further reshaping.
"""
import hashlib
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests

from desc_demo.config import FINK_ZTF_API_URL, RAW_DIR
from desc_demo.sn_cutouts import FinkUnavailable

# Conventional ZTF band colors (roughly matching what Fink's own plots
# and most ZTF papers use), so this is visually consistent with anything
# else you look at outside this project.
BAND_COLORS = {"ztfg": "green", "ztfr": "red", "ztfi": "darkorange"}

# ZTF's filter numbering (i:fid in Fink's schema) mapped to the exact
# bandpass names sncosmo has registered — confirmed directly against a
# running sncosmo install rather than assumed, since a mismatch here
# would silently break Stage 4's fit later instead of erroring loudly.
FID_TO_BAND = {1: "ztfg", 2: "ztfr", 3: "ztfi"}

# Arbitrary but fixed reference zeropoint for the mag -> flux conversion
# below. This does NOT throw away calibration: Fink's magpsf values are
# already physically calibrated (each alert's own zeropoint, i:magzpsci,
# is already baked in) — REFERENCE_ZP is just the single shared reference
# point every epoch's flux gets expressed relative to, so the whole light
# curve ends up on one consistent flux scale. sncosmo only cares that zp
# is consistent across the light curve, not what specific value it is.
REFERENCE_ZP = 25.0
ZP_SYSTEM = "ab"

_LIGHT_CURVE_COLUMNS = [
    "time", "band", "flux", "fluxerr",  # what sncosmo.fit_lc() needs
    "zp", "zpsys",
    "mag", "magerr",                     # kept too — what's actually plotted below
    "rb",                                 # real-bogus score, for later quality cuts
]


def _cache_path(object_id: str) -> Path:
    # Same pattern as sn_discovery.py's TNS cache: keyed by a hash of the
    # object id, parquet on the external volume. Added specifically to
    # support a slow overnight prefetch (see scripts/prefetch_light_curves.py)
    # — without this, every rerun of any stage re-hits Fink for every object.
    digest = hashlib.sha1(object_id.encode()).hexdigest()[:10]
    return RAW_DIR / f"lightcurve_{digest}.parquet"


def fetch_light_curve(object_id: str, use_cache: bool = True) -> pd.DataFrame:
    """Pull every archived alert for `object_id` and reshape into a
    light curve table, one row per (time, band) detection.

    Unlike sn_cutouts.fetch_cutouts (which deliberately keeps only the
    newest alert, for the image view), this keeps *all* of them — the
    whole point of Stage 2 is the time series.
    """
    cache_file = _cache_path(object_id)
    if use_cache and cache_file.exists():
        return pd.read_parquet(cache_file)

    try:
        response = requests.post(
            f"{FINK_ZTF_API_URL}/objects",
            json={"objectId": object_id, "output-format": "json"},
            timeout=45,
        )
    except requests.exceptions.RequestException as exc:
        # Same distinction sn_cutouts.py makes: a network/server failure
        # (confirmed real during a full-batch run — one object hit a 502)
        # is not the same thing as "this object has no data", so it must
        # not be cached as an empty result.
        raise FinkUnavailable(str(exc)) from exc

    if response.status_code != 200:
        raise FinkUnavailable(f"HTTP {response.status_code}: {response.text[:200]}")

    rows = response.json()
    if not rows:
        empty = pd.DataFrame(columns=_LIGHT_CURVE_COLUMNS)
        empty.to_parquet(cache_file)
        return empty

    table = pd.DataFrame(rows)

    mag = table["i:magpsf"].astype(float)
    magerr = table["i:sigmapsf"].astype(float)

    # mag -> flux: standard relation, using our single shared reference
    # zeropoint (see REFERENCE_ZP above) so every epoch lands on one scale.
    flux = 10 ** (-0.4 * (mag - REFERENCE_ZP))
    # Error propagation: d(flux)/flux = ln(10)/2.5 * d(mag) for this
    # relation — the standard small-error approximation used throughout
    # the field for this exact conversion.
    fluxerr = flux * (np.log(10) / 2.5) * magerr

    light_curve = pd.DataFrame({
        "time": table["i:jd"].astype(float) - 2_400_000.5,  # JD -> MJD
        "band": table["i:fid"].map(FID_TO_BAND),
        "flux": flux,
        "fluxerr": fluxerr,
        "zp": REFERENCE_ZP,
        "zpsys": ZP_SYSTEM,
        "mag": mag,
        "magerr": magerr,
        "rb": table["i:rb"].astype(float),
    })

    light_curve = light_curve.sort_values("time").reset_index(drop=True)
    light_curve.to_parquet(cache_file)
    return light_curve


def plot_light_curve(light_curve: pd.DataFrame, title: str = "") -> plt.Figure:
    """Magnitude vs. time, one color per band, error bars, y-axis
    inverted — brighter (numerically smaller magnitude) plots higher,
    which is the universal convention for light curve plots (and the
    opposite of what a plain matplotlib default would give you).
    """
    fig, ax = plt.subplots(figsize=(8, 4.5))

    for band, points in light_curve.groupby("band"):
        ax.errorbar(
            points["time"], points["mag"], yerr=points["magerr"],
            fmt="o", markersize=4, capsize=2,
            color=BAND_COLORS.get(band, "gray"), label=band,
        )

    ax.invert_yaxis()
    ax.set_xlabel("MJD (days)")
    ax.set_ylabel("magnitude")
    ax.set_title(title)
    ax.legend()
    fig.tight_layout()
    return fig
