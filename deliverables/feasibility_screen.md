# Feasibility Screen — Vía Corta Oaxaca freight reactivation

**Puebla (Sánchez) → Oaxaca City · línea E · km E-150+000 to E-367+000 · ~216.5 km**

Screening study. Concept level. Prepared against `Prompt.md`.

---

## Verdict

> ## NEGATIVE — the corridor does not support reactivation on a freight revenue case
>
> **Provisional, and conditional in one specific way stated below.** The
> outstanding work can only strengthen this result, not reverse it.

Capital cost for this alignment could not be sourced in Mexico, so the screen
was inverted: **given what the corridor demonstrably moves, and what Mexican
railways demonstrably earn per ton-km, how much capital could the line
support?** That needs no capital estimate.

Both sides now rest on primary sources:

- **Traffic** — 500 articulated veh/day at the corridor terminus, by class
  (T3S2 278, T3S3 86, T3S2R4 136) `[sct-2025-datosviales-*, data year 2024]`
- **Payload bridge** — IMT *carga promedio* by configuration: 13.2 / 20.9 /
  30.1 t, weighted mean **19.1 t/vehicle** `[imt-pt179 Tabla 4.7 — PRIMARY but
  2001, STALE]`. This replaced an assumption, and *raised* the tonnage.
- **Margin** — Ferrosur EBIT **0.402 MXN/net ton-km**, constant 2024 MXN
  `[artf-2024-anuario-ferroviario]`

→ **Corridor tonnage 3.49 Mt/year.**

**Maximum supportable capital**, MXN million per route-km, 216.5 km, 30-year life:

| Share of corridor freight won | @5% | @6% | @8% |
|---|---|---|---|
| **100%** (impossible; a ceiling, not a case) | 21.6 | 19.3 | **15.8** |
| 50% | 10.8 | 9.7 | 7.9 |
| 30% | 6.5 | 5.8 | 4.7 |
| 15% | 3.2 | 2.9 | 2.4 |

**Against the benchmarks:**

| Benchmark | MXN m/km | Verdict |
|---|---|---|
| Línea Z Mexican precedent `[PRESS — UNVERIFIED]` | ~60 | **Fails at every capture rate and every margin basis**, including 100% capture on the gross-revenue basis (max 49.9) |
| World Bank **general** renewal — *track only* | 12.2–14.3 | Clears **only at ~100% capture** |
| World Bank **partial** renewal — *track only* | 6.3–9.3 | Clears **only at ~50% capture** |

`[wb-2020-serbia-railways-lcc Tabla 11]`. Currency is **not stated in the
source**; both plausible currencies are carried and the direction is unchanged.

### Step 2 output, stated as the brief asks — tonnes/year and truckloads/day

The workbook is now populated from sourced values and computes end-to-end.
Capital scenarios are the World Bank track-renewal costs; **structures are set
to zero deliberately**, so every figure below is a *lower bound on cost* and an
*upper bound on viability*.

| Capital scenario (track only) | Capital MXN m | Breakeven t/yr | Loaded truckloads/day **each way** | % of ALL corridor articulated freight |
|---|---:|---:|---:|---:|
| Light @5% | 1,494 | 1,116,554 | **80** | **32%** |
| Light @8% | 1,494 | 1,524,650 | 109 | 44% |
| Heavy @5% | 2,013 | 1,504,921 | 108 | 43% |
| Heavy @8% | 2,013 | 2,054,963 | 147 | 59% |
| Substantial @5% | 3,096 | 2,314,019 | 166 | 66% |
| Substantial @8% | 3,096 | 3,159,782 | **227** | **91%** |

Observed corridor traffic is ~250 articulated vehicles/day each way, carrying
3.49 Mt/year in total.

> **Even with bridges, drainage, slope stabilisation, signalling and
> right-of-way all costed at zero, the line must capture between 32% and 91% of
> every articulated tonne moving in the corridor simply to break even.**

Since divertible tonnage cannot exceed total tonnage, those percentages are a
**lower bound** on the required capture rate. The commodity segregation, when
done, can only push them up.

### The decisive point about those World Bank figures

They are **track only** — rail, sleepers, ballast, subsoil. They exclude
**bridges, drainage and slope stabilisation** (the dominant uncertainty in a
canyon at the convergence of two fault systems), signalling, and right-of-way
clearance after 20+ years dormant. So:

