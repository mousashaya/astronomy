"""Reproduce BTSbot's own published ZTF test-set numbers (Rehemtulla et al.
2024: 94.1% accuracy, 100% completeness, 84-93% purity), as a validation
step before ever pointing this model at new (LSST) data — see README.md
for why this order of operations matters.

Two things were verified by hand before writing this (see conversation/
project notes, not repeated as code comments here since they're one-time
verification facts, not things this script itself checks):
  - Published test_triplets images are already L2-normalized (checked:
    np.linalg.norm per channel == 1.0 exactly) -- fed to the model as-is.
  - Metadata needs no external normalization -- BatchNormalization is the
    first layer inside the model itself, using its own learned stats.
"""
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.metrics import roc_auc_score, roc_curve

if sys.platform == "darwin":
    tf.config.set_visible_devices([], "GPU")  # BTSbot's own README notes M1 GPU issues

DATA_DIR = Path("/Volumes/Machine Learning/astronomy/data/btsbot")
MODEL_DIR = Path("btsbot_eval/models/v1.0.1_best_model")
RESULTS_DIR = Path("btsbot_eval/results")
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

# Exact order from BTSbot's own usage example -- order matters, this is
# what the model was trained on.
METADATA_COLS = [
    "sgscore1", "distpsnr1", "sgscore2", "distpsnr2", "fwhm", "magpsf",
    "sigmapsf", "chipsf", "ra", "dec", "diffmaglim", "ndethist", "nmtchps",
    "age", "days_since_peak", "days_to_peak", "peakmag_so_far", "new_drb",
    "ncovhist", "nnotdet", "chinr", "sharpnr", "scorr", "sky", "maxmag_so_far",
]

# Published numbers (Rehemtulla et al. 2024) to compare our reproduction against.
PUBLISHED = {"accuracy": 94.1, "completeness": 100.0, "purity_range": (84.0, 93.0)}

THRESHOLD = 0.5  # standard cutoff; report a couple of others too for context


