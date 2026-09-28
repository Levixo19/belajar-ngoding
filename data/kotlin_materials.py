KOTLIN_MATERIALS = [
    {
        "title": "1. Pengenalan Kotlin & Instalasi",
        "sections": [
            {
                "body": [
                    "Apa itu Kotlin?",
                    "  - Dibuat JetBrains, versi 1.0 rilis 2016.",
                    "  - Statically typed, dengan inferensi tipe yang kuat.",
                    "  - Berjalan di atas JVM, tapi juga bisa dikompilasi ke",
                    "    JavaScript, ke binari native, dan ke WebAssembly.",
                    "  - Sejak 2019 jadi bahasa yang DIUTAMAKAN untuk Android.",
                    "",
                    "Kotlin lahir dari satu keluhan yang sangat konkret: Java",
                    "terlalu banyak basa-basinya. Tujuan desainnya bukan jadi",
                    "bahasa yang paling canggih, melainkan bahasa yang bisa",
                    "menggantikan Java SECARA BERTAHAP di proyek yang sudah",
                    "ada.",
                    "",
                    "Itu sebabnya INTEROPERABILITAS jadi fitur utamanya:",
                    "  - Kode Kotlin bisa memanggil kode Java, dan sebaliknya.",
                    "  - Satu proyek boleh memuat berkas .java dan .kt sekaligus.",
                    "  - Seluruh ekosistem pustaka Java langsung bisa dipakai.",
                    "",
                    "Yang diperbaiki Kotlin dari Java, dan ini bukan daftar",
                    "kosmetik:",
                    "  - NULL diperiksa compiler. NullPointerException, yang",
                    "    di Java baru muncul saat program jalan, jadi error",
                    "    kompilasi di Kotlin.",
                    "  - Data class menggantikan 60 baris boilerplate POJO.",
                    "  - Tidak ada checked exception yang memaksa try-catch.",
                    "  - Extension function menambah method ke class yang",
                    "    bukan milikmu.",
                    "  - Coroutine untuk kode asinkron tanpa callback.",
                    "",
                    "Dipakai membangun: mayoritas aplikasi Android modern,",
                    "backend dengan Ktor dan Spring Boot, serta aplikasi",
                    "lintas platform lewat Compose Multiplatform.",
                    "",
                    "Instalasi:",
                    "  - Butuh JDK 17 atau lebih baru lebih dulu.",
                    "  - Fedora  : sudo dnf install kotlin",
                    "  - SDKMAN  : sdk install kotlin",
                    "  - macOS   : brew install kotlin",
                    "  - Windows : choco install kotlinc",
                    "  - Cek     : kotlinc -version",
                    "",
                    "Menjalankan:",
                    "  kotlinc main.kt -include-runtime -d main.jar",
                    "  java -jar main.jar",
                    "",
                    "  kotlinc main.kt -d kelas && kotlin -cp kelas MainKt",
                    "  kotlinc              sesi interaktif (REPL)",
                ]
            },
            {
                "heading": "Program pertama",
                "code": """fun main() {
    println("Halo Dunia!")
    println("Aku sedang belajar Kotlin.")

    val nama = "Andi"
    println("Halo, $nama! Umurmu ${2026 - 2006} tahun.")

    repeat(3) { i -> println("baris ke-${i + 1}") }
}"""
            },
            {
                "body": [
                    "Yang langsung terlihat berbeda dari Java:",
                    "",
                    "  - TIDAK ADA class pembungkus. `fun main()` boleh",
                    "    berdiri sendiri di level berkas.",
                    "  - TIDAK ADA titik koma.",
                    "  - TIDAK ADA `public static void`.",
                    "  - Tipe ditulis SESUDAH nama, dipisah titik dua.",
                    "  - `val` untuk yang tidak berubah, `var` untuk yang",
                    "    berubah.",
                    "",
                    "NAMA BERKAS menentukan nama class yang dihasilkan:",
                    "`main.kt` menghasilkan class `MainKt`, dan itulah yang",
                    "dijalankan JVM. Ini penting saat kamu menjalankannya",
                    "tanpa jar.",
                    "",
                    "INTERPOLASI memakai tanda dolar:",
                    "  \"$nama\"            variabel sederhana",
                    "  \"${2026 - 2006}\"   ekspresi apa pun, pakai kurawal",
                    "  \"\"\"mentah\"\"\"       tanpa escape, boleh multi-baris",
                    "",
                    "Untuk menulis tanda dolar harfiah, pakai `${'$'}` atau",
                    "escape `\\$`.",
                    "",
                    "`repeat(3) { ... }` adalah fungsi biasa yang menerima",
                    "LAMBDA sebagai argumen terakhir. Kotlin punya aturan",
                    "khusus: lambda yang jadi argumen terakhir boleh ditulis",
                    "DI LUAR tanda kurung. Itulah yang membuat kode Kotlin",
                    "sering terlihat seperti punya sintaks bawaan padahal",
                    "cuma pemanggilan fungsi biasa.",
                    "",
                    "Konvensi penamaan:",
                    "  camelCase       fungsi, properti, variabel lokal",
                    "  PascalCase      class, interface, object",
                    "  SCREAMING_CASE  konstanta di level atas",
                    "  Indentasi EMPAT spasi.",
                ]
            },
        ],
    },
    {
        "title": "2. val, var & Tipe Data",
        "sections": [
            {
                "body": [
                    "Dua kata kunci untuk variabel, dan memilihnya adalah",
                    "keputusan yang kamu ambil setiap baris:",
                    "",
                    "  val nama = \"Andi\"     TIDAK bisa diisi ulang",
                    "  var umur = 20         bisa diisi ulang",
                    "",
                    "`val` bukan berarti isinya beku — sebuah `val` yang",
                    "menunjuk MutableList tetap boleh ditambahi. Yang tidak",
                    "bisa diubah adalah ke mana ia menunjuk.",
                    "",
                    "ATURAN PRAKTIS: pakai `val` sampai compiler memaksamu",
                    "memakai `var`. Di kode Kotlin yang sehat, `var` jarang.",
                    "",
                    "Tipe boleh ditulis atau disimpulkan:",
                    "  val umur: Int = 20",
                    "  val umur = 20              sama saja",
                    "  var nanti: String          WAJIB bertipe kalau belum diisi",
                    "",
                    "Tipe bilangan:",
                    "  Byte    8 bit      Short   16 bit",
                    "  Int     32 bit     Long    64 bit",
                    "  Float   32 bit     Double  64 bit",
                    "  UByte UShort UInt ULong    tanpa tanda",
                    "",
                    "  Int adalah bawaan untuk bilangan bulat, Double untuk",
                    "  pecahan. Long ditulis 100L, Float ditulis 3.14f.",
                    "",
                    "Lainnya: Boolean, Char (kutip tunggal), String.",
                    "",
                    "Kotlin TIDAK PERNAH mengonversi tipe diam-diam. Bahkan",
                    "Int ke Long pun harus ditulis:",
                    "  val besar: Long = angka.toLong()",
                    "",
                    "Fungsi konversi: toByte, toShort, toInt, toLong,",
                    "toFloat, toDouble, toChar, toString.",
                    "",
                    "Dari teks ke angka, dan pilihannya penting:",
                    "  \"42\".toInt()          MELEMPAR kalau gagal",
                    "  \"42\".toIntOrNull()    null kalau gagal",
                    "",
                    "Untuk masukan pengguna, `toIntOrNull()` hampir selalu",
                    "yang benar — salah ketik adalah kejadian normal.",
                    "",
                    "Konstanta:",
                    "  const val MAKS = 100      saat KOMPILASI, level atas",
                    "  val sekarang = hitung()   saat program jalan",
                ]
            },
            {
                "heading": "Tipe, batas, dan konversi",
                "code": """fun main() {
    val umur: Int = 20
    val tinggi = 172.5          // Double
    val huruf = 'K'
    val aktif = true
    val panjang = 100L
    val kecil = 3.14f

    println("Int    : ${Int.MIN_VALUE} .. ${Int.MAX_VALUE}")
    println("Long   : ${Long.MIN_VALUE} .. ${Long.MAX_VALUE}")
    println("nilai  : $umur $tinggi $huruf $aktif $panjang $kecil")

    // Konversi WAJIB eksplisit
    val sebagaiLong: Long = umur.toLong()
    val sebagaiDouble: Double = umur.toDouble()
    println("konversi: $sebagaiLong $sebagaiDouble")

    // Pembagian bilangan bulat memotong
    println("7 / 2     = ${7 / 2}")
    println("7.0 / 2   = ${7.0 / 2}")
    println("7 % 2     = ${7 % 2}")

    // toIntOrNull: tidak melempar
    for (teks in listOf("42", "3.5", "abc", "")) {
        val n = teks.toIntOrNull()
        println("\\"$teks\\".toIntOrNull() = $n")
    }

    // val menunjuk tetap, ISINYA belum tentu
    val daftar = mutableListOf(1, 2, 3)
    daftar.add(4)               // boleh: yang ditunjuk sama
    println("val mutableList: $daftar")
}"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  Int    : -2147483648 .. 2147483647",
                    "  Long   : -9223372036854775808 .. 9223372036854775807",
                    "  nilai  : 20 172.5 K true 100 3.14",
                    "  konversi: 20 20.0",
                    "  7 / 2     = 3",
                    "  7.0 / 2   = 3.5",
                    "  7 % 2     = 1",
                    "  \"42\".toIntOrNull() = 42",
                    "  \"3.5\".toIntOrNull() = null",
                    "  \"abc\".toIntOrNull() = null",
                    "  \"\".toIntOrNull() = null",
                    "  val mutableList: [1, 2, 3, 4]",
                    "",
                    "Baris terakhir adalah hal yang paling sering",
                    "disalahpahami: `val` mencegah VARIABELNYA diisi ulang,",
                    "bukan ISINYA diubah. Untuk daftar yang benar-benar tidak",
                    "bisa diubah, pakai `listOf` alih-alih `mutableListOf`.",
                    "",
                    "Kotlin membedakan keduanya di TINGKAT TIPE:",
                    "  List<T>          hanya baca",
                    "  MutableList<T>   bisa ditambah dan dihapus",
                    "",
                    "Ini berbeda dari Java, tempat `List` selalu punya `add`",
                    "dan pelanggarannya baru ketahuan sebagai",
                    "UnsupportedOperationException saat program jalan.",
                    "",
                    "Catatan halus: `List<T>` di Kotlin disebut read-only,",
                    "BUKAN immutable. Kalau ia sebenarnya membungkus sebuah",
                    "MutableList, pemegang referensi lain masih bisa",
                    "mengubahnya. Untuk jaminan yang sesungguhnya, salin",
                    "dengan `.toList()`.",
                ]
            },
        ],
    },
    {
        "title": "3. Null Safety",
        "sections": [
            {
                "body": [
                    "Inilah fitur yang paling sering disebut orang saat",
                    "ditanya kenapa memilih Kotlin.",
                    "",
                    "Di Kotlin, sebuah tipe TIDAK BISA bernilai null kecuali",
                    "kamu menyatakannya:",
                    "",
                    "  var nama: String = \"Andi\"",
                    "  nama = null            ERROR KOMPILASI",
                    "",
                    "  var nama: String? = \"Andi\"",
                    "  nama = null            sah",
                    "",
                    "Tanda tanya di belakang tipe itulah seluruh fiturnya.",
                    "`String` dan `String?` adalah DUA TIPE BERBEDA, dan",
                    "compiler tidak akan mengizinkanmu memakai yang kedua",
                    "seolah-olah yang pertama.",
                    "",
                    "Akibatnya: NullPointerException, yang di Java baru",
                    "muncul saat program jalan di tangan pengguna, jadi error",
                    "kompilasi.",
                    "",
                    "Cara memakai nilai yang mungkin null:",
                    "",
                    "  SAFE CALL",
                    "    nama?.length          null kalau nama null",
                    "    a?.b?.c?.d            rantai, berhenti di null pertama",
                    "",
                    "  ELVIS",
                    "    nama?.length ?: 0     pakai 0 kalau kirinya null",
                    "    val n = cari() ?: return",
                    "    val n = cari() ?: throw IllegalStateException(\"...\")",
                    "",
                    "  SAFE CALL + let",
                    "    nama?.let { println(it.uppercase()) }",
                    "    Bloknya HANYA jalan kalau nama bukan null.",
                    "",
                    "  NOT-NULL ASSERTION",
                    "    nama!!.length         melempar NPE kalau null",
                    "",
                    "Dua tanda seru itu berkata 'percaya aku'. Setiap kali",
                    "kamu menulisnya, kamu memindahkan tanggung jawab dari",
                    "compiler ke dirimu sendiri. Kadang itu benar; tapi kalau",
                    "sebuah berkas penuh `!!`, yang sebenarnya terjadi adalah",
                    "fiturnya dimatikan diam-diam.",
                    "",
                    "SMART CAST — hal yang membuat null safety enak dipakai:",
                    "",
                    "  if (nama != null) {",
                    "      println(nama.length)    <- TANPA ?. atau !!",
                    "  }",
                    "",
                    "Compiler MENGINGAT bahwa kamu sudah memeriksanya. Ini",
                    "berlaku juga sesudah `is`, sesudah `return` lebih awal,",
                    "dan di dalam `when`.",
                    "",
                    "Smart cast TIDAK berlaku untuk `var` milik class yang",
                    "bisa diubah thread lain — di situ compiler tidak bisa",
                    "menjamin nilainya masih sama.",
                ]
            },
            {
                "heading": "Semua bentuk penanganan null",
                "code": """fun panjangAtauNol(teks: String?): Int = teks?.length ?: 0

fun sapa(nama: String?): String {
    // Pulang lebih awal: sesudah ini compiler tahu nama bukan null
    if (nama.isNullOrBlank()) return "(tanpa nama)"
    return "Halo, ${nama.trim().uppercase()}!"
}

data class Alamat(val kota: String?, val pos: String?)
data class Orang(val nama: String, val alamat: Alamat?)

fun main() {
    val daftar: List<String?> = listOf("Andi", null, "", "  ", "Budi")
    daftar.forEach { println("[${sapa(it)}]") }

    println("---")
    println("panjang \\"halo\\" : ${panjangAtauNol("halo")}")
    println("panjang null    : ${panjangAtauNol(null)}")

    println("---")
    val a = Orang("Andi", Alamat("Bandung", "40111"))
    val b = Orang("Budi", null)
    val c = Orang("Cici", Alamat(null, "12345"))

    for (o in listOf(a, b, c)) {
        // Rantai safe call: berhenti di null pertama
        val kota = o.alamat?.kota ?: "tidak diketahui"
        println("${o.nama.padEnd(6)}$kota")
    }

    println("---")
    // let: blok hanya jalan kalau bukan null
    val mungkin: String? = "isi"
    mungkin?.let { println("ada isinya: ${it.length} huruf") }
    val kosong: String? = null
    kosong?.let { println("ini tidak pernah tercetak") }
    println("sesudah let")

    println("---")
    // Smart cast sesudah pemeriksaan
    val apa: Any = "sebuah teks"
    if (apa is String) {
        println("panjangnya ${apa.length}")   // tanpa cast manual
    }

    // Menyaring null dari koleksi
    val bersih: List<String> = daftar.filterNotNull()
    println("tanpa null: $bersih")
}"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  [Halo, ANDI!]",
                    "  [(tanpa nama)]",
                    "  [(tanpa nama)]",
                    "  [(tanpa nama)]",
                    "  [Halo, BUDI!]",
                    "  ---",
                    "  panjang \"halo\" : 4",
                    "  panjang null    : 0",
                    "  ---",
                    "  Andi  Bandung",
                    "  Budi  tidak diketahui",
                    "  Cici  tidak diketahui",
                    "  ---",
                    "  ada isinya: 3 huruf",
                    "  sesudah let",
                    "  ---",
                    "  panjangnya 11",
                    "  tanpa null: [Andi, ,   , Budi]",
                    "",
                    "`isNullOrBlank()` menangani tiga kasus sekaligus: null,",
                    "string kosong, dan string berisi spasi saja. Pasangannya",
                    "`isNullOrEmpty()` yang tidak memeriksa spasi. Untuk",
                    "memvalidasi masukan pengguna, yang pertama hampir selalu",
                    "yang kamu maksud.",
                    "",
                    "Perhatikan baris Cici: alamatnya ADA tapi kotanya null,",
                    "dan rantai `o.alamat?.kota ?: \"...\"` menanganinya dengan",
                    "kode yang sama persis seperti Budi yang alamatnya null.",
                    "Itulah kekuatan safe call berantai.",
                    "",
                    "Fungsi bantu yang sering dipakai:",
                    "  x.orEmpty()            String? -> String",
                    "  daftar.filterNotNull() List<T?> -> List<T>",
                    "  x ?: return            pulang lebih awal",
                    "  requireNotNull(x)      melempar dengan pesan jelas",
                    "  checkNotNull(x)",
                    "",
                    "PERINGATAN soal Java: nilai yang datang dari pustaka",
                    "Java bertipe PLATFORM TYPE, ditulis `String!`. Kotlin",
                    "tidak tahu apakah ia bisa null, jadi ia MENGIZINKANMU",
                    "memakainya tanpa pemeriksaan — dan di situlah NPE masih",
                    "mungkin terjadi. Kalau sebuah nilai datang dari Java,",
                    "beri tipe eksplisit `String?` dan periksa sendiri.",
                ]
            },
        ],
    },
    {
        "title": "4. Fungsi",
        "sections": [
            {
                "body": [
                    "  fun tambah(a: Int, b: Int): Int {",
                    "      return a + b",
                    "  }",
                    "",
                    "  fun tambah(a: Int, b: Int): Int = a + b      bentuk ekspresi",
                    "  fun tambah(a: Int, b: Int) = a + b           tipe disimpulkan",
                    "",
                    "Tipe parameter WAJIB ditulis. Tipe kembalian boleh",
                    "disimpulkan HANYA pada bentuk ekspresi (dengan tanda",
                    "sama dengan).",
                    "",
                    "Fungsi tanpa nilai kembalian bertipe `Unit`, dan itu",
                    "boleh dihilangkan:",
                    "  fun cetak(x: Int): Unit { println(x) }",
                    "  fun cetak(x: Int) { println(x) }              sama",
                    "",
                    "PARAMETER BAWAAN — menggantikan overload:",
                    "",
                    "  fun garis(isi: String, lebar: Int = 30, pengisi: Char = '-')",
                    "",
                    "  garis(\"judul\")",
                    "  garis(\"judul\", 40)",
                    "  garis(\"judul\", pengisi = '=')      lewati yang tengah",
                    "",
                    "ARGUMEN BERNAMA membuat pemanggilan menjelaskan dirinya:",
                    "  gambar(tebal = true, miring = false)",
                    "",
                    "Ini bukan kosmetik. `gambar(true, false)` tidak memberi",
                    "tahu apa pun, dan menukarnya tidak menghasilkan error",
                    "apa pun.",
                    "",
                    "vararg — jumlah argumen bebas:",
                    "  fun total(vararg angka: Int) = angka.sum()",
                    "  total(1, 2, 3)",
                    "  total(*arrayOf(1, 2, 3))      tanda bintang membongkar",
                    "",
                    "EXTENSION FUNCTION — menambah method ke class yang BUKAN",
                    "milikmu:",
                    "",
                    "  fun String.rapikan(): String = trim().lowercase()",
                    "  \"  HALO  \".rapikan()        -> \"halo\"",
                    "",
                    "  fun Int.kuadrat() = this * this",
                    "  5.kuadrat()                 -> 25",
                    "",
                    "Ini salah satu fitur Kotlin yang paling banyak dipakai.",
                    "Di baliknya ia cuma fungsi statis biasa yang menerima",
                    "penerimanya sebagai parameter pertama — jadi ia TIDAK",
                    "benar-benar mengubah class aslinya, dan tidak bisa",
                    "mengakses anggota privatnya.",
                    "",
                    "Akibat penting: extension function TIDAK polimorfik.",
                    "Yang dipanggil ditentukan oleh tipe yang TERTULIS, bukan",
                    "objek yang sebenarnya.",
                    "",
                    "Fungsi bisa bersarang, dan fungsi lokal berguna untuk",
                    "memecah fungsi panjang tanpa mengotori level berkas.",
                ]
            },
            {
                "heading": "Semua bentuk fungsi",
                "code": """// Bentuk ekspresi
fun luasPersegi(sisi: Double) = sisi * sisi

// Parameter bawaan dan argumen bernama
fun garis(isi: String, lebar: Int = 30, pengisi: Char = '-'): String {
    val sisa = (lebar - isi.length).coerceAtLeast(0)
    val kiri = sisa / 2
    return pengisi.toString().repeat(kiri) + isi +
        pengisi.toString().repeat(sisa - kiri)
}

// vararg
fun rataRata(vararg angka: Int): Double =
    if (angka.isEmpty()) 0.0 else angka.sum().toDouble() / angka.size

// Extension function
fun String.rapikan(): String = trim().lowercase()
fun Int.kuadrat(): Int = this * this
fun List<Int>.ringkas(): String = "n=$size min=${min()} max=${max()}"

// Fungsi lokal: memecah tanpa mengotori level berkas
fun analisis(data: List<Int>): String {
    fun genap(x: Int) = x % 2 == 0
    val (a, b) = data.partition(::genap)
    return "genap=${a.size} ganjil=${b.size}"
}

fun main() {
    println("luas      : ${luasPersegi(2.5)}")

    println(garis(" REKAP "))
    println(garis(" KECIL ", 20))
    println(garis(" TEBAL ", pengisi = '='))
    println(garis(lebar = 24, isi = " BERNAMA ", pengisi = '*'))

    println("rata-rata : ${rataRata(80, 90, 100)}")
    println("kosong    : ${rataRata()}")
    val nilai = intArrayOf(70, 80, 90)
    println("dibongkar : ${rataRata(*nilai)}")

    println("---")
    println("rapikan   : '${"  HALO Dunia  ".rapikan()}'")
    println("kuadrat   : ${7.kuadrat()}")
    println("ringkas   : ${listOf(3, 9, 1, 7).ringkas()}")
    println("analisis  : ${analisis(listOf(1, 2, 3, 4, 5, 6, 7))}")
}"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  luas      : 6.25",
                    "  ----------- REKAP ------------",
                    "  ------ KECIL -------",
                    "  =========== TEBAL ============",
                    "  ******* BERNAMA ********",
                    "  rata-rata : 90.0",
                    "  kosong    : 0.0",
                    "  dibongkar : 80.0",
                    "  ---",
                    "  rapikan   : 'halo dunia'",
                    "  kuadrat   : 49",
                    "  ringkas   : n=4 min=1 max=9",
                    "  analisis  : genap=3 ganjil=4",
                    "",
                    "Beberapa hal yang layak diperhatikan:",
                    "",
                    "  `coerceAtLeast(0)` memastikan angkanya tidak negatif.",
                    "  Pasangannya `coerceAtMost` dan `coerceIn(a, b)`.",
                    "  Ketiganya jauh lebih terbaca daripada `maxOf` dan",
                    "  `minOf` yang bersarang.",
                    "",
                    "  `::genap` adalah REFERENSI FUNGSI — cara mengoper",
                    "  sebuah fungsi sebagai nilai tanpa membungkusnya dalam",
                    "  lambda. Bentuk lain: `String::length`, `::println`.",
                    "",
                    "  `val (a, b) = data.partition(...)` memakai",
                    "  DESTRUCTURING: sebuah Pair dipecah jadi dua variabel",
                    "  sekaligus. Ini bekerja untuk Pair, Triple, data class,",
                    "  dan apa pun yang punya operator `component1`,",
                    "  `component2`, dan seterusnya.",
                    "",
                    "  Extension `List<Int>.ringkas()` memanggil `min()` dan",
                    "  `max()` tanpa penerima — di dalam extension function,",
                    "  anggota penerimanya langsung tersedia seperti `this`",
                    "  yang tersirat.",
                ]
            },
        ],
    },
    {
        "title": "5. Kendali Alur",
        "sections": [
            {
                "body": [
                    "if di Kotlin adalah EKSPRESI, jadi ia menghasilkan nilai:",
                    "",
                    "  val status = if (nilai >= 75) \"lulus\" else \"ulang\"",
                    "",
                    "Karena itu Kotlin TIDAK PUNYA operator ternary — tidak",
                    "diperlukan.",
                    "",
                    "WHEN menggantikan switch, dan jauh lebih kuat:",
                    "",
                    "  val grade = when {",
                    "      nilai >= 85 -> \"A\"",
                    "      nilai >= 75 -> \"B\"",
                    "      else -> \"C\"",
                    "  }",
                    "",
                    "  when (x) {",
                    "      1, 2 -> \"satu atau dua\"",
                    "      in 3..10 -> \"tiga sampai sepuluh\"",
                    "      !in 0..100 -> \"di luar rentang\"",
                    "      is String -> \"sebuah teks\"",
                    "      else -> \"lainnya\"",
                    "  }",
                    "",
                    "Bentuk pertama (tanpa subjek) adalah rantai kondisi.",
                    "Bentuk kedua mencocokkan satu nilai, dan bisa mencampur",
                    "nilai, rentang, dan TIPE dalam satu blok.",
                    "",
                    "`when` atas sebuah enum atau sealed class TIDAK butuh",
                    "`else` kalau seluruh kemungkinannya sudah ditulis — dan",
                    "compiler akan MEMAKSAMU melengkapinya. Itu sifat yang",
                    "sangat berharga: menambah varian baru langsung membuat",
                    "setiap `when` yang belum diperbarui gagal dikompilasi.",
                    "",
                    "PERULANGAN:",
                    "  for (i in 1..5)            1,2,3,4,5",
                    "  for (i in 1 until 5)       1,2,3,4",
                    "  for (i in 5 downTo 1)      5,4,3,2,1",
                    "  for (i in 1..10 step 2)    1,3,5,7,9",
                    "  for (x in daftar)",
                    "  for ((i, x) in daftar.withIndex())",
                    "  for ((k, v) in peta)",
                    "",
                    "  while (syarat) { }",
                    "  do { } while (syarat)",
                    "",
                    "LABEL untuk keluar dari perulangan bersarang:",
                    "  luar@ for (i in 1..5) {",
                    "      for (j in 1..5) {",
                    "          if (i * j > 6) break@luar",
                    "      }",
                    "  }",
                    "",
                    "Di dalam lambda, `return` biasa keluar dari FUNGSI",
                    "pembungkusnya. Untuk keluar dari lambdanya saja, pakai",
                    "label: `return@forEach`.",
                ]
            },
            {
                "heading": "when yang mencampur banyak jenis pola",
                "code": """fun jelaskan(x: Any?): String = when (x) {
    null -> "kosong"
    0 -> "nol"
    in 1..9 -> "satuan $x"
    in 10..99 -> "puluhan $x"
    is Int -> if (x < 0) "negatif $x" else "bilangan besar $x"
    is Double -> "pecahan $x"
    is String -> if (x.isEmpty()) "teks kosong" else "teks ${x.length} huruf"
    is Boolean -> if (x) "benar" else "salah"
    is List<*> -> "daftar ${x.size} elemen"
    else -> "tipe lain: ${x::class.simpleName}"
}

enum class Arah { UTARA, TIMUR, SELATAN, BARAT }

// when atas enum yang LENGKAP tidak butuh else
fun putarKanan(a: Arah): Arah = when (a) {
    Arah.UTARA -> Arah.TIMUR
    Arah.TIMUR -> Arah.SELATAN
    Arah.SELATAN -> Arah.BARAT
    Arah.BARAT -> Arah.UTARA
}

fun main() {
    val contoh = listOf(null, 0, 5, 42, 1234, -7, 3.14, "", "halo", true,
                        listOf(1, 2), 'x')
    contoh.forEach { println(jelaskan(it)) }

    println("---")
    var arah = Arah.UTARA
    repeat(5) {
        print("$arah -> ")
        arah = putarKanan(arah)
    }
    println(arah)

    println("---")
    // Rentang dan langkah
    print("1..10 step 3 : ")
    for (i in 1..10 step 3) print("$i ")
    println()
    print("5 downTo 1   : ")
    for (i in 5 downTo 1) print("$i ")
    println()

    println("---")
    // Label untuk keluar dari dua perulangan
    var ketemu = 0 to 0
    luar@ for (i in 1..20) {
        for (j in 1..20) {
            if (i * j == 143) {
                ketemu = i to j
                break@luar
            }
        }
    }
    println("143 = ${ketemu.first} x ${ketemu.second}")

    println("---")
    // return@label di dalam lambda
    listOf(1, 2, 3, 4, 5).forEach {
        if (it == 3) return@forEach      // lanjut, bukan keluar dari main
        print("$it ")
    }
    println("selesai")
}"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  kosong",
                    "  nol",
                    "  satuan 5",
                    "  puluhan 42",
                    "  bilangan besar 1234",
                    "  negatif -7",
                    "  pecahan 3.14",
                    "  teks kosong",
                    "  teks 4 huruf",
                    "  benar",
                    "  daftar 2 elemen",
                    "  tipe lain: Char",
                    "  ---",
                    "  UTARA -> TIMUR -> SELATAN -> BARAT -> UTARA -> TIMUR",
                    "  ---",
                    "  1..10 step 3 : 1 4 7 10",
                    "  5 downTo 1   : 5 4 3 2 1",
                    "  ---",
                    "  143 = 11 x 13",
                    "  ---",
                    "  1 2 4 5 selesai",
                    "",
                    "URUTAN BERARTI di `when`: `in 1..9` harus ditulis",
                    "sebelum `is Int`, kalau tidak semua bilangan tertangkap",
                    "cabang Int lebih dulu.",
                    "",
                    "`putarKanan` TIDAK punya `else`, dan itu disengaja.",
                    "Kalau nanti ada `Arah.TENGGARA` ditambahkan, fungsi itu",
                    "langsung gagal dikompilasi — compiler menunjukkan persis",
                    "tempat yang perlu diperbarui. Dengan `else`, varian baru",
                    "akan diam-diam tertangkap di situ dan bugnya muncul",
                    "entah kapan.",
                    "",
                    "`return@forEach` melanjutkan ke elemen berikutnya, bukan",
                    "keluar dari fungsi. Tanpa label, `return` di dalam lambda",
                    "keluar dari FUNGSI pembungkusnya — perilaku yang disebut",
                    "non-local return, dan sumber kebingungan yang cukup",
                    "sering.",
                    "",
                    "`0 to 0` membuat sebuah `Pair`. Fungsi infix `to` itu",
                    "sama yang dipakai untuk membuat isi Map:",
                    "`mapOf(\"a\" to 1, \"b\" to 2)`.",
                ]
            },
        ],
    },
    {
        "title": "6. Koleksi",
        "sections": [
            {
                "body": [
                    "Kotlin membedakan koleksi HANYA-BACA dan YANG BISA",
                    "DIUBAH di tingkat tipe:",
                    "",
                    "  listOf(1, 2, 3)          List<Int>",
                    "  mutableListOf(1, 2, 3)   MutableList<Int>",
                    "  setOf(1, 2)              Set<Int>",
                    "  mutableSetOf(1, 2)       MutableSet<Int>",
                    "  mapOf(\"a\" to 1)          Map<String, Int>",
                    "  mutableMapOf(\"a\" to 1)   MutableMap<String, Int>",
                    "  arrayOf(1, 2, 3)         Array<Int>",
                    "  emptyList<Int>()",
                    "",
                    "Aturan praktisnya: kembalikan `List`, terima `List`,",
                    "pakai `MutableList` hanya di dalam fungsi tempat kamu",
                    "sedang membangunnya.",
                    "",
                    "Akses:",
                    "  daftar[0]            melempar kalau di luar batas",
                    "  daftar.getOrNull(0)  null kalau di luar batas",
                    "  daftar.getOrElse(0) { -1 }",
                    "  daftar.first() / last()        melempar kalau kosong",
                    "  daftar.firstOrNull() / lastOrNull()",
                    "  daftar.size / isEmpty() / isNotEmpty()",
                    "",
                    "Map:",
                    "  peta[\"a\"]                     null kalau tidak ada",
                    "  peta.getValue(\"a\")            melempar kalau tidak ada",
                    "  peta.getOrDefault(\"a\", 0)",
                    "  peta.getOrPut(\"a\") { 0 }      isi kalau belum ada",
                    "  peta.keys / values / entries",
                    "",
                    "OPERASI yang paling sering dipakai — semuanya",
                    "menghasilkan koleksi BARU, tidak mengubah yang asli:",
                    "",
                    "  map filter filterNot filterNotNull mapNotNull",
                    "  flatMap associate associateBy associateWith",
                    "  groupBy partition chunked windowed zip",
                    "  sorted sortedBy sortedByDescending reversed",
                    "  distinct take drop takeWhile dropWhile",
                    "  sum sumOf count max min maxBy maxOf minOf average",
                    "  any all none find first single",
                    "  fold reduce runningFold",
                    "  joinToString forEach onEach",
                    "",
                    "Yang mengubah di tempat punya nama berbeda: `sort()`",
                    "versus `sorted()`, `reverse()` versus `reversed()`,",
                    "`shuffle()` versus `shuffled()`. Yang berakhiran -ed",
                    "atau -d mengembalikan salinan.",
                    "",
                    "SEQUENCE untuk data besar: `.asSequence()` membuat",
                    "rantainya MALAS, sehingga tidak ada koleksi perantara",
                    "yang dibuat di tiap langkah.",
                ]
            },
            {
                "heading": "Mengolah koleksi",
                "code": """data class Murid(val nama: String, val kelas: String, val nilai: Int)

fun main() {
    val nilai = listOf(78, 92, 65, 88, 71, 95, 59, 83)

    println("Data      : ${nilai.joinToString(", ")}")
    println("Terurut   : ${nilai.sorted().joinToString(", ")}")
    println("Jumlah    : ${nilai.size}")
    println("Total     : ${nilai.sum()}")
    println("Rata-rata : ${"%.2f".format(nilai.average())}")
    println("Tertinggi : ${nilai.max()}")
    println("Terendah  : ${nilai.min()}")

    val rata = nilai.average()
    println("Di atas rata-rata: ${nilai.filter { it > rata }.joinToString(", ")}")

    println("---")
    val data = listOf(
        Murid("Andi", "A", 88), Murid("Budi", "B", 72),
        Murid("Cici", "A", 95), Murid("Dedi", "B", 64),
        Murid("Euis", "A", 79), Murid("Fajar", "B", 91),
    )

    data.filter { it.nilai >= 75 }
        .sortedByDescending { it.nilai }
        .forEach { println("  ${it.nama.padEnd(6)}${it.kelas} ${it.nilai}") }

    println("---")
    println("lulus     : ${data.count { it.nilai >= 75 }}")
    println("tertinggi : ${data.maxBy { it.nilai }.nama}")
    println("ada <65?  : ${data.any { it.nilai < 65 }}")
    println("semua >60?: ${data.all { it.nilai > 60 }}")

    println("---")
    // groupBy menghasilkan Map kunci -> List
    data.groupBy { it.kelas }
        .toSortedMap()
        .forEach { (kelas, anggota) ->
            val r = anggota.map { it.nilai }.average()
            println("Kelas $kelas: ${anggota.size} murid, rata-rata ${"%.1f".format(r)}")
        }

    println("---")
    // partition memecah jadi dua
    val (lulus, ulang) = data.partition { it.nilai >= 75 }
    println("lulus : ${lulus.joinToString(", ") { it.nama }}")
    println("ulang : ${ulang.joinToString(", ") { it.nama }}")

    println("---")
    // Frekuensi kata dengan groupingBy
    val kata = "kucing makan ikan kucing tidur ikan kucing".split(" ")
    kata.groupingBy { it }.eachCount()
        .entries.sortedWith(compareByDescending<Map.Entry<String, Int>> { it.value }
            .thenBy { it.key })
        .forEach { (k, n) -> println("${k.padEnd(7)}: $n") }
}"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  Data      : 78, 92, 65, 88, 71, 95, 59, 83",
                    "  Terurut   : 59, 65, 71, 78, 83, 88, 92, 95",
                    "  Jumlah    : 8",
                    "  Total     : 631",
                    "  Rata-rata : 78.88",
                    "  Tertinggi : 95",
                    "  Terendah  : 59",
                    "  Di atas rata-rata: 92, 88, 95, 83",
                    "  ---",
                    "    Cici  A 95",
                    "    Fajar B 91",
                    "    Andi  A 88",
                    "    Euis  A 79",
                    "  ---",
                    "  lulus     : 4",
                    "  tertinggi : Cici",
                    "  ada <65?  : true",
                    "  semua >60?: true",
                    "  ---",
                    "  Kelas A: 3 murid, rata-rata 87.3",
                    "  Kelas B: 3 murid, rata-rata 75.7",
                    "  ---",
                    "  lulus : Andi, Cici, Euis, Fajar",
                    "  ulang : Budi, Dedi",
                    "  ---",
                    "  kucing : 3",
                    "  ikan   : 2",
                    "  makan  : 1",
                    "  tidur  : 1",
                    "",
                    "`groupingBy { it }.eachCount()` adalah cara paling",
                    "ringkas menghitung frekuensi di Kotlin. Bedanya dari",
                    "`groupBy`: ia tidak membuat List perantara untuk tiap",
                    "kelompok, cuma menghitung.",
                    "",
                    "`compareByDescending { ... }.thenBy { ... }` menyusun",
                    "pembanding dua tingkat. Bentuk ini muncul di mana-mana",
                    "saat urutan harus pasti — dan urutan yang pasti itulah",
                    "yang membuat keluaran bisa diuji.",
                    "",
                    "`it` adalah nama bawaan untuk parameter tunggal sebuah",
                    "lambda. Untuk lambda bersarang, beri nama sendiri supaya",
                    "tidak membingungkan: `{ murid -> ... }`.",
                ]
            },
        ],
    },
    {
        "title": "7. Class, Properti & Constructor",
        "sections": [
            {
                "body": [
                    "  class Murid(val nama: String, var nilai: Int)",
                    "",
                    "Satu baris itu menghasilkan class dengan dua properti,",
                    "constructor, getter untuk keduanya, dan setter untuk",
                    "`nilai`. Di Java, padanannya sekitar 25 baris.",
                    "",
                    "PRIMARY CONSTRUCTOR ditulis di belakang nama class.",
                    "Parameter ber-`val` atau `var` otomatis jadi PROPERTI;",
                    "yang tanpa keduanya cuma parameter biasa.",
                    "",
                    "  class Murid(val nama: String, nilaiAwal: Int) {",
                    "      var nilai = nilaiAwal        // nilaiAwal cuma parameter",
                    "  }",
                    "",
                    "Blok `init` berjalan saat objek dibuat:",
                    "  init {",
                    "      require(nilai in 0..100) { \"nilai di luar 0..100\" }",
                    "  }",
                    "",
                    "SECONDARY CONSTRUCTOR untuk bentuk pembuatan lain:",
                    "  constructor(nama: String) : this(nama, 0)",
                    "",
                    "Dalam praktik ia jarang dipakai — parameter bawaan",
                    "biasanya lebih baik.",
                    "",
                    "PROPERTI dengan getter dan setter sendiri:",
                    "",
                    "  var nilai: Int = 0",
                    "      set(baru) {",
                    "          require(baru in 0..100)",
                    "          field = baru          // `field` = backing field",
                    "      }",
                    "",
                    "  val grade: String                 // properti TERHITUNG",
                    "      get() = when { nilai >= 85 -> \"A\"; else -> \"B\" }",
                    "",
                    "Kata `field` hanya boleh dipakai di dalam accessor, dan",
                    "ia merujuk penyimpanan sesungguhnya. Menulis `nilai =",
                    "baru` di dalam setter akan memanggil setternya sendiri",
                    "— rekursi tak berujung.",
                    "",
                    "VISIBILITAS:",
                    "  public     bawaan",
                    "  internal   terlihat di seluruh MODUL yang sama",
                    "  protected  class ini dan turunannya",
                    "  private    berkas atau class ini saja",
                    "",
                    "`internal` tidak ada di Java, dan berguna untuk API yang",
                    "publik di dalam pustakamu tapi tidak untuk pemakainya.",
                    "",
                    "LATEINIT untuk properti yang diisi belakangan:",
                    "  lateinit var db: Database",
                    "",
                    "Ia menghindari tipe nullable untuk sesuatu yang PASTI",
                    "terisi sebelum dipakai. Mengaksesnya sebelum terisi",
                    "melempar UninitializedPropertyAccessException — pesan",
                    "yang jauh lebih jelas daripada NPE.",
                ]
            },
            {
                "heading": "Class lengkap",
                "code": """class Rekening(val pemilik: String, saldoAwal: Long = 0) {

    companion object {
        private var urutan = 0
        fun buatBanyak(vararg nama: String) = nama.map { Rekening(it) }
    }

    val nomor: String

    var saldo: Long = saldoAwal
        private set          // boleh dibaca siapa pun, diubah hanya dari dalam

    val kosong: Boolean
        get() = saldo == 0L

    init {
        require(pemilik.isNotBlank()) { "pemilik wajib diisi" }
        urutan++
        nomor = "AC%04d".format(urutan)
    }

    fun setor(jumlah: Long): Rekening {
        require(jumlah > 0) { "jumlah harus positif" }
        saldo += jumlah
        return this                  // bisa dirantai
    }

    fun tarik(jumlah: Long): Boolean {
        if (jumlah <= 0 || jumlah > saldo) return false
        saldo -= jumlah
        return true
    }

    override fun toString() =
        "$nomor ${pemilik.padEnd(8)}${saldo.toString().padStart(12)}"
}

fun main() {
    val a = Rekening("Andi", 500_000)
    val b = Rekening("Budi")

    a.setor(250_000)
    println("tarik 900rb: ${a.tarik(900_000)}")
    println("tarik 300rb: ${a.tarik(300_000)}")
    b.setor(100_000)

    println(a)
    println(b)

    println("---")
    println("b kosong? ${b.kosong}")
    println("saldo a  : ${a.saldo}")
    // a.saldo = 1                 <- tidak bisa dikompilasi: setter private

    println("---")
    Rekening.buatBanyak("Cici", "Dedi").forEach { println(it) }

    try {
        Rekening("   ")
    } catch (e: IllegalArgumentException) {
        println("Ditolak: ${e.message}")
    }
}"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  tarik 900rb: false",
                    "  tarik 300rb: true",
                    "  AC0001 Andi          450000",
                    "  AC0002 Budi          100000",
                    "  ---",
                    "  b kosong? false",
                    "  saldo a  : 450000",
                    "  ---",
                    "  AC0003 Cici               0",
                    "  AC0004 Dedi               0",
                    "  Ditolak: pemilik wajib diisi",
                    "",
                    "Empat hal yang layak ditiru:",
                    "",
                    "  1. `var saldo: Long = saldoAwal` dengan `private set`.",
                    "     Dunia luar boleh MEMBACA saldo, tapi hanya class ini",
                    "     yang boleh mengubahnya, dan hanya lewat setor/tarik",
                    "     yang sudah memvalidasi. Ini satu baris; di Java ia",
                    "     butuh field privat plus getter.",
                    "",
                    "  2. `require(...) { \"pesan\" }` melempar",
                    "     IllegalArgumentException dengan pesan yang hanya",
                    "     dihitung KALAU syaratnya gagal. Saudaranya `check`",
                    "     (IllegalStateException) dan `error(\"...\")`.",
                    "",
                    "  3. `companion object` adalah tempat anggota statis di",
                    "     Kotlin. Kotlin tidak punya kata kunci `static`;",
                    "     yang ada objek pendamping yang menempel pada class.",
                    "",
                    "  4. `setor` mengembalikan `this`, sehingga bisa",
                    "     dirantai. Pola ini lazim untuk builder.",
                    "",
                    "Perhatikan `nomor` dideklarasikan `val` TANPA nilai,",
                    "lalu diisi di dalam `init`. Compiler memeriksa bahwa",
                    "setiap jalur pasti mengisinya tepat sekali — kalau ada",
                    "cabang yang lupa, kodenya tidak akan dikompilasi.",
                ]
            },
        ],
    },
    {
        "title": "8. Data Class, Object & Sealed",
        "sections": [
            {
                "body": [
                    "DATA CLASS — wadah data dalam satu baris:",
                    "",
                    "  data class Produk(val nama: String, val harga: Long)",
                    "",
                    "Compiler membuatkan:",
                    "  equals() dan hashCode() berbasis NILAI",
                    "  toString() yang enak dibaca",
                    "  copy() untuk menyalin sambil mengubah sebagian",
                    "  componentN() sehingga bisa di-destructure",
                    "",
                    "  val a = Produk(\"Kopi\", 25_000)",
                    "  val b = a.copy(harga = 27_000)",
                    "  val (nama, harga) = a",
                    "",
                    "Yang dipakai untuk equals dan toString HANYA properti di",
                    "PRIMARY constructor. Properti yang dideklarasikan di",
                    "badan class tidak ikut — jebakan yang perlu diingat.",
                    "",
                    "OBJECT — singleton, satu-satunya instance:",
                    "",
                    "  object Konfigurasi {",
                    "      val versi = \"1.0\"",
                    "      fun muat() { ... }",
                    "  }",
                    "  Konfigurasi.versi",
                    "",
                    "Ia dibuat sekali, malas, dan aman dari balapan thread —",
                    "tanpa satu pun kode penguncian yang harus kamu tulis.",
                    "",
                    "COMPANION OBJECT adalah object yang menempel pada sebuah",
                    "class, dan itulah pengganti `static`:",
                    "",
                    "  class Murid private constructor(val nama: String) {",
                    "      companion object {",
                    "          fun buat(nama: String) = Murid(nama.trim())",
                    "      }",
                    "  }",
                    "",
                    "SEALED CLASS — hierarki TERTUTUP:",
                    "",
                    "  sealed class Hasil",
                    "  data class Sukses(val data: String) : Hasil()",
                    "  data class Gagal(val pesan: String) : Hasil()",
                    "  object Memuat : Hasil()",
                    "",
                    "Seluruh turunannya harus berada di modul yang sama, jadi",
                    "compiler TAHU daftarnya lengkap. Akibatnya `when` atas",
                    "sealed class tidak butuh `else`, dan menambah turunan",
                    "baru langsung membuat setiap `when` yang belum diperbarui",
                    "gagal dikompilasi.",
                    "",
                    "Ini padanan enum berdata di Rust, dan ia cara paling",
                    "bersih menyatakan 'hasilnya salah satu dari ini saja'.",
                    "",
                    "ENUM CLASS untuk daftar tetap tanpa data berbeda:",
                    "  enum class Status(val label: String) {",
                    "      DRAF(\"Konsep\"), TERBIT(\"Sudah terbit\");",
                    "      fun bisaDisunting() = this == DRAF",
                    "  }",
                ]
            },
            {
                "heading": "Data class, sealed class, dan object",
                "code": """data class Produk(val nama: String, val kategori: String, val harga: Long) {
    val mahal: Boolean get() = harga > 100_000
}

sealed class Hasil<out T> {
    data class Sukses<T>(val data: T) : Hasil<T>()
    data class Gagal(val pesan: String) : Hasil<Nothing>()
    data object Memuat : Hasil<Nothing>()
}

object Katalog {
    private val isi = mutableListOf<Produk>()

    fun tambah(p: Produk): Hasil<Produk> {
        if (isi.any { it.nama == p.nama }) {
            return Hasil.Gagal("produk ${p.nama} sudah ada")
        }
        isi.add(p)
        return Hasil.Sukses(p)
    }

    fun cari(nama: String): Hasil<Produk> =
        isi.find { it.nama == nama }
            ?.let { Hasil.Sukses(it) }
            ?: Hasil.Gagal("produk $nama tidak ditemukan")

    fun semua(): List<Produk> = isi.sortedBy { it.nama }
}

// when atas sealed class: TANPA else, dan compiler memeriksa kelengkapannya
fun jelaskan(h: Hasil<Produk>): String = when (h) {
    is Hasil.Sukses -> "berhasil: ${h.data.nama} (${h.data.harga})"
    is Hasil.Gagal -> "gagal: ${h.pesan}"
    Hasil.Memuat -> "sedang memuat"
}

fun main() {
    val kopi = Produk("Kopi", "Minuman", 25_000)

    println(jelaskan(Katalog.tambah(kopi)))
    println(jelaskan(Katalog.tambah(Produk("Teh", "Minuman", 15_000))))
    println(jelaskan(Katalog.tambah(kopi)))
    println(jelaskan(Katalog.cari("Teh")))
    println(jelaskan(Katalog.cari("Jus")))
    println(jelaskan(Hasil.Memuat))

    println("---")
    // Data class: copy, destructuring, kesetaraan berbasis nilai
    val naik = kopi.copy(harga = 120_000)
    println("asli  : $kopi")
    println("naik  : $naik")
    println("mahal?: ${kopi.mahal} / ${naik.mahal}")

    val (nama, kategori, harga) = kopi
    println("pecah : $nama / $kategori / $harga")

    println("sama nilainya? ${kopi == Produk("Kopi", "Minuman", 25_000)}")
    println("sama objeknya? ${kopi === Produk("Kopi", "Minuman", 25_000)}")

    println("---")
    Katalog.semua().forEach { println("  ${it.nama.padEnd(6)}${it.harga}") }
}"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  berhasil: Kopi (25000)",
                    "  berhasil: Teh (15000)",
                    "  gagal: produk Kopi sudah ada",
                    "  berhasil: Teh (15000)",
                    "  gagal: produk Jus tidak ditemukan",
                    "  sedang memuat",
                    "  ---",
                    "  asli  : Produk(nama=Kopi, kategori=Minuman, harga=25000)",
                    "  naik  : Produk(nama=Kopi, kategori=Minuman, harga=120000)",
                    "  mahal?: false / true",
                    "  pecah : Kopi / Minuman / 25000",
                    "  sama nilainya? true",
                    "  sama objeknya? false",
                    "  ---",
                    "    Kopi  25000",
                    "    Teh   15000",
                    "",
                    "Perhatikan `mahal` TIDAK muncul di toString. Itu karena",
                    "ia properti terhitung di BADAN class, bukan di primary",
                    "constructor — dan hanya yang di primary constructor yang",
                    "ikut ke equals, hashCode, toString, dan copy.",
                    "",
                    "`==` membandingkan NILAI (memanggil equals), sedangkan",
                    "`===` membandingkan apakah objeknya sama persis.",
                    "Kebalikan dari Java, tempat `==` justru membandingkan",
                    "referensi dan orang harus ingat memanggil `.equals()`.",
                    "",
                    "`Hasil<out T>` memakai `out` untuk menyatakan bahwa",
                    "`Hasil<Produk>` boleh dipakai di tempat yang menerima",
                    "`Hasil<Any>`. Itu sebabnya `Gagal` bisa bertipe",
                    "`Hasil<Nothing>` dan tetap cocok di mana pun.",
                    "",
                    "`Nothing` adalah tipe yang TIDAK PUNYA satu pun nilai.",
                    "Ia turunan dari semua tipe, sehingga berguna persis di",
                    "situasi seperti ini — dan juga sebagai tipe kembalian",
                    "fungsi yang tidak pernah kembali normal.",
                    "",
                    "`data object` (Kotlin 1.9) memberi toString yang enak",
                    "dibaca untuk singleton di dalam sealed hierarchy.",
                ]
            },
        ],
    },
    {
        "title": "9. Pewarisan & Interface",
        "sections": [
            {
                "body": [
                    "Di Kotlin, class TERTUTUP untuk pewarisan secara bawaan.",
                    "Untuk membukanya, tulis `open`:",
                    "",
                    "  open class Hewan(val nama: String) {",
                    "      open fun suara(): String = \"...\"",
                    "  }",
                    "",
                    "  class Kucing(nama: String) : Hewan(nama) {",
                    "      override fun suara() = \"Meong\"",
                    "  }",
                    "",
                    "Ini kebalikan dari Java, dan alasannya dinyatakan",
                    "eksplisit oleh perancangnya: sebuah class yang bisa",
                    "diturunkan adalah JANJI PUBLIK yang harus dipikirkan,",
                    "bukan kecelakaan. Kalau kamu tidak merancang sebuah",
                    "class untuk diturunkan, turunannya bisa merusak asumsi",
                    "di dalamnya tanpa kamu tahu.",
                    "",
                    "`override` WAJIB ditulis. Tanpa itu, kodenya tidak akan",
                    "dikompilasi — sehingga tidak mungkin ada method yang",
                    "tanpa sengaja menimpa method induk.",
                    "",
                    "Constructor induk dipanggil di daftar supertype:",
                    "  class Kucing(nama: String) : Hewan(nama)",
                    "",
                    "ABSTRACT: tidak bisa di-instance, boleh punya anggota",
                    "tanpa badan. `abstract` sudah otomatis `open`.",
                    "",
                    "INTERFACE bisa punya implementasi bawaan DAN properti",
                    "abstrak, tapi TIDAK bisa menyimpan keadaan:",
                    "",
                    "  interface BisaDiringkas {",
                    "      val nama: String              // abstrak",
                    "      fun luas(): Double            // abstrak",
                    "      fun ringkas(): String =       // ada badannya",
                    "          \"%-16s%8.2f\".format(nama, luas())",
                    "  }",
                    "",
                    "Satu class boleh mengimplementasi BANYAK interface tapi",
                    "hanya punya SATU induk. Kalau dua interface punya method",
                    "bernama sama dengan badan, kamu WAJIB memilih eksplisit:",
                    "",
                    "  override fun f() = super<A>.f()",
                    "",
                    "DELEGASI dengan `by` — menggantikan pewarisan:",
                    "",
                    "  class Pencatat(dasar: List<Int>) : List<Int> by dasar",
                    "",
                    "Satu kata `by` membuat seluruh method List diteruskan ke",
                    "`dasar`, dan kamu tinggal menimpa yang perlu saja. Di",
                    "Java, pola delegasi yang sama butuh puluhan method",
                    "penerus yang ditulis tangan.",
                ]
            },
            {
                "heading": "Interface, abstract, dan delegasi",
                "code": """interface Bangun {
    val nama: String
    fun luas(): Double

    // Implementasi bawaan: turunan boleh memakainya apa adanya
    fun ringkas(): String = "%-16s%8.2f".format(nama, luas())
}

interface Berwarna {
    var warna: String
    fun deskripsi() = "$warna"
}

abstract class BangunDasar(override val nama: String) : Bangun, Berwarna {
    override var warna: String = "hitam"
}

class Persegi(private val sisi: Double) : BangunDasar("Persegi") {
    override fun luas() = sisi * sisi
}

class Lingkaran(private val jari: Double) : BangunDasar("Lingkaran") {
    companion object { const val PI = 3.14159 }

    override fun luas() = PI * jari * jari
    override fun ringkas() = super.ringkas() + "  (r=$jari)"
}

class PersegiPanjang(private val p: Double, private val l: Double) :
    BangunDasar("PersegiPanjang") {
    override fun luas() = p * l
}

// Delegasi: seluruh method List diteruskan ke `isi`, satu ditimpa
class Galeri(private val isi: List<BangunDasar>) : List<BangunDasar> by isi {
    fun totalLuas() = isi.sumOf { it.luas() }
    override fun toString() = isi.joinToString(", ") { it.nama }
}

fun main() {
    val galeri = Galeri(listOf(Persegi(4.0), Lingkaran(3.0), PersegiPanjang(6.0, 3.0)))

    galeri.forEach { println(it.ringkas()) }
    println("%-16s%8.2f".format("TOTAL", galeri.totalLuas()))

    println("---")
    // Method List tersedia tanpa satu pun ditulis di Galeri
    println("jumlah    : ${galeri.size}")
    println("pertama   : ${galeri.first().nama}")
    println("terluas   : ${galeri.maxBy { it.luas() }.nama}")
    println("isi       : $galeri")

    println("---")
    galeri[0].warna = "merah"
    println("warna [0] : ${galeri[0].deskripsi()}")
    println("warna [1] : ${galeri[1].deskripsi()}")

    println("---")
    // is + smart cast
    for (b in galeri) {
        val tambahan = if (b is Lingkaran) " (lingkaran)" else ""
        println("${b.nama}$tambahan")
    }
}"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  Persegi            16.00",
                    "  Lingkaran          28.27  (r=3.0)",
                    "  PersegiPanjang     18.00",
                    "  TOTAL              62.27",
                    "  ---",
                    "  jumlah    : 3",
                    "  pertama   : Persegi",
                    "  terluas   : Lingkaran",
                    "  isi       : Persegi, Lingkaran, PersegiPanjang",
                    "  ---",
                    "  warna [0] : merah",
                    "  warna [1] : hitam",
                    "  ---",
                    "  Persegi",
                    "  Lingkaran (lingkaran)",
                    "  PersegiPanjang",
                    "",
                    "Class `Galeri` adalah contoh delegasi yang tidak bisa",
                    "ditiru sesingkat ini di Java. Satu frasa `: List<Bangun>",
                    "by isi` membuat SELURUH method List — size, get, iterator,",
                    "contains, indexOf, subList, dan belasan lainnya —",
                    "diteruskan ke `isi`. Yang ditulis tangan cuma `totalLuas`",
                    "dan `toString`.",
                    "",
                    "Kenapa ini lebih baik daripada `class Galeri : ArrayList`:",
                    "dengan pewarisan, Galeri mewarisi juga method yang MENGUBAH",
                    "(add, remove, clear) yang mungkin tidak kamu inginkan.",
                    "Dengan delegasi, kamu memilih antarmuka yang dipaparkan.",
                    "",
                    "Perhatikan tipe parameternya `List<BangunDasar>`, BUKAN",
                    "`List<Bangun>`. Yang menentukan anggota apa yang bisa",
                    "dipanggil pada `galeri[0]` adalah tipe yang TERTULIS,",
                    "bukan objek sesungguhnya. Dengan `List<Bangun>`, properti",
                    "`warna` dari interface Berwarna tidak terlihat sama",
                    "sekali -- dan pesannya bukan 'tidak punya warna'",
                    "melainkan 'unresolved reference', yang terdengar seperti",
                    "salah ketik.",
                    "",
                    "`b is Lingkaran` melakukan SMART CAST: di dalam cabang",
                    "itu, `b` otomatis bertipe Lingkaran tanpa cast manual.",
                    "Di Java, pola yang sama butuh `instanceof` lalu cast",
                    "eksplisit — dua kali menyebut tipenya.",
                    "",
                    "`override var warna` di dalam abstract class MENGISI",
                    "properti abstrak dari interface. Interface boleh",
                    "mendeklarasikan properti, tapi tidak boleh menyimpan",
                    "nilainya — yang menyimpan harus class.",
                ]
            },
        ],
    },
    {
        "title": "10. Lambda & Higher-Order Function",
        "sections": [
            {
                "body": [
                    "LAMBDA ditulis di dalam kurung kurawal:",
                    "",
                    "  val tambah: (Int, Int) -> Int = { a, b -> a + b }",
                    "  val kuadrat = { x: Int -> x * x }",
                    "  val cetak: (String) -> Unit = { println(it) }",
                    "",
                    "Kalau parameternya cuma SATU, namanya boleh dihilangkan",
                    "dan diganti `it`.",
                    "",
                    "TIPE FUNGSI ditulis `(A, B) -> C`. Ia tipe kelas satu,",
                    "jadi boleh jadi parameter, nilai kembalian, dan isi",
                    "koleksi.",
                    "",
                    "HIGHER-ORDER FUNCTION menerima atau mengembalikan fungsi:",
                    "",
                    "  fun saring(data: List<Int>, syarat: (Int) -> Boolean) =",
                    "      data.filter(syarat)",
                    "",
                    "ATURAN LAMBDA TERAKHIR: kalau parameter terakhir sebuah",
                    "fungsi bertipe fungsi, lambdanya boleh ditulis DI LUAR",
                    "tanda kurung:",
                    "",
                    "  saring(data) { it > 5 }          alih-alih",
                    "  saring(data, { it > 5 })",
                    "",
                    "Aturan inilah yang membuat `repeat`, `forEach`, `with`,",
                    "`apply`, dan seluruh DSL Kotlin terlihat seperti sintaks",
                    "bawaan bahasa — padahal semuanya fungsi biasa.",
                    "",
                    "REFERENSI FUNGSI mengoper fungsi yang sudah ada:",
                    "  data.filter(::genap)",
                    "  data.map(String::length)",
                    "  data.forEach(::println)",
                    "",
                    "SCOPE FUNCTION — lima fungsi yang sangat khas Kotlin:",
                    "",
                    "  let     x.let { it }      -> hasil lambda",
                    "  run     x.run { this }    -> hasil lambda",
                    "  with    with(x) { this }  -> hasil lambda",
                    "  apply   x.apply { this }  -> X sendiri",
                    "  also    x.also { it }     -> X sendiri",
                    "",
                    "Dua kolom itu yang membedakan: apa NAMA penerimanya di",
                    "dalam blok, dan APA yang dikembalikan.",
                    "",
                    "Kapan memakai yang mana, versi praktisnya:",
                    "  let    jalankan blok kalau bukan null, atau ubah bentuk",
                    "  apply  setel banyak properti lalu kembalikan objeknya",
                    "  also   selipkan efek samping (log) tanpa mengubah rantai",
                    "  run    hitung sesuatu dari sebuah objek",
                    "  with   panggil banyak method pada satu objek",
                    "",
                    "Jangan memaksakan semuanya. Kalau sebuah `let` membuat",
                    "kodenya lebih sulit dibaca, variabel biasa lebih baik.",
                ]
            },
            {
                "heading": "Lambda, higher-order, dan scope function",
                "code": """class Setelan {
    var tema: String = "terang"
    var ukuran: Int = 14
    var gerak: Boolean = true
    override fun toString() = "Setelan(tema=$tema, ukuran=$ukuran, gerak=$gerak)"
}

// Higher-order: menerima fungsi
fun <T> saring(data: List<T>, syarat: (T) -> Boolean): List<T> {
    val hasil = mutableListOf<T>()
    for (x in data) if (syarat(x)) hasil.add(x)
    return hasil
}

// Higher-order: MENGEMBALIKAN fungsi
fun pengali(faktor: Int): (Int) -> Int = { it * faktor }

fun genap(n: Int) = n % 2 == 0

fun main() {
    val angka = (1..10).toList()

    println("genap     : ${saring(angka) { it % 2 == 0 }}")
    println("ref fungsi: ${saring(angka, ::genap)}")
    println("lebih 7   : ${saring(angka) { it > 7 }}")

    val kaliTiga = pengali(3)
    println("kali tiga : ${angka.map(kaliTiga)}")

    println("---")
    // Fungsi disimpan di dalam Map
    val operasi: Map<String, (Int, Int) -> Int> = mapOf(
        "tambah" to { a, b -> a + b },
        "kurang" to { a, b -> a - b },
        "kali" to { a, b -> a * b },
    )
    operasi.forEach { (nama, fn) ->
        println("${nama.padEnd(7)}(9, 4) = ${fn(9, 4)}")
    }

    println("---")
    // apply: setel banyak properti, kembalikan objeknya
    val s = Setelan().apply {
        tema = "gelap"
        ukuran = 18
    }
    println("apply : $s")

    // also: efek samping tanpa mengubah rantai
    val hasil = angka.filter { it > 5 }
        .also { println("also  : sesudah filter ada ${it.size} elemen") }
        .map { it * 10 }
    println("hasil : $hasil")

    // let: jalankan hanya kalau bukan null, dan ubah bentuknya
    val mungkin: String? = "kotlin"
    val panjang = mungkin?.let { it.length * 2 } ?: 0
    println("let   : $panjang")

    // run: hitung sesuatu dari sebuah objek
    val ringkas = s.run { "$tema/$ukuran" }
    println("run   : $ringkas")

    // with: panggil banyak method pada satu objek
    with(StringBuilder()) {
        append("Halo")
        append(", ")
        append("dunia")
        println("with  : $this")
    }
}"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  genap     : [2, 4, 6, 8, 10]",
                    "  ref fungsi: [2, 4, 6, 8, 10]",
                    "  lebih 7   : [8, 9, 10]",
                    "  kali tiga : [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]",
                    "  ---",
                    "  tambah (9, 4) = 13",
                    "  kurang (9, 4) = 5",
                    "  kali   (9, 4) = 36",
                    "  ---",
                    "  apply : Setelan(tema=gelap, ukuran=18, gerak=true)",
                    "  also  : sesudah filter ada 5 elemen",
                    "  hasil : [60, 70, 80, 90, 100]",
                    "  let   : 12",
                    "  run   : gelap/18",
                    "  with  : Halo, dunia",
                    "",
                    "`pengali(3)` mengembalikan FUNGSI yang mengingat nilai 3.",
                    "Itu disebut CLOSURE: lambdanya menangkap variabel dari",
                    "lingkungan tempat ia dibuat, dan variabel itu tetap hidup",
                    "selama lambdanya hidup.",
                    "",
                    "`also` layak diperhatikan: ia menyisipkan efek samping di",
                    "TENGAH rantai tanpa memutusnya. Untuk mencari tahu",
                    "kenapa sebuah rantai menghasilkan data yang salah, ini",
                    "jauh lebih enak daripada memecah rantainya jadi variabel",
                    "sementara.",
                    "",
                    "INLINE — satu hal yang membuat higher-order function di",
                    "Kotlin gratis. Fungsi yang ditandai `inline` disalin",
                    "badannya ke tempat pemanggilan saat kompilasi, sehingga",
                    "tidak ada objek lambda yang dibuat sama sekali:",
                    "",
                    "  inline fun <T> ukur(blok: () -> T): T { ... }",
                    "",
                    "Seluruh fungsi koleksi standar (filter, map, forEach)",
                    "sudah `inline`. Itu sebabnya rantai operasi di Kotlin",
                    "secepat perulangan yang ditulis tangan.",
                    "",
                    "`inline` juga yang memungkinkan `return` non-lokal:",
                    "`return` di dalam `forEach` bisa keluar dari fungsi",
                    "pembungkusnya, karena badan lambdanya memang tersalin",
                    "ke situ.",
                ]
            },
        ],
    },
    {
        "title": "11. Generic & Extension Lanjut",
        "sections": [
            {
                "body": [
                    "GENERIC membuat satu kode bekerja untuk banyak tipe:",
                    "",
                    "  class Kotak<T>(private val isi: MutableList<T> = mutableListOf())",
                    "  fun <T> pertama(daftar: List<T>): T? = daftar.firstOrNull()",
                    "",
                    "BATASAN dengan titik dua:",
                    "  fun <T : Comparable<T>> terbesar(a: T, b: T) =",
                    "      if (a > b) a else b",
                    "",
                    "Untuk lebih dari satu batasan, pakai `where`:",
                    "  fun <T> proses(x: T) where T : Comparable<T>, T : Cloneable",
                    "",
                    "VARIANSI — bagian yang paling sering membingungkan:",
                    "",
                    "  out T   PRODUSEN: hanya mengeluarkan T, tidak menerima.",
                    "          List<Kucing> boleh dipakai sebagai List<Hewan>.",
                    "  in T    KONSUMEN: hanya menerima T, tidak mengeluarkan.",
                    "          Comparator<Hewan> boleh dipakai sebagai",
                    "          Comparator<Kucing>.",
                    "",
                    "Cara mengingatnya: `out` untuk yang KELUAR, `in` untuk",
                    "yang MASUK. `List<out T>` aman diperlebar karena tidak",
                    "ada cara menyisipkan Anjing ke dalam List<Kucing> yang",
                    "sedang dipandang sebagai List<Hewan>.",
                    "",
                    "REIFIED — mengetahui tipe generic saat program jalan:",
                    "",
                    "  inline fun <reified T> saringTipe(daftar: List<Any>) =",
                    "      daftar.filterIsInstance<T>()",
                    "",
                    "Di JVM, informasi tipe generic DIHAPUS saat kompilasi",
                    "(type erasure), sehingga `T::class` biasanya mustahil.",
                    "`reified` mengatasinya dengan menyalin badan fungsinya ke",
                    "tempat pemanggilan, tempat tipenya masih diketahui. Ia",
                    "HANYA bisa dipakai bersama `inline`.",
                    "",
                    "EXTENSION PROPERTY, pasangan extension function:",
                    "  val String.hurufSaja: String",
                    "      get() = filter { it.isLetter() }",
                    "",
                    "Ia tidak menyimpan apa pun — tidak ada tempat untuk",
                    "menyimpannya di class yang bukan milikmu — jadi ia wajib",
                    "punya getter.",
                    "",
                    "EXTENSION dengan penerima nullable:",
                    "  fun String?.atauKosong(): String = this ?: \"\"",
                    "",
                    "Di dalamnya `this` boleh null, dan itu sah. Inilah cara",
                    "`isNullOrBlank()` di pustaka standar bekerja.",
                ]
            },
            {
                "heading": "Generic, variansi, dan reified",
                "code": """// Generic dengan batasan
fun <T : Comparable<T>> terbesar(daftar: List<T>): T? =
    daftar.maxOrNull()

// Kotak generic
class Kotak<T>(private val muat: Int) {
    private val isi = mutableListOf<T>()

    val jumlah: Int get() = isi.size
    val penuh: Boolean get() = isi.size >= muat

    fun masuk(x: T): Boolean {
        if (penuh) return false
        isi.add(x)
        return true
    }

    fun keluar(): T? = isi.removeFirstOrNull()

    override fun toString() = "[${isi.joinToString(", ")}] $jumlah/$muat"
}

// out: produsen. List<Kucing> boleh jadi List<Hewan>
open class Hewan(val nama: String)
class Kucing(nama: String) : Hewan(nama)

fun semuaNama(hewan: List<Hewan>) = hewan.joinToString(", ") { it.nama }

// reified: tipe generic diketahui saat program jalan
inline fun <reified T> saringTipe(daftar: List<Any>): List<T> =
    daftar.filterIsInstance<T>()

// Extension property dan extension pada tipe nullable
val String.hurufSaja: String get() = filter { it.isLetter() }
fun String?.ringkas(maks: Int = 10): String =
    when {
        this == null -> "(kosong)"
        length <= maks -> this
        else -> take(maks - 3) + "..."
    }

fun main() {
    println("terbesar Int  : ${terbesar(listOf(3, 9, 1, 7))}")
    println("terbesar teks : ${terbesar(listOf("apel", "jeruk", "mangga"))}")

    println("---")
    val angka = Kotak<Int>(3)
    for (n in listOf(10, 20, 30, 40)) println("masuk $n: ${angka.masuk(n)}")
    println(angka)
    println("keluar: ${angka.keluar()}")
    println(angka)

    println("---")
    val kucing: List<Kucing> = listOf(Kucing("Mimi"), Kucing("Momo"))
    println("variansi out: ${semuaNama(kucing)}")

    println("---")
    val campur: List<Any> = listOf(1, "dua", 3.0, "empat", 5, true)
    println("hanya Int    : ${saringTipe<Int>(campur)}")
    println("hanya String : ${saringTipe<String>(campur)}")

    println("---")
    println("hurufSaja    : '${"K0t1in 2026!".hurufSaja}'")
    println("ringkas      : ${"pemrograman".ringkas()}")
    println("ringkas null : ${null.ringkas()}")
    println("ringkas pendek: ${"halo".ringkas()}")
}"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  terbesar Int  : 9",
                    "  terbesar teks : mangga",
                    "  ---",
                    "  masuk 10: true",
                    "  masuk 20: true",
                    "  masuk 30: true",
                    "  masuk 40: false",
                    "  [10, 20, 30] 3/3",
                    "  keluar: 10",
                    "  [20, 30] 2/3",
                    "  ---",
                    "  variansi out: Mimi, Momo",
                    "  ---",
                    "  hanya Int    : [1, 5]",
                    "  hanya String : [dua, empat]",
                    "  ---",
                    "  hurufSaja    : 'Ktin'",
                    "  ringkas      : pemrogr...",
                    "  ringkas null : (kosong)",
                    "  ringkas pendek: halo",
                    "",
                    "`semuaNama(kucing)` bekerja padahal parameternya bertipe",
                    "`List<Hewan>` dan yang dioper `List<Kucing>`. Itu karena",
                    "`List<out E>` di Kotlin memang deklarasinya produsen —",
                    "ia tidak punya `add`, jadi tidak ada cara menyelipkan",
                    "Anjing ke dalamnya. Dengan `MutableList<Kucing>`, kode",
                    "itu TIDAK akan dikompilasi, dan itu benar.",
                    "",
                    "`saringTipe<Int>(campur)` bisa memeriksa tipe T saat",
                    "program jalan HANYA karena `reified` + `inline`. Tanpa",
                    "keduanya, `T::class` dan `is T` adalah error kompilasi —",
                    "JVM sudah menghapus informasi tipenya.",
                    "",
                    "`null.ringkas()` memanggil method pada NULL, dan itu sah",
                    "karena penerimanya bertipe `String?`. Di dalam fungsi",
                    "itu, `this` boleh null dan harus diperiksa. Inilah",
                    "mekanisme yang sama dengan `isNullOrBlank()` di pustaka",
                    "standar.",
                    "",
                    "Perhatikan juga `removeFirstOrNull()` dan `maxOrNull()`:",
                    "pustaka standar Kotlin konsisten menyediakan pasangan",
                    "`xxx()` yang melempar dan `xxxOrNull()` yang tidak.",
                    "Memilih di antaranya adalah keputusan desain yang kamu",
                    "ambil, bukan kelalaian yang dibiarkan.",
                ]
            },
        ],
    },
    {
        "title": "12. Exception & Penanganan Galat",
        "sections": [
            {
                "body": [
                    "  try {",
                    "      ...",
                    "  } catch (e: NumberFormatException) {",
                    "      ...",
                    "  } catch (e: Exception) {",
                    "      ...",
                    "  } finally {",
                    "      ...            SELALU dijalankan",
                    "  }",
                    "",
                    "`try` adalah EKSPRESI, jadi menghasilkan nilai:",
                    "",
                    "  val n = try { teks.toInt() } catch (e: Exception) { 0 }",
                    "",
                    "PERBEDAAN BESAR dari Java: Kotlin TIDAK PUNYA checked",
                    "exception. Tidak ada `throws` di tanda tangan fungsi, dan",
                    "tidak ada compiler yang memaksamu membungkus sesuatu",
                    "dengan try-catch.",
                    "",
                    "Alasannya dinyatakan perancangnya: di proyek besar,",
                    "checked exception hampir selalu berakhir sebagai",
                    "`catch (e: Exception) { }` kosong — yang JUSTRU lebih",
                    "buruk daripada membiarkannya naik. Yang hilang adalah",
                    "paksaan; yang tersisa tanggung jawabmu sendiri.",
                    "",
                    "Melempar:",
                    "  throw IllegalArgumentException(\"pesan\")",
                    "  require(syarat) { \"pesan\" }      -> IllegalArgumentException",
                    "  check(syarat) { \"pesan\" }        -> IllegalStateException",
                    "  error(\"pesan\")                   -> IllegalStateException",
                    "  requireNotNull(x) { \"pesan\" }",
                    "  checkNotNull(x) { \"pesan\" }",
                    "  TODO(\"belum dibuat\")             -> NotImplementedError",
                    "",
                    "`require` untuk memeriksa ARGUMEN, `check` untuk memeriksa",
                    "KEADAAN objeknya. Keduanya menghitung pesannya HANYA",
                    "kalau syaratnya gagal.",
                    "",
                    "`throw` juga ekspresi bertipe `Nothing`, sehingga bisa",
                    "dipakai di sisi kanan Elvis:",
                    "  val n = cari() ?: throw IllegalStateException(\"tidak ada\")",
                    "",
                    "RESULT — alternatif yang lebih aman untuk API:",
                    "",
                    "  val hasil: Result<Int> = runCatching { teks.toInt() }",
                    "  hasil.getOrNull()",
                    "  hasil.getOrDefault(0)",
                    "  hasil.getOrElse { -1 }",
                    "  hasil.onSuccess { }.onFailure { }",
                    "  hasil.map { it * 2 }",
                    "",
                    "`runCatching` menangkap SEMUA Throwable, jadi ia terlalu",
                    "luas untuk dipakai sembarangan. Untuk kode yang memang",
                    "cuma boleh gagal dengan cara tertentu, sealed class",
                    "bikinan sendiri (seperti `Hasil` di materi sebelumnya)",
                    "lebih tepat.",
                    "",
                    "`use` adalah padanan try-with-resources:",
                    "  File(\"data.txt\").bufferedReader().use { it.readText() }",
                    "  Berkasnya ditutup apa pun yang terjadi.",
                ]
            },
            {
                "heading": "Exception sendiri, try sebagai ekspresi, dan Result",
                "code": """class SaldoKurangException(val kurang: Long) :
    RuntimeException("saldo kurang $kurang")

class Dompet(private var saldo: Long) {
    fun saldo() = saldo

    fun bayar(jumlah: Long) {
        require(jumlah > 0) { "jumlah $jumlah tidak sah" }
        if (jumlah > saldo) throw SaldoKurangException(jumlah - saldo)
        saldo -= jumlah
    }
}

fun parseNilai(teks: String): Int {
    val n = teks.trim().toIntOrNull()
        ?: throw NumberFormatException("bukan angka: ${teks.trim()}")
    require(n in 0..100) { "di luar 0..100: $n" }
    return n
}

fun main() {
    val d = Dompet(50_000)

    for (tagihan in listOf(20_000L, -5L, 100_000L, 30_000L)) {
        try {
            d.bayar(tagihan)
            println("bayar %7d -> sisa %d".format(tagihan, d.saldo()))
        } catch (e: SaldoKurangException) {
            println("bayar %7d -> GAGAL, kurang %d".format(tagihan, e.kurang))
        } catch (e: IllegalArgumentException) {
            println("bayar %7d -> DITOLAK: %s".format(tagihan, e.message))
        }
    }

    println("---")
    // try sebagai EKSPRESI
    for (teks in listOf("88", " 92 ", "abc", "150")) {
        val pesan = try {
            "-> ${parseNilai(teks)}"
        } catch (e: NumberFormatException) {
            "-> bukan angka"
        } catch (e: IllegalArgumentException) {
            "-> ${e.message}"
        }
        println("%5s %s".format(teks, pesan))
    }

    println("---")
    // Result dengan runCatching
    listOf("42", "abc").forEach { teks ->
        val hasil = runCatching { parseNilai(teks) }
        println("$teks: sukses=${hasil.isSuccess} nilai=${hasil.getOrNull()} " +
                "bawaan=${hasil.getOrDefault(-1)}")
    }

    println("---")
    // finally selalu jalan
    fun dengan(nama: String, blok: () -> Int): Int? {
        println("buka $nama")
        return try {
            blok()
        } catch (e: RuntimeException) {
            println("galat: ${e.message}")
            null
        } finally {
            println("tutup $nama")
        }
    }

    println("hasil: ${dengan("berkas") { 6 * 7 }}")
    println("hasil: ${dengan("berkas") { error("rusak") }}")
}"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  bayar   20000 -> sisa 30000",
                    "  bayar      -5 -> DITOLAK: jumlah -5 tidak sah",
                    "  bayar  100000 -> GAGAL, kurang 70000",
                    "  bayar   30000 -> sisa 0",
                    "  ---",
                    "     88 -> 88",
                    "    92  -> 92",
                    "    abc -> bukan angka",
                    "    150 -> di luar 0..100: 150",
                    "  ---",
                    "  42: sukses=true nilai=42 bawaan=42",
                    "  abc: sukses=false nilai=null bawaan=-1",
                    "  ---",
                    "  buka berkas",
                    "  tutup berkas",
                    "  hasil: 42",
                    "  buka berkas",
                    "  galat: rusak",
                    "  tutup berkas",
                    "  hasil: null",
                    "",
                    "Perhatikan urutan catch: `SaldoKurangException` ditulis",
                    "SEBELUM `IllegalArgumentException`. Kalau dibalik, yang",
                    "umum akan menelan yang khusus — dan berbeda dari C#,",
                    "Kotlin TIDAK memperingatkanmu soal itu karena keduanya",
                    "bukan hubungan induk-turunan di sini.",
                    "",
                    "`?: throw ...` di `parseNilai` memanfaatkan bahwa `throw`",
                    "bertipe `Nothing`, yang merupakan turunan dari SEMUA",
                    "tipe. Karena itu ia cocok di sisi kanan Elvis tanpa",
                    "keberatan compiler.",
                    "",
                    "Aturan yang sama berlaku seperti di bahasa lain:",
                    "",
                    "  JANGAN `catch (e: Exception) { }` kosong. Program",
                    "  berjalan terus dalam keadaan rusak.",
                    "",
                    "  JANGAN menangkap apa yang tidak bisa kamu perbaiki.",
                    "",
                    "  JANGAN memakai exception untuk alur normal. Salah ketik",
                    "  pengguna itu normal — pakai `toIntOrNull`.",
                    "",
                    "Khusus Kotlin: hati-hati menangkap `Exception` di kode",
                    "yang memakai coroutine. `CancellationException` adalah",
                    "turunannya, dan menelannya membuat pembatalan berhenti",
                    "bekerja tanpa satu pun tanda.",
                ]
            },
        ],
    },
    {
        "title": "13. Coroutine: Asinkron Tanpa Callback",
        "sections": [
            {
                "body": [
                    "Coroutine adalah cara Kotlin menangani pekerjaan yang",
                    "MENUNGGU: memanggil API, membaca berkas, query database.",
                    "",
                    "Yang membuatnya berbeda: kode asinkron ditulis seperti",
                    "kode biasa, dari atas ke bawah, tanpa callback bersarang",
                    "dan tanpa rantai `.then()`.",
                    "",
                    "  suspend fun ambil(): String {",
                    "      delay(1000)          // tidak memblokir thread",
                    "      return \"data\"",
                    "  }",
                    "",
                    "`suspend` menandai fungsi yang BISA BERHENTI SEJENAK lalu",
                    "dilanjutkan. Fungsi suspend hanya boleh dipanggil dari",
                    "fungsi suspend lain atau dari dalam coroutine.",
                    "",
                    "MEMULAI coroutine:",
                    "  runBlocking { }      memblokir thread; untuk main & tes",
                    "  launch { }           jalankan, jangan tunggu hasilnya",
                    "  async { }            jalankan, hasilnya diambil .await()",
                    "  withContext(D) { }   pindah dispatcher, tunggu selesai",
                    "",
                    "DISPATCHER menentukan thread mana yang dipakai:",
                    "  Dispatchers.Default   perhitungan berat, sejumlah core",
                    "  Dispatchers.IO        menunggu jaringan/berkas, banyak thread",
                    "  Dispatchers.Main      UI (Android)",
                    "  Dispatchers.Unconfined  jarang dipakai",
                    "",
                    "STRUCTURED CONCURRENCY adalah gagasan intinya, dan ia",
                    "menyelesaikan masalah yang sangat nyata: coroutine SELALU",
                    "punya induk, dan induknya tidak selesai sebelum semua",
                    "anaknya selesai.",
                    "",
                    "Akibatnya:",
                    "  - Tidak ada coroutine yang bocor tanpa pemilik.",
                    "  - Membatalkan induk membatalkan seluruh anaknya.",
                    "  - Galat di anak dilaporkan ke induknya, tidak hilang.",
                    "",
                    "BERURUTAN versus BERSAMAAN — kesalahan paling mahal:",
                    "",
                    "  // BERURUTAN: 2 detik",
                    "  val a = ambilA()",
                    "  val b = ambilB()",
                    "",
                    "  // BERSAMAAN: 1 detik",
                    "  val a = async { ambilA() }",
                    "  val b = async { ambilB() }",
                    "  val hasil = a.await() + b.await()",
                    "",
                    "Coroutine BUKAN bagian dari bahasanya; ia pustaka",
                    "terpisah yang harus ditambahkan:",
                    "  implementation(\"org.jetbrains.kotlinx:kotlinx-coroutines-core\")",
                    "",
                    "Yang ADA di bahasanya cuma kata kunci `suspend` dan",
                    "mesin state yang dihasilkan compiler untuknya.",
                ]
            },
            {
                "heading": "Meniru coroutine dengan thread biasa",
                "code": """// Contoh ini memakai thread bawaan JVM, BUKAN pustaka coroutine --
// supaya bisa dijalankan tanpa dependensi apa pun. Bentuk akhirnya
// mirip, dan pelajarannya sama: yang menunggu sebaiknya berjalan
// BERSAMAAN, bukan berbaris satu-satu.

import kotlin.system.measureTimeMillis

fun ambil(nama: String, ms: Long): String {
    Thread.sleep(ms)
    return "$nama selesai (${ms}ms)"
}

fun main() {
    // --- BERURUTAN ---
    val berurutan = measureTimeMillis {
        println(ambil("A", 200))
        println(ambil("B", 200))
    }
    println("Berurutan ~${berurutan / 100 * 100} ms")

    println("---")

    // --- BERSAMAAN ---
    val hasil = mutableListOf<String>()
    val bersamaan = measureTimeMillis {
        val t1 = Thread { hasil.add(ambil("C", 200)) }
        val t2 = Thread { hasil.add(ambil("D", 200)) }
        t1.start(); t2.start()
        t1.join(); t2.join()
    }
    // Urutan selesainya thread TIDAK pasti: diurut supaya bisa diuji
    hasil.sorted().forEach { println(it) }
    println("Bersamaan ~${bersamaan / 100 * 100} ms")

    println("---")

    // Versi coroutine-nya akan berbentuk begini:
    //
    //   runBlocking {
    //       val a = async { ambilAsync("C", 200) }
    //       val b = async { ambilAsync("D", 200) }
    //       println(a.await())
    //       println(b.await())
    //   }
    //
    // Bedanya: async TIDAK membuat thread baru. Ribuan coroutine bisa
    // berbagi segelintir thread, karena yang sedang menunggu melepaskan
    // threadnya alih-alih menahannya seperti Thread.sleep di atas.
    println("Thread: mahal, ribuan sekaligus tidak mungkin.")
    println("Coroutine: murah, ratusan ribu sekaligus wajar.")
}"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  A selesai (200ms)",
                    "  B selesai (200ms)",
                    "  Berurutan ~400 ms",
                    "  ---",
                    "  C selesai (200ms)",
                    "  D selesai (200ms)",
                    "  Bersamaan ~200 ms",
                    "  ---",
                    "  Thread: mahal, ribuan sekaligus tidak mungkin.",
                    "  Coroutine: murah, ratusan ribu sekaligus wajar.",
                    "",
                    "Contoh di atas memakai Thread supaya bisa dijalankan",
                    "tanpa dependensi. Pelajarannya sama, dan kesalahan yang",
                    "dihindarinya juga sama: menulis `await()` tepat sesudah",
                    "`async` membuat pekerjaan yang seharusnya bersamaan jadi",
                    "berbaris satu-satu.",
                    "",
                    "  // SALAH: 400 ms",
                    "  val a = async { ambil(\"A\") }.await()",
                    "  val b = async { ambil(\"B\") }.await()",
                    "",
                    "  // BENAR: 200 ms",
                    "  val a = async { ambil(\"A\") }",
                    "  val b = async { ambil(\"B\") }",
                    "  println(a.await() + b.await())",
                    "",
                    "Bagian yang TIDAK bisa ditiru thread biasa adalah",
                    "ongkosnya. Satu thread JVM memakan sekitar satu megabyte",
                    "stack; satu coroutine beberapa ratus byte. Itu sebabnya",
                    "server berbasis coroutine bisa melayani ratusan ribu",
                    "koneksi bersamaan di mesin yang sama.",
                    "",
                    "Beberapa hal yang wajib diketahui saat memakai coroutine",
                    "sungguhan:",
                    "",
                    "  - `runBlocking` HANYA untuk main dan tes. Memakainya di",
                    "    kode produksi membuang seluruh gunanya.",
                    "  - `GlobalScope` melanggar structured concurrency dan",
                    "    hampir selalu salah.",
                    "  - `withContext(Dispatchers.IO)` untuk yang MENUNGGU,",
                    "    `Dispatchers.Default` untuk yang MENGHITUNG.",
                    "  - Pembatalan bersifat KOOPERATIF: kode yang tidak",
                    "    pernah suspend tidak bisa dibatalkan. Sisipkan",
                    "    `yield()` atau periksa `isActive` di perulangan",
                    "    panjang.",
                ]
            },
        ],
    },
    {
        "title": "14. Teks, Regex & Format",
        "sections": [
            {
                "body": [
                    "Method String yang paling sering dipakai:",
                    "  length  uppercase()  lowercase()",
                    "  trim()  trimStart()  trimEnd()  trimIndent()",
                    "  substring(2, 5)  take(3)  drop(3)  takeLast(3)",
                    "  indexOf(\"x\")  contains(\"x\")  startsWith / endsWith",
                    "  replace(\"a\", \"b\")  split(\",\")  lines()",
                    "  padStart(10)  padEnd(10)  repeat(3)  reversed()",
                    "  isEmpty()  isBlank()  isNotBlank()",
                    "  toIntOrNull()  toDoubleOrNull()",
                    "  format(...)  joinToString(...)",
                    "",
                    "String di Kotlin IMMUTABLE, sama seperti Java dan C#.",
                    "Semua method di atas mengembalikan string BARU.",
                    "",
                    "RAW STRING ditulis dengan TIGA kutip ganda: tanpa escape,",
                    "boleh multi-baris. `trimIndent()` memotong indentasi",
                    "bersamanya, dan `trimMargin()` memakai penanda garis",
                    "tegak kalau kamu ingin mengendalikan indentasinya sendiri.",
                    "",
                    "Raw string sangat cocok untuk regex dan path Windows:",
                    "polanya ditulis apa adanya tanpa menggandakan backslash.",
                    "",
                    "FORMAT memakai extension `format`:",
                    "  \"%-10s%5d%8.2f\".format(nama, jumlah, harga)",
                    "  \"%,d\".format(1234567)          -> 1,234,567",
                    "  \"%05d\".format(42)              -> 00042",
                    "  \"%+.1f\".format(3.14)           -> +3.1",
                    "",
                    "Sama seperti di Java, penentu `%,d` dan `%.2f` MENGIKUTI",
                    "setelan wilayah. Untuk keluaran yang harus sama di mesin",
                    "mana pun, oper Locale eksplisit:",
                    "  \"%.2f\".format(Locale.ROOT, nilai)",
                    "",
                    "REGEX adalah kelas tersendiri, bukan string:",
                    "",
                    "  val pola = Regex(\"\\\\d{4}-\\\\d{2}-\\\\d{2}\")",
                    "  pola.matches(teks)         SELURUH teks cocok",
                    "  pola.containsMatchIn(teks) ada di dalamnya",
                    "  pola.find(teks)            MatchResult pertama, atau null",
                    "  pola.findAll(teks)         Sequence semua kecocokan",
                    "  pola.replace(teks, \"x\")",
                    "  pola.split(teks)",
                    "",
                    "Perhatikan `matches` menuntut SELURUH teks cocok —",
                    "berbeda dari Ruby dan PHP tempat pencocokan bersifat",
                    "sebagian secara bawaan. Untuk validasi, ini justru",
                    "perilaku yang lebih aman.",
                    "",
                    "GRUP:",
                    "  m.groupValues[1]           berdasarkan nomor",
                    "  m.groups[\"tahun\"]?.value   berdasarkan nama",
                    "  val (a, b) = m.destructured",
                ]
            },
            {
                "heading": "Mengolah teks dan log",
                "code": """import java.util.Locale

fun main() {
    val kalimat = "Kotlin membuat kode Android jauh lebih ringkas"

    println("asli       : $kalimat")
    println("panjang    : ${kalimat.length}")
    println("kata       : ${kalimat.split(" ").size}")
    println("besar      : ${kalimat.uppercase()}")
    println("terbalik   : ${kalimat.reversed()}")
    println("ganti      : ${kalimat.replace("ringkas", "enak")}")
    println("terpanjang : ${kalimat.split(" ").maxBy { it.length }}")
    println("3 kata     : ${kalimat.split(" ").take(3).joinToString(" ")}")

    println("---")
    // Format dengan Locale tetap supaya sama di mesin mana pun
    val barang = listOf("Keyboard" to 350_000, "Mouse" to 85_000, "Monitor" to 1_750_000)
    println("%-12s%12s".format("Barang", "Harga"))
    println("-".repeat(24))
    barang.forEach { (nama, harga) ->
        println("%-12s%,12d".format(Locale.ROOT, nama, harga))
    }
    println("-".repeat(24))
    println("%-12s%,12d".format(Locale.ROOT, "TOTAL", barang.sumOf { it.second }))

    println("---")
    // Regex pada beberapa baris log
    val log = listOf(
        "2026-09-22 09:15:03 INFO  masuk user=andi ip=10.0.0.5",
        "2026-09-22 09:15:44 WARN  gagal user=budi ip=10.0.0.9",
        "baris yang formatnya tidak dikenal",
        "2026-09-22 09:16:10 ERROR koneksi putus ip=10.0.0.9",
    )

    val pola = Regex("^(\\\\d{4}-\\\\d{2}-\\\\d{2}) (\\\\d{2}:\\\\d{2}:\\\\d{2}) (\\\\w+)\\\\s+(.+)$")

    val cocok = log.mapNotNull { pola.find(it) }
    cocok.forEach { m ->
        val (_, jam, taraf, pesan) = m.destructured
        println("%-10s%-6s%s".format(jam, taraf, pesan))
    }
    println("dikenali   : ${cocok.size} dari ${log.size}")

    val ip = Regex("ip=(\\\\d{1,3}(?:\\\\.\\\\d{1,3}){3})")
        .findAll(log.joinToString("\\n"))
        .map { it.groupValues[1] }
        .distinct().sorted().toList()
    println("IP unik    : ${ip.joinToString(", ")}")

    println("---")
    // matches menuntut SELURUH teks cocok
    val tanggal = Regex("\\\\d{4}-\\\\d{2}-\\\\d{2}")
    listOf("2026-09-22", "tgl 2026-09-22", "22/09/2026").forEach {
        println("%-16s matches=%-6s contains=%s".format(
            it, tanggal.matches(it), tanggal.containsMatchIn(it)))
    }
}"""
            },
            {
                "body": [
                    "Keluaran (bagian pentingnya):",
                    "  asli       : Kotlin membuat kode Android jauh lebih ringkas",
                    "  panjang    : 46",
                    "  kata       : 7",
                    "  besar      : KOTLIN MEMBUAT KODE ANDROID JAUH LEBIH RINGKAS",
                    "  terbalik   : sakgnir hibel huaj diordnA edok taubmem niltoK",
                    "  ganti      : Kotlin membuat kode Android jauh lebih enak",
                    "  terpanjang : membuat",
                    "  3 kata     : Kotlin membuat kode",
                    "  ---",
                    "  Barang             Harga",
                    "  ------------------------",
                    "  Keyboard         350,000",
                    "  Mouse             85,000",
                    "  Monitor        1,750,000",
                    "  ------------------------",
                    "  TOTAL          2,185,000",
                    "  ---",
                    "  09:15:03  INFO  masuk user=andi ip=10.0.0.5",
                    "  09:15:44  WARN  gagal user=budi ip=10.0.0.9",
                    "  09:16:10  ERROR koneksi putus ip=10.0.0.9",
                    "  dikenali   : 3 dari 4",
                    "  IP unik    : 10.0.0.5, 10.0.0.9",
                    "  ---",
                    "  2026-09-22       matches=true   contains=true",
                    "  tgl 2026-09-22   matches=false  contains=true",
                    "  22/09/2026       matches=false  contains=false",
                    "",
                    "`m.destructured` memecah grup regex jadi variabel",
                    "sekaligus. Ia hanya bekerja untuk grup bernomor, dan",
                    "jumlah variabelnya harus cocok dengan jumlah grup di",
                    "polanya.",
                    "",
                    "Tiga baris terakhir menunjukkan perbedaan yang paling",
                    "sering menjebak: `matches` menuntut SELURUH teks cocok,",
                    "`containsMatchIn` cukup sebagiannya. Untuk memvalidasi",
                    "masukan, `matches` yang benar — dan Kotlin membuatnya",
                    "bentuk bawaan, berbeda dari Ruby dan PHP.",
                    "",
                    "`Locale.ROOT` pada `format` wajib kalau keluarannya harus",
                    "sama di mesin mana pun. Tanpa itu, penentu ribuan memakai",
                    "titik di locale Indonesia dan koma di locale Inggris —",
                    "dan sebuah tes yang lulus di laptopmu gagal di server.",
                    "",
                    "Di kode sungguhan, polanya lebih enak ditulis memakai raw",
                    "string tiga kutip supaya backslash-nya tidak perlu",
                    "digandakan.",
                ]
            },
        ],
    },
    {
        "title": "15. Berkas & Baris Perintah",
        "sections": [
            {
                "body": [
                    "Kotlin memakai java.io dan java.nio, tapi dengan",
                    "extension function yang membuatnya jauh lebih ringkas.",
                    "",
                    "  import java.io.File",
                    "",
                    "  File(\"data.txt\").writeText(isi)",
                    "  File(\"data.txt\").appendText(isi)",
                    "  File(\"data.txt\").readText()",
                    "  File(\"data.txt\").readLines()",
                    "  File(\"data.txt\").forEachLine { ... }",
                    "  File(\"data.txt\").useLines { baris -> ... }",
                    "",
                    "Untuk berkas BESAR, `useLines` yang benar: ia membaca",
                    "malas dan menutup berkasnya otomatis. `readLines()`",
                    "menarik seluruh isinya ke memori.",
                    "",
                    "Memeriksa dan mengelola:",
                    "  f.exists()  f.length()  f.isDirectory",
                    "  f.delete()  f.renameTo(g)  f.copyTo(g)",
                    "  f.mkdirs()  f.listFiles()",
                    "  f.name  f.extension  f.nameWithoutExtension  f.parent",
                    "",
                    "Menyusun path lintas sistem:",
                    "  File(folder, \"data.txt\")",
                    "  System.getProperty(\"java.io.tmpdir\")",
                    "",
                    "`use` adalah padanan try-with-resources dan berlaku untuk",
                    "apa pun yang Closeable:",
                    "  File(\"a.txt\").bufferedReader().use { it.readText() }",
                    "",
                    "JSON: Kotlin TIDAK punya pengurai JSON bawaan. Pilihan",
                    "yang lazim:",
                    "  kotlinx.serialization   resmi, memakai plugin compiler",
                    "  Gson / Jackson / Moshi  dari dunia Java",
                    "",
                    "Dengan kotlinx.serialization, satu anotasi sudah cukup:",
                    "",
                    "  @Serializable",
                    "  data class Murid(val nama: String, val nilai: Int)",
                    "",
                    "  Json.encodeToString(murid)",
                    "  Json.decodeFromString<Murid>(teks)",
                    "",
                    "Ia bekerja TANPA refleksi — kodenya dihasilkan compiler.",
                    "Itu sebabnya ia juga jalan di Kotlin/Native dan",
                    "Kotlin/JS, bukan cuma di JVM.",
                    "",
                    "ARGUMEN baris perintah masuk lewat parameter main:",
                    "  fun main(args: Array<String>) { ... }",
                    "",
                    "Variabel lingkungan: `System.getenv(\"HOME\")`.",
                    "Masukan: `readLine()` mengembalikan `String?` — null",
                    "kalau masukannya habis. Itu bukan kerewelan: masukan",
                    "yang dialirkan dari berkas memang bisa habis.",
                ]
            },
            {
                "heading": "Menulis, membaca, dan mengolah berkas",
                "code": """import java.io.File

data class Murid(val nama: String, val kelas: String, val nilai: Int)

fun List<Murid>.keCsv(): String = buildString {
    appendLine("nama,kelas,nilai")
    this@keCsv.forEach { appendLine("${it.nama},${it.kelas},${it.nilai}") }
}

fun String.keMurid(): List<Murid> =
    lines().drop(1).filter { it.isNotBlank() }.map { baris ->
        val (nama, kelas, nilai) = baris.split(",")
        Murid(nama, kelas, nilai.toInt())
    }

fun main() {
    val folder = System.getProperty("java.io.tmpdir")
    val berkas = File(folder, "belajar-kotlin.csv")

    val data = listOf(
        Murid("Andi", "A", 88),
        Murid("Budi", "B", 72),
        Murid("Cici", "A", 95),
    )

    berkas.writeText(data.keCsv())
    println("ditulis    : ${berkas.name} (${berkas.length()} byte)")

    val kembali = berkas.readText().keMurid()
    kembali.sortedByDescending { it.nilai }.forEach {
        println("  ${it.nama.padEnd(6)}${it.kelas} ${it.nilai.toString().padStart(3)}")
    }
    println("rata-rata  : %.2f".format(kembali.map { it.nilai }.average()))

    println("---")
    // Membaca baris demi baris, hemat memori dan menutup sendiri
    berkas.useLines { baris ->
        baris.withIndex().forEach { (i, b) ->
            println("${(i + 1).toString().padStart(2)}| $b")
        }
    }

    println("---")
    // Menyusun JSON dengan tangan untuk melihat bentuknya
    val json = kembali.joinToString(",\\n", "[\\n", "\\n]") {
        "  {\\"nama\\": \\"${it.nama}\\", \\"kelas\\": \\"${it.kelas}\\", \\"nilai\\": ${it.nilai}}"
    }
    println(json)

    println("---")
    berkas.delete()
    println("masih ada? ${berkas.exists()}")
    println("HOME ada?  ${System.getenv("HOME") != null}")
}"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  ditulis    : belajar-kotlin.csv (47 byte)",
                    "    Cici  A  95",
                    "    Andi  A  88",
                    "    Budi  B  72",
                    "  rata-rata  : 85.00",
                    "  ---",
                    "   1| nama,kelas,nilai",
                    "   2| Andi,A,88",
                    "   3| Budi,B,72",
                    "   4| Cici,A,95",
                    "  ---",
                    "  [",
                    "    {\"nama\": \"Andi\", \"kelas\": \"A\", \"nilai\": 88},",
                    "    {\"nama\": \"Budi\", \"kelas\": \"B\", \"nilai\": 72},",
                    "    {\"nama\": \"Cici\", \"kelas\": \"A\", \"nilai\": 95}",
                    "  ]",
                    "  ---",
                    "  masih ada? false",
                    "  HOME ada?  true",
                    "",
                    "`buildString { ... }` membuat StringBuilder, menjalankan",
                    "bloknya dengan StringBuilder itu sebagai penerima, lalu",
                    "mengembalikan hasilnya. Pola yang sama ada di",
                    "`buildList`, `buildMap`, dan `buildSet`.",
                    "",
                    "`this@keCsv` menyebut penerima extension function-nya,",
                    "karena di dalam `buildString` kata `this` sudah dipakai",
                    "oleh StringBuilder. Label penerima seperti ini muncul",
                    "setiap kali ada scope bersarang.",
                    "",
                    "`joinToString(pemisah, awalan, akhiran) { ... }` membangun",
                    "seluruh teks JSON dalam satu ekspresi. Tiga parameter",
                    "pertamanya sering terlupa padahal sangat berguna.",
                    "",
                    "`val (nama, kelas, nilai) = baris.split(\",\")` memakai",
                    "destructuring pada List — ia bekerja untuk hingga lima",
                    "komponen. Hati-hati: kalau barisnya punya kolom lebih",
                    "sedikit, ini melempar IndexOutOfBoundsException.",
                    "",
                    "PERINGATAN CSV yang sama seperti di bahasa lain:",
                    "`split(\",\")` hanya benar kalau tidak ada koma DI DALAM",
                    "kolom. Untuk data sungguhan pakai pustaka CSV; untuk",
                    "latihan seperti ini cukup, asal kamu tahu batasnya.",
                ]
            },
        ],
    },
    {
        "title": "16. Struktur Proyek & Gradle",
        "sections": [
            {
                "body": [
                    "PACKAGE mengelompokkan kode dan mencegah nama",
                    "bertabrakan:",
                    "",
                    "  package toko.domain",
                    "",
                    "  import toko.data.ProdukRepository",
                    "  import kotlin.math.sqrt",
                    "  import java.time.LocalDate as Tanggal      alias",
                    "",
                    "Berbeda dari Java, nama berkas TIDAK harus sama dengan",
                    "nama class, dan satu berkas boleh memuat beberapa class",
                    "sekaligus. Struktur folder juga tidak wajib mengikuti",
                    "package — meski mengikutinya tetap kebiasaan yang baik.",
                    "",
                    "Kotlin juga memperbolehkan fungsi dan properti di LEVEL",
                    "BERKAS, di luar class mana pun. Itu sebabnya kode",
                    "utilitas di Kotlin tidak butuh class `Utils` yang isinya",
                    "method statis semua.",
                    "",
                    "GRADLE adalah build tool yang dipakai hampir semua",
                    "proyek Kotlin, dan berkas konfigurasinya ditulis DALAM",
                    "Kotlin (build.gradle.kts). Perintah sehari-hari:",
                    "",
                    "  ./gradlew build          kompilasi + tes",
                    "  ./gradlew run            jalankan",
                    "  ./gradlew test           tes saja",
                    "  ./gradlew clean",
                    "  ./gradlew dependencies   pohon dependensi",
                    "",
                    "`./gradlew` adalah GRADLE WRAPPER — skrip yang mengunduh",
                    "versi Gradle yang TEPAT untuk proyek itu. Selalu pakai",
                    "wrapper, bukan `gradle` global: itulah yang membuat build",
                    "di mesinmu dan di CI menghasilkan hal yang sama.",
                    "",
                    "Beda `implementation` dan `api`:",
                    "  implementation  dependensi TIDAK diteruskan ke pemakai",
                    "                  pustakamu. Ini bawaan yang benar.",
                    "  api             ikut diteruskan. Pakai hanya kalau",
                    "                  tipenya muncul di tanda tangan publikmu.",
                    "",
                    "Memilih `implementation` membuat kompilasi ulang jauh",
                    "lebih cepat, karena perubahan di dependensi dalam tidak",
                    "memaksa seluruh proyek dikompilasi ulang.",
                ]
            },
            {
                "heading": "Struktur proyek Kotlin",
                "code": """proyekku/
├── build.gradle.kts        konfigurasi, ditulis dalam Kotlin
├── settings.gradle.kts     nama proyek dan daftar modul
├── gradle.properties
├── gradlew                 wrapper; SELALU pakai ini
├── gradle/
│   └── libs.versions.toml  katalog versi terpusat
└── src/
    ├── main/kotlin/
    │   └── toko/
    │       ├── Main.kt             fungsi main
    │       ├── domain/Produk.kt
    │       ├── data/ProdukRepo.kt
    │       └── util/Format.kt      fungsi level berkas
    └── test/kotlin/
        └── toko/
            └── domain/ProdukTest.kt"""
            },
            {
                "heading": "build.gradle.kts",
                "code": """plugins {
    kotlin("jvm") version "2.1.0"
    application
}

group = "id.belajar"
version = "0.1.0"

repositories {
    mavenCentral()
}

dependencies {
    implementation("org.jetbrains.kotlinx:kotlinx-coroutines-core:1.9.0")
    implementation("org.jetbrains.kotlinx:kotlinx-serialization-json:1.7.3")

    testImplementation(kotlin("test"))
}

kotlin {
    jvmToolchain(17)
}

application {
    mainClass.set("toko.MainKt")
}

tasks.test {
    useJUnitPlatform()
}"""
            },
            {
                "body": [
                    "Beberapa hal yang layak diperhatikan:",
                    "",
                    "`mainClass.set(\"toko.MainKt\")` — akhiran Kt itu bukan",
                    "salah ketik. Berkas `Main.kt` yang berisi fungsi level",
                    "atas dikompilasi jadi class bernama `MainKt`. Kalau kamu",
                    "menuliskannya tanpa akhiran itu, `./gradlew run` akan",
                    "mengeluh class tidak ditemukan.",
                    "",
                    "`jvmToolchain(17)` membuat Gradle MENGUNDUH JDK 17 kalau",
                    "belum ada, alih-alih memakai JDK apa pun yang kebetulan",
                    "terpasang. Ini yang membuat build di mesin berbeda",
                    "menghasilkan hal yang sama.",
                    "",
                    "`gradle/libs.versions.toml` adalah katalog versi: semua",
                    "nomor versi dikumpulkan di satu berkas, lalu dirujuk",
                    "dengan `libs.coroutines`. Di proyek bermodul banyak, ini",
                    "menghilangkan seluruh kelas masalah 'versi yang berbeda",
                    "di modul berbeda'.",
                    "",
                    "Berkas yang WAJIB masuk .gitignore:",
                    "  build/",
                    "  .gradle/",
                    "  local.properties",
                    "",
                    "Yang JUSTRU wajib masuk git: `gradlew`, `gradlew.bat`,",
                    "dan seluruh folder wrapper-nya. Tanpa itu, orang yang",
                    "meng-clone proyekmu tidak punya cara membangunnya.",
                    "",
                    "Alat bantu yang layak dipasang sejak awal:",
                    "  ktlint / ktfmt      perapi dan pemeriksa gaya",
                    "  detekt              analisis statis, menemukan bug",
                    "                      dan kerumitan berlebih",
                    "  kover               pengukur cakupan tes",
                ]
            },
        ],
    },
    {
        "title": "17. Pengujian",
        "sections": [
            {
                "body": [
                    "Kotlin memakai JUnit 5 lewat pembungkus `kotlin.test`",
                    "yang memberi nama assertion yang lebih terbaca.",
                    "",
                    "  testImplementation(kotlin(\"test\"))",
                    "  import kotlin.test.*",
                    "",
                    "NAMA FUNGSI DI DALAM BACKTICK adalah fitur Kotlin yang",
                    "sangat berguna di tes: nama boleh memuat spasi dan tanda",
                    "baca, sehingga laporan tes terbaca seperti kalimat.",
                    "",
                    "Assertion yang tersedia:",
                    "  assertEquals(harap, aktual)      URUTANNYA: harapan dulu",
                    "  assertNotEquals",
                    "  assertTrue / assertFalse",
                    "  assertNull / assertNotNull",
                    "  assertContains(koleksi, x)",
                    "  assertFailsWith<TipeError> { ... }",
                    "  assertIs<Tipe>(x)",
                    "  fail(\"pesan\")",
                    "",
                    "Untuk Double, JANGAN assertEquals biasa — pecahan biner",
                    "tidak pernah persis. Pakai toleransi:",
                    "  assertEquals(85.0, hasil, 0.001)",
                    "",
                    "Anotasi siklus hidup:",
                    "  @BeforeTest   sebelum SETIAP tes",
                    "  @AfterTest    sesudah SETIAP tes",
                    "  @Ignore       lewati",
                    "",
                    "`@BeforeTest` penting: ia membuat tiap tes mulai dari",
                    "keadaan yang sama persis. Tes yang bergantung pada urutan",
                    "menjalankannya adalah tes yang suatu hari gagal tanpa ada",
                    "yang mengubah apa pun.",
                    "",
                    "MENGUJI DI BATAS adalah kebiasaan yang paling berharga:",
                    "uji 85 dan 84, bukan 90 dan 50. Di batas itulah `>=`",
                    "versus `>` salah ketik.",
                    "",
                    "Pustaka pihak ketiga yang lazim:",
                    "  kotest      gaya spesifikasi + property-based testing",
                    "  mockk       pembuat objek palsu, dirancang untuk Kotlin",
                    "  turbine     menguji Flow",
                    "  kotlinx-coroutines-test   runTest, waktu virtual",
                    "",
                    "`runTest` memakai WAKTU VIRTUAL, sehingga jeda sepuluh",
                    "detik di dalam tes selesai seketika alih-alih menunggu",
                    "sungguhan.",
                ]
            },
            {
                "heading": "Kelas beserta tesnya",
                "code": """// ==== File: src/main/kotlin/Rapor.kt ====
class Rapor {
    private val nilai = mutableMapOf<String, Int>()

    fun catat(nama: String, n: Int): Rapor {
        require(n in 0..100) { "nilai $n di luar 0..100" }
        nilai[nama] = n
        return this
    }

    fun rataRata(): Double? =
        if (nilai.isEmpty()) null else nilai.values.average()

    fun lulus(): List<String> =
        nilai.filterValues { it >= 75 }.keys.sorted()

    companion object {
        fun grade(n: Int): String = when {
            n >= 85 -> "A"
            n >= 75 -> "B"
            n >= 60 -> "C"
            else -> "D"
        }
    }
}

// ==== File: src/test/kotlin/RaporTest.kt ====
import kotlin.test.AfterTest
import kotlin.test.BeforeTest
import kotlin.test.Test
import kotlin.test.assertContains
import kotlin.test.assertEquals
import kotlin.test.assertFailsWith
import kotlin.test.assertNull

class RaporTest {
    private lateinit var rapor: Rapor

    @BeforeTest
    fun siapkan() {
        rapor = Rapor()          // tiap tes mulai dari nol
    }

    @Test
    fun `grade tepat di batas tiap huruf`() {
        // Di batas inilah tanda lebih-besar-sama-dengan salah ketik
        val kasus = listOf(
            85 to "A", 84 to "B", 75 to "B",
            74 to "C", 60 to "C", 59 to "D", 0 to "D",
        )
        kasus.forEach { (n, harap) ->
            assertEquals(harap, Rapor.grade(n), "gagal di nilai $n")
        }
    }

    @Test
    fun `rata-rata kosong menghasilkan null`() {
        assertNull(rapor.rataRata())
    }

    @Test
    fun `rata-rata dihitung benar`() {
        rapor.catat("Andi", 80).catat("Budi", 90)
        assertEquals(85.0, rapor.rataRata()!!, 0.001)
    }

    @Test
    fun `lulus terurut dan hanya yang lulus`() {
        rapor.catat("Cici", 95).catat("Budi", 64).catat("Andi", 75)
        assertEquals(listOf("Andi", "Cici"), rapor.lulus())
    }

    @Test
    fun `nilai di luar rentang ditolak`() {
        val e = assertFailsWith<IllegalArgumentException> {
            rapor.catat("Andi", 150)
        }
        assertContains(e.message!!, "di luar 0..100")
    }
}"""
            },
            {
                "body": [
                    "Perhatikan nilai yang dipilih di tes grade: 85 dan 84,",
                    "75 dan 74, 60 dan 59. Menguji tepat di batas jauh lebih",
                    "berharga daripada menguji nilai di tengah rentang, yang",
                    "hampir tidak pernah menemukan bug.",
                    "",
                    "`assertEquals(harap, aktual, \"pesan\")` — argumen ketiga",
                    "muncul saat tesnya gagal. Di tes berulang seperti di",
                    "atas, tanpa pesan itu kamu cuma tahu 'ada yang gagal',",
                    "bukan yang mana.",
                    "",
                    "`assertEquals(85.0, hasil, 0.001)` memakai toleransi.",
                    "Tanpa itu, pecahan biner yang tidak pernah persis akan",
                    "membuat tesmu gagal secara acak.",
                    "",
                    "`catat` mengembalikan `this`, sehingga penyiapan data tes",
                    "jadi satu baris alih-alih tiga. Ini bukan kebetulan: API",
                    "yang enak diuji biasanya juga API yang enak dipakai.",
                    "",
                    "Menjalankan:",
                    "  ./gradlew test",
                    "  ./gradlew test --tests \"*grade*\"",
                    "  ./gradlew test --info          keluaran lengkap",
                    "",
                    "Cakupan tes berguna untuk MENEMUKAN yang belum diuji,",
                    "bukan sebagai angka yang dikejar. Cakupan seratus persen",
                    "dengan assertion yang lemah lebih buruk daripada tujuh",
                    "puluh persen yang benar-benar memeriksa perilaku.",
                ]
            },
        ],
    },
    {
        "title": "18. Proyek Utuh: Menggabungkan Semuanya",
        "sections": [
            {
                "body": [
                    "Materi penutup ini menggabungkan data class, sealed",
                    "class, koleksi, scope function, dan pemisahan tanggung",
                    "jawab dalam satu program utuh.",
                    "",
                    "Yang dibangun: sistem inventaris gudang. Yang penting",
                    "bukan fiturnya melainkan CARA bagiannya dipisah.",
                    "",
                    "Tiga lapisan, panah ketergantungan satu arah:",
                    "",
                    "  Antarmuka  ->  Layanan  ->  Model",
                    "",
                    "  MODEL     data class Barang, enum Gerak, dan sealed",
                    "            class galatnya. Tidak tahu apa-apa tentang",
                    "            layar.",
                    "  LAYANAN   class Gudang dengan seluruh aturannya. TIDAK",
                    "            PERNAH memanggil println.",
                    "  ANTARMUKA main: memanggil layanan, mencetak hasilnya.",
                    "",
                    "Yang khas Kotlin di sini: kegagalan TIDAK dilempar",
                    "sebagai exception melainkan DIKEMBALIKAN sebagai bagian",
                    "dari tipenya, lewat sealed class.",
                    "",
                    "Bedanya nyata:",
                    "  - Compiler MEMAKSA pemanggil menangani setiap cabang,",
                    "    karena `when` atas sealed class diperiksa",
                    "    kelengkapannya.",
                    "  - Tidak ada jalur kegagalan yang tak terlihat di tanda",
                    "    tangan fungsinya.",
                    "  - Menambah jenis galat baru langsung membuat setiap",
                    "    `when` yang belum diperbarui gagal dikompilasi.",
                    "",
                    "Ini pola yang sama dengan Result di Rust, dan ia tersedia",
                    "di Kotlin tanpa fitur bahasa tambahan apa pun — cukup",
                    "sealed class.",
                ]
            },
            {
                "heading": "Program lengkap",
                "code": """// ---------------------------------------------------------------- MODEL
data class Barang(
    val kode: String,
    val nama: String,
    val stok: Int,
    val harga: Long,
) {
    val subtotal: Long get() = stok * harga

    override fun toString() =
        "%-5s%-12s%2d%10d%12d".format(kode, nama, stok, harga, subtotal)
}

enum class Gerak { MASUK, KELUAR }

sealed class GalatGudang(val pesan: String) {
    class KodeSudahAda(kode: String) : GalatGudang("kode $kode sudah ada")
    class KodeTidakDikenal(kode: String) : GalatGudang("kode $kode tidak dikenal")
    class JumlahTidakSah(n: Int) : GalatGudang("jumlah $n tidak sah")
    class StokTidakCukup(punya: Int, diminta: Int) :
        GalatGudang("stok cuma $punya, diminta $diminta")
}

sealed class Hasil<out T> {
    data class Ok<T>(val nilai: T) : Hasil<T>()
    data class Salah(val galat: GalatGudang) : Hasil<Nothing>()
}

// -------------------------------------------------------------- LAYANAN
class Gudang {
    private val isi = linkedMapOf<String, Barang>()

    fun daftar(b: Barang): Hasil<Barang> {
        if (b.kode in isi) return Hasil.Salah(GalatGudang.KodeSudahAda(b.kode))
        isi[b.kode] = b
        return Hasil.Ok(b)
    }

    fun catat(kode: String, gerak: Gerak, jumlah: Int): Hasil<Int> {
        val b = isi[kode] ?: return Hasil.Salah(GalatGudang.KodeTidakDikenal(kode))
        if (jumlah <= 0) return Hasil.Salah(GalatGudang.JumlahTidakSah(jumlah))

        val baru = if (gerak == Gerak.MASUK) b.stok + jumlah else b.stok - jumlah
        if (baru < 0) {
            return Hasil.Salah(GalatGudang.StokTidakCukup(b.stok, jumlah))
        }

        isi[kode] = b.copy(stok = baru)
        return Hasil.Ok(baru)
    }

    fun semua(): List<Barang> = isi.values.sortedBy { it.kode }

    fun nilaiPersediaan(): Long = isi.values.sumOf { it.subtotal }

    fun stokMenipis(batas: Int): List<Barang> =
        isi.values.filter { it.stok < batas }
            .sortedWith(compareBy({ it.stok }, { it.kode }))
}

// ------------------------------------------------------------ ANTARMUKA
fun main() {
    val gudang = Gudang()

    listOf(
        Barang("B01", "Kabel", 10, 15_000),
        Barang("B02", "Adaptor", 4, 85_000),
        Barang("B03", "Mouse", 25, 120_000),
    ).forEach { gudang.daftar(it) }

    val langkah = listOf(
        Triple("B01", Gerak.MASUK, 15),
        Triple("B02", Gerak.KELUAR, 10),
        Triple("B03", Gerak.KELUAR, 5),
        Triple("B09", Gerak.MASUK, 1),
        Triple("B03", Gerak.KELUAR, 0),
    )

    for ((kode, gerak, jumlah) in langkah) {
        val aksi = gerak.name.lowercase().replaceFirstChar { it.uppercase() }
        val label = "$aksi $kode $jumlah"
        // when atas sealed class: compiler memeriksa kelengkapannya
        when (val hasil = gudang.catat(kode, gerak, jumlah)) {
            is Hasil.Ok -> println("$label -> stok ${hasil.nilai}")
            is Hasil.Salah -> println("$label -> DITOLAK: ${hasil.galat.pesan}")
        }
    }

    println("---")
    gudang.semua().forEach { println(it) }

    println("---")
    println("nilai persediaan: ${gudang.nilaiPersediaan()}")

    val menipis = gudang.stokMenipis(10)
        .joinToString(", ") { "${it.kode} ${it.nama} (${it.stok})" }
    println("stok menipis (<10): $menipis")
}"""
            },
            {
                "body": [
                    "Empat keputusan yang layak ditiru:",
                    "",
                    "  1. Kegagalan dikembalikan lewat sealed class, bukan",
                    "     dilempar. Tanda tangan `catat` menyatakan bahwa ia",
                    "     bisa gagal, dan `when` atasnya WAJIB lengkap. Jalur",
                    "     kegagalan jadi tidak mungkin terlewat diam-diam.",
                    "",
                    "  2. `Barang` adalah data class yang TIDAK BISA DIUBAH.",
                    "     Perubahan stok dilakukan dengan `copy(stok = baru)`,",
                    "     menghasilkan objek baru. Tidak ada tempat lain di",
                    "     program yang bisa memegang Barang lalu mengubah",
                    "     stoknya diam-diam.",
                    "",
                    "  3. `semua()` dan `stokMenipis()` MENGURUTKAN sebelum",
                    "     mengembalikan. Keluaran yang urutannya tidak pasti",
                    "     mustahil diuji.",
                    "",
                    "  4. Gudang tidak memanggil println sama sekali. Itu yang",
                    "     membuat seluruh aturannya bisa diuji dengan",
                    "     assertEquals tanpa membaca layar.",
                    "",
                    "`when (val hasil = gudang.catat(...))` menggabungkan",
                    "penugasan dan pencocokan dalam satu baris — bentuk yang",
                    "sangat lazim di Kotlin dan membuat variabelnya hidup",
                    "hanya di dalam `when` itu.",
                    "",
                    "`compareBy({ it.stok }, { it.kode })` membuat pembanding",
                    "dua tingkat dalam satu ekspresi. Untuk urutan menurun,",
                    "pasangannya `compareByDescending`.",
                    "",
                    "Langkah berikutnya kalau kamu ingin melanjutkannya:",
                    "  - Simpan ke JSON dengan kotlinx.serialization.",
                    "  - Sembunyikan penyimpanan di balik sebuah interface,",
                    "    sehingga Gudang tidak tahu datanya di berkas, di",
                    "    database, atau cuma di memori saat tes.",
                    "  - Jadikan operasinya suspend dan panggil dari coroutine.",
                    "  - Tulis tes untuk Gudang — perhatikan ini langsung",
                    "    bisa dilakukan tanpa mengubah satu baris pun, justru",
                    "    karena keputusan nomor 4.",
                ]
            },
        ],
    },
]
