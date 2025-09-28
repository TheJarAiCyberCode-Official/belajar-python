"""
main.py

Titik masuk utama (main execution file) untuk proyek belajar Python ini.
File ini bertanggung jawab sebagai skrip yang pertama kali dijalankan saat proyek dijalankan.
Semua kode utama, inisialisasi, atau pemanggilan fungsi dapat diletakkan di sini.

Fitur:
- Menampilkan nama file skrip yang sedang dijalankan.
- Memberikan struktur penanda awal dan akhir eksekusi agar output mudah dibaca di terminal.
- Tempat utama untuk memulai koding atau eksperimen Python dalam proyek ini.

Penggunaan:
Jalankan file ini secara langsung untuk memulai aplikasi atau pengujian awal.
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
#         Tempat kamu memulai koding disini!
#=======================================================#
print ("----------------------------------------")
print (f"==> Skrip {nama_file} selesai dijalankan <==")
