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
# Payload bridge, now from a MEXICAN PRIMARY SOURCE rather than an assumption.
# IMT Publicacion Tecnica 179, Tabla 4.7 "Porcentajes Promedio de Llenado":
# average load actually carried (carga promedio), tonnes, by configuration.
# NOTE [STALE - 2001 data, 25 years old]. Load factors may have risen since.
# carga promedio is the average load across observed vehicles, so it ALREADY
# nets out empty and partial running -- applying a further empty-running
# discount on top would double-count.
IMT_LOAD = {"T3S2": 13.2, "T3S3": 20.9, "T3S2R4": 30.1}
# Class mix at the corridor terminus, from the aforo extraction (mean of the
# two MEX-135D stations north of Oaxaca City, data year 2024).
TERMINUS_MIX = {"T3S2": 278.0, "T3S3": 86.0, "T3S2R4": 136.0}   # veh/day
MARGINS = {"EBIT basis (ARTF, conservative)": 0.402,
           "midpoint": 0.660,
           "gross revenue basis (generous)": 0.930}
DIVERSION = (1.00, 0.50, 0.30, 0.15)   # [ASSUMPTION] share of corridor freight won


def annuity_factor(r: float, n: int) -> float:
    return (1 - (1 + r) ** -n) / r


def corridor_tonnage() -> tuple[float, float]:
    """Annual tonnes in the corridor, from observed class mix x IMT load factors."""
    per_day = sum(TERMINUS_MIX[k] * IMT_LOAD[k] for k in TERMINUS_MIX)
    t = per_day * 365
    return t, t   # single figure now: the bridge is sourced, not a range


def main() -> None:
    lo, hi = corridor_tonnage()
    print("=" * 78)
    print("CORRIDOR TONNAGE implied by observed articulated traffic")
    print("=" * 78)
    mix = "  ".join(f"{k}={v:.0f}@{IMT_LOAD[k]}t" for k, v in TERMINUS_MIX.items())
    print(f"  terminus class mix (veh/day, aforo 2024): {mix}")
    print(f"  x IMT PT-179 Tabla 4.7 carga promedio [PRIMARY, but 2001 - STALE] x 365")
    print(f"  weighted mean load = {sum(TERMINUS_MIX[k]*IMT_LOAD[k] for k in TERMINUS_MIX)/sum(TERMINUS_MIX.values()):.1f} t/veh")
    print(f"  => {hi/1e6:.2f} million tonnes/year in the corridor\n")

    print("=" * 78)
    print("MAXIMUM SUPPORTABLE CAPITAL  (MXN million per route-km, 216.5 km, 30-yr life)")
    print("=" * 78)
    for mname, margin in MARGINS.items():
        print(f"\n--- margin basis: {mname}  =  {margin:.3f} MXN / net ton-km ---")
        print(f"    {'diversion':>10} {'tonnage Mt/yr':>15} {'surplus MXNm/yr':>16}"
              f"  {''.join(f'@{r:.0%} MXNm/km' for r in RATES)}")
        for div in DIVERSION:
            t_lo, t_hi = lo * div, hi * div
            s_lo = t_lo * LENGTH_KM * margin / 1e6
            s_hi = t_hi * LENGTH_KM * margin / 1e6
            cells = [f"{s_hi*annuity_factor(r, LIFE)/LENGTH_KM:12.1f}" for r in RATES]
            print(f"    {div:>9.0%} {t_hi/1e6:15.2f} {s_hi:16.0f}  {''.join(cells)}")

    print("\n" + "=" * 78)
    print("BENCHMARKS TO COMPARE AGAINST")
    print("=" * 78)
    print("  UNESCAP light rehabilitation  : < USD 500,000/route-km")
    print("                                  ~9.3 MXN million/km at 18.5 MXN/USD")
    print("                                  [rate is an ASSUMPTION - state rate and date]")
    print("  Linea Z (Mexican precedent)   : ~60 MXN million/km  [PRESS - UNVERIFIED]")
    print("  World Bank general renewal    : ~12.2-14.3 MXN million/km  TRACK ONLY")
    print("  World Bank partial renewal    : ~6.3-9.3   MXN million/km  TRACK ONLY")
    print("    [wb-2020-serbia-railways-lcc Tabla 11; currency not stated in source;")
    print("     EXCLUDES bridges, drainage, slope stabilisation, signalling, ROW]")


if __name__ == "__main__":
    main()
