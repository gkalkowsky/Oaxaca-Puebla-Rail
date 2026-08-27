# Task: Phase 0 feasibility screen, Puebla to Oaxaca City freight rail reactivation

## Context

The "Vía Corta Oaxaca" (rail line "E", Sánchez, Puebla to Oaxaca City, Oaxaca,
km E-150+000 to E-367+000, approximately 216.5 km) is a dormant standard-gauge
freight corridor. It follows the Tehuacán valley and Cañada de Cuicatlán river
valley system rather than crossing the Sierra Norte.

Known history:
- Built as Ferrocarril Mexicano del Sur, Puebla to Oaxaca, 367 km, opened
  November 1892. Originally narrow gauge; widened to standard gauge (1952 per
  some sources) to increase cargo capacity.
- Passenger and freight service under the state railway ended by May 2004.
- Tendered for concession twice in the late 1990s. Both tenders drew no bidders.
- August 1999: SCT imposed service obligations on Ferrosur under Art. 23 of the
  Ley Reglamentaria del Servicio Ferroviario. A 2003 DOF notice described the
  line as in "precarious condition" with service suspended during rainy season.
- October 2012: the segment was excluded from Ferrosur's concession and reverted
  to the federal government, free of liens.
- April 2023: assigned to Ferrocarril del Istmo de Tehuantepec (FIT), the
  state operator (under SEMAR) that runs the Tren Interoceánico.

Facilities on record (2003 DOF): freight stations at Etla and Hacienda Blanca;
travel inspection centers at Tomellín and Oaxaca; minor repair shop and supply
yard at Oaxaca.

Verify all of the above independently. Treat it as a starting point, not fact.

## Objective

Do NOT forecast demand. Back-solve for breakeven tonnage, then test whether the
corridor actually moves that much in rail-divertible commodity classes. Produce
a defensible go / no-go screening recommendation at concept level.

A clean negative is a valid and useful deliverable. Do not soften a failing
result. An honest "indeterminate" is also a valid deliverable. See the stop
rules below.

## Method

### Step 1: Capital cost band

Planning-level estimate for rehabilitation of 216.5 route-km of existing
single-track alignment.

- Start from published benchmarks for rehabilitation of existing mixed-traffic
  lines (UNESCAP railway master plan guidance cites under USD 500,000/route-km).
- Prefer Mexico-specific unit costs where obtainable: SICT/ARTF tender awards,
  Tren Interoceánico Línea Z rehabilitation contract values per km, CIIT
  published budgets. Deflate historical MXN figures to a stated base year and
  state the MXN/USD rate used.
- Adjust upward for canyon and fault-zone terrain (Cañada de Cuicatlán sits at
  the convergence of Sierra Madre Oriental and Sierra Madre del Sur folding).
- Present low / base / high band. Treat bridges, drainage structures, and slope
  stabilization as the dominant uncertainty and carry them as a separate line
  with its own range, not buried in a percentage contingency.

### Step 2: Back-solve breakeven tonnage

- 30-year asset life. Sensitivity across 5%, 6%, 8% cost of capital.
- Research actual Mexican rail contribution margin per ton-km (ARTF publishes
  rail statistics: Anuario Estadístico Ferroviario). Do not silently substitute
  US Class I figures; if you must use a proxy, label it as such and show the
  sensitivity to that assumption.
- Add a fixed O&M layer. Note that track maintenance cost scales with gross
  passing tonnage, so O&M is not independent of the demand answer. Handle the
  circularity explicitly (iterate or bound it).
- Output at each sensitivity point: required tons/year, and the equivalent in
  loaded truckloads/day each way, so the result is directly comparable to
  observable road traffic.

### Step 3: Count what actually moves

Sources, in priority order:
- SICT "Datos Viales" and aforo vehicular (automatic counting station data) for
  corridor highways, principally 135D and 190, Tehuacán to Oaxaca City. Extract
  TDPA by vehicle classification, isolating articulated truck classes
  (C2, C3, T3-S2, T3-S3, T3-S2-R4, etc.).
- IMT (Instituto Mexicano del Transporte) publications, including the Manual
  Estadístico del Sector Transporte and any corridor-level freight studies.
- INEGI Encuesta Anual de Transporte de Carga (EATC) and Censos Económicos for
  commodity tonnage and transport establishment data.
- INEGI / Data México trade and production data for Oaxaca and Puebla by
  commodity.
