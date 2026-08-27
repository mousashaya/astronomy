"""Project-wide configuration.

Data lives on the external volume by default (internal SSD is tight).
Override with the ASTRO_DATA_DIR env var if you want it somewhere else.
"""
import os
from dataclasses import dataclass
from pathlib import Path

# CLMM auto-detects a modeling backend (ccl / NumCosmo / cluster_toolkit) at
# import time; must be set before `clmm` is imported anywhere.
os.environ.setdefault("CLMM_MODELING_BACKEND", "ccl")

DATA_DIR = Path(os.environ.get("ASTRO_DATA_DIR", "/Volumes/Machine Learning/astronomy/data"))
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
FIGURES_DIR = DATA_DIR / "figures"

for _d in (RAW_DIR, PROCESSED_DIR, FIGURES_DIR):
    _d.mkdir(parents=True, exist_ok=True)

# NOIRLab Data Lab TAP service — public, no auth required for DR1 tables.
DATALAB_TAP_URL = "https://datalab.noirlab.edu/tap"

# Fink runs separate infrastructure per survey (ZTF vs LSST alerts are
# different data, processed and stored independently) — so there are two
# API hosts. The TNS resolver (sn_discovery.py) happens to work on either,
# since TNS itself isn't survey-specific, but anything object-level —
# photometry, cutouts (sn_cutouts.py) — has to hit the host that actually
# has that survey's alerts.
FINK_LSST_API_URL = "https://api.lsst.fink-portal.org/api/v1"
FINK_ZTF_API_URL = "https://api.ztf.fink-portal.org/api/v1"

# Kept as an alias for the resolver call in sn_discovery.py, which doesn't
# care which host it hits.
FINK_API_URL = FINK_LSST_API_URL

# TNS classification string we treat as "confirmed SN Ia" for the discovery
# pipeline. Kept as a named constant (not a literal buried in a filter) so
# it's a one-line change later to widen this to subtypes like "SN Ia-91bg".
TNS_SN_IA_TYPE = "SN Ia"


@dataclass(frozen=True)
class ClusterTarget:
    name: str
    ra_deg: float
    dec_deg: float
    redshift: float
    radius_deg: float = 0.3


# Default target: RMJ051637.4-543001.6 (ACO S520), the same cluster used in
# the LSST DESC CLMM package's own DES-data worked example. Reusing it means
# we have a literature cross-check for the recovered mass.
DEFAULT_CLUSTER = ClusterTarget(
    name="RMJ051637.4-543001.6 (ACO S520)",
    ra_deg=79.155704,
    dec_deg=-54.500456,
    redshift=0.30416065,
)

# Wider, source-only field for the cosmic shear tomography measurement
# (mass mapping wants a tight radius around one halo; tomography wants area).
TOMOGRAPHY_FIELD_RADIUS_DEG = 1.5
