#!/usr/bin/env python
"""CLI: produce the dark-matter figure -- KS convergence map + CLMM mass fit."""
from dataclasses import replace

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker
import numpy as np

from desc_demo.config import DEFAULT_CLUSTER, FIGURES_DIR
from desc_demo.data_access import apply_metacal_response, fetch_shape_catalog
from desc_demo.mass_map import fit_cluster_mass, kaiser_squires_map


def main():
    catalog = fetch_shape_catalog(
        DEFAULT_CLUSTER.ra_deg, DEFAULT_CLUSTER.dec_deg, DEFAULT_CLUSTER.radius_deg
    )
    catalog = apply_metacal_response(catalog)
    fit = fit_cluster_mass(catalog, DEFAULT_CLUSTER)

    ks_cluster = replace(DEFAULT_CLUSTER, radius_deg=0.6)
    ks_catalog = fetch_shape_catalog(ks_cluster.ra_deg, ks_cluster.dec_deg, ks_cluster.radius_deg)
    ks_catalog = apply_metacal_response(ks_catalog)
    ks = kaiser_squires_map(ks_catalog, ks_cluster)

    fig, (ax_profile, ax_map) = plt.subplots(1, 2, figsize=(13, 5.5))

    # --- Panel 1: azimuthally-averaged tangential shear + NFW fit (the headline result) ---
    fd = fit["fit_data"]
    ax_profile.errorbar(fd["radius"], fd["gt"], yerr=fd["gt_err"], fmt="o", color="C0",
                         label="measured $g_t$ (radially binned)", zorder=3)
    ax_profile.plot(fit["best_fit_r_mpc"], fit["best_fit_gt"], color="C1", lw=2,
                     label=f"best-fit NFW, $M_{{200c}}$={fit['m_msun']:.2e} $M_\\odot$")
    ax_profile.axhline(0, color="gray", lw=0.5)
    ax_profile.set_xscale("log")
    ax_profile.xaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
    ax_profile.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{v:g}"))
    ax_profile.set_xlabel("radius [Mpc]")
    ax_profile.set_ylabel(r"reduced tangential shear $g_t$")
    ax_profile.set_title("CLMM: tangential shear profile + NFW fit")
    ax_profile.legend(fontsize=8)

    # --- Panel 2: 2D Kaiser-Squires convergence map (illustrative) ---
    extent = [ks["x_arcmin"][0], ks["x_arcmin"][-1], ks["y_arcmin"][0], ks["y_arcmin"][-1]]
    im = ax_map.imshow(ks["kappa"].T, origin="lower", extent=extent, cmap="inferno")
    ax_map.contour(ks["x_arcmin"], ks["y_arcmin"], ks["kappa"].T, levels=6, colors="white", linewidths=0.5, alpha=0.6)
    ax_map.plot(0, 0, marker="+", color="cyan", markersize=16, markeredgewidth=2, label="cluster center (redMaPPer)")

    n = ks["kappa"].shape[0]
    trim = n // 4
    rect_half = ks["x_arcmin"][n - trim - 1]
    ax_map.add_patch(plt.Rectangle((-rect_half, -rect_half), 2 * rect_half, 2 * rect_half,
                                    fill=False, ls="--", color="lightgray", lw=1, label="trusted region"))
    ax_map.set_xlabel("arcmin (RA offset)")
    ax_map.set_ylabel("arcmin (Dec offset)")
    ax_map.set_title("Kaiser-Squires convergence map")
    fig.colorbar(im, ax=ax_map, label=r"$\kappa$", fraction=0.046)
    ax_map.legend(loc="upper right", fontsize=7)

    fig.suptitle(f"Dark matter: weak-lensing mass of {DEFAULT_CLUSTER.name}", fontsize=13)

    caption = (
        f"CLMM NFW fit: M200c = {fit['m_msun']:.2e} +/- {fit['m_msun_err']:.2e} Msun "
        f"({fit['n_source_galaxies']} background galaxies, ~{fit['m_msun'] / fit['m_msun_err']:.1f} sigma). "
        "The azimuthally-averaged tangential-shear fit (left) is the robust quantitative detection; "
        "the raw 2D convergence map (right) is shape-noise limited at this depth/field size for a single "
        "cluster and is shown for illustration, not as a standalone detection."
    )
    fig.text(0.02, -0.03, caption, fontsize=8, wrap=True, va="top")

    out_path = FIGURES_DIR / "dark_matter_mass_map.png"
    fig.savefig(out_path, dpi=150, bbox_inches="tight")
    print(f"Saved {out_path}")


if __name__ == "__main__":
    main()
