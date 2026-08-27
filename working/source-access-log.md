# Source access log — Stop Rule 7 determination

Probed 2026-08-27 from the sandboxed execution environment. This log is the
evidence for the Stop Rule 7 decision and feeds the "what could NOT be
obtained" section of `deliverables/data_sources.md`.

**Determination: STOP RULE 7 DOES NOT FIRE.** The two decisive dataset
families — road aforo/TDPA by vehicle classification, and rail freight
tonnage/ton-km — were both obtained from primary Mexican government sources.
Access required routing to alternative official hosts, documented below.

---

## Two distinct failure modes, not one

Blocked sources failed for two different reasons that must not be conflated:

1. **Egress policy denial** — the environment's proxy refuses the host.
   Reported, not circumvented, per the environment's proxy policy.
2. **Site-side bot challenge** — the host is reachable but returns a
   "Challenge Validation" interstitial (HTTP 200, ~1.8 KB) instead of content.
   Not circumvented: defeating bot protection is out of scope.

An HTTP 200 from a `gob.mx` host is **not** evidence of access. The challenge
page returns 200 with a plausible-looking body. Every probe below was checked
on body content, not status code.

## Blocked

| Host | Mode | Evidence |
|---|---|---|
| `www.dof.gob.mx` | Egress policy | `CONNECT tunnel failed, 502`; proxy status logged `connect_rejected … policy denial` for `www.dof.gob.mx:443` |
| `web.archive.org/web/<ts>/…` | Egress policy | HTTP 403, body `Blocked by egress policy` (24 bytes). Capture *content* is blocked though `archive.org/wayback/available` responds |
| `www.gob.mx/*` (ARTF, SICT, CONANP landing pages) | Bot challenge | HTTP 200, 1821 bytes, `<title>Challenge Validation</title>` |
| `www.sct.gob.mx` | Bot challenge | Same 1821-byte challenge page |
| `www.imt.mx` | Bot challenge | Cloudflare `cdn-cgi/challenge-platform` + redirect to gob.mx |
| `whc.unesco.org` | HTTP 403 | UNESCO property 1534 boundary description not retrieved this way |
| `datos.gob.mx` search API | HTTP 404 | Platform reachable; CKAN-style endpoints not found at documented paths |

**Consequence:** DOF is the authoritative record for the 2003 "precarious
condition" notice, the 2012 concession exclusion, and the 2023 FIT assignment.
Wayback was the designed fallback for link rot and is also unavailable. Both
routes named in the brief for these are closed. This is a real gap in the
corridor's legal/administrative history and is carried as such — it is not
worked around by substituting press reporting.

## Accessible — and the routing that made them work

| Source | Host | Result |
|---|---|---|
| **Datos Viales 2025, Oaxaca** | `micrs.sct.gob.mx` | 1.46 MB PDF, 36 pp, born-digital |
| **Datos Viales 2025, Puebla** | `micrs.sct.gob.mx` | 1.49 MB PDF, 50 pp, born-digital |
| **Datos Viales 2025, Introducción** | `micrs.sct.gob.mx` | 797 KB PDF (methodology, class definitions) |
| **Manual Estadístico del Sector Transporte 2023** | `imt.mx` (bare domain) | 6.3 MB PDF, 126 pp, born-digital |
| Datos Viales download portal | `appdatosviales.sctcloud.com.mx` | HTTP 200 over **http only** — https fails cert validation (`no alternative certificate subject name matches`). Not used; the direct PDFs are authoritative and served over https |
| INEGI | `www.inegi.org.mx` | Site and EATC programme pages reachable; `/app/api/indicadores/` returns 403 without a token |
| ASF | `www.asf.gob.mx` | Reachable, real content |

**The routing finding that unblocked this task:** `www.sct.gob.mx` and
`www.imt.mx` are bot-challenged, but the *same institutions* serve their
document trees from hosts that are not:

- `micrs.sct.gob.mx/images/DireccionesGrales/DGST/Datos_Viales_2025/<NN>_DV2025_<State>.pdf`
- `imt.mx/archivos/Publicaciones/…` (bare domain; `www.imt.mx` is challenged)

`<NN>` is the **INEGI state code** (20 = Oaxaca, 21 = Puebla). Both files were
verified by reading page 1, not by trusting the filename.

## What the accessible data does and does not contain

Verified by full-text search of the extractions, not assumed:

**Datos Viales (Oaxaca) — contains**
- `TDPA` on 21 of 36 pages
- Vehicle classification columns: `A, B, C2, C3, T3S2, T3S3, T3S2R4, OTROS`
- Station name, route (`MEX-`), km point, and **latitude/longitude**
- Data year **2024** inside the 2025 publication

Coordinates are what makes Stop Rule 2 testable: stations can be ordered along
the corridor geographically, so the articulated-truck directional gradient
between Tehuacán and Oaxaca City can actually be measured rather than assumed.

**Manual Estadístico 2023 — contains**
- `carga ferroviaria` (11 pages), `ton-km` (5 pages, incl. pp. 43, 54–61)

**Manual Estadístico 2023 — does NOT contain**
- `TDPA`: 0 pages. `aforo`: 0 pages. `datos viales`: 0 pages.
  It is **not** a substitute for the aforo data. Only the DGST state volumes are.

## Extraction hazards already identified

- **`T3-S2` matches nothing; the PDFs write `T3S2`.** The brief's own search
  string uses the hyphenated form. A search on the hyphenated string returns
  zero and would look like "the data is not there".
- **Reading-order extraction scrambles these tables.** In the raw text stream a
  station's detailed class percentages sum to ~92.6 while the aggregated
  `A/B/C` triple sums to 100.0 — the columns are interleaved, so column
  identity cannot be assigned from reading order. Any TDPA table must be
  reconstructed from **word bounding boxes**, then validated (classes sum to
  100 ± rounding) before use. This is exactly the silent corruption the brief
  warns about, and it is present in this document.

## Tooling state in this environment

- `poppler-utils` absent; `apt-get install` unavailable → no `pdftotext`/`pdffonts`.
- `pypdf` installs but crashes: system `cryptography` has a broken Rust binding
  (`ModuleNotFoundError: _cffi_backend` → `PanicException`).
- **`pymupdf` works** and gives word-level bounding boxes. Added to
  `extract_source.py` as the preferred extractor ahead of `pdftotext`.
- `marker` (brief's primary) not installed; it pulls torch and model weights.
  Text-layer check shows all three documents are born-digital, so the brief's
  own routing rule ("do not run full-page VLM on clean born-digital tables")
  says the text-layer path is correct here. Marker remains worth adding for
  table structure if bounding-box reconstruction proves insufficient.
