#!/usr/bin/env python3
"""Build analysis/breakeven_model.xlsx.

The workbook is generated, not hand-edited, so the model's structure lives in
version control as reviewable code rather than as an opaque binary diff. Run
this to recreate it:

    python3 analysis/scripts/build_breakeven_model.py

Every input on the Assumptions sheet ships blank with a Source column beside
it. Blank means "not yet established" -- the formulas return empty rather than
a plausible-looking zero, so the workbook cannot show a breakeven figure that
no source supports. Fill an input only together with its citation.
"""

from __future__ import annotations

from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "analysis" / "breakeven_model.xlsx"

TITLE = Font(bold=True, size=14)
HEAD = Font(bold=True, color="FFFFFF")
SECTION = Font(bold=True)
NOTE = Font(italic=True, size=9, color="666666")
HEAD_FILL = PatternFill("solid", fgColor="1F3864")
SECTION_FILL = PatternFill("solid", fgColor="D9E2F3")
INPUT_FILL = PatternFill("solid", fgColor="FFF2CC")   # yellow = enter a value
DERIVED_FILL = PatternFill("solid", fgColor="E2EFDA")  # green  = calculated
THIN = Side(style="thin", color="BFBFBF")
BOX = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)

MONEY = '#,##0.0'
COUNT = '#,##0'
PCT = '0.0%'


def header_row(ws, row: int, labels: list[str]) -> None:
    for col, label in enumerate(labels, start=1):
        c = ws.cell(row=row, column=col, value=label)
        c.font, c.fill, c.border = HEAD, HEAD_FILL, BOX
        c.alignment = Alignment(vertical="center")


def section(ws, row: int, label: str, width: int = 5) -> None:
    ws.cell(row=row, column=1, value=label).font = SECTION
    for col in range(1, width + 1):
        ws.cell(row=row, column=col).fill = SECTION_FILL


def param(ws, row, name, unit, *, formula=None, fmt=None, source="", note=""):
    """One parameter line: name | value | unit | source | notes."""
    ws.cell(row=row, column=1, value=name)
    v = ws.cell(row=row, column=2, value=formula)
    v.fill = DERIVED_FILL if formula else INPUT_FILL
    v.border = BOX
    if fmt:
        v.number_format = fmt
    ws.cell(row=row, column=3, value=unit)
    ws.cell(row=row, column=4, value=source)
    ws.cell(row=row, column=5, value=note).font = NOTE


def widths(ws, spec: dict[int, int]) -> None:
    for col, w in spec.items():
        ws.column_dimensions[get_column_letter(col)].width = w


def blank(*refs: str) -> str:
    """Excel condition true when any referenced input is still empty."""
    return "OR(" + ",".join(f'{r}=""' for r in refs) + ")"


def build_readme(ws) -> None:
    ws.title = "README"
    ws["A1"] = "Oaxaca–Puebla Rail — Breakeven Model"
    ws["A1"].font = TITLE
    lines = [
        "",
        "Status: Phase 0 scaffold. All inputs are blank. No breakeven figure has been established.",
        "",
        "PURPOSE",
        "Answer one question: how many passengers a year does this line need to cover its costs,",
        "and how does that compare with the number of people who currently travel the corridor at all?",
        "That comparison is stop rule SR-2 in deliverables/feasibility_screen.md.",
        "",
        "HOW TO USE",
        "1. Fill a yellow input cell on 'Assumptions' ONLY together with its Source column entry.",
        "   The source is the manifest ID from deliverables/data_sources.md, e.g. inegi-2020-censo.",
        "2. Green cells are calculated. Do not type over them.",
        "3. Blank inputs propagate as blank, not as zero — the model stays silent until it is fed.",
        "4. Read 'Breakeven'. Read 'Sensitivity' before believing 'Breakeven'.",
        "",
        "CONVENTIONS",
        "Currency and base year are declared on 'Assumptions' and apply to every money figure.",
        "Mixing nominal and real figures, or MXN and USD, is risk R-10 in the risk register.",
        "",
        "WHAT THIS MODEL DELIBERATELY DOES NOT DO",
        "It does not forecast demand. Projected ridership is corridor travel × an assumed capture",
        "rate that the analyst enters by hand; the model reports what that assumption implies,",
        "it does not defend it. Capital recovery is shown separately from operating breakeven",
        "because the funding model is unknown at screen stage — a line may be worth operating",
        "while never recovering its capital, and the screen should be able to say so.",
        "",
        "It is a screening tool. Its output supports a decision to study further, nothing more.",
        "",
        "Regenerate with: python3 analysis/scripts/build_breakeven_model.py",
    ]
    for i, text in enumerate(lines, start=2):
        c = ws.cell(row=i, column=1, value=text)
        if text.isupper() and text:
            c.font = SECTION
    widths(ws, {1: 100})


