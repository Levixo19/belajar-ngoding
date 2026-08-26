CPP_MATERIALS = [
    {
        "title": "1. Pengenalan C++ & Perbedaan dari C",
        "sections": [
            {
                "body": [
                    "Apa itu C++?",
                    "  - Dibuat oleh Bjarne Stroustrup (1979-1985) sebagai",
                    "    'C with Classes' - perluasan bahasa C dengan OOP.",
                    "  - C++ adalah SUPERSET dari C: hampir semua kode C valid",
                    "    juga di C++ (dengan sedikit pengecualian).",
                    "  - Dipakai untuk: game engine (Unreal Engine), aplikasi",
                    "    performa tinggi, sistem trading, browser (Chrome, Firefox),",
                    "    database engine (MySQL, MongoDB ditulis dalam C++).",
                    "",
                    "Kenapa belajar C++ setelah C:",
                    "  - Menambahkan OOP (class, inheritance, polymorphism) di",
                    "    atas fondasi C yang sudah kamu kuasai.",
                    "  - STL (Standard Template Library) menyediakan struktur data",
                    "    siap pakai (vector, map, dll) - tidak perlu implementasi",
                    "    manual seperti linked list di C.",
                    "  - Smart pointer membantu mengurangi bug memory leak.",
                ]
            },
            {
                "heading": "Program pertama (simpan sebagai hello.cpp)",
                "code": """#include <iostream>
using namespace std;

int main() {
    cout << "Halo Dunia!" << endl;
    cout << "Aku sedang belajar C++." << endl;
    return 0;
}"""
            },
            {
                "body": [
                    "Kompilasi & jalankan:",
                    "  g++ hello.cpp -o hello    (kompilasi jadi executable)",
                    "  ./hello                    (jalankan hasilnya)",
                    "",
                    "Perbedaan UTAMA dari C yang sudah kamu pelajari:",
                    "  1. #include <iostream> menggantikan <stdio.h> untuk I/O.",
                    "  2. cout << ... dan cin >> ... menggantikan printf/scanf.",
                    "  3. using namespace std; agar tidak perlu tulis std:: berulang.",
                    "  4. bool, true, false adalah tipe BAWAAN (tidak perlu",
                    "     #include <stdbool.h> seperti di C).",
                    "  5. // dan /* */ untuk komentar (SAMA seperti C).",
                    "  6. C++ TETAP mendukung printf/scanf jika diperlukan -",
                    "     kode C lama bisa langsung dikompilasi sebagai C++.",
                ]
            },
        ],
    },
    {
        "title": "2. Variabel, Tipe Data & Namespace",
        "sections": [
            {
                "body": [
                    "Tipe data dasar C++ SAMA PERSIS dengan C (int, float,",
                    "double, char), ditambah bool sebagai tipe BAWAAN (bukan",
                    "dari stdbool.h seperti di C).",
                    "",
                    "  int umur = 20;",
                    "  double harga = 15000.50;",
                    "  char grade = 'A';",
                    "  bool lulus = true;         // bawaan C++, tanpa header tambahan",
                    "  string nama = \"Andi\";      // butuh #include <string>",
                    "",
                    "string (huruf kecil) adalah class dari STL, BUKAN char array",
                    "seperti string C - jauh lebih mudah dipakai (bisa +, ==, dll).",
                ]
            },
            {
                "heading": "Contoh tipe data & namespace",
                "code": """#include <iostream>
#include <string>
using namespace std;

int main() {
    int umur = 20;
    double harga = 15000.50;
    bool lulus = true;
    string nama = "Andi";        // class string, BUKAN char array!

    cout << "Nama: " << nama << ", Umur: " << umur << endl;
    cout << "Harga: " << harga << endl;
    cout << "Lulus: " << lulus << endl;   // tampil sebagai 1 (true) / 0 (false)

    // Operasi string yang JAUH lebih mudah dari char array C:
    string namaLengkap = nama + " Wijaya";   // + untuk menggabung string!
    cout << namaLengkap << endl;
    cout << "Panjang: " << namaLengkap.length() << endl;

    return 0;
}"""
            },
            {
                "body": [
                    "namespace: mekanisme untuk mengelompokkan nama (fungsi,",
                    "class, variabel) agar tidak bentrok antar library.",
                    "",
                    "  using namespace std;   // pakai SEMUA nama dari namespace std",
                    "  std::cout << \"Halo\";    // ATAU akses langsung dengan std::",
                    "",
                    "Di project BESAR, praktik yang lebih disarankan adalah",
                    "TIDAK memakai 'using namespace std;' secara global (bisa",
                    "menyebabkan konflik nama), melainkan akses spesifik std::cout,",
                    "std::string, dsb - tapi untuk belajar, 'using namespace std;'",
                    "tetap umum dipakai agar kode lebih ringkas dibaca.",
                    "",
                    "auto (C++11+): compiler menebak tipe data otomatis dari nilai:",
                    "  auto x = 10;        // otomatis jadi int",
                    "  auto nama = string(\"Andi\");   // otomatis jadi string",
                ]
            },
        ],
    },
    {
        "title": "3. Input/Output Modern (cin & cout)",
        "sections": [
            {
                "body": [
                    "cout (console output) dan cin (console input) adalah",
                    "cara STANDAR C++ untuk I/O, menggantikan printf/scanf dari C.",
                    "",
                    "  cout << nilai;           -> mencetak nilai (operator <<)",
                    "  cout << a << b << c;     -> bisa dirangkai (chaining)",
                    "  cin >> variabel;         -> membaca input (operator >>)",
                    "  endl                     -> baris baru (mirip \\n, plus flush buffer)",
                    "",
                    "Keunggulan cout dibanding printf: TIDAK perlu format specifier",
                    "(%d, %s, dll) - compiler otomatis tahu tipe data dari operator <<.",
                ]
            },
            {
                "heading": "Contoh cin & cout",
                "code": """#include <iostream>
#include <string>
using namespace std;

int main() {
    string nama;
    int umur;
    double tinggi;

    cout << "Masukkan nama: ";
    cin >> nama;              // TIDAK bisa baca spasi (berhenti di spasi pertama)

    cout << "Masukkan umur: ";
    cin >> umur;               // TIDAK perlu & seperti scanf, TIDAK perlu %d

    cout << "Masukkan tinggi: ";
    cin >> tinggi;

    cout << "Halo " << nama << ", umur " << umur
         << " tahun, tinggi " << tinggi << " cm" << endl;

    // Untuk membaca SATU BARIS PENUH termasuk spasi:
    cin.ignore();              // buang newline sisa dari cin >> sebelumnya
    string namaLengkap;
    cout << "Nama lengkap: ";
    getline(cin, namaLengkap); // getline membaca sampai newline (mirip fgets di C)
    cout << "Halo " << namaLengkap << endl;

    return 0;
}"""
            },
            {
                "body": [
                    "cout formatting (dari <iomanip>):",
                    "  #include <iomanip>",
                    "  cout << fixed << setprecision(2) << 3.14159;  // 3.14",
                    "  cout << setw(10) << nilai;    // lebar minimal 10 karakter",
                    "",
                    "Perbandingan singkat printf/scanf vs cout/cin:",
                    "  printf/scanf: lebih cepat (sedikit), butuh format specifier",
                    "                yang harus PERSIS sesuai tipe data.",
                    "  cout/cin:     type-safe otomatis, lebih mudah dibaca &",
                    "                lebih 'C++ idiomatic', SEDIKIT lebih lambat.",
                    "  Keduanya BISA dipakai bersamaan dalam satu program C++.",
                ]
            },
        ],
    },
    {
        "title": "4. Referensi (&) vs Pointer",
        "sections": [
            {
                "body": [
                    "C++ menambahkan REFERENCE (&) sebagai alternatif pointer",
                    "yang lebih AMAN & lebih mudah dibaca untuk banyak kasus.",
                    "",
                    "Reference = 'alias' (nama lain) untuk variabel yang SUDAH",
                    "ada, BUKAN variabel terpisah yang menyimpan alamat (walau",
                    "di baliknya tetap memakai alamat memori).",
                    "",
                    "  int angka = 10;",
                    "  int &ref = angka;    // ref adalah ALIAS dari angka",
                    "  ref = 20;             // ini SAMA DENGAN mengubah angka",
                    "  cout << angka;        // 20! (angka ikut berubah)",
                    "",
                    "Perbedaan pointer vs reference:",
                    "  Pointer (int *p)         Reference (int &r)",
                    "  --------------------      --------------------",
                    "  BISA NULL                  TIDAK BISA null (harus langsung",
                    "                              di-inisialisasi ke variabel valid)",
                    "  BISA di-reassign            TIDAK BISA 'pindah' alias setelah",
                    "  (menunjuk ke lain)           diinisialisasi",
                    "  butuh * untuk akses          diakses LANGSUNG seperti variabel biasa",
                    "  butuh & untuk assign          TIDAK butuh operator khusus",
                ]
            },
            {
                "heading": "Reference sebagai parameter fungsi (pass by reference)",
                "code": """#include <iostream>
using namespace std;

// Pass by value (C style) - TIDAK mengubah variabel asli
void tambahSatuValue(int x) {
    x = x + 1;
}

// Pass by reference (C++ style) - MENGUBAH variabel asli, TANPA pointer!
void tambahSatuRef(int &x) {
    x = x + 1;
}

void tukar(int &a, int &b) {   // swap TANPA pointer, jauh lebih mudah dibaca!
    int temp = a;
    a = b;
    b = temp;
}

int main() {
    int angka = 5;
    tambahSatuValue(angka);
    cout << angka << endl;   // 5 (tidak berubah, pass by value)

    tambahSatuRef(angka);
    cout << angka << endl;   // 6 (berubah, pass by reference)

    int x = 1, y = 2;
    tukar(x, y);
    cout << x << " " << y << endl;   // 2 1

    return 0;
}"""
            },
            {
                "body": [
                    "Kapan pakai reference vs pointer di C++ modern:",
                    "  - Reference: untuk parameter fungsi yang PASTI ada nilainya",
                    "    (tidak butuh 'kosong'/null) - LEBIH DISARANKAN, lebih aman.",
                    "  - Pointer: untuk kasus yang BUTUH kemungkinan 'tidak menunjuk",
                    "    apa pun' (null), atau butuh berpindah target, atau untuk",
                    "    dynamic memory allocation (new/delete, materi berikutnya).",
                    "",
                    "const reference (SANGAT umum di C++, untuk efisiensi):",
                    "  void tampilkan(const string &teks) {   // tidak menyalin string besar,",
                    "      cout << teks;                        // TAPI dijamin tidak diubah",
                    "  }",
                ]
            },
        ],
    },
    {
        "title": "5. Function Overloading & Default Parameter",
        "sections": [
            {
                "body": [
                    "Function overloading = BEBERAPA fungsi dengan NAMA SAMA",
                    "tapi PARAMETER BERBEDA (jumlah atau tipe) - compiler",
                    "otomatis memilih versi yang sesuai berdasarkan argumen",
                    "yang dikirim. (C TIDAK mendukung ini - fitur khas C++/OOP.)",
                ]
            },
            {
                "heading": "Contoh function overloading & default parameter",
                "code": """#include <iostream>
using namespace std;

int tambah(int a, int b) {
    return a + b;
}

double tambah(double a, double b) {   // overload: parameter beda tipe
    return a + b;
}

int tambah(int a, int b, int c) {     // overload: jumlah parameter beda
    return a + b + c;
}

// Default parameter: nilai default jika argumen tidak diisi
void sapa(string nama, string sapaan = "Halo") {
    cout << sapaan << ", " << nama << "!" << endl;
}

int main() {
    cout << tambah(2, 3) << endl;         // 5 (versi int)
    cout << tambah(2.5, 3.5) << endl;     // 6.0 (versi double)
    cout << tambah(1, 2, 3) << endl;      // 6 (versi 3 parameter)

    sapa("Andi");                          // Halo, Andi!
    sapa("Budi", "Hai");                   // Hai, Budi!

    return 0;
}"""
            },
            {
                "body": [
                    "Aturan overloading:",
                    "  - Compiler membedakan fungsi berdasarkan JUMLAH & TIPE",
                    "    parameter (disebut 'function signature'), BUKAN nama",
                    "    parameter atau tipe kembali saja.",
                    "  - Dua fungsi dengan parameter SAMA PERSIS tapi tipe kembali",
                    "    beda TIDAK dianggap overload yang valid (ambigu, error).",
                    "",
                    "Default parameter HANYA boleh di akhir daftar parameter:",
                    "  void f(int a, int b = 10, int c = 20) { ... }   // BENAR",
                    "  void f(int a = 10, int b) { ... }               // ERROR!",
                ]
            },
        ],
    },
    {
        "title": "6. OOP: Class & Object Dasar",
        "sections": [
            {
                "body": [
                    "class di C++ mirip struct C, TAPI bisa punya METHOD",
                    "(fungsi anggota) selain data, plus access control",
                    "(public/private/protected - materi encapsulation).",
                    "",
                    "  class NamaClass {",
                    "  public:",
                    "      tipeData atribut;",
                    "      tipeKembali method() { ... }",
                    "  };",
                    "",
                    "Perbedaan struct vs class di C++ (BEDA dari C!):",
                    "  - struct: member DEFAULT-nya public.",
                    "  - class:  member DEFAULT-nya private.",
                    "  - Selain itu, keduanya FUNGSIONAL SAMA di C++ (beda",
                    "    dengan C dimana struct TIDAK bisa punya method).",
                ]
            },
            {
                "heading": "Contoh class & object dasar",
                "code": """#include <iostream>
#include <string>
using namespace std;

class Mahasiswa {
public:
    string nama;
    int umur;

    void perkenalan() {                 // method di dalam class
        cout << "Halo, saya " << nama << ", " << umur << " tahun." << endl;
    }
};

int main() {
    Mahasiswa m1;              // membuat objek (TANPA 'new', di stack)
    m1.nama = "Andi";
    m1.umur = 20;
    m1.perkenalan();

    Mahasiswa m2;
    m2.nama = "Budi";
    m2.umur = 22;
    m2.perkenalan();

    return 0;
}"""
            },
            {
                "body": [
                    "Membuat objek dengan 'new' (dynamic allocation, mirip malloc):",
                    "  Mahasiswa *ptr = new Mahasiswa();   // alokasi di heap",
                    "  ptr->nama = \"Citra\";                 // akses lewat -> (seperti C)",
                    "  ptr->perkenalan();",
                    "  delete ptr;                          // WAJIB! (pasangan dari 'new')",
                    "",
                    "  new/delete adalah versi C++ dari malloc/free di C, TAPI",
                    "  new JUGA otomatis memanggil constructor (materi berikutnya),",
                    "  dan delete otomatis memanggil destructor.",
                ]
            },
        ],
    },
    {
        "title": "7. Constructor & Destructor",
        "sections": [
            {
                "body": [
                    "Constructor = method KHUSUS yang otomatis dipanggil saat",
                    "objek dibuat, biasanya untuk inisialisasi atribut.",
                    "  - Nama constructor SAMA PERSIS dengan nama class.",
                    "  - TIDAK punya tipe kembali (bahkan tidak 'void').",
                    "",
                    "Destructor = method KHUSUS yang otomatis dipanggil saat",
                    "objek 'dihancurkan' (keluar dari scope, atau delete untuk",
                    "objek hasil 'new') - biasanya untuk membersihkan resource.",
                    "  - Nama destructor: ~NamaClass() (diawali tanda ~)",
                    "  - TIDAK punya parameter, TIDAK bisa di-overload.",
                ]
            },
            {
                "heading": "Contoh constructor & destructor",
                "code": """#include <iostream>
#include <string>
using namespace std;

class Mahasiswa {
public:
    string nama;
    int umur;

    Mahasiswa(string n, int u) {        // constructor
        nama = n;
        umur = u;
        cout << "Objek " << nama << " dibuat." << endl;
    }

    ~Mahasiswa() {                       // destructor
        cout << "Objek " << nama << " dihancurkan." << endl;
    }

    void perkenalan() {
        cout << "Halo, saya " << nama << ", " << umur << " tahun." << endl;
    }
};

int main() {
    Mahasiswa m1("Andi", 20);    // constructor otomatis terpanggil
    m1.perkenalan();

    {
        Mahasiswa m2("Budi", 22);
        m2.perkenalan();
    }   // m2 keluar scope di sini -> destructor m2 OTOMATIS terpanggil

    cout << "Program hampir selesai..." << endl;
    return 0;
}   // m1 keluar scope -> destructor m1 terpanggil di sini"""
            },
            {
                "body": [
                    "Constructor overloading (BOLEH punya beberapa constructor,",
                    "sama seperti function overloading):",
                    "  class Mahasiswa {",
                    "  public:",
                    "      Mahasiswa() { nama = \"Tanpa Nama\"; }        // default constructor",
                    "      Mahasiswa(string n) { nama = n; }            // dengan 1 parameter",
                    "      Mahasiswa(string n, int u) { nama=n; umur=u; } // dengan 2 parameter",
                    "  };",
                    "",
                    "Initializer list (cara LEBIH EFISIEN inisialisasi atribut):",
                    "  Mahasiswa(string n, int u) : nama(n), umur(u) {",
                    "      // body constructor, atribut SUDAH terisi sebelum masuk sini",
                    "  }",
                ]
            },
        ],
    },
    {
        "title": "8. Encapsulation: private, public, protected",
        "sections": [
            {
                "body": [
                    "Access modifier di C++ (SAMA KONSEPNYA dengan Java):",
                    "  public    -> bisa diakses dari MANA SAJA (luar class).",
                    "  private   -> HANYA bisa diakses di dalam class itu sendiri.",
                    "  protected -> class sendiri + subclass (materi inheritance).",
                    "",
                    "DEFAULT untuk 'class' adalah private (beda dari struct",
                    "yang default-nya public).",
                    "",
                    "Praktik standar: atribut dibuat PRIVATE, akses lewat",
                    "method getter/setter PUBLIC (sama seperti Java).",
                ]
            },
            {
                "heading": "Contoh encapsulation dengan getter/setter",
                "code": """#include <iostream>
#include <string>
using namespace std;

class Rekening {
private:
    string pemilik;
    double saldo;         // TIDAK bisa diakses langsung dari luar!

public:
    Rekening(string p, double s) : pemilik(p), saldo(s) {}

    // Getter
    string getPemilik() const { return pemilik; }   // const: method TIDAK ubah data
    double getSaldo() const { return saldo; }

    // Setter dengan validasi
    void setor(double jumlah) {
        if (jumlah > 0) {
            saldo += jumlah;
        }
    }

    bool tarik(double jumlah) {
        if (jumlah > 0 && jumlah <= saldo) {
            saldo -= jumlah;
            return true;
        }
        return false;
    }
};

int main() {
    Rekening r("Andi", 100000);

    // r.saldo = 999999;   // ERROR! saldo private, tidak bisa diakses langsung

    r.setor(50000);
    cout << "Saldo: " << r.getSaldo() << endl;   // 150000, HANYA lewat getter

    bool berhasil = r.tarik(200000);
    cout << "Tarik berhasil? " << berhasil << endl;   // 0 (false, saldo kurang)

    return 0;
}"""
            },
            {
                "body": [
                    "Keyword 'const' pada method (const string getPemilik() const):",
                    "  const DI AKHIR signature method menandakan method TIDAK",
                    "  akan mengubah atribut objek - compiler akan ERROR jika",
                    "  di dalam method itu tetap ada percobaan mengubah atribut.",
                    "  Praktik BAIK: tandai const untuk SEMUA getter/method yang",
                    "  hanya 'membaca' data, tidak mengubahnya.",
                ]
            },
        ],
    },
    {
        "title": "9. Inheritance (Pewarisan)",
        "sections": [
            {
                "body": [
                    "Inheritance C++ mirip konsepnya dengan Java, sintaks",
                    "sedikit beda: pakai titik dua (:) bukan 'extends'.",
                    "",
                    "  class Anak : public Induk {",
                    "      // atribut/method tambahan",
                    "  };",
                    "",
                    "'public' sebelum nama class induk menentukan bagaimana",
                    "member induk diwariskan (public inheritance PALING umum",
                    "dipakai - anggap saja standar, mirip 'extends' di Java).",
                ]
            },
            {
                "heading": "Contoh inheritance dengan constructor",
                "code": """#include <iostream>
#include <string>
using namespace std;

class Hewan {
protected:                    // BISA diakses subclass (beda dari private)
    string nama;

public:
    Hewan(string n) : nama(n) {}

    void bersuara() {
        cout << nama << " bersuara." << endl;
    }
};

class Kucing : public Hewan {
public:
    Kucing(string n) : Hewan(n) {}   // panggil constructor induk

    void bersuara() {                 // TIDAK otomatis override tanpa 'virtual'!
        cout << nama << ": Meong!" << endl;   // nama bisa diakses (protected)
    }
};

int main() {
    Kucing k("Tom");
    k.bersuara();          // Tom: Meong!

    Hewan h("Generic");
    h.bersuara();          // Generic bersuara.

    return 0;
}"""
            },
            {
                "body": [
                    "PENTING - perbedaan dari Java: method di atas TEKNISNYA",
                    "BUKAN 'override' sungguhan tanpa keyword 'virtual' - method",
                    "yang dipanggil ditentukan berdasarkan TIPE STATIS variabel,",
                    "bukan tipe objek sebenarnya (dibahas detail di materi",
                    "Polymorphism berikutnya - virtual sangat penting!).",
                    "",
                    "Jenis inheritance access specifier:",
                    "  class B : public A     -> public tetap public, protected tetap protected",
                    "  class B : protected A  -> public JADI protected di B",
                    "  class B : private A    -> SEMUA jadi private di B (paling jarang dipakai)",
                    "",
                    "C++ (BEDA dari Java) MENDUKUNG multiple inheritance:",
                    "  class C : public A, public B { ... }   // mewarisi dari A DAN B",
                ]
            },
        ],
    },
    {
        "title": "10. Polymorphism & Virtual Function",
        "sections": [
            {
                "body": [
                    "Tanpa keyword 'virtual', C++ TIDAK melakukan polymorphism",
                    "runtime sungguhan - inilah yang membedakan dari Java (yang",
                    "SEMUA method-nya otomatis virtual).",
                    "",
                    "virtual = menandai method BOLEH di-override oleh subclass,",
                    "dan method yang DIPANGGIL akan sesuai TIPE OBJEK SEBENARNYA",
                    "(runtime), bukan tipe variabel yang dideklarasikan (static).",
                ]
            },
            {
                "heading": "Contoh polymorphism dengan virtual function",
                "code": """#include <iostream>
#include <string>
using namespace std;

class Hewan {
protected:
    string nama;
public:
    Hewan(string n) : nama(n) {}

    virtual void bersuara() {        // 'virtual' AKTIFKAN polymorphism!
        cout << nama << " bersuara." << endl;
    }

    virtual ~Hewan() {}               // destructor JUGA harus virtual di base class!
};

class Kucing : public Hewan {
public:
    Kucing(string n) : Hewan(n) {}

    void bersuara() override {        // 'override' (C++11+): eksplisit & dicek compiler
        cout << nama << ": Meong!" << endl;
    }
};

class Anjing : public Hewan {
public:
    Anjing(string n) : Hewan(n) {}

    void bersuara() override {
        cout << nama << ": Guk!" << endl;
    }
};

int main() {
    Hewan *h1 = new Kucing("Tom");    // pointer BERTIPE Hewan, tapi OBJEK Kucing!
    Hewan *h2 = new Anjing("Bobby");

    h1->bersuara();    // Tom: Meong!  (karena virtual, method Kucing yang dipanggil)
    h2->bersuara();    // Bobby: Guk!

    delete h1;          // destructor virtual PENTING agar Kucing's destructor
    delete h2;          // ikut terpanggil, bukan hanya Hewan's destructor

    return 0;
}"""
            },
            {
                "body": [
                    "Kenapa destructor HARUS virtual di base class (jika class",
                    "akan dipakai secara polymorphic seperti contoh di atas)?",
                    "  Tanpa 'virtual ~Hewan()', 'delete h1;' HANYA akan memanggil",
                    "  ~Hewan() (destructor induk), TIDAK memanggil ~Kucing() -",
                    "  ini menyebabkan RESOURCE LEAK jika Kucing punya resource",
                    "  sendiri yang perlu dibersihkan (misal dynamic memory).",
                    "",
                    "'override' keyword (C++11+): TIDAK WAJIB secara teknis, tapi",
                    "SANGAT DISARANKAN - compiler akan ERROR jika kamu salah tulis",
                    "signature method (typo nama, parameter beda), membantu",
                    "menangkap bug lebih awal dibanding tanpa keyword ini.",
                ]
            },
        ],
    },
    {
        "title": "11. Abstract Class & Pure Virtual Function",
        "sections": [
            {
                "body": [
                    "Pure virtual function = method virtual TANPA implementasi,",
                    "ditandai '= 0' di akhir deklarasi. Class yang punya MINIMAL",
                    "satu pure virtual function otomatis jadi ABSTRACT CLASS -",
                    "TIDAK BISA dibuat objeknya langsung (mirip abstract Java).",
                    "",
                    "  class Bentuk {",
                    "  public:",
                    "      virtual double luas() = 0;   // pure virtual - WAJIB di-override",
                    "  };",
                    "",
                    "C++ TIDAK punya keyword 'interface' terpisah seperti Java -",
                    "'interface' di C++ biasanya berupa abstract class yang",
                    "SEMUA method-nya pure virtual (tanpa atribut data).",
                ]
            },
            {
                "heading": "Contoh abstract class sebagai 'interface'",
                "code": """#include <iostream>
using namespace std;

class Bentuk {                          // abstract class ('interface')
public:
    virtual double luas() = 0;          // pure virtual, WAJIB di-override
    virtual void tampilkanInfo() {       // virtual biasa BOLEH punya isi
        cout << "Luas: " << luas() << endl;
    }
    virtual ~Bentuk() {}
};

class Lingkaran : public Bentuk {
private:
    double radius;
public:
    Lingkaran(double r) : radius(r) {}
    double luas() override {             // WAJIB implement, kalau tidak: error!
        return 3.14159 * radius * radius;
    }
};

class Persegi : public Bentuk {
private:
    double sisi;
public:
    Persegi(double s) : sisi(s) {}
    double luas() override {
        return sisi * sisi;
    }
};

int main() {
    // Bentuk b;               // ERROR! abstract class tidak bisa di-instansiasi

    Bentuk *bentuk1 = new Lingkaran(7);
    Bentuk *bentuk2 = new Persegi(5);

    bentuk1->tampilkanInfo();   // Luas: 153.938
    bentuk2->tampilkanInfo();   // Luas: 25

    delete bentuk1;
    delete bentuk2;
    return 0;
}"""
            },
            {
                "body": [
                    "Kenapa abstract class/interface berguna:",
                    "  - Menjamin SEMUA subclass punya method tertentu (kontrak).",
                    "  - Memungkinkan menulis kode yang bekerja dengan TIPE INDUK",
                    "    (Bentuk*), otomatis bekerja untuk SEMUA turunannya.",
                    "  - Dasar dari banyak design pattern (Strategy, Factory, dll).",
                ]
            },
        ],
    },
    {
        "title": "12. Operator Overloading",
        "sections": [
            {
                "body": [
                    "C++ (BEDA dari Java) mengizinkan OPERATOR (+, -, ==, <<,",
                    "dll) di-DEFINISIKAN ULANG untuk class buatan sendiri, agar",
                    "objek bisa dipakai dengan sintaks yang natural.",
                    "",
                    "  Titik a(1, 2), b(3, 4);",
                    "  Titik c = a + b;   // 'BISA' jika operator+ di-overload!",
                ]
            },
            {
                "heading": "Contoh operator overloading",
                "code": """#include <iostream>
using namespace std;

class Titik {
public:
    int x, y;

    Titik(int x = 0, int y = 0) : x(x), y(y) {}

    // Overload operator + : mengembalikan Titik baru hasil penjumlahan
    Titik operator+(const Titik &lain) const {
        return Titik(x + lain.x, y + lain.y);
    }

    // Overload operator == : membandingkan dua Titik
    bool operator==(const Titik &lain) const {
        return x == lain.x && y == lain.y;
    }

    // Overload operator << untuk cout (harus 'friend' karena cout di kiri)
    friend ostream& operator<<(ostream &os, const Titik &t) {
        os << "(" << t.x << ", " << t.y << ")";
        return os;
    }
};

int main() {
    Titik a(1, 2), b(3, 4);

    Titik c = a + b;              // memanggil operator+ yang kita buat
    cout << c << endl;             // (4, 6) -- lewat operator<<

    cout << (a == Titik(1, 2)) << endl;   // 1 (true)
    cout << (a == b) << endl;              // 0 (false)

    return 0;
}"""
            },
            {
                "body": [
                    "Operator yang UMUM di-overload: +, -, *, /, ==, !=, <, >,",
                    "<<, >>, [], (), = (assignment operator).",
                    "",
                    "Aturan/etika operator overloading:",
                    "  1. Perilaku operator HARUS 'masuk akal' & intuitif -",
                    "     jangan overload '+' untuk melakukan PENGURANGAN!",
                    "  2. Gunakan 'const' pada parameter & method jika operator",
                    "     tidak seharusnya mengubah objek.",
                    "  3. Jangan berlebihan - overload HANYA jika benar-benar",
                    "     membuat kode lebih jelas dibaca (misal untuk Vector,",
                    "     Matrix, Complex Number - bukan untuk SEMUA class).",
                ]
            },
        ],
    },
    {
        "title": "13. Templates (Generic Programming)",
        "sections": [
            {
                "body": [
                    "Template = cara membuat fungsi/class yang bekerja dengan",
                    "BERBAGAI tipe data TANPA menulis ulang kode (mirip Generics",
                    "di Java, tapi konsepnya lebih 'dalam' - template di-compile",
                    "ULANG untuk tiap tipe yang dipakai).",
                    "",
                    "  template <typename T>",
                    "  T maksimum(T a, T b) {",
                    "      return (a > b) ? a : b;",
                    "  }",
                    "",
                    "  maksimum(3, 7);        // T otomatis jadi int",
                    "  maksimum(3.5, 2.1);    // T otomatis jadi double",
                ]
            },
            {
                "heading": "Function template & class template",
                "code": """#include <iostream>
using namespace std;

// Function template
template <typename T>
T maksimum(T a, T b) {
    return (a > b) ? a : b;
}

// Class template
template <typename T>
class Kotak {
private:
    T isi;
public:
    void simpan(T nilai) { isi = nilai; }
    T ambil() { return isi; }
};

int main() {
    cout << maksimum(3, 7) << endl;         // 7 (T = int)
    cout << maksimum(3.5, 2.1) << endl;     // 3.5 (T = double)
    cout << maksimum(string("apel"), string("jeruk")) << endl;  // "jeruk" (T = string)

    Kotak<int> kotakAngka;
    kotakAngka.simpan(100);
    cout << kotakAngka.ambil() << endl;     // 100

    Kotak<string> kotakNama;
    kotakNama.simpan("Andi");
    cout << kotakNama.ambil() << endl;      // Andi

    return 0;
}"""
            },
            {
                "body": [
                    "Template dengan BANYAK tipe parameter:",
                    "  template <typename K, typename V>",
                    "  class Pasangan {",
                    "      K key; V value;",
                    "      // ...",
                    "  };",
                    "  Pasangan<string, int> p;   // K=string, V=int",
                    "",
                    "STL (dibahas materi selanjutnya) SELURUHNYA dibangun",
                    "dengan template - inilah kenapa vector<int>, map<string,int>,",
                    "dsb BISA bekerja dengan tipe data APAPUN yang kamu tentukan.",
                ]
            },
        ],
    },
    {
        "title": "14. STL: Vector & Array Container",
        "sections": [
            {
                "body": [
                    "STL (Standard Template Library) menyediakan struktur data",
                    "SIAP PAKAI - kamu TIDAK perlu implementasi manual linked",
                    "list/dynamic array seperti di C.",
                    "",
                    "vector<T> = 'array dinamis' - ukurannya BISA bertambah/",
                    "berkurang otomatis (mirip ArrayList Java / list Python),",
                    "PALING SERING dipakai dari semua container STL.",
                ]
            },
            {
                "heading": "Contoh operasi vector",
                "code": """#include <iostream>
#include <vector>
#include <array>
using namespace std;

int main() {
    vector<int> nilai = {80, 90, 75, 85};   // inisialisasi langsung

    nilai.push_back(95);          // tambah di akhir (mirip ArrayList.add)
    cout << "Ukuran: " << nilai.size() << endl;   // 5

    for (size_t i = 0; i < nilai.size(); i++) {
        cout << nilai[i] << " ";   // akses seperti array biasa
    }
    cout << endl;

    // range-based for (C++11+) - cara MODERN & ringkas
    for (int n : nilai) {
        cout << n << " ";
    }
    cout << endl;

    nilai.pop_back();             // hapus elemen TERAKHIR
    cout << "Setelah pop_back, ukuran: " << nilai.size() << endl;

    // array<T, N> (C++11+) - alternatif array C dengan ukuran TETAP tapi lebih aman
    array<int, 3> tetap = {1, 2, 3};
    cout << "array ukuran tetap: " << tetap.size() << endl;

    return 0;
}"""
            },
            {
                "body": [
                    "Method vector yang sering dipakai:",
                    "  push_back(x)   -> tambah di akhir",
                    "  pop_back()     -> hapus elemen terakhir",
                    "  size()         -> jumlah elemen",
                    "  empty()        -> true jika kosong",
                    "  clear()        -> hapus SEMUA elemen",
                    "  front()/back() -> elemen pertama/terakhir",
                    "  insert(pos, x) -> sisipkan di posisi tertentu",
                    "  erase(pos)     -> hapus di posisi tertentu",
                    "",
                    "Kenapa vector LEBIH DISARANKAN dari array C biasa:",
                    "  - Ukuran dinamis, tidak perlu tahu jumlah elemen di awal.",
                    "  - Otomatis mengelola memori (tidak perlu malloc/free manual).",
                    "  - Punya bounds-checking OPSIONAL dengan .at(i) (throw",
                    "    exception jika index salah, beda dengan [i] yang tidak cek).",
                ]
            },
        ],
    },
    {
        "title": "15. STL: Map, Set & Pair",
        "sections": [
            {
                "body": [
                    "map<K, V> = struktur key-value TERURUT (berdasarkan key),",
                    "mirip TreeMap Java. Ada juga unordered_map (mirip HashMap,",
                    "TIDAK terurut tapi rata-rata lebih cepat O(1)).",
                    "",
                    "set<T> = koleksi elemen UNIK & TERURUT (mirip TreeSet Java).",
                    "Ada juga unordered_set untuk versi tanpa urutan (lebih cepat).",
                ]
            },
            {
                "heading": "Contoh map & set",
                "code": """#include <iostream>
#include <map>
#include <set>
#include <string>
using namespace std;

int main() {
    map<string, int> nilai;
    nilai["Andi"] = 85;
    nilai["Budi"] = 90;
    nilai["Citra"] = 78;

    cout << nilai["Andi"] << endl;   // 85

    // Iterasi map (otomatis TERURUT berdasarkan key)
    for (const auto &pasangan : nilai) {
        cout << pasangan.first << " -> " << pasangan.second << endl;
    }

    // Cek key ada/tidak (count mengembalikan 0 atau 1 untuk map biasa)
    if (nilai.count("Dedi") == 0) {
        cout << "Dedi tidak ditemukan" << endl;
    }

    // set - hanya elemen unik
    set<int> angka = {5, 2, 8, 2, 5, 1};
    cout << "Ukuran set: " << angka.size() << endl;   // 4 (duplikat hilang)
    for (int n : angka) {
        cout << n << " ";    // 1 2 5 8 (OTOMATIS terurut!)
    }
    cout << endl;

    return 0;
}"""
            },
            {
                "heading": "pair - menyimpan 2 nilai sekaligus",
                "code": """#include <iostream>
#include <utility>
#include <vector>
#include <string>
using namespace std;

int main() {
    pair<string, int> mahasiswa = {"Andi", 20};

    cout << mahasiswa.first << " berumur " << mahasiswa.second << " tahun" << endl;

    // make_pair - cara alternatif membuat pair
    auto p2 = make_pair("Budi", 22);
    cout << p2.first << ", " << p2.second << endl;

    // pair sering dipakai sebagai elemen vector untuk data 2 kolom
    vector<pair<string, int>> daftar;
    daftar.push_back({"Citra", 21});
    daftar.push_back({"Dedi", 23});

    for (const auto &m : daftar) {
        cout << m.first << ": " << m.second << endl;
    }
    return 0;
}"""
            },
        ],
    },
    {
        "title": "16. STL: Algorithm Library",
        "sections": [
            {
                "body": [
                    "<algorithm> menyediakan FUNGSI SIAP PAKAI untuk operasi",
                    "umum pada container (vector, array, dll) - menghindari",
                    "penulisan loop manual berulang-ulang untuk hal yang sama.",
                ]
            },
            {
                "heading": "Contoh sort, find, dan fungsi algorithm umum",
                "code": """#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
using namespace std;

int main() {
    vector<int> data = {5, 2, 8, 1, 9, 3};

    sort(data.begin(), data.end());              // urutkan ascending
    for (int n : data) cout << n << " ";
    cout << endl;   // 1 2 3 5 8 9

    sort(data.begin(), data.end(), greater<int>());  // urutkan descending
    for (int n : data) cout << n << " ";
    cout << endl;   // 9 8 5 3 2 1

    // find - mencari elemen, kembalikan iterator
    auto it = find(data.begin(), data.end(), 5);
    if (it != data.end()) {
        cout << "Ditemukan di posisi: " << (it - data.begin()) << endl;
    }

    cout << "Max: " << *max_element(data.begin(), data.end()) << endl;
    cout << "Min: " << *min_element(data.begin(), data.end()) << endl;

    int total = accumulate(data.begin(), data.end(), 0);  // butuh <numeric>
    cout << "Total: " << total << endl;

    // count_if dengan lambda (materi berikutnya)
    int jumlahGenap = count_if(data.begin(), data.end(),
                                [](int n) { return n % 2 == 0; });
    cout << "Jumlah genap: " << jumlahGenap << endl;

    return 0;
}"""
            },
            {
                "body": [
                    "Fungsi algorithm yang sering dipakai:",
                    "  sort(begin, end)          -> urutkan",
                    "  reverse(begin, end)       -> balik urutan",
                    "  find(begin, end, nilai)   -> cari elemen",
                    "  max_element/min_element   -> elemen terbesar/terkecil",
                    "  count(begin, end, nilai)  -> hitung kemunculan nilai",
                    "  count_if(begin, end, fn)  -> hitung yang memenuhi kondisi",
                    "  all_of/any_of/none_of      -> cek kondisi semua/sebagian/tidak ada",
                    "",
                    ".begin() dan .end() adalah ITERATOR - 'penunjuk' posisi",
                    "elemen pertama dan SATU-SETELAH-elemen-terakhir dalam",
                    "container, dipakai HAMPIR SEMUA fungsi algorithm STL.",
                ]
            },
        ],
    },
    {
        "title": "17. Smart Pointer: unique_ptr & shared_ptr",
        "sections": [
            {
                "body": [
                    "Smart pointer (C++11+, dari <memory>) mengOTOMATISKAN",
                    "manajemen memori - TIDAK perlu delete manual lagi, mengatasi",
                    "MASALAH UTAMA new/delete manual (lupa delete = memory leak,",
                    "delete dua kali = crash - sama seperti masalah malloc/free di C).",
                    "",
                    "unique_ptr<T> - KEPEMILIKAN TUNGGAL:",
                    "  HANYA SATU unique_ptr yang boleh 'memiliki' objek pada",
                    "  satu waktu. Otomatis delete objek saat unique_ptr keluar",
                    "  scope. TIDAK BISA disalin, HANYA bisa dipindah (move).",
                    "",
                    "shared_ptr<T> - KEPEMILIKAN BERSAMA:",
                    "  BOLEH ada BANYAK shared_ptr menunjuk objek yang SAMA.",
                    "  Objek dihapus OTOMATIS saat shared_ptr TERAKHIR yang",
                    "  menunjuknya keluar scope (reference counting).",
                ]
            },
            {
                "heading": "Contoh unique_ptr & shared_ptr",
                "code": """#include <iostream>
#include <memory>
#include <string>
using namespace std;

class Mahasiswa {
public:
    string nama;
    Mahasiswa(string n) : nama(n) {
        cout << "Mahasiswa " << nama << " dibuat" << endl;
    }
    ~Mahasiswa() {
        cout << "Mahasiswa " << nama << " dihapus" << endl;
    }
};

int main() {
    // unique_ptr - kepemilikan tunggal, TIDAK perlu delete manual!
    {
        unique_ptr<Mahasiswa> u1 = make_unique<Mahasiswa>("Andi");
        cout << u1->nama << endl;
        // delete OTOMATIS terjadi saat u1 keluar scope di sini
    }
    cout << "--- setelah blok unique_ptr ---" << endl;

    // shared_ptr - kepemilikan bersama, dihitung reference-nya
    {
        shared_ptr<Mahasiswa> s1 = make_shared<Mahasiswa>("Budi");
        cout << "Reference count: " << s1.use_count() << endl;   // 1
        {
            shared_ptr<Mahasiswa> s2 = s1;    // s2 JUGA menunjuk objek yang sama
            cout << "Reference count: " << s1.use_count() << endl;   // 2
        }   // s2 keluar scope, count berkurang jadi 1 (objek BELUM dihapus)
        cout << "Reference count: " << s1.use_count() << endl;   // 1
    }   // s1 keluar scope, count jadi 0 -> BARU objek dihapus di sini

    return 0;
}"""
            },
            {
                "body": [
                    "ATURAN EMAS C++ modern: HINDARI 'new' dan 'delete' manual -",
                    "SELALU pakai smart pointer (make_unique/make_shared) untuk",
                    "dynamic memory allocation. Ini menghilangkan HAMPIR SEMUA",
                    "bug memory leak & dangling pointer yang umum di C/C++ lama.",
                    "",
                    "Kapan pakai unique_ptr vs shared_ptr:",
                    "  - unique_ptr: DEFAULT pilihan, dipakai saat kepemilikan JELAS",
                    "    tunggal (paling umum, overhead paling kecil).",
                    "  - shared_ptr: HANYA saat BENAR-BENAR butuh banyak 'pemilik'",
                    "    yang sah atas objek yang sama (ada overhead reference",
                    "    counting, sedikit lebih lambat dari unique_ptr).",
                ]
            },
        ],
    },
    {
        "title": "18. Exception Handling",
        "sections": [
            {
                "body": [
                    "Exception handling C++ mirip Java: try-catch-throw.",
                    "BEDA dari C yang tidak punya mekanisme ini secara bawaan",
                    "(C biasanya pakai return code untuk menandakan error).",
                    "",
                    "  try {",
                    "      // kode yang mungkin error",
                    "  } catch (TipeException &e) {",
                    "      // penanganan error",
                    "  }",
                    "",
                    "<stdexcept> menyediakan class exception bawaan:",
                    "  std::runtime_error, std::invalid_argument,",
                    "  std::out_of_range, std::logic_error",
                ]
            },
            {
                "heading": "Contoh try-catch & custom exception",
                "code": """#include <iostream>
#include <stdexcept>
using namespace std;

double bagi(double a, double b) {
    if (b == 0) {
        throw runtime_error("Tidak bisa membagi dengan nol!");
    }
    return a / b;
}

// Custom exception class (turunan dari std::exception)
class SaldoTidakCukup : public exception {
private:
    string pesan;
public:
    SaldoTidakCukup(string p) : pesan(p) {}
    const char* what() const noexcept override {
        return pesan.c_str();
    }
};

int main() {
    try {
        cout << bagi(10, 2) << endl;   // 5
        cout << bagi(10, 0) << endl;   // akan throw
    } catch (const runtime_error &e) {
        cout << "Error: " << e.what() << endl;
    }

    try {
        throw SaldoTidakCukup("Saldo tidak cukup untuk transaksi ini");
    } catch (const exception &e) {     // base class exception menangkap SEMUA turunannya
        cout << "Error khusus: " << e.what() << endl;
    }

    cout << "Program tetap lanjut setelah exception ditangani." << endl;
    return 0;
}"""
            },
            {
                "body": [
                    "Menangkap berdasarkan base class (exception &e) menangkap",
                    "SEMUA jenis exception turunannya - berguna untuk catch-all,",
                    "tapi sebaiknya tangkap tipe SPESIFIK dulu jika perilaku",
                    "penanganannya berbeda per jenis error.",
                    "",
                    "RAII (Resource Acquisition Is Initialization) - PENTING",
                    "dipahami: di C++, exception AMAN dipakai bersama smart",
                    "pointer/objek STL karena destructor TETAP terpanggil",
                    "walau terjadi exception (stack unwinding otomatis) -",
                    "beda dengan C dimana kamu harus manual cleanup di tiap",
                    "kemungkinan jalur keluar fungsi.",
                ]
            },
        ],
    },
    {
        "title": "19. Lambda Expression & Fitur Modern C++",
        "sections": [
            {
                "body": [
                    "Lambda (C++11+) = fungsi anonim ringkas, mirip lambda",
                    "Python/Java atau arrow function JavaScript.",
                    "",
                    "  Sintaks: [capture](parameter) -> tipeKembali { isi }",
                    "",
                    "  auto tambah = [](int a, int b) { return a + b; };",
                    "  cout << tambah(3, 4);   // 7",
                    "",
                    "[capture] menentukan variabel LUAR mana yang bisa diakses",
                    "di dalam lambda:",
                    "  []          -> tidak menangkap variabel luar apa pun",
                    "  [x]         -> menangkap x BY VALUE (salinan)",
                    "  [&x]        -> menangkap x BY REFERENCE (bisa diubah)",
                    "  [=]         -> semua variabel luar by value",
                    "  [&]         -> semua variabel luar by reference",
                ]
            },
            {
                "heading": "Contoh lambda dengan STL algorithm",
                "code": """#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    vector<int> angka = {5, 3, 8, 1, 9, 2};

    // Lambda sebagai comparator custom untuk sort
    sort(angka.begin(), angka.end(), [](int a, int b) {
        return a > b;   // urutkan descending
    });
    for (int n : angka) cout << n << " ";
    cout << endl;   // 9 8 5 3 2 1

    // Lambda dengan capture untuk filter dinamis
    int batas = 5;
    int jumlahDiAtasBatas = count_if(angka.begin(), angka.end(),
        [batas](int n) { return n > batas; });   // capture 'batas' by value
    cout << "Jumlah di atas " << batas << ": " << jumlahDiAtasBatas << endl;

    // Lambda dengan capture by reference untuk akumulasi
    int total = 0;
    for_each(angka.begin(), angka.end(), [&total](int n) {
        total += n;      // &total: bisa MENGUBAH variabel luar
    });
    cout << "Total: " << total << endl;

    return 0;
}"""
            },
            {
                "body": [
                    "Fitur modern C++ lain yang sering dipakai (C++11 ke atas):",
                    "",
                    "  auto - type inference (compiler tebak tipe otomatis):",
                    "    auto x = 10;              // int",
                    "    auto nama = string(\"Andi\"); // string",
                    "",
                    "  range-based for (C++11):",
                    "    for (int n : vektor) { ... }         // by value (salinan)",
                    "    for (int &n : vektor) { n *= 2; }     // by reference (bisa ubah)",
                    "    for (const auto &item : vektor) { ... } // paling umum: aman & efisien",
                    "",
                    "  nullptr (C++11) menggantikan NULL/0 untuk pointer kosong:",
                    "    int *ptr = nullptr;   // lebih type-safe dari NULL",
                    "",
                    "  structured bindings (C++17) untuk pair/tuple:",
                    "    auto [nama, umur] = pasangan;   // langsung destructure",
                ]
            },
        ],
    },
    {
        "title": "20. RAII & Move Semantics (Lanjutan)",
        "sections": [
            {
                "body": [
                    "RAII (Resource Acquisition Is Initialization) = PRINSIP",
                    "PALING PENTING dalam C++ modern: ikat SIKLUS HIDUP resource",
                    "(memori, file, koneksi, lock) dengan siklus hidup OBJEK.",
                    "  - Resource DIAMBIL di constructor.",
                    "  - Resource DILEPASKAN di destructor.",
                    "  - Karena destructor OTOMATIS terpanggil saat objek keluar",
                    "    scope (bahkan saat exception!), resource TIDAK PERNAH",
                    "    'bocor' - inilah kenapa smart pointer, vector, string,",
                    "    fstream SEMUA bekerja tanpa perlu cleanup manual.",
                ]
            },
            {
                "heading": "Contoh RAII sederhana (file handler otomatis)",
                "code": """#include <iostream>
#include <fstream>
#include <string>
using namespace std;

class FileLogger {
private:
    ofstream file;
public:
    FileLogger(string namaFile) {
        file.open(namaFile);           // resource DIAMBIL di constructor
        cout << "File dibuka." << endl;
    }
    void tulis(string pesan) {
        file << pesan << endl;
    }
    ~FileLogger() {                     // resource DILEPAS di destructor
        file.close();
        cout << "File otomatis ditutup." << endl;
    }
};

int main() {
    {
        FileLogger logger("log.txt");
        logger.tulis("Aplikasi dimulai");
        logger.tulis("Proses selesai");
    }   // logger keluar scope -> destructor otomatis -> file OTOMATIS tertutup!

    cout << "Program selesai, tidak perlu close() manual." << endl;
    return 0;
}"""
            },
            {
                "body": [
                    "Move semantics (C++11+, konsep LANJUTAN): mekanisme untuk",
                    "'MEMINDAHKAN' resource dari satu objek ke objek lain TANPA",
                    "menyalin (copy) data yang mahal, memakai rvalue reference (&&).",
                    "",
                    "  vector<int> buatVector() {",
                    "      vector<int> v = {1,2,3,4,5};",
                    "      return v;    // C++ modern OTOMATIS 'move', bukan copy!",
                    "  }",
                    "  vector<int> hasil = buatVector();   // efisien, tanpa duplikasi data",
                    "",
                    "  std::move(objek) memaksa 'move' secara eksplisit:",
                    "  vector<int> a = {1,2,3};",
                    "  vector<int> b = std::move(a);   // a 'dipindah' ke b, a jadi kosong",
                    "",
                    "Move semantics adalah topik LANJUTAN - untuk pemula, cukup",
                    "PAHAMI bahwa C++ modern OTOMATIS mengoptimalkan banyak kasus",
                    "'return objek besar dari fungsi' tanpa perlu kode tambahan.",
                ]
            },
        ],
    },
    {
        "title": "21. Roadmap Menjadi C++ Programmer Handal",
        "sections": [
            {
                "body": [
                    "Kamu sudah menguasai fondasi C++ yang solid: OOP lengkap",
                    "(inheritance, polymorphism, abstract class), template, STL,",
                    "smart pointer, exception handling, hingga RAII & lambda.",
                    "Digabung dengan fondasi C sebelumnya, kamu punya pemahaman",
                    "LENGKAP dari level memori sampai abstraksi tinggi.",
                    "",
                    "TAHAP 1 - Kuatkan Fondasi (kamu di sini):",
                    "  - Pastikan paham KAPAN pakai reference vs pointer vs",
                    "    smart pointer, dan KAPAN virtual function diperlukan.",
                    "  - Latihan: implementasikan struktur data dengan template",
                    "    sendiri (Stack<T>, Queue<T>) sebelum pakai STL langsung.",
                ]
            },
            {
                "body": [
                    "TAHAP 2 - Perdalam C++ Modern (C++11/14/17/20):",
                    "  - Move semantics & perfect forwarding (topik lanjutan).",
                    "  - constexpr - komputasi saat COMPILE TIME, bukan runtime.",
                    "  - Concepts (C++20) - constraint untuk template yang lebih jelas.",
                    "  - Multithreading dengan <thread>, <mutex>, <atomic>.",
                    "",
                    "TAHAP 3 - Pilih Jalur Spesialisasi:",
                    "  Game Development:",
                    "    - Unreal Engine (C++ adalah bahasa utamanya).",
                    "    - Pelajari game loop, physics engine dasar, rendering.",
                    "  High-Performance/Systems:",
                    "    - Trading systems, embedded systems real-time.",
                    "    - Optimasi performa: cache-friendly code, profiling.",
                    "  Aplikasi Umum:",
                    "    - Qt framework untuk desktop GUI application.",
                    "    - Boost library - 'STL tambahan' yang sangat powerful.",
                ]
            },
            {
                "body": [
                    "TAHAP 4 - Kebiasaan Profesional:",
                    "  1. SELALU pakai smart pointer, HINDARI new/delete manual.",
                    "  2. Kompilasi dengan -Wall -Wextra, aktifkan juga -Wshadow",
                    "     dan -Wconversion untuk menangkap bug lebih banyak.",
                    "  3. Gunakan CMake untuk build system project besar",
                    "     (standar industri, menggantikan Makefile manual).",
                    "  4. Testing dengan Google Test (gtest) atau Catch2.",
                    "  5. Baca 'Effective C++' oleh Scott Meyers - buku wajib",
                    "     untuk memahami idiom & best practice C++ mendalam.",
                    "",
                    "Kebiasaan harian agar handal:",
                    "  1. Ketik ulang semua contoh, JANGAN copy-paste.",
                    "  2. Bandingkan solusi 'gaya C' (pointer, malloc) vs 'gaya",
                    "     C++ modern' (reference, smart pointer, STL) untuk",
                    "     masalah yang sama - pahami TRADE-OFF keduanya.",
                    "  3. Baca kode open source C++ berkualitas (LLVM, dll).",
                    "  4. C++ adalah bahasa yang 'dalam' - jangan berkecil hati",
                    "     jika masih banyak yang belum dipahami; bahkan senior",
                    "     C++ engineer terus belajar nuansa baru bertahun-tahun.",
                ]
            },
        ],
    },
]
