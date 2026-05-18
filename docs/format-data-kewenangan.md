# Format Data Kewenangan Kawasan Kumuh

Dokumen ini mengikuti format data yang Anda kirim:

- RT/RW
- Kampung
- Desa
- Kecamatan
- Luas (Ha)
- Kewenangan (`KAB/KOTA`, `PROVINSI`, `PUSAT`)
- Bobot Kumuh

## Header CSV Standar

```csv
rt_rw,kampung,desa,kecamatan,luas_ha,kewenangan,bobot_kumuh
```

## Catatan kualitas data

- Gunakan titik (`.`) sebagai pemisah desimal untuk `luas_ha`.
- Konsistenkan penulisan kampung (mis. `KP.`) agar mudah difilter.
- Simpan `rt_rw` sebagai teks karena bisa mengandung huruf (mis. `RT06A-RW002`).
- Jika ada data duplikat dari sumber gabungan, lakukan deduplikasi berdasarkan kombinasi `rt_rw+kampung+desa+kecamatan`.
