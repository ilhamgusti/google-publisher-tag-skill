---
name: google-publisher-tag
description: Official Google Publisher Tag (GPT) and Google Ad Manager developer reference, guides, best practices, and code samples. Use when implementing, debugging, reviewing, or optimizing GPT ad tags, ad slots, display formats (interstitial, rewarded, anchor, side rail, out-of-page), key-value targeting, responsive ad sizing, lazy loading, SRA batching, refresh strategies, Publisher Console diagnosis, or Core Web Vitals (CLS/performance) ad optimizations.
---

# Google Publisher Tag (GPT) Skill

This skill provides direct access to the official Google Publisher Tag (GPT) and Google Ad Manager documentation mirror, guides, TypeScript API reference, and runnable code samples.

---

## Documentation Location

The canonical documentation mirror is maintained in:
- **Repository-relative path:** `docs/` (when working within this repository or a project containing a GPT mirror)
- **Skill package reference:** `<repo-root>/docs/` or `<skill-dir>/docs/`

> **Note on Upstream Sync:**
> `docs/` is a byte-identical mirror of official Google Publisher Tag documentation.
> Run `./docs/scripts/refetch.sh` to pull upstream updates, followed by `python3 scripts/build-okf.py` to rebuild the OKF bundle.
> **NEVER** edit files in `docs/` directly or inject YAML frontmatter into them, keeping them byte-identical to upstream for clean cutover.
> Always read files on demand from `docs/`.

---

## Core Invariants & Rules for GPT Implementations

1. **Async Command Queue Pattern**:
   Always guard and queue GPT calls using the command queue. Never assume `window.googletag` methods are immediately available:
   ```javascript
   window.googletag = window.googletag || { cmd: [] };
   googletag.cmd.push(() => {
     // GPT operations
   });
   ```
   Do not listen to `<script>` tag `onload` events to trigger GPT calls, as internal modules (`pubads_impl.js`) load asynchronously.

2. **Strict Execution Order**:
   Race conditions occur if calls are mis-ordered. Use one of the standard valid orderings:
   - **Define-Enable-Display**:
     1. Page-level settings & targeting (`googletag.pubads().setTargeting(...)`)
     2. Slot definitions (`googletag.defineSlot(...)`)
     3. Enable services (`googletag.enableServices()`)
     4. Display slots (`googletag.display(...)`)

3. **Checking API Readiness**:
   - Do NOT check `typeof googletag !== 'undefined'` to know if GPT is ready.
   - Use `googletag.apiReady` or `googletag.pubadsReady`, or simply queue callbacks in `googletag.cmd.push`.

4. **DOM Placement & Anti-CLS (Cumulative Layout Shift)**:
   - Do not move slot container elements in the DOM after `googletag.display()` is called.
   - Reserve space for slots using CSS `min-height` / wrapper containers or use `collapseEmptyDivs()` before enabling services to prevent layout shifts.

5. **Single Request Architecture (SRA)**:
   - `googletag.pubads().enableSingleRequest()` batches ad requests.
   - For infinite scroll or dynamic content, disable initial load (`googletag.pubads().disableInitialLoad()`) and control request batching manually with `googletag.pubads().refresh([slots])`.

---

## Task Routing Table

Use this table to quickly locate the relevant guide or sample in `docs/`:

