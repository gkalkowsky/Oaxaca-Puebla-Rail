#!/usr/bin/env python3
"""Extract DGST 'Datos Viales' aforo tables to validated records.

    python3 analysis/scripts/extract_aforo.py <source-id> [<source-id> ...]

These pages are ROTATED 90 degrees. In PDF coordinate space a *station* is a
column of constant x, and a *field* is a band of constant y -- the logical
table is transposed. Reading-order text interleaves the columns, so records are
reconstructed from word bounding boxes, never from the text stream.

Field bands, top to bottom in PDF space (20 numeric bands):

    LONGITUD LATITUD D K' C_agg B_agg A_agg OTROS T3S2R4 T3S3 T3S2
    C3 C2 B A M TDPA SC TE KM

Station-name words sit below the numeric bands and read bottom-to-top.

Every record is validated against three independent identities before it is
allowed out:

    (1) A + B + C2 + C3 + T3S2 + T3S3 + T3S2R4 + OTROS + M == 100
    (2) C2 + C3 + T3S2 + T3S3 + T3S2R4 + OTROS         == C_agg
    (3) A + M                                          == A_agg

Identity (1) is why M matters: without motos the detailed classes sum to ~92.6
and look wrong. Records failing any identity are written to the reject file
with the reason and are NOT emitted for analysis.

Note the class label is 'T3S2' in these PDFs, not the hyphenated 'T3-S2'.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parents[2]
FIELDS = ["LONGITUD", "LATITUD", "D", "Kp", "C_agg", "B_agg", "A_agg", "OTROS",
          "T3S2R4", "T3S3", "T3S2", "C3", "C2", "B", "A", "M", "TDPA", "SC", "TE", "KM"]
TRUCKS = ["C2", "C3", "T3S2", "T3S3", "T3S2R4", "OTROS"]
NUM = re.compile(r"^-?\d+(?:\.\d+)?$")
TOL = 0.35  # percentage-point tolerance for rounding in published figures


def cluster(vals: list[float], gap: float) -> list[float]:
    """Group sorted scalars into clusters separated by more than `gap`."""
    out: list[list[float]] = []
    for v in sorted(vals):
        if out and v - out[-1][-1] <= gap:
            out[-1].append(v)
        else:
            out.append([v])
    return [sum(c) / len(c) for c in out]


def page_records(page: pymupdf.Page, page_no: int) -> tuple[list[dict], list[dict]]:
    words = page.get_text("words")
    if not words:
        return [], []

    nums = [(x0, y0, t) for x0, y0, x1, y1, t, *_ in words if NUM.match(t)]
    if len(nums) < 20:
        return [], []

    # Numeric field bands: cluster y over numeric tokens, keep the densest 20.
    bands = cluster([y for _, y, _ in nums], gap=6.0)
    counts = [(sum(1 for _, y, _ in nums if abs(y - b) < 6.0), b) for b in bands]
    bands = sorted(b for _, b in sorted(counts, reverse=True)[:len(FIELDS)])
    if len(bands) < len(FIELDS):
        return [], []
    band_field = dict(zip(bands, FIELDS))

    # Route per block, anchored on the 'RUTA' label rather than a prefix match:
    # the value sits at the same x, ~40pt above the label in PDF space. Federal
    # routes read 'MEX-135D', state feeder roads read 'OAX' / 'PUE', so matching
    # on 'MEX-' alone silently blanks every state road.
    routes = []
    for x0, y0, x1, y1, t, *_ in words:
        if t != "RUTA":
            continue
        cands = [(abs(yy - (y0 - 40.7)), tt)
                 for xx, yy, xx1, yy1, tt, *_ in words
                 if abs(xx - x0) < 2.5 and (y0 - 60) < yy < (y0 - 20)
                 and not NUM.match(tt) and tt not in (":", "AÑO")]
        if cands:
            routes.append((x0, min(cands)[1]))
    routes.sort()

    # Stations: cluster x over numeric tokens that fall on a band.
    on_band = [(x, y, t) for x, y, t in nums if any(abs(y - b) < 6.0 for b in bands)]
    st_xs = cluster([x for x, _, _ in on_band], gap=4.0)

    keep, reject = [], []
    for sx in st_xs:
        rec: dict = {}
        for x, y, t in on_band:
            if abs(x - sx) > 4.0:
                continue
            for b in bands:
                if abs(y - b) < 6.0:
                    rec[band_field[b]] = float(t)
                    break
        # A real station row carries the full percentage set plus TDPA.
        need = ["A", "B", "M", "TDPA", "LATITUD", "LONGITUD"] + TRUCKS
        if any(k not in rec for k in need):
            continue

        # Station name: words below the numeric bands, read bottom-to-top.
        floor = max(bands) + 8
        name_words = sorted(
            ((y0, t) for x0, y0, x1, y1, t, *_ in words
             if abs(x0 - sx) <= 6.0 and y0 > floor and not NUM.match(t)),
            reverse=True)
        rec["ESTACION"] = " ".join(t for _, t in name_words).strip()

        prev = [t for x, t in routes if x <= sx + 6.0]
        rec["RUTA"] = prev[-1] if prev else ""
        rec["page"] = page_no

        detailed = rec["A"] + rec["B"] + rec["M"] + sum(rec[c] for c in TRUCKS)
        truck_sum = sum(rec[c] for c in TRUCKS)
        problems = []
        if abs(detailed - 100.0) > TOL:
            problems.append(f"classes sum to {detailed:.1f}, not 100")
        if "C_agg" in rec and abs(truck_sum - rec["C_agg"]) > TOL:
            problems.append(f"trucks {truck_sum:.1f} != C_agg {rec['C_agg']:.1f}")
        if "A_agg" in rec and abs(rec["A"] + rec["M"] - rec["A_agg"]) > TOL:
            problems.append(f"A+M {rec['A']+rec['M']:.1f} != A_agg {rec['A_agg']:.1f}")
        if not (0 < rec["TDPA"] < 500000):
            problems.append(f"implausible TDPA {rec['TDPA']}")
        # Sanity bound only -- is this a coordinate inside Mexico at all? Being
        # outside the STUDY corridor is a scope question, not an extraction
        # failure, and must not be recorded as one: these volumes legitimately
        # carry stations in neighbouring states (Guerrero, Veracruz).
        if not (14 <= rec["LATITUD"] <= 33 and -118 <= rec["LONGITUD"] <= -86):
            problems.append(
                f"coordinates not in Mexico ({rec['LATITUD']}, {rec['LONGITUD']})")

        rec["truck_pct"] = round(truck_sum, 2)
        rec["artic_pct"] = round(rec["T3S2"] + rec["T3S3"] + rec["T3S2R4"], 2)
        rec["truck_tdpa"] = round(rec["TDPA"] * truck_sum / 100.0, 1)
        rec["artic_tdpa"] = round(rec["TDPA"] * rec["artic_pct"] / 100.0, 1)
        (reject if problems else keep).append(
            {**rec, "problems": problems} if problems else rec)
    return keep, reject


def main() -> None:
    ids = sys.argv[1:]
    if not ids:
        sys.exit("usage: extract_aforo.py <source-id> [<source-id> ...]")
    allk, allr = [], []
    for sid in ids:
        pdf = ROOT / "sources" / "raw" / f"{sid}.pdf"
        if not pdf.exists():
            sys.exit(f"missing {pdf}")
        doc = pymupdf.open(str(pdf))
        k_tot = r_tot = 0
        for i, page in enumerate(doc, start=1):
            k, r = page_records(page, i)
            for rec in k:
                rec["source_id"] = sid
            for rec in r:
                rec["source_id"] = sid
            allk += k
            allr += r
            k_tot += len(k)
            r_tot += len(r)
        print(f"{sid}: {k_tot} validated, {r_tot} rejected")

    outdir = ROOT / "working"
    outdir.mkdir(exist_ok=True)
    (outdir / "aforo_stations.json").write_text(
        json.dumps(allk, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    (outdir / "aforo_rejects.json").write_text(
        json.dumps(allr, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"\nTOTAL: {len(allk)} validated, {len(allr)} rejected "
          f"({100*len(allk)/max(1,len(allk)+len(allr)):.1f}% pass)")
    print("wrote working/aforo_stations.json and working/aforo_rejects.json")


if __name__ == "__main__":
    main()
