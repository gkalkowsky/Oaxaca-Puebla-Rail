# CLAUDE.md — Project State

Live state file for the **Puebla → Oaxaca City freight rail reactivation**
screen. **Read this first; a fresh session should be able to resume from it
without re-reading the repo.** Update it in the same commit as the work it
describes.

The authoritative task definition is **`Prompt.md`** (committed at the repo
root). Where this file and `Prompt.md` disagree, `Prompt.md` wins.

---

## Correction on record

Commits `579f18b`–`21c8641` scaffolded this repo for the **wrong project**: a
new-build *passenger* line crossing the Sierra Madre. The actual task is
reactivation of an existing **dormant freight** line (Vía Corta Oaxaca, línea
E, ~216.5 km) that follows the **Tehuacán valley and Cañada de Cuicatlán**,
explicitly *not* a Sierra Norte crossing.

That scaffold was built before `Prompt.md` reached the session. Consequences
still being unwound are listed under **Known-wrong artifacts** below.

Separately: the `CLAUDE.md` written in `21c8641` was not authored from the
work — it was pre-supplied in the session context and reproduced. This file
replaces it and is written from the actual state of the repo.

## Current phase

**Phase 1 — source retrieval. In progress.**

| Phase | What it delivers | Status |
|---|---|---|
| 0 | Repo structure, extraction pipeline, hygiene guard | done (content misaimed, see above) |
| 1 | Source access + retrieval | **in progress** — access gate passed, 3 sources in |
| 2 | Step 1 capital band → Step 2 breakeven tonnage back-solve | not started |
| 3 | Step 3 aforo extraction + commodity segregation | not started |
| 4 | Steps 4–6 compare, risk register, benefit-cost framing | not started |

## Stop rules — from `Prompt.md`, these govern whether a verdict may be issued

| Rule | Question | Status |
|---|---|---|
| **SR-7 Network access** | Are primary Mexican government sources reachable? | **EVALUATED — DOES NOT FIRE.** Aforo and rail tonnage both obtained. Evidence: `working/source-access-log.md` |
| **SR-2 Through-traffic contamination** | Does articulated-truck volume decline approaching Oaxaca City? If not, counts are through-traffic, not addressable demand | not evaluated — testable, station coordinates are in hand |
| **SR-3 Track condition straddle** | Do light / heavy / substantial-reconstruction capital cases straddle breakeven? If so the answer is INDETERMINATE | not evaluated |

Declining to conclude is an explicitly permitted outcome. Per `Prompt.md`,
manufacturing a conclusion to satisfy the deliverable spec is the worst
possible result.

## Retrieved and verified

Manifest with SHA-256 in `deliverables/data_sources.md` §1. All born-digital,
extracted with `pymupdf`, identity verified by reading page 1.

| ID | What it gives |
|---|---|
| `sct-2025-datosviales-oaxaca` | TDPA + class % (A, B, C2, C3, T3S2, T3S3, T3S2R4, OTROS) + lat/long per station. Data year 2024 |
| `sct-2025-datosviales-puebla` | Same, Puebla side |
| `imt-2023-manual-estadistico` | Rail `carga ferroviaria`, `ton-km` (pp. 43, 54–61). Confirmed to contain **no** aforo/TDPA |

**Access routing that made this work** (the non-obvious part): `www.sct.gob.mx`
and `www.imt.mx` serve bot-challenge pages, but `micrs.sct.gob.mx` and the bare
`imt.mx` domain serve the same institutions' document trees unchallenged. State
volumes are numbered by **INEGI state code** — 20 Oaxaca, 21 Puebla.

## Blocked

- **DOF** (`www.dof.gob.mx`) — egress policy denial at the proxy. Reported, not
  circumvented.
- **Wayback capture paths** — egress policy. The brief's designated link-rot
  fallback is unavailable.
- **ARTF Anuario Estadístico Ferroviario** (`www.gob.mx/artf`) — bot challenge.
  Blocks the commodity-level contribution margin per ton-km that Step 2 needs.
- **UNESCO property 1534 boundary** (`whc.unesco.org`) — HTTP 403.

