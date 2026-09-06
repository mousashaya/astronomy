# Roman & Rubin: Pathways to Involvement + a Graduate-Level Astronomy Reference

**Purpose.** Two things in one document:

1. **Part I — Pathways.** A map of the routes by which an unaffiliated software/data
   engineer can get close to the Nancy Grace Roman Space Telescope and the Vera C.
   Rubin Observatory / LSST — from pure infrastructure work to small pieces of
   science. Many routes, with honest assessment of each. Meant to be slept on.

2. **Part II — Astronomy background.** A dense, self-contained reference to build the
   astronomy knowledge these projects assume. Written for someone with a strong
   math / physics / software background and a weak astronomy background. The
   teaching content is in the text: definitions, equations, physical meaning,
   measurement practice, dominant systematics, and why each survey cares. External
   links are "go deeper" pointers and a bibliography, never required reading to
   follow the argument.

Audience: me. Living document — annotate freely.

Last substantive update: 2026-08-31.

---

# PART I — PATHWAYS TO INVOLVEMENT

## 1. The landscape: who actually runs what

You cannot navigate the pathways without a mental model of the institutions,
because "joining Roman" or "joining Rubin" is never one thing.

### Rubin / LSST

- **Rubin Observatory** — the facility on Cerro Pachón, Chile. Operated by
  **NSF NOIRLab** (the telescope) and **DOE / SLAC** (the camera and the US Data
  Facility). Construction was NSF + DOE; operations are a joint NSF–DOE program.
- **Data Management (DM)** — the group (centered at SLAC, Princeton, University of
  Washington, and NOIRLab) that builds the **LSST Science Pipelines** ("the
  Stack"), the Butler data-access middleware, the alert-production system, and the
  Rubin Science Platform. This is the software organization. Its code is public on
  GitHub under the `lsst` org; its process is open (RFCs, a public Discourse forum,
  a public Jira).
- **The eight LSST Science Collaborations** — independent, self-governing
  communities of researchers, *not* part of the Observatory:
  1. **DESC** — Dark Energy Science Collaboration (weak lensing, clustering, SNe,
     clusters; the 3×2pt cosmology program).
  2. **TVS** — Transients and Variable Stars.
  3. **SSSC** — Solar System Science Collaboration.
  4. **Galaxies**.
  5. **SMWLV** — Stars, Milky Way, and Local Volume.
  6. **AGN** — Active Galactic Nuclei.
  7. **ISSC** — Informatics and Statistics Science Collaboration. *This is the
     methods/software-facing one.*
  8. **SLSC** — Strong Lensing Science Collaboration.
  Each sets its own membership rules. Some evaluate primarily for research
  engagement; others admit "builders" (people who contribute software, pipelines,
  simulations, infrastructure) on roughly equal footing.
- **LSST Discovery Alliance** (formerly LSST Corporation / LSSTC) — a non-profit of
  member institutions. Runs education/workforce programs, the Enabling Science
  grants, hack weeks, and the Data Science Fellowship Program. Not a data-rights
  authority, but a community and funding node.
- **LINCC** — LSST Interdisciplinary Network for Collaborative Computing. Its
  engineering arm, **LINCC Frameworks**, is a funded partnership between the DiRAC
  Institute (UW) and the McWilliams Center for Cosmology (CMU) that builds
  open-source, scale-out analysis tools for LSST (LSDB, HATS, `nested-pandas`,
  etc.). Explicitly community-oriented, runs "incubators" with outside
  contributors. **A strong, under-appreciated entry point for you.**
- **Community brokers** — independent systems that ingest the full Rubin alert
  stream and add value (classification, cross-match, filtering): ALeRCE, ANTARES,
  Fink, Lasair, Pitt-Google, BABAMUL, and others. Several (Fink especially) accept
  external contributions of "science modules."

**Data rights.** LSST survey data carry a proprietary period (a rolling ~2-year
embargo; alerts are public immediately, but the associated catalogs/images are
restricted). Access is granted to scientists at US institutions, at Chilean
institutions, and to international partners who made an approved **in-kind
contribution** (software, compute, personnel, or observing resources). An
individual with no institutional data-rights allocation cannot get full catalog
access by asking. **The alert stream and the Data Previews are exceptions — those
are open to anyone.**

### Roman

- **NASA Goddard Space Flight Center (GSFC)** — mission management; the Mission
  Operations Center.
- **Space Telescope Science Institute (STScI)** — the **Science Operations Center
  (SOC)**: observation scheduling, Wide Field Instrument data processing, and the
  archive (through MAST). Builds `romancal` and the data-model / simulation stack.
- **IPAC / Caltech** — the **Science Support Center (SSC)**: processing for the
  survey-level science products (the time-domain surveys in particular), community
  support, the microlensing and time-domain pipelines, and the IRSA archive.
- **JPL** — the Coronagraph Instrument.
- **Project Infrastructure Teams (PITs)** — competitively selected (NASA ROSES,
  2023), funded teams that build the analysis infrastructure for each Core
  Community Survey:
  - **HLWAS PIT** — High Latitude Wide Area Survey (cosmology: lensing,
    clustering, clusters).
  - **HLTDS / Supernova PIT** — High Latitude Time Domain Survey (SN Ia
    cosmology). **The closest match to what you have already built.**
  - **GBTDS PIT** — Galactic Bulge Time Domain Survey (microlensing exoplanets).
  You cannot "join" a PIT — the teams were selected. But their code is developed
  in the open, and PITs have affiliate / associate tiers and take outside
  contributions. Being useful on their GitHub is the route in.
- **The Roman community** — open mailing lists, community forums, science working
  groups, community workshops, and the Roman Research Nexus (the cloud science
  platform). Sign-up is open. This is the umbrella you already found.

**Data rights.** None. No proprietary period. Everything becomes public through
MAST and IRSA once processed and validated. This is the structural reason Roman is
the easier target for you.

---

## 2. Pathway families at a glance

| # | Pathway | Gatekeeping | Effort to first contact | Effort to "meaningful dialogue" | Unlocks | Fit for you |
|---|---------|-------------|--------------------------|-------------------------------|---------|-------------|
| A | Open-source infrastructure contribution | None (public repos) | Low | Medium (weeks–months of PRs) | Credibility, working relationships, co-authorship on software papers | **Very high** |
| B | Community membership & working groups | Low (Roman) / Medium (LSST SCs) | Low | Medium | Telecons, mailing lists, a seat where decisions are discussed | **High** |
| C | Institutional affiliation / data-rights sponsor | High (needs a person to sponsor) | Medium (cold outreach) | Medium | LSST proprietary data; formal collaboration membership | Medium |
| D | Employment / funded role | High (hiring bar) | Medium | n/a (you're in) | Everything, automatically | Medium (semi-retired; contract possible) |
| E | Small science | Medium (needs a result + a venue) | Medium | Medium | Publications, a research identity | Medium–High |
| F | Relationship building (conferences, sprints, direct engagement) | None | Low–Medium | Low once you show up with work | The actual goal: a group or person you're in dialogue with | **High** |

The families are not exclusive. A realistic trajectory threads several: A + B + F
running in parallel, feeding E opportunistically, with C or D as a later
possibility if you want it.

---

## 3. Pathway A — Open-source infrastructure contribution

This is the path with no gate. Anyone can clone the repo, read the code, file an
issue, and open a pull request. In these communities, **the GitHub issue tracker
and PR review threads *are* the "meaningful dialogue"** — that is where
maintainers and scientists actually talk about the software. A merged PR is a
credential that does not depend on anyone's permission.

### A1. Roman calibration & data stack (STScI)

- **`romancal`** — the WFI calibration pipeline. Detector-level corrections →
  calibrated exposures → resampled mosaics → source catalogs. Built on the shared
  STScI framework `stpipe` / `stcal` / `stdatamodels`, which it has in common with
  the JWST pipeline (`jwst`). Apache-2.0. Active issue tracker. `pip`-installable;
  runnable from the shell via `strun` (no notebook).
- **`roman_datamodels`** / **`rad`** — the ASDF schemas and Python data-model
  classes for every Roman data product.
- **`romanisim`** — the image simulator. Produces Level-1/Level-2 products in the
  *real* formats, so anything you build against its output runs on real data
  later.
- **`stpsf`** (formerly `webbpsf`) — model PSFs for Roman WFI and JWST.
- **Shared substrate** — `stcal`, `stpipe`, `stdatamodels`, `asdf`,
  `asdf-astropy`, `asdf-standard`, `gwcs` (generalized WCS). Contributions here
  touch both Roman and JWST, which multiplies their value and visibility.

**Why it fits you:** this is a data-pipeline codebase with a schema/format layer,
a middleware layer, and a numerical-processing layer — your career in one
sentence. The ASDF format (below, §25) is genuinely new plumbing to learn, and
that is a data-engineering task, not an astrophysics one.

**First concrete step:** clone `romancal` and `romanisim`; run the pipeline on a
`romanisim` frame end to end; read the "good first issue" and "help wanted"
labels; reproduce one open bug and comment with a minimal repro.

### A2. Roman Supernova / time-domain infrastructure

The **Roman Supernova PIT** develops its analysis chain in the open
(`Roman-Supernova-PIT` on GitHub): image differencing, transient detection,
scene-modeling photometry, light-curve construction, SALT fitting, and the
cosmology inference. You have already built a standalone version of stages 3–6 of
exactly this chain against ZTF data. Reading their code and issues is the shortest
path from what you have to a real contribution, and it puts you in contact with
the people whose working group you want to be in.

**Adjacent, widely used:**

- **`sncosmo`** — SN light-curve fitting and K-corrections. You already use it.
  Open, takes PRs, small enough that a maintainer notices a good contribution.
- **SNANA** — the C+Python SN simulation-and-analysis framework used by both the
  Roman SN PIT and DESC. `pippin` orchestrates SNANA pipelines.
- **Difference imaging** — `PyZOGY`, `properimage`, `SFFT` (GPU), `hotpants`
  (classic). Roman and Rubin both need robust, well-tested subtraction; this is
  numerically demanding code that benefits from a performance-minded contributor.

### A3. Rubin / LSST Science Pipelines

Heavier to enter than Roman's stack — larger codebase, C++ core (`afw`), a formal
RFC process, review norms honed over a decade — but entirely open.

- **Entry-friendlier packages:** `analysis_tools` (QA plots and metrics),
  `sdm_schemas` (the Science Data Model schemas), documentation, and the many
  Python-level `pipe_tasks` steps.
- **Deeper:** `daf_butler` (data access / provenance middleware — a database and
  storage-abstraction problem, close to your background), `pipe_base` +
  `ctrl_bps` (the PipelineTask / QuantumGraph / workflow system), `ap_pipe` +
  `ap_association` (alert production — difference imaging, DIASource/DIAObject
  association, the 60-second budget), `meas_algorithms` / `meas_base` /
  `meas_extensions_*` (measurement).
- **Process:** development on GitHub (`lsst` org); design discussion via **RFCs**
  on the `community.lsst.org` Discourse forum and a public Jira
  (`rubinobs.atlassian.net`); a weekly set of open DM meetings.

**First concrete step:** install `rubin-env` (conda); work through the Data
Preview 0.2 pipeline tutorials as *scripts*; pick a small `analysis_tools` or docs
issue; introduce yourself on `community.lsst.org` in the Data Management category.

### A4. LINCC Frameworks — scale-out analysis tooling

`LSDB` (large-catalog cross-match and analysis on Dask), **HATS** (HEALPix
Adaptive Tiling Scheme — the partitioned on-disk catalog format, formerly
HiPSCat), `hats-import`, `nested-pandas` (nested/variable-length columns in a
pandas-like API — light curves attached to objects), `fibad` (ML on images at
scale). Built by a funded team that *wants* outside contributors, runs public tech
talks and incubators, and is solving exactly the "billions of rows, spatial
partitioning, time series per object" problem you have done analogues of.

**First concrete step:** watch a LINCC Frameworks tech talk; run the `LSDB`
cross-match quickstart on a public catalog; open an issue or PR on `nested-pandas`
or `hats`.

### A5. The cosmology / probe-level stack (DESC-adjacent, mostly public)

Even though DESC *membership* is gated, much of its software is public and takes
external PRs:

- **CCL** (`pyccl`) — the Core Cosmology Library. You already use it. C library +
  Python bindings; benchmark-driven; welcomes contributions.
- **TXPipe** — the 3×2pt measurement pipeline (`ceci`/`parsl` stages).
- **firecrown** — the likelihood layer connecting CCL to samplers (Cobaya,
  CosmoSIS, NumCosmo).
- **RAIL** — Redshift Assessment Infrastructure Layers: the photometric-redshift
  estimation-and-validation framework. Modular, actively built, photo-z is *the*
  weak-lensing systematic (§19, §21), and RAIL explicitly wants method
  contributions and infrastructure work.
- **SACC** (data-vector + covariance container), **Augur** (Fisher forecasting),
  **CLMM** (cluster weak lensing — you already use it), **qp** (parametrized PDFs),
  **NaMaster**/`pymaster` (pseudo-Cℓ on a cut sky), **TreeCorr** (two-point
  correlations — you already use it), **Corrfunc** (fast pair counting).

### A6. The Astropy ecosystem — the shared foundation

Both missions build on Astropy. Contributions here are the most portable
credential in the field: `astropy` core (units, coordinates, time, `io.fits`,
`wcs`, `cosmology`, `modeling`, `stats`, `timeseries`), and the coordinated
packages `photutils` (photometry), `astroquery` (archive access), `reproject`,
`ccdproc`, `specutils`, `regions`, `astropy-healpix`. Weekly public dev calls.
Well-run review process. A good `photutils` or `astroquery` PR is seen by people
across every survey.

### A7. The IVOA / Virtual Observatory layer

If you like protocol and interoperability work: `pyvo` (the Python VO client — TAP,
SIA, SSA, SODA, cone search, DataLink), and the IVOA standards themselves. Both
Rubin's RSP and IRSA expose VO services; a client-side contributor who understands
the standards is scarce and useful.

**Bottom line on Pathway A:** start here regardless of what else you do. It is the
only pathway with zero gate, it produces the credential every other pathway wants
to see, and the review threads are the dialogue you said you want.

---

## 4. Pathway B — Community membership & working groups

### B1. Roman community (open)

- Join the Roman community mailing lists / newsletter and the community forum.
- Join a **science working group** — these are open. The infrastructure /
  software / time-domain WFI group you already identified is exactly this.
- Get a Roman Research Nexus account (cloud platform; JupyterLab-fronted, but you
  can drop to a terminal, and you do not need it — MAST/IRSA downloads work fine
  for local script-based work).
- Attend the Roman community workshops (virtual attendance is normal).

**How to make it count (not just be a name on a list):**
1. Lurk first — read the list archive and sit in on two telecons before speaking.
   Learn what is decided, what is contested, what is stalled for lack of hands.
2. Introduce yourself by what you bring: "Principal software/data architect, ~40
   years — distributed databases, large-scale pipeline performance, schema design;
   recently built a full SN Ia light-curve-to-Hubble-diagram pipeline and an
   independent reproduction of the BTSbot classifier. Here to help with
   infrastructure and software." Not "I'm learning astronomy."
3. Take one small, concrete, unglamorous task and finish it well.

### B2. LSST Science Collaborations

- **ISSC** (Informatics and Statistics) — the natural home for a methods/software
  person. Statistical methodology, scalable computation, ML, visualization.
- **TVS** (Transients and Variable Stars) — broad, welcoming, and where the
  real/bogus, light-curve-classification, and brokering work lives. A good fit
  given your BTSbot work.
- **SSSC** (Solar System) — small, friendly, algorithm-heavy (orbit linking,
  detection association). Low barrier.
- **DESC** — you have already applied once via the ASU affiliation without success.
  DESC evaluates for active research engagement and requires data rights + an
  endorsement. Re-approach only with a stronger portfolio and, ideally, an internal
  advocate you met through Pathway A or F.

Most SCs have a membership application and ask for a current collaborator to
endorse you. The endorsement is easier to obtain *after* you have visible
contributions and a working relationship — which is why A and F come first.

### B3. In-kind contributions (Rubin)

Rubin's in-kind contribution program trades software / compute / effort for data
rights, but it operates at the level of institutions and recognized programs, not
individuals. Worth understanding as context; not a direct individual route.

---

## 5. Pathway C — Institutional affiliation / a data-rights sponsor

Relevant mainly for Rubin (Roman needs none of this).

### C1. What "affiliation" does and does not do

- It is a checkbox some applications require and a prerequisite for an LSST
  data-rights allocation.
- It is **not** a qualification by itself. Your existing ASU affiliate status (via
  the lichenology consortium) was already used for the DESC application and did
  not open the door — a general affiliate slot outside the astronomy unit does not
  read as research engagement, and it does not automatically confer data rights.
- It is **not** a sponsor. A sponsor is a *person* already in the collaboration
  who vouches for you.

### C2. Concrete affiliation routes

- **A faculty member at a data-rights-holding institution** agrees to sponsor you
  for a data-rights slot and/or bring you into their group. Requires cold (or
  warm) outreach with a portfolio in hand. Targets discussed previously:
  University of Arizona / Steward Observatory; ASU's School of Earth and Space
  Exploration (SESE) — where a warm-ish intro is possible because you already hold
  an ASU affiliation and do an analogous data-pipeline project for another ASU
  unit.
- **Research affiliate / visiting scholar status** at a university with a
  sponsoring professor — a formal but lightweight arrangement some departments
  offer unaffiliated researchers.
- **Membership through a broker or software team** that itself holds an allocation.

### C3. When to spend effort here

Only if you decide you specifically want Rubin *proprietary* data. If your center
of gravity is Roman (open data) plus Rubin's *public* products (alert stream, Data
Previews, eventually the public-after-embargo releases), you may never need C.
Keep it as an option, not a blocker.

---

## 6. Pathway D — Employment & funded roles

You are semi-retired and not job-hunting, but contract work is on the table, and
these roles confer everything (data rights, membership, dialogue) automatically.

- **STScI / AURA** — Roman and JWST scientific software engineers, pipeline
  developers, data analysts. STScI routinely hires software engineers without
  astronomy PhDs.
- **IPAC / Caltech** — Roman SSC, IRSA; scientific programmers and data engineers.
- **SLAC (Stanford)** — operates Rubin's US Data Facility; DM and DESC software
  roles.
- **NSF NOIRLab** — Rubin Observatory data management and operations.
- **LINCC Frameworks (CMU / UW)** — research software engineers, explicitly.
- **National labs** — Fermilab, LBNL, BNL, Argonne all have Rubin/DESC programs
  and hire scientific software staff.
- **Contract / consulting** — targeted short engagements (a performance problem, a
  schema migration, a pipeline-hardening pass) are a plausible fit for your
  profile and your stated preference.

Worth watching the AAS Job Register, the Rubin/NOIRLab and STScI careers pages,
and the LINCC Frameworks hiring announcements even if only to understand what
these organizations value.

---

## 7. Pathway E — Routes to (small) science

Your stated position: infrastructure first, but any small, honest piece of science
would be welcome. Realistic venues and forms, roughly easiest first:

### E1. Software / methods publications

- **JOSS** (Journal of Open Source Software) — a short, peer-reviewed paper about a
  software package. Free. Review happens on GitHub against clear criteria
  (substance, docs, tests, open license). Produces a citable DOI. If you build one
  genuinely useful tool — a non-notebook Roman data-access client, a light-curve
  QA library, a cross-match utility — this is a legitimate first-author
  publication squarely in your competence.
- **ADASS** (Astronomical Data Analysis Software and Systems) — the annual
  conference for exactly this work. Posters and short proceedings papers, indexed
  in ADS. Pipeline tooling, data management, archive access, performance,
  schema/format design are all in scope. Engineers present there routinely.
- **RNAAS** (Research Notes of the AAS) — ~1000 words, not peer-reviewed, citable
  DOI, indexed in ADS. The right home for "a tiny result": an independent
  reproduction, a characterized data-quality issue, a small methods comparison.
  (Requires AAS membership or a modest fee — check current policy.)

### E2. Specific candidates you are already close to

1. **The completed BTSbot ZTF reproduction**, written up as an independent
   reproduction note (ROC-AUC 0.9864 vs. published 0.984), with the silent-failure
   traps documented (pre-applied L2 normalization; BatchNorm baked into the model).
   Independent reproductions are under-published and genuinely valued. RNAAS-shaped
   as it stands.
2. **BTSbot (or any ZTF-trained classifier) evaluated on OpenUniverse Roman+Rubin
   simulations** — cross-survey transfer is an open question the BTSbot authors
   themselves named as future work. A careful, small-N, honestly-caveated result
   is RNAAS or a short paper; contacting the authors first turns it from potential
   duplication into collaboration.
3. **A non-notebook Roman data-access client** (pyvo/astroquery wrapper + CLI) →
   JOSS.
4. **The multi-domain alert-stream schema design** (survey-agnostic
   `objects`/`alerts` core + domain-specific extension tables) → ADASS poster.
5. **A characterized data-quality finding** — e.g., the duplicate-TNS-name /
   cross-matched-under-two-IDs issue you already hit — written up with the
   detection method and incidence rate. Cross-match methodology is your
   lichenology-consortium background applied directly; RNAAS or a methods note.

### E3. Co-authorship via infrastructure

Large-collaboration papers list infrastructure contributors as authors. If you are
on a pipeline team and your code is in the analysis, you are on the paper. This is
the most reliable way your name ends up on a *science* paper, and it does not
require you to have produced the science claim.

### E4. "Builder science" — the sweet spot

Empirical, methodical work that needs rigor rather than deep theory and is
genuinely useful: measuring the completeness and purity of a selection;
characterizing a classifier's performance on a new domain; validating a simulation
against real data; quantifying a systematic; benchmarking a method. These are
publishable, they play to your strengths, and they are the natural output of
infrastructure work done carefully.

### E5. What is not realistic

A solo, first-author cosmology-parameter paper — new dark-energy constraints and
the like. Not because you cannot run the analysis, but because surviving referee
review on a novel science *claim* requires collaboration-internal context on
systematics and priors, and an unaffiliated solo author is scrutinized hard. You
have already agreed the science lane is not the goal; this is just the boundary of
Pathway E.

---

## 8. Pathway F — Building the relationships ("meaningful dialogue")

This is the actual objective; A–E are substrates for it. What produces a group or a
person you are genuinely in dialogue with:

- **GitHub as the venue.** Sustained, high-quality issue and PR activity on one or
  two repos *is* an ongoing technical conversation with the maintainers. Pick one
  or two, go deep, become a known handle.
- **Telecons and mailing lists.** Join, lurk to learn the vocabulary and the live
  questions, then contribute where you have something concrete.
- **Conferences and workshops** — where sponsorships and collaborations actually
  get arranged:
  - **ADASS** — annual; the software/data crowd; a poster puts you in the room.
  - **AAS meetings** — January and June; huge; splinter sessions for Rubin and
    Roman.
  - **Rubin Community Workshop** — annual; sessions on pipelines, brokers, science
    collaborations.
  - **Roman community workshops / conferences** — mission news, survey definition,
    infrastructure.
  - **`.Astronomy` (dotastro)** — the astro-software-culture unconference; small,
    high-signal for tool builders.
  - **SciPy / PyData** — if you present an astro tool.
- **Hack weeks and sprints** — LSST Discovery Alliance / LINCC hack weeks, Astropy
  coordination meetings, broker sprints. Days of co-working with practitioners;
  relationships form fast.
- **Office hours** — Rubin's Community Engagement Team runs them; Astropy has open
  dev calls; `romancal` has community engagement channels.
- **Write in public.** A short blog on each piece of work (the BTSbot
  reproduction, the Roman pipeline notes) creates a surface people find and
  reference.
- **Follow one person's work closely** and engage substantively over months — read
  their papers and code, comment usefully, ask sharp questions. That is how a
  single sustained dialogue starts.

---

## 9. How the pathways connect

They are not alternatives. The dependency structure:

```
        Pathway A (open-source contribution)   Pathway F (show up: telecons,
              |         |                              conferences, sprints)
              |         |                       /            |
     builds credential  |            builds relationships    |
              |         |            /                       |
              v         v           v                        |
   Pathway B (working groups, SC membership) <--- endorsement from people
              |                                     met via A and F
              v
   opportunities for Pathway E (small science, co-authorship)
              |
              v
   optionally Pathway C (a sponsor offers affiliation / data rights)
   or Pathway D (a role opens up) --- if you want them
```

- **A and F are the engine.** Do them in parallel, immediately, with no
  permission required.
- **B follows** naturally once A and F have made you a known, useful contributor.
- **E is opportunistic** — take the small-science opening when infrastructure work
  surfaces one.
- **C and D are optional endpoints**, pursued only if you decide you want Rubin
  proprietary data or a paid engagement.

---

## 10. Honest assessment of the bottlenecks

- **The technical work is not the bottleneck.** You can do the infrastructure work
  alone, on your own schedule, starting now.
- **The astronomy-knowledge gap is real but bounded.** It is a vocabulary and
  domain-context gap, not a raw-ability gap. Part II is sized to close it. Expect
  a few months of steady study alongside the coding.
- **The social bottleneck is the hard one.** Getting a specific person to know your
  work, trust it, and advocate for you depends on other people's attention and
  bandwidth. It involves non-responses and slow threads. It is helped enormously
  by the pre-operational timing (working groups are doing foundational
  infrastructure work now and have bandwidth to onboard), but it still takes
  months and some rejection. Budget patience, not just effort.
- **Roman lowers every bar relative to Rubin** — no data rights, open pipelines,
  younger community still forming its infrastructure. If you want the shortest path
  to "in dialogue with a group," Roman is it.

---

## 11. One opinionated sequencing (to sleep on, not to commit to)

**Months 0–1**
- Work through Part II §§13–16 and §§23–26 (conventions, measurement, time domain,
  both data systems). Enough to read the code and the telecon agendas.
- Clone `romancal`, `romanisim`, `roman_datamodels`; run the pipeline on simulated
  data end to end as scripts; get fluent in ASDF.
- Join the Roman mailing lists and the infrastructure/software/time-domain working
  group. Lurk.

**Months 1–3**
- Pick one repo (`romancal`, a Roman SN PIT repo, `sncosmo`, or a LINCC Frameworks
  package). Fix one real "good first issue." Then a second, slightly bigger one.
- Introduce yourself in the working group with the credential-forward framing.
- Port your SN Ia stages 4–6 onto simulated Roman light curves (SNANA or Roman SN
  PIT sims). Port your BTSbot harness onto OpenUniverse cutouts.
- Study Part II §§17, 19–22 (SN Ia cosmology, galaxies/photo-z, cosmology, lensing,
  astro statistics).

**Months 3–6**
- Turn one of the ported analyses into an RNAAS note or an ADASS abstract.
- Have three or more merged PRs on one project; become a recognized handle there.
- From that relationship, ask about affiliate status on the associated team, or an
  endorsement for the relevant LSST Science Collaboration (ISSC or TVS).
- Attend one workshop (virtual is fine); present the poster if the abstract lands.

**Beyond 6 months (real data arriving)**
- You are an embedded contributor before the operational rush, not someone trying
  to break in during it.
- Decide then whether you want Pathway C or D.

---

# PART II — GRADUATE-LEVEL ASTRONOMY BACKGROUND

## 12. Orientation: what you actually need, and why

You are not trying to become an observational astronomer or a theorist. You are
trying to (a) read the pipeline code and the science requirements documents
without a dictionary, (b) hold a technical conversation with the scientists whose
infrastructure you are building, and (c) recognize when a data-quality problem is
astrophysically meaningful. That defines the syllabus.

The knowledge splits into four layers, in rough priority order for you:

1. **Conventions and the measurement chain** (§§13–16, 22). Coordinates, time,
   magnitudes, flux, filters, PSF, noise, detectors, photometry, astrometry,
   difference imaging, the statistics idioms. This is 80% of the vocabulary gap and
   it is where your physics background transfers almost directly. Highest ROI.
2. **The survey and data-system particulars** (§§23–27). What Rubin and Roman
   actually are, how their data flows, what the products are, what the formats are,
   how the pipelines are structured. Directly job-relevant; learn it early.
3. **The science domains** (§§17–21). SN Ia cosmology, microlensing, galaxies and
   photometric redshifts, large-scale structure, cosmology, gravitational lensing.
   Go as deep as the pathway you choose demands — time-domain depth for the SN /
   broker route, cosmology + lensing depth for the 3×2pt route.
4. **Theory backfill**. General relativity for lensing and FRW cosmology; radiative
   processes; stellar and galaxy astrophysics. Pull in as needed; do not
   front-load.

A note on units. Astronomy uses **CGS** almost everywhere (erg, cm, g, Gauss),
plus a thick layer of custom units: the parsec, the astronomical unit, the solar
mass / luminosity / radius, the Jansky, the magnitude (a logarithmic unit), the
Ångström, the year, the electron-volt for particle energies. `astropy.units`
exists because of this. Internalize the parsec (3.086×10¹⁸ cm ≈ 3.26 light-years),
the AU (1.496×10¹³ cm), the solar mass (1.989×10³³ g), and the Jansky
(10⁻²³ erg s⁻¹ cm⁻² Hz⁻¹).

---

## 13. Astronomical conventions and the measurement vocabulary

### 13.1 Position on the sky

The sky is treated as a unit sphere (the *celestial sphere*). A direction is two
angles. The systems you will meet:

- **Equatorial (RA, Dec).** Right Ascension α (like longitude, measured eastward,
  usually in hours: 24ʰ = 360°, so 1ʰ = 15°) and Declination δ (like latitude,
  −90° to +90°). The reference plane is the projection of Earth's equator; the
  zero of RA is the *vernal equinox*. Because Earth precesses, you must specify an
  **epoch/equinox**: modern data use **ICRS** (International Celestial Reference
  System), a fixed, non-rotating frame defined by distant quasars, aligned to
  within milliarcseconds of equatorial **J2000.0**. Treat "ICRS" and "J2000
  equatorial" as interchangeable for survey work unless you are doing
  milliarcsecond astrometry.
- **Galactic (l, b).** Longitude l around the Milky Way plane from the Galactic
  center, latitude b out of the plane. Used for anything Milky Way–related and for
  describing where Galactic dust extinction is bad (low |b|).
- **Ecliptic (λ, β).** Referenced to Earth's orbital plane. Natural for Solar
  System work and for describing a space telescope's field of regard (Roman, like
  JWST, can only point in an annulus roughly perpendicular to the Sun line).

