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
| R-01 | ROW passes through **core zones** of the Tehuacán-Cuicatlán Biosphere Reserve / UNESCO property 1534, not merely buffer. Core-zone transit would escalate MIA to *modalidad regional*, constrain grading, drainage and alignment modification, and may foreclose segments outright | unassessed — `whc.unesco.org` returned 403 | **fatal** | UNESCO nomination boundary description for property 1534 + CONANP *programa de manejo* zoning, overlaid on the alignment |
| R-02 | Rainy-season scour and slope instability where the alignment follows the Río Salado / Cañada. The 2003 record already describes service suspension in the rainy season | medium — documented in the brief's history, unverified against DOF | major | Geotechnical reconnaissance; historical washout records from FIT/ARTF |
| R-03 | Structures (bridges, drainage) are the dominant capital uncertainty and **no public inventory is expected to exist** | high | major | Field structure survey. Carried in the model as its own line with its own range, never as a contingency percentage |

## B. Right-of-way, land and consent

| ID | Risk | Likelihood | Impact | What would retire it |
|---|---|---|---|---|
| R-04 | ROW encroachment and squatting after 20+ years dormant | medium-high | major | Satellite/street imagery for ROW clearance (indicative only); RAN and registry inquiry |
| R-05 | Alignment crosses **bienes comunales / ejido** land where consent runs through **Sistemas Normativos Indígenas** community assembly. This is a real gate, not a formality, and cannot be discharged by compensation alone | high | **fatal** | Municipality and agrarian-nucleus list from cartography, then formal RAN inquiry. Deliverable at screen stage is a list of required inquiries, not a conclusion |
| R-06 | Organised community opposition to rail megaprojects in Oaxaca (UCIZONI and others have opposed publicly) | medium-high | major | Documented consultation record; cannot be assessed from desk sources |
| R-07 | Land tenure records are not web-accessible (RAN, public registry require formal or in-person query) | high | moderate | Formal request. Constrains what any desk screen can conclude |

## C. Institutional and delivery

| ID | Risk | Likelihood | Impact | What would retire it |
|---|---|---|---|---|
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
