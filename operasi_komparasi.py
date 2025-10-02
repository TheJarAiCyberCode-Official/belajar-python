"""Skrip ini mendemonstrasikan berbagai macam operasi komparasi (perbandingan)
dalam bahasa pemrograman Python, seperti >, <, ==, >=, <=, is, dan is not.
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

# Operasi Komparasi
# lebih dari (>)
# kurang dari (<)
# sama dengan (==)
# Tidak sama dengan (!=)
# lebih dari sama dengan (>=)
# kurang dari sama dengan (<=)
# adalah (is)
# adalah bukan (is not)

a = float(input("Masukan angka pertama: "))
b = float(input("Masukan angka kedua: "))

print ("--- LEBIH DARI (>) ---")
hasil = a > b
print ("Apakah nilai",a,">",b,"Jawabanya:", hasil)

print () #indentasi

print ("--- KURANG DARI (<) ---")
hasil = a < b
print ("Apakah nilai",a,"<",b,"Jawabanya:",hasil)

print () #indentasi

print ("--- SAMA DENGAN (==) ---")
hasil = a == b
print ("Apakah nilai",a,"==",b,"Jawabanya:",hasil)

print () #indentasi

print ("--- TIDAK SAMA DENGAN (!=) ---")
hasil = a != b
print ("Apakah nilai",a,"!=",b,"Jawabanya:",hasil)

print () #indentasi

print ("--- LEBIH BESAR SAMA DENGAN (>=) ---")
hasil = a >= b
print ("Apakah nilai",a,">=",b,"Jawabanya:",hasil)

print () #indentasi

print ("--- LEBIH KECIL SAMA DENGAN (<=) ---")
hasil = a <= b
print ("Apakah nilai",a,"<=",b,"Jawabanya:",hasil)

print () #indentasi

print ("--- ADALAH (is) ---")
hasil = a is b
print ("Apakah nilai",a,"is",b,"Jawabanya:",hasil)

print () #indentasi

print ("--- ADALAH BUKAN (is not) ---")
hasil = a is not b
print ("Apakah nilai",a,"is not",b, "Jawabanya:",hasil)
#=======================================================#
print ("----------------------------------------")
print (f"==> Skrip {nama_file} selesai dijalankan <==")
