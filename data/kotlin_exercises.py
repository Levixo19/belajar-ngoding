KOTLIN_EXERCISES = [
    {
        "title": "Latihan 1: Perkenalan Diri",
        "difficulty": "Mudah",
        "question": [
            "Buat program Kotlin yang menampilkan tepat tiga baris.",
            "",
            "Keluaran yang diharapkan:",
            "",
            "  Halo, namaku Andi!",
            "  Aku sedang belajar Kotlin.",
            "  Kotlin memeriksa null saat kompilasi.",
        ],
        "hints": [
            "Program Kotlin dimulai dari fungsi main, tanpa class pembungkus seperti di Java. Baca ulang materi \"Pengenalan Kotlin & Instalasi\".",
            "Tulis tiga perintah cetak di dalam main, satu untuk tiap baris keluaran. println() mencetak teksnya lalu pindah baris, dan Kotlin nggak butuh titik koma di akhir baris.",
            "Kerangkanya: fun main() { ... }, lalu isi kurawalnya dengan tiga println(\"...\") berisi kalimat persis seperti di soal.",
        ],
        "solution": """fun main() {
    println("Halo, namaku Andi!")
    println("Aku sedang belajar Kotlin.")
    println("Kotlin memeriksa null saat kompilasi.")
}""",
    },
    {
        "title": "Latihan 2: Kalkulator Dua Bilangan",
        "difficulty": "Mudah",
        "question": [
            "Buat dua variabel a = 17 dan b = 5, lalu tampilkan:",
            "",
            "Keluaran yang diharapkan:",
            "",
            "  17 + 5 = 22",
            "  17 - 5 = 12",
            "  17 * 5 = 85",
            "  17 / 5 = 3",
            "  17 % 5 = 2",
            "  17 / 5 = 3.40 (desimal)",
        ],
        "hints": [
            "Ini latihan operator aritmetika dan string template. Baca ulang materi \"val, var & Tipe Data\", terutama bagian pembagian Int.",
            "Tiap baris berbentuk \"a op b = hasil\": sisipkan nilai dengan $a dan hasil hitungan dengan ${...}. 17 / 5 antara dua Int menghasilkan 3 karena sisanya dibuang; untuk 3.40, ubah salah satu sisi jadi Double dengan .toDouble().",
            "Contoh satu baris: println(\"$a + $b = ${a + b}\"). Dua angka di belakang koma: \"%.2f\".format(nilai).",
        ],
        "solution": """fun main() {
    val a = 17
    val b = 5

    println("$a + $b = ${a + b}")
    println("$a - $b = ${a - b}")
    println("$a * $b = ${a * b}")
    println("$a / $b = ${a / b}")
    println("$a % $b = ${a % b}")
    println("$a / $b = ${"%.2f".format(a.toDouble() / b)} (desimal)")
}""",
    },
    {
        "title": "Latihan 3: Konversi Suhu",
        "difficulty": "Mudah",
        "question": [
            "Baca satu angka suhu Celsius dari input.",
            "Tampilkan konversinya ke Fahrenheit dan Kelvin.",
            "",
            "Rumus:",
            "  F = C * 9 / 5 + 32",
            "  K = C + 273.15",
            "",
            "Untuk input 25, keluaran yang diharapkan:",
            "",
            "  Celsius    : 25.00",
            "  Fahrenheit : 77.00",
            "  Kelvin     : 298.15",
        ],
        "hints": [
            "Kamu perlu membaca input, mengubahnya jadi angka, lalu menghitung dengan Double. Baca ulang materi \"Null Safety\" (readLine() mengembalikan String?) dan \"val, var & Tipe Data\".",
            "Baca baris dengan readLine(), tangani null-nya dengan !! atau ?:, lalu trim() dan toDouble(). Hitung F dengan 9.0 / 5 supaya bukan pembagian Int. Jangan mencetak prompt apa pun sebelum membaca input, karena teks itu ikut dinilai.",
            "Dua desimal: \"%.2f\".format(f). Perhatikan perataan label di soal: \"Celsius    : \" diikuti beberapa spasi supaya titik duanya sejajar.",
        ],
        "stdin": "25\n",
        "solution": """fun main() {
    val c = readLine()!!.trim().toDouble()
    val f = c * 9.0 / 5 + 32
    val k = c + 273.15

    println("Celsius    : ${"%.2f".format(c)}")
    println("Fahrenheit : ${"%.2f".format(f)}")
    println("Kelvin     : ${"%.2f".format(k)}")
}""",
    },
    {
        "title": "Latihan 4: Grade & Kelulusan",
        "difficulty": "Mudah",
        "question": [
            "Baca satu angka nilai (0-100) dari input.",
            "Tampilkan grade sesuai aturan:",
            "  >= 85 : A",
            "  >= 75 : B",
            "  >= 60 : C",
            "  >= 40 : D",
            "  selain itu : E",
            "",
            "Lalu tampilkan status Lulus kalau nilai >= 75,",
            "atau Tidak Lulus kalau kurang.",
            "",
            "Untuk input 78, keluaran yang diharapkan:",
            "",
            "  Grade: B",
            "  Status: Lulus",
        ],
        "hints": [
            "Ini soal rantai kondisi. Di Kotlin, when dan if adalah ekspresi yang menghasilkan nilai. Baca ulang materi \"Kendali Alur\".",
            "Baca nilai sebagai Int. Pakai when tanpa subjek, urutkan cabangnya dari batas tertinggi (85) ke terendah, dan akhiri dengan else. Simpan hasilnya di satu val, lalu tentukan status dengan if yang juga menghasilkan nilai.",
            "Bentuknya: when { nilai >= 85 -> \"A\" ... else -> \"E\" }. Cabang else wajib ada supaya semua kemungkinan tertangani.",
        ],
        "stdin_list": ["92\n", "78\n", "65\n", "45\n", "12\n"],
        "solution": """fun main() {
    val nilai = readLine()!!.trim().toInt()

    val grade = when {
        nilai >= 85 -> "A"
        nilai >= 75 -> "B"
        nilai >= 60 -> "C"
        nilai >= 40 -> "D"
        else -> "E"
    }

    println("Grade: $grade")
    println("Status: ${if (nilai >= 75) "Lulus" else "Tidak Lulus"}")
}""",
    },
    {
        "title": "Latihan 5: Tabel Perkalian",
        "difficulty": "Mudah",
        "question": [
            "Tampilkan tabel perkalian 1 sampai 5.",
            "",
            "Keluaran yang diharapkan:",
            "",
            "  1 x 1 =  1   1 x 2 =  2   1 x 3 =  3   1 x 4 =  4   1 x 5 =  5",
            "  2 x 1 =  2   2 x 2 =  4   2 x 3 =  6   2 x 4 =  8   2 x 5 = 10",
            "  3 x 1 =  3   3 x 2 =  6   3 x 3 =  9   3 x 4 = 12   3 x 5 = 15",
            "  4 x 1 =  4   4 x 2 =  8   4 x 3 = 12   4 x 4 = 16   4 x 5 = 20",
            "  5 x 1 =  5   5 x 2 = 10   5 x 3 = 15   5 x 4 = 20   5 x 5 = 25",
            "",
            "Tiap baris diawali dua spasi. Hasil perkaliannya rata kanan",
            "selebar 2 karakter, dan tiap sel dipisah tiga spasi.",
        ],
        "hints": [
            "Butuh perulangan bersarang: satu untuk baris, satu untuk kolom. Baca ulang materi \"Kendali Alur\" (for dengan rentang 1..5) dan \"Teks, Regex & Format\" untuk perataan.",
            "Untuk tiap baris b, bangun lima sel \"b x k = hasil\", gabungkan dengan tiga spasi, lalu awali barisnya dengan dua spasi. Hasil perkalian harus rata kanan selebar 2.",
            "Rata kanan: (b * k).toString().padStart(2), atau \"%2d\".format(hasil). Menggabungkan sel: (1..5).map { k -> ... }.joinToString(\"   \").",
        ],
        "solution": """fun main() {
    for (b in 1..5) {
        val sel = (1..5).map { k -> "$b x $k = ${(b * k).toString().padStart(2)}" }
        println("  " + sel.joinToString("   "))
    }
}""",
    },
    {
        "title": "Latihan 6: Statistik Nilai",
        "difficulty": "Menengah",
        "question": [
            "Diberikan daftar nilai berikut di dalam kodemu:",
            "  78, 92, 65, 88, 71, 95, 59, 83",
            "",
            "Keluaran yang diharapkan:",
            "",
            "  Data      : 78, 92, 65, 88, 71, 95, 59, 83",
            "  Terurut   : 59, 65, 71, 78, 83, 88, 92, 95",
            "  Jumlah    : 8",
            "  Total     : 631",
            "  Rata-rata : 78.88",
            "  Tertinggi : 95",
            "  Terendah  : 59",
            "  Di atas rata-rata: 92, 88, 95, 83",
        ],
        "hints": [
            "Hampir semua yang diminta sudah ada sebagai fungsi bawaan koleksi. Baca ulang materi \"Koleksi\".",
            "Simpan daftar dengan listOf, hitung rata-ratanya sekali, lalu cetak tiap baris. Untuk baris Terurut pakai fungsi yang mengembalikan salinan, supaya baris Data tetap dalam urutan asli. sum(), average(), max(), dan min() sudah tersedia.",
            "sorted() mengembalikan salinan terurut (sort() mengubah di tempat). Menggabungkan jadi teks: joinToString(\", \"). Yang di atas rata-rata: filter { it > rata }, urutan aslinya tetap terjaga.",
        ],
        "solution": """fun main() {
    val nilai = listOf(78, 92, 65, 88, 71, 95, 59, 83)
    val rata = nilai.average()

    println("Data      : ${nilai.joinToString(", ")}")
    println("Terurut   : ${nilai.sorted().joinToString(", ")}")
    println("Jumlah    : ${nilai.size}")
    println("Total     : ${nilai.sum()}")
    println("Rata-rata : ${"%.2f".format(rata)}")
    println("Tertinggi : ${nilai.max()}")
    println("Terendah  : ${nilai.min()}")
    println("Di atas rata-rata: ${nilai.filter { it > rata }.joinToString(", ")}")
}""",
    },
    {
        "title": "Latihan 7: Balik Teks & Palindrom",
        "difficulty": "Menengah",
        "question": [
            "Baca satu baris teks dari input, lalu tampilkan:",
            "  Asli    : teks aslinya",
            "  Dibalik : teksnya dibalik",
            "  Huruf   : jumlah huruf tanpa spasi",
            "  Palindrom: ya / bukan (abaikan spasi dan besar-kecil huruf)",
            "",
            "Untuk input 'Kasur ini rusak', keluaran yang diharapkan:",
            "",
            "  Asli    : Kasur ini rusak",
            "  Dibalik : kasur ini rusaK",
            "  Huruf   : 13",
            "  Palindrom: ya",
        ],
        "hints": [
            "Ini soal olah String: membalik, menyaring karakter, dan membandingkan. Baca ulang materi \"Teks, Regex & Format\" dan \"Null Safety\" untuk readLine().",
            "Baca teks dan tangani null-nya. Buat versi tanpa spasi untuk menghitung huruf, lalu versi huruf kecil dari situ untuk cek palindrom. Baris Dibalik memakai teks asli, lengkap dengan spasi dan huruf besarnya.",
            "reversed() membalik String, filter { !it.isWhitespace() } membuang spasi, dan lowercase() menyamakan besar-kecil huruf.",
        ],
        "stdin_list": ["Kasur ini rusak\n", "Belajar Kotlin\n", "Ini\n"],
        "solution": """fun main() {
    val teks = readLine() ?: ""
    val rapat = teks.filter { !it.isWhitespace() }
    val bersih = rapat.lowercase()

    println("Asli    : $teks")
    println("Dibalik : ${teks.reversed()}")
    println("Huruf   : ${rapat.length}")
    println("Palindrom: ${if (bersih == bersih.reversed()) "ya" else "bukan"}")
}""",
    },
    {
        "title": "Latihan 8: Menghitung Frekuensi Kata",
        "difficulty": "Menengah",
        "question": [
            "Diberikan kalimat berikut di dalam kodemu:",
            "  \"kucing makan ikan kucing tidur ikan kucing\"",
            "",
            "Hitung berapa kali tiap kata muncul, lalu tampilkan terurut",
            "dari yang paling sering. Kalau jumlahnya sama, urutkan abjad.",
            "",
            "Keluaran yang diharapkan:",
            "",
            "  kucing : 3",
            "  ikan   : 2",
            "  makan  : 1",
            "  tidur  : 1",
            "  ---",
            "  Kata unik  : 4",
            "  Total kata : 7",
            "",
            "Nama kata rata kiri selebar 7 karakter.",
        ],
        "hints": [
            "Menghitung kemunculan adalah pekerjaan Map. Baca ulang materi \"Koleksi\", bagian groupingBy dan pengurutan.",
            "Pecah kalimat jadi List kata, hitung frekuensinya, lalu urutkan entri Map dengan dua kunci: jumlah menurun, lalu kata menaik. Kata unik adalah ukuran Map, total kata adalah ukuran List.",
            "groupingBy { it }.eachCount() menghitung frekuensi. Dua kunci urutan: sortedWith(compareByDescending<Map.Entry<String, Int>> { it.value }.thenBy { it.key }). Rata kiri selebar 7: padEnd(7).",
        ],
        "solution": """fun main() {
    val kalimat = "kucing makan ikan kucing tidur ikan kucing"
    val kata = kalimat.split(" ")
    val hitung = kata.groupingBy { it }.eachCount()

    hitung.entries
        .sortedWith(compareByDescending<Map.Entry<String, Int>> { it.value }
            .thenBy { it.key })
        .forEach { (k, n) -> println("${k.padEnd(7)}: $n") }

    println("---")
    println("Kata unik  : ${hitung.size}")
    println("Total kata : ${kata.size}")
}""",
    },
    {
        "title": "Latihan 9: Data Class & Null Safety",
        "difficulty": "Menengah",
        "question": [
            "Buat data class Alamat(val kota: String?, val pos: String?)",
            "dan data class Orang(val nama: String, val alamat: Alamat?).",
            "",
            "Buat fungsi ringkas(o: Orang): String yang menghasilkan",
            "\"<nama rata kiri 6><kota>\", dengan kota diganti",
            "\"tidak diketahui\" kalau alamatnya null ATAU kotanya null.",
            "",
            "Buat juga fungsi sapa(nama: String?): String yang",
            "mengembalikan \"(tanpa nama)\" kalau namanya null, kosong,",
            "atau hanya berisi spasi; selain itu \"Halo, <NAMA BESAR>!\"",
            "",
            "Uji sapa dengan: \"Andi\", null, \"\", \"  \", \"Budi\".",
            "Uji ringkas dengan Andi(Bandung/40111), Budi(null),",
            "dan Cici(Alamat(null, \"12345\")).",
            "",
            "Keluaran yang diharapkan:",
            "",
            "  [Halo, ANDI!]",
            "  [(tanpa nama)]",
            "  [(tanpa nama)]",
            "  [(tanpa nama)]",
            "  [Halo, BUDI!]",
            "  ---",
            "  Andi  Bandung",
            "  Budi  tidak diketahui",
            "  Cici  tidak diketahui",
        ],
        "hints": [
            "Latihan ini menguji safe call, operator Elvis, dan smart cast. Baca ulang materi \"Null Safety\" dan \"Data Class, Object & Sealed\".",
            "Di sapa, tangani null, string kosong, dan spasi saja dalam satu pengecekan, lalu kembalikan lebih awal. Sesudah itu compiler tahu nama pasti non-null. Di ringkas, rantai safe call dari orang ke kota, lalu beri nilai cadangan.",
            "isNullOrBlank() menangani null, kosong, dan spasi sekaligus. Rantai: o.alamat?.kota ?: \"tidak diketahui\". Nama rata kiri: padEnd(6).",
        ],
        "solution": """data class Alamat(val kota: String?, val pos: String?)
data class Orang(val nama: String, val alamat: Alamat?)

fun sapa(nama: String?): String {
    if (nama.isNullOrBlank()) return "(tanpa nama)"
    return "Halo, ${nama.trim().uppercase()}!"
}

fun ringkas(o: Orang): String =
    "${o.nama.padEnd(6)}${o.alamat?.kota ?: "tidak diketahui"}"

fun main() {
    val nama: List<String?> = listOf("Andi", null, "", "  ", "Budi")
    nama.forEach { println("[${sapa(it)}]") }

    println("---")
    val orang = listOf(
        Orang("Andi", Alamat("Bandung", "40111")),
        Orang("Budi", null),
        Orang("Cici", Alamat(null, "12345")),
    )
    orang.forEach { println(ringkas(it)) }
}""",
    },
    {
        "title": "Latihan 10: Interface, Abstract & Polimorfisme",
        "difficulty": "Lanjut",
        "question": [
            "Buat interface Bangun dengan `val nama: String`,",
            "`fun luas(): Double`, dan implementasi bawaan",
            "`fun ringkas(): String` berformat \"%-16s%8.2f\".",
            "",
            "Buat abstract class BangunDasar(override val nama: String)",
            "yang mengimplementasi Bangun.",
            "",
            "Turunkan Persegi(sisi), Lingkaran(jari) dengan PI = 3.14159",
            "yang MENIMPA ringkas() menjadi \"<bawaan>  (r=<jari>)\",",
            "dan PersegiPanjang(p, l).",
            "",
            "Masukkan Persegi(4.0), Lingkaran(3.0), PersegiPanjang(6.0, 3.0)",
            "ke satu List<Bangun>, telusuri sekali, lalu cetak totalnya.",
            "",
            "Keluaran yang diharapkan:",
            "",
            "  Persegi            16.00",
            "  Lingkaran          28.27  (r=3.0)",
            "  PersegiPanjang     18.00",
            "  TOTAL              62.27",
        ],
        "hints": [
            "Interface di Kotlin boleh punya method dengan badan (implementasi bawaan), dan class turunannya boleh menimpanya. Baca ulang materi \"Pewarisan & Interface\".",
            "Tulis ringkas() bawaan di interface Bangun. BangunDasar cukup menerima nama lewat override val. Tiap bentuk menimpa luas(); hanya Lingkaran yang juga menimpa ringkas() dan menambahkan \"  (r=...)\" di belakang versi bawaan. Simpan ketiganya di List<Bangun> lalu jumlahkan luasnya.",
            "Versi bawaan dipanggil dengan super.ringkas(). PI cocok ditaruh di companion object sebagai const val. Total: semua.sumOf { it.luas() }, dicetak dengan format \"%-16s%8.2f\" yang sama.",
        ],
        "solution": """interface Bangun {
    val nama: String
    fun luas(): Double
    fun ringkas(): String = "%-16s%8.2f".format(nama, luas())
}

abstract class BangunDasar(override val nama: String) : Bangun

class Persegi(private val sisi: Double) : BangunDasar("Persegi") {
    override fun luas() = sisi * sisi
}

class Lingkaran(private val jari: Double) : BangunDasar("Lingkaran") {
    companion object {
        const val PI = 3.14159
    }

    override fun luas() = PI * jari * jari
    override fun ringkas() = super.ringkas() + "  (r=$jari)"
}

class PersegiPanjang(private val p: Double, private val l: Double) :
    BangunDasar("PersegiPanjang") {
    override fun luas() = p * l
}

fun main() {
    val semua: List<Bangun> = listOf(
        Persegi(4.0),
        Lingkaran(3.0),
        PersegiPanjang(6.0, 3.0),
    )

    semua.forEach { println(it.ringkas()) }
    println("%-16s%8.2f".format("TOTAL", semua.sumOf { it.luas() }))
}""",
    },
    {
        "title": "Latihan 11: Sealed Class sebagai Hasil",
        "difficulty": "Lanjut",
        "question": [
            "Buat sealed class Hasil<out T> dengan dua turunan:",
            "  data class Ok<T>(val nilai: T) : Hasil<T>()",
            "  data class Salah(val pesan: String) : Hasil<Nothing>()",
            "",
            "Buat fungsi parseNilai(teks: String): Hasil<Int> yang:",
            "  - membuang spasi lalu mengurai jadi Int",
            "  - Salah(\"bukan angka: <teks>\") kalau gagal diurai",
            "  - Salah(\"di luar 0..100: <n>\") kalau di luar rentang",
            "",
            "Buat fungsi rataRata(semua: List<String>): Hasil<Double> yang",
            "membatalkan seluruh perhitungan kalau ada satu yang gagal.",
            "",
            "Uji parseNilai dengan: \"88\", \" 92 \", \"abc\", \"150\", \"-3\"",
            "lalu rataRata dengan [\"80\",\"90\",\"100\"] dan [\"80\",\"xx\",\"100\"].",
            "",
            "Keluaran yang diharapkan:",
            "",
            "     88 -> 88",
            "    92  -> 92",
            "    abc -> bukan angka: abc",
            "    150 -> di luar 0..100: 150",
            "     -3 -> di luar 0..100: -3",
            "  ---",
            "  baik  : 90.0",
            "  rusak : bukan angka: xx",
            "",
            "Teks masukan dicetak rata kanan selebar 5.",
        ],
        "hints": [
            "Sealed class cocok untuk hasil yang bisa sukses atau gagal, dan when atasnya diperiksa kelengkapannya oleh compiler. Baca ulang materi \"Data Class, Object & Sealed\" dan \"Exception & Penanganan Galat\".",
            "Di parseNilai: trim, coba ubah jadi Int tanpa melempar exception, kembalikan Salah kalau gagal, lalu cek rentangnya. Di rataRata: telusuri tiap teks dengan for dan langsung return Salah pertama yang ditemukan; kalau semua Ok, hitung rata-ratanya sebagai Double.",
            "toIntOrNull() menghasilkan null alih-alih melempar, jadi bisa disambung ?: return Hasil.Salah(...). when atas Hasil nggak butuh else kalau Ok dan Salah sudah ditulis. Teks masukan rata kanan selebar 5: padStart(5).",
        ],
        "solution": """sealed class Hasil<out T> {
    data class Ok<T>(val nilai: T) : Hasil<T>()
    data class Salah(val pesan: String) : Hasil<Nothing>()
}

fun parseNilai(teks: String): Hasil<Int> {
    val bersih = teks.trim()
    val n = bersih.toIntOrNull() ?: return Hasil.Salah("bukan angka: $bersih")
    if (n !in 0..100) return Hasil.Salah("di luar 0..100: $n")
    return Hasil.Ok(n)
}

fun rataRata(semua: List<String>): Hasil<Double> {
    var total = 0
    for (t in semua) {
        when (val h = parseNilai(t)) {
            is Hasil.Ok -> total += h.nilai
            is Hasil.Salah -> return h
        }
    }
    return Hasil.Ok(total.toDouble() / semua.size)
}

fun main() {
    for (t in listOf("88", " 92 ", "abc", "150", "-3")) {
        val pesan = when (val h = parseNilai(t)) {
            is Hasil.Ok -> "${h.nilai}"
            is Hasil.Salah -> h.pesan
        }
        println("${t.padStart(5)} -> $pesan")
    }

    println("---")
    for ((label, data) in listOf(
        "baik " to listOf("80", "90", "100"),
        "rusak" to listOf("80", "xx", "100"),
    )) {
        val pesan = when (val h = rataRata(data)) {
            is Hasil.Ok -> "${h.nilai}"
            is Hasil.Salah -> h.pesan
        }
        println("$label : $pesan")
    }
}""",
    },
    {
        "title": "Latihan 12: Rantai Koleksi",
        "difficulty": "Lanjut",
        "question": [
            "Buat data class Transaksi(barang, kategori, jumlah, harga)",
            "dengan properti terhitung `subtotal`.",
            "",
            "Isi dengan:",
            "  Kopi  Minuman  3  25000",
            "  Teh   Minuman  5  15000",
            "  Roti  Makanan  2  20000",
            "  Nasi  Makanan  4  30000",
            "  Jus   Minuman  1  35000",
            "",
            "Tampilkan semua terurut subtotal MENURUN; kalau sama, nama",
            "barang MENAIK. Lalu total, rekap per kategori terurut abjad,",
            "dan barang termahal.",
            "",
            "Keluaran yang diharapkan:",
            "",
            "  Nasi       Makanan     4 x  30000 =   120000",
            "  Kopi       Minuman     3 x  25000 =    75000",
            "  Teh        Minuman     5 x  15000 =    75000",
            "  Roti       Makanan     2 x  20000 =    40000",
            "  Jus        Minuman     1 x  35000 =    35000",
            "  ---",
            "  Total     : 345000",
            "  Makanan   : 160000 (2 transaksi)",
            "  Minuman   : 185000 (3 transaksi)",
            "  Termahal  : Nasi",
            "",
            "Kolom: barang rata kiri 11, kategori rata kiri 11, jumlah rata",
            "kanan 2, harga rata kanan 6, subtotal rata kanan 8.",
        ],
        "hints": [
            "Ini gabungan properti terhitung, pengurutan dua kunci, dan pengelompokan. Baca ulang materi \"Class, Properti & Constructor\" dan \"Koleksi\".",
            "Beri Transaksi properti subtotal yang dihitung dari jumlah dan harga lewat getter. Urutkan dengan subtotal menurun lalu nama barang menaik. Untuk rekap, kelompokkan per kategori dan urutkan kuncinya; untuk termahal, cari transaksi dengan subtotal terbesar.",
            "Properti terhitung memakai get() = ... sesudah tipenya. Dua kunci: compareByDescending<Transaksi> { it.subtotal }.thenBy { it.barang }. Rekap terurut: groupBy { it.kategori }.toSortedMap(). Terbesar: maxBy { it.subtotal }.",
        ],
        "solution": """data class Transaksi(
    val barang: String,
    val kategori: String,
    val jumlah: Int,
    val harga: Int,
) {
    val subtotal: Int get() = jumlah * harga
}

fun main() {
    val data = listOf(
        Transaksi("Kopi", "Minuman", 3, 25_000),
        Transaksi("Teh", "Minuman", 5, 15_000),
        Transaksi("Roti", "Makanan", 2, 20_000),
        Transaksi("Nasi", "Makanan", 4, 30_000),
        Transaksi("Jus", "Minuman", 1, 35_000),
    )

    data.sortedWith(
        compareByDescending<Transaksi> { it.subtotal }.thenBy { it.barang }
    ).forEach {
        println("%-11s%-11s%2d x %6d = %8d".format(
            it.barang, it.kategori, it.jumlah, it.harga, it.subtotal))
    }

    println("---")
    println("%-10s: %d".format("Total", data.sumOf { it.subtotal }))

    data.groupBy { it.kategori }.toSortedMap().forEach { (kategori, anggota) ->
        println("%-10s: %d (%d transaksi)".format(
            kategori, anggota.sumOf { it.subtotal }, anggota.size))
    }

    println("%-10s: %s".format("Termahal", data.maxBy { it.subtotal }.barang))
}""",
    },
    {
        "title": "Latihan 13: Scope Function & Extension",
        "difficulty": "Lanjut",
        "question": [
            "Buat class Setelan dengan var tema, ukuran, dan gerak,",
            "beserta toString berformat",
            "\"Setelan(tema=..., ukuran=..., gerak=...)\".",
            "",
            "Buat extension berikut:",
            "  fun String.rapikan(): String   -> trim lalu lowercase",
            "  fun Int.kuadrat(): Int",
            "  val List<Int>.ringkas: String  -> \"n=<size> min=<min> max=<max>\"",
            "  fun String?.atauKosong(): String -> \"\" kalau null",
            "",
            "Di main, tunjukkan berurutan:",
            "  1. apply untuk menyetel dua properti sekaligus",
            "  2. also untuk mencetak jumlah elemen di TENGAH rantai",
            "  3. let yang hanya jalan kalau bukan null",
            "  4. run untuk menghitung sesuatu dari objek",
            "  5. keempat extension di atas",
            "",
            "Keluaran yang diharapkan:",
            "",
            "  apply : Setelan(tema=gelap, ukuran=18, gerak=true)",
            "  also  : sesudah filter ada 5 elemen",
            "  hasil : [60, 70, 80, 90, 100]",
            "  let   : 12",
            "  run   : gelap/18",
            "  ---",
            "  rapikan : 'halo dunia'",
            "  kuadrat : 49",
            "  ringkas : n=4 min=1 max=9",
            "  kosong  : ''",
        ],
        "hints": [
            "Scope function seperti apply, also, let, dan run cuma beda di dua hal: penerimanya this atau it, dan yang dikembalikan objeknya atau hasil lambda. Baca ulang materi \"Lambda & Higher-Order Function\" dan \"Generic & Extension Lanjut\".",
            "apply cocok untuk menyetel properti lalu tetap memegang objeknya. also menyelipkan println di tengah rantai filter-map tanpa memutusnya. let dipanggil lewat ?. supaya cuma jalan kalau nilainya bukan null. run menghitung sesuatu dari objek dengan this.",
            "Extension property wajib punya getter: val List<Int>.ringkas: String get() = ... . Extension pada tipe nullable ditulis fun String?.atauKosong(), dan di dalamnya this boleh null, jadi this ?: \"\" sudah cukup.",
        ],
        "solution": """class Setelan {
    var tema: String = "terang"
    var ukuran: Int = 14
    var gerak: Boolean = true
    override fun toString() =
        "Setelan(tema=$tema, ukuran=$ukuran, gerak=$gerak)"
}

fun String.rapikan(): String = trim().lowercase()
fun Int.kuadrat(): Int = this * this
val List<Int>.ringkas: String get() = "n=$size min=${min()} max=${max()}"
fun String?.atauKosong(): String = this ?: ""

fun main() {
    val s = Setelan().apply {
        tema = "gelap"
        ukuran = 18
    }
    println("apply : $s")

    val hasil = (1..10).toList()
        .filter { it > 5 }
        .also { println("also  : sesudah filter ada ${it.size} elemen") }
        .map { it * 10 }
    println("hasil : $hasil")

    val mungkin: String? = "kotlin"
    println("let   : ${mungkin?.let { it.length * 2 } ?: 0}")
    println("run   : ${s.run { "$tema/$ukuran" }}")

    println("---")
    println("rapikan : '${"  HALO Dunia  ".rapikan()}'")
    println("kuadrat : ${7.kuadrat()}")
    println("ringkas : ${listOf(3, 9, 1, 7).ringkas}")
    println("kosong  : '${null.atauKosong()}'")
}""",
    },
    {
        "title": "Latihan 14: Generic & Reified",
        "difficulty": "Sulit",
        "question": [
            "Buat class generic Kotak<T>(muat: Int) dengan:",
            "  - val jumlah dan val penuh sebagai properti terhitung",
            "  - fun masuk(x: T): Boolean  (false kalau penuh)",
            "  - fun keluar(): T?          (ambil dari DEPAN)",
            "  - toString berbentuk \"[a, b] 2/3\"",
            "",
            "Buat juga:",
            "  fun <T : Comparable<T>> terbesar(d: List<T>): T?",
            "  inline fun <reified T> saringTipe(d: List<Any>): List<T>",
            "",
            "Di main, buktikan Kotak bekerja untuk Int dan String,",
            "terbesar bekerja untuk angka dan teks, dan saringTipe",
            "memisahkan Int dari String di dalam satu List<Any>.",
            "",
            "Keluaran yang diharapkan:",
            "",
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
            "  masuk apel: true",
            "  masuk jeruk: true",
            "  masuk mangga: false",
            "  [apel, jeruk] 2/2",
            "  ---",
            "  hanya Int    : [1, 5]",
            "  hanya String : [dua, empat]",
        ],
        "hints": [
            "Parameter tipe T membuat satu class bekerja untuk Int maupun String. Baca ulang materi \"Generic & Extension Lanjut\", bagian batas tipe (T : Comparable<T>) dan reified.",
            "Simpan isi Kotak di MutableList privat; jumlah dan penuh dihitung dari ukurannya. masuk menolak kalau penuh, keluar mengambil dari depan dan aman untuk list kosong. terbesar cukup memanggil fungsi max yang mengembalikan null untuk daftar kosong.",
            "reified cuma bisa dipakai bersama inline. Di dalam saringTipe, filterIsInstance<T>() menyaring berdasarkan tipe. removeFirstOrNull() dan maxOrNull() menangani kasus kosong tanpa exception.",
        ],
        "solution": """class Kotak<T>(private val muat: Int) {
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

fun <T : Comparable<T>> terbesar(d: List<T>): T? = d.maxOrNull()

inline fun <reified T> saringTipe(d: List<Any>): List<T> = d.filterIsInstance<T>()

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
    val buah = Kotak<String>(2)
    for (b in listOf("apel", "jeruk", "mangga")) println("masuk $b: ${buah.masuk(b)}")
    println(buah)

    println("---")
    val campur: List<Any> = listOf(1, "dua", 3.0, "empat", 5, true)
    println("hanya Int    : ${saringTipe<Int>(campur)}")
    println("hanya String : ${saringTipe<String>(campur)}")
}""",
    },
    {
        "title": "Latihan 15: Mesin Keadaan dengan Enum",
        "difficulty": "Sulit",
        "question": [
            "Buat enum class Keadaan { DRAF, DITINJAU, DISETUJUI, DITOLAK,",
            "TERBIT } dan enum class Aksi { KIRIM, SETUJUI, TOLAK,",
            "TERBITKAN, TARIK }.",
            "",
            "Buat fungsi lanjut(k: Keadaan, a: Aksi): Keadaan? yang",
            "mengembalikan keadaan baru kalau transisinya sah, atau null",
            "kalau tidak. Aturan transisi:",
            "  DRAF      + KIRIM     -> DITINJAU",
            "  DITINJAU  + SETUJUI   -> DISETUJUI",
            "  DITINJAU  + TOLAK     -> DITOLAK",
            "  DISETUJUI + TERBITKAN -> TERBIT",
            "  DITOLAK   + TARIK     -> DRAF",
            "",
            "Jalankan dari DRAF: KIRIM, TERBITKAN, SETUJUI, TOLAK,",
            "TERBITKAN, TARIK. Kalau ditolak, keadaannya TIDAK berubah.",
            "",
            "Keluaran yang diharapkan:",
            "",
            "  DRAF      + KIRIM      -> DITINJAU",
            "  DITINJAU  + TERBITKAN  -> DITOLAK: TERBITKAN tidak sah dari DITINJAU",
            "  DITINJAU  + SETUJUI    -> DISETUJUI",
            "  DISETUJUI + TOLAK      -> DITOLAK: TOLAK tidak sah dari DISETUJUI",
            "  DISETUJUI + TERBITKAN  -> TERBIT",
            "  TERBIT    + TARIK      -> DITOLAK: TARIK tidak sah dari TERBIT",
            "  ---",
            "  keadaan akhir: TERBIT",
            "",
            "Keadaan rata kiri 10, aksi rata kiri 11.",
        ],
        "hints": [
            "Enum memberi nama untuk tiap keadaan dan aksi, dan when bisa memetakan pasangan keadaan-aksi ke keadaan berikutnya. Baca ulang materi \"Kendali Alur\" dan \"Data Class, Object & Sealed\".",
            "lanjut mengembalikan Keadaan? : keadaan baru untuk lima transisi yang sah, null untuk sisanya. Di main, simpan keadaan di var, panggil lanjut untuk tiap aksi, dan perbarui var itu cuma kalau hasilnya bukan null. Cetak keadaan sebelum diperbarui di kolom pertama.",
            "when atas pasangan: when (k to a) { Keadaan.DRAF to Aksi.KIRIM -> Keadaan.DITINJAU ... else -> null }. Nama enum sebagai teks: .name. Kolom rata kiri: \"%-10s+ %-11s-> %s\".",
        ],
        "solution": """enum class Keadaan { DRAF, DITINJAU, DISETUJUI, DITOLAK, TERBIT }
enum class Aksi { KIRIM, SETUJUI, TOLAK, TERBITKAN, TARIK }

fun lanjut(k: Keadaan, a: Aksi): Keadaan? = when (k to a) {
    Keadaan.DRAF to Aksi.KIRIM -> Keadaan.DITINJAU
    Keadaan.DITINJAU to Aksi.SETUJUI -> Keadaan.DISETUJUI
    Keadaan.DITINJAU to Aksi.TOLAK -> Keadaan.DITOLAK
    Keadaan.DISETUJUI to Aksi.TERBITKAN -> Keadaan.TERBIT
    Keadaan.DITOLAK to Aksi.TARIK -> Keadaan.DRAF
    else -> null
}

fun main() {
    var keadaan = Keadaan.DRAF

    val urutan = listOf(
        Aksi.KIRIM, Aksi.TERBITKAN, Aksi.SETUJUI,
        Aksi.TOLAK, Aksi.TERBITKAN, Aksi.TARIK,
    )

    for (a in urutan) {
        val sebelum = keadaan
        val baru = lanjut(sebelum, a)
        val hasil = if (baru != null) {
            keadaan = baru
            baru.name
        } else {
            "DITOLAK: ${a.name} tidak sah dari ${sebelum.name}"
        }
        println("%-10s+ %-11s-> %s".format(sebelum.name, a.name, hasil))
    }

    println("---")
    println("keadaan akhir: ${keadaan.name}")
}""",
    },
    {
        "title": "Latihan 16: Proyek Akhir - Inventaris Gudang",
        "difficulty": "Sulit",
        "proyek": True,
        "question": [
            "Bangun sistem inventaris yang MEMISAHKAN tiga lapisan:",
            "model (data), layanan (aturan), dan antarmuka (cetak).",
            "",
            "MODEL",
            "  data class Barang(kode, nama, stok, harga) dengan properti",
            "  terhitung `subtotal` dan toString berformat",
            "  \"%-5s%-12s%2d%10d%12d\".",
            "  enum class Gerak { MASUK, KELUAR }",
            "  sealed class GalatGudang(val pesan: String) dengan turunan:",
            "    KodeSudahAda, KodeTidakDikenal, JumlahTidakSah,",
            "    StokTidakCukup. Pesannya:",
            "      \"kode B01 sudah ada\"",
            "      \"kode B09 tidak dikenal\"",
            "      \"jumlah 0 tidak sah\"",
            "      \"stok cuma 4, diminta 10\"",
            "  sealed class Hasil<out T> dengan Ok dan Salah.",
            "",
            "LAYANAN  class Gudang",
            "  - daftar(Barang): Hasil<Barang>",
            "  - catat(kode, Gerak, jumlah): Hasil<Int>",
            "    urutan periksa: kode dulu, lalu jumlah, baru kecukupan stok",
            "  - semua(): List<Barang> terurut kode",
            "  - nilaiPersediaan(): Long",
            "  - stokMenipis(batas): List<Barang> terurut stok naik lalu kode",
            "  Gudang TIDAK BOLEH memanggil println sama sekali.",
            "",
            "ANTARMUKA",
            "  Daftarkan B01 Kabel 10 15000, B02 Adaptor 4 85000,",
            "            B03 Mouse 25 120000",
            "  Jalankan: MASUK B01 15, KELUAR B02 10, KELUAR B03 5,",
            "            MASUK B09 1, KELUAR B03 0",
            "",
            "Keluaran yang diharapkan:",
            "",
            "  Masuk B01 15 -> stok 25",
            "  Keluar B02 10 -> DITOLAK: stok cuma 4, diminta 10",
            "  Keluar B03 5 -> stok 20",
            "  Masuk B09 1 -> DITOLAK: kode B09 tidak dikenal",
            "  Keluar B03 0 -> DITOLAK: jumlah 0 tidak sah",
            "  ---",
            "  B01  Kabel       25     15000      375000",
            "  B02  Adaptor      4     85000      340000",
            "  B03  Mouse       20    120000     2400000",
            "  ---",
            "  nilai persediaan: 3115000",
            "  stok menipis (<10): B02 Adaptor (4)",
        ],
        "hints": [
            "Proyek ini menyatukan data class, enum, sealed class, dan pemisahan lapisan. Baca ulang materi \"Proyek Utuh: Menggabungkan Semuanya\" dan \"Data Class, Object & Sealed\".",
            "Gudang menyimpan Barang di Map berkunci kode (linkedMapOf mempertahankan urutan penyisipan). Di catat, periksa berurutan: kode dikenal, jumlah lebih dari 0, lalu stok cukup; tiap kegagalan langsung return Salah. semua() tetap wajib mengurutkan menurut kode supaya keluarannya bisa diuji.",
            "data class nggak bisa diubah, jadi perbarui stok dengan copy(stok = baru). when atas Hasil nggak butuh else, dan compiler mengecek kelengkapannya. Label aksi: gerak.name.lowercase().replaceFirstChar { it.uppercase() } menghasilkan \"Masuk\" dari MASUK.",
        ],
        "solution": """// ---------------------------------------------------------------- MODEL
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
        if (baru < 0) return Hasil.Salah(GalatGudang.StokTidakCukup(b.stok, jumlah))

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
}""",
    },
]
