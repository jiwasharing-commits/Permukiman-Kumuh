# Permukiman-Kumuh
Penanganan Kawasan Kumuh.

## Starter Pack (MVP)
Repository ini berisi rancangan awal untuk web data kawasan kumuh:

- `docs/struktur-data.md` untuk struktur tabel, index, dan SQL draft.
- `data/sumber_data_baru.csv` sebagai satu-satunya file data utama yang dipakai web demo.
- `web/index.html` untuk contoh tampilan dashboard dan tabel.

Langkah berikutnya:
1. Implement backend (Laravel/Node) dan koneksi database.
2. Tambahkan fitur import CSV/XLSX.
3. Tambahkan pagination + filter server-side untuk 600+ data.
4. Integrasikan peta interaktif (Leaflet/OpenStreetMap).


## Data Kewenangan (Input Lapangan)
- `data/sumber_data_baru.csv` berisi dataset aktif dari format yang Anda kirim (RT/RW, Kampung, Desa, Kecamatan, Luas, Kewenangan, Bobot Kumuh).
- `docs/format-data-kewenangan.md` berisi standar format dan catatan pembersihan data.


## Menjalankan Web Demo
- Karena browser biasanya memblokir `fetch` file lokal, jalankan web via local server:
- `cd web && python3 -m http.server 8000`
- Buka: `http://localhost:8000`

- Tabel langsung tampil saat halaman dibuka (tanpa login), dengan fitur pencarian, filter, pagination, dan reload data.


## Validasi Jumlah Data
- Jalankan: `./scripts/validate_kawasan_csv.py`
- Script membaca `data/sumber_data_baru.csv`, memvalidasi header tanpa mengubah isi CSV, lalu menampilkan total baris dan total data unik.
- Target validasi: `602` data unik.
