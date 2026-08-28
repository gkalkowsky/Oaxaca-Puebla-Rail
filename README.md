# Vía Corta Oaxaca — Freight Reactivation Feasibility Screen

Desk-based **Phase 0 feasibility screen** of reactivating the dormant
**Vía Corta Oaxaca** (rail line "E", Sánchez, Puebla → Oaxaca City, Oaxaca,
km E-150+000 to E-367+000, ~216.5 km) for **freight**.

The line follows the **Tehuacán valley and Cañada de Cuicatlán**, not a Sierra
Norte crossing. It opened in 1892 as the Ferrocarril Mexicano del Sur, was
converted from narrow to standard gauge in the 1950s, and has been out of
service since 2004. It is currently assigned to **FIT** (Ferrocarril del Istmo
de Tehuantepec).

The authoritative task definition is **`Prompt.md`** at the repo root.
**`CLAUDE.md` is the live state file — read it first when resuming.**

---

## Result

> ### NEGATIVE — the corridor does not support reactivation on a freight revenue case
>
> Provisional. The outstanding work can only strengthen this, not reverse it.

**Even with bridges, drainage, slope stabilisation, signalling and
right-of-way all costed at zero, the line must capture 32–91% of every
articulated tonne moving in the corridor simply to break even** — 80 to 227
loaded truckloads/day each way, against ~250 articulated vehicles/day each way
observed.

Four independent lines converge:

| | |
|---|---|
| **Haul distance** | Mexican rail freight averages a **678 km** haul (ARTF). This corridor is 216.5 km — 32% of the system mean, and 53% of even the shortest-hauling commodity group. Rail's advantage over road is distance-dependent; this corridor sits below where Mexican rail demonstrably competes |
| **Revealed traffic** | The road that actually parallels the alignment through the Cañada carries **10–34 articulated veh/day**. The 500/day figure is measured on MEX-135D, which runs the **Mixteca** — its intermediate destinations are **not on the railway** |
| **Operator economics** | **FIT has never covered its operating costs**: an operating loss in all six published years, 2024 cost recovery **16.2%**, costs 6.2× revenue, best year 36.2% |
| **Permitting** | A second, independent constraint that binds regardless of economics — see below |

### The environmental constraint

The Tehuacán-Cuicatlán reserve has **no core or buffer zones** — the
*declaratoria* set only a general polygon. The binding instrument is subzonal,
and the **only** subzone permitting general infrastructure construction is
*Aprovechamiento Especial*: **239.2 ha, 0.049% of the reserve**, across 14
polygons that are without exception quarries, salt works and a landfill. A
216.5 km alignment at a 20 m right-of-way would cover ~433 ha — **1.8× that
entire subzone**.

Caveats that cut the other way are stated in the screen: the railway predates
the reserve by a century and is mapped as an existing feature; rehabilitation
might be *maintenance* rather than *construction*; and **no GIS overlay was
performed**, so which subzones are actually crossed is not established.

### What is not concluded

- **Step 6 public-benefit case is bounded, not measured.** Required external
  benefit is 0.11–0.19 MXN/ton-km at 50% capture (modest, plausibly met by
  avoided road damage, accidents and CO₂), rising to 1.29–1.58 at 15% capture.
  A negative freight revenue case is not a negative public-benefit case.
- **No Mexican capital unit cost** was obtained. World Bank track-renewal costs
  are substituted and labelled as an international transfer.
- **Corridor legal history** is unverified against the primary record — DOF and
  Wayback are both egress-blocked.

---

## Status

| | |
|---|---|
| **Phase** | 4 — verdict issued; all six method steps addressed |
| **Sources** | 11 retrieved, 9 primary, all extracted and committed |
| **Aforo extraction** | 1,102 stations validated, 2 rejected (99.8%) |
| **Stop rules** | SR-7 evaluated (does not fire) · SR-2 evaluated (does not fire) · SR-3 evaluated (resolves negative) |
| **Open** | GIS overlay · Mexican capital unit cost · INEGI bottom-up cross-check · DOF legal history |

`CLAUDE.md` supersedes this table.

---

## Repository layout

