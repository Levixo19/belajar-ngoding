GO_EXERCISES = [
    {
        "title": "Latihan 1: Halo, Nama!",
        "difficulty": "Mudah",
        "question": [
            "Buat program Go yang menampilkan tepat dua baris:",
            "  Halo, namaku Andi!",
            "  Aku sedang belajar Go.",
        ],
        "hints": [
            "Setiap program eksekutabel dimulai dengan: package main",
            "Butuh import \"fmt\" untuk mencetak ke layar.",
            "Gunakan fmt.Println() untuk tiap baris.",
        ],
        "solution": """package main

import "fmt"

func main() {
	fmt.Println("Halo, namaku Andi!")
	fmt.Println("Aku sedang belajar Go.")
}""",
    },
    {
        "title": "Latihan 2: Kalkulator Sederhana",
        "difficulty": "Mudah",
        "question": [
            "Buat dua variabel a = 15 dan b = 4.",
            "Tampilkan hasil operasi dengan format persis:",
            "  15 + 4 = 19",
            "  15 - 4 = 11",
            "  15 * 4 = 60",
            "  15 / 4 = 3",
            "  15 % 4 = 3",
            "  15 / 4 = 3.75 (desimal)",
        ],
        "hints": [
            "Gunakan bentuk singkat: a, b := 15, 4",
            "Pembagian dua int menghasilkan int, sisanya dibuang.",
            "Untuk desimal, konversi dulu: float64(a) / float64(b), cetak dengan %.2f",
        ],
        "solution": """package main

import "fmt"

func main() {
	a, b := 15, 4

	fmt.Printf("%d + %d = %d\\n", a, b, a+b)
	fmt.Printf("%d - %d = %d\\n", a, b, a-b)
	fmt.Printf("%d * %d = %d\\n", a, b, a*b)
	fmt.Printf("%d / %d = %d\\n", a, b, a/b)
	fmt.Printf("%d %% %d = %d\\n", a, b, a%b)
	fmt.Printf("%d / %d = %.2f (desimal)\\n", a, b, float64(a)/float64(b))
}""",
    },
    {
        "title": "Latihan 3: Cek Kelulusan",
        "difficulty": "Mudah",
        "question": [
            "Baca satu angka nilai dari input.",
            "Tampilkan grade sesuai aturan:",
            "  >= 85 : A",
            "  >= 75 : B",
            "  >= 60 : C",
            "  selain itu : E",
            "",
            "Lalu tampilkan status Lulus kalau nilai >= 75,",
            "atau Tidak Lulus kalau kurang.",
            "",
            "Untuk input 80, output yang benar:",
            "  Grade: B",
            "  Status: Lulus",
        ],
        "hints": [
            "Baca angka dengan fmt.Scan(&nilai), jangan lupa tanda &.",
            "Gunakan rantai if / else if / else.",
            "Deklarasikan variabel grade lebih dulu lalu isi di dalam if.",
        ],
        "stdin": "80\n",
        "solution": """package main

import "fmt"

func main() {
	var nilai int
	fmt.Scan(&nilai)

	var grade string
	if nilai >= 85 {
		grade = "A"
	} else if nilai >= 75 {
		grade = "B"
	} else if nilai >= 60 {
		grade = "C"
	} else {
		grade = "E"
	}

	status := "Tidak Lulus"
	if nilai >= 75 {
		status = "Lulus"
	}

	fmt.Println("Grade:", grade)
	fmt.Println("Status:", status)
}""",
    },
    {
        "title": "Latihan 4: Deret Angka Genap",
        "difficulty": "Mudah",
        "question": [
            "Tampilkan semua bilangan genap dari 1 sampai 20,",
            "satu angka per baris.",
            "Di baris terakhir tampilkan:",
            "  Total: 110",
        ],
        "hints": [
            "Pakai for i := 1; i <= 20; i++",
            "Bilangan genap berarti i % 2 == 0",
            "Siapkan variabel total di luar perulangan.",
        ],
        "solution": """package main

import "fmt"

func main() {
	total := 0

	for i := 1; i <= 20; i++ {
		if i%2 == 0 {
			fmt.Println(i)
			total += i
		}
	}

	fmt.Println("Total:", total)
}""",
    },
    {
        "title": "Latihan 5: Segitiga Bintang",
        "difficulty": "Mudah",
        "question": [
            "Baca satu angka n dari input.",
            "Tampilkan segitiga bintang setinggi n baris.",
            "",
            "Untuk input 5, outputnya:",
            "  *",
            "  **",
            "  ***",
            "  ****",
            "  *****",
            "",
            "(tanpa spasi di depan bintang)",
        ],
        "hints": [
            "Butuh dua perulangan bersarang.",
            "Perulangan luar mengatur baris, perulangan dalam mencetak bintang.",
            "Pakai fmt.Print(\"*\") lalu fmt.Println() di akhir tiap baris.",
        ],
        "stdin": "5\n",
        "solution": """package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)

	for i := 1; i <= n; i++ {
		for j := 0; j < i; j++ {
			fmt.Print("*")
		}
		fmt.Println()
	}
}""",
    },
    {
        "title": "Latihan 6: Statistik Slice",
        "difficulty": "Sedang",
        "question": [
            "Buat slice berisi: 80, 65, 90, 45, 75",
            "Tampilkan:",
            "  Data: [80 65 90 45 75]",
            "  Jumlah data: 5",
            "  Total: 355",
            "  Rata-rata: 71.00",
            "  Tertinggi: 90",
            "  Terendah: 45",
            "  Terurut: [45 65 75 80 90]",
            "",
            "Pengurutan tidak boleh mengubah slice aslinya.",
        ],
        "hints": [
            "Buat slice dengan: nilai := []int{80, 65, 90, 45, 75}",
            "Salin dulu sebelum sort: salinan := make([]int, len(nilai)); copy(salinan, nilai)",
            "Urutkan dengan sort.Ints dari package sort.",
        ],
        "solution": """package main

import (
	"fmt"
	"sort"
)

func main() {
	nilai := []int{80, 65, 90, 45, 75}

	total := 0
	tertinggi := nilai[0]
	terendah := nilai[0]

	for _, n := range nilai {
		total += n
		if n > tertinggi {
			tertinggi = n
		}
		if n < terendah {
			terendah = n
		}
	}

	salinan := make([]int, len(nilai))
	copy(salinan, nilai)
	sort.Ints(salinan)

	fmt.Println("Data:", nilai)
	fmt.Println("Jumlah data:", len(nilai))
	fmt.Println("Total:", total)
	fmt.Printf("Rata-rata: %.2f\\n", float64(total)/float64(len(nilai)))
	fmt.Println("Tertinggi:", tertinggi)
	fmt.Println("Terendah:", terendah)
	fmt.Println("Terurut:", salinan)
}""",
    },
    {
        "title": "Latihan 7: Hitung Frekuensi Kata",
        "difficulty": "Sedang",
        "question": [
            "Diberikan kalimat: \"go itu cepat go itu sederhana go itu kuat\"",
            "Hitung berapa kali tiap kata muncul.",
            "Tampilkan hasilnya URUT ABJAD dengan format:",
            "  cepat     : 1",
            "  go        : 3",
            "  itu       : 3",
            "  kuat      : 1",
            "  sederhana : 1",
            "  Total kata unik: 5",
            "",
            "Nama kata dicetak rata kiri selebar 9 karakter.",
        ],
        "hints": [
            "Pecah kalimat dengan strings.Fields(kalimat).",
            "Hitung dengan map[string]int, cukup tulis frekuensi[kata]++",
            "Urutan map acak! Kumpulkan kunci ke slice lalu sort.Strings.",
        ],
        "solution": """package main

import (
	"fmt"
	"sort"
	"strings"
)

func main() {
	kalimat := "go itu cepat go itu sederhana go itu kuat"

	frekuensi := make(map[string]int)
	for _, kata := range strings.Fields(kalimat) {
		frekuensi[kata]++
	}

	kunci := make([]string, 0, len(frekuensi))
	for k := range frekuensi {
		kunci = append(kunci, k)
	}
	sort.Strings(kunci)

	for _, k := range kunci {
		fmt.Printf("%-9s : %d\\n", k, frekuensi[k])
	}

	fmt.Println("Total kata unik:", len(frekuensi))
}""",
    },
    {
        "title": "Latihan 8: Fungsi Multi Return",
        "difficulty": "Sedang",
        "question": [
            "Buat fungsi bagi(a, b float64) (float64, error).",
            "Fungsi mengembalikan error kalau pembaginya nol.",
            "",
            "Buat juga fungsi statistik(data []int) (min, maks, total int).",
            "Gunakan named return values.",
            "",
            "Uji keduanya sehingga outputnya:",
            "  10 / 4 = 2.50",
            "  Error: pembagi tidak boleh nol",
            "  Min: 3 Maks: 9 Total: 17",
        ],
        "hints": [
            "Buat error dengan errors.New(\"pesan\").",
            "Named return: func statistik(data []int) (min, maks, total int)",
            "Dengan named return, cukup tulis 'return' kosong di akhir.",
        ],
        "solution": """package main

import (
	"errors"
	"fmt"
)

func bagi(a, b float64) (float64, error) {
	if b == 0 {
		return 0, errors.New("pembagi tidak boleh nol")
	}
	return a / b, nil
}

func statistik(data []int) (min, maks, total int) {
	min = data[0]
	maks = data[0]
	for _, n := range data {
		total += n
		if n < min {
			min = n
		}
		if n > maks {
			maks = n
		}
	}
	return
}

func main() {
	if hasil, err := bagi(10, 4); err == nil {
		fmt.Printf("10 / 4 = %.2f\\n", hasil)
	}

	if _, err := bagi(10, 0); err != nil {
		fmt.Println("Error:", err)
	}

	min, maks, total := statistik([]int{5, 9, 3})
	fmt.Println("Min:", min, "Maks:", maks, "Total:", total)
}""",
    },
    {
        "title": "Latihan 9: Pointer & Tukar Nilai",
        "difficulty": "Sedang",
        "question": [
            "Buat tiga fungsi:",
            "  tukar(a, b *int)           menukar isi dua variabel",
            "  naikkan(n *int, x int)     menambah nilai n sebanyak x",
            "  gandakan(s []int)          mengalikan tiap elemen slice dengan 2",
            "",
            "Uji sehingga outputnya:",
            "  Sebelum tukar: a=1 b=2",
            "  Sesudah tukar: a=2 b=1",
            "  Sebelum naikkan: 10",
            "  Sesudah naikkan: 35",
            "  Sebelum gandakan: [1 2 3]",
            "  Sesudah gandakan: [2 4 6]",
        ],
        "hints": [
            "Kirim alamat variabel dengan tanda &, misalnya tukar(&a, &b).",
            "Di dalam fungsi, akses nilainya dengan *a dan *b.",
            "Slice sudah berperilaku seperti referensi, jadi TIDAK perlu pointer.",
        ],
        "solution": """package main

import "fmt"

func tukar(a, b *int) {
	*a, *b = *b, *a
}

func naikkan(n *int, x int) {
	*n += x
}

func gandakan(s []int) {
	for i := range s {
		s[i] *= 2
	}
}

func main() {
	a, b := 1, 2
	fmt.Printf("Sebelum tukar: a=%d b=%d\\n", a, b)
	tukar(&a, &b)
	fmt.Printf("Sesudah tukar: a=%d b=%d\\n", a, b)

	n := 10
	fmt.Println("Sebelum naikkan:", n)
	naikkan(&n, 25)
	fmt.Println("Sesudah naikkan:", n)

	s := []int{1, 2, 3}
	fmt.Println("Sebelum gandakan:", s)
	gandakan(s)
	fmt.Println("Sesudah gandakan:", s)
}""",
    },
    {
        "title": "Latihan 10: Struct Siswa",
        "difficulty": "Sedang",
        "question": [
            "Buat struct Siswa dengan field Nama (string) dan Nilai (float64).",
            "Buat method:",
            "  Lulus() bool         true kalau Nilai >= 75",
            "  Remedial(x float64)  menambah nilai, maksimal 100",
            "",
            "Buat slice berisi 3 siswa: Andi 72, Budi 88, Citra 65.",
            "Tampilkan tiap siswa, beri remedial 10 poin untuk yang belum lulus,",
            "lalu tampilkan ulang dan cetak rata-ratanya.",
            "",
            "Output yang diharapkan:",
            "  == Sebelum remedial ==",
            "  Andi       72.0  belum lulus",
            "  Budi       88.0  lulus",
            "  Citra      65.0  belum lulus",
            "  == Sesudah remedial ==",
            "  Andi       82.0  lulus",
            "  Budi       88.0  lulus",
            "  Citra      75.0  lulus",
            "  Rata-rata: 81.67",
        ],
        "hints": [
            "Method pengubah butuh pointer receiver: func (s *Siswa) Remedial(...)",
            "Agar bisa mengubah isi slice, iterasi dengan indeks: for i := range daftar",
            "Format kolom dengan fmt.Printf(\"%-10s %.1f  %s\\n\", ...)",
        ],
        "solution": """package main

import "fmt"

type Siswa struct {
	Nama  string
	Nilai float64
}

func (s Siswa) Lulus() bool {
	return s.Nilai >= 75
}

func (s *Siswa) Remedial(x float64) {
	s.Nilai += x
	if s.Nilai > 100 {
		s.Nilai = 100
	}
}

func tampilkan(daftar []Siswa) {
	for _, s := range daftar {
		ket := "belum lulus"
		if s.Lulus() {
			ket = "lulus"
		}
		fmt.Printf("%-10s %.1f  %s\\n", s.Nama, s.Nilai, ket)
	}
}

func main() {
	daftar := []Siswa{
		{Nama: "Andi", Nilai: 72},
		{Nama: "Budi", Nilai: 88},
		{Nama: "Citra", Nilai: 65},
	}

	fmt.Println("== Sebelum remedial ==")
	tampilkan(daftar)

	for i := range daftar {
		if !daftar[i].Lulus() {
			daftar[i].Remedial(10)
		}
	}

	fmt.Println("== Sesudah remedial ==")
	tampilkan(daftar)

	total := 0.0
	for _, s := range daftar {
		total += s.Nilai
	}
	fmt.Printf("Rata-rata: %.2f\\n", total/float64(len(daftar)))
}""",
    },
    {
        "title": "Latihan 11: Interface Bentuk Geometri",
        "difficulty": "Sulit",
        "question": [
            "Buat interface Bentuk dengan method Luas() float64 dan Nama() string.",
            "Buat tiga tipe yang memenuhinya: Persegi, Lingkaran, Segitiga.",
            "",
            "Simpan ketiganya dalam satu slice []Bentuk lalu tampilkan",
            "diurutkan dari luas TERBESAR ke terkecil.",
            "",
            "Gunakan Persegi sisi 4, Lingkaran jari-jari 3, Segitiga alas 6 tinggi 5.",
            "",
            "Output yang diharapkan:",
            "  Lingkaran        28.27",
            "  Persegi          16.00",
            "  Segitiga         15.00",
            "  Total luas: 59.27",
        ],
        "hints": [
            "Luas lingkaran memakai math.Pi * r * r.",
            "Urutkan dengan sort.Slice(daftar, func(i, j int) bool { ... }).",
            "Fungsi pembanding mengembalikan true kalau i harus di depan j.",
        ],
        "solution": """package main

import (
	"fmt"
	"math"
	"sort"
)

type Bentuk interface {
	Luas() float64
	Nama() string
}

type Persegi struct{ Sisi float64 }

func (p Persegi) Luas() float64 { return p.Sisi * p.Sisi }
func (p Persegi) Nama() string  { return "Persegi" }

type Lingkaran struct{ Jari float64 }

func (l Lingkaran) Luas() float64 { return math.Pi * l.Jari * l.Jari }
func (l Lingkaran) Nama() string  { return "Lingkaran" }

type Segitiga struct{ Alas, Tinggi float64 }

func (s Segitiga) Luas() float64 { return 0.5 * s.Alas * s.Tinggi }
func (s Segitiga) Nama() string  { return "Segitiga" }

func main() {
	daftar := []Bentuk{
		Persegi{Sisi: 4},
		Lingkaran{Jari: 3},
		Segitiga{Alas: 6, Tinggi: 5},
	}

	sort.Slice(daftar, func(i, j int) bool {
		return daftar[i].Luas() > daftar[j].Luas()
	})

	total := 0.0
	for _, b := range daftar {
		fmt.Printf("%-16s %.2f\\n", b.Nama(), b.Luas())
		total += b.Luas()
	}

	fmt.Printf("Total luas: %.2f\\n", total)
}""",
    },
    {
        "title": "Latihan 12: Error Kustom Rekening",
        "difficulty": "Sulit",
        "question": [
            "Buat struct Rekening dengan field Pemilik dan Saldo (int).",
            "Buat error sentinel ErrSaldoKurang dan ErrJumlahTidakValid.",
            "",
            "Method Tarik(jumlah int) error dengan aturan:",
            "  jumlah <= 0        -> ErrJumlahTidakValid",
            "  jumlah > Saldo     -> ErrSaldoKurang (dibungkus dengan konteks)",
            "  selain itu         -> kurangi saldo, kembalikan nil",
            "",
            "Uji dengan saldo awal 100000 dan penarikan: 30000, 0, 500000, 70000.",
            "",
            "Output yang diharapkan:",
            "  Tarik 30000 berhasil, sisa 70000",
            "  Ditolak: jumlah penarikan tidak valid",
            "  Ditolak: tarik 500000 dari saldo 70000: saldo tidak mencukupi",
            "  Tarik 70000 berhasil, sisa 0",
        ],
        "hints": [
            "Buat sentinel dengan var ErrX = errors.New(\"...\") di level package.",
            "Bungkus dengan fmt.Errorf(\"...: %w\", ErrSaldoKurang).",
            "Periksa dengan errors.Is(err, ErrSaldoKurang), bukan perbandingan ==.",
        ],
        "solution": """package main

import (
	"errors"
	"fmt"
)

var (
	ErrSaldoKurang       = errors.New("saldo tidak mencukupi")
	ErrJumlahTidakValid  = errors.New("jumlah penarikan tidak valid")
)

type Rekening struct {
	Pemilik string
	Saldo   int
}

func (r *Rekening) Tarik(jumlah int) error {
	if jumlah <= 0 {
		return ErrJumlahTidakValid
	}
	if jumlah > r.Saldo {
		return fmt.Errorf("tarik %d dari saldo %d: %w", jumlah, r.Saldo, ErrSaldoKurang)
	}
	r.Saldo -= jumlah
	return nil
}

func main() {
	r := &Rekening{Pemilik: "Andi", Saldo: 100000}

	for _, jumlah := range []int{30000, 0, 500000, 70000} {
		err := r.Tarik(jumlah)

		switch {
		case err == nil:
			fmt.Printf("Tarik %d berhasil, sisa %d\\n", jumlah, r.Saldo)
		case errors.Is(err, ErrJumlahTidakValid):
			fmt.Println("Ditolak:", err)
		case errors.Is(err, ErrSaldoKurang):
			fmt.Println("Ditolak:", err)
		default:
			fmt.Println("Error tak terduga:", err)
		}
	}
}""",
    },
    {
        "title": "Latihan 13: Goroutine & Channel",
        "difficulty": "Sulit",
        "question": [
            "Hitung kuadrat dari angka 1 sampai 8 secara paralel.",
            "",
            "Bagian 1: pakai sync.WaitGroup dan sync.Mutex,",
            "kumpulkan hasilnya ke slice lalu urutkan.",
            "",
            "Bagian 2: pakai channel berpenyangga, kirim hasilnya,",
            "tutup channel, lalu jumlahkan dengan range.",
            "",
            "Output yang diharapkan:",
            "  Kuadrat: [1 4 9 16 25 36 49 64]",
            "  Total dari channel: 204",
        ],
        "hints": [
            "Panggil wg.Add(1) SEBELUM menjalankan goroutine, dan defer wg.Done() di dalamnya.",
            "Kirim variabel loop sebagai argumen goroutine agar nilainya benar.",
            "Hasil goroutine urutannya acak, jadi wajib sort.Ints sebelum dicetak.",
        ],
        "solution": """package main

import (
	"fmt"
	"sort"
	"sync"
)

func main() {
	// Bagian 1: WaitGroup + Mutex
	var wg sync.WaitGroup
	var mu sync.Mutex
	hasil := make([]int, 0, 8)

	for i := 1; i <= 8; i++ {
		wg.Add(1)
		go func(n int) {
			defer wg.Done()
			kuadrat := n * n
			mu.Lock()
			hasil = append(hasil, kuadrat)
			mu.Unlock()
		}(i)
	}
	wg.Wait()

	sort.Ints(hasil)
	fmt.Println("Kuadrat:", hasil)

	// Bagian 2: channel berpenyangga
	ch := make(chan int, 8)
	go func() {
		defer close(ch)
		for i := 1; i <= 8; i++ {
			ch <- i * i
		}
	}()

	total := 0
	for n := range ch {
		total += n
	}
	fmt.Println("Total dari channel:", total)
}""",
    },
    {
        "title": "Latihan 14: Inventaris Barang",
        "difficulty": "Sulit",
        "question": [
            "Buat sistem inventaris sederhana:",
            "",
            "  struct Barang: Kode, Nama string; Harga, Stok int",
            "  method NilaiTotal() int -> Harga * Stok",
            "  struct Inventaris menyimpan map[string]*Barang",
            "  method Tambah(b Barang)   -> kalau kode sudah ada, stok ditambah",
            "  method Ambil(kode, jumlah) error",
            "  method Laporan()          -> cetak URUT berdasarkan kode",
            "",
            "Tambahkan: B001 Beras 65000 x20, B002 Gula 15000 x8,",
            "B003 Minyak 32000 x12, lalu B002 lagi x5.",
            "Cetak laporan, ambil B001 sebanyak 5, cetak laporan lagi.",
            "",
            "Output yang diharapkan:",
            "  == LAPORAN ==",
            "  B001   Beras             65000 x 20 =  1300000",
            "  B002   Gula              15000 x 13 =   195000",
            "  B003   Minyak            32000 x 12 =   384000",
            "  Nilai total: 1879000",
            "  Ambil B001 x5 berhasil",
            "  == LAPORAN ==",
            "  B001   Beras             65000 x 15 =   975000",
            "  B002   Gula              15000 x 13 =   195000",
            "  B003   Minyak            32000 x 12 =   384000",
            "  Nilai total: 1554000",
        ],
        "hints": [
            "Simpan POINTER di map (map[string]*Barang) agar stok bisa diubah.",
            "Urutan map acak: kumpulkan kunci ke slice lalu sort.Strings sebelum mencetak.",
            "Format kolom: fmt.Printf(\"%-6s %-14s %8d x %2d = %8d\\n\", ...)",
        ],
        "solution": """package main

import (
	"fmt"
	"sort"
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
		return fmt.Errorf("kode %s tidak ditemukan", kode)
	}
	if b.Stok < jumlah {
		return fmt.Errorf("stok %s hanya %d", b.Nama, b.Stok)
	}
	b.Stok -= jumlah
	return nil
}

func (i *Inventaris) kodeTerurut() []string {
	kode := make([]string, 0, len(i.barang))
	for k := range i.barang {
		kode = append(kode, k)
	}
	sort.Strings(kode)
	return kode
}

func (i *Inventaris) Laporan() {
	fmt.Println("== LAPORAN ==")
	total := 0
	for _, k := range i.kodeTerurut() {
		b := i.barang[k]
		fmt.Printf("%-6s %-14s %8d x %2d = %8d\\n",
			b.Kode, b.Nama, b.Harga, b.Stok, b.NilaiTotal())
		total += b.NilaiTotal()
	}
	fmt.Println("Nilai total:", total)
}

func main() {
	inv := BuatInventaris()

	inv.Tambah(Barang{"B001", "Beras", 65000, 20})
	inv.Tambah(Barang{"B002", "Gula", 15000, 8})
	inv.Tambah(Barang{"B003", "Minyak", 32000, 12})
	inv.Tambah(Barang{"B002", "Gula", 15000, 5})

	inv.Laporan()

	if err := inv.Ambil("B001", 5); err != nil {
		fmt.Println("Gagal:", err)
	} else {
		fmt.Println("Ambil B001 x5 berhasil")
	}

	inv.Laporan()
}""",
    },
]
