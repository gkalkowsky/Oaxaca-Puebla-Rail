#!/usr/bin/env python3
"""Maximum supportable capital — the screen inverted.

A planning-level capital cost for this alignment could not be sourced. But the
question can be turned around: given what the corridor demonstrably moves, and
what Mexican railways demonstrably earn per ton-km, HOW MUCH capital could the
line support? That ceiling is then compared against published unit costs.

This requires no capital estimate, so it is not blocked by the missing figure.

INPUTS, ALL PRIMARY-SOURCED
  Traffic  : <= 500 articulated veh/day both directions at the corridor terminus
             [sct-2025-datosviales-oaxaca, data year 2024; working/sr2-evaluation.md]
  Margin   : ARTF Anuario Estadistico Ferroviario 2024, constant 2024 MXN
             Ferrosur revenue/ton-km $0.93 (Tabla 7-8); operating profit ratio
             3,688,169 / 8,538,620 = 43.19% (Tablas 7-3, 7.7)
             => EBIT per ton-km = 0.93 * 0.4319 = $0.402
  Length   : 216.5 route-km [Prompt.md]

ASSUMPTIONS, LABELLED AS SUCH EVERY TIME THEY APPEAR
  payload per loaded articulated truck : 25-30 t   [ASSUMPTION]
  empty running                        : 30-50%    [Prompt.md range]
  diversion to rail                    : swept     [ASSUMPTION]
  margin basis                         : swept 0.402 (EBIT) .. 0.93 (gross revenue)

Ferrosur's margin comes from a dense, functioning network. A 216.5 km branch
carrying a fraction of that traffic would very likely earn less per ton-km, so
using it is generous to the project.
"""
from __future__ import annotations

ARTIC_VEH_DAY = 500.0      # both directions, corridor terminus
LENGTH_KM = 216.5
LIFE = 30
RATES = (0.05, 0.06, 0.08)
PAYLOAD = (25.0, 30.0)     # [ASSUMPTION] tonnes per loaded articulated truck
EMPTY = (0.50, 0.30)       # [Prompt.md] 30-50% empty running
MARGINS = {"EBIT basis (ARTF, conservative)": 0.402,
           "midpoint": 0.660,
           "gross revenue basis (generous)": 0.930}
DIVERSION = (1.00, 0.50, 0.30, 0.15)   # [ASSUMPTION] share of corridor freight won


def annuity_factor(r: float, n: int) -> float:
    return (1 - (1 + r) ** -n) / r


def corridor_tonnage() -> tuple[float, float]:
    """Annual tonnes moving in the corridor by articulated truck, low and high."""
    lo = ARTIC_VEH_DAY * (1 - EMPTY[0]) * PAYLOAD[0] * 365   # most conservative
    hi = ARTIC_VEH_DAY * (1 - EMPTY[1]) * PAYLOAD[1] * 365   # most generous
    return lo, hi


def main() -> None:
    lo, hi = corridor_tonnage()
    print("=" * 78)
    print("CORRIDOR TONNAGE implied by observed articulated traffic")
    print("=" * 78)
    print(f"  {ARTIC_VEH_DAY:.0f} artic veh/day both directions (SR-2 bound, aforo 2024)")
    print(f"  x (1 - empty running {EMPTY[0]:.0%}..{EMPTY[1]:.0%}) x payload "
          f"{PAYLOAD[0]:.0f}-{PAYLOAD[1]:.0f} t [ASSUMPTIONS] x 365")
    print(f"  => {lo/1e6:.2f} - {hi/1e6:.2f} million tonnes/year in the corridor\n")

    print("=" * 78)
    print("MAXIMUM SUPPORTABLE CAPITAL  (MXN million per route-km, 216.5 km, 30-yr life)")
    print("=" * 78)
    for mname, margin in MARGINS.items():
        print(f"\n--- margin basis: {mname}  =  {margin:.3f} MXN / net ton-km ---")
        print(f"    {'diversion':>10} {'tonnage Mt/yr':>16} {'surplus MXNm/yr':>17}"
              f"  {'  '.join(f'@{r:.0%} MXNm/km' for r in RATES)}")
        for div in DIVERSION:
            t_lo, t_hi = lo * div, hi * div
            s_lo = t_lo * LENGTH_KM * margin / 1e6
            s_hi = t_hi * LENGTH_KM * margin / 1e6
            cells = []
            for r in RATES:
                af = annuity_factor(r, LIFE)
                cells.append(f"{s_lo*af/LENGTH_KM:6.1f}-{s_hi*af/LENGTH_KM:<6.1f}")
            print(f"    {div:>9.0%} {t_lo/1e6:7.2f}-{t_hi/1e6:<6.2f} "
                  f"{s_lo:7.0f}-{s_hi:<7.0f}  {'  '.join(cells)}")

    print("\n" + "=" * 78)
    print("BENCHMARKS TO COMPARE AGAINST")
    print("=" * 78)
    print("  UNESCAP light rehabilitation  : < USD 500,000/route-km")
    print("                                  ~9.3 MXN million/km at 18.5 MXN/USD")
    print("                                  [rate is an ASSUMPTION - state rate and date]")
    print("  Linea Z (Mexican precedent)   : ~18,000 MXN million / ~300 km")
    print("                                  ~60 MXN million/km  [PRESS - UNVERIFIED]")


if __name__ == "__main__":
    main()