def build_assumptions(ws) -> None:
    ws["A1"] = "Assumptions — all values pending Phase 2"
    ws["A1"].font = TITLE
    ws["A2"] = "Yellow = enter a value with its source. Green = calculated. Never fill a value without a source."
    ws["A2"].font = NOTE
    header_row(ws, 3, ["Parameter", "Value", "Unit", "Source (manifest ID)", "Notes"])

    section(ws, 4, "CORRIDOR")
    param(ws, 5, "Route length", "km", fmt=COUNT,
          note="Plausible alignment, not straight-line distance")

    section(ws, 6, "CAPITAL")
    param(ws, 7, "Capital cost per route-km", "MXN million / km", fmt=MONEY,
          note="[ANALOGUE] — only from a project of comparable terrain class")
    param(ws, 8, "Total capital cost", "MXN million",
          formula=f'=IF({blank("B5","B7")},"",B5*B7)', fmt=MONEY)
    param(ws, 9, "Discount rate", "% / yr", fmt=PCT,
          note="Social discount rate used for public projects")
    param(ws, 10, "Asset life", "years", fmt=COUNT)
    param(ws, 11, "Annualised capital charge", "MXN million / yr",
          formula=f'=IF({blank("B8","B9","B10")},"",-PMT(B9,B10,B8))', fmt=MONEY,
          note="Level annual charge recovering capital over asset life")

    section(ws, 12, "OPERATING")
    param(ws, 13, "Daily services each way", "trains / day", fmt=COUNT)
    param(ws, 14, "Operating days per year", "days", fmt=COUNT)
    param(ws, 15, "Annual train-km", "train-km / yr",
          formula=f'=IF({blank("B5","B13","B14")},"",B13*2*B14*B5)', fmt=COUNT,
          note="Services each way × 2 × operating days × route length")
    param(ws, 16, "Operating cost per train-km", "MXN / train-km", fmt=MONEY,
          note="All-in: crew, energy, maintenance, track access, overhead")
    param(ws, 17, "Annual operating cost", "MXN million / yr",
          formula=f'=IF({blank("B15","B16")},"",B15*B16/1000000)', fmt=MONEY)

    section(ws, 18, "REVENUE")
    param(ws, 19, "Average fare per trip", "MXN", fmt=MONEY,
          note="Blended across classes and distances actually travelled")
    param(ws, 20, "Non-fare revenue per trip", "MXN", fmt=MONEY,
          note="Concessions, advertising, parking; 0 is a defensible screen value")
    param(ws, 21, "Average revenue per trip", "MXN",
          formula=f'=IF({blank("B19","B20")},"",B19+B20)', fmt=MONEY)

    section(ws, 22, "DEMAND")
    param(ws, 23, "Corridor travel, all modes", "trips / yr", fmt=COUNT,
          note="Observed bus + air + private vehicle. NOT derived from population — risk R-03")
    param(ws, 24, "Assumed rail mode capture", "% of corridor travel", fmt=PCT,
          note="The assumption most likely to be wrong — risk R-04. State it, test it on 'Sensitivity'")
    param(ws, 25, "Projected annual ridership", "trips / yr",
          formula=f'=IF({blank("B23","B24")},"",B23*B24)', fmt=COUNT)

    section(ws, 26, "CONVENTIONS")
    param(ws, 27, "Base year", "yyyy", note="All money figures are real terms in this year")
    param(ws, 28, "Currency", "", note="MXN throughout; convert at a stated rate and record it")
    param(ws, 29, "FX rate used, if any", "MXN / USD", fmt=MONEY)

    widths(ws, {1: 34, 2: 16, 3: 22, 4: 26, 5: 74})
    ws.freeze_panes = "A4"


