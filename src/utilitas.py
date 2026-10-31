
def tampilkan_judul():
    print("=" * 50)
    print("       PROGRAM ANALISIS NILAI MAHASISWA")
    print("=" * 50)


def tampilkan_data(data):
    print("\nDAFTAR NILAI MAHASISWA")
    print("-" * 65)
    print(f"{'NIM':<12} {'NAMA':<25} {'NILAI':<10} {'STATUS'}")
    print("-" * 65)

    for mahasiswa in data:
        if mahasiswa["nilai"] >= 60:
            status = "Lulus"
        else:
            status = "Tidak Lulus"

        print(
            f"{mahasiswa['nim']:<12} "
            f"{mahasiswa['nama']:<25} "
            f"{mahasiswa['nilai']:<10.2f} "
            f"{status}"
        )

    print("-" * 65)


def tampilkan_hasil_analisis(data, rata_rata, tertinggi, terendah,
                              jumlah_lulus, jumlah_tidak_lulus):
    print("\nHASIL ANALISIS NILAI MAHASISWA")
    print("-" * 40)
    print(f"Jumlah mahasiswa       : {len(data)}")
    print(f"Nilai rata-rata        : {rata_rata:.2f}")

    if tertinggi is not None:
        print(f"Nilai tertinggi        : {tertinggi['nilai']:.2f}")
        print(f"Mahasiswa              : {tertinggi['nama']}")

    if terendah is not None:
        print(f"Nilai terendah         : {terendah['nilai']:.2f}")
        print(f"Mahasiswa              : {terendah['nama']}")

    print(f"Jumlah mahasiswa lulus : {jumlah_lulus}")
    print(f"Jumlah tidak lulus     : {jumlah_tidak_lulus}")
    print("-" * 40)
