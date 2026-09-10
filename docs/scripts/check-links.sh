#!/usr/bin/env bash
#
# check-links.sh — verify every relative markdown link in README.md + related.md
# (and any other .md passed as args) resolves to an existing file.
#
# External http(s) links and anchors (#…) are skipped. Exit 1 if any broken.
#
set -euo pipefail

DOCS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$DOCS_DIR"

# default files to check
files=()
if [ "$#" -gt 0 ]; then files=("$@"); else files=(README.md related.md); fi

broken=0
checked=0

for f in "${files[@]}"; do
  [ -f "$f" ] || { echo "✗ file not found: $f"; broken=$((broken+1)); continue; }
  # extract link targets: [text](target)  — grep -oE pulls each `](...)`
  while IFS= read -r tgt; do
    # strip leading/trailing whitespace
    tgt="${tgt//[[:space:]]/}"
    # skip empty, anchors, external URLs, mailto
    case "$tgt" in
      ""|"#"*) continue ;;
      http://*|https://*|mailto:*) continue ;;
    esac
    # strip any anchor fragment
    path="${tgt%%#*}"
    [ -z "$path" ] && continue
    checked=$((checked+1))
    if [ ! -e "$path" ]; then
      echo "✗ BROKEN  $f  →  $tgt"
      broken=$((broken+1))
    fi
  done < <(grep -oE '\]\([^)]+\)' "$f" | sed -E 's/^\]\(//; s/\)$//')
done

echo ""
echo "checked: $checked   broken: $broken"
[ "$broken" = 0 ] && echo "✓ all relative links resolve" || exit 1
