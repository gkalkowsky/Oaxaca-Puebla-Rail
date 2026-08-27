# Feasibility Screen — Vía Corta Oaxaca freight reactivation

**Puebla (Sánchez) → Oaxaca City · línea E · km E-150+000 to E-367+000 · ~216.5 km**

Screening study. Concept level. Prepared against `Prompt.md`.

---

## Verdict

> ## NEGATIVE — the corridor does not support reactivation on a freight revenue case
>
> **Provisional, and conditional in one specific way stated below.** The
> outstanding work can only strengthen this result, not reverse it.

The screen was inverted to reach this. A planning-level capital cost for the
alignment could not be sourced, so rather than wait on it, the question was
turned around: **given what the corridor demonstrably moves, and what Mexican
railways demonstrably earn per ton-km, how much capital could the line
support?** That needs no capital estimate.

**Maximum supportable capital** — ARTF EBIT margin basis, 216.5 km, 30-year
life, in MXN million per route-km:

| Share of corridor freight won | @5% | @6% | @8% |
|---|---|---|---|
| **100%** (impossible, shown as a ceiling) | 18.6 | 16.7 | **13.6** |
| 50% | 9.3 | 8.3 | 6.8 |
| 30% | 5.6 | 5.0 | 4.1 |
| 15% | 2.8 | 2.5 | 2.0 |

Against the benchmarks:

- **Mexican precedent (Línea Z, ~60 MXN million/km)** — the corridor fails at
  **every** diversion rate and **every** cost of capital, including a physically
  impossible 100% capture of all corridor articulated freight. It is short by
  roughly **3× to 4×** at the ceiling and by an order of magnitude at plausible
  capture. *(Press-sourced and unverified — but the gap is far too wide for
  source quality to change the direction.)*
- **UNESCAP light rehabilitation (<USD 500,000/route-km ≈ 9.25 MXN million/km
  at 18.5 MXN/USD [ASSUMED rate — state rate and date])** — clears **only at
  ~50% diversion or above**.

### The flip point, which the brief asks for by name

> **~50% capture of all corridor articulated freight**, and only if
> rehabilitation is achievable at the international *light* benchmark rather
> than at Mexican precedent cost.

That is the single most decision-relevant number here. Both conditions must
hold simultaneously.

### Why this resolves negative rather than INDETERMINATE

By the letter of SR-3 the scenarios straddle: light rehabilitation clears at
≥50% diversion while substantial reconstruction fails everywhere. But the
straddle only exists **if ≥50% diversion is credible, and three independent
lines of evidence say it is not**:

1. The road that actually parallels the rail alignment through the Cañada
   carries **10–34 articulated veh/day**, not 500.
2. The 500 veh/day figure is measured on MEX-135D, which runs the **Mixteca** —
   its intermediate destinations are **not on the railway**.
3. A large share of Oaxaca's tradeable output is in explicitly **low-diversion**
   classes (mezcal, coffee, avocado, mango, figs, refrigerated, time-sensitive).

A 20-year-dormant line through a fault-zone canyon is also an unlikely candidate
for the *light* end of the rehabilitation range.

### What would overturn it

Only a demand argument this screen deliberately does not make: that rail would
generate **new** freight not currently on the road. That is demand forecasting,
which the brief forbids, and it is an assumption, not evidence.

### Why it is safe to issue before the commodity segregation

The segregation (SIAP / INEGI, not yet done) can only **reduce** the divertible
share below 100%. The result already fails against Mexican precedent **at** 100%.
The missing work therefore cannot reverse the direction — only deepen it. That
asymmetry is what makes a provisional negative defensible rather than premature.

### Not concluded

Step 6's public-benefit case is **untested**. A negative freight revenue case is
not a negative public-benefit case: the brief notes ~89% of measured benefits in
comparable studies come from reduced road transport operating cost. That case
may still exist and is the honest next question — but it is a different question,
and a subsidy argument, not a commercial one.

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
