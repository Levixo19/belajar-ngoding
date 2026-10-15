C_MATERIALS = [
    {
        "title": "1. Pengenalan C & Instalasi",
        "sections": [
            {
                "body": [
                    "C adalah bahasa pemrograman yang dibuat Dennis Ritchie di Bell Labs",
                    "pada tahun 1972. C termasuk bahasa prosedural: programnya berupa urutan",
                    "langkah yang dijalankan satu per satu. Orang biasa menyebutnya bahasa",
                    "tingkat rendah-menengah, karena C cukup dekat dengan cara kerja mesin,",
                    "tapi masih enak dibaca manusia.",
                    "",
                    "Hampir semua bahasa modern meniru cara C menulis kode. Java, Python,",
                    "JavaScript, C++, Go, dan Rust semuanya terinspirasi atau terpengaruh",
                    "sintaks C.",
                    "",
                    "C dipakai untuk:",
                    "  - sistem operasi, misalnya kernel Linux dan Windows",
                    "  - embedded system, yaitu program yang ditanam di dalam perangkat",
                    "    elektronik",
                    "  - driver, database engine, dan compiler",
                    "",
                    "Kenapa C masih layak dipelajari walaupun umurnya sudah tua?",
                    "  - C memperlihatkan cara kerja memori komputer secara langsung. Memori",
                    "    itu tempat program menyimpan data selama dia berjalan.",
                    "  - Konsep dasar banyak bahasa lain berasal dari C atau mirip C. Jadi",
                    "    sesudah paham C, bahasa lain terasa lebih gampang.",
                    "  - C masih dipakai luas. Kernel Linux ditulis dalam C, begitu juga",
                    "    CPython, program yang menjalankan kode Python.",
                    "",
                    "Sebelum mulai, kamu butuh compiler, yaitu program yang menerjemahkan",
                    "kode C jadi program yang bisa dijalankan komputer:",
                    "  - Linux: biasanya gcc sudah terpasang. Kalau belum, pasang dengan",
                    "    sudo apt install gcc.",
                    "  - Windows: pakai MinGW atau WSL. WSL lebih disarankan.",
                    "  - Mac: pasang Xcode Command Line Tools. Isinya compiler clang, yang",
                    "    perintahnya kompatibel dengan gcc.",
                    "  - Cek hasil instalasinya dengan gcc --version.",
                ]
            },
            {
                "heading": "Program pertama (simpan sebagai hello.c)",
                "code": """#include <stdio.h>

int main(void) {
    printf("Halo Dunia!\\n");
    printf("Aku sedang belajar C.\\n");
    return 0;
}"""
            },
            {
                "body": [
                    "Program tadi perlu dua langkah supaya jalan. Pertama dikompilasi, lalu",
                    "hasilnya dijalankan:",
                    "",
                    "  gcc hello.c -o hello    (kompilasi jadi executable 'hello')",
                    "  ./hello                  (jalankan hasilnya)",
                    "",
                    "Executable artinya berkas program yang bisa langsung dijalankan.",
                    "",
                    "Sekarang kita bahas baris demi baris:",
                    "",
                    "  #include <stdio.h>",
                    "    Menyertakan library standar untuk input dan output. Tanpa baris",
                    "    ini, compiler nggak kenal printf.",
                    "",
                    "  int main(void)",
                    "    Titik masuk program. Setiap program C wajib punya main, dan",
                    "    program selalu mulai jalan dari sini.",
                    "    int  -> main mengembalikan kode status berupa angka.",
                    "    void -> main nggak menerima parameter apa pun. Ada juga bentuk",
                    "            (int argc, char *argv[]) untuk menerima argumen dari",
                    "            command line. Bentuk itu dibahas di materi Program &",
                    "            Sistem, jadi belum perlu kamu hafal sekarang.",
                    "",
                    "  printf(\"...\")",
                    "    Mencetak teks ke layar.",
                    "",
                    "  \\n",
                    "    Karakter escape untuk pindah ke baris baru.",
                    "",
                    "  return 0;",
                    "    Melapor ke sistem operasi bahwa program selesai dengan sukses.",
                    "    0 artinya sukses, angka selain 0 artinya ada error.",
                    "",
                    "Setiap pernyataan diakhiri titik koma (;). Satu blok kode ditandai",
                    "dengan kurung kurawal { }.",
                ]
            },
            {
                "heading": "Komentar: catatan untuk manusia, dilewati compiler",
                "body": [
                    "Komentar adalah tulisan untuk manusia. Compiler membuang semua komentar",
                    "sebelum membaca kodenya. C punya dua bentuk komentar:",
                    "",
                    "  // sampai akhir baris   -> satu baris saja",
                    "  /* ... */               -> blok, boleh melintasi banyak baris",
                    "",
                    "  int umur = 20;   // keterangan pendek di kanan kode",
                    "",
                    "  /* Bentuk blok dipakai untuk penjelasan panjang, atau untuk",
                    "     catatan lisensi di kepala berkas. */",
                    "",
                    "Ada dua hal yang perlu kamu tahu dari awal:",
                    "  1. Komentar blok /* ... */ nggak boleh ditaruh di dalam komentar blok",
                    "     lain. Coba lihat tulisan ini:",
                    "       /* luar /* dalam */ luar */",
                    "     Komentarnya selesai di */ yang pertama. Sisanya dibaca sebagai",
                    "     kode, dan hasilnya error.",
                    "  2. Bentuk // baru resmi sejak standar C99. Compiler yang sengaja",
                    "     dipaksa memakai standar lama (C89) menolaknya.",
                    "",
                    "Komentar juga berguna untuk hal lain. Menaruh // di depan sebuah baris",
                    "adalah cara tercepat mematikan kode sementara, tanpa menghapusnya. Cara",
                    "ini dipakai terus waktu mencari bug:",
                    "",
                    "  // printf(\"baris ini sedang tidak aku pakai\\n\");",
                    "",
                    "Mulai materi berikutnya, keterangan di dalam contoh kode ditulis pakai",
                    "dua bentuk komentar ini.",
                ]
            },
        ],
    },
    {
        "title": "2. Variabel & Tipe Data",
        "sections": [
            {
                "body": [
                    "C termasuk bahasa statically typed. Artinya, tipe setiap variabel harus",
                    "kamu tulis sebelum variabel itu dipakai, dan tipenya nggak bisa berubah",
                    "lagi sesudahnya. Di Python atau JavaScript, satu variabel boleh berisi",
                    "angka lalu diganti teks. Di C nggak bisa.",
                    "",
                    "Ini tipe data dasar beserta ukurannya. Ukurannya bisa beda di sistem",
                    "lain, jadi pakai sizeof() untuk memastikan ukurannya di komputermu:",
                    "  char     1 byte    satu karakter ('A') atau angka kecil",
                    "  int      4 byte    bilangan bulat (paling umum)",
                    "  float    4 byte    bilangan desimal presisi tunggal",
                    "  double   8 byte    bilangan desimal presisi ganda",
                    "  short    2 byte    bilangan bulat lebih kecil dari int",
                    "  long     8 byte    bilangan bulat lebih besar dari int",
                    "  _Bool    1 byte    true/false (perlu #include <stdbool.h>",
                    "                     agar bisa pakai 'bool', 'true', 'false')",
                    "",
                    "Mendeklarasikan variabel artinya memperkenalkan variabel baru ke",
                    "compiler. Bentuknya begini:",
                    "  tipeData namaVariabel = nilai;",
                ]
            },
            {
                "heading": "Contoh deklarasi variabel & sizeof",
                "code": """#include <stdio.h>
#include <stdbool.h>

int main(void) {
    int umur = 20;
    double harga = 15000.50;
    char grade = 'A';           // karakter pakai kutip TUNGGAL
    bool lulus = true;          // butuh #include <stdbool.h>

    printf("Umur: %d tahun\\n", umur);
    printf("Harga: %.2f\\n", harga);
    printf("Grade: %c\\n", grade);
    printf("Lulus: %d\\n", lulus);    // C lama: tampil 1 (true) atau 0 (false)

    printf("Ukuran int: %zu byte\\n", sizeof(int));
    printf("Ukuran double: %zu byte\\n", sizeof(double));
    return 0;
}"""
            },
            {
                "body": [
                    "Format specifier adalah kode berawalan % di printf dan scanf. Kode ini",
                    "wajib cocok dengan tipe datanya:",
                    "  %d   -> int              %f   -> float/double",
                    "  %c   -> char              %s   -> string (char array)",
                    "  %ld  -> long              %lf  -> double (khusus scanf)",
                    "  %u   -> unsigned int      %x   -> hexadecimal",
                    "  %zu  -> size_t (hasil sizeof)",
                    "  %lld -> long long         %o   -> oktal (basis 8)",
                    "  %e   -> notasi ilmiah (15000.5 tampil jadi 1.500050e+04)",
                    "  %g   -> pilih sendiri antara %f dan %e, mana yang lebih ringkas",
                    "  %p   -> alamat memori (dipakai mulai materi Pointer Dasar)",
                    "  %%   -> mencetak tanda persen itu sendiri, bukan pembuka format",
                    "",
                    "Tipe untuk %u, %x, %o, dan %zu dibahas di materi berikutnya, Bilangan",
                    "Biner, Heksadesimal & Tipe Bilangan Bulat.",
                    "",
                    "Konstanta adalah nilai yang nggak bisa diubah sesudah dibuat. Ada dua",
                    "cara membuatnya, pakai kata kunci const atau #define:",
                    "  const double PI = 3.14159;   // const: type-checked, disarankan",
                    "  #define MAX_SIZE 100          // macro: text replacement (materi 26)",
                    "",
                    "const diperiksa tipenya oleh compiler, jadi lebih disarankan. #define",
                    "cuma mengganti teks sebelum kompilasi.",
                    "",
                    "Casting artinya mengubah tipe sebuah nilai secara paksa:",
                    "  int x = (int) 3.99;    // x = 3 (pecahan dibuang/truncate)",
                    "  double y = (double) 7 / 2;   // y = 3.5 (paksa pembagian desimal)",
                ]
            },
        ],
    },
    {
        "title": "3. Bilangan Biner, Heksadesimal & Tipe Bilangan Bulat",
        "sections": [
            {
                "body": [
                    "Di materi sebelumnya ada angka \"4 byte\" di tabel tipe data. Di materi",
                    "Operator nanti, kamu juga bakal ketemu tulisan \"12 = biner 1100\". Dua",
                    "hal itu belum dijelaskan. Kalau dibiarkan, operator bitwise cuma bisa",
                    "dihafal, dan kode C sungguhan yang penuh 0x1F, uint8_t, dan size_t",
                    "bakal susah dibaca. Materi ini menjelaskan dasarnya.",
                    "",
                    "Bit adalah satu tempat yang cuma bisa berisi 0 atau 1. Bit itu satuan",
                    "terkecil di dalam mesin, dan semua data lain disusun dari bit.",
                    "",
                    "Byte adalah kumpulan 8 bit. Angka 8 itu kesepakatan industri yang",
                    "mulai dipakai bersama di era 1970-an, jadi nggak ada hukum alam yang",
                    "mengharuskannya.",
                    "Hari ini praktis semua mesin memakainya. Walaupun begitu, C tetap",
                    "menyediakan konstanta CHAR_BIT, supaya kode yang butuh kepastian nggak",
                    "perlu berasumsi.",
                    "",
                    "Jadi \"int 4 byte\" artinya ada 4 x 8 = 32 bit untuk menyimpan satu",
                    "angka. Dengan 32 bit, cuma ada 2^32 = 4.294.967.296 pola berbeda yang",
                    "bisa ditulis. Dari situlah jangkauan setiap tipe berasal. Kotaknya",
                    "memang cuma sebesar itu, jadi angka ke-4.294.967.297 nggak punya",
                    "tempat.",
                    "",
                    "Cara membaca biner: tiap posisi punya nilai tempat, dan nilainya dua",
                    "kali lipat posisi di sebelah kanannya. Mirip angka desimal, cuma",
                    "kelipatannya 2, bukan 10.",
                    "",
                    "  nilai tempat : 128  64  32  16   8   4   2   1",
                    "  angka 12     :   0   0   0   0   1   1   0   0",
                    "                                   ^   ^",
                    "                                   8 + 4 = 12",
                    "",
                    "Mengubah desimal ke biner: bagi 2 terus-menerus, catat sisanya, lalu",
                    "baca sisa itu dari bawah ke atas.",
                    "",
                    "  12 / 2 = 6, sisa 0     <- bit paling kanan",
                    "   6 / 2 = 3, sisa 0",
                    "   3 / 2 = 1, sisa 1",
                    "   1 / 2 = 0, sisa 1     <- bit paling kiri",
                    "  dibaca dari bawah: 1100",
                    "",
                    "Heksadesimal (basis 16) memakai 16 lambang: 0 sampai 9, lalu A B C D E",
                    "F. A artinya 10, dan F artinya 15. Gunanya ada basis ketiga ini: 16 =",
                    "2^4, jadi satu digit hex sama persis dengan empat bit. Mengubah biner ke",
                    "hex nggak butuh hitungan. Cukup potong binernya per empat bit:",
                    "",
                    "  biner 1101 1110  ->  1101 = 13 = D,  1110 = 14 = E   ->  hex DE",
                    "  hex   0x1F       ->  1 = 0001, F = 1111              ->  0001 1111 = 31",
                    "",
                    "Akibatnya, 2 digit hex selalu tepat 1 byte, tanpa kecuali. Makanya warna",
                    "web ditulis #FFA000, alamat memori dicetak %p dalam hex, dan hex editor",
                    "menampilkan isi berkas dua digit per byte. Biner terlalu panjang untuk",
                    "dibaca mata, sedangkan desimal nggak pernah pas dengan batas bit. Hex",
                    "ada di tengah-tengahnya.",
                    "",
                    "Ini angka yang sama, ditulis dalam tiga basis di kode C:",
                    "  int a = 31;      // desimal biasa",
                    "  int b = 0x1F;    // awalan 0x = heksadesimal. Nilainya SAMA PERSIS: 31",
                    "  int c = 037;     // awalan angka 0 saja = OKTAL (basis 8). Juga 31",
                    "",
                    "Jebakan: nol di depan angka itu ada artinya. int kode = 0755; bernilai",
                    "493, jadi nilainya nggak sama dengan 755, dan compiler nggak mengeluh",
                    "sama sekali. Menambah nol supaya kolom angka kelihatan rata adalah bug",
                    "klasik yang nggak memunculkan error. Oktal masih dipakai di izin berkas",
                    "Unix: chmod 755 memang basis 8.",
                    "",
                    "Untuk mencetaknya: %x untuk hex huruf kecil, %X untuk hex huruf besar,",
                    "%o untuk oktal, dan %u untuk unsigned. printf standar nggak punya %b",
                    "untuk biner. %b baru masuk di C23 dan belum umum, jadi untuk mencetak",
                    "biner kamu harus menulis fungsinya sendiri. Contohnya ada di bawah.",
                ],
            },
            {
                "heading": "Melihat angka yang sama dalam biner, hex, dan oktal",
                "code": """#include <stdio.h>

// Cetak 8 bit terendah dari n, mulai dari bit bernilai 128 di paling kiri.
void cetakBiner8(unsigned int n) {
    for (int i = 7; i >= 0; i--) {
        printf("%u", (n >> i) & 1u);     // geser bit ke-i ke kanan, ambil bit terakhir
        if (i == 4) printf(" ");         // pemisah tiap 4 bit = tepat 1 digit hex
    }
}

int main(void) {
    unsigned int a = 12;

    printf("desimal %u  -> biner ", a);
    cetakBiner8(a);
    printf("\\n");

    printf("12 dalam hex = %x, dalam oktal = %o\\n", a, a);

    unsigned int topeng = 0x1F;          // literal hex: 0x1F = 31
    printf("0x1F = %u desimal -> biner ", topeng);
    cetakBiner8(topeng);
    printf("\\n");

    printf("huruf kecil %%x: %x    huruf besar %%X: %X\\n", 48879, 48879);

    // 1 digit hex = 4 bit, jadi 2 digit hex = tepat 1 byte
    unsigned char merah = 0xFF, hijau = 0xA0, biru = 0x00;
    printf("warna #%02X%02X%02X\\n", merah, hijau, biru);
    return 0;
}""",
            },
            {
                "body": [
                    "Secara bawaan, semua tipe bilangan bulat di C bertanda (signed),",
                    "artinya bisa negatif. Kata unsigned membuang kemampuan itu. Gantinya,",
                    "jangkauan positifnya jadi dua kali lipat, karena bit yang tadinya",
                    "menandai minus sekarang ikut menyimpan nilai. Ukuran byte-nya nggak",
                    "berubah sama sekali.",
                    "",
                    "  tipe                ukuran   jangkauan",
                    "  char                1 byte   -128 .. 127   (bertanda di x86)",
                    "  unsigned char       1 byte   0 .. 255",
                    "  short               2 byte   -32.768 .. 32.767",
                    "  unsigned short      2 byte   0 .. 65.535",
                    "  int                 4 byte   -2.147.483.648 .. 2.147.483.647",
                    "  unsigned int        4 byte   0 .. 4.294.967.295",
                    "  long                8 byte   sekitar -9,2 x 10^18 .. 9,2 x 10^18",
                    "  unsigned long       8 byte   0 .. sekitar 1,8 x 10^19",
                    "",
                    "Catatan: long 8 byte di Linux dan macOS 64-bit, sedangkan di Windows",
                    "long tetap 4 byte. Ukuran ini nggak dijamin standar. Lihat bagian",
                    "<stdint.h> di bawah.",
                    "",
                    "unsigned char punya peran khusus: di C, dia dipakai sebagai \"satu byte",
                    "data mentah\". Isi berkas gambar, paket jaringan, dan buffer apa pun",
                    "biasanya disimpan sebagai unsigned char. Alasannya, jangkauannya 0..255,",
                    "persis semua pola yang mungkin ada di satu byte, tanpa urusan tanda",
                    "minus.",
                    "",
                    "Komplemen dua adalah cara C menyimpan angka negatif. Istilah ini juga",
                    "muncul di komentar contoh materi Operator ('~a = -13 (komplemen dua)').",
                    "Aturannya: -x disimpan sebagai \"balik semua bit x, lalu tambah 1\".",
                    "",
                    "  dalam 8 bit:  12  = 0000 1100",
                    "                ~12 = 1111 0011   <- semua bit dibalik",
                    "                +1  = 1111 0100   <- inilah pola untuk -12",
                    "",
                    "Jadi pola 1111 0011 (yaitu ~12) dibaca sebagai -13. Ada aturan praktis",
                    "yang bisa dipakai tanpa menghitung bit: ~x selalu sama dengan -x - 1.",
                    "",
                    "-1 adalah pola yang semua bitnya 1 (1111 1111 di 8 bit). Kamu bisa",
                    "membuktikannya dari arah lain: 0 - 1 harus \"meminjam\" ke kiri sampai",
                    "semua kolom penuh. Makanya -1 dipakai sebagai topeng \"semua bit",
                    "menyala\", dan sebagai tanda gagal di fungsi sistem. open(), read(), dan",
                    "write() semuanya mengembalikan -1 kalau error.",
                    "",
                    "Kenapa cara menyimpannya dibuat berputar begini, dan nggak pakai satu",
                    "bit khusus untuk tanda minus aja?",
                    "  - Penjumlahan bertanda dan tak bertanda bisa memakai rangkaian yang",
                    "    sama. Prosesor nggak perlu tahu angkanya negatif atau bukan.",
                    "  - Nol cuma punya satu bentuk. Kalau pakai bit tanda, bakal ada +0 dan",
                    "    -0.",
                    "",
                    "Harganya, jangkauannya nggak simetris. Sisi negatifnya selalu kelebihan",
                    "satu angka, jadi INT_MIN (-2.147.483.648) nggak punya pasangan positif.",
                    "Akibatnya -INT_MIN dan abs(INT_MIN) malah meluap (overflow, artinya",
                    "hasilnya nggak muat di tipenya). Ini bug nyata yang pernah membobol",
                    "banyak program.",
                    "",
                    "Satu lagi soal operator >> (geser kanan) di materi Operator: hasil",
                    "menggeser kanan angka bertanda yang negatif nggak dijamin standar. Di",
                    "praktiknya bit tandanya disalin, jadi -8 >> 1 = -4. Kalau yang kamu mau",
                    "adalah menggeser pola bit, pakai tipe unsigned supaya hasilnya pasti.",
                ],
            },
            {
                "heading": "Batas tipe, overflow, dan unsigned yang berputar",
                "code": """#include <stdio.h>
#include <limits.h>

int main(void) {
    printf("CHAR_BIT = %d  (berapa bit dalam 1 byte di mesin ini)\\n", CHAR_BIT);
    printf("int          : %zu byte, %d .. %d\\n", sizeof(int), INT_MIN, INT_MAX);
    printf("unsigned int : %zu byte, 0 .. %u\\n", sizeof(unsigned int), UINT_MAX);
    printf("unsigned char: %zu byte, 0 .. %d\\n", sizeof(unsigned char), UCHAR_MAX);

    printf("~12 = %d   (aturannya: ~x selalu sama dengan -x - 1)\\n", ~12);

    unsigned int nol = 0;
    printf("0u - 1 = %u   <- BERPUTAR ke nilai terbesar, bukan -1\\n", nol - 1);

    unsigned char b = 250;
    b = b + 10;                  // 260 tidak muat di 8 bit -> tersisa 260 - 256
    printf("unsigned char 250 + 10 = %u\\n", b);

    int negatif = -1;
    unsigned int satu = 1;
    printf("apakah -1 < 1u ? hasilnya %d   (0 berarti TIDAK!)\\n", negatif < satu);

    // Meluap pada tipe BERTANDA (misal INT_MAX + 1) adalah undefined behavior:
    // compiler boleh menghasilkan apa pun, termasuk membuang cek yang kita tulis.
    // Sengaja tidak dicontohkan di sini karena hasilnya memang tidak bisa dijanjikan.
    return 0;
}""",
            },
            {
                "heading": "size_t dan <stdint.h>: tipe yang mengisi kode C sungguhan",
                "body": [
                    "Baris '0u - 1' dan '-1 < 1u' di contoh atas adalah pintu masuk ke dua",
                    "bug yang paling sering menjebak pemula. Asalnya satu fakta: bilangan",
                    "unsigned nggak pernah negatif. Kalau hasilnya seharusnya negatif,",
                    "angkanya berputar ke ujung atas jangkauan. Beda dengan meluapnya tipe",
                    "bertanda, perilaku berputar ini dijamin standar. Jadi programnya nggak",
                    "crash, cuma hasilnya salah tanpa ada tanda apa pun.",
                    "",
                    "Jebakan pertama: loop mundur yang nggak pernah berhenti.",
                    "",
                    "  for (unsigned i = n; i >= 0; i--) { ... }   // MACET SELAMANYA",
                    "",
                    "Untuk tipe unsigned, kondisi i >= 0 selalu benar, karena nilainya",
                    "memang nggak bisa turun di bawah 0. Begitu i = 0, i-- membuatnya jadi",
                    "4.294.967.295, dan loop berputar lagi. Bentuk yang benar:",
                    "",
                    "  for (size_t i = n; i-- > 0; ) { ... }   // i dipakai sesudah dikurangi",
                    "  for (int i = n - 1; i >= 0; i--) { ... } // aman selama n muat di int",
                    "",
                    "Jebakan kedua: mencampur bertanda dan tak bertanda dalam satu",
                    "perbandingan. C mengubah yang bertanda jadi tak bertanda lebih dulu,",
                    "tanpa memberi tahu:",
                    "",
                    "  int n = -1;",
                    "  if (n < strlen(nama)) { ... }   // TIDAK pernah masuk: -1 jadi angka raksasa",
                    "",
                    "Kompilasi pakai gcc -Wall -Wextra supaya compiler memperingatkanmu",
                    "('comparison of integer expressions of different signedness').",
                    "Peringatan ini termasuk yang paling layak dipercaya di C.",
                    "",
                    "size_t itu nama sebuah tipe, jadi jangan dibaca sebagai nama variabel.",
                    "Pemula sering salah baca di sini. size_t tak bertanda, dan dijamin cukup",
                    "besar untuk menampung ukuran objek terbesar yang bisa ada di mesin itu.",
                    "sizeof (materi Variabel & Tipe Data) dan strlen (materi String)",
                    "mengembalikan size_t. Kalau hasilnya ditampung di int, nilainya",
                    "dipersempit dan bisa salah. Cetak size_t pakai %zu, dan susuri isi",
                    "array dengan pola baku for (size_t i = 0; i < n; i++).",
                    "",
                    "<stdint.h> menyediakan tipe yang ukurannya pasti: int8_t, uint8_t,",
                    "int16_t, uint16_t, int32_t, uint32_t, int64_t, uint64_t. Angkanya adalah",
                    "jumlah bit, dan awalan u berarti unsigned. Tipe ini dipakai hampir di",
                    "seluruh kode kernel, embedded, dan protokol jaringan. Alasannya, standar",
                    "C cuma menjanjikan int \"setidaknya 16 bit\". Ukuran 4 byte itu kebiasaan,",
                    "dan standar nggak menjanjikannya. Waktu kode membaca header paket TCP",
                    "atau register hardware, meleset satu byte aja bikin seluruh sisa",
                    "datanya salah baca. uint32_t menghilangkan keraguan itu.",
                    "",
                    "Mencetak tipe <stdint.h> perlu sedikit hati-hati, karena %d dan %u",
                    "belum tentu cocok dengan ukurannya. Cara aman untuk sekarang: cast dulu,",
                    "seperti (unsigned)umur dan (unsigned long long)id di contoh. Cara",
                    "resminya memakai makro PRId32 / PRIu64 dari <inttypes.h>. Cukup kenali",
                    "namanya dulu.",
                    "",
                    "Akhiran _t adalah kebiasaan penamaan tipe di C, dan sintaks C sendiri",
                    "nggak mewajibkannya. Contohnya size_t, time_t, dan uint8_t. FILE adalah",
                    "pengecualian lama yang nggak pakai _t. Jadi begitu kamu melihat _t di",
                    "ujung sebuah nama, baca sebagai \"ini nama tipe\".",
                ],
                "code": """#include <stdio.h>
#include <string.h>
#include <stdint.h>

int main(void) {
    char nama[] = "Levi";
    size_t panjang = strlen(nama);        // strlen mengembalikan size_t, bukan int
    printf("panjang \\"%s\\" = %zu\\n", nama, panjang);

    for (size_t i = 0; i < panjang; i++) {    // pola baku menyusuri isi
        printf("%zu:%c ", i, nama[i]);
    }
    printf("\\n");

    uint8_t umur = 20;                    // TEPAT 8 bit tanpa tanda: 0..255
    int32_t saldo = -1500;                // TEPAT 32 bit bertanda
    uint64_t idPengguna = 9000000000ULL;  // muat, walau melebihi jangkauan uint32_t

    printf("umur=%u saldo=%d id=%llu\\n",
           (unsigned)umur, (int)saldo, (unsigned long long)idPengguna);
    printf("uint8_t %zu byte, int32_t %zu byte, uint64_t %zu byte\\n",
           sizeof(uint8_t), sizeof(int32_t), sizeof(uint64_t));

    // Satu byte data mentah paling tepat disimpan sebagai uint8_t
    uint8_t paket[3] = {0xDE, 0xAD, 0x0B};
    for (size_t i = 0; i < sizeof(paket) / sizeof(paket[0]); i++) {
        printf("%02X ", paket[i]);
    }
    printf("\\n");
    return 0;
}""",
            },
        ],
    },
    {
        "title": "4. Operator",
        "sections": [
            {
                "body": [
                    "Operator aritmatika di C sama seperti di Java:",
                    "  +  -  *  /  %",
                    "  ++ increment   -- decrement",
                    "",
                    "Posisi tanda ++ ada artinya. ++i menaikkan nilai dulu, baru nilainya",
                    "dipakai. i++ memakai nilainya dulu, baru naik. Bedanya baru terasa",
                    "kalau ++ ditulis di dalam ekspresi lain. Materi Ekspresi, Prioritas",
                    "Operator & Prefix/Postfix membahasnya lebih dalam.",
                    "",
                    "Hati-hati dengan pembagian integer:",
                    "  7 / 2   = 3     (int / int = int, sisa dibuang, sama seperti Java)",
                    "  7.0 / 2 = 3.5   (salah satu double, hasilnya desimal)",
                    "  7 % 2   = 1     (sisa bagi, hanya untuk tipe integer)",
                    "",
                    "Operator lain yang sering dipakai:",
                    "  penugasan     =  +=  -=  *=  /=  %=",
                    "  perbandingan  ==  !=  >  <  >=  <=",
                    "  logika        &&  (AND)   ||  (OR)   !  (NOT)",
                    "",
                    "Tulisan operator logika di C sama persis dengan Java. Python berbeda,",
                    "karena memakai kata and, or, dan not.",
                ]
            },
            {
                "heading": "Operator bitwise (KHAS pemrograman level rendah)",
                "code": """#include <stdio.h>

int main(void) {
    int a = 12;    // biner: 1100
    int b = 10;    // biner: 1010

    printf("a & b  = %d\\n", a & b);   // AND bit:  1000 = 8
    printf("a | b  = %d\\n", a | b);   // OR bit:   1110 = 14
    printf("a ^ b  = %d\\n", a ^ b);   // XOR bit:  0110 = 6
    printf("~a     = %d\\n", ~a);      // NOT bit:  -13 (komplemen dua)
    printf("a << 1 = %d\\n", a << 1);  // geser kiri 1 bit: 24 (kali 2)
    printf("a >> 1 = %d\\n", a >> 1);  // geser kanan 1 bit: 6 (bagi 2)

    return 0;
}"""
            },
            {
                "body": [
                    "Operator bitwise biasanya dipakai untuk:",
                    "  - mengatur flag atau bit satu per satu di program embedded dan",
                    "    program sistem",
                    "  - optimasi, karena menggeser bit lebih cepat daripada mengali atau",
                    "    membagi dengan pangkat 2",
                    "  - bekerja langsung dengan register hardware",
                    "",
                    "Di aplikasi tingkat tinggi sehari-hari, operator bitwise jarang",
                    "dipakai.",
                    "",
                    "Komentar di contoh tadi menyebut '1100' dan 'komplemen dua' begitu",
                    "aja. Cara membaca angka biner, dan alasan ~a dengan a = 12 menghasilkan",
                    "-13, sudah dibahas di materi Bilangan Biner, Heksadesimal & Tipe",
                    "Bilangan Bulat.",
                ]
            },
        ],
    },
    {
        "title": "5. Ekspresi, Prioritas Operator & Prefix/Postfix",
        "sections": [
            {
                "body": [
                    "Materi Operator memberi daftar operatornya. Materi ini menjawab",
                    "pertanyaan yang muncul begitu beberapa operator dipakai bersamaan dalam",
                    "satu baris: mana yang dikerjakan duluan, dan berapa nilai tiap",
                    "potongannya.",
                    "",
                    "Kuncinya satu ide: di C, hampir semua yang kamu tulis adalah ekspresi,",
                    "dan setiap ekspresi punya nilai.",
                    "",
                    "  Ekspresi   -> potongan kode yang bisa dihitung menjadi sebuah nilai.",
                    "                2 + 3 bernilai 5. umur bernilai isinya.",
                    "                tambah(2, 3) bernilai 5.",
                    "  Pernyataan -> satu perintah utuh; biasanya sebuah ekspresi + titik koma.",
                    "                'i++;' adalah ekspresi i++ yang dijadikan pernyataan.",
                    "",
                    "Yang sering mengejutkan orang yang datang dari Python: penugasan juga",
                    "termasuk ekspresi.",
                    "  x = 5    mengisi x dengan 5, dan seluruh ekspresi itu juga bernilai 5",
                    "",
                    "Akibatnya, baris seperti ini sah dan sering muncul di kode nyata:",
                    "  int a, b;",
                    "  a = b = 0;      // '=' berasosiasi KANAN ke KIRI: b = 0 dikerjakan dulu,",
                    "                  // ekspresi itu bernilai 0, dan 0 itulah yang masuk ke a.",
                    "",
                    "printf() juga ekspresi. Nilainya adalah jumlah karakter yang berhasil",
                    "dicetak:",
                    "  int n = printf(\"abc\\n\");   // mencetak abc, lalu n berisi 4 (3 huruf + \\n)",
                    "",
                    "Nilai itu hampir selalu diabaikan, tapi tetap ada.",
                    "",
                    "Operator koma (,) menyambung dua ekspresi jadi satu, dan nilainya",
                    "diambil dari ekspresi yang kanan. Dalam praktik, operator ini cuma",
                    "dipakai di kepala for, dan di situ memang berguna:",
                    "  for (int i = 0, j = 5; i < j; i++, j--) { ... }",
                    "  // dua penghitung sekaligus",
                    "",
                    "Koma yang memisahkan argumen fungsi, seperti di printf(\"%d\", x), nggak",
                    "termasuk operator koma. Tandanya kebetulan sama, perannya beda.",
                ],
            },
            {
                "heading": "Prefix vs postfix, dan idiom yang bergantung penuh padanya",
                "body": [
                    "Materi Operator menyebut ++ dan --. Yang belum disebut: keduanya punya",
                    "dua bentuk, dan bedanya ada di nilai yang dikembalikan ekspresinya.",
                    "",
                    "  a++  (postfix) -> menaikkan a, tapi mengembalikan nilai LAMA a.",
                    "  ++a  (prefix)  -> menaikkan a, lalu mengembalikan nilai BARU a.",
                    "",
                    "Kalau ditulis sebagai pernyataan sendiri ('i++;' atau '++i;'),",
                    "keduanya sama persis. Makanya bedanya belum pernah terasa sampai",
                    "sekarang. Bedanya baru muncul waktu nilai ekspresinya dipakai, dan",
                    "beberapa idiom khas C bergantung pada beda itu.",
                ],
                "code": """#include <stdio.h>

int main(void) {
    int a = 5;
    int b = a++;      // b menerima nilai LAMA a (5), SESUDAH itu a jadi 6
    printf("postfix: a = %d, b = %d\\n", a, b);   // a = 6, b = 5

    int c = 5;
    int d = ++c;      // c dinaikkan DULU jadi 6, baru nilai itu masuk ke d
    printf("prefix : c = %d, d = %d\\n", c, d);   // c = 6, d = 6

    // Idiom 1: mengisi array sambil memajukan indeks dalam satu gerakan
    int arr[5];
    int i = 0;
    arr[i++] = 10;    // dipakai i lama (0), sesudah itu i jadi 1
    arr[i++] = 20;    // dipakai i lama (1), sesudah itu i jadi 2
    printf("arr[0]=%d arr[1]=%d i=%d\\n", arr[0], arr[1], i);

    // Idiom 2: stack. ++top menaikkan DULU (ke slot kosong berikutnya),
    // top-- membaca puncak DULU baru turun. Pola persis ini dipakai Latihan 15.
    int stack[10];
    int top = -1;                 // -1 berarti kosong
    stack[++top] = 100;           // top jadi 0, lalu stack[0] = 100
    stack[++top] = 200;           // top jadi 1, lalu stack[1] = 200
    printf("pop: %d\\n", stack[top--]);   // baca stack[1]=200, sesudah itu top=0
    printf("pop: %d\\n", stack[top--]);   // baca stack[0]=100, sesudah itu top=-1
    printf("top = %d (kosong lagi)\\n", top);

    // Idiom 3: while (n--) menguji nilai LAMA, jadi badannya jalan tepat n kali
    int n = 3;
    while (n--) {
        printf("n di dalam badan: %d\\n", n);
    }
    printf("n sesudah loop: %d\\n", n);
    return 0;
}""",
            },
            {
                "body": [
                    "Kalau satu ekspresi memuat banyak operator, C nggak membacanya begitu",
                    "aja dari kiri ke kanan. Ada prioritas, yaitu operator mana yang",
                    "dikerjakan duluan. Ada juga asosiativitas, yaitu arah pengelompokan",
                    "operator yang prioritasnya sama.",
                    "",
                    "  Prioritas   Operator                                        Asosiativitas",
                    "  ----------  ----------------------------------------------  -------------",
                    "  tertinggi   ()  []  ->  .   x++  x--   (postfix)            kiri ke kanan",
                    "              ++x  --x   !  ~   +x  -x   (unary)              kanan ke kiri",
                    "              *p (isi)  &x (alamat)  sizeof  (tipe) cast      kanan ke kiri",
                    "              *   /   %                                       kiri ke kanan",
                    "              +   -                                           kiri ke kanan",
                    "              <<  >>                                          kiri ke kanan",
                    "              <   <=  >   >=                                  kiri ke kanan",
                    "              ==  !=                                          kiri ke kanan",
                    "              &    (bitwise AND)                              kiri ke kanan",
                    "              ^    (bitwise XOR)                              kiri ke kanan",
                    "              |    (bitwise OR)                               kiri ke kanan",
                    "              &&                                              kiri ke kanan",
                    "              ||                                              kiri ke kanan",
                    "              ?:   (ternary)                                  kanan ke kiri",
                    "              =  +=  -=  *=  /=  %=  &=  |=  ^=  <<=  >>=     kanan ke kiri",
                    "  terendah    ,    (operator koma)                            kiri ke kanan",
                    "",
                    "Ada empat akibat yang paling sering bikin salah:",
                    "  1. Postfix lebih kuat daripada * (isi).",
                    "       *p++            dibaca   *(p++)",
                    "     Yang naik adalah pointer-nya, dan nilai yang ditunjuk nggak",
                    "     berubah. Untuk menaikkan nilainya, tulis (*p)++.",
                    "  2. == lebih kuat daripada & (bitwise).",
                    "       flags & MASK == MASK      dibaca   flags & (MASK == MASK)",
                    "       flags = 12, MASK = 4      ->  hasilnya 0",
                    "       (flags & MASK) == MASK    ->  hasilnya 1, ini yang dimaksud",
                    "  3. + lebih kuat daripada geser bit.",
                    "       x << 1 + 2      dibaca   x << (1 + 2)",
                    "     Dengan x = 1 hasilnya 8, sedangkan (x << 1) + 2 hasilnya 4.",
                    "  4. ! (unary) lebih kuat daripada &.",
                    "       !flags & MASK   dibaca   (!flags) & MASK",
                    "       !(flags & MASK) ->  ini yang hampir selalu dimaksud",
                    "",
                    "gcc -Wall menegur nomor 2, 3, dan 4 dengan pesan 'suggest parentheses'.",
                    "Cuma nomor 1 yang lolos tanpa peringatan apa pun. Compiler menganggapnya",
                    "wajar, karena memang itu arti yang kamu tulis.",
                    "",
                    "Kamu nggak perlu menghafal tabel itu. Cukup satu kebiasaan: kalau",
                    "sebuah ekspresi mencampur dua jenis operator, kasih kurung. Kurung nggak",
                    "pernah bikin program lebih lambat, dan pembacanya nggak perlu membuka",
                    "tabel.",
                    "",
                    "Tabel ini juga asal aturan yang nanti muncul di materi Preprocessor &",
                    "Macro: \"macro wajib dibungkus kurung\". Macro adalah penggantian teks",
                    "mentah, jadi hasil tempelannya dibaca ulang memakai tabel prioritas di",
                    "atas:",
                    "",
                    "  #define KUADRAT_SALAH(x) x * x",
                    "  KUADRAT_SALAH(2+3)  ->  2+3 * 2+3  ->  2 + 6 + 3  =  11   (bukan 25)",
                    "",
                    "Mengurung tiap parameter memperbaiki satu sisi. Mengurung seluruh badan",
                    "macro memperbaiki sisi lainnya, yaitu apa yang terjadi di sekeliling",
                    "macro-nya:",
                    "",
                    "  #define JUMLAH(a, b) (a) + (b)      // parameter dikurung, badannya belum",
                    "  JUMLAH(1, 2) * 3  ->  (1) + (2) * 3  =  7   (bukan 9)",
                    "",
                    "Jadi bentuk yang aman mengurung dua-duanya:",
                    "  #define JUMLAH(a, b)  ((a) + (b))",
                    "  #define KUADRAT(x)    ((x) * (x))",
                ],
            },
            {
                "heading": "Hubung-singkat: sisi kanan yang tidak pernah dijalankan",
                "body": [
                    "&& dan || punya sifat yang nggak dimiliki operator lain: keduanya",
                    "berhenti begitu hasilnya sudah pasti. Ini disebut evaluasi",
                    "hubung-singkat (short-circuit).",
                    "",
                    "  kiri && kanan  -> kalau kiri SALAH, hasilnya pasti salah; 'kanan' dilewati.",
                    "  kiri || kanan  -> kalau kiri BENAR, hasilnya pasti benar; 'kanan' dilewati.",
                    "",
                    "Sifat ini dijamin standar C, jadi kamu boleh mengandalkannya. Kode C",
                    "nyata memakainya sebagai pengaman, dan hemat waktunya cuma bonus.",
                    "Saudaranya di bitwise, & dan |, nggak punya sifat ini. Kedua sisinya",
                    "selalu dihitung.",
                    "",
                    "Ini bentuk pengaman yang bakal sering banget kamu lihat:",
                    "  if (p != NULL && p->data > 0) { ... }    // p diperiksa DULU, baru dibuka",
                    "  if (p == NULL || p->data == 0) { ... }   // kebalikannya, sama amannya",
                    "  if (!p || p->data == 0) { ... }          // sama persis, gaya lebih ringkas",
                    "  if (i < n && arr[i] > 0) { ... }         // batas array dulu, baru isinya",
                    "",
                    "Kalau urutannya dibalik jadi if (p->data > 0 && p != NULL), programnya",
                    "crash waktu p bernilai NULL. Pemeriksaannya datang terlambat.",
                    "",
                    "Contoh di bawah memakai pointer dan NULL, yang baru dibahas lengkap di",
                    "materi Pointer Dasar. Di sini cukup perhatikan satu hal: baris mana yang",
                    "nggak tercetak.",
                ],
                "code": """#include <stdio.h>

typedef struct Node {
    int data;
    struct Node *next;
} Node;

// Mencetak namanya lalu mengembalikan nilai, supaya kita LIHAT sisi
// mana yang benar-benar dijalankan.
int lapor(const char *nama, int nilai) {
    printf("    (%s ikut dievaluasi)\\n", nama);
    return nilai;
}

// Aman walaupun p bernilai NULL: p->data tidak akan pernah disentuh,
// karena sisi kirinya sudah salah lebih dulu. Pola ini yang membuat
// penelusuran linked list di Latihan 16 tidak berujung segfault.
int dataPositif(Node *p) {
    return p != NULL && p->data > 0;
}

int main(void) {
    int a = lapor("kiri", 0) && lapor("kanan", 1);
    printf("&& dengan kiri salah -> %d\\n\\n", a);

    int b = lapor("kiri", 1) || lapor("kanan", 1);
    printf("|| dengan kiri benar -> %d\\n\\n", b);

    Node n = {7, NULL};
    printf("dataPositif(&n)   = %d\\n", dataPositif(&n));
    printf("dataPositif(NULL) = %d  (tidak crash)\\n\\n", dataPositif(NULL));

    int isi[] = {4, 8, 15, 0};

    // Bentuk pengaman yang sama tanpa pointer: batas array diperiksa
    // DULU, jadi isi[9] tidak pernah dibaca sama sekali.
    int i = 9;
    if (i < 4 && isi[i] > 0) {
        printf("tidak akan pernah tercetak\\n");
    }

    // Penugasan DI DALAM kondisi: ambil elemen, simpan ke c, baru uji c.
    // Angka 0 dipakai sebagai penanda "data sudah habis".
    int c;
    i = 0;
    while ((c = isi[i++]) != 0) {
        printf("dapat %d\\n", c);
    }
    return 0;
}""",
            },
            {
                "body": [
                    "Ada tiga jebakan yang lahir langsung dari materi ini. Ketiganya sah",
                    "secara sintaks, jadi compiler nggak menolaknya. Dua yang pertama cuma",
                    "memunculkan peringatan.",
                    "",
                    "  1. if (x = 5), yaitu satu = di tempat yang seharusnya ==.",
                    "     Ekspresi x = 5 bernilai 5, dan 5 itu bukan 0, jadi kondisinya selalu",
                    "     benar. Lebih parah lagi, x ikut berubah jadi 5. Bug klasik ini bisa",
                    "     bertahan berbulan-bulan, karena programnya tetap jalan dan cuma",
                    "     jawabannya yang salah. gcc -Wall memperingatkannya dengan pesan",
                    "     'suggest parentheses around assignment used as truth value'.",
                    "     Peringatan itu jangan pernah diabaikan. Sebagian orang menulis",
                    "     if (5 == x), supaya salah ketik seperti ini jadi galat kompilasi.",
                    "  2. Kurung ganda di while ((c = isi[i++]) != 0) ada gunanya.",
                    "     Tanpa kurung dalam, kondisinya dibaca seperti di bawah, karena !=",
                    "     lebih kuat daripada =:",
                    "       while (c = isi[i++] != 0)   dibaca   c = (isi[i++] != 0)",
                    "     Akibatnya c berisi 0 atau 1, padahal yang mau disimpan adalah",
                    "     datanya, dan loop-nya salah total. Kurung itu juga jadi tanda buat",
                    "     pembaca dan compiler bahwa penugasan di situ memang disengaja.",
                    "  3. Mengubah satu variabel dua kali di dalam satu ekspresi adalah",
                    "     undefined behavior, artinya standar C nggak menentukan hasilnya.",
                    "       i = i++ + 1;      // JANGAN. Standar C tidak menentukan hasilnya.",
                    "       arr[i] = i++;     // JANGAN, alasan yang sama.",
                    "     Hasilnya juga nggak konsisten. Compiler berbeda, tingkat optimasi",
                    "     berbeda, atau versi berbeda boleh memberi hasil yang berbeda, dan",
                    "     semuanya dianggap sah. gcc -Wall menegurnya lewat -Wsequence-point.",
                    "     Hal yang mirip berlaku untuk urutan pemanggilan fungsi dalam satu",
                    "     ekspresi:",
                    "       int total = f() + g();   // f() belum tentu dijalankan sebelum g()",
                    "     Kalau f dan g saling memengaruhi, misalnya mengubah variabel yang",
                    "     sama atau sama-sama mencetak, urutannya nggak dijamin. Pisahkan",
                    "     jadi beberapa baris:",
                    "       int x = f();",
                    "       int y = g();",
                    "       int total = x + y;",
                    "",
                    "Aturan praktis untuk ketiganya: dalam satu ekspresi, ubah sebuah",
                    "variabel paling banyak sekali, dan jangan sekaligus memakainya untuk",
                    "keperluan lain.",
                ],
            },
        ],
    },
    {
        "title": "6. Input & Output (printf & scanf)",
        "sections": [
            {
                "body": [
                    "printf() menampilkan output ke layar, dan scanf() membaca input dari",
                    "keyboard.",
                    "",
                    "Waktu memakai scanf() untuk tipe selain string, tulis operator alamat",
                    "(&) di depan nama variabelnya. & artinya \"alamat dari\". scanf butuh",
                    "alamat variabelnya supaya bisa mengisi variabel itu:",
                    "  scanf(\"%d\", &umur);     // & WAJIB untuk int, float, dll",
                    "  scanf(\"%s\", nama);      // TANPA & untuk array/string (nama",
                    "                          // sudah berupa alamat, materi Pointer & Array)",
                ]
            },
            {
                "heading": "Contoh input & output dasar",
                "code": """#include <stdio.h>

int main(void) {
    int umur;
    double tinggi;
    char nama[50];   // array karakter untuk menampung string

    printf("Masukkan nama: ");
    scanf("%s", nama);          // %s berhenti di spasi pertama!

    printf("Masukkan umur: ");
    scanf("%d", &umur);         // WAJIB pakai &

    printf("Masukkan tinggi (cm): ");
    scanf("%lf", &tinggi);      // %lf untuk double di scanf

    printf("Halo %s, umur %d tahun, tinggi %.1f cm\\n", nama, umur, tinggi);
    return 0;
}"""
            },
            {
                "body": [
                    "scanf(\"%s\", ...) berhenti di spasi pertama. Jadi nama yang mengandung",
                    "spasi seperti 'Andi Wijaya' cuma terbaca 'Andi'. Untuk membaca satu",
                    "baris penuh termasuk spasinya, pakai fgets():",
                    "",
                    "  char nama[50];",
                    "  printf(\"Nama lengkap: \");",
                    "  fgets(nama, sizeof(nama), stdin);",
                    "  // fgets menyertakan karakter newline (\\n) di akhir,",
                    "  // sering perlu dibersihkan manual jika mengganggu.",
                    "",
                    "Ada juga masalah kebalikannya: scanf meninggalkan sisa newline (tanda",
                    "Enter) di belakang. Akibatnya fgets berikutnya seolah dilewati tanpa",
                    "menunggu kamu mengetik. Penyebab dan cara mengatasinya ada di materi",
                    "I/O Tingkat Karakter & Berkas Biner.",
                    "",
                    "Format printf lanjutan:",
                    "  %5d   -> tampilkan angka rata kanan, lebar minimal 5 karakter",
                    "  %-5d  -> rata kiri, lebar minimal 5",
                    "  %05d  -> isi dengan nol di depan jika kurang dari 5 digit",
                    "  %.2f  -> desimal dibulatkan 2 angka di belakang koma",
                    "  %*d   -> lebarnya diambil dari argumen, tidak ditulis tetap:",
                    "           printf(\"%*d\", 5, x) sama hasilnya dengan %5d, bedanya",
                    "           angka 5 itu boleh dihitung saat program berjalan",
                    "  %%    -> mencetak tanda persen itu sendiri. Untuk menampilkan",
                    "           'sisa bagi' apa adanya:",
                    "           printf(\"15 %% 4 = %d\\n\", 15 % 4);   -> 15 % 4 = 3",
                    "           Satu tanda persen saja akan dibaca printf sebagai",
                    "           pembuka format, dan yang tercetak jadi sampah.",
                ]
            },
        ],
    },
    {
        "title": "7. Percabangan (if / else / switch)",
        "sections": [
            {
                "body": [
                    "Sintaks if-else di C sama persis dengan Java:",
                    "  if (kondisi) {",
                    "      // jalankan jika true",
                    "  } else if (kondisi2) {",
                    "      // jalankan jika kondisi2 true",
                    "  } else {",
                    "      // jalankan jika semua false",
                    "  }",
                    "",
                    "Ada satu perbedaan penting dengan bahasa modern. Sebelum C99, C nggak",
                    "punya tipe boolean asli (C99 menambah _Bool, dan C23 menjadikan bool",
                    "kata kunci). Kondisi di C dinilai sebagai angka:",
                    "  0        -> FALSE",
                    "  selain 0 -> TRUE (termasuk angka negatif!)",
                    "",
                    "  if (5) { ... }    // TRUE, karena 5 != 0",
                    "  if (0) { ... }    // FALSE",
                    "  if (-1) { ... }   // TRUE! (sering mengejutkan pemula)",
                ]
            },
            {
                "heading": "Contoh if-else & switch",
                "code": """#include <stdio.h>

int main(void) {
    int nilai = 85;

    if (nilai >= 90) {
        printf("A\\n");
    } else if (nilai >= 80) {
        printf("B\\n");
    } else if (nilai >= 70) {
        printf("C\\n");
    } else {
        printf("D\\n");
    }
    // Output: B

    // Ternary operator (sama seperti Java)
    const char *status = (nilai >= 75) ? "Lulus" : "Tidak Lulus";
    printf("%s\\n", status);

    // switch-case
    int hari = 3;
    switch (hari) {
        case 1:
            printf("Senin\\n");
            break;
        case 2:
            printf("Selasa\\n");
            break;
        case 3:
            printf("Rabu\\n");
            break;
        default:
            printf("Hari tidak valid\\n");
    }
    return 0;
}"""
            },
            {
                "body": [
                    "switch di C, sama seperti di Java, butuh break; di tiap case. Kalau",
                    "break lupa ditulis, terjadi fall-through: eksekusi lanjut ke case",
                    "berikutnya tanpa mengecek kondisinya lagi. Ini sering jadi bug pemula.",
                    "",
                    "switch cuma bisa dipakai untuk tipe integer (int, char, enum). Untuk",
                    "float, double, atau string, switch nggak bisa dipakai. Ini beda dengan",
                    "bahasa modern seperti JS, yang punya switch untuk string.",
                    "",
                    "Ada satu bentuk di contoh tadi yang belum waktunya dibahas: const char",
                    "*status. Itu bukan tipe \"string\". Itu pointer ke teks, yaitu variabel",
                    "yang menyimpan alamat tempat teks itu berada. const artinya teks yang",
                    "ditunjuk nggak boleh diubah. Untuk sekarang, baca aja sebagai",
                    "\"penampung teks\". Detailnya ada di materi String Lanjutan: char *,",
                    "const & Keluarga mem*.",
                ]
            },
            {
                "heading": "Kurawal boleh dihilangkan - dan di situ jebakannya",
                "body": [
                    "if, else, for, dan while masing-masing mengikat tepat satu pernyataan.",
                    "Kalau isinya memang cuma satu, kurawalnya boleh nggak ditulis:",
                    "",
                    "  if (n < 0) printf(\"negatif\\n\");",
                    "  if (i == 5) continue;      // bentuk ini muncul di materi",
                    "                             // Perulangan berikutnya",
                    "  if (!p) return NULL;       // idiom 'pulang lebih awal',",
                    "                             // sangat umum di kode C nyata",
                    "",
                    "Kurawal { } itu bukan bagian dari if. Kurawal adalah alat untuk",
                    "menggabungkan banyak pernyataan jadi satu. Makanya bentuk tanpa kurawal",
                    "juga sah.",
                    "",
                    "Jebakannya baru muncul waktu kamu menambah baris kedua nanti:",
                    "",
                    "  if (saldo < 0)",
                    "      printf(\"saldo minus\\n\");",
                    "      saldo = 0;      // BUKAN bagian if! selalu jalan, walau",
                    "                      // saldonya 100",
                    "",
                    "Indentasinya menipu. Compiler cuma membaca pernyataan pertama sesudah",
                    "if. gcc -Wall memang menegur kasus ini (-Wmisleading-indentation), tapi",
                    "kalau barisnya ditulis rata kiri, peringatan itu nggak muncul lagi.",
                    "Makanya banyak proyek besar, salah satunya kernel Linux, mewajibkan",
                    "kurawal begitu badannya lebih dari satu baris. Menulis kurawal setiap",
                    "saat juga nggak pernah salah.",
                ]
            },
        ],
    },
    {
        "title": "8. Perulangan (for, while, do-while)",
        "sections": [
            {
                "body": [
                    "Sintaks loop di C sama persis dengan Java, karena Java memang",
                    "mewarisinya dari C:",
                    "",
                    "  for (awal; kondisi; update) { ... }",
                    "  while (kondisi) { ... }",
                    "  do { ... } while (kondisi);   // pasti jalan minimal 1x",
                    "",
                    "Ketiganya mengulang kode selama kondisinya benar. Bedanya, do-while",
                    "mengecek kondisinya di akhir, jadi badannya pasti jalan minimal sekali.",
                    "",
                    "Ada dua kata kunci untuk mengatur loop. Satu putaran loop disebut",
                    "iterasi.",
                    "  break    -> menghentikan loop sepenuhnya.",
                    "  continue -> lompat ke iterasi berikutnya.",
                ]
            },
            {
                "heading": "Contoh semua jenis loop",
                "code": """#include <stdio.h>

int main(void) {
    // for
    for (int i = 1; i <= 5; i++) {
        printf("%d ", i);
    }
    printf("\\n");   // 1 2 3 4 5

    // while
    int j = 1;
    while (j <= 5) {
        printf("%d ", j);
        j++;
    }
    printf("\\n");   // 1 2 3 4 5

    // do-while (pasti jalan minimal sekali)
    int k = 10;
    do {
        printf("k = %d\\n", k);
        k++;
    } while (k < 3);   // k = 10 (cetak sekali walau kondisi langsung false)

    // break & continue
    for (int i = 1; i <= 10; i++) {
        if (i == 5) continue;
        if (i == 8) break;
        printf("%d ", i);
    }
    printf("\\n");   // 1 2 3 4 6 7

    // nested loop: pola segitiga bintang
    for (int i = 1; i <= 4; i++) {
        for (int j = 1; j <= i; j++) {
            printf("*");
        }
        printf("\\n");
    }
    return 0;
}"""
            },
        ],
    },
    {
        "title": "9. Array",
        "sections": [
            {
                "body": [
                    "Array di C adalah deretan elemen yang disimpan berurutan di memori,",
                    "dengan ukuran tetap. Untuk array biasa, ukurannya harus sudah diketahui",
                    "waktu kompilasi. Semua elemennya juga harus bertipe sama.",
                    "",
                    "  int angka[5];                  // 5 int, isi awal 'sampah' (undefined)",
                    "  int angka[5] = {1, 2, 3, 4, 5}; // langsung dengan nilai",
                    "  int angka[] = {1, 2, 3};        // ukuran otomatis dari jumlah elemen",
                    "",
                    "Elemen diambil lewat indeks yang mulai dari 0, sama seperti di Java:",
                    "  angka[0] -> elemen pertama",
                    "  angka[4] -> elemen terakhir (untuk array ukuran 5)",
                    "",
                    "Jebakan: C nggak memeriksa batas array (bounds-checking). Kalau kamu",
                    "menulis di luar array, nggak ada error, baik waktu kompilasi maupun",
                    "waktu program jalan. Memori di sebelah array yang jadi rusak:",
                    "  angka[10] = 99;   // TIDAK error saat kompilasi ATAU runtime,",
                    "                    // tapi MERUSAK memori di luar array",
                    "                    // (undefined behavior - bisa crash, bisa",
                    "                    // 'diam-diam salah' - bug paling berbahaya di C)",
                ]
            },
            {
                "heading": "Contoh operasi array",
                "code": """#include <stdio.h>

int main(void) {
    int nilai[] = {80, 90, 75, 85};
    int n = sizeof(nilai) / sizeof(nilai[0]);   // cara mendapat JUMLAH elemen

    printf("Jumlah elemen: %d\\n", n);

    for (int i = 0; i < n; i++) {
        printf("Indeks %d: %d\\n", i, nilai[i]);
    }

    int total = 0;
    for (int i = 0; i < n; i++) {
        total += nilai[i];
    }
    double rata = (double) total / n;
    printf("Total: %d, Rata-rata: %.2f\\n", total, rata);

    // Array 2 dimensi (matriks)
    int matriks[2][3] = {
        {1, 2, 3},
        {4, 5, 6}
    };
    printf("matriks[0][1] = %d\\n", matriks[0][1]);   // 2

    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 3; j++) {
            printf("%d ", matriks[i][j]);
        }
        printf("\\n");
    }
    return 0;
}"""
            },
            {
                "body": [
                    "Rumus sizeof(nilai)/sizeof(nilai[0]) cuma bekerja untuk array yang",
                    "dideklarasikan langsung. Rumus ini nggak bekerja untuk hasil malloc,",
                    "atau untuk array yang diterima sebagai parameter fungsi. Alasannya",
                    "dibahas di materi pointer: array \"meluruh\" jadi pointer waktu dikirim",
                    "sebagai parameter fungsi.",
                    "",
                    "Catatan: aturan \"ukuran harus diketahui waktu kompilasi\" itu berlaku",
                    "untuk C89. Sejak C99, aturan itu nggak mutlak lagi. Kode ini sah:",
                    "",
                    "  int n;",
                    "  scanf(\"%d\", &n);",
                    "  int buf[n];      // variable length array (VLA): ukurannya baru",
                    "                   // diketahui saat program berjalan",
                    "",
                    "Harganya nggak kecil, makanya VLA jarang dipakai:",
                    "  - Tempatnya diambil dari stack, yaitu area memori kecil yang dipakai",
                    "    fungsi untuk variabel lokalnya. Kalau n besar (misalnya sejuta),",
                    "    yang terjadi crash mendadak, tanpa pesan error yang jelas.",
                    "  - Ukurannya nggak bisa diubah lagi sesudah dibuat, dan isinya ikut",
                    "    hilang begitu fungsinya selesai.",
                    "  - Sejak C11, VLA jadi fitur opsional bagi compiler. MSVC (compiler C",
                    "    bawaan Visual Studio) nggak mendukungnya sama sekali.",
                    "",
                    "Untuk array besar, array yang harus hidup lebih lama dari fungsinya,",
                    "atau array yang ukurannya masih akan berubah, pakai malloc. Caranya ada",
                    "di materi Dynamic Memory Allocation.",
                ]
            },
        ],
    },
    {
        "title": "10. String (Array of Char)",
        "sections": [
            {
                "body": [
                    "C nggak punya tipe string asli seperti Java atau Python. String di C",
                    "adalah array of char, yaitu deretan karakter, yang diakhiri karakter",
                    "null terminator ('\\0'). Karakter '\\0' itu penanda \"string selesai di",
                    "sini\".",
                    "",
                    "  char nama[] = \"Andi\";",
                    "  // Sebenarnya tersimpan sebagai: {'A','n','d','i','\\0'}",
                    "  // Perhatikan array butuh 5 slot untuk 4 huruf + '\\0'!",
                    "",
                    "  char nama2[20] = \"Budi\";   // ukuran cukup, sisanya kosong",
                    "  char nama3[3] = \"Budi\";    // BAHAYA! 'Budi'+'\\0' butuh 5,",
                    "                              // hanya ada 3 slot -> buffer overflow!",
                    "",
                    "Buffer overflow artinya menulis melewati batas tempat yang tersedia.",
                ]
            },
            {
                "heading": "Fungsi string dari <string.h>",
                "code": """#include <stdio.h>
#include <string.h>

int main(void) {
    char nama[50] = "Andi";
    char kota[50] = "Jakarta";

    printf("Panjang: %zu\\n", strlen(nama));     // 4 (TIDAK termasuk \\0)

    strcat(nama, " dari ");     // gabung (concatenate) - HATI-HATI overflow!
    strcat(nama, kota);
    printf("%s\\n", nama);       // "Andi dari Jakarta"

    char salinan[50];
    strcpy(salinan, nama);      // salin string
    printf("Salinan: %s\\n", salinan);

    if (strcmp("Andi", "andi") == 0) {   // strcmp: 0 jika SAMA PERSIS
        printf("Sama\\n");
    } else {
        printf("Beda (case-sensitive!)\\n");   // ini yang tercetak
    }

    printf("strcmp hasil: %d\\n", strcmp("apel", "jeruk"));  // negatif ('a'<'j')
    return 0;
}"""
            },
            {
                "body": [
                    "Ada tiga hal soal string di C yang perlu kamu waspadai:",
                    "  1. strcpy dan strcat nggak mengecek ukuran tujuan, jadi gampang",
                    "     overflow. Untuk kode production biasanya disarankan strncpy dan",
                    "     strncat, yaitu versi yang diberi batas panjang. Materi String",
                    "     Lanjutan nanti menunjukkan bahwa strncpy pun punya jebakan.",
                    "  2. Lupa menyediakan tempat untuk '\\0' adalah bug klasik pemula.",
                    "  3. Membandingkan string harus pakai strcmp(), jangan pakai ==. Tanda",
                    "     == membandingkan alamat array, dan isinya nggak ikut dibandingkan.",
                    "     Mirip masalah is vs == di Python, atau == vs equals() di Java,",
                    "     cuma akibatnya lebih parah di C.",
                    "",
                    "Fungsi lain dari string.h yang berguna:",
                    "  strlen(s), strcpy(dst,src), strncpy(dst,src,n),",
                    "  strcat(dst,src), strcmp(a,b), strchr(s,c), strstr(s,sub)",
                    "",
                    "  strncat(dst,src,n)   gabung dengan batas panjang - pasangan",
                    "                       aman dari strcat",
                    "  strrchr(s,c)         cari karakter c dari BELAKANG. Inilah cara",
                    "                       mengambil ekstensi berkas ('.' terakhir)",
                    "                       atau nama berkas dari sebuah path ('/')",
                    "  strspn(s,set)        berapa karakter PERTAMA s yang semuanya",
                    "                       masih anggota set",
                    "  strtok(s,pemisah)    memecah satu string jadi potongan -",
                    "                       tulang punggung hampir semua parser",
                    "                       sederhana (CSV, baris konfigurasi, kalimat)",
                ]
            },
            {
                "heading": "Memecah string dengan strtok, dan mencari dari belakang",
                "code": """#include <stdio.h>
#include <string.h>

int main(void) {
    // strtok MENGUBAH string yang dipecah: tiap pemisah ditimpa \'\\0\'.
    // Jadi jangan pernah memberinya string literal langsung - literal itu
    // read-only dan programnya bisa crash. Salin dulu ke array seperti ini.
    char baris[] = "andi,budi,cici";

    char *kata = strtok(baris, ",");    // panggilan PERTAMA: kirim stringnya
    while (kata != NULL) {
        printf("[%s]\\n", kata);
        kata = strtok(NULL, ",");       // panggilan berikutnya: kirim NULL!
    }

    char berkas[] = "laporan.akhir.txt";
    char *titik = strrchr(berkas, \'.\');       // \'.\' terakhir, bukan yang pertama
    printf("ekstensi: %s\\n", titik + 1);      // txt

    printf("digit di depan: %zu\\n", strspn("2024tahun", "0123456789"));
    return 0;
}"""
            },
            {
                "body": [
                    "Ada dua hal tentang strtok yang sering bikin orang tersandung:",
                    "  1. Panggilan pertama menerima string-nya. Panggilan selanjutnya",
                    "     menerima NULL. Dari NULL itu strtok tahu dia harus melanjutkan",
                    "     string yang tadi.",
                    "  2. strtok merusak string aslinya, dan menyimpan posisi terakhirnya di",
                    "     satu tempat tersembunyi. Jadi dua pemecahan nggak boleh berjalan",
                    "     bersamaan.",
                    "",
                    "strdup(s) menyalin string sekaligus menyediakan tempat untuk",
                    "salinannya. Fungsi ini umum di kode nyata. Sampai C17, strdup milik",
                    "POSIX dan nggak termasuk C standar. Baru C23 yang memasukkannya ke",
                    "standar. Hasilnya wajib di-free (materi Dynamic Memory Allocation). Di",
                    "compiler yang dipaksa ketat ke standar lama (-std=c11), namanya bisa",
                    "nggak dikenal.",
                    "",
                    "Keluarga mem* (memcpy, memset, memcmp) dan snprintf, yang menutup",
                    "lubang keamanan strcpy, dibahas di materi String Lanjutan: char *,",
                    "const & Keluarga mem*.",
                ]
            },
        ],
    },
    {
        "title": "11. Pustaka Standar: math.h, ctype.h, stdlib & time.h",
        "sections": [
            {
                "body": [
                    "Sampai sini kamu sudah memakai beberapa header, misalnya <stdio.h>,",
                    "<string.h>, <stdbool.h>, <limits.h>, dan <stdint.h>. Pustaka standar C",
                    "jauh lebih luas dari itu. Ada fungsi matematika, pemeriksa karakter,",
                    "pengubah teks jadi angka, dan penanggalan. Semuanya sudah ikut",
                    "compiler, jadi nggak ada yang perlu diunduh atau dipasang. Kamu cuma",
                    "perlu tahu nama header-nya.",
                    "",
                    "Sebelum lanjut, ada hal kecil yang jarang dijelaskan: berkas header",
                    "(.h) itu cuma janji.",
                    "  - Isinya deklarasi: nama fungsi, tipe parameternya, dan tipe nilai",
                    "    kembaliannya.",
                    "  - Kode mesin fungsinya nggak ada di situ. Kode mesin itu tinggal di",
                    "    berkas pustaka terpisah. Yang menyambungkannya ke programmu adalah",
                    "    linker, yaitu tahap yang berjalan sesudah kompilasi selesai.",
                    "",
                    "Untuk stdio.h, stdlib.h, string.h, dan ctype.h, pustakanya (namanya",
                    "libc) ditautkan otomatis oleh gcc. <math.h> adalah pengecualian dari",
                    "zaman dulu. Kode mesinnya ada di pustaka terpisah bernama libm, dan gcc",
                    "nggak menautkan libm kecuali kamu memintanya.",
                    "",
                    "Jadi program yang memakai sqrt() lalu dikompilasi begini:",
                    "  gcc hitung.c -o hitung",
                    "",
                    "gagal dengan pesan yang kira-kira berbunyi seperti ini:",
                    "  /usr/bin/ld: /tmp/ccQx1a.o: in function `main':",
                    "  hitung.c:(.text+0x1f): undefined reference to `sqrt'",
                    "  collect2: error: ld returned 1 exit status",
                    "",
                    "Coba baca pesannya lagi. Yang mengeluh adalah ld, si linker, dan",
                    "compiler-nya sendiri nggak protes. Nggak ada satu pun baris kodemu yang",
                    "salah. Yang kurang adalah pustakanya. Makanya nomor baris yang disebut",
                    "nggak menunjuk ke kode yang masuk akal, dan mencari salah ketik di kode",
                    "cuma buang waktu.",
                    "",
                    "Obatnya dua huruf: -lm. -l artinya \"tautkan pustaka\", dan m adalah nama",
                    "pustakanya.",
                    "  gcc hitung.c -o hitung -lm",
                    "",
                    "Taruh -lm di akhir, sesudah nama berkas. Urutan argumen itu ada artinya",
                    "buat linker. Kalau ditulis di depan nama berkas, kompilasinya bisa tetap",
                    "gagal dengan pesan yang sama persis.",
                    "",
                    "Catatan soal aplikasi ini: tombol 'Coba jalankan' di sini sudah",
                    "memasang -lm untukmu, jadi kamu nggak akan melihat galat itu di layar",
                    "ini. Tapi perintah di petunjuk berkas tiap contoh ('gcc nama.c -o",
                    "nama') belum memuat -lm. Kalau kamu mengetik sendiri di terminal,",
                    "tambahkan -lm. Kalau lupa, program pertamamu yang memakai sqrt() bakal",
                    "gagal dengan pesan di atas, dan kamu bisa mengira ada yang rusak.",
                ],
            },
            {
                "heading": "<math.h>: fungsi yang paling sering terpakai",
                "body": [
                    "Semua fungsi di bawah ini bekerja dengan double: argumennya double, dan",
                    "hasilnya juga double. Memberinya int boleh aja, karena int otomatis",
                    "dinaikkan jadi double. Masalahnya muncul kalau hasilnya ditampung di",
                    "int, karena pecahannya bakal terpotong.",
                    "",
                    "  sqrt(x)      akar kuadrat              sqrt(9.0)      -> 3.0",
                    "  pow(x, y)    x pangkat y               pow(2.0, 10.0) -> 1024.0",
                    "  fabs(x)      nilai mutlak (double)     fabs(-2.5)     -> 2.5",
                    "  floor(x)     bulatkan ke BAWAH         floor(-2.5)    -> -3.0",
                    "  ceil(x)      bulatkan ke ATAS          ceil(2.1)      -> 3.0",
                    "  round(x)     bulatkan ke yang terdekat round(2.5)     -> 3.0",
                    "  fmod(x, y)   sisa bagi untuk desimal   fmod(7.5, 2.0) -> 1.5",
                    "",
                    "Ada tiga jebakan yang sering kena:",
                    "  1. (int) x memotong ke arah nol, sedangkan floor() membulatkan ke",
                    "     arah minus tak hingga. Untuk angka positif, hasil keduanya sama,",
                    "     jadi bugnya nggak kelihatan. Lalu suatu hari datanya negatif, dan",
                    "     (int) -2.5 memberi -2 sementara floor(-2.5) memberi -3.",
                    "  2. Operator % nggak bisa dipakai untuk double sama sekali. 7.5 % 2.0",
                    "     langsung jadi error kompilasi. Untuk sisa bagi desimal, pakai",
                    "     fmod().",
                    "  3. fabs() untuk double, abs() untuk int, dan abs() itu ada di",
                    "     <stdlib.h>, nggak di <math.h>. Yang berbahaya: abs(-3.7) lolos",
                    "     kompilasi tanpa peringatan kalau kamu cuma pakai -Wall, lalu",
                    "     mengembalikan 3. Penyebabnya, -3.7 dipotong jadi -3 dulu sebelum",
                    "     masuk ke abs(). Baru -Wextra yang menegurnya (-Wabsolute-value).",
                ],
                "code": """#include <stdio.h>
#include <math.h>

int main(void) {
    double x = 2.5;
    double y = -2.5;

    printf("sqrt(9.0)      = %.2f\\n", sqrt(9.0));
    printf("pow(2.0, 10.0) = %.1f\\n", pow(2.0, 10.0));
    printf("fabs(%.1f)     = %.1f\\n", y, fabs(y));

    printf("floor(%.1f) = %.1f   ceil(%.1f) = %.1f\\n", x, floor(x), x, ceil(x));
    printf("floor(%.1f) = %.1f   ceil(%.1f) = %.1f\\n", y, floor(y), y, ceil(y));

    // (int) memotong ke arah NOL, floor() turun ke arah minus tak hingga
    printf("(int)%.1f = %d  TAPI floor(%.1f) = %.1f\\n", y, (int) y, y, floor(y));

    // round() membulatkan MENJAUHI nol saat pecahannya tepat setengah
    printf("round(2.5) = %.1f   round(-2.5) = %.1f\\n", round(2.5), round(-2.5));

    // Operator % hanya untuk bilangan bulat; untuk desimal pakai fmod()
    printf("fmod(7.5, 2.0) = %.2f\\n", fmod(7.5, 2.0));

    // Kasus nyata: jarak dua titik (teorema Pythagoras)
    double dx = 3.0, dy = 4.0;
    printf("Jarak = %.2f\\n", sqrt(pow(dx, 2.0) + pow(dy, 2.0)));
    return 0;
}""",
            },
            {
                "heading": "<ctype.h>: memeriksa dan mengubah SATU karakter",
                "body": [
                    "Isi <ctype.h> adalah fungsi yang menjawab pertanyaan tentang satu",
                    "karakter, dan fungsi yang mengubah satu karakter. Namanya seragam: yang",
                    "diawali is... bertanya, yang diawali to... mengubah.",
                    "",
                    "  isdigit(c)   apakah '0'..'9'?           isupper(c)   huruf besar?",
                    "  isalpha(c)   apakah huruf?              islower(c)   huruf kecil?",
                    "  isalnum(c)   huruf ATAU angka?          toupper(c)   jadikan huruf besar",
                    "  isspace(c)   spasi, tab, atau newline?  tolower(c)   jadikan huruf kecil",
                    "",
                    "Kenapa harus memanggil isdigit(c), padahal bisa menulis c >= '0' && c",
                    "<= '9'? Ada beberapa alasan:",
                    "  - Niatnya langsung terbaca oleh siapa pun yang membaca kodemu nanti.",
                    "  - isspace() benar untuk semua karakter putih (whitespace): spasi,",
                    "    '\\t', '\\n', '\\r', dan dua lagi yang jarang dipakai. Versi tulisan",
                    "    tangan hampir selalu kelewatan salah satunya.",
                    "  - Kamu nggak perlu berasumsi huruf tersusun berurutan di tabel",
                    "    karakter mesin yang menjalankan programmu.",
                    "",
                    "Ada tiga jebakan:",
                    "  1. Fungsi is...() nggak menjanjikan nilai 1. Standarnya cuma bilang",
                    "     \"nol kalau bukan, selain nol kalau ya\". Jadi jangan menulis",
                    "     if (isalpha(c) == 1). Cukup tulis if (isalpha(c)).",
                    "  2. toupper() mengembalikan karakter baru, dan karakter lamanya nggak",
                    "     diubah. Baris toupper(s[i]); yang berdiri sendiri nggak melakukan",
                    "     apa-apa, dan compiler nggak akan mengeluh. Yang benar:",
                    "     s[i] = toupper(s[i]);",
                    "  3. Argumennya harus bernilai unsigned char atau EOF. Di banyak mesin,",
                    "     char itu bertanda. Akibatnya byte di atas 127 (huruf beraksen, teks",
                    "     UTF-8) bernilai negatif, dan itu undefined behavior. Kebiasaan yang",
                    "     aman: isalpha((unsigned char) s[i]).",
                    "",
                    "Karakter yang bukan huruf dibiarkan apa adanya oleh toupper dan",
                    "tolower. Makanya kamu bisa menjalankannya atas seluruh string, tanpa",
                    "memilah dulu mana yang huruf dan mana yang bukan.",
                ],
                "code": """#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main(void) {
    char kalimat[] = "Aku belajar C sejak 2024, tiap hari!";
    int huruf = 0, angka = 0, spasi = 0, lainnya = 0;

    for (int i = 0; kalimat[i] != '\\0'; i++) {
        unsigned char c = (unsigned char) kalimat[i];   // aman untuk ctype.h
        if (isalpha(c)) {
            huruf++;
        } else if (isdigit(c)) {
            angka++;
        } else if (isspace(c)) {
            spasi++;
        } else {
            lainnya++;
        }
    }

    printf("Kalimat: %s\\n", kalimat);
    printf("Huruf  : %d\\n", huruf);
    printf("Angka  : %d\\n", angka);
    printf("Spasi  : %d\\n", spasi);
    printf("Lainnya: %d\\n", lainnya);

    // toupper MENGEMBALIKAN karakter baru, jadi hasilnya HARUS disimpan
    char besar[64];
    strcpy(besar, kalimat);
    for (int i = 0; besar[i] != '\\0'; i++) {
        besar[i] = (char) toupper((unsigned char) besar[i]);
    }
    printf("Huruf besar: %s\\n", besar);

    // Yang bukan huruf tidak disentuh sama sekali
    printf("toupper('7') tetap '%c', tolower('#') tetap '%c'\\n",
           toupper('7'), tolower('#'));
    return 0;
}""",
            },
            {
                "heading": "<stdlib.h>: teks jadi angka, dan kenapa atoi berbahaya",
                "body": [
                    "Angka yang datang dari luar program, seperti argumen command line, isi",
                    "berkas, atau hasil fgets(), selalu berbentuk teks. Di C, \"123\" nggak",
                    "berubah jadi 123 dengan sendirinya. Kamu harus memanggil fungsi",
                    "konversi.",
                    "",
                    "  atoi(s)   teks -> int      atof(s)   teks -> double",
                    "  atol(s)   teks -> long     strtol(s, &sisa, basis)   versi yang benar",
                    "",
                    "Masalah atoi(): dia nggak punya cara memberi tahu kalau gagal.",
                    "  - atoi(\"nol\") mengembalikan 0. atoi(\"0\") juga mengembalikan 0. Nggak",
                    "    ada cara membedakan masukan rusak dari angka nol yang sah.",
                    "  - atoi(\"12abc\") mengembalikan 12, dan nggak bilang apa-apa soal 'abc'",
                    "    yang dibuang.",
                    "",
                    "Di program sungguhan, artinya salah ketik pengguna berubah jadi angka 0",
                    "yang kelihatan wajar, lalu ikut dihitung tanpa ada tanda bahaya.",
                    "",
                    "strtol() memperbaiki masalah itu lewat parameter keduanya, yaitu",
                    "endptr:",
                    "  char *sisa;",
                    "  long n = strtol(teks, &sisa, 10);",
                    "",
                    "strtol mengisi sisa dengan alamat karakter pertama yang nggak ikut",
                    "terbaca. Dari situ kamu bisa memeriksa dua hal:",
                    "  sisa == teks    -> tidak ada satu angka pun di awal teks",
                    "  *sisa != '\\0'   -> ada angka, tapi masih ada sampah di belakangnya",
                    "",
                    "Parameter ketiga adalah basis: 10 untuk desimal, 16 untuk",
                    "heksadesimal, 2 untuk biner, dan 0 artinya \"tebak dari awalannya\" (0x",
                    "berarti heksa, 0 di depan berarti oktal). Ini nyambung dengan materi",
                    "Bilangan Biner & Heksadesimal. Versi untuk double namanya strtod().",
                    "",
                    "Masih dari <stdlib.h>: abs() untuk int, labs() untuk long, dan llabs()",
                    "untuk long long. Bedanya ada di tipe, dan besar angkanya nggak",
                    "menentukan pilihan. Kalau abs() dipakai untuk sebuah long, nilainya",
                    "bisa terpotong di mesin yang long-nya lebih lebar daripada int.",
                ],
                "code": """#include <stdio.h>
#include <stdlib.h>

int main(void) {
    printf("atoi(\\"123\\")   = %d\\n", atoi("123"));
    printf("atoi(\\"12abc\\") = %d\\n", atoi("12abc"));   // berhenti diam-diam
    printf("atoi(\\"nol\\")   = %d\\n", atoi("nol"));     // 0, persis atoi("0")
    printf("atof(\\"3.14\\")  = %.2f\\n", atof("3.14"));
    printf("\\n");

    const char *masukan[] = {"42", "12abc", "nol", "  7"};
    for (int i = 0; i < 4; i++) {
        char *sisa;
        long nilai = strtol(masukan[i], &sisa, 10);   // 10 = basis desimal

        if (sisa == masukan[i]) {
            printf("\\"%s\\" -> tidak ada angka sama sekali\\n", masukan[i]);
        } else if (*sisa != '\\0') {
            printf("\\"%s\\" -> terbaca %ld, tapi ada sisa \\"%s\\"\\n",
                   masukan[i], nilai, sisa);
        } else {
            printf("\\"%s\\" -> %ld (bersih, seluruh teks terpakai)\\n",
                   masukan[i], nilai);
        }
    }
    printf("\\n");

    printf("strtol(\\"ff\\", NULL, 16)  = %ld\\n", strtol("ff", NULL, 16));
    printf("strtol(\\"0x1A\\", NULL, 0) = %ld\\n", strtol("0x1A", NULL, 0));
    printf("abs(-7) = %d   labs(-1234567890L) = %ld\\n",
           abs(-7), labs(-1234567890L));
    return 0;
}""",
            },
            {
                "heading": "rand() & <time.h>: bacaan, dengan alasannya",
                "body": [
                    "Bagian ini sengaja cuma jadi bacaan, dan alasannya begini. Aplikasi ini",
                    "menilai jawaban dengan membandingkan keluaran programmu dengan keluaran",
                    "yang benar. Program yang memakai rand() tanpa benih tetap, time(NULL),",
                    "atau clock() menghasilkan keluaran berbeda tiap kali dijalankan, jadi",
                    "mustahil dicocokkan. Karena itu topik ini nggak punya latihan yang",
                    "dinilai otomatis. Pahami cara kerjanya di sini, lalu coba-coba sendiri",
                    "di terminalmu.",
                    "",
                    "rand() dari <stdlib.h> menghasilkan bilangan semu-acak dari 0 sampai",
                    "RAND_MAX. Nilai RAND_MAX dijamin minimal 32767, dan di banyak sistem",
                    "jauh lebih besar.",
                    "  - Tanpa srand(), urutan angkanya sama persis setiap kali program",
                    "    dijalankan. Memang begitu perilakunya, dan ini berguna kalau kamu",
                    "    butuh hasil yang bisa diulang. Pemula sering mengira mesinnya yang",
                    "    rusak.",
                    "  - srand(benih) menentukan titik awal urutannya. Pola yang umum:",
                    "      srand((unsigned) time(NULL));   // benih dari detik saat ini",
                    "  - srand() dipanggil sekali di awal main(), jangan di dalam loop.",
                    "    Kalau di dalam loop, semua putaran yang jatuh di detik yang sama",
                    "    memakai benih yang sama, dan menghasilkan angka yang sama",
                    "    berulang-ulang. Bug klasik ini bikin orang menyimpulkan rand()",
                    "    rusak.",
                    "  - Membatasi rentang: rand() % 6 + 1 untuk dadu 1..6. Sisa bagi",
                    "    seperti ini sedikit memiringkan peluangnya. Cukup untuk permainan,",
                    "    tapi nggak cukup untuk kata sandi atau kunci. rand() memang nggak",
                    "    dibuat untuk keamanan.",
                    "",
                    "<time.h> berputar di sekitar tipe time_t: satu bilangan berisi jumlah",
                    "detik sejak 1 Januari 1970 UTC, yang disebut Unix epoch.",
                    "  time_t sekarang = time(NULL);   // NULL: kita cuma mau nilai baliknya",
                    "",
                    "Angka detik itu nggak enak dibaca, jadi dipecah dulu jadi struct tm:",
                    "  localtime(&t) -> struct tm menurut zona waktu MESIN yang menjalankan",
                    "  gmtime(&t)    -> struct tm dalam UTC, sama di mesin mana pun",
                    "",
                    "Keduanya mengembalikan pointer ke satu buffer internal yang dipakai",
                    "bersama. Panggilan berikutnya menimpa hasil sebelumnya. Jadi kalau kamu",
                    "menyimpan dua pointer dari dua panggilan, keduanya menunjuk isi yang",
                    "sama. Jebakan ini bikin bingung banget waktu pertama kali kena.",
                    "",
                    "Ada dua field struct tm yang hampir selalu salah dipakai pertama kali:",
                    "  tm_year  jumlah tahun SEJAK 1900   -> tahun asli = tm_year + 1900",
                    "  tm_mon   bulan mulai dari 0        -> bulan asli = tm_mon + 1",
                    "  (tm_mday sudah 1..31. Ya, ketiganya memang tidak seragam.)",
                    "",
                    "strftime(buf, ukuran, format, &tm) menulis waktu jadi teks yang siap",
                    "ditampilkan:",
                    "  %Y tahun 4 digit   %m bulan   %d tanggal",
                    "  %H jam             %M menit   %S detik",
                    "",
                    "Nilai kembaliannya adalah jumlah karakter yang ditulis, atau 0 kalau",
                    "nggak muat.",
                    "",
                    "difftime(akhir, awal) memberi selisih dua time_t dalam detik, bertipe",
                    "double. Kenapa nggak dikurangi biasa aja? Standar C nggak menjanjikan",
                    "time_t berupa \"detik dalam bentuk angka biasa\", jadi difftime adalah",
                    "cara yang portabel.",
                    "",
                    "clock() mengukur waktu prosesor yang terpakai, dan itu nggak sama",
                    "dengan waktu jam dinding:",
                    "  clock_t mulai = clock();",
                    "  /* ... kerjakan sesuatu yang berat ... */",
                    "  double detik = (double)(clock() - mulai) / CLOCKS_PER_SEC;",
                    "",
                    "Program yang menunggu masukan atau tidur bakal menunjukkan hampir 0",
                    "detik, karena selama menunggu, prosesornya memang nggak mengerjakan",
                    "apa-apa.",
                    "",
                    "Contoh di bawah memakai waktu yang dipatok, dan nggak memakai",
                    "time(NULL), supaya keluarannya bisa diperiksa. Trik yang sama dipakai",
                    "kalau kamu mau menulis tes untuk kode yang bergantung pada waktu.",
                ],
                "code": """#include <stdio.h>
#include <time.h>

int main(void) {
    // Dipatok, bukan time(NULL), supaya keluaran program ini selalu sama.
    time_t awal  = 1700000000;   // detik ke-1.700.000.000 sejak 1 Jan 1970
    time_t akhir = 1700090000;

    // gmtime = UTC, sama di mesin mana pun. localtime = zona waktu mesin,
    // jadi hasilnya berbeda di Jakarta dan di London.
    struct tm *bagian = gmtime(&awal);

    printf("tm_year mentah : %d  -> tahun %d\\n", bagian->tm_year,
           bagian->tm_year + 1900);
    printf("tm_mon  mentah : %d   -> bulan %d\\n", bagian->tm_mon,
           bagian->tm_mon + 1);
    printf("tm_mday        : %d  (yang ini sudah 1..31)\\n", bagian->tm_mday);

    char teks[64];
    strftime(teks, sizeof(teks), "%d-%m-%Y %H:%M:%S", bagian);
    printf("Diformat       : %s UTC\\n", teks);

    double selisih = difftime(akhir, awal);
    printf("Selisih        : %.0f detik = %.1f jam\\n", selisih, selisih / 3600.0);
    return 0;
}""",
            },
        ],
    },
    {
        "title": "12. Function (Fungsi)",
        "sections": [
            {
                "body": [
                    "Function (fungsi) adalah sekumpulan kode yang diberi nama, supaya bisa",
                    "dipanggil berkali-kali. Sintaksnya begini:",
                    "  tipeKembali namaFungsi(parameter) {",
                    "      // isi fungsi",
                    "      return nilai;   // jika tipeKembali bukan void",
                    "  }",
                    "",
                    "Secara tradisional, C butuh fungsi dideklarasikan atau didefinisikan",
                    "sebelum dipanggil. Ini beda dengan Java, yang boleh memanggil method di",
                    "mana aja dalam class.",
                    "",
                    "Solusinya, tulis function prototype, yaitu deklarasi fungsi tanpa isi,",
                    "di bagian atas. Definisi lengkapnya boleh ditaruh di bawah main().",
                ]
            },
            {
                "heading": "Contoh function & prototype",
                "code": """#include <stdio.h>

// Function prototype (deklarasi) - beri tahu compiler fungsi ini akan ada
int tambah(int a, int b);
void tampilkanInfo(char bahasa[]);

int main(void) {
    int hasil = tambah(10, 5);
    printf("10 + 5 = %d\\n", hasil);
    tampilkanInfo("C");
    return 0;
}

// Function definition (isi lengkap) - boleh diletakkan setelah main()
int tambah(int a, int b) {
    return a + b;
}

void tampilkanInfo(char bahasa[]) {
    printf("Belajar %s itu membuka wawasan tentang komputer!\\n", bahasa);
}"""
            },
            {
                "body": [
                    "Pass by value adalah cara bawaan C mengirim parameter. Fungsi menerima",
                    "salinan nilainya, dan variabel aslinya nggak ikut terkirim. Jadi",
                    "mengubah parameter di dalam fungsi nggak memengaruhi variabel asli di",
                    "luar fungsi:",
                    "",
                    "  void tambahSatu(int x) {",
                    "      x = x + 1;   // hanya mengubah SALINAN lokal",
                    "  }",
                    "  int main(void) {",
                    "      int angka = 5;",
                    "      tambahSatu(angka);",
                    "      printf(\"%d\", angka);  // TETAP 5, bukan 6!",
                    "  }",
                    "",
                    "Untuk mengubah variabel aslinya, kamu harus mengirim alamatnya lewat",
                    "pointer. Pointer dibahas di materi Pointer Dasar, dan konsep ini",
                    "termasuk yang paling penting dan paling mendasar di C.",
                ]
            },
            {
                "heading": "Konvensi penamaan di kode C nyata",
                "body": [
                    "Begitu kamu mulai membaca kode C orang lain, empat pola nama ini bakal",
                    "terus muncul. Kalau sudah kenal polanya, kode asing jadi lebih gampang",
                    "dibaca:",
                    "",
                    "  snake_case      fungsi & variabel:  hitung_rata_rata, jumlah_data",
                    "  HURUF_BESAR     makro & konstanta enum:  MAX_SIZE, WARNA_MERAH",
                    "  akhiran _t      nama tipe hasil typedef:  size_t, uint32_t, node_t",
                    "  awalan modul    setiap nama publik sebuah pustaka:  str_potong,",
                    "                  sqlite3_open, png_read_image, av_frame_alloc",
                    "",
                    "Awalan modul itu memang diperlukan, karena C nggak punya namespace,",
                    "yaitu ruang nama yang terpisah untuk tiap modul. Semua nama fungsi",
                    "publik dari semua pustaka bertemu di satu ruang yang sama waktu program",
                    "di-link. Jadi dua pustaka yang sama-sama punya fungsi buka() bakal",
                    "bertabrakan. Menempelkan nama modul di depan adalah satu-satunya obat",
                    "yang tersedia.",
                    "",
                    "Catatan soal kurikulum ini: contoh di sini memakai camelCase",
                    "(tampilkanInfo, tambahDiAwal, bebaskanList) supaya seragam dengan",
                    "materi Java yang mungkin kamu baca berdampingan. Kode C di dunia nyata",
                    "hampir selalu memakai snake_case. Jadi jangan mengira gaya di sini",
                    "adalah gaya C yang umum. Kalau kamu menulis kode yang akan dibaca orang",
                    "lain, pakai snake_case. Yang lebih penting lagi, ikuti gaya berkas yang",
                    "sedang kamu sunting.",
                ]
            },
        ],
    },
    {
        "title": "13. Rekursi",
        "sections": [
            {
                "body": [
                    "Rekursi adalah fungsi yang memanggil dirinya sendiri. Kedengarannya",
                    "aneh, tapi cara ini paling wajar untuk soal yang bentuknya \"soal yang",
                    "sama, cuma lebih kecil\".",
                    "",
                    "  5! = 5 * 4!   dan   4! = 4 * 3!   ... begitu terus sampai mentok.",
                    "",
                    "Setiap fungsi rekursif wajib punya dua bagian:",
                    "  1. Base case: kondisi berhenti. Jawabannya langsung diberikan tanpa",
                    "     memanggil diri sendiri lagi. Ini remnya.",
                    "  2. Recursive case: fungsi memanggil dirinya dengan soal yang lebih",
                    "     kecil, dan soalnya harus makin dekat ke base case.",
                    "",
                    "  long faktorial(int n) {",
                    "      if (n <= 1) return 1;            // BASE CASE (rem)",
                    "      return n * faktorial(n - 1);     // RECURSIVE CASE (n mengecil)",
                    "  }",
                    "",
                    "Ada dua cara merusaknya, dan akibatnya sama:",
                    "  - Lupa menulis base case sama sekali.",
                    "  - Menulis recursive case yang nggak mengecil, misalnya faktorial(n)",
                    "    alih-alih faktorial(n - 1), atau faktorial(n + 1) karena salah",
                    "    ketik satu karakter.",
                    "",
                    "Fungsinya lalu memanggil dirinya terus tanpa henti. Bedanya dengan",
                    "while(1): loop tak berujung cuma bikin program menggantung, sedangkan",
                    "rekursi tak berujung bikin program crash. Alasannya dijelaskan di",
                    "bagian call stack di bawah.",
                ],
            },
            {
                "heading": "Faktorial & Fibonacci: rekursif dan iteratif berdampingan",
                "code": """#include <stdio.h>

/* --- Faktorial --- */
long faktorialRekursif(int n) {
    if (n <= 1) {                            // BASE CASE: berhenti di sini
        return 1;
    }
    return n * faktorialRekursif(n - 1);     // RECURSIVE CASE: soalnya mengecil
}

long faktorialIteratif(int n) {
    long hasil = 1;
    for (int i = 2; i <= n; i++) {           // loop biasa, satu variabel 'hasil'
        hasil *= i;
    }
    return hasil;
}

/* --- Fibonacci: 0 1 1 2 3 5 8 13 ... tiap suku = dua suku sebelumnya --- */
long fibRekursif(int n) {
    if (n < 2) {                             // BASE CASE ganda: fib(0)=0, fib(1)=1
        return n;
    }
    return fibRekursif(n - 1) + fibRekursif(n - 2);   // DUA panggilan, bukan satu
}

long fibIteratif(int n) {
    long a = 0, b = 1;
    for (int i = 0; i < n; i++) {
        long berikut = a + b;
        a = b;
        b = berikut;
    }
    return a;
}

int main(void) {
    printf("faktorial(5) rekursif = %ld\\n", faktorialRekursif(5));   // 120
    printf("faktorial(5) iteratif = %ld\\n", faktorialIteratif(5));   // 120
    printf("fib(10) rekursif      = %ld\\n", fibRekursif(10));        // 55
    printf("fib(10) iteratif      = %ld\\n", fibIteratif(10));        // 55

    printf("fib 0..9 : ");
    for (int i = 0; i < 10; i++) {
        printf("%ld ", fibRekursif(i));      // 0 1 1 2 3 5 8 13 21 34
    }
    printf("\\n");
    return 0;
}""",
            },
            {
                "heading": "Call stack: kenapa rekursi bekerja, dan kenapa bisa crash",
                "body": [
                    "Setiap panggilan fungsi menempati satu bingkai (stack frame) di tumpukan",
                    "yang namanya call stack. Isi bingkai itu: parameter, variabel lokal, dan",
                    "alamat baris yang harus dilanjutkan sesudah fungsinya selesai.",
                    "",
                    "Ada dua akibat yang perlu kamu pegang:",
                    "  1. Tiap panggilan punya salinan sendiri dari variabel lokalnya.",
                    "     faktorial(3) dan faktorial(2) sama-sama punya n, tapi itu dua n",
                    "     yang berbeda. Ini lanjutan dari pass by value di materi Function.",
                    "  2. Panggilan terdalam selesai lebih dulu. Yang terakhir masuk,",
                    "     pertama keluar, persis seperti tumpukan piring.",
                    "",
                    "  faktorial(3)  n=3, menunggu faktorial(2)        <- masuk PERTAMA",
                    "    faktorial(2)  n=2, menunggu faktorial(1)",
                    "      faktorial(1)  n=1, BASE CASE, kembalikan 1  <- selesai PERTAMA",
                    "    faktorial(2)  2 * 1 = 2",
                    "  faktorial(3)  3 * 2 = 6                         <- selesai TERAKHIR",
                    "",
                    "Perhatikan: perkaliannya baru terjadi waktu panggilan-panggilan itu",
                    "kembali, dan nggak terjadi waktu mereka turun. Waktu turun, pekerjaannya",
                    "cuma ditumpuk dan ditunda.",
                    "",
                    "Tumpukan itu terbatas. Di Linux jatahnya biasanya 8 MB (cek dengan",
                    "ulimit -s). Rekursi yang nggak pernah sampai ke base case bakal",
                    "menghabiskannya, dan itulah yang disebut stack overflow. Batasnya",
                    "tergantung seberapa besar tiap bingkai:",
                    "  - fungsi sekecil contoh di bawah mentok sekitar 250.000 tingkat",
                    "  - fungsi dengan char buf[4096] mentok sekitar 2.000 tingkat",
                    "",
                    "Jebakan: di Linux, stack overflow juga muncul sebagai 'Segmentation",
                    "fault'. Pesannya sama persis dengan bug pointer NULL di materi",
                    "Debugging. Cara membedakannya: jalankan gdb, lalu ketik backtrace.",
                    "Kalau isinya ribuan baris fungsi yang sama berulang, itu rekursi tak",
                    "berujung, dan pointer-mu nggak salah apa-apa. Jadi jangan buang waktu",
                    "memeriksa pointer yang nggak bersalah.",
                    "",
                    "Program di bawah mencetak sendiri urutan masuk dan keluarnya:",
                ],
                "code": """#include <stdio.h>

void hitungMundur(int n) {
    int lokal = n * 10;          // tiap panggilan punya 'lokal' SENDIRI

    printf("masuk  n=%d, lokal=%d\\n", n, lokal);

    if (n > 0) {                 // BASE CASE: n == 0 -> tidak memanggil lagi
        hitungMundur(n - 1);
    }

    printf("keluar n=%d, lokal=%d\\n", n, lokal);   // 'lokal' utuh, tidak tertimpa
}

int main(void) {
    hitungMundur(3);
    return 0;
}

/* Keluaran - perhatikan 'keluar' berurutan TERBALIK dari 'masuk':
   masuk  n=3, lokal=30
   masuk  n=2, lokal=20
   masuk  n=1, lokal=10
   masuk  n=0, lokal=0
   keluar n=0, lokal=0
   keluar n=1, lokal=10
   keluar n=2, lokal=20
   keluar n=3, lokal=30      */""",
            },
            {
                "heading": "Rekursi pada data: array, string, dan menara Hanoi",
                "code": """#include <stdio.h>
#include <string.h>

// Menjumlah n elemen PERTAMA sebuah array
int jumlah(const int arr[], int n) {
    if (n == 0) {                             // BASE CASE: tidak ada elemen -> 0
        return 0;
    }
    return arr[n - 1] + jumlah(arr, n - 1);   // elemen terakhir + jumlah sisanya
}

// Membalik string DI TEMPAT, dengan menukar ujung ke ujung
void balik(char s[], int kiri, int kanan) {
    if (kiri >= kanan) {                      // BASE CASE: kedua penunjuk bertemu
        return;
    }
    char tmp = s[kiri];
    s[kiri] = s[kanan];
    s[kanan] = tmp;
    balik(s, kiri + 1, kanan - 1);            // sisanya: bagian dalamnya
}

// Menara Hanoi: pindahkan n cakram dari 'asal' ke 'tujuan' lewat 'bantu'
void hanoi(int n, char asal, char tujuan, char bantu) {
    if (n == 0) {                             // BASE CASE: tidak ada yang dipindah
        return;
    }
    hanoi(n - 1, asal, bantu, tujuan);        // sisihkan n-1 cakram ke tiang bantu
    printf("Pindahkan cakram %d: %c -> %c\\n", n, asal, tujuan);
    hanoi(n - 1, bantu, tujuan, asal);        // tumpuk lagi di atas cakram terbesar
}

int main(void) {
    int data[] = {4, 8, 15, 16, 23, 42};
    int n = (int) (sizeof(data) / sizeof(data[0]));
    printf("Jumlah array = %d\\n", jumlah(data, n));      // 108

    char kata[] = "rekursi";
    balik(kata, 0, (int) strlen(kata) - 1);
    printf("Dibalik      = %s\\n", kata);                 // isruker

    printf("Hanoi 3 cakram (butuh 7 langkah):\\n");
    hanoi(3, 'A', 'C', 'B');
    return 0;
}""",
            },
            {
                "body": [
                    "Rekursi lebih jelas daripada loop kalau datanya bercabang:",
                    "  - Pohon: binary tree, folder di dalam folder, elemen HTML di dalam",
                    "    elemen lain.",
                    "  - Parser: di dalam ekspresi '(2 + 3) * 4' ada ekspresi lagi.",
                    "  - Algoritma bagi dua: binary search, merge sort, quicksort.",
                    "",
                    "Semua itu bisa ditulis pakai loop, tapi kamu harus mengurus tumpukanmu",
                    "sendiri pakai array. Kodenya jadi lebih panjang dan lebih gampang",
                    "salah.",
                    "",
                    "Rekursi jauh lebih mahal kalau soal yang sama dihitung berulang-ulang.",
                    "fibRekursif di atas melakukannya: fib(5) menghitung fib(3) dua kali,",
                    "fib(2) tiga kali, dan seterusnya makin membengkak:",
                    "",
                    "  n     panggilan fibRekursif     langkah fibIteratif",
                    "  20              21.891                    20",
                    "  30           2.692.537                    30",
                    "  40         331.160.281                    40",
                    "",
                    "Jumlah panggilannya naik sekitar 1,6 kali setiap n bertambah 1.",
                    "Pertumbuhan yang berlipat seperti ini biasa ditulis O(2^n). fib(40)",
                    "versi rekursif naif butuh waktu yang terasa (di mesin modern hampir",
                    "satu detik), sedangkan versi iteratifnya selesai seketika. Obatnya",
                    "nggak harus membuang rekursinya. Simpan hasil yang sudah pernah",
                    "dihitung di sebuah array (memoization), dan fib(40) turun dari 331 juta",
                    "panggilan jadi 79.",
                    "",
                    "Rekursi ekor (tail recursion) terjadi kalau panggilan rekursif adalah",
                    "hal terakhir yang dikerjakan fungsi, dan nggak ada n * yang masih",
                    "menunggu hasilnya. Dalam kasus ini, compiler boleh memakai ulang",
                    "bingkai yang sama, jadi tumpukannya nggak tumbuh:",
                    "",
                    "  long ekor(int n, long akum) {",
                    "      if (n <= 1) return akum;",
                    "      return ekor(n - 1, akum * n);   // hasilnya LANGSUNG dikembalikan",
                    "  }",
                    "",
                    "gcc -O2 memang mengubahnya jadi loop, sedangkan gcc tanpa -O nggak.",
                    "Tanpa -O, program yang sama tetap crash di kedalaman jutaan. Standar C",
                    "nggak menjanjikan apa pun soal ini, jadi jangan bergantung padanya.",
                    "",
                    "Nanti kamu bakal ketemu rekursi lagi tanpa disebut namanya.",
                    "Menelusuri linked list (materi Linked List) dan binary tree hampir",
                    "selalu ditulis dengan pola \"kerjakan node ini, lalu kerjakan sisanya",
                    "dengan cara yang sama persis\".",
                ],
            },
        ],
    },
    {
        "title": "14. Lingkup, Masa Hidup & Kelas Penyimpanan Variabel",
        "sections": [
            {
                "body": [
                    "Sampai sini, setiap variabel kita lahir dan mati di dalam satu fungsi.",
                    "Begitu program makin besar, muncul dua pertanyaan berbeda yang sering",
                    "dikira satu:",
                    "",
                    "  lingkup (scope)         dari baris mana saja nama ini boleh disebut?",
                    "  masa hidup (lifetime)   sejak kapan sampai kapan nilainya ada di memori?",
                    "",
                    "Bedanya nyata, dan nanti kita lihat sendiri. Ada variabel yang nggak",
                    "bisa disebut dari luar fungsinya, tapi nilainya tetap hidup sesudah",
                    "fungsi itu selesai.",
                    "",
                    "Aturan lingkup di C cukup satu kalimat: sebuah nama berlaku sejak baris",
                    "deklarasinya sampai kurawal penutup } dari blok tempat dia",
                    "dideklarasikan.",
                    "  - Blok nggak cuma badan fungsi. Kurawal milik if, else, for, while,",
                    "    bahkan kurawal { } yang kamu tulis sendiri tanpa apa-apa di",
                    "    depannya, semuanya blok.",
                    "  - for (int i = 0; ...) membuat i cuma ada di dalam loop-nya. Menyebut",
                    "    i sesudah loop menghasilkan error \"'i' undeclared\". Deklarasi di",
                    "    dalam for baru sah sejak C99, makanya kode lama sering menaruh",
                    "    int i; jauh di atas.",
                    "  - Parameter fungsi juga variabel lokal. Lingkupnya seluruh badan",
                    "    fungsi, dan isinya salinan (pass by value, lihat materi Function).",
                    "",
                    "Shadowing terjadi kalau blok di dalam memakai nama yang sama dengan",
                    "variabel di luar. Variabel di dalam menutupi variabel di luar selama",
                    "blok itu berjalan, dan variabel di luar nggak ikut berubah. Compiler",
                    "nggak protes karena ini memang sah, dan di situ jebakannya. Kamu merasa",
                    "sudah mengubah sesuatu, padahal yang berubah cuma kembarannya yang",
                    "sebentar lagi hilang. Minta compiler melaporkannya:",
                    "",
                    "  gcc -Wall -Wextra -Wshadow lingkup.c -o lingkup",
                    "  (-Wshadow TIDAK ikut di dalam -Wall maupun -Wextra, harus diminta sendiri)",
                ],
            },
            {
                "heading": "Lingkup blok, shadowing, dan satu variabel global",
                "code": """#include <stdio.h>

int nomor_baris = 0;        // GLOBAL: di luar semua fungsi, otomatis berisi 0

void catat(char pesan[]) {
    nomor_baris++;          // fungsi mana pun di berkas ini melihat nama yang sama
    printf("%d. %s\\n", nomor_baris, pesan);
}

int main(void) {
    int nilai = 10;

    {                            // blok telanjang, sah ditulis di C
        int nilai = 99;          // SHADOWING: menutupi 'nilai' milik main
        catat("masuk blok dalam");
        printf("   nilai di dalam blok = %d\\n", nilai);
    }                            // 'nilai' yang 99 mati persis di sini

    printf("   nilai di luar blok  = %d\\n", nilai);   // tetap 10, tidak tersentuh

    for (int i = 0; i < 3; i++) {
        catat("satu putaran loop");
    }
    // printf("%d", i);   <- kalau dibuka: error, 'i' sudah tidak ada di sini

    catat("selesai");
    printf("total baris tercatat = %d\\n", nomor_baris);
    return 0;
}""",
            },
            {
                "body": [
                    "Kelas penyimpanan (storage class) menentukan di mana sebuah nilai",
                    "tinggal. Tempat itulah yang menentukan berapa lama nilainya hidup:",
                    "",
                    "  Tempat  Kelas       Lahir                    Mati",
                    "  ------  ----------  -----------------------  --------------------------",
                    "  stack   automatic   saat fungsi dipanggil    saat fungsi itu selesai",
                    "  data    static      sebelum main() jalan     saat program berhenti",
                    "  heap    dynamic     saat malloc() dipanggil  saat kamu memanggil free()",
                    "",
                    "Variabel lokal biasa termasuk automatic. Itu kelas bawaan, jadi nggak",
                    "perlu ditulis. Variabel global dan apa pun yang diberi kata static",
                    "termasuk static. Yang di heap dibahas tersendiri di materi Dynamic",
                    "Memory Allocation.",
                    "",
                    "Variabel global adalah variabel yang dideklarasikan di luar semua",
                    "fungsi, termasuk di luar main().",
                    "  - Variabel ini terlihat oleh semua fungsi di berkas itu, mulai dari",
                    "    baris deklarasinya ke bawah. Kalau fungsi di atasnya juga butuh,",
                    "    taruh deklarasinya paling atas di berkas.",
                    "  - Isinya otomatis 0 kalau nggak diberi nilai awal. Ini beda jauh",
                    "    dengan variabel lokal, yang isinya sampah kalau lupa diberi nilai",
                    "    awal.",
                    "  - Nilai awalnya harus konstanta yang sudah diketahui waktu",
                    "    kompilasi. int x = hitung(); di luar fungsi ditolak compiler.",
                    "  - Pakai seperlunya aja. Fungsi yang menerima parameter dan",
                    "    mengembalikan nilai menunjukkan dengan jelas apa yang dia butuhkan.",
                    "    Variabel global menyembunyikan hal itu. Kalau isinya salah, kamu",
                    "    harus mencurigai seluruh berkas, karena semua fungsi boleh menulis",
                    "    ke sana.",
                    "  - Yang pantas jadi global biasanya cuma satu-dua hal: pencacah, tabel",
                    "    tetap, atau keadaan tunggal milik program. Sisanya lebih baik",
                    "    dikirim sebagai parameter.",
                    "",
                    "Ada dua kata kunci peninggalan lama. Keduanya disebut di sini supaya",
                    "kamu nggak bingung kalau ketemu:",
                    "  auto     -> menegaskan 'ini automatic', padahal itu memang bawaannya.",
                    "              Praktis tidak pernah ditulis lagi. (Di C++ modern kata yang",
                    "              sama dipakai untuk hal yang BERBEDA TOTAL: menebak tipe.)",
                    "  register -> dulu usul supaya variabel ditaruh di register CPU. Compiler",
                    "              sekarang memutuskan sendiri dan mengabaikan usul itu. Satu",
                    "              akibatnya masih terasa: &x pada variabel register ditolak,",
                    "              \"address of register variable requested\".",
                ],
            },
            {
                "heading": "static di dalam fungsi: variabel yang punya ingatan",
                "body": [
                    "Peringatan buat yang pernah pakai Java atau C++: static di C nggak",
                    "berarti \"milik kelas, bukan milik objek\". C nggak punya kelas sama",
                    "sekali. Di C, satu kata ini mengerjakan dua tugas yang nggak saling",
                    "berhubungan, dan tugasnya ditentukan oleh posisi penulisannya:",
                    "  - Di dalam fungsi, static mengatur masa hidup. Variabelnya nggak",
                    "    lahir ulang setiap fungsi dipanggil.",
                    "  - Di luar fungsi, static mengatur jangkauan nama. Namanya cuma milik",
                    "    berkas itu (bagian terakhir materi ini).",
                    "",
                    "Satu-satunya cara mengingatnya adalah memperhatikan di mana kata static",
                    "ditulis.",
                    "",
                    "static di dalam fungsi: variabelnya tetap lokal, jadi nggak ada yang",
                    "bisa menyebut namanya dari luar. Tapi memorinya disiapkan sekali",
                    "sebelum main() jalan, dan bertahan sampai program berhenti. Baris",
                    "pemberian nilai awalnya juga dijalankan sekali aja, nggak setiap kali",
                    "fungsinya dipanggil. Ini dipakai untuk pencacah, cache kecil, atau",
                    "penanda \"fungsi ini sudah pernah dipanggil\".",
                    "",
                    "Masa hidup ini juga menjelaskan satu bug klasik. Sintaksnya benar, dan",
                    "masalahnya ada di masa hidup variabel:",
                    "",
                    "  char *salam(void) {",
                    "      char teks[] = \"Halo\";   // automatic: tinggal di stack fungsi ini",
                    "      return teks;             // alamatnya dikembalikan...",
                    "  }                            // ...tapi memorinya mati persis di sini",
                    "",
                    "Pemanggilnya memegang alamat yang sudah nggak dimiliki siapa pun.",
                    "Pointer seperti ini disebut dangling pointer (pointer menggantung).",
                    "Kadang isinya masih terbaca 'Halo', dan justru itu jebakannya.",
                    "Programnya kelihatan benar hari ini lalu rusak besok, begitu ada",
                    "pemanggilan fungsi lain yang memakai ulang bagian stack tersebut. gcc",
                    "-Wall sudah memperingatkan lebih dulu: \"function returns address of",
                    "local variable\".",
                    "",
                    "Menambahkan static pada teks[] membuatnya \"berhasil\", karena memorinya",
                    "hidup selamanya (lihat nama_hari() di bawah). Tapi buffernya cuma satu",
                    "untuk seluruh program, jadi panggilan kedua menimpa hasil panggilan",
                    "pertama. Cara ini aman untuk teks tetap, dan berbahaya untuk nilai yang",
                    "berubah. Cara yang benar untuk mengembalikan data baru adalah malloc",
                    "(materi Dynamic Memory Allocation), atau buffer yang disiapkan",
                    "pemanggil lalu dikirim lewat pointer.",
                ],
                "code": """#include <stdio.h>

int nomor_tiket(void) {
    static int terakhir = 0;   // diberi nilai SEKALI, sebelum main() jalan
    terakhir++;                // nilainya diingat sampai program berhenti
    return terakhir;
}

int nomor_lupa(void) {
    int terakhir = 0;          // automatic: lahir ulang jadi 0 tiap dipanggil
    terakhir++;
    return terakhir;
}

// Aman dikembalikan: 'nama' static, memorinya tidak ikut mati saat fungsi usai.
char *nama_hari(void) {
    static char nama[] = "Senin";
    return nama;
}

int main(void) {
    for (int putaran = 1; putaran <= 3; putaran++) {
        int pakai_static = nomor_tiket();
        int pakai_lokal = nomor_lupa();
        printf("panggilan %d -> static: %d   lokal biasa: %d\\n",
               putaran, pakai_static, pakai_lokal);
    }

    printf("hari sibuk: %s\\n", nama_hari());
    // printf("%d", terakhir);  <- error: 'terakhir' tetap tidak terlihat dari sini
    return 0;
}""",
            },
            {
                "heading": "static di luar fungsi & extern: siapa boleh melihat nama ini",
                "body": [
                    "Di luar fungsi, static nggak ada hubungannya dengan masa hidup, karena",
                    "variabel global memang sudah hidup selamanya. Artinya berganti jadi",
                    "jangkauan nama: \"nama ini milik berkas .c ini saja\". Istilahnya",
                    "internal linkage.",
                    "",
                    "Makanya di berkas .c sungguhan, hampir semua fungsi pembantu diawali",
                    "kata static, dan cuma sedikit yang sengaja dibiarkan tanpa static:",
                    "  - Nama pembantumu nggak bertabrakan dengan nama yang sama di berkas",
                    "    lain. Dua berkas yang sama-sama punya fungsi bantu() tanpa static",
                    "    lolos tahap compile, lalu gagal di tahap link: \"multiple definition",
                    "    of bantu\".",
                    "  - static menunjukkan niat: \"jangan panggil ini dari luar, aku boleh",
                    "    mengubahnya kapan aja\". Perannya sama dengan private di Java.",
                    "",
                    "Lawannya adalah extern. Untuk memakainya, kamu perlu membedakan dua hal",
                    "yang selama ini kelihatan mirip:",
                    "  int saldo = 1000;   DEFINISI  -> menyediakan memorinya. Boleh ada SATU",
                    "                                   saja di seluruh program.",
                    "  extern int saldo;   DEKLARASI -> 'percaya saja, ini ada di berkas lain'.",
                    "                                   Tidak memakan memori, boleh diulang.",
                    "",
                    "Prototype fungsi yang kamu pakai sejak materi Function juga termasuk",
                    "deklarasi extern, cuma kata extern-nya boleh nggak ditulis. Tempat yang",
                    "tepat untuk deklarasi extern adalah berkas .h, supaya semua berkas yang",
                    "meng-include-nya sepakat pada bentuk yang sama (materi Kompilasi",
                    "Multi-File & Header).",
                ],
                "code": """/* ===== File: kas.c ===== */
#include <stdio.h>

int saldo = 1000;              // global tanpa static: berkas lain boleh memakainya

static int biaya_admin = 5;    // static di LUAR fungsi: hanya kas.c yang melihatnya

static void catat(char aksi[], int jumlah) {   // pembantu, privat berkas ini
    printf("  %-6s %4d (admin %d)\\n", aksi, jumlah, biaya_admin);
}

void tarik(int jumlah) {       // tanpa static -> boleh dipanggil dari berkas lain
    saldo -= jumlah + biaya_admin;
    catat("tarik", jumlah);
}

/* ===== File: main.c ===== */
#include <stdio.h>

extern int saldo;              // DEKLARASI: saldo ada, definisinya di berkas lain
void tarik(int jumlah);        // prototype: sudah berarti extern tanpa ditulis

// extern int biaya_admin;     <- lolos compile, GAGAL saat link:
//                                undefined reference to biaya_admin

int main(void) {
    printf("saldo awal  : %d\\n", saldo);
    tarik(100);
    tarik(200);
    printf("saldo akhir : %d\\n", saldo);
    return 0;
}

/* Kompilasi keduanya sekaligus:  gcc -Wall -Wextra main.c kas.c -o kas
   Jalankan hasilnya:             ./kas                                   */""",
            },
        ],
    },
    {
        "title": "15. Pointer Dasar",
        "sections": [
            {
                "body": [
                    "Pointer adalah variabel yang isinya alamat memori dari variabel lain.",
                    "Yang disimpan pointer adalah alamatnya, dan nilai variabel itu sendiri",
                    "nggak ikut disimpan. Konsep ini yang paling penting dan paling khas",
                    "dari C.",
                    "",
                    "Gampangnya begini. Bayangkan memori komputer sebagai deretan loker",
                    "bernomor. Variabel biasa adalah isi sebuah loker. Pointer adalah",
                    "secarik kertas yang berisi nomor loker.",
                    "",
                    "Ada dua operator kunci:",
                    "  &  (address-of)   -> mendapatkan ALAMAT sebuah variabel.",
                    "  *  (dereference)  -> mengakses NILAI yang ditunjuk pointer.",
                    "",
                    "  int angka = 10;",
                    "  int *ptr = &angka;   // ptr menyimpan ALAMAT dari 'angka'",
                    "",
                    "  *ptr sekarang berarti 'nilai yang ditunjuk ptr' -> 10",
                    "",
                    "Dereference artinya \"buka alamatnya, lalu ambil isinya\".",
                ]
            },
            {
                "heading": "Contoh dasar pointer",
                "code": """#include <stdio.h>

int main(void) {
    int angka = 10;
    int *ptr = &angka;    // ptr menunjuk ke alamat 'angka'

    printf("Nilai angka       : %d\\n", angka);
    printf("Alamat angka (&)  : %p\\n", (void*)&angka);
    printf("Nilai ptr (alamat): %p\\n", (void*)ptr);
    printf("Nilai *ptr (deref): %d\\n", *ptr);   // 10, mengakses lewat pointer

    *ptr = 99;    // mengubah NILAI lewat pointer
    printf("angka setelah *ptr = 99: %d\\n", angka);   // 99! (angka ikut berubah)

    return 0;
}"""
            },
            {
                "heading": "Pass by Reference dengan pointer (SOLUSI masalah materi 9)",
                "code": """#include <stdio.h>

// Menerima ALAMAT (pointer), bukan salinan nilai
void tambahSatu(int *x) {
    *x = *x + 1;    // mengubah NILAI ASLI lewat alamatnya
}

void tukar(int *a, int *b) {   // swap dua variabel - HANYA mungkin dengan pointer!
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main(void) {
    int angka = 5;
    tambahSatu(&angka);       // kirim ALAMAT angka, bukan nilainya
    printf("%d\\n", angka);    // 6! sekarang BERHASIL berubah

    int x = 1, y = 2;
    tukar(&x, &y);
    printf("x=%d, y=%d\\n", x, y);   // x=2, y=1 (berhasil ditukar)

    return 0;
}"""
            },
            {
                "body": [
                    "NULL pointer adalah pointer yang nggak menunjuk ke mana pun.",
                    "  int *ptr = NULL;   // praktik AMAN, bukan alamat acak",
                    "  if (ptr != NULL) { ... }   // SELALU cek sebelum dereference!",
                    "  *ptr;   // JIKA ptr NULL, ini CRASH (segmentation fault)!",
                    "",
                    "Mengisi pointer dengan NULL sejak awal adalah kebiasaan yang aman,",
                    "karena pointer yang belum diisi berisi alamat acak. Selalu cek NULL",
                    "sebelum dereference. Kalau ptr bernilai NULL lalu kamu membaca *ptr,",
                    "program crash dengan pesan segmentation fault.",
                    "",
                    "Di sistem yang sama, ukuran pointer selalu sama, apa pun tipe data yang",
                    "ditunjuknya (biasanya 8 byte di sistem 64-bit). Tipe pointer cuma",
                    "memberi tahu compiler cara menafsirkan data di alamat itu.",
                ]
            },
        ],
    },
    {
        "title": "16. Pointer & Array: Hubungan Erat Keduanya",
        "sections": [
            {
                "body": [
                    "Kalau nama array dipakai di dalam ekspresi, nama itu otomatis berubah",
                    "jadi alamat elemen pertamanya. Perubahan otomatis ini biasa disebut",
                    "\"meluruh\" (decay). Karena itu, pointer dan array di C erat sekali",
                    "hubungannya.",
                    "",
                    "  int angka[] = {10, 20, 30};",
                    "  int *ptr = angka;      // SAMA dengan: int *ptr = &angka[0];",
                    "",
                    "  angka[0]   SAMA DENGAN   *(angka + 0)   SAMA DENGAN   *angka",
                    "  angka[1]   SAMA DENGAN   *(angka + 1)",
                    "  angka[i]   SAMA DENGAN   *(angka + i)",
                    "",
                    "Walaupun begitu, nama array tetap nggak sama dengan variabel pointer.",
                    "Kamu nggak bisa mengisinya dengan alamat lain. Materi String Lanjutan",
                    "membahas bedanya.",
                ]
            },
            {
                "heading": "Pointer arithmetic (aritmatika pointer)",
                "code": """#include <stdio.h>

int main(void) {
    int angka[] = {10, 20, 30, 40, 50};
    int *ptr = angka;   // ptr menunjuk ke angka[0]

    printf("%d\\n", *ptr);        // 10
    printf("%d\\n", *(ptr + 1));  // 20 (ptr+1 = alamat elemen BERIKUTNYA)
    printf("%d\\n", *(ptr + 2));  // 30

    ptr++;                        // pindah ke elemen berikutnya
    printf("Setelah ptr++: %d\\n", *ptr);   // 20

    // Melintasi array dengan pointer (alternatif dari indexing biasa)
    ptr = angka;   // reset ke awal
    for (int i = 0; i < 5; i++) {
        printf("%d ", *(ptr + i));
    }
    printf("\\n");   // 10 20 30 40 50

    return 0;
}"""
            },
            {
                "heading": "Array sebagai parameter fungsi (SELALU 'meluruh' jadi pointer!)",
                "code": """#include <stdio.h>

// Ketiga cara ini SAMA PERSIS bagi compiler (array parameter = pointer):
void cetak1(int arr[], int n) { for (int i=0;i<n;i++) printf("%d ", arr[i]); }
void cetak2(int arr[5], int n) { for (int i=0;i<n;i++) printf("%d ", arr[i]); }
void cetak3(int *arr, int n)   { for (int i=0;i<n;i++) printf("%d ", arr[i]); }

int main(void) {
    int data[] = {1, 2, 3, 4, 5};
    cetak3(data, 5);
    printf("\\n");

    // AKIBATNYA: sizeof() di DALAM fungsi TIDAK bekerja seperti di luar!
    // sizeof(arr) di dalam cetak1/2/3 akan mengembalikan ukuran POINTER
    // (misal 8 byte), BUKAN ukuran seluruh array (20 byte untuk 5 int).
    // INILAH KENAPA parameter 'n' (jumlah elemen) HARUS dikirim terpisah!
    return 0;
}"""
            },
            {
                "heading": "Array 2 dimensi sebagai parameter (dimensi KEDUA wajib!)",
                "body": [
                    "Peluruhan tadi punya akibat yang mengejutkan pada matriks. Yang meluruh",
                    "jadi pointer cuma dimensi pertama. Dimensi kedua wajib tetap ditulis.",
                    "",
                    "  void cetakMatriks(int m[][3], int baris);   // BENAR",
                    "  void cetakMatriks(int m[][], int baris);    // GALAT kompilasi",
                    "",
                    "Alasannya hitungan, jadi kamu nggak perlu menghafalnya. Isi int",
                    "nilai[2][3] tersusun rapat di memori sebagai enam int berurutan: baris",
                    "0 dulu, baru baris 1. Untuk menemukan m[i][j], compiler menghitung",
                    "alamatnya sebagai m + i*3 + j. Angka 3 itu adalah panjang satu baris.",
                    "Tanpa dimensi kedua, hitungan itu mustahil dilakukan.",
                    "",
                    "Akibatnya, fungsi di atas cuma bisa melayani matriks yang lebar",
                    "barisnya persis 3. Kalau lebarnya harus bisa berubah-ubah, kode nyata",
                    "biasanya memakai satu array datar berisi baris*kolom elemen, lalu",
                    "menghitung indeksnya sendiri: arr[i * kolom + j].",
                ],
                "code": """#include <stdio.h>

// Dimensi KEDUA wajib ditulis; yang PERTAMA boleh dikosongkan.
void cetakMatriks(int m[][3], int baris) {
    for (int i = 0; i < baris; i++) {
        for (int j = 0; j < 3; j++) {
            printf("%d ", m[i][j]);
        }
        printf("\\n");
    }
}

int main(void) {
    int nilai[2][3] = {{1, 2, 3}, {4, 5, 6}};
    cetakMatriks(nilai, 2);      // baris 1: 1 2 3   baris 2: 4 5 6
    return 0;
}"""
            },
            {
                "heading": "Idiom pointer padat: *p++, while (*s), *dst++ = *src++",
                "body": [
                    "Tiga bentuk pendek ini terus muncul begitu kamu membuka kode C",
                    "sungguhan. Bahannya sudah kamu punya semua. Yang baru cuma bentuknya",
                    "yang padat.",
                    "",
                    "  *p++             pakai nilai yang ditunjuk, LALU majukan pointer",
                    "  while (*s)       jalan selama karakter yang ditunjuk bukan '\\0'",
                    "  *dst++ = *src++  salin satu karakter, lalu majukan KEDUANYA",
                    "",
                    "Kuncinya prioritas operator (materi Ekspresi, Prioritas Operator &",
                    "Prefix/Postfix): ++ mengikat lebih kuat daripada *. Jadi *p++ dibaca",
                    "*(p++). Yang naik adalah pointer-nya, dan nilai yang ditunjuk nggak",
                    "berubah. Untuk menaikkan nilainya, kurungnya wajib: (*p)++",
                    "",
                    "while (*s) adalah singkatan dari while (*s != '\\0'). Karakter '\\0'",
                    "bernilai nol, dan nol berarti \"salah\". Jadi penutup string itu sendiri",
                    "yang menghentikan loop. Makanya string C nggak perlu membawa panjangnya",
                    "ke mana-mana.",
                ],
                "code": """#include <stdio.h>

// Inilah isi strcpy yang sesungguhnya - sependek ini.
void salin(char *dst, const char *src) {
    while (*src) {           // selama karakter yang ditunjuk bukan '\\0'
        *dst++ = *src++;     // salin, lalu majukan KEDUA pointer
    }
    *dst = '\\0';             // penutupnya harus ditulis sendiri
}

int main(void) {
    char tujuan[20];
    salin(tujuan, "pointer");
    printf("%s\\n", tujuan);          // pointer

    const char *s = "abc";
    while (*s) {
        printf("[%c]", *s++);        // *s dipakai dulu, s baru maju
    }
    printf("\\n");                    // [a][b][c]
    return 0;
}"""
            },
        ],
    },
    {
        "title": "17. String Lanjutan: char *, const & Keluarga mem*",
        "sections": [
            {
                "body": [
                    "Materi String mengajarkan string dalam satu bentuk aja: char nama[] =",
                    "\"Andi\". Kode C sungguhan juga penuh bentuk kedua: char *s = \"Andi\". Dua",
                    "baris itu kelihatan hampir sama, padahal cara kerjanya beda total.",
                    "Salah membedakannya adalah penyebab segfault yang paling sering menimpa",
                    "pemula C. Segfault itu crash karena program menyentuh memori yang",
                    "nggak boleh dia sentuh.",
                    "",
                    "  char kotak[] = \"halo\";  // compiler menyiapkan 5 byte MILIKMU, lalu MENYALIN",
                    "  char *tunjuk = \"halo\";  // tidak ada salinan; tunjuk cuma menyimpan ALAMAT",
                    "",
                    "Bentuk pertama: \"halo\" dipakai sebagai nilai awal. Byte-nya disalin ke",
                    "array yang jadi milik fungsimu (di stack, kalau dideklarasikan di",
                    "dalam fungsi). Isinya bebas kamu ubah, karena memang punyamu sendiri.",
                    "",
                    "Bentuk kedua: literal \"halo\" disimpan sekali aja, di bagian program",
                    "yang ditandai \"cuma boleh dibaca\" waktu program dimuat ke memori. Yang",
                    "kamu pegang cuma alamatnya. Hurufnya bukan milikmu.",
                    "",
                    "  tunjuk[0] = 'H';",
                    "  // gcc TIDAK protes sedikit pun. Kompilasi mulus, 0 warning.",
                    "  // Lalu dijalankan: Segmentation fault (core dumped).",
                    "",
                    "Ini jenis bug yang paling menyebalkan. Compiler nggak bisa menolongmu,",
                    "dan crash-nya baru muncul waktu program dijalankan, bisa jadi di",
                    "komputer orang lain. Jalan keluarnya: tulis tipenya dengan jujur.",
                    "",
                    "  const char *tunjuk = \"halo\";",
                    "  tunjuk[0] = 'H';   // error: assignment of read-only location '*tunjuk'",
                    "",
                    "Makanya di kode yang rapi, literal string selalu ditulis dengan const",
                    "char *. Tujuannya praktis: const memindahkan kegagalan dari \"crash di",
                    "tangan pemakai\" ke \"ditolak sebelum programnya jadi\".",
                    "",
                    "Ada beda lain yang juga sering bikin bingung:",
                    "  - sizeof kotak hasilnya 5, yaitu ukuran array-nya (4 huruf + '\\0').",
                    "  - sizeof tunjuk hasilnya 8, yaitu ukuran pointer. Panjang teksnya",
                    "    nggak dihitung.",
                    "  - tunjuk = \"dunia\"; boleh. Pointer memang variabel yang isinya",
                    "    alamat, jadi isinya boleh diganti.",
                    "  - kotak = \"dunia\"; nggak bisa dikompilasi. Nama array nggak sama",
                    "    dengan variabel pointer. Nama array cuma \"meluruh\" jadi alamat",
                    "    waktu dipakai (materi Pointer & Array), dan alamat itu tetap.",
                ],
            },
            {
                "heading": "Bukti nyata: char[] bisa diubah, char * tidak",
                "code": """#include <stdio.h>

int main(void) {
    char kotak[] = "halo";          // 5 byte MILIK KITA, isinya disalin dari literal
    const char *tunjuk = "halo";    // cuma alamat; literalnya read-only

    kotak[0] = 'H';                 // BOLEH: yang diubah salinan sendiri
    printf("kotak      : %s\\n", kotak);
    printf("tunjuk     : %s\\n", tunjuk);
    // tunjuk[0] = 'H';             // ditolak compiler. Tanpa const: lolos lalu CRASH.

    printf("sizeof kotak  : %zu\\n", sizeof kotak);    // 5 = 4 huruf + '\\0'
    printf("sizeof tunjuk : %zu\\n", sizeof tunjuk);   // 8 = ukuran sebuah POINTER

    tunjuk = "dunia";               // pointer boleh dipindah ke literal lain
    printf("tunjuk baru   : %s\\n", tunjuk);
    // kotak = "dunia";             // TIDAK BISA: nama array bukan variabel pointer

    const char *hari[3] = {"Senin", "Selasa", "Rabu"};   // 3 POINTER ke 3 literal
    char bulan[3][8]    = {"Januari", "Mei", "Juli"};    // 3 x 8 byte MENYATU

    bulan[1][0] = 'm';              // boleh: bulan benar-benar menyimpan hurufnya
    // hari[1][0] = 's';            // tidak boleh: yang ditunjuk itu literal read-only
    printf("%s / %s\\n", hari[1], bulan[1]);
    printf("sizeof hari  : %zu\\n", sizeof hari);    // 3 pointer  = 24 byte
    printf("sizeof bulan : %zu\\n", sizeof bulan);   // 3 x 8 byte = 24 byte
    return 0;
}""",
            },
            {
                "body": [
                    "const pada sebuah parameter adalah janji yang ikut diperiksa compiler:",
                    "\"fungsi ini nggak akan mengubah data yang kamu kirim\". Makanya",
                    "deklarasi fungsi di pustaka standar bisa dibaca seperti kontrak,",
                    "bahkan sebelum kamu membuka dokumentasinya:",
                    "",
                    "  size_t strlen(const char *s);                 -> s cuma DIBACA",
                    "  int    strcmp(const char *a, const char *b);  -> dua-duanya cuma DIBACA",
                    "  char  *strcpy(char *dst, const char *src);    -> dst DITULISI, src DIBACA",
                    "",
                    "Cara memakainya waktu membaca kode: parameter yang ber-const aman diisi",
                    "apa aja, termasuk literal. Parameter tanpa const berniat menulis ke",
                    "sana, jadi jangan pernah mengirim literal ke situ.",
                    "",
                    "  strcpy(\"halo\", nama);   // dst-nya literal. Nol warning, lalu segfault.",
                    "",
                    "Kenapa nggak ada warning sama sekali? Di C, literal string bertipe",
                    "char[], dan nggak bertipe const char[]. Ini peninggalan sejarah, supaya",
                    "kode kuno tetap bisa dikompilasi. Jadi compiler nggak melihat",
                    "pelanggaran apa pun. Yang menolak adalah sistem operasi, waktu program",
                    "dijalankan.",
                    "",
                    "Ada tiga bentuk const pada pointer. Cara membacanya: mulai dari nama",
                    "variabel, lalu mundur ke kiri.",
                    "",
                    "  const char *p;",
                    "      p -> pointer -> ke char yang const",
                    "      ISI-nya terkunci; p sendiri bebas dipindah menunjuk lain.",
                    "  char * const p;",
                    "      p -> pointer yang const -> ke char",
                    "      POINTER-nya terkunci; isinya masih boleh diubah lewat p.",
                    "  const char * const p;",
                    "      dua-duanya terkunci: tak bisa dipindah, tak bisa ditulisi.",
                    "",
                    "Pintasan yang jarang meleset: const di kiri tanda * mengunci isi yang",
                    "ditunjuk, sedangkan const di kanan tanda * mengunci pointer-nya",
                    "sendiri.",
                    "",
                    "Ada dua pesan khas kalau janji const dilanggar. Keduanya sering muncul,",
                    "jadi kenali bunyinya:",
                    "",
                    "  error: assignment of read-only location '*s'",
                    "    -> menulis ke data yang dijanjikan const. Ini ERROR, kompilasi berhenti.",
                    "  warning: assignment discards 'const' qualifier from pointer target type",
                    "    -> memasukkan const char * ke dalam char *, alias membuang",
                    "       janjinya diam-diam. Ini cuma WARNING; program TETAP jadi.",
                    "       Satu lagi alasan kenapa -Wall -Wextra (materi Debugging)",
                    "       bukan soal selera.",
                    "",
                    "Baris seperti const char *nama[3] = {\"tambah\", \"kurang\", \"kali\"}, yang",
                    "nanti muncul di materi Function Pointer, sekarang bisa kamu baca utuh.",
                    "Itu array berisi 3 pointer ke literal yang tersebar entah di mana.",
                    "Bandingkan dengan char nama[3][10], yaitu satu blok 30 byte yang",
                    "menyatu:",
                    "",
                    "  const char *nama[3]   panjang tiap kata BEBAS, isi read-only,",
                    "                        tiap elemen 8 byte (alamat). Menukar urutan",
                    "                        = menukar dua alamat saja.",
                    "  char nama[3][10]      semua baris DIPATOK 10 byte, isi boleh diubah,",
                    "                        tidak ada alamat terpisah. Menukar urutan",
                    "                        = menyalin byte sungguhan.",
                ],
            },
            {
                "heading": "Keluarga mem*, merakit dengan snprintf, mengurai dengan sscanf",
                "body": [
                    "Daftar <string.h> di materi String berhenti di keluarga str*. Yang sama",
                    "seringnya muncul di kode nyata adalah keluarga mem*. Bedanya mendasar:",
                    "mem* bekerja pada byte mentah sebanyak yang kamu sebutkan, dan nggak",
                    "peduli sama sekali pada '\\0'.",
                    "",
                    "  memset(buf, 0, sizeof buf)  isi n byte dengan satu nilai yang sama",
                    "  memcpy(tujuan, asal, n)     salin n byte; daerahnya TIDAK BOLEH",
                    "                              bertumpang tindih",
                    "  memmove(tujuan, asal, n)    sama, tapi AMAN walau daerahnya",
                    "                              bertumpang tindih",
                    "  memcmp(a, b, n)             bandingkan n byte apa adanya; '\\0' ikut",
                    "                              dibandingkan",
                    "",
                    "Karena nggak peduli '\\0', mem* juga bisa dipakai untuk data yang sama",
                    "sekali bukan teks: array int, struct, dan buffer berkas biner.",
                    "",
                    "Ini juga jalan keluar dari larangan di materi String (\"strcat dan",
                    "strcpy nggak mengecek ukuran\"). Cara yang lazim untuk merakit teks di C",
                    "adalah snprintf. Fungsi ini menulis paling banyak sizeof buf byte,",
                    "selalu menutup teksnya dengan '\\0', dan mengembalikan jumlah karakter",
                    "yang dibutuhkan seandainya tempatnya cukup. Jadi memeriksa hasil >=",
                    "sizeof buf adalah satu-satunya cara tahu teksmu terpotong tanpa",
                    "menebak. Kembarannya, sprintf, nggak punya batas sama sekali.",
                    "Perlakukan sprintf seperti strcpy: jangan dipakai.",
                    "",
                    "Arah sebaliknya adalah sscanf. Fungsi ini memecah satu baris yang sudah",
                    "ada di memori (misalnya hasil fgets di materi Input & Output), lalu",
                    "mengembalikan jumlah bagian yang berhasil terisi.",
                ],
                "code": """#include <stdio.h>
#include <string.h>

// Merakit teks ke buffer MILIK PEMANGGIL, lengkap dengan pemeriksaan terpotong.
void rakit(char *keluar, size_t muat, const char *nama, int id) {
    int perlu = snprintf(keluar, muat, "%s-%03d", nama, id);
    if (perlu < 0 || (size_t) perlu >= muat) {
        printf("  (TERPOTONG: perlu %d karakter, yang muat cuma %zu)\\n",
               perlu, muat - 1);
    }
    printf("  [%s]\\n", keluar);
}

int main(void) {
    char buf[32];
    memset(buf, 0, sizeof buf);          // nolkan 32 byte sekaligus, tanpa loop
    printf("setelah memset : [%s]\\n", buf);

    printf("snprintf lega  :\\n");
    rakit(buf, sizeof buf, "levi", 7);
    char sempit[6];
    printf("snprintf sempit:\\n");
    rakit(sempit, sizeof sempit, "levi", 7);

    char salin[32];
    memcpy(salin, buf, strlen(buf) + 1); // +1 WAJIB supaya '\\0' ikut terbawa
    printf("memcpy         : [%s]\\n", salin);

    char geser[] = "abcdefg";
    memmove(geser + 2, geser, 5);        // asal & tujuan BERTUMPANG TINDIH
    printf("memmove        : [%s]\\n", geser);

    char p[4] = {'a', 'b', '\\0', 'X'};   // byte KEEMPAT sengaja dibuat beda,
    char q[4] = {'a', 'b', '\\0', 'Y'};   // padahal keduanya sama-sama "ab"
    printf("strcmp p vs q  : %s\\n", strcmp(p, q) == 0 ? "sama" : "beda");
    printf("memcmp 4 byte  : %s\\n", memcmp(p, q, 4) == 0 ? "sama" : "beda");

    char baris[] = "12,34";
    int x = 0, y = 0;
    if (sscanf(baris, "%d,%d", &x, &y) == 2) {   // SELALU cek jumlah yang terisi
        printf("sscanf         : x=%d y=%d\\n", x, y);
    }
    return 0;
}""",
            },
            {
                "body": [
                    "Ini jebakan yang sering menjebak orang:",
                    "",
                    "  1. memset(buf, 0, sizeof buf) cuma benar kalau buf array sungguhan.",
                    "     Begitu buf jadi parameter fungsi, dia meluruh jadi pointer (materi",
                    "     Pointer & Array), dan sizeof-nya jadi 8. Kamu cuma menolkan 8 byte",
                    "     pertama, lalu mengira semuanya sudah bersih.",
                    "  2. Urutan argumen memset gampang tertukar. Nilai dulu, baru jumlah.",
                    "     memset(b, 32, 0) nggak menulis apa-apa. Yang benar memset(b, 0,",
                    "     32).",
                    "  3. memcpy(dst, src, strlen(src)) melupakan '\\0'. Seharusnya",
                    "     strlen(src) + 1. Kalau nggak, dst nggak punya penutup, dan",
                    "     printf(\"%s\") bakal terus membaca sampai kebetulan menemukan nol di",
                    "     memori sebelah.",
                    "  4. Daerah yang bertumpang tindih wajib pakai memmove. memcpy boleh",
                    "     menyalin dengan urutan apa pun (bahkan 16 byte sekaligus), jadi",
                    "     hasilnya bisa benar hari ini lalu rusak sesudah ganti compiler.",
                    "     memmove menjamin hasilnya seolah sumbernya disalin dulu ke tempat",
                    "     sementara.",
                    "  5. strncpy, yang disarankan di materi String, nggak menjamin '\\0'",
                    "     kalau panjang sumbernya pas n. snprintf(dst, n, \"%s\", src) selalu",
                    "     menutup string-nya, jadi pakai itu.",
                    "",
                    "Ada dua kualifier lain yang bakal kamu temui waktu membaca kode orang.",
                    "Kualifier adalah kata tambahan pada tipe, seperti const.",
                    "",
                    "volatile artinya \"jangan simpan nilai ini di register, baca ulang dari",
                    "memori setiap kali\". Normalnya compiler boleh berasumsi nggak ada yang",
                    "mengubah variabel tanpa sepengetahuannya. Jadi while (siap == 0) {} sah",
                    "dioptimasi jadi loop yang nggak pernah berhenti. Kalau yang mengubah",
                    "siap adalah handler interrupt, sinyal, atau hardware, asumsi itu salah,",
                    "dan programnya menggantung tanpa satu pun pesan galat.",
                    "",
                    "  // register hardware:",
                    "  volatile uint32_t *reg = (volatile uint32_t *) 0x40021000;",
                    "  volatile int siap = 0;      // diubah dari handler interrupt/sinyal",
                    "",
                    "Perlu #include <stdint.h> untuk uint32_t. Catatan: volatile nggak",
                    "membuat kode aman untuk multi-thread. Itu urusan atomic dan mutex.",
                    "",
                    "restrict adalah janji kebalikannya: \"dua pointer ini nggak menunjuk",
                    "daerah yang sama\". Dengan janji itu, compiler boleh mengoptimasi lebih",
                    "agresif. Kalau janjinya ternyata bohong, hasilnya undefined. Di sinilah",
                    "semuanya ketemu. Prototipe aslinya berbunyi:",
                    "",
                    "  void *memcpy(void *restrict dst, const void *restrict src, size_t n);",
                    "  void *memmove(void *dst, const void *src, size_t n);      // TANPA restrict",
                    "",
                    "Baris itu alasan resmi kenapa memcpy dilarang untuk daerah yang",
                    "bertumpang tindih, sedangkan memmove boleh. Sekarang kamu bisa",
                    "membacanya sendiri dari header-nya.",
                ],
            },
        ],
    },
    {
        "title": "18. Dynamic Memory Allocation (malloc, calloc, free)",
        "sections": [
            {
                "body": [
                    "Array biasa punya ukuran tetap yang ditentukan waktu kompilasi. Dynamic",
                    "memory allocation memungkinkan kamu meminta memori waktu program",
                    "berjalan (runtime), dengan ukuran yang bisa ditentukan dari input",
                    "pengguna. Memori ini diambil dari heap, yaitu area memori besar yang",
                    "dipinjamkan sesuai permintaan program.",
                    "",
                    "Fungsi-fungsinya ada di <stdlib.h>:",
                    "  malloc(ukuran)         -> alokasi memori mentah (isi 'sampah')",
                    "  calloc(jumlah, ukuran)  -> alokasi + otomatis diisi NOL",
                    "  realloc(ptr, ukuranBaru)-> ubah ukuran alokasi yang sudah ada",
                    "  free(ptr)               -> KEMBALIKAN memori ke sistem (WAJIB!)",
                    "",
                    "Aturan emasnya: setiap malloc atau calloc harus diikuti satu free()",
                    "yang sesuai. Lupa free() menyebabkan memory leak (kebocoran memori),",
                    "yaitu memori yang terus terpakai walaupun sudah nggak dibutuhkan.",
                ]
            },
            {
                "heading": "Contoh malloc, penggunaan, dan free",
                "code": """#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int n;
    printf("Berapa banyak angka? ");
    scanf("%d", &n);

    // Alokasi array berukuran DINAMIS sesuai input user
    int *angka = (int*) malloc(n * sizeof(int));

    if (angka == NULL) {              // SELALU cek hasil malloc!
        printf("Alokasi memori gagal!\\n");
        return 1;
    }

    for (int i = 0; i < n; i++) {
        angka[i] = (i + 1) * 10;      // pointer hasil malloc BISA diakses [i]
    }

    for (int i = 0; i < n; i++) {
        printf("%d ", angka[i]);
    }
    printf("\\n");

    free(angka);        // WAJIB! kembalikan memori ke sistem
    angka = NULL;        // praktik baik: hindari 'dangling pointer'

    return 0;
}"""
            },
            {
                "heading": "Kenapa ada (int*) di depan malloc?",
                "body": [
                    "malloc nggak tahu, dan nggak peduli, kamu mau menyimpan apa di memori",
                    "itu. Prototipenya berbunyi:",
                    "",
                    "  void *malloc(size_t n);",
                    "",
                    "void * adalah \"alamat tanpa tipe\". Detailnya dibahas di materi C",
                    "Generik: void *, qsort & Fungsi Variadic. Yang perlu kamu tahu sekarang",
                    "cuma satu: di C, cast (int*) itu opsional. Baris ini sama sahnya, dan",
                    "lebih disukai kode C modern:",
                    "",
                    "  int *angka = malloc(n * sizeof(int));",
                    "",
                    "Ada juga bentuk yang lebih tahan salah, karena tipenya nggak perlu",
                    "ditulis dua kali. Kalau int nanti diganti jadi long, ukurannya ikut",
                    "menyesuaikan sendiri:",
                    "",
                    "  int *angka = malloc(n * sizeof *angka);",
                    "",
                    "Di C++, cast itu wajib, dan dari situlah kebiasaan menuliskannya",
                    "berasal. Jadi kalau kamu melihatnya di kode orang, sekarang kamu tahu",
                    "bahasa C sendiri nggak mengharuskannya.",
                ]
            },
            {
                "heading": "realloc: menumbuhkan array yang sudah telanjur dipakai",
                "body": [
                    "malloc memberi tempat sekali, dengan ukuran yang harus sudah kamu",
                    "ketahui. Padahal sering kali datanya datang satu per satu, dan",
                    "jumlahnya baru ketahuan di akhir. Contohnya isi berkas, masukan",
                    "pengguna, atau data dari jaringan. Untuk itulah ada realloc.",
                    "",
                    "Polanya selalu sama, dan namanya \"gandakan kapasitas kalau penuh\".",
                    "Mulai dari tempat kecil, lalu setiap kali penuh, minta dua kali lipat.",
                    "Menggandakan (dan nggak cuma menambah satu) membuat jumlah panggilan",
                    "realloc tetap sedikit walaupun datanya jutaan.",
                    "",
                    "Ada satu jebakan di sini, dan akibatnya mahal:",
                    "",
                    "  data = realloc(data, ukuranBaru);   // JANGAN pernah begini!",
                    "",
                    "Kalau realloc gagal, dia mengembalikan NULL, tapi blok lama tetap utuh",
                    "dan masih milikmu. Kalau data ditimpa dengan NULL, alamat blok lama itu",
                    "hilang selamanya. Kamu nggak bisa membacanya lagi, dan nggak bisa",
                    "mem-free-nya lagi. Memorinya bocor. Makanya hasil realloc selalu",
                    "ditampung dulu di pointer sementara, dan baru dipindahkan sesudah",
                    "terbukti nggak NULL.",
                ],
                "code": """#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int kapasitas = 2;                  // sengaja kecil supaya cepat penuh
    int jumlah = 0;
    int *data = malloc(kapasitas * sizeof *data);
    if (data == NULL) return 1;

    for (int i = 1; i <= 5; i++) {
        if (jumlah == kapasitas) {              // penuh -> gandakan
            int baru = kapasitas * 2;
            int *sementara = realloc(data, baru * sizeof *data);
            if (sementara == NULL) {            // GAGAL: blok lama MASIH utuh
                free(data);                     // jadi masih sempat dibebaskan
                return 1;
            }
            data = sementara;                   // baru sekarang boleh ditimpa
            kapasitas = baru;
        }
        data[jumlah++] = i * i;
    }

    for (int i = 0; i < jumlah; i++) printf("%d ", data[i]);
    printf("\\n");                               // 1 4 9 16 25
    printf("kapasitas akhir: %d\\n", kapasitas); // 8

    free(data);
    return 0;
}"""
            },
            {
                "body": [
                    "Ada tiga catatan tentang realloc:",
                    "  1. Isi lama disalin otomatis. Alamatnya bisa aja pindah, jadi pointer",
                    "     lain yang menunjuk ke dalam blok itu langsung basi sesudah realloc",
                    "     berhasil.",
                    "  2. realloc(NULL, n) berperilaku persis seperti malloc(n). Makanya",
                    "     banyak kode mulai dengan pointer NULL aja, dan nggak pernah",
                    "     memanggil malloc sama sekali.",
                    "  3. Tempat tambahannya nggak dinolkan. Isinya sampah, sama seperti",
                    "     malloc.",
                    "",
                    "Terakhir, malloc bukan satu-satunya cara mendapat ukuran yang baru",
                    "diketahui waktu program berjalan. Sejak C99 ada juga VLA:",
                    "",
                    "  int buf[n];      // VLA - lihat materi Array",
                    "",
                    "Bedanya penting. VLA hidup di stack yang kecil, ikut mati begitu",
                    "fungsinya selesai, dan ukurannya nggak bisa ditambah. Untuk data besar,",
                    "data yang harus hidup lebih lama dari fungsi pembuatnya, atau data yang",
                    "masih akan bertambah, pakai malloc dan realloc.",
                ]
            },
            {
                "body": [
                    "Ini bug klasik soal memori dinamis. Bug ini sering ditanyakan di",
                    "wawancara kerja, dan sering jadi penyebab crash aplikasi C/C++:",
                    "",
                    "  1. Memory leak: lupa free(), jadi memori yang bocor terus menumpuk",
                    "     selama program berjalan.",
                    "  2. Dangling pointer: memakai pointer sesudah di-free().",
                    "       int *p = malloc(...); free(p); *p = 5; // BAHAYA!",
                    "  3. Double free: memanggil free() dua kali pada pointer yang sama.",
                    "     Hasilnya undefined behavior, dan sering crash.",
                    "  4. Buffer overflow: menulis di luar batas memori yang dialokasikan.",
                    "",
                    "Alat untuk mendeteksi bug memori dibahas di materi Debugging: gdb,",
                    "valgrind & Bug Umum:",
                    "  valgrind ./program   -> mendeteksi memory leak & akses ilegal",
                ]
            },
        ],
    },
    {
        "title": "19. Struct",
        "sections": [
            {
                "body": [
                    "Struct adalah tipe data buatanmu sendiri yang menggabungkan beberapa",
                    "variabel jadi satu kesatuan. Variabel-variabel di dalamnya disebut",
                    "field, dan tipenya boleh beda-beda. Struct adalah cikal bakal konsep",
                    "class di bahasa OOP seperti Java dan C++.",
                    "",
                    "Contohnya, data seorang mahasiswa punya nama, umur, dan ipk. Daripada",
                    "tiga variabel terpisah, ketiganya bisa dibungkus jadi satu struct:",
                    "",
                    "  struct Mahasiswa {",
                    "      char nama[50];",
                    "      int umur;",
                    "      double ipk;",
                    "  };",
                    "",
                    "  struct Mahasiswa m1;         // deklarasi variabel struct",
                    "  strcpy(m1.nama, \"Andi\");     // akses field dengan titik (.)",
                    "  m1.umur = 20;",
                ]
            },
            {
                "heading": "Contoh struct, typedef, dan array of struct",
                "code": """#include <stdio.h>
#include <string.h>

// typedef membuat 'alias' agar tidak perlu tulis 'struct' berulang
typedef struct {
    char nama[50];
    int umur;
    double ipk;
} Mahasiswa;

void tampilkan(Mahasiswa m) {
    printf("%s, %d tahun, IPK %.2f\\n", m.nama, m.umur, m.ipk);
}

int main(void) {
    Mahasiswa m1;                    // dengan typedef, tanpa kata 'struct'
    strcpy(m1.nama, "Andi");
    m1.umur = 20;
    m1.ipk = 3.5;

    // Inisialisasi langsung (harus urut sesuai deklarasi field)
    Mahasiswa m2 = {"Budi", 22, 3.2};

    tampilkan(m1);
    tampilkan(m2);

    // Array of struct - untuk menyimpan BANYAK data terstruktur
    Mahasiswa daftar[2] = {
        {"Citra", 21, 3.8},
        {"Dedi", 23, 2.9}
    };
    for (int i = 0; i < 2; i++) {
        tampilkan(daftar[i]);
    }
    return 0;
}"""
            },
            {
                "heading": "Pointer ke struct (operator -> )",
                "code": """#include <stdio.h>

typedef struct {
    char nama[50];
    double saldo;
} Rekening;

void setor(Rekening *r, double jumlah) {   // terima POINTER agar bisa diubah
    r->saldo += jumlah;    // -> adalah shortcut untuk (*r).saldo
}

int main(void) {
    Rekening r1 = {"Andi", 100000};

    setor(&r1, 50000);     // kirim ALAMAT struct
    printf("Saldo: %.2f\\n", r1.saldo);   // 150000.00

    Rekening *ptr = &r1;
    printf("%s\\n", ptr->nama);       // akses field lewat pointer pakai ->
    printf("%s\\n", (*ptr).nama);     // SAMA PERSIS, tapi -> lebih ringkas
    return 0;
}"""
            },
        ],
    },
    {
        "title": "20. Struct Lanjutan: Inisialisasi Bernama, Bit-field & Tata Letak Memori",
        "sections": [
            {
                "body": [
                    "Di materi Struct ada satu kalimat yang perlu diluruskan: \"Inisialisasi",
                    "langsung (harus urut sesuai deklarasi field)\". Kalimat itu benar untuk",
                    "bentuk yang dipakai di sana. Tapi sejak C99 ada bentuk kedua, dan",
                    "bentuk kedua itulah yang paling banyak dipakai di kode C hari ini, dari",
                    "kernel Linux sampai pustaka kecil. Kalau kamu belum kenal, banyak kode",
                    "C sungguhan bakal kelihatan asing, padahal isinya hal yang sudah kamu",
                    "tahu.",
                    "",
                    "Designated initializer: sebut nama field-nya, dengan titik di",
                    "depannya.",
                    "",
                    "  Mahasiswa m = { .umur = 20, .nama = \"Andi\", .ipk = 3.5 };",
                    "",
                    "Dibanding {\"Andi\", 20, 3.5}, ada tiga hal yang berubah:",
                    "  - Urutan nggak berarti apa-apa lagi. .umur boleh ditulis duluan.",
                    "  - Field yang nggak disebut dijamin bernilai 0. Pointer jadi NULL,",
                    "    double jadi 0.0, dan array char jadi kosong. Ini dijamin standar,",
                    "    jadi kamu boleh mengandalkannya.",
                    "  - Kodenya menyebut sendiri apa yang sedang diisi. Kamu bisa",
                    "    membacanya tanpa membuka definisi struct-nya untuk menghitung koma.",
                    "",
                    "Poin terakhir itu lebih dari soal kerapian. Bentuk berurutan punya satu",
                    "jebakan yang nggak memunculkan error sama sekali. Begitu seseorang",
                    "menyisipkan satu field baru di tengah struct, semua {a, b, c} yang lama",
                    "bergeser maknanya tanpa ketahuan. Kalau tipe field yang bergeser",
                    "kebetulan cocok, compiler nggak bilang apa-apa, dan programnya jadi",
                    "salah. Bentuk bernama aman dari penyisipan seperti itu.",
                    "",
                    "Mengosongkan seluruh struct sekaligus:",
                    "",
                    "  Mahasiswa m = {0};  // semua field jadi 0 / NULL / 0.0 / string kosong",
                    "",
                    "Angka 0 di dalamnya cuma mengisi field pertama. Sisanya ikut nol karena",
                    "aturan \"yang nggak disebut jadi nol\" tadi. Kurung kurawal kosong ({})",
                    "baru sah di C23, jadi biasakan menulis {0} supaya aman di compiler mana",
                    "pun. Untuk variabel yang sudah telanjur ada dan mau dibersihkan ulang,",
                    "pakai memset dari <string.h>:",
                    "",
                    "  memset(&m, 0, sizeof m);    // & karena memset menerima ALAMAT (materi 15)",
                    "",
                    "Perhatikan sizeof m yang ditulis tanpa kurung. sizeof pada sebuah",
                    "variabel memang boleh ditulis begitu. Bentuk ini juga lebih awet",
                    "daripada sizeof(Mahasiswa). Kalau tipe m suatu saat diganti, baris ini",
                    "tetap benar tanpa perlu disunting.",
                    "",
                    "Bedanya halus tapi ada: {0} menolkan nilai tiap field, sedangkan",
                    "memset menolkan byte-nya. Di mesin biasa hasilnya sama, cuma memset",
                    "juga ikut membersihkan lubang padding. Itu justru berguna, dan",
                    "alasannya ada di bagian padding di bawah.",
                    "",
                    "Array juga punya bentuk bernama, dengan indeks di dalam kurung siku:",
                    "",
                    "  int hari[12] = { [0] = 31, [1] = 28, [2] = 31 };",
                    "  // sembilan sisanya otomatis 0",
                    "  const char *pesan[5] = { [4] = \"terakhir\" };",
                    "  // empat slot pertama NULL",
                    "",
                    "Bentuk ini bikin tabel yang jarang terisi enak ditulis. Tabel yang cuma",
                    "terisi di indeks 2 dan 13 nggak perlu diisi nol satu per satu, dan",
                    "indeksnya terbaca di sebelah nilainya.",
                    "",
                    "Compound literal adalah struct (atau array) tanpa nama yang dibuat",
                    "langsung di tempat:",
                    "",
                    "  tampilkan((Mahasiswa){ .nama = \"Andi\", .umur = 20 });",
                    "",
                    "Cara membacanya: (NamaTipe) di depan kurung kurawal berarti \"buatkan",
                    "satu objek bertipe ini, isinya segini, sekarang juga\". Gunanya untuk",
                    "argumen sekali pakai, supaya kamu nggak perlu membuat variabel",
                    "sementara yang cuma hidup satu baris.",
                    "",
                    "Compound literal juga satu-satunya cara menimpa isi struct yang sudah",
                    "ada sekaligus. Bagian ini sering bikin bingung, karena bentuknya mirip",
                    "dan salah satunya ditolak:",
                    "",
                    "  Mahasiswa m = { .umur = 20 };    // SAH: inisialisasi saat variabel lahir",
                    "  m = { .umur = 21 };              // DITOLAK: kurawal bukan sebuah nilai",
                    "  m = (Mahasiswa){ .umur = 21 };   // SAH: compound literal nilai yang utuh",
                    "",
                    "Jebakan: compound literal di dalam fungsi umurnya sependek variabel",
                    "lokal biasa. Menulis return &(Mahasiswa){...}; memberi pemanggilnya",
                    "pointer menggantung. Kasusnya persis sama dengan mengembalikan alamat",
                    "variabel lokal, dan sama berbahayanya.",
                    "",
                    "Semua bentuk di atas butuh C99 ke atas. gcc modern sudah memakainya",
                    "secara bawaan. Buat yang nanti mau belajar C++: bahasa itu baru",
                    "menerima designated initializer di C++20, dan di sana urutannya tetap",
                    "wajib mengikuti deklarasi.",
                ],
            },
            {
                "heading": "Semua bentuk inisialisasi dalam satu program",
                "code": """#include <stdio.h>
#include <string.h>

typedef struct {
    char   nama[50];
    int    umur;
    double ipk;
    int    aktif;
} Mahasiswa;

typedef struct {
    int         verbose;
    int         ulangi;
    const char *path;
} Opsi;

void tampilkan(Mahasiswa m) {
    printf("%-6s umur %2d  ipk %.2f  aktif %d\\n", m.nama, m.umur, m.ipk, m.aktif);
}

int main(void) {
    // Gaya materi 13: posisi yang menentukan segalanya.
    Mahasiswa lama = {"Budi", 22, 3.2, 1};

    // Designated initializer: field dipanggil NAMANYA, urutannya bebas.
    Mahasiswa m = { .umur = 20, .nama = "Andi", .ipk = 3.5 };
    // .aktif tidak disebut -> dijamin 0, bukan sampah.

    tampilkan(lama);
    tampilkan(m);

    Mahasiswa kosong = {0};          // seluruh struct dinolkan sekaligus
    printf("kosong: nama=\\"%s\\" umur=%d ipk=%.2f aktif=%d\\n",
           kosong.nama, kosong.umur, kosong.ipk, kosong.aktif);

    Mahasiswa dipakai = { .nama = "Citra", .umur = 21 };
    memset(&dipakai, 0, sizeof dipakai);   // alat yang sama untuk variabel yang SUDAH ada
    printf("setelah memset: nama=\\"%s\\" umur=%d\\n", dipakai.nama, dipakai.umur);

    Opsi o = { .verbose = 1, .path = "/tmp/data.txt" };
    printf("verbose=%d ulangi=%d path=%s\\n", o.verbose, o.ulangi, o.path);

    // Array juga bisa: indeksnya ditulis di dalam kurung siku.
    int hari[12] = { [0] = 31, [1] = 28, [2] = 31, [3] = 30 };
    printf("hari: %d %d %d %d %d\\n", hari[0], hari[1], hari[2], hari[3], hari[4]);

    // Compound literal: struct tanpa nama, dibuat langsung di tempat pemakaian.
    tampilkan((Mahasiswa){ .nama = "Dedi", .umur = 23, .ipk = 2.9 });

    // Menimpa seluruh isi variabel LAMA: butuh compound literal, bukan { } telanjang.
    m = (Mahasiswa){ .nama = "Andi", .umur = 21, .ipk = 3.6, .aktif = 1 };
    tampilkan(m);
    return 0;
}""",
            },
            {
                "heading": "Nama tag, alias typedef, tipe buram, dan menyalin struct",
                "body": [
                    "Materi Struct menulis typedef struct { ... } Mahasiswa; tanpa nama",
                    "sesudah kata struct. Contoh hubung-singkat di materi Ekspresi (dan",
                    "nanti materi Linked List) menulis typedef struct Node { ... } Node;",
                    "dengan nama Node muncul dua kali. Itu bukan salah ketik, dan",
                    "pengulangannya ada gunanya.",
                    "",
                    "C punya dua tempat penyimpanan nama yang terpisah:",
                    "  - Nama tag, yaitu kata sesudah struct. Tipenya bernama dua kata:",
                    "    struct Node.",
                    "  - Nama tipe biasa, tempat typedef menaruh aliasnya. Namanya satu",
                    "    kata: Node.",
                    "",
                    "Karena keduanya disimpan di tempat yang berbeda, nama yang sama boleh",
                    "dipakai di dua-duanya tanpa bertabrakan. Jadi baris typedef struct Node",
                    "{ ... } Node; artinya: buat struct dengan tag Node, lalu beri tipe itu",
                    "alias satu kata yang juga bernama Node.",
                    "",
                    "Kenapa di dalam badannya kamu tetap wajib menulis struct Node *next,",
                    "dan nggak boleh Node *next? Alias Node belum ada di situ. typedef baru",
                    "selesai di titik koma penutup, sesudah badannya habis. Waktu baris next",
                    "ditulis, satu-satunya nama yang sudah ada adalah tag-nya. Ini juga",
                    "sebabnya struct yang menunjuk dirinya sendiri selalu punya tag. Bentuk",
                    "anonim typedef struct { ... } Node; nggak punya nama apa pun untuk",
                    "dipakai di dalam dirinya sendiri.",
                    "",
                    "Deklarasi maju (forward declaration) artinya menyebut bahwa sebuah",
                    "struct ada, tanpa menyebut isinya.",
                    "",
                    "  struct Guru;  // tipenya ADA, isinya belum diketahui",
                    "  struct Murid { struct Guru  *wali; };",
                    "  struct Guru  { struct Murid *anak[30]; };",
                    "",
                    "Tanpa baris pertama, dua struct yang saling menunjuk mustahil ditulis,",
                    "karena salah satunya pasti disebut sebelum dikenal. Tipe yang sudah",
                    "disebut tapi belum dijelaskan isinya disebut tipe tidak lengkap",
                    "(incomplete type). Pointer ke tipe itu boleh dibuat, karena semua",
                    "pointer ukurannya sama dan compiler cukup tahu itu. Tapi variabelnya",
                    "nggak boleh dibuat. Mencoba Guru g; di sana menghasilkan error 'storage",
                    "size of g isn't known'.",
                    "",
                    "Tipe buram (opaque type) justru memanfaatkan keterbatasan itu. Di",
                    "header:",
                    "",
                    "  typedef struct Berkas Berkas;  // tidak ada satu pun field terlihat",
                    "  Berkas *berkas_buka(const char *nama);",
                    "  void    berkas_tutup(Berkas *b);",
                    "",
                    "Definisi lengkapnya, struct Berkas { FILE *fp; int baris; };,",
                    "disembunyikan di berkas .c milik pustakanya. Pemakai cuma memegang",
                    "pointer dan memanggil fungsi.",
                    "",
                    "Contoh nyata pola ini adalah FILE dari <stdio.h>, yang dipakai di",
                    "materi File I/O. Di sana kamu selalu menulis FILE *fp sebagai pointer,",
                    "nggak pernah FILE f, dan isinya nggak pernah kamu sentuh. Itu",
                    "disengaja. Untungnya dua arah. Pustakanya bebas mengubah field di",
                    "dalam tanpa memaksa program siapa pun dikompilasi ulang. Pemakainya",
                    "juga nggak bisa merusak keadaan internal yang nggak dia mengerti.",
                    "",
                    "Menyalin struct: satu tanda = menyalin seluruh isinya.",
                    "",
                    "  Rapor salinan = asli;  // semua field ikut, termasuk ISI array di dalamnya",
                    "",
                    "Ini kejutan kecil yang berguna. Array biasa nggak bisa disalin dengan =",
                    "(materi String memakai strcpy justru karena itu). Tapi array yang ada",
                    "di dalam struct ikut tersalin utuh. Membungkus array dalam struct",
                    "adalah cara resmi supaya array bisa disalin dan dikembalikan dari",
                    "fungsi.",
                    "",
                    "Tapi salinannya dangkal. Field yang berupa pointer disalin alamatnya,",
                    "dan barang yang ditunjuk nggak ikut tersalin. Dua struct itu lalu",
                    "berbagi objek yang sama, dan mem-free salah satunya membuat pointer di",
                    "struct satunya lagi menggantung.",
                    "",
                    "Membandingkan struct: nggak ada operatornya. if (a == b) pada dua",
                    "struct ditolak compiler. C sengaja nggak menebak. Apakah dua rapor",
                    "\"sama\" kalau namanya sama? Bagaimana kalau pointernya menunjuk objek",
                    "berbeda dengan isi yang sama? Nggak ada jawaban yang benar untuk semua",
                    "orang, jadi kamu yang menuliskannya sendiri, field demi field.",
                    "",
                    "Godaan berikutnya biasanya memcmp(&a, &b, sizeof a). Cara ini malah",
                    "lebih berbahaya, karena sering kelihatan berhasil. memcmp",
                    "membandingkan byte mentah, termasuk lubang padding yang isinya nggak",
                    "dijamin apa-apa, dan termasuk sisa sampah di array char sesudah '\\0'.",
                    "Dua struct yang seluruh field-nya identik bisa dinyatakan berbeda.",
                    "Bagian berikutnya menjelaskan lubang itu.",
                ],
                "code": """#include <stdio.h>
#include <string.h>

// Nama Node muncul DUA KALI dengan arti yang berbeda:
//   struct Node {   <- nama TAG, satu-satunya nama yang sudah ada di dalam badan
//   } Node;         <- nama ALIAS typedef, baru lahir di titik koma penutup
typedef struct Node {
    int          data;
    struct Node *next;      // WAJIB 'struct Node': alias Node belum ada di sini
} Node;

typedef struct {
    char  nama[50];
    int  *nilai;            // POINTER: yang tersalin nanti cuma alamatnya
} Rapor;

int main(void) {
    Node c = { .data = 3, .next = NULL };
    Node b = { .data = 2, .next = &c };
    Node a = { .data = 1, .next = &b };

    for (Node *p = &a; p != NULL; p = p->next) {
        printf("%d ", p->data);
    }
    printf("\\n");

    int angka = 90;
    Rapor asli = { .nama = "Andi", .nilai = &angka };

    Rapor salinan = asli;      // satu tanda '=' menyalin SELURUH isi struct

    strcpy(salinan.nama, "Budi");        // array nama benar-benar terpisah
    printf("asli.nama=%s  salinan.nama=%s\\n", asli.nama, salinan.nama);

    *salinan.nilai = 75;                 // tapi pointernya menunjuk objek yang SAMA
    printf("angka lewat asli.nilai = %d\\n", *asli.nilai);

    // if (asli == salinan) { }   <- TIDAK bisa dikompilasi: C tidak punya == untuk struct.
    if (strcmp(asli.nama, salinan.nama) == 0 && asli.nilai == salinan.nilai) {
        printf("dianggap sama\\n");
    } else {
        printf("dianggap beda\\n");       // ini yang tercetak
    }
    return 0;
}""",
            },
            {
                "heading": "Padding: kenapa sizeof struct lebih besar dari jumlah fieldnya",
                "body": [
                    "Materi Variabel & Tipe Data dan materi Array mengajarkan sizeof dengan",
                    "teliti. Jadi cepat atau lambat pertanyaan ini muncul: struct berisi",
                    "char + int + char + double punya jumlah ukuran field 1+4+1+8 = 14 byte,",
                    "tapi sizeof-nya 24. Sepuluh byte itu nggak hilang. Itu lubang yang",
                    "sengaja dipasang compiler.",
                    "",
                    "Penyebabnya alignment (penjajaran). Prosesor membaca memori per blok,",
                    "dan setiap tipe punya syarat alamat: int 4 byte wajib mulai di alamat",
                    "kelipatan 4, dan double 8 byte di kelipatan 8. Aturan ini ada",
                    "akibatnya. Di x86, alamat yang meleset cuma bikin aksesnya lebih",
                    "lambat. Di banyak prosesor ARM dan embedded, alamat yang meleset",
                    "langsung jadi kesalahan hardware dan programnya mati.",
                    "",
                    "Compiler menyisipkan padding, yaitu byte kosong, supaya setiap field",
                    "mendarat di alamat yang sah. Compiler nggak boleh menyusun ulang urutan",
                    "field-mu, karena C menjamin field ditempatkan sesuai urutan",
                    "deklarasinya. Jadi satu-satunya hal yang bisa kamu atur adalah urutan",
                    "penulisannya.",
                    "",
                    "  struct Boros { char a; int b; char c; double d; };",
                    "",
                    "  byte 0           ->  a",
                    "  byte 1 s.d. 3    ->  padding, supaya b mendarat di alamat kelipatan 4",
                    "  byte 4 s.d. 7    ->  b",
                    "  byte 8           ->  c",
                    "  byte 9 s.d. 15   ->  padding, supaya d mendarat di alamat kelipatan 8",
                    "  byte 16 s.d. 23  ->  d",
                    "",
                    "Ada padding kedua yang sering terlupa, yaitu di ekor. Ukuran struct",
                    "dibulatkan ke atas sampai kelipatan syarat alignment terketatnya (di",
                    "sini 8, karena ada double). Alasannya array. Kalau satu elemen",
                    "berukuran 21 byte, elemen kedua bakal mulai di alamat 21, dan double di",
                    "dalamnya jadi nggak sejajar. Makanya ukurannya 24, dan nggak 21.",
                    "",
                    "Urutkan field dari yang terbesar ke yang terkecil, dan lubangnya",
                    "menyusut sendiri. Dengan data yang sama persis, 24 byte jadi 16 byte,",
                    "hemat sepertiga. Untuk satu variabel, ini nggak ada artinya. Untuk",
                    "array satu juta record, hematnya 8 MB, dan cache prosesor lebih banyak",
                    "terpakai untuk data sungguhan.",
                    "",
                    "offsetof(tipe, field) dari <stddef.h> memberi posisi byte sebuah field",
                    "di dalam struct-nya. Fungsinya lebih dari alat intip untuk belajar.",
                    "Kode C tingkat rendah memakainya sungguhan, misalnya makro container_of",
                    "di kernel Linux, yang berjalan mundur dari alamat sebuah field ke alamat",
                    "struct yang memuatnya.",
                    "",
                    "Ada dua akibat yang perlu kamu ingat:",
                    "",
                    "  1. memcmp nggak bisa dipercaya untuk membandingkan struct. Isi lubang",
                    "     padding nggak dijamin apa pun. Bahkan sesudah a = b, padding-nya",
                    "     belum tentu ikut tersalin. Kalau kamu memang harus membandingkan",
                    "     atau meng-hash byte mentahnya, nolkan dulu seluruh struct-nya",
                    "     dengan memset sebelum field-field-nya diisi.",
                    "",
                    "  2. fwrite(&s, sizeof s, 1, fp) menulis padding dan tata letak mesinmu",
                    "     apa adanya ke dalam berkas. Berkas itu nggak bisa diandalkan untuk",
                    "     dibaca compiler lain atau arsitektur lain. Format berkas dan",
                    "     protokol jaringan yang serius selalu menulis field satu per satu,",
                    "     dengan ukuran yang ditetapkan sendiri.",
                    "",
                    "Ada cara memaksa padding hilang, yaitu #pragma pack(1) atau",
                    "__attribute__((packed)). Tapi keduanya di luar standar C, dan hasilnya",
                    "struct yang field-nya nggak sejajar. Mengambil pointer ke field di",
                    "dalamnya lalu membacanya adalah bug yang tinggal menunggu waktu. Pakai",
                    "cuma kalau memang nggak ada pilihan lain, dan sadari harganya.",
                ],
                "code": """#include <stdio.h>
#include <stddef.h>       // offsetof

struct Boros {
    char   a;             // 1 byte
    int    b;             // 4 byte, alamatnya wajib kelipatan 4
    char   c;             // 1 byte
    double d;             // 8 byte, alamatnya wajib kelipatan 8
};

struct Rapi {             // field yang SAMA, cuma diurutkan dari besar ke kecil
    double d;
    int    b;
    char   a;
    char   c;
};

int main(void) {
    printf("jumlah mentah semua field = %zu byte\\n",
           sizeof(char) + sizeof(int) + sizeof(char) + sizeof(double));
    printf("sizeof(struct Boros)      = %zu byte\\n", sizeof(struct Boros));
    printf("sizeof(struct Rapi)       = %zu byte\\n", sizeof(struct Rapi));
    printf("\\n");

    printf("Boros  a=%zu  b=%zu  c=%zu  d=%zu\\n",
           offsetof(struct Boros, a), offsetof(struct Boros, b),
           offsetof(struct Boros, c), offsetof(struct Boros, d));
    printf("Rapi   d=%zu  b=%zu  a=%zu  c=%zu\\n",
           offsetof(struct Rapi, d), offsetof(struct Rapi, b),
           offsetof(struct Rapi, a), offsetof(struct Rapi, c));

    // Lubang padding itu nyata: hitung berapa byte yang terlewat antara a dan b.
    printf("\\nlubang antara a dan b di Boros = %zu byte\\n",
           offsetof(struct Boros, b) - offsetof(struct Boros, a) - sizeof(char));
    return 0;
}""",
            },
            {
                "heading": "Bit-field: field yang diukur dalam bit, bukan byte",
                "body": [
                    "Kadang satu byte per penanda pun terlalu boros, misalnya di header",
                    "protokol jaringan, register hardware, atau array record yang jumlahnya",
                    "jutaan. C membolehkan sebuah field diberi lebar dalam bit, ditulis",
                    "dengan titik dua sesudah namanya.",
                    "",
                    "  struct Flag {",
                    "      unsigned int aktif     : 1;    // 1 bit  -> hanya 0 atau 1",
                    "      unsigned int prioritas : 3;    // 3 bit  -> 0..7",
                    "      unsigned int tipe      : 4;    // 4 bit  -> 0..15",
                    "  };",
                    "",
                    "Cara memakainya persis seperti field biasa, misalnya f.prioritas = 5.",
                    "Jadi kodenya tetap gampang dibaca, padahal ketiga field itu berdesakan",
                    "di satu byte. Tiga unsigned int biasa makan 12 byte, sedangkan struct",
                    "di atas cuma 4 byte.",
                    "",
                    "Ada empat jebakan bit-field:",
                    "  1. Nilai yang nggak muat dipotong tanpa pemberitahuan. Ini yang",
                    "     paling sering kena. Field 3 bit cuma bisa menampung 0..7. Kalau",
                    "     diisi 8, hasilnya 0, tanpa error dan tanpa peringatan. Kalau",
                    "     angkanya datang dari variabel waktu program berjalan, compiler",
                    "     nggak punya kesempatan mengeluh sama sekali. Kamu sendiri yang",
                    "     harus menjaga jangkauannya.",
                    "  2. Tulis unsigned secara eksplisit. Untuk int x : 1; yang polos,",
                    "     standar C membiarkan compiler memilih apakah bit-nya bertanda.",
                    "     Kalau bertanda, field 1 bit itu cuma bisa berisi 0 dan -1, dan",
                    "     kode if (x == 1) nggak akan pernah benar.",
                    "  3. Bit-field nggak punya alamat sendiri. &f.aktif ditolak compiler,",
                    "     karena alamat terkecil yang bisa ditunjuk di C adalah satu byte",
                    "     penuh. Akibatnya bit-field nggak bisa dipakai di scanf(\"%d\",",
                    "     &f.aktif), dan nggak bisa dikirim ke fungsi yang minta pointer.",
                    "  4. Tata letaknya nggak portabel. Jebakan ini membatalkan kegunaan",
                    "     yang paling sering dibayangkan orang. Standar C nggak menetapkan",
                    "     dari ujung mana field pertama mulai diisi (ada compiler yang mulai",
                    "     dari bit terendah, ada yang dari tertinggi). Standar juga nggak",
                    "     menetapkan apakah sebuah field boleh terbelah melewati batas unit",
                    "     penyimpanan, dan berapa padding yang disisipkan. Jadi struct",
                    "     bit-field nggak bisa diandalkan sebagai peta untuk paket jaringan",
                    "     atau format berkas.",
                    "",
                    "Kode jaringan yang benar membaca byte mentah, lalu membongkarnya",
                    "sendiri dengan geser bit dan topeng, yaitu operator bitwise dari materi",
                    "Operator. Cara itu juga dicontohkan di bawah, supaya kelihatan bahwa",
                    "bit-field cuma menuliskan hal yang sama dengan lebih rapi.",
                    "",
                    "Jadi kapan bit-field layak dipakai? Waktu kode dan pembacanya ada di",
                    "mesin yang sama. Contohnya penanda hemat tempat di struct besar, serta",
                    "driver dan kernel yang dikompilasi satu compiler untuk satu target yang",
                    "sudah pasti. Digabung dengan union (materi Union & Enum), pola ini juga",
                    "dipakai untuk melihat satu register hardware dari dua sisi sekaligus:",
                    "sebagai satu angka utuh, dan sebagai kumpulan bit bernama.",
                ],
                "code": """#include <stdio.h>

// Satu byte flag di header sebuah protokol, dipetakan jadi field bernama.
struct Flag {
    unsigned int aktif     : 1;    // 1 bit  -> hanya 0 atau 1
    unsigned int prioritas : 3;    // 3 bit  -> 0..7
    unsigned int tipe      : 4;    // 4 bit  -> 0..15
};

struct TanpaBitfield {             // field yang sama tanpa ':' sama sekali
    unsigned int aktif;
    unsigned int prioritas;
    unsigned int tipe;
};

int main(void) {
    struct Flag f = { .aktif = 1, .prioritas = 5, .tipe = 9 };

    printf("aktif=%u prioritas=%u tipe=%u\\n", f.aktif, f.prioritas, f.tipe);
    printf("sizeof(struct Flag)          = %zu byte\\n", sizeof(struct Flag));
    printf("sizeof(struct TanpaBitfield) = %zu byte\\n", sizeof(struct TanpaBitfield));

    unsigned int diminta = 8;      // 8 butuh 4 bit, ladangnya cuma punya 3
    f.prioritas = diminta;         // dipotong DIAM-DIAM, tanpa error apa pun
    printf("prioritas setelah diisi 8    = %u\\n", f.prioritas);

    // Cara manual yang setara, memakai operator bitwise dari materi 3:
    unsigned char paket = 0;
    paket |= 1u;                   // bit 0   = aktif
    paket |= (5u & 7u) << 1;       // bit 1-3 = prioritas
    paket |= (9u & 15u) << 4;      // bit 4-7 = tipe
    printf("paket manual = 0x%02X\\n", paket);
    printf("dibaca lagi: aktif=%u prioritas=%u tipe=%u\\n",
           paket & 1u, (paket >> 1) & 7u, (paket >> 4) & 15u);

    // &f.aktif TIDAK bisa ditulis: bit-field tidak punya alamat sendiri.
    return 0;
}""",
            },
        ],
    },
    {
        "title": "21. Union & Enum",
        "sections": [
            {
                "body": [
                    "UNION mirip struct, tapi SEMUA field BERBAGI alamat memori",
                    "YANG SAMA - hanya SATU field yang valid pada satu waktu.",
                    "Ukuran union = ukuran field TERBESAR di dalamnya (hemat memori).",
                    "",
                    "  union Data {",
                    "      int angka;",
                    "      float desimal;",
                    "      char karakter;",
                    "  };",
                    "  union Data d;",
                    "  d.angka = 10;      // menulis 'angka' MENIMPA memori 'desimal' juga",
                    "  printf(\"%d\", d.angka);  // OK, ini yang terakhir ditulis",
                    "",
                    "Union JARANG dipakai di kode aplikasi biasa, tapi berguna",
                    "untuk optimasi memori di programming embedded/sistem level rendah.",
                ]
            },
            {
                "heading": "Contoh enum (enumeration) - PALING sering dipakai",
                "code": """#include <stdio.h>

// enum: cara membuat KONSTANTA BERNAMA yang lebih jelas dari angka mentah
enum Hari {
    SENIN,      // otomatis bernilai 0
    SELASA,     // 1
    RABU,       // 2
    KAMIS,      // 3
    JUMAT,      // 4
    SABTU,      // 5
    MINGGU      // 6
};

// Bisa juga set nilai awal manual:
enum StatusHttp {
    OK = 200,
    NOT_FOUND = 404,
    SERVER_ERROR = 500
};

int main(void) {
    enum Hari hariIni = RABU;

    if (hariIni == RABU) {
        printf("Hari ini Rabu (nilai enum: %d)\\n", hariIni);   // 2
    }

    enum StatusHttp status = NOT_FOUND;
    printf("Status: %d\\n", status);   // 404

    // Kenapa enum lebih baik dari angka mentah ('magic number'):
    // if (hariIni == 2)  <- kurang jelas, 2 itu apa?
    // if (hariIni == RABU) <- JAUH lebih jelas maksudnya!
    return 0;
}"""
            },
        ],
    },
    {
        "title": "22. File I/O",
        "sections": [
            {
                "body": [
                    "File I/O di C memakai tipe FILE* (pointer ke struct FILE)",
                    "dari <stdio.h>.",
                    "",
                    "Fungsi utama:",
                    "  fopen(nama, mode)   -> membuka file, kembalikan FILE* (atau",
                    "                          NULL jika gagal - SELALU cek!)",
                    "  fclose(fp)          -> menutup file (WAJIB, seperti free())",
                    "  fprintf(fp, ...)    -> menulis (seperti printf, tapi ke file)",
                    "  fscanf(fp, ...)     -> membaca (seperti scanf, tapi dari file)",
                    "  fgets(buffer, n, fp)-> membaca satu baris (LEBIH AMAN)",
                    "  fputs/fputc/fgetc   -> tulis/baca string/karakter",
                    "",
                    "Mode file:",
                    "  \"r\"  -> read (baca)      \"w\"  -> write (tulis, timpa isi lama)",
                    "  \"a\"  -> append (tambah)  \"r+\" -> baca & tulis",
                    "  \"w+\" -> baca & tulis, isi lama DIHAPUS lebih dulu",
                    "  \"a+\" -> baca & tulis, tapi tulisannya SELALU di akhir",
                    "",
                    "Huruf b boleh ditempel di belakang mana pun - \"rb\", \"wb\", \"ab\",",
                    "\"rb+\" - artinya mode BINER: byte berkas dilewatkan apa adanya,",
                    "tanpa terjemahan akhir baris. Di Linux dan macOS b tidak",
                    "mengubah apa pun, tapi di Windows mode teks diam-diam mengubah",
                    "\\n jadi \\r\\n saat menulis. Untuk berkas non-teks (gambar, .dat",
                    "hasil fwrite) b itu WAJIB, kalau tidak isinya rusak di Windows.",
                    "Kebiasaannya sederhana: teks tanpa b, selain teks pakai b.",
                    "Berkas biner dan fread/fwrite dibahas di materi I/O Tingkat",
                    "Karakter & Berkas Biner.",
                ]
            },
            {
                "heading": "Contoh menulis & membaca file",
                "code": """#include <stdio.h>

int main(void) {
    // Menulis ke file
    FILE *fp = fopen("catatan.txt", "w");
    if (fp == NULL) {                    // SELALU cek hasil fopen!
        printf("Gagal membuka file untuk menulis!\\n");
        return 1;
    }
    fprintf(fp, "Baris pertama\\n");
    fprintf(fp, "Angka: %d\\n", 42);
    fclose(fp);                          // WAJIB ditutup!

    // Membaca file baris per baris (cara PALING aman)
    FILE *fp2 = fopen("catatan.txt", "r");
    if (fp2 == NULL) {
        printf("Gagal membuka file untuk membaca!\\n");
        return 1;
    }

    char baris[100];
    while (fgets(baris, sizeof(baris), fp2) != NULL) {
        printf("Baca: %s", baris);       // fgets menyertakan \\n, tak perlu tambah lagi
    }
    fclose(fp2);

    return 0;
}"""
            },
            {
                "body": [
                    "Kenapa fgets() LEBIH DISARANKAN dari fscanf(\"%s\", ...):",
                    "  - fgets() membaca SATU BARIS PENUH termasuk spasi.",
                    "  - fgets() menerima parameter UKURAN BUFFER, mencegah",
                    "    buffer overflow (fscanf %s TIDAK punya batasan ini).",
                    "",
                    "Selalu ikuti pola: cek NULL setelah fopen(), lalu WAJIB",
                    "fclose() di akhir (atau saat keluar lebih awal karena error) -",
                    "lupa fclose() bisa menyebabkan file rusak/data tidak tersimpan.",
                    "",
                    "Satu hal yang menjelaskan kejanggalan dari materi sebelumnya:",
                    "stdin (keyboard), stdout (layar), dan stderr (layar, jalur",
                    "pesan galat) SENDIRI bertipe FILE *, sudah dibuka otomatis",
                    "sebelum main() mulai dan tidak perlu - tidak boleh - kamu",
                    "fopen. Itulah sebabnya fgets(nama, sizeof(nama), stdin) di",
                    "materi Input & Output memakai fungsi BERKAS untuk membaca",
                    "ketikan, dan kenapa printf(...) sama saja dengan",
                    "fprintf(stdout, ...). Ketiganya dibahas di materi Program &",
                    "Sistem: argc, argv, Stream Standar & Kode Keluar.",
                ]
            },
        ],
    },
    {
        "title": "23. Program & Sistem: argc, argv, Stream Standar & Kode Keluar",
        "sections": [
            {
                "body": [
                    "Sampai sini SEMUA contoh memakai int main(void) - main yang tidak menerima apa-apa.",
                    "Tapi buka kode C mana pun di GitHub - Git, Redis, SQLite, kernel Linux - dan baris",
                    "pertama programnya hampir selalu berbunyi begini:",
                    "",
                    "  int main(int argc, char *argv[])",
                    "",
                    "Itulah cara program menerima kata-kata yang diketik SESUDAH namanya di terminal.",
                    "Saat kamu mengetik:",
                    "",
                    "  ./tampil catatan.txt -n",
                    "",
                    "shell memecah baris itu jadi tiga kata, lalu menyerahkannya ke programmu:",
                    "",
                    "  argc = 3                  jumlah kata, TERMASUK nama programnya sendiri",
                    "  argv[0] = \"./tampil\"      SELALU nama program - bukan argumen pertama",
                    "  argv[1] = \"catatan.txt\"   argumen pertama yang sesungguhnya",
                    "  argv[2] = \"-n\"",
                    "  argv[3] = NULL            standar C menjamin slot sesudah yang terakhir NULL",
                    "",
                    "Tiga hal yang paling sering bikin salah:",
                    "  1. argc tidak pernah 0 dalam praktik; nilai terkecilnya 1 (cuma nama program).",
                    "     Jadi 'ada argumen atau tidak' diperiksa dengan if (argc < 2), BUKAN argc == 0.",
                    "  2. Loop argumen mulai dari i = 1, bukan i = 0 - kecuali kamu memang mau argv[0].",
                    "  3. Isi argv SELALU string, walau yang kamu ketik terlihat seperti angka.",
                    "     \"42\" bukan 42. Menyerahkannya ke printf(\"%d\") langsung adalah bug.",
                    "",
                    "char *argv[] artinya 'array of pointer ke char', yaitu array of string. Karena nama",
                    "array meluruh jadi pointer ke elemen pertamanya (materi Pointer & Array), bentuk di",
                    "bawah ini IDENTIK artinya dan sama seringnya kamu temui:",
                    "",
                    "  int main(int argc, char **argv)     // sama persis, cuma beda cara menulis",
                    "",
                    "argv adalah pointer ke pointer; argv[1] satu string (char *); argv[1][0] huruf",
                    "pertamanya (char).",
                    "",
                    "Mengubah argumen jadi angka - dua jalan, satu di antaranya buruk:",
                    "  atoi(argv[1])                ringkas, TAPI mengembalikan 0 untuk masukan tidak",
                    "                               sah - padahal 0 juga jawaban sah untuk \"0\". Kamu",
                    "                               tidak punya cara membedakan keduanya.",
                    "  strtol(argv[1], &sisa, 10)   memberi tahu SAMPAI MANA ia berhasil membaca lewat",
                    "                               pointer 'sisa'. Kalau *sisa bukan '\\0', ada sampah",
                    "                               di belakang angkanya -> tolak masukannya.",
                    "  (Kedua fungsi ini dibahas utuh di materi Pustaka Standar; di sini yang penting",
                    "   kenapa pemeriksaannya wajib: argumen datang dari manusia, bukan dari kodemu.)",
                ],
            },
            {
                "heading": "Membaca argumen: cetak argc dan seluruh argv",
                "code": """#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    printf("argc = %d\\n", argc);
    printf("argv[0] = %s   <- nama program, BUKAN argumen pertama\\n", argv[0]);

    for (int i = 1; i < argc; i++) {     // mulai dari 1, lewati nama program
        printf("argv[%d] = %s\\n", i, argv[i]);
    }

    if (argv[argc] == NULL) {            // dijamin oleh standar C
        printf("argv[%d] = NULL   <- penanda akhir daftar\\n", argc);
    }

    if (argc >= 2) {
        char *sisa;
        long n = strtol(argv[1], &sisa, 10);      // 10 = basis desimal
        if (sisa == argv[1] || *sisa != '\\0') {   // tak ada digit, atau ada sisa
            printf("argv[1] bukan angka utuh, tidak jadi dikonversi.\\n");
        } else {
            printf("argv[1] sebagai angka: %ld, dikali dua: %ld\\n", n, n * 2);
        }
    }
    return 0;
}""",
            },
            {
                "body": [
                    "Kompilasi, lalu jalankan dengan beberapa kata di belakangnya. Kalau hasil",
                    "kompilasinya kamu beri nama ./argumen dan yang kamu ketik ./argumen 21 apel:",
                    "",
                    "  argc = 3",
                    "  argv[0] = ./argumen   <- nama program, BUKAN argumen pertama",
                    "  argv[1] = 21",
                    "  argv[2] = apel",
                    "  argv[3] = NULL   <- penanda akhir daftar",
                    "  argv[1] sebagai angka: 21, dikali dua: 42",
                    "",
                    "Coba juga ./argumen 12abc - strtol berhasil membaca 12 lalu berhenti di 'a', jadi",
                    "*sisa = 'a' dan masukannya ditolak. atoi() akan diam-diam menjawab 12.",
                    "",
                    "TIGA STREAM STANDAR",
                    "Setiap program C yang mulai berjalan SUDAH punya tiga berkas terbuka, tanpa satu",
                    "pun panggilan fopen():",
                    "",
                    "  stdin    FILE *   masukan    - biasanya ketikan keyboard",
                    "  stdout   FILE *   keluaran   - biasanya layar; ini HASIL kerja programmu",
                    "  stderr   FILE *   keluhan    - juga layar, tapi jalur TERPISAH untuk pesan galat",
                    "",
                    "Ketiganya bertipe FILE * yang sama persis dengan hasil fopen() di materi File I/O.",
                    "Artinya fgets(nama, sizeof(nama), stdin) yang dipakai sejak materi Input & Output",
                    "sebenarnya fungsi BERKAS biasa - stdin cuma kebetulan berkas yang sudah dibukakan",
                    "untukmu. Begitu juga printf: printf(\"%d\\n\", x) hanyalah nama pendek untuk",
                    "fprintf(stdout, \"%d\\n\", x). Tidak ada sihir; cuma berkas yang sudah terbuka.",
                    "",
                    "KENAPA stderr HARUS ADA - alasannya sangat praktis:",
                    "",
                    "  ./tampil catatan.txt > hasil.txt",
                    "",
                    "Tanda > mengalihkan stdout SAJA ke berkas. Pesan galat yang dicetak dengan",
                    "fprintf(stderr, \"...\") TETAP muncul di layar, jadi kamu langsung tahu ada yang",
                    "gagal walau hasilnya masuk berkas. Kalau galat itu kamu cetak dengan printf, ia",
                    "ikut tertelan ke hasil.txt: mengotori data DAN hilang dari pandanganmu sekaligus.",
                    "",
                    "  ./tampil catatan.txt > hasil.txt 2> galat.txt   # 2> khusus mengalihkan stderr",
                    "  ./tampil catatan.txt 2> /dev/null               # buang semua keluhannya",
                    "",
                    "Aturan praktisnya: stdout untuk hal yang mau diolah program lain, stderr untuk hal",
                    "yang mau dibaca manusia. Progress bar, peringatan, dan pesan galat -> stderr.",
                    "",
                    "BUFFERING - sumber keluhan 'kok urutannya kebalik?'",
                    "stdout tidak langsung dikirim; ia ditumpuk dulu di buffer, dan perilakunya berubah",
                    "tergantung ke mana ia mengalir:",
                    "  - ke terminal     buffer BARIS: disiram tiap ketemu \\n. Urutan terlihat wajar.",
                    "  - ke berkas/pipe  buffer PENUH: baru disiram setelah beberapa KB terkumpul.",
                    "  - stderr          TIDAK di-buffer sama sekali - pesan galat harus sampai walau",
                    "                    program keburu crash sedetik kemudian.",
                    "",
                    "Akibatnya nyata di program berikutnya: dijalankan ke terminal, baris-baris berkas",
                    "keluar dulu baru catatan stderr-nya. Dialihkan ke berkas atau pipe, catatan stderr",
                    "justru muncul DULUAN. Itu bukan bug, cuma dua buffer dengan aturan berbeda.",
                    "",
                    "fflush(stdout) memaksa isi buffer keluar saat itu juga. Yang paling sering butuh:",
                    "  printf(\"Nama: \");   fflush(stdout);   fgets(nama, sizeof(nama), stdin);",
                    "Tanpa fflush, prompt tanpa \\n itu bisa belum kelihatan saat program sudah diam",
                    "menunggu ketikan - dan orang mengira programnya hang.",
                ],
            },
            {
                "heading": "Alat baris perintah: tampilkan isi berkas dari argv",
                "code": """#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    if (argc < 2) {
        fprintf(stderr, "Pemakaian: %s <berkas>\\n", argv[0]);
        return 1;                        // BUKAN 0: program tidak mengerjakan tugasnya
    }

    FILE *fp = fopen(argv[1], "r");      // nama berkas datang dari baris perintah
    if (fp == NULL) {
        fprintf(stderr, "%s: gagal membuka '%s'\\n", argv[0], argv[1]);
        exit(EXIT_FAILURE);              // efeknya sama dengan return 1 di main
    }

    char baris[512];
    int nomor = 1;
    while (fgets(baris, sizeof(baris), fp) != NULL) {
        printf("%4d | %s", nomor, baris);                // HASIL   -> stdout
        nomor++;
    }
    fclose(fp);

    fprintf(stderr, "(%d baris dibaca)\\n", nomor - 1);    // CATATAN -> stderr
    return EXIT_SUCCESS;                 // EXIT_SUCCESS bernilai 0
}""",
            },
            {
                "body": [
                    "Kompilasi programnya - anggap hasilnya bernama ./tampil - lalu coba empat hal ini:",
                    "  ./tampil                     -> 'Pemakaian: ./tampil <berkas>' di stderr, keluar 1",
                    "  ./tampil hantu.txt           -> pesan gagal membuka di stderr, keluar 1",
                    "  ./tampil catatan.txt         -> isi berkas bernomor di stdout, keluar 0",
                    "  ./tampil catatan.txt > h.txt -> h.txt berisi hasilnya, catatan tetap di layar",
                    "Bentuk ini - periksa argc, ambil nama berkas dari argv[1], keluhkan lewat stderr -",
                    "adalah kerangka hampir semua alat baris perintah yang pernah kamu pakai.",
                    "",
                    "KODE KELUAR: satu angka yang dibaca seluruh sistem",
                    "return 0 di akhir main bukan formalitas. Angka itu diserahkan ke sistem operasi",
                    "sebagai laporan sesingkat mungkin: berhasil atau tidak.",
                    "",
                    "  0          BERHASIL. Hanya satu angka yang berarti sukses.",
                    "  selain 0   GAGAL. 1 untuk 'gagal biasa'; program besar memberi arti khusus tiap",
                    "             angka (grep memakai 1 untuk 'tidak ketemu', 2 untuk 'ada error').",
                    "",
                    "Dua cara mengembalikannya:",
                    "  - Dari main    : return 0;  atau  return 1;",
                    "  - Dari fungsi MANA PUN, sedalam apa pun tumpukan panggilannya:",
                    "    exit(EXIT_SUCCESS) / exit(EXIT_FAILURE) dari <stdlib.h>. exit() menghentikan",
                    "    SELURUH program saat itu juga - ia tidak pernah kembali ke pemanggilnya - tapi",
                    "    tetap menyiram buffer stdout dan menutup berkas yang terbuka lebih dulu.",
                    "    EXIT_SUCCESS bernilai 0, EXIT_FAILURE bernilai 1; namanya lebih jelas dibaca.",
                    "",
                    "Melihat kode keluar perintah terakhir di shell:",
                    "  ./tampil catatan.txt",
                    "  echo $?          -> 0 kalau berhasil, 1 kalau gagal",
                    "",
                    "Dan inilah yang membuat rantai perintah bekerja:",
                    "  gcc tampil.c -o tampil && ./tampil catatan.txt   # kanan jalan HANYA kalau kiri 0",
                    "  ./tampil catatan.txt || echo \"gagal\"             # kanan jalan kalau kiri BUKAN 0",
                    "Shell script, Makefile, dan seluruh CI bertumpu pada satu angka ini. Program yang",
                    "selalu return 0 walau gagal membuat rantai itu terus berjalan di atas hasil rusak -",
                    "dan itu jauh lebih berbahaya daripada berhenti dengan pesan galat.",
                    "",
                    "Dua jebakan terakhir:",
                    "  - Hanya 8 bit terendah yang sampai ke shell. return 256 terbaca 0 (dianggap",
                    "    SUKSES!), return -1 terbaca 255. Pakai angka 0-125 saja; 126 ke atas sudah",
                    "    dipakai shell sendiri untuk 'tidak bisa dijalankan' dan 'dihentikan sinyal'.",
                    "  - Sejak C99, lupa menulis return di main dianggap return 0. Tetap tulis saja",
                    "    supaya niatnya terbaca - dan ingat di fungsi SELAIN main, lupa return tetap bug.",
                ],
            },
        ],
    },
    {
        "title": "24. I/O Tingkat Karakter & Berkas Biner",
        "sections": [
            {
                "body": [
                    "Materi File I/O membaca berkas per BARIS: fgets() untuk mengambil, fprintf()",
                    "untuk menulis. Di bawah lapisan itu ada yang lebih halus lagi: SATU KARAKTER",
                    "satu langkah. Ini gaya I/O paling tua di C, dan sampai hari ini bentuk",
                    "dasar hampir semua alat baris perintah (wc, grep, tr) serta setiap",
                    "lexer/parser bahasa pemrograman - semuanya pada akhirnya cuma loop yang",
                    "mengambil karakter berikutnya.",
                    "",
                    "Enam fungsi, semuanya dari <stdio.h>:",
                    "  getchar()      -> baca SATU karakter dari stdin (keyboard atau pipa)",
                    "  putchar(c)     -> tulis SATU karakter ke layar",
                    "  fgetc(fp)      -> baca SATU karakter dari berkas fp",
                    "  fputc(c, fp)   -> tulis SATU karakter ke berkas fp",
                    "  puts(s)        -> tulis string ke layar, MENAMBAH \\n sendiri",
                    "  fputs(s, fp)   -> tulis string ke berkas, TIDAK menambah \\n",
                    "",
                    "Perhatikan pasangan terakhir: puts MENAMBAH baris baru, fputs TIDAK. Beda",
                    "kecil ini bukan salah ketik di dokumentasi, memang begitu aturannya, dan",
                    "hampir semua orang tertipu olehnya setidaknya sekali.",
                    "",
                    "EOF ('end of file') adalah makro dari <stdio.h> yang bernilai NEGATIF",
                    "(hampir selalu -1). Ia BUKAN karakter yang tersimpan di dalam berkas -",
                    "ia nilai khusus yang dikembalikan saat sudah tidak ada lagi yang bisa",
                    "dibaca. Karena itu penampungnya WAJIB int, JANGAN char:",
                    "",
                    "  int  c;   // BENAR: muat 256 nilai byte DITAMBAH satu nilai EOF",
                    "  char c;   // SALAH: cuma muat 256 nilai, tidak ada ruang untuk EOF",
                    "",
                    "Akibat memakai 'char c' berbeda-beda tergantung mesinnya, dan dua-duanya",
                    "menyakitkan:",
                    "  - char bertanda (PC x86 biasa): byte 0xFF terbaca sebagai -1, sama",
                    "    persis dengan EOF -> loop BERHENTI di tengah berkas, diam-diam.",
                    "  - char tak bertanda (ARM di Linux: Raspberry Pi, HP Android, server ARM):",
                    "    nilainya tak pernah negatif -> perbandingan != EOF SELALU benar",
                    "    -> loop TIDAK PERNAH berhenti.",
                    "Di PC biasa gcc -Wall -Wextra tidak mengeluh sedikit pun soal ini; di mesin",
                    "char tak bertanda barulah keluar peringatan \"comparison is always true\".",
                    "",
                    "Idiom bakunya - kamu akan melihat baris ini seumur hidup:",
                    "",
                    "  int c;",
                    "  while ((c = getchar()) != EOF) {",
                    "      putchar(c);",
                    "  }",
                    "",
                    "Bacanya dari dalam ke luar: ambil satu karakter, SIMPAN ke c, baru",
                    "bandingkan c dengan EOF. Kurung dalam di sekitar (c = getchar()) tidak",
                    "boleh dihapus, karena != berprioritas LEBIH TINGGI daripada = :",
                    "",
                    "  while (c = getchar() != EOF)   // dibaca C sebagai: c = (getchar() != EOF)",
                    "  // c jadi berisi 1 atau 0. Karakternya sendiri hilang, tidak pernah disimpan.",
                    "",
                    "Saudara dekatnya: kadang kamu terlanjur membaca satu karakter yang ternyata",
                    "bukan jatahmu - misalnya saat mengumpulkan digit angka, kamu baru tahu",
                    "angkanya habis setelah menelan huruf sesudahnya. ungetc(c, stdin)",
                    "MENGEMBALIKAN karakter itu ke antrean supaya pembaca berikutnya menemukannya",
                    "lagi. Yang dijamin standar cuma SATU karakter pushback, jangan menumpuknya.",
                    "",
                    "SISA NEWLINE SETELAH scanf - ini sebab pasti dari 'program melompati",
                    "input', keluhan yang sudah disebut di materi Input & Output tanpa pernah",
                    "diberi jalan keluarnya. scanf(\"%d\", &n) berhenti TEPAT di depan Enter yang",
                    "kamu tekan; karakter '\\n' itu ditinggal begitu saja di dalam buffer. fgets()",
                    "berikutnya langsung menemukan '\\n' tadi, menganggapnya sebuah baris kosong",
                    "yang sudah selesai, dan pulang tanpa menunggumu mengetik apa pun. Programnya",
                    "tidak melompat - ia justru membaca sesuatu yang kamu tidak sadar sudah ada",
                    "di sana.",
                    "",
                    "Obatnya: telan sisa baris itu sampai habis sebelum membaca yang berikut.",
                    "",
                    "  int n, c;",
                    "  scanf(\"%d\", &n);",
                    "  while ((c = getchar()) != '\\n' && c != EOF)",
                    "      ;                      // titik koma = badan loop KOSONG, disengaja",
                    "  fgets(nama, sizeof nama, stdin);   // baru bersih",
                    "",
                    "Syarat '&& c != EOF' bukan hiasan: kalau masukannya habis tanpa Enter",
                    "terakhir (biasa terjadi saat input dipipa dari berkas), tanpa syarat itu",
                    "loopnya menunggu '\\n' yang tidak akan pernah datang.",
                ],
            },
            {
                "heading": "Contoh utuh: membaca berkas karakter per karakter",
                "code": """#include <stdio.h>

int main(void) {
    // Langkah 1: buat dulu satu berkas teks supaya ada yang bisa dibaca.
    FILE *tulis = fopen("puisi.txt", "w");
    if (tulis == NULL) {
        printf("Gagal membuka berkas untuk menulis!\\n");
        return 1;
    }
    fputs("aku belajar C\\n", tulis);   // fputs TIDAK menambah \\n sendiri
    fputs("satu karakter\\n", tulis);   // (beda dari puts() yang menambahkannya)
    fputc('!', tulis);                 // fputc menulis SATU karakter saja
    fputc('\\n', tulis);
    fclose(tulis);

    // Langkah 2: baca kembali KARAKTER PER KARAKTER sampai bertemu EOF.
    FILE *baca = fopen("puisi.txt", "r");
    if (baca == NULL) {
        printf("Gagal membuka berkas untuk membaca!\\n");
        return 1;
    }

    int c;                    // WAJIB int -- EOF tidak muat di dalam char
    long karakter = 0, baris = 0, diubah = 0;

    while ((c = fgetc(baca)) != EOF) {   // kurung dalam WAJIB
        karakter++;
        if (c == '\\n') {
            baris++;
        }
        if (c >= 'a' && c <= 'z') {
            putchar(c - 'a' + 'A');      // cetak versi huruf besarnya
            diubah++;
        } else {
            putchar(c);                  // selain huruf kecil, salin apa adanya
        }
    }
    fclose(baca);

    puts("---");                         // puts() menambah \\n sendiri
    printf("%ld karakter, %ld baris, %ld huruf dibesarkan\\n",
           karakter, baris, diubah);
    return 0;
}""",
            },
            {
                "body": [
                    "Sampai sini semua berkas kita berkas TEKS. Ada mode kedua: BINER. Yang",
                    "membedakannya cuma satu huruf tambahan di string mode:",
                    "",
                    "  \"rb\"    -> baca biner (berkas HARUS sudah ada, kalau tidak NULL)",
                    "  \"wb\"    -> tulis biner (buat baru, atau KOSONGKAN yang lama)",
                    "  \"ab\"    -> tambah biner di ujung (isi lama aman)",
                    "  \"r+b\"   -> baca DAN tulis berkas yang sudah ada, isi lama tidak dihapus",
                    "  \"w+b\"   -> baca & tulis juga, tapi isinya dikosongkan lebih dulu",
                    "",
                    "Huruf b boleh di ujung: \"rb+\" sama sahnya dengan \"r+b\". Khusus mode",
                    "ber-'+', di antara satu operasi baca dan satu operasi tulis kamu WAJIB",
                    "menyelipkan fseek/rewind/fflush; melanggar aturan ini hasilnya tidak",
                    "terdefinisi, dan biasanya berupa data yang tertulis di tempat salah.",
                    "",
                    "Apa bedanya dengan mode teks? Di Linux dan macOS: TIDAK ADA SAMA SEKALI,",
                    "byte yang kamu tulis persis byte yang tersimpan. Di Windows bedanya nyata:",
                    "  - Mode teks MENERJEMAHKAN: tiap '\\n' yang kamu tulis jadi dua byte",
                    "    0x0D 0x0A di berkas, lalu diterjemahkan balik saat dibaca.",
                    "  - Mode teks juga menganggap byte 0x1A (Ctrl-Z) sebagai akhir berkas.",
                    "",
                    "Untuk teks itu justru membantu. Untuk data biner itu MERUSAK: sebuah int",
                    "bernilai 10 mengandung byte 0x0A, mode teks menyisipkan 0x0D di depannya,",
                    "berkasnya membengkak, seluruh record sesudahnya bergeser, dan fread",
                    "membaca sampah. Bug ini tidak akan pernah muncul di mesinmu kalau kamu",
                    "pakai Linux - ia muncul di komputer orang lain. Karena itu tulis 'b'",
                    "untuk data biner walaupun di tempatmu tidak ada bedanya.",
                    "",
                    "Menyimpan struct APA ADANYA, tanpa diubah jadi teks lebih dulu:",
                    "",
                    "  fwrite(&m, sizeof m, 1, fp);   // tulis 1 item sebesar sizeof m",
                    "  fread(&m, sizeof m, 1, fp);    // baca 1 item sebesar sizeof m",
                    "",
                    "Urutan argumennya: alamat data, UKURAN satu item, JUMLAH item, berkas.",
                    "Nilai kembalinya adalah jumlah ITEM yang berhasil, BUKAN jumlah byte.",
                    "Jadi pemeriksaan yang benar adalah '== 1' (atau '== n'), bukan '> 0', dan",
                    "sama sekali bukan '== sizeof m'. fread yang mengembalikan kurang dari yang",
                    "diminta berarti berkasnya habis ATAU ada galat - dua hal berbeda yang",
                    "dibedakan belakangan oleh feof/ferror.",
                    "",
                    "(sizeof m dan sizeof(Mahasiswa) sama saja; kurung cuma wajib kalau yang",
                    "diukur nama TIPE, bukan nama variabel.)",
                    "",
                    "Karena tiap record ukurannya SAMA PERSIS, berkas biner bisa dibaca acak:",
                    "lompat langsung ke record ke-i tanpa membaca yang sebelum-sebelumnya.",
                    "",
                    "  fseek(fp, offset, SEEK_SET)  -> offset dihitung dari AWAL berkas",
                    "  fseek(fp, offset, SEEK_CUR)  -> dari posisi sekarang (boleh negatif)",
                    "  fseek(fp, offset, SEEK_END)  -> dari UJUNG berkas (0 = tepat di ujung)",
                    "  ftell(fp)                    -> posisi sekarang dalam byte, bertipe long",
                    "  rewind(fp)                   -> balik ke posisi 0 sekaligus menghapus",
                    "                                  penanda galat dan EOF",
                    "",
                    "  fseek(fp, i * (long)sizeof(Mahasiswa), SEEK_SET);   // ke record ke-i",
                    "",
                    "Ukuran berkas juga didapat dari pasangan ini - lompat ke ujung, lalu",
                    "tanya posisinya:",
                    "  fseek(fp, 0, SEEK_END);",
                    "  long ukuran = ftell(fp);",
                    "  rewind(fp);",
                    "Cara ini sah untuk berkas BINER. Pada berkas TEKS di Windows angkanya",
                    "bisa tidak sama dengan jumlah karakter yang nanti kamu baca, gara-gara",
                    "penerjemahan \\r\\n tadi.",
                    "",
                    "Satu lagi yang sering menolong: fseek MENGHAPUS penanda EOF. Setelah",
                    "loop baca selesai kamu boleh langsung fseek dan membaca lagi, tanpa",
                    "menutup dan membuka ulang berkasnya.",
                ],
            },
            {
                "heading": "Contoh utuh: menyimpan array of struct ke berkas biner",
                "code": """#include <stdio.h>

typedef struct {
    char   nama[20];
    int    umur;
    double ipk;
} Mahasiswa;

int main(void) {
    Mahasiswa daftar[3] = {
        {"Andi",  20, 3.50},
        {"Budi",  22, 3.20},
        {"Citra", 21, 3.85}
    };

    // ---- MENYIMPAN: mode "wb" = write binary -------------------------------
    FILE *fp = fopen("mahasiswa.dat", "wb");
    if (fp == NULL) {
        printf("Gagal membuka mahasiswa.dat untuk menulis!\\n");
        return 1;
    }
    size_t ditulis = fwrite(daftar, sizeof(Mahasiswa), 3, fp);
    printf("fwrite mengembalikan %zu (jumlah ITEM, bukan byte)\\n", ditulis);
    fclose(fp);

    // ---- MEMBACA KEMBALI: mode "rb" = read binary --------------------------
    fp = fopen("mahasiswa.dat", "rb");
    if (fp == NULL) {
        printf("Gagal membuka mahasiswa.dat untuk membaca!\\n");
        return 1;
    }

    fseek(fp, 0, SEEK_END);            // lompat ke ujung berkas
    long ukuran = ftell(fp);           // posisi di ujung = ukuran berkas
    rewind(fp);                        // balik lagi ke posisi 0
    printf("Ukuran berkas %ld byte, satu record %ld byte\\n",
           ukuran, (long)sizeof(Mahasiswa));

    Mahasiswa m;
    while (fread(&m, sizeof m, 1, fp) == 1) {   // == 1: satu ITEM berhasil dibaca
        printf("  %-6s %d thn  IPK %.2f\\n", m.nama, m.umur, m.ipk);
    }
    if (ferror(fp)) {                  // dicek DULUAN: berhenti karena rusak?
        printf("Berhenti karena GALAT baca, bukan karena habis.\\n");
    } else if (feof(fp)) {
        printf("Berhenti karena sampai ujung berkas.\\n");
    }

    // ---- AKSES ACAK: langsung ke record indeks 2 ---------------------------
    fseek(fp, 2 * (long)sizeof(Mahasiswa), SEEK_SET);  // fseek menghapus tanda EOF
    if (fread(&m, sizeof m, 1, fp) == 1) {
        printf("Lompat ke record indeks 2: %s (ipk %.2f)\\n", m.nama, m.ipk);
    }
    fclose(fp);
    return 0;
}""",
            },
            {
                "body": [
                    "Berkas mahasiswa.dat itu tidak bisa dibuka dengan editor teks. Diintip",
                    "dengan 'hexdump -C mahasiswa.dat' di mesin x86-64, 32 byte pertamanya",
                    "(record Andi) terlihat begini:",
                    "",
                    "  00000000  41 6e 64 69 00 00 00 00  00 00 00 00 00 00 00 00  |Andi............|",
                    "  00000010  00 00 00 00 14 00 00 00  00 00 00 00 00 00 0c 40  |...............@|",
                    "",
                    "20 byte pertama array nama (\"Andi\" lalu nol semua), byte ke-20 sampai",
                    "ke-23 adalah umur: 14 heksa = 20 desimal, tersimpan TERBALIK sebagai",
                    "14 00 00 00, lalu 8 byte terakhir adalah double 3.5. Tidak ada koma,",
                    "tidak ada kutip, tidak ada apa pun yang menjelaskan dirinya sendiri.",
                    "",
                    "PERINGATAN PORTABILITAS - berkas biner pada dasarnya FOTO ISI MEMORI",
                    "mesinmu, jadi ia mewarisi semua kebiasaan lokal mesin itu:",
                    "  - Padding: compiler menyisipkan byte kosong di antara field agar tiap",
                    "    field jatuh di alamat yang rapi (dibahas di materi Struct Lanjutan).",
                    "    Byte kosong itu ikut tertulis, dan compiler lain boleh menaruhnya",
                    "    di tempat berbeda.",
                    "  - Endianness: mesin x86 dan ARM menyimpan int 20 sebagai 14 00 00 00,",
                    "    mesin big-endian menyimpannya 00 00 00 14. Angka yang sama, urutan",
                    "    byte terbalik, hasil bacanya kacau total.",
                    "  - Ukuran tipe: long 8 byte di Linux 64-bit tapi 4 byte di Windows",
                    "    64-bit. Record-nya langsung beda ukuran.",
                    "  - Pointer: struct berisi char * menyimpan ALAMAT, bukan teks yang",
                    "    ditunjuknya. Dibaca ulang di program lain, alamat itu tidak berarti",
                    "    apa-apa - dan mengikutinya berujung segfault.",
                    "",
                    "Kesimpulan praktisnya: berkas biner buatan sendiri bagus untuk data yang",
                    "dipakai program yang SAMA di mesin yang SAMA - cache, save game, simpanan",
                    "sementara. Begitu datanya harus dibaca mesin lain, bahasa lain, atau versi",
                    "programmu berikutnya yang struct-nya sudah berubah, pakailah format teks",
                    "(CSV, JSON) atau format biner yang aturannya ditulis eksplisit byte per",
                    "byte, bukan sekadar menumpahkan isi struct.",
                    "",
                    "BUG KLASIK - jangan pernah menulis while (!feof(fp)):",
                    "",
                    "  while (!feof(fp)) {                    // SALAH",
                    "      fgets(baris, sizeof baris, fp);",
                    "      printf(\"%s\", baris);",
                    "  }",
                    "",
                    "feof() tidak meramal apa pun. Ia baru bernilai benar SETELAH ada satu",
                    "pembacaan yang gagal karena berkas habis. Di putaran terakhir feof masih",
                    "0, loop masuk sekali lagi, fgets gagal, isi 'baris' TIDAK BERUBAH, dan",
                    "baris terakhir tercetak DUA KALI. Inilah asal usul keluhan 'kenapa baris",
                    "terakhirnya dobel'.",
                    "",
                    "Yang benar: kondisi loopnya adalah nilai kembali fungsi bacanya sendiri.",
                    "  while (fgets(baris, sizeof baris, fp) != NULL) { ... }",
                    "  while (fread(&m, sizeof m, 1, fp) == 1)         { ... }",
                    "  while ((c = fgetc(fp)) != EOF)                  { ... }",
                    "",
                    "feof dan ferror tetap berguna - SESUDAH loop, untuk menjawab 'berhenti",
                    "karena habis, atau karena rusak?'. Periksa ferror(fp) lebih dulu: berkas",
                    "yang gagal dibaca di tengah jalan juga menghentikan loop, dan diam-diam",
                    "menganggapnya 'sudah selesai' adalah cara kehilangan data tanpa sadar.",
                    "clearerr(fp) menghapus kedua penanda itu kalau kamu memang mau mencoba",
                    "membaca lagi.",
                ],
            },
        ],
    },
    {
        "title": "25. Menangani Kegagalan: errno, perror, assert & goto cleanup",
        "sections": [
            {
                "body": [
                    "Sepanjang kurikulum ini kamu sudah menulis baris yang sama puluhan kali:",
                    "",
                    "  if (fp == NULL) { printf(\"Gagal membuka file!\\n\"); return 1; }",
                    "",
                    "Itu tidak salah, tapi bukan begitu cara kode C sungguhan menulisnya. Buka Git, SQLite,",
                    "atau kernel Linux - tiga proyek yang materi Roadmap sarankan untuk dibaca - dan baris",
                    "pertama penanganan galatnya hampir selalu memuat empat hal yang belum pernah kamu lihat:",
                    "errno, perror, exit, dan goto. Materi ini menutup jarak itu.",
                    "",
                    "KENAPA C TIDAK PUNYA EXCEPTION SAMA SEKALI",
                    "Java punya try/catch, Python punya raise/except. C tidak punya satu pun: tidak ada throw,",
                    "tidak ada catch, tidak ada finally. Itu bukan kelalaian, tapi keputusan. Exception butuh",
                    "mesin yang membongkar tumpukan panggilan saat program berjalan, dan C dirancang untuk",
                    "tempat yang tidak punya mesin seperti itu - kernel, driver, dan mikrokontroler.",
                    "",
                    "Akibatnya cuma satu, tapi besar: SATU-SATUNYA cara sebuah fungsi C melapor gagal adalah",
                    "lewat nilai kembalinya. Kalau kamu tidak memeriksa nilai itu, kegagalannya lenyap tanpa",
                    "jejak dan program lanjut berjalan di atas data rusak. Tidak akan ada yang berteriak.",
                    "",
                    "Konvensinya sudah baku, dan hampir seluruh pustaka C memakainya:",
                    "",
                    "  Yang dikembalikan    Penanda GAGAL       Contoh fungsinya",
                    "  pointer              NULL                malloc, calloc, fopen, fgets, strchr",
                    "  int kode status      -1                  open, read, write, remove, fseek",
                    "  int jumlah item      kurang dari yang    fread/fwrite (jumlah item), scanf (jumlah",
                    "                       diminta             field yang berhasil terbaca)",
                    "  int 0 = sukses       apa pun selain 0    fclose, dan mayoritas API pustaka",
                    "",
                    "Perhatikan baris terakhir: di C, 0 justru berarti BERHASIL - kebalikan dari kebiasaan",
                    "boolean di bahasa lain. Ini jebakan yang sering memakan korban: if (fclose(fp)) { ... }",
                    "menjalankan isinya saat fclose GAGAL, bukan saat berhasil.",
                    "",
                    "ERRNO: SATU-SATUNYA KOTAK PESAN YANG ADA",
                    "Nilai kembali cuma sanggup bilang \"gagal\". Ia tidak bilang KENAPA. fopen mengembalikan",
                    "NULL entah karena berkasnya tidak ada, karena izinnya kurang, atau karena programmu",
                    "kehabisan jatah berkas terbuka - tiga masalah yang butuh tiga tindakan berbeda.",
                    "",
                    "Alasannya dititipkan di errno dari <errno.h>: nilai yang DIISI pustaka setiap kali sebuah",
                    "panggilan gagal. Bentuknya terlihat seperti variabel int global, tapi sebenarnya makro",
                    "yang menunjuk ke salinan milik tiap thread - itu sebabnya errno tetap aman di program",
                    "yang berjalan bercabang.",
                    "",
                    "Tiga aturan; melanggar satu saja membuat pesan galatmu berbohong:",
                    "  1. BACA SEGERA. Panggilan pustaka apa pun sesudahnya - termasuk printf - boleh menimpa",
                    "     errno. Kalau pembacaannya harus ditunda, salin dulu: int simpan = errno;",
                    "  2. Baca HANYA setelah nilai kembalinya menyatakan gagal. Panggilan yang BERHASIL pun",
                    "     boleh mengubah errno; standar cuma menjanjikan errno tidak pernah di-nol-kan sendiri.",
                    "  3. Kalau kamu sendiri yang mau mengandalkan errno (misalnya untuk strtol), setel",
                    "     errno = 0 lebih dulu - tidak ada yang membersihkannya untukmu.",
                    "",
                    "Mengubah angka errno jadi kalimat manusia - dua fungsi, dan keduanya sudah kamu miliki:",
                    "  perror(\"fopen\")    cetak ke STDERR: \"fopen: No such file or directory\". Teks dalam",
                    "                     kurung itu label buatanmu; bagian setelah titik dua datang dari",
                    "                     errno. Label paling berguna kalau diisi nama berkas yang gagal.",
                    "  strerror(errno)    kembalikan kalimat itu sebagai string, supaya bisa kamu rangkai",
                    "                     sendiri: fprintf(stderr, \"%s: %s\\n\", nama, strerror(errno));",
                    "                     Fungsi ini dari <string.h>, bukan <errno.h>.",
                    "",
                    "Nama galat yang paling sering muncul (semuanya makro dari <errno.h>):",
                    "  ENOENT   No such file or directory   nama berkas/foldernya salah ketik atau tak ada",
                    "  EACCES   Permission denied           berkasnya ADA, tapi kamu tidak berhak membukanya",
                    "  ENOMEM   Cannot allocate memory      malloc kehabisan memori",
                    "  EEXIST   File exists                 membuat sesuatu yang sudah ada di sana",
                    "  EINVAL   Invalid argument            argumen yang kamu kirim tidak masuk akal",
                    "",
                    "Bandingkan errno dengan NAMANYA - if (errno == ENOENT) - jangan dengan angkanya. Angka",
                    "di balik nama itu berbeda antar sistem operasi; namanya tidak.",
                ],
            },
            {
                "heading": "Melihat errno bekerja, lalu melihat errno berbohong",
                "code": """#include <errno.h>
#include <stdio.h>
#include <string.h>

int main(void) {
    errno = 0;                    // tidak ada yang membersihkan errno selain kamu sendiri

    FILE *fp = fopen("berkas-yang-tidak-ada.txt", "r");
    if (fp == NULL) {             // periksa NILAI KEMBALI dulu, baru errno
        int simpan = errno;       // AMBIL SEGERA, sebelum fungsi apa pun dipanggil

        perror("fopen");          // ke stderr: "fopen: <penjelasan dari errno>"
        fprintf(stderr, "errno = %d, strerror = %s\\n", simpan, strerror(simpan));

        if (simpan == ENOENT) {                 // bandingkan NAMA, bukan angka
            fprintf(stderr, "ENOENT: berkasnya memang tidak ada.\\n");
        } else if (simpan == EACCES) {
            fprintf(stderr, "EACCES: berkasnya ada, tapi izinnya tidak cukup.\\n");
        }
    }

    // Sekarang panggilan yang BERHASIL. Perhatikan errno TIDAK dikembalikan ke 0.
    FILE *ok = fopen("coba-errno.txt", "w");
    if (ok == NULL) {
        perror("fopen coba-errno.txt");
        return 1;
    }
    fputs("berhasil\\n", ok);
    fclose(ok);

    printf("fopen kedua BERHASIL, tapi errno sekarang bernilai %d.\\n", errno);
    printf("Angka itu tidak berarti apa-apa - tidak ada yang gagal.\\n");
    return 0;
}""",
            },
            {
                "body": [
                    "Kompilasi dan jalankan. Keluarannya kira-kira begini:",
                    "",
                    "  fopen: No such file or directory",
                    "  errno = 2, strerror = No such file or directory",
                    "  ENOENT: berkasnya memang tidak ada.",
                    "  fopen kedua BERHASIL, tapi errno sekarang bernilai 22.",
                    "  Angka itu tidak berarti apa-apa - tidak ada yang gagal.",
                    "",
                    "Dua baris terakhir itu inti pelajarannya. Tidak ada yang gagal, tapi errno berubah dari 2",
                    "jadi 22 karena pustaka memakainya untuk urusan internal. Di mesinmu angkanya bisa lain -",
                    "dan justru itu buktinya: errno yang dibaca tanpa memeriksa nilai kembali lebih dulu bukan",
                    "informasi, melainkan tebakan. Tiga baris pertama muncul di stderr dan dua terakhir di",
                    "stdout, jadi urutannya bisa terlihat teracak kalau keluarannya dialihkan ke berkas -",
                    "sebabnya dijelaskan di materi Program & Sistem.",
                    "",
                    "POLA YANG DIPAKAI KODE NYATA",
                    "Satukan errno dengan stderr, exit, dan EXIT_FAILURE dari materi Program & Sistem, dan",
                    "pola lama dari materi Dynamic Memory Allocation dan File I/O berubah bentuk:",
                    "",
                    "  // yang selama ini kamu tulis",
                    "  FILE *fp = fopen(nama, \"r\");",
                    "  if (fp == NULL) { printf(\"Gagal membuka file!\\n\"); return 1; }",
                    "",
                    "  // yang ditulis kode C sungguhan",
                    "  FILE *fp = fopen(nama, \"r\");",
                    "  if (fp == NULL) { perror(nama); exit(EXIT_FAILURE); }",
                    "",
                    "Tiga perbaikan sekaligus, dan tak satu pun kosmetik:",
                    "  - perror menulis ke stderr, jadi keluhannya tidak ikut tertelan saat hasil program",
                    "    dialihkan ke berkas, dan tidak mengotori data yang sedang diolah program lain.",
                    "  - Pesannya menyebut PENYEBAB dan NAMA BERKASNYA. Yang membacanya langsung tahu apakah",
                    "    ia salah ketik nama atau kurang izin - dua hal yang \"Gagal membuka file!\" sembunyikan.",
                    "  - exit(EXIT_FAILURE) sah dipanggil dari fungsi mana pun; return 1 cuma berarti di main.",
                    "",
                    "Tapi exit() punya satu bahaya yang belum disebut: ia berhenti SAAT ITU JUGA. Kalau di",
                    "atasnya sudah ada malloc yang belum di-free atau berkas yang belum ditutup, tidak ada",
                    "kesempatan lagi membereskannya. Untuk program kecil sistem operasi memang membersihkan",
                    "sisanya, tapi di dalam FUNGSI yang dipanggil berulang - server, parser, pustaka - exit",
                    "adalah pilihan yang salah. Fungsi harus MELAPOR gagal, bukan membunuh seluruh program.",
                    "Di situlah goto masuk.",
                    "",
                    "GOTO: SINTAKSNYA DULU",
                    "  goto nama_label;       // lompat ke sana",
                    "  nama_label:            // label = sebuah nama diikuti titik dua",
                    "      pernyataan;        // label harus diikuti sebuah pernyataan",
                    "Labelnya cuma berlaku di dalam SATU fungsi. goto tidak bisa melompat ke fungsi lain.",
                    "",
                    "Reputasi buruk goto itu pantas. Dipakai melompat sembarangan - mundur ke atas, masuk ke",
                    "tengah loop, keluar-masuk blok - alur programnya jadi mustahil dilacak: kamu kehilangan",
                    "kemampuan menjawab \"bagaimana eksekusi bisa sampai di baris ini\" dengan membaca dari atas",
                    "ke bawah. Untuk perulangan dan percabangan, for/while/if/switch selalu lebih jelas, dan",
                    "tidak pernah ada alasan memakai goto di sana.",
                    "",
                    "KECUALI SATU BENTUK: goto cleanup",
                    "Bayangkan fungsi yang malloc dua kali lalu fopen sekali, dan fopen-nya gagal. Dua buffer",
                    "sudah terlanjur ada dan wajib dibebaskan sebelum keluar. Tanpa goto ada dua jalan, dan",
                    "keduanya buruk:",
                    "  - Salin baris free di setiap titik keluar. Lima titik keluar berarti lima salinan, dan",
                    "    satu saja yang lupa disalin jadi memory leak yang cuma muncul saat sedang error -",
                    "    yaitu justru jalur yang paling jarang diuji orang.",
                    "  - Bersarangkan if sedalam jumlah kegagalannya. Kodenya melenceng makin ke kanan dan",
                    "    bagian yang benar-benar bekerja tenggelam di dasar tumpukan kurawal.",
                    "",
                    "C tidak punya try/finally seperti Java dan tidak punya destructor seperti C++, jadi tidak",
                    "ada mekanisme lain yang membereskan otomatis. Maka lahir satu-satunya goto yang dipuji",
                    "orang: semua jalur gagal melompat ke TANGGA LABEL di ujung fungsi, masing-masing masuk di",
                    "anak tangga yang sesuai dengan seberapa jauh ia sempat berhasil.",
                    "",
                    "Empat aturan supaya tangganya benar:",
                    "  1. Deklarasikan semua sumber daya di ATAS fungsi dan isi NULL, supaya label yang",
                    "     terlewati tetap bekerja pada nilai yang jelas.",
                    "  2. Urutan label KEBALIKAN dari urutan pembuatan: yang terakhir dibuat, pertama dibereskan.",
                    "  3. Lompat ke label yang PERSIS setingkat. Gagal di fopen berarti dua buffer perlu",
                    "     dibebaskan tapi belum ada berkas untuk ditutup - jangan kelebihan, jangan kekurangan.",
                    "  4. Simpan hasilnya di satu variabel status yang DIAWALI GAGAL, dan diubah jadi berhasil",
                    "     hanya di baris terakhir jalur normal. Jalur yang lupa kamu tangani otomatis dilaporkan",
                    "     gagal, bukan diam-diam dianggap berhasil.",
                    "",
                    "Label di bawah ini dinamai Bahasa Indonesia supaya jelas, tapi di kode nyata namanya",
                    "hampir selalu pendek dan berbahasa Inggris: cleanup, cleanup_file, cleanup_buf, err,",
                    "fail, out, done. Jadi kalau nanti kamu melihat goto out; di tengah sebuah fungsi kernel",
                    "Linux atau SQLite, artinya persis sama dengan tangga di bawah - bukan lompatan liar,",
                    "melainkan satu pintu keluar bersama yang membereskan apa pun yang sempat dibuat.",
                ],
            },
            {
                "heading": "Tangga pembersihan: dua malloc, satu fopen, dan jalan keluar yang rapi",
                "code": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Baca baris pertama sebuah berkas, ubah jadi huruf besar, lalu cetak.
// Nilai kembalinya mengikuti konvensi C: 0 kalau berhasil, -1 kalau gagal.
int cetak_huruf_besar(const char *nama, size_t n) {
    char *masuk = NULL;          // semua sumber daya dideklarasikan DI ATAS
    char *keluar = NULL;         // dan diisi NULL, supaya label aman dilewati
    FILE *fp = NULL;
    size_t panjang = 0;
    int status = -1;             // anggap GAGAL sampai terbukti sebaliknya

    masuk = malloc(n);
    if (masuk == NULL) {
        fprintf(stderr, "malloc buffer masuk gagal\\n");
        goto selesai;            // belum ada apa pun yang perlu dibereskan
    }

    keluar = malloc(n);
    if (keluar == NULL) {
        fprintf(stderr, "malloc buffer keluar gagal\\n");
        goto bebaskan_masuk;     // buffer pertama sudah ada -> WAJIB dibebaskan
    }

    fp = fopen(nama, "r");
    if (fp == NULL) {
        perror(nama);            // "hantu.txt: No such file or directory"
        goto bebaskan_keluar;    // dua buffer sudah ada, berkas belum
    }

    if (fgets(masuk, (int) n, fp) == NULL) {
        fprintf(stderr, "%s: tidak ada baris untuk dibaca\\n", nama);
        goto tutup_berkas;       // dua buffer + satu berkas terbuka
    }

    panjang = strlen(masuk);
    for (size_t i = 0; i < panjang; i++) {
        char c = masuk[i];
        keluar[i] = (c >= 'a' && c <= 'z') ? (char) (c - 'a' + 'A') : c;
    }
    keluar[panjang] = '\\0';
    printf("%s", keluar);
    status = 0;                  // HANYA di sini status jadi berhasil

tutup_berkas:                    // tangga: dari yang TERAKHIR dibuat ke yang pertama
    fclose(fp);
bebaskan_keluar:
    free(keluar);
bebaskan_masuk:
    free(masuk);
selesai:
    return status;               // satu titik keluar untuk semua jalur
}

int main(void) {
    FILE *tulis = fopen("data-goto.txt", "w");
    if (tulis == NULL) {
        perror("fopen data-goto.txt");
        return EXIT_FAILURE;
    }
    fputs("halo dari dalam berkas\\n", tulis);
    fclose(tulis);

    if (cetak_huruf_besar("data-goto.txt", 128) != 0) {
        return EXIT_FAILURE;                  // kegagalan yang TIDAK diharapkan
    }

    // Sengaja gagal di tengah jalan: berkasnya tidak ada. Dua malloc sudah
    // terlanjur berhasil, dan tangga label memastikan keduanya tetap di-free.
    if (cetak_huruf_besar("hantu.txt", 128) != 0) {
        fprintf(stderr, "(gagal seperti yang direncanakan, tanpa bocor memori)\\n");
    }
    return EXIT_SUCCESS;
}""",
            },
            {
                "heading": "assert: menyatakan asumsi, bukan memeriksa masukan",
                "body": [
                    "assert(syarat) dari <assert.h> adalah cara MENYATAKAN sesuatu yang menurutmu mustahil",
                    "salah. Kalau ternyata salah, program berhenti saat itu juga sambil mencetak ke stderr:",
                    "",
                    "  assert-menyatakan: assert-menyatakan.c:13: rata_rata: Assertion `n > 0' failed.",
                    "  Aborted (core dumped)",
                    "",
                    "Isinya lengkap tanpa kamu menulis apa pun: nama program, nama berkas, NOMOR BARIS, nama",
                    "fungsi, dan syarat yang dilanggar apa adanya. Kode keluarnya 134 - artinya program",
                    "dihentikan sinyal SIGABRT, bukan berhenti biasa - jadi shell pun tahu ini bukan kegagalan",
                    "normal. Bandingkan dengan printf(\"ada yang aneh\") yang tidak menyebut baris mana pun.",
                    "",
                    "YANG PALING SERING BIKIN TERSANDUNG: assert BISA HILANG TOTAL.",
                    "Program di bawah bisa dikompilasi dua cara, dan hasilnya berbeda jauh:",
                    "  gcc -Wall -g assert-menyatakan.c -o assert-menyatakan",
                    "      -> assert AKTIF. Ini build pengembangan, dan inilah perilaku default gcc.",
                    "  gcc -Wall -DNDEBUG -O2 assert-menyatakan.c -o assert-menyatakan",
                    "      -> setiap assert MENGUAP jadi baris kosong. Ini build rilis.",
                    "NDEBUG (\"no debug\") adalah makro yang dikenali <assert.h>. Hampir semua build rilis",
                    "menyalakannya supaya pemeriksaannya tidak lagi membebani program yang sudah jadi.",
                    "",
                    "Dua akibat yang wajib diingat:",
                    "  1. JANGAN taruh pekerjaan di dalam assert. assert(hapus(nama) == 0) berhenti menghapus",
                    "     apa pun di build rilis, karena seluruh isi kurungnya ikut terhapus. Panggil dulu,",
                    "     simpan hasilnya, baru assert hasilnya.",
                    "  2. JANGAN pakai assert untuk masukan pengguna, isi berkas, atau hasil malloc. Semua itu",
                    "     bisa gagal walaupun kodemu benar - dan di build rilis pemeriksaannya lenyap.",
                    "",
                    "Pembagian tugasnya sederhana begitu dilihat dari sumber masalahnya:",
                    "  assert   untuk BUG PROGRAMMER: \"fungsi ini tidak pernah dipanggil dengan n = 0\".",
                    "           Kalau ia gagal, yang harus diperbaiki adalah KODENYA, bukan masukannya.",
                    "  if       untuk hal yang memang bisa terjadi di dunia nyata: berkas tidak ada, angka",
                    "           di luar jangkauan, malloc mengembalikan NULL. Ini ditangani, bukan di-assert.",
                    "",
                    "_Static_assert(syarat, \"pesan\") memeriksa saat KOMPILASI, bukan saat program berjalan.",
                    "Syaratnya harus bisa dihitung compiler sendiri (sizeof, konstanta, nilai enum). Kalau",
                    "salah, gcc berhenti dengan \"error: static assertion failed: <pesanmu>\" dan programnya",
                    "tidak pernah jadi - jauh lebih baik daripada crash di tangan pengguna. Sejak C23 namanya",
                    "boleh ditulis static_assert saja; di C11 tulis _Static_assert, atau sertakan <assert.h>",
                    "yang menyediakan alias static_assert.",
                    "",
                    "Coba sendiri di program berikut: hapus dua garis miring di baris paling bawah, lalu",
                    "kompilasi DUA KALI. Tanpa -DNDEBUG program berhenti dengan pesan Assertion `n > 0' failed",
                    "dan kode keluar 134. Dengan -DNDEBUG ia jalan terus, membagi dengan nol, mencetak -nan,",
                    "dan keluar dengan kode 0 - gagal diam-diam. Itu gambaran paling jelas kenapa assert bukan",
                    "pengganti if.",
                ],
                "code": """#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

// Diperiksa saat KOMPILASI. Kalau syaratnya salah, gcc menolak membuat
// programnya sama sekali - jadi tidak ada apa pun yang bisa gagal nanti.
_Static_assert(sizeof(int) >= 4, "kode ini menganggap int minimal 4 byte");

// KONTRAK fungsi ini: pemanggil wajib mengirim pointer sah dan n lebih dari 0.
// Melanggarnya adalah BUG DI KODE, bukan kesalahan pengguna.
double rata_rata(const int *data, size_t n) {
    assert(data != NULL);        // asumsi 1: pointernya sah
    assert(n > 0);               // asumsi 2: pembaginya bukan nol

    long jumlah = 0;
    for (size_t i = 0; i < n; i++) {
        jumlah += data[i];
    }
    return (double) jumlah / (double) n;
}

int main(void) {
    int nilai[] = {80, 90, 70, 100};
    size_t total = sizeof(nilai) / sizeof(nilai[0]);

    printf("Rata-rata semua: %.2f\\n", rata_rata(nilai, total));

    // Bayangkan angka ini datang dari pengguna (scanf atau argv). Masukan
    // pengguna diperiksa dengan if, TIDAK PERNAH dengan assert - sebab assert
    // lenyap begitu programnya dikompilasi dengan -DNDEBUG.
    int diminta = 3;
    if (diminta <= 0 || (size_t) diminta > total) {
        fprintf(stderr, "Jumlah harus antara 1 dan %zu.\\n", total);
        return EXIT_FAILURE;
    }
    printf("Rata-rata %d nilai pertama: %.2f\\n",
           diminta, rata_rata(nilai, (size_t) diminta));

    // Hapus dua garis miring di bawah untuk melihat sendiri assert yang gagal.
    // printf("%.2f\\n", rata_rata(nilai, 0));
    return 0;
}""",
            },
        ],
    },
    {
        "title": "26. Preprocessor & Macro",
        "sections": [
            {
                "body": [
                    "Preprocessor adalah tahap SEBELUM kompilasi sungguhan -",
                    "memproses baris yang diawali tanda pagar (#) dengan cara",
                    "'text replacement' (mengganti teks) SEBELUM kode dikompilasi.",
                    "",
                    "#include <file.h>   -> menyertakan isi file header",
                    "  <...>  -> cari di system include path (library standar)",
                    "  \"...\"  -> cari di folder project sendiri (header sendiri)",
                    "",
                    "#define NAMA nilai   -> membuat macro (konstanta/text replacement)",
                    "  #define MAX_SIZE 100",
                    "  int arr[MAX_SIZE];   // preprocessor GANTI jadi: int arr[100];",
                ]
            },
            {
                "heading": "Macro dengan parameter (function-like macro)",
                "code": """#include <stdio.h>

#define PI 3.14159
#define KUADRAT(x) ((x) * (x))       // TANDA KURUNG penting! (hindari bug)
#define MAX(a, b) ((a) > (b) ? (a) : (b))

int main(void) {
    printf("PI = %.5f\\n", PI);
    printf("Kuadrat 5 = %d\\n", KUADRAT(5));        // (5)*(5) = 25
    printf("Max(3, 7) = %d\\n", MAX(3, 7));         // 7

    // KENAPA harus pakai kurung ekstra di macro? Contoh bug tanpa kurung:
    // #define KUADRAT_SALAH(x) x * x
    // KUADRAT_SALAH(2+3)  -> preprocessor ganti jadi: 2+3 * 2+3 = 2+6+3 = 11
    //                        (BUKAN 25 seperti yang diharapkan!)
    // Dengan kurung: ((2+3) * (2+3)) = 25  -> BENAR

    return 0;
}"""
            },
            {
                "body": [
                    "Conditional compilation (kompilasi bersyarat):",
                    "  #ifdef DEBUG",
                    "      printf(\"Mode debug aktif\\n\");",
                    "  #endif",
                    "",
                    "  #ifndef HEADER_NAME     // 'include guard' - MENCEGAH file",
                    "  #define HEADER_NAME     // header di-include LEBIH dari sekali",
                    "  // ... isi header ...",
                    "  #endif",
                    "",
                    "  Alternatif modern (didukung compiler mayoritas):",
                    "  #pragma once   // sama seperti include guard, lebih ringkas",
                    "",
                    "Macro vs const/function biasa:",
                    "  - Macro: text replacement MENTAH, TIDAK type-checked,",
                    "    tidak muncul di debugger, tapi TIDAK ada overhead fungsi.",
                    "  - const/inline function: type-checked, lebih AMAN,",
                    "    DISARANKAN untuk kode modern kecuali alasan khusus.",
                    "",
                    "Dua pengganti macro itu bentuknya begini:",
                    "",
                    "  const int MAX_SIZE = 100;               // pengganti #define nilai",
                    "  static inline int kuadrat(int x) {      // pengganti KUADRAT(x)",
                    "      return x * x;",
                    "  }",
                    "",
                    "Kata kunci inline (baru ada sejak C99) adalah SARAN kepada",
                    "compiler: 'boleh tempelkan isi fungsi ini langsung di tempat",
                    "pemanggilan, tidak usah lompat'. Hasilnya secepat macro, tapi",
                    "argumennya tetap diperiksa tipenya, argumennya tetap dihitung",
                    "SEKALI saja (macro bisa menghitungnya dua kali - MAX(a++, b)",
                    "menaikkan a dua kali), dan gdb tetap bisa memasang breakpoint",
                    "di dalamnya.",
                    "",
                    "Pasangan static inline itulah bentuk yang hampir selalu dipakai",
                    "kalau fungsinya ditaruh di dalam berkas .h - kenapa harus",
                    "static, dan apa yang terjadi kalau tidak, dibahas di materi",
                    "Preprocessor Lanjutan: Kompilasi Bersyarat & Makro Sungguhan.",
                ]
            },
        ],
    },
    {
        "title": "27. Preprocessor Lanjutan: Kompilasi Bersyarat & Makro Sungguhan",
        "sections": [
            {
                "body": [
                    "Materi 16 berhenti di #define, #ifdef, dan include guard. Kode C",
                    "nyata memakai jauh lebih banyak: preprocessor punya percabangan",
                    "PENUH, dan percabangan itu diputuskan saat KOMPILASI - bukan saat",
                    "program berjalan.",
                    "",
                    "  #if <ekspresi>     -> ekspresi ANGKA, dihitung preprocessor",
                    "  #elif <ekspresi>   -> 'else if' versi preprocessor",
                    "  #else",
                    "  #endif             -> WAJIB; tidak ada kurawal yang menutup",
                    "                        blok ini otomatis",
                    "",
                    "Beda #if dan #ifdef - ini sumber salah paham nomor satu:",
                    "",
                    "  #ifdef NAMA        -> benar kalau NAMA pernah di-#define,",
                    "                        isinya apa pun",
                    "  #if defined(NAMA)  -> arti sama, tapi bisa digabung:",
                    "                        #if defined(A) && !defined(B)",
                    "  #if NAMA           -> membaca NILAI-nya; nama yang belum",
                    "                        pernah didefinisikan dianggap 0",
                    "",
                    "  #define AMAN 0",
                    "  #ifdef AMAN   -> MASUK  (namanya memang ada)",
                    "  #if AMAN      -> TIDAK  (nilainya 0)",
                    "",
                    "Dua baris terakhir itu bukan sinonim, dan tidak ada peringatan",
                    "apa pun kalau kamu memilih yang keliru.",
                    "",
                    "Cabang yang kalah bukan sekadar dilewati saat program berjalan -",
                    "ia tidak pernah sampai ke compiler sama sekali. Isinya boleh",
                    "memanggil fungsi Windows yang tidak ada di Linux; selama",
                    "cabangnya tidak terpilih, tidak ada satu pun error.",
                    "",
                    "Nilainya boleh datang dari baris perintah, tanpa menyentuh kode:",
                    "  gcc -DDEBUG program.c -o program     # = #define DEBUG 1",
                    "  gcc -DVERSI=2 program.c -o program   # = #define VERSI 2",
                    "",
                    "Menghentikan kompilasi dengan pesan sendiri:",
                    "  #error \"pesan\"     -> kompilasi BERHENTI, pesanmu yang tercetak",
                    "  #warning \"pesan\"   -> cuma peringatan, kompilasi lanjut",
                    "                        (GCC/Clang; bukan bagian C standar)",
                    "",
                    "Gunanya bukan gaya-gayaan: ia menangkap salah konfigurasi di",
                    "detik pertama, sebelum berubah jadi error linker 200 baris yang",
                    "tidak menyebut sebabnya sama sekali.",
                ],
            },
            {
                "heading": "Blok lintas platform + makro bawaan compiler",
                "code": """#include <stdio.h>

// Cabang di bawah ini dipilih SAAT KOMPILASI. Yang tidak terpilih
// tidak pernah sampai ke compiler - isinya boleh memakai fungsi yang
// tidak ada di sistem ini sekalipun. Blok seperti ini ada di berkas
// pertama hampir semua proyek C.
#if defined(_WIN32)
#define NAMA_OS   "Windows"
#define BERSIHKAN "cls"
#elif defined(__APPLE__)
#define NAMA_OS   "macOS"
#define BERSIHKAN "clear"
#elif defined(__linux__)
#define NAMA_OS   "Linux"
#define BERSIHKAN "clear"
#else
#error "Platform belum didukung - tambahkan cabangnya di sini dulu."
#endif

// Nilai boleh datang dari luar: tambahkan -DVERSI=2 pada perintah gcc,
// dan angka bawaan di bawah ini tidak terpakai sama sekali.
#ifndef VERSI
#define VERSI 1
#endif

int main(void) {
    // Empat makro ini diisi compiler, bukan olehmu.
    printf("Berkas  : %s\\n", __FILE__);   // nama berkas sumbernya
    printf("Baris   : %d\\n", __LINE__);   // nomor baris INI juga
    printf("Fungsi  : %s\\n", __func__);   // nama fungsi tempatnya berada
    printf("OS      : %s\\n", NAMA_OS);
    printf("Bersih  : %s\\n", BERSIHKAN);
    printf("Versi   : %d\\n", VERSI);

#if VERSI >= 2
    printf("Fitur tambahan ikut dikompilasi\\n");
#else
    printf("Mode dasar\\n");
#endif

    // __STDC_VERSION__ = versi standar C-nya. 199901L artinya C99.
#if defined(__STDC_VERSION__) && __STDC_VERSION__ >= 199901L
    printf("Compiler ini C99 ke atas\\n");
#endif

    // Ada juga __DATE__ dan __TIME__ (waktu KOMPILASI, bukan waktu
    // jalan). Sengaja tidak dicetak: hasilnya berubah tiap kompilasi.
    return 0;
}""",
            },
            {
                "body": [
                    "Tiga alat yang HANYA ada di dalam #define, dan tidak berlaku di",
                    "mana pun lagi:",
                    "",
                    "  #x        'stringify' - mengubah ARGUMEN jadi teks apa adanya",
                    "            #define TEKS(x) #x",
                    "            TEKS(1 + 2)  ->  \"1 + 2\"   (teksnya, bukan 3)",
                    "",
                    "  x ## y    'token paste' - menempel dua potong nama jadi SATU",
                    "            #define VAR(n) angka_##n",
                    "            VAR(3)       ->  angka_3",
                    "",
                    "  ...       parameter sebanyak apa pun; di badan makro semuanya",
                    "            diwakili __VA_ARGS__",
                    "            #define LOG(fmt, ...) printf(fmt, __VA_ARGS__)",
                    "",
                    "Kenapa makro yang berisi lebih dari satu pernyataan selalu",
                    "dibungkus do { ... } while (0)? Karena tanpa itu hasilnya rusak",
                    "diam-diam:",
                    "",
                    "  #define BERSIH() a = 0; b = 0;",
                    "  if (rusak) BERSIH();",
                    "",
                    "  Sesudah teksnya diganti:  if (rusak) a = 0; b = 0;",
                    "  -> b = 0 SELALU jalan, di luar if. Tidak error, tidak ada",
                    "     warning, cuma salah.",
                    "",
                    "Kurawal telanjang { a = 0; b = 0; } belum menyelesaikan juga:",
                    "'if (x) { ... };' meninggalkan titik koma nyasar yang mematahkan",
                    "'else' sesudahnya.",
                    "",
                    "do { ... } while (0) menutup dua-duanya sekaligus: isinya jadi",
                    "satu blok, DAN ia sebuah pernyataan yang memang menuntut titik",
                    "koma - jadi LOG(...); ditulis persis seperti pemanggilan fungsi",
                    "biasa. Loop-nya berjalan tepat sekali, lalu dibuang optimizer.",
                ],
            },
            {
                "heading": "Makro logging & pemeriksa buatan sendiri",
                "body": [
                    "Inilah bentuk yang menunggumu di hampir setiap proyek C: satu",
                    "makro LOG dan satu makro semacam assert, dibangun dari lima hal",
                    "di atas sekaligus.",
                    "",
                    "Kalau sebuah makro berperilaku aneh, jangan menebak - LIHAT",
                    "hasil penggantiannya:",
                    "  gcc -E makro-logging.c              # kode SESUDAH preprocessor",
                    "  gcc -E makro-logging.c | tail -40   # bagian bawahnya saja",
                    "",
                    "Keluarannya panjang karena seluruh isi <stdio.h> ikut disalin ke",
                    "situ - memang itu yang dikerjakan #include. Kode tulisanmu ada di",
                    "paling bawah, sudah dalam bentuk jadinya.",
                ],
                "code": """#include <stdio.h>
#include <stdlib.h>

// # mengubah ARGUMEN jadi teks apa adanya.
#define TEKS(x) #x

// ## menempel dua token jadi satu nama baru.
#define BUAT_KUADRAT(nama) int kuadrat_##nama(int n) { return n * n; }

BUAT_KUADRAT(int)   // jadi: int kuadrat_int(int n) { return n * n; }

// ... = argumen sebanyak apa pun, diwakili __VA_ARGS__ di badan makro.
// Pembungkus do { ... } while (0) membuatnya berlaku sebagai SATU
// pernyataan, persis seperti pemanggilan fungsi.
#define LOG(fmt, ...)                                            \\
    do {                                                         \\
        fprintf(stderr, "%s:%d: " fmt "\\n",                      \\
                __FILE__, __LINE__, __VA_ARGS__);                \\
    } while (0)

// #kondisi mencetak ULANG syarat yang gagal sebagai teks - guna '#'.
#define PERIKSA(kondisi)                                         \\
    do {                                                         \\
        if (!(kondisi)) {                                        \\
            fprintf(stderr, "%s:%d: syarat gagal: %s\\n",         \\
                    __FILE__, __LINE__, #kondisi);               \\
            exit(1);                                             \\
        }                                                        \\
    } while (0)

int main(void) {
    int umur = 17;

    printf("%s\\n", TEKS(umur + 1));   // tercetak: umur + 1, bukan 18
    printf("%d\\n", kuadrat_int(6));   // 36

    // if TANPA kurawal pun aman, justru karena do/while tadi.
    if (umur < 18)
        LOG("belum cukup umur (%d)", umur);
    else
        LOG("sudah cukup umur (%d)", umur);

    PERIKSA(umur > 0);
    printf("selesai\\n");
    return 0;
}""",
            },
            {
                "heading": "Kapan makro justru TIDAK dipakai, dan pola static inline",
                "body": [
                    "Makro itu penggantian teks mentah: tidak punya tipe, tidak",
                    "kelihatan di gdb, dan argumennya bisa dievaluasi dua kali -",
                    "MAX(a++, b) menaikkan a dua kali. Jadi sebelum mengetik #define,",
                    "tanya dulu apakah ada bentuk yang lebih aman:",
                    "",
                    "  Sekumpulan angka tetap ->  enum { MAKS = 100, MIN = 1 };",
                    "  Satu konstanta         ->  static const int MAKS = 100;",
                    "  Perhitungan kecil      ->  static inline function (di bawah)",
                    "",
                    "#define tetap tak tergantikan untuk tiga hal: include guard,",
                    "kompilasi bersyarat, dan makro yang MEMANG butuh __FILE__ atau",
                    "__LINE__ milik PEMANGGILNYA. Yang terakhir itu alasan LOG tidak",
                    "bisa jadi fungsi biasa: __LINE__ di dalam sebuah fungsi menunjuk",
                    "baris fungsi itu sendiri - angka yang sama terus, tidak berguna.",
                    "",
                    "Materi 19 bilang .h berisi prototype dan .c berisi isinya.",
                    "static inline adalah pengecualian resminya:",
                    "  inline  -> izin bagi compiler menyalin isi fungsi ke tempat",
                    "             pemanggilan; secepat makro, tapi tetap bertipe",
                    "  static  -> salinannya milik tiap .c sendiri, jadi linker tidak",
                    "             melihat dua nama sama saat header itu di-include",
                    "             oleh lebih dari satu berkas",
                    "",
                    "Keduanya ditulis berpasangan, dan dua kesalahannya sama-sama",
                    "muncul di LINKER - tahap paling akhir, tanpa menunjuk satu baris",
                    "pun di kodemu:",
                    "",
                    "  fungsi biasa di .h, di-include 2 berkas",
                    "      -> multiple definition of 'maks'",
                    "  'inline' ditulis tanpa 'static'",
                    "      -> undefined reference to 'maks'",
                ],
                "code": """/* ===== File: kecil.h ===== */
#ifndef KECIL_H
#define KECIL_H

// Definisi LENGKAP di dalam .h - boleh, ASAL ditandai static inline.
static inline int maks(int a, int b) {
    return a > b ? a : b;
}

#endif

/* ===== File: tampil.c ===== */
#include <stdio.h>
#include "kecil.h"

void tampilkan(void) {
    printf("tampil: %d\\n", maks(3, 9));
}

/* ===== File: main.c ===== */
#include <stdio.h>
#include "kecil.h"

void tampilkan(void);

int main(void) {
    tampilkan();
    printf("main  : %d\\n", maks(10, 4));
    return 0;
}

/* Kompilasi:  gcc main.c tampil.c -o program
   Keluaran :  tampil: 9
               main  : 10                      */""",
            },
        ],
    },
    {
        "title": "28. Function Pointer",
        "sections": [
            {
                "body": [
                    "Function pointer = pointer yang menyimpan ALAMAT sebuah",
                    "FUNGSI, bukan alamat variabel biasa. Ini memungkinkan",
                    "fungsi 'dikirim' sebagai parameter ke fungsi lain - dasar",
                    "dari konsep callback (SEBELUM ada lambda/arrow function).",
                    "",
                    "  Sintaks: tipeKembali (*namaPointer)(tipeParameter);",
                    "",
                    "  int tambah(int a, int b) { return a + b; }",
                    "  int (*fp)(int, int) = tambah;   // fp menunjuk ke fungsi tambah",
                    "  int hasil = fp(3, 4);            // memanggil lewat pointer -> 7",
                ]
            },
            {
                "heading": "Contoh function pointer sebagai callback",
                "code": """#include <stdio.h>

int tambah(int a, int b) { return a + b; }
int kurang(int a, int b) { return a - b; }
int kali(int a, int b)   { return a * b; }

// Fungsi yang MENERIMA function pointer sebagai parameter (callback)
int hitung(int a, int b, int (*operasi)(int, int)) {
    return operasi(a, b);    // panggil fungsi APAPUN yang dikirim
}

int main(void) {
    printf("%d\\n", hitung(10, 5, tambah));   // 15
    printf("%d\\n", hitung(10, 5, kurang));   // 5
    printf("%d\\n", hitung(10, 5, kali));     // 50

    // Array of function pointer - mirip 'dictionary operasi'
    int (*operasiList[3])(int, int) = {tambah, kurang, kali};
    const char *nama[3] = {"tambah", "kurang", "kali"};

    for (int i = 0; i < 3; i++) {
        printf("%s(10, 5) = %d\\n", nama[i], operasiList[i](10, 5));
    }
    return 0;
}"""
            },
            {
                "body": [
                    "Kegunaan nyata function pointer:",
                    "  1. Callback untuk qsort() - fungsi sort bawaan C butuh",
                    "     function pointer 'compare' untuk menentukan urutan.",
                    "  2. Dasar dari konsep 'strategy pattern' di bahasa OOP.",
                    "  3. Membuat tabel dispatch (seperti array operasiList di atas).",
                    "  4. Fondasi konseptual dari lambda/closure di bahasa modern",
                    "     (JavaScript, Python, Java) - semuanya BERAKAR dari ide ini.",
                ]
            },
        ],
    },
    {
        "title": "29. C Generik: void *, qsort & Fungsi Variadic",
        "sections": [
            {
                "body": [
                    "C tidak punya generics, template, atau Object. Yang dipunyainya cuma SATU alat:",
                    "void * - pointer yang tidak tahu, dan tidak peduli, tipe data yang ditunjuknya.",
                    "Begitu kamu mulai membaca kode C orang lain, void * ada di mana-mana:",
                    "",
                    "  void *malloc(size_t n);                        // nilai kembali malloc",
                    "  void *memcpy(void *tujuan, const void *asal, size_t n);",
                    "  void *memset(void *s, int c, size_t n);",
                    "  void  qsort(void *base, size_t n, size_t ukuran,",
                    "              int (*banding)(const void *, const void *));",
                    "  struct Tombol { const char *label; void *data; };   // 'data' titipan pemakai",
                    "",
                    "Kenapa bentuk ini ada: ini satu-satunya cara menulis SATU fungsi yang bekerja",
                    "untuk int, double, dan struct buatanmu sekaligus, tanpa menulisnya tiga kali.",
                    "",
                    "Dua aturan yang tidak bisa ditawar:",
                    "",
                    "  1. void * BOLEH menampung alamat apa pun, dan alamat apa pun boleh masuk ke",
                    "     sana tanpa cast. Informasi tipenya HILANG - bukan disimpan diam-diam.",
                    "",
                    "  2. void * TIDAK boleh di-dereference (*p) dan TIDAK boleh diaritmatikakan",
                    "     (p + 1) sebelum dikembalikan ke tipe aslinya. Compiler tidak tahu satu",
                    "     elemennya berapa byte, jadi tidak ada yang bisa dihitungnya.",
                    "     *p pada void * adalah GALAT keras ('invalid use of void expression').",
                    "     p + 1 ditolak standar; gcc mengizinkannya sebagai perluasan (menganggap",
                    "     void berukuran 1 byte) dan baru mengeluh kalau diberi -Wpedantic.",
                    "",
                    "Arah SEBALIKNYA - void * kembali jadi int * - tidak butuh cast DI C:",
                    "  int *p = malloc(n * sizeof *p);          // sah, dan bentuk yang disarankan",
                    "  int *p = (int *) malloc(n * sizeof *p);  // juga sah, cuma lebih berisik",
                    "Di C++ cast itu WAJIB (g++ menolak yang pertama: 'invalid conversion from",
                    "void* to int*'), dan banyak kode C ditulis agar bisa dikompilasi kedua-duanya.",
                    "Itulah asal-usul (int*) di depan malloc pada materi Dynamic Memory Allocation.",
                    "",
                    "%p adalah satu-satunya format specifier untuk mencetak ALAMAT, dan argumennya",
                    "harus bertipe void *. Alamat bertipe lain HARUS kamu cast sendiri:",
                    "  printf(\"%p\\n\", (void *)&angka);   // benar",
                    "  printf(\"%p\\n\", &angka);           // undefined behavior, walau sering 'jalan'",
                    "printf tidak bisa mengoreksinya karena argumen sesudah format string memang",
                    "tidak diperiksa compiler - alasan lengkapnya di bagian fungsi variadic nanti.",
                    "Inilah penjelasan (void*) yang selama ini muncul di materi Pointer Dasar.",
                ],
            },
            {
                "heading": "Satu void * untuk semua tipe",
                "code": """#include <stdio.h>

// Satu fungsi untuk tipe APA PUN: yang diterima cuma alamat mentah + ukurannya.
void cetak_byte(const void *data, size_t n) {
    const unsigned char *b = data;   // dari void * ke tipe nyata (cast opsional di C)
    for (size_t i = 0; i < n; i++) {
        printf("%02x ", b[i]);
    }
    printf("\\n");
}

int main(void) {
    int angka = 5;
    double pecahan = 1.5;
    char huruf = 'A';

    void *p;              // satu variabel, sanggup menampung alamat apa pun

    p = &angka;
    printf("alamat angka : %p\\n", p);
    printf("isi angka    : %d\\n", *(int *)p);      // WAJIB di-cast sebelum di-*

    p = &pecahan;
    printf("isi pecahan  : %.1f\\n", *(double *)p);

    p = &huruf;
    printf("isi huruf    : %c\\n", *(char *)p);

    // Mencetak alamat variabel lain: %p minta void *, jadi alamatnya di-cast.
    printf("alamat huruf : %p\\n", (void *)&huruf);

    cetak_byte(&angka, sizeof angka);   // 05 00 00 00 di mesin little-endian
    cetak_byte(&huruf, sizeof huruf);   // 41  (kode ASCII 'A')

    // p + 1;   // ditolak -Wpedantic: aritmatika pada void *, ukurannya tak diketahui
    // *p;      // GALAT keras: mau dibaca berapa byte? tidak ada yang tahu
    return 0;
}""",
            },
            {
                "heading": "typedef untuk tipe FUNGSI, dan struct berisi function pointer",
                "body": [
                    "Sintaks function pointer dari materi sebelumnya jadi hampir tak terbaca begitu",
                    "ia masuk ke daftar parameter atau ke dalam sebuah struct. Karena itu kode nyata",
                    "hampir selalu menyembunyikannya di balik typedef lebih dulu:",
                    "",
                    "  typedef int (*Pembanding)(const void *, const void *);",
                    "",
                    "Perhatikan bedanya dengan typedef struct: pada typedef tipe FUNGSI, nama tipenya",
                    "duduk di TENGAH, bukan di akhir. Baca dari dalam ke luar - '(*Pembanding)' itu",
                    "sebuah pointer, '(const void *, const void *)' membuatnya pointer ke fungsi, dan",
                    "'int' di depan adalah nilai kembali fungsinya.",
                    "",
                    "Sesudah itu Pembanding dipakai persis seperti tipe biasa:",
                    "  Pembanding f = banding_int;                     // variabel",
                    "  void urutkan(int *a, int n, Pembanding f);      // parameter",
                    "  struct Aturan { const char *nama; Pembanding banding; };   // field struct",
                    "",
                    "Konvensi akhiran _t (size_t, time_t, uint32_t, FILE, pthread_t) menandai 'ini",
                    "nama TIPE, bukan nama variabel atau fungsi'. Pakai kalau kodemu bergaya pustaka",
                    "C. Satu catatan jujur: POSIX memesan akhiran _t untuk dirinya sendiri, jadi",
                    "sebagian proyek sengaja memilih gaya lain (PembandingFn, penulis_fn). Yang jauh",
                    "lebih penting daripada memilih gaya: konsisten di dalam satu proyek.",
                    "",
                    "Struct yang field-nya berisi function pointer adalah cara C meniru interface,",
                    "atau vtable. Objek di C++, Java, dan Go menyimpan tabel semacam ini di dalamnya",
                    "juga - bedanya di sana tabelnya dibuatkan compiler, sedangkan di C kamu sendiri",
                    "yang mengisi tiap field-nya. Tanpa mengenali bentuk ini, baris seperti",
                    "'.tulis = tulis_berkas' di kode orang akan terlihat seperti sihir.",
                ],
                "code": """#include <stdio.h>

// typedef untuk TIPE FUNGSI: nama tipenya diselipkan di TENGAH, bukan di akhir.
typedef int (*penulis_t)(const char *pesan);

static int tulis_layar(const char *pesan) {
    return printf("layar | %s\\n", pesan);
}

static int tulis_diam(const char *pesan) {
    (void)pesan;      // sengaja diabaikan; (void)x mematikan peringatan "tak terpakai"
    return 0;
}

// "Interface" versi C: struct yang isinya function pointer.
typedef struct {
    const char *nama;
    penulis_t   tulis;    // field bertipe function pointer, ditulis lewat typedef
} Ops;

// lapor() tidak tahu - dan tidak perlu tahu - pesannya berakhir di mana.
static void lapor(const Ops *ops, const char *pesan) {
    if (ops->tulis(pesan) < 0) {
        printf("gagal menulis lewat %s\\n", ops->nama);
    }
}

// typedef yang sama dipakai sebagai TIPE PARAMETER
static void coba(penulis_t f) {
    f("dipanggil lewat parameter bertipe penulis_t");
}

int main(void) {
    Ops layar = { .nama = "layar", .tulis = tulis_layar };
    Ops diam  = { .nama = "diam",  .tulis = tulis_diam  };

    lapor(&layar, "halo");
    lapor(&diam,  "pesan ini hilang tanpa jejak");

    Ops aktif = diam;
    aktif.tulis = tulis_layar;   // ganti implementasi = ganti SATU pointer
    lapor(&aktif, "implementasi ditukar saat program berjalan");

    coba(tulis_layar);
    return 0;
}""",
            },
            {
                "heading": "qsort & bsearch: void * yang paling sering kamu temui",
                "body": [
                    "qsort() dari <stdlib.h> mengurutkan array APA PUN. Karena ia sama sekali tidak",
                    "tahu isi arraymu, kamu wajib memberitahu empat hal:",
                    "",
                    "  qsort(arr, n, sizeof arr[0], banding);",
                    "    arr             alamat elemen pertama - masuk sebagai void *",
                    "    n               BANYAK elemen, bukan jumlah byte",
                    "    sizeof arr[0]   ukuran SATU elemen, supaya qsort bisa melompat & menukar",
                    "    banding         fungsi yang memutuskan siapa duluan",
                    "",
                    "Tulis 'sizeof arr[0]', bukan 'sizeof(int)'. Kalau suatu hari tipe elemennya",
                    "berubah, bentuk pertama ikut benar sendiri sedangkan bentuk kedua diam-diam",
                    "mengacak seluruh isi array tanpa satu pun peringatan compiler.",
                    "",
                    "Kontrak comparator - hafalkan sekali, dipakai seumur hidup:",
                    "  int banding(const void *a, const void *b);",
                    "  kembalikan < 0 bila a harus di DEPAN b, > 0 bila di BELAKANG, 0 bila setara.",
                    "a dan b adalah alamat DUA ELEMEN. Untuk array int, isinya int *, bukan int -",
                    "makanya harus di-cast dan di-dereference dulu sebelum dibandingkan.",
                    "",
                    "JEBAKAN yang tersebar di seluruh internet: 'return *(int *)a - *(int *)b;'.",
                    "Bentuk ini SALAH. Pengurangan int bisa overflow. Urutkan {2000000000,",
                    "-2000000000, 0} dengan comparator itu: selisihnya 4 miliar, tidak muat di int,",
                    "tandanya berbalik, dan qsort mengembalikan urutan yang keliru - tanpa peringatan",
                    "apa pun, tanpa crash. Bandingkan dengan < dan > seperti pada kode di bawah.",
                    "",
                    "bsearch() memakai tanda tangan dan comparator yang SAMA, mencari secara binary",
                    "search, dan mengembalikan NULL bila tidak ketemu. Ia hanya sah pada array yang",
                    "SUDAH terurut dengan comparator itu juga; kalau tidak, hasilnya bukan sekadar",
                    "'salah' tapi tak bisa ditebak sama sekali.",
                ],
                "code": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char nama[16];
    int  nilai;
} Siswa;

// Tanda tangan comparator SELALU begini - qsort yang menentukan, bukan kita.
int banding_int(const void *a, const void *b) {
    int x = *(const int *)a;     // cast dulu ke tipe asli, BARU dereference
    int y = *(const int *)b;
    if (x < y) return -1;        // JANGAN 'return x - y;' - bisa overflow
    if (x > y) return 1;
    return 0;
}

// Mengurutkan array of struct berdasarkan SALAH SATU field-nya.
int banding_siswa(const void *a, const void *b) {
    const Siswa *p = a;          // void * -> Siswa *, cast tidak wajib di C
    const Siswa *q = b;
    if (p->nilai != q->nilai) {
        return (p->nilai < q->nilai) ? 1 : -1;   // nilai BESAR lebih dulu
    }
    return strcmp(p->nama, q->nama);             // seri -> urut abjad
}

// Mengurutkan array of char *: elemennya SENDIRI sudah pointer, jadi a menunjuk
// ke sebuah 'const char *', bukan ke huruf pertamanya. Itu sebabnya ada bintang
// dua dan ada *p di dalam strcmp.
int banding_teks(const void *a, const void *b) {
    const char *const *p = a;
    const char *const *q = b;
    return strcmp(*p, *q);
}

int main(void) {
    int angka[] = {42, 7, 13, 7, 99, 1};
    size_t n = sizeof angka / sizeof angka[0];

    qsort(angka, n, sizeof angka[0], banding_int);
    for (size_t i = 0; i < n; i++) printf("%d ", angka[i]);
    printf("\\n");                                  // 1 7 7 13 42 99

    int cari = 13;
    int *ketemu = bsearch(&cari, angka, n, sizeof angka[0], banding_int);
    printf("13 -> %s (indeks %ld)\\n", ketemu ? "ketemu" : "tidak ada",
           ketemu ? ketemu - angka : -1);

    Siswa kelas[] = {{"Dedi", 80}, {"Ani", 95}, {"Budi", 80}};
    qsort(kelas, 3, sizeof kelas[0], banding_siswa);
    for (int i = 0; i < 3; i++) printf("%-5s %d\\n", kelas[i].nama, kelas[i].nilai);

    const char *buah[] = {"mangga", "apel", "jeruk"};
    qsort(buah, 3, sizeof buah[0], banding_teks);
    for (int i = 0; i < 3; i++) printf("%s ", buah[i]);
    printf("\\n");                                  // apel jeruk mangga
    return 0;
}""",
            },
            {
                "heading": "Fungsi variadic: tanda ... , <stdarg.h>, dan cara printf bekerja",
                "body": [
                    "Setelah puluhan kali menulis printf(\"%d %s\\n\", a, b), pertanyaannya wajar:",
                    "bagaimana SATU fungsi bisa menerima jumlah argumen yang berbeda-beda tiap",
                    "dipanggil? Jawabannya fungsi variadic, dan tanda tangan printf memperlihatkannya:",
                    "",
                    "  int printf(const char *fmt, ...);",
                    "",
                    "Tiga titik itu sungguhan bagian dari sintaks C, bukan singkatan penulis buku.",
                    "Alat untuk membaca argumen tambahan itu ada di <stdarg.h>:",
                    "  va_list ap;           wadah penunjuk argumen",
                    "  va_start(ap, fmt);    mulai - sebutkan parameter BERNAMA yang paling akhir",
                    "  va_arg(ap, int);      ambil satu argumen; KAMU yang menyebutkan tipenya",
                    "  va_end(ap);           tutup - wajib, sepasang dengan va_start",
                    "",
                    "Yang bikin orang tersandung:",
                    "  - Wajib ada minimal SATU parameter bernama sebelum '...'; va_start perlu",
                    "    pijakan untuk tahu di mana argumen tambahan dimulai.",
                    "  - Tidak ada cara apa pun mengetahui BERAPA argumen yang dikirim. Kamu harus",
                    "    memberi tahu sendiri: lewat hitungan (jumlahkan(3, ...)), lewat penanda",
                    "    akhir seperti NULL, atau lewat format string - itu cara printf.",
                    "  - va_arg(ap, char) dan va_arg(ap, float) SELALU salah. Argumen variadic",
                    "    mengalami promosi otomatis: char/short jadi int, float jadi double. Minta",
                    "    int dan double, lalu kecilkan sendiri kalau perlu.",
                    "  - Fungsi variadic TIDAK bisa meneruskan '...'-nya ke printf. Untuk itu ada",
                    "    varian ber-'v' yang menerima va_list: vprintf, vfprintf, vsnprintf.",
                    "",
                    "Dan inilah jawaban atas jebakan printf yang paling mahal: argumen sesudah format",
                    "string TIDAK diperiksa compiler - tipenya memang tidak tertulis di tanda tangan",
                    "fungsinya. printf(\"%d\", \"halo\") lolos kompilasi dan merusak apa pun saat",
                    "dijalankan. gcc terlihat memeriksanya hanya karena printf dikenali secara khusus.",
                    "Untuk fungsi variadic buatanmu sendiri, mintalah pemeriksaan yang sama dengan",
                    "atribut format() di kode bawah; tanpa atribut itu, compiler diam saja.",
                ],
                "code": """#include <stdarg.h>
#include <stdio.h>

// '...' berarti "boleh ada argumen tambahan". WAJIB ada minimal SATU parameter
// bernama sebelum '...' - itulah tempat berpijak va_start.
int jumlahkan(int banyak, ...) {
    va_list ap;
    int total = 0;

    va_start(ap, banyak);            // sebut parameter bernama TERAKHIR
    for (int i = 0; i < banyak; i++) {
        total += va_arg(ap, int);    // KITA yang menyebut tipenya, bukan compiler
    }
    va_end(ap);                      // wajib, sepasang dengan va_start
    return total;
}

// Meneruskan '...' ke fungsi lain: pakai varian ber-'v'. Atribut format() di
// bawah ini khas gcc/clang; berkatnya compiler memeriksa argumen log_galat
// persis seperti printf. Tanpa atribut itu, salah format specifier lolos diam.
__attribute__((format(printf, 1, 2)))
void log_galat(const char *fmt, ...) {
    va_list ap;
    va_start(ap, fmt);
    fprintf(stderr, "GALAT: ");
    vfprintf(stderr, fmt, ap);       // inilah cara printf sendiri bekerja
    fprintf(stderr, "\\n");
    va_end(ap);
}

int main(void) {
    printf("%d\\n", jumlahkan(3, 10, 20, 30));      // 60
    printf("%d\\n", jumlahkan(5, 1, 2, 3, 4, 5));   // 15
    printf("%d\\n", jumlahkan(0));                  // 0 - tanpa argumen tambahan

    // Baris berikut keluar lewat stderr yang tidak di-buffer, jadi jangan kaget
    // kalau ia muncul MENDAHULUI angka-angka di atas saat dijalankan.
    log_galat("berkas %s tidak ditemukan (kode %d)", "data.txt", 2);
    return 0;
}""",
            },
        ],
    },
    {
        "title": "30. Linked List: Struktur Data Dinamis",
        "sections": [
            {
                "body": [
                    "Linked List = struktur data yang terdiri dari beberapa",
                    "'node', masing-masing berisi DATA + POINTER ke node berikutnya.",
                    "BEDA dari array: ukurannya benar-benar dinamis (tambah/hapus",
                    "node kapan saja tanpa perlu 'menggeser' elemen lain).",
                    "",
                    "  struct Node {",
                    "      int data;",
                    "      struct Node *next;    // pointer ke node BERIKUTNYA",
                    "  };",
                    "",
                    "  [data|next] -> [data|next] -> [data|next] -> NULL",
                    "   node 1         node 2         node 3 (terakhir, next=NULL)",
                ]
            },
            {
                "heading": "Implementasi linked list sederhana",
                "code": """#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node *next;
} Node;

// Menambah node BARU di awal list (head)
Node* tambahDiAwal(Node *head, int nilai) {
    Node *baru = (Node*) malloc(sizeof(Node));
    baru->data = nilai;
    baru->next = head;     // node baru menunjuk ke head LAMA
    return baru;           // node baru jadi head BARU
}

// Menampilkan semua elemen list
void tampilkan(Node *head) {
    Node *current = head;
    while (current != NULL) {
        printf("%d -> ", current->data);
        current = current->next;
    }
    printf("NULL\\n");
}

// WAJIB: bebaskan SEMUA node agar tidak memory leak
void bebaskanList(Node *head) {
    Node *current = head;
    while (current != NULL) {
        Node *temp = current;
        current = current->next;
        free(temp);
    }
}

int main(void) {
    Node *head = NULL;               // list awalnya kosong

    head = tambahDiAwal(head, 30);
    head = tambahDiAwal(head, 20);
    head = tambahDiAwal(head, 10);

    tampilkan(head);      // 10 -> 20 -> 30 -> NULL

    bebaskanList(head);   // WAJIB, karena tiap node hasil malloc()
    head = NULL;

    return 0;
}"""
            },
            {
                "body": [
                    "Kelebihan linked list dibanding array:",
                    "  - Ukuran benar-benar dinamis, insert/delete di awal O(1).",
                    "  - Tidak perlu 'menggeser' elemen lain saat insert/delete.",
                    "",
                    "Kekurangan dibanding array:",
                    "  - TIDAK bisa akses langsung by index (harus 'jalan' node",
                    "    demi node dari head - akses elemen ke-n adalah O(n)).",
                    "  - Butuh memori EKSTRA untuk menyimpan pointer 'next'.",
                    "  - Lebih rawan bug (lupa update pointer, memory leak).",
                    "",
                    "Linked list adalah FONDASI untuk struktur data lanjutan:",
                    "  Stack, Queue, Doubly Linked List, Binary Tree, Graph -",
                    "  semuanya memakai konsep node + pointer yang sama.",
                ]
            },
        ],
    },
    {
        "title": "31. Kompilasi Multi-File & Header (.h)",
        "sections": [
            {
                "body": [
                    "Project C nyata SELALU dipecah jadi banyak file (.c) agar",
                    "terorganisir, dengan file .h (header) untuk 'menyambungkan'",
                    "deklarasi antar file.",
                    "",
                    "Struktur umum:",
                    "  matematika.h  -> deklarasi (prototype) fungsi",
                    "  matematika.c  -> implementasi (isi) fungsi",
                    "  main.c        -> memakai fungsi dari matematika.h",
                ]
            },
            {
                "heading": "Contoh struktur multi-file",
                "code": """/* ===== File: matematika.h ===== */
#ifndef MATEMATIKA_H
#define MATEMATIKA_H

int tambah(int a, int b);
int kurang(int a, int b);

#endif

/* ===== File: matematika.c ===== */
#include "matematika.h"

int tambah(int a, int b) {
    return a + b;
}

int kurang(int a, int b) {
    return a - b;
}

/* ===== File: main.c ===== */
#include <stdio.h>
#include "matematika.h"     // tanda kutip untuk header SENDIRI (bukan <>)

int main(void) {
    printf("%d\\n", tambah(10, 5));
    printf("%d\\n", kurang(10, 5));
    return 0;
}"""
            },
            {
                "body": [
                    "Kompilasi manual multi-file:",
                    "  gcc main.c matematika.c -o program",
                    "  ./program",
                    "",
                    "Untuk project besar, kompilasi manual jadi merepotkan -",
                    "gunakan Makefile untuk otomatisasi:",
                    "",
                    "  # Makefile",
                    "  program: main.c matematika.c",
                    "  \tgcc main.c matematika.c -o program",
                    "",
                    "  clean:",
                    "  \trm -f program",
                    "",
                    "  Jalankan dengan: make       (kompilasi)",
                    "                   make clean (hapus hasil build)",
                    "",
                    "  (Catatan: baris perintah Makefile HARUS diawali karakter",
                    "  TAB, bukan spasi - kesalahan umum pemula saat menulis Makefile.)",
                ]
            },
            {
                "heading": "Bentuk header C sungguhan (yang benar-benar kamu buka)",
                "body": [
                    "Header di contoh tadi sudah benar, tapi masih telanjang. Buka",
                    "berkas .h dari pustaka C mana pun - SQLite, zlib, cJSON - dan",
                    "tiga hal berikut hampir selalu ada, justru di bagian PERTAMA",
                    "yang dilihat mata.",
                    "",
                    "1. Blok komentar pembuka berisi keterangan berkas dan lisensi.",
                    "   Baris SPDX-License-Identifier itu bentuk baku yang dibaca",
                    "   mesin - satu baris menggantikan paragraf lisensi panjang.",
                    "",
                    "2. Blok extern \"C\", tepat SETELAH include guard. Ini pagar",
                    "   untuk pemakai C++: compiler C++ mengubah nama fungsi saat",
                    "   dikompilasi (name mangling, supaya boleh ada dua fungsi",
                    "   bernama sama dengan tipe berbeda). Kalau header C dipakai",
                    "   dari C++ tanpa pagar ini, linker mencari nama yang sudah",
                    "   berubah dan tidak menemukan apa pun di .o milikmu.",
                    "   Makro __cplusplus HANYA didefinisikan oleh compiler C++,",
                    "   jadi bagi gcc yang mengompilasi C blok itu lenyap total.",
                    "",
                    "3. Komentar dokumentasi bergaya Doxygen (/** ... */ dengan",
                    "   @param dan @return) di atas tiap prototype. Bentuk ini",
                    "   dibaca alat pembuat dokumentasi, dan editor modern",
                    "   memunculkannya sebagai tooltip saat kamu mengetik nama",
                    "   fungsinya.",
                ]
            },
            {
                "code": """/* statistik.h - hitungan rata-rata sederhana.
 * SPDX-License-Identifier: MIT
 */
#ifndef STATISTIK_H
#define STATISTIK_H

#ifdef __cplusplus
extern "C" {
#endif

/* Dibaca semua berkas .c yang meng-include header ini.
   Definisi SEBENARNYA (tanpa extern) hidup di statistik.c saja. */
extern int jumlah_panggilan;

/** Menghitung rata-rata isi arr.
 *  @param arr array bilangan, tidak boleh NULL
 *  @param n   jumlah elemen, harus lebih besar dari 0
 *  @return    rata-rata sebagai double
 */
double rata_rata(const int *arr, int n);

#ifdef __cplusplus
}
#endif

#endif  /* STATISTIK_H */"""
            },
            {
                "body": [
                    "Perhatikan baris extern int jumlah_panggilan. Header bukan",
                    "cuma tempat prototype fungsi - ia juga cara BERBAGI VARIABEL",
                    "antar berkas. Aturannya:",
                    "",
                    "  statistik.h  ->  extern int jumlah_panggilan;   // JANJI",
                    "  statistik.c  ->  int jumlah_panggilan = 0;      // BARANGNYA",
                    "",
                    "extern berarti 'variabel ini ADA di suatu berkas lain, linker",
                    "yang mencarikan'. Tanpa extern, tiap berkas yang meng-include",
                    "header itu membuat variabelnya SENDIRI, dan linker berhenti",
                    "dengan 'multiple definition of jumlah_panggilan'. Lawannya,",
                    "static di depan variabel atau fungsi, justru MENYEMBUNYIKAN-nya",
                    "dari berkas lain - keduanya dibahas di materi Lingkup, Masa",
                    "Hidup & Kelas Penyimpanan Variabel.",
                    "",
                    "Catatan jujur: variabel global yang dibagi lewat header itu",
                    "gampang menyusahkan (siapa saja bisa mengubahnya, dari mana",
                    "saja). Kode yang rapi lebih memilih fungsi pengaksesnya -",
                    "misalnya int statistik_jumlah_panggilan(void). Tapi bentuk",
                    "extern ini ada di mana-mana di kode nyata, jadi kamu harus",
                    "bisa membacanya.",
                ]
            },
        ],
    },
    {
        "title": "32. Membangun Proyek C: Kompilasi Terpisah, Linker & Build System",
        "sections": [
            {
                "body": [
                    "Materi Kompilasi Multi-File & Header sudah menunjukkan cara memecah proyek jadi .c dan",
                    ".h, lalu menutupnya dengan satu perintah: gcc main.c matematika.c -o program. Perintah",
                    "itu bekerja, tapi ia menyembunyikan seluruh mesinnya - dan begitu proyekmu tumbuh, atau",
                    "begitu kamu mencoba mengompilasi kode orang lain dari GitHub, justru yang tersembunyi",
                    "itulah yang akan menghentikanmu.",
                    "",
                    "Yang sebenarnya terjadi: gcc bukan satu program, melainkan SOPIR yang memanggil empat",
                    "program berbeda secara berurutan. Tiap tahap punya keluaran sendiri dan JENIS GALAT",
                    "sendiri - dan pesan galatnya terlihat sangat berbeda satu sama lain.",
                    "",
                    "  1. PREPROCESSOR (cpp)      .c  ->  .i",
                    "     Menjalankan semua baris berawalan #: isi #include disalin masuk, #define diganti",
                    "     teksnya. Belum ada satu pun kode yang diperiksa benar-salahnya.",
                    "       gcc -E main.c -o main.i",
                    "     Coba sendiri: main.c yang cuma 12 baris membengkak jadi 856 baris begitu isi",
                    "     <stdio.h> disalin ke dalamnya. Angkanya beda-beda tiap mesin; besarnya itu",
                    "     yang penting. (Tahapnya dibongkar di materi Preprocessor & Macro.)",
                    "",
                    "  2. COMPILER (cc1)          .i  ->  .s",
                    "     Menerjemahkan C jadi ASSEMBLY - masih teks, tapi sudah berupa perintah prosesor.",
                    "       gcc -S main.c -o main.s",
                    "     Di sinilah galat sintaks dan galat tipe lahir, dan semuanya menyebut nomor baris.",
                    "",
                    "  3. ASSEMBLER (as)          .s  ->  .o",
                    "     Assembly jadi OBJECT FILE: berkas BINER berisi kode mesin.",
                    "       gcc -c main.c -o main.o",
                    "     Object file BELUM bisa dijalankan. Ia tahu dirinya memanggil rata_rata(), tapi",
                    "     belum tahu rata_rata() ada di alamat berapa - lubang itu sengaja dibiarkan kosong.",
                    "",
                    "  4. LINKER (ld)             .o + .o + pustaka  ->  satu executable",
                    "     Mengisi semua lubang tadi lalu menyatukannya jadi satu berkas yang bisa dijalankan.",
                    "       gcc main.o statistik.o -o program -lm",
                    "     Di sinilah 'undefined reference' lahir - galat yang TIDAK menunjuk baris kodemu.",
                    "",
                    "Tiga tahap pertama dikerjakan PER BERKAS .c, sendiri-sendiri, seolah berkas lain tidak",
                    "ada. Baru tahap keempat melihat semuanya sekaligus. Itu satu kalimat, tapi hampir semua",
                    "kebingungan proyek C bermuara ke sana.",
                ],
            },
            {
                "heading": "Satu proyek kecil: tiga berkas kode + satu Makefile",
                "code": """/* ===== File: statistik.h ===== */
#ifndef STATISTIK_H
#define STATISTIK_H

/* Header itu JANJI: hanya prototype. Kode mesinnya ada di statistik.c. */
double rata_rata(const double *data, int n);
double simpangan_baku(const double *data, int n);

#endif

/* ===== File: statistik.c ===== */
#include <math.h>          /* sqrt() -> perlu -lm saat MENAUTKAN, bukan saat compile */
#include "statistik.h"     /* agar compiler mengadu isi di sini dengan janji di .h  */

double rata_rata(const double *data, int n) {
    double total = 0.0;
    for (int i = 0; i < n; i++) {
        total += data[i];
    }
    return total / n;
}

double simpangan_baku(const double *data, int n) {
    double m = rata_rata(data, n);
    double jumlah = 0.0;
    for (int i = 0; i < n; i++) {
        jumlah += (data[i] - m) * (data[i] - m);
    }
    return sqrt(jumlah / n);
}

/* ===== File: main.c ===== */
#include <stdio.h>
#include "statistik.h"

int main(void) {
    double nilai[] = {80.0, 90.0, 70.0, 100.0, 60.0};
    int n = 5;

    printf("Jumlah data    : %d\\n", n);
    printf("Rata-rata      : %.2f\\n", rata_rata(nilai, n));
    printf("Simpangan baku : %.2f\\n", simpangan_baku(nilai, n));
    return 0;
}

# ===== File: Makefile =====
# PERHATIAN: tiap baris perintah di bawah diawali karakter TAB, bukan spasi.
CC      = gcc
CFLAGS  = -std=c11 -Wall -Wextra -g
LDLIBS  = -lm
OBJ     = main.o statistik.o

.PHONY: all clean

all: program

program: $(OBJ)
	$(CC) $^ -o $@ $(LDLIBS)

%.o: %.c statistik.h
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(OBJ) program""",
            },
            {
                "body": [
                    "KOMPILASI TERPISAH",
                    "Simpan keempat berkas di atas dalam satu folder, lalu kerjakan tahap 3 dan 4 sendiri-",
                    "sendiri - persis yang nanti dilakukan make untukmu:",
                    "",
                    "  gcc -std=c11 -Wall -Wextra -c main.c      -o main.o",
                    "  gcc -std=c11 -Wall -Wextra -c statistik.c -o statistik.o",
                    "  gcc main.o statistik.o -o program -lm",
                    "  ./program",
                    "",
                    "  Jumlah data    : 5",
                    "  Rata-rata      : 80.00",
                    "  Simpangan baku : 14.14",
                    "",
                    "Kenapa repot, padahal 'gcc main.c statistik.c -o program -lm' juga berhasil?",
                    "  - Kalau besok hanya statistik.c yang kamu ubah, cukup statistik.o yang dibuat ulang.",
                    "    Di proyek 4 berkas bedanya tak terasa; di proyek 4.000 berkas itu beda 3 detik",
                    "    melawan 20 menit, setiap kali kamu mengetik ulang satu huruf.",
                    "  - Berkas .o bisa dipakai ulang: dibungkus jadi pustaka, dipakai beberapa program.",
                    "  Menghemat kompilasi ulang itu SATU-SATUNYA alasan Makefile ada. Kalau kalimat ini",
                    "  sudah masuk, sisa materi ini tinggal sintaks.",
                    "",
                    "Perhatikan pembagian flag-nya. -std, -Wall, -Wextra, -g dipakai saat MEMBUAT .o;",
                    "-lm dipakai saat MENAUTKAN. Menaruh -lm di perintah -c tidak berguna, dan menaruh",
                    "-Wall di perintah link tidak memeriksa apa pun: dua tahap berbeda, dua daftar flag",
                    "berbeda. Itu juga sebabnya Makefile memisahkan CFLAGS dari LDLIBS.",
                    "",
                    "DUA KELUARGA GALAT - PEMBEDA PALING BERGUNA DI MATERI INI",
                    "Sebelum memperbaiki apa pun, tanyakan dulu: SIAPA yang bicara?",
                    "",
                    "  statistik.c: In function 'rata_rata':",
                    "  statistik.c:7:25: error: expected ';' before '}' token",
                    "      7 |         total += data[i]",
                    "        |                         ^",
                    "     Ada nama berkas, nomor baris, nomor kolom, dan potongan kodenya = COMPILER.",
                    "     Ada yang salah TULIS. Perbaiki tepat di baris itu, dan selalu kerjakan galat",
                    "     PERTAMA lebih dulu - sisanya sering cuma akibat beruntun dari yang pertama.",
                    "",
                    "  /usr/bin/ld: main.o: in function `main':",
                    "  main.c:(.text+0x71): undefined reference to `rata_rata'",
                    "  collect2: error: ld returned 1 exit status",
                    "     Ada 'ld', ada '(.text+0x71)', dan TIDAK ada potongan kode = LINKER.",
                    "     Tidak ada satu huruf pun di kodemu yang salah tulis. Yang hilang adalah ISI",
                    "     fungsinya. Mencari-cari salah ketik di sini adalah cara tercepat membuang sore.",
                    "",
                    "Buktikan sendiri: jalankan 'gcc main.o -o program -lm' (sengaja tanpa statistik.o) dan",
                    "pesan di atas muncul persis. Tiga sebab tersering undefined reference, urut frekuensi:",
                    "  1. Berkas .c yang berisi fungsi itu lupa ikut ditautkan. Header-nya memang sudah",
                    "     di-include, tapi #include cuma menyalin JANJI - lihat materi Pustaka Standar.",
                    "  2. Namanya beda tipis: rata_rata di .h, rataRata di .c. Compiler diam saja karena",
                    "     tiap berkas dikompilasi sendiri-sendiri; baru linker sadar keduanya tak bertemu.",
                    "  3. Fungsinya milik pustaka yang belum disebut - 'undefined reference to sqrt' = -lm.",
                    "",
                    "Galat kembarannya muncul kalau satu nama punya DUA isi:",
                    "  /usr/bin/ld: salinan.o: in function `rata_rata':",
                    "  salinan.c:(.text+0x0): multiple definition of `rata_rata';",
                    "      statistik.o: first defined here",
                    "     Include guard tidak menolong sedikit pun di sini: ia mencegah pengulangan di",
                    "     DALAM satu berkas, sedangkan linker melihat semua berkas sekaligus. Sebab",
                    "     tersering: menaruh ISI fungsi - bukan cuma prototype - di dalam .h yang di-include",
                    "     dua berkas. Bisa juga karena satu .c tidak sengaja disebut dua kali di perintah",
                    "     link, atau karena variabel global didefinisikan di .h (lihat materi Lingkup,",
                    "     Masa Hidup & Kelas Penyimpanan Variabel soal extern).",
                    "",
                    "Alat pemeriksanya satu perintah, dan ia mengakhiri semua tebak-tebakan: nm membaca",
                    "daftar nama di dalam sebuah .o.",
                    "  nm statistik.o",
                    "    0000000000000000 T rata_rata        T = Tersedia, didefinisikan di berkas ini",
                    "    0000000000000063 T simpangan_baku",
                    "                     U sqrt            U = Undefined, dipakai tapi harus dicari linker",
                    "Kalau nama yang diributkan linker tidak muncul dengan huruf T di satu pun .o milikmu,",
                    "kamu sudah menemukan sebabnya tanpa menebak sekali pun.",
                ],
            },
            {
                "body": [
                    "make cuma bisa satu hal, dan hal itu sederhana: membandingkan WAKTU UBAH berkas. Kalau",
                    "target lebih tua daripada salah satu prasyaratnya, perintahnya dijalankan; kalau tidak,",
                    "dilewati. Seluruh kepintaran 'hanya yang berubah yang dikompilasi ulang' berasal dari",
                    "perbandingan tanggal itu, bukan dari pemahaman apa pun tentang bahasa C.",
                    "",
                    "Bentuk satu ATURAN (rule):",
                    "",
                    "  target: prasyarat prasyarat ...",
                    "  <TAB>perintah",
                    "",
                    "TAB, BUKAN SPASI. Ini jebakan nomor satu Makefile, dan pesannya sama sekali tidak",
                    "menolong:",
                    "  Makefile:2: *** missing separator.  Stop.",
                    "Editor modern sering diam-diam mengubah TAB jadi empat spasi tanpa memberitahumu.",
                    "Begitu melihat pesan itu, periksa indentasinya lebih dulu sebelum mencurigai hal lain.",
                    "",
                    "VARIABEL - dipanggil dengan $(NAMA):",
                    "  CC      = gcc                          compiler yang dipakai",
                    "  CFLAGS  = -std=c11 -Wall -Wextra -g    flag saat MENGOMPILASI  (.c -> .o)",
                    "  LDLIBS  = -lm                          pustaka saat MENAUTKAN (.o -> program)",
                    "  OBJ     = main.o statistik.o           daftar object file, ditulis sekali",
                    "Nama CC, CFLAGS, LDFLAGS, dan LDLIBS bukan sekadar kebiasaan - make sudah mengenalnya",
                    "lewat aturan bawaannya. Karena itu mengganti compiler untuk seluruh proyek cukup",
                    "sebaris: make CC=clang. Nilai di baris perintah menang atas nilai di dalam Makefile.",
                    "",
                    "VARIABEL OTOMATIS - baca saja sebagai kata ganti:",
                    "  $@    nama TARGET aturan ini      di 'program: $(OBJ)' berarti  program",
                    "  $^    SEMUA prasyarat             di aturan yang sama berarti   main.o statistik.o",
                    "  $<    prasyarat PERTAMA saja      di '%.o: %.c statistik.h' berarti berkas .c-nya",
                    "Tanpa ketiganya kamu harus menulis nama berkas yang sama di dua tempat - dan suatu",
                    "hari kamu akan mengubah salah satunya saja lalu bingung sendiri.",
                    "",
                    "ATURAN POLA - satu aturan untuk semua berkas sejenis:",
                    "  %.o: %.c statistik.h",
                    "  <TAB>$(CC) $(CFLAGS) -c $< -o $@",
                    "Dibaca: \"berkas .o apa pun dibuat dari berkas .c bernama sama\". Tanda % adalah bagian",
                    "nama yang dicocokkan; di aturan ini $< jadi main.c atau statistik.c, dan $@ jadi",
                    "main.o atau statistik.o. Tanpa aturan pola kamu menulis satu aturan per berkas.",
                    "",
                    "Perhatikan statistik.h ikut jadi prasyarat di situ. Itu bukan hiasan: tanpa menyebut",
                    "header, mengubah isi .h TIDAK memicu kompilasi ulang, dan kamu akan menatap program",
                    "yang tetap berperilaku lama padahal kodenya sudah diganti. Itu bug 'kok tidak berubah'",
                    "yang paling sering menghabiskan waktu satu sore penuh di proyek C pemula.",
                    "",
                    ".PHONY: all clean",
                    "Menyatakan all dan clean BUKAN nama berkas. Tanpa baris ini, kalau kebetulan ada",
                    "berkas bernama 'clean' di folder itu, make menjawab:",
                    "  make: 'clean' is up to date.",
                    "dan tidak menghapus apa pun. Semua target yang bukan berkas - all, clean, install,",
                    "test, run - wajib didaftarkan di .PHONY.",
                    "",
                    "Target PERTAMA di berkas adalah target bawaan; 'make' polos di sini menjalankan 'all'.",
                    "Coba urutan ini di folder proyek tadi, dan yang diperhatikan adalah baris yang DICETAK:",
                    "  make               -> dua .o dibuat, lalu ditautkan",
                    "  make               -> make: Nothing to be done for 'all'.",
                    "  touch statistik.c",
                    "  make               -> HANYA statistik.o dibuat ulang, lalu ditautkan lagi",
                    "  make clean         -> rm -f main.o statistik.o program",
                    "Baris keempat itulah bukti kompilasi terpisah bekerja: main.o tidak disentuh sama",
                    "sekali. Kalau ingin melihat rencananya tanpa menjalankan apa pun, pakai make -n.",
                ],
            },
            {
                "body": [
                    "VERSI STANDAR C - kenapa CFLAGS di atas repot-repot menulis -std=c11",
                    "\"C\" bukan satu bahasa yang membeku di tahun 1972. Ada beberapa versi resmi, dan",
                    "compiler bisa disuruh mengikuti yang mana:",
                    "",
                    "  C89 / C90   Standar pertama. Variabel WAJIB dideklarasikan di ATAS blok, dan komentar",
                    "              hanya /* ... */ - tidak ada //.",
                    "  C99         // komentar, deklarasi di dalam for, <stdbool.h>, array berukuran variabel",
                    "              (VLA), dan inisialisasi bernama: struct Titik t = {.x = 1, .y = 2};",
                    "  C11         _Static_assert, struct/union anonim, dukungan thread; VLA turun jadi opsional.",
                    "  C17         C11 dengan perbaikan rumusan saja - tidak ada fitur baru.",
                    "  C23         bool, true, false jadi kata kunci sendiri (tanpa <stdbool.h>), nullptr,",
                    "              constexpr.",
                    "",
                    "Kalau -std= tidak ditulis, gcc memakai bawaan VERSINYA SENDIRI - dan bawaan itu berubah",
                    "antar versi gcc (gcc lama memakai gnu11 lalu gnu17, gcc 15 ke atas sudah gnu23).",
                    "Akibatnya kode yang mulus di mesinmu bisa gagal di mesin orang lain tanpa satu baris",
                    "pun berubah. Karena itu proyek sungguhan selalu menyebut versinya. Buktikan sendiri:",
                    "  gcc -std=c89 main.c   -> error: C++ style comments are not allowed in ISO C90",
                    "                           error: 'for' loop initial declarations are only allowed",
                    "                           in C99 or C11 mode",
                    "  gcc -std=c11 main.c   -> lolos",
                    "  -std=gnu11 berarti C11 ditambah ekstensi khas GNU. Linux kernel memakai varian gnu.",
                    "",
                    "FLAG PUSTAKA & HEADER",
                    "  -lnama    tautkan pustaka libnama: -lm (math.h), -lpthread, -lsqlite3, -lcurl.",
                    "            Materi Pustaka Standar sudah menjelaskan kenapa <math.h> butuh -lm",
                    "            sementara <stdio.h> tidak. Tulis -l di AKHIR, sesudah nama berkas.",
                    "  -L dir    direktori tempat LINKER mencari berkas pustaka   (-L. = folder ini)",
                    "  -I dir    direktori tempat COMPILER mencari header         (-Iinclude)",
                    "  Bedakan baik-baik: -I bekerja di tahap 1-2, -L dan -l di tahap 4. Salah menaruhnya",
                    "  memberi galat yang menyesatkan - 'No such file or directory' untuk header yang",
                    "  sebenarnya ada di disk, misalnya.",
                    "",
                    "PUSTAKA STATIS vs DINAMIS",
                    "  Statis   libnama.a    Dibuat dengan arsiper: ar rcs libstatistik.a statistik.o",
                    "                        (r = masukkan, c = buat kalau belum ada, s = tulis indeks.)",
                    "                        Isinya DISALIN ke dalam executable saat menautkan. Berkasnya",
                    "                        jadi besar, tapi jalan di mesin yang tidak punya pustaka itu.",
                    "  Dinamis  libnama.so   (.dll di Windows, .dylib di macOS.) TIDAK disalin; yang",
                    "                        disimpan cuma catatan \"nanti cari libm.so.6\", dan pustakanya",
                    "                        dimuat saat program DIJALANKAN. Satu salinan di disk dipakai",
                    "                        semua program, dan bisa diperbarui tanpa mengompilasi ulang",
                    "                        programmu. Harganya: berkasnya harus ADA di mesin tujuan.",
                    "  Melihat pustaka dinamis apa yang dipakai sebuah program:",
                    "    ldd ./program",
                    "      libm.so.6 => /lib64/libm.so.6",
                    "      libc.so.6 => /lib64/libc.so.6",
                    "  libstatistik.a TIDAK akan muncul di daftar ldd, dan itu memang benar: yang statis",
                    "  sudah menyatu ke dalam executable dan bukan lagi berkas terpisah.",
                    "",
                    "BUILD SYSTEM YANG DIPAKAI PROYEK SUNGGUHAN",
                    "Makefile tulisan tangan cocok untuk proyek kecil. Proyek besar memakai alat yang",
                    "MEMBUATKAN Makefile, karena satu Makefile yang benar untuk Linux, macOS, dan Windows",
                    "sekaligus terlalu panjang untuk ditulis manual. Lihat berkas apa yang ada di akar repo -",
                    "berkas itu yang menentukan perintahnya, bukan tebakan:",
                    "",
                    "  CMakeLists.txt   ->  cmake -B build && cmake --build build     (paling umum kini)",
                    "  configure        ->  ./configure && make && sudo make install  (autotools, gaya lama)",
                    "  configure.ac     ->  ./autogen.sh dulu, baru ./configure",
                    "  meson.build      ->  meson setup build && ninja -C build",
                    "  Makefile saja    ->  make",
                    "",
                    "Isi CMakeLists.txt untuk proyek statistik tadi cuma sepanjang ini:",
                    "  cmake_minimum_required(VERSION 3.16)",
                    "  project(statistik C)",
                    "  set(CMAKE_C_STANDARD 11)",
                    "  add_executable(program main.c statistik.c)",
                    "  target_link_libraries(program m)",
                    "Perhatikan tidak ada satu pun nama berkas .o di situ. Itu bedanya alat generasi baru:",
                    "kamu menyebut MAKSUD, ia yang menurunkan aturan-aturannya.",
                    "",
                    "pkg-config menjawab satu pertanyaan: \"flag apa yang dibutuhkan pustaka ini di mesin INI?\"",
                    "  pkg-config --cflags --libs zlib      ->  -DWITH_GZFILEOP -lz",
                    "  gcc main.c $(pkg-config --cflags --libs zlib) -o program",
                    "Bentuk $( ... ) menjalankan perintah di dalamnya lebih dulu lalu menempelkan hasilnya",
                    "ke perintah gcc. Ini yang membuat jalur pustaka tidak perlu ditulis tangan per mesin.",
                    "",
                    "RESEP MENGOMPILASI REPO C DARI GITHUB",
                    "  1. Baca README bagian Build / Install / Compiling LEBIH DULU. Hampir semua repo",
                    "     menuliskan perintah persisnya di situ; menebak sendiri hampir selalu lebih lama.",
                    "  2. Lihat berkas di akar repo lalu cocokkan dengan tabel di atas.",
                    "  3. Pasang dependensinya. README biasanya menyebut nama paketnya. Di Debian/Ubuntu",
                    "     akhirannya -dev (libssl-dev), di Fedora/RHEL -devel (openssl-devel).",
                    "  4. Jalankan perintah bakunya. Kalau gagal, baca galat PERTAMA, bukan yang terakhir:",
                    "       fatal error: openssl/ssl.h: No such file  ->  paket -dev/-devel belum terpasang",
                    "       undefined reference to 'SSL_new'          ->  pustakanya belum disebut di -l",
                    "       missing separator                         ->  Makefile-nya rusak (TAB)",
                    "  5. Kalau repo memakai submodule, klon dengan git clone --recursive, atau perbaiki",
                    "     belakangan dengan git submodule update --init. Lupa ini memberi galat 'No such",
                    "     file' untuk folder yang di GitHub kelihatan ada.",
                    "",
                    "Aturan tambahan di bawah membungkus statistik.o jadi pustaka statis, lalu memakainya",
                    "lewat -L dan -l. Tempelkan di bawah Makefile tadi, lalu jalankan make program-statis.",
                ],
                "code": """# Aturan TAMBAHAN untuk Makefile di atas - bukan berkas baru, tempel di bawahnya.
# Ingat: baris perintahnya diawali TAB.

libstatistik.a: statistik.o
	ar rcs $@ $^

program-statis: main.o libstatistik.a
	$(CC) main.o -L. -lstatistik $(LDLIBS) -o $@

# make program-statis  -> bangun pustakanya dulu, baru tautkan dengan -lstatistik
# ldd ./program-statis  -> hanya libm dan libc yang terdaftar; yang statis sudah menyatu
# Jangan lupa: tambahkan libstatistik.a dan program-statis ke aturan clean di atas.""",
            },
        ],
    },
    {
        "title": "33. Debugging: gdb, valgrind & Bug Umum",
        "sections": [
            {
                "body": [
                    "C TIDAK punya 'jaring pengaman' seperti bahasa modern -",
                    "banyak kesalahan (akses memori ilegal, dll) TIDAK terdeteksi",
                    "saat kompilasi, hanya muncul sebagai CRASH saat runtime.",
                    "Karena itu, debugging adalah skill WAJIB untuk programmer C.",
                    "",
                    "Bug paling umum & berbahaya di C:",
                    "  1. Segmentation fault (segfault): akses memori yang",
                    "     TIDAK BOLEH diakses (null pointer, array out-of-bounds,",
                    "     use-after-free).",
                    "  2. Memory leak: lupa free() memori yang di-malloc().",
                    "  3. Buffer overflow: menulis melebihi ukuran array/buffer.",
                    "  4. Uninitialized variable: memakai variabel SEBELUM diisi",
                    "     nilai (isinya 'sampah' dari memori sebelumnya).",
                ]
            },
            {
                "body": [
                    "Kompilasi dengan flag debugging & warning (SELALU lakukan ini!):",
                    "  gcc -Wall -Wextra -g program.c -o program",
                    "    -Wall -Wextra  -> tampilkan SEMUA warning yang mungkin",
                    "                      (BANYAK bug bisa dicegah dari warning saja!)",
                    "    -g             -> sertakan informasi debug untuk gdb",
                    "",
                    "gdb (GNU Debugger) - menjalankan program step-by-step:",
                    "  gdb ./program",
                    "  (gdb) run                  -> jalankan program",
                    "  (gdb) break nama_fungsi     -> pasang breakpoint",
                    "  (gdb) next                  -> jalankan satu baris (step over)",
                    "  (gdb) step                  -> masuk ke dalam fungsi (step into)",
                    "  (gdb) print nama_variabel    -> lihat nilai variabel saat ini",
                    "  (gdb) backtrace              -> lihat 'jejak' fungsi saat crash",
                ]
            },
            {
                "body": [
                    "valgrind - mendeteksi memory leak & akses memori ilegal:",
                    "  valgrind --leak-check=full ./program",
                    "",
                    "  Valgrind akan melaporkan:",
                    "  - Berapa byte 'leaked' (di-malloc tapi tidak pernah di-free)",
                    "  - Baris kode PERSIS yang menyebabkan masalah",
                    "  - Invalid read/write (akses di luar batas alokasi)",
                    "",
                    "Kebiasaan mencegah bug sejak awal:",
                    "  1. SELALU inisialisasi variabel saat dideklarasikan.",
                    "  2. SELALU cek NULL setelah malloc()/fopen().",
                    "  3. SELALU pasangkan tiap malloc() dengan SATU free().",
                    "  4. Kompilasi dengan -Wall -Wextra, JANGAN abaikan warning.",
                    "  5. Set pointer ke NULL setelah free() (hindari dangling pointer).",
                    "  6. Gunakan valgrind SEBELUM menganggap kode 'selesai'.",
                ]
            },
            {
                "heading": "Sanitizer: valgrind yang dipasang di dalam programnya",
                "body": [
                    "valgrind bekerja dari LUAR - ia menjalankan programmu di atas",
                    "CPU tiruan, dan itu membuatnya 10-50 kali lebih lambat.",
                    "Sanitizer bekerja dari DALAM: compiler menyisipkan pemeriksaan",
                    "ke dalam kodemu sendiri saat dikompilasi.",
                    "",
                    "  gcc -fsanitize=address,undefined -g program.c -o program",
                    "  ./program",
                    "",
                    "  address (ASan)     -> buffer overflow, use-after-free,",
                    "                        double free, memory leak",
                    "  undefined (UBSan)  -> integer overflow, geser bit berlebihan,",
                    "                        pembagian nol, dereference NULL",
                    "",
                    "Bedanya dengan valgrind terasa begitu dipakai:",
                    "  - Jauh lebih cepat (sekitar 2x lebih lambat, bukan 20x).",
                    "  - Laporannya menunjuk baris yang salah SEKALIGUS baris",
                    "    tempat memori itu dulu di-malloc dan di-free.",
                    "  - UBSan menangkap kelas bug yang valgrind buta terhadapnya,",
                    "    karena overflow bilangan bukan urusan memori.",
                    "  - Harganya: harus dikompilasi ulang. valgrind sanggup",
                    "    memeriksa program yang binernya sudah jadi.",
                    "",
                    "Kebiasaan yang dipakai proyek sungguhan: sanitizer saat",
                    "mengembangkan (cepat, dipakai tiap kali menjalankan tes),",
                    "valgrind sesekali sebagai pemeriksa kedua. Keduanya JANGAN",
                    "digabung dalam satu jalan - hasilnya kacau. Dan jangan lupa",
                    "membangun ulang TANPA -fsanitize untuk versi rilis.",
                    "",
                    "Kalau gcc menjawab \"cannot find /usr/lib64/libasan.so\",",
                    "runtime-nya belum terpasang: di Fedora pasang paket libasan",
                    "dan libubsan; di Debian/Ubuntu biasanya sudah ikut gcc.",
                ]
            },
            {
                "body": [
                    "Dua alat lagi yang melengkapi bab ini, masing-masing sudah",
                    "punya rumahnya sendiri di kurikulum:",
                    "",
                    "  assert(syarat)  - gdb, valgrind, dan sanitizer hanya bisa",
                    "  MENEMUKAN bug setelah terjadi. assert bekerja terbalik: ia",
                    "  MENYATAKAN asumsimu, dan menghentikan program di detik",
                    "  pertama asumsi itu dilanggar - jauh sebelum akibatnya",
                    "  menyebar dan berubah jadi segfault yang membingungkan.",
                    "  Lihat materi Menangani Kegagalan: errno, perror, assert &",
                    "  goto cleanup.",
                    "",
                    "  -std=c11  - bab ini memakai flag gcc terus-menerus",
                    "  (-g, -fsanitize) tanpa pernah menerangkannya. Satu yang",
                    "  paling sering menggigit: -std= menentukan VERSI bahasa C",
                    "  yang dipakai compiler. Tanpa itu, gcc memakai bawaan",
                    "  versinya sendiri, dan kode yang mulus di mesinmu bisa",
                    "  gagal di mesin orang lain. Seluruh daftar flag - dan",
                    "  kenapa -Wall tidak berguna di perintah link - dibongkar",
                    "  di materi Membangun Proyek C: Kompilasi Terpisah,",
                    "  Linker & Build System.",
                ]
            },
        ],
    },
    {
        "title": "34. Roadmap Menjadi C Programmer Handal",
        "sections": [
            {
                "body": [
                    "Kamu sudah menguasai fondasi C yang solid: sintaks dasar,",
                    "pointer, dynamic memory, struct, linked list, hingga debugging.",
                    "C adalah salah satu bahasa TERSULIT untuk dikuasai TUNTAS -",
                    "tapi begitu paham, bahasa lain akan terasa jauh lebih mudah.",
                    "",
                    "TAHAP 1 - Kuatkan Fondasi (kamu di sini):",
                    "  - Pastikan BENAR-BENAR paham pointer (bukan cuma hafal sintaks).",
                    "  - Latihan: implementasikan struktur data dari nol (stack,",
                    "    queue, binary tree) TANPA melihat contoh dulu.",
                    "",
                    "TAHAP 2 - Perdalam Struktur Data & Algoritma:",
                    "  - Stack & Queue (pakai array atau linked list).",
                    "  - Binary Search Tree, Hash Table (implementasi manual).",
                    "  - Sorting & searching algorithm dari nol (quicksort, dll).",
                    "  - Kompleksitas: pahami Big O Notation untuk analisis performa.",
                ]
            },
            {
                "body": [
                    "TAHAP 3 - Pilih Jalur Spesialisasi:",
                    "  Systems Programming:",
                    "    - Pelajari Operating System concepts (proses, thread,",
                    "      memory management, file system).",
                    "    - Linux system programming (system call, POSIX API).",
                    "    - Kontribusi ke proyek open source C (Linux kernel,",
                    "      Git, Redis, SQLite - semua ditulis dalam C!).",
                    "  Embedded Systems:",
                    "    - Pemrograman microcontroller (Arduino, ARM, ESP32).",
                    "    - Memahami register, interrupt, dan real-time constraint.",
                    "    - Kata kunci wajibnya: volatile. Register hardware dan",
                    "      variabel yang diubah interrupt handler berubah TANPA",
                    "      sepengetahuan compiler, jadi tanpa volatile compiler",
                    "      berhak menyimpan nilainya di register dan tidak pernah",
                    "      membacanya ulang - programnya menggantung tanpa satu",
                    "      pun pesan galat. Lihat materi String Lanjutan: char *,",
                    "      const & Keluarga mem*.",
                    "  Bahasa Lanjutan:",
                    "    - C++ (perluasan C dengan OOP) - lihat menu C++ di aplikasi ini!",
                    "    - Rust - alternatif modern C dengan keamanan memori built-in.",
                ]
            },
            {
                "body": [
                    "TAHAP 4 - Kebiasaan Profesional:",
                    "  1. SELALU kompilasi dengan -Wall -Wextra, tangani semua warning.",
                    "  2. Rutin memakai valgrind/gdb untuk debug, bukan cuma printf().",
                    "  3. Gunakan Git untuk version control, biasakan commit rapi.",
                    "  4. Tulis Makefile untuk otomatisasi build project.",
                    "  5. Baca kode open source C berkualitas (Redis, SQLite - source",
                    "     code-nya relatif mudah dibaca untuk belajar gaya kode C yang baik).",
                    "",
                    "Kebiasaan harian agar handal:",
                    "  1. Ketik ulang semua contoh, JANGAN copy-paste - ketikan manual",
                    "     membantu otak mengenali pola sintaks secara refleks.",
                    "  2. Gambar diagram pointer/memori di kertas saat bingung -",
                    "     visualisasi SANGAT membantu memahami pointer.",
                    "  3. Selalu tanya: 'siapa yang bertanggung jawab free() memori",
                    "     ini?' setiap kali menulis kode dengan malloc().",
                    "  4. Debug bug SENDIRI dulu dengan gdb sebelum bertanya ke orang.",
                    "  5. Setelah C, C++ akan terasa jauh lebih masuk akal karena",
                    "     kamu sudah paham fondasi memori & pointer di baliknya.",
                ]
            },
            {
                "heading": "Yang sekarang bisa kamu kenali saat membuka berkas .c orang",
                "body": [
                    "Tolok ukur sesungguhnya bukan 'bisa menulis program', melainkan",
                    "'bisa membaca kode orang tanpa tersandung'. Berikut bentuk-bentuk",
                    "yang dulu terlihat seperti sihir, dan sekarang tidak lagi:",
                    "",
                    "  static int bantu(...)     fungsi yang SENGAJA disembunyikan,",
                    "                            hanya dipakai di dalam berkas itu",
                    "  goto cleanup;             satu-satunya goto yang diterima:",
                    "                            jalan keluar tunggal yang menutup",
                    "                            berkas dan mem-free semuanya",
                    "  uint32_t / size_t         tipe berukuran pasti, dan tipe resmi",
                    "                            untuk 'ukuran atau jumlah'",
                    "  struct T t = {.x = 1};    inisialisasi bernama - urutan field",
                    "                            tidak perlu diingat",
                    "  const char *pesan         pointer ke teks yang tidak boleh",
                    "                            diubah lewat pointer itu",
                    "  fprintf(stderr, ...)      pesan galat lewat jalur terpisah,",
                    "                            supaya tidak ikut kalau outputnya",
                    "                            dialihkan ke berkas",
                    "  extern \"C\" { ... }        pagar di header supaya pustaka C",
                    "                            ini juga bisa dipakai dari C++",
                    "  #ifdef __cplusplus        penjaga pagar itu - hanya compiler",
                    "                            C++ yang mendefinisikannya",
                    "  *dst++ = *src++;          menyalin sambil memajukan dua pointer",
                    "                            sekaligus; inilah isi strcpy",
                    "  volatile uint32_t *reg    register hardware: baca ulang dari",
                    "                            memori tiap kali, jangan dioptimasi",
                    "",
                    "Kalau daftar ini terbaca lancar, kamu sudah lewat dari 'belajar",
                    "sintaks C' ke 'membaca C'. Buka satu berkas .c dari proyek",
                    "sungguhan hari ini juga - SQLite atau Redis - dan buktikan",
                    "sendiri berapa banyak yang sudah masuk akal.",
                ]
            },
        ],
    },
]
