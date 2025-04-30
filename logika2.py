print("Nama:Yayan Nadhir Kalam Nim : 24241118")

inputUser = int(input("masukan angka yang bernilai kurang dari 24 atau lebih besar dari 18:"))

#memeriksa angka kurang dari 18
iskurangdari = (inputUser <18)

#memeriksa angka lebih dari 24
islebihdari = (inputUser >24)

final = iskurangdari or islebihdari
print("angka yang anda masukan :",final)