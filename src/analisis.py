
def hitung_rata_rata(data):
    if not data:
        return 0

    total = sum(mahasiswa["nilai"] for mahasiswa in data)
    rata_rata = total / len(data)

    return rata_rata


def cari_nilai_tertinggi(data):
    if not data:
        return None

    return max(data, key=lambda mahasiswa: mahasiswa["nilai"])


def cari_nilai_terendah(data):
    if not data:
        return None

    return min(data, key=lambda mahasiswa: mahasiswa["nilai"])


def hitung_kelulusan(data):
    jumlah_lulus = 0
    jumlah_tidak_lulus = 0

    for mahasiswa in data:
        if mahasiswa["nilai"] >= 60:
            jumlah_lulus += 1
        else:
            jumlah_tidak_lulus += 1

    return jumlah_lulus, jumlah_tidak_lulus
