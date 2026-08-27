# Step 3b revisited — commodity segregation via haul distance

SIAP was unreachable (`siap.gob.mx` and `nube.siap.gob.mx` both fail to
connect; `www.gob.mx/siap` is bot-challenged), so the bottom-up agricultural
route to commodity segregation is closed. **A better route was available in
data already retrieved.**

Rather than estimate what *could* divert from road — which needs production
statistics and an assumed diversion elasticity — ARTF reports what *actually*
moves by rail in Mexico, **and at what distance**. Haul distance is the
variable that decides whether rail can compete at all.

## ARTF Anuario 2024, Tabla 2-2 — mean haul distance by product group

| Product group | Mt | M ton-km | Mean haul (km) | Corridor as % of it |
|---|---:|---:|---:|---:|
| Inorgánicos | 5.26 | 2,155 | 409.4 | 53% |
| Petróleo y derivados | 17.14 | 8,962 | 523.0 | 41% |
| Industriales | 63.74 | 40,928 | 642.1 | 34% |
| Forestales | 1.04 | 727 | 697.2 | 31% |
| Minerales | 7.10 | 5,262 | 741.6 | 29% |
| Agrícolas | 38.08 | 31,556 | 828.6 | 26% |
| Derivados de animales | 0.32 | 386 | 1,201.9 | 18% |
| **System weighted mean** | **132.68** | **89,976** | **678.1** | **32%** |

## The finding

> **The Vía Corta Oaxaca is 216.5 km. Mexican rail freight, in practice, moves
> at a mean haul of 678 km. No product group in the national statistics
> averages anywhere near 216.5 km — the corridor is 53% of even the
> shortest-hauling group (Inorgánicos, 409 km) and 32% of the system mean.**

This matters because rail's cost advantage over road is distance-dependent.
Rail carries high fixed terminal costs — loading, unloading, and drayage at both
ends — offset by low line-haul cost per ton-km. The advantage only materialises
once the haul is long enough to amortise those terminal costs. Below that
threshold, door-to-door trucking wins on both cost and transit time.

The ARTF distance distribution is **direct evidence that Mexican rail does not
compete at this corridor's length**, and it is evidence rather than assumption.

## Effect on the diversion assumption

The supportable-capital analysis swept diversion at 100 / 50 / 30 / 15%. Those
were labelled assumptions. This evidence says the realistic figure sits at or
below the **bottom** of that range:

- The screen's conclusion required ~50% capture even to fund *track-only*
  renewal.
- A 216.5 km haul is roughly half the distance at which Mexico's shortest-haul
  commodity group operates.
- Independently, the road that parallels the alignment carries **10–34**
  articulated veh/day, against 500 on the Mixteca route the railway does not
  serve.

Three independent lines — commodity haul economics, revealed road traffic in the
Cañada, and corridor geometry — converge on the same conclusion.

## The caveat that cuts the other way, and why it does not rescue the case

**If the corridor operated as a feeder** — Oaxaca traffic interlining onto the
national network toward Veracruz, the Isthmus or the north — the *effective*
haul for the shipper would be much longer than 216.5 km, and rail economics
would improve accordingly. This is the strongest argument available for the
project and it should not be dismissed.

It does not rescue the screen, for two reasons:

1. **The revenue attributable to this segment is what must service this
   segment's capital.** A shipper moving Oaxaca→Monterrey pays for ~2,000 km,
   but only the 216.5 km of Vía Corta Oaxaca earns against its own
   rehabilitation. The breakeven model already computes on that basis
   (216.5 km × margin), so a longer end-to-end haul does not change the
   segment's arithmetic.
2. **A feeder role implies tonnage this corridor's revealed traffic does not
   show.** It would have to come from traffic not currently visible in the road
   counts — which is demand forecasting, explicitly outside this brief.

Recorded as the principal residual uncertainty on the demand side, and as the
thing a follow-on study should test first if anyone wants to challenge the
verdict.

## What remains unobtained

SIAP crop-level production for Oaxaca, and INEGI Censos Económicos
establishment data, would allow a genuine bottom-up tonnage cross-check with no
through-traffic component — the brief's second method. `inegi.org.mx` is
reachable and this remains doable; SIAP is not currently reachable.

That cross-check can only **reduce** the divertible share below the
all-commodity bound already used. It cannot reverse the direction.