- SIAP (agricultural production) for volume by crop, since agricultural output
  is a large share of Oaxaca's tradeable goods.

Then perform COMMODITY SEGREGATION. This is the decisive analytical step:
- Split observed tonnage into rail-divertible classes (cement, aggregate,
  fertilizer, grain, fuel, steel, containerized manufactured goods) versus
  low-diversion classes (refrigerated, time-sensitive, high-value low-density
  agricultural exports such as mezcal, coffee, avocado, mango, figs).
- Apply realistic mode-diversion rates by commodity class, each with a cited
  source. State the diversion rates as an explicit, editable assumption block,
  because the answer is highly sensitive to them.
- Correct for empty trips. Published estimates put empty running at roughly
  30 to 50 percent for trucks. Do not treat raw truck counts as loaded tonnage.

### Step 4: Compare and recommend

Set divertible tonnage against breakeven tonnage. State whether the project
clears, fails, is marginal, or is indeterminate, and by what factor. Give the
result as a range tied to the sensitivity cases, not a single number. Apply the
stop rules below before issuing any recommendation.

### Step 5: Risk register

At minimum:
- UNESCO World Heritage / Tehuacán-Cuicatlán Biosphere Reserve. Determine
  whether the right-of-way passes through core zones, buffer zone, or outside
  the property boundary. Obtain the UNESCO nomination boundary description
  (property ref. 1534) and the CONANP reserve management program. Assess
  implications for permitting scope, MIA (Manifestación de Impacto Ambiental)
  level required, and limits on alignment modification, grading, and drainage.
- Right-of-way integrity after 20+ years dormant: encroachment, squatting,
  title, and consent requirements where the alignment crosses bienes comunales
  or ejido land. Note that Sierra Norte and Cañada communities govern by
  Sistemas Normativos Indígenas, meaning community assembly consent is a real
  gate, not a formality. Note also that UCIZONI and other community
  organizations have publicly opposed rail megaprojects in Oaxaca.
- Institutional and delivery risk. Reference the ASF (Auditoría Superior de la
  Federación) findings on the 2019 Línea Z rehabilitation, the 28 December 2025
  Asunción Ixtaltepec derailment (14 dead, 98 injured), the July 2026 freight
  derailment in the same zone, and the FGR determination. Assess what this
  implies for confidence in the current assignee's rehabilitation delivery.
- Seasonal and geotechnical: documented rainy-season service suspension,
  slope stability, scour at water crossings.

### Step 6: Benefit-cost framing

If the pure revenue case is marginal or negative, test whether a public-benefit
case is plausible.
- In comparable studies, reduced road transport operating cost accounts for
  roughly 89 percent of measured benefits, with CO2 and road accident reduction
  around 3 percent each. Build the case on that structure.
- Quantify highway operating cost savings, pavement wear avoided, and consumer
  price impact for central valley and Sierra Norte communities.
- Identify plausible funding mechanisms: federal (SICT/ARTF, Programa Nacional
  Ferroviario), multilateral (IDB, World Bank, CAF transport lending), and any
  Plan Sur / regional development instruments.

## PDF extraction

Many Mexican transport datasets are PDF-only. Do not skip a source because it
is a PDF, and do not eyeball numbers out of a rendered page.

