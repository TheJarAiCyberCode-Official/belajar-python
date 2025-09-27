"""
Skrip ini mendemonstrasikan proses casting (konversi) antar
tipe data dasar di Python: string, integer, float, dan boolean.
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

## STRING
print ("----- STRING -----")
DATA_STRING = "10"
print ("Data:", DATA_STRING, ",Bertipe:", type(DATA_STRING))

DATA_FLOAT   = float(DATA_STRING) # string harus berupa angka
DATA_INTEGER = int(DATA_STRING) # string harus berupa angka
DATA_BOOLEAN = bool(DATA_STRING) # jadi False jika string kosong ""
print ("Data:", DATA_FLOAT, ",Bertipe:", type(DATA_FLOAT))
print ("Data:", DATA_INTEGER, ",Bertipe:", type(DATA_INTEGER))
print ("Data:", DATA_BOOLEAN, ",Bertipe:", type(DATA_BOOLEAN))

## INTEGER
print ("----- INTEGER -----")
DATA_INTEGER = 9
print ("Data:", DATA_INTEGER, ",Bertipe:", type(DATA_INTEGER))

DATA_FLOAT   = float(DATA_INTEGER)
DATA_STRING  = str(DATA_INTEGER)
DATA_BOOLEAN = bool(DATA_INTEGER) # jadi False jika nilai int = 0
print ("Data:", DATA_FLOAT, ",Bertipe:", type(DATA_FLOAT))
print ("Data:", DATA_STRING, ",Bertipe:", type(DATA_STRING))
print ("Data:", DATA_BOOLEAN, ",Bertipe:", type(DATA_BOOLEAN))

## FLOAT
print ("----- FLOAT -----")
DATA_FLOAT = 9.5
print ("Data:", DATA_FLOAT, ",Bertipe", type(DATA_FLOAT))

DATA_INTEGER = int(DATA_FLOAT) # jadi dibulatkan ke bawah
DATA_STRING  = str(DATA_FLOAT)
DATA_BOOLEAN = bool(DATA_FLOAT) # jadi False jika nilai float = 0
print ("Data:", DATA_INTEGER, ",Bertipe:", type(DATA_INTEGER))
print ("Data:", DATA_STRING, ",Bertipe:", type(DATA_STRING))
print ("Data:", DATA_BOOLEAN, ",Bertipe:", type(DATA_BOOLEAN))

## BOOLEAN
print ("----- BOOLEAN -----")
DATA_BOOLEAN = True
print ("Data:", DATA_BOOLEAN, ",Bertipe:", type(DATA_BOOLEAN))

DATA_INTEGER = int(DATA_BOOLEAN)
DATA_STRING  = str(DATA_BOOLEAN)
DATA_FLOAT   = float(DATA_BOOLEAN)
print ("Data:", DATA_INTEGER, ",Bertipe:", type(DATA_INTEGER))
print ("Data:", DATA_STRING, ",Bertipe:", type(DATA_STRING))
print ("Data:", DATA_FLOAT, ",Bertipe:", type(DATA_FLOAT))

#=======================================================#
print ("----------------------------------------")
print (f"==> Skrip {nama_file} selesai dijalankan <==")
