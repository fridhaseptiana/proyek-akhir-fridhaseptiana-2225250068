# TEST CASE
## Program Pengolahan dan Analisis Data Nilai Mahasiswa

**Nama:** Fridha Septiana  
**NIM:** 2225250068  
**Kelas:** 3E

## 1. Tujuan Pengujian

Pengujian dilakukan untuk memastikan program dapat membaca, mengolah, dan menganalisis data nilai mahasiswa dengan benar serta mampu menangani kesalahan pada data.

## 2. Daftar Test Case

| No. | Pengujian | Input | Hasil yang Diharapkan |
|---|---|---|---|
| 1 | Membaca data mahasiswa | File berisi 10 data valid | Seluruh data berhasil dibaca |
| 2 | Menghitung rata-rata | Nilai 85, 90, 80, 75, 65, 95, 55, 70, 88, 60 | Rata-rata 76,30 |
| 3 | Nilai tertinggi | Data nilai mahasiswa | Nilai tertinggi 95 |
| 4 | Nilai terendah | Data nilai mahasiswa | Nilai terendah 55 |
| 5 | Menghitung kelulusan | Nilai minimal 60 | 9 mahasiswa lulus dan 1 tidak lulus |
| 6 | Nilai di luar rentang | Nilai 120 | Data dilewati |
| 7 | Nilai negatif | Nilai -10 | Data dilewati |
| 8 | Nilai berupa huruf | Nilai abc | Data dilewati |
| 9 | Data tidak lengkap | Data tanpa nilai | Data dilewati |
| 10 | File tidak ditemukan | File tidak tersedia | Menampilkan pesan kesalahan |

## 3. Hasil Pengujian

Pengujian dilakukan dengan menjalankan program menggunakan perintah:

```bash
python src/main.py
```

Program diharapkan dapat menampilkan data mahasiswa, hasil perhitungan rata-rata, nilai tertinggi, nilai terendah, serta jumlah mahasiswa yang lulus dan tidak lulus.

## 4. Kesimpulan

Berdasarkan rancangan pengujian, program diharapkan mampu mengolah data nilai mahasiswa dengan benar. Program juga dilengkapi validasi data dan penanganan kesalahan agar data yang tidak sesuai tidak ikut diproses dalam analisis.

