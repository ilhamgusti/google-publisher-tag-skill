#!/usr/bin/env python3
"""
build-okf.py — Generate an Open Knowledge Format (OKF) v0.1 bundle from docs/

Maintains clean cutover for docs/ mirror by generating a separate okf/ bundle directory.
Ensures 100% OKF v0.1 conformance:
  - Every concept .md has valid YAML frontmatter with required `type` field.
  - Bundle root index.md declares okf_version: "0.1".
  - Subdirectory index.md files contain progressive disclosure lists without frontmatter.
  - log.md contains ISO 8601 date headings without frontmatter.
  - Sample runnable code is preserved alongside sample concepts.
"""

import os
import shutil
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = REPO_ROOT / "docs"
OKF_DIR = REPO_ROOT / "okf"

TIMESTAMP = "2026-09-10T00:00:00Z"

# Explicit curated metadata for guides, reference, support, and top-level pages
METADATA_MAP = {
    "guides/get-started.md": {
        "type": "Guide",
        "title": "Get Started with Google Publisher Tag",
        "description": "Quick start guide to displaying test ads and initializing GPT.",
        "resource": "https://developers.google.com/publisher-tag/guides/get-started",
        "tags": ["gpt", "getting-started", "test-ad", "basics"],
    },
    "guides/learn-basics.md": {
        "type": "Guide",
        "title": "Learn Basic GPT Concepts",
        "description": "Fundamental concepts of GPT including ad slots, services, targeting, and lifecycle.",
        "resource": "https://developers.google.com/publisher-tag/guides/learn-basics",
        "tags": ["gpt", "basics", "lifecycle", "architecture"],
    },
    "guides/use-typescript.md": {
        "type": "Guide",
        "title": "Use Google Publisher Tag with TypeScript",
        "description": "How to set up and use official GPT TypeScript type definitions.",
        "resource": "https://developers.google.com/publisher-tag/guides/use-typescript",
        "tags": ["gpt", "typescript", "types", "tooling"],
    },
    "guides/ad-sizes.md": {
        "type": "Guide",
        "title": "Ad Sizes (Fixed, Fluid, Responsive)",
        "description": "Configuring fixed, fluid, and responsive ad sizes using size mapping in GPT.",
        "resource": "https://developers.google.com/publisher-tag/guides/ad-sizes",
        "tags": ["gpt", "ad-sizes", "responsive", "size-mapping"],
    },
    "guides/key-value-targeting.md": {
        "type": "Guide",
        "title": "Key-Value Targeting",
        "description": "Configuring page-level and slot-level custom targeting keys and values.",
        "resource": "https://developers.google.com/publisher-tag/guides/key-value-targeting",
        "tags": ["gpt", "targeting", "key-value", "inventory"],
    },
    "guides/control-ad-loading.md": {
        "type": "Guide",
        "title": "Control Ad Loading and Refresh",
        "description": "Managing ad request batching, initial load, and refresh behavior.",
        "resource": "https://developers.google.com/publisher-tag/guides/control-ad-loading",
        "tags": ["gpt", "loading", "refresh", "sra"],
    },
    "guides/passback-tags.md": {
        "type": "Guide",
        "title": "Passback Tags",
        "description": "Serving ads through third-party ad servers or networks via passback tags.",
        "resource": "https://developers.google.com/publisher-tag/guides/passback-tags",
        "tags": ["gpt", "passback", "third-party", "ad-networks"],
    },
    "guides/cross-origin-embedder-policy.md": {
        "type": "Guide",
        "title": "Cross-Origin Embedder Policy (COEP)",
        "description": "Integrating GPT on pages that enforce Cross-Origin Embedder Policy.",
        "resource": "https://developers.google.com/publisher-tag/guides/cross-origin-embedder-policy",
        "tags": ["gpt", "coep", "security", "cross-origin"],
    },
    "guides/content-security-policy.md": {
        "type": "Guide",
        "title": "Content Security Policy (CSP)",
        "description": "Configuring Content Security Policy headers and directives for GPT.",
        "resource": "https://developers.google.com/publisher-tag/guides/content-security-policy",
        "tags": ["gpt", "csp", "security", "headers"],
    },
    "guides/publisher-console.md": {
        "type": "Troubleshooting",
        "title": "Google Publisher Console",
        "description": "Debugging ad delivery and performance issues using Google Publisher Console.",
        "resource": "https://developers.google.com/publisher-tag/guides/publisher-console",
        "tags": ["gpt", "debugging", "console", "troubleshooting"],
    },
    "guides/publisher-console-messages.md": {
        "type": "Troubleshooting",
        "title": "Publisher Console Message Reference",
        "description": "Catalog of error, warning, and informational messages from Publisher Console.",
        "resource": "https://developers.google.com/publisher-tag/guides/publisher-console-messages",
        "tags": ["gpt", "debugging", "errors", "warnings", "troubleshooting"],
    },
    "guides/general-best-practices.md": {
        "type": "Best Practice",
        "title": "General GPT Best Practices",
        "description": "Core best practices for performance, tag placement, and script execution.",
        "resource": "https://developers.google.com/publisher-tag/guides/general-best-practices",
        "tags": ["gpt", "best-practices", "performance", "optimization"],
    },
    "guides/ad-best-practices.md": {
        "type": "Best Practice",
        "title": "Ad Placement and Viewability Best Practices",
        "description": "Recommendations for ad sizing, slot viewability, and user experience.",
        "resource": "https://developers.google.com/publisher-tag/guides/ad-best-practices",
        "tags": ["gpt", "viewability", "placement", "best-practices"],
    },
    "guides/minimize-layout-shift.md": {
        "type": "Best Practice",
        "title": "Minimize Layout Shift (CLS)",
        "description": "Preventing Cumulative Layout Shift through slot reservation and styling.",
        "resource": "https://developers.google.com/publisher-tag/guides/minimize-layout-shift",
        "tags": ["gpt", "cls", "core-web-vitals", "layout-shift"],
    },
    "guides/monitor-performance.md": {
        "type": "Best Practice",
        "title": "Monitor Performance",
        "description": "Techniques and APIs to measure and monitor ad loading performance.",
        "resource": "https://developers.google.com/publisher-tag/guides/monitor-performance",
        "tags": ["gpt", "performance", "metrics", "monitoring"],
    },
    "guides/config-migration.md": {
        "type": "Guide",
        "title": "Config Migration to setConfig()",
        "description": "Guide for migrating legacy configuration settings to googletag.setConfig().",
        "resource": "https://developers.google.com/publisher-tag/guides/config-migration",
        "tags": ["gpt", "migration", "setConfig", "configuration"],
    },
    "reference.md": {
        "type": "API Reference",
        "title": "Google Publisher Tag API Reference",
        "description": "Complete TypeScript API reference for googletag namespace, interfaces, enums, and events.",
        "resource": "https://developers.google.com/publisher-tag/reference",
        "tags": ["gpt", "api", "reference", "typescript", "googletag"],
    },
    "common-implementation-mistakes.md": {
        "type": "Troubleshooting",
        "title": "Avoiding Common GPT Implementation Mistakes",
        "description": "Detailed catalog of frequent implementation anti-patterns, race conditions, and their fixes.",
        "resource": "https://developers.google.com/publisher-tag/common-implementation-mistakes",
        "tags": ["gpt", "anti-patterns", "pitfalls", "troubleshooting", "bugs"],
    },
    "adsense-attributes.md": {
        "type": "Reference",
        "title": "AdSense Attributes in GPT",
        "description": "Reference for AdSense attributes configurable through Google Publisher Tag.",
        "resource": "https://developers.google.com/publisher-tag/adsense-attributes",
        "tags": ["gpt", "adsense", "attributes", "reference"],
    },
    "release-notes.md": {
        "type": "Reference",
        "title": "GPT Production Release Notes",
        "description": "Changelog and historical release notes for Google Publisher Tag production releases.",
        "resource": "https://developers.google.com/publisher-tag/release-notes",
        "tags": ["gpt", "release-notes", "changelog", "versions"],
    },
    "versions.md": {
        "type": "Reference",
        "title": "GPT Version History",
        "description": "Historical GPT versions and release timeline.",
        "resource": "https://developers.google.com/publisher-tag/versions",
        "tags": ["gpt", "versions", "history"],
    },
    "sample-builder.md": {
        "type": "Tool",
        "title": "GPT Sample Builder",
        "description": "Documentation and guide for building custom GPT code samples.",
        "resource": "https://developers.google.com/publisher-tag/sample-builder",
        "tags": ["gpt", "sample-builder", "generator"],
    },
    "support/browser-support.md": {
        "type": "Support",
        "title": "Browser Support Matrix",
        "description": "Supported browsers, environments, and compatibility requirements for GPT.",
        "resource": "https://developers.google.com/publisher-tag/support/browser-support",
        "tags": ["gpt", "support", "browsers", "compatibility"],
    },
    "support/feedback-questions.md": {
        "type": "Support",
        "title": "Feedback and Support Options",
        "description": "Community, issue reporting, and official support channels for GPT developers.",
        "resource": "https://developers.google.com/publisher-tag/support/feedback-questions",
        "tags": ["gpt", "support", "help", "feedback"],
    },
}

