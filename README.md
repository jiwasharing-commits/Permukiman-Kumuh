# Permukiman-Kumuh
Penanganan Kawasan Kumuh.

## Starter Pack (MVP)
Repository ini sekarang berisi rancangan awal untuk web data kawasan kumuh:

- `docs/struktur-data.md` untuk struktur tabel, index, dan SQL draft.
- `data/contoh_kawasan_kumuh.csv` untuk contoh format impor data.
- `web/index.html` untuk contoh tampilan dashboard dan tabel.

Langkah berikutnya:
1. Implement backend (Laravel/Node) dan koneksi database.
2. Tambahkan fitur import CSV/XLSX.
3. Tambahkan pagination + filter server-side untuk 600+ data.
4. Integrasikan peta interaktif (Leaflet/OpenStreetMap).


## Data Kewenangan (Input Lapangan)
- `data/lokasi_kewenangan_kabupaten.csv` berisi dataset awal dari format yang Anda kirim (RT/RW, Kampung, Desa, Kecamatan, Luas, Kewenangan, Bobot Kumuh).
- `docs/format-data-kewenangan.md` berisi standar format dan catatan pembersihan data.