**Angular separation** between two directions is the great-circle angle. For small
separations the sky is locally flat and you can use tangent-plane ("gnomonic")
coordinates, but near the poles or over large areas you must use spherical
trig or the *haversine* formula to avoid the cos δ singularity. This is a
recurring source of bugs in cross-match code.

**Angular units.** Degree → arcminute (′, 1/60°) → arcsecond (″, 1/3600°) →
milliarcsecond (mas). Rubin's pixels are 0.2″; its median delivered image quality
("seeing") is ~0.7″ FWHM. Roman WFI pixels are ~0.11″; its PSF is
diffraction-limited at ~0.07–0.1″ in the near-IR. Gaia astrometry is at the
tens-of-µas level. A useful constant: 1 radian = 206,265″.

**Solid angle** is in steradians (sr) or square degrees (1 sr = (180/π)² ≈ 3282.8
deg²). The whole sky is 4π sr ≈ 41,253 deg². Rubin's WFD survey footprint is
~18,000 deg²; Roman's High Latitude Wide Area Survey is ~2,000 deg².

### 13.2 Time

Astronomical time-keeping is a whole subsystem. The ones that matter:

- **UTC** — civil time, with leap seconds. Never do arithmetic across a leap second
  in UTC.
- **TAI** — atomic time, no leap seconds. TAI = UTC + (number of leap seconds; 37 s
  as of the mid-2020s).
- **TT** — Terrestrial Time, the timescale for geocentric ephemerides.
  TT = TAI + 32.184 s.
- **TDB** — Barycentric Dynamical Time, used for solar-system-barycentre
  ephemerides; differs from TT by ≤ ~2 ms periodic terms.
- **UT1** — tied to Earth's actual rotation angle; UTC is kept within 0.9 s of it
  (the reason for leap seconds).

**Date representations:**

- **JD** — Julian Date: continuous count of days since noon UTC, 1 Jan 4713 BC. A
  large number (~2,460,000 in the 2020s), so single-precision float loses ~seconds
  — always use float64 or split (integer + fraction) representations.
- **MJD** — Modified Julian Date = JD − 2,400,000.5. Starts at midnight. ~60,000 in
  the mid-2020s. The default in survey databases.
- **Besselian / Julian epoch** — "J2000.0" means JD 2451545.0 (TT), i.e. 2000
  Jan 1, 12:00 TT. "B1950" is the older Besselian system; you will see it in
  historical catalogs and must convert.
- **Decimal year** — e.g. 2026.66; convenient, imprecise.

**Barycentric correction.** A periodic signal (a pulsating star, an exoplanet
transit, a pulsar) must be referenced to the Solar System barycentre, not the
moving Earth, or you inject a ±8.3-minute (±1 AU / c) annual timing modulation.
The corrected quantity is **BJD** (usually BJD_TDB). `astropy.time` +
`astropy.coordinates` does this.

### 13.3 Brightness: magnitudes, flux, luminosity

This is the single most important convention block, because every catalog is full
of it and the sign convention is backwards from intuition.

**Flux density** is what a detector measures: energy per unit time per unit
collecting area per unit wavelength (Fλ, erg s⁻¹ cm⁻² Å⁻¹) or per unit frequency
(Fν, erg s⁻¹ cm⁻² Hz⁻¹). They relate by Fλ dλ = Fν dν ⇒ Fλ = Fν c/λ². The
frequency-domain unit of choice is the **Jansky**: 1 Jy = 10⁻²³ erg s⁻¹ cm⁻² Hz⁻¹
= 10⁻²⁶ W m⁻² Hz⁻¹.

**Luminosity** L is the intrinsic power output (erg s⁻¹). For an isotropic source
at luminosity distance D_L, the observed **bolometric flux** is
F = L / (4π D_L²).

**Magnitude** is a logarithmic brightness scale, defined so that a factor of 100
in flux is exactly 5 magnitudes, and **brighter objects have smaller (more
negative) magnitudes** — a 2000-year-old inherited convention. The *Pogson*
relation:

```
m = -2.5 log10(F / F_ref)
m1 - m2 = -2.5 log10(F1 / F2)
```

so Δm = 1 ⇒ flux ratio 10^(0.4) ≈ 2.512; Δm = 5 ⇒ ratio 100.

Magnitudes come in **systems** defined by the reference flux F_ref:

- **AB magnitudes** (Oke & Gunn): F_ref is a constant in Fν, chosen so that
  m_AB = −2.5 log10(Fν / 3631 Jy) = −2.5 log10(Fν [erg s⁻¹ cm⁻² Hz⁻¹]) − 48.60.
  An object with a flat Fν spectrum has the same AB magnitude in every band. This
  is what Rubin and most modern surveys use.
