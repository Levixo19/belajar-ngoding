RUBY_EXERCISES = [
    {
        "title": "Latihan 1: Perkenalan Diri",
        "difficulty": "Mudah",
        "question": [
            "Buat program Ruby yang menampilkan tepat tiga baris:",
            "",
            "Keluaran yang diharapkan:",
            "",
            "  Halo, namaku Andi!",
            "  Aku sedang belajar Ruby.",
            "  Di Ruby, semuanya adalah objek.",
        ],
        "hints": [
            "puts mencetak lalu pindah baris.",
            "Tidak perlu titik koma dan tidak perlu fungsi main.",
            "Kode dijalankan dari atas ke bawah.",
        ],
        "solution": """puts "Halo, namaku Andi!"
puts "Aku sedang belajar Ruby."
puts "Di Ruby, semuanya adalah objek.\"""",
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
            "  17 ** 2 = 289",
            "  17 / 5 = 3.40 (desimal)",
        ],
        "hints": [
            "Interpolasi: puts \"#{a} + #{b} = #{a + b}\"",
            "Dua Integer dibagi menghasilkan Integer; sisanya dibuang.",
            "Untuk desimal, panggil .to_f pada salah satu sisi.",
            "Format dua desimal: '%.2f' % nilai",
        ],
        "solution": """a = 17
b = 5

puts "#{a} + #{b} = #{a + b}"
puts "#{a} - #{b} = #{a - b}"
puts "#{a} * #{b} = #{a * b}"
puts "#{a} / #{b} = #{a / b}"
puts "#{a} % #{b} = #{a % b}"
puts "#{a} ** 2 = #{a**2}"
puts "#{a} / #{b} = #{'%.2f' % (a.to_f / b)} (desimal)\"""",
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
            "gets membaca satu baris; .to_f mengubahnya jadi Float.",
            "Pakai 9.0 / 5 supaya pembagiannya bukan pembagian Integer.",
            "format('%.2f', x) atau '%.2f' % x untuk dua desimal.",
            "Jangan mencetak apa pun sebelum gets.",
        ],
        "stdin": "25\n",
        "solution": """c = gets.to_f
f = c * 9.0 / 5 + 32
k = c + 273.15

puts "Celsius    : #{'%.2f' % c}"
puts "Fahrenheit : #{'%.2f' % f}"
puts "Kelvin     : #{'%.2f' % k}\"""",
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
            "case dengan rentang: when 85..100 then 'A'",
            "Rentang inklusif memakai .. dan eksklusif memakai ...",
            "case adalah ekspresi, jadi hasilnya langsung bisa ditugaskan.",
            "if juga ekspresi: status = nilai >= 75 ? 'Lulus' : 'Tidak Lulus'",
        ],
        "stdin_list": ["92\n", "78\n", "65\n", "45\n", "12\n"],
        "solution": """nilai = gets.to_i

grade = case nilai
        when 85..100 then "A"
        when 75...85 then "B"
        when 60...75 then "C"
        when 40...60 then "D"
        else              "E"
        end

puts "Grade: #{grade}"
puts "Status: #{nilai >= 75 ? 'Lulus' : 'Tidak Lulus'}\"""",
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
            "(1..5).each { |b| ... } untuk tiap baris.",
            "print mencetak tanpa pindah baris; puts kosong hanya pindah baris.",
            "rjust(2) meratakan ke kanan selebar 2 karakter.",
            "Kumpulkan sel-selnya ke array lalu join dengan tiga spasi.",
        ],
        "solution": """(1..5).each do |b|
  sel = (1..5).map { |k| "#{b} x #{k} = #{(b * k).to_s.rjust(2)}" }
  puts "  " + sel.join("   ")
end""",
    },
    {
        "title": "Latihan 6: Statistik Nilai",
        "difficulty": "Menengah",
        "question": [
            "Diberikan array nilai berikut di dalam kodemu:",
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
            "join(', ') menggabungkan array jadi teks.",
            "sort mengembalikan array BARU, sort! mengubah yang asli.",
            "sum, min, max, dan size sudah tersedia di Array.",
            "Jangan lupa .to_f supaya rata-ratanya bukan pembagian Integer.",
        ],
        "solution": """nilai = [78, 92, 65, 88, 71, 95, 59, 83]
rata = nilai.sum.to_f / nilai.size

puts "Data      : #{nilai.join(', ')}"
puts "Terurut   : #{nilai.sort.join(', ')}"
puts "Jumlah    : #{nilai.size}"
puts "Total     : #{nilai.sum}"
puts "Rata-rata : #{'%.2f' % rata}"
puts "Tertinggi : #{nilai.max}"
puts "Terendah  : #{nilai.min}"
puts "Di atas rata-rata: #{nilai.select { |n| n > rata }.join(', ')}\"""",
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
            "reverse membalik string.",
            "delete(' ') atau gsub(/\\s/, '') membuang spasi.",
            "downcase untuk mengabaikan besar-kecil huruf.",
            "chomp membuang karakter baris baru dari gets.",
        ],
        "stdin_list": ["Kasur ini rusak\n", "Belajar Ruby\n", "Ini\n"],
        "solution": """teks = gets.chomp
rapat = teks.delete(" ")
bersih = rapat.downcase

puts "Asli    : #{teks}"
puts "Dibalik : #{teks.reverse}"
puts "Huruf   : #{rapat.length}"
puts "Palindrom: #{bersih == bersih.reverse ? 'ya' : 'bukan'}\"""",
    },
    {
        "title": "Latihan 8: Menghitung Frekuensi Kata",
        "difficulty": "Menengah",
        "question": [
            "Diberikan kalimat berikut di dalam kodemu:",
            "  \"kucing makan ikan kucing tidur ikan kucing\"",
            "",
            "Hitung berapa kali tiap kata muncul, lalu tampilkan",
            "terurut dari yang paling sering. Kalau jumlahnya sama,",
            "urutkan berdasarkan abjad.",
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
            "split memecah kalimat jadi array kata.",
            "tally menghitung frekuensi dalam satu panggilan.",
            "Dua kunci urutan: sort_by { |k, n| [-n, k] }",
            "ljust(7) meratakan ke kiri selebar 7.",
        ],
        "solution": """kalimat = "kucing makan ikan kucing tidur ikan kucing"
kata = kalimat.split
hitung = kata.tally

hitung.sort_by { |k, n| [-n, k] }.each do |k, n|
  puts "#{k.ljust(7)}: #{n}"
end

puts "---"
puts "Kata unik  : #{hitung.size}"
puts "Total kata : #{kata.size}\"""",
    },
    {
        "title": "Latihan 9: Class Murid dengan Validasi",
        "difficulty": "Menengah",
        "question": [
            "Buat class Murid dengan:",
            "  - attr_reader :nama dan :nilai",
            "  - initialize(nama, nilai) yang memanggil setternya sendiri",
            "  - nilai=(baru) yang MENOLAK di luar 0..100 dengan ArgumentError",
            "    berpesan \"nilai di luar 0..100\"",
            "  - grade -> 'A' jika >=85, 'B' >=75, 'C' >=60, sisanya 'D'",
            "  - to_s berbentuk \"Andi     92 A\"",
            "    (nama rata kiri 8, nilai rata kanan 3, spasi, grade)",
            "",
            "Buat tiga murid: Andi 92, Budi 78, Cici 64. Cetak ketiganya,",
            "lalu coba mengisi nilai Andi dengan 150 dan tangkap galatnya.",
            "",
            "Keluaran yang diharapkan:",
            "",
            "  Andi     92 A",
            "  Budi     78 B",
            "  Cici     64 C",
            "  Ditolak: nilai di luar 0..100",
        ],
        "hints": [
            "attr_reader membuat getter; setternya ditulis tangan: def nilai=(baru)",
            "Di dalam initialize, panggil `self.nilai = nilai` supaya validasinya ikut.",
            "(0..100).cover?(baru) memeriksa rentang.",
            "puts pada objek memanggil to_s secara otomatis.",
        ],
        "solution": """class Murid
  attr_reader :nama, :nilai

  def initialize(nama, nilai)
    @nama = nama
    self.nilai = nilai
  end

  def nilai=(baru)
    raise ArgumentError, "nilai di luar 0..100" unless (0..100).cover?(baru)

    @nilai = baru
  end

  def grade
    case @nilai
    when 85.. then "A"
    when 75.. then "B"
    when 60.. then "C"
    else           "D"
    end
  end

  def to_s = format("%-8s%3d %s", @nama, @nilai, grade)
end

kelas = [Murid.new("Andi", 92), Murid.new("Budi", 78), Murid.new("Cici", 64)]
kelas.each { |m| puts m }

begin
  kelas[0].nilai = 150
rescue ArgumentError => e
  puts "Ditolak: #{e.message}"
end""",
    },
    {
        "title": "Latihan 10: Module, Mixin & Comparable",
        "difficulty": "Lanjut",
        "question": [
            "Buat module BisaDiringkas dengan method ringkas yang",
            "menghasilkan format('%-16s%8.2f', nama, luas).",
            "",
            "Buat class Bangun yang memakai module itu, include Comparable,",
            "menyimpan nama, punya method luas yang melempar",
            "NotImplementedError, dan <=> yang membandingkan luas.",
            "",
            "Turunkan Persegi(sisi), Lingkaran(jari) dengan PI = 3.14159,",
            "dan PersegiPanjang(panjang, lebar).",
            "",
            "Buat array berisi Persegi(4), Lingkaran(3), PersegiPanjang(6, 3),",
            "lalu cetak ringkasannya, totalnya, dan yang terluas.",
            "",
            "Keluaran yang diharapkan:",
            "",
            "  Persegi            16.00",
            "  Lingkaran          28.27",
            "  PersegiPanjang     18.00",
            "  TOTAL              62.27",
            "  terluas: Lingkaran",
        ],
        "hints": [
            "include BisaDiringkas dan include Comparable di class induknya.",
            "super('Persegi') memanggil initialize induk.",
            "Dengan <=> dan Comparable, .max pada array langsung bekerja.",
            "sum(&:luas) menjumlahkan hasil method luas tiap elemen.",
        ],
        "solution": """module BisaDiringkas
  def ringkas = format("%-16s%8.2f", nama, luas)
end

class Bangun
  include BisaDiringkas
  include Comparable

  attr_reader :nama

  def initialize(nama) = @nama = nama

  def luas = raise(NotImplementedError, "#{self.class} harus punya luas")

  def <=>(lain) = luas <=> lain.luas
end

class Persegi < Bangun
  def initialize(sisi)
    super("Persegi")
    @sisi = sisi
  end

  def luas = @sisi**2
end

class Lingkaran < Bangun
  PI = 3.14159

  def initialize(jari)
    super("Lingkaran")
    @jari = jari
  end

  def luas = PI * @jari**2
end

class PersegiPanjang < Bangun
  def initialize(panjang, lebar)
    super("PersegiPanjang")
    @panjang = panjang
    @lebar = lebar
  end

  def luas = @panjang * @lebar
end

semua = [Persegi.new(4), Lingkaran.new(3), PersegiPanjang.new(6, 3)]

semua.each { |b| puts b.ringkas }
puts format("%-16s%8.2f", "TOTAL", semua.sum(&:luas))
puts "terluas: #{semua.max.nama}\"""",
    },
    {
        "title": "Latihan 11: Blok, yield & ensure",
        "difficulty": "Lanjut",
        "question": [
            "Buat method ulangi(n) yang memanggil blok n kali dengan angka",
            "1..n dan mengumpulkan hasilnya jadi array.",
            "",
            "Buat method dengan_pengukur(nama) yang:",
            "  - mencetak \"mulai <nama>\"",
            "  - menjalankan bloknya dan mengembalikan hasilnya",
            "  - mencetak \"selesai <nama>\" kalau berhasil",
            "  - menangkap RuntimeError, mencetak \"galat: <pesan>\", balik nil",
            "  - SELALU mencetak \"(bersih <nama>)\" di akhir",
            "",
            "Buat juga Hash berisi tiga lambda: tambah, kurang, kali,",
            "lalu jalankan semuanya dengan (9, 4).",
            "",
            "Keluaran yang diharapkan:",
            "",
            "  [1, 4, 9, 16, 25]",
            "  [\"baris 1\", \"baris 2\", \"baris 3\"]",
            "  mulai hitung",
            "  selesai hitung",
            "  (bersih hitung)",
            "  hasil: 42",
            "  mulai gagal",
            "  galat: ada masalah",
            "  (bersih gagal)",
            "  hasil: nil",
            "  tambah (9, 4) = 13",
            "  kurang (9, 4) = 5",
            "  kali   (9, 4) = 36",
        ],
        "hints": [
            "yield(i) menjalankan bloknya dengan argumen i.",
            "ensure di dalam method berlaku untuk seluruh badan method.",
            "Lambda ditulis ->(a, b) { ... } dan dipanggil dengan .call(a, b).",
            "inspect menampilkan nil sebagai 'nil' dan array dengan kurung siku.",
        ],
        "solution": """def ulangi(n)
  (1..n).map { |i| yield(i) }
end

def dengan_pengukur(nama)
  puts "mulai #{nama}"
  hasil = yield
  puts "selesai #{nama}"
  hasil
rescue RuntimeError => e
  puts "galat: #{e.message}"
  nil
ensure
  puts "(bersih #{nama})"
end

puts ulangi(5) { |i| i * i }.inspect
puts ulangi(3) { |i| "baris #{i}" }.inspect

puts "hasil: #{dengan_pengukur('hitung') { 6 * 7 }.inspect}"
puts "hasil: #{dengan_pengukur('gagal') { raise 'ada masalah' }.inspect}"

operasi = {
  tambah: ->(a, b) { a + b },
  kurang: ->(a, b) { a - b },
  kali: ->(a, b) { a * b },
}

operasi.each do |nama, fn|
  puts "#{nama.to_s.ljust(7)}(9, 4) = #{fn.call(9, 4)}"
end""",
    },
    {
        "title": "Latihan 12: Rantai Enumerable",
        "difficulty": "Lanjut",
        "question": [
            "Buat Struct Transaksi dengan barang, kategori, jumlah, harga.",
            "Isi dengan:",
            "  Kopi  Minuman  3  25000",
            "  Teh   Minuman  5  15000",
            "  Roti  Makanan  2  20000",
            "  Nasi  Makanan  4  30000",
            "  Jus   Minuman  1  35000",
            "",
            "Tambahkan method subtotal di dalam Struct-nya.",
            "Tampilkan semua transaksi terurut subtotal MENURUN; kalau sama,",
            "nama barang MENAIK. Lalu total, rekap per kategori terurut",
            "abjad, dan barang termahal.",
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
            "Struct.new(:a, :b) do ... end boleh memuat method sendiri.",
            "Dua kunci urutan: sort_by { |t| [-t.subtotal, t.barang] }",
            "group_by(&:kategori) menghasilkan Hash kategori -> array.",
            "max_by(&:subtotal) mencari elemen dengan nilai terbesar.",
        ],
        "solution": """Transaksi = Struct.new(:barang, :kategori, :jumlah, :harga) do
  def subtotal = jumlah * harga
end

data = [
  Transaksi.new("Kopi", "Minuman", 3, 25_000),
  Transaksi.new("Teh", "Minuman", 5, 15_000),
  Transaksi.new("Roti", "Makanan", 2, 20_000),
  Transaksi.new("Nasi", "Makanan", 4, 30_000),
  Transaksi.new("Jus", "Minuman", 1, 35_000),
]

data.sort_by { |t| [-t.subtotal, t.barang] }.each do |t|
  puts format("%-11s%-11s%2d x %6d = %8d",
              t.barang, t.kategori, t.jumlah, t.harga, t.subtotal)
end

puts "---"
puts format("%-10s: %d", "Total", data.sum(&:subtotal))

data.group_by(&:kategori).sort.each do |kategori, anggota|
  puts format("%-10s: %d (%d transaksi)",
              kategori, anggota.sum(&:subtotal), anggota.size)
end

puts format("%-10s: %s", "Termahal", data.max_by(&:subtotal).barang)""",
    },
    {
        "title": "Latihan 13: Exception Sendiri & retry",
        "difficulty": "Lanjut",
        "question": [
            "Buat SaldoKurangError < StandardError dengan attr_reader :kurang",
            "dan pesan \"saldo kurang <n>\".",
            "",
            "Buat class Dompet dengan attr_reader :saldo dan method bayar:",
            "  - jumlah tidak positif -> ArgumentError \"jumlah <n> tidak sah\"",
            "  - jumlah > saldo -> SaldoKurangError",
            "  - selain itu saldo berkurang",
            "",
            "Mulai saldo 50000, bayar berurutan 20000, -5, 100000, 30000.",
            "",
            "Lalu buat method ambil_data yang gagal dua kali pertama",
            "(IOError) dan berhasil di panggilan ketiga. Pakai retry dengan",
            "batas 5 percobaan.",
            "",
            "Keluaran yang diharapkan:",
            "",
            "  bayar   20000 -> sisa 30000",
            "  bayar      -5 -> DITOLAK: jumlah -5 tidak sah",
            "  bayar  100000 -> GAGAL, kurang 70000",
            "  bayar   30000 -> sisa 0",
            "  ---",
            "  percobaan 1 gagal: koneksi gagal",
            "  percobaan 2 gagal: koneksi gagal",
            "  berhasil di percobaan 3: data ke-3",
            "",
            "Angka tagihan dicetak rata kanan selebar 7.",
        ],
        "hints": [
            "initialize exception sendiri memanggil super(pesan) di akhir.",
            "rescue boleh ditulis langsung di dalam blok do...end sejak Ruby 2.6.",
            "retry mengulang blok begin dari awal — WAJIB dibatasi penghitung.",
            "Tangkap yang PALING SPESIFIK lebih dulu.",
        ],
        "solution": """class SaldoKurangError < StandardError
  attr_reader :kurang

  def initialize(kurang)
    @kurang = kurang
    super("saldo kurang #{kurang}")
  end
end

class Dompet
  attr_reader :saldo

  def initialize(saldo) = @saldo = saldo

  def bayar(jumlah)
    raise ArgumentError, "jumlah #{jumlah} tidak sah" unless jumlah.positive?
    raise SaldoKurangError, jumlah - @saldo if jumlah > @saldo

    @saldo -= jumlah
  end
end

d = Dompet.new(50_000)

[20_000, -5, 100_000, 30_000].each do |tagihan|
  d.bayar(tagihan)
  puts format("bayar %7d -> sisa %d", tagihan, d.saldo)
rescue SaldoKurangError => e
  puts format("bayar %7d -> GAGAL, kurang %d", tagihan, e.kurang)
rescue ArgumentError => e
  puts format("bayar %7d -> DITOLAK: %s", tagihan, e.message)
end

puts "---"

@panggilan = 0

def ambil_data
  @panggilan += 1
  raise IOError, "koneksi gagal" if @panggilan <= 2

  "data ke-#{@panggilan}"
end

percobaan = 0
begin
  percobaan += 1
  puts "berhasil di percobaan #{percobaan}: #{ambil_data}"
rescue IOError => e
  puts "percobaan #{percobaan} gagal: #{e.message}"
  retry if percobaan < 5
  raise
end""",
    },
    {
        "title": "Latihan 14: Enumerable Sendiri",
        "difficulty": "Sulit",
        "question": [
            "Buat class Kelas yang include Enumerable dan menyimpan murid",
            "dalam Hash nama -> nilai.",
            "",
            "  - tambah(nama, nilai) mengembalikan self supaya bisa dirantai",
            "  - each memberi pasangan [nama, nilai] TERURUT nilai MENURUN;",
            "    kalau nilainya sama, urut nama MENAIK",
            "  - size mengembalikan jumlah murid",
            "",
            "Buktikan bahwa dengan satu `each` saja, seluruh Enumerable",
            "ikut bekerja: pakai count, first, map, select, sum, dan",
            "partition TANPA menuliskan satu pun di class itu.",
            "",
            "Isi: Andi 88, Budi 72, Cici 95, Dedi 72, Euis 79",
            "",
            "Keluaran yang diharapkan:",
            "",
            "  Cici    95",
            "  Andi    88",
            "  Euis    79",
            "  Budi    72",
            "  Dedi    72",
            "  ---",
            "  jumlah   : 5",
            "  lulus    : 3",
            "  tertinggi: Cici",
            "  nama     : Cici, Andi, Euis, Budi, Dedi",
            "  total    : 406",
            "  lulus    : Cici, Andi, Euis",
            "  ulang    : Budi, Dedi",
        ],
        "hints": [
            "include Enumerable menuntut method each yang memakai yield.",
            "sort_by dengan array kunci: [-nilai, nama]",
            "first memberi elemen pertama dari each — di sini pasangan array.",
            "partition memecah jadi dua array: yang cocok dan yang tidak.",
        ],
        "solution": """class Kelas
  include Enumerable

  def initialize = @murid = {}

  def tambah(nama, nilai)
    @murid[nama] = nilai
    self
  end

  def each
    @murid.sort_by { |nama, nilai| [-nilai, nama] }
          .each { |nama, nilai| yield(nama, nilai) }
  end

  def size = @murid.size
end

k = Kelas.new
       .tambah("Andi", 88)
       .tambah("Budi", 72)
       .tambah("Cici", 95)
       .tambah("Dedi", 72)
       .tambah("Euis", 79)

k.each { |nama, nilai| puts "#{nama.ljust(8)}#{nilai}" }

puts "---"
puts "jumlah   : #{k.size}"
puts "lulus    : #{k.count { |_, n| n >= 75 }}"
puts "tertinggi: #{k.first[0]}"
puts "nama     : #{k.map { |nama, _| nama }.join(', ')}"
puts "total    : #{k.sum { |_, n| n }}"

lulus, ulang = k.partition { |_, n| n >= 75 }
puts "lulus    : #{lulus.map(&:first).join(', ')}"
puts "ulang    : #{ulang.map(&:first).join(', ')}\"""",
    },
    {
        "title": "Latihan 15: Mesin Keadaan Dokumen",
        "difficulty": "Sulit",
        "question": [
            "Buat class Dokumen dengan keadaan awal :draf dan tabel",
            "transisi berikut sebagai konstanta Hash:",
            "  draf      + :kirim     -> :ditinjau",
            "  ditinjau  + :setujui   -> :disetujui",
            "  ditinjau  + :tolak     -> :ditolak",
            "  disetujui + :terbitkan -> :terbit",
            "  ditolak   + :tarik     -> :draf",
            "",
            "Method lanjut(aksi):",
            "  - kalau transisinya sah, keadaan berubah dan mengembalikan",
            "    keadaan baru",
            "  - kalau tidak, lempar ArgumentError berpesan",
            "    \"<aksi> tidak sah dari <keadaan>\" dan keadaan TIDAK berubah",
            "",
            "Jalankan dari draf: kirim, terbitkan, setujui, tolak,",
            "terbitkan, tarik. Cetak hasil tiap langkah.",
            "",
            "Keluaran yang diharapkan:",
            "",
            "  draf      + kirim      -> ditinjau",
            "  ditinjau  + terbitkan  -> DITOLAK: terbitkan tidak sah dari ditinjau",
            "  ditinjau  + setujui    -> disetujui",
            "  disetujui + tolak      -> DITOLAK: tolak tidak sah dari disetujui",
            "  disetujui + terbitkan  -> terbit",
            "  terbit    + tarik      -> DITOLAK: tarik tidak sah dari terbit",
            "  ---",
            "  keadaan akhir: terbit",
            "",
            "Keadaan rata kiri 10, aksi rata kiri 11.",
        ],
        "hints": [
            "Hash berkunci array: { [:draf, :kirim] => :ditinjau, ... }",
            "TRANSISI.fetch([keadaan, aksi], nil) mencari dengan aman.",
            "freeze pada konstanta mencegahnya diubah tanpa sengaja.",
            "Simpan keadaan sebelum mencoba, supaya bisa dicetak apa pun hasilnya.",
        ],
        "solution": """class Dokumen
  TRANSISI = {
    %i[draf kirim] => :ditinjau,
    %i[ditinjau setujui] => :disetujui,
    %i[ditinjau tolak] => :ditolak,
    %i[disetujui terbitkan] => :terbit,
    %i[ditolak tarik] => :draf,
  }.freeze

  attr_reader :keadaan

  def initialize = @keadaan = :draf

  def lanjut(aksi)
    baru = TRANSISI[[@keadaan, aksi]]
    raise ArgumentError, "#{aksi} tidak sah dari #{@keadaan}" if baru.nil?

    @keadaan = baru
  end
end

d = Dokumen.new

%i[kirim terbitkan setujui tolak terbitkan tarik].each do |aksi|
  sebelum = d.keadaan
  hasil = d.lanjut(aksi)
  puts format("%-10s+ %-11s-> %s", sebelum, aksi, hasil)
rescue ArgumentError => e
  puts format("%-10s+ %-11s-> DITOLAK: %s", sebelum, aksi, e.message)
end

puts "---"
puts "keadaan akhir: #{d.keadaan}\"""",
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
            "  Struct Barang(kode, nama, stok, harga) dengan method subtotal",
            "  dan to_s berformat \"%-5s%-12s%2d%10d%12d\".",
            "  module Gerak dengan konstanta MASUK = :masuk, KELUAR = :keluar.",
            "  GudangError < StandardError sebagai induk, dengan turunan:",
            "  KodeSudahAdaError, KodeTidakDikenalError, JumlahTidakSahError,",
            "  StokTidakCukupError. Pesannya:",
            "    \"kode B01 sudah ada\"",
            "    \"kode B09 tidak dikenal\"",
            "    \"jumlah 0 tidak sah\"",
            "    \"stok cuma 4, diminta 10\"",
            "",
            "LAYANAN  class Gudang yang include Enumerable",
            "  - daftar(barang) -> tolak kode kembar, kembalikan self",
            "  - catat(kode, gerak, jumlah) -> kembalikan stok baru;",
            "    urutan periksa: kode dulu, lalu jumlah, baru kecukupan stok",
            "  - each -> barang terurut kode",
            "  - nilai_persediaan",
            "  - stok_menipis(batas) -> terurut stok naik lalu kode",
            "  Gudang TIDAK BOLEH memanggil puts sama sekali.",
            "",
            "ANTARMUKA",
            "  Daftarkan B01 Kabel 10 15000, B02 Adaptor 4 85000,",
            "            B03 Mouse 25 120000",
            "  Jalankan: Masuk B01 15, Keluar B02 10, Keluar B03 5,",
            "            Masuk B09 1, Keluar B03 0",
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
            "Struct.new(...) do ... end boleh memuat method sendiri.",
            "Satu `rescue GudangError` di antarmuka cukup menangani keempat "
            "galat sekaligus, sementara bug sungguhan tetap naik dan terlihat.",
            "include Enumerable + satu `each` langsung memberi sum, select, "
            "sort_by, dan count tanpa menulisnya.",
            "each WAJIB mengurutkan: keluaran yang urutannya tidak pasti "
            "mustahil diuji.",
            "capitalize pada :masuk memberi \"Masuk\".",
        ],
        "solution": """# ---------------------------------------------------------------- MODEL
Barang = Struct.new(:kode, :nama, :stok, :harga) do
  def subtotal = stok * harga
  def to_s = format("%-5s%-12s%2d%10d%12d", kode, nama, stok, harga, subtotal)
end

module Gerak
  MASUK = :masuk
  KELUAR = :keluar
end

class GudangError < StandardError; end

class KodeSudahAdaError < GudangError
  def initialize(kode) = super("kode #{kode} sudah ada")
end

class KodeTidakDikenalError < GudangError
  def initialize(kode) = super("kode #{kode} tidak dikenal")
end

class JumlahTidakSahError < GudangError
  def initialize(jumlah) = super("jumlah #{jumlah} tidak sah")
end

class StokTidakCukupError < GudangError
  def initialize(punya, diminta) = super("stok cuma #{punya}, diminta #{diminta}")
end

# -------------------------------------------------------------- LAYANAN
class Gudang
  include Enumerable

  def initialize = @isi = {}

  def daftar(barang)
    raise KodeSudahAdaError, barang.kode if @isi.key?(barang.kode)

    @isi[barang.kode] = barang
    self
  end

  def catat(kode, gerak, jumlah)
    barang = @isi[kode]
    raise KodeTidakDikenalError, kode if barang.nil?
    raise JumlahTidakSahError, jumlah unless jumlah.positive?

    baru = gerak == Gerak::MASUK ? barang.stok + jumlah : barang.stok - jumlah
    raise StokTidakCukupError.new(barang.stok, jumlah) if baru.negative?

    barang.stok = baru
  end

  def each(&) = @isi.values.sort_by(&:kode).each(&)

  def nilai_persediaan = sum(&:subtotal)

  def stok_menipis(batas)
    select { |b| b.stok < batas }.sort_by { |b| [b.stok, b.kode] }
  end
end

# ------------------------------------------------------------ ANTARMUKA
gudang = Gudang.new
gudang.daftar(Barang.new("B01", "Kabel", 10, 15_000))
      .daftar(Barang.new("B02", "Adaptor", 4, 85_000))
      .daftar(Barang.new("B03", "Mouse", 25, 120_000))

langkah = [
  ["B01", Gerak::MASUK, 15],
  ["B02", Gerak::KELUAR, 10],
  ["B03", Gerak::KELUAR, 5],
  ["B09", Gerak::MASUK, 1],
  ["B03", Gerak::KELUAR, 0],
]

langkah.each do |kode, gerak, jumlah|
  label = "#{gerak.to_s.capitalize} #{kode} #{jumlah}"
  puts "#{label} -> stok #{gudang.catat(kode, gerak, jumlah)}"
rescue GudangError => e
  puts "#{label} -> DITOLAK: #{e.message}"
end

puts "---"
gudang.each { |b| puts b }

puts "---"
puts "nilai persediaan: #{gudang.nilai_persediaan}"

menipis = gudang.stok_menipis(10).map { |b| "#{b.kode} #{b.nama} (#{b.stok})" }
puts "stok menipis (<10): #{menipis.join(', ')}\"""",
    },
]
