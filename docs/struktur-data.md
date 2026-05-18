# Rancangan Data Kawasan Kumuh

Dokumen ini menyiapkan struktur data awal untuk aplikasi web pemetaan dan manajemen kawasan kumuh.

## 1) Struktur Tabel Utama

Nama tabel: `kawasan_kumuh`

| Kolom | Tipe Data | Aturan | Keterangan |
|---|---|---|---|
| id | BIGINT UNSIGNED | PK, AUTO_INCREMENT | ID unik data |
| kode_kawasan | VARCHAR(30) | UNIQUE, NOT NULL | Kode referensi kawasan |
| nama_kawasan | VARCHAR(200) | NOT NULL | Nama kawasan kumuh |
| alamat | TEXT | NULL | Alamat rinci |
| kelurahan | VARCHAR(120) | NOT NULL | Kelurahan |
| kecamatan | VARCHAR(120) | NOT NULL | Kecamatan |
| kabupaten_kota | VARCHAR(120) | NOT NULL | Kabupaten/Kota |
| luas_ha | DECIMAL(10,2) | NOT NULL, DEFAULT 0 | Luas dalam hektar |
| tingkat_kumuh | ENUM('Ringan','Sedang','Berat') | NOT NULL | Kategori tingkat kumuh |
| jumlah_bangunan | INT UNSIGNED | NULL | Total bangunan terdampak |
| jumlah_kk | INT UNSIGNED | NULL | Total KK terdampak |
| latitude | DECIMAL(10,7) | NULL | Titik lintang |
| longitude | DECIMAL(10,7) | NULL | Titik bujur |
| tahun_penetapan | YEAR | NULL | Tahun penetapan kawasan |
| status_penanganan | ENUM('Belum','Proses','Selesai') | NOT NULL, DEFAULT 'Belum' | Status program |
| keterangan | TEXT | NULL | Catatan tambahan |
| created_at | TIMESTAMP | NOT NULL | Waktu dibuat |
| updated_at | TIMESTAMP | NOT NULL | Waktu diperbarui |

## 2) Index yang Disarankan

- `INDEX idx_nama_kawasan (nama_kawasan)`
- `INDEX idx_wilayah (kecamatan, kelurahan)`
- `INDEX idx_tingkat_kumuh (tingkat_kumuh)`
- `INDEX idx_status_penanganan (status_penanganan)`

## 3) SQL Draft (MySQL)

```sql
CREATE TABLE kawasan_kumuh (
  id BIGINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
  kode_kawasan VARCHAR(30) NOT NULL UNIQUE,
  nama_kawasan VARCHAR(200) NOT NULL,
  alamat TEXT NULL,
  kelurahan VARCHAR(120) NOT NULL,
  kecamatan VARCHAR(120) NOT NULL,
  kabupaten_kota VARCHAR(120) NOT NULL,
  luas_ha DECIMAL(10,2) NOT NULL DEFAULT 0,
  tingkat_kumuh ENUM('Ringan','Sedang','Berat') NOT NULL,
  jumlah_bangunan INT UNSIGNED NULL,
  jumlah_kk INT UNSIGNED NULL,
  latitude DECIMAL(10,7) NULL,
  longitude DECIMAL(10,7) NULL,
  tahun_penetapan YEAR NULL,
  status_penanganan ENUM('Belum','Proses','Selesai') NOT NULL DEFAULT 'Belum',
  keterangan TEXT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
```

## 4) Catatan Implementasi untuk 600+ Data

- Gunakan pagination server-side (10/25/50 data per halaman).
- Aktifkan filter berdasarkan kecamatan, tingkat_kumuh, dan status_penanganan.
- Sediakan import CSV/XLSX untuk upload massal.
- Validasi duplikasi berdasarkan `kode_kawasan` dan kombinasi nama+wilayah.
