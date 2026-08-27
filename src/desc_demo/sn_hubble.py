"""Stage 6 of the SN Ia pipeline: assemble a Hubble diagram from
everything that survives Stages 1-5, and compare against CCL theory
curves for different Omega_m / w0 -- the actual dark-energy-sensitive
comparison. Uses the same pyccl conventions as the weak-lensing demo's
shear_tomography.py (same parameter names/defaults), so both probes in
this project share one cosmology toolchain rather than two.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from desc_demo.sn_fitting import fit_salt2
from desc_demo.sn_photometry import fetch_light_curve
from desc_demo.sn_quality import check_light_curve
from desc_demo.sn_standardization import standardize


def build_hubble_sample(candidates: pd.DataFrame) -> pd.DataFrame:
    """Run Stages 2-5 for every candidate, keeping only the ones that
    make it all the way through cleanly. A candidate failing at any
    stage is skipped, not raised -- with a small real sample, some
    fraction failing is the expected, normal outcome, not exceptional.
    """
    rows = []
    for _, cand in candidates.iterrows():
        object_id = cand["f:internalname"]
        redshift = cand["f:redshift"]

        light_curve = fetch_light_curve(object_id)
        if light_curve.empty:
            continue

        if not check_light_curve(light_curve).is_fittable:
            continue

        fit = fit_salt2(light_curve, redshift=redshift)
        if not fit.success:
            continue

        dist = standardize(fit)
        rows.append({
            "object_id": object_id,
            "name": cand["f:fullname"],
            "z": redshift,
            "mu": dist.mu,
            "mu_err": dist.mu_err,
            "chisq_dof": fit.chisq / fit.ndof,
        })

    return pd.DataFrame(rows)


def ccl_theory_mu(z, Omega_c=0.25, Omega_b=0.045, h=0.7, n_s=0.965,
                   sigma8=0.81, w0=-1.0, wa=0.0):
    """Predicted distance modulus vs. redshift for a given cosmology --
    same CCL call pattern as shear_tomography.ccl_theory_xip, just
    luminosity_distance instead of angular_cl/correlation.
    """
    import pyccl as ccl

    cosmo = ccl.Cosmology(Omega_c=Omega_c, Omega_b=Omega_b, h=h, n_s=n_s,
                           sigma8=sigma8, w0=w0, wa=wa,
                           transfer_function="eisenstein_hu")
    a = 1 / (1 + np.asarray(z))
    d_l_mpc = ccl.luminosity_distance(cosmo, a)
    return 5 * np.log10(d_l_mpc * 1e6) - 5


def plot_hubble_diagram(sample: pd.DataFrame) -> plt.Figure:
    """Data vs. fiducial theory, plus sensitivity to Omega_m/w0 --
    same "variants" style as plot_shear_tomography.py's dark-energy panel.
    """
    fig, ax = plt.subplots(figsize=(7, 5))

    z_smooth = np.linspace(max(sample["z"].min() * 0.8, 0.001), sample["z"].max() * 1.2, 100)

    variants = [
        (0.30, -1.0, "C1", "-", r"fiducial: $\Omega_m$=0.30, $w_0$=-1.0"),
        (0.20, -1.0, "C2", "--", r"$\Omega_m$=0.20, $w_0$=-1.0"),
        (0.40, -1.0, "C3", "--", r"$\Omega_m$=0.40, $w_0$=-1.0"),
        (0.30, -0.7, "C4", ":", r"$\Omega_m$=0.30, $w_0$=-0.7"),
        (0.30, -1.3, "C5", ":", r"$\Omega_m$=0.30, $w_0$=-1.3"),
    ]
    for omega_m, w0, color, ls, label in variants:
        mu_theory = ccl_theory_mu(z_smooth, Omega_c=omega_m - 0.045, w0=w0)
        ax.plot(z_smooth, mu_theory, color=color, ls=ls, label=label)

    ax.errorbar(sample["z"], sample["mu"], yerr=sample["mu_err"],
                fmt="o", color="k", ms=5, label="our sample", zorder=3)

    ax.set_xlabel("redshift z")
    ax.set_ylabel(r"distance modulus $\mu$")
    ax.set_title("Hubble diagram: sensitivity to $\\Omega_m$ and dark energy $w_0$")
    ax.legend(fontsize=8)
    fig.tight_layout()
    return fig