> Even ignoring structures, signalling and right-of-way **entirely**, the
> corridor must capture roughly **half of all its articulated freight** to fund
> **track renewal alone**.

Every excluded item pushes the same way.

### The flip point, which the brief asks for by name

> **~50% capture of all corridor articulated freight**, *and* rehabilitation
> achievable at the World Bank *partial*-renewal level with structures,
> signalling and ROW costing effectively nothing.

Both conditions must hold simultaneously.

### Why this resolves negative rather than INDETERMINATE

Formally the capital scenarios straddle. The straddle only exists if ≥50%
diversion is credible, and it is not:

1. The road that actually parallels the alignment through the Cañada carries
   **10–34 articulated veh/day**, not 500.
2. The 500 veh/day is measured on MEX-135D, which runs the **Mixteca** — its
   intermediate destinations are **not on the railway**.
3. Much of Oaxaca's tradeable output is in explicitly **low-diversion** classes
   (mezcal, coffee, avocado, mango, figs, refrigerated, time-sensitive).
4. **The corridor is far too short for Mexican rail freight economics.** ARTF
   Tabla 2-2 gives a system mean haul of **678 km**; no product group averages
   near 216.5 km, which is **53%** of even the shortest-hauling group
   (Inorgánicos, 409 km) and **32%** of the system mean. Rail's advantage over
   road is distance-dependent — terminal costs amortised over line haul — so
   this corridor sits below the range where Mexican rail demonstrably competes.
   This converts the diversion rate from assumption to evidence.
   `[artf-2024-anuario-ferroviario Tabla 2-2; working/step3b-commodity-and-haul.md]`

### Corroboration from the operator's own accounts

**FIT — the assignee of Vía Corta Oaxaca (ARTF Tabla 1-1) — has never covered
its operating costs.** ARTF Tablas 7-3 and 7-5, constant 2024 MXN: an operating
loss in every one of the six published years; 2024 cost recovery **16.2%**,
costs **6.2× revenue**; best year on record 2019 at **36.2%**, before the
Línea Z works that suppressed later revenue.

The analysis above used **Ferrosur's** margin — a profitable private operator.
On the actual operator's realised economics the margin available to service
rehabilitation capital is **negative**, and there is no positive capital ceiling
to compute at all. See `working/operator-economics.md`.

A long-run note, from SCT's own account: the Ferrocarril Mexicano del Sur was
recording losses of over six million pesos a year by **1896**.

### A correction that went against this conclusion

The IMT payload bridge **raised** supportable capital from 13.6–18.6 to
15.8–21.6 MXN m/km at the ceiling, because IMT's measured load factors imply
more tonnage than the assumption they replaced. Reported because it happened,
not because it helps.

## Environmental permitting — a live risk, but NOT a second basis for the verdict

> **Corrected 2026-08-28.** An earlier version of this screen presented
> permitting as a second, independent constraint that would bind even if the
> economics were favourable. **A GIS overlay against CONANP's own boundary
> shapefile does not support that.** The Cañada valley floor, where both
> MEX-135 and the railway run, is largely **excluded** from the reserve: all
> nine corridor waypoints test **outside** the ANP polygon, and south of
> ~17.53°N there is no reserve at any longitude. The constraint is downgraded
> to a live but unresolved risk with thin margin. The freight revenue verdict
> never depended on it and is unaffected.

**The reserve has no core or buffer zones.** The brief asks whether the ROW
crosses core zones, buffer, or lies outside the property. That framing does not
apply: the *declaratoria* established only a **general polygon** and set no zona
núcleo or zona de amortiguamiento `[conanp-2013-pm-tehuacan-cuicatlan p.140]`.
The operative instrument is **subzonal**.

| Subzona | Hectares | % | Infrastructure rule |
|---|---:|---:|---|
| Preservación | 141,782 | 29.06% | Maintenance of **existing roads** only; opening trails/tracks/roads **prohibited** |
| Uso Tradicional | 133,739 | 27.41% | Only infrastructure **in support of** research / education / low-impact tourism |
| Aprov. Sust. Recursos Naturales | 33,047 | 6.77% | Same |
| Aprov. Sust. Ecosistemas | 178,169 | 36.51% | Same |
| Uso Público | 1,001 | 0.21% | Tourism-oriented |
| **Aprovechamiento Especial** | **239** | **0.049%** | **Only subzona permitting general infrastructure construction** |

