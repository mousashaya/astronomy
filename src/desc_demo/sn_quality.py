"""Stage 3 of the SN Ia pipeline: decide whether a light curve is even
worth handing to Stage 4's SALT2 fit.

Every threshold below was picked against real objects we actually pulled
and looked at, not chosen abstractly — see the module-level test at the
bottom, which locks in that behavior against those specific objects so a
future change can't silently break what we already verified by eye:
  - SN 2025gha  (3 points, 1 band, 12 days)    -> should FAIL (too sparse)
  - SN 2026lxa  (11 points, 2 bands, 12 days)  -> should FAIL (too short)
  - SN 2021qta  (14 points, 2 bands, 42 days)  -> should PASS (real shape)
  - the 1922-day object (ZTF18aazhwnh)          -> should FAIL (contaminated)
"""
from dataclasses import dataclass

import pandas as pd

MIN_TOTAL_POINTS = 8
MIN_BANDS = 2
MIN_SPAN_DAYS = 20     # below this, can't have seen a real rise-to-decline shape
MAX_SPAN_DAYS = 365    # above this, it's not one SN Ia event (they fade in months)
PEAK_BRACKET_DAYS = 3  # need a point at least this many days before AND after peak


@dataclass
class QualityResult:
    is_fittable: bool
    reasons: list[str]  # every check that failed; empty if is_fittable


def check_light_curve(light_curve: pd.DataFrame) -> QualityResult:
    """Run every quality check and report which ones failed, not just a
    single pass/fail — so a rejected object is actionable ("too short")
    rather than a mystery.
    """
    reasons = []

    if len(light_curve) < MIN_TOTAL_POINTS:
        reasons.append(f"only {len(light_curve)} points (need >= {MIN_TOTAL_POINTS})")

    n_bands = light_curve["band"].nunique()
    if n_bands < MIN_BANDS:
        reasons.append(f"only {n_bands} band(s) (need >= {MIN_BANDS} for color info)")

    if light_curve.empty:
        # Nothing else below can be computed on empty data — report just
        # the two checks above (both will already have failed) rather
        # than crashing on .min()/.max() of nothing.
        return QualityResult(is_fittable=False, reasons=reasons)

    span = light_curve["time"].max() - light_curve["time"].min()
    if span < MIN_SPAN_DAYS:
        reasons.append(f"only spans {span:.0f} days (need >= {MIN_SPAN_DAYS}, too short to see a real shape)")
    if span > MAX_SPAN_DAYS:
        reasons.append(f"spans {span:.0f} days (max {MAX_SPAN_DAYS} — real SNe Ia fade within a year; this is likely contaminated)")

    # Bracketing check: real data strictly before AND after the brightest
    # (lowest-magnitude) point, not just a one-sided fragment that happens
    # to include the peak as its first or last measurement.
    peak_time = light_curve.loc[light_curve["mag"].idxmin(), "time"]
    has_before = (light_curve["time"] <= peak_time - PEAK_BRACKET_DAYS).any()
    has_after = (light_curve["time"] >= peak_time + PEAK_BRACKET_DAYS).any()
    if not (has_before and has_after):
        reasons.append(
            f"peak isn't bracketed by real data at least {PEAK_BRACKET_DAYS} days "
            f"on both sides — likely only caught the rise or only the decline, not both"
        )

    return QualityResult(is_fittable=not reasons, reasons=reasons)


if __name__ == "__main__":
    # Locks in the behavior described in the module docstring against the
    # real objects we already inspected by eye — run with:
    #   python -m desc_demo.sn_quality
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
    from desc_demo.sn_photometry import fetch_light_curve

    expectations = {
        "ZTF25aalrrdz": False,  # SN 2025gha — too sparse
        "ZTF26aavjuuc": False,  # SN 2026lxa — too short
        "ZTF21abhthvj": True,   # SN 2021qta — real shape
        "ZTF18aazhwnh": False,  # 1922-day object — contaminated
    }
    for object_id, expected in expectations.items():
        result = check_light_curve(fetch_light_curve(object_id))
        status = "OK" if result.is_fittable == expected else "MISMATCH"
        print(f"[{status}] {object_id}: fittable={result.is_fittable} (expected {expected}) — {result.reasons}")
