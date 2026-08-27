"""CLI: run Stage 1 (TNS discovery) and print the result.

Same role as run_mass_map.py / run_shear_tomography.py for the weak-lensing
demo — a plain terminal entry point, no UI needed to sanity-check one stage.

Usage:
    python scripts/run_sn_discovery.py
"""
from desc_demo.sn_discovery import find_sn_ia_candidates

if __name__ == "__main__":
    candidates = find_sn_ia_candidates()
    print(f"Found {len(candidates)} TNS-confirmed SN Ia with usable ZTF data\n")
    print(candidates.to_string(index=False))
