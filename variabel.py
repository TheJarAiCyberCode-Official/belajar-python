"""
Skrip ini mendemonstrasikan cara membuat, menampilkan, dan memahami
tipe data dasar (string, integer, float, boolean) serta aturan
penamaan variabel di Python.
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

# Variabel Python
# Variabel adalah sebuah tempat untuk menyimpan nilai data

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

# Mengetahui tipe data suatu variabel dengan fungsi type()
print ("Tipe data VARIABEL_FLOAT adalah:", type(VARIABEL_FLOAT))

# Tanda kutip tunggal atau ganda ?
# Variabel string bisa di deklarasikan dengan menggunakan
# tanda kutip tunggal dan ganda itu sama saja.
# Contohnya:
# VARIABEL_STRING = 'The JarAi Cyber Code'
# VARIABEL_STRING = "The JarAi Cyber Code"


# Peka terhadap huruf kecil dan besar
# Nama suatu variabel peka huruf kecil dan besar. Contohnya:
# ini akan membuat dua variabel
# variabel = 8
# Variabel = "JarAi"

# Penamaan variabel
# nama_variabel = 10 # menggunakan underscore/garis bawah (snake_case) <== Disarankan!
# namaVariabel = 3 # huruf kecil diawal, huruf kapital awal kata berikutnya. (camelCase)
# variabel3 = 5 # menggunakan kombinasi angka di akhir

#=======================================================#
print ("----------------------------------------")
print (f"==> Skrip {nama_file} selesai dijalankan <==")