Consequence: the corridor's legal/administrative history (2003 condition
notice, 2012 concession exclusion, 2023 FIT assignment) cannot currently be
verified against the primary record. `Prompt.md` says to treat its own history
section as a starting point, not fact — so this stays an open gap, and is not
closed by substituting press reporting.

## Key figures established

_None yet._ A figure enters this table only with a manifest ID beside it.

| Figure | Value | Unit | Source |
|---|---|---|---|
| _(none)_ | | | |

## Known-wrong artifacts — do not build on these

Written against the wrong project; each needs rebuilding before use:

- `analysis/breakeven_model.xlsx` — models **passenger ridership**. The task
  back-solves **freight tonnage** (30-yr life; 5/6/8% cost of capital; O&M that
  scales with gross passing tonnage, so the circularity must be bounded
  explicitly). Regenerate from the script, do not patch the workbook.
- `deliverables/feasibility_screen.md` — invented stop rules SR-1/SR-4/SR-5.
  The real rules are SR-2, SR-3, SR-7 above.
- `deliverables/risk_register.md` — R-01..R-12 are passenger/new-build risks.
  Real register must cover UNESCO/CONANP Tehuacán-Cuicatlán zoning, ROW
  integrity after 20+ years dormant, bienes comunales and Sistemas Normativos
  Indígenas consent, ASF findings on Línea Z, and the Asunción Ixtaltepec
  derailments.

## Next action

**Build the aforo table extractor** (`Prompt.md` Step 3), then evaluate SR-2.

The extraction hazard is already confirmed, not hypothetical: reading-order
text from the DGST tables interleaves columns — detailed class percentages sum
to **92.6** while the aggregated A/B/C triple sums to **100.0**. Columns must be
reconstructed from **word bounding boxes** (`pymupdf` `get_text("words")`),
then validated (classes sum to 100 ± rounding; TDPA plausible; station IDs
reconcile across years) before any number is used.

Then: order stations along the corridor by coordinate, measure the articulated
-truck gradient Tehuacán → Oaxaca City, and evaluate SR-2. If no gradient and
no bottom-up cross-check can be built, addressable demand is unbounded and no
go/no-go may be issued.

## Working rules

- **Search in Spanish, write in English.** Preserve Spanish technical terms and
  official titles verbatim so figures stay traceable.
- **`T3-S2` is written `T3S2` in the source PDFs.** The hyphenated form matches
  nothing and looks like absent data.
- **A gob.mx HTTP 200 is not access.** The challenge page returns 200 with a
  ~1821-byte body. Check body content, never status code.
- **Do not circumvent egress denials or bot challenges.** Report blocked hosts.
- **Label every assumption as an assumption, every time it appears.** Never
  silently substitute a proxy (e.g. US Class I margins) for the real figure.
- **Never fill a figure without its source.** Tag `[UNSOURCED]`,
  `[ANALOGUE: <project>]`, `[ESTIMATE: <method>]`. Flag anything older than
  5 years as potentially stale.
- **Deflate to one stated base year** (INEGI INPC) and state the MXN/USD rate
  and its date for every conversion. Never mix nominal figures across years.
- **Ranges, not false precision.** This is a screening study.
- **Checkpoint to disk continuously** — findings go in `/working` as they are
  produced, so an interrupted session resumes without redoing retrieval.
- **Do not re-download or re-extract** a source already present; the pipeline
  guards this, check `data_sources.md` §1 first.
- **Commit at each milestone.** Run `analysis/scripts/check_repo_hygiene.sh`.

## Repo map

```
Prompt.md                              the authoritative task definition
CLAUDE.md                              this file — live state
sources/raw/                           downloaded originals (gitignored)
sources/extracted/<id>/document.md     committed evidence chain
analysis/scripts/fetch_source.sh       download + hash + manifest row
analysis/scripts/extract_source.py     PDF -> markdown (marker|pymupdf|pdftotext|pypdf)
analysis/scripts/build_breakeven_model.py   regenerates the workbook
analysis/scripts/check_repo_hygiene.sh      pre-commit size/content guard
deliverables/                          the four required deliverables
working/source-access-log.md           SR-7 evidence: what is reachable, what is not
```
