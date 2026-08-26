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
        "title": "4. Input & Output dengan fmt",
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
        "title": "5. Percabangan (if & switch)",
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
                    "       switch hari := waktu.Weekday(); hari {",
                    "",
                    "  6. Type switch untuk memeriksa tipe di balik interface:",
                    "       switch v := x.(type) {",
                    "       case int:    fmt.Println(\"int:\", v)",
                    "       case string: fmt.Println(\"string:\", v)",
                    "       }",
                ]
            },
        ],
    },
    {
        "title": "6. Perulangan (for)",
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
        "title": "7. Array & Slice",
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
                    "Slice dua dimensi:",
                    "  matriks := [][]int{{1, 2}, {3, 4}}",
                    "  fmt.Println(matriks[1][0])   -> 3",
                ]
            },
        ],
    },
    {
        "title": "8. Map",
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
                ]
            },
        ],
    },
    {
        "title": "9. Fungsi",
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
                    "5. defer menunda eksekusi sampai fungsi selesai:",
                    "     f, _ := os.Open(\"data.txt\")",
                    "     defer f.Close()",
                    "   Baris Close dijamin jalan walau terjadi error di",
                    "   tengah jalan. Beberapa defer dijalankan terbalik,",
                    "   yang terakhir didaftarkan jalan duluan.",
                    "",
                    "6. Nama berhuruf besar = publik (bisa diakses package",
                    "   lain). Berhuruf kecil = privat. Ini menggantikan",
                    "   kata kunci public/private.",
                ]
            },
        ],
    },
    {
        "title": "10. Pointer",
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
        "title": "11. Struct & Method",
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
        "title": "12. Interface",
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
                ]
            },
        ],
    },
    {
        "title": "13. Error Handling",
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
        "title": "14. Goroutine & Channel",
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
        "title": "15. Package, Module & Testing",
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
                    "",
                    "TABLE-DRIVEN TEST",
                    "Pola di contoh atas adalah gaya resmi komunitas Go:",
                    "kumpulkan semua kasus uji dalam satu slice struct,",
                    "lalu ulangi. Menambah kasus baru cukup menambah",
                    "satu baris, bukan menyalin seluruh fungsi test.",
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
        "title": "16. Studi Kasus: Manajemen Inventaris",
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
                    "Lanjutan yang bisa kamu coba sendiri:",
                    "  - Simpan data ke file JSON dengan encoding/json",
                    "  - Tambah antarmuka baris perintah interaktif",
                    "  - Tulis unit test untuk Ambil dan StokMenipis",
                    "  - Ubah agar aman dipakai banyak goroutine",
                    "    dengan sync.RWMutex",
                    "  - Tambah pencatatan riwayat transaksi",
                ]
            },
        ],
    },
]
