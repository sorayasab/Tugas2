# Penjelasan Tugas 4
[Todolist App](https://tugas5-todolist.herokuapp.com/todolist)

## Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
**Inline CSS** merupakan kode CSS yang dituliskan langsung pada setiap tag yang akan didesain. Kelebihannya, yaitu fokus melihat perubahan pada satu element, memperbaiki kode dengan cepat, dan HTTP request lebih kecil dan load process akan lebih cepat. Kekurangannya, yaitu tidak efisien apabila terdapat lebih dari satu elemen dengan style yang sama. 
Contohnya dari Inline CSS adalah sebagai berikut:
```shell
<html>
<body style="background-color:beige">
<h1 style="color:white;font-family:sans-serif">Hostinger Tutorials</h1>
</body>
</html>
```
**Internal CSS** merupakan kode CSS yang ditulis di tag <style> dan berada didalam tag <head>. Kelebihannya, yaitu perubahan kode CSS terjadi pada satu halaman saja, tidak perlu upload beberapa file HTML dan CSS karena terjadi pada satu file HTML yang sama, class dan ID bisa digunakan. Kekurangannya, yaitu apabila menggunakan kode CSS yang sama dalam beberapa file HTML, maka hal ini menjadi tidak efisien, dan performa website menjadi lambat karena mengakibatkan load berulang kali ketika mengganti page. 
Contohnya adalah sebagai berikut:
```shell
<html>
<head>
  <style>
  </style>
</head>
</html>
```
**External CSS** merupakan kode CSS yang dituliskan diluar HTML dan Kode CSS akan dituliskan pada file khusus dengan ekstensi .css. Apabila menggunakan external css maka pastikan untuk menuliskan {% load static %} dan <link rel="stylesheet" href="{% static 'folder/filename.css' %}">. Kelebihannya, yaitu kode HTML menjadi rapi, ukuran file HTML lebih kecil, loading website lebih cepat, dan file CSS dapat digunakan sekaligus. Kekurangannya yaitu, page akan menjadi berantakan apabila file CSS gagal dipanggil oleh file HTML. 
Contohnya adalah sebagai berikut:
```shell
body{
    background: white;
}
```

## Jelaskan tag HTML5 yang kamu ketahui.
```<!DOCTYPE html>``` sebagai deklarasi file HTML.
```<html></html>``` sebagai root.
```<title></title>``` sebagai judul
```<body></body>``` sebagai isi yang akan ditampilkan. 
```<style></style>``` untuk menambahkan desain pada elemen, seperti font-size, font-family, dan color.
```<head></head>``` sebagai informasi awal dokumen, biasanya berisi nama penulis, judul dokumen dan keywords. 
```<p></p>``` untuk membuat paragraf.
```<table></table>``` untuk membuat table.

## Jelaskan tipe-tipe CSS selector yang kamu ketahui.
id = memilih elemen berdasarkan id, id yang dimiliki tiap elemen tentu berbeda-beda.
class = memilih seluruh elemen yang berada pada class yang sama.
element = memilih berdasarkan <element> saja.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Menambahkan ```{% load static %}``` pada awal line tiap file HTML yang akan diberikan CSS style.
2. Menambahkan <link rel="stylesheet" href="{% static 'todolist/namefile.css' %}"> sesuai dengan kode CSS yang diberikan.
3. Menambahkan syle pada file css sesuai dengan kebutuhan dan keinginan. 
4. Jalankan perintah http://localhost:8000/todolist/ untuk preview dan pastikan untuk menyalakan virtual environment. 
5. Git add, commit, dan push. 
