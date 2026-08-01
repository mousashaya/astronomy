#!/usr/bin/env python
"""CLI: produce the dark-energy figure -- cosmic shear xi+ vs CCL theory."""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker
import numpy as np


def _clean_log_xaxis(ax):
    ax.xaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
    ax.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{v:g}"))

from desc_demo.config import DEFAULT_CLUSTER, FIGURES_DIR, TOMOGRAPHY_FIELD_RADIUS_DEG
from desc_demo.data_access import apply_metacal_response, fetch_shape_catalog
from desc_demo.shear_tomography import ccl_theory_xip, measure_shear_correlation, redshift_distribution


def main():
    catalog = fetch_shape_catalog(
        DEFAULT_CLUSTER.ra_deg, DEFAULT_CLUSTER.dec_deg, TOMOGRAPHY_FIELD_RADIUS_DEG
    )
    catalog = apply_metacal_response(catalog)
    print(f"Loaded {len(catalog)} sources over {TOMOGRAPHY_FIELD_RADIUS_DEG} deg radius")

    # Full sample (not tomographically split) for the best-S/N headline measurement.
    result = measure_shear_correlation(catalog, catalog, min_sep=2.0, max_sep=60.0, nbins=8)
    z_c, nz = redshift_distribution(catalog)
    theta_deg = result["theta_arcmin"] / 60.0

    fig, (ax_xip, ax_dark_energy) = plt.subplots(1, 2, figsize=(13, 5.5))

    # --- Panel 1: measured xi+ vs fiducial CCL theory ---
    ax_xip.errorbar(result["theta_arcmin"], result["xip"], yerr=result["xip_err"],
                     fmt="o", color="C0", label=r"measured $\xi_+$ (TreeCorr)", zorder=3)
    theory_fid = ccl_theory_xip(z_c, nz, z_c, nz, theta_deg)
    ax_xip.plot(result["theta_arcmin"], theory_fid, color="C1", lw=2,
                label=r"CCL theory, fiducial $\Omega_m$=0.30, $w_0$=-1")
    ax_xip.axhline(0, color="gray", lw=0.5)
    ax_xip.set_xscale("log")
    _clean_log_xaxis(ax_xip)
    ax_xip.set_xlabel("angular separation [arcmin]")
    ax_xip.set_ylabel(r"$\xi_+(\theta)$")
    ax_xip.set_title("Cosmic shear correlation function")
    ax_xip.legend(fontsize=8)

    # --- Panel 2: dark energy sensitivity -- same theta bins, varying Omega_m and w0 ---
    variants = [
        (0.30, -1.0, "C1", "-", r"fiducial: $\Omega_m$=0.30, $w_0$=-1.0"),
        (0.20, -1.0, "C2", "--", r"$\Omega_m$=0.20, $w_0$=-1.0"),
        (0.40, -1.0, "C3", "--", r"$\Omega_m$=0.40, $w_0$=-1.0"),
        (0.30, -0.7, "C4", ":", r"$\Omega_m$=0.30, $w_0$=-0.7"),
        (0.30, -1.3, "C5", ":", r"$\Omega_m$=0.30, $w_0$=-1.3"),
    ]
    theta_smooth_deg = np.geomspace(theta_deg.min(), theta_deg.max(), 60)
    theta_smooth_arcmin = theta_smooth_deg * 60.0
    for omega_m, w0, color, ls, label in variants:
        xip_variant = ccl_theory_xip(z_c, nz, z_c, nz, theta_smooth_deg,
                                      Omega_c=omega_m - 0.045, w0=w0)
        ax_dark_energy.plot(theta_smooth_arcmin, xip_variant, color=color, ls=ls, label=label)
    ax_dark_energy.errorbar(result["theta_arcmin"], result["xip"], yerr=result["xip_err"],
                             fmt="o", color="k", ms=4, label="measured (this field)", zorder=3)
    ax_dark_energy.axhline(0, color="gray", lw=0.5)
    ax_dark_energy.set_xscale("log")
    _clean_log_xaxis(ax_dark_energy)
    ax_dark_energy.set_xlabel("angular separation [arcmin]")
    ax_dark_energy.set_ylabel(r"$\xi_+(\theta)$")
    ax_dark_energy.set_title(r"Sensitivity to $\Omega_m$ and dark energy $w_0$")
    ax_dark_energy.legend(fontsize=7)

    fig.suptitle("Dark energy: cosmic shear two-point function", fontsize=13)

    caption = (
        f"{len(catalog)} source galaxies over a {TOMOGRAPHY_FIELD_RADIUS_DEG} deg radius "
        f"(~{np.pi * TOMOGRAPHY_FIELD_RADIUS_DEG**2:.0f} sq deg) field -- for reference, DES Y1's actual "
        "cosmic shear analysis used ~1500 sq deg. This measurement is a pipeline/methodology "
        "demonstration (TAP retrieval -> TreeCorr -> CCL comparison, the same chain DESC's 3x2pt "
        "analysis uses), not a standalone cosmological constraint: at this field size the signal is "
        "shape-noise and cosmic-variance limited, consistent with the theory curve's amplitude but not "
        "a high-significance detection on its own."
    )
    fig.text(0.02, -0.05, caption, fontsize=8, wrap=True, va="top")

    out_path = FIGURES_DIR / "dark_energy_cosmic_shear.png"
    fig.savefig(out_path, dpi=150, bbox_inches="tight")
    print(f"Saved {out_path}")


if __name__ == "__main__":
    main()
