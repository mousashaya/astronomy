#!/usr/bin/env python
"""CLI: measure tomographic cosmic shear and compare to CCL theory."""
import numpy as np

from desc_demo.config import DEFAULT_CLUSTER, TOMOGRAPHY_FIELD_RADIUS_DEG
from desc_demo.data_access import apply_metacal_response, fetch_shape_catalog
from desc_demo.shear_tomography import (
    assign_tomographic_bins,
    ccl_theory_xip,
    measure_shear_correlation,
    redshift_distribution,
)


def main():
    catalog = fetch_shape_catalog(
        DEFAULT_CLUSTER.ra_deg, DEFAULT_CLUSTER.dec_deg, TOMOGRAPHY_FIELD_RADIUS_DEG
    )
    catalog = apply_metacal_response(catalog)
    print(f"Loaded {len(catalog)} sources over {TOMOGRAPHY_FIELD_RADIUS_DEG} deg radius")

    z_edges = [0.2, 0.6, 1.0, 1.5]
    zbins = assign_tomographic_bins(catalog, z_edges)
    for i, zb in enumerate(zbins):
        print(f"bin {i} [{z_edges[i]}, {z_edges[i+1]}): {len(zb)} galaxies")

    # Auto-correlation of the best-populated bin, checked against both sign
    # conventions -- compare xi- (which IS sensitive to a g2 flip) against
    # the theory prediction to determine which convention is physical.
    best = max(zbins, key=len)
    z_c, nz = redshift_distribution(best)

    results = {}
    for flip in (False, True):
        results[flip] = measure_shear_correlation(best, best, flip_g2=flip)
        r = results[flip]
        print(f"\nflip_g2={flip}:")
        print(f"  xi+ = {np.array2string(r['xip'], precision=6)}")
        print(f"  xi- = {np.array2string(r['xim'], precision=6)}")

    theta_deg = results[False]["theta_arcmin"] / 60.0
    theory_xip = ccl_theory_xip(z_c, nz, z_c, nz, theta_deg)
    print(f"\nCCL fiducial theory xi+ (same theta bins): {np.array2string(theory_xip, precision=8)}")


if __name__ == "__main__":
    main()