```
Prompt.md                              authoritative task definition
CLAUDE.md                              live state — read first
README.md                              this file

sources/raw/                           downloaded originals (gitignored)
sources/extracted/<id>/document.md     committed evidence chain

analysis/breakeven_model.xlsx          6-sheet model, populated, live formulas
analysis/scripts/
  fetch_source.sh                      download + SHA-256 + manifest row
  extract_source.py                    PDF -> committed markdown
  extract_aforo.py                     DGST aforo tables -> validated records
  build_breakeven_model.py             regenerates the workbook
  supportable_capital.py               the screen inverted: capital ceiling
  step6_benefit_threshold.py           Step 6 inverted: required external benefit
  check_repo_hygiene.sh                pre-commit size/content guard

deliverables/
  feasibility_screen.md                the verdict and its basis
  data_sources.md                      manifest, extraction confidence, what was NOT obtained
  risk_register.md                     risks to the conclusion

working/
  source-access-log.md                 SR-7 evidence: reachable vs blocked
  sr2-evaluation.md                    SR-2 gradient and the corrected bound
  margin-derivation.md                 ARTF margin, derived step by step
  operator-economics.md                FIT vs Ferrosur cost recovery
  capital-benchmarks.md                World Bank unit costs vs the ceiling
  environmental-permitting.md          CONANP subzones
  step3b-commodity-and-haul.md         haul distance vs corridor length
  aforo_stations.json                  1,102 validated station records
```

---

## Reproducing

```bash
pip install -r analysis/scripts/requirements.txt

bash   analysis/scripts/fetch_source.sh <source-id> <url>   # download + hash
python3 analysis/scripts/extract_source.py <source-id>      # -> committed markdown
python3 analysis/scripts/extract_aforo.py sct-2025-datosviales-oaxaca \
                                          sct-2025-datosviales-puebla
python3 analysis/scripts/build_breakeven_model.py           # regenerate workbook
python3 analysis/scripts/supportable_capital.py
python3 analysis/scripts/step6_benefit_threshold.py
bash   analysis/scripts/check_repo_hygiene.sh               # before committing
```

The workbook is **generated, not hand-edited**, so the model's structure is
reviewable as code rather than as a binary diff. Change the script, not the file.

### Government-source access — the non-obvious part

`www.gob.mx/<agency>`, `www.sct.gob.mx`, `www.imt.mx` and `www.conanp.gob.mx`
serve **bot-challenge pages**: HTTP 200 with a ~1821-byte "Challenge Validation"
body. **A gob.mx HTTP 200 is not access** — check body content, never status.

The same institutions serve their document trees unchallenged from other paths:

| Route | Serves |
|---|---|
| `micrs.sct.gob.mx/images/DireccionesGrales/DGST/…` | SICT/DGST Datos Viales |
| `imt.mx/archivos/Publicaciones/…` (bare domain) | IMT publications |
| `www.gob.mx/cms/uploads/attachment/file/<id>/…` | **any gob.mx attachment**, incl. the ARTF Anuario |
| `simec.conanp.gob.mx/pdf_libro_pm/…` | CONANP management programmes |
| `documents1.worldbank.org/curated/…` | World Bank reports |

The third is the general case: find the attachment ID via search, fetch the CDN
path directly.

**Blocked and reported, not circumvented:** DOF and `web.archive.org/web/`
capture paths (egress policy); IADB, UNESCAP, PPIAF, `whc.unesco.org` (403);
SIAP and `proyectosmexico.gob.mx` (will not connect). Bot challenges were not
defeated.

---

## Evidence chain

```
deliverable claim
  └─ cites → sources/extracted/<source-id>/document.md
       └─ extracted from → raw document (SHA-256 in data_sources.md)
            └─ retrieved from → URL + date in data_sources.md
```

A claim that cannot complete this chain is tagged `[UNSOURCED]`,
`[ANALOGUE: <project>]` or `[ESTIMATE: <method>]` and cannot support a
conclusion. Press sources never support one alone. Raw PDFs are gitignored;
reproducibility comes from the URL, date and hash, not from committing the
binary.

### Two extraction hazards, both confirmed in these documents

- The DGST pages are **rotated 90°**: a station is a column of constant *x*, a
  field a band of constant *y*. Reading-order text interleaves the columns.
  Records are rebuilt from word bounding boxes and validated against three
  arithmetic identities before use.
- The class label is **`T3S2`, not `T3-S2`**. The hyphenated form — which the
  brief's own search strings use — matches nothing and reads as absent data.

---

## Scope boundary

In scope: corridor traffic and its composition, breakeven tonnage, order-of-
magnitude capital, institutional and legal posture, environmental permitting,
and the risks that would invalidate any of the above.

Out of scope: alignment engineering, geotechnical survey, environmental impact
assessment, rolling-stock procurement, financial structuring, and consultation
with affected communities. **Track condition cannot be resolved from a desk**
and is the load-bearing unknown behind SR-3.

This is a screening study. Ranges, not false precision. A negative screen is an
argument against spending more on study — it is not an engineering judgement
that the line cannot be rebuilt.
