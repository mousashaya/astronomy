"""Postage-stamp cutout images (science / template / difference) for a
single ZTF alert, pulled from Fink's /objects endpoint with
`withcutouts=True`.

Fink hands back raw 2D pixel arrays, not ready-made images — this is the
same "science minus template = difference" idea behind every alert we've
been looking at, just at the pixel level instead of the magnitude level.
So on top of fetching the arrays, this module also does the minimal work
to make them visible: a percentile-clipped stretch (matplotlib can't
usefully imshow() raw flux values without one — they're not in a 0-1
range and often have a long tail of bright pixels that would wash out
everything else).
"""
import numpy as np
import requests
from astropy.stats import sigma_clipped_stats
from astropy.visualization import AsinhStretch, ImageNormalize, ManualInterval
from PIL import Image
from scipy.ndimage import gaussian_filter

from desc_demo.config import FINK_ZTF_API_URL

CUTOUT_KINDS = ["Science", "Template", "Difference"]


class FinkUnavailable(Exception):
    """Fink's API didn't respond in time (or the connection failed).

    Deliberately a *different* signal than fetch_cutouts() returning {} —
    that means "we got an answer and the object genuinely has no data";
    this means "we don't actually know, Fink's infrastructure didn't
    respond." Conflating the two would tell you a real object has no
    data when actually the request just timed out.
    """


def fetch_cutouts(object_id: str) -> dict:
    """Return {kind: 2D numpy array} for this object's most recent alert.

    An object accumulates one alert per ZTF visit, so there can be many
    rows; we always want the newest one, picked explicitly by Julian
    date (`i:jd`) rather than assuming the API returns rows in order.
    """
    try:
        response = requests.post(
            f"{FINK_ZTF_API_URL}/objects",
            json={
                "objectId": object_id,
                "withcutouts": "True",
                "cutout-kind": "All",
                "output-format": "json",
            },
            timeout=45,
        )
    except requests.exceptions.RequestException as exc:
        # Fink's infrastructure is known to be slow/overloaded at times —
        # this is that, not a statement about the object itself.
        raise FinkUnavailable(str(exc)) from exc

    if response.status_code != 200:
        # Known Fink API quirk: an object with zero archived alerts (e.g.
        # one that faded before Fink started archiving ZTF data in Nov
        # 2019) 500s here instead of returning an empty list. Treat that
        # the same as "nothing to show" rather than crashing the caller —
        # a TNS cross-match existing is no guarantee Fink itself has data.
        return {}
    rows = response.json()
    if not rows:
        return {}

    latest = max(rows, key=lambda row: row["i:jd"])
    return {
        kind: np.array(latest[f"b:cutout{kind}_stampData"])
        for kind in CUTOUT_KINDS
    }


def stretch(image: np.ndarray, smoothing_sigma: float = 1.2) -> np.ndarray:
    """Normalize a raw stamp to [0, 1] for display.

    Two earlier attempts at this both still looked grainy/"SAR-image"-
    like, for two different reasons — worth recording since the fix
    ended up being a different kind of change than either attempt:

    1. A hand-rolled percentile+asinh stretch picked its scale from a
       tight percentile of the noisy data itself, pushing background
       *noise* into the compressive region along with the source.
    2. Swapping in `ZScaleInterval` (DS9's default algorithm) fixed
       that, but the underlying problem turned out to be simpler: a
       single 63x63 stamp genuinely has visible pixel-to-pixel shot/read
       noise at the level needed to show an ~8-sigma point source — no
       choice of stretch *curve* removes real noise, it only chooses how
       to display it.

    So the actual fix is a `gaussian_filter` smoothing pass before any
    stretch is computed at all — the same reasoning source-detection
    algorithms use: a real source is spread across several pixels, but
    uncorrelated per-pixel noise isn't, so a small blur suppresses noise
    more than it suppresses the source. This is a *display* choice (it
    trades a little resolution for legibility) — it never touches the
    photometry Fink already measured, which is what Stage 4's SALT2 fit
    will actually use, so it can't bias any science result.

    Background level/spread are then estimated with sigma-clipped
    statistics (median, robust std — the source counts as an outlier
    and gets excluded) rather than a plain percentile or ZScale, which
    both had failure modes on stamps this small. The interval is set to
    [median - 2·std, median + 10·std]: background sits calmly near the
    low end, genuine sources (many-sigma above background) still pop.
    """
    smoothed = gaussian_filter(image, sigma=smoothing_sigma)
    _, median, std = sigma_clipped_stats(smoothed, sigma=3.0)
    interval = ManualInterval(median - 2 * std, median + 10 * std)
    normalize = ImageNormalize(interval=interval, stretch=AsinhStretch(a=0.5))
    return np.nan_to_num(np.clip(normalize(smoothed), 0, 1))


def render_cutout(image: np.ndarray, size: int = 300) -> Image.Image:
    """Turn a raw stamp into something that actually looks good on screen.

    Beyond the stretch() normalization above, these stamps are only
    ~63x63 pixels — blown up to fill a wide UI column with nearest-
    neighbor scaling (the default if you just hand a small array to
    st.image), each pixel becomes a visible flat block. Resizing with
    smooth (LANCZOS) interpolation instead fixes that.
    """
    normalized = stretch(image)
    as_uint8 = (normalized * 255).astype(np.uint8)
    pil_image = Image.fromarray(as_uint8, mode="L")
    return pil_image.resize((size, size), Image.LANCZOS)
