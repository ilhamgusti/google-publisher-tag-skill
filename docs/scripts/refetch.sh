#!/usr/bin/env bash
#
# refetch.sh — sync GPT docs mirror, driven by the official release-notes Atom feed.
#
# Behavior:
#   default      fetch the Atom feed, compare <updated> with cached value,
#                only refetch everything if the feed advanced (or no cache).
#   --force      refetch regardless of feed state.
#   --check      only print feed status, don't fetch anything.
#   --diff       print new release-note entries since last sync.
#
# Mirror files stay byte-identical to the source (.md.txt + GitHub code),
# so updates are a clean cutover. State lives in .cache/.
#
set -euo pipefail

DOCS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CACHE_DIR="$DOCS_DIR/.cache"
BASE="https://developers.google.com/publisher-tag"
FEED="https://developers.google.com/static/publisher-tag/feeds/release-notes-atom.xml"
GHRAW="https://raw.githubusercontent.com/googleads/google-publisher-tag-samples/main/dist"
GHREPO="https://github.com/googleads/google-publisher-tag-samples/tree/main/dist"
DEMOBASE="https://googleads.github.io/google-publisher-tag-samples"

# ── page inventory ────────────────────────────────────────────────────────────
GUIDES=(
  get-started learn-basics use-typescript ad-sizes key-value-targeting
  control-ad-loading passback-tags cross-origin-embedder-policy
  content-security-policy publisher-console publisher-console-messages
  general-best-practices ad-best-practices minimize-layout-shift
  monitor-performance config-migration
)
TOPLEVEL=(
  "common-implementation-mistakes.md|common_implementation_mistakes.md.txt"
  "adsense-attributes.md|adsense_attributes.md.txt"
  "reference.md|reference.md.txt"
  "release-notes.md|release-notes.md.txt"
  "versions.md|versions.md.txt"
  "sample-builder.md|sample-builder.md.txt"
)
SUPPORT=( feedback-questions browser-support )
SAMPLES=(
  ad-event-listeners ad-sizes basic-concepts collapse-empty-ad-slots
  configure-privacy control-sra-batching display-anchor-ad
  display-gaming-interstitial-ad display-limited-ad display-out-of-page-ad
  display-rewarded-ad display-side-rail-ad display-test-ad
  display-web-interstitial-ad event-based-requests infinite-content
  key-value-targeting lazy-loading offerwall-custom-choice refresh
  reserve-space shadow-dom
)

# ── flags ─────────────────────────────────────────────────────────────────────
FORCE=0; CHECK_ONLY=0; DIFF=0
for arg in "$@"; do
  case "$arg" in
    --force) FORCE=1 ;;
    --check) CHECK_ONLY=1 ;;
    --diff)  DIFF=1 ;;
    -h|--help) sed -n '2,14p' "${BASH_SOURCE[0]}"; exit 0 ;;
    *) echo "unknown flag: $arg" >&2; exit 2 ;;
  esac
done

mkdir -p "$CACHE_DIR"

# ── 1. feed check ─────────────────────────────────────────────────────────────
echo "→ fetching feed…"
curl -sf -o "$CACHE_DIR/feed-atom.new.xml" "$FEED"

extract_first() { grep -oE "<$1>[^<]+</$1>" "$2" | head -1 | sed -E "s/<\/?$1>//g"; }
new_updated=$( extract_first updated "$CACHE_DIR/feed-atom.new.xml" )
feed_title=$(   extract_first title   "$CACHE_DIR/feed-atom.new.xml" )
latest_entry=$( grep -oE '<title>[^<]+</title>' "$CACHE_DIR/feed-atom.new.xml" \
                | sed -E 's/<\/?title>//g' | sed -n '2p' )
old_updated=$( cat "$CACHE_DIR/feed-updated" 2>/dev/null || echo "(none)" )

echo "  feed:      $feed_title"
echo "  latest:    $latest_entry"
echo "  updated:   $new_updated"
echo "  last sync: $old_updated"

if [ "$CHECK_ONLY" = 1 ]; then exit 0; fi

if [ "$DIFF" = 1 ]; then
  echo "→ entries since last sync ($old_updated):"
  if [ "$old_updated" = "(none)" ]; then
    echo "  (no prior sync — run without --diff first)"
  else
    awk -v cut="$old_updated" '
      /<entry>/ {e=1; t=""; u=""}
      /<title>/ && e {gsub(/<\/?title>|^[ \t]+|[ \t]+$/,""); t=$0}
      /<updated>/ && e {gsub(/<\/?updated>|^[ \t]+|[ \t]+$/,""); u=$0}
      /<\/entry>/ && e {e=0; if (u>cut) printf "  • %s  (%s)\n", t, u}
    ' "$CACHE_DIR/feed-atom.new.xml"
  fi
  exit 0
