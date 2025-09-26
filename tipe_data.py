"""
Skrip ini mendemonstrasikan berbagai tipe data dasar di Python:
string, integer, float, boolean, dan tipe data khusus complex.
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

# tipe data: Kumpulan huruf atau karakter (string)
DATA_STRING = "The JarAi Cyber Code"
print ("Data:", DATA_STRING)
print ("Bertipe:", type(DATA_STRING))

# tipe data: Angka bilangan bulat/satuan tanpa tanda koma . (integer)
DATA_INTEGER = 10
print ("Data:", DATA_INTEGER)
print ("Bertipe:", type(DATA_INTEGER))

# tipe data: Angka bilangan desimal dengan tanda koma . (float)
DATA_FLOAT = 10.5
print ("Data:", DATA_FLOAT)
print ("Bertipe:", type(DATA_FLOAT))

# tipe data: Biner True/False (boolean)
DATA_BOOL = True
print ("Data:", DATA_BOOL)
print ("Bertipe:", type(DATA_BOOL))

## tipe data khusus
# bilangan kompleks
data_complex = complex(10,5)
print ("Data:", data_complex)
print ("Bertipe:", type(data_complex))

#=======================================================#
print ("----------------------------------------")
print (f"==> Skrip {nama_file} selesai dijalankan <==")
