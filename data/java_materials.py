JAVA_MATERIALS = [
    {
        "title": "1. Pengenalan Java & Persiapan",
        "sections": [
            {
                "body": [
                    "Apa itu Java?",
                    "  - Java adalah bahasa pemrograman berorientasi objek (OOP).",
                    "  - Dibuat oleh James Gosling di Sun Microsystems (1995).",
                    "  - Slogannya: 'Write Once, Run Anywhere' (WORA).",
                    "  - Kode Java dikompilasi menjadi bytecode yang dijalankan",
                    "    oleh Java Virtual Machine (JVM).",
                    "",
                    "Komponen yang perlu kamu tahu:",
                    "  1. JDK (Java Development Kit)  -> untuk menulis & menjalankan kode.",
                    "  2. JRE (Java Runtime Environment) -> untuk menjalankan aplikasi Java.",
                    "  3. JVM (Java Virtual Machine)   -> mesin yang menjalankan bytecode.",
                    "",
                    "Cara instalasi (pilih salah satu):",
                    "  - Windows/Mac/Linux: download dari https://adoptium.net (OpenJDK).",
                    "  - Cek instalasi dengan perintah:  java -version",
                    "",
                    "Menulis program pertama:",
                    "  1. Buat file bernama Hello.java (nama file HARUS sama dengan nama class).",
                    "  2. Tulis kodenya (lihat contoh di bawah).",
                    "  3. Kompilasi:  javac Hello.java",
                    "  4. Jalankan:    java Hello",
                    "",
                    "Struktur dasar program Java:",
                    "  - Setiap program butuh method main sebagai titik masuk.",
                    "  - Java bersifat case-sensitive: Hello beda dengan hello.",
                ]
            },
            {
                "heading": "Program pertama",
                "code": """public class Hello {
    public static void main(String[] args) {
        System.out.println("Halo Dunia!");
    }
}"""
            },
            {
                "body": [
                    "Penjelasan baris per baris:",
                    "  public class Hello  -> deklarasi class bernama Hello.",
                    "  public static void main(String[] args) -> method utama.",
                    "      - public    : bisa diakses dari mana saja.",
                    "      - static    : dipanggil tanpa membuat objek.",
                    "      - void      : tidak mengembalikan nilai.",
                    "      - String[] args : argumen dari baris perintah.",
                    "  System.out.println(\"Halo Dunia!\") -> mencetak teks + baris baru.",
                    "  Setiap statement di Java diakhiri titik koma (;).",
                    "  Setiap blok { } menandakan awal/akhir dari sebuah bagian.",
                ]
            },
        ],
    },
    {
        "title": "2. Variabel & Tipe Data",
        "sections": [
            {
                "body": [
                    "Variabel = 'kotak' penyimpan data. Setiap variabel punya tipe data.",
                    "",
                    "Tipe data primitif di Java:",
                    "  Tipe     Ukuran   Rentang nilai",
                    "  ------   ------   --------------------------------",
                    "  byte     1 byte   -128 s/d 127",
                    "  short    2 byte   -32.768 s/d 32.767",
                    "  int      4 byte   -2^31 s/d 2^31-1 (paling umum)",
                    "  long     8 byte   -2^63 s/d 2^63-1",
                    "  float    4 byte   bilangan desimal",
                    "  double   8 byte   bilangan desimal presisi ganda",
                    "  char     2 byte   satu karakter ('A', '1', '@')",
                    "  boolean  1 bit    true atau false",
                    "",
                    "Tipe data referensi:",
                    "  - String: kumpulan karakter (\"Halo\").",
                    "  - Array, Class, Interface (dipelajari nanti).",
                    "",
                    "Deklarasi variabel:",
                    "  tipeData namaVariabel = nilai;",
                ]
            },
            {
                "heading": "Contoh deklarasi variabel",
                "code": """int umur = 20;
double harga = 15000.50;
char grade = 'A';
boolean lulus = true;
String nama = "Budi";
long saldoBank = 1000000000L;  // akhiri L untuk long
float tinggi = 170.5f;         // akhiri f untuk float"""
            },
            {
                "body": [
                    "Konstanta (nilai tetap): pakai kata kunci final.",
                    "  final double PI = 3.14;",
                    "  PI = 3.0;  // ERROR! tidak bisa diubah",
                    "",
                    "Aturan penamaan variabel:",
                    "  1. Boleh huruf, angka, _ dan $. Tidak boleh diawali angka.",
                    "  2. Tidak boleh memakai kata kunci Java (int, class, if, dll).",
                    "  3. Ikuti konvensi camelCase untuk variabel: jumlahMahasiswa.",
                    "  4. Nama harus deskriptif supaya mudah dibaca.",
                    "",
                    "Type inference (Java 10+): pakai kata kunci var.",
                    "  var nama = \"Andi\";   // otomatis dianggap String",
                    "  var angka = 10;       // otomatis dianggap int",
                    "",
                    "Konversi tipe data:",
                    "  - Widening (otomatis): int -> long -> double",
                    "  - Narrowing (manual):  (int) 3.99 hasilnya 3",
                    "    int x = (int) 3.99;   // x = 3",
                ]
            },
        ],
    },
    {
        "title": "3. Operator",
        "sections": [
            {
                "body": [
                    "Operator aritmatika:",
                    "  +  penjumlahan      a + b",
                    "  -  pengurangan      a - b",
                    "  *  perkalian        a * b",
                    "  /  pembagian        a / b",
                    "  %  sisa bagi        a % b (modulus)",
                    "  ++ increment (naik 1)   -- decrement (turun 1)",
                    "",
                    "Catatan penting tentang pembagian:",
                    "  7 / 2  = 3   (int / int = int, sisa dibuang)",
                    "  7.0 / 2 = 3.5 (float / double = desimal)",
                    "  7 % 2  = 1   (sisa pembagian)",
                    "",
                    "Operator penugasan (assignment):",
                    "  =   x = 5    ->  x menjadi 5",
                    "  +=  x += 3   ->  x = x + 3",
                    "  -=  x -= 3   ->  x = x - 3",
                    "  *=  x *= 3   ->  x = x * 3",
                    "  /=  x /= 3   ->  x = x / 3",
                    "  %=  x %= 3   ->  x = x % 3",
                ]
            },
            {
                "body": [
                    "Operator perbandingan (hasilnya boolean):",
                    "  ==  sama dengan      a == b",
                    "  !=  tidak sama       a != b",
                    "  >   lebih besar      a > b",
                    "  <   lebih kecil      a < b",
                    "  >=  lebih besar sama a >= b",
                    "  <=  lebih kecil sama a <= b",
                    "",
                    "Operator logika:",
                    "  &&  DAN (keduanya true baru true)",
                    "  ||  ATAU (salah satu true jadi true)",
                    "  !   NEGASI (membalik nilai)",
                    "",
                    "Contoh:",
                    "  (5 > 3) && (2 > 1)  -> true",
                    "  (5 > 3) && (2 > 5)  -> false",
                    "  (5 > 3) || (2 > 5)  -> true",
                    "  !(5 > 3)            -> false",
                    "",
                    "Urutan prioritas operator (dari tertinggi):",
                    "  1. ()  ekspresi dalam kurung",
                    "  2. * / %",
                    "  3. + -",
                    "  4. perbandingan",
                    "  5. &&",
                    "  6. ||",
                    "  Selalu gunakan kurung agar tidak bingung!",
                ]
            },
            {
                "heading": "Contoh penggunaan operator",
                "code": """int a = 10, b = 3;
System.out.println(a + b);   // 13
System.out.println(a - b);   // 7
System.out.println(a * b);   // 30
System.out.println(a / b);   // 3
System.out.println(a % b);   // 1
System.out.println(a++);     // 10 (tampil dulu, baru naik)
System.out.println(++a);     // 12 (naik dulu, baru tampil)"""
            },
        ],
    },
    {
        "title": "4. Percabangan (if / switch)",
        "sections": [
            {
                "body": [
                    "Percabangan membuat program mengambil keputusan.",
                    "",
                    "if - else if - else:",
                    "  if (kondisi) {",
                    "      // jalankan jika kondisi true",
                    "  } else if (kondisi2) {",
                    "      // jalankan jika kondisi2 true",
                    "  } else {",
                    "      // jalankan jika semua false",
                    "  }",
                    "",
                    "TIPS: Kondisi harus bernilai boolean.",
                    "      (x = 5) itu SALAH, yang benar (x == 5).",
                    "",
                    "Ternary operator (if satu baris):",
                    "  tipe nama = (kondisi) ? nilaiTrue : nilaiFalse;",
                    "  String hasil = (nilai >= 75) ? \"Lulus\" : \"Tidak Lulus\";",
                ]
            },
            {
                "heading": "Contoh if",
                "code": """int nilai = 85;
if (nilai >= 90) {
    System.out.println("A");
} else if (nilai >= 80) {
    System.out.println("B");
} else if (nilai >= 70) {
    System.out.println("C");
} else {
    System.out.println("D");
}
// Output: B"""
            },
            {
                "body": [
                    "switch - case: untuk membandingkan satu nilai dengan banyak pilihan.",
                    "",
                    "switch (ekspresi) {",
                    "    case nilai1:",
                    "        // kode",
                    "        break;",
                    "    case nilai2:",
                    "        // kode",
                    "        break;",
                    "    default:",
                    "        // jika tidak ada yang cocok",
                    "}",
                    "",
                    "Mulai Java 14, ada switch expression yang lebih ringkas:",
                    "  String hasil = switch (hari) {",
                    "      case 1 -> \"Senin\";",
                    "      case 2 -> \"Selasa\";",
                    "      default -> \"Lainnya\";",
                    "  };",
                    "",
                    "break penting! Tanpa break, semua case di bawahnya ikut dieksekusi",
                    "(disebut fall-through).",
                ]
            },
            {
                "heading": "Contoh switch",
                "code": """int hari = 3;
switch (hari) {
    case 1:
        System.out.println("Senin");
        break;
    case 2:
        System.out.println("Selasa");
        break;
    case 3:
        System.out.println("Rabu");
        break;
    default:
        System.out.println("Hari tidak valid");
}
// Output: Rabu"""
            },
        ],
    },
    {
        "title": "5. Perulangan (Loop)",
        "sections": [
            {
                "body": [
                    "Perulangan menjalankan kode berulang-ulang.",
                    "",
                    "1. for - dipakai saat jumlah perulangan sudah diketahui.",
                    "   for (awal; kondisi; update) {",
                    "       // kode diulang",
                    "   }",
                    "",
                    "2. while - dipakai saat jumlah tidak pasti, cek kondisi DULU.",
                    "   while (kondisi) {",
                    "       // kode",
                    "   }",
                    "",
                    "3. do-while - Dijalankan DULU, baru cek kondisi.",
                    "   do {",
                    "       // kode (pasti jalan minimal 1x)",
                    "   } while (kondisi);",
                    "",
                    "Kata kunci tambahan:",
                    "  break -> menghentikan perulangan langsung.",
                    "  continue -> melewati iterasi ini, lanjut ke berikutnya.",
                ]
            },
            {
                "heading": "Contoh for, while, do-while",
                "code": """// for: cetak 1-5
for (int i = 1; i <= 5; i++) {
    System.out.print(i + " ");
}
System.out.println();          // 1 2 3 4 5

// while: cetak 1-5
int j = 1;
while (j <= 5) {
    System.out.print(j + " ");
    j++;
}
System.out.println();          // 1 2 3 4 5

// do-while: pasti jalan minimal sekali
int k = 10;
do {
    System.out.println("k = " + k);
    k++;
} while (k < 3);               // k = 10"""
            },
            {
                "heading": "Contoh break dan continue",
                "code": """for (int i = 1; i <= 10; i++) {
    if (i == 5) continue;   // lewati 5
    if (i == 8) break;      // berhenti di 8
    System.out.print(i + " ");
}
// Output: 1 2 3 4 6 7"""
            },
            {
                "body": [
                    "Perulangan bersarang (nested loop):",
                    "  - Perulangan di dalam perulangan.",
                    "  - Sering dipakai untuk pola bintang atau tabel.",
                    "",
                    "Pola segitiga bintang:",
                    "  for (int i = 1; i <= 4; i++) {",
                    "      for (int j = 1; j <= i; j++) {",
                    "          System.out.print(\"*\");",
                    "      }",
                    "      System.out.println();",
                    "  }",
                    "  Output:",
                    "  *",
                    "  **",
                    "  ***",
                    "  ****",
                    "",
                    "For-each (enhanced for): untuk membaca semua elemen koleksi/array.",
                    "  for (int elemen : array) { ... }",
                    "  for (String nama : daftarNama) { ... }",
                ]
            },
        ],
    },
    {
        "title": "6. Array",
        "sections": [
            {
                "body": [
                    "Array = kumpulan data dengan tipe yang sama dan ukuran tetap.",
                    "",
                    "Deklarasi array:",
                    "  int[] angka = new int[5];          // array 5 int, isi default 0",
                    "  int[] angka = {1, 2, 3, 4, 5};     // langsung dengan nilai",
                    "  String[] nama = {\"Andi\", \"Budi\"};",
                    "",
                    "Mengakses elemen array:",
                    "  Indeks array DIMULAI dari 0.",
                    "  int[] angka = {10, 20, 30};",
                    "  angka[0] -> 10",
                    "  angka[1] -> 20",
                    "  angka[2] -> 30",
                    "",
                    "Panjang array:",
                    "  angka.length  -> 3",
                    "",
                    "PENTING: Indeks di luar batas menyebabkan error",
                    "ArrayIndexOutOfBoundsException.",
                    "  angka[3] -> ERROR!",
                ]
            },
            {
                "heading": "Contoh array",
                "code": """int[] nilai = {80, 90, 75, 85};

// cetak semua nilai
for (int i = 0; i < nilai.length; i++) {
    System.out.println("Indeks " + i + ": " + nilai[i]);
}

// hitung total & rata-rata
int total = 0;
for (int n : nilai) {          // for-each
    total += n;
}
double rata = (double) total / nilai.length;
System.out.println("Total: " + total);
System.out.println("Rata-rata: " + rata);
// Total: 330, Rata-rata: 82.5"""
            },
            {
                "body": [
                    "Array 2 dimensi (matriks):",
                    "  int[][] matriks = {",
                    "      {1, 2, 3},",
                    "      {4, 5, 6}",
                    "  };",
                    "  matriks[0][1] -> 2 (baris 0, kolom 1)",
                    "",
                    "  for (int[] baris : matriks) {",
                    "      for (int nilai : baris) {",
                    "          System.out.print(nilai + \" \");",
                    "      }",
                    "      System.out.println();",
                    "  }",
                    "  Output:",
                    "  1 2 3",
                    "  4 5 6",
                    "",
                    "ArrayList (dipelajari di Collection Framework):",
                    "  - Ukuran array bisa berubah (dinamis).",
                    "  - import java.util.ArrayList;",
                ]
            },
        ],
    },
    {
        "title": "7. Method (Fungsi)",
        "sections": [
            {
                "body": [
                    "Method = blok kode yang bisa dipanggil berulang-ulang.",
                    "Membantu menghindari kode yang duplikat.",
                    "",
                    "Sintaks method:",
                    "  tipeKembali namaMethod(parameter) {",
                    "      // isi method",
                    "      return nilai;   // jika tipeKembali bukan void",
                    "  }",
                    "",
                    "Contoh deklarasi:",
                    "  int tambah(int a, int b) {",
                    "      return a + b;",
                    "  }",
                    "  void sapa(String nama) {",
                    "      System.out.println(\"Halo, \" + nama);",
                    "  }",
                    "",
                    "Memanggil method:",
                    "  int hasil = tambah(3, 4);   // hasil = 7",
                    "  sapa(\"Andi\");               // Halo, Andi",
                ]
            },
            {
                "heading": "Contoh method lengkap",
                "code": """public class Kalkulator {
    public static void main(String[] args) {
        int hasil = tambah(10, 5);
        System.out.println("10 + 5 = " + hasil);
        tampilkanInfo("Java");
    }

    static int tambah(int a, int b) {
        return a + b;
    }

    static void tampilkanInfo(String bahasa) {
        System.out.println("Belajar " + bahasa + " itu seru!");
    }
}"""
            },
            {
                "body": [
                    "Method overloading: beberapa method dengan NAMA SAMA",
                    "tapi parameter BERBEDA.",
                    "",
                    "  int tambah(int a, int b) { return a + b; }",
                    "  int tambah(int a, int b, int c) { return a + b + c; }",
                    "  double tambah(double a, double b) { return a + b; }",
                    "",
                    "  tambah(1, 2)        -> memanggil yang 2 param",
                    "  tambah(1, 2, 3)     -> memanggil yang 3 param",
                    "  tambah(1.5, 2.5)    -> memanggil yang double",
                    "",
                    "Scope variabel:",
                    "  - Variabel di dalam method hanya dikenal di method itu (lokal).",
                    "  - Variabel yang sama boleh ada di method berbeda.",
                    "  - Parameter method bersifat lokal juga.",
                    "",
                    "Static method:",
                    "  - Dipanggil langsung tanpa membuat objek: Math.pow(2, 3).",
                    "  - Non-static butuh objek: kalkulator.tambah(1, 2).",
                ]
            },
        ],
    },
    {
        "title": "8. OOP: Class & Object",
        "sections": [
            {
                "body": [
                    "OOP = Object-Oriented Programming.",
                    "Pemrograman berbasis 'objek' yang menggabungkan data & perilaku.",
                    "",
                    "Class = cetakan (blueprint).",
                    "Object = hasil cetakan (instance) dari class.",
                    "",
                    "Contoh analogi:",
                    "  - Class 'Resep Kue' = blueprint.",
                    "  - Object 'Kue coklat' = hasil jadi dari resep itu.",
                    "",
                    "Bagian-bagian class:",
                    "  1. Attribute / field -> data (misal: nama, umur).",
                    "  2. Constructor        -> method khusus saat objek dibuat.",
                    "  3. Method             -> perilaku (misal: berjalan, bicara).",
                ]
            },
            {
                "heading": "Contoh class & object",
                "code": """class Mahasiswa {
    // attribute
    String nama;
    int umur;

    // constructor
    Mahasiswa(String nama, int umur) {
        this.nama = nama;
        this.umur = umur;
    }

    // method
    void perkenalan() {
        System.out.println("Halo, saya " + nama + ", " + umur + " tahun.");
    }
}

public class Main {
    public static void main(String[] args) {
        Mahasiswa m1 = new Mahasiswa("Andi", 20);
        Mahasiswa m2 = new Mahasiswa("Budi", 22);
        m1.perkenalan();
        m2.perkenalan();
    }
}"""
            },
            {
                "body": [
                    "Penjelasan:",
                    "  new Mahasiswa(...)  -> membuat objek baru.",
                    "  this.nama            -> merujuk attribute, bukan parameter.",
                    "  m1, m2               -> variabel referensi ke objek.",
                    "",
                    "Kata kunci penting:",
                    "  this  -> merujuk ke objek saat ini.",
                    "  new   -> membuat objek baru dari sebuah class.",
                    "  null  -> referensi yang belum menunjuk objek apa pun.",
                    "",
                    "Access modifier (tingkat akses):",
                    "  public    -> bisa diakses dari mana saja.",
                    "  private   -> hanya bisa diakses di dalam class yang sama.",
                    "  protected -> class yang sama + subclass + package sama.",
                    "  (tanpa)   -> package-private, hanya package sama.",
                    "",
                    "Aturan umum: attribute dibuat private, method dibuat public.",
                    "Itulah konsep Encapsulation (dipelajari selanjutnya).",
                ]
            },
        ],
    },
    {
        "title": "9. OOP: Encapsulation",
        "sections": [
            {
                "body": [
                    "Encapsulation = menyembunyikan data internal dan",
                    "memberi akses terkontrol lewat method (getter/setter).",
                    "",
                    "Manfaat:",
                    "  1. Data aman dari perubahan sembarangan.",
                    "  2. Bisa menambahkan validasi.",
                    "  3. Kode lebih mudah dirawat.",
                    "",
                    "Cara membuatnya:",
                    "  1. Buat attribute menjadi private.",
                    "  2. Sediakan getter untuk membaca.",
                    "  3. Sediakan setter untuk mengubah (dengan validasi).",
                ]
            },
            {
                "heading": "Contoh encapsulation",
                "code": """class Rekening {
    private String pemilik;
    private double saldo;

    public Rekening(String pemilik, double saldo) {
        this.pemilik = pemilik;
        this.saldo = saldo;
    }

    public String getPemilik() {
        return pemilik;
    }

    public double getSaldo() {
        return saldo;
    }

    public void setor(double jumlah) {
        if (jumlah > 0) {
            saldo += jumlah;
        }
    }

    public boolean tarik(double jumlah) {
        if (jumlah > 0 && jumlah <= saldo) {
            saldo -= jumlah;
            return true;
        }
        return false;
    }
}"""
            },
            {
                "body": [
                    "Catatan:",
                    "  saldo tidak bisa diubah sembarangan karena private.",
                    "  Semua perubahan lewat setor()/tarik() yang divalidasi.",
                    "  Ini mencegah saldo jadi negatif.",
                    "",
                    "Keuntungan getter/setter:",
                    "  - Bisa menambah logika (validasi, logging).",
                    "  - Bisa mengubah implementasi internal tanpa mengubah pemakai.",
                    "  - Format penamaan standar: getNama(), setNama(String nama).",
                ]
            },
        ],
    },
    {
        "title": "10. OOP: Inheritance (Pewarisan)",
        "sections": [
            {
                "body": [
                    "Inheritance = class mewarisi attribute & method dari class lain.",
                    "  - Class induk  -> parent / superclass.",
                    "  - Class anak   -> child / subclass.",
                    "  - Pakai kata kunci extends.",
                    "  - Child bisa TAMBAH attribute/method baru, atau OVERRIDE.",
                    "",
                    "  class Hewan { ... }",
                    "  class Kucing extends Hewan { ... }",
                    "",
                    "Keuntungan:",
                    "  - Mengurangi duplikasi kode.",
                    "  - Kode lebih terstruktur dan mudah dirawat.",
                    "",
                    "super: merujuk ke member class induk.",
                    "  - super()        -> memanggil constructor induk.",
                    "  - super.method() -> memanggil method induk.",
                    "",
                    "Override: menulis ulang method induk dengan @Override.",
                ]
            },
            {
                "heading": "Contoh inheritance",
                "code": """class Hewan {
    String nama;

    Hewan(String nama) {
        this.nama = nama;
    }

    void bersuara() {
        System.out.println(nama + " bersuara.");
    }
}

class Kucing extends Hewan {
    Kucing(String nama) {
        super(nama);        // panggil constructor induk
    }

    @Override
    void bersuara() {
        System.out.println(nama + ": Meow!");
    }
}

public class Main {
    public static void main(String[] args) {
        Kucing k = new Kucing("Tom");
        k.bersuara();       // Tom: Meow!
    }
}"""
            },
            {
                "body": [
                    "Konsep 'is-a':",
                    "  - Kucing IS-A Hewan (benar) -> boleh diwarisi.",
                    "  - Lebih hati-hati dengan hierarki yang aneh.",
                    "    (Mobil IS-A Mesin itu salah).",
                    "",
                    "Keyword final:",
                    "  - final class -> tidak bisa diwarisi.",
                    "  - final method -> tidak bisa di-override.",
                    "  - final variabel -> tidak bisa diubah.",
                    "",
                    "Java TIDAK mendukung multiple inheritance antar class",
                    "(satu class hanya bisa extends satu parent).",
                    "Solusinya memakai Interface (materi berikutnya).",
                ]
            },
        ],
    },
    {
        "title": "11. OOP: Polymorphism",
        "sections": [
            {
                "body": [
                    "Polymorphism = 'banyak bentuk'.",
                    "Objek yang sama bisa berperilaku berbeda tergantung class aslinya.",
                    "",
                    "Ada 2 jenis:",
                    "  1. Compile-time (method overloading).",
                    "     Method sama, parameter beda. (sudah dibahas)",
                    "  2. Runtime (method overriding).",
                    "     Method induk ditulis ulang oleh anak, dipanggil",
                    "     sesuai objek aslinya.",
                    "",
                    "Kunci polymorphism:",
                    "  Variabel bertipe class induk boleh menampung objek anak.",
                    "  Hewan h = new Kucing(\"Tom\");",
                    "  h.bersuara();  // memanggil versi Kucing!",
                ]
            },
            {
                "heading": "Contoh polymorphism runtime",
                "code": """class Hewan {
    void bersuara() {
        System.out.println("Hewan bersuara");
    }
}

class Kucing extends Hewan {
    @Override
    void bersuara() {
        System.out.println("Meow!");
    }
}

class Anjing extends Hewan {
    @Override
    void bersuara() {
        System.out.println("Guk!");
    }
}

public class Main {
    public static void main(String[] args) {
        Hewan h1 = new Kucing();
        Hewan h2 = new Anjing();
        h1.bersuara();   // Meow!
        h2.bersuara();   // Guk!
    }
}"""
            },
            {
                "body": [
                    "Kenapa berguna?",
                    "  Kamu bisa menulis method yang menerima tipe induk,",
                    "  dan otomatis bekerja untuk semua turunannya.",
                    "",
                    "  void panggil(Hewan h) {",
                    "      h.bersuara();",
                    "  }",
                    "  panggil(new Kucing());  // Meow!",
                    "  panggil(new Anjing());  // Guk!",
                    "",
                    "Upcasting: anak diperlakukan sebagai induk (otomatis).",
                    "  Hewan h = new Kucing();",
                    "",
                    "Downcasting: induk dipaksa jadi anak (manual).",
                    "  Kucing k = (Kucing) h;   // wajib cast",
                    "  Periksa dulu dengan instanceof untuk aman.",
                ]
            },
        ],
    },
    {
        "title": "12. OOP: Abstract & Interface",
        "sections": [
            {
                "body": [
                    "Abstract class:",
                    "  - Class yang TIDAK bisa dibuat objeknya (tidak bisa new).",
                    "  - Boleh punya method abstrak (tanpa isi) & method biasa.",
                    "  - Bertindak sebagai kerangka untuk diturunkan.",
                    "",
                    "  abstract class Bentuk {",
                    "      abstract double luas();   // tanpa isi",
                    "      void info() { ... }        // method biasa",
                    "  }",
                    "",
                    "Interface:",
                    "  - 'Kontrak' yang harus dipenuhi class.",
                    "  - Semua method secara default public abstract (Java 8 ke bawah).",
                    "  - Sejak Java 8: boleh default method & static method.",
                    "  - Class bisa implements BANYAK interface (solusi multiple inheritance).",
                ]
            },
            {
                "heading": "Contoh interface",
                "code": """interface Kendaraan {
    void start();
    void berhenti();
}

class Mobil implements Kendaraan {
    public void start() {
        System.out.println("Mobil dinyalakan.");
    }

    public void berhenti() {
        System.out.println("Mobil berhenti.");
    }
}

class SepedaMotor implements Kendaraan {
    public void start() {
        System.out.println("Motor dinyalakan.");
    }

    public void berhenti() {
        System.out.println("Motor berhenti.");
    }
}"""
            },
            {
                "body": [
                    "Abstract class vs Interface (ringkas):",
                    "  Abstract class:",
                    "    - Bisa punya attribute & method biasa.",
                    "    - extends (satu parent saja).",
                    "    - Gunakan saat class punya 'kemiripan' kuat.",
                    "  Interface:",
                    "    - Hanya kontrak (metode utama).",
                    "    - implements (bisa banyak).",
                    "    - Gunakan saat ingin 'kemampuan' yang sama di class berbeda.",
                    "",
                    "Contoh penggunaan interface di Java API:",
                    "  - List, Map, Set adalah interface.",
                    "  - ArrayList, HashMap, HashSet adalah implementasinya.",
                    "  - Konsep ini dipakai terus di Collection Framework.",
                ]
            },
        ],
    },
    {
        "title": "13. Exception Handling",
        "sections": [
            {
                "body": [
                    "Exception = error yang terjadi saat program berjalan.",
                    "Tanpa penanganan, program langsung berhenti.",
                    "",
                    "Contoh error umum:",
                    "  - 10 / 0                -> ArithmeticException",
                    "  - arr[10] padahal kecil   -> ArrayIndexOutOfBoundsException",
                    "  - null.something()        -> NullPointerException",
                    "  - mengubah String jadi int -> NumberFormatException",
                    "",
                    "Cara menangani: try - catch - finally.",
                    "",
                    "  try {",
                    "      // kode yang mungkin error",
                    "  } catch (TipeException e) {",
                    "      // penanganan error",
                    "  } finally {",
                    "      // selalu dijalankan (opsional)",
                    "  }",
                ]
            },
            {
                "heading": "Contoh try-catch",
                "code": """public class Main {
    public static void main(String[] args) {
        try {
            int hasil = 10 / 0;
            System.out.println(hasil);
        } catch (ArithmeticException e) {
            System.out.println("Tidak bisa membagi dengan nol!");
        } finally {
            System.out.println("Blok finally selalu jalan.");
        }
        System.out.println("Program tetap lanjut.");
    }
}"""
            },
            {
                "body": [
                    "Menangkap beberapa exception:",
                    "  } catch (ArithmeticException | NullPointerException e) { ... }",
                    "  atau berurutan (yang lebih spesifik duluan).",
                    "",
                    "Throw & Throws:",
                    "  - throw  -> melempar exception secara sengaja.",
                    "      if (umur < 0) { throw new IllegalArgumentException(\"Umur salah\"); }",
                    "  - throws -> menandakan method bisa melempar exception.",
                    "      void bacaFile() throws IOException { ... }",
                    "",
                    "Checked vs Unchecked:",
                    "  - Checked  : dipaksa ditangani saat kompilasi (mis. IOException).",
                    "  - Unchecked: tidak dipaksa (RuntimeException beserta turunannya).",
                    "",
                    "Membuat exception sendiri:",
                    "  class SaldoTidakCukup extends Exception {",
                    "      SaldoTidakCukup(String pesan) { super(pesan); }",
                    "  }",
                ]
            },
        ],
    },
    {
        "title": "14. Collection Framework",
        "sections": [
            {
                "body": [
                    "Collection Framework = struktur data siap pakai di java.util.",
                    "Menggantikan array yang ukurannya tetap.",
                    "",
                    "Interface utama:",
                    "  - List  -> berurutan, boleh duplikat. (ArrayList, LinkedList)",
                    "  - Set   -> tidak berurutan, TIDAK boleh duplikat. (HashSet)",
                    "  - Map   -> pasangan key-value. (HashMap)",
                    "  - Queue -> antrian FIFO. (PriorityQueue)",
                    "",
                    "ArrayList:",
                    "  import java.util.ArrayList;",
                    "  import java.util.List;",
                    "  List<String> nama = new ArrayList<>();",
                    "  nama.add(\"Andi\");     // tambah",
                    "  nama.get(0);            // ambil indeks 0",
                    "  nama.size();            // jumlah elemen",
                    "  nama.remove(0);         // hapus indeks 0",
                    "  nama.contains(\"Andi\"); // cek ada tidak",
                ]
            },
            {
                "heading": "Contoh Collection Framework",
                "code": """import java.util.*;

public class Main {
    public static void main(String[] args) {
        // List
        List<String> buah = new ArrayList<>(List.of("Apel", "Mangga", "Jeruk"));
        buah.add("Durian");
        for (String b : buah) {
            System.out.print(b + " ");
        }
        System.out.println();   // Apel Mangga Jeruk Durian

        // Set (hapus duplikat)
        Set<Integer> angka = new HashSet<>();
        angka.add(1); angka.add(2); angka.add(2); angka.add(3);
        System.out.println(angka);   // [1, 2, 3]

        // Map
        Map<String, Integer> nilai = new HashMap<>();
        nilai.put("Andi", 85);
        nilai.put("Budi", 90);
        System.out.println(nilai.get("Andi"));   // 85
        for (Map.Entry<String, Integer> e : nilai.entrySet()) {
            System.out.println(e.getKey() + " -> " + e.getValue());
        }
    }
}"""
            },
            {
                "body": [
                    "Perbedaan cepat:",
                    "  ArrayList vs LinkedList:",
                    "    - ArrayList: akses cepat dengan indeks, lambat saat insert tengah.",
                    "    - LinkedList: cepat insert/delete, lambat akses indeks.",
                    "  HashMap vs TreeMap:",
                    "    - HashMap: cepat, tidak terurut.",
                    "    - TreeMap: terurut (sorted), sedikit lebih lambat.",
                    "",
                    "Mengurutkan List:",
                    "  Collections.sort(listAngka);",
                    "  listNama.sort(String::compareTo);",
                    "",
                    "Stream (Java 8+): pemrosesan data secara deklaratif.",
                    "  List<Integer> genap = list.stream()",
                    "      .filter(n -> n % 2 == 0)",
                    "      .collect(Collectors.toList());",
                ]
            },
        ],
    },
    {
        "title": "15. String & Scanner (Input)",
        "sections": [
            {
                "body": [
                    "String = kumpulan karakter, objek yang TIDAK bisa diubah (immutable).",
                    "",
                    "Membaca input dari keyboard pakai Scanner:",
                    "  import java.util.Scanner;",
                    "  Scanner sc = new Scanner(System.in);",
                    "  int umur = sc.nextInt();",
                    "  String nama = sc.nextLine();",
                    "  double tinggi = sc.nextDouble();",
                    "",
                    "PENTING: sc.nextInt() tidak membaca baris baru.",
                    "  Jika langsung panggil sc.nextLine(), hasilnya string kosong!",
                    "  Solusi: panggil sc.nextLine() sekali setelah nextInt().",
                    "",
                    "Method String yang sering dipakai:",
                    "  length(), charAt(i), substring(a,b), toUpperCase(),",
                    "  toLowerCase(), trim(), split(\",\"), replace(), equals(),",
                    "  equalsIgnoreCase(), contains(), startsWith(), indexOf().",
                    "  String.format(\"Halo %s umur %d\", nama, umur)",
                ]
            },
            {
                "heading": "Contoh input & manipulasi String",
                "code": """import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Nama: ");
        String nama = sc.nextLine();

        System.out.print("Umur: ");
        int umur = sc.nextInt();

        System.out.println("Halo " + nama.toUpperCase());
        System.out.println("Umur kamu " + umur + " tahun.");
        System.out.println("Panjang nama: " + nama.length());

        // String.format
        System.out.println(String.format("Nama: %s, Umur: %d", nama, umur));

        sc.close();
    }
}"""
            },
            {
                "body": [
                    "Membandingkan String:",
                    "  - Pakai .equals(), BUKAN == !",
                    "  - ==  membandingkan alamat/referensi, bukan isi.",
                    "    \"Andi\".equals(\"Andi\")  -> true",
                    "    \"Andi\" == \"Andi\"       -> bisa true/false (menipu!)",
                    "  - .equalsIgnoreCase() -> abaikan besar kecil huruf.",
                    "",
                    "StringBuffer / StringBuilder:",
                    "  - Untuk mengubah String berkali-kali (String immutable, mahal).",
                    "  - StringBuilder lebih cepat, tidak thread-safe.",
                    "    StringBuilder sb = new StringBuilder();",
                    "    sb.append(\"Halo\"); sb.append(\" Dunia\");",
                    "    String hasil = sb.toString();",
                ]
            },
        ],
    },
    {
        "title": "16. Lambda Expression & Functional Interface",
        "sections": [
            {
                "body": [
                    "Functional Interface = interface dengan TEPAT SATU abstract method.",
                    "Lambda expression adalah cara ringkas menulis implementasi",
                    "dari functional interface, tanpa menulis class terpisah.",
                    "",
                    "Sintaks lambda:",
                    "  (parameter) -> ekspresi",
                    "  (parameter) -> { beberapa statement; return nilai; }",
                    "",
                    "Sebelum lambda (cara lama, anonymous class):",
                    "  Runnable r = new Runnable() {",
                    "      public void run() {",
                    "          System.out.println(\"Jalan!\");",
                    "      }",
                    "  };",
                    "",
                    "Dengan lambda (Java 8+):",
                    "  Runnable r = () -> System.out.println(\"Jalan!\");",
                    "",
                    "Annotation @FunctionalInterface menandai interface yang",
                    "hanya boleh punya satu abstract method (opsional, tapi disarankan).",
                ]
            },
            {
                "heading": "Membuat & memakai functional interface sendiri",
                "code": """@FunctionalInterface
interface Operasi {
    int hitung(int a, int b);
}

public class Main {
    public static void main(String[] args) {
        Operasi tambah = (a, b) -> a + b;
        Operasi kali   = (a, b) -> a * b;

        System.out.println(tambah.hitung(3, 4));  // 7
        System.out.println(kali.hitung(3, 4));    // 12
    }
}"""
            },
            {
                "body": [
                    "Functional interface bawaan Java (java.util.function):",
                    "  Function<T,R>    -> menerima T, mengembalikan R. apply(T)",
                    "  Predicate<T>     -> menerima T, mengembalikan boolean. test(T)",
                    "  Consumer<T>      -> menerima T, tidak mengembalikan apa pun. accept(T)",
                    "  Supplier<T>      -> tidak menerima apa pun, mengembalikan T. get()",
                    "  BiFunction<T,U,R>-> menerima 2 argumen, kembalikan R.",
                    "",
                    "Contoh:",
                    "  Predicate<Integer> genap = n -> n % 2 == 0;",
                    "  genap.test(4);      // true",
                    "",
                    "  Function<String, Integer> panjang = s -> s.length();",
                    "  panjang.apply(\"Java\");  // 4",
                    "",
                    "  Consumer<String> cetak = s -> System.out.println(s);",
                    "  cetak.accept(\"Halo\");",
                    "",
                    "Method reference (lebih ringkas dari lambda):",
                    "  Consumer<String> cetak = System.out::println;",
                    "  Function<String, Integer> panjang = String::length;",
                ]
            },
        ],
    },
    {
        "title": "17. Stream API",
        "sections": [
            {
                "body": [
                    "Stream = cara memproses koleksi data secara deklaratif",
                    "(fokus pada 'apa yang mau dilakukan', bukan 'bagaimana loop-nya').",
                    "",
                    "Membuat stream:",
                    "  list.stream()          -> dari List/Set/Map",
                    "  Arrays.stream(array)   -> dari array",
                    "  Stream.of(1, 2, 3)     -> langsung dari nilai",
                    "",
                    "Operasi intermediate (mengembalikan stream baru, bisa dirangkai):",
                    "  filter(predicate)  -> menyaring elemen",
                    "  map(function)      -> mengubah tiap elemen",
                    "  sorted()           -> mengurutkan",
                    "  distinct()         -> hilangkan duplikat",
                    "  limit(n)           -> ambil n elemen pertama",
                    "",
                    "Operasi terminal (mengakhiri stream, hasilkan nilai akhir):",
                    "  collect(Collectors.toList())  -> jadi List",
                    "  forEach(consumer)              -> proses tiap elemen",
                    "  count()                        -> jumlah elemen",
                    "  reduce(...)                    -> gabungkan jadi satu nilai",
                    "  anyMatch/allMatch/noneMatch    -> uji kondisi",
                ]
            },
            {
                "heading": "Contoh Stream API lengkap",
                "code": """import java.util.*;
import java.util.stream.*;

public class Main {
    public static void main(String[] args) {
        List<Integer> angka = List.of(5, 3, 8, 1, 9, 2, 7);

        // filter genap, urutkan, cetak
        List<Integer> genap = angka.stream()
                .filter(n -> n % 2 == 0)
                .sorted()
                .collect(Collectors.toList());
        System.out.println(genap);         // [2, 8]

        // map: kalikan 2 semua elemen
        List<Integer> dikali2 = angka.stream()
                .map(n -> n * 2)
                .collect(Collectors.toList());
        System.out.println(dikali2);       // [10, 6, 16, 2, 18, 4, 14]

        // reduce: total semua elemen
        int total = angka.stream().reduce(0, (a, b) -> a + b);
        System.out.println("Total: " + total);   // 35

        // count & anyMatch
        long jumlahGenap = angka.stream().filter(n -> n % 2 == 0).count();
        boolean adaGenap = angka.stream().anyMatch(n -> n % 2 == 0);
        System.out.println(jumlahGenap + " " + adaGenap);   // 2 true

        // Nama mahasiswa yang lulus (>=75), diubah jadi huruf besar
        List<String> nama = List.of("Andi", "Budi", "Citra");
        List<Integer> nilai = List.of(80, 60, 95);
        // gabungkan dua list dengan IntStream (indeks)
        List<String> lulus = IntStream.range(0, nama.size())
                .filter(i -> nilai.get(i) >= 75)
                .mapToObj(i -> nama.get(i).toUpperCase())
                .collect(Collectors.toList());
        System.out.println(lulus);   // [ANDI, CITRA]
    }
}"""
            },
            {
                "body": [
                    "Collectors yang sering dipakai:",
                    "  Collectors.toList()        -> jadi List",
                    "  Collectors.toSet()         -> jadi Set",
                    "  Collectors.joining(\", \")  -> gabung String jadi satu",
                    "  Collectors.groupingBy(fn)  -> kelompokkan jadi Map<K, List<V>>",
                    "  Collectors.counting()      -> hitung jumlah per grup",
                    "  Collectors.summingInt(fn)  -> jumlahkan nilai int",
                    "",
                    "PENTING: Stream TIDAK mengubah koleksi aslinya (immutable-style).",
                    "Setiap operasi menghasilkan stream/koleksi BARU.",
                    "",
                    "Parallel stream (untuk data besar, hati-hati efek samping):",
                    "  list.parallelStream().filter(...).collect(...);",
                ]
            },
        ],
    },
    {
        "title": "18. Generics",
        "sections": [
            {
                "body": [
                    "Generics = membuat class/method/interface yang bisa bekerja",
                    "dengan BERBAGAI tipe data, tapi tetap type-safe (aman saat kompilasi).",
                    "",
                    "Tanpa generics (sebelum Java 5), harus pakai Object dan casting",
                    "manual yang rawan error (ClassCastException saat runtime).",
                    "",
                    "Dengan generics, tipe diperiksa saat KOMPILASI, bukan runtime.",
                    "  List<String> nama = new ArrayList<>();",
                    "  nama.add(\"Andi\");     // OK",
                    "  nama.add(123);        // ERROR saat kompilasi, bukan runtime!",
                    "",
                    "Konvensi huruf tipe generik:",
                    "  T -> Type, E -> Element, K -> Key, V -> Value, R -> Return",
                ]
            },
            {
                "heading": "Membuat class generic sendiri",
                "code": """class Kotak<T> {
    private T isi;

    public void simpan(T isi) {
        this.isi = isi;
    }

    public T ambil() {
        return isi;
    }
}

public class Main {
    public static void main(String[] args) {
        Kotak<String> kotakNama = new Kotak<>();
        kotakNama.simpan("Andi");
        System.out.println(kotakNama.ambil());   // Andi

        Kotak<Integer> kotakAngka = new Kotak<>();
        kotakAngka.simpan(100);
        System.out.println(kotakAngka.ambil());  // 100
    }
}"""
            },
            {
                "heading": "Generic method & bounded type",
                "code": """public class Utilitas {
    // Generic method: <T> ditulis sebelum tipe kembali
    static <T> void cetakSemua(List<T> daftar) {
        for (T item : daftar) {
            System.out.println(item);
        }
    }

    // Bounded type: T harus turunan Number (int, double, dll)
    static <T extends Number> double jumlahkan(List<T> daftar) {
        double total = 0;
        for (T item : daftar) {
            total += item.doubleValue();
        }
        return total;
    }

    public static void main(String[] args) {
        cetakSemua(List.of("A", "B", "C"));
        System.out.println(jumlahkan(List.of(1, 2, 3)));       // 6.0
        System.out.println(jumlahkan(List.of(1.5, 2.5)));      // 4.0
    }
}"""
            },
            {
                "body": [
                    "Wildcard (?): dipakai saat tipe pasti tidak diketahui/tak penting.",
                    "  List<?> apaSaja       -> list tipe apa pun (read-only aman)",
                    "  List<? extends Number> -> list Number atau turunannya (untuk baca)",
                    "  List<? super Integer>  -> list Integer atau induknya (untuk tulis)",
                    "",
                    "Generics banyak dipakai di Collection Framework:",
                    "  List<T>, Map<K,V>, Set<T>, Optional<T> semua pakai generics.",
                ]
            },
        ],
    },
    {
        "title": "19. Optional & Null Safety",
        "sections": [
            {
                "body": [
                    "NullPointerException (NPE) adalah error paling umum di Java,",
                    "terjadi saat memanggil method/field dari referensi yang null.",
                    "",
                    "Optional<T> = 'kotak' yang mungkin berisi nilai, mungkin kosong.",
                    "Memaksa developer untuk secara eksplisit menangani kasus kosong,",
                    "sehingga NPE bisa dicegah sejak awal.",
                    "",
                    "Membuat Optional:",
                    "  Optional<String> ada = Optional.of(\"Andi\");     // pasti tidak null",
                    "  Optional<String> kosong = Optional.empty();     // sengaja kosong",
                    "  Optional<String> aman = Optional.ofNullable(mungkinNull);",
                ]
            },
            {
                "heading": "Contoh penggunaan Optional",
                "code": """import java.util.Optional;

public class Main {
    static Optional<String> cariNama(int id) {
        if (id == 1) {
            return Optional.of("Andi");
        }
        return Optional.empty();
    }

    public static void main(String[] args) {
        Optional<String> hasil = cariNama(1);

        // isPresent() + get()
        if (hasil.isPresent()) {
            System.out.println(hasil.get());   // Andi
        }

        // orElse: nilai default jika kosong
        String nama = cariNama(99).orElse("Tidak ditemukan");
        System.out.println(nama);   // Tidak ditemukan

        // ifPresent: jalankan kode hanya jika ada isinya
        cariNama(1).ifPresent(n -> System.out.println("Halo, " + n));

        // map: transformasi nilai di dalam Optional
        cariNama(1).map(String::toUpperCase).ifPresent(System.out::println);  // ANDI

        // orElseThrow: lempar exception custom jika kosong
        try {
            cariNama(99).orElseThrow(() -> new RuntimeException("Data tidak ada!"));
        } catch (RuntimeException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}"""
            },
            {
                "body": [
                    "Aturan penggunaan Optional yang baik:",
                    "  1. Gunakan sebagai TIPE KEMBALI method, bukan sebagai field/parameter.",
                    "  2. Jangan panggil .get() tanpa cek isPresent() dulu (bisa NPE juga!).",
                    "  3. Lebih baik pakai orElse/orElseGet/orElseThrow/ifPresent.",
                    "  4. Jangan overuse - untuk kasus sederhana, if-null check biasa cukup.",
                ]
            },
        ],
    },
    {
        "title": "20. Multithreading & Concurrency Dasar",
        "sections": [
            {
                "body": [
                    "Thread = 'jalur eksekusi' program. Secara default program Java",
                    "berjalan di satu thread (main thread).",
                    "Multithreading = menjalankan beberapa bagian kode SECARA BERSAMAAN.",
                    "",
                    "Manfaat multithreading:",
                    "  - Program lebih responsif (misal UI tidak freeze saat loading).",
                    "  - Memanfaatkan CPU multi-core secara maksimal.",
                    "  - Cocok untuk tugas paralel: download banyak file sekaligus, dll.",
                    "",
                    "Cara membuat thread:",
                    "  1. extends Thread lalu override run().",
                    "  2. implements Runnable lalu jalankan lewat new Thread(runnable).",
                    "     (Cara ke-2 lebih disarankan karena Java tidak multiple inheritance).",
                ]
            },
            {
                "heading": "Contoh membuat & menjalankan thread",
                "code": """class TugasCetak implements Runnable {
    private String label;

    TugasCetak(String label) {
        this.label = label;
    }

    @Override
    public void run() {
        for (int i = 1; i <= 3; i++) {
            System.out.println(label + " - langkah " + i);
        }
    }
}

public class Main {
    public static void main(String[] args) throws InterruptedException {
        Thread t1 = new Thread(new TugasCetak("Thread-A"));
        Thread t2 = new Thread(new TugasCetak("Thread-B"));

        t1.start();   // BUKAN t1.run() ! start() membuat thread baru
        t2.start();

        t1.join();    // tunggu t1 selesai sebelum lanjut
        t2.join();
        System.out.println("Semua thread selesai.");
    }
}"""
            },
            {
                "body": [
                    "Race condition: bug yang muncul saat beberapa thread mengubah",
                    "data yang sama secara bersamaan, hasilnya jadi tidak menentu.",
                    "",
                    "Solusi: kata kunci synchronized untuk mengunci akses satu-per-satu.",
                    "  synchronized void tambahSaldo(double jumlah) {",
                    "      saldo += jumlah;   // aman, hanya 1 thread pada satu waktu",
                    "  }",
                    "",
                    "ExecutorService: cara modern mengelola banyak thread (thread pool),",
                    "lebih efisien daripada membuat Thread satu-satu secara manual.",
                    "  ExecutorService pool = Executors.newFixedThreadPool(4);",
                    "  pool.submit(() -> System.out.println(\"Tugas jalan\"));",
                    "  pool.shutdown();",
                    "",
                    "Ini topik lanjutan yang dalam - cukup pahami konsep dasarnya dulu,",
                    "lalu perdalam saat mulai membuat aplikasi backend yang nyata.",
                ]
            },
        ],
    },
    {
        "title": "21. File I/O & Serialization",
        "sections": [
            {
                "body": [
                    "File I/O = membaca dan menulis data ke file (Input/Output).",
                    "Berguna untuk menyimpan data agar tidak hilang saat program ditutup.",
                    "",
                    "Kelas utama di java.io & java.nio.file:",
                    "  File            -> representasi path file/folder.",
                    "  FileWriter      -> menulis teks ke file.",
                    "  FileReader / BufferedReader -> membaca teks dari file.",
                    "  Files (java.nio.file) -> API modern, lebih ringkas.",
                    "",
                    "Semua operasi file BISA melempar IOException (checked exception),",
                    "jadi harus ditangani dengan try-catch atau throws.",
                ]
            },
            {
                "heading": "Menulis & membaca file teks",
                "code": """import java.io.*;
import java.nio.file.*;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        String namaFile = "catatan.txt";

        // Menulis dengan try-with-resources (otomatis ditutup)
        try (FileWriter fw = new FileWriter(namaFile)) {
            fw.write("Baris pertama\\n");
            fw.write("Baris kedua\\n");
        } catch (IOException e) {
            System.out.println("Gagal menulis: " + e.getMessage());
        }

        // Membaca dengan BufferedReader
        try (BufferedReader br = new BufferedReader(new FileReader(namaFile))) {
            String baris;
            while ((baris = br.readLine()) != null) {
                System.out.println("Baca: " + baris);
            }
        } catch (IOException e) {
            System.out.println("Gagal membaca: " + e.getMessage());
        }

        // Cara modern: java.nio.file.Files (lebih ringkas)
        try {
            Files.writeString(Path.of("modern.txt"), "Halo dari Files API");
            List<String> semuaBaris = Files.readAllLines(Path.of("modern.txt"));
            System.out.println(semuaBaris);
        } catch (IOException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}"""
            },
            {
                "body": [
                    "try-with-resources:",
                    "  try (Resource r = ...) { ... }",
                    "  Resource otomatis ditutup (close()) walau terjadi error,",
                    "  tidak perlu finally { r.close(); } manual lagi.",
                    "  Syarat: resource harus implements AutoCloseable.",
                    "",
                    "Serialization: mengubah objek Java menjadi byte stream agar bisa",
                    "disimpan ke file atau dikirim lewat jaringan.",
                    "  class Mahasiswa implements Serializable { ... }",
                    "  ObjectOutputStream -> menulis objek ke file.",
                    "  ObjectInputStream  -> membaca objek dari file.",
                    "",
                    "Untuk data terstruktur (config, dsb), lebih umum sekarang",
                    "memakai format JSON dengan library seperti Jackson atau Gson.",
                ]
            },
        ],
    },
    {
        "title": "22. JDBC: Menghubungkan Java ke Database",
        "sections": [
            {
                "body": [
                    "JDBC (Java Database Connectivity) = API bawaan Java untuk",
                    "menghubungkan aplikasi Java dengan database (MySQL, PostgreSQL, dll).",
                    "",
                    "Langkah dasar memakai JDBC:",
                    "  1. Tambahkan driver database (misal mysql-connector-j) ke project.",
                    "  2. Buat koneksi dengan DriverManager.getConnection(url, user, pass).",
                    "  3. Buat Statement/PreparedStatement untuk menjalankan query.",
                    "  4. Proses ResultSet (hasil query SELECT).",
                    "  5. Tutup koneksi (atau pakai try-with-resources).",
                    "",
                    "Format URL koneksi MySQL:",
                    "  jdbc:mysql://localhost:3306/nama_database",
                ]
            },
            {
                "heading": "Contoh koneksi & query dengan PreparedStatement",
                "code": """import java.sql.*;

public class Main {
    public static void main(String[] args) {
        String url = "jdbc:mysql://localhost:3306/belajar_db";
        String user = "root";
        String pass = "password";

        String sql = "SELECT nim, nama, ipk FROM mahasiswa WHERE ipk > ?";

        try (Connection conn = DriverManager.getConnection(url, user, pass);
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setDouble(1, 3.0);   // isi tanda '?' pertama

            try (ResultSet rs = stmt.executeQuery()) {
                while (rs.next()) {
                    int nim = rs.getInt("nim");
                    String nama = rs.getString("nama");
                    double ipk = rs.getDouble("ipk");
                    System.out.println(nim + " - " + nama + " - " + ipk);
                }
            }
        } catch (SQLException e) {
            System.out.println("Error database: " + e.getMessage());
        }
    }
}"""
            },
            {
                "body": [
                    "PENTING: Selalu pakai PreparedStatement, JANGAN gabungkan String",
                    "query dengan input user secara langsung (rawan SQL Injection!).",
                    "",
                    "  // BAHAYA - jangan ditiru:",
                    "  String sql = \"SELECT * FROM users WHERE nama = '\" + input + \"'\";",
                    "",
                    "  // AMAN - gunakan placeholder ?:",
                    "  PreparedStatement stmt = conn.prepareStatement(",
                    "      \"SELECT * FROM users WHERE nama = ?\");",
                    "  stmt.setString(1, input);",
                    "",
                    "INSERT/UPDATE/DELETE pakai executeUpdate(), bukan executeQuery():",
                    "  int baris = stmt.executeUpdate();  // jumlah baris terpengaruh",
                    "",
                    "Untuk project nyata, disarankan pakai ORM seperti Hibernate/JPA",
                    "atau framework Spring Data JPA yang menyederhanakan kode JDBC ini.",
                ]
            },
        ],
    },
    {
        "title": "23. Unit Testing dengan JUnit",
        "sections": [
            {
                "body": [
                    "Unit Testing = menguji bagian kecil kode (biasanya satu method)",
                    "secara otomatis untuk memastikan hasilnya sesuai harapan.",
                    "",
                    "Manfaat testing:",
                    "  1. Menemukan bug lebih awal, sebelum ke production.",
                    "  2. Berani refactor kode tanpa takut merusak fitur lain.",
                    "  3. Dokumentasi hidup: test menunjukkan cara pakai kode.",
                    "  4. Wajib di dunia kerja profesional (CI/CD selalu jalankan test).",
                    "",
                    "JUnit 5 adalah framework testing paling populer di Java.",
                    "Anotasi utama:",
                    "  @Test        -> menandai method sebagai test case.",
                    "  @BeforeEach  -> dijalankan sebelum setiap test.",
                    "  @AfterEach   -> dijalankan setelah setiap test.",
                    "  @DisplayName -> memberi nama deskriptif pada test.",
                ]
            },
            {
                "heading": "Contoh unit test sederhana",
                "code": """import org.junit.jupiter.api.*;
import static org.junit.jupiter.api.Assertions.*;

class Kalkulator {
    int tambah(int a, int b) {
        return a + b;
    }
    int bagi(int a, int b) {
        if (b == 0) throw new ArithmeticException("Tidak boleh bagi nol");
        return a / b;
    }
}

class KalkulatorTest {
    Kalkulator kalkulator;

    @BeforeEach
    void setUp() {
        kalkulator = new Kalkulator();   // dijalankan sebelum tiap test
    }

    @Test
    @DisplayName("Penjumlahan dua angka positif")
    void testTambah() {
        assertEquals(7, kalkulator.tambah(3, 4));
    }

    @Test
    void testBagiDenganNol() {
        assertThrows(ArithmeticException.class, () -> {
            kalkulator.bagi(10, 0);
        });
    }
}"""
            },
            {
                "body": [
                    "Assertion (pengecekan) yang sering dipakai:",
                    "  assertEquals(expected, actual) -> nilai harus sama",
                    "  assertTrue(kondisi) / assertFalse(kondisi)",
                    "  assertNull(obj) / assertNotNull(obj)",
                    "  assertThrows(Exception.class, () -> { ... }) -> harus melempar error",
                    "",
                    "Konsep AAA (Arrange - Act - Assert) untuk menulis test yang jelas:",
                    "  1. Arrange -> siapkan data/objek yang dibutuhkan.",
                    "  2. Act     -> panggil method yang diuji.",
                    "  3. Assert  -> periksa hasilnya sesuai harapan.",
                    "",
                    "Test coverage: seberapa banyak baris kode yang tercakup test.",
                    "Target umum di industri: 70-90% (tidak harus 100%).",
                ]
            },
        ],
    },
    {
        "title": "24. Design Pattern & Clean Code",
        "sections": [
            {
                "body": [
                    "Design Pattern = solusi umum untuk masalah desain yang berulang",
                    "dalam pengembangan software. Bukan kode siap pakai, tapi 'pola pikir'.",
                    "",
                    "Beberapa pattern populer:",
                    "  Singleton  -> memastikan hanya ada SATU instance dari sebuah class.",
                    "  Factory    -> menyembunyikan logika pembuatan objek yang kompleks.",
                    "  Builder    -> membangun objek kompleks langkah demi langkah.",
                    "  Observer   -> objek 'berlangganan' perubahan dari objek lain.",
                    "  Strategy   -> menukar algoritma/perilaku secara dinamis.",
                ]
            },
            {
                "heading": "Contoh Singleton & Builder",
                "code": """// Singleton: hanya satu instance untuk seluruh aplikasi
class Konfigurasi {
    private static Konfigurasi instance;
    private String appName = "AplikasiBelajar";

    private Konfigurasi() { }   // constructor private!

    public static Konfigurasi getInstance() {
        if (instance == null) {
            instance = new Konfigurasi();
        }
        return instance;
    }

    public String getAppName() { return appName; }
}

// Builder: membangun objek kompleks step-by-step
class Mahasiswa {
    private final String nama;
    private final int umur;
    private final String jurusan;

    private Mahasiswa(Builder b) {
        this.nama = b.nama;
        this.umur = b.umur;
        this.jurusan = b.jurusan;
    }

    static class Builder {
        private String nama;
        private int umur;
        private String jurusan;

        Builder nama(String n) { this.nama = n; return this; }
        Builder umur(int u) { this.umur = u; return this; }
        Builder jurusan(String j) { this.jurusan = j; return this; }
        Mahasiswa build() { return new Mahasiswa(this); }
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println(Konfigurasi.getInstance().getAppName());

        Mahasiswa m = new Mahasiswa.Builder()
                .nama("Andi")
                .umur(20)
                .jurusan("Informatika")
                .build();
    }
}"""
            },
            {
                "body": [
                    "Prinsip Clean Code (kode yang mudah dibaca & dirawat):",
                    "  1. Nama yang jelas: hitungTotalBelanja() lebih baik dari htb().",
                    "  2. Satu method = satu tanggung jawab (Single Responsibility).",
                    "  3. Hindari 'magic number', gunakan konstanta bernama:",
                    "       final double PPN = 0.11;   bukan   total * 0.11",
                    "  4. Method sebaiknya pendek (idealnya < 20-30 baris).",
                    "  5. Hindari duplikasi kode (prinsip DRY: Don't Repeat Yourself).",
                    "  6. Tulis komentar untuk 'MENGAPA', bukan 'APA' (kode sudah jelas 'apa').",
                    "  7. Konsisten dengan format & konvensi penamaan tim/project.",
                    "",
                    "Prinsip SOLID (untuk OOP yang baik):",
                    "  S - Single Responsibility : satu class, satu tanggung jawab.",
                    "  O - Open/Closed          : terbuka untuk ekstensi, tertutup untuk modifikasi.",
                    "  L - Liskov Substitution  : subclass harus bisa gantikan parent-nya.",
                    "  I - Interface Segregation: interface kecil & spesifik, bukan 1 raksasa.",
                    "  D - Dependency Inversion : bergantung pada abstraksi, bukan implementasi.",
                ]
            },
        ],
    },
    {
        "title": "25. Git, Maven/Gradle & Alur Kerja Developer",
        "sections": [
            {
                "body": [
                    "Git = sistem version control untuk melacak perubahan kode",
                    "dan berkolaborasi dengan developer lain. WAJIB dikuasai.",
                    "",
                    "Perintah git dasar:",
                    "  git init                 -> membuat repo baru",
                    "  git clone <url>          -> menyalin repo dari GitHub/GitLab",
                    "  git add <file>           -> menandai perubahan untuk disimpan",
                    "  git commit -m 'pesan'    -> menyimpan perubahan (snapshot)",
                    "  git push                 -> kirim commit ke server (remote)",
                    "  git pull                 -> ambil perubahan terbaru dari server",
                    "  git branch nama          -> membuat cabang baru",
                    "  git checkout nama        -> pindah ke cabang lain",
                    "  git merge nama           -> gabungkan cabang ke cabang aktif",
                    "  git status               -> lihat perubahan yang belum disimpan",
                ]
            },
            {
                "body": [
                    "Build tool (Maven & Gradle):",
                    "  Fungsi: mengelola dependency (library eksternal), mengompilasi,",
                    "  menjalankan test, dan mem-package aplikasi menjadi .jar/.war.",
                    "",
                    "  Maven (pom.xml)          Gradle (build.gradle)",
                    "  ---------------          ---------------------",
                    "  Konfigurasi XML          Konfigurasi Groovy/Kotlin DSL",
                    "  mvn clean install        ./gradlew build",
                    "  mvn test                 ./gradlew test",
                    "",
                    "Contoh dependency di pom.xml (Maven):",
                    "  <dependency>",
                    "      <groupId>mysql</groupId>",
                    "      <artifactId>mysql-connector-j</artifactId>",
                    "      <version>8.0.33</version>",
                    "  </dependency>",
                    "",
                    "Alur kerja developer profesional (ringkas):",
                    "  1. Ambil task/issue dari board (Jira/Trello/GitHub Issues).",
                    "  2. Buat branch baru dari main/develop.",
                    "  3. Tulis kode + unit test.",
                    "  4. Commit dengan pesan jelas, push ke remote.",
                    "  5. Buat Pull Request / Merge Request untuk direview tim.",
                    "  6. Setelah disetujui & lolos CI (test otomatis), merge ke main.",
                ]
            },
        ],
    },
    {
        "title": "26. Roadmap Menjadi Programmer Handal",
        "sections": [
            {
                "body": [
                    "Kamu sudah menyelesaikan pondasi Java yang solid. Berikut adalah",
                    "roadmap realistis untuk melangkah dari 'paham dasar' menjadi",
                    "programmer yang handal dan siap kerja/industri.",
                    "",
                    "TAHAP 1 - Kuatkan Fondasi (kamu di sini):",
                    "  - Sudah paham: variabel, OOP, collection, exception, lambda, stream.",
                    "  - Target: bisa menjelaskan SEMUA konsep di atas dengan bahasamu sendiri,",
                    "    bukan cuma hafal sintaks.",
                    "",
                    "TAHAP 2 - Bangun Project Nyata (3-6 bulan):",
                    "  1. To-Do List CLI  -> latihan logika & OOP dasar.",
                    "  2. Sistem Nilai Mahasiswa dengan file/database -> CRUD + JDBC.",
                    "  3. REST API sederhana pakai Spring Boot -> backend web.",
                    "  4. Aplikasi dengan testing (JUnit) dari awal -> kebiasaan profesional.",
                ]
            },
            {
                "body": [
                    "TAHAP 3 - Pelajari Ekosistem Industri (6-12 bulan):",
                    "  - Spring Boot / Spring Framework  -> standar backend Java di industri.",
                    "  - Spring Data JPA / Hibernate      -> ORM, menggantikan JDBC manual.",
                    "  - REST API & JSON (Jackson/Gson)   -> komunikasi antar layanan.",
                    "  - Docker                           -> containerization aplikasi.",
                    "  - Git & GitHub                     -> kolaborasi tim (WAJIB).",
                    "  - Message Queue (Kafka/RabbitMQ)   -> untuk sistem skala besar.",
                    "  - Microservices                    -> arsitektur aplikasi modern.",
                    "",
                    "TAHAP 4 - Soft Skill & Kebiasaan Profesional:",
                    "  1. Baca kode orang lain (open source di GitHub).",
                    "  2. Ikut code review, terima kritik dengan terbuka.",
                    "  3. Biasakan menulis dokumentasi (README, komentar penting).",
                    "  4. Latihan algoritma & struktur data (LeetCode/HackerRank).",
                    "  5. Ikuti komunitas developer (Discord, forum, meetup lokal).",
                ]
            },
            {
                "body": [
                    "Kebiasaan harian untuk jadi handal:",
                    "  1. Ketik ulang SEMUA contoh kode di aplikasi ini, jangan copy-paste.",
                    "  2. Ubah-ubah kodenya, tebak outputnya dulu, baru jalankan & cek.",
                    "  3. Kerjakan minimal 1 latihan coding per hari, konsisten > cepat.",
                    "  4. Debug error SENDIRI dulu 15-30 menit sebelum bertanya ke orang lain.",
                    "  5. Baca error message pelan-pelan - itu petunjuk paling akurat.",
                    "  6. Bangun proyek kecil dari nol, jangan cuma ikuti tutorial pasif.",
                    "  7. Kuasai SQL & database untuk jadi full-stack developer.",
                    "  8. Ajarkan yang sudah kamu pelajari ke orang lain (Feynman technique).",
                    "",
                    "Ingat: 'programmer yang paham SETIAP baris kode di dunia' itu mustahil",
                    "secara harfiah (bahkan senior engineer terus belajar tiap hari) -",
                    "tapi programmer HANDAL adalah yang punya fondasi kuat, terbiasa",
                    "membaca & memahami kode baru dengan cepat, dan tidak takut hal asing.",
                    "Itulah target yang realistis dan bisa kamu capai dengan konsisten.",
                ]
            },
        ],
    },
]
