1.	Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)! <br />
•	Membuat sebuah proyek Django baru. <br />
•	Cara: Pertama, buat direktori baru dengan nama “gudangku”, sesuai dengan nama aplikasi diinginkan. Lalu aktifkan virtual environment yang bertujuan untuk mengisolasi package dan dependencies dari aplikasi sehingga tidak bertabrakan dengan versi lain yang ada di komputer. Kedua, siapkan dependencies dengan menginstallnya, lalu buat proyek Django dengan perintah “django-admin startproject gudangku .”. Ketiga, konfigurasi proyek dengan mengisi ALLOWED_HOSTS dengan “*” lalu terakhir jalankan servernya.
•	Membuat aplikasi dengan nama main pada proyek tersebut.
•	Cara: Menjalankan perintah “python manage.py startapp main” pada command prompt lalu mendaftarkan aplikasi main ke dalam  proyek dengan cara menambahkan ‘main’ ke dalam daftar aplikasi yang ada (INSTALLED_APPS).
•	Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
•	Cara: Pertama, impor fungsi include dari django.urls pada berkas urls.py yang ada di direktori proyek gudangku. Kedua, tambahkan rute URL “path('main/', include('main.urls')),” pada variabel urlpatterns. Selanjutnya coba jalankan proyek Django dengan perintah “python manage.py runserver” dan buka local host (http://localhost:8000/main/) untuk mengecek halaman yang telah dibuat, jangan lupa tambahkan /main di akhir address untuk dapat menuju ke halaman yang dibuat.
•	Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib sebagai berikut.
o	name sebagai nama item dengan tipe CharField.
o	amount sebagai jumlah item dengan tipe IntegerField.
o	description sebagai deskripsi item dengan tipe TextField.
•	Cara: Pertama, buka berkas models.py pada direktori aplikasi main, lalu isi berkas dengan function yang menerima argumen models.Model dengan atribut name, amount, dan description sesuai tipe data pada soal. Kedua, jangan lupa untuk melakukan migrasi setiap kali mengubah model, yaitu dengan menjalankan “python manage.py makemigrations” lalu “python manage.py migrate” pada command prompt.
•	Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
•	Cara: Pertama, buka berkas views.py yang ada di dalam berkas aplikasi main. Selanjutnya, impor render dari django.shortcuts. Lalu tambahkan fungsi show_main yang menerima parameter request dan mereturn “render(request, "main.html", context)”, dimana context merupakan dictionary dengan key adalah variabel dan valuenya adalah isi dari variabel tersebut, seperti {‘nama’: ‘Mario’, ...}. Terakhir, isi template main.html pada direktori templates di main dengan kode HTML yang menampilkan data dari dictionary context yang sudah dibuat sebelumnya, namun buat agar menjadi dinamis (penggunaan nama langsung diganti dengan variabel).
•	Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
•	Cara: Pertama, buat berkas urls.py dalam direktori main. Selanjutnya, isi urls.py dengan mengimpor path dari django.urls dan show_main dari main.views. Lalu buat variabel app_name yang diisi dengan ‘main’, bertujuan untuk memberikan nama unik pada pola URL dalam aplikasi. Terakhir, buat list urlpatterns yang berisi daftar path yang akan di-handle oleh aplikasi web Django, dapat ditulis “path('', show_main, name='show_main'),”. Dimana show_main digunakan sebagai tampilan yang akan ditampilkan ketika URL diakses.
•	Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
•	Cara: Pertama, buat repositori baru pada akun GitHub (karena saya sudah mengatur akun Email dan lain-lain sebelumnya, jadi tidak perlu mulai dari awal lagi). Selanjutnya, hubungkan repositori lokal dengan repositori di GitHub dengan cara menjalankan perintah “git branch -M main” untuk membuat branch utama baru dengan nama main. Selanjutnya gunakan perintah “git remote add origin https://github.com/mariomichael/gudangku.git” untuk menghubungkan repository lokal dengan yang ada di GitHub. Selanjutnya, push kode yang telah dibuat ke GitHub. Untuk melakukan push, pertama lakukan git init (untuk menginisiasi direktori “gudangku” sebagai repositori Git) pada command prompt direktori gudangku (direktori yang akan dipush), lalu tambahkan berkas .gitignore yang digunakan untuk menentukan berkas dan direktori yang harus diabaikan oleh Git. Setelah itu gunakan “git add .” yang bertujuan untuk meng-add semua berkas yang ada. Setelah itu lakukan “git commit -m <pesan>” dimana pesan berupa deskripsi singkat atas perubahan yang dilakukan. Terakhir lakukan “git push -u origin <branch_utama>”, dimana dalam hal ini branch utamanya adalah main. Lakukan git add, commit, push setiap ada beberapa perubahan. Setelah itu buka web Adaptable (https://adaptable.io/). Klik “App Dashboard” lalu klik “+ NEW APP”. Pilih “Connect an Existing Repository”. Pilih mariomichael/gudangku. Selanjutnya pilih branch main. Untuk Deploy Template pilih Python App Template, Database Type pilih PostgreSQL, Python version pilih 3.11. Start command ubah ke “python manage.py migrate && gunicorn gudangku.wsgi”. Selanjutnya masukkan nama aplikasi yang akan menjadi nama domain situs web, dalam hal ini “gudangku”. Centang bagian HTTP Listener on Port dan klik Deploy App, maka app akan terdeploy.
•	Membuat sebuah README.md yang berisi tautan menuju aplikasi Adaptable yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut.
•	Cara: Tambahkan file README.md baru pada folder gudangku. Jawab semua pertanyaan, lalu lakukan git add, commit, dan push.

2.	Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

![Bagan request ke client dan hubungan antarelemen](foto2.jpeg)

3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Virtual environment digunakan untuk mengisolasi package dan dependencies dari setiap aplikasi yang kita bangun sehingga terhindar dari konflik dengan versi lain aplikasi yang ada di komputer kita. Selain itu virtual environment juga memudahkan proyek untuk dikelola karena kita bisa mengaktifkan dan menonaktifkan virtual environment. Kerusakan yang tidak disengaja pada suatu environment juga tidak akan memengaruhi environment lain sehingga keselamatan proyek lebih terjaga. Dengan virtual environment juga kita dapat dengan mudah mencatat dependencies proyek dalam sebuah file, sehingga memudahkan kita untuk mengulang proyek dengan konfigurasi yang sama di masa depan.

Ya, sebenarnya kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment karena virtual environment lebih ditujukan untuk mengantisipasi segala masalah yang bisa terjadi pada proyek yang kita kerjakan, bukan merupakan syarat untuk berjalannya sebuah proyek Django. Namun tetap lebih baik menggunakan virtual environment untuk menghindari masalah-masalah di atas, terutama menghindari konflik package dengan versi yang berbeda dan menjaga dependensi. Selain itu akan lebih sulit untuk mengembangkan dan menguji proyek yang kita buat.

4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

a.	MVC (Model-View-Controller)
MVC adalah sebuah pola desain arsitektur yang memisahkan sebuah aplikasi menjadi tiga komponen logika utama, yaitu model, view, dan controller. Penggunaan MVC bersifat lebih umum dan tidak terbatas pada pengembangan web, bisa giunakan untuk pengembangan desktop dan aplikasi seluler. View akan mengirim request ke controller, lalu controller merender view, controller akan memanipulasi model dan view juga akan menampilkan model.
•	Model bertanggung jawab untuk mengurus data dan logika, model juga berisi informasi dan metode untuk memanipulasi data.
•	View bertanggung jawab untuk menampilkan data kepada pengguna dari informasi yang diberikan model.
•	Controller bertanggung jawab untuk mengelola alur logika aplikasi dan interaksi pengguna serta mengontrol model untuk memutuskan tampilan mana yang harus ditampilkan.
b.	MVT (Model-View-Template)
MVT adalah sebuah konsep arsitektur yang digunakan dalam pengembangan web untuk memisahkan komponen-komponen utama dari sebuah aplikasi menjadi beberapa bagian, yaitu model, view, dan template. Konsep ini membuat kode menjadi lebih terstuktur dan terorganisir.
•	Model adalah komponen yang bertanggung jawab untuk mengatur dan mengelola data dari aplikasi. Model mewakili struktur data dan logika yang berada di belakang tampilan. Model menghubungkan aplikasi dengan basis data dan mengatur interaksinya.
•	View adalah komponen yang bertanggung jawab untuk menangani logika presentasi dalam konsep MVT. View mengatur bagaimana data yang sebelumnya sudah dikelola oleh model akan ditampilkan. Jadi peran view adalah sebagai pengatur tampilan dan menyajikan data kepada pengguna yang diambil dari model.
•	Template adalah komponen yang bertanggung jawab untuk mengatur tampilan antarmuka pengguna. Template memisahkan kode HTML yang membangun tampilan web dari logika aplikasi. Jadi template berfungsi untuk merancang tampilan yang diisi dengan data yang disajikan view yang diambil dari model.
c.	MVVM (Model-View-ViewModel)
MVVM adalah sebuah pola arsitektur pembuatan aplikasi berbasis antarmuka pengguna (User Interface (UI)) yang berfokus pada pemisahan antara kode untuk logika bisnis dan tampilan aplikasi. MVVM terbagi atas beberapa layer, yaitu model, view, dan ViewModel.
•	Model adalah bagian yang bertanggung jawab untuk merepresentasikan data yang akan digunakan pada logika bisnis.
•	View adalah bagian yang berisi UI dari aplikasi untuk mengatur bagaimana informasi akan ditampilkan sekaligus menampilkan informasi tersebut.
•	ViewModel adalah bagian yang bertanggung jawab untuk berinteraksi dengan model dimana data yang ada akan diteruskan ke view. ViewModel mengubah data dari model agar cocok dengan format yang bisa digunakan view untuk mengelola logika tampilan. Bagian ini memungkinkan pengikatan dan pemisahan data yang kuat antara tampilan dan logika aplikasi.

Perbedaan dari ketiganya adalah View pada MVT bertugas untuk menangani logika presentasi pada aplikasi, sedangkan View pada MVC dan MVVM bertugas untuk menampilkan data kepada pengguna yang diambil dari model (sebagai tampilan data). Selain itu perbedaan ketiganya terdapat pada bagian controller pada MVC, template pada MVT, dan ViewModel pada MVVM. Controller bertugas untuk mengatur alur logika aplikasi dan mengelola input pengguna, template digunakan untuk presentasi/menampilkan data kepada pengguna, dan ViewModel digunakan untuk mengelola dari dari model dan mengubahnya menjadi format yang sesuai tampilan, juga memiliki logika tambahan untuk tampilan. 