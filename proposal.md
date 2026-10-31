# PROPOSAL PROYEK AKHIR

## Program Pengolahan dan Analisis Data Nilai Mahasiswa

**Nama:** Fridha Septiana  
**NIM:** 2225250068  
**Kelas:** 3E

## 1. Latar Belakang

Dalam kegiatan pembelajaran, pengolahan nilai mahasiswa merupakan salah satu kegiatan yang penting untuk mengetahui hasil belajar. Data nilai mahasiswa perlu dikelola dan dianalisis agar dapat memberikan informasi mengenai perkembangan hasil belajar.

Pengolahan data nilai secara manual membutuhkan waktu dan ketelitian, terutama jika jumlah data mahasiswa cukup banyak. Oleh karena itu, diperlukan sebuah program sederhana yang dapat membantu proses pengolahan dan analisis data nilai mahasiswa secara lebih cepat dan terstruktur.

Program ini dibuat menggunakan bahasa pemrograman Python dengan menerapkan konsep pembacaan file, struktur data, fungsi, serta penanganan kesalahan.

## 2. Tujuan Proyek

1. Membuat program untuk mengolah data nilai mahasiswa.
2. Menerapkan penggunaan list dan dictionary dalam penyimpanan data.
3. Menerapkan fungsi untuk mengelola proses program.
4. Membaca data mahasiswa dari file teks.
5. Menghitung rata-rata, nilai tertinggi, dan nilai terendah.
6. Menentukan jumlah mahasiswa yang lulus dan tidak lulus.
7. Menerapkan penanganan kesalahan pada proses pengolahan data.

## 3. Manfaat Proyek

1. Mempermudah proses pengolahan data nilai mahasiswa.
2. Membantu memperoleh informasi hasil belajar mahasiswa.
3. Mengurangi kesalahan dalam perhitungan nilai.
4. Meningkatkan pemahaman mengenai penerapan bahasa pemrograman Python.

## 4. Batasan Masalah

Program ini memiliki beberapa batasan, yaitu:

1. Data yang diolah berupa identitas dan nilai mahasiswa.
2. Data dibaca dari file teks bernama `nilai_contoh.txt`.
3. Nilai mahasiswa berada pada rentang 0 sampai 100.
4. Program menghitung rata-rata, nilai tertinggi, dan nilai terendah.
5. Kriteria kelulusan ditentukan berdasarkan nilai minimal 60.
6. Program dijalankan melalui terminal menggunakan Python.

## 5. Rancangan Input, Process, dan Output

### A. Input

Data yang dimasukkan berupa:
- NIM mahasiswa.
- Nama mahasiswa.
- Nilai mahasiswa.

Data disimpan dalam file `data/nilai_contoh.txt`.

### B. Process

Proses yang dilakukan program meliputi:
1. Membaca data dari file.
2. Memeriksa dan memvalidasi data.
3. Menyimpan data mahasiswa ke dalam struktur data.
4. Menghitung nilai rata-rata.
5. Menentukan nilai tertinggi dan terendah.
6. Menghitung jumlah mahasiswa yang lulus dan tidak lulus.

### C. Output

Program menghasilkan informasi berupa:
- Daftar data mahasiswa.
- Jumlah mahasiswa.
- Nilai rata-rata.
- Nilai tertinggi.
- Nilai terendah.
- Jumlah mahasiswa yang lulus.
- Jumlah mahasiswa yang tidak lulus.

## 6. Rancangan Fungsi Program

Program dibagi menjadi beberapa file agar lebih terstruktur.

1. `main.py`: menjalankan program utama.
2. `data_io.py`: membaca dan mengelola data dari file.
3. `analisis.py`: melakukan perhitungan dan analisis nilai mahasiswa.
4. `utilitas.py`: menyediakan fungsi pendukung program.

## 7. Rencana Pengujian

Pengujian dilakukan dengan beberapa kondisi, yaitu:

1. Menguji pembacaan data mahasiswa yang valid.
2. Menguji perhitungan nilai rata-rata.
3. Menguji penentuan nilai tertinggi dan terendah.
4. Menguji penentuan status kelulusan.
5. Menguji data dengan nilai di luar rentang 0 sampai 100.
6. Menguji data yang tidak lengkap.
7. Menguji kondisi file tidak ditemukan.

## 8. Hasil yang Diharapkan

Program diharapkan dapat membaca, mengolah, dan menganalisis data nilai mahasiswa dengan benar. Selain itu, program mampu menangani data yang tidak valid sehingga proses pengolahan data dapat berjalan dengan lebih terstruktur dan mudah dipahami.

## 9. Kesimpulan

Pembuatan program pengolahan dan analisis data nilai mahasiswa merupakan penerapan konsep dasar pemrograman Python dalam menyelesaikan permasalahan sederhana. Melalui proyek ini, penggunaan file, struktur data, fungsi, analisis data, dan error handling dapat diterapkan secara langsung.
