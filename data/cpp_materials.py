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
                    "Satu tambahan kecil yang menghemat berjam-jam kebingungan -",
                    "mulai sekarang pakai perintah yang LEBIH LENGKAP ini:",
                    "",
                    "  g++ -std=c++17 -Wall hello.cpp -o hello",
                    "",
                    "  -std=c++17  memberi tahu compiler VERSI C++ mana yang dipakai.",
                    "  -Wall       menyalakan peringatan; baca peringatannya juga,",
                    "              jangan cuma error-nya.",
                    "",
                    "Kenapa versi itu perlu disebut? C++ direvisi berkala dan tiap",
                    "revisi dinamai tahunnya: C++11 (revisi besar - auto, range-based",
                    "for, smart pointer, lambda), C++14 & C++17 (make_unique,",
                    "structured bindings), lalu C++20. Hampir semua fitur di",
                    "kurikulum ini C++11 ke atas.",
                    "",
                    "Sebagian compiler masih memakai standar LAMA kalau tidak diberi",
                    "tahu, dan pesan errornya sama sekali tidak menyebut-nyebut versi -",
                    "cuma 'make_unique is not a member of std' atau keluhan soal tanda",
                    "kurung yang membingungkan. Menempelkan -std=c++17 sejak sekarang",
                    "membuat semua contoh di materi berikutnya jalan apa adanya.",
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
                    "  7. Header C dipakai lewat nama ber-awalan c dan TANPA",
                    "     .h: <math.h> jadi <cmath>, <stdlib.h> jadi <cstdlib>,",
                    "     <string.h> jadi <cstring>, <time.h> jadi <ctime>.",
                    "     Isinya sama persis; bedanya versi C++ menaruhnya di",
                    "     namespace std. Jadi sqrt(), pow(), abs(), rand(), dan",
                    "     seluruh isi math.h yang kamu pakai di C tetap ada -",
                    "     tulis #include <cmath> lalu panggil seperti biasa.",
                    "",
                    "Yang lama (<math.h>) masih diterima compiler, jadi tidak ada",
                    "error yang memberi tahu kalau kamu memakainya. Pakai bentuk",
                    "baru supaya konsisten dengan sisa kode C++-mu.",
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
        "title": "3. Namespace Sendiri & Operator ::",
        "sections": [
            {
                "body": [
                    "Materi sebelumnya MEMAKAI namespace milik orang lain: std. Sekarang giliranmu",
                    "MEMBUAT sendiri - dan itu yang akan kamu temui di hampir semua kode C++ nyata.",
                    "",
                    "Kenapa namespace ada sama sekali:",
                    "  - Satu program besar memakai banyak pustaka. Dua di antaranya bisa sama-sama",
                    "    punya fungsi bernama hitung(), atau class bernama Timer.",
                    "  - Di C tabrakan itu fatal: linker melihat dua simbol bernama sama lalu menyerah",
                    "    ('multiple definition'). Jalan keluar C adalah menempeli nama dengan awalan",
                    "    buatan tangan - SDL_Init(), gtk_widget_show(), sqlite3_open().",
                    "  - C++ memberi cara resmi: bungkus namanya dalam sebuah namespace, lalu sebut",
                    "    lengkap saat dipakai. Awalannya jadi bagian bahasa, bukan kebiasaan.",
                    "",
                    "Membuat namespace = membuka blok, mengisinya, lalu menutupnya:",
                    "",
                    "  namespace toko {",
                    "      double pajak = 0.11;",
                    "      double hitungTotal(double harga) { ... }",
                    "  }        <- TANPA titik koma (beda dari class yang wajib ditutup '};')",
                    "",
                    "Dari luar, isinya disebut memakai operator :: (scope resolution operator):",
                    "",
                    "  toko::pajak              // variabel pajak yang ada DI DALAM toko",
                    "  toko::hitungTotal(9000)  // fungsinya",
                    "",
                    "Baca :: sebagai 'yang ada di dalam'. Jadi std::cout berarti 'cout yang ada di",
                    "dalam std' - :: bukan sintaks khusus untuk std, melainkan operator umum yang",
                    "berlaku untuk namespace apa pun, termasuk buatanmu sendiri.",
                ],
            },
            {
                "heading": "Contoh namespace sendiri",
                "code": """#include <iostream>
#include <string>
using namespace std;

namespace toko {
    double pajak = 0.11;

    double hitungTotal(double harga) {
        return harga + harga * pajak;   // di DALAM toko, cukup tulis 'pajak'
    }

    namespace detail {                  // namespace DI DALAM namespace
        void catat(string pesan) {
            cout << "[toko] " << pesan << endl;
        }
    }
}

namespace gudang {
    double pajak = 0.0;                 // nama sama dengan toko::pajak, tidak bentrok

    double hitungTotal(double harga) {  // nama fungsi sama, isi beda
        return harga;
    }
}

int main() {
    cout << "Toko  : " << toko::hitungTotal(100000) << endl;
    cout << "Gudang: " << gudang::hitungTotal(100000) << endl;

    toko::detail::catat("dua fungsi bernama sama, nol bentrok");
    return 0;
}""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  Toko  : 111000",
                    "  Gudang: 100000",
                    "  [toko] dua fungsi bernama sama, nol bentrok",
                    "",
                    "Yang perlu ditangkap dari situ:",
                    "  - toko::pajak dan gudang::pajak adalah DUA variabel yang benar-benar berbeda.",
                    "    Namanya kebetulan sama, tempat tinggalnya tidak.",
                    "  - DI DALAM sebuah namespace, isinya sendiri dipanggil polos tanpa awalan -",
                    "    hitungTotal() cukup menulis 'pajak', bukan 'toko::pajak'.",
                    "  - Awalan baru wajib begitu dipanggil dari LUAR, termasuk dari main().",
                    "",
                    "Namespace boleh DIBUKA LAGI berkali-kali, bahkan di berkas yang berbeda:",
                    "",
                    "  namespace toko { void a(); }   // di berkas pertama",
                    "  namespace toko { void b(); }   // di berkas lain - toko yang SAMA, isinya nambah",
                    "",
                    "Itulah cara std bisa tersebar di puluhan header (<iostream>, <string>, <vector>)",
                    "tapi tetap satu namespace. Artinya namespace BUKAN berkas dan bukan class - ia",
                    "cuma sebuah nama yang menempel di depan, dan boleh disambung dari mana saja.",
                    "",
                    "Namespace bersarang punya dua bentuk yang artinya sama persis:",
                    "",
                    "  namespace toko { namespace detail { ... } }   // bentuk klasik, selalu jalan",
                    "  namespace toko::detail { ... }                // bentuk ringkas C++17",
                    "",
                    "Keduanya dipakai sebagai toko::detail::catat(...). Bentuk ringkas butuh compiler",
                    "yang dijalankan minimal C++17: g++ -std=c++17 program.cpp -o program.",
                    "",
                    "Dua jebakan yang benar-benar menjebak:",
                    "  - Penutup namespace TIDAK memakai titik koma, sedangkan class wajib '};'.",
                    "    Tertukar sedikit saja, pesan errornya menunjuk baris yang jauh di bawahnya.",
                    "  - JANGAN menaruh int main() di dalam namespace. Yang dicari linker adalah main",
                    "    di namespace global; app::main tidak dianggap. Dan errornya tidak menyebut",
                    "    namespace sama sekali - cuma 'undefined reference to main'.",
                ],
            },
            {
                "heading": "Contoh using, alias & anonymous namespace",
                "code": """#include <iostream>
#include <string>

using std::cout;      // using-DECLARATION: menarik SATU nama saja
using std::endl;
using std::string;

namespace laporan::format {      // bentuk ringkas C++17
    string tebal(string teks) {
        return "**" + teks + "**";
    }
}

namespace fmt = laporan::format; // ALIAS: nama pendek untuk namespace panjang

namespace {                      // ANONYMOUS: milik berkas INI saja
    int nomorBaris = 0;

    string awalan() {            // fungsi bantu, tak terlihat dari berkas lain
        return "[log] ";
    }
}

int hitung() { return 1; }       // fungsi di namespace GLOBAL

namespace laporan {              // namespace laporan DIBUKA LAGI
    int hitung() { return 2; }   // menutupi hitung() yang global

    void tampil() {
        nomorBaris++;
        cout << awalan() << nomorBaris << ". laporan::hitung=" << hitung()
             << "  ::hitung=" << ::hitung() << endl;   // :: = ambil yang global
    }
}

int main() {
    laporan::tampil();
    laporan::tampil();
    cout << fmt::tebal("selesai") << endl;
    return 0;
}""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  [log] 1. laporan::hitung=2  ::hitung=1",
                    "  [log] 2. laporan::hitung=2  ::hitung=1",
                    "  **selesai**",
                    "",
                    "Tiga cara memendekkan nama, dan bedanya penting:",
                    "",
                    "  using namespace std;             // using-DIRECTIVE: SELURUH isi std terlihat",
                    "  using std::cout;                 // using-DECLARATION: cuma cout",
                    "  namespace fs = std::filesystem;  // ALIAS: nama lain untuk satu namespace",
                    "",
                    "  - using-directive paling ringkas dan paling berisiko: ribuan nama masuk",
                    "    sekaligus. Punya fungsi sendiri bernama count(), distance(), atau size()?",
                    "    Ia bisa bentrok dengan milik std padahal kamu tidak pernah menulis std.",
                    "  - Dua using-directive sekaligus membuat bentroknya muncul di tempat pemakaian,",
                    "    bukan di tempat penulisan: 'call of tampil() is ambiguous', dan compiler",
                    "    menyebut kedua kandidatnya.",
                    "  - using-declaration menarik satu nama saja, jadi terbaca apa yang kamu pinjam.",
                    "  - Alias dipakai untuk namespace panjang atau bersarang, persis seperti fmt di",
                    "    contoh di atas. Ia tidak membuat namespace baru, cuma nama panggilan.",
                    "",
                    "Aturan yang paling sering dilanggar: JANGAN menulis using namespace di berkas",
                    "header (.h). Isi header disalin ke setiap .cpp yang meng-include-nya, jadi satu",
                    "baris itu memaksakan seluruh namespace ke berkas orang lain yang tidak pernah",
                    "memintanya. Di dalam .cpp - apalagi di dalam satu fungsi - masih wajar.",
                    "",
                    "namespace { ... } tanpa nama = anonymous namespace:",
                    "  - Isinya hanya terlihat dari BERKAS tempat ia ditulis. Ini padanan C++ dari",
                    "    kata 'static' di depan fungsi C, dan cara standar menyembunyikan fungsi bantu",
                    "    yang tidak boleh dipanggil berkas lain.",
                    "  - Karena itu nomorBaris dan awalan() di contoh tadi aman: berkas .cpp lain boleh",
                    "    punya nama yang sama tanpa keduanya saling menabrak saat di-link.",
                    "",
                    "::nama tanpa apa pun di depannya = 'ambil yang di namespace GLOBAL'. Berguna saat",
                    "nama lokal menutupi nama global, seperti ::hitung() di contoh tadi.",
                    "",
                    "Terakhir: :: bukan cuma milik namespace. Bentuk yang sama muncul lagi sebagai",
                    "Kelas::metode dan Status::Aktif (enum class) di materi-materi berikutnya. Begitu",
                    "kamu membacanya sebagai 'yang ada di dalam', ketiganya jadi satu aturan yang sama.",
                    "",
                    "Dan namespace tidak menambah beban saat program berjalan - ia diselesaikan",
                    "compiler, bukan saat runtime.",
                ],
            },
        ],
    },
    {
        "title": "4. enum class, Konstanta & Alias Tipe",
        "sections": [
            {
                "body": [
                    "Semua nilai di contoh sejauh ini adalah variabel biasa yang bebas",
                    "diubah kapan saja. Padahal banyak nilai justru TIDAK BOLEH berubah:",
                    "nilai PI, batas maksimum, kode status. Untuk itu ada const.",
                    "",
                    "  const double PI = 3.14159;       // boleh ditulis DI LUAR fungsi",
                    "  constexpr int MAKS_SISWA = 100;",
                    "",
                    "const artinya 'nilainya tidak boleh diubah lagi setelah diberi",
                    "nilai awal'. Menulis PI = 3.14; ditolak compiler dengan pesan:",
                    "  error: assignment of read-only variable 'PI'",
                    "",
                    "Itu bukan kerewelan, itu justru gunanya. Angka mentah yang",
                    "tersebar di banyak tempat ('magic number') lalu suatu hari diubah",
                    "di SEBAGIAN tempat saja adalah bug yang paling melelahkan untuk",
                    "dicari, karena programnya tetap jalan - cuma hasilnya salah. Satu",
                    "konstanta bernama membuat kesalahan itu mustahil.",
                    "",
                    "constexpr (C++11+) satu tingkat lebih kuat: nilainya WAJIB sudah",
                    "bisa dihitung saat KOMPILASI, bukan saat program jalan. Bedanya",
                    "nyata:",
                    "",
                    "  const int a = bacaDariInput();      // BOLEH - diketahui saat jalan",
                    "  constexpr int b = bacaDariInput();  // ERROR - compiler tak sanggup",
                    "",
                    "Kenapa itu berguna: hal-hal yang HARUS pasti sebelum program",
                    "jalan - ukuran array biasa, argumen template, isi static_assert -",
                    "hanya mau menerima nilai constexpr. Fungsi pun boleh constexpr,",
                    "sehingga hasilnya ikut dihitung compiler.",
                    "",
                    "static_assert adalah kerabat dekatnya: satu baris pemeriksaan",
                    "yang dikerjakan compiler, dan kalau salah program GAGAL",
                    "DIKOMPILASI - tidak menunggu bug muncul di tangan pemakai.",
                    "",
                    "Pegangan praktis: pakai const dulu, naikkan ke constexpr kalau",
                    "nilainya memang sudah tetap sejak awal. Kata const nanti muncul",
                    "lagi dalam dua peran lain - 'const string &teks' sebagai",
                    "parameter, dan 'int getSaldo() const' di akhir method - keduanya",
                    "dibahas di materinya sendiri. Janjinya selalu sama: ada sesuatu",
                    "yang dipastikan tidak berubah.",
                ],
            },
            {
                "heading": "Contoh const, constexpr & static_assert",
                "code": """#include <iostream>
using namespace std;

// Konstanta di lingkup berkas: ditulis DI LUAR fungsi, dikenal seluruh berkas.
const double PI = 3.14159;         // nilainya tidak boleh diubah lagi
constexpr int MAKS_SISWA = 100;    // nilainya sudah pasti saat KOMPILASI

// Fungsi constexpr: kalau argumennya konstanta, compiler yang menghitungnya.
constexpr int kuadrat(int n) {
    return n * n;
}

// static_assert: pemeriksaan yang dikerjakan compiler, bukan saat program jalan.
// Kalau salah, program GAGAL DIKOMPILASI - tidak menunggu bug muncul di runtime.
static_assert(kuadrat(4) == 16, "kuadrat(4) seharusnya 16");

int main() {
    double jari = 7.0;
    cout << "Luas lingkaran: " << PI * jari * jari << endl;

    int nilai[MAKS_SISWA];   // ukuran array WAJIB sudah pasti saat kompilasi
    nilai[0] = 90;
    cout << "Kapasitas: " << MAKS_SISWA << ", isi pertama: " << nilai[0] << endl;

    const int batas = 5;     // const juga boleh di dalam fungsi
    cout << "Batas: " << batas << endl;
    cout << "kuadrat(9) = " << kuadrat(9) << endl;

    // PI = 3.14;            // <- error: assignment of read-only variable 'PI'
    // batas = 6;            // <- error yang sama
    return 0;
}""",
            },
            {
                "body": [
                    "Di kursus C kamu sudah bertemu enum: cara memberi NAMA pada",
                    "sekumpulan angka supaya kodenya terbaca - 'if (hari == RABU)',",
                    "bukan 'if (hari == 2)'. C++ mewarisi enum itu apa adanya, jadi",
                    "bentuk lama ini tetap sah:",
                    "",
                    "  enum Warna { MERAH, HIJAU, BIRU };   // otomatis 0, 1, 2",
                    "  Warna w = MERAH;",
                    "",
                    "Masalahnya, enum polos bocor ke dua arah, dan keduanya sudah",
                    "pernah menjatuhkan orang sungguhan:",
                    "",
                    "  1. Nilainya diam-diam berubah jadi int. 'if (w == 0)' LOLOS",
                    "     dikompilasi, begitu juga 'int x = w + 5;'. Padahal 'warna",
                    "     ditambah 5' tidak berarti apa-apa - dan compiler tidak",
                    "     protes sedikit pun.",
                    "  2. Nama anggotanya tumpah keluar dari enum-nya. Menambah",
                    "     'enum Lampu { MERAH, KUNING };' di berkas yang sama gagal:",
                    "       error: 'MERAH' conflicts with a previous declaration",
                    "",
                    "C++11 menambahkan versi yang menutup keduanya - enum class",
                    "(nama resminya 'scoped enum'):",
                    "",
                    "  enum class Status { Aktif, Nonaktif, Diblokir };",
                    "  Status s = Status::Aktif;",
                    "",
                    "Tiga hal yang bikin orang tersandung pertama kali, dijawab satu",
                    "per satu:",
                    "",
                    "  1. Kenapa ada kata 'class' padahal ini bukan class?",
                    "     Kata itu cuma dipinjam. Status tidak jadi punya method,",
                    "     constructor, atau private. Yang dipinjam hanya SIFAT-nya:",
                    "     nama anggotanya terkurung di dalam Status, persis seperti",
                    "     anggota sebuah class terkurung di dalam classnya.",
                    "",
                    "  2. Kenapa harus ditulis Status::Aktif, bukan Aktif saja?",
                    "     Karena justru itu intinya - Aktif memang TIDAK ada di luar",
                    "     Status. Yang dibayar adalah tulisan lebih panjang; yang",
                    "     dibeli adalah kebocoran nomor 2 di atas tertutup, sehingga",
                    "     enum lain di berkas yang sama boleh punya Aktif juga.",
                    "",
                    "  3. Kenapa 'if (s == 0)' TIDAK dikompilasi?",
                    "       error: no match for 'operator=='",
                    "       (operand types are 'Status' and 'int')",
                    "     Scoped enum tidak dikonversi otomatis ke int - itu",
                    "     kebocoran nomor 1 yang sengaja ditutup. Kalau angkanya",
                    "     memang kamu butuhkan (misalnya mau disimpan ke database),",
                    "     minta terang-terangan: static_cast<int>(s). Alasan yang",
                    "     sama membuat 'cout << s;' juga ditolak - cout tidak tahu",
                    "     Status itu apa, jadi cetaklah lewat fungsi pengubah ke",
                    "     teks, persis seperti labelnya() di contoh berikut.",
                ],
            },
            {
                "heading": "enum class sebagai tipe parameter & isi switch",
                "code": """#include <iostream>
#include <string>
using namespace std;

// enum class: di baliknya tetap 0, 1, 2 - tapi TIDAK otomatis jadi int.
enum class Status { Aktif, Nonaktif, Diblokir };

string labelnya(Status s) {          // enum class dipakai sebagai TIPE parameter
    switch (s) {                     // case-nya wajib berawalan Status:: juga
        case Status::Aktif:    return "Akun aktif";
        case Status::Nonaktif: return "Akun nonaktif";
        case Status::Diblokir: return "Akun diblokir";
    }
    return "Status tidak dikenal";
}

int main() {
    Status s = Status::Aktif;        // WAJIB menyebut nama enum-nya di depan
    cout << labelnya(s) << endl;

    s = Status::Diblokir;
    cout << labelnya(s) << endl;

    // if (s == 2) { }               // <- TIDAK dikompilasi: Status bukan int
    if (s == Status::Diblokir) {     // begini yang benar
        cout << "Silakan hubungi admin." << endl;
    }

    // Kalau angkanya memang dibutuhkan, minta terang-terangan:
    cout << "Kode angkanya: " << static_cast<int>(s) << endl;   // 2

    // cout << s;                    // <- ditolak juga: cout tak kenal Status
    return 0;
}""",
            },
            {
                "heading": "Alias tipe: using & typedef",
                "body": [
                    "Alias tipe = NAMA BARU untuk tipe yang sudah ada. Bukan tipe",
                    "baru; cuma nama lain untuk barang yang sama.",
                    "",
                    "  using Daftar = vector<int>;    // bentuk MODERN (C++11+)",
                    "  typedef vector<int> Daftar;    // bentuk LAMA gaya C, sama saja",
                    "",
                    "BACA BAGIAN INI PELAN-PELAN. Kata 'using' di sini SAMA SEKALI",
                    "BEDA artinya dari 'using namespace std;' yang kamu tulis di",
                    "setiap program. Yang itu berarti 'impor semua nama dari",
                    "namespace std'. Yang ini berarti 'mulai sekarang Daftar berarti",
                    "vector<int>'. Satu kata, dua pekerjaan yang tidak berhubungan",
                    "sama sekali - dan pembedanya cuma bentuk barisnya:",
                    "",
                    "  using namespace X;   -> ada 'namespace', TIDAK ada tanda '='",
                    "  using A = B;         -> ada tanda '=', TIDAK ada 'namespace'",
                    "",
                    "Kenapa alias ada di hampir semua header C++ nyata: tipe di sini",
                    "cepat sekali jadi panjang. 'vector<pair<string, int>>' yang",
                    "diulang di lima tanda tangan fungsi jauh lebih sulit dibaca",
                    "daripada 'BukuNilai' - dan kalau suatu hari int-nya harus jadi",
                    "double, kamu cukup mengubah SATU baris alias.",
                    "",
                    "Jebakannya: alias TIDAK membuat tipe baru. Daftar dan",
                    "vector<int> boleh saling ditugaskan bebas, dan compiler tidak",
                    "akan menghentikanmu kalau keduanya tertukar. Kalau yang kamu",
                    "mau adalah tipe yang benar-benar berbeda dan dijaga compiler,",
                    "yang kamu butuhkan class - bukan alias.",
                ],
                "code": """#include <iostream>
#include <string>
#include <utility>
#include <vector>
using namespace std;

// 'using' DI SINI bukan impor namespace - ini memberi NAMA BARU untuk sebuah tipe.
using Daftar = vector<int>;
using Nilai = pair<string, int>;      // satu baris nilai: nama + angka
using BukuNilai = vector<Nilai>;      // alias boleh dibangun dari alias lain

typedef vector<int> DaftarLama;       // bentuk LAMA gaya C, artinya sama persis

void cetak(const Daftar &angka) {     // parameter pun boleh memakai aliasnya
    for (int n : angka) cout << n << " ";
    cout << endl;
}

int main() {
    Daftar angka = {5, 3, 9};
    cetak(angka);

    DaftarLama sama = {1, 2};
    angka = sama;          // BOLEH: alias bukan tipe baru, dua-duanya vector<int>
    cetak(angka);

    BukuNilai buku;
    buku.push_back(Nilai("Andi", 85));
    buku.push_back({"Budi", 90});

    for (const Nilai &baris : buku) {
        cout << baris.first << " -> " << baris.second << endl;
    }
    return 0;
}""",
            },
        ],
    },
    {
        "title": "5. Input/Output Modern (cin & cout)",
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
            {
                "heading": "Tiga aliran keluaran: cout, cerr & clog",
                "body": [
                    "cout bukan satu-satunya. Ada dua saudaranya yang wajib kamu kenali:",
                    "",
                    "  cout  -> keluaran NORMAL program, yaitu HASIL kerjanya.",
                    "  cerr  -> pesan ERROR. Tidak di-buffer, jadi langsung muncul.",
                    "  clog  -> pesan log/diagnostik. Seperti cerr tapi di-buffer.",
                    "",
                    "Ketiganya sama-sama dipakai dengan <<, dan ketiganya dari <iostream>.",
                    "",
                    "Kenapa memisahkan pesan error dari cout itu penting? Karena di",
                    "terminal keluaran program sering DIALIHKAN atau DIPIPA:",
                    "",
                    "  ./program > hasil.txt        (simpan keluarannya ke berkas)",
                    "  ./program | sort             (kirim keluarannya ke program lain)",
                    "",
                    "Yang ikut dialihkan HANYA cout. Pesan cerr tetap tampil di layar.",
                    "Kalau pesan error ikut dicetak lewat cout, dua hal rusak sekaligus:",
                    "berkas hasilnya tercemar kalimat error, dan penggunanya tidak",
                    "melihat apa-apa saat programnya gagal. Aturan praktisnya: DATA ke",
                    "cout, KELUHAN ke cerr.",
                ],
            },
            {
                "heading": "Saat pengguna mengetik huruf padahal diminta angka",
                "body": [
                    "cin TIDAK melempar exception dan TIDAK menghentikan program. Ia",
                    "masuk keadaan GAGAL (fail state): variabelnya tidak terisi, dan",
                    "huruf yang bikin gagal itu TERTINGGAL di antrean masukan.",
                    "",
                    "Akibatnya inilah yang bikin bingung: SEMUA pembacaan cin",
                    "berikutnya ikut gagal seketika tanpa menunggu apa pun. Program",
                    "terlihat 'melompati' semua pertanyaan sisanya lalu selesai.",
                    "",
                    "Memeriksanya:",
                    "  if (!cin) { ... }        // cin langsung dipakai sebagai kondisi",
                    "  if (cin.fail()) { ... }  // sama artinya, ditulis lebih eksplisit",
                    "",
                    "Memulihkannya - WAJIB DUA LANGKAH, satu saja tidak cukup:",
                    "  cin.clear();   // hapus tanda gagal supaya cin mau membaca lagi",
                    "  cin.ignore(numeric_limits<streamsize>::max(), \'\\n\');  // buang barisnya",
                    "",
                    "clear() sendirian tidak menolong: huruf penyebabnya masih di",
                    "antrean dan akan menggagalkan pembacaan berikutnya juga. ignore()",
                    "yang membuangnya sampai ganti baris. numeric_limits butuh <limits>.",
                ],
                "code": """#include <iostream>
#include <limits>
using namespace std;

int main() {
    int umur;
    cout << "Masukkan umur: ";

    if (!(cin >> umur)) {                 // cin >> mengembalikan cin itu sendiri
        cerr << "Itu bukan angka." << endl;   // cerr, BUKAN cout
        cin.clear();                      // hapus tanda gagalnya
        cin.ignore(numeric_limits<streamsize>::max(), '\\n');  // buang sisa barisnya
        umur = 0;
    }
    cout << "Umur tercatat: " << umur << endl;

    // Membaca SAMPAI HABIS: berhenti sendiri saat masukan habis atau gagal
    int n, total = 0;
    while (cin >> n) {
        total += n;
    }
    cout << "Total angka sisanya: " << total << endl;
    return 0;
}"""
            },
            {
                "body": [
                    "Idiom membaca SAMPAI MASUKAN HABIS - pola yang ada di hampir",
                    "semua utilitas baris perintah:",
                    "",
                    "  int n;",
                    "  while (cin >> n) { ... }              // per angka/kata",
                    "",
                    "  string baris;",
                    "  while (getline(cin, baris)) { ... }   // per baris, spasi ikut",
                    "",
                    "Kenapa itu bisa jadi kondisi while? Karena 'cin >> n' MENGEMBALIKAN",
                    "cin itu sendiri, dan cin di dalam if/while bernilai true selama ia",
                    "belum gagal. Loop berhenti sendiri saat masukan habis atau saat ada",
                    "yang tidak cocok tipenya - kamu tidak perlu menghitung jumlah data",
                    "di depan. Prinsip 'mengembalikan stream-nya sendiri' itu juga yang",
                    "membuat cout << a << b << c bisa dirangkai.",
                    "",
                    "Saat dijalankan lewat keyboard, 'masukan habis' ditandai dengan",
                    "Ctrl+D (Linux/macOS) atau Ctrl+Z lalu Enter (Windows). Saat datanya",
                    "dipipa - echo \"1 2 3\" | ./program - habisnya terjadi sendiri.",
                ]
            },
        ],
    },
    {
        "title": "6. String C++ Lebih Dalam & stringstream",
        "sections": [
            {
                "body": [
                    "Di materi Variabel kamu berkenalan dengan string lewat tiga kemampuan saja: +, ==, dan",
                    ".length(). Itu baru pintu depannya. Pekerjaan yang PALING SERING dilakukan sebuah program",
                    "adalah mengolah teks - memotong, mencari, menyambung, mengubah angka jadi teks dan",
                    "sebaliknya - jadi sisa API-nya bukan barang langka yang dipakai sesekali. Ia muncul di",
                    "hampir setiap berkas .cpp yang akan kamu baca.",
                    "",
                    "Yang dipakai sehari-hari:",
                    "  s.size()  / s.length()   -> jumlah karakter. DUA NAMA UNTUK HAL YANG SAMA PERSIS;",
                    "                              size() dipakai supaya seragam dengan vector, map, dan set.",
                    "  s.empty()                -> true kalau isinya kosong. Lebih jelas dari s.size() == 0.",
                    "  s[i]                     -> karakter ke-i (mulai dari 0), TANPA pemeriksaan batas.",
                    "  s.at(i)                  -> sama, TAPI melempar out_of_range kalau i kelewat batas.",
                    "  s += \"lagi\";             -> menempel di akhir. Lebih murah dari s = s + \"lagi\".",
                    "  s.substr(mulai, jumlah)  -> potongan baru sepanjang 'jumlah' huruf.",
                    "  s.find(\"cari\")           -> POSISI kemunculan pertama.",
                    "  s.replace(mulai, n, \"x\") -> ganti n huruf mulai posisi 'mulai' dengan \"x\".",
                    "  s.erase(mulai)           -> buang semuanya mulai posisi itu.",
                    "  a == b  /  a < b         -> bandingkan ISI-nya; < memakai urutan kamus.",
                    "",
                    "string::npos - kenapa namanya aneh",
                    "  find() harus bisa menjawab 'tidak ketemu', padahal yang ia kembalikan adalah nomor",
                    "  posisi. Nol pun sudah dipakai (posisi paling depan). Jadi C++ memilih satu nilai yang",
                    "  MUSTAHIL jadi posisi sungguhan - angka bulat terbesar yang muat - dan memberinya nama",
                    "  string::npos ('no position'). Ia bukan angka ajaib, cuma penanda.",
                    "",
                    "  Karena itu bentuk baku pengecekannya - salah satu baris paling sering muncul di kode",
                    "  C++ mana pun - adalah:",
                    "",
                    "      if (s.find(\"error\") != string::npos) { ... ketemu ... }",
                    "",
                    "  Tulis string::npos apa adanya, jangan diganti -1. Nilai kembalian find bertipe unsigned",
                    "  (size_t), dan membandingkannya dengan -1 adalah cara paling cepat bikin bug yang",
                    "  kelihatan benar tapi keliru.",
                ],
            },
            {
                "heading": "Contoh operasi string yang dipakai sehari-hari",
                "code": """#include <iostream>
#include <string>
using namespace std;

int main() {
    string kalimat = "Belajar C++ itu seru";

    cout << "Panjang : " << kalimat.size() << endl;     // 20
    cout << "Kosong? : " << kalimat.empty() << endl;    // 0 (artinya false)
    cout << "Huruf 0 : " << kalimat[0] << endl;         // B
    cout << "Huruf 8 : " << kalimat.at(8) << endl;      // C

    // substr(mulai, JUMLAH huruf) -- argumen kedua PANJANG, bukan posisi akhir
    cout << kalimat.substr(0, 7) << endl;               // Belajar
    cout << kalimat.substr(8) << endl;                  // C++ itu seru (sampai habis)

    // find mengembalikan POSISI, atau string::npos kalau tidak ketemu
    size_t pos = kalimat.find("itu");
    if (pos != string::npos) {
        cout << "'itu' mulai di posisi " << pos << endl;   // 12
    }
    if (kalimat.find("Java") == string::npos) {
        cout << "'Java' tidak ada di kalimat ini" << endl;
    }

    string sapaan = "Halo";
    sapaan += ", ";            // += menempel di akhir
    sapaan += "Levi";
    cout << sapaan << endl;    // Halo, Levi

    string salinan = kalimat;
    salinan.replace(0, 7, "Latihan");   // ganti 7 huruf mulai posisi 0
    cout << salinan << endl;            // Latihan C++ itu seru
    salinan.erase(7);                   // buang semua huruf mulai posisi 7
    cout << salinan << endl;            // Latihan

    cout << (salinan == "Latihan") << endl;       // 1 -- ISI-nya yang dibandingkan
    cout << (string("apel") < "jeruk") << endl;   // 1 -- urutan kamus (a sebelum j)

    return 0;
}""",
            },
            {
                "body": [
                    "",
                    "MEMBUANG SPASI DI UJUNG: find_first_not_of DAN find_last_not_of",
                    "",
                    "Teks yang datang dari pengguna atau dari berkas hampir selalu membawa",
                    "spasi yang tidak diminta. C++ tidak punya .trim() bawaan seperti bahasa",
                    "lain, jadi bentuk di bawah ini yang dipakai orang - dan sekali kamu",
                    "mengenalinya, ia ada di mana-mana.",
                    "",
                    "  find(x)              -> posisi x yang PERTAMA",
                    "  find_first_not_of(x) -> posisi pertama yang BUKAN x",
                    "  find_last_not_of(x)  -> posisi terakhir yang BUKAN x",
                    "",
                    "Dua yang terakhir menerima sekumpulan karakter sekaligus, bukan satu:",
                    "\" \\t\\n\" berarti 'spasi ATAU tab ATAU baris baru'.",
                    "",
                    "  std::string rapikan(const std::string& s) {",
                    "      const std::string spasi = \" \\t\\n\";",
                    "      std::size_t awal = s.find_first_not_of(spasi);",
                    "      if (awal == std::string::npos) return \"\";   // isinya spasi semua",
                    "      std::size_t akhir = s.find_last_not_of(spasi);",
                    "      return s.substr(awal, akhir - awal + 1);",
                    "  }",
                    "",
                    "Baris npos itu WAJIB ada. Kalau seluruh isinya spasi, tidak ada satu pun",
                    "karakter yang 'bukan spasi', dan find_first_not_of mengembalikan npos.",
                    "Meneruskannya ke substr melempar std::out_of_range.",
                    "",
                    "JEBAKAN: npos + 1 BERNILAI 0, DAN ITU DIAM-DIAM MASUK AKAL",
                    "",
                    "Bentuk ini dipakai untuk membuang nol di ekor bilangan:",
                    "",
                    "  std::string angka = \"3.1400\";",
                    "  angka.erase(angka.find_last_not_of('0') + 1);   // -> \"3.14\"",
                    "",
                    "Sekarang bayangkan isinya \"0000\". find_last_not_of('0') tidak menemukan",
                    "apa pun, jadi ia mengembalikan npos - dan npos itu bilangan TANPA TANDA",
                    "yang nilainya paling besar. Menambah 1 padanya berputar kembali ke 0,",
                    "sehingga erase(0) menghapus SELURUH string.",
                    "",
                    "Kebetulan hasilnya benar untuk pekerjaan ini: \"0000\" memang seharusnya",
                    "tidak menyisakan apa-apa. Tapi jangan mengandalkannya tanpa sadar. Kalau",
                    "hasilnya yang kamu mau berbeda, periksa npos-nya sendiri lebih dulu.",
                    "",
                    "MEMERIKSA SATU KARAKTER: <cctype>",
                    "",
                    "Untuk bertanya 'karakter ini angka?' atau 'huruf?', pustaka <cctype>",
                    "menyediakan sederet fungsi pendek:",
                    "",
                    "  isdigit(c)  angka 0-9          isalpha(c)  huruf",
                    "  isspace(c)  spasi/tab/newline  isupper(c)  huruf besar",
                    "  toupper(c)  jadikan huruf besar  tolower(c)  jadikan huruf kecil",
                    "",
                    "JEBAKAN: ARGUMENNYA HARUS unsigned char",
                    "",
                    "  for (char c : teks)",
                    "      if (isdigit(c)) ...                              // BERISIKO",
                    "      if (isdigit(static_cast<unsigned char>(c))) ...  // BENAR",
                    "",
                    "Fungsi-fungsi ini mewarisi C dan menerima int, bukan char. Di kebanyakan",
                    "mesin char BERTANDA, jadi huruf beraksen seperti 'é' bernilai NEGATIF -",
                    "dan nilai negatif selain EOF membuat perilakunya tidak terdefinisi.",
                    "Untuk teks ASCII biasa ia tidak akan terlihat salah, dan itulah yang",
                    "membuat bug ini bertahan lama. Cast-nya murah; pasang selalu.",
                    "",
                    "Perhatikan juga bahwa isdigit mengembalikan int, bukan bool: nilai apa",
                    "pun selain 0 berarti benar. Dipakai di dalam if ia tetap bekerja seperti",
                    "yang kamu harapkan.",
                    "Angka <-> teks: dua arah yang harus kamu hafal",
                    "",
                    "  to_string(n)  -> angka apa pun jadi string. Ini yang membuat \"NIM \" + to_string(nim)",
                    "                   bisa ditulis; tanpa itu, + antara teks dan int TIDAK ADA di C++.",
                    "  stoi(s)       -> string jadi int   (string to int)",
                    "  stod(s)       -> string jadi double",
                    "  stol(s)       -> string jadi long, untuk angka yang tidak muat di int",
                    "",
                    "Dari mana teks-yang-sebenarnya-angka itu datang? Hampir selalu dari luar program:",
                    "getline(cin, baris), satu baris berkas, atau ARGUMEN BARIS PERINTAH. Yang terakhir ini",
                    "wajib dikenali karena bentuknya khas:",
                    "",
                    "      int main(int argc, char *argv[])",
                    "",
                    "  argc = berapa kata yang diketik (nama programnya ikut dihitung), argv = daftar katanya",
                    "  sebagai TEKS. Jadi ./program 7 memberi argc == 2 dan argv[1] == \"7\" - sebuah string",
                    "  berisi satu huruf '7', bukan angka tujuh. stoi(argv[1]) yang mengubahnya.",
                    "  argv[0] SELALU nama program yang dijalankan (\"./program\"), jadi argumen yang kamu",
                    "  ketik sendiri mulai dari argv[1] - itulah sebabnya contoh mana pun membaca argv[1],",
                    "  bukan argv[0].",
                    "",
                    "Awas dua hal:",
                    "  - Periksa argc dulu. Membaca argv[1] saat orang lupa mengetik argumennya adalah crash.",
                    "  - stoi MELEMPAR exception (invalid_argument) kalau teksnya sama sekali bukan angka.",
                    "    Tapi kalau teksnya DIAWALI angka, ia diam-diam berhenti di huruf pertama: stoi(\"12abc\")",
                    "    mengembalikan 12 tanpa keluhan apa pun.",
                ],
                "code": """#include <iostream>
#include <string>
#include <stdexcept>
using namespace std;

int main(int argc, char *argv[]) {
    // Kalau dijalankan tanpa argumen, argc cuma 1 -- pakai nilai cadangan.
    string masukan = (argc > 1) ? argv[1] : "42";
    cout << "Teks masukan: " << masukan << endl;

    int angka = stoi(masukan);          // teks -> int
    cout << "Dikali dua : " << angka * 2 << endl;

    double harga = stod("15000.5");     // teks -> double
    cout << "Harga x 2  : " << harga * 2 << endl;

    int nim = 2201;
    string label = "NIM " + to_string(nim);   // angka -> teks, baru boleh di-+
    cout << label << endl;
    cout << to_string(87.5) << endl;    // 87.500000 <- to_string SELALU 6 desimal

    // Bentuk try-catch dibahas tuntas di materi Exception Handling nanti.
    try {
        int gagal = stoi("duapuluh");
        cout << gagal << endl;
    } catch (const invalid_argument &e) {
        cout << "'duapuluh' bukan angka, stoi menolak" << endl;
    }

    cout << stoi("12abc") << endl;      // 12 -- berhenti di huruf, TIDAK error

    return 0;
}""",
            },
            {
                "heading": "stringstream: merakit dan memecah teks (butuh #include <sstream>)",
                "code": """#include <iostream>
#include <sstream>     // WAJIB. Tanpa header ini ostringstream/istringstream tidak dikenal.
#include <string>
using namespace std;

int main() {
    // ostringstream = "cout yang hasilnya disimpan", bukan dicetak ke layar.
    ostringstream oss;
    oss << "NIM " << 2201 << " nilai " << 87.5;
    string ringkasan = oss.str();      // .str() mengambil teks yang sudah terakit
    cout << ringkasan << endl;         // NIM 2201 nilai 87.5

    // istringstream = "cin yang sumbernya sebuah string", bukan keyboard.
    string baris = "Andi 20 87.5";
    istringstream iss(baris);
    string nama;
    int umur;
    double nilai;
    iss >> nama >> umur >> nilai;      // dipisah spasi, persis seperti cin >>
    cout << nama << " / " << umur << " / " << nilai << endl;

    // Pemisah selain spasi: getline dengan argumen KETIGA
    string csv = "Andi,20,Bandung";
    istringstream baca(csv);
    string potongan;
    while (getline(baca, potongan, ',')) {
        cout << "[" << potongan << "]";
    }
    cout << endl;                      // [Andi][20][Bandung]

    return 0;
}""",
            },
            {
                "body": [
                    "Kenapa stringstream ada, padahal sudah ada to_string dan stoi?",
                    "  - Merakit: satu ostringstream menampung SEMUA tipe sekaligus (\"NIM \" << 2201 << 87.5)",
                    "    tanpa satu pun to_string. Ia juga memakai aturan tampilan cout, jadi 87.5 tercetak",
                    "    \"87.5\" - bukan \"87.500000\" seperti to_string. Bisa dirapikan dengan fixed dan",
                    "    setprecision dari <iomanip> yang sudah kamu kenal di materi cin & cout.",
                    "  - Memecah: istringstream mengubah satu baris jadi kolom-kolom bertipe. Baris CSV, baris",
                    "    berkas, satu baris perintah - semuanya dipecah dengan cara yang sama. Ini pola yang",
                    "    akan langsung terpakai begitu kamu membaca berkas nanti.",
                    "",
                    ".c_str() - jembatan ke dunia C",
                    "  Fungsi lama gaya C (printf, fopen, banyak library sistem) tidak mengerti std::string;",
                    "  yang mereka minta const char*. .c_str() menyediakannya:",
                    "",
                    "      printf(\"Halo %s\\n\", nama.c_str());",
                    "",
                    "  Pointer itu MEMINJAM, bukan memiliki. Ia sah selama string aslinya masih hidup dan",
                    "  belum diubah. Baris ini bug klasik yang compiler pun tidak mengeluh:",
                    "",
                    "      const char *p = (nama + \" Wijaya\").c_str();   // string sementaranya langsung mati",
                    "      cout << p;                                    // isinya sudah bukan milik siapa-siapa",
                    "",
                    "  Simpan dulu ke variabel string, baru panggil .c_str() darinya.",
                    "",
                    "Jebakan yang benar-benar menjebak:",
                    "  1. substr(a, b): b itu PANJANG, bukan posisi akhir. Beda dari substring Java dan slicing",
                    "     Python. substr(0, 7) memberi 7 huruf pertama, bukan huruf 0 sampai 6-lalu-berhenti.",
                    "  2. s[i] tidak memeriksa batas. Index kelewat = perilaku tak tentu, kadang tidak crash",
                    "     hari ini lalu crash besok. Pakai .at(i) saat index-nya datang dari input.",
                    "  3. find yang tidak ketemu BUKAN mengembalikan -1 dan bukan 0. Bandingkan dengan",
                    "     string::npos, selalu.",
                    "  4. Lupa #include <string> atau <sstream>. Kadang tetap kompilasi karena header lain",
                    "     ikut menariknya, lalu gagal di mesin orang lain. Tulis include-nya sendiri.",
                ],
            },
        ],
    },
    {
        "title": "7. Referensi (&) vs Pointer",
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
        "title": "8. Function Overloading & Default Parameter",
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
        "title": "9. OOP: Class & Object Dasar",
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
        "title": "10. Constructor & Destructor",
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
        "title": "11. Encapsulation: private, public, protected",
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
        "title": "12. Memecah Class ke Header (.h) & Sumber (.cpp)",
        "sections": [
            {
                "body": [
                    "Semua contoh C++ sampai sini menulis badan method DI DALAM kurung kurawal class.",
                    "Itu sengaja, supaya satu contoh muat di satu layar. Tapi kode C++ nyata hampir",
                    "tidak pernah begitu - dan itu artinya .cpp mana pun yang kamu buka di GitHub",
                    "dimulai dengan bentuk yang belum pernah muncul di kurikulum ini.",
                    "",
                    "Bentuk bakunya: SATU class dipecah jadi DUA berkas.",
                    "  rekening.h    -> DEKLARASI: 'class Rekening punya method setor(double)'",
                    "  rekening.cpp  -> DEFINISI:  badan method setor yang sebenarnya",
                    "",
                    "Anggap header itu daftar isi buku (siapa saja yang ada dan bentuk panggilannya),",
                    "dan .cpp itu isi babnya (bagaimana kerjanya).",
                    "",
                    "Kenapa repot-repot dipisah:",
                    "  - Yang mau MEMAKAI class cukup baca header yang pendek, tidak perlu ikut",
                    "    membaca ratusan baris implementasi.",
                    "  - Mengubah isi satu method cuma memaksa satu .cpp dikompilasi ulang, bukan",
                    "    seluruh project.",
                    "  - Header itulah 'kontrak' yang dipegang berkas lain. Selama header tidak",
                    "    berubah, isi .cpp boleh kamu tulis ulang total tanpa mengganggu siapa pun.",
                    "",
                    "Baris pembuka yang paling sering bikin bingung waktu pertama kali dibaca:",
                    "",
                    "  void Rekening::setor(double jumlah) { ... }",
                    "",
                    "Dibaca pelan-pelan dari kiri:",
                    "  void        -> method ini tidak mengembalikan apa-apa",
                    "  Rekening::  -> method MILIK class Rekening, bukan fungsi bebas yang kebetulan",
                    "                 bernama setor",
                    "  setor       -> nama methodnya",
                    "",
                    "Tanda :: itu operator yang SAMA PERSIS dengan yang ada di std::cout (materi",
                    "Variabel, Tipe Data & Namespace). Artinya 'ambil nama yang ada DI DALAM':",
                    "std::cout = cout milik namespace std, Rekening::setor = setor milik Rekening.",
                    "",
                    "Lupa menulis 'Rekening::' bukan salah ketik sepele: compiler menganggapnya",
                    "fungsi bebas, lalu mengeluh 'saldo was not declared in this scope' - karena",
                    "fungsi bebas memang tidak punya saldo. Errornya menunjuk baris saldo, padahal",
                    "yang salah ada di baris judul methodnya.",
                ],
            },
            {
                "heading": "Satu class, tiga berkas (contoh utuh)",
                "code": """/* ===== File: rekening.h ===== */
#ifndef REKENING_H
#define REKENING_H

#include <string>

class Rekening {
private:
    std::string pemilik;
    double saldo;

public:
    Rekening(std::string p, double s);        // DEKLARASI, ditutup titik koma

    std::string getPemilik() const { return pemilik; }   // pendek: biar di sini
    double getSaldo() const { return saldo; }

    void setor(double jumlah);                // badannya ada di rekening.cpp
    bool tarik(double jumlah);
};

#endif

/* ===== File: rekening.cpp ===== */
#include "rekening.h"

Rekening::Rekening(std::string p, double s) : pemilik(p), saldo(s) {}

void Rekening::setor(double jumlah) {
    if (jumlah > 0) {
        saldo += jumlah;
    }
}

bool Rekening::tarik(double jumlah) {
    if (jumlah > 0 && jumlah <= saldo) {
        saldo -= jumlah;
        return true;
    }
    return false;
}

/* ===== File: main.cpp ===== */
#include <iostream>
#include "rekening.h"

using namespace std;

int main() {
    Rekening r("Andi", 100000);

    r.setor(50000);
    cout << r.getPemilik() << " punya saldo " << r.getSaldo() << endl;
    cout << "Tarik 200000 berhasil? " << r.tarik(200000) << endl;

    return 0;
}""",
            },
            {
                "body": [
                    "Perhatikan di rekening.cpp: constructor pun ditulis 'Rekening::Rekening(...)' -",
                    "nama class dulu (siapa pemiliknya), baru nama methodnya yang kebetulan sama.",
                    "Initializer list ': pemilik(p), saldo(s)' ikut pindah ke .cpp; yang tinggal di",
                    "header cuma deklarasinya.",
                    "",
                    "Sekarang tiga hal di header itu yang belum pernah dijelaskan.",
                    "",
                    "1) Include guard - #ifndef / #define / #endif",
                    "",
                    "Satu header sering ter-include LEBIH DARI SEKALI di berkas yang sama tanpa kamu",
                    "sadari: main.cpp meng-include rekening.h dan juga bank.h, sementara bank.h",
                    "sendiri meng-include rekening.h. Isinya ditempel dua kali, dan compiler berhenti:",
                    "",
                    "  error: redefinition of 'class Rekening'",
                    "",
                    "Tiga baris penjaganya bekerja begini:",
                    "  #ifndef REKENING_H   // kalau REKENING_H belum pernah didefinisikan...",
                    "  #define REKENING_H   // ...definisikan sekarang, lalu baca terus isinya",
                    "  ...isi header...",
                    "  #endif               // penempelan KEDUA melompat langsung ke sini, kosong",
                    "",
                    "Nama guard-nya bebas asal UNIK di seluruh project; kebiasaannya NAMA_BERKAS_H",
                    "huruf besar. Dua header yang tanpa sengaja memakai nama guard sama membuat salah",
                    "satunya hilang diam-diam, dan errornya muncul jauh dari penyebabnya.",
                    "",
                    "Padanan modernnya cuma satu baris di paling atas berkas, tanpa #endif:",
                    "",
                    "  #pragma once",
                    "",
                    "Bukan bagian resmi standar C++, tapi didukung semua compiler besar (g++, clang,",
                    "MSVC). Keduanya akan kamu temui di kode nyata - pilih satu dan konsisten. Tidak",
                    "perlu memakai keduanya sekaligus di berkas yang sama.",
                    "",
                    "2) #include \"rekening.h\" vs #include <vector>",
                    "",
                    "  <kurung sudut>  -> cari di folder pustaka sistem/compiler. Untuk header standar",
                    "                     dan pustaka pihak ketiga: <iostream>, <string>, <vector>.",
                    "  \"tanda kutip\"   -> cari DULU di folder berkas ini sendiri. Untuk header",
                    "                     buatanmu: \"rekening.h\".",
                    "",
                    "Salah pilih memberi 'fatal error: rekening.h: No such file or directory' untuk",
                    "berkas yang jelas-jelas ada di sebelahnya.",
                    "",
                    "3) Jangan pernah menulis 'using namespace std;' DI DALAM header.",
                    "",
                    "Header disalin apa adanya ke SETIAP berkas yang meng-include-nya, jadi baris itu",
                    "memaksakan keputusanmu ke semua orang yang memakai class-mu, dan bentroknya baru",
                    "meledak belakangan di berkas yang bukan kamu tulis. Di header, tulis lengkap:",
                    "std::string, std::vector. 'using namespace std;' cukup di .cpp - lihat main.cpp",
                    "di contoh atas, sementara rekening.h tidak punya baris itu.",
                ],
            },
            {
                "heading": "Mana yang tetap tinggal di header",
                "body": [
                    "Aturan praktisnya sederhana:",
                    "  - Getter/setter satu baris: biarkan di dalam class. Memindahkannya ke .cpp",
                    "    cuma menambah baris tanpa memperjelas apa pun.",
                    "  - Method yang badannya lebih dari 2-3 baris, atau butuh #include tambahan:",
                    "    deklarasikan di header, definisikan di .cpp.",
                    "",
                    "Kenapa method di dalam class aman ditulis di header padahal header disalin ke",
                    "banyak berkas? Karena method yang didefinisikan di DALAM badan class otomatis",
                    "dianggap inline oleh compiler. Fungsi BEBAS tidak dapat perlakuan itu - kalau",
                    "badannya ditulis di header tanpa 'inline', dua .cpp yang meng-include header",
                    "yang sama menghasilkan dua salinan, dan linker berhenti dengan:",
                    "",
                    "  multiple definition of `persen(double, double)'",
                    "",
                    "Tambahkan 'inline' dan linker paham 'salinan ini boleh muncul di mana-mana,",
                    "pakai salah satu saja'. Ini juga alasan template selalu ditulis penuh di header",
                    "(materi Templates) - compiler perlu melihat badannya di tiap berkas pemakainya.",
                    "",
                    "Di contoh bawah, 'double saldo = 0;' menunjukkan satu hal lagi: nilai awal",
                    "atribut boleh ditulis langsung di header sejak C++11, tanpa lewat constructor.",
                ],
                "code": """// ===== bantu.h =====
#pragma once

class Rekening {
public:
    double getSaldo() const { return saldo; }   // satu baris: biarkan di sini
    void setor(double jumlah);                  // lebih panjang: pindah ke .cpp
private:
    double saldo = 0;
};

// Fungsi BEBAS (bukan method) yang ditulis lengkap di header WAJIB 'inline'.
inline double persen(double nilai, double p) {
    return nilai * p / 100.0;
}""",
            },
            {
                "body": [
                    "Mengompilasi banyak berkas. Yang disebut HANYA .cpp - header tidak pernah ikut",
                    "ditulis di perintah, karena isinya sudah masuk lewat #include:",
                    "",
                    "  g++ -std=c++17 -Wall main.cpp rekening.cpp -o app",
                    "  ./app",
                    "",
                    "Kalau satu .cpp lupa disertakan, errornya bukan dari compiler tapi dari LINKER:",
                    "",
                    "  undefined reference to `Rekening::setor(double)'",
                    "",
                    "Terjemahannya: 'aku percaya method ini ada karena header menjanjikannya, tapi",
                    "badannya tidak ketemu di berkas mana pun yang kamu berikan.' Obatnya hampir",
                    "selalu sama - tambahkan .cpp yang hilang ke perintah kompilasi. Cara cepat",
                    "membedakannya dari error biasa: error compiler selalu menyebut nomor baris,",
                    "error linker tidak - ia cuma tahu nama.",
                    "",
                    "Menulis daftar .cpp satu per satu jadi tidak terkelola begitu berkasnya belasan.",
                    "Standar industri C++ untuk itu CMake (Makefile lebih lekat ke dunia C). Isi",
                    "CMakeLists.txt paling kecil yang sudah cukup untuk project di atas:",
                    "",
                    "  cmake_minimum_required(VERSION 3.16)",
                    "  project(rekening)",
                    "  set(CMAKE_CXX_STANDARD 17)",
                    "  add_executable(app main.cpp rekening.cpp)",
                    "",
                    "Membangunnya:",
                    "  cmake -B build         # sekali saja: siapkan folder build",
                    "  cmake --build build    # ulangi tiap kali kode berubah",
                    "  ./build/app",
                    "",
                    "Terakhir, ini juga cara membaca repo C++ orang lain. Jangan mulai dari daftar",
                    "berkas - buka CMakeLists.txt dulu. Baris add_executable menyebut .cpp mana yang",
                    "jadi program dan di mana main()-nya, add_library menyebut mana yang cuma pustaka",
                    "pendukung. Setelah tahu itu, baru buka header-nya untuk melihat class apa saja",
                    "yang tersedia, lalu .cpp yang senama kalau kamu perlu tahu isinya.",
                ],
            },
        ],
    },
    {
        "title": "13. Pointer this, Anggota static & explicit",
        "sections": [
            {
                "body": [
                    "Setiap method non-static punya satu variabel tersembunyi bernama 'this'.",
                    "Isinya ALAMAT objek yang sedang mengerjakan method itu.",
                    "",
                    "  r.setor(50000);   // di dalam setor, this bernilai &r",
                    "  s.setor(50000);   // di dalam setor yang SAMA, this bernilai &s",
                    "",
                    "Kata kuncinya: this adalah POINTER - bukan objek, bukan reference.",
                    "Kalau kamu datang dari Java, di sinilah tersandungnya: 'this' di Java",
                    "adalah referensi ke objeknya, jadi ditulis this.nama. Di C++:",
                    "",
                    "  this->nama     // akses lewat pointer, -> yang sama dari materi Referensi",
                    "  (*this).nama   // sama artinya, cuma lebih panjang",
                    "  *this          // OBJEKNYA sendiri, hasil dereference pointer",
                    "  this.nama      // ERROR: this itu pointer, titik tidak berlaku untuknya",
                    "",
                    "KEGUNAAN 1 - membedakan atribut dari parameter yang namanya sama:",
                    "",
                    "  Rekening(string nama) { this->nama = nama; }",
                    "",
                    "  Di dalam constructor itu, 'nama' polos selalu berarti PARAMETER (yang",
                    "  lebih dekat), sedangkan atributnya hanya bisa dicapai lewat this->.",
                    "  Tanpa this->, baris 'nama = nama;' menyalin parameter ke dirinya",
                    "  sendiri: atribut objek tidak pernah terisi. Bahkan -Wall -Wextra pun",
                    "  DIAM - yang muncul cuma nama kosong dan angka sampah saat dijalankan.",
                    "  Inilah alasan materi-materi sebelumnya selalu memakai nama parameter",
                    "  pendek (n, u, p) atau initializer list ': nama(n)' - keduanya cara",
                    "  menghindari bentrok. Sekarang kamu punya cara ketiga, dan cara inilah",
                    "  yang paling sering kamu temui saat membaca kode orang lain.",
                    "",
                    "KEGUNAAN 2 - 'return *this;' supaya method bisa dirangkai:",
                    "",
                    "  obj.setA(1).setB(2).setC(3);",
                    "",
                    "  Tipe kembalinya WAJIB reference (Rekening&). Kalau ditulis 'Rekening'",
                    "  polos, yang dikembalikan SALINAN, jadi setB(2) mengubah salinan itu",
                    "  lalu salinannya dibuang - objek aslinya cuma kena setA(1). Kode tetap",
                    "  kompilasi tanpa satu peringatan pun; yang salah hanya hasilnya.",
                    "  Pola return *this ini akan wajib lagi nanti saat menulis operator=.",
                    "",
                    "Di method ber-const (lihat materi Encapsulation), tipe this ikut jadi",
                    "const Rekening*, sehingga percobaan mengubah atribut langsung ditolak.",
                ],
            },
            {
                "heading": "Contoh this-> dan method berantai",
                "code": """#include <iostream>
#include <string>
using namespace std;

class Rekening {
private:
    string nama;
    double saldo;

public:
    Rekening(string nama, double saldo) {
        this->nama = nama;        // kiri: ATRIBUT objek. kanan: PARAMETER
        this->saldo = saldo;
    }

    Rekening& gantiNama(string nama) {
        this->nama = nama;
        return *this;             // kembalikan OBJEKNYA, bukan pointernya
    }

    Rekening& setor(double jumlah) {
        if (jumlah > 0) saldo += jumlah;   // tidak ada bentrok nama, this-> boleh dilewat
        return *this;
    }

    void tampil() const {
        cout << nama << ": " << saldo << endl;
    }

    bool objekYangSama(const Rekening& lain) const {
        return this == &lain;     // bandingkan ALAMAT, bukan isi
    }
};

int main() {
    Rekening r("Andi", 100000);
    r.tampil();                                            // Andi: 100000

    r.gantiNama("Andi Wijaya").setor(50000).setor(25000);  // berantai
    r.tampil();                                            // Andi Wijaya: 175000

    Rekening kembar("Andi Wijaya", 175000);                // isinya sama persis
    cout << r.objekYangSama(r) << " "
         << r.objekYangSama(kembar) << endl;               // 1 0 (beda alamat)

    return 0;
}""",
            },
            {
                "body": [
                    "Kata 'static' dipakai untuk TIGA hal yang sebenarnya tidak berhubungan.",
                    "Memisahkannya lebih dulu menghemat banyak kebingungan nanti.",
                    "",
                    "1. ANGGOTA DATA static - satu nilai milik CLASS, bukan milik tiap objek.",
                    "   Seribu objek Tiket tetap berbagi SATU jumlahDibuat yang sama.",
                    "   Yang ditulis di dalam class cuma DEKLARASI; nilainya harus",
                    "   didefinisikan sekali lagi di LUAR class, di tingkat berkas:",
                    "",
                    "     class Tiket { static int jumlahDibuat; };   // deklarasi",
                    "     int Tiket::jumlahDibuat = 0;                // definisi, tanpa 'static'",
                    "",
                    "   Lupa baris kedua = kompilasi mulus, tapi linker menolak dengan",
                    "   'undefined reference to Tiket::jumlahDibuat'. Pesan itu menyesatkan:",
                    "   yang hilang bukan sebuah fungsi, melainkan tempat penyimpanannya.",
                    "",
                    "2. METHOD static - milik class, dipanggil TANPA objek apa pun:",
                    "",
                    "     Tiket::totalDibuat();     // pakai ::, bukan titik",
                    "",
                    "   Karena tidak ada objek yang memanggilnya, method static tidak punya",
                    "   this - jadi ia tidak bisa menyentuh atribut biasa sama sekali.",
                    "   Dua pemakaian tersering: fungsi utilitas/penghitung, dan FACTORY",
                    "   METHOD - fungsi yang membuatkan objek dengan aturannya sendiri.",
                    "   Untuk konstanta milik class: static constexpr int MAKS = 100;",
                    "   ('constexpr' = nilainya sudah pasti sejak waktu kompilasi).",
                    "",
                    "3. VARIABEL static di dalam fungsi biasa - dibuat sekali, nilainya",
                    "   BERTAHAN sampai panggilan berikutnya, tidak direset tiap masuk:",
                    "",
                    "     int nomorAntrean() { static int terakhir = 0; return ++terakhir; }",
                    "",
                    "   Baris 'static int terakhir = 0;' hanya dijalankan pada panggilan",
                    "   PERTAMA. Berguna, tapi hati-hati: fungsinya jadi punya ingatan, dan",
                    "   hasilnya tidak lagi cuma bergantung pada argumen yang kamu berikan.",
                    "",
                    "(Di C ada makna keempat lagi: 'static' di luar fungsi berarti nama itu",
                    "tidak terlihat dari berkas lain. Beda topik dari ketiga di atas.)",
                ],
            },
            {
                "heading": "Contoh anggota static, factory method & static lokal",
                "code": """#include <iostream>
#include <string>
using namespace std;

class Tiket {
private:
    string kode;
    static int jumlahDibuat;          // DEKLARASI: satu nilai untuk SELURUH class

public:
    static constexpr int MAKS = 100;  // konstanta milik class, bukan milik objek

    Tiket(string kode) : kode(kode) {
        jumlahDibuat++;               // setiap objek menambah penghitung yang SAMA
    }

    static int totalDibuat() {        // method static: TIDAK punya this
        // cout << kode;              // ERROR kalau dibuka: kode milik objek
        return jumlahDibuat;
    }

    static Tiket buatGratis() {       // factory: membuat objek dengan aturan sendiri
        return Tiket("GRATIS");
    }

    void tampil() const { cout << "Tiket " << kode << endl; }
};

int Tiket::jumlahDibuat = 0;          // DEFINISI wajib: di luar class, pakai ::

int nomorAntrean() {
    static int terakhir = 0;          // static LOKAL: bertahan antar panggilan
    terakhir++;
    return terakhir;
}

int main() {
    cout << "Awal  : " << Tiket::totalDibuat() << endl;   // 0, tanpa objek apa pun

    Tiket a("A-01");
    Tiket b("B-02");
    Tiket c = Tiket::buatGratis();
    c.tampil();

    cout << "Total : " << Tiket::totalDibuat() << endl;   // 3
    cout << "Maks  : " << Tiket::MAKS << endl;            // 100

    cout << nomorAntrean() << " ";    // 1
    cout << nomorAntrean() << " ";    // 2
    cout << nomorAntrean() << endl;   // 3 - TIDAK kembali ke 0

    return 0;
}""",
            },
            {
                "heading": "Contoh explicit, kurung kurawal & nilai bawaan atribut",
                "body": [
                    "Constructor satu parameter diam-diam merangkap jadi ATURAN KONVERSI.",
                    "Punya KotakLama(int) berarti compiler boleh mengubah int apa pun jadi",
                    "KotakLama di mana pun sebuah KotakLama diminta:",
                    "",
                    "  terima(7);          // 7 diubah jadi KotakLama(7) tanpa satu kata pun",
                    "  KotakLama a = 7;    // ikut lolos",
                    "",
                    "Terasa praktis, sampai suatu hari kamu salah menaruh argumen dan",
                    "compiler menutupinya dengan membuatkan objek yang tidak pernah kamu minta.",
                    "'explicit' mematikan konversi diam-diam itu. Objeknya tetap bisa dibuat,",
                    "hanya saja harus ditulis terang-terangan: Kotak q{7}; atau Kotak(7).",
                    "Aturan praktis: tandai explicit SEMUA constructor satu parameter, kecuali",
                    "kamu memang menginginkan konversi otomatisnya.",
                    "",
                    "Kurung kurawal untuk membuat objek dan mengisi variabel:",
                    "",
                    "  Kotak p{7};      // sama dengan Kotak p(7);",
                    "  int hitung{};    // 0 - kurawal kosong berarti 'isi dengan nol'",
                    "  int belum;       // TIDAK diinisialisasi - isinya sampah dari memori",
                    "",
                    "Dua alasan C++ modern lebih menyukai kurawal:",
                    "  - Ia MENOLAK narrowing. 'int x{3.7};' error; 'int x = 3.7;' diam-diam 3.",
                    "  - Ia menghindari most vexing parse: 'Kotak p();' ternyata bukan objek",
                    "    melainkan DEKLARASI FUNGSI tanpa parameter. 'Kotak p{};' aman.",
                    "",
                    "Default member initializer - nilai awal ditulis langsung di badan class",
                    "(int isi{0}; atau int kapasitas = 10;, artinya sama). Semua constructor",
                    "otomatis ikut memakainya, jadi tidak ada lagi atribut yang lupa diisi di",
                    "salah satu constructor. Aturannya kalau keduanya ada: INITIALIZER LIST",
                    "MENANG - pada 'Kotak(int n, int k) : isi(n), kapasitas(k) {}' baris",
                    "'= 10' tidak pernah dipakai. Nilai di badan class hanya berlaku untuk",
                    "anggota yang TIDAK disebut di initializer list constructor yang dipanggil.",
                ],
                "code": """#include <iostream>
using namespace std;

class KotakLama {
public:
    int isi;
    KotakLama(int n) : isi(n) {}          // TANPA explicit
};

class Kotak {
public:
    int isi{0};                            // default member initializer
    int kapasitas = 10;                    // bentuk lain, artinya sama persis

    Kotak() {}                             // isi 0, kapasitas 10
    explicit Kotak(int n) : isi(n) {}      // isi n, kapasitas TETAP 10
    Kotak(int n, int k) : isi(n), kapasitas(k) {}   // init list MENANG atas '= 10'
};

void terima(KotakLama k) { cout << "terima KotakLama isi " << k.isi << endl; }

int main() {
    terima(7);            // LOLOS: 7 diam-diam diubah jadi KotakLama(7)
    KotakLama a = 7;      // LOLOS juga, padahal 'KotakLama' tidak tertulis di kanan
    cout << "a.isi = " << a.isi << endl;

    // Kotak salah = 7;   // ERROR kalau dibuka - itulah gunanya explicit
    Kotak p;              // 0 10
    Kotak q{7};           // 7 10  - konversinya ditulis terang-terangan
    Kotak r{7, 99};       // 7 99  - initializer list menimpa nilai bawaan
    cout << p.isi << " " << p.kapasitas << endl;
    cout << q.isi << " " << q.kapasitas << endl;
    cout << r.isi << " " << r.kapasitas << endl;

    int hitung{};         // 0 - kurawal kosong berarti "isi dengan nol"
    cout << "hitung = " << hitung << endl;
    return 0;
}""",
            },
        ],
    },
    {
        "title": "14. Inheritance (Pewarisan)",
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
        "title": "15. Polymorphism & Virtual Function",
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
                    "",
                    "'final' (C++11+) adalah pasangannya, dan ia berdiri di posisi",
                    "yang PERSIS SAMA dengan override - karena itu saat pertama",
                    "terlihat ia gampang dikira salah tulis. Artinya: kunci, cukup",
                    "sampai di sini.",
                    "",
                    "  void bersuara() override final;   // METHOD ini tidak boleh",
                    "                                    // di-override lagi ke bawah",
                    "  class Persia final : public Kucing { ... };  // CLASS ini tidak",
                    "                                               // boleh diwarisi",
                    "",
                    "Kalau ada yang tetap mencoba menurunkannya, compiler menolak saat",
                    "itu juga. Dipakai saat sebuah class atau method sudah 'selesai'",
                    "dan pewarisan lebih lanjut cuma akan merusak asumsinya. Bedanya",
                    "dengan override: override boleh berdiri sendiri, sedangkan final",
                    "pada method biasanya menempel SETELAH override.",
                ]
            },
        ],
    },
    {
        "title": "16. Abstract Class & Pure Virtual Function",
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
        "title": "17. Konversi Tipe: static_cast & dynamic_cast",
        "sections": [
            {
                "body": [
                    "Bilangan bulat dibagi bilangan bulat tapi hasilnya mau desimal, .size()",
                    "dibandingkan dengan int, pointer induk yang mau dipakai sebagai anak - di",
                    "kode nyata kamu terus-menerus memindahkan nilai dari satu tipe ke tipe lain.",
                    "Perpindahan itu namanya KONVERSI TIPE (cast).",
                    "",
                    "Di C caranya cuma satu: tulis tipe tujuannya dalam kurung.",
                    "",
                    "  int x = (int) harga;   // gaya C - MASIH jalan di C++, tapi dihindari",
                    "",
                    "Kenapa dihindari padahal jalan:",
                    "  - Satu bentuk untuk beberapa pekerjaan yang bahayanya jauh berbeda.",
                    "    Compiler mencoba diam-diam: konversi wajar dulu, kalau gagal buang",
                    "    const, kalau masih gagal paksa baca ulang bit mentah - mana pun yang",
                    "    berhasil dipakai, TANPA memberitahumu yang mana yang terjadi.",
                    "  - Tidak kelihatan saat membaca. '(int)' tenggelam di tengah baris dan mata",
                    "    melewatinya begitu saja. static_cast<int> justru sengaja bertele-tele,",
                    "    supaya tiap konversi kelihatan sebagai keputusan, bukan kecelakaan.",
                    "  - Style guide besar (Google, LLVM) melarangnya, dan g++ menandainya kalau",
                    "    dikompilasi dengan -Wold-style-cast:",
                    "      warning: use of old-style cast to 'int' [-Wold-style-cast]",
                    "",
                    "C++ memecahnya jadi EMPAT kata kunci, masing-masing satu pekerjaan:",
                    "  static_cast<T>(v)       konversi wajar, dicek compiler saat kompilasi",
                    "  dynamic_cast<T>(v)      turun ke tipe anak, diperiksa saat program JALAN",
                    "  const_cast<T>(v)        membuang atau memasang const",
                    "  reinterpret_cast<T>(v)  memaksa membaca ulang bit mentah - paling bahaya",
                    "",
                    "Bentuknya selalu 'nama_cast<Tipe>(nilai)'. Kurung sudut <> di sini BUKAN",
                    "template buatanmu (itu materi tersendiri nanti) - keempatnya kata kunci",
                    "bawaan C++, dan yang ditulis di dalam <> adalah tipe TUJUAN-nya.",
                ],
            },
            {
                "heading": "Contoh static_cast: pembagian, pemotongan, dan .size()",
                "code": """#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
    int total = 7;
    int jumlah = 2;

    // Dua int dibagi = pembagian INTEGER, sisanya dibuang. Ini sering bikin
    // rata-rata jadi salah tanpa satu pun peringatan compiler.
    cout << "Salah : " << total / jumlah << endl;                      // 3

    // Cukup SATU sisi yang diubah jadi double; sisi lain ikut naik sendiri.
    cout << "Benar : " << static_cast<double>(total) / jumlah << endl;  // 3.5

    double harga = 3.99;
    cout << "Jadi int: " << static_cast<int>(harga) << endl;   // 3, BUKAN 4 - dipotong,
                                                               // bukan dibulatkan!

    char huruf = 'A';
    cout << "Kode 'A': " << static_cast<int>(huruf) << endl;   // 65 (nilai ASCII-nya)

    vector<string> nama = {"Andi", "Budi", "Cici"};

    // .size() TIDAK mengembalikan int (lihat penjelasan size_t di bawah).
    // Kalau memang mau disimpan ke int, akui penyempitannya dengan static_cast.
    int banyak = static_cast<int>(nama.size());
    cout << "Jumlah nama: " << banyak << endl;

    for (size_t i = 0; i < nama.size(); i++) {
        cout << i << ". " << nama[i] << endl;
    }

    return 0;
}""",
            },
            {
                "body": [
                    "size_t = tipe bilangan bulat TANPA TANDA (unsigned) yang dipakai C++ untuk",
                    "UKURAN. .size() milik vector/string/map dan operator sizeof mengembalikan",
                    "tipe ini. Ia tidak pernah negatif - karena panjang sesuatu memang tidak",
                    "pernah negatif.",
                    "",
                    "Itu sebabnya loop di materi vector ditulis 'for (size_t i = 0; ...)'.",
                    "Kalau ditulis 'int i', g++ -Wall langsung mengeluh:",
                    "  warning: comparison of integer expressions of different signedness:",
                    "  'int' and 'std::vector<int>::size_type' [-Wsign-compare]",
                    "Membandingkan bertanda dengan tak-bertanda memaksa compiler mengubah salah",
                    "satunya diam-diam, dan hasilnya belum tentu yang kamu kira.",
                    "",
                    "JEBAKAN yang paling sering makan korban - menelusuri mundur dari belakang:",
                    "",
                    "  vector<int> kosong;",
                    "  for (size_t i = kosong.size() - 1; i >= 0; i--) {   // RUSAK",
                    "      cout << kosong[i];",
                    "  }",
                    "",
                    "kosong.size() bernilai 0. Nol dikurangi satu pada tipe unsigned TIDAK jadi",
                    "-1; ia MEMBUNGKUS ke nilai terbesar: 18446744073709551615. Dan 'i >= 0'",
                    "selalu benar, karena unsigned memang tak bisa kurang dari nol - g++ -Wextra",
                    "bahkan mengatakannya: 'comparison of unsigned expression in >= 0 is always",
                    "true'. Programnya membaca jauh di luar vector: biasanya crash, kadang malah",
                    "tampak jalan sebentar sambil mencetak angka sampah.",
                    "",
                    "Dua jalan keluarnya:",
                    "  - Pakai indeks bertanda, dan akui konversinya:",
                    "      for (int i = static_cast<int>(v.size()) - 1; i >= 0; i--)",
                    "  - Atau jangan pakai indeks sama sekali: range-based for cukup untuk",
                    "    sebagian besar kasus, dan tidak punya cara untuk salah hitung.",
                ],
            },
            {
                "heading": "Contoh dynamic_cast: turun dari pointer induk ke tipe anak",
                "code": """#include <iostream>
#include <typeinfo>       // untuk std::bad_cast
using namespace std;

class Hewan {
public:
    virtual void bersuara() { cout << "..." << endl; }
    virtual ~Hewan() {}    // sudah cukup membuat Hewan 'polymorphic'
};

class Kucing : public Hewan {
public:
    void bersuara() override { cout << "Meong!" << endl; }
    void garukSofa() { cout << "Kucing menggaruk sofa." << endl; }   // HANYA milik Kucing
};

class Anjing : public Hewan {
public:
    void bersuara() override { cout << "Guk!" << endl; }
};

void cobaGaruk(Hewan *h) {
    // Turun dari Hewan* ke Kucing*. Kalau objeknya memang Kucing -> pointer valid.
    // Kalau bukan -> nullptr. TIDAK ada error compile, TIDAK ada exception.
    Kucing *k = dynamic_cast<Kucing*>(h);

    if (k != nullptr) {            // pemeriksaan ini WAJIB, bukan opsional
        k->garukSofa();
    } else {
        cout << "Bukan Kucing - garukSofa() tidak ada di sini." << endl;
    }
}

int main() {
    Hewan *a = new Kucing();
    Hewan *b = new Anjing();

    a->bersuara();                 // Meong!
    b->bersuara();                 // Guk!

    cobaGaruk(a);                  // Kucing menggaruk sofa.
    cobaGaruk(b);                  // Bukan Kucing - garukSofa() tidak ada di sini.

    // Versi REFERENSI: tidak punya nullptr untuk dikembalikan, jadi ia MELEMPAR.
    try {
        Kucing &k = dynamic_cast<Kucing&>(*b);   // *b sebenarnya Anjing -> gagal
        k.garukSofa();                            // tidak pernah sampai sini
    } catch (const bad_cast &e) {
        cout << "Tertangkap bad_cast: " << e.what() << endl;
    }

    delete a;
    delete b;
    return 0;
}""",
            },
            {
                "body": [
                    "Alurnya: variabelnya bertipe Hewan*, tapi objek yang ditunjuk bisa Kucing",
                    "bisa Anjing (lihat materi Polymorphism & Virtual Function). NAIK ke tipe",
                    "induk selalu aman dan otomatis; TURUN kembali ke tipe anak butuh",
                    "dynamic_cast, karena benar-tidaknya baru ketahuan saat program berjalan.",
                    "",
                    "Empat hal yang wajib diingat:",
                    "  - Hasil cast POINTER wajib diperiksa terhadap nullptr. Cast yang gagal",
                    "    tidak melempar apa pun dan tidak bikin compiler marah - ia mengembalikan",
                    "    nullptr, dan kalau langsung dipanggil methodnya, program crash.",
                    "  - Versi REFERENSI berbeda perilakunya: dynamic_cast<Kucing&>(*h) melempar",
                    "    std::bad_cast dari <typeinfo>, jadi bungkus dengan try-catch (lihat",
                    "    materi Exception Handling). Pilih versi pointer kalau gagal itu wajar,",
                    "    versi referensi kalau gagal berarti ada bug.",
                    "  - Class induknya WAJIB polymorphic: minimal punya SATU virtual function,",
                    "    dan destructor virtual sudah menghitung. Kalau tidak, ini error KOMPILASI:",
                    "      error: cannot 'dynamic_cast' ... (source type is not polymorphic)",
                    "  - static_cast juga bisa turun ke anak, tapi ia TIDAK memeriksa apa pun.",
                    "    Kalau tebakanmu meleset tidak ada tanda sama sekali sampai program",
                    "    berperilaku aneh atau crash di tempat yang tak berhubungan.",
                    "",
                    "Nasihat yang jarang ada di dokumentasi: kalau kamu sering butuh dynamic_cast,",
                    "biasanya bukan cast-nya yang salah - desainnya yang kurang virtual function.",
                    "Rantai 'kalau dia Kucing lakukan A, kalau Anjing lakukan B' adalah tanda",
                    "perilaku itu seharusnya menjadi satu virtual function di Hewan yang di-override",
                    "tiap turunan. dynamic_cast baru pas kalau methodnya memang MILIK anak saja dan",
                    "tidak masuk akal ditaruh di induk.",
                    "",
                    "Dua sisanya jarang dipakai, tapi kenali bentuknya supaya tidak bingung kalau",
                    "terlihat di kode orang:",
                    "  const_cast<T>(v)        membuang const, umumnya cuma untuk memanggil fungsi",
                    "                          library lama yang lupa menandai parameternya const.",
                    "                          Menulis ke objek yang aslinya memang const =",
                    "                          undefined behavior, apa pun bisa terjadi.",
                    "  reinterpret_cast<T>(v)  membaca ulang deretan bit sebagai tipe lain; dipakai",
                    "                          di kode dekat perangkat keras, driver, atau protokol",
                    "                          jaringan. Kalau kamu merasa memerlukannya, hampir",
                    "                          selalu ada cara lain yang lebih aman.",
                ],
            },
        ],
    },
    {
        "title": "18. Operator Overloading",
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
                "heading": "Apa itu 'friend' - dan kenapa cout bisa dirangkai",
                "body": [
                    "Baris 'friend ostream& operator<<(...)' di atas memuat TIGA hal",
                    "yang belum pernah dijelaskan. Dibongkar satu per satu:",
                    "",
                    "1. friend = IZIN MASUK",
                    "",
                    "   friend memberi satu fungsi atau satu class LAIN hak mengakses",
                    "   bagian private dan protected. Ini satu-satunya lubang RESMI",
                    "   pada encapsulation yang kamu pelajari di materi Encapsulation -",
                    "   dan lubang itu dibuka oleh class-nya sendiri, dari dalam.",
                    "",
                    "     friend ostream& operator<<(ostream&, const Titik&);  // 1 fungsi",
                    "     friend class Auditor;                          // SELURUH class",
                    "",
                    "   Dua hal yang bikin orang salah paham:",
                    "     - Izinnya DIBERIKAN, bukan diambil. Kamu tidak bisa menyatakan",
                    "       diri sebagai friend milik class orang lain.",
                    "     - Fungsi friend BUKAN anggota class. Ia ditulis tanpa awalan",
                    "       'Titik::' dan tidak punya pointer this - itu sebabnya objek",
                    "       Titik-nya harus dioper sebagai parameter.",
                    "",
                    "   Di kode nyata friend paling sering muncul untuk operator<<, dan",
                    "   untuk pola friend-untuk-testing: 'friend class UjiRekening;'",
                    "   supaya kelas tes boleh memeriksa isi private tanpa memaksa",
                    "   seluruh atribut jadi public cuma demi bisa dites.",
                    "",
                    "2. ostream ITU NAMA CLASS",
                    "",
                    "   ostream adalah CLASS dari objek cout - kependekan dari 'output",
                    "   stream'. Pasangannya istream, class dari cin. Jadi parameter",
                    "   'ostream &os' berarti 'aliran keluaran mana pun': cout, cerr,",
                    "   atau ofstream yang menulis ke berkas. Satu operator<< karena",
                    "   itu cukup untuk semua tujuan sekaligus.",
                    "",
                    "3. 'ostream&' DAN 'return os;' ITU REFERENCE",
                    "",
                    "   Materi Referensi (&) vs Pointer memakai & untuk PARAMETER. Di",
                    "   sini & dipakai pada KEMBALIAN: fungsinya mengembalikan stream",
                    "   ITU SENDIRI, bukan salinannya.",
                    "",
                    "   Justru itulah yang membuat perangkaian mungkin. Compiler",
                    "   membaca cout << a << b sebagai:",
                    "",
                    "     (cout << a) << b;",
                    "",
                    "   '(cout << a)' menyerahkan cout kembali, sehingga '<< b' punya",
                    "   sesuatu di sebelah kirinya untuk dikerjakan. Kalau kembaliannya",
                    "   void - atau ostream tanpa & - rantainya putus di operator kedua",
                    "   dan compiler menolak dengan pesan yang panjang dan tidak jelas.",
                ],
            },
            {
                "heading": "friend function & friend class dalam satu contoh",
                "code": """#include <iostream>
#include <string>
using namespace std;

class Rekening {
private:
    string pemilik;
    long saldo;   // rupiah, dibulatkan

public:
    Rekening(string p, long s) : pemilik(p), saldo(s) {}

    // friend FUNCTION: fungsi bebas ini boleh menyentuh 'pemilik' dan 'saldo'
    friend ostream& operator<<(ostream &os, const Rekening &r);

    // friend CLASS: SELURUH method Auditor boleh menyentuh bagian private
    friend class Auditor;
};

// Perhatikan: TIDAK ada 'Rekening::' di sini. Ini fungsi bebas, bukan method.
ostream& operator<<(ostream &os, const Rekening &r) {
    os << r.pemilik << " (Rp" << r.saldo << ")";
    return os;              // kembalikan os-nya sendiri -> itulah kunci perangkaian
}

class Auditor {
public:
    bool mencurigakan(const Rekening &r) {
        return r.saldo > 1000000;   // membaca private milik class lain: sah, karena friend
    }
};

int main() {
    Rekening a("Andi", 500000), b("Budi", 2500000);

    cout << a << " | " << b << endl;   // dirangkai: bisa karena os DIKEMBALIKAN

    Auditor kantor;
    cout << kantor.mencurigakan(a) << " " << kantor.mencurigakan(b) << endl;  // 0 1
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
        "title": "19. Copy Constructor, operator= & Aturan Tiga",
        "sections": [
            {
                "body": [
                    "Setiap class yang kamu tulis kedatangan dua anggota gratis dari compiler,",
                    "DIAM-DIAM, selama kamu tidak menuliskannya sendiri:",
                    "",
                    "  Buffer(const Buffer &lain);              // copy constructor",
                    "  Buffer& operator=(const Buffer &lain);   // copy assignment",
                    "",
                    "Keduanya tidak tertulis di kodemu, tidak pernah kamu sebut, dan tetap ada.",
                    "Isi buatan compiler selalu sama: salin SETIAP atribut satu per satu,",
                    "apa adanya.",
                    "",
                    "Untuk atribut int, string, atau vector itu sudah BENAR - string dan vector",
                    "tahu cara menyalin dirinya sendiri. Yang berbahaya cuma satu jenis atribut:",
                    "POINTER MENTAH. Menyalin pointer apa adanya berarti menyalin ALAMATNYA,",
                    "bukan isinya - dan sekarang ada DUA objek yang memegang alamat yang SAMA.",
                    "",
                    "Bedanya kedua anggota itu, dan ini yang paling sering tertukar:",
                    "  Buffer b = a;    objek b BELUM ada, baru lahir -> COPY CONSTRUCTOR",
                    "  b = a;           objek b SUDAH ada, ditimpa    -> operator=",
                    "",
                    "Penyalinan juga terjadi di tempat yang sama sekali tidak terlihat seperti",
                    "penyalinan - inilah kenapa bugnya sering muncul dari arah yang tak terduga:",
                    "  - mengoper objek ke fungsi by value:  void cetak(Buffer b)",
                    "  - mengembalikan objek dari sebuah fungsi",
                    "  - v.push_back(objek) ke dalam vector",
                ],
            },
            {
                "heading": "Program yang SENGAJA mati - jalankan dan lihat sendiri",
                "body": [
                    "Class di bawah ini sudah benar menurut materi Constructor & Destructor:",
                    "resource diambil dengan new di constructor, dilepas dengan delete[] di",
                    "destructor. Satu baris penyalinan yang tampak biasa membuatnya ambruk.",
                    "",
                    "(Catatan kecil: 'new int[n]' berpasangan dengan 'delete[]' yang pakai kurung",
                    "siku, bukan 'delete' polos. Salah pasangan juga merusak, walau bukan itu",
                    "yang sedang kita bahas.)",
                ],
                "code": """#include <iostream>
using namespace std;

class Buffer {
public:
    int *data;      // POINTER MENTAH - ini sumber masalahnya
    int jumlah;

    Buffer(int n) {
        jumlah = n;
        data = new int[n];              // resource DIAMBIL di sini
        for (int i = 0; i < n; i++) {
            data[i] = 0;
        }
        cout << "Buffer dibuat" << endl;
    }

    ~Buffer() {
        cout << "Buffer dihapus (delete[] dipanggil)" << endl;
        delete[] data;                  // resource DILEPAS di sini
    }
};

int main() {
    Buffer a(3);
    Buffer b = a;        // copy constructor BAWAAN: b.data = a.data, alamatnya saja

    b.data[0] = 99;      // mengubah lewat b ...
    cout << "a.data[0] = " << a.data[0] << endl;   // ... a IKUT berubah jadi 99

    cout << "Sampai sini masih aman." << endl;
    return 0;
}   // b dihancurkan -> delete[] atas alamat X
    // a dihancurkan -> delete[] atas alamat X LAGI -> double free -> program mati""",
            },
            {
                "body": [
                    "Program MATI di tengah jalan, dengan pesan semacam ini:",
                    "  free(): double free detected in tcache 2",
                    "",
                    "Di aplikasi ini pesannya diterjemahkan jadi \"Program membatalkan dirinya",
                    "sendiri (abort)\"; di terminal biasa muncul \"Aborted (core dumped)\". Teks",
                    "persisnya beda-beda per mesin - yang penting: programnya BERHENTI PAKSA,",
                    "bukan selesai.",
                    "",
                    "Dua hal salah sekaligus, dan keduanya berasal dari satu sebab yang sama.",
                    "",
                    "SHALLOW COPY (buatan compiler) - dua objek, SATU memori:",
                    "",
                    "  a.data ---+",
                    "            +---> [ 99 ][ 0 ][ 0 ]     <- cuma ada SATU, dipakai berdua",
                    "  b.data ---+",
                    "",
                    "  1. b.data[0] = 99 ikut mengubah a, karena memang barang yang sama.",
                    "  2. destructor jalan DUA KALI atas alamat yang sama -> double free.",
                    "",
                    "DEEP COPY (yang harus kita tulis sendiri) - dua objek, DUA memori:",
                    "",
                    "  a.data ------> [ 10 ][ 0 ][ 0 ]",
                    "  b.data ------> [ 99 ][ 0 ][ 0 ]      <- salinan MILIK SENDIRI",
                    "",
                    "  Masing-masing punya memorinya sendiri, jadi masing-masing boleh",
                    "  menghapus miliknya sendiri satu kali. Tidak ada yang bentrok.",
                    "",
                    "JEBAKAN yang membuat bug ini terkenal susah: double free TIDAK selalu",
                    "langsung mematikan program. Kadang ia cuma merusak pembukuan heap, dan",
                    "yang ambruk justru baris lain jauh kemudian - baris yang tidak bersalah",
                    "sama sekali. Tempat kejadian bukan tempat penyebab.",
                    "",
                    "Selain itu, satu delete[] tadi juga sudah membuat pointer di objek yang",
                    "lain menunjuk memori yang sudah dikembalikan (dangling pointer). Membaca",
                    "a.data[0] setelah b dihancurkan sudah salah, walaupun kadang 'kelihatan",
                    "jalan' - dan yang 'kadang jalan' justru lebih berbahaya daripada yang",
                    "selalu crash.",
                ],
            },
            {
                "heading": "Versi benar: tiga anggota yang harus datang bersama",
                "body": [
                    "Tiga tanda tangan ini wajib kamu KENALI saat membaca kode orang lain:",
                    "",
                    "  Buffer(const Buffer &lain);              // copy constructor",
                    "  Buffer& operator=(const Buffer &lain);   // copy assignment",
                    "  ~Buffer();                               // destructor",
                    "",
                    "Kenapa parameternya 'const Buffer &lain', bukan 'Buffer lain':",
                    "  - kalau by value, mengoper argumennya sendiri sudah butuh penyalinan,",
                    "    dan penyalinan itu memanggil copy constructor lagi - tak berujung.",
                    "    Compiler menolaknya: \"invalid constructor; you probably meant",
                    "    Buffer (const Buffer&)\".",
                    "  - const supaya sumber yang disalin dijamin tidak ikut berubah, dan",
                    "    supaya objek const pun tetap bisa disalin.",
                    "",
                    "Kenapa operator= mengembalikan 'Buffer&' lalu ditutup 'return *this;':",
                    "  - supaya rangkaian 'x = y = z' bekerja seperti pada tipe bawaan,",
                    "  - referensi, bukan salinan, supaya hasilnya tidak menyalin sekali lagi.",
                    "  - '*this' sudah dibahas di materi Pointer this: objek yang sedang",
                    "    mengerjakan method itu sendiri.",
                    "",
                    "Kenapa ada penjaga 'if (this == &lain) return *this;':",
                    "  operator= MENGHAPUS milik sendiri dulu, baru menyalin dari sumber.",
                    "  Pada 'a = a;' tanpa penjaga, ia menghapus data a lalu menyalin dari",
                    "  a yang barusan dihapus - isinya jadi sampah. Terdengar konyol, tapi",
                    "  bentuk nyatanya bukan 'a = a' melainkan 'v[i] = v[j];' atau",
                    "  'objek = *penunjuk;' yang kebetulan menunjuk objek yang sama.",
                ],
                "code": """#include <iostream>
using namespace std;

class Buffer {
private:
    int *data;
    int jumlah;

public:
    Buffer(int n) : data(new int[n]), jumlah(n) {
        for (int i = 0; i < n; i++) {
            data[i] = 0;
        }
    }

    // 1. COPY CONSTRUCTOR - dipakai saat objek BARU lahir dari objek lain
    Buffer(const Buffer &lain) : data(new int[lain.jumlah]), jumlah(lain.jumlah) {
        for (int i = 0; i < jumlah; i++) {
            data[i] = lain.data[i];     // ISINYA yang disalin, bukan alamatnya
        }
        cout << "copy constructor: memori BARU dialokasikan" << endl;
    }

    // 2. COPY ASSIGNMENT - dipakai saat objek yang SUDAH ADA ditimpa
    Buffer& operator=(const Buffer &lain) {
        cout << "operator=: objek lama ditimpa" << endl;
        if (this == &lain) {
            return *this;               // penjaga self-assignment
        }
        delete[] data;                  // buang milik sendiri dulu, kalau tidak: bocor
        jumlah = lain.jumlah;
        data = new int[jumlah];
        for (int i = 0; i < jumlah; i++) {
            data[i] = lain.data[i];
        }
        return *this;                   // supaya "x = y = z" bisa dirangkai
    }

    // 3. DESTRUCTOR
    ~Buffer() {
        delete[] data;
    }

    void isi(int posisi, int nilai) { data[posisi] = nilai; }
    int lihat(int posisi) const { return data[posisi]; }
};

int main() {
    Buffer a(3);
    a.isi(0, 10);

    Buffer b = a;                       // -> copy constructor
    b.isi(0, 99);
    cout << "a = " << a.lihat(0) << endl;    // 10, TIDAK ikut berubah
    cout << "b = " << b.lihat(0) << endl;    // 99

    Buffer c(3);
    c = a;                              // -> operator=
    cout << "c = " << c.lihat(0) << endl;    // 10

    a = a;                              // aman berkat penjaga self-assignment
    cout << "a = " << a.lihat(0) << endl;    // 10, bukan sampah

    return 0;
}""",
            },
            {
                "body": [
                    "ATURAN TIGA (Rule of Three) - hafalkan yang ini:",
                    "",
                    "  Kalau sebuah class butuh DESTRUCTOR buatan sendiri, ia hampir pasti",
                    "  juga butuh COPY CONSTRUCTOR dan operator= buatan sendiri.",
                    "",
                    "Alasannya persis yang barusan kamu lihat: destructor manual ditulis karena",
                    "class itu MEMILIKI sesuatu - memori, berkas, koneksi, lock. Sesuatu yang",
                    "dimiliki tidak boleh ikut tersalin mentah-mentah ke objek kedua. Menulis",
                    "satu dari tiga tanpa dua sisanya adalah bom waktu, dan compiler tidak akan",
                    "memperingatkanmu sama sekali.",
                    "",
                    "Kalau class-mu memang TIDAK BOLEH disalin, katakan begitu secara eksplisit:",
                    "",
                    "  class Berkas {",
                    "  public:",
                    "      Berkas(const Berkas &) = delete;             // dilarang disalin",
                    "      Berkas& operator=(const Berkas &) = delete;  // dilarang ditimpa-salin",
                    "  };",
                    "",
                    "  Berkas g = f;   // error: use of deleted function 'Berkas::Berkas(...)'",
                    "",
                    "'= delete' TIDAK ADA HUBUNGANNYA dengan operator delete yang membebaskan",
                    "memori. Kata kuncinya kebetulan dipakai ulang; artinya di sini cuma",
                    "'anggota ini tidak ada, jangan coba dipanggil'. Lawannya '= default':",
                    "'buatkan versi bawaanmu, saya cuma mau menyebutnya terang-terangan'.",
                    "",
                    "  Titik(const Titik &) = default;   // versi bawaan compiler, sengaja diminta",
                    "",
                    "INILAH mekanisme di balik kalimat 'unique_ptr TIDAK BISA disalin' di materi",
                    "Smart Pointer: copy constructor-nya memang ditandai = delete di dalam header",
                    "standarnya. Pesan errornya pun sebentuk: 'use of deleted function ...",
                    "unique_ptr(const unique_ptr&)'. Baris '= delete' semacam itu juga berdiri di",
                    "atas hampir setiap class serius yang memegang resource - mutex, thread,",
                    "ifstream - dan sekarang kamu tahu artinya saat membacanya.",
                    "",
                    "Jalan keluar yang paling sering benar: cara TERAMAN lolos dari Aturan Tiga",
                    "adalah tidak memiliki pointer mentah sama sekali. Pakai vector, string, dan",
                    "smart pointer sebagai atribut - ketiganya sudah tahu cara menyalin dan",
                    "menghapus dirinya sendiri, jadi versi bawaan compiler kembali BENAR dan kamu",
                    "tidak perlu menulis satu pun dari tiga anggota itu.",
                    "",
                    "Di C++11 ke atas Aturan Tiga berkembang jadi ATURAN LIMA: dua tambahannya",
                    "adalah move constructor dan move assignment, yang menyusul di materi",
                    "RAII & Move Semantics.",
                ],
            },
        ],
    },
    {
        "title": "20. Templates (Generic Programming)",
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
            {
                "heading": "Tiga hal yang langsung menyambutmu di pustaka template",
                "body": [
                    "1. 'class' dan 'typename' adalah EJAAN yang sama",
                    "",
                    "   template <class T>      // artinya SAMA PERSIS dengan",
                    "   template <typename T>   // yang ini",
                    "",
                    "   'class' di posisi itu TIDAK berarti T harus berupa class -",
                    "   Kotak<int> tetap sah. Kata itu cuma sisa sejarah: typename",
                    "   baru ditambahkan belakangan. Pustaka lama memakai 'class',",
                    "   kode baru cenderung 'typename', dan kamu akan melihat",
                    "   keduanya berdampingan di berkas yang sama. Jangan dicari",
                    "   bedanya - memang tidak ada.",
                    "",
                    "2. Template WAJIB tinggal di HEADER",
                    "",
                    "   Materi Memecah Class ke Header mengajarkan pola baku:",
                    "   deklarasi di .h, isinya di .cpp. Untuk template pola itu",
                    "   TIDAK BERLAKU. Compiler baru membuat versi Kotak<int> pada",
                    "   saat ia melihat 'Kotak<int>' dipakai - dan untuk itu ia",
                    "   butuh SELURUH ISI template-nya di detik itu juga, bukan",
                    "   cuma deklarasinya.",
                    "",
                    "   Kalau isinya kamu pindahkan ke kotak.cpp, kompilasi lolos",
                    "   tapi linker mengeluh soal sesuatu yang tidak pernah dibuat:",
                    "",
                    "     undefined reference to `Kotak<int>::simpan(int)'",
                    "",
                    "   Pesan itu menyesatkan - kodenya jelas-jelas ada di kotak.cpp.",
                    "   Yang benar: taruh definisi template UTUH di header, method",
                    "   dan semuanya. Inilah alasan seluruh STL dan hampir semua",
                    "   pustaka template berupa header saja, tanpa satu pun .cpp",
                    "   untuk dikompilasi - kamu cukup #include, tidak ada yang",
                    "   perlu dibangun.",
                    "",
                    "3. Spesialisasi: satu tipe yang minta diperlakukan beda",
                    "",
                    "   Kadang versi umum template-mu benar untuk semua tipe KECUALI",
                    "   satu. Untuk itu ada spesialisasi - versi khusus yang dipilih",
                    "   compiler hanya kalau tipenya persis yang disebut:",
                    "",
                    "     template <> class Kotak<bool> { ... };",
                    "",
                    "   'template <>' dengan kurung sudut KOSONG artinya 'tidak ada",
                    "   lagi tipe yang bebas di sini, semuanya sudah ditentukan'.",
                    "   Contoh nyatanya ada di STL: vector<bool> adalah spesialisasi",
                    "   yang menyimpan tiap elemen sebagai satu bit, dan itulah",
                    "   sebabnya ia berperilaku sedikit aneh dibanding vector lain.",
                ],
            },
            {
                "heading": "Spesialisasi template untuk satu tipe tertentu",
                "code": """#include <iostream>
#include <string>
using namespace std;

// 'class' di sini artinya SAMA PERSIS dengan 'typename'
template <class T>
class Kotak {
private:
    T isi;
public:
    void simpan(T nilai) { isi = nilai; }
    void tampilkan() { cout << "Isi kotak: " << isi << endl; }
};

// SPESIALISASI: versi khusus yang HANYA dipakai kalau T-nya bool
template <>
class Kotak<bool> {
private:
    bool isi = false;
public:
    void simpan(bool nilai) { isi = nilai; }
    void tampilkan() { cout << "Isi kotak: " << (isi ? "benar" : "salah") << endl; }
};

int main() {
    Kotak<int> a;
    a.simpan(100);
    a.tampilkan();          // Isi kotak: 100

    Kotak<string> b;
    b.simpan("Andi");
    b.tampilkan();          // Isi kotak: Andi

    Kotak<bool> c;
    c.simpan(true);
    c.tampilkan();          // Isi kotak: benar  <- versi spesialisasi yang dipakai
    return 0;
}"""
            },
        ],
    },
    {
        "title": "21. STL: Vector & Array Container",
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
            {
                "heading": "emplace_back, reserve & si tipe index size_t",
                "body": [
                    "emplace_back - saudara push_back yang lebih hemat",
                    "",
                    "  push_back(x) menerima OBJEK yang sudah jadi, lalu menaruh",
                    "  salinannya ke dalam vector. Kalau elemennya sebuah class,",
                    "  kamu jadi harus merakit objeknya lebih dulu:",
                    "",
                    "    daftar.push_back(Mahasiswa(\"Andi\", 20));",
                    "",
                    "  emplace_back menerima ARGUMEN CONSTRUCTOR-nya apa adanya",
                    "  lalu membangun objeknya LANGSUNG di dalam vector - tidak",
                    "  ada objek sementara, tidak ada salinan yang dibuang:",
                    "",
                    "    daftar.emplace_back(\"Andi\", 20);",
                    "",
                    "  Di kode C++ modern emplace_back sama seringnya dengan",
                    "  push_back, dan sering justru menggantikannya. Untuk tipe",
                    "  sederhana seperti int keduanya sama saja - bedanya baru",
                    "  terasa saat elemennya objek. Container lain punya pasangan",
                    "  serupa: emplace, emplace_front, emplace_back.",
                    "",
                    "reserve() - beri tahu ukurannya di depan",
                    "",
                    "  Vector menyimpan isinya dalam SATU blok memori berurutan.",
                    "  Begitu blok itu penuh, ia mencari blok baru yang lebih",
                    "  besar lalu memindahkan seluruh isinya ke sana. Itu terjadi",
                    "  diam-diam, berkali-kali, sepanjang loop push_back panjang.",
                    "",
                    "    size()     -> berapa elemen yang BENAR-BENAR ada",
                    "    capacity() -> berapa yang MUAT sebelum pindah blok",
                    "    reserve(n) -> sediakan tempat untuk n sekarang juga",
                    "",
                    "  Kalau kamu sudah tahu akan memasukkan 1000 elemen, satu",
                    "  baris v.reserve(1000) di depan menghapus semua pemindahan",
                    "  itu. reserve TIDAK menambah elemen: setelahnya size() masih",
                    "  0, cuma capacity()-nya yang jadi 1000.",
                    "",
                    "Contoh di bawah sengaja mencetak setiap penyalinan supaya",
                    "bedanya kelihatan: push_back menjalankan constructor LALU copy",
                    "constructor, emplace_back cuma constructor. Biasanya salinan",
                    "itu tidak mencetak apa-apa - jadi ia mahal tanpa terlihat.",
                    "",
                    "Kenapa loop indeks di contoh PERTAMA materi ini ditulis",
                    "'for (size_t i = 0; ...)' dan bukan 'int i'? Karena size_t",
                    "itulah tipe yang dikembalikan size().",
                    "Alasan lengkapnya - beserta bug perulangan-mundur yang terkenal -",
                    "ada di materi Konversi Tipe: static_cast & dynamic_cast.",
                ],
            },
            {
                "heading": "emplace_back & reserve saat dijalankan",
                "code": """#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Mahasiswa {
public:
    string nama;
    int umur;
    Mahasiswa(string n, int u) : nama(n), umur(u) {
        cout << "  constructor jalan untuk " << nama << endl;
    }
    // Sengaja ditulis supaya SALINANNYA kelihatan. Tanpa baris-baris ini
    // penyalinannya tetap terjadi, cuma tidak mencetak apa pun.
    Mahasiswa(const Mahasiswa &lain) : nama(lain.nama), umur(lain.umur) {
        cout << "  SALINAN dibuat untuk " << nama << endl;
    }
};

int main() {
    vector<Mahasiswa> daftar;
    daftar.reserve(3);        // siapkan tempat 3 di depan: isi tidak perlu pindah-pindah

    cout << "push_back:" << endl;
    daftar.push_back(Mahasiswa("Andi", 20));   // objek DIBUAT dulu, BARU disalin masuk

    cout << "emplace_back:" << endl;
    daftar.emplace_back("Budi", 21);           // dibangun LANGSUNG di dalam vector

    cout << "size=" << daftar.size()
         << " capacity=" << daftar.capacity() << endl;   // size=2 capacity=3
    for (const auto &m : daftar) {
        cout << m.nama << " (" << m.umur << ")" << endl;
    }
    return 0;
}"""
            },
        ],
    },
    {
        "title": "22. STL: Map, Set & Pair",
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
            {
                "heading": "Mengisi & membaca map: insert, emplace, at",
                "body": [
                    "Contoh di atas memakai m[kunci] untuk segalanya. Itu cara yang",
                    "benar untuk MENULIS, tapi bukan satu-satunya cara - dan untuk",
                    "MEMBACA ia justru punya jebakan yang dibongkar tuntas di materi",
                    "Iterator. Tiga saudaranya yang perlu kamu kenal sekarang:",
                    "",
                    "  m.insert({kunci, nilai})",
                    "    Menambah. Kalau kuncinya SUDAH ADA, ia TIDAK menimpa dan",
                    "    tidak mengeluh - cuma diam. Kembaliannya sebuah pair:",
                    "    .first iterator ke entri yang bersangkutan, .second bool",
                    "    'benar-benar baru ditambah?'. Periksa .second kalau kamu",
                    "    perlu tahu bedanya.",
                    "",
                    "  m.emplace(kunci, nilai)",
                    "    Sama, tanpa merakit pair-nya lebih dulu - persis seperti",
                    "    emplace_back pada vector di materi sebelumnya.",
                    "",
                    "  m.at(kunci)",
                    "    MEMBACA saja. Kalau kuncinya tidak ada ia MELEMPAR",
                    "    out_of_range: berisik, dan itu memang maunya. Bandingkan",
                    "    dengan m[kunci] yang malah diam-diam membuat entri baru.",
                    "    at() juga satu-satunya dari keduanya yang boleh dipakai",
                    "    pada map yang const.",
                    "",
                    "Aturan praktisnya: [] untuk menulis, at() atau find() untuk",
                    "membaca, count() untuk sekadar memeriksa ada atau tidak.",
                    "",
                    "Menelusuri map dengan structured bindings",
                    "",
                    "Loop di atas menamai tiap entri 'pasangan' lalu memakai .first",
                    "dan .second - dua nama yang tidak memberi tahu apa-apa tentang",
                    "isinya. Sejak C++17 kamu boleh membongkar pair-nya langsung di",
                    "kepala loop, sekalian menamai kedua bagiannya:",
                    "",
                    "  for (const auto &[nama, angka] : nilai) {",
                    "      cout << nama << \" -> \" << angka << endl;",
                    "  }",
                    "",
                    "Inilah bentuk yang paling sering terlihat di kode C++ modern.",
                    "Kurung sikunya BUKAN array - itu structured bindings, fitur yang",
                    "sama dengan 'auto [nama, umur] = pasangan;' di materi Lambda",
                    "Expression & Fitur Modern C++. Buang '&' kalau mau salinan, dan",
                    "buang 'const' kalau mau menyunting nilainya (kuncinya tetap",
                    "tidak boleh diubah - mengubahnya akan merusak urutan map).",
                ],
            },
            {
                "heading": "insert, emplace, at & structured bindings pada map",
                "code": """#include <iostream>
#include <map>
#include <stdexcept>
#include <string>
using namespace std;

int main() {
    map<string, int> nilai;

    nilai["Andi"] = 85;              // [] untuk MENULIS -- ini pemakaian yang benar
    nilai.insert({"Budi", 90});      // insert: tidak menimpa kalau kuncinya sudah ada
    nilai.emplace("Citra", 78);      // emplace: sama, tanpa merakit pair-nya dulu

    auto hasil = nilai.insert({"Andi", 999});      // Andi sudah ada
    cout << "Andi tertimpa? " << hasil.second << endl;   // 0 -- insert menolak, diam-diam
    cout << "Nilai Andi tetap " << nilai["Andi"] << endl;   // 85

    cout << "at(Budi) = " << nilai.at("Budi") << endl;      // 90
    try {
        cout << nilai.at("Dedi") << endl;   // tidak ada -> MELEMPAR, bukan bikin entri baru
    } catch (const out_of_range &e) {
        cout << "at(Dedi) melempar out_of_range" << endl;
    }

    // Bentuk range-for yang paling sering terlihat di kode C++17 modern
    for (const auto &[nama, angka] : nilai) {
        cout << nama << " -> " << angka << endl;
    }
    cout << "Jumlah entri: " << nilai.size() << endl;   // 3 -- at() tidak menambah apa pun
    return 0;
}"""
            },
        ],
    },
    {
        "title": "23. STL: unordered_map, stack, queue & Container Lain",
        "sections": [
            {
                "body": [
                    "Materi sebelumnya mengenalkan vector, map, set, dan pair, lalu",
                    "MENYEBUT unordered_map sambil lalu. Padahal di kode C++ yang beredar",
                    "di dunia nyata, unordered_map justru yang paling sering kamu temui.",
                    "Di sampingnya ada stack, queue, deque, priority_queue, dan list yang",
                    "muncul di hampir semua kode algoritmik tanpa pernah dijelaskan.",
                    "Materi ini menutup daftar itu, supaya tidak ada baris",
                    "'#include <queue>' yang membuatmu berhenti membaca.",
                    "",
                    "MAP vs UNORDERED_MAP: BEDANYA CUMA CARA MENYIMPAN",
                    "",
                    "Keduanya menyimpan pasangan key -> value, dan cara memakainya nyaris",
                    "identik. Yang berbeda adalah mesin di dalamnya:",
                    "",
                    "  map<K,V>            pohon biner seimbang. Key selalu tersusun",
                    "                      rapi menurut urutannya. Cari, sisip, hapus",
                    "                      O(log n). Header <map>.",
                    "  unordered_map<K,V>  tabel hash. Key dilempar ke 'ember' menurut",
                    "                      hasil hitungan hash, jadi posisinya terlihat",
                    "                      acak. Rata-rata O(1). Header <unordered_map>.",
                    "",
                    "O(1) rata-rata artinya: berapa pun isinya, satu pencarian butuh waktu",
                    "yang kira-kira sama. Pada map, tiap kali jumlah datanya berlipat dua,",
                    "pencarian bertambah satu langkah. Untuk sepuluh data bedanya tidak",
                    "terasa; untuk sejuta data, itu selisih yang nyata.",
                    "",
                    "Kata 'rata-rata' di situ jujur: kalau banyak key kebetulan jatuh ke",
                    "ember yang sama, unordered_map bisa melambat sampai O(n). Untuk key",
                    "biasa seperti int dan string, itu praktis tidak pernah terjadi.",
                    "",
                    "PILIH YANG MANA",
                    "",
                    "Pakai unordered_map sebagai PILIHAN DEFAULT. Sebagian besar kode cuma",
                    "butuh satu hal: 'diberi key, berikan value-nya, cepat'. Urutan key",
                    "tidak dipakai untuk apa-apa.",
                    "",
                    "Pindah ke map hanya kalau salah satu dari ini benar:",
                    "  - Kamu perlu menelusuri isinya dalam keadaan TERURUT, misalnya",
                    "    untuk mencetak laporan.",
                    "  - Kamu perlu key terkecil/terbesar, atau 'key pertama yang >= X'",
                    "    (lower_bound).",
                    "  - Key-nya tipe buatanmu sendiri. map cukup butuh operator<,",
                    "    sedangkan unordered_map menuntut fungsi hash - dan tanpa itu",
                    "    kodenya gagal KOMPILASI dengan pesan sangat panjang dari dalam",
                    "    std::hash, yang hampir mustahil dibaca kalau kamu tidak tahu",
                    "    sebabnya.",
                    "",
                    "JEBAKAN: URUTAN ITERASI UNORDERED TIDAK BOLEH DIANDALKAN",
                    "",
                    "Iterasi unordered_map memberi urutan yang tidak dijanjikan siapa pun,",
                    "dan urutan itu bisa berubah kalau isinya bertambah, kalau compiler-nya",
                    "beda, atau kalau versinya naik. Program yang keluarannya kebetulan",
                    "benar di komputermu bisa mencetak urutan lain di komputer orang lain.",
                    "Kalau keluaranmu harus berurutan: pakai map, atau salin key-nya ke",
                    "vector lalu sort(). Hal yang sama berlaku untuk unordered_set vs set.",
                ],
            },
            {
                "heading": "unordered_map & unordered_set - dan jebakan operator[]",
                "body": [
                    "Jebakan ini berlaku untuk map maupun unordered_map, dan ia menyerang",
                    "pemula maupun yang sudah lama. m[\"key\"] pada key yang BELUM ADA tidak",
                    "mengembalikan error dan tidak mengembalikan 'kosong' - ia MEMBUAT",
                    "entri baru berisi nilai default (0 untuk int, string kosong untuk",
                    "string), lalu mengembalikan entri itu. Jadi sekadar MEMBACA lewat []",
                    "diam-diam menumbuhkan map-mu. Perhatikan angka size() di bawah.",
                ],
                "code": """#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <string>
using namespace std;

int main() {
    unordered_map<string, int> stok;
    stok["pensil"] = 12;
    stok["buku"] = 5;
    stok["penghapus"] = 30;

    cout << "buku: " << stok["buku"] << endl;
    cout << "jumlah key: " << stok.size() << endl;      // 3

    // JEBAKAN: operator[] MEMBUAT key baru bernilai 0 kalau key belum ada
    cout << "stok spidol: " << stok["spidol"] << endl;  // 0 - spidol kini ADA
    cout << "jumlah key: " << stok.size() << endl;      // 4

    // Cara membaca TANPA menyisipkan apa pun: find() lebih dulu
    auto it = stok.find("krayon");
    cout << "stok krayon: " << (it == stok.end() ? 0 : it->second) << endl;
    cout << "jumlah key: " << stok.size() << endl;      // tetap 4

    // Menghitung frekuensi - pemakaian unordered_map yang paling sering
    unordered_map<char, int> hitung;
    for (char c : string("banana")) {
        hitung[c]++;        // di sini [] yang menyisipkan justru MEMBANTU
    }
    // Urutan iterasi unordered_map TIDAK dijamin, jadi jangan
    // mengandalkannya: cetak lewat key yang kita tentukan sendiri.
    for (char c : {'a', 'b', 'n'}) {
        cout << c << " = " << hitung[c] << endl;
    }

    unordered_set<string> hadir = {"Andi", "Budi"};
    hadir.insert("Andi");                               // duplikat diabaikan
    cout << "peserta unik: " << hadir.size() << endl;   // 2
    cout << "Budi hadir? " << (hadir.count("Budi") ? "ya" : "tidak") << endl;

    return 0;
}""",
            },
            {
                "heading": "Container adaptor: stack, queue & priority_queue",
                "body": [
                    "Ketiganya disebut ADAPTOR, bukan container baru. Isinya tetap",
                    "disimpan di deque atau vector; yang dilakukan adaptor adalah MENUTUP",
                    "semua operasi lain dan hanya menyisakan yang masuk akal untuk",
                    "struktur itu. Itu bukan kekurangan, itu justru gunanya: siapa pun",
                    "yang membaca 'stack<int> s' langsung tahu tidak ada yang bisa",
                    "menyelinap ke tengah tumpukan.",
                    "",
                    "  stack<T>   LIFO - terakhir masuk, pertama keluar.",
                    "             push, top, pop, empty, size. Header <stack>.",
                    "             Dipakai untuk undo, riwayat halaman, mencocokkan",
                    "             tanda kurung, dan DFS.",
                    "  queue<T>   FIFO - pertama masuk, pertama keluar.",
                    "             push, front, back, pop, empty, size. Header <queue>.",
                    "             Ini tulang punggung BFS: tetangga didorong ke",
                    "             belakang, yang diproses selalu yang paling depan.",
                    "             Juga antrean tugas - pekerjaan masuk dari satu ujung,",
                    "             pekerja mengambil dari ujung lain.",
                    "  priority_queue<T>",
                    "             yang keluar duluan bukan yang terlama, tapi yang",
                    "             TERBESAR. push, top, pop, empty, size. Headernya",
                    "             JUGA <queue>, bukan <priority_queue> - berkas dengan",
                    "             nama itu tidak ada.",
                    "",
                    "Bentuk min-heap-nya (yang keluar duluan justru yang TERKECIL)",
                    "ditulis lengkap bertiga:",
                    "",
                    "    priority_queue<int, vector<int>, greater<int>> antre;",
                    "",
                    "Argumen kedua adalah container penyimpannya, dan kamu tetap harus",
                    "menuliskannya meski nilainya sama dengan bawaan - di C++ tidak ada",
                    "cara melewati argumen tengah. greater<int> berasal dari",
                    "<functional>. Bentuk ini yang dipakai algoritma Dijkstra dan 'ambil",
                    "N terkecil', jadi kamu akan sering melihatnya persis seperti itu.",
                    "",
                    "JEBAKAN NOMOR SATU: pop() TIDAK MENGEMBALIKAN NILAI",
                    "",
                    "  int x = s.pop();   // SALAH, gagal kompilasi - pop() bertipe void",
                    "  int x = s.top();   // benar: lihat dulu",
                    "  s.pop();           // lalu buang",
                    "",
                    "Ini bukan kelalaian perancangnya. Kalau pop() mengembalikan salinan",
                    "nilainya, lalu penyalinan itu melempar exception, elemennya sudah",
                    "telanjur dihapus dan datanya hilang tanpa bisa diselamatkan. Dipisah",
                    "jadi dua langkah, tidak ada keadaan setengah jadi.",
                    "",
                    "JEBAKAN KEDUA: top() atau front() pada wadah KOSONG bukan error,",
                    "melainkan undefined behavior. Tidak ada exception, tidak ada pesan",
                    "apa pun - kamu bisa mendapat angka sampah, atau crash yang muncul",
                    "jauh dari sumbernya. SELALU jaga dengan while (!s.empty()).",
                    "",
                    "JEBAKAN KETIGA: adaptor tidak punya begin()/end(). Ia tidak bisa",
                    "dipakai di range-based for maupun di fungsi <algorithm>, dan",
                    "satu-satunya cara melihat seluruh isinya adalah mengosongkannya.",
                    "Kalau kamu butuh menelusuri isinya berulang kali, berarti container",
                    "yang kamu pilih memang salah.",
                ],
            },
            {
                "heading": "stack, queue, deque & priority_queue dalam satu program",
                "code": """#include <iostream>
#include <stack>
#include <queue>
#include <deque>
#include <vector>
#include <functional>
#include <string>
using namespace std;

int main() {
    // stack: LIFO - yang TERAKHIR masuk, PERTAMA keluar
    stack<string> riwayat;
    riwayat.push("beranda");
    riwayat.push("daftar-produk");
    riwayat.push("detail-produk");

    cout << "Halaman sekarang: " << riwayat.top() << endl;

    // pop() TIDAK mengembalikan apa-apa: ambil dulu pakai top(), BARU pop()
    string ditinggalkan = riwayat.top();
    riwayat.pop();
    cout << "Back dari " << ditinggalkan << " -> " << riwayat.top() << endl;

    while (!riwayat.empty()) {      // selalu cek empty() sebelum top()
        cout << "sisa riwayat: " << riwayat.top() << endl;
        riwayat.pop();
    }

    // queue: FIFO - yang PERTAMA masuk, PERTAMA keluar
    queue<string> antrean;
    antrean.push("Andi");
    antrean.push("Budi");
    antrean.push("Citra");
    cout << "Dilayani: " << antrean.front()
         << " | paling belakang: " << antrean.back() << endl;
    antrean.pop();                 // Andi selesai dilayani
    cout << "Giliran berikutnya: " << antrean.front() << endl;

    // deque: seperti vector, tapi BISA tumbuh di kedua ujung
    deque<int> d = {2, 3};
    d.push_front(1);
    d.push_back(4);
    for (int n : d) cout << n << " ";
    cout << endl;
    cout << "index tetap bisa dipakai, d[2] = " << d[2] << endl;

    // priority_queue: yang keluar duluan adalah yang TERBESAR (max-heap)
    priority_queue<int> terbesar;
    for (int n : {4, 9, 1, 7}) terbesar.push(n);
    cout << "prioritas tertinggi: " << terbesar.top() << endl;

    // Bentuk min-heap - argumen template ini WAJIB lengkap bertiga
    priority_queue<int, vector<int>, greater<int>> terkecil;
    for (int n : {4, 9, 1, 7}) terkecil.push(n);
    cout << "keluar berurutan naik:";
    while (!terkecil.empty()) {
        cout << " " << terkecil.top();
        terkecil.pop();
    }
    cout << endl;

    return 0;
}""",
            },
            {
                "heading": "deque, list, dan tabel pemilihan container",
                "body": [
                    "deque<T> (dibaca 'dek', dari double-ended queue, header <deque>)",
                    "adalah vector yang JUGA bisa tumbuh di depan lewat push_front dan",
                    "pop_front. vector tidak punya keduanya, dan menyisipkan di awal",
                    "vector memaksa seluruh isinya bergeser satu per satu. deque juga",
                    "yang diam-diam dipakai stack dan queue sebagai penyimpan bawaannya.",
                    "",
                    "list<T> (header <list>) adalah doubly linked list. Menyisipkan atau",
                    "menghapus di tengah hanya menyambung ulang dua penunjuk - TAPI itu",
                    "berlaku kalau kamu SUDAH memegang posisi elemennya; mencari posisi",
                    "itu tetap harus ditelusuri dari ujung. Ia juga tidak punya akses",
                    "index sama sekali: l[3] tidak ada.",
                    "",
                    "Karena tiap elemen list dialokasikan terpisah, isinya berserakan di",
                    "memori dan prosesor kehilangan keuntungan membaca data yang",
                    "berdampingan. Akibatnya sering mengejutkan: untuk data berukuran",
                    "wajar, vector MENGALAHKAN list bahkan pada operasi yang secara teori",
                    "list menang. Pakai list hanya kalau kamu benar-benar sering",
                    "menyunting di tengah sambil sudah memegang iteratornya, atau butuh",
                    "splice untuk memindahkan potongan antar list. Kalau ragu: vector.",
                    "",
                    "  Butuh apa                                    Pakai apa",
                    "  ------------------------------------------   --------------",
                    "  Daftar biasa, akses index, iterasi           vector",
                    "  Tambah/hapus cepat di KEDUA ujung            deque",
                    "  Ukuran tetap & diketahui saat menulis kode   array<T, N>",
                    "  Key -> value, urutan tidak dipakai           unordered_map",
                    "  Key -> value, wajib terurut / butuh min-max  map",
                    "  Kumpulan unik, urutan tidak dipakai          unordered_set",
                    "  Kumpulan unik yang terurut                   set",
                    "  Terakhir masuk keluar duluan (undo, DFS)     stack",
                    "  Pertama masuk keluar duluan (BFS, antrean)   queue",
                    "  Selalu ambil yang terbesar/terkecil dulu     priority_queue",
                    "  Sering menyunting di tengah, tanpa index     list",
                    "",
                    "Semua container di atas mengelola memorinya sendiri dan",
                    "membebaskannya saat keluar scope - tidak ada satu pun delete yang",
                    "perlu kamu tulis. Dan kesalahan yang paling sering terjadi bukan",
                    "salah memilih antara map dan unordered_map, melainkan memaksakan",
                    "vector lalu mencari isinya dengan loop manual di setiap tempat,",
                    "padahal yang dibutuhkan sejak awal adalah sebuah map.",
                ],
            },
        ],
    },
    {
        "title": "24. Iterator: Menelusuri & Menyunting Container",
        "sections": [
            {
                "body": [
                    "Di materi Algorithm, .begin() dan .end() selalu cuma DIOPER ke",
                    "sort/find. Padahal keduanya mengembalikan sebuah NILAI biasa yang",
                    "boleh disimpan di variabel sendiri: itulah iterator - penunjuk",
                    "posisi di dalam container.",
                    "",
                    "  auto it = v.begin();   // it menunjuk elemen PERTAMA",
                    "  cout << *it;           // *it = nilai di posisi itu (deref)",
                    "  *it = 99;              // *it boleh jadi SASARAN penugasan juga",
                    "  ++it;                  // geser it ke posisi berikutnya",
                    "",
                    "end() BUKAN elemen terakhir. Ia posisi SATU-SETELAH-terakhir,",
                    "penanda garis finis yang sengaja tidak berisi apa-apa. Dua akibat",
                    "yang harus melekat di kepala:",
                    "  - Syarat loop-nya selalu it != v.end(), bukan it <= v.end().",
                    "  - *v.end() adalah undefined behavior. Biasanya TIDAK crash, cuma",
                    "    memberi angka sampah - jenis bug yang paling lama dicari orang.",
                    "",
                    "Kalau elemennya objek, struct, atau pair, pakai it->anggota sebagai",
                    "singkatan dari (*it).anggota - aturan yang sudah kamu kenal dari",
                    "pointer di materi Referensi.",
                    "",
                    "Kenapa bentuk panjang for (auto it = v.begin(); it != v.end(); ++it)",
                    "masih bertebaran di kode nyata? Sebelum C++11 belum ada range-based",
                    "for maupun auto, jadi inilah SATU-SATUNYA cara menelusuri map atau",
                    "list. Kode lama jarang ditulis ulang, dan kamu akan terus",
                    "membacanya seumur karier.",
                    "",
                    "Sebaliknya, for (auto &x : v) bukan mekanisme yang berbeda -",
                    "compiler menerjemahkannya menjadi loop iterator seperti di atas.",
                    "Itu sebabnya container apa pun yang punya begin() dan end()",
                    "otomatis bisa dipakai di range-based for.",
                ],
            },
            {
                "heading": "Contoh: maju, mundur, dan versi yang tidak boleh diubah",
                "code": """#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
    vector<string> antrean = {"Andi", "Budi", "Citra"};

    // Bentuk PANJANG: it sebuah variabel biasa, isinya "posisi", bukan nilai
    for (vector<string>::iterator it = antrean.begin(); it != antrean.end(); ++it) {
        cout << *it << " ";          // *it = NILAI yang ada di posisi itu
    }
    cout << endl;

    // Sama persis, tapi tipe panjangnya dibiarkan ditebak compiler (C++11)
    for (auto it = antrean.begin(); it != antrean.end(); ++it) {
        *it += "!";                  // *it bisa jadi SASARAN penugasan juga
    }

    // cbegin/cend memberi const_iterator: boleh dibaca, HARAM diubah
    for (auto it = antrean.cbegin(); it != antrean.cend(); ++it) {
        cout << *it << " ";
        // *it += "?";   <- baris ini TIDAK akan mau dikompilasi
    }
    cout << endl;

    // rbegin/rend menelusuri MUNDUR; ++it tetap dipakai, tapi majunya ke kiri
    for (auto it = antrean.rbegin(); it != antrean.rend(); ++it) {
        cout << *it << " ";
    }
    cout << endl;

    // Khusus vector, selisih dua iterator = jarak posisi alias indeksnya
    auto it = antrean.begin() + 1;
    cout << "Indeks " << (it - antrean.begin()) << " berisi " << *it << endl;

    return 0;
}""",
            },
            {
                "body": [
                    "Pada map, iterator menunjuk sebuah pair, jadi:",
                    "  it->first  -> KUNCInya. Bertipe const: mengubahnya akan merusak",
                    "                urutan map, sehingga compiler langsung menolak.",
                    "  it->second -> NILAInya. Ini boleh diubah: it->second = 90;",
                    "",
                    "Materi sebelumnya memeriksa keberadaan kunci dengan m.count(kunci).",
                    "Itu benar, tapi kalau sesudahnya kamu tetap butuh nilainya, map",
                    "dicari DUA KALI - sekali oleh count, sekali lagi oleh m[kunci].",
                    "Bentuk baku yang dipakai di mana-mana mencari sekali saja lalu",
                    "langsung memakai hasil pencariannya:",
                    "",
                    "  auto it = m.find(kunci);",
                    "  if (it != m.end()) {",
                    "      cout << it->first << \" = \" << it->second;",
                    "  } else {",
                    "      cout << \"tidak ada\";",
                    "  }",
                    "",
                    "JEBAKAN operator[] yang membuat data hantu",
                    "",
                    "m[kunci] pada map BUKAN sekadar membaca. Kalau kuncinya belum ada,",
                    "ia DIAM-DIAM membuat entri baru berisi nilai default (0 untuk int,",
                    "string kosong untuk string) lalu mengembalikan entri itu. Tidak ada",
                    "error, tidak ada peringatan compiler.",
                    "",
                    "Akibat yang benar-benar terjadi di kode nyata:",
                    "  - if (m[\"Dedi\"] == 0) menambah satu anggota ke map cuma karena",
                    "    kuncinya diperiksa.",
                    "  - Loop yang mengecek 1000 kunci bisa menggelembungkan map jadi",
                    "    1000 entri.",
                    "  - Laporan 'jumlah siswa' jadi salah, dan penyebabnya ada di baris",
                    "    yang kelihatannya cuma membaca - itulah kenapa bug ini sulit",
                    "    dicurigai.",
                    "  - Pada map yang const, m[kunci] bahkan TIDAK BISA dikompilasi,",
                    "    karena ia memang berhak mengubah isi.",
                    "",
                    "Aturan aman: pakai find() untuk memeriksa dan membaca, pakai []",
                    "hanya saat kamu memang mau MENULIS (m[kunci] = nilai). Untuk",
                    "sekadar ada/tidak, count() tetap paling ringkas, dan sejak C++20",
                    "ada m.contains(kunci) yang lebih jelas maksudnya.",
                ],
            },
            {
                "heading": "Contoh: idiom find() dan jebakan operator[]",
                "code": """#include <iostream>
#include <map>
#include <string>
using namespace std;

int main() {
    map<string, int> nilai = {{"Andi", 85}, {"Budi", 90}, {"Citra", 78}};

    // Idiom baku: cari SEKALI, lalu pakai hasil pencariannya
    auto it = nilai.find("Budi");
    if (it != nilai.end()) {
        cout << it->first << " nilainya " << it->second << endl;
        it->second += 5;             // menyunting isi map lewat iterator
        cout << "Setelah remedial: " << it->second << endl;
    }

    // Kunci yang tidak ada tidak bikin crash - find cuma mengembalikan end()
    if (nilai.find("Dedi") == nilai.end()) {
        cout << "Dedi belum terdaftar" << endl;
    }
    cout << "Jumlah entri: " << nilai.size() << endl;

    // JEBAKAN: membaca dengan [] justru MEMBUAT entrinya
    cout << "Baca nilai Dedi pakai []: " << nilai["Dedi"] << endl;
    cout << "Jumlah entri sekarang: " << nilai.size() << endl;

    for (auto it2 = nilai.begin(); it2 != nilai.end(); ++it2) {
        cout << it2->first << "=" << it2->second << " ";
    }
    cout << endl;

    return 0;
}""",
            },
            {
                "body": [
                    "Menghapus sambil menelusuri adalah tempat orang paling sering",
                    "tersandung, dan hukumannya bukan pesan error melainkan program yang",
                    "kadang benar kadang tidak.",
                    "",
                    "Sebabnya: menghapus sebuah elemen membuat iterator yang menunjuk",
                    "elemen itu TIDAK SAH lagi. Menulis ++it sesudah v.erase(it) berarti",
                    "menggeser penunjuk yang sudah mati. Karena itu erase() MENGEMBALIKAN",
                    "iterator elemen berikutnya, dan bentuk benarnya menahan diri supaya",
                    "tidak maju dua kali:",
                    "",
                    "  it = v.erase(it);   // kalau menghapus: pakai kembalian erase",
                    "  ++it;               // kalau TIDAK menghapus: baru maju sendiri",
                    "",
                    "Perhatikan bagian ketiga for-nya dikosongkan:",
                    "  for (auto it = v.begin(); it != v.end(); )",
                    "Kalau ++it tetap ditulis di situ, tiap penghapusan akan MELEWATI",
                    "satu elemen - dua angka genap berurutan bikin salah satunya lolos",
                    "tanpa jejak.",
                    "",
                    "Yang juga membatalkan iterator, dan sering lupa:",
                    "  - vector: push_back/insert/resize bisa memindahkan seluruh isi ke",
                    "    blok memori baru saat kapasitasnya habis, dan SEMUA iterator",
                    "    lama (termasuk end()) mati seketika. Bahayanya, kalau",
                    "    kapasitasnya kebetulan masih cukup, kodenya jalan normal - jadi",
                    "    bug ini baru muncul saat datanya membesar.",
                    "  - map/set: hanya iterator ke elemen yang dihapus yang mati;",
                    "    sisanya tetap sah.",
                    "",
                    "Dan karena for (auto &x : v) juga loop iterator, menambah elemen ke",
                    "v di dalamnya adalah bug yang sama persis - cuma lebih sulit",
                    "dilihat karena iteratornya disembunyikan.",
                ],
                "code": """#include <iostream>
#include <vector>
#include <map>
#include <string>
using namespace std;

int main() {
    vector<int> data = {1, 2, 3, 4, 5, 6};

    // Perhatikan: bagian ketiga for-nya SENGAJA dikosongkan
    for (auto it = data.begin(); it != data.end(); ) {
        if (*it % 2 == 0) {
            it = data.erase(it);     // erase mengembalikan iterator BERIKUTNYA
        } else {
            ++it;                    // hanya maju kalau tidak ada yang dihapus
        }
    }
    for (int n : data) cout << n << " ";
    cout << endl;

    // Pola yang sama persis untuk map, dengan it->second sebagai syaratnya
    map<string, int> stok = {{"beras", 0}, {"gula", 5}, {"teh", 0}};
    for (auto it = stok.begin(); it != stok.end(); ) {
        if (it->second == 0) {
            cout << "Habis, dicoret: " << it->first << endl;
            it = stok.erase(it);
        } else {
            ++it;
        }
    }
    cout << "Sisa jenis barang: " << stok.size() << endl;

    return 0;
}""",
            },
        ],
    },
    {
        "title": "25. STL: Algorithm Library",
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

    // count_if: menghitung elemen yang MEMENUHI SYARAT. Syaratnya ditulis sebagai
    // LAMBDA -- fungsi tanpa nama yang dibahas tuntas di materi Lambda Expression
    // & Fitur Modern C++. Bentuknya: [](int n) { return <syarat>; } dan 'n' itu
    // tiap elemen, dioperkan satu per satu oleh count_if.
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
            {
                "heading": "find_if, for_each & accumulate yang berlambda",
                "body": [
                    "Daftar di atas berhenti terlalu cepat. Tiga bentuk berikut ada di",
                    "hampir semua kode yang memakai <algorithm>, dan dua di antaranya",
                    "kamu butuhkan begitu masuk latihan.",
                    "",
                    "find_if(begin, end, syarat)",
                    "",
                    "  find mencari NILAI yang persis sama; find_if mencari elemen",
                    "  PERTAMA yang memenuhi syarat. Yang dikembalikan sebuah ITERATOR -",
                    "  bukan elemennya, bukan pula posisinya. Idiom lengkapnya selalu",
                    "  dua baris ini, dan jangan pernah dipotong jadi satu:",
                    "",
                    "    auto it = find_if(v.begin(), v.end(), [](int n) { return n > 7; });",
                    "    if (it != v.end()) { cout << *it; }      // WAJIB dicek dulu",
                    "",
                    "  Melewatkan pemeriksaan '!= end()' lalu langsung menulis *it adalah",
                    "  undefined behavior saat tidak ada yang cocok: biasanya tidak crash,",
                    "  cuma memberi angka sampah - jenis bug yang paling lama dicari.",
                    "",
                    "for_each(begin, end, aksi)",
                    "",
                    "  Menjalankan aksi untuk TIAP elemen. Ia tidak mengembalikan apa-apa",
                    "  yang berguna; gunanya cuma menyingkat loop, dan sejak ada",
                    "  range-based for ia lebih sering kamu BACA daripada kamu tulis.",
                    "",
                    "accumulate dengan EMPAT argumen",
                    "",
                    "  Bentuk tiga argumen di contoh atas cuma bisa menjumlah. Argumen",
                    "  keempat menerima lambda, dan dengan itu ia bisa menggabungkan",
                    "  apa saja - mengalikan, menghitung bersyarat, merangkai teks:",
                    "",
                    "    accumulate(begin, end, nilaiAwal, [](Hasil sejauhIni, Elemen e) {",
                    "        return <hasil gabungan yang baru>;",
                    "    });",
                    "",
                    "  Peran kedua parameter lambda-nya gampang tertukar, jadi hafalkan:",
                    "    - parameter PERTAMA = akumulator yang sedang berjalan (isinya",
                    "      nilaiAwal pada putaran pertama),",
                    "    - parameter KEDUA  = elemen yang sedang dikunjungi,",
                    "    - yang DIKEMBALIKAN jadi akumulator untuk putaran berikutnya.",
                    "  Kalau tertukar, hasilnya salah tanpa satu pun pesan error.",
                    "",
                    "Terakhir, satu bentuk yang perlu kamu KENALI dulu tanpa harus",
                    "mengerti: greater<int>() yang jadi argumen ketiga sort di contoh",
                    "atas. Perhatikan tanda kurung di ujungnya - yang dioper ke sort",
                    "bukan NAMA sebuah fungsi, ada sesuatu yang DIBUAT di situ juga.",
                    "Saudaranya less<int>() adalah urutan bawaan sort. Benda apa itu",
                    "sebenarnya, dan kenapa ia boleh dipanggil seperti fungsi,",
                    "dibongkar tuntas di materi Functor & std::function.",
                ],
            },
            {
                "heading": "find_if, for_each & accumulate empat argumen",
                "code": """#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
using namespace std;

int main() {
    vector<int> data = {5, 2, 8, 1, 9, 3};

    // find_if: seperti find, tapi syaratnya sebuah LAMBDA. Hasilnya ITERATOR.
    auto it = find_if(data.begin(), data.end(), [](int n) { return n > 7; });
    if (it != data.end()) {                    // WAJIB dicek sebelum *it dipakai
        cout << "Angka >7 pertama: " << *it << endl;                  // 8
        cout << "Posisinya      : " << (it - data.begin()) << endl;   // 2
    }

    // for_each: jalankan sesuatu untuk TIAP elemen
    for_each(data.begin(), data.end(), [](int n) { cout << n * 10 << " "; });
    cout << endl;                              // 50 20 80 10 90 30

    // accumulate EMPAT argumen: nilai awal + lambda penggabung
    int totalGenap = accumulate(data.begin(), data.end(), 0,
        [](int sejauhIni, int n) {
            return (n % 2 == 0) ? sejauhIni + n : sejauhIni;
        });
    cout << "Jumlah yang genap: " << totalGenap << endl;    // 10

    long hasilKali = accumulate(data.begin(), data.end(), 1L,
        [](long sejauhIni, int n) { return sejauhIni * n; });
    cout << "Hasil kali semua: " << hasilKali << endl;      // 2160
    return 0;
}"""
            },
        ],
    },
    {
        "title": "26. Smart Pointer: unique_ptr & shared_ptr",
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
            {
                "heading": "Menyeberang antara PEMILIK dan PEMINJAM",
                "body": [
                    "Smart pointer memisahkan dua peran yang di C selalu tercampur:",
                    "yang MEMILIKI objek (bertanggung jawab menghapusnya) dan yang",
                    "cuma MEMINJAM (memakainya sebentar lalu selesai). Tiga method",
                    "berikut adalah pintu antar keduanya.",
                    "",
                    "  .get()      Mengembalikan raw pointer di dalamnya, UNTUK",
                    "              DIPINJAM. Kepemilikan TIDAK pindah - smart",
                    "              pointer-nya tetap yang akan menghapus objek itu.",
                    "              Dipakai saat kamu harus memanggil fungsi lama",
                    "              yang parameternya masih T*. Yang HARAM: menaruh",
                    "              hasil .get() ke smart pointer lain, atau",
                    "              men-delete-nya sendiri - keduanya bikin objeknya",
                    "              dihapus dua kali.",
                    "",
                    "  .reset()    Melepas isinya SEKARANG juga (objeknya dihapus),",
                    "              tanpa menunggu keluar scope. Smart pointer-nya",
                    "              jadi kosong dan boleh dipakai lagi.",
                    "",
                    "  .release()  Melepas KEPEMILIKAN tanpa menghapus apa pun: ia",
                    "              menyerahkan raw pointer-nya lalu mengosongkan",
                    "              diri. Mulai detik itu KAMU yang wajib men-delete.",
                    "              Jarang benar-benar dibutuhkan; kalau kamu merasa",
                    "              memerlukannya, biasanya std::move ke pemilik baru",
                    "              yang sebenarnya kamu maksud.",
                    "",
                    "Aturan mengoper smart pointer ke fungsi - hafalkan tiga baris ini:",
                    "",
                    "  void pakai(const Mahasiswa &m)   // cuma MEMBACA objeknya",
                    "  void pakai(Mahasiswa *m)         // boleh mengubah, boleh null",
                    "  void ambilAlih(unique_ptr<Mahasiswa> m)   // KEPEMILIKAN pindah",
                    "",
                    "Fungsi yang cuma MEMAKAI objek sebaiknya tidak pernah menyebut",
                    "kata unique_ptr atau shared_ptr sama sekali - minta reference",
                    "atau raw pointer saja, supaya ia bisa dipakai objek dari mana",
                    "pun asalnya. Hanya fungsi yang benar-benar mengambil alih yang",
                    "meminta unique_ptr utuh, dan pemanggilnya WAJIB menulis",
                    "std::move - tanpa itu compiler menolak, karena unique_ptr",
                    "memang tidak bisa disalin.",
                    "",
                    "weak_ptr - anggota ketiga keluarga ini",
                    "",
                    "shared_ptr punya satu titik buta: SIKLUS. Kalau A memegang",
                    "shared_ptr ke B dan B memegang shared_ptr ke A, hitungan",
                    "keduanya tidak pernah mencapai nol - keduanya saling menahan,",
                    "dan dua-duanya bocor walaupun tidak ada lagi yang memakainya.",
                    "Bentuk yang paling sering kena: parent-child, dan observer yang",
                    "menyimpan balik pointer ke objek yang mengamatinya.",
                    "",
                    "weak_ptr<T> menunjuk objek TANPA ikut memiliki: ia tidak",
                    "menambah hitungan referensi, jadi ia tidak bisa menahan apa pun",
                    "tetap hidup. Putuskan siklusnya dengan membuat SATU arah saja",
                    "yang shared_ptr (parent -> child), dan arah baliknya weak_ptr.",
                    "",
                    "Karena objeknya bisa saja sudah terhapus, weak_ptr tidak boleh",
                    "langsung dipakai. Kamu harus meminta izin dulu lewat .lock():",
                    "",
                    "  if (auto p = w.lock()) { ... }   // p = shared_ptr sementara",
                    "",
                    "Kalau objeknya masih hidup, .lock() memberi shared_ptr yang",
                    "menjaganya tetap hidup selama blok itu. Kalau sudah terhapus, ia",
                    "memberi shared_ptr kosong dan blok itu dilewati - tidak ada",
                    "dangling pointer, tidak ada crash. Ada juga w.expired() kalau",
                    "kamu cuma ingin tahu masih hidup atau tidak.",
                ],
            },
            {
                "heading": "get, reset, std::move & weak_ptr",
                "code": """#include <iostream>
#include <memory>
#include <string>
using namespace std;

class Mahasiswa {
public:
    string nama;
    Mahasiswa(string n) : nama(n) {}
    ~Mahasiswa() { cout << "  [hapus " << nama << "]" << endl; }
};

// PEMINJAM: cuma memakai objeknya, tidak ikut memiliki -> pointer/reference biasa
void cetak(const Mahasiswa *m) {
    cout << "Dipinjam: " << m->nama << endl;
}

// PENERIMA KEPEMILIKAN: minta unique_ptr utuh -> pemanggil WAJIB pakai std::move
void arsipkan(unique_ptr<Mahasiswa> milik) {
    cout << "Kepemilikan " << milik->nama << " pindah ke arsipkan()" << endl;
}   // dihapus DI SINI, karena sekarang dialah pemiliknya

int main() {
    auto u = make_unique<Mahasiswa>("Andi");

    cetak(u.get());          // .get() = pinjamkan raw pointer-nya; kepemilikan TIDAK pindah
    cout << "u masih memiliki? " << (u ? "ya" : "tidak") << endl;      // ya

    u = make_unique<Mahasiswa>("Budi");   // Andi otomatis dihapus saat digantikan
    cout << "Sekarang u memegang " << u->nama << endl;

    arsipkan(std::move(u));  // TANPA std::move: error, unique_ptr tidak bisa disalin
    cout << "Setelah dipindah, u kosong? " << (u ? "tidak" : "ya") << endl;   // ya

    // weak_ptr: menunjuk TANPA ikut memiliki
    shared_ptr<Mahasiswa> s = make_shared<Mahasiswa>("Citra");
    weak_ptr<Mahasiswa> w = s;                        // use_count TIDAK bertambah
    cout << "use_count: " << s.use_count() << endl;   // 1

    if (auto pinjam = w.lock()) {        // .lock() -> shared_ptr sementara, atau kosong
        cout << "Masih hidup: " << pinjam->nama << endl;
    }
    s.reset();                           // pemilik terakhir melepas -> objek dihapus
    cout << "w kadaluarsa? " << (w.expired() ? "ya" : "tidak") << endl;      // ya
    return 0;
}"""
            },
        ],
    },
    {
        "title": "27. Exception Handling",
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
            {
                "heading": "Membongkar baris 'const char* what() const noexcept override'",
                "body": [
                    "Baris itu ada di contoh atas, dan ia baris yang paling sering",
                    "membuat orang menyerah - lima kata asing berderet tanpa spasi",
                    "untuk bernapas. Dibaca dari kiri ke kanan, satu per satu:",
                    "",
                    "  const char*   Tipe KEMBALIANNYA: pointer ke teks gaya C yang",
                    "                tidak boleh diubah. Bukan std::string - itu",
                    "                sebabnya isinya dikembalikan dengan .c_str().",
                    "",
                    "  what()        Namanya. Wajib persis ini, karena inilah nama",
                    "                yang dipakai std::exception.",
                    "",
                    "  const         Method ini TIDAK MENGUBAH objeknya (kamu sudah",
                    "                bertemu ini di materi Encapsulation).",
                    "",
                    "  noexcept      Janji: fungsi ini TIDAK AKAN melempar exception.",
                    "",
                    "  override      Menegaskan ini menimpa method virtual milik base",
                    "                class - compiler akan protes kalau tandanya",
                    "                ternyata tidak cocok.",
                    "",
                    "Yang benar-benar baru di situ cuma noexcept. Artinya sesederhana",
                    "janji di atas, tapi ada satu hal yang perlu kamu tahu: kalau",
                    "fungsi ber-noexcept ternyata TETAP melempar, program langsung",
                    "DIHENTIKAN paksa (std::terminate). Tidak ada catch yang bisa",
                    "menyelamatkannya - noexcept bukan permintaan, ia jaminan.",
                    "",
                    "Kenapa what() HARUS memakainya? Karena versi di base class-nya",
                    "sudah ber-noexcept, dan aturan override melarang versi turunan",
                    "jadi LEBIH LONGGAR dari yang ditimpanya. Menghapus noexcept di",
                    "situ langsung ditolak compiler. Jadi jangan dihafal sebagai",
                    "mantra - ia ada di situ karena base class-nya menuntut begitu.",
                    "",
                    "noexcept juga akan kamu temui lagi di materi RAII & Move",
                    "Semantics, di tempat yang justru menentukan performa.",
                ],
            },
            {
                "heading": "catch (...), lempar ulang & satu larangan keras",
                "body": [
                    "Dua bentuk terakhir yang melengkapi try-catch:",
                    "",
                    "  catch (...) { ... }",
                    "    Kurung dengan tiga titik menangkap APA SAJA - termasuk yang",
                    "    dilempar bukan sebagai turunan std::exception (di C++ kamu",
                    "    boleh melempar int atau string mentah, dan pustaka lama",
                    "    kadang begitu). Harganya: kamu tidak punya nama variabel,",
                    "    jadi tidak ada e.what() yang bisa dibaca - kamu tahu ada",
                    "    yang salah, tapi tidak tahu apa. Karena itu ia selalu",
                    "    ditaruh PALING BAWAH, sesudah catch yang spesifik, sebagai",
                    "    jaring pengaman - bukan sebagai penangan utama.",
                    "",
                    "  throw;",
                    "    'throw' TANPA argumen di dalam blok catch berarti: lempar",
                    "    ULANG exception yang sedang kamu tangani, apa adanya. Ini",
                    "    beda dengan 'throw e;' yang membuat SALINAN dan bisa",
                    "    kehilangan tipe aslinya. Dipakai untuk pola 'catat lalu",
                    "    teruskan': lapisan bawah mencatat kejadiannya, lapisan atas",
                    "    yang memutuskan program lanjut atau berhenti.",
                    "",
                    "Satu larangan keras: DESTRUCTOR TIDAK BOLEH MELEMPAR.",
                    "",
                    "Saat sebuah exception sedang naik mencari catch, C++ memanggil",
                    "destructor semua objek yang dilewatinya (stack unwinding, yang",
                    "barusan disebut di atas). Kalau salah satu destructor itu ikut",
                    "melempar, ada DUA exception aktif sekaligus dan C++ menyerah:",
                    "program dihentikan paksa, tanpa pesan yang berguna. Itu sebabnya",
                    "destructor di C++11 ke atas otomatis dianggap noexcept. Kalau di",
                    "dalam destructor ada yang bisa gagal - menutup berkas, mengirim",
                    "sisa data - tangkap sendiri di situ dengan try-catch, jangan",
                    "biarkan lolos keluar.",
                ],
                "code": """#include <iostream>
#include <stdexcept>
#include <string>
using namespace std;

void bacaKonfigurasi(int kode) {
    if (kode == 1) throw runtime_error("berkas konfigurasi tidak ditemukan");
    if (kode == 2) throw string("ini string biasa, BUKAN turunan std::exception");
    cout << "  konfigurasi terbaca" << endl;
}

void lapisanTengah(int kode) {
    try {
        bacaKonfigurasi(kode);
    } catch (const exception &e) {
        cout << "  [tengah] mencatat lalu meneruskan: " << e.what() << endl;
        throw;      // 'throw;' TANPA argumen = lempar ULANG yang sedang ditangani
    }
}

int main() {
    for (int kode = 0; kode <= 2; kode++) {
        cout << "kode " << kode << ":" << endl;
        try {
            lapisanTengah(kode);
        } catch (const exception &e) {
            cout << "  [main] ditangani: " << e.what() << endl;
        } catch (...) {         // menangkap APA SAJA, termasuk yang bukan std::exception
            cout << "  [main] sesuatu dilempar, tipenya tidak dikenali" << endl;
        }
    }
    return 0;
}"""
            },
        ],
    },
    {
        "title": "28. Berkas: ifstream & ofstream",
        "sections": [
            {
                "body": [
                    "Sampai sekarang semua data programmu lenyap begitu programnya berhenti.",
                    "cin dan cout cuma bicara dengan keyboard dan layar. Berkas adalah tempat",
                    "data BERTAHAN setelah program selesai - dan hampir semua program nyata",
                    "membutuhkan itu.",
                    "",
                    "Alatnya satu header: #include <fstream>. Isinya tiga tipe:",
                    "",
                    "  ofstream   output file stream  ->  MENULIS ke berkas",
                    "  ifstream   input file stream   ->  MEMBACA dari berkas",
                    "  fstream    baca DAN tulis sekaligus (jauh lebih jarang dipakai)",
                    "",
                    "Huruf depannya dibaca dari sudut pandang PROGRAM, bukan dari sudut",
                    "pandang berkasnya: 'o' = data KELUAR dari program menuju berkas,",
                    "'i' = data MASUK ke program dari berkas. Banyak orang tertukar di sini",
                    "pada minggu-minggu pertamanya.",
                    "",
                    "Yang membuat ini gampang: ketiganya STREAM, jenis benda yang sama",
                    "dengan cout dan cin. Semua yang sudah kamu pelajari di materi",
                    "Input/Output Modern langsung berlaku apa adanya:",
                    "",
                    "  keluar << \"Halo\" << 42 << '\\n';   // persis seperti cout <<",
                    "  masuk >> nama >> nilai;           // persis seperti cin >>",
                    "  getline(masuk, baris);            // persis seperti getline(cin, s)",
                    "",
                    "Yang berganti cuma ujung salurannya: bukan terminal, tapi sebuah berkas",
                    "di disk.",
                    "",
                    "Berkasnya dibuka lewat CONSTRUCTOR - mendeklarasikan dan membuka jadi",
                    "satu baris:",
                    "",
                    "  ofstream keluar(\"data.txt\");   // dibuka saat objeknya lahir",
                    "  ifstream masuk(\"data.txt\");",
                    "",
                    "Nama \"data.txt\" tanpa garis miring adalah PATH RELATIF, dan relatifnya",
                    "terhadap direktori tempat program DIJALANKAN - bukan tempat berkas .cpp",
                    "atau binernya berada. Biner yang sama, dijalankan dari folder lain,",
                    "mendadak 'tidak menemukan' berkas yang jelas-jelas ada di situ.",
                ],
            },
            {
                "heading": "Menulis, menambah, lalu membaca kembali",
                "code": """#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
    // ---- MENULIS. ofstream MEMBUAT catatan.txt, atau MENIMPA isi lamanya.
    ofstream keluar("catatan.txt");
    if (!keluar.is_open()) {             // gagal? berhenti sekarang juga
        cout << "Gagal membuka catatan.txt untuk menulis" << endl;
        return 1;
    }
    keluar << "Baris pertama" << '\\n';   // persis seperti cout <<
    keluar << "Angka: " << 42 << '\\n';
    keluar.close();   // EKSPLISIT: berkasnya langsung dibuka lagi di bawah

    // ---- MENAMBAH di akhir tanpa menghapus yang lama: mode ios::app
    ofstream tambah("catatan.txt", ios::app);
    tambah << "Baris tambahan" << '\\n';
    tambah.close();

    // ---- MEMBACA baris demi baris sampai habis
    ifstream masuk("catatan.txt");
    if (!masuk.is_open()) {              // TIDAK OPSIONAL - lihat penjelasan
        cout << "catatan.txt tidak bisa dibuka" << endl;
        return 1;
    }
    string baris;
    int nomor = 0;
    while (getline(masuk, baris)) {      // berhenti sendiri saat berkas habis
        nomor++;
        cout << nomor << ": " << baris << endl;
    }
    cout << "Selesai, " << nomor << " baris terbaca." << endl;
    // masuk tidak perlu di-close: destructor-nya menutup sendiri di sini
    return 0;
}""",
            },
            {
                "body": [
                    "Kenapa memeriksa is_open() itu WAJIB, bukan sekadar sopan santun:",
                    "",
                    "C++ TIDAK melempar exception saat sebuah berkas gagal dibuka. Stream-nya",
                    "cuma menyalakan penanda error di dalam dirinya, lalu setiap << dan >>",
                    "sesudahnya DIAM-DIAM tidak melakukan apa-apa. Program berjalan mulus",
                    "sampai habis dan keluar dengan kode 0, seolah semuanya baik-baik saja.",
                    "",
                    "  ofstream keluar(\"laporan/hasil.txt\");  // folder laporan/ tidak ada",
                    "  keluar << hasilKerjaSeharian;          // hilang, tanpa satu pesan pun",
                    "",
                    "Itu jenis kegagalan paling jahat: bukan program yang crash, tapi program",
                    "yang terlihat sukses padahal tidak menyimpan apa pun. Yang menyadarinya",
                    "biasanya kamu sendiri, seminggu kemudian, saat datanya dicari.",
                    "",
                    "Di sisi baca jebakannya kembar. Berkas KOSONG dan berkas TIDAK ADA",
                    "memberi hasil yang sama persis kalau kamu cuma melihat loop-nya -",
                    "dua-duanya berjalan nol kali:",
                    "",
                    "  berkas kosong     ->  is_open() true    (wajar, memang tak ada isi)",
                    "  berkas tidak ada  ->  is_open() false   (BUG: salah nama/salah folder)",
                    "",
                    "Bentuk ringkas yang juga sering kamu temui di kode orang lain:",
                    "",
                    "  if (!masuk) { ... }",
                    "",
                    "Artinya sama - sebuah stream yang bermasalah bernilai false kalau diuji",
                    "sebagai kondisi.",
                    "",
                    "MODE PEMBUKAAN, yaitu argumen kedua constructor:",
                    "",
                    "  (tanpa mode)  default ofstream. Berkas dibuat kalau belum ada, dan",
                    "                isi lamanya DIHAPUS HABIS begitu dibuka - bahkan kalau",
                    "                kamu tidak jadi menulis apa pun ke situ.",
                    "  ios::app      append: tulisanmu ditambahkan di AKHIR, isi lama utuh.",
                    "                Ini yang dipakai berkas log.",
                    "  ios::binary   data mentah, bukan teks (gambar, berkas terkompresi).",
                    "",
                    "SOAL close(): di C kamu WAJIB fclose(). Di C++ tidak. Destructor",
                    "ifstream/ofstream menutup berkasnya sendiri saat objeknya keluar scope",
                    "- termasuk saat fungsi keluar lebih awal lewat return, dan termasuk",
                    "saat sebuah exception melemparmu keluar dari blok itu (materi",
                    "sebelumnya). Pola ini namanya RAII; materi RAII & Move Semantics",
                    "membahasnya tuntas, dan contoh FileLogger di sana persis benda yang",
                    "sedang kamu pakai sekarang.",
                    "",
                    "Tetap tulis close() eksplisit di SATU keadaan: kalau berkas itu mau",
                    "langsung dibuka lagi di program yang sama. Tulisan ke berkas mampir",
                    "dulu di buffer memori dan baru disiram ke disk saat berkasnya ditutup",
                    "- membaca ulang berkas yang masih terbuka untuk menulis bisa memberimu",
                    "isi yang belum lengkap.",
                ],
            },
            {
                "heading": "Membaca kolom: operator >> dan istringstream",
                "body": [
                    "Berkas data jarang berupa kalimat bebas; biasanya berbentuk KOLOM. Ada",
                    "dua cara membacanya, dan memilih yang salah memotong datamu di tengah:",
                    "",
                    "  masuk >> nama >> nilai   kolom dipisah SPASI, dan tidak boleh ada",
                    "                           kolom yang mengandung spasi (>> berhenti",
                    "                           di spasi pertama).",
                    "  getline + istringstream  baca satu baris utuh dulu, lalu pecah",
                    "                           sendiri. Wajib untuk CSV, atau untuk kolom",
                    "                           yang boleh berisi spasi.",
                    "",
                    "istringstream berasal dari <sstream> dan dibahas di materi String C++",
                    "Lebih Dalam & stringstream: ia membungkus sebuah string biasa supaya",
                    "string itu bisa dibaca seperti stream.",
                ],
                "code": """#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
using namespace std;

int main() {
    // Siapkan dulu berkas datanya supaya contoh ini bisa langsung jalan.
    ofstream siap("nilai.txt");
    siap << "Andi 80\\n";
    siap << "Budi 95\\n";
    siap << "Cici 70\\n";
    siap.close();

    // CARA 1: kolom demi kolom dengan >>. Operator >> MELOMPATI spasi dan
    // newline sendiri, jadi satu loop cukup membaca seluruh berkas.
    ifstream masuk("nilai.txt");
    if (!masuk.is_open()) {
        cout << "nilai.txt tidak ada" << endl;
        return 1;
    }
    string nama;
    int nilai, total = 0, banyak = 0;
    while (masuk >> nama >> nilai) {  // habis/gagal -> kondisi jadi false
        cout << nama << " dapat " << nilai << endl;
        total += nilai;
        banyak++;
    }
    cout << "Rata-rata: " << total / banyak << endl;

    // CARA 2: baca satu BARIS, lalu pecah barisnya sendiri. Wajib kalau
    // pemisahnya bukan spasi (CSV), atau kalau satu kolom boleh berisi
    // spasi - >> akan memotong "Andi Wijaya" jadi dua kolom.
    ofstream siap2("orang.csv");
    siap2 << "Andi Wijaya,Bandung,80\\n";
    siap2 << "Budi Santoso,Surabaya,95\\n";
    siap2.close();

    ifstream csv("orang.csv");
    if (!csv.is_open()) {
        cout << "orang.csv tidak ada" << endl;
        return 1;
    }
    string baris;
    while (getline(csv, baris)) {
        istringstream potong(baris);  // barisnya diperlakukan sebagai stream
        string nm, kota, angka;
        getline(potong, nm, ',');     // argumen KETIGA = karakter pemisahnya
        getline(potong, kota, ',');
        getline(potong, angka);       // tanpa pemisah = sisa barisnya
        cout << nm << " (" << kota << ") nilai " << angka << endl;
    }
    return 0;
}""",
            },
            {
                "body": [
                    "EMPAT JEBAKAN yang benar-benar menjatuhkan orang:",
                    "",
                    "JEBAKAN 1 - while (!masuk.eof()). Jangan pernah menulis ini. eof() baru",
                    "menyala SESUDAH sebuah pembacaan menabrak ujung berkas, jadi loop-nya",
                    "terlanjur masuk sekali lagi dan memproses baris terakhir DUA KALI (yang",
                    "kedua isinya kosong). Tulis while (getline(masuk, baris)): kondisinya",
                    "adalah hasil pembacaan itu sendiri, jadi tidak ada iterasi ekstra.",
                    "",
                    "JEBAKAN 2 - mencampur >> lalu getline. Sama persis dengan jebakan",
                    "cin >> lalu getline(cin, s) di materi Input/Output Modern: >> berhenti",
                    "TEPAT sebelum newline dan meninggalkan newline itu di stream, jadi",
                    "getline berikutnya langsung menemuinya dan mengembalikan string KOSONG.",
                    "Obatnya juga sama: masuk.ignore() dulu sebelum getline.",
                    "",
                    "JEBAKAN 3 - membuka ofstream cuma untuk 'mengecek berkasnya ada atau",
                    "tidak'. Membukanya saja SUDAH mengosongkannya. Untuk memeriksa",
                    "keberadaan sebuah berkas, buka pakai ifstream lalu lihat is_open().",
                    "",
                    "JEBAKAN 4 - lupa bahwa path-nya relatif ke direktori kerja. Program",
                    "yang jalan mulus dari terminalmu bisa gagal total saat dijalankan lewat",
                    "cara lain, walau binernya sama persis.",
                    "",
                    "PERBANDINGAN dengan File I/O gaya C yang sudah kamu pelajari:",
                    "",
                    "  C                              C++",
                    "  FILE *fp = fopen(\"a.txt\",\"r\"); ifstream masuk(\"a.txt\");",
                    "  if (fp == NULL) { ... }        if (!masuk.is_open()) { ... }",
                    "  fgets(buf, sizeof(buf), fp);   getline(masuk, baris);",
                    "  fprintf(fp, \"%d\\n\", n);        keluar << n << '\\n';",
                    "  fclose(fp);                    (otomatis saat objeknya keluar scope)",
                    "",
                    "Yang hilang bukan cuma ketikan. Buffer berukuran tetap - sumber buffer",
                    "overflow klasik - diganti string yang tumbuh sendiri; format specifier",
                    "yang harus cocok dengan tipe diganti operator yang tahu tipenya; dan",
                    "fclose() yang wajib diulang di setiap jalur keluar fungsi diganti",
                    "destructor yang tidak bisa lupa.",
                ],
            },
        ],
    },
    {
        "title": "29. Lambda Expression & Fitur Modern C++",
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
            {
                "heading": "Kosakata C++17 yang muncul di TANDA TANGAN fungsi",
                "body": [
                    "Fitur di atas boleh kamu lewati kalau tidak suka - ia cuma cara",
                    "menulis. Tiga tipe berikut lain urusannya: ia berdiri di tanda",
                    "tangan fungsi, tempat yang tidak bisa dilewati pembaca. Begitu",
                    "kamu membuka kode C++ modern orang lain, ketiganya langsung",
                    "menghadangmu di baris pertama.",
                    "",
                    "optional<T> - 'mungkin ada, mungkin tidak'",
                    "",
                    "  Sebuah fungsi cari() harus bisa menjawab 'tidak ketemu'. Cara",
                    "  lama: kembalikan pointer, lalu nullptr kalau nihil - dan",
                    "  pemanggil yang lupa memeriksanya dapat crash. optional",
                    "  mengatakannya di tanda tangan, terang-terangan:",
                    "",
                    "    optional<Produk> cari(const vector<Produk> &rak, string nama);",
                    "",
                    "  Isinya diperiksa dan diambil begini:",
                    "    if (hasil) { ... }        // atau hasil.has_value()",
                    "    hasil->nama               // seperti pointer",
                    "    hasil.value()             // melempar kalau ternyata kosong",
                    "    hasil.value_or(cadangan)  // nilai cadangan kalau kosong",
                    "",
                    "  Untuk mengembalikan yang kosong, tulis 'return nullopt;'.",
                    "  Bedanya dari pointer: tidak ada memori yang dialokasikan, dan",
                    "  'kosong' di sini berarti WAJAR - bukan error, bukan kegagalan.",
                    "",
                    "string_view - parameter teks yang murah",
                    "",
                    "    void sapa(string_view teks);   // bukan const string&",
                    "",
                    "  string_view cuma menyimpan alamat awal teks dan panjangnya -",
                    "  ia MELIHAT, tidak memiliki dan tidak menyalin. Untungnya:",
                    "  memanggil sapa(\"Andi\") dengan literal tidak lagi diam-diam",
                    "  membuat objek string baru, dan potongan teks bisa dioper",
                    "  tanpa substr yang menyalin.",
                    "",
                    "  PERINGATAN umurnya, dan ini penting: string_view tidak menahan",
                    "  teks yang dilihatnya tetap hidup. Kalau string aslinya keluar",
                    "  scope atau berubah, string_view-nya menunjuk ke tempat yang",
                    "  sudah tidak berlaku - persis seperti dangling pointer. Aman",
                    "  sebagai PARAMETER (teks aslinya jelas masih hidup selama",
                    "  fungsinya jalan); berbahaya sebagai atribut class atau",
                    "  sebagai kembalian.",
                    "",
                    "variant<A, B> sekilas",
                    "",
                    "  Satu variabel yang isinya boleh salah satu dari beberapa tipe,",
                    "  dan ia INGAT sedang berisi yang mana - jadi tidak seperti",
                    "  union gaya C yang bisa kamu baca dengan tipe yang salah.",
                    "  Periksa dengan holds_alternative<T>(v), ambil dengan get<T>(v).",
                    "  Sering muncul sebagai 'hasil ATAU pesan kesalahan'.",
                ],
            },
            {
                "heading": "optional, string_view, variant, lambda mutable & generic lambda",
                "code": """#include <iostream>
#include <optional>
#include <string>
#include <string_view>
#include <variant>
#include <vector>
using namespace std;

struct Produk {
    string nama;
    int harga;
};

// optional<Produk> = "mungkin berisi Produk, mungkin kosong" - tanpa pointer, tanpa null
optional<Produk> cari(const vector<Produk> &rak, string_view nama) {
    for (const auto &p : rak) {
        if (p.nama == nama) return p;
    }
    return nullopt;          // kosong, dan itu WAJAR - bukan error
}

// string_view: parameter yang cuma MEMBACA teks, tanpa menyalinnya
void sapa(string_view teks) {
    cout << "Halo, " << teks << " (" << teks.size() << " huruf)" << endl;
}

int main() {
    vector<Produk> rak = {{"pensil", 2000}, {"buku", 15000}};

    if (auto hasil = cari(rak, "buku")) {        // optional bernilai true kalau berisi
        cout << hasil->nama << " Rp" << hasil.value().harga << endl;
    }
    auto kosong = cari(rak, "tas");
    cout << "has_value: " << kosong.has_value() << endl;    // 0

    optional<int> stok;                             // sengaja dibiarkan kosong
    cout << "Stok: " << stok.value_or(0) << endl;   // 0 <- nilai cadangan kalau kosong

    sapa("Andi");            // literal langsung dipakai, tanpa membuat string baru

    // variant: SATU variabel, beberapa kemungkinan tipe
    variant<int, string> nilai = 90;
    cout << "sedang berisi int? " << holds_alternative<int>(nilai) << endl;   // 1
    nilai = string("belum dinilai");
    cout << get<string>(nilai) << endl;

    // lambda mutable: SALINAN tangkapannya boleh diubah di dalam
    int hitungan = 0;
    auto penghitung = [hitungan]() mutable { return ++hitungan; };
    cout << penghitung() << " " << penghitung() << " ";
    cout << penghitung() << endl;                            // 1 2 3
    cout << "hitungan di luar tetap " << hitungan << endl;   // 0

    // generic lambda: parameternya 'auto', satu lambda untuk banyak tipe
    auto cetak = [](const auto &x) { cout << x << " "; };
    cetak(7); cetak(3.5); cetak("teks");
    cout << endl;                                            // 7 3.5 teks
    return 0;
}"""
            },
            {
                "body": [
                    "Dua bentuk lambda yang belum disebut, dan keduanya muncul di",
                    "contoh barusan:",
                    "",
                    "  mutable - lambda yang boleh mengubah tangkapannya",
                    "    Tangkapan by value ([x]) bersifat const di dalam lambda:",
                    "    'x = 5;' langsung ditolak compiler. Tambahkan 'mutable'",
                    "    SESUDAH daftar parameter dan larangan itu dicabut - tapi",
                    "    yang berubah cuma SALINAN milik lambda-nya. Variabel di",
                    "    luar tetap tidak tersentuh, dan salinan itu bertahan antar",
                    "    pemanggilan. Itulah kenapa penghitung() di atas menghasilkan",
                    "    1, 2, 3 sementara 'hitungan' di luar tetap 0.",
                    "",
                    "  generic lambda - parameter bertipe auto",
                    "    Tulis 'auto' sebagai tipe parameter dan compiler membuatkan",
                    "    versi terpisah untuk tiap tipe yang dipakai - persis seperti",
                    "    template di materi Templates, tapi dalam satu baris.",
                    "",
                    "      auto cetak = [](const auto &x) { cout << x; };",
                    "",
                    "    Berguna untuk lambda pembantu yang kamu pakai pada beberapa",
                    "    jenis container sekaligus, tanpa menulis ulang tiga kali.",
                ]
            },
        ],
    },
    {
        "title": "30. Functor & std::function",
        "sections": [
            {
                "body": [
                    "Sejak materi STL: Algorithm Library kamu mengetik greater<int>()",
                    "untuk mengurutkan menurun, tanpa pernah diberi tahu benda apa itu.",
                    "Jawabannya: itu BUKAN fungsi. Itu sebuah OBJEK.",
                    "",
                    "FUNCTOR (function object) = objek yang bisa DIPANGGIL seperti",
                    "fungsi. Caranya: sebuah class meng-overload operator() - operator",
                    "'panggil' yang di materi Operator Overloading cuma disebut sekilas.",
                    "",
                    "  struct LebihBesar {",
                    "      bool operator()(int a, int b) const { return a > b; }",
                    "  };",
                    "",
                    "  LebihBesar bandingkan;        // MEMBUAT objek",
                    "  bandingkan(3, 1);             // MEMANGGIL objeknya -> true",
                    "",
                    "Baca pelan-pelan bentuk 'operator()(int a, int b)': sepasang ()",
                    "yang pertama adalah NAMA operatornya, sepasang () kedua barulah",
                    "daftar parameter biasa. Itu sebabnya kurungnya terlihat dobel.",
                    "",
                    "Kenapa repot begini kalau fungsi biasa sudah ada? Karena objek",
                    "punya sesuatu yang tidak dimiliki fungsi: ANGGOTA DATA. Functor",
                    "bisa MENYIMPAN nilai di dalam dirinya - ambang batas, penghitung,",
                    "konfigurasi - lalu memakainya lagi tiap kali dipanggil. Fungsi",
                    "biasa hanya punya parameternya; selesai dipanggil, tidak ada yang",
                    "tersisa.",
                ],
            },
            {
                "heading": "Contoh functor: buatan sendiri dan bawaan STL",
                "code": """#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>
#include <functional>   // rumah greater, less, hash, function
using namespace std;

// FUNCTOR: class biasa, yang membuatnya istimewa cuma operator()
struct LebihBesar {
    bool operator()(int a, int b) const {
        return a > b;
    }
};

// Functor yang MENYIMPAN keadaan - fungsi biasa tidak bisa begini
class DiAtasAmbang {
private:
    int ambang;
public:
    DiAtasAmbang(int a) : ambang(a) {}
    bool operator()(int n) const {
        return n > ambang;
    }
};

int main() {
    vector<int> angka = {5, 3, 8, 1, 9, 2};

    // LebihBesar() = MEMBUAT objek; sort lalu memanggilnya berkali-kali
    sort(angka.begin(), angka.end(), LebihBesar());
    for (int n : angka) cout << n << " ";
    cout << endl;                     // 9 8 5 3 2 1

    // greater<int>() bekerja persis sama - functor bawaan <functional>
    sort(angka.begin(), angka.end(), greater<int>());
    for (int n : angka) cout << n << " ";
    cout << endl;                     // 9 8 5 3 2 1

    DiAtasAmbang lebihDari4(4);       // ambang DISIMPAN di dalam objek
    cout << lebihDari4(7) << endl;    // 1 -- objek dipanggil seperti fungsi
    cout << lebihDari4(2) << endl;    // 0
    cout << count_if(angka.begin(), angka.end(), lebihDari4) << endl;  // 3

    // Di sini greater<int> TANPA () -- yang diminta TIPE-nya, bukan objeknya
    priority_queue<int, vector<int>, greater<int>> antrean;
    antrean.push(30); antrean.push(10); antrean.push(20);
    cout << antrean.top() << endl;    // 10 (terkecil dulu, bukan terbesar)

    map<string, int, greater<string>> nilai;
    nilai["andi"] = 80; nilai["budi"] = 90; nilai["citra"] = 70;
    for (const auto &p : nilai) cout << p.first << " ";
    cout << endl;                     // citra budi andi (Z ke A)

    return 0;
}""",
            },
            {
                "body": [
                    "Functor bawaan tinggal di header <functional>. Semuanya class",
                    "TEMPLATE, jadi selalu ada <tipe> di belakang namanya:",
                    "",
                    "  less<int>       -> a < b    (BAWAAN sort, map, set)",
                    "  greater<int>    -> a > b    (dipakai untuk urutan menurun)",
                    "  equal_to<int>   -> a == b",
                    "  plus<int>       -> a + b",
                    "  hash<string>    -> ubah nilai jadi angka; inilah yang dipakai",
                    "                     unordered_map untuk memilih ember",
                    "",
                    "Dua bentuk yang sangat gampang tertukar:",
                    "",
                    "  greater<int>     -> sebuah TIPE (nama classnya)",
                    "  greater<int>()   -> sebuah OBJEK (hasil pembuatan dari class itu)",
                    "",
                    "sort() minta OBJEK pembanding, jadi ada () di belakangnya.",
                    "Container minta TIPE-nya sebagai parameter template, jadi TANPA ():",
                    "",
                    "  sort(v.begin(), v.end(), greater<int>());           // objek",
                    "  map<string, int, greater<string>> m;                // tipe",
                    "  priority_queue<int, vector<int>, greater<int>> pq;  // tipe",
                    "",
                    "Ketinggalan atau kelebihan sepasang kurung di situ menghasilkan",
                    "salah satu pesan error terpanjang di C++. Sejak C++14 tipenya boleh",
                    "dikosongkan - greater<> saja - dan compiler menebak sendiri.",
                    "",
                    "LAMBDA ITU FUNCTOR. Ini bukan kiasan: compiler benar-benar",
                    "membuatkan sebuah class ber-operator() di baliknya, dan variabel",
                    "yang kamu [capture] menjadi ANGGOTA DATA class itu. Dua bentuk ini",
                    "sama persis di mata compiler:",
                    "",
                    "  int batas = 5;                 class Anon {",
                    "  auto cek = [batas](int n) {        int batas;   // hasil capture",
                    "      return n > batas;          public:",
                    "  };                                 Anon(int b) : batas(b) {}",
                    "                                     bool operator()(int n) const {",
                    "                                         return n > batas;",
                    "                                     }",
                    "                                 };",
                    "",
                    "Jadi lambda bukan barang ajaib yang berdiri sendiri - ia cuma cara",
                    "singkat menulis functor. Dan itu juga yang menjelaskan kenapa tiap",
                    "lambda punya tipe yang BERBEDA meski isinya sama: dua class berbeda",
                    "tetap dua tipe berbeda. Karena itu lambda selalu ditampung 'auto'.",
                ],
            },
            {
                "heading": "std::function: menyimpan dan mengoper fungsi",
                "body": [
                    "Sampai sini semua fungsi selalu langsung DIPAKAI di tempat. Tapi",
                    "kode nyata sering perlu MENYIMPAN sebuah fungsi lebih dulu dan",
                    "memanggilnya nanti - saat tombol diklik, saat data selesai dimuat,",
                    "saat perintah tertentu diketik. Untuk itu perlu sebuah TIPE, dan",
                    "'auto' tidak bisa dipakai sebagai tipe anggota class atau parameter.",
                    "",
                    "std::function<void(int)> adalah tipe itu. Bacanya dari dalam ke",
                    "luar: 'apa saja yang bisa dipanggil dengan satu int dan tidak",
                    "mengembalikan apa-apa'. Yang muat ke dalamnya ada tiga macam:",
                    "pointer fungsi biasa, functor, dan lambda.",
                    "",
                    "Contoh di bawah memakainya di tiga posisi sekaligus: sebagai",
                    "variabel, sebagai isi map (tabel handler), dan sebagai parameter",
                    "constructor yang lalu disimpan jadi anggota class - itulah pola",
                    "CALLBACK, dan bentuknya sama di hampir semua API C++.",
                ],
                "code": """#include <iostream>
#include <string>
#include <map>
#include <functional>
using namespace std;

void sapa(int n) {                       // 1. fungsi biasa
    cout << "fungsi  : " << n << endl;
}

struct Cetak {                           // 2. functor
    void operator()(int n) const {
        cout << "functor : " << n << endl;
    }
};

// Class yang MENERIMA fungsi dari luar, lalu memanggilnya saat ada kejadian
class Tombol {
private:
    string nama;
    function<void(int)> saatDiklik;      // fungsi disimpan sebagai ANGGOTA
public:
    Tombol(string nama, function<void(int)> aksi)
        : nama(nama), saatDiklik(aksi) {}

    void klik(int nilai) {
        cout << "[" << nama << "] ";
        if (saatDiklik) saatDiklik(nilai);      // cek kosong dulu!
        else cout << "belum ada aksi" << endl;
    }
};

int main() {
    function<void(int)> f;               // satu tipe, tiga isi berbeda
    f = sapa;        f(1);
    f = Cetak();     f(2);
    f = [](int n) { cout << "lambda  : " << n << endl; };
    f(3);

    // Tabel handler: nama perintah -> apa yang dikerjakan
    map<string, function<void(int)>> perintah;
    perintah["tambah"] = [](int n) { cout << "menambah " << n << endl; };
    perintah["hapus"]  = [](int n) { cout << "menghapus " << n << endl; };

    string masuk = "tambah";
    if (perintah.count(masuk)) perintah[masuk](5);

    // Callback: aksinya ditentukan pemakai class, bukan class-nya sendiri
    Tombol simpan("Simpan", [](int n) {
        cout << "menyimpan " << n << " baris" << endl;
    });
    simpan.klik(3);

    Tombol kosong("Kosong", nullptr);
    kosong.klik(9);

    return 0;
}""",
            },
            {
                "body": [
                    "Jebakan yang sungguh menjebak:",
                    "",
                    "  - Lupa #include <functional>. greater<int>() sering tetap jalan",
                    "    karena ikut terbawa <algorithm> di sebagian compiler, lalu",
                    "    gagal compile di komputer orang lain. Tulis include-nya.",
                    "",
                    "  - Memanggil std::function yang masih KOSONG. Ia melempar",
                    "    exception std::bad_function_call, bukan sekadar diam. Cek",
                    "    dengan 'if (f)' seperti Tombol di atas.",
                    "",
                    "  - Menyimpan lambda ber-[&] ke dalam std::function yang hidup",
                    "    lebih lama dari variabel yang ditangkap. Anggota datanya",
                    "    berupa referensi ke memori yang sudah mati, dan programnya",
                    "    tetap 'jalan' - cuma hasilnya salah, tanpa satu pun error.",
                    "    Untuk callback yang DISIMPAN, tangkap by value ([x] atau [=]).",
                    "",
                    "  - Memakai std::function padahal auto cukup. std::function",
                    "    menyimpan isinya di balik satu lapis tak-langsung, jadi ada",
                    "    biaya kecil tiap panggilan. Untuk lambda yang langsung dioper",
                    "    ke sort/count_if, biarkan auto atau template. Pakai",
                    "    std::function kalau isinya memang harus BISA BERGANTI, atau",
                    "    harus disimpan di anggota class / container.",
                    "",
                    "  - Mengira parameter std::function berarti 'harus lambda'. Yang",
                    "    dicocokkan bentuk PANGGILANNYA, bukan asal-usulnya - nama",
                    "    fungsi biasa pun langsung diterima, seperti 'f = sapa;'.",
                ],
            },
        ],
    },
    {
        "title": "31. RAII & Move Semantics (Lanjutan)",
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
            {
                "heading": "Tanda tangan yang selama ini disembunyikan",
                "body": [
                    "Sampai di sini move semantics selalu diceritakan dari sisi",
                    "PEMAKAI: vector dan string sudah tahu cara memindahkan dirinya.",
                    "Tapi tahu dari mana? Karena seseorang menuliskan dua anggota ini",
                    "di dalamnya - dan bentuknya belum pernah kamu lihat:",
                    "",
                    "  Buffer(Buffer &&lain) noexcept;              // move constructor",
                    "  Buffer& operator=(Buffer &&lain) noexcept;   // move assignment",
                    "",
                    "Tiga bagian yang perlu dibaca pelan:",
                    "",
                    "  &&        rvalue reference: 'objek yang sudah tidak akan",
                    "            dipakai lagi'. Isinya boleh kamu bongkar, karena",
                    "            pemiliknya memang sedang menyerahkannya - entah",
                    "            karena ia objek sementara, entah karena ditandai",
                    "            std::move.",
                    "",
                    "  &lain     Bandingkan dengan copy constructor yang menerima",
                    "            'const Buffer &lain'. Di sini TIDAK ADA const, dan",
                    "            memang tidak boleh ada: seluruh pekerjaan move justru",
                    "            MENGUBAH sumbernya.",
                    "",
                    "  noexcept  Bukan hiasan, dan bukan sekadar kerapian - lihat di",
                    "            bawah, ia yang menentukan apakah vector mau memakai",
                    "            move-mu sama sekali.",
                    "",
                    "Isinya selalu pola yang sama: CURI lalu KOSONGKAN.",
                    "",
                    "  data = lain.data;      // curi pointernya, tidak menyalin isinya",
                    "  lain.data = nullptr;   // kosongkan sumbernya",
                    "",
                    "Baris kedua bukan kerapian, ia WAJIB. Kalau dilewatkan, dua objek",
                    "memegang pointer yang sama dan dua destructor akan menghapus",
                    "memori yang sama - crash, atau lebih buruk lagi: kerusakan diam.",
                    "",
                    "Untuk move assignment ada dua tambahan: buang dulu milik sendiri",
                    "(delete[] data;) sebelum mengambil milik orang, dan periksa",
                    "'if (this != &lain)' supaya 'a = std::move(a)' tidak menghapus",
                    "isinya sendiri lalu menyalin dari puing.",
                    "",
                    "Kenapa noexcept itu menentukan performa",
                    "",
                    "Ingat materi Vector: saat penuh, vector memindahkan seluruh isinya",
                    "ke blok memori yang lebih besar. Vector wajib menjamin bahwa kalau",
                    "pemindahan itu gagal di tengah jalan, isinya tetap utuh. Move yang",
                    "bisa melempar tidak bisa dijamin - kalau ia gagal di elemen ke-50,",
                    "sumbernya sudah terlanjur dibongkar dan tidak ada jalan pulang.",
                    "",
                    "Jadi vector memeriksa: kalau move constructor-mu noexcept, ia",
                    "MEMINDAHKAN. Kalau tidak, ia diam-diam MENYALIN semuanya - aman,",
                    "tapi berkali-kali lipat lebih lambat, tanpa satu pun peringatan.",
                    "Satu kata noexcept yang lupa ditulis benar-benar bisa jadi selisih",
                    "performa yang kamu cari-cari seharian.",
                    "",
                    "Kedua anggota ini juga menerima '= default' dan '= delete' seperti",
                    "copy constructor di materi Copy Constructor, operator= &",
                    "Aturan Tiga:",
                    "",
                    "  Buffer(Buffer&&) = default;   // buatkan versi bawaanmu",
                    "  Buffer(Buffer&&) = delete;    // class ini tidak boleh dipindah",
                ],
            },
            {
                "heading": "Move constructor & move assignment ditulis lengkap",
                "code": """#include <iostream>
#include <utility>
using namespace std;

class Buffer {
private:
    int *data;
    size_t n;
public:
    Buffer(size_t ukuran) : data(new int[ukuran]), n(ukuran) {}
    ~Buffer() { delete[] data; }

    // COPY constructor: siapkan memori BARU, lalu salin isinya satu per satu (mahal)
    Buffer(const Buffer &lain) : data(new int[lain.n]), n(lain.n) {
        cout << "  COPY: menyalin " << n << " elemen" << endl;
        for (size_t i = 0; i < n; i++) data[i] = lain.data[i];
    }

    // MOVE constructor: CURI pointernya, lalu KOSONGKAN sumbernya
    Buffer(Buffer &&lain) noexcept : data(lain.data), n(lain.n) {
        cout << "  MOVE: tanpa menyalin apa pun" << endl;
        lain.data = nullptr;   // WAJIB. Tanpa ini, destructor 'lain' menghapus memori
        lain.n = 0;            // yang sekarang sudah jadi milik kita -> crash.
    }

    // MOVE assignment: sama, tapi buang dulu milik sendiri
    Buffer& operator=(Buffer &&lain) noexcept {
        cout << "  MOVE assignment" << endl;
        if (this != &lain) {              // jaga-jaga dari 'a = std::move(a)'
            delete[] data;
            data = lain.data;
            n = lain.n;
            lain.data = nullptr;
            lain.n = 0;
        }
        return *this;
    }

    Buffer& operator=(const Buffer &) = delete;   // sengaja dilarang di contoh ini
    size_t ukuran() const { return n; }
};

int main() {
    Buffer a(5);
    Buffer b = a;                 // COPY: a masih utuh
    Buffer c = std::move(a);      // MOVE: isi a pindah ke c

    cout << "a=" << a.ukuran() << " b=" << b.ukuran()
         << " c=" << c.ukuran() << endl;          // a=0 b=5 c=5

    Buffer d(2);
    d = std::move(b);
    cout << "b=" << b.ukuran() << " d=" << d.ukuran() << endl;   // b=0 d=5
    return 0;
}"""
            },
            {
                "heading": "Dari Aturan Tiga ke ATURAN LIMA - lalu ke Aturan NOL",
                "body": [
                    "Materi Copy Constructor menutup dengan janji bahwa Aturan Tiga",
                    "berkembang jadi Aturan Lima. Inilah kelimanya, dan sekarang kamu",
                    "sudah tahu kegunaan tiap barisnya:",
                    "",
                    "  1. ~Buffer();                                  destructor",
                    "  2. Buffer(const Buffer&);                       copy constructor",
                    "  3. Buffer& operator=(const Buffer&);            copy assignment",
                    "  4. Buffer(Buffer&&) noexcept;                   move constructor",
                    "  5. Buffer& operator=(Buffer&&) noexcept;        move assignment",
                    "",
                    "ATURAN LIMA: kalau kamu menulis SALAH SATU dari kelimanya, kamu",
                    "hampir pasti perlu memikirkan kelima-limanya. Alasannya sama",
                    "seperti Aturan Tiga - kamu menulisnya karena class itu MEMILIKI",
                    "sesuatu - ditambah satu jebakan baru: menulis destructor atau",
                    "copy constructor sendiri membuat compiler BERHENTI membuatkan",
                    "move constructor untukmu. Kelasmu masih jalan, tapi diam-diam",
                    "kembali menyalin di tempat yang seharusnya memindahkan. Tidak",
                    "ada error, tidak ada peringatan, cuma jadi lambat.",
                    "",
                    "ATURAN NOL (Rule of Zero) - yang sebenarnya kamu incar",
                    "",
                    "Saran penutup materi yang sama - 'pakai vector, string, dan",
                    "smart pointer, biar versi bawaan compiler yang benar' - ternyata",
                    "punya nama, dan sekarang berlaku untuk KELIMA anggota, bukan",
                    "cuma tiga.",
                    "",
                    "Cara terbaik menghadapi Aturan Lima adalah tidak berhadapan",
                    "dengannya sama sekali. Kalau seluruh atribut class-mu berupa",
                    "vector, string, dan smart pointer, kelimanya SUDAH tahu cara",
                    "menyalin, memindahkan, dan menghapus dirinya sendiri. Versi",
                    "bawaan compiler otomatis benar, dan kamu tidak perlu menulis",
                    "satu pun dari lima anggota itu:",
                    "",
                    "  class Mahasiswa {          // nol anggota khusus, dan itu BAGUS",
                    "      string nama;",
                    "      vector<int> nilai;",
                    "      unique_ptr<Berkas> arsip;",
                    "  };",
                    "",
                    "Kelas seperti itu bisa disalin, dipindah, dan dihapus dengan",
                    "benar tanpa satu baris pun kode tambahan. Contoh Buffer di atas",
                    "sengaja memakai 'int *data' MENTAH supaya kelima anggotanya",
                    "kelihatan; di kode sungguhan pilihan pertamamu adalah vector<int>,",
                    "dan seluruh halaman ini jadi tidak perlu.",
                    "",
                    "Kapan Aturan Lima tetap harus kamu tulis sendiri? Saat class-mu",
                    "memegang sesuatu yang belum ada pembungkus RAII-nya: handle sistem",
                    "operasi, koneksi soket, resource pustaka C. Di situlah kamu jadi",
                    "orang yang MEMBUAT pembungkusnya - sekali, lalu semua pemakainya",
                    "kembali menikmati Aturan Nol.",
                ],
            },
        ],
    },
    {
        "title": "32. Multithreading Dasar: thread, mutex & lock_guard",
        "sections": [
            {
                "body": [
                    "Sampai sekarang programmu mengerjakan satu hal pada satu waktu:",
                    "satu baris selesai, baru baris berikutnya jalan. THREAD adalah",
                    "jalur eksekusi KEDUA di dalam satu program yang sama - dua bagian",
                    "kode benar-benar berjalan bersamaan di dua inti prosesor.",
                    "",
                    "Kenapa perlu? C++ dipakai justru karena performanya. Server yang",
                    "melayani ribuan koneksi, game engine yang menggambar sambil",
                    "menghitung fisika, sistem trading - hampir semuanya multithread.",
                    "Prosesor sekarang punya banyak inti, dan program satu thread cuma",
                    "memakai SATU di antaranya berapa pun jumlah intinya.",
                    "",
                    "Membuat thread (butuh #include <thread>):",
                    "",
                    "  void kerja(int n) { ... }",
                    "",
                    "  thread t(kerja, 5);   // thread LANGSUNG jalan; 5 dikirim ke kerja()",
                    "  t.join();             // main BERHENTI di sini sampai t selesai",
                    "",
                    "join() (atau detach()) itu WAJIB sebelum objek thread-nya hancur.",
                    "Kalau lupa, program tidak sekadar salah - ia MATI MENDADAK:",
                    "",
                    "  terminate called without an active exception",
                    "  Aborted (core dumped)",
                    "",
                    "  - t.join()   -> tunggu sampai selesai. Ini yang hampir selalu",
                    "    kamu mau, dan satu-satunya cara aman membaca hasil kerjanya.",
                    "  - t.detach() -> lepaskan, biarkan hidup sendiri. Bahayanya: thread",
                    "    itu bisa menyentuh variabel yang sudah mati saat main selesai",
                    "    duluan. Pakai hanya kalau kamu benar-benar tahu alasannya.",
                    "",
                    "Satu hal yang harus kamu terima sejak awal: URUTAN jalannya thread",
                    "TIDAK bisa ditebak. Program yang sama, dijalankan dua kali, bisa",
                    "mencetak dengan urutan berbeda - dan itu BUKAN bug di kodemu.",
                    "Karena itu semua contoh di sini disusun supaya hasil AKHIRNYA",
                    "tetap pasti, walau jalannya di dalam tidak pernah pasti.",
                ],
            },
            {
                "heading": "Contoh: dua thread, lalu banyak thread dengan lambda",
                "code": """#include <iostream>
#include <thread>
#include <vector>
#include <functional>
using namespace std;

// Tiap thread menulis ke SLOT-nya sendiri, jadi tidak ada yang berebut.
void jumlahkan(int mulai, int sampai, long &hasil) {
    long total = 0;
    for (int i = mulai; i <= sampai; i++) total += i;
    hasil = total;
}

int main() {
    long a = 0, b = 0;

    // Argumen DISALIN masuk ke thread. Karena jumlahkan() menerima
    // referensi, variabel aslinya harus dibungkus ref() dari <functional>.
    thread t1(jumlahkan, 1, 500, ref(a));
    thread t2(jumlahkan, 501, 1000, ref(b));

    cout << "main sudah membuat 2 thread, sekarang menunggu." << endl;
    t1.join();   // tanpa join, hasilnya belum tentu sudah ditulis
    t2.join();

    cout << "Bagian 1 (1..500)    : " << a << endl;
    cout << "Bagian 2 (501..1000) : " << b << endl;
    cout << "Total                : " << (a + b) << endl;

    // Banyak thread sekaligus: vector<thread> + lambda (materi Lambda)
    vector<long> potongan(4, 0);
    vector<thread> pekerja;
    for (int i = 0; i < 4; i++) {
        pekerja.push_back(thread([i, &potongan]() {
            long total = 0;
            for (int n = i * 250 + 1; n <= (i + 1) * 250; n++) total += n;
            potongan[i] = total;   // tiap thread menyentuh indeks BERBEDA
        }));
    }
    for (thread &t : pekerja) t.join();   // join SEMUA dulu, baru baca hasil

    long total = 0;
    for (long p : potongan) total += p;
    cout << "Total dari 4 thread  : " << total << endl;
    return 0;
}""",
            },
            {
                "body": [
                    "Contoh di atas aman karena tiap thread punya tempat sendiri. Yang",
                    "menghancurkan program adalah dua thread menyentuh SATU variabel",
                    "yang sama. Baris sesederhana ini pun tidak aman:",
                    "",
                    "  counter++;   // BACA nilainya -> TAMBAH 1 -> TULIS balik",
                    "",
                    "Itu TIGA langkah, dan thread lain bisa menyela di antaranya. Kalau",
                    "keduanya membaca 40, keduanya menulis 41 - satu penambahan HILANG.",
                    "Inilah DATA RACE: hasilnya meleset, jumlah melesetnya berubah tiap",
                    "kali dijalankan, dan program tetap 'jalan' tanpa satu pun pesan error.",
                    "",
                    "std::mutex (dari <mutex>) adalah gemboknya: hanya SATU thread boleh",
                    "memegangnya, sisanya antre di depan pintu. Tapi jangan mengunci",
                    "manual:",
                    "",
                    "  mu.lock(); ... mu.unlock();   // JANGAN - sekali ada return atau",
                    "                                // exception di tengah, gembok itu",
                    "                                // TIDAK PERNAH terbuka lagi dan",
                    "                                // seluruh program membeku",
                    "",
                    "Pakai lock_guard - ini persis RAII dari materi sebelumnya:",
                    "",
                    "  {",
                    "      lock_guard<mutex> kunci(mu);   // constructor MENGUNCI",
                    "      denganKunci++;",
                    "  }                                  // destructor MEMBUKA di sini",
                    "",
                    "Inilah yang membuat baris lock_guard<mutex> kunci(mu); terlihat aneh",
                    "waktu pertama kali membaca kode orang: sebuah variabel dibuat, lalu",
                    "namanya tidak pernah dipakai lagi. Padahal justru itu intinya - yang",
                    "bekerja adalah constructor dan destructor-nya, bukan nilainya. Karena",
                    "destructor SELALU terpanggil (bahkan saat exception), gembok itu",
                    "mustahil lupa dibuka.",
                    "",
                    "Khusus penghitung sederhana ada jalan yang lebih ringan: std::atomic",
                    "(dari <atomic>). atomic<int> x; lalu x++ dijamin utuh satu langkah",
                    "di tingkat prosesor - tidak ada celah untuk disela, tanpa mutex sama",
                    "sekali. Pakai atomic kalau yang dijaga cuma SATU variabel; pakai",
                    "mutex kalau ada beberapa variabel yang harus berubah bersama-sama.",
                    "",
                    "Contoh berikut sengaja MEMELANKAN tiga langkah tadi - menuliskannya",
                    "satu per satu dan menyelipkan this_thread::yield() di tengah - supaya",
                    "celahnya terlihat SETIAP kali dijalankan. Dengan counter++ polos,",
                    "di mesin cepat hasilnya kadang kebetulan pas, dan itulah sifat paling",
                    "berbahaya dari data race: ia sering LOLOS pengujian, lalu meledak",
                    "di komputer atau beban yang berbeda.",
                ],
            },
            {
                "heading": "Contoh: data race, lalu diperbaiki dengan mutex & atomic",
                "code": """#include <iostream>
#include <thread>
#include <mutex>
#include <atomic>
using namespace std;

const int PUTARAN = 20000;

int tanpaKunci = 0;            // BAHAYA: dua thread menyentuhnya bersamaan
int denganKunci = 0;           // dilindungi mutex di bawah
mutex mu;                      // gembok milik denganKunci
atomic<int> pakaiAtomic(0);    // aman tanpa mutex sama sekali

// Ini "tanpaKunci++" yang dipelankan, supaya celahnya kelihatan tiap kali.
void naikTanpaKunci() {
    for (int i = 0; i < PUTARAN; i++) {
        int sementara = tanpaKunci;      // 1. BACA
        this_thread::yield();            // celah: thread lain boleh menyela
        tanpaKunci = sementara + 1;      // 2. TAMBAH lalu 3. TULIS balik
    }
}

void naikDenganMutex() {
    for (int i = 0; i < PUTARAN; i++) {
        lock_guard<mutex> kunci(mu);     // constructor: MENGUNCI
        int sementara = denganKunci;
        this_thread::yield();            // celah yang sama - tapi kini tak ada
        denganKunci = sementara + 1;     // yang bisa masuk untuk memanfaatkannya
    }                                    // destructor: OTOMATIS MEMBUKA
}

void naikAtomic() {
    for (int i = 0; i < PUTARAN; i++) {
        pakaiAtomic++;                   // satu langkah utuh, tak ada celah
    }
}

int main() {
    int seharusnya = 2 * PUTARAN;

    thread a1(naikTanpaKunci), a2(naikTanpaKunci);
    a1.join();
    a2.join();

    thread b1(naikDenganMutex), b2(naikDenganMutex);
    b1.join();
    b2.join();

    thread c1(naikAtomic), c2(naikAtomic);
    c1.join();
    c2.join();

    cout << "Seharusnya  : " << seharusnya << endl;
    cout << "tanpaKunci  : " << tanpaKunci
         << "   <- hilang " << (seharusnya - tanpaKunci) << endl;
    cout << "denganKunci : " << denganKunci << endl;
    cout << "pakaiAtomic : " << pakaiAtomic << endl;
    return 0;
}""",
            },
            {
                "body": [
                    "Jalankan contoh itu beberapa kali. denganKunci dan pakaiAtomic",
                    "SELALU tepat 40000. tanpaKunci berakhir di sekitar 20000 - hampir",
                    "SEPARUH penambahan lenyap, dan angka persisnya berbeda tiap kali.",
                    "Itulah wujud asli data race: bukan crash, bukan pesan error, cuma",
                    "angka yang diam-diam salah.",
                    "",
                    "Jebakan yang benar-benar menjebak:",
                    "",
                    "  - Lupa mengunci di SATU tempat saja sudah cukup merusak. Gembok",
                    "    hanya bekerja kalau SEMUA yang menyentuh data itu memakainya.",
                    "  - DEADLOCK: thread A memegang mu1 lalu minta mu2, thread B",
                    "    memegang mu2 lalu minta mu1. Keduanya menunggu selamanya dan",
                    "    program membeku tanpa pesan apa pun - tidak ada yang crash,",
                    "    tidak ada yang bisa di-debug dari keluarannya. Obatnya: kunci",
                    "    selalu dengan URUTAN yang sama di seluruh program, atau pakai",
                    "    scoped_lock (C++17) yang mengambil beberapa mutex sekaligus",
                    "    dengan aman:  scoped_lock kunci(mu1, mu2);",
                    "  - Mengunci terlalu lebar. Kalau seluruh isi fungsi dikunci, thread",
                    "    lain cuma antre dan programmu jadi LEBIH LAMBAT dari versi satu",
                    "    thread. Kunci sesempit mungkin. (Karena itu juga, yield() di",
                    "    dalam lock_guard tadi murni alat peraga - jangan pernah menahan",
                    "    kunci sambil menunggu apa pun di kode sungguhan.)",
                    "  - cout dari banyak thread bisa saling menyisip di tengah baris.",
                    "    Untuk keluaran rapi: simpan hasil per slot, cetak setelah semua",
                    "    join() - persis seperti contoh pertama.",
                    "  - Lupa ref() saat mengirim variabel yang harus diubah. Pesannya",
                    "    puluhan baris template dan berbunyi: 'static assertion failed:",
                    "    std::thread arguments must be invocable after conversion to",
                    "    rvalues'. Artinya cuma satu: bungkus argumennya dengan ref(x).",
                    "",
                    "unique_lock<mutex> adalah saudara lock_guard yang lebih luwes: bisa",
                    "dibuka dan dikunci ulang di tengah jalan, dan wajib dipakai bersama",
                    "condition_variable (cara thread saling menunggu - topik lanjutan).",
                    "Ongkosnya sedikit lebih mahal, jadi pilih lock_guard selama kamu",
                    "cuma perlu mengunci satu blok dari awal sampai akhir.",
                    "",
                    "Kompilasi: program berthread perlu library thread milik sistem.",
                    "",
                    "  g++ -std=c++17 -pthread program.cpp -o program",
                    "",
                    "Di Linux baru g++ tanpa -pthread sering tetap berhasil - makanya",
                    "contoh di halaman ini bisa langsung dijalankan - tapi biasakan",
                    "menuliskannya: di mesin lain ketiadaannya memunculkan error linker",
                    "yang membingungkan seperti 'undefined reference to pthread_create'.",
                    "Di CMake, jangan tulis -pthread manual, minta CMake yang mencarinya:",
                    "",
                    "  find_package(Threads REQUIRED)",
                    "  target_link_libraries(program PRIVATE Threads::Threads)",
                    "",
                    "Terakhir, thread::hardware_concurrency() memberi tahu berapa thread",
                    "yang masuk akal dibuat di mesin itu. Membuat 500 thread di mesin 8",
                    "inti tidak membuat apa pun lebih cepat - yang bertambah cuma ongkos",
                    "bergantian antar-thread.",
                ],
            },
        ],
    },
    {
        "title": "33. Roadmap Menjadi C++ Programmer Handal",
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
                "heading": "Sebelum membuka repo orang: konvensi penamaan C++",
                "body": [
                    "Satu jeda sebentar dari daftar TAHAP - TAHAP 4 menyusul lagi",
                    "sesudah bagian ini, dan bagian ini justru bekalnya.",
                    "",
                    "Seluruh contoh di kurikulum ini memakai camelCase berbahasa",
                    "Indonesia - totalHarga, getSaldo, jumlahItem - supaya kamu bisa",
                    "berkonsentrasi pada konsepnya. Repo C++ di GitHub terlihat SANGAT",
                    "berbeda, dan bedanya itu bukan gaya perorangan melainkan konvensi",
                    "yang sudah lama mapan. Kenali sekarang, supaya nanti tidak ada",
                    "yang kamu kira kata kunci istimewa padahal cuma nama biasa.",
                    "",
                    "  pustaka standar & Boost   snake_case, huruf kecil semua:",
                    "                            push_back, make_shared, value_type,",
                    "                            find_if. Kalau namanya bergaya begini,",
                    "                            biasanya ia meniru STL dengan sengaja.",
                    "",
                    "  class & struct            PascalCase: KeranjangBelanja, HttpClient.",
                    "                            Ini yang paling seragam di mana-mana.",
                    "",
                    "  atribut anggota           berawalan m_ (m_jumlahItem) atau",
                    "                            berakhiran garis bawah (jumlah_item_).",
                    "                            Tandanya cuma untuk membedakan atribut",
                    "                            dari variabel lokal saat membaca method",
                    "                            yang panjang - TIDAK ada artinya bagi",
                    "                            compiler. Ini yang paling sering",
                    "                            disangka sintaks rahasia.",
                    "",
                    "  makro                     SELALU HURUF_BESAR_BERGARIS: MAKS_KONEKSI.",
                    "                            Sengaja mencolok, karena makro bekerja",
                    "                            dengan menimpa teks dan bisa mengejutkan.",
                    "",
                    "  konstanta                 kadang berawalan k: kMaksUkuran (gaya",
                    "                            Google). Di tempat lain HURUF_BESAR saja.",
                    "",
                    "Satu proyek biasanya memilih SATU gaya lalu memakainya di semua",
                    "berkas. Saat kamu ikut menyumbang kode ke repo orang, tiru gaya",
                    "yang sudah ada di sana - konsisten jauh lebih berharga daripada",
                    "benar menurut selera sendiri.",
                ],
            },
            {
                "heading": "Potongan berkonvensi 'gaya luar'",
                "code": """#include <iostream>
#include <string>
#include <vector>

#define MAKS_KONEKSI 100                 // makro: SELALU HURUF_BESAR_BERGARIS

namespace toko_online {                  // namespace: snake_case

const int kMaksItem = 50;                // konstanta: berawalan k (gaya Google)

class KeranjangBelanja {                 // class: PascalCase
public:
    void tambah_item(const std::string &nama) {   // method: snake_case (gaya STL/Boost)
        if (jumlah_item_ < kMaksItem) {
            items_.push_back(nama);
            ++jumlah_item_;
        }
    }
    int total_item() const { return jumlah_item_; }

private:
    std::vector<std::string> items_;     // atribut: berakhiran garis bawah
    int jumlah_item_ = 0;                // gaya lain: berawalan m_ -> int m_jumlahItem;
};

}  // namespace toko_online

int main() {
    toko_online::KeranjangBelanja keranjang;   // perhatikan: tanpa 'using namespace std;'
    keranjang.tambah_item("pensil");
    keranjang.tambah_item("buku");
    std::cout << keranjang.total_item() << " item (batas koneksi "
              << MAKS_KONEKSI << ")" << std::endl;
    return 0;
}"""
            },
            {
                "body": [
                    "TAHAP 4 - Kebiasaan Profesional:",
                    "  1. SELALU pakai smart pointer, HINDARI new/delete manual.",
                    "  2. Kompilasi dengan -Wall -Wextra, aktifkan juga -Wshadow",
                    "     dan -Wconversion untuk menangkap bug lebih banyak.",
                    "     -Wall inilah yang memunculkan peringatan signed/unsigned",
                    "     pada perbandingan size_t di materi Konversi Tipe. Jangan",
                    "     dimatikan - peringatan itu menunjuk bug sungguhan.",
                    "  3. Gunakan CMake untuk build system project besar (standar",
                    "     industri, menggantikan Makefile manual). CMakeLists.txt",
                    "     terkecil yang sudah cukup ada di materi Memecah Class ke",
                    "     Header - mulai dari yang itu, jangan menyalin berkas CMake",
                    "     raksasa punya orang yang belum kamu mengerti isinya.",
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
