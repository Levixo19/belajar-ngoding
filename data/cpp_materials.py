CPP_MATERIALS = [
    {
        "title": "1. Pengenalan C++ & Perbedaan dari C",
        "sections": [
            {
                "body": [
                    "C++ itu bahasa C yang ditambahi kemampuan baru. Pembuatnya Bjarne",
                    "Stroustrup, antara tahun 1979 dan 1985. Awalnya namanya 'C with",
                    "Classes', artinya C yang ditambah class. Tambahan utamanya OOP",
                    "(Object-Oriented Programming), yaitu cara menyusun program dari",
                    "benda-benda yang punya data dan perilaku sendiri.",
                    "",
                    "Gampangnya, C++ itu superset dari C. Hampir semua kode C juga sah di",
                    "C++, dengan sedikit pengecualian. Jadi yang udah kamu pelajari di C",
                    "nggak hilang, cuma ditambah.",
                    "",
                    "C++ dipakai di tempat yang butuh program cepat:",
                    "  - Game engine, misalnya Unreal Engine.",
                    "  - Aplikasi yang butuh performa tinggi, termasuk sistem trading.",
                    "  - Browser, misalnya Chrome dan Firefox.",
                    "  - Database engine. MySQL dan MongoDB ditulis dalam C++.",
                    "",
                    "Kenapa belajar C++ sesudah C?",
                    "  - Kamu dapat OOP (class, inheritance, polymorphism) di atas dasar C",
                    "    yang udah kamu kuasai.",
                    "  - Ada STL (Standard Template Library), kumpulan struktur data siap",
                    "    pakai seperti vector dan map. Kamu nggak perlu lagi bikin linked",
                    "    list sendiri kayak di C.",
                    "  - Ada smart pointer, yang membantu mengurangi bug memory leak, yaitu",
                    "    memori yang lupa dikembalikan.",
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
                    "Cara kompilasi dan menjalankannya:",
                    "  g++ hello.cpp -o hello    (kompilasi jadi executable)",
                    "  ./hello                    (jalankan hasilnya)",
                    "",
                    "Ada satu kebiasaan kecil yang bisa menghemat banyak kebingungan. Mulai",
                    "sekarang, pakai perintah yang lebih lengkap ini:",
                    "",
                    "  g++ -std=c++17 -Wall hello.cpp -o hello",
                    "",
                    "  -std=c++17  memberi tahu compiler VERSI C++ mana yang dipakai.",
                    "  -Wall       menyalakan peringatan; baca peringatannya juga,",
                    "              jangan cuma error-nya.",
                    "",
                    "Kenapa versinya perlu disebut? C++ diperbarui berkala, dan tiap versi",
                    "dinamai sesuai tahunnya:",
                    "  - C++11, perubahan besar: auto, range-based for, smart pointer, dan",
                    "    lambda.",
                    "  - C++14 dan C++17: make_unique dan structured bindings.",
                    "  - Lalu C++20.",
                    "",
                    "Hampir semua fitur di kurikulum ini butuh C++11 ke atas.",
                    "",
                    "Masalahnya, sebagian compiler masih pakai standar lama kalau nggak",
                    "dikasih tahu. Pesan error-nya juga nggak nyebut soal versi sama",
                    "sekali. Yang muncul cuma 'make_unique is not a member of std', atau",
                    "keluhan soal tanda kurung yang bikin bingung. Kalau dari sekarang kamu",
                    "selalu nulis -std=c++17, semua contoh di materi berikutnya jalan apa",
                    "adanya.",
                    "",
                    "Ini perbedaan utama C++ dari C yang udah kamu pelajari:",
                    "  1. #include <iostream> menggantikan <stdio.h> untuk input dan",
                    "     output.",
                    "  2. cout << ... dan cin >> ... menggantikan printf dan scanf.",
                    "  3. using namespace std; dipakai supaya kamu nggak perlu nulis std::",
                    "     berulang-ulang.",
                    "  4. bool, true, dan false udah jadi tipe bawaan. Nggak perlu",
                    "     #include <stdbool.h> kayak di C.",
                    "  5. Komentar tetap pakai // dan /* */, sama seperti C.",
                    "  6. printf dan scanf masih bisa dipakai kalau perlu. Kode C lama bisa",
                    "     langsung dikompilasi sebagai C++.",
                    "  7. Header C dipakai lewat nama berawalan c, tanpa .h:",
                    "     <math.h> jadi <cmath>, <stdlib.h> jadi <cstdlib>, <string.h> jadi",
                    "     <cstring>, dan <time.h> jadi <ctime>. Isinya sama persis. Bedanya,",
                    "     versi C++ menaruh isinya di namespace std. Jadi sqrt(), pow(),",
                    "     abs(), rand(), dan semua isi math.h yang kamu pakai di C tetap",
                    "     ada. Tulis #include <cmath>, lalu panggil seperti biasa.",
                    "",
                    "Bentuk lama (<math.h>) masih diterima compiler, jadi nggak ada error",
                    "yang ngasih tahu kalau kamu memakainya. Tetap pakai bentuk baru supaya",
                    "seragam dengan sisa kode C++-mu.",
                ]
            },
        ],
    },
    {
        "title": "2. Variabel, Tipe Data & Namespace",
        "sections": [
            {
                "body": [
                    "Tipe data dasar C++ sama persis dengan C: int, float, double, dan",
                    "char. Bedanya cuma satu. Di C++, bool udah jadi tipe bawaan, jadi",
                    "nggak perlu ambil dari stdbool.h kayak di C.",
                    "",
                    "  int umur = 20;",
                    "  double harga = 15000.50;",
                    "  char grade = 'A';",
                    "  bool lulus = true;         // bawaan C++, tanpa header tambahan",
                    "  string nama = \"Andi\";      // butuh #include <string>",
                    "",
                    "string (huruf kecil semua) itu sebuah class dari pustaka standar C++,",
                    "yang biasa disebut juga bagian dari STL. Dia beda dengan string di C",
                    "yang cuma char array. Pakainya jauh lebih gampang: dua string bisa",
                    "digabung pakai +, dan dibandingkan pakai ==.",
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
                    "Namespace itu cara mengelompokkan nama, misalnya nama fungsi, class,",
                    "atau variabel. Gunanya supaya nama dari library yang berbeda nggak",
                    "bentrok satu sama lain.",
                    "",
                    "  using namespace std;   // pakai SEMUA nama dari namespace std",
                    "  std::cout << \"Halo\";    // ATAU akses langsung dengan std::",
                    "",
                    "Di project besar, orang biasanya nggak nulis 'using namespace std;'",
                    "untuk seluruh berkas, karena bisa bikin nama bentrok. Mereka nulis",
                    "lengkap: std::cout, std::string, dan seterusnya. Untuk belajar, 'using",
                    "namespace std;' tetap umum dipakai supaya kodenya lebih ringkas dibaca.",
                    "",
                    "auto (mulai C++11) menyuruh compiler menebak sendiri tipe datanya dari",
                    "nilai yang kamu kasih:",
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
                    "Di materi sebelumnya kamu cuma memakai namespace punya orang lain,",
                    "yaitu std. Sekarang kamu bikin sendiri. Bentuk ini bakal sering kamu",
                    "temui di kode C++ sungguhan.",
                    "",
                    "Kenapa namespace perlu ada?",
                    "  - Program besar biasanya memakai banyak pustaka. Dua di antaranya",
                    "    bisa sama-sama punya fungsi bernama hitung(), atau class bernama",
                    "    Timer.",
                    "  - Di C, tabrakan nama begitu bikin program gagal dibangun. Linker,",
                    "    yaitu alat yang menyatukan semua bagian program, ketemu dua simbol",
                    "    bernama sama lalu berhenti dengan pesan 'multiple definition'.",
                    "    Orang C mengakalinya dengan nempelin awalan buatan sendiri di",
                    "    depan nama: SDL_Init(), gtk_widget_show(), sqlite3_open().",
                    "  - C++ punya cara resmi. Kamu bungkus nama-namanya dalam sebuah",
                    "    namespace, lalu sebut lengkap waktu memakainya. Awalannya jadi",
                    "    bagian dari bahasa, nggak cuma kebiasaan.",
                    "",
                    "Bikin namespace itu gampang: buka blok, isi, lalu tutup.",
                    "",
                    "  namespace toko {",
                    "      double pajak = 0.11;",
                    "      double hitungTotal(double harga) { ... }",
                    "  }        <- TANPA titik koma (beda dari class yang wajib ditutup '};')",
                    "",
                    "Dari luar, isinya dipanggil pakai operator :: (scope resolution",
                    "operator):",
                    "",
                    "  toko::pajak              // variabel pajak yang ada DI DALAM toko",
                    "  toko::hitungTotal(9000)  // fungsinya",
                    "",
                    "Baca :: sebagai 'yang ada di dalam'. Jadi std::cout artinya 'cout yang",
                    "ada di dalam std'. Operator :: ini berlaku untuk namespace apa pun,",
                    "termasuk yang kamu bikin sendiri, nggak khusus untuk std.",
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
                    "Yang perlu kamu tangkap dari contoh itu:",
                    "  - toko::pajak dan gudang::pajak itu dua variabel yang berbeda.",
                    "    Namanya kebetulan sama, tapi tempatnya beda.",
                    "  - Di dalam namespace-nya sendiri, isinya cukup dipanggil tanpa",
                    "    awalan. Makanya hitungTotal() cukup nulis 'pajak', nggak perlu",
                    "    'toko::pajak'.",
                    "  - Awalan baru wajib ditulis kalau dipanggil dari luar, termasuk dari",
                    "    main().",
                    "",
                    "Namespace boleh dibuka lagi berkali-kali, bahkan di berkas yang",
                    "berbeda:",
                    "",
                    "  namespace toko { void a(); }  // di berkas pertama",
                    "  namespace toko { void b(); }  // berkas lain: toko yang SAMA, isinya nambah",
                    "",
                    "Dengan cara itu std bisa tersebar di puluhan header (<iostream>,",
                    "<string>, <vector>) tapi tetap satu namespace. Jadi namespace itu",
                    "nggak sama dengan berkas, dan nggak sama dengan class. Dia cuma nama",
                    "yang nempel di depan, dan boleh disambung dari mana aja.",
                    "",
                    "Namespace bersarang, artinya namespace di dalam namespace, punya dua",
                    "cara tulis yang artinya sama persis:",
                    "",
                    "  namespace toko { namespace detail { ... } }   // bentuk klasik, selalu jalan",
                    "  namespace toko::detail { ... }                // bentuk ringkas C++17",
                    "",
                    "Dua-duanya dipanggil sebagai toko::detail::catat(...). Bentuk ringkas",
                    "butuh compiler yang dijalankan minimal dengan C++17:",
                    "g++ -std=c++17 program.cpp -o program.",
                    "",
                    "Ada dua jebakan yang sering kena:",
                    "  - Penutup namespace nggak pakai titik koma, sedangkan class wajib",
                    "    ditutup '};'. Kalau tertukar, pesan error-nya nunjuk baris yang",
                    "    jauh di bawahnya.",
                    "  - Jangan taruh int main() di dalam namespace. Linker nyari main di",
                    "    namespace global, dan app::main nggak dihitung. Pesan error-nya",
                    "    juga nggak nyebut namespace sama sekali, cuma 'undefined reference",
                    "    to main'.",
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
                    "Ada tiga cara memendekkan nama, dan bedanya perlu kamu tahu:",
                    "",
                    "  using namespace std;            // using-DIRECTIVE: SELURUH isi std terlihat",
                    "  using std::cout;                // using-DECLARATION: cuma cout",
                    "  namespace fs = std::filesystem; // ALIAS: nama lain untuk satu namespace",
                    "",
                    "  - using-directive paling ringkas, tapi paling berisiko, karena ribuan",
                    "    nama masuk sekaligus. Misalnya kamu punya fungsi sendiri bernama",
                    "    count(), distance(), atau size(). Fungsi itu bisa bentrok dengan",
                    "    punya std, padahal kamu nggak pernah nulis std.",
                    "  - Kalau ada dua using-directive sekaligus, bentroknya baru ketahuan",
                    "    di tempat nama itu dipakai, bukan di tempat using ditulis. Pesannya",
                    "    'call of tampil() is ambiguous', dan compiler menyebut kedua",
                    "    calonnya.",
                    "  - using-declaration cuma menarik satu nama, jadi kelihatan jelas apa",
                    "    yang kamu pinjam.",
                    "  - Alias dipakai untuk namespace yang panjang atau bersarang, persis",
                    "    seperti fmt di contoh tadi. Alias nggak bikin namespace baru, cuma",
                    "    nama panggilan.",
                    "",
                    "Jangan nulis using namespace di berkas header (.h). Aturan ini yang",
                    "paling sering dilanggar. Isi header disalin ke setiap .cpp yang",
                    "meng-include-nya. Jadi satu baris itu memaksakan seluruh namespace ke",
                    "berkas orang lain yang nggak pernah memintanya. Di dalam .cpp, apalagi",
                    "di dalam satu fungsi, pemakaiannya masih wajar.",
                    "",
                    "namespace { ... } tanpa nama disebut anonymous namespace:",
                    "  - Isinya cuma kelihatan dari berkas tempat dia ditulis. Ini padanan",
                    "    C++ untuk kata 'static' di depan fungsi C. Ini juga cara standar",
                    "    menyembunyikan fungsi bantu yang nggak boleh dipanggil berkas lain.",
                    "  - Makanya nomorBaris dan awalan() di contoh tadi aman. Berkas .cpp",
                    "    lain boleh punya nama yang sama, dan keduanya nggak tabrakan waktu",
                    "    di-link.",
                    "",
                    "Kalau kamu nulis ::nama tanpa apa pun di depannya, artinya 'ambil yang",
                    "ada di namespace global'. Ini berguna kalau nama lokal menutupi nama",
                    "global, seperti ::hitung() di contoh tadi.",
                    "",
                    "Bentuk :: juga dipakai di luar namespace. Nanti kamu ketemu lagi",
                    "sebagai Kelas::metode dan Status::Aktif (enum class) di materi-materi",
                    "berikutnya. Kalau kamu membacanya sebagai 'yang ada di dalam', ketiga",
                    "bentuk itu jadi satu aturan yang sama.",
                    "",
                    "Namespace juga nggak menambah beban waktu program berjalan. Semuanya",
                    "diselesaikan compiler, sebelum program dijalankan.",
                ],
            },
        ],
    },
    {
        "title": "4. enum class, Konstanta & Alias Tipe",
        "sections": [
            {
                "body": [
                    "Sejauh ini semua nilai di contoh disimpan di variabel biasa, yang",
                    "bebas diubah kapan aja. Padahal banyak nilai yang nggak boleh berubah,",
                    "misalnya nilai PI, batas maksimum, atau kode status. Untuk itu ada",
                    "const.",
                    "",
                    "  const double PI = 3.14159;       // boleh ditulis DI LUAR fungsi",
                    "  constexpr int MAKS_SISWA = 100;",
                    "",
                    "const artinya nilainya nggak boleh diubah lagi sesudah diisi nilai",
                    "awal. Kalau kamu nulis PI = 3.14; compiler menolaknya dengan pesan:",
                    "  error: assignment of read-only variable 'PI'",
                    "",
                    "Penolakan itu memang gunanya const. Bayangkan sebuah angka mentah",
                    "ditulis di banyak tempat. Angka seperti ini disebut magic number.",
                    "Suatu hari angkanya diubah, tapi cuma di sebagian tempat. Programnya",
                    "tetap jalan, cuma hasilnya salah, dan bug begini paling capek dicari.",
                    "Kalau angkanya disimpan di satu konstanta bernama, kesalahan itu nggak",
                    "mungkin terjadi.",
                    "",
                    "constexpr (mulai C++11) satu tingkat lebih ketat. Nilainya wajib udah",
                    "bisa dihitung waktu kompilasi, sebelum program jalan. Bedanya kelihatan",
                    "di sini:",
                    "",
                    "  const int a = bacaDariInput();      // BOLEH - diketahui saat jalan",
                    "  constexpr int b = bacaDariInput();  // ERROR - compiler tak sanggup",
                    "",
                    "Gunanya apa? Ada hal-hal yang harus udah pasti sebelum program jalan:",
                    "ukuran array biasa, argumen template, dan isi static_assert. Semuanya",
                    "cuma mau menerima nilai yang udah diketahui waktu kompilasi, dan",
                    "constexpr menjamin itu. Fungsi juga boleh ditandai constexpr, supaya",
                    "hasilnya ikut dihitung compiler.",
                    "",
                    "static_assert itu pasangan dekatnya. Dia satu baris pemeriksaan yang",
                    "dikerjakan compiler. Kalau pemeriksaannya salah, program gagal",
                    "dikompilasi. Jadi bug-nya ketahuan sebelum programnya sampai ke tangan",
                    "pemakai.",
                    "",
                    "Pegangan praktisnya: pakai const dulu. Naikkan ke constexpr kalau",
                    "nilainya memang udah tetap dari awal.",
                    "",
                    "Kata const nanti muncul lagi dengan dua peran lain: 'const string",
                    "&teks' sebagai parameter, dan 'int getSaldo() const' di akhir method.",
                    "Dua-duanya dibahas di materinya sendiri. Artinya selalu sama: ada",
                    "sesuatu yang dijamin nggak berubah.",
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
                    "Di kursus C kamu udah ketemu enum, yaitu cara ngasih nama ke",
                    "sekumpulan angka supaya kodenya gampang dibaca. Kamu bisa nulis 'if",
                    "(hari == RABU)', nggak perlu 'if (hari == 2)'. C++ mewarisi enum itu",
                    "apa adanya, jadi bentuk lama ini tetap sah:",
                    "",
                    "  enum Warna { MERAH, HIJAU, BIRU };   // otomatis 0, 1, 2",
                    "  Warna w = MERAH;",
                    "",
                    "Masalahnya, enum biasa ini bocor ke dua arah, dan dua-duanya sering",
                    "bikin bug:",
                    "",
                    "  1. Nilainya otomatis berubah jadi int tanpa pemberitahuan. 'if (w ==",
                    "     0)' lolos dikompilasi, begitu juga 'int x = w + 5;'. Padahal",
                    "     \"warna ditambah 5\" nggak ada artinya, dan compiler nggak protes",
                    "     sama sekali.",
                    "  2. Nama anggotanya tumpah keluar dari enum-nya. Kalau kamu menambah",
                    "     'enum Lampu { MERAH, KUNING };' di berkas yang sama, hasilnya",
                    "     gagal:",
                    "       error: 'MERAH' conflicts with a previous declaration",
                    "",
                    "C++11 menambahkan versi yang menutup dua kebocoran itu, yaitu enum",
                    "class. Nama resminya 'scoped enum':",
                    "",
                    "  enum class Status { Aktif, Nonaktif, Diblokir };",
                    "  Status s = Status::Aktif;",
                    "",
                    "Ada tiga hal yang biasanya bikin bingung waktu pertama kali ketemu.",
                    "Kita jawab satu per satu:",
                    "",
                    "  1. Kenapa ada kata 'class', padahal ini bukan class?",
                    "     Kata itu cuma dipinjam. Status nggak jadi punya method,",
                    "     constructor, atau private. Yang dipinjam cuma sifatnya: nama",
                    "     anggotanya terkurung di dalam Status, sama seperti anggota class",
                    "     terkurung di dalam class-nya.",
                    "",
                    "  2. Kenapa harus nulis Status::Aktif, nggak cukup Aktif?",
                    "     Justru itu intinya: Aktif memang nggak ada di luar Status.",
                    "     Tulisannya jadi lebih panjang, tapi kebocoran nomor 2 tadi",
                    "     tertutup. Enum lain di berkas yang sama jadi boleh punya Aktif",
                    "     juga.",
                    "",
                    "  3. Kenapa 'if (s == 0)' nggak bisa dikompilasi?",
                    "       error: no match for 'operator=='",
                    "       (operand types are 'Status' and 'int')",
                    "     Scoped enum nggak diubah otomatis jadi int. Itu kebocoran nomor 1",
                    "     yang sengaja ditutup. Kalau kamu memang butuh angkanya, misalnya",
                    "     mau disimpan ke database, minta terang-terangan:",
                    "     static_cast<int>(s). Karena alasan yang sama, 'cout << s;' juga",
                    "     ditolak. cout nggak tahu Status itu apa. Jadi cetak lewat fungsi",
                    "     yang mengubahnya ke teks, seperti labelnya() di contoh berikut.",
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
                    "Alias tipe itu nama baru untuk tipe yang udah ada. Dia nggak bikin",
                    "tipe baru, cuma nama lain untuk barang yang sama.",
                    "",
                    "  using Daftar = vector<int>;    // bentuk MODERN (C++11+)",
                    "  typedef vector<int> Daftar;    // bentuk LAMA gaya C, sama saja",
                    "",
                    "Bagian ini baca pelan-pelan. Kata 'using' di sini artinya beda total",
                    "dari 'using namespace std;' yang kamu tulis di setiap program.",
                    "'using namespace std;' artinya \"ambil semua nama dari namespace",
                    "std\". 'using Daftar = vector<int>;' artinya \"mulai sekarang, Daftar",
                    "berarti vector<int>\". Katanya sama, tapi pekerjaannya nggak ada",
                    "hubungannya. Bedanya cuma kelihatan dari bentuk barisnya:",
                    "",
                    "  using namespace X;   -> ada 'namespace', TIDAK ada tanda '='",
                    "  using A = B;         -> ada tanda '=', TIDAK ada 'namespace'",
                    "",
                    "Kenapa alias muncul di hampir semua header C++ sungguhan? Nama tipe",
                    "di C++ cepat jadi panjang. Coba bayangkan 'vector<pair<string, int>>'",
                    "diulang di lima deklarasi fungsi. Itu jauh lebih susah dibaca daripada",
                    "'BukuNilai'. Terus, kalau suatu hari int-nya harus diganti double,",
                    "kamu cukup mengubah satu baris alias.",
                    "",
                    "Jebakan: alias nggak bikin tipe baru. Daftar dan vector<int> boleh",
                    "saling diisi satu sama lain, dan compiler nggak bakal menghentikanmu",
                    "kalau keduanya tertukar. Kalau kamu butuh tipe yang betul-betul beda",
                    "dan dijaga compiler, yang kamu perlukan itu class, bukan alias.",
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
                    "cout (console output) dan cin (console input) adalah cara standar C++",
                    "untuk input dan output. Keduanya menggantikan printf dan scanf dari C.",
                    "",
                    "  cout << nilai;           -> mencetak nilai (operator <<)",
                    "  cout << a << b << c;     -> bisa dirangkai (chaining)",
                    "  cin >> variabel;         -> membaca input (operator >>)",
                    "  endl                     -> baris baru (mirip \\n, plus flush buffer)",
                    "",
                    "Kelebihan cout dibanding printf: kamu nggak perlu format specifier",
                    "seperti %d atau %s. Compiler udah tahu tipe datanya dari operator <<.",
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
                    "Untuk mengatur tampilan angka, pakai alat dari <iomanip>:",
                    "  #include <iomanip>",
                    "  cout << fixed << setprecision(2) << 3.14159;  // 3.14",
                    "  cout << setw(10) << nilai;    // lebar minimal 10 karakter",
                    "",
                    "Kalau dibandingkan:",
                    "  - printf/scanf sedikit lebih cepat, tapi butuh format specifier yang",
                    "    harus persis cocok dengan tipe datanya.",
                    "  - cout/cin otomatis aman soal tipe (type-safe), lebih gampang dibaca,",
                    "    dan lebih bergaya C++. Kekurangannya, sedikit lebih lambat.",
                    "  - Dua-duanya boleh dipakai bareng dalam satu program C++.",
                ]
            },
            {
                "heading": "Tiga aliran keluaran: cout, cerr & clog",
                "body": [
                    "cout ternyata punya dua saudara yang perlu kamu kenal:",
                    "",
                    "  cout  -> keluaran NORMAL program, yaitu HASIL kerjanya.",
                    "  cerr  -> pesan ERROR. Tidak di-buffer, jadi langsung muncul.",
                    "  clog  -> pesan log/diagnostik. Seperti cerr tapi di-buffer.",
                    "",
                    "Buffer itu tempat penampungan sementara. Teks yang di-buffer dikumpulkan",
                    "dulu, baru ditampilkan belakangan. Ketiganya sama-sama dipakai dengan",
                    "<<, dan ketiganya berasal dari <iostream>.",
                    "",
                    "Kenapa pesan error perlu dipisah dari cout? Di terminal, keluaran",
                    "program sering dialihkan ke berkas atau dikirim ke program lain",
                    "(dipipa):",
                    "",
                    "  ./program > hasil.txt        (simpan keluarannya ke berkas)",
                    "  ./program | sort             (kirim keluarannya ke program lain)",
                    "",
                    "Yang ikut dialihkan cuma cout. Pesan cerr tetap tampil di layar. Kalau",
                    "pesan error ikut dicetak lewat cout, ada dua masalah. Berkas hasilnya",
                    "kecampur kalimat error. Penggunanya juga nggak lihat apa-apa waktu",
                    "programnya gagal. Pegangannya gampang: data ke cout, keluhan ke cerr.",
                ],
            },
            {
                "heading": "Saat pengguna mengetik huruf padahal diminta angka",
                "body": [
                    "Kalau pengguna ngetik huruf padahal yang diminta angka, cin nggak",
                    "melempar exception dan nggak menghentikan program. Dia masuk keadaan",
                    "gagal (fail state). Variabelnya nggak terisi, dan huruf penyebabnya",
                    "tertinggal di antrean masukan.",
                    "",
                    "Ini yang bikin bingung: semua pembacaan cin sesudahnya ikut gagal",
                    "langsung, tanpa nunggu apa pun. Programnya kelihatan seperti",
                    "melompati semua pertanyaan sisanya, lalu selesai.",
                    "",
                    "Cara ngeceknya:",
                    "  if (!cin) { ... }        // cin langsung dipakai sebagai kondisi",
                    "  if (cin.fail()) { ... }  // sama artinya, ditulis lebih eksplisit",
                    "",
                    "Cara memulihkannya butuh dua langkah. Satu langkah aja nggak cukup:",
                    "  cin.clear();   // hapus tanda gagal supaya cin mau membaca lagi",
                    "  cin.ignore(numeric_limits<streamsize>::max(), '\\n');  // buang barisnya",
                    "",
                    "clear() sendirian nggak menolong, karena huruf penyebabnya masih ada",
                    "di antrean dan bakal menggagalkan pembacaan berikutnya. ignore() yang",
                    "membuang isi antrean sampai ganti baris. numeric_limits butuh <limits>.",
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
                    "Ada pola untuk membaca masukan sampai habis. Pola ini dipakai di hampir",
                    "semua program baris perintah:",
                    "",
                    "  int n;",
                    "  while (cin >> n) { ... }              // per angka/kata",
                    "",
                    "  string baris;",
                    "  while (getline(cin, baris)) { ... }   // per baris, spasi ikut",
                    "",
                    "Kok bisa jadi kondisi while? 'cin >> n' mengembalikan cin itu sendiri.",
                    "Di dalam if atau while, cin bernilai true selama dia belum gagal. Jadi",
                    "loop-nya berhenti sendiri kalau masukan habis, atau kalau ada data",
                    "yang tipenya nggak cocok. Kamu nggak perlu tahu jumlah datanya dari",
                    "awal. Sifat \"mengembalikan stream-nya sendiri\" ini juga yang bikin cout",
                    "<< a << b << c bisa dirangkai.",
                    "",
                    "Kalau kamu ngetik masukan lewat keyboard, tanda \"masukan habis\" itu",
                    "Ctrl+D (Linux/macOS), atau Ctrl+Z lalu Enter (Windows). Kalau datanya",
                    "dipipa, misalnya echo \"1 2 3\" | ./program, masukannya habis dengan",
                    "sendirinya.",
                ]
            },
        ],
    },
    {
        "title": "6. String C++ Lebih Dalam & stringstream",
        "sections": [
            {
                "body": [
                    "Di materi Variabel kamu baru kenal tiga kemampuan string: +, ==, dan",
                    ".length(). Itu baru permulaan. Pekerjaan yang paling sering dilakukan",
                    "program adalah mengolah teks: memotong, mencari, menyambung, dan",
                    "mengubah angka jadi teks atau sebaliknya. Jadi fungsi-fungsi string",
                    "lainnya bakal kamu temui di hampir setiap berkas .cpp yang kamu baca.",
                    "",
                    "Yang dipakai sehari-hari:",
                    "  - s.size() dan s.length() sama-sama ngasih jumlah karakter. Dua nama",
                    "    untuk hal yang sama persis. size() lebih sering dipakai supaya",
                    "    seragam dengan vector, map, dan set.",
                    "  - s.empty() bernilai true kalau isinya kosong. Lebih jelas daripada",
                    "    nulis s.size() == 0.",
                    "  - s[i] ngambil karakter ke-i (mulai dari 0), tanpa ngecek batas.",
                    "  - s.at(i) sama, tapi melempar out_of_range kalau i kelewat batas.",
                    "  - s += \"lagi\"; menempel teks di akhir. Lebih hemat daripada",
                    "    s = s + \"lagi\".",
                    "  - s.substr(mulai, jumlah) bikin potongan baru sepanjang 'jumlah'",
                    "    huruf.",
                    "  - s.find(\"cari\") ngasih posisi kemunculan pertama.",
                    "  - s.replace(mulai, n, \"x\") mengganti n huruf mulai dari posisi",
                    "    'mulai' dengan \"x\".",
                    "  - s.erase(mulai) membuang semua huruf mulai dari posisi itu.",
                    "  - a == b dan a < b membandingkan isinya. Tanda < memakai urutan",
                    "    kamus.",
                    "",
                    "Soal string::npos, kenapa namanya aneh?",
                    "",
                    "find() harus bisa menjawab \"nggak ketemu\". Masalahnya, yang dia",
                    "kembalikan itu nomor posisi, dan nol pun udah kepakai untuk posisi",
                    "paling depan. Jadi C++ memilih satu nilai yang nggak mungkin jadi",
                    "posisi sungguhan, yaitu angka bulat terbesar yang muat. Nilai itu",
                    "dikasih nama string::npos ('no position'). Dia cuma penanda, bukan",
                    "angka khusus yang perlu kamu hafal.",
                    "",
                    "Makanya cara baku ngecek hasil find seperti ini. Baris ini termasuk",
                    "yang paling sering muncul di kode C++:",
                    "",
                    "      if (s.find(\"error\") != string::npos) { ... ketemu ... }",
                    "",
                    "Tulis string::npos apa adanya, jangan diganti -1. Nilai kembalian find",
                    "bertipe unsigned (size_t), artinya nggak punya tanda minus. Kalau",
                    "dibandingkan dengan -1, kodenya kelihatan benar padahal keliru.",
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
                    "Membuang spasi di ujung: find_first_not_of dan find_last_not_of",
                    "",
                    "Teks dari pengguna atau dari berkas hampir selalu membawa spasi yang",
                    "nggak diminta. C++ nggak punya .trim() bawaan kayak bahasa lain. Jadi",
                    "orang memakai bentuk di bawah ini, dan bentuk ini bakal sering kamu",
                    "lihat.",
                    "",
                    "  find(x)              -> posisi x yang PERTAMA",
                    "  find_first_not_of(x) -> posisi pertama yang BUKAN x",
                    "  find_last_not_of(x)  -> posisi terakhir yang BUKAN x",
                    "",
                    "Dua fungsi terakhir menerima sekumpulan karakter sekaligus. Tulisan",
                    "\" \\t\\n\" artinya spasi, tab, atau baris baru.",
                    "",
                    "  std::string rapikan(const std::string& s) {",
                    "      const std::string spasi = \" \\t\\n\";",
                    "      std::size_t awal = s.find_first_not_of(spasi);",
                    "      if (awal == std::string::npos) return \"\";   // isinya spasi semua",
                    "      std::size_t akhir = s.find_last_not_of(spasi);",
                    "      return s.substr(awal, akhir - awal + 1);",
                    "  }",
                    "",
                    "Baris npos di situ wajib ada. Kalau isinya spasi semua, nggak ada satu",
                    "pun karakter yang \"bukan spasi\", jadi find_first_not_of mengembalikan",
                    "npos. Kalau npos itu diteruskan ke substr, substr melempar",
                    "std::out_of_range.",
                    "",
                    "Jebakan: npos + 1 hasilnya 0, dan kadang hasil itu kebetulan benar.",
                    "",
                    "Bentuk ini dipakai untuk membuang nol di belakang bilangan:",
                    "",
                    "  std::string angka = \"3.1400\";",
                    "  angka.erase(angka.find_last_not_of('0') + 1);   // -> \"3.14\"",
                    "",
                    "Sekarang bayangkan isinya \"0000\". find_last_not_of('0') nggak",
                    "menemukan apa pun, jadi dia mengembalikan npos. npos itu bilangan",
                    "tanpa tanda yang nilainya paling besar. Kalau ditambah 1, nilainya",
                    "berputar balik ke 0. Akibatnya erase(0) menghapus seluruh string.",
                    "",
                    "Untuk pekerjaan ini hasilnya kebetulan benar, karena \"0000\" memang",
                    "seharusnya nggak menyisakan apa-apa. Tapi jangan mengandalkannya tanpa",
                    "sadar. Kalau hasil yang kamu mau berbeda, cek npos-nya sendiri dulu.",
                    "",
                    "Memeriksa satu karakter: <cctype>",
                    "",
                    "Untuk nanya \"karakter ini angka?\" atau \"ini huruf?\", pustaka <cctype>",
                    "punya beberapa fungsi pendek:",
                    "",
                    "  isdigit(c)  angka 0-9          isalpha(c)  huruf",
                    "  isspace(c)  spasi/tab/newline  isupper(c)  huruf besar",
                    "  toupper(c)  jadikan huruf besar  tolower(c)  jadikan huruf kecil",
                    "",
                    "Jebakan: argumen fungsi-fungsi ini harus unsigned char.",
                    "",
                    "  for (char c : teks)",
                    "      if (isdigit(c)) ...                              // BERISIKO",
                    "      if (isdigit(static_cast<unsigned char>(c))) ...  // BENAR",
                    "",
                    "Fungsi-fungsi ini warisan dari C, dan menerima int, bukan char. Di",
                    "kebanyakan mesin, char itu bertanda (bisa negatif). Jadi huruf beraksen",
                    "seperti 'é' nilainya negatif. Nilai negatif selain EOF bikin",
                    "perilakunya nggak terdefinisi, artinya hasilnya nggak bisa ditebak.",
                    "Untuk teks ASCII biasa, bug ini nggak kelihatan, makanya bisa bertahan",
                    "lama. Cast-nya murah, jadi pasang selalu.",
                    "",
                    "Satu lagi: isdigit mengembalikan int, bukan bool. Nilai apa pun selain",
                    "0 artinya benar. Kalau dipakai di dalam if, dia tetap bekerja seperti",
                    "yang kamu harapkan.",
                    "",
                    "Angka dan teks: dua arah yang perlu kamu hafal",
                    "  - to_string(n) mengubah angka apa pun jadi string. Fungsi ini yang",
                    "    bikin \"NIM \" + to_string(nim) bisa ditulis. Tanpa itu, C++ nggak",
                    "    punya + antara teks dan int.",
                    "  - stoi(s) mengubah string jadi int (string to int).",
                    "  - stod(s) mengubah string jadi double.",
                    "  - stol(s) mengubah string jadi long, untuk angka yang nggak muat di",
                    "    int.",
                    "",
                    "Teks yang isinya angka itu datangnya dari mana? Hampir selalu dari",
                    "luar program: getline(cin, baris), satu baris berkas, atau argumen",
                    "baris perintah. Argumen baris perintah perlu kamu kenali karena",
                    "bentuknya khas:",
                    "",
                    "      int main(int argc, char *argv[])",
                    "",
                    "argc itu jumlah kata yang diketik, dan nama programnya ikut dihitung.",
                    "argv itu daftar kata-katanya, dalam bentuk teks. Jadi ./program 7",
                    "memberi argc == 2 dan argv[1] == \"7\". Isinya string berisi satu huruf",
                    "'7', bukan angka tujuh. stoi(argv[1]) yang mengubahnya jadi angka.",
                    "",
                    "argv[0] selalu berisi nama program yang dijalankan (\"./program\"). Jadi",
                    "argumen yang kamu ketik sendiri mulai dari argv[1]. Makanya contoh mana",
                    "pun membaca argv[1], bukan argv[0].",
                    "",
                    "Hati-hati dengan dua hal:",
                    "  - Cek argc dulu. Kalau orang lupa ngetik argumennya lalu kamu membaca",
                    "    argv[1], programnya crash.",
                    "  - stoi melempar exception (invalid_argument) kalau teksnya sama",
                    "    sekali bukan angka. Tapi kalau teksnya diawali angka, dia berhenti",
                    "    di huruf pertama tanpa protes. stoi(\"12abc\") mengembalikan 12 tanpa",
                    "    keluhan apa pun.",
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
                    "Kenapa perlu stringstream, padahal udah ada to_string dan stoi?",
                    "  - Untuk merakit. Satu ostringstream bisa menampung semua tipe",
                    "    sekaligus (\"NIM \" << 2201 << 87.5) tanpa satu pun to_string. Dia",
                    "    juga ikut aturan tampilan cout, jadi 87.5 tercetak \"87.5\", bukan",
                    "    \"87.500000\" seperti hasil to_string. Tampilannya bisa dirapikan",
                    "    pakai fixed dan setprecision dari <iomanip>, yang udah kamu kenal",
                    "    di materi cin & cout.",
                    "  - Untuk memecah. istringstream mengubah satu baris jadi kolom-kolom",
                    "    dengan tipe masing-masing. Baris CSV, baris berkas, atau satu baris",
                    "    perintah, semuanya dipecah dengan cara yang sama. Pola ini langsung",
                    "    kepakai nanti waktu kamu belajar membaca berkas.",
                    "",
                    ".c_str(): jembatan ke dunia C",
                    "",
                    "Fungsi lama gaya C (printf, fopen, dan banyak library sistem) nggak",
                    "ngerti std::string. Yang mereka minta const char*. .c_str() yang",
                    "menyediakannya:",
                    "",
                    "      printf(\"Halo %s\\n\", nama.c_str());",
                    "",
                    "Pointer hasil .c_str() cuma meminjam isi string-nya. Pointer itu sah",
                    "selama string aslinya masih ada dan belum diubah. Baris di bawah ini",
                    "bug klasik, dan compiler pun nggak protes:",
                    "",
                    "      // string sementaranya langsung mati di akhir baris ini:",
                    "      const char *p = (nama + \" Wijaya\").c_str();",
                    "      cout << p;   // isinya sudah bukan milik siapa-siapa",
                    "",
                    "Simpan dulu ke variabel string, baru panggil .c_str() dari variabel",
                    "itu.",
                    "",
                    "Kesalahan yang paling sering terjadi:",
                    "  1. Di substr(a, b), b itu panjang, bukan posisi akhir. Beda dengan",
                    "     substring di Java dan slicing di Python. substr(0, 7) ngasih 7",
                    "     huruf pertama.",
                    "  2. s[i] nggak ngecek batas. Index yang kelewat bikin perilaku nggak",
                    "     terdefinisi. Kadang hari ini nggak crash, besok crash. Pakai .at(i)",
                    "     kalau index-nya datang dari input.",
                    "  3. find yang nggak ketemu nggak mengembalikan -1, dan juga bukan 0.",
                    "     Selalu bandingkan dengan string::npos.",
                    "  4. Lupa #include <string> atau <sstream>. Kadang programnya tetap bisa",
                    "     dikompilasi karena header lain ikut menariknya, lalu gagal di mesin",
                    "     orang lain. Tulis include-nya sendiri.",
                ],
            },
        ],
    },
    {
        "title": "7. Referensi (&) vs Pointer",
        "sections": [
            {
                "body": [
                    "C++ menambahkan reference (&). Untuk banyak kasus, reference lebih aman",
                    "dan lebih gampang dibaca daripada pointer.",
                    "",
                    "Reference itu alias, artinya nama lain untuk variabel yang udah ada.",
                    "Dia bukan variabel terpisah yang menyimpan alamat, walaupun di",
                    "belakang layar tetap memakai alamat memori.",
                    "",
                    "  int angka = 10;",
                    "  int &ref = angka;    // ref adalah ALIAS dari angka",
                    "  ref = 20;             // ini SAMA DENGAN mengubah angka",
                    "  cout << angka;        // 20! (angka ikut berubah)",
                    "",
                    "Beda pointer dan reference:",
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
                    "Kapan pakai reference, kapan pakai pointer di C++ modern?",
                    "  - Reference dipakai untuk parameter fungsi yang pasti ada nilainya,",
                    "    yang nggak perlu bisa \"kosong\" (null). Ini pilihan yang lebih",
                    "    disarankan karena lebih aman.",
                    "  - Pointer dipakai kalau kamu butuh kemungkinan \"nggak menunjuk apa",
                    "    pun\" (null), atau butuh pindah ke target lain. Pointer juga dipakai",
                    "    untuk dynamic memory allocation, yaitu minta memori waktu program",
                    "    jalan (new/delete, dibahas di materi berikutnya).",
                    "",
                    "const reference dipakai di mana-mana di C++, supaya hemat. Datanya",
                    "nggak disalin, tapi dijamin nggak diubah:",
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
                    "Function overloading artinya kamu boleh bikin beberapa fungsi dengan",
                    "nama yang sama, asal parameternya beda, entah jumlahnya atau tipenya.",
                    "Compiler sendiri yang memilih versi yang cocok, berdasarkan argumen",
                    "yang kamu kirim. C nggak punya fitur ini. Ini fitur khas C++.",
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
                    "  - Compiler membedakan fungsi dari jumlah dan tipe parameternya.",
                    "    Gabungan nama fungsi dan daftar parameternya disebut function",
                    "    signature. Nama parameter dan tipe kembalian nggak ikut dihitung.",
                    "  - Jadi dua fungsi dengan parameter yang sama persis, tapi tipe",
                    "    kembaliannya beda, nggak sah sebagai overload. Compiler",
                    "    menganggapnya ambigu dan ngasih error.",
                    "",
                    "Default parameter, yaitu nilai bawaan kalau argumennya nggak diisi,",
                    "cuma boleh ada di akhir daftar parameter:",
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
                    "class di C++ itu mirip struct di C. Bedanya, class bisa punya method,",
                    "yaitu fungsi yang jadi anggota class, selain data. class juga punya",
                    "pengaturan akses (public, private, protected), yang dibahas di materi",
                    "encapsulation.",
                    "",
                    "  class NamaClass {",
                    "  public:",
                    "      tipeData atribut;",
                    "      tipeKembali method() { ... }",
                    "  };",
                    "",
                    "Di C++, struct dan class bedanya tipis, dan ini beda dengan C:",
                    "  - Anggota struct secara bawaan public.",
                    "  - Anggota class secara bawaan private.",
                    "  - Selain itu, fungsi keduanya sama di C++. Di C, struct nggak bisa",
                    "    punya method.",
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
                    "Objek juga bisa dibuat pakai 'new' (dynamic allocation, mirip malloc):",
                    "  Mahasiswa *ptr = new Mahasiswa();   // alokasi di heap",
                    "  ptr->nama = \"Citra\";                 // akses lewat -> (seperti C)",
                    "  ptr->perkenalan();",
                    "  delete ptr;                          // WAJIB! (pasangan dari 'new')",
                    "",
                    "new dan delete itu versi C++ dari malloc dan free di C. Bedanya, new",
                    "juga otomatis memanggil constructor (dibahas di materi berikutnya),",
                    "dan delete otomatis memanggil destructor. Setiap new wajib punya",
                    "pasangan delete.",
                ]
            },
        ],
    },
    {
        "title": "10. Constructor & Destructor",
        "sections": [
            {
                "body": [
                    "Constructor adalah method khusus yang dipanggil otomatis waktu objek",
                    "dibuat. Biasanya dipakai untuk mengisi nilai awal atribut.",
                    "  - Namanya harus sama persis dengan nama class.",
                    "  - Nggak punya tipe kembali, bahkan nggak pakai void.",
                    "",
                    "Destructor kebalikannya. Dia method khusus yang dipanggil otomatis waktu",
                    "objek dihancurkan. Objek dihancurkan kalau keluar dari scope, yaitu",
                    "wilayah kurung kurawal tempat dia dibuat. Untuk objek hasil new,",
                    "destructor dipanggil waktu kamu menulis delete. Biasanya destructor",
                    "dipakai untuk membereskan resource, misalnya menutup berkas atau",
                    "mengembalikan memori.",
                    "  - Namanya ~NamaClass(), diawali tanda ~.",
                    "  - Nggak punya parameter, dan nggak bisa di-overload.",
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
                    "Satu class boleh punya beberapa constructor. Ini namanya constructor",
                    "overloading, sama seperti function overloading:",
                    "  class Mahasiswa {",
                    "  public:",
                    "      Mahasiswa() { nama = \"Tanpa Nama\"; }        // default constructor",
                    "      Mahasiswa(string n) { nama = n; }            // dengan 1 parameter",
                    "      Mahasiswa(string n, int u) { nama=n; umur=u; } // dengan 2 parameter",
                    "  };",
                    "",
                    "Ada cara yang lebih efisien untuk mengisi atribut, namanya initializer",
                    "list. Tulis daftar atributnya sesudah titik dua, sebelum badan",
                    "constructor:",
                    "  Mahasiswa(string n, int u) : nama(n), umur(u) {",
                    "      // body constructor, atribut SUDAH terisi sebelum masuk sini",
                    "  }",
                    "",
                    "Bedanya, dengan initializer list atribut langsung lahir dengan nilai",
                    "itu. Waktu badan constructor mulai jalan, atributnya udah terisi.",
                ]
            },
        ],
    },
    {
        "title": "11. Encapsulation: private, public, protected",
        "sections": [
            {
                "body": [
                    "Access modifier menentukan siapa yang boleh menyentuh isi class.",
                    "Konsepnya sama dengan di Java:",
                    "  public    -> bisa diakses dari MANA SAJA (luar class).",
                    "  private   -> HANYA bisa diakses di dalam class itu sendiri.",
                    "  protected -> class sendiri + subclass (materi inheritance).",
                    "",
                    "Kalau nggak ditulis apa-apa, isi class otomatis private. Ini beda dari",
                    "struct, yang bawaannya public.",
                    "",
                    "Kebiasaan yang umum dipakai: atribut dibuat private, lalu diakses lewat",
                    "method getter dan setter yang public. Sama seperti di Java. Getter",
                    "adalah method untuk membaca nilai, setter untuk mengubahnya.",
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
                    "Perhatikan kata const di getter tadi: string getPemilik() const.",
                    "  - const di akhir judul method artinya method itu janji nggak akan",
                    "    mengubah atribut objek.",
                    "  - Kalau di dalam method itu ternyata ada kode yang mengubah atribut,",
                    "    compiler langsung kasih error.",
                    "  - Biasakan menandai const di semua getter dan method lain yang cuma",
                    "    membaca data.",
                ]
            },
        ],
    },
    {
        "title": "12. Memecah Class ke Header (.h) & Sumber (.cpp)",
        "sections": [
            {
                "body": [
                    "Sampai sini, semua contoh C++ menulis badan method di dalam kurung",
                    "kurawal class. Itu sengaja, supaya satu contoh muat di satu layar. Tapi",
                    "kode C++ beneran hampir nggak pernah ditulis begitu. Akibatnya, .cpp",
                    "mana pun yang kamu buka di GitHub bakal dimulai dengan bentuk yang",
                    "belum pernah muncul di kurikulum ini.",
                    "",
                    "Bentuk bakunya begini: satu class dipecah jadi dua berkas.",
                    "  rekening.h    -> DEKLARASI: 'class Rekening punya method setor(double)'",
                    "  rekening.cpp  -> DEFINISI:  badan method setor yang sebenarnya",
                    "",
                    "Deklarasi artinya cuma menyebut \"ada method ini, bentuk panggilannya",
                    "begini\". Definisi artinya menulis isi method itu. Gampangnya, header",
                    "itu daftar isi buku: siapa aja yang ada dan cara memanggilnya. Berkas",
                    ".cpp itu isi babnya: cara kerjanya.",
                    "",
                    "Kenapa harus dipisah?",
                    "  - Orang yang mau memakai class cukup baca header yang pendek. Dia",
                    "    nggak perlu ikut membaca ratusan baris isi method.",
                    "  - Kalau kamu mengubah isi satu method, yang dikompilasi ulang cuma",
                    "    satu .cpp, nggak seluruh project.",
                    "  - Header itu semacam kontrak yang dipegang berkas lain. Selama header",
                    "    nggak berubah, isi .cpp boleh kamu tulis ulang total tanpa",
                    "    mengganggu siapa pun.",
                    "",
                    "Baris ini yang paling sering bikin bingung waktu pertama kali dibaca:",
                    "",
                    "  void Rekening::setor(double jumlah) { ... }",
                    "",
                    "Bacanya pelan-pelan dari kiri:",
                    "  void        -> method ini tidak mengembalikan apa-apa",
                    "  Rekening::  -> method MILIK class Rekening, bukan fungsi bebas yang",
                    "                 kebetulan bernama setor",
                    "  setor       -> nama methodnya",
                    "",
                    "Tanda :: itu operator yang sama persis dengan yang ada di std::cout",
                    "(materi Variabel, Tipe Data & Namespace). Artinya \"ambil nama yang ada",
                    "di dalam\". Jadi std::cout itu cout milik namespace std, dan",
                    "Rekening::setor itu setor milik Rekening.",
                    "",
                    "Jebakan: kalau kamu lupa menulis Rekening::, compiler menganggapnya",
                    "fungsi bebas. Lalu dia protes 'saldo was not declared in this scope',",
                    "karena fungsi bebas memang nggak punya saldo. Error-nya nunjuk ke baris",
                    "saldo, padahal yang salah ada di baris judul method-nya.",
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
                    "Perhatikan rekening.cpp: constructor pun ditulis",
                    "Rekening::Rekening(...). Nama class dulu (siapa pemiliknya), baru nama",
                    "method-nya, yang kebetulan sama. Initializer list ': pemilik(p),",
                    "saldo(s)' ikut pindah ke .cpp. Yang tinggal di header cuma",
                    "deklarasinya.",
                    "",
                    "Sekarang ada tiga hal di header itu yang belum dijelaskan.",
                    "",
                    "1) Include guard: #ifndef, #define, #endif",
                    "",
                    "Satu header sering ke-include lebih dari sekali di berkas yang sama",
                    "tanpa kamu sadari. Misalnya main.cpp meng-include rekening.h dan juga",
                    "bank.h, padahal bank.h sendiri meng-include rekening.h. Isinya jadi",
                    "ditempel dua kali, dan compiler berhenti:",
                    "",
                    "  error: redefinition of 'class Rekening'",
                    "",
                    "Tiga baris penjaga ini mencegahnya:",
                    "  #ifndef REKENING_H   // kalau REKENING_H belum pernah didefinisikan...",
                    "  #define REKENING_H   // ...definisikan sekarang, lalu baca terus isinya",
                    "  ...isi header...",
                    "  #endif               // penempelan KEDUA melompat langsung ke sini, kosong",
                    "",
                    "Nama guard-nya bebas, asal unik di seluruh project. Kebiasaannya nama",
                    "berkas dalam huruf besar, misalnya NAMA_BERKAS_H. Kalau dua header",
                    "nggak sengaja pakai nama guard yang sama, salah satunya ikut terlewat",
                    "tanpa pesan apa pun, dan error-nya muncul jauh dari penyebabnya.",
                    "",
                    "Bentuk modernnya cuma satu baris di paling atas berkas, tanpa #endif:",
                    "",
                    "  #pragma once",
                    "",
                    "#pragma once bukan bagian resmi standar C++. Tapi semua compiler besar",
                    "mendukungnya (g++, clang, MSVC). Dua-duanya bakal kamu temui di kode",
                    "beneran. Pilih satu dan pakai terus. Nggak perlu memakai keduanya",
                    "sekaligus di berkas yang sama.",
                    "",
                    "2) #include \"rekening.h\" vs #include <vector>",
                    "",
                    "  <kurung sudut>  -> cari di folder pustaka sistem/compiler. Untuk",
                    "                     header standar dan pustaka pihak ketiga:",
                    "                     <iostream>, <string>, <vector>.",
                    "  \"tanda kutip\"   -> cari DULU di folder berkas ini sendiri. Untuk",
                    "                     header buatanmu: \"rekening.h\".",
                    "",
                    "Kalau salah pilih, kamu dapat 'fatal error: rekening.h: No such file",
                    "or directory', padahal berkasnya jelas ada di sebelahnya.",
                    "",
                    "3) Jangan pernah menulis 'using namespace std;' di dalam header.",
                    "",
                    "Header disalin apa adanya ke setiap berkas yang meng-include-nya. Jadi",
                    "baris itu ikut dipaksakan ke semua orang yang memakai class-mu.",
                    "Bentrok namanya baru muncul belakangan, di berkas yang bukan kamu yang",
                    "nulis. Di header, tulis nama lengkapnya: std::string, std::vector.",
                    "'using namespace std;' cukup ditulis di .cpp. Lihat main.cpp di contoh",
                    "atas, sementara rekening.h nggak punya baris itu.",
                ],
            },
            {
                "heading": "Mana yang tetap tinggal di header",
                "body": [
                    "Aturan gampangnya:",
                    "  - Getter atau setter satu baris biarkan di dalam class. Memindahkannya",
                    "    ke .cpp cuma menambah baris tanpa bikin apa pun lebih jelas.",
                    "  - Method yang badannya lebih dari 2-3 baris, atau yang butuh #include",
                    "    tambahan, dideklarasikan di header dan didefinisikan di .cpp.",
                    "",
                    "Header kan disalin ke banyak berkas. Terus kok method di dalam class",
                    "aman ditulis di header? Alasannya, method yang didefinisikan di dalam",
                    "badan class otomatis dianggap inline oleh compiler. Inline artinya",
                    "\"salinan fungsi ini boleh muncul di banyak berkas\".",
                    "",
                    "Fungsi bebas nggak dapat perlakuan itu. Kalau badannya ditulis di",
                    "header tanpa kata inline, dua .cpp yang meng-include header yang sama",
                    "menghasilkan dua salinan. Linker, yaitu program yang menyatukan semua",
                    "hasil kompilasi jadi satu program, lalu berhenti dengan:",
                    "",
                    "  multiple definition of `persen(double, double)'",
                    "",
                    "Tambahkan inline, dan linker paham bahwa salinan itu boleh muncul di",
                    "mana-mana dan cukup dipakai salah satu. Ini juga alasan template selalu",
                    "ditulis lengkap di header (materi Templates): compiler perlu melihat",
                    "badannya di tiap berkas yang memakainya.",
                    "",
                    "Di contoh bawah ada satu hal lagi, yaitu 'double saldo = 0;'. Sejak",
                    "C++11, nilai awal atribut boleh ditulis langsung di header, tanpa lewat",
                    "constructor.",
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
                    "Sekarang cara mengompilasi banyak berkas. Yang ditulis di perintah cuma",
                    "berkas .cpp. Header nggak pernah ikut ditulis, karena isinya udah masuk",
                    "lewat #include:",
                    "",
                    "  g++ -std=c++17 -Wall main.cpp rekening.cpp -o app",
                    "  ./app",
                    "",
                    "Kalau satu .cpp lupa disertakan, error-nya datang dari linker, bukan",
                    "dari compiler:",
                    "",
                    "  undefined reference to `Rekening::setor(double)'",
                    "",
                    "Artinya kira-kira: \"aku percaya method ini ada karena header",
                    "menjanjikannya, tapi badannya nggak ketemu di berkas mana pun yang kamu",
                    "kasih\". Obatnya hampir selalu sama: tambahkan .cpp yang ketinggalan ke",
                    "perintah kompilasi. Cara cepat membedakannya dari error biasa: error",
                    "compiler selalu menyebut nomor baris, error linker nggak. Linker cuma",
                    "tahu nama.",
                    "",
                    "Kalau berkasnya udah belasan, menulis daftar .cpp satu per satu jadi",
                    "nggak kepegang. Alat standar di industri C++ untuk ini adalah CMake.",
                    "Makefile lebih dekat ke dunia C. Ini isi CMakeLists.txt paling kecil",
                    "yang udah cukup untuk project di atas:",
                    "",
                    "  cmake_minimum_required(VERSION 3.16)",
                    "  project(rekening)",
                    "  set(CMAKE_CXX_STANDARD 17)",
                    "  add_executable(app main.cpp rekening.cpp)",
                    "",
                    "Cara membangunnya:",
                    "  cmake -B build         # sekali saja: siapkan folder build",
                    "  cmake --build build    # ulangi tiap kali kode berubah",
                    "  ./build/app",
                    "",
                    "Terakhir, ini juga cara membaca repo C++ orang lain. Jangan mulai dari",
                    "daftar berkas. Buka CMakeLists.txt dulu. Baris add_executable",
                    "menyebut .cpp mana yang jadi program dan di mana main()-nya. Baris",
                    "add_library menyebut mana yang cuma pustaka pendukung. Sesudah tahu",
                    "itu, baru buka header-nya untuk melihat class apa aja yang tersedia.",
                    "Kalau perlu tahu isinya, buka .cpp yang namanya sama.",
                ],
            },
        ],
    },
    {
        "title": "13. Pointer this, Anggota static & explicit",
        "sections": [
            {
                "body": [
                    "Setiap method non-static punya satu variabel tersembunyi bernama this.",
                    "Isinya alamat objek yang lagi menjalankan method itu.",
                    "",
                    "  r.setor(50000);   // di dalam setor, this bernilai &r",
                    "  s.setor(50000);   // di dalam setor yang SAMA, this bernilai &s",
                    "",
                    "Yang perlu kamu pegang: this itu pointer. Dia bukan objek, juga bukan",
                    "reference. Kalau kamu datang dari Java, di sinilah biasanya kesandung.",
                    "Di Java, this adalah referensi ke objeknya, jadi ditulis this.nama. Di",
                    "C++ bentuknya begini:",
                    "",
                    "  this->nama     // akses lewat pointer, -> yang sama dari materi Referensi",
                    "  (*this).nama   // sama artinya, cuma lebih panjang",
                    "  *this          // OBJEKNYA sendiri, hasil dereference pointer",
                    "  this.nama      // ERROR: this itu pointer, titik tidak berlaku untuknya",
                    "",
                    "Kegunaan pertama: membedakan atribut dari parameter yang namanya sama.",
                    "",
                    "  Rekening(string nama) { this->nama = nama; }",
                    "",
                    "Di dalam constructor itu, nama yang ditulis polos selalu berarti",
                    "parameter, karena parameter itu yang paling dekat. Atributnya cuma bisa",
                    "dicapai lewat this->.",
                    "",
                    "Jebakan: tanpa this->, baris 'nama = nama;' cuma menyalin parameter ke",
                    "dirinya sendiri. Atribut objeknya nggak pernah terisi. g++ dengan -Wall",
                    "-Wextra pun nggak kasih peringatan apa-apa. Yang kelihatan cuma nama",
                    "kosong dan angka sampah waktu programnya jalan.",
                    "",
                    "Makanya materi-materi sebelumnya selalu pakai nama parameter pendek (n,",
                    "u, p) atau initializer list ': nama(n)'. Dua-duanya cara menghindari",
                    "bentrok nama. Sekarang kamu punya cara ketiga, dan cara ini juga yang",
                    "paling sering kamu temui di kode orang lain.",
                    "",
                    "Kegunaan kedua: 'return *this;' supaya method bisa dirangkai.",
                    "",
                    "  obj.setA(1).setB(2).setC(3);",
                    "",
                    "Tipe kembalinya wajib reference, yaitu Rekening&. Kalau kamu nulis",
                    "Rekening polos, yang dikembalikan adalah salinan objeknya. Jadi setB(2)",
                    "mengubah salinan itu, lalu salinannya dibuang. Objek aslinya cuma kena",
                    "setA(1). Kodenya tetap bisa dikompilasi tanpa satu peringatan pun, cuma",
                    "hasilnya yang salah. Pola return *this ini bakal kamu pakai lagi nanti",
                    "waktu menulis operator=.",
                    "",
                    "Di method yang ditandai const (lihat materi Encapsulation), tipe this",
                    "ikut jadi const Rekening*. Akibatnya, percobaan mengubah atribut",
                    "langsung ditolak compiler.",
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
                    "Kata static dipakai untuk tiga hal yang sebetulnya nggak berhubungan.",
                    "Kalau dipisah dari awal, nanti kamu nggak gampang bingung.",
                    "",
                    "Pertama, anggota data static: satu nilai milik class, nggak dimiliki",
                    "masing-masing objek. Seribu objek Tiket tetap berbagi satu",
                    "jumlahDibuat yang sama. Yang ditulis di dalam class cuma",
                    "deklarasinya. Nilainya harus didefinisikan sekali lagi di luar class,",
                    "di tingkat berkas:",
                    "",
                    "  class Tiket { static int jumlahDibuat; };   // deklarasi",
                    "  int Tiket::jumlahDibuat = 0;                // definisi, tanpa 'static'",
                    "",
                    "Kalau baris kedua lupa ditulis, kompilasinya lancar, tapi linker",
                    "menolak dengan 'undefined reference to Tiket::jumlahDibuat'. Pesan itu",
                    "bisa menyesatkan. Yang hilang di sini tempat penyimpanan nilainya,",
                    "padahal kata \"reference\" bikin kesannya kayak fungsi yang hilang.",
                    "",
                    "Kedua, method static: milik class, dipanggil tanpa objek apa pun:",
                    "",
                    "  Tiket::totalDibuat();     // pakai ::, bukan titik",
                    "",
                    "Karena nggak ada objek yang memanggilnya, method static nggak punya",
                    "this. Jadi dia nggak bisa menyentuh atribut biasa sama sekali. Dua",
                    "pemakaian yang paling sering: fungsi bantu atau penghitung, dan",
                    "factory method, yaitu fungsi yang membuatkan objek dengan aturannya",
                    "sendiri. Untuk konstanta milik class, tulis static constexpr int MAKS",
                    "= 100; (constexpr artinya nilainya udah pasti sejak waktu kompilasi).",
                    "",
                    "Ketiga, variabel static di dalam fungsi biasa: dibuat sekali, dan",
                    "nilainya bertahan sampai panggilan berikutnya. Nilainya nggak direset",
                    "tiap kali fungsi dipanggil:",
                    "",
                    "  int nomorAntrean() { static int terakhir = 0; return ++terakhir; }",
                    "",
                    "Baris 'static int terakhir = 0;' cuma dijalankan di panggilan pertama.",
                    "Ini berguna, tapi hati-hati: fungsinya jadi punya ingatan. Hasilnya",
                    "nggak lagi cuma bergantung pada argumen yang kamu kasih.",
                    "",
                    "Ada juga makna keempat yang mungkin kamu kenal dari C: static di luar",
                    "fungsi artinya nama itu nggak kelihatan dari berkas lain. Itu topik",
                    "lain, beda dari tiga di atas.",
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
                    "Constructor dengan satu parameter ternyata juga jadi aturan konversi.",
                    "Kalau kamu punya KotakLama(int), compiler boleh mengubah int apa pun",
                    "jadi KotakLama di mana pun sebuah KotakLama diminta:",
                    "",
                    "  terima(7);          // 7 diubah jadi KotakLama(7) tanpa satu kata pun",
                    "  KotakLama a = 7;    // ikut lolos",
                    "",
                    "Kelihatannya praktis. Masalahnya, suatu hari kamu salah menaruh",
                    "argumen, dan compiler malah menutupinya dengan membuatkan objek yang",
                    "nggak pernah kamu minta.",
                    "",
                    "Kata explicit mematikan konversi otomatis itu. Objeknya tetap bisa",
                    "dibuat, cuma harus ditulis terang-terangan: Kotak q{7}; atau Kotak(7).",
                    "Aturan gampangnya: tandai explicit di semua constructor satu parameter,",
                    "kecuali kamu memang mau konversi otomatisnya.",
                    "",
                    "Kurung kurawal juga bisa dipakai untuk membuat objek dan mengisi",
                    "variabel:",
                    "",
                    "  Kotak p{7};      // sama dengan Kotak p(7);",
                    "  int hitung{};    // 0 - kurawal kosong berarti 'isi dengan nol'",
                    "  int belum;       // TIDAK diinisialisasi - isinya sampah dari memori",
                    "",
                    "C++ modern lebih suka kurawal karena dua alasan:",
                    "  - Kurawal menolak narrowing, yaitu nilai yang terpotong waktu",
                    "    dimasukkan ke tipe yang lebih sempit. 'int x{3.7};' jadi error,",
                    "    sedangkan 'int x = 3.7;' jadi 3 tanpa protes.",
                    "  - Kurawal menghindari most vexing parse. 'Kotak p();' ternyata dibaca",
                    "    compiler sebagai deklarasi fungsi tanpa parameter, dan nggak ada",
                    "    objek yang dibuat. 'Kotak p{};' aman.",
                    "",
                    "Nilai awal atribut juga bisa ditulis langsung di badan class. Namanya",
                    "default member initializer. Contohnya 'int isi{0};' atau",
                    "'int kapasitas = 10;', dan dua bentuk itu artinya sama. Semua",
                    "constructor otomatis ikut memakainya, jadi nggak ada lagi atribut yang",
                    "lupa diisi di salah satu constructor.",
                    "",
                    "Kalau atribut punya dua-duanya, initializer list yang dipakai. Pada",
                    "'Kotak(int n, int k) : isi(n), kapasitas(k) {}', nilai '= 10' nggak",
                    "pernah dipakai. Nilai di badan class cuma berlaku untuk atribut yang",
                    "nggak disebut di initializer list constructor yang dipanggil.",
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
                    "Inheritance atau pewarisan artinya sebuah class mewarisi atribut dan",
                    "method dari class lain. Class yang mewarisi disebut anak (subclass),",
                    "yang diwarisi disebut induk. Konsepnya mirip Java, tapi sintaksnya",
                    "sedikit beda. C++ pakai titik dua (:), bukan extends.",
                    "",
                    "  class Anak : public Induk {",
                    "      // atribut/method tambahan",
                    "  };",
                    "",
                    "Kata public sebelum nama class induk menentukan cara anggota induk",
                    "diwariskan. Public inheritance yang paling umum dipakai. Anggap aja",
                    "itu bentuk standar, mirip extends di Java.",
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
                    "Perhatikan bedanya dengan Java. Tanpa kata virtual, method bersuara di",
                    "Kucing tadi secara teknis belum override sungguhan. Method mana yang",
                    "dipanggil ditentukan oleh tipe statis variabelnya, yaitu tipe yang",
                    "tertulis di kode. Tipe objek aslinya nggak dilihat. Soal virtual ini",
                    "dibahas lengkap di materi Polymorphism berikutnya, dan kamu bakal",
                    "sering memakainya.",
                    "",
                    "Jenis access specifier waktu mewarisi:",
                    "  class B : public A     -> public tetap public, protected tetap protected",
                    "  class B : protected A  -> public JADI protected di B",
                    "  class B : private A    -> SEMUA jadi private di B (paling jarang dipakai)",
                    "",
                    "Beda lagi dari Java, C++ mendukung multiple inheritance, yaitu satu",
                    "class mewarisi dari beberapa induk sekaligus:",
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
                    "Polymorphism artinya satu panggilan yang sama bisa menjalankan method",
                    "yang beda, tergantung objek aslinya. Di C++, ini baru terjadi kalau",
                    "method-nya ditandai virtual. Tanpa kata virtual, C++ nggak melakukan",
                    "polymorphism runtime sungguhan. Di sini C++ beda dari Java, karena di",
                    "Java semua method otomatis virtual.",
                    "",
                    "Kata virtual menandai bahwa method itu boleh di-override oleh",
                    "subclass. Method yang dipanggil lalu ditentukan oleh tipe objek",
                    "aslinya waktu program jalan (runtime). Tipe variabel yang ditulis di",
                    "kode (tipe statis) nggak lagi menentukan.",
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
                    "Destructor juga harus virtual di base class, kalau class itu dipakai",
                    "lewat pointer induk seperti contoh di atas.",
                    "",
                    "Jebakan: tanpa 'virtual ~Hewan()', 'delete h1;' cuma memanggil ~Hewan()",
                    "(destructor induk). ~Kucing() nggak ikut dipanggil. Kalau Kucing punya",
                    "resource sendiri yang harus dibereskan, misalnya memori dinamis,",
                    "resource itu bocor (resource leak). Aturan resmi C++ malah menyebut",
                    "kasus ini undefined behavior, artinya hasilnya nggak dijamin sama",
                    "sekali.",
                    "",
                    "Lalu kata override (C++11 ke atas). Secara teknis override nggak",
                    "wajib, tapi pakai terus. Kalau kamu salah tulis judul method-nya,",
                    "misalnya namanya typo atau parameternya beda, compiler langsung kasih",
                    "error. Bug-nya ketahuan jauh lebih awal dibanding kalau kamu nggak",
                    "nulis override.",
                    "",
                    "Pasangannya adalah final (juga C++11 ke atas). Posisinya persis sama",
                    "dengan override, jadi waktu pertama kali lihat, kamu mungkin mengira",
                    "itu salah tulis. Artinya: dikunci, cukup sampai di sini.",
                    "",
                    "  void bersuara() override final;   // METHOD ini tidak boleh",
                    "                                    // di-override lagi ke bawah",
                    "  class Persia final : public Kucing { ... };  // CLASS ini tidak",
                    "                                               // boleh diwarisi",
                    "",
                    "Kalau ada yang tetap mencoba menurunkannya, compiler langsung",
                    "menolak. final dipakai kalau sebuah class atau method udah dianggap",
                    "selesai, dan pewarisan lebih lanjut cuma bakal merusak cara kerjanya.",
                    "Bedanya dengan override: override boleh berdiri sendiri, sedangkan",
                    "final di method biasanya ditulis sesudah override.",
                ]
            },
        ],
    },
    {
        "title": "16. Abstract Class & Pure Virtual Function",
        "sections": [
            {
                "body": [
                    "Pure virtual function adalah method virtual yang nggak punya isi.",
                    "Tandanya '= 0' di akhir deklarasi. Kalau sebuah class punya minimal",
                    "satu pure virtual function, class itu otomatis jadi abstract class.",
                    "Abstract class nggak bisa dibuat objeknya langsung, mirip abstract di",
                    "Java.",
                    "",
                    "  class Bentuk {",
                    "  public:",
                    "      virtual double luas() = 0;   // pure virtual - WAJIB di-override",
                    "  };",
                    "",
                    "C++ nggak punya kata interface tersendiri seperti Java. Yang disebut",
                    "interface di C++ biasanya abstract class yang semua method-nya pure",
                    "virtual dan nggak punya atribut data.",
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
                    "Kenapa abstract class atau interface berguna?",
                    "  - Dia menjamin semua subclass punya method tertentu. Anggap aja",
                    "    kontrak.",
                    "  - Kamu bisa menulis kode yang bekerja dengan tipe induk (Bentuk*),",
                    "    dan kode itu otomatis jalan untuk semua turunannya.",
                    "  - Banyak design pattern dibangun di atasnya, misalnya Strategy dan",
                    "    Factory.",
                ]
            },
        ],
    },
    {
        "title": "17. Konversi Tipe: static_cast & dynamic_cast",
        "sections": [
            {
                "body": [
                    "Di kode beneran, kamu bakal sering memindahkan nilai dari satu tipe ke",
                    "tipe lain. Misalnya bilangan bulat dibagi bilangan bulat tapi hasilnya",
                    "mau desimal. Atau .size() dibandingkan dengan int. Atau pointer induk",
                    "yang mau dipakai sebagai anak. Perpindahan itu namanya konversi tipe,",
                    "atau cast.",
                    "",
                    "Di C caranya cuma satu: tulis tipe tujuannya dalam kurung.",
                    "",
                    "  int x = (int) harga;   // gaya C - MASIH jalan di C++, tapi dihindari",
                    "",
                    "Cara ini masih jalan, tapi sebaiknya dihindari. Alasannya:",
                    "  - Satu bentuk dipakai untuk beberapa pekerjaan yang bahayanya jauh",
                    "    beda. Compiler mencoba beberapa cara: konversi wajar, membuang",
                    "    const, sampai memaksa membaca ulang bit mentah. Cara mana pun yang",
                    "    berhasil langsung dipakai, dan kamu nggak dikasih tahu yang mana.",
                    "  - Susah kelihatan waktu dibaca. '(int)' tenggelam di tengah baris,",
                    "    dan mata gampang melewatinya. static_cast<int> sengaja dibikin",
                    "    panjang supaya tiap konversi kelihatan sebagai keputusan yang",
                    "    disengaja.",
                    "  - Style guide besar (Google, LLVM) melarangnya. g++ juga menandainya",
                    "    kalau dikompilasi dengan -Wold-style-cast:",
                    "      warning: use of old-style cast to 'int' [-Wold-style-cast]",
                    "",
                    "C++ memecahnya jadi empat kata kunci, masing-masing untuk satu",
                    "pekerjaan:",
                    "  static_cast<T>(v)       konversi wajar, dicek compiler saat kompilasi",
                    "  dynamic_cast<T>(v)      turun ke tipe anak, diperiksa saat program JALAN",
                    "  const_cast<T>(v)        membuang atau memasang const",
                    "  reinterpret_cast<T>(v)  memaksa membaca ulang bit mentah - paling bahaya",
                    "",
                    "Bentuknya selalu 'nama_cast<Tipe>(nilai)'. Kurung sudut <> di sini",
                    "nggak ada hubungannya dengan template buatanmu (itu materi tersendiri",
                    "nanti). Keempatnya kata kunci bawaan C++, dan yang ditulis di dalam <>",
                    "adalah tipe tujuannya.",
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
                    "size_t adalah tipe bilangan bulat tanpa tanda (unsigned) yang dipakai",
                    "C++ untuk ukuran. .size() milik vector, string, dan map mengembalikan",
                    "tipe ini, begitu juga operator sizeof. Nilainya nggak pernah negatif,",
                    "karena panjang sesuatu memang nggak pernah negatif.",
                    "",
                    "Makanya loop di materi vector ditulis 'for (size_t i = 0; ...)'. Kalau",
                    "ditulis 'int i', g++ -Wall langsung mengeluh:",
                    "  warning: comparison of integer expressions of different signedness:",
                    "  'int' and 'std::vector<int>::size_type' [-Wsign-compare]",
                    "",
                    "Kalau bilangan bertanda dibandingkan dengan yang tanpa tanda, compiler",
                    "terpaksa mengubah salah satunya tanpa bilang-bilang. Hasilnya belum",
                    "tentu sesuai dugaanmu.",
                    "",
                    "Jebakan: kesalahan yang paling sering terjadi adalah menelusuri vector",
                    "mundur dari belakang.",
                    "",
                    "  vector<int> kosong;",
                    "  for (size_t i = kosong.size() - 1; i >= 0; i--) {   // RUSAK",
                    "      cout << kosong[i];",
                    "  }",
                    "",
                    "kosong.size() bernilai 0. Di tipe unsigned, nol dikurangi satu nggak",
                    "jadi -1. Nilainya muter ke angka terbesar: 18446744073709551615. Lalu",
                    "'i >= 0' selalu benar, karena unsigned memang nggak bisa kurang dari",
                    "nol. g++ -Wextra bahkan bilang begitu: 'comparison of unsigned",
                    "expression in >= 0 is always true'. Programnya membaca jauh di luar",
                    "vector. Biasanya langsung crash, kadang malah kelihatan jalan sebentar",
                    "sambil mencetak angka sampah.",
                    "",
                    "Ada dua jalan keluarnya:",
                    "  - Pakai indeks bertanda, dan tulis konversinya terang-terangan:",
                    "      for (int i = static_cast<int>(v.size()) - 1; i >= 0; i--)",
                    "  - Atau nggak usah pakai indeks sama sekali. Range-based for cukup",
                    "    untuk sebagian besar kasus, dan dengan cara itu nggak ada indeks",
                    "    yang bisa salah hitung.",
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
                    "Alurnya begini. Variabelnya bertipe Hewan*, tapi objek yang ditunjuk",
                    "bisa Kucing, bisa juga Anjing (lihat materi Polymorphism & Virtual",
                    "Function). Naik ke tipe induk selalu aman dan terjadi otomatis. Turun",
                    "lagi ke tipe anak butuh dynamic_cast, karena benar atau salahnya baru",
                    "ketahuan waktu program jalan.",
                    "",
                    "Ada empat hal yang perlu kamu ingat:",
                    "  - Hasil cast pointer wajib dicek apakah nullptr. Cast yang gagal",
                    "    nggak melempar apa pun dan nggak bikin compiler protes. Dia cuma",
                    "    mengembalikan nullptr. Kalau method-nya langsung dipanggil,",
                    "    programnya crash.",
                    "  - Versi referensi perilakunya beda. dynamic_cast<Kucing&>(*h) melempar",
                    "    std::bad_cast dari <typeinfo>, jadi bungkus dengan try-catch (lihat",
                    "    materi Exception Handling). Pilih versi pointer kalau gagal itu hal",
                    "    wajar. Pilih versi referensi kalau gagal berarti ada bug.",
                    "  - Class induknya wajib polymorphic, artinya minimal punya satu virtual",
                    "    function. Destructor virtual juga dihitung. Kalau nggak, kamu dapat",
                    "    error waktu kompilasi:",
                    "      error: cannot 'dynamic_cast' ... (source type is not polymorphic)",
                    "  - static_cast juga bisa dipakai turun ke anak, tapi dia nggak",
                    "    memeriksa apa pun. Kalau tebakanmu meleset, nggak ada tanda apa-apa",
                    "    sampai programnya berperilaku aneh atau crash di tempat yang nggak",
                    "    ada hubungannya.",
                    "",
                    "Satu saran yang jarang ditulis di dokumentasi: kalau kamu sering butuh",
                    "dynamic_cast, biasanya masalahnya ada di desain. Kemungkinan ada",
                    "virtual function yang belum dibikin. Rantai \"kalau dia Kucing lakukan",
                    "A, kalau Anjing lakukan B\" adalah tanda perilaku itu harusnya jadi",
                    "satu virtual function di Hewan, yang di-override tiap turunan.",
                    "dynamic_cast baru pas dipakai kalau method-nya memang cuma dimiliki",
                    "anak dan nggak masuk akal ditaruh di induk.",
                    "",
                    "Dua cast sisanya jarang dipakai. Tapi kenali bentuknya supaya kamu",
                    "nggak bingung kalau ketemu di kode orang:",
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
                    "Di C++, operator seperti +, -, ==, dan << boleh kamu definisikan ulang",
                    "untuk class buatanmu sendiri. Java nggak mengizinkan ini. Hasilnya,",
                    "objekmu bisa dipakai dengan tulisan yang wajar, sama seperti angka.",
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
                    "Baris 'friend ostream& operator<<(...)' di contoh tadi memuat tiga hal",
                    "yang belum pernah dijelaskan. Kita bongkar satu per satu.",
                    "",
                    "Pertama, friend artinya izin masuk.",
                    "",
                    "friend memberi satu fungsi, atau satu class lain, hak untuk mengakses",
                    "bagian private dan protected. Ini satu-satunya celah resmi pada",
                    "encapsulation yang kamu pelajari di materi Encapsulation. Celah itu",
                    "dibuka oleh class-nya sendiri, dari dalam.",
                    "",
                    "     friend ostream& operator<<(ostream&, const Titik&);  // 1 fungsi",
                    "     friend class Auditor;                          // SELURUH class",
                    "",
                    "Ada dua hal yang sering disalahpahami:",
                    "  - Izinnya diberikan, nggak bisa diambil. Kamu nggak bisa menyatakan",
                    "    dirimu sendiri sebagai friend dari class orang lain.",
                    "  - Fungsi friend itu bukan anggota class. Dia ditulis tanpa awalan",
                    "    'Titik::' dan nggak punya pointer this. Makanya objek Titik-nya",
                    "    harus dioper sebagai parameter.",
                    "",
                    "Di kode sungguhan, friend paling sering muncul untuk operator<<. Selain",
                    "itu ada pola friend untuk testing: 'friend class UjiRekening;'. Dengan",
                    "begitu class tes boleh memeriksa isi private, tanpa harus membuat",
                    "semua atribut jadi public cuma supaya bisa dites.",
                    "",
                    "Kedua, ostream itu nama class.",
                    "",
                    "ostream adalah class dari objek cout, kependekan dari 'output stream'.",
                    "Pasangannya istream, class dari cin. Jadi parameter 'ostream &os'",
                    "artinya \"aliran keluaran mana pun\": cout, cerr, atau ofstream yang",
                    "menulis ke berkas. Karena itu, satu operator<< cukup untuk semua",
                    "tujuan sekaligus.",
                    "",
                    "Ketiga, 'ostream&' dan 'return os;' itu reference.",
                    "",
                    "Di materi Referensi (&) vs Pointer, & dipakai untuk parameter. Di sini",
                    "& dipakai untuk nilai kembalian. Fungsinya mengembalikan stream itu",
                    "sendiri, bukan salinannya.",
                    "",
                    "Hal itu yang bikin cout bisa dirangkai. Compiler membaca cout << a << b",
                    "sebagai:",
                    "",
                    "     (cout << a) << b;",
                    "",
                    "'(cout << a)' menyerahkan cout kembali, jadi '<< b' punya sesuatu di",
                    "sebelah kirinya untuk dikerjakan. Kalau kembaliannya void, atau ostream",
                    "tanpa &, rangkaiannya putus di operator kedua. Compiler lalu menolak",
                    "dengan pesan yang panjang dan susah dipahami.",
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
                    "Operator yang umum di-overload: +, -, *, /, ==, !=, <, >, <<, >>, [],",
                    "(), dan = (assignment operator).",
                    "",
                    "Aturan main operator overloading:",
                    "  1. Perilaku operatornya harus masuk akal dan gampang ditebak. Jangan",
                    "     overload '+' untuk melakukan pengurangan.",
                    "  2. Pakai 'const' pada parameter dan method kalau operatornya nggak",
                    "     seharusnya mengubah objek.",
                    "  3. Jangan berlebihan. Overload cuma kalau kodenya jadi lebih jelas",
                    "     dibaca, misalnya untuk Vector, Matrix, atau Complex Number. Nggak",
                    "     semua class perlu.",
                ]
            },
        ],
    },
    {
        "title": "19. Copy Constructor, operator= & Aturan Tiga",
        "sections": [
            {
                "body": [
                    "Setiap class yang kamu tulis otomatis dapat dua anggota gratis dari",
                    "compiler, selama kamu nggak menulisnya sendiri:",
                    "",
                    "  Buffer(const Buffer &lain);              // copy constructor",
                    "  Buffer& operator=(const Buffer &lain);   // copy assignment",
                    "",
                    "Dua anggota itu nggak tertulis di kodemu, nggak pernah kamu sebut,",
                    "tapi tetap ada. Isi buatan compiler selalu sama: salin setiap atribut",
                    "satu per satu, apa adanya.",
                    "",
                    "Untuk atribut int, string, atau vector, cara itu udah benar. string",
                    "dan vector tahu cara menyalin dirinya sendiri. Yang bahaya cuma satu",
                    "jenis atribut, yaitu pointer mentah. Menyalin pointer apa adanya",
                    "artinya yang disalin alamatnya, bukan isinya. Akibatnya ada dua objek",
                    "yang memegang alamat yang sama.",
                    "",
                    "Dua anggota itu sering tertukar. Bedanya begini:",
                    "  Buffer b = a;    objek b BELUM ada, baru lahir -> COPY CONSTRUCTOR",
                    "  b = a;           objek b SUDAH ada, ditimpa    -> operator=",
                    "",
                    "Penyalinan juga terjadi di tempat yang nggak kelihatan seperti",
                    "penyalinan. Makanya bug-nya sering muncul dari arah yang nggak kamu",
                    "duga:",
                    "  - mengoper objek ke fungsi by value:  void cetak(Buffer b)",
                    "  - mengembalikan objek dari sebuah fungsi",
                    "  - v.push_back(objek) ke dalam vector",
                ],
            },
            {
                "heading": "Program yang SENGAJA mati - jalankan dan lihat sendiri",
                "body": [
                    "Class di bawah ini udah benar menurut materi Constructor & Destructor.",
                    "Resource diambil pakai new di constructor, lalu dilepas pakai delete[]",
                    "di destructor. Tapi satu baris penyalinan yang kelihatan biasa bikin",
                    "programnya ambruk.",
                    "",
                    "(Catatan kecil: 'new int[n]' berpasangan dengan 'delete[]' yang pakai",
                    "kurung siku, bukan 'delete' biasa. Salah pasangan juga merusak, walaupun",
                    "bukan itu yang sedang kita bahas.)",
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
                    "Programnya mati di tengah jalan, dengan pesan kira-kira seperti ini:",
                    "  free(): double free detected in tcache 2",
                    "",
                    "Di aplikasi ini pesannya diterjemahkan jadi \"Program membatalkan",
                    "dirinya sendiri (abort)\". Di terminal biasa yang muncul \"Aborted (core",
                    "dumped)\". Teks persisnya beda-beda tiap mesin. Yang penting, programnya",
                    "berhenti paksa, nggak selesai dengan normal.",
                    "",
                    "Ada dua hal yang salah sekaligus, dan dua-duanya berasal dari satu",
                    "sebab.",
                    "",
                    "Shallow copy (buatan compiler): dua objek, satu memori.",
                    "",
                    "  a.data ---+",
                    "            +---> [ 99 ][ 0 ][ 0 ]     <- cuma ada SATU, dipakai berdua",
                    "  b.data ---+",
                    "",
                    "  1. b.data[0] = 99 ikut mengubah a, karena memang barangnya sama.",
                    "  2. destructor jalan dua kali atas alamat yang sama. Ini yang",
                    "     disebut double free.",
                    "",
                    "Deep copy (yang harus kita tulis sendiri): dua objek, dua memori.",
                    "",
                    "  a.data ------> [ 10 ][ 0 ][ 0 ]",
                    "  b.data ------> [ 99 ][ 0 ][ 0 ]      <- salinan MILIK SENDIRI",
                    "",
                    "Masing-masing punya memorinya sendiri, jadi masing-masing boleh",
                    "menghapus miliknya satu kali. Nggak ada yang bentrok.",
                    "",
                    "Jebakan: double free nggak selalu langsung mematikan program. Kadang",
                    "dia cuma merusak catatan pengelolaan heap, dan yang ambruk malah baris",
                    "lain jauh sesudahnya, baris yang nggak salah apa-apa. Jadi tempat",
                    "programnya crash belum tentu tempat penyebabnya.",
                    "",
                    "Selain itu, satu delete[] tadi juga bikin pointer di objek yang satunya",
                    "menunjuk ke memori yang udah dikembalikan. Pointer seperti ini disebut",
                    "dangling pointer. Membaca a.data[0] sesudah b dihancurkan itu udah",
                    "salah, walaupun kadang kelihatan jalan. Kode yang kadang jalan malah",
                    "lebih bahaya daripada yang selalu crash, karena kesalahannya lebih",
                    "lama ketahuan.",
                ],
            },
            {
                "heading": "Versi benar: tiga anggota yang harus datang bersama",
                "body": [
                    "Tiga deklarasi ini perlu kamu kenali waktu membaca kode orang lain:",
                    "",
                    "  Buffer(const Buffer &lain);              // copy constructor",
                    "  Buffer& operator=(const Buffer &lain);   // copy assignment",
                    "  ~Buffer();                               // destructor",
                    "",
                    "Kenapa parameternya 'const Buffer &lain', bukan 'Buffer lain'?",
                    "  - Kalau by value, mengoper argumennya aja udah butuh penyalinan.",
                    "    Penyalinan itu memanggil copy constructor lagi, dan begitu terus",
                    "    tanpa ujung. Compiler menolaknya: \"invalid constructor; you",
                    "    probably meant Buffer (const Buffer&)\".",
                    "  - const dipakai supaya sumber yang disalin dijamin nggak ikut",
                    "    berubah, dan supaya objek const pun tetap bisa disalin.",
                    "",
                    "Kenapa operator= mengembalikan 'Buffer&' lalu ditutup 'return *this;'?",
                    "  - Supaya rangkaian 'x = y = z' bekerja seperti pada tipe bawaan.",
                    "  - Yang dikembalikan reference, bukan salinan, supaya hasilnya nggak",
                    "    disalin sekali lagi.",
                    "  - '*this' udah dibahas di materi Pointer this, yaitu objek yang",
                    "    sedang menjalankan method itu.",
                    "",
                    "Kenapa ada penjaga 'if (this == &lain) return *this;'?",
                    "  operator= menghapus milik sendiri dulu, baru menyalin dari sumber.",
                    "  Pada 'a = a;' tanpa penjaga, dia menghapus data a, lalu menyalin dari",
                    "  a yang barusan dihapus. Isinya jadi sampah. Kedengarannya konyol,",
                    "  tapi di kode sungguhan bentuknya jarang 'a = a'. Biasanya 'v[i] =",
                    "  v[j];' atau 'objek = *penunjuk;' yang kebetulan menunjuk objek yang",
                    "  sama.",
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
                    "Aturan Tiga (Rule of Three). Yang ini perlu kamu hafal:",
                    "",
                    "  Kalau sebuah class butuh DESTRUCTOR buatan sendiri, ia hampir pasti",
                    "  juga butuh COPY CONSTRUCTOR dan operator= buatan sendiri.",
                    "",
                    "Alasannya persis yang barusan kamu lihat. Destructor manual ditulis",
                    "karena class itu memiliki sesuatu: memori, berkas, koneksi, atau lock.",
                    "Sesuatu yang dimiliki nggak boleh ikut tersalin mentah-mentah ke objek",
                    "kedua. Kalau kamu cuma menulis satu dari tiga, bug-nya tinggal tunggu",
                    "waktu, dan compiler nggak bakal ngasih peringatan sama sekali.",
                    "",
                    "Kalau class-mu memang nggak boleh disalin, nyatakan terang-terangan:",
                    "",
                    "  class Berkas {",
                    "  public:",
                    "      Berkas(const Berkas &) = delete;             // dilarang disalin",
                    "      Berkas& operator=(const Berkas &) = delete;  // dilarang ditimpa-salin",
                    "  };",
                    "",
                    "  Berkas g = f;   // error: use of deleted function 'Berkas::Berkas(...)'",
                    "",
                    "'= delete' di sini nggak ada hubungannya dengan operator delete yang",
                    "membebaskan memori. Kata kuncinya kebetulan dipakai ulang. Artinya di",
                    "sini cuma \"anggota ini nggak ada, jangan coba dipanggil\". Lawannya",
                    "'= default', artinya \"buatkan versi bawaanmu, aku cuma mau menyebutnya",
                    "terang-terangan\".",
                    "",
                    "  Titik(const Titik &) = default;   // versi bawaan compiler, sengaja diminta",
                    "",
                    "Dengan cara ini juga unique_ptr dibuat nggak bisa disalin, seperti yang",
                    "nanti kamu lihat di materi Smart Pointer. Copy constructor-nya memang",
                    "ditandai = delete di header standarnya. Pesan error-nya pun mirip:",
                    "'use of deleted function ... unique_ptr(const unique_ptr&)'. Baris",
                    "'= delete' seperti itu juga ada di hampir setiap class serius yang",
                    "memegang resource, misalnya mutex, thread, dan ifstream. Sekarang kamu",
                    "tahu artinya waktu membacanya.",
                    "",
                    "Cara paling aman lolos dari Aturan Tiga adalah nggak memegang pointer",
                    "mentah sama sekali. Pakai vector, string, dan smart pointer sebagai",
                    "atribut. Ketiganya udah tahu cara mengurus penyalinan dan penghapusan",
                    "dirinya sendiri. Jadi versi bawaan compiler kembali benar, dan kamu",
                    "nggak perlu menulis satu pun dari tiga anggota itu.",
                    "",
                    "Mulai C++11, Aturan Tiga berkembang jadi Aturan Lima. Dua tambahannya",
                    "adalah move constructor dan move assignment, yang dibahas di materi",
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
                    "Template itu cara bikin fungsi atau class yang bisa bekerja dengan",
                    "berbagai tipe data, tanpa menulis ulang kodenya. Mirip Generics di",
                    "Java, tapi cara kerjanya beda: compiler membuat ulang kode template",
                    "untuk setiap tipe yang dipakai.",
                    "",
                    "  template <typename T>",
                    "  T maksimum(T a, T b) {",
                    "      return (a > b) ? a : b;",
                    "  }",
                    "",
                    "  maksimum(3, 7);        // T otomatis jadi int",
                    "  maksimum(3.5, 2.1);    // T otomatis jadi double",
                    "",
                    "T di situ cuma nama sementara untuk \"tipe apa pun yang nanti dipakai\".",
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
                    "Template juga boleh punya lebih dari satu tipe parameter:",
                    "  template <typename K, typename V>",
                    "  class Pasangan {",
                    "      K key; V value;",
                    "      // ...",
                    "  };",
                    "  Pasangan<string, int> p;   // K=string, V=int",
                    "",
                    "STL, yang dibahas di materi berikutnya, seluruhnya dibangun pakai",
                    "template. Makanya vector<int>, map<string,int>, dan kawan-kawannya bisa",
                    "bekerja dengan tipe data apa pun yang kamu tentukan.",
                ]
            },
            {
                "heading": "Tiga hal yang langsung menyambutmu di pustaka template",
                "body": [
                    "Ada tiga hal yang bakal langsung kamu temui di pustaka yang memakai",
                    "template.",
                    "",
                    "Pertama, 'class' dan 'typename' itu artinya sama.",
                    "",
                    "   template <class T>      // artinya SAMA PERSIS dengan",
                    "   template <typename T>   // yang ini",
                    "",
                    "Kata 'class' di posisi itu nggak berarti T harus berupa class.",
                    "Kotak<int> tetap sah. Kata itu cuma sisa sejarah, karena typename baru",
                    "ditambahkan belakangan. Pustaka lama memakai 'class', kode baru",
                    "cenderung memakai 'typename'. Kamu bakal sering lihat keduanya di",
                    "berkas yang sama. Nggak usah dicari bedanya, karena memang nggak ada.",
                    "",
                    "Kedua, template wajib ditulis lengkap di header.",
                    "",
                    "Di materi Memecah Class ke Header kamu belajar pola baku: deklarasi di",
                    ".h, isinya di .cpp. Untuk template, pola itu nggak berlaku. Compiler",
                    "baru membuat versi Kotak<int> waktu dia melihat 'Kotak<int>' dipakai.",
                    "Saat itu juga dia butuh seluruh isi template-nya, nggak cukup",
                    "deklarasinya aja.",
                    "",
                    "Kalau isinya kamu pindahkan ke kotak.cpp, kompilasi tetap lolos. Tapi",
                    "linker mengeluh soal sesuatu yang nggak pernah dibuat:",
                    "",
                    "     undefined reference to `Kotak<int>::simpan(int)'",
                    "",
                    "Pesan itu menyesatkan, karena kodenya jelas ada di kotak.cpp. Yang",
                    "benar: taruh definisi template secara utuh di header, termasuk semua",
                    "method-nya. Itu juga alasan STL dan hampir semua pustaka template cuma",
                    "berupa header, tanpa satu pun .cpp yang perlu dikompilasi. Kamu cukup",
                    "#include, nggak ada yang perlu dibangun.",
                    "",
                    "Ketiga, spesialisasi: versi khusus untuk satu tipe.",
                    "",
                    "Kadang versi umum template-mu benar untuk semua tipe, kecuali satu.",
                    "Untuk kasus itu ada spesialisasi, yaitu versi khusus yang dipilih",
                    "compiler cuma kalau tipenya persis yang disebut:",
                    "",
                    "     template <> class Kotak<bool> { ... };",
                    "",
                    "'template <>' dengan kurung sudut kosong artinya \"di sini udah nggak",
                    "ada tipe yang bebas, semuanya udah ditentukan\". Contoh nyatanya ada di",
                    "STL. vector<bool> adalah spesialisasi yang menyimpan tiap elemen",
                    "sebagai satu bit. Makanya perilakunya agak aneh dibanding vector lain.",
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
                    "STL (Standard Template Library) menyediakan struktur data siap pakai.",
                    "Kamu nggak perlu lagi bikin linked list atau array dinamis sendiri",
                    "kayak di C.",
                    "",
                    "vector<T> itu array dinamis, artinya ukurannya bisa bertambah dan",
                    "berkurang sendiri. Mirip ArrayList di Java atau list di Python. Dari",
                    "semua container STL, vector yang paling sering dipakai. Container",
                    "artinya wadah untuk menyimpan banyak data.",
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
                    "Kenapa vector lebih disarankan daripada array C biasa?",
                    "  - Ukurannya dinamis. Kamu nggak perlu tahu jumlah elemennya dari",
                    "    awal.",
                    "  - Memorinya diurus sendiri. Nggak perlu malloc dan free manual.",
                    "  - Ada pengecekan batas yang bisa kamu pilih pakai, lewat .at(i). Kalau",
                    "    index-nya salah, .at(i) melempar exception. Beda dengan [i] yang",
                    "    nggak ngecek apa-apa.",
                ]
            },
            {
                "heading": "emplace_back, reserve & si tipe index size_t",
                "body": [
                    "emplace_back: saudara push_back yang lebih hemat",
                    "",
                    "push_back(x) menerima objek yang udah jadi, lalu menaruh salinannya ke",
                    "dalam vector. Kalau elemennya sebuah class, kamu harus merakit",
                    "objeknya dulu:",
                    "",
                    "    daftar.push_back(Mahasiswa(\"Andi\", 20));",
                    "",
                    "emplace_back menerima argumen constructor-nya apa adanya, lalu",
                    "membangun objeknya langsung di dalam vector. Nggak ada objek",
                    "sementara, dan nggak ada salinan yang dibuang:",
                    "",
                    "    daftar.emplace_back(\"Andi\", 20);",
                    "",
                    "Di kode C++ modern, emplace_back sama seringnya dengan push_back,",
                    "bahkan sering menggantikannya. Untuk tipe sederhana seperti int,",
                    "keduanya sama aja. Bedanya baru terasa kalau elemennya objek.",
                    "Container lain punya pasangan serupa: emplace, emplace_front, dan",
                    "emplace_back.",
                    "",
                    "reserve(): kasih tahu ukurannya dari awal",
                    "",
                    "Vector menyimpan isinya dalam satu blok memori yang berurutan. Begitu",
                    "blok itu penuh, vector mencari blok baru yang lebih besar, lalu",
                    "memindahkan seluruh isinya ke sana. Ini terjadi tanpa kelihatan,",
                    "berkali-kali, selama loop push_back yang panjang.",
                    "",
                    "    size()     -> berapa elemen yang BENAR-BENAR ada",
                    "    capacity() -> berapa yang MUAT sebelum pindah blok",
                    "    reserve(n) -> sediakan tempat untuk n sekarang juga",
                    "",
                    "Kalau kamu udah tahu bakal memasukkan 1000 elemen, tulis satu baris",
                    "v.reserve(1000) di awal. Semua pemindahan tadi jadi nggak perlu.",
                    "reserve nggak menambah elemen. Sesudahnya size() masih 0, cuma",
                    "capacity()-nya yang jadi 1000.",
                    "",
                    "Contoh di bawah sengaja mencetak setiap penyalinan supaya bedanya",
                    "kelihatan. push_back menjalankan constructor, lalu copy constructor.",
                    "emplace_back cuma menjalankan constructor. Biasanya salinan itu nggak",
                    "mencetak apa-apa, jadi biayanya ada tapi nggak kelihatan.",
                    "",
                    "Kenapa loop di contoh pertama materi ini ditulis 'for (size_t i = 0;",
                    "...)', bukan 'int i'? size_t adalah tipe yang dikembalikan size().",
                    "Alasan lengkapnya, termasuk bug terkenal waktu loop mundur, ada di",
                    "materi Konversi Tipe: static_cast & dynamic_cast.",
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
                    "map<K, V> menyimpan pasangan key-value, yaitu kunci dan nilainya,",
                    "dan selalu terurut berdasarkan key. Mirip TreeMap di Java. Ada juga",
                    "unordered_map, mirip HashMap. Isinya nggak terurut, tapi rata-rata",
                    "lebih cepat: O(1), artinya waktu carinya hampir nggak bertambah",
                    "walaupun datanya makin banyak.",
                    "",
                    "set<T> itu kumpulan elemen yang unik (nggak ada yang dobel) dan",
                    "terurut. Mirip TreeSet di Java. Ada juga unordered_set untuk versi",
                    "tanpa urutan, yang lebih cepat.",
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
                    "Contoh tadi memakai m[kunci] untuk semua hal. Untuk menulis, cara itu",
                    "benar. Tapi ada cara lain, dan untuk membaca, m[kunci] justru punya",
                    "jebakan. Jebakan itu nanti dibongkar tuntas di materi Iterator.",
                    "Sekarang kenalan dulu dengan tiga saudaranya:",
                    "",
                    "  - m.insert({kunci, nilai}) menambah entri. Kalau kuncinya udah ada,",
                    "    insert nggak menimpa dan nggak protes, cuma diam. Kembaliannya",
                    "    sebuah pair. .first-nya iterator ke entri yang bersangkutan,",
                    "    .second-nya bool yang menjawab \"betul baru ditambah?\". Cek .second",
                    "    kalau kamu perlu tahu bedanya.",
                    "  - m.emplace(kunci, nilai) sama dengan insert, tapi tanpa merakit",
                    "    pair-nya dulu. Persis seperti emplace_back pada vector di materi",
                    "    sebelumnya.",
                    "  - m.at(kunci) cuma untuk membaca. Kalau kuncinya nggak ada, at()",
                    "    melempar out_of_range. Dia sengaja ribut supaya kesalahannya",
                    "    ketahuan. Bandingkan dengan m[kunci], yang malah bikin entri baru",
                    "    tanpa bilang apa-apa. Di antara keduanya, cuma at() yang boleh",
                    "    dipakai pada map yang const.",
                    "",
                    "Pegangan praktisnya: [] untuk menulis, at() atau find() untuk membaca,",
                    "dan count() kalau cuma mau ngecek ada atau nggak.",
                    "",
                    "Menelusuri map dengan structured bindings",
                    "",
                    "Loop di atas menamai tiap entri 'pasangan', lalu memakai .first dan",
                    ".second. Dua nama itu nggak ngasih tahu apa-apa soal isinya. Sejak",
                    "C++17 kamu boleh membongkar pair-nya langsung di kepala loop, sekalian",
                    "ngasih nama ke dua bagiannya:",
                    "",
                    "  for (const auto &[nama, angka] : nilai) {",
                    "      cout << nama << \" -> \" << angka << endl;",
                    "  }",
                    "",
                    "Bentuk ini yang paling sering kelihatan di kode C++ modern. Kurung",
                    "sikunya bukan array. Namanya structured bindings, fitur yang sama",
                    "dengan 'auto [nama, umur] = pasangan;' yang nanti kamu temui di materi",
                    "Lambda Expression & Fitur Modern C++. Buang '&' kalau kamu mau salinan.",
                    "Buang 'const' kalau kamu mau mengubah nilainya. Kuncinya tetap nggak",
                    "boleh diubah, karena mengubah kunci bakal merusak urutan map.",
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
                    "Materi sebelumnya ngenalin vector, map, set, dan pair, dan cuma",
                    "nyebut unordered_map sekilas. Padahal di kode C++ sungguhan,",
                    "unordered_map justru yang paling sering kamu temui. Selain itu ada",
                    "stack, queue, deque, priority_queue, dan list. Semuanya muncul di",
                    "hampir semua kode algoritma, tapi jarang dijelaskan. Materi ini",
                    "membahas semuanya, supaya kamu nggak berhenti membaca gara-gara",
                    "ketemu baris '#include <queue>'.",
                    "",
                    "map dan unordered_map: bedanya cuma cara menyimpan",
                    "",
                    "Dua-duanya menyimpan pasangan key -> value, dan cara pakainya hampir",
                    "sama. Yang beda itu cara kerja di dalamnya:",
                    "",
                    "  map<K,V>            pohon biner seimbang. Key selalu tersusun",
                    "                      rapi menurut urutannya. Cari, sisip, hapus",
                    "                      O(log n). Header <map>.",
                    "  unordered_map<K,V>  tabel hash. Key dilempar ke 'ember' menurut",
                    "                      hasil hitungan hash, jadi posisinya terlihat",
                    "                      acak. Rata-rata O(1). Header <unordered_map>.",
                    "",
                    "O(1) rata-rata artinya begini: berapa pun banyak isinya, satu",
                    "pencarian butuh waktu yang kira-kira sama. Di map, tiap kali jumlah",
                    "datanya jadi dua kali lipat, pencariannya nambah satu langkah. Untuk",
                    "sepuluh data, bedanya nggak terasa. Untuk sejuta data, selisihnya",
                    "kelihatan.",
                    "",
                    "Kata \"rata-rata\" di situ memang perlu. Kalau banyak key kebetulan",
                    "jatuh ke ember yang sama, unordered_map bisa melambat sampai O(n).",
                    "Untuk key biasa seperti int dan string, hal itu praktis nggak pernah",
                    "terjadi.",
                    "",
                    "Pilih yang mana?",
                    "",
                    "Jadikan unordered_map pilihan awalmu. Kebanyakan kode cuma butuh",
                    "satu hal: dikasih key, kasih value-nya, dan cepat. Urutan key-nya",
                    "nggak dipakai untuk apa-apa.",
                    "",
                    "Pindah ke map cuma kalau salah satu dari ini berlaku:",
                    "  - Kamu perlu menelusuri isinya secara terurut, misalnya untuk",
                    "    mencetak laporan.",
                    "  - Kamu perlu key terkecil atau terbesar, atau \"key pertama yang",
                    "    >= X\" (lower_bound).",
                    "  - Key-nya tipe buatanmu sendiri. map cukup butuh operator<,",
                    "    sedangkan unordered_map butuh fungsi hash. Tanpa fungsi hash,",
                    "    kodenya gagal dikompilasi dengan pesan panjang sekali dari dalam",
                    "    std::hash. Pesan itu hampir mustahil dibaca kalau kamu nggak tahu",
                    "    penyebabnya.",
                    "",
                    "Jebakan: urutan isi unordered_map waktu ditelusuri nggak bisa",
                    "diandalkan.",
                    "",
                    "Urutan itu nggak dijamin siapa pun. Urutannya bisa berubah kalau",
                    "isinya bertambah, kalau compiler-nya beda, atau kalau versinya naik.",
                    "Program yang keluarannya kebetulan benar di komputermu bisa mencetak",
                    "urutan lain di komputer orang lain. Kalau keluaranmu harus urut,",
                    "pakai map, atau salin key-nya ke vector lalu sort(). Aturan yang sama",
                    "berlaku untuk unordered_set dan set.",
                ],
            },
            {
                "heading": "unordered_map & unordered_set - dan jebakan operator[]",
                "body": [
                    "Masalah operator[] ini berlaku untuk map dan unordered_map, dan bisa",
                    "kena siapa aja, termasuk yang udah lama ngoding. Misalnya kamu nulis m[\"key\"]",
                    "untuk key yang belum ada. Hasilnya bukan error, dan bukan juga",
                    "\"kosong\". m[\"key\"] bikin entri baru berisi nilai bawaan (0 untuk int,",
                    "string kosong untuk string), lalu mengembalikan entri itu. Jadi cuma",
                    "dengan membaca lewat [], map-mu ikut bertambah isinya tanpa kamu",
                    "sadari. Perhatikan angka size() di contoh bawah.",
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
                    "Ketiganya disebut adaptor, karena mereka bukan container baru. Isinya",
                    "tetap disimpan di deque atau vector. Yang dilakukan adaptor adalah",
                    "menutup semua operasi lain, dan cuma menyisakan yang masuk akal untuk",
                    "struktur itu. Itu memang gunanya. Siapa pun yang membaca",
                    "'stack<int> s' langsung tahu nggak ada data yang bisa nyelip ke",
                    "tengah tumpukan.",
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
                    "Ada juga bentuk min-heap, yaitu yang keluar duluan justru yang",
                    "terkecil. Bentuk ini ditulis lengkap dengan tiga argumen:",
                    "",
                    "    priority_queue<int, vector<int>, greater<int>> antre;",
                    "",
                    "Argumen kedua itu container penyimpannya. Kamu tetap harus",
                    "menulisnya walaupun nilainya sama dengan bawaan, karena di C++ nggak",
                    "ada cara melompati argumen di tengah. greater<int> berasal dari",
                    "<functional>. Bentuk ini dipakai algoritma Dijkstra dan \"ambil N",
                    "terkecil\", jadi kamu bakal sering lihat bentuk persis seperti itu.",
                    "",
                    "Jebakan: pop() nggak mengembalikan nilai.",
                    "",
                    "  int x = s.pop();   // SALAH, gagal kompilasi - pop() bertipe void",
                    "  int x = s.top();   // benar: lihat dulu",
                    "  s.pop();           // lalu buang",
                    "",
                    "Ini disengaja. Misalkan pop() mengembalikan salinan nilainya, lalu",
                    "proses penyalinan itu melempar exception. Elemennya udah telanjur",
                    "dihapus, dan datanya hilang tanpa bisa diselamatkan. Kalau dipisah",
                    "jadi dua langkah, nggak ada keadaan setengah jadi.",
                    "",
                    "Hal kedua yang sering salah: memanggil top() atau front() pada wadah",
                    "kosong. Hasilnya undefined behavior, artinya perilakunya nggak bisa",
                    "ditebak. Nggak ada exception, nggak ada pesan apa pun. Kamu bisa dapat",
                    "angka sampah, atau crash yang muncul jauh dari sumbernya. Selalu jaga",
                    "dengan while (!s.empty()).",
                    "",
                    "Hal ketiga: adaptor nggak punya begin() dan end(). Jadi adaptor",
                    "nggak bisa dipakai di range-based for, dan nggak bisa dipakai di",
                    "fungsi <algorithm>. Satu-satunya cara melihat seluruh isinya adalah",
                    "dengan mengosongkannya. Kalau kamu perlu menelusuri isinya berulang",
                    "kali, berarti container yang kamu pilih memang salah.",
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
                    "deque<T> (dibaca 'dek', dari double-ended queue, header <deque>) itu",
                    "seperti vector yang juga bisa tumbuh di depan, lewat push_front dan",
                    "pop_front. vector nggak punya dua fungsi itu. Kalau kamu menyisipkan",
                    "di awal vector, seluruh isinya harus bergeser satu per satu. deque",
                    "juga yang dipakai stack dan queue sebagai penyimpan bawaannya.",
                    "",
                    "list<T> (header <list>) itu doubly linked list, yaitu rantai elemen",
                    "yang masing-masing tahu tetangga depan dan belakangnya. Menyisipkan",
                    "atau menghapus di tengah cuma perlu menyambung ulang dua penunjuk.",
                    "Tapi itu berlaku kalau kamu udah memegang posisi elemennya. Mencari",
                    "posisi itu tetap harus ditelusuri dari ujung. list juga sama sekali",
                    "nggak punya akses index: l[3] nggak ada.",
                    "",
                    "Tiap elemen list dialokasikan terpisah, jadi isinya berserakan di",
                    "memori. Prosesor kehilangan keuntungan membaca data yang letaknya",
                    "berdampingan. Hasilnya sering bikin kaget: untuk data berukuran",
                    "wajar, vector lebih cepat daripada list, bahkan di operasi yang",
                    "secara teori dimenangkan list. Pakai list cuma kalau kamu sering",
                    "menyunting di tengah sambil udah memegang iteratornya, atau butuh",
                    "splice untuk memindahkan potongan antar list. Kalau ragu, pakai",
                    "vector.",
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
                    "Semua container di atas mengurus memorinya sendiri, dan",
                    "membebaskannya waktu keluar scope. Kamu nggak perlu nulis satu pun",
                    "delete.",
                    "",
                    "Salah yang paling sering terjadi justru bukan salah pilih antara map",
                    "dan unordered_map. Yang lebih sering: semuanya dipaksa pakai",
                    "vector, lalu isinya dicari pakai loop manual di setiap tempat.",
                    "Padahal dari awal yang dibutuhkan itu sebuah map.",
                ],
            },
        ],
    },
    {
        "title": "24. Iterator: Menelusuri & Menyunting Container",
        "sections": [
            {
                "body": [
                    "Iterator itu penunjuk posisi di dalam container. Kamu bakal sering",
                    "lihat .begin() dan .end(), misalnya di materi Algorithm sesudah ini,",
                    "yang cuma dioper begitu aja ke sort atau find. Padahal dua-duanya",
                    "mengembalikan nilai biasa, dan nilai itu boleh kamu simpan di",
                    "variabel sendiri. Nilai itulah yang disebut iterator.",
                    "",
                    "  auto it = v.begin();   // it menunjuk elemen PERTAMA",
                    "  cout << *it;           // *it = nilai di posisi itu (deref)",
                    "  *it = 99;              // *it boleh jadi SASARAN penugasan juga",
                    "  ++it;                  // geser it ke posisi berikutnya",
                    "",
                    "end() itu bukan elemen terakhir. end() adalah posisi satu langkah",
                    "sesudah elemen terakhir. Anggap aja garis finis yang sengaja nggak",
                    "berisi apa-apa. Akibatnya ada dua hal yang perlu kamu ingat:",
                    "  - Syarat loop-nya selalu it != v.end(), bukan it <= v.end().",
                    "  - *v.end() itu undefined behavior, artinya hasilnya nggak bisa",
                    "    ditebak. Biasanya nggak crash, cuma ngasih angka sampah. Bug",
                    "    seperti ini paling lama dicari.",
                    "",
                    "Kalau elemennya objek, struct, atau pair, pakai it->anggota sebagai",
                    "singkatan dari (*it).anggota. Aturan ini udah kamu kenal dari pointer",
                    "di materi Referensi.",
                    "",
                    "Kenapa bentuk panjang for (auto it = v.begin(); it != v.end(); ++it)",
                    "masih banyak ditemui di kode sungguhan? Sebelum C++11 belum ada",
                    "range-based for, dan belum ada auto. Jadi dulu, cuma cara itu yang",
                    "bisa dipakai untuk menelusuri map atau list. Kode lama jarang ditulis",
                    "ulang, jadi kamu bakal terus membacanya.",
                    "",
                    "Sebaliknya, for (auto &x : v) juga bukan cara yang berbeda. Compiler",
                    "menerjemahkannya jadi loop iterator seperti di atas. Makanya container",
                    "apa pun yang punya begin() dan end() otomatis bisa dipakai di",
                    "range-based for.",
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
                    "Di map, iterator menunjuk sebuah pair, jadi:",
                    "  it->first  -> KUNCInya. Bertipe const: mengubahnya akan merusak",
                    "                urutan map, sehingga compiler langsung menolak.",
                    "  it->second -> NILAInya. Ini boleh diubah: it->second = 90;",
                    "",
                    "Materi sebelumnya ngecek ada tidaknya kunci pakai m.count(kunci). Itu",
                    "benar. Tapi kalau sesudah itu kamu masih butuh nilainya, map dicari",
                    "dua kali: sekali oleh count, sekali lagi oleh m[kunci]. Bentuk baku",
                    "yang dipakai di mana-mana cukup mencari sekali, lalu langsung memakai",
                    "hasil pencariannya:",
                    "",
                    "  auto it = m.find(kunci);",
                    "  if (it != m.end()) {",
                    "      cout << it->first << \" = \" << it->second;",
                    "  } else {",
                    "      cout << \"tidak ada\";",
                    "  }",
                    "",
                    "Jebakan: operator[] bisa bikin data hantu.",
                    "",
                    "m[kunci] pada map nggak cuma membaca. Kalau kuncinya belum ada, dia",
                    "bikin entri baru berisi nilai bawaan (0 untuk int, string kosong",
                    "untuk string), lalu mengembalikan entri itu. Nggak ada error, dan",
                    "compiler nggak ngasih peringatan.",
                    "",
                    "Akibatnya di kode sungguhan:",
                    "  - if (m[\"Dedi\"] == 0) menambah satu anggota ke map, cuma karena",
                    "    kuncinya dicek.",
                    "  - Loop yang ngecek 1000 kunci bisa bikin map membengkak jadi 1000",
                    "    entri.",
                    "  - Laporan \"jumlah siswa\" jadi salah. Penyebabnya ada di baris yang",
                    "    kelihatannya cuma membaca, makanya bug ini susah dicurigai.",
                    "  - Pada map yang const, m[kunci] malah nggak bisa dikompilasi,",
                    "    karena operator itu memang boleh mengubah isi.",
                    "",
                    "Pegangan amannya: pakai find() untuk ngecek dan membaca. Pakai []",
                    "cuma kalau kamu memang mau menulis (m[kunci] = nilai). Kalau cuma",
                    "mau tahu ada atau nggak, count() tetap paling ringkas. Mulai C++20",
                    "ada juga m.contains(kunci), yang maksudnya lebih jelas.",
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
                    "Menghapus elemen sambil menelusuri itu tempat orang paling sering",
                    "salah. Kesalahannya nggak muncul sebagai pesan error. Yang muncul",
                    "program yang kadang benar, kadang nggak.",
                    "",
                    "Penyebabnya begini. Begitu sebuah elemen dihapus, iterator yang",
                    "menunjuk elemen itu nggak sah lagi. Kalau kamu nulis ++it sesudah",
                    "v.erase(it), kamu menggeser penunjuk yang udah mati. Makanya erase()",
                    "mengembalikan iterator ke elemen berikutnya. Bentuk yang benar",
                    "memastikan iteratornya nggak maju dua kali:",
                    "",
                    "  it = v.erase(it);   // kalau menghapus: pakai kembalian erase",
                    "  ++it;               // kalau TIDAK menghapus: baru maju sendiri",
                    "",
                    "Perhatikan bagian ketiga for-nya dikosongkan:",
                    "  for (auto it = v.begin(); it != v.end(); )",
                    "",
                    "Kalau ++it tetap ditulis di situ, tiap kali ada yang dihapus, satu",
                    "elemen sesudahnya bakal terlewat. Misalnya kamu menghapus angka",
                    "genap, dan ada dua angka genap berurutan. Salah satunya lolos tanpa",
                    "ketahuan.",
                    "",
                    "Ada juga hal lain yang bikin iterator nggak sah, dan sering",
                    "terlupa:",
                    "  - vector: push_back, insert, atau resize bisa memindahkan seluruh",
                    "    isinya ke blok memori baru kalau kapasitasnya habis. Begitu itu",
                    "    terjadi, semua iterator lama (termasuk end()) langsung nggak sah.",
                    "    Bahayanya, kalau kapasitasnya kebetulan masih cukup, kodenya",
                    "    kelihatan jalan normal. Jadi bug ini baru muncul waktu datanya",
                    "    membesar.",
                    "  - map dan set: cuma iterator ke elemen yang dihapus yang jadi nggak",
                    "    sah. Sisanya tetap sah.",
                    "",
                    "for (auto &x : v) juga loop iterator. Jadi menambah elemen ke v di",
                    "dalam loop itu bug yang sama persis, cuma lebih susah dilihat karena",
                    "iteratornya disembunyikan.",
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
                    "<algorithm> berisi fungsi siap pakai untuk pekerjaan yang umum pada",
                    "container, misalnya vector dan array. Dengan fungsi-fungsi ini, kamu",
                    "nggak perlu nulis loop manual yang sama berulang-ulang.",
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
                    ".begin() dan .end() itu iterator, yaitu penunjuk posisi. .begin()",
                    "menunjuk elemen pertama, dan .end() menunjuk satu langkah sesudah",
                    "elemen terakhir. Hampir semua fungsi algorithm di STL memakai",
                    "keduanya.",
                ]
            },
            {
                "heading": "find_if, for_each & accumulate yang berlambda",
                "body": [
                    "Daftar tadi masih kurang. Tiga bentuk berikut muncul di hampir semua",
                    "kode yang memakai <algorithm>, dan dua di antaranya bakal kamu",
                    "butuhkan begitu masuk latihan.",
                    "",
                    "find_if(begin, end, syarat)",
                    "",
                    "find mencari nilai yang persis sama. find_if mencari elemen pertama",
                    "yang memenuhi syarat. Yang dikembalikan itu iterator, bukan elemennya",
                    "dan bukan juga posisinya. Bentuk lengkapnya selalu dua baris ini,",
                    "dan jangan pernah dipotong jadi satu:",
                    "",
                    "    auto it = find_if(v.begin(), v.end(), [](int n) { return n > 7; });",
                    "    if (it != v.end()) { cout << *it; }      // WAJIB dicek dulu",
                    "",
                    "Kalau pengecekan '!= end()' dilewati lalu kamu langsung nulis *it,",
                    "hasilnya undefined behavior waktu nggak ada yang cocok. Biasanya",
                    "programnya nggak crash, cuma ngasih angka sampah. Bug seperti ini",
                    "paling lama dicari.",
                    "",
                    "for_each(begin, end, aksi)",
                    "",
                    "for_each menjalankan aksi untuk tiap elemen. Nilai kembaliannya",
                    "nggak berguna, jadi gunanya cuma menyingkat loop. Sejak ada",
                    "range-based for, for_each lebih sering kamu baca di kode orang",
                    "daripada kamu tulis sendiri.",
                    "",
                    "accumulate dengan empat argumen",
                    "",
                    "Bentuk tiga argumen di contoh atas cuma bisa menjumlah. Argumen",
                    "keempat menerima lambda, yaitu fungsi kecil tanpa nama. Dengan itu,",
                    "accumulate bisa menggabungkan apa aja: mengalikan, menghitung yang",
                    "memenuhi syarat, atau merangkai teks.",
                    "",
                    "    accumulate(begin, end, nilaiAwal, [](Hasil sejauhIni, Elemen e) {",
                    "        return <hasil gabungan yang baru>;",
                    "    });",
                    "",
                    "Peran dua parameter lambda-nya gampang tertukar, jadi hafalkan:",
                    "  - Parameter pertama itu akumulator, yaitu hasil sementara yang terus",
                    "    dibawa. Di putaran pertama isinya nilaiAwal.",
                    "  - Parameter kedua itu elemen yang sedang dikunjungi.",
                    "  - Nilai yang dikembalikan jadi akumulator untuk putaran berikutnya.",
                    "",
                    "Kalau tertukar, hasilnya salah tanpa satu pun pesan error.",
                    "",
                    "Terakhir, ada satu bentuk yang cukup kamu kenali dulu, belum perlu",
                    "dimengerti: greater<int>() yang jadi argumen ketiga sort di contoh",
                    "atas. Perhatikan tanda kurung di ujungnya. Yang dioper ke sort itu",
                    "bukan nama fungsi. Ada sesuatu yang dibuat di situ. Pasangannya,",
                    "less<int>(), adalah urutan bawaan sort. Benda apa itu, dan kenapa dia",
                    "boleh dipanggil seperti fungsi, dibahas di materi Functor &",
                    "std::function.",
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
                    "Smart pointer (mulai C++11, dari <memory>) mengurus memori secara",
                    "otomatis. Kamu nggak perlu nulis delete sendiri lagi. Ini menjawab",
                    "masalah utama new/delete manual, yang sama dengan masalah malloc/free",
                    "di C: lupa delete bikin memory leak, dan delete dua kali bikin crash.",
                    "",
                    "Ada dua jenis yang paling sering dipakai.",
                    "",
                    "unique_ptr<T> artinya kepemilikan tunggal. Cuma boleh ada satu",
                    "unique_ptr yang \"memiliki\" sebuah objek pada satu waktu. Objeknya",
                    "otomatis di-delete waktu unique_ptr itu keluar dari scope, yaitu",
                    "waktu blok kurung kurawal tempat dia dibuat selesai. unique_ptr nggak",
                    "bisa disalin, cuma bisa dipindah (move).",
                    "",
                    "shared_ptr<T> artinya kepemilikan bersama. Boleh ada banyak shared_ptr",
                    "yang menunjuk objek yang sama. Dia menghitung ada berapa shared_ptr",
                    "yang sedang menunjuk objek itu. Cara ini disebut reference counting.",
                    "Objeknya baru dihapus otomatis waktu shared_ptr terakhir yang",
                    "menunjuknya keluar dari scope.",
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
                    "Pegangan utama di C++ modern: hindari new dan delete manual. Untuk",
                    "dynamic memory allocation, selalu pakai smart pointer lewat",
                    "make_unique atau make_shared. Dengan begitu, sebagian besar bug memory",
                    "leak dan dangling pointer yang umum di kode C/C++ lama nggak bakal",
                    "muncul. Dangling pointer itu pointer yang masih menunjuk ke objek",
                    "yang udah dihapus.",
                    "",
                    "Kapan pakai unique_ptr, kapan shared_ptr?",
                    "  - unique_ptr jadi pilihan pertama. Pakai waktu pemiliknya jelas cuma",
                    "    satu. Ini kasus yang paling umum, dan beban tambahannya paling",
                    "    kecil.",
                    "  - shared_ptr cuma dipakai kalau memang butuh banyak pemilik yang sah",
                    "    atas objek yang sama. Ada beban tambahan untuk reference counting,",
                    "    jadi sedikit lebih lambat daripada unique_ptr.",
                ]
            },
            {
                "heading": "Menyeberang antara PEMILIK dan PEMINJAM",
                "body": [
                    "Smart pointer memisahkan dua peran yang di C selalu tercampur. Ada",
                    "yang memiliki objek, artinya bertanggung jawab menghapusnya. Ada juga",
                    "yang cuma meminjam, artinya memakainya sebentar lalu selesai. Tiga",
                    "method berikut jadi pintu di antara dua peran itu:",
                    "  - .get() mengembalikan raw pointer (pointer biasa) di dalamnya untuk",
                    "    dipinjam. Kepemilikannya nggak pindah. Smart pointer-nya tetap",
                    "    yang nanti menghapus objek itu. Ini dipakai kalau kamu harus",
                    "    memanggil fungsi lama yang parameternya masih T*.",
                    "  - .reset() melepas isinya saat itu juga, jadi objeknya langsung",
                    "    dihapus tanpa nunggu keluar scope. Smart pointer-nya jadi kosong",
                    "    dan boleh dipakai lagi.",
                    "  - .release() melepas kepemilikan tanpa menghapus apa pun. Dia",
                    "    menyerahkan raw pointer-nya, lalu mengosongkan diri. Mulai saat",
                    "    itu, kamu yang wajib men-delete objeknya. Fungsi ini jarang",
                    "    dibutuhkan. Kalau kamu merasa perlu, biasanya yang kamu maksud",
                    "    adalah std::move ke pemilik baru.",
                    "",
                    "Jebakan: hasil .get() jangan dimasukkan ke smart pointer lain, dan",
                    "jangan di-delete sendiri. Dua-duanya bikin objek yang sama dihapus dua",
                    "kali.",
                    "",
                    "Cara mengoper smart pointer ke fungsi bisa diringkas jadi tiga baris",
                    "ini:",
                    "",
                    "  void pakai(const Mahasiswa &m)   // cuma MEMBACA objeknya",
                    "  void pakai(Mahasiswa *m)         // boleh mengubah, boleh null",
                    "  void ambilAlih(unique_ptr<Mahasiswa> m)   // KEPEMILIKAN pindah",
                    "",
                    "Fungsi yang cuma memakai objek sebaiknya nggak menyebut unique_ptr",
                    "atau shared_ptr sama sekali. Minta reference atau raw pointer aja,",
                    "supaya fungsinya bisa dipakai untuk objek dari mana pun asalnya.",
                    "",
                    "Cuma fungsi yang memang mengambil alih kepemilikan yang meminta",
                    "unique_ptr utuh. Pemanggilnya wajib menulis std::move. Tanpa itu",
                    "compiler menolak, karena unique_ptr memang nggak bisa disalin.",
                    "",
                    "weak_ptr, anggota ketiga keluarga ini",
                    "",
                    "shared_ptr punya satu kelemahan: siklus. Misalnya A memegang",
                    "shared_ptr ke B, dan B memegang shared_ptr ke A. Hitungan keduanya",
                    "nggak pernah sampai nol, karena mereka saling menahan. Akibatnya",
                    "dua-duanya bocor, walaupun udah nggak ada yang memakainya. Bentuk yang",
                    "paling sering kena adalah hubungan parent-child, dan observer yang",
                    "menyimpan pointer balik ke objek yang diamatinya.",
                    "",
                    "weak_ptr<T> menunjuk objek tanpa ikut memiliki. Dia nggak menambah",
                    "hitungan referensi, jadi dia nggak bisa menahan objek tetap hidup.",
                    "Cara memutus siklusnya: jadikan satu arah aja yang shared_ptr (parent",
                    "ke child), dan arah baliknya weak_ptr.",
                    "",
                    "Objek yang ditunjuk weak_ptr bisa aja udah terhapus. Makanya weak_ptr",
                    "nggak boleh langsung dipakai. Kamu harus minta izin dulu lewat",
                    ".lock():",
                    "",
                    "  if (auto p = w.lock()) { ... }   // p = shared_ptr sementara",
                    "",
                    "Kalau objeknya masih hidup, .lock() ngasih shared_ptr yang menjaga",
                    "objek itu tetap hidup selama blok tersebut. Kalau udah terhapus, dia",
                    "ngasih shared_ptr kosong, dan bloknya dilewati. Jadi nggak ada",
                    "dangling pointer dan nggak ada crash. Kalau kamu cuma mau tahu",
                    "objeknya masih hidup atau nggak, ada juga w.expired().",
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
                    "Exception itu cara program melaporkan kesalahan, dengan \"melempar\"",
                    "sinyal error yang nanti \"ditangkap\" di tempat lain. Di C++ caranya",
                    "mirip Java: try, catch, dan throw. C nggak punya mekanisme bawaan",
                    "seperti ini. Di C, error biasanya ditandai lewat return code, yaitu",
                    "nilai kembalian khusus.",
                    "",
                    "  try {",
                    "      // kode yang mungkin error",
                    "  } catch (TipeException &e) {",
                    "      // penanganan error",
                    "  }",
                    "",
                    "<stdexcept> menyediakan beberapa class exception bawaan:",
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
                    "Kalau kamu menangkap lewat base class (exception &e), semua jenis",
                    "exception turunannya ikut tertangkap. Ini berguna untuk menangkap",
                    "semuanya sekaligus. Tapi kalau cara menangani tiap jenis error",
                    "berbeda, tangkap dulu tipe yang spesifik.",
                    "",
                    "Satu konsep yang perlu kamu pahami di sini namanya RAII (Resource",
                    "Acquisition Is Initialization). Di C++, exception aman dipakai bareng",
                    "smart pointer dan objek STL. Alasannya, destructor tetap dipanggil",
                    "walaupun terjadi exception. Proses ini disebut stack unwinding, dan",
                    "terjadi otomatis. Di C beda: kamu harus membereskan sendiri semua",
                    "sumber daya di setiap jalur keluar fungsi.",
                ]
            },
            {
                "heading": "Membongkar baris 'const char* what() const noexcept override'",
                "body": [
                    "Baris itu ada di contoh atas, dan baris ini yang paling sering bikin",
                    "orang menyerah. Lima kata asing berderet sekaligus. Kita baca dari kiri",
                    "ke kanan, satu per satu:",
                    "  - const char* adalah tipe kembaliannya: pointer ke teks gaya C yang",
                    "    nggak boleh diubah. Tipenya bukan std::string, makanya isinya",
                    "    dikembalikan pakai .c_str().",
                    "  - what() adalah namanya. Harus persis ini, karena nama itu yang",
                    "    dipakai std::exception.",
                    "  - const artinya method ini nggak mengubah objeknya. Kamu udah ketemu",
                    "    ini di materi Encapsulation.",
                    "  - noexcept adalah janji bahwa fungsi ini nggak akan melempar",
                    "    exception.",
                    "  - override menegaskan bahwa method ini menimpa method virtual milik",
                    "    base class. Compiler bakal protes kalau tanda tangannya ternyata",
                    "    nggak cocok.",
                    "",
                    "Yang betul-betul baru di situ cuma noexcept. Artinya sesederhana janji",
                    "tadi. Tapi kamu perlu tahu akibatnya. Kalau fungsi ber-noexcept",
                    "ternyata tetap melempar, program langsung dihentikan paksa",
                    "(std::terminate). Nggak ada catch yang bisa menyelamatkannya. Jadi",
                    "noexcept itu jaminan, nggak sekadar permintaan.",
                    "",
                    "Kenapa what() harus pakai noexcept? Versi what() di base class-nya",
                    "udah ber-noexcept. Aturan override melarang versi turunan jadi lebih",
                    "longgar daripada yang ditimpanya. Kalau noexcept di situ dihapus,",
                    "compiler langsung menolak. Jadi kata itu nggak perlu dihafal kayak",
                    "mantra. Dia ada karena base class-nya menuntut begitu.",
                    "",
                    "noexcept bakal kamu temui lagi di materi RAII & Move Semantics. Di",
                    "sana dia ikut menentukan performa.",
                ],
            },
            {
                "heading": "catch (...), lempar ulang & satu larangan keras",
                "body": [
                    "Ada dua bentuk lagi yang melengkapi try-catch.",
                    "",
                    "Yang pertama catch (...), dengan tiga titik di dalam kurung:",
                    "",
                    "  catch (...) { ... }",
                    "",
                    "Bentuk ini menangkap apa aja, termasuk yang dilempar bukan sebagai",
                    "turunan std::exception. Di C++ kamu boleh melempar int atau string",
                    "mentah, dan pustaka lama kadang begitu. Kekurangannya, kamu nggak",
                    "punya nama variabel, jadi nggak ada e.what() yang bisa dibaca. Kamu",
                    "tahu ada yang salah, tapi nggak tahu apa. Makanya catch (...) selalu",
                    "ditaruh paling bawah, sesudah catch yang spesifik. Dia jaring",
                    "pengaman, bukan penangan utama.",
                    "",
                    "Yang kedua throw; tanpa argumen:",
                    "",
                    "  throw;",
                    "",
                    "Kalau ditulis di dalam blok catch, artinya: lempar ulang exception",
                    "yang sedang kamu tangani, apa adanya. Ini beda dengan 'throw e;', yang",
                    "membuat salinan dan bisa kehilangan tipe aslinya. Bentuk ini dipakai",
                    "untuk pola \"catat lalu teruskan\". Lapisan bawah mencatat kejadiannya,",
                    "lalu lapisan atas yang memutuskan program lanjut atau berhenti.",
                    "",
                    "Jangan pernah biarkan destructor melempar exception.",
                    "",
                    "Waktu sebuah exception sedang naik mencari catch, C++ memanggil",
                    "destructor semua objek yang dilewatinya. Ini stack unwinding yang",
                    "disebut tadi. Kalau salah satu destructor itu ikut melempar, ada dua",
                    "exception aktif sekaligus, dan C++ menyerah. Program dihentikan paksa,",
                    "tanpa pesan yang berguna. Makanya mulai C++11, destructor otomatis",
                    "dianggap noexcept. Kalau di dalam destructor ada yang bisa gagal,",
                    "misalnya menutup berkas atau mengirim sisa data, tangkap sendiri di",
                    "situ pakai try-catch. Jangan biarkan exception-nya lolos keluar.",
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
                    "Sampai sekarang semua data programmu hilang begitu programnya",
                    "berhenti. cin dan cout cuma ngobrol dengan keyboard dan layar. Berkas",
                    "adalah tempat data tetap tersimpan sesudah program selesai, dan hampir",
                    "semua program sungguhan butuh itu.",
                    "",
                    "Alatnya cukup satu header: #include <fstream>. Isinya tiga tipe:",
                    "",
                    "  ofstream   output file stream  ->  MENULIS ke berkas",
                    "  ifstream   input file stream   ->  MEMBACA dari berkas",
                    "  fstream    baca DAN tulis sekaligus (jauh lebih jarang dipakai)",
                    "",
                    "Huruf depannya dibaca dari sudut pandang program, bukan dari sudut",
                    "pandang berkas. 'o' artinya data keluar dari program menuju berkas.",
                    "'i' artinya data masuk ke program dari berkas. Banyak orang tertukar",
                    "di sini waktu baru mulai.",
                    "",
                    "Kabar baiknya, ketiganya adalah stream, jenis benda yang sama dengan",
                    "cout dan cin. Semua yang udah kamu pelajari di materi Input/Output",
                    "Modern langsung berlaku apa adanya:",
                    "",
                    "  keluar << \"Halo\" << 42 << '\\n';   // persis seperti cout <<",
                    "  masuk >> nama >> nilai;           // persis seperti cin >>",
                    "  getline(masuk, baris);            // persis seperti getline(cin, s)",
                    "",
                    "Yang berganti cuma ujung salurannya. Dulu terminal, sekarang sebuah",
                    "berkas di disk.",
                    "",
                    "Berkasnya dibuka lewat constructor. Jadi mendeklarasikan dan membuka",
                    "cukup satu baris:",
                    "",
                    "  ofstream keluar(\"data.txt\");   // dibuka saat objeknya lahir",
                    "  ifstream masuk(\"data.txt\");",
                    "",
                    "Nama \"data.txt\" tanpa garis miring disebut path relatif. Relatifnya",
                    "terhadap folder tempat program dijalankan, bukan tempat berkas .cpp",
                    "atau programnya berada. Jadi program yang sama, kalau dijalankan dari",
                    "folder lain, bisa nggak menemukan berkas yang jelas-jelas ada.",
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
                    "Kenapa is_open() wajib dicek?",
                    "",
                    "C++ nggak melempar exception kalau sebuah berkas gagal dibuka.",
                    "Stream-nya cuma menyalakan tanda error di dalam dirinya. Sesudah itu,",
                    "setiap << dan >> nggak melakukan apa-apa, tanpa pemberitahuan.",
                    "Programnya jalan mulus sampai habis dan keluar dengan kode 0, seolah",
                    "semuanya baik-baik aja.",
                    "",
                    "  ofstream keluar(\"laporan/hasil.txt\");  // folder laporan/ tidak ada",
                    "  keluar << hasilKerjaSeharian;          // hilang, tanpa satu pesan pun",
                    "",
                    "Ini kegagalan yang paling susah ketahuan. Programnya nggak crash,",
                    "kelihatannya sukses, padahal nggak menyimpan apa pun. Biasanya kamu",
                    "sendiri yang baru sadar seminggu kemudian, waktu datanya dicari.",
                    "",
                    "Di sisi baca ada jebakan kembarannya. Kalau kamu cuma lihat loop-nya,",
                    "berkas kosong dan berkas yang nggak ada memberi hasil yang sama persis.",
                    "Dua-duanya bikin loop jalan nol kali:",
                    "",
                    "  berkas kosong     ->  is_open() true    (wajar, memang tak ada isi)",
                    "  berkas tidak ada  ->  is_open() false   (BUG: salah nama/salah folder)",
                    "",
                    "Bentuk ringkas yang juga sering kamu temui di kode orang lain:",
                    "",
                    "  if (!masuk) { ... }",
                    "",
                    "Artinya sama. Stream yang bermasalah bernilai false kalau dipakai",
                    "sebagai kondisi.",
                    "",
                    "Mode pembukaan adalah argumen kedua constructor:",
                    "  - Tanpa mode: ini bawaan ofstream. Berkas dibuat kalau belum ada, dan",
                    "    isi lamanya langsung dihapus habis begitu dibuka, bahkan kalau kamu",
                    "    nggak jadi menulis apa pun.",
                    "  - ios::app (append): tulisanmu ditambahkan di akhir, dan isi lama",
                    "    tetap utuh. Mode ini yang dipakai untuk berkas log.",
                    "  - ios::binary: data mentah, bukan teks, misalnya gambar atau berkas",
                    "    terkompresi.",
                    "",
                    "Soal close(): di C kamu wajib memanggil fclose(). Di C++ nggak perlu.",
                    "Destructor ifstream dan ofstream menutup berkasnya sendiri waktu",
                    "objeknya keluar dari scope. Itu termasuk waktu fungsi selesai lebih",
                    "awal lewat return, dan waktu sebuah exception melemparmu keluar dari",
                    "blok itu (materi sebelumnya). Pola ini namanya RAII. Materi RAII & Move",
                    "Semantics membahasnya lengkap, dan contoh FileLogger di sana persis",
                    "benda yang sedang kamu pakai sekarang.",
                    "",
                    "Tetap tulis close() sendiri dalam satu keadaan: kalau berkas itu mau",
                    "langsung dibuka lagi di program yang sama. Tulisan ke berkas mampir",
                    "dulu di buffer memori, dan baru dikirim ke disk waktu berkasnya",
                    "ditutup. Kalau kamu membaca ulang berkas yang masih terbuka untuk",
                    "ditulis, isinya bisa belum lengkap.",
                ],
            },
            {
                "heading": "Membaca kolom: operator >> dan istringstream",
                "body": [
                    "Berkas data jarang berisi kalimat bebas. Biasanya isinya berbentuk",
                    "kolom. Ada dua cara membacanya, dan kalau salah pilih, datamu terpotong",
                    "di tengah:",
                    "  - masuk >> nama >> nilai cocok kalau kolomnya dipisah spasi, dan",
                    "    nggak ada kolom yang isinya mengandung spasi. Alasannya, >>",
                    "    berhenti di spasi pertama.",
                    "  - getline lalu istringstream: baca satu baris utuh dulu, lalu pecah",
                    "    sendiri. Cara ini wajib untuk CSV, atau untuk kolom yang boleh",
                    "    berisi spasi.",
                    "",
                    "istringstream berasal dari <sstream> dan dibahas di materi String C++",
                    "Lebih Dalam & stringstream. Dia membungkus string biasa supaya string",
                    "itu bisa dibaca seperti stream.",
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
                    "Ada empat jebakan yang paling sering bikin orang jatuh:",
                    "",
                    "  1. while (!masuk.eof()). Jangan pernah nulis ini. eof() baru menyala",
                    "     sesudah sebuah pembacaan menabrak ujung berkas. Jadi loop-nya",
                    "     telanjur masuk satu kali lagi, dan putaran tambahan itu memproses",
                    "     data kosong. Tulis while (getline(masuk, baris)). Kondisinya",
                    "     adalah hasil pembacaan itu sendiri, jadi nggak ada putaran",
                    "     tambahan.",
                    "  2. Mencampur >> lalu getline. Ini sama persis dengan jebakan cin >>",
                    "     lalu getline(cin, s) di materi Input/Output Modern. >> berhenti",
                    "     tepat sebelum newline dan meninggalkan newline itu di stream. Jadi",
                    "     getline berikutnya langsung ketemu newline itu dan mengembalikan",
                    "     string kosong. Obatnya juga sama: panggil masuk.ignore() dulu",
                    "     sebelum getline.",
                    "  3. Membuka ofstream cuma untuk ngecek berkasnya ada atau nggak. Baru",
                    "     dibuka aja, isinya udah kosong. Untuk ngecek sebuah berkas ada",
                    "     atau nggak, buka pakai ifstream lalu lihat is_open().",
                    "  4. Lupa bahwa path-nya relatif ke folder tempat program dijalankan.",
                    "     Program yang jalan mulus dari terminalmu bisa gagal total kalau",
                    "     dijalankan dengan cara lain, walaupun programnya sama persis.",
                    "",
                    "Kalau dibandingkan dengan File I/O gaya C yang udah kamu pelajari:",
                    "",
                    "  C                              C++",
                    "  FILE *fp = fopen(\"a.txt\",\"r\"); ifstream masuk(\"a.txt\");",
                    "  if (fp == NULL) { ... }        if (!masuk.is_open()) { ... }",
                    "  fgets(buf, sizeof(buf), fp);   getline(masuk, baris);",
                    "  fprintf(fp, \"%d\\n\", n);        keluar << n << '\\n';",
                    "  fclose(fp);                    (otomatis saat objeknya keluar scope)",
                    "",
                    "Yang berkurang nggak cuma jumlah ketikan. Buffer berukuran tetap, yang",
                    "dulu sering jadi sumber buffer overflow, diganti string yang bisa",
                    "memanjang sendiri. Format specifier yang harus cocok dengan tipe",
                    "diganti operator yang udah tahu tipenya. fclose() yang wajib diulang",
                    "di setiap jalur keluar fungsi diganti destructor yang nggak mungkin",
                    "lupa.",
                ],
            },
        ],
    },
    {
        "title": "29. Lambda Expression & Fitur Modern C++",
        "sections": [
            {
                "body": [
                    "Lambda (mulai C++11) itu fungsi tanpa nama yang ditulis ringkas, tepat",
                    "di tempat dia dipakai. Mirip lambda di Python atau Java, dan arrow",
                    "function di JavaScript.",
                    "",
                    "  Sintaks: [capture](parameter) -> tipeKembali { isi }",
                    "",
                    "  auto tambah = [](int a, int b) { return a + b; };",
                    "  cout << tambah(3, 4);   // 7",
                    "",
                    "Bagian [capture] menentukan variabel dari luar lambda mana aja yang",
                    "boleh dipakai di dalamnya:",
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
                    "Ada beberapa fitur modern C++ lain (C++11 ke atas) yang sering",
                    "dipakai:",
                    "",
                    "  auto, type inference (compiler menebak tipenya sendiri):",
                    "    auto x = 10;              // int",
                    "    auto nama = string(\"Andi\"); // string",
                    "",
                    "  range-based for (C++11):",
                    "    for (int n : vektor) { ... }         // by value (salinan)",
                    "    for (int &n : vektor) { n *= 2; }     // by reference (bisa ubah)",
                    "    for (const auto &item : vektor) { ... } // paling umum: aman & efisien",
                    "",
                    "  nullptr (C++11) menggantikan NULL atau 0 untuk pointer kosong:",
                    "    int *ptr = nullptr;   // lebih type-safe dari NULL",
                    "",
                    "  structured bindings (C++17) untuk pair atau tuple:",
                    "    auto [nama, umur] = pasangan;   // langsung destructure",
                ]
            },
            {
                "heading": "Kosakata C++17 yang muncul di TANDA TANGAN fungsi",
                "body": [
                    "Fitur di atas boleh kamu lewati kalau nggak suka, karena cuma soal",
                    "cara menulis. Tiga tipe berikut lain cerita. Mereka muncul di tanda",
                    "tangan fungsi, yaitu baris yang menyebut nama fungsi, parameter, dan",
                    "tipe kembaliannya. Bagian itu nggak bisa dilewati waktu membaca. Begitu",
                    "kamu membuka kode C++ modern orang lain, ketiganya langsung muncul di",
                    "baris pertama.",
                    "",
                    "optional<T>: mungkin ada, mungkin nggak",
                    "",
                    "Fungsi cari() harus bisa menjawab \"nggak ketemu\". Cara lama:",
                    "kembalikan pointer, lalu kembalikan nullptr kalau nggak ada hasilnya.",
                    "Pemanggil yang lupa ngecek bakal kena crash. optional menyatakannya",
                    "terang-terangan di tanda tangan fungsi:",
                    "",
                    "    optional<Produk> cari(const vector<Produk> &rak, string nama);",
                    "",
                    "Isinya dicek dan diambil begini:",
                    "    if (hasil) { ... }        // atau hasil.has_value()",
                    "    hasil->nama               // seperti pointer",
                    "    hasil.value()             // melempar kalau ternyata kosong",
                    "    hasil.value_or(cadangan)  // nilai cadangan kalau kosong",
                    "",
                    "Untuk mengembalikan yang kosong, tulis 'return nullopt;'. Bedanya",
                    "dengan pointer, nggak ada memori yang dialokasikan. Kosong di sini",
                    "juga hal yang wajar, bukan tanda error atau kegagalan.",
                    "",
                    "string_view: parameter teks yang murah",
                    "",
                    "    void sapa(string_view teks);   // bukan const string&",
                    "",
                    "string_view cuma menyimpan alamat awal teks dan panjangnya. Dia cuma",
                    "melihat teksnya, nggak memiliki dan nggak menyalin. Untungnya ada dua.",
                    "Memanggil sapa(\"Andi\") dengan literal nggak lagi membuat objek string",
                    "baru di belakang layar. Potongan teks juga bisa dioper tanpa substr",
                    "yang menyalin.",
                    "",
                    "Jebakan: string_view nggak menjaga teks yang dilihatnya tetap hidup.",
                    "Kalau string aslinya keluar dari scope atau berubah, string_view-nya",
                    "menunjuk ke tempat yang udah nggak berlaku, persis seperti dangling",
                    "pointer. Sebagai parameter dia aman, karena teks aslinya jelas masih",
                    "hidup selama fungsinya jalan. Sebagai atribut class atau sebagai nilai",
                    "kembalian, dia berbahaya.",
                    "",
                    "variant<A, B> sekilas",
                    "",
                    "variant adalah satu variabel yang isinya boleh salah satu dari",
                    "beberapa tipe. Dia ingat sedang berisi tipe yang mana. Jadi beda",
                    "dengan union gaya C, yang bisa kamu baca dengan tipe yang salah. Cek",
                    "isinya dengan holds_alternative<T>(v), ambil dengan get<T>(v). variant",
                    "sering dipakai untuk \"hasil atau pesan kesalahan\".",
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
                    "Ada dua bentuk lambda yang belum dibahas, dan dua-duanya muncul di",
                    "contoh barusan.",
                    "",
                    "Yang pertama mutable, yaitu lambda yang boleh mengubah tangkapannya.",
                    "Tangkapan by value ([x]) bersifat const di dalam lambda. Kalau kamu",
                    "nulis 'x = 5;', compiler langsung menolak. Tambahkan 'mutable' sesudah",
                    "daftar parameter, dan larangan itu dicabut. Tapi yang berubah cuma",
                    "salinan milik lambda-nya. Variabel di luar tetap nggak tersentuh, dan",
                    "salinan itu bertahan dari satu pemanggilan ke pemanggilan berikutnya.",
                    "Makanya penghitung() di atas menghasilkan 1, 2, 3, sedangkan",
                    "'hitungan' di luar tetap 0.",
                    "",
                    "Yang kedua generic lambda, yaitu lambda dengan parameter bertipe auto.",
                    "Kalau kamu nulis 'auto' sebagai tipe parameter, compiler membuatkan",
                    "versi terpisah untuk tiap tipe yang dipakai. Persis seperti template",
                    "di materi Templates, tapi cukup satu baris.",
                    "",
                    "  auto cetak = [](const auto &x) { cout << x; };",
                    "",
                    "Ini berguna untuk lambda pembantu yang kamu pakai di beberapa jenis",
                    "container sekaligus, tanpa perlu menulis ulang tiga kali.",
                ]
            },
        ],
    },
    {
        "title": "30. Functor & std::function",
        "sections": [
            {
                "body": [
                    "Sejak materi STL: Algorithm Library, kamu udah nulis greater<int>()",
                    "untuk mengurutkan dari besar ke kecil. Tapi belum pernah dijelaskan",
                    "benda apa itu. Jawabannya: greater<int>() itu sebuah objek, bukan",
                    "fungsi.",
                    "",
                    "Functor (function object) adalah objek yang bisa dipanggil seperti",
                    "fungsi. Caranya, sebuah class meng-overload operator(), yaitu operator",
                    "\"panggil\". Operator ini cuma disebut sekilas di materi Operator",
                    "Overloading.",
                    "",
                    "  struct LebihBesar {",
                    "      bool operator()(int a, int b) const { return a > b; }",
                    "  };",
                    "",
                    "  LebihBesar bandingkan;        // MEMBUAT objek",
                    "  bandingkan(3, 1);             // MEMANGGIL objeknya -> true",
                    "",
                    "Baca pelan-pelan bentuk 'operator()(int a, int b)'. Pasangan () yang",
                    "pertama adalah nama operatornya. Pasangan () yang kedua baru daftar",
                    "parameter biasa. Makanya kurungnya kelihatan dobel.",
                    "",
                    "Kenapa repot begini, padahal fungsi biasa udah ada? Objek punya",
                    "sesuatu yang nggak dimiliki fungsi, yaitu anggota data. Functor bisa",
                    "menyimpan nilai di dalam dirinya, misalnya ambang batas, penghitung,",
                    "atau konfigurasi. Nilai itu dipakai lagi setiap kali dia dipanggil.",
                    "Fungsi biasa cuma punya parameternya. Begitu selesai dipanggil, nggak",
                    "ada yang tersisa.",
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
                    "Functor bawaan ada di header <functional>. Semuanya class template,",
                    "jadi selalu ada <tipe> di belakang namanya:",
                    "",
                    "  less<int>       -> a < b    (BAWAAN sort, map, set)",
                    "  greater<int>    -> a > b    (dipakai untuk urutan menurun)",
                    "  equal_to<int>   -> a == b",
                    "  plus<int>       -> a + b",
                    "  hash<string>    -> ubah nilai jadi angka; inilah yang dipakai",
                    "                     unordered_map untuk memilih ember",
                    "",
                    "Dua bentuk ini gampang banget tertukar:",
                    "",
                    "  greater<int>     -> sebuah TIPE (nama classnya)",
                    "  greater<int>()   -> sebuah OBJEK (hasil pembuatan dari class itu)",
                    "",
                    "sort() minta objek pembanding, jadi ada () di belakangnya. Container",
                    "minta tipenya sebagai parameter template, jadi tanpa ():",
                    "",
                    "  sort(v.begin(), v.end(), greater<int>());           // objek",
                    "  map<string, int, greater<string>> m;                // tipe",
                    "  priority_queue<int, vector<int>, greater<int>> pq;  // tipe",
                    "",
                    "Kalau sepasang kurung di situ ketinggalan atau kelebihan, kamu bakal",
                    "dapat salah satu pesan error terpanjang di C++. Sejak C++14, tipenya",
                    "boleh dikosongkan, cukup greater<>, dan compiler menebak sendiri.",
                    "",
                    "Lambda itu functor, dalam arti harfiah. Di belakang layar, compiler",
                    "membuatkan sebuah class yang punya operator(). Variabel yang kamu",
                    "tangkap lewat [capture] jadi anggota data class itu. Di mata compiler,",
                    "dua bentuk ini sama persis:",
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
                    "Jadi lambda cuma cara singkat menulis functor. Ini juga menjelaskan",
                    "kenapa tiap lambda punya tipe yang berbeda, walaupun isinya sama. Dua",
                    "class yang berbeda tetap dua tipe yang berbeda. Karena tipenya nggak",
                    "punya nama yang bisa kamu tulis, lambda biasanya ditampung pakai",
                    "'auto'.",
                ],
            },
            {
                "heading": "std::function: menyimpan dan mengoper fungsi",
                "body": [
                    "Sampai sini, setiap fungsi selalu langsung dipakai di tempat. Padahal",
                    "kode sungguhan sering perlu menyimpan sebuah fungsi dulu, lalu",
                    "memanggilnya nanti. Misalnya waktu tombol diklik, waktu data selesai",
                    "dimuat, atau waktu perintah tertentu diketik. Untuk itu kamu butuh",
                    "sebuah tipe, dan 'auto' nggak bisa dipakai sebagai tipe anggota class",
                    "atau tipe parameter.",
                    "",
                    "std::function<void(int)> adalah tipe itu. Bacanya dari dalam ke luar:",
                    "\"apa aja yang bisa dipanggil dengan satu int dan nggak mengembalikan",
                    "apa-apa\". Yang bisa masuk ke situ misalnya pointer fungsi biasa,",
                    "functor, dan lambda.",
                    "",
                    "Contoh di bawah memakainya di tiga tempat sekaligus. Pertama sebagai",
                    "variabel. Kedua sebagai isi map, jadi semacam tabel handler. Ketiga",
                    "sebagai parameter constructor yang lalu disimpan jadi anggota class.",
                    "Pola yang terakhir disebut callback, yaitu fungsi yang kamu titipkan",
                    "supaya dipanggil belakangan. Bentuknya sama di hampir semua API C++.",
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
                    "Kesalahan yang sering terjadi:",
                    "",
                    "  - Lupa #include <functional>. Di sebagian compiler, greater<int>()",
                    "    tetap jalan karena ikut terbawa <algorithm>. Lalu programnya gagal",
                    "    dikompilasi di komputer orang lain. Tulis include-nya sendiri.",
                    "",
                    "  - Memanggil std::function yang masih kosong. Dia melempar exception",
                    "    std::bad_function_call, nggak cuma diam. Cek dulu dengan 'if (f)',",
                    "    seperti di class Tombol di atas.",
                    "",
                    "  - Menyimpan lambda ber-[&] ke dalam std::function yang umurnya lebih",
                    "    panjang daripada variabel yang ditangkap. Anggota datanya jadi",
                    "    referensi ke memori yang udah mati. Programnya tetap jalan, cuma",
                    "    hasilnya salah, tanpa satu pun error. Untuk callback yang disimpan,",
                    "    tangkap by value ([x] atau [=]).",
                    "",
                    "  - Memakai std::function padahal auto udah cukup. std::function",
                    "    menyimpan isinya di balik satu lapis perantara, jadi ada biaya",
                    "    kecil setiap kali dipanggil. Untuk lambda yang langsung dioper ke",
                    "    sort atau count_if, biarkan pakai auto atau template. Pakai",
                    "    std::function kalau isinya memang harus bisa berganti, atau harus",
                    "    disimpan di anggota class atau container.",
                    "",
                    "  - Mengira parameter std::function artinya \"harus lambda\". Yang",
                    "    dicocokkan itu bentuk panggilannya, bukan asal-usulnya. Nama fungsi",
                    "    biasa pun langsung diterima, seperti 'f = sapa;'.",
                ],
            },
        ],
    },
    {
        "title": "31. RAII & Move Semantics (Lanjutan)",
        "sections": [
            {
                "body": [
                    "RAII (Resource Acquisition Is Initialization) adalah prinsip yang",
                    "paling sering kamu pakai di C++ modern. Idenya: umur sebuah resource",
                    "diikat ke umur sebuah objek. Resource itu apa pun yang harus diambil",
                    "lalu dikembalikan, misalnya memori, file, koneksi, atau lock.",
                    "  - Resource diambil di constructor.",
                    "  - Resource dilepas di destructor.",
                    "  - Destructor otomatis dipanggil waktu objek keluar dari scope,",
                    "    bahkan waktu ada exception. Jadi resource-nya nggak pernah bocor.",
                    "    Cara ini yang dipakai smart pointer, vector, string, dan",
                    "    fstream, makanya semuanya bekerja tanpa perlu dibereskan manual.",
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
                    "Move semantics (mulai C++11, konsep lanjutan) adalah cara memindahkan",
                    "resource dari satu objek ke objek lain tanpa menyalin datanya. Menyalin",
                    "data besar itu mahal. Alatnya adalah rvalue reference (&&).",
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
                    "Move semantics memang topik lanjutan. Untuk pemula, cukup pahami satu",
                    "hal: C++ modern otomatis mengoptimalkan banyak kasus \"mengembalikan",
                    "objek besar dari fungsi\", tanpa kamu perlu nulis kode tambahan.",
                ]
            },
            {
                "heading": "Tanda tangan yang selama ini disembunyikan",
                "body": [
                    "Sejauh ini move semantics selalu diceritakan dari sisi pemakai: vector",
                    "dan string udah tahu cara memindahkan dirinya. Tapi mereka tahu dari",
                    "mana? Ada orang yang menuliskan dua anggota ini di dalamnya, dan",
                    "bentuknya belum pernah kamu lihat:",
                    "",
                    "  Buffer(Buffer &&lain) noexcept;              // move constructor",
                    "  Buffer& operator=(Buffer &&lain) noexcept;   // move assignment",
                    "",
                    "Ada tiga bagian yang perlu dibaca pelan-pelan:",
                    "  - && adalah rvalue reference, artinya \"objek yang nggak bakal dipakai",
                    "    lagi\". Isinya boleh kamu bongkar, karena pemiliknya memang sedang",
                    "    menyerahkannya. Entah karena dia objek sementara, entah karena",
                    "    ditandai std::move.",
                    "  - &lain. Bandingkan dengan copy constructor yang menerima 'const",
                    "    Buffer &lain'. Di sini nggak ada const, dan memang nggak boleh ada,",
                    "    karena pekerjaan move justru mengubah sumbernya.",
                    "  - noexcept artinya fungsi ini dijamin nggak melempar exception. Kata",
                    "    ini yang menentukan apakah vector mau memakai move-mu atau nggak.",
                    "    Penjelasannya ada di bawah.",
                    "",
                    "Isinya selalu ikut pola yang sama: ambil, lalu kosongkan.",
                    "",
                    "  data = lain.data;      // curi pointernya, tidak menyalin isinya",
                    "  lain.data = nullptr;   // kosongkan sumbernya",
                    "",
                    "Baris kedua wajib ada. Kalau dilewati, dua objek memegang pointer yang",
                    "sama. Lalu dua destructor menghapus memori yang sama. Hasilnya crash,",
                    "atau lebih parah lagi, memori rusak tanpa tanda apa pun.",
                    "",
                    "Move assignment butuh dua tambahan. Pertama, buang dulu milik sendiri",
                    "(delete[] data;) sebelum mengambil milik objek lain. Kedua, cek 'if",
                    "(this != &lain)'. Tanpa cek ini, 'a = std::move(a)' menghapus isinya",
                    "sendiri, lalu menyalin dari sisa yang udah hancur.",
                    "",
                    "Kenapa noexcept menentukan kecepatan?",
                    "",
                    "Ingat materi Vector: waktu penuh, vector memindahkan semua isinya ke",
                    "blok memori yang lebih besar. Vector wajib menjamin isinya tetap utuh",
                    "kalau pemindahan itu gagal di tengah jalan. Move yang bisa melempar",
                    "exception nggak bisa dijamin. Kalau gagal di elemen ke-50, sumbernya",
                    "udah telanjur dibongkar dan nggak bisa dikembalikan.",
                    "",
                    "Jadi vector ngecek dulu. Kalau move constructor-mu noexcept, dia",
                    "memindahkan. Kalau bukan, dia menyalin semuanya tanpa bilang apa-apa.",
                    "Cara itu aman, tapi lambatnya bisa berkali-kali lipat, dan nggak ada",
                    "satu pun peringatan. Satu kata noexcept yang lupa ditulis bisa jadi",
                    "penyebab program lambat yang kamu cari seharian.",
                    "",
                    "Dua anggota ini juga bisa ditulis '= default' dan '= delete', sama",
                    "seperti copy constructor di materi Copy Constructor, operator= &",
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
                    "Materi Copy Constructor ditutup dengan janji bahwa Aturan Tiga nanti",
                    "berkembang jadi Aturan Lima. Ini dia kelimanya, dan sekarang kamu",
                    "udah tahu guna tiap barisnya:",
                    "",
                    "  1. ~Buffer();                                  destructor",
                    "  2. Buffer(const Buffer&);                       copy constructor",
                    "  3. Buffer& operator=(const Buffer&);            copy assignment",
                    "  4. Buffer(Buffer&&) noexcept;                   move constructor",
                    "  5. Buffer& operator=(Buffer&&) noexcept;        move assignment",
                    "",
                    "Aturan Lima bunyinya begini: kalau kamu menulis salah satu dari",
                    "kelimanya, hampir pasti kamu perlu memikirkan kelima-limanya.",
                    "Alasannya sama dengan Aturan Tiga. Kamu menulisnya karena class itu",
                    "memiliki sesuatu yang harus diurus sendiri.",
                    "",
                    "Ada satu jebakan baru. Kalau kamu menulis destructor atau copy",
                    "constructor sendiri, compiler berhenti membuatkan move constructor",
                    "untukmu. Class-mu tetap jalan, tapi balik menyalin di tempat yang",
                    "seharusnya memindahkan. Nggak ada error, nggak ada peringatan,",
                    "programnya cuma jadi lambat.",
                    "",
                    "Aturan Nol (Rule of Zero), yang sebetulnya kamu incar",
                    "",
                    "Materi yang sama ditutup dengan saran \"pakai vector, string, dan smart",
                    "pointer, biar versi bawaan compiler yang benar\". Saran itu ternyata",
                    "punya nama, dan sekarang berlaku untuk kelima anggota, nggak cuma",
                    "tiga.",
                    "",
                    "Cara terbaik menghadapi Aturan Lima adalah nggak usah berurusan",
                    "dengannya sama sekali. Kalau semua atribut class-mu berupa vector,",
                    "string, dan smart pointer, masing-masing udah tahu cara mengurus",
                    "dirinya sendiri. Versi bawaan compiler otomatis benar, dan kamu nggak",
                    "perlu menulis satu pun dari lima anggota itu:",
                    "",
                    "  class Mahasiswa {          // nol anggota khusus, dan itu BAGUS",
                    "      string nama;",
                    "      vector<int> nilai;",
                    "      unique_ptr<Berkas> arsip;",
                    "  };",
                    "",
                    "Class seperti itu bisa dipindah dan dihapus dengan benar tanpa satu",
                    "baris kode tambahan. Karena ada unique_ptr, menyalinnya otomatis",
                    "dilarang compiler, sebab unique_ptr memang nggak boleh disalin. Kalau",
                    "atributnya cuma vector dan string, class-nya juga bisa disalin dengan",
                    "benar.",
                    "",
                    "Contoh Buffer di atas sengaja memakai 'int *data' mentah supaya",
                    "kelima anggotanya kelihatan. Di kode sungguhan, pilihan pertamamu",
                    "adalah vector<int>, dan semua urusan tadi jadi nggak perlu.",
                    "",
                    "Kapan Aturan Lima tetap harus kamu tulis sendiri? Waktu class-mu",
                    "memegang sesuatu yang belum punya pembungkus RAII, misalnya handle",
                    "sistem operasi, koneksi soket, atau resource dari pustaka C. Di situ",
                    "kamu yang membuat pembungkusnya, cukup sekali. Sesudah itu semua",
                    "pemakainya bisa kembali pakai Aturan Nol.",
                ],
            },
        ],
    },
    {
        "title": "32. Multithreading Dasar: thread, mutex & lock_guard",
        "sections": [
            {
                "body": [
                    "Sampai sekarang programmu mengerjakan satu hal dalam satu waktu. Satu",
                    "baris selesai, baru baris berikutnya jalan. Thread adalah jalur kerja",
                    "kedua di dalam program yang sama. Dengan thread, dua bagian kode bisa",
                    "berjalan bersamaan, misalnya di dua inti prosesor.",
                    "",
                    "Buat apa? Orang memakai C++ justru karena performanya. Server yang",
                    "melayani ribuan koneksi, game engine yang menggambar sambil menghitung",
                    "fisika, dan sistem trading hampir semuanya multithread. Prosesor",
                    "sekarang punya banyak inti. Program yang cuma punya satu thread hanya",
                    "memakai satu inti, berapa pun jumlah intinya.",
                    "",
                    "Cara bikin thread (butuh #include <thread>):",
                    "",
                    "  void kerja(int n) { ... }",
                    "",
                    "  thread t(kerja, 5);   // thread LANGSUNG jalan; 5 dikirim ke kerja()",
                    "  t.join();             // main BERHENTI di sini sampai t selesai",
                    "",
                    "Sebelum objek thread-nya hancur, kamu wajib memanggil join() atau",
                    "detach(). Kalau lupa, programnya nggak cuma salah, tapi langsung mati:",
                    "",
                    "  terminate called without an active exception",
                    "  Aborted (core dumped)",
                    "",
                    "  - t.join() artinya tunggu sampai selesai. Ini yang hampir selalu",
                    "    kamu mau, dan satu-satunya cara aman untuk membaca hasil kerjanya.",
                    "  - t.detach() artinya lepaskan, biarkan dia hidup sendiri. Bahayanya,",
                    "    thread itu bisa menyentuh variabel yang udah mati kalau main",
                    "    selesai duluan. Pakai cuma kalau kamu betul-betul tahu alasannya.",
                    "",
                    "Ada yang perlu kamu terima dari awal: urutan jalannya thread",
                    "nggak bisa ditebak. Program yang sama, dijalankan dua kali, bisa",
                    "mencetak dengan urutan yang beda. Itu bukan bug di kodemu. Makanya",
                    "semua contoh di sini disusun supaya hasil akhirnya tetap pasti,",
                    "walaupun jalannya di dalam nggak pernah pasti.",
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
                    "Contoh di atas aman karena tiap thread punya tempat sendiri. Masalah",
                    "muncul kalau dua thread menyentuh satu variabel yang sama. Baris",
                    "sesederhana ini pun nggak aman:",
                    "",
                    "  counter++;   // BACA nilainya -> TAMBAH 1 -> TULIS balik",
                    "",
                    "Itu tiga langkah, dan thread lain bisa menyela di antaranya. Kalau dua",
                    "thread sama-sama membaca 40, dua-duanya menulis 41. Satu penambahan",
                    "hilang. Kejadian ini disebut data race. Hasilnya meleset, besar",
                    "melesetnya berubah tiap kali dijalankan, dan programnya tetap jalan",
                    "tanpa satu pun pesan error.",
                    "",
                    "std::mutex (dari <mutex>) itu gemboknya. Cuma satu thread yang boleh",
                    "memegangnya, yang lain antre di depan pintu. Tapi jangan mengunci",
                    "secara manual:",
                    "",
                    "  mu.lock(); ... mu.unlock();   // JANGAN - sekali ada return atau",
                    "                                // exception di tengah, gembok itu",
                    "                                // TIDAK PERNAH terbuka lagi dan",
                    "                                // seluruh program membeku",
                    "",
                    "Pakai lock_guard. Ini persis RAII dari materi sebelumnya:",
                    "",
                    "  {",
                    "      lock_guard<mutex> kunci(mu);   // constructor MENGUNCI",
                    "      denganKunci++;",
                    "  }                                  // destructor MEMBUKA di sini",
                    "",
                    "Waktu pertama kali membaca kode orang, baris lock_guard<mutex>",
                    "kunci(mu); kelihatan aneh. Sebuah variabel dibuat, lalu namanya nggak",
                    "pernah dipakai lagi. Justru itu intinya. Yang bekerja adalah",
                    "constructor dan destructor-nya, bukan nilainya. Destructor selalu",
                    "dipanggil, bahkan waktu ada exception, jadi gemboknya nggak mungkin",
                    "lupa dibuka.",
                    "",
                    "Untuk penghitung sederhana ada cara yang lebih ringan: std::atomic",
                    "(dari <atomic>). Kalau kamu nulis atomic<int> x; lalu x++, penambahan",
                    "itu dijamin terjadi dalam satu langkah utuh di tingkat prosesor. Nggak",
                    "ada celah untuk disela, dan nggak perlu mutex sama sekali. Pakai",
                    "atomic kalau yang dijaga cuma satu variabel. Pakai mutex kalau ada",
                    "beberapa variabel yang harus berubah bersama-sama.",
                    "",
                    "Contoh berikut sengaja memperlambat tiga langkah tadi. Langkahnya",
                    "ditulis satu per satu, dan this_thread::yield() diselipkan di tengah,",
                    "supaya celahnya kelihatan setiap kali dijalankan. Dengan counter++",
                    "biasa, di mesin yang cepat hasilnya kadang kebetulan pas. Itu sifat",
                    "data race yang paling berbahaya: dia sering lolos waktu diuji, lalu",
                    "baru rusak di komputer lain atau waktu bebannya beda.",
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
                    "Jalankan contoh itu beberapa kali. denganKunci dan pakaiAtomic selalu",
                    "tepat 40000. tanpaKunci berakhir di sekitar 20000, artinya hampir",
                    "separuh penambahan hilang, dan angka persisnya beda tiap kali. Begitu",
                    "wujud data race: nggak ada crash, nggak ada pesan error, cuma angka",
                    "yang salah tanpa ketahuan.",
                    "",
                    "Kesalahan yang sering terjadi:",
                    "",
                    "  - Lupa mengunci di satu tempat aja udah cukup merusak. Gembok cuma",
                    "    bekerja kalau semua kode yang menyentuh data itu memakainya.",
                    "  - Deadlock. Thread A memegang mu1 lalu minta mu2, sementara thread B",
                    "    memegang mu2 lalu minta mu1. Keduanya menunggu selamanya, dan",
                    "    programnya membeku tanpa pesan apa pun. Nggak ada yang crash, dan",
                    "    keluarannya nggak ngasih petunjuk. Obatnya: selalu kunci dengan",
                    "    urutan yang sama di seluruh program. Atau pakai scoped_lock",
                    "    (C++17), yang mengambil beberapa mutex sekaligus dengan aman:",
                    "    scoped_lock kunci(mu1, mu2);",
                    "  - Mengunci terlalu lebar. Kalau seluruh isi fungsi dikunci, thread",
                    "    lain cuma antre, dan programmu malah lebih lambat daripada versi",
                    "    satu thread. Kunci sesempit mungkin. Karena itu juga, yield() di",
                    "    dalam lock_guard tadi cuma alat peraga. Di kode sungguhan, jangan",
                    "    pernah menahan kunci sambil menunggu apa pun.",
                    "  - cout dari banyak thread bisa saling nyelip di tengah baris. Supaya",
                    "    keluarannya rapi, simpan hasil di slot masing-masing, lalu cetak",
                    "    sesudah semua join(), persis seperti contoh pertama.",
                    "  - Lupa ref() waktu mengirim variabel yang harus diubah. Pesan",
                    "    error-nya puluhan baris template, bunyinya: 'static assertion",
                    "    failed: std::thread arguments must be invocable after conversion",
                    "    to rvalues'. Artinya cuma satu: bungkus argumennya dengan ref(x).",
                    "",
                    "unique_lock<mutex> itu saudara lock_guard yang lebih luwes. Dia bisa",
                    "dibuka lalu dikunci lagi di tengah jalan. Dia juga wajib dipakai",
                    "bareng condition_variable, yaitu cara thread saling menunggu (topik",
                    "lanjutan). Ongkosnya sedikit lebih mahal. Jadi pilih lock_guard",
                    "selama kamu cuma perlu mengunci satu blok dari awal sampai akhir.",
                    "",
                    "Cara kompilasi: program yang pakai thread butuh library thread milik",
                    "sistem.",
                    "",
                    "  g++ -std=c++17 -pthread program.cpp -o program",
                    "",
                    "Di Linux versi baru, g++ tanpa -pthread sering tetap berhasil. Makanya",
                    "contoh di halaman ini bisa langsung dijalankan. Tapi biasakan tetap",
                    "menulisnya. Di mesin lain, tanpa -pthread bisa muncul error linker",
                    "yang membingungkan seperti 'undefined reference to pthread_create'.",
                    "Kalau pakai CMake, jangan tulis -pthread manual. Minta CMake yang",
                    "mencarinya:",
                    "",
                    "  find_package(Threads REQUIRED)",
                    "  target_link_libraries(program PRIVATE Threads::Threads)",
                    "",
                    "Terakhir, thread::hardware_concurrency() memberi tahu berapa thread",
                    "yang masuk akal dibuat di mesin itu. Bikin 500 thread di mesin 8 inti",
                    "nggak bikin apa pun lebih cepat. Yang bertambah cuma ongkos",
                    "gonta-ganti antar-thread.",
                ],
            },
        ],
    },
    {
        "title": "33. Roadmap Menjadi C++ Programmer Handal",
        "sections": [
            {
                "body": [
                    "Sekarang kamu udah pegang dasar C++ yang kuat: OOP lengkap",
                    "(inheritance, polymorphism, abstract class), template, STL, smart",
                    "pointer, exception handling, sampai RAII dan lambda. Ditambah dasar C",
                    "yang kamu pelajari sebelumnya, kamu udah paham dari urusan memori",
                    "sampai abstraksi tingkat tinggi.",
                    "",
                    "Tahap 1: kuatkan dasar (kamu ada di sini)",
                    "  - Pastikan kamu paham kapan pakai reference, pointer, atau smart",
                    "    pointer, dan kapan virtual function diperlukan.",
                    "  - Latihan: bikin sendiri struktur data pakai template, misalnya",
                    "    Stack<T> dan Queue<T>, sebelum langsung pakai STL.",
                ]
            },
            {
                "body": [
                    "Tahap 2: perdalam C++ modern (C++11/14/17/20)",
                    "  - Move semantics dan perfect forwarding (topik lanjutan).",
                    "  - constexpr, yaitu perhitungan yang dikerjakan waktu kompilasi,",
                    "    bukan waktu program jalan.",
                    "  - Concepts (C++20), yaitu syarat untuk template supaya maksudnya",
                    "    lebih jelas.",
                    "  - Multithreading dengan <thread>, <mutex>, dan <atomic>.",
                    "",
                    "Tahap 3: pilih jalur spesialisasi",
                    "  - Game development. Pelajari Unreal Engine, yang bahasa utamanya",
                    "    C++. Pelajari juga game loop, dasar physics engine, dan rendering.",
                    "  - High-performance dan systems, misalnya sistem trading dan embedded",
                    "    system yang real-time. Di sini kamu belajar optimasi performa:",
                    "    kode yang ramah cache, dan profiling.",
                    "  - Aplikasi umum. Pakai Qt framework untuk aplikasi desktop ber-GUI,",
                    "    dan Boost, kumpulan library yang sering disebut \"STL tambahan\".",
                ]
            },
            {
                "heading": "Sebelum membuka repo orang: konvensi penamaan C++",
                "body": [
                    "Kita jeda sebentar dari daftar tahap. Tahap 4 menyusul sesudah bagian",
                    "ini, dan bagian ini bekal untuk tahap itu.",
                    "",
                    "Semua contoh di kurikulum ini memakai camelCase berbahasa Indonesia,",
                    "misalnya totalHarga, getSaldo, dan jumlahItem, supaya kamu bisa fokus",
                    "ke konsepnya. Repo C++ di GitHub kelihatan beda jauh. Bedanya itu",
                    "datang dari konvensi yang udah lama dipakai, nggak cuma selera",
                    "masing-masing orang. Kenali dari sekarang, supaya nanti kamu nggak",
                    "mengira sebuah nama biasa itu kata kunci khusus.",
                    "",
                    "  - Pustaka standar dan Boost pakai snake_case, huruf kecil semua:",
                    "    push_back, make_shared, value_type, find_if. Kalau ada nama",
                    "    bergaya begini, biasanya penulisnya sengaja meniru STL.",
                    "  - class dan struct pakai PascalCase: KeranjangBelanja, HttpClient.",
                    "    Ini yang paling seragam di mana-mana.",
                    "  - Atribut anggota diberi awalan m_ (m_jumlahItem) atau akhiran garis",
                    "    bawah (jumlah_item_). Tanda itu cuma untuk membedakan atribut dari",
                    "    variabel lokal waktu membaca method yang panjang. Bagi compiler",
                    "    tanda itu nggak ada artinya. Ini yang paling sering disangka",
                    "    sintaks rahasia.",
                    "  - Makro selalu ditulis huruf besar dengan garis bawah:",
                    "    MAKS_KONEKSI. Sengaja dibuat mencolok, karena makro bekerja dengan",
                    "    menimpa teks dan hasilnya bisa mengejutkan.",
                    "  - Konstanta kadang diberi awalan k: kMaksUkuran (gaya Google). Di",
                    "    tempat lain cukup ditulis huruf besar semua.",
                    "",
                    "Satu proyek biasanya memilih satu gaya, lalu memakainya di semua",
                    "berkas. Waktu kamu ikut menyumbang kode ke repo orang, tiru gaya yang",
                    "udah ada di sana, walaupun beda dengan selera kamu sendiri.",
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
                    "Tahap 4: kebiasaan profesional",
                    "  1. Selalu pakai smart pointer. Hindari new/delete manual.",
                    "  2. Kompilasi dengan -Wall -Wextra. Nyalakan juga -Wshadow dan",
                    "     -Wconversion supaya lebih banyak bug ketangkap. -Wall ini juga",
                    "     yang memunculkan peringatan signed/unsigned pada perbandingan",
                    "     size_t di materi Konversi Tipe. Jangan dimatikan, karena",
                    "     peringatan itu menunjuk bug sungguhan.",
                    "  3. Pakai CMake sebagai build system untuk project besar. CMake itu",
                    "     standar industri, dan menggantikan Makefile yang ditulis manual.",
                    "     CMakeLists.txt terkecil yang udah cukup ada di materi Memecah",
                    "     Class ke Header. Mulai dari situ. Jangan menyalin berkas CMake",
                    "     raksasa punya orang yang isinya belum kamu pahami.",
                    "  4. Bikin tes pakai Google Test (gtest) atau Catch2.",
                    "  5. Baca 'Effective C++' karya Scott Meyers. Buku ini membahas idiom",
                    "     dan kebiasaan baik (best practice) C++ secara mendalam.",
                    "",
                    "Kebiasaan harian supaya makin jago:",
                    "  1. Ketik ulang semua contoh. Jangan copy-paste.",
                    "  2. Untuk masalah yang sama, bandingkan solusi gaya C (pointer,",
                    "     malloc) dengan gaya C++ modern (reference, smart pointer, STL).",
                    "     Pahami untung-rugi masing-masing.",
                    "  3. Baca kode open source C++ yang bagus, misalnya LLVM.",
                    "  4. C++ itu bahasa yang dalam. Jangan berkecil hati kalau masih",
                    "     banyak yang belum kamu pahami. Engineer C++ senior pun masih",
                    "     terus belajar hal baru bertahun-tahun.",
                ]
            },
        ],
    },
]
