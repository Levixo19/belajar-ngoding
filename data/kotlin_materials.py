KOTLIN_MATERIALS = [
    {
        "title": "1. Pengenalan Kotlin & Instalasi",
        "sections": [
            {
                "body": [
                    "Kotlin adalah bahasa pemrograman buatan JetBrains. Versi 1.0-nya rilis",
                    "tahun 2016. Sejak 2019, Kotlin jadi bahasa yang diutamakan Google untuk",
                    "bikin aplikasi Android.",
                    "",
                    "Beberapa sifat dasarnya:",
                    "  - Statically typed. Artinya tipe tiap variabel sudah pasti waktu",
                    "    kodenya dikompilasi, yaitu diterjemahkan oleh compiler jadi bentuk",
                    "    yang bisa dijalankan. Salah tipe jadi ketahuan sebelum program",
                    "    jalan.",
                    "  - Inferensi tipenya kuat. Kamu sering nggak perlu menulis tipe,",
                    "    karena compiler bisa menyimpulkannya sendiri dari nilainya.",
                    "  - Berjalan di atas JVM (Java Virtual Machine), mesin yang juga",
                    "    menjalankan program Java. Kotlin juga bisa dikompilasi ke",
                    "    JavaScript, ke program native yang jalan tanpa JVM, dan ke",
                    "    WebAssembly, format program yang bisa jalan di dalam browser.",
                    "",
                    "Kotlin lahir dari satu keluhan: kode Java kebanyakan basa-basi. Untuk",
                    "hal sederhana pun kamu harus menulis banyak baris. Targetnya juga bukan",
                    "jadi bahasa paling canggih. Kotlin dirancang supaya bisa menggantikan",
                    "Java sedikit demi sedikit di proyek yang sudah ada.",
                    "",
                    "Makanya fitur utamanya adalah interoperabilitas, yaitu kemampuan",
                    "bekerja bareng kode Java:",
                    "  - Kode Kotlin bisa memanggil kode Java, dan sebaliknya.",
                    "  - Satu proyek boleh berisi berkas .java dan .kt sekaligus.",
                    "  - Semua pustaka Java bisa langsung dipakai. Pustaka itu kumpulan kode",
                    "    siap pakai buatan orang lain.",
                    "",
                    "Perbaikan yang dibawa Kotlin juga lebih dari soal gaya penulisan:",
                    "  - Null diperiksa compiler. Null artinya \"nggak ada isinya\". Di Java,",
                    "    memakai nilai yang ternyata null bikin program berhenti dengan",
                    "    NullPointerException, dan error itu baru muncul waktu program",
                    "    jalan. Di Kotlin, kesalahan yang sama sudah ditolak waktu",
                    "    kompilasi.",
                    "  - Data class, yaitu class khusus untuk menyimpan data. Satu baris",
                    "    data class menggantikan 60 baris boilerplate untuk sebuah POJO",
                    "    (Plain Old Java Object), class Java biasa yang isinya cuma data.",
                    "    Boilerplate itu kode berulang yang isinya itu-itu aja.",
                    "  - Nggak ada checked exception. Di Java, checked exception adalah",
                    "    error yang wajib kamu tangkap pakai try-catch atau kamu umumkan di",
                    "    fungsinya. Kotlin nggak memaksamu menulis try-catch.",
                    "  - Extension function, cara menambah method (fungsi milik class) ke",
                    "    class yang bukan milikmu, misalnya ke String.",
                    "  - Coroutine untuk kode asinkron tanpa callback. Kode asinkron itu",
                    "    kode yang harus menunggu sesuatu, misalnya jawaban dari internet.",
                    "    Callback adalah fungsi yang dititipkan supaya dipanggil nanti",
                    "    kalau tunggunya selesai.",
                    "",
                    "Kotlin dipakai untuk sebagian besar aplikasi Android modern, untuk",
                    "backend (program yang jalan di server) dengan Ktor dan Spring Boot, dan",
                    "untuk aplikasi lintas platform lewat Compose Multiplatform.",
                    "",
                    "Untuk memasang Kotlin, kamu butuh JDK 17 atau yang lebih baru. JDK",
                    "(Java Development Kit) itu paket alat untuk mengompilasi dan",
                    "menjalankan program Java, dan Kotlin numpang di situ. Pasang JDK dulu,",
                    "lalu pilih salah satu perintah ini:",
                    "",
                    "  Fedora   : sudo dnf install kotlin",
                    "  SDKMAN   : sdk install kotlin",
                    "  macOS    : brew install kotlin",
                    "  Windows  : choco install kotlinc",
                    "",
                    "Kata sudo di perintah Fedora artinya perintah itu dijalankan dengan hak",
                    "admin, jadi kamu bakal diminta kata sandi. Sesudah terpasang, cek",
                    "dengan perintah di bawah. Kalau yang keluar nomor versi, Kotlin siap",
                    "dipakai.",
                    "",
                    "  kotlinc -version",
                    "",
                    "Ada dua cara menjalankan program Kotlin dari terminal. Cara pertama,",
                    "kompilasi jadi satu berkas jar, lalu jalankan dengan perintah java.",
                    "Jar adalah satu berkas yang membungkus seluruh program. Opsi -d",
                    "menentukan ke mana hasil kompilasinya ditulis, dan -include-runtime",
                    "memasukkan pustaka bawaan Kotlin ke dalam jar itu supaya java bisa",
                    "menjalankannya.",
                    "",
                    "  kotlinc main.kt -include-runtime -d main.jar",
                    "  java -jar main.jar",
                    "",
                    "Cara kedua, kompilasi ke folder kelas, lalu jalankan dengan perintah",
                    "kotlin. Tanda && artinya perintah kedua cuma jalan kalau perintah",
                    "pertama berhasil. Asal nama MainKt dijelaskan sesudah contoh program",
                    "di bawah.",
                    "",
                    "  kotlinc main.kt -d kelas && kotlin -cp kelas MainKt",
                    "",
                    "Kalau kotlinc dijalankan tanpa nama berkas, yang terbuka adalah REPL,",
                    "yaitu sesi interaktif: kamu ketik satu baris, Kotlin langsung",
                    "menjalankannya.",
                    "",
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
                    "Dibanding Java, beberapa hal langsung kelihatan beda:",
                    "  - Nggak ada class pembungkus. `fun main()` boleh berdiri sendiri di",
                    "    level berkas, di luar class mana pun.",
                    "  - Nggak ada titik koma di akhir baris.",
                    "  - Nggak ada `public static void`.",
                    "  - Tipe ditulis sesudah nama, dipisah titik dua, misalnya",
                    "    `val umur: Int`.",
                    "  - `val` untuk nilai yang nggak berubah, `var` untuk yang bisa",
                    "    berubah.",
                    "",
                    "Nama berkas menentukan nama class yang dihasilkan compiler. Berkas",
                    "`main.kt` jadi class `MainKt`, dan class itulah yang dijalankan JVM.",
                    "Nama ini perlu kamu tahu kalau menjalankan program tanpa jar, seperti",
                    "perintah `kotlin -cp kelas MainKt` tadi.",
                    "",
                    "Untuk memasukkan nilai ke dalam teks, pakai tanda dolar. Cara ini",
                    "namanya interpolasi string:",
                    "",
                    "  \"$nama\"            variabel sederhana",
                    "  \"${2026 - 2006}\"   ekspresi apa pun, pakai kurawal",
                    "  \"\"\"mentah\"\"\"       tanpa escape, boleh multi-baris",
                    "",
                    "Yang terakhir namanya raw string, teks mentah yang diapit tiga tanda",
                    "kutip. Di dalamnya nggak ada escape, yaitu kode berawalan backslash",
                    "seperti \\n untuk pindah baris. Teksnya juga boleh lebih dari satu",
                    "baris.",
                    "",
                    "Kalau kamu butuh tanda dolar apa adanya, tulis `${'$'}` atau escape",
                    "`\\$`. Cara kedua cuma berlaku di string biasa, nggak di raw string.",
                    "",
                    "`repeat(3) { ... }` kelihatan seperti perintah bawaan, padahal cuma",
                    "pemanggilan fungsi biasa. Fungsi repeat menerima sebuah lambda, yaitu",
                    "fungsi tanpa nama yang ditulis langsung di tempat dipakai, di dalam",
                    "kurung kurawal. Kotlin punya aturan khusus: lambda yang jadi argumen",
                    "terakhir boleh ditulis di luar tanda kurung. Aturan ini yang bikin",
                    "kode Kotlin sering kelihatan seperti punya sintaks bawaan.",
                    "",
                    "Di contoh tadi, `i` adalah parameter lambdanya, yaitu nilai yang",
                    "diterima lambda tiap kali dipanggil. Isinya nomor putaran yang dimulai",
                    "dari 0, makanya program mencetak `i + 1` supaya hitungannya mulai dari",
                    "1.",
                    "",
                    "Kebiasaan penamaan di Kotlin:",
                    "",
                    "  camelCase       fungsi, properti, variabel lokal",
                    "  PascalCase      class, interface, object",
                    "  SCREAMING_CASE  konstanta di level atas",
                    "",
                    "Konstanta adalah nilai yang nggak pernah berubah. Properti, interface,",
                    "dan object dibahas di materi-materi berikutnya, jadi untuk sekarang",
                    "cukup kenali bentuk namanya. Indentasinya empat spasi per tingkat.",
                ]
            },
        ],
    },
    {
        "title": "2. val, var & Tipe Data",
        "sections": [
            {
                "body": [
                    "Kotlin punya dua kata kunci untuk bikin variabel, dan tiap kali bikin",
                    "variabel kamu memilih salah satunya:",
                    "",
                    "  val nama = \"Andi\"     tidak bisa diisi ulang",
                    "  var umur = 20         bisa diisi ulang",
                    "",
                    "Gampangnya, val itu singkatan value (nilai) dan var singkatan variable.",
                    "Sesudah diisi, val nggak bisa diisi nilai lain, sedangkan var boleh.",
                    "",
                    "Hati-hati, val nggak berarti isinya beku. Sebuah val yang menunjuk",
                    "MutableList, yaitu daftar yang isinya bisa ditambah, tetap boleh",
                    "ditambahi. Yang nggak bisa diubah cuma ke mana val itu menunjuk.",
                    "",
                    "Aturan praktisnya: pakai val dulu, dan ganti ke var cuma kalau compiler",
                    "memaksamu. Di kode Kotlin yang rapi, var jarang muncul.",
                    "",
                    "Tipe boleh kamu tulis, boleh juga disimpulkan compiler dari nilainya:",
                    "",
                    "  val umur: Int = 20",
                    "  val umur = 20              sama saja",
                    "  var nanti: String          wajib bertipe kalau belum diisi",
                    "",
                    "Baris terakhir belum punya nilai, jadi compiler nggak punya petunjuk",
                    "apa pun. Di situ tipenya wajib ditulis.",
                    "",
                    "Ini tipe-tipe bilangan beserta ukurannya dalam bit. Makin banyak",
                    "bitnya, makin besar angka yang muat:",
                    "",
                    "  Byte    8 bit      Short   16 bit",
                    "  Int     32 bit     Long    64 bit",
                    "  Float   32 bit     Double  64 bit",
                    "  UByte UShort UInt ULong    tanpa tanda",
                    "",
                    "Empat yang terakhir disebut unsigned (tanpa tanda), artinya nggak bisa",
                    "negatif. Untuk bilangan bulat, tipe bawaannya Int. Untuk pecahan,",
                    "Double. Angka Long ditulis dengan akhiran L (100L), dan Float dengan",
                    "akhiran f (3.14f).",
                    "",
                    "Tipe lainnya: Boolean untuk true atau false, Char untuk satu huruf",
                    "yang diapit kutip tunggal seperti 'K', dan String untuk teks.",
                    "",
                    "Kotlin nggak pernah mengubah tipe angka secara otomatis. Int ke Long",
                    "pun harus kamu tulis sendiri:",
                    "",
                    "  val besar: Long = angka.toLong()",
                    "",
                    "Fungsi konversinya: toByte, toShort, toInt, toLong, toFloat, toDouble,",
                    "toChar, dan toString.",
                    "",
                    "Untuk mengubah teks jadi angka ada dua pilihan, dan bedanya penting:",
                    "",
                    "  \"42\".toInt()          melempar error kalau gagal",
                    "  \"42\".toIntOrNull()    null kalau gagal",
                    "",
                    "Melempar error artinya program berhenti dengan exception kalau nggak",
                    "ada yang menangkapnya. Untuk masukan dari pengguna, toIntOrNull()",
                    "hampir selalu pilihan yang tepat, karena salah ketik itu kejadian",
                    "biasa.",
                    "",
                    "Untuk konstanta, yaitu nilai yang nggak pernah berubah, ada dua",
                    "bentuk:",
                    "",
                    "  const val MAKS = 100      saat kompilasi, level atas",
                    "  val sekarang = hitung()   saat program jalan",
                    "",
                    "Nilai const val sudah ditentukan waktu kompilasi, jadi isinya harus",
                    "nilai sederhana yang langsung ditulis, seperti angka atau teks. Bentuk",
                    "ini cuma boleh ada di level atas berkas atau di dalam object, nggak",
                    "boleh di dalam fungsi. Sedangkan val biasa baru dihitung waktu program",
                    "jalan, jadi boleh diisi hasil fungsi seperti hitung().",
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
                    "7 / 2 hasilnya 3, karena pembagian dua bilangan bulat membuang",
                    "pecahannya. Begitu salah satunya Double (7.0), hasilnya 3.5. Tanda %",
                    "memberi sisa baginya. \"3.5\" juga menghasilkan null di toIntOrNull(),",
                    "karena 3.5 bukan bilangan bulat.",
                    "",
                    "Baris terakhir menunjukkan hal yang paling sering disalahpahami. Kata",
                    "val mencegah variabelnya diisi ulang, tapi isinya tetap boleh diubah. Kalau",
                    "kamu butuh daftar yang memang nggak bisa diubah, pakai `listOf`, bukan",
                    "`mutableListOf`.",
                    "",
                    "Kotlin membedakan dua jenis daftar itu lewat tipenya:",
                    "",
                    "  List<T>          hanya baca",
                    "  MutableList<T>   bisa ditambah dan dihapus",
                    "",
                    "T di situ artinya tipe isinya, misalnya List<Int> untuk daftar angka.",
                    "Ini beda dari Java. Di Java, List selalu punya method add, dan",
                    "kesalahan menambah ke daftar yang nggak boleh diubah baru ketahuan",
                    "waktu program jalan, sebagai UnsupportedOperationException.",
                    "",
                    "Satu lagi yang halus: List<T> di Kotlin disebut read-only (hanya baca),",
                    "dan itu belum tentu immutable (nggak bisa berubah sama sekali). Kalau",
                    "List itu ternyata membungkus sebuah MutableList, kode lain yang",
                    "memegang MutableList-nya masih bisa mengubah isinya. Kalau kamu butuh",
                    "jaminan isinya nggak berubah, salin dulu dengan `.toList()`.",
                ]
            },
        ],
    },
    {
        "title": "3. Null Safety",
        "sections": [
            {
                "body": [
                    "Null artinya \"nggak ada isinya\". Bayangin kotak surat yang kosong:",
                    "kotaknya ada, tapi nggak ada surat yang bisa diambil. Di banyak bahasa,",
                    "memakai nilai yang ternyata null bikin program berhenti dengan error.",
                    "Di Java, error itu namanya NullPointerException.",
                    "",
                    "Null safety (pengaman null) adalah fitur yang paling sering disebut",
                    "orang waktu ditanya kenapa memilih Kotlin. Idenya: di Kotlin, sebuah",
                    "tipe nggak boleh bernilai null, kecuali kamu bilang boleh.",
                    "",
                    "  var nama: String = \"Andi\"",
                    "  nama = null            error waktu kompilasi",
                    "",
                    "  var nama: String? = \"Andi\"",
                    "  nama = null            sah",
                    "",
                    "Bedanya cuma tanda tanya di belakang tipe, dan seluruh fiturnya ada di",
                    "tanda tanya itu. String dan String? adalah dua tipe yang berbeda.",
                    "String pasti berisi teks. String? boleh berisi teks, boleh juga null.",
                    "Compiler nggak akan mengizinkanmu memakai String? seolah-olah String.",
                    "",
                    "Akibatnya, NullPointerException, yang di Java baru muncul waktu program",
                    "sudah dipakai orang, di Kotlin jadi error kompilasi. Kamu ketemu",
                    "kesalahannya sebelum programnya jalan.",
                    "",
                    "Ada beberapa cara memakai nilai yang mungkin null.",
                    "",
                    "Safe call (?.), artinya \"panggil kalau ada isinya\":",
                    "",
                    "  nama?.length          null kalau nama null",
                    "  a?.b?.c?.d            berantai, berhenti di null pertama",
                    "",
                    "Elvis (?:), artinya \"kalau kirinya null, pakai yang kanan\". Namanya",
                    "diambil dari bentuk ?: yang mirip jambul penyanyi Elvis Presley kalau",
                    "dilihat miring:",
                    "",
                    "  nama?.length ?: 0     pakai 0 kalau kirinya null",
                    "  val n = cari() ?: return",
                    "  val n = cari() ?: throw IllegalStateException(\"...\")",
                    "",
                    "Sisi kanan Elvis boleh berisi return (keluar dari fungsi) atau throw",
                    "(melempar error). Jadi kalau cari() menghasilkan null, fungsinya",
                    "berhenti di baris itu.",
                    "",
                    "Safe call ditambah let, untuk menjalankan satu blok kode cuma kalau",
                    "nilainya ada:",
                    "",
                    "  nama?.let { println(it.uppercase()) }",
                    "",
                    "Blok di dalam kurung kurawal itu hanya jalan kalau nama bukan null. Di",
                    "dalam blok, `it` adalah isi nama yang sudah pasti ada.",
                    "",
                    "Not-null assertion (!!), artinya \"aku jamin ini nggak null\":",
                    "",
                    "  nama!!.length         melempar NullPointerException kalau null",
                    "",
                    "Dua tanda seru itu sama dengan bilang \"percaya aja sama aku\". Tiap kali",
                    "kamu menulisnya, tanggung jawab ngecek null pindah dari compiler ke",
                    "kamu. Kadang itu memang perlu. Tapi kalau satu berkas penuh `!!`,",
                    "artinya pengaman null di berkas itu udah mati tanpa ada yang sadar.",
                    "",
                    "Yang bikin pengaman null ini enak dipakai adalah smart cast. Sesudah",
                    "kamu memeriksa sebuah nilai, compiler ingat hasilnya dan otomatis",
                    "memperlakukan nilai itu sesuai hasil pemeriksaannya:",
                    "",
                    "  if (nama != null) {",
                    "      println(nama.length)    <- tanpa ?. atau !!",
                    "  }",
                    "",
                    "Di dalam if itu, nama diperlakukan sebagai String biasa. Smart cast",
                    "juga berlaku sesudah pemeriksaan tipe dengan `is`, dan sesudah return",
                    "lebih awal, yaitu keluar dari fungsi duluan kalau nilainya null. Smart",
                    "cast juga jalan di dalam `when`, pengganti switch yang dibahas di",
                    "materi Kendali Alur.",
                    "",
                    "Pengecualiannya, smart cast nggak berlaku untuk var milik class. Nilai",
                    "seperti itu bisa diubah thread lain, yaitu bagian program yang jalan",
                    "bersamaan, di antara pemeriksaan dan pemakaian. Jadi compiler nggak",
                    "bisa menjamin nilainya masih sama.",
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
                    "`isNullOrBlank()` menangani tiga kasus sekaligus: null, string kosong,",
                    "dan string yang isinya spasi semua. Pasangannya `isNullOrEmpty()`, yang",
                    "nggak memeriksa spasi. Untuk memeriksa masukan pengguna, yang pertama",
                    "hampir selalu yang kamu maksud.",
                    "",
                    "Sesudah baris if di fungsi sapa, compiler tahu nama pasti nggak null.",
                    "Makanya `nama.trim()` boleh ditulis tanpa `?.`. Ini smart cast juga.",
                    "",
                    "Lihat baris Cici. Alamatnya ada, tapi kotanya null. Rantai",
                    "`o.alamat?.kota ?: \"...\"` menangani Cici dengan kode yang persis sama",
                    "seperti Budi, yang alamatnya null. Satu rantai safe call sudah cukup,",
                    "di tingkat mana pun null-nya muncul.",
                    "",
                    "Fungsi bantu yang sering dipakai:",
                    "",
                    "  x.orEmpty()            String? -> String",
                    "  daftar.filterNotNull() List<T?> -> List<T>",
                    "  x ?: return            pulang lebih awal",
                    "  requireNotNull(x)      melempar dengan pesan jelas",
                    "  checkNotNull(x)",
                    "",
                    "`orEmpty()` mengganti null dengan string kosong. `filterNotNull()`",
                    "cuma membuang null. String kosong dan string berisi spasi tetap ikut,",
                    "makanya baris terakhir keluaran punya dua tempat kosong di antara Andi",
                    "dan Budi.",
                    "",
                    "Hati-hati dengan nilai yang datang dari pustaka Java. Tipenya platform",
                    "type, ditulis `String!`. Kotlin nggak tahu apakah nilai itu bisa null,",
                    "jadi kamu diizinkan memakainya tanpa pemeriksaan. Di situlah",
                    "NullPointerException masih bisa terjadi. Kalau sebuah nilai datang dari",
                    "Java, tulis tipenya terang-terangan sebagai `String?`, lalu periksa",
                    "sendiri.",
                ]
            },
        ],
    },
    {
        "title": "4. Fungsi",
        "sections": [
            {
                "body": [
                    "Fungsi adalah sekumpulan perintah yang diberi nama, supaya bisa",
                    "dipanggil lagi kapan aja. Di Kotlin, fungsi dibuat dengan kata kunci",
                    "fun. Fungsi di bawah menerima dua angka, lalu mengembalikan jumlahnya:",
                    "",
                    "  fun tambah(a: Int, b: Int): Int {",
                    "      return a + b",
                    "  }",
                    "",
                    "Nilai a dan b disebut parameter, yaitu nilai yang diterima fungsi.",
                    "Int yang terakhir, sesudah tanda kurung, adalah tipe kembalian: tipe",
                    "hasil yang dikembalikan lewat return.",
                    "",
                    "Kalau isi fungsinya cuma satu ekspresi, ada bentuk yang lebih pendek.",
                    "Ekspresi itu potongan kode yang menghasilkan nilai, seperti a + b.",
                    "",
                    "  fun tambah(a: Int, b: Int): Int = a + b      bentuk ekspresi",
                    "  fun tambah(a: Int, b: Int) = a + b           tipe disimpulkan",
                    "",
                    "Tipe parameter wajib ditulis. Tipe kembalian boleh disimpulkan",
                    "compiler, tapi cuma di bentuk ekspresi, yang memakai tanda sama dengan.",
                    "",
                    "Fungsi yang nggak mengembalikan apa-apa bertipe Unit, dan Unit boleh",
                    "nggak ditulis:",
                    "",
                    "  fun cetak(x: Int): Unit { println(x) }",
                    "  fun cetak(x: Int) { println(x) }              sama",
                    "",
                    "Parameter boleh punya nilai bawaan. Kalau pemanggil nggak mengisinya,",
                    "nilai bawaan itu yang dipakai. Di Java, untuk hal yang sama kamu harus",
                    "menulis beberapa versi fungsi bernama sama, yang disebut overload. Di",
                    "Kotlin, nilai bawaan menggantikan overload:",
                    "",
                    "  fun garis(isi: String, lebar: Int = 30, pengisi: Char = '-')",
                    "",
                    "  garis(\"judul\")",
                    "  garis(\"judul\", 40)",
                    "  garis(\"judul\", pengisi = '=')      lewati yang tengah",
                    "",
                    "Baris terakhir memakai argumen bernama: nama parameternya ditulis di",
                    "depan nilainya. Dengan begitu kamu bisa melewati lebar dan langsung",
                    "mengisi pengisi. Argumen bernama juga bikin pemanggilan menjelaskan",
                    "dirinya sendiri:",
                    "",
                    "  gambar(tebal = true, miring = false)",
                    "",
                    "Bandingkan dengan `gambar(true, false)`. Dari situ kamu nggak tahu true",
                    "itu untuk apa, dan kalau kedua nilainya tertukar, nggak ada error sama",
                    "sekali.",
                    "",
                    "`vararg` bikin fungsi bisa menerima argumen berapa pun banyaknya:",
                    "",
                    "  fun total(vararg angka: Int) = angka.sum()",
                    "  total(1, 2, 3)",
                    "  total(*intArrayOf(1, 2, 3))   tanda bintang membongkar",
                    "",
                    "Di dalam fungsi, angka berupa array, yaitu deretan nilai bertipe sama.",
                    "Kalau nilainya sudah ada di dalam array, tanda bintang (*) membongkar",
                    "array itu jadi argumen satu per satu. Untuk vararg bertipe Int,",
                    "array-nya harus IntArray, jadi buatnya pakai intArrayOf. Array dari",
                    "arrayOf(1, 2, 3) bertipe Array<Int>, dan compiler menolaknya di situ.",
                    "",
                    "Extension function adalah cara menambah method ke class yang bukan",
                    "milikmu, misalnya String atau Int, tanpa mengubah class aslinya. Method",
                    "itu fungsi yang menempel pada sebuah nilai dan dipanggil pakai titik,",
                    "seperti \"teks\".trim(). Caranya, tulis nama class-nya di depan nama",
                    "fungsi:",
                    "",
                    "  fun String.rapikan(): String = trim().lowercase()",
                    "  \"  HALO  \".rapikan()        -> \"halo\"",
                    "",
                    "  fun Int.kuadrat() = this * this",
                    "  5.kuadrat()                 -> 25",
                    "",
                    "Nilai yang ditempeli fungsi itu disebut penerima (receiver). Di dalam",
                    "fungsinya, this menunjuk ke penerima itu, misalnya angka 5 di",
                    "5.kuadrat().",
                    "",
                    "Fitur ini termasuk yang paling banyak dipakai di Kotlin. Di baliknya,",
                    "extension function cuma fungsi statis biasa, yaitu fungsi yang nggak",
                    "menempel pada objek mana pun. Penerimanya dioper sebagai parameter",
                    "pertama. Jadi class aslinya nggak berubah sama sekali, dan fungsi itu",
                    "nggak bisa mengakses anggota private (yang disembunyikan) milik class",
                    "tersebut.",
                    "",
                    "Akibatnya, extension function nggak polimorfik. Fungsi yang dipanggil",
                    "ditentukan oleh tipe yang tertulis di kode, dan objek aslinya nggak",
                    "ikut menentukan. Misalnya ada extension untuk Hewan dan untuk Kucing.",
                    "Variabel bertipe Hewan yang isinya Kucing tetap memanggil versi Hewan.",
                    "",
                    "Fungsi juga boleh dibuat di dalam fungsi lain. Fungsi lokal seperti",
                    "ini berguna untuk memecah fungsi yang panjang tanpa menambah fungsi",
                    "baru di level berkas.",
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
                    "Pemanggilan garis yang keempat menulis semua argumennya dengan nama,",
                    "jadi urutannya boleh bebas. Argumen vararg juga boleh kosong sama sekali:",
                    "`rataRata()` tanpa argumen menghasilkan 0.0, karena fungsinya memeriksa",
                    "`isEmpty()` lebih dulu.",
                    "",
                    "Beberapa hal lain dari contoh itu:",
                    "  - `coerceAtLeast(0)` memastikan angkanya nggak negatif. Pasangannya",
                    "    `coerceAtMost` dan `coerceIn(a, b)`. Ketiganya jauh lebih gampang",
                    "    dibaca daripada `maxOf` dan `minOf` yang bersarang.",
                    "  - `::genap` adalah referensi fungsi, cara mengoper sebuah fungsi",
                    "    sebagai nilai tanpa membungkusnya dalam lambda. Bentuk lainnya",
                    "    `String::length` dan `::println`.",
                    "  - `val (a, b) = data.partition(...)` memakai destructuring, yaitu",
                    "    memecah satu nilai jadi beberapa variabel sekaligus. Di sini",
                    "    partition menghasilkan Pair, pasangan dua nilai: daftar angka genap",
                    "    dan daftar angka ganjil. Destructuring jalan untuk Pair, Triple,",
                    "    data class, dan apa pun yang punya operator `component1`,",
                    "    `component2`, dan seterusnya.",
                    "  - Extension `List<Int>.ringkas()` memanggil `min()` dan `max()` tanpa",
                    "    menyebut penerimanya. Di dalam extension function, anggota",
                    "    penerimanya langsung bisa dipakai, seolah ada `this.` yang nggak",
                    "    ditulis.",
                ]
            },
        ],
    },
    {
        "title": "5. Kendali Alur",
        "sections": [
            {
                "body": [
                    "Kendali alur artinya mengatur bagian kode mana yang jalan: memilih",
                    "salah satu jalan (if, when), atau mengulang beberapa kali (for,",
                    "while).",
                    "",
                    "Di Kotlin, if adalah ekspresi. Artinya if menghasilkan nilai yang bisa",
                    "langsung disimpan:",
                    "",
                    "  val status = if (nilai >= 75) \"lulus\" else \"ulang\"",
                    "",
                    "Makanya Kotlin nggak punya operator ternary, yaitu bentuk",
                    "syarat ? a : b di Java. Kotlin nggak butuh, karena if sudah bisa",
                    "dipakai begitu.",
                    "",
                    "`when` menggantikan switch dari Java, dan kemampuannya jauh lebih",
                    "banyak:",
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
                    "Bentuk pertama nggak punya subjek, jadi isinya rantai kondisi yang",
                    "diperiksa dari atas. Kondisi pertama yang benar, itu yang dipakai.",
                    "Bentuk kedua mencocokkan satu nilai, yaitu x. Dalam satu blok, kamu",
                    "boleh mencampur nilai biasa, rentang (in 3..10), dan pemeriksaan tipe",
                    "(is String). Cabang else menangkap semua yang nggak cocok di atasnya.",
                    "",
                    "`when` atas sebuah enum atau sealed class nggak butuh else kalau semua",
                    "kemungkinannya sudah ditulis. Enum itu daftar nilai tetap, misalnya",
                    "empat arah mata angin. Sealed class dibahas di materi Data Class,",
                    "Object & Sealed. Compiler bahkan memaksamu melengkapi semua",
                    "kemungkinannya. Ini menolong: kalau nanti ada nilai baru, setiap when",
                    "yang belum diperbarui langsung gagal dikompilasi, jadi nggak ada yang",
                    "kelewat.",
                    "",
                    "Untuk perulangan:",
                    "",
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
                    "Rentang `1..5` berarti 1 sampai 5, termasuk 5. Kalau pakai `until`,",
                    "angka terakhirnya nggak ikut. `downTo` menghitung mundur, dan `step`",
                    "menentukan lompatannya. `withIndex()` memberi nomor urut sekaligus",
                    "isinya, dan perulangan atas peta (sebuah Map) memberi pasangan kunci",
                    "dan nilai. Perulangan while memeriksa syaratnya dulu baru jalan,",
                    "sedangkan do-while jalan sekali dulu baru memeriksa.",
                    "",
                    "Kalau perulangannya bersarang, yaitu ada perulangan di dalam",
                    "perulangan, break biasa cuma keluar dari perulangan paling dalam.",
                    "Untuk keluar dari semuanya sekaligus, kasih label:",
                    "",
                    "  luar@ for (i in 1..5) {",
                    "      for (j in 1..5) {",
                    "          if (i * j > 6) break@luar",
                    "      }",
                    "  }",
                    "",
                    "`luar@` adalah nama label yang kamu pilih sendiri, dan `break@luar`",
                    "artinya \"keluar dari perulangan bernama luar\".",
                    "",
                    "Di dalam lambda yang dioper ke fungsi seperti forEach, return biasa",
                    "keluar dari seluruh fungsi yang membungkusnya. Kalau kamu cuma mau",
                    "keluar dari lambdanya, pakai label: `return@forEach`. Alasan return",
                    "bisa begitu dibahas di materi Lambda & Higher-Order Function.",
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
                    "Urutan cabang di when itu penting. Cabang `in 1..9` harus ditulis",
                    "sebelum `is Int`. Kalau dibalik, semua bilangan bulat sudah tertangkap",
                    "cabang Int duluan, dan cabang rentangnya nggak pernah kepakai.",
                    "",
                    "Fungsi putarKanan sengaja nggak punya else. Kalau nanti enum Arah ditambah",
                    "`Arah.TENGGARA`, fungsi itu langsung gagal dikompilasi, dan compiler",
                    "menunjukkan persis tempat yang perlu diperbarui. Kalau ada else, arah",
                    "baru itu bakal tertangkap else tanpa ada yang sadar, dan bugnya baru",
                    "muncul entah kapan.",
                    "",
                    "`return@forEach` lanjut ke elemen berikutnya, dan nggak keluar dari",
                    "main. Makanya angka 3 nggak dicetak, tapi 4, 5, dan kata selesai tetap",
                    "dicetak.",
                    "",
                    "Tanpa label, return di dalam lambda keluar dari seluruh fungsi yang",
                    "membungkusnya. Perilaku ini namanya non-local return, dan cukup sering",
                    "bikin bingung.",
                    "",
                    "`0 to 0` membuat sebuah Pair, yaitu pasangan dua nilai. Fungsi infix",
                    "`to` itu juga yang dipakai untuk mengisi Map:",
                    "`mapOf(\"a\" to 1, \"b\" to 2)`. Fungsi infix artinya fungsi yang bisa",
                    "dipanggil tanpa titik dan tanpa kurung, cukup ditulis di antara dua",
                    "nilai.",
                ]
            },
        ],
    },
    {
        "title": "6. Koleksi",
        "sections": [
            {
                "body": [
                    "Koleksi adalah wadah yang menampung banyak nilai sekaligus. Tiga yang",
                    "paling sering dipakai adalah List (daftar berurutan), Set (kumpulan",
                    "tanpa isi kembar), dan Map (pasangan kunci dan nilai, seperti kamus).",
                    "",
                    "Kotlin membedakan koleksi yang hanya bisa dibaca dan koleksi yang bisa",
                    "diubah lewat tipenya:",
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
                    "Kolom kanan adalah tipe hasilnya. Array itu deretan nilai yang",
                    "panjangnya tetap, dan `emptyList` membuat list kosong.",
                    "",
                    "Aturan praktisnya: fungsi mengembalikan List dan menerima List. Pakai",
                    "MutableList cuma di dalam fungsi yang sedang membangun daftarnya.",
                    "Dengan begitu, kode lain yang menerima daftarmu nggak bisa menambah",
                    "atau menghapus isinya.",
                    "",
                    "Cara mengambil isi list:",
                    "",
                    "  daftar[0]            melempar kalau di luar batas",
                    "  daftar.getOrNull(0)  null kalau di luar batas",
                    "  daftar.getOrElse(0) { -1 }",
                    "  daftar.first() / last()        melempar kalau kosong",
                    "  daftar.firstOrNull() / lastOrNull()",
                    "  daftar.size / isEmpty() / isNotEmpty()",
                    "",
                    "Indeks dimulai dari 0, jadi `daftar[0]` adalah isi pertama.",
                    "`getOrElse` menjalankan lambda di belakangnya kalau indeksnya nggak",
                    "ada. Di contoh ini hasilnya -1.",
                    "",
                    "Untuk Map:",
                    "",
                    "  peta[\"a\"]                     null kalau tidak ada",
                    "  peta.getValue(\"a\")            melempar kalau tidak ada",
                    "  peta.getOrDefault(\"a\", 0)",
                    "  peta.getOrPut(\"a\") { 0 }      isi kalau belum ada",
                    "  peta.keys / values / entries",
                    "",
                    "`getOrPut` cuma ada di MutableMap, karena dia mengisi kunci yang",
                    "belum ada. `keys` berisi semua kunci, `values` semua nilai, dan",
                    "`entries` semua pasangannya.",
                    "",
                    "Operasi yang paling sering dipakai ada di bawah ini. Nggak ada satu pun",
                    "yang mengubah koleksi aslinya. Yang mengembalikan koleksi, seperti map,",
                    "filter, dan sorted, membuat koleksi baru. Yang lain menghasilkan satu",
                    "nilai, misalnya sum, count, dan any.",
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
                    "Nggak perlu dihafal sekarang. Yang paling dasar: map mengubah tiap",
                    "isi, filter menyaring isi yang memenuhi syarat, dan sorted",
                    "mengurutkan. Sisanya bakal ketemu sambil jalan.",
                    "",
                    "Yang mengubah koleksi aslinya punya nama yang mirip: `sort()` dan",
                    "`sorted()`, `reverse()` dan `reversed()`, `shuffle()` dan",
                    "`shuffled()`. Yang berakhiran -ed atau -d mengembalikan salinan. Yang",
                    "tanpa akhiran itu mengubah koleksinya langsung, jadi cuma bisa dipakai",
                    "pada koleksi yang bisa diubah, misalnya MutableList.",
                    "",
                    "Untuk data besar ada Sequence. `.asSequence()` bikin rantai operasinya",
                    "malas (lazy): tiap isi diproses lewat semua langkah satu per satu, dan",
                    "nggak ada koleksi perantara yang dibuat di tiap langkah.",
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
                    "`groupBy` menghasilkan Map yang kuncinya kelas dan nilainya daftar",
                    "murid di kelas itu. `toSortedMap()` mengurutkan kuncinya, jadi kelas A",
                    "dicetak sebelum kelas B. `partition` memecah daftar jadi dua: yang",
                    "memenuhi syarat dan yang nggak.",
                    "",
                    "`groupingBy { it }.eachCount()` adalah cara paling ringkas menghitung",
                    "frekuensi, yaitu berapa kali tiap kata muncul. Bedanya dari groupBy:",
                    "groupingBy nggak membuat List perantara untuk tiap kelompok. Dia cuma",
                    "menghitung.",
                    "",
                    "`compareByDescending { ... }.thenBy { ... }` menyusun pembanding dua",
                    "tingkat. Di contoh tadi, kata diurutkan dari yang paling sering muncul.",
                    "Kalau jumlahnya sama, seperti makan dan tidur, urutannya ditentukan",
                    "abjad. Bentuk ini sering dipakai kalau urutannya harus pasti, dan",
                    "urutan yang pasti itu yang bikin keluaran bisa diuji.",
                    "",
                    "`it` adalah nama bawaan untuk parameter tunggal sebuah lambda. Kalau",
                    "lambdanya bersarang, kasih nama sendiri supaya nggak membingungkan:",
                    "`{ murid -> ... }`.",
                ]
            },
        ],
    },
    {
        "title": "7. Class, Properti & Constructor",
        "sections": [
            {
                "body": [
                    "Class adalah cetakan untuk membuat objek. Misalnya class Murid",
                    "menjelaskan bahwa tiap murid punya nama dan nilai. Andi dan Budi adalah",
                    "dua objek yang dibuat dari cetakan itu. Di Kotlin, class sederhana",
                    "cukup ditulis satu baris:",
                    "",
                    "  class Murid(val nama: String, var nilai: Int)",
                    "",
                    "Satu baris itu sudah menghasilkan class dengan dua properti (variabel",
                    "milik objek), sebuah constructor (bagian yang jalan waktu objek",
                    "dibuat), getter untuk keduanya, dan setter untuk `nilai`. Getter itu",
                    "fungsi untuk membaca properti, setter untuk mengubahnya. Di Java,",
                    "padanannya sekitar 25 baris.",
                    "",
                    "Bagian dalam kurung di belakang nama class disebut primary constructor",
                    "(constructor utama). Parameter yang diawali `val` atau `var` otomatis",
                    "jadi properti. Parameter tanpa keduanya cuma parameter biasa, yang",
                    "hanya bisa dipakai waktu objeknya dibuat:",
                    "",
                    "  class Murid(val nama: String, nilaiAwal: Int) {",
                    "      var nilai = nilaiAwal        // nilaiAwal cuma parameter",
                    "  }",
                    "",
                    "Blok `init` jalan waktu objek dibuat. Biasanya dipakai untuk memeriksa",
                    "nilai awal:",
                    "",
                    "  init {",
                    "      require(nilai in 0..100) { \"nilai di luar 0..100\" }",
                    "  }",
                    "",
                    "`require` melempar error kalau syaratnya nggak terpenuhi, jadi objek",
                    "dengan nilai 150 nggak pernah jadi.",
                    "",
                    "Kalau butuh cara lain untuk membuat objek, ada secondary constructor",
                    "(constructor tambahan):",
                    "",
                    "  constructor(nama: String) : this(nama, 0)",
                    "",
                    "Artinya, kalau objek dibuat cuma dengan nama, constructor utama",
                    "dipanggil dengan nilai 0. Dalam praktiknya ini jarang dipakai, karena",
                    "nilai bawaan parameter biasanya lebih praktis.",
                    "",
                    "Properti juga boleh punya getter dan setter buatan sendiri:",
                    "",
                    "  var nilai: Int = 0",
                    "      set(baru) {",
                    "          require(baru in 0..100)",
                    "          field = baru          // `field` = backing field",
                    "      }",
                    "",
                    "  val grade: String                 // properti terhitung",
                    "      get() = when { nilai >= 85 -> \"A\"; else -> \"B\" }",
                    "",
                    "Setter di atas jalan tiap kali nilai diubah, dan menolak angka di luar",
                    "0 sampai 100. Properti grade disebut properti terhitung: dia nggak",
                    "menyimpan apa pun, dan nilainya dihitung ulang tiap kali dibaca.",
                    "",
                    "Kata `field` artinya tempat penyimpanan asli properti itu, yang",
                    "disebut backing field. Kata ini cuma boleh dipakai di dalam getter atau",
                    "setter (disebut juga accessor). Di dalam setter, tulis `field = baru`, jangan",
                    "`nilai = baru`. Bentuk kedua memanggil setter itu sendiri, lalu setter",
                    "memanggil dirinya lagi terus-menerus (rekursi tak berujung) sampai",
                    "program berhenti dengan StackOverflowError.",
                    "",
                    "Visibilitas menentukan siapa yang boleh memakai sebuah class, fungsi,",
                    "atau properti:",
                    "",
                    "  public     bawaan",
                    "  internal   terlihat di seluruh modul yang sama",
                    "  protected  class ini dan turunannya",
                    "  private    berkas atau class ini saja",
                    "",
                    "Kalau nggak ditulis apa-apa, artinya public, jadi semua kode boleh",
                    "memakai. Modul itu sekumpulan berkas Kotlin yang dikompilasi bareng,",
                    "misalnya satu proyek. `internal` nggak ada di Java. Gunanya untuk",
                    "sesuatu yang boleh dipakai di seluruh pustakamu sendiri, tapi nggak",
                    "untuk orang yang memakai pustakamu.",
                    "",
                    "`lateinit` dipakai untuk properti yang baru diisi belakangan:",
                    "",
                    "  lateinit var db: Database",
                    "",
                    "Tanpa lateinit, properti seperti ini harus dibuat nullable (boleh",
                    "null), padahal kamu tahu dia pasti terisi sebelum dipakai. Kalau",
                    "ternyata kamu mengaksesnya sebelum terisi, program melempar",
                    "UninitializedPropertyAccessException. Pesan itu jauh lebih jelas",
                    "daripada NullPointerException.",
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
                    "Empat hal dari contoh itu yang layak ditiru:",
                    "  1. `var saldo: Long = saldoAwal` dengan `private set`. Kode di luar",
                    "     class boleh membaca saldo, tapi yang boleh mengubahnya cuma class",
                    "     ini sendiri, lewat setor dan tarik yang sudah memeriksa",
                    "     jumlahnya. Di Kotlin ini cukup satu baris. Di Java kamu butuh",
                    "     field private ditambah getter.",
                    "  2. `require(...) { \"pesan\" }` melempar IllegalArgumentException.",
                    "     Pesannya cuma dihitung kalau syaratnya gagal. Saudaranya `check`",
                    "     (melempar IllegalStateException) dan `error(\"...\")`.",
                    "  3. `companion object` adalah tempat anggota statis di Kotlin, yaitu",
                    "     anggota milik class itu sendiri, dan nggak menempel pada objek",
                    "     mana pun. Kotlin nggak punya kata kunci static. Penggantinya objek",
                    "     pendamping yang menempel pada class, jadi kamu bisa memanggil",
                    "     `Rekening.buatBanyak(...)` tanpa membuat objek Rekening dulu.",
                    "  4. `setor` mengembalikan `this`, jadi pemanggilannya bisa dirantai,",
                    "     misalnya `a.setor(1).setor(2)`. Pola ini lazim untuk builder,",
                    "     yaitu objek yang dipakai untuk merakit objek lain langkah demi",
                    "     langkah.",
                    "",
                    "Baris terakhir keluaran berasal dari require di blok init. Pemilik yang",
                    "isinya spasi semua ditolak, jadi objek Rekening itu nggak pernah jadi.",
                    "",
                    "Lihat juga properti nomor. Dia ditulis `val` tanpa nilai, lalu diisi",
                    "di dalam `init`. Compiler memeriksa bahwa setiap jalur pasti mengisinya",
                    "tepat sekali. Kalau ada cabang yang lupa mengisinya, kodenya nggak bisa",
                    "dikompilasi.",
                ]
            },
        ],
    },
    {
        "title": "8. Data Class, Object & Sealed",
        "sections": [
            {
                "body": [
                    "Data class adalah class yang tugasnya cuma menyimpan data, misalnya",
                    "data sebuah produk. Cukup satu baris:",
                    "",
                    "  data class Produk(val nama: String, val harga: Long)",
                    "",
                    "Dari satu baris itu, compiler membuatkan beberapa fungsi sekaligus:",
                    "",
                    "  equals() dan hashCode() berbasis nilai",
                    "  toString() yang enak dibaca",
                    "  copy() untuk menyalin sambil mengubah sebagian",
                    "  componentN() sehingga bisa di-destructure",
                    "",
                    "`equals()` dipakai untuk membandingkan dua objek. Berbasis nilai",
                    "artinya dua Produk dianggap sama kalau semua isinya sama. `hashCode()`",
                    "adalah angka ringkasan isi objek, dipakai Set dan Map untuk mencari",
                    "dengan cepat. `componentN()` memungkinkan destructuring, yaitu memecah",
                    "objek jadi beberapa variabel sekaligus:",
                    "",
                    "  val a = Produk(\"Kopi\", 25_000)",
                    "  val b = a.copy(harga = 27_000)",
                    "  val (nama, harga) = a",
                    "",
                    "Garis bawah di 25_000 cuma pemisah supaya angkanya gampang dibaca.",
                    "Variabel b adalah salinan a dengan harga baru. Baris ketiga mengisi",
                    "nama dengan \"Kopi\" dan harga dengan 25000.",
                    "",
                    "Jebakan: yang dipakai equals, hashCode, dan toString cuma properti di",
                    "primary constructor. Properti yang ditulis di badan class nggak ikut.",
                    "",
                    "Kata kunci `object` membuat singleton, yaitu class yang cuma punya satu",
                    "objek di seluruh program:",
                    "",
                    "  object Konfigurasi {",
                    "      val versi = \"1.0\"",
                    "      fun muat() { ... }",
                    "  }",
                    "  Konfigurasi.versi",
                    "",
                    "Objek itu dibuat sekali, dan baru dibuat waktu pertama kali dipakai.",
                    "Dia juga aman walaupun diakses beberapa thread (bagian program yang",
                    "jalan bersamaan) sekaligus. Semua itu tanpa satu baris pun kode",
                    "penguncian yang harus kamu tulis.",
                    "",
                    "Companion object adalah object yang menempel pada sebuah class, dan",
                    "jadi pengganti static di Kotlin. Anggotanya dipanggil lewat nama class,",
                    "tanpa membuat objek dulu:",
                    "",
                    "  class Murid private constructor(val nama: String) {",
                    "      companion object {",
                    "          fun buat(nama: String) = Murid(nama.trim())",
                    "      }",
                    "  }",
                    "",
                    "Di contoh ini constructor-nya private, jadi dari luar, Murid cuma bisa",
                    "dibuat lewat `Murid.buat(\"...\")`. Fungsi buat sekalian merapikan",
                    "namanya dengan `trim()`.",
                    "",
                    "Sealed class adalah hierarki tertutup: daftar turunannya sudah pasti",
                    "dan nggak bisa ditambah dari luar. Turunan itu class yang mewarisi",
                    "class lain. Pewarisan dibahas di materi Pewarisan & Interface.",
                    "",
                    "  sealed class Hasil",
                    "  data class Sukses(val data: String) : Hasil()",
                    "  data class Gagal(val pesan: String) : Hasil()",
                    "  object Memuat : Hasil()",
                    "",
                    "Semua turunannya harus ada di modul yang sama, jadi compiler tahu",
                    "daftarnya lengkap. Akibatnya `when` atas sealed class nggak butuh",
                    "else, dan menambah turunan baru langsung bikin setiap `when` yang",
                    "belum diperbarui gagal dikompilasi.",
                    "",
                    "Ini padanan enum berdata di Rust. Kalau kamu mau bilang \"hasilnya",
                    "pasti salah satu dari ini, nggak ada yang lain\", sealed class adalah",
                    "cara paling rapi untuk menyatakannya.",
                    "",
                    "Enum class dipakai untuk daftar nilai tetap yang nggak membawa data",
                    "berbeda-beda:",
                    "",
                    "  enum class Status(val label: String) {",
                    "      DRAF(\"Konsep\"), TERBIT(\"Sudah terbit\");",
                    "      fun bisaDisunting() = this == DRAF",
                    "  }",
                    "",
                    "Bedanya dengan sealed class: tiap nilai enum cuma ada satu, dan",
                    "bentuknya sama semua. Turunan sealed class boleh membawa data yang",
                    "beda-beda, seperti Sukses yang membawa data dan Gagal yang membawa",
                    "pesan.",
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
                    "Di contoh ini, Sukses, Gagal, dan Memuat ditulis di dalam Hasil, jadi",
                    "namanya dipanggil Hasil.Sukses, Hasil.Gagal, dan Hasil.Memuat. Tempat",
                    "penyimpanan produknya dibuat dengan object, jadi cuma ada satu di",
                    "seluruh program, dan fungsinya dipanggil langsung lewat namanya,",
                    "misalnya `Katalog.tambah(kopi)`.",
                    "",
                    "Lihat baris asli dan naik: properti mahal nggak muncul di toString.",
                    "Alasannya, mahal adalah properti terhitung di badan class. Yang ikut ke",
                    "equals, hashCode, toString, dan copy cuma properti di primary",
                    "constructor.",
                    "",
                    "`==` membandingkan nilai (memanggil equals), sedangkan `===` memeriksa",
                    "apakah dua-duanya objek yang persis sama. Makanya \"sama nilainya?\"",
                    "mencetak true, tapi \"sama objeknya?\" mencetak false: isinya sama, tapi",
                    "keduanya objek yang dibuat terpisah. Ini kebalikan dari Java. Di Java,",
                    "`==` justru membandingkan referensi (alamat objek), dan kamu harus",
                    "ingat memanggil `.equals()`.",
                    "",
                    "`Hasil<out T>` memakai kata out. T di sini tipe isinya. Artinya",
                    "`Hasil<Produk>` boleh dipakai di tempat yang menerima `Hasil<Any>`, dan",
                    "Any adalah induk semua tipe yang nggak boleh null. Berkat out, Gagal",
                    "bisa bertipe `Hasil<Nothing>` dan tetap cocok di mana pun.",
                    "",
                    "`Nothing` adalah tipe yang nggak punya satu nilai pun. Nothing dianggap",
                    "turunan dari semua tipe, makanya cocok dipakai di situasi seperti",
                    "Gagal tadi. Nothing juga dipakai sebagai tipe kembalian fungsi yang",
                    "nggak pernah selesai dengan normal, misalnya fungsi yang selalu",
                    "melempar error.",
                    "",
                    "`data object` (ada sejak Kotlin 1.9) memberi toString yang enak dibaca",
                    "untuk singleton di dalam hierarki sealed class, seperti Memuat.",
                ]
            },
        ],
    },
    {
        "title": "9. Pewarisan & Interface",
        "sections": [
            {
                "body": [
                    "Pewarisan artinya membuat class baru dari class yang sudah ada. Class",
                    "baru itu (turunan) otomatis punya semua isi class lama (induk), lalu",
                    "boleh menambah atau mengganti sebagian. Misalnya Kucing adalah turunan",
                    "Hewan.",
                    "",
                    "Di Kotlin, class tertutup untuk pewarisan secara bawaan. Supaya bisa",
                    "diturunkan, tulis `open`:",
                    "",
                    "  open class Hewan(val nama: String) {",
                    "      open fun suara(): String = \"...\"",
                    "  }",
                    "",
                    "  class Kucing(nama: String) : Hewan(nama) {",
                    "      override fun suara() = \"Meong\"",
                    "  }",
                    "",
                    "Ini kebalikan dari Java, dan perancang Kotlin menjelaskan alasannya",
                    "secara terbuka. Class yang bisa diturunkan adalah janji publik kepada",
                    "pemakainya, jadi harus dirancang dengan sengaja, jangan sampai terjadi",
                    "karena kebetulan. Kalau sebuah class nggak dirancang untuk diturunkan,",
                    "turunannya bisa merusak anggapan di dalam class itu tanpa kamu tahu.",
                    "",
                    "Kata `override` (menimpa, yaitu mengganti method milik induk) wajib",
                    "ditulis. Tanpa override, kodenya nggak bisa dikompilasi. Jadi nggak",
                    "mungkin ada method yang nggak sengaja menimpa method induknya.",
                    "",
                    "Constructor induk dipanggil di daftar supertype, yaitu bagian sesudah",
                    "titik dua yang menyebut induk dan interface sebuah class:",
                    "",
                    "  class Kucing(nama: String) : Hewan(nama)",
                    "",
                    "Di sini nama milik Kucing diteruskan ke constructor Hewan.",
                    "",
                    "Class abstract nggak bisa dibuat objeknya langsung, dan boleh punya",
                    "anggota tanpa isi yang wajib diisi turunannya. Class abstract otomatis",
                    "open, jadi nggak perlu ditulis open lagi.",
                    "",
                    "Interface adalah daftar kemampuan yang dijanjikan sebuah class.",
                    "Interface boleh punya fungsi yang sudah ada isinya (implementasi",
                    "bawaan) dan properti abstrak, tapi nggak bisa menyimpan keadaan, yaitu",
                    "nilai yang disimpan di dalam objek:",
                    "",
                    "  interface BisaDiringkas {",
                    "      val nama: String              // abstrak",
                    "      fun luas(): Double            // abstrak",
                    "      fun ringkas(): String =       // ada badannya",
                    "          \"%-16s%8.2f\".format(nama, luas())",
                    "  }",
                    "",
                    "Class yang memakai interface ini wajib mengisi nama dan `luas()`, dan",
                    "boleh langsung memakai `ringkas()` apa adanya.",
                    "",
                    "Satu class boleh mengimplementasi, yaitu memenuhi janji, banyak",
                    "interface sekaligus. Induknya cuma boleh satu. Kalau dua interface",
                    "punya method bernama sama yang sama-sama ada isinya, kamu wajib",
                    "memilih sendiri yang mana:",
                    "",
                    "  override fun f() = super<A>.f()",
                    "",
                    "Bentuk `super<A>.f()` artinya \"pakai versi f milik interface A\".",
                    "",
                    "Delegasi dengan `by` bisa menggantikan pewarisan. Delegasi artinya",
                    "menyerahkan pekerjaan ke objek lain:",
                    "",
                    "  class Pencatat(dasar: List<Int>) : List<Int> by dasar",
                    "",
                    "Satu kata by membuat semua method List diteruskan ke dasar, dan kamu",
                    "tinggal menimpa yang perlu aja. Di Java, pola delegasi yang sama butuh",
                    "puluhan method penerus yang ditulis satu per satu.",
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
                    "Class Galeri adalah contoh delegasi yang nggak bisa ditulis sesingkat",
                    "ini di Java. Frasa `: List<BangunDasar> by isi` meneruskan semua method",
                    "List ke isi: size, get, iterator, contains, indexOf, subList, dan",
                    "sisanya. Yang ditulis sendiri cuma totalLuas dan toString.",
                    "",
                    "Kenapa nggak `class Galeri : ArrayList` aja? Dengan pewarisan, Galeri",
                    "ikut mewarisi method yang mengubah isi, seperti add, remove, dan clear,",
                    "padahal mungkin kamu nggak mau Galeri bisa diubah. Dengan delegasi,",
                    "kamu yang memilih kemampuan apa yang ditunjukkan ke luar.",
                    "",
                    "Tipe parameternya `List<BangunDasar>`, dan itu disengaja. Kalau ditulis",
                    "`List<Bangun>`, kodenya nggak bisa dikompilasi. Anggota apa yang bisa",
                    "dipanggil pada `galeri[0]` ditentukan oleh tipe yang tertulis, dan",
                    "objek aslinya nggak ikut menentukan. Dengan `List<Bangun>`, properti",
                    "warna dari interface Berwarna nggak kelihatan sama sekali. Pesan",
                    "errornya juga nggak bilang \"nggak punya warna\". Yang muncul adalah",
                    "\"unresolved reference\" (nama itu nggak dikenal), yang kedengarannya",
                    "seperti salah ketik.",
                    "",
                    "Mengubah warna `galeri[0]` nggak memengaruhi `galeri[1]`, karena tiap",
                    "objek menyimpan warnanya sendiri. Nilai awalnya \"hitam\".",
                    "",
                    "Lingkaran menimpa `ringkas()`, tapi tetap memakai versi bawaannya",
                    "lewat `super.ringkas()`, lalu menambahkan jari-jarinya di belakang.",
                    "",
                    "`b is Lingkaran` melakukan smart cast. Di dalam cabang itu, b otomatis",
                    "dianggap bertipe Lingkaran tanpa perlu diubah tipenya secara manual",
                    "(cast). Di Java, pola yang sama butuh instanceof lalu cast manual, jadi",
                    "tipenya disebut dua kali.",
                    "",
                    "`override var warna` di dalam abstract class mengisi properti abstrak",
                    "milik interface. Interface boleh mengumumkan properti, tapi nggak boleh",
                    "menyimpan nilainya. Yang menyimpan harus class.",
                ]
            },
        ],
    },
    {
        "title": "10. Lambda & Higher-Order Function",
        "sections": [
            {
                "body": [
                    "Lambda adalah fungsi tanpa nama yang kamu tulis langsung di tempat ia",
                    "dipakai. Bentuknya potongan kode di dalam kurung kurawal:",
                    "",
                    "  val tambah: (Int, Int) -> Int = { a, b -> a + b }",
                    "  val kuadrat = { x: Int -> x * x }",
                    "  val cetak: (String) -> Unit = { println(it) }",
                    "",
                    "Di dalam kurung kurawal, yang di kiri tanda panah adalah parameternya,",
                    "dan yang di kanan adalah isinya. Kalau parameternya cuma satu, namanya",
                    "boleh dihilangkan. Kotlin otomatis menamainya `it`, seperti di lambda",
                    "`cetak`.",
                    "",
                    "Tipe sebuah fungsi ditulis `(A, B) -> C`. Artinya fungsi itu menerima",
                    "dua parameter bertipe A dan B, lalu menghasilkan C. Tipe fungsi",
                    "diperlakukan sama seperti tipe lain, istilahnya tipe kelas satu. Jadi",
                    "fungsi boleh jadi parameter, jadi nilai kembalian, atau disimpan di",
                    "dalam koleksi.",
                    "",
                    "Fungsi yang menerima atau mengembalikan fungsi lain disebut higher-order",
                    "function. Contohnya `saring`, yang menerima fungsi `syarat`:",
                    "",
                    "  fun saring(data: List<Int>, syarat: (Int) -> Boolean) =",
                    "      data.filter(syarat)",
                    "",
                    "Ada satu aturan yang bikin kode Kotlin kelihatan khas. Kalau parameter",
                    "terakhir sebuah fungsi bertipe fungsi, lambdanya boleh ditulis di luar",
                    "tanda kurung:",
                    "",
                    "  saring(data) { it > 5 }          alih-alih",
                    "  saring(data, { it > 5 })",
                    "",
                    "Berkat aturan ini, `repeat`, `forEach`, `with`, `apply`, dan semua DSL",
                    "Kotlin kelihatan seperti sintaks bawaan bahasa. Padahal semuanya fungsi",
                    "biasa. DSL adalah kode yang dibentuk mirip bahasa kecil untuk satu",
                    "keperluan, misalnya isi berkas build.gradle.kts.",
                    "",
                    "Kalau fungsinya sudah ada, kamu nggak perlu membungkusnya dengan lambda.",
                    "Oper aja referensi fungsinya, yang ditandai `::`. Cara ini menyebut",
                    "sebuah fungsi sebagai nilai, tanpa memanggilnya:",
                    "",
                    "  data.filter(::genap)",
                    "  data.map(String::length)",
                    "  data.forEach(::println)",
                    "",
                    "Kotlin juga punya lima scope function yang khas. Scope function",
                    "menjalankan satu blok kode dengan sebuah objek sebagai pusatnya. Objek",
                    "itu disebut penerima. Di `x.let { }`, penerimanya `x`.",
                    "",
                    "  let     x.let { it }      -> hasil lambda",
                    "  run     x.run { this }    -> hasil lambda",
                    "  with    with(x) { this }  -> hasil lambda",
                    "  apply   x.apply { this }  -> X sendiri",
                    "  also    x.also { it }     -> X sendiri",
                    "",
                    "Bedanya ada di dua kolom itu. Pertama, nama penerimanya di dalam blok:",
                    "`it` atau `this`. Kedua, apa yang dikembalikan: hasil lambdanya, atau",
                    "objek X itu sendiri.",
                    "",
                    "Kapan pakai yang mana? Versi praktisnya begini:",
                    "",
                    "  let    jalankan blok kalau bukan null, atau ubah bentuk",
                    "  apply  setel banyak properti lalu kembalikan objeknya",
                    "  also   selipkan efek samping (log) tanpa mengubah rantai",
                    "  run    hitung sesuatu dari sebuah objek",
                    "  with   panggil banyak method pada satu objek",
                    "",
                    "Efek samping di tabel itu artinya pekerjaan tambahan di luar menghitung",
                    "hasil, misalnya mencetak log.",
                    "",
                    "Jangan memaksakan semuanya. Kalau sebuah `let` malah bikin kodenya lebih",
                    "susah dibaca, pakai variabel biasa.",
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
                    "`pengali(3)` mengembalikan fungsi yang mengingat angka 3. Fungsi seperti",
                    "ini disebut closure. Lambdanya menangkap variabel dari tempat ia dibuat,",
                    "dan variabel itu tetap hidup selama lambdanya masih hidup. Di contoh",
                    "tadi, `faktor` tetap bernilai 3 walaupun `pengali` sudah lama selesai.",
                    "",
                    "`also` menyelipkan efek samping di tengah rantai tanpa memutusnya. Di",
                    "contoh tadi, `also` mencetak jumlah elemen sesudah `filter`, lalu",
                    "rantainya lanjut ke `map`. Kalau sebuah rantai menghasilkan data yang",
                    "salah, cara ini jauh lebih enak untuk ngecek tiap langkah. Kamu nggak",
                    "perlu memecah rantainya jadi beberapa variabel sementara.",
                    "",
                    "Sekarang soal ongkosnya. Tanpa `inline`, lambda yang kamu oper ke sebuah",
                    "fungsi dibuat jadi objek dulu. Fungsi yang ditandai `inline` menghindari",
                    "itu. Waktu kompilasi, badan fungsinya disalin ke tempat ia dipanggil,",
                    "jadi nggak ada objek lambda yang dibuat sama sekali:",
                    "",
                    "  inline fun <T> ukur(blok: () -> T): T { ... }",
                    "",
                    "Karena itu higher-order function di Kotlin bisa dibilang gratis. Semua",
                    "fungsi koleksi standar, seperti `filter`, `map`, dan `forEach`, sudah",
                    "`inline`. Jadi lambda di situ nggak menambah ongkos dibanding perulangan",
                    "yang kamu tulis sendiri.",
                    "",
                    "Tapi tiap langkah di sebuah rantai tetap bikin list baru. `filter` lalu",
                    "`map` berarti dua list. Untuk data besar, pakai Sequence (lihat materi",
                    "Koleksi) supaya list perantara itu nggak dibuat.",
                    "",
                    "`inline` juga yang memungkinkan return non-lokal, yaitu `return` di",
                    "dalam lambda yang langsung keluar dari fungsi pembungkusnya. Contohnya",
                    "`return` di dalam `forEach`. Ini bisa terjadi karena badan lambdanya",
                    "memang tersalin ke dalam fungsi itu.",
                ]
            },
        ],
    },
    {
        "title": "11. Generic & Extension Lanjut",
        "sections": [
            {
                "body": [
                    "Generic membuat satu kode bisa dipakai untuk banyak tipe. Huruf `T` di",
                    "contoh ini cuma nama sementara untuk sebuah tipe. Tipe aslinya baru",
                    "ditentukan waktu kode itu dipakai, misalnya `Kotak<Int>` atau",
                    "`Kotak<String>`:",
                    "",
                    "  class Kotak<T>(private val isi: MutableList<T> = mutableListOf())",
                    "  fun <T> pertama(daftar: List<T>): T? = daftar.firstOrNull()",
                    "",
                    "Kadang T nggak boleh sembarang tipe. Fungsi `terbesar` misalnya perlu",
                    "membandingkan dua nilai, jadi T harus tipe yang bisa dibandingkan.",
                    "`Comparable<T>` artinya bisa dibandingkan dengan T lain. Batasan seperti",
                    "itu ditulis pakai titik dua:",
                    "",
                    "  fun <T : Comparable<T>> terbesar(a: T, b: T) =",
                    "      if (a > b) a else b",
                    "",
                    "Untuk lebih dari satu batasan, pakai `where`:",
                    "  fun <T> proses(x: T) where T : Comparable<T>, T : Cloneable",
                    "",
                    "Bagian yang paling sering bikin bingung adalah variansi. Variansi",
                    "menjawab pertanyaan ini: kapan `List<Kucing>` boleh dipakai di tempat",
                    "yang meminta `List<Hewan>`? Kotlin menandainya dengan dua kata:",
                    "  - `out T` artinya produsen. Tipe itu cuma mengeluarkan T dan nggak",
                    "    pernah menerima T. Contohnya `List<Kucing>` boleh dipakai sebagai",
                    "    `List<Hewan>`.",
                    "  - `in T` artinya konsumen. Tipe itu cuma menerima T dan nggak pernah",
                    "    mengeluarkannya. Contohnya `Comparator<Hewan>` boleh dipakai sebagai",
                    "    `Comparator<Kucing>`.",
                    "",
                    "Comparator adalah objek yang tahu cara membandingkan dua nilai, misalnya",
                    "untuk mengurutkan. Comparator yang bisa membandingkan dua hewan apa pun",
                    "pasti bisa membandingkan dua kucing.",
                    "",
                    "Cara mengingatnya: `out` untuk yang keluar, `in` untuk yang masuk.",
                    "`List<out T>` aman diperlebar karena List nggak punya cara untuk",
                    "menerima elemen baru. Jadi nggak ada cara menyisipkan Anjing ke dalam",
                    "`List<Kucing>` yang sedang dipandang sebagai `List<Hewan>`.",
                    "",
                    "Masalah berikutnya ada di JVM. Di sana informasi tipe generic dihapus",
                    "waktu kompilasi, istilahnya type erasure. Waktu program jalan,",
                    "`List<Int>` dan `List<String>` kelihatan sama. Akibatnya `T::class`",
                    "biasanya mustahil.",
                    "",
                    "Kata `reified` mengatasinya, jadi kamu bisa tahu tipe generic waktu",
                    "program jalan:",
                    "",
                    "  inline fun <reified T> saringTipe(daftar: List<Any>) =",
                    "      daftar.filterIsInstance<T>()",
                    "",
                    "Caranya, badan fungsi disalin ke tempat pemanggilan, dan di sana tipenya",
                    "masih diketahui. Karena itu `reified` cuma bisa dipakai bersama",
                    "`inline`.",
                    "",
                    "Extension property adalah pasangan extension function, yaitu properti",
                    "yang kamu tempelkan ke class milik orang lain:",
                    "  val String.hurufSaja: String",
                    "      get() = filter { it.isLetter() }",
                    "",
                    "Extension property nggak menyimpan apa pun, karena nggak ada tempat",
                    "untuk menyimpannya di class yang bukan milikmu. Makanya dia wajib punya",
                    "getter, yaitu fungsi kecil yang menghitung nilainya setiap kali properti",
                    "itu dibaca.",
                    "",
                    "Extension juga bisa ditempelkan ke tipe nullable, yaitu tipe yang boleh",
                    "berisi null:",
                    "  fun String?.atauKosong(): String = this ?: \"\"",
                    "",
                    "Di dalam fungsi itu `this` boleh null, dan itu sah. Fungsi",
                    "`isNullOrBlank()` di pustaka standar bekerja dengan cara yang sama.",
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
                    "`semuaNama(kucing)` jalan, padahal parameternya bertipe `List<Hewan>`",
                    "dan yang dioper `List<Kucing>`. Alasannya, `List<out E>` di Kotlin",
                    "memang dideklarasikan sebagai produsen. List itu nggak punya `add`, jadi",
                    "nggak ada cara menyelipkan Anjing ke dalamnya.",
                    "",
                    "Lain ceritanya dengan `MutableList`, yang punya `add`. Kalau parameter",
                    "`semuaNama` bertipe `MutableList<Hewan>`, mengoper `MutableList<Kucing>`",
                    "bakal ditolak compiler. Penolakan itu benar. Kalau lolos, fungsi itu",
                    "bisa menambahkan Anjing ke daftar kucingmu.",
                    "",
                    "`saringTipe<Int>(campur)` bisa memeriksa tipe T waktu program jalan cuma",
                    "karena ada `reified` dan `inline`. Tanpa keduanya, `T::class` dan `is T`",
                    "jadi error kompilasi, karena JVM sudah menghapus informasi tipenya.",
                    "",
                    "`null.ringkas()` memanggil fungsi pada null, dan itu sah karena",
                    "penerimanya bertipe `String?`. Di dalam fungsi itu, `this` boleh null",
                    "dan harus diperiksa dulu. Mekanismenya sama dengan `isNullOrBlank()` di",
                    "pustaka standar.",
                    "",
                    "Lihat juga `removeFirstOrNull()` dan `maxOrNull()`. Pustaka standar",
                    "Kotlin konsisten menyediakan pasangan seperti ini. `xxx()` melempar",
                    "exception kalau gagal, jadi program berhenti dengan error kecuali",
                    "exception itu ditangkap. `xxxOrNull()` mengembalikan null. Memilih salah",
                    "satunya adalah keputusan desain, jadi pilih dengan sengaja.",
                ]
            },
        ],
    },
    {
        "title": "12. Exception & Penanganan Galat",
        "sections": [
            {
                "body": [
                    "Exception adalah error yang muncul waktu program jalan. Contohnya teks",
                    "\"abc\" yang mau diubah jadi angka. Waktu itu terjadi, program melempar",
                    "exception. Kalau nggak ada yang menangkapnya, program berhenti.",
                    "",
                    "Untuk menangkapnya, pakai `try` dan `catch`:",
                    "",
                    "  try {",
                    "      ...",
                    "  } catch (e: NumberFormatException) {",
                    "      ...",
                    "  } catch (e: Exception) {",
                    "      ...",
                    "  } finally {",
                    "      ...            selalu dijalankan",
                    "  }",
                    "",
                    "Kode yang mungkin gagal ditulis di dalam `try`. Kalau gagal, blok",
                    "`catch` pertama yang tipenya cocok yang dijalankan. Blok `finally`",
                    "selalu dijalankan, entah ada error atau nggak.",
                    "",
                    "`try` di Kotlin adalah ekspresi, jadi dia menghasilkan nilai:",
                    "",
                    "  val n = try { teks.toInt() } catch (e: Exception) { 0 }",
                    "",
                    "Kalau `toInt()` berhasil, `n` berisi angkanya. Kalau gagal, `n` jadi 0.",
                    "",
                    "Ada perbedaan besar dari Java: Kotlin nggak punya checked exception. Di",
                    "Java, checked exception wajib kamu tangkap, atau kamu umumkan lewat",
                    "`throws` di tanda tangan fungsi. Tanda tangan fungsi itu baris",
                    "pertamanya, yang memuat nama, parameter, dan tipe kembalian. Kalau nggak",
                    "ditangani, kode Java-nya nggak bisa dikompilasi.",
                    "",
                    "Di Kotlin nggak ada `throws` di tanda tangan fungsi. Compiler juga nggak",
                    "pernah memaksamu membungkus sesuatu dengan try-catch.",
                    "",
                    "Alasannya dijelaskan sendiri oleh perancang Kotlin. Di proyek besar,",
                    "checked exception hampir selalu berakhir jadi `catch (e: Exception) { }`",
                    "yang kosong. Itu malah lebih buruk daripada membiarkan exception-nya",
                    "naik ke fungsi pemanggil. Yang hilang di Kotlin cuma paksaannya.",
                    "Tanggung jawab menangani error tetap ada di kamu.",
                    "",
                    "Cara melempar exception:",
                    "  throw IllegalArgumentException(\"pesan\")",
                    "  require(syarat) { \"pesan\" }      -> IllegalArgumentException",
                    "  check(syarat) { \"pesan\" }        -> IllegalStateException",
                    "  error(\"pesan\")                   -> IllegalStateException",
                    "  requireNotNull(x) { \"pesan\" }",
                    "  checkNotNull(x) { \"pesan\" }",
                    "  TODO(\"belum dibuat\")             -> NotImplementedError",
                    "",
                    "Pakai `require` untuk memeriksa argumen, dan `check` untuk memeriksa",
                    "keadaan objeknya. Dua-duanya cuma menyusun pesannya kalau syaratnya",
                    "gagal.",
                    "",
                    "`throw` juga ekspresi, dan tipenya `Nothing`. Karena itu `throw` bisa",
                    "ditaruh di sisi kanan operator Elvis (`?:`):",
                    "  val n = cari() ?: throw IllegalStateException(\"tidak ada\")",
                    "",
                    "Untuk API, yaitu fungsi yang kamu sediakan untuk dipakai kode lain, ada",
                    "alternatif yang lebih aman: Result. Result adalah wadah yang isinya",
                    "salah satu dari dua: nilai kalau berhasil, atau exception yang",
                    "tertangkap kalau gagal. Kamu membuatnya dengan `runCatching`:",
                    "",
                    "  val hasil: Result<Int> = runCatching { teks.toInt() }",
                    "  hasil.getOrNull()",
                    "  hasil.getOrDefault(0)",
                    "  hasil.getOrElse { -1 }",
                    "  hasil.onSuccess { }.onFailure { }",
                    "  hasil.map { it * 2 }",
                    "",
                    "`runCatching` menangkap semua Throwable, yaitu induk dari semua error",
                    "dan exception di JVM. Jangkauannya terlalu luas untuk dipakai",
                    "sembarangan. Kalau kodemu cuma boleh gagal dengan cara tertentu, sealed",
                    "class bikinan sendiri lebih tepat. Contohnya `Hasil` di materi Data",
                    "Class, Object & Sealed.",
                    "",
                    "`use` adalah padanan try-with-resources di Java, yaitu cara menutup",
                    "berkas secara otomatis:",
                    "  File(\"data.txt\").bufferedReader().use { it.readText() }",
                    "",
                    "Berkasnya ditutup apa pun yang terjadi, termasuk kalau pembacaannya",
                    "gagal di tengah jalan.",
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
                    "Catch diperiksa dari atas ke bawah, dan yang dijalankan adalah catch",
                    "pertama yang cocok. Di contoh ini `SaldoKurangException` ditulis sebelum",
                    "`IllegalArgumentException`. Keduanya sama-sama turunan",
                    "`RuntimeException`, dan yang satu bukan turunan yang lain. Jadi di",
                    "contoh ini urutannya nggak berpengaruh, karena tiap exception cuma cocok",
                    "dengan satu catch.",
                    "",
                    "Urutan baru menentukan kalau tipe yang satu turunan tipe lainnya.",
                    "Misalnya `catch (e: Exception)` ditulis paling atas. Dia bakal menangkap",
                    "semuanya, dan catch di bawahnya nggak pernah jalan. C# menolak urutan",
                    "seperti itu waktu kompilasi, sedangkan Kotlin nggak memperingatkanmu.",
                    "Jadi tulis tipe yang paling khusus lebih dulu.",
                    "",
                    "`?: throw ...` di `parseNilai` memanfaatkan tipe `Nothing`. `Nothing`",
                    "adalah turunan dari semua tipe, jadi `throw` cocok di sisi kanan Elvis",
                    "dan compiler nggak keberatan.",
                    "",
                    "Kebiasaan baik soal exception sama seperti di bahasa lain:",
                    "  - Jangan menulis `catch (e: Exception) { }` yang kosong. Programnya",
                    "    jalan terus dalam keadaan rusak.",
                    "  - Jangan menangkap exception yang nggak bisa kamu perbaiki.",
                    "  - Jangan memakai exception untuk alur normal. Salah ketik pengguna itu",
                    "    kejadian normal, jadi pakai `toIntOrNull`.",
                    "",
                    "Hati-hati, yang ini khusus Kotlin. Kalau kodemu memakai coroutine",
                    "(dibahas di materi sesudah ini), jangan sembarangan menangkap",
                    "`Exception`. Coroutine bisa dibatalkan, artinya dihentikan karena",
                    "hasilnya sudah nggak dibutuhkan. Pembatalan itu bekerja lewat",
                    "`CancellationException`, yang merupakan turunan `Exception`. Kalau",
                    "exception itu ikut tertelan, pembatalannya berhenti bekerja tanpa satu",
                    "pun tanda.",
                ]
            },
        ],
    },
    {
        "title": "13. Coroutine: Asinkron Tanpa Callback",
        "sections": [
            {
                "body": [
                    "Coroutine adalah cara Kotlin menangani pekerjaan yang isinya menunggu,",
                    "misalnya memanggil API, membaca berkas, atau menjalankan query",
                    "(permintaan data) ke database. Selama satu pekerjaan menunggu, program",
                    "bisa mengerjakan hal lain. Cara kerja seperti ini disebut asinkron.",
                    "",
                    "Cara lama menulis kode asinkron adalah callback, yaitu fungsi yang kamu",
                    "titipkan untuk dipanggil nanti waktu pekerjaannya selesai. Kalau",
                    "callback-nya bersarang, kodenya cepat berantakan. Dengan coroutine, kode",
                    "asinkron ditulis seperti kode biasa, dari atas ke bawah, tanpa callback",
                    "bersarang dan tanpa rantai `.then()`:",
                    "",
                    "  suspend fun ambil(): String {",
                    "      delay(1000)          // tidak memblokir thread",
                    "      return \"data\"",
                    "  }",
                    "",
                    "Thread adalah jalur kerja yang menjalankan kodemu, dan satu program bisa",
                    "punya beberapa thread. `delay(1000)` menunggu satu detik tanpa memblokir",
                    "thread. Artinya thread itu bebas mengerjakan hal lain selama menunggu.",
                    "",
                    "`suspend` menandai fungsi yang bisa berhenti sejenak lalu dilanjutkan",
                    "lagi. Fungsi suspend cuma boleh dipanggil dari fungsi suspend lain, atau",
                    "dari dalam coroutine.",
                    "",
                    "Cara memulai coroutine:",
                    "  runBlocking { }      memblokir thread; untuk main & tes",
                    "  launch { }           jalankan, jangan tunggu hasilnya",
                    "  async { }            jalankan, hasilnya diambil .await()",
                    "  withContext(D) { }   pindah dispatcher, tunggu selesai",
                    "",
                    "Dispatcher menentukan thread mana yang dipakai coroutine:",
                    "  Dispatchers.Default   perhitungan berat, sejumlah core",
                    "  Dispatchers.IO        menunggu jaringan/berkas, banyak thread",
                    "  Dispatchers.Main      UI (Android)",
                    "  Dispatchers.Unconfined  jarang dipakai",
                    "",
                    "Core di tabel itu artinya inti prosesor. `Dispatchers.Default` memakai",
                    "thread sebanyak jumlah core-nya, paling sedikit dua.",
                    "",
                    "Gagasan inti coroutine namanya structured concurrency. Concurrency",
                    "artinya beberapa pekerjaan berjalan bersamaan, dan structured artinya",
                    "pekerjaan itu tertata. Aturannya: coroutine selalu punya induk, dan",
                    "induknya nggak selesai sebelum semua anaknya selesai.",
                    "",
                    "Dengan aturan itu, beberapa masalah nyata jadi beres:",
                    "  - Nggak ada coroutine yang bocor tanpa pemilik.",
                    "  - Membatalkan induk ikut membatalkan semua anaknya.",
                    "  - Error di anak dilaporkan ke induknya, jadi nggak hilang.",
                    "",
                    "Bedakan juga pekerjaan yang berurutan dan yang bersamaan. Salah memilih",
                    "di sini adalah kesalahan yang paling mahal. Misalnya `ambilA()` dan",
                    "`ambilB()` masing-masing butuh satu detik:",
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
                    "Coroutine nggak termasuk bahasa Kotlin itu sendiri. Dia pustaka terpisah",
                    "yang harus kamu tambahkan ke proyek, di berkas build.gradle.kts (dibahas",
                    "di materi Struktur Proyek & Gradle):",
                    "  implementation(\"org.jetbrains.kotlinx:kotlinx-coroutines-core:1.9.0\")",
                    "",
                    "Yang ada di bahasanya cuma kata kunci `suspend`, ditambah mesin state",
                    "(state machine) yang dibuat compiler untuk tiap fungsi suspend. Mesin",
                    "state itu mencatat sampai mana fungsinya berjalan, supaya bisa",
                    "dilanjutkan dari titik berhentinya.",
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
                    "Contoh di atas memakai Thread supaya bisa dijalankan tanpa dependensi,",
                    "yaitu tanpa pustaka tambahan. Pelajarannya sama dengan versi coroutine,",
                    "begitu juga kesalahan yang dihindarinya. Kalau `await()` ditulis tepat",
                    "sesudah `async`, pekerjaan yang seharusnya bersamaan jadi berbaris",
                    "satu-satu:",
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
                    "Di versi yang salah, `await()` langsung menunggu hasilnya, jadi `async`",
                    "kedua baru mulai sesudah yang pertama selesai.",
                    "",
                    "Yang nggak bisa ditiru thread biasa adalah ongkosnya. Satu thread JVM",
                    "memakan sekitar satu megabyte memori untuk stack, yaitu catatan",
                    "fungsi-fungsi yang sedang berjalan. Satu coroutine cuma butuh beberapa",
                    "ratus byte. Makanya server berbasis coroutine bisa melayani ratusan ribu",
                    "koneksi bersamaan di mesin yang sama.",
                    "",
                    "Beberapa hal yang wajib kamu tahu waktu memakai coroutine sungguhan:",
                    "  - `runBlocking` cuma untuk main dan tes. Dia memblokir thread selama",
                    "    menunggu, jadi kalau dipakai di kode produksi (program yang dipakai",
                    "    sungguhan), gunanya hilang.",
                    "  - `GlobalScope` membuat coroutine tanpa induk. Itu melanggar",
                    "    structured concurrency dan hampir selalu salah.",
                    "  - Pakai `withContext(Dispatchers.IO)` untuk pekerjaan yang menunggu,",
                    "    dan `Dispatchers.Default` untuk pekerjaan yang menghitung.",
                    "  - Pembatalan bersifat kooperatif, artinya coroutine harus ikut bekerja",
                    "    sama supaya bisa dibatalkan. Kode yang nggak pernah suspend nggak",
                    "    bisa dibatalkan. Di perulangan panjang, sisipkan `yield()` atau",
                    "    periksa `isActive`.",
                ]
            },
        ],
    },
    {
        "title": "14. Teks, Regex & Format",
        "sections": [
            {
                "body": [
                    "Ini method String yang paling sering dipakai:",
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
                    "String di Kotlin immutable, artinya isinya nggak bisa diubah sesudah",
                    "dibuat, sama seperti di Java dan C#. Jadi semua method di atas",
                    "mengembalikan string baru, dan string aslinya tetap.",
                    "",
                    "Raw string ditulis dengan tiga tanda kutip ganda. Di dalamnya nggak ada",
                    "escape, yaitu kode berawalan backslash seperti `\\n` untuk baris baru.",
                    "Raw string juga boleh terdiri dari beberapa baris.",
                    "",
                    "`trimIndent()` membuang indentasi yang ikut terbawa, yaitu indentasi",
                    "yang sama di semua barisnya. Kalau kamu ingin mengatur indentasinya",
                    "sendiri, pakai `trimMargin()`. Fungsi itu memakai garis tegak (|)",
                    "sebagai penanda awal tiap baris.",
                    "",
                    "Raw string cocok untuk regex (pola pencarian teks, dibahas di bawah) dan",
                    "path Windows. Polanya bisa ditulis apa adanya tanpa menggandakan",
                    "backslash.",
                    "",
                    "Untuk menyusun teks yang rapi, pakai extension `format`:",
                    "  \"%-10s%5d%8.2f\".format(nama, jumlah, harga)",
                    "  \"%,d\".format(1234567)          -> 1,234,567",
                    "  \"%05d\".format(42)              -> 00042",
                    "  \"%+.1f\".format(3.14)           -> +3.1",
                    "",
                    "Kode berawalan % di situ disebut penentu format:",
                    "  - `%-10s` artinya teks selebar 10 kolom, rata kiri.",
                    "  - `%5d` artinya bilangan bulat selebar 5 kolom.",
                    "  - `%8.2f` artinya pecahan selebar 8 kolom, dengan dua angka di",
                    "    belakang koma.",
                    "  - `%,d` artinya bilangan bulat dengan pemisah ribuan.",
                    "",
                    "Sama seperti di Java, penentu `%,d` dan `%.2f` mengikuti setelan wilayah",
                    "(locale) komputernya. Pemisah ribuan dan pemisah desimalnya bisa beda",
                    "antarnegara. Kalau keluarannya harus sama di mesin mana pun, oper Locale",
                    "secara eksplisit:",
                    "  \"%.2f\".format(Locale.ROOT, nilai)",
                    "",
                    "Regex (regular expression) adalah pola untuk mencari teks, misalnya",
                    "\"empat angka, tanda hubung, dua angka\". Di Kotlin, regex adalah class",
                    "tersendiri, terpisah dari String:",
                    "",
                    "  val pola = Regex(\"\\\\d{4}-\\\\d{2}-\\\\d{2}\")",
                    "  pola.matches(teks)         seluruh teks cocok",
                    "  pola.containsMatchIn(teks) ada di dalamnya",
                    "  pola.find(teks)            MatchResult pertama, atau null",
                    "  pola.findAll(teks)         Sequence semua kecocokan",
                    "  pola.replace(teks, \"x\")",
                    "  pola.split(teks)",
                    "",
                    "Di string biasa, backslash harus ditulis dua kali, karena backslash",
                    "tunggal dipakai untuk escape. Jadi `\\\\d` di kode itu sampai ke regex",
                    "sebagai `\\d`, artinya satu angka. `{4}` artinya empat kali.",
                    "",
                    "Perhatikan: `matches` menuntut seluruh teks cocok dengan pola. Di Ruby",
                    "dan PHP, pencocokan bawaannya cukup sebagian. Untuk validasi, perilaku",
                    "Kotlin ini lebih aman.",
                    "",
                    "Bagian pola yang ditulis di dalam kurung disebut grup. Hasil tiap grup",
                    "bisa diambil sendiri-sendiri dari `m`, yaitu MatchResult hasil `find`:",
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
                    "`m.destructured` memecah hasil grup regex jadi beberapa variabel",
                    "sekaligus. Dia mengambil grup menurut nomornya: variabel pertama dapat",
                    "grup 1, variabel kedua dapat grup 2, dan seterusnya. Tanda `_` di contoh",
                    "tadi artinya grup 1 (tanggalnya) sengaja nggak dipakai. Jumlah",
                    "variabelnya boleh lebih sedikit daripada jumlah grup, asal nggak",
                    "melebihi jumlah grup di polanya.",
                    "",
                    "Tiga baris terakhir menunjukkan beda yang paling sering menjebak.",
                    "`matches` menuntut seluruh teks cocok, sedangkan `containsMatchIn` cukup",
                    "sebagian. Untuk memvalidasi masukan, `matches` yang benar. Di Kotlin,",
                    "`matches` memang pencocokan utuh secara bawaan, beda dari Ruby dan PHP.",
                    "",
                    "Jebakan: tanpa Locale yang ditulis eksplisit, `format` mengikuti setelan",
                    "wilayah komputernya. Pemisah ribuannya jadi titik di locale Indonesia",
                    "dan koma di locale Inggris. Akibatnya tes yang lulus di laptopmu bisa",
                    "gagal di server. Kalau keluarannya harus sama di mesin mana pun,",
                    "`Locale.ROOT` wajib dipakai.",
                    "",
                    "Di kode sungguhan, pola regex lebih enak ditulis pakai raw string tiga",
                    "kutip, supaya backslash-nya nggak perlu digandakan:",
                    "  val tanggal = Regex(\"\"\"\\d{4}-\\d{2}-\\d{2}\"\"\")",
                ]
            },
        ],
    },
    {
        "title": "15. Berkas & Baris Perintah",
        "sections": [
            {
                "body": [
                    "Untuk urusan berkas, Kotlin memakai pustaka bawaan Java, yaitu java.io",
                    "dan java.nio. Bedanya, Kotlin menambahkan extension function sehingga",
                    "kodenya jauh lebih ringkas:",
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
                    "`writeText` menimpa isi berkas, sedangkan `appendText` menambah di",
                    "bagian akhir. `readText` membaca semuanya jadi satu String, dan",
                    "`readLines` membacanya jadi list berisi baris-baris.",
                    "",
                    "Untuk berkas besar, pakai `useLines`. Dia membaca secara malas, artinya",
                    "baris berikutnya baru diambil waktu dibutuhkan, lalu menutup berkasnya",
                    "otomatis. Sebaliknya, `readLines()` menarik seluruh isi berkas ke memori",
                    "sekaligus.",
                    "",
                    "Untuk memeriksa dan mengelola berkas:",
                    "  f.exists()  f.length()  f.isDirectory",
                    "  f.delete()  f.renameTo(g)  f.copyTo(g)",
                    "  f.mkdirs()  f.listFiles()",
                    "  f.name  f.extension  f.nameWithoutExtension  f.parent",
                    "",
                    "Windows memisahkan folder dengan backslash, sedangkan Linux dan macOS",
                    "memakai garis miring. Supaya path-nya benar di sistem mana pun, susun",
                    "dengan cara ini:",
                    "  File(folder, \"data.txt\")",
                    "  System.getProperty(\"java.io.tmpdir\")",
                    "",
                    "`File(folder, \"data.txt\")` memilih pemisah yang benar sendiri.",
                    "`java.io.tmpdir` berisi alamat folder sementara milik sistem.",
                    "",
                    "`use` adalah padanan try-with-resources di Java. Dia berlaku untuk apa",
                    "pun yang Closeable, yaitu benda yang harus ditutup sesudah dipakai,",
                    "seperti berkas:",
                    "  File(\"a.txt\").bufferedReader().use { it.readText() }",
                    "",
                    "JSON adalah format teks yang populer untuk bertukar data. Kotlin nggak",
                    "punya pengurai JSON bawaan. Pilihan yang lazim:",
                    "  kotlinx.serialization   resmi, memakai plugin compiler",
                    "  Gson / Jackson / Moshi  dari dunia Java",
                    "",
                    "Dengan kotlinx.serialization, satu anotasi sudah cukup. Anotasi adalah",
                    "penanda berawalan @ yang ditempel di atas class:",
                    "",
                    "  @Serializable",
                    "  data class Murid(val nama: String, val nilai: Int)",
                    "",
                    "  Json.encodeToString(murid)",
                    "  Json.decodeFromString<Murid>(teks)",
                    "",
                    "`encodeToString` mengubah objek jadi teks JSON, dan `decodeFromString`",
                    "mengubah teks JSON jadi objek.",
                    "",
                    "kotlinx.serialization bekerja tanpa refleksi, yaitu kemampuan program",
                    "memeriksa isi class-nya sendiri waktu jalan. Kode pengubahnya sudah",
                    "dibuat compiler lebih dulu. Karena itu pustaka ini juga jalan di",
                    "Kotlin/Native dan Kotlin/JS, selain di JVM.",
                    "",
                    "Argumen baris perintah adalah kata-kata yang kamu ketik sesudah nama",
                    "program waktu menjalankannya. Argumen itu masuk lewat parameter `main`:",
                    "  fun main(args: Array<String>) { ... }",
                    "",
                    "Variabel lingkungan dibaca dengan `System.getenv(\"HOME\")`. Variabel",
                    "lingkungan adalah setelan yang disediakan sistem operasi untuk program,",
                    "misalnya HOME yang berisi folder rumah pengguna.",
                    "",
                    "Masukan dibaca dengan `readLine()`. Hasilnya bertipe `String?`, dan",
                    "isinya null kalau masukannya habis. Ini masuk akal, karena masukan yang",
                    "dialirkan dari berkas memang bisa habis.",
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
                    "`buildString { ... }` membuat sebuah StringBuilder, yaitu wadah untuk",
                    "menyusun teks sedikit demi sedikit. Bloknya dijalankan dengan",
                    "StringBuilder itu sebagai penerima, jadi `appendLine` bisa langsung",
                    "dipanggil. Sesudah itu hasilnya dikembalikan sebagai String. Pola yang",
                    "sama ada di `buildList`, `buildMap`, dan `buildSet`.",
                    "",
                    "`this@keCsv` menyebut penerima extension function `keCsv`, yaitu list",
                    "muridnya. Label ini perlu karena di dalam `buildString`, kata `this`",
                    "sudah dipakai StringBuilder. Label penerima seperti ini muncul tiap kali",
                    "ada scope bersarang, yaitu blok di dalam blok yang masing-masing punya",
                    "`this` sendiri.",
                    "",
                    "`joinToString(pemisah, awalan, akhiran) { ... }` menyusun seluruh teks",
                    "JSON dalam satu ekspresi. Di contoh tadi pemisahnya `,\\n`, awalannya",
                    "`[\\n`, dan akhirannya `\\n]`. Tiga parameter pertama ini sering terlupa,",
                    "padahal berguna sekali.",
                    "",
                    "`val (nama, kelas, nilai) = baris.split(\",\")` memakai destructuring pada",
                    "List, yaitu memecah isi list jadi beberapa variabel sekaligus. Cara ini",
                    "bisa dipakai untuk paling banyak lima komponen.",
                    "",
                    "Hati-hati: kalau sebuah baris punya kolom lebih sedikit daripada jumlah",
                    "variabelnya, destructuring tadi melempar IndexOutOfBoundsException.",
                    "",
                    "Jebakan: `split(\",\")` cuma benar kalau nggak ada koma di dalam kolom.",
                    "Misalnya nama \"Budi, S.Kom\" bakal terpecah jadi dua kolom. Masalah CSV",
                    "(teks yang kolomnya dipisah koma) ini sama di semua bahasa. Untuk data",
                    "sungguhan, pakai pustaka CSV. Untuk latihan seperti ini cukup, asal kamu",
                    "tahu batasnya.",
                ]
            },
        ],
    },
    {
        "title": "16. Struktur Proyek & Gradle",
        "sections": [
            {
                "body": [
                    "Package adalah nama kelompok untuk kode. Gunanya mengelompokkan kode dan",
                    "mencegah nama bertabrakan, misalnya dua class bernama `Produk` di dua",
                    "bagian program:",
                    "",
                    "  package toko.domain",
                    "",
                    "  import toko.data.ProdukRepository",
                    "  import kotlin.math.sqrt",
                    "  import java.time.LocalDate as Tanggal      alias",
                    "",
                    "`import` mengambil nama dari package lain. Kata `as` memberi nama lain",
                    "(alias), jadi di berkas itu `LocalDate` bisa dipanggil `Tanggal`.",
                    "",
                    "Beda dengan Java, nama berkas Kotlin nggak harus sama dengan nama class,",
                    "dan satu berkas boleh berisi beberapa class sekaligus. Susunan folder",
                    "juga nggak wajib mengikuti package, walaupun mengikutinya tetap",
                    "kebiasaan yang baik.",
                    "",
                    "Kotlin juga mengizinkan fungsi dan properti di level berkas, di luar",
                    "class mana pun. Makanya kode utilitas di Kotlin nggak butuh class",
                    "`Utils` yang isinya method statis semua.",
                    "",
                    "Gradle adalah build tool, yaitu alat yang mengompilasi kode, menjalankan",
                    "tes, dan mengunduh pustaka yang dibutuhkan. Hampir semua proyek Kotlin",
                    "memakainya. Berkas konfigurasinya juga ditulis dalam Kotlin, namanya",
                    "build.gradle.kts. Perintah sehari-harinya:",
                    "",
                    "  ./gradlew build          kompilasi + tes",
                    "  ./gradlew run            jalankan",
                    "  ./gradlew test           tes saja",
                    "  ./gradlew clean",
                    "  ./gradlew dependencies   pohon dependensi",
                    "",
                    "`clean` menghapus hasil build yang lama. Dependensi adalah pustaka lain",
                    "yang dipakai proyekmu. `dependencies` menampilkannya sebagai pohon,",
                    "lengkap dengan pustaka yang dipakai oleh pustaka itu.",
                    "",
                    "`./gradlew` itu Gradle wrapper, skrip kecil yang mengunduh versi Gradle",
                    "yang tepat untuk proyek itu. Selalu pakai wrapper, jangan `gradle` yang",
                    "terpasang global di komputermu. Dengan wrapper, build di mesinmu dan di",
                    "CI menghasilkan hal yang sama. CI (continuous integration) adalah server",
                    "yang otomatis membangun dan menguji kode setiap kali ada perubahan.",
                    "",
                    "Di bagian dependencies, pustaka bisa ditambahkan dengan dua cara:",
                    "  - `implementation`: dependensinya nggak diteruskan ke pemakai",
                    "    pustakamu. Ini pilihan bawaan yang benar.",
                    "  - `api`: dependensinya ikut diteruskan. Pakai cuma kalau tipe dari",
                    "    dependensi itu muncul di tanda tangan publikmu, yaitu fungsi dan",
                    "    class yang bisa dipanggil pemakai pustakamu.",
                    "",
                    "Memilih `implementation` bikin kompilasi ulang jauh lebih cepat, karena",
                    "perubahan di dependensi dalam nggak memaksa seluruh proyek dikompilasi",
                    "ulang.",
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
                    "Akhiran Kt di `mainClass.set(\"toko.MainKt\")` bukan salah ketik. Berkas",
                    "`Main.kt` yang berisi fungsi level atas dikompilasi jadi class bernama",
                    "`MainKt`. Kalau kamu menulisnya tanpa akhiran itu, `./gradlew run` bakal",
                    "mengeluh class-nya nggak ditemukan.",
                    "",
                    "`jvmToolchain(17)` memaksa Gradle memakai JDK 17, alih-alih JDK apa pun",
                    "yang kebetulan terpasang. Ini yang bikin build di mesin yang berbeda",
                    "menghasilkan hal yang sama.",
                    "",
                    "Gradle juga bisa mengunduh JDK 17 sendiri kalau belum ada, asal",
                    "proyeknya memasang penyedia JDK (toolchain resolver). Contohnya plugin",
                    "foojay-resolver-convention di settings.gradle.kts. Tanpa penyedia itu,",
                    "Gradle 8 ke atas berhenti dengan error bahwa JDK 17 nggak ditemukan.",
                    "",
                    "`gradle/libs.versions.toml` adalah daftar versi terpusat. Gradle",
                    "menyebutnya version catalog. Semua nomor versi dikumpulkan di satu",
                    "berkas, lalu dirujuk lewat nama seperti `libs.coroutines`. Modul adalah",
                    "bagian proyek yang dikompilasi sendiri-sendiri. Di proyek yang modulnya",
                    "banyak, cara ini menghapus satu jenis masalah sekaligus: versi pustaka",
                    "yang berbeda di modul yang berbeda.",
                    "",
                    "Berkas dan folder ini wajib ditulis di .gitignore, yaitu berkas berisi",
                    "daftar hal yang sengaja nggak dimasukkan ke git:",
                    "  build/",
                    "  .gradle/",
                    "  local.properties",
                    "",
                    "Sebaliknya, `gradlew`, `gradlew.bat`, dan seluruh folder wrapper-nya",
                    "wajib masuk git. Tanpa itu, orang yang meng-clone proyekmu nggak punya",
                    "cara untuk membangunnya.",
                    "",
                    "Alat bantu yang layak dipasang sejak awal:",
                    "  ktlint / ktfmt      perapi dan pemeriksa gaya",
                    "  detekt              analisis statis, menemukan bug",
                    "                      dan kerumitan berlebih",
                    "  kover               pengukur cakupan tes",
                    "",
                    "Analisis statis artinya memeriksa kode tanpa menjalankannya. Cakupan tes",
                    "adalah persentase kode yang ikut dijalankan waktu tes berjalan.",
                ]
            },
        ],
    },
    {
        "title": "17. Pengujian",
        "sections": [
            {
                "body": [
                    "Tes otomatis adalah kode yang memeriksa kodemu sendiri. Kamu menulis",
                    "\"kalau dikasih ini, hasilnya harus itu\", lalu komputer mengecek semuanya",
                    "setiap kali tes dijalankan.",
                    "",
                    "Kotlin memakai JUnit 5, pustaka tes dari dunia Java, lewat pembungkus",
                    "bernama `kotlin.test`. Pembungkus ini memberi nama assertion yang lebih",
                    "enak dibaca. Assertion adalah pernyataan \"hasilnya harus begini\" yang",
                    "bikin tes gagal kalau nggak terpenuhi.",
                    "",
                    "  testImplementation(kotlin(\"test\"))",
                    "  import kotlin.test.*",
                    "",
                    "Baris pertama masuk ke bagian dependencies di build.gradle.kts. Baris",
                    "kedua ditulis di atas berkas tes.",
                    "",
                    "Ada fitur Kotlin yang berguna sekali di tes: nama fungsi boleh ditulis",
                    "di dalam backtick (`). Nama seperti itu boleh memuat spasi dan sebagian",
                    "tanda baca, misalnya tanda hubung, tapi titik nggak boleh di JVM.",
                    "Hasilnya, laporan tes terbaca seperti kalimat.",
                    "",
                    "Assertion yang tersedia:",
                    "  assertEquals(harap, aktual)      urutannya: harapan dulu",
                    "  assertNotEquals",
                    "  assertTrue / assertFalse",
                    "  assertNull / assertNotNull",
                    "  assertContains(koleksi, x)",
                    "  assertFailsWith<TipeError> { ... }",
                    "  assertIs<Tipe>(x)",
                    "  fail(\"pesan\")",
                    "",
                    "Urutan argumen `assertEquals` penting: nilai yang diharapkan dulu, baru",
                    "hasil yang didapat. Kalau ketuker, pesan gagalnya jadi terbalik dan",
                    "membingungkan.",
                    "",
                    "Jangan pakai `assertEquals` biasa untuk Double. Banyak pecahan desimal",
                    "nggak bisa disimpan persis dalam bentuk biner, jadi hasil hitungan bisa",
                    "meleset sedikit. Pakai toleransi, yaitu selisih yang masih boleh:",
                    "  assertEquals(85.0, hasil, 0.001)",
                    "",
                    "Beberapa anotasi, yaitu penanda berawalan @, mengatur jalannya tiap",
                    "tes:",
                    "  @BeforeTest   sebelum setiap tes",
                    "  @AfterTest    sesudah setiap tes",
                    "  @Ignore       lewati",
                    "",
                    "`@BeforeTest` penting karena dia bikin tiap tes mulai dari keadaan yang",
                    "sama persis. Tes yang hasilnya bergantung pada urutan menjalankannya",
                    "suatu hari bakal gagal, padahal nggak ada yang mengubah apa pun.",
                    "",
                    "Kebiasaan yang paling berharga dalam menulis tes adalah menguji di",
                    "batas. Kalau nilai A dimulai dari 85, uji 85 dan 84, jangan 90 dan 50.",
                    "Di batas itulah salah ketik antara `>=` dan `>` bakal ketahuan.",
                    "",
                    "Pustaka pihak ketiga yang lazim:",
                    "  kotest      gaya spesifikasi + property-based testing",
                    "  mockk       pembuat objek palsu, dirancang untuk Kotlin",
                    "  turbine     menguji Flow",
                    "  kotlinx-coroutines-test   runTest, waktu virtual",
                    "",
                    "Property-based testing artinya pustaka itu mencoba banyak masukan acak",
                    "untuk memeriksa satu sifat kodemu. Flow adalah aliran data dari pustaka",
                    "coroutine, yang nilainya datang satu per satu.",
                    "",
                    "`runTest` memakai waktu virtual, yaitu jam pura-pura yang bisa dimajukan",
                    "seketika. Jeda sepuluh detik di dalam tes jadi selesai saat itu juga,",
                    "nggak perlu menunggu sungguhan.",
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
                    "Lihat nilai yang dipilih di tes grade: 85 dan 84, 75 dan 74, 60 dan 59.",
                    "Menguji tepat di batas jauh lebih berguna daripada menguji nilai di",
                    "tengah rentang. Tes dengan nilai di tengah rentang hampir nggak pernah",
                    "menemukan bug.",
                    "",
                    "`assertEquals(harap, aktual, \"pesan\")` punya argumen ketiga, yaitu pesan",
                    "yang muncul waktu tesnya gagal. Di tes yang berulang seperti di atas,",
                    "tanpa pesan itu kamu cuma tahu ada yang gagal, tanpa tahu yang mana.",
                    "",
                    "`assertEquals(85.0, hasil, 0.001)` memakai toleransi. Tanpa toleransi,",
                    "tesmu bisa gagal cuma karena selisih kecil di digit paling belakang.",
                    "Selisih itu muncul karena banyak pecahan desimal nggak bisa disimpan",
                    "persis dalam bentuk biner.",
                    "",
                    "`catat` mengembalikan `this`, jadi penyiapan data tes cukup satu baris,",
                    "nggak perlu tiga. Biasanya API yang enak diuji juga enak dipakai.",
                    "",
                    "Cara menjalankan tes:",
                    "  ./gradlew test",
                    "  ./gradlew test --tests \"*grade*\"",
                    "  ./gradlew test --info          keluaran lengkap",
                    "",
                    "Opsi `--tests \"*grade*\"` cuma menjalankan tes yang namanya mengandung",
                    "kata grade.",
                    "",
                    "Cakupan tes berguna untuk menemukan bagian yang belum diuji, dan",
                    "angkanya nggak perlu dikejar. Cakupan seratus persen cuma berarti tiap",
                    "baris pernah dijalankan tes. Itu belum berarti hasilnya diperiksa. Kalau",
                    "assertion-nya lemah, bug tetap lolos, dan angka seratus persen itu malah",
                    "bikin kamu merasa aman. Cakupan tujuh puluh persen dengan assertion yang",
                    "memeriksa perilaku jauh lebih berguna.",
                ]
            },
        ],
    },
    {
        "title": "18. Proyek Utuh: Menggabungkan Semuanya",
        "sections": [
            {
                "body": [
                    "Materi penutup ini menggabungkan data class, sealed class, koleksi,",
                    "scope function, dan pemisahan tanggung jawab dalam satu program utuh.",
                    "",
                    "Yang dibangun adalah sistem inventaris gudang, yaitu program pencatat",
                    "stok barang. Fokusnya ada di cara bagian-bagiannya dipisah, jadi jangan",
                    "terlalu memikirkan fiturnya.",
                    "",
                    "Programnya dibagi jadi tiga lapisan. Panah ketergantungannya satu arah:",
                    "Antarmuka memakai Layanan, Layanan memakai Model, dan nggak pernah",
                    "sebaliknya.",
                    "",
                    "  Antarmuka  ->  Layanan  ->  Model",
                    "",
                    "  - Model: data class `Barang`, enum `Gerak`, dan sealed class untuk",
                    "    galatnya. Model nggak tahu apa-apa soal layar.",
                    "  - Layanan: class `Gudang` beserta semua aturannya. Layanan nggak",
                    "    pernah memanggil `println`.",
                    "  - Antarmuka: fungsi `main`. Tugasnya memanggil layanan, lalu mencetak",
                    "    hasilnya.",
                    "",
                    "Yang khas Kotlin di sini: kegagalan nggak dilempar sebagai exception.",
                    "Kegagalan dikembalikan sebagai bagian dari tipe hasilnya, lewat sealed",
                    "class.",
                    "",
                    "Bedanya terasa di tiga hal:",
                    "  - Compiler memaksa pemanggil menangani setiap cabang, karena `when`",
                    "    atas sealed class diperiksa kelengkapannya.",
                    "  - Nggak ada jalur kegagalan yang tersembunyi dari tanda tangan",
                    "    fungsinya, yaitu nama, parameter, dan tipe kembaliannya.",
                    "  - Menambah jenis galat baru langsung membuat setiap `when` yang belum",
                    "    diperbarui gagal dikompilasi.",
                    "",
                    "Ini pola yang sama dengan Result di Rust. Di Kotlin, pola ini tersedia",
                    "tanpa fitur bahasa tambahan apa pun, cukup pakai sealed class.",
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
                    "Ada empat keputusan di program ini yang layak ditiru:",
                    "  1. Kegagalan dikembalikan lewat sealed class, nggak dilempar. Tanda",
                    "     tangan `catat` sudah menyatakan bahwa fungsi itu bisa gagal, dan",
                    "     `when` atas hasilnya wajib lengkap. Jadi jalur kegagalan nggak",
                    "     mungkin terlewat tanpa ketahuan.",
                    "  2. `Barang` adalah data class yang nggak bisa diubah. Stok diubah",
                    "     lewat `copy(stok = baru)`, yang menghasilkan objek baru. Jadi nggak",
                    "     ada bagian lain program yang bisa memegang sebuah `Barang` lalu",
                    "     mengubah stoknya tanpa ketahuan.",
                    "  3. `semua()` dan `stokMenipis()` mengurutkan hasilnya sebelum",
                    "     dikembalikan. Keluaran yang urutannya nggak pasti mustahil diuji.",
                    "  4. `Gudang` sama sekali nggak memanggil `println`. Karena itu semua",
                    "     aturannya bisa diuji dengan `assertEquals`, tanpa perlu membaca",
                    "     layar.",
                    "",
                    "`when (val hasil = gudang.catat(...))` menggabungkan penugasan dan",
                    "pencocokan dalam satu baris. Penugasan artinya mengisi variabel. Bentuk",
                    "ini lazim sekali di Kotlin, dan variabel `hasil` cuma hidup di dalam",
                    "`when` itu.",
                    "",
                    "`compareBy({ it.stok }, { it.kode })` membuat pembanding dua tingkat",
                    "dalam satu ekspresi: urutkan menurut stok, dan kalau stoknya sama,",
                    "menurut kode. Untuk urutan menurun, pasangannya `compareByDescending`.",
                    "",
                    "Kalau kamu ingin melanjutkan program ini, ini langkah berikutnya:",
                    "  - Simpan datanya ke JSON dengan kotlinx.serialization.",
                    "  - Sembunyikan penyimpanan di balik sebuah interface. Dengan begitu",
                    "    `Gudang` nggak tahu datanya ada di berkas, di database, atau cuma di",
                    "    memori waktu tes.",
                    "  - Jadikan operasinya suspend, lalu panggil dari coroutine.",
                    "  - Tulis tes untuk `Gudang`. Tes ini bisa langsung ditulis tanpa",
                    "    mengubah satu baris pun, justru karena keputusan nomor 4.",
                ]
            },
        ],
    },
]
