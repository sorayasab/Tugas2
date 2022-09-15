# Penjelasan

   Terdapat beberapa tahap alur *request client* yang diproses di Django. Pertama, *request* yang masuk ke dalam server Django akan diproses melalui urls. Kemudian diteruskan ke views yang didefinisikan oleh *developer* untuk memproses permintaan tersebut. Jika ada proses yang memerlukan keterlibatan database, maka views akan memanggil query ke models dan database akan mengembalikan hasil dari query tersebut ke views. Setelah permintaan telah selesai diproses, hasil proses tersebut akan dipetakan ke dalam HTML yang telah ditentukan sebelum akhirnya HTML tersebut dikembalikan ke komputer atau pengguna sebagai respons.

## Heroku
Berikut merupakan link aplikasi Heroku yang sudah di *deploy*:
[https://tugas2-katalog.herokuapp.com/katalog/]

## Virtual environment

Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

The virtual environment merupakan environment yang digunakan Django mengeksekusi aplikasi. Ini direkomendasikan untuk membuat dan mengeksekusi sebuah Django application di dalam environment terpisah. Python menyediakan tool virtualenv untuk membuat isolated Python environment. Kita tetap dapat membuat aplikasi web berbasis Django tanpa virtualenv, namun lebih baik digunakan karena virtualenv berguna untuk mengatur Python packages untuk beberapa projects yang berbeda. Dengan menggunakan virtualenv, dapat menghindari installing Python packages globally yang bisa merusak system tools atau projects lain. Kita dapat menginstall virtualenv menggunakan perintah pip.

## Cara Mengimplementasi

Terdapat beberapa tahap yang perlu dilakukan dari awal hingga deploy ke Heroku, yaitu:
1. Bukalah [https://github.com/pbp-fasilkom-ui/assignment-repository] dan klik "use this template". Kemudian akan dialihkan ke halaman untuk membuat repository baru.
2. Isi nama repository, pastikan bersifat public, abaikan "Include all branches", dan klik "create repository from this template".
3. Setelah itu, buka terminal atau command prompt untuk clone repository ke komputer dengan menjalankan perintah git clone <URL_REPOSITORY>.
4. Masuk ke dalam direktori dan buat sebuah *virtual environment* dengan menjalankan perintah berikut pada terminal atau command prompt ```shell python -m venv env ```
5. Nyalakan *virtual environment* dengan menjalankan perintah pada Linux/Mac OS 
```shell 
Unix (Linux & Mac OS):
source env/bin/activate
```
4. Dalam direktori terdapat views.py yang perlu ditambahkan fungsi untuk mengambil data dari model dan dikembalikan ke dalam sebuah html. Memetakan data yang didapatkan dari models.py ke HTML.
```shell 
from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_catalog(request):
    data_katalog = CatalogItem.objects.all()
    context = {
        'list_katalog': data_katalog,
        'nama': 'Soraya Sabrina',
        'npm': '2106651061',
    }
    return render(request, "katalog.html", context)
```
5. Menambahkan path ```shell ('katalog/', include('katalog.urls')),``` ke urls.py yang ada di dalam folder project_django. Setelah itu, akan routing ke urls.py dalam folder katalog. Maka perlu menambahkan 
```shell 
from django.urls import path
from katalog.views import show_catalog

app_name = 'katalog'

urlpatterns = [
    path('', show_catalog, name='show_catalog'),
]
```
6. Membuka katalog.html dan ubah Fill me! yang ada di dalam HTML tag <p> menjadi {{nama}} untuk menampilkan nama kamu di halaman HTML.
7. Untuk menampilkan katalog ke dalam table, iterasi beberapa variable yang ada di models.py. Contohnya adalah sebagai berikut:
```shell
<table>
    <tr>
      <th>Item Name</th>
      <th>Item Price</th>
      <th>Item Stock</th>
      <th>Rating</th>
      <th>Description</th>
      <th>Item URL</th>
    </tr>
    {% comment %} Add the data below this line {% endcomment %}
    {% for katalog in list_katalog %}
    <tr>
      <th>{{katalog.item_name}}</th>
      <th>{{katalog.item_price}}</th>
      <th>{{katalog.item_stock}}</th>
      <th>{{katalog.rating}}</th>
      <th>{{katalog.description}}</th>
      <th>{{katalog.item_url}}</th>
  </tr>
  {% endfor %}
  </table>
 ```
8. Install *depedencies* yang diperlukan dengan menjalankan perintah ```shell pip install <NAMA_DEPEDENCIES>```.
9. Simpan daftar *depedencies* ke dalam txt file dengan menjalankan perintah ```shell pip freeze > requirements.txt ```
10. Create new app pada Heroku.
11. Salin API Key dari akun kamu. API Key dapat kamu temukan di ```shell Account Settings -> API Key```. Simpanlah API Key beserta informasi tentang aplikasi Heroku kamu pada file teks dengan format berikut:
```shell
HEROKU_API_KEY: <VALUE_API_KEY_ANDA>
HEROKU_APP_NAME: <NAMA_APLIKASI_HEROKU_ANDA>
```
12. Buka konfigurasi repositori GitHub dan buka bagian Secrets untuk GitHub Actions. Simpan API key dan nama aplikasi di teks filex. 
13. Tambahkan variabel repository secret baru untuk melakukan deployment. Pasangan Name-Value dari variabel yang akan dibuat dapat diambil dari informasi yang dicatat pada file teks sebelumnya. Contohnya adalah sebagai berikut.
14. Lakukan perintah python manage.py makemigrations untuk mempersiapkan migrasi skema model ke dalam database Django lokal.
15. Menjalankan perintah python manage.py migrate untuk menerapkan skema model yang telah dibuat ke dalam database Django lokal.
16. Menjalankan perintah python manage.py loaddata initial_catalog_data.json untuk memasukkan data tersebut ke dalam database Django lokal.
17. Mencoba proyek dengan menjalankan python manage.py runserver di Windows atau ./manage.py runserver di OS berbasis Unix. Pastikan manage.py aktif pada shell saat ini.
18. Buka http://localhost:8000 dan akan terdapat roket meluncur yang menandakan berhasil.
19. Setelah itu, kita akan deploy ke Heroku. Mula-mula pastikan terdapat dpl.yml dalam folder .github/workflows.
20. Mengecek Procfile untuk memastikan setelah realease dilakukan migrate dan loaddata
21. Jalankan perintah python manage.py makemigrations.
22. Jalankan perintah add, commit, push perubahan ke dalam GitHub.
23. Buka tab GitHub Actions di repository, tunggu beberapa saat, dan status deployment akan berubah menjadi success. 
24. Sekarang aplikasi dapat diakses melalui ```shell https://tugas2-katalog.herokuapp.com/katalog ```


# Template Proyek Django PBP

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

*Read this in other languages: [Indonesian](README.md), [English](README.en.md)*

## Pendahuluan

Repositori ini merupakan sebuah template yang dirancang untuk membantu mahasiswa yang sedang mengambil mata kuliah Pemrograman Berbasis Platform (CSGE602022) mengetahui struktur sebuah proyek aplikasi Django serta file dan konfigurasi yang penting dalam berjalannya aplikasi. Kamu dapat dengan bebas menyalin isi dari repositori ini atau memanfaatkan repositori ini sebagai pembelajaran sekaligus awalan dalam membuat sebuah proyek Django.

## Cara Menggunakan

Apabila kamu ingin menggunakan repositori ini sebagai repositori awalan yang nantinya akan kamu modifikasi:

1. Buka laman GitHub repositori templat kode, lalu klik tombol "**Use this template**"
   untuk membuat salinan repositori ke dalam akun GitHub milikmu.
2. Buka laman GitHub repositori yang dibuat dari templat, lalu gunakan perintah
   `git clone` untuk menyalin repositorinya ke suatu lokasi di dalam sistem
   berkas (_filesystem_) komputermu:

   ```shell
   git clone <URL ke repositori di GitHub> <path ke suatu lokasi di filesystem>
   ```
3. Masuk ke dalam repositori yang sudah di-_clone_ dan jalankan perintah berikut
   untuk menyalakan _virtual environment_:

   ```shell
   python -m venv env
   ```
4. Nyalakan environment dengan perintah berikut:

   ```shell
   # Windows
   .\env\Scripts\activate
   # Linux/Unix, e.g. Ubuntu, MacOS
   source env/bin/activate
   ```
5. Install dependencies yang dibutuhkan untuk menjalankan aplikasi dengan perintah berikut:

   ```shell
   pip install -r requirements.txt
   ```

6. Jalankan aplikasi Django menggunakan server pengembangan yang berjalan secara
   lokal:

   ```shell
   python manage.py runserver
   ```
7. Bukalah `http://localhost:8000` pada browser favoritmu untuk melihat apakah aplikasi sudah berjalan dengan benar.

## Contoh Deployment 

Pada template ini, deployment dilakukan dengan memanfaatkan GitHub Actions sebagai _runner_ dan Heroku sebagai platform Hosting aplikasi. 

Untuk melakukan deployment, kamu dapat melihat instruksi yang ada pada [Tutorial 0](https://pbp-fasilkom-ui.github.io/ganjil-2023/assignments/tutorial/tutorial-0).

Untuk contoh aplikasi Django yang sudah di deploy, dapat kamu akses di [https://django-pbp-template.herokuapp.com/](https://django-pbp-template.herokuapp.com/)

## Credits

Template ini dibuat berdasarkan [PBP Ganjil 2021](https://gitlab.com/PBP-2021/pbp-lab) yang ditulis oleh Tim Pengajar Pemrograman Berbasis Platform 2021 ([@prakashdivyy](https://gitlab.com/prakashdivyy)) dan [django-template-heroku](https://github.com/laymonage/django-template-heroku) yang ditulis oleh [@laymonage, et al.](https://github.com/laymonage). Template ini dirancang sedemikian rupa sehingga mahasiswa dapat menjadikan template ini sebagai awalan serta acuan dalam mengerjakan tugas maupun dalam berkarya.