def main():
    print("Loading test metadata and images...")
    cand = pd.read_csv(DATA_DIR / "metadata_v10" / "test_cand_v10_N100_programid1.csv")
    trips = np.load(DATA_DIR / "test_triplets_v10_N100_programid1.npy", mmap_mode="r")
    assert len(cand) == len(trips), f"row count mismatch: {len(cand)} vs {len(trips)}"
    print(f"{len(cand)} alert-level rows, {cand['objectId'].nunique()} unique objects")

    metadata = cand[METADATA_COLS].to_numpy(dtype="float32")
    images = trips[:].astype("float32")  # full read now, not mmap -- we're using all of it

    print("Loading model and running inference...")
    sm = tf.saved_model.load(str(MODEL_DIR))
    sig = sm.signatures["serving_default"]

    t0 = time.time()
    # Batch in chunks to keep memory bounded, not because speed requires it
    # (already measured: ~1ms/example, so batching is just good hygiene).
    batch_size = 2000
    scores = []
    for i in range(0, len(cand), batch_size):
        out = sig(
            triplet=tf.constant(images[i:i + batch_size]),
            metadata=tf.constant(metadata[i:i + batch_size]),
        )
        scores.append(out["fc_out"].numpy().flatten())
    scores = np.concatenate(scores)
    print(f"Inference done in {time.time()-t0:.1f}s")

    cand = cand.copy()
    cand["raw_score"] = scores
    cand["predicted"] = (scores >= THRESHOLD).astype(int)
    labels = cand["label"].to_numpy(dtype=int)
    preds = cand["predicted"].to_numpy()

    # --- Per-alert metrics ---
    accuracy = 100 * np.mean(preds == labels)
    TP = np.sum((labels == 1) & (preds == 1))
    TN = np.sum((labels == 0) & (preds == 0))
    FP = np.sum((labels == 0) & (preds == 1))
    FN = np.sum((labels == 1) & (preds == 0))
    completeness = 100 * TP / (TP + FN) if (TP + FN) else float("nan")
    purity = 100 * TP / (TP + FP) if (TP + FP) else float("nan")
    auc = roc_auc_score(labels, scores)

    # --- Per-object metrics: does the object ever get flagged, using its
    # best (max) score across all its alerts -- the natural per-object
    # aggregation, since BTS only needs ONE alert to trigger a save ---
    obj = cand.groupby("objectId").agg(label=("label", "max"), best_score=("raw_score", "max"))
    obj["predicted"] = (obj["best_score"] >= THRESHOLD).astype(int)
    obj_labels = obj["label"].to_numpy(dtype=int)
    obj_preds = obj["predicted"].to_numpy()
    obj_accuracy = 100 * np.mean(obj_preds == obj_labels)
    oTP = np.sum((obj_labels == 1) & (obj_preds == 1))
    oFP = np.sum((obj_labels == 0) & (obj_preds == 1))
    oFN = np.sum((obj_labels == 1) & (obj_preds == 0))
    obj_completeness = 100 * oTP / (oTP + oFN) if (oTP + oFN) else float("nan")
    obj_purity = 100 * oTP / (oTP + oFP) if (oTP + oFP) else float("nan")

    # --- Threshold sensitivity, since purity is threshold-dependent ---
    threshold_sweep = []
    for t in [0.3, 0.5, 0.7, 0.9]:
        p = (scores >= t).astype(int)
        tp = np.sum((labels == 1) & (p == 1))
        fp = np.sum((labels == 0) & (p == 1))
        fn = np.sum((labels == 1) & (p == 0))
        c = 100 * tp / (tp + fn) if (tp + fn) else float("nan")
        pu = 100 * tp / (tp + fp) if (tp + fp) else float("nan")
        threshold_sweep.append((t, c, pu))

    # --- Report ---
    report = []
    report.append("=" * 70)
    report.append("BTSbot v1.0.1 reproduction -- ZTF published test set")
    report.append("=" * 70)
    report.append(f"\n{len(cand)} alerts, {len(obj)} unique objects, threshold={THRESHOLD}")
    report.append(f"TensorFlow {tf.__version__}, run {time.strftime('%Y-%m-%d %H:%M')}")
    report.append("\n--- Per-alert (matches paper's likely unit) ---")
    report.append(f"{'Metric':<15}{'Reproduced':<15}{'Published':<15}")
    report.append(f"{'Accuracy':<15}{accuracy:<15.2f}{PUBLISHED['accuracy']:<15.2f}")
    report.append(f"{'Completeness':<15}{completeness:<15.2f}{PUBLISHED['completeness']:<15.2f}")
    published_purity_str = f"{PUBLISHED['purity_range'][0]}-{PUBLISHED['purity_range'][1]}"
    report.append(f"{'Purity':<15}{purity:<15.2f}{published_purity_str:<15}")
    report.append(f"{'ROC-AUC':<15}{auc:<15.4f}{'0.984':<15}")
    report.append(f"\nConfusion matrix (alert-level): TP={TP} TN={TN} FP={FP} FN={FN}")

    report.append("\n--- Per-object (best score per objectId) ---")
    report.append(f"Accuracy={obj_accuracy:.2f}  Completeness={obj_completeness:.2f}  Purity={obj_purity:.2f}")
    report.append(f"Confusion matrix (object-level): TP={oTP} FP={oFP} FN={oFN}")

    report.append("\n--- Threshold sensitivity (alert-level) ---")
    report.append(f"{'threshold':<12}{'completeness':<15}{'purity':<10}")
    for t, c, pu in threshold_sweep:
        report.append(f"{t:<12}{c:<15.2f}{pu:<10.2f}")

    report_text = "\n".join(report)
    print("\n" + report_text)

    (RESULTS_DIR / "summary_report.txt").write_text(report_text)
    cand[["objectId", "candid", "jd", "label", "raw_score", "predicted"]].to_csv(
        RESULTS_DIR / "per_alert_predictions.csv", index=False
    )
    print(f"\nSaved: {RESULTS_DIR}/summary_report.txt, {RESULTS_DIR}/per_alert_predictions.csv")


if __name__ == "__main__":
    main()
