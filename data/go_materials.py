GO_MATERIALS = [
    {
        "title": "1. Pengenalan Go & Instalasi",
        "sections": [
            {
                "body": [
                    "Go itu bahasa pemrograman buatan Google, dirilis tahun 2009.",
                    "Perancangnya tiga orang: Robert Griesemer, Rob Pike, dan Ken Thompson.",
                    "Orang sering menyebutnya \"Golang\", karena situs resminya dulu",
                    "golang.org.",
                    "",
                    "Dua sifat Go yang perlu kamu tahu dari awal:",
                    "  - Go itu bahasa compiled. Artinya, sebelum dijalankan, kodemu diubah",
                    "    dulu jadi satu file binari mandiri, yaitu program siap jalan.",
                    "  - Go itu statically typed. Artinya, tipe tiap variabel (angka, teks,",
                    "    dan seterusnya) dicek waktu kompilasi, sebelum programnya jalan.",
                    "",
                    "Kenapa banyak perusahaan pakai Go?",
                    "  - Kompilasinya cepat, cuma hitungan detik.",
                    "  - Hasilnya satu file binari. Gampang dipasang di server, nggak perlu",
                    "    memasang runtime atau penerjemah tambahan.",
                    "  - Concurrency, yaitu menjalankan banyak pekerjaan sekaligus, gampang",
                    "    dan murah berkat goroutine.",
                    "  - Sintaksnya sedikit, jadi cepat dipelajari.",
                    "  - Ada garbage collector yang membereskan memori otomatis, jadi kamu",
                    "    nggak perlu ngatur memori sendiri.",
                    "",
                    "Program yang dibikin pakai Go antara lain Docker, Kubernetes,",
                    "Terraform, Prometheus, dan banyak layanan backend berskala besar.",
                    "",
                    "Cara memasang:",
                    "  - Unduh dari https://go.dev/dl",
                    "  - Cek hasilnya dengan perintah: go version",
                    "",
                    "Cara menjalankan program:",
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
                    "Kita bahas bagian demi bagian:",
                    "",
                    "  package main",
                    "    Setiap file Go milik sebuah package, yaitu kelompok kode. Nama",
                    "    main itu khusus: dia menandai program yang bisa dijalankan.",
                    "",
                    "  import \"fmt\"",
                    "    Memuat package standar fmt (singkatan dari format) untuk input",
                    "    dan output.",
                    "",
                    "  func main()",
                    "    Titik awal program. Wajib ada di package main.",
                    "",
                    "  fmt.Println(...)",
                    "    Mencetak teks, lalu pindah baris.",
                    "",
                    "Beberapa aturan Go yang langsung kerasa:",
                    "  1. Nggak perlu titik koma di akhir baris.",
                    "  2. Kurung kurawal pembuka harus di baris yang sama.",
                    "     func main() {     BENAR",
                    "     func main()",
                    "     {                 SALAH, program tidak akan dikompilasi",
                    "  3. Import yang nggak dipakai dianggap error. Go nggak cuma ngasih",
                    "     peringatan, programnya gagal dikompilasi.",
                    "  4. Variabel lokal yang nggak dipakai juga error.",
                    "  5. Indentasi resmi pakai tab, dan dirapikan otomatis oleh gofmt.",
                    "",
                    "Aturan 3 dan 4 memang terasa galak di awal. Untungnya, kode jadi",
                    "tetap bersih dan nggak ada sisa-sisa yang numpuk.",
                    "",
                    "Nanti di kode orang lain kamu bakal ketemu dua pengecualian. Biar",
                    "nggak bingung:",
                    "  - Import yang diawali garis bawah, misalnya import _ \"paket\". Paket",
                    "    itu memang nggak pernah dipakai, tapi tetap sah.",
                    "  - func init(). Fungsi ini jalan sebelum main, padahal nggak ada yang",
                    "    memanggilnya.",
                    "Dua-duanya dibahas di materi Module, Import & Direktif Compiler. Untuk",
                    "sekarang belum perlu dipahami.",
                ]
            },
        ],
    },
    {
        "title": "2. Variabel, Konstanta & Tipe Data",
        "sections": [
            {
                "body": [
                    "Variabel itu tempat menyimpan nilai, dan tiap variabel punya nama. Di",
                    "Go ada tiga cara membuatnya:",
                    "",
                    "  var nama string = \"Andi\"     lengkap dengan tipe",
                    "  var nama = \"Andi\"            tipe ditebak dari nilai",
                    "  nama := \"Andi\"               bentuk singkat",
                    "",
                    "Bentuk := paling sering dipakai. Tapi bentuk ini cuma boleh di dalam",
                    "fungsi. Di level package, yaitu di luar semua fungsi, kamu wajib",
                    "pakai var.",
                    "",
                    "Ada satu aturan := yang sering bikin bingung. Sisi kirinya boleh berisi",
                    "nama yang udah ada, asal minimal satu nama di situ masih baru. Nama",
                    "yang lama cuma diisi ulang, nama yang baru dibuat.",
                    "",
                    "  n, err := hitung()      n dan err sama-sama baru",
                    "  m, err := hitungLagi()  m baru, err diisi ulang -> sah",
                    "  n, err := hitung()      tidak ada nama baru sama sekali:",
                    "                          no new variables on left side of :=",
                    "",
                    "Shadowing",
                    "",
                    "Variabel di dalam sebuah blok boleh punya nama yang sama dengan",
                    "variabel di luarnya. Yang di dalam menutupi yang di luar, istilahnya",
                    "shadowing, dan compiler nggak protes:",
                    "",
                    "  err := simpan()",
                    "  if err != nil {",
                    "      err := kirim(err)   err BARU, hidup di blok if saja",
                    "      fmt.Println(err)",
                    "  }",
                    "  // err di luar masih hasil simpan(), tak tersentuh",
                    "",
                    "Bentuk if err := f(); err != nil juga selalu bikin err yang baru. Dari",
                    "sini muncul bug yang sering banget kejadian: kamu merasa error-nya",
                    "hilang, padahal yang kamu periksa di luar ternyata err yang lain.",
                    "",
                    "Kalau sebuah variabel nggak diisi, dia otomatis dapat nilai bawaan,",
                    "istilahnya zero value:",
                    "  angka   -> 0",
                    "  string  -> \"\" (kosong)",
                    "  bool    -> false",
                    "  pointer, slice, map -> nil",
                    "",
                    "Go nggak punya nilai undefined. Begitu dibuat, setiap variabel",
                    "langsung punya nilai yang jelas.",
                    "",
                    "Konstanta dibuat pakai const. Nilainya harus udah diketahui waktu",
                    "kompilasi:",
                    "  const Pi = 3.14159",
                    "  const NamaApp = \"Belajar Go\"",
                    "",
                    "Beberapa const boleh dikumpulkan dalam satu blok, mirip blok",
                    "var ( ... ) di kode di bawah:",
                    "  const (",
                    "      Pi      = 3.14159",
                    "      NamaApp = \"Belajar Go\"",
                    "  )",
                    "Ada juga blok const yang berisi nama tanpa nilai di sebelahnya. Itu",
                    "pola tersendiri bernama iota, dan dibahas di materi Tipe Bentukan,",
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
                    "Konversi tipe harus ditulis sendiri",
                    "",
                    "Go nggak pernah mengubah tipe tanpa kamu minta:",
                    "",
                    "  var a int = 5",
                    "  var b float64 = a          SALAH, tidak dikompilasi",
                    "  var b float64 = float64(a) BENAR",
                    "",
                    "Aturan ini mencegah bug kecil yang muncul dari konversi yang nggak",
                    "disengaja.",
                    "",
                    "Untuk mengubah teks jadi angka atau sebaliknya, pakai package strconv:",
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
                    "Hati-hati waktu membagi. Hasilnya tergantung tipe angkanya:",
                    "  7 / 2       -> 3     kedua operand int, hasilnya int",
                    "  7.0 / 2.0   -> 3.5   operand float, hasilnya float",
                    "  float64(7) / float64(2) -> 3.5",
                    "",
                    "Operand itu angka atau nilai yang dikenai operator. Kalau dua-duanya",
                    "int, sisa desimalnya dibuang.",
                    "",
                    "Di Go, i++ dan i-- adalah pernyataan, bukan ekspresi. Jadi dia harus",
                    "berdiri sendiri di satu baris, dan nggak bisa dipakai sebagai nilai:",
                    "  x := i++      SALAH",
                    "  i++           BENAR",
                    "Bentuk ++i juga nggak ada sama sekali.",
                    "",
                    "Operator penugasan:",
                    "  =   +=   -=   *=   /=   %=",
                    "",
                    "Operator perbandingan (hasilnya bool):",
                    "  ==  !=  <  <=  >  >=",
                    "",
                    "Operator logika:",
                    "  &&  DAN     ||  ATAU     !  NOT",
                    "",
                    "&& dan || sama-sama short-circuit. Artinya, Go berhenti menilai begitu",
                    "hasilnya udah pasti. Misalnya di a && b, kalau a udah false, b nggak",
                    "dicek lagi.",
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
                    "Operator bitwise dipakai untuk mengotak-atik bit, yaitu angka 0 dan 1",
                    "di balik sebuah bilangan:",
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
                    "Kalau ragu, pakai kurung. Kode yang jelas lebih gampang dibaca daripada",
                    "kode yang mengandalkan hafalan tabel prioritas.",
                    "",
                    "Go nggak punya operator ternary (kondisi ? a : b). Tulis aja if-else",
                    "biasa. Ini sengaja dibikin begitu supaya kodenya tetap gampang dibaca.",
                ]
            },
        ],
    },
    {
        "title": "4. Angka & Waktu: math, time & strconv",
        "sections": [
            {
                "body": [
                    "Operator + - * / % dari materi sebelumnya cuma cukup untuk hitungan",
                    "paling dasar. Kalau kamu butuh akar, pangkat, atau pembulatan, alatnya",
                    "ada di package math.",
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
                    "Ada juga konstanta yang udah disiapkan:",
                    "  math.Pi          3.141592653589793",
                    "  math.MaxInt64    bilangan int64 terbesar",
                    "  math.MaxFloat64  float64 terbesar",
                    "",
                    "math.Pi ini yang nanti dipakai di rumus luas lingkaran",
                    "(math.Pi * r * r), di materi Interface dan latihannya.",
                    "",
                    "Jebakan: semua fungsi math menerima dan mengembalikan float64. Versi",
                    "int-nya nggak ada.",
                    "",
                    "  n := 81",
                    "  math.Sqrt(n)            SALAH, gagal DIKOMPILASI",
                    "  math.Sqrt(float64(n))   BENAR",
                    "",
                    "Pesan compilernya persis begini:",
                    "  cannot use n (variable of type int) as float64 value",
                    "  in argument to math.Sqrt",
                    "",
                    "Ini aturan \"konversi harus ditulis sendiri\" dari Materi 2. Hasilnya",
                    "juga float64. Kalau mau balik ke int, ingat bahwa int(3.9) memotong",
                    "jadi 3, nggak membulatkan. Kalau maunya dibulatkan, tulis",
                    "int(math.Round(3.9)).",
                    "",
                    "Ada tiga fungsi builtin, yaitu fungsi bawaan yang bisa dipakai tanpa",
                    "import apa pun (Go 1.21 ke atas):",
                    "  min(a, b, ...)  nilai terkecil",
                    "  max(a, b, ...)  nilai terbesar",
                    "  clear(m)        kosongkan map (dibahas di materi Map)",
                    "",
                    "math.Min dan math.Max masih ada, tapi cuma bisa dipakai untuk",
                    "float64. Builtin min dan max bisa menerima int, float, bahkan string.",
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
                    "Kenapa 0.1 + 0.2 nggak sama dengan 0.3",
                    "",
                    "float64 menyimpan pecahan dalam basis dua. Angka 0.1 nggak bisa",
                    "ditulis pas di basis dua, sama seperti 1/3 nggak bisa ditulis pas di",
                    "basis sepuluh (0,333... terus tanpa ujung). Jadi yang tersimpan selalu",
                    "nilai terdekat, belum tentu angka yang kamu ketik.",
                    "",
                    "  a := 0.1",
                    "  b := 0.2",
                    "  a + b       -> 0.30000000000000004",
                    "  a+b == 0.3  -> false",
                    "",
                    "Anehnya, kalau 0.1 + 0.2 == 0.3 ditulis langsung tanpa variabel,",
                    "hasilnya malah true. Soalnya konstanta dihitung compiler dengan",
                    "presisi tinggi sebelum program jalan. Jebakannya baru kelihatan",
                    "begitu angkanya lewat variabel.",
                    "",
                    "Dua akibatnya yang perlu kamu ingat:",
                    "  - Jangan bandingkan float pakai ==. Bandingkan selisihnya:",
                    "      math.Abs(x-y) < 0.000001",
                    "  - Jangan simpan uang sebagai float64. Sesudah ribuan kali",
                    "    penjumlahan, saldonya bisa meleset beberapa sen, dan selisih itu",
                    "    susah dilacak asalnya. Simpan dalam satuan terkecil sebagai int,",
                    "    lalu bagi cuma waktu ditampilkan:  harga := 19999   // rupiah utuh",
                    "",
                    "Teks ke angka dan sebaliknya: package strconv",
                    "",
                    "Materi 2 udah nyebut Atoi dan Itoa. Ini daftar lengkapnya:",
                    "  strconv.ParseFloat(s, 64)           teks -> float64",
                    "  strconv.ParseInt(s, basis, 64)      teks -> int64",
                    "  strconv.ParseBool(\"true\")            teks -> bool",
                    "  strconv.FormatFloat(f, 'f', 2, 64)  float64 -> teks",
                    "  strconv.FormatInt(255, 16)          int64 -> teks basis 16",
                    "  strconv.Quote(s)                    bungkus jadi literal Go",
                    "",
                    "Basis di ParseInt: 2 untuk biner, 8 oktal, 10 biasa, 16 heksa. Angka",
                    "64 di belakangnya artinya hasilnya harus muat di 64 bit.",
                    "",
                    "Semua fungsi Parse mengembalikan dua nilai: hasil dan err. Kalau",
                    "teksnya ternyata bukan angka, hasilnya 0 dan err berisi alasannya.",
                    "Untuk input dari pengguna, jangan pernah buang err itu pakai _.",
                    "",
                    "Jebakan: string(65) hasilnya \"A\", bukan \"65\". Konversi tipe nggak sama",
                    "dengan memformat angka jadi teks. Di sini 65 dibaca sebagai nomor",
                    "karakter Unicode, dan karakter nomor 65 itu huruf A. Kalau mau angka",
                    "jadi teks, pakai strconv.Itoa(65) atau fmt.Sprintf(\"%d\", 65).",
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
                    "Format tanggal: angkanya 1 2 3 4 5 6",
                    "",
                    "Go nggak kenal format seperti \"YYYY-MM-DD\". Caranya lain: kamu menulis",
                    "ulang satu tanggal acuan yang sama untuk semua orang, dalam bentuk",
                    "yang kamu mau. Tanggal acuannya ini:",
                    "",
                    "  Mon Jan 2 15:04:05 MST 2006",
                    "",
                    "Angka-angkanya sengaja berurutan supaya gampang diingat:",
                    "  1  bulan   Jan / January / 01",
                    "  2  hari    2 / 02 / Monday",
                    "  3  jam     3 (12 jam), atau 15 untuk format 24 jam,",
                    "             karena jam acuannya jam 3 sore alias 15.00",
                    "  4  menit   4 / 04",
                    "  5  detik   5 / 05",
                    "  6  tahun   06 / 2006",
                    "",
                    "Jadi \"2006-01-02\" artinya tahun-bulan-hari, dan \"02/01/2006\" artinya",
                    "hari/bulan/tahun. Bentuk format ini disebut layout. Nol di depan juga",
                    "ditiru: \"01\" memaksa dua digit, \"1\" membiarkan angkanya apa adanya.",
                    "",
                    "Kalau kamu nulis t.Format(\"YYYY-MM-DD\"), nggak ada error sama sekali.",
                    "Hasilnya cuma teks YYYY-MM-DD apa adanya. Ini jebakan yang paling",
                    "sering kena ke orang yang datang dari bahasa lain: nggak ada yang",
                    "negur, tahu-tahu hasilnya salah.",
                    "",
                    "time.Parse, yang mengubah teks jadi tanggal, pakai layout yang sama.",
                    "Dia ketat soal kecocokan bentuknya:",
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
                    "Duration itu angka yang dikasih nama",
                    "",
                    "time.Duration itu tipe untuk lama waktu. Isinya cuma int64 berisi",
                    "jumlah nanodetik, dengan nama tipe sendiri, jadi dia bukan struct.",
                    "Karena itu 5 * time.Second sah ditulis: yang terjadi cuma angka",
                    "dikali angka.",
                    "",
                    "  time.Nanosecond  Microsecond  Millisecond",
                    "  time.Second      Minute       Hour",
                    "  jeda := 300 * time.Millisecond",
                    "  jeda.Seconds()      -> 0.3",
                    "  fmt.Println(jeda)   -> 300ms, dicetak rapi bukan angka",
                    "  time.Sleep(2 * time.Second)   menghentikan program 2 detik",
                    "",
                    "Tapi variabel bertipe int nggak bisa langsung dikalikan:",
                    "  detik := 5",
                    "  detik * time.Second   SALAH",
                    "  -> mismatched types int and time.Duration",
                    "  time.Duration(detik) * time.Second   BENAR",
                    "",
                    "Yang lain yang sering dipakai:",
                    "  time.Now()         waktu sekarang",
                    "  time.Since(mulai)  Duration sejak mulai, untuk mengukur",
                    "  t.Before(t2)       mana yang lebih dulu; pasangannya t.After",
                    "  t.Unix()           detik sejak 1 Januari 1970",
                    "  t.Equal(t2)        bandingkan dengan ini, JANGAN dengan ==,",
                    "                     karena time.Time menyimpan zona waktu dan",
                    "                     jam monotonik yang ikut dibandingkan",
                    "",
                    "Catatan: time.Now() bikin keluaran program berubah tiap kali",
                    "dijalankan. Jangan pakai dia di solusi latihan yang dinilai otomatis",
                    "di aplikasi ini. Kunci jawabannya didapat dengan menjalankan solusi",
                    "contoh, jadi hasilmu nggak bakal pernah cocok. Pakai time.Date dengan",
                    "tanggal tetap.",
                ],
            },
        ],
    },
    {
        "title": "5. Input & Output dengan fmt",
        "sections": [
            {
                "body": [
                    "Package fmt punya fungsi-fungsi utama untuk mencetak:",
                    "",
                    "  fmt.Print(...)    cetak tanpa baris baru",
                    "  fmt.Println(...)  cetak lalu pindah baris,",
                    "                    argumen dipisah spasi otomatis",
                    "  fmt.Printf(...)   cetak dengan format khusus",
                    "  fmt.Sprintf(...)  sama seperti Printf tapi hasilnya",
                    "                    dikembalikan sebagai string",
                    "",
                    "Namanya nggak asal. Ada tiga awalan yang berpasangan:",
                    "  tanpa awalan  Print   Println   Printf   -> ke layar",
                    "  awalan S      Sprint  Sprintln  Sprintf  -> jadi string",
                    "  awalan F      Fprint  Fprintln  Fprintf  -> ke tujuan lain",
                    "",
                    "Yang berawalan F minta tujuan sebagai argumen pertama:",
                    "  fmt.Fprintln(os.Stderr, \"gagal:\", err)",
                    "Tujuannya boleh apa aja yang bisa ditulisi, termasuk berkas. Pesan",
                    "error sebaiknya dikirim ke os.Stderr, supaya nggak campur dengan",
                    "keluaran asli programmu.",
                    "",
                    "Masih satu keluarga: fmt.Errorf. Cara kerjanya persis seperti",
                    "Sprintf, cuma hasilnya sebuah error, bukan string. Fungsi ini bakal",
                    "sering kamu pakai di materi Error Handling.",
                    "",
                    "Printf memakai kata kerja format, istilahnya verb. Verb itu kode",
                    "berawalan % yang nunjukin nilainya dicetak dalam bentuk apa:",
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
                    "Verb lain yang bakal kamu temui di kode orang:",
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
                    "Ada tiga cara membaca input. Pilih sesuai kebutuhan:",
                    "",
                    "  1. fmt.Scan atau fmt.Scanln. Ini yang paling singkat.",
                    "       var n int",
                    "       fmt.Scan(&n)",
                    "     Tanda & wajib ditulis. Fungsinya butuh alamat variabel supaya",
                    "     bisa mengubah isinya. Kekurangannya, Scan berhenti di spasi, jadi",
                    "     nggak cocok buat membaca kalimat.",
                    "",
                    "  2. bufio.NewReader(os.Stdin).ReadString('\\n')",
                    "     Membaca sampai akhir baris, termasuk spasinya. Hasilnya masih",
                    "     mengandung karakter pindah baris (newline), jadi wajib",
                    "     dibersihkan pakai strings.TrimSpace.",
                    "",
                    "  3. bufio.NewScanner(os.Stdin)",
                    "       pemindai := bufio.NewScanner(os.Stdin)",
                    "       for pemindai.Scan() {",
                    "           baris := pemindai.Text()",
                    "       }",
                    "     Paling cocok untuk membaca banyak baris sampai habis.",
                    "",
                    "Tanda garis bawah _ di nama, _ := ... disebut blank identifier.",
                    "Artinya nilai kedua sengaja dibuang. Ini perlu karena Go melarang",
                    "variabel yang nggak dipakai.",
                ]
            },
        ],
    },
    {
        "title": "6. Percabangan (if & switch)",
        "sections": [
            {
                "body": [
                    "Percabangan artinya program memilih jalan: kalau kondisinya benar,",
                    "kerjakan ini, kalau nggak, kerjakan yang lain. Bentuk if di Go:",
                    "",
                    "  if kondisi {",
                    "      ...",
                    "  } else if kondisiLain {",
                    "      ...",
                    "  } else {",
                    "      ...",
                    "  }",
                    "",
                    "Kalau kamu pernah belajar C atau Java, ini bedanya:",
                    "  - Kondisinya nggak dibungkus kurung biasa.",
                    "      if x > 5 {        BENAR",
                    "      if (x > 5) {      jalan, tapi tidak idiomatis",
                    "    Idiomatis artinya sesuai kebiasaan programmer Go. Pakai kurung",
                    "    tetap jalan, cuma kelihatan aneh di mata orang yang biasa nulis",
                    "    Go.",
                    "  - Kurung kurawal wajib, walaupun isinya cuma satu baris.",
                    "  - Kondisinya harus bertipe bool. Angka nggak bisa jadi kondisi.",
                    "      if 1 { }          SALAH di Go",
                    "  - else harus ditulis di baris yang sama dengan } penutup.",
                    "",
                    "Ada satu fitur khas Go: pernyataan pendek sebelum kondisi.",
                    "",
                    "  if n, err := strconv.Atoi(teks); err == nil {",
                    "      fmt.Println(\"Angka:\", n)",
                    "  }",
                    "",
                    "Variabel n dan err cuma hidup di dalam blok if itu. Pola ini sering",
                    "banget dipakai untuk menangani error.",
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
                    "switch cocok kalau kamu membandingkan satu nilai dengan banyak",
                    "kemungkinan. Beberapa kelebihan switch di Go:",
                    "",
                    "  1. Nggak perlu break. Setiap case otomatis berhenti sesudah",
                    "     selesai. Di C dan Java kebalikannya: lupa break bikin program",
                    "     lanjut ke case berikutnya (fallthrough) tanpa disengaja, dan itu",
                    "     sumber bug.",
                    "  2. Satu case boleh menampung beberapa nilai:",
                    "       case 6, 7:",
                    "  3. switch tanpa ekspresi sama dengan if-else berantai, cuma lebih",
                    "     rapi:",
                    "       switch {",
                    "       case nilai >= 85:",
                    "       }",
                    "  4. Kalau memang perlu lanjut ke case berikutnya, tulis sendiri",
                    "     kata fallthrough:",
                    "       case 1:",
                    "           fmt.Println(\"satu\")",
                    "           fallthrough",
                    "  5. switch juga bisa pakai pernyataan pendek:",
                    "       switch hari := time.Now().Weekday(); hari {",
                    "       case time.Saturday, time.Sunday:",
                    "           fmt.Println(\"Libur\")",
                    "       }",
                    "     Contoh ini butuh import \"time\", yang udah kamu pakai di materi",
                    "     Angka & Waktu.",
                    "  6. Type switch, untuk memeriksa tipe di balik sebuah interface:",
                    "       switch v := x.(type) {",
                    "       case int:    fmt.Println(\"int:\", v)",
                    "       case string: fmt.Println(\"string:\", v)",
                    "       }",
                    "     Interface dan bentuk x.(type) dibahas lengkap di materi",
                    "     Interface. Di sini cukup kenali bentuk switch-nya. Kamu belum",
                    "     ketinggalan apa-apa.",
                ]
            },
        ],
    },
    {
        "title": "7. Perulangan (for)",
        "sections": [
            {
                "body": [
                    "Perulangan artinya mengerjakan hal yang sama berkali-kali. Go cuma",
                    "punya satu kata kunci perulangan, yaitu for. Nggak ada while, nggak",
                    "ada do-while. Sebagai gantinya, for punya empat bentuk yang bisa",
                    "menggantikan semuanya.",
                    "",
                    "  1. Bentuk lengkap, seperti for di C:",
                    "       for i := 0; i < 10; i++ {",
                    "       }",
                    "  2. Bentuk kondisi saja, perannya sama seperti while:",
                    "       for i < 10 {",
                    "           i++",
                    "       }",
                    "  3. Tanpa apa pun, jadi perulangan yang nggak pernah berhenti",
                    "     sendiri:",
                    "       for {",
                    "           if selesai { break }",
                    "       }",
                    "  4. Bentuk range, untuk menelusuri isi sebuah koleksi:",
                    "       for indeks, nilai := range slice {",
                    "       }",
                    "",
                    "Sama seperti if, kondisi for juga nggak dibungkus kurung biasa.",
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
                    "range menghasilkan nilai yang beda-beda, tergantung apa yang",
                    "ditelusuri:",
                    "  Pada slice/array : indeks, nilai",
                    "  Pada string      : posisi byte, rune (karakter)",
                    "  Pada map         : kunci, nilai",
                    "  Pada channel     : nilai saja",
                    "  Pada int         : 0, 1, 2, ... sampai n-1 (Go 1.22)",
                    "",
                    "Bentuk yang terakhir paling baru. Waktu pertama lihat, biasanya orang",
                    "kaget karena nggak ada koleksi apa pun di situ:",
                    "  for i := range 10 { }   mengulang sepuluh kali, i = 0..9",
                    "  for range 10 { }        sepuluh kali, angkanya tak dipakai",
                    "Ini cara singkat untuk for i := 0; i < 10; i++.",
                    "",
                    "Kalau cuma butuh indeks, tulis satu variabel aja:",
                    "  for i := range buah { }",
                    "Kalau cuma butuh nilai, buang indeksnya pakai _ :",
                    "  for _, b := range buah { }",
                    "",
                    "Jebakan: urutan map selalu acak. Go sengaja mengacak urutan",
                    "penelusuran map setiap kali program dijalankan. Jadi jangan pernah",
                    "mengandalkan urutannya. Kalau butuh urut, kumpulkan dulu kuncinya,",
                    "lalu urutkan:",
                    "    kunci := make([]string, 0, len(m))",
                    "    for k := range m { kunci = append(kunci, k) }",
                    "    sort.Strings(kunci)",
                    "    for _, k := range kunci { fmt.Println(k, m[k]) }",
                    "",
                    "Empat baris itu pakai make, append, dan map, yang belum kamu pelajari.",
                    "Jadi nggak usah dihafal sekarang. make dan append dibahas di materi",
                    "Array & Slice, map di materi Map. Balik lagi ke sini sesudah dua",
                    "materi itu selesai, dan resep ini bakal gampang dibaca.",
                    "",
                    "Mengendalikan perulangan:",
                    "  break      keluar dari perulangan",
                    "  continue   lompat ke iterasi berikutnya",
                    "",
                    "Untuk keluar dari perulangan bersarang (perulangan di dalam",
                    "perulangan), pakai label:",
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
                    "Array dan slice sama-sama menyimpan banyak nilai bertipe sama secara",
                    "berurutan, misalnya daftar nilai ujian. Bentuknya mirip, tapi",
                    "perilakunya beda.",
                    "",
                    "Array: panjangnya tetap, dan panjang itu bagian dari tipenya.",
                    "  var angka [5]int",
                    "  nilai := [3]string{\"a\", \"b\", \"c\"}",
                    "",
                    "Jadi [3]int dan [5]int itu dua tipe yang beda. Di kode sehari-hari,",
                    "array jarang dipakai langsung.",
                    "",
                    "Slice: panjangnya bisa berubah. Yang biasa dipakai sehari-hari itu slice.",
                    "  var angka []int",
                    "  nilai := []string{\"a\", \"b\", \"c\"}",
                    "  data := make([]int, 3)      panjang 3, isi nol semua",
                    "  data := make([]int, 0, 10)  panjang 0, kapasitas 10",
                    "",
                    "Bedanya waktu ditulis cuma satu: ada angka di dalam kurung siku atau",
                    "nggak. Tapi perilakunya jauh beda.",
                    "",
                    "Slice itu ibarat jendela ke sebuah array yang tersembunyi. Isinya tiga",
                    "hal: pointer (penunjuk) ke datanya, panjang (len), dan kapasitas",
                    "(cap). Kapasitas itu jumlah tempat yang udah disiapkan, termasuk yang",
                    "belum diisi.",
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
                    "Hal-hal yang wajib kamu pahami soal slice:",
                    "",
                    "  1. append mengembalikan slice baru. Hasilnya harus ditampung lagi:",
                    "       angka = append(angka, 4)    BENAR",
                    "       append(angka, 4)            SALAH, hasilnya hilang",
                    "  2. Slice berbagi data dengan slice asalnya.",
                    "       a := []int{1, 2, 3}",
                    "       b := a[0:2]",
                    "       b[0] = 99",
                    "       fmt.Println(a)   -> [99 2 3], a ikut berubah!",
                    "     Kalau butuh salinan yang terpisah, pakai copy().",
                    "  3. Slice kosong dan slice nil itu beda:",
                    "       var a []int           nil, tapi tetap aman dipakai",
                    "       b := []int{}          tidak nil, panjang 0",
                    "     Dua-duanya bisa langsung di-append.",
                    "  4. Mengakses indeks di luar batas bikin panic, yaitu program",
                    "     berhenti mendadak waktu jalan. Ini bukan error kompilasi, jadi",
                    "     compiler nggak bisa mencegahnya. Selalu cek len() sebelum",
                    "     mengakses indeks yang nilainya baru diketahui waktu program",
                    "     jalan.",
                    "  5. Menghapus elemen di indeks i:",
                    "       s = append(s[:i], s[i+1:]...)",
                    "     Tanda ... membongkar slice jadi argumen yang terpisah-pisah.",
                    "  6. Mengurutkan dengan aturan sendiri pakai sort.Slice. sort.Ints dan",
                    "     sort.Strings cuma tahu urutan bawaan. Untuk aturan lain, kasih",
                    "     fungsi pembanding:",
                    "       sort.Slice(daftar, func(i, j int) bool {",
                    "           return daftar[i] < daftar[j]",
                    "       })",
                    "     Perhatikan: pembandingnya menerima indeks i dan j, bukan",
                    "     elemennya. Elemennya kamu ambil sendiri dari slice-nya, seperti",
                    "     daftar[i] di atas. Kembalikan true kalau elemen i harus berdiri",
                    "     di depan elemen j. Untuk membalik urutan, cukup ganti < jadi >.",
                    "     Beda dengan append, sort.Slice mengurutkan di tempat, jadi nggak",
                    "     ada yang perlu ditampung lagi.",
                    "",
                    "Slice dua dimensi:",
                    "  matriks := [][]int{{1, 2}, {3, 4}}",
                    "  fmt.Println(matriks[1][0])   -> 3",
                    "",
                    "Kurawal dobel di situ bukan sintaks khusus. Di dalam []T{...}, nama",
                    "tipe elemennya boleh dihilangkan. Jadi baris tadi cuma bentuk pendek",
                    "dari:",
                    "  matriks := [][]int{[]int{1, 2}, []int{3, 4}}",
                    "",
                    "Aturan yang sama nanti membuat []Siswa{{Nama: \"Andi\"}} di materi",
                    "Struct & Method bisa ditulis tanpa mengulang kata Siswa di tiap",
                    "barisnya.",
                ]
            },
        ],
    },
    {
        "title": "9. String, Rune & Package strings",
        "sections": [
            {
                "body": [
                    "Di Go, string itu deretan byte yang isinya nggak bisa diubah. Byte itu",
                    "satuan data terkecil yang biasa dipakai komputer, isinya angka 0",
                    "sampai 255. Jadi string bukan daftar huruf. Kedengarannya teknis, tapi",
                    "akibatnya langsung kerasa:",
                    "",
                    "  s := \"café\"",
                    "  len(s)      -> 5, bukan 4",
                    "  s[0]        -> 99, bukan \"c\"",
                    "  s[0] = 'x'  -> tidak dikompilasi sama sekali",
                    "",
                    "Kok 5? Go menyimpan teks dalam UTF-8. Di UTF-8, huruf a sampai z",
                    "makan 1 byte, é makan 2 byte, dan emoji bisa makan 4 byte. len()",
                    "menghitung byte, bukan huruf.",
                    "",
                    "s[0] jadi angka karena mengindeks string menghasilkan satu byte (alias",
                    "uint8), dan fmt mencetak tipe angka sebagai angka. Bungkus pakai",
                    "string(...) supaya hurufnya kelihatan.",
                    "",
                    "s[0] = 'x' ditolak karena string di Go immutable, artinya isinya nggak",
                    "pernah berubah. Semua fungsi yang kelihatannya mengubah string",
                    "sebetulnya mengembalikan string baru. String yang lama tetap utuh. Kalau",
                    "hasilnya nggak kamu tampung, hasil itu hilang.",
                    "",
                    "Untuk bekerja per karakter, Go punya tipe rune (alias int32). Satu rune",
                    "menyimpan satu kode Unicode, yaitu nomor sebuah karakter. Ubah dulu",
                    "string-nya jadi []rune, baru kamu bisa mengindeks dan memotong dengan",
                    "aman.",
                    "",
                    "  Tipe    Isinya                        Didapat dari",
                    "  byte    satu byte mentah, 0-255       s[i] atau []byte(s)",
                    "  rune    satu karakter Unicode         []rune(s) atau for range",
                    "",
                    "Di Materi 7 udah disebut bahwa for range pada string memberi posisi",
                    "byte dan rune. Sekarang alasannya kelihatan: angka pertamanya itu",
                    "jumlah byte yang udah dilewati, bukan nomor urut karakter. Makanya",
                    "angkanya melompat di huruf beraksen.",
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
                    "Perhatikan dua hal di akhir keluarannya.",
                    "",
                    "  - kata[:4] mencetak caf lalu satu karakter rusak. Potongannya",
                    "    membelah é jadi separuh, dan separuh byte itu bukan huruf apa pun.",
                    "  - for range cuma berputar 4 kali untuk 5 byte: i=0, 1, 2, 3, lalu",
                    "    selesai. é mulai di byte 3 dan dibaca sekali sebagai satu rune,",
                    "    jadi byte 4 nggak pernah muncul sebagai i.",
                    "",
                    "Aturan praktisnya: potong per byte cuma kalau kamu yakin isinya ASCII",
                    "(huruf Inggris biasa, angka, dan tanda baca dasar). Selain itu, ubah",
                    "dulu jadi []rune.",
                    "",
                    "Kenapa lewat package, kok bukan method?",
                    "",
                    "Orang yang datang dari Python atau Java biasanya langsung ngetik:",
                    "",
                    "  nama.split(\",\")       Python",
                    "  nama.toUpperCase()    Java",
                    "",
                    "Di Go dua-duanya nggak ada. string itu tipe bawaan, dan tipe bawaan",
                    "nggak punya method. Semua operasi teks ada di package strings, dengan",
                    "teksnya sebagai argumen pertama:",
                    "",
                    "  strings.Split(nama, \",\")",
                    "  strings.ToUpper(nama)",
                    "",
                    "Jangan lupa import \"strings\". Di Go, lupa import itu error kompilasi,",
                    "bukan peringatan.",
                    "",
                    "Isi package strings yang sering dipakai sehari-hari:",
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
                    "    Index(s, sub)         posisi BYTE kemunculan pertama,",
                    "                          -1 kalau tidak ada",
                    "    Count(s, sub)         berapa kali muncul",
                    "    EqualFold(a, b)       sama, tanpa peduli huruf besar-kecil",
                    "  Mengubah, dan semuanya menghasilkan string BARU",
                    "    ToUpper(s) / ToLower(s)",
                    "    Replace(s, lama, baru, n) / ReplaceAll(s, lama, baru)",
                    "    TrimSpace(s)          buang spasi, tab, dan enter di kedua ujung",
                    "    Repeat(s, n)          ulang n kali, enak untuk garis pemisah",
                    "",
                    "Untuk membuang sesuatu di ujung teks ada enam bentuk Trim. Yang",
                    "membedakan mereka nggak cuma sisi mana yang dibuang:",
                    "    TrimSpace(s)            buang spasi/tab/enter di KEDUA ujung",
                    "    Trim(s, cutset)         buang karakter cutset di kedua ujung",
                    "    TrimLeft(s, cutset)     ...cuma di ujung kiri",
                    "    TrimRight(s, cutset)    ...cuma di ujung kanan",
                    "    TrimPrefix(s, awalan)   buang AWALAN itu persis, sekali",
                    "    TrimSuffix(s, akhiran)  buang AKHIRAN itu persis, sekali",
                    "",
                    "Jebakan: cutset itu kumpulan huruf, bukan potongan teks. Trim,",
                    "TrimLeft, dan TrimRight membaca argumen keduanya huruf per huruf. Lalu",
                    "huruf mana pun yang ada di kumpulan itu dibuang, berulang-ulang, sampai",
                    "ketemu huruf yang bukan anggotanya. TrimPrefix dan TrimSuffix membaca",
                    "argumennya sebagai satu potongan utuh, dan cuma membuangnya sekali.",
                    "",
                    "Bedanya baru kelihatan kalau datanya kebetulan pas:",
                    "  TrimRight (\"laporan.csv\", \".csv\")  -> \"laporan\"   kelihatan benar",
                    "  TrimRight (\"kasus.csv\",   \".csv\")  -> \"kasu\"      huruf s ikut termakan",
                    "  TrimSuffix(\"kasus.csv\",   \".csv\")  -> \"kasus\"     yang ini yang dimaksud",
                    "",
                    "Kalau yang mau dibuang itu sebuah akhiran, pakai TrimSuffix. TrimRight",
                    "dengan \".csv\" bakal terus menggerogoti selama hurufnya masih c, s, v,",
                    "atau titik, dan berhentinya beda-beda untuk tiap nama berkas.",
                    "",
                    "TrimRight justru pas kalau yang dibuang memang sekumpulan huruf yang",
                    "boleh berulang. Misalnya baris baru di ekor berkas, yang bisa satu,",
                    "bisa beberapa:",
                    "  strings.TrimRight(isi, \"\\n\")",
                    "TrimSuffix di situ cuma membuang satu, dan menyisakan baris kosong",
                    "kalau berkasnya diakhiri dua enter.",
                    "",
                    "Ada dua nama di program berikut yang perlu dijelaskan sendiri.",
                    "",
                    "strings.Builder dipakai untuk merangkai teks di dalam loop. Karena",
                    "string nggak bisa diubah, s += x selalu menghasilkan string baru, dan",
                    "seluruh isi lama disalin ulang di setiap putaran. Untuk 10 potong nggak",
                    "kerasa. Untuk 100.000 potong, programnya jadi lambat banget. Builder",
                    "menumpuk potongannya di satu penampung (buffer), lalu menjadikannya",
                    "string sekali aja di akhir:",
                    "",
                    "    var b strings.Builder",
                    "    for _, x := range daftar {",
                    "        b.WriteString(x)",
                    "    }",
                    "    hasil := b.String()",
                    "",
                    "b nggak perlu diisi apa-apa sebelum dipakai. Zero value-nya udah siap",
                    "kerja.",
                    "",
                    "strings.NewReader mengubah sebuah string jadi sumber bacaan",
                    "(io.Reader). Fungsi yang biasanya membaca dari berkas jadi bisa dikasih",
                    "string biasa, tanpa menyentuh disk. Ini yang bikin kode pembaca berkas",
                    "gampang diuji. io.Reader sendiri dibahas lengkap di materi Berkas.",
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
                    "Sampai sini semua string ditulis pakai tanda kutip ganda. Go punya",
                    "bentuk kedua: backtick, yaitu tombol di kiri angka 1. Aturannya cuma",
                    "satu, dan kebalikan dari kutip ganda:",
                    "",
                    "  Di dalam backtick TIDAK ADA escape. Apa yang ditulis, itu yang tersimpan.",
                    "",
                    "Escape itu kode berawalan backslash seperti \\n untuk pindah baris.",
                    "Akibat aturan tadi ada dua:",
                    "  - \\n di dalam backtick artinya dua karakter, yaitu backslash dan",
                    "    huruf n. Nggak pindah baris.",
                    "  - Baris baru sungguhan boleh diketik apa adanya, jadi teks yang",
                    "    banyak barisnya nggak perlu disambung pakai tanda tambah.",
                    "",
                    "Di kode nyata, backtick paling sering dipakai untuk:",
                    "  - Teks banyak baris: pesan bantuan, banner, template.",
                    "  - Contoh JSON, karena nggak perlu satu pun \\\" di dalamnya.",
                    "  - Query SQL yang panjang.",
                    "  - Pola regexp: `\\d{4}` jauh lebih gampang dibaca daripada \"\\\\d{4}\".",
                    "  - Struct tag seperti `json:\"nama\"`, yang dipakai di materi JSON.",
                    "",
                    "Satu-satunya yang nggak bisa dimasukkan ke dalamnya adalah backtick",
                    "itu sendiri.",
                    "",
                    "Membandingkan string:",
                    "  - == membandingkan isinya, bukan alamatnya. Di Go nggak ada .equals()",
                    "    seperti di Java.",
                    "  - < dan > membandingkan urutan kamus menurut nilai byte. Jadi",
                    "    \"Zebra\" < \"apel\" hasilnya true, karena huruf besar punya kode lebih",
                    "    kecil daripada huruf kecil.",
                    "  - EqualFold dipakai kalau besar-kecilnya huruf nggak boleh",
                    "    berpengaruh.",
                    "",
                    "Jebakan yang paling sering kena:",
                    "  1. strings.ToUpper(s) nggak mengubah s. Tampung hasilnya:",
                    "     s = strings.ToUpper(s).",
                    "  2. Split(\"a,,b\", \",\") menghasilkan 3 potong, salah satunya kosong.",
                    "     Fields menghasilkan 2. Untuk memecah kalimat pakai Fields, untuk",
                    "     CSV pakai Split.",
                    "  3. Split(\"\", \",\") menghasilkan satu potong berisi string kosong,",
                    "     bukan slice kosong. len()-nya 1, jadi jangan dipakai untuk",
                    "     mendeteksi masukan kosong.",
                    "  4. Index mengembalikan posisi byte. Jangan dianggap nomor urut",
                    "     karakter.",
                    "  5. len(s) bukan jumlah huruf. Untuk menghitung huruf, pakai",
                    "     utf8.RuneCountInString(s).",
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
                    "Map menyimpan pasangan kunci dan nilai. Bayangkan buku telepon: kamu",
                    "cari namanya (kunci), dapat nomornya (nilai). Mirip dictionary di",
                    "Python atau HashMap di Java.",
                    "",
                    "Cara membuat map:",
                    "  var m map[string]int          nil, BELUM bisa diisi",
                    "  m := make(map[string]int)     siap dipakai",
                    "  m := map[string]int{          langsung dengan isi",
                    "      \"andi\": 25,",
                    "      \"budi\": 30,",
                    "  }",
                    "",
                    "Jebakan: menulis ke map nil bikin panic, yaitu program berhenti",
                    "mendadak.",
                    "  var m map[string]int",
                    "  m[\"a\"] = 1        PANIC saat dijalankan",
                    "Selalu buat map pakai make() atau langsung dengan isinya.",
                    "",
                    "Operasi dasar:",
                    "  m[\"citra\"] = 28       tambah atau ubah",
                    "  nilai := m[\"andi\"]    baca",
                    "  delete(m, \"budi\")     hapus",
                    "  len(m)                jumlah pasangan",
                    "",
                    "Kalau kuncinya nggak ada, membaca map menghasilkan zero value, dan",
                    "nggak ada error. Untuk map[string]int hasilnya 0.",
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
                    "Untuk mengecek apakah sebuah kunci ada, pakai pola comma ok:",
                    "",
                    "  nilai, ada := m[\"kunci\"]",
                    "",
                    "  nilai -> isinya, atau zero value kalau tidak ada",
                    "  ada   -> true kalau kunci memang ada",
                    "",
                    "Pola ini perlu karena kunci yang nggak ada menghasilkan 0, sama",
                    "persis dengan kunci yang memang bernilai 0. Tanpa ada, kamu nggak bisa",
                    "membedakan keduanya.",
                    "",
                    "  skor := map[string]int{\"andi\": 0}",
                    "  skor[\"andi\"]  -> 0  (ada, nilainya nol)",
                    "  skor[\"budi\"]  -> 0  (tidak ada sama sekali)",
                    "",
                    "Aturan lain soal map:",
                    "  - Kuncinya harus tipe yang bisa dibandingkan: string, angka, bool,",
                    "    atau struct sederhana. Slice dan map nggak bisa jadi kunci.",
                    "  - Nilainya boleh tipe apa aja, termasuk slice atau struct.",
                    "  - Map dikirim ke fungsi sebagai referensi. Kalau map diubah di",
                    "    dalam fungsi, map aslinya ikut berubah.",
                    "  - Urutan penelusuran map selalu acak. Ini sengaja, supaya",
                    "    programmer nggak bergantung pada urutan itu tanpa sadar.",
                    "",
                    "Map yang nilainya slice:",
                    "  kelompok := map[string][]string{}",
                    "  kelompok[\"A\"] = append(kelompok[\"A\"], \"andi\")",
                    "Ini aman walaupun kunci \"A\" belum ada, karena append ke slice nil",
                    "tetap jalan.",
                    "",
                    "Himpunan (set) pakai map",
                    "",
                    "Go nggak punya tipe himpunan, yaitu kumpulan nilai tanpa duplikat. Di",
                    "kode nyata, orang pakai map yang nilainya sengaja nggak dipakai:",
                    "",
                    "  ada := map[string]struct{}{}",
                    "  ada[\"andi\"] = struct{}{}",
                    "  if _, ok := ada[\"andi\"]; ok { fmt.Println(\"terdaftar\") }",
                    "",
                    "struct{}{} kelihatan kayak salah ketik, tapi cara bacanya begini:",
                    "struct{} adalah tipe struct tanpa field, lalu pasangan kurawal kedua",
                    "membuat nilai dari tipe itu. Tipe tanpa field makan nol byte, jadi yang",
                    "tersimpan di map cuma kuncinya.",
                    "",
                    "Pilihan lainnya map[string]bool. Ini lebih enak dibaca, karena",
                    "ada[\"andi\"] langsung bernilai true atau false tanpa comma ok. Ongkosnya",
                    "satu byte per kunci. Untuk data biasa, pilih yang mana aja. Dua-duanya",
                    "sama-sama sering dipakai.",
                ]
            },
        ],
    },
    {
        "title": "11. Fungsi",
        "sections": [
            {
                "body": [
                    "Fungsi itu sekumpulan kode yang dikasih nama, supaya bisa dipanggil",
                    "berkali-kali. Bentuk dasarnya:",
                    "",
                    "  func namaFungsi(param1 tipe1, param2 tipe2) tipeHasil {",
                    "      return nilai",
                    "  }",
                    "",
                    "Perhatikan: di Go, tipe ditulis sesudah nama parameter. Di C dan Java",
                    "kebalikannya.",
                    "  func tambah(a int, b int) int      Go",
                    "  int tambah(int a, int b)           C/Java",
                    "",
                    "Kalau beberapa parameter berurutan tipenya sama, boleh disingkat:",
                    "  func tambah(a, b int) int",
                    "",
                    "Fitur khas Go: fungsi bisa mengembalikan banyak nilai sekaligus.",
                    "  func bagi(a, b float64) (float64, error) {",
                    "      if b == 0 {",
                    "          return 0, errors.New(\"pembagi nol\")",
                    "      }",
                    "      return a / b, nil",
                    "  }",
                    "",
                    "Cara Go menangani error dibangun di atas fitur ini. Go nggak punya",
                    "exception. Error dikembalikan sebagai nilai biasa, di samping hasilnya.",
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
                    "Beberapa hal penting soal fungsi di Go:",
                    "",
                    "  1. Named return values, yaitu nilai kembalian yang dikasih nama.",
                    "       func f() (total int, err error) {",
                    "     Variabel total dan err otomatis dibuat. return tanpa isi bakal",
                    "     mengembalikan nilai keduanya saat itu. Nama ini berguna sebagai",
                    "     keterangan, tapi jangan dipakai di fungsi yang panjang, karena",
                    "     pembacanya jadi susah ngikutin nilainya.",
                    "",
                    "  2. Variadic, yaitu fungsi yang menerima jumlah argumen bebas,",
                    "     ditulis pakai ...",
                    "       func f(angka ...int)",
                    "     Di dalam fungsi, angka itu []int biasa. Untuk mengirim slice yang",
                    "     udah ada, tulis f(slice...).",
                    "",
                    "  3. Fungsi adalah nilai, istilahnya first-class. Fungsi bisa disimpan",
                    "     di variabel, dikirim sebagai argumen, dan dikembalikan dari fungsi",
                    "     lain.",
                    "",
                    "  4. Closure, yaitu fungsi yang ingat variabel di luarnya.",
                    "",
                    "       func penghitung() func() int {",
                    "           n := 0",
                    "           return func() int {",
                    "               n++",
                    "               return n",
                    "           }",
                    "       }",
                    "       c := penghitung()",
                    "       c()  -> 1",
                    "       c()  -> 2",
                    "",
                    "     Fungsi tanpa nama seperti itu juga bisa langsung dipanggil di",
                    "     tempat. Caranya, tempelkan sepasang kurung kosong di ujungnya:",
                    "",
                    "       func() {",
                    "           fmt.Println(\"jalan sekarang juga\")",
                    "       }()",
                    "",
                    "     Kurung terakhir itu yang memanggilnya. Tanpa kurung itu, yang kamu",
                    "     tulis cuma sebuah nilai fungsi yang nggak pernah jalan. Bentuk ini",
                    "     yang bikin defer func() { ... }() di materi Error Handling dan",
                    "     go func() { ... }() di materi Goroutine bisa bekerja.",
                    "",
                    "  5. defer menunda sebuah perintah sampai fungsinya selesai:",
                    "       f, err := os.Open(\"data.txt\")",
                    "       if err != nil {",
                    "           return err",
                    "       }",
                    "       defer f.Close()",
                    "     Baris Close dijamin jalan, walaupun di tengah jalan terjadi",
                    "     error. Kalau ada beberapa defer, urutan jalannya terbalik: yang",
                    "     terakhir didaftarkan jalan duluan.",
                    "",
                    "     Error-nya wajib diperiksa dulu. Kalau os.Open gagal, f bernilai",
                    "     nil, dan f.Close() malah bikin panic. Membuka berkas dibahas",
                    "     lengkap di materi Berkas.",
                    "",
                    "     Dua hal soal defer yang sering menjebak:",
                    "       - Argumennya dihitung waktu defer didaftarkan, bukan waktu",
                    "         dijalankan:",
                    "           i := 1",
                    "           defer fmt.Println(i)   mencetak 1, bukan 2",
                    "           i = 2",
                    "       - defer di dalam loop nggak jalan di akhir tiap putaran.",
                    "         Dia numpuk sampai seluruh fungsinya selesai. Membuka seribu",
                    "         berkas di dalam loop dengan defer f.Close() artinya seribu",
                    "         berkas terbuka bersamaan. Pindahkan isi loop ke fungsi",
                    "         tersendiri, supaya defer-nya selesai di tiap putaran.",
                    "",
                    "  6. Nama yang diawali huruf besar itu publik, artinya bisa dipakai",
                    "     dari package lain. Nama yang diawali huruf kecil itu privat. Go",
                    "     nggak punya kata kunci public dan private. Aturan huruf ini yang",
                    "     menggantikannya.",
                ]
            },
        ],
    },
    {
        "title": "12. Pointer",
        "sections": [
            {
                "body": [
                    "Pointer menyimpan alamat sebuah nilai di memori, bukan nilainya.",
                    "Bayangkan kertas berisi alamat rumah. Kertas itu cuma nunjukin letak",
                    "rumahnya. Dengan alamat itu, kamu bisa datang dan mengubah isi",
                    "rumahnya.",
                    "",
                    "Ada dua operator utama:",
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
                    "Untuk apa pointer? Go selalu mengirim argumen ke fungsi sebagai",
                    "salinan. Jadi kalau sebuah fungsi harus mengubah variabel aslinya,",
                    "fungsi itu harus menerima pointer.",
                    "",
                    "Nilai bawaan pointer adalah nil. Mengakses *p waktu p bernilai nil",
                    "bikin panic.",
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
                    "Kapan pakai pointer:",
                    "  1. Fungsi perlu mengubah argumen aslinya.",
                    "  2. Struct-nya besar, jadi menyalinnya boros memori.",
                    "  3. Kamu perlu membedakan \"nggak ada nilai\" (nil) dari \"nilainya",
                    "     nol\".",
                    "  4. Method perlu mengubah isi struct penerimanya.",
                    "",
                    "Kapan nggak perlu:",
                    "  1. Slice, map, dan channel udah berperilaku seperti referensi.",
                    "     Mengubah isinya di dalam fungsi udah kelihatan dari luar, tanpa",
                    "     pointer.",
                    "  2. Tipe kecil seperti int, bool, atau struct 1-2 field yang nggak",
                    "     perlu diubah.",
                    "",
                    "Pointer di Go lebih aman daripada di C:",
                    "  - Nggak ada aritmatika pointer. Kamu nggak bisa nulis p++ untuk",
                    "    pindah ke alamat sebelahnya. Dengan begitu, satu jenis bug yang",
                    "    terkenal di C, buffer overflow lewat pointer, nggak bisa terjadi.",
                    "  - Garbage collector yang membereskan memori. Nggak ada malloc dan",
                    "    free.",
                    "  - Mengembalikan pointer ke variabel lokal itu aman:",
                    "",
                    "      func buat() *int {",
                    "          n := 5",
                    "          return &n     aman di Go, bug di C",
                    "      }",
                    "",
                    "    Compiler otomatis memindahkan n ke heap, yaitu bagian memori yang",
                    "    tetap hidup sesudah fungsinya selesai. Perilaku ini disebut escape",
                    "    analysis.",
                ]
            },
        ],
    },
    {
        "title": "13. Struct & Method",
        "sections": [
            {
                "body": [
                    "Struct mengelompokkan beberapa data jadi satu tipe baru. Misalnya data",
                    "seorang siswa: nama, umur, dan nilai, disimpan sebagai satu kesatuan.",
                    "Go nggak punya class. Penggantinya ya struct ini.",
                    "",
                    "  type Siswa struct {",
                    "      Nama  string",
                    "      Umur  int",
                    "      Nilai float64",
                    "  }",
                    "",
                    "Tiap isian di dalam struct disebut field. Cara membuat nilai dari",
                    "struct, istilahnya instance:",
                    "  s := Siswa{Nama: \"Andi\", Umur: 20, Nilai: 85.5}",
                    "  s := Siswa{\"Andi\", 20, 85.5}   urutan harus persis",
                    "  var s Siswa                     semua field zero value",
                    "  p := &Siswa{Nama: \"Budi\"}       pointer ke struct",
                    "",
                    "Bentuk yang menyebut nama field lebih disukai. Kodenya tetap benar",
                    "walaupun nanti urutan field-nya berubah.",
                    "",
                    "Field diakses pakai titik:",
                    "  s.Nama = \"Citra\"",
                    "  fmt.Println(s.Umur)",
                    "",
                    "Lewat pointer juga cukup pakai titik. Go otomatis mengambil nilai yang",
                    "ditunjuk pointer itu (istilahnya dereference):",
                    "  p.Nama = \"Dedi\"     tidak perlu (*p).Nama",
                    "",
                    "Struct anonim",
                    "",
                    "Tipe struct boleh ditulis langsung di tempat, tanpa type dan tanpa",
                    "nama, kalau memang cuma dipakai sekali:",
                    "",
                    "  kasus := []struct {",
                    "      nama string",
                    "      a, b int",
                    "  }{",
                    "      {\"positif\", 2, 3},",
                    "      {\"negatif\", -2, -3},",
                    "  }",
                    "",
                    "Bagian }{ yang kelihatan aneh itu sebetulnya dua hal yang",
                    "bersebelahan. Kurawal pertama menutup definisi tipenya, kurawal kedua",
                    "membuka nilainya. Sama seperti []int{1, 2}, cuma nama tipenya diganti",
                    "seluruh definisi struct.",
                    "",
                    "Ingat istilahnya: struct anonim. Bentuk ini dipakai table-driven test",
                    "di materi Package, Module & Testing dan di Studi Kasus. Kalau kamu tahu",
                    "namanya, kamu bisa mencarinya sendiri di dokumentasi.",
                    "",
                    "Membandingkan dua struct",
                    "",
                    "Dua struct bisa dibandingkan pakai == asal semua field-nya bisa",
                    "dibandingkan: angka, string, bool, pointer, dan struct sejenis.",
                    "  Siswa{\"Andi\", 20, 85.5} == Siswa{\"Andi\", 20, 85.5}  true",
                    "Kalau ada satu aja field bertipe slice, map, atau func, compiler",
                    "menolak ==.",
                    "",
                    "Karena itu juga, struct yang semua field-nya bisa dibandingkan boleh",
                    "dipakai sebagai kunci map. Ini melengkapi aturan kunci map di materi",
                    "Map:",
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
                    "Value receiver dan pointer receiver",
                    "",
                    "Method itu fungsi yang nempel ke sebuah tipe. Receiver adalah bagian",
                    "di depan nama method yang nunjukin method itu milik tipe apa. Bagian",
                    "ini yang paling sering bikin pemula bingung.",
                    "",
                    "  func (s Siswa) Baca() string      value receiver",
                    "    - s adalah salinan struct-nya.",
                    "    - Mengubah s nggak memengaruhi struct aslinya.",
                    "    - Pakai untuk method yang cuma membaca data.",
                    "",
                    "  func (s *Siswa) Ubah()            pointer receiver",
                    "    - s menunjuk ke struct yang asli.",
                    "    - Perubahan pada s kelihatan dari luar.",
                    "    - Pakai untuk method yang mengubah data.",
                    "    - Juga dipakai kalau struct-nya besar.",
                    "",
                    "Aturan praktisnya: kalau ada satu aja method yang butuh pointer",
                    "receiver, bikin semua method tipe itu pakai pointer receiver. Kalau",
                    "dicampur, kamu harus terus ingat method mana yang mengubah data dan",
                    "mana yang nggak.",
                    "",
                    "Kabar baiknya, waktu memanggil method, Go menyesuaikan sendiri:",
                    "  a := Siswa{}",
                    "  a.NaikkanNilai(5)     Go otomatis jadi (&a).NaikkanNilai(5)",
                    "",
                    "Embedding: cara Go menggantikan pewarisan",
                    "",
                    "Pewarisan (inheritance) di bahasa lain artinya sebuah class mendapat",
                    "isi class lain. Go nggak punya itu. Gantinya, sebuah struct bisa",
                    "disematkan ke struct lain:",
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
                    "Karyawan ikut mendapat field dan method dari Orang. Go menyebut ini",
                    "komposisi, bukan pewarisan. Bedanya, nggak ada hierarki tipe. Struct",
                    "yang satu cuma digabung ke struct yang lain.",
                ]
            },
        ],
    },
    {
        "title": "14. Interface",
        "sections": [
            {
                "body": [
                    "Interface itu daftar method yang harus dimiliki sebuah tipe.",
                    "Interface nggak berisi data apa pun.",
                    "",
                    "  type Bentuk interface {",
                    "      Luas() float64",
                    "      Keliling() float64",
                    "  }",
                    "",
                    "Setiap tipe yang punya kedua method itu otomatis memenuhi interface",
                    "Bentuk. Kamu nggak perlu nulis implements seperti di Java.",
                    "",
                    "Cara ini disebut implicit implementation, atau duck typing statis.",
                    "Patokannya: kalau bersuara seperti bebek, ya dia bebek. Kalau sebuah",
                    "tipe punya method yang diminta, tipe itu dianggap memenuhi",
                    "interface-nya.",
                    "",
                    "Untungnya, kamu bisa bikin interface untuk tipe yang udah ada, bahkan",
                    "tipe dari library orang lain, tanpa mengubah kode tipe itu.",
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
                    "Prinsip-prinsip interface di Go:",
                    "",
                    "  1. Bikin interface sekecil mungkin. Ada pepatah di komunitas Go:",
                    "     \"The bigger the interface, the weaker the abstraction.\" Artinya,",
                    "     makin banyak method yang diminta, makin sedikit tipe yang bisa",
                    "     memenuhinya. Banyak interface standar cuma punya satu method:",
                    "",
                    "       type Stringer interface { String() string }",
                    "       type Error interface { Error() string }",
                    "       type Reader interface { Read(p []byte) (int, error) }",
                    "       type Writer interface { Write(p []byte) (int, error) }",
                    "",
                    "  2. Interface ditulis di sisi pemakai, bukan di sisi pembuat tipe.",
                    "     Ini kebalikan dari Java.",
                    "",
                    "  3. Pasang method String() supaya tipemu tampil rapi waktu dicetak.",
                    "     Tipe yang punya method ini memenuhi interface Stringer:",
                    "",
                    "       func (s Siswa) String() string {",
                    "           return s.Nama",
                    "       }",
                    "       fmt.Println(siswa)   -> otomatis memakai String()",
                    "",
                    "  4. Type assertion, yaitu cara mengambil tipe asli dari dalam",
                    "     interface, punya dua bentuk:",
                    "       v := x.(Persegi)        panic kalau salah tipe",
                    "       v, ok := x.(Persegi)    aman, ok bernilai false",
                    "     Selalu pakai bentuk kedua, kecuali kamu yakin betul tipenya.",
                    "",
                    "  5. Interface nil punya jebakan yang terkenal. Sebuah interface baru",
                    "     bernilai nil kalau tipe dan nilainya sama-sama nil. Pointer nil",
                    "     yang disimpan di interface bikin interface itu nggak nil lagi.",
                    "     Makanya, fungsi yang mengembalikan error sebaiknya ditulis",
                    "     dengan tipe kembalian error, jangan pointer ke tipe error",
                    "     buatanmu sendiri.",
                    "",
                    "  6. Method set: pointer receiver nggak ikut ke nilai biasa. Di materi",
                    "     Struct & Method kamu udah lihat Go otomatis mengubah a.Ubah() jadi",
                    "     (&a).Ubah(). Untuk urusan memenuhi interface, kemudahan itu nggak",
                    "     berlaku. Aturannya:",
                    "",
                    "       receiver Persegi   dimiliki Persegi DAN *Persegi",
                    "       receiver *Persegi  dimiliki *Persegi SAJA",
                    "",
                    "     Jadi kalau Luas() ditulis dengan pointer receiver,",
                    "     func (p *Persegi) Luas() float64, maka Persegi{Sisi: 4} di daftar",
                    "     []Bentuk pada kode di atas nggak memenuhi Bentuk lagi. Compiler",
                    "     bilang begini:",
                    "",
                    "       cannot use Persegi{…} (value of type Persegi) as",
                    "       Bentuk value in array or slice literal: Persegi does",
                    "       not implement Bentuk (method Luas has pointer receiver)",
                    "",
                    "     Bagian tengah pesannya tergantung tempat kejadiannya: in array or",
                    "     slice literal di sini, in variable declaration kalau ditaruh di",
                    "     var, in argument to laporkan kalau dikirim ke fungsi. Yang selalu",
                    "     sama, dan yang perlu kamu kenali, adalah ujungnya: method Luas",
                    "     has pointer receiver.",
                    "",
                    "     Obatnya cukup satu tanda: tulis &Persegi{Sisi: 4}.",
                    "",
                    "     Kamu juga bisa memasang pemeriksa waktu kompilasi di berkas",
                    "     tipenya. Dengan begitu kesalahannya ketahuan di situ, nggak jauh",
                    "     di tempat tipe itu dipakai:",
                    "       var _ Bentuk = (*Persegi)(nil)",
                    "     Baris itu nggak menyimpan apa pun, karena _ membuang nilainya.",
                    "     Tapi baris itu memaksa compiler mengecek bahwa *Persegi memang",
                    "     memenuhi Bentuk.",
                    "",
                    "     Aturan ini juga alasan materi Error Handling mengembalikan",
                    "     &ErrValidasi{...} dengan tanda &, dan memeriksanya lewat",
                    "     var ev *ErrValidasi. Method Error() di sana pakai pointer",
                    "     receiver, jadi yang memenuhi interface error adalah *ErrValidasi,",
                    "     bukan ErrValidasi.",
                ]
            },
        ],
    },
    {
        "title": "15. Tipe Bentukan, Konstanta Berkelompok & iota",
        "sections": [
            {
                "body": [
                    "Sampai materi ini, setiap type yang kamu tulis selalu struct atau",
                    "interface. Padahal bentuk type yang paling ringkas justru begini:",
                    "",
                    "  type Celsius float64",
                    "  type Status int",
                    "  type KodePos string",
                    "  type Daftar []string",
                    "  type Validator func(string) error",
                    "",
                    "Artinya: bikin tipe baru yang isinya sama persis dengan tipe di",
                    "kanannya. Tipe di kanan itu disebut tipe dasar (underlying type). Tipe",
                    "barunya disebut tipe bentukan (defined type).",
                    "",
                    "Buat apa? Di mata compiler, tipe baru itu beda dari tipe dasarnya:",
                    "",
                    "  var c Celsius = 10",
                    "  var f float64 = c",
                    "  ERROR: cannot use c (variable of type Celsius) as float64 value",
                    "",
                    "  var f float64 = float64(c)   BENAR",
                    "",
                    "Dua tipe bentukan yang tipe dasarnya sama pun tetap nggak bisa",
                    "dicampur:",
                    "",
                    "  c + Fahrenheit(1)",
                    "  ERROR: invalid operation: mismatched types Celsius and Fahrenheit",
                    "",
                    "Di situ gunanya. Detik dan meter sama-sama float64. Begitu dua-duanya",
                    "jadi tipe sendiri, kamu nggak bisa lagi menjumlahkan detik dengan",
                    "meter tanpa sadar. Aturan \"konversi harus ditulis sendiri\" dari Materi",
                    "2 jadinya membantumu, nggak cuma bikin repot.",
                    "",
                    "Bonus terbesarnya: method boleh dipasang ke tipe apa pun yang dibuat",
                    "di package yang sama, nggak cuma ke struct.",
                    "",
                    "  func (c Celsius) String() string { ... }",
                    "",
                    "Ini menjawab pertanyaan yang sering muncul waktu membaca kode orang:",
                    "kok sebuah int, string, atau slice bisa punya method?",
                    "",
                    "Larangannya cuma satu: kamu nggak boleh memasang method ke tipe milik",
                    "package lain, termasuk ke float64 atau string polos. Bungkus dulu jadi",
                    "tipe bentukan sendiri, baru pasang method-nya.",
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
                    "Konstanta boleh dikelompokkan dalam satu blok, sama seperti",
                    "var ( ... ) yang udah kamu pakai di Materi 2:",
                    "",
                    "  const (",
                    "      Merah = \"merah\"",
                    "      Hijau = \"hijau\"",
                    "  )",
                    "",
                    "iota adalah penghitung yang hidup di dalam blok const:",
                    "  - Nilainya 0 di baris deklarasi pertama blok itu.",
                    "  - Naik satu di tiap baris deklarasi berikutnya.",
                    "  - Baris kosong dan baris komentar nggak ikut dihitung.",
                    "  - Balik ke 0 di setiap blok const yang baru.",
                    "",
                    "Ada satu aturan lagi yang bikin semuanya masuk akal: baris tanpa tanda",
                    "sama dengan mengulang ekspresi di baris sebelumnya.",
                    "",
                    "  const (",
                    "      Draf     Status = iota   ditulis lengkap        -> 0",
                    "      Menunggu                 diam-diam sama         -> 1",
                    "      Aktif                    diam-diam sama         -> 2",
                    "  )",
                    "",
                    "Jadi nama-nama polos tanpa nilai itu nggak ada sihirnya. Compiler",
                    "menyalin ulang ekspresi terakhir, dan yang berubah di tiap baris cuma",
                    "iota.",
                    "",
                    "Tiga variasi yang paling sering kamu temui di kode orang:",
                    "",
                    "  _      Level = iota      buang nilai 0",
                    "  Senin  Hari  = iota + 1  mulai berhitung dari 1",
                    "  Baca   Izin  = 1 << iota  1, 2, 4, 8 ... satu bit per nama",
                    "",
                    "Yang terakhir pakai operator geser dari Materi 3. Pola ini dipakai",
                    "untuk flag, yaitu pilihan yang boleh digabung: Baca|Tulis muat dalam",
                    "satu angka.",
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
                    "Enum itu tipe yang nilainya cuma boleh dari daftar tertentu, misalnya",
                    "status pesanan. Go nggak punya kata kunci enum. Polanya selalu tiga",
                    "bagian, dan kalau kurang satu, akibatnya kerasa:",
                    "  1. type Status int            supaya punya tipe sendiri",
                    "  2. blok const + iota          daftar nilainya",
                    "  3. func (s Status) String()   supaya tercetak sebagai nama",
                    "",
                    "Tanpa nomor 3, fmt.Println(status) mencetak 2, dan log-mu jadi deretan",
                    "angka yang harus ditebak artinya. String() itu Stringer dari materi",
                    "Interface. fmt memakainya sendiri tanpa diminta.",
                    "",
                    "Jebakan yang sering kena:",
                    "",
                    "  1. String() yang memanggil dirinya sendiri.",
                    "       return fmt.Sprintf(\"Status(%v)\", s)",
                    "     Hasilnya fatal error: stack overflow. %v bikin fmt memanggil",
                    "     String() lagi, terus-menerus tanpa henti. Konversi dulu ke int:",
                    "     fmt.Sprintf(\"...%d\", int(s)).",
                    "",
                    "  2. Zero value otomatis jadi nilai pertama. var s Status bernilai 0,",
                    "     dan 0 itu Draf. Struct yang lupa diisi kelihatan berstatus Draf,",
                    "     dan nggak ada yang curiga. Kalau itu berbahaya, buang 0 pakai _",
                    "     atau kasih nama khusus seperti StatusTidakDikenal.",
                    "",
                    "  3. Menyisipkan nama di tengah blok iota menggeser semua nilai di",
                    "     bawahnya. Kalau angka itu pernah tersimpan di database atau",
                    "     berkas, data lama tiba-tiba artinya lain. Tambahkan nama baru di",
                    "     paling bawah.",
                    "",
                    "  4. Tipe bentukan nggak menutup semua celah: Status(99) tetap",
                    "     dikompilasi. Enum di Go itu kesepakatan, nggak ada jaminan dari",
                    "     compiler. Nilai yang datang dari luar (input, JSON, database)",
                    "     tetap wajib kamu cek sendiri.",
                    "",
                    "  5. Tipe bentukan nggak ikut membawa method tipe dasarnya.",
                    "     type Waktu time.Time bikin semua method time.Time hilang:",
                    "       w.Year undefined (type Waktu has no field or method Year)",
                    "     Kalau maumu menambah method, sematkan struct-nya (embedding, di",
                    "     materi Struct & Method). Jangan bikin tipe bentukan.",
                    "",
                    "Konstanta tanpa tipe (untyped constant):",
                    "  const Pi = 3.14     belum bertipe -> bisa jadi float32 ATAU float64",
                    "  const Batas = 100   bisa jadi int, int64, uint8, bahkan float64",
                    "",
                    "Karena itu suhu*2 di contoh pertama sah: angka 2 menyesuaikan diri jadi",
                    "Celsius. Begitu kamu tulis const Pi float64 = 3.14, tipenya terkunci,",
                    "dan var x float32 = Pi langsung ditolak compiler.",
                    "",
                    "Sekarang dua hal yang tadinya aneh jadi masuk akal:",
                    "  - 5 * time.Second sah karena time.Duration cuma type Duration int64,",
                    "    dan 5 itu konstanta tanpa tipe. Lihat lagi materi Angka & Waktu.",
                    "  - HandlerFunc di net/http, yang ditulis",
                    "    type HandlerFunc func(ResponseWriter, *Request), juga cuma tipe",
                    "    fungsi yang dikasih nama, sama seperti Validator di contoh",
                    "    pertama.",
                ],
            },
        ],
    },
    {
        "title": "16. Error Handling",
        "sections": [
            {
                "body": [
                    "Go nggak punya exception, try, atau catch. Di Go, error itu nilai",
                    "biasa yang dikembalikan fungsi.",
                    "",
                    "  hasil, err := lakukanSesuatu()",
                    "  if err != nil {",
                    "      return err",
                    "  }",
                    "",
                    "Pola if err != nil bakal kamu tulis ribuan kali. Kesannya",
                    "bertele-tele, tapi untungnya banyak:",
                    "  - Alur error kelihatan jelas di kode, nggak tersembunyi.",
                    "  - Nggak ada lompatan mendadak ke tempat lain.",
                    "  - Kamu dipaksa memikirkan setiap kemungkinan gagal.",
                    "",
                    "error itu cuma interface sederhana:",
                    "  type error interface {",
                    "      Error() string",
                    "  }",
                    "",
                    "Cara membuat error:",
                    "  errors.New(\"pesan\")",
                    "  fmt.Errorf(\"gagal memuat %s: %w\", nama, err)",
                    "",
                    "Verb %w membungkus error asalnya, supaya nanti masih bisa diperiksa",
                    "pakai errors.Is atau errors.As.",
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
                    "Ada tiga alat untuk memeriksa error:",
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
                    "Error sentinel itu error yang disimpan di variabel, misalnya",
                    "ErrTarget, lalu dibandingkan dengan error lain untuk dikenali.",
                    "",
                    "Menggabungkan beberapa kegagalan",
                    "",
                    "Kadang satu pekerjaan gagal di lebih dari satu tempat sekaligus,",
                    "misalnya waktu memvalidasi formulir. errors.Join menyatukan semuanya",
                    "jadi satu error:",
                    "",
                    "  err := errors.Join(errNama, errUmur)",
                    "  errors.Is(err, errNama)   -> true",
                    "  errors.Is(err, errUmur)   -> true",
                    "",
                    "Error yang nil diabaikan. Kalau semuanya nil, hasilnya juga nil. Jadi",
                    "kamu aman menumpuk error satu per satu, lalu memeriksanya sekali di",
                    "akhir. Pesannya memuat tiap error di barisnya sendiri.",
                    "",
                    "fmt.Errorf juga boleh memuat lebih dari satu %w:",
                    "  fmt.Errorf(\"simpan gagal: %w, lalu %w\", errTulis, errTutup)",
                    "",
                    "panic dan recover",
                    "",
                    "panic menghentikan program seketika. Pakai panic cuma untuk kondisi",
                    "yang nggak mungkin dilanjutkan, misalnya bug programmer. Kesalahan",
                    "input dari pengguna nggak termasuk.",
                    "",
                    "  panic(\"ini seharusnya tidak pernah terjadi\")",
                    "",
                    "recover menangkap panic, tapi cuma bisa dipanggil di dalam fungsi",
                    "yang di-defer:",
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
                    "Aturan pakainya:",
                    "  - Kesalahan yang wajar terjadi (berkas nggak ada, input salah,",
                    "    koneksi putus): kembalikan error.",
                    "  - Kondisi mustahil yang menandakan bug: panic.",
                    "  - Jangan pakai panic sebagai pengganti exception.",
                    "",
                    "Jangan abaikan error pakai _ kecuali kamu tahu persis akibatnya:",
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
                    "Sampai materi ini, semua yang dihitung programmu hilang begitu",
                    "programnya berhenti. Menyimpannya ke berkas adalah cara paling",
                    "sederhana supaya hasilnya tetap ada.",
                    "",
                    "Go punya dua tingkat cara untuk pekerjaan yang sama. Salah pilih di",
                    "sini adalah kesalahan pertama yang paling sering terjadi.",
                    "",
                    "  1. Sekali jalan: seluruh isi berkas masuk ke memori sekaligus.",
                    "     Cocok untuk berkas kecil, misalnya konfigurasi, catatan, atau CSV",
                    "     pendek.",
                    "",
                    "       data, err := os.ReadFile(\"stok.txt\")          // ([]byte, error)",
                    "       err := os.WriteFile(\"stok.txt\", data, 0644)   // error",
                    "",
                    "     os.ReadFile mengembalikan []byte, bukan string. Pakai string(data)",
                    "     kalau mau memperlakukannya sebagai teks, dan []byte(teks) untuk",
                    "     arah sebaliknya waktu menulis.",
                    "",
                    "  2. Bertahap: berkas dibuka dulu, lalu dibaca atau ditulis sepotong",
                    "     demi sepotong. Cara ini wajib untuk berkas besar. os.ReadFile",
                    "     pada berkas 4 GB artinya minta memori 4 GB, dan programnya bakal",
                    "     mati sebelum sempat mengerjakan apa pun.",
                    "",
                    "Angka 0644 itu apa?",
                    "",
                    "Itu izin akses gaya Unix. Awalan 0 bikin angkanya dibaca sebagai",
                    "oktal (basis 8), jadi bukan enam ratus empat puluh empat. Boleh juga",
                    "ditulis 0o644 supaya lebih jelas. Tiga digitnya berturut-turut untuk",
                    "pemilik, grup, dan orang lain.",
                    "",
                    "  4 = boleh dibaca   2 = boleh ditulis   1 = boleh dijalankan",
                    "  6 = 4+2 = baca & tulis      7 = 4+2+1 = semuanya",
                    "",
                    "Jadi 0644 artinya pemilik boleh baca dan tulis, yang lain cuma boleh",
                    "baca. Untuk folder, pakai 0755. Tanpa bit 1, folder itu nggak bisa",
                    "dimasuki siapa pun, termasuk pemiliknya sendiri.",
                    "",
                    "Izin ini cuma dipakai waktu berkasnya baru dibuat. Kalau berkasnya",
                    "udah ada, izin lamanya dibiarkan apa adanya.",
                    "",
                    "Menambah di akhir berkas tanpa menimpa",
                    "",
                    "  f, err := os.OpenFile(nama, os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)",
                    "",
                    "Tanda | menggabungkan beberapa bendera (flag): tambah di akhir, buat",
                    "kalau belum ada, dan buka untuk menulis saja. Tanpa O_APPEND,",
                    "tulisanmu menimpa isi berkas mulai dari posisi awal.",
                    "",
                    "os.Create(nama) sama artinya dengan bendera O_RDWR|O_CREATE|O_TRUNC.",
                    "Perhatikan O_TRUNC di situ: berkas yang udah ada langsung dikosongkan.",
                    "Itu memang tugasnya, bukan bug.",
                    "",
                    "Menyusun nama berkas",
                    "",
                    "  nama := filepath.Join(\"data\", \"2024\", \"stok.txt\")",
                    "",
                    "Jangan menyambung sendiri seperti \"data/\" + sub + \"/\" + berkas.",
                    "filepath.Join memakai pemisah folder yang benar di tiap sistem",
                    "operasi, dan membereskan garis miring dobel yang nggak sengaja",
                    "tertulis.",
                ],
            },
            {
                "heading": "Satu berkas dari nol sampai dihapus",
                "body": [
                    "Contoh ini bikin foldernya sendiri, lalu menghapusnya lagi di akhir.",
                    "Jadi aman dijalankan berkali-kali.",
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
                    "Empat jebakan berkas yang paling sering kena:",
                    "",
                    "  1. Lupa memanggil scanner.Err()",
                    "     Loop for pemindai.Scan() bisa berhenti karena dua sebab:",
                    "     berkasnya habis, atau pembacaannya gagal di tengah jalan. Kalau",
                    "     kamu nggak memeriksa Err() sesudah loop, kegagalan itu kebaca",
                    "     sebagai \"udah selesai\". Programmu lalu melaporkan data setengah",
                    "     jadi sebagai data lengkap, tanpa satu pun peringatan.",
                    "",
                    "     Scanner bawaan juga menyerah pada baris yang lebih panjang dari",
                    "     64 KB. Ini penyebab \"kok datanya kepotong\" yang nggak bakal",
                    "     ketahuan kalau Err() nggak diperiksa.",
                    "",
                    "  2. Lupa Flush pada bufio.Writer",
                    "     bufio menumpuk tulisan di memori, dan baru menuliskannya ke",
                    "     berkas kalau tumpukannya penuh. Kalau program selesai tanpa",
                    "     Flush, berkasnya kosong atau terpotong, lagi-lagi tanpa satu pun",
                    "     pesan error. Jebakan ini yang paling sering bikin orang mengira",
                    "     kodenya nggak pernah jalan.",
                    "",
                    "  3. Mengabaikan error dari Close pada berkas yang ditulis",
                    "     Tulisan terakhir bisa gagal justru waktu berkasnya ditutup,",
                    "     misalnya karena disk penuh, kuota habis, atau media",
                    "     penyimpanannya dicabut. defer f.Close() yang polos membuang error",
                    "     itu tanpa kabar.",
                    "",
                    "     Cara yang benar ada di contoh kedua: dua defer. Karena defer",
                    "     dijalankan terbalik (lihat materi Fungsi), yang didaftarkan",
                    "     belakangan, yaitu Flush, jalan lebih dulu, baru Close. Kalau",
                    "     urutannya kebalik, kamu menulis ke berkas yang udah ditutup.",
                    "",
                    "     Untuk berkas yang cuma dibaca, defer f.Close() polos udah cukup.",
                    "     Nggak ada data yang bisa hilang.",
                    "",
                    "  4. Memeriksa dulu, baru membuka",
                    "     Bentuk yang salah:",
                    "       if _, err := os.Stat(nama); err == nil {",
                    "           f, _ := os.Open(nama)",
                    "       }",
                    "     Di antara dua baris itu, berkasnya bisa aja dihapus program lain.",
                    "     Langsung buka aja, lalu periksa error-nya:",
                    "       f, err := os.Open(nama)",
                    "       if errors.Is(err, os.ErrNotExist) { ... }",
                    "",
                    "     Kenapa pakai errors.Is, nggak err == os.ErrNotExist? Package os",
                    "     membungkus penyebabnya di dalam *os.PathError, supaya pesannya",
                    "     menyebut nama berkasnya. Akibatnya perbandingan == selalu false.",
                    "     Di sini kepakai errors.Is dari materi sebelumnya, untuk error",
                    "     yang nggak kamu buat sendiri.",
                    "",
                    "Fungsi berkas lain yang sering dipakai:",
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
                    "io.Reader dan io.Writer masing-masing cuma punya satu method. Kamu udah",
                    "lihat definisinya di materi Interface. Karena sekecil itu, hampir semua",
                    "hal di Go memenuhinya. Reader adalah apa pun yang bisa dibaca, Writer",
                    "adalah apa pun yang bisa ditulisi:",
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
                    "Akibatnya buat cara kamu menulis kode: tulis",
                    "func laporkan(w io.Writer, ...), jangan func laporkan(f *os.File, ...).",
                    "Ongkosnya nol huruf tambahan. Hasilnya satu fungsi yang bisa mencetak",
                    "ke layar, menyimpan ke berkas, dan mengirim ke jaringan. Yang paling",
                    "berguna, fungsi itu bisa diuji pakai bytes.Buffer tanpa menyentuh disk",
                    "sama sekali.",
                    "",
                    "Aturan yang sama berlaku untuk membaca: terima io.Reader, jangan",
                    "*os.File, supaya bisa diuji pakai strings.NewReader.",
                    "",
                    "Dua fungsi pembantu yang selalu ada:",
                    "",
                    "  data, err := io.ReadAll(r)     baca habis jadi []byte",
                    "  n, err := io.Copy(dst, src)    salin Reader mana pun ke",
                    "                                 Writer mana pun",
                    "",
                    "io.Copy menyalin sepotong demi sepotong, jadi berkas 2 GB pun nggak",
                    "perlu muat di memori. io.ReadAll kebalikannya: semuanya dimuat",
                    "sekaligus. Jadi jangan pakai io.ReadAll untuk sumber yang isinya",
                    "nggak ada habisnya.",
                    "",
                    "Stdout dan stderr",
                    "",
                    "fmt.Println menulis ke os.Stdout. Itu jalur hasil, yang biasa",
                    "disalurkan (pipe) ke program lain. Pesan kesalahan dan laporan",
                    "kemajuan harus lewat jalur lain:",
                    "",
                    "  fmt.Fprintln(os.Stderr, \"gagal membuka:\", err)",
                    "",
                    "Kalau keduanya dicampur, orang yang menjalankan",
                    "./program > hasil.txt bakal menemukan pesan error-mu ikut tersimpan",
                    "di dalam berkas hasilnya.",
                    "",
                    "Terakhir, bungkus pakai bufio kalau kamu menulis atau membaca banyak",
                    "potongan kecil. Satu Write langsung ke *os.File artinya satu panggilan",
                    "ke sistem operasi. bufio menggabungkan ribuan tulisan kecil jadi",
                    "beberapa tulisan besar. Dan sekali lagi: jangan lupa Flush.",
                ],
            },
        ],
    },
    {
        "title": "18. Program Baris Perintah: Argumen, flag & log",
        "sections": [
            {
                "body": [
                    "Di Materi 5 kamu bikin program yang nunggu ketikan lewat stdin. Alat",
                    "yang dipakai sehari-hari jarang bekerja begitu. Perintah yang kamu",
                    "ketik di terminal biasanya menerima masukannya langsung dari baris",
                    "perintah:",
                    "",
                    "  go build -o server main.go",
                    "  grep -n \"halo\" catatan.txt",
                    "",
                    "Kata-kata sesudah nama program itu disebut argumen. Di Go, semua",
                    "argumen masuk ke satu slice string bernama os.Args.",
                    "",
                    "  ./sapa Levi --keras",
                    "",
                    "  os.Args[0]    \"./sapa\"    nama/jalur programnya SENDIRI",
                    "  os.Args[1]    \"Levi\"",
                    "  os.Args[2]    \"--keras\"",
                    "  len(os.Args)  3",
                    "",
                    "Argumen yang diketik pemakai mulai dari indeks 1, bukan 0. Di sinilah",
                    "pemula biasanya ketemu panic pertamanya:",
                    "",
                    "  nama := os.Args[1]",
                    "",
                    "  panic: runtime error: index out of range [1] with length 1",
                    "",
                    "Program itu langsung mati kalau dijalankan tanpa argumen. Jadi hitung",
                    "dulu jumlahnya:",
                    "",
                    "  if len(os.Args) < 2 {",
                    "      fmt.Fprintln(os.Stderr, \"cara pakai: sapa <nama>\")",
                    "      os.Exit(1)",
                    "  }",
                    "",
                    "Ada dua hal baru di potongan itu:",
                    "",
                    "  fmt.Fprintln(os.Stderr, ...)",
                    "    Sama seperti fmt.Println, tapi tujuannya kamu tentukan sendiri.",
                    "    os.Stderr itu jalur untuk pesan yang dibaca manusia. os.Stdout",
                    "    untuk hasil, yang mungkin disalurkan (pipe) ke perintah lain.",
                    "    Alasan lengkapnya ada di bagian terakhir materi ini.",
                    "",
                    "  os.Exit(1)",
                    "    Menghentikan program saat itu juga, sambil menyerahkan satu",
                    "    angka ke shell. 0 artinya berhasil, selain 0 artinya gagal.",
                    "    Kebalikan dari dugaan kebanyakan orang, tapi angka inilah yang",
                    "    dibaca && dan || di shell, dan yang dipakai CI untuk memutuskan",
                    "    build-nya merah atau hijau. main yang selesai dengan wajar",
                    "    otomatis menyerahkan 0.",
                    "",
                    "Angka yang diserahkan os.Exit itu disebut kode keluar (exit code). CI",
                    "yang disebut di atas adalah layanan yang menjalankan build dan tes",
                    "secara otomatis tiap kali kode dikirim.",
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
                    "Jalankan dua kali supaya bedanya kerasa:",
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
                    "Perhatikan os.Args[0]. Kalau pakai go run, isinya jalur biner",
                    "sementara yang aneh, dan angkanya ganti tiap kali dijalankan. Soalnya",
                    "go run memang mengompilasi ke folder sementara dulu. Sesudah go build,",
                    "isinya jalur binermu sendiri. Jadi jangan pakai os.Args[0] sebagai",
                    "data. Gunanya cuma untuk pesan bantuan.",
                    "",
                    "Perhatikan juga \"dua kata\". Shell yang menyatukannya jadi satu",
                    "argumen, karena kamu kasih tanda kutip.",
                    "",
                    "Flag itu argumen berawalan strip yang mengatur perilaku program,",
                    "seperti --versi di atas. Kalau kamu mengurus flag sendiri, kodenya",
                    "cepat berantakan begitu flag-nya lebih dari dua. Kamu harus ngatur",
                    "urutan, nilai bawaan, bentuk --x=1, dan teks bantuan. Package flag",
                    "dari pustaka standar udah mengerjakan semuanya.",
                    "",
                    "  nama := flag.String(\"nama\", \"dunia\", \"nama yang disapa\")",
                    "  ulang := flag.Int(\"ulang\", 1, \"berapa kali dicetak\")",
                    "  keras := flag.Bool(\"keras\", false, \"pakai huruf kapital\")",
                    "  flag.Parse()",
                    "",
                    "Urutannya wajib begitu: daftarkan semua flag dulu, baru panggil",
                    "flag.Parse().",
                    "",
                    "Bagian yang paling bikin bingung: flag.String nggak mengembalikan",
                    "string. Dia mengembalikan *string, yaitu sebuah pointer (materi",
                    "Pointer).",
                    "",
                    "  fmt.Println(nama)    mencetak alamatnya: 0xc000010030",
                    "  fmt.Println(*nama)   mencetak isinya   : dunia",
                    "",
                    "Alasannya masuk akal. Waktu baris flag.String dijalankan, argumennya",
                    "belum dibaca sama sekali. Fungsi itu cuma memesan sebuah kotak kosong",
                    "lalu menyerahkan alamatnya. flag.Parse() yang nanti mengisi kotak itu.",
                    "Akibatnya, membaca *nama sebelum flag.Parse() selalu memberi nilai",
                    "bawaan, bukan yang diketik pemakai. Bug ini susah ketahuan karena",
                    "programnya tetap jalan.",
                    "",
                    "Kalau variabelnya udah ada (sering dipakai untuk mengisi field struct",
                    "konfigurasi), pakai bentuk ...Var yang tanpa pointer:",
                    "",
                    "  var nama string",
                    "  flag.StringVar(&nama, \"nama\", \"dunia\", \"nama yang disapa\")",
                    "",
                    "Ada juga IntVar, BoolVar, Float64Var, dan DurationVar.",
                    "",
                    "Argumen yang bukan flag diambil terpisah. Argumen begini disebut",
                    "argumen posisional:",
                    "  flag.Args()   []string berisi argumen posisional",
                    "  flag.NArg()   jumlahnya",
                    "  flag.Arg(0)   yang pertama",
                    "",
                    "Empat jebakan yang sering kena:",
                    "",
                    "  1. flag berhenti membaca begitu ketemu argumen pertama yang bukan",
                    "     flag.",
                    "       ./sapa -keras Levi    -keras terbaca sebagai flag",
                    "       ./sapa Levi -keras    -keras jadi argumen biasa, TIDAK aktif",
                    "     Tulis semua flag di depan. Banyak program lain membolehkan urutan",
                    "     bebas, package flag nggak.",
                    "",
                    "  2. Flag bool nggak menerima nilai yang ditulis terpisah.",
                    "       -keras          benar, artinya true",
                    "       -keras=false    benar",
                    "       -keras false    'false' jadi argumen posisional, flagnya",
                    "                       tetap TRUE. Diam-diam salah.",
                    "",
                    "  3. Satu strip dan dua strip sama aja: -nama dan --nama identik.",
                    "",
                    "  4. Flag yang nggak dikenal, atau nilai yang salah tipe, bikin",
                    "     program mencetak bantuan lalu keluar dengan kode 2. Kamu nggak",
                    "     perlu nulis satu pun pemeriksaan untuk itu.",
                    "",
                    "-h dan -help tersedia otomatis tanpa perlu didaftarkan. Isinya",
                    "disusun dari argumen ketiga tiap flag. Jadi kalimat itu bukan",
                    "komentar, kalimat itu dibaca pemakai programmu.",
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
                    "Package log",
                    "",
                    "log.Println dan log.Printf mirip fmt, tapi bedanya dua:",
                    "  - Tujuannya stderr, bukan stdout.",
                    "  - Tiap baris otomatis dikasih tanggal dan jam.",
                    "",
                    "  log.Println(\"mulai\")",
                    "  2025/07/01 09:14:22 mulai",
                    "",
                    "Makanya keluaran log kelihatan beda dari fmt.Println. Yang bisa",
                    "diatur:",
                    "  log.SetFlags(0)              matikan tanggal & jam",
                    "  log.SetFlags(log.LstdFlags | log.Lshortfile)  tambah berkas:baris",
                    "  log.SetPrefix(\"sapa: \")      awalan tetap di tiap baris",
                    "  log.New(os.Stderr, \"sapa: \", log.LstdFlags)   logger sendiri",
                    "",
                    "log.Fatal(err) sama dengan log.Print(err), lalu os.Exit(1). Kalau",
                    "programmu berhenti tepat di satu baris, padahal nggak ada panic dan",
                    "nggak ada jejak error panjang khas Go, biasanya penyebabnya log.Fatal.",
                    "Ada juga log.Fatalf untuk versi berformat, dan log.Panic yang mencetak",
                    "lalu panic. Panic dari log.Panic masih bisa ditangkap recover (materi",
                    "Error Handling). Fatal nggak bisa dihentikan siapa pun.",
                    "",
                    "Jebakan: os.Exit, dan karena itu juga log.Fatal, nggak menjalankan",
                    "defer yang masih tertunda.",
                    "",
                    "  defer f.Close()",
                    "  log.Fatal(err)    f tidak pernah ditutup, berkas sementara",
                    "                    tidak terhapus, kunci tidak dilepas",
                    "",
                    "Karena itu, main yang idiomatis memisahkan pekerjaannya:",
                    "",
                    "  func main() {",
                    "      if err := jalankan(); err != nil {",
                    "          log.Fatal(err)",
                    "      }",
                    "  }",
                    "",
                    "jalankan() cuma mengembalikan error. Waktu dia return, semua defer di",
                    "dalamnya sempat jalan, baru main mematikan program. Coba buktikan",
                    "sendiri: go run main.go -ulang 0 mencetak sapa: selesai lebih dulu,",
                    "baru baris Fatal-nya. Baris exit status 1 sesudahnya datang dari",
                    "go run, bukan dari programmu. Biner hasil go build nggak mencetaknya.",
                    "",
                    "Aturan pakainya: log.Fatal dan os.Exit cuma boleh dipanggil di main.",
                    "Jangan pernah dipanggil di dalam fungsi yang dipakai orang lain.",
                    "Fungsi library yang memanggil log.Fatal mematikan seluruh program",
                    "pemanggilnya, tanpa ngasih kesempatan menangani apa pun, dan nggak",
                    "mungkin diuji pakai go test. Fungsi cukup mengembalikan error. Yang",
                    "memutuskan program berhenti adalah main.",
                    "",
                    "Variabel lingkungan",
                    "",
                    "Variabel lingkungan (environment variable) adalah pengaturan yang",
                    "dikasih dari luar program, lewat shell:",
                    "  os.Getenv(\"HOME\")               isinya, atau \"\" kalau tidak ada",
                    "  nilai, ada := os.LookupEnv(\"X\")   'ada' membedakan diset-tapi-",
                    "                                   kosong dari tidak diset",
                    "Getenv nggak bisa membedakan dua keadaan itu. Jadi pakai LookupEnv",
                    "kalau string kosong termasuk nilai yang sah. Untuk mengisinya cuma",
                    "untuk sekali jalan: SAPA_LOKASI=Bontang go run main.go",
                    "",
                    "Stdout dan stderr, dan kenapa dipisah",
                    "  stdout = HASIL program, yang layak dipipe ke perintah berikutnya",
                    "  stderr = pesan untuk manusia: log, peringatan, cara pakai",
                    "",
                    "  $ go run main.go > hasil.txt",
                    "  sapa: SAPA_LOKASI belum diset, memakai bawaan",
                    "  sapa: selesai",
                    "",
                    "hasil.txt cuma berisi Halo, dunia!. Baris log tetap muncul di layar",
                    "karena nggak ikut dialihkan. Kalau log dicetak ke stdout, semua orang",
                    "yang mem-pipe programmu bakal menerima catatanmu sebagai data, dan",
                    "alatmu jadi nggak bisa disambung dengan alat lain. Karena itulah",
                    "package log memakai stderr dari awal.",
                ],
            },
        ],
    },
    {
        "title": "19. JSON & Struct Tag",
        "sections": [
            {
                "body": [
                    "JSON (JavaScript Object Notation) adalah format teks untuk bertukar",
                    "data. Hampir semua API di internet menjawab dalam bentuk JSON, dan",
                    "kebanyakan berkas konfigurasi modern juga memakainya.",
                    "",
                    "Go menyediakannya lewat package standar encoding/json. Nggak ada yang",
                    "perlu dipasang.",
                    "",
                    "Ada dua arah yang perlu kamu kuasai:",
                    "",
                    "  struct Go   --Marshal-->    teks JSON   (data keluar)",
                    "  teks JSON   --Unmarshal->   struct Go   (data masuk)",
                    "",
                    "Marshal mengubah data Go jadi teks JSON. Unmarshal kebalikannya.",
                    "Bentuk fungsinya:",
                    "",
                    "  func Marshal(v any) ([]byte, error)",
                    "  func Unmarshal(data []byte, v any) error",
                    "",
                    "Marshal mengembalikan []byte, bukan string. Untuk melihat isinya,",
                    "bungkus pakai string(data). Sebaliknya, Unmarshal menerima []byte,",
                    "jadi teks harus dibungkus []byte(teks) dulu.",
                    "",
                    "MarshalIndent sama persis dengan Marshal, cuma hasilnya dikasih",
                    "indentasi supaya enak dibaca manusia:",
                    "",
                    "  json.MarshalIndent(b, \"\", \"  \")   awalan \"\", indentasi 2 spasi",
                    "",
                    "Kenapa Unmarshal harus pakai &",
                    "",
                    "  var b Barang",
                    "  err := json.Unmarshal(data, &b)",
                    "",
                    "Tugas Unmarshal adalah mengisi variabel milik pemanggil. Sama seperti",
                    "di materi Pointer: Go selalu mengirim salinan, jadi fungsi yang perlu",
                    "mengubah variabel aslinya wajib menerima alamatnya.",
                    "",
                    "Lupa & nggak ketahuan waktu kompilasi. Programnya tetap dikompilasi,",
                    "lalu waktu jalan Unmarshal mengembalikan error",
                    "\"json: Unmarshal(non-pointer main.Barang)\", dan struct-mu tetap",
                    "kosong.",
                    "",
                    "Cuma field berhuruf besar yang ikut",
                    "",
                    "Aturan huruf besar dan kecil yang udah kamu pelajari kerasa akibatnya",
                    "di sini. encoding/json itu package lain, jadi dia nggak bisa melihat",
                    "field yang diawali huruf kecil sama sekali. Field seperti",
                    "kategori string hilang dari hasil Marshal, dan tetap kosong sesudah",
                    "Unmarshal. Nggak ada error, panic, atau peringatan apa pun. Ini",
                    "penyebab paling umum dari pertanyaan \"kenapa JSON-ku keluar cuma {}?\".",
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
                    "Perhatikan keluaran program di atas:",
                    "  - Diskon nggak muncul di JSON pertama, karena nilainya 0 dan",
                    "    bertanda omitempty.",
                    "  - Catatan nggak pernah muncul, karena bertanda \"-\".",
                    "  - kategori nggak muncul, karena huruf awalnya kecil.",
                    "",
                    "Bagian-bagian struct tag",
                    "",
                    "  Nama string `json:\"nama\"`",
                    "",
                    "Tulisan di dalam backtick itu namanya struct tag. Dia bukan komentar,",
                    "dan juga bukan nilai bawaan. Struct tag adalah string mentah (raw",
                    "string) yang nempel di sebuah field dan ikut tersimpan di dalam tipe",
                    "itu. Backtick dipakai supaya tanda petik di dalamnya nggak perlu",
                    "di-escape.",
                    "",
                    "Tulisnya rapat, tanpa spasi sesudah titik dua:",
                    "",
                    "  `json:\"nama\"`     benar",
                    "  `json: \"nama\"`    diam-diam tidak berlaku",
                    "",
                    "Kalau field-nya nggak dikasih tag sama sekali, nama di JSON mengikuti",
                    "nama field Go apa adanya. Jadi Harga menghasilkan {\"Harga\":15000}",
                    "dengan H besar. Itu jarang cocok dengan API yang minta huruf kecil.",
                    "",
                    "Opsi ditulis sesudah nama, dipisah koma:",
                    "",
                    "  `json:\"diskon,omitempty\"`  jangan tulis kalau nilainya kosong",
                    "  `json:\"-\"`                 jangan ikutkan sama sekali",
                    "  `json:\"harga,string\"`      angkanya ditulis sebagai \"15000\"",
                    "",
                    "Opsi ,string ada karena JavaScript kehilangan ketelitian untuk angka",
                    "di atas 2^53. Makanya banyak API mengirim ID yang besar sebagai teks.",
                    "",
                    "Empat jebakan yang sering kena:",
                    "",
                    "  1. omitempty memakai arti \"kosong\" versi Go: 0, \"\", false, nil,",
                    "     slice kosong, dan map kosong. Struct di dalam struct nggak",
                    "     pernah dianggap kosong, jadi omitempty di field seperti itu",
                    "     nggak ada efeknya.",
                    "  2. `json:\"-\"` membuang field. Kalau kamu memang mau field bernama",
                    "     \"-\", tulis `json:\"-,\"` pakai koma.",
                    "  3. Nama tag yang salah ketik nggak pernah dilaporkan. Field-nya",
                    "     cuma kosong terus, tanpa pesan apa pun.",
                    "  4. Field di JSON yang nggak punya pasangan di struct diabaikan,",
                    "     juga tanpa error. Kalau kamu mau field seperti itu ditolak,",
                    "     pakai dec.DisallowUnknownFields().",
                    "",
                    "Bentuk yang sama dibaca library lain",
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
                    "Go sendiri nggak ngerti arti db atau validate. Buat compiler,",
                    "semuanya cuma teks. Yang membacanya adalah library yang bersangkutan,",
                    "waktu program berjalan. Karena itu tag yang salah tulis nggak pernah",
                    "bikin kompilasi gagal.",
                    "",
                    "Sekarang kamu tahu arti backtick yang nempel di belakang hampir setiap",
                    "field struct di kode Go sungguhan.",
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
                    "Membedakan \"bernilai nol\" dari \"nggak ada\"",
                    "",
                    "Kalau JSON nggak memuat \"poin\", field Poin int bakal bernilai 0. Itu",
                    "sama persis dengan JSON yang memuat \"poin\": 0. Masalahnya sama dengan",
                    "membaca kunci map yang nggak ada di materi Map, dan jalan keluarnya",
                    "juga mirip:",
                    "",
                    "  Poin *int      nil berarti field-nya tidak ada di JSON,",
                    "                 atau ada tapi bernilai null; pointer ke 0",
                    "                 berarti ada dan nilainya memang nol",
                    "  map[string]any nilai, ada := m[\"poin\"]   pola comma ok",
                    "",
                    "Pakai pointer field cuma kalau perbedaan itu memang penting.",
                    "Contohnya permintaan PATCH, yang cuma mengubah field yang dikirim.",
                    "Setiap pointer menambah satu pemeriksaan nil di semua kode yang",
                    "memakainya.",
                    "",
                    "Semua angka JSON jadi float64",
                    "",
                    "Waktu Unmarshal ke map[string]any atau any, Go nggak tahu kamu maunya",
                    "int atau pecahan. JSON sendiri cuma punya satu tipe, yaitu number.",
                    "Jadi semuanya dijadikan float64:",
                    "",
                    "  bebas[\"umur\"].(int)      ok bernilai false; tanpa ok: PANIC",
                    "  bebas[\"umur\"].(float64)  benar, lalu int(umur) kalau perlu",
                    "",
                    "Akibat berikutnya: ID di atas 2^53 kehilangan ketelitian kalau lewat",
                    "float64. Untuk itu pakai struct dengan field int64, atau json.Number.",
                    "",
                    "Jadi, pakai map[string]any cuma kalau bentuk datanya memang nggak",
                    "diketahui. Kalau bentuknya udah pasti, pakai struct. Tipenya jelas,",
                    "salah ketik nama field ketahuan waktu kompilasi, dan nggak perlu type",
                    "assertion.",
                    "",
                    "Decoder dan Encoder: JSON yang mengalir",
                    "",
                    "  json.NewDecoder(r).Decode(&v)   r = io.Reader apa pun",
                    "  json.NewEncoder(w).Encode(v)    w = io.Writer apa pun",
                    "",
                    "Dua-duanya nggak peduli sumber dan tujuannya apa. Berkas dari materi",
                    "Berkas, os.Stdin dan os.Stdout, strings.NewReader untuk pengujian,",
                    "dan nanti body permintaan HTTP, semuanya memenuhi io.Reader atau",
                    "io.Writer. Di sini kelihatan untungnya interface kecil yang cuma punya",
                    "satu method.",
                    "",
                    "Bedanya dengan Marshal dan Unmarshal:",
                    "  - Marshal menyusun seluruh hasilnya di memori dulu. Cocok kalau",
                    "    datanya kecil, atau kamu memang butuh []byte-nya.",
                    "  - Decoder membaca sambil jalan, jadi nggak perlu memuat seluruh",
                    "    berkas ke memori. Ini yang dipakai untuk data besar.",
                    "  - Encode selalu menambahkan satu baris baru di akhir.",
                    "",
                    "JSON lebih ketat dari dugaanmu",
                    "",
                    "  - Koma di akhir daftar dilarang: {\"nama\":\"Eka\",} nggak sah. Ini",
                    "    kebalikan dari Go, yang justru mewajibkan koma di baris terakhir",
                    "    literal struct dan slice yang ditulis menurun.",
                    "  - Kunci wajib pakai tanda petik ganda. Petik satu ditolak.",
                    "  - Nggak ada komentar di dalam JSON.",
                    "",
                    "Jangan pernah abaikan error dari Unmarshal",
                    "",
                    "  json.Unmarshal(data, &b)      <- error dibuang begitu saja",
                    "",
                    "Kalau JSON-nya rusak, b tetap berisi zero value: nama \"\", harga 0,",
                    "slice nil. Dari luar nggak ada yang kelihatan salah. Program jalan",
                    "terus, menyimpan data kosong itu ke database, atau melaporkan saldo 0",
                    "ke orang yang saldonya nggak nol. Bug seperti ini baru ketahuan",
                    "berhari-hari kemudian, dan susah dilacak karena nggak ada yang crash.",
                    "",
                    "Anggap setiap JSON dari luar sebagai data yang belum tentu benar, dan",
                    "tulis if err != nil seperti di materi Error Handling.",
                ],
            },
        ],
    },
    {
        "title": "20. Goroutine & Channel",
        "sections": [
            {
                "body": [
                    "Fitur di materi ini yang bikin Go terkenal.",
                    "",
                    "Goroutine adalah fungsi yang jalan bersamaan dengan fungsi lain.",
                    "Caranya gampang: tambahkan kata go di depan pemanggilan fungsi.",
                    "",
                    "  go kerjakanSesuatu()",
                    "",
                    "Goroutine itu murah. Satu goroutine cuma makan sekitar 2 KB memori di",
                    "awal, sedangkan satu thread sistem operasi butuh 1-8 MB. Program Go",
                    "biasa bisa menjalankan ribuan goroutine tanpa masalah.",
                    "",
                    "Masalahnya, main() nggak nunggu goroutine selesai. Begitu main",
                    "berakhir, semua goroutine langsung ikut mati.",
                    "",
                    "Ada dua cara menunggu dengan benar:",
                    "  1. sync.WaitGroup  - tunggu sekumpulan goroutine",
                    "  2. channel         - komunikasi sekaligus sinkronisasi",
                    "",
                    "Prinsip Go soal concurrency:",
                    "  'Jangan berkomunikasi dengan berbagi memori.",
                    "   Berbagilah memori dengan berkomunikasi.'",
                    "",
                    "Maksudnya, daripada banyak goroutine mengutak-atik variabel yang",
                    "sama, lebih baik data dikirim dari satu goroutine ke goroutine lain",
                    "lewat channel.",
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
                    "Contoh tadi pakai dua tipe dari package sync tanpa penjelasan.",
                    "Dua-duanya langsung siap dipakai begitu dideklarasikan. Zero value-nya",
                    "udah benar, jadi nggak perlu make() atau new():",
                    "  var wg sync.WaitGroup",
                    "  var mu sync.Mutex",
                    "",
                    "sync.WaitGroup itu cuma sebuah penghitung:",
                    "  wg.Add(1)    naikkan pencacah satu",
                    "  wg.Done()    turunkan satu, biasanya lewat defer",
                    "  wg.Wait()    berhenti di sini sampai pencacahnya nol",
                    "",
                    "Ada dua aturan letak yang nggak boleh ketuker:",
                    "  - wg.Add(1) ditulis di goroutine yang memanggil, sebelum kata go.",
                    "    Kalau ditaruh di dalam goroutine-nya, wg.Wait() bisa lolos sebelum",
                    "    goroutine itu sempat dihitung. Programnya selesai sebelum",
                    "    kerjanya beres.",
                    "  - defer wg.Done() ditulis di baris pertama badan goroutine. Dengan",
                    "    begitu penghitungnya tetap turun, walaupun goroutine keluar lewat",
                    "    return atau panic. Satu Done yang nggak pernah jalan bikin Wait()",
                    "    nunggu selamanya.",
                    "",
                    "Satu jebakan lagi: WaitGroup nggak boleh disalin. Kalau perlu dikirim",
                    "ke fungsi lain, kirim sebagai pointer (*sync.WaitGroup). Kalau disalin,",
                    "Done() menurunkan penghitung salinannya, sedangkan Wait() di pemanggil",
                    "nunggu penghitung yang asli. Hasilnya nunggu selamanya. Compiler diam",
                    "aja soal ini, tapi go vet bisa menangkapnya:",
                    "  kerja passes lock by value: sync.WaitGroup contains sync.noCopy",
                    "Bentuk yang benar bakal kamu lihat di worker pool, materi berikutnya.",
                    "",
                    "sync.Mutex itu kunci pintu. Pada satu waktu, kuncinya cuma dipegang",
                    "satu goroutine:",
                    "  mu.Lock()          ambil kunci, tunggu kalau sedang dipegang",
                    "  mu.Unlock()        kembalikan kunci",
                    "  defer mu.Unlock()  bentuk paling aman kalau kuncinya sefungsi penuh",
                    "",
                    "Bagian yang paling penting, dan paling sering disalahpahami: mutex",
                    "menjaga data tertentu, bukan blok kode. Di contoh tadi, mu menjaga",
                    "slice hasil. Artinya setiap akses ke hasil, termasuk cuma membaca,",
                    "harus lewat kunci yang sama. Kalau ada satu tempat yang lupa",
                    "mengunci, semua Lock di tempat lain jadi percuma.",
                    "",
                    "select yang muncul di baris terakhir contoh dibahas lengkap di materi",
                    "berikutnya, Pola Goroutine.",
                ]
            },
            {
                "body": [
                    "Channel adalah pipa untuk mengirim data antar goroutine.",
                    "",
                    "  ch := make(chan int)       tanpa penyangga",
                    "  ch := make(chan int, 5)    penyangga 5 slot",
                    "",
                    "  ch <- 10       KIRIM nilai ke channel",
                    "  n := <-ch      TERIMA nilai dari channel",
                    "  close(ch)      tutup channel",
                    "",
                    "Penyangga (buffer) itu tempat antre di dalam channel. Channel tanpa",
                    "penyangga bersifat sinkron: pengirim nunggu sampai ada penerima, dan",
                    "sebaliknya. Channel berpenyangga nggak bikin pengirim menunggu sampai",
                    "penyangganya penuh.",
                    "",
                    "Menerima dari channel yang udah ditutup:",
                    "  n, ok := <-ch",
                    "ok bernilai false kalau channel-nya udah ditutup dan isinya kosong.",
                    "",
                    "Aturan close:",
                    "  - Cuma pengirim yang boleh menutup channel.",
                    "  - Mengirim ke channel yang udah ditutup bikin panic.",
                    "  - Menutup channel dua kali juga bikin panic.",
                    "  - Menutup channel nggak wajib. Tutup cuma kalau penerimanya perlu",
                    "    tahu bahwa datanya udah habis.",
                    "",
                    "Deadlock",
                    "",
                    "Deadlock terjadi kalau semua goroutine saling nunggu, dan nggak ada",
                    "yang bisa jalan. Go mendeteksinya, lalu menghentikan program dengan",
                    "pesan:",
                    "  fatal error: all goroutines are asleep - deadlock!",
                    "",
                    "Penyebab yang paling umum:",
                    "  ch := make(chan int)",
                    "  ch <- 1        deadlock, tidak ada yang menerima",
                    "",
                    "Race condition",
                    "",
                    "Kalau beberapa goroutine mengubah data yang sama tanpa penjagaan,",
                    "hasilnya nggak bisa ditebak. Ini yang disebut race condition. Cara",
                    "mengatasinya:",
                    "  - pakai sync.Mutex untuk mengunci akses, atau",
                    "  - kirim datanya lewat channel, jangan dipakai bareng-bareng.",
                    "",
                    "Race bisa dideteksi otomatis dengan:  go run -race program.go",
                ]
            },
        ],
    },
    {
        "title": "21. Pola Goroutine: Channel Berarah, select & Worker Pool",
        "sections": [
            {
                "body": [
                    "Materi Goroutine & Channel udah ngenalin go, channel, WaitGroup, Mutex,",
                    "dan close. Tapi di kode contohnya ada dua hal yang dipakai tanpa",
                    "dijelaskan sama sekali: kata select, dan tanda }(i) di ujung",
                    "goroutine. Materi ini menjelaskan keduanya, lalu membahas pola-pola",
                    "yang bakal kamu temui waktu membaca kode Go orang lain.",
                    "",
                    "Channel berarah",
                    "",
                    "Selama ini channel selalu ditulis chan int: boleh dikirimi, boleh",
                    "diterima. Arahnya bisa dipersempit, dan arah itu jadi bagian dari",
                    "tipenya:",
                    "",
                    "  chan Tugas      dua arah: boleh kirim, boleh terima",
                    "  <-chan Tugas    HANYA boleh diterima (dibaca)",
                    "  chan<- Hasil    HANYA boleh dikirimi (ditulis)",
                    "",
                    "Cara bacanya: panah selalu nempel di kata chan.",
                    "  <-chan   panah KELUAR dari channel -> data keluar, kamu menerima",
                    "  chan<-   panah MASUK ke channel    -> data masuk, kamu mengirim",
                    "",
                    "Buat apa? Arahnya jadi keterangan yang dijaga compiler. Lihat bentuk",
                    "fungsi ini:",
                    "",
                    "  func pekerja(id int, tugas <-chan Tugas, hasil chan<- Hasil)",
                    "",
                    "Tanpa membaca isinya sama sekali, kamu udah tahu pekerja mengambil",
                    "tugas dan menghasilkan hasil, dan nggak mungkin kebalik. Kalau di",
                    "dalamnya kamu salah nulis tugas <- t, kesalahannya nggak nunggu",
                    "ketahuan waktu program jalan. Programnya langsung gagal dikompilasi:",
                    "",
                    "  invalid operation: cannot send to receive-only channel tugas",
                    "",
                    "close juga ikut dijaga: close(tugas) pada channel yang cuma boleh",
                    "diterima ditolak compiler. Ini aturan \"yang menutup channel cuma",
                    "pengirim\" dari materi sebelumnya. Bedanya, sekarang compiler yang",
                    "menjaganya, kamu nggak perlu ngandelin ingatan.",
                    "",
                    "Penyempitan arah terjadi otomatis, dan cuma bisa ke satu arah:",
                    "  chan T    ->  <-chan T  atau  chan<- T     boleh, tanpa konversi",
                    "  <-chan T  ->  chan T                       TIDAK boleh",
                    "Jadi polanya selalu sama. Bikin channel dua arah sekali di make(),",
                    "lalu persempit arahnya waktu diserahkan ke fungsi.",
                ],
            },
            {
                "heading": "Worker pool: tiga pekerja, satu antrean",
                "body": [
                    "Worker pool adalah pola concurrency yang paling sering ditemui di kode",
                    "sungguhan. Susunannya selalu begini: satu channel tugas, N goroutine",
                    "pekerja yang membaca channel itu, satu channel hasil, dan WaitGroup",
                    "untuk tahu kapan semua pekerja selesai.",
                    "",
                    "Jumlah pekerja nggak harus sama dengan jumlah tugas, dan memang di",
                    "situ gunanya. Enam ribu tugas boleh dikerjakan tiga pekerja. Pekerja",
                    "yang nganggur mengambil tugas berikutnya sendiri, tanpa ada yang",
                    "ngatur.",
                    "",
                    "Yang paling sering salah adalah siapa menutup apa:",
                    "  - Channel tugas ditutup oleh yang mengirim tugas, sesudah tugasnya",
                    "    habis. Itu yang bikin for t := range tugas di tiap pekerja",
                    "    berhenti sendiri. Tanpa close, ketiga pekerja nunggu selamanya.",
                    "  - Channel hasil ditutup sesudah semua pekerja selesai, dan itu harus",
                    "    dikerjakan goroutine tersendiri. Kalau wg.Wait() dipanggil di main",
                    "    sebelum for h := range hasil, pekerja kejebak nunggu hasilnya",
                    "    diambil, sementara main nunggu pekerja selesai. Hasilnya deadlock.",
                    "",
                    "Perhatikan juga, wg dikirim sebagai pointer (*sync.WaitGroup).",
                    "WaitGroup nggak boleh disalin. Salinannya punya penghitung sendiri, dan",
                    "Wait() yang asli nggak bakal pernah selesai. go vet menangkapnya:",
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
                    "Aturan main select",
                    "",
                    "select bentuknya mirip switch, tapi tiap case-nya wajib berupa operasi",
                    "channel, yaitu mengirim atau menerima. Aturannya cuma lima, dan",
                    "semuanya perlu kamu tahu:",
                    "",
                    "  1. Semua case dilihat sekaligus. select nunggu sampai ada satu case",
                    "     yang siap, lalu menjalankan case itu aja, sekali.",
                    "",
                    "  2. Kalau beberapa case siap bersamaan, yang dijalankan dipilih acak,",
                    "     nggak selalu yang paling atas. Ini sengaja, supaya satu channel",
                    "     yang selalu ramai nggak bikin channel lain nggak pernah kebagian.",
                    "     Jadi jangan pernah mengandalkan urutan case.",
                    "",
                    "  3. Kalau ada klausa default, select nggak nunggu sama sekali. Begitu",
                    "     nggak ada case yang siap, default langsung jalan. Ini cara",
                    "     mengintip channel tanpa ikut nunggu.",
                    "",
                    "  4. select{} tanpa satu case pun nunggu selamanya. Kadang dipakai di",
                    "     ujung main() sebuah server, supaya programnya nggak keburu keluar.",
                    "",
                    "  5. Channel yang bernilai nil nggak pernah siap. Kalau sebuah variabel",
                    "     channel kamu isi nil, case yang memakainya praktis mati. Trik ini",
                    "     bakal kamu lihat di loop select yang sumber datanya habis satu per",
                    "     satu.",
                    "",
                    "Timeout",
                    "  case <-time.After(2 * time.Second):",
                    "time.After mengembalikan channel yang menerima satu nilai sesudah",
                    "waktunya lewat. Kalau dipasang di select, artinya: tunggu, tapi",
                    "menyerah kalau kelamaan.",
                    "",
                    "Jebakannya, kalau ditaruh di dalam loop yang berputar ribuan kali,",
                    "setiap putaran bikin timer baru. Untuk menunggu berulang-ulang, pakai",
                    "time.NewTimer beserta Reset, atau ticker.",
                    "",
                    "Detak berkala",
                    "  tick := time.NewTicker(20 * time.Millisecond)",
                    "  defer tick.Stop()",
                    "Ticker mengirim waktu ke tick.C berulang-ulang selama program hidup.",
                    "Kalau lupa Stop(), dia terus berdetak walaupun nggak ada yang",
                    "mendengarkan.",
                    "",
                    "Channel sinyal",
                    "  selesai := make(chan struct{})",
                    "  close(selesai)",
                    "struct{} itu struct kosong. Ukurannya nol byte, dan nggak menyimpan",
                    "apa-apa. Memang itu maksudnya: yang dikirim adalah kejadiannya, bukan",
                    "data. make(chan bool) juga bisa, tapi pembacanya jadi bertanya-tanya",
                    "apakah true dan false-nya punya arti. Dengan struct{}, nggak ada yang",
                    "bisa salah paham.",
                    "",
                    "Kenapa pakai close(selesai), nggak kirim selesai <- struct{}{}?",
                    "  - Satu kiriman cuma membangunkan satu penerima. Kalau ada lima",
                    "    goroutine yang nunggu, empat sisanya tetap menggantung.",
                    "  - close membangunkan semua penerima sekaligus, dan seterusnya.",
                    "    Menerima dari channel yang udah ditutup langsung mengembalikan",
                    "    nilai nol tanpa menunggu, berapa kali pun dibaca.",
                    "Karena itu, semua pola \"berhenti sekarang\" pakai close, bukan kirim.",
                    "",
                    "Kebocoran goroutine",
                    "",
                    "Goroutine yang nunggu channel yang nggak pernah diisi nggak bakal",
                    "pernah selesai. Programnya nggak crash. Dia cuma makin lama makin",
                    "boros memori, dan server yang jalan berhari-hari akhirnya kehabisan",
                    "memori. Deteksi deadlock Go nggak membantu di sini, karena dia cuma",
                    "bunyi kalau semua goroutine tidur. Cara menyuruh goroutine berhenti",
                    "dengan rapi dibahas di materi context berikutnya.",
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
                    "Jebakan variabel loop",
                    "",
                    "Materi sebelumnya menulis goroutine-nya begini tanpa penjelasan:",
                    "go func(n int) { ... }(i). Kenapa i dikirim sebagai argumen, nggak",
                    "langsung dipakai dari dalam?",
                    "",
                    "Sebelum Go 1.22, for i := 1; i <= 5; i++ cuma bikin satu variabel i,",
                    "yang dipakai ulang di semua putaran. Closure di dalam goroutine",
                    "menangkap variabelnya, bukan nilainya saat itu. Goroutine baru mulai",
                    "jalan sesaat kemudian, dan waktu dia akhirnya membaca i, loop-nya udah",
                    "selesai. Akibatnya, lima goroutine mencetak angka yang sama, biasanya",
                    "6, karena itu nilai i waktu loop berhenti.",
                    "",
                    "Ada dua cara mengatasinya, dan dua-duanya masih banyak di kode lama:",
                    "",
                    "  go func(n int) { pakai(n) }(i)   oper sebagai argumen; salinannya",
                    "                                   dibuat saat itu juga, saat dipanggil",
                    "  i := i                           bikin variabel baru tiap putaran,",
                    "                                   sengaja dinamai sama",
                    "",
                    "Sejak Go 1.22, variabelnya memang baru di tiap putaran, jadi dua cara",
                    "itu nggak diperlukan lagi. Tapi perhatikan: yang menentukan aturan",
                    "mana yang berlaku adalah baris go 1.xx di go.mod, bukan versi Go yang",
                    "terpasang di komputermu. Modul yang masih menulis go 1.21 tetap pakai",
                    "aturan lama, walaupun dikompilasi pakai Go 1.23.",
                    "",
                    "Jadi i := i bukan kode aneh, dan bukan salah ketik. Itu kode yang",
                    "ditulis sebelum 1.22, dan kamu bakal sering melihatnya. Jebakan yang",
                    "sama dulu juga berlaku untuk for _, v := range daftar.",
                    "",
                    "Selain Mutex",
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
                    "Membuktikan ada atau nggaknya race",
                    "  go run -race program.go",
                    "  go test -race ./...",
                    "Race detector mengawasi akses memori sungguhan selama program jalan.",
                    "Dia melapor kalau ada dua goroutine yang menyentuh alamat yang sama",
                    "tanpa penjagaan. Race detector jauh lebih lambat dan lebih boros",
                    "memori, jadi dipakai waktu menguji, bukan di produksi. Dia juga cuma",
                    "melihat kode yang betul-betul dijalankan. Race di jalur kode yang",
                    "nggak pernah diuji tetap lolos. Ketiga program di materi ini bersih",
                    "waktu dijalankan dengan -race.",
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
                    "Materi Goroutine & Channel ngajarin cara menunggu goroutine sampai",
                    "selesai. Materi ini ngajarin cara menyuruhnya berhenti.",
                    "",
                    "Bedanya besar. sync.WaitGroup nanya \"udah selesai belum?\". context",
                    "bilang \"udah, jangan diterusin, pulang aja\".",
                    "",
                    "Untuk apa? Bayangkan satu permintaan HTTP masuk. Untuk melayaninya,",
                    "program menjalankan tiga query database dan dua panggilan ke layanan",
                    "lain. Lalu pemakainya menutup tab browser-nya. Tanpa context, kelima",
                    "pekerjaan itu jalan terus sampai habis. Koneksi database terpakai",
                    "untuk hasil yang nggak bakal dibaca siapa pun, dan goroutine-nya",
                    "numpuk. Server yang sibuk sering mati pelan-pelan karena hal seperti",
                    "ini, bukan karena salah hitung.",
                    "",
                    "context.Context adalah satu nilai yang dibawa turun ke setiap fungsi,",
                    "dan isinya sinyal \"berhenti\". Kamu bakal sering melihatnya sebagai",
                    "parameter pertama di hampir semua kode Go sungguhan:",
                    "",
                    "  func AmbilUser(ctx context.Context, id int) (*User, error)",
                    "",
                    "Akarnya dibuat cuma di satu tempat, di paling atas:",
                    "  context.Background()  akar sungguhan, dibuat di main() atau",
                    "                        di titik masuk sebuah permintaan",
                    "  context.TODO()        penanda 'belum diputuskan mau pakai",
                    "                        context yang mana'. Perilakunya sama",
                    "                        persis; bedanya cuma niat, supaya",
                    "                        gampang dicari lagi nanti",
                    "",
                    "Dari akar itu diturunkan context anak:",
                    "  ctx, cancel := context.WithCancel(induk)",
                    "  ctx, cancel := context.WithTimeout(induk, 2*time.Second)",
                    "  ctx, cancel := context.WithDeadline(induk, jamTertentu)",
                    "",
                    "WithTimeout menghitung dari sekarang (\"paling lama 2 detik\").",
                    "WithDeadline menyebut titik waktunya (\"paling lambat jam 10\").",
                    "",
                    "Ketiganya mengembalikan dua nilai, dan nilai kedua, cancel, wajib",
                    "dipanggil. Biasanya langsung didaftarkan: defer cancel(). Kalau lupa,",
                    "context anak tetap nempel ke induknya sampai induknya sendiri mati.",
                    "Itu kebocoran memori. go vet bisa menangkapnya, dengan pesan:",
                    "  the cancel function returned by context.WithTimeout should",
                    "  be called, not discarded, to avoid a context leak",
                    "",
                    "Memanggil cancel dua kali itu aman dan nggak ngapa-ngapain. Jadi nggak",
                    "ada alasan ragu untuk men-defer-nya.",
                    "",
                    "Context yang diturunkan membentuk pohon. Membatalkan satu context",
                    "otomatis membatalkan semua keturunannya, sedalam apa pun. Karena itu,",
                    "satu permintaan yang dibatalkan bisa menghentikan semua pekerjaan yang",
                    "lahir darinya sekaligus. Kamu nggak perlu mendaftar satu per satu",
                    "siapa aja yang harus dikasih tahu.",
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
                    "Sebuah Context cuma punya empat method, dan yang sering dipakai",
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
                    "Periksa alasannya pakai errors.Is, jangan pakai ==. Dalam perjalanan",
                    "pulang, error itu biasanya udah dibungkus %w (lihat materi Error",
                    "Handling):",
                    "  if errors.Is(err, context.DeadlineExceeded) { ... }",
                    "",
                    "Ini bentuk baku di dalam loop atau worker. Hafalkan, karena kamu bakal",
                    "menulisnya berkali-kali:",
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
                    "Jebakan yang perlu kamu tahu:",
                    "",
                    "  1. context nggak membunuh apa pun. Dia cuma menutup sebuah channel.",
                    "     Kalau kodemu nggak pernah memeriksa ctx.Done(), pekerjaannya",
                    "     jalan terus sampai habis, seolah nggak terjadi apa-apa.",
                    "     Perulangan berat, time.Sleep, dan pembacaan berkas biasa nggak",
                    "     berhenti sendiri gara-gara timeout.",
                    "",
                    "  2. Sesudah cancel(), goroutine-nya belum tentu udah berhenti. Kamu",
                    "     baru mengirim sinyal. Contoh di atas betul-betul menunggunya",
                    "     lewat channel selesai. Tanpa itu, main bisa keburu keluar, dan",
                    "     kamu nggak bakal sempat melihat pesan penutupnya.",
                    "",
                    "  3. Kalau ctx.Done() dan channel data sama-sama siap, select memilih",
                    "     secara acak. Jadi satu data bisa telanjur diproses walaupun",
                    "     context-nya udah batal. Kalau itu nggak boleh terjadi, cek lagi",
                    "     ctx.Err() != nil di awal case-nya.",
                    "",
                    "  4. Batas waktu itu diwariskan, dan nggak bisa dilonggarkan. Anak dari",
                    "     induk yang sisa waktunya 1 detik nggak bisa minta 5 detik. Dia",
                    "     tetap mati waktu induknya mati. Deadline anak cuma bisa lebih",
                    "     pendek, nggak pernah lebih panjang.",
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
                    "context.WithValue menitipkan data yang ikut sepanjang satu permintaan.",
                    "Misalnya request ID untuk log, identitas pemakai yang udah login, atau",
                    "penanda bahasa. Cuma itu gunanya.",
                    "",
                    "WithValue bukan tempat menaruh parameter fungsi biasa. Kalau sebuah",
                    "fungsi butuh id barang untuk bekerja, tulis id sebagai parameter.",
                    "Kalau id itu disembunyikan di dalam ctx, compiler nggak bisa lagi",
                    "ngasih tahu waktu kamu lupa mengisinya. Kesalahannya baru ketahuan",
                    "waktu program udah jalan.",
                    "",
                    "Dua aturan WithValue yang gampang dilanggar:",
                    "  - Kuncinya jangan string polos. Pakai tipe sendiri",
                    "    (type kunciCtx string), supaya package lain yang kebetulan juga",
                    "    pakai kunci \"user\" nggak menimpa punyamu tanpa ketahuan.",
                    "  - Value() mengembalikan any, jadi selalu pakai type assertion",
                    "    dua nilai: v, ok := ctx.Value(k).(string). Bentuk satu nilai",
                    "    bakal panic begitu titipannya ternyata nggak ada.",
                    "",
                    "Ada kebiasaan yang bikin kode Go di mana-mana kelihatan seragam:",
                    "  - ctx selalu jadi parameter pertama, bahkan sebelum parameter yang",
                    "    kelihatannya lebih penting.",
                    "  - Namanya selalu ctx. Bukan c, bukan konteks, bukan cx.",
                    "  - Jangan kirim nil sebagai context. Pakai context.TODO() kalau",
                    "    memang belum punya.",
                    "  - Jangan simpan Context di field struct. Context itu milik satu",
                    "    panggilan, sedangkan struct dipakai berulang-ulang. Hasilnya ctx",
                    "    basi yang udah lama batal, atau malah ctx yang nggak pernah batal",
                    "    padahal seharusnya batal. Kirim lewat parameter, jangan lewat",
                    "    field.",
                    "",
                    "Di mana kamu bakal ketemu context:",
                    "  r.Context()                   ctx milik satu permintaan HTTP;",
                    "                                otomatis batal saat pemakai",
                    "                                memutus koneksinya",
                    "  http.NewRequestWithContext()  panggilan HTTP keluar yang bisa",
                    "                                dibatalkan dan dibatasi waktu",
                    "  db.QueryContext(ctx, ...)     query yang benar-benar berhenti",
                    "  exec.CommandContext(ctx, ...) proses luar yang ikut dimatikan",
                    "",
                    "Hampir setiap library Go buatan pihak lain meminta ctx di parameter",
                    "pertamanya. Sekarang kamu tahu benda apa yang harus dikasih ke situ,",
                    "dan kenapa hampir selalu ada defer cancel() di dekatnya.",
                ],
            },
        ],
    },
    {
        "title": "23. Generics: Type Parameter & Package slices/maps",
        "sections": [
            {
                "body": [
                    "Misalkan kamu butuh fungsi \"ambil yang terbesar\" untuk int dan juga",
                    "untuk float64. Sampai materi ini, pilihanmu cuma dua, dan dua-duanya",
                    "jelek:",
                    "",
                    "  1. Tulis dua fungsi kembar, TerbesarInt dan TerbesarFloat. Lalu tiga,",
                    "     lalu empat, dan tiap perbaikan bug harus disalin ke semuanya.",
                    "  2. Pakai any (interface{}), lalu type assertion di dalamnya. Compiler",
                    "     jadi nggak bisa ngecek apa-apa. Salah tipe baru ketahuan waktu",
                    "     program jalan, dalam bentuk panic.",
                    "",
                    "Sejak Go 1.18 ada pilihan ketiga, yaitu generics. Fungsinya ditulis",
                    "sekali, tipenya jadi parameter, dan compiler tetap memeriksa semuanya",
                    "seperti biasa.",
                    "",
                    "  func Terbesar[T int | float64](a, b T) T {",
                    "      if a > b {",
                    "          return a",
                    "      }",
                    "      return b",
                    "  }",
                    "",
                    "Cara membaca kurung sikunya",
                    "",
                    "Bagian ini paling sering salah dibaca, karena kurung siku udah dipakai",
                    "untuk hal lain sejak materi Array & Slice. Bedakan dari letaknya:",
                    "",
                    "  angka[2]         kurung siku sesudah sebuah NILAI     -> indeks slice/array",
                    "  Terbesar[int]    kurung siku sesudah sebuah NAMA      -> parameter tipe",
                    "  []int            kurung siku kosong di DEPAN tipe     -> slice",
                    "  [5]int           ada angkanya, di DEPAN tipe          -> array",
                    "",
                    "Jadi Terbesar[int] bukan \"elemen ke-int dari Terbesar\". Artinya",
                    "Terbesar yang T-nya diisi int. Kalau udah terbiasa, T di [T any]",
                    "kebaca sama seperti n di (n int): sebuah nama kosong yang diisi waktu",
                    "dipanggil. Bedanya, yang diisikan ke T itu sebuah tipe, bukan angka.",
                    "",
                    "Constraint: tipe apa aja yang boleh mengisi T",
                    "",
                    "Yang ditulis sesudah T disebut constraint, yaitu syarat untuk T.",
                    "Bentuknya interface, tapi di sini interface dipakai sebagai daftar",
                    "tipe, bukan daftar method:",
                    "",
                    "  [T any]             apa saja. any itu nama lain interface{}",
                    "                      (materi Interface).",
                    "  [T comparable]      tipe yang bisa dibandingkan dengan == dan !=. Inilah",
                    "                      syarat supaya T boleh dipakai sebagai KUNCI map.",
                    "  [T int | float64]   salah satu dari daftar itu saja. Pemisahnya tanda |.",
                    "",
                    "Daftar yang panjang biasanya dikasih nama sendiri, supaya bisa dipakai",
                    "berulang:",
                    "",
                    "  type Angka interface {",
                    "      ~int | ~int64 | ~float64",
                    "  }",
                    "",
                    "Tanda ~ (tilde) itu ada artinya. ~int artinya \"int, atau tipe bentukan",
                    "mana pun yang tipe dasarnya int\". Tanpa tilde, type Celsius float64",
                    "dari materi Tipe Bentukan bakal ditolak, padahal isinya persis",
                    "float64. Hampir semua constraint di kode nyata pakai tilde. Kalau kamu",
                    "lupa, yang kena adalah orang yang memakai fungsimu, dan pesannya",
                    "membingungkan:",
                    "  Celsius does not satisfy Angka (possibly missing ~ for float64)",
                    "",
                    "Inferensi tipe",
                    "",
                    "Inferensi artinya compiler menyimpulkan sendiri. Hampir selalu kamu",
                    "nggak perlu menyebut T sama sekali:",
                    "",
                    "  Terbesar(2, 3)            T disimpulkan int dari argumennya",
                    "  Terbesar(2.5, 1.5)        T disimpulkan float64",
                    "  Terbesar[float64](2, 7)   ditulis tegas; perlu kalau argumennya ambigu",
                    "",
                    "Makanya kode yang memakai generics sering nggak kelihatan \"generik\"",
                    "waktu dipanggil. Kurung sikunya cuma muncul di tempat fungsinya",
                    "didefinisikan.",
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
                    "Parameter tipe nggak terbatas di fungsi. Struct juga boleh punya.",
                    "Ada tiga aturan yang bikin orang kesandung di sini:",
                    "",
                    "  - Nama tipenya selalu membawa T. Yang ada itu Tumpukan[int] dan",
                    "    Tumpukan[string]. Tumpukan sendirian bukan tipe yang sah.",
                    "  - Receiver method-nya wajib mengulang [T], dan itu artinya",
                    "    mendeklarasikan nama, bukan mengisi tipe:",
                    "    func (t *Tumpukan[T]) Dorong(v T).",
                    "  - Method nggak boleh punya parameter tipe sendiri. Kalau butuh tipe",
                    "    kedua yang bebas (misalnya Peta di contoh sebelumnya), jadikan",
                    "    fungsi biasa di luar struct. Ini memang batasan Go, bukan karena",
                    "    kamu lupa sesuatu.",
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
                    "Begitu ada generics, fungsi-fungsi yang dulu ditulis ulang di tiap",
                    "proyek akhirnya bisa masuk pustaka standar: package slices (Go 1.21)",
                    "dan maps. Cara yang lama nggak dihapus, jadi kamu bakal melihat",
                    "dua-duanya di kode orang. Anggap aja sebagai hal yang sama:",
                    "",
                    "  cara lama                      cara sekarang",
                    "  sort.Ints(s)                   slices.Sort(s)",
                    "  sort.Strings(s)                slices.Sort(s)",
                    "  sort.Slice(s, kurangDari)      slices.SortFunc(s, banding)",
                    "  sort.SearchInts(s, x)          slices.BinarySearch(s, x)",
                    "  loop cari sendiri              slices.Contains(s, x), slices.Index(s, x)",
                    "  loop kumpulkan kunci lalu sort slices.Sorted(maps.Keys(m))",
                    "",
                    "Ada satu beda yang gampang menjebak. Pembanding sort.Slice",
                    "mengembalikan bool (apakah a duluan?). Pembanding slices.SortFunc",
                    "mengembalikan int: negatif, nol, atau positif, seperti",
                    "strings.Compare.",
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
                    "Jebakan yang sering kena:",
                    "",
                    "  1. Fungsi generik cuma boleh memakai apa yang dijanjikan",
                    "     constraint-nya. Dengan [T any], baris a > b ditolak compiler,",
                    "     karena any nggak menjanjikan apa-apa soal urutan. Dengan",
                    "     [T comparable], a == b boleh, tapi a > b tetap nggak boleh. Kalau",
                    "     butuh method, constraint-nya harus interface yang memuat method",
                    "     itu. Isi fungsi nggak bisa minta lebih dari yang dijanjikan.",
                    "",
                    "  2. return nil sering nggak sah di dalam fungsi generik. T bisa aja",
                    "     int, dan int nggak punya nil. Polanya: var kosong T, lalu",
                    "     return kosong, false.",
                    "",
                    "  3. slices.Sort, slices.Reverse, dan slices.SortFunc mengubah slice di",
                    "     tempat, dan nggak mengembalikan apa pun. Nulis s = slices.Sort(s)",
                    "     nggak bakal dikompilasi. Karena slice berbagi data (materi Array &",
                    "     Slice), mengurutkannya juga mengubah slice lain yang menunjuk",
                    "     array yang sama. Pakai slices.Clone(s) dulu kalau yang asli masih",
                    "     dipakai.",
                    "",
                    "  4. slices.BinarySearch menganggap slice-nya udah urut. Kalau",
                    "     slice-nya acak, dia nggak error sama sekali, cuma jawabannya",
                    "     salah. Bug seperti ini paling susah kelihatan, karena nggak ada",
                    "     pesan apa pun.",
                    "",
                    "  5. comparable artinya \"bisa == dan !=\", bukan \"bisa dibandingkan",
                    "     besar-kecilnya\". Slice, map, dan func nggak comparable, jadi",
                    "     ketiganya juga nggak bisa jadi kunci map. Aturan kunci map di",
                    "     materi Map dan constraint ini membicarakan hal yang sama.",
                    "",
                    "Kapan jangan pakai generics",
                    "",
                    "Kalau yang kamu butuhkan cuma perilaku, interface udah cukup dan lebih",
                    "sederhana. Interface tetap cara utama di Go (materi Interface).",
                    "Generics baru lebih unggul kalau tipe konkretnya perlu dipertahankan:",
                    "masuk []int, keluar []int, bukan keluar []any yang harus di-assert",
                    "satu per satu. Pedoman di komunitas Go: tulis dulu kode biasa, dan",
                    "jadikan generik sesudah kamu betul-betul menulis fungsi kembar yang",
                    "ketiga.",
                    "",
                    "Sekilas iterator (range-over-func, Go 1.23)",
                    "",
                    "Di kode baru, kamu bakal makin sering melihat fungsi yang hasilnya",
                    "bisa langsung di-range:",
                    "",
                    "  for k := range maps.Keys(stok) { ... }",
                    "",
                    "maps.Keys nggak mengembalikan []string. Dia mengembalikan",
                    "iter.Seq[string], yaitu sebuah fungsi yang tahu cara menyebutkan",
                    "isinya satu per satu. Karena itu hasilnya nggak bisa dikasih len() dan",
                    "nggak bisa diindeks. Kalau kamu butuh slice sungguhan:",
                    "",
                    "  slices.Collect(maps.Keys(m))   jadi slice, urutannya acak seperti map",
                    "  slices.Sorted(maps.Keys(m))    jadi slice sekaligus terurut",
                    "",
                    "Kalau contoh dari internet gagal dengan pesan cannot range over ...",
                    "(value of type func(...)), hampir pasti versi Go di komputermu lebih",
                    "tua dari 1.23. Cek pakai go version.",
                ],
            },
        ],
    },
    {
        "title": "24. Package, Module & Testing",
        "sections": [
            {
                "body": [
                    "Module adalah satuan kode Go yang dibagikan dan dipasang sebagai satu",
                    "kesatuan. Satu module berisi satu atau banyak package.",
                    "",
                    "Cara memulai project baru:",
                    "  mkdir proyekku && cd proyekku",
                    "  go mod init github.com/namamu/proyekku",
                    "",
                    "Perintah itu membuat file go.mod. Isinya nama module, versi Go, dan",
                    "daftar dependensi, yaitu kode orang lain yang dipakai project-mu.",
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
                    "Aturan siapa boleh memakai apa",
                    "  Nama berawalan HURUF BESAR -> bisa diakses package lain",
                    "  Nama berawalan huruf kecil -> hanya di package sendiri",
                    "",
                    "  func Hitung()   publik",
                    "  func hitung()   privat",
                    "",
                    "Go nggak punya kata kunci public, private, atau protected. Huruf",
                    "pertama nama itulah yang menentukan.",
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
                    "  - Nama file harus diakhiri _test.go.",
                    "  - Nama fungsinya harus diawali Test.",
                    "  - Parameternya t *testing.T.",
                    "  - Kegagalan dilaporkan pakai t.Errorf atau t.Fatalf:",
                    "      t.Errorf  catat gagal, test LANJUT",
                    "      t.Fatalf  catat gagal, test BERHENTI",
                    "",
                    "Cara menjalankan test:",
                    "  go test              test di folder ini",
                    "  go test ./...        semua test di project",
                    "  go test -v           tampilkan detail tiap test",
                    "  go test -cover       tampilkan cakupan kode",
                    "  go test -run TestBagi  jalankan test tertentu saja",
                    "  go test -bench=.     jalankan benchmark, bukan cuma test",
                    "  go test -race        detektor race yang di materi Goroutine",
                    "                       & Channel kamu pakai lewat 'go run -race'",
                    "",
                    "Dua yang terakhir dibahas lengkap di materi Testing Lanjutan.",
                    "",
                    "Table-driven test",
                    "",
                    "Pola di contoh atas adalah gaya yang dipakai hampir semua programmer",
                    "Go. Semua kasus uji dikumpulkan dalam satu slice struct, lalu",
                    "diulang satu per satu. Kalau mau menambah kasus baru, cukup tambah",
                    "satu baris. Kamu nggak perlu menyalin seluruh fungsi test.",
                    "",
                    "Slice struct itu bentuknya struct anonim. Tipenya ditulis langsung di",
                    "tempat, tanpa type dan tanpa nama, karena cuma dipakai di satu fungsi",
                    "ini. Penjelasan bentuknya, termasuk arti }{ yang aneh itu, ada di",
                    "materi Struct & Method.",
                    "",
                    "t.Run membuat subtest yang punya nama. Jadi keluarannya nunjukin",
                    "persis kasus mana yang gagal.",
                    "",
                    "Susunan folder project Go yang umum:",
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
                    "Folder bernama internal diperlakukan khusus oleh Go. Package di",
                    "dalamnya nggak bisa diimpor dari luar module.",
                ]
            },
        ],
    },
    {
        "title": "25. Module, Import & Direktif Compiler",
        "sections": [
            {
                "body": [
                    "Kalau kamu membuka repo Go milik orang lain, dua hal pertama yang",
                    "kelihatan selalu sama: berkas go.mod di akar folder, dan blok import",
                    "5-20 baris di bagian atas tiap berkas. Materi Package, Module &",
                    "Testing udah nyuruh kamu menjalankan go mod init. Materi ini membahas",
                    "apa yang dihasilkan perintah itu, dan apa arti tiap baris di bagian",
                    "atas berkas.",
                    "",
                    "Nama module adalah awalan semua jalur import. Kalau baris pertama",
                    "go.mod berbunyi:",
                    "  module github.com/andi/tokoku",
                    "maka folder internal/hitung di dalam project itu diimpor sebagai:",
                    "  import \"github.com/andi/tokoku/internal/hitung\"",
                    "",
                    "Jalur import nggak dimulai dari nama folder di komputermu. Folder",
                    "project-nya boleh kamu taruh di ~/kerjaan/coba1, tapi namanya di mata",
                    "Go tetap github.com/andi/tokoku. Jalur relatif seperti",
                    "import \"./internal/hitung\" juga nggak ada di Go modern. Itu kebiasaan",
                    "dari Node atau Python, dan compiler Go menolaknya.",
                    "",
                    "Kenapa bentuknya mirip URL? Supaya perintah go bisa mengunduhnya",
                    "sendiri, kalau suatu hari kode itu dipublikasikan. Untuk project",
                    "pribadi yang nggak pernah diunggah, nama apa pun sah. Tapi biasakan",
                    "bentuk domain/nama, supaya nggak bentrok dengan module orang lain",
                    "waktu project-nya mulai dipakai bareng.",
                ],
            },
            {
                "heading": "Isi go.mod sebuah project sungguhan",
                "body": [
                    "Kita bahas baris demi baris:",
                    "",
                    "  module github.com/andi/tokoku",
                    "    Nama module. Ini awalan jalur import tadi.",
                    "",
                    "  go 1.22",
                    "    Versi bahasa Go yang dipakai project ini. Ini bukan versi",
                    "    compiler yang terpasang di komputermu. Fitur yang baru ada sejak",
                    "    1.21 ditolak kalau baris ini masih 1.19.",
                    "",
                    "  toolchain go1.23.4",
                    "    Versi compiler yang otomatis diunduh kalau punyamu lebih tua.",
                    "    Baris ini sering muncul sendiri sesudah go get, jadi biasanya",
                    "    bukan kamu yang ngetik.",
                    "",
                    "  require ( ... )",
                    "    Daftar dependensi beserta versinya. Yang dikasih komentar",
                    "    // indirect bukan kamu yang memakainya langsung. Dia dibutuhkan",
                    "    oleh dependensimu. Jangan dihapus manual: dia bakal balik",
                    "    sendiri, atau malah bikin build gagal.",
                    "",
                    "  replace github.com/andi/utilku => ../utilku",
                    "    Mengalihkan sebuah dependensi ke folder lokal. Berguna kalau kamu",
                    "    lagi menyunting dua project sekaligus. Masalahnya, baris ini",
                    "    sering lupa dihapus. Akibatnya kode gagal dibangun di komputer",
                    "    orang lain yang nggak punya folder itu.",
                    "",
                    "  exclude github.com/contoh/rusak v1.2.0",
                    "    Melarang satu versi tertentu dipakai, misalnya karena versi itu",
                    "    cacat.",
                    "",
                    "go.sum berisi hash tiap dependensi, dua baris per module. Hash itu",
                    "semacam sidik jari isi berkas. Gunanya memastikan isi paket v1.6.0",
                    "yang diunduh hari ini sama persis dengan yang dulu. Kalau ada yang",
                    "menukar isinya di server, build-nya gagal, dan kode asing itu nggak",
                    "ikut terpakai tanpa ketahuan. Jadi:",
                    "  - go.sum ikut di-commit ke git. Itu bukan berkas sampah.",
                    "  - Jangan pernah disunting tangan. go mod tidy yang mengurusnya.",
                    "",
                    "Versi semantik",
                    "",
                    "Nomor versi v1.6.0 dibaca mayor.minor.tambalan: mayor 1, minor 6,",
                    "tambalan 0. Kalau nomor mayor naik, pembuatnya boleh mengubah hal yang",
                    "bikin kode lama rusak. Karena itu Go memaksa satu aturan: mulai v2,",
                    "nomor mayornya ikut masuk ke jalur import.",
                    "  import \"github.com/gin-gonic/gin\"        library versi v1.x",
                    "  import \"github.com/redis/go-redis/v9\"    library versi v9.x",
                    "Akhiran /v2 atau /v9 itu penanda versi, bukan nama folder. Efeknya,",
                    "v1 dan v2 dari library yang sama bisa dipakai berdampingan dalam satu",
                    "program.",
                    "",
                    "Perintah yang menyunting go.mod dan go.sum untukmu:",
                    "  go get contoh.com/pkg@v1.2.3     tambah/pindahkan ke versi itu",
                    "  go get -u ./...                  naikkan ke versi minor terbaru",
                    "  go mod tidy                      tambah yang kurang, buang yang tak dipakai",
                    "  go mod download                  unduh ke cache, daftar tidak berubah",
                    "  go mod vendor                    salin semua dependensi ke vendor/",
                    "  go install contoh.com/alat@latest   pasang PROGRAM-nya, bukan jadi",
                    "                                      dependensi",
                    "",
                    "Beda yang sering bikin salah: go build menaruh binari di folder ini.",
                    "go install memasangnya ke folder bin milik Go, supaya bisa dipanggil",
                    "dari mana aja. Sejak Go 1.16, go get nggak lagi memasang program. Itu",
                    "tugas go install.",
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
                    "Ada dua hal yang perlu kamu perhatikan:",
                    "",
                    "  - Jalurnya \"contoh.dev/tokoku/internal/hitung\", yaitu nama module",
                    "    ditambah jalur folder. Bukan \"internal/hitung\", dan bukan juga",
                    "    jalur di hard disk.",
                    "  - Waktu memanggil, yang ditulis adalah nama package (harga), bukan",
                    "    nama folder terakhir (hitung). Keduanya boleh beda, dan di library",
                    "    sungguhan memang sering beda. Ini penyebab umum error",
                    "    undefined: hitung, padahal baris import-nya udah benar. Cara",
                    "    memastikannya: buka berkasnya, baca baris package-nya.",
                    "",
                    "    Sebaliknya, di kodemu sendiri samakan aja nama folder dan",
                    "    package, kecuali ada alasan kuat. Nggak ada untungnya bikin",
                    "    keduanya beda.",
                    "",
                    "Ada empat bentuk baris import:",
                    "",
                    "  import \"fmt\"                    biasa, dipanggil fmt.Println",
                    "  import f \"fmt\"                  alias, dipanggil f.Println",
                    "  import _ \"github.com/lib/pq\"    blank, tidak dipanggil sama sekali",
                    "  import . \"fmt\"                  dot, Println tanpa awalan apa pun",
                    "",
                    "Alias wajib dipakai kalau ada dua package yang nama akhirnya sama:",
                    "  import (",
                    "      \"database/sql\"",
                    "      xsql \"contoh.com/alat/sql\"",
                    "  )",
                    "Tanpa alias, keduanya sama-sama bernama sql, dan Go menolak berkasnya.",
                    "Di luar kasus bentrok itu, jangan pakai alias. Pembaca kodemu jadi",
                    "harus menghafal singkatan buatanmu untuk sesuatu yang udah punya nama",
                    "resmi.",
                    "",
                    "Dot import membuang awalan sama sekali. Kelihatannya praktis, tapi",
                    "pembaca kehilangan satu-satunya petunjuk dari mana sebuah nama",
                    "berasal. Nama dari package itu juga bisa bentrok dengan variabelmu",
                    "tanpa kamu sadari. Hampir semua tim melarangnya. Paling-paling kamu",
                    "cuma bakal menemuinya di berkas test.",
                    "",
                    "Urutan blok import yang dipakai hampir semua kode Go:",
                    "  import (",
                    "      \"fmt\"          kelompok pertama: package standar",
                    "      \"os\"",
                    "",
                    "      \"github.com/lib/pq\"                  kelompok kedua: pihak ketiga",
                    "      \"contoh.dev/tokoku/internal/hitung\"   dan package milik module sendiri",
                    "  )",
                    "Di dalam tiap kelompok, urutannya alfabetis. gofmt yang mengurutkan,",
                    "tapi dia nggak memindahkan baris antar kelompok. Baris kosong pemisah",
                    "itu kamu yang naruh. goimports, versi gofmt yang lebih pintar, juga",
                    "menambah import yang kurang dan membuang yang nggak dipakai. Pasang di",
                    "editormu dari sekarang.",
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
                    "Setiap kali program mulai, Go menjamin urutan ini:",
                    "  1. Semua package yang diimpor diinisialisasi lebih dulu, sampai",
                    "     tuntas.",
                    "  2. Di tiap package, variabel level package diisi.",
                    "  3. Lalu semua func init() di package itu jalan, urut berkas lalu urut",
                    "     baris.",
                    "  4. Paling akhir, baru func main() milik package main.",
                    "",
                    "Jadi aturan di Materi 1, \"func main() itu titik awal program\", benar",
                    "untuk kode yang kamu tulis. Tapi main bukan baris pertama yang",
                    "dijalankan mesin. Kalau kamu memasang titik henti di main dan heran",
                    "kenapa sebuah variabel udah terisi, jawabannya ada di init().",
                    "",
                    "Aturan init():",
                    "  - Nggak punya parameter dan nggak punya nilai balik. Ini nggak bisa",
                    "    diubah.",
                    "  - Nggak bisa dipanggil manual. Menulis init() di kodemu itu error.",
                    "  - Boleh lebih dari satu per package, bahkan lebih dari satu per",
                    "    berkas.",
                    "  - Cuma jalan sekali, berapa kali pun package itu diimpor.",
                    "",
                    "init() juga yang jadi alasan blank import ada:",
                    "  import _ \"github.com/lib/pq\"",
                    "Driver PostgreSQL itu nggak punya satu pun fungsi yang kamu panggil.",
                    "Yang kamu butuhkan cuma init()-nya. init() itu mendaftarkan driver ke",
                    "database/sql, supaya sql.Open(\"postgres\", ...) kenal nama \"postgres\".",
                    "Barisnya kelihatan seperti salah ketik atau sisa kode lama. Kalau kamu",
                    "menghapusnya, program tetap dikompilasi, tapi mati waktu jalan dengan",
                    "pesan unknown driver.",
                    "",
                    "Ini pengecualian yang sah dari aturan nomor 3 di Materi 1. Import yang",
                    "nggak dipakai memang error, kecuali kamu menamainya _, yang artinya",
                    "\"aku cuma butuh efek sampingnya\". Tanda _ itu blank identifier yang",
                    "sama dengan di Materi 5 (nama, _ := ...): artinya \"ada, tapi sengaja",
                    "nggak dipakai\". Bedanya, di sini yang diabaikan adalah nama package,",
                    "bukan nilai balik fungsi.",
                    "",
                    "Jangan pakai init() untuk pekerjaan berat seperti membaca berkas,",
                    "membuka koneksi, atau memanggil jaringan. init() jalan sebelum kamu",
                    "sempat menangani error apa pun. Test juga jadi susah dikendalikan,",
                    "karena init() nggak bisa dimatikan.",
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
                    "Sebagian komentar di Go ditulis untuk dibaca alat Go, dan manusia",
                    "cuma ikut membaca. Komentar seperti ini disebut direktif. Ada tiga",
                    "yang pasti kamu temui:",
                    "",
                    "  1. //go:build adalah syarat kapan berkas ini ikut dikompilasi.",
                    "     Ditulis di baris paling atas berkas, di atas package, dan wajib",
                    "     dipisah satu baris kosong:",
                    "       //go:build linux",
                    "",
                    "       package berkas",
                    "     Ada cara kedua, lewat akhiran nama berkas:",
                    "       simpan_linux.go     ikut dikompilasi hanya di Linux",
                    "       simpan_windows.go   ikut dikompilasi hanya di Windows",
                    "     Ini sebabnya dua berkas dalam satu folder boleh berisi fungsi",
                    "     dengan nama sama persis: keduanya nggak pernah dikompilasi",
                    "     bersamaan. Kalau sebuah fungsi \"hilang\" padahal berkasnya jelas",
                    "     ada di folder itu, dua hal ini yang pertama perlu diperiksa.",
                    "",
                    "  2. //go:embed memasukkan isi berkas ke variabel waktu kompilasi. Di",
                    "     contoh atas, pesan.txt jadi bagian dari binari, jadi programnya",
                    "     tetap jalan walaupun berkas aslinya dihapus. Dipakai untuk",
                    "     template HTML, berkas migrasi SQL, dan aset web, supaya hasil",
                    "     deploy tetap satu berkas. Syaratnya:",
                    "       - import \"embed\", blank kalau tipenya cuma string atau []byte,",
                    "       - komentarnya menempel tepat di atas var, tanpa baris kosong,",
                    "       - berkasnya ada di folder yang sama atau di bawahnya, bukan di",
                    "         atasnya.",
                    "",
                    "  3. //go:generate adalah perintah yang dijalankan kalau kamu ngetik",
                    "     go generate.",
                    "       //go:generate stringer -type=Status",
                    "     Perintah ini nggak ikut jalan waktu go build. Gunanya mencatat",
                    "     asal-usul berkas seperti status_string.go atau nama_gen.go.",
                    "     Berkas seperti itu dibuat mesin, jadi percuma kamu sunting",
                    "     isinya. Suntinganmu bakal tertimpa begitu ada yang menjalankan",
                    "     generate lagi. Berkas begitu biasanya diawali baris",
                    "     \"Code generated ... DO NOT EDIT.\"",
                    "",
                    "Mengompilasi untuk sistem lain",
                    "",
                    "Go bisa membuat program untuk sistem operasi lain tanpa perlu punya",
                    "mesinnya. Istilahnya cross-compile:",
                    "  GOOS=linux   GOARCH=amd64 go build -o server .",
                    "  GOOS=windows GOARCH=amd64 go build -o server.exe .",
                    "  GOOS=darwin  GOARCH=arm64 go build -o server .",
                    "Nilai GOOS dan GOARCH ini juga yang dibaca //go:build dan akhiran nama",
                    "berkas tadi. Satu perintah dari laptopmu menghasilkan binari untuk",
                    "server orang lain. Ini alasan Go disukai untuk program yang harus",
                    "disebar ke banyak mesin.",
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
                    "Di materi pertama disebut bahwa Go dipakai membangun \"layanan backend",
                    "berskala besar\". Tapi sampai sini, semua contohnya masih program",
                    "konsol yang mencetak ke layar lalu selesai. Bagian yang belum ada:",
                    "cara sebuah program Go menunggu permintaan, lalu menjawabnya. Program",
                    "seperti itu disebut server.",
                    "",
                    "Nggak ada yang perlu dipasang. Server HTTP-nya udah ada di pustaka",
                    "standar, di package net/http. Di bahasa lain kamu biasanya memasang",
                    "Tomcat, Apache, atau Express dulu. Di Go, satu berkas binari hasil",
                    "go build udah jadi server-nya sendiri.",
                    "",
                    "Server paling pendek yang bisa ditulis",
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
                    "Itu program yang utuh. Jalankan, buka http://127.0.0.1:8080 di",
                    "browser, dan kamu udah punya server.",
                    "",
                    "Bentuk fungsi handler",
                    "",
                    "Handler adalah fungsi yang menjawab satu permintaan. Bentuknya selalu",
                    "begini:",
                    "",
                    "  func(w http.ResponseWriter, r *http.Request)",
                    "",
                    "Hafalkan bentuk ini. Sesudah if err != nil, baris ini yang paling",
                    "sering muncul di kode Go sungguhan. Setiap library web yang bakal kamu",
                    "baca dibangun di sekitar bentuk ini.",
                    "",
                    "  w   Tempat kamu menulis jawaban. Dia sebuah io.Writer (lihat materi",
                    "      Berkas), jadi semua cara menulis ke berkas juga bisa dipakai",
                    "      di sini: fmt.Fprintf(w, ...), io.Copy(w, ...), dan",
                    "      json.NewEncoder(w).Encode(v). Perhatikan, w bukan pointer.",
                    "      http.ResponseWriter itu interface, dan nilai di dalamnya udah",
                    "      berupa pointer.",
                    "",
                    "  r   Permintaan yang masuk: method, alamat, header, dan isinya. r itu",
                    "      pointer (*http.Request), karena struct-nya besar. Menyalinnya",
                    "      untuk setiap permintaan itu boros (materi Pointer).",
                    "",
                    "Handler nggak mengembalikan apa pun. Nggak ada return jawaban. Kamu",
                    "menjawab dengan menulis ke w, dan permintaan dianggap selesai begitu",
                    "fungsinya berakhir.",
                    "",
                    "Jebakan: http.Error(w, ...) cuma menulis pesan gagal. Dia nggak",
                    "menghentikan handler-mu. Kalau kamu lupa nulis return sesudahnya,",
                    "satu permintaan dijawab dua kali.",
                    "",
                    "Kenapa ListenAndServe mengembalikan error",
                    "",
                    "ListenAndServe nggak pernah selesai dengan sukses. Dia berhenti di",
                    "baris itu selama server hidup. Dia baru kembali kalau ada yang salah,",
                    "misalnya port 8080 udah dipakai program lain, atau server sengaja",
                    "dimatikan. Karena itu jangan cuma dipanggil lalu dilupakan. Bentuk",
                    "yang benar:",
                    "",
                    "  log.Fatal(http.ListenAndServe(\"127.0.0.1:8080\", nil))",
                    "",
                    "Kalau nilai kembaliannya diabaikan, muncul bug yang paling bikin",
                    "bingung pemula: program langsung keluar tanpa satu pesan pun. Ternyata",
                    "port-nya udah dipakai, dan nggak ada yang membacakan error-nya.",
                    "",
                    "Catatan: contoh besar di bawah adalah server sungguhan. Dia nunggu",
                    "terus tanpa henti, dan memakai jaringan. Tombol Coba jalankan di",
                    "aplikasi ini bakal menggantung sampai batas waktu, lalu dihentikan",
                    "paksa. Itu bukan error di kodemu. Salin kodenya ke berkas main.go,",
                    "jalankan go run main.go di terminalmu sendiri, lalu panggil dari",
                    "browser atau curl. Contoh kedua sengaja dibikin berhenti sendiri, jadi",
                    "yang itu boleh kamu jalankan di sini.",
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
                    "Mengambil isi permintaan",
                    "",
                    "Semuanya ada di r. Yang ini dipakai hampir setiap hari:",
                    "",
                    "  r.Method                     \"GET\", \"POST\", \"PUT\", \"DELETE\",",
                    "                               selalu huruf besar",
                    "  r.URL.Path                   \"/barang/B001\", alamat tanpa ?query",
                    "  r.URL.Query().Get(\"q\")       dari /cari?q=beras menghasilkan \"beras\".",
                    "                               Kalau q memang tidak dikirim, hasilnya \"\",",
                    "                               bukan error, jadi kamu sendiri yang",
                    "                               memeriksa kosong atau tidak",
                    "  r.PathValue(\"kode\")          potongan yang ditangkap pola (Go 1.22+)",
                    "  r.Header.Get(\"Content-Type\") satu header, tidak peduli besar-kecil",
                    "                               hurufnya",
                    "  r.FormValue(\"nama\")          isian form HTML biasa",
                    "  r.Body                       isi permintaan, sebuah io.ReadCloser",
                    "",
                    "Semua yang datang dari alamat berbentuk string. Angka harus dikonversi",
                    "sendiri pakai strconv.Atoi (materi Angka & Waktu), dan hasilnya wajib",
                    "diperiksa. Pemakai bisa ngetik /barang?halaman=abc kapan aja.",
                    "",
                    "Untuk isi permintaan berformat JSON, r.Body cukup diserahkan ke",
                    "decoder (materi JSON & Struct Tag):",
                    "",
                    "  var b Barang",
                    "  if err := json.NewDecoder(r.Body).Decode(&b); err != nil {",
                    "      http.Error(w, \"JSON tidak sah\", http.StatusBadRequest)",
                    "      return",
                    "  }",
                    "",
                    "Kamu bakal sering lihat defer r.Body.Close() di kode orang. Itu nggak",
                    "salah, tapi di dalam handler hal itu nggak wajib. Server yang menutup",
                    "isi permintaan sesudah handler selesai. Yang betul-betul wajib adalah",
                    "resp.Body.Close() di sisi klien. Lihat contoh kedua.",
                    "",
                    "Menulis jawaban: tiga langkah, urutannya nggak boleh dibalik",
                    "",
                    "  1. w.Header().Set(\"Content-Type\", \"application/json\")",
                    "  2. w.WriteHeader(http.StatusCreated)",
                    "  3. json.NewEncoder(w).Encode(barang)",
                    "",
                    "Kenapa harus begitu? Jawaban HTTP dikirim sebagai aliran byte: baris",
                    "status dulu, lalu header, baru isinya. Begitu satu byte isi terkirim,",
                    "header-nya udah lewat di kabel, dan nggak bisa ditarik lagi.",
                    "",
                    "Ini yang terjadi kalau urutannya salah. Nggak ada satu pun yang jadi",
                    "error, dan itu yang bikin susah ditemukan:",
                    "  - Set() sesudah WriteHeader: header itu diabaikan tanpa kabar.",
                    "    Jawabannya terkirim tanpa Content-Type yang kamu pasang.",
                    "  - Menulis isi tanpa memanggil WriteHeader sama sekali: statusnya",
                    "    otomatis 200 OK. Praktis, tapi artinya handler yang gagal di",
                    "    tengah jalan udah telanjur mengirim 200 sebelum kamu sempat",
                    "    memasang 500.",
                    "  - WriteHeader dua kali: yang kedua diabaikan, dan server mencatat",
                    "    http: superfluous response.WriteHeader call di log. Kalau kamu",
                    "    lihat baris itu, biasanya ada return yang lupa ditulis.",
                    "",
                    "Kalau Content-Type nggak kamu pasang, net/http menebaknya dari 512",
                    "byte pertama isi jawaban. Untuk JSON, tebakannya selalu meleset jadi",
                    "text/plain, dan browser menampilkannya sebagai teks mentah, bukan",
                    "sebagai data. Jadi selalu pasang sendiri.",
                    "",
                    "Kode status: pakai konstantanya, jangan angkanya",
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
                    "w.WriteHeader(403) tetap jalan. Tapi konstanta lebih cepat dibaca",
                    "orang, dan salah ketiknya pasti ketahuan: 4o3 nggak bakal dikompilasi,",
                    "sedangkan 430 diterima begitu aja. Ingat pembagian besarnya: 4xx",
                    "artinya kesalahan pengirim, 5xx artinya kesalahan server. Membalas 500",
                    "untuk input yang salah bentuk bikin orang nyari bug di tempat yang",
                    "salah.",
                    "",
                    "ServeMux: tabel yang menentukan handler mana yang dipanggil",
                    "",
                    "Argumen kedua ListenAndServe yang tadi diisi nil artinya \"pakai",
                    "DefaultServeMux\". Itu mux global milik package net/http. Mux (singkatan",
                    "dari multiplexer) adalah tabel yang mencocokkan alamat dengan",
                    "handler-nya. Untuk belajar, DefaultServeMux praktis. Untuk program",
                    "sungguhan, hindari. Package mana pun yang kamu import, termasuk milik",
                    "orang lain, bisa ikut mendaftarkan rute di situ tanpa kamu tahu. Bikin",
                    "sendiri pakai http.NewServeMux(), lalu pasang di srv.Handler.",
                    "",
                    "Sejak Go 1.22, polanya boleh menyebut method dan menangkap potongan",
                    "alamat. Sebelumnya, semua orang menulis if r.Method != \"GET\" sendiri",
                    "di setiap handler, atau memasang router buatan pihak lain:",
                    "",
                    "  \"/\"                     penampung terakhir: cocok untuk semua alamat",
                    "                          yang tidak tertangkap pola lain",
                    "  \"GET /{$}\"              hanya \"/\" persis. Inilah halaman depan",
                    "  \"GET /barang/{kode}\"    satu potongan, dibaca r.PathValue(\"kode\")",
                    "  \"POST /barang\"          alamat sama, method beda, handler beda",
                    "  \"/statik/\"              berakhiran garis miring = seluruh cabangnya",
                    "  \"GET /berkas/{sisa...}\" menangkap SISA alamat, garis miringnya ikut",
                    "",
                    "Begitu method ditulis di pola, kamu dapat dua hal gratis:",
                    "  - POST ke \"GET /cari\" otomatis dibalas 405 Method Not Allowed,",
                    "    lengkap dengan header Allow. Kamu nggak perlu nulis sebaris pun.",
                    "  - Mendaftarkan \"GET /x\" otomatis melayani HEAD /x juga.",
                    "",
                    "Kalau dua pola sama-sama cocok, yang lebih spesifik menang:",
                    "\"/barang/B001\" mengalahkan \"/barang/{kode}\". Kalau ada dua pola yang",
                    "tumpang tindih tanpa ada yang lebih spesifik, program langsung panic",
                    "waktu pola itu didaftarkan, dan nggak nunggu sampai salah pilih waktu",
                    "melayani. Ini sengaja, supaya bug rute ketahuan sebelum server",
                    "menyala.",
                    "",
                    "http.Handler dan http.HandlerFunc",
                    "",
                    "Interface Handler cuma punya satu method, sesuai nasihat \"interface",
                    "sekecil mungkin\" di materi Interface:",
                    "",
                    "  type Handler interface {",
                    "      ServeHTTP(w http.ResponseWriter, r *http.Request)",
                    "  }",
                    "",
                    "mux, srv.Handler, dan hasil catat() di contoh atas semuanya Handler.",
                    "Lalu gimana caranya fungsi biasa bisa jadi Handler? Lewat lima baris",
                    "pendek di pustaka standar ini:",
                    "",
                    "  type HandlerFunc func(http.ResponseWriter, *http.Request)",
                    "",
                    "  func (f HandlerFunc) ServeHTTP(w http.ResponseWriter, r *http.Request) {",
                    "      f(w, r)",
                    "  }",
                    "",
                    "Itu tipe bentukan di atas tipe fungsi (materi Tipe Bentukan), lengkap",
                    "dengan method-nya sendiri. Jadi http.HandlerFunc(f) itu konversi tipe,",
                    "bukan pemanggilan fungsi. Fungsi biasa berubah jadi nilai yang punya",
                    "ServeHTTP, tanpa ada yang disalin. HandleFunc (tanpa huruf r) cuma",
                    "bentuk singkat yang lebih enak ditulis:",
                    "",
                    "  mux.HandleFunc(pola, f)  sama dengan  mux.Handle(pola, http.HandlerFunc(f))",
                    "",
                    "Middleware: handler yang membungkus handler lain",
                    "",
                    "Bentuknya selalu sama di mana-mana. Terima Handler, kembalikan",
                    "Handler:",
                    "",
                    "  func catat(next http.Handler) http.Handler",
                    "",
                    "Di dalamnya kamu boleh melakukan sesuatu sebelum next.ServeHTTP(w, r)",
                    "dan sesudahnya, seperti roti lapis. Pencatatan log, pemeriksaan token",
                    "login, pembatasan jumlah permintaan, dan pemulihan dari panic,",
                    "semuanya berbentuk begini. Karena yang masuk dan yang keluar sama-sama",
                    "Handler, middleware bisa ditumpuk:",
                    "",
                    "  srv.Handler = pulihDariPanic(catat(periksaLogin(mux)))",
                    "",
                    "Yang paling luar jalan lebih dulu, dan cuma dia yang bisa menangkap",
                    "panic dari semua yang ada di dalamnya. Karena itu pemulih panic hampir",
                    "selalu dipasang paling luar. Kalau dia ditaruh di dalam pencatat log,",
                    "panic yang terjadi di pencatat itu tetap merobohkan permintaannya.",
                    "",
                    "Satu permintaan, satu goroutine",
                    "",
                    "net/http menjalankan handler-mu di goroutine baru untuk setiap",
                    "permintaan yang masuk. Kamu nggak nulis satu pun kata go untuk itu,",
                    "dan nggak bisa mematikannya. Akibatnya, data apa pun yang dipakai",
                    "bersama oleh banyak permintaan wajib dijaga, sama seperti di materi",
                    "Goroutine & Channel. Karena itu Gudang di contoh atas memegang",
                    "sync.RWMutex, nggak cuma map polos. Map yang dibaca dan ditulis",
                    "bersamaan nggak cuma kadang-kadang salah. Go sengaja mendeteksinya,",
                    "lalu mematikan seluruh program:",
                    "",
                    "  fatal error: concurrent map writes",
                    "",
                    "RWMutex dipakai, bukan Mutex biasa, karena membaca boleh berbarengan:",
                    "  RLock/RUnlock  banyak pembaca sekaligus, tidak saling menunggu",
                    "  Lock/Unlock    satu penulis, semua yang lain menunggu",
                    "Buktikan sendiri dengan: go run -race main.go",
                    "",
                    "r.Context() memberi context milik satu permintaan itu (materi",
                    "context). Context ini batal sendiri begitu kliennya memutus koneksi,",
                    "misalnya tab ditutup, jaringan putus, atau kliennya sendiri kehabisan",
                    "waktu. Teruskan context ini ke setiap pekerjaan berat:",
                    "",
                    "  ctx := r.Context()",
                    "  baris, err := db.QueryContext(ctx, \"SELECT ...\")",
                    "",
                    "Tanpa itu, query untuk halaman yang udah nggak ditunggu siapa pun",
                    "tetap jalan sampai habis. Sepuluh ribu permintaan batal yang tetap",
                    "dikerjakan seperti itu bisa bikin server yang sibuk mati pelan-pelan.",
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
                    "Sisi klien: programmu memanggil server lain",
                    "",
                    "Go yang sama juga bisa jadi klien, yaitu pihak yang mengirim",
                    "permintaan. Bentuknya cuma tiga baris. Yang penting adalah apa yang",
                    "wajib menyertainya:",
                    "",
                    "  resp, err := klien.Get(alamat)",
                    "  if err != nil { return err }",
                    "  defer resp.Body.Close()",
                    "",
                    "Ada tiga jebakan di tiga baris itu:",
                    "",
                    "  1. err == nil belum tentu berhasil. 404 dan 500 itu jawaban yang",
                    "     sampai dengan selamat, jadi err-nya nil. err cuma terisi kalau",
                    "     koneksinya yang gagal: nama domain nggak ketemu, koneksi ditolak,",
                    "     atau waktunya habis. Yang menentukan berhasil atau nggak adalah",
                    "     resp.StatusCode. Ini beda besar dari banyak library di bahasa lain",
                    "     yang melempar exception untuk status 4xx dan 5xx.",
                    "",
                    "  2. Body yang nggak ditutup bikin koneksi bocor. Setiap resp memegang",
                    "     satu koneksi TCP sampai body-nya dibaca habis dan ditutup. Tutup",
                    "     walaupun isinya sama sekali nggak kamu pakai. Dan jangan nulis",
                    "     defer resp.Body.Close() di dalam perulangan. defer baru jalan",
                    "     waktu fungsinya selesai, bukan waktu satu putaran selesai. Seribu",
                    "     putaran artinya seribu body terbuka nganggur sampai akhir. Karena",
                    "     itu contoh di atas menutupnya langsung, tanpa defer.",
                    "",
                    "  3. http.Get() dan http.Post() memakai klien bawaan yang nggak punya",
                    "     batas waktu sama sekali. Server yang macet bakal bikin programmu",
                    "     ikut macet, selamanya, tanpa satu pesan pun. Selalu bikin klien",
                    "     sendiri:",
                    "",
                    "       klien := &http.Client{Timeout: 5 * time.Second}",
                    "",
                    "Sesudah itu, resp.Body cuma io.Reader biasa. io.ReadAll(resp.Body)",
                    "mengambil semuanya sebagai []byte. Kalau jawabannya JSON, serahkan",
                    "langsung ke json.NewDecoder(resp.Body).Decode(&v). Untuk panggilan",
                    "yang harus bisa dibatalkan, pakai http.NewRequestWithContext, lalu",
                    "klien.Do(req).",
                    "",
                    "&http.Server: kapan berhenti memakai ListenAndServe polos",
                    "",
                    "http.ListenAndServe(alamat, nil) nggak punya satu pun batas waktu.",
                    "Satu klien jahat, atau cuma jaringan yang jelek, bisa membuka koneksi",
                    "lalu mengirim satu byte per menit, dan menahan sumber daya server",
                    "selamanya. Di produksi, bentuk yang dipakai selalu struct-nya:",
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
                    "Alamat \":8080\" tanpa host artinya mendengarkan di semua antarmuka",
                    "jaringan. Setiap perangkat di WiFi yang sama bisa menghubunginya.",
                    "\"127.0.0.1:8080\" cuma bisa dihubungi dari komputermu sendiri. Selama",
                    "masih belajar, pakai yang kedua. Server latihan yang nggak sengaja",
                    "terbuka ke jaringan adalah salah satu cara orang kebobolan.",
                    "",
                    "Berhenti dengan rapi",
                    "",
                    "Ctrl+C membunuh proses seketika, dan memotong permintaan yang masih",
                    "setengah jalan. srv.Shutdown(ctx) menghentikannya dengan sopan: tolak",
                    "sambungan baru, lalu tunggu yang sedang dilayani selesai. ctx-nya",
                    "adalah batas sabar menunggu. Kalau waktunya habis, Shutdown",
                    "mengembalikan error, dan sisanya memang dipotong.",
                    "",
                    "Begitu Shutdown dipanggil, ListenAndServe yang tadinya nunggu langsung",
                    "kembali dengan error http.ErrServerClosed. Itu bukan kegagalan. Itu",
                    "kabar bahwa perintahmu udah dikerjakan. Karena itu pemeriksaannya",
                    "selalu ditulis begini:",
                    "",
                    "  if err := srv.ListenAndServe(); err != nil && err != http.ErrServerClosed {",
                    "      log.Fatal(err)",
                    "  }",
                    "",
                    "Yang sengaja nggak dibahas di sini",
                    "",
                    "net/http udah cukup untuk server sungguhan. Framework seperti Gin,",
                    "Echo, atau Chi bikin kerja lebih nyaman, tapi nggak menambah",
                    "kemampuan baru. Semuanya dibangun di atas http.Handler yang sama, dan",
                    "middleware mereka bentuknya persis seperti catat() tadi. Kalau bagian",
                    "ini udah kamu pahami, membaca kode framework mana pun tinggal soal",
                    "mengenali nama-nama baru.",
                    "",
                    "Satu pertanyaan sengaja belum dijawab di sini, yaitu cara menguji",
                    "handler tanpa menyalakan server dan tanpa menyentuh jaringan sama",
                    "sekali. Alatnya package net/http/httptest, dan itu dibahas di materi",
                    "berikutnya.",
                ],
            },
        ],
    },
    {
        "title": "27. Testing Lanjutan: Benchmark, Example & httptest",
        "sections": [
            {
                "body": [
                    "Materi Package, Module & Testing ngenalin satu bentuk fungsi:",
                    "func TestX(t *testing.T). Kalau kamu buka berkas _test.go di proyek Go",
                    "sungguhan, kamu bakal lihat empat bentuk lain di sebelahnya.",
                    "",
                    "Lima fungsi yang dikenali go test",
                    "",
                    "  func TestX(t *testing.T)        memeriksa benar atau salah",
                    "  func BenchmarkX(b *testing.B)   mengukur cepat atau lambat",
                    "  func ExampleX()                 contoh pemakaian yang IKUT DIUJI",
                    "  func FuzzX(f *testing.F)        mencari masukan yang merusak",
                    "  func TestMain(m *testing.M)     satu kali setup & bersih-bersih",
                    "",
                    "Yang dikenali cuma nama yang bentuknya persis begitu. Huruf sesudah",
                    "kata Test wajib huruf besar. func Testkecil(t *testing.T) nggak pernah",
                    "dijalankan, dan go test nggak protes sama sekali. Dia lulus dengan",
                    "tenang tanpa menyentuh test itu. Yang bisa menangkapnya go vet:",
                    "",
                    "  Testkecil has malformed name: first letter after 'Test' must not",
                    "  be lowercase",
                    "",
                    "Ini alasan nyata kenapa go vet ./... perlu dijalankan: test yang",
                    "nggak pernah jalan kelihatan persis sama dengan test yang lulus.",
                    "",
                    "Empat alat di t yang belum pernah dipakai",
                    "",
                    "  t.Helper()    'aku cuma pembantu, jangan tunjuk baris di dalamku'",
                    "  t.Parallel()  'aku boleh jalan berbarengan dengan test lain'",
                    "  t.Cleanup(f)  jalankan f saat test ini selesai, lulus maupun gagal",
                    "  t.Skip(...)   berhenti dan tandai dilewati, bukan gagal atau lulus",
                    "",
                    "t.Helper() yang paling sering menghemat waktu. Tanpa itu, setiap",
                    "kegagalan yang lewat sebuah fungsi bantu bakal menunjuk baris t.Errorf",
                    "di dalam fungsi bantu itu. Barisnya sama untuk sepuluh kasus yang",
                    "beda, jadi kamu nggak tahu kasus mana yang gagal.",
                    "",
                    "t.Cleanup bisa didaftarkan dari dalam fungsi bantu, dan baru jalan",
                    "sesudah test beserta semua subtest-nya selesai. defer di dalam fungsi",
                    "bantu nggak bisa begitu: dia langsung jalan begitu fungsi bantunya",
                    "selesai, padahal test-nya masih butuh yang dia bereskan.",
                    "",
                    "Package berakhiran _test",
                    "",
                    "Berkas teks_test.go boleh mendeklarasikan package teks (di dalam) atau",
                    "package teks_test (di luar). Cuma berkas _test.go yang boleh punya",
                    "package kedua seperti ini. Di tempat lain, Go melarangnya.",
                    "",
                    "  package teks       boleh menyentuh fungsi privat huruf kecil",
                    "  package teks_test  wajib mengimpor 'contoh/teks', dan hanya bisa",
                    "                     memakai nama yang huruf depannya besar",
                    "",
                    "Kalau bisa, pilih yang di luar. Yang diuji jadi bagian yang memang",
                    "dipakai orang lain, bukan isi dalam yang bebas kamu ubah besok pagi.",
                    "Cara ini juga satu-satunya jalan keluar dari import cycle, yaitu dua",
                    "package yang saling mengimpor. Contohnya, test butuh package yang",
                    "justru mengimpor package yang sedang diuji.",
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
                    "Menjalankan benchmark",
                    "",
                    "Benchmark adalah test yang mengukur kecepatan.",
                    "",
                    "  go test -bench=.            jalankan semua benchmark",
                    "  go test -bench=Balik        yang namanya cocok pola saja",
                    "  go test -bench=. -benchmem  tambahkan kolom memori",
                    "  go test -bench=. -run=^$    benchmark saja, semua test dilewati",
                    "",
                    "Tanpa -bench, benchmark nggak dijalankan sama sekali. Itu disengaja.",
                    "Mengukur waktu itu lama, jadi Go nggak melakukannya kecuali diminta.",
                    "Pola -run=^$ artinya \"jalankan test yang namanya cocok dengan pola",
                    "kosong\". Nggak ada yang cocok, jadi yang tersisa tinggal",
                    "benchmark-nya.",
                    "",
                    "Keluaran sungguhannya:",
                    "",
                    "  goos: linux",
                    "  goarch: amd64",
                    "  pkg: contoh/teks",
                    "  BenchmarkBalik-8    47832    32569 ns/op    2560 B/op    2 allocs/op",
                    "",
                    "Cara membacanya dari kiri:",
                    "  BenchmarkBalik-8   nama, lalu jumlah inti (GOMAXPROCS), bukan hasil",
                    "  47832              berapa kali fungsinya dipanggil; ini b.N terakhir",
                    "  32569 ns/op        nanodetik per satu panggilan",
                    "  2560 B/op          byte yang dialokasikan per panggilan",
                    "  2 allocs/op        berapa KALI alokasi terjadi per panggilan",
                    "",
                    "Alokasi artinya program minta tempat baru di memori. Angka-angka tadi",
                    "beda di tiap komputer, dan beda tiap kali dijalankan. Yang penting",
                    "adalah perbandingan sebelum dan sesudah kamu mengubah kode, nggak",
                    "angkanya sendiri. allocs/op sering lebih berguna daripada ns/op.",
                    "Jumlah alokasi bisa dihitung dan stabil, sedangkan waktu ikut",
                    "naik-turun tergantung beban komputer.",
                    "",
                    "Kenapa ada b.N",
                    "",
                    "Kamu nggak pernah mengisi b.N sendiri. Yang mengisinya Go: fungsimu",
                    "dipanggil 1 kali, lalu 100, lalu 10.000, naik terus sampai total",
                    "waktunya cukup lama untuk diukur dengan jujur (bawaannya sekitar 1",
                    "detik). Satu panggilan saja terlalu cepat, karena jam komputer nggak",
                    "sehalus itu.",
                    "",
                    "Akibatnya, isi benchmark wajib berbentuk:",
                    "",
                    "  for i := 0; i < b.N; i++ { ... }",
                    "",
                    "Tiga kesalahan yang sering terjadi:",
                    "  - Menulis i < 1000 dan mengabaikan b.N. Go tetap membagi total",
                    "    waktunya dengan b.N, jadi angka ns/op yang keluar ngawur.",
                    "  - Menaruh persiapan berat di dalam loop, sehingga yang terukur",
                    "    malah persiapannya. Obatnya: panggil b.ResetTimer() sesudah",
                    "    persiapan.",
                    "  - Membuang hasil panggilan. Compiler boleh menghapus perhitungan",
                    "    yang hasilnya nggak dipakai, dan benchmark-nya jadi mengukur",
                    "    kekosongan. Karena itu contoh di atas menyimpan hasilnya ke",
                    "    var simpan string di tingkat package.",
                    "",
                    "  b.ResetTimer()   nol-kan stopwatch, buang waktu persiapan",
                    "  b.StopTimer()    jeda di tengah loop kalau ada persiapan per iterasi",
                    "  b.StartTimer()   lanjutkan lagi",
                    "  b.ReportAllocs() paksa kolom B/op dan allocs/op muncul",
                    "",
                    "Perintah lain yang dipakai sehari-hari",
                    "",
                    "  go test -short           lewati yang dijaga testing.Short()",
                    "  go test -race            detektor race; 2-10x lebih lambat, pakai di CI",
                    "  go test -cover           persentase pernyataan yang tersentuh",
                    "  go test -coverprofile=cover.out ./...",
                    "  go tool cover -func=cover.out          rincian per fungsi",
                    "  go tool cover -html=cover.out -o cover.html    warnai baris di browser",
                    "  go test -fuzz=FuzzBalik -fuzztime=30s",
                    "",
                    "Cakupan (coverage) artinya berapa persen baris kodemu yang pernah",
                    "dijalankan oleh test. Rincian -func bentuknya begini. Justru kolom",
                    "yang belum 100% yang berguna, karena kolom itu nunjukin cabang kode",
                    "yang belum pernah dijalankan:",
                    "",
                    "  contoh/web/handler.go:15:  Halo          100.0%",
                    "  contoh/web/handler.go:27:  AmbilPesan     75.0%",
                    "  total:                     (statements)   85.7%",
                    "",
                    "Cakupan tinggi nggak membuktikan kodenya benar. Cakupan cuma",
                    "membuktikan barisnya pernah dijalankan. Baris yang dijalankan tanpa",
                    "satu pun pemeriksaan tetap dihitung 100%.",
                    "",
                    "Example: dokumentasi yang nggak bisa basi",
                    "",
                    "Komentar // Output: di akhir ExampleBalik itu ada fungsinya. Keluaran",
                    "fungsi itu ditangkap, lalu dibandingkan dengan isi komentarnya. Jadi",
                    "contoh yang udah nggak cocok dengan kodenya bakal gagal, dan nggak",
                    "bisa ketinggalan zaman tanpa ketahuan seperti contoh di README.",
                    "",
                    "Aturannya:",
                    "  - Nama sesudah Example harus menunjuk nama yang memang ada:",
                    "    ExampleBalik untuk func Balik, ExampleAntre_Ambil untuk method",
                    "    Ambil pada tipe Antre. Nama karangan ditegur go vet.",
                    "  - Varian kedua ditambahi garis bawah dan huruf kecil:",
                    "    ExampleBalik_kosong.",
                    "  - Pakai // Unordered output: kalau urutan barisnya nggak dijamin.",
                    "  - Contoh tanpa komentar Output tetap dikompilasi, tapi nggak pernah",
                    "    dijalankan. Ini jebakan yang nggak bersuara: kamu merasa punya",
                    "    test, padahal yang kamu punya cuma kode yang lolos compiler.",
                    "",
                    "Yang menampilkan Example sebagai contoh siap salin adalah dokumentasi",
                    "web-nya (pkg.go.dev atau perkakas godoc). Perintah go doc di terminal",
                    "nggak menampilkannya. go doc -all cuma menampilkan komentar",
                    "dokumentasinya.",
                    "",
                    "Fuzzing: mencari masalah, bukan membuktikan benar",
                    "",
                    "Fuzzing artinya Go mengarang masukan acak untuk mencari yang bikin",
                    "kodemu rusak. Tanpa -fuzz, FuzzBalik cuma menjalankan masukan awal",
                    "(benih) dari f.Add. Dengan -fuzz, Go terus-menerus mengarang masukan",
                    "baru, dan menyimpan yang menambah cakupan. Contoh di atas gagal dalam",
                    "hitungan detik:",
                    "",
                    "  --- FAIL: FuzzBalik",
                    "      dibalik dua kali harusnya kembali ke \"\\xc8\"",
                    "      Failing input written to testdata/fuzz/FuzzBalik/d6be63583e2876b0",
                    "",
                    "Fuzzer-nya nggak sedang rewel. []rune mengubah byte yang bukan UTF-8",
                    "sah jadi U+FFFD, jadi Balik memang nggak bisa mengembalikannya. Ini",
                    "bug sungguhan, yang nggak bakal kepikiran kalau kamu cuma nebak",
                    "sendiri.",
                    "",
                    "Jebakan berikutnya: berkas di testdata/fuzz itu jadi kasus uji",
                    "permanen. Sejak saat itu, go test biasa pun ikut gagal terus, sampai",
                    "bug-nya diperbaiki atau berkas korpusnya dihapus. Itu memang sengaja,",
                    "supaya bug yang udah ketemu nggak bisa dilupakan.",
                    "",
                    "t.Parallel() dan akibatnya",
                    "",
                    "Test yang memanggil t.Parallel() ditahan dulu, lalu dilepas",
                    "bersama-sama sesudah test yang berurutan selesai. Untungnya jelas,",
                    "tapi ada harganya:",
                    "  - Test yang berbagi variabel global tiba-tiba saling menimpa.",
                    "  - Test yang mengubah folder kerja atau environment ikut merusak",
                    "    test di sebelahnya. Untuk folder sementara, pakai t.TempDir.",
                    "    Untuk environment, pakai t.Setenv, jangan os.Setenv. Tapi",
                    "    t.Setenv bakal panic di test yang memanggil t.Parallel, jadi test",
                    "    yang mengubah environment jangan dijadikan paralel.",
                    "  - Urutan keluaran -v jadi selang-seling. Itu bukan tanda ada yang",
                    "    rusak.",
                    "",
                    "Pasangkan dengan go test -race. Ini detektor yang sama dengan yang di",
                    "materi Goroutine & Channel dipanggil lewat go run -race. Dengan begitu,",
                    "data yang dipakai berbarengan ketahuan sebagai laporan race yang",
                    "menyebut baris dan goroutine-nya. Kalau nggak, yang kamu lihat cuma",
                    "kegagalan aneh yang muncul sekali sebulan.",
                    "",
                    "Sejak Go 1.22, variabel perulangan dibuat ulang di tiap putaran. Jadi",
                    "baris k := k yang dulu wajib sebelum t.Run + t.Parallel sekarang udah",
                    "nggak perlu. Kalau kamu melihatnya di kode lama, itu bukan kesalahan.",
                    "Itu jejak Go versi lama.",
                ],
            },
            {
                "heading": "Menguji HTTP tanpa membuka satu port pun",
                "body": [
                    "Handler HTTP dan mux-nya udah dibahas di materi Server HTTP dengan",
                    "net/http. Pertanyaan di sini beda: gimana cara mengujinya?",
                    "",
                    "Godaan pertamanya biasanya menyalakan server sungguhan di port 8080,",
                    "lalu memanggilnya dari test. Hasilnya berantakan. Port-nya bisa udah",
                    "dipakai program lain. Test yang jalan paralel saling rebutan port. Dan",
                    "kalau satu test lupa mematikan server-nya, test berikutnya gagal",
                    "karena alasan yang nggak ada hubungannya sama kode yang lagi diuji.",
                    "",
                    "Package net/http/httptest menyediakan tiga hal:",
                    "",
                    "  httptest.NewRequest(metode, url, badan)  permintaan palsu",
                    "  httptest.NewRecorder()   penampung jawaban; punya .Code, .Header(),",
                    "                           dan .Body, semua bisa diperiksa langsung",
                    "  httptest.NewServer(h)    server sungguhan di 127.0.0.1, port pilihan",
                    "                           sistem, hidup selama test saja",
                    "",
                    "Dua yang pertama untuk menguji handler buatanmu, tanpa membuka satu",
                    "port pun. Handler itu cuma fungsi biasa, jadi panggil aja langsung",
                    "seperti fungsi lain. Yang ketiga untuk menguji klien buatanmu. Klien",
                    "butuh lawan bicara, dan srv.URL memberi alamat yang hidup. Selalu",
                    "pasangkan dengan defer srv.Close(). Kalau nggak, server-nya numpuk",
                    "sampai semua test selesai.",
                    "",
                    "Syarat yang gampang dilupakan: alamat server-nya harus jadi parameter,",
                    "bukan konstanta di dalam fungsi. Fungsi yang menulis alamat",
                    "produksinya langsung di dalam badannya nggak mungkin diuji tanpa",
                    "internet. Yang diuji jadinya keadaan jaringanmu, bukan kodemu.",
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
                    "Folder testdata",
                    "",
                    "Perkakas Go mengabaikan folder bernama testdata. Isinya nggak pernah",
                    "dikompilasi, nggak ikut go build ./..., dan namanya nggak dianggap",
                    "package. Folder ini tempat resmi untuk menaruh berkas contoh: sampel",
                    "JSON, potongan CSV, gambar rusak untuk diuji, apa aja.",
                    "",
                    "  lapor/",
                    "    lapor.go",
                    "    lapor_test.go",
                    "    testdata/",
                    "      laporan.golden",
                    "",
                    "Waktu test jalan, folder kerjanya selalu folder package itu sendiri.",
                    "Jadi testdata/laporan.golden selalu benar, dari folder mana pun kamu",
                    "ngetik go test.",
                    "",
                    "Berkas golden",
                    "",
                    "Untuk keluaran yang panjang, seperti laporan, HTML, atau JSON, menulis",
                    "harapannya di dalam kode itu menyiksa dan susah dibaca. Caranya:",
                    "simpan keluaran yang udah kamu periksa sendiri ke sebuah berkas yang",
                    "disebut berkas golden. Test tinggal membandingkan hasilnya dengan",
                    "berkas itu.",
                    "",
                    "Flag -update di contoh ini dibuat sendiri pakai package flag, bukan",
                    "bawaan Go. Karena itu letaknya di baris perintah gampang salah:",
                    "",
                    "  go test -update ./lapor/    SALAH -> no Go files in ...",
                    "  go test ./lapor/ -update    benar: flag milik binari test di belakang",
                    "",
                    "Satu lagi yang sering makan waktu: -update menulis berkasnya, tapi",
                    "nggak membuat foldernya. Kalau testdata/ belum ada, yang keluar cuma",
                    "pesan no such file or directory. Buat sekali aja: mkdir testdata",
                    "",
                    "Ada satu kebiasaan yang wajib menyertainya. -update bikin test selalu",
                    "lulus, karena harapannya baru aja ditimpa hasilnya sendiri. Baca",
                    "git diff berkas golden-nya sebelum commit. Kalau nggak, sebuah bug bisa",
                    "berubah jadi perilaku yang dianggap benar oleh test-mu tanpa kamu",
                    "sadari.",
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
                    "Di materi ini, semua yang udah kamu pelajari digabung jadi satu program",
                    "utuh: sistem inventaris barang sederhana. Inventaris itu catatan barang",
                    "yang dimiliki sebuah toko, lengkap dengan stok dan nilainya.",
                    "",
                    "Konsep yang dipakai:",
                    "  - struct dan method",
                    "  - interface untuk laporan (method String() bikin Barang memenuhi",
                    "    interface Stringer)",
                    "  - map untuk penyimpanan",
                    "  - slice dan sort untuk urutan yang stabil",
                    "  - error kustom dan errors.Is",
                    "  - pointer receiver untuk mengubah data",
                    "  - fmt.Printf untuk keluaran berformat",
                    "",
                    "Perhatikan cara kunci map dikumpulkan lalu diurutkan sebelum dicetak.",
                    "Urutan isi map di Go berubah-ubah tiap kali program dijalankan. Kalau",
                    "kuncinya nggak diurutkan dulu, urutan keluarannya ikut berubah-ubah.",
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
                    "Beberapa keputusan desain di program itu, beserta alasannya:",
                    "",
                    "1. map[string]*Barang menyimpan pointer ke Barang, bukan nilai Barang",
                    "   itu sendiri. Kalau yang disimpan nilainya, b.Stok -= jumlah cuma",
                    "   mengubah salinan, dan data aslinya nggak ikut berubah.",
                    "2. Method Tambah bikin salinan dulu:",
                    "     salinan := b",
                    "     i.barang[b.Kode] = &salinan",
                    "   Dengan begitu, pemanggil nggak ikut memegang pointer ke data di",
                    "   dalam inventaris.",
                    "3. kodeTerurut() dipanggil di semua tempat yang mencetak. Urutan map",
                    "   yang acak gampang jadi sumber bug yang susah dilacak, apalagi waktu",
                    "   kamu menulis test.",
                    "4. Error dibungkus pakai %w, supaya errors.Is tetap bisa mengenalinya.",
                    "   Sekalian, pesan errornya dapat tambahan konteks yang berguna buat",
                    "   orang yang membacanya.",
                    "5. Method String() bikin Barang otomatis tercetak rapi lewat",
                    "   fmt.Println, tanpa fungsi tambahan.",
                    "",
                    "Mau melanjutkan sendiri? Ini beberapa idenya. Bahan untuk tiap butir",
                    "udah ada materinya:",
                    "  - Simpan data ke berkas JSON pakai encoding/json. Struct tag,",
                    "    Marshal, dan Unmarshal ada di materi JSON & Struct Tag.",
                    "  - Pakai sync.RWMutex supaya inventarisnya aman dipakai banyak",
                    "    goroutine sekaligus. RWMutex, Once, dan atomic ada di materi Pola",
                    "    Goroutine.",
                    "  - Tambah antarmuka baris perintah dengan subperintah tambah, ambil,",
                    "    dan daftar. os.Args, flag, dan log ada di materi Program Baris",
                    "    Perintah.",
                    "  - Tulis unit test untuk Ambil dan StokMenipis dengan gaya",
                    "    table-driven dari materi Package, Module & Testing.",
                    "  - Tambah pencatatan riwayat transaksi.",
                ]
            },
        ],
    },
]
