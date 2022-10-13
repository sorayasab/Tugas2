# Penjelasan Tugas 6
[Todolist App](https://tugas5-todolist.herokuapp.com/todolist)

## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
Cara kerja asynchronous yaitu input user meminta request ke server. Setelah request dijawab oleh server, tidak ada komunikasi lebih lanjut yang terjadi hingga input pengguna berikutnya (click, wait, refresh). Secara singkat, user harus menunggu sampai server generate dan send data. Sedangkan synchronous, user tetap bisa memberikan beberapa request walaupun request sebelumnya belum dijawab oleh server. Selagi server generate dan send data, server bisa memberikan beberapa request tambahan.

## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Event-Driven Programming merupakan suatu paradigma pemrograman dimana eksekusi program diatur oleh *user events* (mouse clicks, keypresses, sensor outputs, atau pesan yang disampaikan dari program lain). Event-drivent programming biasanya digunakan dalam *graphical user interfaces* atau aplikasi lainnya yang berfokus pada melakukan tindakan *user* sebagai respons terhadap *user input* (user clicks). Contohnya element.click() yang berfungsi sebagai metode untuk mensimulasikan *mouse-click* pada element. 

## Jelaskan penerapan asynchronous programming pada AJAX.
Penerapan asynchronous programming pada ajax memungkinkan website untuk tidak reload atau diperbaharui ketika terdapat perubahan data. Browser tidak perlu memperbaharui seluruh *page* untuk menampilkan data yang terbaru. Ajax akan menerima perintah dan mengirimkan ke server untuk mengubah data secara asynchronous. Dengan menggunakan AJAX get() dan post(), data akan di request dan diambil untuk ditampilkan ke server. Kemudian data yang diambil akan ditampilkan tanpa perlu memperbaharui page.
 
## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Membuat fungsi show_json untuk AJAX pada views.py.
2. Melakukan routing url pada urls.py /todolist/json dengan memanggil show_json.
3. Membuat fungsi add_todo pada views.py untuk mengembalikan seluruh data task dalam bentuk JSON.
4. Melakukan routing url pada urls.py /todolist/add dengan memanggil add_todo.
5. Import dan implementasi ajax pada html. 