Tooling:
- PRIMARY: datalab-to/marker (https://github.com/datalab-to/marker).
  Text-layer-first with selective OCR. Use for born-digital PDFs. CPU-only path
  available for born-digital documents. Outputs markdown plus JSON with
  bounding boxes.
- FALLBACK: opendatalab/MinerU (https://github.com/opendatalab/mineru).
  Full-page VLM plus OCR dual engine, 109 languages. Use only when a page has
  no usable text layer.
- Check for a text layer first (pdffonts / pdftotext) and route accordingly.
  Do not run full-page VLM on clean born-digital tables.

Extraction discipline, this matters more than tool choice:
- Target data is TABULAR: station ID, highway segment, year, TDPA, and
  percentage or count by vehicle classification. Column misalignment silently
  corrupts the entire downstream analysis.
- VALIDATE every extracted table before use:
  * vehicle class percentages sum to 100 (+/- rounding), or class counts sum to
    the stated total
  * TDPA values are plausible order of magnitude for the segment
  * station IDs and highway designations reconcile across years
- Any table failing validation: re-extract with the fallback engine, compare
  outputs, and if they still disagree, flag the value as unverified rather than
  using it.
- Persist raw extracted markdown/JSON alongside parsed values so every number in
  the memo traces to a specific page of a specific document.
- Log extraction confidence per table. State which figures came from clean
  text-layer extraction versus OCR of a scan.

## Spanish search strings to try verbatim

Aforo / traffic:
"datos viales" SCT Oaxaca
"aforo vehicular" carretera 135D Tehuacán Oaxaca
"TDPA" carretera federal 190 Oaxaca estación de conteo
IMT "estudio de aforo" corredor Puebla Oaxaca
"volumen de tránsito" clasificación vehicular T3-S2 Oaxaca

Rail line specifics:
"vía corta Oaxaca" línea E Sánchez Oaxaca rehabilitación
"Ferrocarril Mexicano del Sur" ramal Oaxaca estado de la vía
"derecho de vía" ferroviario Oaxaca invasión abandono
ARTF "Anuario Estadístico Ferroviario" carga toneladas-kilómetro
DOF "vía corta Oaxaca" concesión asignación

Cost benchmarks:
SICT licitación rehabilitación vía férrea costo por kilómetro
"Tren Interoceánico" Línea Z rehabilitación monto contrato kilómetro
ASF auditoría rehabilitación ferroviaria Istmo

Environmental / land:
CONANP "Tehuacán-Cuicatlán" programa de manejo zonificación
"Manifestación de Impacto Ambiental" ferroviario reserva de la biosfera
"bienes comunales" Cuicatlán derecho de vía ferrocarril

## Known limitations to plan around, not discover late

Read this section before starting and design the workflow around it.

1. AFORO DATA GIVES VEHICLES, NOT TONNAGE OR COMMODITY. Counting stations
   classify by axle configuration only. There is no commodity field. You cannot
   derive commodity mix from aforo data. You must bridge from vehicle counts to
   tonnage using payload assumptions by vehicle class, and to commodity mix
   using separate production and trade data. Both bridges are assumptions.
   Make them explicit and show sensitivity.

2. AFORO IS LINK VOLUME, NOT ORIGIN-DESTINATION. A truck counted on 135D may be
   through-traffic bound for Chiapas, the Isthmus, or Guatemala, not
   Puebla-Oaxaca corridor freight. Naive use overcounts addressable demand,
   possibly badly. See stop rule 2 below.

3. NO CURRENT TRACK CONDITION DATA EXISTS PUBLICLY. The most recent condition
   statement on record is the 2003 "precarious condition" language, now over
   two decades old. Degradation of unmaintained track is nonlinear. This is the
   load-bearing unknown for capital cost and it CANNOT be resolved from a desk.
   Do not manufacture a condition assumption. Bound it: present capital cost
   under "light rehabilitation," "heavy rehabilitation," and "substantial
   reconstruction" scenarios. If satellite or street-level imagery can indicate
   whether rail is still in place and the ROW is clear, use it and say so, but
   do not overclaim what imagery can show about tie, ballast, or structure
   condition. See stop rule 3 below.

4. RAIL TARIFF AND MARGIN DATA IS PARTLY CONFIDENTIAL. ARTF publishes aggregate
   statistics but commodity- and corridor-specific contribution margins are
   commercially sensitive. Expect to work from aggregate averages. Show how the
   breakeven answer moves across a plausible margin range rather than presenting
   one figure.

5. RIGHT-OF-WAY TITLE AND COMMUNAL LAND STATUS IS LIKELY NOT WEB-ACCESSIBLE.
   RAN (Registro Agrario Nacional) and public property registry records
   generally require formal request or in-person query. Identify which
   municipalities and agrarian nuclei the alignment crosses using available
   cartography, and produce a list of required inquiries rather than a
   conclusion.

6. NO PUBLIC BRIDGE OR STRUCTURE INVENTORY IS LIKELY TO EXIST for this line.
   Treat structures as a bounded unknown and say so.

7. SANDBOX NETWORK RESTRICTIONS. The execution environment may block .gob.mx and
   other non-allowlisted domains. Test access to a representative government
   source EARLY, before building any pipeline. See stop rule 7 below.

8. GOVERNMENT PORTAL INSTABILITY AND LINK ROT. SICT/SCT portals have been
   restructured repeatedly and older releases move or disappear. Use Wayback
   Machine captures where live links fail, and record the capture date. Some
   series have gaps or methodology changes between years; check for definitional
   breaks in vehicle classification schemes before comparing across years.

9. CURRENCY, INFLATION, AND BASE YEAR. Mexican cost figures span decades of
   significant inflation and exchange rate movement. Deflate to a single stated
   base year using INEGI INPC, and state the MXN/USD rate and its date for every
   converted figure. Never mix nominal figures across years.

10. SPANISH-LANGUAGE PRIMARY SOURCES AND TERMINOLOGY. Search in Spanish. Key
    terms: aforo vehicular, TDPA (tránsito diario promedio anual), datos viales,
    vía corta, derecho de vía, bienes comunales, Manifestación de Impacto
    Ambiental, kilometraje. English-only searching will miss most of the
    primary material.

11. SESSION LENGTH AND CONTEXT. This is a long task. Checkpoint work to disk
    continuously. Write intermediate findings to files as you go rather than
    holding them in context. If the session is interrupted, the work products on
    disk should be sufficient to resume without redoing retrieval.

## Detection and stop rules

These govern whether you are permitted to issue a recommendation at all. You
have explicit permission to decline to conclude. Manufacturing a conclusion to
satisfy the deliverable spec is the worst possible outcome of this task.

STOP RULE 2, through-traffic contamination:
DETECT: compare TDPA on corridor segments north of Tehuacán, mid-corridor, and
immediately north of Oaxaca City. If articulated truck volume does not decline
materially approaching Oaxaca City, the count is dominated by through-traffic
and the raw number is NOT addressable corridor demand.
BOUND: use the differential between corridor-entry and corridor-terminus truck
volume as the upper bound on corridor-internal freight. Cross-check against an
independent estimate built bottom-up from Oaxaca state production and
consumption tonnage (SIAP, INEGI Censos Económicos), which has no through-
traffic component at all. If the two methods disagree by more than a factor of
2, report both and do not average them.
STOP: if neither a directional gradient nor a bottom-up cross-check can be
constructed, state that addressable demand could not be bounded, and do not
issue a go/no-go. An unbounded demand figure is not a conservative estimate,
it is an unknown.

STOP RULE 3, track condition:
DETECT: after computing capital under light rehabilitation, heavy
rehabilitation, and substantial reconstruction, check whether the breakeven
conclusion is consistent across all three.
STOP: if the scenarios straddle the breakeven threshold, meaning the project
clears under one and fails under another, the correct output is
"INDETERMINATE, pending field reconnaissance," with the specific scope of
recon required and its estimated cost. Do not select a base case and present
a conclusion. Report which scenario the answer flips at, since that is the
single most decision-relevant number in the study.

STOP RULE 7, network access:
STOP: if primary Mexican government sources are inaccessible and no adequate
substitute is found for the aforo or tonnage data specifically, abort the
screening analysis and deliver a data-availability report instead. A screening
recommendation built entirely on secondary and tertiary sources is worse than
no recommendation, because it carries unearned authority.

## Deliverables

Write to disk and present:
1. `feasibility_screen.md` - full memo, engineering-report tone, assumptions
   stated inline, every external figure cited with source, date, and retrieval
   method. If a stop rule triggered, lead with that.
2. `breakeven_model.xlsx` - capital cost band, cost-of-capital sensitivity,
   tonnage back-solve, commodity segregation, and diversion-rate assumptions as
   LIVE FORMULAS, not hardcoded values. All assumptions in a single editable
   input block at the top so a reviewer can rerun the case.
3. `data_sources.md` - every source consulted with URL, retrieval date, what was
   obtained, extraction method and confidence, plus an explicit list of what
   could NOT be obtained and what it would take to get it.
4. `risk_register.md` - risks with likelihood, impact, and what would retire each.

## Standards

- Search in Spanish, but write all deliverables in English. Preserve Spanish
  technical terms and official document titles verbatim rather than translating
  them, so figures remain traceable to their source.
- Distinguish rigorously between retrieved data and your own assumptions. Label
  assumptions as assumptions every single time they appear.
- Where a figure cannot be obtained, say so and state what it would take to get
  it. Do not fabricate, and do not silently substitute a proxy for the real thing.
- Flag any figure older than 5 years as potentially stale.
- Present ranges, not false precision. This is a screening study.
- If the screen fails, say it fails. If it cannot conclude, say that instead.
