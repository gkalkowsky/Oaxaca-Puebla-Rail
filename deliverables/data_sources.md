# Data Sources

The reproducibility record for this screen. Raw documents are **not** committed
(see `.gitignore`); this file is what makes them re-fetchable. Extracted
markdown under `sources/extracted/` **is** committed and is what deliverables
cite.

**Status: eleven sources retrieved (2026-08-27), nine primary.** Access to Mexican
government hosts is partly blocked; the routing that worked, and what remains
unobtainable, is recorded in §1 and in `working/source-access-log.md`.

---

## 1. Manifest

One row per retrieved document. Never edit a row after its extraction is
committed; supersede it with a new row and mark the old one `superseded`.

| ID | Title | Publisher | Type | URL | Retrieved (UTC) | SHA-256 | Extracted to | Status |
|----|-------|-----------|------|-----|-----------------|---------|--------------|--------|
| `sct-2025-datosviales-oaxaca` | Datos Viales 2025 — Oaxaca (data year 2024) | SICT / DGST | primary | https://micrs.sct.gob.mx/images/DireccionesGrales/DGST/Datos_Viales_2025/20_DV2025_Oaxaca.pdf | 2026-08-27 | `adceb7b1a17c2b21977dbeef94d86907ca44904e6c0364c2a0b03ea4baa82ff4` | `sources/extracted/sct-2025-datosviales-oaxaca/` | active |
| `sct-2025-datosviales-puebla` | Datos Viales 2025 — Puebla (data year 2024) | SICT / DGST | primary | https://micrs.sct.gob.mx/images/DireccionesGrales/DGST/Datos_Viales_2025/21_DV2025_Puebla.pdf | 2026-08-27 | `b6c37c73bd1876dd867ec3cd37fa61d80f3252be327610db50b5162981db1929` | `sources/extracted/sct-2025-datosviales-puebla/` | active |
| `imt-2023-manual-estadistico` | Manual Estadístico del Sector Transporte 2023 | IMT | primary | https://imt.mx/archivos/Publicaciones/Manual/mn2023.pdf | 2026-08-27 | `01ecb7aec3b9ed78811286aa136da44e3deb452ba37a50370c1d05f6de020765` | `sources/extracted/imt-2023-manual-estadistico/` | active |
| `artf-2024-anuario-ferroviario` | Anuario Estadístico Ferroviario 2024 | ARTF / SICT | primary | https://www.gob.mx/cms/uploads/attachment/file/1020005/Anuario_2024_P.pdf | 2026-08-27 | `526fcb0cf407213228c6eb74f8be3b63abc830147c256b749c49c1f9e254a5fd` | `sources/extracted/artf-2024-anuario-ferroviario/` | active |
| `artf-2023-anuario-ferroviario` | Anuario Estadístico Ferroviario 2023 | ARTF / SICT | primary | https://www.gob.mx/cms/uploads/attachment/file/920778/Anuario_2023_ARTF.pdf | 2026-08-27 | `cdc6d2aefee528a407064e5e054d35a91709a6baafe53ffcdf0d0901d96bc8eb` | `sources/extracted/artf-2023-anuario-ferroviario/` | active |
| `fit-2021-programa-inversion` | Programa Institucional 2021-2024 FIT — Avance y Resultados 2021 | FIT (SEMAR) | primary | https://www.gob.mx/cms/uploads/attachment/file/735993/47_PI_FIT_AyR21.pdf | 2026-08-27 | `87e4e41d969719f669dc8b56af533cedf13fa4ded29579f72ffc811930aea1fc` | `sources/extracted/fit-2021-programa-inversion/` | active |
| `ciep-2024-infraestructura-ferroviaria` | Infraestructura Ferroviaria: Presupuesto 2013-2024 | CIEP | secondary | https://ciep.mx/wp-content/uploads/2024/10/Infraestructura-ferroviaria.-Presupuesto-2013-2024.pdf | 2026-08-27 | `948485e47e8dd24ffde16a84dbd87b18c95a3b4a6e745a2f2a4ca6c4dca4a654` | `sources/extracted/ciep-2024-infraestructura-ferroviaria/` | active |
| `wb-2020-serbia-railways-lcc` | Serbia Railways Asset Management Plan Using Life-Cycle Costs (AUS0001540) | World Bank | primary | https://documents1.worldbank.org/curated/en/726091593064265592/pdf/Serbia-Railways-Asset-Management-Plan-Using-Life-Cycle-Costs.pdf | 2026-08-27 | `9894572c04566eb7dd6a13045b95bdb6000ce09e1a3f9d2addd15f4b961e3f8e` | `sources/extracted/wb-2020-serbia-railways-lcc/` | active |
| `itf-2020-road-rail-cba` | Comparing Road and Rail Investment in Cost-Benefit Analysis (ITF Discussion Paper) | OECD / ITF | secondary | https://www.oecd.org/content/dam/oecd/en/publications/reports/2020/12/comparing-road-and-rail-investment-in-cost-benefit-analysis_8452f4cb/71792956-en.pdf | 2026-08-27 | `eb3a93a2c59c8b6ed62fcdc664e585b1743d39637538bdbbaff8886b60c45d7c` | `sources/extracted/itf-2020-road-rail-cba/` | active |
| `imt-pt179-costos-operacion-vehicular` | Análisis de Costos de Operación Vehicular del Autotransporte de Carga (Publicación Técnica 179, 2001) | IMT | primary | https://imt.mx/archivos/Publicaciones/PublicacionTecnica/pt179.pdf | 2026-08-27 | `27e7a5e65adc855e73313e095b1a5f2d91b5d280cb8c4594547731b3730a04d2` | `sources/extracted/imt-pt179-costos-operacion-vehicular/` | active |
| `conanp-2013-pm-tehuacan-cuicatlan` | Programa de Manejo Reserva de la Biosfera Tehuacán-Cuicatlán (2013) | CONANP | primary | https://simec.conanp.gob.mx/pdf_libro_pm/123_libro_pm.pdf | 2026-08-27 | `727e4d810d2661ef23131f5981e5953e70df191cf6bd2e7239e9eb47f731ae30` | `sources/extracted/conanp-2013-pm-tehuacan-cuicatlan/` | active |

