"""Pulls DES DR1 metacalibration shapes + photo-z from NOIRLab Data Lab via TAP.

Query pattern verified against the LSST DESC CLMM package's own worked
example (Example5_Fit_Halo_mass_to_DES_data), which uses these same two
tables and join: https://lsstdesc.org/CLMM/compiled-examples/
"""
import hashlib

import pyvo
from astropy.table import Table

from desc_demo.config import DATALAB_TAP_URL, RAW_DIR

QUERY_TEMPLATE = """
SELECT P.mean_z,
       C.coadd_objects_id, C.ra, C.dec, C.e1, C.e2,
       C.r11, C.r12, C.r21, C.r22
FROM des_dr1.photo_z AS P
INNER JOIN des_dr1.shape_metacal_riz_unblind AS C
  ON P.coadd_objects_id = C.coadd_objects_id
WHERE 't' = Q3C_RADIAL_QUERY(C.ra, C.dec, {ra}, {dec}, {radius})
  AND P.minchi2 < 1
  AND P.z_sigma < 0.1
  AND C.flags_select = 0
"""


def _cache_path(ra: float, dec: float, radius: float) -> "Path":
    key = f"{ra:.6f}_{dec:.6f}_{radius:.4f}"
    digest = hashlib.sha1(key.encode()).hexdigest()[:10]
    return RAW_DIR / f"shape_photoz_{digest}.parquet"


def fetch_shape_catalog(ra_deg: float, dec_deg: float, radius_deg: float,
                         use_cache: bool = True) -> Table:
    """Query DES DR1 metacal shapes + photo-z around (ra, dec).

    Results are cached to Parquet on the external data volume, keyed by
    the query parameters, so re-running an analysis doesn't re-hit the
    TAP service every time.
    """
    cache_file = _cache_path(ra_deg, dec_deg, radius_deg)
    if use_cache and cache_file.exists():
        return Table.from_pandas(__import__("pandas").read_parquet(cache_file))

    service = pyvo.dal.TAPService(DATALAB_TAP_URL)
    query = QUERY_TEMPLATE.format(ra=ra_deg, dec=dec_deg, radius=radius_deg)
    result = service.search(query)
    table = result.to_table()

    table.to_pandas().to_parquet(cache_file)
    return table


def apply_metacal_response(table: Table) -> Table:
    """Calibrate raw ellipticities by the mean diagonal metacal response.

    Off-diagonal response terms are known to be sub-percent for this
    catalog and are dropped, matching the CLMM tutorial's approach.
    """
    r_diag = (table["r11"].mean() + table["r22"].mean()) / 2.0
    table["g1"] = table["e1"] / r_diag
    table["g2"] = table["e2"] / r_diag
    table.meta["r_diag"] = float(r_diag)
    return table


if __name__ == "__main__":
    from desc_demo.config import DEFAULT_CLUSTER

    cat = fetch_shape_catalog(
        DEFAULT_CLUSTER.ra_deg, DEFAULT_CLUSTER.dec_deg, DEFAULT_CLUSTER.radius_deg
    )
    cat = apply_metacal_response(cat)
    print(f"Fetched {len(cat)} sources around {DEFAULT_CLUSTER.name}")
    print(f"mean r_diag = {cat.meta['r_diag']:.4f}")
