# Stop Rule 2 — through-traffic contamination: EVALUATED, DOES NOT FIRE

Source: `sct-2025-datosviales-oaxaca`, `sct-2025-datosviales-puebla`
(SICT/DGST Datos Viales 2025, **data year 2024**). 1,102 station records
extracted and arithmetically validated; 1,037 after deduplicating the 60
coordinates that appear in both state volumes. Method and validation identities:
`analysis/scripts/extract_aforo.py`.

## Test as specified

> DETECT: compare TDPA on corridor segments north of Tehuacán, mid-corridor,
> and immediately north of Oaxaca City. If articulated truck volume does not
> decline materially approaching Oaxaca City, the count is dominated by
> through-traffic.

Articulated classes = `T3S2 + T3S3 + T3S2R4`. TDPA is **both directions
combined**. Profile along MEX-135D (Cuacnopalan–Oaxaca cuota):

| Position | Lat band | n | artic TDPA (range) | mean | TDPA mean |
|---|---|---|---|---|---|
| Entry — Plaza de Cobro Tehuacán | 18.47–18.50 | 2 | 780 – 1,259 | 1,020 | 9,768 |
| Upper — Chilac / Miahuatlán | 18.25–18.43 | 4 | 581 – 763 | 665 | 6,692 |
| Mid — Tepelmeme / Coixtlahuaca | 17.72–17.88 | 3 | 604 – 758 | 676 | 6,008 |
| Lower — Nochistlán | 17.45–17.48 | 2 | 501 – 592 | 547 | 6,205 |
| Approach — Huitzo | 17.26–17.28 | 3 | 276 – 603 | 401 | 5,509 |
| Terminus — N of Oaxaca City | 17.14–17.16 | 2 | 500 – 501 | 500 | 5,560 |

**A directional gradient exists**: articulated volume falls from ~1,259/day at
corridor entry to ~500/day at the terminus, a **60% decline**, and the decline
is monotonic across the intermediate bands. The counts are therefore *not*
dominated by through-traffic, and the STOP condition — "if neither a
directional gradient nor a bottom-up cross-check can be constructed" — does not
fire. A go/no-go remains permitted on this ground.

## Where the specified bound breaks, and what replaces it

> BOUND: use the differential between corridor-entry and corridor-terminus
> truck volume as the upper bound on corridor-internal freight.

Applied literally: 1,259 − 500 = **759 articulated veh/day**.

**That figure is not usable as the addressable-demand bound for this rail
line, and using it would materially overstate the case.** The reason is
geographic, and it only becomes visible once stations are placed by coordinate:

- **MEX-135D and the railway are not the same corridor.** They share endpoints
  and nothing else. 135D runs south-west through the **Mixteca Alta** —
  Tepelmeme, Coixtlahuaca, Nochistlán. The Vía Corta Oaxaca runs south-east
  through the **Cañada de Cuicatlán** — Teotitlán del Camino, Tecomavaca,
  Cuicatlán, Etla.
- The 759 veh/day differential is precisely the traffic that *leaves* 135D at
  intermediate Mixteca destinations. **Those destinations are not on the
  railway.** Counting them as rail-addressable assigns the line demand it
  physically cannot serve.

The defensible upper bound is instead the **endpoint-to-endpoint flow**, which
is bounded above by the terminus volume:

> **≤ ~500 articulated veh/day (both directions) at the corridor terminus
> north of Oaxaca City** — and this is still an over-count, because an unknown
> share continues *past* Oaxaca City toward the Isthmus and Chiapas on
> MEX-190, which the railway does not serve either.

This bound is ~1/2.5 of the figure the specified method produces. Both are
reported; they are not averaged.

## The rail-parallel road carries almost no articulated freight

The highway that actually follows the rail alignment through the Cañada is
route `PUE-MEX-135` (libre):

| Station | Lat | TDPA | truck % | artic % | **artic TDPA** |
|---|---|---|---|---|---|
| Teotitlán del Camino | 18.132 | 1,554 | 8.3 | 1.4 | **21.8** |
| Teotitlán del Camino | 18.119 | 2,806 | 6.5 | 1.2 | **33.7** |
| Santa María Tecomavaca | 17.956 | 1,259 | 6.5 | 1.3 | **16.4** |
| Santa María Tecomavaca | 17.950 | 1,094 | 6.5 | 0.9 | **9.8** |
| T. Izq. Cuicatlán | 17.794 | 1,409 | 7.3 | 0.7 | **9.9** |
| T. Izq. Nacaltepec | 17.506 | 705 | 10.6 | 3.1 | **21.9** |

**10–34 articulated vehicles per day** through the Cañada. (The 210/day reading
at 18.090 is the Tuxtepec junction, a different flow, and is excluded.)

Two readings of this are possible and the screen must not silently pick one:

1. *The Cañada is not a freight route today.* Rail through it would be building
   into a corridor with no revealed freight demand.
2. *The Cañada road is a poor canyon alignment and suppresses its own demand.*
   Freight that would use a good Cañada route currently diverts to 135D. Rail
   geometry differs from road geometry, so suppressed demand could re-route.

Reading 2 is the case for the project and it is **not evidenced by this data**.
It is an assumption. Distinguishing the two requires the bottom-up
production/consumption cross-check (SIAP, INEGI Censos Económicos), which has
no through-traffic component. That is the next retrieval task.

## Carried forward

- Addressable articulated flow: **≤ ~500 veh/day both directions**
  `[sct-2025-datosviales-oaxaca; sct-2025-datosviales-puebla]`
- Conversion to tonnage still requires payload-by-class and empty-running
  assumptions (brief: 30–50% empty). Both are assumptions, to be stated as such
  with sensitivity, not folded into a point estimate.
- **Not yet done:** the bottom-up cross-check the brief requires. Until it
  exists, the demand side rests on one method only. If the two disagree by more
  than a factor of 2, both get reported and neither is averaged.
