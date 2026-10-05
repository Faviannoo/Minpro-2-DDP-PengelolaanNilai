import os
from prettytable import PrettyTable
import pwinput

# DATA MAHASISWA
data_mahasiswa = []

# FUNCTION MEMBERSIHKAN LAYAR
def bersihkan_layar():
    os.system("cls")

# DATA AKUN
akun = {
    "dosen": {
        "password": "dosen123",
        "role": "admin"
    },
    "mahasigma": {
        "password": "user123",
        "role": "user"
    }
}

# FUNCTION LOGIN
def login():

    while True:
        bersihkan_layar()
        print("=====================================")
        print("      PENGELOLAAN NILAI MAHASISWA")
        print("=====================================")
        print("\n=== LOGIN ===")
        username = input("Username: ")
        password = pwinput.pwinput("Password: ")
        if username in akun and akun[username]["password"] == password:
            print("\nLogin Berhasil!")
            print("Selamat Datang,", username)
            print("Role:", akun[username]["role"])
            input("\nTekan Enter untuk melanjutkan...")
            return akun[username]["role"]
        else:
            print("\nUsername atau Password Salah!")
            input("\nTekan Enter untuk mencoba lagi...")

# FUNCTION TAMBAH NILAI
def tambah_nilai():

    bersihkan_layar()
    print("=====================================")
    print("          TAMBAH NILAI")
    print("=====================================")
    nama = input("Nama Mahasiswa: ")
    if nama == "":
        print("\nNama tidak boleh kosong!")
        input("\nTekan Enter...")
        return
    while True:
        try:
            tugas = float(input("Masukkan Nilai Tugas (0-100) : "))
            if 0 <= tugas <= 100 :
                break
            else :
                print("Nilai Harus Antara 0-100")
        except ValueError:
                print("Input Harus Berupa Angka")
    while True:
        try:
            uts = float(input("Masukkan Nilai UTS (0-100): "))
            if 0 <= uts <= 100:
                break
            else:
                    print("Nilai Harus Antara 0-100")
        except ValueError:
                print("Input Harus Berupa Angka")
    while True:
        try:
            uas = float(input("Masukkan Nilai UAS (0-100): "))
            if 0 <= uas <= 100:
                break
            else:
                print("Nilai Harus Antara 0-100")
        except ValueError:
                print("Input Harus Berupa Angka")    
    data = {
        "nama": nama,
        "tugas": tugas,
        "uts": uts,
        "uas": uas
    }
    data_mahasiswa.append(data)
    print("\nData berhasil ditambahkan!")
    input("\nTekan Enter...")

# FUNCTION TAMPILKAN NILAI
def tampilkan_nilai():
    bersihkan_layar()
    print("=====================================")
    print("        DATA NILAI MAHASISWA")
    print("=====================================")
    if len(data_mahasiswa) == 0:
        print("\nBelum ada data mahasiswa.")
        input("\nTekan Enter...")
        return
    tabel = PrettyTable()
    tabel.field_names = [
        "No",
        "Nama",
        "Tugas",
        "UTS",
        "UAS",
        "Nilai Akhir",
        "Grade"
    ]
    nomor = 1
    for data in data_mahasiswa:
        nilai_akhir = (
            data["tugas"] * 0.30 +
            data["uts"] * 0.30 +
            data["uas"] * 0.40
        )
        if nilai_akhir >= 85:
            grade = "A"
        elif nilai_akhir >= 75:
            grade = "B"
        elif nilai_akhir >= 65:
            grade = "C"
        elif nilai_akhir >= 50:
            grade = "D"
        else:
            grade = "E"
        tabel.add_row([
            nomor,
            data["nama"],
            data["tugas"],
            data["uts"],
            data["uas"],
            round(nilai_akhir, 2),
            grade
        ])
        nomor += 1
    print(tabel)
    input("\nTekan Enter...")