fi

if [ "$new_updated" = "$old_updated" ] && [ "$FORCE" = 0 ]; then
  echo "→ no change. use --force to refetch anyway."
  exit 0
fi

# ── 2. refetch .md.txt pages ──────────────────────────────────────────────────
echo "→ refetching pages…"
fetch() { # dst src
  mkdir -p "$DOCS_DIR/$(dirname "$1")"
  if curl -sf -o "$DOCS_DIR/$1" "$BASE/$2"; then echo "  ✓ $1";
  else echo "  ✗ FAIL $1"; fi
}
for g in "${GUIDES[@]}"; do fetch "guides/$g.md" "guides/$g.md.txt"; done
for t in "${TOPLEVEL[@]}"; do fetch "${t%%|*}" "${t##*|}"; done
fetch "samples/integrations/react.md" "samples/integrations/react.md.txt"
for s in "${SUPPORT[@]}"; do fetch "support/$s.md" "support/$s.md.txt"; done

# ── 3. regenerate samples (header from .md.txt + code from GitHub) ────────────
echo "→ regenerating samples with code…"
tmp=$(mktemp -d); trap 'rm -rf "$tmp"' EXIT
regen_sample() { # s
  local s="$1" k
  for k in js legacyjs ts; do
    local f=$([ "$k" = "ts" ] && echo "index.html" || echo "demo.html")
    curl -sf -o "$tmp/${s}__${k}.html" "$GHRAW/$s/$k/$f"
  done
  curl -sf -o "$tmp/${s}__ts-sample.ts" "$GHRAW/$s/ts/sample.ts"
  # header = .md.txt content before "## Sample implementation"
  curl -sf "$BASE/samples/$s.md.txt" \
    | awk '/^## Sample implementation/{exit} {print}' > "$tmp/$s.hdr"
  {
    cat "$tmp/$s.hdr"
    printf '\n## Sample implementation\n\n'
    printf '**Live demo:** [%s/%s/js/demo.html](%s/%s/js/demo.html)\n\n' "$DEMOBASE" "$s" "$DEMOBASE" "$s"
    printf '**Source:** [%s/%s](%s/%s)\n\n' "$GHREPO" "$s" "$GHREPO" "$s"
    printf '### JavaScript\n\n%s\n' '```html';      cat "$tmp/${s}__js.html";      printf '%s\n' '```'
    printf '\n### JavaScript (legacy)\n\n%s\n' '```html'; cat "$tmp/${s}__legacyjs.html"; printf '%s\n' '```'
    printf '\n### TypeScript\n\n%s\n' '`ts/index.html`:'
    printf '\n\n%s\n' '```html';      cat "$tmp/${s}__ts.html";       printf '%s\n' '```'
    printf '\n%s\n' '`ts/sample.ts`:'
    printf '\n\n%s\n' '```typescript'; cat "$tmp/${s}__ts-sample.ts"; printf '%s\n' '```'
  } > "$DOCS_DIR/samples/$s.md"
  # also sync runnable code dirs (mirror GitHub structure) — keeps .md and runnable files in lockstep
  mkdir -p "$DOCS_DIR/samples/$s/js" "$DOCS_DIR/samples/$s/legacyjs" "$DOCS_DIR/samples/$s/ts"
  cp "$tmp/${s}__js.html"       "$DOCS_DIR/samples/$s/js/demo.html"
  cp "$tmp/${s}__legacyjs.html" "$DOCS_DIR/samples/$s/legacyjs/demo.html"
  cp "$tmp/${s}__ts.html"       "$DOCS_DIR/samples/$s/ts/index.html"
  cp "$tmp/${s}__ts-sample.ts"  "$DOCS_DIR/samples/$s/ts/sample.ts"
  echo "  ✓ samples/$s.md"
}
for s in "${SAMPLES[@]}"; do regen_sample "$s"; done

# ── 4. commit feed state ──────────────────────────────────────────────────────
mv "$CACHE_DIR/feed-atom.new.xml" "$CACHE_DIR/feed-atom.xml"
echo "$new_updated" > "$CACHE_DIR/feed-updated"
echo "→ done. $old_updated → $new_updated"

# ── 5. rebuild OKF bundle hook ────────────────────────────────────────────────
OKF_BUILDER="$DOCS_DIR/../scripts/build-okf.py"
if [ -f "$OKF_BUILDER" ] && command -v python3 >/dev/null 2>&1; then
  echo "→ rebuilding OKF bundle..."
  python3 "$OKF_BUILDER"
fi