SAMPLE_DESCRIPTIONS = {
    "basic-concepts.md": ("Basic Concepts Sample", "Sample demonstration of core GPT ad slot definition and rendering."),
    "display-test-ad.md": ("Display Test Ad", "Sample implementation showing how to display a test ad from Google's test network."),
    "refresh.md": ("Refresh Ad Slots", "Sample implementation showing how to refresh specific ad slots dynamically."),
    "control-sra-batching.md": ("Control SRA Batching", "Sample implementation demonstrating how to control SRA batching."),
    "infinite-content.md": ("Infinite Content / Scroll", "Sample showing lazy loading and dynamic ad slot injection for infinite scroll."),
    "lazy-loading.md": ("Lazy Loading Ads", "Sample showing viewport-based ad request pausing and lazy rendering."),
    "event-based-requests.md": ("Event-Based Ad Requests", "Sample demonstrating requesting ads triggered by specific user interactions."),
    "shadow-dom.md": ("Shadow DOM Integration", "Sample showing how to render GPT ads inside Shadow DOM boundaries."),
    "display-anchor-ad.md": ("Display Anchor Ad", "Sample implementing sticky top or bottom anchor ads for mobile and desktop."),
    "display-side-rail-ad.md": ("Display Side Rail Ad", "Sample implementing left and right side rail display ads."),
    "display-out-of-page-ad.md": ("Display Out-of-Page Ad", "Sample demonstrating generic out-of-page ad unit definition."),
    "display-web-interstitial-ad.md": ("Display Web Interstitial Ad", "Sample implementing full-screen interstitial ads between page navigations."),
    "display-gaming-interstitial-ad.md": ("Display Gaming Interstitial Ad", "Sample implementing gaming interstitial ad experiences."),
    "display-rewarded-ad.md": ("Display Rewarded Ad", "Sample implementing rewarded ads where users view ads for in-app rewards."),
    "offerwall-custom-choice.md": ("Offerwall Custom Choice", "Sample demonstrating publisher-customized choices inside Google Offerwall."),
    "key-value-targeting.md": ("Key-Value Targeting Sample", "Sample demonstrating page-level and slot-level targeting keys and values."),
    "ad-sizes.md": ("Ad Sizes Sample", "Sample implementation using sizeMapping to support responsive ad slots."),
    "collapse-empty-ad-slots.md": ("Collapse Empty Ad Slots", "Sample showing how to collapse unfilled ad slots automatically."),
    "reserve-space.md": ("Reserve Space (Anti-CLS)", "Sample demonstrating slot space reservation to prevent Cumulative Layout Shift."),
    "ad-event-listeners.md": ("Ad Event Listeners", "Sample listening to slotRenderEnded, impressionViewable, and slotVisibilityChanged."),
    "configure-privacy.md": ("Configure Privacy Settings", "Sample configuring CCPA (RDP), GDPR (TFUA), and COPPA privacy compliance."),
    "display-limited-ad.md": ("Display Limited Ads", "Sample implementing limited ads mode when cookie/personalization consent is absent."),
    "integrations/react.md": ("GPT React / Next.js Integration", "Guide and sample for integrating GPT into React and Next.js applications."),
}


