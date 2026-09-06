# BTSbot evaluation

Investigating whether [BTSbot](https://github.com/nabeelre/BTSbot) — ZTF's
published, open-source scanner-automation model — generalizes to real LSST
alert data. First step: reproduce its own published ZTF test-set numbers
(94.1% accuracy, 100% completeness, 84-93% purity, Rehemtulla et al. 2024)
to confirm our inference harness is correct before pointing it at anything
new. See `docs/references.md` in the repo root for the full paper citation
and context on why this is worth doing.

## Environment

Separate venv (`.venv-btsbot/` at repo root, Python 3.12) — kept apart from
the main project's `.venv` because TensorFlow has no published wheel for
the main venv's Python (3.14) yet. Nothing else about this work needs the
main pipeline's dependencies (sncosmo, pyccl, clmm), or vice versa.

```
python3.12 -m venv .venv-btsbot
source .venv-btsbot/bin/activate
pip install tensorflow pandas numpy scikit-learn
```

## Layout

```
reference/    vendored source from BTSbot v1.0.1 (MIT licensed, see
              reference/LICENSE) — architectures.py, bts_val.py,
              alert_utils.py, README.md. This is the "Publication Version"
              tag/release, matching the exact model that produced the
              published paper numbers -- NOT the same as the current
              `main` branch, which has since been reworked into a newer
              "v2" architecture (ConvNeXt/MaxViT). Using the wrong version
              would make any reproduction attempt meaningless.
models/       gitignored (large binary artifacts, not ours to redistribute
              even though the MIT license technically permits it) --
              v1.0.1_best_model/ is BTSbot's actual production model
              weights (Keras SavedModel format), extracted from
              production_models/v1.0.1.tar.gz in the BTSbot repo at the
              v1.0.1 tag.
```

## Data

The labeled ZTF train/val/test set (images + metadata, CC BY 4.0, Zenodo
record 10839691) lives on the external volume:
`/Volumes/Machine Learning/astronomy/data/btsbot/` — not in this repo,
same pattern as the main pipeline's cached data (see `src/desc_demo/config.py`).

## The 25 metadata features (order matters)

From BTSbot's own usage example — confirmed these column names already
exist in the downloaded `test_cand_v10_N100_programid1.csv`:

```
sgscore1, distpsnr1, sgscore2, distpsnr2, fwhm, magpsf, sigmapsf, chipsf,
ra, dec, diffmaglim, ndethist, nmtchps, age, days_since_peak, days_to_peak,
peakmag_so_far, new_drb, ncovhist, nnotdet, chinr, sharpnr, scorr, sky,
maxmag_so_far
```

## Status

Environment set up, model + reference code vendored, data downloaded.
Next: write the actual inference + metrics script (mirroring
`reference/bts_val.py`'s methodology — label vs. thresholded prediction,
ROC curve, TP/FP/TN/FN masks) and run it against the real test split.
