# Belajar-Python
Repositori ini untuk belajar Python dari dasar untuk pemula,
sekaligus merupakan dokumentasi proses pembelajaran Saya.

---

# Python REPL
Python REPL itu singkatan dalam bahasa inggris **Read-Eval-Print-Loop**
atau dalam bahasa sehari-hari bisa dibilang sebagai **konsol interaktif**-nya Python.🐍

Sebuah program kecil yang memungkinkan kamu mengetikan kode Python
secara langsung dan melihat hasilnya seketika.
Jadi menggunakan REPL ini cara yang bagus untuk bereksperimen dan belajar!

## Cara kerja REPL 💻
Sesuai dengan namanya (**Read-Eval-Print-Loop**), REPL bekerja dalam siklus yang berulang:
1. **Read (Baca)**: REPL membaca (menerima) baris kode Python yang kamu ketikan.
2. **Eval (Evaluasi)**: Python menjalankan (mengeksekusi) kode tersebut.
3. **Print (Cetak)**: Hasil dari eksekusi (misalnya, nilai sebuah variabel,
hasil perhitungan) akan ditampilkan dilayar.
4. **Loop (Ulang)**: Proses kembali ke langkah nomor 1, menunggu kode berikutnya.

## Kenapa REPL Penting? 🤔
Buat kamu yang suka ngulik di bidang Teknologi Informasi dan Pemrograman.
REPL ini beguna banget buat:
+ **Eksperimen Cepat**: Mau coba fungsi atau sintaks baru? Tinggal ketik aja,
enggak perlu bikin file (`.py`) dulu.
+ **Debug Instan**: Bisa buat ngecek nilai variabel atau hasil perhitungan 
di tengah-tengah proses _coding_.
+ **Belajar**: Pemula biasanya pakai REPL
buat langsung praktik dan melihat bagaimana kode Python bekerja.

## Menjelajahi dan Cara Memulai Python REPL 🚀
Gampang kok! Kalau kamu sudah menginstal Python di komputer,
biasanya kamu bisa memulainya dengan:

+ Buka Terminal (di Linux/macOS) atau Command Prompt/PowerShell (di Windows).
+ Setelah terminal terbuka, ketik perintah: `python` atau kadang `python3`
+ Kamu akan melihat prompt perintah yang terdiri dari tiga panah (`>>>`).
yang menandakan kamu sudah masuk ke mode REPL dan siap mengetikkan kode!
+ Untuk lebih jelasnya, Kamu tidak perlu mengetikkan tiga panah tersebut
Kamu hanya perlu mengetikkan perintah setelahnya.

Contoh sederhana di dalam REPL:
```python
>>> 8
8
```
Apa yang terjadi? Ingat singkatan REPL Read-Eval-Print-Loop:
+ **Read (Baca)**: Python membaca 8
+ **Eval (Evaluasi)**: Python mengevaluasi masukan tersebut
lalu memutuskan bahwa itu sebuah angka
+ **Print (Cetak)**: mencetak apa yang dievaluasi dalam hal ini angka 8
+ **Loop (Ulang)**: siap untuk input kode berikutnya

Coba terus bereksperimen sesuatu apa yang ingin kamu pelajari dalam kode Python
dan jangan takut membuat kesalahan.
seperti apa yang di sebutkan dalam buku yang dibuat Oleh AI Sweigart:
[Automate the Boring Stuff with Python](https://automatetheboringstuff.com/3e/chapter1.html)
> KESALAHAN ITU WAJAR!
>> Hal terbaik tentang komputer adalah ia menjalankan instruksi persis seperti yang Anda berikan.
>> Ini juga hal terburuk tentang komputer.
>> Komputer tidak bisa menggunakan akal sehat untuk memahami apa yang ingin Anda lakukan.
>> Program akan macet jika berisi kode yang tidak dipahami komputer,
>> yang akan menyebabkan Python menampilkan pesan kesalahan.
>> Namun, pesan kesalahan tidak merusak komputer Anda, jadi jangan takut membuat kesalahan.
>> Macet hanya berarti program berhenti berjalan secara tiba-tiba.
>> 
>> Biasakan diri melihat pesan kesalahan, karena Anda akan terus-menerus menemuinya 
>> (meskipun Anda memiliki pengalaman pemrograman puluhan tahun).
>> Pesan kesalahan seringkali samar dan tidak dimaksudkan untuk langsung dipahami oleh pemula.
>> Jika Anda ingin tahu lebih banyak tentang suatu kesalahan,
>> Anda dapat mencari teks pesan kesalahan yang tepat secara daring untuk informasi lebih lanjut. 

## Menggunakan riwayat perintah (history)
Kamu perlu tahu bahwa Python REPL juga menyimpan riwayat perintah?
Kamu bisa berpindah antar perintah sebelumnya dengan menekan tombol panah atas dan bawah.
Python menyimpan riwayat ini dalam sebuah berkas, pada sebagian besar OS biasanya di: `~/.python_history`
sehingga riwayat ini akan tetap ada bahkan di antara sesi.
Kecuali, jika Kamu menghapus file `~/.python_history`.

---

# Variabel Python
Dalam Python, variabel merupakan sebuah wadah yang berfungsi untuk menyimpan data.

## Tanda kutip tunggal atau ganda ?
Variabel string bisa di deklarasikan dengan menggunakan
tanda kutip tunggal dan ganda itu sama saja. Contohnya:
```python
nama_saya = 'The JarAi Cyber Code'
asal_negara = "Indonesia"

print (nama_saya)
print (asal_negara)
```
## Aturan Penamaan variabel
Untuk menggunakan variabel secara efektif, kita harus mengikuti aturan penamaan Python:
+ Nama variabel hanya dapat berisi huruf, angka, dan garis bawah (_).
+ Nama variabel tidak dapat dimulai dengan angka.
+ Hindari penggunaan kata kunci Python (misalnya, if, else, for) sebagai nama variabel.
    + Benar:
    ```python
    nama = "The JarAi Cyber Code"
    _usia = 81
    tinggi_badan = 175
    ```
    + Salah:
    ```python
    2nama = "Kode akan Error" #karena dimulai dengan angka
    if = 10 # menggunakan kata kunci Python
    nama-saya = "Udin" 
    ```

+ Peka terhadap huruf kecil dan besar
Nama suatu variabel peka huruf kecil dan besar.
ini akan membuat dua variabel berbeda. Contohnya:
    ```python
    VARIABEL = 'JarAi'
    variabel = 'Cyber Code'

    print (VARIABEL)
    print (variabel)
    ```
