
def baca_data(nama_file):
    data_mahasiswa = []

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            next(file)

            for baris in file:
                baris = baris.strip()

                if not baris:
                    continue

                bagian = baris.split(",")

                if len(bagian) != 3:
                    print(f"Data tidak lengkap, dilewati: {baris}")
                    continue

                try:
                    nim = bagian[0].strip()
                    nama = bagian[1].strip()
                    nilai = float(bagian[2].strip())

                    if not nim or not nama:
                        print(f"Identitas tidak lengkap, dilewati: {baris}")
                        continue

                    if nilai < 0 or nilai > 100:
                        print(f"Nilai tidak valid, dilewati: {baris}")
                        continue

                    mahasiswa = {
                        "nim": nim,
                        "nama": nama,
                        "nilai": nilai
                    }

                    data_mahasiswa.append(mahasiswa)

                except ValueError:
                    print(f"Nilai harus berupa angka, dilewati: {baris}")

    except FileNotFoundError:
        print("Error: File data tidak ditemukan.")

    except OSError:
        print("Error: File tidak dapat dibaca.")

    return data_mahasiswa
