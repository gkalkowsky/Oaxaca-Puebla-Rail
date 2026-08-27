#!/usr/bin/env python3
"""Extract a raw source document to committed markdown.

    python3 analysis/scripts/extract_source.py <source-id> [--force]

Writes sources/extracted/<source-id>/document.md plus an extraction.json
recording which extractor ran, when, and against which SHA-256. That record is
what makes a citation auditable: it ties committed markdown to a specific raw
file that is itself listed in deliverables/data_sources.md.

Skips work when an extraction already exists. Do not re-extract a source that
is already present -- pass --force only to deliberately redo one.

Extractors, in preference order:
  1. marker-pdf   -- layout-aware, preserves tables (needs model weights)
  2. pdftotext    -- poppler, layout mode; adequate for text-heavy documents
  3. pypdf        -- pure python fallback, weakest table handling
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / "sources" / "raw"
EXTRACTED = ROOT / "sources" / "extracted"


def find_raw(source_id: str) -> Path:
    matches = sorted(p for p in RAW.glob(f"{source_id}.*") if p.is_file())
    if not matches:
        sys.exit(
            f"no raw file for '{source_id}' in {RAW.relative_to(ROOT)}/\n"
            f"fetch it first: analysis/scripts/fetch_source.sh {source_id} <url>"
        )
    return matches[0]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def extract_marker(src: Path, out_dir: Path) -> str | None:
    if shutil.which("marker_single") is None:
        return None
    subprocess.run(
        ["marker_single", str(src), "--output_dir", str(out_dir)],
        check=True,
    )
    produced = sorted(out_dir.rglob("*.md"))
    if not produced:
        return None
    text = produced[0].read_text(encoding="utf-8")
    for stray in produced:
        if stray.name != "document.md":
            stray.unlink()
    return text


def extract_pymupdf(src: Path, _out_dir: Path) -> str | None:
    """Coordinate-aware text extraction.

    Preferred over pdftotext/pypdf for the fixed-layout DGST tables: PyMuPDF
    exposes word-level bounding boxes, so columns can be reconstructed
    geometrically rather than inferred from reading order. Reading order in
    these documents interleaves columns and silently scrambles rows.
    """
    try:
        import pymupdf
    except ImportError:
        return None
    doc = pymupdf.open(str(src))
    out = []
    for n, page in enumerate(doc, start=1):
        out.append(f"\n\n<!-- page {n} -->\n\n{page.get_text()}")
    return "".join(out)


def extract_pdftotext(src: Path, _out_dir: Path) -> str | None:
    if shutil.which("pdftotext") is None:
        return None
    result = subprocess.run(
        ["pdftotext", "-layout", "-enc", "UTF-8", str(src), "-"],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout


def extract_pypdf(src: Path, _out_dir: Path) -> str | None:
    try:
        from pypdf import PdfReader
    except ImportError:
        return None
    reader = PdfReader(str(src))
    pages = []
    for n, page in enumerate(reader.pages, start=1):
        pages.append(f"\n\n<!-- page {n} -->\n\n{page.extract_text() or ''}")
    return "".join(pages)


EXTRACTORS = (
    ("marker", extract_marker),
    ("pymupdf", extract_pymupdf),
    ("pdftotext", extract_pdftotext),
    ("pypdf", extract_pypdf),
)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("source_id")
    ap.add_argument("--force", action="store_true",
                    help="re-extract even though an extraction already exists")
    args = ap.parse_args()

    out_dir = EXTRACTED / args.source_id
    record = out_dir / "extraction.json"

    if record.exists() and not args.force:
        prior = json.loads(record.read_text(encoding="utf-8"))
        print(
            f"already extracted: {out_dir.relative_to(ROOT)}/ "
            f"(extractor={prior['extractor']}, {prior['extracted_utc']})\n"
            f"nothing to do -- pass --force to redo."
        )
        return

    src = find_raw(args.source_id)
    out_dir.mkdir(parents=True, exist_ok=True)

    if src.suffix.lower() != ".pdf":
        # Non-PDF sources (CSV, JSON) are evidence as-is; copy them through so
        # the extracted tree stays the single place deliverables cite.
        dest = out_dir / f"data{src.suffix.lower()}"
        shutil.copy2(src, dest)
        used, body = "verbatim-copy", None
    else:
        used = body = None
        for name, fn in EXTRACTORS:
            try:
                body = fn(src, out_dir)
            except subprocess.CalledProcessError as exc:
                print(f"{name} failed ({exc}); trying next extractor", file=sys.stderr)
                continue
            if body:
                used = name
                break
        if body is None:
            sys.exit(
                "no extractor available -- install poppler-utils (pdftotext) "
                "or `pip install -r analysis/scripts/requirements.txt`"
            )
        header = (
            f"<!-- source-id: {args.source_id} -->\n"
            f"<!-- extractor: {used} -->\n"
            f"<!-- raw sha256: {sha256(src)} -->\n\n"
        )
        (out_dir / "document.md").write_text(header + body, encoding="utf-8")

    record.write_text(
        json.dumps(
            {
                "source_id": args.source_id,
                "raw_filename": src.name,
                "raw_sha256": sha256(src),
                "extractor": used,
                "extracted_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"extracted {args.source_id} -> {out_dir.relative_to(ROOT)}/ (extractor={used})")
    print("now confirm the manifest row in deliverables/data_sources.md and commit the extraction.")


if __name__ == "__main__":
    main()
