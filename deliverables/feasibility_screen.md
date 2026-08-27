# Feasibility Screen — Vía Corta Oaxaca freight reactivation

**Puebla (Sánchez) → Oaxaca City · línea E · km E-150+000 to E-367+000 · ~216.5 km**

Screening study. Concept level. Prepared against `Prompt.md`.

---

## Verdict

> ## NO VERDICT ISSUED — screen incomplete
>
> Demand-side work is complete enough to bound addressable freight. The
> **cost side is not sourced**, so no go / no-go / marginal judgement may be
> issued. This is a statement about the evidence, not about the project.

The brief is explicit that manufacturing a conclusion to satisfy the
deliverable spec is the worst possible outcome. Two of the three inputs that
would decide this screen — planning-level capital cost for this alignment, and
contribution margin per ton-km — have no primary source behind them yet. A
verdict now would be an assumption wearing a conclusion's clothes.

What is established, and what it would take to close the gap, is set out below.

---

## 1. Stop rules

| Rule | Status | Basis |
|---|---|---|
| **SR-7 Network access** | **EVALUATED — does not fire** | Aforo *and* rail tonnage both obtained from primary government sources. `working/source-access-log.md` |
| **SR-2 Through-traffic contamination** | **EVALUATED — does not fire** | Directional gradient exists and is measurable. `working/sr2-evaluation.md` |
| **SR-3 Track-condition straddle** | **NOT YET EVALUABLE** | Requires capital band (Step 1), which has no sourced Mexican unit cost. The model is built and will evaluate it the moment inputs exist |

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
| 1 — Capital cost band | **Blocked on sourcing.** Model built (light / heavy / substantial reconstruction, structures carried as a separate line with its own range). No sourced Mexican unit cost yet |
| 2 — Breakeven tonnage back-solve | **Model built and verified.** 30-yr life, 5/6/8% cost of capital, outputs t/yr and loaded truckloads/day each way. Awaiting inputs |
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

1. **Contribution margin per ton-km** — ARTF *Anuario Estadístico Ferroviario*,
   or an FIT/CIIT tariff filing. Without it Step 2 has no revenue side.
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
- **No revenue figure.** Margin per ton-km not obtained.
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