> The single subzone in which general "construcción y mantenimiento de
> infraestructura" is permitted covers **239.2 ha — 0.049% of the reserve** —
> across 14 polygons that are, without exception, **quarries, salt works and the
> Tehuacán landfill**. None is a transport corridor. A 216.5 km alignment at an
> assumed 20 m right-of-way would cover ~433 ha: **1.8× that entire subzone.**

Those rules are factually correct about the reserve's interior. **What the
overlay changed is whether they bind on this alignment.**

### GIS overlay result

Source: CONANP's boundary shapefile `232-ANP_ITRF08_19162026.shp`
(`sig.conanp.gob.mx/Shape` — the site root 503s, that path serves).

| Waypoint | Gap from reserve edge to the valley-floor station |
|---|---|
| Tehuacán (corridor entry) | **0.6 km** |
| Santa María Tecomavaca | **0.8 – 1.2 km** |
| San Juan Bautista Cuicatlán | 3.3 km |
| Teotitlán del Camino | 4.6 – 6.5 km |
| Nacaltepec → Oaxaca City | **no reserve at these latitudes** |

Also independently confirmed: CONANP's national zonas-núcleo layer contains
**zero polygons** for this reserve — corroborating the management programme's
statement that none was ever established, from a different source type.

**So the alignment may run substantially, perhaps wholly, outside the ANP.** A
straight-line traverse between waypoints reports "32% inside"; that is an
artefact of chording across slopes a valley alignment would not enter, and is
not used.

**What keeps it a live risk rather than a closed question:** the excluded
corridor is under 1 km wide at Tehuacán and Tecomavaca, so cuttings, borrow
pits, spoil and structures could enter reserve land even where the centreline
does not; the reserve's zone of influence is larger than the polygon; and **the
rail centreline was never obtained** — road stations are the proxy throughout.

CONANP separately identifies **federal 135 Tehuacán-Cuicatlán** among roads
causing "inestabilidad de taludes, erosión, incendios" in the Cañada, and names
right-of-way clearing as a fire-pressure source (pp. 81, 83) — which still
corroborates the geotechnical risk (R-02) regardless of the boundary question.

Full treatment: `working/environmental-permitting.md`,
`working/anp-overlay.txt`.

### What would overturn it

Only a demand argument this screen deliberately does not make: that rail would
generate **new** freight not currently on the road, or that the line would
operate as a **feeder** interlining onto the national network at much longer
effective hauls. The feeder case is the strongest argument available and is
recorded as the principal residual uncertainty — but only the 216.5 km segment
earns against its own rehabilitation, which is how the model computes, and a
feeder role implies tonnage the revealed traffic does not show. Both are demand
forecasting, which the brief forbids.

### Why it is safe to issue before the commodity segregation

The segregation (SIAP / INEGI, not yet done) can only **reduce** the divertible
share below 100%. The result already fails against Mexican precedent **at** 100%,
and clears track-only renewal only at capture rates the corridor evidence
contradicts. The missing work cannot reverse the direction.

## Step 6 — public-benefit case, inverted rather than left blank

Quantifying benefits directly needs current Mexican road operating costs. The
only Mexican source located (IMT PT-179) is from **2001** and too stale to carry
a benefit figure. So the same inversion was applied: **what external benefit
would be required to close the gap?** That needs no benefit data and is
falsifiable by any future study.

Basis: World Bank **track-renewal-only** capital, annualised at 6% over 30
years; commercial surplus at the ARTF margin of 0.402 MXN/ton-km.

| Capture | Tonnage Mt/yr | Commercial surplus MXN m/yr | Annualised capital MXN m/yr | Gap | **Required external benefit** |
|---:|---:|---:|---:|---:|---:|
| 100% | 3.49 | 304 | 192–225 | none | commercial case alone suffices |
| 50% | 1.75 | 152 | 192–225 | 40–73 | **0.11–0.19 MXN/ton-km** |
| 30% | 1.05 | 91 | 192–225 | 101–134 | **0.44–0.59 MXN/ton-km** |
| 15% | 0.52 | 46 | 192–225 | 146–179 | **1.29–1.58 MXN/ton-km** |

**Reading it honestly, in both directions:**

- At **50% capture** the required external benefit is **0.11–0.19 MXN/ton-km** —
  modest, and plausibly met by avoided pavement damage, accident and CO₂
  externalities. **The public-benefit case is not absurd at high capture.**