All three are born-digital (text layer present), extracted with `pymupdf`.
Identity of each was verified by reading page 1, not by trusting the filename.

**Not yet obtained** — see `working/source-access-log.md` for the full probe log:

| Wanted | Blocker | Consequence |
|---|---|---|
| DOF notices (2003 condition, 2012 concession exclusion, 2023 FIT assignment) | Egress policy denial on `www.dof.gob.mx` | Corridor legal history unverifiable from the primary record |
| Wayback captures | Egress policy blocks `web.archive.org/web/` capture paths | The brief's designated fallback for link rot is unavailable |
| ~~ARTF *Anuario Estadístico Ferroviario*~~ | **RESOLVED.** The HTML page is bot-challenged, but the PDF is served unchallenged from `www.gob.mx/cms/uploads/attachment/file/...` | Margin obtained: Ferrosur EBIT $0.402/ton-km |
| Mexican rehabilitation unit cost per km | ASF serves a JS application; `proyectosmexico.gob.mx` will not connect (HTTP 000); `ppiaf.org` and `ppp.worldbank.org` return Cloudflare challenges; DOF egress-blocked | **Still unsourced for Mexico.** Substituted with a World Bank international benchmark, clearly labelled as a transfer |
| UNESCAP light-rehabilitation figure at source | `unescap.org` HTTP 403 | Brief's `< USD 500,000/route-km` could not be verified directly. **Corroborated independently** by World Bank partial-renewal unit costs |
| The brief's "~89% of benefits from road operating cost" | Not located in any retrieved source | Step 6's benefit structure is **unverified**. Recorded rather than repeated as fact |
| IADB publications | `publications.iadb.org` HTTP 403 challenge | Latin American rail benchmarks unavailable from that source |
| UNESCO property 1534 boundary | `whc.unesco.org` HTTP 403 (both the listing and the document endpoint) | **Substantially mitigated.** The CONANP *programa de manejo* supplies the operative Mexican zoning instrument, which is what governs permitting. The UNESCO inscription boundary remains unobtained |
| Subzone polygon geometry (shapefile) | Not located in PDF form | Which subzones the alignment crosses is **not established**; no GIS overlay performed |

Column rules:

- **ID** — `<pub>-<yyyy>-<slug>`, e.g. `sict-2024-pnid`. Stable forever; it is
  what citations point at.
- **Type** — `primary` (issuing body's own document: statute, budget line,
  concession title, official statistic), `secondary` (analysis of primary
  material), or `press` (news reporting). A conclusion may not rest on `press`
  alone.
- **Retrieved** — UTC date the file was downloaded, not the document's date.
- **SHA-256** — of the raw file as downloaded. Detects silent republication.
- **Status** — `active`, `superseded`, `paywalled`, `dead-link`, `unavailable`.

## 1b. Extraction method and confidence

| ID | Extractor | Text layer | Confidence | Basis |
|---|---|---|---|---|
| `sct-2025-datosviales-oaxaca` | `pymupdf` word bounding boxes | born-digital | **high** | 502 records, 1 rejected. Three arithmetic identities enforced per record |
| `sct-2025-datosviales-puebla` | `pymupdf` word bounding boxes | born-digital | **high** | 600 records, 1 rejected |
| `imt-2023-manual-estadistico` | `pymupdf` reading order | born-digital | **medium** | Narrative and table text read cleanly; no per-record validation applied, figures used only qualitatively so far |