# FUNCTION UBAH NILAI
def ubah_nilai():

    bersihkan_layar()
    print("=====================================")
    print("           UBAH NILAI")
    print("=====================================")
    if len(data_mahasiswa) == 0:
        print("\nBelum ada data mahasiswa.")
        input("\nTekan Enter...")
        return  
    
    cari_nama = input("Nama Mahasiswa: ")
    for data in data_mahasiswa:
        if data["nama"] == cari_nama:
            print("Data", data["nama"],"Ditemukan")
            while True:
                try:
                    tugas = float(input("Masukkan Nilai Tugas Baru (0-100): "))
                    if 0 <= tugas <= 100:
                        break
                    else:
                        print("Nilai Harus Antara 0-100")
                except ValueError:
                        print("Input Harus Berupa Angka")
            while True:
                try:
                    uts = float(input("Masukkan Nilai UTS Baru (0-100): "))
                    if 0 <= uts <= 100:
                                break
                    else:                            
                        print("Nilai Harus Antara 0-100")
                except ValueError:
                        print("Input Harus Berupa Angka")
            while True:
                try:
                    uas = float(input("Masukkan Nilai UAS Baru (0-100): "))
                    if 0 <= uas <= 100:
                            break
                    else:
                        print("Nilai Harus Antara 0-100")
                except ValueError:
                        print("Input Harus Berupa Angka")
            data["tugas"] = tugas
            data["uts"] = uts
            data["uas"] = uas

            print("\nData Mahasiswa Berhasil Diubah")
            break
        else:
            print("\nData mahasiswa tidak ditemukan")

# FUNCTION HAPUS NILAi
def hapus_nilai():

    bersihkan_layar()
    print("=====================================")
    print("          HAPUS NILAI")
    print("=====================================")
    if len(data_mahasiswa) == 0:
        print("\nBelum ada data mahasiswa.")
        input("\nTekan Enter...")
        return

    cari_nama = input("Masukkan Nama Mahasiswa Yang Ingin Dihapus: ")

    for data in data_mahasiswa:
        if data["nama"] == cari_nama:
            data_mahasiswa.remove(data)
            print("Data Mahasiswa ",data["nama"] ," Berhasil Dihapus")
        break
    else:
        print("\nData Mahasiswa Tidak Ditemukan")    

# FUNCTION MENU
def menu(role):
    while True:
        bersihkan_layar()
        if role == "admin":
            print("=====================================")
            print("             MENU ADMIN")
            print("=====================================")
            print("1. Tambah Nilai")
            print("2. Tampilkan Nilai")
            print("3. Ubah Nilai")
            print("4. Hapus Nilai")
            print("5. Keluar")
            print("=====================================")
            pilihan = input("Pilih Menu (1-5): ")
            if pilihan == "1":
                tambah_nilai()
            elif pilihan == "2":
                tampilkan_nilai()
            elif pilihan == "3":
                ubah_nilai()
            elif pilihan == "4":
                hapus_nilai()
            elif pilihan == "5":
                print("\nLogout berhasil!")
                return
            else:
                print("\nPilihan menu tidak tersedia!")
                input("\nTekan Enter...")
        else:
            print("=====================================")
            print("             MENU USER")
            print("=====================================")
            print("1. Tampilkan Nilai")
            print("2. Keluar")
            print("=====================================")
            pilihan = input("Pilih Menu (1-2): ")
            if pilihan == "1":
                tampilkan_nilai()
            elif pilihan == "2":
                print("\nLogout berhasil!")
                return
            else:
                print("\nPilihan menu tidak tersedia!")
                input("\nTekan Enter...")

# PROGRAM UTAMA
def main():
    while True:
        role = login()
        menu(role)
        keluar = input("\nKeluar dari program? (y/n): ")
        if keluar == "y":
            break
        
    bersihkan_layar()
    print("=====================================")
    print("          PROGRAM SELESAI")
    print("=====================================")
    print("Terima kasih telah menggunakan program :)")
main()