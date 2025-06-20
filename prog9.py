# pemisahan string
# buat program untuk memisahkan string berikut

# masukkan nama domain anda
domain = input("Masukkan nama domain anda (misalnya: yayannadhirkalamm.com): ")

# memisahkan domain menggunakan tanda titik
nama, ekstensi = domain.split(".")

# menampilkan hasil
print("Nama domain anda:", nama)
print("Domain yang anda gunakan:", ekstensi)