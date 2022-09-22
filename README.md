# Penjelasan Tugas 3
## Perbedaan JSON, XML, dan HTML
![Image Link](https://github.com/sorayasab/Tugas2/blob/main/Images/difference.jpg)

## Heroku
Berikut merupakan link aplikasi Heroku yang sudah di *deploy*:
https://tugas3-mywatchlist.herokuapp.com/mywatchlist/json/
https://tugas3-mywatchlist.herokuapp.com/mywatchlist/xml/
https://tugas3-mywatchlist.herokuapp.com/mywatchlist/html/

## Data Delivery

Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery merupakan teknologi yang mengizinkan kita untuk pengumpulan data, diubah, disatukan, dan dikirim ke *user*, aplikasi, atau *platform*. Bagian penting dari *digital transformation* adalah mengembangkan strategi data yang akan digunakan bisnis, lebih khusus lagi, bagaimana data dikumpulkan, diamankan, diatur, dan (yang paling penting) digunakan untuk meningkatkan kinerja bisnis. Oleh karena itu, data delivery merupakan hal yang sangat penting. Namun, memerlukan metode *data delivery* yang sesuai karena data yang dikirim atau diterima dapat berbeda-beda.

## Cara Mengimplementasi

Terdapat beberapa tahap yang perlu dilakukan dari awal hingga deploy ke Heroku, yaitu:

1. Masuk ke dalam direktori dan buat sebuah *virtual environment* dengan menjalankan perintah berikut pada terminal atau command prompt ```python -m venv env ```

2. Nyalakan *virtual environment* dengan menjalankan perintah pada Linux/Mac OS 
```shell 
Unix (Linux & Mac OS):
source env/bin/activate
```

3. Install *depedencies* yang diperlukan dengan menjalankan perintah ```shell pip install <NAMA_DEPEDENCIES>```.

4. Simpan daftar *depedencies* ke dalam txt file dengan menjalankan perintah ```shell pip freeze > requirements.txt ``

5. Buatlah django app dengan nama mywatchlist dengan menjalankan perintah ```manage.py startapp mywatchlist```

6. Buka settings.py di folder project_django dan tambahkan aplikasi mywatchlist ke dalam variabel INSTALLED_APPS untuk mendaftarkan django-app yang sudah kamu buat ke dalam proyek Django-mu. Contohnya adalah sebagai berikut.
```shell 
INSTALLED_APPS = [
    ...,
    'mywatchlist',
]
```

7. Menambahkan path mywatchlist pada urls.py dalam folder project_django 
```shell 
urlpatterns = [
    ...,
    path('mywatchlist/', include('mywatchlist.urls')),
]
```

8. Mengimplementasikan models.py yang berisikan informasi mengenai watched, time, rating, release_date, dan review
```shell
from django.db import models

class MyWatchListItem(models.Model):
    watched = models.BooleanField()
    title = models.CharField(max_length=255)
    rating = models.IntegerField()
    release_date = models.CharField(max_length=255)
    review = models.TextField()
```

9. Mengimplementasi views.py yang ada di folder mywatchlist, seperti berikut
```shell 
from django.shortcuts import render
from mywatchlist.models import MyWatchListItem
from django.http import HttpResponse
from django.core import serializers

def show_watchlist(request):
    return render(request, "mywatchlist.html", context)

data_tontonan = MyWatchListItem.objects.all()
context = {
    'list_tontonan': data_tontonan,
    'nama': 'Soraya Sabrina',
    'npm': '2106651061',
}

def show_xml(request):
    data = MyWatchListItem.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchListItem.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_html(request):
    data_tontonan = MyWatchListItem.objects.all()
    contextHTML = {
            'list_tontonan': data_tontonan
        }
    return render(request, 'watchedlist.html', contextHTML)

def show_xml_by_id(request, id):
    data = MyWatchListItem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = MyWatchListItem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

10. Menambahkan path ``` ('mywatchlist/', include('mywatchlist.urls')),``` ke urls.py yang ada di dalam folder project_django. Setelah itu, akan routing ke urls.py dalam folder mywatchlist. Maka perlu menambahkan sebagai berikut.
```shell
from django.urls import path
from mywatchlist.views import show_watchlist
from mywatchlist.views import show_xml
from mywatchlist.views import show_xml_by_id
from mywatchlist.views import show_json
from mywatchlist.views import show_json_by_id
from mywatchlist.views import show_html

app_name = 'MyWatchList'

urlpatterns = [
    path('', show_watchlist, name='show_watchlist'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('html/', show_html, name='show_html'),
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
]
```

11. Buat folder bernama fixtures dan buat initial_mywatchlist_data.json dan memasukkan 10 data mengenai watched, time, rating, release_date, dan review

12. Buatlah folder bernama templates dan buat mywatchlist.html dan watchedlist.html

13. Menambahkan unit test pada tests.py untuk menguji bahwa tiga URL dapat mengembalikan respon HTTP 200 OK

11. Lakukan perintah python manage.py makemigrations untuk mempersiapkan migrasi skema model ke dalam database Django lokal.

12. Menjalankan perintah python manage.py migrate untuk menerapkan skema model yang telah dibuat ke dalam database Django lokal.

13. Menjalankan perintah python manage.py loaddata initial_mywatchlist_data.json untuk memasukkan data tersebut ke dalam database Django lokal.

14. Mencoba proyek dengan menjalankan python manage.py runserver di Windows atau ./manage.py runserver di OS berbasis Unix. Pastikan manage.py aktif pada shell saat ini.

15. Buka http://localhost:8000/json, http://localhost:8000/xml, http://localhost:8000/html dan akan terdapat tampilan beserta datanya.

16. Create new app pada Heroku.

11. Salin API Key dari akun kamu. API Key dapat kamu temukan di ```shell Account Settings -> API Key```. Simpanlah API Key beserta informasi tentang aplikasi Heroku kamu pada file teks dengan format berikut:
```shell
HEROKU_API_KEY: <VALUE_API_KEY_ANDA>
HEROKU_APP_NAME: <NAMA_APLIKASI_HEROKU_ANDA>
```

12. Buka konfigurasi repositori GitHub dan buka bagian Secrets untuk GitHub Actions. Simpan API key dan nama aplikasi di teks file. 

13. Tambahkan variabel repository secret baru untuk melakukan deployment. Pasangan Name-Value dari variabel yang akan dibuat dapat diambil dari informasi yang dicatat pada file teks sebelumnya. Contohnya adalah sebagai berikut.

16. Jalankan perintah add, commit, push perubahan ke dalam GitHub.

23. Buka tab GitHub Actions di repository, tunggu beberapa saat, dan status deployment akan berubah menjadi success. 

## Screenshot Postman
1. JSON
![Image Link](https://github.com/sorayasab/Tugas2/blob/main/Images/json.png)

2. XML
![Image Link](https://github.com/sorayasab/Tugas2/blob/main/Images/xml.png)

3. HTML 
![Image Link](https://github.com/sorayasab/Tugas2/blob/main/Images/html.png)