- **Vega magnitudes**: F_ref is the flux of the star Vega in that band, so Vega has
  m ≈ 0 in all bands by construction. Common in the near-IR (2MASS) and in older
  work. AB−Vega offsets are band-dependent and tabulated (e.g. in K band,
  m_AB ≈ m_Vega + 1.85).
- **ST magnitudes**: constant in Fλ; mostly an HST/STScI internal convention.

**Apparent vs. absolute.** Apparent magnitude m is what you observe. **Absolute
magnitude** M is what the object would have at a standard distance of 10 pc. The
difference is the **distance modulus**:

```
mu = m - M = 5 log10(D_L / 10 pc) = 5 log10(D_L / Mpc) + 25
```

For a SN Ia at z = 1, D_L ≈ 6700 Mpc, μ ≈ 44. This is the quantity a SN cosmology
pipeline ultimately produces per object, and the Hubble diagram is μ vs. z.

**Colour** is a difference of magnitudes in two bands, e.g. g − r. Because
magnitude is −2.5 log(flux), colour is a log flux ratio, i.e. a crude spectral
slope. Bluer (hotter, younger, less reddened) objects have smaller g − r.

**Two corrections you will see everywhere:**

- **Galactic extinction / reddening.** Dust in the Milky Way absorbs and scatters
  light, more at bluer wavelengths, so it both dims (extinction A_λ, in
  magnitudes) and reddens (colour excess E(B−V) = A_B − A_V). The standard
  parametrization is A_λ = R_λ · E(B−V) with a wavelength-dependent extinction
  curve; for the diffuse ISM the total-to-selective ratio R_V ≡ A_V/E(B−V) ≈ 3.1.
  E(B−V) per line of sight comes from dust maps (Schlegel–Finkbeiner–Davis 1998,
  recalibrated by Schlafly & Finkbeiner 2011). Every survey "de-reddens"
  photometry before science. Extinction is near-negligible at high Galactic
  latitude and in the near-IR — one of Roman's advantages.
- **K-correction.** Redshift moves the spectrum through your fixed filter, so the
  flux you measure in band X at redshift z does not correspond to the rest-frame
  band-X luminosity. The K-correction converts between them; it depends on the
  object's spectral shape and can be large and uncertain when a rest-frame
  ultraviolet region redshifts into an optical filter. This is precisely why Roman
  observes SNe Ia in the near-IR: at z ~ 1–2 the near-IR *is* the rest-frame
  optical, so the K-correction is small and well-calibrated. Ground-based optical
  surveys hit a wall around z ~ 1 for this reason.

**Surface brightness** is flux per unit solid angle, quoted in mag arcsec⁻². It is
distance-independent in Euclidean geometry, and *dims* as (1+z)⁴ in an expanding
universe (Tolman dimming) — an important effect for high-z galaxy photometry and a
classic cosmological test.

### 13.4 Filters and bandpasses

A photometric measurement is an integral of the source spectrum against a
**throughput curve** S(λ) — the product of atmosphere (ground only), mirrors,
optics, filter transmission, and detector quantum efficiency. Key descriptors: the
**effective wavelength** (throughput-weighted mean λ), the **bandwidth** (FWHM of
S(λ)), and whether the system is "AB" or "Vega" calibrated.

- **Rubin `ugrizy`**: six broad filters spanning ~320–1050 nm. u ~ 365 nm (hard,
  atmosphere- and detector-limited), g ~ 480, r ~ 620, i ~ 750, z ~ 870,
  y ~ 970 nm (near-IR edge of silicon).
- **Roman WFI imaging filters**: **F062** (~0.62 µm, "R"), **F087** ("z"),
  **F106** ("Y"), **F129** ("J"), **F146** — a very wide filter (~0.93–2.0 µm)
  used for the microlensing survey for maximum throughput, **F158** ("H"),
  **F184**, **F213** ("K"-ish, ~2.0–2.3 µm, the reddest). Numbers are the central
  wavelength in units of 0.01 µm.
- **Roman WFI spectroscopy**: the **grism (G150)**, slitless, resolving power
  R ~ 400–800 over ~1.0–1.93 µm, for the wide-area survey's emission-line galaxy
  redshifts; the **prism (P127)**, R ~ 70–180 over ~0.75–1.8 µm, for
  spectrophotometry of supernovae in the time-domain survey (typing and
  redshifts).

**Synthetic photometry** is computing the magnitude a given spectrum would produce
through a given bandpass: m = −2.5 log10( ∫ f_λ λ S(λ) dλ / ∫ f_λ^ref λ S(λ) dλ ).
The λ weighting appears because detectors count photons, not energy. Tools:
`synphot`/`stsynphot` (STScI), `speclite`, `sncosmo`'s bandpass machinery.

### 13.5 Spectroscopy vocabulary (light version)

- **Redshift** z: the fractional wavelength stretch of spectral features,
  1 + z = λ_obs / λ_emit. For nearby objects it is a Doppler velocity, cz ≈ v; at
  cosmological distances it is the integrated expansion of space and *not* a simple
  velocity.
- **Spectral resolution** R = λ/Δλ: R ~ 100 (prism, rough SED), R ~ 1000 (typical
  survey spectrograph, can measure redshifts from emission lines), R ~ 100,000
  (precision radial velocity).
- **Emission lines** (from hot, low-density gas: H II regions, star-forming
  galaxies, AGN narrow-line regions) vs. **absorption lines** (from cooler gas in
  front of a continuum: stellar atmospheres, the interstellar medium). Redshift
  surveys lock onto strong features: Hα 6563 Å, Hβ 4861 Å, [O III] 5007 Å,
  [O II] 3727 Å, the Ca II H&K break at 3933/3968 Å, the 4000 Å break.
- **Equivalent width** — line strength measured as the width of continuum that
  contains the same flux as the line. Distance-independent.
- **SED** — spectral energy distribution: the broadband flux vs. wavelength, i.e.
  very-low-resolution spectroscopy assembled from photometry. Photometric redshifts
  (§19) are SED fitting.

---

## 14. Radiation, detectors, and photometry

### 14.1 Thermal radiation

Most continuum light starts as approximately thermal emission. The **Planck
function** gives the specific intensity of a blackbody at temperature T:

```
B_nu(T) = (2 h nu^3 / c^2) * 1 / (exp(h nu / k T) - 1)
```

Consequences you should carry:

- **Wien's law**: the spectrum peaks at λ_max T ≈ 2.90×10⁻³ m·K. The Sun
  (T ≈ 5772 K) peaks in the optical (~500 nm). A T ≈ 3000 K red dwarf or a dusty
  torus peaks in the near-IR — Roman's band. A T ≈ 10⁷ K cluster gas emits X-rays.
- **Stefan–Boltzmann**: the bolometric flux from a blackbody surface is σT⁴, so a
  star's luminosity L = 4πR² σ T_eff⁴. This defines the **effective temperature**
  T_eff — the blackbody temperature that reproduces the star's total output.
- **Rayleigh–Jeans tail** (hν ≪ kT): B_ν ∝ ν² T. **Wien tail** (hν ≫ kT):
  exponential cutoff. Colours (§13.3) are a crude thermometer because they sample
  the slope between two points on this curve.

Non-thermal emission you will meet by name: **synchrotron** (relativistic
electrons in magnetic fields — AGN jets, radio; power-law spectrum),
**bremsstrahlung / free–free** (hot ionized gas — cluster X-rays, H II regions),
**line emission** (recombination and forbidden transitions), **inverse Compton**.

### 14.2 The detected signal and its noise

A CCD or near-IR array pixel converts incident photons to photo-electrons with
**quantum efficiency** QE(λ) (electrons per photon, ~0.7–0.9 for modern devices in
their sensitive band). The measured counts (in "ADU" / "DN", digital numbers) are
electrons divided by the **gain** (e⁻/DN).

The total electrons in a source aperture is source + background + instrument. The
noise is the quadrature sum of independent contributions, and photon arrival is
**Poisson**, so a mean of N electrons carries shot noise √N. The **CCD equation**
for the signal-to-noise ratio of a point source measured in n_pix pixels:

```
                        N_star
S/N  =  ---------------------------------------------------
        sqrt( N_star + n_pix * ( N_sky + N_dark + RN^2 ) )
```

- **N_star** — source electrons (∝ collecting area × QE × throughput × exposure
  time × source flux).
- **N_sky** — sky-background electrons per pixel. Dominates for faint sources. On
  the ground the optical night sky is bright (airglow, scattered moonlight,
  zodiacal light); from space it is much darker, but the **zodiacal light** (sunlit
  interplanetary dust) is the irreducible near-IR background for Roman and depends
  on ecliptic latitude and solar elongation.
- **N_dark** — thermally generated electrons per pixel per second × exposure; small
  for cooled detectors.
- **RN** — **read noise**, the rms electrons added by the readout amplifier per
  read, independent of signal. Sets the noise floor for short exposures.

**Regimes:** bright source → S/N ≈ √N_star (source-shot-noise limited); faint
source, long exposure → S/N ≈ N_star / √(n_pix N_sky) (background limited); faint
source, short exposure → read-noise limited. Survey exposure times are chosen to be
sky-limited (so that co-adding many exposures is efficient).

**Depth** is usually quoted as the **5σ point-source limiting magnitude** — the
magnitude at which S/N = 5. Rubin single-visit 5σ depths are r ~ 24.5; the 10-year
coadd reaches r ~ 27.5. Roman's High Latitude survey reaches ~26.5–27 AB in the
near-IR, far deeper than any wide near-IR survey before it.

### 14.3 The point-spread function (PSF)

A point source does not image to a point. The **PSF** is the system's response to a
delta-function input — the shape a star makes on the detector.

- **Diffraction limit** (space, or any aberration-free system): the PSF is an Airy
  pattern with angular scale θ ≈ 1.22 λ/D (first null). For Roman (D = 2.4 m) at
  λ = 1.5 µm, θ ≈ 0.16″ to the first null; the FWHM is ~0.1″. Sharper at bluer
  wavelengths.
- **Seeing** (ground): atmospheric turbulence smears stars into a roughly
  Gaussian/Moffat blob typically 0.5″–1.5″ FWHM, varying shot to shot. Rubin's
  median is ~0.7″. This is why space resolution is worth so much for blended
  sources and galaxy shapes.
- **Analytic models**: Gaussian (too thin-tailed), **Moffat**
  I(r) = I₀ [1 + (r/α)²]^(−β) (good wings), or a pixelized empirical model.
- **Encircled energy** / **curve of growth**: the fraction of total flux within
  radius r. Aperture photometry with a finite aperture misses the wings, so you
  apply an **aperture correction** derived from bright stars.
- **Why the PSF is a central object in survey pipelines**: PSF photometry fits the
  known PSF shape to get fluxes in crowded fields; PSF *matching* is the heart of
  difference imaging (§16); and for weak lensing the PSF must be modeled to
  sub-percent accuracy because it distorts galaxy shapes exactly like the
  cosmological signal (§21). Roman's PSF is stable (space) but undersampled (pixels
  coarser than the diffraction FWHM), which is handled by combining dithered
  exposures. Rubin's PSF varies across the 3.5° field and visit to visit.

### 14.4 Detectors: CCDs vs. near-IR arrays

**CCDs (Rubin LSSTCam: 189 devices, silicon, thick, fully depleted):**

- Charge is clocked across the device to a readout amplifier. **Charge Transfer
  Efficiency (CTE)** must be ~0.999999+; radiation damage degrades it, leaving
  trailed charge behind bright sources.
- **Brighter-fatter effect**: accumulated charge distorts the pixel boundary
  field, so bright stars' PSFs are slightly wider than faint stars' — a
  per-electron nonlinearity that must be corrected before shape measurement.
- **Full well** and **blooming**: saturated pixels bleed charge along columns.
- **Fringing**: thinned CCDs show interference fringes in the far red (z, y) from
  night-sky lines.
- **Cosmic rays**: sharp, few-pixel hits; rejected by comparing dithered
  exposures.

**Near-IR arrays (Roman WFI: 18 Teledyne H4RG-10 HgCdTe devices, 4096², 10 µm
pixels, ~2.3 µm cutoff):**

- **Non-destructive readout**: the array is sampled *up the ramp* many times during
  an exposure without clearing it (MULTIACCUM / "sample-up-the-ramp"). The pipeline
  fits a slope (count rate) per pixel to the ramp, which also lets it flag and
  reject cosmic rays *within* a single exposure (a jump in the ramp) — very
  different from CCD cosmic-ray rejection.
- **Reference pixels**: a border of light-insensitive pixels tracks and removes
  bias/thermal drift during readout.
- **Persistence / image latency**: a bright source leaves a decaying afterimage in
  subsequent exposures — a time-correlated systematic with no CCD analogue.
- **Inter-pixel capacitance (IPC)**: electronic crosstalk that convolves the image
  with a small fixed kernel, effectively part of the PSF.
- **Classical nonlinearity** and **count-rate-dependent nonlinearity
  ("reciprocity failure")**: response is not perfectly proportional to
  fluence or to flux; both are calibrated out.
- **Brighter-fatter** exists here too, via a different mechanism.

You do not need to derive these, but you must recognize them, because a large
fraction of `romancal` and the LSST ISR ("Instrument Signature Removal") code is
exactly these corrections, and a "data-quality bug" is very often one of them
misbehaving.

### 14.5 Photometry and calibration

- **Aperture photometry**: sum counts in a fixed aperture, subtract a
  background estimated from an annulus. Simple, robust, but degrades in crowded
  fields and for faint sources (aperture noise).
- **PSF photometry**: fit the (known) PSF model, scaled and positioned, to each
  source; the amplitude is the flux. Essential in crowded fields (the Galactic
  bulge, globular clusters).
- **Model photometry**: fit a galaxy profile (Sérsic, or a bulge+disk) convolved
  with the PSF.
- **Forced photometry**: measure flux at a *fixed* position (from a deep reference
  catalog) in every epoch, even where nothing is detected — how you build a light
  curve that includes non-detections and pre-explosion baseline. Central to
  time-domain science.
- **Photometric calibration**: convert instrumental magnitudes to a standard
  system. Steps: flat-fielding and gain harmonization; correcting for atmospheric
  extinction as a function of airmass (ground); tying to standard stars or, at
  survey scale, **self-calibration / übercalibration** (using repeat observations
  of the same stars across the survey to solve simultaneously for zero points and
  throughput terms); anchoring the absolute scale to spectrophotometric standards
  (often white dwarfs with model atmospheres). Rubin targets ~1% relative and
  absolute photometry; Roman similar.
- **Astrometric calibration**: solve the WCS (§15) per exposure against a reference
  catalog — now almost always **Gaia** — accounting for optical distortion, proper
  motions, parallax, and (ground) differential chromatic refraction.

---

## 15. Astrometry, world coordinate systems, and reference frames

### 15.1 The WCS: pixels ↔ sky

A **World Coordinate System** is the mapping from detector pixel (i, j) to sky
direction (α, δ). The FITS WCS standard (Greisen & Calabretta papers) factors it
into:

1. a linear step: `CRPIX` (reference pixel), `CD`/`PC` matrix + `CDELT` (scale and
   rotation) → intermediate "world" coordinates;
2. a projection: `CTYPE` like `RA---TAN` (gnomonic/tangent plane), `RA---SIN`
   (orthographic, used in radio), `RA---TAN-SIP` (TAN plus a **Simple Imaging
   Polynomial** distortion correction), or a lookup table;
3. optional higher-order distortion (SIP, or the `-TPV` convention, or a
   `-TAB`/`-TPD` table).

For wide, fast optics (Rubin's 3.5° field, Roman's 0.28° per detector across 18
detectors) the distortion polynomial is not optional — the plate scale varies
measurably across the field, and a naïve `TAN` WCS mis-locates sources by many
pixels near the edges. Rubin and Roman both use a **generalized WCS** (`gwcs`, an
Astropy-affiliated package that represents the transform as a composable pipeline
of models rather than fixed FITS keywords) internally, serialized in ASDF for
Roman.

Practical tools: `astropy.wcs` (FITS WCS, including SIP), `gwcs`, `astropy.wcs.utils`
for pixel↔world helpers, `reproject` for resampling an image onto a new WCS.

### 15.2 Proper motion and parallax

Stars are not fixed. Two motions matter at survey precision:

- **Proper motion** (µ_α*, µ_δ): the star's transverse angular velocity across the
  sky, in mas/yr (µ_α* ≡ µ_α cos δ, to make it a true angular rate). Nearby stars
  move arcseconds per decade; this must be propagated from the catalog epoch to the
  observation epoch or cross-matches fail and difference images show dipoles.
- **Parallax** (ϖ): the annual ellipse a nearby star traces because of Earth's (or
  a spacecraft's) orbital motion, with semi-major axis ϖ = 1 AU / d in the
  small-angle sense — **distance in parsecs = 1 / parallax in arcseconds** (that is
  the *definition* of the parsec). Gaia measures ϖ to tens of µas, giving distances
  to ~10% out to several kpc.

`astropy.coordinates.SkyCoord` carries `pm_ra_cosdec`, `pm_dec`, `distance`,
`radial_velocity`, and an `obstime`, and `.apply_space_motion(new_obstime=...)`
propagates the full 6-D state. Use it; hand-rolled epoch propagation is a common
bug source.

### 15.3 Reference catalogs and frames

- **ICRS** — the realized celestial frame; defined by VLBI positions of ~quasars,
  materialized for optical work by **Gaia** (Gaia-CRF3). Assume all modern survey
  positions are ICRS unless stated.
