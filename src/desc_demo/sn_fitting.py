"""Stage 4 of the SN Ia pipeline: fit SALT2 to a light curve that passed
Stage 3's quality check.

This is the step everything else has been building toward — the SALT2
model (t0, x0, x1, c) is exactly what Stage 5 will plug into the
Tripp/Phillips formula to get a standardized distance, which is the
actual dark-energy measurement.
"""
from dataclasses import dataclass

import matplotlib.pyplot as plt
import pandas as pd
import sncosmo
from astropy.table import Table

# The columns sncosmo needs, in the exact format it expects — this is
# only a format conversion (pandas -> astropy Table), not a reshape,
# because sn_photometry.py already built the light curve with these
# exact column names for this exact reason.
_SNCOSMO_COLUMNS = ["time", "band", "flux", "fluxerr", "zp", "zpsys"]

# Loose but physically-motivated bounds for the fit, not tight guesses:
# t0 within 20 days of our own by-eye peak estimate (the SALT2 model
# itself is ~2 months wide, so 20 days is a generous search window, not
# a strong prior); x1 and c bounded to the range real SNe Ia occupy,
# wide enough that a genuine SN Ia won't hit the edge.
_T0_SEARCH_WINDOW_DAYS = 20
_X1_BOUNDS = (-3.0, 3.0)
_C_BOUNDS = (-0.3, 0.3)


@dataclass
class FitResult:
    success: bool
    params: dict          # {name: value} for z, t0, x0, x1, c
    errors: dict           # {name: 1-sigma uncertainty} for the 4 fitted ones (not z, which is fixed)
    chisq: float
    ndof: int
    model: sncosmo.Model    # the fitted model, needed by plot_fit() below


def fit_salt2(light_curve: pd.DataFrame, redshift: float) -> FitResult:
    """Fit SALT2's 4 free parameters (t0, x0, x1, c) to a light curve,
    with redshift held fixed at the real spectroscopic value from TNS —
    there's no reason to let the fitter guess something we already
    measured directly.
    """
    data = Table.from_pandas(light_curve[_SNCOSMO_COLUMNS])

    model = sncosmo.Model(source="salt2")
    model.set(z=redshift)

    # A reasonable starting guess matters for convergence: seed t0 from
    # the brightest observed point (same logic Stage 3 already uses for
    # its peak-bracketing check) rather than an arbitrary default.
    t0_guess = light_curve.loc[light_curve["mag"].idxmin(), "time"]
    model.set(t0=t0_guess, x0=1e-5)

    result, fitted_model = sncosmo.fit_lc(
        data, model, ["t0", "x0", "x1", "c"],
        bounds={
            "t0": (t0_guess - _T0_SEARCH_WINDOW_DAYS, t0_guess + _T0_SEARCH_WINDOW_DAYS),
            "x1": _X1_BOUNDS,
            "c": _C_BOUNDS,
        },
    )

    return FitResult(
        success=result.success,
        params=dict(zip(result.param_names, result.parameters)),
        errors=dict(result.errors),
        chisq=result.chisq,
        ndof=result.ndof,
        model=fitted_model,
    )


def plot_fit(light_curve: pd.DataFrame, fit: FitResult) -> plt.Figure:
    """The fitted model curve overlaid on the real data, per band, with
    a "pull" (residual / uncertainty) panel underneath each — sncosmo's
    own built-in diagnostic plot. Not hand-rolled: this is well-tested,
    standard-in-the-field code for exactly this job, same reasoning as
    using astropy's ZScaleInterval instead of a hand-rolled stretch in
    sn_cutouts.py.
    """
    data = Table.from_pandas(light_curve[_SNCOSMO_COLUMNS])
    return sncosmo.plot_lc(data, model=fit.model, errors=fit.errors)
