# Reference material

Notes and citations for papers/tools relevant to this project. PDFs
themselves live in `docs/papers/` (gitignored — publisher copyright,
not ours to redistribute) and are for local reading only.

## Rehemtulla, Coughlin, Miller & Jegou du Laz (2025)

**"The automation of optical transient discovery and classification in
Rubin-era time-domain astronomy"**, Nature Astronomy, published online
2025-12-08. DOI: [10.1038/s41550-025-02720-6](https://doi.org/10.1038/s41550-025-02720-6)

Written by the BTSbot authors themselves (Rehemtulla is BTSbot's lead
author/maintainer). A *Perspective* piece — a review of the field's
current automation paradigm and open challenges for the Rubin/LSST era,
not a new-results paper.

**Why it matters here:** directly names the exact problem behind the
planned BTSbot-on-LSST evaluation — scanning-tool ML "can... be
simplistic and brittle. This introduces weaknesses such as preventing
transfer to new surveys" — and frames LSST domain adaptation as a
needed *future* direction, not something already solved. As of this
paper (accepted Oct 2025), no evidence BTSbot itself had been tested or
retrained on real LSST data. Checked directly: no LSST-related
branches, commits, or issues in the BTSbot repo (`nabeelre/BTSbot`) as
of 2026-08-28.

**BTSbot itself:** [github.com/nabeelre/BTSbot](https://github.com/nabeelre/BTSbot)
— open source (TensorFlow/Keras), pretrained models also on HuggingFace
Hub. Multimodal CNN: 63x63 science/template/difference cutout triplet +
25 metadata features -> single 0-1 "bright transient" score. On ZTF:
94.1% accuracy, 100% completeness, 84-93% purity; achieved the first
fully automatic zero-human-intervention transient discovery+
classification (SN 2023tyk).