| Goal / Topic | Primary Documentation File | Code / Implementation Details |
|---|---|---|
| **Quick Start / Test Ad** | `docs/guides/get-started.md` | `docs/samples/display-test-ad.md` |
| **Core Concepts & Lifecycle** | `docs/guides/learn-basics.md` | `docs/samples/basic-concepts.md` |
| **Complete API Reference** | `docs/reference.md` | 8,200+ lines TS definitions for `googletag.*` |
| **Avoiding Common Mistakes** | `docs/common-implementation-mistakes.md` | Pitfalls: closures, DOM moves, script onload |
| **Ad Sizes (Fixed/Fluid/Responsive)** | `docs/guides/ad-sizes.md` | `docs/samples/ad-sizes.md` (`sizeMapping()`) |
| **Key-Value Targeting** | `docs/guides/key-value-targeting.md` | `docs/samples/key-value-targeting.md` |
| **Ad Loading & Refresh Control** | `docs/guides/control-ad-loading.md` | `docs/samples/refresh.md` |
| **Lazy Loading Ads** | `docs/samples/lazy-loading.md` | Sample code in `docs/samples/lazy-loading/{js,ts}/` |
| **Infinite Scroll / Dynamic Content**| `docs/samples/infinite-content.md` | Dynamic slot creation & selective refresh |
| **SRA Batching Control** | `docs/samples/control-sra-batching.md` | `enableSingleRequest()` batching patterns |
| **Anchor Ads (Top/Bottom sticky)** | `docs/samples/display-anchor-ad.md` | Out-of-page anchor slot setup |
| **Side Rail Ads** | `docs/samples/display-side-rail-ad.md` | Left/right side rail setup |
| **Web Interstitial Ads** | `docs/samples/display-web-interstitial-ad.md` | Full-page web interstitial slot |
| **Rewarded Ads** | `docs/samples/display-rewarded-ad.md` | Rewarded ad display & reward callbacks |
| **Out-of-page Ads** | `docs/samples/display-out-of-page-ad.md` | Generic out-of-page slot definition |
| **Event Listeners** | `docs/samples/ad-event-listeners.md` | `slotRenderEnded`, `impressionViewable`, etc. |
| **Layout Shift (CLS) Optimization** | `docs/guides/minimize-layout-shift.md` | `docs/samples/reserve-space.md` |
| **Collapse Empty Slots** | `docs/samples/collapse-empty-ad-slots.md` | `collapseEmptyDivs()` |
| **Publisher Console Debugging** | `docs/guides/publisher-console.md` | Error messages in `docs/guides/publisher-console-messages.md` |
| **TypeScript Setup** | `docs/guides/use-typescript.md` | `docs/reference.md` type definitions |
| **Privacy (GDPR/CCPA/Limited Ads)** | `docs/samples/configure-privacy.md` | `docs/samples/display-limited-ad.md` |
| **Security (CSP & COEP)** | `docs/guides/content-security-policy.md` | `docs/guides/cross-origin-embedder-policy.md` |
| **React / Next.js Integration** | `docs/samples/integrations/react.md` | React component integration guide |

---

## Directory Structure of Docs

```
docs/
├── README.md                           # Mirror overview and sync documentation
├── reference.md                        # Full TypeScript API reference (8200+ lines)
├── common-implementation-mistakes.md   # Detailed anti-patterns and solutions
├── adsense-attributes.md               # AdSense attribute reference
├── release-notes.md                    # Production release notes history
├── versions.md                         # GPT version table
├── sample-builder.md                   # Custom sample builder guide
├── guides/                             # 16 official guides
│   ├── get-started.md
│   ├── learn-basics.md
│   ├── use-typescript.md
│   ├── ad-sizes.md
│   ├── key-value-targeting.md
│   ├── control-ad-loading.md
│   ├── passback-tags.md
│   ├── cross-origin-embedder-policy.md
│   ├── content-security-policy.md
│   ├── publisher-console.md
│   ├── publisher-console-messages.md
│   ├── general-best-practices.md
│   ├── ad-best-practices.md
│   ├── minimize-layout-shift.md
│   ├── monitor-performance.md
│   └── config-migration.md
├── samples/                            # 20+ sample specifications
│   ├── basic-concepts.md
│   ├── display-test-ad.md
│   ├── refresh.md
│   ├── control-sra-batching.md
│   ├── infinite-content.md
│   ├── lazy-loading.md
│   ├── event-based-requests.md
│   ├── shadow-dom.md
│   ├── display-anchor-ad.md
│   ├── display-side-rail-ad.md
│   ├── display-out-of-page-ad.md
│   ├── display-web-interstitial-ad.md
│   ├── display-gaming-interstitial-ad.md
│   ├── display-rewarded-ad.md
│   ├── offerwall-custom-choice.md
│   ├── key-value-targeting.md
│   ├── ad-sizes.md
│   ├── collapse-empty-ad-slots.md
│   ├── reserve-space.md
│   ├── ad-event-listeners.md
│   ├── configure-privacy.md
│   ├── display-limited-ad.md
│   ├── integrations/react.md
│   └── <sample-name>/                  # Runnable code directories
│       ├── js/demo.html
│       ├── ts/{index.html, sample.ts}
│       └── legacyjs/demo.html
├── support/
│   ├── browser-support.md
│   └── feedback-questions.md
└── scripts/
    ├── refetch.sh                      # Upstream mirror sync script
    └── check-links.sh                  # Documentation link validator
```

---

## Workflow for Agents Working on GPT

1. **Identify the Intent**: Match the task to the [Task Routing Table](#task-routing-table).
2. **Read Targeted Documentation**: Read only the relevant guide or sample (e.g. `docs/samples/lazy-loading.md`) rather than reading large files upfront.
3. **Inspect Sample Code**: When generating code for complex slots (anchor, rewarded, interstitial), read the corresponding `docs/samples/<name>/js/demo.html` or `sample.ts`.
4. **API Verification**: For exact parameter types, method options, or event payload fields, grep or inspect `docs/reference.md`.
5. **Sanity Check Against Pitfalls**: Verify against `docs/common-implementation-mistakes.md` before finalizing ad slot scripts.
