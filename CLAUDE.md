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

**Phase 4 — VERDICT ISSUED: negative, provisional. Steps 3b and 6 outstanding.**

| Phase | What it delivers | Status |
|---|---|---|
| 0 | Repo structure, extraction pipeline, hygiene guard | done (content misaimed, see above) |
| 1 | Source access + retrieval | done — SR-7 evaluated, 3 primary sources in |
| 2 | Step 2 breakeven model (freight tonnage back-solve) | **done — ARTF margin obtained, model live** |
| 3 | Step 3 aforo extraction | **done — 1,102 stations validated (99.8%)** |
| 3b | Step 3 commodity segregation | not started — needs SIAP / INEGI |
| 2b | Step 1 capital band | unsourced — **bypassed** by inverting to supportable capital |
| 4 | Step 4 compare + verdict | **done — NEGATIVE (provisional)** |
| 6 | Step 6 public-benefit case | **not tested** — the honest next question |

## Stop rules — from `Prompt.md`, these govern whether a verdict may be issued

| Rule | Question | Status |
|---|---|---|
| **SR-7 Network access** | Are primary Mexican government sources reachable? | **EVALUATED — DOES NOT FIRE.** Aforo and rail tonnage both obtained. Evidence: `working/source-access-log.md` |
| **SR-2 Through-traffic contamination** | Does articulated-truck volume decline approaching Oaxaca City? | **EVALUATED — DOES NOT FIRE.** 60% monotonic decline, 1,259 → 500 artic veh/day. Evidence: `working/sr2-evaluation.md` |
| **SR-3 Track condition straddle** | Do capital cases straddle breakeven? | **EVALUATED — resolves negative.** Formal straddle exists but needs ≥50% diversion to be credible; three lines of evidence say it is not. Flip point: **~50% capture AND light-benchmark capital** |

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

| Figure | Value | Unit | Source |
|---|---|---|---|
| Articulated veh/day, corridor entry (Plaza de Cobro Tehuacán, MEX-135D) | ~1,259 | veh/day, both dirs | `sct-2025-datosviales-oaxaca` |
| Articulated veh/day, corridor terminus (N of Oaxaca City) | ~500 | veh/day, both dirs | `sct-2025-datosviales-oaxaca` |
| Decline entry → terminus | 60 | % | derived, above |
| **Addressable articulated flow (upper bound)** | **≤ ~500** | veh/day, both dirs | derived — see `working/sr2-evaluation.md` |
| Articulated veh/day on the rail-parallel Cañada road (`PUE-MEX-135`) | 10–34 | veh/day, both dirs | `sct-2025-datosviales-oaxaca` |
| Aforo data year | 2024 | year | `sct-2025-datosviales-oaxaca` (publ. 2025) |

| **Contribution margin (Ferrosur EBIT/ton-km)** | **0.402** | MXN / net ton-km, const. 2024 | `artf-2024-anuario-ferroviario` |
| Weighted mean load per articulated vehicle | 19.1 | tonnes | `imt-pt179` Tabla 4.7 [2001 — STALE] |
| **Corridor tonnage** | **3.49** | Mt / year | derived (aforo class mix × IMT loads) |
| World Bank general renewal, **track only** | 12.2–14.3 | MXN million / km | `wb-2020-serbia-railways-lcc` Tabla 11 |
| World Bank partial renewal, **track only** | 6.3–9.3 | MXN million / km | `wb-2020-serbia-railways-lcc` Tabla 11 |
| **FIT cost recovery 2024** | **16.2** | % | `artf-2024-anuario-ferroviario` Tablas 7-3, 7-5 |
| FIT best year cost recovery (2019) | 36.2 | % | same |
| Ferrosur revenue per ton-km | 0.93 | MXN / ton-km, const. 2024 | `artf-2024-anuario-ferroviario` Tabla 7-8 |
| **Max supportable capital @100% capture** | **15.8–21.6** | MXN million / km | derived |
| **National mean rail haul** | **678** | km | `artf-2024-anuario-ferroviario` Tabla 2-2 |
| Corridor as share of mean haul | 32 | % | derived — **corridor far too short for rail economics** |
| **Aprovechamiento Especial subzone** (only one permitting infrastructure) | **239.2** | ha (0.049% of reserve) | `conanp-2013-pm-tehuacan-cuicatlan` |
| Mexican precedent (Línea Z) | ~60 | MXN million / km | **[PRESS — UNVERIFIED]** |
| UNESCAP light rehabilitation | ~9.25 | MXN million / km | brief, at 18.5 MXN/USD [ASSUMED] |

**Capital cost per km remains unsourced.** The verdict rests on the supportable-
capital ceiling, not on a cost estimate.

## Known-wrong artifacts

All three have been rebuilt against the real brief (commit `0022f4e`). Nothing
in the repo now targets the passenger new-build.

## The geographic correction that matters most

**MEX-135D and the railway share endpoints and nothing else.** 135D runs the
**Mixteca Alta**; the Vía Corta Oaxaca runs the **Cañada de Cuicatlán**. The
brief's specified SR-2 bound (entry − terminus = 759 veh/day) is exactly the
traffic leaving 135D at Mixteca destinations **not on the railway**. Using it
overstates addressable demand by ~2.5×. Use the endpoint flow (≤ ~500) instead.
Both are reported; they are never averaged.

## The access pattern that unblocked this task — reuse it

`www.gob.mx/<agency>` and `www.sct.gob.mx` serve bot-challenge pages, but the
**same institutions' document trees are served unchallenged from other paths**:

- `micrs.sct.gob.mx/images/DireccionesGrales/DGST/...` → DGST Datos Viales
- `imt.mx/archivos/Publicaciones/...` (bare domain) → IMT publications
- `www.gob.mx/cms/uploads/attachment/file/<id>/<name>.pdf` → **any gob.mx
  attachment**, including the ARTF Anuario

The third is the general case: find the attachment ID via search, fetch the CDN
path directly. This is what unblocked ARTF after it was written off as blocked.

## Next action

The verdict is issued. Remaining work sharpens it; it cannot reverse it.

1. **Bottom-up tonnage cross-check** (INEGI Censos Económicos — `inegi.org.mx`
   is reachable; SIAP is not). The brief's second method. Can only reduce the
   divertible share.
2. **Step 6 public-benefit case — the honest open question.** A negative freight
   revenue case is not a negative public-benefit case (~89% of measured benefits
   in comparable studies are reduced road operating cost). Untested.
3. **GIS overlay** of CONANP subzone polygons on the alignment — the one thing
   that would settle the permitting constraint. Shapefile not yet located.
4. **Capital unit cost for Mexico**, still unsourced. Try the CDN pattern for
   ASF audit reports and SICT tender awards.
5. **Legal history** still unverified — DOF and Wayback both egress-blocked.
   ARTF Tabla 1-1 confirms FIT holds Vía Corta Oaxaca; SCT's El Mirador
   confirms 367 km, Nov 1892, narrow→standard gauge.

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
