#!/usr/bin/env python
"""Slowly, politely pull light curves for a much larger candidate pool
than we've used interactively so far, caching everything to disk (see
sn_photometry.fetch_light_curve's new caching) so a future Hubble-diagram
run just reads local files instead of re-hitting Fink for everything.

Meant to run unattended (overnight, while away from the machine) — safe
to interrupt and rerun: already-cached objects are skipped near-instantly,
so a rerun just continues from wherever it left off.

Deliberately sequential, not parallel, and paced with a delay between
requests — Fink is free, public, shared infrastructure, not something to
hammer just because our own hardware could technically go faster.
"""
import sys
import time

# Python buffers stdout when it's not a terminal (e.g. redirected to a log
# file) -- without this, progress wouldn't actually appear until the
# buffer filled or the script exited, defeating the entire point of a
# script meant to be watched via `tail -f` while running unattended.
sys.stdout.reconfigure(line_buffering=True)

from desc_demo.sn_discovery import find_sn_ia_candidates
from desc_demo.sn_photometry import _cache_path, fetch_light_curve
from desc_demo.sn_cutouts import FinkUnavailable

NMAX = 200_000          # Fink's TNS resolver caps out around here (see sn_discovery.py)
DELAY_SECONDS = 0.3      # politeness pause between *network* requests (cached hits skip this)


def main():
    print(f"Pulling up to {NMAX} TNS records and filtering to available SN Ia candidates...")
    print("(this first step can itself take a minute or two on a cold cache)")
    candidates = find_sn_ia_candidates(nmax=NMAX)
    total = len(candidates)
    print(f"\n{total} candidates to process\n")

    fetched, cached, failed = 0, 0, 0
    start = time.time()

    for i, (_, cand) in enumerate(candidates.iterrows(), start=1):
        object_id = cand["f:internalname"]
        already_cached = _cache_path(object_id).exists()

        try:
            lc = fetch_light_curve(object_id)
        except FinkUnavailable as exc:
            failed += 1
            print(f"[{i}/{total}] {object_id}: FAILED ({exc}) -- will retry on next run")
            continue

        if already_cached:
            cached += 1
        else:
            fetched += 1
            time.sleep(DELAY_SECONDS)  # only pace real network calls, not cache hits

        # Progress every single object, not batched -- this is meant to be
        # watched, per the whole point of running it visibly.
        elapsed = time.time() - start
        status = "cached" if already_cached else "fetched"
        print(f"[{i}/{total}] {object_id} ({cand['f:fullname']}): "
              f"{status}, {len(lc)} points -- "
              f"{fetched} fetched / {cached} already cached / {failed} failed, "
              f"{elapsed:.0f}s elapsed")

    print(f"\nDone. {fetched} newly fetched, {cached} already cached, {failed} failed.")
    print(f"Total time: {time.time()-start:.0f}s")
    print("Failed ones (if any) will just be retried next time this script runs.")


if __name__ == "__main__":
    main()
