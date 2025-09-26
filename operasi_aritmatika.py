"""
Skrip ini mendemonstrasikan berbagai operator aritmatika dasar di Python,
termasuk eksponen, perkalian, pembagian, modulus, penjumlahan,
pengurangan, serta aturan prioritas operasi (order of operations).
"""

# Modul os digunakan untuk berinteraksi dengan sistem operasi.
import os

# Mengambil bagian nama file saja dari path lengkap yang ada di __file__.
# jika __file__ isinya /home/TheJarAiCyberCode/script/namafile.py,
# maka os.path.basename() akan mengambil namafile.py saja.
nama_file = os.path.basename(__file__)

# Untuk penanda agar struktur output skrip mudah dibaca
print (f"==> Skrip {nama_file} dimulai <==")
print ("----------------------------------------")
#=======================================================#

# OPERASI ARITMATIKA
print ("""Operasi Aritmatika ini dipakai untuk perhitungan matematika biasa
""")

# Eksponen atau pangkat (**)
A = 10
B = 3
print ("Hasil Eksponen atau pangkat dari nilai",A,"**",B,"=",A ** B)

# Perkalian (*)
print ("Hasil Perkalian dari nilai",A,"*",B,"=",A * B)

# Pembagian (/)
print ("Hasil Pembagian dari nilai",A,"/",B,"=",A / B)

# Pembagian dibulatkan ke bawah (//)
print ("Hasil Pembagian Bulat dari nilai",A,"//",B,"=",A // B)

# Modulus atau sisa pembagian (%)
print ("Hasil Modulus atau sisa pembagian dari nilai",A,"%",B,"=",A % B)

# Pertambahan (+)
print ("Hasil Penjumlahan dari nilai",A,"+",B,"=",A + B)

# Pengurangan (-)
print ("Hasil Pengurangan dari nilai",A,"-",B,"=",A - B)

# Prioritas operasi
print () # Indentasi

#  1. ()
#  2. Eksponen atau pangkat
#  3. Perkalian, Pembagian, Pembagian dibulatkan, Modulus * / // %
#  4. Pertambahan, Pengurangan + -

X = 3
Y = 2
Z = 4

HASIL = X ** Y * Z + X / Y - Y % Z // X
print (X,"**",Y,"*",Z,"+",X,"/",Y,"-",Y,"%",Z,"//",X,"=",HASIL)

HASIL = X + Y * Z
print (X,"+",Y,"*",Z,"=",HASIL)

HASIL = (X + Y) * Z
print ("(",X,"+",Y,") *",Z,"=",HASIL)
#=======================================================#
print ("----------------------------------------")
print (f"==> Skrip {nama_file} selesai dijalankan <==")
