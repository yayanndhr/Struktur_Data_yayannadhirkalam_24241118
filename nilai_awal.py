#program digit angka

harga_normal = 15.5935
harga_diskon = 16.45987
harga_retail = 14.96884

print ("pilih harga")
print ("1. harga normal")
print ("2. harga diskon")
print ("3. harga retail")
pilihan = int(input("masukan pilihan (1/2/3): "))

if pilihan == 1 :
    harga = harga_normal
elif pilihan == 2 :
    harga = harga_diskon
elif pilihan == 3 :
    harga = harga_retail
else:
    print("pilihan tidak valid")
    exit()

print(f"harga dengan 1 digit:{harga:.1f}")
print(f"harga dengan 2 digit:{harga:.2f}")                 