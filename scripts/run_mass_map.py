#!/usr/bin/env python
"""CLI: fit cluster mass (CLMM) and build a Kaiser-Squires convergence map."""
from desc_demo.config import DEFAULT_CLUSTER, FIGURES_DIR
from desc_demo.data_access import apply_metacal_response, fetch_shape_catalog
from desc_demo.mass_map import fit_cluster_mass, kaiser_squires_map


def main():
    catalog = fetch_shape_catalog(
        DEFAULT_CLUSTER.ra_deg, DEFAULT_CLUSTER.dec_deg, DEFAULT_CLUSTER.radius_deg
    )
    catalog = apply_metacal_response(catalog)
    print(f"Loaded {len(catalog)} sources around {DEFAULT_CLUSTER.name}")

    print("\n--- CLMM NFW mass fit ---")
    fit = fit_cluster_mass(catalog, DEFAULT_CLUSTER)
    print(f"N background galaxies used: {fit['n_source_galaxies']}")
    print(f"M200c = {fit['m_msun']:.3e} +/- {fit['m_msun_err']:.3e} Msun")

    print("\n--- Kaiser-Squires convergence map ---")
    # Wider field than the CLMM fit: KS mapping is source-count limited, and
    # a bigger footprint gives more galaxies to smooth over. Keep the fit
    # above on the tutorial-matched 0.3 deg radius for reproducibility.
    from dataclasses import replace

    ks_cluster = replace(DEFAULT_CLUSTER, radius_deg=0.6)
    ks_catalog = fetch_shape_catalog(ks_cluster.ra_deg, ks_cluster.dec_deg, ks_cluster.radius_deg)
    ks_catalog = apply_metacal_response(ks_catalog)
    print(f"Loaded {len(ks_catalog)} sources for the wider mass-map field")
    ks = kaiser_squires_map(ks_catalog, ks_cluster)
    print(f"Grid shape: {ks['kappa'].shape}")
    print(f"kappa range: [{ks['kappa'].min():.4f}, {ks['kappa'].max():.4f}]")

    import numpy as np

    # KS reconstruction is only trustworthy well inside the field boundary:
    # the true shear signal from mass just outside the field still leaks in,
    # biasing the map near the edges. Standard practice is to only inspect
    # peaks in an inner "trusted" region -- trim outer quarter on each side.
    n = ks["kappa"].shape[0]
    trim = n // 4
    inner = ks["kappa"][trim:n - trim, trim:n - trim]
    peak_idx = np.unravel_index(np.argmax(inner), inner.shape)
    peak_x = ks["x_arcmin"][trim:n - trim][peak_idx[0]]
    peak_y = ks["y_arcmin"][trim:n - trim][peak_idx[1]]
    print(f"Peak kappa (inner trusted region) = {inner.max():.4f} at "
          f"({peak_x:.2f}, {peak_y:.2f}) arcmin from cluster center")


if __name__ == "__main__":
    main()
