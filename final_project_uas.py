
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    clear()
    print("###### KELOMPOK ######")
    print("Nama: Yayan Nadhir Kalam | NIM: 24241118")
    print("Nama: Muhammad Dede Anggian Rizadi  | NIM: 24241116")
    print("Nama: Surya Ramdhani  | NIM: 24241144")
    print("=" * 40)

def tugas1():
    clear()
    print("===== TUGAS 1: Logika Boolean =====")
    print("NOT:", not False)
    print("AND:", False and True, True and True)
    print("OR:", False or True, True or False)
    print("XOR:", False ^ True, True ^ True)

def tugas2():
    clear()
    print("===== TUGAS 2: Logika Input Angka =====")
    angka = int(input("Masukkan angka (<24 atau >38): "))
    print("Angka < 24:", angka < 24)
    print("Angka > 38:", angka > 38)
    print("Valid:", angka < 24 or angka > 38)

def tugas3():
    clear()
    print("===== TUGAS 3: Nilai Kuliah =====")
    nilai = float(input("Masukkan nilai (0-100): "))
    if nilai >= 90:
        grade = "A"
    elif nilai >= 85:
        grade = "A-"
    elif nilai >= 80:
        grade = "B+"
    elif nilai >= 70:
        grade = "B"
    elif nilai >= 65:
        grade = "B-"
    elif nilai >= 60:
        grade = "C+"
    elif nilai >= 55:
        grade = "C"
    elif nilai >= 50:
        grade = "C-"
    elif nilai >= 40:
        grade = "D"
    else:
        grade = "E"
    print("Grade:", grade)

def tugas4():
    clear()
    print("===== TUGAS 4: Cek Umur =====")
    umur = int(input("Masukkan umur: "))
    print("Kategori:", "Anak-anak" if umur < 18 else "Dewasa")

def tugas5():
    clear()
    print("===== TUGAS 5: Cek Password =====")
    password = input("Masukkan password: ")
    print("Panjang password:", len(password))
    print("Validasi:", "Lolos" if len(password) >= 8 else "Tidak Lolos")

def tugas6():
    clear()
    print("===== TUGAS 6: String Angka =====")
    angka = "1234567890"
    print("Data terakhir:", angka[-1])
    print("Data pertama:", angka[0])
    print("Data ke-3 sampai 6:", angka[2:6])

def tugas7():
    clear()
    print("===== TUGAS 7: Pemisah Domain =====")
    domain = input("Masukkan domain (contoh: surya.com): ")
    bagian = domain.partition(".")
    print("Nama domain:", bagian[0])
    print("Ekstensi:", bagian[2])

def tugas8():
    clear()
    print("===== TUGAS 8: Pembulatan Harga =====")
    print("Harga Normal: 15.5935 ->", round(15.5935, 1), "(1 digit),", round(15.5935, 2), "(2 digit)")
    print("Harga Diskon: 16.45987 ->", round(16.45987, 1), "(1 digit),", round(16.45987, 2), "(2 digit)")
    print("Harga Retail: 14.96884 ->", round(14.96884, 1), "(1 digit),", round(14.96884, 2), "(2 digit)")

def main():
    banner()
    while True:
        print("\nPilih Program:")
        print("[1] TUGAS 1  | [2] TUGAS 2  | [3] TUGAS 3")
        print("[4] TUGAS 4  | [5] TUGAS 5  | [6] TUGAS 6")
        print("[7] TUGAS 7  | [8] TUGAS 8  | [0] Keluar")
        pilihan = input(">> Pilih nomor tugas: ")
        if pilihan == '1':
            tugas1()
        elif pilihan == '2':
            tugas2()
        elif pilihan == '3':
            tugas3()
        elif pilihan == '4':
            tugas4()
        elif pilihan == '5':
            tugas5()
        elif pilihan == '6':
            tugas6()
        elif pilihan == '7':
            tugas7()
        elif pilihan == '8':
            tugas8()
        elif pilihan == '0':
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid.")
        input("\nTekan Enter untuk kembali...")
        banner()

if __name__ == "__main__":
    main()