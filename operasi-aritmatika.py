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
a = 10
b = 3
print ("Hasil Eksponen atau pangkat dari nilai",a,"**",b,"=",a ** b)

# Perkalian (*)
print ("Hasil Perkalian dari nilai",a,"*",b,"=",a * b)

# Pembagian (/)
print ("Hasil Pembagian dari nilai",a,"/",b,"=",a / b)

# Pembagian dibulatkan ke bawah (//)
print ("Hasil Pembagian Bulat dari nilai",a,"//",b,"=",a // b)

# Modulus atau sisa pembagian (%)
print ("Hasil Modulus atau sisa pembagian dari nilai",a,"%",b,"=",a % b)

# Pertambahan (+)
print ("Hasil Penjumlahan dari nilai",a,"+",b,"=",a + b)

# Pengurangan (-)
print ("Hasil Pengurangan dari nilai",a,"-",b,"=",a - b)

# Prioritas operasi
print () # Indentasi
"""
  1. ()
  2. Eksponen atau pangkat
  3. Perkalian, Pembagian, Pembagian dibulatkan, Modulus * / // %
  4. Pertambahan, Pengurangan + -
"""
x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print (x,"**",y,"*",z,"+",x,"/",y,"-",y,"%",z,"//",x,"=",hasil)

hasil = x + y * z
print (x,"+",y,"*",z,"=",hasil)

hasil = (x + y) * z
print ("(",x,"+",y,") *",z,"=",hasil)
#=======================================================#
print ("----------------------------------------")
print (f"==> Skrip {nama_file} selesai dijalankan <==")
