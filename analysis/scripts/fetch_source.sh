#!/usr/bin/env bash
# Fetch a source document, hash it, and emit its manifest row.
#
#   analysis/scripts/fetch_source.sh <source-id> <url>
#
# Refuses to overwrite an existing raw file: a source already retrieved is not
# re-downloaded. Delete the file deliberately to force a re-fetch.
set -euo pipefail

if [[ $# -ne 2 ]]; then
  echo "usage: $0 <source-id> <url>" >&2
  echo "  source-id format: <pub>-<yyyy>-<slug>, e.g. sict-2024-pnid" >&2
  exit 2
fi

id="$1"
url="$2"
root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
raw_dir="$root/sources/raw"
mkdir -p "$raw_dir"

existing="$(find "$raw_dir" -maxdepth 1 -name "$id.*" -print -quit)"
if [[ -n "$existing" ]]; then
  echo "already retrieved: $existing" >&2
  echo "check deliverables/data_sources.md before re-fetching; delete the file to force." >&2
  exit 0
fi

tmp="$(mktemp)"
trap 'rm -f "$tmp"' EXIT

echo "fetching $url" >&2
curl -fsSL --retry 4 --retry-delay 2 --retry-all-errors -o "$tmp" "$url"

mime="$(file -b --mime-type "$tmp")"
case "$mime" in
  application/pdf)              ext=pdf  ;;
  text/csv|text/plain)          ext=csv  ;;
  application/json)             ext=json ;;
  application/zip)              ext=zip  ;;
  *)                            ext=bin  ;;
esac

dest="$raw_dir/$id.$ext"
mv "$tmp" "$dest"
trap - EXIT

sha="$(sha256sum "$dest" | cut -d' ' -f1)"
size_mb="$(( $(stat -c%s "$dest") / 1048576 ))"
retrieved="$(date -u +%Y-%m-%d)"

echo >&2
echo "saved: $dest (${size_mb}MB, gitignored)" >&2
echo "add this row to deliverables/data_sources.md §1:" >&2
echo >&2
echo "| $id | <title> | <publisher> | primary | $url | $retrieved | $sha | sources/extracted/$id/ | active |"