def build_breakeven(ws) -> None:
    ws["A1"] = "Breakeven"
    ws["A1"].font = TITLE
    ws["A2"] = "Blank output means an input it depends on has not been established. That is the correct display."
    ws["A2"].font = NOTE
    header_row(ws, 3, ["Output", "Value", "Unit", "Basis", "Notes"])

    a = "Assumptions!"
    section(ws, 4, "ANNUAL COST")
    param(ws, 5, "Annual operating cost", "MXN million / yr",
          formula=f"={a}B17", fmt=MONEY, source="Assumptions B17")
    param(ws, 6, "Annualised capital charge", "MXN million / yr",
          formula=f"={a}B11", fmt=MONEY, source="Assumptions B11")
    param(ws, 7, "Total annual cost", "MXN million / yr",
          formula=f'=IF({blank("B5","B6")},"",B5+B6)', fmt=MONEY)

    section(ws, 8, "BREAKEVEN RIDERSHIP")
    param(ws, 9, "Average revenue per trip", "MXN",
          formula=f"={a}B21", fmt=MONEY, source="Assumptions B21")
    param(ws, 10, "Breakeven — operating cost only", "trips / yr",
          formula=f'=IF(OR(B5="",B9="",B9=0),"",B5*1000000/B9)', fmt=COUNT,
          note="The screening figure: can the line cover the cost of running it?")
    param(ws, 11, "Breakeven — operating + capital", "trips / yr",
          formula=f'=IF(OR(B7="",B9="",B9=0),"",B7*1000000/B9)', fmt=COUNT,
          note="Shown separately: funding model is unknown at screen stage")

    section(ws, 12, "AGAINST ACTUAL CORRIDOR TRAVEL")
    param(ws, 13, "Corridor travel, all modes", "trips / yr",
          formula=f"={a}B23", fmt=COUNT, source="Assumptions B23")
    param(ws, 14, "Operating breakeven as share of all corridor travel", "%",
          formula=f'=IF(OR(B10="",B13="",B13=0),"",B10/B13)', fmt=PCT,
          note="Above 100% means SR-2 triggers: unbuildable demand case")
    param(ws, 15, "Projected annual ridership", "trips / yr",
          formula=f"={a}B25", fmt=COUNT, source="Assumptions B25")
    param(ws, 16, "Margin over operating breakeven", "trips / yr",
          formula=f'=IF(OR(B15="",B10=""),"",B15-B10)', fmt=COUNT,
          note="Negative means the assumed capture rate does not cover operating cost")

    section(ws, 17, "STOP RULE SR-2")
    ws.cell(row=18, column=1, value="Demand floor test")
    t = ws.cell(
        row=18, column=2,
        value='=IF(OR(B10="",B13=""),"pending inputs",'
              'IF(B10>B13,"SR-2 TRIGGERED — breakeven exceeds all corridor travel at 100% capture",'
              '"SR-2 not triggered"))',
    )
    t.fill, t.border, t.font = DERIVED_FILL, BOX, SECTION
    ws.cell(row=18, column=5,
            value="Record the result in deliverables/feasibility_screen.md §2").font = NOTE

    widths(ws, {1: 46, 2: 20, 3: 20, 4: 20, 5: 72})
    ws.freeze_panes = "A4"


def build_sensitivity(ws) -> None:
    ws["A1"] = "Sensitivity — fare"
    ws["A1"].font = TITLE
    ws["A2"] = ("Breakeven is close to linear in fare, so this grid mostly guards against a "
                "conclusion resting on one optimistic fare assumption.")
    ws["A2"].font = NOTE
    ws["A3"] = ("Read row 8 first: if breakeven exceeds 100% of corridor travel anywhere in the "
                "plausible fare range, the demand case is fragile.")
    ws["A3"].font = NOTE

    steps = [-0.20, -0.10, 0.0, 0.10, 0.20]
    header_row(ws, 5, ["Fare scenario"] + [f"{s:+.0%}" if s else "base" for s in steps])

    rows = [
        (6, "Average fare per trip (MXN)",
         lambda col, s: f'=IF(Assumptions!$B$19="","",Assumptions!$B$19*{1 + s})', MONEY),
        (7, "Revenue per trip incl. non-fare (MXN)",
         lambda col, s: f'=IF(OR({col}6="",Assumptions!$B$20=""),"",{col}6+Assumptions!$B$20)', MONEY),
        (8, "Breakeven ridership, operating (trips/yr)",
         lambda col, s: f'=IF(OR({col}7="",{col}7=0,Breakeven!$B$5=""),"",Breakeven!$B$5*1000000/{col}7)', COUNT),
        (9, "As share of all corridor travel",
         lambda col, s: f'=IF(OR({col}8="",Assumptions!$B$23="",Assumptions!$B$23=0),"",'
                        f'{col}8/Assumptions!$B$23)', PCT),
        (10, "Margin vs projected ridership (trips/yr)",
         lambda col, s: f'=IF(OR({col}8="",Assumptions!$B$25=""),"",Assumptions!$B$25-{col}8)', COUNT),
    ]
    for row, label, make, fmt in rows:
        ws.cell(row=row, column=1, value=label)
        for i, s in enumerate(steps):
            col = get_column_letter(2 + i)
            c = ws.cell(row=row, column=2 + i, value=make(col, s))
            c.fill, c.border, c.number_format = DERIVED_FILL, BOX, fmt

    ws["A12"] = "TO ADD IN PHASE 2"
    ws["A12"].font = SECTION
    for i, text in enumerate(
        [
            "Capture-rate sensitivity — the dominant uncertainty (risk R-04). Vary Assumptions!B24 "
            "across a range whose low end is a rail service nobody switches to.",
            "Capital cost per km sensitivity — analogue transfer error is the second dominant "
            "uncertainty (risk R-02), and matters most for the operating+capital breakeven.",
            "Both are deferred until real inputs exist: a sensitivity grid over invented base "
            "values reads as analysis while carrying no information.",
        ],
        start=13,
    ):
        ws.cell(row=i, column=1, value="• " + text).font = NOTE

    widths(ws, {1: 42, 2: 16, 3: 16, 4: 16, 5: 16, 6: 16})


def main() -> None:
    wb = Workbook()
    build_readme(wb.active)
    build_assumptions(wb.create_sheet("Assumptions"))
    build_breakeven(wb.create_sheet("Breakeven"))
    build_sensitivity(wb.create_sheet("Sensitivity"))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    wb.save(OUT)
    print(f"wrote {OUT.relative_to(ROOT)}  ({OUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
