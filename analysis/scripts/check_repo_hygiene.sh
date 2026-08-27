#!/usr/bin/env bash
# Fail if anything staged violates repo policy:
#   - no blob over 50MB
#   - no raw source document committed
#   - no model weights or virtualenv content
#
# Run before committing, or wire in as a pre-commit hook:
#   ln -s ../../analysis/scripts/check_repo_hygiene.sh .git/hooks/pre-commit
set -euo pipefail

limit=$((50 * 1024 * 1024))
fail=0

while IFS= read -r path; do
  [[ -f "$path" ]] || continue
  size=$(stat -c%s "$path")
  if (( size > limit )); then
    printf 'BLOCKED %s (%dMB > 50MB limit)\n' "$path" "$(( size / 1048576 ))" >&2
    fail=1
  fi
  case "$path" in
    sources/raw/*)
      [[ "$path" == sources/raw/.gitkeep ]] && continue
      printf 'BLOCKED %s (raw sources are not committed; record it in data_sources.md)\n' "$path" >&2
      fail=1 ;;
    *.safetensors|*.ckpt|*.pt|*.pth|*.gguf|*.onnx)
      printf 'BLOCKED %s (model weights are not committed)\n' "$path" >&2
      fail=1 ;;
    .venv/*|venv/*|*/__pycache__/*)
      printf 'BLOCKED %s (environment/cache content is not committed)\n' "$path" >&2
      fail=1 ;;
  esac
done < <(git diff --cached --name-only --diff-filter=ACM)

if (( fail )); then
  echo >&2
  echo "commit blocked by repo hygiene policy (analysis/scripts/check_repo_hygiene.sh)" >&2
  exit 1
fi
echo "repo hygiene OK"
