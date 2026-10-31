
import os

from data_io import baca_data
from analisis import (
    hitung_rata_rata,
    cari_nilai_tertinggi,
    cari_nilai_terendah,
    hitung_kelulusan
)
from utilitas import (
    tampilkan_judul,
    tampilkan_data,
    tampilkan_hasil_analisis
)


def main():
    tampilkan_judul()

    lokasi_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    nama_file = os.path.join(lokasi_folder, "data", "nilai_contoh.txt")

    data = baca_data(nama_file)

    if not data:
        print("\nTidak ada data mahasiswa yang dapat dianalisis.")
        return

    tampilkan_data(data)

    rata_rata = hitung_rata_rata(data)
    tertinggi = cari_nilai_tertinggi(data)
    terendah = cari_nilai_terendah(data)

    jumlah_lulus, jumlah_tidak_lulus = hitung_kelulusan(data)

    tampilkan_hasil_analisis(
        data,
        rata_rata,
        tertinggi,
        terendah,
        jumlah_lulus,
        jumlah_tidak_lulus
    )


if __name__ == "__main__":
    main()