- At **30%** it must roughly **match the entire commercial margin** (0.402).
- At **15%** it must be **three to four times** the commercial margin.

And this is for **track renewal alone** — before structures, signalling,
right-of-way, or FIT's own operating deficit, which on the evidence would need
permanent subsidy regardless.

So Step 6 turns on the same variable everything else does: **capture rate**.
The haul-distance evidence (216.5 km against a 678 km national mean) argues
capture sits at the bottom of that table, where the public-benefit case becomes
very demanding.

**Still not computed**, and required before any of this becomes a benefit
estimate: current Mexican road vehicle operating cost per veh-km; pavement
damage avoided per ESAL-km on MEX-135D/190; Mexican accident and CO₂
valuations; and the brief's own "~89% of benefits from road operating cost"
figure, which **could not be located in any retrieved source** and is recorded
as unverified rather than repeated.

### Not concluded

Step 6's public-benefit case is **bounded but not measured**. A negative freight revenue case is
not a negative public-benefit case. Note though — ITF/OECD observes that for
rail **freight** specifically, unlike roads or passenger rail, financial
viability is legitimately a decision criterion, because a commercial
relationship exists between infrastructure owner and haulier
`[itf-2020-road-rail-cba]`. The public-benefit case here would have to justify a
**permanent operating subsidy**, not merely a capital grant — which is what
FIT's accounts show is actually required.

---

## 1. Stop rules

| Rule | Status | Basis |
|---|---|---|
| **SR-7 Network access** | **EVALUATED — does not fire** | Aforo *and* rail tonnage both obtained from primary government sources. `working/source-access-log.md` |
| **SR-2 Through-traffic contamination** | **EVALUATED — does not fire** | Directional gradient exists and is measurable. `working/sr2-evaluation.md` |
| **SR-3 Track-condition straddle** | **EVALUATED via inversion — resolves negative** | Formal straddle exists but requires ≥50% diversion to be credible; three independent lines of evidence say it is not. Flip point reported above |

### SR-7 — network access

Does not fire, but only via a routing finding worth recording: `www.sct.gob.mx`,
`www.imt.mx` and `www.gob.mx/artf` all serve bot-challenge pages (HTTP 200,
1821 bytes). **A gob.mx HTTP 200 is not access.** The same institutions serve
their document trees from `micrs.sct.gob.mx` and the bare `imt.mx` domain,
which are not challenged.

Genuinely unavailable, reported rather than circumvented: **DOF**
(egress-policy denial) and **web.archive.org capture paths** (egress policy) —
so the brief's own designated fallback for link rot is closed. **ARTF's
*Anuario Estadístico Ferroviario*** is bot-challenged, and **UNESCO property
1534** returns 403.

### SR-2 — through-traffic contamination

Does not fire. Articulated volume on MEX-135D declines monotonically from
~1,259 veh/day at corridor entry (Plaza de Cobro Tehuacán) to ~500 veh/day at
the terminus north of Oaxaca City — a **60% decline**. The counts are not
through-traffic dominated.

**The brief's specified bound is reported but not used.** Entry minus terminus
= 759 veh/day. Placing stations by coordinate shows why that figure cannot
carry the demand case: **MEX-135D and the railway share endpoints and nothing
else.** 135D runs through the **Mixteca Alta** (Tepelmeme, Coixtlahuaca,
Nochistlán); the railway runs through the **Cañada de Cuicatlán** (Teotitlán
del Camino, Tecomavaca, Cuicatlán, Etla). The 759 veh/day differential *is* the
traffic leaving 135D at Mixteca destinations — which are not on the railway.
Counting it as rail-addressable assigns the line demand it cannot physically
serve.

Defensible bound instead:

> **≤ ~500 articulated veh/day (both directions)** at the corridor terminus,
> itself an over-count because an unknown share continues past Oaxaca City
> toward the Isthmus.

Both figures are reported. They are **not averaged**, per the brief.

---

## 2. The finding that most bears on the project

The highway that actually parallels the rail alignment through the Cañada
(`PUE-MEX-135`) carries **10–34 articulated vehicles per day**
`[sct-2025-datosviales-oaxaca]` — against 500–1,259/day on the Mixteca toll
route.

Two readings are possible and the screen must not silently pick one:

