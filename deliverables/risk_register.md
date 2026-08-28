# Risk Register — Vía Corta Oaxaca freight reactivation

Risks to the **screen's conclusion** and to the project's deliverability.
Screening level: likelihood and impact are judged on retrieved evidence, and
marked `unassessed` where there is none rather than guessed.

**Impact** = effect on a go/no-go if the risk is real. `fatal` would flip it;
`major` moves a headline figure by more than an order of magnitude; `moderate`
moves it materially; `minor` is noted for completeness.

## A. Environmental and protected-area

| ID | Risk | Likelihood | Impact | What would retire it |
|---|---|---|---|---|
| R-01 | **REFRAMED, THEN DOWNGRADED.** The reserve has no core/buffer zoning — only a general polygon (PM 2013 p.140), independently confirmed by CONANP's zonas-núcleo layer containing zero polygons for it. Internally, general infrastructure construction is permitted only in *Aprovechamiento Especial* (239.2 ha, 0.049%, all quarries/saltworks/landfill). **But the GIS overlay shows the Cañada valley floor is largely OUTSIDE the reserve**: all nine corridor waypoints test outside, and south of ~17.53°N there is no reserve at all. The alignment may run substantially outside the ANP | **medium** — margin is thin (<1 km at Tehuacán and Tecomavaca), not absent | **moderate**, downgraded from fatal | The rail centreline (never obtained; road stations are the proxy), then a SEMARNAT determination on construction-vs-maintenance for a pre-existing federal ROW. See `working/environmental-permitting.md` |
| R-02 | Rainy-season scour and slope instability along the Río Salado / Cañada. **Now corroborated by CONANP**, which identifies federal 135 Tehuacán-Cuicatlán among roads causing "inestabilidad de taludes, erosión, incendios" in the Cañada, and names right-of-way clearing as a fire-pressure source (PM 2013 pp. 81, 83) | **high** | major | Geotechnical reconnaissance; historical washout records from FIT/ARTF |
| R-03 | Structures (bridges, drainage) are the dominant capital uncertainty and **no public inventory is expected to exist** | high | major | Field structure survey. Carried in the model as its own line with its own range, never as a contingency percentage |

## B. Right-of-way, land and consent

| ID | Risk | Likelihood | Impact | What would retire it |
|---|---|---|---|---|
| R-04 | ROW encroachment and squatting after 20+ years dormant | medium-high | major | Satellite/street imagery for ROW clearance (indicative only); RAN and registry inquiry |
| R-05 | Alignment crosses **bienes comunales / ejido** land where consent runs through **Sistemas Normativos Indígenas** community assembly — a real gate, not a formality, not dischargeable by compensation. **Consent surface now sized**: the reserve alone spans 51 municipios, **130 comunidades y ejidos**, 250 localidades, ~36,000 inhabitants inside and ~600,000 in the zone of influence (PM 2013 p.137) | high | **fatal** | Municipality and agrarian-nucleus list from cartography, then formal RAN inquiry. Deliverable at screen stage is a list of required inquiries, not a conclusion |
| R-06 | Organised community opposition to rail megaprojects in Oaxaca (UCIZONI and others have opposed publicly) | medium-high | major | Documented consultation record; cannot be assessed from desk sources |
| R-07 | Land tenure records are not web-accessible (RAN, public registry require formal or in-person query) | high | moderate | Formal request. Constrains what any desk screen can conclude |

## C. Institutional and delivery

| ID | Risk | Likelihood | Impact | What would retire it |
|---|---|---|---|---|
| R-08b | **Assignee financial capacity — EVIDENCED.** FIT has never covered its operating costs: an operating loss in all six published years, 2024 cost recovery **16.2%**, costs **6.2× revenue**, best year 2019 at 36.2% (ARTF Anuario 2024, Tablas 7-3/7-5) | **certain — observed** | **fatal** to the commercial case | Nothing retires it short of a different operator or a permanent subsidy. See `working/operator-economics.md` |
| R-08 | Assignee delivery capability. ASF findings on the 2019 Línea Z rehabilitation include specification substitution (115 lb/yd rail placed where 136 lb/yd was specified) — press-reported, ASF primary not retrieved | medium | major | ASF audit reports on Línea Z, primary |
| R-09 | Safety record in the assignee's operating zone: Asunción Ixtaltepec derailment of 28 Dec 2025 (14 dead, 98 injured), a further freight derailment in the same zone in July 2026, and the FGR determination | unassessed — press only | major | FGR determination; ARTF incident record |
| R-10 | Cost escalation against budget on comparable Mexican rail rehabilitation. Press reports ~18,000 MXN million on Línea Z and a doubling of Transístmico cost | medium-high | major | SICT/ARTF tender awards; FIT contract values; ASF audits |
| R-11 | 2003 "precarious condition" is the most recent condition statement on record, now 20+ years old, and degradation of unmaintained track is **nonlinear** | high | **fatal** | Field reconnaissance. This is the load-bearing unknown and the basis of SR-3 |

## D. Method and evidence

| ID | Risk | Likelihood | Impact | What would retire it |
|---|---|---|---|---|
| R-12 | **Aforo gives vehicles, not tonnage or commodity.** Counting stations classify by axle configuration only; there is no commodity field. Two separate assumption bridges (payload-by-class, commodity mix) sit between counts and any tonnage figure | certain — structural | **fatal** if unlabelled | Both bridges stated as assumptions with sensitivity; commodity mix from SIAP / INEGI, never from truck counts |
| R-13 | **Aforo is link volume, not origin-destination.** A truck on 135D may be bound for the Isthmus, Chiapas or Guatemala | certain — structural | **fatal** if unlabelled | Addressed by SR-2 gradient; still needs the bottom-up cross-check |
| R-14 | **Corridor misidentification.** MEX-135D and the railway share endpoints only: 135D runs the Mixteca, the rail runs the Cañada. Using 135D drop-off traffic as rail-addressable overstates demand by ~2.5x | **realised and corrected** — see `working/sr2-evaluation.md` | major | Corrected: bound taken at endpoint flow, not differential |
| R-15 | Rail margin data partly confidential; ARTF *Anuario* unreachable. Substituting US Class I margins would import a different cost structure silently | high | major | ARTF Anuario, or FIT/CIIT tariff filing. Currently swept, not assumed |
| R-16 | Primary legal record unverifiable: DOF egress-blocked, Wayback capture paths egress-blocked. Corridor's concession and assignment history rests on the brief's own account | **realised** | major | DOF access, or INAI transparency request |
| R-17 | Extraction corruption in tabular PDFs. Reading-order text interleaves the DGST columns | **realised and mitigated** | major | Bounding-box reconstruction + three arithmetic identities per record; 99.8% validation pass, failures excluded not patched |
| R-18 | Currency, inflation and base-year mixing across decades of Mexican cost figures | medium | moderate | Single base year via INEGI INPC; MXN/USD rate and its date recorded per conversion |
| R-19 | Confirmation pressure toward issuing *a* verdict because a verdict is the expected deliverable | medium | **fatal** | Stop rules evaluated in order and in writing before any verdict is drafted. Currently: no verdict issued |

## Review

Reviewed at every phase boundary. New risks appended, never renumbered. A risk
is closed only with a note stating what evidence closed it.
