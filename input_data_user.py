"""
Skrip ini dibuat untuk mendemonstrasikan bagaimana fungsi input() di Python
selalu menghasilkan string (str) dan cara melakukan konversi tipe data
(type casting) ke integer (int), float, dan boolean (bool).
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

# Data yang dimasukan pasti tipe str (string)
data = input("Masukan data : ")
print ("Data:",data,",Bertipe:",type(data))

# Jika ingin memasukan int (integer) dan float, maka perlu di casting
angka = int(input("Masukan angka: "))
print ("Data:",angka,",Bertipe:",type(angka))

angka = float(input("Masukan angka: "))
print ("Data:",angka,",Bertipe:",type(angka))

# Bagaimana dengan bool (boolean)?
# Akan bisa False jika di casting ke Integer (int) dengan nilai 0=False 1=True
data_bool = bool(int(input("Masukan nilai boolean: ")))
print ("Data:", data_bool,",Bertipe:",type(data_bool))

#=======================================================#
print ("----------------------------------------")
print (f"==> Skrip {nama_file} selesai dijalankan <==")