1. **The Cañada is not a freight route today.** Reactivation would build into a
   corridor with no revealed freight demand.
2. **The Cañada road is a poor canyon alignment that suppresses its own
   demand.** Freight that would use a good Cañada route diverts to 135D today;
   rail geometry differs from road geometry, so that demand could re-route.

Reading 2 is the case for the project. **It is an assumption and this data does
not evidence it.** Separating the two requires the bottom-up production and
consumption cross-check (SIAP, INEGI Censos Económicos), which has no
through-traffic component. That work is not yet done, so the demand side
currently rests on one method.

---

## 3. Method status

| Step | Status |
|---|---|
| 1 — Capital cost band | **Still unsourced**, and now bypassed. Screen inverted to solve for maximum supportable capital instead |
| 2 — Breakeven tonnage back-solve | **Complete.** Margin obtained from ARTF primary ($0.402/ton-km EBIT, Ferrosur, constant 2024 MXN). See `working/margin-derivation.md` |
| 3 — Count what moves | **Aforo complete** (1,102 stations validated). Commodity segregation not started — needs SIAP/INEGI |
| 4 — Compare and recommend | Not reached |
| 5 — Risk register | Drafted, `risk_register.md` |
| 6 — Benefit-cost framing | Not reached |

### The O&M circularity, resolved rather than hand-waved

Track maintenance scales with gross passing tonnage, so O&M depends on the
tonnage being solved for. Revenue and variable O&M are both linear in tonnage,
so the circularity closes in closed form:

```
T = (AnnualCapital + FixedOM) / ( L × ( margin − varOM × (1 + tare) ) )
```

The denominator is net contribution per ton-km **after track wear**. If it
reaches zero the line loses money on every incremental tonne and no tonnage
breaks even; the model reports that rather than returning a large finite
number. Verified by recalculation.

### Margin is swept, not assumed

ARTF's commodity-level contribution margin is commercially confidential and its
*Anuario* was unreachable. Rather than silently substitute US Class I figures,
breakeven is solved **across** a margin range. No proxy has been entered.

---

## 4. What would close this screen

In priority order:

1. ~~Contribution margin per ton-km~~ — **OBTAINED.** ARTF *Anuario* 2024 via
   the `/cms/uploads/attachment/file/` path, which is not bot-challenged.
   Ferrosur EBIT $0.402/ton-km, constant 2024 MXN.
2. **Mexican rehabilitation unit costs** — SICT/ARTF tender awards or FIT
   contract values per km. Press reports ~18,000 MXN million on Línea Z
   (~300 km, order ~60 MXN million/km, roughly an order of magnitude above the
   UNESCAP <USD 500,000/route-km guidance). **Press-sourced and unverified**;
   ASF primary is a JS application and DOF is egress-blocked.
3. **Bottom-up commodity tonnage** — SIAP and INEGI Censos Económicos, to
   cross-check the aforo-derived bound. If the two methods disagree by more
   than a factor of 2, both get reported and neither is averaged.
4. **Track condition** — cannot be resolved from a desk. This is the
   load-bearing unknown and the reason SR-3 exists. Satellite imagery can
   indicate whether rail is in place and the ROW is clear; it cannot show tie,
   ballast or structure condition.

---

## 5. What this screen does not establish

- **No capital cost figure.** No sourced unit cost for this alignment.
- **No verified capital cost.** The supportable-capital ceiling is established;
  the actual cost is not. The comparison rests on a press-sourced precedent.
- **No commodity mix.** Aforo classifies by axle configuration only — there is
  **no commodity field**. Commodity mix cannot be derived from truck counts.
- **No tonnage.** Converting vehicle counts to tonnage requires payload-by-class
  and empty-running assumptions (brief: 30–50% empty). Both are assumptions and
  neither has been entered.
- **No legal history verification.** The 2003 condition notice, 2012 concession
  exclusion and 2023 FIT assignment are unverified against the primary record;
  DOF and Wayback are both blocked. Not closed by substituting press reporting.
- **No environmental determination.** Whether the ROW crosses core zones, buffer
  zone, or falls outside the Tehuacán-Cuicatlán property is undetermined —
  UNESCO 1534 returned 403.
- **No land-tenure determination.** RAN and registry records are not
  web-accessible; the deliverable there is a list of required inquiries, not a
  conclusion.

Figures older than 5 years are flagged where used. Aforo data is **data year
2024**, published 2025.
