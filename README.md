# Oaxaca–Puebla Rail — Feasibility Screen

A desk-based **feasibility screen** of a rail connection between Oaxaca de
Juárez, Oaxaca and Puebla de Zaragoza, Puebla, Mexico. The output is a
go / no-go / needs-more-work judgement backed by a traceable evidence chain,
not an engineering design and not an investment recommendation.

**Screen, not a study.** The purpose is to find the cheapest disqualifying
fact early. If a stop rule triggers (see `CLAUDE.md`), work halts, the finding
is written up, and the remaining questions go unanswered on purpose.

---

## Status

| | |
|---|---|
| **Phase** | 0 — repository scaffold |
| **Sources retrieved** | none |
| **Figures established** | none |
| **Blocked on** | nothing |
| **Next action** | Phase 1 source retrieval (see `CLAUDE.md`) |

`CLAUDE.md` is the live state file and always supersedes this table. Read it
first when resuming.

---

## Repository layout

```
CLAUDE.md                        live project state — read this first
README.md                        this file
sources/
  raw/                           downloaded PDFs & datasets, unmodified (gitignored)
  extracted/                     marker/MinerU output, one dir per source (committed)
analysis/
  breakeven_model.xlsx           ridership / cost breakeven model
  scripts/                       extraction and analysis code
deliverables/
  feasibility_screen.md          the answer: go / no-go / needs-more-work
  data_sources.md                every source, its URL, retrieval date, checksum
  risk_register.md               what could invalidate the screen
working/                         scratch, notes, intermediate findings
```

### Why raw PDFs are not committed

Raw documents are gitignored. Every one of them is recorded in
`deliverables/data_sources.md` with its URL, publisher, retrieval date and
SHA-256, so the corpus is reproducible without carrying hundreds of megabytes
of government PDFs in git history. The **extracted markdown is committed** —
that is what the deliverables cite, and it must be auditable in the diff.

---

## Evidence chain

Every figure in a deliverable is traceable back to a primary document:

```
deliverable claim
  └─ cites → sources/extracted/<source-id>/<file>.md#<section>
       └─ extracted from → raw document (SHA-256 in data_sources.md)
            └─ retrieved from → URL + date in data_sources.md
```

A claim that cannot complete this chain is marked `[UNSOURCED]` and does not
support a conclusion. Estimates carried from analogue projects are marked
`[ANALOGUE]` and named as such.

---

## Resuming work

1. Read `CLAUDE.md` — current phase, verified figures, blockers, next action.
2. Check `sources/extracted/` **before** downloading or extracting anything.
   Re-extraction is wasted work; the manifest in `data_sources.md` is the index.
3. Do the next action.
4. Commit at each milestone. If a stop rule triggers, commit the partial work
   and the stop-rule finding before anything else.

## Setup

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r analysis/scripts/requirements.txt
```

## Scope boundary

In scope: corridor geography and grade, existing rail assets and their
condition, demand proxies, order-of-magnitude capital and operating cost,
breakeven ridership, institutional and legal posture, and the risks that would
invalidate any of the above.

Out of scope: alignment engineering, geotechnical work, environmental impact
assessment, rolling-stock procurement, financial structuring, and any
consultation with affected communities. A favourable screen is an argument for
commissioning that work — it is not a substitute for it.