No OCR was used. All three documents carry a text layer, so per the brief's own
routing rule the text-layer path is correct and full-page VLM was not run.

**Validation identities applied to every aforo record** (failures excluded, not
patched):

1. `A + B + C2 + C3 + T3S2 + T3S3 + T3S2R4 + OTROS + M = 100`
2. `C2 + C3 + T3S2 + T3S3 + T3S2R4 + OTROS = C_agg`
3. `A + M = A_agg`

Result: **1,102 validated / 2 rejected (99.8%)**. Both rejects are unnamed rows
on a summary page. Identity (1) is why `M` (motos) matters: without it the
detailed classes sum to ~92.6 and appear corrupt.

**Two extraction hazards confirmed in these documents:**

- The pages are **rotated 90°**. A station is a column of constant *x* and a
  field is a band of constant *y*; reading-order text interleaves the columns.
  Records must be rebuilt from bounding boxes.
- The class label is **`T3S2`, not `T3-S2`**. The hyphenated form — which the
  brief's own search strings use — matches nothing and reads as absent data.

## 1c. Secondary and press material consulted, not relied upon

Recorded for traceability. Per §1 rules, `press` may not solely support a
conclusion, and none of the below carries any figure in the screen.

| Topic | Nature | Status |
|---|---|---|
| Línea Z rehabilitation spend (~18,000 MXN million, ~300 km) | Press (El Universal, El Sol de Chiapas) | **UNVERIFIED.** Used only as order-of-magnitude context in a clearly labelled model cell. ASF primary is a JS application; direct PDF paths 404 |
| Contract FIT-GARMOP-OP-Z-13-2022; rail specification substitution (115 vs 136 lb/yd) | Press reporting of ASF findings | **UNVERIFIED.** Carried in the risk register as press-sourced |

## 2. Retrieval protocol

```bash
bash analysis/scripts/fetch_source.sh <source-id> <url>   # downloads + hashes + stubs a manifest row
python3 analysis/scripts/extract_source.py <source-id>    # PDF -> sources/extracted/<source-id>/
```

1. Download to `sources/raw/<source-id>.<ext>` — never rename or edit it.
2. Record URL, publisher, retrieval date and SHA-256 in the manifest above.
3. Extract to `sources/extracted/<source-id>/` (`document.md` plus any
   `tables/*.json`) and commit the extraction.
4. **Check this manifest before fetching anything.** A source already listed
   `active` with an extraction present is not re-downloaded or re-extracted.

## 3. Dead links and paywalls

Mexican federal sites reorganise often and links die across administrations.
When a URL is dead, record the original URL, mark it `dead-link`, and note the
recovery route tried (Wayback Machine snapshot, DOF search by date, an INAI
transparency request). A source that cannot be recovered stays in the manifest
with `status: unavailable` — the gap in the evidence chain must be visible,
not silently dropped.

## 4. Retrieval targets — status

The original Phase 1 target list, annotated with what was obtained. Items
without a manifest row in §1 were not retrieved; the blocked table above says
why for each.

**Corridor and terrain**
- INEGI — continuo de elevaciones mexicano (DEM), topographic and locality data
- INEGI — Red Nacional de Caminos (road network baseline for the competing mode)

**Existing rail assets and their condition**
- ARTF (Agencia Reguladora del Transporte Ferroviario) — network maps,
  concession registry, annual rail statistics
- SICT (Secretaría de Infraestructura, Comunicaciones y Transportes) — rail
  programme documents, published project profiles
- Concessionaire disclosures for the corridor's existing freight lines
- Historical alignment records for any abandoned or out-of-service segment

**Demand**
- INEGI — census population and intercensal counts for both metropolitan areas
- SICT / SECTUR — intercity bus and air passenger volumes on the O-D pair
- Toll road traffic counts (aforos) on the competing highway corridor

**Cost**
- Comparable recent Mexican rail projects — published capital cost per km,
  with terrain class noted (an analogue is only usable if the grade profile is
  comparable)
- Federal budget documents (PEF) for any line item already allocated

**Institutional and legal**
- DOF (Diario Oficial de la Federación) — decrees, concession grants, any
  expropriation notices bearing on the corridor
- ASF (Auditoría Superior de la Federación) — audits of comparable rail
  programmes, for realised-versus-budgeted cost evidence

## 5. Citation format

In deliverables:

> Corridor length is NNN km `[sict-2024-pnid: document.md §4.2]`

Unsourced or carried-over numbers must be tagged inline:

- `[UNSOURCED]` — no primary document behind it; cannot support a conclusion
- `[ANALOGUE: <project>]` — carried from a comparable project, named
- `[ESTIMATE: <method>]` — derived, with the derivation in `/working`
