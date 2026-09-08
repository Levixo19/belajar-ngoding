GO_MATERIALS = [
    {
        "title": "1. Pengenalan Go & Instalasi",
        "sections": [
            {
                "body": [
                    "Apa itu Go?",
                    "  - Bahasa pemrograman buatan Google, dirilis tahun 2009.",
                    "  - Dirancang Robert Griesemer, Rob Pike, dan Ken Thompson.",
                    "  - Sering disebut 'Golang' karena situsnya dulu golang.org.",
                    "  - Compiled: kode diubah jadi satu file binari mandiri.",
                    "  - Statically typed: tipe diperiksa saat kompilasi.",
                    "",
                    "Kenapa Go dipakai banyak perusahaan:",
                    "  - Kompilasi sangat cepat, hitungan detik.",
                    "  - Hasilnya satu file binari, mudah dideploy tanpa runtime.",
                    "  - Concurrency (goroutine) mudah dan murah.",
                    "  - Sintaksnya sedikit, cepat dipelajari.",
                    "  - Garbage collector otomatis, tidak perlu atur memori manual.",
                    "",
                    "Dipakai membangun: Docker, Kubernetes, Terraform,",
                    "Prometheus, dan banyak layanan backend berskala besar.",
                    "",
                    "Instalasi:",
                    "  - Unduh dari https://go.dev/dl",
                    "  - Cek: go version",
                    "",
                    "Menjalankan program:",
                    "  go run program.go     kompilasi & jalankan sekali",
                    "  go build program.go   hasilkan file binari",
                ]
            },
            {
                "heading": "Program pertama",
                "code": """package main

import "fmt"

func main() {
	fmt.Println("Halo Dunia!")
	fmt.Println("Aku sedang belajar Go.")
}"""
            },
            {
                "body": [
                    "Penjelasan tiap bagian:",
                    "",
                    "  package main",
                    "    Setiap file Go milik sebuah package. Nama 'main' khusus:",
                    "    menandai program yang bisa dieksekusi.",
                    "",
                    "  import \"fmt\"",
                    "    Memuat package standar fmt (format) untuk input/output.",
                    "",
                    "  func main()",
                    "    Titik awal program. Wajib ada di package main.",
                    "",
                    "  fmt.Println(...)",
                    "    Cetak teks lalu pindah baris.",
                    "",
                    "Aturan penting Go:",
                    "  1. Tidak butuh titik koma di akhir baris.",
                    "  2. Kurung kurawal pembuka HARUS di baris yang sama.",
                    "     func main() {     BENAR",
                    "     func main()",
                    "     {                 SALAH, program tidak akan dikompilasi",
                    "  3. Import yang tidak dipakai adalah ERROR, bukan peringatan.",
                    "  4. Variabel lokal yang tidak dipakai juga ERROR.",
                    "  5. Indentasi resmi memakai TAB, dirapikan oleh gofmt.",
                    "",
                    "Aturan 3 dan 4 terasa galak di awal, tapi memaksa kode",
                    "tetap bersih tanpa sampah yang menumpuk.",
                    "",
                    "Dua pengecualian yang akan kamu temui di kode orang lain,",
                    "supaya nanti tidak bingung:",
                    "  - import berawalan garis bawah, import _ \"paket\", memang",
                    "    tidak pernah dipakai tapi tetap sah.",
                    "  - func init() dijalankan SEBELUM main tanpa pernah",
                    "    dipanggil siapa pun.",
                    "Keduanya dibedah di materi Module, Import & Direktif Compiler.",
                ]
            },
        ],
    },
    {
        "title": "2. Variabel, Konstanta & Tipe Data",
        "sections": [
            {
                "body": [
                    "Tiga cara membuat variabel:",
                    "",
                    "  var nama string = \"Andi\"     lengkap dengan tipe",
                    "  var nama = \"Andi\"            tipe ditebak dari nilai",
                    "  nama := \"Andi\"               bentuk singkat",
                    "",
                    "Bentuk := paling sering dipakai, TAPI hanya boleh di",
                    "dalam fungsi. Di level package wajib pakai var.",
                    "",
                    "Aturan := yang membingungkan di awal: sisi kiri BOLEH",
                    "memuat nama yang sudah ada, asalkan MINIMAL SATU nama di",
                    "situ masih baru. Yang lama cuma diisi ulang, yang baru",
                    "dibuat.",
                    "",
                    "  n, err := hitung()      n dan err sama-sama baru",
                    "  m, err := hitungLagi()  m baru, err diisi ulang -> sah",
                    "  n, err := hitung()      tidak ada nama baru sama sekali:",
                    "                          no new variables on left side of :=",
                    "",
                    "SHADOWING: variabel di dalam blok boleh MENUTUPI variabel",
                    "bernama sama di luarnya, dan compiler tidak mengeluh:",
                    "",
                    "  err := simpan()",
                    "  if err != nil {",
                    "      err := kirim(err)   err BARU, hidup di blok if saja",
                    "      fmt.Println(err)",
                    "  }",
                    "  // err di luar masih hasil simpan(), tak tersentuh",
                    "",
                    "Bentuk 'if err := f(); err != nil' juga selalu membuat err",
                    "yang benar-benar baru. Inilah sumber bug klasik 'kenapa",
                    "error-ku hilang': yang diperiksa di luar ternyata err lain.",
                    "",
                    "Nilai bawaan (zero value) kalau tidak diisi:",
                    "  angka   -> 0",
                    "  string  -> \"\" (kosong)",
                    "  bool    -> false",
                    "  pointer, slice, map -> nil",
                    "",
                    "Go TIDAK punya nilai 'undefined'. Semua variabel selalu",
                    "punya nilai yang jelas sejak dibuat.",
                    "",
                    "Konstanta memakai const, nilainya harus diketahui",
                    "saat kompilasi:",
                    "  const Pi = 3.14159",
                    "  const NamaApp = \"Belajar Go\"",
                    "",
                    "Beberapa const boleh dikumpulkan dalam satu blok, sejajar",
                    "dengan blok var ( ... ) di kode bawah:",
                    "  const (",
                    "      Pi      = 3.14159",
                    "      NamaApp = \"Belajar Go\"",
                    "  )",
                    "Blok const berisi nama TANPA nilai di sebelahnya adalah",
                    "pola tersendiri (iota), dibahas di materi Tipe Bentukan,",
                    "Konstanta Berkelompok & iota.",
                ]
            },
            {
                "heading": "Tipe data dasar",
                "code": """package main

import "fmt"

func main() {
	var umur int = 25
	var tinggi float64 = 170.5
	var nama string = "Andi"
	var aktif bool = true
	var huruf rune = 'A'
	var data byte = 255

	fmt.Println(umur, tinggi, nama, aktif)
	fmt.Println(huruf, string(huruf), data)

	// Bentuk singkat
	kota := "Jakarta"
	jumlah := 10
	rata := 8.5

	fmt.Printf("%s %d %.1f\\n", kota, jumlah, rata)

	// Deklarasi banyak sekaligus
	var (
		x = 1
		y = 2
	)
	a, b := 3, 4
	fmt.Println(x, y, a, b)
}"""
            },
            {
                "body": [
                    "Daftar tipe dasar:",
                    "",
                    "  Bilangan bulat:",
                    "    int, int8, int16, int32, int64",
                    "    uint, uint8, uint16, uint32, uint64  (tanpa negatif)",
                    "    Pakai 'int' saja kecuali ada alasan khusus.",
                    "",
                    "  Desimal:",
                    "    float32, float64",
                    "    Pakai float64 sebagai bawaan.",
                    "",
                    "  Lainnya:",
                    "    string   teks, tidak bisa diubah isinya",
                    "    bool     true atau false",
                    "    byte     alias uint8, untuk data mentah",
                    "    rune     alias int32, untuk satu karakter Unicode",
                    "",
                    "KONVERSI TIPE HARUS EKSPLISIT.",
                    "Go tidak pernah mengubah tipe diam-diam:",
                    "",
                    "  var a int = 5",
                    "  var b float64 = a          SALAH, tidak dikompilasi",
                    "  var b float64 = float64(a) BENAR",
                    "",
                    "Ini mencegah bug halus akibat konversi tak sengaja.",
                    "",
                    "Konversi angka dan teks butuh package strconv:",
                    "  n, err := strconv.Atoi(\"123\")   teks -> int",
                    "  s := strconv.Itoa(123)          int -> teks",
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
                    "  +  tambah        -  kurang",
                    "  *  kali          /  bagi",
                    "  %  sisa bagi (hanya untuk bilangan bulat)",
                    "",
                    "PENTING soal pembagian:",
                    "  7 / 2       -> 3     kedua operand int, hasilnya int",
                    "  7.0 / 2.0   -> 3.5   operand float, hasilnya float",
                    "  float64(7) / float64(2) -> 3.5",
                    "",
                    "Go TIDAK punya operator ++ dan -- sebagai ekspresi.",
                    "  i++ adalah PERNYATAAN, berdiri sendiri di satu baris.",
                    "  x := i++      SALAH",
                    "  i++           BENAR",
                    "  Tidak ada ++i sama sekali.",
                    "",
                    "Operator penugasan:",
                    "  =   +=   -=   *=   /=   %=",
                    "",
                    "Operator perbandingan (hasilnya bool):",
                    "  ==  !=  <  <=  >  >=",
                    "",
                    "Operator logika:",
                    "  &&  DAN     ||  ATAU     !  NOT",
                    "  Keduanya short-circuit: berhenti menilai begitu",
                    "  hasilnya sudah pasti.",
                ]
            },
            {
                "heading": "Contoh",
                "code": """package main

import "fmt"

func main() {
	a, b := 15, 4

	fmt.Println("Tambah :", a+b)
	fmt.Println("Kurang :", a-b)
	fmt.Println("Kali   :", a*b)
	fmt.Println("Bagi   :", a/b)
	fmt.Println("Sisa   :", a%b)

	// Pembagian desimal butuh konversi
	fmt.Printf("Desimal: %.2f\\n", float64(a)/float64(b))

	// Perbandingan
	fmt.Println(a > b, a == b, a != b)

	// Logika
	nilai := 85
	hadir := true
	fmt.Println("Lulus:", nilai >= 75 && hadir)

	// Increment sebagai pernyataan
	hitung := 0
	hitung++
	hitung += 10
	fmt.Println("Hitung:", hitung)
}"""
            },
            {
                "body": [
                    "Operator bitwise (untuk manipulasi bit):",
                    "  &   AND        |   OR",
                    "  ^   XOR        &^  AND NOT (bit clear)",
                    "  <<  geser kiri   >>  geser kanan",
                    "",
                    "  8 >> 1  -> 4    (sama dengan bagi 2)",
                    "  8 << 1  -> 16   (sama dengan kali 2)",
                    "",
                    "Urutan prioritas dari tinggi ke rendah:",
                    "  1.  *  /  %  <<  >>  &  &^",
                    "  2.  +  -  |  ^",
                    "  3.  ==  !=  <  <=  >  >=",
                    "  4.  &&",
                    "  5.  ||",
                    "",
                    "Kalau ragu, pakai kurung. Kode yang jelas lebih penting",
                    "daripada menghafal tabel prioritas.",
                    "",
                    "Go TIDAK punya operator ternary (kondisi ? a : b).",
                    "Selalu tulis if-else biasa. Ini disengaja supaya kode",
                    "tetap mudah dibaca.",
                ]
            },
        ],
    },
    {
        "title": "4. Angka & Waktu: math, time & strconv",
        "sections": [
            {
                "body": [
                    "Operator + - * / % dari materi sebelumnya cuma menutup hitungan",
                    "paling dasar. Begitu butuh akar, pangkat, atau pembulatan,",
                    "alatnya ada di package math.",
                    "",
                    "  import \"math\"",
                    "",
                    "Yang paling sering dipakai:",
                    "  math.Sqrt(x)     akar kuadrat",
                    "  math.Pow(x, y)   x pangkat y",
                    "  math.Abs(x)      nilai mutlak, tanda minus dibuang",
                    "  math.Floor(x)    bulatkan ke BAWAH     3.9 -> 3",
                    "  math.Ceil(x)     bulatkan ke ATAS      3.1 -> 4",
                    "  math.Round(x)    bulatkan terdekat     3.5 -> 4",
                    "  math.Trunc(x)    potong komanya       -3.9 -> -3",
                    "  math.Mod(x, y)   sisa bagi desimal (% hanya untuk int)",
                    "",
                    "Konstanta yang sudah disiapkan:",
                    "  math.Pi          3.141592653589793",
                    "  math.MaxInt64    bilangan int64 terbesar",
                    "  math.MaxFloat64  float64 terbesar",
                    "",
                    "math.Pi inilah asal rumus luas lingkaran (math.Pi * r * r)",
                    "yang nanti muncul di materi Interface dan latihannya.",
                    "",
                    "JEBAKAN TERBESARNYA: semua fungsi math menerima dan",
                    "mengembalikan float64. Tidak ada versi int-nya.",
                    "",
                    "  n := 81",
                    "  math.Sqrt(n)            SALAH, gagal DIKOMPILASI",
                    "  math.Sqrt(float64(n))   BENAR",
                    "",
                    "Pesan compilernya persis begini:",
                    "  cannot use n (variable of type int) as float64 value",
                    "  in argument to math.Sqrt",
                    "",
                    "Ini aturan 'konversi harus eksplisit' dari Materi 2 yang",
                    "sedang menagih janjinya. Hasilnya pun float64. Mau balik",
                    "ke int? int(3.9) MEMOTONG jadi 3, bukan membulatkan.",
                    "Kalau maunya membulatkan: int(math.Round(3.9)).",
                    "",
                    "Tiga builtin yang tidak perlu import apa pun (Go 1.21+):",
                    "  min(a, b, ...)  nilai terkecil",
                    "  max(a, b, ...)  nilai terbesar",
                    "  clear(m)        kosongkan map (dibahas di materi Map)",
                    "",
                    "math.Min dan math.Max masih ada tapi hanya melayani float64.",
                    "Builtin min dan max menerima int, float, bahkan string.",
                ],
            },
            {
                "heading": "Hitungan dengan math",
                "code": """package main

import (
	"fmt"
	"math"
)

func main() {
	// Semua fungsi math bekerja pada float64
	fmt.Println("Akar 144    :", math.Sqrt(144))
	fmt.Println("2 pangkat 10:", math.Pow(2, 10))
	fmt.Println("Nilai mutlak:", math.Abs(-7.5))

	// Angka bertipe int WAJIB dikonversi lebih dulu
	n := 81
	fmt.Println("Akar dari n :", math.Sqrt(float64(n)))

	harga := 12345.678
	fmt.Println("Floor:", math.Floor(harga))
	fmt.Println("Ceil :", math.Ceil(harga))
	fmt.Println("Round:", math.Round(harga))

	// Membulatkan ke 2 angka di belakang koma
	fmt.Printf("Dua desimal: %.2f\\n", math.Round(harga*100)/100)

	// math.Pi, konstanta yang dipakai rumus lingkaran
	jari := 7.0
	fmt.Printf("Luas lingkaran: %.2f\\n", math.Pi*jari*jari)

	// Sisa bagi untuk desimal, karena % hanya untuk bilangan bulat
	fmt.Println("Mod 10.5 % 3:", math.Mod(10.5, 3))

	// Batas tipe
	fmt.Println("int64 terbesar:", int64(math.MaxInt64))

	// min, max, clear: builtin sejak Go 1.21, tanpa import apa pun
	fmt.Println("min:", min(4, 9), " max:", max(4, 9))
	fmt.Println("min tiga nilai:", min(2.5, 1.25, 9.0))

	// float64 tidak pernah tepat
	a := 0.1
	b := 0.2
	fmt.Println(a+b, a+b == 0.3)
}""",
            },
            {
                "heading": "Pecahan yang meleset, dan strconv",
                "body": [
                    "KENAPA 0.1 + 0.2 BUKAN 0.3",
                    "",
                    "float64 menyimpan pecahan dalam basis dua. Angka 0.1 tidak",
                    "bisa ditulis pas di basis dua, persis seperti 1/3 tidak bisa",
                    "ditulis pas di basis sepuluh. Yang tersimpan selalu nilai",
                    "TERDEKAT, bukan angka yang kamu ketik.",
                    "",
                    "  a := 0.1",
                    "  b := 0.2",
                    "  a + b       -> 0.30000000000000004",
                    "  a+b == 0.3  -> false",
                    "",
                    "Anehnya 0.1 + 0.2 == 0.3 yang ditulis LANGSUNG malah true:",
                    "konstanta dihitung compiler dengan presisi tinggi sebelum",
                    "program jalan. Jebakannya baru kelihatan lewat variabel.",
                    "",
                    "Dua akibat yang harus kamu pegang:",
                    "  - Jangan bandingkan float dengan ==. Bandingkan selisihnya:",
                    "      math.Abs(x-y) < 0.000001",
                    "  - JANGAN simpan uang sebagai float64. Setelah ribuan",
                    "    penjumlahan saldonya meleset beberapa sen, dan tidak ada",
                    "    yang sanggup menjelaskan ke mana perginya. Simpan dalam",
                    "    satuan terkecil sebagai int, lalu bagi hanya saat",
                    "    MENAMPILKAN:  harga := 19999   // rupiah utuh",
                    "",
                    "TEKS <-> ANGKA: package strconv",
                    "",
                    "Materi 2 sudah menyebut Atoi dan Itoa. Selengkapnya:",
                    "  strconv.ParseFloat(s, 64)           teks -> float64",
                    "  strconv.ParseInt(s, basis, 64)      teks -> int64",
                    "  strconv.ParseBool(\"true\")            teks -> bool",
                    "  strconv.FormatFloat(f, 'f', 2, 64)  float64 -> teks",
                    "  strconv.FormatInt(255, 16)          int64 -> teks basis 16",
                    "  strconv.Quote(s)                    bungkus jadi literal Go",
                    "",
                    "Basis di ParseInt: 2 biner, 8 oktal, 10 biasa, 16 heksa.",
                    "Angka 64 di belakangnya berarti hasilnya harus muat di 64 bit.",
                    "",
                    "Semua fungsi Parse mengembalikan DUA nilai: hasil dan err.",
                    "Kalau teksnya bukan angka, hasilnya 0 dan err berisi alasannya.",
                    "Untuk input yang datang dari pengguna, jangan pernah buang err",
                    "itu dengan _.",
                    "",
                    "JEBAKAN: string(65) bukan \"65\", melainkan \"A\". Konversi tipe",
                    "bukan pemformatan: 65 dibaca sebagai nomor karakter Unicode.",
                    "Untuk mengubah angka jadi teks pakai strconv.Itoa(65) atau",
                    "fmt.Sprintf(\"%d\", 65).",
                ],
                "code": """package main

import (
	"fmt"
	"strconv"
)

func main() {
	// Teks -> angka. Selalu ada err, karena teks bisa saja bukan angka.
	umur, err := strconv.Atoi("25")
	fmt.Println(umur, err)

	rusak, err := strconv.Atoi("25 tahun")
	fmt.Println(rusak, err)

	harga, _ := strconv.ParseFloat("19999.5", 64)
	fmt.Println(harga + 0.5)

	// ParseInt dengan basis: 2 biner, 16 heksadesimal, 10 desimal biasa
	biner, _ := strconv.ParseInt("1011", 2, 64)
	heks, _ := strconv.ParseInt("ff", 16, 64)
	fmt.Println(biner, heks)

	// Angka -> teks
	fmt.Println(strconv.Itoa(2024) + " Masehi")
	fmt.Println(strconv.FormatFloat(3.14159, 'f', 2, 64))
	fmt.Println(strconv.FormatInt(255, 16))
	fmt.Println(strconv.FormatBool(true) + "!")

	// Quote membungkus teks jadi literal Go, escape ikut terlihat
	fmt.Println(strconv.Quote("baris\\nbaru"))

	// JEBAKAN: string(65) BUKAN "65"
	kode := 65
	fmt.Println(string(rune(kode)))
	fmt.Println(strconv.Itoa(kode))
	fmt.Println(fmt.Sprintf("kode-%d", kode))
}""",
            },
            {
                "heading": "Waktu dengan package time",
                "body": [
                    "LAYOUT TANGGAL: angkanya 1 2 3 4 5 6",
                    "",
                    "Go tidak mengenal \"YYYY-MM-DD\". Format ditulis dengan MENULIS",
                    "ULANG satu tanggal acuan yang sama untuk semua orang:",
                    "",
                    "  Mon Jan 2 15:04:05 MST 2006",
                    "",
                    "Angka-angkanya berurutan, dan itu memang disengaja supaya",
                    "gampang diingat:",
                    "  1  bulan   Jan / January / 01",
                    "  2  hari    2 / 02 / Monday",
                    "  3  jam     3 (12 jam), atau 15 untuk format 24 jam,",
                    "             karena jam acuannya jam 3 sore alias 15.00",
                    "  4  menit   4 / 04",
                    "  5  detik   5 / 05",
                    "  6  tahun   06 / 2006",
                    "",
                    "Jadi \"2006-01-02\" berarti tahun-bulan-hari, dan \"02/01/2006\"",
                    "berarti hari/bulan/tahun. Nol di depan ikut ditiru: \"01\"",
                    "memaksa dua digit, \"1\" membiarkan apa adanya.",
                    "",
                    "Menulis t.Format(\"YYYY-MM-DD\") TIDAK menghasilkan error;",
                    "keluarannya cuma teks YYYY-MM-DD apa adanya. Inilah jebakan",
                    "favorit pendatang dari bahasa lain: tidak ada yang menegur,",
                    "hanya hasilnya yang salah.",
                    "",
                    "time.Parse memakai layout yang sama dan galak soal kecocokan:",
                    "  time.Parse(\"2006-01-02\", \"01/03/2026\")",
                    "  -> cannot parse \"01/03/2026\" as \"2006\"",
                ],
                "code": """package main

import (
	"fmt"
	"time"
)

func main() {
	// Membuat waktu tertentu. Bulan bukan angka biasa: time.Month.
	merdeka := time.Date(1945, time.August, 17, 10, 0, 0, 0, time.UTC)

	fmt.Println("Tahun  :", merdeka.Year())
	fmt.Println("Bulan  :", merdeka.Month())
	fmt.Println("Tanggal:", merdeka.Day())
	fmt.Println("Hari   :", merdeka.Weekday())

	// Format memakai TANGGAL ACUAN, bukan YYYY-MM-DD
	fmt.Println(merdeka.Format("2006-01-02 15:04:05"))
	fmt.Println(merdeka.Format("02/01/2006"))
	fmt.Println(merdeka.Format("Monday, 02 January 2006"))

	// Membaca tanggal dari teks: layout harus cocok persis
	tenggat, err := time.Parse("2006-01-02", "2026-03-01")
	if err != nil {
		fmt.Println("Format tanggal salah:", err)
		return
	}

	// Menggeser waktu
	seminggu := 7 * 24 * time.Hour
	fmt.Println("Seminggu lagi:", tenggat.Add(seminggu).Format("2006-01-02"))
	fmt.Println("Sebulan lagi :", tenggat.AddDate(0, 1, 0).Format("2006-01-02"))

	// Selisih dua waktu menghasilkan Duration
	selisih := tenggat.Sub(merdeka)
	fmt.Printf("Jaraknya %.0f hari\\n", selisih.Hours()/24)
	fmt.Println("merdeka sebelum tenggat?", merdeka.Before(tenggat))

	// Duration itu tipe angka bernama, jadi 200 * time.Millisecond sah
	jeda := 200 * time.Millisecond
	fmt.Println("Jeda:", jeda, "=", jeda.Seconds(), "detik")

	mulai := time.Now()
	time.Sleep(jeda)
	fmt.Println("Sudah lewat jeda?", time.Since(mulai) >= jeda)
}""",
            },
            {
                "body": [
                    "DURATION ITU ANGKA BERNAMA",
                    "",
                    "time.Duration bukan struct, melainkan int64 berisi jumlah",
                    "NANODETIK dengan tipe sendiri. Itu sebabnya 5 * time.Second",
                    "sah ditulis: yang terjadi cuma angka dikali angka.",
                    "",
                    "  time.Nanosecond  Microsecond  Millisecond",
                    "  time.Second      Minute       Hour",
                    "  jeda := 300 * time.Millisecond",
                    "  jeda.Seconds()      -> 0.3",
                    "  fmt.Println(jeda)   -> 300ms, dicetak rapi bukan angka",
                    "  time.Sleep(2 * time.Second)   menghentikan program 2 detik",
                    "",
                    "Tapi variabel int tidak ikut kebagian:",
                    "  detik := 5",
                    "  detik * time.Second   SALAH",
                    "  -> mismatched types int and time.Duration",
                    "  time.Duration(detik) * time.Second   BENAR",
                    "",
                    "Sisanya yang sering dipakai:",
                    "  time.Now()         waktu sekarang",
                    "  time.Since(mulai)  Duration sejak mulai, untuk mengukur",
                    "  t.Before(t2)       mana yang lebih dulu; pasangannya t.After",
                    "  t.Unix()           detik sejak 1 Januari 1970",
                    "  t.Equal(t2)        bandingkan dengan ini, JANGAN dengan ==,",
                    "                     karena time.Time menyimpan zona waktu dan",
                    "                     jam monotonik yang ikut dibandingkan",
                    "",
                    "CATATAN KHUSUS APLIKASI INI: time.Now() membuat keluaran",
                    "berubah setiap kali dijalankan. Jangan memakainya di solusi",
                    "latihan yang dinilai otomatis. Kunci jawabannya diturunkan",
                    "dengan menjalankan solusi, jadi hasilmu tidak akan pernah",
                    "cocok. Pakai time.Date dengan tanggal tetap.",
                ],
            },
        ],
    },
    {
        "title": "5. Input & Output dengan fmt",
        "sections": [
            {
                "body": [
                    "Package fmt menyediakan fungsi output utama:",
                    "",
                    "  fmt.Print(...)    cetak tanpa baris baru",
                    "  fmt.Println(...)  cetak lalu pindah baris,",
                    "                    argumen dipisah spasi otomatis",
                    "  fmt.Printf(...)   cetak dengan format khusus",
                    "  fmt.Sprintf(...)  sama seperti Printf tapi hasilnya",
                    "                    dikembalikan sebagai string",
                    "",
                    "Namanya bukan acak. Ada tiga awalan yang berpasangan:",
                    "  tanpa awalan  Print   Println   Printf   -> ke layar",
                    "  awalan S      Sprint  Sprintln  Sprintf  -> jadi string",
                    "  awalan F      Fprint  Fprintln  Fprintf  -> ke tujuan lain",
                    "",
                    "Yang berawalan F minta TUJUAN sebagai argumen pertama:",
                    "  fmt.Fprintln(os.Stderr, \"gagal:\", err)",
                    "Tujuannya boleh apa saja yang bisa ditulisi, termasuk",
                    "berkas. Pesan error memang sebaiknya ke os.Stderr, supaya",
                    "tidak tercampur dengan keluaran asli programmu.",
                    "",
                    "Masih sekeluarga: fmt.Errorf, yang bekerja persis seperti",
                    "Sprintf tapi hasilnya sebuah error, bukan string. Itu yang",
                    "dipakai terus-menerus di materi Error Handling.",
                    "",
                    "Kata kerja format (verb) untuk Printf:",
                    "  %d   bilangan bulat",
                    "  %s   string",
                    "  %f   desimal        %.2f  desimal 2 angka",
                    "  %t   boolean",
                    "  %v   nilai apa pun dalam bentuk bawaan",
                    "  %+v  seperti %v tapi struct disertai nama field",
                    "  %T   tampilkan TIPE datanya",
                    "  %q   string dengan tanda petik",
                    "  %%   karakter persen literal",
                    "",
                    "Verb lain yang akan kamu temui di kode nyata:",
                    "  %c   satu karakter dari kode angkanya (rune)",
                    "  %U   kode Unicode-nya, 'A' -> U+0041",
                    "  %x   heksadesimal huruf kecil, %X huruf besar",
                    "       dipakai untuk hash dan isi byte: 255 -> ff",
                    "  %b   biner, %o oktal",
                    "  %e   notasi ilmiah, 1500.0 -> 1.500000e+03",
                    "  %g   otomatis: %e untuk angka ekstrem, %f untuk sisanya",
                    "  %p   alamat pointer",
                    "  %#v  bentuk siap tempel ke kode, paling enak buat debug",
                    "       Titik{1, 2} -> main.Titik{X:1, Y:2}",
                    "",
                    "Mengatur lebar kolom:",
                    "  %5d    rata kanan selebar 5",
                    "  %-10s  rata kiri selebar 10",
                    "  %08.2f lebar 8, 2 desimal, diisi nol di depan",
                ]
            },
            {
                "heading": "Membaca input",
                "code": """package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	pembaca := bufio.NewReader(os.Stdin)

	fmt.Print("Nama: ")
	nama, _ := pembaca.ReadString('\\n')
	nama = strings.TrimSpace(nama)

	fmt.Print("Umur: ")
	teksUmur, _ := pembaca.ReadString('\\n')
	umur, err := strconv.Atoi(strings.TrimSpace(teksUmur))
	if err != nil {
		fmt.Println("Umur harus angka")
		return
	}

	fmt.Printf("Halo %s, umurmu %d tahun.\\n", nama, umur)
	fmt.Printf("Tahun depan kamu %d tahun.\\n", umur+1)
}"""
            },
            {
                "body": [
                    "Tiga cara membaca input, pilih sesuai kebutuhan:",
                    "",
                    "1. fmt.Scan / fmt.Scanln  - paling singkat",
                    "     var n int",
                    "     fmt.Scan(&n)",
                    "   Tanda & wajib: fungsi butuh ALAMAT variabel supaya",
                    "   bisa mengubah isinya.",
                    "   Kelemahan: berhenti di spasi, jadi tidak cocok untuk",
                    "   membaca kalimat.",
                    "",
                    "2. bufio.NewReader(os.Stdin).ReadString('\\n')",
                    "   Membaca sampai akhir baris, termasuk spasi.",
                    "   Hasilnya masih mengandung karakter newline, jadi",
                    "   WAJIB dibersihkan dengan strings.TrimSpace.",
                    "",
                    "3. bufio.NewScanner(os.Stdin)",
                    "     pemindai := bufio.NewScanner(os.Stdin)",
                    "     for pemindai.Scan() {",
                    "         baris := pemindai.Text()",
                    "     }",
                    "   Paling cocok untuk membaca banyak baris sampai habis.",
                    "",
                    "Tanda garis bawah _ pada 'nama, _ := ...' disebut blank",
                    "identifier. Artinya: nilai kedua sengaja diabaikan.",
                    "Ini perlu karena Go melarang variabel tak terpakai.",
                ]
            },
        ],
    },
    {
        "title": "6. Percabangan (if & switch)",
        "sections": [
            {
                "body": [
                    "Bentuk if di Go:",
                    "",
                    "  if kondisi {",
                    "      ...",
                    "  } else if kondisiLain {",
                    "      ...",
                    "  } else {",
                    "      ...",
                    "  }",
                    "",
                    "Perbedaan dari C/Java:",
                    "  - Kondisi TIDAK dibungkus kurung biasa.",
                    "      if x > 5 {        BENAR",
                    "      if (x > 5) {      jalan, tapi tidak idiomatis",
                    "  - Kurung kurawal WAJIB, walau isinya satu baris.",
                    "  - Kondisi harus bertipe bool. Angka bukan kondisi.",
                    "      if 1 { }          SALAH di Go",
                    "  - 'else' harus di baris yang sama dengan } penutup.",
                    "",
                    "Fitur khas Go: pernyataan pendek sebelum kondisi.",
                    "",
                    "  if n, err := strconv.Atoi(teks); err == nil {",
                    "      fmt.Println(\"Angka:\", n)",
                    "  }",
                    "",
                    "Variabel n dan err hanya hidup di dalam blok if itu.",
                    "Pola ini sangat umum untuk menangani error.",
                ]
            },
            {
                "heading": "if dan switch",
                "code": """package main

import "fmt"

func main() {
	nilai := 85

	if nilai >= 85 {
		fmt.Println("Grade A")
	} else if nilai >= 75 {
		fmt.Println("Grade B")
	} else if nilai >= 60 {
		fmt.Println("Grade C")
	} else {
		fmt.Println("Tidak Lulus")
	}

	// switch tanpa break
	hari := 3
	switch hari {
	case 1:
		fmt.Println("Senin")
	case 2:
		fmt.Println("Selasa")
	case 3:
		fmt.Println("Rabu")
	case 6, 7:
		fmt.Println("Akhir pekan")
	default:
		fmt.Println("Hari tidak dikenal")
	}

	// switch tanpa ekspresi, pengganti if berantai
	switch {
	case nilai >= 85:
		fmt.Println("Sangat Baik")
	case nilai >= 75:
		fmt.Println("Baik")
	default:
		fmt.Println("Perlu Belajar Lagi")
	}
}"""
            },
            {
                "body": [
                    "Keunggulan switch di Go:",
                    "",
                    "  1. TIDAK perlu break. Setiap case otomatis berhenti",
                    "     setelah selesai. Ini kebalikan dari C/Java yang",
                    "     rawan bug 'fallthrough' tak sengaja.",
                    "",
                    "  2. Satu case boleh menampung beberapa nilai:",
                    "       case 6, 7:",
                    "",
                    "  3. switch tanpa ekspresi = if-else berantai yang rapi:",
                    "       switch {",
                    "       case nilai >= 85:",
                    "       }",
                    "",
                    "  4. Kalau memang butuh lanjut ke case berikutnya,",
                    "     tulis eksplisit:",
                    "       case 1:",
                    "           fmt.Println(\"satu\")",
                    "           fallthrough",
                    "",
                    "  5. Bisa juga pakai pernyataan pendek:",
                    "       switch hari := time.Now().Weekday(); hari {",
                    "       case time.Saturday, time.Sunday:",
                    "           fmt.Println(\"Libur\")",
                    "       }",
                    "     Butuh import \"time\" yang sudah kamu pakai di materi",
                    "     Angka & Waktu.",
                    "",
                    "  6. Type switch untuk memeriksa tipe di balik interface:",
                    "       switch v := x.(type) {",
                    "       case int:    fmt.Println(\"int:\", v)",
                    "       case string: fmt.Println(\"string:\", v)",
                    "       }",
                    "     Interface dan bentuk x.(type) dibahas tuntas di materi",
                    "     Interface. Di sini cukup kenali bentuk switch-nya saja;",
                    "     kamu belum melewatkan apa pun.",
                ]
            },
        ],
    },
    {
        "title": "7. Perulangan (for)",
        "sections": [
            {
                "body": [
                    "Go hanya punya SATU kata kunci perulangan: for.",
                    "Tidak ada while, tidak ada do-while.",
                    "Tapi for punya empat bentuk yang menutupi semuanya.",
                    "",
                    "1. Bentuk lengkap (seperti for di C):",
                    "     for i := 0; i < 10; i++ {",
                    "     }",
                    "",
                    "2. Bentuk kondisi saja (perannya seperti while):",
                    "     for i < 10 {",
                    "         i++",
                    "     }",
                    "",
                    "3. Tanpa apa pun (perulangan tak berhingga):",
                    "     for {",
                    "         if selesai { break }",
                    "     }",
                    "",
                    "4. Bentuk range (menelusuri koleksi):",
                    "     for indeks, nilai := range slice {",
                    "     }",
                    "",
                    "Sama seperti if, kondisi for tidak dibungkus kurung biasa.",
                ]
            },
            {
                "heading": "Empat bentuk for",
                "code": """package main

import "fmt"

func main() {
	// Bentuk lengkap
	total := 0
	for i := 1; i <= 10; i++ {
		total += i
	}
	fmt.Println("Jumlah 1..10 =", total)

	// Seperti while
	n := 5
	for n > 0 {
		fmt.Print(n, " ")
		n--
	}
	fmt.Println()

	// Tak berhingga dengan break
	hitung := 0
	for {
		hitung++
		if hitung >= 3 {
			break
		}
	}
	fmt.Println("Berhenti di", hitung)

	// range pada slice
	buah := []string{"apel", "jeruk", "mangga"}
	for i, b := range buah {
		fmt.Printf("%d: %s\\n", i, b)
	}

	// range hanya nilai, indeks diabaikan
	for _, b := range buah {
		fmt.Println("-", b)
	}

	// range pada string menghasilkan rune
	for i, r := range "Go!" {
		fmt.Printf("%d=%c ", i, r)
	}
	fmt.Println()
}"""
            },
            {
                "body": [
                    "Catatan penting tentang range:",
                    "",
                    "  Pada slice/array : indeks, nilai",
                    "  Pada string      : posisi byte, rune (karakter)",
                    "  Pada map         : kunci, nilai",
                    "  Pada channel     : nilai saja",
                    "  Pada int         : 0, 1, 2, ... sampai n-1 (Go 1.22)",
                    "",
                    "Yang terakhir bentuk paling baru, dan bikin kaget waktu",
                    "pertama melihatnya karena tidak ada koleksi apa pun di sana:",
                    "  for i := range 10 { }   mengulang sepuluh kali, i = 0..9",
                    "  for range 10 { }        sepuluh kali, angkanya tak dipakai",
                    "Ini pengganti singkat untuk 'for i := 0; i < 10; i++'.",
                    "",
                    "Kalau hanya butuh indeks, cukup tulis satu variabel:",
                    "  for i := range buah { }",
                    "",
                    "Kalau hanya butuh nilai, buang indeks dengan _ :",
                    "  for _, b := range buah { }",
                    "",
                    "PERINGATAN URUTAN MAP:",
                    "  Iterasi map di Go SENGAJA diacak setiap kali dijalankan.",
                    "  Jangan pernah bergantung pada urutannya.",
                    "  Kalau butuh urut, kumpulkan kuncinya lalu sort:",
                    "",
                    "    kunci := make([]string, 0, len(m))",
                    "    for k := range m { kunci = append(kunci, k) }",
                    "    sort.Strings(kunci)",
                    "    for _, k := range kunci { fmt.Println(k, m[k]) }",
                    "",
                    "  Empat baris itu memakai make, append, dan map yang belum",
                    "  dipelajari, jadi jangan dihafal sebagai mantra sekarang:",
                    "  make dan append dibahas di materi Array & Slice, map di",
                    "  materi Map. Kembali ke sini setelah keduanya selesai,",
                    "  dan resep ini akan terbaca sendiri.",
                    "",
                    "Mengendalikan perulangan:",
                    "  break      keluar dari perulangan",
                    "  continue   lompat ke iterasi berikutnya",
                    "  Label untuk keluar dari perulangan bersarang:",
                    "    luar:",
                    "    for i := 0; i < 3; i++ {",
                    "        for j := 0; j < 3; j++ {",
                    "            break luar",
                    "        }",
                    "    }",
                ]
            },
        ],
    },
    {
        "title": "8. Array & Slice",
        "sections": [
            {
                "body": [
                    "Go membedakan dua hal yang mirip tapi berbeda:",
                    "",
                    "ARRAY - panjangnya TETAP, bagian dari tipenya.",
                    "  var angka [5]int",
                    "  nilai := [3]string{\"a\", \"b\", \"c\"}",
                    "  [3]int dan [5]int adalah DUA TIPE BERBEDA.",
                    "  Array jarang dipakai langsung di kode sehari-hari.",
                    "",
                    "SLICE - panjangnya bisa berubah. Inilah yang biasa dipakai.",
                    "  var angka []int",
                    "  nilai := []string{\"a\", \"b\", \"c\"}",
                    "  data := make([]int, 3)      panjang 3, isi nol semua",
                    "  data := make([]int, 0, 10)  panjang 0, kapasitas 10",
                    "",
                    "Perbedaan penulisan cuma satu: ada angka di dalam kurung",
                    "siku atau tidak. Tapi perilakunya sangat berbeda.",
                    "",
                    "Slice sebenarnya adalah 'jendela' ke sebuah array",
                    "tersembunyi. Isinya tiga hal: pointer ke data, panjang",
                    "(len), dan kapasitas (cap).",
                ]
            },
            {
                "heading": "Operasi slice",
                "code": """package main

import (
	"fmt"
	"sort"
)

func main() {
	angka := []int{5, 2, 9, 1, 7}

	fmt.Println("Isi      :", angka)
	fmt.Println("Panjang  :", len(angka))
	fmt.Println("Kapasitas:", cap(angka))
	fmt.Println("Pertama  :", angka[0])
	fmt.Println("Terakhir :", angka[len(angka)-1])

	// Menambah elemen
	angka = append(angka, 4)
	angka = append(angka, 8, 3)
	fmt.Println("Setelah append:", angka)

	// Memotong: [awal:akhir], akhir TIDAK ikut
	fmt.Println("angka[1:4]:", angka[1:4])
	fmt.Println("angka[:3] :", angka[:3])
	fmt.Println("angka[3:] :", angka[3:])

	// Menyalin
	salinan := make([]int, len(angka))
	copy(salinan, angka)

	// Mengurutkan
	sort.Ints(salinan)
	fmt.Println("Terurut:", salinan)

	// Menjumlah dengan range
	total := 0
	for _, n := range angka {
		total += n
	}
	fmt.Println("Total:", total)
}"""
            },
            {
                "body": [
                    "Hal yang WAJIB dipahami tentang slice:",
                    "",
                    "1. append MENGEMBALIKAN slice baru. Hasilnya harus",
                    "   ditampung kembali:",
                    "     angka = append(angka, 4)    BENAR",
                    "     append(angka, 4)            SALAH, hasilnya hilang",
                    "",
                    "2. Slice BERBAGI data dengan slice asalnya.",
                    "     a := []int{1, 2, 3}",
                    "     b := a[0:2]",
                    "     b[0] = 99",
                    "     fmt.Println(a)   -> [99 2 3], a ikut berubah!",
                    "   Kalau butuh salinan mandiri, pakai copy().",
                    "",
                    "3. Slice kosong vs nil:",
                    "     var a []int           nil, tapi tetap aman dipakai",
                    "     b := []int{}          tidak nil, panjang 0",
                    "   Keduanya bisa langsung di-append.",
                    "",
                    "4. Mengakses indeks di luar batas menyebabkan panic",
                    "   saat program berjalan, bukan error kompilasi.",
                    "   Selalu cek len() sebelum mengakses indeks dinamis.",
                    "",
                    "5. Menghapus elemen indeks i:",
                    "     s = append(s[:i], s[i+1:]...)",
                    "   Tanda ... membongkar slice jadi argumen terpisah.",
                    "",
                    "6. Mengurutkan dengan aturan sendiri: sort.Slice.",
                    "   sort.Ints dan sort.Strings cuma tahu urutan bawaan.",
                    "   Untuk aturan lain, serahkan fungsi pembanding:",
                    "     sort.Slice(daftar, func(i, j int) bool {",
                    "         return daftar[i] < daftar[j]",
                    "     })",
                    "   Perhatikan baik-baik: pembandingnya menerima INDEKS i",
                    "   dan j, BUKAN elemennya. Elemennya kamu ambil sendiri",
                    "   dari slice-nya, seperti daftar[i] di atas.",
                    "   Kembalikan true kalau elemen i harus berdiri di DEPAN",
                    "   elemen j. Membalik urutan cukup mengganti < jadi >.",
                    "   Berbeda dari append, sort.Slice mengurutkan DI TEMPAT,",
                    "   jadi tidak ada yang perlu ditampung kembali.",
                    "",
                    "Slice dua dimensi:",
                    "  matriks := [][]int{{1, 2}, {3, 4}}",
                    "  fmt.Println(matriks[1][0])   -> 3",
                    "",
                    "Kurawal dobel di situ bukan sintaks khusus. Di dalam",
                    "[]T{...} nama tipe elemen boleh DIHILANGKAN, jadi baris",
                    "tadi cuma bentuk pendek dari:",
                    "  matriks := [][]int{[]int{1, 2}, []int{3, 4}}",
                    "Aturan yang sama nanti membuat []Siswa{{Nama: \"Andi\"}} di",
                    "materi Struct & Method bisa ditulis tanpa mengulang kata",
                    "Siswa di tiap barisnya.",
                ]
            },
        ],
    },
    {
        "title": "9. String, Rune & Package strings",
        "sections": [
            {
                "body": [
                    "Di Go, string BUKAN daftar huruf. String adalah deretan BYTE yang tidak bisa diubah.",
                    "Kalimatnya terdengar teknis, tapi akibatnya sudah terasa di baris pertama:",
                    "",
                    "  s := \"café\"",
                    "  len(s)      -> 5, bukan 4",
                    "  s[0]        -> 99, bukan \"c\"",
                    "  s[0] = 'x'  -> tidak dikompilasi sama sekali",
                    "",
                    "Kenapa 5? Karena Go menyimpan teks dalam UTF-8. Huruf a sampai z memakai 1 byte,",
                    "tapi é memakai 2 byte dan emoji bisa memakai 4 byte. len() menghitung BYTE, bukan huruf.",
                    "",
                    "Kenapa s[0] jadi angka? Karena mengindeks string menghasilkan satu byte (alias uint8),",
                    "dan fmt mencetak angka untuk tipe angka. Bungkus string(...) supaya hurufnya terlihat.",
                    "",
                    "Kenapa s[0] = 'x' ditolak? String di Go IMMUTABLE, isinya tidak pernah berubah.",
                    "Semua fungsi yang seolah 'mengubah' string sebenarnya mengembalikan string BARU.",
                    "Yang lama tetap utuh, dan kalau hasilnya tidak ditampung, hasilnya hilang begitu saja.",
                    "",
                    "Untuk bekerja per KARAKTER, Go punya tipe rune (alias int32) yang menyimpan satu",
                    "kode Unicode. Ubah dulu jadi []rune, baru indeks dan potong dengan aman.",
                    "",
                    "  Tipe    Isinya                        Didapat dari",
                    "  byte    satu byte mentah, 0-255       s[i] atau []byte(s)",
                    "  rune    satu karakter Unicode         []rune(s) atau for range",
                    "",
                    "Materi 6 sudah menyebut for range pada string memberi (posisi byte, rune).",
                    "Sekarang alasannya jelas: angka pertamanya bukan nomor urut karakter, melainkan",
                    "berapa byte yang sudah dilewati. Itulah kenapa indeksnya MELOMPAT di huruf beraksen.",
                ],
            },
            {
                "heading": "Byte, rune, dan potongan yang salah",
                "code": """package main

import (
	"fmt"
	"unicode/utf8"
)

func main() {
	kata := "café"

	fmt.Println("len(kata)         :", len(kata))
	fmt.Println("jumlah karakter   :", utf8.RuneCountInString(kata))

	// kata[0] bertipe byte, jadi yang tercetak angka
	fmt.Println("kata[0]           :", kata[0])
	fmt.Println("kata[0] jadi huruf:", string(kata[0]))

	// kata[0] = 'x'   <- TIDAK dikompilasi, string tidak bisa diubah

	// Dua konversi yang paling sering dipakai
	b := []byte(kata)
	r := []rune(kata)
	fmt.Println("[]byte:", len(b), b)
	fmt.Println("[]rune:", len(r), r)

	// Balik lagi jadi string: string(b) untuk byte, string(r) untuk rune
	fmt.Println("string(b):", string(b), "| string(r):", string(r))

	// Memotong per KARAKTER lewat []rune: aman
	fmt.Println("2 huruf pertama:", string(r[:2]))
	fmt.Println("huruf terakhir :", string(r[len(r)-1]))

	// Memotong per BYTE: bisa membelah satu huruf jadi separuh
	fmt.Println("kata[:4]       :", kata[:4])

	// Merakit string baru dari rune
	terbalik := make([]rune, 0, len(r))
	for i := len(r) - 1; i >= 0; i-- {
		terbalik = append(terbalik, r[i])
	}
	fmt.Println("dibalik        :", string(terbalik))

	// for range memberi POSISI BYTE, bukan nomor urut karakter
	for i, c := range kata {
		fmt.Printf("i=%d huruf=%c kode=%d\\n", i, c, c)
	}
}""",
            },
            {
                "body": [
                    "Perhatikan dua baris terakhir keluarannya:",
                    "",
                    "  kata[:4] mencetak 'caf' lalu satu karakter rusak, karena potongannya membelah",
                    "  é jadi separuh dan separuh byte itu bukan huruf apa pun.",
                    "  for range melompat dari i=2 langsung ke i=3 lalu berhenti: hanya 4 putaran",
                    "  untuk 5 byte, karena é dibaca sekali sebagai satu rune.",
                    "",
                    "Aturan praktisnya: potong per byte hanya kalau kamu yakin isinya ASCII;",
                    "selain itu ubah dulu ke []rune.",
                    "",
                    "KENAPA LEWAT PACKAGE, BUKAN METHOD",
                    "",
                    "Orang yang datang dari Python atau Java otomatis mengetik:",
                    "",
                    "  nama.split(\",\")       Python",
                    "  nama.toUpperCase()    Java",
                    "",
                    "Di Go keduanya tidak ada, dan tidak akan pernah ada. string adalah tipe bawaan,",
                    "dan tipe bawaan tidak boleh punya method. Semua operasi teks tinggal di",
                    "package strings, dengan teksnya sebagai ARGUMEN PERTAMA:",
                    "",
                    "  strings.Split(nama, \",\")",
                    "  strings.ToUpper(nama)",
                    "",
                    "Jangan lupa import \"strings\". Di Go itu error kompilasi, bukan peringatan.",
                    "",
                    "Isi package strings yang benar-benar dipakai sehari-hari:",
                    "",
                    "  Memecah dan menyambung",
                    "    Fields(s)             pecah per spasi; spasi beruntun dianggap satu",
                    "    Split(s, sep)         pecah per pemisah; potongan kosong tetap ikut",
                    "    SplitN(s, sep, n)     sama, tapi paling banyak n potong",
                    "    Join(potongan, sep)   kebalikan Split",
                    "    Cut(s, sep)           pisah SEKALI: sebelum, sesudah, ketemu",
                    "  Memeriksa",
                    "    Contains(s, sub)      ada atau tidak",
                    "    HasPrefix(s, awal)    diawali teks tertentu",
                    "    HasSuffix(s, akhir)   diakhiri teks tertentu, misalnya \".csv\"",
                    "    Index(s, sub)         posisi BYTE kemunculan pertama, -1 kalau tidak ada",
                    "    Count(s, sub)         berapa kali muncul",
                    "    EqualFold(a, b)       sama, tanpa peduli huruf besar-kecil",
                    "  Mengubah, dan semuanya menghasilkan string BARU",
                    "    ToUpper(s) / ToLower(s)",
                    "    Replace(s, lama, baru, n) / ReplaceAll(s, lama, baru)",
                    "    TrimSpace(s)          buang spasi, tab, dan enter di kedua ujung",
                    "    Trim / TrimPrefix / TrimSuffix",
                    "    Repeat(s, n)          ulang n kali, enak untuk garis pemisah",
                    "",
                    "DUA NAMA DI PROGRAM BERIKUT YANG PERLU PENJELASAN SENDIRI",
                    "",
                    "strings.Builder, untuk merangkai teks di dalam loop.",
                    "  Karena string tidak bisa diubah, hasil dari s += x adalah string BARU: seluruh",
                    "  isi lama disalin ulang setiap iterasi. Untuk 10 potong tidak terasa, untuk",
                    "  100.000 potong program jadi lambat luar biasa. Builder menumpuk potongannya",
                    "  di satu penyangga dan baru menjadikannya string satu kali di akhir:",
                    "",
                    "    var b strings.Builder",
                    "    for _, x := range daftar {",
                    "        b.WriteString(x)",
                    "    }",
                    "    hasil := b.String()",
                    "",
                    "  b tidak perlu diisi apa pun sebelum dipakai; zero value-nya sudah siap kerja.",
                    "",
                    "strings.NewReader, untuk menjadikan sebuah string sumber bacaan (io.Reader).",
                    "  Fungsi yang biasanya membaca dari berkas jadi bisa diberi string biasa tanpa",
                    "  menyentuh disk. Inilah yang membuat kode pembaca berkas gampang diuji.",
                    "  io.Reader sendiri dibahas tuntas di materi berkas.",
                ],
            },
            {
                "heading": "Package strings sehari-hari",
                "code": """package main

import (
	"bufio"
	"fmt"
	"strings"
)

func main() {
	kalimat := "  Belajar Go itu menyenangkan  "
	bersih := strings.TrimSpace(kalimat)
	fmt.Printf("[%s]\\n", bersih)

	// MEMECAH DAN MENYAMBUNG
	fmt.Println(strings.Fields(bersih))            // pisah per spasi
	fmt.Println(strings.Split("a,b,,c", ","))      // yang kosong tetap ikut
	fmt.Println(strings.SplitN("a,b,c,d", ",", 2)) // paling banyak 2 potong
	fmt.Println(strings.Join([]string{"x", "y", "z"}, " - "))

	// MEMERIKSA
	fmt.Println(strings.Contains(bersih, "Go"))
	fmt.Println(strings.HasPrefix(bersih, "Belajar"))
	fmt.Println(strings.HasSuffix("laporan.csv", ".csv"))
	fmt.Println(strings.Index(bersih, "Go")) // posisi byte
	fmt.Println(strings.Index(bersih, "Java"))
	fmt.Println(strings.Count("pisang", "a"))

	// MENGUBAH: yang asli tidak pernah tersentuh
	fmt.Println(strings.ToUpper("go"), strings.ToLower("GO"))
	fmt.Println(strings.ReplaceAll("1-2-3", "-", "/"))
	fmt.Println(strings.Replace("1-2-3", "-", "/", 1)) // hanya sekali
	fmt.Println(strings.TrimSuffix("laporan.csv", ".csv"))
	fmt.Println(strings.TrimPrefix("Rp15000", "Rp"))
	fmt.Println(strings.Trim("**judul**", "*"))
	fmt.Println(strings.Repeat("=", 20))

	// MEMBANDINGKAN
	fmt.Println("Go" == "go", strings.EqualFold("Go", "go"))

	// Cut memisah SEKALI di pemisah pertama
	kunci, nilai, ketemu := strings.Cut("nama=Andi=Budi", "=")
	fmt.Println(kunci, nilai, ketemu)

	// Builder: merangkai di dalam loop tanpa menyalin ulang
	var b strings.Builder
	for i, k := range strings.Fields(bersih) {
		if i > 0 {
			b.WriteString(" | ")
		}
		b.WriteString(strings.ToUpper(k))
	}
	fmt.Println(b.String())

	// NewReader: string diperlakukan seperti berkas yang sedang dibaca
	pemindai := bufio.NewScanner(strings.NewReader("baris 1\\nbaris 2\\nbaris 3"))
	for pemindai.Scan() {
		fmt.Println("baca:", pemindai.Text())
	}
}""",
            },
            {
                "heading": "String mentah dengan backtick",
                "body": [
                    "Sampai sini semua string ditulis dengan tanda kutip ganda. Go punya bentuk KEDUA:",
                    "backtick, tombol di kiri angka 1. Aturannya cuma satu, dan justru kebalikannya:",
                    "",
                    "  Di dalam backtick TIDAK ADA escape. Apa yang ditulis, itu yang tersimpan.",
                    "",
                    "Akibatnya dua hal:",
                    "  - \\n di dalam backtick berarti DUA karakter, backslash dan huruf n.",
                    "    Bukan pindah baris.",
                    "  - Baris baru sungguhan boleh diketik apa adanya, jadi teks banyak baris",
                    "    tidak perlu disambung dengan tanda tambah.",
                    "",
                    "Yang paling sering ditulis dengan backtick di kode nyata:",
                    "  - Teks banyak baris: pesan bantuan, banner, template.",
                    "  - Contoh JSON, karena tidak perlu satu pun \\\" di dalamnya.",
                    "  - Query SQL yang panjang.",
                    "  - Pola regexp: `\\d{4}` jauh lebih terbaca daripada \"\\\\d{4}\".",
                    "  - Struct tag seperti `json:\"nama\"`, yang akan dipakai di materi JSON.",
                    "",
                    "Satu-satunya yang tidak bisa dimasukkan ke dalamnya adalah backtick itu sendiri.",
                    "",
                    "MEMBANDINGKAN STRING",
                    "  ==        membandingkan ISI, bukan alamat. Tidak ada .equals() seperti di Java.",
                    "  < dan >   urut kamus menurut nilai byte, jadi \"Zebra\" < \"apel\" itu true",
                    "            karena huruf besar punya kode lebih kecil daripada huruf kecil.",
                    "  EqualFold kalau besar-kecilnya huruf tidak boleh berpengaruh.",
                    "",
                    "Jebakan yang paling sering menggigit:",
                    "  1. strings.ToUpper(s) TIDAK mengubah s. Tampung: s = strings.ToUpper(s).",
                    "  2. Split(\"a,,b\", \",\") memberi 3 potong, satu di antaranya kosong;",
                    "     Fields memberi 2. Untuk memecah kalimat pakai Fields, untuk CSV pakai Split.",
                    "  3. Split(\"\", \",\") memberi SATU potong berisi string kosong, bukan slice kosong.",
                    "     len()-nya 1, jadi jangan dipakai untuk mendeteksi masukan kosong.",
                    "  4. Index mengembalikan posisi BYTE. Jangan dianggap nomor urut karakter.",
                    "  5. len(s) bukan jumlah huruf. Untuk itu utf8.RuneCountInString(s).",
                ],
                "code": """package main

import "fmt"

func main() {
	// String biasa: \\n jadi pindah baris, \\" jadi tanda kutip
	biasa := "Baris 1\\nBaris 2"
	fmt.Println(biasa)
	fmt.Println("panjang:", len(biasa))

	// String mentah: apa yang ditulis, itu yang keluar
	mentah := `Baris 1\\nBaris 2`
	fmt.Println(mentah)
	fmt.Println("panjang:", len(mentah))

	// Baris baru boleh diketik apa adanya, tanpa tanda tambah
	sql := `SELECT nama, umur
FROM siswa
WHERE umur > 17`
	fmt.Println(sql)

	// Tanda kutip tidak perlu di-escape sama sekali
	contoh := `{"nama": "Andi", "umur": 20}`
	kembar := "{\\"nama\\": \\"Andi\\", \\"umur\\": 20}"
	fmt.Println(contoh)
	fmt.Println("isinya sama?", contoh == kembar)

	// Pola pencocokan teks juga jauh lebih enak dibaca begini
	pola := `\\d{4}-\\d{2}-\\d{2}`
	fmt.Println("pola:", pola, "panjang:", len(pola))
}""",
            },
        ],
    },
    {
        "title": "10. Map",
        "sections": [
            {
                "body": [
                    "Map menyimpan pasangan kunci-nilai, mirip dictionary",
                    "di Python atau HashMap di Java.",
                    "",
                    "Membuat map:",
                    "  var m map[string]int          nil, BELUM bisa diisi",
                    "  m := make(map[string]int)     siap dipakai",
                    "  m := map[string]int{          langsung dengan isi",
                    "      \"andi\": 25,",
                    "      \"budi\": 30,",
                    "  }",
                    "",
                    "HATI-HATI: menulis ke map nil menyebabkan panic.",
                    "  var m map[string]int",
                    "  m[\"a\"] = 1        PANIC saat dijalankan",
                    "Selalu buat dengan make() atau literal.",
                    "",
                    "Operasi dasar:",
                    "  m[\"citra\"] = 28       tambah atau ubah",
                    "  nilai := m[\"andi\"]    baca",
                    "  delete(m, \"budi\")     hapus",
                    "  len(m)                jumlah pasangan",
                    "",
                    "Kalau kunci tidak ada, membaca map memberikan zero value,",
                    "BUKAN error. Untuk map[string]int hasilnya 0.",
                ]
            },
            {
                "heading": "Contoh lengkap",
                "code": """package main

import (
	"fmt"
	"sort"
)

func main() {
	stok := map[string]int{
		"beras":  25,
		"gula":   10,
		"minyak": 8,
	}

	stok["telur"] = 30
	stok["gula"] = 12

	// Cek keberadaan kunci dengan comma ok
	if jumlah, ada := stok["beras"]; ada {
		fmt.Println("Beras tersedia:", jumlah)
	}

	if _, ada := stok["kopi"]; !ada {
		fmt.Println("Kopi tidak ada dalam daftar")
	}

	// Iterasi URUT: kumpulkan kunci lalu sort
	kunci := make([]string, 0, len(stok))
	for k := range stok {
		kunci = append(kunci, k)
	}
	sort.Strings(kunci)

	total := 0
	for _, k := range kunci {
		fmt.Printf("%-8s: %d\\n", k, stok[k])
		total += stok[k]
	}

	fmt.Println("Total stok:", total)
	fmt.Println("Jenis barang:", len(stok))

	delete(stok, "minyak")
	fmt.Println("Setelah dihapus:", len(stok))
}"""
            },
            {
                "body": [
                    "Pola 'comma ok' adalah kunci bekerja dengan map:",
                    "",
                    "  nilai, ada := m[\"kunci\"]",
                    "",
                    "  nilai -> isinya, atau zero value kalau tidak ada",
                    "  ada   -> true kalau kunci benar-benar ada",
                    "",
                    "Kenapa penting? Karena membaca kunci yang tidak ada",
                    "menghasilkan 0, sama seperti kunci yang memang bernilai 0.",
                    "Tanpa 'ada', kamu tidak bisa membedakan keduanya.",
                    "",
                    "  skor := map[string]int{\"andi\": 0}",
                    "  skor[\"andi\"]  -> 0  (ada, nilainya nol)",
                    "  skor[\"budi\"]  -> 0  (tidak ada sama sekali)",
                    "",
                    "Aturan lain tentang map:",
                    "",
                    "  - Kunci harus tipe yang bisa dibandingkan: string,",
                    "    angka, bool, struct sederhana. Slice dan map TIDAK",
                    "    bisa jadi kunci.",
                    "  - Nilai boleh tipe apa pun, termasuk slice atau struct.",
                    "  - Map dilewatkan sebagai referensi. Mengubahnya di",
                    "    dalam fungsi ikut mengubah aslinya.",
                    "  - Urutan iterasi SELALU acak. Ini disengaja supaya",
                    "    programmer tidak diam-diam bergantung padanya.",
                    "",
                    "Map dengan nilai slice:",
                    "  kelompok := map[string][]string{}",
                    "  kelompok[\"A\"] = append(kelompok[\"A\"], \"andi\")",
                    "  Ini aman walau kunci \"A\" belum ada, karena append",
                    "  pada slice nil tetap bekerja.",
                    "",
                    "HIMPUNAN (SET) DENGAN MAP",
                    "",
                    "Go tidak punya tipe himpunan. Kode nyata memakai map yang",
                    "nilainya sengaja tidak dipakai:",
                    "",
                    "  ada := map[string]struct{}{}",
                    "  ada[\"andi\"] = struct{}{}",
                    "  if _, ok := ada[\"andi\"]; ok { fmt.Println(\"terdaftar\") }",
                    "",
                    "struct{}{} yang tampak seperti salah ketik itu terbaca",
                    "begini: struct{} adalah tipe struct TANPA field, lalu",
                    "pasangan kurawal kedua membuat NILAI dari tipe itu. Tipe",
                    "tanpa field memakan nol byte, jadi yang benar-benar",
                    "tersimpan cuma kuncinya.",
                    "",
                    "Alternatifnya map[string]bool: lebih enak dibaca karena",
                    "ada[\"andi\"] langsung bernilai true atau false tanpa comma",
                    "ok, dengan ongkos satu byte per kunci. Untuk data biasa",
                    "pilih mana pun; keduanya sama-sama umum di kode orang.",
                ]
            },
        ],
    },
    {
        "title": "11. Fungsi",
        "sections": [
            {
                "body": [
                    "Bentuk dasar fungsi:",
                    "",
                    "  func namaFungsi(param1 tipe1, param2 tipe2) tipeHasil {",
                    "      return nilai",
                    "  }",
                    "",
                    "Perhatikan: tipe ditulis SESUDAH nama parameter,",
                    "kebalikan dari C/Java.",
                    "  func tambah(a int, b int) int      Go",
                    "  int tambah(int a, int b)           C/Java",
                    "",
                    "Kalau tipe berurutan sama, boleh disingkat:",
                    "  func tambah(a, b int) int",
                    "",
                    "Fitur khas Go: MENGEMBALIKAN BANYAK NILAI.",
                    "  func bagi(a, b float64) (float64, error) {",
                    "      if b == 0 {",
                    "          return 0, errors.New(\"pembagi nol\")",
                    "      }",
                    "      return a / b, nil",
                    "  }",
                    "",
                    "Ini dasar dari seluruh cara Go menangani error.",
                    "Tidak ada exception; error dikembalikan sebagai nilai.",
                ]
            },
            {
                "heading": "Berbagai bentuk fungsi",
                "code": """package main

import (
	"errors"
	"fmt"
)

// Banyak nilai kembali
func bagi(a, b float64) (float64, error) {
	if b == 0 {
		return 0, errors.New("tidak bisa dibagi nol")
	}
	return a / b, nil
}

// Named return values
func hitungStatistik(data []int) (total, maksimal int) {
	maksimal = data[0]
	for _, n := range data {
		total += n
		if n > maksimal {
			maksimal = n
		}
	}
	return // otomatis mengembalikan total dan maksimal
}

// Variadic: jumlah argumen bebas
func jumlahkan(angka ...int) int {
	total := 0
	for _, n := range angka {
		total += n
	}
	return total
}

// Fungsi sebagai parameter
func terapkan(data []int, f func(int) int) []int {
	hasil := make([]int, len(data))
	for i, n := range data {
		hasil[i] = f(n)
	}
	return hasil
}

func main() {
	if h, err := bagi(10, 4); err == nil {
		fmt.Printf("10/4 = %.2f\\n", h)
	}
	if _, err := bagi(10, 0); err != nil {
		fmt.Println("Error:", err)
	}

	total, maks := hitungStatistik([]int{5, 9, 3})
	fmt.Println("Total:", total, "Maks:", maks)

	fmt.Println(jumlahkan(1, 2, 3, 4, 5))
	angka := []int{1, 2, 3}
	fmt.Println(jumlahkan(angka...))

	kuadrat := func(n int) int { return n * n }
	fmt.Println(terapkan(angka, kuadrat))
}"""
            },
            {
                "body": [
                    "Konsep penting pada fungsi Go:",
                    "",
                    "1. Named return values",
                    "     func f() (total int, err error) {",
                    "   Variabel total dan err sudah otomatis dibuat.",
                    "   'return' kosong akan mengembalikan nilainya saat itu.",
                    "   Berguna untuk dokumentasi, tapi jangan dipakai di",
                    "   fungsi panjang karena membingungkan.",
                    "",
                    "2. Variadic dengan ...",
                    "     func f(angka ...int)",
                    "   Di dalam fungsi, angka adalah []int biasa.",
                    "   Untuk mengirim slice yang sudah ada: f(slice...)",
                    "",
                    "3. Fungsi adalah nilai (first-class).",
                    "   Bisa disimpan di variabel, dikirim sebagai argumen,",
                    "   dan dikembalikan dari fungsi lain.",
                    "",
                    "4. Closure: fungsi yang 'mengingat' variabel di luarnya.",
                    "",
                    "     func penghitung() func() int {",
                    "         n := 0",
                    "         return func() int {",
                    "             n++",
                    "             return n",
                    "         }",
                    "     }",
                    "     c := penghitung()",
                    "     c()  -> 1",
                    "     c()  -> 2",
                    "",
                    "   Fungsi tanpa nama seperti itu boleh juga LANGSUNG",
                    "   DIPANGGIL di tempat, dengan menempelkan sepasang kurung",
                    "   kosong di ujungnya:",
                    "",
                    "     func() {",
                    "         fmt.Println(\"jalan sekarang juga\")",
                    "     }()",
                    "",
                    "   Kurung terakhir itulah yang memanggilnya. Tanpa kurung",
                    "   itu, yang kamu tulis cuma sebuah nilai fungsi yang tidak",
                    "   pernah jalan. Bentuk inilah yang membuat",
                    "   'defer func() { ... }()' di materi Error Handling dan",
                    "   'go func() { ... }()' di materi Goroutine bisa bekerja.",
                    "",
                    "5. defer menunda eksekusi sampai fungsi selesai:",
                    "     f, err := os.Open(\"data.txt\")",
                    "     if err != nil {",
                    "         return err",
                    "     }",
                    "     defer f.Close()",
                    "   Baris Close dijamin jalan walau terjadi error di",
                    "   tengah jalan. Beberapa defer dijalankan terbalik,",
                    "   yang terakhir didaftarkan jalan duluan.",
                    "   Error-nya wajib diperiksa DULU: kalau os.Open gagal, f",
                    "   bernilai nil dan f.Close() malah bikin panic. Membuka",
                    "   berkas dibahas lengkap di materi Berkas.",
                    "",
                    "   Dua hal yang sering menjebak soal defer:",
                    "     - Argumennya DIEVALUASI saat didaftarkan, bukan saat",
                    "       dijalankan:",
                    "         i := 1",
                    "         defer fmt.Println(i)   mencetak 1, bukan 2",
                    "         i = 2",
                    "     - defer di dalam loop TIDAK jalan di akhir putaran,",
                    "       tapi menumpuk sampai seluruh fungsinya selesai.",
                    "       Membuka seribu berkas dalam loop dengan",
                    "       'defer f.Close()' berarti seribu berkas terbuka",
                    "       bersamaan. Pindahkan isi loop ke fungsi tersendiri",
                    "       supaya defer-nya punya ujung.",
                    "",
                    "6. Nama berhuruf besar = publik (bisa diakses package",
                    "   lain). Berhuruf kecil = privat. Ini menggantikan",
                    "   kata kunci public/private.",
                ]
            },
        ],
    },
    {
        "title": "12. Pointer",
        "sections": [
            {
                "body": [
                    "Pointer menyimpan ALAMAT sebuah nilai, bukan nilainya.",
                    "",
                    "Dua operator utama:",
                    "  &x   ambil ALAMAT dari variabel x",
                    "  *p   ambil NILAI yang ditunjuk pointer p",
                    "",
                    "  x := 10",
                    "  p := &x        p menunjuk ke x",
                    "  fmt.Println(*p)   -> 10",
                    "  *p = 20           mengubah x lewat p",
                    "  fmt.Println(x)    -> 20",
                    "",
                    "Tipe pointer ditulis dengan bintang di depan:",
                    "  var p *int      pointer ke int",
                    "  var s *string   pointer ke string",
                    "",
                    "Kenapa pointer dibutuhkan?",
                    "  Go SELALU mengirim argumen sebagai SALINAN.",
                    "  Kalau fungsi harus mengubah variabel aslinya,",
                    "  fungsi itu harus menerima pointer.",
                    "",
                    "Nilai bawaan pointer adalah nil. Mengakses *p saat",
                    "p bernilai nil menyebabkan panic.",
                ]
            },
            {
                "heading": "Pointer dalam praktik",
                "code": """package main

import "fmt"

// Menerima salinan: perubahan TIDAK terlihat di luar
func tambahSalinan(n int) {
	n += 100
}

// Menerima pointer: perubahan terlihat di luar
func tambahPointer(n *int) {
	*n += 100
}

func tukar(a, b *int) {
	*a, *b = *b, *a
}

func main() {
	x := 10
	tambahSalinan(x)
	fmt.Println("Setelah tambahSalinan:", x) // 10

	tambahPointer(&x)
	fmt.Println("Setelah tambahPointer:", x) // 110

	a, b := 1, 2
	tukar(&a, &b)
	fmt.Println("a =", a, "b =", b) // 2 1

	// new() membuat pointer ke zero value
	p := new(int)
	*p = 42
	fmt.Println("Isi p:", *p)

	// Pointer nil harus dicek sebelum dipakai
	var q *int
	if q == nil {
		fmt.Println("q masih nil, tidak boleh dibaca")
	}
}"""
            },
            {
                "body": [
                    "Kapan memakai pointer:",
                    "",
                    "  1. Fungsi perlu MENGUBAH argumen aslinya.",
                    "  2. Struct-nya besar, menyalin jadi boros memori.",
                    "  3. Perlu membedakan 'tidak ada nilai' (nil) dari",
                    "     'nilai nol'.",
                    "  4. Method perlu mengubah isi struct penerimanya.",
                    "",
                    "Kapan TIDAK perlu:",
                    "",
                    "  1. Slice, map, dan channel sudah berperilaku seperti",
                    "     referensi. Mengubah isinya di dalam fungsi sudah",
                    "     terlihat di luar tanpa pointer.",
                    "  2. Tipe kecil seperti int, bool, atau struct 1-2 field",
                    "     yang tidak perlu diubah.",
                    "",
                    "Yang membuat Go lebih aman daripada C:",
                    "",
                    "  - TIDAK ADA aritmatika pointer. Kamu tidak bisa",
                    "    menulis p++ untuk berpindah alamat. Ini menghapus",
                    "    seluruh kelas bug buffer overflow.",
                    "  - Garbage collector mengurus pembebasan memori.",
                    "    Tidak ada malloc dan free.",
                    "  - Mengembalikan pointer ke variabel lokal AMAN:",
                    "",
                    "      func buat() *int {",
                    "          n := 5",
                    "          return &n     aman di Go, bug di C",
                    "      }",
                    "",
                    "    Compiler otomatis memindahkan n ke heap. Perilaku",
                    "    ini disebut escape analysis.",
                ]
            },
        ],
    },
    {
        "title": "13. Struct & Method",
        "sections": [
            {
                "body": [
                    "Struct mengelompokkan beberapa data jadi satu tipe baru.",
                    "Go tidak punya class, struct adalah penggantinya.",
                    "",
                    "  type Siswa struct {",
                    "      Nama  string",
                    "      Umur  int",
                    "      Nilai float64",
                    "  }",
                    "",
                    "Membuat instance:",
                    "  s := Siswa{Nama: \"Andi\", Umur: 20, Nilai: 85.5}",
                    "  s := Siswa{\"Andi\", 20, 85.5}   urutan harus persis",
                    "  var s Siswa                     semua field zero value",
                    "  p := &Siswa{Nama: \"Budi\"}       pointer ke struct",
                    "",
                    "Bentuk dengan nama field lebih disukai karena tetap",
                    "benar walau urutan field berubah di kemudian hari.",
                    "",
                    "Mengakses field pakai titik:",
                    "  s.Nama = \"Citra\"",
                    "  fmt.Println(s.Umur)",
                    "",
                    "Lewat pointer juga cukup titik, Go otomatis",
                    "melakukan dereference:",
                    "  p.Nama = \"Dedi\"     tidak perlu (*p).Nama",
                    "",
                    "STRUCT ANONIM",
                    "Tipe struct boleh ditulis langsung di tempat, tanpa type",
                    "dan tanpa nama, kalau memang cuma dipakai sekali:",
                    "",
                    "  kasus := []struct {",
                    "      nama string",
                    "      a, b int",
                    "  }{",
                    "      {\"positif\", 2, 3},",
                    "      {\"negatif\", -2, -3},",
                    "  }",
                    "",
                    "Bagian '}{' yang tampak aneh itu sebenarnya dua hal",
                    "bersebelahan: kurawal pertama MENUTUP definisi tipenya,",
                    "kurawal kedua MEMBUKA nilainya. Persis seperti []int{1, 2},",
                    "cuma nama tipenya diganti seluruh definisi struct.",
                    "",
                    "Hafalkan istilahnya: struct anonim. Inilah bentuk yang",
                    "dipakai table-driven test di materi Package, Module &",
                    "Testing dan di Studi Kasus, dan tanpa nama itu kamu tidak",
                    "punya kata untuk mencarinya sendiri.",
                    "",
                    "MEMBANDINGKAN DUA STRUCT",
                    "Dua struct bisa dibandingkan dengan == asalkan SEMUA",
                    "field-nya bisa dibandingkan: angka, string, bool, pointer,",
                    "dan struct sejenis.",
                    "  Siswa{\"Andi\", 20, 85.5} == Siswa{\"Andi\", 20, 85.5}  true",
                    "Kalau ada satu saja field bertipe slice, map, atau func,",
                    "compiler menolak ==.",
                    "",
                    "Karena itu pula struct yang semua field-nya bisa",
                    "dibandingkan boleh dipakai sebagai KUNCI MAP, melengkapi",
                    "aturan kunci map di materi Map:",
                    "  type Titik struct{ X, Y int }",
                    "  peta := map[Titik]string{{0, 0}: \"asal\"}",
                ]
            },
            {
                "heading": "Struct dan method",
                "code": """package main

import "fmt"

type Siswa struct {
	Nama  string
	Umur  int
	Nilai float64
}

// Value receiver: bekerja pada SALINAN
func (s Siswa) Keterangan() string {
	return fmt.Sprintf("%s (%d th), nilai %.1f", s.Nama, s.Umur, s.Nilai)
}

func (s Siswa) Lulus() bool {
	return s.Nilai >= 75
}

// Pointer receiver: bisa MENGUBAH struct aslinya
func (s *Siswa) NaikkanNilai(tambahan float64) {
	s.Nilai += tambahan
	if s.Nilai > 100 {
		s.Nilai = 100
	}
}

// Struct bersarang
type Kelas struct {
	Nama  string
	Murid []Siswa
}

func (k Kelas) RataRata() float64 {
	if len(k.Murid) == 0 {
		return 0
	}
	total := 0.0
	for _, m := range k.Murid {
		total += m.Nilai
	}
	return total / float64(len(k.Murid))
}

func main() {
	a := Siswa{Nama: "Andi", Umur: 20, Nilai: 72}
	fmt.Println(a.Keterangan())
	fmt.Println("Lulus?", a.Lulus())

	a.NaikkanNilai(10)
	fmt.Println("Setelah remedial:", a.Keterangan())
	fmt.Println("Lulus?", a.Lulus())

	k := Kelas{
		Nama: "12 IPA 1",
		Murid: []Siswa{
			{Nama: "Budi", Umur: 20, Nilai: 80},
			{Nama: "Citra", Umur: 19, Nilai: 90},
		},
	}
	fmt.Printf("Rata-rata %s: %.1f\\n", k.Nama, k.RataRata())
}"""
            },
            {
                "body": [
                    "VALUE RECEIVER vs POINTER RECEIVER",
                    "Ini konsep yang paling sering membingungkan pemula.",
                    "",
                    "  func (s Siswa) Baca() string      value receiver",
                    "    - s adalah SALINAN struct",
                    "    - Perubahan pada s TIDAK memengaruhi aslinya",
                    "    - Pakai untuk method yang hanya MEMBACA",
                    "",
                    "  func (s *Siswa) Ubah()            pointer receiver",
                    "    - s menunjuk ke struct ASLI",
                    "    - Perubahan pada s TERLIHAT di luar",
                    "    - Pakai untuk method yang MENGUBAH data",
                    "    - Juga dipakai kalau struct-nya besar",
                    "",
                    "Aturan praktis: kalau ada satu saja method yang butuh",
                    "pointer receiver, buat SEMUA method tipe itu pakai",
                    "pointer receiver. Konsistensi mencegah kebingungan.",
                    "",
                    "Kabar baiknya, Go otomatis menyesuaikan saat memanggil:",
                    "  a := Siswa{}",
                    "  a.NaikkanNilai(5)     Go otomatis jadi (&a).NaikkanNilai(5)",
                    "",
                    "EMBEDDING - cara Go menggantikan pewarisan:",
                    "",
                    "  type Orang struct {",
                    "      Nama string",
                    "  }",
                    "  type Karyawan struct {",
                    "      Orang           <- disematkan, tanpa nama field",
                    "      Gaji int",
                    "  }",
                    "",
                    "  k := Karyawan{Orang{\"Andi\"}, 5000000}",
                    "  fmt.Println(k.Nama)     langsung, tanpa k.Orang.Nama",
                    "",
                    "Karyawan mewarisi field DAN method dari Orang.",
                    "Go menyebut ini komposisi, bukan pewarisan. Bedanya:",
                    "tidak ada hierarki tipe, hanya penggabungan.",
                ]
            },
        ],
    },
    {
        "title": "14. Interface",
        "sections": [
            {
                "body": [
                    "Interface mendefinisikan SEKUMPULAN METHOD yang harus",
                    "dimiliki sebuah tipe. Interface tidak berisi data.",
                    "",
                    "  type Bentuk interface {",
                    "      Luas() float64",
                    "      Keliling() float64",
                    "  }",
                    "",
                    "Setiap tipe yang punya kedua method itu OTOMATIS",
                    "memenuhi interface Bentuk. Tidak perlu menulis",
                    "'implements' seperti di Java.",
                    "",
                    "Ini disebut IMPLICIT IMPLEMENTATION atau duck typing",
                    "statis: kalau bersuara seperti bebek, ia bebek.",
                    "",
                    "Keuntungannya: kamu bisa membuat interface untuk tipe",
                    "yang sudah ada, bahkan dari library orang lain,",
                    "tanpa mengubah kode tipe itu.",
                    "",
                    "Interface kosong menerima nilai apa pun:",
                    "  interface{}   atau   any   (Go 1.18+)",
                ]
            },
            {
                "heading": "Interface dalam praktik",
                "code": """package main

import (
	"fmt"
	"math"
)

type Bentuk interface {
	Luas() float64
	Nama() string
}

type Persegi struct {
	Sisi float64
}

func (p Persegi) Luas() float64 { return p.Sisi * p.Sisi }
func (p Persegi) Nama() string  { return "Persegi" }

type Lingkaran struct {
	Jari float64
}

func (l Lingkaran) Luas() float64 { return math.Pi * l.Jari * l.Jari }
func (l Lingkaran) Nama() string  { return "Lingkaran" }

type Persegipanjang struct {
	Panjang, Lebar float64
}

func (r Persegipanjang) Luas() float64 { return r.Panjang * r.Lebar }
func (r Persegipanjang) Nama() string  { return "Persegi Panjang" }

// Satu fungsi melayani SEMUA tipe yang memenuhi Bentuk
func laporkan(b Bentuk) {
	fmt.Printf("%-16s luas %.2f\\n", b.Nama(), b.Luas())
}

func main() {
	daftar := []Bentuk{
		Persegi{Sisi: 4},
		Lingkaran{Jari: 3},
		Persegipanjang{Panjang: 5, Lebar: 2},
	}

	total := 0.0
	for _, b := range daftar {
		laporkan(b)
		total += b.Luas()
	}
	fmt.Printf("Total luas: %.2f\\n", total)

	// Type assertion: ambil tipe konkret di balik interface
	var b Bentuk = Persegi{Sisi: 10}
	if p, ok := b.(Persegi); ok {
		fmt.Println("Sisinya:", p.Sisi)
	}

	// Type switch
	for _, x := range daftar {
		switch v := x.(type) {
		case Persegi:
			fmt.Println("Persegi bersisi", v.Sisi)
		case Lingkaran:
			fmt.Println("Lingkaran berjari-jari", v.Jari)
		default:
			fmt.Println("Bentuk lain:", v.Nama())
		}
	}
}"""
            },
            {
                "body": [
                    "Prinsip penting soal interface di Go:",
                    "",
                    "1. BUAT INTERFACE SEKECIL MUNGKIN.",
                    "   Pepatah komunitas Go: 'The bigger the interface,",
                    "   the weaker the abstraction.'",
                    "   Banyak interface standar hanya punya satu method:",
                    "",
                    "     type Stringer interface { String() string }",
                    "     type Error interface { Error() string }",
                    "     type Reader interface { Read(p []byte) (int, error) }",
                    "     type Writer interface { Write(p []byte) (int, error) }",
                    "",
                    "2. Interface didefinisikan di sisi PEMAKAI, bukan",
                    "   di sisi pembuat tipe. Ini kebalikan dari Java.",
                    "",
                    "3. Terapkan Stringer supaya tipe kamu tampil rapi",
                    "   saat dicetak:",
                    "",
                    "     func (s Siswa) String() string {",
                    "         return s.Nama",
                    "     }",
                    "     fmt.Println(siswa)   -> otomatis memakai String()",
                    "",
                    "4. Type assertion punya dua bentuk:",
                    "     v := x.(Persegi)        panic kalau salah tipe",
                    "     v, ok := x.(Persegi)    aman, ok bernilai false",
                    "   SELALU pakai bentuk kedua kecuali kamu benar-benar",
                    "   yakin tipenya.",
                    "",
                    "5. Interface nil punya jebakan terkenal:",
                    "   Sebuah interface bernilai nil hanya kalau TIPE dan",
                    "   NILAI-nya sama-sama nil. Pointer nil yang disimpan",
                    "   di interface membuat interface itu TIDAK nil.",
                    "   Karena itu, jangan pernah mengembalikan pointer",
                    "   konkret bertipe error; kembalikan error langsung.",
                    "",
                    "6. METHOD SET: pointer receiver TIDAK ikut ke nilai biasa.",
                    "   Di materi Struct & Method kamu belajar Go otomatis",
                    "   menyesuaikan a.Ubah() jadi (&a).Ubah(). Untuk memenuhi",
                    "   interface, kemudahan itu TIDAK berlaku. Aturannya:",
                    "",
                    "     receiver Persegi   dimiliki Persegi DAN *Persegi",
                    "     receiver *Persegi  dimiliki *Persegi SAJA",
                    "",
                    "   Jadi kalau Luas() ditulis dengan pointer receiver",
                    "   'func (p *Persegi) Luas() float64', maka Persegi{Sisi: 4}",
                    "   di daftar []Bentuk pada kode di atas tidak lagi memenuhi",
                    "   Bentuk, dan compiler berkata:",
                    "",
                    "     cannot use Persegi{\u2026} (value of type Persegi) as",
                    "     Bentuk value in array or slice literal: Persegi does",
                    "     not implement Bentuk (method Luas has pointer receiver)",
                    "",
                    "   Klausa tengahnya ikut tempat kejadian: 'in array or slice",
                    "   literal' di sini, 'in variable declaration' kalau ditaruh",
                    "   di var, 'in argument to laporkan' kalau dioper ke fungsi.",
                    "   Yang selalu sama - dan yang perlu kamu kenali - adalah",
                    "   ekornya: method Luas has pointer receiver.",
                    "",
                    "   Obatnya satu tanda: tulis &Persegi{Sisi: 4}.",
                    "",
                    "   Pasang pemeriksa waktu kompilasi di berkas tipenya,",
                    "   supaya salahnya ketahuan di sana dan bukan jauh di",
                    "   tempat pemakaian:",
                    "     var _ Bentuk = (*Persegi)(nil)",
                    "   Baris itu tidak menyimpan apa pun - _ membuang nilainya",
                    "   - tapi memaksa compiler memeriksa bahwa *Persegi memang",
                    "   memenuhi Bentuk.",
                    "",
                    "   Inilah juga sebabnya materi Error Handling mengembalikan",
                    "   &ErrValidasi{...} dengan tanda &, dan memeriksanya lewat",
                    "   'var ev *ErrValidasi': Error() di sana ber-receiver",
                    "   pointer, jadi yang memenuhi interface error adalah",
                    "   *ErrValidasi, bukan ErrValidasi.",
                ]
            },
        ],
    },
    {
        "title": "15. Tipe Bentukan, Konstanta Berkelompok & iota",
        "sections": [
            {
                "body": [
                    "Sampai materi ini, setiap 'type' yang kamu tulis selalu struct atau",
                    "interface. Padahal bentuk paling ringkasnya justru ini:",
                    "",
                    "  type Celsius float64",
                    "  type Status int",
                    "  type KodePos string",
                    "  type Daftar []string",
                    "  type Validator func(string) error",
                    "",
                    "Artinya: buat TIPE BARU yang isinya sama persis dengan tipe di",
                    "kanannya. Yang di kanan itu disebut tipe dasarnya (underlying type).",
                    "Namanya tipe bentukan (defined type).",
                    "",
                    "Kenapa repot-repot? Karena di mata compiler tipe barunya BERBEDA",
                    "dari tipe dasarnya:",
                    "",
                    "  var c Celsius = 10",
                    "  var f float64 = c",
                    "  ERROR: cannot use c (variable of type Celsius) as float64 value",
                    "",
                    "  var f float64 = float64(c)   BENAR",
                    "",
                    "Dan dua tipe bentukan yang dasarnya sama pun tetap tidak bisa dicampur:",
                    "",
                    "  c + Fahrenheit(1)",
                    "  ERROR: invalid operation: mismatched types Celsius and Fahrenheit",
                    "",
                    "Di situlah gunanya. Detik dan meter sama-sama float64; begitu keduanya",
                    "jadi tipe sendiri, tidak ada lagi cara menjumlahkannya tanpa sadar.",
                    "Aturan 'konversi harus eksplisit' dari Materi 2 akhirnya bekerja UNTUK",
                    "kamu, bukan cuma merepotkanmu.",
                    "",
                    "Bonus terbesarnya:",
                    "METHOD BOLEH DIPASANG KE TIPE APA PUN yang dideklarasikan di package",
                    "yang sama, bukan cuma ke struct.",
                    "",
                    "  func (c Celsius) String() string { ... }",
                    "",
                    "Inilah jawaban atas pertanyaan yang muncul saat membaca kode orang:",
                    "'kok sebuah int/string/slice bisa punya method?'",
                    "",
                    "Satu-satunya larangan: kamu tidak boleh memasang method ke tipe milik",
                    "package lain, termasuk ke float64 atau string polos. Bungkus dulu jadi",
                    "tipe bentukan sendiri, baru pasang method.",
                ],
            },
            {
                "heading": "Tipe bentukan di atas angka, teks, slice, dan fungsi",
                "code": """package main

import (
	"errors"
	"fmt"
	"strings"
)

// Tipe bentukan: nama BARU di atas tipe yang sudah ada.
type Celsius float64
type Fahrenheit float64
type KodePos string
type Daftar []string
type Validator func(string) error

// Method boleh dipasang ke tipe apa pun, bukan cuma struct.
func (c Celsius) String() string { return fmt.Sprintf("%.1f C", float64(c)) }

func (c Celsius) KeFahrenheit() Fahrenheit {
	return Fahrenheit(float64(c)*9/5 + 32)
}

func (k KodePos) Sah() bool { return len(k) == 5 }

func (d Daftar) Gabung() string { return strings.Join(d, ", ") }

func tidakKosong(s string) error {
	if strings.TrimSpace(s) == "" {
		return errors.New("nilai tidak boleh kosong")
	}
	return nil
}

// Nama tipe fungsi bikin tanda tangan panjang jadi enak dibaca.
func periksa(nilai string, aturan Validator) {
	if err := aturan(nilai); err != nil {
		fmt.Printf("%q gagal: %v\\n", nilai, err)
		return
	}
	fmt.Printf("%q lolos\\n", nilai)
}

func main() {
	var suhu Celsius = 27.5
	fmt.Println("Suhu       :", suhu) // fmt memakai String()
	fmt.Println("Fahrenheit :", suhu.KeFahrenheit())

	// var f float64 = suhu   <- ERROR, Celsius bukan float64
	f := float64(suhu)
	fmt.Println("float64    :", f)

	// suhu + Fahrenheit(1)   <- ERROR, mismatched types
	fmt.Println("Dua kali   :", suhu*2)

	kode := KodePos("40115")
	fmt.Println("Kode sah?  :", kode.Sah())

	d := Daftar{"Andi", "Budi", "Citra"}
	fmt.Println("Daftar     :", d.Gabung())

	periksa("Bandung", tidakKosong)
	periksa("   ", tidakKosong)
}""",
            },
            {
                "body": [
                    "Konstanta boleh dikelompokkan dalam satu blok, sejajar dengan",
                    "var ( ... ) yang sudah kamu pakai di Materi 2:",
                    "",
                    "  const (",
                    "      Merah = \"merah\"",
                    "      Hijau = \"hijau\"",
                    "  )",
                    "",
                    "IOTA adalah pencacah yang hidup di dalam blok const:",
                    "  - Bernilai 0 di baris DEKLARASI pertama blok itu.",
                    "  - Naik satu tiap baris deklarasi berikutnya.",
                    "  - Baris kosong dan baris komentar TIDAK ikut dihitung.",
                    "  - Kembali ke 0 di setiap blok const yang baru.",
                    "",
                    "Satu aturan lagi yang membuat semuanya masuk akal:",
                    "BARIS TANPA TANDA SAMA DENGAN MENGULANG EKSPRESI BARIS SEBELUMNYA.",
                    "",
                    "  const (",
                    "      Draf     Status = iota   ditulis lengkap        -> 0",
                    "      Menunggu                 diam-diam sama         -> 1",
                    "      Aktif                    diam-diam sama         -> 2",
                    "  )",
                    "",
                    "Jadi nama-nama polos tanpa nilai itu bukan sihir: compiler menyalin",
                    "ulang ekspresi terakhir, dan iota-lah yang berubah tiap baris.",
                    "",
                    "Tiga variasi yang paling sering kamu temui di kode nyata:",
                    "",
                    "  _      Level = iota      buang nilai 0",
                    "  Senin  Hari  = iota + 1  mulai berhitung dari 1",
                    "  Baca   Izin  = 1 << iota  1, 2, 4, 8 ... satu bit per nama",
                    "",
                    "Yang terakhir memakai operator geser dari Materi 3, dan dipakai untuk",
                    "flag yang boleh digabung: Baca|Tulis muat dalam satu angka.",
                ],
            },
            {
                "heading": "Pola enum lengkap: type + const iota + String()",
                "code": """package main

import "fmt"

type Status int

const (
	Draf     Status = iota // 0
	Menunggu               // 1  baris kosong ini mengulang "Status = iota"
	Aktif                  // 2
	Ditolak                // 3
)

// Stringer: bikin angkanya tampil sebagai nama saat dicetak.
func (s Status) String() string {
	switch s {
	case Draf:
		return "Draf"
	case Menunggu:
		return "Menunggu"
	case Aktif:
		return "Aktif"
	case Ditolak:
		return "Ditolak"
	}
	// int(s), BUKAN %v. Lihat jebakan nomor 1 di bawah.
	return fmt.Sprintf("Status(%d)", int(s))
}

type Level int

const (
	_      Level = iota // 0 dibuang, biar zero value bukan level sah
	Rendah              // 1
	Sedang              // 2
	Tinggi              // 3
)

type Hari int

const (
	Senin  Hari = iota + 1 // 1
	Selasa                 // 2
	Rabu                   // 3
)

type Izin uint8

const (
	Baca  Izin = 1 << iota // 1 -> biner 001
	Tulis                  // 2 -> biner 010
	Hapus                  // 4 -> biner 100
)

func main() {
	s := Aktif
	fmt.Println("Status      :", s)      // "Aktif", bukan 2
	fmt.Println("Angkanya    :", int(s)) // 2
	fmt.Println("Tak dikenal :", Status(99))

	var belum Status
	fmt.Println("Zero value  :", belum) // hati-hati: ini Draf

	fmt.Printf("Level: %d %d %d\\n", Rendah, Sedang, Tinggi)
	fmt.Printf("Hari : %d %d %d\\n", Senin, Selasa, Rabu)

	punya := Baca | Tulis
	fmt.Printf("Izin        : %03b\\n", punya)
	fmt.Println("Boleh tulis :", punya&Tulis != 0)
	fmt.Println("Boleh hapus :", punya&Hapus != 0)

	punya |= Hapus // tambah satu izin
	punya &^= Baca // cabut satu izin
	fmt.Printf("Setelah ubah: %03b\\n", punya)
}""",
            },
            {
                "body": [
                    "POLA ENUM UTUH DI GO selalu tiga bagian. Kurang satu, terasa akibatnya:",
                    "  1. type Status int            supaya bukan sekadar int lepas",
                    "  2. blok const + iota          daftar nilainya",
                    "  3. func (s Status) String()   supaya tercetak sebagai nama",
                    "",
                    "Tanpa nomor 3, fmt.Println(status) mencetak 2, dan log-mu jadi deretan",
                    "angka yang harus ditebak. String() itu Stringer dari materi Interface;",
                    "fmt memakainya sendiri tanpa diminta.",
                    "",
                    "JEBAKAN YANG SUNGGUH MENJEBAK:",
                    "",
                    "1. String() yang memanggil dirinya sendiri.",
                    "   return fmt.Sprintf(\"Status(%v)\", s)",
                    "   -> fatal error: stack overflow. %v membuat fmt memanggil String()",
                    "   lagi, terus-menerus. Konversi dulu: fmt.Sprintf(\"...%d\", int(s)).",
                    "",
                    "2. Zero value diam-diam jadi nilai pertama.",
                    "   var s Status bernilai 0, dan 0 itu Draf. Struct yang lupa diisi",
                    "   terlihat seperti 'Draf' tanpa ada yang curiga. Kalau itu berbahaya,",
                    "   buang 0 dengan _ atau beri nama khusus seperti StatusTidakDikenal.",
                    "",
                    "3. Menyisipkan nama di TENGAH blok iota menggeser semua nilai di",
                    "   bawahnya. Kalau angka itu pernah tersimpan di database atau berkas,",
                    "   data lama mendadak berarti lain. Tambahkan nama baru di BAWAH.",
                    "",
                    "4. Tipe bentukan bukan pagar rapat: Status(99) tetap dikompilasi.",
                    "   Enum di Go itu kesepakatan, bukan jaminan. Nilai yang datang dari",
                    "   luar (input, JSON, database) tetap wajib kamu validasi sendiri.",
                    "",
                    "5. Tipe bentukan TIDAK mewarisi method tipe dasarnya.",
                    "   type Waktu time.Time membuat SEMUA method time.Time hilang:",
                    "   'w.Year undefined (type Waktu has no field or method Year)'.",
                    "   Kalau maunya menambah method, sematkan struct-nya (embedding,",
                    "   Materi 11), jangan bikin tipe bentukan.",
                    "",
                    "KONSTANTA TANPA TIPE (untyped constant):",
                    "  const Pi = 3.14     belum bertipe -> bisa jadi float32 ATAU float64",
                    "  const Batas = 100   bisa jadi int, int64, uint8, bahkan float64",
                    "",
                    "Karena itu suhu*2 di contoh pertama sah: angka 2 menyesuaikan diri jadi",
                    "Celsius. Begitu kamu tulis const Pi float64 = 3.14, ia terkunci, dan",
                    "var x float32 = Pi langsung ditolak compiler.",
                    "",
                    "Sekarang dua hal yang tadinya aneh jadi masuk akal:",
                    "  - 5 * time.Second sah karena time.Duration cuma 'type Duration int64'",
                    "    dan 5 itu konstanta tanpa tipe. Lihat lagi materi Angka & Waktu.",
                    "  - type HandlerFunc func(w, r) di net/http bukan barang ajaib, cuma",
                    "    tipe fungsi bernama, persis seperti Validator di contoh pertama.",
                ],
            },
        ],
    },
    {
        "title": "16. Error Handling",
        "sections": [
            {
                "body": [
                    "Go TIDAK punya exception, try, atau catch.",
                    "Error adalah nilai biasa yang dikembalikan fungsi.",
                    "",
                    "  hasil, err := lakukanSesuatu()",
                    "  if err != nil {",
                    "      return err",
                    "  }",
                    "",
                    "Pola 'if err != nil' akan kamu tulis ribuan kali.",
                    "Terasa bertele-tele, tapi keuntungannya besar:",
                    "  - Alur error terlihat jelas di kode, tidak tersembunyi",
                    "  - Tidak ada lompatan mendadak ke tempat lain",
                    "  - Compiler memaksa kamu memikirkan setiap kegagalan",
                    "",
                    "error sebenarnya cuma interface sederhana:",
                    "  type error interface {",
                    "      Error() string",
                    "  }",
                    "",
                    "Membuat error:",
                    "  errors.New(\"pesan\")",
                    "  fmt.Errorf(\"gagal memuat %s: %w\", nama, err)",
                    "",
                    "Kata kerja %w membungkus error asal supaya bisa",
                    "diperiksa lagi nanti dengan errors.Is atau errors.As.",
                ]
            },
            {
                "heading": "Menangani error",
                "code": """package main

import (
	"errors"
	"fmt"
)

// Error sentinel: bisa dibandingkan dengan errors.Is
var ErrSaldoKurang = errors.New("saldo tidak mencukupi")

// Error kustom dengan data tambahan
type ErrValidasi struct {
	Field string
	Pesan string
}

func (e *ErrValidasi) Error() string {
	return fmt.Sprintf("field %s: %s", e.Field, e.Pesan)
}

type Rekening struct {
	Pemilik string
	Saldo   int
}

func (r *Rekening) Tarik(jumlah int) error {
	if jumlah <= 0 {
		return &ErrValidasi{Field: "jumlah", Pesan: "harus lebih dari nol"}
	}
	if jumlah > r.Saldo {
		return fmt.Errorf("tarik %d dari saldo %d: %w",
			jumlah, r.Saldo, ErrSaldoKurang)
	}
	r.Saldo -= jumlah
	return nil
}

func main() {
	r := &Rekening{Pemilik: "Andi", Saldo: 100000}

	for _, jumlah := range []int{50000, 0, 200000} {
		err := r.Tarik(jumlah)

		switch {
		case err == nil:
			fmt.Printf("Tarik %d berhasil, sisa %d\\n", jumlah, r.Saldo)

		case errors.Is(err, ErrSaldoKurang):
			fmt.Println("DITOLAK, saldo kurang:", err)

		default:
			var ev *ErrValidasi
			if errors.As(err, &ev) {
				fmt.Println("INPUT SALAH pada", ev.Field, "-", ev.Pesan)
			} else {
				fmt.Println("Error lain:", err)
			}
		}
	}
}"""
            },
            {
                "body": [
                    "Tiga alat pemeriksa error:",
                    "",
                    "  errors.Is(err, ErrTarget)",
                    "    Cek apakah err ADALAH atau MEMBUNGKUS ErrTarget.",
                    "    Untuk error sentinel yang dibandingkan identitasnya.",
                    "",
                    "  errors.As(err, &target)",
                    "    Cek apakah err bertipe tertentu, sekaligus mengisi",
                    "    target supaya field-nya bisa dibaca.",
                    "",
                    "  errors.Unwrap(err)",
                    "    Ambil error yang dibungkus di dalamnya.",
                    "",
                    "MENGGABUNGKAN BEBERAPA KEGAGALAN",
                    "",
                    "Kadang satu pekerjaan gagal di lebih dari satu tempat",
                    "sekaligus, misalnya memvalidasi formulir. errors.Join",
                    "menyatukannya jadi satu error:",
                    "",
                    "  err := errors.Join(errNama, errUmur)",
                    "  errors.Is(err, errNama)   -> true",
                    "  errors.Is(err, errUmur)   -> true",
                    "",
                    "Yang nil diabaikan, dan kalau semuanya nil hasilnya juga",
                    "nil. Jadi aman menumpuk error satu per satu lalu memeriksa",
                    "sekali di akhir. Pesannya memuat tiap error di baris",
                    "sendiri.",
                    "",
                    "fmt.Errorf juga boleh memuat lebih dari satu %w:",
                    "  fmt.Errorf(\"simpan gagal: %w, lalu %w\", errTulis, errTutup)",
                    "",
                    "PANIC dan RECOVER",
                    "",
                    "panic menghentikan program seketika. Dipakai HANYA",
                    "untuk kondisi yang benar-benar tidak bisa dilanjutkan,",
                    "misalnya bug programmer, bukan kesalahan input user.",
                    "",
                    "  panic(\"ini seharusnya tidak pernah terjadi\")",
                    "",
                    "recover menangkap panic, tapi hanya bisa dipanggil",
                    "di dalam fungsi yang di-defer:",
                    "",
                    "  func aman() {",
                    "      defer func() {",
                    "          if r := recover(); r != nil {",
                    "              fmt.Println(\"Pulih dari panic:\", r)",
                    "          }",
                    "      }()",
                    "      panic(\"ada masalah\")",
                    "  }",
                    "",
                    "Aturan pakai:",
                    "  - Kesalahan yang WAJAR terjadi (file tidak ada,",
                    "    input salah, koneksi putus) -> kembalikan error.",
                    "  - Kondisi mustahil yang menandakan bug -> panic.",
                    "  - Jangan pakai panic sebagai pengganti exception.",
                    "",
                    "Jangan pernah abaikan error dengan _ kecuali kamu",
                    "benar-benar sadar konsekuensinya:",
                    "  hasil, _ := fungsiRawanGagal()   biasanya pertanda buruk",
                ]
            },
        ],
    },
    {
        "title": "17. Berkas: Membaca, Menulis & io.Reader/io.Writer",
        "sections": [
            {
                "body": [
                    "Sampai materi ini, semua yang dihitung programmu lenyap",
                    "begitu programnya berhenti. Berkas adalah cara paling",
                    "sederhana membuatnya bertahan.",
                    "",
                    "Go menyediakan DUA TINGKAT untuk pekerjaan yang sama, dan",
                    "memilih yang keliru adalah kesalahan pertama yang lazim:",
                    "",
                    "1. SEKALI JALAN -- seluruh isi masuk memori sekaligus.",
                    "   Cocok untuk berkas kecil: konfigurasi, catatan, CSV pendek.",
                    "",
                    "     data, err := os.ReadFile(\"stok.txt\")          // ([]byte, error)",
                    "     err := os.WriteFile(\"stok.txt\", data, 0644)   // error",
                    "",
                    "   os.ReadFile mengembalikan []byte, BUKAN string.",
                    "   Pakai string(data) kalau mau diperlakukan sebagai teks,",
                    "   dan []byte(teks) untuk arah sebaliknya saat menulis.",
                    "",
                    "2. BERTAHAP -- dibuka dulu, lalu dibaca atau ditulis",
                    "   sepotong demi sepotong. WAJIB untuk berkas besar:",
                    "   os.ReadFile pada berkas 4 GB berarti meminta 4 GB memori,",
                    "   dan program itu akan mati sebelum sempat mengerjakan apa pun.",
                    "",
                    "ANGKA 0644 ITU APA",
                    "",
                    "Itu izin akses ala Unix, dan awalan 0 membuatnya OKTAL",
                    "(basis 8) -- bukan enam ratus empat puluh empat. Boleh juga",
                    "ditulis 0o644 supaya lebih jelas.",
                    "Tiga digitnya berturut-turut: pemilik, grup, orang lain.",
                    "",
                    "  4 = boleh dibaca   2 = boleh ditulis   1 = boleh dijalankan",
                    "  6 = 4+2 = baca & tulis      7 = 4+2+1 = semuanya",
                    "",
                    "Jadi 0644 = pemilik baca+tulis, selain itu baca saja.",
                    "Untuk FOLDER pakai 0755: tanpa bit 1, folder itu tidak bisa",
                    "dimasuki siapa pun, termasuk pemiliknya sendiri.",
                    "Izin ini hanya berlaku saat berkasnya BARU dibuat; kalau",
                    "berkasnya sudah ada, izin lamanya dibiarkan apa adanya.",
                    "",
                    "MENAMBAH DI AKHIR, BUKAN MENIMPA",
                    "",
                    "  f, err := os.OpenFile(nama, os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)",
                    "",
                    "Tanda | menggabungkan bendera: tambah di akhir, buat kalau",
                    "belum ada, buka untuk menulis saja. Tanpa O_APPEND tulisanmu",
                    "menimpa dari posisi awal berkas.",
                    "os.Create(nama) sendiri sama artinya dengan bendera",
                    "O_RDWR|O_CREATE|O_TRUNC -- perhatikan TRUNC: berkas yang sudah",
                    "ada langsung DIKOSONGKAN. Itu bukan bug, itu memang tugasnya.",
                    "",
                    "MENYUSUN NAMA BERKAS",
                    "",
                    "  nama := filepath.Join(\"data\", \"2024\", \"stok.txt\")",
                    "",
                    "Jangan menyambung sendiri dengan \"data/\" + sub + \"/\" + berkas.",
                    "filepath.Join memakai pemisah yang benar di tiap sistem operasi",
                    "dan membereskan garis miring dobel yang tidak sengaja tertulis.",
                ],
            },
            {
                "heading": "Satu berkas dari nol sampai dihapus",
                "body": [
                    "Contoh ini membuat foldernya sendiri dan menghapusnya lagi di",
                    "akhir, jadi aman dijalankan berulang kali.",
                ],
                "code": """package main

import (
	"bufio"
	"errors"
	"fmt"
	"os"
	"path/filepath"
	"strings"
)

func main() {
	// filepath.Join menyusun path dengan pemisah yang benar di tiap sistem.
	folder := "gudang"
	if err := os.MkdirAll(folder, 0755); err != nil {
		fmt.Println("gagal membuat folder:", err)
		return
	}
	nama := filepath.Join(folder, "stok.txt")

	// 1. SEKALI JALAN: seluruh isi ditulis dalam satu panggilan.
	isi := "beras 12\\ngula 5\\nminyak 8\\n"
	if err := os.WriteFile(nama, []byte(isi), 0644); err != nil {
		fmt.Println("gagal menulis:", err)
		return
	}

	// 2. SEKALI JALAN: seluruh isi dibaca ke memori sebagai []byte.
	data, err := os.ReadFile(nama)
	if err != nil {
		fmt.Println("gagal membaca:", err)
		return
	}
	fmt.Printf("Terbaca %d byte:\\n%s", len(data), data)

	// 3. MENAMBAH di akhir tanpa menghapus yang sudah ada.
	f, err := os.OpenFile(nama, os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	if err != nil {
		fmt.Println("gagal membuka:", err)
		return
	}
	fmt.Fprintf(f, "%s %d\\n", "telur", 30)
	// Berkas yang DITULIS: error dari Close wajib diperiksa.
	if err := f.Close(); err != nil {
		fmt.Println("gagal menutup:", err)
		return
	}

	// 4. BARIS PER BARIS: satu baris di memori, bukan seluruh berkas.
	baca, err := os.Open(nama)
	if err != nil {
		fmt.Println("gagal membuka:", err)
		return
	}
	defer baca.Close()

	pemindai := bufio.NewScanner(baca)
	jumlah := 0
	for pemindai.Scan() {
		kolom := strings.Fields(pemindai.Text())
		fmt.Printf("  %-8s x%s\\n", kolom[0], kolom[1])
		jumlah++
	}
	// Loop di atas juga berhenti kalau ada KEGAGALAN, bukan cuma kalau habis.
	if err := pemindai.Err(); err != nil {
		fmt.Println("pembacaan terputus:", err)
		return
	}
	fmt.Println("Total baris:", jumlah)

	// 5. Berkas yang tidak ada: error-nya bisa dikenali, bukan ditebak.
	if _, err := os.ReadFile(filepath.Join(folder, "belum-ada.txt")); err != nil {
		if errors.Is(err, os.ErrNotExist) {
			fmt.Println("Belum pernah dibuat -- pakai nilai awal saja.")
		} else {
			fmt.Println("gagal lain:", err)
			return
		}
	}

	info, err := os.Stat(nama)
	if err != nil {
		fmt.Println("gagal stat:", err)
		return
	}
	fmt.Printf("%s berukuran %d byte\\n", info.Name(), info.Size())

	os.RemoveAll(folder)
}""",
            },
            {
                "body": [
                    "EMPAT JEBAKAN BERKAS YANG BENAR-BENAR SERING KENA",
                    "",
                    "1. LUPA scanner.Err()",
                    "   Loop 'for pemindai.Scan()' berhenti karena DUA sebab:",
                    "   berkasnya habis, atau pembacaannya GAGAL di tengah jalan.",
                    "   Tanpa memeriksa Err() sesudah loop, kegagalan terbaca",
                    "   sebagai 'sudah selesai', dan programmu melaporkan data",
                    "   setengah jadi sebagai data yang lengkap -- tanpa sepatah",
                    "   pun peringatan.",
                    "   Bawaan Scanner juga menyerah pada baris yang lebih panjang",
                    "   dari 64 KB. Itulah biang 'kok datanya kepotong' yang tidak",
                    "   pernah ketahuan kalau Err() tidak diperiksa.",
                    "",
                    "2. LUPA Flush PADA bufio.Writer",
                    "   bufio menumpuk tulisan di memori dan baru menyiramnya ke",
                    "   berkas kalau tumpukannya penuh. Program selesai tanpa",
                    "   Flush = berkas kosong atau terpotong, dan sekali lagi",
                    "   tanpa satu pun pesan error. Ini jebakan yang paling sering",
                    "   bikin orang mengira kodenya tidak pernah jalan.",
                    "",
                    "3. MENGABAIKAN ERROR DARI Close PADA BERKAS YANG DITULIS",
                    "   Tulisan terakhir bisa gagal justru pada saat ditutup --",
                    "   disk penuh, kuota habis, media dicabut. 'defer f.Close()'",
                    "   polos membuang error itu diam-diam.",
                    "   Bentuknya ada di contoh kedua: dua defer, dan karena defer",
                    "   dijalankan TERBALIK (lihat Materi Fungsi), yang didaftarkan",
                    "   belakangan -- Flush -- jalan lebih dulu, baru Close.",
                    "   Kalau urutannya terbalik, kamu menyiram ke berkas yang",
                    "   sudah ditutup.",
                    "   Untuk berkas yang cuma DIBACA, 'defer f.Close()' polos",
                    "   memang sudah cukup: tidak ada data yang bisa hilang.",
                    "",
                    "4. MEMERIKSA DULU, BARU MEMBUKA",
                    "   Bentuk yang salah:",
                    "     if _, err := os.Stat(nama); err == nil {",
                    "         f, _ := os.Open(nama)",
                    "     }",
                    "   Di antara dua baris itu berkasnya bisa dihapus proses lain.",
                    "   Langsung buka saja, lalu tanyai error-nya:",
                    "     f, err := os.Open(nama)",
                    "     if errors.Is(err, os.ErrNotExist) { ... }",
                    "",
                    "   Kenapa errors.Is dan bukan err == os.ErrNotExist?",
                    "   Karena os membungkus penyebabnya di dalam *os.PathError",
                    "   supaya pesannya menyebut nama berkasnya, jadi",
                    "   perbandingan == akan selalu false. Inilah gunanya",
                    "   errors.Is dari materi sebelumnya, dipakai pada error",
                    "   yang tidak kamu buat sendiri.",
                    "",
                    "FUNGSI BERKAS LAIN YANG SERING DIPAKAI",
                    "",
                    "  os.Stat(nama)           info: Size(), IsDir(), ModTime()",
                    "  os.Remove(nama)         hapus satu berkas",
                    "  os.RemoveAll(folder)    hapus folder beserta seluruh isinya",
                    "  os.MkdirAll(dir, 0755)  buat folder bertingkat sekaligus,",
                    "                          dan diam saja kalau sudah ada",
                    "  os.Rename(lama, baru)   pindahkan atau ganti nama",
                    "  os.ReadDir(folder)      daftar isi folder",
                ],
            },
            {
                "heading": "Satu fungsi, tiga tujuan yang berbeda",
                "code": """package main

import (
	"bufio"
	"bytes"
	"fmt"
	"io"
	"os"
	"strings"
)

type Barang struct {
	Nama   string
	Jumlah int
}

// Parameternya io.Writer, BUKAN *os.File. Fungsi yang sama jadi bisa mencetak
// ke layar, ke berkas, atau ke buffer di memori saat diuji.
func laporkan(w io.Writer, daftar []Barang) error {
	if _, err := fmt.Fprintln(w, "== STOK =="); err != nil {
		return err
	}
	for _, b := range daftar {
		if _, err := fmt.Fprintf(w, "%-8s %3d\\n", b.Nama, b.Jumlah); err != nil {
			return err
		}
	}
	return nil
}

// Parameternya io.Reader: sumbernya boleh berkas, os.Stdin, sebuah string,
// atau body HTTP -- fungsi ini tidak perlu tahu yang mana.
func hitungBaris(r io.Reader) (int, error) {
	data, err := io.ReadAll(r)
	if err != nil {
		return 0, err
	}
	return bytes.Count(data, []byte("\\n")), nil
}

// err bernama supaya defer bisa mengubahnya (lihat Materi Fungsi).
func simpan(nama string, daftar []Barang) (err error) {
	f, err := os.Create(nama)
	if err != nil {
		return err
	}
	w := bufio.NewWriter(f)
	// Didaftarkan lebih dulu = dijalankan paling akhir. Urutannya: Flush, Close.
	defer func() {
		if cerr := f.Close(); err == nil {
			err = cerr
		}
	}()
	defer func() {
		if ferr := w.Flush(); err == nil {
			err = ferr
		}
	}()
	return laporkan(w, daftar)
}

func main() {
	daftar := []Barang{{"beras", 12}, {"gula", 5}}

	// Tujuan 1: layar.
	if err := laporkan(os.Stdout, daftar); err != nil {
		fmt.Println("gagal:", err)
		return
	}

	// Tujuan 2: buffer di memori. Beginilah fungsi seperti ini diuji.
	var buf bytes.Buffer
	if err := laporkan(&buf, daftar); err != nil {
		fmt.Println("gagal:", err)
		return
	}
	fmt.Println("Panjang laporan:", buf.Len(), "byte")

	// Tujuan 3: berkas. Isi fungsi laporkan tidak berubah sedikit pun.
	if err := simpan("stok.txt", daftar); err != nil {
		fmt.Println("gagal:", err)
		return
	}

	// Satu fungsi pembaca, dua sumber yang sama sekali berbeda.
	n, err := hitungBaris(strings.NewReader("a\\nb\\nc\\n"))
	if err != nil {
		fmt.Println("gagal:", err)
		return
	}
	fmt.Println("Baris dari string:", n)

	f, err := os.Open("stok.txt")
	if err != nil {
		fmt.Println("gagal:", err)
		return
	}
	defer f.Close()

	// io.Copy menyalin dari Reader mana pun ke Writer mana pun, sepotong
	// demi sepotong -- berkas 2 GB pun tidak perlu masuk memori.
	if _, err := io.Copy(os.Stdout, f); err != nil {
		fmt.Println("gagal:", err)
		return
	}

	os.Remove("stok.txt")
}""",
            },
            {
                "body": [
                    "io.Reader dan io.Writer masing-masing hanya punya SATU method",
                    "(kamu sudah melihat definisinya di Materi Interface). Justru",
                    "karena sekecil itu, hampir semua hal di Go memenuhinya:",
                    "",
                    "  MEMBACA (io.Reader)        MENULIS (io.Writer)",
                    "  ----------------------     ----------------------",
                    "  *os.File dari os.Open      *os.File dari os.Create",
                    "  os.Stdin                   os.Stdout dan os.Stderr",
                    "  strings.NewReader(s)       *bytes.Buffer",
                    "  bytes.NewReader(b)         bufio.NewWriter(w)",
                    "  resp.Body (jawaban HTTP)   http.ResponseWriter",
                    "  net.Conn (koneksi)         net.Conn (koneksi)",
                    "  gzip, tar, csv, json       gzip, tar, csv, json",
                    "",
                    "AKIBAT PRAKTISNYA, dan ini yang mengubah cara menulis kode:",
                    "tulis func laporkan(w io.Writer, ...) alih-alih",
                    "func laporkan(f *os.File, ...). Biayanya nol huruf tambahan,",
                    "hasilnya satu fungsi yang bisa mencetak ke layar, menyimpan ke",
                    "berkas, mengirim ke jaringan, dan -- yang paling berharga --",
                    "diuji dengan bytes.Buffer tanpa menyentuh disk sama sekali.",
                    "Aturan yang sama berlaku untuk arah baca: terima io.Reader,",
                    "bukan *os.File, supaya bisa diuji dengan strings.NewReader.",
                    "",
                    "DUA FUNGSI PEMBANTU YANG SELALU ADA",
                    "",
                    "  data, err := io.ReadAll(r)     baca habis jadi []byte",
                    "  n, err := io.Copy(dst, src)    salin Reader mana pun ke",
                    "                                 Writer mana pun",
                    "",
                    "io.Copy menyalin sepotong demi sepotong, jadi berkas 2 GB pun",
                    "tidak perlu muat di memori. io.ReadAll sebaliknya: memuat",
                    "semuanya, jadi jangan diarahkan ke sumber yang tak terbatas.",
                    "",
                    "STDOUT vs STDERR",
                    "",
                    "fmt.Println menulis ke os.Stdout -- itu jalur HASIL, yang",
                    "orang salurkan (pipe) ke program lain. Pesan kesalahan dan",
                    "laporan kemajuan harus lewat jalur lain:",
                    "",
                    "  fmt.Fprintln(os.Stderr, \"gagal membuka:\", err)",
                    "",
                    "Kalau keduanya dicampur, orang yang menjalankan",
                    "'./program > hasil.txt' akan menemukan pesan errormu ikut",
                    "tersimpan rapi di dalam berkas hasilnya.",
                    "",
                    "Terakhir: bungkus dengan bufio kalau kamu menulis atau membaca",
                    "BANYAK potongan kecil. Satu Write langsung ke *os.File berarti",
                    "satu panggilan sistem operasi; bufio menggabungkan ribuan",
                    "tulisan kecil jadi beberapa tulisan besar. Dan sekali lagi:",
                    "jangan lupa Flush.",
                ],
            },
        ],
    },
    {
        "title": "18. Program Baris Perintah: Argumen, flag & log",
        "sections": [
            {
                "body": [
                    "Materi 4 mengajarkan program yang menunggu ketikan lewat stdin. Alat",
                    "sungguhan jarang bekerja begitu. Perintah yang kamu pakai tiap hari",
                    "menerima masukannya langsung dari BARIS PERINTAH:",
                    "",
                    "  go build -o server main.go",
                    "  grep -n \"halo\" catatan.txt",
                    "",
                    "Kata-kata setelah nama program itu disebut ARGUMEN. Di Go semuanya",
                    "masuk ke satu slice string bernama os.Args.",
                    "",
                    "  ./sapa Levi --keras",
                    "",
                    "  os.Args[0]    \"./sapa\"    nama/jalur programnya SENDIRI",
                    "  os.Args[1]    \"Levi\"",
                    "  os.Args[2]    \"--keras\"",
                    "  len(os.Args)  3",
                    "",
                    "Argumen yang sesungguhnya mulai dari indeks 1, bukan 0. Itu sumber",
                    "panic pertama buat pemula:",
                    "",
                    "  nama := os.Args[1]",
                    "",
                    "  panic: runtime error: index out of range [1] with length 1",
                    "",
                    "Programnya mati begitu dijalankan tanpa argumen. Jadi hitung dulu:",
                    "",
                    "  if len(os.Args) < 2 {",
                    "      fmt.Fprintln(os.Stderr, \"cara pakai: sapa <nama>\")",
                    "      os.Exit(1)",
                    "  }",
                    "",
                    "Dua hal baru di potongan itu:",
                    "",
                    "  fmt.Fprintln(os.Stderr, ...)",
                    "    Sama seperti fmt.Println, tapi tujuannya ditentukan sendiri.",
                    "    os.Stderr adalah aliran untuk pesan buat MANUSIA; os.Stdout",
                    "    untuk hasil yang mungkin dipipe ke perintah lain. Alasan",
                    "    lengkapnya di bagian terakhir materi ini.",
                    "",
                    "  os.Exit(1)",
                    "    Menghentikan program sekarang juga sambil menyerahkan satu",
                    "    angka ke shell: 0 berarti BERHASIL, selain nol berarti GAGAL.",
                    "    Terbalik dari dugaan, tapi angka itulah yang dibaca && dan ||",
                    "    di shell, dan yang dipakai CI untuk memutuskan build merah",
                    "    atau hijau. main yang selesai wajar otomatis bernilai 0.",
                ],
            },
            {
                "heading": "Membaca os.Args apa adanya",
                "code": """package main

import (
	"fmt"
	"os"
)

func main() {
	fmt.Println("Nama program  :", os.Args[0])
	fmt.Println("Jumlah argumen:", len(os.Args)-1)

	if len(os.Args) < 2 {
		fmt.Fprintln(os.Stderr, "Belum ada argumen sama sekali.")
		fmt.Fprintln(os.Stderr, "Coba jalankan lagi: go run main.go halo dunia")
		return
	}

	for i, arg := range os.Args[1:] {
		fmt.Printf("  argumen ke-%d = %q\\n", i+1, arg)
	}

	if os.Args[1] == "--versi" {
		fmt.Println("versi 1.0")
	}
}""",
            },
            {
                "body": [
                    "Jalankan dua kali supaya bedanya terasa:",
                    "",
                    "  $ go run main.go",
                    "  Nama program  : /tmp/go-build3487/b001/exe/main",
                    "  Jumlah argumen: 0",
                    "  Belum ada argumen sama sekali.",
                    "  Coba jalankan lagi: go run main.go halo dunia",
                    "",
                    "  $ go run main.go --versi \"dua kata\"",
                    "  Nama program  : /tmp/go-build9051/b001/exe/main",
                    "  Jumlah argumen: 2",
                    "    argumen ke-1 = \"--versi\"",
                    "    argumen ke-2 = \"dua kata\"",
                    "  versi 1.0",
                    "",
                    "Perhatikan os.Args[0]: dengan go run isinya jalur biner sementara",
                    "yang aneh dan angkanya berganti tiap kali dijalankan, karena go run",
                    "memang mengompilasi ke folder sementara dulu. Setelah go build,",
                    "isinya jalur binermu sendiri. Jangan pernah memakai os.Args[0]",
                    "sebagai data; ia cuma untuk pesan bantuan.",
                    "Perhatikan juga \"dua kata\": shell yang menyatukannya jadi SATU",
                    "argumen karena diberi tanda kutip.",
                    "",
                    "Mengurus flag sendiri seperti baris '--versi' di atas cepat kacau",
                    "begitu flagnya lebih dari dua: kamu harus mengatur urutan, nilai",
                    "bawaan, bentuk --x=1, dan teks bantuan. Package flag dari pustaka",
                    "standar sudah melakukan semuanya.",
                    "",
                    "  nama := flag.String(\"nama\", \"dunia\", \"nama yang disapa\")",
                    "  ulang := flag.Int(\"ulang\", 1, \"berapa kali dicetak\")",
                    "  keras := flag.Bool(\"keras\", false, \"pakai huruf kapital\")",
                    "  flag.Parse()",
                    "",
                    "Urutannya wajib begitu: daftarkan SEMUA flag dulu, baru flag.Parse().",
                    "",
                    "YANG PALING BIKIN BINGUNG: flag.String tidak mengembalikan string.",
                    "Ia mengembalikan *string, sebuah POINTER (materi Pointer).",
                    "",
                    "  fmt.Println(nama)    mencetak alamatnya: 0xc000010030",
                    "  fmt.Println(*nama)   mencetak isinya   : dunia",
                    "",
                    "Alasannya masuk akal begitu dipikirkan: saat baris flag.String",
                    "dieksekusi, argumen belum dibaca sama sekali. Fungsi itu cuma",
                    "memesan sebuah kotak kosong dan menyerahkan alamatnya; flag.Parse()",
                    "yang mengisi kotak itu nanti. Akibat langsungnya: membaca *nama",
                    "SEBELUM flag.Parse() selalu memberi nilai bawaan, bukan yang",
                    "diketik pemakai — bug yang senyap karena programnya tetap jalan.",
                    "",
                    "Kalau variabelnya sudah ada (sering dipakai untuk mengisi field",
                    "struct konfigurasi), pakai bentuk ...Var yang tanpa pointer:",
                    "",
                    "  var nama string",
                    "  flag.StringVar(&nama, \"nama\", \"dunia\", \"nama yang disapa\")",
                    "",
                    "Tersedia juga IntVar, BoolVar, Float64Var, dan DurationVar.",
                    "",
                    "Argumen yang BUKAN flag diambil terpisah:",
                    "  flag.Args()   []string berisi argumen posisional",
                    "  flag.NArg()   jumlahnya",
                    "  flag.Arg(0)   yang pertama",
                    "",
                    "Empat jebakan yang sungguh sering menjerat:",
                    "",
                    "  1. flag BERHENTI membaca di argumen bukan-flag yang pertama.",
                    "       ./sapa -keras Levi    -keras terbaca sebagai flag",
                    "       ./sapa Levi -keras    -keras jadi argumen biasa, TIDAK aktif",
                    "     Tulis semua flag di depan. Banyak program lain membolehkan",
                    "     urutan bebas, package flag tidak.",
                    "",
                    "  2. Flag bool tidak menerima nilainya terpisah.",
                    "       -keras          benar, artinya true",
                    "       -keras=false    benar",
                    "       -keras false    'false' jadi argumen posisional, flagnya",
                    "                       tetap TRUE. Diam-diam salah.",
                    "",
                    "  3. Satu strip dan dua strip sama saja: -nama dan --nama identik.",
                    "",
                    "  4. Flag tak dikenal atau nilai salah tipe membuat program",
                    "     mencetak bantuan lalu keluar dengan kode 2, tanpa kamu",
                    "     menulis satu pun pemeriksaan.",
                    "",
                    "-h dan -help tersedia otomatis tanpa didaftarkan. Isinya disusun",
                    "dari argumen ketiga tiap flag, jadi kalimat itu bukan komentar —",
                    "ia dibaca pemakai.",
                ],
            },
            {
                "heading": "flag, log, dan pola main yang benar",
                "code": """package main

import (
	"flag"
	"fmt"
	"log"
	"os"
	"strings"
)

func main() {
	if err := jalankan(); err != nil {
		log.Fatal(err)
	}
}

func jalankan() error {
	nama := flag.String("nama", "dunia", "nama yang disapa")
	ulang := flag.Int("ulang", 1, "berapa kali sapaan dicetak")
	keras := flag.Bool("keras", false, "cetak dengan huruf kapital")
	flag.Parse()

	// Awalan "sapa: " menandai pesan ini milik siapa; flag 0 mematikan
	// tanggal & jam supaya keluarannya sama persis tiap dijalankan.
	catat := log.New(os.Stderr, "sapa: ", 0)
	defer catat.Println("selesai")

	if lokasi, ada := os.LookupEnv("SAPA_LOKASI"); ada {
		catat.Println("lokasi dari environment:", lokasi)
	} else {
		catat.Println("SAPA_LOKASI belum diset, memakai bawaan")
	}

	if *ulang < 1 {
		return fmt.Errorf("-ulang minimal 1, dapat %d", *ulang)
	}

	sapaan := "Halo, " + *nama + "!"
	if *keras {
		sapaan = strings.ToUpper(sapaan)
	}
	for i := 0; i < *ulang; i++ {
		fmt.Println(sapaan)
	}

	if sisa := flag.Args(); len(sisa) > 0 {
		catat.Println("argumen sisa:", strings.Join(sisa, ", "))
	}
	return nil
}""",
            },
            {
                "body": [
                    "Tiga cara menjalankannya, dan apa yang keluar:",
                    "",
                    "  $ go run main.go",
                    "  sapa: SAPA_LOKASI belum diset, memakai bawaan",
                    "  Halo, dunia!",
                    "  sapa: selesai",
                    "",
                    "  $ go run main.go -nama Levi -ulang 2 -keras berkas.txt",
                    "  sapa: SAPA_LOKASI belum diset, memakai bawaan",
                    "  HALO, LEVI!",
                    "  HALO, LEVI!",
                    "  sapa: argumen sisa: berkas.txt",
                    "  sapa: selesai",
                    "",
                    "  $ SAPA_LOKASI=Bontang go run main.go",
                    "  sapa: lokasi dari environment: Bontang",
                    "  Halo, dunia!",
                    "  sapa: selesai",
                    "",
                    "PACKAGE log",
                    "log.Println dan log.Printf mirip fmt, beda di dua hal:",
                    "  - Tujuannya STDERR, bukan stdout.",
                    "  - Tiap baris otomatis diberi tanggal dan jam.",
                    "",
                    "  log.Println(\"mulai\")",
                    "  2025/07/01 09:14:22 mulai",
                    "",
                    "Itulah jawaban 'kenapa keluaran log kelihatan beda dari fmt.Println'.",
                    "Yang bisa diatur:",
                    "  log.SetFlags(0)              matikan tanggal & jam",
                    "  log.SetFlags(log.LstdFlags | log.Lshortfile)  tambah berkas:baris",
                    "  log.SetPrefix(\"sapa: \")      awalan tetap di tiap baris",
                    "  log.New(os.Stderr, \"sapa: \", log.LstdFlags)   logger sendiri",
                    "",
                    "log.Fatal(err) = log.Print(err) LALU os.Exit(1).",
                    "Ini jawaban atas 'kenapa programku berhenti tepat di baris itu',",
                    "padahal tidak ada panic dan tidak ada jejak error panjang khas Go.",
                    "Ada log.Fatalf untuk versi berformat, dan log.Panic yang mencetak",
                    "lalu panic — panic itu masih bisa ditangkap recover (materi Error",
                    "Handling), sedangkan Fatal tidak bisa dihentikan siapa pun.",
                    "",
                    "JEBAKAN BESARNYA: os.Exit, dan karena itu juga log.Fatal, TIDAK",
                    "menjalankan defer yang tertunda.",
                    "",
                    "  defer f.Close()",
                    "  log.Fatal(err)    f tidak pernah ditutup, berkas sementara",
                    "                    tidak terhapus, kunci tidak dilepas",
                    "",
                    "Itu sebabnya main yang idiomatis memisahkan pekerjaannya:",
                    "",
                    "  func main() {",
                    "      if err := jalankan(); err != nil {",
                    "          log.Fatal(err)",
                    "      }",
                    "  }",
                    "",
                    "jalankan() cuma MENGEMBALIKAN error. Saat ia return, semua defer di",
                    "dalamnya sempat jalan, baru main mematikan program. Buktikan sendiri:",
                    "'go run main.go -ulang 0' mencetak 'sapa: selesai' LEBIH DULU, baru",
                    "baris Fatal-nya. Baris 'exit status 1' sesudahnya datang dari go run,",
                    "bukan dari programmu — biner hasil go build tidak mencetaknya.",
                    "",
                    "ATURAN PAKAI: log.Fatal dan os.Exit hanya boleh di main. Jangan",
                    "pernah di dalam fungsi yang dipakai orang lain. Fungsi library yang",
                    "memanggil log.Fatal mematikan seluruh program pemanggilnya tanpa",
                    "memberi kesempatan menangani apa pun, dan mustahil diuji dengan",
                    "go test. Fungsi mengembalikan error; yang memutuskan berhenti main.",
                    "",
                    "VARIABEL LINGKUNGAN",
                    "  os.Getenv(\"HOME\")               isinya, atau \"\" kalau tidak ada",
                    "  nilai, ada := os.LookupEnv(\"X\")   'ada' membedakan diset-tapi-",
                    "                                   kosong dari tidak diset",
                    "Getenv tidak bisa membedakan keduanya, jadi pakai LookupEnv kalau",
                    "string kosong adalah pilihan yang sah. Mengisinya untuk satu",
                    "jalan saja: SAPA_LOKASI=Bontang go run main.go",
                    "",
                    "STDOUT vs STDERR, DAN KENAPA DIPISAH",
                    "  stdout = HASIL program, yang layak dipipe ke perintah berikutnya",
                    "  stderr = pesan untuk manusia: log, peringatan, cara pakai",
                    "",
                    "  $ go run main.go > hasil.txt",
                    "  sapa: SAPA_LOKASI belum diset, memakai bawaan",
                    "  sapa: selesai",
                    "",
                    "hasil.txt cuma berisi 'Halo, dunia!' — baris log tetap muncul di",
                    "layar karena tidak ikut dialihkan. Kalau log dicetak ke stdout,",
                    "setiap orang yang mem-pipe programmu menerima catatanmu sebagai",
                    "data dan alatnya jadi tidak bisa dirangkai. Itulah alasan package",
                    "log memilih stderr sejak awal.",
                ],
            },
        ],
    },
    {
        "title": "19. JSON & Struct Tag",
        "sections": [
            {
                "body": [
                    "JSON (JavaScript Object Notation) adalah format teks untuk",
                    "bertukar data. Hampir semua API di internet menjawab dengan",
                    "JSON, dan sebagian besar berkas konfigurasi modern memakainya.",
                    "",
                    "Go menyediakannya lewat package standar encoding/json.",
                    "Tidak ada yang perlu dipasang.",
                    "",
                    "Dua arah yang harus kamu kuasai:",
                    "",
                    "  struct Go   --Marshal-->    teks JSON   (data keluar)",
                    "  teks JSON   --Unmarshal->   struct Go   (data masuk)",
                    "",
                    "Tanda tangan keduanya:",
                    "",
                    "  func Marshal(v any) ([]byte, error)",
                    "  func Unmarshal(data []byte, v any) error",
                    "",
                    "Marshal mengembalikan []byte, BUKAN string. Untuk melihatnya",
                    "bungkus dengan string(data). Sebaliknya Unmarshal menerima",
                    "[]byte, jadi teks harus dibungkus []byte(teks).",
                    "MarshalIndent sama persis, hanya hasilnya diberi indentasi",
                    "supaya enak dibaca manusia:",
                    "",
                    "  json.MarshalIndent(b, \"\", \"  \")   awalan \"\", indentasi 2 spasi",
                    "",
                    "KENAPA UNMARSHAL HARUS PAKAI &",
                    "",
                    "  var b Barang",
                    "  err := json.Unmarshal(data, &b)",
                    "",
                    "Unmarshal bertugas MENGISI variabel milik pemanggil. Sama",
                    "seperti di materi Pointer: Go selalu mengirim salinan, jadi",
                    "fungsi yang perlu mengubah variabel aslinya wajib menerima",
                    "alamatnya. Lupa & tidak ditangkap compiler. Programnya tetap",
                    "dikompilasi, lalu saat jalan mengembalikan error",
                    "\"json: Unmarshal(non-pointer main.Barang)\" dan struct-mu",
                    "tetap kosong.",
                    "",
                    "HANYA FIELD BERHURUF BESAR YANG IKUT",
                    "",
                    "Aturan visibilitas yang sudah kamu pelajari punya akibat yang",
                    "sangat nyata di sini. encoding/json adalah package LAIN, jadi",
                    "ia sama sekali tidak bisa melihat field berhuruf kecil. Field",
                    "seperti 'kategori string' hilang dari hasil Marshal dan tetap",
                    "kosong sesudah Unmarshal, tanpa satu pun error, panic, atau",
                    "peringatan. Ini penyebab nomor satu dari pertanyaan",
                    "\"kenapa JSON-ku keluar cuma {}?\".",
                ],
            },
            {
                "heading": "Marshal, Unmarshal, dan struct tag",
                "code": """package main

import (
	"encoding/json"
	"fmt"
)

type Barang struct {
	Kode     string  `json:"kode"`
	Nama     string  `json:"nama"`
	Harga    int     `json:"harga"`
	Diskon   float64 `json:"diskon,omitempty"`
	Catatan  string  `json:"-"`
	kategori string
}

func main() {
	b := Barang{
		Kode:     "B001",
		Nama:     "Beras 5kg",
		Harga:    65000,
		Catatan:  "hanya untuk gudang",
		kategori: "pangan",
	}

	data, err := json.Marshal(b)
	if err != nil {
		fmt.Println("gagal marshal:", err)
		return
	}
	fmt.Println(string(data))

	rapi, _ := json.MarshalIndent(b, "", "  ")
	fmt.Println(string(rapi))

	teks := `{"kode":"B002","nama":"Gula 1kg","harga":15000,"diskon":0.1}`

	var masuk Barang
	if err := json.Unmarshal([]byte(teks), &masuk); err != nil {
		fmt.Println("JSON rusak:", err)
		return
	}
	fmt.Println("Kode  :", masuk.Kode)
	fmt.Println("Nama  :", masuk.Nama)
	fmt.Printf("Bayar : %.0f\\n", float64(masuk.Harga)*(1-masuk.Diskon))
	fmt.Printf("Catatan tetap kosong: %q, kategori juga: %q\\n",
		masuk.Catatan, masuk.kategori)
}""",
            },
            {
                "body": [
                    "Perhatikan keluaran program di atas: Diskon tidak muncul di",
                    "JSON pertama (karena 0 dan bertanda omitempty), Catatan tidak",
                    "pernah muncul (bertanda \"-\"), dan kategori tidak muncul",
                    "karena huruf awalnya kecil.",
                    "",
                    "ANATOMI STRUCT TAG",
                    "",
                    "  Nama string `json:\"nama\"`",
                    "",
                    "Yang di dalam backtick itu BUKAN komentar dan BUKAN nilai",
                    "bawaan. Ia sebuah string mentah (raw string) yang menempel",
                    "pada field dan ikut tersimpan di dalam tipe itu sendiri.",
                    "Backtick dipilih supaya tanda petik di dalamnya tidak perlu",
                    "di-escape. Tulisannya rapat, TIDAK ADA spasi sesudah titik dua:",
                    "",
                    "  `json:\"nama\"`     benar",
                    "  `json: \"nama\"`    diam-diam tidak berlaku",
                    "",
                    "Tanpa tag sama sekali, nama di JSON mengikuti nama field Go",
                    "apa adanya, jadi Harga menghasilkan {\"Harga\":15000} dengan H",
                    "besar. Itu jarang cocok dengan API yang menuntut huruf kecil.",
                    "",
                    "Opsi ditulis sesudah nama, dipisah koma:",
                    "",
                    "  `json:\"diskon,omitempty\"`  jangan tulis kalau nilainya kosong",
                    "  `json:\"-\"`                 jangan ikutkan sama sekali",
                    "  `json:\"harga,string\"`      angkanya ditulis sebagai \"15000\"",
                    "",
                    "Opsi \",string\" ada karena JavaScript kehilangan ketelitian di",
                    "atas 2^53; banyak API mengirim ID besar sebagai teks.",
                    "",
                    "Empat jebakan yang sungguh sering kena:",
                    "",
                    "  1. omitempty memakai definisi 'kosong' milik Go: 0, \"\",",
                    "     false, nil, slice dan map kosong. Struct bersarang TIDAK",
                    "     pernah dianggap kosong, jadi omitempty di atasnya tidak",
                    "     berefek apa-apa.",
                    "  2. `json:\"-\"` membuang field. Kalau kamu benar-benar ingin",
                    "     field bernama \"-\", tulis `json:\"-,\"` pakai koma.",
                    "  3. Nama tag yang salah ketik tidak pernah dilaporkan siapa",
                    "     pun. Field-nya cuma diam-diam kosong terus.",
                    "  4. Field di JSON yang tidak punya pasangan di struct",
                    "     DIABAIKAN, juga tanpa error. Kalau kamu ingin ditolak,",
                    "     pakai dec.DisallowUnknownFields().",
                    "",
                    "BENTUK YANG SAMA DIBACA LIBRARY LAIN",
                    "",
                    "Satu field boleh membawa beberapa tag sekaligus, dipisah spasi:",
                    "",
                    "  Kode string `json:\"kode\" db:\"kode\" validate:\"required\"`",
                    "",
                    "  json      encoding/json, bagian dari Go sendiri",
                    "  db        library database seperti sqlx",
                    "  yaml      pembaca berkas konfigurasi YAML",
                    "  xml       encoding/xml",
                    "  validate  pemeriksa isi seperti go-playground/validator",
                    "",
                    "Go sendiri tidak mengerti arti \"db\" atau \"validate\". Bagi",
                    "compiler semuanya cuma teks; yang membacanya adalah library",
                    "yang bersangkutan, saat program berjalan. Itulah sebabnya tag",
                    "yang salah tulis tidak pernah menggagalkan kompilasi.",
                    "",
                    "Sekarang kamu punya penjelasan untuk backtick yang menempel",
                    "di belakang hampir setiap field struct di kode Go sungguhan.",
                ],
            },
            {
                "heading": "Bersarang, pointer field, dan JSON tanpa struct",
                "code": """package main

import (
	"encoding/json"
	"fmt"
	"os"
	"strings"
)

type Alamat struct {
	Kota string `json:"kota"`
	Pos  string `json:"kode_pos"`
}

type Pelanggan struct {
	Nama   string   `json:"nama"`
	Alamat Alamat   `json:"alamat"`
	Tag    []string `json:"tag"`
	Poin   *int     `json:"poin"`
}

const teksJSON = `[
  {"nama":"Andi","alamat":{"kota":"Bandung","kode_pos":"40111"},
   "tag":["baru","vip"],"poin":0},
  {"nama":"Budi","alamat":{"kota":"Medan","kode_pos":"20111"},
   "tag":[],"poin":null}
]`

func main() {
	// Array JSON -> slice struct, objek bersarang -> struct bersarang
	var daftar []Pelanggan
	if err := json.Unmarshal([]byte(teksJSON), &daftar); err != nil {
		fmt.Println("JSON rusak:", err)
		return
	}

	for _, p := range daftar {
		tag := "[" + strings.Join(p.Tag, " ") + "]"
		fmt.Printf("%-5s %-8s %-12s ", p.Nama, p.Alamat.Kota, tag)
		if p.Poin == nil {
			fmt.Println("poin: TIDAK ADA / null")
		} else {
			fmt.Println("poin:", *p.Poin)
		}
	}

	// Tanpa struct: semua nilai jadi any, dan angka SELALU float64
	var bebas map[string]any
	if err := json.Unmarshal([]byte(`{"nama":"Citra","umur":30}`), &bebas); err != nil {
		fmt.Println("JSON rusak:", err)
		return
	}
	for _, k := range []string{"nama", "umur", "kota"} {
		nilai, ada := bebas[k]
		fmt.Printf("%-5s ada=%-5t tipe=%-8T nilai=%v\\n", k, ada, nilai, nilai)
	}
	if umur, ok := bebas["umur"].(float64); ok {
		fmt.Println("umur sebagai int:", int(umur))
	}

	// Encoder menulis ke io.Writer apa pun -- di sini layar
	enc := json.NewEncoder(os.Stdout)
	enc.SetIndent("", "  ")
	if err := enc.Encode(daftar[1]); err != nil {
		fmt.Println("gagal encode:", err)
	}

	// Decoder membaca io.Reader apa pun -- di sini sebuah string
	var satu Pelanggan
	if err := json.NewDecoder(strings.NewReader(`{"NaMa":"Dedi"}`)).Decode(&satu); err != nil {
		fmt.Println("gagal decode:", err)
	}
	fmt.Printf("cocok walau beda huruf besar-kecil: %q\\n", satu.Nama)

	// Koma menggantung: sah di Go, TERLARANG di JSON
	var rusak Pelanggan
	err := json.Unmarshal([]byte(`{"nama":"Eka",}`), &rusak)
	fmt.Println("err =", err)
	fmt.Printf("isinya: nama=%q kota=%q poin=%v\\n",
		rusak.Nama, rusak.Alamat.Kota, rusak.Poin)
}""",
            },
            {
                "body": [
                    "MEMBEDAKAN 'BERNILAI NOL' DARI 'TIDAK ADA'",
                    "",
                    "Kalau JSON tidak memuat \"poin\", field Poin int akan bernilai",
                    "0, persis sama dengan JSON yang memuat \"poin\": 0. Ini masalah",
                    "yang sama dengan membaca kunci map yang tidak ada di materi",
                    "Map, dan jawabannya juga mirip:",
                    "",
                    "  Poin *int      nil berarti field-nya tidak ada di JSON,",
                    "                 atau ada tapi bernilai null; pointer ke 0",
                    "                 berarti ada dan nilainya memang nol",
                    "  map[string]any nilai, ada := m[\"poin\"]   pola comma ok",
                    "",
                    "Pakai pointer field HANYA kalau perbedaannya memang penting,",
                    "misalnya PATCH yang cuma mengubah field yang dikirim. Setiap",
                    "pointer menambah satu pemeriksaan nil di semua kode pemakainya.",
                    "",
                    "SEMUA ANGKA JSON MENJADI float64",
                    "",
                    "Saat Unmarshal ke map[string]any atau any, Go tidak tahu kamu",
                    "maunya int atau pecahan. JSON sendiri cuma punya satu tipe",
                    "'number'. Jadi semuanya dijadikan float64:",
                    "",
                    "  bebas[\"umur\"].(int)      ok bernilai false; tanpa ok: PANIC",
                    "  bebas[\"umur\"].(float64)  benar, lalu int(umur) kalau perlu",
                    "",
                    "Akibat lanjutannya: ID di atas 2^53 kehilangan ketelitian kalau",
                    "lewat float64. Untuk itu pakai struct dengan field int64, atau",
                    "json.Number.",
                    "",
                    "Kesimpulannya: pakai map[string]any hanya kalau bentuk datanya",
                    "memang tidak diketahui. Kalau bentuknya sudah pasti, struct",
                    "selalu lebih baik: tipenya jelas, salah ketik nama field",
                    "ketahuan saat kompilasi, dan tidak ada type assertion.",
                    "",
                    "DECODER DAN ENCODER: JSON YANG MENGALIR",
                    "",
                    "  json.NewDecoder(r).Decode(&v)   r = io.Reader apa pun",
                    "  json.NewEncoder(w).Encode(v)    w = io.Writer apa pun",
                    "",
                    "Keduanya tidak peduli sumber dan tujuannya apa. Berkas dari",
                    "materi Berkas, os.Stdin dan os.Stdout, strings.NewReader untuk",
                    "pengujian, dan nanti body permintaan HTTP, semuanya memenuhi",
                    "io.Reader atau io.Writer. Inilah untung nyata dari interface",
                    "kecil satu method.",
                    "",
                    "Bedanya dengan Marshal/Unmarshal:",
                    "  - Marshal menyusun SELURUH hasil di memori dulu. Cocok kalau",
                    "    datanya kecil atau kamu memang butuh []byte-nya.",
                    "  - Decoder membaca sambil jalan, tidak perlu memuat seluruh",
                    "    berkas ke memori. Ini yang dipakai untuk data besar.",
                    "  - Encode SELALU menambahkan satu baris baru di akhir.",
                    "",
                    "JSON LEBIH KETAT DARIPADA YANG KAMU KIRA",
                    "",
                    "  - Koma menggantung TERLARANG: {\"nama\":\"Eka\",} tidak sah.",
                    "    Ini justru kebalikan dari Go, yang MEWAJIBKAN koma di",
                    "    baris terakhir literal struct dan slice bergaya menurun.",
                    "  - Kunci wajib memakai tanda petik ganda; petik satu ditolak.",
                    "  - Tidak ada komentar di dalam JSON.",
                    "",
                    "JANGAN PERNAH ABAIKAN ERROR UNMARSHAL",
                    "",
                    "  json.Unmarshal(data, &b)      <- error dibuang begitu saja",
                    "",
                    "Kalau JSON-nya rusak, b tetap berisi zero value: nama \"\",",
                    "harga 0, slice nil. Tidak ada yang terlihat salah dari luar:",
                    "program lanjut, menyimpan data kosong itu ke database, atau",
                    "melaporkan saldo 0 kepada orang yang saldonya tidak nol. Bug",
                    "seperti ini baru ketahuan berhari-hari kemudian dan sulit",
                    "dilacak, justru karena tidak ada yang crash.",
                    "",
                    "Perlakukan setiap JSON dari luar sebagai data yang tidak bisa",
                    "dipercaya, dan tulis if err != nil seperti di materi Error",
                    "Handling.",
                ],
            },
        ],
    },
    {
        "title": "20. Goroutine & Channel",
        "sections": [
            {
                "body": [
                    "Inilah fitur yang membuat Go terkenal.",
                    "",
                    "GOROUTINE adalah fungsi yang berjalan bersamaan dengan",
                    "fungsi lain. Cukup tambahkan kata 'go' di depan",
                    "pemanggilan fungsi:",
                    "",
                    "  go kerjakanSesuatu()",
                    "",
                    "Goroutine sangat murah. Satu goroutine hanya memakai",
                    "sekitar 2 KB memori awal, sementara satu thread sistem",
                    "butuh 1-8 MB. Program Go biasa menjalankan ribuan",
                    "goroutine tanpa masalah.",
                    "",
                    "MASALAHNYA: main() tidak menunggu goroutine selesai.",
                    "Kalau main berakhir, semua goroutine langsung mati.",
                    "",
                    "Dua cara menunggu dengan benar:",
                    "  1. sync.WaitGroup  - tunggu sekumpulan goroutine",
                    "  2. channel         - komunikasi sekaligus sinkronisasi",
                    "",
                    "Filosofi Go soal concurrency:",
                    "  'Jangan berkomunikasi dengan berbagi memori.",
                    "   Berbagilah memori dengan berkomunikasi.'",
                ]
            },
            {
                "heading": "WaitGroup dan channel",
                "code": """package main

import (
	"fmt"
	"sort"
	"sync"
)

func main() {
	// ---- WaitGroup: tunggu semua goroutine selesai
	var wg sync.WaitGroup
	var mu sync.Mutex
	hasil := []int{}

	for i := 1; i <= 5; i++ {
		wg.Add(1)
		go func(n int) {
			defer wg.Done()
			mu.Lock()
			hasil = append(hasil, n*n)
			mu.Unlock()
		}(i)
	}
	wg.Wait()

	sort.Ints(hasil)
	fmt.Println("Kuadrat:", hasil)

	// ---- Channel: kirim dan terima nilai
	pesan := make(chan string)
	go func() {
		pesan <- "halo dari goroutine"
	}()
	fmt.Println(<-pesan)

	// ---- Channel berpenyangga + range + close
	angka := make(chan int, 5)
	go func() {
		defer close(angka)
		for i := 1; i <= 5; i++ {
			angka <- i * 10
		}
	}()

	total := 0
	for n := range angka {
		total += n
	}
	fmt.Println("Total dari channel:", total)

	// ---- select: tunggu channel mana pun yang siap
	a := make(chan string, 1)
	b := make(chan string, 1)
	a <- "dari A"

	select {
	case m := <-a:
		fmt.Println("Terima", m)
	case m := <-b:
		fmt.Println("Terima", m)
	}
}"""
            },
            {
                "heading": "Membaca kode di atas: WaitGroup dan Mutex",
                "body": [
                    "Dua tipe dari package sync dipakai di contoh tadi tanpa penjelasan.",
                    "Keduanya sama-sama siap pakai begitu dideklarasikan; nilai zero-nya",
                    "sudah benar, jadi tidak ada make() atau new() untuk keduanya:",
                    "  var wg sync.WaitGroup",
                    "  var mu sync.Mutex",
                    "",
                    "sync.WaitGroup sebenarnya cuma sebuah PENCACAH:",
                    "  wg.Add(1)    naikkan pencacah satu",
                    "  wg.Done()    turunkan satu, biasanya lewat defer",
                    "  wg.Wait()    berhenti di sini sampai pencacahnya nol",
                    "",
                    "Dua aturan penempatan yang tidak boleh ditukar:",
                    "  - wg.Add(1) ditulis di goroutine PEMANGGIL, sebelum kata go.",
                    "    Kalau ditaruh di dalam goroutine-nya, wg.Wait() bisa lolos",
                    "    sebelum goroutine itu sempat dihitung, dan program selesai",
                    "    sebelum kerjanya jadi.",
                    "  - defer wg.Done() di baris PERTAMA badan goroutine, supaya",
                    "    pencacahnya tetap turun walau keluar lewat return atau panic.",
                    "    Satu Done yang tidak pernah jalan berarti Wait() menunggu",
                    "    selamanya.",
                    "",
                    "Satu jebakan lagi: WaitGroup tidak boleh DISALIN. Kalau dioper ke",
                    "fungsi lain, oper sebagai pointer (*sync.WaitGroup). Menyalinnya",
                    "membuat Done() menurunkan pencacah SALINAN, sementara Wait() di",
                    "pemanggil menunggu pencacah aslinya - jadi menunggu selamanya.",
                    "Compiler diam soal ini, tapi go vet menangkapnya:",
                    "  kerja passes lock by value: sync.WaitGroup contains sync.noCopy",
                    "Bentuk yang benar kamu lihat di worker pool materi berikutnya.",
                    "",
                    "sync.Mutex adalah kunci pintu, dipegang satu goroutine pada satu",
                    "waktu:",
                    "  mu.Lock()          ambil kunci, tunggu kalau sedang dipegang",
                    "  mu.Unlock()        kembalikan kunci",
                    "  defer mu.Unlock()  bentuk paling aman kalau kuncinya sefungsi penuh",
                    "",
                    "Yang paling penting sekaligus paling sering salah dipahami: mutex",
                    "menjaga DATA tertentu, bukan blok kode. Di contoh tadi mu menjaga",
                    "slice hasil. Artinya SETIAP akses ke hasil - membaca sekalipun -",
                    "harus lewat kunci yang sama. Satu tempat yang lupa mengunci membuat",
                    "semua Lock di tempat lain tidak ada gunanya.",
                    "",
                    "select yang muncul di baris terakhir contoh dibahas tuntas di materi",
                    "berikutnya, Pola Goroutine.",
                ]
            },
            {
                "body": [
                    "CHANNEL - pipa untuk mengirim data antar goroutine",
                    "",
                    "  ch := make(chan int)       tanpa penyangga",
                    "  ch := make(chan int, 5)    penyangga 5 slot",
                    "",
                    "  ch <- 10       KIRIM nilai ke channel",
                    "  n := <-ch      TERIMA nilai dari channel",
                    "  close(ch)      tutup channel",
                    "",
                    "Channel tanpa penyangga bersifat SINKRON:",
                    "  pengirim menunggu sampai ada penerima, dan sebaliknya.",
                    "Channel berpenyangga tidak memblokir sampai penuh.",
                    "",
                    "Menerima dari channel tertutup:",
                    "  n, ok := <-ch",
                    "  ok bernilai false kalau channel sudah ditutup dan kosong.",
                    "",
                    "Aturan close:",
                    "  - Hanya PENGIRIM yang boleh menutup channel.",
                    "  - Mengirim ke channel tertutup menyebabkan panic.",
                    "  - Menutup channel dua kali menyebabkan panic.",
                    "  - Tidak wajib menutup channel; lakukan hanya kalau",
                    "    penerima perlu tahu datanya sudah habis.",
                    "",
                    "DEADLOCK",
                    "Kalau semua goroutine saling menunggu, Go mendeteksinya",
                    "dan menghentikan program dengan pesan:",
                    "  fatal error: all goroutines are asleep - deadlock!",
                    "",
                    "Penyebab paling umum:",
                    "  ch := make(chan int)",
                    "  ch <- 1        deadlock, tidak ada yang menerima",
                    "",
                    "RACE CONDITION",
                    "Kalau beberapa goroutine mengubah data yang sama tanpa",
                    "penjagaan, hasilnya tidak bisa ditebak. Solusinya:",
                    "  - sync.Mutex untuk mengunci akses",
                    "  - atau kirim data lewat channel, jangan dibagi",
                    "",
                    "Deteksi otomatis dengan:  go run -race program.go",
                ]
            },
        ],
    },
    {
        "title": "21. Pola Goroutine: Channel Berarah, select & Worker Pool",
        "sections": [
            {
                "body": [
                    "Materi Goroutine & Channel sudah memperkenalkan go, channel, WaitGroup,",
                    "Mutex, dan close. Tapi di blok kodenya ada dua hal yang DIPAKAI tanpa",
                    "pernah dijelaskan sebaris pun: kata select, dan tanda '}(i)' di ujung",
                    "goroutine. Materi ini menutup keduanya, lalu memasang pola yang benar-",
                    "benar kamu temui saat membaca kode Go orang lain.",
                    "",
                    "CHANNEL BERARAH",
                    "",
                    "Selama ini channel selalu ditulis 'chan int': boleh dikirimi, boleh",
                    "diterima. Arahnya bisa dipersempit, dan arah itu bagian dari TIPE-nya,",
                    "bukan operator yang tercecer di suatu tempat:",
                    "",
                    "  chan Tugas      dua arah: boleh kirim, boleh terima",
                    "  <-chan Tugas    HANYA boleh diterima (dibaca)",
                    "  chan<- Hasil    HANYA boleh dikirimi (ditulis)",
                    "",
                    "Cara membacanya: panah selalu menempel pada kata 'chan'.",
                    "  <-chan   panah KELUAR dari channel -> data keluar, kamu menerima",
                    "  chan<-   panah MASUK ke channel    -> data masuk, kamu mengirim",
                    "",
                    "Kenapa repot-repot? Karena arahnya jadi dokumentasi yang dipaksakan",
                    "compiler. Lihat tanda tangan ini:",
                    "",
                    "  func pekerja(id int, tugas <-chan Tugas, hasil chan<- Hasil)",
                    "",
                    "Tanpa membaca satu baris pun isinya, kamu sudah tahu pekerja",
                    "MENGONSUMSI tugas dan MEMPRODUKSI hasil, dan tidak mungkin terbalik.",
                    "Kalau di dalamnya kamu keliru menulis 'tugas <- t', programnya tidak",
                    "salah diam-diam saat jalan - ia gagal dikompilasi:",
                    "",
                    "  invalid operation: cannot send to receive-only channel tugas",
                    "",
                    "close ikut terjaga: close(tugas) pada channel receive-only juga",
                    "ditolak compiler. Ini persis aturan 'yang menutup channel hanyalah",
                    "pihak pengirim' dari materi sebelumnya, cuma sekarang dijamin mesin,",
                    "bukan cuma diingat-ingat sendiri.",
                    "",
                    "Penyempitan arahnya OTOMATIS dan cuma SATU JALUR:",
                    "  chan T    ->  <-chan T  atau  chan<- T     boleh, tanpa konversi",
                    "  <-chan T  ->  chan T                       TIDAK boleh",
                    "Jadi polanya selalu sama: buat channelnya dua arah sekali di make(),",
                    "lalu persempit saat menyerahkannya ke fungsi.",
                ],
            },
            {
                "heading": "Worker pool: tiga pekerja, satu antrean",
                "body": [
                    "Ini pola concurrency yang paling sering ditemui di kode sungguhan.",
                    "Susunannya baku: satu channel TUGAS, N goroutine pekerja yang membaca",
                    "channel itu, satu channel HASIL, dan WaitGroup untuk tahu kapan semua",
                    "pekerja pulang.",
                    "",
                    "Jumlah pekerja tidak perlu sama dengan jumlah tugas - justru itu",
                    "gunanya. Enam ribu tugas boleh dikerjakan tiga pekerja; yang menganggur",
                    "mengambil tugas berikutnya sendiri, tanpa ada yang mengaturnya.",
                    "",
                    "Yang paling sering salah adalah SIAPA MENUTUP APA:",
                    "  - channel tugas ditutup oleh yang mengirim tugas, setelah tugas habis.",
                    "    Itulah yang membuat 'for t := range tugas' di tiap pekerja berhenti",
                    "    sendiri. Tanpa close, ketiganya menunggu selamanya.",
                    "  - channel hasil ditutup setelah SEMUA pekerja selesai, dan itu harus",
                    "    dikerjakan goroutine tersendiri. Kalau wg.Wait() dipanggil di main",
                    "    sebelum 'for h := range hasil', pekerja terjebak menunggu hasilnya",
                    "    diambil sementara main menunggu pekerja selesai: deadlock.",
                    "",
                    "Perhatikan juga wg dioper sebagai POINTER (*sync.WaitGroup). WaitGroup",
                    "tidak boleh disalin - salinannya punya penghitung sendiri, dan Wait()",
                    "yang asli tidak akan pernah selesai. go vet menangkapnya:",
                    "  call of pekerja copies lock value: sync.WaitGroup contains sync.noCopy",
                ],
                "code": """package main

import (
	"fmt"
	"sort"
	"strings"
	"sync"
)

type Tugas struct {
	ID   int
	Kata string
}

type Hasil struct {
	ID    int
	Nilai string
}

// tugas HANYA boleh dibaca, hasil HANYA boleh ditulis. Arahnya bagian
// dari TIPE parameter, dan compiler yang menjaga janjinya.
// wg dioper sebagai POINTER: WaitGroup tidak boleh disalin.
func pekerja(id int, tugas <-chan Tugas, hasil chan<- Hasil, wg *sync.WaitGroup) {
	defer wg.Done()
	for t := range tugas { // berhenti sendiri saat channel tugas ditutup
		hasil <- Hasil{ID: t.ID, Nilai: strings.ToUpper(t.Kata)}
	}
}

func main() {
	kata := []string{"gado", "sate", "rendang", "bakso", "soto", "pempek"}

	tugas := make(chan Tugas) // dua arah di sini,
	hasil := make(chan Hasil) // dipersempit saat diserahkan ke pekerja

	// Tiga pekerja untuk enam tugas. Jumlahnya memang tidak perlu sama.
	var wg sync.WaitGroup
	for i := 1; i <= 3; i++ {
		wg.Add(1)
		go pekerja(i, tugas, hasil, &wg)
	}

	// Yang mengirim tugas, dia juga yang menutup channel tugas.
	go func() {
		for i, k := range kata {
			tugas <- Tugas{ID: i + 1, Kata: k}
		}
		close(tugas)
	}()

	// Penutup hasil: tunggu SEMUA pekerja pulang dulu, baru tutup.
	go func() {
		wg.Wait()
		close(hasil)
	}()

	kumpul := []string{}
	for h := range hasil { // selesai sendiri saat hasil ditutup
		kumpul = append(kumpul, fmt.Sprintf("%d %s", h.ID, h.Nilai))
	}

	sort.Strings(kumpul) // urutan datangnya tidak dijamin
	for _, baris := range kumpul {
		fmt.Println(baris)
	}
	fmt.Println("total hasil:", len(kumpul))
}""",
            },
            {
                "body": [
                    "SELECT - ATURAN MAINNYA",
                    "",
                    "Bentuknya mirip switch, tapi tiap case-nya wajib berupa operasi channel:",
                    "pengiriman atau penerimaan. Aturannya cuma lima, dan semuanya penting:",
                    "",
                    "  1. Semua case dilihat sekaligus. select MEMBLOKIR sampai ada satu",
                    "     case yang siap, lalu menjalankan case itu SAJA, sekali.",
                    "",
                    "  2. Kalau BEBERAPA case siap bersamaan, yang dijalankan dipilih ACAK -",
                    "     bukan yang paling atas. Ini disengaja, supaya satu channel yang",
                    "     selalu ramai tidak membuat channel lain kelaparan selamanya.",
                    "     Jangan pernah menyandarkan urutan pada posisi case-nya.",
                    "",
                    "  3. Kalau ada klausa default, select TIDAK memblokir sama sekali:",
                    "     begitu tidak ada satu pun case yang siap, default langsung jalan.",
                    "     Inilah cara mengintip channel tanpa ikut menunggu.",
                    "",
                    "  4. select{} tanpa satu case pun memblokir SELAMANYA. Kadang dipakai",
                    "     di ujung main() server supaya program tidak keburu keluar.",
                    "",
                    "  5. Channel bernilai nil tidak pernah siap. Menyetel sebuah variabel",
                    "     channel jadi nil praktis MEMATIKAN case yang memakainya - trik",
                    "     yang akan kamu lihat di loop select yang sumbernya habis satu per",
                    "     satu.",
                    "",
                    "TIMEOUT",
                    "  case <-time.After(2 * time.Second):",
                    "time.After mengembalikan channel yang menerima satu nilai setelah",
                    "durasinya lewat. Digabung ke select, artinya: tunggu, tapi menyerah",
                    "kalau kelamaan. Jebakannya, kalau ditaruh di dalam loop yang berputar",
                    "ribuan kali, setiap putaran membuat timer BARU. Untuk penungguan",
                    "berulang pakai time.NewTimer beserta Reset, atau ticker.",
                    "",
                    "DETAK BERKALA",
                    "  tick := time.NewTicker(20 * time.Millisecond)",
                    "  defer tick.Stop()",
                    "Ticker mengirim waktu ke tick.C berulang-ulang selama program hidup.",
                    "Lupa Stop() berarti ia terus berdetak walau tidak ada yang mendengar.",
                    "",
                    "CHANNEL SINYAL",
                    "  selesai := make(chan struct{})",
                    "  close(selesai)",
                    "struct{} adalah struct kosong: NOL byte, tidak menyimpan apa-apa. Itu",
                    "memang maksudnya - yang dikirim bukan datanya, melainkan KEJADIANNYA.",
                    "make(chan bool) juga jalan, tapi pembacanya jadi bertanya-tanya apakah",
                    "true dan false-nya berarti sesuatu. Dengan struct{} tidak ada yang bisa",
                    "disalahpahami.",
                    "",
                    "Kenapa close(selesai), bukan 'selesai <- struct{}{}'?",
                    "  - Satu kiriman membangunkan TEPAT SATU penerima. Kalau ada lima",
                    "    goroutine menunggu, empat sisanya tetap menggantung.",
                    "  - close membangunkan SEMUA penerima sekaligus, dan seterusnya:",
                    "    menerima dari channel tertutup langsung mengembalikan nilai nol",
                    "    tanpa memblokir, berapa kali pun dibaca.",
                    "Itu sebabnya semua pola 'berhenti sekarang' memakai close, bukan kirim.",
                    "",
                    "KEBOCORAN GOROUTINE",
                    "Goroutine yang menunggu channel yang tidak pernah diisi tidak pernah",
                    "mati. Programnya tidak crash - ia cuma pelan-pelan menggemuk, dan",
                    "server yang hidup berhari-hari akhirnya kehabisan memori. Deteksi",
                    "deadlock Go tidak menolong di sini: ia cuma berbunyi kalau SELURUH",
                    "goroutine tidur. Cara menyuruh goroutine berhenti dengan rapi dibahas",
                    "di materi context berikutnya.",
                ],
            },
            {
                "heading": "select: sinyal, detak, timeout, dan default",
                "code": """package main

import (
	"fmt"
	"time"
)

func main() {
	angka := make(chan int)
	selesai := make(chan struct{}) // channel sinyal: nol byte, tanpa data

	go func() {
		for i := 1; i <= 3; i++ {
			angka <- i * 5
		}
		close(selesai) // menutup = membangunkan SEMUA penerima sekaligus
	}()

	for berjalan := true; berjalan; {
		select {
		case n := <-angka:
			fmt.Println("dapat angka", n)
		case <-selesai:
			fmt.Println("pengirim bilang selesai")
			berjalan = false
		case <-time.After(2 * time.Second):
			fmt.Println("timeout: tidak ada kabar selama 2 detik")
			berjalan = false
		}
	}

	// Detak berkala. Ticker WAJIB dihentikan, kalau tidak ia terus jalan.
	tick := time.NewTicker(20 * time.Millisecond)
	defer tick.Stop()
	for i := 1; i <= 3; i++ {
		<-tick.C
		fmt.Println("detak nomor", i)
	}

	// Timeout sungguhan: tidak ada yang pernah mengisi channel ini.
	lambat := make(chan string)
	select {
	case s := <-lambat:
		fmt.Println("jawaban:", s)
	case <-time.After(100 * time.Millisecond):
		fmt.Println("menyerah setelah 100ms")
	}

	// default membuat select TIDAK memblokir sama sekali.
	select {
	case s := <-lambat:
		fmt.Println("jawaban:", s)
	default:
		fmt.Println("belum ada apa-apa, lanjut kerja lain")
	}
}""",
            },
            {
                "heading": "Jebakan variabel loop, RWMutex, Once & atomic",
                "body": [
                    "JEBAKAN VARIABEL LOOP",
                    "",
                    "Materi sebelumnya menulis goroutine-nya begini, tanpa menjelaskan",
                    "kenapa: 'go func(n int) { ... }(i)'. Kenapa i dioper sebagai argumen,",
                    "kok tidak dipakai langsung saja dari dalam?",
                    "",
                    "Sebelum Go 1.22, 'for i := 1; i <= 5; i++' membuat SATU variabel i yang",
                    "dipakai ulang untuk semua putaran. Closure di dalam goroutine menangkap",
                    "VARIABELNYA, bukan nilainya saat itu. Goroutine baru benar-benar jalan",
                    "beberapa saat kemudian - dan waktu ia akhirnya membaca i, loop-nya sudah",
                    "selesai. Hasil klasiknya: lima goroutine mencetak angka yang sama,",
                    "biasanya 6, karena itulah nilai i saat loop berhenti.",
                    "",
                    "Dua penangkalnya, dan dua-duanya masih bertebaran di kode lama:",
                    "",
                    "  go func(n int) { pakai(n) }(i)   oper sebagai argumen; salinannya",
                    "                                   dibuat saat itu juga, saat dipanggil",
                    "  i := i                           bikin variabel baru tiap putaran,",
                    "                                   sengaja dinamai sama",
                    "",
                    "Sejak Go 1.22 variabelnya memang baru tiap putaran, jadi keduanya tidak",
                    "diperlukan lagi. Satu hal yang perlu kamu tahu: yang menentukan aturan",
                    "mana yang berlaku adalah baris 'go 1.xx' di go.mod, BUKAN versi",
                    "toolchain yang terpasang. Modul yang masih menulis 'go 1.21' tetap",
                    "memakai aturan lama walaupun dikompilasi Go 1.23.",
                    "",
                    "Jadi 'i := i' bukan kode aneh dan bukan salah ketik - itu kode yang",
                    "ditulis sebelum 1.22, dan kamu akan sering melihatnya. Perangkap yang",
                    "sama dulu berlaku untuk 'for _, v := range daftar'.",
                    "",
                    "SELAIN Mutex",
                    "",
                    "  sync.RWMutex   Lock/Unlock untuk MENULIS (sendirian), RLock/RUnlock",
                    "                 untuk MEMBACA (banyak goroutine boleh bersamaan). Pas",
                    "                 untuk data yang jauh lebih sering dibaca daripada",
                    "                 ditulis, misalnya cache. Jangan pernah mengubah data",
                    "                 sambil cuma memegang RLock.",
                    "",
                    "  sync.Once      once.Do(f) menjalankan f TEPAT sekali walau dipanggil",
                    "                 dari banyak goroutine sekaligus; pemanggil lain",
                    "                 menunggu sampai f rampung. Untuk inisialisasi mahal",
                    "                 yang cuma perlu sekali seumur program.",
                    "",
                    "  sync/atomic    atomic.Int64 dengan Add/Load/Store untuk pencacah.",
                    "                 Lebih ringan daripada mutex, tapi hanya untuk operasi",
                    "                 pada SATU nilai. Begitu dua variabel harus berubah",
                    "                 bersamaan supaya tetap cocok, kembalilah ke mutex.",
                    "",
                    "MEMBUKTIKAN ADA TIDAKNYA RACE",
                    "  go run -race program.go",
                    "  go test -race ./...",
                    "Race detector mengawasi akses memori sungguhan selagi program jalan,",
                    "lalu melapor kalau dua goroutine menyentuh alamat yang sama tanpa",
                    "penjagaan. Ia jauh lebih lambat dan lebih rakus memori, jadi dipakai",
                    "saat menguji, bukan di produksi. Ia juga hanya melihat kode yang",
                    "benar-benar DIJALANKAN - race di jalur yang tidak pernah diuji tetap",
                    "lolos. Ketiga program di materi ini bersih di bawah -race.",
                ],
                "code": """package main

import (
	"fmt"
	"sort"
	"sync"
	"sync/atomic"
)

// RWMutex: banyak pembaca boleh bersamaan, penulis mengunci sendirian.
type Cache struct {
	mu  sync.RWMutex
	isi map[string]int
}

func (c *Cache) Tulis(k string, v int) {
	c.mu.Lock()
	defer c.mu.Unlock()
	c.isi[k] = v
}

func (c *Cache) Baca(k string) int {
	c.mu.RLock()
	defer c.mu.RUnlock()
	return c.isi[k]
}

func (c *Cache) Kunci() []string {
	c.mu.RLock()
	defer c.mu.RUnlock()
	daftar := make([]string, 0, len(c.isi))
	for k := range c.isi {
		daftar = append(daftar, k)
	}
	sort.Strings(daftar)
	return daftar
}

var (
	sekali  sync.Once
	setelan string
)

func muatSetelan() string {
	sekali.Do(func() {
		fmt.Println("memuat setelan (baris ini cuma muncul sekali)")
		setelan = "mode=produksi"
	})
	return setelan
}

func main() {
	c := &Cache{isi: map[string]int{}}
	var cacah atomic.Int64
	var wg sync.WaitGroup

	for i := 1; i <= 4; i++ {
		i := i // idiom lama; sejak Go 1.22 sudah tidak diperlukan lagi
		wg.Add(1)
		go func() {
			defer wg.Done()
			muatSetelan()
			c.Tulis(fmt.Sprintf("kunci%d", i), i*i)
			cacah.Add(1) // pencacah tanpa mutex
		}()
	}
	wg.Wait()

	for _, k := range c.Kunci() {
		fmt.Println(k, "=", c.Baca(k))
	}
	fmt.Println("goroutine yang selesai:", cacah.Load())
	fmt.Println("setelan:", muatSetelan())
}""",
            },
        ],
    },
    {
        "title": "22. context: Membatalkan & Membatasi Waktu",
        "sections": [
            {
                "body": [
                    "Materi Goroutine & Channel mengajarkan cara MENUNGGU goroutine",
                    "sampai selesai.",
                    "Materi ini mengajarkan cara MENYURUHNYA BERHENTI.",
                    "",
                    "Bedanya besar. sync.WaitGroup bertanya 'sudah selesai belum?'",
                    "context bilang 'sudah, jangan diteruskan, pulang saja'.",
                    "",
                    "Kenapa itu perlu? Bayangkan satu permintaan HTTP masuk. Untuk",
                    "melayaninya program menembak tiga query database dan dua",
                    "panggilan ke layanan lain. Lalu pemakainya menutup tab-nya.",
                    "Tanpa context, kelima pekerjaan itu jalan terus sampai habis:",
                    "koneksi database terpakai untuk hasil yang tidak akan dibaca",
                    "siapa pun, dan goroutine-nya menumpuk. Server sibuk mati",
                    "pelan-pelan karena hal seperti ini, bukan karena salah hitung.",
                    "",
                    "context.Context adalah SATU nilai yang dibawa turun ke setiap",
                    "fungsi, isinya sinyal 'berhenti'. Kamu akan melihatnya sebagai",
                    "parameter pertama hampir di semua kode Go sungguhan:",
                    "",
                    "  func AmbilUser(ctx context.Context, id int) (*User, error)",
                    "",
                    "Membuat AKARNYA - hanya di satu tempat, paling atas:",
                    "  context.Background()  akar sungguhan, dibuat di main() atau",
                    "                        di titik masuk sebuah permintaan",
                    "  context.TODO()        penanda 'belum diputuskan mau pakai",
                    "                        context yang mana'. Perilakunya sama",
                    "                        persis; bedanya cuma niat, supaya",
                    "                        gampang dicari lagi nanti",
                    "",
                    "Dari akar itu diturunkan context ANAK:",
                    "  ctx, cancel := context.WithCancel(induk)",
                    "  ctx, cancel := context.WithTimeout(induk, 2*time.Second)",
                    "  ctx, cancel := context.WithDeadline(induk, jamTertentu)",
                    "",
                    "WithTimeout menghitung dari sekarang ('paling lama 2 detik'),",
                    "WithDeadline menyebut titik waktunya ('paling lambat jam 10').",
                    "",
                    "Ketiganya mengembalikan DUA nilai, dan yang kedua WAJIB",
                    "dipanggil - biasanya langsung didaftarkan: defer cancel().",
                    "Lupa memanggilnya membuat context anak menggantung pada",
                    "induknya sampai induknya sendiri mati; itu kebocoran memori.",
                    "go vet menangkapnya dan berkata:",
                    "  the cancel function returned by context.WithTimeout should",
                    "  be called, not discarded, to avoid a context leak",
                    "Memanggil cancel dua kali AMAN dan tidak melakukan apa-apa,",
                    "jadi tidak ada alasan untuk ragu men-defer-nya.",
                    "",
                    "Turunan itu membentuk POHON. Membatalkan satu context otomatis",
                    "membatalkan seluruh keturunannya, sedalam apa pun - itulah yang",
                    "membuat satu permintaan yang dibatalkan bisa mematikan semua",
                    "pekerjaan yang lahir darinya sekaligus, tanpa kamu mendaftar",
                    "satu per satu siapa saja yang harus diberi tahu.",
                ],
            },
            {
                "heading": "Membatalkan, kehabisan waktu, dan pohon context",
                "code": """package main

import (
	"context"
	"errors"
	"fmt"
	"time"
)

// hitung mengirim angka terus-menerus sampai ctx dibatalkan.
// Perhatikan: ctx adalah parameter PERTAMA.
func hitung(ctx context.Context, keluar chan<- int) {
	for i := 1; ; i++ {
		select {
		case <-ctx.Done(): // channel ini TERTUTUP saat dibatalkan
			fmt.Println("  hitung berhenti karena:", ctx.Err())
			return
		case keluar <- i:
		}
	}
}

func main() {
	// ---- 1. WithCancel: kita yang memutuskan kapan berhenti
	ctx, cancel := context.WithCancel(context.Background())
	keluar := make(chan int)
	selesai := make(chan struct{})

	go func() {
		defer close(selesai)
		hitung(ctx, keluar)
	}()

	for i := 0; i < 3; i++ {
		fmt.Println("  dapat", <-keluar)
	}
	cancel()  // suruh berhenti
	<-selesai // tunggu goroutine-nya benar-benar keluar

	// ---- 2. WithTimeout: yang memutuskan adalah jam, bukan kita
	ctxT, cancelT := context.WithTimeout(context.Background(), 30*time.Millisecond)
	defer cancelT()

	hasil := make(chan string, 1)
	go func() {
		time.Sleep(200 * time.Millisecond) // pekerjaan yang kelamaan
		hasil <- "data lengkap"
	}()

	select {
	case h := <-hasil:
		fmt.Println("Hasil:", h)
	case <-ctxT.Done():
		fmt.Println("Menyerah:", ctxT.Err())
		fmt.Println("Kehabisan waktu?", errors.Is(ctxT.Err(), context.DeadlineExceeded))
	}

	// ---- 3. Context itu POHON: induk dibatalkan, anak ikut mati
	induk, batalInduk := context.WithCancel(context.Background())
	anak, batalAnak := context.WithCancel(induk)
	defer batalAnak()

	batalInduk()
	<-anak.Done() // ikut tertutup tanpa kita sentuh sama sekali
	fmt.Println("Anak ikut batal:", anak.Err())
	fmt.Println("Dibatalkan manual?", errors.Is(anak.Err(), context.Canceled))
}""",
            },
            {
                "body": [
                    "Isi sebuah Context cuma empat method, dan yang sering dipakai",
                    "sehari-hari cuma dua:",
                    "",
                    "  ctx.Done()      channel yang TERTUTUP begitu context batal.",
                    "                  Tidak pernah ada nilai yang dikirim ke sana;",
                    "                  penutupannya sendiri yang jadi sinyal. Itu",
                    "                  sebabnya <-ctx.Done() membebaskan SEMUA yang",
                    "                  sedang menunggunya sekaligus.",
                    "  ctx.Err()       nil selama masih hidup. Setelah mati ia",
                    "                  berisi ALASANNYA:",
                    "                    context.Canceled          cancel() dipanggil",
                    "                    context.DeadlineExceeded  waktunya habis",
                    "  ctx.Deadline()  kapan batas waktunya, kalau memang ada",
                    "  ctx.Value(k)    ambil nilai titipan (lihat bagian terakhir)",
                    "",
                    "Periksa alasannya dengan errors.Is, jangan dengan ==, karena",
                    "error itu biasanya sudah dibungkus %w dalam perjalanan pulang",
                    "(lihat materi Error Handling):",
                    "  if errors.Is(err, context.DeadlineExceeded) { ... }",
                    "",
                    "BENTUK BAKU di dalam loop atau worker - hafalkan yang ini,",
                    "kamu akan menulisnya berulang kali:",
                    "",
                    "  for {",
                    "      select {",
                    "      case <-ctx.Done():",
                    "          return ctx.Err()",
                    "      case tugas, ok := <-antrean:",
                    "          if !ok {",
                    "              return nil",
                    "          }",
                    "          kerjakan(tugas)",
                    "      }",
                    "  }",
                    "",
                    "JEBAKAN",
                    "",
                    "1. context tidak MEMBUNUH apa pun. Ia cuma menutup sebuah",
                    "   channel. Kalau kodemu tidak pernah memeriksa ctx.Done(),",
                    "   pekerjaannya jalan terus sampai habis seolah tidak terjadi",
                    "   apa-apa. Perulangan berat, time.Sleep, dan pembacaan berkas",
                    "   biasa tidak berhenti sendiri gara-gara timeout.",
                    "",
                    "2. Setelah cancel(), goroutine-nya belum tentu SUDAH berhenti.",
                    "   Kamu baru mengirim sinyal. Contoh di atas menunggunya betul",
                    "   lewat channel 'selesai'; tanpa itu main bisa keburu keluar",
                    "   dan kamu tidak akan pernah melihat pesan penutupnya.",
                    "",
                    "3. Kalau ctx.Done() dan channel data SAMA-SAMA siap, select",
                    "   memilih ACAK - satu data bisa terlanjur diproses walau",
                    "   context sudah batal. Kalau itu tidak boleh terjadi, periksa",
                    "   ulang ctx.Err() != nil di awal case-nya.",
                    "",
                    "4. Batas waktu itu WARISAN dan tidak bisa dilonggarkan. Anak",
                    "   dari induk bersisa 1 detik tidak bisa minta 5 detik; ia",
                    "   tetap mati saat induknya mati. Deadline anak hanya bisa",
                    "   lebih pendek, tidak pernah lebih panjang.",
                ],
            },
            {
                "heading": "ctx di kode nyata: parameter pertama & WithValue",
                "code": """package main

import (
	"context"
	"errors"
	"fmt"
	"time"
)

// Tipe kunci sendiri supaya tidak bentrok dengan paket lain.
type kunciCtx string

const kunciPermintaan kunciCtx = "permintaan-id"

func catat(ctx context.Context, pesan string) {
	id, ok := ctx.Value(kunciPermintaan).(string)
	if !ok {
		id = "tanpa-id"
	}
	fmt.Printf("[%s] %s\\n", id, pesan)
}

// ctx SELALU parameter pertama, dan namanya selalu ctx.
func ambilData(ctx context.Context, tabel string) (string, error) {
	catat(ctx, "mulai query ke tabel "+tabel)
	select {
	case <-time.After(60 * time.Millisecond): // pura-pura query database
		return tabel + ": 3 baris", nil
	case <-ctx.Done():
		return "", fmt.Errorf("query %s dibatalkan: %w", tabel, ctx.Err())
	}
}

func main() {
	akar := context.WithValue(context.Background(), kunciPermintaan, "req-42")

	// Permintaan pertama: waktunya cukup.
	ctx1, cancel1 := context.WithTimeout(akar, 2*time.Second)
	defer cancel1()
	data, err := ambilData(ctx1, "produk")
	if err != nil {
		catat(ctx1, "gagal: "+err.Error())
	} else {
		catat(ctx1, "sukses -> "+data)
	}

	// Permintaan kedua: batas waktunya sengaja terlalu pendek.
	ctx2, cancel2 := context.WithTimeout(akar, 10*time.Millisecond)
	defer cancel2()
	_, err = ambilData(ctx2, "pesanan")
	catat(ctx2, "hasilnya: "+err.Error())
	fmt.Println("Kehabisan waktu?", errors.Is(err, context.DeadlineExceeded))
}""",
            },
            {
                "body": [
                    "context.WithValue menitipkan data yang ikut sepanjang SATU",
                    "permintaan: request ID untuk log, identitas pemakai yang sudah",
                    "login, penanda bahasa. Itu saja.",
                    "",
                    "Ia BUKAN tempat menaruh parameter fungsi biasa. Kalau sebuah",
                    "fungsi butuh id barang untuk bekerja, tulis id sebagai",
                    "parameter. Menyembunyikannya di dalam ctx membuat compiler",
                    "tidak bisa lagi memberitahu kalau kamu lupa mengisinya, dan",
                    "kesalahannya baru ketahuan saat program sudah jalan.",
                    "",
                    "Dua aturan WithValue yang gampang dilanggar:",
                    "  - Kuncinya JANGAN string telanjang. Pakai tipe sendiri",
                    "    (type kunciCtx string) supaya paket lain yang kebetulan",
                    "    juga memakai kunci \"user\" tidak menimpa punyamu diam-diam.",
                    "  - Value() mengembalikan any, jadi selalu pakai type assertion",
                    "    dua nilai: v, ok := ctx.Value(k).(string). Bentuk satu",
                    "    nilai akan panic begitu titipannya ternyata tidak ada.",
                    "",
                    "KONVENSI yang membuat kode Go di mana-mana terlihat seragam:",
                    "  - ctx adalah parameter PERTAMA, selalu, bahkan sebelum",
                    "    parameter yang terasa lebih penting.",
                    "  - Namanya selalu ctx. Bukan c, bukan konteks, bukan cx.",
                    "  - Jangan mengoper nil sebagai context; pakai context.TODO()",
                    "    kalau memang belum punya.",
                    "  - JANGAN menyimpan Context di field struct. Context milik",
                    "    satu panggilan, sedangkan struct dipakai berulang-ulang -",
                    "    hasilnya ctx basi yang sudah lama batal, atau malah ctx",
                    "    yang tidak pernah batal padahal seharusnya. Oper lewat",
                    "    parameter, bukan lewat field.",
                    "",
                    "DI MANA KAMU AKAN BERTEMU INI:",
                    "  r.Context()                   ctx milik satu permintaan HTTP;",
                    "                                otomatis batal saat pemakai",
                    "                                memutus koneksinya",
                    "  http.NewRequestWithContext()  panggilan HTTP keluar yang bisa",
                    "                                dibatalkan dan dibatasi waktu",
                    "  db.QueryContext(ctx, ...)     query yang benar-benar berhenti",
                    "  exec.CommandContext(ctx, ...) proses luar yang ikut dimatikan",
                    "",
                    "Hampir setiap library Go pihak ketiga meminta ctx di parameter",
                    "pertamanya. Sekarang kamu tahu benda apa yang harus dikasihkan",
                    "ke situ, dan kenapa hampir selalu ada defer cancel() di",
                    "dekatnya.",
                ],
            },
        ],
    },
    {
        "title": "23. Generics: Type Parameter & Package slices/maps",
        "sections": [
            {
                "body": [
                    "Misalkan kamu butuh fungsi 'ambil yang terbesar' untuk int DAN untuk float64.",
                    "Sampai materi ini, pilihanmu cuma dua, dan dua-duanya buruk:",
                    "",
                    "  1. Tulis dua fungsi kembar: TerbesarInt dan TerbesarFloat. Lalu tiga, lalu",
                    "     empat, dan tiap perbaikan bug harus disalin ke semuanya.",
                    "  2. Pakai any (interface{}) lalu type assertion di dalamnya. Compiler jadi",
                    "     buta: salah tipe baru ketahuan saat program JALAN, berupa panic.",
                    "",
                    "Sejak Go 1.18 ada pilihan ketiga: GENERICS. Fungsinya ditulis sekali, tipenya",
                    "jadi parameter, dan compiler tetap memeriksa semuanya seperti biasa.",
                    "",
                    "  func Terbesar[T int | float64](a, b T) T {",
                    "      if a > b {",
                    "          return a",
                    "      }",
                    "      return b",
                    "  }",
                    "",
                    "MEMBACA KURUNG SIKUNYA",
                    "Ini bagian yang paling sering salah dibaca, karena kurung siku sudah dipakai",
                    "untuk hal lain sejak Materi 7. Bedakan dari POSISINYA:",
                    "",
                    "  angka[2]         kurung siku sesudah sebuah NILAI     -> indeks slice/array",
                    "  Terbesar[int]    kurung siku sesudah sebuah NAMA      -> parameter tipe",
                    "  []int            kurung siku kosong di DEPAN tipe     -> slice",
                    "  [5]int           ada angkanya, di DEPAN tipe          -> array",
                    "",
                    "Jadi Terbesar[int] bukan 'elemen ke-int dari Terbesar'. Itu Terbesar yang",
                    "T-nya diisi int. Begitu terbiasa, T di [T any] terbaca sama seperti n di",
                    "(n int): sebuah nama kosong yang diisi saat dipanggil. Bedanya, yang diisi",
                    "ke T bukan angka, melainkan sebuah TIPE.",
                    "",
                    "CONSTRAINT: APA SAJA YANG BOLEH MENGISI T",
                    "Yang ditulis sesudah T adalah constraint-nya. Bentuknya interface, tapi di",
                    "sini interface dipakai sebagai DAFTAR TIPE, bukan daftar method:",
                    "",
                    "  [T any]             apa saja. any itu nama lain interface{} (Materi 12).",
                    "  [T comparable]      tipe yang bisa dibandingkan dengan == dan !=. Inilah",
                    "                      syarat supaya T boleh dipakai sebagai KUNCI map.",
                    "  [T int | float64]   salah satu dari daftar itu saja. Pemisahnya tanda |.",
                    "",
                    "Daftar yang panjang biasanya dinamai sendiri supaya bisa dipakai berulang:",
                    "",
                    "  type Angka interface {",
                    "      ~int | ~int64 | ~float64",
                    "  }",
                    "",
                    "Tanda ~ (tilde) itu bukan hiasan. ~int berarti 'int, ATAU tipe bentukan mana",
                    "pun yang tipe dasarnya int'. Tanpa tilde, type Celsius float64 dari materi",
                    "Tipe Bentukan akan DITOLAK padahal isinya persis float64. Hampir semua",
                    "constraint di kode nyata memakai tilde; kalau kamu lupa, yang kena adalah",
                    "orang yang memakai fungsimu, dan pesannya membingungkan:",
                    "  Celsius does not satisfy Angka (possibly missing ~ for float64)",
                    "",
                    "INFERENSI TIPE",
                    "Hampir selalu kamu tidak perlu menyebut T sama sekali:",
                    "",
                    "  Terbesar(2, 3)            T disimpulkan int dari argumennya",
                    "  Terbesar(2.5, 1.5)        T disimpulkan float64",
                    "  Terbesar[float64](2, 7)   ditulis tegas; perlu kalau argumennya ambigu",
                    "",
                    "Itu sebabnya kode yang memakai generics sering tidak kelihatan 'generik'",
                    "saat dipanggil. Kurung sikunya cuma muncul di tempat ia DIDEFINISIKAN.",
                ],
            },
            {
                "heading": "Fungsi generik: constraint, tilde, dan inferensi",
                "code": """package main

import (
	"fmt"
	"sort"
)

// Constraint: gabungan tipe dipisah |. Tanda ~ artinya "termasuk tipe
// bentukan yang dasarnya itu" -- lihat materi Tipe Bentukan.
type Angka interface {
	~int | ~int64 | ~float64
}

type Celsius float64

func Terbesar[T Angka](a, b T) T {
	if a > b {
		return a
	}
	return b
}

func Jumlah[T Angka](data []T) T {
	var total T // zero value milik T, apa pun T-nya
	for _, v := range data {
		total += v
	}
	return total
}

// Dua parameter tipe. K wajib comparable karena dipakai sebagai kunci map.
func Kunci[K comparable, V any](m map[K]V) []K {
	hasil := make([]K, 0, len(m))
	for k := range m {
		hasil = append(hasil, k)
	}
	return hasil
}

func Peta[T, U any](data []T, ubah func(T) U) []U {
	hasil := make([]U, 0, len(data))
	for _, v := range data {
		hasil = append(hasil, ubah(v))
	}
	return hasil
}

func Saring[T any](data []T, cocok func(T) bool) []T {
	hasil := []T{}
	for _, v := range data {
		if cocok(v) {
			hasil = append(hasil, v)
		}
	}
	return hasil
}

func Lipat[T, U any](data []T, awal U, gabung func(U, T) U) U {
	hasil := awal
	for _, v := range data {
		hasil = gabung(hasil, v)
	}
	return hasil
}

func main() {
	fmt.Println(Terbesar(3, 9))          // T disimpulkan int
	fmt.Println(Terbesar(2.5, 1.5))      // T disimpulkan float64
	fmt.Println(Terbesar[float64](2, 7)) // T dipaksa float64

	// Celsius lolos karena constraint-nya ~float64, bukan float64 polos
	fmt.Println(Terbesar(Celsius(31.5), Celsius(28)))

	angka := []int{4, 8, 15, 16, 23, 42}
	fmt.Println("Jumlah   :", Jumlah(angka))
	fmt.Println("Genap    :", Saring(angka, func(n int) bool { return n%2 == 0 }))
	fmt.Println("Kuadrat  :", Peta(angka, func(n int) int { return n * n }))
	fmt.Println("Jadi teks:", Peta(angka, func(n int) string { return fmt.Sprint(n) }))
	fmt.Println("Puncak   :", Lipat(angka, angka[0], Terbesar[int]))

	stok := map[string]int{"beras": 25, "gula": 10, "minyak": 8}
	kunci := Kunci(stok)
	sort.Strings(kunci) // map tidak punya urutan; lihat Materi 8
	fmt.Println("Kunci    :", kunci)
}""",
            },
            {
                "heading": "Tipe generik dan method-nya",
                "body": [
                    "Bukan cuma fungsi yang boleh punya parameter tipe; struct juga. Tiga aturan",
                    "yang bikin orang tersandung di sini:",
                    "",
                    "  - Nama tipenya membawa T selamanya. Yang ada itu Tumpukan[int] dan",
                    "    Tumpukan[string]; 'Tumpukan' sendirian bukan tipe yang sah.",
                    "  - Receiver method-nya WAJIB mengulang [T], dan itu deklarasi nama, bukan",
                    "    pengisian: func (t *Tumpukan[T]) Dorong(v T).",
                    "  - Method TIDAK BOLEH punya parameter tipe sendiri. Kalau butuh tipe kedua",
                    "    yang bebas (misalnya Peta di contoh sebelumnya), jadikan fungsi biasa",
                    "    di luar struct. Ini batasan Go, bukan kelupaanmu.",
                ],
                "code": """package main

import "fmt"

// Parameter tipe ditulis SETELAH nama tipe. Setiap pemakaian Tumpukan
// wajib menyebut T-nya: Tumpukan[int], Tumpukan[string], ...
type Tumpukan[T any] struct {
	isi []T
}

// Receiver mengulang [T]. Itu bukan indeks, itu nama parameter tipenya.
func (t *Tumpukan[T]) Dorong(v T) {
	t.isi = append(t.isi, v)
}

func (t *Tumpukan[T]) Ambil() (T, bool) {
	var kosong T // tidak bisa "return nil": T belum tentu punya nil
	if len(t.isi) == 0 {
		return kosong, false
	}
	akhir := len(t.isi) - 1
	v := t.isi[akhir]
	t.isi = t.isi[:akhir]
	return v, true
}

func (t *Tumpukan[T]) Panjang() int { return len(t.isi) }

type Pasangan[K comparable, V any] struct {
	Kunci K
	Nilai V
}

func main() {
	var angka Tumpukan[int]
	angka.Dorong(1)
	angka.Dorong(2)
	angka.Dorong(3)
	fmt.Println("Isi tumpukan:", angka.Panjang(), "elemen")

	for angka.Panjang() > 0 {
		v, _ := angka.Ambil()
		fmt.Print(v, " ") // keluar terbalik: yang terakhir masuk, duluan keluar
	}
	fmt.Println()

	kata := &Tumpukan[string]{}
	kata.Dorong("halo")
	kata.Dorong("dunia")
	v, ok := kata.Ambil()
	fmt.Println("Diambil:", v, ok)

	var hampa Tumpukan[string]
	s, ada := hampa.Ambil()
	fmt.Printf("Tumpukan kosong -> %q %v\\n", s, ada)

	p := Pasangan[string, int]{Kunci: "beras", Nilai: 25}
	fmt.Printf("%s = %d\\n", p.Kunci, p.Nilai)

	// angka.Dorong("empat") -> ditolak saat KOMPILASI, bukan saat jalan:
	// cannot use "empat" (untyped string constant) as int value
}""",
            },
            {
                "heading": "Package slices dan maps",
                "body": [
                    "Begitu generics ada, fungsi-fungsi yang dulu ditulis ulang di tiap proyek",
                    "akhirnya bisa masuk stdlib: package slices (Go 1.21) dan maps. Yang lama",
                    "tidak dihapus, jadi kamu akan melihat KEDUANYA di kode nyata. Kenali",
                    "sebagai hal yang sama:",
                    "",
                    "  cara lama                      cara sekarang",
                    "  sort.Ints(s)                   slices.Sort(s)",
                    "  sort.Strings(s)                slices.Sort(s)",
                    "  sort.Slice(s, kurangDari)      slices.SortFunc(s, banding)",
                    "  sort.SearchInts(s, x)          slices.BinarySearch(s, x)",
                    "  loop cari sendiri              slices.Contains(s, x), slices.Index(s, x)",
                    "  loop kumpulkan kunci lalu sort slices.Sorted(maps.Keys(m))",
                    "",
                    "Satu beda yang gampang menjebak: pembanding sort.Slice mengembalikan bool",
                    "(a duluan?), sedangkan pembanding slices.SortFunc mengembalikan int -",
                    "negatif, nol, atau positif, seperti strings.Compare.",
                ],
                "code": """package main

import (
	"fmt"
	"maps"
	"slices"
	"strings"
)

type Barang struct {
	Nama  string
	Harga int
}

func main() {
	angka := []int{5, 2, 9, 1, 7}

	urut := slices.Clone(angka) // Sort mengubah di tempat, jadi salin dulu
	slices.Sort(urut)           // pengganti sort.Ints dari Materi 7
	fmt.Println("Asli    :", angka)
	fmt.Println("Terurut :", urut)

	fmt.Println("Max, Min:", slices.Max(angka), slices.Min(angka))
	fmt.Println("Ada 9?  :", slices.Contains(angka, 9))
	fmt.Println("Indeks 1:", slices.Index(angka, 1))
	fmt.Println("Sama?   :", slices.Equal(angka, []int{5, 2, 9, 1, 7}))

	// BinarySearch hanya benar pada slice yang SUDAH terurut
	posisi, ketemu := slices.BinarySearch(urut, 7)
	fmt.Println("Cari 7  :", posisi, ketemu)

	slices.Reverse(urut) // mengubah di tempat, tidak mengembalikan apa pun
	fmt.Println("Dibalik :", urut)

	barang := []Barang{
		{"gula", 14000},
		{"beras", 12000},
		{"minyak", 21000},
	}

	// SortFunc: negatif kalau a duluan, positif kalau b duluan, 0 kalau seri
	slices.SortFunc(barang, func(a, b Barang) int {
		return strings.Compare(a.Nama, b.Nama)
	})
	fmt.Println("Per nama :", barang)

	slices.SortFunc(barang, func(a, b Barang) int {
		return b.Harga - a.Harga // termahal dulu
	})
	fmt.Println("Termahal :", barang)

	stok := map[string]int{"beras": 25, "gula": 10, "minyak": 8}

	// maps.Keys mengembalikan ITERATOR, bukan slice.
	// slices.Sorted menampungnya sekaligus mengurutkannya.
	fmt.Println("Kunci  :", slices.Sorted(maps.Keys(stok)))
	fmt.Println("Nilai  :", slices.Sorted(maps.Values(stok)))

	// Iterator itu bisa di-range langsung (Go 1.23 ke atas)
	cacah := 0
	for range maps.Keys(stok) {
		cacah++
	}
	fmt.Println("Cacah  :", cacah)

	salinan := maps.Clone(stok)
	salinan["gula"] = 99
	fmt.Println("Asli gula   :", stok["gula"])
	fmt.Println("Salinan gula:", salinan["gula"])
}""",
            },
            {
                "body": [
                    "JEBAKAN YANG SUNGGUH MENJEBAK",
                    "",
                    "1. Fungsi generik cuma boleh memakai apa yang DIJANJIKAN constraint-nya.",
                    "   Dengan [T any], baris a > b ditolak compiler: any tidak menjanjikan",
                    "   apa-apa soal urutan. Dengan [T comparable], a == b boleh, a > b tetap",
                    "   tidak. Kalau butuh method, constraint-nya harus interface yang memuat",
                    "   method itu. Isi badan fungsi tidak bisa 'minta lebih' dari janjinya.",
                    "",
                    "2. return nil sering tidak sah di dalam fungsi generik: T bisa saja int,",
                    "   dan int tidak punya nil. Polanya: var kosong T lalu return kosong, false.",
                    "",
                    "3. slices.Sort, slices.Reverse, dan slices.SortFunc mengubah slice DI TEMPAT",
                    "   dan tidak mengembalikan apa pun. Menulis s = slices.Sort(s) tidak",
                    "   dikompilasi. Dan karena slice berbagi data (Materi 7), mengurutkannya",
                    "   ikut mengubah slice lain yang menunjuk array yang sama - pakai",
                    "   slices.Clone(s) dulu kalau yang asli masih dipakai.",
                    "",
                    "4. slices.BinarySearch menganggap slice-nya sudah terurut. Pada slice acak",
                    "   ia tidak error sama sekali, cuma menjawab salah. Bug jenis ini yang",
                    "   paling sulit terlihat karena tidak ada yang berteriak.",
                    "",
                    "5. comparable bukan berarti 'bisa dibandingkan besar-kecil', tapi 'bisa ==",
                    "   dan !='. Slice, map, dan func TIDAK comparable, jadi ketiganya juga",
                    "   tidak bisa jadi kunci map - aturan Materi 8 dan constraint ini satu hal",
                    "   yang sama.",
                    "",
                    "KAPAN JANGAN PAKAI GENERICS",
                    "Kalau yang kamu butuhkan cuma PERILAKU, interface sudah cukup dan lebih",
                    "sederhana; itu tetap cara Go yang utama (Materi 12). Generics baru menang",
                    "kalau tipe konkretnya perlu DIPERTAHANKAN: masuk []int, keluar []int, bukan",
                    "keluar []any yang harus di-assert satu per satu. Pedoman komunitas Go:",
                    "tulis dulu kode biasa, dan jadikan generik baru setelah kamu benar-benar",
                    "menulis fungsi kembar yang ketiga.",
                    "",
                    "SEKILAS ITERATOR (range-over-func, Go 1.23)",
                    "Di kode baru kamu akan makin sering melihat fungsi yang hasilnya langsung",
                    "bisa di-range:",
                    "",
                    "  for k := range maps.Keys(stok) { ... }",
                    "",
                    "maps.Keys TIDAK mengembalikan []string, melainkan iter.Seq[string]: sebuah",
                    "FUNGSI yang tahu cara menyebutkan isinya satu per satu. Karena itu ia tidak",
                    "bisa diberi len() dan tidak bisa diindeks. Kalau kamu butuh slice sungguhan:",
                    "",
                    "  slices.Collect(maps.Keys(m))   jadi slice, urutannya acak seperti map",
                    "  slices.Sorted(maps.Keys(m))    jadi slice sekaligus terurut",
                    "",
                    "Kalau contoh dari internet gagal dengan pesan 'cannot range over ... (value",
                    "of type func(...))', hampir pasti Go di mesinmu lebih tua dari 1.23. Cek",
                    "dengan go version.",
                ],
            },
        ],
    },
    {
        "title": "24. Package, Module & Testing",
        "sections": [
            {
                "body": [
                    "MODULE adalah satuan distribusi kode Go.",
                    "Satu module berisi satu atau banyak package.",
                    "",
                    "Memulai project baru:",
                    "  mkdir proyekku && cd proyekku",
                    "  go mod init github.com/namamu/proyekku",
                    "",
                    "Perintah itu membuat file go.mod yang mencatat nama",
                    "module, versi Go, dan daftar dependensi.",
                    "",
                    "Perintah go yang sering dipakai:",
                    "  go run .          jalankan package di folder ini",
                    "  go build          hasilkan binari",
                    "  go test ./...     jalankan semua test",
                    "  go fmt ./...      rapikan format kode",
                    "  go vet ./...      cari kesalahan umum",
                    "  go mod tidy       bersihkan dependensi tak terpakai",
                    "  go get paket      tambah dependensi",
                    "  go doc fmt.Println   baca dokumentasi",
                    "",
                    "ATURAN VISIBILITAS",
                    "  Nama berawalan HURUF BESAR -> bisa diakses package lain",
                    "  Nama berawalan huruf kecil -> hanya di package sendiri",
                    "",
                    "  func Hitung()   publik",
                    "  func hitung()   privat",
                    "",
                    "Tidak ada kata kunci public/private/protected.",
                ]
            },
            {
                "heading": "Struktur project & unit test",
                "code": """// ==== file: kalkulator/kalkulator.go ====
package kalkulator

import "errors"

var ErrBagiNol = errors.New("pembagi tidak boleh nol")

func Tambah(a, b int) int { return a + b }

func Bagi(a, b int) (int, error) {
	if b == 0 {
		return 0, ErrBagiNol
	}
	return a / b, nil
}

// ==== file: kalkulator/kalkulator_test.go ====
package kalkulator

import (
	"errors"
	"testing"
)

func TestTambah(t *testing.T) {
	kasus := []struct {
		nama    string
		a, b    int
		harapan int
	}{
		{"positif", 2, 3, 5},
		{"negatif", -2, -3, -5},
		{"campur", -2, 5, 3},
		{"nol", 0, 0, 0},
	}

	for _, k := range kasus {
		t.Run(k.nama, func(t *testing.T) {
			hasil := Tambah(k.a, k.b)
			if hasil != k.harapan {
				t.Errorf("Tambah(%d,%d) = %d, harusnya %d",
					k.a, k.b, hasil, k.harapan)
			}
		})
	}
}

func TestBagiNol(t *testing.T) {
	_, err := Bagi(10, 0)
	if !errors.Is(err, ErrBagiNol) {
		t.Errorf("harusnya ErrBagiNol, dapat %v", err)
	}
}"""
            },
            {
                "body": [
                    "Aturan file test:",
                    "  - Nama file harus berakhiran _test.go",
                    "  - Nama fungsi harus diawali Test",
                    "  - Parameternya t *testing.T",
                    "  - Laporkan kegagalan dengan t.Errorf atau t.Fatalf",
                    "      t.Errorf  catat gagal, test LANJUT",
                    "      t.Fatalf  catat gagal, test BERHENTI",
                    "",
                    "Menjalankan test:",
                    "  go test              test di folder ini",
                    "  go test ./...        semua test di project",
                    "  go test -v           tampilkan detail tiap test",
                    "  go test -cover       tampilkan cakupan kode",
                    "  go test -run TestBagi  jalankan test tertentu saja",
                    "  go test -bench=.     jalankan benchmark, bukan cuma test",
                    "  go test -race        detektor race yang di materi Goroutine",
                    "                       & Channel kamu pakai lewat 'go run -race'",
                    "",
                    "Dua yang terakhir itu dibedah di materi Testing Lanjutan.",
                    "",
                    "TABLE-DRIVEN TEST",
                    "Pola di contoh atas adalah gaya resmi komunitas Go:",
                    "kumpulkan semua kasus uji dalam satu slice struct,",
                    "lalu ulangi. Menambah kasus baru cukup menambah",
                    "satu baris, bukan menyalin seluruh fungsi test.",
                    "",
                    "Slice struct itu bentuknya STRUCT ANONIM: tipenya ditulis",
                    "langsung di tempat, tanpa type dan tanpa nama, karena cuma",
                    "dipakai satu fungsi ini. Bedah bentuknya, termasuk arti",
                    "'}{' yang aneh itu, ada di materi Struct & Method.",
                    "",
                    "t.Run membuat subtest bernama, sehingga output",
                    "menunjukkan persis kasus mana yang gagal.",
                    "",
                    "Struktur folder project Go yang umum:",
                    "",
                    "  proyekku/",
                    "    go.mod",
                    "    main.go",
                    "    internal/          hanya boleh dipakai project ini",
                    "      layanan/",
                    "    pkg/               boleh dipakai project lain",
                    "      kalkulator/",
                    "    cmd/               beberapa program sekaligus",
                    "      server/main.go",
                    "      cli/main.go",
                    "",
                    "Folder bernama 'internal' diperlakukan khusus oleh Go:",
                    "package di dalamnya tidak bisa diimpor dari luar module.",
                ]
            },
        ],
    },
    {
        "title": "25. Module, Import & Direktif Compiler",
        "sections": [
            {
                "body": [
                    "Buka repo Go milik orang lain, dua hal pertama yang terlihat selalu sama:",
                    "berkas go.mod di akar folder, dan blok import 5-20 baris di kepala tiap berkas.",
                    "Materi 15 sudah menyuruh menjalankan go mod init; materi ini membedah apa yang",
                    "sebenarnya dihasilkan perintah itu, dan apa arti tiap baris di kepala berkas.",
                    "",
                    "NAMA MODULE ADALAH AWALAN SEMUA JALUR IMPORT.",
                    "Kalau baris pertama go.mod berbunyi:",
                    "  module github.com/andi/tokoku",
                    "maka folder internal/hitung di dalam project itu diimpor sebagai:",
                    "  import \"github.com/andi/tokoku/internal/hitung\"",
                    "",
                    "Jalur import TIDAK dimulai dari nama folder di komputermu. Folder projectnya",
                    "boleh kamu taruh di ~/kerjaan/coba1, namanya di mata Go tetap",
                    "github.com/andi/tokoku. Dan jalur relatif seperti import \"./internal/hitung\"",
                    "TIDAK ADA di Go modern -- itu kebiasaan dari Node/Python, compiler menolaknya.",
                    "",
                    "Kenapa bentuknya seperti URL? Supaya perintah go bisa mengunduhnya sendiri kalau",
                    "suatu hari kode itu dipublikasikan. Untuk project pribadi yang tidak pernah",
                    "diunggah, nama apa pun sah -- tapi biasakan bentuk domain/nama supaya tidak",
                    "bentrok dengan module orang lain saat project itu mulai dipakai bersama.",
                ],
            },
            {
                "heading": "Isi go.mod sebuah project sungguhan",
                "body": [
                    "Baris demi baris:",
                    "",
                    "  module github.com/andi/tokoku",
                    "    Nama module. Inilah awalan jalur import tadi.",
                    "",
                    "  go 1.22",
                    "    Versi BAHASA yang dipakai, bukan versi compiler yang terpasang di mesinmu.",
                    "    Fitur yang baru ada sejak 1.21 ditolak kalau baris ini masih 1.19.",
                    "",
                    "  toolchain go1.23.4",
                    "    Versi compiler yang otomatis diunduh kalau punyamu lebih tua. Baris ini",
                    "    sering muncul sendiri setelah go get; bukan kamu yang mengetiknya.",
                    "",
                    "  require ( ... )",
                    "    Daftar dependensi beserta versinya. Yang berkomentar // indirect BUKAN",
                    "    kamu yang memakainya -- ia dibutuhkan oleh dependensimu. Jangan dihapus",
                    "    manual; ia akan kembali sendiri, atau justru bikin build gagal.",
                    "",
                    "  replace github.com/andi/utilku => ../utilku",
                    "    Alihkan sebuah dependensi ke FOLDER LOKAL. Berguna saat kamu menyunting",
                    "    dua project sekaligus, dan sering lupa dihapus lagi -- akibatnya kode",
                    "    gagal dibangun di komputer orang lain yang tidak punya folder itu.",
                    "",
                    "  exclude github.com/contoh/rusak v1.2.0",
                    "    Larang satu versi tertentu dipakai, misalnya karena versi itu cacat.",
                    "",
                    "go.sum berisi HASH tiap dependensi, dua baris per module. Gunanya memastikan",
                    "isi paket v1.6.0 yang diunduh hari ini sama persis dengan yang dulu. Kalau ada",
                    "yang menukar isinya di server, build GAGAL alih-alih diam-diam memakai kode",
                    "asing. Jadi:",
                    "  - go.sum ikut di-commit ke git. Ia bukan berkas sampah.",
                    "  - Jangan pernah disunting tangan. go mod tidy yang mengurusnya.",
                    "",
                    "VERSI SEMANTIK: v1.6.0 = MAYOR.MINOR.TAMBALAN. Naik MAYOR berarti pembuatnya",
                    "boleh merusak kode lama. Karena itu Go memaksa satu aturan: mulai v2, nomor",
                    "mayornya ikut masuk ke JALUR IMPORT.",
                    "  import \"github.com/gin-gonic/gin\"        library versi v1.x",
                    "  import \"github.com/redis/go-redis/v9\"    library versi v9.x",
                    "Akhiran /v2 atau /v9 itu bukan nama folder, melainkan penanda versi. Efeknya",
                    "v1 dan v2 dari library yang sama bisa hidup berdampingan dalam satu program.",
                    "",
                    "Perintah yang MENYUNTING go.mod / go.sum untukmu:",
                    "  go get contoh.com/pkg@v1.2.3     tambah/pindahkan satu dependensi ke versi itu",
                    "  go get -u ./...                  naikkan dependensi ke versi minor terbaru",
                    "  go mod tidy                      tambah yang kurang, buang yang tak terpakai",
                    "  go mod download                  unduh isinya ke cache, daftar tidak berubah",
                    "  go mod vendor                    salin semua dependensi ke folder vendor/",
                    "  go install contoh.com/alat@latest   pasang PROGRAM-nya, bukan jadi dependensi",
                    "",
                    "Beda yang sering bikin salah: go build menaruh binari di folder ini, go install",
                    "memasangnya ke folder bin milik Go supaya bisa dipanggil dari mana saja. Dan",
                    "sejak Go 1.16 go get TIDAK lagi memasang program -- itu tugas go install.",
                ],
                "code": """// ==== file: go.mod ====
module github.com/andi/tokoku

go 1.22

toolchain go1.23.4

require (
	github.com/google/uuid v1.6.0
	github.com/lib/pq v1.10.9
)

require golang.org/x/text v0.14.0 // indirect

replace github.com/andi/utilku => ../utilku

exclude github.com/contoh/rusak v1.2.0""",
            },
            {
                "heading": "Mengimpor package milik module sendiri",
                "body": [
                    "Simpan ketiganya sesuai penanda lalu jalankan dari folder akar: go run .",
                    "Keluarannya:",
                    "  NOTA",
                    "  Total: 10000",
                    "",
                    "Dua hal yang perlu benar-benar diperhatikan:",
                    "",
                    "  - Jalurnya \"contoh.dev/tokoku/internal/hitung\": nama module + jalur folder.",
                    "    Bukan \"internal/hitung\", bukan pula jalur di hard disk.",
                    "  - Yang ditulis saat memanggil adalah NAMA PACKAGE (harga), bukan nama",
                    "    folder terakhir (hitung). Keduanya boleh berbeda, dan di library",
                    "    sungguhan memang sering berbeda. Inilah penyebab umum error",
                    "    'undefined: hitung' padahal baris import-nya sudah benar.",
                    "    Cara memastikan: buka berkasnya, baca baris package-nya.",
                    "    Sebaliknya, di kodemu sendiri samakan saja nama folder dan package",
                    "    kecuali ada alasan kuat -- tidak ada yang untung dari perbedaan itu.",
                    "",
                    "EMPAT BENTUK BARIS IMPORT:",
                    "",
                    "  import \"fmt\"                    biasa, dipanggil fmt.Println",
                    "  import f \"fmt\"                  alias, dipanggil f.Println",
                    "  import _ \"github.com/lib/pq\"    blank, tidak dipanggil sama sekali",
                    "  import . \"fmt\"                  dot, Println tanpa awalan apa pun",
                    "",
                    "ALIAS wajib kalau dua package berakhiran nama yang sama:",
                    "  import (",
                    "      \"database/sql\"",
                    "      xsql \"contoh.com/alat/sql\"",
                    "  )",
                    "Tanpa alias, keduanya sama-sama bernama sql dan Go menolak berkasnya. Di luar",
                    "kasus bentrok itu jangan memberi alias: pembaca kodemu jadi harus menghafal",
                    "singkatan buatanmu untuk sesuatu yang sudah punya nama resmi.",
                    "",
                    "DOT IMPORT membuang awalan sama sekali. Kelihatan praktis, tapi pembaca",
                    "kehilangan satu-satunya petunjuk asal sebuah nama, dan nama dari package bisa",
                    "bentrok diam-diam dengan variabelmu. Hampir semua tim melarangnya; kamu akan",
                    "menemuinya paling banter di berkas test.",
                    "",
                    "URUTAN BLOK IMPORT yang dipakai seluruh dunia Go:",
                    "  import (",
                    "      \"fmt\"          kelompok pertama: package standar",
                    "      \"os\"",
                    "",
                    "      \"github.com/lib/pq\"                  kelompok kedua: pihak ketiga",
                    "      \"contoh.dev/tokoku/internal/hitung\"   dan package milik module sendiri",
                    "  )",
                    "Di dalam tiap kelompok urutannya alfabetis. gofmt yang mengurutkan, tapi ia",
                    "TIDAK memindahkan baris antar kelompok -- baris kosong pemisah itu kamu yang",
                    "menaruh. goimports (versi gofmt yang lebih pintar) juga menambah import yang",
                    "kurang dan membuang yang tidak terpakai; pasang di editormu sejak hari ini.",
                ],
                "code": """// ==== file: go.mod ====
module contoh.dev/tokoku

go 1.22

// ==== file: internal/hitung/harga.go ====
// Foldernya bernama "hitung", package di dalamnya bernama "harga".
package harga

// Huruf depan besar -> boleh dipakai package lain (lihat Materi 15).
func Total(satuan, jumlah int) int {
	return satuan * jumlah
}

// ==== file: main.go ====
package main

import (
	"fmt"
	"strings"

	"contoh.dev/tokoku/internal/hitung"
)

func main() {
	fmt.Println(strings.ToUpper("nota"))
	fmt.Println("Total:", harga.Total(2500, 4))
}""",
            },
            {
                "heading": "func init(): jalan sebelum main tanpa pernah dipanggil",
                "body": [
                    "Urutan yang dijamin Go setiap kali program mulai:",
                    "  1. Semua package yang diimpor diinisialisasi lebih dulu, sampai tuntas.",
                    "  2. Di tiap package: variabel level package diisi.",
                    "  3. Lalu semua func init() package itu, urut berkas lalu urut baris.",
                    "  4. Paling akhir baru func main() milik package main.",
                    "",
                    "Jadi aturan Materi 1 \"func main() titik awal program\" benar untuk KODE YANG",
                    "KAMU TULIS, tapi ia bukan baris pertama yang dijalankan mesin. Kalau kamu",
                    "memasang titik henti di main dan heran kenapa sebuah variabel sudah terisi,",
                    "jawabannya ada di init().",
                    "",
                    "Aturan init():",
                    "  - Tidak punya parameter dan tidak punya nilai balik. Tidak boleh diubah.",
                    "  - Tidak bisa dipanggil manual; menulis init() di kodemu adalah error.",
                    "  - Boleh lebih dari satu per package, bahkan lebih dari satu per berkas.",
                    "  - Hanya jalan sekali, sebanyak apa pun package itu diimpor orang.",
                    "",
                    "INILAH SEBABNYA BLANK IMPORT ADA:",
                    "  import _ \"github.com/lib/pq\"",
                    "Driver PostgreSQL itu tidak punya satu pun fungsi yang kamu panggil. Yang kamu",
                    "butuhkan adalah init()-nya, yang mendaftarkan diri ke database/sql supaya",
                    "sql.Open(\"postgres\", ...) mengenali nama \"postgres\". Barisnya tampak seperti",
                    "salah ketik atau sisa kode lama, dan MENGHAPUSNYA membuat program tetap",
                    "dikompilasi tapi mati saat jalan dengan pesan 'unknown driver'.",
                    "Ini pengecualian sah dari aturan Materi 1 nomor 3: import tak terpakai memang",
                    "error, kecuali kamu menamainya _ untuk bilang \"aku cuma mau efek sampingnya\".",
                    "Tanda _ itu blank identifier yang sama dengan di Materi 4 (nama, _ := ...):",
                    "artinya \"ada, tapi sengaja tidak dipakai\" -- di sini yang diabaikan bukan nilai",
                    "balik sebuah fungsi, melainkan nama package-nya.",
                    "",
                    "Jangan memakai init() untuk pekerjaan berat: membaca berkas, membuka koneksi,",
                    "memanggil jaringan. Ia jalan sebelum kamu sempat menangani error apa pun, dan",
                    "membuat test sulit dikendalikan karena tidak ada cara mematikannya.",
                ],
                "code": """package main

import "fmt"

// Dijalankan saat variabel level package diisi -- sebelum init() mana pun.
var pajak = hitungPajak()

var kasir string

func hitungPajak() int {
	fmt.Println("1. variabel level package diisi")
	return 11
}

// init() tidak pernah dipanggil siapa pun. Go yang memanggilnya.
func init() {
	fmt.Println("2. init() pertama")
	kasir = "Andi"
}

// Boleh ada lebih dari satu init() dalam satu package.
func init() {
	fmt.Println("3. init() kedua, urut dari atas ke bawah")
}

func main() {
	fmt.Println("4. baru main() jalan")
	fmt.Println("pajak:", pajak, "kasir:", kasir)
}""",
            },
            {
                "heading": "Komentar yang dibaca compiler, bukan manusia",
                "body": [
                    "Sebagian komentar di Go bukan untuk manusia. Tiga yang pasti kamu temui:",
                    "",
                    "1. //go:build -- syarat kapan berkas ini ikut dikompilasi. Ditulis di baris",
                    "   paling atas berkas, di atas package, dan wajib dipisah satu baris kosong:",
                    "     //go:build linux",
                    "",
                    "     package berkas",
                    "   Ada jalan pintas kedua lewat AKHIRAN NAMA BERKAS:",
                    "     simpan_linux.go     ikut dikompilasi hanya di Linux",
                    "     simpan_windows.go   ikut dikompilasi hanya di Windows",
                    "   Inilah jawaban kenapa dua berkas dalam satu folder boleh berisi fungsi",
                    "   dengan nama sama persis: keduanya tidak pernah dikompilasi bersamaan.",
                    "   Kalau sebuah fungsi \"hilang\" padahal berkasnya jelas ada di folder itu,",
                    "   dua hal inilah yang pertama harus diperiksa.",
                    "",
                    "2. //go:embed -- isi berkas dimasukkan ke variabel saat KOMPILASI. Di contoh",
                    "   atas, pesan.txt menyatu ke dalam binari, jadi programnya tetap jalan walau",
                    "   berkas aslinya dihapus. Dipakai untuk template HTML, berkas migrasi SQL,",
                    "   dan aset web supaya hasil deploy tetap satu berkas tunggal. Syaratnya:",
                    "     - import \"embed\", blank kalau tipenya cuma string atau []byte,",
                    "     - komentarnya menempel tepat di atas var, tanpa baris kosong,",
                    "     - berkasnya ada di folder yang sama atau di bawahnya, bukan di atasnya.",
                    "",
                    "3. //go:generate -- perintah yang dijalankan kalau kamu mengetik go generate.",
                    "     //go:generate stringer -type=Status",
                    "   Ia TIDAK ikut jalan saat go build. Gunanya mencatat asal-usul berkas macam",
                    "   status_string.go atau nama_gen.go: berkas itu dibuat mesin, jadi menyunting",
                    "   isinya sia-sia -- suntinganmu tertimpa saat orang menjalankan generate lagi.",
                    "   Berkas begitu biasanya dibuka baris \"Code generated ... DO NOT EDIT.\"",
                    "",
                    "MENGKOMPILASI UNTUK SISTEM LAIN (cross-compile), tanpa mesin target:",
                    "  GOOS=linux   GOARCH=amd64 go build -o server .",
                    "  GOOS=windows GOARCH=amd64 go build -o server.exe .",
                    "  GOOS=darwin  GOARCH=arm64 go build -o server .",
                    "Nilai GOOS dan GOARCH itu pula yang dibaca //go:build dan akhiran nama berkas",
                    "tadi. Satu perintah dari laptopmu menghasilkan binari untuk server orang lain:",
                    "inilah alasan Go begitu digemari untuk program yang harus disebar.",
                ],
                "code": """// ==== file: pesan.txt ====
Teks ini ikut masuk ke dalam binari.
// ==== file: main.go ====
package main

// Blank import: package embed tidak dipanggil sekali pun di kode,
// tapi tanpa barisnya, //go:embed di bawah tidak akan bekerja.
import (
	_ "embed"
	"fmt"
)

//go:embed pesan.txt
var pesan string

func main() {
	fmt.Print(pesan)
	fmt.Println("panjang:", len(pesan))
}""",
            },
        ],
    },
    {
        "title": "26. Server HTTP dengan net/http",
        "sections": [
            {
                "body": [
                    "Materi pertama menjanjikan Go dipakai membangun 'layanan backend",
                    "berskala besar'. Sampai sini semua contohnya masih program konsol yang",
                    "mencetak ke layar lalu selesai. Inilah bagian yang hilang: cara sebuah",
                    "program Go MENUNGGU permintaan dan menjawabnya.",
                    "",
                    "Tidak ada yang perlu dipasang. Server HTTP-nya sudah ada di dalam",
                    "standard library, di package net/http. Di bahasa lain kamu memasang",
                    "Tomcat, Apache, atau Express dulu; di Go, satu berkas binari hasil",
                    "go build SUDAH server-nya sendiri.",
                    "",
                    "SERVER TERPENDEK YANG BISA DITULIS",
                    "",
                    "  package main",
                    "",
                    "  import \"net/http\"",
                    "",
                    "  func main() {",
                    "      http.HandleFunc(\"/\", func(w http.ResponseWriter, r *http.Request) {",
                    "          w.Write([]byte(\"halo dari Go\\n\"))",
                    "      })",
                    "      http.ListenAndServe(\"127.0.0.1:8080\", nil)",
                    "  }",
                    "",
                    "Itu program utuh. Jalankan, buka http://127.0.0.1:8080 di browser, dan",
                    "kamu sudah punya server.",
                    "",
                    "MEMBACA TANDA TANGAN HANDLER",
                    "",
                    "  func(w http.ResponseWriter, r *http.Request)",
                    "",
                    "Hafalkan bentuk ini. Sesudah 'if err != nil', inilah baris yang paling",
                    "sering muncul di kode Go sungguhan; setiap library web yang akan kamu",
                    "baca berputar di sekitarnya.",
                    "",
                    "  w   tempat kamu MENULIS jawaban. Ia sebuah io.Writer (lihat materi",
                    "      Berkas), jadi semua yang bisa menulis ke berkas bisa menulis ke",
                    "      sini juga: fmt.Fprintf(w, ...), io.Copy(w, ...), dan",
                    "      json.NewEncoder(w).Encode(v). Perhatikan ia BUKAN pointer --",
                    "      http.ResponseWriter adalah interface, dan nilai konkret di",
                    "      dalamnya sudah berupa pointer.",
                    "",
                    "  r   permintaan yang MASUK: method, alamat, header, dan isinya. Ia",
                    "      pointer (*http.Request) karena struct-nya besar; menyalinnya",
                    "      untuk setiap permintaan itu pemborosan (materi Pointer).",
                    "",
                    "Handler TIDAK mengembalikan apa pun. Tidak ada 'return jawaban'. Kamu",
                    "menjawab dengan menulis ke w, dan permintaan dianggap selesai begitu",
                    "fungsinya berakhir. Dari situ lahir jebakan pertama: http.Error(w, ...)",
                    "cuma MENULIS pesan gagal, ia tidak menghentikan handler-mu. Lupa",
                    "menulis return sesudahnya berarti satu permintaan dijawab dua kali.",
                    "",
                    "KENAPA ListenAndServe MENGEMBALIKAN error",
                    "Fungsi itu tidak pernah selesai dengan sukses. Ia menghadang di baris",
                    "itu selama server hidup, dan satu-satunya cara ia kembali adalah kalau",
                    "ada yang salah: port 8080 sudah dipakai program lain, atau server",
                    "sengaja dimatikan. Karena itu bentuk yang benar bukan memanggilnya",
                    "lalu lupa, melainkan:",
                    "",
                    "  log.Fatal(http.ListenAndServe(\"127.0.0.1:8080\", nil))",
                    "",
                    "Mengabaikan nilai kembaliannya menghasilkan bug yang paling",
                    "membingungkan buat pemula: program langsung keluar tanpa satu pesan",
                    "pun, karena port-nya ternyata sudah dipakai dan tidak ada yang",
                    "membacakan errornya.",
                    "",
                    "CATATAN JUJUR SOAL APLIKASI INI",
                    "Contoh besar di bawah adalah server sungguhan: ia menunggu SELAMANYA",
                    "dan menyentuh jaringan. Tombol 'Coba jalankan' di sini akan tergantung",
                    "sampai batas waktu lalu dihentikan paksa -- itu bukan error di kodemu.",
                    "Salin ke berkas main.go, jalankan 'go run main.go' di terminalmu",
                    "sendiri, lalu panggil dari browser atau curl. Contoh KEDUA sengaja",
                    "dibuat berhenti sendiri, jadi yang itu boleh kamu tekan.",
                ],
            },
            {
                "heading": "Server sungguhan: mux, JSON, dan middleware",
                "code": """package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"sync"
	"time"
)

type Barang struct {
	Kode  string `json:"kode"`
	Nama  string `json:"nama"`
	Harga int    `json:"harga"`
}

// Setiap permintaan dilayani goroutine SENDIRI, jadi data bersama wajib
// dijaga mutex -- lihat materi Goroutine & Channel.
type Gudang struct {
	mu     sync.RWMutex
	barang map[string]Barang
}

func (g *Gudang) ambil(kode string) (Barang, bool) {
	g.mu.RLock()
	defer g.mu.RUnlock()
	b, ada := g.barang[kode]
	return b, ada
}

func (g *Gudang) simpan(b Barang) {
	g.mu.Lock()
	defer g.mu.Unlock()
	g.barang[b.Kode] = b
}

// w = tempat MENULIS jawaban. r = permintaan yang MASUK.
func (g *Gudang) lihat(w http.ResponseWriter, r *http.Request) {
	kode := r.PathValue("kode") // dari pola "GET /barang/{kode}"
	b, ada := g.ambil(kode)
	if !ada {
		http.Error(w, "barang "+kode+" tidak ada", http.StatusNotFound)
		return // WAJIB: http.Error tidak menghentikan handler
	}
	tulisJSON(w, http.StatusOK, b)
}

func (g *Gudang) tambah(w http.ResponseWriter, r *http.Request) {
	var b Barang
	if err := json.NewDecoder(r.Body).Decode(&b); err != nil {
		http.Error(w, "JSON tidak sah: "+err.Error(), http.StatusBadRequest)
		return
	}
	if b.Kode == "" {
		http.Error(w, "field kode wajib diisi", http.StatusBadRequest)
		return
	}
	g.simpan(b)
	tulisJSON(w, http.StatusCreated, b)
}

func cari(w http.ResponseWriter, r *http.Request) {
	q := r.URL.Query().Get("q") // /cari?q=beras -> "beras"
	if q == "" {
		http.Error(w, "parameter q kosong", http.StatusBadRequest)
		return
	}
	fmt.Fprintf(w, "%s %s mencari %q\\n", r.Method, r.URL.Path, q)
}

// TIGA LANGKAH INI TIDAK BOLEH DIBALIK URUTANNYA.
func tulisJSON(w http.ResponseWriter, status int, v any) {
	w.Header().Set("Content-Type", "application/json") // 1. header
	w.WriteHeader(status)                              // 2. baris status
	json.NewEncoder(w).Encode(v)                       // 3. isi
}

// Middleware: terima Handler, kembalikan Handler.
func catat(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		mulai := time.Now()
		next.ServeHTTP(w, r) // handler aslinya dijalankan di sini
		log.Printf("%s %s selesai dalam %s", r.Method, r.URL.Path, time.Since(mulai))
	})
}

func main() {
	g := &Gudang{barang: map[string]Barang{
		"B001": {Kode: "B001", Nama: "Beras 5kg", Harga: 65000},
	}}

	mux := http.NewServeMux()
	mux.HandleFunc("GET /barang/{kode}", g.lihat)
	mux.HandleFunc("POST /barang", g.tambah)
	mux.HandleFunc("GET /cari", cari)

	srv := &http.Server{
		Addr:         "127.0.0.1:8080",
		Handler:      catat(mux), // seluruh mux dibungkus satu middleware
		ReadTimeout:  5 * time.Second,
		WriteTimeout: 10 * time.Second,
	}

	log.Println("siap di http://127.0.0.1:8080 -- hentikan dengan Ctrl+C")
	if err := srv.ListenAndServe(); err != nil && err != http.ErrServerClosed {
		log.Fatal(err)
	}
}""",
            },
            {
                "body": [
                    "MENGAMBIL ISI PERMINTAAN",
                    "Semuanya ada di r. Yang ini dipakai hampir setiap hari:",
                    "",
                    "  r.Method                     \"GET\", \"POST\", \"PUT\", \"DELETE\",",
                    "                               selalu huruf besar",
                    "  r.URL.Path                   \"/barang/B001\", alamat TANPA ?query",
                    "  r.URL.Query().Get(\"q\")       dari /cari?q=beras menghasilkan \"beras\".",
                    "                               Kalau q memang tidak dikirim, hasilnya \"\"",
                    "                               -- bukan error, jadi kamu sendiri yang",
                    "                               memeriksa kosong atau tidak",
                    "  r.PathValue(\"kode\")          potongan yang ditangkap pola (Go 1.22+)",
                    "  r.Header.Get(\"Content-Type\") satu header, tidak peduli besar-kecil",
                    "                               hurufnya",
                    "  r.FormValue(\"nama\")          isian form HTML biasa",
                    "  r.Body                       isi permintaan, sebuah io.ReadCloser",
                    "",
                    "Semua yang datang dari alamat berbentuk STRING. Angka dikonversi",
                    "sendiri dengan strconv.Atoi (materi Angka & Waktu), dan hasilnya wajib",
                    "diperiksa -- pemakai bisa mengetik /barang?halaman=abc kapan saja.",
                    "",
                    "Untuk badan permintaan berformat JSON, r.Body cukup diserahkan ke",
                    "decoder (materi JSON & Struct Tag):",
                    "",
                    "  var b Barang",
                    "  if err := json.NewDecoder(r.Body).Decode(&b); err != nil {",
                    "      http.Error(w, \"JSON tidak sah\", http.StatusBadRequest)",
                    "      return",
                    "  }",
                    "",
                    "Kamu akan sering melihat 'defer r.Body.Close()' di kode orang. Itu",
                    "tidak salah, tapi di dalam handler memang TIDAK wajib: server yang",
                    "menutup badan permintaan sesudah handler selesai. Yang benar-benar",
                    "wajib adalah resp.Body.Close() di sisi KLIEN -- lihat contoh kedua.",
                    "",
                    "MENULIS JAWABAN: TIGA LANGKAH, URUTANNYA TIDAK BOLEH DIBALIK",
                    "",
                    "  1. w.Header().Set(\"Content-Type\", \"application/json\")",
                    "  2. w.WriteHeader(http.StatusCreated)",
                    "  3. json.NewEncoder(w).Encode(barang)",
                    "",
                    "Kenapa sekeras itu? Karena jawaban HTTP dikirim sebagai aliran byte:",
                    "baris status dulu, lalu header, baru isinya. Begitu satu byte isi",
                    "terkirim, header-nya SUDAH lewat di kabel dan tidak ada cara",
                    "menariknya kembali.",
                    "",
                    "Yang terjadi kalau urutannya salah -- dan tidak satu pun jadi error,",
                    "itulah yang membuatnya sulit ditemukan:",
                    "",
                    "  - Set() sesudah WriteHeader: header itu diabaikan diam-diam.",
                    "    Jawabannya terkirim tanpa Content-Type yang kamu pasang.",
                    "  - Menulis isi tanpa memanggil WriteHeader sama sekali: statusnya",
                    "    otomatis 200 OK. Praktis, tapi berarti handler yang gagal di",
                    "    tengah jalan sudah terlanjur mengirim 200 sebelum kamu sempat",
                    "    memasang 500.",
                    "  - WriteHeader dua kali: yang kedua diabaikan, dan server mencatat",
                    "    di log 'http: superfluous response.WriteHeader call'. Kalau kamu",
                    "    melihat baris itu, biasanya ada return yang lupa ditulis.",
                    "",
                    "Kalau Content-Type tidak kamu pasang, net/http MENEBAKNYA dari 512",
                    "byte pertama isi jawaban. Untuk JSON tebakannya selalu meleset jadi",
                    "text/plain, dan browser menampilkannya sebagai teks mentah alih-alih",
                    "memperlakukannya sebagai data. Pasang sendiri, selalu.",
                    "",
                    "KODE STATUS: PAKAI KONSTANTANYA, JANGAN ANGKANYA",
                    "",
                    "  http.StatusOK                   200  berhasil",
                    "  http.StatusCreated              201  data baru berhasil dibuat",
                    "  http.StatusNoContent            204  berhasil, tanpa isi jawaban",
                    "  http.StatusBadRequest           400  kiriman pemakai salah bentuk",
                    "  http.StatusUnauthorized         401  belum login",
                    "  http.StatusForbidden            403  sudah login, tapi tidak berhak",
                    "  http.StatusNotFound             404  alamatnya tidak ada",
                    "  http.StatusMethodNotAllowed     405  alamat ada, method-nya salah",
                    "  http.StatusInternalServerError  500  SERVER-nya yang bermasalah",
                    "",
                    "w.WriteHeader(403) tetap jalan, tapi konstantanya dibaca orang lebih",
                    "cepat dan salah ketik jadi mustahil: 4o3 tidak akan dikompilasi,",
                    "sedangkan 430 akan diam saja. Ingat pembagian besarnya: 4xx =",
                    "kesalahan PENGIRIM, 5xx = kesalahan SERVER. Membalas 500 untuk input",
                    "yang salah bentuk membuat orang mencari bug di tempat yang keliru.",
                    "",
                    "SERVEMUX: TABEL YANG MEMUTUSKAN HANDLER MANA YANG DIPANGGIL",
                    "",
                    "Argumen kedua ListenAndServe yang tadi diisi nil berarti 'pakai",
                    "DefaultServeMux', sebuah mux GLOBAL milik package net/http. Untuk",
                    "belajar itu praktis; untuk program sungguhan hindari, karena package",
                    "mana pun yang kamu import -- termasuk milik orang lain -- bisa ikut",
                    "mendaftarkan rute di situ tanpa kamu tahu. Buat sendiri dengan",
                    "http.NewServeMux() lalu pasang di srv.Handler.",
                    "",
                    "Sejak Go 1.22 polanya boleh menyebut METHOD dan menangkap potongan",
                    "alamat. Sebelum itu semua orang menulis 'if r.Method != \"GET\"' sendiri",
                    "di setiap handler, atau memasang router pihak ketiga:",
                    "",
                    "  \"/\"                     penampung TERAKHIR: cocok untuk semua alamat",
                    "                          yang tidak tertangkap pola lain",
                    "  \"GET /{$}\"              HANYA \"/\" persis. Inilah halaman depan",
                    "  \"GET /barang/{kode}\"    satu potongan, dibaca r.PathValue(\"kode\")",
                    "  \"POST /barang\"          alamat sama, method beda, handler beda",
                    "  \"/statik/\"              berakhiran garis miring = seluruh cabangnya",
                    "  \"GET /berkas/{sisa...}\" menangkap SISA alamat, garis miringnya ikut",
                    "",
                    "Dua hadiah gratis begitu method ditulis di pola:",
                    "  - POST ke \"GET /cari\" otomatis dibalas 405 Method Not Allowed",
                    "    lengkap dengan header Allow. Kamu tidak menulis sebaris pun.",
                    "  - Mendaftarkan \"GET /x\" otomatis melayani HEAD /x juga.",
                    "",
                    "Kalau dua pola sama-sama cocok, yang LEBIH SPESIFIK menang:",
                    "\"/barang/B001\" mengalahkan \"/barang/{kode}\". Dua pola yang tumpang",
                    "tindih tanpa ada yang lebih spesifik membuat program PANIC saat",
                    "mendaftar, bukan diam-diam salah memilih saat melayani. Itu disengaja",
                    "-- bug rute lebih baik ketahuan sebelum server menyala.",
                    "",
                    "http.Handler vs http.HandlerFunc",
                    "Interface-nya cuma satu method, persis nasihat 'interface sekecil",
                    "mungkin' di materi Interface:",
                    "",
                    "  type Handler interface {",
                    "      ServeHTTP(w http.ResponseWriter, r *http.Request)",
                    "  }",
                    "",
                    "mux, srv.Handler, dan hasil catat() di contoh atas semuanya Handler.",
                    "Lalu dari mana fungsi biasa bisa jadi Handler? Dari lima baris ini,",
                    "salah satu potongan paling pintar di seluruh standard library:",
                    "",
                    "  type HandlerFunc func(http.ResponseWriter, *http.Request)",
                    "",
                    "  func (f HandlerFunc) ServeHTTP(w http.ResponseWriter, r *http.Request) {",
                    "      f(w, r)",
                    "  }",
                    "",
                    "Itu tipe bentukan di atas tipe FUNGSI (materi Tipe Bentukan), lengkap",
                    "dengan method-nya sendiri. Akibatnya http.HandlerFunc(f) BUKAN",
                    "pemanggilan fungsi melainkan KONVERSI TIPE: fungsi biasa berubah jadi",
                    "nilai yang punya ServeHTTP, tanpa ada yang disalin. Dan HandleFunc",
                    "(tanpa huruf r) cuma pembungkus manisnya:",
                    "",
                    "  mux.HandleFunc(pola, f)  sama dengan  mux.Handle(pola, http.HandlerFunc(f))",
                    "",
                    "MIDDLEWARE: HANDLER YANG MEMBUNGKUS HANDLER LAIN",
                    "Bentuknya selalu sama di mana-mana -- terima Handler, kembalikan",
                    "Handler:",
                    "",
                    "  func catat(next http.Handler) http.Handler",
                    "",
                    "Di dalamnya kamu boleh berbuat sesuatu SEBELUM next.ServeHTTP(w, r)",
                    "dan SESUDAHNYA, seperti roti lapis. Pencatatan log, pemeriksaan token",
                    "login, pembatasan jumlah permintaan, dan pemulihan dari panic semuanya",
                    "berbentuk ini. Karena masuk dan keluarnya sama-sama Handler, mereka",
                    "bisa ditumpuk:",
                    "",
                    "  srv.Handler = pulihDariPanic(catat(periksaLogin(mux)))",
                    "",
                    "Yang TERLUAR jalan lebih dulu, dan cuma dia yang bisa menangkap panic",
                    "dari semua yang ada di dalamnya. Karena itu pemulih panic hampir",
                    "selalu dipasang paling luar; menaruhnya di dalam pencatat log berarti",
                    "panic yang terjadi di pencatat itu tetap merobohkan permintaannya.",
                    "",
                    "SATU PERMINTAAN = SATU GOROUTINE",
                    "net/http menjalankan handler-mu di goroutine BARU untuk setiap",
                    "permintaan yang masuk. Kamu tidak menulis satu pun kata 'go' untuk",
                    "itu, dan tidak bisa mematikannya. Konsekuensinya keras: data apa pun",
                    "yang dipakai bersama antar permintaan wajib dijaga, persis seperti di",
                    "materi Goroutine & Channel. Itu sebabnya Gudang di contoh atas",
                    "memegang sync.RWMutex dan bukan map telanjang. map yang dibaca dan",
                    "ditulis bersamaan bukan cuma 'kadang salah' -- Go sengaja",
                    "mendeteksinya lalu mematikan seluruh program:",
                    "",
                    "  fatal error: concurrent map writes",
                    "",
                    "RWMutex dipakai, bukan Mutex biasa, karena membaca boleh berbarengan:",
                    "  RLock/RUnlock  banyak pembaca sekaligus, tidak saling menunggu",
                    "  Lock/Unlock    satu penulis, semua yang lain menunggu",
                    "Buktikan sendiri dengan: go run -race main.go",
                    "",
                    "r.Context() memberi context milik satu permintaan itu (materi",
                    "context). Ia BATAL sendiri begitu kliennya memutus koneksi -- tab",
                    "ditutup, jaringan putus, atau kliennya sendiri kehabisan waktu.",
                    "Teruskan ke setiap pekerjaan berat:",
                    "",
                    "  ctx := r.Context()",
                    "  baris, err := db.QueryContext(ctx, \"SELECT ...\")",
                    "",
                    "Tanpa itu, query untuk halaman yang sudah tidak ditunggu siapa pun",
                    "tetap jalan sampai habis. Sepuluh ribu permintaan yang dibatalkan",
                    "begitu adalah cara server sibuk mati pelan-pelan.",
                ],
            },
            {
                "heading": "Sisi klien, dan berhenti dengan rapi",
                "code": """package main

import (
	"context"
	"fmt"
	"io"
	"net"
	"net/http"
	"strings"
	"time"
)

func halo(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Halo, %s!", r.PathValue("nama"))
}

func rahasia(w http.ResponseWriter, r *http.Request) {
	http.Error(w, "kamu belum login", http.StatusUnauthorized)
}

func main() {
	mux := http.NewServeMux()
	mux.HandleFunc("GET /halo/{nama}", halo)
	mux.HandleFunc("GET /rahasia", rahasia)

	// Port 0 artinya "pinjam port kosong mana pun", supaya contoh ini tidak
	// bentrok dengan program lain yang kebetulan sedang memakai :8080.
	pintu, err := net.Listen("tcp", "127.0.0.1:0")
	if err != nil {
		fmt.Println("gagal membuka port:", err)
		return
	}
	alamat := "http://" + pintu.Addr().String()

	srv := &http.Server{Handler: mux, ReadTimeout: 5 * time.Second}
	go func() { _ = srv.Serve(pintu) }() // server jalan di goroutine sendiri

	// ---------- SISI KLIEN ----------
	// http.Get() memakai klien bawaan yang TIDAK punya batas waktu.
	// Buat klien sendiri; server yang menggantung jangan sampai ikut
	// menggantung program kita.
	klien := &http.Client{Timeout: 5 * time.Second}

	for _, jalur := range []string{"/halo/Levi", "/rahasia", "/tidak-ada"} {
		resp, err := klien.Get(alamat + jalur)
		if err != nil {
			fmt.Println("gagal memanggil:", err)
			continue
		}

		isi, err := io.ReadAll(resp.Body)
		resp.Body.Close() // WAJIB ditutup, apa pun status codenya
		if err != nil {
			fmt.Println("gagal membaca isi:", err)
			continue
		}

		fmt.Printf("%-11s -> %d %-13s | %s\\n", jalur, resp.StatusCode,
			http.StatusText(resp.StatusCode), strings.TrimSpace(string(isi)))
	}

	// ---------- BERHENTI DENGAN RAPI ----------
	// Shutdown menolak sambungan baru lalu MENUNGGU permintaan yang sedang
	// dilayani sampai selesai. ctx-nya adalah batas kesabaran menunggu.
	ctx, batal := context.WithTimeout(context.Background(), 3*time.Second)
	defer batal()

	if err := srv.Shutdown(ctx); err != nil {
		fmt.Println("masih ada yang belum selesai:", err)
		return
	}
	fmt.Println("server berhenti dengan rapi")
}""",
            },
            {
                "body": [
                    "Contoh kedua itu berhenti sendiri, jadi boleh dijalankan dari sini.",
                    "Keluarannya:",
                    "",
                    "  /halo/Levi  -> 200 OK            | Halo, Levi!",
                    "  /rahasia    -> 401 Unauthorized  | kamu belum login",
                    "  /tidak-ada  -> 404 Not Found     | 404 page not found",
                    "  server berhenti dengan rapi",
                    "",
                    "SISI KLIEN: PROGRAMMU MEMANGGIL SERVER LAIN",
                    "Go yang sama juga jadi klien, dan bentuknya cuma tiga baris. Yang",
                    "penting adalah apa yang WAJIB menyertainya:",
                    "",
                    "  resp, err := klien.Get(alamat)",
                    "  if err != nil { return err }",
                    "  defer resp.Body.Close()",
                    "",
                    "Tiga jebakan hidup di tiga baris itu:",
                    "",
                    "1. err == nil TIDAK berarti berhasil. 404 dan 500 adalah jawaban yang",
                    "   sampai dengan selamat, jadi err-nya nil. err hanya terisi kalau",
                    "   KONEKSINYA yang gagal: nama domain tidak ketemu, koneksi ditolak,",
                    "   waktunya habis. Yang menentukan sukses atau tidak adalah",
                    "   resp.StatusCode. Ini beda besar dari banyak library di bahasa lain",
                    "   yang melempar exception untuk status 4xx dan 5xx.",
                    "",
                    "2. Body yang tidak ditutup adalah kebocoran koneksi. Setiap resp",
                    "   memegang satu koneksi TCP sampai body-nya dibaca habis DAN ditutup.",
                    "   Tutup walaupun isinya sama sekali tidak kamu pakai. Dan JANGAN",
                    "   menulis 'defer resp.Body.Close()' di dalam perulangan: defer baru",
                    "   jalan saat FUNGSINYA selesai, bukan saat satu putaran selesai --",
                    "   seribu putaran berarti seribu body menganggur terbuka sampai akhir.",
                    "   Itu sebabnya contoh di atas menutupnya langsung, tanpa defer.",
                    "",
                    "3. http.Get() dan http.Post() memakai klien bawaan yang TIDAK punya",
                    "   batas waktu sama sekali. Server yang menggantung akan menggantung",
                    "   programmu juga, selamanya, tanpa satu pesan pun. Selalu buat",
                    "   klien sendiri:",
                    "",
                    "     klien := &http.Client{Timeout: 5 * time.Second}",
                    "",
                    "Sesudah itu resp.Body cuma sebuah io.Reader biasa: io.ReadAll(resp.Body)",
                    "mengambil semuanya sebagai []byte, atau serahkan langsung ke",
                    "json.NewDecoder(resp.Body).Decode(&v) kalau jawabannya JSON. Untuk",
                    "panggilan yang harus bisa dibatalkan, pakai http.NewRequestWithContext",
                    "lalu klien.Do(req).",
                    "",
                    "&http.Server: KAPAN BERHENTI MEMAKAI ListenAndServe POLOS",
                    "http.ListenAndServe(alamat, nil) tidak punya SATU pun batas waktu.",
                    "Satu klien jahat -- atau cuma jaringan yang buruk -- yang membuka",
                    "koneksi lalu mengirim satu byte per menit bisa menahan sumber daya",
                    "server selamanya. Bentuk yang dipakai di produksi selalu struct-nya:",
                    "",
                    "  srv := &http.Server{",
                    "      Addr:         \"127.0.0.1:8080\",",
                    "      Handler:      catat(mux),",
                    "      ReadTimeout:  5 * time.Second,  // batas membaca permintaan",
                    "      WriteTimeout: 10 * time.Second, // batas menulis jawaban",
                    "      IdleTimeout:  60 * time.Second, // batas koneksi menganggur",
                    "  }",
                    "  srv.ListenAndServe()",
                    "",
                    "Alamat \":8080\" tanpa host berarti MENDENGAR DI SEMUA antarmuka",
                    "jaringan: setiap mesin di WiFi yang sama bisa menghubunginya.",
                    "\"127.0.0.1:8080\" hanya mesinmu sendiri. Selama masih belajar, pakai",
                    "yang kedua -- server latihan yang tidak sengaja terbuka ke jaringan",
                    "adalah cara nyata orang kebobolan.",
                    "",
                    "BERHENTI DENGAN RAPI",
                    "Ctrl+C membunuh proses seketika, memotong permintaan yang sedang",
                    "setengah jalan. srv.Shutdown(ctx) melakukannya dengan sopan: tolak",
                    "sambungan baru, tunggu yang sedang dilayani selesai. ctx-nya adalah",
                    "batas kesabaran menunggu; kalau habis, Shutdown mengembalikan error",
                    "dan sisanya memang dipotong.",
                    "",
                    "Begitu Shutdown dipanggil, ListenAndServe yang sedang menghadang",
                    "KEMBALI dengan error http.ErrServerClosed. Itu bukan kegagalan, itu",
                    "kabar bahwa perintahmu sudah dikerjakan -- dan karena itu",
                    "pemeriksaannya selalu ditulis begini:",
                    "",
                    "  if err := srv.ListenAndServe(); err != nil && err != http.ErrServerClosed {",
                    "      log.Fatal(err)",
                    "  }",
                    "",
                    "YANG SENGAJA TIDAK ADA DI SINI",
                    "net/http sudah cukup untuk server sungguhan. Framework seperti Gin,",
                    "Echo, atau Chi menambah kenyamanan, bukan kemampuan: semuanya berdiri",
                    "di atas http.Handler yang sama, dan middleware mereka berbentuk persis",
                    "seperti catat() tadi. Kalau bagian ini kamu pahami, membaca kode",
                    "framework mana pun tinggal soal mengenali nama baru.",
                    "",
                    "Satu pertanyaan sengaja belum dijawab: bagaimana MENGUJI handler tanpa",
                    "menyalakan server dan tanpa menyentuh jaringan sama sekali? Jawabannya",
                    "package net/http/httptest, dan itu materi berikutnya.",
                ],
            },
        ],
    },
    {
        "title": "27. Testing Lanjutan: Benchmark, Example & httptest",
        "sections": [
            {
                "body": [
                    "Materi Package, Module & Testing memperkenalkan satu bentuk fungsi:",
                    "func TestX(t *testing.T). Buka berkas _test.go di proyek Go sungguhan",
                    "dan kamu akan melihat empat bentuk lain berdiri di sebelahnya.",
                    "",
                    "LIMA FUNGSI YANG DIKENALI go test",
                    "",
                    "  func TestX(t *testing.T)        memeriksa benar atau salah",
                    "  func BenchmarkX(b *testing.B)   mengukur cepat atau lambat",
                    "  func ExampleX()                 contoh pemakaian yang IKUT DIUJI",
                    "  func FuzzX(f *testing.F)        mencari masukan yang merusak",
                    "  func TestMain(m *testing.M)     satu kali setup & bersih-bersih",
                    "",
                    "Yang dikenali hanya nama berbentuk PERSIS begitu: huruf sesudah kata",
                    "Test wajib huruf besar. func Testkecil(t *testing.T) tidak pernah",
                    "dijalankan, dan go test tidak mengeluh sedikit pun -- ia lulus dengan",
                    "tenang tanpa menyentuhnya. Yang menangkapnya go vet:",
                    "",
                    "  Testkecil has malformed name: first letter after 'Test' must not be lowercase",
                    "",
                    "Inilah alasan konkret kenapa 'go vet ./...' bukan basa-basi: test yang",
                    "hilang diam-diam terlihat persis sama dengan test yang lulus.",
                    "",
                    "EMPAT ALAT DI t YANG BELUM PERNAH DIPAKAI",
                    "",
                    "  t.Helper()    'aku cuma pembantu, jangan tunjuk baris di dalamku'",
                    "  t.Parallel()  'aku boleh jalan berbarengan dengan test lain'",
                    "  t.Cleanup(f)  jalankan f saat test ini selesai, lulus maupun gagal",
                    "  t.Skip(...)   berhenti dan tandai DILEWATI -- bukan gagal, bukan lulus",
                    "",
                    "t.Helper() yang paling sering menyelamatkan waktu. Tanpa itu, setiap",
                    "kegagalan yang lewat sebuah fungsi bantu menunjuk baris t.Errorf di",
                    "dalam fungsi bantunya -- baris yang sama untuk sepuluh kasus berbeda,",
                    "dan kamu tidak tahu kasus mana yang jatuh.",
                    "",
                    "t.Cleanup lebih andal daripada defer di badan test, karena ia tetap",
                    "jalan meski testnya berhenti di tengah oleh t.Fatalf.",
                    "",
                    "PACKAGE BERAKHIRAN _test",
                    "Berkas teks_test.go boleh mendeklarasikan 'package teks' (di dalam)",
                    "atau 'package teks_test' (di luar). Hanya berkas _test.go yang boleh",
                    "punya package kedua seperti ini; di tempat lain Go melarangnya.",
                    "",
                    "  package teks       boleh menyentuh fungsi privat huruf kecil",
                    "  package teks_test  wajib mengimpor 'contoh/teks', dan hanya bisa",
                    "                     memakai nama yang huruf depannya BESAR",
                    "",
                    "Pilih yang di luar kalau bisa. Yang teruji jadi API yang sungguhan",
                    "dipakai orang lain, bukan isi perut yang bebas kamu ubah besok pagi.",
                    "Ia juga satu-satunya jalan keluar dari import cycle, misalnya saat",
                    "test butuh package yang justru mengimpor package yang sedang diuji.",
                ],
            },
            {
                "heading": "Satu berkas _test.go yang memakai semuanya",
                "code": """// Siapkan dulu:
//   mkdir belajar-uji && cd belajar-uji
//   go mod init contoh
//   mkdir teks

// ==== file: teks/teks.go ====
package teks

// Balik membalik urutan karakter s. Ia bekerja per rune, bukan per byte,
// supaya huruf beraksen tidak tercabik jadi byte tak bermakna.
func Balik(s string) string {
	r := []rune(s)
	for i, j := 0, len(r)-1; i < j; i, j = i+1, j-1 {
		r[i], r[j] = r[j], r[i]
	}
	return string(r)
}

// ==== file: teks/teks_test.go ====
package teks_test

import (
	"fmt"
	"os"
	"path/filepath"
	"strings"
	"testing"

	"contoh/teks"
)

// TestMain berjalan SEKALI untuk seluruh package: semua yang ada di sini
// terjadi sebelum dan sesudah SEMUA test. Wajib memanggil os.Exit(m.Run()),
// kalau tidak hasil testnya tidak pernah dilaporkan ke go test.
func TestMain(m *testing.M) {
	fmt.Println("--- siapkan data uji ---")
	kode := m.Run()
	fmt.Println("--- bereskan data uji ---")
	os.Exit(kode)
}

// cocok adalah fungsi bantu. t.Helper() membuat laporan gagal menunjuk
// baris PEMANGGIL, bukan baris t.Errorf yang ada di dalam sini.
func cocok(t *testing.T, dapat, harapan string) {
	t.Helper()
	if dapat != harapan {
		t.Errorf("dapat %q, harusnya %q", dapat, harapan)
	}
}

func TestBalik(t *testing.T) {
	t.Parallel()

	kasus := []struct {
		nama, masuk, harapan string
	}{
		{"biasa", "kucing", "gnicuk"},
		{"kosong", "", ""},
		{"palindrom", "katak", "katak"},
		{"beraksen", "naïf", "fïan"},
	}
	for _, k := range kasus {
		t.Run(k.nama, func(t *testing.T) {
			t.Parallel()
			cocok(t, teks.Balik(k.masuk), k.harapan)
		})
	}
}

func TestTulisBerkas(t *testing.T) {
	folder := t.TempDir()
	jalur := filepath.Join(folder, "catatan.txt")
	t.Cleanup(func() {
		fmt.Println("--- selesai memakai", filepath.Base(jalur))
	})

	if err := os.WriteFile(jalur, []byte("halo"), 0o644); err != nil {
		t.Fatalf("gagal menulis: %v", err)
	}
	isi, err := os.ReadFile(jalur)
	if err != nil {
		t.Fatalf("gagal membaca: %v", err)
	}
	cocok(t, string(isi), "halo")
}

func TestKalimatPanjang(t *testing.T) {
	if testing.Short() {
		t.Skip("dilewati karena dijalankan dengan -short")
	}
	panjang := strings.Repeat("gado-gado ", 1000)
	cocok(t, teks.Balik(teks.Balik(panjang)), panjang)
}

// Penampung supaya compiler tidak menyimpulkan hasilnya tidak terpakai
// lalu membuang seluruh panggilan yang sedang diukur.
var simpan string

func BenchmarkBalik(b *testing.B) {
	kalimat := strings.Repeat("gado-gado ", 50)
	b.ReportAllocs()
	b.ResetTimer()

	var s string
	for i := 0; i < b.N; i++ {
		s = teks.Balik(kalimat)
	}
	simpan = s
}

// Komentar // Output: bukan hiasan: isinya dibandingkan dengan keluaran
// sungguhan, jadi contoh ini ikut diuji go test.
func ExampleBalik() {
	fmt.Println(teks.Balik("Kucing"))
	fmt.Println(teks.Balik("katak"))
	// Output:
	// gnicuK
	// katak
}

func FuzzBalik(f *testing.F) {
	f.Add("halo")
	f.Add("")
	f.Add("naïf")
	f.Fuzz(func(t *testing.T, s string) {
		if teks.Balik(teks.Balik(s)) != s {
			t.Errorf("dibalik dua kali harusnya kembali ke %q", s)
		}
	})
}""",
            },
            {
                "body": [
                    "MENJALANKAN BENCHMARK",
                    "",
                    "  go test -bench=.            jalankan semua benchmark",
                    "  go test -bench=Balik        yang namanya cocok pola saja",
                    "  go test -bench=. -benchmem  tambahkan kolom memori",
                    "  go test -bench=. -run=^$    benchmark saja, semua test dilewati",
                    "",
                    "Tanpa -bench, benchmark TIDAK dijalankan sama sekali. Itu bukan",
                    "kelalaian: mengukur waktu itu lambat, jadi Go tidak melakukannya",
                    "kecuali diminta. Pola -run=^$ artinya 'jalankan test yang namanya",
                    "cocok dengan pola kosong' -- tidak ada yang cocok, jadi yang tersisa",
                    "tinggal benchmark-nya.",
                    "",
                    "Keluaran sungguhannya:",
                    "",
                    "  goos: linux",
                    "  goarch: amd64",
                    "  pkg: contoh/teks",
                    "  BenchmarkBalik-8    47832    32569 ns/op    2560 B/op    2 allocs/op",
                    "",
                    "Dibaca dari kiri:",
                    "  BenchmarkBalik-8   nama, lalu jumlah inti (GOMAXPROCS) -- bukan hasil",
                    "  47832              berapa kali fungsinya dipanggil; ini b.N terakhir",
                    "  32569 ns/op        nanodetik per satu panggilan",
                    "  2560 B/op          byte yang dialokasikan per panggilan",
                    "  2 allocs/op        berapa KALI alokasi terjadi per panggilan",
                    "",
                    "Angkanya berbeda di tiap mesin dan tiap kali dijalankan. Yang berarti",
                    "bukan angkanya, melainkan PERBANDINGAN sebelum dan sesudah kamu ubah",
                    "kodenya. allocs/op sering lebih berguna daripada ns/op: alokasi bisa",
                    "dihitung dan stabil, sedangkan waktu ikut naik-turun oleh beban mesin.",
                    "",
                    "KENAPA b.N ADA",
                    "Kamu tidak pernah mengisi b.N. Yang mengisinya runtime: fungsimu",
                    "dipanggil 1 kali, lalu 100, lalu 10.000, naik terus sampai totalnya",
                    "cukup lama (bawaannya sekitar 1 detik) untuk diukur dengan jujur.",
                    "Satu panggilan tunggal terlalu cepat; jam komputer tidak sehalus itu.",
                    "",
                    "Akibatnya badan benchmark WAJIB berbentuk:",
                    "",
                    "  for i := 0; i < b.N; i++ { ... }",
                    "",
                    "Tiga kesalahan yang benar-benar sering terjadi:",
                    "  - Menulis 'i < 1000' dan mengabaikan b.N. Go tetap membagi total",
                    "    waktunya dengan b.N, jadi ns/op yang keluar omong kosong.",
                    "  - Menaruh persiapan berat di dalam loop, sehingga yang terukur",
                    "    persiapannya. Obatnya b.ResetTimer() sesudah persiapan.",
                    "  - Membuang hasil panggilan. Compiler boleh menghapus perhitungan",
                    "    yang hasilnya tidak dipakai, dan benchmark-nya jadi mengukur",
                    "    kekosongan. Itu sebabnya contoh di atas menyimpannya ke",
                    "    'var simpan string' di tingkat package.",
                    "",
                    "  b.ResetTimer()   nol-kan stopwatch, buang waktu persiapan",
                    "  b.StopTimer()    jeda di tengah loop kalau ada persiapan per iterasi",
                    "  b.StartTimer()   lanjutkan lagi",
                    "  b.ReportAllocs() paksa kolom B/op dan allocs/op muncul",
                    "",
                    "PERINTAH LAIN YANG DIPAKAI SEHARI-HARI",
                    "",
                    "  go test -short           lewati yang dijaga testing.Short()",
                    "  go test -race            detektor race; 2-10x lebih lambat, pakai di CI",
                    "  go test -cover           persentase pernyataan yang tersentuh",
                    "  go test -coverprofile=cover.out ./...",
                    "  go tool cover -func=cover.out          rincian per fungsi",
                    "  go tool cover -html=cover.out -o cover.html    warnai baris di browser",
                    "  go test -fuzz=FuzzBalik -fuzztime=30s",
                    "",
                    "Rincian -func-nya berbentuk begini, dan justru kolom yang BUKAN 100%",
                    "yang berguna -- ia menunjuk cabang yang belum pernah dijalankan:",
                    "",
                    "  contoh/web/handler.go:15:  Halo          100.0%",
                    "  contoh/web/handler.go:27:  AmbilPesan     75.0%",
                    "  total:                     (statements)   85.7%",
                    "",
                    "Cakupan tinggi bukan bukti kode benar; ia cuma bukti barisnya pernah",
                    "dijalankan. Baris yang dijalankan tanpa satu pun pemeriksaan tetap",
                    "menghitung 100%.",
                    "",
                    "EXAMPLE: DOKUMENTASI YANG TIDAK BISA BASI",
                    "Komentar '// Output:' di akhir ExampleBalik bukan hiasan. Keluaran",
                    "fungsi itu ditangkap lalu dibandingkan dengan isi komentarnya, jadi",
                    "contoh yang tidak lagi cocok dengan kodenya akan MERAH -- tidak bisa",
                    "diam-diam ketinggalan zaman seperti contoh di README.",
                    "",
                    "Aturannya:",
                    "  - Nama sesudah Example harus menunjuk identifier yang benar-benar",
                    "    ada: ExampleBalik untuk func Balik, ExampleAntre_Ambil untuk",
                    "    method Ambil pada tipe Antre. Nama karangan ditegur go vet.",
                    "  - Varian kedua ditambahi garis bawah plus huruf KECIL:",
                    "    ExampleBalik_kosong.",
                    "  - '// Unordered output:' kalau urutan barisnya tidak dijamin.",
                    "  - Contoh TANPA komentar Output tetap dikompilasi tapi TIDAK PERNAH",
                    "    dijalankan. Ini jebakan sunyi: kamu merasa punya test, padahal",
                    "    yang kamu punya cuma kode yang lolos compiler.",
                    "",
                    "Yang menampilkan Example sebagai contoh siap salin adalah dokumentasi",
                    "web-nya (pkg.go.dev atau perkakas godoc), bukan perintah 'go doc' di",
                    "terminal -- 'go doc -all' hanya menampilkan komentar dokumentasinya.",
                    "",
                    "FUZZING: MENCARI MASALAH, BUKAN MEMBUKTIKAN BENAR",
                    "Tanpa -fuzz, FuzzBalik cuma menjalankan benih dari f.Add. Dengan",
                    "-fuzz, Go mengarang masukan baru terus-menerus dan menyimpan yang",
                    "menambah cakupan. Contoh di atas jatuh dalam hitungan detik:",
                    "",
                    "  --- FAIL: FuzzBalik",
                    "      dibalik dua kali harusnya kembali ke \"\\xc8\"",
                    "      Failing input written to testdata/fuzz/FuzzBalik/d6be63583e2876b0",
                    "",
                    "Fuzzer-nya tidak sedang rewel. []rune mengubah byte yang bukan UTF-8",
                    "sah menjadi U+FFFD, jadi Balik memang tidak bisa mengembalikannya --",
                    "sebuah bug sungguhan yang tidak akan pernah kamu tebak sendiri.",
                    "",
                    "Jebakan yang menyusul: berkas di testdata/fuzz itu jadi kasus uji",
                    "PERMANEN. Sejak saat itu 'go test' biasa pun ikut merah selamanya,",
                    "sampai bug-nya diperbaiki atau berkas korpusnya dihapus. Itu memang",
                    "disengaja -- supaya bug yang sudah ketemu tidak bisa dilupakan.",
                    "",
                    "t.Parallel() DAN AKIBATNYA",
                    "Test ber-t.Parallel() ditahan dulu, lalu dilepas bersama-sama sesudah",
                    "test yang berurutan selesai. Keuntungannya jelas; harganya juga:",
                    "  - Test yang berbagi variabel global mendadak saling menimpa.",
                    "  - Test yang mengubah folder kerja atau environment ikut merusak",
                    "    tetangganya. Pakai t.Setenv dan t.TempDir, jangan os.Setenv.",
                    "  - Urutan keluaran -v jadi berselang-seling, bukan tanda kerusakan.",
                    "Pasangkan dengan 'go test -race' -- detektor yang sama yang di materi",
                    "Goroutine & Channel dipanggil lewat 'go run -race'. Dengan begitu data",
                    "yang dipakai berbarengan ketahuan sebagai laporan race yang menyebut",
                    "baris dan goroutine-nya, bukan sebagai kegagalan aneh sekali sebulan.",
                    "",
                    "Sejak Go 1.22, variabel perulangan dibuat ulang tiap iterasi, jadi",
                    "baris 'k := k' yang dulu wajib sebelum t.Run + t.Parallel sekarang",
                    "sudah tidak perlu. Kalau melihatnya di kode lama, itu bukan kesalahan",
                    "-- itu jejak Go versi lama.",
                ],
            },
            {
                "heading": "Menguji HTTP tanpa membuka satu port pun",
                "body": [
                    "Handler HTTP dan mux-nya dibahas di materi Server HTTP dengan net/http.",
                    "Di sini pertanyaannya berbeda: bagaimana cara mengujinya?",
                    "",
                    "Godaan pertamanya adalah menyalakan server sungguhan di port 8080 lalu",
                    "menembaknya dari test. Itu berantakan: port bisa sudah dipakai program",
                    "lain, test yang paralel saling rebutan port, dan kalau satu test lupa",
                    "mematikan server-nya, test berikutnya gagal karena alasan yang sama",
                    "sekali tidak berhubungan dengan kode yang sedang diuji.",
                    "",
                    "Package net/http/httptest menyediakan tiga hal:",
                    "",
                    "  httptest.NewRequest(metode, url, badan)  permintaan palsu",
                    "  httptest.NewRecorder()   penampung jawaban; punya .Code, .Header(),",
                    "                           dan .Body -- semua bisa diperiksa langsung",
                    "  httptest.NewServer(h)    server sungguhan di 127.0.0.1, port pilihan",
                    "                           sistem, hidup selama test saja",
                    "",
                    "Dua yang pertama untuk menguji HANDLER buatanmu, dan tidak membuka",
                    "satu port pun: handler itu cuma fungsi biasa, jadi panggil saja",
                    "langsung seperti fungsi lain. Yang ketiga untuk menguji KLIEN buatanmu",
                    "-- klien butuh lawan bicara, dan srv.URL memberi alamat yang hidup.",
                    "Selalu pasangkan dengan defer srv.Close(), kalau tidak server-nya",
                    "menumpuk sampai test selesai.",
                    "",
                    "Syarat yang gampang dilupakan: alamat servernya harus jadi PARAMETER,",
                    "bukan konstanta di dalam fungsi. Fungsi yang menuliskan alamat",
                    "produksinya langsung di badannya mustahil diuji tanpa internet -- dan",
                    "yang diuji jadi keadaan jaringanmu, bukan kodemu.",
                ],
                "code": """// ==== file: web/handler.go ====
package web

import (
	"encoding/json"
	"io"
	"net/http"
)

type Sapaan struct {
	Pesan string `json:"pesan"`
}

// Halo adalah handler biasa. Perhatikan: ia tidak tahu apa-apa soal port,
// alamat, atau server. Ia cuma sebuah fungsi yang menulis ke w.
func Halo(w http.ResponseWriter, r *http.Request) {
	nama := r.URL.Query().Get("nama")
	if nama == "" {
		http.Error(w, "nama wajib diisi", http.StatusBadRequest)
		return
	}
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(Sapaan{Pesan: "Halo, " + nama})
}

// AmbilPesan adalah sisi KLIEN: ia memanggil server milik orang lain.
// Alamatnya sengaja jadi parameter -- itulah yang membuatnya bisa diuji.
func AmbilPesan(alamat string) (string, error) {
	resp, err := http.Get(alamat)
	if err != nil {
		return "", err
	}
	defer resp.Body.Close()

	isi, err := io.ReadAll(resp.Body)
	if err != nil {
		return "", err
	}
	return string(isi), nil
}

// ==== file: web/handler_test.go ====
package web_test

import (
	"net/http"
	"net/http/httptest"
	"strings"
	"testing"

	"contoh/web"
)

// Tidak ada port yang dibuka di sini. NewRequest membuat permintaan palsu,
// NewRecorder menampung jawabannya, lalu handler-nya dipanggil langsung.
func TestHalo(t *testing.T) {
	req := httptest.NewRequest(http.MethodGet, "/halo?nama=Levi", nil)
	rek := httptest.NewRecorder()

	web.Halo(rek, req)

	if rek.Code != http.StatusOK {
		t.Fatalf("status %d, harusnya 200", rek.Code)
	}
	if ct := rek.Header().Get("Content-Type"); ct != "application/json" {
		t.Errorf("Content-Type %q, harusnya application/json", ct)
	}
	badan := strings.TrimSpace(rek.Body.String())
	if badan != `{"pesan":"Halo, Levi"}` {
		t.Errorf("badan %s", badan)
	}
}

func TestHaloTanpaNama(t *testing.T) {
	rek := httptest.NewRecorder()
	web.Halo(rek, httptest.NewRequest(http.MethodGet, "/halo", nil))

	if rek.Code != http.StatusBadRequest {
		t.Errorf("status %d, harusnya 400", rek.Code)
	}
}

// Menguji sisi klien butuh lawan bicara. NewServer menyalakan server
// sungguhan di 127.0.0.1 dengan port pilihan sistem, hidup selama test saja.
func TestAmbilPesan(t *testing.T) {
	srv := httptest.NewServer(http.HandlerFunc(
		func(w http.ResponseWriter, r *http.Request) {
			w.Write([]byte("dari server palsu"))
		}))
	defer srv.Close()

	pesan, err := web.AmbilPesan(srv.URL)
	if err != nil {
		t.Fatalf("tidak terduga: %v", err)
	}
	if pesan != "dari server palsu" {
		t.Errorf("dapat %q", pesan)
	}
}""",
            },
            {
                "heading": "testdata dan berkas golden",
                "body": [
                    "FOLDER testdata",
                    "Perkakas Go mengabaikan folder bernama testdata: isinya tidak pernah",
                    "dikompilasi, tidak ikut 'go build ./...', dan namanya tidak dianggap",
                    "package. Itu tempat resmi menaruh berkas contoh -- sampel JSON,",
                    "potongan CSV, gambar rusak untuk diuji, apa pun.",
                    "",
                    "  lapor/",
                    "    lapor.go",
                    "    lapor_test.go",
                    "    testdata/",
                    "      laporan.golden",
                    "",
                    "Saat test berjalan, direktori kerjanya SELALU folder package itu",
                    "sendiri. Jadi 'testdata/laporan.golden' selalu benar, tak peduli dari",
                    "folder mana kamu mengetik go test.",
                    "",
                    "BERKAS GOLDEN",
                    "Untuk keluaran panjang -- laporan, HTML, JSON -- menuliskan harapannya",
                    "di dalam kode itu menyiksa dan sulit dibaca. Polanya: simpan keluaran",
                    "yang sudah kamu periksa dengan mata ke sebuah berkas 'golden', lalu",
                    "test tinggal membandingkan.",
                    "",
                    "Flag -update itu buatan sendiri dengan package flag, bukan bawaan Go.",
                    "Karena itu posisinya di baris perintah menjebak:",
                    "",
                    "  go test -update ./lapor/    SALAH -> no Go files in ...",
                    "  go test ./lapor/ -update    benar: flag milik binari test di belakang",
                    "",
                    "Satu lagi yang menyita waktu tanpa perlu: -update MENULIS berkasnya,",
                    "tapi tidak membuat foldernya. Kalau testdata/ belum ada, yang keluar",
                    "cuma 'no such file or directory'. Buat sekali saja: mkdir testdata",
                    "",
                    "Dan ada disiplin yang wajib menyertainya: -update membuat test SELALU",
                    "lulus, karena harapannya baru saja ditimpa oleh hasilnya sendiri.",
                    "Baca 'git diff' berkas golden-nya sebelum commit. Kalau tidak, sebuah",
                    "bug diam-diam berubah jadi perilaku yang 'benar' menurut testmu.",
                ],
                "code": """package lapor

import (
	"bytes"
	"flag"
	"os"
	"path/filepath"
	"testing"
)

var perbarui = flag.Bool("update", false, "tulis ulang berkas golden")

func TestLaporan(t *testing.T) {
	hasil := []byte(Laporan([]string{"gula", "kopi", "teh"}))
	emas := filepath.Join("testdata", "laporan.golden")

	if *perbarui {
		if err := os.WriteFile(emas, hasil, 0o644); err != nil {
			t.Fatalf("gagal menulis golden: %v", err)
		}
	}

	harapan, err := os.ReadFile(emas)
	if err != nil {
		t.Fatalf("golden belum ada; jalankan: go test -update (%v)", err)
	}
	if !bytes.Equal(hasil, harapan) {
		t.Errorf("keluaran beda dari %s; periksa, lalu go test -update", emas)
	}
}""",
            },
        ],
    },
    {
        "title": "28. Studi Kasus: Manajemen Inventaris",
        "sections": [
            {
                "body": [
                    "Kita gabungkan semua materi jadi satu program utuh:",
                    "sistem inventaris barang sederhana.",
                    "",
                    "Konsep yang dipakai:",
                    "  struct dan method",
                    "  interface untuk laporan",
                    "  map untuk penyimpanan",
                    "  slice dan sort untuk urutan yang stabil",
                    "  error kustom dan errors.Is",
                    "  pointer receiver untuk mengubah data",
                    "  fmt.Printf untuk keluaran berformat",
                    "",
                    "Perhatikan bagaimana kunci map dikumpulkan lalu",
                    "diurutkan sebelum dicetak. Tanpa itu, urutan output",
                    "berubah-ubah setiap kali program dijalankan.",
                ]
            },
            {
                "heading": "inventaris.go",
                "code": """package main

import (
	"errors"
	"fmt"
	"sort"
)

var (
	ErrTidakDitemukan = errors.New("barang tidak ditemukan")
	ErrStokKurang     = errors.New("stok tidak mencukupi")
)

type Barang struct {
	Kode  string
	Nama  string
	Harga int
	Stok  int
}

func (b Barang) NilaiTotal() int {
	return b.Harga * b.Stok
}

func (b Barang) String() string {
	return fmt.Sprintf("%-6s %-14s %8d x%3d = %9d",
		b.Kode, b.Nama, b.Harga, b.Stok, b.NilaiTotal())
}

type Inventaris struct {
	barang map[string]*Barang
}

func BuatInventaris() *Inventaris {
	return &Inventaris{barang: make(map[string]*Barang)}
}

func (i *Inventaris) Tambah(b Barang) {
	if lama, ada := i.barang[b.Kode]; ada {
		lama.Stok += b.Stok
		return
	}
	salinan := b
	i.barang[b.Kode] = &salinan
}

func (i *Inventaris) Ambil(kode string, jumlah int) error {
	b, ada := i.barang[kode]
	if !ada {
		return fmt.Errorf("kode %s: %w", kode, ErrTidakDitemukan)
	}
	if b.Stok < jumlah {
		return fmt.Errorf("%s butuh %d punya %d: %w",
			b.Nama, jumlah, b.Stok, ErrStokKurang)
	}
	b.Stok -= jumlah
	return nil
}

// kodeTerurut menjamin output selalu sama urutannya.
func (i *Inventaris) kodeTerurut() []string {
	kode := make([]string, 0, len(i.barang))
	for k := range i.barang {
		kode = append(kode, k)
	}
	sort.Strings(kode)
	return kode
}

func (i *Inventaris) Laporan() {
	fmt.Println("=== LAPORAN INVENTARIS ===")
	total := 0
	for _, k := range i.kodeTerurut() {
		b := i.barang[k]
		fmt.Println(b)
		total += b.NilaiTotal()
	}
	fmt.Printf("Jumlah jenis : %d\\n", len(i.barang))
	fmt.Printf("Nilai total  : %d\\n", total)
}

func (i *Inventaris) StokMenipis(batas int) []string {
	var hasil []string
	for _, k := range i.kodeTerurut() {
		if i.barang[k].Stok < batas {
			hasil = append(hasil, i.barang[k].Nama)
		}
	}
	return hasil
}

func main() {
	inv := BuatInventaris()

	inv.Tambah(Barang{"B001", "Beras 5kg", 65000, 20})
	inv.Tambah(Barang{"B002", "Gula 1kg", 15000, 8})
	inv.Tambah(Barang{"B003", "Minyak 2L", 32000, 12})
	inv.Tambah(Barang{"B002", "Gula 1kg", 15000, 5})

	inv.Laporan()

	fmt.Println()
	for _, uji := range []struct {
		kode   string
		jumlah int
	}{
		{"B001", 5},
		{"B002", 100},
		{"B999", 1},
	} {
		err := inv.Ambil(uji.kode, uji.jumlah)
		switch {
		case err == nil:
			fmt.Printf("Ambil %s x%d berhasil\\n", uji.kode, uji.jumlah)
		case errors.Is(err, ErrStokKurang):
			fmt.Println("Gagal, stok kurang:", err)
		case errors.Is(err, ErrTidakDitemukan):
			fmt.Println("Gagal, tidak terdaftar:", err)
		}
	}

	fmt.Println()
	inv.Laporan()
	fmt.Println("\\nStok di bawah 15:", inv.StokMenipis(15))
}"""
            },
            {
                "body": [
                    "Keputusan desain yang perlu diperhatikan:",
                    "",
                    "1. map[string]*Barang menyimpan POINTER, bukan nilai.",
                    "   Kalau menyimpan nilai, b.Stok -= jumlah hanya",
                    "   mengubah salinan dan data asli tidak berubah.",
                    "",
                    "2. Method Tambah membuat salinan lebih dulu:",
                    "     salinan := b",
                    "     i.barang[b.Kode] = &salinan",
                    "   Ini mencegah pemanggil ikut memegang pointer ke",
                    "   data internal inventaris.",
                    "",
                    "3. kodeTerurut() dipanggil di semua tempat yang",
                    "   mencetak. Urutan map yang acak adalah sumber bug",
                    "   yang sulit dilacak, terutama saat menulis test.",
                    "",
                    "4. Error dibungkus dengan %w supaya errors.Is tetap",
                    "   bisa mengenalinya, sambil menambah konteks",
                    "   yang berguna bagi pembaca pesan error.",
                    "",
                    "5. Method String() membuat Barang otomatis tercetak",
                    "   rapi lewat fmt.Println tanpa fungsi tambahan.",
                    "",
                    "Lanjutan yang bisa kamu coba sendiri. Ini bukan janji",
                    "kosong: bahan tiap butirnya sudah ada materinya.",
                    "",
                    "  - Simpan data ke berkas JSON dengan encoding/json.",
                    "    Struct tag, Marshal, dan Unmarshal ada di materi",
                    "    JSON & Struct Tag.",
                    "  - Ubah agar aman dipakai banyak goroutine dengan",
                    "    sync.RWMutex. RWMutex, Once, dan atomic ada di materi",
                    "    Pola Goroutine.",
                    "  - Tambah antarmuka baris perintah: subperintah tambah,",
                    "    ambil, dan daftar. os.Args, flag, dan log ada di materi",
                    "    Program Baris Perintah.",
                    "  - Tulis unit test untuk Ambil dan StokMenipis, gaya",
                    "    table-driven dari materi Package, Module & Testing.",
                    "  - Tambah pencatatan riwayat transaksi.",
                ]
            },
        ],
    },
]
