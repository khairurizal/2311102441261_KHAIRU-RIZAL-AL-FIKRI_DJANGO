## ⚡ DJANGO WEB PROJECT

### 📝 Fitur Website

- **🏠 Beranda (Home)**  
  Menampilkan halaman utama dari website yang menjadi titik awal akses pengguna.

- **📊 Dashboard**  
  Menampilkan laporan grafis, manajemen data, serta informasi penting dalam tampilan visual yang informatif dan responsif.

---

### 🔧 Langkah Menjalankan Proyek

⚙️ DJANGO
💡Apa Saja Di Website Ini?
1. HOME - Menampilkan Halaman Utama dari website.
2. Dashboard - Menampilkan laporan grafis, manajemen informasi, dan data-data.

🪄 Cara Menjalankan Proyek Django:

1. **Buka Command Prompt (CMD)**
   - Tekan `Win + R`, lalu ketik `cmd` dan tekan Enter.

2. **Masuk ke Folder Tempat Proyek Akan Dibuat**
   - Gunakan perintah `cd` untuk berpindah ke direktori tempat kamu ingin membuat proyek.
     Contoh:
     ```
     cd nama_folder
     ```

3. **Buat Virtual Environment**
   - Gunakan perintah berikut untuk membuat virtual environment:
     ```
     py -m venv .venv
     ```

4. **Aktifkan Virtual Environment**
   - Setelah membuat virtual environment, aktifkan dengan perintah berikut:
     ```
     .venv\Scripts\activate
     ```

5. **Install Django**
   - Install Django dengan menggunakan pip:
     ```
     pip install django
     ```

6. **Buat Migration**
   - Setelah instalasi selesai, buat migration dengan perintah:
     ```
     python manage.py makemigrations
     ```

7. **Migrate Database**
   - Setelah migration dibuat, lakukan migrate ke database dengan perintah:
     ```
     python manage.py migrate
     ```

8. **Jalankan Server**
   - Terakhir, jalankan server Django dengan perintah:
     ```
     python manage.py runserver
     ```

Setelah itu, buka browser dan akses `http://127.0.0.1:8000/` untuk melihat website yang berjalan.
