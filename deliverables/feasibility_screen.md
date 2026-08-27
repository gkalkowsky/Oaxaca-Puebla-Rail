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

### What would overturn it

Only a demand argument this screen deliberately does not make: that rail would
generate **new** freight not currently on the road. That is demand forecasting,
which the brief forbids, and it is an assumption, not evidence.

### Why it is safe to issue before the commodity segregation

The segregation (SIAP / INEGI, not yet done) can only **reduce** the divertible
share below 100%. The result already fails against Mexican precedent **at** 100%,
and clears track-only renewal only at capture rates the corridor evidence
contradicts. The missing work cannot reverse the direction.

### Not concluded

Step 6's public-benefit case is **untested**. A negative freight revenue case is
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
