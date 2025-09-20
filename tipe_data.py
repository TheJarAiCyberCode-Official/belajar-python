# Modul os digunakan untuk berinteraksi dengan sistem operasi.
import os

# Mengambil nama file dari variabel __file__
nama_file = os.path.basename(__file__)

# Untuk penanda agar struktur output skrip mudah dibaca
print (f"==> Skrip {nama_file} dimulai <==")
print ("----------------------------------------")
#=======================================================#

# tipe data: Kumpulan huruf atau karakter (string)
data_string = "The JarAi Cyber Code"
print ("Data:", data_string)
print ("Bertipe:", type(data_string))

# tipe data: Angka bilangan bulat/satuan tanpa tanda koma . (integer)
data_integer = 10
print ("Data:", data_integer)
print ("Bertipe:", type(data_integer))

# tipe data: Angka bilangan desimal dengan tanda koma . (float)
data_float = 10.5
print ("Data:", data_float)
print ("Bertipe:", type(data_float))

# tipe data: Biner True/False (boolean)
data_bool = True
print ("Data:", data_bool)
print ("Bertipe:", type(data_bool))

## tipe data khusus
# bilangan kompleks
data_complex = complex(10,5)
print ("Data:", data_complex)
print ("Bertipe:", type(data_complex))

#=======================================================#
print ("----------------------------------------")
print (f"==> Skrip {nama_file} selesai dijalankan <==")
