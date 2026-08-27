#!/usr/bin/env python
"""CLI: produce the SN Ia Hubble diagram figure -- runs the full
Stage 1-6 pipeline and saves the result, same role as
plot_mass_map.py / plot_shear_tomography.py for the weak-lensing demo.

Network-bound (a light curve fetch + SALT2 fit per candidate), so this
takes a minute or two, not seconds -- there's no caching on Stage 2's
fetch_light_curve yet, unlike the weak-lensing demo's TAP queries.
"""
from desc_demo.config import FIGURES_DIR
from desc_demo.sn_discovery import find_sn_ia_candidates
from desc_demo.sn_hubble import build_hubble_sample, plot_hubble_diagram

N_CANDIDATES = 40  # matches what was used to generate the committed figure


def main():
    candidates = find_sn_ia_candidates()
    print(f"{len(candidates)} available candidates; running the full pipeline on the first {N_CANDIDATES}")

    sample = build_hubble_sample(candidates.head(N_CANDIDATES))
    print(f"{len(sample)} / {N_CANDIDATES} made it through all 5 stages cleanly")

    fig = plot_hubble_diagram(sample)
    out_path = FIGURES_DIR / "sn_hubble_diagram.png"
    fig.savefig(out_path, dpi=150, bbox_inches="tight")
    print(f"Saved {out_path}")


if __name__ == "__main__":
    main()
