"""
Skrip ini mendemonstrasikan cara kerja dasar dari
Operator Logika (Boolean) dalam bahasa pemrograman Python,
yaitu operator 'and', 'or', dan 'not'.
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

# Operator Logika (Boolean):
# and (DAN)
# or (ATAU)
# not (TIDAK)

# OPERATOR and (DAN)
# Fungsi: Menghasilkan True jika kedua kondisi yang dibandingkan bernilai True.
# Kalau salah satu False atau kedua kondisi False, maka hasilnya False.
print ("---Operator and (DAN)---")
HASIL = True and True
print ("Hasil dari True and True =",HASIL)
HASIL = True and False
print ("Hasil dari True and False =",HASIL)
HASIL = False and False
print ("Hasil dari False and False =",HASIL)

print () #indentasi

# OPERATOR or (ATAU)
# Fungsi: Menghasilkan True jika salah satu atau kedua kondisi bernilai True.
# Hanya menghasilkan False jika kedua kondisi bernilai False.
print ("---Operator or (ATAU)---")
HASIL = True or False
print ("Hasil dari True or False =",HASIL)
HASIL = False or False
print ("Hasil dari False or False =",HASIL)
HASIL = True or True
print ("Hasil dari True or True =",HASIL)

print () #indentasi

# OPERATOR not (TIDAK)
# Fungsi: Membalikan (negasi) nilai Boolean. True menjadi False,
# dan False menjadi True
print ("---Operator not (TIDAK)---")
HASIL = not True
print ("Hasil dari not True =",HASIL)
HASIL = not False
print ("Hasil dari not False =",HASIL)

#=======================================================#
print ("----------------------------------------")
print (f"==> Skrip {nama_file} selesai dijalankan <==")
