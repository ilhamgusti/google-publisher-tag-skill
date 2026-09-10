# Google Publisher Tag (GPT) — Documentation Mirror, Agent Skill & OKF Bundle

A comprehensive developer resource for [Google Publisher Tag (GPT)](https://developers.google.com/publisher-tag) and Google Ad Manager, packaged for AI coding agents and developers in **two interoperable consumption modes**:

1. **Agent Skill (`SKILL.md`)** — Standard open agent skill format with task-based routing tables and implementation guardrails.
2. **Open Knowledge Format Bundle (`okf/`)** — An [Open Knowledge Format (OKF v0.1)](https://github.com/fabricioctelles/skills) bundle featuring structured YAML frontmatter on every concept, ready for semantic vector/BM25 search and LLM wiki ingestion.

The repository also maintains a **Live Upstream Mirror (`docs/`)** that remains 100% byte-identical to Google Developers documentation and GitHub sample repositories.

---

## Repository Architecture

```
google-publisher-tag/
├── SKILL.md                 # Mode 1: Agent Skill entry point & router
├── okf/                     # Mode 2: Open Knowledge Format (OKF v0.1) bundle
│   ├── index.md             # Root progressive disclosure index (okf_version: "0.1")
│   ├── log.md               # Chronological update log (ISO 8601)
│   ├── guides/              # 16 OKF concepts for guides
│   ├── samples/             # 24 OKF concepts + runnable JS/TS code
│   └── support/             # Browser support & developer feedback concepts
├── docs/                    # Official live mirror (byte-identical)
│   ├── README.md            # Upstream mirror structure & guidelines
│   ├── reference.md         # Full TypeScript API reference (8,200+ lines)
│   ├── guides/              # 16 official guides
│   ├── samples/             # 24 sample guides with runnable code
│   ├── support/             # Browser support & feedback
│   └── scripts/             # refetch.sh & check-links.sh
└── scripts/
    └── build-okf.py         # Automated OKF bundle generator from docs/
```

---

## Mode 1: Agent Skill (`SKILL.md`)

Designed for AI coding agents such as Claude Code, Cursor, Windsurf, Oh My Pi, and Herdr.

### Skill Highlights:
- **Task Routing Table**: Directs agent attention to exact guides and samples based on developer intent (e.g., lazy loading, responsive sizing, CLS mitigation, interstitial ads) without context window bloat.
- **Core GPT Guardrails**: Enforces critical rules:
  1. Asynchronous command queue: `window.googletag = window.googletag || { cmd: [] }; googletag.cmd.push(...)`
  2. Execution order: Page Settings $\rightarrow$ Define Slots $\rightarrow$ `enableServices()` $\rightarrow$ `display()`
  3. API readiness check via `googletag.apiReady` (never `typeof googletag !== 'undefined'`)
  4. Anti-CLS slot space reservation prior to rendering

### Installing the Skill (Zero Project Pollution)

The documentation and samples are **permanently attached to the skill**. Projects using this skill remain 100% clean and never need a `docs/` folder.

**Global installation (recommended for agents across all your projects):**
```bash
# Option A: Clone directly into your agent skills directory
git clone https://github.com/ilhamgusti/google-publisher-tag-skill.git ~/.agents/skills/google-publisher-tag

# Option B: If cloned locally, symlink the repository
ln -s "$(pwd)" ~/.agents/skills/google-publisher-tag
```

Once installed, your AI agent automatically accesses GPT documentation, TypeScript definitions, and code samples internally without polluting your project workspace.

---

## Mode 2: Open Knowledge Format Bundle (`okf/`)

Designed for agent wikis, vector search, and organizational knowledge engines conforming to the [Open Knowledge Format (OKF v0.1)](https://github.com/fabricioctelles/skills) specification.

### Bundle Highlights:
- **100% OKF v0.1 Conformance**: Verified with zero errors and zero warnings:
  ```bash
  validate.sh okf/
  # Files scanned: 53
  # ✅ Bundle is OKF v0.1 conformant
  ```
- **53 Concept Documents**: Every markdown concept contains structured YAML frontmatter:
  - `type`: `Guide`, `API Reference`, `Sample`, `Troubleshooting`, `Best Practice`, `Support`
  - `title`: Human-readable display name
  - `description`: Single-sentence summary
  - `resource`: Canonical Google Developers URL
  - `tags`: Domain taxonomy tags
  - `timestamp`: ISO 8601 timestamp
- **Progressive Disclosure**: Sub-index directories at `okf/guides/index.md`, `okf/samples/index.md`, and `okf/support/index.md`.
- **Runnable Code**: Preserved alongside sample concepts (`js/demo.html`, `ts/index.html`, `ts/sample.ts`).

### Validating Conformance:
```bash
# Using the OKF validator script
bash path/to/validate.sh okf/

# Or using okflint (if installed)
okflint validate okf/
```

---

## Upstream Synchronization Pipeline

The `docs/` directory is deliberately kept **100% byte-identical** to Google Developers source endpoints (`.md.txt` and `googleads/google-publisher-tag-samples`). This ensures all automated updates are **clean cutovers** without merge conflicts.

### Sync Workflow:

```bash
# 1. Check if upstream Atom feed has newer releases
./docs/scripts/refetch.sh --check

# 2. Inspect release note entries published since last sync
./docs/scripts/refetch.sh --diff

# 3. Pull latest documentation and samples
./docs/scripts/refetch.sh

# 4. Verify relative link integrity
./docs/scripts/check-links.sh
```

### Automated Rebuild Hook:
`./docs/scripts/refetch.sh` automatically invokes `scripts/build-okf.py` upon completing a successful fetch, ensuring the OKF bundle stays up to date without manual intervention.

To trigger the OKF generator manually:
```bash
python3 scripts/build-okf.py
```

---

## License
- Documentation Content: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) by Google LLC.
- Sample Code: [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0).
