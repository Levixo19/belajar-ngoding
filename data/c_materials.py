C_MATERIALS = [
    {
        "title": "1. Pengenalan C & Instalasi",
        "sections": [
            {
                "body": [
                    "Apa itu C?",
                    "  - Bahasa pemrograman prosedural tingkat rendah-menengah.",
                    "  - Dibuat oleh Dennis Ritchie di Bell Labs, 1972.",
                    "  - Fondasi HAMPIR SEMUA bahasa modern (Java, Python, JS,",
                    "    C++, Go, Rust terinspirasi/terpengaruh sintaks C).",
                    "  - Dipakai untuk: sistem operasi (Linux/Windows kernel),",
                    "    embedded system, driver, database engine, compiler.",
                    "",
                    "Kenapa C penting dipelajari (walau 'tua'):",
                    "  - Mengajarkan cara kerja MEMORI komputer secara langsung.",
                    "  - Memahami C mempermudah belajar bahasa lain (semua konsep",
                    "    dasarnya berasal/mirip dari C).",
                    "  - Masih dipakai luas: Linux kernel, Python interpreter (CPython)",
                    "    sendiri ditulis dalam C!",
                    "",
                    "Instalasi compiler:",
                    "  - Linux: sudah ada gcc, atau install via 'sudo apt install gcc'",
                    "  - Windows: MinGW atau WSL (disarankan)",
                    "  - Mac: Xcode Command Line Tools (clang, kompatibel gcc)",
                    "  - Cek instalasi: gcc --version",
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
                    "Kompilasi & jalankan:",
                    "  gcc hello.c -o hello    (kompilasi jadi executable 'hello')",
                    "  ./hello                  (jalankan hasilnya)",
                    "",
                    "Penjelasan baris per baris:",
                    "  #include <stdio.h>  -> menyertakan library standar input/output.",
                    "  int main(void)       -> titik masuk WAJIB tiap program C.",
                    "      int  -> fungsi main mengembalikan kode status (angka).",
                    "      void -> tidak menerima parameter (bisa juga (int argc,",
                    "              char *argv[]) untuk menerima argumen command line).",
                    "  printf(\"...\")        -> mencetak teks ke layar.",
                    "  \\n                    -> karakter escape untuk baris baru.",
                    "  return 0;            -> mengembalikan status SUKSES ke sistem",
                    "                          operasi (0 = sukses, selain 0 = ada error).",
                    "  Setiap statement diakhiri titik koma (;).",
                    "  Blok kode ditandai kurung kurawal { }.",
                ]
            },
        ],
    },
    {
        "title": "2. Variabel & Tipe Data",
        "sections": [
            {
                "body": [
                    "C adalah bahasa STATICALLY TYPED: tipe variabel HARUS",
                    "dideklarasikan eksplisit SEBELUM dipakai, dan TIDAK bisa",
                    "berubah tipe setelah itu (beda dengan Python/JS).",
                    "",
                    "Tipe data dasar & ukurannya (bisa beda antar sistem,",
                    "gunakan sizeof() untuk memastikan di komputermu):",
                    "  char     1 byte    satu karakter ('A') atau angka kecil",
                    "  int      4 byte    bilangan bulat (paling umum)",
                    "  float    4 byte    bilangan desimal presisi tunggal",
                    "  double   8 byte    bilangan desimal presisi ganda",
                    "  short    2 byte    bilangan bulat lebih kecil dari int",
                    "  long     8 byte    bilangan bulat lebih besar dari int",
                    "  _Bool    1 byte    true/false (perlu #include <stdbool.h>",
                    "                     agar bisa pakai 'bool', 'true', 'false')",
                    "",
                    "Deklarasi variabel: tipeData namaVariabel = nilai;",
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
                    "Format specifier printf/scanf (WAJIB sesuai tipe data):",
                    "  %d   -> int              %f   -> float/double",
                    "  %c   -> char              %s   -> string (char array)",
                    "  %ld  -> long              %lf  -> double (khusus scanf)",
                    "  %u   -> unsigned int      %x   -> hexadecimal",
                    "  %zu  -> size_t (hasil sizeof)",
                    "",
                    "Konstanta: pakai keyword 'const' atau '#define'.",
                    "  const double PI = 3.14159;   // const: type-checked, disarankan",
                    "  #define MAX_SIZE 100          // macro: text replacement (materi 16)",
                    "",
                    "Konversi tipe (casting):",
                    "  int x = (int) 3.99;    // x = 3 (dibulatkan ke bawah/truncate)",
                    "  double y = (double) 7 / 2;   // y = 3.5 (paksa pembagian desimal)",
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
                    "  +  -  *  /  %  (sama seperti Java)",
                    "  ++ increment   -- decrement",
                    "",
                    "PENTING - pembagian integer:",
                    "  7 / 2   = 3     (int / int = int, sisa dibuang, SAMA seperti Java)",
                    "  7.0 / 2 = 3.5   (salah satu double, hasil desimal)",
                    "  7 % 2   = 1     (sisa bagi, HANYA untuk tipe integer)",
                    "",
                    "Operator penugasan: =, +=, -=, *=, /=, %=",
                    "",
                    "Operator perbandingan: ==, !=, >, <, >=, <=",
                    "Operator logika: && (AND), || (OR), ! (NOT)",
                    "  -- SAMA PERSIS dengan Java, beda dengan Python yang pakai kata --",
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
                    "Kapan operator bitwise dipakai:",
                    "  - Manipulasi flag/bit dalam programming embedded/sistem.",
                    "  - Optimasi (geser bit lebih cepat dari kali/bagi untuk pangkat 2).",
                    "  - Bekerja dengan hardware register secara langsung.",
                    "  - JARANG dipakai di aplikasi level tinggi sehari-hari.",
                ]
            },
        ],
    },
    {
        "title": "4. Input & Output (printf & scanf)",
        "sections": [
            {
                "body": [
                    "printf() -> menampilkan output ke layar.",
                    "scanf()  -> membaca input dari keyboard.",
                    "",
                    "PENTING: scanf() untuk tipe NON-string butuh operator",
                    "ALAMAT (&) di depan nama variabel!",
                    "  scanf(\"%d\", &umur);     // & WAJIB untuk int, float, dll",
                    "  scanf(\"%s\", nama);      // TANPA & untuk array/string (nama",
                    "                            SUDAH berupa alamat, materi 10-11)",
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
                    "PERHATIAN: scanf(\"%s\", ...) berhenti di SPASI PERTAMA,",
                    "sehingga TIDAK BISA membaca nama dengan spasi ('Andi Wijaya'",
                    "hanya akan terbaca 'Andi'). Untuk membaca SATU BARIS PENUH",
                    "termasuk spasi, gunakan fgets():",
                    "",
                    "  char nama[50];",
                    "  printf(\"Nama lengkap: \");",
                    "  fgets(nama, sizeof(nama), stdin);",
                    "  // fgets menyertakan karakter newline (\\n) di akhir,",
                    "  // sering perlu dibersihkan manual jika mengganggu.",
                    "",
                    "printf format lanjutan:",
                    "  %5d   -> tampilkan angka rata kanan, lebar minimal 5 karakter",
                    "  %-5d  -> rata kiri, lebar minimal 5",
                    "  %05d  -> isi dengan nol di depan jika kurang dari 5 digit",
                    "  %.2f  -> desimal dibulatkan 2 angka di belakang koma",
                ]
            },
        ],
    },
    {
        "title": "5. Percabangan (if / else / switch)",
        "sections": [
            {
                "body": [
                    "Sintaks if-else di C IDENTIK dengan Java:",
                    "  if (kondisi) {",
                    "      // jalankan jika true",
                    "  } else if (kondisi2) {",
                    "      // jalankan jika kondisi2 true",
                    "  } else {",
                    "      // jalankan jika semua false",
                    "  }",
                    "",
                    "PERBEDAAN PENTING dari bahasa modern: C (sebelum C99/C23)",
                    "TIDAK punya tipe boolean asli - kondisi dianggap:",
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
                    "PENTING: switch di C (SAMA seperti Java) butuh 'break;' di",
                    "tiap case, KALAU TIDAK akan 'fall-through' (lanjut ke case",
                    "berikutnya tanpa cek kondisi lagi) - ini SERING jadi bug pemula.",
                    "",
                    "switch HANYA bisa dipakai untuk tipe integer (int, char, enum),",
                    "TIDAK BISA untuk float/double atau string (berbeda dari",
                    "bahasa modern seperti JS yang punya switch string).",
                ]
            },
        ],
    },
    {
        "title": "6. Perulangan (for, while, do-while)",
        "sections": [
            {
                "body": [
                    "Sintaks loop C IDENTIK dengan Java (Java memang mewarisi dari C):",
                    "",
                    "  for (awal; kondisi; update) { ... }",
                    "  while (kondisi) { ... }",
                    "  do { ... } while (kondisi);   // pasti jalan minimal 1x",
                    "",
                    "break    -> menghentikan loop sepenuhnya.",
                    "continue -> lompat ke iterasi berikutnya.",
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
        "title": "7. Array",
        "sections": [
            {
                "body": [
                    "Array C = blok memori BERURUTAN dengan UKURAN TETAP",
                    "(harus ditentukan saat kompilasi untuk array statis).",
                    "SEMUA elemen HARUS bertipe SAMA.",
                    "",
                    "  int angka[5];                  // 5 int, isi awal 'sampah' (undefined)",
                    "  int angka[5] = {1, 2, 3, 4, 5}; // langsung dengan nilai",
                    "  int angka[] = {1, 2, 3};        // ukuran otomatis dari jumlah elemen",
                    "",
                    "Mengakses elemen (indeks dari 0, SAMA seperti Java):",
                    "  angka[0] -> elemen pertama",
                    "  angka[4] -> elemen terakhir (untuk array ukuran 5)",
                    "",
                    "BAHAYA BESAR: C TIDAK melakukan bounds-checking!",
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
                    "PENTING: sizeof(nilai)/sizeof(nilai[0]) HANYA bekerja untuk",
                    "array yang dideklarasikan LANGSUNG (bukan hasil malloc atau",
                    "yang diterima sebagai parameter fungsi - dibahas di materi",
                    "pointer, karena array 'meluruh' jadi pointer saat dikirim",
                    "sebagai parameter fungsi).",
                ]
            },
        ],
    },
    {
        "title": "8. String (Array of Char)",
        "sections": [
            {
                "body": [
                    "C TIDAK punya tipe 'string' asli seperti Java/Python -",
                    "string di C adalah ARRAY OF CHAR yang diakhiri karakter",
                    "NULL TERMINATOR ('\\0') sebagai penanda 'akhir string'.",
                    "",
                    "  char nama[] = \"Andi\";",
                    "  // Sebenarnya tersimpan sebagai: {'A','n','d','i','\\0'}",
                    "  // Perhatikan array butuh 5 slot untuk 4 huruf + '\\0'!",
                    "",
                    "  char nama2[20] = \"Budi\";   // ukuran cukup, sisanya kosong",
                    "  char nama3[3] = \"Budi\";    // BAHAYA! 'Budi'+'\\0' butuh 5,",
                    "                              // hanya ada 3 slot -> buffer overflow!",
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
                    "PERINGATAN KERAS soal string di C:",
                    "  1. strcpy/strcat TIDAK cek ukuran tujuan - MUDAH overflow!",
                    "     Disarankan pakai strncpy/strncat (versi 'aman' dengan",
                    "     batas panjang) di kode production.",
                    "  2. LUPA menambah ruang untuk '\\0' adalah bug KLASIK pemula.",
                    "  3. Membandingkan string HARUS pakai strcmp(), BUKAN ==",
                    "     (== membandingkan ALAMAT array, bukan ISI-nya - mirip",
                    "     masalah 'is' vs '==' di Python/Java tapi lebih parah di C).",
                    "",
                    "Fungsi string.h lain yang berguna:",
                    "  strlen(s), strcpy(dst,src), strncpy(dst,src,n),",
                    "  strcat(dst,src), strcmp(a,b), strchr(s,c), strstr(s,sub)",
                ]
            },
        ],
    },
    {
        "title": "9. Function (Fungsi)",
        "sections": [
            {
                "body": [
                    "Sintaks function C:",
                    "  tipeKembali namaFungsi(parameter) {",
                    "      // isi fungsi",
                    "      return nilai;   // jika tipeKembali bukan void",
                    "  }",
                    "",
                    "PENTING: C (secara tradisional) butuh fungsi DIDEKLARASIKAN",
                    "atau DIDEFINISIKAN SEBELUM dipakai/dipanggil - beda dengan",
                    "Java yang bisa panggil method di mana saja dalam class.",
                    "  - Solusi: taruh 'function prototype' (deklarasi tanpa isi)",
                    "    di atas, definisi lengkapnya boleh di bawah main().",
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
                    "PENTING - Pass by Value (default C):",
                    "  Parameter fungsi C dikirim sebagai SALINAN (copy) nilainya,",
                    "  BUKAN variabel aslinya. Mengubah parameter DI DALAM fungsi",
                    "  TIDAK memengaruhi variabel ASLI di luar fungsi:",
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
                    "  Untuk BENAR-BENAR mengubah variabel asli, HARUS mengirim",
                    "  ALAMAT-nya (pointer) - inilah topik materi berikutnya,",
                    "  konsep PALING PENTING & mendasar di bahasa C.",
                ]
            },
        ],
    },
    {
        "title": "10. Pointer Dasar",
        "sections": [
            {
                "body": [
                    "Pointer = variabel yang menyimpan ALAMAT MEMORI dari",
                    "variabel lain, BUKAN nilai itu sendiri. Ini adalah",
                    "KONSEP PALING PENTING & PALING KHAS dari bahasa C.",
                    "",
                    "Dua operator kunci:",
                    "  &  (address-of)   -> mendapatkan ALAMAT sebuah variabel.",
                    "  *  (dereference)  -> mengakses NILAI yang ditunjuk pointer.",
                    "",
                    "  int angka = 10;",
                    "  int *ptr = &angka;   // ptr menyimpan ALAMAT dari 'angka'",
                    "",
                    "  *ptr sekarang berarti 'nilai yang ditunjuk ptr' -> 10",
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
                    "NULL pointer: pointer yang TIDAK menunjuk ke mana pun.",
                    "  int *ptr = NULL;   // praktik AMAN, bukan alamat acak",
                    "  if (ptr != NULL) { ... }   // SELALU cek sebelum dereference!",
                    "  *ptr;   // JIKA ptr NULL, ini CRASH (segmentation fault)!",
                    "",
                    "Ukuran pointer SELALU SAMA di sistem yang sama (biasanya",
                    "8 byte di sistem 64-bit) TIDAK PEDULI tipe data yang ditunjuk -",
                    "yang beda adalah bagaimana compiler MENAFSIRKAN data di alamat itu.",
                ]
            },
        ],
    },
    {
        "title": "11. Pointer & Array: Hubungan Erat Keduanya",
        "sections": [
            {
                "body": [
                    "Fakta PENTING: nama array SEBENARNYA adalah pointer ke",
                    "elemen PERTAMA-nya. Inilah kenapa pointer & array sangat",
                    "erat hubungannya di C.",
                    "",
                    "  int angka[] = {10, 20, 30};",
                    "  int *ptr = angka;      // SAMA dengan: int *ptr = &angka[0];",
                    "",
                    "  angka[0]   SAMA DENGAN   *(angka + 0)   SAMA DENGAN   *angka",
                    "  angka[1]   SAMA DENGAN   *(angka + 1)",
                    "  angka[i]   SAMA DENGAN   *(angka + i)",
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
        ],
    },
    {
        "title": "12. Dynamic Memory Allocation (malloc, calloc, free)",
        "sections": [
            {
                "body": [
                    "Array biasa punya ukuran TETAP (ditentukan saat kompilasi).",
                    "Dynamic memory allocation memungkinkan alokasi memori",
                    "SAAT PROGRAM BERJALAN (runtime), dengan ukuran yang bisa",
                    "ditentukan berdasarkan input pengguna.",
                    "",
                    "Fungsi dari <stdlib.h>:",
                    "  malloc(ukuran)         -> alokasi memori mentah (isi 'sampah')",
                    "  calloc(jumlah, ukuran)  -> alokasi + otomatis diisi NOL",
                    "  realloc(ptr, ukuranBaru)-> ubah ukuran alokasi yang sudah ada",
                    "  free(ptr)               -> KEMBALIKAN memori ke sistem (WAJIB!)",
                    "",
                    "ATURAN EMAS: SETIAP malloc/calloc HARUS diikuti free() yang",
                    "sesuai. Lupa free() = MEMORY LEAK (kebocoran memori).",
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
                "body": [
                    "Bug klasik terkait dynamic memory (SERING ditanya saat",
                    "wawancara kerja & jadi sumber CRASH aplikasi C/C++):",
                    "",
                    "  1. Memory leak: lupa free() -> memori 'bocor' terus",
                    "     menumpuk selama program berjalan.",
                    "  2. Dangling pointer: pakai pointer SETELAH di-free().",
                    "     int *p = malloc(...); free(p); *p = 5; // BAHAYA!",
                    "  3. Double free: memanggil free() DUA KALI pada pointer",
                    "     yang sama -> undefined behavior, sering crash.",
                    "  4. Buffer overflow: menulis di luar batas alokasi.",
                    "",
                    "Tools untuk mendeteksi bug memori (dibahas di materi 20):",
                    "  valgrind ./program   -> mendeteksi memory leak & akses ilegal",
                ]
            },
        ],
    },
    {
        "title": "13. Struct",
        "sections": [
            {
                "body": [
                    "Struct = tipe data KUSTOM yang menggabungkan beberapa",
                    "variabel (bisa beda tipe) jadi SATU unit. Ini adalah",
                    "'cikal bakal' konsep class di bahasa OOP (Java, C++, dll).",
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
        "title": "14. Union & Enum",
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
        "title": "15. File I/O",
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
                ]
            },
        ],
    },
    {
        "title": "16. Preprocessor & Macro",
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
                ]
            },
        ],
    },
    {
        "title": "17. Function Pointer",
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
        "title": "18. Linked List: Struktur Data Dinamis",
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
        "title": "19. Kompilasi Multi-File & Header (.h)",
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
                    "  \ttgcc main.c matematika.c -o program",
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
        ],
    },
    {
        "title": "20. Debugging: gdb, valgrind & Bug Umum",
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
        ],
    },
    {
        "title": "21. Roadmap Menjadi C Programmer Handal",
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
        ],
    },
]
