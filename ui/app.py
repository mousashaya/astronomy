"""Streamlit UI for the SN Ia pipeline — a live view of results as each
stage gets built, instead of reading terminal output.

Run with:
    streamlit run ui/app.py

Stages 1 (TNS discovery), 2 (light curve retrieval), and 3 (quality
check) exist so far. Later stages — SALT2 fitting, the Hubble diagram —
will each get their own `st.header(...)` section appended below as we
build them, so this file grows one stage at a time rather than being
rewritten each time.
"""
import sys
from pathlib import Path

# Streamlit runs this file standalone (it's not imported as part of the
# `desc_demo` package), so `src/` isn't on the import path automatically.
# Add it by hand, before importing anything from desc_demo, below.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

import streamlit as st

from desc_demo.sn_cutouts import CUTOUT_KINDS, FinkUnavailable, fetch_cutouts, render_cutout
from desc_demo.sn_discovery import find_sn_ia_candidates, naive_distance_gly
from desc_demo.sn_photometry import fetch_light_curve, plot_light_curve
from desc_demo.sn_quality import check_light_curve

st.set_page_config(page_title="DESC demo: SN Ia pipeline", layout="wide")
st.title("SN Ia pipeline — live view")

st.header("Stage 1 — TNS-confirmed candidates")
st.caption(
    "Pulls Fink's TNS cross-match catalog and filters to objects "
    "spectroscopically typed 'SN Ia', with a usable ZTF alert ID and a "
    "known redshift. See src/desc_demo/sn_discovery.py for why this "
    "particular filter was chosen over Fink's raw ML classification."
)

# A slider instead of a hardcoded number so you can see, hands-on, how the
# candidate count changes as you search through more/fewer TNS records —
# useful for building intuition before this becomes a fixed pipeline setting.
nmax = st.slider(
    "How many TNS records to search through", 1000, 50000, 20000, step=1000
)
only_available = st.checkbox(
    "Only show candidates that actually have archived Fink data",
    value=True,
    help=(
        "A TNS 'SN Ia' classification doesn't guarantee Fink archived any "
        "ZTF alert for that object — checking this filters those dead "
        "ends out upfront instead of you finding out one at a time."
    ),
)

if st.button("Run discovery"):
    # Stash in session_state so the table + dropdown selection survive the
    # reruns Streamlit triggers every time you pick something below (a
    # plain local variable would reset to empty on each of those reruns).
    # only_available's data-availability check is the slow part (network
    # calls per candidate) — the spinner covers that, not the TNS pull.
    with st.spinner("Running discovery..."):
        st.session_state["candidates"] = find_sn_ia_candidates(
            nmax=nmax, use_cache=True, only_available=only_available
        )

candidates = st.session_state.get("candidates")

if candidates is not None:
    st.success(f"Found {len(candidates)} candidates")

    # Display-only columns — grounding for the raw redshift number, not
    # part of what Stage 2+ actually consumes (that stays `candidates`,
    # untouched, so downstream code doesn't accidentally depend on a
    # column that only exists for browsing).
    display = candidates.copy()
    naive_gly = naive_distance_gly(display["f:redshift"]).round(2)
    display.insert(3, "approx distance (Gly)", naive_gly)
    display.insert(4, "approx look-back time (Gyr)", naive_gly)  # same number, see naive_distance_gly docstring
    st.caption(
        "The two 'approx' columns are the same number on purpose — at "
        "this level of approximation, light-travel distance and "
        "look-back time are identical by definition. See "
        "naive_distance_gly() in sn_discovery.py for why, and why "
        "'approx' matters here."
    )
    st.dataframe(display, width="stretch")

    # A dropdown instead of clickable table rows: Streamlit's built-in row
    # selection turned out to only trigger from a specific left-edge gutter
    # click (easy to miss, and there are open Streamlit bugs about it being
    # unreliable) — a selectbox is unambiguous, so use that instead.
    labels = candidates["f:fullname"] + " (" + candidates["f:internalname"] + ")"
    picked = st.selectbox("Pick a candidate to view", options=labels, index=None)

    if picked is not None:
        row = candidates.iloc[labels.tolist().index(picked)]
        object_id = row["f:internalname"]

        st.header(f"Cutouts — {row['f:fullname']} ({object_id})")
        st.caption(
            "Science = the actual exposure. Template = the reference image "
            "Fink subtracts off. Difference = Science − Template — this is "
            "what actually triggered the alert."
        )

        try:
            with st.spinner(f"Fetching cutouts for {object_id}..."):
                cutouts = fetch_cutouts(object_id)
        except FinkUnavailable:
            cutouts = None  # distinct from {} — see the branches below

        if cutouts is None:
            st.error(
                "Fink's API didn't respond in time — its infrastructure can "
                "be slow or overloaded, independent of whether this object "
                "has data. Try the same candidate again in a moment before "
                "assuming it's empty."
            )
        elif not cutouts:
            st.warning(
                "Fink has no archived alerts for this object, so there's no "
                "cutout to show — it likely faded before Fink started "
                "archiving ZTF data (Nov 2019). Try another candidate."
            )
        else:
            columns = st.columns(len(CUTOUT_KINDS))
            for col, kind in zip(columns, CUTOUT_KINDS):
                with col:
                    st.caption(kind)
                    st.image(render_cutout(cutouts[kind]), width="stretch")

        st.header(f"Light curve — {row['f:fullname']} ({object_id})")
        st.caption(
            "Every archived alert for this object, not just the newest "
            "one — magnitude vs. time, one color per band. A real SN Ia "
            "fades within a few months; a light curve spanning years is "
            "a sign this position has other, unrelated variability mixed "
            "in (see src/desc_demo/sn_photometry.py's module docstring)."
        )

        light_curve = fetch_light_curve(object_id)
        if light_curve.empty:
            st.warning("No photometry available for this object.")
        else:
            span_days = light_curve["time"].max() - light_curve["time"].min()
            st.write(
                f"{len(light_curve)} points across "
                f"{sorted(light_curve['band'].unique())}, spanning "
                f"{span_days:.0f} days (first point to last — NOT how "
                f"densely it was sampled in between, see below)"
            )
            st.pyplot(plot_light_curve(light_curve, title=row["f:fullname"]))

            st.markdown(
                "**Column reference**\n"
                "- `time` — MJD (days since a fixed reference date, astronomy's plain day-counter)\n"
                "- `band` — ztfg (green) / ztfr (red) / ztfi filter used\n"
                "- `flux`, `fluxerr` — brightness on our own internal scale; what the SALT2 fit will actually use, not a physical unit\n"
                "- `zp`, `zpsys` — the fixed reference point (25.0, AB system) flux is expressed relative to — same for every row by design\n"
                "- `mag`, `magerr` — the real, physically-calibrated apparent magnitude — what's actually plotted above\n"
                "- `rb` — real-bogus score (0-1): ZTF's own confidence this detection is a genuine source, not an artifact; higher is more trustworthy"
            )
            st.dataframe(light_curve, width="stretch")

            st.header("Stage 3 — Quality check")
            st.caption(
                "Every threshold here was picked against real objects we "
                "pulled and looked at, not chosen abstractly — see "
                "src/desc_demo/sn_quality.py's module docstring for the "
                "specific test cases that locked these numbers in."
            )
            quality = check_light_curve(light_curve)
            if quality.is_fittable:
                st.success("Passes all checks — worth handing to Stage 4's SALT2 fit.")
            else:
                st.error("Not fittable:\n" + "\n".join(f"- {r}" for r in quality.reasons))