def sanitize_yaml_string(s: str) -> str:
    """Escapes strings for YAML double quotes."""
    return s.replace('\\', '\\\\').replace('"', '\\"')


def generate_frontmatter(metadata: dict) -> str:
    lines = ["---"]
    lines.append(f"type: {metadata['type']}")
    lines.append(f"title: \"{sanitize_yaml_string(metadata['title'])}\"")
    lines.append(f"description: \"{sanitize_yaml_string(metadata['description'])}\"")
    if "resource" in metadata:
        lines.append(f"resource: \"{sanitize_yaml_string(metadata['resource'])}\"")
    if "tags" in metadata and metadata["tags"]:
        tags_str = ", ".join(metadata["tags"])
        lines.append(f"tags: [{tags_str}]")
    lines.append(f"timestamp: {metadata.get('timestamp', TIMESTAMP)}")
    lines.append("---")
    return "\n".join(lines)


def get_metadata_for_file(rel_path: str, content: str) -> dict:
    if rel_path in METADATA_MAP:
        return METADATA_MAP[rel_path]

    if rel_path.startswith("samples/"):
        sub_rel = rel_path[len("samples/"):]
        if sub_rel in SAMPLE_DESCRIPTIONS:
            title, desc = SAMPLE_DESCRIPTIONS[sub_rel]
            stem = Path(sub_rel).stem
            return {
                "type": "Sample",
                "title": title,
                "description": desc,
                "resource": f"https://developers.google.com/publisher-tag/samples/{stem}",
                "tags": ["gpt", "sample", stem.replace("-", " ")],
            }

    # Fallback heuristic
    first_heading = None
    first_para = None
    for line in content.splitlines():
        if line.startswith("# ") and not first_heading:
            first_heading = line[2:].strip()
        elif line.strip() and not line.startswith("#") and not first_para:
            first_para = line.strip()

    title = first_heading or Path(rel_path).stem.replace("-", " ").title()
    desc = first_para or f"Documentation for {title} in Google Publisher Tag."
    if len(desc) > 160:
        desc = desc[:157] + "..."

    category = rel_path.split("/")[0] if "/" in rel_path else "general"
    type_map = {
        "guides": "Guide",
        "samples": "Sample",
        "support": "Support",
    }
    concept_type = type_map.get(category, "Reference")

    return {
        "type": concept_type,
        "title": title,
        "description": desc,
        "tags": ["gpt", category],
    }


