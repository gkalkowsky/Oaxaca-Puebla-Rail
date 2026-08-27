# Data Sources

The reproducibility record for this screen. Raw documents are **not** committed
(see `.gitignore`); this file is what makes them re-fetchable. Extracted
markdown under `sources/extracted/` **is** committed and is what deliverables
cite.

**Status: three primary sources retrieved (2026-08-27).** Access to Mexican
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

All three are born-digital (text layer present), extracted with `pymupdf`.
Identity of each was verified by reading page 1, not by trusting the filename.

**Not yet obtained** — see `working/source-access-log.md` for the full probe log:

| Wanted | Blocker | Consequence |
|---|---|---|
| DOF notices (2003 condition, 2012 concession exclusion, 2023 FIT assignment) | Egress policy denial on `www.dof.gob.mx` | Corridor legal history unverifiable from the primary record |
| Wayback captures | Egress policy blocks `web.archive.org/web/` capture paths | The brief's designated fallback for link rot is unavailable |
| ARTF *Anuario Estadístico Ferroviario* | `www.gob.mx/artf` returns a bot-challenge page | Rail contribution margin per ton-km not yet sourced; Manual Estadístico gives aggregate ton-km only |
| UNESCO property 1534 boundary | `whc.unesco.org` HTTP 403 | Biosphere-reserve zoning overlap not yet determinable |

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

## 4. Retrieval targets — Phase 1

Candidate sources to locate, not yet retrieved or verified. Institution names
are search starting points; actual document titles and availability are
unconfirmed until a manifest row exists.

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
