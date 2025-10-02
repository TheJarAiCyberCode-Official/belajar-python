"""
operasi_logika.py
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

# Operator Logika dalam Python:
# and (DAN)
# or (ATAU)
# not (TIDAK)

print ("---Operator and (DAN)---")
hasil = True and True
print ("Hasil dari True and True =",hasil)
hasil = True and False
print ("Hasil dari True and False =",hasil)
hasil = False and False
print ("Hasil dari False and False =",hasil)

print () #indentasi

print ("---Operator or (ATAU)---")
hasil = True or False
print ("Hasil dari True or False =",hasil)
hasil = False or False
print ("Hasil dari False or False =",hasil)
hasil = True or True
print ("Hasil dari True or True =",hasil)

print () #indentasi

print ("---Operator not (TIDAK)---")
hasil = not True
print ("Hasil dari not True =",hasil)
hasil = not False
print ("Hasil dari not False =",hasil)

#=======================================================#
print ("----------------------------------------")
print (f"==> Skrip {nama_file} selesai dijalankan <==")
