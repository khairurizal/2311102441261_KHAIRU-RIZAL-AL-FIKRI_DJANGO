## Deskripsi tentang yang saya buat
Project yang saya telah buat ini kurang lebih seperti yang ditunjukkan di video terlampir. Aplikasinya berisi kumpulan berita dan artikel, dan saya merancangnya supaya punya potensi untuk terus dikembangkan agar fiturnya lebih lengkap dan bermanfaat.

# Cara menjalakannya
Langkah 1: Buka Command Prompt (CMD)
Buka CMD atau terminal bawaan 

Langkah 2: Masuk ke Direktori Proyek
Arahkan ke folder tempat proyek akan dibuat atau sudah ada:
cd nama_folder

Langkah 3: Buat Virtual Environment
Buat virtual environment untuk mengelola  proyek:
py -m venv .venv

Langkah 4: Aktifkan Virtual Environment
Aktifkan virtual environment:
.venv\Scripts\activate

Langkah 5: Install Django
Install Django menggunakan pip:
pip install django

Langkah 6: Buat Proyek Django (Opsional, jika belum dibuat)
Jika belum ada proyek, buat dengan perintah:
django-admin startproject nama_proyek .

Langkah 7: Buat Migrasi Database
Setelah membuat atau mengedit model, buat file migrasi:
python manage.py makemigrations

Langkah 8: Terapkan Migrasi Database
Terapkan file migrasi untuk membuat struktur database:
python manage.py migrate

Langkah 9: Jalankan Server
Jalankan server pengembangan untuk memeriksa aplikasi:
python manage.py runserver

Langkah 10: Akses Aplikasi di Browser
Buka browser dan akses :
http://127.0.0.1:8000