def build_bundle():
    print(f"Building OKF bundle in {OKF_DIR} from {DOCS_DIR}...")
    if OKF_DIR.exists():
        shutil.rmtree(OKF_DIR)
    OKF_DIR.mkdir(parents=True, exist_ok=True)

    # Track concepts for sub-index generation
    guides_entries = []
    samples_entries = []
    support_entries = []
    toplevel_entries = []

    # Process all markdown files in docs/
    for md_file in sorted(DOCS_DIR.glob("**/*.md")):
        rel_path = str(md_file.relative_to(DOCS_DIR))
        # Skip README.md from becoming a concept file
        if rel_path == "README.md":
            continue

        target_file = OKF_DIR / rel_path
        target_file.parent.mkdir(parents=True, exist_ok=True)

        content = md_file.read_text(encoding="utf-8")
        meta = get_metadata_for_file(rel_path, content)

        # Track for directory index
        entry = (rel_path, meta["title"], meta["description"])
        if rel_path.startswith("guides/"):
            guides_entries.append((rel_path.replace("guides/", ""), meta["title"], meta["description"]))
        elif rel_path.startswith("samples/"):
            samples_entries.append((rel_path.replace("samples/", ""), meta["title"], meta["description"]))
        elif rel_path.startswith("support/"):
            support_entries.append((rel_path.replace("support/", ""), meta["title"], meta["description"]))
        else:
            toplevel_entries.append((rel_path, meta["title"], meta["description"]))

        frontmatter = generate_frontmatter(meta)
        target_file.write_text(f"{frontmatter}\n\n{content}", encoding="utf-8")

    # Copy code assets in samples/ (HTML/TS/JS directories)
    for sample_dir in (DOCS_DIR / "samples").iterdir():
        if sample_dir.is_dir():
            target_sample_dir = OKF_DIR / "samples" / sample_dir.name
            target_sample_dir.mkdir(parents=True, exist_ok=True)
            for sub in sample_dir.iterdir():
                if sub.is_dir() and sub.name in ("js", "ts", "legacyjs"):
                    dest_sub = target_sample_dir / sub.name
                    if dest_sub.exists():
                        shutil.rmtree(dest_sub)
                    shutil.copytree(sub, dest_sub)

    # Create root index.md (with okf_version: "0.1" frontmatter)
    root_index_content = """---
okf_version: "0.1"
---

# Google Publisher Tag (GPT) Knowledge Bundle

An Open Knowledge Format (OKF) v0.1 bundle mirroring the official Google Publisher Tag developer documentation, TypeScript API references, and runnable samples.

## Knowledge Sections

- [Guides](./guides/) - 16 developer guides covering fundamentals, ad sizes, targeting, privacy, and optimization.
- [Reference](./reference.md) - Full 8,200+ lines TypeScript API reference for `googletag.*`.
- [Samples](./samples/) - 20+ ad format and behavior code samples with runnable JS/TS implementations.
- [Common Implementation Mistakes](./common-implementation-mistakes.md) - Critical anti-patterns, race conditions, and fixes.
- [Support](./support/) - Browser compatibility and official developer support channels.

## Reference & Notes

- [AdSense Attributes](./adsense-attributes.md) - AdSense attribute reference.
- [Release Notes](./release-notes.md) - Historical production release notes.
- [Versions](./versions.md) - GPT version timeline.
- [Sample Builder](./sample-builder.md) - Interactive custom sample generator.
"""
    (OKF_DIR / "index.md").write_text(root_index_content, encoding="utf-8")

    # Create okf/log.md (no frontmatter, ISO 8601 date headings)
    log_content = """# Update Log

## 2026-09-10
- **Creation**: Generated OKF v0.1 bundle from Google Publisher Tag documentation mirror.
- **Organization**: Structured concepts into guides, reference, samples, and support categories.
- **Enrichment**: Added type, title, description, resource links, and tags to all concepts.
"""
    (OKF_DIR / "log.md").write_text(log_content, encoding="utf-8")

    # Create sub-index files (NO frontmatter per OKF v0.1 spec)
    # 1. Guides index
    guides_index = ["# Guides", "", "Developer guides for Google Publisher Tag:", ""]
    for path, title, desc in sorted(guides_entries, key=lambda x: x[0]):
        guides_index.append(f"- [{title}](./{path}) - {desc}")
    (OKF_DIR / "guides" / "index.md").write_text("\n".join(guides_index) + "\n", encoding="utf-8")

    # 2. Samples index
    samples_index = ["# Samples", "", "Implementation samples with runnable JavaScript and TypeScript code:", ""]
    for path, title, desc in sorted(samples_entries, key=lambda x: x[0]):
        samples_index.append(f"- [{title}](./{path}) - {desc}")
    (OKF_DIR / "samples" / "index.md").write_text("\n".join(samples_index) + "\n", encoding="utf-8")

    # 3. Support index
    support_index = ["# Support", "", "Support options and browser compatibility:", ""]
    for path, title, desc in sorted(support_entries, key=lambda x: x[0]):
        support_index.append(f"- [{title}](./{path}) - {desc}")
    (OKF_DIR / "support" / "index.md").write_text("\n".join(support_index) + "\n", encoding="utf-8")

    print("OKF bundle generation complete.")


if __name__ == "__main__":
    build_bundle()
