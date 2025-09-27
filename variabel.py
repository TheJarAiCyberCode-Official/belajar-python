"""
Skrip ini mendemonstrasikan cara membuat, menampilkan, dan memahami
variabel di Python.
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

# Membuat variabel
VARIABEL_STRING = "The JarAi Cyber Code"
VARIABEL_INTEGER = 10
VARIABEL_FLOAT = 10.5
VARIABEL_BOOL = True

# Mencetak atau menampilkan variabel dengan print()
print ("Isi dari VARIABEL_STRING adalah:", VARIABEL_STRING)
print ("Isi dari VARIABEL_INTEGER adalah:", VARIABEL_INTEGER)
print ("Isi dari VARIABEL_FLOAT adalah:", VARIABEL_FLOAT)
print ("Isi dari VARIABEL_BOOL adalah:", VARIABEL_BOOL)

#=======================================================#
print ("----------------------------------------")
print (f"==> Skrip {nama_file} selesai dijalankan <==")
