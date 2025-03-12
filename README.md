## PORTOFOLIO WEB SAYA ##
di dalam web saya ini terdapat sedikit informasi dari saya

## ADA APA SAJA DALAM WEB INI"
pada halaman home : menampilkan sedikit infomasi tentang jurusan dan nama kampus saya
pada halaman about : menampilkan sedikit tentang diri saya

# CARA MENJALANKAN PROJECT #
1.Buka Command Prompt (CMD) : Cari "cmd" di pencarian Windows dan buka.

2.Masuk ke Folder Tempat Proyek Akan Dibuat
Gunakan perintah berikut untuk berpindah ke folder tempat  menyimpan proyek
(cd nama_folder)

3.Buat Virtual Environment
Ketik perintah ini untuk membuat virtual environment:
(py -m venv .venv)

4.Aktifkan Virtual Environment
Masuk ke folder virtual environment dengan mengetik:
(.venv\Scripts\activate)

5.Install Django
Setelah virtual environment aktif, ketik perintah ini untuk menginstal Django:
(pip install django)

6.Buat Proyek Baru
Gunakan perintah ini untuk membuat proyek baru:
(django-admin startproject webrzl)

7.Cek Proyek Django yang Dibuat
Masuk ke folder proyek:
(cd webrzl)

Jalankan perintah ini untuk memulai server Django:
(py manage.py runserver)

Jika berhasil, Anda akan melihat pesan bahwa server sedang berjalan.
Buka browser Anda, lalu akses:
cpp
Copy
Edit
http://127.0.0.1:8000
kita akan melihat halaman "Welcome to Django".