- **Gaia** (DR2, EDR3, DR3, and future DR4/DR5) — the astrometric and photometric
  backbone: positions, parallaxes, proper motions, and G/BP/RP photometry for ~1.8
  billion sources to G ≈ 21. Every ground survey calibrates astrometry and often
  photometry against Gaia. Know that it exists and what it provides.
- **Legacy frames you must convert from**: FK5/J2000 (close to ICRS, sub-arcsec
  differences), FK4/B1950 (rotating, needs proper handling — `astropy` has
  `FK4`/`FK4NoETerms`), Galactic and Ecliptic (rotations of ICRS).

### 15.4 Ground-only effects (Rubin) absent for Roman

- **Atmospheric refraction** lifts sources toward the zenith by an amount that
  depends on airmass; **differential chromatic refraction (DCR)** does it
  wavelength-dependently, so a blue star and a red star at the same true position
  land at slightly different pixels, and the offset changes with airmass — a
  spurious "astrometric variability" and a difference-imaging artifact that the
  pipeline must model.
- **Airmass** X ≈ sec(zenith angle): the path length through the atmosphere in
  units of the zenith path. Extinction ∝ X; sky brightness and seeing also degrade
  with X.
- **Scintillation**: rapid brightness flicker from atmospheric turbulence, a noise
  term for bright-star photometry.

Roman, in space, has none of these — but gains **pointing jitter**, thermal
"breathing" of the optics, and the field-of-regard constraint (it can only observe
in an annulus roughly 54°–126° from the Sun).

---

## 16. Stars, variability, and the time domain

### 16.1 The minimum stellar-astrophysics vocabulary

- **Spectral type** — the O B A F G K M sequence (hot blue → cool red), subdivided
  0–9, plus luminosity class I–V (supergiant → dwarf). The Sun is G2V. Cool dwarfs
  (M, and the L, T, Y brown-dwarf extensions) emit mostly in the near-IR — Roman
  territory.
- **The Hertzsprung–Russell diagram** — luminosity (or absolute magnitude) vs.
  temperature (or colour). Stars spend most of their life on the **main sequence**
  (core hydrogen fusion), then move to the **giant branch**, and end as **white
  dwarfs** (≲ 1.4 M_⊙, electron-degenerate), **neutron stars**, or **black holes**.
  Position on the HR diagram encodes mass and age; this is the basis of stellar
  population analysis and of using stars as distance indicators.
- **Metallicity** [Fe/H] — log abundance of elements heavier than helium relative
  to solar. A population tracer and a nuisance parameter in almost every stellar
  relation.
- **Stellar populations** — old, metal-poor Population II (halo, globular clusters)
  vs. younger, metal-rich Population I (disk). Galaxies' integrated light is a sum
  over populations; "stellar population synthesis" models (e.g. FSPS, BC03) are how
  photo-z and stellar-mass estimates are made.

### 16.2 Variability: the taxonomy a broker deals with

Time-domain surveys detect anything that changes. The pipeline and broker must
distinguish physically distinct classes with very different light curves:

**Periodic / quasi-periodic (variable stars):**

- **Pulsators** — the star's envelope oscillates:
  - **Cepheids** (classical): radial pulsation, periods ~1–100 d, obey a tight
    **period–luminosity relation** (the Leavitt Law) — the first rung of the
    extragalactic distance ladder.
  - **RR Lyrae**: horizontal-branch pulsators, P ~ 0.2–1 d, near-constant absolute
    magnitude — standard candles for the Milky Way halo.
  - **Mira / long-period variables**: cool giants, P ~ 100–1000 d, large
    amplitude, bright in the near-IR.
  - **δ Scuti, γ Doradus, etc.** — shorter-period, lower-amplitude.
- **Eclipsing binaries** — two stars orbiting in a plane near the line of sight;
  the light curve shows periodic dips. Give stellar masses and radii directly, and
  a geometric distance if you also have radial velocities.
- **Rotational variables / starspots**, **ellipsoidal variables**.

**Stochastic / secular:**

- **Cataclysmic variables** (white dwarf accreting from a companion): dwarf novae
  (recurrent outbursts of a few magnitudes), novae (thermonuclear runaway on the
  white dwarf surface, ~10 mag), and — the important one for cosmology — **Type Ia
  supernovae** (§17), the complete thermonuclear disruption of the white dwarf.
- **Young stellar objects** — irregular accretion variability.
- **AGN / quasars** — accreting supermassive black holes; aperiodic variability at
  the ~10% level on timescales of days to years, well described by a **damped
  random walk** / Gaussian process. Reverberation mapping uses the lag between
  continuum and emission-line variability to weigh the black hole.

**Explosive / one-time transients:**

- **Supernovae** — core-collapse (Types II, IIb, Ib, Ic: massive-star death;
  hydrogen present → II, stripped → Ib/Ic; plateau or linear decline; enormous
  diversity) and thermonuclear (**Type Ia**: no hydrogen, silicon absorption near
  peak, remarkably uniform; §17).
- **Kilonovae** — the optical/near-IR glow of r-process material from a neutron-star
  merger; the electromagnetic counterpart to a gravitational-wave event
  (GW170817/AT2017gfo is the archetype). Fast, red, faint; a prime Rubin+Roman
  target-of-opportunity science case.
- **Tidal disruption events (TDEs)** — a star shredded by a massive black hole;
  months-long blue flares from galactic nuclei.
- **Superluminous supernovae**, **fast blue optical transients (FBOTs)**,
  **gamma-ray-burst afterglows**, **gap transients** (luminous red novae, Ca-rich
  transients).
- **Microlensing events** (§18) — a foreground mass magnifies a background star;
  achromatic, symmetric, non-repeating.

### 16.3 Time-series analysis methods you will meet in the code

- **Lomb–Scargle periodogram** — least-squares fitting of sinusoids to
  unevenly-sampled data; the workhorse for period-finding.
  `astropy.timeseries.LombScargle`. Watch for aliasing at the sidereal day, the
  lunar month, and the survey cadence.
- **Phase folding** — once you have a period, plot flux vs. phase = (t mod P)/P to
  see the light-curve shape.
- **Box Least Squares (BLS)** — matched filter for periodic *boxcar* dips; the
  standard transit-search statistic (Roman's bulge survey will find thousands of
  transiting planets as a by-product).
- **Structure function** — rms magnitude difference as a function of time lag;
  characterizes aperiodic (AGN) variability without assuming a period.
- **Gaussian-process regression** — flexible modeling of stochastic variability
  and of light curves with gaps; `celerite2`, `george`, `sklearn`'s GP.
- **Feature extraction for classification** — amplitude, skew, periodicity
  strength, colour, rise/decline rates, host association. Packages: `feets`,
  `cesium`, `light-curve` (Rust-backed, fast, used by brokers).
- **The real/bogus problem** — before any of the above, a classifier must decide
  whether a difference-image detection is a real astrophysical source or an
  artifact (bad subtraction, cosmic ray, dipole, optical ghost, satellite streak).
  Historically random forests on hand-built features; now CNNs on the image
  triplet (science / reference / difference). Your BTSbot work is exactly this
  lineage — BTSbot goes one step further and also does the science classification
  ("is this a bright extragalactic transient worth a spectrum").

### 16.4 How a time-domain survey actually produces a light curve

1. Take an image; calibrate it (ISR, WCS, photometric zero point).
2. Subtract a deep, seeing-matched **reference/template** image of the same field
   (difference imaging, §26.4). What remains is anything that changed.
3. Detect and measure sources in the difference image → **DIASources** (Rubin's
   term): position, difference flux, shape, quality flags, real/bogus score.
4. **Associate** DIASources across epochs into **DIAObjects** (a persistent
   time-domain object) by position.
5. For each visit, also do **forced photometry** at every known DIAObject position,
   so the light curve has points (with error bars) even where nothing was detected.
6. Package the new DIASource + its DIAObject history + image cutouts + context
   (nearest static object, its photo-z, Solar-System-object check) into an **alert
   packet**, and ship it (Rubin: within 60 s, ~10 million per night, as Avro over
   Kafka to community brokers).
7. Brokers classify, filter, cross-match to external catalogs (TNS, Gaia, etc.),
   and serve the subset each science group cares about.

Roman does not run a 60-second alert stream, but the HLTDS and GBTDS pipelines do
steps 1–5 on the survey cadence and release the difference images, detections, and
light curves as data products. Transient discovery still happens; it is packaged
as periodic data releases rather than a real-time firehose.

---

## 17. Supernovae and SN Ia cosmology

This is the science your existing pipeline implements, and the core of Roman's
High Latitude Time Domain Survey. Worth knowing well.

### 17.1 What a Type Ia supernova is

A carbon–oxygen **white dwarf** in a binary is pushed toward the Chandrasekhar
mass (~1.4 M_⊙) — by accretion from a companion (single-degenerate) or by merger
with another white dwarf (double-degenerate); the progenitor question is still
open. Compressional heating ignites carbon fusion, a thermonuclear flame
(deflagration transitioning to detonation) burns much of the star to
iron-group elements in seconds, and the star is **completely unbound** — no
remnant. The light curve is powered by the radioactive decay chain
⁵⁶Ni → ⁵⁶Co → ⁵⁶Fe (half-lives 6.1 d and 77 d); the ~0.6 M_⊙ of ⁵⁶Ni synthesized
sets the peak luminosity.

Because the trigger mass and the fuel are nearly the same every time, SNe Ia are
nearly **standard candles**: peak absolute magnitude M_B ≈ −19.3 with a scatter of
only ~0.3–0.4 mag *before* correction. Spectroscopically they are identified by **no
hydrogen** and a **Si II absorption line at 6150 Å** near peak.

### 17.2 Standardization: turning "nearly standard" into "standardizable"

Two empirical correlations reduce the scatter to ~0.12–0.14 mag:

- **The Phillips relation (1993)** — light-curve shape correlates with luminosity:
  more luminous SNe Ia rise and fall *more slowly*. Parametrized historically by
  **Δm₁₅(B)** (the decline in B magnitudes in the 15 days after B-band peak);
  "broader = brighter."
- **The colour–luminosity relation** — redder SNe Ia (after light-curve-shape
  correction) are fainter, partly from host-galaxy dust, partly intrinsic.

Modern practice fits the multi-band light curve with a template model —
**SALT2 / SALT3** (Spectral Adaptive Light-curve Template; `sncosmo` implements
these) — which returns per SN:

- **x₀** — overall amplitude (→ apparent peak magnitude m_B = −2.5 log₁₀ x₀ + const);
- **x₁** — the stretch / light-curve-width parameter (the Phillips axis);
- **c** — the colour parameter (≈ rest-frame B−V excess at peak);
- plus **t₀** (time of peak) and, if the redshift is free, z.

The **Tripp (1998) estimator** turns these into a standardized distance modulus:

```
mu_obs = m_B  -  M_B  +  alpha * x1  -  beta * c   ( + gamma * host_term )
```

- **α** (~0.14) and **β** (~3.1) are nuisance parameters fit globally across the
  whole sample (not per SN).
- **M_B** is the fiducial absolute magnitude — degenerate with H₀, so SN-only
  cosmology constrains *relative* distances (Ω_m, w) unless an external absolute
  calibration (Cepheids, TRGB) is added to also get H₀.
- **The host-mass step (γ)** — after all corrections, SNe Ia in high-stellar-mass
  host galaxies are ~0.03–0.09 mag brighter than those in low-mass hosts. The cause
  (progenitor age, metallicity, dust law) is unresolved; it is handled as a step
  function of host stellar mass (threshold ~10¹⁰ M_⊙) or, increasingly, as a
  function of host colour or local star-formation rate. This is currently one of
  the leading systematics in SN cosmology and an active research area — the kind of
  thing a careful infrastructure person can contribute to characterizing.

The **Hubble diagram** is μ_obs vs. z; its shape constrains the expansion history
E(z) and hence Ω_m and the dark-energy equation of state w (§20). The 1998
discovery of accelerating expansion (Riess et al.; Perlmutter et al.) was exactly
this measurement with ~50 SNe; modern samples (Pantheon+, DES-SN, Union3) have
~1500–2000, and Roman aims for many thousands to z ~ 2–3.

### 17.3 Systematics (the part that matters for pipeline work)

- **Photometric calibration** — the dominant systematic in every modern SN survey.
  A 1% cross-band zero-point error maps almost directly into a w error. Roman's SN
  program is built around an internal calibration strategy (a stable spacecraft, a
  well-characterized detector, on-board reference sources).
- **K-corrections and the rest-frame wavelength coverage** — see §13.3. Roman's
  near-IR bands keep high-z SNe in the rest-frame optical where SALT is calibrated;
  this is the single biggest reason Roman can push to z ~ 2.
- **Selection (Malmquist) bias** — flux-limited samples preferentially catch the
  brighter SNe at each redshift, biasing μ. Corrected with large simulations
  (SNANA) via the **BEAMS with Bias Corrections (BBC)** framework
  (Kessler & Scolnic 2017).
- **Contamination** — core-collapse SNe or peculiar Ia's leaking into the sample.
  Handled with spectroscopic typing where possible, and with a
  probabilistic-classification likelihood (**BEAMS**) where not. Roman's prism
  gives a spectrum for a large fraction of its SNe.
- **Host-galaxy effects** — the mass step (above), plus host light contaminating
  the SN photometry (scene modeling / difference imaging must handle this),
  plus mis-associated hosts giving wrong redshifts.
- **Dust** — separating host-galaxy reddening (which correlates with luminosity via
  β) from intrinsic colour variation; the assumed dust law R_V and whether it
  varies host to host.
- **Peculiar velocities** — at low z, local flows perturb the redshift–distance
  relation; corrected with peculiar-velocity models.
- **Gravitational lensing** — at high z, magnification by foreground structure adds
  scatter (and skew) to the Hubble diagram; a floor Roman's high-z SNe will hit.

### 17.4 Software

`sncosmo` (light-curve fitting, SALT2/SALT3, bandpasses, K-corrections — you use
this), **SNANA** (simulation + fitting at survey scale; the SN cosmology
standard), `pippin` (SNANA pipeline orchestration), the Pantheon+/SH0ES data
products (for cross-checks), and the Roman SN PIT's own chain (difference imaging →
scene-modeling photometry → SALT → BBC → cosmology).

---

## 18. Gravitational microlensing and the Galactic Bulge survey

Roman's Galactic Bulge Time Domain Survey is a different science entirely — not
cosmology, but exoplanet demographics — and it produces an enormous stellar
variability dataset as a by-product. Worth knowing because it is a third of
Roman's core program and the pipeline problems (high-cadence, ultra-crowded-field
photometry) are distinctive.

### 18.1 The physics

A foreground mass (a star, or a star+planet) passing near the line of sight to a
background star bends its light and **magnifies** it — no spectral change
(achromatic), a smooth symmetric rise and fall, and it never repeats. The angular
scale is the **Einstein radius**:

```
theta_E = sqrt( kappa * M * pi_rel ),    kappa = 4G / (c^2 * AU) ≈ 8.14 mas / M_sun
pi_rel = AU * (1/D_lens - 1/D_source)    (the lens–source relative parallax)
```

For a solar-mass lens halfway to the bulge, θ_E ~ 0.5 mas. The **point-source,
point-lens** ("Paczyński") light curve is

```
A(u) = (u^2 + 2) / ( u * sqrt(u^2 + 4) ),   u(t) = sqrt( u0^2 + ((t - t0)/t_E)^2 )
```

where u is the lens–source separation in units of θ_E, u₀ is the impact parameter,
t₀ the time of closest approach, and **t_E = θ_E / µ_rel** the Einstein-radius
crossing time (~20 days for typical bulge events, the one directly measurable
timescale). Because t_E blends mass, distance, and relative proper motion, a single
light curve does **not** give the lens mass without extra information.

### 18.2 Planets, and why space helps

A planet orbiting the lens star creates a brief (hours-to-days) **anomaly** on the
otherwise-smooth stellar light curve when the source crosses a caustic the planet
induces. The anomaly's parameters are the planet/star **mass ratio q** and the
projected **separation s** (in θ_E). Microlensing is uniquely sensitive to
**cold, low-mass planets beyond the snow line** — the population Doppler and
transit methods miss — and even to **free-floating planets** (isolated events with
t_E of hours).

Ground-based microlensing (OGLE, MOA, KMTNet) is limited by seeing: the bulge is
so crowded that main-sequence source stars are blended below the noise. Roman,
from space at ~0.1″ resolution, resolves them, and its ~15-minute cadence in the
wide **F146** filter over six ~72-day seasons will catch the short anomalies.
Expected yield: thousands of bound planets down to sub-Earth masses, plus a
free-floating-planet census, plus — as free by-products — tens of thousands of
transiting planets, and precise light curves and astrometry for hundreds of
millions of bulge stars.

### 18.3 Second-order effects (in the modeling code)

- **Finite-source effects** — when u ≲ ρ (ρ = θ_source/θ_E), the source disk is
  resolved by the magnification pattern; the light curve deviates from the
  point-source form and you can *measure* θ_E.
