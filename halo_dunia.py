"""
halo_dunia.py

Program belajar python pertama untuk menyapa dan menanyakan nama, dan usia.
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
# Program ini menyapa dan menanyakan nama, dan usia.
print ("Halo, Dunia!")
print ("Siapa nama Kamu?")
nama_saya = input(">")

print ("Senang bertemu denganmu, " + nama_saya)
print ("Panjang nama Anda adalah:",len(nama_saya))

print ("Berapa umur kamu?")
usia_saya = input(">")

print ("Kamu akan berusia " + str(int(usia_saya) + 1) + " tahun, dalam setahun.")
#=======================================================#
print ("----------------------------------------")
print (f"==> Skrip {nama_file} selesai dijalankan <==")
