# Data Sources

The reproducibility record for this screen. Raw documents are **not** committed
(see `.gitignore`); this file is what makes them re-fetchable. Extracted
markdown under `sources/extracted/` **is** committed and is what deliverables
cite.

**Status: no sources retrieved yet.** The manifest below is empty by design —
Phase 0 is scaffold only.

---

## 1. Manifest

One row per retrieved document. Never edit a row after its extraction is
committed; supersede it with a new row and mark the old one `superseded`.

| ID | Title | Publisher | Type | URL | Retrieved (UTC) | SHA-256 | Extracted to | Status |
|----|-------|-----------|------|-----|-----------------|---------|--------------|--------|
| _(none yet)_ | | | | | | | | |

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
