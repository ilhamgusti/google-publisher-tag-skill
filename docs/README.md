# Google Publisher Tag (GPT) — Docs Mirror

Mirror lokal dari dokumentasi resmi [Google Publisher Tag](https://developers.google.com/publisher-tag).
Setiap file adalah salinan markdown (`.md.txt`) dari halaman resmi, plus kode sumber aktual untuk setiap sample.

**Sumber:** https://developers.google.com/publisher-tag
**License:** Konten — [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); kode — [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0).

Struktur mengikuti 5 tab resmi di sidebar: **Guides · Reference · Samples · Sample builder · Support**.

---

## Guides (`guides/`)

### Get started

- [get-started.md](guides/get-started.md) — Mulai cepat: tampilkan test ad
- [learn-basics.md](guides/learn-basics.md) — Konsep dasar GPT
- [use-typescript.md](guides/use-typescript.md) — Pakai GPT dengan TypeScript

### Basic concepts

- [ad-sizes.md](guides/ad-sizes.md) — Ukuran iklan (fixed, fluid, responsive)
- [key-value-targeting.md](guides/key-value-targeting.md) — Key-value targeting

### Advanced concepts

- [control-ad-loading.md](guides/control-ad-loading.md) — Kontrol loading & refresh iklan
- [passback-tags.md](guides/passback-tags.md) — Passback tags

### Security and privacy

- [cross-origin-embedder-policy.md](guides/cross-origin-embedder-policy.md) — Integrasi COEP
- [content-security-policy.md](guides/content-security-policy.md) — Integrasi CSP

### Troubleshooting

- [publisher-console.md](guides/publisher-console.md) — Publisher Console
- [publisher-console-messages.md](guides/publisher-console-messages.md) — Daftar pesan Publisher Console

### Best practices

- [general-best-practices.md](guides/general-best-practices.md) — Best practice umum
- [ad-best-practices.md](guides/ad-best-practices.md) — Best practice iklan
- [minimize-layout-shift.md](guides/minimize-layout-shift.md) — Minimalkan layout shift (CLS)
- [monitor-performance.md](guides/monitor-performance.md) — Monitoring performa
- [common-implementation-mistakes.md](common-implementation-mistakes.md) — Kesalahan implementasi umum

---

## Reference

Halaman dari tab **Reference** ([/publisher-tag/reference](https://developers.google.com/publisher-tag/reference)).

- [reference.md](reference.md) — Referensi TypeScript lengkap `googletag.*` (8200+ baris)
- [config-migration.md](guides/config-migration.md) — Migrasi ke `setConfig()`
- [release-notes.md](release-notes.md) — Riwayat rilis produksi
- [versions.md](versions.md) — Tabel riwayat versi GPT
- [adsense-attributes.md](adsense-attributes.md) — Atribut AdSense

---

## Samples (`samples/`)

Setiap file berisi deskripsi + **kode lengkap** (JavaScript, JavaScript legacy, TypeScript) bersumber dari [googleads/google-publisher-tag-samples](https://github.com/googleads/google-publisher-tag-samples).

### Beginner

- [basic-concepts.md](samples/basic-concepts.md)
- [display-test-ad.md](samples/display-test-ad.md)
- [refresh.md](samples/refresh.md)

### Advanced

- [control-sra-batching.md](samples/control-sra-batching.md) — kontrol SRA batching
- [infinite-content.md](samples/infinite-content.md) — lazy loading untuk infinite scroll
- [lazy-loading.md](samples/lazy-loading.md)
- [event-based-requests.md](samples/event-based-requests.md) — request berbasis event
- [shadow-dom.md](samples/shadow-dom.md)

### Ad formats

- [display-anchor-ad.md](samples/display-anchor-ad.md) — anchor (top/bottom)
- [display-side-rail-ad.md](samples/display-side-rail-ad.md) — side rail (kiri/kanan)
- [display-out-of-page-ad.md](samples/display-out-of-page-ad.md)
- [display-web-interstitial-ad.md](samples/display-web-interstitial-ad.md)
- [display-gaming-interstitial-ad.md](samples/display-gaming-interstitial-ad.md)
- [display-rewarded-ad.md](samples/display-rewarded-ad.md) — rewarded ad
- [offerwall-custom-choice.md](samples/offerwall-custom-choice.md) — offerwall

### Targeting & behavior

- [key-value-targeting.md](samples/key-value-targeting.md)
- [ad-sizes.md](samples/ad-sizes.md) — fixed/fluid/responsive
- [collapse-empty-ad-slots.md](samples/collapse-empty-ad-slots.md)
- [reserve-space.md](samples/reserve-space.md) — reserve space untuk anti-CLS
- [ad-event-listeners.md](samples/ad-event-listeners.md)

### Privacy

- [configure-privacy.md](samples/configure-privacy.md) — CCPA/GDPR
- [display-limited-ad.md](samples/display-limited-ad.md) — limited ads

### Integrations

- [integrations/react.md](samples/integrations/react.md) — GPT + React/Next.js (StackBlitz)

---

## Sample builder

- [sample-builder.md](sample-builder.md) — Tool interaktif untuk merakit sample kustom (beta)

---

## Support (`support/`)

- [feedback-questions.md](support/feedback-questions.md) — opsi support
- [browser-support.md](support/browser-support.md) — browser yang didukung
- [related.md](related.md) — peta relasi Guide ↔ Sample (navigasi silang)

---

## Catatan konversi

- File `.md` di-_mirror_ dari endpoint resmi `…/<path>.md.txt`.
- Setiap sample juga punya **kode runnable** di `samples/<name>/{js,legacyjs,ts}/` (struktur mirror GitHub) — buka `samples/<name>/js/demo.html` di browser untuk lihat sample jalan. Dir ini di-sync `refetch.sh` bersamaan dengan `.md`.
- Halaman **samples** di situs resmi me-render kode di dalam `<iframe>` (JS-loaded), sehingga `.md.txt`-nya hanya berisi deskripsi + placeholder `Loading...`. Di repo ini, kode aktual (`js/demo.html`, `legacyjs/demo.html`, `ts/index.html`, `ts/sample.ts`) diambil dari repo GitHub resmi dan ditanam langsung ke setiap file sample — sehingga self-contained.
- Sample `integrations/react` adalah project Next.js penuh (bukan single-file), kode-nya ada di [StackBlitz](https://stackblitz.com/edit/gpt-react); file ini hanya menyimpan deskripsi + link.
- `reference.md` (8200+ baris) berisi seluruh API surface GPT (`googletag`, namespaces, interfaces, enums, events, secureSignals).
- File mirror sengaja dibuat **byte-identik dengan sumber** — tanpa catatan/link tambahan inline — supaya refetch adalah clean cutover.

---

## Update ulang

Sinkronisasi otomatis via [`scripts/refetch.sh`](scripts/refetch.sh), didorong oleh
[feed Atom release-notes resmi](https://developers.google.com/static/publisher-tag/feeds/release-notes-atom.xml).
Script hanya me-refetch saat Google merilis update baru — file mirror tetap identik dengan sumber.
> Verifikasi integritas link: `./scripts/check-links.sh` (cek semua relative link di README + related resolve ke file).

```bash
./scripts/refetch.sh --check    # cek feed saja, tanpa fetch
./scripts/refetch.sh            # refetch hanya jika feed maju (default)
./scripts/refetch.sh --diff     # tampilkan entri rilis baru sejak sync terakhir
./scripts/refetch.sh --force    # refetch paksa semua halaman + kode sample
```

State sync disimpan di `.cache/` (`feed-updated`, `feed-atom.xml`). Inventory URL dideklarasikan di array `GUIDES` / `TOPLEVEL` / `SAMPLES` / `SUPPORT` di dalam script — tambah/hapus halaman di sana.

> Tip: idempoten dan aman dijadwalkan via cron harian.
