JAVA_MATERIALS = [
    {
        "title": "1. Pengenalan Java & Persiapan",
        "sections": [
            {
                "body": [
                    "Java adalah bahasa pemrograman berorientasi objek, atau OOP",
                    "(object-oriented programming). Gampangnya, program Java disusun dari",
                    "objek, yaitu benda di dalam program yang punya data dan bisa mengerjakan",
                    "sesuatu. Soal objek nanti dibahas sendiri. Sekarang cukup kenal namanya",
                    "dulu.",
                    "",
                    "Sedikit soal asal-usulnya:",
                    "  - Java dibikin oleh James Gosling di Sun Microsystems, dan rilis tahun 1995.",
                    "  - Slogannya \"Write Once, Run Anywhere\" (WORA). Artinya, tulis sekali,",
                    "    jalan di mana aja.",
                    "  - Kode Java nggak langsung dijalankan komputer. Kodenya dikompilasi",
                    "    dulu jadi bytecode, yaitu kode perantara. Bytecode itu lalu",
                    "    dijalankan oleh Java Virtual Machine (JVM).",
                    "",
                    "Ada tiga singkatan yang bakal sering kamu dengar:",
                    "  1. JDK (Java Development Kit). Dipakai untuk menulis dan menjalankan",
                    "     kode. Ini yang perlu kamu pasang.",
                    "  2. JRE (Java Runtime Environment). Cuma untuk menjalankan aplikasi Java.",
                    "  3. JVM (Java Virtual Machine). Mesin yang menjalankan bytecode.",
                    "",
                    "Cara memasangnya:",
                    "  - Di Windows, Mac, maupun Linux, unduh OpenJDK dari https://adoptium.net.",
                    "  - Sesudah terpasang, cek dengan perintah java -version di terminal.",
                    "",
                    "Langkah bikin program pertama:",
                    "  1. Bikin berkas bernama Hello.java. Nama berkasnya harus sama persis",
                    "     dengan nama class di dalamnya.",
                    "  2. Tulis kodenya. Contohnya ada di bawah.",
                    "  3. Kompilasi dengan perintah javac Hello.java.",
                    "  4. Jalankan dengan perintah java Hello.",
                    "",
                    "Dua hal yang perlu kamu tahu soal bentuk programnya:",
                    "  - Setiap program butuh method main. Di situlah program mulai jalan.",
                    "  - Java membedakan huruf besar dan huruf kecil. Istilahnya",
                    "    case-sensitive. Jadi Hello dan hello itu dua nama yang beda.",
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
                    "Kita bahas baris demi baris:",
                    "",
                    "  public class Hello",
                    "    Bikin class bernama Hello. Untuk sekarang, anggap aja class itu",
                    "    wadah tempat kodemu ditulis.",
                    "",
                    "  public static void main(String[] args)",
                    "    Method utama, tempat program mulai jalan. Arti tiap katanya:",
                    "      public          bisa diakses dari mana aja",
                    "      static          bisa dipanggil tanpa bikin objek dulu",
                    "      void            nggak mengembalikan nilai apa pun",
                    "      String[] args   argumen yang diketik di baris perintah",
                    "",
                    "  System.out.println(\"Halo Dunia!\")",
                    "    Mencetak teks ke layar, lalu pindah ke baris baru.",
                    "",
                    "Setiap perintah di Java, istilahnya statement, diakhiri titik koma (;).",
                    "Sepasang kurung kurawal { } menandai awal dan akhir sebuah blok, yaitu",
                    "satu kelompok kode.",
                ]
            },
            {
                "body": [
                    "Angka versi Java",
                    "",
                    "Java terus nambah fitur dari versi ke versi. Makanya kode Java di dua",
                    "proyek bisa kelihatan beda jauh, padahal bahasanya sama.",
                    "",
                    "Tapi nggak semua versi dipakai orang. Proyek sungguhan biasanya memilih",
                    "versi LTS (Long Term Support), yaitu versi yang masih dikasih perbaikan",
                    "bertahun-tahun sesudah rilis:",
                    "",
                    "  8    warisan. Masih banyak di proyek lama. Sudah punya lambda & Stream.",
                    "  11   LTS pertama sesudah 8. Sudah punya var dan 'java Berkas.java'.",
                    "  17   LTS yang paling umum sekarang. Sudah punya record, sealed, text block.",
                    "  21   LTS. Pattern matching di switch, virtual thread.",
                    "  25   LTS terbaru, rilis September 2025.",
                    "",
                    "Versi di antaranya (9, 10, 12 sampai 16, 18 sampai 20, 22 sampai 24)",
                    "tetap rilis. Bedanya, umur dukungannya pendek, jadi jarang dipilih",
                    "proyek.",
                    "",
                    "Cek versi punyamu:",
                    "",
                    "  java -version",
                    "  openjdk version \"17.0.16\" 2025-07-15",
                    "                  ^^ ini yang penting: JDK-mu versi 17.",
                    "",
                    "Angka ini kepakai waktu kamu nyalin kode dari internet. Kadang javac",
                    "menolak kode itu dengan pesan 'preview feature' atau 'illegal start of",
                    "expression'. Sering kali kodenya nggak salah. JDK-mu aja yang lebih tua",
                    "daripada fitur yang dipakai kode itu.",
                    "",
                    "Nanti kamu bakal ketemu var (butuh Java 10), switch bentuk panah (butuh",
                    "14), dan record (butuh 16). Tiap kali fitur seperti itu muncul, versi",
                    "minimalnya ikut disebut, supaya kamu tahu JDK-mu cukup atau nggak.",
                    "",
                    "Sejak Java 11 ada satu kemudahan: program yang cuma satu berkas boleh",
                    "dijalankan tanpa javac.",
                    "",
                    "  java Hello.java     // langsung jalan, tidak ada Hello.class yang tertinggal",
                    "",
                    "Cara ini enak buat nyoba potongan kode kecil. Begitu programmu terdiri",
                    "dari lebih dari satu berkas, balik lagi ke javac lalu java seperti",
                    "langkah di atas.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Hari pertama PKL di tim yang memakai Java biasanya dimulai dengan tugas",
                    "yang sama: pasang JDK yang versinya cocok dengan proyek, lalu kompilasi",
                    "dan jalankan kodenya di laptopmu sendiri. Program Java di server toko",
                    "online maupun di aplikasi kasir melewati dua langkah yang persis sama,",
                    "javac lalu java.",
                    "",
                    "Kasus kecil: mentor mengirim berkas absen.java. Isinya class public",
                    "bernama Absen. Begitu kamu mengetik javac absen.java, compiler menolak",
                    "dengan pesan class Absen is public, should be declared in a file named",
                    "Absen.java.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Baca pesannya pelan-pelan. Compiler udah menyebut nama berkas yang",
                    "     dia mau, yaitu Absen.java.",
                    "  2. Bandingkan nama berkas dengan nama class, huruf demi huruf. Java",
                    "     membedakan huruf besar dan kecil, jadi absen dan Absen itu dua nama",
                    "     yang beda.",
                    "  3. Ganti nama berkasnya, lalu ulangi dua langkah dari materi ini:",
                    "      javac Absen.java",
                    "      java Absen",
                    "  4. Cek kasus pinggirnya: perintah java ditulis dengan nama class saja.",
                    "     Kalau kamu mengetik java Absen.class, Java mencari class bernama",
                    "     Absen.class dan menjawab Could not find or load main class.",
                    "",
                    "Ingat: cek java -version sebelum mulai. Kalau proyeknya butuh Java 17",
                    "dan JDK-mu masih 11, kode yang benar pun bisa ditolak javac.",
                ]
            },
        ],
    },
    {
        "title": "2. Anatomi Berkas Java: package, import, dan komentar",
        "sections": [
            {
                "body": [
                    "Di materi sebelumnya kamu udah nulis class dan method main. Sekarang",
                    "kita lihat sisa kepala berkasnya, yaitu baris-baris di atas class.",
                    "Bagian ini yang pertama kamu lihat tiap kali membuka kode orang lain.",
                    "",
                    "Baris pertama hampir setiap berkas Java di proyek sungguhan bentuknya begini:",
                    "",
                    "  package com.tokobuku.penjualan;",
                    "",
                    "Package itu folder tempat sebuah class tinggal. Nama package juga jadi",
                    "bagian dari nama lengkap class-nya. Jadi nama lengkap class Keranjang",
                    "yang ada di package itu adalah com.tokobuku.penjualan.Keranjang. Nama",
                    "lengkap ini disebut nama berkualifikasi penuh (fully qualified name),",
                    "dan nama ini yang dipakai Java di belakang layar.",
                    "",
                    "Ada tiga aturan package yang wajib kamu ikuti:",
                    "  1. Deklarasi package harus jadi baris kode pertama di berkas. Yang",
                    "     boleh ada di atasnya cuma komentar.",
                    "  2. Nama package harus persis mengikuti susunan folder:",
                    "       package com.tokobuku.penjualan;",
                    "       -> berkasnya duduk di  com/tokobuku/penjualan/Keranjang.java",
                    "     Kalau foldernya nggak cocok, javac sering masih mau mengompilasi.",
                    "     Tapi waktu dijalankan, perintah java menolak dengan pesan seperti:",
                    "       wrong name: com/tokobuku/penjualan/Keranjang",
                    "     Aturan ini saudara dekat aturan \"nama berkas harus sama dengan nama",
                    "     class public\".",
                    "  3. Ditulis huruf kecil semua, dipisah titik, tanpa garis bawah. Nama",
                    "     seperti com.TokoBuku memang lolos compiler, tapi praktis nggak ada",
                    "     yang nulis begitu.",
                    "",
                    "Kenapa nama domainnya dibalik jadi com.tokobuku? Nama domain seperti",
                    "tokobuku.com udah pasti unik di seluruh dunia. Kalau dibalik lalu",
                    "dipakai sebagai nama package, package-mu ikut unik. Nggak perlu ada",
                    "panitia yang ngatur siapa boleh pakai nama apa.",
                    "",
                    "Berkas tanpa baris package masuk ke \"default package\". Semua contoh kode",
                    "di aplikasi ini memakainya, supaya bisa langsung dijalankan dengan javac",
                    "dan java biasa. Di proyek sungguhan hal ini hampir nggak pernah terjadi,",
                    "soalnya class di default package nggak bisa diimpor dari package mana",
                    "pun.",
                    "",
                    "Susunan folder yang bakal kamu temui di hampir semua proyek Java:",
                    "",
                    "  proyek-toko/",
                    "    pom.xml                 <- daftar library & konfigurasi build (Maven)",
                    "    src/",
                    "      main/",
                    "        java/               <- kode program ada di bawah sini",
                    "          com/tokobuku/penjualan/",
                    "            Keranjang.java",
                    "            Faktur.java",
                    "        resources/          <- bukan kode: gambar, konfigurasi, template",
                    "      test/",
                    "        java/               <- kode tes, package-nya sengaja sama",
                    "          com/tokobuku/penjualan/",
                    "            KeranjangTest.java",
                    "    target/                 <- hasil build (.class, .jar). Jangan di-commit.",
                    "",
                    "Kode dan tes dipisah jadi dua pohon folder, padahal package-nya sama.",
                    "Alasannya begini:",
                    "  - Yang dikirim ke pengguna cuma isi src/main. Tes nggak ikut masuk ke",
                    "    berkas .jar.",
                    "  - Karena package-nya sama, tes tetap boleh memakai method yang nggak",
                    "    public. Kode dari package lain nggak punya hak itu.",
                    "  - Gradle pakai susunan yang sama persis. Bedanya cuma folder hasilnya",
                    "    bernama build/.",
                    "  - Jadi begitu lihat folder src/main/java, kamu langsung tahu itu",
                    "    proyek Java bergaya Maven.",
                ],
            },
            {
                "body": [
                    "Sesudah package, datang blok import. Bagian ini yang paling sering",
                    "disalahpahami. Import nggak memuat atau menyalin kode apa pun ke",
                    "berkasmu. Semua class yang tersedia udah tersedia dari awal, mau diimpor",
                    "atau nggak. Gunanya import cuma satu: supaya kamu boleh nulis nama",
                    "pendek, nggak harus nama berkualifikasi penuh.",
                    "",
                    "Dua baris ini sama persis buat compiler:",
                    "",
                    "  java.util.ArrayList<String> a = new java.util.ArrayList<>(); // tanpa import",
                    "  ArrayList<String> a = new ArrayList<>();                     // pakai import",
                    "",
                    "Ada tiga bentuk import yang bakal kamu temui:",
                    "",
                    "  import java.util.ArrayList;",
                    "      Satu class, satu baris. Bentuk ini paling jelas dibaca, dan bentuk",
                    "      ini juga yang ditulis otomatis oleh IDE, yaitu aplikasi khusus",
                    "      untuk menulis kode.",
                    "",
                    "  import java.util.*;",
                    "      Ini wildcard. Artinya semua class yang ada langsung di java.util.",
                    "      Sub-package nggak ikut, jadi java.util.function tetap harus",
                    "      diimpor sendiri. Bentuk ini praktis untuk contoh singkat. Di",
                    "      proyek tim biasanya dihindari, soalnya asal sebuah nama jadi nggak",
                    "      kelihatan dan gampang terjadi tabrakan nama.",
                    "",
                    "  import static java.lang.Math.max;",
                    "      Ini impor static. Yang dibawa nama member static-nya, yaitu method",
                    "      atau variabel static milik class itu. Jadi tulisan \"Math.\" boleh",
                    "      dibuang, cukup tulis max(a, b). Bentuk yang sama muncul sebagai",
                    "      import static ...Assertions.*; di setiap berkas tes JUnit. Makanya",
                    "      assertEquals(...) di sana bisa ditulis tanpa nama class di",
                    "      depannya.",
                    "",
                    "String, System, Math, Integer, dan Object nggak pernah diimpor. Semuanya",
                    "tinggal di package java.lang, dan java.lang diimpor otomatis ke setiap",
                    "berkas Java. Cuma package itu yang diperlakukan istimewa begini.",
                    "",
                    "Tabrakan nama",
                    "",
                    "Blok import layak dibaca, jangan dilewati. Contohnya begini:",
                    "  - Di JDK ada dua class bernama List: java.util.List (koleksi data) dan",
                    "    java.awt.List (komponen daftar di jendela aplikasi desktop).",
                    "    Fungsinya beda total.",
                    "  - Melihat tulisan List di tengah berkas belum cukup untuk tahu yang",
                    "    mana. Yang menentukan artinya adalah baris import di kepala berkas.",
                    "  - Kalau kamu nulis import java.util.*; dan import java.awt.*;",
                    "    sekaligus, lalu memakai List, compiler menolak dengan pesan",
                    "    reference to List is ambiguous.",
                    "  - Java nggak punya cara mengganti nama waktu impor. Nggak ada bentuk",
                    "    import ... as ... seperti di Python. Kalau dua class yang namanya",
                    "    sama sama-sama dibutuhkan, biasanya salah satunya diimpor, dan yang",
                    "    lain ditulis dengan nama panjangnya:",
                    "      import java.util.List;",
                    "      List<String> data = new ArrayList<>();            // java.util.List",
                    "      java.awt.List daftarLayar = new java.awt.List();  // ditulis penuh",
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
                    "Kita bedah kepala berkas di atas baris demi baris:",
                    "  package com.tokobuku.penjualan;",
                    "    Berkasnya ada di folder com/tokobuku/penjualan/.",
                    "  import java.util.ArrayList;",
                    "    Izin menulis ArrayList tanpa nama panjang.",
                    "  import java.util.List;",
                    "    List di berkas ini artinya java.util.List.",
                    "  /** ... */ di atas class",
                    "    Javadoc: dokumentasi, bukan perintah.",
                    "  public class Keranjang",
                    "    Class public, jadi berkasnya wajib bernama Keranjang.java.",
                    "  public static final int BATAS_BARANG",
                    "    Konstanta. Ditandai dengan nama huruf besar semua.",
                    "  private final List<String> barang",
                    "    Data internal. Nggak bisa disentuh dari luar class.",
                    "  public boolean tambah(String nama)",
                    "    Method publik. Ini yang dipakai kode lain.",
                    "",
                    "Blok ini sengaja dibuat sebagai potongan, bukan program utuh. Di",
                    "dalamnya nggak ada method main. Selain itu, karena ada baris package,",
                    "blok ini cuma bisa dikompilasi kalau foldernya udah disusun dengan",
                    "benar.",
                    "",
                    "Komentar",
                    "",
                    "Java punya tiga bentuk komentar, dan compiler mengabaikan ketiganya",
                    "sepenuhnya:",
                    "  // ...      komentar satu baris, berlaku sampai ujung baris itu saja.",
                    "  /* ... */   komentar beberapa baris, berhenti tepat di penutupnya.",
                    "  /** ... */  Javadoc: bentuk khusus /* */ untuk alat pembuat dokumentasi.",
                    "",
                    "Jebakan: di contoh-contoh materi ini sering ada baris seperti ini.",
                    "",
                    "  System.out.println(a % b);   // 1",
                    "",
                    "Angka 1 di ujung baris itu bukan perintah, dan nggak dicetak oleh apa",
                    "pun. Itu catatan untukmu, isinya hasil yang bakal muncul di layar. Kalau",
                    "semua komentarnya dihapus, programnya tetap jalan sama persis. Itu bukti",
                    "komentar nggak ikut dijalankan.",
                    "",
                    "Tag Javadoc yang bakal sering kamu lihat:",
                    "  @param nama           menjelaskan satu parameter method.",
                    "  @return               menjelaskan nilai yang dikembalikan.",
                    "  @throws Exception     menjelaskan kapan method melempar exception itu.",
                    "  @author               siapa penulisnya.",
                    "  {@link Kelas#member}  tautan ke bagian lain dokumentasi; dipakai di tengah",
                    "                        kalimat, bukan sebagai baris tersendiri.",
                    "",
                    "Perintah javadoc mengubah semua tag itu jadi halaman HTML. IDE juga",
                    "menampilkannya sebagai tooltip, yaitu kotak kecil yang muncul waktu",
                    "kursormu berhenti di atas nama method.",
                    "",
                    "Ingat: tanda @ di dalam /** */ cuma teks biasa. Lain halnya dengan",
                    "@Override, @Test, dan @BeforeEach yang ditulis di luar komentar. Itu",
                    "anotasi, dan anotasi betul-betul memengaruhi program: dicek compiler dan",
                    "dibaca framework. Bedanya cuma satu, ada di dalam /** */ atau nggak.",
                    "",
                    "Kalau dua hal ini tertukar, orang bisa mengira dokumentasi mengubah",
                    "perilaku program. Atau sebaliknya, mengira @Override boleh dihapus tanpa",
                    "akibat apa-apa.",
                    "",
                    "Konvensi penamaan",
                    "",
                    "Konvensi penamaan bisa kamu pakai sebagai alat bantu membaca kode. Dari",
                    "bentuk namanya aja kamu udah tahu benda itu apa:",
                    "",
                    "  PascalCase",
                    "    tipe: class, interface, enum, record. Contoh: Keranjang",
                    "  camelCase",
                    "    variabel atau method. Contoh: totalHarga",
                    "  HURUF_BESAR_DENGAN_GARIS_BAWAH",
                    "    konstanta (static final). Contoh: BATAS_BARANG",
                    "  huruf kecil dipisah titik",
                    "    package. Contoh: com.tokobuku",
                    "",
                    "Ada juga akhiran nama yang menandai peran sebuah class. Dari akhiran ini",
                    "kamu bisa nebak susunan sebuah proyek sebelum membuka satu berkas pun:",
                    "  XxxTest        unit test untuk Xxx (materi Unit Testing dengan JUnit)",
                    "  XxxService     logika bisnis: menghitung, memutuskan, mengatur alur",
                    "  XxxRepository  urusan simpan-ambil data (database, berkas)",
                    "  XxxController  pintu masuk permintaan dari luar, misalnya dari web",
                    "  XxxException   exception buatan sendiri",
                    "  XxxUtils       kumpulan method static pembantu, biasanya tanpa objek",
                    "  XxxImpl        implementasi konkret dari interface bernama Xxx",
                    "",
                    "Nggak satu pun akhiran itu dipaksa compiler. Tapi hampir semua",
                    "programmer Java mematuhinya. Kalau kamu melanggarnya, kodemu terasa",
                    "asing buat orang yang membacanya nanti, termasuk kamu sendiri tiga bulan",
                    "lagi.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Begitu kamu membuka proyek Java di kantor, yang pertama kamu lihat",
                    "adalah kepala berkas: baris package, deretan import, lalu Javadoc di",
                    "atas class. Dari baris package kamu tahu berkas itu tinggal di folder",
                    "mana. Dari import kamu tahu nama pendek seperti List menunjuk class yang",
                    "mana.",
                    "",
                    "Kasus kecil: berkas CetakStruk.java di aplikasi kasir punya import",
                    "java.util.*; dan import java.awt.*; (untuk jendela cetak). Begitu kamu",
                    "menambah baris List<String> barang = new ArrayList<>();, compiler",
                    "menolak dengan pesan reference to List is ambiguous.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Baca pesannya. Compiler menemukan dua class bernama List yang",
                    "     sama-sama terbawa: java.util.List dan java.awt.List.",
                    "  2. Cari sumbernya di blok import. Dua wildcard itulah yang membawa",
                    "     keduanya sekaligus.",
                    "  3. Tambahkan import satu class untuk List yang kamu maksud. Import",
                    "     satu class selalu menang atas wildcard:",
                    "      import java.util.*;",
                    "      import java.awt.*;",
                    "      import java.util.List;   // List di berkas ini = java.util.List",
                    "  4. Cek kasus pinggirnya: kalau berkas yang sama juga butuh",
                    "     java.awt.List, tulis yang itu dengan nama panjangnya. Java nggak",
                    "     punya bentuk import ... as ....",
                    "",
                    "Ingat: cara paling rapi tetap mengganti semua wildcard dengan import",
                    "satu per satu, seperti yang ditulis IDE. Dengan begitu, asal setiap nama",
                    "langsung kelihatan dari kepala berkas.",
                ]
            },
        ],
    },
    {
        "title": "3. Variabel & Tipe Data",
        "sections": [
            {
                "body": [
                    "Variabel itu tempat menyimpan data, mirip kotak yang dikasih nama.",
                    "Setiap variabel di Java punya tipe data. Tipe ini menentukan isi macam",
                    "apa yang boleh masuk ke kotaknya: angka bulat, angka desimal, huruf, dan",
                    "seterusnya.",
                    "",
                    "Java punya delapan tipe data primitif, yaitu tipe dasar yang udah",
                    "tersedia di bahasanya:",
                    "  Tipe     Ukuran   Rentang nilai",
                    "  ------   ------   --------------------------------",
                    "  byte     1 byte   -128 s/d 127",
                    "  short    2 byte   -32.768 s/d 32.767",
                    "  int      4 byte   -2^31 s/d 2^31-1 (paling umum)",
                    "  long     8 byte   -2^63 s/d 2^63-1",
                    "  float    4 byte   bilangan desimal",
                    "  double   8 byte   bilangan desimal presisi ganda",
                    "  char     2 byte   satu karakter ('A', '1', '@')",
                    "  boolean  1 bit*   true atau false",
                    "",
                    "Catatan: isi boolean memang cuma 1 bit informasi, tapi Java nggak",
                    "menetapkan berapa tempat yang dipakainya di memori. JVM biasanya memakai",
                    "1 byte.",
                    "",
                    "Selain primitif, ada tipe data referensi. Yang paling sering kamu pakai",
                    "adalah String, yaitu kumpulan karakter seperti \"Halo\". Array, class, dan",
                    "interface juga termasuk tipe referensi. Ketiganya dibahas nanti.",
                    "",
                    "Bentuk umum deklarasi variabel:",
                    "",
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
                    "Dua jenis tanda kutip di contoh tadi nggak boleh tertukar:",
                    "",
                    "  'A'   kutip tunggal -> char, tepat satu karakter.",
                    "  \"A\"   kutip ganda   -> String, teks berisi berapa pun karakter.",
                    "  'AB'  ERROR: unclosed character literal (char cuma muat satu).",
                    "  \"\"    String kosong, sah. char kosong tidak ada.",
                    "",
                    "Terus gimana cara nulis karakter yang nggak bisa diketik langsung,",
                    "misalnya tombol Enter? Java pakai escape sequence, yaitu garis miring",
                    "terbalik (backslash) diikuti satu huruf. Gabungan dua tanda itu dihitung",
                    "satu karakter.",
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
                    "  char br = '\\n';   // satu char, nilainya 10",
                    "",
                    "Di dalam tanda kutip, backslash selalu dianggap awal escape sequence.",
                    "Contohnya alamat folder Windows \"C:\\Users\". Compiler menolaknya dengan",
                    "pesan illegal escape character, soalnya \\U bukan escape yang dikenal.",
                    "Yang benar pakai dua backslash.",
                ]
            },
            {
                "body": [
                    "Konstanta adalah variabel yang nilainya nggak bisa diubah lagi. Caranya",
                    "pakai kata kunci final:",
                    "",
                    "  final double PI = 3.14;",
                    "  PI = 3.0;  // ERROR! tidak bisa diubah",
                    "",
                    "Aturan memberi nama variabel:",
                    "  1. Boleh berisi huruf, angka, _ dan $, tapi nggak boleh diawali angka.",
                    "  2. Nggak boleh memakai kata kunci Java, misalnya int, class, atau if.",
                    "  3. Ikuti gaya camelCase: kata pertama huruf kecil, kata berikutnya",
                    "     diawali huruf besar. Contohnya jumlahMahasiswa.",
                    "  4. Pilih nama yang menjelaskan isinya, supaya kodenya gampang dibaca.",
                    "",
                    "Sejak Java 10 ada kata kunci var. Dengan var, kamu nggak perlu nulis",
                    "tipenya, karena compiler nebak sendiri dari nilai awalnya. Istilahnya",
                    "type inference.",
                    "",
                    "  var nama = \"Andi\";   // otomatis dianggap String",
                    "  var angka = 10;       // otomatis dianggap int",
                    "",
                    "Konversi tipe data ada dua arah:",
                    "  - Widening, dari tipe kecil ke tipe besar. Terjadi otomatis: int ->",
                    "    long -> double.",
                    "  - Narrowing, dari tipe besar ke tipe kecil. Harus ditulis manual, dan",
                    "    bagian desimalnya dibuang. Jadi (int) 3.99 hasilnya 3.",
                    "      int x = (int) 3.99;   // x = 3",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Tiap data yang dicatat aplikasi sekolah, kasir, atau bank harus dikasih",
                    "tipe sebelum disimpan. Tipe yang salah jarang langsung bikin error.",
                    "Akibatnya baru muncul belakangan: nol di depan nomor hilang, angka",
                    "desimal kepotong, atau total yang tiba-tiba negatif karena lewat batas",
                    "int.",
                    "",
                    "Kasus kecil: kamu diminta menyiapkan variabel untuk satu baris data",
                    "rapor. Isinya nomor induk 0012345, nama Siti Aminah, rata-rata 87,5,",
                    "predikat A, status naik kelas, dan nomor HP orang tua 081234567890.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Untuk tiap data, tanya dulu: angka ini bakal dihitung atau cuma",
                    "     dicatat? Rata-rata dihitung, jadi double. Predikat cuma satu huruf,",
                    "     jadi char.",
                    "  2. Nomor induk dan nomor HP nggak pernah dijumlah atau dikali. Simpan",
                    "     sebagai String, supaya nol di depannya tetap ada.",
                    "  3. Status naik kelas cuma punya dua kemungkinan, jadi boolean:",
                    "      String nomorInduk = \"0012345\";",
                    "      String nama = \"Siti Aminah\";",
                    "      double rataRata = 87.5;",
                    "      char predikat = 'A';",
                    "      boolean naikKelas = true;",
                    "      String hpOrangTua = \"081234567890\";",
                    "  4. Cek kasus pinggirnya: 81234567890 jauh di atas batas int (sekitar",
                    "     2,1 miliar), jadi int nggak muat. long muat, tapi nol depannya",
                    "     tetap hilang.",
                    "",
                    "Jebakan: int nomor = 0012345; lolos compiler, tapi isinya 5349. Angka",
                    "bulat yang diawali nol dibaca Java sebagai bilangan basis 8 (oktal).",
                ]
            },
        ],
    },
    {
        "title": "4. Kelas Pembungkus & Konversi Tipe",
        "sections": [
            {
                "body": [
                    "Di materi sebelumnya kamu udah kenal tipe primitif: int, double, char,",
                    "boolean, dan teman-temannya. Untuk setiap tipe primitif itu, Java juga",
                    "menyediakan pasangan berupa objek. Namanya kelas pembungkus (wrapper",
                    "class). Ada delapan primitif dan delapan pembungkus, berpasangan",
                    "satu-satu:",
                    "",
                    "  Primitif   Pembungkus     Primitif   Pembungkus",
                    "  --------   ----------     --------   ----------",
                    "  int        Integer        float      Float",
                    "  double     Double         short      Short",
                    "  long       Long           byte       Byte",
                    "  char       Character      boolean    Boolean",
                    "",
                    "Kebanyakan nama pembungkus cuma beda huruf besar di depannya. Ada dua",
                    "yang beda: int jadi Integer, dan char jadi Character. Kalau kamu nulis",
                    "Int atau Char, compiler langsung menolak.",
                    "",
                    "Kenapa Java repot menyediakan dua-duanya? Ada tiga alasan:",
                    "  1. Generic, koleksi, dan Optional cuma bisa menampung objek.",
                    "       List<int> daftar;       // ERROR, tidak akan dikompilasi",
                    "       List<Integer> daftar;   // benar",
                    "     Makanya di materi Collection Framework, Generics, dan Optional kamu",
                    "     selalu ketemu List<Integer> atau Map<String, Integer>, dan nggak",
                    "     pernah List<int>.",
                    "  2. Pembungkus bisa bernilai null, sedangkan primitif nggak pernah",
                    "     bisa. Kalau dipakai sebagai field (variabel milik objek), Integer",
                    "     nilai awalnya null, yang bisa berarti \"belum diisi\". Field int",
                    "     nilai awalnya 0, jadi \"belum diisi\" dan \"nilainya nol\" nggak bisa",
                    "     dibedakan.",
                    "       Integer nilaiUjian;   // default null -> 'belum diisi'",
                    "       int absen;            // default 0    -> 'belum diisi' dan",
                    "                             //                 nol tak terbedakan",
                    "  3. Pembungkus punya method dan konstanta bawaan. Contohnya",
                    "     Integer.parseInt untuk mengubah teks jadi angka, dan",
                    "     Integer.MAX_VALUE untuk batas atasnya.",
                    "",
                    "Dua istilah yang bakal terus kamu dengar:",
                    "  - Autoboxing: primitif otomatis dibungkus jadi objek (int -> Integer).",
                    "  - Unboxing: kebalikannya, objek dibuka jadi primitif.",
                    "",
                    "Dua-duanya terjadi sendiri tanpa kamu nulis apa pun. Justru karena nggak",
                    "kelihatan, dua jebakan di bagian bawah materi ini sering menipu",
                    "programmer yang udah berpengalaman.",
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
                    "Teks jadi angka",
                    "",
                    "parseInt kamu butuhkan begitu angkanya datang dari tempat lain selain",
                    "Scanner. Argumen baris perintah (String[] args), isi berkas, dan data",
                    "JSON semuanya sampai ke programmu sebagai teks. Yang perlu kamu tahu:",
                    "  - parseX mengembalikan primitif, sedangkan valueOf mengembalikan pembungkus.",
                    "      int a = Integer.parseInt(\"20\");      // int",
                    "      Integer b = Integer.valueOf(\"20\");   // Integer",
                    "    Sehari-hari pakai parseInt. valueOf baru perlu kalau kamu memang",
                    "    butuh objeknya, misalnya mau dimasukkan ke List<Integer>.",
                    "  - Integer.parseInt rewel soal spasi dan titik. Tiga panggilan di bawah",
                    "    ini melempar NumberFormatException, nggak mengembalikan 0:",
                    "      Integer.parseInt(\" 20 \")   // spasi ikut terbaca",
                    "      Integer.parseInt(\"3.0\")    // int tidak kenal titik desimal",
                    "      Integer.parseInt(\"\")       // teks kosong",
                    "    Solusinya, panggil teks.trim() dulu untuk membuang spasi di awal dan",
                    "    akhir. Anehnya, Double.parseDouble dengan teks \" 3.5 \" malah lolos,",
                    "    karena dia memangkas spasinya sendiri. Jangan mengandalkan keanehan",
                    "    itu. Pakai trim() aja untuk semuanya.",
                    "  - Boolean.parseBoolean nggak pernah melempar exception. Apa pun selain",
                    "    kata \"true\" jadi false, dan besar kecilnya huruf diabaikan:",
                    "      Boolean.parseBoolean(\"TRUE\")  -> true",
                    "      Boolean.parseBoolean(\"Ya\")    -> false",
                    "    Baris kedua nggak error, tapi hasilnya salah tanpa peringatan. Ini",
                    "    lebih berbahaya daripada exception, karena exception setidaknya",
                    "    kelihatan.",
                    "",
                    "Angka jadi teks",
                    "",
                    "Ada tiga cara, dan semuanya benar:",
                    "  String.valueOf(x)     paling aman: null pun jadi \"null\", nggak error",
                    "  Integer.toString(x)   paling jelas maksudnya, tapi x wajib int",
                    "  \"\" + x                paling sering kamu temui di kode orang;",
                    "                        pendek, tapi menyamarkan bahwa di situ",
                    "                        sedang terjadi konversi",
                    "",
                    "Konstanta dan method pembungkus yang sering kepakai:",
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
                    "",
                    "Pada objek, operator == mengecek apakah dua variabel menunjuk objek yang",
                    "sama di memori. Isinya nggak dibandingkan. Aturan ini sama persis dengan",
                    "yang berlaku pada String.",
                    "",
                    "Java menyimpan cache Integer untuk nilai -128 sampai 127. Cache di sini",
                    "artinya simpanan objek yang dipakai ulang. Jadi dua Integer bernilai 127",
                    "menunjuk objek yang sama, dan == kebetulan true. Di luar rentang itu",
                    "objeknya dibikin baru, jadi == langsung false.",
                    "",
                    "Jebakan: kode yang diuji pakai angka kecil bakal lolos, lalu rusak",
                    "begitu angkanya membesar. Jadi bandingkan pembungkus selalu dengan",
                    ".equals(). Kalau memang mau pakai ==, ubah dulu ke primitif:",
                    "a.intValue() == b.intValue(). Satu-satunya == yang benar untuk",
                    "pembungkus adalah membandingkan dengan null, yaitu x == null.",
                    "",
                    "Kenapa unboxing null jadi NullPointerException?",
                    "",
                    "Baris int nilai = belumDiisi; diterjemahkan compiler jadi",
                    "belumDiisi.intValue(). Memanggil method pada null selalu menghasilkan",
                    "NullPointerException, yang sering disingkat NPE. Yang bikin ketipu, di",
                    "baris itu nggak kelihatan satu titik pun. Kasus ini sering muncul kalau",
                    "data datang dari database atau JSON yang kolomnya boleh kosong. Cek null",
                    "dulu, atau bungkus dengan Optional (dibahas di materi Optional & Null",
                    "Safety).",
                    "",
                    "Biaya tersembunyi autoboxing",
                    "",
                    "  Long total = 0L;",
                    "  for (int i = 0; i < 1000000; i++) { total += i; }",
                    "",
                    "Di setiap putaran, total dibuka jadi long, dijumlah, lalu dibungkus",
                    "lagi. Baris sependek itu bikin sejuta objek Long tanpa kelihatan. Ganti",
                    "tipenya jadi long primitif, dan semua pekerjaan tambahan itu hilang.",
                    "Hasilnya tetap sama, 499999500000.",
                    "",
                    "Aturan praktis memilih int atau Integer:",
                    "  - Pakai int, long, atau double untuk variabel lokal, penghitung loop,",
                    "    dan perhitungan. Ini pilihan bawaanmu. Jangan pakai pembungkus tanpa",
                    "    alasan.",
                    "  - Pakai Integer, Long, atau Double kalau nilainya boleh kosong (null),",
                    "    atau kalau harus masuk ke List, Map, Optional, atau generic.",
                    "  - Method yang mengembalikan Integer seolah bilang ke pemanggilnya",
                    "    \"hasilnya mungkin null\". Kalau hasilnya nggak pernah null,",
                    "    kembalikan int aja. Tanda tangan method, yaitu baris yang menyebut",
                    "    nama, parameter, dan tipe kembaliannya, ikut jadi dokumentasi buat",
                    "    orang yang membacanya nanti.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Data yang datang dari luar program hampir selalu berupa teks: isi form",
                    "pendaftaran, argumen baris perintah, kolom berkas CSV, atau hasil",
                    "pemindai barcode di kasir. Sebelum bisa dijumlah, teks itu harus diubah",
                    "jadi angka lewat Integer.parseInt dan teman-temannya.",
                    "",
                    "Kasus kecil: aplikasi kasir menerima harga dua barang dari pemindai",
                    "sebagai teks, yaitu \"3500\" dan \" 12000\" (ada spasi di depannya). Kamu",
                    "perlu totalnya sebagai angka.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tentukan masukan dan keluarannya: dua String masuk, satu int",
                    "     keluar.",
                    "  2. Jangan langsung dijumlah. \"3500\" + \" 12000\" menghasilkan teks",
                    "     \"3500 12000\", karena tanda + pada teks artinya menyambung.",
                    "  3. Pangkas spasinya dengan trim(), baru ubah dengan Integer.parseInt:",
                    "      String a = \"3500\", b = \" 12000\";",
                    "      int total = Integer.parseInt(a.trim()) + Integer.parseInt(b.trim());",
                    "      System.out.println(total);   // 15500",
                    "  4. Cek kasus pinggirnya: pemindai yang gagal membaca mengirim teks",
                    "     kosong. parseInt(\"\") melempar NumberFormatException, nggak",
                    "     mengembalikan 0. Tangkap exception-nya, lalu minta kasir memindai",
                    "     ulang.",
                    "",
                    "Jebakan: harga yang ditulis \"12.000\" juga ditolak. parseInt cuma",
                    "menerima digit, ditambah tanda plus atau minus di depan, jadi titik",
                    "ribuan bikin dia melempar NumberFormatException.",
                ]
            },
        ],
    },
    {
        "title": "5. Operator",
        "sections": [
            {
                "body": [
                    "Operator aritmatika dipakai untuk berhitung:",
                    "  +  penjumlahan      a + b",
                    "  -  pengurangan      a - b",
                    "  *  perkalian        a * b",
                    "  /  pembagian        a / b",
                    "  %  sisa bagi        a % b (modulus)",
                    "  ++ increment (naik 1)   -- decrement (turun 1)",
                    "",
                    "Hati-hati dengan pembagian:",
                    "  7 / 2   = 3    (int / int = int, sisa dibuang)",
                    "  7.0 / 2 = 3.5  (double / int = desimal)",
                    "  7 % 2   = 1    (sisa pembagian)",
                    "",
                    "Kalau dua angkanya bilangan bulat, hasilnya juga bilangan bulat. Sisanya",
                    "dibuang begitu aja, nggak dibulatkan. Begitu salah satu angkanya",
                    "desimal, hasilnya ikut desimal.",
                    "",
                    "Operator penugasan (assignment) dipakai untuk mengisi atau mengubah isi",
                    "variabel:",
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
                    "Tanda + punya tugas kedua: menyambung teks. Istilahnya konkatenasi.",
                    "Begitu salah satu sisinya String, + berhenti menjumlahkan dan mulai",
                    "menyambung.",
                    "",
                    "  \"Halo \" + \"Andi\"  ->  \"Halo Andi\"",
                    "  \"Umur: \" + 20      ->  \"Umur: 20\"    (20 diubah jadi teks dulu)",
                    "  \"Nilai \" + true    ->  \"Nilai true\"",
                    "",
                    "Kamu bakal sering banget nulis bentuk di bawah ini. Bentuk ini juga",
                    "muncul di hampir semua contoh sesudah materi ini:",
                    "",
                    "  System.out.println(\"Total: \" + total);",
                    "",
                    "Tanpa penyambung teks, kamu cuma bisa mencetak satu hal per baris.",
                    "",
                    "Tapi + dikerjakan dari kiri ke kanan, dan hasilnya kadang bikin kaget:",
                    "",
                    "  1 + 2 + \"x\"  ->  \"3x\"    (1+2 dijumlahkan dulu, baru ditempel)",
                    "  \"x\" + 1 + 2  ->  \"x12\"   (begitu kena String, sisanya cuma menempel)",
                    "",
                    "Jadi kalau mau menjumlahkan di tengah teks, pakai kurung:",
                    "",
                    "  System.out.println(\"Jumlah: \" + 10 + 5);     // Jumlah: 105   (salah)",
                    "  System.out.println(\"Jumlah: \" + (10 + 5));   // Jumlah: 15    (benar)",
                    "",
                    "Operator += juga berlaku untuk String, misalnya pesan += \" selesai\";.",
                    "Enak dipakai untuk beberapa baris. Tapi jangan dipakai di dalam loop",
                    "yang panjang. String nggak bisa diubah, jadi setiap += bikin String baru",
                    "di belakang layar. Untuk kebutuhan itu ada StringBuilder (lihat materi",
                    "String & Scanner).",
                    "",
                    "Jebakan: char itu bukan String. 'A' + 1 hasilnya 66, karena char",
                    "disimpan sebagai angka (kode huruf A adalah 65). Kalau mau dapat \"A1\",",
                    "tulis \"\" + 'A' + 1.",
                ]
            },
            {
                "body": [
                    "Operator perbandingan hasilnya selalu boolean, yaitu true atau false:",
                    "  ==  sama dengan      a == b",
                    "  !=  tidak sama       a != b",
                    "  >   lebih besar      a > b",
                    "  <   lebih kecil      a < b",
                    "  >=  lebih besar sama a >= b",
                    "  <=  lebih kecil sama a <= b",
                    "",
                    "Operator logika dipakai untuk menggabungkan beberapa kondisi:",
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
                    "Urutan prioritas operator, dari yang dikerjakan paling dulu:",
                    "  1. () ekspresi dalam kurung",
                    "  2. * / %",
                    "  3. + -",
                    "  4. perbandingan",
                    "  5. &&",
                    "  6. ||",
                    "",
                    "Kalau ragu, pakai kurung. Kodenya jadi lebih gampang dibaca, dan kamu",
                    "nggak perlu menghafal urutan ini.",
                ]
            },
            {
                "body": [
                    "Operator bit bekerja pada angka bit per bit, nggak pada nilainya secara",
                    "utuh. Bit adalah angka 0 atau 1 dalam bentuk biner. Di awal belajar kamu",
                    "jarang nulis operator ini sendiri. Tapi kamu bakal sering membacanya di",
                    "kode orang. Kalau belum kenal bentuknya, & kelihatan seperti && yang",
                    "kurang satu huruf.",
                    "",
                    "  &    DAN bit       5 & 3   ->  1    (0101 & 0011 = 0001)",
                    "  |    ATAU bit      5 | 3   ->  7    (0101 | 0011 = 0111)",
                    "  ^    XOR bit       5 ^ 3   ->  6    (beda -> 1, sama -> 0)",
                    "  ~    BALIK bit     ~5      -> -6",
                    "  <<   geser kiri    1 << 3  ->  8    (sama dengan dikali 2 sebanyak 3 kali)",
                    "  >>   geser kanan   -16 >> 2   -> -4   (tanda minus ikut terjaga)",
                    "  >>>  geser kanan tanpa tanda   -16 >>> 28  ->  15",
                    "",
                    "Semua operator ini juga punya bentuk gabungan:  &=  |=  ^=  <<=  >>=  >>>=",
                    "",
                    "Prioritas operator bit ada di bawah perbandingan. Jadi (izin & TULIS) !=",
                    "0 wajib pakai kurung.",
                    "",
                    "& dan | juga bisa dipakai pada boolean. Di sini bedanya dengan && dan ||",
                    "jadi penting. & dan | selalu mengerjakan kedua sisi. Sebaliknya, && dan",
                    "|| berhenti begitu jawabannya udah pasti. Sifat berhenti lebih awal ini",
                    "namanya short-circuit.",
                    "",
                    "  if (obj != null && obj.cek())   aman: obj.cek() tak dipanggil kalau null",
                    "  if (obj != null &  obj.cek())   error: sisi kanan tetap dijalankan",
                    "",
                    "Pemakaian yang paling sering kamu temui: menyimpan banyak saklar",
                    "hidup/mati di dalam satu angka. Istilahnya bit flag.",
                    "",
                    "  static final int BACA = 1, TULIS = 2, HAPUS = 4;   // 1, 10, 100 dalam biner",
                    "  int izin = BACA | HAPUS;                    // gabungkan  -> 5",
                    "  boolean bolehTulis = (izin & TULIS) != 0;   // periksa    -> false",
                    "  izin |= TULIS;                              // nyalakan   -> 7",
                    "  izin &= ~HAPUS;                             // matikan    -> 3",
                    "",
                    "Ada dua bentuk lain yang juga sering muncul. Pertama, x & 0xFF untuk",
                    "mengambil 8 bit terakhir sebuah angka (300 & 0xFF -> 44). Kedua, 1 << n",
                    "untuk bikin 2 pangkat n.",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aplikasi parkir mal, kasir, dan ojek online penuh dengan hitungan",
                    "kecil: total, kembalian, tarif per jam. Pembagian bulat dan sisa bagi",
                    "(%) muncul tiap kali satu satuan harus dipecah jadi satuan lain,",
                    "misalnya menit jadi jam, atau gram jadi kilogram.",
                    "",
                    "Kasus kecil: tarif parkir Rp3.000 per jam, dan sisa menit tetap",
                    "dihitung satu jam penuh. Sebuah mobil parkir 135 menit. Layar harus",
                    "menampilkan 2 jam 15 menit, dan tagihannya Rp9.000.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Masukannya satu angka, yaitu durasi dalam menit. Keluarannya tiga:",
                    "     jam, sisa menit, dan tarif.",
                    "  2. Pecah menit jadi jam pakai / dan %. Dua-duanya int, jadi pecahan",
                    "     jamnya langsung dibuang:",
                    "      int durasi = 135;",
                    "      int jam = durasi / 60, menit = durasi % 60;      // 2 dan 15",
                    "  3. Untuk pembulatan ke atas tanpa if, tambahkan 59 dulu sebelum",
                    "     dibagi 60:",
                    "      int jamDitagih = (durasi + 59) / 60;            // 3",
                    "      System.out.println(\"Bayar: \" + (jamDitagih * 3000));   // 9000",
                    "  4. Uji kasus pinggirnya: durasi 120 harus jadi 2 jam (179 / 60 = 2),",
                    "     dan durasi 121 harus jadi 3 jam (180 / 60 = 3).",
                    "",
                    "Jebakan: durasi / 60 * 3000 kelihatan benar, padahal sisa 15 menit ikut",
                    "terbuang dan pemilik parkir kehilangan tarif satu jam.",
                ]
            },
        ],
    },
    {
        "title": "6. Percabangan (if / switch)",
        "sections": [
            {
                "body": [
                    "Percabangan bikin program bisa mengambil keputusan. Kalau kondisinya",
                    "begini, kerjakan ini. Kalau nggak, kerjakan yang lain.",
                    "",
                    "Bentuk if, else if, dan else:",
                    "  if (kondisi) {",
                    "      // jalankan jika kondisi true",
                    "  } else if (kondisi2) {",
                    "      // jalankan jika kondisi2 true",
                    "  } else {",
                    "      // jalankan jika semua false",
                    "  }",
                    "",
                    "Kondisinya dicek dari atas ke bawah. Begitu ada yang true, bloknya",
                    "dijalankan dan sisanya dilewati. Kalau nggak ada satu pun yang true,",
                    "blok else yang jalan.",
                    "",
                    "Ingat: kondisinya harus bernilai boolean. Tulisan (x = 5) itu salah,",
                    "karena satu tanda = artinya mengisi nilai. Yang benar (x == 5).",
                    "",
                    "Ternary operator adalah if yang ditulis dalam satu baris:",
                    "  tipe nama = (kondisi) ? nilaiTrue : nilaiFalse;",
                    "  String hasil = (nilai >= 75) ? \"Lulus\" : \"Tidak Lulus\";",
                    "",
                    "Cara bacanya: kalau nilai >= 75, hasil diisi \"Lulus\". Kalau nggak, hasil",
                    "diisi \"Tidak Lulus\".",
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
                    "switch dipakai untuk membandingkan satu nilai dengan banyak pilihan sekaligus:",
                    "",
                    "  switch (ekspresi) {",
                    "      case nilai1:",
                    "          // kode",
                    "          break;",
                    "      case nilai2:",
                    "          // kode",
                    "          break;",
                    "      default:",
                    "          // jika tidak ada yang cocok",
                    "  }",
                    "",
                    "Mulai Java 14 ada switch expression yang lebih ringkas:",
                    "  String hasil = switch (hari) {",
                    "      case 1 -> \"Senin\";",
                    "      case 2 -> \"Selasa\";",
                    "      default -> \"Lainnya\";",
                    "  };",
                    "",
                    "Jebakan: di switch bentuk lama, break itu penting. Tanpa break, semua",
                    "case di bawahnya ikut dijalankan walaupun nilainya nggak cocok. Kejadian",
                    "ini disebut fall-through. Switch bentuk panah (->) nggak punya masalah",
                    "ini.",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Hampir setiap aturan bisnis ditulis sebagai percabangan: ongkir",
                    "tergantung berat, predikat rapor tergantung nilai, harga tiket",
                    "tergantung umur. Yang paling sering salah di sini urutan kondisinya dan",
                    "angka di batasnya.",
                    "",
                    "Kasus kecil: kolam renang kota memasang tarif begini. Anak di bawah 5",
                    "tahun gratis, umur 5 sampai 12 Rp15.000, umur 13 sampai 59 Rp25.000,",
                    "dan umur 60 ke atas Rp15.000.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Masukannya umur (int), keluarannya harga (int). Tulis dulu",
                    "     rentangnya di kertas, lengkap dengan angka batasnya.",
                    "  2. Urutkan kondisinya dari umur terkecil. Java memeriksa dari atas dan",
                    "     berhenti di kondisi pertama yang true, jadi tiap cabang cukup",
                    "     menulis batas atasnya:",
                    "      int harga;",
                    "      if (umur < 5) harga = 0;",
                    "      else if (umur <= 12) harga = 15000;",
                    "      else if (umur < 60) harga = 25000;",
                    "      else harga = 15000;",
                    "  3. Uji tepat di batasnya: 4, 5, 12, 13, 59, dan 60. Salah pilih < dan",
                    "     <= hampir selalu ketahuan di angka-angka ini.",
                    "",
                    "Jebakan: kalau umur < 60 diperiksa paling atas, anak 3 tahun ikut bayar",
                    "Rp25.000. Kondisi itu udah true duluan, jadi cabang gratis nggak pernah",
                    "tercapai.",
                ]
            },
        ],
    },
    {
        "title": "7. Perulangan (Loop)",
        "sections": [
            {
                "body": [
                    "Perulangan, atau loop, menjalankan kode yang sama berulang-ulang. Java",
                    "punya tiga bentuk:",
                    "  1. for, dipakai kalau jumlah perulangannya udah diketahui.",
                    "       for (awal; kondisi; update) {",
                    "           // kode diulang",
                    "       }",
                    "  2. while, dipakai kalau jumlahnya belum pasti. Kondisinya dicek dulu",
                    "     sebelum kodenya jalan.",
                    "       while (kondisi) {",
                    "           // kode",
                    "       }",
                    "  3. do-while. Kodenya dijalankan dulu, baru kondisinya dicek. Jadi",
                    "     kodenya pasti jalan minimal sekali.",
                    "       do {",
                    "           // kode (pasti jalan minimal 1x)",
                    "       } while (kondisi);",
                    "",
                    "Ada dua kata kunci tambahan:",
                    "  - break menghentikan perulangan saat itu juga.",
                    "  - continue melewati putaran (iterasi) yang sedang berjalan, lalu",
                    "    lanjut ke putaran berikutnya.",
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
                    "Perulangan bersarang (nested loop) artinya ada perulangan di dalam",
                    "perulangan. Bentuk ini sering dipakai untuk bikin pola bintang atau",
                    "tabel.",
                    "",
                    "Contohnya pola segitiga bintang:",
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
                    "Loop luar mengatur baris. Loop dalam mencetak bintang sebanyak nomor",
                    "barisnya: baris 1 satu bintang, baris 2 dua bintang, dan seterusnya.",
                    "",
                    "For-each (enhanced for) dipakai untuk membaca semua elemen array atau",
                    "koleksi satu per satu, tanpa perlu indeks:",
                    "  for (int elemen : array) { ... }",
                    "  for (String nama : daftarNama) { ... }",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Perulangan muncul di mana pun ada pekerjaan yang diulang sampai beres.",
                    "Contohnya mencetak tiap baris struk, menghitung cicilan bulan demi",
                    "bulan, atau menampilkan menu kasir lagi sampai kasir memilih keluar.",
                    "Kalau jumlah putarannya belum ketahuan dari awal, yang dipakai while.",
                    "",
                    "Kasus kecil: saldo tabungan Dina Rp120.000. Tiap minggu dia menabung",
                    "Rp50.000, dan dia mau beli sepatu seharga Rp1.000.000. Berapa minggu",
                    "lagi uangnya cukup?",
                    "",
                    "Cara memecahkannya:",
                    "  1. Masukannya saldo awal, setoran, dan target. Keluarannya jumlah",
                    "     minggu.",
                    "  2. Jumlah minggunya belum ketahuan, jadi pakai while dengan syarat",
                    "     \"saldo masih kurang\":",
                    "      int saldo = 120000, minggu = 0;",
                    "      while (saldo < 1000000) {",
                    "          saldo += 50000;",
                    "          minggu++;",
                    "      }",
                    "      System.out.println(minggu + \" minggu\");   // 18 minggu",
                    "  3. Cocokkan dengan hitungan kasar: kurangnya Rp880.000, dibagi",
                    "     Rp50.000 jadi 17,6, dibulatkan ke atas jadi 18.",
                    "  4. Uji kasus pinggirnya: kalau saldo awal udah Rp1.000.000, loop-nya",
                    "     nggak jalan sama sekali dan hasilnya 0 minggu. Dengan do-while,",
                    "     hasilnya malah 1, dan itu salah.",
                    "",
                    "Jebakan: kalau baris saldo += 50000 lupa ditulis, syaratnya nggak",
                    "pernah berubah dan loop-nya berputar terus tanpa henti.",
                ]
            },
        ],
    },
    {
        "title": "8. Array",
        "sections": [
            {
                "body": [
                    "Array adalah kumpulan data bertipe sama dengan ukuran tetap. Begitu",
                    "dibikin dengan ukuran 5, isinya selalu 5 slot.",
                    "",
                    "Cara mendeklarasikan array:",
                    "  int[] angka = new int[5];          // array 5 int, isi default 0",
                    "  int[] angka = {1, 2, 3, 4, 5};     // langsung dengan nilai",
                    "  String[] nama = {\"Andi\", \"Budi\"};",
                    "",
                    "Elemen array diambil lewat indeks, yaitu nomor urut slotnya. Indeks",
                    "array dimulai dari 0:",
                    "  int[] angka = {10, 20, 30};",
                    "  angka[0] -> 10",
                    "  angka[1] -> 20",
                    "  angka[2] -> 30",
                    "",
                    "Panjang array bisa dilihat lewat .length:",
                    "  angka.length  -> 3",
                    "",
                    "Jebakan: indeks di luar batas bikin error",
                    "ArrayIndexOutOfBoundsException. Array di atas cuma punya indeks 0 sampai",
                    "2, jadi indeks 3 langsung error:",
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
                    "Array 2 dimensi (matriks) adalah array yang isinya array lagi. Bayangkan",
                    "tabel yang punya baris dan kolom:",
                    "  int[][] matriks = {",
                    "      {1, 2, 3},",
                    "      {4, 5, 6}",
                    "  };",
                    "  matriks[0][1] -> 2 (baris 0, kolom 1)",
                    "",
                    "Untuk membaca semuanya, pakai dua for-each. Yang luar mengambil tiap",
                    "baris, yang dalam mengambil tiap angka di baris itu:",
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
                    "Kalau butuh array yang ukurannya bisa berubah (dinamis), pakai",
                    "ArrayList. Untuk memakainya kamu perlu import java.util.ArrayList;.",
                    "Detailnya dibahas di materi Collection Framework.",
                ]
            },
            {
                "body": [
                    "Ini jebakan pemula yang paling terkenal di Java. Karena bukan error,",
                    "nggak ada yang ngasih peringatan:",
                    "",
                    "  int[] nilai = {80, 90, 75, 85};",
                    "  System.out.println(nilai);      ->  [I@1b6d3586",
                    "",
                    "Hasil ini nggak rusak dan nggak kebetulan. Array nggak punya cara",
                    "mencetak isinya sendiri. Jadi yang keluar adalah tipenya ([I artinya",
                    "\"array of int\") ditambah sebuah angka heksadesimal. Angka itu sering",
                    "disebut alamat memori, walaupun aslinya kode hash objek. Yang penting,",
                    "angkanya bisa berubah tiap kali program dijalankan.",
                    "",
                    "Solusinya satu baris: Arrays.toString(nilai).",
                    "",
                    "Arrays adalah kelas utilitas di java.util. Isinya method static untuk",
                    "mengolah array. Di kode sungguhan, array hampir selalu diproses lewat",
                    "class ini, jarang lewat loop manual seperti contoh tadi.",
                    "",
                    "  import java.util.Arrays;",
                    "",
                    "  Arrays.toString(arr)           ubah jadi teks yang terbaca",
                    "  Arrays.deepToString(arr2d)     sama, untuk array di dalam array",
                    "  Arrays.sort(arr)               urutkan di tempat (array aslinya berubah!)",
                    "  Arrays.fill(arr, nilai)        isi semua slot dengan nilai yang sama",
                    "  Arrays.copyOf(arr, n)          salinan sepanjang n (kelebihannya diisi 0)",
                    "  Arrays.copyOfRange(arr, a, b)  potong indeks a sampai sebelum b",
                    "  Arrays.equals(a, b)            bandingkan isi; == cuma bandingkan alamat",
                    "  Arrays.binarySearch(arr, x)    cari cepat, tapi hanya di array terurut",
                    "  Arrays.asList(a, b, c)         jadikan List berukuran tetap (add ditolak)",
                    "  System.arraycopy(...)          salin sepotong array ke array lain",
                    "",
                    "Tiga hal yang paling sering bikin salah:",
                    "  1. Arrays.sort mengubah array yang kamu kasih, dan nggak mengembalikan",
                    "     apa pun. Kalau urutan aslinya masih dibutuhkan, salin dulu pakai",
                    "     copyOf.",
                    "  2. Arrays.binarySearch ngasih angka ngawur, tanpa error, kalau",
                    "     arraynya belum terurut.",
                    "  3. Arrays.asList menghasilkan List yang panjangnya terkunci. set()",
                    "     boleh, tapi add() dan remove() melempar",
                    "     UnsupportedOperationException.",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Array cocok untuk data yang jumlahnya tetap: omzet tujuh hari dalam",
                    "seminggu, nilai dua belas bulan, atau denah kursi bioskop yang berbaris",
                    "dan berkolom. Pekerjaan paling umum pada array adalah mencari: yang",
                    "terbesar, yang terkecil, atau posisi sebuah nilai.",
                    "",
                    "Kasus kecil: pemilik warung mencatat omzet seminggu dari Senin sampai",
                    "Minggu: 320000, 275000, 410000, 0, 390000, 520000, 610000. Hari Kamis",
                    "warungnya tutup. Dia mau tahu hari buka yang paling sepi.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Masukannya dua array sejajar, hari dan omzet, dengan indeks yang",
                    "     sama untuk hari yang sama. Keluarannya nama hari dan angkanya.",
                    "  2. Anggap dulu hari pertama yang paling sepi, lalu bandingkan dengan",
                    "     hari-hari sesudahnya satu per satu.",
                    "  3. Lewati omzet 0, karena itu hari tutup:",
                    "      int iMin = 0;",
                    "      for (int i = 1; i < omzet.length; i++) {",
                    "          if (omzet[i] == 0) continue;",
                    "          if (omzet[i] < omzet[iMin]) iMin = i;",
                    "      }",
                    "      System.out.println(hari[iMin] + \": \" + omzet[iMin]);   // Selasa",
                    "  4. Pikirkan kasus pinggir yang tersisa. Kalau dua hari sama-sama",
                    "     paling sepi, tanda < memilih yang pertama. Kalau justru hari",
                    "     pertama yang tutup, titik awalnya ikut salah, jadi mulailah dari",
                    "     hari buka pertama.",
                    "",
                    "Jebakan: System.out.println(omzet) mencetak sesuatu seperti [I@66d3c617,",
                    "bukan isinya. Pakai Arrays.toString(omzet) waktu mau memeriksa datanya.",
                ]
            },
        ],
    },
    {
        "title": "9. Method (Fungsi)",
        "sections": [
            {
                "body": [
                    "Method adalah blok kode yang dikasih nama, supaya bisa dipanggil",
                    "berulang-ulang. Daripada menulis kode yang sama di lima tempat, kamu",
                    "tulis sekali di dalam method, lalu panggil namanya di lima tempat itu.",
                    "",
                    "Bentuk umum method:",
                    "  tipeKembali namaMethod(parameter) {",
                    "      // isi method",
                    "      return nilai;   // jika tipeKembali bukan void",
                    "  }",
                    "",
                    "tipeKembali adalah jenis nilai yang dikirim balik oleh method lewat",
                    "return. Kalau method-nya nggak mengembalikan apa-apa, tulis void di",
                    "situ.",
                    "",
                    "Contoh deklarasi:",
                    "  int tambah(int a, int b) {",
                    "      return a + b;",
                    "  }",
                    "  void sapa(String nama) {",
                    "      System.out.println(\"Halo, \" + nama);",
                    "  }",
                    "",
                    "Cara memanggil method:",
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
                    "Method overloading",
                    "",
                    "Overloading artinya beberapa method punya nama yang sama, tapi",
                    "parameternya beda. Java memilih method yang cocok dari jumlah dan tipe",
                    "argumen yang kamu kirim:",
                    "",
                    "  int tambah(int a, int b) { return a + b; }",
                    "  int tambah(int a, int b, int c) { return a + b + c; }",
                    "  double tambah(double a, double b) { return a + b; }",
                    "",
                    "  tambah(1, 2)        -> memanggil yang 2 param",
                    "  tambah(1, 2, 3)     -> memanggil yang 3 param",
                    "  tambah(1.5, 2.5)    -> memanggil yang double",
                    "",
                    "Scope variabel",
                    "",
                    "Scope artinya wilayah tempat sebuah variabel dikenal.",
                    "  - Variabel yang dibuat di dalam method cuma dikenal di method itu.",
                    "    Istilahnya variabel lokal.",
                    "  - Karena itu, nama variabel yang sama boleh dipakai di method yang berbeda.",
                    "  - Parameter method juga termasuk variabel lokal.",
                    "",
                    "Method static",
                    "  - Method static dipanggil langsung, tanpa bikin objek. Contohnya",
                    "    Math.pow(2, 3).",
                    "  - Method yang nggak static butuh objek dulu, misalnya",
                    "    kalkulator.tambah(1, 2).",
                ]
            },
            {
                "body": [
                    "Varargs",
                    "",
                    "Varargs adalah parameter yang jumlah argumennya bebas. Tanda tiga titik",
                    "sesudah tipe artinya \"nol atau lebih nilai bertipe ini\".",
                    "",
                    "  static void tulis(String... bagian) { ... }",
                    "",
                    "  tulis();                    // boleh, tanpa argumen sama sekali",
                    "  tulis(\"a\");",
                    "  tulis(\"a\", \"b\", \"c\");",
                    "",
                    "Di dalam method, bagian bentuknya array biasa. Jadi bagian.length dan",
                    "for-each jalan persis seperti di materi Array. Java yang membungkus",
                    "argumen-argumenmu jadi array.",
                    "",
                    "Ada dua aturan:",
                    "  1. Varargs wajib jadi parameter terakhir. Di depannya boleh ada",
                    "     parameter biasa:",
                    "       static void tulis(String pemisah, String... bagian)",
                    "  2. Satu method cuma boleh punya satu varargs.",
                    "",
                    "Kamu bakal sering ketemu varargs di method bawaan Java:",
                    "  List.of(5, 3, 8)                     varargs",
                    "  String.format(\"%s umur %d\", a, b)    varargs",
                    "  System.out.printf(...)               varargs",
                    "",
                    "Makanya jumlah argumen ketiganya boleh berubah-ubah, padahal method",
                    "biasa harus dipanggil dengan jumlah argumen yang pas. Jadi kalau nanti",
                    "kamu lihat tiga titik di daftar parameter kode orang, itu bukan salah",
                    "ketik.",
                ]
            },
            {
                "body": [
                    "Class Math",
                    "",
                    "Math adalah contoh paling jelas dari method static, karena semua isinya",
                    "method static. Kamu nggak pernah nulis new Math(). Cukup",
                    "Math.sesuatu(...). Math tinggal di java.lang, jadi nggak perlu import.",
                    "",
                    "  Math.abs(-9)      ->  9        nilai mutlak",
                    "  Math.max(3, 8)    ->  8        yang terbesar dari dua",
                    "  Math.min(3, 8)    ->  3        yang terkecil dari dua",
                    "  Math.round(2.5)   ->  3        bulatkan ke yang terdekat",
                    "  Math.ceil(4.1)    ->  5.0      bulatkan ke atas",
                    "  Math.floor(4.9)   ->  4.0      bulatkan ke bawah",
                    "  Math.sqrt(144)    ->  12.0     akar kuadrat",
                    "  Math.pow(2, 10)   ->  1024.0   pangkat",
                    "  Math.random()     ->  0.0 sampai di bawah 1.0, acak tiap panggilan",
                    "  Math.PI           ->  3.141592653589793  (konstanta, bukan method)",
                    "",
                    "Perhatikan tipe kembaliannya, karena bagian ini yang paling sering bikin",
                    "bingung. pow, sqrt, ceil, dan floor selalu menghasilkan double. Jadi",
                    "Math.pow(2, 3) hasilnya 8.0, bukan 8. Math.round menghasilkan long kalau",
                    "masukannya double, dan int kalau masukannya float.",
                    "",
                    "Math.round berguna kalau angka hasil hitunganmu kepanjangan:",
                    "",
                    "  double luas = Math.PI * 7 * 7;",
                    "  System.out.println(luas);               // 153.93804002589985",
                    "  System.out.println(Math.round(luas));   // 154",
                    "",
                    "Kalau yang kamu mau dua angka di belakang koma, pakai format teks,",
                    "jangan Math (lihat materi String & Scanner).",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Di aplikasi kantin sekolah, harga sesudah diskon dihitung di tiga",
                    "tempat: layar kasir, struk, dan laporan harian. Kalau rumusnya disalin",
                    "ke tiga tempat, suatu hari satu salinan diubah dan dua lainnya",
                    "terlupa. Method menaruh rumus itu di satu tempat yang punya nama.",
                    "",
                    "Kasus kecil: kantin memberi diskon persen untuk menu tertentu. Nasi",
                    "goreng Rp20.000 dengan diskon 15% harus jadi Rp17.000. Pecahan rupiah",
                    "dibuang, jadi es teh Rp2.550 dengan diskon yang sama jadi Rp2.168.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Jadikan masukannya parameter (harga dan persen, dua-duanya int),",
                    "     dan keluarannya tipe kembali (int).",
                    "  2. Kasih nama yang menyebut apa yang dihasilkan, misalnya",
                    "     hargaSetelahDiskon.",
                    "  3. Tulis badannya, lalu uji dengan angka yang kamu tahu jawabannya:",
                    "      static int hargaSetelahDiskon(int harga, int persen) {",
                    "          return harga - harga * persen / 100;",
                    "      }",
                    "      // hargaSetelahDiskon(20000, 15) -> 17000",
                    "  4. Cek kasus pinggirnya: persen 0 harus mengembalikan harga utuh, dan",
                    "     es teh Rp2.550 harus jadi 2168.",
                    "",
                    "Jebakan: harga / 100 * persen kelihatan sama, padahal pembagian int-nya",
                    "jalan duluan. Untuk Rp2.550 hasilnya 2175, selisih tujuh rupiah dari",
                    "rumus yang benar.",
                ]
            },
        ],
    },
    {
        "title": "10. Rekursi",
        "sections": [
            {
                "body": [
                    "Rekursi artinya method yang di dalam badannya memanggil dirinya sendiri.",
                    "Sekilas kedengarannya kayak putaran tanpa ujung. Nggak akan begitu, asal",
                    "setiap pemanggilan mengerjakan versi soal yang lebih kecil dari",
                    "sebelumnya.",
                    "",
                    "Perumpamaannya antrean. Kamu pengin tahu kamu orang ke berapa. Kamu",
                    "tanya orang di depanmu, \"Kamu nomor berapa?\" Dia juga nggak tahu, jadi",
                    "dia tanya orang di depannya. Begitu terus sampai orang paling depan",
                    "menjawab, \"Aku nomor 1.\" Jawaban itu lalu mengalir balik ke belakang,",
                    "dan tiap orang menambah 1. Nggak ada satu orang pun yang tahu jawaban",
                    "lengkapnya. Tiap orang cuma tahu \"nomorku = nomor orang di depanku + 1\".",
                    "",
                    "Rekursi butuh dua syarat. Kalau salah satunya hilang, rekursinya pasti rusak:",
                    "  1. Base case: kondisi yang langsung punya jawaban, tanpa memanggil",
                    "     dirinya lagi.",
                    "  2. Langkah mengecil: tiap pemanggilan makin dekat ke base case.",
                    "",
                    "Contohnya faktorial: 4! = 4 x 3 x 2 x 1 = 24. Rumusnya sendiri udah rekursif:",
                    "  faktorial(n) = n * faktorial(n - 1)     dan     faktorial(1) = 1",
                    "",
                    "Coba telusuri pelan-pelan. Pertama turun dulu. Soalnya dipecah, tapi",
                    "jawabannya belum ada:",
                    "  faktorial(4) = 4 * faktorial(3)       <- ditahan, menunggu jawaban",
                    "    faktorial(3) = 3 * faktorial(2)     <- ditahan juga",
                    "      faktorial(2) = 2 * faktorial(1)   <- ditahan juga",
                    "        faktorial(1) = 1                <- base case, ada jawaban!",
                    "",
                    "Lalu naik. Jawabannya dikembalikan, dan pemanggilan yang tadi ditahan",
                    "bisa selesai:",
                    "      faktorial(2) = 2 * 1 = 2",
                    "    faktorial(3) = 3 * 2 = 6",
                    "  faktorial(4) = 4 * 6 = 24",
                    "",
                    "Waktu faktorial(1) dijawab, ada tiga pemanggilan lain yang masih",
                    "menunggu. Masing-masing memegang nilai n-nya sendiri. Keempatnya",
                    "betul-betul ada di memori pada saat yang sama.",
                    "",
                    "Pola yang sama bisa dipakai untuk menjumlahkan 1 sampai n:",
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
                    "Call stack",
                    "",
                    "Call stack adalah tumpukan pemanggilan method yang belum selesai.",
                    "",
                    "Setiap kali sebuah method dipanggil, Java menyiapkan satu \"kotak\" di",
                    "memori. Isinya parameter dan variabel lokal method itu. Kotak ini",
                    "ditaruh di atas kotak milik pemanggilnya. Kotak paling atas adalah",
                    "method yang sedang jalan. Begitu method itu selesai (return), kotaknya",
                    "dibuang. Method di bawahnya lalu lanjut tepat dari baris tempat dia tadi",
                    "berhenti.",
                    "",
                    "Ini berlaku untuk semua method, nggak cuma yang rekursif. Bedanya, pada",
                    "rekursi tumpukannya berisi method yang itu-itu juga. Bisa sepuluh atau",
                    "seribu kotak dari method yang sama, masing-masing dengan nilai n",
                    "sendiri.",
                    "",
                    "Ukuran tumpukan itu terbatas. Di kebanyakan komputer 64-bit besarnya",
                    "sekitar 1 MB, dan bisa disetel lewat opsi -Xss. Untuk method sederhana,",
                    "itu kira-kira cukup untuk sepuluh ribuan tingkat pemanggilan. Lewat dari",
                    "itu, Java melempar StackOverflowError.",
                    "",
                    "Bug rekursi yang paling sering terjadi adalah base case yang nggak",
                    "pernah kena:",
                    "",
                    "  static int hitungMundur(int n) {",
                    "      if (n == 0) return 0;",
                    "      return n + hitungMundur(n - 2);   // LOMPAT DUA",
                    "  }",
                    "",
                    "hitungMundur(5) nggak pernah menyentuh 0: 5, 3, 1, -1, -3, -5, dan",
                    "seterusnya. Base case-nya ada dan ditulis dengan benar, tapi langkahnya",
                    "melompatinya. Itu yang bikin bug ini susah dilihat. Nggak ada satu baris",
                    "pun yang salah. Yang salah adalah hubungan antara base case dan",
                    "langkahnya. Perbaikannya: ganti kondisinya jadi n <= 0, atau turun",
                    "satu-satu.",
                    "",
                    "Kalau program itu dijalankan, yang muncul di layar:",
                    "",
                    "  Exception in thread \"main\" java.lang.StackOverflowError",
                    "      at Rusak.hitungMundur(Rusak.java:8)",
                    "      at Rusak.hitungMundur(Rusak.java:8)",
                    "      at Rusak.hitungMundur(Rusak.java:8)",
                    "      ... baris yang sama terulang lebih dari seribu kali",
                    "",
                    "Pesan seperti itu namanya stack trace, dan isinya ya tumpukan tadi.",
                    "Bacanya dari atas ke bawah. Baris paling atas adalah tempat error",
                    "terjadi, dan baris paling bawah biasanya main(). Kalau satu baris yang",
                    "sama terulang puluhan sampai ribuan kali, hampir pasti itu rekursi yang",
                    "base case-nya nggak pernah tercapai. Buka nomor baris yang disebut, lalu",
                    "cek dua hal aja: base case-nya ada atau nggak, dan langkahnya",
                    "betul-betul mengecil ke arah base case itu atau nggak.",
                    "",
                    "Jebakan: StackOverflowError itu termasuk Error, beda dengan Exception",
                    "biasa (lihat materi Exception Handling). Jangan ditangkap pakai",
                    "try-catch. Yang bermasalah kodenya, bukan datanya. Menangkap error ini",
                    "cuma menyembunyikan bug yang tetap ada di sana.",
                ],
            },
            {
                "heading": "Fibonacci naif dan Fibonacci yang mengingat",
                "body": [
                    "Fibonacci adalah deret 0, 1, 1, 2, 3, 5, 8, 13, 21, dan seterusnya. Tiap",
                    "angka adalah jumlah dua angka sebelumnya. Rumusnya rekursif, dan kali",
                    "ini ada dua cabang:",
                    "  fib(n) = fib(n - 1) + fib(n - 2),   fib(0) = 0,   fib(1) = 1",
                    "",
                    "Versi paling polosnya benar, tapi lambat. Alasannya kelihatan di sini:",
                    "  fib(5) memanggil fib(4) dan fib(3)",
                    "  fib(4) memanggil fib(3) dan fib(2)   <- fib(3) dihitung ULANG",
                    "  makin dalam, makin banyak pekerjaan yang persis sama diulang",
                    "",
                    "Program di bawah menghitung sendiri berapa kali method-nya dipanggil.",
                    "Untuk n = 20, jumlahnya 21.891 panggilan, cuma untuk dapat satu angka,",
                    "yaitu 6765.",
                    "",
                    "Solusinya sederhana. Simpan hasil yang udah pernah dihitung, lalu cek",
                    "catatan itu sebelum menghitung ulang. Teknik ini namanya memoization.",
                    "Dengan catatan, n = 20 selesai dalam 39 panggilan. Rekursinya nggak",
                    "diganti sama sekali. Bedanya cuma satu: pekerjaan yang sama nggak",
                    "dikerjakan berulang kali.",
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
                    "Rekursi atau perulangan?",
                    "",
                    "Rekursi dan perulangan bisa saling menggantikan. Contohnya ini:",
                    "",
                    "  static int jumlahLoop(int n) {",
                    "      int total = 0;",
                    "      for (int i = 1; i <= n; i++) total += i;",
                    "      return total;",
                    "  }",
                    "",
                    "Versi loop ini mengerjakan hal yang sama persis dengan jumlah(n)",
                    "rekursif tadi. Bedanya, versi loop lebih cepat dan nggak bisa kena",
                    "StackOverflowError. Untuk soal yang jalannya lurus, loop hampir selalu",
                    "pilihan yang lebih baik. Contoh soal yang lurus: 1 sampai n, isi array",
                    "dari depan ke belakang, atau baca berkas baris demi baris. Kalau soal",
                    "begitu ditulis rekursif, kodenya cuma kelihatan pintar tanpa jadi lebih",
                    "jelas.",
                    "",
                    "Rekursi unggul kalau datanya bercabang dan kedalamannya nggak diketahui.",
                    "Misalnya folder di dalam folder, elemen HTML di dalam elemen HTML, nilai",
                    "JSON di dalam nilai JSON, atau komentar yang punya balasan, dan",
                    "balasannya punya balasan lagi. Aturannya cuma \"kerjakan hal yang sama",
                    "untuk tiap anak\", dan aturan itu harus bisa masuk lagi sedalam apa pun.",
                    "",
                    "Loop biasa nggak punya tempat untuk mengingat \"tadi aku lagi di mana\"",
                    "waktu dia turun satu tingkat. Jadi kamu terpaksa bikin tumpukan sendiri.",
                    "Padahal pekerjaan itu udah dikerjakan call stack secara gratis.",
                    "",
                    "Pohon folder di bawah ditulis pakai array, supaya belum perlu class",
                    "(lihat materi Array). Sesudah belajar Class & Object, kamu bakal",
                    "menulisnya sebagai objek yang punya daftar anak. Bentuk rekursinya tetap",
                    "sama persis.",
                    "",
                    "Perhatikan juga base case di method total(). Di sana nggak ada satu if",
                    "pun. Folder yang nggak punya anak bikin for-each-nya nggak jalan sama",
                    "sekali, jadi method itu langsung return. Base case boleh berupa keadaan",
                    "seperti itu, nggak harus kondisi yang ditulis terang-terangan.",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Data yang bercabang dan kedalamannya nggak ketahuan ada di banyak",
                    "aplikasi: kategori produk toko online (Elektronik, lalu HP, lalu",
                    "Aksesoris HP), struktur organisasi sekolah, atau komentar yang saling",
                    "berbalas. Menghitung sesuatu di data seperti itu paling enak ditulis",
                    "rekursif.",
                    "",
                    "Kasus kecil: toko online menyimpan kategori dalam tiga array, persis",
                    "seperti contoh folder di materi ini. Elektronik punya 5 produk langsung,",
                    "HP 40, Aksesoris HP 120, dan Laptop 30. HP dan Laptop ada di bawah",
                    "Elektronik, Aksesoris HP di bawah HP. Halaman Elektronik harus",
                    "menampilkan total produknya.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Masukannya indeks satu kategori. Keluarannya jumlah produk di",
                    "     kategori itu beserta semua turunannya.",
                    "  2. Rumuskan dengan kalimat dulu: total sebuah kategori sama dengan",
                    "     produknya sendiri ditambah total tiap anaknya.",
                    "  3. Base case-nya kategori tanpa anak. Loop-nya nggak jalan, jadi",
                    "     method langsung mengembalikan produknya sendiri:",
                    "      static int total(int i) {",
                    "          int jumlah = produk[i];",
                    "          for (int a : anak[i]) jumlah += total(a);",
                    "          return jumlah;",
                    "      }",
                    "  4. Hitung dengan tangan: 5 + (40 + 120) + 30 = 195. Program yang",
                    "     benar harus mengeluarkan angka yang sama.",
                    "",
                    "Jebakan: kalau data kategorinya keliru dan sebuah kategori tercatat",
                    "sebagai anak dari cucunya sendiri, rekursinya berputar sampai",
                    "StackOverflowError. Perbaiki datanya, jangan tangkap error-nya.",
                ]
            },
        ],
    },
    {
        "title": "11. OOP: Class & Object",
        "sections": [
            {
                "body": [
                    "OOP singkatan dari Object-Oriented Programming. Di gaya pemrograman ini,",
                    "data dan perilaku digabung jadi satu di dalam objek.",
                    "",
                    "Dua istilah yang perlu kamu pegang:",
                    "  - Class adalah cetakan (blueprint).",
                    "  - Object adalah hasil cetakan dari class itu. Nama lainnya instance.",
                    "",
                    "Perumpamaannya begini. Class itu resep kue, dan object itu kue cokelat",
                    "yang jadi dari resep itu. Satu resep bisa dipakai untuk bikin banyak",
                    "kue.",
                    "",
                    "Isi sebuah class:",
                    "  1. Attribute atau field: datanya, misalnya nama dan umur.",
                    "  2. Constructor: method khusus yang jalan waktu objek dibuat.",
                    "  3. Method: perilakunya, misalnya berjalan atau bicara.",
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
                    "Penjelasan kodenya:",
                    "  new Mahasiswa(...)",
                    "    Membuat objek baru.",
                    "  this.nama",
                    "    Menunjuk attribute nama milik objek, bukan parameter nama.",
                    "  m1, m2",
                    "    Variabel referensi, yaitu variabel yang menunjuk ke sebuah objek.",
                    "",
                    "Kata kunci penting:",
                    "  this  -> merujuk ke objek saat ini.",
                    "  new   -> membuat objek baru dari sebuah class.",
                    "  null  -> referensi yang belum menunjuk objek apa pun.",
                    "",
                    "Access modifier menentukan siapa aja yang boleh memakai sebuah attribute",
                    "atau method:",
                    "  public    -> bisa diakses dari mana saja.",
                    "  private   -> hanya bisa diakses di dalam class yang sama.",
                    "  protected -> class yang sama + subclass + package sama.",
                    "  (tanpa)   -> package-private, hanya package sama.",
                    "",
                    "Aturan umumnya: attribute dibikin private, method dibikin public. Konsep",
                    "ini namanya Encapsulation, dan dibahas di materi Encapsulation.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aplikasi ojek online punya objek pengemudi, penumpang, dan order.",
                    "Aplikasi kasir punya objek barang. Tiap objek membawa datanya sendiri,",
                    "jadi nama, harga, dan stok satu barang selalu pergi bersama dan nggak",
                    "tercecer di tiga variabel terpisah.",
                    "",
                    "Kasus kecil: kasir menyimpan data barang di tiga array, yaitu nama[],",
                    "harga[], dan stok[]. Suatu hari seseorang mengurutkan array harga, dan",
                    "sejak itu harga Gula 1 kg nyangkut di nama Minyak Goreng.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Kumpulkan data yang selalu ikut bersama. Nama, harga, dan stok",
                    "     milik satu barang, jadi ketiganya jadi field satu class.",
                    "  2. Cari perilaku yang memakai data itu, misalnya menghitung nilai stok",
                    "     (harga dikali stok). Perilaku itu jadi method.",
                    "  3. Isi datanya lewat constructor waktu objek dibuat:",
                    "      class Barang {",
                    "          String nama;",
                    "          int harga, stok;",
                    "          Barang(String n, int h, int s) { nama = n; harga = h; stok = s; }",
                    "          int nilaiStok() { return harga * stok; }",
                    "      }",
                    "  4. Uji satu objek: new Barang(\"Gula 1 kg\", 17500, 40).nilaiStok()",
                    "     harus menghasilkan 700000.",
                    "",
                    "Jebakan: Barang b2 = b1; nggak bikin barang baru. Dua variabel itu",
                    "menunjuk objek yang sama, jadi mengubah b2.stok ikut mengubah b1.stok.",
                ]
            },
        ],
    },
    {
        "title": "12. Anggota Class: Constructor, static, dan Konstanta",
        "sections": [
            {
                "body": [
                    "Di materi Class & Object kamu udah nyalin baris seperti ini tanpa penjelasan:",
                    "  Mahasiswa(String nama, int umur) { ... }",
                    "",
                    "Itu namanya constructor, yaitu bagian class yang dijalankan waktu objek",
                    "dibuat. Ada tiga aturan yang wajib diikuti, dan melanggarnya nggak",
                    "selalu memunculkan error:",
                    "  1. Namanya harus persis sama dengan nama class, termasuk huruf",
                    "     besar-kecilnya.",
                    "  2. Nggak punya tipe kembali. Bukan int, bukan String, void pun nggak.",
                    "  3. Dijalankan otomatis tepat sekali, saat kata new dijalankan.",
                    "",
                    "Jebakan: kalau aturan nomor 2 dilanggar, compiler diam aja.",
                    "",
                    "  class Mahasiswa {",
                    "      String nama;",
                    "      void Mahasiswa(String nama) {   // ada void -> BUKAN constructor",
                    "          this.nama = nama;",
                    "      }",
                    "  }",
                    "",
                    "Kode itu sah, tapi sebagai method biasa yang kebetulan bernama",
                    "Mahasiswa. new nggak pernah memanggilnya. Programnya tetap jalan, nama",
                    "tetap null, dan nggak ada pesan error apa pun yang menunjuk ke sini.",
                    "",
                    "Constructor default",
                    "",
                    "Kalau kamu nggak menulis constructor sama sekali, Java otomatis",
                    "menambahkan satu constructor kosong: Mahasiswa() { }. Begitu kamu",
                    "menulis satu constructor sendiri, constructor kosong itu nggak",
                    "ditambahkan lagi.",
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
                    "Makanya error ini sering muncul di kode yang kemarin masih jalan.",
                    "Seseorang menambah constructor berparameter, lalu semua new Mahasiswa()",
                    "di berkas lain ikut gagal. Solusinya jangan menghapus constructor yang",
                    "baru. Tulis lagi constructor kosongnya kalau memang masih dipakai.",
                    "",
                    "Overloading constructor dan this(...)",
                    "",
                    "Satu class boleh punya banyak constructor, asal daftar parameternya",
                    "beda. Aturannya sama persis dengan method overloading di materi Method.",
                    "Supaya isinya nggak disalin berulang-ulang, constructor yang pendek",
                    "memanggil constructor yang lengkap lewat this(...):",
                    "",
                    "  public Kotak() { this(1, 1); }",
                    "",
                    "Dua hal soal this(...):",
                    "  - this(...) wajib jadi baris pertama di dalam constructor. Kalau",
                    "    nggak, muncul error:",
                    "      error: call to this must be first statement in constructor",
                    "  - Jangan tertukar dengan this.lebar. Pakai titik artinya field milik",
                    "    objek ini. Pakai kurung artinya memanggil constructor lain.",
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
                    "Satu hal lagi soal constructor, supaya kamu nggak kaget di materi",
                    "Inheritance. Kalau baris pertama sebuah constructor bukan this(...) dan",
                    "bukan super(...), Java otomatis menyisipkan super(); di situ, tanpa",
                    "kecuali. super(...) artinya memanggil constructor class induk. Alasannya",
                    "masuk akal: bagian induk dari objek harus jadi lebih dulu.",
                    "",
                    "Akibatnya, kalau class induk nggak punya constructor tanpa argumen,",
                    "class anak wajib memanggil super(...) sendiri. Kalau lupa, muncul error",
                    "ini:",
                    "",
                    "  error: constructor Hewan in class Hewan cannot be applied to given types;",
                    "  class Kucing extends Hewan {",
                    "",
                    "Perhatikan: yang disebut Hewan, tapi baris yang ditunjuk ada di Kucing.",
                    "Sebagian IDE menulis pesannya dengan kalimat lain, misalnya 'there is no",
                    "default constructor available in Hewan'. Artinya sama aja.",
                    "",
                    "Field static dan field instance",
                    "",
                    "  Field instance (tanpa static) -> tiap objek punya salinan sendiri.",
                    "  Field static                  -> satu nilai, dipakai bersama semua objek.",
                    "",
                    "Objek dibuat dari cetakan, yaitu class-nya. Field static menempel di",
                    "cetakannya, nggak di hasil cetakan. Field static udah ada sebelum objek",
                    "pertama dibuat, dan tetap ada sesudah semua objek dibuang. Makanya",
                    "penghitung \"udah berapa objek yang pernah dibuat\" cuma bisa ditulis",
                    "sebagai field static.",
                    "",
                    "Konstanta: static + final",
                    "",
                    "  private static final double PPN = 0.11;",
                    "  public  static final int    KURSI_MAKS = 40;",
                    "",
                    "  static -> menempel di class, tidak disalin ke tiap objek.",
                    "  final  -> tidak bisa diisi ulang setelah nilainya masuk.",
                    "  Konvensi namanya HURUF_BESAR dipisah garis bawah.",
                    "",
                    "Ini bentuk baku konstanta di kode sungguhan. Variabel final di dalam",
                    "method, seperti yang kamu lihat sebelumnya, cuma berlaku selama method",
                    "itu jalan.",
                    "",
                    "Pola yang sama juga menjelaskan baris yang nongkrong di atas hampir",
                    "setiap class di proyek besar:",
                    "",
                    "  private static final Logger log = LoggerFactory.getLogger(Pesanan.class);",
                    "",
                    "Artinya, satu objek pencatat (logger) dibuat sekali untuk seluruh class.",
                    "private supaya nggak dipakai class lain, final supaya nggak ada yang",
                    "menggantinya.",
                    "",
                    "Blok inisialisasi static",
                    "",
                    "  static { ... }",
                    "",
                    "Blok ini dijalankan sekali, waktu class-nya pertama kali dipakai. Kalau",
                    "class itu yang punya main, blok ini jalan sebelum main. Kamu jarang",
                    "menulisnya sendiri, tapi kenali bentuknya supaya nggak bingung waktu",
                    "ketemu. Blok ini bukan method dan nggak punya nama.",
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
                    "Dari keluaran itu kelihatan dua hal:",
                    "  - 'Loket dibuka.' muncul paling atas, padahal blok static ditulis di",
                    "    tengah class. Itu bukti blok static jalan sebelum main.",
                    "  - jumlahTerjual bisa sampai 2 karena kedua objek menaikkan angka yang",
                    "    sama. Kalau kata static-nya dihapus, tiap tiket punya penghitung",
                    "    sendiri yang isinya selalu 1.",
                    "",
                    "Error static yang bikin hampir semua pemula mentok",
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
                    "Alasannya masuk akal kalau dibaca pelan-pelan. main itu static, jadi dia",
                    "jalan tanpa objek apa pun. Sedangkan sapa() milik objek. Java nggak tahu",
                    "objek yang mana yang harus menyapa.",
                    "",
                    "Ada dua cara membetulkannya, tergantung maksudmu:",
                    "  1. Bikin objeknya dulu: new Main().sapa();",
                    "  2. Jadikan method-nya static juga: static void sapa() { ... }",
                    "",
                    "Pilih cara 1 kalau method itu memakai field instance. Pilih cara 2 kalau",
                    "method itu cuma mengolah parameternya sendiri.",
                    "",
                    "Aturan yang sama berlaku untuk field, dengan pesan error yang mirip:",
                    "",
                    "  error: non-static variable umur cannot be referenced from a static context",
                    "",
                    "Method static nggak boleh menyentuh field instance maupun this. Waktu",
                    "method static jalan, belum tentu ada objek yang bisa disentuh.",
                    "Sebaliknya boleh: method instance bebas memakai field static.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Nomor antrean puskesmas, nomor faktur toko, dan nomor tiket bioskop",
                    "punya kebutuhan yang sama. Semuanya butuh satu penghitung yang dipakai",
                    "bersama semua objek, supaya nomornya nggak pernah kembar. Penghitung",
                    "itu field static, dan awalan yang nggak boleh berubah seperti \"A-\" jadi",
                    "konstanta static final.",
                    "",
                    "Kasus kecil: loket pendaftaran puskesmas membuat satu objek Pasien",
                    "untuk tiap orang yang datang. Tiap pasien harus dapat nomor berurutan:",
                    "A-1, A-2, A-3, dan seterusnya.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pisahkan data milik tiap pasien (nama, nomor antrean) dari data",
                    "     milik bersama (nomor terakhir yang udah dipakai).",
                    "  2. Data milik tiap pasien jadi field instance. Penghitungnya jadi",
                    "     field static, karena cuma boleh ada satu.",
                    "  3. Constructor menaikkan penghitung, lalu memakai angkanya:",
                    "      class Pasien {",
                    "          static final String AWALAN = \"A-\";",
                    "          static int terakhir = 0;",
                    "          final String nomor;",
                    "          Pasien() { terakhir++; nomor = AWALAN + terakhir; }",
                    "      }",
                    "  4. Uji dengan tiga pasien. Nomornya harus A-1, A-2, A-3. Kalau",
                    "     ketiganya A-1, berarti kata static di penghitungnya terhapus.",
                    "",
                    "Ingat: field static cuma hidup selama programnya jalan. Begitu program",
                    "ditutup, penghitungnya mulai dari 0 lagi. Menyimpan nomor terakhir",
                    "secara permanen itu urusan berkas atau database di materi-materi akhir.",
                ]
            },
        ],
    },
    {
        "title": "13. Enum: Himpunan Nilai Tetap",
        "sections": [
            {
                "body": [
                    "Enum adalah daftar pilihan yang jumlahnya tetap dan udah diketahui waktu",
                    "kode ditulis. Contohnya status akun, hari dalam seminggu, level",
                    "pengguna, jenis pembayaran, atau arah mata angin.",
                    "",
                    "Sebelum ada enum, orang menulis pilihan seperti itu sebagai angka atau teks:",
                    "  int status = 1;              // 1 itu aktif atau nonaktif? tebak sendiri",
                    "  String status = \"AKTIF\";",
                    "",
                    "Dua cara itu punya masalah yang sama: compiler nggak tahu nilai mana yang sah.",
                    "  status = 99;                 // lolos kompilasi, kacau saat program jalan",
                    "  status = \"aktip\";            // salah ketik, lolos kompilasi, salah",
                    "",
                    "Dengan enum, nilai ngawur udah ditolak waktu kompilasi. Kesalahannya",
                    "ketahuan sebelum programnya dipakai orang:",
                    "  Status status = Status.AKTIF;",
                    "  status = 99;                 // error: incompatible types",
                    "",
                    "Bentuk paling sederhananya, di berkas Status.java:",
                    "  public enum Status { AKTIF, NONAKTIF, DIBLOKIR }",
                    "",
                    "Isinya ditulis huruf besar semua karena tiap nama itu konstanta. Di",
                    "belakang layar, Java mengubahnya jadi `public static final Status AKTIF",
                    "= ...`. Konvensi Java untuk static final memang HURUF_BESAR.",
                    "",
                    "Akibat terpentingnya: satu konstanta berarti satu objek, dan objek itu",
                    "dibuat sekali oleh JVM. Kamu nggak pernah nulis `new Status(...)`,",
                    "karena memang nggak diizinkan. Karena objeknya cuma satu, `==` aman",
                    "dipakai untuk membandingkan enum. Ini kebalikan dari String, yang wajib",
                    "pakai .equals() (dibahas di materi String & Scanner). Pada enum, `==`",
                    "malah lebih aman: nggak melempar NullPointerException walaupun",
                    "variabelnya null.",
                    "",
                    "Enum itu class khusus. Semua yang udah kamu pelajari soal field,",
                    "constructor, dan method tetap berlaku di sini. Bedanya cuma satu: daftar",
                    "objeknya udah ditentukan dari awal.",
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
                    "Dari program itu kelihatan:",
                    "  - Enum dipakai persis seperti tipe lain: jadi tipe field, tipe",
                    "    parameter, dan tipe kembalian method.",
                    "  - `b.status == Status.DIBLOKIR` aman, karena tiap konstanta cuma satu objek.",
                    "",
                    "Di dalam switch, enum ditulis `case AKTIF`, tanpa `Status.` di depannya.",
                    "switch udah tahu tipenya dari ekspresi di dalam kurung, jadi menyebut",
                    "nama enum di tiap case cuma pengulangan. Di Java 17 dan sebelumnya,",
                    "menulis `case Status.AKTIF` malah bikin error kompilasi. Java 21 mulai",
                    "mengizinkannya, tapi bentuk pendek tetap yang paling umum. Soal break",
                    "dan fall-through di bentuk klasik, lihat materi Percabangan. Bentuk",
                    "panah nggak punya fall-through, jadi nggak perlu break.",
                    "",
                    "Switch bentuk panah yang dipakai sebagai ekspresi, seperti di",
                    "batasUnggah, punya satu kelebihan. Kalau semua konstanta udah dicakup,",
                    "`default` boleh dihilangkan. Lalu suatu hari ada yang menambah konstanta",
                    "baru ke enum-nya. Compiler langsung menunjuk setiap switch yang belum",
                    "menanganinya. Kalau ada `default`, konstanta baru itu masuk ke cabang",
                    "default tanpa peringatan, dan bug-nya baru ketahuan dari laporan",
                    "pemakai.",
                    "",
                    "Method bawaan yang dimiliki semua enum tanpa perlu ditulis:",
                    "  values()           array berisi semua konstanta, urut sesuai deklarasi",
                    "  valueOf(\"AKTIF\")   teks -> konstanta; harus persis, peka huruf besar-kecil",
                    "  name()             nama konstanta sebagai String (\"AKTIF\")",
                    "  ordinal()          posisi konstanta, mulai dari 0",
                    "  toString()         bawaannya sama dengan name(); println() mencetak nama",
                    "  compareTo()        membandingkan berdasarkan ordinal, jadi enum bisa di-sort",
                    "",
                    "Jebakan: teks yang nggak cocok bikin valueOf() melempar",
                    "IllegalArgumentException. Dia nggak mengembalikan null. Data yang datang",
                    "dari berkas, form web, atau database harus dibungkus try-catch atau",
                    "dicek dulu. Cara membungkusnya dibahas di materi Exception Handling.",
                    "",
                    "Jebakan: jangan pernah menyimpan ordinal() ke database atau berkas.",
                    "Angka itu cuma cerminan urutan kamu mengetik. Kalau ada konstanta baru",
                    "disisipkan di tengah daftar, semua nomor sesudahnya bergeser. Akibatnya",
                    "semua data lama berubah arti tanpa satu pun pesan error. Simpan name()",
                    "sebagai teks, atau simpan field kode buatanmu sendiri seperti contoh",
                    "berikut.",
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
                    "Enum yang punya constructor adalah bentuk yang paling sering kamu temui",
                    "di kode sungguhan:",
                    "  - Nilai di dalam kurung, misalnya `HEMAT(\"Hemat\", 10)`, adalah argumen",
                    "    untuk constructor-nya.",
                    "  - Constructor enum selalu private. Kalau kamu nulis `public` di situ,",
                    "    hasilnya error. Masuk akal, karena nggak ada yang boleh bikin",
                    "    konstanta baru selain enum itu sendiri.",
                    "  - Constructor-nya jalan sekali untuk tiap konstanta, waktu enum-nya",
                    "    pertama kali dipakai.",
                    "  - Field dibikin `private final` supaya nilainya nggak bisa diubah dari luar.",
                    "  - Titik koma sesudah konstanta terakhir wajib ditulis kalau di",
                    "    bawahnya ada field, constructor, atau method. Lupa titik koma ini",
                    "    termasuk error enum yang paling sering.",
                    "",
                    "Kalau tiap konstanta butuh method dengan isi yang beda, deklarasikan",
                    "method `abstract` di enum-nya. Lalu tiap konstanta membawa blok { }",
                    "berisi versinya sendiri. Cara ini menggantikan switch panjang yang harus",
                    "diedit tiap kali ada konstanta baru. Di sini compiler menolak konstanta",
                    "yang lupa mengisi method abstraknya.",
                    "",
                    "Enum boleh `implements` interface, tapi nggak boleh `extends` class. Di",
                    "belakang layar, enum udah mewarisi java.lang.Enum, dan Java cuma",
                    "mengizinkan satu induk.",
                    "",
                    "EnumMap dan EnumSet (dari java.util) sebaiknya dipakai kalau kuncinya",
                    "enum, ketimbang HashMap atau HashSet:",
                    "  - EnumMap disimpan sebagai array sepanjang jumlah konstanta, dengan",
                    "    ordinal sebagai indeksnya. Nggak ada hashing dan nggak ada tabrakan,",
                    "    jadi lebih hemat memori dan lebih cepat.",
                    "  - Urutan isinya selalu sesuai urutan deklarasi. HashMap nggak",
                    "    menjanjikan urutan apa pun.",
                    "  - EnumSet menyimpan anggotanya sebagai bit. Untuk enum sampai 64",
                    "    konstanta, semuanya muat di dalam satu long, jadi gabungan dan",
                    "    irisan himpunan cuma operasi bit. EnumSet.allOf(Paket.class),",
                    "    EnumSet.noneOf(...), dan EnumSet.range(...) juga sering dipakai.",
                    "",
                    "Enum di dalam class, seperti `Pesanan.Status`, cocok kalau enum-nya cuma",
                    "bermakna bersama class itu. Di dalam Pesanan cukup ditulis `Status`.",
                    "Dari luar ditulis `Pesanan.Status`, dan konstantanya",
                    "`Pesanan.Status.SELESAI`.",
                    "",
                    "Ringkasan jebakan:",
                    "  - `case Status.AKTIF` di dalam switch error di Java 17 ke bawah. Tulis",
                    "    `case AKTIF` aja.",
                    "  - valueOf() melempar IllegalArgumentException, nggak mengembalikan null.",
                    "  - Jangan simpan ordinal() secara permanen. Simpan name() atau kode",
                    "    buatan sendiri.",
                    "  - Jangan lupa titik koma sesudah konstanta terakhir kalau enum punya",
                    "    isi tambahan.",
                    "  - Enum nggak bisa di-`new` dan nggak bisa `extends` class lain.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Toko online punya pilihan yang jumlahnya tetap di banyak tempat: status",
                    "pesanan, metode pembayaran, dan jenis layanan kirim. Kalau pilihan itu",
                    "ditulis sebagai teks biasa, salah ketik seperti \"kilt\" baru ketahuan",
                    "waktu ada paket yang nyasar. Dengan enum, compiler yang menolaknya.",
                    "",
                    "Kasus kecil: toko punya dua layanan kirim. Reguler tarifnya Rp9.000 per",
                    "kg dan sampai dalam 3 hari. Kilat tarifnya Rp15.000 per kg dan sampai",
                    "besok. Halaman checkout butuh ongkir dan perkiraan lamanya.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pilihannya tetap dan udah ketahuan waktu kode ditulis, jadi pakai",
                    "     enum.",
                    "  2. Tiap pilihan membawa data sendiri, yaitu tarif dan lama kirim.",
                    "     Simpan sebagai field, lalu isi lewat constructor enum.",
                    "  3. Hitungan ongkir jadi method di enum itu sendiri:",
                    "      enum Layanan {",
                    "          REGULER(9000, 3), KILAT(15000, 1);",
                    "          final int tarifPerKg, hari;",
                    "          Layanan(int t, int h) { tarifPerKg = t; hari = h; }",
                    "          int ongkir(int kg) { return tarifPerKg * kg; }",
                    "      }",
                    "  4. Uji ongkir Kilat untuk 2 kg, hasilnya harus 30000. Lalu cek kasus",
                    "     pinggirnya: pilihan dari form web datang sebagai teks huruf kecil,",
                    "     dan valueOf(\"kilat\") melempar IllegalArgumentException. Ubah dulu",
                    "     teksnya jadi huruf besar semua sebelum memanggil valueOf.",
                    "",
                    "Jebakan: waktu menyimpan pilihan pembeli ke database, simpan name(),",
                    "jangan ordinal(). Kalau suatu hari ada layanan baru yang disisipkan di",
                    "tengah daftar, nomor urutnya bergeser dan pesanan lama berubah layanan.",
                ]
            },
        ],
    },
    {
        "title": "14. OOP: Encapsulation",
        "sections": [
            {
                "body": [
                    "Encapsulation artinya menyembunyikan data di dalam objek, lalu memberi",
                    "akses yang terkontrol lewat method. Method itu biasanya disebut getter",
                    "(untuk membaca) dan setter (untuk mengubah).",
                    "",
                    "Manfaatnya:",
                    "  1. Data aman dari perubahan sembarangan.",
                    "  2. Kamu bisa menambahkan validasi, yaitu pengecekan apakah nilai baru",
                    "     masuk akal.",
                    "  3. Kodenya lebih gampang dirawat.",
                    "",
                    "Cara membuatnya:",
                    "  1. Jadikan attribute-nya private.",
                    "  2. Sediakan getter untuk membaca.",
                    "  3. Sediakan setter untuk mengubah, lengkap dengan validasinya.",
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
                    "Perhatikan contoh tadi:",
                    "  - saldo nggak bisa diubah sembarangan dari luar, karena private.",
                    "  - Semua perubahan harus lewat setor() atau tarik(), dan dua method itu",
                    "    mengecek jumlahnya dulu.",
                    "  - Hasilnya, saldo nggak mungkin jadi negatif.",
                    "",
                    "Keuntungan getter dan setter:",
                    "  - Kamu bisa menambah logika di dalamnya, misalnya validasi atau",
                    "    logging (mencatat kejadian).",
                    "  - Isi class bisa diubah tanpa mengubah kode yang memakainya.",
                    "  - Ada format nama yang standar: getNama() dan setNama(String nama).",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Saldo dompet digital, stok gudang, dan nilai rapor punya aturan yang",
                    "nggak boleh dilanggar. Saldo nggak boleh minus, stok nggak boleh kurang",
                    "dari nol, dan nilai harus di antara 0 sampai 100. Encapsulation",
                    "memastikan data itu cuma bisa diubah lewat method yang ngecek",
                    "aturannya.",
                    "",
                    "Kasus kecil: laporan gudang menunjukkan stok sabun -5. Ternyata ada",
                    "kode di bagian penjualan yang langsung menulis barang.stok -= 10,",
                    "padahal stoknya tinggal 5.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tulis aturannya dulu: jumlah yang diambil harus lebih dari 0, dan",
                    "     nggak boleh melebihi stok.",
                    "  2. Jadikan field stok private, supaya baris seperti barang.stok -= 10",
                    "     ditolak compiler di mana pun dia ditulis.",
                    "  3. Sediakan satu method yang ngecek aturan itu sebelum mengubah stok:",
                    "      private int stok;",
                    "      public boolean ambil(int jumlah) {",
                    "          if (jumlah <= 0 || jumlah > stok) return false;",
                    "          stok -= jumlah;",
                    "          return true;",
                    "      }",
                    "  4. Uji kasus pinggirnya: ambil(5) saat stok 5 harus berhasil dan",
                    "     stoknya jadi 0. ambil(-3) harus ditolak, karena tanpa cek itu stok",
                    "     malah bertambah.",
                    "",
                    "Jebakan: menambah setter polos setStok(int stok) tanpa validasi membuka",
                    "lagi celah yang barusan kamu tutup.",
                ]
            },
        ],
    },
    {
        "title": "15. OOP: Inheritance (Pewarisan)",
        "sections": [
            {
                "body": [
                    "Inheritance (pewarisan) artinya sebuah class mewarisi attribute dan",
                    "method dari class lain.",
                    "  - Class yang mewariskan disebut induk, atau parent, atau superclass.",
                    "  - Class yang mewarisi disebut anak, atau child, atau subclass.",
                    "  - Kata kuncinya extends.",
                    "  - Class anak boleh menambah attribute atau method baru. Dia juga boleh",
                    "    menulis ulang method induknya. Istilahnya override.",
                    "",
                    "  class Hewan { ... }",
                    "  class Kucing extends Hewan { ... }",
                    "",
                    "Keuntungannya:",
                    "  - Kode yang sama nggak perlu ditulis berulang-ulang.",
                    "  - Kode lebih tertata dan gampang dirawat.",
                    "",
                    "Kata kunci super dipakai untuk menunjuk member class induk:",
                    "  - super()        -> memanggil constructor induk.",
                    "  - super.method() -> memanggil method induk.",
                    "",
                    "Untuk override, tulis ulang method induk di class anak, dan kasih tanda",
                    "@Override di atasnya.",
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
                    "Konsep \"is-a\" (adalah sebuah):",
                    "  - Kucing adalah sebuah Hewan. Kalimat itu benar, jadi Kucing boleh",
                    "    mewarisi Hewan.",
                    "  - Hati-hati dengan hubungan yang aneh. \"Mobil adalah sebuah Mesin\" itu",
                    "    salah, jadi Mobil nggak seharusnya mewarisi Mesin.",
                    "",
                    "Kata kunci final punya tiga arti:",
                    "  - final class: class itu nggak bisa diwarisi.",
                    "  - final method: method itu nggak bisa di-override.",
                    "  - final variabel: isinya nggak bisa diubah.",
                    "",
                    "Java nggak mendukung multiple inheritance antar class. Artinya, satu",
                    "class cuma bisa extends satu induk. Solusinya pakai interface, yang",
                    "dibahas di materi Abstract & Interface.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aplikasi penggajian punya karyawan tetap dan karyawan harian. Keduanya",
                    "punya nama dan cara dipanggil yang sama, tapi rumus gajinya beda.",
                    "Inheritance menaruh bagian yang sama di class induk, dan tiap anak cuma",
                    "menulis bagian yang beda.",
                    "",
                    "Kasus kecil: karyawan harian dibayar Rp120.000 per hari masuk, dan",
                    "bulan ini Pak Joko masuk 22 hari. Class induk Karyawan udah punya field",
                    "nama, constructor Karyawan(String nama), dan method gaji().",
                    "",
                    "Cara memecahkannya:",
                    "  1. Uji hubungannya dengan kalimat \"Harian adalah sebuah Karyawan\".",
                    "     Kalimat itu benar, jadi Harian boleh extends Karyawan.",
                    "  2. Cari yang beda dari induknya: upah per hari dan jumlah hari masuk.",
                    "     Keduanya jadi field baru di class anak.",
                    "  3. Tulis ulang gaji() dengan @Override, dan teruskan nama ke",
                    "     constructor induk lewat super:",
                    "      class Harian extends Karyawan {",
                    "          int upah = 120000, hariMasuk = 22;",
                    "          Harian(String nama) { super(nama); }",
                    "          @Override int gaji() { return upah * hariMasuk; }",
                    "      }",
                    "  4. Uji hasilnya: new Harian(\"Pak Joko\").gaji() harus 2640000.",
                    "",
                    "Jebakan: kalau baris super(nama) dihapus, compiler menolak dengan pesan",
                    "constructor Karyawan in class Karyawan cannot be applied to given",
                    "types. Induknya nggak punya constructor tanpa argumen, jadi super();",
                    "yang disisipkan Java nggak bisa dipakai.",
                ]
            },
        ],
    },
    {
        "title": "16. OOP: Polymorphism",
        "sections": [
            {
                "body": [
                    "Polymorphism artinya \"banyak bentuk\". Satu panggilan method yang sama",
                    "bisa berperilaku beda, tergantung class asli objeknya.",
                    "",
                    "Ada dua jenis:",
                    "  1. Compile-time, lewat method overloading. Nama method-nya sama,",
                    "     parameternya beda. Ini udah dibahas di materi Method.",
                    "  2. Runtime, lewat method overriding. Method induk ditulis ulang oleh",
                    "     anak, dan versi yang dipanggil mengikuti objek aslinya.",
                    "",
                    "Kunci polymorphism ada di sini: variabel bertipe class induk boleh",
                    "menampung objek anak.",
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
                    "Kenapa ini berguna? Kamu bisa menulis satu method yang menerima tipe",
                    "induk, dan method itu otomatis jalan untuk semua turunannya:",
                    "",
                    "  void panggil(Hewan h) {",
                    "      h.bersuara();",
                    "  }",
                    "  panggil(new Kucing());  // Meow!",
                    "  panggil(new Anjing());  // Guk!",
                    "",
                    "Upcasting artinya anak diperlakukan sebagai induk. Ini terjadi otomatis:",
                    "  Hewan h = new Kucing();",
                    "",
                    "Downcasting artinya induk dipaksa jadi anak. Ini harus ditulis manual",
                    "pakai cast, yaitu nama tipe di dalam kurung:",
                    "  Kucing k = (Kucing) h;   // wajib cast",
                    "",
                    "Supaya aman, cek dulu pakai instanceof.",
                ]
            },
            {
                "body": [
                    "instanceof adalah alat pengecek yang barusan disebut sekilas.",
                    "",
                    "  objek instanceof Tipe",
                    "",
                    "Hasilnya boolean: true kalau objeknya memang bertipe itu atau",
                    "turunannya. Karena hasilnya boolean biasa, dia boleh dipakai di mana pun",
                    "boolean boleh dipakai, nggak harus langsung di dalam if:",
                    "  boolean iniKucing = h instanceof Kucing;",
                    "",
                    "Ada dua sifat yang membantu:",
                    "  1. null instanceof apa pun selalu false, dan nggak pernah melempar",
                    "     NullPointerException. Jadi kamu nggak perlu ngecek null dulu.",
                    "  2. Perbandingan yang mustahil langsung ditolak compiler. Misalnya kamu",
                    "     nulis teks instanceof Integer untuk variabel String. Compiler",
                    "     berhenti dengan pesan:",
                    "       error: incompatible types: String cannot be converted to Integer",
                    "",
                    "Kenapa harus dicek? Downcasting yang salah nggak ditolak compiler.",
                    "Kesalahannya baru muncul waktu program udah jalan:",
                    "",
                    "  Hewan h = new Anjing();",
                    "  Kucing k = (Kucing) h;",
                    "",
                    "  Exception in thread \"main\" java.lang.ClassCastException:",
                    "      class Anjing cannot be cast to class Kucing",
                    "",
                    "Jadi pola amannya selalu berpasangan: cek dulu, baru cast.",
                    "",
                    "  if (h instanceof Kucing) {",
                    "      Kucing k = (Kucing) h;",
                    "      k.mengeong();",
                    "  }",
                    "",
                    "Sejak Java 16, dua langkah itu boleh disatukan. Namanya pattern matching:",
                    "  if (h instanceof Kucing k) { k.mengeong(); }",
                    "",
                    "Pengecekan dan cast jadi satu, dan k cuma ada di dalam blok yang udah",
                    "pasti Kucing. Bentuk ini sekarang dipakai di mana-mana, termasuk di",
                    "dalam equals() hampir setiap class. Aturan lengkapnya dibahas di materi",
                    "Record & Sintaks Java Modern. Untuk sekarang, cukup tahu bahwa dua",
                    "bentuk itu artinya sama.",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Kasir toko menerima pembayaran tunai, transfer bank, dan dompet",
                    "digital. Kode kasir cukup memanggil satu method, misalnya biayaAdmin(),",
                    "dan tiap jenis pembayaran menjawab dengan aturannya sendiri. Jenis baru",
                    "bisa ditambah tanpa menyentuh loop di kasir.",
                    "",
                    "Kasus kecil: hari ini ada tiga pembayaran, yaitu satu tunai dan dua",
                    "transfer. Tunai nggak kena biaya admin, transfer kena Rp2.500. Laporan",
                    "harian butuh total biaya adminnya.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Cari yang sama dari semua jenis pembayaran: semuanya punya biaya",
                    "     admin. Jadikan method di class induk Pembayaran.",
                    "  2. Tiap anak (Tunai, Transfer) meng-override method itu dengan",
                    "     angkanya sendiri.",
                    "  3. Simpan semuanya di array bertipe induk, lalu panggil method yang",
                    "     sama. Java memilih versi milik objek aslinya:",
                    "      Pembayaran[] hariIni = { new Tunai(), new Transfer(), new Transfer() };",
                    "      int totalAdmin = 0;",
                    "      for (Pembayaran p : hariIni) {",
                    "          totalAdmin += p.biayaAdmin();",
                    "      }",
                    "      // totalAdmin = 5000",
                    "  4. Cek kasus pinggirnya: kalau cuma Transfer yang punya data tambahan",
                    "     seperti nomor rekening, periksa dulu pakai instanceof sebelum cast.",
                    "     Cast objek Tunai ke Transfer melempar ClassCastException.",
                    "",
                    "Ingat: menambah DompetDigital cukup dengan satu class anak baru. Loop di",
                    "atas nggak perlu diubah sama sekali.",
                ]
            },
        ],
    },
    {
        "title": "17. Class Object: toString, equals, dan hashCode",
        "sections": [
            {
                "body": [
                    "Ada satu class yang nggak pernah kamu tulis, tapi selalu ikut:",
                    "java.lang.Object. Semua class di Java adalah turunannya, termasuk class",
                    "yang nggak menulis extends apa pun.",
                    "",
                    "  class Titik { }        // yang dibaca compiler: class Titik extends Object",
                    "",
                    "Artinya, setiap objek udah punya beberapa method sebelum kamu mengetik",
                    "satu baris pun:",
                    "  toString()      -> wujud teks objek; dipakai tiap kali objek dicetak.",
                    "  equals(Object)  -> apakah objek ini dianggap sama dengan objek lain?",
                    "  hashCode()      -> satu int wakil objek; dipakai HashSet dan HashMap.",
                    "  getClass()      -> class asli objek, diketahui saat program berjalan.",
                    "  clone(), finalize(), wait(), notify(), notifyAll() -> jarang ditulis.",
                    "",
                    "Karena itu juga, variabel bertipe Object bisa menampung apa aja:",
                    "  Object apa = \"halo\";   // String pun turunan Object.",
                    "",
                    "Kenapa System.out.println(objek) mencetak Titik@1b6d3586? println nggak",
                    "punya trik khusus. Dia cuma memanggil objek.toString(), lalu mencetak",
                    "hasilnya. Penggabungan \"Titik: \" + objek juga begitu.",
                    "",
                    "toString() bawaan Object isinya kira-kira begini:",
                    "  getClass().getName() + \"@\" + Integer.toHexString(hashCode())",
                    "",
                    "Jadi yang kamu lihat adalah nama class ditambah hashCode dalam",
                    "heksadesimal. Angka itu berubah tiap program dijalankan ulang, dan nggak",
                    "ngasih tahu apa pun soal isi objeknya.",
                    "",
                    "Tiga method pertama punya perilaku bawaan yang hampir nggak pernah",
                    "sesuai maumu. Materi ini membahas cara mengganti ketiganya, dan kenapa",
                    "dua di antaranya wajib ditulis berpasangan.",
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
                    "Ada tiga hal yang perlu diperbaiki dari contoh di atas.",
                    "",
                    "Perbaikan pertama, toString(). Tulis isi yang pengin kamu lihat waktu",
                    "debugging dan logging:",
                    "  @Override",
                    "  public String toString() { return \"Titik(\" + x + \", \" + y + \")\"; }",
                    "",
                    "@Override itu ada gunanya. Kalau nama atau parameter method-nya salah",
                    "ketik, compiler langsung menolak. Tanpa @Override, Java diam aja dan",
                    "menganggapnya method baru yang nggak pernah dipanggil siapa pun.",
                    "",
                    "Perbaikan kedua, equals(). Versi bawaan Object isinya persis 'this ==",
                    "lain'. Artinya dia cuma ngecek apakah dua variabel menunjuk objek yang",
                    "sama. Dua objek yang datanya identik tetap dianggap beda, karena memang",
                    "dua objek. String terasa lain (lihat materi String & Scanner) cuma",
                    "karena String udah meng-override equals. Nggak ada aturan khusus untuk",
                    "String.",
                    "",
                    "Kerangka equals selalu empat langkah, dengan urutan ini:",
                    "  if (this == lain) return true;               // 1. objek yang sama persis",
                    "  if (!(lain instanceof Titik)) return false;  // 2. null pun jatuh di sini",
                    "  Titik t = (Titik) lain;                      // 3. aman, tipenya pasti",
                    "  // 4. bandingkan field satu per satu",
                    "",
                    "Field primitif (int, double, boolean) cukup dibandingkan dengan ==.",
                    "Field berupa objek pakai Objects.equals(a, b). Method ini aman kalau",
                    "ketemu null, sedangkan a.equals(b) melempar NullPointerException begitu",
                    "a kebetulan null.",
                    "",
                    "Jebakan: parameternya wajib bertipe Object. Kalau kamu nulis",
                    "equals(Titik lain), yang terbentuk method baru (overload), bukan",
                    "override. HashSet tetap memakai versi bawaan. Jebakan ini nggak",
                    "menghasilkan error apa pun, dan cuma @Override yang bisa menangkapnya.",
                    "",
                    "Ada kontrak yang dipegang seluruh library Java. equals yang kamu tulis",
                    "harus memenuhinya:",
                    "  - Refleksif: x.equals(x) selalu true.",
                    "  - Simetris: x.equals(y) hasilnya sama dengan y.equals(x).",
                    "  - Transitif: kalau x sama dengan y, dan y sama dengan z, maka x sama",
                    "    dengan z.",
                    "  - Konsisten: hasilnya nggak berubah selama datanya nggak berubah.",
                    "  - x.equals(null) selalu false.",
                    "",
                    "Perbaikan ketiga, hashCode(). Method ini wajib ditulis setiap kali",
                    "equals ditulis. Aturannya cuma satu kalimat: dua objek yang equals harus",
                    "mengembalikan hashCode yang sama. Cara terpendeknya return",
                    "Objects.hash(x, y);. Isi Objects.hash dengan field yang sama persis",
                    "dengan yang dipakai di equals.",
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
                    "",
                    "HashSet dan HashMap mencari data dalam dua langkah. Pertama, hashCode",
                    "dihitung untuk menentukan \"ember\" tempat data disimpan. Kedua, isi ember",
                    "itu dibandingkan satu per satu pakai equals. Kalau hashCode dibiarkan",
                    "bawaan, dua objek yang equals bisa mendarat di ember yang beda, dan",
                    "equals nggak pernah sempat dipanggil.",
                    "",
                    "Bug dari equals dan hashCode yang nggak beres nggak melempar error apa",
                    "pun. Akibatnya seperti ini:",
                    "  - HashSet menyimpan duplikat, jadi size() lebih besar dari hitunganmu.",
                    "  - map.get(key) mengembalikan null, padahal datanya jelas udah di-put.",
                    "  - Kalau equals juga belum di-override, list.contains(objek) dan",
                    "    list.remove(objek) bilang objeknya nggak ketemu.",
                    "  - Kalau equals belum di-override, tes juga bisa gagal dengan pesan",
                    "    seperti 'expected Titik(3, 4) but was Titik(3, 4)'. Dua teks itu",
                    "    kelihatan sama persis, karena yang beda memang bukan teksnya.",
                    "",
                    "Kebalikannya, yaitu hashCode di-override tapi equals dibiarkan, sama",
                    "rusaknya. Objeknya mendarat di ember yang tepat, lalu ditolak karena",
                    "dianggap objek lain.",
                    "",
                    "getClass() bakal sering kamu temui di tiga tempat:",
                    "  - Di equals, sebagai pengganti instanceof yang lebih ketat:",
                    "      if (lain == null || getClass() != lain.getClass()) return false;",
                    "  - Di log dan pesan error. getClass().getSimpleName() memberi \"Titik\",",
                    "    sedangkan getClass().getName() memberi nama lengkap beserta",
                    "    package-nya.",
                    "  - Waktu kamu perlu tahu isi asli sebuah variabel bertipe Object.",
                    "",
                    "Bedanya, instanceof menerima subclass (Titik3D dianggap Titik),",
                    "sedangkan getClass menolaknya. instanceof lebih fleksibel, getClass",
                    "lebih aman untuk menjaga sifat simetris di kontrak equals. Dua-duanya",
                    "dipakai di proyek sungguhan. Pilih satu, lalu pakai terus secara",
                    "konsisten di satu class.",
                    "",
                    "Method Object lainnya cukup kamu kenali waktu membaca kode orang:",
                    "  clone()    -> menyalin objek; rancangannya bermasalah sejak awal, jadi orang",
                    "                lebih suka constructor penyalin atau method salinan sendiri.",
                    "  finalize() -> dulu dipanggil sebelum objek dibuang; sudah deprecated,",
                    "                jangan dipakai.",
                    "  wait(), notify(), notifyAll() -> komunikasi antar thread, dibahas di materi",
                    "                Multithreading & Concurrency Dasar.",
                    "",
                    "IDE bisa membuatkan ketiga method tadi dengan sekali klik. Record (Java",
                    "16+) bahkan menghasilkan ketiganya otomatis. Justru karena itu kamu",
                    "perlu paham isinya. Kode hasil generate itu yang paling sering kamu baca",
                    "di proyek orang. Yang perlu kamu cek adalah field mana aja yang ikut",
                    "dibandingkan, karena di situ bug-nya biasa ngumpet.",
                    "",
                    "Di aplikasi ini, kunci jawaban Latihan 12 (Kotak Generic) memakai",
                    "@Override public String toString() supaya System.out.println(p) mencetak",
                    "(Andi, 20), bukan Pasangan@1b6d3586. Sekarang kamu tahu kenapa baris itu",
                    "ada di sana.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Data ganda adalah masalah sehari-hari di aplikasi pendaftaran. Satu",
                    "orang mengisi form online, lalu datang lagi dan mengisi form kertas.",
                    "Supaya HashSet bisa membuang yang kembar, Java harus tahu kapan dua",
                    "objek dianggap sama, dan itu ditentukan equals dan hashCode yang kamu",
                    "tulis.",
                    "",
                    "Kasus kecil: panitia beasiswa menggabungkan pendaftar dari form online",
                    "dan form kertas. Siti Aminah dengan NIK 3201123456780001 muncul di",
                    "dua-duanya. Waktu dimasukkan ke HashSet<Pendaftar>, dia tetap terhitung",
                    "dua orang.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tentukan dulu arti \"sama\". Nama bisa kembar dan bisa salah ketik,",
                    "     jadi pakai NIK, yang memang dibuat unik untuk tiap orang.",
                    "  2. Override equals supaya cuma membandingkan NIK. Langkah instanceof",
                    "     sekaligus menolak null.",
                    "  3. Override hashCode dari field yang sama persis:",
                    "      @Override public boolean equals(Object o) {",
                    "          if (!(o instanceof Pendaftar)) return false;",
                    "          return nik.equals(((Pendaftar) o).nik);",
                    "      }",
                    "      @Override public int hashCode() { return Objects.hash(nik); }",
                    "  4. Uji kasus pinggirnya: \"Siti Aminah\" dan \"siti aminah\" dengan NIK",
                    "     yang sama harus terhitung satu orang. Dua orang bernama sama dengan",
                    "     NIK berbeda harus tetap dua.",
                    "",
                    "Ingat: tambahkan juga toString() yang mencetak nama dan NIK. Waktu",
                    "panitia memeriksa log, Pendaftar@1b6d3586 nggak ngasih tahu apa pun.",
                ]
            },
        ],
    },
    {
        "title": "18. OOP: Abstract & Interface",
        "sections": [
            {
                "body": [
                    "Abstract class",
                    "",
                    "Abstract class adalah class yang nggak bisa dibuat objeknya. Kamu nggak",
                    "bisa memakai new untuk class ini.",
                    "  - Boleh punya method abstrak, yaitu method tanpa isi. Boleh juga punya",
                    "    method biasa.",
                    "  - Gunanya jadi kerangka yang nanti diturunkan ke class lain.",
                    "",
                    "  abstract class Bentuk {",
                    "      abstract double luas();   // tanpa isi",
                    "      void info() { ... }        // method biasa",
                    "  }",
                    "",
                    "Interface",
                    "",
                    "Interface adalah semacam kontrak. Class yang memakainya wajib memenuhi",
                    "isi kontrak itu.",
                    "  - Method tanpa isi di interface otomatis public abstract. Sebelum Java",
                    "    8, semua method interface memang begitu.",
                    "  - Sejak Java 8, interface boleh punya default method dan static method.",
                    "  - Satu class bisa implements banyak interface sekaligus. Ini jalan",
                    "    keluar Java untuk multiple inheritance.",
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
                    "Abstract class dan interface, ringkasnya:",
                    "  Abstract class:",
                    "    - Bisa punya attribute & method biasa.",
                    "    - extends (satu parent saja).",
                    "    - Gunakan saat class punya 'kemiripan' kuat.",
                    "  Interface:",
                    "    - Hanya kontrak (metode utama).",
                    "    - implements (bisa banyak).",
                    "    - Gunakan saat ingin 'kemampuan' yang sama di class berbeda.",
                    "",
                    "Gampangnya, abstract class cocok untuk class yang masih satu keluarga,",
                    "misalnya Lingkaran dan Persegi yang sama-sama Bentuk. Interface cocok",
                    "untuk kemampuan yang bisa dimiliki class yang nggak saling berhubungan.",
                    "",
                    "Contoh interface di library bawaan Java:",
                    "  - List, Map, dan Set adalah interface.",
                    "  - ArrayList, HashMap, dan HashSet adalah implementasinya.",
                    "  - Konsep ini dipakai terus di materi Collection Framework.",
                ]
            },
            {
                "body": [
                    "Di atas disebut bahwa sejak Java 8 interface boleh punya default method",
                    "dan static method. Bagian ini perlu penjelasan sendiri, karena artinya",
                    "interface nggak lagi selalu kosong.",
                    "",
                    "Masalah yang diselesaikan default kira-kira begini. Bayangkan interface",
                    "List udah dipakai ribuan class di seluruh dunia. Lalu Java pengin",
                    "menambahkan method sort() ke List. Dengan aturan lama, setiap class yang",
                    "implements List langsung gagal dikompilasi, karena semuanya tiba-tiba",
                    "kurang satu method. default menyelesaikan masalah ini. Method baru itu",
                    "dibawa lengkap dengan isinya, jadi class lama nggak perlu diubah sama",
                    "sekali. Class yang pengin versinya sendiri tinggal meng-override.",
                    "",
                    "  default double total() { return jumlah() + biaya(); }",
                    "",
                    "Sekarang ada empat jenis method yang boleh ada di dalam interface:",
                    "  abstract   tanpa isi, wajib diisi pelaksana (yang sudah kamu tahu)",
                    "  default    punya isi, dipakai otomatis, boleh ditimpa pelaksana",
                    "  static     milik interface-nya sendiri: Pembayaran.rupiah(...). Tidak",
                    "             diwariskan, jadi Transfer.rupiah(...) tidak ada",
                    "  private    penolong bersama antar-default, tak terlihat dari luar (Java 9+)",
                    "",
                    "Field di interface juga istimewa. Apa pun yang kamu tulis di sana",
                    "otomatis jadi public static final, mau kata-kata itu kamu ketik atau",
                    "nggak.",
                    "  double TARIF_ADMIN = 2500;   // sama saja: public static final double",
                    "",
                    "Karena itu interface tetap nggak bisa menyimpan data per objek. Yang ada",
                    "di sana cuma konstanta.",
                    "",
                    "Dua contoh yang bakal sering kamu pakai. List.of(...) adalah static",
                    "method di interface List. Nanti di materi Comparable & Comparator kamu",
                    "bakal memanggil .reversed(). Itu default method milik interface",
                    "Comparator, yang langsung tersedia di comparator apa pun tanpa kamu",
                    "tulis sendiri.",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Toko online mengirim kabar pesanan lewat email, SMS, atau WhatsApp, dan",
                    "pilihannya bisa bertambah tahun depan. Kalau kode checkout cuma",
                    "bergantung pada interface Notifikasi, saluran baru cukup ditambah",
                    "sebagai class baru. Kode checkout-nya nggak perlu dibongkar.",
                    "",
                    "Kasus kecil: tim kamu diminta menambah notifikasi SMS di samping email",
                    "yang udah ada. Checkout cuma boleh tahu bahwa ada sesuatu yang bisa",
                    "mengirim pesan ke sebuah alamat atau nomor.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Cari kemampuan yang sama dari semua saluran: semuanya bisa",
                    "     kirim(tujuan, pesan). Kemampuan itu jadi isi interface.",
                    "  2. Tiap saluran jadi class yang implements interface itu dengan",
                    "     caranya sendiri:",
                    "      interface Notifikasi { void kirim(String tujuan, String pesan); }",
                    "      class NotifSms implements Notifikasi {",
                    "          public void kirim(String tujuan, String pesan) {",
                    "              System.out.println(\"SMS ke \" + tujuan + \": \" + pesan);",
                    "          }",
                    "      }",
                    "  3. Method checkout menerima parameter bertipe Notifikasi. Dia nggak",
                    "     peduli objek yang datang itu email atau SMS.",
                    "  4. Uji dengan dua saluran yang berbeda, lalu pastikan kode checkout",
                    "     nggak berubah satu baris pun.",
                    "",
                    "Jebakan: method kirim di class pelaksana wajib ditulis public. Tanpa",
                    "public, compiler menolak dengan pesan attempting to assign weaker access",
                    "privileges, karena method di interface selalu public.",
                ]
            },
        ],
    },
    {
        "title": "19. Anotasi: Metadata untuk Compiler & Framework",
        "sections": [
            {
                "body": [
                    "Sejak materi Inheritance kamu udah berkali-kali nulis @Override. Nanti",
                    "di JUnit ada @Test. Begitu masuk Spring Boot atau JPA, dua hal yang",
                    "disebut di materi terakhir kurikulum ini, hampir separuh isi berkasnya",
                    "berupa @Entity, @Autowired, dan @GetMapping. Selama ini semuanya cuma",
                    "hafalan: \"kalau override, tulis @Override di atasnya\". Padahal semuanya",
                    "satu jenis benda yang sama. Namanya anotasi, dan siapa pun bisa bikin",
                    "anotasi sendiri, termasuk kamu.",
                    "",
                    "Anotasi adalah penanda yang ditempel pada sesuatu di dalam kode. Ditulis",
                    "dengan @ lalu namanya, dan diletakkan tepat di atas (atau di depan)",
                    "benda yang ditandai.",
                    "",
                    "  @Override                          menempel di sebuah method",
                    "  @Entity                            menempel di sebuah class",
                    "  @Autowired                         menempel di sebuah field",
                    "  void simpan(@Valid Buku buku)      menempel di sebuah parameter",
                    "",
                    "Sekarang aturan yang paling penting, dan yang paling sering salah dipahami:",
                    "",
                    "  Anotasi nggak mengerjakan apa pun dengan sendirinya.",
                    "",
                    "Anotasi cuma tempelan, seperti stiker di kardus. Menempelkan @Test pada",
                    "sebuah method nggak bikin method itu jalan. Yang menjalankannya JUnit,",
                    "setelah dia membaca stikernya. Anotasi yang nggak ada pembacanya sama",
                    "aja dengan komentar: sah ditulis, tapi nggak berakibat apa-apa. Ini yang",
                    "bikin kesalahan anotasi berbahaya. Kalau gagal, nggak muncul error.",
                    "Programnya cuma diam.",
                    "",
                    "Ada tiga golongan pembaca anotasi. Golongannya menentukan kapan anotasi",
                    "itu bekerja:",
                    "",
                    "  Pembaca            Bekerja saat        Contoh",
                    "  ----------------   -----------------   ------------------------------",
                    "  compiler (javac)   dikompilasi         @Override, @FunctionalInterface,",
                    "                                         @SuppressWarnings, @SafeVarargs",
                    "  alat bantu & IDE   menulis / build     @Deprecated (namanya dicoret di",
                    "                                         layar), Lombok (menuliskan kode",
                    "                                         untukmu)",
                    "  framework          program berjalan    @Test, @Entity, @RestController",
                    "",
                    "Jangan tertukar dengan @param, @return, dan @throws yang muncul di dalam",
                    "blok /** ... */. Yang di dalam komentar cuma teks untuk manusia dan alat",
                    "dokumentasi. Compiler membuang seluruh komentar tanpa melihat isinya.",
                    "Bedanya cuma satu: ada di dalam /** */ atau nggak. Yang di luar komentar",
                    "itulah anotasi, dan anotasi betul-betul mengubah nasib kode.",
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
                    "Program di atas jalan dan mencetak dua baris. Yang menarik justru apa",
                    "yang terjadi kalau anotasinya diutak-atik.",
                    "",
                    "@Override, penyelamat dari salah ketik",
                    "",
                    "Coba ubah 'void bersuara()' di class Kucing jadi 'void bersura()'. Tanpa",
                    "@Override, kode itu sah. Java menganggapnya method baru yang kebetulan",
                    "namanya lain. Kucing tetap mewarisi bersuara() dari Hewan, dan",
                    "programnya mencetak 'Hewan bersuara'. Nggak ada error, nggak ada",
                    "peringatan. Yang ada cuma perilaku yang salah dan susah dilacak.",
                    "",
                    "Dengan @Override, javac langsung menolak:",
                    "",
                    "  error: method does not override or implement a method from a supertype",
                    "",
                    "Jebakan yang sama juga terjadi kalau parameternya meleset, dan ini",
                    "sering terjadi. Menulis equals(Kucing lain), padahal seharusnya",
                    "equals(Object lain), adalah kesalahan klasik yang cuma bisa ditangkap",
                    "@Override. Jadi tulis @Override setiap kali kamu override.",
                    "",
                    "@Deprecated, artinya \"masih ada, tapi jangan dipakai lagi\"",
                    "",
                    "Method-nya tetap berfungsi, karena kode lama nggak boleh mendadak rusak.",
                    "Tapi kode yang memanggilnya kena peringatan, dan IDE mencoret namanya:",
                    "",
                    "  warning: [deprecation] suara() in Hewan has been deprecated",
                    "",
                    "Kamu bakal sering lihat ini di library. Artinya ada cara baru yang lebih",
                    "benar.",
                    "",
                    "@SuppressWarnings(\"unchecked\"), untuk membungkam peringatan",
                    "",
                    "Anotasi ini cuma membungkam peringatan, dan masalahnya nggak ikut beres.",
                    "Hapus baris itu, lalu kompilasi dengan 'javac -Xlint:all Main.java'.",
                    "Muncul empat peringatan rawtypes dan unchecked, karena List tanpa",
                    "<String> bikin compiler nggak bisa lagi menjamin isinya String.",
                    "Anotasinya cuma menyuruh compiler diam. Bahayanya, kalau ternyata isinya",
                    "memang salah, kamu baru tahu waktu program crash. Pasang anotasi ini",
                    "cuma kalau kamu udah ngecek sendiri, dan sesempit mungkin: di satu",
                    "method, jangan di seluruh class.",
                    "",
                    "@FunctionalInterface, pengunci interface supaya tetap punya satu",
                    "abstract method",
                    "",
                    "Sapaan sengaja nggak dipakai sama sekali di program itu. Anotasi ini",
                    "bekerja pada deklarasinya, nggak pada pemakaiannya. Tambahkan satu",
                    "method lagi ke Sapaan, dan kompilasinya gagal dengan pesan 'Unexpected",
                    "@FunctionalInterface annotation'. Tanpa anotasi itu, penambahannya",
                    "diterima. Yang rusak malah semua lambda yang terlanjur memakai Sapaan di",
                    "tempat lain (lihat materi Lambda Expression).",
                    "",
                    "@SafeVarargs, janji bahwa method varargs bergenerik nggak",
                    "menyalahgunakan argumennya",
                    "",
                    "Jarang kamu tulis sendiri. Cukup kenali bentuknya waktu membaca library.",
                    "",
                    "Anotasi yang membawa argumen",
                    "",
                    "Banyak anotasi butuh keterangan tambahan. Bentuknya seperti memanggil method:",
                    "",
                    "  @DisplayName(\"Penjumlahan dua angka positif\")",
                    "  @Column(name = \"nama_lengkap\", nullable = false)",
                    "  @SuppressWarnings({\"unchecked\", \"rawtypes\"})   // beberapa nilai: pakai { }",
                    "",
                    "Argumennya ditulis 'nama = nilai', dipisah koma. Tapi ada satu jalan",
                    "pintas yang sering bikin bingung waktu membaca kode Spring:",
                    "",
                    "  @RequestMapping(\"/user\")",
                    "  sama persis dengan",
                    "  @RequestMapping(value = \"/user\")",
                    "",
                    "Kalau kamu cuma mengisi satu argumen, dan nama argumennya kebetulan",
                    "value, namanya boleh dihilangkan. Jalan pintas ini cuma berlaku untuk",
                    "argumen bernama value. Jadi @Table(\"buku\") artinya @Table(value =",
                    "\"buku\"), dan itu nggak sama dengan @Table(name = \"buku\"). @Table milik",
                    "JPA nggak punya argumen value, jadi di sana bentuk pendek itu ditolak",
                    "compiler.",
                    "",
                    "Nilai argumennya harus konstanta yang udah pasti waktu kompilasi: teks,",
                    "angka, true/false, enum, atau .class. Hasil pemanggilan method atau isi",
                    "variabel biasa nggak boleh.",
                    "",
                    "Satu benda boleh ditempeli beberapa anotasi sekaligus. Nggak pakai koma,",
                    "dan urutannya bebas:",
                    "",
                    "  @Test",
                    "  @DisplayName(\"Saldo tidak boleh minus\")",
                    "  void testSaldo() { ... }",
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
                    "Contoh ini bukan untuk sering kamu tulis. Di tahun pertama, mungkin kamu",
                    "nggak akan nulis yang begini sekali pun. Tujuannya supaya anotasi nggak",
                    "lagi terasa seperti sihir. Kamu baru aja bikin @Langkah sendiri, dan",
                    "cara kerjanya persis seperti @Test.",
                    "",
                    "Kita bedah barisnya:",
                    "  @interface Langkah { ... }   mendeklarasikan anotasi baru. Perhatikan '@'",
                    "                               menempel di 'interface', beda dari interface",
                    "                               biasa.",
                    "  String nama();               'argumen' anotasi ditulis seperti method",
                    "                               tanpa isi. Boleh diberi bawaan:",
                    "                               int urutan() default 99;",
                    "  @Retention(...RUNTIME)       sampai kapan tanda ini bertahan.",
                    "  @Target(ElementType.METHOD)  boleh ditempel di mana saja.",
                    "",
                    "Ya, @Retention dan @Target itu sendiri adalah anotasi yang ditempel pada",
                    "anotasi. Nggak ada tingkatan khusus di sini. Semuanya benda biasa.",
                    "",
                    "@Retention punya tiga pilihan. Salah pilih di sini adalah penyebab",
                    "paling sering anotasi buatan sendiri \"nggak jalan\":",
                    "  SOURCE   dibuang setelah dikompilasi. Cuma untuk compiler & alat bantu",
                    "           (@Override).",
                    "  CLASS    ikut ke berkas .class, tapi tidak dimuat saat berjalan.",
                    "           Ini bawaannya.",
                    "  RUNTIME  masih bisa dibaca saat program berjalan. Wajib untuk framework.",
                    "",
                    "Coba hapus baris @Retention di program tadi. Programnya tetap",
                    "dikompilasi tanpa keluhan sedikit pun, lalu mati waktu dijalankan dengan",
                    "NullPointerException. Penyebabnya, isAnnotationPresent nggak menemukan",
                    "apa-apa. Lagi-lagi gagal tanpa suara.",
                    "",
                    "@Target menutup celah yang lain. Coba tempelkan @Langkah pada class",
                    "Laporan. javac menolak dengan pesan 'annotation type not applicable to",
                    "this kind of declaration'. Nilai yang sering dipakai:",
                    "",
                    "  TYPE (class/interface/enum), METHOD, FIELD, PARAMETER, CONSTRUCTOR",
                    "",
                    "Boleh lebih dari satu sekaligus:",
                    "",
                    "  @Target({ElementType.METHOD, ElementType.FIELD})",
                    "",
                    "Bagian 'Laporan.class.getDeclaredMethods()' itu namanya refleksi.",
                    "Refleksi adalah kemampuan program memeriksa dirinya sendiri waktu",
                    "berjalan: melihat daftar method sebuah class, melihat anotasi yang",
                    "menempel di method itu, lalu memanggilnya lewat invoke(). Kamu belum",
                    "perlu menguasai refleksi sekarang. Cukup tahu bahwa begitulah framework",
                    "Java bekerja. Nggak ada keajaiban, cuma program yang membaca tanda lalu",
                    "bertindak.",
                    "",
                    "Anotasi yang bakal kamu temui di kode sungguhan:",
                    "",
                    "  Anotasi                 Dari        Maksudnya",
                    "  ---------------------   ---------   ------------------------------------",
                    "  @Test                   JUnit       jalankan method ini sebagai satu kasus",
                    "                                      uji",
                    "  @BeforeEach             JUnit       jalankan ini dulu, sebelum setiap @Test",
                    "  @DisplayName(\"...\")     JUnit       pakai kalimat ini di laporan, bukan",
                    "                                      nama method",
                    "  @Service, @Component    Spring      buatkan satu objek class ini dan",
                    "                                      kelola untukku",
                    "  @Autowired              Spring      isikan field ini dengan objek yang",
                    "                                      kamu kelola",
                    "  @RestController         Spring      class ini melayani HTTP dan menjawab",
                    "                                      JSON",
                    "  @GetMapping(\"/buku\")    Spring      panggil method ini kalau ada GET ke",
                    "                                      /buku",
                    "  @Entity                 JPA         class ini mewakili satu tabel di",
                    "                                      database",
                    "  @Id                     JPA         field ini primary key-nya",
                    "  @Column(name = \"...\")   JPA         field ini menempel ke kolom bernama itu",
                    "  @JsonProperty(\"nama\")   Jackson     saat diubah jadi JSON, pakai nama itu",
                    "  @Data                   Lombok      tuliskan getter, setter, toString,",
                    "                                      equals, hashCode-nya untukku saat",
                    "                                      kompilasi",
                    "  @Builder                Lombok      buatkan cara membangun objek ini",
                    "                                      bertahap",
                    "",
                    "Kalau kamu bingung, curigai Lombok lebih dulu. Lombok menuliskan method",
                    "sungguhan waktu kompilasi. Jadi getNama() betul-betul ada dan bisa",
                    "dipanggil, tapi nggak akan kamu temukan di berkasnya, berapa kali pun",
                    "kamu menggulir. Kalau ada method yang \"nggak ada tapi bisa dipanggil\",",
                    "lihat anotasi di kepala class-nya.",
                    "",
                    "Jebakan yang paling sering bikin orang buang waktu:",
                    "  1. Anotasi dari package yang salah. org.junit.Test (JUnit 4) dan",
                    "     org.junit.jupiter.api.Test (JUnit 5) sama-sama bernama @Test. Kalau",
                    "     salah import, tesnya nggak pernah dijalankan, dan laporannya bilang",
                    "     \"semua lulus\".",
                    "  2. Anotasi tanpa pembaca. @Autowired di objek yang kamu bikin sendiri",
                    "     pakai new nggak diisi siapa pun. Spring cuma mengurus objek yang",
                    "     dia buat sendiri.",
                    "  3. Anotasi buatan sendiri tanpa @Retention(RUNTIME). Ini udah dibahas",
                    "     di atas.",
                    "",
                    "Ada satu cara membaca kode Spring atau JPA tanpa panik. Coret dulu semua",
                    "baris yang diawali @. Yang tersisa hampir selalu class dan method Java",
                    "biasa yang udah kamu pahami. Sesudah itu, baca anotasinya satu per satu",
                    "sebagai perintah ke framework: \"buatkan objeknya\", \"petakan ke tabel\",",
                    "\"panggil kalau ada request\". Yang kamu tulis adalah isi method-nya.",
                    "Sisanya dikerjakan program lain yang membaca tanda-tanda itu.",
                    "",
                    "Kalau ada anotasi yang nggak kamu kenal, arahkan kursor ke situ lalu",
                    "tekan Ctrl+klik di IDE. Anotasi itu berkas biasa berisi '@interface',",
                    "jadi bisa kamu baca.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Di proyek Spring Boot, @GetMapping menentukan method mana yang menjawab",
                    "sebuah alamat web. Di JUnit, @Test menentukan method mana yang",
                    "dijalankan sebagai tes. Di antara semuanya, yang paling sering",
                    "menyelamatkan pemula justru yang paling kecil, yaitu @Override.",
                    "",
                    "Kasus kecil: di aplikasi kasir, class Diskon punya method int",
                    "potongan(int total) yang mengembalikan 0. Programmer lain menulis",
                    "DiskonMember extends Diskon dengan method int potongan(long total).",
                    "Programnya jalan tanpa error, tapi member tetap bayar penuh.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Mulai dari gejalanya: method milik class anak nggak pernah",
                    "     dipanggil. Itu tanda klasik override yang meleset.",
                    "  2. Bandingkan tanda tangan dua method itu. Tipe parameternya beda",
                    "     (int dan long), jadi Java menganggapnya method baru yang cuma",
                    "     kebetulan bernama sama.",
                    "  3. Tempelkan @Override, lalu kompilasi. javac langsung menolak dengan",
                    "     pesan method does not override or implement a method from a",
                    "     supertype:",
                    "      class DiskonMember extends Diskon {",
                    "          @Override",
                    "          int potongan(long total) { return (int) (total / 10); }",
                    "      }",
                    "  4. Samakan parameternya jadi int, kompilasi lagi, lalu uji: member",
                    "     yang belanja 100000 harus dapat potongan 10000.",
                    "",
                    "Ingat: biasakan menulis @Override di setiap method yang kamu maksud",
                    "sebagai pengganti. Tanpa anotasi itu, kesalahan seperti ini baru",
                    "ketahuan dari keluhan pelanggan.",
                ]
            },
        ],
    },
    {
        "title": "20. Record & Sintaks Java Modern",
        "sections": [
            {
                "body": [
                    "Semua yang kamu pelajari sampai materi ini masih berlaku. Yang berubah",
                    "cuma cara orang menuliskannya. Sejak Java 17 lalu 21 jadi versi LTS,",
                    "berkas Java baru yang kamu buka di GitHub atau di kantor banyak memakai",
                    "empat hal baru. Keempatnya belum pernah disebut di sini: record, text",
                    "block, switch ekspresi bentuk lengkap, dan sealed. Tanpa kenal",
                    "keempatnya, kode Java zaman sekarang kelihatan seperti bahasa lain, dan",
                    "kamu bisa macet dari baris pertama.",
                    "",
                    "Masalah yang diselesaikan record",
                    "",
                    "Class yang tugasnya cuma membawa data selalu bentuknya begini:",
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
                    "Kalau ditulis lengkap, itu sekitar tiga puluh baris cuma untuk menyimpan",
                    "dua angka. Di dalamnya nggak ada satu pun keputusan. Semuanya bisa",
                    "ditebak dari nama dan tipe field-nya. Java 16 menyediakan bentuk",
                    "singkatnya. Satu baris di bawah ini sama persis dengan class tiga puluh",
                    "baris tadi:",
                    "",
                    "  public record Titik(int x, int y) { }",
                    "",
                    "Dari satu baris itu, Java membuatkan:",
                    "  - Dua field private final bernama x dan y. Nggak kamu tulis, tapi",
                    "    betul-betul ada.",
                    "  - Canonical constructor, yaitu constructor utama: new Titik(3, 4).",
                    "    Urutan parameternya persis urutan di dalam kurung.",
                    "  - Dua method pembaca: x() dan y().",
                    "  - equals(Object), yang bernilai true kalau semua komponennya sama.",
                    "  - hashCode(), yang otomatis berpasangan dengan equals-nya. Jadi",
                    "    HashMap dan HashSet langsung berperilaku benar. Alasan keduanya",
                    "    wajib berpasangan ada di materi Class Object.",
                    "  - toString(), yang menghasilkan \"Titik[x=3, y=4]\", bukan Titik@1b6d3586.",
                    "",
                    "Nama-nama di dalam kurung itu disebut komponen. Istilahnya beda dari",
                    "parameter dan field.",
                    "",
                    "Kenapa getter-nya x(), bukan getX()?",
                    "",
                    "Setiap komponen dapat satu method yang namanya sama persis dengan",
                    "komponennya. Aturan getX() itu konvensi JavaBeans dari tahun 1997.",
                    "Konvensi itu dibuat untuk objek yang datanya bisa diubah lewat pasangan",
                    "getX() dan setX(). Record nggak begitu, jadi awalan get- nggak dipakai.",
                    "",
                    "Akibatnya waktu kamu membaca kode: kalau ketemu p.harga() tanpa \"get\",",
                    "jangan capek nyari method harga() di badan class. Biasanya method itu",
                    "memang nggak ditulis di sana.",
                    "",
                    "Akibatnya waktu kamu menulis kode: kalau kamu ngetik p.getHarga() pada",
                    "sebuah record, hasilnya:",
                    "  error: cannot find symbol",
                    "",
                    "Pemula biasanya mengira ada import yang kurang. Padahal nama method-nya",
                    "memang bukan itu.",
                    "",
                    "Kenapa nggak ada setter?",
                    "",
                    "Semua field record bersifat final. Nggak ada setX(), dan menulis x = 5",
                    "di dalam record ditolak:",
                    "  error: cannot assign a value to final variable x",
                    "",
                    "Ini memang tujuan record, jadi nggak perlu diakali. Objek yang nggak",
                    "bisa berubah disebut immutable. Objek immutable aman jadi kunci HashMap,",
                    "aman dipakai beberapa thread sekaligus, dan nggak bakal berubah tanpa",
                    "sepengetahuanmu gara-gara dioper ke method milik orang lain. Kalau mau",
                    "\"mengubahnya\", bikin objek baru. Contohnya ada di method denganAngka()",
                    "di program berikutnya.",
                    "",
                    "Jebakan: final di record cuma berlaku satu lapis.",
                    "  record Tim(String nama, List<String> anggota) { }",
                    "",
                    "Field anggota nggak bisa diganti dengan list lain. Tapi isi list itu",
                    "masih bisa ditambah dan dihapus oleh siapa pun yang memegangnya. Kalau",
                    "isinya harus betul-betul beku, salin list-nya di compact constructor:",
                    "anggota = List.copyOf(anggota);",
                    "",
                    "Compact constructor",
                    "",
                    "Compact constructor adalah constructor tanpa daftar parameter. Isinya",
                    "validasi dan perapian data.",
                    "",
                    "  record Nilai(String nama, int angka) {",
                    "      Nilai {                  // tanpa (String nama, int angka)",
                    "          if (angka < 0) throw new IllegalArgumentException(\"negatif\");",
                    "          nama = nama.trim();  // menimpa parameter; ini yang disimpan",
                    "      }",
                    "  }",
                    "",
                    "Menulis this.nama = nama di dalamnya malah error, karena Java baru",
                    "mengisi field-nya sesudah blok itu selesai. Yang boleh kamu lakukan di",
                    "situ cuma dua: melempar exception, atau menimpa nilai parameter sebelum",
                    "disimpan.",
                    "",
                    "Yang boleh ditambahkan ke badan record: method biasa, method static,",
                    "konstanta static, constructor lain (baris pertamanya wajib this(...)),",
                    "dan implements interface apa pun.",
                    "",
                    "Yang nggak boleh, beserta pesan compiler-nya:",
                    "  - field instance tambahan  ->  error: field declaration must be static",
                    "  - extends class lain       ->  error: '{' expected",
                    "",
                    "Alasan yang kedua: record otomatis menurunkan java.lang.Record, dan Java",
                    "cuma mengizinkan satu induk.",
                    "",
                    "Record tetap boleh implements interface sebanyak apa pun. Karena itu",
                    "record cocok dipasangkan dengan sealed, yang dibahas di bagian akhir",
                    "materi ini.",
                    "",
                    "Kapan record cocok dipakai:",
                    "  - DTO (data transfer object), yaitu bentuk data yang lewat antar",
                    "    lapisan program, misalnya request dan response sebuah API.",
                    "  - Satu baris hasil query database.",
                    "  - Nilai gabungan: Koordinat(x, y), Rentang(awal, akhir), Uang(jumlah,",
                    "    mataUang).",
                    "  - Kunci gabungan untuk HashMap, karena equals dan hashCode-nya udah",
                    "    benar dari awal.",
                    "  - Node pohon parser, dipasangkan dengan sealed.",
                    "",
                    "Kapan record nggak cocok:",
                    "  - Field-nya memang harus berubah selama objek hidup, misalnya",
                    "    keranjang belanja, koneksi, atau objek yang menyimpan status. Untuk",
                    "    itu tetap pakai class biasa.",
                    "  - Entity JPA atau Hibernate. Framework itu membuat objek lewat",
                    "    constructor kosong, lalu mengisi field satu per satu. Record nggak",
                    "    menyediakan dua-duanya. Pola yang umum: class biasa untuk entity,",
                    "    record untuk DTO yang dikirim keluar.",
                    "  - Kamu butuh pewarisan bertingkat lewat extends.",
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
                    "  Andi / 92",
                    "  Nilai[nama=Andi, angka=92]",
                    "  true",
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
                    "Tiga baris pertama masing-masing membuktikan satu hal:",
                    "  Andi / 92                   nama() sudah ter-trim oleh compact constructor",
                    "  Nilai[nama=Andi, angka=92]  toString bawaan record, tanpa ditulis sendiri",
                    "  true                        equals membandingkan isi, bukan alamat objek",
                    "",
                    "Tiga baris yang rapi berkolom itu datang dari printf, bukan println:",
                    "",
                    "  System.out.printf(\"%-6s %3d %c%n\", nama, angka, grade);",
                    "",
                    "Cara bacanya: %-6s artinya teks rata kiri selebar 6, %3d angka rata",
                    "kanan selebar 3, %c satu karakter, dan %n ganti baris. Nilainya diambil",
                    "berurutan dari argumen sesudah tanda kutip. Makanya kolomnya sejajar",
                    "walaupun panjang namanya beda-beda. Hal ini nggak mungkin dirapikan",
                    "pakai println dan tanda tambah. Daftar lengkap penandanya beserta",
                    "jebakannya ada di materi String & Scanner. Di sini cukup tahu bahwa",
                    "printf itu println yang bisa dikasih cetakan.",
                    "",
                    "Text block (Java 15+)",
                    "",
                    "Text block adalah string yang dibuka dan ditutup dengan tiga tanda",
                    "kutip. Sebelum ada text block, SQL empat baris terpaksa ditulis begini:",
                    "",
                    "  String sql = \"SELECT nama, angka\\n\" +",
                    "               \"FROM nilai\\n\" +",
                    "               \"WHERE angka >= 70\";",
                    "",
                    "Tiap baris butuh tanda kutip, tanda tambah, dan \\n sendiri. Satu \\n",
                    "kelupaan, dan query-mu jadi berbunyi \"...angkaFROM nilai\". Error-nya",
                    "muncul jauh dari tempat salahnya. JSON lebih parah lagi. Setiap tanda",
                    "kutip di dalamnya harus ditulis \\\", sampai barisnya susah dibaca",
                    "manusia. Di dalam text block, tanda kutip ditulis apa adanya.",
                    "",
                    "Ada tiga aturan text block, dan ketiganya sering menjebak:",
                    "  1. Tiga kutip pembuka wajib langsung diikuti ganti baris.",
                    "  2. Indentasi yang sama-sama dipakai semua baris dipotong otomatis.",
                    "  3. Kalau tiga kutip penutup berdiri di baris sendiri, ada satu ganti",
                    "     baris tambahan di ujung string.",
                    "",
                    "Aturan 1 artinya tiga kutip, lalu SELECT, lalu tiga kutip dalam satu",
                    "baris ditolak compiler. Isi string-nya harus mulai di baris berikutnya.",
                    "",
                    "Aturan 2 yang paling sering bikin salah. Java mencari baris yang paling",
                    "sedikit menjoroknya, termasuk baris tempat tiga kutip penutup berdiri.",
                    "Lalu Java memotong spasi sebanyak itu dari semua baris. Makanya kode",
                    "yang menjorok rapi di dalam method nggak membawa spasinya masuk ke isi",
                    "string. Akibat yang bikin kaget: kalau penutupnya dipindah ke kolom nol,",
                    "seluruh spasi indentasi ikut masuk ke string. Bug ini nggak menghentikan",
                    "apa pun, SQL-nya tetap jalan. Tapi teks di log jadi menjorok aneh, dan",
                    "perbandingan pakai equals mendadak gagal tanpa kelihatan sebabnya.",
                    "",
                    "Aturan 3: kalau kamu nggak mau ada ganti baris tambahan di akhir,",
                    "tempelkan tiga kutip penutup di ujung baris terakhir isinya. Persis",
                    "seperti sql dan json di program tadi.",
                    "",
                    "Ada dua escape yang cuma ada di text block:",
                    "",
                    "  \\ di ujung baris   sambung ke baris berikutnya tanpa ganti baris. Berguna",
                    "                     untuk satu kalimat panjang yang ingin ditulis rapi di",
                    "                     beberapa baris.",
                    "  \\s                 satu spasi yang tidak ikut dibuang. Spasi di ujung tiap",
                    "                     baris selalu dipangkas Java, dan biasanya memang itu",
                    "                     yang kamu mau.",
                    "",
                    "Switch ekspresi, bentuk lengkapnya",
                    "",
                    "Materi Percabangan udah memperkenalkan bentuk panah satu baris. Tiga hal",
                    "berikut belum dibahas, dan ketiganya ada di method grade() tadi:",
                    "  1. Satu cabang boleh punya beberapa label: case 10, 9 -> 'A';",
                    "  2. Cabang yang badannya pakai kurung kurawal menyerahkan nilainya",
                    "     lewat yield, bukan return.",
                    "  3. Nggak ada break sama sekali, dan itu memang disengaja.",
                    "",
                    "Label berkoma menggantikan pola lama case 10: case 9: yang mengandalkan",
                    "fall-through. Pola lama itu cuma jalan kalau break-nya sengaja",
                    "dihilangkan, dan pembacanya selalu ragu apakah itu disengaja atau lupa.",
                    "",
                    "yield dipakai kalau sebuah cabang butuh lebih dari satu baris:",
                    "",
                    "  default -> {",
                    "      char sementara = angka >= 60 ? 'D' : 'E';",
                    "      yield sementara;",
                    "  }",
                    "",
                    "Menulis return di dalamnya ditolak:",
                    "  error: attempt to return out of a switch expression",
                    "",
                    "Alasannya masuk akal. return keluar dari seluruh method, padahal yang",
                    "dibutuhkan di sini cuma satu nilai untuk satu cabang.",
                    "",
                    "Soal break: bentuk panah nggak punya fall-through sama sekali. Tiap",
                    "cabang berdiri sendiri. break cuma urusan bentuk lama yang pakai titik",
                    "dua.",
                    "",
                    "Ada beda penting antara switch ekspresi dan switch statement, dan ini",
                    "yang paling sering bikin salah. Switch ekspresi menghasilkan nilai, jadi",
                    "dia wajib punya jawaban untuk setiap kemungkinan masukan. Tanpa default,",
                    "compiler menolak dengan pesan:",
                    "  error: the switch expression does not cover all possible input values",
                    "",
                    "Switch statement, yang nggak menghasilkan nilai, nggak menuntut itu.",
                    "Pengecualiannya ada di bagian berikutnya: enum dan sealed bisa",
                    "dinyatakan lengkap tanpa default.",
                    "",
                    "Jangan juga mencampur dua bentuk label dalam satu switch:",
                    "",
                    "  case 1 -> ...;",
                    "  case 2: ...;     ->  error: different case kinds used in the switch",
                    "",
                    "Pilih satu bentuk untuk seluruh switch itu.",
                ],
            },
            {
                "body": [
                    "Sisa materi ini membahas dua fitur yang hampir selalu muncul bersama record.",
                    "",
                    "Pattern matching",
                    "",
                    "Sejak Java 16, instanceof boleh sekalian memberi nama variabel:",
                    "  if (h instanceof Kucing k) { k.mengeong(); }",
                    "",
                    "Dulu kamu menulis dua langkah: cek dengan instanceof, lalu cast manual",
                    "(lihat materi Polymorphism). Bentuk baru menggabungkan keduanya.",
                    "Variabel k cuma ada di dalam blok yang udah pasti Kucing, jadi cast yang",
                    "salah nggak mungkin terjadi.",
                    "",
                    "Sejak Java 21, pola yang sama boleh dipakai sebagai label switch:",
                    "",
                    "  String suara = switch (h) {",
                    "      case Kucing k -> k.nama() + \" bilang meong\";",
                    "      case Anjing a -> a.nama() + \" bilang guk\";",
                    "      case null     -> \"tidak ada hewan\";",
                    "      default       -> \"hewan lain\";",
                    "  };",
                    "",
                    "Bentuk ini menggantikan rantai if-instanceof panjang yang dulu wajib",
                    "ditulis. Hasilnya satu ekspresi dan satu nilai, dan variabelnya (k, a)",
                    "langsung siap dipakai di cabangnya masing-masing.",
                    "",
                    "case null adalah perubahan besar yang gampang terlewat. Selama ini,",
                    "switch atas nilai null selalu melempar NullPointerException, jadi orang",
                    "terbiasa menaruh if (h == null) di atasnya. Sekarang null boleh jadi",
                    "cabang biasa.",
                    "",
                    "Jebakan: kalau case null nggak kamu tulis, perilaku lamanya masih",
                    "berlaku. switch-nya tetap melempar NullPointerException, dan null nggak",
                    "jatuh ke default.",
                    "",
                    "Kamu juga boleh menambahkan syarat dengan when:",
                    "  case Lingkaran l when l.jari() > 100 -> \"lingkaran raksasa\";",
                    "",
                    "Di sini urutan case jadi penting. Cabang yang pakai when ditulis sebelum",
                    "versi tanpa syarat, karena yang dipakai adalah cabang pertama yang",
                    "cocok. Kalau urutannya dibalik, cabang ber-when nggak akan pernah kena,",
                    "dan compiler menolak cabang yang jelas nggak bisa dicapai.",
                    "",
                    "Karena record tahu persis komponennya, Java 21 juga membolehkan",
                    "membongkar isinya langsung di label. Namanya record pattern:",
                    "  case Persegi(double sisi) -> \"persegi sisi \" + sisi;",
                    "",
                    "Hasilnya sama dengan case Persegi p -> lalu memakai p.sisi(). Bedanya,",
                    "kamu langsung dapat sisi tanpa lewat p.",
                    "",
                    "Sealed (Java 17+)",
                    "",
                    "sealed membatasi siapa aja yang boleh menurunkan sebuah tipe.",
                    "  sealed interface Bentuk permits Lingkaran, Persegi, Segitiga { }",
                    "",
                    "Artinya, nggak ada class lain di mana pun yang boleh implements Bentuk.",
                    "Interface biasa terbuka untuk siapa aja (lihat materi Abstract &",
                    "Interface). sealed menutupnya jadi daftar yang pasti dan bisa dihitung.",
                    "Setiap nama di permits wajib memilih salah satu dari tiga: final, sealed",
                    "lagi, atau non-sealed. non-sealed artinya \"mulai dari sini boleh",
                    "diturunkan bebas lagi\". Record otomatis final, jadi record memenuhi",
                    "syarat itu tanpa kata tambahan. Makanya sealed dan record sering banget",
                    "dipakai berpasangan.",
                    "",
                    "Untungnya kerasa di compiler. Karena daftar turunannya tertutup, switch",
                    "yang mencakup ketiganya dianggap lengkap, dan default boleh dihilangkan.",
                    "Suatu hari kamu menambah Trapesium ke permits. Setiap switch yang belum",
                    "menanganinya langsung ditolak dengan pesan:",
                    "  error: the switch expression does not cover all possible input values",
                    "",
                    "Bandingkan dengan menulis default -> throw new",
                    "IllegalStateException(...). Dengan cara itu, bug yang sama baru ketahuan",
                    "waktu program udah jalan, dari laporan pemakai. Prinsipnya sama dengan",
                    "switch atas enum tanpa default (lihat materi Enum), cuma diperluas ke",
                    "class dan record.",
                    "",
                    "Versi Java (cek punyamu dengan java -version):",
                    "",
                    "  14  switch ekspresi (panah, yield)     15  text block",
                    "  16  record, instanceof berpola         17  sealed",
                    "  21  pattern matching di switch, case null, when, record pattern",
                    "",
                    "Contoh terakhir di bawah butuh Java 21, jadi sengaja ditulis tanpa",
                    "method main. Bentuknya memang berkas model yang dipakai berkas lain.",
                    "Kalau kamu menyalinnya dan javac-mu masih versi 17, pesannya:",
                    "  error: patterns in switch statements are a preview feature and are",
                    "  disabled by default.",
                    "",
                    "Kodenya nggak salah. JDK-mu aja yang lebih tua. Bentuk ini makin sering",
                    "muncul di kode Java baru, jadi bisa mengenalinya lebih penting daripada",
                    "bisa menjalankannya.",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aplikasi ojek online mengirim titik jemput sebagai pasangan lintang dan",
                    "bujur. Data seperti itu cuma dibawa dari satu bagian program ke bagian",
                    "lain dan nggak pernah diubah. Record cocok untuk ini, karena equals,",
                    "hashCode, dan toString-nya udah benar sejak baris pertama.",
                    "",
                    "Kasus kecil: pernah ada titik jemput yang masuk dengan lintang 106.8",
                    "dan bujur -6.2, karena urutannya tertukar. Peta akhirnya menunjuk",
                    "tempat yang ngawur, dan pengemudi bingung harus ke mana.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Datanya cuma dibawa dan nggak berubah, jadi pakai record dengan dua",
                    "     komponen, lintang dan bujur.",
                    "  2. Tulis aturannya: lintang harus di antara -90 dan 90, bujur di",
                    "     antara -180 dan 180.",
                    "  3. Taruh pengecekannya di compact constructor, supaya objek yang salah",
                    "     nggak pernah sempat dibuat. Bujur dicek dengan cara yang sama:",
                    "      record Titik(double lintang, double bujur) {",
                    "          Titik {",
                    "              if (lintang < -90 || lintang > 90)",
                    "                  throw new IllegalArgumentException(\"lintang \" + lintang);",
                    "          }",
                    "      }",
                    "  4. Uji dua arah: new Titik(-6.2, 106.8) harus lolos, dan",
                    "     new Titik(106.8, -6.2) harus ditolak dengan pesan lintang 106.8.",
                    "",
                    "Jebakan: nilai komponennya dibaca lewat titik.lintang(), bukan",
                    "titik.getLintang(). Menulis getLintang() pada record berujung error",
                    "cannot find symbol.",
                ]
            },
        ],
    },
    {
        "title": "21. Exception Handling",
        "sections": [
            {
                "body": [
                    "Exception adalah error yang terjadi waktu program sedang berjalan. Kalau",
                    "nggak ditangani, program langsung berhenti di baris itu, dan baris-baris",
                    "sesudahnya nggak pernah dijalankan.",
                    "",
                    "Beberapa contoh yang bakal sering kamu temui:",
                    "  - 10 / 0 melempar ArithmeticException, karena bilangan bulat nggak",
                    "    bisa dibagi nol.",
                    "  - arr[10], padahal array-nya lebih kecil dari itu, melempar",
                    "    ArrayIndexOutOfBoundsException.",
                    "  - null.something(), yaitu memanggil method lewat variabel yang isinya",
                    "    null, melempar NullPointerException.",
                    "  - Mengubah String jadi int, padahal isinya bukan angka, melempar",
                    "    NumberFormatException.",
                    "",
                    "Supaya program nggak berhenti begitu aja, kodenya dibungkus pakai try,",
                    "catch, dan finally:",
                    "",
                    "  try {",
                    "      // kode yang mungkin error",
                    "  } catch (TipeException e) {",
                    "      // penanganan error",
                    "  } finally {",
                    "      // selalu dijalankan (opsional)",
                    "  }",
                    "",
                    "Cara bacanya begini:",
                    "  - try berisi kode yang mungkin gagal.",
                    "  - catch jalan kalau di dalam try terjadi exception yang tipenya cocok.",
                    "    e adalah objek exception-nya, isinya keterangan soal error tadi.",
                    "  - finally selalu dijalankan, entah try-nya berhasil atau gagal. Bagian",
                    "    ini boleh nggak ditulis.",
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
                    "Satu catch boleh menangkap beberapa jenis exception sekaligus. Pisahkan",
                    "tipenya pakai garis tegak:",
                    "",
                    "  } catch (ArithmeticException | NullPointerException e) { ... }",
                    "",
                    "Bisa juga pakai beberapa blok catch berurutan. Kalau begitu, taruh yang",
                    "lebih spesifik duluan. Kalau kebalik, misalnya catch (Exception e)",
                    "ditaruh di atas catch (ArithmeticException e), compiler menolak dengan",
                    "pesan exception ArithmeticException has already been caught.",
                    "",
                    "throw dan throws mirip, tapi tugasnya beda:",
                    "  - throw melempar exception dengan sengaja. Biasanya dipakai waktu data",
                    "    yang masuk nggak masuk akal:",
                    "      if (umur < 0) { throw new IllegalArgumentException(\"Umur salah\"); }",
                    "  - throws ditulis di kepala method. Artinya method itu bisa melempar",
                    "    exception jenis tersebut, jadi yang memanggil harus siap.",
                    "      void bacaFile() throws IOException { ... }",
                    "",
                    "Exception dibagi jadi dua golongan:",
                    "  - Checked: compiler memaksa kamu mengurusnya, misalnya IOException.",
                    "    Kalau nggak ditangkap pakai try-catch dan nggak ditulis di throws,",
                    "    programnya nggak mau dikompilasi. Pesannya: unreported exception",
                    "    IOException; must be caught or declared to be thrown.",
                    "  - Unchecked: compiler nggak memaksa. Golongan ini adalah",
                    "    RuntimeException beserta semua turunannya, termasuk empat contoh di",
                    "    awal materi ini.",
                    "",
                    "Selain Exception, ada juga keluarga Error, misalnya StackOverflowError",
                    "dan OutOfMemoryError. Error nggak termasuk Exception. Error artinya JVM",
                    "sendiri yang bermasalah, jadi nggak untuk ditangkap. Silsilah lengkapnya",
                    "dibahas di materi Membaca Error: Stack Trace, Throwable, dan Logging.",
                    "",
                    "Kamu juga boleh bikin exception sendiri. Caranya, bikin class turunan",
                    "Exception, lalu teruskan pesannya ke constructor induk lewat super:",
                    "",
                    "  class SaldoTidakCukup extends Exception {",
                    "      SaldoTidakCukup(String pesan) { super(pesan); }",
                    "  }",
                    "",
                    "Karena induknya langsung Exception, SaldoTidakCukup termasuk checked.",
                    "Method yang melemparnya wajib menangkapnya sendiri atau menulis throws",
                    "SaldoTidakCukup di kepalanya.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aplikasi bank menolak penarikan yang melebihi saldo, dan aplikasi",
                    "pendaftaran menolak tanggal lahir yang mustahil. Penolakan seperti itu",
                    "ditulis dengan throw di method yang tahu aturannya. Lalu catch",
                    "menangkapnya di bagian yang bisa memberi tahu pengguna.",
                    "",
                    "Kasus kecil: method tarik di aplikasi koperasi sekolah menerima saldo",
                    "Rp150.000 dan jumlah penarikan. Penarikan Rp200.000 harus ditolak",
                    "dengan pesan yang jelas, dan programnya tetap jalan untuk anggota",
                    "berikutnya.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Daftar dulu cara method ini bisa gagal. Jumlah nol atau negatif",
                    "     itu salah pemanggil, jadi pakai IllegalArgumentException. Saldo",
                    "     kurang itu kejadian wajar, jadi pakai SaldoTidakCukup, exception",
                    "     checked buatan sendiri dari materi ini.",
                    "  2. Lempar exception-nya di method yang tahu aturannya:",
                    "      static int tarik(int saldo, int jumlah) throws SaldoTidakCukup {",
                    "          if (jumlah <= 0) throw new IllegalArgumentException(\"jumlah salah\");",
                    "          int kurang = jumlah - saldo;",
                    "          if (kurang > 0) throw new SaldoTidakCukup(\"kurang Rp\" + kurang);",
                    "          return saldo - jumlah;",
                    "      }",
                    "  3. Tangkap di tempat yang bisa ngomong ke pengguna, misalnya layar",
                    "     kasir: catch (SaldoTidakCukup e), lalu tampilkan e.getMessage().",
                    "  4. Uji kasus pinggirnya: menarik tepat Rp150.000 harus boleh, dan",
                    "     saldonya jadi 0. Karena itu syaratnya kurang > 0, dan bukan >= 0.",
                    "",
                    "Jebakan: catch (Exception e) { } yang kosong bikin penarikan gagal",
                    "tanpa jejak. Pengguna mengira uangnya keluar, padahal saldonya nggak",
                    "berubah.",
                ]
            },
        ],
    },
    {
        "title": "22. Membaca Error: Stack Trace, Throwable, dan Logging",
        "sections": [
            {
                "body": [
                    "Materi Exception Handling ngajarin cara menangkap exception. Materi ini",
                    "membahas kebalikannya: apa yang muncul di layar kalau nggak ada yang",
                    "menangkapnya.",
                    "",
                    "Teks itu bakal sering banget kamu lihat sebagai programmer Java. Banyak",
                    "pemula refleks menutup terminalnya. Padahal teks yang barusan muncul itu",
                    "petunjuk paling akurat yang bisa kamu dapat soal apa yang rusak.",
                    "",
                    "Kalau sebuah exception terus naik sampai keluar dari main() tanpa ada",
                    "yang menangkap, JVM menghentikan program, lalu mencetak stack trace.",
                    "Stack trace adalah jejak pemanggilan: daftar method yang sedang berjalan",
                    "waktu error terjadi. Bentuknya seperti ini:",
                    "",
                    "  Exception in thread \"main\" java.lang.NumberFormatException:",
                    "          For input string: \"8.000\"",
                    "      at java.base/java.lang.NumberFormatException.forInputString(",
                    "          NumberFormatException.java:67)",
                    "      at java.base/java.lang.Integer.parseInt(Integer.java:668)",
                    "      at java.base/java.lang.Integer.parseInt(Integer.java:786)",
                    "      at Jejak.hargaDari(Jejak.java:6)",
                    "      at Jejak.totalBelanja(Jejak.java:12)",
                    "      at Jejak.main(Jejak.java:19)",
                    "",
                    "Di layar, baris pertama dan baris forInputString masing-masing tampil",
                    "utuh dalam satu baris panjang. Di sini keduanya dipotong supaya muat.",
                    "",
                    "Ada tiga aturan untuk membacanya:",
                    "  1. Baris pertama menyebut jenis error dan pesannya. Di sini ada teks",
                    "     yang gagal diubah jadi angka, dan teks itu \"8.000\". Bagian",
                    "     'Exception in thread \"main\"' cuma menyebut thread mana yang mati.",
                    "     Thread adalah jalur yang menjalankan kodemu. Program sederhana",
                    "     menjalankan semuanya di thread bernama main.",
                    "  2. Tiap baris 'at ...' adalah satu pemanggilan method yang masih",
                    "     berlangsung waktu error terjadi. Urutannya dari dalam ke luar.",
                    "     Baris paling atas adalah tempat error-nya muncul, baris paling",
                    "     bawah adalah titik berangkatnya. Kalau dibaca dari bawah ke atas,",
                    "     ceritanya jadi utuh: main memanggil totalBelanja, totalBelanja",
                    "     memanggil hargaDari, dan seterusnya.",
                    "  3. Angka sesudah titik dua adalah nomor baris di berkas itu.",
                    "     'Jejak.java:12' artinya buka Jejak.java, lalu lompat ke baris 12.",
                    "",
                    "Sekarang bagian yang paling menentukan: cari baris yang menyebut kodemu",
                    "sendiri. Tiga baris teratas diawali 'java.base/'. Itu isi JDK, kode",
                    "bawaan Java. Membuka Integer.java nggak ada gunanya. parseInt nggak",
                    "rusak, dia cuma melapor bahwa yang kamu kasih bukan angka. Baris pertama",
                    "yang menyebut class milikmu, 'Jejak.hargaDari', itu yang harus kamu",
                    "buka.",
                    "",
                    "Di proyek nyata yang pakai Spring atau Hibernate, satu jejak bisa",
                    "sepanjang 60 baris, dan cuma tiga di antaranya milikmu. Di sini kelihatan",
                    "beda pemula dengan orang yang udah terbiasa: yang udah terbiasa bisa",
                    "memindai 60 baris itu dalam lima detik. Kemampuan itu murni datang dari",
                    "latihan.",
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
                    "Kenapa catch (Exception e) bisa menangkap begitu banyak jenis error?",
                    "Semua error di Java adalah objek, dan objek-objek itu satu keluarga:",
                    "",
                    "  Throwable                    <- akar; cuma ini dan turunannya bisa di-throw",
                    "    |",
                    "    +-- Error                  <- JVM-nya sendiri yang bermasalah",
                    "    |     +-- OutOfMemoryError       memori habis",
                    "    |     +-- StackOverflowError     rekursi tanpa ujung",
                    "    |",
                    "    +-- Exception              <- masalah wajar yang layak ditangani",
                    "          +-- IOException            checked",
                    "          +-- SQLException           checked",
                    "          +-- RuntimeException <- semua turunannya unchecked",
                    "                +-- NullPointerException",
                    "                +-- NumberFormatException",
                    "                +-- ArithmeticException",
                    "                +-- IndexOutOfBoundsException",
                    "",
                    "Pembagian checked dan unchecked dari materi Exception Handling letaknya",
                    "persis di pohon ini. Semua yang ada di bawah RuntimeException itu",
                    "unchecked, jadi compiler diam aja. Sisanya yang ada di bawah Exception",
                    "itu checked. Untuk yang checked, compiler memaksa kamu menangkapnya atau",
                    "menuliskan throws.",
                    "",
                    "catch (Exception e) menyapu seluruh cabang Exception. Jangkauannya lebar",
                    "banget, makanya dipakai kalau kamu memang mau semua exception",
                    "tertangkap. Cabang Error sengaja nggak ikut tertangkap. Menangkap",
                    "OutOfMemoryError lalu melanjutkan program itu sama aja dengan menempel",
                    "lakban di atas lampu peringatan. Memorinya tetap habis, dan blok",
                    "catch-mu nggak bisa memperbaiki apa pun.",
                    "",
                    "Jangan pernah menulis catch (Throwable t). Itu satu-satunya cara ikut",
                    "menelan cabang Error. Kalau bentuk itu muncul di kode orang, hampir",
                    "selalu itu tanda penulisnya menyerah, dan bukan tanda dia berhati-hati.",
                    "",
                    "Sebelum contoh berikutnya, kenalan dulu dengan System.err. System.out",
                    "dan System.err adalah dua aliran keluaran yang terpisah. System.out",
                    "untuk hasil program, System.err untuk keluhan, dan printStackTrace()",
                    "mencetak ke System.err.",
                    "",
                    "Pemisahan ini ada gunanya. Perintah java Laporan > hasil.txt cuma",
                    "menampung System.out ke berkas hasil.txt. Pesan error tetap kelihatan di",
                    "layar dan nggak ikut mengotori berkas hasilnya.",
                    "",
                    "Sebaliknya, kalau keduanya ditampung di tempat yang beda, misalnya",
                    "java Laporan > hasil.txt 2> galat.txt, urutan di antara keduanya",
                    "hilang. Dari dua berkas itu nggak ada lagi cara untuk tahu baris mana",
                    "yang tercetak duluan. Alat yang membaca dua aliran itu dengan penampung",
                    "sementara (buffer) masing-masing juga bisa menampilkannya nggak",
                    "berurutan. Contohnya konsol IDE, atau log CI, yaitu server yang",
                    "menjalankan tes otomatis. Jadi posisi baris error di layar nggak bisa",
                    "dipakai sebagai bukti kapan error itu terjadi.",
                    "",
                    "Di versi web aplikasi ini, keduanya juga dipisah. Waktu kamu menekan",
                    "Jalankan di blok kode, isi System.out tampil di kotak Keluaran,",
                    "sedangkan pesan dari System.err tampil terpisah di bawahnya.",
                ],
            },
            {
                "heading": "Objek e, dan membungkus exception",
                "body": [
                    "e di dalam blok catch adalah nama variabel biasa, isinya sebuah objek",
                    "exception. Namanya boleh kamu ganti, misalnya jadi ex. Method warisan",
                    "Throwable yang paling sering dipakai:",
                    "  - e.getMessage() memberi pesannya aja, tanpa nama class. Hasilnya bisa",
                    "    null, karena banyak exception dilempar tanpa pesan. Akibatnya",
                    "    \"Error: \" + e.getMessage() mencetak \"Error: null\". Kalau itu",
                    "    terjadi, cetak e-nya langsung, karena toString() selalu punya isi.",
                    "  - e.toString() memberi nama class, lalu \": \" dan pesannya. Method ini",
                    "    yang otomatis dipanggil waktu e digabung ke String pakai +.",
                    "  - e.printStackTrace() mencetak seluruh jejak ke System.err.",
                    "  - e.getStackTrace() memberi jejak yang sama dalam bentuk array. Elemen",
                    "    [0] adalah baris teratas, yaitu tempat error-nya muncul.",
                    "  - e.getCause() memberi exception yang jadi penyebabnya, atau null",
                    "    kalau nggak ada.",
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
                    "  Caused by: java.lang.NumberFormatException:",
                    "          For input string: \"delapan puluh\"",
                    "      at java.base/java.lang.NumberFormatException.forInputString(",
                    "          NumberFormatException.java:67)",
                    "      at java.base/java.lang.Integer.parseInt(Integer.java:668)",
                    "      at java.base/java.lang.Integer.parseInt(Integer.java:786)",
                    "      at Konfigurasi.bacaPort(Konfigurasi.java:5)",
                    "      ... 1 more",
                    "",
                    "Sama seperti tadi, dua baris yang dipotong di atas tampil utuh di",
                    "layar.",
                    "",
                    "Jejak ini disebut rantai sebab, dan cara bacanya kebalikan dari dugaan",
                    "kebanyakan orang. Blok paling atas cuma bungkusnya. Kerusakan aslinya",
                    "ada di blok Caused by paling bawah. Kalau ada tiga Caused by bertumpuk,",
                    "yang terakhir yang menyebut penyebab aslinya.",
                    "",
                    "Jadi urutan membacanya begini:",
                    "  1. Baca judul di paling atas untuk tahu apa yang gagal.",
                    "  2. Lompat ke Caused by paling bawah untuk tahu penyebabnya.",
                    "  3. Di blok itu, cari baris yang menyebut kodemu sendiri.",
                    "",
                    "Baris '... 1 more' artinya sisa barisnya sama persis dengan jejak di",
                    "atasnya, jadi nggak dicetak dua kali. Nggak ada yang disembunyikan.",
                    "",
                    "Kenapa exception-nya perlu dibungkus? Pesan 'For input string:",
                    "\"delapan puluh\"' kalau berdiri sendiri nggak ngasih tahu bahwa yang",
                    "gagal itu pemuatan konfigurasi. Teks itu bisa datang dari mana aja.",
                    "Baris ini menambah keterangan tanpa membuang penyebabnya:",
                    "",
                    "  throw new RuntimeException(\"gagal memuat konfigurasi\", e);",
                    "",
                    "Argumen kedua, yaitu e, wajib ditulis. Tanpa e, seluruh blok Caused by",
                    "hilang, dan yang tersisa cuma kalimat sopan tanpa satu pun nomor baris.",
                    "Kesalahan ini yang paling sering bikin sebuah error mustahil dilacak.",
                    "",
                    "Di kode profesional, printStackTrace() hampir nggak pernah dipakai.",
                    "Alasannya:",
                    "  - Hasilnya selalu ke System.err dan nggak bisa dimatikan.",
                    "  - Dia nggak menyebut waktu kejadian maupun class asalnya.",
                    "  - Hasilnya nggak ikut masuk ke berkas log server.",
                    "",
                    "Penggantinya logger, yaitu alat pencatat kejadian di program. Di dunia",
                    "Java, kombinasi yang paling umum SLF4J dan Logback. Bentuknya hampir",
                    "selalu begini:",
                    "",
                    "  private static final Logger log = LoggerFactory.getLogger(Layanan.class);",
                    "",
                    "  } catch (SQLException e) {",
                    "      log.error(\"gagal simpan user {}\", id, e);",
                    "  }",
                    "",
                    "Tanda {} adalah tempat nilai disisipkan, di sini nilai id. Argumen",
                    "terakhir yang bertipe exception nggak mengisi {} mana pun. Argumen itu",
                    "dicetak sebagai stack trace lengkap. Jadi satu baris tadi memberi pesan,",
                    "data, dan jejaknya sekaligus.",
                    "",
                    "Tingkat log, dari yang paling gawat:",
                    "  - error: gagal, ada yang nggak jadi. Manusia perlu tahu.",
                    "  - warn: aneh tapi masih jalan, misalnya percobaan ulang berhasil atau",
                    "    setelan usang.",
                    "  - info: peristiwa normal yang layak dicatat, misalnya aplikasi menyala",
                    "    atau order masuk.",
                    "  - debug: detail untuk menelusuri masalah. Biasanya dimatikan di server",
                    "    produksi.",
                    "",
                    "Ada tiga pola yang pasti kamu temui di kode orang. Ketiganya sebaiknya",
                    "nggak kamu tiru:",
                    "  1. Blok catch kosong:",
                    "       catch (Exception e) { }",
                    "     Error terjadi, nggak ada satu pun jejak, dan program lanjut dengan",
                    "     data yang salah. Dari sinilah datang bug 'entah kenapa datanya",
                    "     hilang', yang bisa makan waktu berhari-hari karena nggak ada apa",
                    "     pun yang bisa dibaca.",
                    "  2. Pesannya dibuang:",
                    "       catch (Exception e) { System.out.println(\"Error!\"); }",
                    "     Tulisan \"Error!\" nggak ngasih tahu apa pun ke siapa pun.",
                    "  3. Menangkap, mencatat, lalu lanjut seolah nggak terjadi apa-apa.",
                    "     Kalau di titik itu kamu nggak bisa memperbaiki keadaannya, lempar",
                    "     ulang exception-nya dengan keterangan tambahan. Jangan ditelan.",
                    "",
                    "Aturan: satu exception cukup ditangani sekali, di tempat yang tahu harus",
                    "berbuat apa. Di tempat lain, biarkan exception itu naik supaya jejaknya",
                    "tetap utuh.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Waktu aplikasi di server error tengah malam, yang tersisa untuk",
                    "programmer cuma isi log: stack trace dan pesan yang dicatat logger.",
                    "Makin cepat jejak itu terbaca, makin cepat penyebabnya ketemu dan",
                    "layanannya jalan lagi.",
                    "",
                    "Kasus kecil: rekap penjualan harian berhenti di tengah jalan. Datanya",
                    "diambil dari berkas yang diisi kasir, dan di layar muncul jejak seperti",
                    "di langkah pertama.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Baca baris pertama. Jenis error-nya NumberFormatException, dan teks",
                    "     yang gagal diubah jadi angka adalah \"Rp12.000\":",
                    "      Exception in thread \"main\" java.lang.NumberFormatException:",
                    "              For input string: \"Rp12.000\"",
                    "          ... tiga baris java.base/ dilewati ...",
                    "          at Rekap.hargaDari(Rekap.java:3)",
                    "          at Rekap.main(Rekap.java:7)",
                    "  2. Lewati baris yang diawali java.base/. Baris pertama yang menyebut",
                    "     class milikmu, Rekap.hargaDari di baris 3, yang harus dibuka.",
                    "  3. Lihat data yang masuk ke baris itu. Ada kasir yang mengetik harga",
                    "     lengkap dengan \"Rp\" dan titik ribuan, jadi parseInt menolaknya.",
                    "  4. Perbaiki dengan merapikan teksnya sebelum diubah: buang \"Rp\" dan",
                    "     titiknya. Kalau exception-nya kamu bungkus ulang, sertakan e",
                    "     sebagai argumen kedua supaya blok Caused by tetap ada.",
                    "  5. Uji ulang dengan tiga bentuk harga: \"12000\", \"Rp12.000\", dan teks",
                    "     kosong. Yang kosong tetap harus ditolak dengan pesan yang jelas.",
                    "",
                    "Jebakan: catch (Exception e) { System.out.println(\"Error!\"); } membuang",
                    "semua petunjuk tadi. Kalau mau mencatat, pakai logger dan sertakan e",
                    "sebagai argumen terakhir, supaya stack trace-nya ikut tercetak.",
                ]
            },
        ],
    },
    {
        "title": "23. Collection Framework",
        "sections": [
            {
                "body": [
                    "Collection Framework adalah kumpulan struktur data siap pakai di paket",
                    "java.util. Struktur data artinya wadah untuk menyimpan banyak nilai",
                    "dengan aturan tertentu. Wadah-wadah ini jadi pengganti array, yang",
                    "ukurannya tetap sejak dibuat.",
                    "",
                    "Ada empat interface utama, masing-masing dengan aturannya sendiri. Di",
                    "tiap butir ada contoh class yang mengimplementasikannya, yaitu wadah",
                    "yang bisa langsung kamu buat pakai new:",
                    "  - List: isinya berurutan dan boleh ada yang kembar. Contohnya",
                    "    ArrayList dan LinkedList.",
                    "  - Set: isinya nggak boleh kembar, dan urutannya nggak dijamin.",
                    "    Contohnya HashSet.",
                    "  - Map: pasangan key dan value. Mirip kamus: tiap kata (key) punya",
                    "    artinya sendiri (value). Contohnya HashMap.",
                    "  - Queue: antrean, yang masuk duluan keluar duluan atau FIFO (First",
                    "    In, First Out). Contohnya ArrayDeque dan LinkedList, dibahas di",
                    "    materi Antrean dan Tumpukan. PriorityQueue juga sebuah Queue, tapi",
                    "    yang keluar duluan elemen yang paling kecil menurut urutannya, dan",
                    "    belum tentu yang masuk duluan.",
                    "",
                    "Yang paling sering dipakai adalah ArrayList, yaitu list yang isinya",
                    "disimpan di array yang bisa membesar sendiri. Cara pakainya:",
                    "",
                    "  import java.util.ArrayList;",
                    "  import java.util.List;",
                    "",
                    "  List<String> nama = new ArrayList<>();",
                    "  nama.add(\"Andi\");        // tambah",
                    "  nama.get(0);             // ambil indeks 0",
                    "  nama.size();             // jumlah elemen",
                    "  nama.remove(0);          // hapus indeks 0",
                    "  nama.contains(\"Andi\");   // cek ada tidak",
                ]
            },
            {
                "body": [
                    "Sebelum lanjut, ada dua simbol asing di baris yang barusan kamu lihat:",
                    "",
                    "  List<String> nama = new ArrayList<>();",
                    "",
                    "Bagian <String> dibaca \"List yang isinya String\". Kurung sudut itu",
                    "ngasih tahu compiler jenis barang apa yang boleh masuk. Manfaatnya",
                    "kelihatan di sini:",
                    "",
                    "  nama.add(\"Andi\");   // OK",
                    "  nama.add(123);      // ditolak saat kompilasi, bukan saat program jalan",
                    "",
                    "Imbalannya, waktu mengambil isinya kamu langsung dapat String, tanpa",
                    "perlu cast. Isi kurung sudutnya bisa diganti sesuai kebutuhan:",
                    "List<Integer>, Set<String>, atau Map<String, Integer>. Map butuh dua",
                    "tipe, yaitu tipe key dan tipe value.",
                    "",
                    "Yang boleh masuk ke kurung sudut cuma tipe objek. List<int> ditolak, dan",
                    "yang benar List<Integer> (lihat materi Kelas Pembungkus & Konversi",
                    "Tipe).",
                    "",
                    "Tanda <> kosong di sebelah kanan namanya diamond operator. Java udah",
                    "tahu tipenya dari sebelah kiri, jadi kamu nggak perlu menulisnya dua",
                    "kali:",
                    "",
                    "  List<String> nama = new ArrayList<String>();   // sah, tapi bertele-tele",
                    "  List<String> nama = new ArrayList<>();         // ini yang ditulis orang",
                    "",
                    "Ada juga kebiasaan yang perlu kamu kenali: List ditulis di kiri,",
                    "ArrayList di kanan. Yang kiri itu interface, yaitu kontraknya. Yang",
                    "kanan implementasinya. Kalau suatu hari ArrayList mau diganti",
                    "LinkedList, cukup satu kata di sebelah kanan yang berubah. Kode lain",
                    "yang memakai variabel itu tetap aman.",
                    "",
                    "Mekanisme kurung sudut ini namanya Generics, dan nanti dibahas di",
                    "materi Generics. Untuk sekarang kamu cukup bisa membacanya.",
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
                    "Kapan pakai yang mana? Ini perbandingan yang paling sering ditanyakan:",
                    "  - ArrayList cepat kalau kamu mengambil isi lewat indeks, tapi lambat",
                    "    kalau harus menyisipkan elemen di tengah.",
                    "  - LinkedList cepat untuk menyisipkan dan menghapus, tapi lambat kalau",
                    "    mengambil isi lewat indeks.",
                    "  - HashMap cepat, tapi urutan isinya nggak menentu.",
                    "  - TreeMap menyimpan isinya terurut (sorted) menurut key, tapi sedikit",
                    "    lebih lambat.",
                    "",
                    "Untuk mengurutkan List, ada dua cara:",
                    "",
                    "  Collections.sort(listAngka);",
                    "  listNama.sort(String::compareTo);",
                    "",
                    "Sejak Java 8 ada juga Stream, cara mengolah data secara deklaratif.",
                    "Artinya kamu cukup menulis apa yang kamu mau, misalnya \"ambil yang",
                    "genap\", tanpa menulis langkah-langkah loop-nya sendiri:",
                    "",
                    "  List<Integer> genap = list.stream()",
                    "      .filter(n -> n % 2 == 0)",
                    "      .collect(Collectors.toList());",
                    "",
                    "Terus terang aja, tiga bentuk di beberapa baris terakhir ini sengaja",
                    "ditunjukkan sekarang supaya kamu mengenalinya. Kamu belum perlu",
                    "memahaminya:",
                    "",
                    "  String::compareTo    method reference (materi Lambda Expression)",
                    "  n -> n % 2 == 0      lambda           (materi Lambda Expression)",
                    "  .stream()...collect  Stream API       (materi Stream API, nanti)",
                    "",
                    "Ketiganya dijelaskan tuntas di materi-materi berikutnya. Kalau bagian",
                    "akhir ini terasa melompat, memang begitu, dan itu bukan karena kamu",
                    "ketinggalan sesuatu.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Keranjang belanja di toko online bentuknya List, karena urutan dan",
                    "jumlah barangnya penting. Daftar kota tujuan pengiriman bentuknya Set,",
                    "karena satu kota cukup tercatat sekali. Harga per kode barang bentuknya",
                    "Map. Memilih wadah yang pas sering jadi separuh penyelesaian masalahnya.",
                    "",
                    "Kasus kecil: pembina ekskul punya daftar hadir tiga pertemuan dalam",
                    "bentuk List<String>. Banyak nama muncul di lebih dari satu pertemuan.",
                    "Sekolah minta jumlah siswa yang pernah hadir paling nggak sekali.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Masukannya tiga List nama, keluarannya satu angka. Nama yang muncul",
                    "     berkali-kali cuma boleh dihitung sekali.",
                    "  2. \"Nggak boleh kembar\" itu ciri Set, jadi kumpulkan semuanya ke",
                    "     HashSet:",
                    "      Set<String> pernahHadir = new HashSet<>();",
                    "      for (String n : pertemuan1) pernahHadir.add(n);",
                    "      for (String n : pertemuan2) pernahHadir.add(n);",
                    "      for (String n : pertemuan3) pernahHadir.add(n);",
                    "      System.out.println(pernahHadir.size() + \" siswa\");",
                    "  3. Uji dengan data kecil yang jawabannya kamu tahu: [Andi, Budi],",
                    "     [Budi, Citra], dan [Andi] harus menghasilkan 3 siswa.",
                    "  4. Cek kasus pinggirnya: \"Andi\" dan \"andi \" dihitung dua orang oleh",
                    "     Set. Rapikan dulu tiap nama sebelum dimasukkan: buang spasinya",
                    "     dengan trim(), dan samakan huruf besar-kecilnya.",
                    "",
                    "Ingat: HashSet nggak menjamin urutan. Kalau daftar namanya mau dicetak",
                    "urut abjad, salin dulu ke List, lalu urutkan dengan Collections.sort.",
                ]
            },
        ],
    },
    {
        "title": "24. Iterasi, Perubahan, dan Idiom Collection Modern",
        "sections": [
            {
                "body": [
                    "Materi Collection Framework mengenalkan List, Set, dan Map. Materi ini",
                    "membahas apa yang terjadi begitu kamu mulai mengolah isinya, yaitu",
                    "menelusurinya dan mengubahnya sambil ditelusuri. Ada juga beberapa idiom",
                    "yang dipakai di hampir semua kode Java nyata, tapi nggak pernah muncul",
                    "di buku pengantar.",
                    "",
                    "Cara kerja for-each",
                    "",
                    "  for (String b : buah) { ... }",
                    "",
                    "Loop ini nggak cuma bisa dipakai untuk List. Dia bisa dipakai untuk apa",
                    "pun yang mengimplementasikan interface Iterable. Iterable cuma",
                    "menjanjikan satu method, yaitu iterator(). Iterator sendiri semacam",
                    "penunjuk yang berjalan dari satu elemen ke elemen berikutnya. Dia punya",
                    "tiga method inti: hasNext(), next(), dan remove().",
                    "",
                    "Compiler menerjemahkan for-each di atas jadi persis loop ini:",
                    "",
                    "  for (Iterator<String> it = buah.iterator(); it.hasNext(); ) {",
                    "      String b = it.next();",
                    "      ...",
                    "  }",
                    "",
                    "Jadi for-each cuma singkatan, dan mekanismenya sama dengan loop di atas.",
                    "Bentuk panjang ini masih sering dipakai di kode nyata, karena cuma lewat",
                    "bentuk ini kamu bisa memegang iterator-nya. Iterator itulah yang kamu",
                    "butuhkan kalau mau menghapus elemen di tengah jalan.",
                    "",
                    "Bagian ketiga for-nya kosong (it.hasNext(); ). Yang memajukan posisi",
                    "adalah it.next(), dan bukan i++. Kalau kamu menulis it.next() dua kali",
                    "dalam satu putaran, satu elemen terlewat. Salah ketik seperti ini susah",
                    "kelihatan.",
                    "",
                    "ConcurrentModificationException",
                    "",
                    "Kalau kamu memanggil list.remove(...) atau list.add(...) selagi",
                    "for-each atas list itu masih berjalan, Java melempar",
                    "ConcurrentModificationException, yang sering disingkat CME.",
                    "",
                    "Namanya menyesatkan. Kata Concurrent bikin orang mengira ini soal",
                    "thread, padahal error ini juga muncul di program satu thread yang",
                    "tenang-tenang aja. Concurrent di sini artinya koleksinya berubah",
                    "bersamaan dengan iterasinya. Jadi kalau kamu mencari error ini dan",
                    "hasilnya penuh artikel soal multithreading, kamu nggak salah cari.",
                    "Namanya yang memang mengecoh.",
                    "",
                    "Mekanismenya begini. ArrayList menyimpan penghitung bernama modCount,",
                    "yang naik tiap kali ada elemen yang ditambah atau dihapus. Iterator",
                    "mencatat nilai modCount waktu dia dibuat, lalu membandingkannya tiap",
                    "kali next() dipanggil. Kalau nilainya beda, berarti ada yang mengubah",
                    "list di luar sepengetahuannya, dan iterator langsung melempar exception.",
                    "Cara ini disebut deteksi fail-fast, artinya cepat gagal: lebih baik",
                    "program berhenti dengan jelas daripada melompati elemen tanpa ketahuan.",
                    "",
                    "Jebakan: kadang exception-nya nggak muncul. Kalau yang kamu hapus elemen",
                    "kedua dari belakang, posisi iterator (namanya cursor) jadi sama dengan",
                    "size list yang baru. hasNext() langsung bernilai false, dan loop",
                    "berhenti sebelum sempat memeriksa. Elemen terakhir nggak pernah dilihat,",
                    "dan nggak ada satu pun pesan error. Jadi jangan menyimpulkan kodemu aman",
                    "cuma karena nggak ada error. Uji dengan data yang lebih panjang.",
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
                    "  - removeIf(...) jadi pilihan pertama. Paling pendek, paling jelas, dan",
                    "    paling susah salah.",
                    "  - it.remove() dipakai kalau syarat hapusnya rumit, atau kamu juga",
                    "    perlu mengganti isi elemen lewat it.set(...). Untuk it.set(...),",
                    "    iterator-nya harus ListIterator, yang didapat dari",
                    "    list.listIterator().",
                    "  - Salin dulu dipakai kalau di dalam loop kamu juga mengubah list lain,",
                    "    atau menambah elemen. it.remove() cuma bisa menghapus, nggak bisa",
                    "    menambah.",
                    "",
                    "Dua jebakan kecil pada it.remove():",
                    "  - Dia menghapus elemen yang baru aja dikembalikan next(). Kalau",
                    "    dipanggil sebelum next() pernah dipanggil, hasilnya",
                    "    IllegalStateException, dan bukan ConcurrentModificationException.",
                    "  - Dia cuma boleh dipanggil sekali untuk tiap next().",
                    "",
                    "Method Map pengganti cara buku teks",
                    "",
                    "Pola \"cek dulu, baru isi\" diajarkan di mana-mana:",
                    "",
                    "  if (map.containsKey(k)) {",
                    "      map.put(k, map.get(k) + 1);",
                    "  } else {",
                    "      map.put(k, 1);",
                    "  }",
                    "",
                    "Sejak Java 8, pola ini udah nggak ditulis lagi. Map-nya ditelusuri dua",
                    "kali (containsKey, lalu get), jadi boros, dan bentuk if-else-nya bikin",
                    "maksudnya tenggelam. Penggantinya:",
                    "  - map.getOrDefault(k, bawaan) memberi nilai k, atau bawaan kalau k",
                    "    nggak ada. Method ini nggak menulis apa pun ke map.",
                    "  - map.putIfAbsent(k, nilai) mengisi kalau k belum ada. Kalau udah",
                    "    ada, isinya dibiarkan. Yang dikembalikan nilai lama, atau null",
                    "    kalau k baru.",
                    "  - map.computeIfAbsent(k, k -> ...) mirip putIfAbsent, tapi nilainya",
                    "    baru dibuat kalau perlu. Yang dikembalikan selalu nilai yang ada di",
                    "    map.",
                    "  - map.computeIfPresent(k, (k,v) -> ...) mengubah nilai cuma kalau k",
                    "    udah ada.",
                    "  - map.merge(k, nilaiAwal, (lama, baru) -> ...) memakai nilaiAwal",
                    "    kalau k belum ada. Kalau udah ada, fungsi penggabungnya yang",
                    "    dijalankan.",
                    "",
                    "Beda putIfAbsent dan computeIfAbsent sering bikin bingung. putIfAbsent",
                    "selalu membuat objek argumennya, walaupun nanti objek itu dibuang.",
                    "computeIfAbsent baru menjalankan lambda-nya kalau key-nya memang",
                    "kosong. Untuk new ArrayList<>() bedanya sepele, tapi untuk sesuatu yang",
                    "mahal dibuat, bedanya kerasa.",
                    "",
                    "Ingat: di compute* dan merge, fungsi yang mengembalikan null artinya",
                    "key itu dihapus dari map, dan null-nya nggak disimpan. Perilaku ini",
                    "sering dipakai dengan sengaja. Tapi kalau kamu nggak tahu, entri yang",
                    "hilang sendiri itu bikin bingung.",
                    "",
                    "Menelusuri Map",
                    "",
                    "Ada tiga pintu untuk menelusuri isi Map, ditambah forEach:",
                    "",
                    "  map.keySet()    Set berisi semua key.",
                    "  map.values()    Collection berisi semua value (boleh ada duplikat).",
                    "  map.entrySet()  Set berisi pasangan Map.Entry; e.getKey(), e.getValue().",
                    "  map.forEach((k, v) -> ...)  tanpa loop sama sekali.",
                    "",
                    "Ada yang jarang disadari orang: ketiga pintu itu adalah view, yaitu",
                    "jendela ke isi map yang asli, dan bukan salinan. Jadi",
                    "map.keySet().remove(\"a\") ikut menghapus entri \"a\" dari map-nya, dan",
                    "e.setValue(x) di dalam loop entrySet menulis balik ke map.",
                    "",
                    "Kalau kamu butuh key sekaligus value-nya, entrySet lebih hemat daripada",
                    "keySet yang diikuti map.get(k) untuk tiap key. Cara kedua itu mencari",
                    "dua kali.",
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
                    "Coba lihat lagi baris ini dari contoh di atas:",
                    "",
                    "  grup.computeIfAbsent(n.charAt(0), k -> new ArrayList<>()).add(n)",
                    "",
                    "Baris itu mengerjakan dua hal sekaligus. Pertama, memastikan ada List",
                    "di key itu. Kedua, langsung menambah n ke List yang dikembalikannya.",
                    "Bentuk ini ada di mana-mana, jadi begitu kamu mengenalinya, kode",
                    "pengolahan data Java jadi jauh lebih gampang dibaca. Stream API punya",
                    "Collectors.groupingBy untuk pekerjaan yang sama, dan nanti dibahas di",
                    "materi Stream API.",
                    "",
                    "Koleksi yang nggak bisa diubah",
                    "",
                    "Bagian ini menjawab satu baris yang tadi lewat begitu aja. Di materi",
                    "Collection Framework ada baris ini:",
                    "",
                    "  List<String> buah = new ArrayList<>(List.of(\"Apel\", \"Mangga\", \"Jeruk\"));",
                    "",
                    "Kenapa List.of(...) dibungkus new ArrayList<>? List.of(...)",
                    "menghasilkan koleksi immutable, artinya isinya terkunci selamanya.",
                    "Kalau baris itu kamu sederhanakan jadi List<String> buah = List.of(...)",
                    "lalu kamu panggil buah.add(\"Durian\"), program berhenti saat dijalankan:",
                    "",
                    "  Exception in thread \"main\" java.lang.UnsupportedOperationException",
                    "",
                    "Pesannya nggak menyebut List.of sama sekali, jadi penyebabnya hampir",
                    "nggak kelihatan. Sekarang kamu tahu: kalau UnsupportedOperationException",
                    "muncul pada sebuah koleksi, hampir selalu artinya kamu mencoba mengubah",
                    "sesuatu yang memang nggak bisa diubah.",
                    "",
                    "Semua bentuk di bawah ini immutable. Kalau isinya dicoba diubah lewat",
                    "add, remove, set, atau removeIf, yang muncul",
                    "UnsupportedOperationException:",
                    "",
                    "  List.of(...)   Set.of(...)   Map.of(...)   List.copyOf(...)",
                    "  Collections.emptyList()      Collections.singletonList(x)",
                    "  Collections.unmodifiableList(lain)",
                    "",
                    "Ada satu pengecualian kecil: remove dan removeIf pada",
                    "Collections.emptyList() cuma mengembalikan false, karena memang nggak",
                    "ada yang bisa dihapus.",
                    "",
                    "List.of dan Map.of punya dua aturan tambahan yang sering bikin kaget.",
                    "Elemennya nggak boleh null, karena langsung NullPointerException. Lalu",
                    "Map.of dengan key kembar langsung melempar IllegalArgumentException.",
                    "ArrayList dan HashMap membolehkan keduanya.",
                    "",
                    "Di antara dua kutub itu ada Arrays.asList(\"a\", \"b\"), yang udah kamu",
                    "temui di materi Array. Hasilnya list setengah jalan: ukurannya",
                    "terkunci, tapi isinya boleh ditimpa. Dia juga bukan ArrayList yang",
                    "biasa. Yang setengah-setengah begini justru paling membingungkan. Kalau",
                    "kamu butuh list yang bisa tumbuh, bungkus juga:",
                    "new ArrayList<>(Arrays.asList(...)).",
                    "",
                    "Lalu kenapa koleksi immutable tetap dipakai? Justru kunci itulah",
                    "gunanya. Koleksi yang nggak bisa diubah aman dibagi ke mana-mana, tanpa",
                    "takut ada yang mengubahnya di luar sepengetahuanmu. Dari situ lahir pola",
                    "yang sering banget kamu lihat di getter:",
                    "",
                    "  private final List<String> anggota = new ArrayList<>();",
                    "",
                    "  public List<String> getAnggota() {",
                    "      // atau: return List.copyOf(anggota);",
                    "      return Collections.unmodifiableList(anggota);",
                    "  }",
                    "",
                    "Tanpa pembungkus itu, siapa pun yang memanggil getAnggota() bisa",
                    "memanggil .add() dan menembus encapsulation yang udah susah payah kamu",
                    "bangun. Field-nya memang private, tapi isinya terbuka lebar.",
                    "",
                    "Dua pilihan tadi bedanya penting. unmodifiableList adalah view, jadi",
                    "kalau list aslinya berubah, hasilnya ikut berubah. List.copyOf adalah",
                    "salinan, yang membeku pada keadaan saat itu.",
                    "",
                    "Terakhir, beberapa method Collections lain yang sering kamu lihat:",
                    "  - Collections.shuffle(list) mengacak urutan. Hasilnya beda tiap kali",
                    "    program dijalankan.",
                    "  - Collections.swap(list, i, j) menukar isi dua posisi.",
                    "  - Collections.emptyList() memberi List kosong yang immutable. Biasanya",
                    "    dipakai sebagai nilai kembalian yang artinya \"nggak ada\".",
                    "  - Collections.singletonList(x) memberi List berisi tepat satu elemen.",
                    "",
                    "Sejak Java 8, List juga punya method sort(pembanding) sendiri.",
                    "list.sort(null) artinya \"urutkan dengan urutan alaminya\", sama dengan",
                    "Collections.sort(list).",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Laporan penjualan harian, rekap absensi per kelas, dan jumlah pesanan",
                    "per kurir punya bentuk yang sama: menghitung atau mengelompokkan isi",
                    "sebuah daftar ke dalam Map. Di kode Java sungguhan, pekerjaan itu",
                    "biasanya ditulis dengan merge dan computeIfAbsent.",
                    "",
                    "Kasus kecil: mesin kasir kafe mencatat tiap menu yang terjual hari ini:",
                    "kopi, teh, kopi, roti, kopi, teh. Pemilik kafe mau tahu jumlah terjual",
                    "per menu dan menu yang paling laku.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Masukannya satu List<String>. Keluarannya Map dari nama menu ke",
                    "     jumlahnya, ditambah satu nama menu terlaris.",
                    "  2. Hitung frekuensinya dengan merge. TreeMap dipakai supaya urutan",
                    "     cetaknya pasti, dan hasilnya {kopi=3, roti=1, teh=2}:",
                    "      Map<String, Integer> laku = new TreeMap<>();",
                    "      for (String m : terjual) laku.merge(m, 1, Integer::sum);",
                    "  3. Cari yang terbesar dengan menelusuri key-nya satu per satu:",
                    "      String terlaris = \"\";",
                    "      for (String m : laku.keySet()) {",
                    "          if (laku.get(m) > laku.getOrDefault(terlaris, 0)) terlaris = m;",
                    "      }",
                    "  4. Cek kasus pinggirnya. Kalau dua menu sama larisnya, tanda > memilih",
                    "     yang ketemu duluan menurut urutan abjad TreeMap. Kalau hari ini",
                    "     belum ada penjualan, terlaris tetap \"\", jadi tampilkan kalimat",
                    "     \"belum ada penjualan\".",
                    "",
                    "Jebakan: menghapus entri lewat laku.remove(...) di dalam for-each atas",
                    "map yang sama berujung ConcurrentModificationException. Pakai",
                    "laku.values().removeIf(n -> n < 2) atau iterator-nya.",
                ]
            },
        ],
    },
    {
        "title": "25. Antrean dan Tumpukan: Queue, Deque, dan ArrayDeque",
        "sections": [
            {
                "body": [
                    "Materi Collection Framework mengenalkan List, Set, dan Map. Ketiganya",
                    "menjawab kebutuhan \"simpan banyak nilai\". Materi ini membahas bentuk",
                    "keempat: koleksi yang isinya keluar-masuk terus, dan nggak cuma",
                    "disimpan lalu dibaca.",
                    "",
                    "Sesudah materi ini kamu bisa:",
                    "  - membedakan antrean (FIFO) dari tumpukan (LIFO), dan tahu kapan butuh",
                    "    yang mana;",
                    "  - memakai ArrayDeque untuk keduanya;",
                    "  - tahu method mana yang melempar exception waktu koleksinya kosong,",
                    "    dan mana yang mengembalikan null. Bedanya cuma kerasa persis saat",
                    "    kosong.",
                    "",
                    "Kenapa nggak pakai ArrayList aja?",
                    "",
                    "ArrayList bisa dipakai untuk meniru antrean. Tambah di belakang pakai",
                    "add(x), ambil dari depan pakai remove(0). Hasilnya jalan, dan untuk",
                    "sepuluh elemen nggak ada yang terasa lambat.",
                    "",
                    "Masalahnya nggak kelihatan. remove(0) harus menggeser seluruh sisa",
                    "isinya satu langkah ke kiri, karena elemen ArrayList wajib duduk rapat",
                    "mulai dari indeks 0. Mengambil satu orang dari depan antrean berisi",
                    "seribu orang berarti 999 kali pemindahan, untuk pekerjaan yang",
                    "seharusnya cukup sekali sentuh.",
                    "",
                    "ArrayDeque nggak menyimpan isinya rapat dari indeks 0. Dia menyimpan",
                    "dua penanda: mana ujung depan, mana ujung belakang. Menambah atau",
                    "mengambil di kedua ujung cukup menggeser penandanya. Nggak ada isi yang",
                    "ikut dipindahkan.",
                    "",
                    "FIFO dan LIFO: satu class, dua perilaku",
                    "",
                    "Ada dua cara antre yang perlu kamu bedakan:",
                    "  - FIFO (First In, First Out): yang masuk duluan keluar duluan.",
                    "    Contohnya antrean kasir, yang datang duluan dilayani duluan.",
                    "  - LIFO (Last In, First Out): yang masuk terakhir keluar duluan.",
                    "    Contohnya tumpukan piring, yang ditaruh terakhir diambil duluan.",
                    "",
                    "Deque dibaca \"dek\", singkatan dari double ended queue, artinya antrean",
                    "berujung dua. Karena Deque bisa menambah dan mengambil di kedua ujung,",
                    "satu class yang sama bisa melayani dua-duanya:",
                    "",
                    "  antrean  : masuk di belakang (addLast),  keluar dari depan (removeFirst)",
                    "  tumpukan : masuk di depan    (addFirst), keluar dari depan (removeFirst)",
                    "",
                    "Yang berubah cuma ujung masuknya, sedangkan keluarnya sama-sama dari",
                    "depan. Beda antrean dan tumpukan cuma itu.",
                    "",
                    "Queue atau Deque?",
                    "",
                    "Queue adalah interface yang lebih tua dan lebih sempit. Dia cuma",
                    "menjanjikan satu ujung masuk dan satu ujung keluar. Deque memperluasnya",
                    "dengan ujung kedua, jadi setiap Deque otomatis juga sebuah Queue.",
                    "",
                    "Untuk kode baru, tulis tipenya Deque dan isinya new ArrayDeque<>().",
                    "Kebiasaan menulis interface di kiri dan implementasi di kanan berlaku",
                    "sama seperti pada List dan ArrayList.",
                ],
            },
            {
                "heading": "Antrean dan tumpukan dari satu kelas yang sama",
                "code": """import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        // ANTREAN (FIFO): masuk di belakang, keluar dari depan.
        Deque<String> antrean = new ArrayDeque<>();
        antrean.addLast("Ani");                    // datang pertama
        antrean.addLast("Budi");
        antrean.addLast("Cici");
        System.out.println("Antrean : " + antrean);
        System.out.println("Dilayani: " + antrean.removeFirst());
        System.out.println("Berikut : " + antrean.peekFirst());   // dilihat, tidak diambil
        System.out.println("Sisa    : " + antrean);

        // TUMPUKAN (LIFO): masuk di DEPAN, keluar juga dari depan.
        Deque<String> tumpukan = new ArrayDeque<>();
        tumpukan.addFirst("piring 1");
        tumpukan.addFirst("piring 2");
        tumpukan.addFirst("piring 3");
        System.out.println();
        System.out.println("Tumpukan: " + tumpukan);
        System.out.println("Diambil : " + tumpukan.removeFirst());
        System.out.println("Sisa    : " + tumpukan);

        // SAAT KOSONG: dua cara bertanya, dua akibat yang berbeda.
        Deque<String> habis = new ArrayDeque<>();
        System.out.println();
        System.out.println("peekFirst() saat kosong: " + habis.peekFirst());
        try {
            habis.removeFirst();
        } catch (java.util.NoSuchElementException e) {
            System.out.println("removeFirst() saat kosong: " + e.getClass().getSimpleName());
        }

        // Dipakai sebagai loop: selama masih ada yang antre, layani.
        Deque<String> loket = new ArrayDeque<>(List.of("Dita", "Eka", "Fajar"));
        System.out.println();
        while (!loket.isEmpty()) {
            System.out.println("Memanggil: " + loket.removeFirst());
        }

        // Pembanding: ArrayList memang bisa, tapi remove(0) menggeser sisanya.
        List<Integer> daftar = new ArrayList<>(List.of(1, 2, 3, 4, 5));
        daftar.remove(0);
        System.out.println();
        System.out.println("ArrayList setelah remove(0): " + daftar);
    }
}""",
            },
            {
                "body": [
                    "Tiga pasang method, dan bedanya baru kerasa waktu kosong",
                    "",
                    "Tiap pekerjaan punya dua versi method. Versi pertama berhenti keras",
                    "dengan exception, versi kedua mengembalikan penanda:",
                    "",
                    "                    berhenti keras        mengembalikan penanda",
                    "  masuk depan       addFirst(x)           offerFirst(x)  -> boolean",
                    "  masuk belakang    addLast(x)            offerLast(x)   -> boolean",
                    "  keluar depan      removeFirst()         pollFirst()    -> null kalau kosong",
                    "  keluar belakang   removeLast()          pollLast()     -> null kalau kosong",
                    "  lihat depan       getFirst()            peekFirst()    -> null kalau kosong",
                    "  lihat belakang    getLast()             peekLast()     -> null kalau kosong",
                    "",
                    "Selama koleksinya ada isinya, kolom kiri dan kanan berperilaku persis",
                    "sama. Bedanya muncul tepat waktu kosong: removeFirst() melempar",
                    "NoSuchElementException, sedangkan pollFirst() mengembalikan null dan",
                    "program jalan terus.",
                    "",
                    "Mana yang dipakai tergantung arti \"kosong\" di programmu:",
                    "  - Kalau kosong berarti ada yang salah di programmu, pakai",
                    "    removeFirst(). Biarkan program berhenti tepat di tempat",
                    "    kesalahannya, bukan beberapa baris sesudahnya.",
                    "  - Kalau kosong adalah keadaan yang wajar (\"belum ada yang antre\"),",
                    "    pakai pollFirst() atau peekFirst(), lalu periksa null-nya.",
                    "",
                    "Bentuk yang paling sering ditulis justru menghindari keduanya:",
                    "",
                    "  while (!antrean.isEmpty()) {",
                    "      String orang = antrean.removeFirst();",
                    "      ...",
                    "  }",
                    "",
                    "isEmpty() udah menjamin antreannya ada isinya, jadi removeFirst() di",
                    "situ nggak akan pernah melempar apa pun.",
                    "",
                    "Jebakan: ArrayDeque nggak boleh berisi null. Baris di bawah ini langsung",
                    "melempar NullPointerException:",
                    "",
                    "  antrean.addLast(null);   // NullPointerException, langsung",
                    "",
                    "Larangan ini ada alasannya. peekFirst() memakai null untuk berarti",
                    "\"kosong\". Kalau null boleh ikut disimpan, hasil null nggak bisa lagi",
                    "dibedakan: antreannya kosong, atau elemen di depan memang null?",
                    "Larangan di sisi masuk menutup kebingungan itu di sisi keluar.",
                    "ArrayList nggak punya masalah ini, jadi ArrayList boleh berisi null.",
                    "Perbedaan ini gampang bikin kaget.",
                    "",
                    "Jangan pakai class Stack. Java punya java.util.Stack sejak versi paling",
                    "awal, dan namanya bikin orang mengira itulah cara bikin tumpukan. Ada",
                    "dua alasan untuk menghindarinya:",
                    "  - Stack mewarisi Vector, yang setiap method-nya synchronized, yaitu",
                    "    dikunci supaya cuma satu thread yang bisa masuk dalam satu waktu.",
                    "    Programmu tetap membayar ongkos penguncian itu walaupun cuma",
                    "    berjalan di satu thread.",
                    "  - Iterasinya berjalan dari dasar tumpukan ke atas, berlawanan dengan",
                    "    urutan pengambilan pop(). Mencetak sebuah Stack memberi urutan yang",
                    "    beda dari urutan isinya keluar, dan salah paham seperti ini susah",
                    "    dilacak.",
                    "",
                    "Dokumentasi Java sendiri menyarankan Deque sebagai penggantinya.",
                    "",
                    "Di mana bentuk ini dipakai:",
                    "  - Simulasi: siapa yang menunggu dilayani lebih dulu (antrean loket,",
                    "    lift, printer).",
                    "  - Undo: langkah terakhir dibatalkan lebih dulu (tumpukan).",
                    "  - Menelusuri peta atau jaringan lapis demi lapis (antrean), lawan dari",
                    "    menelusuri sedalam-dalamnya dulu (tumpukan).",
                    "  - Memeriksa tanda kurung seimbang: setiap kurung buka ditumpuk, setiap",
                    "    kurung tutup mengambil satu dari tumpukan.",
                    "",
                    "Begitu sebuah program harus meniru sesuatu yang berjalan, dan nggak",
                    "cuma menghitung sekumpulan angka, hampir selalu ada antrean di",
                    "dalamnya.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Tombol urungkan (undo) di aplikasi kasir dan tombol kembali di browser",
                    "bekerja dengan tumpukan: yang terakhir masuk, itu yang pertama",
                    "dibatalkan. Antrean puskesmas dan antrean cetak printer kebalikannya,",
                    "yang datang duluan dilayani duluan. Keduanya bisa ditulis dengan",
                    "ArrayDeque.",
                    "",
                    "Kasus kecil: kasir memindai mi instan, lalu gula 1 kg, lalu sadar gula",
                    "itu salah. Tombol urungkan harus membatalkan gula dulu. Kalau ditekan",
                    "lagi, giliran mi instan. Kalau ditekan sekali lagi, layar cukup bilang",
                    "nggak ada yang bisa dibatalkan.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Yang dibatalkan selalu aksi terakhir, jadi ini tumpukan (LIFO).",
                    "  2. Pakai Deque. Tiap aksi masuk di depan dengan addFirst, dan tombol",
                    "     urungkan mengambil dari depan juga.",
                    "  3. Riwayat kosong itu keadaan wajar, jadi pakai pollFirst, yang",
                    "     mengembalikan null alih-alih melempar exception:",
                    "      Deque<String> riwayat = new ArrayDeque<>();",
                    "      riwayat.addFirst(\"scan mi instan\");",
                    "      riwayat.addFirst(\"scan gula 1 kg\");",
                    "      System.out.println(riwayat.pollFirst());   // scan gula 1 kg",
                    "      System.out.println(riwayat.pollFirst());   // scan mi instan",
                    "      System.out.println(riwayat.pollFirst());   // null",
                    "  4. Uji kasus pinggirnya: tekan urungkan sebelum ada barang yang",
                    "     dipindai. Hasilnya harus null, layar menampilkan pesan, dan",
                    "     programnya nggak boleh berhenti.",
                    "",
                    "Jebakan: jangan pakai class Stack untuk riwayat ini. Kalau dicetak,",
                    "urutan isinya berlawanan dengan urutan keluarnya, dan tiap method-nya",
                    "tetap membayar ongkos synchronized.",
                ]
            },
        ],
    },
    {
        "title": "26. String & Scanner (Input)",
        "sections": [
            {
                "body": [
                    "String adalah teks, yaitu deretan karakter. Di Java, String itu objek",
                    "yang nggak bisa diubah (immutable). Method yang kelihatannya mengubah",
                    "String, seperti toUpperCase(), selalu menghasilkan String baru. String",
                    "yang lama tetap apa adanya.",
                    "",
                    "Untuk membaca masukan dari keyboard, pakai Scanner:",
                    "",
                    "  import java.util.Scanner;",
                    "  Scanner sc = new Scanner(System.in);",
                    "  int umur = sc.nextInt();",
                    "  String nama = sc.nextLine();",
                    "  double tinggi = sc.nextDouble();",
                    "",
                    "System.in adalah masukan standar program, biasanya ketikan dari",
                    "keyboard. nextInt() membaca satu bilangan bulat, nextLine() membaca",
                    "satu baris teks, dan nextDouble() membaca satu bilangan desimal.",
                    "",
                    "Jebakan: sc.nextInt() nggak ikut membaca Enter di ujung baris. Kalau",
                    "sesudahnya kamu langsung memanggil sc.nextLine(), yang terbaca cuma",
                    "sisa baris itu, jadi hasilnya string kosong. Solusinya, panggil",
                    "sc.nextLine() sekali sesudah nextInt() untuk membuang sisa baris",
                    "tersebut.",
                    "",
                    "Method String yang sering dipakai:",
                    "  - length() memberi jumlah karakternya.",
                    "  - charAt(i) memberi karakter di indeks i, yang dihitung mulai dari 0.",
                    "  - substring(a,b) memberi potongan dari indeks a sampai sebelum indeks",
                    "    b.",
                    "  - toUpperCase() dan toLowerCase() mengubah semua huruf jadi besar atau",
                    "    jadi kecil.",
                    "  - trim() membuang spasi di awal dan di akhir teks.",
                    "  - split(\",\") memecah teks jadi array di setiap koma.",
                    "  - replace() mengganti potongan teks dengan teks lain.",
                    "  - equals() dan equalsIgnoreCase() membandingkan isi dua teks.",
                    "  - contains() dan startsWith() mengecek apakah teks memuat, atau",
                    "    diawali, potongan tertentu.",
                    "  - indexOf() memberi posisi pertama sebuah potongan, atau -1 kalau",
                    "    nggak ketemu.",
                    "  - String.format(\"Halo %s umur %d\", nama, umur) bikin String dari",
                    "    sebuah cetakan. Cara kerjanya dibahas di bawah.",
                    "",
                    "Program contoh di bawah butuh masukan. Di versi web, tombol Jalankan",
                    "nggak punya kotak masukan, jadi programnya berhenti dengan",
                    "NoSuchElementException. Untuk mencobanya, buka lewat tombol Ruang Coba",
                    "di sebelahnya, lalu isi kotak \"Masukan program (stdin)\", misalnya",
                    "dengan dua baris ini:",
                    "",
                    "  Andi",
                    "  20",
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
                    "Untuk membandingkan isi String, pakai .equals(), dan jangan pakai ==.",
                    "Operator == membandingkan alamat objeknya (referensi), dan nggak",
                    "melihat isinya:",
                    "",
                    "  \"Andi\".equals(\"Andi\")          -> true",
                    "  \"Andi\" == \"Andi\"               -> true, karena dua-duanya objek yang sama",
                    "  new String(\"Andi\") == \"Andi\"   -> false, padahal isinya sama",
                    "",
                    "Java menyimpan teks yang ditulis langsung di kode cukup satu kali,",
                    "jadi dua tulisan \"Andi\" di atas menunjuk objek yang sama, dan ==",
                    "memberi true. Begitu salah satunya dibuat waktu program berjalan,",
                    "misalnya dari Scanner atau hasil penggabungan teks, == bisa memberi",
                    "false walaupun isinya sama persis. Hasil yang kadang true kadang false",
                    "itu yang bikin == menipu.",
                    "",
                    "Kalau besar-kecil huruf nggak penting, pakai .equalsIgnoreCase():",
                    "",
                    "  \"Andi\".equalsIgnoreCase(\"ANDI\")   -> true",
                    "",
                    "Kalau kamu perlu mengubah teks berkali-kali, misalnya menyambung teks",
                    "di dalam loop, pakai StringBuilder atau StringBuffer. String itu",
                    "immutable, jadi setiap perubahan menghasilkan objek baru, dan itu",
                    "mahal. StringBuilder lebih cepat, tapi nggak thread-safe, artinya",
                    "nggak aman dipakai beberapa thread sekaligus. StringBuffer aman untuk",
                    "itu, tapi lebih lambat.",
                    "",
                    "  StringBuilder sb = new StringBuilder();",
                    "  sb.append(\"Halo\"); sb.append(\" Dunia\");",
                    "  String hasil = sb.toString();",
                ]
            },
            {
                "body": [
                    "printf artinya mencetak pakai cetakan. Baris String.format di daftar",
                    "tadi lewat begitu aja, padahal alat ini yang pertama kamu butuhkan",
                    "begitu program menampilkan uang, persen, atau rata-rata. Tanpa",
                    "cetakan, rata-rata tercetak 82.5 dan saldo tercetak 100000.0, apa",
                    "adanya.",
                    "",
                    "  System.out.printf(\"Halo %s, umur %d%n\", nama, umur);",
                    "",
                    "String pertama adalah cetakannya. Setiap tanda % di dalamnya adalah",
                    "lubang yang diisi argumen berikutnya, sesuai urutan. Huruf sesudah %",
                    "menentukan jenis isinya:",
                    "",
                    "  %s   apa saja, diubah jadi teks      %d   bilangan bulat (int, long)",
                    "  %f   bilangan desimal                %b   true / false",
                    "  %c   satu karakter                   %n   ganti baris",
                    "  %%   tanda persen sungguhan",
                    "",
                    "Angka di antara % dan hurufnya mengatur bentuknya:",
                    "",
                    "  %.2f    dua angka di belakang koma     82.5     ->  82.50",
                    "  %10s    lebar 10, rata kanan           \"Andi\"   ->  '      Andi'",
                    "  %-10s   lebar 10, rata kiri            \"Andi\"   ->  'Andi      '",
                    "  %5d     lebar 5, rata kanan            42       ->  '   42'",
                    "  %05d    lebar 5, sisanya diisi nol     42       ->  '00042'",
                    "  %,d     pemisah ribuan                 100000   ->  '100,000'",
                    "",
                    "Dengan lebar tetap, tabel di terminal jadi lurus rapi tanpa kamu harus",
                    "menghitung spasi sendiri.",
                    "",
                    "Pemisah ribuan dan tanda desimal ikut setelan bahasa di komputer yang",
                    "menjalankan program (locale). Contoh di atas memakai setelan Inggris.",
                    "Di komputer yang disetel ke bahasa Indonesia, %,d mencetak 100.000 dan",
                    "%.2f mencetak 82,50.",
                    "",
                    "printf dan String.format memakai cetakan yang sama persis. Bedanya cuma",
                    "tujuan hasilnya. printf langsung mencetak, sedangkan String.format",
                    "mengembalikan String yang bisa kamu simpan, gabungkan, atau tulis ke",
                    "berkas.",
                    "",
                    "Dua hal yang sering bikin tersandung:",
                    "  1. Pakai %n, bukan \\n. %n memakai penanda baris baru milik sistem yang",
                    "     sedang menjalankan program, jadi berkas hasilnya benar juga di",
                    "     Windows.",
                    "  2. Tipe argumen harus cocok dengan hurufnya. Salah pasang nggak",
                    "     ketahuan compiler, dan program baru berhenti dengan error waktu",
                    "     dijalankan:",
                    "       System.out.printf(\"%d%n\", \"Andi\");",
                    "       java.util.IllegalFormatConversionException: d != java.lang.String",
                    "     Kalau ragu, pakai %s, yang menerima apa pun.",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Isi form yang diketik orang hampir nggak pernah rapi. Ada spasi",
                    "berlebih, huruf besar kecil campur aduk, dan tanda baca yang",
                    "macam-macam. Sebelum disimpan atau dibandingkan, teks itu dirapikan",
                    "dulu dengan method String seperti trim, replace, dan startsWith.",
                    "",
                    "Kasus kecil: form pendaftaran toko online menerima nomor HP dalam",
                    "berbagai bentuk, misalnya \" 0812-3456-7890 \". Sistem pengirim pesan",
                    "butuh bentuk baku 6281234567890: tanpa spasi, tanpa tanda hubung, dan",
                    "diawali kode negara 62.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Masukannya satu String berantakan, keluarannya satu String baku.",
                    "     Tulis dulu satu contoh masukan beserta keluaran yang benar.",
                    "  2. Pecah jadi langkah kecil: buang spasi di ujung, buang tanda hubung,",
                    "     lalu ganti 0 di depan jadi 62:",
                    "      String hp = \" 0812-3456-7890 \".trim().replace(\"-\", \"\");",
                    "      if (hp.startsWith(\"0\")) {",
                    "          hp = \"62\" + hp.substring(1);",
                    "      }",
                    "      System.out.println(hp);   // 6281234567890",
                    "  3. Uji kasus pinggirnya: nomor yang ditulis \"+62 812 3456 7890\" harus",
                    "     ikut jadi baku. Buang juga tanda plus dan spasi di tengahnya dengan",
                    "     replace.",
                    "  4. Bandingkan hasilnya dengan nomor yang udah tersimpan pakai equals,",
                    "     jangan pakai ==.",
                    "",
                    "Jebakan: hp.trim(); yang ditulis sendirian nggak mengubah apa pun.",
                    "String itu immutable, jadi hasilnya wajib ditampung: hp = hp.trim();.",
                ]
            },
        ],
    },
    {
        "title": "27. Tanggal & Waktu (java.time)",
        "sections": [
            {
                "body": [
                    "Hampir semua aplikasi nyata menyimpan waktu: tanggal lahir, tanggal",
                    "transaksi, jatuh tempo tagihan, kapan sebuah baris data dibuat, atau",
                    "jam berapa sebuah error terjadi. Sejak Java 8, Java punya satu paket",
                    "khusus untuk itu: java.time.",
                    "",
                    "Kenapa perlu paket baru? Paket yang lama punya tiga cacat yang bikin",
                    "banyak masalah:",
                    "  - java.util.Date bisa diubah. Kamu mengoper sebuah tanggal ke method",
                    "    orang lain, method itu menggesernya, dan tanggal di tempatmu ikut",
                    "    berubah tanpa tanda apa pun.",
                    "  - SimpleDateFormat nggak aman dipakai bersamaan oleh beberapa thread.",
                    "    Orang menjadikannya field static supaya hemat. Kelihatannya benar",
                    "    bertahun-tahun, lalu di server yang ramai dia sesekali mengeluarkan",
                    "    tanggal ngawur. Bug seperti ini hampir mustahil ditiru ulang. (Soal",
                    "    thread, lihat materi Multithreading & Concurrency Dasar.)",
                    "  - Calendar menghitung bulan mulai dari 0. Januari = 0, Desember = 11.",
                    "    Jadi new GregorianCalendar(2026, 0, 15) itu 15 Januari, dan bukan",
                    "    15 Februari. Lebih parah lagi, tanggal yang mustahil nggak ditolak.",
                    "    Tanggal itu digulung ke tanggal berikutnya tanpa peringatan:",
                    "    new GregorianCalendar(2026, 1, 29) menghasilkan 1 Maret 2026, tanpa",
                    "    error apa pun.",
                    "",
                    "Ketiganya masih ada di mana-mana. Kode lama, library lama, dan paket",
                    "java.sql masih penuh Date dan Calendar, jadi kamu pasti ketemu mereka",
                    "waktu membaca kode orang. Cara menyeberang dari dan ke java.time ada di",
                    "bagian akhir materi ini.",
                    "",
                    "Memilih tipe",
                    "",
                    "Ini keputusan pertama, dan paling sering diambil asal-asalan. Ada lima",
                    "tipe utama:",
                    "  - LocalDate: tanggal saja, misalnya 2026-01-15. Cocok untuk tanggal",
                    "    lahir, jatuh tempo, dan tanggal libur.",
                    "  - LocalTime: jam saja, misalnya 08:30. Cocok untuk jam buka toko dan",
                    "    jadwal alarm.",
                    "  - LocalDateTime: tanggal dan jam, tanpa zona waktu, misalnya",
                    "    2026-01-15T13:45. Cocok untuk jadwal rapat dan kolom DATETIME di",
                    "    database.",
                    "  - Instant: satu titik di garis waktu, misalnya 2026-01-15T02:30:00Z.",
                    "    Cocok untuk stempel baris log, created_at, dan apa pun yang perlu",
                    "    diurutkan.",
                    "  - ZonedDateTime: tanggal, jam, dan zona waktu, misalnya",
                    "    2026-01-15T09:30+07:00[Asia/Jakarta]. Cocok untuk apa pun yang",
                    "    dilihat pemakai di dua kota yang beda zona waktunya.",
                    "",
                    "Kata Local di depan nama tipe artinya tanpa zona waktu, dan bukan",
                    "\"waktu setempat\". LocalDateTime '2026-01-15 13:45' nggak ngasih tahu",
                    "itu jam 13:45 di kota mana, jadi nilai itu nggak bisa dibandingkan",
                    "dengan jam 13:45 milik kota lain.",
                    "",
                    "Pegangannya begini. Kalau yang kamu simpan adalah saat sesuatu terjadi",
                    "(log, transaksi, pembayaran), pakai Instant. Kalau yang kamu simpan",
                    "adalah angka di kalender, pakai LocalDate. Contohnya tanggal lahir,",
                    "yang tetap 17 Mei di mana pun orangnya berada.",
                    "",
                    "Membuat nilainya",
                    "",
                    "Ada tiga cara, dan namanya sama untuk semua tipe di atas:",
                    "",
                    "  LocalDate.now()                 dari jam sistem",
                    "  LocalDate.of(2026, 1, 15)       dari angka; bulan 1-12, tidak mulai 0",
                    "  LocalDate.parse(\"2026-01-15\")   dari teks berformat ISO",
                    "",
                    "Format ISO adalah format standar internasional, urutannya",
                    "tahun-bulan-tanggal seperti 2026-01-15.",
                    "",
                    "Contoh di materi ini sengaja nggak memakai now(). Hasil now() beda tiap",
                    "kali program dijalankan, jadi keluaranmu nggak akan pernah cocok dengan",
                    "yang tertulis di sini.",
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
                    "println() untuk tipe java.time selalu memberi bentuk ISO (2026-01-15),",
                    "dan nggak memberi bentuk Indonesia. Mengubahnya jadi 15/01/2026 itu",
                    "urusan DateTimeFormatter, yang dibahas di bagian berikutnya.",
                    "",
                    "Jebakan: semua tipe java.time immutable. plusDays, minusMonths,",
                    "withDayOfMonth, dan plusHours nggak mengubah objeknya. Semuanya",
                    "mengembalikan objek baru. Kalau hasilnya nggak ditampung, perubahannya",
                    "hilang, dan compiler diam aja karena secara tata bahasa nggak ada yang",
                    "salah.",
                    "",
                    "Contohnya baris jatuhTempo.plusDays(10); di program tadi. Kelihatannya",
                    "seperti \"majukan sepuluh hari\", padahal nggak melakukan apa-apa: objek",
                    "baru dibuat, lalu langsung dibuang. Yang benar selalu menampung",
                    "hasilnya:",
                    "",
                    "  jatuhTempo = jatuhTempo.plusDays(10);",
                    "",
                    "Sifat ini sama persis dengan String (lihat materi String & Scanner),",
                    "dan alasannya pun sama. Objek yang nggak bisa diubah aman dioper ke",
                    "mana-mana, dan aman dipakai antar-thread.",
                    "",
                    "Untuk membandingkan tanggal, jangan pakai ==. Dua tanggal 17 Mei 2000",
                    "di program tadi isinya sama persis, tapi lahir == salinan bernilai",
                    "false. LocalDate.of() membuat objek baru tiap kali dipanggil, sedangkan",
                    "== membandingkan alamat objek, dan nggak melihat isinya. Yang benar:",
                    "",
                    "  isBefore(lain)   lebih awal?",
                    "  isAfter(lain)    lebih akhir?",
                    "  isEqual(lain)    menunjuk saat yang sama?",
                    "  equals(lain)     seluruh isinya sama?",
                    "",
                    "Tipe tanggal dan waktu di java.time, seperti LocalDate dan Instant,",
                    "juga Comparable. Jadi Collections.sort(daftarTanggal) langsung jalan",
                    "tanpa comparator (lihat materi Collection Framework).",
                    "",
                    "isEqual dan equals baru kelihatan bedanya pada ZonedDateTime. Jam 09:30",
                    "Jakarta dan jam 02:30 UTC adalah saat yang sama, jadi isEqual memberi",
                    "true. Tapi field-nya beda, karena zonanya beda, jadi equals memberi",
                    "false. Untuk menjawab \"apakah ini saat yang sama\", pakai isEqual.",
                    "",
                    "getMonth() dan getDayOfWeek() nggak memberi angka. Hasilnya enum:",
                    "",
                    "  lahir.getMonth()       -> MAY         (enum Month)",
                    "  lahir.getDayOfWeek()   -> WEDNESDAY   (enum DayOfWeek)",
                    "",
                    "Untuk angkanya, pakai getMonthValue() dan hari.getValue(), dengan",
                    "1 = Senin sampai 7 = Minggu. Namanya tercetak dalam bahasa Inggris",
                    "karena itu name() sebuah enum, dan bukan hasil terjemahan (lihat materi",
                    "Enum: Himpunan Nilai Tetap). Nama hari dalam bahasa Indonesia didapat",
                    "lewat formatter yang diberi Locale, dan nggak lewat getDayOfWeek().",
                    "",
                    "plusMonths menjepit tanggal yang nggak ada. 31 Januari ditambah 1 bulan",
                    "jadi 28 Februari, karena 31 Februari nggak ada. Akibatnya geser bulan",
                    "nggak bisa dibalik: hasil di atas kembali ke 28 Januari, dan bukan 31.",
                    "Untuk \"hari terakhir bulan ini\", jangan menghitung sendiri. Pakai",
                    "TemporalAdjusters dari java.time.temporal:",
                    "",
                    "  tanggal.with(TemporalAdjusters.lastDayOfMonth())",
                    "",
                    "Class itu juga punya method lain yang sejenis, misalnya:",
                    "",
                    "  tanggal.with(TemporalAdjusters.next(DayOfWeek.MONDAY))",
                    "  tanggal.with(TemporalAdjusters.firstDayOfMonth())",
                    "",
                    "Beda dengan Calendar, tanggal yang mustahil langsung ditolak waktu",
                    "dibuat, dan nggak digulung ke tanggal lain:",
                    "",
                    "  LocalDate.of(2026, 2, 29)",
                    "      -> DateTimeException: Invalid date 'February 29' ...",
                    "  LocalDate.of(2026, 13, 1)",
                    "      -> DateTimeException: Invalid value for MonthOfYear ...",
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
                    "Ada tiga alat untuk menghitung selisih, dan salah pilih alat adalah",
                    "kesalahan paling umum di bagian ini:",
                    "",
                    "  Period                     berbasis kalender: tahun, bulan, hari",
                    "  Duration                   berbasis detik: jam, menit, detik, nano",
                    "  ChronoUnit.X.between(a,b)  satu satuan saja, hasilnya long",
                    "",
                    "Period.between cuma menerima LocalDate. Duration.between butuh sesuatu",
                    "yang punya jam, jadi Duration.between(tanggal1, tanggal2) melempar",
                    "UnsupportedTemporalTypeException: Unsupported unit: Seconds. Error ini",
                    "muncul waktu program jalan, dan nggak ketahuan waktu kompilasi.",
                    "",
                    "Jebakan: getDays() memberi sisa hari sesudah tahun dan bulannya",
                    "diambil, dan bukan total hari.",
                    "",
                    "  Period.between(1 Jan 2026, 10 Mar 2026).getDays()  ->  9    (bukan 68!)",
                    "",
                    "Angka 9 di atas artinya \"2 bulan 9 hari\". Untuk total hari, satu-satunya",
                    "jawaban yang benar adalah:",
                    "",
                    "  ChronoUnit.DAYS.between(a, b)",
                    "",
                    "Duration punya jebakan yang sama. toHours() memberi total jam yang",
                    "dibulatkan ke bawah (8), toMinutes() memberi total menit (525), dan",
                    "toMinutesPart() memberi sisa menit (45). Kalau toHours() dicampur",
                    "dengan toMinutes() dalam satu kalimat, hasilnya \"8 jam 525 menit\".",
                    "",
                    "Bentuk toString-nya mengikuti ISO: P25Y7M29D dibaca 25 tahun 7 bulan",
                    "29 hari, dan PT8H45M dibaca 8 jam 45 menit.",
                    "",
                    "Format dan parse",
                    "",
                    "format() mengubah objek jadi teks, parse() mengubah teks jadi objek.",
                    "Huruf pola yang sering dipakai:",
                    "",
                    "  yyyy  tahun 4 digit      MM  bulan angka (01)    dd  tanggal (15)",
                    "  MMM   nama bulan singkat MMMM nama bulan penuh    EEEE nama hari",
                    "  HH    jam 0-23           hh  jam 1-12 (butuh a)   a   AM/PM",
                    "  mm    menit              ss  detik                SSS milidetik",
                    "",
                    "Jebakan: huruf besar dan kecil di pola itu beda artinya. Semua salah",
                    "ketik di bawah ini lolos kompilasi, dan salahnya baru kelihatan di",
                    "layar:",
                    "  - \"HH:MM\": mm itu menit, MM itu bulan. Jam 21:05 di bulan Januari",
                    "    tercetak jadi 21:01.",
                    "  - \"dd/MM/YYYY\": Y itu tahun berbasis pekan, dan bukan tahun kalender.",
                    "    31 Desember 2025 tercetak 31/12/2026, karena hari itu udah masuk",
                    "    pekan pertama tahun berikutnya. Bug ini cuma muncul di sekitar",
                    "    pergantian tahun, pas laporan akhir tahun dicetak.",
                    "  - \"DD\": D itu hari ke berapa dalam setahun. 31 Desember 2025 jadi",
                    "    365.",
                    "",
                    "Pakai huruf kecil untuk hari (dd), menit (mm), dan tahun (yyyy). Selalu",
                    "uji formatter barumu dengan satu tanggal yang kamu tahu jawabannya.",
                    "",
                    "parse() menuntut teks yang cocok persis dengan polanya, termasuk nol di",
                    "depan:",
                    "",
                    "  LocalDate.parse(\"06/09/2026\")  gagal, tanpa formatter Java menuntut ISO",
                    "  LocalDate.parse(\"2026-1-5\")    gagal, ISO menuntut 2026-01-05",
                    "",
                    "DateTimeParseException itu unchecked, jadi compiler nggak memaksamu",
                    "menangkapnya. Teks tanggal yang datang dari form, berkas, atau API",
                    "wajib kamu bungkus try-catch sendiri (lihat materi Exception Handling).",
                    "",
                    "Untuk format baku ada konstanta siap pakai:",
                    "DateTimeFormatter.ISO_LOCAL_DATE, ISO_LOCAL_DATE_TIME, dan ISO_INSTANT.",
                    "Untuk nama bulan dan hari berbahasa Indonesia, sertakan Locale:",
                    "",
                    "  DateTimeFormatter.ofPattern(\"EEEE, dd MMMM yyyy\",",
                    "                              Locale.forLanguageTag(\"id\"))",
                    "",
                    "Dengan formatter itu, 15 Januari 2026 tercetak \"Kamis, 15 Januari",
                    "2026\".",
                    "",
                    "Beda dengan SimpleDateFormat yang lama, DateTimeFormatter aman dipakai",
                    "antar-thread. Jadi formatter boleh, malah sebaiknya, disimpan sebagai",
                    "static final dan dipakai bersama.",
                    "",
                    "Instant dan zona waktu",
                    "",
                    "Instant nggak punya zona sama sekali. Huruf Z di ujungnya artinya UTC,",
                    "yaitu waktu acuan dunia. toEpochMilli() memberi jumlah milidetik sejak",
                    "1 Januari 1970 UTC, angka besar yang sering kamu temui di JSON dan log.",
                    "",
                    "atZone() nggak menggeser waktunya. Method ini cuma mengubah cara",
                    "membacanya: 02:30 UTC dan 09:30 di Jakarta adalah saat yang sama.",
                    "",
                    "Nama zona ditulis dalam bentuk Benua/Kota, seperti \"Asia/Jakarta\", dan",
                    "bukan \"WIB\" atau \"+7\". Nama kota yang membawa sejarah aturan zona dan",
                    "daylight saving (pergeseran jam di musim panas) negara itu.",
                    "",
                    "Di mana java.time ketemu materi lain? Bagian ini menyebut beberapa",
                    "materi yang baru datang nanti. Kamu belum perlu memahaminya sekarang,",
                    "cukup tahu bahwa hubungannya ada:",
                    "  - JDBC (materi JDBC: Menghubungkan Java ke Database): driver modern",
                    "    mengerti java.time langsung.",
                    "      stmt.setObject(1, tanggalLahir);",
                    "      LocalDate tgl = rs.getObject(\"tgl_lahir\", LocalDate.class);",
                    "    Pemetaan tipe kolomnya:",
                    "      DATE                       -> LocalDate",
                    "      DATETIME / TIMESTAMP       -> LocalDateTime",
                    "      TIMESTAMP WITH TIME ZONE   -> OffsetDateTime",
                    "    Hindari rs.getDate(), yang mengembalikan java.sql.Date lama.",
                    "  - File I/O (materi File I/O & Serialization): nama berkas bertanggal",
                    "    pakai pola \"yyyyMMdd\", supaya laporan-20260115.txt berurut sendiri",
                    "    secara alfabetis. Pola \"dd-MM-yyyy\" nggak berurut begitu.",
                    "  - Log: pakai Instant.now() untuk stempel waktu. Bentuk ISO-nya bisa",
                    "    diurutkan sebagai teks biasa.",
                    "  - Unit testing (materi Unit Testing dengan JUnit): method yang",
                    "    memanggil LocalDate.now() di dalamnya mustahil diuji, karena",
                    "    hasilnya berubah tiap hari. Terima java.time.Clock sebagai",
                    "    parameter, lalu panggil LocalDate.now(jam). Di tes, berikan",
                    "      Clock.fixed(Instant.parse(\"2026-01-15T02:30:00Z\"),",
                    "                  ZoneId.of(\"Asia/Jakarta\"))",
                    "",
                    "Menyeberang dari API lama",
                    "",
                    "Kalau kamu terpaksa memanggil kode lama, pakai pasangan konversi ini.",
                    "Yang kiri mengubah java.time ke tipe lama, yang kanan sebaliknya:",
                    "",
                    "  Date lama = Date.from(instant);              Instant i = lama.toInstant();",
                    "  java.sql.Date sd = java.sql.Date.valueOf(localDate);   sd.toLocalDate();",
                    "  Timestamp ts = Timestamp.valueOf(localDateTime);       ts.toLocalDateTime();",
                    "",
                    "Ubah ke java.time secepat mungkin di batas kodemu, lalu jangan sentuh",
                    "lagi tipe lama.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Perpustakaan sekolah menghitung denda keterlambatan, aplikasi kredit",
                    "menghitung jatuh tempo cicilan, dan absensi kantor mencatat jam masuk.",
                    "Semuanya hitungan tanggal, dan java.time mengerjakannya tanpa kamu",
                    "perlu menghafal jumlah hari tiap bulan.",
                    "",
                    "Kasus kecil: buku dipinjam 3 September 2026 dengan batas 7 hari, lalu",
                    "dikembalikan 15 September. Dendanya Rp1.000 per hari terlambat.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Masukannya dua tanggal, yaitu tanggal pinjam dan tanggal kembali.",
                    "     Keluarannya jumlah hari terlambat dan dendanya. Isinya cuma",
                    "     tanggal tanpa jam, jadi pakai LocalDate.",
                    "  2. Hitung batasnya dengan plusDays, dan tampung hasilnya, karena",
                    "     LocalDate immutable.",
                    "  3. Hitung selisih dari batas sampai tanggal kembali dengan",
                    "     ChronoUnit, yang memberi jumlah hari secara utuh:",
                    "      LocalDate pinjam = LocalDate.of(2026, 9, 3);",
                    "      LocalDate batas = pinjam.plusDays(7);            // 2026-09-10",
                    "      LocalDate kembali = LocalDate.of(2026, 9, 15);",
                    "      long telat = Math.max(0, ChronoUnit.DAYS.between(batas, kembali));",
                    "      System.out.println(telat * 1000);                // 5000",
                    "  4. Uji kasus pinggirnya: buku yang kembali 8 September menghasilkan",
                    "     selisih negatif. Math.max(0, ...) mengubahnya jadi 0 hari, jadi",
                    "     dendanya nol.",
                    "",
                    "Jebakan: Period.between(batas, kembali).getDays() cuma memberi sisa",
                    "hari sesudah bulannya diambil. Buku yang telat 1 bulan 2 hari bakal",
                    "didenda 2 hari saja, padahal telatnya 32 hari.",
                ]
            },
        ],
    },
    {
        "title": "28. Lambda Expression & Functional Interface",
        "sections": [
            {
                "body": [
                    "Functional interface adalah interface yang punya tepat satu abstract",
                    "method. Lambda expression adalah cara ringkas menulis implementasi",
                    "functional interface, tanpa perlu bikin class terpisah.",
                    "",
                    "Bentuk lambda ada dua:",
                    "",
                    "  (parameter) -> ekspresi",
                    "  (parameter) -> { beberapa statement; return nilai; }",
                    "",
                    "Bentuk pertama dipakai kalau isinya cuma satu ekspresi. Kalau method-nya",
                    "mengembalikan nilai, hasil ekspresi itu otomatis jadi nilai",
                    "kembaliannya. Bentuk kedua dipakai kalau isinya beberapa baris, dan",
                    "return-nya kamu tulis sendiri.",
                    "",
                    "Contohnya Runnable, functional interface bawaan Java yang method-nya",
                    "cuma satu, yaitu run(). Cara lama, sebelum ada lambda, memakai",
                    "anonymous class, yaitu class tanpa nama yang langsung dibuat di tempat:",
                    "",
                    "  Runnable r = new Runnable() {",
                    "      public void run() {",
                    "          System.out.println(\"Jalan!\");",
                    "      }",
                    "  };",
                    "",
                    "Dengan lambda (Java 8+), hasilnya sama, tapi cukup satu baris:",
                    "",
                    "  Runnable r = () -> System.out.println(\"Jalan!\");",
                    "",
                    "Anotasi @FunctionalInterface menandai interface yang cuma boleh punya",
                    "satu abstract method. Sifatnya opsional, tapi disarankan. Kalau suatu",
                    "hari ada yang menambah abstract method kedua, compiler langsung",
                    "menolak.",
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
                    "Kamu nggak selalu perlu bikin functional interface sendiri. Java udah",
                    "menyediakan yang umum di paket java.util.function:",
                    "",
                    "  Function<T,R>     -> menerima T, mengembalikan R. apply(T)",
                    "  Predicate<T>      -> menerima T, mengembalikan boolean. test(T)",
                    "  Consumer<T>       -> menerima T, tidak mengembalikan apa pun. accept(T)",
                    "  Supplier<T>       -> tidak menerima apa pun, mengembalikan T. get()",
                    "  BiFunction<T,U,R> -> menerima 2 argumen, mengembalikan R.",
                    "",
                    "Contoh pemakaiannya:",
                    "",
                    "  Predicate<Integer> genap = n -> n % 2 == 0;",
                    "  genap.test(4);      // true",
                    "",
                    "  Function<String, Integer> panjang = s -> s.length();",
                    "  panjang.apply(\"Java\");  // 4",
                    "",
                    "  Consumer<String> cetak = s -> System.out.println(s);",
                    "  cetak.accept(\"Halo\");",
                    "",
                    "Kalau lambda-nya cuma meneruskan argumen ke satu method yang udah ada,",
                    "kamu bisa menulisnya lebih ringkas lagi pakai method reference, yaitu",
                    "menyebut nama method-nya langsung dengan tanda ::.",
                    "",
                    "  Consumer<String> cetak = System.out::println;",
                    "  Function<String, Integer> panjang = String::length;",
                    "",
                    "Baris pertama sama artinya dengan s -> System.out.println(s), dan baris",
                    "kedua sama dengan s -> s.length().",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aturan promo di toko online berganti tiap minggu: minggu ini potong",
                    "10%, minggu depan potong Rp5.000. Daripada mengubah method harga tiap",
                    "kali, aturannya dikirim sebagai nilai berupa lambda. Pola yang sama",
                    "dipakai untuk aksi tombol, filter pencarian, dan aturan validasi.",
                    "",
                    "Kasus kecil: ada dua promo. Potong 10% untuk barang Rp80.000 harus",
                    "menghasilkan Rp72.000. Potong Rp5.000 untuk barang Rp3.000 nggak boleh",
                    "bikin harganya minus.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Cari bagian yang berubah-ubah, yaitu rumus harganya. Masukannya",
                    "     satu harga, keluarannya harga baru.",
                    "  2. Bentuk itu cocok dengan Function<Integer, Integer> dari",
                    "     java.util.function, jadi kamu nggak perlu bikin interface sendiri.",
                    "  3. Tulis tiap promo sebagai lambda, lalu panggil lewat apply:",
                    "      Function<Integer, Integer> potong10Persen = h -> h - h / 10;",
                    "      Function<Integer, Integer> potong5Ribu = h -> Math.max(0, h - 5000);",
                    "      System.out.println(potong10Persen.apply(80000));   // 72000",
                    "      System.out.println(potong5Ribu.apply(3000));       // 0",
                    "  4. Uji kasus pinggirnya: barang Rp3.000 dengan potongan Rp5.000. Tanpa",
                    "     Math.max, hasilnya -2000, seolah toko yang membayar pembeli.",
                    "",
                    "Ingat: method yang menerima Function<Integer, Integer> sebagai",
                    "parameter bisa dipakai untuk promo apa pun, termasuk promo yang baru",
                    "dibuat tahun depan.",
                ]
            },
        ],
    },
    {
        "title": "29. Mengurutkan Objek: Comparable & Comparator",
        "sections": [
            {
                "body": [
                    "Di materi Collection Framework ada Collections.sort(listAngka). Nanti di",
                    "materi Stream API ada juga .sorted(). Dua-duanya jalan mulus tanpa",
                    "penjelasan apa pun, dan justru itu yang bikin salah paham.",
                    "",
                    "Mereka jalan karena Integer dan String udah membawa aturan urutannya",
                    "sendiri. Java nggak otomatis bisa mengurutkan apa aja. Begitu yang",
                    "diurutkan objek buatanmu sendiri, dua-duanya berhenti bekerja:",
                    "",
                    "  // daftar berisi beberapa objek Mahasiswa",
                    "  List<Mahasiswa> daftar = new ArrayList<>(...);",
                    "  Collections.sort(daftar);              // ditolak compiler",
                    "  daftar.stream().sorted().toList();     // lolos compiler, gagal saat jalan",
                    "",
                    "Satu penyebab, dua pesan yang beda jauh. Pesan pertama datang dari",
                    "compiler:",
                    "  error: no suitable method found for sort(List<Mahasiswa>)",
                    "      (inference variable T#1 has incompatible bounds",
                    "        lower bounds: Comparable<? super T#1>)",
                    "Pesan kedua baru muncul waktu programnya jalan. Kadang baru ketahuan",
                    "berbulan-bulan kemudian, waktu baris itu akhirnya kejalan:",
                    "  Exception in thread \"main\" java.lang.ClassCastException:",
                    "      class Mahasiswa cannot be cast to class java.lang.Comparable",
                    "",
                    "Penyebabnya: Java nggak tahu mana yang duluan di antara dua Mahasiswa.",
                    "Collections.sort menulis syarat itu di tanda tangannya, yaitu baris",
                    "deklarasi method-nya: <T extends Comparable<? super T>>. Karena",
                    "syaratnya tertulis, compiler bisa menolak sebelum program jalan.",
                    "",
                    "Sementara itu, .sorted() tanpa argumen nggak menulis syarat apa pun.",
                    "Waktu dikompilasi dia lolos aja. Baru waktu jalan dia mencoba melakukan",
                    "cast tiap elemen ke Comparable, lalu gagal di tengah jalan.",
                    "",
                    "Ditolak lebih awal itu menguntungkan. Kesalahan yang ditolak compiler",
                    "langsung ketahuan waktu kamu menulis kode. Kesalahan yang baru muncul",
                    "waktu program jalan bisa lolos sampai ke tangan pengguna. Yang bikin",
                    "beda adalah syarat di dalam kurung sudut tadi, namanya generic bound",
                    "(batasan tipe). Materi Generics nanti membahasnya lebih jauh.",
                    "",
                    "Kontrak compareTo",
                    "",
                    "Kontrak di sini artinya aturan main yang harus dipatuhi setiap class",
                    "yang memakai Comparable. Isi interface Comparable cuma satu method:",
                    "  int compareTo(T lain)",
                    "Hasilnya int, bukan boolean. Bagian ini yang paling sering salah",
                    "dibaca. Arti hasilnya:",
                    "  negatif  -> objek ini harus berada sebelum 'lain'",
                    "  nol      -> keduanya dianggap sama posisinya",
                    "  positif  -> objek ini harus berada sesudah 'lain'",
                    "",
                    "Yang dihitung cuma tandanya, besarnya nggak penting.",
                    "\"Andi\".compareTo(\"Zaki\") hasilnya -25, bukan -1. String menghitung",
                    "selisih huruf pertama yang berbeda, dan jarak dari A ke Z memang 25.",
                    "",
                    "Jebakan: jangan pernah nulis if (a.compareTo(b) == -1). Tulis",
                    "if (a.compareTo(b) < 0). Kode yang membandingkan dengan -1 benar untuk",
                    "sebagian data dan salah untuk sebagian lain. Bug kayak gini lebih susah",
                    "dilacak daripada kode yang salah untuk semua data.",
                    "",
                    "Sebuah tipe dikasih urutan alami dengan implements Comparable<TipeItu>,",
                    "lalu meng-override compareTo. Urutan alami artinya urutan bawaan tipe",
                    "itu, yang dipakai kalau kamu nggak minta urutan lain.",
                    "",
                    "Kapan sebuah tipe pantas punya urutan alami? Kalau ada satu urutan yang",
                    "hampir semua orang setujui tanpa perlu nanya: angka dari kecil, teks",
                    "dari A sampai Z, tanggal dari lama ke baru, NIM dari kecil. Kalau kamu",
                    "harus nanya dulu \"diurutkan berdasarkan apa?\", tipe itu nggak punya",
                    "urutan alami. Yang kamu butuhkan Comparator.",
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
                    "Comparable menempel di class-nya, jadi satu tipe cuma bisa punya satu",
                    "urutan. Padahal tiap layar sering butuh urutan yang beda. Papan",
                    "peringkat butuh IPK. Buku alumni butuh nama. Laporan fakultas butuh",
                    "jurusan dulu, baru IPK. Kamu nggak mungkin mengubah compareTo tiap kali",
                    "butuh urutan baru, apalagi kalau class-nya milik orang lain dan nggak",
                    "bisa kamu ubah sama sekali.",
                    "",
                    "Comparator memisahkan cara mengurutkan dari class yang diurutkan. Dia",
                    "objek tersendiri. Kamu bisa bikin sebanyak yang kamu mau, menyimpannya",
                    "di variabel, mengopernya sebagai argumen method, dan memakainya",
                    "berulang kali. Comparator juga functional interface, yaitu interface",
                    "yang abstract method-nya cuma satu (di sini compare(a, b)). Jadi semua",
                    "yang kamu pelajari di materi Lambda berlaku juga di sini.",
                    "",
                    "Bentuk paling mentahnya lambda dengan dua argumen:",
                    "  Comparator<Mahasiswa> perNama =",
                    "          (a, b) -> a.getNama().compareTo(b.getNama());",
                    "Bentuk ini sah, dan bakal sering kamu lihat di kode orang. Masalahnya,",
                    "bentuk ini gampang salah tanpa peringatan apa pun. Kalau a dan b",
                    "ketuker, urutannya kebalik. Kalau di kiri pakai getNama() tapi di kanan",
                    "getJurusan(), urutannya jadi ngawur, dan kodenya tetap lolos compiler.",
                    "",
                    "Sejak Java 8 ada bentuk yang cuma menyebut kuncinya. Kunci di sini",
                    "artinya nilai yang dipakai untuk membandingkan, misalnya nama:",
                    "  Comparator<Mahasiswa> perNama = Comparator.comparing(Mahasiswa::getNama);",
                    "Di sini nggak ada a dan b yang bisa ketuker. Kamu cukup nunjuk satu",
                    "field, sisanya diurus Java.",
                    "",
                    "Berikut pabrik dan perangkainya, semuanya method di interface",
                    "Comparator. Pabrik artinya method yang bikin comparator baru. Perangkai",
                    "artinya method yang menyambung comparator dengan kunci berikutnya atau",
                    "membalik arahnya. Seri artinya dua elemen punya nilai kunci yang sama.",
                    "  Comparator.comparing(fn)        kunci apa pun yang Comparable",
                    "                                  (String, Integer, LocalDate)",
                    "  Comparator.comparing(fn, cmp)   kunci diambil fn, tapi cara",
                    "                                  mengurutkannya ditentukan cmp",
                    "  Comparator.comparingInt(fn)     kunci int, tanpa membungkusnya jadi",
                    "                                  Integer",
                    "  Comparator.comparingLong(fn)    kunci long",
                    "  Comparator.comparingDouble(fn)  kunci double",
                    "  .thenComparing(fn)              kunci kedua, dipakai cuma kalau kunci",
                    "                                  pertama seri",
                    "  .thenComparingInt/Long/Double   kunci kedua bertipe primitif",
                    "  .reversed()                     membalik arah comparator ini",
                    "  Comparator.naturalOrder()       urutan alami tipenya (butuh Comparable)",
                    "  Comparator.reverseOrder()       kebalikan urutan alami",
                    "  Comparator.nullsFirst(cmp)      izinkan kunci null, taruh di paling",
                    "                                  depan",
                    "  Comparator.nullsLast(cmp)       izinkan kunci null, taruh di paling",
                    "                                  belakang",
                    "",
                    "Kenapa ada comparingInt dan comparingDouble, padahal comparing aja udah",
                    "cukup? comparing memaksa setiap nilai primitif dibungkus jadi Integer",
                    "atau Double dulu sebelum dibandingkan. Untuk sepuluh baris data nggak",
                    "kerasa. Untuk list panjang yang diurutkan berkali-kali, itu bisa jadi",
                    "jutaan objek sampah, yaitu objek yang dibikin cuma untuk langsung",
                    "dibuang lagi.",
                    "",
                    "Ini semua tempat yang menerima comparator. Cara pakainya sama, jadi",
                    "begitu kamu paham satu, yang lain gampang:",
                    "  - daftar.sort(cmp): mengurutkan list di tempat, artinya list aslinya",
                    "    yang berubah.",
                    "  - Collections.sort(daftar, cmp): bentuk lama, hasilnya sama.",
                    "  - Arrays.sort(array, cmp): untuk array berisi objek.",
                    "  - daftar.stream().sorted(cmp): menghasilkan aliran baru, list aslinya",
                    "    nggak berubah.",
                    "  - daftar.stream().max(cmp) dan .min(cmp): mengembalikan Optional<T>.",
                    "  - Collections.max(daftar, cmp): mengembalikan elemennya langsung, dan",
                    "    error kalau list-nya kosong.",
                    "  - new TreeSet<>(cmp) dan new TreeMap<>(cmp): urutan isinya ditentukan",
                    "    comparator ini.",
                    "  - new PriorityQueue<>(cmp): menentukan siapa yang keluar duluan dari",
                    "    antrean.",
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
                    "Ada tujuh jebakan yang sering bikin orang tersandung waktu mengurutkan:",
                    "  1. Jangan mengurutkan pakai pengurangan.",
                    "     (a, b) -> a.getUmur() - b.getUmur() kelihatan pintar, dan hasilnya",
                    "     benar untuk umur manusia. Tapi kalau kuncinya angka besar atau",
                    "     boleh negatif, misalnya saldo, selisih waktu, atau koordinat, hasil",
                    "     pengurangannya bisa overflow. Overflow artinya hasilnya melewati",
                    "     batas int (sekitar 2,1 miliar), lalu tandanya kebalik:",
                    "       2000000000 - (-2000000000)  ->  -294967296",
                    "           (negatif! padahal kiri jauh lebih besar)",
                    "       Integer.compare(2000000000, -2000000000)  ->  1   (benar)",
                    "     Selalu pakai Integer.compare, Long.compare, atau Double.compare.",
                    "     Untuk pecahan, Double.compare juga satu-satunya cara yang benar.",
                    "     Dia bisa menangani NaN dan -0.0, dua nilai yang bikin a < b",
                    "     bertingkah aneh.",
                    "  2. Posisi reversed() menentukan apa yang dibalik. Bandingkan dua",
                    "     bentuk ini:",
                    "       comparing(getJurusan).thenComparing(getIpk).reversed()",
                    "         -> membalik seluruh rangkaian: jurusan jadi Z-A, IPK jadi",
                    "            turun. Jarang ada yang mau begini.",
                    "       comparing(getJurusan)",
                    "               .thenComparing(comparingDouble(getIpk).reversed())",
                    "         -> jurusan tetap A-Z, cuma IPK yang turun. Biasanya ini yang",
                    "            kamu maksud.",
                    "     Dua-duanya nggak menghasilkan error. Yang salah cuma isi layarnya,",
                    "     dan bug kayak gini bisa bertahan lama karena datanya kelihatan",
                    "     terurut.",
                    "  3. Urutan String itu leksikografis, artinya diurutkan menurut nomor",
                    "     karakternya. Semua huruf besar punya nomor yang lebih kecil",
                    "     daripada huruf kecil, jadi hasilnya beda dari urutan abjad:",
                    "       [\"Zebra\", \"apel\", \"Mangga\"] naturalOrder -> [Mangga, Zebra, apel]",
                    "     Kalau kamu mau urutan yang enak dibaca manusia, pakai",
                    "     String.CASE_INSENSITIVE_ORDER:",
                    "       daftar.sort(Comparator.comparing(Mahasiswa::getNama,",
                    "               String.CASE_INSENSITIVE_ORDER));",
                    "     Hasilnya [apel, Mangga, Zebra]. Untuk bahasa yang hurufnya",
                    "     beraksen, java.text.Collator lebih tepat.",
                    "  4. Kunci null bikin pengurutan gagal. Kalau ada email yang null,",
                    "     Comparator.comparing(Mahasiswa::getEmail) melempar",
                    "     NullPointerException di tengah pengurutan. Pesannya nggak nyebut",
                    "     email sama sekali, misalnya:",
                    "       Cannot invoke \"java.lang.Comparable.compareTo(Object)\" because",
                    "       the return value of \"java.util.function.Function.apply(Object)\" is null",
                    "     nullsFirst dan nullsLast menentukan null ditaruh di ujung mana.",
                    "     Dua-duanya sah. Yang nggak sah itu pura-pura null nggak ada.",
                    "     Bedakan dua sasarannya:",
                    "       daftar.sort(Comparator.nullsLast(cmp))",
                    "         -> elemennya yang boleh null",
                    "       comparing(getEmail, Comparator.nullsLast(naturalOrder()))",
                    "         -> kuncinya yang boleh null",
                    "  5. Comparator yang nggak konsisten dengan equals bisa menghilangkan",
                    "     data. Untuk List.sort ini nggak masalah, karena seri artinya boleh",
                    "     berdampingan. Tapi TreeSet dan TreeMap sama sekali nggak memakai",
                    "     equals. Buat mereka, compare(a, b) == 0 artinya \"ini elemen yang",
                    "     sama\", jadi elemen kedua ditolak masuk tanpa error apa pun. Lihat",
                    "     baris terakhir contoh di atas: empat mahasiswa dimasukkan, cuma",
                    "     tiga yang tersimpan. Obatnya, untuk TreeSet dan TreeMap selalu",
                    "     rangkai kuncinya sampai comparator-nya nggak mungkin seri,",
                    "     misalnya dengan .thenComparing(Mahasiswa::getNim). Soal kontrak",
                    "     equals dan hashCode sendiri, lihat materi Class Object.",
                    "  6. Comparator yang nggak transitif ditolak mentah-mentah oleh sort.",
                    "     Transitif artinya kalau a sebelum b dan b sebelum c, maka a pasti",
                    "     sebelum c. Kalau comparator-mu bisa bilang a < b, b < c, tapi",
                    "     c < a (paling sering gara-gara aturan if bertingkat yang ditulis",
                    "     tangan), Java melempar:",
                    "       java.lang.IllegalArgumentException:",
                    "           Comparison method violates its general contract!",
                    "     Pesan ini membingungkan karena yang dituduh sort, padahal yang",
                    "     rusak comparator-nya. Pesan ini juga cuma muncul kalau datanya",
                    "     cukup banyak. Jadi tes kecil lolos, tapi programnya gagal begitu",
                    "     dipakai dengan data sungguhan. Kalau kamu merangkai",
                    "     Comparator.comparing dan thenComparing, masalah ini hampir mustahil",
                    "     terjadi.",
                    "  7. Lambda polos di dalam comparing sering gagal dikompilasi, dan",
                    "     pesannya menyesatkan. Java menebak tipe parameter lambda dari",
                    "     konteksnya. Begitu hasil comparing langsung dirangkai, konteks itu",
                    "     hilang:",
                    "       daftar.sort(Comparator.comparing(m -> m.getNama()).reversed());",
                    "       error: cannot find symbol",
                    "         symbol:   method getNama()",
                    "         location: variable m of type Object",
                    "     Pesannya bilang getNama() nggak ada, padahal method itu jelas ada.",
                    "     Yang terjadi, Java menyerah menebak tipe m lalu memakai Object.",
                    "     Pakai method reference (Mahasiswa::getNama), yang tipenya nggak",
                    "     perlu ditebak. Atau tulis tipenya langsung:",
                    "     ((Mahasiswa m) -> m.getNama()). Ini alasan praktis kedua kenapa",
                    "     comparing dengan method reference lebih jarang bikin repot daripada",
                    "     lambda (a, b) yang ditulis tangan.",
                    "",
                    "Jebakan: daftar.sort(cmp) mengubah list di tempat, jadi list-nya harus",
                    "boleh diubah. Urusannya memang di luar soal urutan, tapi sering ikut",
                    "bikin tersandung. List berikut nggak boleh diubah: List.of(...),",
                    "List.copyOf(...), Collections.unmodifiableList(...), dan hasil",
                    "stream().toList() (Java 16+). Semuanya melempar",
                    "UnsupportedOperationException. Pesan itu nggak nyebut urutan sama",
                    "sekali, jadi orang biasanya malah nyari salahnya di comparator.",
                    "",
                    "Bandingkan dengan .collect(Collectors.toList()), yang mengembalikan",
                    "ArrayList biasa dan boleh diurutkan. Jalan keluarnya ada dua: bungkus",
                    "dulu dengan new ArrayList<>(...), atau pakai stream().sorted(cmp) yang",
                    "memang nggak menyentuh list aslinya.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Toko online menawarkan urutan termurah, termahal, dan terlaris untuk",
                    "daftar produk yang sama. Papan peringkat kelas mengurutkan nilai dari",
                    "yang tertinggi. Semuanya memakai Comparator, yaitu cara mengurutkan",
                    "yang terpisah dari class yang diurutkan.",
                    "",
                    "Kasus kecil: wali kelas minta ranking dengan nilai tertinggi di atas.",
                    "Andi 92, Citra 88, Bayu 88. Kalau nilainya sama, urutkan nama dari A",
                    "sampai Z, supaya Bayu selalu di atas Citra.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tentukan kunci utamanya (nilai, dari besar ke kecil) dan kunci",
                    "     keduanya (nama, dari A ke Z).",
                    "  2. Rangkai keduanya dengan comparingInt, reversed, dan thenComparing:",
                    "      record Siswa(String nama, int nilai) { }",
                    "      List<Siswa> kelas = new ArrayList<>(List.of(new Siswa(\"Citra\", 88),",
                    "              new Siswa(\"Andi\", 92), new Siswa(\"Bayu\", 88)));",
                    "      kelas.sort(Comparator.comparingInt(Siswa::nilai).reversed()",
                    "              .thenComparing(Siswa::nama));",
                    "      // Andi 92, Bayu 88, Citra 88",
                    "  3. Uji kasus pinggirnya: tukar urutan Citra dan Bayu di data awal.",
                    "     Hasilnya harus tetap Andi, Bayu, Citra. Tanpa kunci kedua, urutan",
                    "     dua siswa yang seri cuma ikut urutan data awal.",
                    "",
                    "Jebakan: .reversed() yang ditaruh paling ujung membalik seluruh",
                    "rangkaian. Nama ikut terurut dari Z ke A, jadi Citra malah di atas",
                    "Bayu.",
                ]
            },
        ],
    },
    {
        "title": "30. Class di dalam Class: Nested, Inner, dan Anonymous",
        "sections": [
            {
                "body": [
                    "Sampai sini, setiap class selalu kamu tulis sejajar dengan class lain.",
                    "Padahal Java juga membolehkan class ditulis di dalam class lain. Kamu",
                    "udah ketemu bentuk ini beberapa kali, cuma belum dikasih tahu namanya:",
                    "  - Map.Entry<String, Integer> di materi Collection Framework. Ada titik",
                    "    di tengah nama tipenya karena Entry itu class yang tinggal di dalam",
                    "    Map.",
                    "  - new Runnable() { public void run() { ... } } di materi Lambda",
                    "    Expression. Di sana bentuk ini cuma disebut \"cara lama\", lalu",
                    "    ditinggal begitu aja.",
                    "",
                    "Nanti di materi Design Pattern & Clean Code kamu juga bakal ketemu",
                    "static class Builder. Itu juga class di dalam class.",
                    "",
                    "Bentuknya ada empat. Yang membedakan cuma dua pertanyaan: ditulis di",
                    "mana, dan butuh objek luar atau nggak. Objek luar artinya objek dari",
                    "class yang membungkusnya.",
                    "",
                    "  Bentuk          Ditulis di          Butuh objek luar?  Punya nama?",
                    "  -------------   -----------------   -----------------  -----------",
                    "  static nested   badan class         tidak              ya",
                    "  inner           badan class         ya                 ya",
                    "  local           badan method        tergantung         ya",
                    "  anonymous       di tengah ekspresi  tergantung         tidak",
                    "",
                    "Buat apa repot-repot? Sebagian class cuma punya arti di dalam satu",
                    "class lain. Node cuma berguna buat struktur data yang memilikinya.",
                    "Entry cuma berarti buat Map. Kalau ditaruh di berkas sendiri, orang",
                    "bakal mengira class itu boleh dipakai di mana aja. Padahal dia cuma",
                    "detail dalaman yang bisa berubah kapan aja. Dengan menaruhnya di dalam",
                    "pemiliknya, kodenya sendiri yang menunjukkan hubungan itu.",
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
                    "Static nested class itu class biasa yang kebetulan tinggal di dalam",
                    "class lain. Kata static di sini artinya beda dari static di field. Dia",
                    "nggak berarti \"cuma ada satu\" atau \"milik bersama\". Artinya cuma satu:",
                    "class ini nggak butuh objek luar.",
                    "",
                    "Dari luar, namanya ditulis NamaLuar.NamaDalam:",
                    "  Mahasiswa.Builder b = new Mahasiswa.Builder();   // Design Pattern",
                    "  Map.Entry<String, Integer> e = ...;              // Collection Framework",
                    "Titik di situ artinya \"class Entry yang ada di dalam Map\". Titik itu",
                    "nggak sedang mengambil field dari sebuah objek. Makanya cukup dengan",
                    "import java.util.Map; kamu udah bisa memakai Map.Entry. Entry ikut",
                    "terbawa bersama pemiliknya.",
                    "",
                    "Berkas .class-nya juga terpisah, dan namanya pakai tanda dolar:",
                    "  Tumpukan.class      Tumpukan$Node.class",
                    "Nama seperti Sekolah$1 atau Sekolah$1Penghitung kadang muncul di stack",
                    "trace. Itu nama class bersarang yang dibuatkan compiler, jadi kodenya",
                    "baik-baik aja.",
                    "",
                    "Inner class adalah nested class tanpa static, dan bedanya besar. Setiap",
                    "objek inner class menyimpan referensi, yaitu penunjuk, ke satu objek",
                    "luar, walaupun kamu nggak pernah menulisnya. Karena itu dia boleh",
                    "langsung memakai field objek luar tadi, tanpa perlu dioper lewat",
                    "constructor atau parameter.",
                    "",
                    "Ada dua akibat yang sering bikin orang tersandung:",
                    "  1. Inner class harus dibuat lewat objek luarnya: luar.new Dalam().",
                    "     Kalau kamu nulis new Dalam() polos di dalam method static,",
                    "     compiler menolak dengan pesan:",
                    "       non-static variable this cannot be referenced from a static context",
                    "     Dari class lain, pesannya beda lagi:",
                    "       an enclosing instance that contains C.Dalam is required",
                    "  2. Selama objek inner-nya masih dipegang, objek luarnya nggak bisa",
                    "     dibersihkan garbage collector, yaitu bagian Java yang membuang",
                    "     objek yang udah nggak dipakai. Objek luar itu tetap tertahan,",
                    "     walaupun isinya udah nggak dipakai siapa pun. Satu Node inner yang",
                    "     nyangkut di cache bisa menahan seluruh list induknya di memori.",
                    "",
                    "Aturan praktisnya: tulis static, kecuali kamu memang butuh field objek",
                    "luar. Node di contoh atas dibikin static karena alasan itu. Dia cuma",
                    "butuh isinya sendiri.",
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
                    "Sekarang kita bedah new Runnable() { ... }. Sintaks ini mustahil",
                    "ditebak sendiri. Kelihatannya seperti bikin objek dari interface,",
                    "padahal itu dilarang (lihat materi OOP: Abstract & Interface). Yang",
                    "terjadi adalah dua langkah sekaligus:",
                    "  1. Java bikin class baru tanpa nama yang implements Runnable. Isi",
                    "     class itu adalah blok kurung kurawal sesudah new Runnable().",
                    "  2. Java langsung bikin satu objek dari class tanpa nama tadi.",
                    "",
                    "Jadi yang di-new adalah class dadakan tadi, interface-nya sendiri",
                    "nggak pernah di-new. Kalau yang ditulis nama class (bukan interface),",
                    "blok itu artinya \"extends class tersebut\". Begitulah cara meng-override",
                    "sebuah abstract class secara dadakan.",
                    "",
                    "Local class jarang dipakai, tapi ada. Local class adalah class yang",
                    "dideklarasikan di dalam method, dan cuma kelihatan di dalam method",
                    "itu. Gunanya kalau kamu butuh beberapa method sekaligus untuk satu",
                    "perhitungan, tapi nggak mau menambah class yang kelihatan oleh kode",
                    "lain.",
                    "",
                    "Class di dalam method sering memakai variabel lokal milik method itu.",
                    "Istilahnya menangkap variabel. Aturannya berlaku untuk inner class,",
                    "local class, anonymous class, dan lambda: variabel lokal yang dipakai",
                    "dari dalam harus final atau effectively final. Effectively final",
                    "artinya variabel itu nggak pernah diisi nilai baru sesudah diisi",
                    "pertama kali. Kamu nggak wajib menulis kata final. Kalau dilanggar,",
                    "pesannya begini:",
                    "  local variables referenced from an inner class must be final or",
                    "  effectively final",
                    "",
                    "Alasannya begini. Nilai variabelnya disalin waktu objeknya dibuat.",
                    "Kalau variabel aslinya boleh berubah, salinannya jadi basi tanpa ada",
                    "yang tahu. Field objek (this.sesuatu) nggak kena aturan ini, yang",
                    "dibatasi cuma variabel lokal. Jalan keluarnya: salin dulu ke variabel",
                    "baru, atau simpan di field.",
                    "",
                    "Jebakan: di dalam inner class dan anonymous class, this menunjuk objek",
                    "dalam, bukan objek luar. Untuk objek luar, tulis NamaLuar.this, seperti",
                    "Sekolah.this.nama di contoh atas. Lambda beda. Lambda nggak punya this",
                    "sendiri, jadi this di dalamnya tetap objek luar. Dua bentuk ini",
                    "kelihatan setara, tapi perilakunya beda.",
                    "",
                    "Lambda udah ada dan lebih ringkas. Anonymous class masih dipakai dalam",
                    "empat keadaan:",
                    "  - Interface-nya punya lebih dari satu abstract method. Lambda cuma",
                    "    bisa untuk functional interface, yang abstract method-nya tepat",
                    "    satu.",
                    "  - Yang mau di-override abstract class, bukan interface. Lambda nggak",
                    "    bisa dipakai untuk itu.",
                    "  - Kamu butuh field sendiri untuk menyimpan keadaan (state), seperti",
                    "    dijalankan di contoh atas.",
                    "  - Trik new TypeReference<>() { } di library JSON seperti Jackson.",
                    "    Blok kosong itu memaksa Java bikin subclass, dan tipe generiknya",
                    "    ikut tersimpan di berkas class. Cuma lewat cara ini library-nya",
                    "    bisa membaca tipe itu waktu program jalan. (Generics punya materi",
                    "    sendiri, dua materi lagi dari sini.)",
                    "",
                    "Kalau ragu: interface satu method dan nggak butuh state, pakai lambda.",
                    "Selain itu, anonymous class masih bentuk paling ringkas yang tersedia.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Class kecil yang cuma berarti di dalam class lain ada di banyak",
                    "library: Map.Entry milik Map, Builder milik objek yang dibangunnya, dan",
                    "Node milik struktur data. Di aplikasi Android versi lama, aksi tombol",
                    "juga sering ditulis sebagai anonymous class.",
                    "",
                    "Kasus kecil: class Pesanan di aplikasi kafe perlu menyimpan beberapa",
                    "item, masing-masing dengan nama menu dan harga. Item nggak ada artinya",
                    "di luar pesanan, jadi kamu nggak mau class Item berdiri sendiri di",
                    "berkas lain.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Item cuma berarti di dalam Pesanan, jadi taruh di dalam class",
                    "     Pesanan.",
                    "  2. Tanya: apakah Item butuh field milik objek Pesanan? Nggak, dia",
                    "     cukup membawa datanya sendiri. Jadi tulis static:",
                    "      class Pesanan {",
                    "          static class Item {",
                    "              final String nama; final int harga;",
                    "              Item(String n, int h) { nama = n; harga = h; }",
                    "          }",
                    "      }",
                    "  3. Dari class lain, sebut namanya lewat class pemiliknya:",
                    "     new Pesanan.Item(\"Kopi susu\", 18000).",
                    "  4. Uji kasus pinggirnya: hapus kata static, lalu kompilasi lagi. Baris",
                    "     tadi ditolak dengan pesan an enclosing instance that contains",
                    "     Pesanan.Item is required, karena inner class butuh objek Pesanan",
                    "     lebih dulu.",
                    "",
                    "Ingat: tulis static kecuali Item memang butuh field milik Pesanan.",
                    "Inner class tanpa static selalu membawa penunjuk ke objek luarnya,",
                    "walaupun penunjuk itu nggak pernah dipakai.",
                ]
            },
        ],
    },
    {
        "title": "31. Stream API",
        "sections": [
            {
                "body": [
                    "Stream adalah cara memproses isi koleksi secara deklaratif. Artinya",
                    "kamu cukup bilang apa yang mau dilakukan, misalnya \"ambil yang genap,",
                    "lalu urutkan\". Kamu nggak perlu nulis loop-nya langkah demi langkah.",
                    "",
                    "Cara bikin stream:",
                    "  list.stream()            -> dari List atau Set",
                    "  map.entrySet().stream()  -> dari Map (lewat pasangan key-value-nya)",
                    "  Arrays.stream(array)     -> dari array",
                    "  Stream.of(1, 2, 3)       -> langsung dari nilai",
                    "",
                    "Operasi perantara (intermediate) mengembalikan stream baru, jadi bisa",
                    "dirangkai satu sesudah yang lain:",
                    "  filter(predicate)  -> menyaring elemen",
                    "  map(function)      -> mengubah tiap elemen",
                    "  sorted()           -> mengurutkan",
                    "  distinct()         -> membuang duplikat",
                    "  limit(n)           -> mengambil n elemen pertama",
                    "",
                    "Operasi akhir (terminal) menutup stream dan menghasilkan nilai akhir:",
                    "  collect(Collectors.toList())  -> jadi List",
                    "  forEach(consumer)              -> memproses tiap elemen",
                    "  count()                        -> jumlah elemen",
                    "  reduce(...)                    -> menggabungkan jadi satu nilai",
                    "  anyMatch/allMatch/noneMatch    -> menguji kondisi",
                    "",
                    "Kata predicate, function, dan consumer di tabel itu menunjuk",
                    "functional interface dari materi Lambda: Predicate, Function, dan",
                    "Consumer. Biasanya kamu mengisinya dengan lambda, seperti di contoh",
                    "berikut.",
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
                    "Ingat: stream nggak pernah mengubah koleksi aslinya. Setiap operasi",
                    "menghasilkan stream atau koleksi baru. Gaya ini sering disebut",
                    "immutable-style: data lama dibiarkan, hasilnya ditaruh di tempat baru.",
                    "",
                    "Untuk data besar ada parallel stream, yang membagi pekerjaannya ke",
                    "beberapa thread sekaligus. Thread itu jalur kerja yang berjalan",
                    "bersamaan, dan dibahas di materi Multithreading & Concurrency Dasar.",
                    "  list.parallelStream().filter(...).collect(...);",
                    "",
                    "Hati-hati dengan efek samping di parallel stream. Efek samping artinya",
                    "lambda yang mengubah sesuatu di luar stream, misalnya menambah isi list",
                    "lain. Kalau dijalankan beberapa thread sekaligus, hasilnya bisa kacau.",
                ]
            },
            {
                "body": [
                    "Di contoh tadi ada satu baris yang muncul begitu aja:",
                    "IntStream.range(...). Itu anggota lain keluarga stream. Kalau belum",
                    "kenal, kamu bakal buntu justru di dua hal yang paling biasa:",
                    "menjumlahkan angka dan menghitung rata-rata.",
                    "",
                    "Masalahnya, Stream<Integer> nggak punya sum(). Stream biasa bisa berisi",
                    "objek apa aja, dan Java nggak bisa memastikan objek itu bisa",
                    "dijumlahkan. Makanya Java menyediakan tiga stream khusus untuk tipe",
                    "primitif, yang isinya angka betulan:",
                    "",
                    "  IntStream      untuk int (juga short, byte, char)",
                    "  LongStream     untuk long",
                    "  DoubleStream   untuk double",
                    "",
                    "Cara menyeberang dari satu keluarga ke keluarga lain:",
                    "",
                    "  Stream<T>        --mapToInt / mapToLong / mapToDouble-->  stream primitif",
                    "  stream primitif  --mapToObj-->  Stream<T>  (tiap angka jadi objek apa pun)",
                    "  stream primitif  --boxed()-->   Stream<Integer> dan sejenisnya",
                    "",
                    "Yang cuma ada di stream primitif:",
                    "",
                    "  IntStream.range(0, 5)          0,1,2,3,4  - batas atas tidak ikut",
                    "  IntStream.rangeClosed(1, 5)    1,2,3,4,5  - batas atas ikut",
                    "  sum()                          jumlah semua, langsung int/long/double",
                    "  average()                      OptionalDouble - list kosong tidak punya",
                    "                                 rata-rata (Optional dibahas di materi",
                    "                                 Optional & Null Safety)",
                    "  max() / min()                  OptionalInt",
                    "  summaryStatistics()            count, sum, min, average, max sekaligus",
                    "",
                    "Jadi IntStream.range(0, nama.size()) di contoh tadi cuma cara",
                    "menghasilkan indeks 0, 1, 2. Anggap aja for biasa yang ditulis sebagai",
                    "stream, supaya dua list bisa dibaca berbarengan.",
                    "",
                    "Ada satu bentuk baru yang makin sering muncul di kode Java baru:",
                    "  .toList()                        Java 16+, ringkas",
                    "  .collect(Collectors.toList())    bentuk lama, panjang",
                    "Dua-duanya menghasilkan List. Bedanya udah kamu temui di materi",
                    "Mengurutkan Objek: Comparable & Comparator. List hasil toList() nggak",
                    "bisa diubah lagi.",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Laporan di aplikasi toko hampir selalu berbentuk \"ambil yang memenuhi",
                    "syarat, ubah, lalu jumlahkan\". Contohnya omzet pesanan yang lunas,",
                    "rata-rata nilai siswa yang lulus, atau lima produk terlaris. Stream",
                    "menulis alur itu sebagai satu rangkaian yang terbaca dari atas ke",
                    "bawah.",
                    "",
                    "Kasus kecil: hari ini ada tiga pesanan. Andi Rp45.000 udah lunas, Budi",
                    "Rp120.000 belum bayar, dan Citra Rp78.000 udah lunas. Pemilik toko mau",
                    "omzet dari pesanan yang lunas saja.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Masukannya List<Pesanan>, keluarannya satu angka. Pesanan bisa",
                    "     dibuat sebagai record dengan komponen pelanggan, total, dan lunas.",
                    "  2. Susun alurnya dengan kata-kata dulu: saring yang lunas, ambil",
                    "     totalnya, lalu jumlahkan.",
                    "  3. Terjemahkan tiap kata jadi satu operasi stream. sum() cuma ada di",
                    "     IntStream, jadi turun dulu lewat mapToInt:",
                    "      int omzet = pesanan.stream()",
                    "              .filter(Pesanan::lunas)",
                    "              .mapToInt(Pesanan::total)",
                    "              .sum();",
                    "      // 123000",
                    "  4. Uji kasus pinggirnya: kalau belum ada pesanan yang lunas, hasilnya",
                    "     0 dan programnya tetap jalan. Beda dengan average(), yang untuk",
                    "     daftar kosong mengembalikan OptionalDouble kosong.",
                    "",
                    "Jebakan: stream nggak mengubah list aslinya. Pesanan Budi yang belum",
                    "lunas tetap ada di list pesanan sesudah filter.",
                ]
            },
        ],
    },
    {
        "title": "32. Generics",
        "sections": [
            {
                "body": [
                    "Generics adalah cara bikin class, method, atau interface yang bisa",
                    "dipakai untuk berbagai tipe data, tapi tetap type-safe. Type-safe",
                    "artinya kesalahan tipe udah ketahuan waktu kompilasi, sebelum program",
                    "jalan.",
                    "",
                    "Sebelum ada generics (sebelum Java 5), kamu harus pakai Object lalu",
                    "melakukan cast manual. Cara ini rawan error, karena salah tipe baru",
                    "ketahuan waktu program jalan, dalam bentuk ClassCastException.",
                    "",
                    "Dengan generics, tipe diperiksa waktu kompilasi:",
                    "  List<String> nama = new ArrayList<>();",
                    "  nama.add(\"Andi\");     // OK",
                    "  nama.add(123);        // error saat kompilasi, bukan saat runtime",
                    "",
                    "Huruf untuk tipe generik punya kebiasaan penamaan sendiri, dan hampir",
                    "semua programmer Java mengikutinya:",
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
                    "Wildcard (?) dipakai kalau tipe pastinya nggak diketahui atau nggak",
                    "penting:",
                    "  List<?> apaSaja       -> list tipe apa pun (read-only aman)",
                    "  List<? extends Number> -> list Number atau turunannya (untuk baca)",
                    "  List<? super Integer>  -> list Integer atau induknya (untuk tulis)",
                    "",
                    "Gampangnya: extends untuk list yang cuma kamu baca isinya, super untuk",
                    "list yang mau kamu isi.",
                    "",
                    "Generics dipakai di mana-mana. List<T>, Map<K,V>, dan Set<T> di",
                    "Collection Framework semuanya pakai generics, begitu juga Optional<T>.",
                ]
            },
            {
                "body": [
                    "Bounded type <T extends Number> dibaca begini: T boleh Number sendiri,",
                    "atau class apa pun turunan Number, misalnya Integer, Long, Double,",
                    "Float, dan BigDecimal. Kata extends di sini agak menipu. Kata yang sama",
                    "dipakai juga untuk interface (<T extends Comparable<T>>), dan bisa",
                    "digabung pakai tanda &, misalnya <T extends Number & Comparable<T>>.",
                    "",
                    "Batasan ini ada untungnya. Karena Java sekarang tahu T pasti Number,",
                    "kamu boleh memanggil method milik Number di dalamnya. Dari situlah",
                    "item.doubleValue() di contoh atas datang. doubleValue() itu milik class",
                    "Number, bukan milik T. Tanpa batasan itu, T dianggap Object aja, dan",
                    "Object nggak punya doubleValue().",
                    "",
                    "int dan double nggak termasuk. Tipe primitif bukan objek. Dia nggak",
                    "punya class induk, nggak turunan dari class apa pun, dan sama sekali",
                    "nggak punya method. Generics cuma bekerja dengan objek. Karena itu:",
                    "",
                    "  List<int> angka;       ->  error: unexpected type / required: reference",
                    "  List<Integer> angka;   ->  ini yang benar",
                    "",
                    "Terus jumlahkan(List.of(1, 2, 3)) di atas kok tetap jalan? Itu berkat",
                    "autoboxing (lihat materi Kelas Pembungkus & Konversi Tipe). Angka 1, 2,",
                    "dan 3 otomatis dibungkus jadi Integer dulu. Yang sampai ke method-mu",
                    "adalah List<Integer>, bukan list berisi int.",
                    "",
                    "Type erasure",
                    "",
                    "Type erasure adalah alasan di balik batasan generics yang terasa aneh.",
                    "Kurung sudut cuma hidup waktu kompilasi. Sesudah dikompilasi, semua <T>",
                    "dihapus (erased), dan bytecode-nya, yaitu isi berkas .class, cuma kenal",
                    "Object. Compiler udah memeriksa semuanya duluan dan menyisipkan cast",
                    "untukmu. Waktu program jalan, List<String> dan List<Integer> adalah",
                    "class yang sama persis.",
                    "",
                    "Ada tiga akibat yang cepat atau lambat bakal kamu temui:",
                    "  1. new T() dan new T[10] nggak bisa ditulis. Waktu program jalan, T",
                    "     udah nggak ada, jadi nggak ada yang bisa di-new. Penggantinya",
                    "     biasanya (T[]) new Object[10], atau cukup pakai List<T>.",
                    "  2. Kalau x bertipe Object, x instanceof List<String> ditolak",
                    "     compiler. Yang boleh cuma x instanceof List<?>.",
                    "  3. Dua method dengan parameter List<String> dan List<Integer> dianggap",
                    "     kembar, jadi nggak bisa dipakai sebagai overload.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Banyak method di aplikasi mengembalikan \"data, atau pesan kenapa",
                    "gagal\": cari siswa, cari buku, cek stok. Daripada bikin HasilSiswa,",
                    "HasilBuku, dan HasilStok yang isinya sama, generics membolehkan satu",
                    "class Hasil<T> dipakai untuk semuanya. List<T> dan Optional<T> dibangun",
                    "dengan cara yang sama.",
                    "",
                    "Kasus kecil: aplikasi perpustakaan punya method cariBuku dan cekStok.",
                    "Keduanya bisa gagal, dan pemanggilnya butuh data atau alasan gagalnya.",
                    "Tipe datanya beda: yang satu String judul, yang lain Integer jumlah.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Cari bagian yang sama dari kedua hasil: ada data, ada pesan gagal.",
                    "     Yang beda cuma tipe datanya, jadi tipe itu jadi parameter tipe T.",
                    "  2. Tulis class-nya sekali:",
                    "      class Hasil<T> {",
                    "          final T data; final String galat;",
                    "          Hasil(T d, String g) { data = d; galat = g; }",
                    "          boolean sukses() { return galat == null; }",
                    "      }",
                    "  3. Pakai dengan tipe yang beda-beda: Hasil<String> untuk judul buku,",
                    "     Hasil<Integer> untuk jumlah stok. Compiler menolak kalau kamu",
                    "     mengisi Hasil<Integer> dengan teks.",
                    "  4. Cek kasus pinggirnya: Hasil<int> ditolak compiler, karena generics",
                    "     cuma menerima objek. Tulis Hasil<Integer>, dan autoboxing yang",
                    "     mengurus sisanya.",
                    "",
                    "Jebakan: Hasil tanpa kurung sudut (raw type) tetap dikompilasi, cuma",
                    "dengan catatan unchecked. Pengecekan tipenya hilang, dan kesalahannya",
                    "baru muncul sebagai ClassCastException waktu program jalan.",
                ]
            },
        ],
    },
    {
        "title": "33. Optional & Null Safety",
        "sections": [
            {
                "body": [
                    "NullPointerException (sering disingkat NPE) adalah error paling umum di",
                    "Java. Error ini muncul waktu kamu memanggil method atau mengakses field",
                    "lewat referensi yang isinya null, yaitu variabel yang nggak menunjuk",
                    "objek apa pun.",
                    "",
                    "Optional<T> itu semacam kotak yang mungkin berisi nilai, mungkin juga",
                    "kosong. Dengan Optional, kamu dipaksa menangani kasus kosong secara",
                    "terang-terangan, jadi NullPointerException bisa dicegah dari awal.",
                    "",
                    "Cara bikin Optional:",
                    "  Optional<String> ada = Optional.of(\"Andi\");     // pasti tidak null",
                    "  Optional<String> kosong = Optional.empty();     // sengaja kosong",
                    "  Optional<String> aman = Optional.ofNullable(mungkinNull);",
                    "Optional.of dipakai kalau nilainya pasti ada. Kalau ternyata null, dia",
                    "langsung melempar NullPointerException. Kalau nilainya mungkin null,",
                    "pakai Optional.ofNullable.",
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
                    "Supaya Optional ada gunanya, pegang empat kebiasaan ini:",
                    "  1. Pakai Optional sebagai tipe kembalian method. Jangan dipakai untuk",
                    "     field atau parameter.",
                    "  2. Jangan panggil .get() sebelum ngecek isPresent(). Kalau Optional-nya",
                    "     kosong, get() melempar NoSuchElementException.",
                    "  3. Lebih enak pakai orElse, orElseGet, orElseThrow, atau ifPresent.",
                    "  4. Jangan berlebihan. Untuk kasus sederhana, cek null pakai if biasa",
                    "     udah cukup.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Mencari sesuatu yang mungkin nggak ada adalah kejadian sehari-hari:",
                    "cari member dari nomor HP, cari buku dari kodenya, cari paket dari",
                    "nomor resi. Spring Data JPA, yang disebut di materi terakhir, juga",
                    "mengembalikan Optional dari method findById untuk alasan yang sama.",
                    "",
                    "Kasus kecil: kasir minimarket mengetik nomor HP pembeli. Kalau nomornya",
                    "terdaftar sebagai member, pembeli dapat diskon sesuai catatannya. Kalau",
                    "nggak terdaftar, diskonnya 0, dan kasir lanjut tanpa error.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Masukannya nomor HP, keluarannya persen diskon. Hasil pencariannya",
                    "     bisa kosong, dan itu tanda Optional dibutuhkan.",
                    "  2. Data member disimpan di Map. Map.get mengembalikan null kalau",
                    "     nomornya nggak ada, jadi bungkus dengan Optional.ofNullable.",
                    "  3. Tentukan nilai cadangannya di satu tempat dengan orElse:",
                    "      Map<String, Integer> diskonMember = Map.of(\"081234567890\", 10);",
                    "      int diskon = Optional.ofNullable(diskonMember.get(hp)).orElse(0);",
                    "  4. Uji dua kasus utamanya: nomor terdaftar harus memberi 10, nomor",
                    "     asing harus memberi 0. Kasus pinggirnya nomor kosong (\"\"), yang",
                    "     juga harus memberi 0.",
                    "",
                    "Jebakan: kalau hp-nya sendiri null, get pada Map.of(...) langsung",
                    "melempar NullPointerException sebelum Optional sempat membungkusnya.",
                    "Pastikan dulu masukannya nggak null.",
                ]
            },
        ],
    },
    {
        "title": "34. Multithreading & Concurrency Dasar",
        "sections": [
            {
                "body": [
                    "Thread adalah jalur eksekusi program, yaitu satu urutan perintah yang",
                    "dikerjakan satu per satu. Normalnya program Java berjalan di satu",
                    "thread, namanya main thread. Multithreading artinya menjalankan",
                    "beberapa bagian kode secara bersamaan, masing-masing di thread-nya",
                    "sendiri.",
                    "",
                    "Gunanya:",
                    "  - Program lebih responsif. Misalnya tampilan (UI) nggak macet waktu",
                    "    ada data yang lagi dimuat.",
                    "  - CPU yang punya banyak inti (multi-core) bisa dipakai semuanya.",
                    "  - Cocok untuk tugas paralel, misalnya mengunduh banyak berkas",
                    "    sekaligus.",
                    "",
                    "Ada dua cara bikin thread:",
                    "  1. extends Thread, lalu override run().",
                    "  2. implements Runnable, lalu jalankan lewat new Thread(runnable).",
                    "",
                    "Cara kedua lebih disarankan. Java nggak punya multiple inheritance,",
                    "artinya sebuah class cuma boleh extends satu class. Kalau class-mu udah",
                    "extends Thread, dia nggak bisa extends class lain lagi.",
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
                    "Ada satu baris di contoh tadi yang belum dijelaskan, dan bentuknya",
                    "bakal sering muncul:",
                    "",
                    "  public static void main(String[] args) throws InterruptedException",
                    "",
                    "Method main tiba-tiba punya throws gara-gara t1.join(). Nanti",
                    "Thread.sleep() juga begitu. Dua method itu bisa disela di tengah",
                    "jalan, maksudnya thread lain bisa minta dia berhenti menunggu. Keduanya",
                    "melempar InterruptedException, dan InterruptedException termasuk",
                    "checked exception. Java menolak mengompilasi kalau kamu nggak",
                    "mengurusnya (lihat materi Exception Handling).",
                    "",
                    "Ada dua cara mengurusnya, dan pilihannya tergantung tempat kodenya:",
                    "  1. throws di tanda tangan method, yaitu baris deklarasinya. Artinya",
                    "     urusannya diserahkan ke pemanggil. Cara ini praktis untuk main,",
                    "     karena di atas main memang udah nggak ada siapa-siapa lagi.",
                    "  2. try-catch. Ini wajib kalau kodenya ada di dalam run().",
                    "     Runnable.run() udah ditetapkan tanpa throws, dan method yang",
                    "     meng-override nggak boleh menambah checked exception baru.",
                    "",
                    "Thread.sleep(ms) artinya hentikan thread ini selama sekian milidetik:",
                    "  Thread.sleep(1000);   // satu detik",
                    "Yang ditidurkan adalah thread yang memanggilnya, thread lain nggak",
                    "kena. Kalau ditulis di dalam main, yang berhenti main, dan t1 tetap",
                    "jalan. Di contoh-contoh concurrency, yaitu kode yang menjalankan",
                    "beberapa pekerjaan sekaligus, sleep dipakai untuk pura-pura sedang",
                    "mengerjakan sesuatu yang lama, supaya urutan kejadiannya kelihatan.",
                    "",
                    "Setiap kali menangkap InterruptedException, tiru pola ini apa adanya:",
                    "",
                    "  } catch (InterruptedException e) {",
                    "      Thread.currentThread().interrupt();",
                    "  }",
                    "",
                    "Alasannya begini. Setiap thread punya satu tanda yang artinya \"ada yang",
                    "minta kamu berhenti\". Waktu sleep melihat tanda itu, dia melempar",
                    "InterruptedException sekaligus menghapus tandanya. Kalau kamu menangkap",
                    "exception-nya lalu diam aja, permintaan berhenti tadi hilang tanpa",
                    "jejak, dan bagian program di atasmu nggak bakal pernah tahu. Memanggil",
                    "interrupt() memasang tandanya lagi.",
                    "",
                    "Jangan pernah bikin catch kosong untuk InterruptedException.",
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
                    "Race condition adalah bug yang muncul waktu beberapa thread mengubah",
                    "data yang sama pada saat bersamaan. Hasilnya jadi nggak bisa ditebak.",
                    "",
                    "Salah satu solusinya kata kunci synchronized. Kata kunci ini mengunci",
                    "aksesnya, jadi thread-thread itu bergiliran satu per satu:",
                    "  synchronized void tambahSaldo(double jumlah) {",
                    "      saldo += jumlah;   // aman, hanya 1 thread pada satu waktu",
                    "  }",
                    "",
                    "ExecutorService adalah cara modern mengelola banyak thread lewat thread",
                    "pool, yaitu sekumpulan thread yang dipakai bergantian. Cara ini lebih",
                    "efisien daripada bikin Thread satu per satu secara manual:",
                    "  ExecutorService pool = Executors.newFixedThreadPool(4);",
                    "  pool.submit(() -> System.out.println(\"Tugas jalan\"));",
                    "  pool.shutdown();",
                    "",
                    "Topik ini dalam. Untuk sekarang cukup pahami konsep dasarnya dulu.",
                    "Materi berikutnya, Concurrency Lanjutan, membahas ExecutorService lebih",
                    "jauh, dan sisanya bisa kamu perdalam waktu mulai bikin aplikasi",
                    "backend sungguhan.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Server toko online melayani banyak pembeli pada saat yang sama, dan",
                    "tiap permintaan bisa jalan di thread-nya sendiri. Selama mereka cuma",
                    "membaca, nggak ada masalah. Masalah muncul waktu dua thread mengubah",
                    "data yang sama, misalnya stok barang terakhir saat flash sale.",
                    "",
                    "Kasus kecil: stok sepatu promo tinggal 1. Dua pembeli menekan tombol",
                    "beli hampir bersamaan, dan dua-duanya dapat pesan berhasil. Stoknya",
                    "jadi -1, padahal barangnya cuma satu.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Cari data yang dipakai bersama, yaitu field stok. Lalu cari langkah",
                    "     yang harus utuh: cek stok, kemudian kurangi.",
                    "  2. Bayangkan urutan terburuknya. Thread A ngecek stok 1, lalu thread B",
                    "     juga ngecek stok 1 sebelum A sempat mengurangi. Dua-duanya lolos.",
                    "  3. Tandai method yang ngecek dan mengurangi itu dengan synchronized,",
                    "     supaya cuma satu thread yang bisa masuk dalam satu waktu:",
                    "      synchronized boolean beli() {",
                    "          if (stok == 0) return false;",
                    "          stok--;",
                    "          return true;",
                    "      }",
                    "  4. Uji dengan dua thread yang memanggil beli() untuk stok 1, lalu",
                    "     ulangi ribuan kali. Hasilnya harus selalu satu true dan satu false,",
                    "     dan stok akhirnya 0.",
                    "",
                    "Jebakan: bug seperti ini jarang muncul waktu dicoba sekali dua kali di",
                    "laptopmu. Dia baru muncul waktu programnya dipakai banyak orang, jadi",
                    "lolos uji coba sekali belum membuktikan kodenya aman.",
                ]
            },
        ],
    },
    {
        "title": "35. Concurrency Lanjutan: Future, Atomic, dan Koleksi Aman-Thread",
        "sections": [
            {
                "body": [
                    "Materi Multithreading & Concurrency Dasar sengaja berhenti di dasar:",
                    "thread, race condition, synchronized, dan satu baris pool.submit().",
                    "Materi itu berhenti tepat sebelum dua hal yang paling sering muncul di",
                    "kode Java sungguhan:",
                    "  1. Cara mengambil hasil tugas yang udah dilempar ke thread lain.",
                    "  2. Cara berbagi data antar-thread tanpa menulis kunci sendiri.",
                    "",
                    "Di kode backend zaman sekarang, synchronized jarang diketik tangan.",
                    "Yang dipakai adalah perkakas siap pakai di paket java.util.concurrent,",
                    "dan materi ini membahas perkakas itu.",
                    "",
                    "ExecutorService lebih dalam",
                    "",
                    "Ada dua cara menyerahkan tugas ke ExecutorService:",
                    "  - execute(Runnable): langsung jalan, dan nggak ada nilai kembalian.",
                    "    Kalau tugasnya melempar exception, stack trace-nya cuma dicetak ke",
                    "    System.err atas nama thread pool itu, misalnya Exception in thread",
                    "    \"pool-1-thread-1\".",
                    "  - submit(tugas): mengembalikan Future, semacam tanda terima. Hasil",
                    "    tugas itu, atau error-nya, nanti muncul di Future ini.",
                    "",
                    "Jenis pool yang disediakan class Executors:",
                    "  - newFixedThreadPool(n): n thread tetap. Kalau ragu, ini pilihan",
                    "    yang aman.",
                    "  - newSingleThreadExecutor(): 1 thread. Tugas dikerjakan berurutan",
                    "    sesuai antrean.",
                    "  - newCachedThreadPool(): thread dibuat sesuai kebutuhan, lalu dibuang",
                    "    sesudah menganggur 60 detik. Hati-hati kalau bebannya besar, karena",
                    "    jumlah thread-nya bisa membengkak.",
                    "  - newScheduledThreadPool(n): bisa menunda tugas, atau mengulangnya",
                    "    secara berkala.",
                    "",
                    "Pool wajib dimatikan. Caranya:",
                    "  - shutdown(): menolak tugas baru, tapi tugas yang udah masuk antrean",
                    "    tetap diselesaikan.",
                    "  - shutdownNow(): menolak tugas baru, menyela (interrupt) tugas yang",
                    "    lagi jalan, lalu mengembalikan daftar tugas yang belum sempat",
                    "    dimulai.",
                    "  - awaitTermination(waktu, satuan): menunggu sampai pool selesai",
                    "    total. Hasilnya true kalau keburu, false kalau waktunya habis.",
                    "",
                    "Jebakan: thread di dalam pool bukan daemon thread. Daemon thread adalah",
                    "thread latar yang nggak menahan program untuk selesai. Karena thread",
                    "pool bukan daemon, lupa shutdown() berarti program menggantung dan",
                    "nggak pernah keluar, walaupun baris terakhir main() udah lama lewat.",
                    "",
                    "Sekilas, ini bentuk baru yang bakal kamu temui (Java 19+ dan 21).",
                    "Kenali aja dulu:",
                    "  // ExecutorService sekarang AutoCloseable, jadi boleh masuk try (...)",
                    "  try (ExecutorService pool = Executors.newFixedThreadPool(4)) {",
                    "      pool.submit(...);",
                    "  }   // shutdown() + menunggu sampai selesai dikerjakan otomatis di sini",
                    "",
                    "  Executors.newVirtualThreadPerTaskExecutor()    // Java 21: virtual thread",
                    "",
                    "Bentuk try (...) { } itu namanya try-with-resources. Apa pun yang",
                    "dibuka di dalam kurungnya otomatis ditutup begitu bloknya selesai.",
                    "Penjelasan lengkapnya ada di materi File I/O & Serialization.",
                    "",
                    "Virtual thread adalah thread yang murah. Ribuan sekaligus pun nggak",
                    "masalah, karena yang mengelolanya JVM, bukan sistem operasi. Cara",
                    "memakainya sama persis: tetap ExecutorService, Callable, dan Future.",
                    "Yang berubah cuma ongkosnya.",
                    "",
                    "Bedanya Runnable dan Callable<T>:",
                    "  - Runnable: void run(). Nggak boleh melempar checked exception.",
                    "  - Callable<T>: T call() throws Exception. Mengembalikan nilai, dan",
                    "    boleh melempar exception.",
                    "  - Dua-duanya functional interface (lihat materi Lambda), jadi",
                    "    dua-duanya bisa ditulis sebagai lambda.",
                    "",
                    "Future<T> adalah tanda terima untuk tugas yang udah masuk antrean:",
                    "  - get(): menunggu sampai hasilnya siap. Selama menunggu, thread yang",
                    "    memanggilnya ikut berhenti (memblokir).",
                    "  - get(waktu, satuan): berhenti menunggu kalau waktunya habis, lalu",
                    "    melempar TimeoutException. Tugasnya sendiri nggak ikut berhenti,",
                    "    dia tetap jalan di pool.",
                    "  - isDone(): udah kelar atau belum? Hasilnya true untuk tugas yang",
                    "    selesai, gagal, maupun dibatalkan.",
                    "  - cancel(true): membatalkan tugas. Nilai true artinya thread yang",
                    "    sedang mengerjakannya ikut disela (interrupt).",
                    "",
                    "Jebakan paling besar di sini: exception yang terjadi di dalam tugas",
                    "kiriman submit() nggak muncul di layar. Exception itu disimpan di",
                    "Future, dan baru dilempar waktu kamu memanggil get(), dibungkus",
                    "ExecutionException.",
                    "Penyebab aslinya diambil pakai e.getCause(). Kalau Future-nya nggak",
                    "pernah di-get, error itu hilang tanpa jejak sama sekali. Makanya",
                    "submit() yang hasilnya dibiarkan begitu aja adalah salah satu cara",
                    "paling gampang menyembunyikan bug sendiri.",
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
                    "Kenapa counter++ rusak kalau dipakai banyak thread? Di layar dia cuma",
                    "satu baris, tapi di CPU ada tiga langkah: baca nilai, tambah 1, tulis",
                    "balik. Dua thread bisa sama-sama membaca 100, lalu dua-duanya",
                    "menulis 101. Satu kenaikan hilang, dan nggak ada error apa pun.",
                    "",
                    "Bug kayak gini hampir nggak pernah muncul waktu dicoba sekali dua",
                    "kali. Dia muncul waktu programnya udah dipakai orang beneran",
                    "(produksi), sesekali, dan angkanya selalu kurang.",
                    "",
                    "Class Atomic (paket java.util.concurrent.atomic) menyelesaikan masalah",
                    "ini tanpa kunci:",
                    "  - AtomicInteger dan AtomicLong untuk penghitung.",
                    "  - AtomicReference<T> untuk satu objek yang diganti-ganti antar-thread.",
                    "",
                    "Method yang perlu kamu kenali:",
                    "  - incrementAndGet(): naikkan 1, lalu kembalikan nilai sesudah naik.",
                    "  - getAndIncrement(): kembalikan nilai sebelum naik. Bedanya persis",
                    "    seperti ++i dan i++.",
                    "  - addAndGet(n): tambah n sekaligus.",
                    "  - get() dan set(n): baca dan timpa nilainya.",
                    "  - compareAndSet(lama, baru): ganti cuma kalau isinya masih 'lama'.",
                    "    Hasilnya boolean.",
                    "",
                    "compareAndSet (disingkat CAS) adalah dasar semua class Atomic. Dia",
                    "memakai satu instruksi CPU yang membandingkan dan menulis dalam sekali",
                    "gerak, jadi nggak ada celah untuk disela thread lain.",
                    "",
                    "Kata kunci volatile paling sering disalahpahami, jadi baca",
                    "pelan-pelan:",
                    "  - Yang dijamin: setiap thread membaca nilai terbaru, bukan salinan",
                    "    basi di cache CPU-nya sendiri. Cocok untuk penanda seperti boolean",
                    "    berhenti.",
                    "  - Yang nggak dijamin: volatile itu bukan kunci. hitung++ pada",
                    "    variabel volatile tetap rusak. Yang dijaga cuma baca dan tulis",
                    "    masing-masing, sedangkan hitung++ butuh tiga langkah tadi",
                    "    sekaligus.",
                    "  - Butuh baca-ubah-tulis yang aman? Pakai Atomic, jangan volatile.",
                    "",
                    "Koleksi aman-thread",
                    "",
                    "HashMap dan ArrayList dari materi Collection Framework nggak aman",
                    "dipakai beberapa thread sekaligus. Penggantinya:",
                    "  - ConcurrentHashMap: pengganti HashMap. Banyak thread boleh menulis",
                    "    sekaligus.",
                    "  - CopyOnWriteArrayList: setiap kali ada penulisan, seluruh isinya",
                    "    disalin. Cuma cocok untuk daftar yang sering dibaca tapi jarang",
                    "    diubah, misalnya daftar listener (objek yang menunggu kabar dari",
                    "    objek lain).",
                    "  - BlockingQueue: antrean produsen-konsumen, yaitu satu pihak mengisi",
                    "    dan pihak lain mengambil. take() menunggu sampai ada isi, put()",
                    "    menunggu sampai ada ruang. Kamu nggak perlu wait/notify manual.",
                    "",
                    "HashMap biasa yang diisi dua thread sekaligus bisa rusak dengan banyak",
                    "cara. Entri bisa hilang, size() bisa memberi angka yang salah, dan di",
                    "Java versi lama get() pernah berputar selamanya sampai CPU mentok 100%.",
                    "Semuanya terjadi tanpa satu pun exception yang memberi tahu.",
                    "",
                    "Method ConcurrentHashMap yang memang aman dipakai bersamaan:",
                    "  - peta.merge(kunci, 1, Integer::sum): tambah 1, atau isi 1 kalau",
                    "    kuncinya belum ada.",
                    "  - peta.computeIfAbsent(kunci, k -> ...): hitung nilainya sekali aja",
                    "    (pola cache).",
                    "  - peta.putIfAbsent(kunci, nilai): isi cuma kalau kuncinya masih",
                    "    kosong.",
                    "",
                    "Catatan: get() lalu put() sebagai dua langkah terpisah tetap nggak",
                    "aman, walaupun petanya ConcurrentHashMap. Yang dijamin utuh cuma satu",
                    "panggilan method.",
                    "",
                    "Jadi pakai perkakas siap pakai di atas, dan jangan bikin kunci sendiri.",
                    "synchronized buatan tangan gampang berujung deadlock, yaitu dua thread",
                    "saling menunggu kunci yang dipegang lawannya. Deadlock nggak melempar",
                    "error apa pun. Programnya cuma diam membeku, dan itu jauh lebih susah",
                    "dilacak daripada program yang crash.",
                    "",
                    "Contoh terakhir memakai CompletableFuture, yaitu Future yang bisa",
                    "dirangkai. Ini bentuk asinkron yang paling sering kamu temui di kode",
                    "Java baru. Asinkron artinya kamu nggak menunggu hasilnya di tempat:",
                    "kerjanya jalan di thread lain, dan hasilnya diolah begitu tiba.",
                    "  supplyAsync(fn)     -> mulai kerja di thread lain, hasilnya menyusul.",
                    "  thenApply(fn)       -> olah hasilnya begitu tiba, tanpa memblokir.",
                    "  thenCombine(cf, fn) -> gabungkan hasil dua CompletableFuture.",
                    "  allOf(a, b, ...)    -> selesai kalau semuanya sudah selesai.",
                    "  join()              -> ambil hasil akhirnya. Sama seperti get(), tapi",
                    "                         tanpa checked exception, jadi enak dipakai di",
                    "                         dalam lambda.",
                    "  exceptionally(fn)   -> nilai cadangan kalau ada langkah yang gagal.",
                    "",
                    "Kalau kamu nggak memberi pool sendiri, semuanya jalan di",
                    "ForkJoinPool.commonPool(). Thread di sana daemon, jadi kalau main()",
                    "keburu selesai, kerjanya ikut mati di tengah jalan.",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Dasbor pemilik toko yang punya tiga cabang perlu omzet dari tiap",
                    "cabang. Kalau tiap panggilan ke server cabang makan satu detik dan",
                    "dijalankan berurutan, dasbornya menunggu tiga detik. ExecutorService",
                    "dan Future menjalankan ketiganya bersamaan, lalu mengumpulkan hasilnya.",
                    "",
                    "Kasus kecil: method omzetCabang(String cabang) butuh sekitar satu detik",
                    "untuk menjawab. Cabangnya ada tiga: Bandung, Bogor, dan Depok. Dasbor",
                    "harus menampilkan total omzet dalam waktu sekitar satu detik.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Periksa dulu apakah tugasnya saling bebas. Omzet Bandung nggak",
                    "     butuh omzet Bogor, jadi ketiganya boleh jalan bersamaan.",
                    "  2. Kirim tiap cabang sebagai tugas ke pool, lalu simpan Future-nya:",
                    "      ExecutorService pool = Executors.newFixedThreadPool(3);",
                    "      List<Future<Integer>> hasil = new ArrayList<>();",
                    "      for (String c : cabang) hasil.add(pool.submit(() -> omzetCabang(c)));",
                    "      int total = 0;",
                    "      for (Future<Integer> f : hasil) total += f.get();   // menunggu",
                    "      pool.shutdown();",
                    "  3. Ukur waktunya. Tiga tugas yang masing-masing satu detik selesai",
                    "     dalam kira-kira satu detik, karena pool-nya punya tiga thread.",
                    "  4. Cek kasus pinggirnya: kalau satu cabang error, f.get() melempar",
                    "     ExecutionException, dan penyebab aslinya ada di getCause().",
                    "     Tangkap per cabang, supaya dua cabang lain tetap terhitung.",
                    "",
                    "Jebakan: kalau pool.shutdown() lupa dipanggil, thread di pool tetap",
                    "hidup dan programnya nggak pernah selesai, walaupun main() udah sampai",
                    "baris terakhir.",
                ]
            },
        ],
    },
    {
        "title": "36. File I/O & Serialization",
        "sections": [
            {
                "body": [
                    "File I/O artinya membaca dan menulis data ke berkas. I/O singkatan dari",
                    "Input/Output, yaitu masukan dan keluaran. Gunanya untuk menyimpan data",
                    "supaya nggak hilang waktu programnya ditutup.",
                    "",
                    "Class utamanya ada di java.io dan java.nio.file:",
                    "  File            -> wakil jalur (path) sebuah berkas atau folder.",
                    "  FileWriter      -> menulis teks ke berkas.",
                    "  FileReader / BufferedReader -> membaca teks dari berkas.",
                    "  Files (java.nio.file) -> API modern, lebih ringkas.",
                    "",
                    "Semua operasi berkas bisa melempar IOException, yang termasuk checked",
                    "exception. Jadi kamu harus mengurusnya pakai try-catch atau throws.",
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
                    "Contoh tadi memakai try-with-resources:",
                    "  try (Resource r = ...) { ... }",
                    "Resource di sini artinya sesuatu yang harus ditutup sesudah dipakai,",
                    "misalnya berkas yang dibuka. Resource yang ditulis di dalam kurung try",
                    "otomatis ditutup (close() dipanggil), walaupun terjadi error. Kamu",
                    "nggak perlu lagi nulis finally { r.close(); } sendiri. Syaratnya,",
                    "resource itu harus implements AutoCloseable.",
                    "",
                    "Serialization artinya mengubah objek Java jadi deretan byte (byte",
                    "stream), supaya bisa disimpan ke berkas atau dikirim lewat jaringan:",
                    "  class Mahasiswa implements Serializable { ... }",
                    "  ObjectOutputStream -> menulis objek ke berkas.",
                    "  ObjectInputStream  -> membaca objek dari berkas.",
                    "",
                    "Hati-hati: jangan memakai ObjectInputStream untuk membaca data dari",
                    "sumber yang nggak kamu percaya, misalnya berkas kiriman orang lain atau",
                    "data dari jaringan. Data serialisasi yang sengaja dirusak bisa dipakai",
                    "penyerang untuk menjalankan kode di komputermu.",
                    "",
                    "Untuk data terstruktur seperti konfigurasi, sekarang orang lebih sering",
                    "memakai format JSON dengan library seperti Jackson atau Gson.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Kasir dan aplikasi gudang sering bertukar data lewat berkas CSV, yaitu",
                    "teks yang kolomnya dipisah koma. Berkas seperti itu bisa dibuka di",
                    "Excel, diekspor dari aplikasi lain, atau dikirim lewat email. Membacanya",
                    "baris demi baris lalu menghitung totalnya adalah tugas yang umum.",
                    "",
                    "Kasus kecil: berkas penjualan.csv diawali baris judul",
                    "tanggal,barang,jumlah,harga, lalu satu baris per transaksi, misalnya",
                    "2026-10-01,Gula,3,17500. Pemilik toko mau total uang dari semua",
                    "transaksi.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Masukannya satu berkas, keluarannya satu angka. Baris pertama itu",
                    "     judul kolom, jadi harus dilewati.",
                    "  2. Baca semua barisnya dengan Files.readAllLines, pecah tiap baris",
                    "     dengan split(\",\"), lalu kalikan kolom jumlah dan harga:",
                    "      List<String> baris = Files.readAllLines(Path.of(\"penjualan.csv\"));",
                    "      int total = 0;",
                    "      for (String b : baris.subList(1, baris.size())) {   // lewati judul",
                    "          String[] k = b.split(\",\");",
                    "          total += Integer.parseInt(k[2]) * Integer.parseInt(k[3]);",
                    "      }",
                    "  3. Urus IOException-nya, karena exception itu checked: bungkus dengan",
                    "     try-catch, atau tulis throws IOException di method-nya.",
                    "  4. Cek kasus pinggirnya: baris kosong, misalnya karena ada Enter",
                    "     berlebih di akhir berkas, bikin k[2] melempar",
                    "     ArrayIndexOutOfBoundsException. Lewati baris yang isBlank() sebelum",
                    "     di-split.",
                    "",
                    "Jebakan: berkas CSV dari Excel kadang memakai titik koma (;) sebagai",
                    "pemisah, tergantung setelan bahasa komputernya. Lihat dulu satu",
                    "barisnya sebelum memilih pemisah untuk split.",
                ]
            },
        ],
    },
    {
        "title": "37. JDBC: Menghubungkan Java ke Database",
        "sections": [
            {
                "body": [
                    "JDBC (Java Database Connectivity) adalah API bawaan Java untuk",
                    "menghubungkan aplikasi Java dengan database, misalnya MySQL atau",
                    "PostgreSQL.",
                    "",
                    "Langkah dasarnya:",
                    "  1. Tambahkan driver database ke project, misalnya mysql-connector-j.",
                    "     Driver itu library yang tahu cara ngobrol dengan satu jenis",
                    "     database tertentu.",
                    "  2. Buat koneksi pakai DriverManager.getConnection(url, user, pass).",
                    "  3. Buat Statement atau PreparedStatement untuk menjalankan query.",
                    "  4. Proses ResultSet, yaitu hasil query SELECT.",
                    "  5. Tutup koneksinya, atau pakai try-with-resources supaya ditutup",
                    "     otomatis.",
                    "",
                    "Format URL koneksi MySQL:",
                    "  jdbc:mysql://localhost:3306/nama_database",
                    "Di URL itu, localhost artinya komputermu sendiri, dan 3306 adalah",
                    "nomor port bawaan MySQL.",
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
                    "Kalau kamu menekan Jalankan pada contoh di atas, yang keluar cuma",
                    "\"Error database: No suitable driver found for",
                    "jdbc:mysql://localhost:3306/belajar_db\". Itu wajar. Driver MySQL-nya",
                    "belum ada di aplikasi ini, dan kodenya juga butuh server MySQL yang",
                    "jalan di komputermu. Untuk mencobanya sungguhan, kamu perlu memasang",
                    "MySQL dan menambahkan driver-nya ke project.",
                    "",
                    "Jangan pernah menggabungkan teks query dengan input pengguna secara",
                    "langsung. Selalu pakai PreparedStatement. Kalau digabung langsung,",
                    "programmu rawan SQL injection, yaitu input yang sengaja ditulis supaya",
                    "mengubah isi query-mu.",
                    "",
                    "  // BAHAYA - jangan ditiru:",
                    "  String sql = \"SELECT * FROM users WHERE nama = '\" + input + \"'\";",
                    "",
                    "Misalnya pengguna mengetik ' OR '1'='1 sebagai nama. Query-nya berubah",
                    "jadi begini, dan seluruh isi tabel users ikut terambil:",
                    "  SELECT * FROM users WHERE nama = '' OR '1'='1'",
                    "",
                    "Bentuk yang aman memakai placeholder, yaitu tanda ? yang nanti diisi",
                    "lewat method setString dan kawan-kawannya:",
                    "",
                    "  // AMAN - gunakan placeholder ?:",
                    "  PreparedStatement stmt = conn.prepareStatement(",
                    "      \"SELECT * FROM users WHERE nama = ?\");",
                    "  stmt.setString(1, input);",
                    "",
                    "Dengan PreparedStatement, input pengguna selalu diperlakukan sebagai",
                    "data, nggak pernah sebagai bagian dari perintah SQL.",
                    "",
                    "INSERT, UPDATE, dan DELETE pakai executeUpdate(), bukan executeQuery():",
                    "  int baris = stmt.executeUpdate();  // jumlah baris terpengaruh",
                    "",
                    "Kata sandi di contoh tadi ditulis langsung di kode supaya contohnya",
                    "pendek. Di proyek sungguhan, simpan kata sandi di luar kode, misalnya",
                    "di variabel lingkungan (environment variable), supaya nggak ikut",
                    "tersimpan di Git dan terbaca orang lain.",
                    "",
                    "Untuk project nyata, biasanya dipakai ORM seperti Hibernate/JPA, atau",
                    "framework Spring Data JPA, yang bikin kode JDBC seperti di atas jauh",
                    "lebih sederhana. ORM (Object-Relational Mapping) memetakan tabel",
                    "database ke class Java, jadi kamu nggak perlu menulis query dan",
                    "membaca ResultSet satu per satu.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aplikasi sekolah, kasir, dan toko online menyimpan datanya di database,",
                    "dan di Java pintunya JDBC. Salah satu fitur pertama yang biasanya",
                    "diminta adalah kotak pencarian. Kotak itu menerima teks bebas dari",
                    "pengguna, jadi di situlah PreparedStatement paling dibutuhkan.",
                    "",
                    "Kasus kecil: aplikasi data siswa butuh pencarian nama. Guru mengetik",
                    "\"ruf\", dan hasilnya harus memuat siswa bernama Ma'ruf dan Rufi. Versi",
                    "lama menyambung teks pencarian langsung ke query, dan query-nya rusak",
                    "begitu ada guru yang mengetik Ma'ruf.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Masukannya teks dari kotak pencarian, keluarannya daftar nama. Teks",
                    "     itu datang dari pengguna, jadi wajib lewat placeholder ?.",
                    "  2. Pencarian sebagian di SQL memakai LIKE dengan tanda %. Tempelkan %",
                    "     ke nilainya, jangan ke teks SQL-nya:",
                    "      String sql = \"SELECT nama FROM siswa WHERE nama LIKE ?\";",
                    "      try (PreparedStatement st = conn.prepareStatement(sql)) {",
                    "          st.setString(1, \"%\" + cari + \"%\");",
                    "          ResultSet rs = st.executeQuery();    // ikut ditutup bersama st",
                    "          while (rs.next()) System.out.println(rs.getString(\"nama\"));",
                    "      }",
                    "  3. Uji kasus pinggirnya: cari \"Ma'ruf\". Dengan PreparedStatement,",
                    "     tanda kutip itu diperlakukan sebagai data biasa, jadi query-nya",
                    "     tetap utuh.",
                    "  4. Uji juga teks kosong. \"%\" + \"\" + \"%\" jadi \"%%\", yang cocok dengan",
                    "     semua nama. Putuskan apakah itu memang yang kamu mau, atau kotak",
                    "     kosong harus ditolak lebih dulu.",
                    "",
                    "Jebakan: perintah yang mengubah data, seperti INSERT dan UPDATE,",
                    "dijalankan dengan executeUpdate(). Kalau dipanggil lewat",
                    "executeQuery(), driver biasanya menolaknya dengan SQLException.",
                ]
            },
        ],
    },
    {
        "title": "38. Unit Testing dengan JUnit",
        "sections": [
            {
                "body": [
                    "Unit testing artinya menguji bagian kecil kode, biasanya satu method,",
                    "secara otomatis. Tujuannya memastikan hasil method itu sesuai harapan.",
                    "",
                    "Manfaatnya:",
                    "  1. Bug ketemu lebih awal, sebelum programnya dipakai orang",
                    "     (production).",
                    "  2. Kamu berani merapikan susunan kode (refactor) tanpa takut merusak",
                    "     fitur lain.",
                    "  3. Test jadi dokumentasi hidup, karena test menunjukkan cara memakai",
                    "     kodenya.",
                    "  4. Di dunia kerja profesional, test itu wajib. Sistem CI/CD, yang",
                    "     otomatis membangun dan menguji kode setiap ada perubahan, selalu",
                    "     menjalankan test.",
                    "",
                    "JUnit 5 adalah framework testing paling populer di Java. Framework itu",
                    "kerangka kerja siap pakai: kamu tinggal menulis test-nya, JUnit yang",
                    "menjalankan dan melaporkan hasilnya. Anotasi utamanya:",
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
                    "Assertion adalah pengecekan di dalam test. Yang sering dipakai:",
                    "  assertEquals(expected, actual) -> nilai harus sama",
                    "  assertTrue(kondisi) / assertFalse(kondisi)",
                    "  assertNull(obj) / assertNotNull(obj)",
                    "  assertThrows(Exception.class, () -> { ... }) -> harus melempar error",
                    "",
                    "Supaya test-nya jelas, pakai pola AAA (Arrange, Act, Assert):",
                    "  1. Arrange: siapkan data atau objek yang dibutuhkan.",
                    "  2. Act: panggil method yang diuji.",
                    "  3. Assert: periksa apakah hasilnya sesuai harapan.",
                    "",
                    "Test coverage artinya seberapa banyak baris kode yang ikut teruji oleh",
                    "test. Target yang umum di industri 70-90%, dan nggak harus 100%.",
                    "",
                    "Kode di atas butuh library JUnit, yang nggak ikut terpasang bersama",
                    "JDK. Di proyek sungguhan, test dijalankan lewat build tool seperti",
                    "Maven (mvn test) atau Gradle (./gradlew test). Dua alat itu dibahas di",
                    "materi Git, Maven/Gradle & Alur Kerja Developer.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Di tim yang memakai CI, semua tes dijalankan otomatis setiap kali ada",
                    "kode yang di-push, dan kode yang bikin tes gagal nggak boleh digabung.",
                    "Tes paling berguna ditulis untuk aturan bisnis yang punya batas, karena",
                    "di angka batas itulah bug paling sering ngumpet.",
                    "",
                    "Kasus kecil: aturan toko bilang belanja Rp100.000 ke atas dapat diskon",
                    "10%. Ada laporan pembeli yang belanja tepat Rp100.000 tapi nggak dapat",
                    "diskon. Kamu diminta memperbaikinya tanpa merusak yang lain.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tulis aturannya sebagai contoh angka dulu: 99.999 dapat 0, 100.000",
                    "     dapat 10.000, dan 150.000 dapat 15.000.",
                    "  2. Ubah tiap contoh jadi satu assertEquals di dalam method @Test:",
                    "      @Test",
                    "      void diskonMulaiTepatSeratusRibu() {",
                    "          assertEquals(0, Kasir.diskon(99_999));",
                    "          assertEquals(10_000, Kasir.diskon(100_000));",
                    "          assertEquals(15_000, Kasir.diskon(150_000));",
                    "      }",
                    "  3. Jalankan tesnya sebelum memperbaiki apa pun. Baris 100_000 harus",
                    "     gagal dengan pesan expected: <10000> but was: <0>. Kegagalan itu",
                    "     bukti tesmu memang menangkap bug-nya.",
                    "  4. Cari penyebabnya di kode, biasanya > yang seharusnya >=. Perbaiki,",
                    "     lalu jalankan ulang semua tes sampai hijau.",
                    "",
                    "Ingat: tes ini tetap tinggal di proyek sesudah bug-nya beres. Kalau",
                    "suatu hari ada yang mengubah syaratnya lagi, CI langsung menolak",
                    "perubahan itu.",
                ]
            },
        ],
    },
    {
        "title": "39. Design Pattern & Clean Code",
        "sections": [
            {
                "body": [
                    "Design pattern adalah solusi umum untuk masalah desain yang sering",
                    "berulang waktu bikin software. Design pattern nggak berbentuk kode siap",
                    "pakai. Dia lebih mirip pola pikir: cara menyusun class yang udah",
                    "terbukti berhasil, dan kodenya tetap kamu tulis sendiri.",
                    "",
                    "Beberapa pattern yang populer:",
                    "  Singleton  -> memastikan cuma ada satu objek (instance) dari sebuah class.",
                    "  Factory    -> menyembunyikan logika pembuatan objek yang rumit.",
                    "  Builder    -> membangun objek yang rumit langkah demi langkah.",
                    "  Observer   -> objek 'berlangganan' perubahan dari objek lain.",
                    "  Strategy   -> menukar algoritma atau perilaku saat program jalan.",
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
                    "Ada dua baris di kode itu yang memakai kata static dengan arti yang",
                    "beda. Dua-duanya gampang terlewat karena kelihatan seperti kata sambung",
                    "biasa.",
                    "",
                    "  private static Konfigurasi instance;",
                    "",
                    "static di sini menandai field. Artinya cuma ada satu nilai untuk",
                    "seluruh aplikasi, nggak satu per objek (lihat materi Anggota Class).",
                    "Sifat itu yang bikin Singleton bisa jalan. Kalau instance disimpan per",
                    "objek, setiap pemanggil punya salinannya sendiri, dan nggak ada lagi",
                    "yang namanya \"satu\".",
                    "",
                    "  static class Builder { ... }",
                    "",
                    "static di sini menandai class di dalam class, yaitu static nested class",
                    "(lihat materi Class di dalam Class). Builder tinggal di dalam",
                    "Mahasiswa, jadi dari luar namanya Mahasiswa.Builder. Makanya",
                    "pemanggilannya ditulis new Mahasiswa.Builder(), bukan new Builder().",
                    "Kata static-nya berarti Builder nggak butuh objek Mahasiswa untuk",
                    "dibuat. Memang harus begitu, karena Builder justru ada untuk membuat",
                    "Mahasiswa yang belum ada.",
                ]
            },
            {
                "body": [
                    "Prinsip clean code, yaitu cara menulis kode yang gampang dibaca dan",
                    "dirawat:",
                    "  1. Pakai nama yang jelas: hitungTotalBelanja() lebih baik daripada",
                    "     htb().",
                    "  2. Satu method, satu tanggung jawab (Single Responsibility).",
                    "  3. Hindari magic number, yaitu angka yang muncul begitu aja tanpa",
                    "     nama. Pakai konstanta bernama:",
                    "       final double PPN = 0.11;   bukan   total * 0.11",
                    "  4. Method sebaiknya pendek, idealnya kurang dari 20-30 baris.",
                    "  5. Hindari duplikasi kode (prinsip DRY: Don't Repeat Yourself).",
                    "  6. Tulis komentar yang menjelaskan kenapa kodenya ditulis begitu.",
                    "     Apa yang dikerjakan kode udah kelihatan dari kodenya sendiri.",
                    "  7. Ikuti format dan kebiasaan penamaan yang dipakai tim atau project.",
                    "",
                    "Prinsip SOLID untuk OOP yang rapi:",
                    "  - S, Single Responsibility: satu class, satu tanggung jawab.",
                    "  - O, Open/Closed: terbuka untuk ekstensi, tertutup untuk modifikasi.",
                    "    Artinya perilaku baru ditambahkan lewat class baru, tanpa mengubah",
                    "    kode lama yang udah jalan.",
                    "  - L, Liskov Substitution: subclass harus bisa menggantikan class",
                    "    induknya tanpa bikin program salah.",
                    "  - I, Interface Segregation: interface yang kecil dan spesifik lebih",
                    "    baik daripada satu interface raksasa.",
                    "  - D, Dependency Inversion: bergantung pada abstraksi (misalnya",
                    "    interface), bukan pada implementasi.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Toko online yang bekerja sama dengan beberapa kurir sering punya method",
                    "hitungOngkir berisi if-else panjang, satu cabang per layanan. Tiap kali",
                    "ada layanan baru, method itu dibongkar lagi. Pola Strategy memindahkan",
                    "tiap rumus ke objeknya sendiri, sesuai prinsip Open/Closed.",
                    "",
                    "Kasus kecil: ongkir dihitung per kilogram dan dibulatkan ke atas.",
                    "Layanan reguler Rp9.000 per kg, layanan kilat Rp15.000 per kg. Paket",
                    "1.500 gram lewat kilat harus kena Rp30.000, dan bulan depan ada layanan",
                    "kargo yang mau ditambahkan.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Cari bagian yang berubah-ubah, yaitu rumus tarif tiap layanan.",
                    "     Bagian itu yang dipisah jadi strategi.",
                    "  2. Bikin interface satu method, lalu daftarkan tiap rumus sebagai",
                    "     lambda di sebuah Map:",
                    "      interface Tarif { int hitung(int gram); }",
                    "      Map<String, Tarif> tarif = Map.of(",
                    "          \"reguler\", g -> 9000 * ((g + 999) / 1000),",
                    "          \"kilat\",   g -> 15000 * ((g + 999) / 1000));",
                    "      int ongkir = tarif.get(\"kilat\").hitung(1500);   // 30000",
                    "  3. Waktu layanan kargo datang, cukup tambah satu entri di Map. Kode",
                    "     yang memanggil tarif.get(...) nggak berubah sama sekali.",
                    "  4. Cek kasus pinggirnya: nama layanan yang nggak terdaftar, termasuk",
                    "     \"Kilat\" yang huruf depannya besar, bikin tarif.get mengembalikan",
                    "     null. Periksa dulu dengan containsKey, lalu tampilkan pesan yang",
                    "     jelas.",
                    "",
                    "Ingat: angka 9000 dan 15000 di contoh ini masih magic number. Di kode",
                    "sungguhan, jadikan konstanta bernama seperti TARIF_REGULER_PER_KG.",
                ]
            },
        ],
    },
    {
        "title": "40. Git, Maven/Gradle & Alur Kerja Developer",
        "sections": [
            {
                "body": [
                    "Git adalah sistem version control, yaitu alat yang mencatat setiap",
                    "perubahan kode dan memudahkan kerja bareng developer lain. Git wajib",
                    "kamu kuasai.",
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
                    "",
                    "Repo (repository) adalah folder proyek yang riwayat perubahannya",
                    "dicatat Git. Aplikasi ini punya kurikulum Git & GitHub tersendiri kalau",
                    "kamu mau belajar lebih dalam.",
                ]
            },
            {
                "body": [
                    "Build tool seperti Maven dan Gradle mengurus dependency, yaitu library",
                    "dari luar yang dipakai project-mu. Selain itu build tool juga",
                    "mengompilasi kode, menjalankan test, dan membungkus aplikasinya jadi",
                    "berkas .jar atau .war.",
                    "",
                    "  Maven (pom.xml)          Gradle (build.gradle)",
                    "  ---------------          ---------------------",
                    "  Konfigurasi XML          Konfigurasi Groovy/Kotlin DSL",
                    "  mvn clean install        ./gradlew build",
                    "  mvn test                 ./gradlew test",
                    "",
                    "Contoh dependency di pom.xml (Maven):",
                    "  <dependency>",
                    "      <groupId>com.mysql</groupId>",
                    "      <artifactId>mysql-connector-j</artifactId>",
                    "      <version>8.0.33</version>",
                    "  </dependency>",
                    "groupId, artifactId, dan version bersama-sama menunjuk satu library",
                    "tertentu. Maven lalu mengunduh library itu untukmu.",
                    "",
                    "Alur kerja developer profesional, ringkasnya:",
                    "  1. Ambil task atau issue dari board (Jira/Trello/GitHub Issues).",
                    "  2. Buat branch baru dari main atau develop.",
                    "  3. Tulis kode beserta unit test-nya.",
                    "  4. Commit dengan pesan yang jelas, lalu push ke remote.",
                    "  5. Buat Pull Request atau Merge Request supaya kodenya direview tim.",
                    "  6. Sesudah disetujui dan lolos CI (test otomatis), merge ke main.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Di tim yang memakai Java, library dari luar nggak disalin manual ke",
                    "folder proyek. Semuanya ditulis di pom.xml atau build.gradle, lalu Maven",
                    "atau Gradle yang mengunduhnya. Perubahan kode masuk lewat branch dan",
                    "pull request, supaya bisa direview dulu sebelum digabung ke main.",
                    "",
                    "Kasus kecil: proyek data siswa butuh driver MySQL. Cara yang pertama",
                    "terpikir: unduh berkas .jar driver, taruh di folder lib/, lalu commit.",
                    "Masalahnya, repo jadi membengkak, dan tiap kali versi driver naik,",
                    "semua orang harus menyalin ulang berkasnya.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Rumuskan tujuannya: semua laptop dan server CI harus memakai",
                    "     library yang sama persis, tanpa ada yang menyalin berkas .jar.",
                    "  2. Tulis dependency-nya di pom.xml, lengkap dengan groupId,",
                    "     artifactId, dan version.",
                    "  3. Kerjakan di branch sendiri, jalankan tes, lalu kirim:",
                    "      git branch tambah-driver-mysql",
                    "      git checkout tambah-driver-mysql",
                    "      mvn test",
                    "      git add pom.xml",
                    "      git commit -m \"Pakai driver MySQL lewat Maven\"",
                    "      git push origin tambah-driver-mysql",
                    "  4. Buka pull request, dan biarkan CI menjalankan tes di mesin yang",
                    "     bersih. Kalau di sana lulus, berarti nggak ada lagi yang bergantung",
                    "     pada berkas yang cuma ada di laptopmu.",
                    "",
                    "Jebakan: folder target/ berisi hasil build dan nggak boleh ikut",
                    "di-commit. Tulis target/ di berkas .gitignore, yaitu daftar berkas yang",
                    "sengaja nggak dicatat Git.",
                ]
            },
        ],
    },
    {
        "title": "41. Roadmap Menjadi Programmer Handal",
        "sections": [
            {
                "body": [
                    "Kamu udah menyelesaikan fondasi Java yang kuat. Berikut roadmap, alias",
                    "peta jalan, yang realistis untuk naik dari paham dasar sampai jadi",
                    "programmer handal yang siap kerja di industri.",
                    "",
                    "Tahap 1: kuatkan fondasi (kamu di sini)",
                    "  - Yang udah kamu pahami: variabel, OOP, collection, exception,",
                    "    lambda, stream.",
                    "  - Targetnya: kamu bisa menjelaskan semua konsep di atas dengan",
                    "    bahasamu sendiri. Hafal sintaks aja belum cukup.",
                    "",
                    "Tahap 2: bangun project nyata (3-6 bulan)",
                    "  1. To-Do List CLI, untuk latihan logika dan OOP dasar.",
                    "  2. Sistem Nilai Mahasiswa dengan berkas atau database, untuk latihan",
                    "     CRUD dan JDBC.",
                    "  3. REST API sederhana pakai Spring Boot, untuk belajar backend web.",
                    "  4. Aplikasi yang memakai testing (JUnit) dari awal, supaya kamu",
                    "     terbiasa dengan kebiasaan profesional.",
                ]
            },
            {
                "body": [
                    "Tahap 3: pelajari ekosistem industri (6-12 bulan)",
                    "  - Spring Boot / Spring Framework: standar backend Java di industri.",
                    "  - Spring Data JPA / Hibernate: ORM, pengganti JDBC manual.",
                    "  - REST API dan JSON (Jackson/Gson): komunikasi antar layanan.",
                    "  - Docker: containerization, yaitu membungkus aplikasi beserta semua",
                    "    kebutuhannya ke dalam container.",
                    "  - Git dan GitHub: kerja bareng tim. Yang ini wajib.",
                    "  - Message queue (Kafka/RabbitMQ): untuk sistem berskala besar.",
                    "  - Microservices: arsitektur aplikasi modern.",
                    "",
                    "Tahap 4: soft skill dan kebiasaan profesional",
                    "  1. Baca kode orang lain, misalnya proyek open source di GitHub.",
                    "  2. Ikut code review, dan terima kritik dengan terbuka.",
                    "  3. Biasakan menulis dokumentasi (README, komentar penting).",
                    "  4. Latihan algoritma dan struktur data (LeetCode/HackerRank).",
                    "  5. Ikut komunitas developer (Discord, forum, meetup lokal).",
                ]
            },
            {
                "body": [
                    "Kebiasaan harian supaya jadi handal:",
                    "  1. Ketik ulang semua contoh kode di aplikasi ini. Jangan copy-paste.",
                    "  2. Ubah-ubah kodenya, tebak dulu keluarannya, baru jalankan dan cek.",
                    "  3. Kerjakan minimal 1 latihan coding per hari. Konsisten lebih",
                    "     penting daripada cepat.",
                    "  4. Coba debug error sendiri dulu selama 15-30 menit sebelum nanya ke",
                    "     orang lain.",
                    "  5. Baca pesan error pelan-pelan. Pesan itu petunjuk paling akurat",
                    "     yang kamu punya.",
                    "  6. Bangun proyek kecil dari nol. Jangan cuma ngikutin tutorial tanpa",
                    "     bikin apa-apa sendiri.",
                    "  7. Kuasai SQL dan database kalau mau jadi full-stack developer.",
                    "  8. Ajarkan yang udah kamu pelajari ke orang lain (Feynman technique).",
                    "",
                    "Nggak ada programmer yang paham setiap baris kode di dunia. Itu",
                    "mustahil, dan programmer senior pun masih terus belajar tiap hari.",
                    "Programmer yang handal adalah yang fondasinya kuat, terbiasa membaca",
                    "dan memahami kode baru dengan cepat, dan nggak takut ketemu hal asing.",
                    "Target itu realistis, dan bisa kamu capai kalau belajarnya konsisten.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Lowongan junior Java developer biasanya menyebut syarat yang mirip:",
                    "Java dan OOP, SQL, Git, dan sering juga Spring Boot. Salah satu cara",
                    "menunjukkan bekal itu adalah satu proyek kecil yang selesai, bisa",
                    "dijalankan orang lain dari repo-mu, dan punya tes.",
                    "",
                    "Kasus kecil: kamu mau bikin proyek portofolio pertama, yaitu aplikasi",
                    "perpustakaan sekolah. Daftar fitur di kepalamu langsung panjang, mulai",
                    "dari login, Spring Boot, dan database, sampai aplikasi Android. Kamu",
                    "bingung harus mulai dari mana.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pangkas jadi versi terkecil yang tetap berguna: tambah buku,",
                    "     pinjam, kembalikan, dan hitung denda, semuanya lewat terminal.",
                    "  2. Petakan tiap fitur ke materi yang udah kamu pelajari:",
                    "      Buku, Peminjaman      class dan record",
                    "      daftar pinjaman       List dan Map",
                    "      denda terlambat       LocalDate dan ChronoUnit",
                    "      simpan data           Files dan berkas CSV",
                    "      aturan denda          tes JUnit",
                    "  3. Kerjakan satu fitur sampai jalan dan teruji, commit, baru pindah ke",
                    "     fitur berikutnya.",
                    "  4. Cek kasus pinggirnya sebelum menyebut proyeknya selesai: buku yang",
                    "     dipinjam dua kali, kode buku yang nggak ada, dan pengembalian di",
                    "     hari yang sama.",
                    "  5. Sesudah versi terminal stabil, baru ganti penyimpanannya ke",
                    "     database lewat JDBC, lalu ke Spring Boot.",
                    "",
                    "Ingat: tulis README yang menjelaskan cara menjalankan proyekmu. Orang",
                    "yang membuka repo-mu biasanya membaca README lebih dulu daripada",
                    "kodenya.",
                ]
            },
        ],
    },
]