- **Microlensing parallax** (π_E) — the light curve seen from two vantage points
  (Roman + ground, or Roman's own orbital motion) differs, breaking the
  mass–distance degeneracy.
- **Orbital motion of the lens binary**, **xallarap** (orbital motion of the
  *source*), **binary-source** blending — all degeneracy-inducing complications
  the fitting code must consider.
- **Degeneracies** — the classic **close/wide** (s ↔ 1/s) degeneracy in the planet
  separation, and various discrete parameter degeneracies that make the likelihood
  surface multi-modal. Fitting needs global optimizers / nested sampling, not local
  gradient descent.

### 18.4 Software

`MulensModel`, `pyLIMA`, `VBBinaryLensing` / `VBMicrolensing` (fast binary-lens
magnification), `RTModel`; the Roman GBTDS PIT pipeline (crowded-field
difference-imaging photometry at scale).

---

## 19. Galaxies, photometric redshifts, and large-scale structure

The domain behind Roman's wide-area survey and Rubin's DESC 3×2pt program.

### 19.1 Galaxies: the minimum

- **Morphology** — ellipticals / spheroids (old stars, little gas, "red and dead"),
  spirals / disks (ongoing star formation, gas, dust), irregulars, and mergers.
  Quantified by **Sérsic index n** in the profile I(r) ∝ exp(−b_n[(r/r_e)^(1/n) −
  1]): n = 1 is an exponential disk, n = 4 is the de Vaucouleurs profile of a
  classical elliptical.
- **The colour bimodality** — galaxies split into a **blue cloud** (star-forming)
  and a **red sequence** (quiescent), with a sparsely populated **green valley**
  between. Colour is a first-order redshift and stellar-population indicator, which
  is what makes photometric redshifts possible at all.
- **Scaling relations** — Tully–Fisher (disk luminosity ↔ rotation speed),
  Faber–Jackson / the fundamental plane (elliptical luminosity ↔ velocity
  dispersion ↔ size), the star-forming "main sequence" (SFR ↔ stellar mass), the
  mass–metallicity relation. These are the levers for using galaxies as
  approximate distance indicators and for sanity-checking photo-z and stellar-mass
  pipelines.
- **Luminosity / stellar-mass function** — the number density of galaxies per unit
  luminosity or mass, well fit by a **Schechter function**
  ϕ(L) dL = ϕ* (L/L*)^α exp(−L/L*) d(L/L*): a power law faint end, an exponential
  cutoff above the characteristic L*.
- **Active galactic nuclei** — a subset with an accreting central supermassive
  black hole outshining the host; broad and/or narrow emission lines, X-ray
  emission, variability, sometimes radio jets. Both a contaminant (point-like,
  variable) and a science target for Rubin's AGN collaboration.

### 19.2 Photometric redshifts — the make-or-break systematic

A spectroscopic redshift needs a spectrum and is expensive. A **photometric
redshift** ("photo-z") is a redshift estimate from broadband fluxes alone —
essentially fitting the position of spectral breaks (the 4000 Å break, the Lyman
break) as they slide through the filter set as z increases. Two families:

- **Template fitting** — fit observed fluxes against a library of redshifted
  galaxy SED templates; output a redshift posterior p(z). Codes: BPZ, EAZY,
  LePHARE, CIGALE.
- **Machine learning** — train a regressor/classifier (random forest, boosted
  trees, neural net, mixture density network) on a spec-z sample. Accurate *inside*
  the training distribution, unreliable outside it. Codes: `pzflow`, `annz`,
  GPz, and many in **RAIL**.

Why it dominates weak-lensing cosmology: the cosmological signal (§21) is measured
in **tomographic redshift bins**, and the theory prediction depends on the true
redshift distribution **n(z)** of the galaxies in each bin. A bias in the *mean*
redshift of a bin of just Δ⟨z⟩ ~ 0.002–0.01 shifts the inferred S₈ and w at the
level of the entire measurement. So the pipeline problem is not just "estimate z
per galaxy" — it is **calibrate the ensemble n(z) and its uncertainty per bin**,
using:

- **Spectroscopic training/validation sets** (always incomplete and
  non-representative at faint magnitudes — the core difficulty);
- **Clustering redshifts** ("clustering-z" / cross-correlation): infer the n(z) of
  a photometric sample by cross-correlating its positions with a
  spectroscopic reference sample of known z — spatial clustering means the
  cross-correlation amplitude vs. reference-z traces the overlap in redshift;
- **Self-organizing maps** and other methods to characterize where in
  colour–magnitude space the spec-z coverage is missing.

**Catastrophic outliers** — galaxies whose photo-z is wrong by Δz > ~0.15,
typically from a colour degeneracy (a low-z galaxy's 4000 Å break mimicking a
high-z galaxy's Lyman break). Their *fraction* and *redshift* both bias n(z).

RAIL (DESC's framework) exists to make this whole calibration-and-validation
process modular and testable — a genuine software-infrastructure problem with
direct cosmological stakes, and an area explicitly open to contributors.

### 19.3 Large-scale structure

Matter is not uniform; it forms the **cosmic web** — sheets, filaments, and knots
(clusters) around under-dense **voids** — grown by gravity from tiny primordial
density fluctuations. The statistics that compress this:

- **The two-point correlation function** ξ(r) — the excess probability, over
  random, of finding two galaxies separated by r: dP = n̄²[1 + ξ(r)] dV₁dV₂.
  Its Fourier transform is the **power spectrum** P(k).
- **Galaxy bias** — galaxies are a biased tracer of the underlying matter:
  on large scales δ_galaxy ≈ b · δ_matter, so ξ_galaxy ≈ b² ξ_matter. b is a
  nuisance parameter (scale- and redshift-dependent in detail) that must be
  marginalized or measured (galaxy–galaxy lensing breaks the b–σ₈ degeneracy).
- **Baryon acoustic oscillations (BAO)** — sound waves in the pre-recombination
  photon–baryon plasma froze in at recombination, imprinting a preferred
  clustering scale, the **sound horizon** r_d ≈ 147 Mpc (comoving). It appears as a
  bump in ξ(r) at ~100 h⁻¹ Mpc / a series of wiggles in P(k), and serves as a
  **standard ruler**: measuring its apparent size vs. redshift gives D_A(z) and
  H(z). Roman's grism redshift survey (Hα and [O III] emitters to z ~ 2–3) targets
  BAO and RSD in a redshift range ground surveys reach poorly.
- **Redshift-space distortions (RSD)** — peculiar velocities (infall toward
  overdensities) distort the clustering pattern along the line of sight
  ("Kaiser squashing" on large scales, "fingers of God" on small scales). The
  anisotropy amplitude measures the **growth rate** f σ₈(z) — a direct probe of
  how fast structure grows, which distinguishes dark energy from modified gravity
  even when they predict the same expansion history.
- **Clusters of galaxies** — the most massive bound structures (10¹⁴–10¹⁵ M_⊙);
  their **abundance as a function of mass and redshift** is exponentially sensitive
  to σ₈ and Ω_m and to the growth history. The catch is **mass calibration**:
  observable proxies (optical richness, X-ray luminosity/temperature,
  Sunyaev–Zel'dovich signal, weak-lensing shear) all need calibrating, and
  weak-lensing mass calibration (CLMM territory — you have touched this) is the
  current gold standard.

### 19.4 Modeling structure

- **Linear perturbation theory** — δ ≪ 1; each Fourier mode grows independently by
  the **growth factor D(a)**, governed by δ̈ + 2H δ̇ − 4πG ρ_m δ = 0. Growth rate
  f ≡ dln D/dln a ≈ Ω_m(a)^γ with γ ≈ 0.55 for GR+ΛCDM (γ is a modified-gravity
  diagnostic).
- **Nonlinear scales** — δ ≳ 1; handled by N-body simulations, fitting formulae
  (HALOFIT), the **halo model** (all matter in virialized halos; the
  power spectrum is a "1-halo" + "2-halo" sum), and **emulators** (Gaussian-process
  or neural interpolators trained on simulation grids — e.g. the Mira-Titan,
  Aemulus, EuclidEmulator families). CCL wraps several of these.
- **Baryonic feedback** — AGN and supernova feedback push gas around and suppress
  the small-scale matter power spectrum by up to ~20%; a major weak-lensing
  systematic on small scales, modeled by "baryonification" or by marginalizing
  over feedback parameters.

---

## 20. Cosmology: the theory Roman and Rubin exist to test

Your GR and field-theory background makes this section mostly a matter of learning
notation and which parameters the surveys constrain.

### 20.1 The homogeneous universe

The universe is, on large scales, homogeneous and isotropic (the **cosmological
principle**), so its geometry is the **Friedmann–Robertson–Walker** metric:

```
ds^2 = -c^2 dt^2 + a(t)^2 [ dr^2/(1 - k r^2) + r^2 dOmega^2 ]
```

with **scale factor** a(t) (normalized a(t₀) = 1 today) and spatial curvature
k ∈ {−1, 0, +1}. **Redshift** relates directly to expansion: 1 + z = 1/a(t_emit).

Einstein's equations reduce to the **Friedmann equations**:

```
H^2 ≡ (a_dot/a)^2 = (8 pi G / 3) rho  -  k c^2 / a^2  +  Lambda c^2 / 3
a_ddot/a = -(4 pi G / 3)(rho + 3p/c^2)  +  Lambda c^2 / 3
```

The second shows that **pressure gravitates**: a component with p < −ρc²/3 drives
**acceleration**. That is dark energy.

Write each component's density as a fraction of the critical density
ρ_crit = 3H²/8πG:

- **Ω_m** — matter (cold dark matter + baryons Ω_b); dilutes as a⁻³.
- **Ω_r** — radiation (photons + relativistic neutrinos); dilutes as a⁻⁴;
  negligible today (~10⁻⁴) but dominant in the early universe.
- **Ω_Λ** (or Ω_DE) — dark energy; constant if a cosmological constant.
- **Ω_k** — an effective curvature term, ≡ −kc²/(a₀²H₀²); Ω_m + Ω_r + Ω_Λ + Ω_k = 1
  by construction. Observations put |Ω_k| ≲ 0.001 — the universe is spatially flat
  to current precision.

The expansion history is packaged as the **dimensionless Hubble parameter**:

```
E(z) ≡ H(z)/H0 = sqrt( Om (1+z)^3  +  Ok (1+z)^2  +  Or (1+z)^4  +  ODE * f_DE(z) )
```

For a **cosmological constant**, f_DE = 1. For dynamical dark energy with equation
of state w(a) ≡ p/(ρc²), f_DE(z) = exp[3 ∫₀^z (1 + w(z')) / (1 + z') dz']. The
standard phenomenological form is **CPL / w₀wₐ**:

```
w(a) = w0 + wa (1 - a) = w0 + wa * z/(1+z)
  =>  f_DE(z) = (1+z)^(3(1 + w0 + wa)) * exp( -3 wa z/(1+z) )
```

**w₀ = −1, wₐ = 0** is ΛCDM. Roman and Rubin's headline goal is to measure
(w₀, wₐ) — i.e. is dark energy a constant, and if not, how does it evolve. (Recent
DESI + SN results have hinted at wₐ ≠ 0; confirming or refuting that is squarely
the Roman/Rubin era's job.)

### 20.2 Distances (the piece you will implement)

All from E(z). With Hubble distance D_H ≡ c/H₀:

```
Comoving (line-of-sight):   D_C(z) = D_H * integral_0^z dz' / E(z')
Transverse comoving:        D_M = D_C                       (flat, Ok = 0)
                            D_M = D_H/sqrt(Ok) * sinh( sqrt(Ok) D_C/D_H )   (open)
                            D_M = D_H/sqrt(|Ok|) * sin( sqrt(|Ok|) D_C/D_H ) (closed)
Angular diameter distance:  D_A(z) = D_M / (1 + z)
Luminosity distance:        D_L(z) = (1 + z) * D_M
Distance modulus:           mu(z) = 5 log10( D_L / 10 pc ) = 5 log10(D_L/Mpc) + 25
```

**Etherington's reciprocity relation**: D_L = (1+z)² D_A always, in any metric
theory with photon-number conservation — a testable consistency check.
**D_A is non-monotonic**: it peaks around z ~ 1.5–1.6 and *decreases* at higher z,
so the most distant galaxies subtend a larger angle than ones at z ~ 2. Hogg's
"Distance measures in cosmology" note is the canonical cheat-sheet; `astropy.cosmology`
and `pyccl` implement all of it — but you should be able to derive and code
D_C from E(z) in your sleep, because it is the kernel of the SN Hubble-diagram
likelihood.

### 20.3 The probes and how they constrain the parameters

| Probe | Primary observable | Mainly constrains |
|-------|--------------------|--------------------|
| **SNe Ia** | luminosity distance D_L(z) via standardized candles | Ω_m, w₀, wₐ (relative distances); + H₀ with an absolute anchor |
| **BAO** | standard ruler r_d imprinted on clustering → D_A(z), H(z) | expansion history, H₀ (with a sound-horizon prior), Ω_m |
| **Weak lensing (cosmic shear)** | distortion of galaxy shapes by foreground mass → matter power spectrum, geometry | S₈ ≡ σ₈√(Ω_m/0.3), w, sum of neutrino masses |
| **Galaxy clustering** | ξ(r) / P(k), RSD | Ω_m, bias, f σ₈ (growth), BAO |
| **Galaxy–galaxy lensing** | shear around lens galaxies → their mean mass profile | breaks galaxy-bias degeneracy; combined with clustering → σ₈ |
| **Cluster counts** | dn/dM/dz | σ₈, Ω_m, growth (very sensitive; mass-calibration-limited) |
| **CMB** (external: Planck, ACT, SPT) | z ≈ 1100 anisotropy | tight priors on Ω_b, Ω_m, n_s, the sound horizon; the anchor everything else is compared to |

**"3×2pt"** is the joint analysis of the three two-point functions measurable from
an imaging survey alone: cosmic shear ξ_±(θ), galaxy–galaxy lensing γ_t(θ), and
galaxy clustering w(θ). DESC's flagship analysis; Roman's HLWAS does the analogous
combination with the added depth and near-IR shape measurements, plus the grism
BAO/RSD survey.

### 20.4 The current tensions (why anyone funds these surveys)

- **The H₀ tension** — the local distance-ladder value (SH0ES: Cepheid-calibrated
  SNe Ia, H₀ ≈ 73 km s⁻¹ Mpc⁻¹) disagrees with the value inferred from the CMB
  assuming ΛCDM (Planck: H₀ ≈ 67.4) at ~5σ. Either a systematic no one has found,
  or new physics (early dark energy, extra relativistic species, …). Roman's SN
  program plus its own Cepheid/TRGB calibration is designed to stress-test the
  local ladder.
- **The S₈ / σ₈ tension** — several weak-lensing surveys (DES, KiDS, HSC) have
  measured S₈ a few percent *lower* than the CMB-extrapolated value, at ~2–3σ (with
  the significance drifting as analyses improve). Rubin/DESC and Roman weak lensing
  have the statistical power to settle whether this is real; if it is, it points to
  suppressed structure growth (massive neutrinos, dark-energy or dark-matter
  interactions, modified gravity).
- **Hints of evolving dark energy** — combinations of DESI BAO, CMB, and SN samples
  have shown mild (~2–4σ, sample-dependent) preference for w₀ > −1 with wₐ < 0.
  Independent confirmation with Roman/Rubin SNe and lensing is the headline test.

### 20.5 Inference machinery

- **Likelihood**: usually Gaussian in the data vector d given theory μ(θ) and a
  covariance C: −2 ln L = (d − μ)ᵀ C⁻¹ (d − μ) + const. The covariance itself is
  estimated from simulations, jackknife/bootstrap, or analytic models, and its
  uncertainty must be propagated (Hartlap/Sellentin–Heavens corrections).
- **Fisher forecasting** — the Gaussian approximation to the likelihood near the
  peak; F_ij = ⟨−∂²lnL/∂θ_i∂θ_j⟩; the parameter covariance is ≈ F⁻¹. Fast survey
  design and "figure of merit" calculations (the dark-energy FoM is
  1/√det Cov(w₀, wₐ)). `Augur` (DESC) does this for LSST.
- **Samplers** — MCMC (`emcee`, `zeus`), nested sampling (`dynesty`, `nautilus`,
  `PolyChord` / `MultiNest`), and gradient-based (HMC/NUTS) where the model is
  differentiable. Chains post-processed with `getdist` / `ChainConsumer`.
- **Frameworks** — CosmoSIS, Cobaya, MontePython tie together a Boltzmann code
  (**CAMB** or **CLASS**, which compute the linear power spectrum and CMB spectra
  from parameters), the nonlinear corrections, the probe-specific data vectors, the
  likelihoods, and the sampler. DESC's stack is CCL + `firecrown` + a sampler.
- **Blinding** — analyses are run with the parameter values or the data vector
  offset by an unknown amount until the pipeline and systematics budget are frozen,
  to prevent confirmation bias. Standard practice; the pipeline must support it.
- **Tension metrics** — quantifying agreement between two datasets: the parameter
  difference in units of its covariance, the "suspiciousness" statistic, evidence
  ratios. Relevant because half the science is "do probe A and probe B agree".

---

## 21. Gravitational lensing and weak-lensing measurement

The probe both missions were largely built for, and the one with the hardest
measurement problem — which is where infrastructure quality matters most.

### 21.1 The lensing formalism

Mass bends light. A mass distribution between you and a source galaxy remaps the
source plane onto the image plane. Locally, the remapping is the Jacobian

```
A = [ 1 - kappa - gamma1     -gamma2        ]
    [   -gamma2           1 - kappa + gamma1 ]
```

- **Convergence** κ — an isotropic (de)magnification. κ = Σ / Σ_crit, where Σ is
  the projected mass surface density and the **critical surface density** is

  ```
  Sigma_crit = (c^2 / 4 pi G) * D_S / (D_L * D_LS)
  ```

  (D_L, D_S, D_LS are angular-diameter distances observer→lens, observer→source,
  lens→source). κ is literally "projected mass in convenient units."
- **Shear** γ = γ₁ + iγ₂ — an anisotropic stretch: it turns a circular source into
  an ellipse. It is a **spin-2** field (invariant under 180° rotation), so it is
  naturally described on the sphere by its **E-mode** (curl-free, what
  gravitational lensing produces) and **B-mode** (divergence-free, which lensing
  produces only at tiny levels — so a measured B-mode is a systematics alarm).
- **Reduced shear** g = γ / (1 − κ) — what you actually measure, because the
  overall scale of A is unobservable (you do not know the galaxy's unlensed size).
  In the weak regime (κ, γ ≪ 1) g ≈ γ.

**Cosmic shear** is the coherent γ (~1–3% rms) imprinted on distant galaxies by
*all* the large-scale structure along the line of sight. Its two-point statistics
— ξ₊(θ), ξ₋(θ) in real space, or C_ℓ^κκ in harmonic space — depend on the matter
power spectrum integrated with a geometric lensing kernel, hence on σ₈, Ω_m, and
(through the growth and the distances) w. Measured in **tomographic photo-z bins**
so the redshift evolution adds constraining power.

**Galaxy–galaxy lensing** is the tangential shear γ_t(θ) of background sources
around foreground lens galaxies — the azimuthally-averaged signal measures the
lenses' mean projected mass profile (ΔΣ(R)). Stacked, it is high-S/N even for
individual-lens noise, and combined with clustering it breaks the galaxy
bias–σ₈ degeneracy. **Cluster weak lensing** (CLMM's domain) is the same
measurement around clusters, giving their masses for the cluster-abundance probe.

### 21.2 Shape measurement — the core engineering problem

You estimate shear from the **ellipticities** of millions of galaxies. In the weak
regime the *average* ellipticity of a population is an unbiased estimator of the
reduced shear (galaxies are randomly oriented intrinsically — mostly; see IA
below), so ⟨e⟩ ≈ g. Getting that average right to sub-percent accuracy is
brutally hard:

- **PSF dilution and anisotropy.** The PSF (§14.3) circularizes galaxies (dilutes
  the shear signal) and, if anisotropic, adds a spurious coherent ellipticity that
  mimics shear. The PSF must be modeled from stars and *interpolated* to each
  galaxy position to sub-percent accuracy in size and ellipticity. PSF modeling
  errors are a leading systematic. (`piff` is the Rubin/DES PSF modeler.)
- **Noise bias.** Ellipticity is a nonlinear function of pixel values, so pixel
  noise produces a *biased* mean even with infinite galaxies. Scales as (S/N)⁻².
- **Model bias.** Fitting a wrong galaxy profile (real galaxies are not pure
  Sérsic; they have bulges, disks, clumps, colour gradients) biases the shape.
- **Selection bias.** If detection or selection efficiency depends on orientation
  relative to the shear or the PSF, the selected sample's mean ellipticity is
  biased.
- **Blending.** At Rubin depth a large fraction of galaxies overlap other sources.
  Deblending errors couple neighbours' shapes. Roman's resolution helps enormously
  here — a major reason space weak lensing is valuable — but Roman's undersampled
  PSF brings its own difficulty.
- **Detector effects** — brighter-fatter, charge transfer inefficiency, IPC,
  the "tree rings" and "edge distortions" in thick CCDs — all imprint spurious
  shapes and must be corrected at the pixel level before shape measurement.

The bias is parametrized as **multiplicative (m) and additive (c)**:

```
gamma_observed = (1 + m) * gamma_true  +  c
```

and the requirement for Stage-IV surveys is roughly |m| ≲ 0.002 and c at the 10⁻⁴
level per tomographic bin. Achieving that needs:

- **Metacalibration** (Huff & Mandelbaum 2017; Sheldon & Huff 2017) — artificially
  shear each galaxy image by a known small amount (deconvolving the PSF, shearing,
  reconvolving), re-measure, and numerically differentiate to get the **response**
  R = ∂e/∂γ per object; ⟨e⟩/⟨R⟩ is then a nearly-unbiased shear estimate with the
  noise and model bias calibrated *from the data itself*. **Metadetection** extends
  this through the detection step (re-running detection on the sheared images) to
  also calibrate selection and blending bias. `ngmix` + `metadetect` implement
  this; it is compute-heavy (several remeasurements per galaxy) — an
  infrastructure/performance problem.
- **Image simulations** — inject realistic galaxies with known shear (`GalSim`,
  `imSim`, `romanisim`) through the real pipeline and measure the recovered m, c.
  The simulation fidelity *is* the calibration accuracy.

### 21.3 The astrophysical systematics on top

- **Intrinsic alignments (IA).** Galaxies near the same tidal field acquire
  correlated *intrinsic* shapes — not from lensing. This contaminates cosmic shear
  at the ~10% level. Modeled by the **nonlinear linear alignment (NLA)** model
  (an amplitude A_IA, possibly with redshift and luminosity dependence) or the
  more physical TATT model. Marginalized over in the cosmology fit; a wrong IA
  model biases w and S₈.
- **Photometric-redshift n(z) calibration** — §19.2; the dominant systematic.
- **Baryonic feedback** on the small-scale power spectrum — §19.4.
- **Source–lens clustering / magnification bias / boost factors** in
  galaxy–galaxy lensing.
- **Reduced-shear and other second-order corrections** at the precision of Stage
  IV.

### 21.4 Software

`GalSim` (the image-simulation engine — you should know this one well; it renders
galaxies, PSFs, and detector effects and is the backbone of every shear
calibration), `ngmix` + `metadetect` (shape measurement), `piff` (PSF), `TreeCorr`
(two-point correlations — you use it), `NaMaster` (pseudo-Cℓ), `CLMM` (cluster
lensing — you use it), `pyccl` (theory predictions), `TXPipe` (the end-to-end
DESC 3×2pt measurement pipeline), `RAIL` (photo-z), `SACC` (data vector +
covariance).

---

## 22. Statistical methods particular to astronomy

You know statistics; this is the astronomy-specific idiom and the recurring traps.

### 22.1 Selection effects and biases (the ones with names)

- **Malmquist bias** — in a flux-limited sample, at any given distance you
  preferentially detect the intrinsically brighter objects, so the *mean* inferred
  luminosity rises with distance. Corrections require knowing the luminosity
  function and the selection function; in SN cosmology this is the BBC/BEAMS
  machinery (§17.3).
- **Eddington bias** — measurement scatter on a steeply-falling number-count
  distribution scatters more objects up than down, inflating the bright end of a
  measured luminosity/mass function. Deconvolve, or forward-model.
- **Lutz–Kelker bias** — the analogous effect for parallax-inferred distances
  (more low-parallax stars scatter up than high-parallax stars scatter down).
- **The "look-elsewhere" effect** — a 3σ bump somewhere in a large search is not a
  3σ detection; the trials factor must be accounted for (periodograms, transient
  searches, line searches).
- **Confirmation bias** — the reason cosmology analyses are blinded (§20.5).

### 22.2 Bayesian practice

- **Hierarchical / multi-level models** — the natural structure for astronomy:
  population hyperparameters → per-object latent parameters → noisy data.
  SN cosmology (global α, β, M_B, intrinsic scatter → per-SN x₁, c, μ → light
  curves) and photo-z n(z) calibration are both hierarchical. Fit with Gibbs/HMC
  or with approximate marginalization.
- **Priors matter and must be reported.** Flat priors are not uninformative under
  reparametrization; a flat prior on a distance is not flat on a parallax. Jeffreys
  priors, reference priors, and explicit sensitivity tests are expected.
- **Marginalization over nuisance parameters** — calibration offsets, bias
  parameters (m, c), IA amplitude, bias b, baryonic parameters, photo-z shifts.
  Stage-IV analyses marginalize over tens of nuisance parameters; the "cosmology"
  is what survives.
- **Model comparison** — Bayesian evidence (nested sampling gives it for free),
  information criteria (AIC/BIC/DIC/WAIC), posterior predictive checks. "Is wₐ ≠ 0
  preferred?" is a model-comparison question, not just a parameter estimate.
- **Errors on errors** — a sample covariance estimated from N_sim simulations is
  itself noisy and biased when inverted; the **Hartlap factor** and the
  **Sellentin–Heavens** likelihood correct for it. If your data vector has 1000
  elements you need ≫ 1000 simulations.

### 22.3 Correlation functions and their estimators

- **Landy–Szalay estimator** for ξ(θ): (DD − 2DR + RR)/RR, using a random catalog
  that encodes the survey mask and selection. The random catalog is often the
  hard part — it must reproduce every position-dependent selection effect.
- **Edge effects, integral constraint, and the survey mask** — a finite, holey
  footprint biases and correlates the measured multipoles; handled by the mask
  deconvolution (`NaMaster` for pseudo-Cℓ) or by mask-aware estimators.
- **Covariance of two-point functions** — Gaussian (analytic) + non-Gaussian
  (trispectrum) + super-sample covariance (modes larger than the survey). Estimated
  analytically, from mocks, or from the data by jackknife/bootstrap (with the
  corrections above).
- **Fast pair-counting** — `Corrfunc`, `TreeCorr` (kd-tree, supports scalar and
  spin-2 fields, weights, jackknife); the naïve O(N²) is hopeless at 10⁹ galaxies.

### 22.4 Time-series statistics (recap + additions)

- **Uneven sampling** breaks FFT-based methods; Lomb–Scargle, Gaussian processes,
  and the CLEAN algorithm handle it. Always compute and show the **window
  function** — most spurious periods are aliases of the cadence.
- **Red noise** — astrophysical variability and instrumental drift are correlated
  in time, so white-noise significance estimates are wildly optimistic. Model the
  noise (GP, ARMA, wavelet) or use empirical false-alarm rates from
  permutations/bootstraps.
- **Detection theory for transients** — the matched filter (image or light curve),
  the ZOGY score image, receiver-operating-characteristic (ROC) analysis,
  completeness vs. purity trade-offs at a chosen threshold — the language your
  BTSbot work already speaks.

### 22.5 Machine learning in astronomy — the field-specific pitfalls

- **Domain shift / covariate shift** — a model trained on ZTF (or on simulations)
  is being asked about Rubin or Roman or real data; the input distribution has
  moved. This is *the* concern for transferring BTSbot to LSST, and the reason a
  careful transfer study is publishable.
- **Label noise and incompleteness** — spectroscopic "ground truth" is itself
  uncertain and non-representative (biased toward bright, nearby, easy objects).
- **Class imbalance** — real transients are a tiny fraction of difference-image
  detections; metrics must be imbalance-aware (precision/recall, PR-AUC, not raw
  accuracy).
- **Silent preprocessing mismatches** — normalization applied twice or not at all,
  a different image cutout convention, a BatchNorm layer's expectations — exactly
  the traps you already documented in the BTSbot reproduction. Always verify the
  preprocessing contract against the published model.
- **Uncertainty quantification** — point predictions are not enough for science;
  the field increasingly requires calibrated probabilities or posteriors (mixture
  density networks, conformal prediction, deep ensembles, simulation-based
  inference).
- **Simulation-based inference (SBI / likelihood-free inference)** — when the
  likelihood is intractable but you can simulate, train a neural density estimator
  on (parameters, simulated data) pairs to get the posterior. A fast-growing area
  in cosmology (`sbi`, `lampe`); relevant to field-level and non-Gaussian
  analyses.

---

## 23. Survey and data system: Vera C. Rubin Observatory / LSST

### 23.1 The hardware

- **Simonyi Survey Telescope** — 8.4 m primary (an unusual monolithic M1+M3 casting),
  3.5° field of view (9.6 deg² usable), f/1.23, a three-mirror anastigmat that
  keeps the wide field in focus. Slews and settles in ~5 s so it can take a new
  field every ~30 s.
- **LSSTCam** — the largest astronomical camera built: 3.2 gigapixels, 189 CCDs
  (4k×4k, from two vendors) tiled into 21 "rafts" on a flat focal plane 64 cm
  across, 0.2″ pixels, a carousel of six filters (**u g r i z y**), and a
  ~30 s standard visit.
- **Site** — Cerro Pachón, Chile, next to Gemini South and SOAR.

### 23.2 The survey

- **Wide-Fast-Deep (WFD)** — ~18,000 deg² covered ~800+ times over 10 years,
  split across the six bands, ~2 visits per field per few nights. Single-visit 5σ
  depth r ≈ 24.5; 10-year coadd r ≈ 27.5.
- **Deep Drilling Fields (DDFs)** — a handful of single pointings observed far more
  frequently and deeply (for SN cosmology, AGN, faint galaxies).
- **Mini-surveys / special programs** — Galactic plane, North Ecliptic Spur, South
  Celestial Pole, Target-of-Opportunity (e.g. gravitational-wave follow-up). The
  exact cadence is still being tuned via the community `rubin_sim` /
  "survey strategy" process — an area with open community input.

### 23.3 The two data paths

**Prompt (nightly).** Within **60 seconds** of each exposure: calibrate → subtract
a template (difference imaging) → detect and measure **DIASources** → associate
into **DIAObjects** → build an **alert packet** (the new detection, the DIAObject's
prior light curve, 2 image cutouts, nearest static-object context, a
solar-system-object match, a real/bogus score) → publish as **Apache Avro** over
**Apache Kafka**. ~10 million alerts per night. Seven **community brokers**
(ALeRCE, ANTARES, BABAMUL, Fink, Lasair, Pitt-Google, + one more) receive the full
stream; everyone else subscribes to a broker or to a small Rubin-provided filtered
stream. Also produced nightly: the **Prompt Products Database** (DIASource,
DIAObject, DIAForcedSource tables), updated cumulatively.

**Data Release (annual).** A full reprocessing of *all* data taken so far, from
pixels up, with a frozen pipeline version: coadds, deep detection, deblending,
multi-epoch/multi-band measurement, forced photometry on every object in every
visit. Products: the **Object** catalog (~20 billion static sources with fluxes,
shapes, photo-z), the **Source** catalog (per-visit measurements), the
**ForcedSource** catalog (light curves), coadd and calibrated single-visit images,
and the SSObject catalog (solar system). Served from **Qserv**, a distributed
shared-nothing parallel SQL database built for this. DR1 is expected around
2026–2027; releases are proprietary to data-rights holders for ~2 years, then
public.

### 23.4 Access: the Rubin Science Platform (RSP)

Three "aspects", all hosted at the US Data Facility (SLAC) and mirrors:

- **Portal** — web UI for catalog queries and image visualization.
- **Notebook** — a JupyterLab environment ("Nublado") with the Stack
  pre-installed. (You will use this only for data proximity, or not at all — the
  API and downloads support script-based work.)
- **API** — **TAP** (Table Access Protocol; query catalogs with **ADQL**, a
  SQL dialect with spatial functions), **SIA**/**SODA** (image discovery and
  cutouts), **HiPS** (hierarchical sky maps), plus an authenticated
  **Butler** client for direct data access. The `lsst-rsp` / `pyvo` clients drive
  these from anywhere with a token.

**Data Previews** (public, no data rights needed) — the way to learn the system
now:

- **DP0.1** — a purely simulated release (the DESC CosmoDC2 extragalactic catalog
  rendered into images with `imSim`), run through an early pipeline.
- **DP0.2** — the same simulated sky reprocessed with the near-final Data Release
  Processing pipeline; the reference dataset for pipeline tutorials.
- **DP0.3** — simulated Solar System data (for SSSC).
- **DP1** — the first *real* data, from the **Commissioning Camera (ComCam)** — a
  small 9-CCD engineering camera — released in 2025, covering several small fields.
- **DP2** — a larger real release from LSSTCam commissioning.

### 23.5 The software: the LSST Science Pipelines ("the Stack")

- Distributed as `lsst_distrib` via a conda environment (`rubin-env`); also
  containers. Python API under `lsst.*`, performance-critical core in C++ (`afw` —
  "Application Framework": `Image`, `Exposure`, `SourceCatalog`, geometry, math).
- **The Butler** (`lsst.daf.butler`, "Gen3") — the data-abstraction layer: you ask
  for a dataset by *type* + *data ID* (e.g. `calexp` for visit=..., detector=...)
  and the Butler resolves storage, format, and provenance. A registry database +
  a datastore (POSIX, S3, …). This is a data-management design problem in your
  wheelhouse.
- **PipelineTask / `pipe_base` / `ctrl_bps`** — pipelines are graphs of
  `PipelineTask`s; the middleware builds a **QuantumGraph** (every unit of work and
  its exact inputs/outputs) and a workflow system (`ctrl_bps` with Parsl,
  HTCondor, or PanDA backends) executes it across a cluster with full provenance.
- **`ap_pipe` / `ap_association`** — alert production (difference imaging,
  DIASource measurement, association, packet generation).
- **`analysis_tools`** — the QA / metrics / plotting framework (good entry point).
- **`meas_*`** — measurement algorithms (aperture, PSF, model, moments, extended).
- **Process:** GitHub (`lsst` org), the **RFC** process and Data Management
  discussions on `community.lsst.org` (Discourse), a public Jira, weekly open
  meetings, the Rubin Community Forum for science users.

### 23.6 `rubin_sim` / survey strategy

`rubin_sim` and the Metrics Analysis Framework (`MAF`) simulate the observing
cadence and evaluate "metrics" (how well a given strategy serves each science
case). The cadence is genuinely still being decided with community input — a place
where a well-argued metric contribution is welcome.

---

## 24. Survey and data system: Nancy Grace Roman Space Telescope

### 24.1 The hardware

- **2.4 m primary** (an ex-National-Reconnaissance-Office mirror, same aperture as
  Hubble but a much wider field), at the Sun–Earth **L2** point.
- **Wide Field Instrument (WFI)** — **18 Teledyne H4RG-10 HgCdTe detectors**
  (4088×4088 active, 10 µm pixels, ~2.3 µm long-wavelength cutoff), ~0.11″ pixels,
  **0.281 deg²** total field of view (~100× JWST NIRCam, ~200× a Hubble WFC3/IR
  pointing). Eight imaging filters **F062, F087, F106, F129, F146 (wide), F158,
  F184, F213**; a **grism (G150)** and a **prism (P127)** for slitless
  spectroscopy. Bandpass ~0.48–2.3 µm.
- **Coronagraph Instrument (CGI)** — a technology-demonstration high-contrast
  imager (deformable mirrors, active wavefront control) aiming at ~10⁻⁸–10⁻⁹
  contrast to directly image mature giant exoplanets and debris disks. Not a
  survey instrument.

### 24.2 The Core Community Surveys

Defined by community committees and refined by the project; parameters below are
approximate and have been revised over time — treat as orientation, verify current
numbers against project documentation.

- **High Latitude Wide Area Survey (HLWAS)** — ~2,000 deg² of multi-band imaging
  **plus** grism spectroscopy, at high Galactic and ecliptic latitude. Science:
  **weak lensing** (space-quality shapes in the near-IR), galaxy clustering,
  cluster counts, and a **grism redshift survey** of Hα and [O III] emission-line
  galaxies to z ~ 2–3 for **BAO and RSD**. This is Roman's 3×2pt-analog cosmology
  engine.
- **High Latitude Time Domain Survey (HLTDS)** — repeated imaging (and **prism**
  spectrophotometry) of a few deg², in a **wide shallow tier** and a **deep tier**,
  at roughly a **5-day cadence** over ~2 years, near an ecliptic pole for
  continuous visibility. Science: **~10,000+ Type Ia supernovae to z ~ 2–3** for
  the expansion history, with the near-IR keeping high-z SNe in the rest-frame
  optical (§17.3). Also core-collapse SNe, TDEs, AGN, and other transients.
- **Galactic Bulge Time Domain Survey (GBTDS)** — ~2 deg² toward the Galactic
  bulge, **~15-minute cadence** in **F146** (plus occasional other filters),
  ~6 seasons of ~72 days over the 5-year prime mission. Science: **exoplanet
  microlensing** (§18) — thousands of bound planets to sub-Earth masses,
  free-floating planets — plus tens of thousands of transiting planets and
  exquisite time series / astrometry for ~200 million bulge stars.
- **General Astrophysics Surveys** — roughly a quarter of observing time, allocated
  to community-proposed programs.

### 24.3 Operations and data flow

- **Mission Operations Center** — GSFC.
- **Science Operations Center (SOC)** — **STScI**: observation planning and
  scheduling, WFI level-1/level-2 data processing, and the archive via **MAST**.
- **Science Support Center (SSC)** — **IPAC/Caltech**: processing for the
  survey-level science products (notably the time-domain surveys — HLTDS and GBTDS
  pipelines), community support, and the **IRSA** archive.
- **CGI** operations involve **JPL**.
- **Data policy:** **no proprietary period.** Products are released through MAST and
  IRSA once processed and validated. A calibrated single-exposure image, a mosaic,
  a difference image, a light-curve table — public as soon as it exists.

### 24.4 Data levels and format

- **L0** — raw telemetry / uncalibrated ramp reads.
- **L1** — assembled uncalibrated exposures (the ramp cube, or the assembled
  frame).
- **L2** — **calibrated single-exposure products**: WFI rate images (slope fits to
  the ramp) with an attached `gwcs`, flagged and calibrated; extracted 1-D/2-D
  spectra for grism/prism.
- **L3** — **combined / resampled products**: coadded mosaics, stacked spectra,
  difference images.
- **L4** — higher-level science products: source catalogs, light-curve catalogs,
  weak-lensing shape catalogs, SN light curves, microlensing event tables.

Everything is **ASDF** (§25), not FITS. The WCS is `gwcs` serialized into the ASDF
tree.

### 24.5 The software stack

- **`romancal`** — the WFI calibration pipeline (ramp fitting, dark/flat, WCS
  assignment, flux calibration, resampling, source detection). Built on
  **`stpipe`** (the step/pipeline framework, shared with `jwst`), **`stcal`**
  (shared calibration algorithms), **`stdatamodels`**. Runs from the shell with
  `strun` or as a Python API.
- **`roman_datamodels`** + **`rad`** — the ASDF schema definitions and the Python
  data-model classes for every product.
- **`romanisim`** — the image simulator (produces L1/L2 in real formats). Also
  **STIPS** (Space Telescope Imaging Product Simulator, scene-level), **`pandeia`**
  (the exposure-time calculator / ETC engine), **`stpsf`** (formerly `webbpsf`;
  model PSFs).
- **Roman Research Nexus** — the cloud science platform (JupyterLab-fronted, with
  terminal access; data-proximate compute). Optional for you.
- **Archives:** MAST (`astroquery.mast`, the MAST API) and IRSA (`pyvo` against
  TAP/SIA/SODA, `astroquery.ipac.irsa`).

### 24.6 Roman ↔ Rubin synergy (and how to work now, pre-data)

- **OpenUniverse2024** — a joint simulation of **Roman and Rubin imaging over the
  same ~70 deg² sky**, with matched truth catalogs (galaxies, stars, SNe,
  transients), released 2024 and hosted on IRSA / NERSC. Built with `imSim`
  (Rubin) and `romanisim` / GalSim (Roman). The single best dataset for building
  and validating analysis pipelines against realistic Roman+Rubin data *before*
  launch data exists — and it lets your BTSbot transfer study and your SN pipeline
  port both proceed now.
- Earlier: the **RomanDESC** image sims (Troxel et al.) for the wide-area/lensing
  case.
- **Complementarity:** Rubin brings area, optical bands, and high-cadence
  time-domain over the whole southern sky; Roman brings depth, ~0.1″ resolution,
  and near-IR coverage over smaller areas. Weak lensing benefits from Roman shapes
  + Rubin colours; SN cosmology benefits from Rubin discovery + Roman high-z
  follow-up and rest-frame-optical light curves; photo-z calibration benefits from
  the combined optical+NIR baseline.

---

## 25. Data formats, standards, and the Virtual Observatory

### 25.1 FITS

**Flexible Image Transport System** — the 40-year-old lingua franca. A file is a
sequence of **HDUs** (Header-Data Units); each HDU has an ASCII header of
80-character `KEYWORD = value / comment` cards followed by a binary payload (an
N-dimensional array, or a binary table). Conventions layered on top: **WCS**
keywords (§15.1), the `BINTABLE` column format, `CHECKSUM`, multi-extension files
(MEF), compressed-image tiles (`fpack`). Strengths: universal, self-describing,
stable. Weaknesses: 80-column headers, 2880-byte block padding, weak support for
hierarchy, no native compression story, awkward for anything that is not
"array + flat table". Python: `astropy.io.fits`, `fitsio`.

### 25.2 ASDF (Roman's format)

**Advanced Scientific Data Format** — developed at STScI to replace FITS for JWST
and Roman. A file is a **human-readable YAML tree** (metadata, structure,
relationships, and *transform models* like a full `gwcs`) followed by optional
**binary blocks** for large arrays, referenced from the tree. Key properties:

- **Schema-validated.** Every data model has a formal schema (`rad` for Roman);
  the file either conforms or it does not. This is the property a data architect
  will appreciate — the structure is a contract, not a convention.
- **Arbitrary hierarchy**, native references, and extensibility via tagged types
  (an ASDF "extension" registers Python (de)serializers for a tag — e.g.
  `astropy` models, `gwcs`, units, `Time`).
- **Streaming and lazy access** to binary blocks; blocks can be compressed.
- Python: `asdf`, `asdf-astropy`, `asdf-standard`, `rad`/`roman_datamodels`.

If you do one "learn the plumbing" exercise for Roman, make it this: open a
`romanisim` L2 file, walk the ASDF tree, pull the `gwcs`, and understand how the
schema pins the structure.

### 25.3 Other formats you will meet

- **HDF5** — hierarchical, chunked, compressed binary; the default for
  simulations, large catalogs, and ML training data (`h5py`, `pytables`).
- **Parquet** — columnar, compressed, predicate-pushdown; increasingly the format
  for large tabular catalogs and light curves (you already use it). `pyarrow`,
  `polars`.
- **HATS / HiPSCat** (LINCC) — Parquet catalogs spatially partitioned on a HEALPix
  scheme so that spatial queries and cross-matches touch only the relevant
  partitions; the substrate for `LSDB` at LSST scale.
- **VOTable** — an XML table format with rich metadata and UCDs (below); what VO
  services return by default.
- **HEALPix** — Hierarchical Equal Area isoLatitude Pixelization of the sphere:
  the standard for sky maps (masks, dust maps, CMB, density maps). `healpy`,
  `cdshealpix`, `astropy-healpix`. **MOC** (Multi-Order Coverage) maps encode
  arbitrary sky regions as sets of HEALPix cells at mixed orders (`mocpy`).

### 25.4 The Virtual Observatory (IVOA standards)

A set of interoperability standards so that any archive can be queried the same
way. The ones you will use:

- **TAP** (Table Access Protocol) — run **ADQL** (SQL + geometry:
  `CONTAINS(POINT(...), CIRCLE(...))`, `POLYGON`, cross-match joins) against a
  service's tables; sync or async. Rubin RSP, IRSA, MAST, Gaia, VizieR all speak
  TAP.
- **SCS** (Simple Cone Search) — "objects within radius r of (α, δ)".
- **SIA** (Simple Image Access) v2 — discover images overlapping a region.
- **SSA** (Simple Spectral Access) — same for spectra.
- **SODA** — server-side cutouts / subsetting of a data product.
- **DataLink** — from a record, discover its related products (previews, cutouts,
  associated files, provenance).
- **ObsCore** — a common data model for "observational dataset" metadata, queryable
  via TAP.
- **UCD** (Unified Content Descriptors) and **VO units** — controlled vocabularies
  that tag what a column *means* (`phot.mag;em.opt.r`) and its units, so clients
  can interpret tables they have never seen.
- **HiPS** (Hierarchical Progressive Survey) — multi-resolution tiled sky imagery
  and catalogs for progressive visualization (Aladin).

Python client: **`pyvo`** (TAP/SCS/SIA/SSA/SODA/DataLink), plus `astroquery` for
archive-specific wrappers. A client-side contributor who actually understands
these standards is rare and useful (Pathway A7).

---

## 26. Pipelines and data-processing architecture

The shape is the same for every optical/NIR survey; the names differ.

### 26.1 The canonical stages

1. **Instrument Signature Removal (ISR)** / detector calibration — turn raw
   counts into a calibrated image of the sky:
   - bias / reference-pixel subtraction; for NIR, **ramp fitting** (slope per
     pixel from the non-destructive reads, with cosmic-ray "jump" detection);
   - dark subtraction; nonlinearity correction; **flat-fielding** (pixel-to-pixel
     and illumination); gain harmonization;
   - brighter-fatter correction; CTE correction (CCD); IPC and persistence
     handling (NIR); crosstalk;
   - bad-pixel / saturation / cosmic-ray masking;
   - background estimation and subtraction (sky, and for slitless spectroscopy the
     dispersed background).
2. **Astrometric calibration** — fit the WCS against a reference catalog (Gaia),
   solving distortion; for the ground, model differential chromatic refraction.
3. **Photometric calibration** — per-visit zero points; survey-wide
   self-calibration ("übercal"); absolute anchor to spectrophotometric standards.
4. **PSF estimation** — model the PSF from stars and its variation across the
   field (and, for coadds, the effective PSF of the stack).
5. **Image coaddition** — register, resample (with a kernel — Lanczos, or
   `drizzle`), and combine visits into deep coadds; build difference-imaging
   templates; produce "likelihood" / decorrelated coadds for optimal detection.
6. **Detection and deblending** — find sources above threshold on the coadd;
   separate overlapping sources (deblending) — a hard, error-prone step at survey
   depth.
7. **Measurement** — for every source: centroid, aperture fluxes, PSF flux,
   model (Sérsic / bulge+disk) fluxes, shape moments and calibrated ellipticity
   (weak lensing), flags. Then **multi-epoch / forced photometry** — measure every
   source's flux in every single-visit image at its fixed reference position,
   producing light curves (including non-detections).
8. **Catalog generation** — assemble the Object / Source / ForcedSource tables;
   run photo-z; classify (star/galaxy/QsO); associate across bands and epochs;
   ingest into the query database.
9. **(Time domain, in parallel)** — difference imaging → DIASource measurement →
   association into DIAObjects → real/bogus and science classification → alert
   packets or transient catalogs (§16.4).

### 26.2 The cross-cutting infrastructure concerns (your territory)

- **Data abstraction & provenance** — the Butler (Rubin) / data-model + archive
  (Roman): given a dataset type and a data ID, resolve storage, format, version,
  and the full processing lineage. Reproducibility depends on it.
- **Workflow orchestration** — express the pipeline as a DAG of atomic units
  ("quanta"), materialize the graph of every input/output, and execute across a
  batch system with retries, checkpointing, and provenance capture
  (`ctrl_bps`/Parsl/PanDA for Rubin; CWL/Snakemake-style for others).
- **Scale** — petabytes of images, tens of billions of catalog rows, trillions of
  forced-photometry measurements. Spatial partitioning (HEALPix / HATS), columnar
  storage (Parquet), distributed SQL (Qserv), and out-of-core dataframes (Dask,
  `nested-pandas`) are the responses.
- **Calibration data management** — the "calibs" (bias, dark, flat, PSF models,
  reference catalogs, throughput curves) are themselves versioned data products
  with validity ranges; getting the right calib for a given exposure is a
  non-trivial lookup.
- **Quality assurance** — automated metrics on every processing run (astrometric
  and photometric residuals, PSF-model residuals, depth, completeness/purity,
  shape-catalog null tests), with dashboards and regression tracking
  (`analysis_tools`, DESCQA-style validation).
- **Versioning and reprocessing** — a Data Release is defined by a frozen pipeline
  version; the ability to reprocess everything reproducibly on demand is a
  first-class requirement.

### 26.3 Simulations in the loop

Every calibration claim is validated by pushing simulated data with known truth
through the *real* pipeline and checking recovery: shear calibration (m, c),
photo-z n(z), detection completeness, deblender performance, SN bias corrections.
The simulation's realism sets the calibration's accuracy — so simulation
infrastructure is science-critical infrastructure.

### 26.4 Difference imaging in detail

The step that makes time-domain science possible, and a numerically delicate one:

- **The problem** — subtract a reference image R from a new science image I so that
  static sources vanish and only varying, moving, or new flux remains. But R and I
  have different PSFs, different noise, slightly different WCS and photometric
  scale, so a naive pixel subtraction leaves huge residuals at every static source.
- **Alard–Lupton (1998)** — find a convolution kernel K (expanded in a basis of
  Gaussians × polynomials, spatially varying) such that R ⊛ K best matches I in
  least squares; the difference is I − R ⊛ K. Robust, widely used (`hotpants`,
  and the classic LSST `ip_diffim`).
- **ZOGY (Zackay, Ofek & Gal-Yam 2016)** — given both PSFs and noise, compute in
  Fourier space the *statistically optimal* difference image **D** (itself a proper
  image with a well-defined PSF) and a matched-filter **score image S** whose peaks
  are the maximum-likelihood detections with correct significance. Cleaner
  statistics; sensitive to accurate PSF and noise models and to astrometric
  registration.
- **SFFT (Hu et al. 2022)** — a δ-function kernel basis solved via FFTs,
  GPU-accelerated; fast enough for the data rates Rubin and Roman generate.
- **Artifacts** — astrometric misregistration produces **dipoles** (a +/− pair);
  bright stars leave residuals; CRs, ghosts, satellite/aircraft streaks, and
  optical reflections all masquerade as sources. Hence the **real/bogus**
  classifier as a mandatory downstream filter (§16.3).

---

## 27. Simulations (what they are, which ones matter)

- **Image simulators** — render a catalog of sources into realistic pixels:
  - **`GalSim`** — the community engine for galaxy/PSF/detector rendering; the
    backbone of weak-lensing shear calibration.
  - **`imSim`** — Rubin's full raw-image simulator (GalSim + a detailed LSSTCam
    and atmosphere model); produced DP0.
  - **`romanisim`** — Roman WFI L1/L2 simulator (GalSim-based) in real data
    formats.
  - **STIPS** — scene-level Roman/HST imaging simulator (faster, lower fidelity).
  - **`skymaker`/`SExtractor`-era** tools — legacy.
- **Catalog / sky simulators** — the truth universe fed to the image sims:
  - **CosmoDC2** — DESC's synthetic extragalactic catalog (~galaxies with
    consistent photometry, shapes, shears, photo-z truth) over ~440 deg² to
    z ≈ 3; the basis of DP0 and many DESC validation efforts.
  - **`SkyCatalog`** — the interface layer serving object truth to imSim/romanisim
    for OpenUniverse.
  - **DESI/Uchuu, MICE, Buzzard, Cardinal** — other mock catalogs built on N-body
    light cones for large-scale-structure and lensing validation.
- **N-body / hydro simulations** — the gravity-only (or gravity+gas) runs
  underneath the mocks: Millennium, MultiDark, Outer Rim, AbacusSummit, FLAMINGO,
  IllustrisTNG. You mostly consume their *derived* emulators and mocks, not the raw
  runs.
- **Survey / cadence simulators** — `rubin_sim` + `MAF` (Rubin observing strategy
  and metrics); the Roman survey-design tools.
- **End-to-end validation frameworks** — DESCQA / `descqa` (validate mock catalogs
  against data), the Roman-side equivalents in the PIT pipelines.
- **OpenUniverse2024** — the current joint Roman+Rubin image simulation over shared
  sky with matched truth; §24.6. **Your build-now dataset.**

---

## 28. The software stack (annotated)

Grouped by function. Bold = learn first for your pathway.

**Numerical / core**
- **`numpy`**, **`scipy`**, **`astropy`** (`units`, `coordinates`, `time`,
  `table`, `io.fits`, `wcs`, **`cosmology`**, `modeling`, `stats`, `convolution`,
  `timeseries`, `nddata`), `matplotlib`.
- `numba`, `cython`, `dask`, `polars`, `pyarrow`, `numexpr` for performance /
  scale.

**Archive access & VO**
- **`pyvo`** (TAP/ADQL, SCS, SIA, SSA, SODA, DataLink), **`astroquery`**
  (`.mast`, `.ipac.irsa`, `.gaia`, `.vizier`, `.ned`, `.simbad`), `lsst-rsp`.
- `requests`/`httpx` for raw archive APIs.

**Images, PSF, photometry, astrometry**
- **`photutils`** (detection, aperture/PSF photometry, background, segmentation),
  `sep` (fast Source-Extractor core), `reproject`, `ccdproc`, `astroscrappy`
  (cosmic rays), `drizzlepac`/`stwcs`, `stpsf` (formerly `webbpsf`), `piff` (PSF
  modeling), `scarlet`/`scarlet2` (deblending).
- Classic C tools you will see invoked: **SExtractor**, **SWarp**, **SCAMP**,
  **PSFEx**, **Astrometry.net**.

**Difference imaging / time domain**
- `hotpants`, `PyZOGY`, `properimage`, **`SFFT`**; Rubin `ip_diffim`.
- **`astropy.timeseries`** (Lomb–Scargle, BLS), `gatspy`, `feets`, `cesium`,
  **`light-curve`** (Rust, broker-grade feature extraction), `celerite2`/`george`
  (GP), `TAPE`/`nested-pandas` (per-object time series at scale).
- **`sncosmo`**, **SNANA** + `pippin`, `MulensModel`/`pyLIMA` (microlensing).

**Catalogs at scale**
- **`LSDB`**, **`hats`**/`hats-import` (LINCC), `nested-pandas`, `dask`,
  `healpy`/`cdshealpix`/`astropy-healpix`, `mocpy`, `dustmaps` (SFD/Planck/Bayestar
  extinction).
- Cross-match: `astropy.coordinates.match_coordinates_sky`, `LSDB` crossmatch,
  `NWAY` / likelihood-ratio matching, `X-Match` (CDS).

**Cosmology / large-scale structure / lensing**
- **`pyccl`** (CCL), **`CAMB`**, `CLASS`, `Cobaya`, `CosmoSIS`, `MontePython`.
- `emcee`, `zeus`, `dynesty`, `nautilus`, `PolyChord`; `getdist`, `ChainConsumer`.
- **`TreeCorr`**, `Corrfunc`, **`NaMaster`**/`pymaster`, `Halotools`, `nbodykit`,
  `pmesh`.
- **`GalSim`**, `ngmix` + `metadetect` (shear), **`CLMM`** (cluster lensing),
  `firecrown`, **`TXPipe`**, `SACC`, `Augur`, `pyccl`-based emulators.
- Photo-z: **`RAIL`**, `pzflow`, `qp` (PDF handling); classic: BPZ, EAZY, LePHARE.

**Pipelines / frameworks**
- **`romancal`** + `stpipe` + `stcal` + `stdatamodels` + **`roman_datamodels`**
  (Roman).
- **LSST Science Pipelines** (`lsst.daf.butler`, `lsst.pipe.base`,
  `lsst.ctrl.bps`, `lsst.afw`, `lsst.ap.pipe`, `lsst.analysis.tools`,
  `lsst.meas.*`).
- `romanisim`, `imSim`, `rubin_sim`/`MAF`.
- Workflow: `parsl`, `ctrl_bps`, `ceci` (DESC), `snakemake`, `nextflow`.

**Formats**
- **`asdf`**, `asdf-astropy`, `asdf-standard`, `rad`; `fitsio`, `h5py`,
  `pytables`, `zarr`, `fsspec`/`s3fs`.

**ML**
- `scikit-learn`, `torch` / `tensorflow`/`keras` (BTSbot is Keras), `xgboost`,
  `lightgbm`; `astroNN`, `fibad` (LINCC ML-on-images), `sbi`/`lampe`
  (simulation-based inference), `deepdisc` (detection/segmentation).

**Visualization (non-notebook-friendly options)**
- `matplotlib`, `bokeh`, `holoviews`/`datashader` (large scatter), `firefly`
  (Rubin/IPAC web viewer, scriptable), DS9 + `pyds9`/XPA, `astropy.visualization`
  (stretches, WCSAxes), Aladin / `ipyaladin`, `astrowidgets`.
- `Jdaviz` exists but is notebook-centric — noted for completeness, not
  recommended for your workflow.

---

## 29. A study plan / sequencing

Ordered by return on investment for your goal (read the code, hold the
conversation, spot the meaningful bug), not by textbook order. Each block is a few
weeks at a serious but part-time pace.

### Block 1 — Vocabulary and the measurement chain (highest priority)

- §§13–15 of this document, worked through with `astropy` open:
  - convert between ICRS / Galactic / Ecliptic; compute angular separations two
    ways (tangent-plane vs. spherical) and see them diverge near the pole;
  - convert JD ↔ MJD ↔ isot ↔ decimal year; apply a barycentric time correction;
  - convert flux ↔ AB mag ↔ Vega mag; compute a distance modulus; de-redden a
    magnitude given E(B−V) from a dust map;
  - build a bandpass, do synthetic photometry of a blackbody, recover its
    temperature from a colour.
- Chromey, *To Measure the Sky*, chapters on magnitudes, detectors, photometry.
- Deliverable: a small script library of these conversions with tests. (Doubles as
  Pathway-A practice and possibly a JOSS-scale tool later.)

### Block 2 — The two data systems (do early; directly job-relevant)

- §§23–26 of this document.
- Rubin: install `rubin-env`; work through the **DP0.2** tutorials **as scripts**
  (not the notebooks) — Butler queries, a TAP/ADQL catalog query via `pyvo`, an
  image cutout via SODA, run one `PipelineTask`. Read `community.lsst.org` for a
  week.
- Roman: install `romancal` + `romanisim` + `roman_datamodels`; simulate a WFI
  frame, run the pipeline end to end with `strun`, open the L2 ASDF file and walk
  the tree, extract and use the `gwcs`.
- Deliverable: notes on where the two architectures agree and differ (Butler vs.
  data-model+archive; QuantumGraph vs. `stpipe`; FITS+FITS-WCS vs. ASDF+gwcs).
  This *is* an ADASS-abstract-shaped observation.

### Block 3 — Statistics idiom + time domain (for the SN / broker pathway)

- §§16, 22 of this document.
- Ivezić et al., *Statistics, Data Mining, and Machine Learning in Astronomy* —
  the chapters on density estimation, regression, classification, time series.
  (This book is the single best match to your background; Ivezić is Rubin's Project
  Scientist.)
- Re-read your own BTSbot reproduction with §22.5 in hand; write the
  reproduction note (Pathway E, candidate 1).
- Port SN pipeline stages 4–6 onto simulated Roman light curves (SNANA or Roman SN
  PIT sims); port the BTSbot harness onto OpenUniverse cutouts.

### Block 4 — SN Ia cosmology depth (for the SN pathway)

- §§17, 20 of this document.
- Hogg, "Distance measures in cosmology" — implement D_C(z) from E(z) yourself,
  check against `astropy.cosmology` and `pyccl`.
- Read one modern SN cosmology analysis end to end (e.g. the Pantheon+ cosmology
  paper, or DES-SN5YR) for the systematics budget and the BBC/BEAMS machinery.
- Goobar & Leibundgut 2011 review (SN Ia cosmology).

### Block 5 — Galaxies, photo-z, large-scale structure, lensing (for the 3×2pt pathway)

- §§19, 21 of this document.
- Free lecture notes: Frank van den Bosch's Yale "Astronomy 610/510" notes
  (galaxies, halos, large-scale structure) — thorough and self-contained.
- Bartelmann & Schneider, *Weak Gravitational Lensing* (Phys. Rep. 2001) for the
  formalism; Mandelbaum 2018 (ARA&A) for the systematics.
- Dodelson & Schmidt, *Modern Cosmology* (2nd ed.) — perturbations, growth,
  lensing, inference. Your GR/field-theory background makes this efficient.
- Run the DESC 3×2pt tutorial stack (`TXPipe` on a small mock, `pyccl` +
  `firecrown` for the theory) as scripts.

### Block 6 — Theory backfill (as needed, not front-loaded)

- Rybicki & Lightman, *Radiative Processes in Astrophysics* — pull the chapters you
  need (blackbody, bremsstrahlung, synchrotron, radiative transfer basics).
- Carroll & Ostlie, *An Introduction to Modern Astrophysics* — the general
  reference to fill any specific gap (stellar structure, galaxies, ISM).
- A GR text (Carroll's *Spacetime and Geometry*, or Schutz) for the lensing and
  FRW derivations if you want them from first principles.

### Ongoing (all blocks)

- One repo, followed closely: read every merged PR for a month before opening your
  own.
- One working-group telecon series: attend, take notes, map the vocabulary to Part
  II.
- Write short public notes on each block's deliverable.

---

## 30. Annotated bibliography

Everything here is either freely available or a standard library book. Grouped by
role. This section is the "go deeper than the text above" layer.

### 30.1 Textbooks — measurement and data

- **Chromey, *To Measure the Sky: An Introduction to Observational Astronomy*
  (2nd ed., CUP).** The best single book for your gap: coordinates, time,
  magnitudes, telescopes, detectors, noise, photometry, astrometry, spectroscopy —
  rigorous, modern, no hand-waving. Start here.
- **Howell, *Handbook of CCD Astronomy* (CUP).** Short, focused; detectors, the
  CCD equation, practical photometry.
- **Ivezić, Connolly, VanderPlas & Gray, *Statistics, Data Mining, and Machine
  Learning in Astronomy* (Princeton).** The methods bridge for a
  computational person entering astronomy; written by Rubin people; the companion
  `astroML` package and website have all the code. Effectively required for your
  path.
- **Hogg, "Distance measures in cosmology"** (arXiv:astro-ph/9905116). Six pages;
  every cosmological distance, defined and related. Implement from it.
- **Hogg, Bovy & Lang, "Data analysis recipes: Fitting a model to data"**
  (arXiv:1008.4686) and the other "Data analysis recipes" notes. The field's
  practical inference style.

### 30.2 Textbooks — astrophysics and cosmology

- **Carroll & Ostlie, *An Introduction to Modern Astrophysics* (2nd ed.).** The
  comprehensive undergrad-to-grad reference ("BOB"); use as a lookup, not a
  cover-to-cover read.
- **Rybicki & Lightman, *Radiative Processes in Astrophysics*.** The standard
  radiation text; graduate level; matches your physics background.
- **Dodelson & Schmidt, *Modern Cosmology* (2nd ed.).** The working cosmologist's
  reference — Boltzmann hierarchy, perturbations, growth, lensing, CMB, inference.
- **Weinberg, *Cosmology* (OUP).** More formal and complete; a reference when
  Dodelson is too terse.
- **Mo, van den Bosch & White, *Galaxy Formation and Evolution* (CUP).** The big
  galaxies-and-structure book; halo model, clustering, bias, semi-analytics.
- **Schneider, *Extragalactic Astronomy and Cosmology* (2nd ed., Springer).** A
  gentler on-ramp to the same material with excellent figures.
- **Kochanek et al., *Saas-Fee Advanced Course 33: Gravitational Lensing: Strong,
  Weak and Micro*.** The lensing reference across all three regimes.

### 30.3 Review articles (Annual Review of Astronomy & Astrophysics unless noted)

- **Bartelmann & Schneider 2001**, *Weak Gravitational Lensing* (Physics Reports
  340, 291) — the lensing formalism reference.
- **Kilbinger 2015** (Rep. Prog. Phys.), *Cosmology with cosmic shear observations*
  — a readable modern review.
- **Mandelbaum 2018**, *Weak Lensing for Precision Cosmology* (ARA&A 56, 393) —
  the systematics review; read this before touching shear code.
- **Weinberg et al. 2013** (Physics Reports 530, 87), *Observational Probes of
  Cosmic Acceleration* — the definitive probe-by-probe survey.
- **Huterer & Shafer 2018** (Rep. Prog. Phys.), *Dark energy two decades after* —
  status and methods.
- **Filippenko 1997**, *Optical Spectra of Supernovae* (ARA&A 35, 309) — the SN
  classification reference.
- **Goobar & Leibundgut 2011**, *Supernova Cosmology: Legacy and Future* (Ann.
  Rev. Nucl. Part. Sci.) — SN Ia as cosmological probes.
- **Gaudi 2012**, *Microlensing Surveys for Exoplanets* (ARA&A 50, 411) — the
  microlensing reference for the Roman bulge survey.
- **Ivezić & the LSST team; Tyson; etc.** — see the survey papers below.
- Look to **ARA&A**, **Physics Reports**, and **Living Reviews in Computational
  Astrophysics** for review-level treatments of any topic here.

### 30.4 Survey / mission papers

- **Ivezić et al. 2019**, *LSST: From Science Drivers to Reference Design and
  Anticipated Data Products* (ApJ 873, 111). The Rubin reference paper.
- **LSST Science Collaboration 2009**, *LSST Science Book* (arXiv:0912.0201).
  Dated in specifics, still the broadest statement of the science case.
- **The DESC Science Requirements Document** (arXiv:1809.01669). What DESC's
  pipelines are built to deliver; a good map of the 3×2pt program.
- **Spergel et al. 2015**, *WFIRST-AFTA 2015 Report* (arXiv:1503.03757). The
  foundational Roman science report.
- **Akeson et al. 2019**, *The Wide Field Infrared Survey Telescope: 100 Hubbles
  for the 2020s* (arXiv:1902.05569). Readable mission overview.
- **Eifler et al. 2021** (two papers, arXiv:2004.04702 and 2004.05271),
  Roman (+Rubin) cosmology forecasts and the high-latitude survey.
- **Wang et al. 2022** and the **Roman High Latitude Time Domain Survey**
  Definition Committee Report — the SN survey design (search for the current
  version).
- **Rose et al. 2021**, *A Reference Survey for the Roman HLTDS*
  (arXiv:2111.03081).
- **Penny et al. 2019**, *Predictions of the Roman Galactic Bulge Time Domain
  Survey* (ApJS 241, 3).
- **OpenUniverse et al. 2025** — the OpenUniverse2024 simulated-data release paper
  (search "OpenUniverse 2024 Roman Rubin data preview").
- **Troxel et al. 2023** — the Roman+Rubin (RomanDESC) image simulation suite.
- The **DES Year 3** key papers (cosmic shear, 3×2pt, methods) as a fully worked
  example of a modern Stage-III analysis you can read end to end.

### 30.5 Documentation portals (reference, not reading)

- Rubin: `rtn` / `dmtn` technical notes, the Science Pipelines docs
  (`pipelines.lsst.io`), the RSP docs (`rsp.lsst.io`), `community.lsst.org`, the
  DP0/DP1 documentation.
- Roman: the STScI Roman documentation ("RDox"), `romancal.readthedocs.io`,
  `roman-datamodels.readthedocs.io`, `romanisim.readthedocs.io`, the IPAC Roman
  pages, MAST and IRSA Roman mission pages.
- Astropy: `docs.astropy.org`; the Astropy tutorials; `learn.astropy.org`.
- IVOA: `ivoa.net/documents` (TAP, ADQL, SIA, SODA, DataLink specs); `pyvo` docs.
- CCL: `readthedocs` + the CCL paper (Chisari et al. 2019, ApJS 242, 2).
- Cosmology tools: Ned Wright's Cosmology Tutorial and Calculator; the `astropy.cosmology`
  docs.
- Lecture notes: Frank van den Bosch (Yale ASTR 610), Mark Krumholz (ANU),
  Daniel Eisenstein and Wayne Hu's cosmology tutorials, the Rubin/LSST Discovery
  Alliance and DESC tutorial repos.

### 30.6 Community / process

- `community.lsst.org` (Rubin science + DM), the LSST Science Collaborations'
  pages, the DESC public pages and GitHub (`LSSTDESC`).
- The Roman community forum / mailing lists; the Roman Research Nexus docs.
- LINCC Frameworks: their site, GitHub (`astronomy-commons`, `lincc-frameworks`),
  and recorded tech talks.
- ADASS (proceedings in ADS), the AAS Journals author pages (RNAAS, JOSS
  cross-listing), the AAS Job Register.

---

## 31. Maintenance notes for this document

- **Part I** is a snapshot of the institutional landscape as of 2026-08. Membership
  rules, survey parameters, PIT structures, and broker lists change — re-verify
  before acting on specifics.
- **Part II §§13–22 and §§25–27** are physics and method; they age slowly.
  **§§23–24** (survey/data-system specifics — filter lists, cadences, survey areas,
  data-release dates, platform names) age fast; treat every number as approximate
  and check the current documentation portals in §30.5.
- Cross-references like "§17.3" point within this file.
- Add a dated line here when you revise a section.

| Date | Change |
|------|--------|
| 2026-08-31 | Initial version. |







