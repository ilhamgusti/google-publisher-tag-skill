# Cross-reference: Guide ↔ Sample

Peta relasi antara halaman **Guide** dan **Sample** yang relevan secara topik.
File ini _sidecar_ — tidak ikut ditimpa oleh `scripts/refetch.sh`, jadi aman dirawat manual.

> Lihat juga: [README](README.md) untuk indeks lengkap semua halaman.

## Guide → Sample

| Guide | Sample terkait |
|---|---|
| [get-started](guides/get-started.md) | [display-test-ad](samples/display-test-ad.md), [basic-concepts](samples/basic-concepts.md) |
| [learn-basics](guides/learn-basics.md) | [basic-concepts](samples/basic-concepts.md) |
| [ad-sizes](guides/ad-sizes.md) | [ad-sizes](samples/ad-sizes.md) |
| [key-value-targeting](guides/key-value-targeting.md) | [key-value-targeting](samples/key-value-targeting.md) |
| [control-ad-loading](guides/control-ad-loading.md) | [control-sra-batching](samples/control-sra-batching.md), [event-based-requests](samples/event-based-requests.md), [refresh](samples/refresh.md) |
| [minimize-layout-shift](guides/minimize-layout-shift.md) | [reserve-space](samples/reserve-space.md) |
| [publisher-console](guides/publisher-console.md) | [ad-event-listeners](samples/ad-event-listeners.md) |

## Sample → Guide

| Sample | Guide terkait |
|---|---|
| [display-test-ad](samples/display-test-ad.md) | [get-started](guides/get-started.md) |
| [basic-concepts](samples/basic-concepts.md) | [get-started](guides/get-started.md), [learn-basics](guides/learn-basics.md) |
| [ad-sizes](samples/ad-sizes.md) | [ad-sizes](guides/ad-sizes.md) |
| [key-value-targeting](samples/key-value-targeting.md) | [key-value-targeting](guides/key-value-targeting.md) |
| [control-sra-batching](samples/control-sra-batching.md) | [control-ad-loading](guides/control-ad-loading.md) |
| [event-based-requests](samples/event-based-requests.md) | [control-ad-loading](guides/control-ad-loading.md) |
| [refresh](samples/refresh.md) | [control-ad-loading](guides/control-ad-loading.md) |
| [reserve-space](samples/reserve-space.md) | [minimize-layout-shift](guides/minimize-layout-shift.md) |
| [ad-event-listeners](samples/ad-event-listeners.md) | [publisher-console](guides/publisher-console.md) |

---

## Konvensi perawatan

- Saat menambah guide/sample baru, daftarkan relasinya di kedua tabel di atas.
- File mirror (`guides/*.md`, `samples/*.md`) **tidak** berisi link silang inline — agar `refetch.sh` adalah clean cutover.
- Jika ingin navigasi inline, lakukan sebagai langkah terpisah pasca-sync (lihat TODO di bawah).

## TODO (opsional, pasca-refetch)

Script untuk menyuntik kembali link inline setelah sync bisa ditambahkan di `scripts/inject-crossrefs.sh`
(membaca tabel di atas, menyisipkan `> Guide terkait:` di sample & `## Terkait` di guide).
Saat ini dinonaktifkan demi kesederhanaan — README + file ini sudah cukup untuk navigasi.
