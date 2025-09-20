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

"""
Casting tipe data, merubah dari satu tipe data ke tipe data lain
tipe data: str, int, float, bool
"""

## STRING
print ("----- STRING -----")
data_string = "10"
print ("Data:", data_string, ",Bertipe:", type(data_string))

data_float   = float(data_string) # string harus berupa angka
data_integer = int(data_string) # string harus berupa angka
data_boolean = bool(data_string) # jadi False jika string kosong
print ("Data:", data_float, ",Bertipe:", type(data_float))
print ("Data:", data_integer, ",Bertipe:", type(data_integer))
print ("Data:", data_boolean, ",Bertipe:", type(data_boolean))

## INTEGER
print ("----- INTEGER -----")
data_integer = 9
print ("Data:", data_integer, ",Bertipe:", type(data_integer))

data_float   = float(data_integer)
data_string  = str(data_integer)
data_boolean = bool(data_integer) # jadi False jika nilai int = 0
print ("Data:", data_float, ",Bertipe:", type(data_float))
print ("Data:", data_string, ",Bertipe:", type(data_string))
print ("Data:", data_boolean, ",Bertipe:", type(data_boolean))

## FLOAT
print ("----- FLOAT -----")
data_float = 9.5
print ("Data:", data_float, ",Bertipe", type(data_float))

data_integer = int(data_float) # jadi dibulatkan ke bawah
data_string  = str(data_float)
data_boolean = bool(data_float) # jadi False jika nilai float = 0
print ("Data:", data_integer, ",Bertipe:", type(data_integer))
print ("Data:", data_string, ",Bertipe:", type(data_string))
print ("Data:", data_boolean, ",Bertipe:", type(data_boolean))

## BOOLEAN
print ("----- BOOLEAN -----")
data_boolean = True
print ("Data:", data_boolean, ",Bertipe:", type(data_boolean))

data_integer = int(data_boolean)
data_string  = str(data_boolean)
data_float   = float(data_boolean)
print ("Data:", data_integer, ",Bertipe:", type(data_integer))
print ("Data:", data_string, ",Bertipe:", type(data_string))
print ("Data:", data_float, ",Bertipe:", type(data_float))

#=======================================================#
print ("----------------------------------------")
print (f"==> Skrip {nama_file} selesai dijalankan <==")
