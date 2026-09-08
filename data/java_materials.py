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
            {
                "body": [
                    "ANGKA VERSI JAVA, dan kenapa kode di dua repo bisa terlihat sangat berbeda.",
                    "",
                    "Java terus bertambah fitur, tapi tidak semua versi dipakai orang. Yang dipilih",
                    "proyek nyata adalah versi LTS (Long Term Support) - versi yang ditambal",
                    "bertahun-tahun sesudah rilis:",
                    "",
                    "  8    warisan. Masih banyak sekali di proyek lama. Sudah punya lambda & Stream.",
                    "  11   LTS pertama sesudah 8. Sudah punya var dan 'java Berkas.java'.",
                    "  17   LTS yang paling umum sekarang. Sudah punya record, sealed, text block.",
                    "  21   LTS terbaru. Pattern matching di switch, virtual thread.",
                    "",
                    "Versi di antaranya (9, 10, 12-16, 18-20, ...) tetap rilis, cuma umur dukungannya",
                    "pendek, jadi jarang jadi pilihan proyek.",
                    "",
                    "Cek punyamu:",
                    "",
                    "  java -version",
                    "  openjdk version \"17.0.16\" 2025-07-15",
                    "                  ^^ ini yang penting: JDK-mu versi 17.",
                    "",
                    "Gunanya angka ini praktis. Saat kamu menyalin kode dari internet lalu javac",
                    "menolaknya dengan kata 'preview feature' atau 'illegal start of expression',",
                    "sering bukan kodenya yang salah - JDK-mu yang lebih tua daripada fitur itu.",
                    "Nanti kamu akan bertemu var (butuh 10), switch bentuk panah (butuh 14), dan",
                    "record (butuh 16); tiap kali muncul, angkanya ikut disebut supaya kamu tahu",
                    "batas bawahnya.",
                    "",
                    "Satu keringanan sejak Java 11: berkas TUNGGAL boleh dijalankan tanpa javac.",
                    "",
                    "  java Hello.java     // langsung jalan, tidak ada Hello.class yang tertinggal",
                    "",
                    "Praktis untuk mencoba potongan kecil. Begitu programmu terdiri dari lebih dari",
                    "satu berkas, kembali ke javac lalu java seperti langkah di atas.",
                ]
            },
        ],
    },
    {
        "title": "2. Anatomi Berkas Java: package, import, dan komentar",
        "sections": [
            {
                "body": [
                    "Kamu sudah menulis class dan method main di materi sebelumnya. Yang belum pernah",
                    "dijelaskan adalah SISA kepala berkasnya - baris-baris di ATAS class. Padahal",
                    "justru itu yang pertama dilihat matamu tiap kali membuka kode orang lain.",
                    "",
                    "Baris pertama hampir setiap berkas Java di dunia nyata:",
                    "",
                    "  package com.tokobuku.penjualan;",
                    "",
                    "Package = folder tempat sebuah class tinggal, sekaligus bagian dari nama aslinya.",
                    "Nama lengkap class di atas bukan 'Keranjang', melainkan",
                    "'com.tokobuku.penjualan.Keranjang'. Itu disebut nama berkualifikasi penuh (fully",
                    "qualified name), dan itulah nama yang benar-benar dipakai Java di dalam.",
                    "",
                    "Tiga aturan package yang tidak bisa ditawar:",
                    "  1. Deklarasi package WAJIB jadi baris KODE pertama di berkas. Hanya komentar",
                    "     yang boleh berada di atasnya.",
                    "  2. Nama package harus PERSIS mengikuti susunan folder:",
                    "       package com.tokobuku.penjualan;",
                    "       -> berkasnya duduk di  com/tokobuku/penjualan/Keranjang.java",
                    "     Kalau foldernya tidak cocok, javac sering masih mau jalan, tapi perintah",
                    "     'java' menolak dengan pesan seperti:",
                    "       wrong name: com/tokobuku/penjualan/Keranjang",
                    "     Ini saudara kandung aturan 'nama berkas = nama class public'.",
                    "  3. Semua huruf kecil, dipisah titik, tanpa garis bawah. 'com.TokoBuku' lolos",
                    "     compiler tapi praktis tidak pernah ditulis siapa pun.",
                    "",
                    "Kenapa dibalik jadi com.tokobuku? Karena nama domain (tokobuku.com) sudah dijamin",
                    "unik sedunia. Membaliknya membuat package-mu ikut unik tanpa perlu ada panitia",
                    "yang mengatur siapa boleh memakai nama apa.",
                    "",
                    "Berkas TANPA baris package masuk ke 'default package'. Semua contoh kode di",
                    "aplikasi ini memakainya supaya bisa langsung dijalankan dengan javac/java polos.",
                    "Di proyek sungguhan itu nyaris tidak pernah terjadi: class di default package",
                    "tidak bisa diimpor dari package mana pun.",
                    "",
                    "Susunan folder yang akan kamu temui di hampir semua proyek Java:",
                    "",
                    "  proyek-toko/",
                    "    pom.xml                 <- daftar library & konfigurasi build (Maven)",
                    "    src/",
                    "      main/",
                    "        java/               <- KODE PROGRAM ada di bawah sini",
                    "          com/tokobuku/penjualan/",
                    "            Keranjang.java",
                    "            Faktur.java",
                    "        resources/          <- bukan kode: gambar, berkas konfigurasi, template",
                    "      test/",
                    "        java/               <- KODE TES, package-nya sengaja SAMA",
                    "          com/tokobuku/penjualan/",
                    "            KeranjangTest.java",
                    "    target/                 <- hasil kompilasi (.class, .jar). Jangan di-commit.",
                    "",
                    "Kenapa kode dan tes dipisah jadi dua pohon padahal package-nya sama?",
                    "  - Yang dikirim ke pengguna hanya isi src/main. Tes tidak ikut masuk ke .jar.",
                    "  - Tapi karena package-nya sama, tes tetap boleh menyentuh method yang tidak",
                    "    public - hak istimewa yang tidak dimiliki kode dari package lain.",
                    "  - Gradle memakai susunan yang sama persis, cuma folder hasilnya bernama build/.",
                    "  - Melihat src/main/java saja kamu sudah tahu: ini proyek Java bergaya Maven.",
                ],
            },
            {
                "body": [
                    "Sesudah package datang blok import. Ini bagian yang paling sering disalahpahami:",
                    "import BUKAN 'memuat' atau 'menyalin' kode ke berkasmu. Semua class yang tersedia",
                    "sudah tersedia, mau diimpor atau tidak. Yang dilakukan import cuma satu hal:",
                    "memberi izin menulis NAMA PENDEK sebagai ganti nama berkualifikasi penuh.",
                    "",
                    "Dua baris ini identik di mata compiler:",
                    "",
                    "  java.util.ArrayList<String> a = new java.util.ArrayList<>();  // tanpa import",
                    "  ArrayList<String> a = new ArrayList<>();                      // dengan import",
                    "",
                    "Bentuk import yang akan kamu temui:",
                    "",
                    "  import java.util.ArrayList;",
                    "      Satu class, satu baris. Paling jelas dibaca, dan inilah yang ditulis",
                    "      otomatis oleh IDE.",
                    "",
                    "  import java.util.*;",
                    "      Wildcard: semua class yang LANGSUNG ada di java.util. Tidak menjangkau",
                    "      sub-package - java.util.function tetap harus diimpor sendiri. Praktis di",
                    "      contoh singkat, dihindari di proyek tim karena menyembunyikan asal-usul",
                    "      nama dan gampang memicu tabrakan.",
                    "",
                    "  import static java.lang.Math.max;",
                    "      Impor STATIC. Yang dibawa bukan nama class, melainkan nama member",
                    "      static-nya, sehingga 'Math.' boleh dihilangkan: cukup tulis max(a, b).",
                    "      Bentuk yang sama muncul sebagai import static ...Assertions.*; di setiap",
                    "      berkas tes JUnit - itu sebabnya assertEquals(...) di sana bisa ditulis",
                    "      polos tanpa nama class di depannya.",
                    "",
                    "Kenapa String, System, Math, Integer, dan Object tidak pernah diimpor?",
                    "Karena semuanya penghuni package java.lang, dan java.lang diimpor OTOMATIS untuk",
                    "setiap berkas Java. Itu satu-satunya package yang diperlakukan istimewa begitu.",
                    "",
                    "Tabrakan nama - dan kenapa blok import layak dibaca, bukan dilewati:",
                    "  - Di JDK ada DUA class bernama List: java.util.List (koleksi data) dan",
                    "    java.awt.List (komponen daftar di jendela aplikasi desktop). Beda total.",
                    "  - Melihat tulisan 'List' di tengah berkas tidak cukup untuk tahu yang mana.",
                    "    Yang menentukan artinya adalah baris import di kepala berkas.",
                    "  - Menulis 'import java.util.*;' DAN 'import java.awt.*;' sekaligus lalu memakai",
                    "    'List' membuat compiler menolak: reference to List is ambiguous.",
                    "  - Java tidak punya cara mengganti nama saat impor (tidak ada 'import ... as ...'",
                    "    seperti di Python). Kalau dua class bernama sama sama-sama dibutuhkan, yang",
                    "    lazim dilakukan: impor salah satunya, tulis yang lain dengan nama panjangnya.",
                    "",
                    "      import java.util.List;",
                    "      List<String> data = new ArrayList<>();             // ini java.util.List",
                    "      java.awt.List daftarLayar = new java.awt.List();   // yang ini ditulis penuh",
                ],
            },
            {
                "heading": "Program kecil: apa yang sebenarnya dikerjakan import",
                "code": """import java.util.ArrayList;
import java.util.List;

import static java.lang.Math.max;

/** Contoh kecil: apa yang sebenarnya dikerjakan sebuah baris import. */
public class Impor {

    // Konstanta ditulis HURUF_BESAR_DENGAN_GARIS_BAWAH. Lihat namanya, langsung tahu.
    static final int STOK_AWAL = 10;

    public static void main(String[] args) {
        // 'List' boleh ditulis pendek karena sudah diimpor di baris paling atas.
        List<String> keranjang = new ArrayList<>();
        keranjang.add("Kopi");
        keranjang.add("Teh");
        System.out.println(keranjang);          // [Kopi, Teh]

        /* Tanpa import, nama panjangnya tetap sah - cuma lebih capek dibaca.
           Persis inilah yang dipendekkan oleh baris import. */
        java.math.BigDecimal harga = new java.math.BigDecimal("12500.00");
        System.out.println(harga);              // 12500.00

        // String dan System tidak pernah diimpor: keduanya penghuni java.lang.
        System.out.println("Sisa stok: " + max(STOK_AWAL - keranjang.size(), 0));

        // Impor static membawa nama METHOD-nya, jadi 'Math.' boleh hilang.
        System.out.println(Math.max(2, 9) == max(2, 9));   // true
    }
}""",
            },
            {
                "heading": "Kepala berkas Java sungguhan (potongan, bukan program utuh)",
                "code": """package com.tokobuku.penjualan;

import java.util.ArrayList;
import java.util.List;

/**
 * Menyimpan barang yang dibeli satu pelanggan dalam satu transaksi.
 *
 * @author Levi
 */
public class Keranjang {

    /** Batas jumlah barang yang boleh masuk sekali belanja. */
    public static final int BATAS_BARANG = 20;

    private final List<String> barang = new ArrayList<>();

    /**
     * Menambahkan satu barang ke keranjang.
     *
     * @param nama nama barang yang dibeli, tidak boleh kosong
     * @return true kalau barangnya berhasil masuk
     * @throws IllegalStateException kalau isinya sudah mencapai {@link #BATAS_BARANG}
     */
    public boolean tambah(String nama) {
        if (barang.size() >= BATAS_BARANG) {
            throw new IllegalStateException("Keranjang penuh");
        }
        return barang.add(nama);
    }
}""",
            },
            {
                "body": [
                    "Bedah kepala berkas di atas, baris per baris:",
                    "  package com.tokobuku.penjualan;    berkasnya duduk di com/tokobuku/penjualan/.",
                    "  import java.util.ArrayList;        izin menulis 'ArrayList' tanpa nama panjang.",
                    "  import java.util.List;             'List' di berkas ini = java.util.List.",
                    "  /** ... */ di atas class           Javadoc: dokumentasi, bukan perintah.",
                    "  public class Keranjang             class public -> berkasnya WAJIB Keranjang.java.",
                    "  public static final int BATAS_...  konstanta; ditandai huruf besar semua.",
                    "  private final List<String> barang  data internal, tidak bisa disentuh dari luar.",
                    "  public boolean tambah(String nama) method publik; inilah yang dipakai orang lain.",
                    "",
                    "Blok ini sengaja bukan program utuh: tidak ada method main, dan karena ada baris",
                    "package, ia hanya bisa dikompilasi kalau foldernya sudah disusun benar.",
                    "",
                    "Tiga bentuk komentar - compiler MENGABAIKAN ketiganya, sepenuhnya:",
                    "  // ...      komentar satu baris, berlaku sampai ujung baris itu saja.",
                    "  /* ... */   komentar beberapa baris, berhenti tepat di penutupnya.",
                    "  /** ... */  Javadoc: bentuk khusus /* */ yang dibaca alat pembuat dokumentasi.",
                    "",
                    "Jebakan pemula yang nyata. Di contoh-contoh materi ini sering muncul:",
                    "",
                    "  System.out.println(a % b);   // 1",
                    "",
                    "Angka '1' itu BUKAN perintah dan tidak dicetak oleh siapa pun. Itu catatan manusia",
                    "yang memberi tahu hasil yang akan muncul. Hapus semua komentarnya, programnya",
                    "tetap berjalan sama persis - itulah bukti bahwa komentar tidak dieksekusi.",
                    "",
                    "Tag Javadoc yang akan kamu lihat terus-menerus:",
                    "  @param nama           menjelaskan satu parameter method.",
                    "  @return               menjelaskan nilai yang dikembalikan.",
                    "  @throws Exception     menjelaskan kapan method melempar exception itu.",
                    "  @author               siapa penulisnya.",
                    "  {@link Kelas#member}  tautan ke bagian lain dokumentasi; dipakai di TENGAH",
                    "                        kalimat, bukan sebagai baris tersendiri.",
                    "Perintah 'javadoc' mengubah semua itu jadi halaman HTML, dan IDE menampilkannya",
                    "sebagai tooltip saat kursormu berhenti di atas nama method.",
                    "",
                    "PERINGATAN yang paling sering menjebak: tanda @ di DALAM /** */ hanyalah teks.",
                    "@Override, @Test, @BeforeEach yang ditulis di LUAR komentar adalah ANOTASI, dan",
                    "anotasi betul-betul mempengaruhi program - dicek compiler, dibaca framework.",
                    "Pembedanya cuma satu: berada di dalam /** */ atau tidak. Salah membaca ini bikin",
                    "orang mengira dokumentasi bisa mengubah perilaku, dan sebaliknya mengira @Override",
                    "boleh dihapus tanpa akibat.",
                    "",
                    "Konvensi penamaan - pakai sebagai ALAT BACA, bukan sekadar aturan sopan santun.",
                    "Dari bentuk namanya saja kamu sudah tahu benda itu apa:",
                    "",
                    "  Bentuk                          Artinya                             Contoh",
                    "  -----------------------------   ---------------------------------   -----------------",
                    "  PascalCase                      tipe: class/interface/enum/record   Keranjang",
                    "  camelCase                       variabel atau method                totalHarga",
                    "  HURUF_BESAR_DENGAN_GARIS_BAWAH  konstanta (static final)            BATAS_BARANG",
                    "  huruf kecil dipisah titik       package                             com.tokobuku",
                    "",
                    "Akhiran nama yang menandai peran. Ini yang membuatmu paham struktur sebuah proyek",
                    "asing sebelum membuka satu berkas pun:",
                    "  XxxTest        unit test untuk Xxx (dibahas di materi Unit Testing dengan JUnit)",
                    "  XxxService     logika bisnis: menghitung, memutuskan, mengatur alur",
                    "  XxxRepository  urusan simpan-ambil data (database, berkas)",
                    "  XxxController  pintu masuk permintaan dari luar, misalnya dari web",
                    "  XxxException   exception buatan sendiri",
                    "  XxxUtils       kumpulan method static pembantu, biasanya tanpa objek",
                    "  XxxImpl        implementasi konkret dari interface bernama Xxx",
                    "",
                    "Tidak satu pun dari akhiran itu dipaksakan compiler. Tapi dipatuhi begitu luas",
                    "sampai melanggarnya membuat kodemu terasa asing bagi pembaca berikutnya - dan",
                    "pembaca berikutnya biasanya kamu sendiri, tiga bulan lagi.",
                ],
            },
        ],
    },
    {
        "title": "3. Variabel & Tipe Data",
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
                    "Dua tanda kutip di contoh itu TIDAK boleh tertukar:",
                    "",
                    "  'A'   kutip TUNGGAL -> char, tepat satu karakter.",
                    "  \"A\"   kutip GANDA   -> String, teks berisi berapa pun karakter.",
                    "  'AB'  ERROR: unclosed character literal (char cuma muat satu).",
                    "  \"\"    String kosong - sah. char kosong tidak ada.",
                    "",
                    "Lalu bagaimana menulis karakter yang tidak bisa diketik, misalnya tombol Enter?",
                    "Java memakai escape sequence: garis miring terbalik (backslash) plus satu huruf.",
                    "Gabungan itu dihitung SATU karakter, bukan dua.",
                    "",
                    "  \\n   baris baru (Enter)        \\t   tab",
                    "  \\\"   tanda kutip ganda di dalam String",
                    "  \\'   tanda kutip tunggal di dalam char",
                    "  \\\\   satu backslash sungguhan",
                    "",
                    "  System.out.println(\"Baris1\\nBaris2\");",
                    "      Baris1",
                    "      Baris2",
                    "",
                    "  System.out.println(\"Dia bilang \\\"halo\\\"\");  ->  Dia bilang \"halo\"",
                    "  System.out.println(\"C:\\\\Users\\\\Levi\");       ->  C:\\Users\\Levi",
                    "  char br = '\\n';   // SATU char, nilainya 10",
                    "",
                    "Di dalam kutip, backslash tidak pernah berarti dirinya sendiri. Menulis alamat",
                    "folder Windows sebagai \"C:\\Users\" ditolak compiler dengan pesan illegal escape",
                    "character, karena \\U bukan escape yang dikenal. Yang benar dua backslash.",
                ]
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
        "title": "4. Kelas Pembungkus & Konversi Tipe",
        "sections": [
            {
                "body": [
                    "Materi sebelumnya memperkenalkan tipe primitif: int, double, char,",
                    "boolean, dan kawan-kawan. Java menyediakan pasangan OBJEK untuk setiap",
                    "primitif itu, namanya kelas pembungkus (wrapper class). Delapan",
                    "primitif, delapan pembungkus, berpasangan satu-satu:",
                    "",
                    "  Primitif   Pembungkus     Primitif   Pembungkus",
                    "  --------   ----------     --------   ----------",
                    "  int        Integer        float      Float",
                    "  double     Double         short      Short",
                    "  long       Long           byte       Byte",
                    "  char       Character      boolean    Boolean",
                    "",
                    "Dua nama tidak sekadar berubah huruf besar: int -> Integer dan",
                    "char -> Character. Menulis Int atau Char langsung ditolak compiler.",
                    "",
                    "Kenapa Java repot menyediakan dua-duanya?",
                    "",
                    "  1. Generic, koleksi, dan Optional hanya bisa menampung OBJEK.",
                    "       List<int> daftar;       // ERROR, tidak akan dikompilasi",
                    "       List<Integer> daftar;   // benar",
                    "     Inilah sebabnya di materi Collection Framework, Generics, dan",
                    "     Optional kamu selalu melihat List<Integer> atau",
                    "     Map<String, Integer>, dan tidak pernah List<int>.",
                    "",
                    "  2. Pembungkus bisa bernilai null; primitif tidak pernah bisa.",
                    "       Integer nilaiUjian;   // default null -> 'belum diisi'",
                    "       int absen;            // default 0    -> 'belum diisi' dan",
                    "                             //                 nol tak terbedakan",
                    "",
                    "  3. Pembungkus membawa method dan konstanta bawaan: Integer.parseInt",
                    "     untuk mengubah teks jadi angka, Integer.MAX_VALUE untuk batasnya.",
                    "",
                    "Dua istilah yang akan terus kamu dengar:",
                    "  - Autoboxing : primitif dibungkus otomatis jadi objek (int -> Integer).",
                    "  - Unboxing   : kebalikannya, objek dibuka jadi primitif.",
                    "Keduanya terjadi diam-diam tanpa kamu menulis apa pun. Justru karena",
                    "tak terlihat itulah dua jebakan di bagian bawah materi ini sanggup",
                    "menipu orang yang sudah berpengalaman sekalipun.",
                ],
            },
            {
                "heading": "Bolak-balik antara primitif, pembungkus, dan teks",
                "code": """public class Main {
    public static void main(String[] args) {
        // Autoboxing: int -> Integer, terjadi otomatis
        int angka = 42;
        Integer kotak = angka;

        // Unboxing: Integer -> int, juga otomatis
        int kembali = kotak;
        System.out.println(kotak + " " + kembali);      // 42 42

        // Teks -> angka
        int umur = Integer.parseInt("20");
        double harga = Double.parseDouble("15000.5");
        long saldo = Long.parseLong("9000000000");
        boolean aktif = Boolean.parseBoolean("true");
        System.out.println(umur + 1);                   // 21
        System.out.println(harga * 2);                  // 30001.0
        System.out.println(saldo);                      // 9000000000
        System.out.println(aktif);                      // true

        // Angka -> teks (tiga cara yang sama-sama benar)
        System.out.println(String.valueOf(umur));       // 20
        System.out.println(Integer.toString(umur));     // 20
        System.out.println("" + umur);                  // 20

        // Teks yang bukan angka: program berhenti kalau tidak ditangkap
        try {
            Integer.parseInt("20 tahun");
        } catch (NumberFormatException e) {
            System.out.println("Gagal baca: " + e.getMessage());
        }
    }
}""",
            },
            {
                "body": [
                    "Tanpa parseInt kamu buntu begitu angkanya datang bukan dari Scanner:",
                    "argumen baris perintah (String[] args), isi berkas, dan data JSON",
                    "semuanya sampai ke programmu sebagai teks. Yang perlu kamu tahu:",
                    "",
                    "  - parseX mengembalikan PRIMITIF, valueOf mengembalikan PEMBUNGKUS.",
                    "      int a = Integer.parseInt(\"20\");      // int",
                    "      Integer b = Integer.valueOf(\"20\");   // Integer",
                    "    Sehari-hari pakai parseInt. valueOf baru perlu kalau objeknya",
                    "    memang dibutuhkan, misalnya mau dimasukkan ke List<Integer>.",
                    "",
                    "  - Integer.parseInt galak soal spasi dan titik. Ketiganya melempar",
                    "    NumberFormatException, bukan mengembalikan 0:",
                    "      Integer.parseInt(\" 20 \")   // spasi ikut terbaca",
                    "      Integer.parseInt(\"3.0\")    // int tidak kenal titik desimal",
                    "      Integer.parseInt(\"\")       // teks kosong",
                    "    Obatnya: panggil teks.trim() dulu. Anehnya Double.parseDouble",
                    "    dengan teks \" 3.5 \" justru lolos karena memangkas spasi sendiri.",
                    "    Jangan mengandalkan keanehan itu; trim() saja semuanya.",
                    "",
                    "  - Boolean.parseBoolean TIDAK PERNAH melempar exception. Apa pun",
                    "    yang bukan kata \"true\" (besar kecil huruf diabaikan) jadi false:",
                    "      Boolean.parseBoolean(\"TRUE\")  -> true",
                    "      Boolean.parseBoolean(\"Ya\")    -> false",
                    "    Baris kedua bukan error; ia salah diam-diam, dan itu lebih",
                    "    berbahaya daripada exception yang berisik.",
                    "",
                    "Arah sebaliknya, angka jadi teks. Tiga cara, sama-sama benar:",
                    "  String.valueOf(x)     paling aman: null pun jadi \"null\", tak NPE",
                    "  Integer.toString(x)   paling jelas maksudnya, tapi x wajib int",
                    "  \"\" + x                paling sering kamu temui di kode orang;",
                    "                        pendek, tapi menyamarkan bahwa di situ",
                    "                        sedang terjadi konversi",
                    "",
                    "Konstanta dan method pembungkus yang sering terpakai:",
                    "  Integer.MAX_VALUE      ->  2147483647",
                    "  Integer.MIN_VALUE      -> -2147483648",
                    "  Long.MAX_VALUE         ->  9223372036854775807",
                    "  Integer.MAX_VALUE + 1  -> -2147483648  (berputar: ini overflow)",
                    "  Integer.compare(3, 5)  -> -1   (yang kiri lebih kecil)",
                    "  Integer.compare(5, 5)  ->  0   (sama)",
                    "  Integer.compare(9, 5)  ->  1   (yang kiri lebih besar)",
                    "  Character.isDigit('7')      -> true",
                    "  Character.isLetter('7')     -> false",
                    "  Character.toUpperCase('a')  -> 'A'",
                    "  Integer.parseInt(\"1011\", 2) -> 11    (angka 2 = basis biner)",
                    "  Integer.parseInt(\"ff\", 16)  -> 255   (basis 16 alias heksadesimal)",
                    "  Integer.toBinaryString(11)  -> \"1011\"",
                ],
            },
            {
                "heading": "Dua jebakan yang jadi bug sungguhan",
                "code": """public class Main {
    public static void main(String[] args) {
        Integer a = 127, b = 127;
        Integer c = 1000, d = 1000;

        System.out.println(a == b);        // true  <- kebetulan, bukan aturan
        System.out.println(c == d);        // false <- isi sama, objeknya beda!
        System.out.println(c.equals(d));   // true  <- ini cara yang benar

        int e = 1000, f = 1000;
        System.out.println(e == f);        // true, karena int bukan objek

        Integer belumDiisi = null;
        System.out.println(belumDiisi == null);   // true, ini perbandingan aman

        try {
            int nilai = belumDiisi;   // diam-diam jadi belumDiisi.intValue()
            System.out.println(nilai);
        } catch (NullPointerException ex) {
            System.out.println("NPE: unboxing Integer yang bernilai null");
        }
    }
}""",
            },
            {
                "body": [
                    "Kenapa c == d bisa false padahal isinya sama-sama 1000?",
                    "  Pada objek, == membandingkan ALAMAT di memori, bukan isi. Ini",
                    "  aturan yang sama persis seperti pada String. Java menyimpan cache",
                    "  Integer untuk nilai -128 sampai 127, jadi dua Integer bernilai 127",
                    "  menunjuk objek yang sama dan == kebetulan true. Di luar rentang itu",
                    "  objeknya dibuat baru, dan == langsung false.",
                    "",
                    "  Jebakannya: kode yang diuji dengan angka kecil akan lulus, lalu",
                    "  rusak begitu angkanya membesar. Aturannya keras: pembungkus SELALU",
                    "  dibandingkan dengan .equals(). Kalau memang ingin memakai ==,",
                    "  turunkan dulu ke primitif, a.intValue() == b.intValue().",
                    "  Satu-satunya == yang benar untuk pembungkus adalah lawan null:",
                    "  x == null.",
                    "",
                    "Kenapa unboxing null jadi NullPointerException?",
                    "  Baris  int nilai = belumDiisi;  diterjemahkan compiler menjadi",
                    "  belumDiisi.intValue(). Memanggil method pada null selalu NPE.",
                    "  Yang menipu: di baris itu tidak ada satu pun titik yang terlihat.",
                    "  Ini rutin muncul begitu data datang dari database atau JSON yang",
                    "  kolomnya boleh kosong. Periksa null lebih dulu, atau bungkus",
                    "  dengan Optional (dibahas di materi Optional & Null Safety).",
                    "",
                    "Biaya tersembunyi autoboxing:",
                    "  Long total = 0L;",
                    "  for (int i = 0; i < 1000000; i++) { total += i; }",
                    "  Tiap putaran: total di-unbox jadi long, dijumlah, lalu di-box lagi.",
                    "  Baris sependek itu diam-diam membuat sejuta objek Long. Ganti",
                    "  tipenya jadi long primitif dan seluruh pekerjaan itu lenyap;",
                    "  hasilnya tetap sama, 499999500000.",
                    "",
                    "Aturan praktis memilih int atau Integer:",
                    "  - Pakai int/long/double untuk variabel lokal, penghitung loop,",
                    "    dan perhitungan. Ini pilihan bawaanmu; jangan pakai pembungkus",
                    "    tanpa alasan.",
                    "  - Pakai Integer/Long/Double kalau nilainya BOLEH tidak ada (null),",
                    "    atau kalau harus masuk ke List, Map, Optional, atau generic.",
                    "  - Method yang mengembalikan Integer sedang memberi tahu",
                    "    pemanggilnya 'hasilnya mungkin null'. Kalau tidak pernah null,",
                    "    kembalikan int saja; tanda tangan method itu ikut jadi",
                    "    dokumentasi bagi orang berikutnya yang membacanya.",
                ],
            },
        ],
    },
    {
        "title": "5. Operator",
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
                    "Tanda + punya PEKERJAAN KEDUA: menyambung teks (konkatenasi).",
                    "Begitu salah satu sisinya String, + berhenti menjumlahkan dan mulai menempel.",
                    "",
                    "  \"Halo \" + \"Andi\"  ->  \"Halo Andi\"",
                    "  \"Umur: \" + 20      ->  \"Umur: 20\"    (20 diubah jadi teks dulu)",
                    "  \"Nilai \" + true    ->  \"Nilai true\"",
                    "",
                    "Inilah idiom yang akan kamu tulis ribuan kali, dan yang muncul di hampir semua",
                    "contoh sesudah ini:",
                    "  System.out.println(\"Total: \" + total);",
                    "Tanpa itu kamu cuma bisa mencetak satu hal per baris.",
                    "",
                    "TAPI + dikerjakan dari KIRI ke KANAN, dan itu memberi hasil yang mengejutkan:",
                    "",
                    "  1 + 2 + \"x\"  ->  \"3x\"    (1+2 dijumlahkan dulu, baru ditempel)",
                    "  \"x\" + 1 + 2  ->  \"x12\"   (begitu kena String, sisanya cuma menempel)",
                    "",
                    "Jadi kalau mau menjumlahkan di tengah teks, kurung dulu:",
                    "",
                    "  System.out.println(\"Jumlah: \" + 10 + 5);     // Jumlah: 105   (salah)",
                    "  System.out.println(\"Jumlah: \" + (10 + 5));   // Jumlah: 15    (benar)",
                    "",
                    "+= juga berlaku untuk String:  pesan += \" selesai\";",
                    "Nyaman untuk beberapa baris, tapi jangan dipakai di dalam loop panjang - String",
                    "tidak bisa diubah, jadi tiap += diam-diam membuat String BARU. Untuk itu ada",
                    "StringBuilder (lihat materi String & Scanner).",
                    "",
                    "Satu jebakan kecil: char BUKAN String. 'A' + 1 menghasilkan 66, bukan \"A1\",",
                    "karena char disimpan sebagai angka. \"\" + 'A' + 1 barulah \"A1\".",
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
                "body": [
                    "Operator bit: bekerja pada angka BIT PER BIT, bukan pada nilainya utuh.",
                    "Jarang kamu tulis sendiri di awal, tapi sering kamu BACA di kode orang - dan",
                    "kalau bentuknya tidak dikenali, & terlihat seperti && yang kurang satu huruf.",
                    "",
                    "  &    DAN bit       5 & 3   ->  1    (0101 & 0011 = 0001)",
                    "  |    ATAU bit      5 | 3   ->  7    (0101 | 0011 = 0111)",
                    "  ^    XOR bit       5 ^ 3   ->  6    (beda -> 1, sama -> 0)",
                    "  ~    BALIK bit     ~5      -> -6",
                    "  <<   geser kiri    1 << 3  ->  8    (sama dengan dikali 2 sebanyak 3 kali)",
                    "  >>   geser kanan   -16 >> 2   -> -4   (tanda minus ikut terjaga)",
                    "  >>>  geser kanan tanpa tanda   -16 >>> 28  ->  15",
                    "",
                    "Bentuk majemuknya ada semua:  &=  |=  ^=  <<=  >>=  >>>=",
                    "Prioritasnya di BAWAH perbandingan, jadi (izin & TULIS) != 0 wajib berkurung.",
                    "",
                    "& dan | juga bekerja pada boolean, dan di situlah bedanya dengan && dan || jadi",
                    "penting: & dan | SELALU mengevaluasi kedua sisi, sedangkan && dan || berhenti",
                    "begitu jawabannya sudah pasti. Sifat berhenti itu namanya short-circuit.",
                    "",
                    "  if (obj != null && obj.cek())   aman: obj.cek() tak dipanggil kalau null",
                    "  if (obj != null &  obj.cek())   MELEDAK: sisi kanan tetap dijalankan",
                    "",
                    "Pemakaian paling umum yang akan kamu temui: menyimpan banyak saklar hidup/mati",
                    "di dalam satu angka (bit flag).",
                    "",
                    "  static final int BACA = 1, TULIS = 2, HAPUS = 4;   // 1, 10, 100 dalam biner",
                    "  int izin = BACA | HAPUS;                    // gabungkan  -> 5",
                    "  boolean bolehTulis = (izin & TULIS) != 0;   // periksa    -> false",
                    "  izin |= TULIS;                              // nyalakan   -> 7",
                    "  izin &= ~HAPUS;                             // matikan    -> 3",
                    "",
                    "Dua bentuk lain yang sering muncul: x & 0xFF untuk mengambil 8 bit terakhir",
                    "sebuah angka (300 & 0xFF -> 44), dan 1 << n untuk membuat 2 pangkat n.",
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
        "title": "6. Percabangan (if / switch)",
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
        "title": "7. Perulangan (Loop)",
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
        "title": "8. Array",
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
            {
                "body": [
                    "Jebakan pemula paling terkenal di Java - dan karena ia bukan error, tidak ada",
                    "yang memperingatkanmu:",
                    "",
                    "  int[] nilai = {80, 90, 75, 85};",
                    "  System.out.println(nilai);      ->  [I@1b6d3586",
                    "",
                    "Itu bukan rusak dan bukan kebetulan. Array tidak punya cara mencetak dirinya",
                    "sendiri, jadi yang keluar adalah tipenya ([I artinya 'array of int') plus",
                    "alamatnya di memori - angka yang berubah tiap kali program dijalankan.",
                    "Obatnya satu baris: Arrays.toString(nilai).",
                    "",
                    "Arrays adalah kelas utilitas di java.util: isinya static method untuk array.",
                    "Di kode nyata, array hampir selalu diproses lewat sini, bukan lewat loop manual",
                    "seperti contoh di atas.",
                    "",
                    "  import java.util.Arrays;",
                    "",
                    "  Arrays.toString(arr)           ubah jadi teks yang terbaca",
                    "  Arrays.deepToString(arr2d)     sama, untuk array di dalam array",
                    "  Arrays.sort(arr)               urutkan DI TEMPAT (array aslinya berubah!)",
                    "  Arrays.fill(arr, nilai)        isi semua slot dengan nilai yang sama",
                    "  Arrays.copyOf(arr, n)          salinan sepanjang n (kelebihannya diisi 0)",
                    "  Arrays.copyOfRange(arr, a, b)  potong indeks a sampai SEBELUM b",
                    "  Arrays.equals(a, b)            bandingkan ISI - == cuma membandingkan alamat",
                    "  Arrays.binarySearch(arr, x)    cari cepat, tapi HANYA di array yang terurut",
                    "  Arrays.asList(a, b, c)         jadikan List berukuran TETAP (add() ditolak)",
                    "  System.arraycopy(...)          salin sepotong array ke array lain",
                    "",
                    "Tiga yang paling sering menggigit:",
                    "  1. Arrays.sort MENGUBAH array yang kamu berikan dan tidak mengembalikan apa",
                    "     pun. Salin dulu dengan copyOf kalau urutan aslinya masih dibutuhkan.",
                    "  2. Arrays.binarySearch memberi angka ngawur - bukan error - kalau arraynya",
                    "     belum terurut.",
                    "  3. Arrays.asList menghasilkan List yang panjangnya terkunci: set() boleh,",
                    "     add() dan remove() melempar UnsupportedOperationException.",
                ]
            },
            {
                "heading": "Kelas utilitas Arrays",
                "code": """import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        int[] nilai = {80, 90, 75, 85};

        // Angka di belakang @ berubah tiap kali program dijalankan.
        System.out.println(nilai);                    // [I@1b6d3586  <- alamat!
        System.out.println(Arrays.toString(nilai));   // [80, 90, 75, 85]

        // Salin dulu, baru urutkan: nilai TIDAK ikut berubah.
        int[] urut = Arrays.copyOf(nilai, nilai.length);
        Arrays.sort(urut);
        System.out.println(Arrays.toString(urut));           // [75, 80, 85, 90]
        System.out.println(Arrays.binarySearch(urut, 85));   // 2 (wajib terurut)

        System.out.println(Arrays.toString(Arrays.copyOfRange(nilai, 1, 3)));
        System.out.println(Arrays.toString(Arrays.copyOf(nilai, 6)));

        int[] kartu = new int[5];
        Arrays.fill(kartu, 7);
        System.out.println(Arrays.toString(kartu));   // [7, 7, 7, 7, 7]

        System.out.println(nilai == new int[]{80, 90, 75, 85});             // false
        System.out.println(Arrays.equals(nilai, new int[]{80, 90, 75, 85})); // true

        // arraycopy(dari, mulaiDari, ke, mulaiKe, berapa)
        int[] tujuan = new int[4];
        System.arraycopy(nilai, 2, tujuan, 0, 2);
        System.out.println(Arrays.toString(tujuan));  // [75, 85, 0, 0]

        int[][] matriks = {{1, 2}, {3, 4}};
        System.out.println(Arrays.deepToString(matriks));   // [[1, 2], [3, 4]]

        List<String> daftar = Arrays.asList("Andi", "Budi");
        daftar.set(0, "Anto");          // boleh: mengganti isi
        System.out.println(daftar);     // [Anto, Budi]
        try {
            daftar.add("Citra");        // TIDAK boleh: ukurannya terkunci
        } catch (UnsupportedOperationException e) {
            System.out.println("asList berukuran tetap");
        }
    }
}"""
            },
        ],
    },
    {
        "title": "9. Method (Fungsi)",
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
            {
                "body": [
                    "Varargs: parameter yang jumlah argumennya bebas.",
                    "Tiga titik sesudah tipe berarti 'nol atau lebih nilai bertipe ini'.",
                    "",
                    "  static void tulis(String... bagian) { ... }",
                    "",
                    "  tulis();                    // boleh, tanpa argumen sama sekali",
                    "  tulis(\"a\");",
                    "  tulis(\"a\", \"b\", \"c\");",
                    "",
                    "Di dalam method, bagian wujudnya array biasa - bagian.length dan for-each",
                    "bekerja persis seperti di materi Array. Java yang membungkus argumenmu.",
                    "",
                    "Dua aturannya:",
                    "  1. Varargs WAJIB jadi parameter TERAKHIR. Boleh didahului parameter biasa:",
                    "       static void tulis(String pemisah, String... bagian)",
                    "  2. Satu method cuma boleh punya satu varargs.",
                    "",
                    "Kamu sebenarnya SUDAH memakainya sejak awal tanpa tahu namanya:",
                    "  List.of(5, 3, 8)                     varargs",
                    "  String.format(\"%s umur %d\", a, b)    varargs",
                    "  System.out.printf(...)               varargs",
                    "Itulah sebabnya jumlah argumen ketiganya boleh berubah-ubah, padahal method",
                    "biasa harus dipanggil dengan jumlah yang persis sama. Kalau nanti kamu melihat",
                    "tiga titik di daftar parameter kode orang, itu bukan salah ketik.",
                ]
            },
            {
                "body": [
                    "Math adalah contoh paling nyata dari kalimat 'static' di atas: seluruh isinya",
                    "static method. Tidak pernah ada 'new Math()'; cukup Math.sesuatu(...). Ia",
                    "tinggal di java.lang, jadi TIDAK perlu import.",
                    "",
                    "  Math.abs(-9)      ->  9        nilai mutlak",
                    "  Math.max(3, 8)    ->  8        yang terbesar dari dua",
                    "  Math.min(3, 8)    ->  3        yang terkecil dari dua",
                    "  Math.round(2.5)   ->  3        bulatkan ke yang TERDEKAT",
                    "  Math.ceil(4.1)    ->  5.0      bulatkan ke ATAS",
                    "  Math.floor(4.9)   ->  4.0      bulatkan ke BAWAH",
                    "  Math.sqrt(144)    ->  12.0     akar kuadrat",
                    "  Math.pow(2, 10)   ->  1024.0   pangkat",
                    "  Math.random()     ->  0.0 sampai di bawah 1.0, acak tiap panggilan",
                    "  Math.PI           ->  3.141592653589793  (konstanta, bukan method)",
                    "",
                    "Perhatikan TIPE KEMBALIANNYA, karena itu yang paling sering bikin bingung:",
                    "pow, sqrt, ceil, dan floor selalu memberi double. Jadi Math.pow(2, 3) itu 8.0,",
                    "bukan 8. Math.round memberi long kalau masukannya double, int kalau float.",
                    "",
                    "Math.round inilah alat yang kamu cari begitu hasil hitungan terlihat jelek:",
                    "",
                    "  double luas = Math.PI * 7 * 7;",
                    "  System.out.println(luas);               // 153.93804002589985",
                    "  System.out.println(Math.round(luas));   // 154",
                    "",
                    "Kalau yang kamu mau bukan bilangan bulat melainkan dua angka di belakang koma,",
                    "yang dipakai bukan Math melainkan format teks (lihat materi String & Scanner).",
                ]
            },
            {
                "heading": "Varargs & kelas Math",
                "code": """public class Main {
    // Varargs: "nol atau lebih int". Di dalam method, angka adalah int[].
    static int jumlahkan(int... angka) {
        int total = 0;
        for (int a : angka) {
            total += a;
        }
        return total;
    }

    // Varargs WAJIB terakhir; boleh didahului parameter biasa.
    static void tulis(String pemisah, String... bagian) {
        System.out.println(String.join(pemisah, bagian));
    }

    public static void main(String[] args) {
        System.out.println(jumlahkan());                 // 0
        System.out.println(jumlahkan(5));                // 5
        System.out.println(jumlahkan(1, 2, 3, 4));       // 10
        System.out.println(jumlahkan(new int[]{7, 8}));  // 15, array pun diterima
        tulis(" - ", "Andi", "Budi", "Citra");           // Andi - Budi - Citra

        double r = 7;
        double luas = Math.PI * r * r;
        System.out.println(luas);                  // 153.93804002589985
        System.out.println(Math.round(luas));      // 154
        System.out.println(Math.ceil(4.1));        // 5.0
        System.out.println(Math.floor(4.9));       // 4.0
        System.out.println(Math.abs(-9));          // 9
        System.out.println(Math.max(3, 8) + " " + Math.min(3, 8));   // 8 3
        System.out.println(Math.sqrt(144));        // 12.0
        System.out.println(Math.pow(2, 10));       // 1024.0
    }
}"""
            },
        ],
    },
    {
        "title": "10. Rekursi",
        "sections": [
            {
                "body": [
                    "Rekursi = method yang di dalam tubuhnya memanggil DIRINYA SENDIRI.",
                    "Sekilas itu terdengar seperti lingkaran setan. Bukan — asalkan tiap",
                    "pemanggilan mengerjakan versi soal yang LEBIH KECIL dari sebelumnya.",
                    "",
                    "Analogi antrean: kamu ingin tahu kamu orang ke berapa. Kamu tanya",
                    "orang di depanmu, 'kamu nomor berapa?'. Ia juga tidak tahu, jadi ia",
                    "tanya orang di depannya, begitu terus sampai orang paling depan",
                    "menjawab 'aku nomor 1'. Jawaban itu mengalir balik ke belakang, tiap",
                    "orang menambah 1. Tidak seorang pun tahu jawaban penuhnya; tiap orang",
                    "cuma tahu 'jawabanku = jawaban orang di depanku + 1'.",
                    "",
                    "Dua syarat WAJIB. Rekursi yang kehilangan salah satunya pasti rusak:",
                    "  1. Base case -> kondisi yang menjawab LANGSUNG, tanpa memanggil diri.",
                    "  2. Langkah mengecil -> tiap pemanggilan makin dekat ke base case.",
                    "",
                    "Faktorial: 4! = 4 x 3 x 2 x 1 = 24. Definisinya sendiri sudah rekursif:",
                    "  faktorial(n) = n * faktorial(n - 1)     dan     faktorial(1) = 1",
                    "",
                    "Telusuri pelan-pelan. Turun dulu — soal dipecah, jawaban belum ada:",
                    "  faktorial(4) = 4 * faktorial(3)       <- ditahan, menunggu jawaban",
                    "    faktorial(3) = 3 * faktorial(2)     <- ditahan juga",
                    "      faktorial(2) = 2 * faktorial(1)   <- ditahan juga",
                    "        faktorial(1) = 1                <- BASE CASE, ada jawaban!",
                    "",
                    "Baru naik. Jawabannya dikembalikan, yang tadi ditahan bisa selesai:",
                    "      faktorial(2) = 2 * 1 = 2",
                    "    faktorial(3) = 3 * 2 = 6",
                    "  faktorial(4) = 4 * 6 = 24",
                    "",
                    "Perhatikan saat faktorial(1) dijawab: TIGA pemanggilan lain masih",
                    "menggantung, masing-masing memegang nilai n-nya sendiri. Itu bukan",
                    "kiasan — keempatnya benar-benar ada di memori pada saat yang sama.",
                    "",
                    "Pola yang sama untuk menjumlahkan 1 sampai n:",
                    "  jumlah(n) = n + jumlah(n - 1)     dan     jumlah(0) = 0",
                    "  jumlah(4) -> 4 + (3 + (2 + (1 + 0))) = 10",
                ],
            },
            {
                "heading": "Faktorial dan penjumlahan, dengan jejaknya",
                "code": """public class Rekursi {
    public static void main(String[] args) {
        System.out.println("Hasil faktorial(4) = " + faktorial(4, 0));
        System.out.println();
        System.out.println("Hasil jumlah(4)    = " + jumlah(4));
    }

    // Parameter "dalam" HANYA untuk mencetak jejak supaya tumpukannya
    // terlihat. Rekursinya sendiri tidak membutuhkannya.
    static int faktorial(int n, int dalam) {
        String spasi = "  ".repeat(dalam);
        System.out.println(spasi + "masuk faktorial(" + n + ")");

        if (n <= 1) {                                  // 1. base case
            System.out.println(spasi + "-> base case, kembalikan 1");
            return 1;
        }

        int lebihKecil = faktorial(n - 1, dalam + 1);  // 2. langkah mengecil
        int hasil = n * lebihKecil;
        System.out.println(spasi + "-> " + n + " * " + lebihKecil + " = " + hasil);
        return hasil;
    }

    static int jumlah(int n) {
        if (n == 0) return 0;          // base case
        return n + jumlah(n - 1);      // n mengecil satu demi satu
    }
}""",
            },
            {
                "body": [
                    "Call stack: tumpukan pemanggilan yang belum selesai.",
                    "",
                    "Tiap kali sebuah method dipanggil, Java menyiapkan satu 'kotak' di",
                    "memori berisi parameter dan variabel lokal method itu, lalu",
                    "MENUMPUKNYA di atas kotak pemanggilnya. Yang paling atas itulah yang",
                    "sedang jalan. Begitu ia return, kotaknya dibuang dan kotak di",
                    "bawahnya melanjutkan tepat dari baris tempat ia tadi berhenti.",
                    "",
                    "Ini berlaku untuk SEMUA method, bukan cuma yang rekursif. Bedanya,",
                    "pada rekursi tumpukan itu berisi method yang itu-itu juga — sepuluh",
                    "atau seribu kotak dari method yang sama, masing-masing dengan nilai",
                    "n miliknya sendiri.",
                    "",
                    "Tumpukan itu TIDAK tak terbatas. Besarnya beberapa ratus KB (bisa",
                    "disetel lewat opsi -Xss), kira-kira cukup untuk sepuluh ribu tingkat",
                    "pemanggilan. Lewat dari itu Java melempar StackOverflowError.",
                    "",
                    "Base case yang salah adalah bug rekursi yang paling sering terjadi:",
                    "",
                    "  static int hitungMundur(int n) {",
                    "      if (n == 0) return 0;",
                    "      return n + hitungMundur(n - 2);   // LOMPAT DUA",
                    "  }",
                    "",
                    "hitungMundur(5) tidak pernah menyentuh 0: 5, 3, 1, -1, -3, -5, ...",
                    "Base casenya ADA dan tertulis benar, tapi langkahnya MELOMPATINYA.",
                    "Itu yang membuat bug semacam ini sulit dilihat: yang salah bukan satu",
                    "barisnya, melainkan hubungan antara base case dan langkahnya.",
                    "Perbaikannya n <= 0, atau turun satu-satu.",
                    "",
                    "Yang muncul di layar kalau itu dijalankan:",
                    "",
                    "  Exception in thread \"main\" java.lang.StackOverflowError",
                    "      at Rusak.hitungMundur(Rusak.java:8)",
                    "      at Rusak.hitungMundur(Rusak.java:8)",
                    "      at Rusak.hitungMundur(Rusak.java:8)",
                    "      ... baris yang sama terulang lebih dari seribu kali",
                    "",
                    "Cara membaca stack trace: isinya tumpukan tadi, dibaca dari ATAS ke",
                    "bawah. Baris teratas adalah tempat error terjadi, baris terbawah",
                    "biasanya main(). Kalau SATU baris yang sama terulang puluhan sampai",
                    "ribuan kali, itu hampir selalu rekursi yang base casenya tidak",
                    "pernah tercapai. Buka nomor baris yang disebut, lalu periksa dua hal",
                    "saja: base casenya ada tidak, dan langkahnya benar-benar mengecil ke",
                    "arah base case itu tidak.",
                    "",
                    "StackOverflowError itu Error, bukan Exception biasa (lihat materi",
                    "Exception Handling). Jangan ditangkap dengan try-catch: yang",
                    "bermasalah bukan datanya melainkan kodenya, dan menangkapnya cuma",
                    "menyembunyikan bug yang tetap ada di sana.",
                ],
            },
            {
                "heading": "Fibonacci naif dan Fibonacci yang mengingat",
                "body": [
                    "Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, ... tiap angka adalah jumlah",
                    "dua angka sebelumnya. Definisinya rekursif, dan kali ini DUA cabang:",
                    "  fib(n) = fib(n - 1) + fib(n - 2),   fib(0) = 0,   fib(1) = 1",
                    "",
                    "Versi naifnya benar tapi lambat, dan alasannya layak dilihat:",
                    "  fib(5) memanggil fib(4) dan fib(3)",
                    "  fib(4) memanggil fib(3) dan fib(2)   <- fib(3) dihitung ULANG",
                    "  makin dalam, makin banyak pekerjaan yang persis sama diulang",
                    "",
                    "Program di bawah menghitung sendiri berapa kali methodnya dipanggil.",
                    "Untuk n = 20 hasilnya 21.891 panggilan, demi satu angka yang",
                    "nilainya cuma 6765.",
                    "",
                    "Obatnya sederhana: simpan hasil yang sudah pernah dihitung, lalu",
                    "periksa catatan itu sebelum menghitung ulang. Namanya memoization.",
                    "Dengan catatan, n = 20 selesai dalam 39 panggilan. Rekursinya tidak",
                    "diganti sama sekali — ia cuma berhenti mengerjakan pekerjaan yang",
                    "sama berulang kali.",
                ],
                "code": """public class Fibonacci {
    static int panggilan = 0;      // penghitung: berapa kali method dipanggil

    public static void main(String[] args) {
        panggilan = 0;
        System.out.println("fib(20)      = " + fib(20));
        System.out.println("panggilan    = " + panggilan);

        long[] catatan = new long[41];   // 0 berarti "belum pernah dihitung"
        panggilan = 0;
        System.out.println("fibIngat(20) = " + fibIngat(20, catatan));
        System.out.println("panggilan    = " + panggilan);
    }

    // Versi naif: dua cabang, dan keduanya menghitung ulang hal yang sama.
    static long fib(int n) {
        panggilan++;
        if (n < 2) return n;                 // base case: fib(0)=0, fib(1)=1
        return fib(n - 1) + fib(n - 2);
    }

    // Versi yang mengingat: hasil yang sudah dihitung disimpan lebih dulu.
    static long fibIngat(int n, long[] catatan) {
        panggilan++;
        if (n < 2) return n;
        if (catatan[n] != 0) return catatan[n];   // jawabannya sudah ada
        catatan[n] = fibIngat(n - 1, catatan) + fibIngat(n - 2, catatan);
        return catatan[n];
    }
}""",
            },
            {
                "heading": "Menelusuri folder di dalam folder",
                "body": [
                    "Rekursi vs perulangan: keduanya bisa saling menggantikan.",
                    "",
                    "  static int jumlahLoop(int n) {",
                    "      int total = 0;",
                    "      for (int i = 1; i <= n; i++) total += i;",
                    "      return total;",
                    "  }",
                    "",
                    "Versi loop ini mengerjakan persis hal yang sama dengan jumlah(n)",
                    "rekursif di atas, lebih cepat, dan kebal StackOverflowError. Untuk",
                    "soal yang jalannya LURUS — 1 sampai n, isi array dari depan ke",
                    "belakang, baca berkas baris demi baris — loop hampir selalu pilihan",
                    "yang lebih baik. Menulisnya rekursif di situ cuma membuat kodenya",
                    "terlihat pintar tanpa menjadi lebih jelas.",
                    "",
                    "Rekursi menang saat datanya BERCABANG dan kedalamannya tidak",
                    "diketahui: folder di dalam folder, elemen HTML di dalam elemen HTML,",
                    "nilai JSON di dalam nilai JSON, komentar yang punya balasan yang",
                    "punya balasan lagi. Aturannya cuma 'kerjakan hal yang sama untuk",
                    "tiap anak', dan itu harus bisa masuk lagi sedalam apa pun.",
                    "",
                    "Loop biasa tidak punya tempat menyimpan 'aku tadi sedang di mana'",
                    "waktu ia turun satu tingkat, jadi kamu terpaksa membangun tumpukanmu",
                    "sendiri — persis pekerjaan yang sudah dilakukan call stack secara",
                    "cuma-cuma.",
                    "",
                    "Pohon folder di bawah digambarkan memakai array supaya belum perlu",
                    "class (lihat materi Array). Setelah belajar Class & Object kamu akan",
                    "menuliskannya sebagai objek yang punya daftar anak, tapi bentuk",
                    "rekursinya sama persis.",
                    "",
                    "Sadari juga base case di method total(): tidak ada satu pun if di",
                    "sana. Folder yang tidak punya anak membuat for-each-nya tidak jalan",
                    "sama sekali, jadi method itu langsung return. Base case boleh berupa",
                    "keadaan seperti itu, tidak harus kondisi yang ditulis eksplisit.",
                ],
                "code": """public class Folder {
    // Satu folder = satu baris di ketiga array ini.
    // anak[i] berisi INDEKS folder-folder yang ada di dalam folder ke-i.
    static String[] nama = {"proyek", "src", "model", "web", "docs"};
    static int[] ukuran  = {2, 0, 40, 25, 8};   // KB berkas di folder itu
    static int[][] anak  = {{1, 4}, {2, 3}, {}, {}, {}};

    public static void main(String[] args) {
        cetak(0, 0);
        System.out.println("Total: " + total(0) + " KB");
    }

    static void cetak(int i, int dalam) {
        String spasi = "  ".repeat(dalam);
        System.out.println(spasi + nama[i] + "/  " + ukuran[i] + " KB");
        for (int a : anak[i]) {
            cetak(a, dalam + 1);      // tiap anak diperlakukan persis sama
        }
    }

    static int total(int i) {
        int jumlah = ukuran[i];
        // Base casenya tersembunyi: folder tanpa anak membuat loop ini
        // tidak berjalan sama sekali, jadi method langsung return.
        for (int a : anak[i]) {
            jumlah += total(a);
        }
        return jumlah;
    }
}""",
            },
        ],
    },
    {
        "title": "11. OOP: Class & Object",
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
        "title": "12. Anggota Class: Constructor, static, dan Konstanta",
        "sections": [
            {
                "body": [
                    "Di materi Class & Object kamu sudah menyalin baris seperti",
                    "  Mahasiswa(String nama, int umur) { ... }",
                    "tanpa penjelasan apa pun. Itu constructor. Tiga aturannya wajib,",
                    "dan melanggarnya tidak selalu memunculkan error.",
                    "",
                    "  1. Namanya PERSIS sama dengan nama class. Huruf besar-kecil ikut dihitung.",
                    "  2. Tidak punya tipe kembali. Bukan int, bukan String, bahkan bukan void.",
                    "  3. Dijalankan otomatis tepat sekali, saat kata new dieksekusi.",
                    "",
                    "Jebakan aturan nomor 2, dan compiler DIAM saja:",
                    "",
                    "  class Mahasiswa {",
                    "      String nama;",
                    "      void Mahasiswa(String nama) {   // ada void -> BUKAN constructor",
                    "          this.nama = nama;",
                    "      }",
                    "  }",
                    "",
                    "Itu sah, tapi sebagai method biasa yang kebetulan bernama Mahasiswa.",
                    "new tidak pernah memanggilnya. Program tetap jalan, nama tetap null,",
                    "dan tidak ada satu pun pesan error yang menunjuk ke sini.",
                    "",
                    "CONSTRUCTOR DEFAULT",
                    "",
                    "Kalau kamu tidak menulis SATU PUN constructor, Java menyisipkan satu",
                    "constructor kosong secara gratis:  Mahasiswa() { }",
                    "Begitu kamu menulis satu constructor sendiri, hadiah itu ditarik.",
                    "",
                    "  class Mahasiswa {",
                    "      Mahasiswa(String nama) { this.nama = nama; }",
                    "  }",
                    "  new Mahasiswa();     // gagal dikompilasi",
                    "",
                    "  error: constructor Mahasiswa in class Mahasiswa cannot be applied",
                    "         to given types;",
                    "    required: String",
                    "    found:    no arguments",
                    "",
                    "Inilah kenapa error itu sering meledak di kode yang kemarin masih jalan:",
                    "seseorang menambah constructor berparameter, dan semua new Mahasiswa()",
                    "di berkas lain ikut mati. Obatnya bukan menghapus constructor barunya,",
                    "tapi menulis kembali constructor kosongnya kalau memang masih dipakai.",
                    "",
                    "OVERLOADING CONSTRUCTOR DAN this(...)",
                    "",
                    "Satu class boleh punya banyak constructor asal daftar parameternya",
                    "berbeda -- aturannya sama persis dengan method overloading di materi",
                    "Method. Supaya isinya tidak disalin berulang, constructor yang pendek",
                    "memanggil constructor yang lengkap lewat this(...):",
                    "",
                    "  public Kotak() { this(1, 1); }",
                    "",
                    "  - this(...) WAJIB jadi baris pertama di dalam constructor. Kalau tidak:",
                    "    error: call to this must be first statement in constructor",
                    "  - Jangan tertukar dengan this.lebar. Pakai TITIK berarti field milik",
                    "    objek ini; pakai KURUNG berarti panggilan ke constructor lain.",
                ],
            },
            {
                "heading": "Tiga constructor untuk satu class",
                "code": """public class Kotak {
    private int lebar;
    private int tinggi;

    // Constructor utama: satu-satunya yang benar-benar mengisi field.
    public Kotak(int lebar, int tinggi) {
        this.lebar = lebar;
        this.tinggi = tinggi;
    }

    // Kotak persegi: cukup satu ukuran, sisanya dilempar ke constructor utama.
    public Kotak(int sisi) {
        this(sisi, sisi);
    }

    // Tanpa argumen: kotak 1 x 1. Ini HARUS ditulis sendiri sekarang, karena
    // hadiah constructor default sudah hilang begitu ada constructor di atas.
    public Kotak() {
        this(1, 1);
    }

    public void tampilkan() {
        System.out.println(lebar + " x " + tinggi + " -> luas " + (lebar * tinggi));
    }

    public static void main(String[] args) {
        Kotak a = new Kotak(3, 4);
        Kotak b = new Kotak(5);
        Kotak c = new Kotak();

        a.tampilkan();   // 3 x 4 -> luas 12
        b.tampilkan();   // 5 x 5 -> luas 25
        c.tampilkan();   // 1 x 1 -> luas 1
    }
}""",
            },
            {
                "body": [
                    "Satu hal lagi soal constructor, supaya nanti tidak kaget di materi",
                    "Inheritance: kalau baris pertama sebuah constructor bukan this(...) dan",
                    "bukan super(...), Java DIAM-DIAM menyisipkan super(); di situ. Selalu.",
                    "Masuk akal: bagian induk dari objek harus jadi lebih dulu.",
                    "",
                    "Akibatnya, kalau class induk tidak punya constructor tanpa argumen,",
                    "class anak wajib memanggil super(...) sendiri. Kalau lupa:",
                    "",
                    "  error: constructor Hewan in class Hewan cannot be applied to given types;",
                    "  class Kucing extends Hewan {",
                    "",
                    "Perhatikan: yang disebut Hewan, tapi baris yang ditunjuk ada di Kucing.",
                    "Sebagian IDE menulisnya lain -- 'there is no default constructor available",
                    "in Hewan' -- artinya sama saja.",
                    "",
                    "FIELD STATIC VS FIELD INSTANCE",
                    "",
                    "  Field instance (tanpa static) -> tiap objek punya salinan SENDIRI.",
                    "  Field static                  -> SATU nilai, dipakai bersama semua objek.",
                    "",
                    "Objek dibuat dari cetakan. Field static menempel di CETAKANNYA, bukan",
                    "di hasil cetakan: ia sudah ada sebelum objek pertama dibuat, dan tetap",
                    "ada setelah semua objek dibuang. Itu sebabnya penghitung 'sudah berapa",
                    "objek yang pernah dibuat' hanya bisa ditulis sebagai field static.",
                    "",
                    "KONSTANTA: static + final",
                    "",
                    "  private static final double PPN = 0.11;",
                    "  public  static final int    KURSI_MAKS = 40;",
                    "",
                    "  static -> menempel di class, tidak disalin ke tiap objek.",
                    "  final  -> tidak bisa diisi ulang setelah nilainya masuk.",
                    "  Konvensi namanya HURUF_BESAR dipisah garis bawah.",
                    "",
                    "Ini bentuk BAKU konstanta di kode nyata; final di dalam method seperti",
                    "yang kamu lihat sebelumnya hanya berlaku selama method itu jalan.",
                    "Pola yang sama juga menjelaskan baris yang nangkring di atas hampir",
                    "setiap class serius:",
                    "",
                    "  private static final Logger log = LoggerFactory.getLogger(Pesanan.class);",
                    "",
                    "Satu objek pencatat, dibuat sekali untuk seluruh class, private supaya",
                    "tidak dipakai class lain, final supaya tidak ada yang menggantinya.",
                    "",
                    "BLOK INISIALISASI static",
                    "",
                    "  static { ... }",
                    "",
                    "Dijalankan sekali saat class itu pertama kali dipakai, SEBELUM main.",
                    "Jarang kamu tulis sendiri, tapi kenali bentuknya supaya tidak bingung",
                    "saat menemuinya -- ia bukan method dan tidak punya nama.",
                ],
            },
            {
                "heading": "Penghitung objek, konstanta, dan blok static",
                "code": """public class Tiket {
    // Konstanta: static + final, namanya HURUF_BESAR.
    public static final double HARGA = 50000;
    private static final String AWALAN = "TKT-";

    // Field static: SATU nilai, dipakai bersama semua objek Tiket.
    private static int jumlahTerjual = 0;

    // Field instance: tiap objek punya salinannya sendiri.
    private final String kode;

    // Blok inisialisasi static: jalan sekali, sebelum main.
    static {
        System.out.println("Loket dibuka.");
    }

    public Tiket() {
        jumlahTerjual++;                    // menaikkan angka milik CLASS
        this.kode = AWALAN + jumlahTerjual; // mengisi field milik OBJEK ini
    }

    public String getKode() {
        return kode;
    }

    // Method static: dipanggil lewat nama class, tanpa perlu objek.
    public static int getJumlahTerjual() {
        return jumlahTerjual;
    }

    public static double totalPendapatan() {
        return jumlahTerjual * HARGA;
    }

    public static void main(String[] args) {
        Tiket a = new Tiket();
        Tiket b = new Tiket();

        System.out.println(a.getKode());
        System.out.println(b.getKode());
        System.out.println("Terjual   : " + Tiket.getJumlahTerjual());
        System.out.println("Pendapatan: " + Tiket.totalPendapatan());
    }
}""",
            },
            {
                "body": [
                    "Keluaran program Tiket:",
                    "",
                    "  Loket dibuka.",
                    "  TKT-1",
                    "  TKT-2",
                    "  Terjual   : 2",
                    "  Pendapatan: 100000.0",
                    "",
                    "Dua hal yang layak diperhatikan:",
                    "  - 'Loket dibuka.' muncul paling atas padahal blok static ditulis di",
                    "    tengah class. Itu buktinya blok static jalan sebelum main.",
                    "  - jumlahTerjual bisa sampai 2 karena kedua objek menaikkan angka yang",
                    "    SAMA. Hapus kata static-nya, dan tiap tiket akan punya penghitung",
                    "    sendiri yang isinya selalu 1.",
                    "",
                    "ERROR STATIC YANG MEMBUAT SEMUA PEMULA MENTOK",
                    "",
                    "  public class Main {",
                    "      void sapa() { System.out.println(\"Halo\"); }",
                    "      public static void main(String[] args) {",
                    "          sapa();       // gagal",
                    "      }",
                    "  }",
                    "",
                    "  error: non-static method sapa() cannot be referenced from a static context",
                    "",
                    "Alasannya masuk akal begitu dibaca pelan: main itu static, jadi ia jalan",
                    "TANPA objek apa pun. Sedangkan sapa() milik objek. Java tidak menolak",
                    "karena galak, ia cuma tidak tahu objek yang MANA yang harus menyapa.",
                    "",
                    "Dua cara membetulkannya, dan pilihannya tergantung maksudmu:",
                    "  1. Buat objeknya dulu:             new Main().sapa();",
                    "  2. Jadikan methodnya static juga:  static void sapa() { ... }",
                    "",
                    "Pilih nomor 1 kalau method itu memang memakai field instance. Pilih",
                    "nomor 2 kalau ia cuma mengolah parameternya sendiri.",
                    "",
                    "Aturan yang sama berlaku ke arah field, dengan bunyi error yang mirip:",
                    "",
                    "  error: non-static variable umur cannot be referenced from a static context",
                    "",
                    "Method static tidak boleh menyentuh field instance maupun this, karena",
                    "saat ia jalan belum tentu ada objek yang bisa disentuh. Sebaliknya",
                    "boleh: method instance bebas memakai field static.",
                ],
            },
        ],
    },
    {
        "title": "13. Enum: Himpunan Nilai Tetap",
        "sections": [
            {
                "body": [
                    "Enum = daftar pilihan yang jumlahnya TETAP dan sudah diketahui sejak kode ditulis.",
                    "Status akun, hari dalam seminggu, level pengguna, jenis pembayaran, arah mata angin —",
                    "semuanya enum.",
                    "",
                    "Masalah yang dipecahkannya. Sebelum enum ada, orang menyatakan pilihan sebagai angka",
                    "atau teks:",
                    "  int status = 1;              // 1 itu aktif atau nonaktif? tebak sendiri",
                    "  String status = \"AKTIF\";",
                    "",
                    "Dua-duanya punya lubang yang sama: compiler tidak tahu apa-apa soal nilai yang sah.",
                    "  status = 99;                 // lolos kompilasi, kacau saat program jalan",
                    "  status = \"aktip\";            // salah ketik, lolos kompilasi, diam-diam salah",
                    "",
                    "Dengan enum, nilai ngawur DITOLAK saat kompilasi, bukan saat pemakai memakainya:",
                    "  Status status = Status.AKTIF;",
                    "  status = 99;                 // error: incompatible types",
                    "",
                    "Bentuk paling sederhana (satu berkas Status.java):",
                    "  public enum Status { AKTIF, NONAKTIF, DIBLOKIR }",
                    "",
                    "Kenapa isinya HURUF BESAR semua? Karena tiap nama itu konstanta. Di balik layar Java",
                    "menjadikannya `public static final Status AKTIF = ...`, dan konvensi Java untuk",
                    "static final memang HURUF_BESAR.",
                    "",
                    "Konsekuensi yang paling penting: satu konstanta = SATU objek, dibuat sekali oleh JVM.",
                    "Kamu tidak pernah menulis `new Status(...)` — memang tidak diizinkan. Karena objeknya",
                    "cuma satu, `==` aman dipakai untuk membandingkan enum. Ini kebalikan dari String yang",
                    "wajib pakai .equals() (dibahas nanti di materi String & Scanner). Pada enum, `==`",
                    "malah lebih aman: ia tidak melempar NullPointerException walau variabelnya null.",
                    "",
                    "Enum sebenarnya CLASS khusus. Semua yang sudah kamu pelajari soal field, constructor,",
                    "dan method tetap berlaku di sini — bedanya cuma: daftar objeknya ditentukan di muka.",
                ],
            },
            {
                "heading": "Enum dipakai sebagai tipe, dibandingkan, dan di-switch",
                "code": """enum Status {
    AKTIF, NONAKTIF, DIBLOKIR
}

class Akun {
    String nama;
    Status status;

    Akun(String nama, Status status) {
        this.nama = nama;
        this.status = status;
    }
}

public class Main {
    // switch bentuk klasik: case ditulis TANPA "Status."
    static String pesan(Status s) {
        switch (s) {
            case AKTIF:
                return "Silakan masuk.";
            case NONAKTIF:
                return "Akun belum diaktifkan.";
            default:
                return "Akun diblokir.";
        }
    }

    // switch bentuk panah (Java 14+), dipakai sebagai ekspresi
    static int batasUnggah(Status s) {
        return switch (s) {
            case AKTIF -> 100;
            case NONAKTIF -> 10;
            case DIBLOKIR -> 0;
        };
    }

    public static void main(String[] args) {
        Akun a = new Akun("Andi", Status.AKTIF);
        Akun b = new Akun("Budi", Status.DIBLOKIR);

        System.out.println(a.nama + ": " + pesan(a.status)
                + " (batas " + batasUnggah(a.status) + " MB)");
        System.out.println(b.nama + ": " + pesan(b.status)
                + " (batas " + batasUnggah(b.status) + " MB)");

        // dibandingkan dengan ==, bukan equals
        if (b.status == Status.DIBLOKIR) {
            System.out.println("Kirim laporan ke admin.");
        }

        // values(): semua konstanta, urut sesuai urutan deklarasi
        for (Status s : Status.values()) {
            System.out.println(s.ordinal() + " " + s.name());
        }

        // teks -> enum
        Status dariTeks = Status.valueOf("NONAKTIF");
        System.out.println("dariTeks = " + dariTeks);

        try {
            Status.valueOf("aktif");   // huruf kecil -> tidak ada
        } catch (IllegalArgumentException e) {
            System.out.println("valueOf gagal: teksnya harus persis sama.");
        }
    }
}""",
            },
            {
                "body": [
                    "Keluaran program di atas:",
                    "  Andi: Silakan masuk. (batas 100 MB)",
                    "  Budi: Akun diblokir. (batas 0 MB)",
                    "  Kirim laporan ke admin.",
                    "  0 AKTIF",
                    "  1 NONAKTIF",
                    "  2 DIBLOKIR",
                    "  dariTeks = NONAKTIF",
                    "  valueOf gagal: teksnya harus persis sama.",
                    "",
                    "Yang perlu diperhatikan:",
                    "  - Enum dipakai persis seperti tipe lain: jadi tipe field, jadi tipe parameter,",
                    "    jadi tipe kembalian method.",
                    "  - `b.status == Status.DIBLOKIR` aman karena tiap konstanta cuma satu objek.",
                    "",
                    "switch atas enum ditulis `case AKTIF`, BUKAN `case Status.AKTIF`.",
                    "Ini bukan soal selera: menulis nama enumnya justru bikin error kompilasi. Alasannya,",
                    "switch sudah tahu tipenya dari ekspresi di dalam kurung, jadi menyebut nama enum di",
                    "tiap case cuma pengulangan. Soal break dan fall-through di bentuk klasik, lihat",
                    "materi Percabangan — bentuk panah tidak punya fall-through jadi tidak perlu break.",
                    "",
                    "Kelebihan bentuk panah yang sering menyelamatkan: kalau SEMUA konstanta dicakup,",
                    "`default` boleh dihilangkan. Suatu hari ada yang menambah konstanta baru ke enumnya,",
                    "compiler langsung menunjuk setiap switch yang belum menanganinya. Sebaliknya kalau",
                    "ada `default`, konstanta baru itu lolos diam-diam ke cabang default dan bug-nya baru",
                    "ketahuan dari laporan pemakai.",
                    "",
                    "Method bawaan yang dimiliki SEMUA enum tanpa perlu ditulis:",
                    "  values()           array berisi semua konstanta, urut sesuai deklarasi",
                    "  valueOf(\"AKTIF\")   teks -> konstanta; harus persis, peka huruf besar-kecil",
                    "  name()             nama konstanta sebagai String (\"AKTIF\")",
                    "  ordinal()          posisi konstanta, mulai dari 0",
                    "  toString()         bawaannya sama dengan name(), jadi println() mencetak namanya",
                    "  compareTo()        membandingkan berdasarkan ordinal, jadi enum bisa di-sort",
                    "",
                    "JEBAKAN valueOf(): teks yang tidak cocok MELEMPAR IllegalArgumentException, bukan",
                    "mengembalikan null. Data yang datang dari berkas, form web, atau database harus",
                    "dibungkus try-catch atau divalidasi lebih dulu. Cara membungkusnya dibahas di materi",
                    "Exception Handling.",
                    "",
                    "JEBAKAN ordinal(): jangan pernah menyimpan ordinal ke database atau berkas. Angka",
                    "itu cuma cerminan urutan mengetik. Menyisipkan satu konstanta baru di tengah daftar",
                    "menggeser semua nomor sesudahnya, dan SELURUH data lama berubah arti tanpa satu pun",
                    "pesan error. Simpan name() sebagai teks, atau simpan field kode buatanmu sendiri",
                    "seperti contoh berikut.",
                ],
            },
            {
                "heading": "Enum berkonstruktor, bermethod, dan bersarang",
                "code": """import java.util.EnumMap;
import java.util.EnumSet;
import java.util.Map;

interface Berbayar {
    int biaya();
}

enum Paket implements Berbayar {
    HEMAT("Hemat", 10),
    STANDAR("Standar", 25),
    PREMIUM("Premium", 60);        // titik koma WAJIB sebelum field & constructor

    private final String label;
    private final int kuotaGb;

    Paket(String label, int kuotaGb) {   // constructor enum selalu private
        this.label = label;
        this.kuotaGb = kuotaGb;
    }

    public String getLabel() {
        return label;
    }

    public boolean muat(int pakaiGb) {   // method biasa, sama untuk semua konstanta
        return pakaiGb <= kuotaGb;
    }

    @Override
    public int biaya() {                 // memenuhi kontrak interface
        return kuotaGb * 2000;
    }
}

enum Operasi {
    TAMBAH("+") {
        public int hitung(int a, int b) { return a + b; }
    },
    KALI("*") {
        public int hitung(int a, int b) { return a * b; }
    };

    private final String simbol;

    Operasi(String simbol) {
        this.simbol = simbol;
    }

    public abstract int hitung(int a, int b);   // isinya beda tiap konstanta

    public String getSimbol() {
        return simbol;
    }
}

class Pesanan {
    enum Status { BARU, DIKIRIM, SELESAI }   // enum di DALAM class

    Status status = Status.BARU;
}

public class Main {
    public static void main(String[] args) {
        for (Paket p : Paket.values()) {
            System.out.println(p.getLabel() + " Rp" + p.biaya()
                    + " cukup untuk 20 GB? " + p.muat(20));
        }

        for (Operasi o : Operasi.values()) {
            System.out.println("6 " + o.getSimbol() + " 3 = " + o.hitung(6, 3));
        }

        // EnumMap: kuncinya enum; urutannya selalu urutan deklarasi
        Map<Paket, Integer> pelanggan = new EnumMap<>(Paket.class);
        pelanggan.put(Paket.PREMIUM, 12);
        pelanggan.put(Paket.HEMAT, 340);
        System.out.println(pelanggan);

        // EnumSet: himpunan konstanta
        EnumSet<Paket> murah = EnumSet.of(Paket.HEMAT, Paket.STANDAR);
        System.out.println("PREMIUM termasuk murah? " + murah.contains(Paket.PREMIUM));

        // dari luar, enum bersarang disebut lewat nama class-nya
        Pesanan pesanan = new Pesanan();
        System.out.println(pesanan.status + " lalu " + Pesanan.Status.SELESAI);
    }
}""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  Hemat Rp20000 cukup untuk 20 GB? false",
                    "  Standar Rp50000 cukup untuk 20 GB? true",
                    "  Premium Rp120000 cukup untuk 20 GB? true",
                    "  6 + 3 = 9",
                    "  6 * 3 = 18",
                    "  {HEMAT=340, PREMIUM=12}",
                    "  PREMIUM termasuk murah? false",
                    "  BARU lalu SELESAI",
                    "",
                    "Enum berkonstruktor — inilah bentuk yang paling sering kamu temui di kode produksi:",
                    "  - Nilai di dalam kurung (`HEMAT(\"Hemat\", 10)`) adalah argumen constructor.",
                    "  - Constructor enum SELALU private. Menulis `public` di situ error, dan itu masuk",
                    "    akal: tidak ada yang boleh membuat konstanta baru selain enum itu sendiri.",
                    "  - Constructor-nya jalan sekali per konstanta, saat enumnya pertama kali dipakai.",
                    "  - Field dibuat `private final` supaya nilainya tidak bisa diubah dari luar.",
                    "  - TITIK KOMA sesudah konstanta terakhir wajib begitu ada field, constructor, atau",
                    "    method di bawahnya. Lupa titik koma ini salah satu error enum paling sering.",
                    "",
                    "Method berbeda per konstanta: deklarasikan method `abstract` di enumnya, lalu tiap",
                    "konstanta membawa blok { } berisi versinya sendiri. Ini menggantikan switch panjang",
                    "yang harus diedit tiap ada konstanta baru — di sini compiler menolak konstanta yang",
                    "lupa mengisi method abstraknya.",
                    "",
                    "Enum boleh `implements` interface, tapi TIDAK boleh `extends` class. Di balik layar",
                    "ia sudah mewarisi java.lang.Enum, dan Java cuma mengizinkan satu parent.",
                    "",
                    "EnumMap & EnumSet (java.util) — pakai ini, bukan HashMap/HashSet, saat kuncinya enum:",
                    "  - EnumMap disimpan sebagai array sepanjang jumlah konstanta, diindeks ordinal.",
                    "    Tidak ada hashing dan tidak ada tabrakan: lebih hemat memori dan lebih cepat.",
                    "  - Iterasinya SELALU urut sesuai deklarasi. Urutan HashMap tidak dijanjikan apa pun.",
                    "  - EnumSet menyimpan anggotanya sebagai bit di dalam satu long, jadi gabungan dan",
                    "    irisan himpunan cuma operasi bit. EnumSet.allOf(Paket.class), EnumSet.noneOf(...),",
                    "    dan EnumSet.range(...) juga sering dipakai.",
                    "",
                    "Enum di dalam class (`Pesanan.Status`): pilih ini kalau enumnya hanya bermakna bersama",
                    "class itu. Di dalam Pesanan cukup ditulis `Status`; dari luar ditulis `Pesanan.Status`",
                    "dan konstantanya `Pesanan.Status.SELESAI`.",
                    "",
                    "Ringkasan jebakan:",
                    "  - `case Status.AKTIF` di dalam switch -> error. Tulis `case AKTIF` saja.",
                    "  - valueOf() melempar IllegalArgumentException, tidak mengembalikan null.",
                    "  - ordinal() jangan pernah disimpan permanen; simpan name() atau kode sendiri.",
                    "  - Lupa titik koma sesudah konstanta terakhir saat enum punya isi tambahan.",
                    "  - Enum tidak bisa di-`new` dan tidak bisa `extends` class lain.",
                ],
            },
        ],
    },
    {
        "title": "14. OOP: Encapsulation",
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
        "title": "15. OOP: Inheritance (Pewarisan)",
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
        "title": "16. OOP: Polymorphism",
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
            {
                "body": [
                    "instanceof - alat pemeriksa yang barusan disebut sambil lalu itu.",
                    "",
                    "  objek instanceof Tipe",
                    "",
                    "Hasilnya boolean: true kalau objeknya memang bertipe itu ATAU turunannya. Karena",
                    "hasilnya boolean biasa, ia boleh dipakai di mana pun boolean boleh dipakai, tidak",
                    "harus langsung di dalam if:",
                    "  boolean iniKucing = h instanceof Kucing;",
                    "",
                    "Dua sifat yang menyelamatkan:",
                    "  1. null instanceof apa pun SELALU false, dan tidak pernah melempar",
                    "     NullPointerException. Jadi kamu tidak perlu memeriksa null lebih dulu.",
                    "  2. Perbandingan yang mustahil ditolak compiler, bukan didiamkan. Menulis",
                    "     'teks instanceof Integer' untuk variabel String berhenti di:",
                    "       error: incompatible types: String cannot be converted to Integer",
                    "",
                    "Kenapa harus dicek? Karena downcasting yang meleset TIDAK ditolak compiler -",
                    "ia baru meledak saat program sudah berjalan:",
                    "",
                    "  Hewan h = new Anjing();",
                    "  Kucing k = (Kucing) h;",
                    "",
                    "  Exception in thread \"main\" java.lang.ClassCastException:",
                    "      class Anjing cannot be cast to class Kucing",
                    "",
                    "Jadi pola amannya selalu berpasangan: periksa dulu, baru cast.",
                    "",
                    "  if (h instanceof Kucing) {",
                    "      Kucing k = (Kucing) h;",
                    "      k.mengeong();",
                    "  }",
                    "",
                    "Sejak Java 16, dua baris itu boleh disatukan. Namanya pattern matching:",
                    "  if (h instanceof Kucing k) { k.mengeong(); }",
                    "Pemeriksaan dan cast jadi satu, dan k cuma ada di dalam blok yang sudah pasti",
                    "Kucing. Bentuk inilah yang sekarang ada di mana-mana, termasuk di dalam equals()",
                    "hampir setiap class. Aturan lengkapnya dibahas di materi Record & Sintaks Java",
                    "Modern; untuk sekarang cukup tahu bahwa keduanya berarti hal yang sama.",
                ]
            },
            {
                "heading": "instanceof, cast, dan ClassCastException",
                "code": """class Hewan { }

class Kucing extends Hewan {
    void mengeong() { System.out.println("Meow!"); }
}

class Anjing extends Hewan { }

public class Main {
    static void periksa(Hewan h) {
        boolean iniKucing = h instanceof Kucing;   // hasilnya boolean biasa
        System.out.println("kucing? " + iniKucing);
        if (h instanceof Kucing) {
            Kucing k = (Kucing) h;   // aman: sudah dipastikan di baris atasnya
            k.mengeong();
        }
    }

    public static void main(String[] args) {
        periksa(new Kucing());   // kucing? true  lalu  Meow!
        periksa(new Anjing());   // kucing? false

        Hewan kosong = null;
        System.out.println(kosong instanceof Kucing);   // false, tidak meledak

        Hewan h = new Anjing();
        try {
            Kucing k = (Kucing) h;   // lolos compiler, gagal saat dijalankan
            k.mengeong();
        } catch (ClassCastException e) {
            System.out.println("gagal cast: " + e.getMessage());
        }
    }
}"""
            },
        ],
    },
    {
        "title": "17. Class Object: toString, equals, dan hashCode",
        "sections": [
            {
                "body": [
                    "Ada satu class yang tidak pernah kamu tulis tapi selalu ikut: java.lang.Object.",
                    "Semua class di Java menurunkannya, termasuk class yang tidak menulis extends apa pun.",
                    "",
                    "  class Titik { }        // yang dibaca compiler: class Titik extends Object",
                    "",
                    "Artinya setiap objek SUDAH punya method sebelum kamu mengetik satu baris pun:",
                    "  toString()      -> wujud teks objek; dipakai tiap kali objek dicetak.",
                    "  equals(Object)  -> apakah objek ini dianggap sama dengan objek lain?",
                    "  hashCode()      -> satu int wakil objek; dipakai HashSet dan HashMap.",
                    "  getClass()      -> class asli objek, diketahui saat program berjalan.",
                    "  clone(), finalize(), wait(), notify(), notifyAll()  -> jarang ditulis sendiri.",
                    "",
                    "Ini juga yang membuat Object bisa menampung apa saja:",
                    "  Object apa = \"halo\";   // String pun turunan Object.",
                    "",
                    "Kenapa System.out.println(objek) mencetak Titik@1b6d3586?",
                    "println tidak punya sihir: ia memanggil objek.toString() lalu mencetak hasilnya.",
                    "Penggabungan \"Titik: \" + objek juga begitu.",
                    "",
                    "toString() bawaan Object isinya kira-kira:",
                    "  getClass().getName() + \"@\" + Integer.toHexString(hashCode())",
                    "Jadi yang kamu lihat adalah nama class + hashCode dalam heksadesimal. Angka itu",
                    "berubah tiap program dijalankan ulang, dan tidak memberi tahu apa pun soal isinya.",
                    "",
                    "Tiga method pertama punya perilaku bawaan yang hampir tidak pernah kamu maksud.",
                    "Materi ini soal mengganti ketiganya, dan kenapa dua di antaranya wajib sepasang.",
                ],
            },
            {
                "heading": "Kalau ketiganya dibiarkan bawaan",
                "code": """import java.util.HashSet;
import java.util.Set;

class Titik {
    int x;
    int y;

    Titik(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

public class Main {
    public static void main(String[] args) {
        Titik a = new Titik(3, 4);
        Titik b = new Titik(3, 4);

        System.out.println(a);                              // Titik@1b6d3586
        System.out.println(a.getClass().getSimpleName());   // Titik

        System.out.println(a == b);         // false, memang dua objek berbeda
        System.out.println(a.equals(b));    // false <- ini yang mengagetkan

        Set<Titik> kumpulan = new HashSet<>();
        kumpulan.add(a);
        kumpulan.add(b);
        System.out.println(kumpulan.size());   // 2, padahal isinya sama persis
    }
}""",
            },
            {
                "body": [
                    "Tiga hal yang perlu diperbaiki dari contoh di atas.",
                    "",
                    "1) toString(): tulis apa yang ingin kamu lihat saat debugging dan logging.",
                    "  @Override",
                    "  public String toString() { return \"Titik(\" + x + \", \" + y + \")\"; }",
                    "",
                    "  @Override bukan hiasan. Kalau nama atau parameternya salah ketik, compiler",
                    "  langsung menolak — bukan diam-diam membuat method baru yang tak pernah dipanggil.",
                    "",
                    "2) equals(): bawaan Object isinya persis 'this == lain', yaitu membandingkan ALAMAT.",
                    "  Dua objek berisi data identik selalu dianggap berbeda karena memang dua objek.",
                    "  String terasa lain (lihat materi String & Scanner) semata karena String SUDAH",
                    "  meng-override equals, bukan karena ada aturan khusus untuk String.",
                    "",
                    "  Kerangkanya empat langkah, selalu urutan ini:",
                    "    1. if (this == lain) return true;                // objek yang sama persis",
                    "    2. if (!(lain instanceof Titik)) return false;   // null pun jatuh di sini",
                    "    3. Titik t = (Titik) lain;                       // aman, tipenya sudah pasti",
                    "    4. bandingkan field satu per satu.",
                    "",
                    "  Field primitif (int, double, boolean) cukup dibandingkan dengan ==.",
                    "  Field objek pakai Objects.equals(a, b) — ia tahan null, sedangkan a.equals(b)",
                    "  melempar NullPointerException begitu a kebetulan null.",
                    "",
                    "  Parameternya WAJIB Object. Menulis equals(Titik lain) membuat method BARU",
                    "  (overload), bukan override, dan HashSet tetap memakai versi bawaan. Ini jebakan",
                    "  klasik yang tidak menghasilkan error apa pun — @Override yang menangkapnya.",
                    "",
                    "  Kontrak yang dipegang seluruh library Java:",
                    "    - refleksif : x.equals(x) selalu true.",
                    "    - simetris  : x.equals(y) hasilnya sama dengan y.equals(x).",
                    "    - transitif : kalau x sama dengan y dan y sama dengan z, maka x sama dengan z.",
                    "    - konsisten : hasilnya tidak berubah selama datanya tidak berubah.",
                    "    - x.equals(null) selalu false.",
                    "",
                    "3) hashCode(): ditulis SETIAP KALI equals ditulis. Aturannya satu kalimat —",
                    "  dua objek yang equals HARUS mengembalikan hashCode yang sama.",
                    "  Cara terpendek: return Objects.hash(x, y);",
                    "  Isi Objects.hash dengan field yang sama persis dengan yang dipakai di equals.",
                ],
            },
            {
                "heading": "Versi yang benar",
                "code": """import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Objects;
import java.util.Set;

class Titik {
    private final int x;
    private final int y;

    Titik(int x, int y) {
        this.x = x;
        this.y = y;
    }

    @Override
    public String toString() {
        return "Titik(" + x + ", " + y + ")";
    }

    @Override
    public boolean equals(Object lain) {
        if (this == lain) return true;                 // objek yang sama persis
        if (!(lain instanceof Titik)) return false;    // null pun jatuh ke sini
        Titik t = (Titik) lain;
        return x == t.x && y == t.y;                   // primitif: cukup ==
    }

    @Override
    public int hashCode() {
        return Objects.hash(x, y);                     // field yang sama dengan di equals
    }
}

public class Main {
    public static void main(String[] args) {
        Titik a = new Titik(3, 4);
        Titik b = new Titik(3, 4);

        System.out.println(a);              // Titik(3, 4)
        System.out.println(a.equals(b));    // true
        System.out.println(a == b);         // tetap false: dua objek berbeda

        Set<Titik> kumpulan = new HashSet<>();
        kumpulan.add(a);
        kumpulan.add(b);
        System.out.println(kumpulan.size());   // 1

        Map<Titik, String> label = new HashMap<>();
        label.put(a, "pojok");
        System.out.println(label.get(new Titik(3, 4)));            // pojok
        System.out.println(kumpulan.contains(new Titik(3, 4)));    // true
    }
}""",
            },
            {
                "body": [
                    "Kenapa hashCode wajib berpasangan dengan equals?",
                    "HashSet dan HashMap mencari dengan DUA langkah: hitung hashCode untuk menentukan",
                    "'ember' penyimpanan, baru bandingkan isi ember itu dengan equals. Kalau hashCode",
                    "dibiarkan bawaan, dua objek yang equals mendarat di ember berbeda — dan equals",
                    "tidak pernah sempat dipanggil sama sekali.",
                    "",
                    "Akibat konkretnya, dan ini kelas bug yang TIDAK melempar error apa pun:",
                    "  - HashSet menyimpan duplikat; size() lebih besar dari yang kamu hitung.",
                    "  - map.get(key) mengembalikan null padahal datanya jelas sudah di-put.",
                    "  - list.contains(objek) dan list.remove(objek) bilang tidak ketemu.",
                    "  - Tes gagal dengan pesan seperti 'expected Titik(3, 4) but was Titik(3, 4)':",
                    "    dua teks yang kelihatan sama persis, karena yang beda memang bukan teksnya.",
                    "Kebalikannya (hashCode di-override, equals dibiarkan) sama rusaknya: objeknya",
                    "mendarat di ember yang tepat, lalu ditolak karena alamatnya berbeda.",
                    "",
                    "getClass() akan sering kamu temui di tiga tempat:",
                    "  - di equals, sebagai pengganti instanceof yang lebih ketat:",
                    "      if (lain == null || getClass() != lain.getClass()) return false;",
                    "  - di log dan pesan error: getClass().getSimpleName() memberi \"Titik\",",
                    "    sedangkan getClass().getName() memberi nama lengkap beserta package-nya.",
                    "  - saat kamu perlu tahu isi sebenarnya dari sebuah variabel bertipe Object.",
                    "Bedanya: instanceof menerima subclass (Titik3D dianggap Titik), getClass menolaknya.",
                    "instanceof lebih fleksibel, getClass lebih aman untuk simetri kontrak equals.",
                    "Keduanya dipakai di dunia nyata; pilih satu dan konsisten di satu class.",
                    "",
                    "Method Object lainnya, cukup dikenali saja saat membaca kode orang:",
                    "  clone()    -> menyalin objek; rancangannya bermasalah sejak awal, jadi orang",
                    "                lebih memilih constructor penyalin atau method salinan sendiri.",
                    "  finalize() -> dulu dipanggil sebelum objek dibuang; sudah deprecated, jangan pakai.",
                    "  wait(), notify(), notifyAll() -> komunikasi antar thread, dibahas di materi",
                    "                Multithreading & Concurrency Dasar.",
                    "",
                    "IDE bisa membuatkan ketiganya sekali klik, dan sebuah record (Java 16+) menghasilkan",
                    "ketiganya otomatis. Itu justru alasan untuk paham isinya: kode hasil generate itulah",
                    "yang paling sering kamu BACA di repo orang, dan yang perlu kamu periksa adalah field",
                    "MANA saja yang ikut dibandingkan — di situlah bug-nya biasa bersembunyi.",
                    "",
                    "Di aplikasi ini: kunci jawaban Latihan 12 (Kotak Generic) memakai",
                    "@Override public String toString() supaya System.out.println(p) mencetak (Andi, 20),",
                    "bukan Pasangan@1b6d3586. Sekarang kamu tahu kenapa baris itu ada di sana.",
                ],
            },
        ],
    },
    {
        "title": "18. OOP: Abstract & Interface",
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
            {
                "body": [
                    "Kalimat 'Sejak Java 8: boleh default method & static method' di atas pantas",
                    "dapat penjelasan sendiri, karena ia membatalkan separuh aturan yang baru saja",
                    "kamu hafalkan: interface TIDAK lagi selalu kosong.",
                    "",
                    "MASALAH yang dipecahkan default. Bayangkan interface List sudah dipakai ribuan",
                    "class di seluruh dunia, lalu Java ingin menambahkan method sort() ke situ.",
                    "Dengan aturan lama, setiap class yang implements List langsung berhenti bisa",
                    "dikompilasi - semuanya tiba-tiba kurang satu method. default menyelesaikannya:",
                    "method baru itu dibawa LENGKAP DENGAN ISINYA, jadi class lama tidak perlu",
                    "diubah sama sekali, dan yang mau versinya sendiri tinggal meng-override.",
                    "",
                    "  default double total() { return jumlah() + biaya(); }",
                    "",
                    "Empat isi yang boleh ada di dalam interface sekarang:",
                    "  abstract   tanpa isi, wajib diisi pelaksana (yang sudah kamu tahu)",
                    "  default    punya isi, dipakai otomatis, boleh ditimpa pelaksana",
                    "  static     milik interface-nya sendiri: Pembayaran.rupiah(...). TIDAK",
                    "             diwariskan, jadi Transfer.rupiah(...) tidak ada",
                    "  private    penolong bersama antar-default, tak terlihat dari luar (Java 9+)",
                    "",
                    "Field di interface juga istimewa: apa pun yang kamu tulis di sana otomatis",
                    "public static final, mau kata-kata itu kamu ketik atau tidak.",
                    "  double TARIF_ADMIN = 2500;   // sama saja: public static final double",
                    "Karena itu interface tetap tidak bisa menyimpan keadaan per objek - yang ada",
                    "di sana cuma konstanta, bukan field biasa.",
                    "",
                    "Dua contoh yang sudah kamu pakai tanpa sadar: List.of(...) adalah static method",
                    "DI interface List, dan nanti di materi Comparable & Comparator kamu akan",
                    "memanggil .reversed() - itu default method milik interface Comparator, yang",
                    "langsung ada di comparator apa pun tanpa pernah kamu tulis sendiri.",
                ]
            },
            {
                "heading": "default, static, private, dan konstanta di interface",
                "code": """interface Pembayaran {
    // Field di interface OTOMATIS public static final -- konstanta, bukan variabel.
    double TARIF_ADMIN = 2500;

    // Method biasa: tanpa isi, wajib diisi setiap pelaksana.
    double jumlah();

    // default: PUNYA isi. Bisa ditambahkan belakangan tanpa merusak class lama.
    default double total() {
        return jumlah() + biaya();
    }

    // private (Java 9+): penolong bersama antar-default, tidak terlihat dari luar.
    private double biaya() {
        return TARIF_ADMIN;
    }

    // static: milik interface-nya sendiri, dipanggil lewat Pembayaran.rupiah(...)
    static String rupiah(double n) {
        return "Rp" + Math.round(n);
    }
}

class Transfer implements Pembayaran {
    public double jumlah() { return 100000; }
    // Tidak menulis total() pun tetap dikompilasi: versi default yang dipakai.
}

class Tarik implements Pembayaran {
    public double jumlah() { return 50000; }

    @Override
    public double total() { return jumlah(); }   // default boleh ditimpa
}

public class Main {
    public static void main(String[] args) {
        System.out.println(Pembayaran.rupiah(new Transfer().total()));   // Rp102500
        System.out.println(Pembayaran.rupiah(new Tarik().total()));      // Rp50000
        System.out.println(Pembayaran.TARIF_ADMIN);                      // 2500.0
    }
}"""
            },
        ],
    },
    {
        "title": "19. Anotasi: Metadata untuk Compiler & Framework",
        "sections": [
            {
                "body": [
                    "Sejak materi Inheritance kamu sudah menulis @Override berkali-kali; nanti di JUnit ada",
                    "@Test, dan begitu masuk Spring Boot atau JPA — dua hal yang ditunjuk materi terakhir",
                    "kurikulum ini — isi berkasnya nyaris separuh @Entity, @Autowired, @GetMapping.",
                    "Selama ini semuanya cuma hafalan: 'kalau override, tulis @Override di atasnya'.",
                    "Padahal itu semua SATU jenis benda yang sama, namanya ANOTASI — dan siapa pun bisa",
                    "membuatnya sendiri, termasuk kamu.",
                    "",
                    "Anotasi = penanda yang ditempelkan pada sesuatu di dalam kode. Ditulis dengan @ lalu",
                    "namanya, diletakkan tepat di atas (atau di depan) benda yang ditandai.",
                    "",
                    "  @Override                          menempel di sebuah method",
                    "  @Entity                            menempel di sebuah class",
                    "  @Autowired                         menempel di sebuah field",
                    "  void simpan(@Valid Buku buku)      menempel di sebuah parameter",
                    "",
                    "Sekarang aturan yang paling penting, dan yang paling sering salah dipahami:",
                    "",
                    "  ANOTASI TIDAK MENGERJAKAN APA PUN DENGAN SENDIRINYA.",
                    "",
                    "Ia cuma tempelan, seperti stiker di kardus. Menempelkan @Test pada sebuah method tidak",
                    "membuat method itu berjalan — yang menjalankannya adalah JUnit, yang lebih dulu MEMBACA",
                    "stikernya. Anotasi yang tidak ada pembacanya sama saja dengan komentar: sah ditulis,",
                    "tidak berakibat apa-apa. Ini yang membuat kesalahan anotasi berbahaya, karena bentuk",
                    "gagalnya bukan error melainkan DIAM.",
                    "",
                    "Tiga golongan pembaca, dan golongannya menentukan KAPAN anotasi itu bekerja:",
                    "",
                    "  Pembaca            Bekerja saat        Contoh",
                    "  ----------------   -----------------   -------------------------------------------",
                    "  compiler (javac)   dikompilasi         @Override, @FunctionalInterface,",
                    "                                         @SuppressWarnings, @SafeVarargs",
                    "  alat bantu & IDE   menulis / build     @Deprecated (namanya dicoret di layar),",
                    "                                         Lombok (menuliskan kode untukmu)",
                    "  framework          program BERJALAN    @Test, @Entity, @RestController",
                    "",
                    "Jangan tertukar dengan @param, @return, @throws yang muncul DI DALAM blok /** ... */.",
                    "Yang di dalam komentar cuma teks untuk manusia dan alat dokumentasi; compiler membuang",
                    "seluruh komentar tanpa pernah melihat isinya. Pembedanya cuma satu: berada di dalam",
                    "/** */ atau tidak. Yang di luar itulah anotasi, dan ia betul-betul mengubah nasib kode.",
                ],
            },
            {
                "heading": "Lima anotasi bawaan yang wajib kamu kenali",
                "code": """import java.util.ArrayList;
import java.util.List;

class Hewan {
    void bersuara() {
        System.out.println("Hewan bersuara");
    }

    @Deprecated
    void suara() {                  // nama lama; masih jalan, tapi jangan dipakai lagi
        bersuara();
    }
}

class Kucing extends Hewan {
    @Override                       // "aku BERMAKSUD menimpa method milik induk"
    void bersuara() {
        System.out.println("Meow!");
    }
}

@FunctionalInterface                // "interface ini hanya boleh punya SATU abstract method"
interface Sapaan {
    String sapa(String nama);
}

public class Main {
    @SuppressWarnings("unchecked")  // "aku sudah tahu risikonya, jangan tegur aku"
    static List<String> daftarLama() {
        List mentah = new ArrayList();   // List tanpa <String>: compiler curiga
        mentah.add("Tom");
        return (List<String>) mentah;
    }

    public static void main(String[] args) {
        Hewan h = new Kucing();
        h.bersuara();                     // Meow!
        System.out.println(daftarLama()); // [Tom]
    }
}""",
            },
            {
                "body": [
                    "Program di atas jalan dan mencetak dua baris. Yang menarik justru bukan keluarannya,",
                    "melainkan apa yang terjadi kalau anotasinya diutak-atik.",
                    "",
                    "@Override — penyelamat dari salah ketik.",
                    "  Coba ubah 'void bersuara()' di class Kucing jadi 'void bersura()'. Tanpa @Override,",
                    "  itu SAH: Java menganggapnya method baru yang kebetulan bernama lain, Kucing tetap",
                    "  mewarisi bersuara() dari Hewan, dan programnya mencetak 'Hewan bersuara'. Tidak ada",
                    "  error, tidak ada peringatan — cuma perilaku yang salah dan sulit dilacak.",
                    "  Dengan @Override, javac langsung menolak:",
                    "    error: method does not override or implement a method from a supertype",
                    "  Jebakan yang sama menunggu di parameter yang meleset, dan itu bukan kasus langka:",
                    "  menulis equals(Kucing lain) alih-alih equals(Object lain) adalah kesalahan klasik",
                    "  yang cuma @Override yang menangkapnya. Tulis @Override setiap kali kamu override.",
                    "",
                    "@Deprecated — 'masih ada, tapi jangan dipakai lagi'.",
                    "  Method-nya tetap berfungsi (kode lama tidak boleh mendadak rusak), tapi yang",
                    "  memanggilnya kena peringatan dan IDE mencoret namanya:",
                    "    warning: [deprecation] suara() in Hewan has been deprecated",
                    "  Kamu akan sering melihatnya di library: pertanda ada cara baru yang lebih benar.",
                    "",
                    "@SuppressWarnings(\"unchecked\") — membungkam peringatan, BUKAN memperbaikinya.",
                    "  Hapus baris itu lalu kompilasi dengan 'javac -Xlint:all Main.java': muncul empat",
                    "  peringatan rawtypes dan unchecked, karena List tanpa <String> membuat compiler tidak",
                    "  lagi bisa menjamin isinya String. Anotasinya cuma menyuruh compiler diam. Bahayanya",
                    "  jelas: kalau ternyata isinya memang salah, kamu baru tahu saat program crash.",
                    "  Pasang hanya kalau kamu sudah memeriksa sendiri, dan sesempit mungkin — di satu",
                    "  method, bukan di seluruh class.",
                    "",
                    "@FunctionalInterface — mengunci sebuah interface tetap punya satu abstract method.",
                    "  Perhatikan bahwa Sapaan tidak dipakai sama sekali di program itu. Sengaja: anotasi",
                    "  ini bekerja pada DEKLARASI-nya, bukan pada pemakaiannya. Tambahkan satu method lagi",
                    "  ke Sapaan dan kompilasi gagal: 'Unexpected @FunctionalInterface annotation'. Tanpa",
                    "  anotasinya, penambahan itu diterima, dan yang rusak adalah semua lambda yang sudah",
                    "  terlanjur memakainya di tempat lain (lihat materi Lambda Expression).",
                    "",
                    "@SafeVarargs — janji bahwa method varargs bergenerik tidak akan menyalahgunakan",
                    "  argumennya. Jarang kamu tulis sendiri; cukup kenali bentuknya saat membaca library.",
                    "",
                    "Anotasi yang membawa argumen.",
                    "  Banyak anotasi butuh keterangan tambahan. Bentuknya seperti memanggil method:",
                    "",
                    "    @DisplayName(\"Penjumlahan dua angka positif\")",
                    "    @Column(name = \"nama_lengkap\", nullable = false)",
                    "    @SuppressWarnings({\"unchecked\", \"rawtypes\"})       // beberapa nilai: pakai { }",
                    "",
                    "  Argumennya ditulis 'nama = nilai', dipisah koma. Tapi ada satu jalan pintas yang",
                    "  membuat orang bingung sendiri saat membaca kode Spring:",
                    "",
                    "    @RequestMapping(\"/user\")   sama persis dengan   @RequestMapping(value = \"/user\")",
                    "",
                    "  Kalau kamu cuma mengisi SATU argumen dan namanya kebetulan 'value', namanya boleh",
                    "  dihilangkan. Jadi @Table(\"buku\") dan @Table(name = \"buku\") bukan dua fitur berbeda —",
                    "  yang satu cuma singkatan, dan hanya berlaku untuk argumen bernama value.",
                    "",
                    "  Nilainya harus konstanta yang sudah pasti saat kompilasi: teks, angka, true/false,",
                    "  enum, atau .class. Tidak boleh hasil pemanggilan method atau isi variabel biasa.",
                    "",
                    "  Beberapa anotasi boleh ditumpuk di satu benda. Tidak pakai koma, urutannya bebas:",
                    "",
                    "    @Test",
                    "    @DisplayName(\"Saldo tidak boleh minus\")",
                    "    void testSaldo() { ... }",
                ],
            },
            {
                "heading": "Membuat anotasi sendiri, lalu membacanya seperti framework",
                "code": """import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;
import java.lang.reflect.Method;

@Retention(RetentionPolicy.RUNTIME)   // ikut terbawa sampai program BERJALAN
@Target(ElementType.METHOD)           // hanya boleh menempel di method
@interface Langkah {
    String nama();
    int urutan();
}

class Laporan {
    @Langkah(nama = "Ambil data penjualan", urutan = 1)
    public void ambil() {
        System.out.println("   ...membaca 120 baris transaksi");
    }

    @Langkah(nama = "Hitung total", urutan = 2)
    public void hitung() {
        System.out.println("   ...total = 4.500.000");
    }

    public void bantuanInternal() {       // tanpa @Langkah, tidak ikut dipanggil
        System.out.println("   ...baris ini tidak pernah muncul");
    }
}

public class Main {
    public static void main(String[] args) throws Exception {
        Method[] rencana = new Method[3];    // slot 1 dan 2 yang dipakai

        // Inilah yang dikerjakan framework: memeriksa isi class, mencari tanda.
        for (Method m : Laporan.class.getDeclaredMethods()) {
            if (m.isAnnotationPresent(Langkah.class)) {
                Langkah tanda = m.getAnnotation(Langkah.class);
                rencana[tanda.urutan()] = m;
            }
        }

        Laporan laporan = new Laporan();
        for (int i = 1; i < rencana.length; i++) {
            Langkah tanda = rencana[i].getAnnotation(Langkah.class);
            System.out.println(i + ". " + tanda.nama());
            rencana[i].invoke(laporan);      // panggil method-nya
        }
    }
}""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "",
                    "  1. Ambil data penjualan",
                    "     ...membaca 120 baris transaksi",
                    "  2. Hitung total",
                    "     ...total = 4.500.000",
                    "",
                    "Tujuan contoh ini bukan supaya kamu sering menulisnya — dalam setahun pertama mungkin",
                    "tidak sekali pun. Tujuannya menghapus kesan 'sihir': kamu baru saja membuat @Langkah",
                    "sendiri, dan ia bekerja persis seperti @Test bekerja.",
                    "",
                    "Bedah barisnya:",
                    "  @interface Langkah { ... }   mendeklarasikan anotasi baru. Perhatikan '@' menempel",
                    "                               di 'interface' — beda dari interface biasa.",
                    "  String nama();               'argumen' anotasi ditulis seperti method tanpa isi.",
                    "                               Boleh diberi bawaan: int urutan() default 99;",
                    "  @Retention(...RUNTIME)       sampai kapan tanda ini bertahan.",
                    "  @Target(ElementType.METHOD)  boleh ditempel di mana saja.",
                    "",
                    "Ya, @Retention dan @Target itu sendiri adalah anotasi yang menempel pada anotasi.",
                    "Tidak ada tingkatan khusus di sini; semuanya benda biasa.",
                    "",
                    "@Retention punya tiga pilihan, dan salah pilih adalah kesalahan yang paling sering",
                    "membuat anotasi buatan sendiri 'tidak jalan':",
                    "  SOURCE   dibuang setelah dikompilasi. Cuma untuk compiler & alat bantu (@Override).",
                    "  CLASS    ikut ke berkas .class, tapi tidak dimuat saat berjalan. INI BAWAANNYA.",
                    "  RUNTIME  masih bisa dibaca saat program berjalan. Wajib untuk framework.",
                    "Hapus baris @Retention di program tadi: ia tetap dikompilasi tanpa keluhan sedikit pun,",
                    "lalu mati saat dijalankan dengan NullPointerException — karena isAnnotationPresent",
                    "tidak menemukan apa-apa. Gagal diam, lagi.",
                    "",
                    "@Target menutup lubang yang lain: coba tempelkan @Langkah pada class Laporan, dan",
                    "javac menolak dengan 'annotation type not applicable to this kind of declaration'.",
                    "Nilai yang sering dipakai: TYPE (class/interface/enum), METHOD, FIELD, PARAMETER,",
                    "CONSTRUCTOR. Boleh lebih dari satu: @Target({ElementType.METHOD, ElementType.FIELD}).",
                    "",
                    "Bagian 'Laporan.class.getDeclaredMethods()' itu namanya REFLEKSI: kemampuan program",
                    "memeriksa dirinya sendiri saat berjalan — daftar method sebuah class, anotasi yang",
                    "menempel padanya, lalu memanggil method itu lewat invoke(). Kamu tidak perlu menguasai",
                    "refleksi sekarang. Cukup tahu bahwa inilah seluruh rahasia framework Java: tidak ada",
                    "keajaiban, cuma sebuah program yang membaca tanda lalu bertindak.",
                    "",
                    "Tur singkat anotasi yang akan kamu temui di kode nyata:",
                    "",
                    "  Anotasi                 Dari        Yang sebenarnya diminta",
                    "  ---------------------   ---------   ----------------------------------------------",
                    "  @Test                   JUnit       jalankan method ini sebagai satu kasus uji",
                    "  @BeforeEach             JUnit       jalankan ini dulu, sebelum SETIAP @Test",
                    "  @DisplayName(\"...\")     JUnit       pakai kalimat ini di laporan, bukan nama method",
                    "  @Service, @Component    Spring      buatkan satu objek class ini dan kelola untukku",
                    "  @Autowired              Spring      isikan field ini dengan objek yang kamu kelola",
                    "  @RestController         Spring      class ini melayani HTTP dan menjawab JSON",
                    "  @GetMapping(\"/buku\")    Spring      panggil method ini kalau ada GET ke /buku",
                    "  @Entity                 JPA         class ini mewakili satu TABEL di database",
                    "  @Id                     JPA         field ini primary key-nya",
                    "  @Column(name = \"...\")   JPA         field ini menempel ke kolom bernama itu",
                    "  @JsonProperty(\"nama\")   Jackson     saat diubah jadi JSON, pakai nama itu",
                    "  @Data                   Lombok      TULISKAN getter, setter, toString, equals,",
                    "                                      hashCode-nya untukku saat kompilasi",
                    "  @Builder                Lombok      buatkan cara membangun objek ini bertahap",
                    "",
                    "Lombok pantas dicurigai lebih dulu waktu kamu bingung. Ia menuliskan method SUNGGUHAN",
                    "saat kompilasi, jadi getNama() betul-betul ada dan bisa dipanggil — tapi tidak akan",
                    "kamu temukan di berkasnya, berapa kali pun kamu menggulir. Kalau sebuah method 'tidak",
                    "ada tapi dipanggil', lihat anotasi di kepala class-nya.",
                    "",
                    "Jebakan yang benar-benar memakan waktu orang:",
                    "  1. Anotasi dari paket yang salah. org.junit.Test (JUnit 4) dan",
                    "     org.junit.jupiter.api.Test (JUnit 5) sama-sama bernama @Test. Salah import berarti",
                    "     test-nya tidak pernah dijalankan, dan laporannya bilang 'semua lulus'.",
                    "  2. Anotasi tanpa pembaca. @Autowired di class yang dibuat sendiri dengan 'new' tidak",
                    "     diisi siapa pun — Spring hanya mengurus objek yang IA yang buat.",
                    "  3. Anotasi buatan sendiri tanpa @Retention(RUNTIME). Sudah dibahas di atas.",
                    "",
                    "Cara membaca kode Spring atau JPA tanpa panik, dan ini yang paling berguna dibawa:",
                    "coret dulu semua barisnya yang diawali @. Yang tersisa hampir selalu class dan method",
                    "Java biasa yang sudah kamu pahami. Sesudah itu baru baca anotasinya satu per satu",
                    "sebagai perintah kepada framework: 'buatkan objeknya', 'petakan ke tabel', 'panggil",
                    "kalau ada request'. Yang kamu tulis adalah isi method-nya; sisanya dikerjakan mesin",
                    "yang membaca tanda. Dan kalau ada anotasi yang tidak kamu kenal, arahkan kursor lalu",
                    "tekan Ctrl+klik di IDE — anotasi itu berkas biasa berisi '@interface', bisa dibaca.",
                ],
            },
        ],
    },
    {
        "title": "20. Record & Sintaks Java Modern",
        "sections": [
            {
                "body": [
                    "Semua yang kamu pelajari sampai materi ini masih berlaku persis. Yang berubah adalah",
                    "cara orang MENULISKANNYA. Sejak Java 17 lalu 21 jadi versi LTS, berkas Java baru yang",
                    "kamu buka di GitHub atau di kantor memakai empat hal yang belum pernah disebut di sini:",
                    "record, text block, switch ekspresi bentuk penuh, dan sealed. Tanpa keempatnya, kode",
                    "Java tahun ini terlihat seperti bahasa lain — dan macetnya biasanya di baris pertama.",
                    "",
                    "MASALAH YANG DISELESAIKAN RECORD.",
                    "Class yang tugasnya cuma membawa data selalu berbentuk begini:",
                    "",
                    "  class Titik {",
                    "      private final int x;",
                    "      private final int y;",
                    "      Titik(int x, int y) { this.x = x; this.y = y; }",
                    "      public int getX() { return x; }",
                    "      public int getY() { return y; }",
                    "      @Override public boolean equals(Object o) { ...delapan baris... }",
                    "      @Override public int hashCode() { ...dua baris... }",
                    "      @Override public String toString() { ...dua baris... }",
                    "  }",
                    "",
                    "Tiga puluh baris untuk menyimpan dua angka, dan tidak ada satu pun keputusan di",
                    "dalamnya — semuanya bisa ditebak dari nama dan tipe fieldnya. Java 16 menyediakan",
                    "bentuk singkatnya, dan baris di bawah ini SAMA persis dengan class tiga puluh baris tadi:",
                    "",
                    "  public record Titik(int x, int y) { }",
                    "",
                    "Yang dibuatkan Java dari satu baris itu:",
                    "",
                    "  - dua field private final bernama x dan y. Tidak kamu tulis, tapi benar-benar ada.",
                    "  - canonical constructor: new Titik(3, 4), urutan parameternya persis urutan di kurung.",
                    "  - dua method pembaca: x() dan y().",
                    "  - equals(Object): true kalau SEMUA komponennya sama.",
                    "  - hashCode(): otomatis sepasang dengan equals-nya, jadi HashMap dan HashSet langsung",
                    "    berperilaku benar. Kenapa keduanya wajib sepasang: lihat materi Class Object.",
                    "  - toString(): menghasilkan \"Titik[x=3, y=4]\", bukan Titik@1b6d3586.",
                    "",
                    "Kata di dalam kurung itu namanya KOMPONEN — bukan parameter, bukan field.",
                    "",
                    "KENAPA GETTERNYA x(), BUKAN getX()?",
                    "Karena tiap komponen mendapat satu method bernama sama persis dengan komponennya.",
                    "Aturan getX() itu konvensi JavaBeans dari 1997, dibuat untuk objek yang datanya bisa",
                    "diubah lewat pasangan getX()/setX(); record bukan itu, jadi awalan get- tidak dipakai.",
                    "Akibatnya saat kamu MEMBACA kode: begitu melihat p.harga() tanpa \"get\", jangan capek",
                    "mencari method harga() di badan class — biasanya memang tidak ada satu pun di sana.",
                    "Akibatnya saat kamu MENULIS kode: mengetik p.getHarga() pada sebuah record menghasilkan",
                    "  error: cannot find symbol",
                    "dan pemula biasanya menyangka ada import yang kurang, padahal namanya memang bukan itu.",
                    "",
                    "KENAPA TIDAK ADA SETTER?",
                    "Semua field record final. Tidak ada setX(), dan menulis x = 5 di dalam record ditolak:",
                    "  error: cannot assign a value to final variable x",
                    "Ini bukan keterbatasan yang perlu diakali, ini seluruh gunanya. Objek yang tidak bisa",
                    "berubah (immutable) aman jadi kunci HashMap, aman dipakai beberapa thread sekaligus,",
                    "dan tidak pernah berubah diam-diam gara-gara dioper ke method milik orang lain.",
                    "Cara \"mengubahnya\": bikin objek BARU — lihat method denganAngka() di contoh berikutnya.",
                    "",
                    "Jebakan yang halus: final-nya cuma sedalam satu lapis.",
                    "  record Tim(String nama, List<String> anggota) { }",
                    "Field anggota tidak bisa DIGANTI dengan list lain, tapi isi list itu masih bisa ditambah",
                    "dan dihapus siapa pun yang memegangnya. Kalau isinya harus benar-benar beku, salin di",
                    "compact constructor:  anggota = List.copyOf(anggota);",
                    "",
                    "COMPACT CONSTRUCTOR: constructor tanpa daftar parameter, isinya validasi dan perapian.",
                    "",
                    "  record Nilai(String nama, int angka) {",
                    "      Nilai {                        // perhatikan: TIDAK ada (String nama, int angka)",
                    "          if (angka < 0) throw new IllegalArgumentException(\"negatif\");",
                    "          nama = nama.trim();        // menimpa PARAMETER, dan itulah yang disimpan",
                    "      }",
                    "  }",
                    "",
                    "Menulis this.nama = nama di dalamnya justru error: pengisian field dikerjakan Java",
                    "SESUDAH blok itu selesai. Yang boleh kamu lakukan cuma dua — melempar exception, dan",
                    "menimpa nilai parameternya sebelum disimpan.",
                    "",
                    "Yang BOLEH ditambahkan ke badan record: method biasa, method static, konstanta static,",
                    "constructor lain (baris pertamanya wajib this(...)), dan implements interface apa pun.",
                    "Yang TIDAK boleh, beserta pesan compilernya:",
                    "",
                    "  - field instance tambahan  ->  error: field declaration must be static",
                    "  - extends class lain       ->  error: '{' expected",
                    "    (record sudah otomatis menurunkan java.lang.Record, dan Java cuma punya satu induk)",
                    "",
                    "Record tetap boleh implements berapa pun interface. Itulah kenapa ia cocok dengan sealed",
                    "di bagian akhir materi ini.",
                    "",
                    "KAPAN RECORD TEPAT:",
                    "",
                    "  - DTO: bentuk data yang lewat antar lapisan, request dan response sebuah API.",
                    "  - Satu baris hasil query database.",
                    "  - Nilai gabungan: Koordinat(x, y), Rentang(awal, akhir), Uang(jumlah, mataUang).",
                    "  - Kunci HashMap gabungan, karena equals dan hashCode-nya sudah benar sejak lahir.",
                    "  - Node pohon parser, berpasangan dengan sealed.",
                    "",
                    "KAPAN RECORD TIDAK TEPAT:",
                    "",
                    "  - Fieldnya memang harus berubah sepanjang hidup objek: keranjang belanja, koneksi,",
                    "    objek yang menyimpan status. Untuk itu class biasa tetap jawabannya.",
                    "  - Entity JPA/Hibernate. Framework itu membuat objeknya lewat constructor KOSONG lalu",
                    "    mengisi field satu per satu; record tidak menyediakan keduanya. Pola yang lazim:",
                    "    class biasa untuk entity, record untuk DTO yang dikirim keluar.",
                    "  - Butuh pewarisan bertingkat lewat extends.",
                ],
            },
            {
                "heading": "Record, text block, dan switch ekspresi dalam satu program",
                "code": "import java.util.List;\n\ninterface Bernilai {\n    char grade();\n}\n\nrecord Nilai(String nama, int angka) implements Bernilai {\n\n    // Compact constructor: tempat validasi & perapian.\n    // Perhatikan: TIDAK ada \"this.nama = nama;\" -- Java yang mengisikannya.\n    Nilai {\n        if (angka < 0 || angka > 100) {\n            throw new IllegalArgumentException(\"nilai di luar 0-100: \" + angka);\n        }\n        nama = nama.trim();\n    }\n\n    // Constructor tambahan WAJIB memanggil constructor utama lewat this(...)\n    Nilai(String nama) {\n        this(nama, 0);\n    }\n\n    @Override\n    public char grade() {\n        return switch (angka / 10) {\n            case 10, 9 -> 'A';            // satu cabang, beberapa label\n            case 8 -> 'B';\n            case 7 -> 'C';\n            default -> {                  // badan berkurung: nilainya lewat yield\n                char sementara = angka >= 60 ? 'D' : 'E';\n                yield sementara;\n            }\n        };\n    }\n\n    // Record tidak bisa diubah; yang \"mengubah\" mengembalikan objek BARU.\n    Nilai denganAngka(int baru) {\n        return new Nilai(nama, baru);\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Nilai a = new Nilai(\"  Andi  \", 92);\n        Nilai b = new Nilai(\"Andi\", 92);\n\n        System.out.println(a.nama() + \" / \" + a.angka());   // getter tanpa \"get\"\n        System.out.println(a);                              // toString otomatis\n        System.out.println(a.equals(b));                    // equals otomatis\n        System.out.println(a.grade() + \" \" + new Nilai(\"Budi\", 64).grade());\n\n        Nilai c = a.denganAngka(70);\n        System.out.println(a + \" -> \" + c);                 // a TIDAK berubah\n\n        String sql = \"\"\"\n                SELECT nama, angka\n                FROM nilai\n                WHERE angka >= 70\n                ORDER BY angka DESC\"\"\";\n\n        String json = \"\"\"\n                {\n                  \"nama\": \"Andi\",\n                  \"grade\": \"A\"\n                }\"\"\";\n\n        System.out.println(sql);\n        System.out.println(json);\n\n        for (Nilai n : List.of(a, c, new Nilai(\"Cici\"))) {\n            System.out.printf(\"%-6s %3d %c%n\", n.nama(), n.angka(), n.grade());\n        }\n\n        try {\n            new Nilai(\"Dedi\", 120);\n        } catch (IllegalArgumentException e) {\n            System.out.println(\"ditolak: \" + e.getMessage());\n        }\n    }\n}",
            },
            {
                "body": [
                    "Keluarannya:",
                    "",
                    "  Andi / 92                       <- nama() sudah ter-trim compact constructor",
                    "  Nilai[nama=Andi, angka=92]      <- toString bawaan record",
                    "  true                            <- equals membandingkan ISI, bukan alamat",
                    "  A D",
                    "  Nilai[nama=Andi, angka=92] -> Nilai[nama=Andi, angka=70]",
                    "  SELECT nama, angka",
                    "  FROM nilai",
                    "  WHERE angka >= 70",
                    "  ORDER BY angka DESC",
                    "  {",
                    "    \"nama\": \"Andi\",",
                    "    \"grade\": \"A\"",
                    "  }",
                    "  Andi    92 A",
                    "  Andi    70 C",
                    "  Cici     0 E",
                    "  ditolak: nilai di luar 0-100: 120",
                    "",
                    "Tiga baris yang rapi berkolom itu datang dari printf, bukan println:",
                    "",
                    "  System.out.printf(\"%-6s %3d %c%n\", nama, angka, grade);",
                    "",
                    "Bacanya begini: %-6s teks rata KIRI selebar 6, %3d angka rata KANAN",
                    "selebar 3, %c satu karakter, dan %n ganti baris. Nilainya diambil",
                    "berurutan dari argumen sesudah tanda kutip. Itu sebabnya kolomnya",
                    "sejajar walau nama-namanya berbeda panjang — sesuatu yang mustahil",
                    "dirapikan dengan println dan tanda tambah. Seluruh daftar penanda",
                    "beserta jebakannya ada di materi String & Scanner; di sini cukup tahu",
                    "bahwa printf itu println yang bisa diberi cetakan.",
                    "",
                    "TEXT BLOCK (Java 15+): string yang dibuka dan ditutup tiga tanda kutip.",
                    "Sebelum ada ini, SQL empat baris terpaksa ditulis begini:",
                    "",
                    "  String sql = \"SELECT nama, angka\\n\" +",
                    "               \"FROM nilai\\n\" +",
                    "               \"WHERE angka >= 70\";",
                    "",
                    "Tiap baris butuh tanda kutip, tanda tambah, dan \\n-nya sendiri. Satu \\n kelupaan dan",
                    "querymu berbunyi \"...angkaFROM nilai\" — errornya muncul jauh dari tempat salahnya.",
                    "Di JSON lebih parah: setiap tanda kutip di dalamnya harus ditulis \\\" sampai barisnya",
                    "tidak terbaca manusia lagi. Di dalam text block, tanda kutip ditulis apa adanya.",
                    "",
                    "Tiga aturannya, dan ketiganya pernah menjebak semua orang:",
                    "",
                    "  1. Tiga kutip pembuka WAJIB langsung diikuti ganti baris.",
                    "  2. Indentasi yang dipakai bersama dipotong otomatis.",
                    "  3. Penutup yang berdiri di baris sendiri menambah satu baris kosong di ujung.",
                    "",
                    "Aturan 1 berarti tiga kutip lalu SELECT lalu tiga kutip dalam satu baris ditolak",
                    "compiler. Isi stringnya harus mulai di baris berikutnya.",
                    "",
                    "Aturan 2 yang paling sering menggigit. Java mencari baris yang paling sedikit",
                    "menjoroknya — TERMASUK baris tempat tiga kutip PENUTUP berdiri — lalu memotong",
                    "sebanyak itu dari SEMUA baris. Itu sebabnya kode yang menjorok rapi di dalam method",
                    "tidak menyeret spasinya ikut masuk ke isi string. Konsekuensi yang mengagetkan:",
                    "memindahkan penutupnya ke kolom nol mengembalikan SELURUH spasi indentasi ke dalam",
                    "stringnya. Bug ini tidak menghentikan apa pun — SQL-nya tetap jalan — tapi teks di",
                    "log jadi menjorok aneh, dan perbandingan dengan equals mendadak gagal tanpa kelihatan",
                    "kenapa.",
                    "",
                    "Aturan 3: kalau kamu tidak mau baris kosong di akhir, tempelkan tiga kutip penutup di",
                    "ujung baris terakhir isinya — persis seperti sql dan json di program tadi.",
                    "",
                    "Dua escape yang cuma ada di text block:",
                    "",
                    "  \\ di ujung baris   sambung ke baris berikutnya TANPA ganti baris. Berguna untuk",
                    "                     satu kalimat panjang yang ingin ditulis rapi di beberapa baris.",
                    "  \\s                 satu spasi yang tidak ikut dibuang. Spasi di ujung tiap baris",
                    "                     selalu dipangkas Java, dan itu memang biasanya yang kamu mau.",
                    "",
                    "SWITCH EKSPRESI, BENTUK PENUHNYA.",
                    "Materi Percabangan sudah memperkenalkan bentuk panah satu baris. Tiga hal berikut",
                    "belum, dan ketiganya ada di method grade() tadi:",
                    "",
                    "  1. Satu cabang boleh punya beberapa label:  case 10, 9 -> 'A';",
                    "  2. Cabang berbadan kurung menyerahkan nilainya lewat yield, bukan return.",
                    "  3. Tidak ada break sama sekali, dan itu memang bukan kelalaian.",
                    "",
                    "Label berkoma menggantikan pola lama case 10: case 9: yang mengandalkan fall-through —",
                    "pola yang cuma bekerja kalau break-nya sengaja dihilangkan, dan yang selalu membuat",
                    "pembacanya ragu apakah itu disengaja atau lupa.",
                    "",
                    "yield dipakai begitu sebuah cabang butuh lebih dari satu baris:",
                    "",
                    "  default -> {",
                    "      char sementara = angka >= 60 ? 'D' : 'E';",
                    "      yield sementara;",
                    "  }",
                    "",
                    "Menulis return di dalamnya ditolak:",
                    "  error: attempt to return out of a switch expression",
                    "Alasannya masuk akal begitu dipikir: return keluar dari seluruh METHOD, sedangkan yang",
                    "dibutuhkan di sini cuma satu nilai untuk satu cabang.",
                    "",
                    "Soal break: bentuk panah TIDAK punya fall-through sama sekali, tiap cabang berdiri",
                    "sendiri. break cuma urusan bentuk lama yang memakai titik dua.",
                    "",
                    "Beda switch EKSPRESI dan switch STATEMENT, dan ini yang paling sering menggigit:",
                    "ekspresi wajib menghasilkan nilai untuk SETIAP kemungkinan masukan. Tanpa default,",
                    "compiler menolak dengan",
                    "  error: the switch expression does not cover all possible input values",
                    "Statement (yang tidak menghasilkan nilai) tidak menuntut itu. Pengecualiannya ada di",
                    "bagian berikutnya: enum dan sealed bisa dinyatakan tuntas tanpa default.",
                    "",
                    "Dan jangan mencampur dua bentuk label dalam satu switch:",
                    "",
                    "  case 1 -> ...;",
                    "  case 2: ...;     ->  error: different case kinds used in the switch",
                    "",
                    "Pilih satu bentuk untuk seluruh switch itu.",
                ],
            },
            {
                "body": [
                    "Sisa materi ini soal dua fitur yang hampir selalu muncul bersama record.",
                    "",
                    "PATTERN MATCHING. Sejak Java 16, instanceof boleh sekalian memberi nama variabelnya:",
                    "  if (h instanceof Kucing k) { k.mengeong(); }",
                    "Sebelumnya kamu menulis dua langkah — periksa dengan instanceof, lalu cast manual",
                    "(lihat materi Polymorphism). Bentuk baru menggabungkan keduanya, dan k cuma ada di",
                    "dalam blok yang memang sudah pasti Kucing, jadi cast yang salah tidak mungkin terjadi.",
                    "",
                    "Sejak Java 21, pola yang sama boleh jadi label switch:",
                    "",
                    "  String suara = switch (h) {",
                    "      case Kucing k -> k.nama() + \" bilang meong\";",
                    "      case Anjing a -> a.nama() + \" bilang guk\";",
                    "      case null     -> \"tidak ada hewan\";",
                    "      default       -> \"hewan lain\";",
                    "  };",
                    "",
                    "Inilah yang menggantikan rantai if-instanceof panjang yang dulu wajib ditulis: satu",
                    "ekspresi, satu nilai, dan variabelnya (k, a) langsung siap pakai di cabangnya sendiri.",
                    "",
                    "case null adalah perubahan besar yang gampang terlewat. Sepanjang sejarah Java, switch",
                    "atas nilai null selalu melempar NullPointerException, jadi orang terbiasa menaruh",
                    "if (h == null) di atasnya. Sekarang null boleh jadi cabang biasa. Tapi baca aturannya",
                    "dengan teliti: kalau case null TIDAK kamu tulis, perilaku lamanya masih berlaku —",
                    "switch-nya tetap melempar NullPointerException. null TIDAK jatuh ke default.",
                    "",
                    "Boleh menambahkan syarat dengan when:",
                    "  case Lingkaran l when l.jari() > 100 -> \"lingkaran raksasa\";",
                    "Di sini urutan case jadi penting: yang ber-when ditulis SEBELUM versi tanpa syarat,",
                    "karena cabang pertama yang cocok itulah yang dipakai. Dibalik urutannya, cabang",
                    "ber-when tidak akan pernah kena — dan compiler menolak cabang yang jelas tak terjangkau.",
                    "",
                    "Karena record tahu persis komponennya, Java 21 juga membolehkan membongkar isinya",
                    "langsung di label. Namanya record pattern:",
                    "  case Persegi(double sisi) -> \"persegi sisi \" + sisi;",
                    "Sama saja dengan case Persegi p -> ... lalu memakai p.sisi(), cuma tanpa singgah di p.",
                    "",
                    "SEALED (Java 17+): membatasi siapa saja yang boleh menurunkan sebuah tipe.",
                    "  sealed interface Bentuk permits Lingkaran, Persegi, Segitiga { }",
                    "Artinya tidak ada class lain di mana pun yang boleh implements Bentuk. Interface biasa",
                    "terbuka untuk siapa saja (lihat materi Abstract & Interface); sealed menutupnya jadi",
                    "daftar tertutup yang bisa dihitung. Setiap nama di permits wajib ikut memilih satu:",
                    "final, sealed lagi, atau non-sealed (\"mulai dari sini boleh diturunkan bebas lagi\").",
                    "Record otomatis final, jadi ia memenuhi syarat itu tanpa kata tambahan — itu sebabnya",
                    "sealed + record jadi pasangan yang begitu sering kamu lihat.",
                    "",
                    "Hadiahnya ada di compiler. Karena daftar turunannya tertutup, switch yang mencakup",
                    "ketiganya dianggap TUNTAS dan default boleh dihilangkan. Suatu hari kamu menambah",
                    "Trapesium ke permits: setiap switch yang belum menanganinya langsung ditolak dengan",
                    "  error: the switch expression does not cover all possible input values",
                    "Bandingkan dengan menulis default -> throw new IllegalStateException(...): bug yang",
                    "sama persis baru ketahuan saat program sudah jalan, dari laporan pemakai. Ini prinsip",
                    "yang sama dengan switch atas enum tanpa default (lihat materi Enum), diperluas ke",
                    "class dan record.",
                    "",
                    "VERSI JAVA — cek punyamu dengan  java -version:",
                    "",
                    "  14  switch ekspresi (panah, yield)     15  text block",
                    "  16  record, instanceof berpola         17  sealed",
                    "  21  pattern matching di switch, case null, when, record pattern",
                    "",
                    "Contoh terakhir di bawah butuh Java 21, jadi ia sengaja ditulis tanpa method main:",
                    "bentuknya memang berkas model yang dipakai berkas lain. Kalau kamu menyalinnya dan",
                    "javac-mu masih 17, pesannya:",
                    "  error: patterns in switch statements are a preview feature and are disabled by default.",
                    "Kodenya tidak salah — JDK-mu yang lebih tua. Bentuk inilah yang makin sering kamu",
                    "temui di kode Java baru, jadi mengenalinya lebih penting daripada bisa menjalankannya.",
                ],
            },
            {
                "heading": "sealed + record + switch pattern (butuh Java 21)",
                "code": """sealed interface Bentuk permits Lingkaran, Persegi, Segitiga {
    String nama();
}

record Lingkaran(double jari) implements Bentuk {
    Lingkaran {
        if (jari <= 0) {
            throw new IllegalArgumentException("jari harus positif");
        }
    }

    public String nama() {
        return "lingkaran";
    }
}

record Persegi(double sisi) implements Bentuk {
    public String nama() {
        return "persegi";
    }
}

record Segitiga(double alas, double tinggi) implements Bentuk {
    public String nama() {
        return "segitiga";
    }
}

final class Geometri {

    // Tanpa default: compiler yang memastikan ketiga bentuk sudah tercakup.
    // Tambah satu turunan baru di permits, baris ini langsung ditolak javac.
    static double luas(Bentuk b) {
        return switch (b) {
            case Lingkaran l -> Math.PI * l.jari() * l.jari();
            case Persegi p -> p.sisi() * p.sisi();
            case Segitiga s -> 0.5 * s.alas() * s.tinggi();
        };
    }

    static String ringkas(Bentuk b) {
        return switch (b) {
            case null -> "(tidak ada bentuk)";
            case Lingkaran l when l.jari() > 100 -> "lingkaran raksasa";
            case Lingkaran l -> "lingkaran jari " + l.jari();
            case Persegi(double sisi) -> "persegi sisi " + sisi;
            case Segitiga s -> "segitiga " + s.alas() + " x " + s.tinggi();
        };
    }
}""",
            },
        ],
    },
    {
        "title": "21. Exception Handling",
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
        "title": "22. Membaca Error: Stack Trace, Throwable, dan Logging",
        "sections": [
            {
                "body": [
                    "Materi Exception Handling mengajarkan cara MENANGKAP exception.",
                    "Materi ini kebalikannya: apa yang muncul di layar ketika tidak ada",
                    "yang menangkapnya. Itu pemandangan paling sering dalam hidup seorang",
                    "programmer Java, dan kebanyakan pemula refleks menutup terminalnya",
                    "padahal yang barusan muncul adalah petunjuk paling akurat yang akan",
                    "pernah mereka dapat soal apa yang rusak.",
                    "",
                    "Kalau sebuah exception naik terus sampai keluar dari main() tanpa",
                    "tertangkap, JVM menghentikan program lalu mencetak STACK TRACE:",
                    "",
                    "  Exception in thread \"main\" java.lang.NumberFormatException: For input string: \"8.000\"",
                    "      at java.base/java.lang.NumberFormatException.forInputString(NumberFormatException.java:67)",
                    "      at java.base/java.lang.Integer.parseInt(Integer.java:668)",
                    "      at java.base/java.lang.Integer.parseInt(Integer.java:786)",
                    "      at Jejak.hargaDari(Jejak.java:6)",
                    "      at Jejak.totalBelanja(Jejak.java:12)",
                    "      at Jejak.main(Jejak.java:19)",
                    "",
                    "Tiga aturan membacanya:",
                    "  1. Baris pertama = JENIS error dan PESANNYA. Di sini: ada teks yang",
                    "     gagal diubah jadi angka, dan teks itu \"8.000\". Bagian",
                    "     'Exception in thread \"main\"' cuma menyebut thread mana yang mati.",
                    "  2. Tiap baris 'at ...' adalah satu pemanggilan method yang sedang",
                    "     berlangsung saat error meledak. Urutannya dari DALAM ke LUAR:",
                    "     yang paling atas tempat meledaknya, yang paling bawah titik",
                    "     berangkatnya. Dibaca dari bawah ke atas, itu cerita lengkap",
                    "     'main memanggil totalBelanja, yang memanggil hargaDari, yang...'.",
                    "  3. Angka sesudah titik dua adalah NOMOR BARIS di berkas itu.",
                    "     'Jejak.java:12' berarti buka Jejak.java, lompat ke baris 12.",
                    "",
                    "Sekarang bagian yang paling menentukan: CARI BARIS YANG MENYEBUT KODE",
                    "SENDIRI. Tiga baris teratas bertanda 'java.base/' - itu isi perut JDK.",
                    "Membuka Integer.java tidak ada gunanya; parseInt tidak rusak, ia cuma",
                    "melapor bahwa yang kamu berikan bukan angka. Baris pertama yang",
                    "menyebut kelasmu sendiri, 'Jejak.hargaDari', itulah yang harus dibuka.",
                    "Di proyek nyata dengan Spring atau Hibernate, satu jejak bisa 60 baris",
                    "dan cuma tiga di antaranya milikmu. Memindai 60 baris itu dalam lima",
                    "detik adalah salah satu beda paling kentara antara pemula dan orang",
                    "yang sudah terbiasa - dan itu murni latihan, bukan bakat.",
                ],
            },
            {
                "heading": "Program yang menghasilkan jejak di atas",
                "code": """public class Jejak {
    // Program ini SENGAJA gagal. Jalankan, lalu cocokkan nomor barisnya
    // dengan jejak yang barusan kamu baca.

    static int hargaDari(String teks) {
        return Integer.parseInt(teks);
    }

    static int totalBelanja(String[] daftar) {
        int total = 0;
        for (String t : daftar) {
            total += hargaDari(t);
        }
        return total;
    }

    public static void main(String[] args) {
        String[] harga = {"12000", "9500", "8.000", "3000"};
        System.out.println("Total: " + totalBelanja(harga));
    }
}""",
            },
            {
                "body": [
                    "Kenapa 'catch (Exception e)' bisa menangkap begitu banyak hal berbeda?",
                    "Karena semua error di Java adalah OBJEK, dan objek-objek itu satu",
                    "keluarga:",
                    "",
                    "  Throwable                    <- akar; hanya turunannya boleh di-throw",
                    "    |",
                    "    +-- Error                  <- JVM-nya sendiri yang bermasalah",
                    "    |     +-- OutOfMemoryError       memori habis",
                    "    |     +-- StackOverflowError     rekursi tanpa ujung",
                    "    |",
                    "    +-- Exception              <- masalah wajar yang layak ditangani",
                    "          +-- IOException            checked",
                    "          +-- SQLException           checked",
                    "          +-- RuntimeException <- SEMUA turunannya unchecked",
                    "                +-- NullPointerException",
                    "                +-- NumberFormatException",
                    "                +-- ArithmeticException",
                    "                +-- IndexOutOfBoundsException",
                    "",
                    "Checked vs unchecked yang sudah kamu baca letaknya persis di pohon",
                    "ini: apa pun di bawah RuntimeException itu unchecked (compiler diam",
                    "saja), sisanya di bawah Exception itu checked (compiler memaksa kamu",
                    "menangani atau menuliskan throws).",
                    "",
                    "'catch (Exception e)' menyapu seluruh cabang Exception - lebar sekali,",
                    "dan itulah alasannya dipakai ketika kamu memang ingin apa pun",
                    "tertangkap. Yang TIDAK ikut tertangkap adalah cabang Error, dan itu",
                    "disengaja. Menangkap OutOfMemoryError lalu melanjutkan program sama",
                    "saja menempelkan lakban di atas lampu peringatan: memorinya tetap",
                    "habis, dan tidak ada satu pun yang bisa diperbaiki blok catch-mu.",
                    "Karena itu jangan pernah menulis 'catch (Throwable t)' - itu",
                    "satu-satunya cara ikut menelan cabang Error, dan hampir selalu ia",
                    "muncul di kode orang sebagai tanda menyerah, bukan tanda hati-hati.",
                    "",
                    "Satu hal lagi sebelum contoh berikutnya: System.out dan System.err",
                    "adalah dua aliran keluaran yang TERPISAH. System.out untuk hasil",
                    "program, System.err untuk keluhan - dan printStackTrace() memakai yang",
                    "kedua. Gunanya nyata: 'java Laporan > hasil.txt' hanya menampung",
                    "System.out, sehingga pesan error tetap terlihat di layar dan tidak ikut",
                    "mengotori berkas hasilnya. Sebaliknya, begitu keduanya ditampung di",
                    "tempat berbeda ('java Laporan > hasil.txt 2> galat.txt'), urutan relatif",
                    "antar keduanya HILANG - dari dua berkas itu tidak ada lagi cara tahu",
                    "baris mana yang tercetak lebih dulu. Alat yang membaca kedua pipa dengan",
                    "penyangga sendiri-sendiri (konsol IDE, log CI) pun bisa menampilkannya",
                    "tidak berurutan, jadi jangan jadikan posisi baris error di layar sebagai",
                    "bukti kapan ia terjadi. Aplikasi ini sendiri menaruh keduanya di dua",
                    "kotak berbeda saat kamu menekan 'Coba jalankan'.",
                ],
            },
            {
                "heading": "Objek e, dan membungkus exception",
                "body": [
                    "'e' di dalam blok catch bukan kata kunci, ia nama variabel biasa yang",
                    "menunjuk sebuah objek. Method warisan Throwable yang paling terpakai:",
                    "",
                    "  e.getMessage()       pesannya saja, tanpa nama kelas. BISA null -",
                    "                       banyak exception dilempar tanpa pesan, dan",
                    "                       \"Error: \" + e.getMessage() lalu mencetak",
                    "                       \"Error: null\". Kalau itu terjadi, cetak 'e'-nya",
                    "                       saja - toString() selalu punya isi.",
                    "  e.toString()         nama kelas + \": \" + pesan. Ini yang otomatis",
                    "                       dipanggil saat 'e' digabung ke String dengan +.",
                    "  e.printStackTrace()  cetak seluruh jejak ke System.err.",
                    "  e.getStackTrace()    jejak yang sama sebagai array; elemen [0] itu",
                    "                       baris teratas, alias tempat meledaknya.",
                    "  e.getCause()         exception yang menjadi SEBAB, atau null.",
                ],
                "code": """public class Konfigurasi {

    static int bacaPort(String teks) {
        try {
            return Integer.parseInt(teks);
        } catch (NumberFormatException e) {
            // Argumen kedua = sebab aslinya. Lupa mengisinya = jejak asli hilang.
            throw new RuntimeException("gagal memuat konfigurasi", e);
        }
    }

    public static void main(String[] args) {
        try {
            bacaPort("delapan puluh");
        } catch (RuntimeException e) {
            System.out.println("getMessage()  : " + e.getMessage());
            System.out.println("toString()    : " + e);
            System.out.println("getCause()    : " + e.getCause());
            System.out.println("baris pertama : " + e.getStackTrace()[0]);

            // printStackTrace() mencetak ke System.err, bukan System.out.
            e.printStackTrace();
        }
    }
}""",
            },
            {
                "body": [
                    "Empat baris pertama keluar lewat System.out, lalu printStackTrace()",
                    "mencetak ini ke System.err:",
                    "",
                    "  java.lang.RuntimeException: gagal memuat konfigurasi",
                    "      at Konfigurasi.bacaPort(Konfigurasi.java:8)",
                    "      at Konfigurasi.main(Konfigurasi.java:14)",
                    "  Caused by: java.lang.NumberFormatException: For input string: \"delapan puluh\"",
                    "      at java.base/java.lang.NumberFormatException.forInputString(NumberFormatException.java:67)",
                    "      at java.base/java.lang.Integer.parseInt(Integer.java:668)",
                    "      at java.base/java.lang.Integer.parseInt(Integer.java:786)",
                    "      at Konfigurasi.bacaPort(Konfigurasi.java:5)",
                    "      ... 1 more",
                    "",
                    "Inilah rantai sebab, dan urutan bacanya kebalikan dari dugaan orang.",
                    "Blok paling atas cuma BUNGKUSNYA. Kerusakan yang sesungguhnya ada di",
                    "blok 'Caused by' paling BAWAH - kalau ada tiga Caused by bertumpuk,",
                    "yang terakhir itulah yang menyebut penyebab aslinya. Jadi urutannya:",
                    "baca judul di atas untuk tahu apa yang gagal, lompat ke Caused by",
                    "terbawah untuk tahu kenapa, baru cari baris kode sendiri di situ.",
                    "'... 1 more' bukan sesuatu yang disembunyikan - artinya sisa barisnya",
                    "sama persis dengan jejak di atasnya, jadi tidak dicetak dua kali.",
                    "",
                    "Kenapa dibungkus? Pesan 'For input string: \"delapan puluh\"' sendirian",
                    "tidak memberi tahu siapa pun bahwa yang gagal adalah PEMUATAN",
                    "KONFIGURASI; teks itu bisa datang dari mana saja. Membungkus dengan",
                    "  throw new RuntimeException(\"gagal memuat konfigurasi\", e);",
                    "menambah konteks tanpa membuang sebabnya. Argumen KEDUA itu wajib:",
                    "tanpa 'e', seluruh Caused by lenyap dan yang tersisa cuma kalimat",
                    "sopan tanpa satu pun nomor baris. Itu kesalahan yang paling sering",
                    "membuat sebuah error jadi mustahil dilacak.",
                    "",
                    "Di kode profesional printStackTrace() nyaris tidak pernah dipakai.",
                    "Ia selalu ke System.err, tidak bisa dimatikan, tidak menyebut waktu",
                    "maupun kelas asalnya, dan tidak ikut masuk ke berkas log server.",
                    "Penggantinya LOGGER; di dunia Java kombinasi paling umum SLF4J +",
                    "Logback, dan bentuknya selalu mirip ini:",
                    "",
                    "  private static final Logger log = LoggerFactory.getLogger(Layanan.class);",
                    "",
                    "  } catch (SQLException e) {",
                    "      log.error(\"gagal simpan user {}\", id, e);",
                    "  }",
                    "",
                    "'{}' adalah tempat nilai disisipkan (di sini id). Argumen terakhir yang",
                    "bertipe exception TIDAK mengisi '{}' mana pun - ia dicetak sebagai",
                    "stack trace penuh. Satu baris itu memberi pesan, data, dan jejaknya",
                    "sekaligus. Tingkatnya, dari paling gawat:",
                    "  error  gagal, ada yang tidak jadi. Manusia perlu tahu.",
                    "  warn   aneh tapi masih jalan (percobaan ulang berhasil, setelan usang).",
                    "  info   peristiwa normal yang layak dicatat (aplikasi menyala, order masuk).",
                    "  debug  detail untuk menelusuri; biasanya dimatikan di server produksi.",
                    "",
                    "Tiga pola yang pasti kamu temui di kode orang dan sebaiknya tidak",
                    "kamu tiru:",
                    "  1. catch (Exception e) { }  <- blok kosong. Error terjadi, tidak ada",
                    "     satu pun jejak, dan program lanjut dengan data yang salah. Ini",
                    "     induk dari bug 'entah kenapa datanya hilang' yang bisa",
                    "     menghabiskan berhari-hari karena tidak ada apa pun untuk dibaca.",
                    "  2. catch (Exception e) { System.out.println(\"Error!\"); }  <- pesannya",
                    "     dibuang. \"Error!\" tidak memberi tahu apa pun kepada siapa pun.",
                    "  3. Menangkap, mencatat, lalu melanjutkan seolah tidak terjadi apa-apa.",
                    "     Kalau di titik itu kamu tidak sanggup memperbaiki keadaannya,",
                    "     lempar ulang dengan konteks, jangan ditelan.",
                    "",
                    "Aturannya sederhana: satu exception ditangani SEKALI, di tempat yang",
                    "benar-benar tahu harus berbuat apa. Selebihnya biarkan ia naik - jejak",
                    "yang utuh jauh lebih berharga daripada program yang pura-pura",
                    "baik-baik saja.",
                ],
            },
        ],
    },
    {
        "title": "23. Collection Framework",
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
                "body": [
                    "Sebelum lanjut: dua simbol asing di baris yang barusan kamu lihat.",
                    "",
                    "  List<String> nama = new ArrayList<>();",
                    "",
                    "<String> dibaca 'List yang ISINYA String'. Kurung sudut itu memberi tahu",
                    "compiler jenis barang apa yang boleh masuk, dan gunanya bukan sekadar rapi:",
                    "  nama.add(\"Andi\");   // OK",
                    "  nama.add(123);        // ditolak SAAT KOMPILASI, bukan saat program jalan",
                    "Sebagai imbalannya, saat mengambil isinya kamu langsung dapat String - tanpa",
                    "perlu cast. Ganti isinya dengan tipe lain sesuai kebutuhan: List<Integer>,",
                    "Set<String>, Map<String, Integer> (Map butuh dua: tipe key dan tipe value).",
                    "",
                    "Yang boleh masuk ke dalam kurung sudut hanya tipe OBJEK. List<int> ditolak;",
                    "yang benar List<Integer> (lihat materi Kelas Pembungkus).",
                    "",
                    "<> kosong di sebelah kanan namanya diamond operator. Java sudah tahu tipenya",
                    "dari sebelah kiri, jadi tidak perlu ditulis dua kali:",
                    "  List<String> nama = new ArrayList<String>();   // sah, tapi bertele-tele",
                    "  List<String> nama = new ArrayList<>();         // ini yang ditulis orang",
                    "",
                    "Perhatikan juga kebiasaan menulis List di KIRI dan ArrayList di kanan: yang",
                    "kiri interface (kontraknya), yang kanan implementasinya. Kalau suatu hari",
                    "ArrayList mau ditukar jadi LinkedList, cukup satu kata di sebelah kanan yang",
                    "berubah - seluruh kode lain yang memakai variabel itu aman.",
                    "",
                    "Nama lengkap mekanisme ini Generics, dan ia punya materinya sendiri nanti.",
                    "Untuk sekarang kamu cuma perlu bisa membacanya.",
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
                    "",
                    "Sejujurnya: tiga bentuk di beberapa baris terakhir ini sengaja DITUNJUKKAN",
                    "sekarang supaya kamu mengenalinya, bukan supaya langsung paham.",
                    "  String::compareTo    method reference (materi Lambda Expression)",
                    "  n -> n % 2 == 0      lambda           (materi Lambda Expression)",
                    "  .stream()...collect  Stream API       (materinya sendiri, nanti)",
                    "Ketiganya dijelaskan tuntas di materi-materi berikutnya. Kalau bagian akhir ini",
                    "terasa melompat, memang melompat - bukan kamu yang ketinggalan sesuatu.",
                ]
            },
        ],
    },
    {
        "title": "24. Iterasi, Perubahan, dan Idiom Collection Modern",
        "sections": [
            {
                "body": [
                    "Materi sebelumnya mengenalkan List, Set, dan Map. Materi ini soal apa yang terjadi",
                    "begitu kamu benar-benar MENGOLAH isinya: menelusurinya, mengubahnya sambil ditelusuri,",
                    "dan idiom-idiom yang dipakai di hampir semua kode Java nyata tapi tidak pernah muncul",
                    "di buku pengantar.",
                    "",
                    "KENAPA for-each BISA BEKERJA",
                    "",
                    "  for (String b : buah) { ... }",
                    "",
                    "Ini bukan sihir khusus untuk List. Ia bekerja untuk apa pun yang mengimplementasikan",
                    "interface Iterable, yang cuma menjanjikan satu method: iterator(). Iterator sendiri",
                    "punya tiga method inti: hasNext(), next(), dan remove().",
                    "",
                    "Kompilator menerjemahkan for-each di atas jadi persis loop ini:",
                    "",
                    "  for (Iterator<String> it = buah.iterator(); it.hasNext(); ) {",
                    "      String b = it.next();",
                    "      ...",
                    "  }",
                    "",
                    "Jadi for-each adalah singkatan, bukan mekanisme lain. Bentuk panjangnya masih ramai",
                    "dipakai di kode nyata karena ia satu-satunya cara memegang iterator-nya — dan itulah",
                    "yang dibutuhkan kalau kamu mau menghapus elemen di tengah jalan.",
                    "",
                    "Perhatikan bagian ketiga for-nya kosong (`it.hasNext(); )`). Yang memajukan posisi",
                    "adalah it.next(), bukan i++. Menulis `it.next()` dua kali dalam satu putaran berarti",
                    "melompati satu elemen — salah ketik yang sulit terlihat.",
                    "",
                    "ConcurrentModificationException (CME)",
                    "",
                    "Kalau kamu memanggil list.remove(...) atau list.add(...) SEMENTARA for-each atas list",
                    "itu masih berjalan, Java melempar ConcurrentModificationException.",
                    "",
                    "Namanya menyesatkan dan ini penting diingat: kata 'Concurrent' membuat orang mengira",
                    "ini soal thread. Bukan. Ia terjadi di program satu thread yang tenang-tenang saja.",
                    "Yang dimaksud 'concurrent' adalah: koleksinya berubah BERSAMAAN dengan iterasinya.",
                    "Kalau kamu mencari error ini dan hasilnya penuh artikel soal multithreading, kamu tidak",
                    "salah cari — namanya memang yang menipu.",
                    "",
                    "Mekanismenya sederhana. ArrayList menyimpan penghitung modCount yang naik tiap kali",
                    "isinya berubah. Iterator mencatat nilai modCount saat ia dibuat, lalu membandingkannya",
                    "setiap kali next() dipanggil. Beda = ada yang mengubah list di belakang punggungnya =",
                    "lempar. Ini deteksi cepat-gagal: lebih baik meledak jelas daripada diam-diam",
                    "melompati elemen.",
                    "",
                    "JEBAKAN TERBURUKNYA: kadang ia TIDAK meledak. Kalau yang kamu hapus adalah elemen",
                    "kedua-dari-belakang, cursor jadi sama dengan size baru, hasNext() langsung false, dan",
                    "loop berhenti diam-diam sebelum sempat memeriksa. Elemen terakhir tidak pernah dilihat",
                    "dan tidak ada satu pun pesan error. Jangan pernah menyimpulkan 'kodeku aman karena",
                    "tidak error' — uji dengan data yang lebih panjang.",
                ],
            },
            {
                "heading": "Menghapus elemen tanpa meledak: tiga obat",
                "code": """import java.util.*;

public class Main {
    static List<String> buah() {
        // Dibungkus new ArrayList<> supaya isinya boleh diubah (lihat bagian akhir materi).
        return new ArrayList<>(List.of("Apel", "Mangga", "Jeruk", "Durian"));
    }

    public static void main(String[] args) {
        // Bentuk panjang for-each: inilah yang sebenarnya dijalankan.
        for (Iterator<String> it = buah().iterator(); it.hasNext(); ) {
            String b = it.next();
            System.out.print(b + " ");
        }
        System.out.println();

        // SALAH: menghapus lewat list-nya sementara for-each masih berjalan.
        List<String> salah = buah();
        try {
            for (String b : salah) {
                if (b.startsWith("M")) {
                    salah.remove(b);      // iterator langsung basi
                }
            }
        } catch (ConcurrentModificationException e) {
            System.out.println("Meledak: " + e.getClass().getSimpleName());
        }

        // Obat 1: hapus lewat iterator-nya sendiri, bukan lewat list-nya.
        List<String> a = buah();
        for (Iterator<String> it = a.iterator(); it.hasNext(); ) {
            if (it.next().startsWith("M")) {
                it.remove();
            }
        }
        System.out.println("it.remove()  -> " + a);

        // Obat 2: removeIf, satu baris dan maksudnya langsung terbaca.
        List<String> b = buah();
        b.removeIf(x -> x.startsWith("M"));
        System.out.println("removeIf     -> " + b);

        // Obat 3: telusuri SALINAN-nya, ubah yang asli.
        List<String> c = buah();
        for (String x : new ArrayList<>(c)) {
            if (x.startsWith("M")) {
                c.remove(x);
            }
        }
        System.out.println("salin dulu   -> " + c);
    }
}""",
            },
            {
                "body": [
                    "Kapan pakai yang mana:",
                    "  - removeIf(...)   : pilihan pertama. Paling pendek, paling jelas, paling sulit salah.",
                    "  - it.remove()     : kalau syarat hapusnya rumit, atau kamu juga butuh it.set(...).",
                    "  - salin dulu      : kalau di dalam loop kamu mengubah list LAIN juga, atau menambah",
                    "                      elemen (it.remove() cuma bisa menghapus, tidak bisa menambah).",
                    "",
                    "Dua jebakan kecil pada it.remove():",
                    "  - Ia menghapus elemen yang BARU SAJA dikembalikan next(). Memanggilnya sebelum",
                    "    next() pernah dipanggil -> IllegalStateException, bukan CME.",
                    "  - Ia cuma boleh dipanggil sekali per next().",
                    "",
                    "METHOD MAP YANG MENGGANTIKAN CARA BUKU TEKS",
                    "",
                    "Pola 'cek dulu, baru isi' yang diajarkan di mana-mana:",
                    "",
                    "  if (map.containsKey(k)) { map.put(k, map.get(k) + 1); } else { map.put(k, 1); }",
                    "",
                    "sudah tidak ditulis lagi sejak Java 8. Menelusuri map dua kali (containsKey lalu get)",
                    "itu boros, dan bentuk if-else-nya membuat maksudnya tenggelam. Penggantinya:",
                    "",
                    "  map.getOrDefault(k, bawaan)        nilai k, atau bawaan kalau k tidak ada.",
                    "                                     TIDAK menulis apa pun ke map.",
                    "  map.putIfAbsent(k, nilai)          isi kalau k belum ada; kalau sudah ada, biarkan.",
                    "                                     Mengembalikan nilai LAMA, atau null kalau baru.",
                    "  map.computeIfAbsent(k, k -> ...)   sama, tapi nilainya baru DIBUAT kalau perlu, dan",
                    "                                     yang dikembalikan selalu nilai yang ada di map.",
                    "  map.computeIfPresent(k, (k,v) -> ...) ubah nilai HANYA kalau k sudah ada.",
                    "  map.merge(k, nilaiAwal, (lama, baru) -> ...)  belum ada -> pakai nilaiAwal;",
                    "                                     sudah ada -> jalankan fungsi penggabungnya.",
                    "",
                    "Beda putIfAbsent dan computeIfAbsent yang sering bikin bingung: putIfAbsent SELALU",
                    "membuat objek argumennya, walau nanti dibuang. computeIfAbsent baru menjalankan",
                    "lambda-nya kalau key-nya memang kosong. Untuk `new ArrayList<>()` bedanya sepele; untuk",
                    "sesuatu yang mahal dibuat, bedanya nyata.",
                    "",
                    "Satu perilaku yang perlu diingat: pada compute*/merge, mengembalikan null berarti",
                    "MENGHAPUS key itu dari map — bukan menyimpan null. Sering dipakai sengaja, tapi kalau",
                    "tidak tahu, entri yang hilang sendiri itu membingungkan.",
                    "",
                    "MENELUSURI MAP — tiga pintu, dan satu hal yang jarang disadari:",
                    "  map.keySet()    Set berisi semua key.",
                    "  map.values()    Collection berisi semua value (boleh ada duplikat).",
                    "  map.entrySet()  Set berisi pasangan Map.Entry; e.getKey(), e.getValue().",
                    "  map.forEach((k, v) -> ...)  tanpa loop sama sekali.",
                    "",
                    "Ketiganya adalah VIEW, bukan salinan. Artinya map.keySet().remove(\"a\") benar-benar",
                    "menghapus entri \"a\" dari map-nya, dan e.setValue(x) di dalam loop entrySet menulis",
                    "balik ke map. Kalau kamu hanya butuh key-nya, entrySet tetap lebih hemat daripada",
                    "keySet lalu map.get(k) untuk tiap key — itu mencari dua kali.",
                ],
            },
            {
                "heading": "Dua idiom yang wajib dikenali + kelas Collections",
                "code": """import java.util.*;

public class Main {
    public static void main(String[] args) {
        String kalimat = "roti susu roti kopi susu roti";

        // IDIOM 1 - menghitung frekuensi.
        // merge(k, 1, Integer::sum): belum ada -> pakai 1; sudah ada -> lama + 1.
        // TreeMap dipakai supaya urutan cetaknya pasti (HashMap tidak menjanjikan urutan).
        Map<String, Integer> hitung = new TreeMap<>();
        for (String kata : kalimat.split(" ")) {
            hitung.merge(kata, 1, Integer::sum);
        }
        System.out.println(hitung);            // {kopi=1, roti=3, susu=2}

        // Versi tanpa merge, supaya kelihatan apa yang digantikannya:
        Map<String, Integer> manual = new TreeMap<>();
        for (String kata : kalimat.split(" ")) {
            manual.put(kata, manual.getOrDefault(kata, 0) + 1);
        }
        System.out.println(manual.equals(hitung));   // true

        // IDIOM 2 - mengelompokkan jadi Map<K, List<V>>.
        String[] nama = {"Andi", "Budi", "Ani", "Cici", "Bayu"};
        Map<Character, List<String>> grup = new TreeMap<>();
        for (String n : nama) {
            grup.computeIfAbsent(n.charAt(0), k -> new ArrayList<>()).add(n);
        }
        System.out.println(grup);   // {A=[Andi, Ani], B=[Budi, Bayu], C=[Cici]}

        // Tiga pintu menelusuri Map, plus forEach.
        System.out.println(hitung.keySet());     // [kopi, roti, susu]
        System.out.println(hitung.values());     // [1, 3, 2]
        for (Map.Entry<String, Integer> e : hitung.entrySet()) {
            System.out.print(e.getKey() + "=" + e.getValue() + " ");
        }
        System.out.println();
        hitung.forEach((k, v) -> System.out.print(k + ":" + v + " "));
        System.out.println();

        // Collections = kelas UTILITAS berisi method static.
        // Bedakan dari Collection (tanpa s) yang merupakan interface.
        List<Integer> angka = new ArrayList<>(List.of(5, 3, 9, 3, 1));
        Collections.sort(angka);
        System.out.println(angka);                            // [1, 3, 3, 5, 9]
        Collections.reverse(angka);
        System.out.println(angka);                            // [9, 5, 3, 3, 1]
        System.out.println(Collections.max(angka) + " " + Collections.min(angka)
                + " " + Collections.frequency(angka, 3));     // 9 1 2

        // Menyalin & menggabung.
        List<Integer> gabung = new ArrayList<>(angka);   // constructor penyalin
        gabung.addAll(List.of(100, 200));
        System.out.println(gabung);       // [9, 5, 3, 3, 1, 100, 200]
        System.out.println(angka);        // [9, 5, 3, 3, 1] - yang asli utuh
    }
}""",
            },
            {
                "body": [
                    "Perhatikan baris `grup.computeIfAbsent(n.charAt(0), k -> new ArrayList<>()).add(n)`.",
                    "Ia melakukan dua hal sekaligus: memastikan ada List di key itu, lalu langsung menambah",
                    "ke List yang dikembalikannya. Begitu kamu mengenali bentuknya, kode pengolahan data",
                    "Java jadi jauh lebih mudah dibaca — bentuk ini ada di mana-mana. (Stream API punya",
                    "Collectors.groupingBy untuk pekerjaan yang sama; dibahas di materi Stream API.)",
                    "",
                    "KOLEKSI YANG TIDAK BISA DIUBAH",
                    "",
                    "Bagian ini menjawab satu baris yang tadi lewat begitu saja. Di materi Collection",
                    "Framework tertulis:",
                    "",
                    "  List<String> buah = new ArrayList<>(List.of(\"Apel\", \"Mangga\", \"Jeruk\"));",
                    "",
                    "Kenapa dibungkus new ArrayList<>? Karena List.of(...) menghasilkan koleksi IMMUTABLE —",
                    "isinya terkunci selamanya. Menyederhanakannya jadi `List<String> buah = List.of(...)`",
                    "lalu memanggil buah.add(\"Durian\") membuat program meledak saat dijalankan:",
                    "",
                    "  Exception in thread \"main\" java.lang.UnsupportedOperationException",
                    "",
                    "Pesannya tidak menyebut List.of sama sekali, jadi penyebabnya nyaris tidak terbaca.",
                    "Sekarang kamu tahu: kalau UnsupportedOperationException muncul pada koleksi, hampir",
                    "selalu artinya kamu mencoba mengubah sesuatu yang memang tidak bisa diubah. Semua ini",
                    "immutable, dan melempar UnsupportedOperationException pada add/remove/set/removeIf:",
                    "  List.of(...)   Set.of(...)   Map.of(...)   List.copyOf(...)",
                    "  Collections.emptyList()      Collections.singletonList(x)",
                    "  Collections.unmodifiableList(lain)",
                    "",
                    "Dua aturan tambahan List.of/Map.of yang mengejutkan orang: elemennya TIDAK boleh null",
                    "(langsung NullPointerException), dan Map.of dengan key kembar langsung",
                    "IllegalArgumentException. ArrayList dan HashMap membolehkan keduanya.",
                    "",
                    "Di antara dua kutub itu duduk Arrays.asList(\"a\", \"b\") yang sudah kamu temui di",
                    "materi Array: bukan ArrayList, tapi bukan pula sepenuhnya immutable — ukurannya",
                    "terkunci, isinya boleh ditimpa. Setengah jalan seperti ini justru yang paling",
                    "membingungkan; kalau butuh yang bisa tumbuh, bungkus juga:",
                    "new ArrayList<>(Arrays.asList(...)).",
                    "",
                    "Kalau begitu kenapa immutable masih dipakai? Karena kunci itu justru gunanya. Koleksi",
                    "yang tidak bisa diubah aman dibagi ke mana-mana tanpa takut ada yang mengubahnya",
                    "diam-diam, dan itu melahirkan pola yang sangat sering terlihat di getter:",
                    "",
                    "  private final List<String> anggota = new ArrayList<>();",
                    "",
                    "  public List<String> getAnggota() {",
                    "      return Collections.unmodifiableList(anggota);   // atau List.copyOf(anggota)",
                    "  }",
                    "",
                    "Tanpa pembungkus itu, siapa pun yang memanggil getAnggota() bisa memanggil .add() dan",
                    "menembus encapsulation yang susah payah kamu bangun — field-nya private, tapi isinya",
                    "terbuka lebar. Beda kedua pilihannya penting: unmodifiableList adalah VIEW, jadi kalau",
                    "list aslinya berubah, hasilnya ikut berubah; List.copyOf adalah SALINAN, membeku pada",
                    "kondisi saat itu.",
                    "",
                    "Terakhir, beberapa method Collections lain yang sering terlihat:",
                    "  Collections.shuffle(list)   mengacak urutan (hasilnya beda tiap kali dijalankan)",
                    "  Collections.swap(list, i, j)  menukar dua posisi",
                    "  Collections.emptyList()     List kosong immutable, untuk nilai kembali 'tidak ada'",
                    "  Collections.singletonList(x)  List berisi tepat satu elemen",
                    "Sejak Java 8 ada juga list.sort(pembanding) langsung di List-nya, dan list.sort(null)",
                    "berarti 'urutkan dengan urutan alaminya' — sama dengan Collections.sort(list).",
                ],
            },
        ],
    },
    {
        "title": "25. String & Scanner (Input)",
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
            {
                "body": [
                    "printf: mencetak dengan CETAKAN. Baris String.format di daftar tadi lewat",
                    "begitu saja, padahal ini alat pertama yang kamu butuhkan begitu program",
                    "menampilkan uang, persen, atau rata-rata. Tanpa ini, rata-rata tercetak",
                    "82.5 dan saldo tercetak 100000.0 - apa adanya.",
                    "",
                    "  System.out.printf(\"Halo %s, umur %d%n\", nama, umur);",
                    "",
                    "String pertama adalah cetakannya. Setiap % di dalamnya adalah lubang yang",
                    "diisi argumen berikutnya, sesuai urutan.",
                    "",
                    "  %s   apa saja, diubah jadi teks      %d   bilangan bulat (int, long)",
                    "  %f   bilangan desimal                %b   true / false",
                    "  %c   satu karakter                   %n   ganti baris",
                    "  %%   tanda persen sungguhan",
                    "",
                    "Angka di antara % dan hurufnya mengatur bentuknya:",
                    "",
                    "  %.2f    dua angka di belakang koma     82.5     ->  82.50",
                    "  %10s    lebar 10, rata KANAN           \"Andi\"   ->  '      Andi'",
                    "  %-10s   lebar 10, rata KIRI            \"Andi\"   ->  'Andi      '",
                    "  %5d     lebar 5, rata kanan            42       ->  '   42'",
                    "  %05d    lebar 5, sisanya diisi nol     42       ->  '00042'",
                    "  %,d     pemisah ribuan                 100000   ->  '100,000'",
                    "",
                    "Lebar tetap itulah yang membuat tabel di terminal lurus rapi - satu-satunya",
                    "cara mengatur kolom tanpa menghitung spasi sendiri.",
                    "",
                    "printf vs String.format: cetakannya sama persis, bedanya cuma tujuan. printf",
                    "MENCETAK langsung; String.format MENGEMBALIKAN String yang bisa kamu simpan,",
                    "gabungkan, atau tulis ke berkas.",
                    "",
                    "Dua hal yang bikin tersandung:",
                    "  1. Pakai %n, bukan \\n. %n memakai penanda baris baru milik sistem yang",
                    "     sedang menjalankan program, jadi berkas hasilnya benar juga di Windows.",
                    "  2. Tipe argumen harus cocok dengan hurufnya, dan salah pasang TIDAK",
                    "     ketahuan compiler - ia meledak saat program jalan:",
                    "       System.out.printf(\"%d%n\", \"Andi\");",
                    "       java.util.IllegalFormatConversionException: d != java.lang.String",
                    "     Kalau ragu, %s menerima apa pun.",
                ]
            },
            {
                "heading": "printf & String.format",
                "code": """public class Main {
    public static void main(String[] args) {
        String nama = "Andi";
        int umur = 20;
        double rata = 82.5;
        long saldo = 100000;

        System.out.printf("Halo %s, umur %d%n", nama, umur);
        System.out.printf("Rata-rata: %.2f%n", rata);
        System.out.printf("Saldo: Rp%,d%n", saldo);
        System.out.printf("[%-10s][%10s]%n", nama, nama);
        System.out.printf("Nomor urut: %05d%n", 42);
        System.out.printf("Lulus: %b, diskon %d%%%n", true, 10);

        // String.format TIDAK mencetak, ia MENGEMBALIKAN String.
        String baris = String.format("%-8s %6.2f", nama, rata);
        System.out.println("[" + baris + "]");

        try {
            System.out.printf("%d%n", nama);   // %d minta angka, diberi String
        } catch (java.util.IllegalFormatConversionException e) {
            System.out.println("format salah: " + e.getMessage());
        }
    }
}"""
            },
        ],
    },
    {
        "title": "26. Tanggal & Waktu (java.time)",
        "sections": [
            {
                "body": [
                    "Nyaris tiap aplikasi nyata menyimpan waktu: tanggal lahir, tanggal transaksi, jatuh",
                    "tempo tagihan, kapan sebuah baris data dibuat, jam berapa sebuah error terjadi. Java",
                    "punya satu paket khusus untuk itu sejak Java 8: java.time.",
                    "",
                    "Kenapa perlu paket BARU? Karena yang lama rusak, dan tiga cacatnya sungguh menyakitkan:",
                    "  - java.util.Date BISA DIUBAH. Kamu mengoper sebuah tanggal ke method orang lain,",
                    "    method itu menggesernya, dan tanggal di tempatmu ikut berubah tanpa satu pun tanda.",
                    "  - SimpleDateFormat TIDAK AMAN dipakai bersamaan oleh beberapa thread. Orang",
                    "    menjadikannya field static supaya hemat, kelihatan benar bertahun-tahun, lalu di",
                    "    server yang ramai ia sesekali mengeluarkan tanggal ngawur. Bug yang nyaris mustahil",
                    "    ditiru ulang. (Soal thread, lihat materi Multithreading.)",
                    "  - Calendar MENGHITUNG BULAN MULAI 0. Januari = 0, Desember = 11. Jadi",
                    "    new GregorianCalendar(2026, 0, 15) itu 15 Januari, bukan 15 Februari.",
                    "    Lebih buruk lagi: tanggal mustahil tidak ditolak, tapi DIGULUNG diam-diam —",
                    "    new GregorianCalendar(2026, 1, 29) menghasilkan 1 Maret 2026, tanpa error apa pun.",
                    "",
                    "Ketiganya belum hilang dari dunia. Kode berumur, library lama, dan paket java.sql masih",
                    "penuh Date dan Calendar, jadi kamu pasti bertemu mereka saat membaca kode orang. Cara",
                    "menyeberang dari dan ke java.time ada di bagian akhir materi ini.",
                    "",
                    "MEMILIH TIPE. Ini keputusan pertama, dan yang paling sering diambil asal:",
                    "",
                    "  Tipe            Isinya                        Contoh nilainya",
                    "  -------------   ---------------------------   ---------------------------",
                    "  LocalDate       tanggal saja                  2026-01-15",
                    "  LocalTime       jam saja                      08:30",
                    "  LocalDateTime   tanggal + jam, TANPA zona     2026-01-15T13:45",
                    "  Instant         satu titik di garis waktu     2026-01-15T02:30:00Z",
                    "  ZonedDateTime   tanggal + jam + zona waktu    2026-01-15T09:30+07:00[Asia/Jakarta]",
                    "",
                    "  LocalDate      -> tanggal lahir, jatuh tempo, tanggal libur",
                    "  LocalTime      -> jam buka toko, jadwal alarm",
                    "  LocalDateTime  -> jadwal rapat, kolom DATETIME di database",
                    "  Instant        -> stempel baris log, created_at, apa pun yang perlu diurutkan",
                    "  ZonedDateTime  -> apa pun yang dilihat pemakai di dua kota yang berbeda zona",
                    "",
                    "Kata 'Local' di depan artinya TANPA ZONA WAKTU — bukan 'waktu setempat'. LocalDateTime",
                    "'2026-01-15 13:45' tidak memberi tahu itu jam 13:45 di kota mana, jadi ia tidak bisa",
                    "dibandingkan dengan jam 13:45 milik kota lain. Pegangannya begini: kalau yang kamu",
                    "simpan adalah SAAT sesuatu terjadi (log, transaksi, pembayaran), pakai Instant. Kalau",
                    "yang kamu simpan adalah ANGKA DI KALENDER — tanggal lahir tetap 17 Mei di mana pun",
                    "orangnya berada — pakai LocalDate.",
                    "",
                    "MEMBUAT NILAINYA. Tiga pintu, dan namanya sama untuk semua tipe di atas:",
                    "  LocalDate.now()                 dari jam sistem",
                    "  LocalDate.of(2026, 1, 15)       dari angka; bulan 1-12, manusiawi, tidak mulai 0",
                    "  LocalDate.parse(\"2026-01-15\")   dari teks berformat ISO",
                    "",
                    "Contoh di materi ini sengaja TIDAK memakai now(). Hasil now() berbeda tiap kali kamu",
                    "menjalankannya, jadi keluaranmu tidak akan pernah cocok dengan yang tertulis di sini.",
                ],
            },
            {
                "heading": "Membuat, membaca bagiannya, menggeser, dan membandingkan",
                "code": """import java.time.DayOfWeek;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.LocalTime;
import java.time.Month;

public class Main {
    public static void main(String[] args) {
        // Tiga pintu pembuatan. now() sengaja dihindari supaya hasilnya tetap.
        LocalDate lahir = LocalDate.of(2000, 5, 17);
        LocalDate jatuhTempo = LocalDate.parse("2026-01-15");
        LocalTime jamBuka = LocalTime.of(8, 30);
        LocalDateTime rapat = LocalDateTime.of(2026, 1, 15, 13, 45);

        System.out.println(lahir);
        System.out.println(jatuhTempo);
        System.out.println(jamBuka);
        System.out.println(rapat);

        // Mengambil bagian-bagiannya
        System.out.println(lahir.getYear() + "|" + lahir.getMonthValue()
                + "|" + lahir.getDayOfMonth());

        Month bulan = lahir.getMonth();
        DayOfWeek hari = lahir.getDayOfWeek();
        System.out.println(bulan + " ke-" + bulan.getValue());
        System.out.println(hari + " ke-" + hari.getValue());
        System.out.println("hari ke-" + lahir.getDayOfYear()
                + " kabisat=" + lahir.isLeapYear());

        // IMMUTABLE: hasilnya objek BARU, yang lama tidak tersentuh
        LocalDate tenggat = jatuhTempo.plusDays(10);
        System.out.println(jatuhTempo + " -> " + tenggat);

        jatuhTempo.plusDays(10);         // hasilnya dibuang: bug klasik
        System.out.println(jatuhTempo);

        // Perubahan dirangkai: bulan depan, lalu tanggal 1
        System.out.println(jatuhTempo.plusMonths(1).withDayOfMonth(1));

        // Membandingkan
        LocalDate salinan = LocalDate.of(2000, 5, 17);
        System.out.println(lahir.isBefore(jatuhTempo));
        System.out.println(lahir.isAfter(jatuhTempo));
        System.out.println(lahir.isEqual(salinan));
        System.out.println(lahir.equals(salinan));
        System.out.println(lahir == salinan);

        // Geser bulan MENJEPIT tanggal yang tidak ada, dan itu tidak bisa dibalik
        LocalDate akhirJanuari = LocalDate.of(2026, 1, 31);
        System.out.println(akhirJanuari.plusMonths(1));
        System.out.println(akhirJanuari.plusMonths(1).minusMonths(1));
    }
}""",
            },
            {
                "body": [
                    "Keluaran program di atas:",
                    "  2000-05-17",
                    "  2026-01-15",
                    "  08:30",
                    "  2026-01-15T13:45",
                    "  2000|5|17",
                    "  MAY ke-5",
                    "  WEDNESDAY ke-3",
                    "  hari ke-138 kabisat=true",
                    "  2026-01-15 -> 2026-01-25",
                    "  2026-01-15",
                    "  2026-02-01",
                    "  true",
                    "  false",
                    "  true",
                    "  true",
                    "  false",
                    "  2026-02-28",
                    "  2026-01-28",
                    "",
                    "println() atas tipe java.time selalu memberi bentuk ISO (2026-01-15), bukan bentuk",
                    "Indonesia. Mengubahnya jadi 15/01/2026 urusan DateTimeFormatter, bagian berikutnya.",
                    "",
                    "JEBAKAN 1 — semuanya IMMUTABLE. plusDays, minusMonths, withDayOfMonth, plusHours: tidak",
                    "satu pun mengubah objeknya. Semua MENGEMBALIKAN objek baru. Baris",
                    "  jatuhTempo.plusDays(10);",
                    "terlihat seperti 'majukan sepuluh hari', padahal ia tidak melakukan apa-apa: objek baru",
                    "dibuat lalu langsung dibuang. Compiler DIAM karena secara sintaks tidak ada yang salah.",
                    "Yang benar selalu menampung hasilnya: `jatuhTempo = jatuhTempo.plusDays(10);`. Sifat ini",
                    "sama persis dengan String (lihat materi String & Scanner) dan alasannya pun sama —",
                    "objek yang tidak bisa diubah aman dioper ke mana-mana dan aman dipakai antar-thread.",
                    "",
                    "JEBAKAN 2 — jangan pakai `==`. Dua tanggal 17 Mei 2000 di atas isinya sama persis, tapi",
                    "`lahir == salinan` bernilai false: LocalDate.of() membuat objek BARU tiap dipanggil, dan",
                    "`==` membandingkan alamat objek, bukan isinya. Yang benar:",
                    "  isBefore(lain)   lebih awal?",
                    "  isAfter(lain)    lebih akhir?",
                    "  isEqual(lain)    menunjuk saat yang sama?",
                    "  equals(lain)     seluruh isinya sama?",
                    "Semua tipe java.time juga Comparable, jadi Collections.sort(daftarTanggal) langsung",
                    "berjalan tanpa comparator (lihat materi Collection Framework).",
                    "",
                    "isEqual dan equals baru terasa berbeda pada ZonedDateTime: jam 09:30 Jakarta dan jam",
                    "02:30 UTC itu SAAT yang sama, jadi isEqual -> true, tapi field-nya (zona!) berbeda, jadi",
                    "equals -> false. Untuk 'apakah ini saat yang sama', pakai isEqual.",
                    "",
                    "JEBAKAN 3 — getMonth() bukan angka. Ia mengembalikan enum Month (MAY), dan getDayOfWeek()",
                    "mengembalikan enum DayOfWeek (WEDNESDAY). Untuk angkanya pakai getMonthValue() dan",
                    "hari.getValue() (1 = Senin ... 7 = Minggu). Nama yang tercetak berbahasa Inggris karena",
                    "itu name() sebuah enum, bukan hasil penerjemahan (lihat materi Enum) — nama hari dalam",
                    "bahasa Indonesia didapat lewat formatter ber-Locale, bukan lewat getDayOfWeek().",
                    "",
                    "JEBAKAN 4 — plusMonths MENJEPIT tanggal yang tidak ada. 31 Januari + 1 bulan = 28",
                    "Februari, karena 31 Februari tidak ada. Akibatnya penggeseran bulan TIDAK BISA DIBALIK:",
                    "hasil di atas kembali ke 28 Januari, bukan 31. Untuk 'hari terakhir bulan ini' jangan",
                    "menghitung sendiri; pakai tanggal.with(TemporalAdjusters.lastDayOfMonth()) dari",
                    "java.time.temporal — kelas itu juga punya next(DayOfWeek.MONDAY), firstDayOfMonth(),",
                    "dan sejenisnya.",
                    "",
                    "Berbeda dari Calendar, tanggal mustahil DITOLAK saat dibuat, bukan digulung diam-diam:",
                    "  LocalDate.of(2026, 2, 29)  -> DateTimeException: Invalid date 'February 29' ...",
                    "  LocalDate.of(2026, 13, 1)  -> DateTimeException: Invalid value for MonthOfYear ...",
                ],
            },
            {
                "heading": "Selisih waktu, format, parse, dan zona",
                "code": """import java.time.Duration;
import java.time.Instant;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.Period;
import java.time.ZoneId;
import java.time.ZonedDateTime;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeParseException;
import java.time.temporal.ChronoUnit;

public class Main {
    public static void main(String[] args) {
        LocalDate lahir = LocalDate.of(2000, 5, 17);
        LocalDate acuan = LocalDate.of(2026, 1, 15);

        // Period: selisih TANGGAL, dipecah jadi tahun + bulan + hari
        Period umur = Period.between(lahir, acuan);
        System.out.println(umur.getYears() + " tahun " + umur.getMonths()
                + " bulan " + umur.getDays() + " hari");
        System.out.println(umur);

        // ChronoUnit: satu satuan saja, hasilnya long
        System.out.println(ChronoUnit.DAYS.between(lahir, acuan) + " hari");
        System.out.println(ChronoUnit.MONTHS.between(lahir, acuan) + " bulan");

        // Duration: selisih WAKTU, satuan jam ke bawah
        LocalDateTime masuk = LocalDateTime.of(2026, 1, 15, 8, 30);
        LocalDateTime pulang = LocalDateTime.of(2026, 1, 15, 17, 15);
        Duration kerja = Duration.between(masuk, pulang);
        System.out.println(kerja.toHours() + " jam " + kerja.toMinutesPart() + " menit");
        System.out.println(kerja.toMinutes() + " menit");
        System.out.println(kerja);

        // Format: objek -> teks
        DateTimeFormatter polaIndo = DateTimeFormatter.ofPattern("dd/MM/yyyy");
        DateTimeFormatter polaLog = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
        System.out.println(acuan.format(polaIndo));
        System.out.println(masuk.format(polaLog));
        System.out.println(acuan.format(DateTimeFormatter.ISO_LOCAL_DATE));

        // Parse: teks -> objek, polanya WAJIB sama persis
        LocalDate dariForm = LocalDate.parse("06/09/2026", polaIndo);
        System.out.println(dariForm);

        try {
            LocalDate.parse("06/09/2026");   // tanpa formatter -> dianggap ISO
        } catch (DateTimeParseException e) {
            System.out.println("gagal: " + e.getMessage());
        }

        // Instant: titik waktu absolut, selalu UTC, untuk log & stempel data
        Instant stempel = Instant.parse("2026-01-15T02:30:00Z");
        System.out.println(stempel);
        System.out.println(stempel.toEpochMilli());
        System.out.println(stempel.plus(90, ChronoUnit.MINUTES));

        // Zona waktu: SAAT yang sama, dibaca dari Jakarta
        ZonedDateTime diJakarta = stempel.atZone(ZoneId.of("Asia/Jakarta"));
        System.out.println(diJakarta);
        System.out.println(diJakarta.toLocalDateTime().format(polaLog));
    }
}""",
            },
            {
                "body": [
                    "Keluaran program di atas:",
                    "  25 tahun 7 bulan 29 hari",
                    "  P25Y7M29D",
                    "  9374 hari",
                    "  307 bulan",
                    "  8 jam 45 menit",
                    "  525 menit",
                    "  PT8H45M",
                    "  15/01/2026",
                    "  2026-01-15 08:30:00",
                    "  2026-01-15",
                    "  2026-09-06",
                    "  gagal: Text '06/09/2026' could not be parsed at index 0",
                    "  2026-01-15T02:30:00Z",
                    "  1768444200000",
                    "  2026-01-15T04:00:00Z",
                    "  2026-01-15T09:30+07:00[Asia/Jakarta]",
                    "  2026-01-15 09:30:00",
                    "",
                    "TIGA ALAT SELISIH, dan memilih yang salah adalah kesalahan paling umum di sini:",
                    "  Period                     berbasis kalender: tahun, bulan, hari",
                    "  Duration                   berbasis detik: jam, menit, detik, nano",
                    "  ChronoUnit.X.between(a,b)  satu satuan saja, hasilnya long",
                    "",
                    "Period.between HANYA menerima LocalDate. Duration.between butuh sesuatu yang punya jam,",
                    "jadi Duration.between(tanggal1, tanggal2) MELEMPAR UnsupportedTemporalTypeException:",
                    "Unsupported unit: Seconds — error saat program jalan, bukan saat kompilasi.",
                    "",
                    "JEBAKAN getDays(): itu SISA hari setelah tahun dan bulannya diambil, bukan total hari.",
                    "  Period.between(1 Jan 2026, 10 Mar 2026).getDays()  ->  9    (bukan 68!)",
                    "Angkanya berarti '2 bulan 9 hari'. Untuk TOTAL hari, satu-satunya jawaban yang benar",
                    "adalah ChronoUnit.DAYS.between(a, b). Cacat yang sama ada di Duration: toHours() = total",
                    "jam dibulatkan ke bawah (8), toMinutes() = total menit (525), toMinutesPart() = sisa",
                    "menit (45). Mencampur toHours() dengan toMinutes() dalam satu kalimat menghasilkan",
                    "'8 jam 525 menit'. Bentuk toString-nya ISO: P25Y7M29D dibaca 25 tahun 7 bulan 29 hari,",
                    "PT8H45M dibaca 8 jam 45 menit.",
                    "",
                    "FORMAT & PARSE. format() mengubah objek jadi teks, parse() mengubah teks jadi objek.",
                    "Huruf pola yang sering dipakai:",
                    "  yyyy  tahun 4 digit      MM  bulan angka (01)    dd  tanggal (15)",
                    "  MMM   nama bulan singkat MMMM nama bulan penuh    EEEE nama hari",
                    "  HH    jam 0-23           hh  jam 1-12 (butuh a)   a   AM/PM",
                    "  mm    menit              ss  detik                SSS milidetik",
                    "",
                    "JEBAKAN huruf besar-kecil. Semuanya LOLOS KOMPILASI; salahnya baru terlihat di layar:",
                    "  \"HH:MM\"      mm itu menit, MM itu BULAN. 21:05 tercetak jadi 21:01.",
                    "  \"dd/MM/YYYY\" Y itu 'tahun berbasis PEKAN', bukan tahun kalender. 31 Desember 2025",
                    "               tercetak 31/12/2026, karena hari itu sudah masuk pekan pertama tahun",
                    "               berikutnya. Bug ini cuma muncul di sekitar pergantian tahun — persis",
                    "               saat laporan akhir tahun dicetak.",
                    "  \"DD\"         D itu hari ke berapa DALAM SETAHUN. 31 Desember 2025 jadi 365.",
                    "Pakai huruf kecil untuk hari (dd), menit (mm), dan tahun (yyyy). Selalu uji formatter",
                    "barumu dengan satu tanggal yang kamu tahu jawabannya.",
                    "",
                    "parse() menuntut teks yang COCOK PERSIS dengan polanya, termasuk nol di depan:",
                    "  LocalDate.parse(\"06/09/2026\")            gagal, tanpa formatter Java menuntut ISO",
                    "  LocalDate.parse(\"2026-1-5\")              gagal, ISO menuntut 2026-01-05",
                    "DateTimeParseException itu unchecked, jadi compiler TIDAK memaksamu menangkapnya. Teks",
                    "tanggal yang datang dari form, berkas, atau API wajib kamu bungkus try-catch sendiri",
                    "(lihat materi Exception Handling). Untuk format baku ada konstanta siap pakai:",
                    "DateTimeFormatter.ISO_LOCAL_DATE, ISO_LOCAL_DATE_TIME, ISO_INSTANT. Untuk nama bulan",
                    "dan hari berbahasa Indonesia, sertakan Locale:",
                    "  DateTimeFormatter.ofPattern(\"EEEE, dd MMMM yyyy\", Locale.forLanguageTag(\"id\"))",
                    "Berbeda dari SimpleDateFormat yang lama, DateTimeFormatter AMAN antar-thread, jadi ia",
                    "boleh — malah sebaiknya — disimpan sebagai `static final` dan dipakai bersama.",
                    "",
                    "INSTANT & ZONA. Instant tidak punya zona sama sekali; huruf Z di ujungnya berarti UTC.",
                    "toEpochMilli() memberi milidetik sejak 1 Januari 1970 UTC — angka besar yang sering kamu",
                    "temui di JSON dan log. atZone() TIDAK menggeser waktunya, ia hanya mengubah cara",
                    "membacanya: 02:30 UTC dan 09:30 WIB adalah saat yang sama. Nama zona ditulis",
                    "'Benua/Kota' seperti \"Asia/Jakarta\", bukan \"WIB\" dan bukan \"+7\", karena nama kotalah",
                    "yang membawa sejarah aturan zona dan daylight saving negara itu.",
                    "",
                    "DI MANA INI BERTEMU MATERI LAIN:",
                    "  - JDBC (materi JDBC): driver modern mengerti java.time langsung.",
                    "      stmt.setObject(1, tanggalLahir);",
                    "      LocalDate tgl = rs.getObject(\"tgl_lahir\", LocalDate.class);",
                    "    Kolom DATE -> LocalDate, DATETIME/TIMESTAMP -> LocalDateTime, TIMESTAMP WITH TIME",
                    "    ZONE -> OffsetDateTime. Hindari rs.getDate() yang mengembalikan java.sql.Date lama.",
                    "  - File I/O (materi File I/O): nama berkas bertanggal pakai pola \"yyyyMMdd\", sehingga",
                    "    laporan-20260115.txt berurut sendiri secara alfabetis. Pola \"dd-MM-yyyy\" tidak.",
                    "  - Log: Instant.now() untuk stempel. Bentuk ISO-nya bisa diurutkan sebagai teks biasa.",
                    "  - Unit testing (materi JUnit): method yang memanggil LocalDate.now() di dalamnya",
                    "    mustahil diuji, karena hasilnya berubah tiap hari. Terima java.time.Clock sebagai",
                    "    parameter lalu panggil LocalDate.now(jam); di tes, berikan",
                    "    Clock.fixed(Instant.parse(\"2026-01-15T02:30:00Z\"), ZoneId.of(\"Asia/Jakarta\")).",
                    "",
                    "MENYEBERANG DARI API LAMA, saat kamu terpaksa memanggil kode berumur:",
                    "  Date lama = Date.from(instant);              Instant i = lama.toInstant();",
                    "  java.sql.Date sd = java.sql.Date.valueOf(localDate);   sd.toLocalDate();",
                    "  Timestamp ts = Timestamp.valueOf(localDateTime);       ts.toLocalDateTime();",
                    "Ubah ke java.time secepat mungkin di batas kodemu, lalu jangan sentuh lagi tipe lama.",
                ],
            },
        ],
    },
    {
        "title": "27. Lambda Expression & Functional Interface",
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
        "title": "28. Mengurutkan Objek: Comparable & Comparator",
        "sections": [
            {
                "body": [
                    "Materi Collection Framework menyebut Collections.sort(listAngka), dan Stream API memakai",
                    ".sorted(). Keduanya jalan mulus tanpa penjelasan tambahan — dan justru itu yang menyesatkan.",
                    "Keduanya jalan BUKAN karena Java bisa mengurutkan apa saja, melainkan karena Integer dan",
                    "String kebetulan sudah membawa aturan urutannya sendiri. Begitu yang diurutkan adalah objek",
                    "buatanmu, semuanya berhenti:",
                    "",
                    "  List<Mahasiswa> daftar = new ArrayList<>();",
                    "  Collections.sort(daftar);              // TIDAK MAU DIKOMPILASI",
                    "  daftar.stream().sorted().count();      // kompilasi lolos, MELEDAK saat dijalankan",
                    "",
                    "Dua pesan yang sama sekali berbeda untuk satu sebab yang sama. Yang pertama, dari compiler:",
                    "  error: no suitable method found for sort(List<Mahasiswa>)",
                    "      (inference variable T#1 has incompatible bounds",
                    "        lower bounds: Comparable<? super T#1>)",
                    "Yang kedua baru muncul setelah program berjalan, kadang berbulan-bulan kemudian:",
                    "  Exception in thread \"main\" java.lang.ClassCastException:",
                    "      class Mahasiswa cannot be cast to class java.lang.Comparable",
                    "",
                    "Sebabnya satu: Java tidak tahu mana yang 'lebih dulu' antara dua Mahasiswa. Collections.sort",
                    "menuliskan syarat itu di tanda tangannya (<T extends Comparable<? super T>>), jadi compiler",
                    "sempat menolak lebih awal. Sedangkan .sorted() tanpa argumen tidak menuliskannya — ia diam",
                    "saja saat dikompilasi, lalu di dalam mesin mencoba mengecast tiap elemen jadi Comparable dan",
                    "gagal di tengah jalan. Pelajaran umumnya: menolak saat kompilasi selalu lebih murah daripada",
                    "menolak saat berjalan, dan sebuah generic bound-lah yang membeli perbedaan itu.",
                    "",
                    "KONTRAK compareTo. Interface Comparable isinya cuma satu method:",
                    "  int compareTo(T lain)",
                    "Yang dikembalikan int, BUKAN boolean. Ini yang paling sering salah dibaca. Artinya:",
                    "  negatif  -> objek ini harus berada SEBELUM 'lain'",
                    "  nol      -> keduanya dianggap SAMA POSISINYA",
                    "  positif  -> objek ini harus berada SESUDAH 'lain'",
                    "",
                    "Yang berarti cuma TANDANYA, bukan besarnya. \"Andi\".compareTo(\"Zaki\") mengembalikan -25, bukan",
                    "-1, karena String menghitung selisih huruf pertama yang berbeda. Jadi jangan pernah menulis",
                    "if (a.compareTo(b) == -1) — tulis if (a.compareTo(b) < 0). Kode yang membandingkan dengan -1",
                    "akan benar untuk sebagian data dan salah untuk sebagian lain, yang jauh lebih sulit dilacak",
                    "daripada kode yang salah untuk semuanya.",
                    "",
                    "Sebuah tipe diberi urutan ALAMI dengan implements Comparable<TipeItu> lalu meng-override",
                    "compareTo. Kapan sebuah tipe pantas punya urutan alami? Kalau ada satu urutan yang hampir",
                    "semua orang setujui tanpa perlu bertanya: angka dari kecil, teks A-Z, tanggal dari lama ke",
                    "baru, NIM dari kecil. Kalau kamu harus bertanya dulu 'diurutkan berdasarkan apa?', tipe itu",
                    "TIDAK punya urutan alami, dan jawabannya bukan Comparable melainkan Comparator.",
                ],
            },
            {
                "heading": "Comparable: memberi Mahasiswa satu urutan alami",
                "code": """import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Mahasiswa implements Comparable<Mahasiswa> {
    private final int nim;
    private final String nama;
    private final double ipk;

    Mahasiswa(int nim, String nama, double ipk) {
        this.nim = nim;
        this.nama = nama;
        this.ipk = ipk;
    }

    public int getNim()     { return nim; }
    public String getNama() { return nama; }
    public double getIpk()  { return ipk; }

    // Urutan ALAMI Mahasiswa: NIM dari kecil ke besar.
    // Satu tipe cuma boleh punya SATU urutan alami, jadi pilih yang paling tidak dipertanyakan.
    @Override
    public int compareTo(Mahasiswa lain) {
        return Integer.compare(this.nim, lain.nim);   // BUKAN this.nim - lain.nim
    }

    @Override
    public String toString() {
        return nim + "-" + nama;
    }
}

public class Main {
    public static void main(String[] args) {
        // Yang penting dari nilai kembalian compareTo hanyalah tandanya:
        System.out.println("10 vs 20 -> " + Integer.compare(10, 20));   // negatif: kiri lebih dulu
        System.out.println("20 vs 20 -> " + Integer.compare(20, 20));   // nol    : dianggap sama
        System.out.println("30 vs 20 -> " + Integer.compare(30, 20));   // positif: kiri lebih belakang
        System.out.println("Andi vs Zaki -> " + "Andi".compareTo("Zaki"));  // -25, bukan -1

        List<Mahasiswa> daftar = new ArrayList<>();
        daftar.add(new Mahasiswa(103, "Citra", 3.4));
        daftar.add(new Mahasiswa(101, "Andi", 3.8));
        daftar.add(new Mahasiswa(102, "Budi", 2.9));

        Collections.sort(daftar);      // sekarang dikompilasi: Mahasiswa punya urutan alami
        System.out.println(daftar);    // [101-Andi, 102-Budi, 103-Citra]

        daftar.sort(null);             // null artinya "pakai urutan alaminya", hasilnya sama
        System.out.println(daftar);

        // Urutan alami juga dipakai diam-diam oleh max/min, TreeSet, TreeMap, dan PriorityQueue.
        System.out.println(Collections.max(daftar));   // 103-Citra
        System.out.println(Collections.min(daftar));   // 101-Andi
    }
}""",
            },
            {
                "body": [
                    "Comparable menempel di kelasnya, jadi satu tipe cuma bisa punya satu urutan. Padahal layar",
                    "yang berbeda butuh urutan yang berbeda: papan peringkat butuh IPK, buku alumni butuh nama,",
                    "laporan fakultas butuh jurusan dulu baru IPK. Kamu tidak mungkin mengubah compareTo tiap",
                    "kali — apalagi kalau kelasnya milik orang lain dan tidak bisa kamu sentuh sama sekali.",
                    "",
                    "Comparator memisahkan 'cara mengurutkan' dari kelas yang diurutkan. Ia objek tersendiri:",
                    "bisa dibuat sebanyak yang kamu mau, disimpan di variabel, dioper sebagai argumen method,",
                    "dan dipakai ulang. Ia juga functional interface (satu method: compare(a, b)), jadi semua",
                    "yang kamu pelajari di materi Lambda berlaku persis di sini.",
                    "",
                    "Bentuk mentahnya sebuah lambda dua argumen:",
                    "  Comparator<Mahasiswa> perNama = (a, b) -> a.getNama().compareTo(b.getNama());",
                    "Bentuk ini sah, dan kamu akan sering melihatnya di kode orang. Tapi ia gampang salah tanpa",
                    "satu pun peringatan: tertukar a dengan b membalik urutan, dan memakai getNama() di kiri tapi",
                    "getJurusan() di kanan menghasilkan urutan ngawur yang tetap dikompilasi. Sejak Java 8 ada",
                    "bentuk yang cuma menyebut KUNCI-nya:",
                    "  Comparator<Mahasiswa> perNama = Comparator.comparing(Mahasiswa::getNama);",
                    "Di sini tidak ada a dan b untuk tertukar. Kamu menunjuk satu field, sisanya diurus Java.",
                    "",
                    "Pabrik dan perangkainya — semuanya method di interface Comparator:",
                    "  Comparator.comparing(fn)         kunci apa pun yang Comparable (String, Integer, LocalDate)",
                    "  Comparator.comparing(fn, cmp)    kunci diambil fn, tapi cara mengurutkannya ditentukan cmp",
                    "  Comparator.comparingInt(fn)      kunci int, tanpa membungkusnya jadi Integer",
                    "  Comparator.comparingLong(fn)     kunci long",
                    "  Comparator.comparingDouble(fn)   kunci double",
                    "  .thenComparing(fn)               kunci KEDUA, dipakai hanya kalau kunci pertama seri",
                    "  .thenComparingInt/Long/Double    kunci kedua bertipe primitif",
                    "  .reversed()                      membalik arah comparator ini",
                    "  Comparator.naturalOrder()        urutan alami tipenya (butuh Comparable)",
                    "  Comparator.reverseOrder()        kebalikan urutan alami",
                    "  Comparator.nullsFirst(cmp)       izinkan kunci null, taruh di paling depan",
                    "  Comparator.nullsLast(cmp)        izinkan kunci null, taruh di paling belakang",
                    "",
                    "Kenapa comparingInt/Double ada padahal comparing sudah cukup? Karena comparing memaksa tiap",
                    "nilai primitif dibungkus jadi Integer/Double dulu sebelum dibandingkan. Untuk sepuluh baris",
                    "data tidak terasa; untuk list panjang yang diurutkan berulang kali, itu jutaan objek sampah.",
                    "",
                    "Semua tempat yang menerima comparator. Hafal satu, sisanya menyusul sendiri:",
                    "  daftar.sort(cmp)                     mengurutkan list DI TEMPAT (list aslinya berubah)",
                    "  Collections.sort(daftar, cmp)        bentuk lama, hasilnya sama",
                    "  Arrays.sort(array, cmp)              untuk array berisi objek",
                    "  daftar.stream().sorted(cmp)          menghasilkan aliran baru, list asli TIDAK berubah",
                    "  daftar.stream().max(cmp) / .min(cmp) mengembalikan Optional<T>",
                    "  Collections.max(daftar, cmp)         mengembalikan elemennya langsung, error kalau kosong",
                    "  new TreeSet<>(cmp) / new TreeMap<>(cmp)   urutan isinya ditentukan comparator ini",
                    "  new PriorityQueue<>(cmp)             menentukan siapa yang keluar duluan dari antrean",
                ],
            },
            {
                "heading": "Comparator: satu daftar, banyak cara mengurutkan",
                "code": """import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.TreeSet;
import java.util.stream.Collectors;

class Mahasiswa {
    private final String nama;
    private final String jurusan;
    private final double ipk;
    private final String email;      // sengaja BOLEH null: data nyata memang berlubang

    Mahasiswa(String nama, String jurusan, double ipk, String email) {
        this.nama = nama;
        this.jurusan = jurusan;
        this.ipk = ipk;
        this.email = email;
    }

    public String getNama()    { return nama; }
    public String getJurusan() { return jurusan; }
    public double getIpk()     { return ipk; }
    public String getEmail()   { return email; }

    @Override
    public String toString() { return nama + "/" + jurusan + "/" + ipk; }
}

public class Main {
    public static void main(String[] args) {
        // List.of menghasilkan list yang TIDAK bisa diubah; dibungkus ArrayList supaya bisa disort.
        List<Mahasiswa> daftar = new ArrayList<>(List.of(
                new Mahasiswa("Citra", "Sipil", 3.85, "citra@kampus.id"),
                new Mahasiswa("Andi",  "Mesin", 3.20, null),
                new Mahasiswa("Budi",  "Mesin", 3.20, "budi@kampus.id"),
                new Mahasiswa("Dewi",  "Sipil", 2.95, "dewi@kampus.id")));

        // 1. Satu kunci. Dua baris ini artinya sama persis; yang bawah lebih sulit ditulis salah.
        daftar.sort((a, b) -> a.getNama().compareTo(b.getNama()));
        daftar.sort(Comparator.comparing(Mahasiswa::getNama));
        System.out.println("nama A-Z    : " + daftar);

        // 2. Kunci angka pakai comparingDouble, arahnya dibalik dengan reversed().
        //    Andi & Budi seri di 3.2, dan urutan mereka tetap seperti sebelumnya: sort itu STABIL,
        //    elemen yang dianggap sama tidak pernah ditukar posisinya.
        daftar.sort(Comparator.comparingDouble(Mahasiswa::getIpk).reversed());
        System.out.println("IPK turun   : " + daftar);

        // 3. Dua kunci: jurusan A-Z, lalu di DALAM tiap jurusan IPK dari besar ke kecil.
        //    Perhatikan reversed() menempel pada kunci KEDUA saja, bukan pada rangkaiannya.
        Comparator<Mahasiswa> perJurusan = Comparator
                .comparing(Mahasiswa::getJurusan)
                .thenComparing(Comparator.comparingDouble(Mahasiswa::getIpk).reversed());
        daftar.sort(perJurusan);
        System.out.println("jurusan+IPK : " + daftar);

        // 4. Kunci yang boleh null WAJIB dibungkus, kalau tidak -> NullPointerException.
        daftar.sort(Comparator.comparing(Mahasiswa::getEmail,
                Comparator.nullsLast(Comparator.naturalOrder())));
        System.out.println("email       : " + daftar);   // Andi (email null) terlempar ke belakang

        // 5. Comparator itu objek biasa: dibuat sekali, dipakai di mana pun urutan dibutuhkan.
        Comparator<Mahasiswa> ipkNaik = Comparator.comparingDouble(Mahasiswa::getIpk);
        System.out.println("tertinggi   : " + Collections.max(daftar, ipkNaik));
        System.out.println("terendah    : " + daftar.stream().min(ipkNaik).orElseThrow());
        // Kunci kedua (nama) membuat hasilnya PASTI walau ada seri — tidak lagi bergantung pada
        // urutan list sebelum diurutkan.
        System.out.println("3 teratas   : " + daftar.stream()
                .sorted(ipkNaik.reversed().thenComparing(Mahasiswa::getNama))
                .limit(3)
                .map(Mahasiswa::getNama)
                .collect(Collectors.toList()));

        // 6. TreeSet dan TreeMap menerima comparator lewat constructor-nya.
        TreeSet<Mahasiswa> perNama = new TreeSet<>(Comparator.comparing(Mahasiswa::getNama));
        perNama.addAll(daftar);
        System.out.println("TreeSet nama: " + perNama.size() + " isi, pertama " + perNama.first());

        // 7. JEBAKAN: bagi TreeSet, comparator yang mengembalikan 0 berarti "objek ini SAMA".
        //    Andi dan Budi sama-sama 3.2, jadi satu di antaranya DIBUANG tanpa error apa pun.
        TreeSet<Mahasiswa> perIpk = new TreeSet<>(ipkNaik);
        perIpk.addAll(daftar);
        System.out.println("TreeSet IPK : " + perIpk.size() + " isi -> " + perIpk);
    }
}""",
            },
            {
                "body": [
                    "Tujuh jebakan yang benar-benar memakan korban:",
                    "",
                    "1) JANGAN mengurutkan dengan pengurangan. (a, b) -> a.getUmur() - b.getUmur() terlihat pintar",
                    "   dan benar untuk umur manusia. Tapi begitu kuncinya angka besar atau boleh negatif — saldo,",
                    "   selisih waktu, koordinat — pengurangannya OVERFLOW dan tandanya terbalik:",
                    "     2000000000 - (-2000000000)  ->  -294967296   (negatif! padahal kiri jauh lebih besar)",
                    "     Integer.compare(2000000000, -2000000000)  ->  1   (benar)",
                    "   Selalu Integer.compare / Long.compare / Double.compare. Double.compare juga satu-satunya",
                    "   cara benar untuk pecahan: ia menangani NaN dan -0.0 yang membuat 'a < b' bertingkah aneh.",
                    "",
                    "2) Posisi reversed() menentukan APA yang dibalik. Perhatikan bedanya:",
                    "     comparing(getJurusan).thenComparing(getIpk).reversed()",
                    "       -> membalik SELURUH rangkaian: jurusan jadi Z-A, IPK jadi turun. Jarang yang dimaui.",
                    "     comparing(getJurusan).thenComparing(comparingDouble(getIpk).reversed())",
                    "       -> jurusan tetap A-Z, hanya IPK yang turun. Ini yang biasanya kamu maksud.",
                    "   Tidak ada error di kedua versi; yang salah cuma isi layar, dan bug semacam ini bertahan",
                    "   lama karena datanya 'kelihatan terurut'.",
                    "",
                    "3) Urutan String itu leksikografis, bukan alfabetis. Perbandingannya memakai nomor karakter,",
                    "   dan SEMUA huruf besar bernomor lebih kecil daripada huruf kecil:",
                    "     [\"Zebra\", \"apel\", \"Mangga\"] naturalOrder -> [Mangga, Zebra, apel]",
                    "   Kalau yang kamu mau urutan buat mata manusia, pakai String.CASE_INSENSITIVE_ORDER:",
                    "     daftar.sort(Comparator.comparing(Mahasiswa::getNama, String.CASE_INSENSITIVE_ORDER));",
                    "   -> [apel, Mangga, Zebra]. (Untuk bahasa berhuruf beraksen, java.text.Collator lebih tepat.)",
                    "",
                    "4) Kunci null meledak. Comparator.comparing(Mahasiswa::getEmail) pada data yang emailnya",
                    "   pernah null melempar NullPointerException di tengah pengurutan — dan pesannya tidak",
                    "   menyebut email sama sekali, cuma \"Cannot invoke compareTo() because c1 is null\".",
                    "   nullsFirst/nullsLast memutuskan null ditaruh di ujung mana; keduanya sah, yang tidak sah",
                    "   adalah berpura-pura null tidak ada. Bedakan dua sasarannya:",
                    "     daftar.sort(Comparator.nullsLast(cmp))                    -> ELEMEN-nya yang boleh null",
                    "     comparing(getEmail, Comparator.nullsLast(naturalOrder())) -> KUNCI-nya yang boleh null",
                    "",
                    "5) Comparator yang tidak konsisten dengan equals bisa MENGHILANGKAN data. Bagi List.sort ini",
                    "   tidak masalah — seri berarti 'boleh berdampingan'. Tapi TreeSet dan TreeMap tidak memakai",
                    "   equals sama sekali; bagi mereka compare(a, b) == 0 berarti 'ini elemen yang SAMA', jadi",
                    "   yang kedua ditolak masuk tanpa satu pun error (lihat baris terakhir contoh di atas: empat",
                    "   mahasiswa masuk, tiga yang tersimpan). Obatnya: untuk TreeSet/TreeMap selalu rangkai kunci",
                    "   sampai comparator-nya tidak mungkin seri, misalnya .thenComparing(Mahasiswa::getNim).",
                    "   Soal kontrak equals dan hashCode sendiri, lihat materi Class Object.",
                    "",
                    "6) Comparator yang tidak transitif ditolak mentah-mentah oleh sort. Kalau comparator-mu bisa",
                    "   bilang a < b, b < c, tapi c < a (paling sering karena aturan if bertingkat yang ditulis",
                    "   tangan), Java melempar:",
                    "     java.lang.IllegalArgumentException: Comparison method violates its general contract!",
                    "   Pesan ini membingungkan karena ia menuduh sort, padahal yang rusak comparator-nya. Ia juga",
                    "   licik: hanya muncul kalau datanya cukup banyak, jadi tes kecil lolos dan produksi tumbang.",
                    "   Merangkai Comparator.comparing/thenComparing membuat masalah ini nyaris mustahil terjadi.",
                    "",
                    "7) Lambda polos di dalam comparing sering gagal DIKOMPILASI dengan pesan yang menyesatkan.",
                    "   Java menebak tipe parameter lambda dari konteksnya, dan begitu hasil comparing langsung",
                    "   dirangkai, konteks itu hilang:",
                    "     daftar.sort(Comparator.comparing(m -> m.getNama()).reversed());",
                    "     error: cannot find symbol  symbol: method getNama()  location: variable m of type Object",
                    "   Pesannya menuduh getNama() tidak ada, padahal method itu jelas-jelas ada; yang sebenarnya",
                    "   terjadi, Java menyerah menebak tipe m dan memakai Object. Pakai method reference",
                    "   (Mahasiswa::getNama) yang tipenya tidak perlu ditebak, atau tulis tipenya terang-terangan",
                    "   ((Mahasiswa m) -> m.getNama()). Ini alasan praktis kedua kenapa bentuk comparing dengan",
                    "   method reference lebih jarang menyusahkan daripada lambda (a, b) yang ditulis tangan.",
                    "",
                    "Satu lagi yang bukan soal urutan tapi selalu ikut tersandung: daftar.sort(cmp) mengubah list",
                    "DI TEMPAT, jadi listnya harus boleh diubah. Yang TIDAK boleh: List.of(...), List.copyOf(...),",
                    "Collections.unmodifiableList(...), dan hasil stream().toList() (Java 16+). Semuanya melempar",
                    "UnsupportedOperationException — pesan yang tidak menyebut urutan sama sekali, sehingga orang",
                    "mencari salahnya di comparator. Perhatikan bedanya dengan .collect(Collectors.toList()) yang",
                    "justru mengembalikan ArrayList biasa dan boleh disort. Jalan keluarnya dua: bungkus dulu dengan",
                    "new ArrayList<>(...), atau pakai stream().sorted(cmp) yang memang tidak menyentuh list aslinya.",
                ],
            },
        ],
    },
    {
        "title": "29. Class di dalam Class: Nested, Inner, dan Anonymous",
        "sections": [
            {
                "body": [
                    "Sampai sini setiap class selalu kamu tulis sejajar dengan class lain.",
                    "Padahal Java mengizinkan class ditulis DI DALAM class lain, dan kamu sudah",
                    "beberapa kali melihatnya di materi sebelumnya tanpa pernah diberi tahu namanya:",
                    "",
                    "  - Map.Entry<String, Integer> di materi Collection Framework.",
                    "    Kenapa ada titik di tengah nama tipe? Karena Entry itu class di dalam Map.",
                    "  - static class Builder di materi Design Pattern & Clean Code.",
                    "  - new Runnable() { public void run() { ... } } di materi Lambda Expression,",
                    "    yang cuma diberi label 'cara lama' lalu ditinggalkan begitu saja.",
                    "",
                    "Bentuknya ada EMPAT, dan yang membedakan cuma dua pertanyaan:",
                    "di mana ia ditulis, dan apakah ia butuh objek pembungkusnya.",
                    "",
                    "  Bentuk          Ditulis di          Butuh objek luar?  Punya nama?",
                    "  -------------   -----------------   -----------------  -----------",
                    "  static nested   badan class         tidak              ya",
                    "  inner           badan class         YA                 ya",
                    "  local           badan method        tergantung         ya",
                    "  anonymous       di tengah ekspresi  tergantung         TIDAK",
                    "",
                    "Kenapa repot-repot? Karena sebagian class cuma punya arti di dalam satu class",
                    "saja. Node hanya berguna buat struktur data yang memilikinya; Entry hanya",
                    "berarti buat Map. Menaruhnya di berkas sendiri membuat orang lain mengira ia",
                    "boleh dipakai di mana-mana, padahal ia detail dalaman yang bisa berubah kapan",
                    "saja. Menaruhnya di dalam pemiliknya menyatakan hubungan itu lewat kode.",
                ],
            },
            {
                "heading": "Static nested class: Node yang tinggal di dalam pemiliknya",
                "code": """public class Tumpukan {
    // Node cuma punya arti di dalam Tumpukan, jadi ia tinggal di dalamnya.
    // static = tidak butuh objek Tumpukan untuk dibuat.
    private static class Node {
        final String isi;
        final Node bawah;

        Node(String isi, Node bawah) {
            this.isi = isi;
            this.bawah = bawah;
        }
    }

    private Node puncak = null;

    void dorong(String isi) {
        puncak = new Node(isi, puncak);
    }

    String ambil() {
        String isi = puncak.isi;
        puncak = puncak.bawah;
        return isi;
    }

    boolean kosong() {
        return puncak == null;
    }

    public static void main(String[] args) {
        Tumpukan t = new Tumpukan();
        t.dorong("A");
        t.dorong("B");
        t.dorong("C");
        while (!t.kosong()) {
            System.out.print(t.ambil() + " ");
        }
        System.out.println();   // C B A
    }
}""",
            },
            {
                "body": [
                    "Static nested class = class biasa yang kebetulan tinggal di dalam class lain.",
                    "Kata static di situ TIDAK berarti 'cuma ada satu' atau 'milik bersama' seperti",
                    "pada field static. Artinya cuma satu hal: ia tidak butuh objek pembungkusnya.",
                    "",
                    "Menyebutnya dari luar: NamaLuar.NamaDalam.",
                    "  Mahasiswa.Builder b = new Mahasiswa.Builder();   // materi Design Pattern",
                    "  Map.Entry<String, Integer> e = ...;               // materi Collection Framework",
                    "Titik di situ bukan 'ambil field dari objek', melainkan 'class Entry yang ada di",
                    "dalam Map'. Itu juga sebabnya import java.util.Map; saja sudah cukup untuk",
                    "memakai Map.Entry: Entry ikut terbawa oleh pemiliknya.",
                    "",
                    "Berkas .class-nya pun terpisah, dinamai dengan tanda dolar:",
                    "  Tumpukan.class      Tumpukan$Node.class",
                    "Nama seperti Sekolah$1 atau Sekolah$1Penghitung yang muncul di stack trace bukan",
                    "tanda kode rusak; itu class bersarang yang namanya dibuatkan compiler.",
                    "",
                    "Inner class = nested class TANPA static. Bedanya besar: tiap objeknya diam-diam",
                    "menyimpan referensi ke satu objek luar, dan karena itu ia boleh langsung memakai",
                    "field objek luar tadi tanpa dioper lewat constructor atau parameter.",
                    "",
                    "Dua akibatnya yang bikin orang tersandung:",
                    "  1. Membuatnya harus lewat objek luarnya:  luar.new Dalam()",
                    "     new Dalam() polos di dalam method static gagal dengan pesan",
                    "     'non-static variable this cannot be referenced from a static context'.",
                    "     Dari class lain pesannya lain lagi:",
                    "     'an enclosing instance that contains C.Dalam is required'.",
                    "  2. Selama objek inner-nya masih dipegang, objek LUARNYA tidak bisa dibersihkan",
                    "     garbage collector, walau isinya sudah tidak dipakai siapa pun. Satu Node",
                    "     inner yang nyangkut di cache bisa menahan seluruh list induknya di memori.",
                    "",
                    "Aturan praktisnya: tulis static, kecuali kamu benar-benar butuh field objek luar.",
                    "Node di contoh atas static justru karena itu, ia cuma butuh isinya sendiri.",
                ],
            },
            {
                "heading": "Inner, local, dan anonymous dalam satu program",
                "code": """import java.util.ArrayList;
import java.util.List;

public class Sekolah {
    private final String nama;
    private final List<String> murid = new ArrayList<>();

    Sekolah(String nama) {
        this.nama = nama;
    }

    // INNER class (tanpa static): tiap objek Absen menempel pada SATU objek
    // Sekolah, jadi ia boleh langsung memakai field milik objek luar itu.
    class Absen {
        private final String nama = "Daftar hadir";   // menutupi nama milik Sekolah

        void cetak() {
            // `nama` polos = milik Absen. Milik Sekolah: Sekolah.this.nama
            System.out.println(nama + " " + Sekolah.this.nama + ": " + murid);
        }
    }

    void daftar(String m) {
        murid.add(m);
    }

    public static void main(String[] args) {
        Sekolah s = new Sekolah("SMA 1");
        s.daftar("Andi");
        s.daftar("Budi");

        // Inner class dibuat LEWAT objek luarnya, bukan `new Absen()` polos.
        Sekolah.Absen a = s.new Absen();
        a.cetak();                       // Daftar hadir SMA 1: [Andi, Budi]

        // LOCAL class: class yang dideklarasikan di dalam sebuah method.
        class Penghitung {
            int hitung() {
                return s.murid.size();   // menangkap s, yang effectively final
            }
        }
        System.out.println(new Penghitung().hitung());    // 2

        // ANONYMOUS class: class tanpa nama, langsung dibuat satu objeknya.
        Runnable tugas = new Runnable() {
            private int dijalankan = 0;  // anonymous class boleh punya field sendiri

            @Override
            public void run() {
                dijalankan++;
                System.out.println("Jalan ke-" + dijalankan + " di " + s.nama);
            }
        };
        tugas.run();                     // Jalan ke-1 di SMA 1
        tugas.run();                     // Jalan ke-2 di SMA 1
    }
}""",
            },
            {
                "body": [
                    "Membedah new Runnable() { ... } — sintaks yang mustahil ditebak sendiri.",
                    "Ia TERLIHAT seperti membuat objek dari interface, padahal itu justru dilarang",
                    "(materi OOP: Abstract & Interface). Yang terjadi sebenarnya dua langkah sekaligus:",
                    "  1. Java membuat class BARU tanpa nama yang implements Runnable; isinya blok",
                    "     kurung kurawal sesudah new Runnable().",
                    "  2. Java langsung membuat satu objek dari class tanpa nama itu.",
                    "Jadi yang di-new bukan interface-nya, melainkan class dadakan tadi. Kalau yang",
                    "ditulis nama class (bukan interface), blok itu berarti 'extends class tersebut'.",
                    "Begitulah cara meng-override sebuah abstract class secara dadakan.",
                    "",
                    "Local class jarang dipakai, tapi ada: class yang dideklarasikan di dalam method,",
                    "hanya terlihat di dalam method itu. Berguna saat butuh beberapa method sekaligus",
                    "untuk satu perhitungan, tapi tidak mau menambah class yang terlihat orang lain.",
                    "",
                    "Aturan penangkapan variabel — berlaku untuk inner, local, anonymous, dan lambda:",
                    "variabel LOKAL yang dipakai dari dalam harus final atau effectively final.",
                    "'Effectively final' artinya cukup tidak pernah diberi nilai baru setelah diisi;",
                    "tidak wajib menulis kata final. Melanggarnya menghasilkan pesan ini:",
                    "  local variables referenced from an inner class must be final or effectively final",
                    "Ini bukan kerewelan compiler. Nilainya DISALIN saat objeknya dibuat, jadi kalau",
                    "variabel aslinya boleh berubah, salinannya jadi basi tanpa ada yang tahu.",
                    "Field objek (this.sesuatu) tidak kena aturan ini, yang dibatasi cuma variabel",
                    "lokal. Jalan keluarnya: salin dulu ke variabel baru, atau simpan di field.",
                    "",
                    "Jebakan this: di dalam inner/anonymous class, this menunjuk objek DALAM, bukan",
                    "objek luar. Untuk objek luar tulis NamaLuar.this — lihat Sekolah.this.nama di",
                    "contoh atas. Di lambda TIDAK begitu: lambda tidak punya this sendiri, jadi this",
                    "di dalamnya tetap objek luar. Dua bentuk yang terlihat setara, perilakunya beda.",
                    "",
                    "Lambda sudah ada dan lebih ringkas. Lalu kapan anonymous class masih dipakai?",
                    "  - Interface-nya punya LEBIH DARI SATU abstract method; lambda cuma bisa untuk",
                    "    functional interface yang abstract method-nya tepat satu.",
                    "  - Yang mau di-override abstract class, bukan interface. Lambda tidak bisa.",
                    "  - Butuh field/state sendiri, seperti dijalankan di contoh atas.",
                    "  - Trik new TypeReference<>() { } di library JSON seperti Jackson: blok kosong",
                    "    itu memaksa Java membuat subclass, dan tipe generiknya ikut tersimpan di",
                    "    berkas class — satu-satunya cara library membacanya saat program berjalan.",
                    "    (Generics dibahas beberapa materi lagi.)",
                    "",
                    "Kalau ragu: interface satu method dan tidak butuh state -> pakai lambda.",
                    "Selain itu, anonymous class masih bentuk paling ringkas yang tersedia.",
                ],
            },
        ],
    },
    {
        "title": "30. Stream API",
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
            {
                "body": [
                    "Ada satu baris di contoh di atas yang muncul begitu saja: IntStream.range(...).",
                    "Itu anggota keluarga stream yang lain, dan tanpa mengenalnya kamu akan buntu",
                    "justru di dua hal paling biasa - menjumlahkan angka dan menghitung rata-rata.",
                    "",
                    "Sebabnya begini: Stream<Integer> TIDAK punya sum(). Stream biasa berisi objek",
                    "apa saja, dan Java tidak bisa memastikan objek itu bisa dijumlahkan. Maka",
                    "disediakan tiga stream khusus untuk tipe primitif, yang isinya angka betulan:",
                    "",
                    "  IntStream      untuk int (juga short, byte, char)",
                    "  LongStream     untuk long",
                    "  DoubleStream   untuk double",
                    "",
                    "Cara menyeberang antar-keluarga:",
                    "",
                    "  Stream<T>        --mapToInt / mapToLong / mapToDouble-->  stream primitif",
                    "  stream primitif  --mapToObj-->  Stream<T>  (tiap angka jadi objek apa pun)",
                    "  stream primitif  --boxed()-->   Stream<Integer> dan sejenisnya",
                    "",
                    "Yang cuma ada di stream primitif:",
                    "",
                    "  IntStream.range(0, 5)          0,1,2,3,4  - batas atas TIDAK ikut",
                    "  IntStream.rangeClosed(1, 5)    1,2,3,4,5  - batas atas ikut",
                    "  sum()                          jumlah semua, langsung int/long/double",
                    "  average()                      OptionalDouble - list kosong tidak punya",
                    "                                 rata-rata (lihat materi Optional)",
                    "  max() / min()                  OptionalInt",
                    "  summaryStatistics()            count, sum, min, average, max sekaligus",
                    "",
                    "Jadi IntStream.range(0, nama.size()) di contoh tadi cuma cara menghasilkan",
                    "indeks 0, 1, 2 - for biasa yang ditulis sebagai stream, supaya dua list bisa",
                    "dibaca berbarengan.",
                    "",
                    "Sekalian satu bentuk baru yang makin sering kamu temui di kode Java baru:",
                    "  .toList()                        Java 16+, ringkas",
                    "  .collect(Collectors.toList())    bentuk lama, panjang",
                    "Keduanya menghasilkan List, dan bedanya sudah kamu tabrak di materi Comparable &",
                    "Comparator: yang keluar dari toList() tidak bisa diubah lagi.",
                ]
            },
            {
                "heading": "IntStream & kawan-kawan",
                "code": """import java.util.List;
import java.util.stream.IntStream;

public class Main {
    public static void main(String[] args) {
        List<Integer> angka = List.of(5, 3, 8, 1, 9);

        // Stream<Integer> tidak punya sum(). Turun dulu ke IntStream.
        System.out.println(angka.stream().mapToInt(n -> n).sum());   // 26
        System.out.println(angka.stream().mapToInt(n -> n)
                .average().getAsDouble());                            // 5.2

        System.out.println(IntStream.range(0, 5).sum());         // 10  (0..4)
        System.out.println(IntStream.rangeClosed(1, 5).sum());   // 15  (1..5)

        // mapToObj: menyeberang balik ke Stream<T>
        List<String> label = IntStream.rangeClosed(1, 3)
                .mapToObj(i -> "ke-" + i)
                .toList();            // Java 16+, sama dengan collect(...toList())
        System.out.println(label);    // [ke-1, ke-2, ke-3]

        // boxed(): IntStream -> Stream<Integer>
        System.out.println(IntStream.range(0, 3).boxed().toList());   // [0, 1, 2]

        System.out.println(IntStream.of(4, 9, 2).max().getAsInt());   // 9
        System.out.println(IntStream.of(4, 9, 2).summaryStatistics());
        // IntSummaryStatistics{count=3, sum=15, min=2, average=5.000000, max=9}
    }
}"""
            },
        ],
    },
    {
        "title": "31. Generics",
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

    // Bounded type: T harus Number atau turunannya (Integer, Double, ...)
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
            {
                "body": [
                    "Bounded type <T extends Number> dibaca: T boleh Number sendiri, atau class",
                    "mana pun yang MENURUNI Number - Integer, Long, Double, Float, BigDecimal.",
                    "Kata 'extends' di sini agak menipu: ia dipakai juga untuk interface",
                    "(<T extends Comparable<T>>), dan boleh digabung dengan tanda &, misalnya",
                    "<T extends Number & Comparable<T>>.",
                    "",
                    "Imbalannya nyata: karena Java kini tahu T pasti Number, kamu boleh memanggil",
                    "method milik Number di dalamnya. Dari situlah item.doubleValue() di contoh di",
                    "atas datang - doubleValue() milik class Number, bukan milik T. Tanpa batasan",
                    "itu, T dianggap Object saja dan doubleValue() tidak ada.",
                    "",
                    "int dan double TIDAK termasuk, dan ini bukan soal kecil. Tipe primitif bukan",
                    "objek: ia tidak punya class induk, tidak menuruni apa pun, dan tidak punya",
                    "method sama sekali. Generics hanya bekerja dengan objek. Karena itu:",
                    "",
                    "  List<int> angka;       ->  error: unexpected type / required: reference",
                    "  List<Integer> angka;   ->  ini yang benar",
                    "",
                    "Lalu kenapa jumlahkan(List.of(1, 2, 3)) di atas tetap jalan? Karena autoboxing",
                    "(lihat materi Kelas Pembungkus): 1, 2, 3 diam-diam dibungkus jadi Integer",
                    "dulu. Yang sampai ke method-mu adalah List<Integer>, bukan list berisi int.",
                    "",
                    "TYPE ERASURE - alasan di balik batasan-batasan generics yang terasa aneh.",
                    "Kurung sudut hanya hidup SAAT KOMPILASI. Sesudah dikompilasi, semua <T>",
                    "dihapus (erased) dan bytecode-nya cuma tahu Object; compiler-lah yang sudah",
                    "memeriksa semuanya dan menyisipkan cast untukmu. Saat program berjalan,",
                    "List<String> dan List<Integer> adalah class yang sama persis.",
                    "",
                    "Tiga akibat yang cepat atau lambat akan kamu tabrak sendiri:",
                    "  1. new T() dan new T[10] tidak bisa ditulis - saat runtime T sudah tidak",
                    "     ada, jadi tidak ada yang bisa di-new. Yang biasa dipakai sebagai ganti:",
                    "     (T[]) new Object[10], atau cukup pakai List<T>.",
                    "  2. x instanceof List<String> ditolak compiler. Yang boleh cuma",
                    "     x instanceof List<?>.",
                    "  3. Dua method dengan parameter List<String> dan List<Integer> dianggap",
                    "     kembar, jadi tidak bisa dipakai sebagai overload.",
                ]
            },
        ],
    },
    {
        "title": "32. Optional & Null Safety",
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
        "title": "33. Multithreading & Concurrency Dasar",
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
                    "Satu baris di contoh tadi belum dijelaskan, dan bentuknya akan terus muncul:",
                    "",
                    "  public static void main(String[] args) throws InterruptedException",
                    "",
                    "Kenapa main tiba-tiba punya throws? Karena t1.join() - dan nanti juga",
                    "Thread.sleep() - adalah method yang bisa DISELA di tengah jalan. Keduanya",
                    "melempar InterruptedException, dan itu checked exception: Java menolak",
                    "mengompilasi kalau kamu tidak mengurusnya (lihat materi Exception Handling).",
                    "",
                    "Dua cara mengurusnya, dan pilihannya bukan soal selera:",
                    "  1. throws di tanda tangan method -> serahkan ke pemanggil. Praktis untuk",
                    "     main, karena di atas main memang tidak ada siapa-siapa lagi.",
                    "  2. try-catch -> WAJIB kalau kodenya ada di dalam run(). Runnable.run()",
                    "     sudah ditetapkan tanpa throws, dan method yang meng-override tidak",
                    "     boleh menambah checked exception baru.",
                    "",
                    "Thread.sleep(ms) artinya: hentikan thread INI selama sekian milidetik.",
                    "  Thread.sleep(1000);   // satu detik",
                    "Ia menidurkan thread yang sedang memanggilnya, bukan thread lain - menulisnya",
                    "di dalam main menghentikan main, bukan t1. Di contoh-contoh concurrency,",
                    "sleep dipakai untuk berpura-pura sedang mengerjakan sesuatu yang lama, supaya",
                    "urutan kejadiannya kelihatan.",
                    "",
                    "Dan ini idiom yang layak kamu tiru bulat-bulat setiap kali menangkapnya:",
                    "",
                    "  } catch (InterruptedException e) {",
                    "      Thread.currentThread().interrupt();",
                    "  }",
                    "",
                    "Alasannya halus tapi penting. Tiap thread punya satu tanda: 'ada yang minta",
                    "kamu berhenti'. Ketika sleep melihat tanda itu, ia melempar",
                    "InterruptedException dan sekaligus MENGHAPUS tandanya. Kalau kamu menangkap",
                    "exception-nya lalu diam saja, permintaan berhenti tadi hilang tanpa jejak dan",
                    "bagian program di atasmu tidak akan pernah tahu. Memanggil interrupt()",
                    "memasang tandanya kembali. Yang tidak boleh sama sekali: catch kosong.",
                ]
            },
            {
                "heading": "Thread.sleep & InterruptedException",
                "code": """public class Main {
    // Cara 1: dilempar ke atas. Boleh untuk main -- inilah yang dipakai
    // contoh thread di atas.
    public static void main(String[] args) throws InterruptedException {
        System.out.println("mulai");
        Thread.sleep(200);                 // berhenti 200 milidetik
        System.out.println("200 ms kemudian");

        Thread t = new Thread(Main::kerja);
        t.start();
        t.join();
    }

    // Cara 2: ditangkap sendiri. WAJIB kalau dipanggil dari dalam run(),
    // karena Runnable.run() tidak boleh menambah throws.
    static void kerja() {
        try {
            Thread.sleep(100);
            System.out.println("tugas selesai");
        } catch (InterruptedException e) {
            // Menangkapnya MENGHAPUS tanda interupsi. Pasang lagi supaya
            // pemanggil di atas masih tahu ada permintaan berhenti.
            Thread.currentThread().interrupt();
        }
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
        "title": "34. Concurrency Lanjutan: Future, Atomic, dan Koleksi Aman-Thread",
        "sections": [
            {
                "body": [
                    "Materi sebelumnya sengaja berhenti di dasar: thread, race condition, synchronized,",
                    "dan satu baris pool.submit(). Ia berhenti tepat sebelum dua hal yang justru paling",
                    "sering muncul di kode Java sungguhan:",
                    "  1. Cara MENGAMBIL hasil sebuah tugas yang sudah dilempar ke thread lain.",
                    "  2. Cara berbagi data antar-thread tanpa menulis kunci sendiri.",
                    "",
                    "Di kode backend masa kini, synchronized jarang diketik tangan. Yang dipakai adalah",
                    "perkakas siap pakai di paket java.util.concurrent. Isi materi ini itu semua.",
                    "",
                    "ExecutorService, lebih dalam dari materi sebelumnya:",
                    "  execute(Runnable) -> jalankan saja. Tidak ada nilai kembali, dan kalau tugasnya",
                    "                       melempar exception, jejaknya cuma tercetak di log thread.",
                    "  submit(tugas)     -> mengembalikan Future: tanda terima tempat hasil (atau error)",
                    "                       tugas itu akan muncul nanti.",
                    "",
                    "Jenis pool yang disediakan kelas Executors:",
                    "  newFixedThreadPool(n)     -> n thread tetap. Pilihan default yang aman.",
                    "  newSingleThreadExecutor() -> 1 thread; tugas dikerjakan berurutan sesuai antrean.",
                    "  newCachedThreadPool()     -> thread dibuat sesuai kebutuhan, dibuang setelah",
                    "                               menganggur 60 detik. Hati-hati untuk beban besar.",
                    "  newScheduledThreadPool(n) -> bisa menunda tugas atau mengulangnya berkala.",
                    "",
                    "Mematikan pool - dan ini WAJIB:",
                    "  shutdown()    -> tolak tugas baru; yang sudah masuk antrean tetap dituntaskan.",
                    "  shutdownNow() -> selain itu, interrupt tugas yang sedang jalan dan kembalikan",
                    "                   daftar tugas yang belum sempat dimulai.",
                    "  awaitTermination(waktu, satuan) -> tunggu sampai pool benar-benar kosong.",
                    "                   Mengembalikan true kalau keburu, false kalau waktunya habis.",
                    "",
                    "JEBAKAN: thread di dalam pool bukan daemon thread. Lupa shutdown() berarti program",
                    "menggantung dan tidak pernah keluar, walau baris terakhir main() sudah lewat lama.",
                    "",
                    "Sekilas bentuk baru yang akan kamu temui (Java 19+ dan 21) - kenali saja dulu:",
                    "  try (ExecutorService pool = Executors.newFixedThreadPool(4)) {   // AutoCloseable",
                    "      pool.submit(...);",
                    "  }   // shutdown() + menunggu sampai selesai dikerjakan otomatis di sini",
                    "",
                    "  Executors.newVirtualThreadPerTaskExecutor()    // Java 21: virtual thread",
                    "Virtual thread adalah thread yang sangat murah - ribuan sekaligus bukan masalah -",
                    "karena dikelola JVM, bukan sistem operasi. Cara memakainya persis sama: tetap",
                    "ExecutorService, Callable, dan Future. Yang berubah cuma harganya.",
                    "",
                    "Runnable vs Callable<T>:",
                    "  Runnable    -> void run().  TIDAK boleh melempar checked exception.",
                    "  Callable<T> -> T call() throws Exception. MENGEMBALIKAN nilai, dan boleh melempar.",
                    "  Keduanya functional interface (materi Lambda), jadi keduanya bisa ditulis sebagai lambda.",
                    "",
                    "Future<T> = tanda terima atas tugas yang sudah diantre:",
                    "  get()              -> MEMBLOKIR sampai hasilnya siap.",
                    "  get(waktu, satuan) -> menyerah menunggu, lalu melempar TimeoutException. Tugasnya",
                    "                        sendiri TIDAK ikut berhenti; ia jalan terus di pool.",
                    "  isDone()           -> sudah kelar? (selesai, gagal, dan dibatalkan: tiga-tiganya true)",
                    "  cancel(true)       -> batalkan; true berarti interrupt thread yang mengerjakannya.",
                    "",
                    "JEBAKAN TERBESAR di sini: exception yang terjadi DI DALAM tugas tidak muncul di layar.",
                    "Ia disimpan di Future dan baru meledak saat get(), terbungkus ExecutionException;",
                    "penyebab aslinya diambil dengan e.getCause(). Kalau Future-nya tidak pernah di-get,",
                    "error itu hilang tanpa jejak sama sekali. Itulah sebabnya submit() yang hasilnya",
                    "diabaikan begitu saja jadi salah satu cara termudah menyembunyikan bug sendiri.",
                ],
            },
            {
                "heading": "Callable, Future, dan hasil yang ditunggu",
                "code": """import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.*;

public class Main {
    // Callable<T> MENGEMBALIKAN nilai, dan boleh melempar checked exception.
    static Callable<Integer> tugasKuadrat(int n) {
        return () -> {
            Thread.sleep(50);                  // pura-pura kerja lama
            if (n == 0) {
                throw new IllegalArgumentException("n tidak boleh 0");
            }
            return n * n;
        };
    }

    public static void main(String[] args) throws InterruptedException {
        ExecutorService pool = Executors.newFixedThreadPool(3);

        List<Future<Integer>> antrean = new ArrayList<>();
        for (int n = 1; n <= 4; n++) {
            antrean.add(pool.submit(tugasKuadrat(n)));   // submit -> dapat Future
        }

        int total = 0;
        for (Future<Integer> f : antrean) {
            try {
                total += f.get();              // MENUNGGU sampai tugas itu selesai
            } catch (ExecutionException e) {
                System.out.println("gagal: " + e.getCause().getMessage());
            }
        }
        System.out.println("total kuadrat 1..4 = " + total);

        // Error di dalam tugas tidak langsung meledak; ia menunggu di get().
        Future<Integer> rusak = pool.submit(tugasKuadrat(0));
        try {
            rusak.get();
        } catch (ExecutionException e) {
            System.out.println("penyebab asli   : " + e.getCause());
        }

        // get(timeout): berhenti menunggu; tugasnya sendiri TIDAK ikut berhenti.
        Future<Integer> lambat = pool.submit(() -> {
            Thread.sleep(3000);
            return 99;
        });
        try {
            lambat.get(100, TimeUnit.MILLISECONDS);
        } catch (TimeoutException e) {
            System.out.println("kelamaan, cancel: " + lambat.cancel(true));
            System.out.println("isDone sesudahnya: " + lambat.isDone());
        } catch (ExecutionException e) {
            System.out.println("gagal: " + e.getCause());
        }

        // shutdown(): tolak tugas baru, sisa antrean tetap dituntaskan.
        pool.shutdown();
        boolean beres = pool.awaitTermination(5, TimeUnit.SECONDS);
        System.out.println("pool berhenti rapi: " + beres);
    }
}""",
            },
            {
                "body": [
                    "Kenapa counter++ rusak kalau dipakai banyak thread?",
                    "Satu baris di layar, tapi TIGA langkah di CPU: baca nilai, tambah 1, tulis balik.",
                    "Dua thread bisa sama-sama membaca 100, dua-duanya menulis 101, dan satu kenaikan",
                    "lenyap tanpa error apa pun. Bug seperti ini nyaris tidak pernah muncul saat dicoba",
                    "sekali dua kali; ia muncul di produksi, sesekali, dengan angka yang selalu KURANG.",
                    "",
                    "Kelas Atomic (paket java.util.concurrent.atomic) menyelesaikannya tanpa kunci:",
                    "  AtomicInteger / AtomicLong -> penghitung.",
                    "  AtomicReference<T>         -> satu objek yang diganti-ganti antar-thread.",
                    "",
                    "Method yang perlu dikenali:",
                    "  incrementAndGet()         -> naikkan 1, kembalikan nilai SESUDAH naik.",
                    "  getAndIncrement()         -> kembalikan nilai SEBELUM naik (persis beda ++i dan i++).",
                    "  addAndGet(n)              -> tambah n sekaligus.",
                    "  get() / set(n)            -> baca / timpa nilainya.",
                    "  compareAndSet(lama, baru) -> ganti HANYA kalau isinya masih 'lama'. Hasilnya boolean.",
                    "",
                    "compareAndSet (CAS) adalah fondasi semuanya: satu instruksi CPU yang membandingkan",
                    "dan menulis dalam sekali gerak, sehingga tidak ada celah untuk disela thread lain.",
                    "",
                    "volatile - kata kunci yang paling sering disalahpahami, jadi baca pelan-pelan:",
                    "  YANG DIJAMIN: setiap thread membaca nilai TERBARU, bukan salinan basi di cache",
                    "                CPU-nya sendiri. Cocok untuk penanda seperti 'boolean berhenti'.",
                    "  YANG TIDAK  : volatile BUKAN kunci. hitung++ pada variabel volatile tetap rusak,",
                    "                karena yang dijaganya cuma baca dan tulis, bukan ketiganya sekaligus.",
                    "  Butuh baca-ubah-tulis yang aman? Pakai Atomic, bukan volatile.",
                    "",
                    "Koleksi aman-thread. HashMap dan ArrayList di materi Collection TIDAK aman dipakai",
                    "beberapa thread sekaligus. Penggantinya:",
                    "  ConcurrentHashMap    -> pengganti HashMap; banyak thread boleh menulis sekaligus.",
                    "  CopyOnWriteArrayList -> setiap penulisan menyalin seluruh isi. Hanya untuk daftar",
                    "                          yang sering dibaca tapi jarang diubah (misal daftar listener).",
                    "  BlockingQueue        -> antrean produsen-konsumen: take() menunggu sampai ada isi,",
                    "                          put() menunggu sampai ada ruang. Tanpa wait/notify manual.",
                    "",
                    "HashMap biasa yang diisi dua thread sekaligus bukan cuma 'kadang salah': entri bisa",
                    "hilang, size() bisa berbohong, dan di Java lama get() pernah berputar selamanya sampai",
                    "CPU mentok 100% - semuanya tanpa satu pun exception yang memberi tahu.",
                    "",
                    "Method ConcurrentHashMap yang memang aman dipakai bersamaan:",
                    "  peta.merge(kunci, 1, Integer::sum)    -> tambah 1, atau isi 1 kalau belum ada.",
                    "  peta.computeIfAbsent(kunci, k -> ...) -> hitung nilainya sekali saja (pola cache).",
                    "  peta.putIfAbsent(kunci, nilai)        -> isi hanya kalau kuncinya masih kosong.",
                    "  CATATAN: get() lalu put() sebagai dua langkah terpisah TETAP tidak aman, sekalipun",
                    "  petanya ConcurrentHashMap. Yang dijamin utuh cuma SATU panggilan method.",
                    "",
                    "Aturan praktisnya: pakai perkakas siap pakai di atas, jangan mengunci sendiri.",
                    "synchronized buatan tangan gampang berujung deadlock - dua thread saling menunggu",
                    "kunci yang dipegang lawannya - dan deadlock tidak melempar error apa pun.",
                    "Programnya cuma diam membeku, dan itu jauh lebih sulit dilacak daripada crash.",
                    "",
                    "Contoh terakhir memakai CompletableFuture: Future yang bisa DIRANGKAI, dan bentuk",
                    "asinkron yang paling sering ditemui di kode Java baru.",
                    "  supplyAsync(fn)     -> mulai kerja di thread lain, hasilnya menyusul.",
                    "  thenApply(fn)       -> olah hasilnya begitu tiba, tanpa memblokir.",
                    "  thenCombine(cf, fn) -> gabungkan hasil dua CompletableFuture.",
                    "  allOf(a, b, ...)    -> selesai kalau semuanya sudah selesai.",
                    "  join()              -> ambil hasil akhirnya; sama seperti get() tapi tanpa checked",
                    "                         exception, jadi enak dipakai di dalam lambda.",
                    "  exceptionally(fn)   -> nilai cadangan kalau ada langkah yang gagal.",
                    "Tanpa pool sendiri, semuanya jalan di ForkJoinPool.commonPool() - dan thread di sana",
                    "daemon, jadi kalau main() keburu selesai, kerjanya ikut mati di tengah jalan.",
                ],
            },
            {
                "heading": "Penghitung rusak vs AtomicInteger, dan ConcurrentHashMap",
                "code": """import java.util.Map;
import java.util.concurrent.*;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.concurrent.atomic.AtomicReference;

public class Main {
    static int biasa = 0;                  // TIDAK aman dipakai banyak thread
    static final AtomicInteger aman = new AtomicInteger(0);

    public static void main(String[] args) throws Exception {
        ExecutorService pool = Executors.newFixedThreadPool(4);
        Map<String, Integer> peta = new ConcurrentHashMap<>();

        Future<?>[] tugas = new Future<?>[4];
        for (int t = 0; t < 4; t++) {
            tugas[t] = pool.submit(() -> {
                for (int i = 0; i < 50_000; i++) {
                    biasa++;                    // baca -> tambah -> tulis
                    aman.incrementAndGet();     // satu langkah, tak bisa disela
                    peta.merge("klik", 1, Integer::sum);
                }
            });
        }
        for (Future<?> f : tugas) {
            f.get();                   // tunggu semuanya benar-benar selesai
        }
        pool.shutdown();

        int harapan = 4 * 50_000;
        System.out.println("harapan          : " + harapan);
        System.out.println("AtomicInteger    : " + aman.get());
        System.out.println("ConcurrentHashMap: " + peta.get("klik"));
        // Angka di bawah ini berubah tiap kali program dijalankan.
        System.out.println("int biasa        : " + biasa);
        // Kenaikan bisa HILANG, tidak pernah bertambah: selalu true.
        System.out.println("biasa <= harapan : " + (biasa <= harapan));

        // compareAndSet: ubah HANYA kalau isinya masih sama. Fondasi Atomic.
        AtomicInteger stok = new AtomicInteger(10);
        System.out.println("CAS 10 -> 9      : " + stok.compareAndSet(10, 9));
        System.out.println("CAS 10 -> 8      : " + stok.compareAndSet(10, 8));
        System.out.println("stok akhir       : " + stok.get());

        AtomicReference<String> status = new AtomicReference<>("menunggu");
        status.compareAndSet("menunggu", "jalan");
        System.out.println("status           : " + status.get());
    }
}""",
            },
            {
                "heading": "CompletableFuture: merangkai kerja asinkron",
                "code": """import java.util.concurrent.CompletableFuture;

public class Main {
    // Pura-pura panggilan lambat: query database atau layanan lain.
    static int ambilHarga(String barang) {
        try {
            Thread.sleep(100);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
        return barang.equals("buku") ? 50000 : 30000;
    }

    static String panggilServer() {
        throw new IllegalStateException("server mati");
    }

    public static void main(String[] args) {
        // supplyAsync: kerjakan di thread lain; keduanya jalan BERBARENGAN.
        CompletableFuture<Integer> buku =
                CompletableFuture.supplyAsync(() -> ambilHarga("buku"));
        CompletableFuture<Integer> pena =
                CompletableFuture.supplyAsync(() -> ambilHarga("pena"));

        // thenCombine: satukan dua hasil, tanpa satu pun get() yang memblokir.
        CompletableFuture<Integer> total = buku.thenCombine(pena, (a, b) -> a + b);

        // thenApply: olah lagi hasilnya, masih di jalur asinkron.
        CompletableFuture<String> struk = total.thenApply(t -> "Total: Rp" + t);

        // join() = get() tanpa checked exception.
        System.out.println(struk.join());

        // allOf: tunggu SEMUA selesai; hasilnya Void, bukan nilai tugasnya.
        CompletableFuture<Void> semua = CompletableFuture.allOf(buku, pena);
        semua.join();
        System.out.println("dua-duanya selesai : " + semua.isDone());
        System.out.println("harga buku         : " + buku.join());

        // exceptionally: nilai cadangan kalau ada langkah yang gagal.
        // e di sini CompletionException; error aslinya ada di getCause().
        String pesan = CompletableFuture.supplyAsync(Main::panggilServer)
                .thenApply(s -> "tidak pernah sampai sini: " + s)
                .exceptionally(e -> "cadangan: " + e.getCause().getMessage())
                .join();
        System.out.println(pesan);
    }
}""",
            },
        ],
    },
    {
        "title": "35. File I/O & Serialization",
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
        "title": "36. JDBC: Menghubungkan Java ke Database",
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
        "title": "37. Unit Testing dengan JUnit",
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
        "title": "38. Design Pattern & Clean Code",
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
                    "Dua baris di kode itu memakai kata static dengan arti yang BERBEDA, dan",
                    "keduanya gampang terlewat karena tampak seperti kata sambung biasa.",
                    "",
                    "  private static Konfigurasi instance;",
                    "",
                    "static di sini menandai FIELD: satu nilai untuk seluruh aplikasi, bukan satu",
                    "per objek (lihat materi Anggota Class). Justru itulah yang membuat Singleton",
                    "mungkin - kalau instance disimpan per objek, tiap pemanggil punya salinannya",
                    "sendiri dan tidak ada yang 'satu' lagi.",
                    "",
                    "  static class Builder { ... }",
                    "",
                    "static di sini menandai CLASS DI DALAM CLASS: static nested class (lihat materi",
                    "Class di dalam Class). Ia hidup di dalam Mahasiswa, jadi namanya dari luar",
                    "adalah Mahasiswa.Builder - dan itulah sebabnya pemanggilannya berbunyi",
                    "new Mahasiswa.Builder(), bukan new Builder(). Kata static-nya berarti Builder",
                    "tidak butuh objek Mahasiswa untuk dibuat, yang memang harus begitu: Builder",
                    "justru ada untuk membuat Mahasiswa yang belum ada.",
                ]
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
        "title": "39. Git, Maven/Gradle & Alur Kerja Developer",
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
        "title": "40. Roadmap Menjadi Programmer Handal",
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
