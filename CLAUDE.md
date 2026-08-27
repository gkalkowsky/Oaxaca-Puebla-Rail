# CLAUDE.md — Project State

Live state file for the Oaxaca–Puebla rail feasibility screen. **Read this
first; it is written so a fresh session can resume without reading the rest of
the repo.** Update it as part of the same commit as the work it describes — a
stale state file is worse than none.

---

## Current phase

**Phase 0 — repository scaffold. Complete.**

| Phase | What it delivers | Status |
|---|---|---|
| 0 | Repo structure, extraction pipeline, model skeleton, deliverable templates | **done** |
| 1 | Source retrieval and extraction (targets in `data_sources.md` §4) | not started |
| 2 | Fill corridor / demand / cost sections; run the breakeven model | not started |
| 3 | Evaluate stop rules in order, write the verdict, state the limits | not started |

## Retrieved and verified

**Nothing.** `sources/raw/` and `sources/extracted/` are empty, the manifest in
`deliverables/data_sources.md` §1 has no rows, and no figure anywhere in this
repo is sourced. Every number visible in a deliverable or the workbook is a
placeholder.

Before fetching anything, check `data_sources.md` §1 and `ls sources/extracted/`.
A source already listed `active` with an extraction present is not re-downloaded
and not re-extracted.

## Blocked

Nothing is blocked. Phase 1 can start immediately.

## Key figures established

_None._ This section is a table of sourced values only — a figure enters it
only with a manifest ID beside it. If it has no source, it does not belong here.

| Figure | Value | Unit | Source (manifest ID) |
|---|---|---|---|
| _(none)_ | | | |

## Stop rules

Defined in `deliverables/feasibility_screen.md` §2, none evaluated:

- **SR-1 Terrain** — Sierra Madre crossing grade beyond viable adhesion rail
- **SR-2 Demand floor** — breakeven ridership exceeds all corridor travel
  (computed directly on the `Breakeven` sheet of the workbook)
- **SR-3 Capital** — cost per km an order of magnitude outside any plausible envelope
- **SR-4 Legal** — concession, protected area or statutory bar with no route around it
- **SR-5 Evidence floor** — primary sources unobtainable → NEEDS-MORE-WORK, not NO-GO

**If a stop rule triggers:** stop analysis, write the finding to
`working/stop-rule-finding.md`, update this file, and commit before doing
anything else. Leave the remaining sections unanswered — that is the point of a
screen.

## Next action

**Begin Phase 1 retrieval, terrain first.** SR-1 is the cheapest stop rule to
test and the most likely to fire on this corridor: Oaxaca and Puebla sit on
opposite sides of the Sierra Madre, and terrain either permits a rail alignment
or it does not, independently of demand or funding. Establishing the elevation
profile and ruling grade needs one DEM and no institutional cooperation, so it
is the fastest path to a defensible NO-GO if there is one.

Concretely:

1. Retrieve INEGI elevation data covering the corridor:
   `analysis/scripts/fetch_source.sh inegi-<yyyy>-cem <url>`
2. Record the manifest row in `data_sources.md` §1; extract with
   `analysis/scripts/extract_source.py <source-id>`.
3. Derive the elevation profile and ruling grade for at least two candidate
   alignments (risk R-11 — do not anchor on the first). Working goes in
   `/working`; the DEM resolution is stated alongside every grade figure
   (risk R-01).
4. Evaluate SR-1 in writing, then proceed to demand or stop.

Only after terrain: existing rail assets and concessions (SR-4), then demand
(SR-2), then cost (SR-3).

## Working rules

- **Never fill a figure without its source.** Untraceable numbers are tagged
  inline `[UNSOURCED]`, `[ANALOGUE: <project>]` or `[ESTIMATE: <method>]` and
  cannot support a conclusion. `press` sources never support one alone.
- **Absence of evidence is not evidence of absence.** "No obstacle found"
  is written as "no obstacle found in sources retrieved", naming what was
  searched.
- **Do not re-download or re-extract** a source already present. Check first.
- **Commit at each milestone**, not once at the end. Run
  `analysis/scripts/check_repo_hygiene.sh` before committing.
- **Regenerate the workbook**, do not hand-edit its structure:
  `python3 analysis/scripts/build_breakeven_model.py`. Entered input values
  live in the file; structural changes live in the script.
- **Raw PDFs are gitignored on purpose.** Reproducibility comes from the URL,
  date and SHA-256 in `data_sources.md`, not from committing the binary.
- **Review the risk register** at every phase boundary; append, never renumber.
- **A GO verdict is not the goal** (risk R-12). Stop rules are evaluated in
  order and in writing before the verdict is drafted.

## Repo map

```
CLAUDE.md                              this file — live state
README.md                              what the project is, how to resume
sources/raw/                           downloaded originals (gitignored)
sources/extracted/<id>/document.md     committed evidence chain
analysis/breakeven_model.xlsx          generated model — blank inputs
analysis/scripts/fetch_source.sh       download + hash + manifest row
analysis/scripts/extract_source.py     PDF -> committed markdown
analysis/scripts/build_breakeven_model.py   regenerates the workbook
analysis/scripts/check_repo_hygiene.sh      pre-commit size/content guard
deliverables/feasibility_screen.md     the verdict + stop rules
deliverables/data_sources.md           manifest, protocol, retrieval targets
deliverables/risk_register.md          risks to the screen's conclusion
working/                               scratch, notes, stop-rule findings
```
