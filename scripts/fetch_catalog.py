#!/usr/bin/env python
"""CLI: pull the DES DR1 shape + photo-z catalog around a target and cache it.

Usage:
    python scripts/fetch_catalog.py                      # default cluster, mass-map radius
    python scripts/fetch_catalog.py --tomography          # wider field for shear tomography
    python scripts/fetch_catalog.py --ra 79.15 --dec -54.5 --radius 0.5
"""
import argparse

from desc_demo.config import DEFAULT_CLUSTER, TOMOGRAPHY_FIELD_RADIUS_DEG
from desc_demo.data_access import apply_metacal_response, fetch_shape_catalog


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ra", type=float, default=DEFAULT_CLUSTER.ra_deg)
    parser.add_argument("--dec", type=float, default=DEFAULT_CLUSTER.dec_deg)
    parser.add_argument("--radius", type=float, default=None)
    parser.add_argument(
        "--tomography", action="store_true",
        help="use the wider tomography field radius instead of the cluster radius",
    )
    parser.add_argument("--no-cache", action="store_true")
    args = parser.parse_args()

    radius = args.radius
    if radius is None:
        radius = TOMOGRAPHY_FIELD_RADIUS_DEG if args.tomography else DEFAULT_CLUSTER.radius_deg

    print(f"Querying DES DR1 around ra={args.ra}, dec={args.dec}, radius={radius} deg ...")
    table = fetch_shape_catalog(args.ra, args.dec, radius, use_cache=not args.no_cache)
    table = apply_metacal_response(table)

    print(f"Fetched {len(table)} sources")
    print(f"mean r_diag = {table.meta['r_diag']:.4f}")
    print(f"redshift range: {table['mean_z'].min():.3f} - {table['mean_z'].max():.3f}")


if __name__ == "__main__":
    main()
