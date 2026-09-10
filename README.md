# Google Publisher Tag (GPT) — Documentation Mirror, Agent Skill & OKF Bundle

Repositori komprehensif dokumentasi resmi [Google Publisher Tag (GPT)](https://developers.google.com/publisher-tag), dikemas dalam **dua mode konsumsi untuk AI coding agents**:
1. **Agent Skill (`SKILL.md`)** — Format standar open agent skills dengan task routing dan panduan anti-pitfalls.
2. **Open Knowledge Format Bundle (`okf/`)** — Format terbuka OKF v0.1 dengan YAML frontmatter pada setiap konsep untuk LLM semantic search / wiki ingestion.

Serta mempertahankan **Live Mirror (`docs/`)** yang byte-identik dengan upstream Google Developers.

---

## Arsitektur Repositori

```
google-publisher-tag/
├── SKILL.md                 # Mode 1: Agent Skill entry point & router
├── okf/                     # Mode 2: Open Knowledge Format (OKF v0.1) bundle
│   ├── index.md             # Bundle root index (okf_version: "0.1")
│   ├── log.md               # Chronological update log (ISO 8601)
│   ├── guides/              # 16 OKF concepts untuk guides
│   ├── samples/             # 20+ OKF concepts + runnable code JS/TS
│   └── support/             # OKF concepts browser & support
├── docs/                    # Live mirror resmi (byte-identik)
│   ├── README.md            # Dokumentasi struktur mirror
│   ├── reference.md         # Full TypeScript API reference (8200+ baris)
│   ├── guides/              # 16 official guides
│   ├── samples/             # 20+ runnable samples
│   ├── support/             # Browser support & feedback
│   └── scripts/             # refetch.sh & check-links.sh
└── scripts/
    └── build-okf.py         # Generator OKF bundle dari docs/
```

---

## Mode 1: Agent Skill (`SKILL.md`)

Dirancang untuk AI coding agents (Claude Code, Cursor, Windsurf, Oh My Pi, Herdr).

### Fitur Skill:
- **Task Routing Table**: Memetakan intent developer (misal "setup lazy loading", "anti CLS", "interstitial ad") ke file panduan dan sampel kode yang tepat tanpa membuang context window.
- **Critical GPT Invariants**: Rule guardrails yang harus dipatuhi AI agent:
  1. Queue pattern (`window.googletag = window.googletag || { cmd: [] }; googletag.cmd.push(...)`)
  2. Urutan eksekusi: Page Settings $\rightarrow$ Define Slots $\rightarrow$ `enableServices()` $\rightarrow$ `display()`
  3. Pengecekan API ready via `googletag.apiReady`, bukan `typeof googletag !== 'undefined'`
  4. Anti-CLS space reservation sebelum display

### Instalasi Skill (Global):
```bash
mkdir -p ~/.agents/skills/google-publisher-tag
cp SKILL.md ~/.agents/skills/google-publisher-tag/
```
Atau symlink repository ini ke `~/.agents/skills/google-publisher-tag`.

---

## Mode 2: Open Knowledge Format Bundle (`okf/`)

Dirancang untuk agent wiki / semantic knowledge engine berstandar [Open Knowledge Format (OKF v0.1)](https://github.com/fabricioctelles/skills).

### Fitur OKF Bundle:
- **100% Conformance OKF v0.1**: Lolos validasi `okflint` dan `validate.sh` tanpa error maupun warning.
- **75 Dokumen Konsep**: Setiap `.md` memiliki YAML frontmatter:
  - `type`: `Guide`, `API Reference`, `Sample`, `Troubleshooting`, `Best Practice`, `Support`
  - `title`: Judul deskriptif manusiawi
  - `description`: Ringkasan satu kalimat
  - `resource`: URL resmi dokumentasi Google
  - `tags`: Tag kategorisasi untuk indexing semantik
  - `timestamp`: ISO 8601
- **Progressive Disclosure**: Sub-index di `okf/guides/index.md`, `okf/samples/index.md`, dan `okf/support/index.md`.
- **Runnable Code**: Disertakan langsung di samping setiap konsep sampel (`js/demo.html`, `ts/index.html`, `ts/sample.ts`).

### Validasi Bundle:
```bash
# Validasi via OKF validator script
bash path/to/validate.sh okf/

# Atau via okflint (jika terinstall)
okflint validate okf/
```

---

## Live Mirror (`docs/`) & Upstream Sync

Folder `docs/` sengaja dijaga **100% byte-identik** dengan endpoint upstream Google Developers (`.md.txt` dan repo GitHub `google-publisher-tag-samples`), sehingga sinkronisasi selalu berupa **clean cutover** tanpa konflik modifikasi manual.

### Sinkronisasi Otomatis:
```bash
# 1. Cek apakah ada update baru di release notes Atom feed
./docs/scripts/refetch.sh --check

# 2. Refetch jika ada rilis baru (atau gunakan --force untuk paksa)
./docs/scripts/refetch.sh

# 3. Validasi keutuhan relative link docs
./docs/scripts/check-links.sh

# 4. Rebuild bundle OKF agar selalu mutakhir
python3 scripts/build-okf.py
```

---

## Lisensi
- Konten Dokumentasi: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) oleh Google LLC.
- Kode Sampel: [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0).
