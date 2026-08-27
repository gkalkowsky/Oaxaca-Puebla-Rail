#!/usr/bin/env python3
"""Step 6 inverted — what must the public-benefit case deliver?

The brief asks whether a public-benefit case is plausible when the revenue case
is negative. Quantifying benefits directly needs current Mexican road operating
costs; the only Mexican source located (IMT PT-179) is from 2001 and too stale
to carry a benefit figure. So the question is inverted, exactly as the capital
question was: what external benefit per tonne-km would be REQUIRED to close the
gap? That needs no benefit data, and it is falsifiable against any future study.

Sources
  capital  : World Bank track-renewal unit costs [wb-2020-serbia-railways-lcc]
             TRACK ONLY -- excludes structures, signalling, ROW
  margin   : Ferrosur EBIT 0.402 MXN/net ton-km [artf-2024-anuario-ferroviario]
  tonnage  : corridor 3.49 Mt/yr at 100% capture [aforo 2024 x IMT loads]
  length   : 216.5 km
"""
L, MARGIN, TONNAGE_100, LIFE, RATE = 216.5, 0.402, 3_490_000, 30, 0.06
CAPEX_PER_KM = (12.2, 14.3)          # MXN m/km, World Bank general renewal, TRACK ONLY
af = (1 - (1 + RATE) ** -LIFE) / RATE

print(f"Annuity factor @{RATE:.0%}, {LIFE} yr: {af:.3f}\n")
print(f"{'diversion':>10} {'tonnage Mt':>11} {'commercial surplus':>19} "
      f"{'annualised capital':>19} {'GAP MXNm/yr':>13} {'required external':>18}")
print(f"{'':>10} {'':>11} {'MXN m/yr':>19} {'MXN m/yr':>19} {'':>13} {'MXN / ton-km':>18}")
for div in (1.00, 0.50, 0.30, 0.15):
    t = TONNAGE_100 * div
    surplus = t * L * MARGIN / 1e6
    lo_cap, hi_cap = (c * L for c in CAPEX_PER_KM)
    ann_lo, ann_hi = lo_cap / af, hi_cap / af
    gap_lo, gap_hi = ann_lo - surplus, ann_hi - surplus
    req_lo, req_hi = gap_lo * 1e6 / (t * L), gap_hi * 1e6 / (t * L)
    print(f"{div:>9.0%} {t/1e6:>11.2f} {surplus:>19.0f} {ann_lo:>8.0f}-{ann_hi:<10.0f} "
          f"{gap_lo:>5.0f}-{gap_hi:<7.0f} {req_lo:>8.2f}-{req_hi:<9.2f}")

print(f"""
READ THIS AS: to justify TRACK RENEWAL ALONE, external benefits would have to be
worth the figures in the last column, per net tonne-kilometre carried, on top of
every peso of commercial margin the traffic already earns.

For scale, the commercial margin itself is {MARGIN} MXN/ton-km. So at realistic
capture the public-benefit case must deliver several times the entire commercial
value of the freight, just to fund track renewal -- before structures,
signalling, right-of-way, or the operator's own operating deficit.

NOT COMPUTED, and required before any of this becomes a benefit estimate:
  - current Mexican road vehicle operating cost per veh-km (IMT PT-179 is 2001)
  - pavement damage cost avoided per ESAL-km on MEX-135D / MEX-190
  - accident and CO2 valuations for Mexican federal highways
  - the brief's '~89% of benefits from road operating cost' claim, which could
    NOT be located in any retrieved source and is therefore unverified
""")
