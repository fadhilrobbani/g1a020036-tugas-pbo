# TUGAS MATA KULIAH PEMROGRAMAN BERBASIS OBJEK

- Nama: Fadhilla Ilham Robbani
- NPM : G1A020036
- Kelas : B
- Link sololearn python intermediete: https://www.sololearn.com/certificates/CC-E690XXOC

## Perbedaan Functional Programming dan Object Oriented Programming

OOP (Object-Oriented Programming) dan FP (Functional Programming) adalah paradigma pemrograman yang berbeda. Pada OOP, program didefinisikan dalam bentuk objek yang dapat memiliki atribut dan metode, sementara pada FP, program didefinisikan dalam bentuk fungsi yang tidak memiliki efek samping dan menghasilkan nilai kembali. OOP berfokus pada objek dan hubungan antar objek, sedangkan FP berfokus pada komputasi dan transformasi data. OOP menggunakan konsep pewarisan dan pengkapsulan, sedangkan FP menggunakan konsep fungsi tingkat tinggi dan rekursi. OOP biasanya digunakan dalam pengembangan aplikasi berorientasi data, sementara FP lebih sering digunakan dalam pengolahan data dan analisis algoritma.

### Functional Programming

Functional programming adalah paradigma pemrograman yang memperlakukan fungsi sebagai objek yang independen, dan menekankan pada komputasi yang deklaratif dan immutable (tidak dapat diubah). Dalam functional programming, fungsi diperlakukan seperti nilai-nilai lainnya, dapat diberikan sebagai argumen ke fungsi lainnya, atau dijadikan sebagai nilai kembali dari suatu fungsi. Pada functional programming, kita perlu menggunakan pure function yaitu fungsi yang:

1.  Deterministik: Fungsi pure selalu mengembalikan nilai yang sama untuk input yang sama. Artinya, jika fungsi dipanggil dengan input tertentu, maka outputnya akan selalu sama tanpa memperhatikan konteks atau lingkungan program.
2.  Tanpa efek samping: Fungsi pure tidak menyebabkan efek samping pada lingkungan program, seperti mengubah variabel global atau menghasilkan keluaran ke perangkat keluaran. Fungsi pure hanya bergantung pada input dan tidak memiliki ketergantungan pada keadaan program atau lingkungan sekitarnya.

Contoh pure function:

```
def add(a, b):
    return a + b

```

> Fungsi di atas hanya bergantung pada inputnya, yaitu a dan b, dan selalu mengembalikan nilai yang sama jika dipanggil dengan input yang sama. Fungsi ini juga tidak memiliki efek samping pada lingkungan program, sehingga dapat dikatakan sebagai pure function.

Contoh yang bukan pure function:

```
my_list = []
def add_to_list(item):
    my_list.append(item)

```

> Fungsi di atas memiliki efek samping pada lingkungan program, yaitu menambahkan nilai ke dalam variabel global my_list, sehingga dapat dikatakan bukan pure function. Jika fungsi ini dipanggil dengan input yang sama, mungkin akan menghasilkan hasil yang berbeda karena efek samping pada my_list.

Contoh kode programnya tentang transaksi produk:

### Object Oriented Programming

OOP (Object-Oriented Programming) atau Pemrograman Berorientasi Objek adalah paradigma pemrograman yang berfokus pada konsep objek yang dapat diidentifikasi, memiliki sifat dan perilaku yang dapat didefinisikan, serta dapat berinteraksi dengan objek lain. OOP digunakan untuk memodelkan masalah dunia nyata dan memungkinkan untuk membuat program yang lebih kompleks dan mudah dimengerti. Python merupakan bahasa pemrograman yang mendukung OOP dan memiliki fitur-fitur berikut:

1.  Class: Class adalah blueprint atau cetakan dari suatu objek. Class dapat digunakan untuk membuat banyak objek dengan sifat dan perilaku yang sama. Suatu class memiliki atribut (variabel) dan metode (fungsi) yang dapat digunakan untuk mengakses dan memanipulasi objek dari class tersebut.
2.  Encapsulation: Encapsulation atau pengkapsulan adalah teknik OOP untuk menyembunyikan detail implementasi dari pengguna dan memungkinkan pengguna untuk mengakses objek hanya melalui metode yang disediakan oleh class. Hal ini dapat meningkatkan keamanan dan kesalahan yang mungkin terjadi pada program. Dalam Python, pengkapsulan dapat dilakukan dengan menandai atribut dan metode sebagai private menggunakan awalan karakter garis bawah ("\_"). Perlu di ingat, cara ini tidak sepenuhnya membuat suatu atribut bersifat private, tetapi lebih sebagai pengingat dan best practice saja.
3.  Inheritance: Inheritance atau pewarisan adalah teknik OOP untuk menurunkan sifat dan perilaku dari satu class ke class lain. Class yang diturunkan disebut subclass atau anak class, sedangkan class yang mewariskan disebut superclass atau induk class. Dalam Python, pewarisan dapat dilakukan dengan menuliskan nama superclass dalam tanda kurung setelah nama subclass. Contoh Employee(Person) artinya kelas Employee mewarisi dari kelas Person.
4.  Polymorphism: Polymorphism atau banyak bentuk adalah kemampuan suatu objek untuk memiliki banyak bentuk atau perilaku yang berbeda-beda dalam situasi yang berbeda. Polymorphism dapat dicapai melalui inheritance dan metode overriding atau overloading.
5.  Abstraction (Abstraksi): Konsep abstraksi memungkinkan untuk memfokuskan pada fitur penting dari suatu objek dan mengabaikan detail implementasi yang tidak penting.

Contoh kode programnya tentang transaksi produk:
