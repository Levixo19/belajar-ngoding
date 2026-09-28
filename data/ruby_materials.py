RUBY_MATERIALS = [
    {
        "title": "1. Pengenalan Ruby & Instalasi",
        "sections": [
            {
                "body": [
                    "Apa itu Ruby?",
                    "  - Dibuat Yukihiro Matsumoto (Matz) di Jepang, 1995.",
                    "  - Interpreted, dynamically typed, object-oriented.",
                    "  - Tujuan desainnya ditulis Matz sendiri: membuat",
                    "    PROGRAMMER bahagia, bukan membuat mesin efisien.",
                    "",
                    "Kalimat itu bukan slogan kosong — ia menjelaskan hampir",
                    "semua keputusan desain Ruby:",
                    "  - Hampir tidak ada tanda baca yang wajib.",
                    "  - Banyak cara menulis hal yang sama, dan kamu boleh",
                    "    memilih yang paling terbaca.",
                    "  - Method diberi nama seperti kalimat: empty?, save!,",
                    "    each_with_index.",
                    "",
                    "SEMUANYA OBJEK. Benar-benar semuanya:",
                    "  5.class          Integer",
                    "  nil.class        NilClass",
                    "  true.class       TrueClass",
                    "  Integer.class    Class",
                    "  5.times { ... }  angka pun punya method",
                    "",
                    "Tidak ada tipe primitif seperti di Java. Tidak ada",
                    "fungsi yang berdiri di luar objek — yang terlihat seperti",
                    "fungsi global sebenarnya method privat milik Object.",
                    "",
                    "Dipakai membangun: Ruby on Rails (GitHub, Shopify,",
                    "Airbnb, Basecamp), Homebrew, Jekyll, Vagrant, dan",
                    "sebagian besar alat bantu DevOps era 2010-an.",
                    "",
                    "Instalasi:",
                    "  - Fedora  : sudo dnf install ruby",
                    "  - Debian  : sudo apt install ruby-full",
                    "  - macOS   : brew install ruby",
                    "  - Windows : RubyInstaller dari https://rubyinstaller.org",
                    "  - Cek     : ruby --version",
                    "",
                    "Untuk mengelola beberapa versi sekaligus, pakai rbenv",
                    "atau rvm — kebiasaan standar di proyek Ruby.",
                    "",
                    "Menjalankan:",
                    "  ruby berkas.rb",
                    "  irb                 sesi interaktif",
                    "  ruby -e 'puts 1+1'  satu baris",
                    "  ruby -c berkas.rb   periksa sintaks",
                ]
            },
            {
                "heading": "Program pertama",
                "code": """puts "Halo Dunia!"
puts "Aku sedang belajar Ruby."

nama = "Andi"
puts "Halo, #{nama}! Umurmu #{2026 - 2006} tahun."

3.times { |i| puts "baris ke-#{i + 1}" }"""
            },
            {
                "body": [
                    "Yang langsung terlihat berbeda:",
                    "",
                    "  - TIDAK ADA titik koma.",
                    "  - TIDAK ADA tanda kurung wajib di pemanggilan method.",
                    "  - TIDAK ADA deklarasi tipe.",
                    "  - TIDAK ADA fungsi main. Kode dijalankan dari atas.",
                    "",
                    "  puts \"halo\"",
                    "    Mencetak lalu pindah baris. Kepanjangan dari",
                    "    'put string'. Untuk array, ia mencetak tiap elemen",
                    "    di baris sendiri.",
                    "",
                    "  print \"halo\"",
                    "    Tanpa pindah baris.",
                    "",
                    "  p objek",
                    "    Mencetak bentuk DEBUG (memanggil .inspect) dan",
                    "    mengembalikan objeknya. Ini yang kamu pakai saat",
                    "    mencari bug: `p` menunjukkan kutip pada string,",
                    "    sehingga \"5\" dan 5 bisa dibedakan.",
                    "",
                    "  pp objek",
                    "    Seperti p tapi berbaris rapi untuk struktur besar.",
                    "",
                    "INTERPOLASI memakai #{...} di dalam kutip GANDA. Di",
                    "dalamnya boleh ekspresi apa pun. Kutip tunggal tidak",
                    "menginterpolasi apa pun.",
                    "",
                    "`3.times { |i| ... }` adalah BLOK — gagasan paling khas",
                    "Ruby. Angka 3 diberi sepotong kode untuk dijalankan tiga",
                    "kali. Bukan perulangan bawaan bahasa, melainkan method",
                    "biasa milik Integer yang menerima blok.",
                    "",
                    "Konvensi penamaan Ruby:",
                    "  snake_case     variabel dan method",
                    "  PascalCase     class dan module",
                    "  SCREAMING      konstanta",
                    "  @nama          variabel instance",
                    "  @@nama         variabel class (jarang dipakai)",
                    "  $nama          variabel global (hindari)",
                    "  nama?          method yang mengembalikan true/false",
                    "  nama!          versi yang BERBAHAYA atau mengubah objek",
                ]
            },
        ],
    },
    {
        "title": "2. Variabel, Tipe & Objek",
        "sections": [
            {
                "body": [
                    "Variabel tidak dideklarasikan, cukup diisi:",
                    "",
                    "  nama = \"Andi\"",
                    "  umur = 20",
                    "  tinggi = 172.5",
                    "  aktif = true",
                    "  kosong = nil",
                    "",
                    "Tipe bawaan yang sering dipakai:",
                    "  Integer     bilangan bulat, ukurannya TIDAK TERBATAS",
                    "  Float       pecahan",
                    "  Rational    pecahan persis: 1r/3",
                    "  String      teks, BISA DIUBAH (berbeda dari Java/C#)",
                    "  Symbol      :nama, teks yang ringan dan tetap",
                    "  Array       daftar",
                    "  Hash        pasangan kunci-nilai",
                    "  Range       1..10 atau 1...10",
                    "  NilClass    nil",
                    "  TrueClass / FalseClass",
                    "",
                    "Integer Ruby tidak punya batas. `2 ** 200` menghasilkan",
                    "angka 61 digit yang benar, bukan melimpah jadi negatif.",
                    "",
                    "SYMBOL adalah hal yang tidak ada di kebanyakan bahasa:",
                    "",
                    "  :nama         sebuah Symbol",
                    "  \"nama\"        sebuah String",
                    "",
                    "Bedanya: symbol yang sama SELALU objek yang sama persis",
                    "di memori, sedangkan dua string dengan isi sama adalah",
                    "dua objek berbeda. Symbol dipakai untuk NAMA — kunci",
                    "hash, nama method, penanda status — sedangkan string",
                    "untuk DATA.",
                    "",
                    "  \"a\".object_id == \"a\".object_id    false",
                    "  :a.object_id == :a.object_id      true",
                    "",
                    "KEBENARAN di Ruby sangat sederhana, dan ini berbeda dari",
                    "hampir semua bahasa lain:",
                    "",
                    "  Hanya `false` dan `nil` yang FALSY.",
                    "  Segala sesuatu yang lain TRUTHY — termasuk 0, \"\",",
                    "  [], dan {}.",
                    "",
                    "Kalau kamu datang dari PHP, JavaScript, atau Python, ini",
                    "menghilangkan seluruh kelas jebakan sekaligus: `if 0`",
                    "di Ruby berarti benar.",
                    "",
                    "Konversi ditulis eksplisit:",
                    "  \"42\".to_i     42",
                    "  \"abc\".to_i    0     <- diam-diam, hati-hati",
                    "  Integer(\"abc\") melempar ArgumentError  <- lebih aman",
                    "  42.to_s       \"42\"",
                    "  \"3.5\".to_f    3.5",
                    "  :nama.to_s    \"nama\"",
                    "  \"nama\".to_sym :nama",
                ]
            },
            {
                "heading": "Melihat semuanya sebagai objek",
                "code": """# Semua punya class
[42, 3.14, "teks", :simbol, true, nil, [1], {a: 1}, (1..5)].each do |x|
  printf("%-12s %-12s %s\\n", x.inspect, x.class, x.respond_to?(:each))
end

puts "---"

# Integer tanpa batas
puts "2 ** 100 = #{2 ** 100}"
puts "digit    = #{(2 ** 100).to_s.length}"

puts "---"

# Symbol versus String
puts "string sama objeknya? #{"a".equal?("a")}"
puts "symbol sama objeknya? #{:a.equal?(:a)}"

puts "---"

# Hanya false dan nil yang falsy
[0, "", [], {}, false, nil].each do |x|
  puts "#{x.inspect.ljust(6)} -> #{x ? 'truthy' : 'falsy'}"
end

puts "---"

# Konversi
puts "\\"42\\".to_i    = #{"42".to_i}"
puts "\\"abc\\".to_i   = #{"abc".to_i}"
begin
  Integer("abc")
rescue ArgumentError => e
  puts "Integer(\\"abc\\") -> #{e.class}"
end"""
            },
            {
                "body": [
                    "Keluaran (bagian pentingnya):",
                    "  42           Integer      false",
                    "  3.14         Float        false",
                    "  \"teks\"       String       false",
                    "  :simbol      Symbol       false",
                    "  true         TrueClass    false",
                    "  nil          NilClass     false",
                    "  [1]          Array        true",
                    "  {a: 1}       Hash         true",
                    "  1..5         Range        true",
                    "  ---",
                    "  2 ** 100 = 1267650600228229401496703205376",
                    "  digit    = 31",
                    "  ---",
                    "  string sama objeknya? false",
                    "  symbol sama objeknya? true",
                    "  ---",
                    "  0      -> truthy",
                    "  \"\"     -> truthy",
                    "  []     -> truthy",
                    "  {}     -> truthy",
                    "  false  -> falsy",
                    "  nil    -> falsy",
                    "  ---",
                    "  \"42\".to_i    = 42",
                    "  \"abc\".to_i   = 0",
                    "  Integer(\"abc\") -> ArgumentError",
                    "",
                    "`respond_to?(:each)` menanyakan 'apakah objek ini punya",
                    "method bernama each?'. Ini inti DUCK TYPING: yang penting",
                    "bukan tipe sebuah objek, melainkan APA YANG BISA",
                    "DILAKUKANNYA. Kalau ia berjalan seperti bebek dan",
                    "bersuara seperti bebek, perlakukan sebagai bebek.",
                    "",
                    "Perbedaan `\"abc\".to_i` (memberi 0 diam-diam) dan",
                    "`Integer(\"abc\")` (melempar) adalah keputusan yang kamu",
                    "ambil setiap kali membaca masukan pengguna. Yang pertama",
                    "menyembunyikan kesalahan; yang kedua membuatnya terlihat.",
                ]
            },
        ],
    },
    {
        "title": "3. String & Symbol",
        "sections": [
            {
                "body": [
                    "Ruby punya banyak cara menulis string:",
                    "",
                    "  'apa adanya'       tanpa interpolasi",
                    "  \"dengan #{nilai}\"  dengan interpolasi dan escape",
                    "  %w[a b c]          array dari kata: ['a','b','c']",
                    "  %i[a b c]          array dari symbol: [:a,:b,:c]",
                    "  <<~TEKS ... TEKS   heredoc; ~ memotong indentasinya",
                    "",
                    "String di Ruby BISA DIUBAH — berbeda dari Java, C#,",
                    "Python, dan JavaScript:",
                    "",
                    "  s = \"halo\"",
                    "  s << \" dunia\"       s sendiri berubah",
                    "  s.upcase!           s sendiri jadi huruf besar",
                    "",
                    "Ini sumber bug yang perlu diwaspadai: kalau kamu mengoper",
                    "sebuah string ke method lain dan method itu memanggil",
                    "`<<`, string ASLI-mu ikut berubah. `.freeze` membekukannya",
                    "supaya percobaan mengubahnya jadi error.",
                    "",
                    "TANDA SERU sebagai akhiran method adalah konvensi, bukan",
                    "sintaks. Artinya: 'versi ini lebih berbahaya daripada",
                    "yang tanpa seru'. Biasanya itu berarti ia mengubah",
                    "objeknya sendiri:",
                    "",
                    "  s.upcase     kembalikan string BARU, s tidak berubah",
                    "  s.upcase!    UBAH s, kembalikan s -- atau nil kalau",
                    "               tidak ada yang berubah",
                    "",
                    "Yang mengembalikan nil itu jebakan nyata:",
                    "  \"ABC\".upcase!   -> nil, karena sudah huruf besar",
                    "",
                    "Jadi `x = s.upcase!` bisa membuat x jadi nil tanpa satu",
                    "pun error. Jangan merangkai method ber-seru.",
                    "",
                    "Method string yang paling sering dipakai:",
                    "  length / size          strip / lstrip / rstrip",
                    "  upcase / downcase      capitalize / swapcase",
                    "  include?(\"x\")          start_with? / end_with?",
                    "  index(\"x\")             sub / gsub (ganti)",
                    "  split(\",\")             chars / bytes / lines",
                    "  center(20) / ljust(10) / rjust(10)",
                    "  * 3                    ulang tiga kali",
                    "  reverse                tr(\"abc\", \"xyz\")",
                    "  to_i / to_f / to_sym   empty?",
                    "",
                    "Beda `sub` dan `gsub`: sub mengganti kemunculan PERTAMA,",
                    "gsub mengganti SEMUANYA (g = global).",
                ]
            },
            {
                "heading": "Mengolah teks",
                "code": """kalimat = "Ruby dirancang untuk membuat programmer bahagia"

puts "asli       : #{kalimat}"
puts "panjang    : #{kalimat.length}"
puts "kata       : #{kalimat.split.size}"
puts "besar      : #{kalimat.upcase}"
puts "terbalik   : #{kalimat.reverse}"
puts "ganti      : #{kalimat.gsub('programmer', 'orang')}"
puts "mulai Ruby?: #{kalimat.start_with?('Ruby')}"
puts "posisi     : #{kalimat.index('untuk')}"
puts "terpanjang : #{kalimat.split.max_by(&:length)}"

puts "---"

# Membangun string
sapaan = String.new
sapaan << "Halo"
sapaan << ", dunia"
sapaan << "!"
puts sapaan

# Beku: percobaan mengubahnya jadi error
tetap = "tidak boleh berubah".freeze
begin
  tetap << "!"
rescue FrozenError => e
  puts "FrozenError: #{e.message}"
end

puts "---"

# Heredoc dengan indentasi dipotong
nama = "Andi"
pesan = <<~TEKS
  Halo #{nama},

  Ini surat yang indentasinya
  dipotong otomatis oleh <<~
TEKS
puts pesan

puts "---"

# Perataan untuk tabel
[["Keyboard", 350_000], ["Mouse", 85_000], ["Monitor", 1_750_000]].each do |nama_barang, harga|
  puts "#{nama_barang.ljust(12)}#{harga.to_s.rjust(10)}"
end"""
            },
            {
                "body": [
                    "Keluaran (bagian pentingnya):",
                    "  asli       : Ruby dirancang untuk membuat programmer bahagia",
                    "  panjang    : 47",
                    "  kata       : 6",
                    "  besar      : RUBY DIRANCANG UNTUK MEMBUAT PROGRAMMER BAHAGIA",
                    "  terbalik   : aigahab remmargorp taubmem kutnu gnacnarid ybuR",
                    "  ganti      : Ruby dirancang untuk membuat orang bahagia",
                    "  mulai Ruby?: true",
                    "  posisi     : 15",
                    "  terpanjang : programmer",
                    "  ---",
                    "  Halo, dunia!",
                    "  FrozenError: can't modify frozen String: \"tidak boleh berubah\"",
                    "  ---",
                    "  Halo Andi,",
                    "",
                    "  Ini surat yang indentasinya",
                    "  dipotong otomatis oleh <<~",
                    "  ---",
                    "  Keyboard        350000",
                    "  Mouse            85000",
                    "  Monitor        1750000",
                    "",
                    "`max_by(&:length)` memakai dua hal sekaligus yang khas",
                    "Ruby. `max_by` mencari elemen dengan nilai terbesar",
                    "menurut sebuah blok, dan `&:length` adalah SINGKATAN",
                    "dari `{ |x| x.length }`.",
                    "",
                    "Bentuk `&:nama_method` disebut symbol-to-proc, dan ia",
                    "ada di mana-mana di kode Ruby:",
                    "  arr.map(&:upcase)",
                    "  arr.select(&:even?)",
                    "  arr.sort_by(&:length)",
                    "",
                    "`350_000` dengan garis bawah sama dengan 350000 — cuma",
                    "jauh lebih terbaca. Berlaku untuk semua angka.",
                    "",
                    "`<<~TEKS` (dengan tilde) memotong indentasi TERKECIL",
                    "dari setiap barisnya, sehingga heredoc bisa ditulis",
                    "menjorok mengikuti kode di sekitarnya tanpa spasi itu",
                    "ikut masuk ke hasilnya. Tanpa tilde (`<<-TEKS`), hanya",
                    "penanda penutupnya yang boleh menjorok.",
                ]
            },
        ],
    },
    {
        "title": "4. Array & Hash",
        "sections": [
            {
                "body": [
                    "ARRAY:",
                    "  a = [1, 2, 3]",
                    "  a = Array.new(3, 0)      [0, 0, 0]",
                    "  a = %w[apel jeruk pir]   tanpa kutip dan koma",
                    "",
                    "  a[0]       elemen pertama",
                    "  a[-1]      elemen TERAKHIR",
                    "  a[1..2]    irisan",
                    "  a[1, 2]    dua elemen mulai index 1",
                    "  a.first(2) / a.last(2)",
                    "  a.dig(0, 1) aman untuk array bersarang",
                    "",
                    "Indeks negatif menghitung dari belakang — fitur yang",
                    "menghemat banyak `length - 1`.",
                    "",
                    "  a.push(4) / a << 4     tambah di akhir",
                    "  a.unshift(0)           tambah di awal",
                    "  a.pop / a.shift        ambil dari akhir / awal",
                    "  a.insert(1, :x)",
                    "  a.delete(3) / a.delete_at(0)",
                    "  a.length / a.size / a.count",
                    "  a.include?(2)          a.empty?",
                    "  a.sort / a.sort_by { }",
                    "  a.reverse / a.uniq / a.flatten / a.compact",
                    "  a.sum / a.min / a.max / a.minmax",
                    "  a.join(\", \")           a.sample / a.shuffle",
                    "",
                    "`compact` membuang nil; `flatten` meratakan array",
                    "bersarang; `uniq` membuang duplikat (tidak perlu",
                    "diurutkan dulu, berbeda dari Rust).",
                    "",
                    "HASH:",
                    "  h = { \"nama\" => \"Andi\", \"umur\" => 20 }",
                    "  h = { nama: \"Andi\", umur: 20 }      kunci Symbol",
                    "",
                    "Bentuk kedua jauh lebih lazim: `nama:` adalah singkatan",
                    "dari `:nama =>`. Kunci symbol lebih cepat dan lebih",
                    "hemat memori.",
                    "",
                    "  h[:nama]                nil kalau tidak ada",
                    "  h.fetch(:nama)          MELEMPAR kalau tidak ada",
                    "  h.fetch(:x, \"bawaan\")   dengan nilai cadangan",
                    "  h[:kota] = \"Bandung\"",
                    "  h.key?(:nama) / h.value?(20)",
                    "  h.keys / h.values / h.size",
                    "  h.each { |k, v| ... }",
                    "  h.map / h.select / h.reject / h.sort_by",
                    "  h.merge(lain)           h.dig(:a, :b)",
                    "  h.transform_values { |v| v * 2 }",
                    "",
                    "`Hash.new(0)` membuat hash yang nilai bawaannya 0 —",
                    "idiom penghitung frekuensi yang paling ringkas di Ruby:",
                    "  hitung = Hash.new(0)",
                    "  kata.each { |k| hitung[k] += 1 }",
                ]
            },
            {
                "heading": "Array, hash, dan statistik",
                "code": """nilai = [78, 92, 65, 88, 71, 95, 59, 83]

puts "Data      : #{nilai.join(', ')}"
puts "Terurut   : #{nilai.sort.join(', ')}"
puts "Jumlah    : #{nilai.size}"
puts "Total     : #{nilai.sum}"
puts "Rata-rata : #{'%.2f' % (nilai.sum.to_f / nilai.size)}"
puts "Tertinggi : #{nilai.max}"
puts "Terendah  : #{nilai.min}"

rata = nilai.sum.to_f / nilai.size
puts "Di atas rata-rata: #{nilai.select { |n| n > rata }.join(', ')}"

puts "---"

murid = [
  { nama: "Andi", kelas: "A", nilai: 88 },
  { nama: "Budi", kelas: "B", nilai: 72 },
  { nama: "Cici", kelas: "A", nilai: 95 },
  { nama: "Dedi", kelas: "B", nilai: 64 },
]

murid.sort_by { |m| -m[:nilai] }.each do |m|
  puts "#{m[:nama].ljust(6)}#{m[:kelas]} #{m[:nilai].to_s.rjust(3)}"
end

puts "---"

# group_by menghasilkan hash: kunci -> array
murid.group_by { |m| m[:kelas] }.sort.each do |kelas, anggota|
  rata_kelas = anggota.sum { |m| m[:nilai] }.to_f / anggota.size
  puts "Kelas #{kelas}: #{anggota.size} murid, rata-rata #{'%.1f' % rata_kelas}"
end

puts "---"

# Hash.new(0): idiom penghitung
kata = "kucing makan ikan kucing tidur ikan kucing".split
hitung = Hash.new(0)
kata.each { |k| hitung[k] += 1 }

hitung.sort_by { |k, n| [-n, k] }.each do |k, n|
  puts "#{k.ljust(7)}: #{n}"
end
puts "kata unik  : #{hitung.size}"
puts "total kata : #{kata.size}\""""
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
                    "  Cici  A  95",
                    "  Andi  A  88",
                    "  Budi  B  72",
                    "  Dedi  B  64",
                    "  ---",
                    "  Kelas A: 2 murid, rata-rata 91.5",
                    "  Kelas B: 2 murid, rata-rata 68.0",
                    "  ---",
                    "  kucing : 3",
                    "  ikan   : 2",
                    "  makan  : 1",
                    "  tidur  : 1",
                    "  kata unik  : 4",
                    "  total kata : 7",
                    "",
                    "Beberapa idiom Ruby yang muncul di situ:",
                    "",
                    "  `sort_by { |m| -m[:nilai] }`  tanda minus untuk urutan",
                    "  MENURUN. Lebih pendek daripada sort lalu reverse.",
                    "",
                    "  `sort_by { |k, n| [-n, k] }`  ARRAY sebagai kunci",
                    "  urutan: bandingkan elemen pertama dulu, kalau sama baru",
                    "  yang kedua. Ini cara termudah mengurutkan dua tingkat",
                    "  di Ruby.",
                    "",
                    "  `'%.2f' % nilai`  operator % pada string adalah",
                    "  format ala printf. Setara `format('%.2f', nilai)`.",
                    "",
                    "  `nilai.sum.to_f / nilai.size`  `.to_f` wajib: dua",
                    "  Integer dibagi menghasilkan Integer, dan sisanya",
                    "  dibuang. `631 / 8` adalah 78, bukan 78.875.",
                    "",
                    "  `group_by` menghasilkan Hash yang nilainya array.",
                    "  Memanggil `.sort` pada hash menghasilkan array pasangan",
                    "  terurut kunci — cara ringkas mendapat keluaran yang",
                    "  urutannya pasti.",
                ]
            },
        ],
    },
    {
        "title": "5. Kendali Alur",
        "sections": [
            {
                "body": [
                    "Percabangan:",
                    "",
                    "  if nilai >= 75",
                    "    puts \"Lulus\"",
                    "  elsif nilai >= 60",
                    "    puts \"Mengulang\"",
                    "  else",
                    "    puts \"Tidak Lulus\"",
                    "  end",
                    "",
                    "Perhatikan `elsif` — satu f. Tidak ada kurung di sekitar",
                    "kondisi, tidak ada kurung kurawal, dan blok ditutup `end`.",
                    "",
                    "MODIFIER — kondisi ditulis di BELAKANG, untuk pernyataan",
                    "pendek:",
                    "  puts \"Lulus\" if nilai >= 75",
                    "  return if daftar.empty?",
                    "  puts \"Kosong\" unless daftar.any?",
                    "",
                    "`unless` adalah `if not`, dan ia sangat khas Ruby. Pakai",
                    "kalau kondisi positifnya lebih enak dibaca. JANGAN pakai",
                    "`unless` dengan `else` — hampir selalu membingungkan.",
                    "",
                    "if adalah EKSPRESI, jadi menghasilkan nilai:",
                    "  status = if nilai >= 75 then \"lulus\" else \"ulang\" end",
                    "",
                    "CASE — jauh lebih kuat daripada switch di bahasa lain:",
                    "",
                    "  grade = case nilai",
                    "          when 85..100 then \"A\"",
                    "          when 75...85 then \"B\"",
                    "          when 60...75 then \"C\"",
                    "          else \"D\"",
                    "          end",
                    "",
                    "`when` memakai operator === yang perilakunya berbeda per",
                    "tipe:",
                    "  Range === angka     apakah angkanya di dalam rentang",
                    "  Class === objek     apakah objeknya bertipe itu",
                    "  Regexp === string   apakah polanya cocok",
                    "  Proc === nilai      hasil pemanggilan lambda",
                    "  selain itu          perbandingan == biasa",
                    "",
                    "Jadi satu `case` bisa mencampur rentang, tipe, dan pola",
                    "regex dalam satu blok — sesuatu yang tidak bisa dilakukan",
                    "switch di C atau Java.",
                    "",
                    "Perulangan — tapi jarang dipakai di Ruby:",
                    "  while i < 5 ... end",
                    "  until selesai ... end",
                    "  loop do ... break ... end",
                    "  for x in arr ... end      (hampir tidak pernah dipakai)",
                    "",
                    "Yang BENAR-BENAR dipakai adalah method beriterasi:",
                    "  5.times { |i| ... }",
                    "  1.upto(5) { |i| ... }",
                    "  (1..5).each { |i| ... }",
                    "  arr.each { |x| ... }",
                    "  arr.each_with_index { |x, i| ... }",
                    "",
                    "Kalau kamu menulis `for` di Ruby, hampir pasti ada cara",
                    "yang lebih terbaca.",
                ]
            },
            {
                "heading": "case yang mencampur banyak jenis pola",
                "code": """def jelaskan(x)
  case x
  when nil            then "kosong"
  when 0              then "nol"
  when 1..9           then "satuan #{x}"
  when 10..99         then "puluhan #{x}"
  when Integer        then "bilangan besar #{x}"
  when Float          then "pecahan #{x}"
  when /\\A\\d+\\z/      then "teks berisi angka: #{x}"
  when String         then "teks #{x.length} huruf"
  when Array          then "array #{x.size} elemen"
  when ->(v) { v.respond_to?(:each) } then "sesuatu yang bisa ditelusuri"
  else                     "tipe lain: #{x.class}"
  end
end

[nil, 0, 5, 42, 1234, 3.14, "123", "halo", [1, 2], { a: 1 }, :simbol].each do |x|
  puts jelaskan(x)
end

puts "---"

# Modifier dan unless
[95, 80, 50].each do |n|
  puts "#{n}: istimewa" if n >= 90
  puts "#{n}: perlu bimbingan" unless n >= 75
end

puts "---"

# case tanpa subjek: seperti rantai if
suhu = 31
saran = case
        when suhu < 15 then "pakai jaket"
        when suhu < 25 then "nyaman"
        when suhu < 33 then "panas, minum air"
        else                "sangat panas"
        end
puts "suhu #{suhu}: #{saran}"

puts "---"

# Perulangan dengan method, bukan for
3.downto(1) { |i| print "#{i} " }
puts "lepas landas!"

hasil = (1..20).each_with_object([]) do |n, kumpulan|
  kumpulan << n if n % 3 == 0 && n.odd?
end
puts "kelipatan 3 yang ganjil: #{hasil.join(', ')}\""""
            },
            {
                "body": [
                    "Keluaran:",
                    "  kosong",
                    "  nol",
                    "  satuan 5",
                    "  puluhan 42",
                    "  bilangan besar 1234",
                    "  satuan 3.14",
                    "  teks berisi angka: 123",
                    "  teks 4 huruf",
                    "  array 2 elemen",
                    "  sesuatu yang bisa ditelusuri",
                    "  tipe lain: Symbol",
                    "  ---",
                    "  95: istimewa",
                    "  50: perlu bimbingan",
                    "  ---",
                    "  suhu 31: panas, minum air",
                    "  ---",
                    "  3 2 1 lepas landas!",
                    "  kelipatan 3 yang ganjil: 3, 9, 15",
                    "",
                    "URUTAN BERARTI di `case`: `when 1..9` harus sebelum",
                    "`when Integer`, kalau tidak semua bilangan akan tertangkap",
                    "cabang Integer lebih dulu. Ruby tidak memperingatkanmu",
                    "soal ini — berbeda dari Rust dan C#.",
                    "",
                    "`->(v) { ... }` adalah LAMBDA, dan ia bisa dipakai di",
                    "`when` karena Proc mengimplementasi `===` sebagai",
                    "'panggil aku dengan nilai ini'. Ini memungkinkan syarat",
                    "sebebas apa pun di dalam case.",
                    "",
                    "`each_with_object([])` menelusuri sambil membawa sebuah",
                    "wadah. Bedanya dengan `reduce`: wadahnya SELALU yang",
                    "dikembalikan, jadi kamu tidak perlu mengingat untuk",
                    "mengembalikannya di tiap putaran — kesalahan yang sangat",
                    "sering di `reduce`.",
                    "",
                    "`n.odd?` dan `n.even?` adalah contoh konvensi tanda tanya:",
                    "method yang mengembalikan true atau false diberi akhiran",
                    "`?`. Ia membuat kondisi terbaca seperti kalimat.",
                ]
            },
        ],
    },
    {
        "title": "6. Blok, Proc & Lambda",
        "sections": [
            {
                "body": [
                    "BLOK adalah gagasan paling khas Ruby: sepotong kode yang",
                    "dioper ke sebuah method.",
                    "",
                    "  arr.each { |x| puts x }",
                    "",
                    "  arr.each do |x|",
                    "    puts x",
                    "  end",
                    "",
                    "Keduanya identik. Konvensinya: kurung kurawal untuk satu",
                    "baris, `do...end` untuk beberapa baris.",
                    "",
                    "Method menerima blok lewat `yield`:",
                    "",
                    "  def tiga_kali",
                    "    yield 1",
                    "    yield 2",
                    "    yield 3",
                    "  end",
                    "",
                    "  tiga_kali { |n| puts \"ke-#{n}\" }",
                    "",
                    "`block_given?` memeriksa apakah ada blok yang dioper.",
                    "Tanpa pemeriksaan itu, `yield` tanpa blok melempar",
                    "LocalJumpError.",
                    "",
                    "Pola paling berharga dari blok adalah MENJAMIN",
                    "PEMBERSIHAN:",
                    "",
                    "  File.open(\"data.txt\") do |f|",
                    "      ...",
                    "  end          # berkas ditutup di sini, GAGAL ATAU TIDAK",
                    "",
                    "Ini padanan `using` di C# dan `with` di Python, tapi",
                    "dibangun dari mekanisme yang sama persis dengan `each` —",
                    "bukan sintaks khusus.",
                    "",
                    "PROC dan LAMBDA adalah blok yang disimpan jadi objek:",
                    "",
                    "  kuadrat = ->(x) { x * x }      lambda, bentuk panah",
                    "  kuadrat = lambda { |x| x * x }",
                    "  kuadrat = proc { |x| x * x }   Proc",
                    "  kuadrat.call(4)  /  kuadrat.(4)  /  kuadrat[4]",
                    "",
                    "DUA PERBEDAAN antara proc dan lambda, dan keduanya",
                    "penting:",
                    "",
                    "  1. JUMLAH ARGUMEN. Lambda ketat: salah jumlah",
                    "     melempar ArgumentError. Proc longgar: yang kurang",
                    "     jadi nil, yang lebih dibuang.",
                    "",
                    "  2. RETURN. `return` di dalam lambda keluar dari",
                    "     LAMBDA-nya. `return` di dalam proc keluar dari",
                    "     METHOD yang membuatnya — sering mengejutkan.",
                    "",
                    "Aturan praktis: pakai lambda kecuali kamu punya alasan",
                    "khusus.",
                    "",
                    "`&` mengubah blok jadi objek dan sebaliknya:",
                    "  def f(&blok)      tangkap bloknya sebagai Proc",
                    "  arr.map(&kuadrat) oper lambda sebagai blok",
                    "  arr.map(&:upcase) symbol-to-proc",
                ]
            },
            {
                "heading": "Blok, yield, dan lambda",
                "code": """# Method yang menerima blok
def ulangi(n)
  return to_enum(:ulangi, n) unless block_given?

  hasil = []
  n.times { |i| hasil << yield(i + 1) }
  hasil
end

puts ulangi(5) { |i| i * i }.inspect
puts ulangi(3) { |i| "baris #{i}" }.inspect

puts "---"

# Blok yang MENJAMIN pembersihan
def dengan_pengukur(nama)
  puts "mulai #{nama}"
  hasil = yield
  puts "selesai #{nama}"
  hasil
ensure
  puts "(pembersihan #{nama})"
end

nilai = dengan_pengukur("hitung") { 6 * 7 }
puts "nilai = #{nilai}"

begin
  dengan_pengukur("gagal") { raise "ada masalah" }
rescue RuntimeError => e
  puts "tertangkap: #{e.message}"
end

puts "---"

# Lambda versus Proc: jumlah argumen
l = ->(a, b) { "lambda #{a} #{b}" }
pr = proc { |a, b| "proc #{a.inspect} #{b.inspect}" }

puts l.call(1, 2)
puts pr.call(1, 2)
puts pr.call(1)            # b jadi nil, tanpa error
begin
  l.call(1)
rescue ArgumentError => e
  puts "lambda menolak: #{e.class}"
end

puts "---"

# Lambda sebagai nilai yang dioper
operasi = {
  tambah: ->(a, b) { a + b },
  kurang: ->(a, b) { a - b },
  kali:   ->(a, b) { a * b },
}

operasi.each do |nama, fn|
  puts "#{nama.to_s.ljust(7)}(9, 4) = #{fn.call(9, 4)}"
end

puts "---"

# &:symbol dan &lambda
kata = %w[ruby adalah bahasa yang menyenangkan]
puts kata.map(&:upcase).join(" ")
puts kata.select { |k| k.length > 5 }.inspect

panjang = ->(s) { s.length }
puts kata.map(&panjang).inspect"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  [1, 4, 9, 16, 25]",
                    "  [\"baris 1\", \"baris 2\", \"baris 3\"]",
                    "  ---",
                    "  mulai hitung",
                    "  selesai hitung",
                    "  (pembersihan hitung)",
                    "  nilai = 42",
                    "  mulai gagal",
                    "  (pembersihan gagal)",
                    "  tertangkap: ada masalah",
                    "  ---",
                    "  lambda 1 2",
                    "  proc 1 2",
                    "  proc 1 nil",
                    "  lambda menolak: ArgumentError",
                    "  ---",
                    "  tambah (9, 4) = 13",
                    "  kurang (9, 4) = 5",
                    "  kali   (9, 4) = 36",
                    "  ---",
                    "  RUBY ADALAH BAHASA YANG MENYENANGKAN",
                    "  [\"adalah\", \"bahasa\", \"menyenangkan\"]",
                    "  [4, 6, 6, 4, 12]",
                    "",
                    "Perhatikan bagian `ensure`: ia dijalankan BAHKAN saat",
                    "bloknya melempar exception — 'selesai gagal' tidak",
                    "tercetak, tapi '(pembersihan gagal)' tetap. Inilah yang",
                    "membuat pola blok bisa menjamin berkas ditutup dan",
                    "koneksi dilepas.",
                    "",
                    "`return to_enum(:ulangi, n) unless block_given?` adalah",
                    "idiom pustaka standar: kalau dipanggil tanpa blok, method",
                    "mengembalikan Enumerator alih-alih gagal. Itu sebabnya",
                    "`arr.each` tanpa blok tetap berguna — ia memberi objek",
                    "yang bisa dirantai.",
                    "",
                    "Ketiga bentuk pemanggilan lambda — `.call(x)`, `.(x)`,",
                    "dan `[x]` — identik. Yang paling umum dipakai `.call`",
                    "karena paling jelas.",
                ]
            },
        ],
    },
    {
        "title": "7. Enumerable: Kekuatan Sesungguhnya",
        "sections": [
            {
                "body": [
                    "Enumerable adalah module yang memberi PULUHAN method",
                    "kepada apa pun yang punya `each`. Array, Hash, Range,",
                    "Set, dan Enumerator semuanya mendapatnya.",
                    "",
                    "Ini pola desain yang layak dipahami: kamu mengimplementasi",
                    "SATU method, dan mendapat lima puluh gratis.",
                    "",
                    "MENGUBAH:",
                    "  map / collect          ubah tiap elemen",
                    "  flat_map               ubah lalu ratakan",
                    "  each_with_index        bawa indeksnya",
                    "  each_with_object(x)    bawa wadah",
                    "  each_slice(3)          potong per 3",
                    "  each_cons(2)           jendela geser 2",
                    "  zip(lain)              pasangkan",
                    "  chunk_while { }        kelompokkan yang berurutan",
                    "",
                    "MENYARING:",
                    "  select / filter        ambil yang cocok",
                    "  reject                 buang yang cocok",
                    "  find / detect          yang PERTAMA cocok",
                    "  filter_map             saring dan ubah sekaligus",
                    "  take(3) / drop(3)",
                    "  take_while / drop_while",
                    "  grep(/pola/)           saring dengan ===",
                    "  uniq / compact",
                    "",
                    "MERINGKAS:",
                    "  reduce / inject        lipat jadi satu nilai",
                    "  sum / count / tally",
                    "  min / max / minmax",
                    "  min_by / max_by / sort_by",
                    "  group_by               kelompokkan jadi Hash",
                    "  partition              pecah jadi dua: cocok & tidak",
                    "  all? / any? / none? / one?",
                    "  first(n) / include?",
                    "",
                    "`tally` (Ruby 2.7) menghitung frekuensi dalam satu",
                    "panggilan — menggantikan seluruh idiom Hash.new(0):",
                    "  kata.tally    # => {\"kucing\"=>3, \"ikan\"=>2, ...}",
                    "",
                    "`reduce` layak dipahami karena ia dasar dari banyak yang",
                    "lain:",
                    "  [1,2,3].reduce(0) { |total, x| total + x }   6",
                    "  [1,2,3].reduce(:+)                           6",
                    "  [1,2,3].sum                                  6",
                    "",
                    "LAZY: untuk deret besar atau tak terbatas, `.lazy`",
                    "membuat rantainya hanya menghitung yang benar-benar",
                    "diminta:",
                    "  (1..Float::INFINITY).lazy",
                    "      .map { |x| x * x }",
                    "      .select { |x| x % 3 == 0 }",
                    "      .first(5)",
                ]
            },
            {
                "heading": "Rantai Enumerable pada data nyata",
                "code": """Murid = Struct.new(:nama, :kelas, :nilai)

data = [
  Murid.new("Andi",  "A", 88),
  Murid.new("Budi",  "B", 72),
  Murid.new("Cici",  "A", 95),
  Murid.new("Dedi",  "B", 64),
  Murid.new("Euis",  "A", 79),
  Murid.new("Fajar", "B", 91),
]

puts "-- Lulus, nilai tertinggi dulu --"
data.select { |m| m.nilai >= 75 }
    .sort_by { |m| -m.nilai }
    .each { |m| puts "  #{m.nama.ljust(6)}#{m.kelas} #{m.nilai}" }

puts
puts "rata-rata : #{'%.2f' % (data.sum(&:nilai).to_f / data.size)}"
puts "tertinggi : #{data.max_by(&:nilai).nama}"
puts "lulus     : #{data.count { |m| m.nilai >= 75 }}"
puts "ada <65?  : #{data.any? { |m| m.nilai < 65 }}"
puts "semua >60?: #{data.all? { |m| m.nilai > 60 }}"

puts
puts "-- partition --"
lulus, ulang = data.partition { |m| m.nilai >= 75 }
puts "lulus : #{lulus.map(&:nama).join(', ')}"
puts "ulang : #{ulang.map(&:nama).join(', ')}"

puts
puts "-- group_by + transform_values --"
data.group_by(&:kelas)
    .transform_values { |a| (a.sum(&:nilai).to_f / a.size).round(1) }
    .sort
    .each { |kelas, rata| puts "Kelas #{kelas}: #{rata}" }

puts
puts "-- tally --"
kata = "kucing makan ikan kucing tidur ikan kucing".split
kata.tally.sort_by { |k, n| [-n, k] }.each { |k, n| puts "#{k.ljust(7)}: #{n}" }

puts
puts "-- reduce --"
puts "total nilai : #{data.reduce(0) { |t, m| t + m.nilai }}"
puts "nama digabung: #{data.map(&:nama).reduce { |a, b| "#{a}|#{b}" }}"

puts
puts "-- lazy pada deret tak terbatas --"
kuadrat_kelipatan3 = (1..Float::INFINITY).lazy
                                         .map { |x| x * x }
                                         .select { |x| x % 3 == 0 }
                                         .first(5)
puts kuadrat_kelipatan3.inspect

puts
puts "-- each_cons: selisih antar nilai terurut --"
terurut = data.map(&:nilai).sort
puts terurut.each_cons(2).map { |a, b| b - a }.inspect"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  -- Lulus, nilai tertinggi dulu --",
                    "    Cici  A 95",
                    "    Fajar B 91",
                    "    Andi  A 88",
                    "    Euis  A 79",
                    "",
                    "  rata-rata : 81.50",
                    "  tertinggi : Cici",
                    "  lulus     : 4",
                    "  ada <65?  : true",
                    "  semua >60?: true",
                    "",
                    "  -- partition --",
                    "  lulus : Andi, Cici, Euis, Fajar",
                    "  ulang : Budi, Dedi",
                    "",
                    "  -- group_by + transform_values --",
                    "  Kelas A: 87.3",
                    "  Kelas B: 75.7",
                    "",
                    "  -- tally --",
                    "  kucing : 3",
                    "  ikan   : 2",
                    "  makan  : 1",
                    "  tidur  : 1",
                    "",
                    "  -- reduce --",
                    "  total nilai : 489",
                    "  nama digabung: Andi|Budi|Cici|Dedi|Euis|Fajar",
                    "",
                    "  -- lazy pada deret tak terbatas --",
                    "  [9, 36, 81, 144, 225]",
                    "",
                    "  -- each_cons: selisih antar nilai terurut --",
                    "  [8, 7, 9, 3, 4]",
                    "",
                    "`Struct.new(:nama, :kelas, :nilai)` membuat class dengan",
                    "tiga atribut, constructor, `==` berbasis nilai, dan",
                    "`to_s` — semuanya dalam satu baris. Padanan `record` di",
                    "C# dan `data class` di Kotlin.",
                    "",
                    "Bagian `lazy` menjalankan rantai pada deret TAK",
                    "TERBATAS. Tanpa `.lazy`, `map` pada `(1..Float::INFINITY)`",
                    "akan menggantung selamanya. Dengan `.lazy`, ia berhenti",
                    "begitu `first(5)` puas.",
                    "",
                    "`data.sum(&:nilai)` adalah gabungan dua idiom: `sum`",
                    "dengan blok, dan symbol-to-proc. Ia setara",
                    "`data.map { |m| m.nilai }.sum` tapi tanpa membuat array",
                    "perantara.",
                ]
            },
        ],
    },
    {
        "title": "8. Method & Argumen",
        "sections": [
            {
                "body": [
                    "  def sapa(nama)",
                    "    \"Halo, #{nama}!\"",
                    "  end",
                    "",
                    "Nilai kembalian adalah EKSPRESI TERAKHIR yang dievaluasi.",
                    "`return` ada tapi hanya dipakai untuk keluar lebih awal.",
                    "Menulis `return` di baris terakhir dianggap berlebihan",
                    "oleh pembaca Ruby.",
                    "",
                    "Empat jenis argumen, dan Ruby punya semuanya:",
                    "",
                    "  POSISIONAL",
                    "    def f(a, b)",
                    "",
                    "  BAWAAN",
                    "    def f(a, b = 10)",
                    "",
                    "  BERKUNCI (keyword)",
                    "    def f(nama:, umur: 0)",
                    "    f(nama: \"Andi\")          umur pakai bawaannya",
                    "",
                    "  BEBAS JUMLAHNYA",
                    "    def f(*angka)            kumpulkan jadi array",
                    "    def f(**opsi)            kumpulkan jadi hash",
                    "    def f(&blok)             tangkap bloknya",
                    "",
                    "Argumen berkunci TANPA nilai bawaan (`nama:`) WAJIB",
                    "diisi. Ini fitur yang sangat berguna: pemanggilan jadi",
                    "menjelaskan dirinya sendiri dan urutannya tidak penting.",
                    "",
                    "  gambar(tebal: true, miring: false)",
                    "",
                    "jauh lebih baik daripada `gambar(true, false)`.",
                    "",
                    "Operator SPLAT membongkar koleksi:",
                    "  a = [1, 2, 3]",
                    "  f(*a)             sama dengan f(1, 2, 3)",
                    "  h = { x: 1 }",
                    "  g(**h)            sama dengan g(x: 1)",
                    "",
                    "METHOD BERTANDA BACA adalah konvensi yang sangat",
                    "informatif:",
                    "  kosong?      kembalikan true/false",
                    "  simpan!      berbahaya: mengubah objek atau melempar",
                    "  nama=        setter, dipanggil sebagai `obj.nama = x`",
                    "  <=> == []  +  semua operator adalah method biasa",
                    "",
                    "Bahwa operator adalah method biasa berarti kamu bisa",
                    "mendefinisikannya untuk class-mu sendiri:",
                    "  def +(lain) ... end",
                    "  def <=>(lain) ... end",
                    "  def [](indeks) ... end",
                ]
            },
            {
                "heading": "Semua bentuk argumen",
                "code": """def laporan(judul, *baris, pemisah: "-", lebar: 40, **opsi)
  puts judul.center(lebar, pemisah)
  baris.each_with_index { |b, i| puts "#{(i + 1).to_s.rjust(2)}. #{b}" }
  opsi.each { |k, v| puts "   #{k}: #{v}" }
  puts pemisah * lebar
  baris.size
end

n = laporan("REKAP", "Kopi 3x", "Teh 5x", "Roti 2x",
            pemisah: "=", lebar: 30, tanggal: "2026-09-22", kasir: "Andi")
puts "jumlah baris: #{n}"

puts

# Argumen berkunci wajib
def buat_akun(nama:, email:, aktif: true)
  "#{nama} <#{email}> #{aktif ? '[aktif]' : '[nonaktif]'}"
end

puts buat_akun(email: "andi@contoh.id", nama: "Andi")
puts buat_akun(nama: "Budi", email: "budi@contoh.id", aktif: false)

begin
  buat_akun(nama: "Cici")
rescue ArgumentError => e
  puts "ditolak: #{e.message}"
end

puts

# Splat membongkar koleksi
angka = [4, 9, 16]
def akar(*n) = n.map { |x| Integer(Math.sqrt(x)) }
puts akar(*angka).inspect

setelan = { lebar: 20, pemisah: "*" }
laporan("KECIL", "satu", **setelan)

puts

# Operator adalah method biasa
class Uang
  include Comparable
  attr_reader :jumlah

  def initialize(jumlah) = @jumlah = jumlah
  def +(lain) = Uang.new(@jumlah + lain.jumlah)
  def -(lain) = Uang.new(@jumlah - lain.jumlah)
  def <=>(lain) = @jumlah <=> lain.jumlah
  def to_s = "Rp#{@jumlah.to_s.reverse.scan(/\\d{1,3}/).join('.').reverse}"
end

a = Uang.new(150_000)
b = Uang.new(75_500)

puts "a       = #{a}"
puts "b       = #{b}"
puts "a + b   = #{a + b}"
puts "a - b   = #{a - b}"
puts "a > b   = #{a > b}"
puts "terbesar= #{[a, b, Uang.new(99_000)].max}\""""
            },
            {
                "body": [
                    "Keluaran (bagian pentingnya):",
                    "  ======REKAP=======",
                    "   1. Kopi 3x",
                    "   2. Teh 5x",
                    "   3. Roti 2x",
                    "     tanggal: 2026-09-22",
                    "     kasir: Andi",
                    "  ==============================",
                    "  jumlah baris: 3",
                    "",
                    "  Andi <andi@contoh.id> [aktif]",
                    "  Budi <budi@contoh.id> [nonaktif]",
                    "  ditolak: missing keyword: :email",
                    "",
                    "  [2, 3, 4]",
                    "  ...",
                    "  a       = Rp150.000",
                    "  b       = Rp75.500",
                    "  a + b   = Rp225.500",
                    "  a - b   = Rp74.500",
                    "  a > b   = true",
                    "  terbesar= Rp150.000",
                    "",
                    "Class Uang menunjukkan dua hal berharga sekaligus.",
                    "",
                    "PERTAMA, operator adalah method. Dengan mendefinisikan",
                    "`+` dan `-`, objekmu bisa dipakai dengan sintaks yang",
                    "sama seperti angka.",
                    "",
                    "KEDUA, `include Comparable` beserta satu method `<=>`",
                    "memberi kamu `<`, `>`, `<=`, `>=`, `==`, `between?`,",
                    "`clamp`, DAN membuat `.max`, `.min`, `.sort` bekerja",
                    "pada array berisi objek itu. Satu method, sebelas",
                    "kemampuan.",
                    "",
                    "`def akar(*n) = ...` memakai ENDLESS METHOD (Ruby 3.0):",
                    "method satu ekspresi ditulis dengan tanda sama dengan,",
                    "tanpa `end`. Cocok untuk getter dan perhitungan pendek.",
                ]
            },
        ],
    },
    {
        "title": "9. Class & Objek",
        "sections": [
            {
                "body": [
                    "  class Murid",
                    "    def initialize(nama, nilai)",
                    "      @nama = nama",
                    "      @nilai = nilai",
                    "    end",
                    "",
                    "    def nama = @nama",
                    "  end",
                    "",
                    "  m = Murid.new(\"Andi\", 88)",
                    "",
                    "`initialize` adalah constructor, dan ia dipanggil",
                    "otomatis oleh `.new`. Namanya bukan `new` — `new` adalah",
                    "method class yang membuat objek lalu memanggil",
                    "`initialize`.",
                    "",
                    "`@nama` adalah VARIABEL INSTANCE. Ia otomatis privat:",
                    "tidak ada cara mengaksesnya dari luar tanpa method.",
                    "Membacanya sebelum diisi memberi `nil`, bukan error.",
                    "",
                    "ATTR untuk membuat getter dan setter otomatis:",
                    "  attr_reader :nama          hanya baca",
                    "  attr_writer :nilai         hanya tulis",
                    "  attr_accessor :nilai       keduanya",
                    "",
                    "Satu baris `attr_reader :nama` menggantikan:",
                    "  def nama",
                    "    @nama",
                    "  end",
                    "",
                    "VISIBILITAS:",
                    "  public      bawaan",
                    "  private     hanya dari dalam objek yang sama",
                    "  protected   boleh dari objek lain BERKELAS SAMA",
                    "",
                    "  private",
                    "  def rahasia",
                    "    ...",
                    "  end",
                    "",
                    "Semua method SESUDAH kata `private` jadi privat. Sejak",
                    "Ruby 3.0 bisa juga per-method: `private def rahasia ... end`",
                    "",
                    "Aturan khas Ruby: method privat TIDAK BISA dipanggil",
                    "dengan penerima eksplisit, bahkan `self`. `self.rahasia`",
                    "adalah error — kecuali untuk setter, yang justru WAJIB",
                    "memakai `self.nilai = x` supaya tidak dikira variabel",
                    "lokal baru.",
                    "",
                    "Method class (statis):",
                    "  def self.buat(...)",
                    "    new(...)",
                    "  end",
                    "",
                    "TO_S dan INSPECT:",
                    "  to_s      untuk manusia, dipakai interpolasi dan puts",
                    "  inspect   untuk programmer, dipakai p dan .inspect",
                ]
            },
            {
                "heading": "Class lengkap",
                "code": """class Rekening
  include Comparable

  @@urutan = 0

  attr_reader :nomor, :pemilik, :saldo

  def initialize(pemilik, saldo_awal = 0)
    raise ArgumentError, "pemilik wajib diisi" if pemilik.to_s.strip.empty?

    @@urutan += 1
    @nomor = format("AC%04d", @@urutan)
    @pemilik = pemilik
    @saldo = saldo_awal
  end

  def setor(jumlah)
    raise ArgumentError, "jumlah harus positif" unless jumlah.positive?

    @saldo += jumlah
    self          # kembalikan diri sendiri supaya bisa dirantai
  end

  def tarik(jumlah)
    return false if jumlah <= 0 || jumlah > @saldo

    @saldo -= jumlah
    true
  end

  def kosong? = @saldo.zero?

  def <=>(lain) = saldo <=> lain.saldo

  def to_s = "#{@nomor} #{@pemilik.ljust(8)}#{rupiah.rjust(12)}"

  def inspect = "#<Rekening #{@nomor} #{@pemilik} #{@saldo}>"

  def self.buat_banyak(*nama) = nama.map { |n| new(n) }

  private

  def rupiah = @saldo.to_s.reverse.scan(/\\d{1,3}/).join(".").reverse
end

a = Rekening.new("Andi", 500_000)
b = Rekening.new("Budi")

a.setor(250_000)
puts "tarik 900rb: #{a.tarik(900_000)}"
puts "tarik 300rb: #{a.tarik(300_000)}"
b.setor(100_000)

puts a
puts b
p a

puts "---"
puts "a > b?     : #{a > b}"
puts "terbesar   : #{[a, b].max.pemilik}"
puts "b kosong?  : #{b.kosong?}"

puts "---"
Rekening.buat_banyak("Cici", "Dedi").each { |r| puts r }

begin
  Rekening.new("  ")
rescue ArgumentError => e
  puts "Ditolak: #{e.message}"
end"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  tarik 900rb: false",
                    "  tarik 300rb: true",
                    "  AC0001 Andi         450.000",
                    "  AC0002 Budi         100.000",
                    "  #<Rekening AC0001 Andi 450000>",
                    "  ---",
                    "  a > b?     : true",
                    "  terbesar   : Andi",
                    "  b kosong?  : false",
                    "  ---",
                    "  AC0003 Cici               0",
                    "  AC0004 Dedi               0",
                    "  Ditolak: pemilik wajib diisi",
                    "",
                    "Beberapa hal yang layak diperhatikan:",
                    "",
                    "  `puts a` memanggil `to_s`, sedangkan `p a` memanggil",
                    "  `inspect`. Membedakan keduanya berguna: yang satu",
                    "  untuk pengguna, yang lain untuk kamu saat mencari bug.",
                    "",
                    "  `setor` mengembalikan `self`, sehingga bisa dirantai:",
                    "  `a.setor(100).setor(200)`. Pola ini disebut fluent",
                    "  interface dan lazim di Ruby.",
                    "",
                    "  `include Comparable` + satu `<=>` memberi seluruh",
                    "  operator perbandingan dan membuat `.max` bekerja.",
                    "",
                    "  `@@urutan` adalah variabel CLASS — satu untuk seluruh",
                    "  program. Ia dipakai di sini untuk penomoran otomatis,",
                    "  tapi variabel class punya masalah serius: ia DIBAGI",
                    "  dengan semua turunannya, sehingga subclass bisa",
                    "  mengacaukan induknya. Untuk kode baru, `@urutan` di",
                    "  level class (class instance variable) lebih aman.",
                    "",
                    "  `rupiah` dideklarasikan privat, jadi `a.rupiah` dari",
                    "  luar melempar NoMethodError — padahal `to_s` di dalam",
                    "  class boleh memanggilnya.",
                ]
            },
        ],
    },
    {
        "title": "10. Pewarisan, Module & Mixin",
        "sections": [
            {
                "body": [
                    "PEWARISAN — satu induk saja:",
                    "",
                    "  class Kucing < Hewan",
                    "    def initialize(nama)",
                    "      super(nama, \"mamalia\")",
                    "    end",
                    "",
                    "    def suara = \"Meong\"",
                    "  end",
                    "",
                    "`super` memanggil method bernama sama di induk. Ada dua",
                    "bentuk yang BERBEDA, dan bedanya sering menjebak:",
                    "",
                    "  super         teruskan SEMUA argumen apa adanya",
                    "  super()       panggil TANPA argumen sama sekali",
                    "  super(a, b)   dengan argumen tertentu",
                    "",
                    "`super` tanpa kurung bukan berarti tanpa argumen.",
                    "",
                    "Semua class mewarisi `Object` (lewat `BasicObject`), dan",
                    "itu sumber method seperti `class`, `inspect`, `respond_to?`,",
                    "`frozen?` yang dimiliki setiap objek.",
                    "",
                    "MODULE menjawab dua kebutuhan sekaligus:",
                    "",
                    "  1. NAMESPACE, mencegah nama bertabrakan",
                    "     module Toko",
                    "       class Produk; end",
                    "     end",
                    "     Toko::Produk.new",
                    "",
                    "  2. MIXIN, berbagi perilaku tanpa pewarisan",
                    "     module BisaDicatat",
                    "       def catat(pesan) = (@catatan ||= []) << pesan",
                    "     end",
                    "",
                    "     class Pesanan",
                    "       include BisaDicatat",
                    "     end",
                    "",
                    "Tiga cara menyisipkan module, dan ketiganya berbeda:",
                    "  include Modul   method jadi method INSTANCE",
                    "  extend Modul    method jadi method CLASS",
                    "  prepend Modul   disisipkan DI DEPAN, menimpa method",
                    "                  class-nya sendiri",
                    "",
                    "Inilah jawaban Ruby untuk pewarisan berganda, dan ia",
                    "lebih aman: urutan pencarian method (ancestors) selalu",
                    "linier dan bisa dilihat dengan `Kelas.ancestors`.",
                    "",
                    "Dua module dari pustaka standar yang wajib kamu kenal:",
                    "  Comparable  butuh <=>, memberi < > <= >= == between?",
                    "  Enumerable  butuh each, memberi map select reduce dan",
                    "              puluhan lainnya",
                    "",
                    "Ini pola yang sama: implementasi SATU method, dapat",
                    "banyak.",
                ]
            },
            {
                "heading": "Mixin, Enumerable, dan ancestors",
                "code": """module BisaDiringkas
  def ringkas = format("%-16s%8.2f", nama, luas)
end

module Berwarna
  def warna = @warna || "hitam"
  def warna=(w) = @warna = w
end

class Bangun
  include BisaDiringkas
  include Berwarna

  def initialize(nama) = @nama = nama
  attr_reader :nama

  def luas = raise(NotImplementedError, "#{self.class} harus punya luas")
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
  def ringkas = "#{super}  (r=#{@jari})"
end

semua = [Persegi.new(4), Lingkaran.new(3), Persegi.new(2.5)]
semua.each { |b| puts b.ringkas }
puts format("%-16s%8.2f", "TOTAL", semua.sum(&:luas))

puts
puts "warna bawaan : #{semua[0].warna}"
semua[0].warna = "merah"
puts "sesudah diisi: #{semua[0].warna}"

puts
puts "Lingkaran.ancestors:"
puts Lingkaran.ancestors.take(5).map { |a| "  #{a}" }

begin
  Bangun.new("Abstrak").luas
rescue NotImplementedError => e
  puts "\\n#{e.class}: #{e.message}"
end

puts

# Enumerable: satu `each`, puluhan method gratis
class Kelas
  include Enumerable

  def initialize = @murid = {}

  def tambah(nama, nilai)
    @murid[nama] = nilai
    self
  end

  def each
    @murid.sort_by { |_, n| -n }.each { |nama, nilai| yield(nama, nilai) }
  end
end

k = Kelas.new.tambah("Andi", 88).tambah("Budi", 72).tambah("Cici", 95)

k.each { |nama, nilai| puts "#{nama.ljust(6)}#{nilai}" }
puts "lulus   : #{k.count { |_, n| n >= 75 }}"
puts "tertinggi: #{k.first.inspect}"
puts "nama     : #{k.map { |nama, _| nama }.join(', ')}\""""
            },
            {
                "body": [
                    "Keluaran:",
                    "  Persegi            16.00",
                    "  Lingkaran          28.27  (r=3)",
                    "  Persegi             6.25",
                    "  TOTAL              50.52",
                    "",
                    "  warna bawaan : hitam",
                    "  sesudah diisi: merah",
                    "",
                    "  Lingkaran.ancestors:",
                    "    Lingkaran",
                    "    Bangun",
                    "    Berwarna",
                    "    BisaDiringkas",
                    "    Object",
                    "",
                    "  NotImplementedError: Bangun harus punya luas",
                    "",
                    "  Cici  95",
                    "  Andi  88",
                    "  Budi  72",
                    "  lulus   : 2",
                    "  tertinggi: [\"Cici\", 95]",
                    "  nama     : Cici, Andi, Budi",
                    "",
                    "`ancestors` menunjukkan URUTAN PENCARIAN method. Ruby",
                    "menelusurinya dari atas: Lingkaran dulu, lalu Bangun,",
                    "lalu module yang di-include (yang TERAKHIR di-include",
                    "berada lebih dulu), lalu Object.",
                    "",
                    "Rantai inilah yang membuat `super` di `Lingkaran#ringkas`",
                    "menemukan versi dari module BisaDiringkas — walaupun",
                    "module itu di-include di class INDUKNYA.",
                    "",
                    "Class `Kelas` menunjukkan kekuatan Enumerable: dengan",
                    "menulis satu `each`, ia langsung punya `count`, `first`,",
                    "`map`, `select`, `sort_by`, `sum`, `group_by`, dan",
                    "puluhan lainnya. Tidak satu pun ditulis di class itu.",
                    "",
                    "`NotImplementedError` adalah cara Ruby menandai method",
                    "abstrak. Ruby tidak punya kata kunci `abstract` — yang",
                    "dipakai adalah konvensi ini.",
                ]
            },
        ],
    },
    {
        "title": "11. Exception & Penanganan Galat",
        "sections": [
            {
                "body": [
                    "  begin",
                    "    ... kode yang mungkin gagal",
                    "  rescue ArgumentError => e",
                    "    ... tangani yang spesifik",
                    "  rescue StandardError => e",
                    "    ... jaring yang lebih luas",
                    "  else",
                    "    ... dijalankan kalau TIDAK ada galat",
                    "  ensure",
                    "    ... SELALU dijalankan",
                    "  end",
                    "",
                    "Di dalam method, `begin` boleh dihilangkan — badan method",
                    "itu sendiri sudah jadi bloknya:",
                    "",
                    "  def baca(path)",
                    "    File.read(path)",
                    "  rescue Errno::ENOENT",
                    "    \"\"",
                    "  end",
                    "",
                    "HIERARKI, dan satu aturan penting darinya:",
                    "",
                    "  Exception",
                    "  ├── NoMemoryError",
                    "  ├── SignalException      Ctrl-C",
                    "  ├── ScriptError",
                    "  │   └── NotImplementedError",
                    "  └── StandardError        <- yang biasa kamu tangani",
                    "      ├── ArgumentError",
                    "      ├── TypeError",
                    "      ├── NameError -> NoMethodError",
                    "      ├── ZeroDivisionError",
                    "      ├── IOError",
                    "      ├── RuntimeError     <- `raise \"pesan\"` polos",
                    "      ├── KeyError",
                    "      └── IndexError -> StopIteration",
                    "",
                    "ATURANNYA: `rescue` tanpa menyebut kelas menangkap",
                    "StandardError saja, BUKAN Exception. Itu disengaja dan",
                    "benar — menangkap `Exception` ikut menelan Ctrl-C dan",
                    "kehabisan memori, sehingga programmu tidak bisa",
                    "dihentikan.",
                    "",
                    "  rescue => e          BENAR (StandardError)",
                    "  rescue Exception     JANGAN",
                    "",
                    "Melempar:",
                    "  raise \"pesan\"                    -> RuntimeError",
                    "  raise ArgumentError, \"pesan\"",
                    "  raise ArgumentError.new(\"pesan\")",
                    "  raise                            lempar ulang yang sama",
                    "",
                    "RETRY mencoba ulang blok begin — berguna untuk jaringan:",
                    "",
                    "  percobaan = 0",
                    "  begin",
                    "    percobaan += 1",
                    "    ambil_data",
                    "  rescue Timeout::Error",
                    "    retry if percobaan < 3",
                    "    raise",
                    "  end",
                    "",
                    "Tanpa penghitung, `retry` adalah perulangan tak berujung.",
                ]
            },
            {
                "heading": "Exception sendiri, ensure, dan retry",
                "code": """class SaldoKurangError < StandardError
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

# ensure dijalankan apa pun yang terjadi
def dengan_sumber_daya(nama)
  puts "buka #{nama}"
  yield
rescue => e
  puts "galat: #{e.message}"
  nil
ensure
  puts "tutup #{nama}"
end

puts "hasil: #{dengan_sumber_daya('berkas') { 6 * 7 }.inspect}"
puts "hasil: #{dengan_sumber_daya('berkas') { raise 'rusak' }.inspect}"

puts "---"

# retry dengan batas
def ambil_data(gagal_sampai:)
  @panggilan = (@panggilan || 0) + 1
  raise IOError, "koneksi gagal" if @panggilan <= gagal_sampai

  "data ke-#{@panggilan}"
end

percobaan = 0
begin
  percobaan += 1
  hasil = ambil_data(gagal_sampai: 2)
  puts "berhasil di percobaan #{percobaan}: #{hasil}"
rescue IOError => e
  puts "percobaan #{percobaan} gagal: #{e.message}"
  retry if percobaan < 5
  raise
end

puts "---"

# Merantai: galat tingkat rendah dibungkus jadi tingkat tinggi
class KonfigurasiError < StandardError; end

def baca_konfigurasi(teks)
  Integer(teks)
rescue ArgumentError => e
  raise KonfigurasiError, "konfigurasi tidak sah: #{teks}"
end

begin
  baca_konfigurasi("bukan-angka")
rescue KonfigurasiError => e
  puts "#{e.class}: #{e.message}"
  puts "penyebab  : #{e.cause.class}"
end"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  bayar   20000 -> sisa 30000",
                    "  bayar      -5 -> DITOLAK: jumlah -5 tidak sah",
                    "  bayar  100000 -> GAGAL, kurang 70000",
                    "  bayar   30000 -> sisa 0",
                    "  ---",
                    "  buka berkas",
                    "  tutup berkas",
                    "  hasil: 42",
                    "  buka berkas",
                    "  galat: rusak",
                    "  tutup berkas",
                    "  hasil: nil",
                    "  ---",
                    "  percobaan 1 gagal: koneksi gagal",
                    "  percobaan 2 gagal: koneksi gagal",
                    "  berhasil di percobaan 3: data ke-3",
                    "  ---",
                    "  KonfigurasiError: konfigurasi tidak sah: bukan-angka",
                    "  penyebab  : ArgumentError",
                    "",
                    "`rescue` di dalam blok `do...end` (seperti di `each` di",
                    "atas) sah sejak Ruby 2.6 — sebelumnya butuh `begin`",
                    "tersendiri di dalamnya.",
                    "",
                    "`e.cause` adalah hal yang berharga dan sering tidak",
                    "diketahui: Ruby OTOMATIS menyimpan exception yang sedang",
                    "ditangani saat sebuah exception baru dilempar. Jadi",
                    "jejak penyebab aslinya tidak pernah hilang, tanpa kamu",
                    "perlu meneruskannya manual seperti di PHP atau C#.",
                    "",
                    "Aturan yang sering dilanggar:",
                    "",
                    "  JANGAN `rescue => e` kosong tanpa berbuat apa-apa.",
                    "  Program berjalan terus dalam keadaan rusak.",
                    "",
                    "  JANGAN `rescue Exception`. Ia menelan Ctrl-C dan",
                    "  kehabisan memori.",
                    "",
                    "  JANGAN memakai exception untuk alur normal. `find`",
                    "  yang tidak ketemu mengembalikan nil; itu bukan galat.",
                    "",
                    "  Untuk method yang WAJAR gagal, sediakan dua versi:",
                    "  `simpan` mengembalikan false, `simpan!` melempar.",
                    "  Pola ini dipakai di seluruh Rails.",
                ]
            },
        ],
    },
    {
        "title": "12. Berkas, JSON & Baris Perintah",
        "sections": [
            {
                "body": [
                    "BERKAS — cara singkat:",
                    "  File.read(path)                  seluruh isi",
                    "  File.readlines(path, chomp: true) tiap baris jadi elemen",
                    "  File.write(path, isi)            tulis (menimpa)",
                    "  File.exist?(path)  File.size(path)  File.delete(path)",
                    "",
                    "Cara dengan blok — yang SELALU menutup berkasnya:",
                    "  File.open(path, \"w\") do |f|",
                    "    f.puts \"baris\"",
                    "  end",
                    "",
                    "  File.foreach(path) do |baris|",
                    "    ...            satu per satu, hemat memori",
                    "  end",
                    "",
                    "Mode: \"r\" baca, \"w\" tulis (MENGOSONGKAN), \"a\" tambah,",
                    "\"r+\" baca-tulis. Tambahkan \"b\" untuk biner.",
                    "",
                    "PATH lintas sistem:",
                    "  File.join(\"data\", \"murid.csv\")",
                    "  File.basename(p) / File.dirname(p) / File.extname(p)",
                    "  File.expand_path(p)",
                    "  Dir.glob(\"*.txt\") / Dir.mkdir / Dir.exist?",
                    "  Dir.tmpdir            butuh require \"tmpdir\"",
                    "  __dir__               folder berkas ini",
                    "",
                    "JSON:",
                    "  require \"json\"",
                    "",
                    "  JSON.generate(data)         atau data.to_json",
                    "  JSON.pretty_generate(data)",
                    "  JSON.parse(teks)                     kunci String",
                    "  JSON.parse(teks, symbolize_names: true)  kunci Symbol",
                    "",
                    "`symbolize_names: true` hampir selalu yang kamu mau di",
                    "Ruby, karena kunci symbol adalah kebiasaan bahasanya.",
                    "",
                    "CSV pernah jadi pustaka standar, TAPI sejak Ruby 3.4 ia",
                    "dipindah jadi bundled gem. Artinya `require \"csv\"` bisa",
                    "gagal dengan LoadError sampai kamu memasangnya sendiri:",
                    "",
                    "  gem install csv          atau tambahkan ke Gemfile",
                    "  require \"csv\"",
                    "  CSV.foreach(path, headers: true) { |baris| ... }",
                    "  CSV.open(path, \"w\") { |csv| csv << [\"a\", \"b\"] }",
                    "",
                    "Hal yang sama menimpa beberapa pustaka lain (abbrev,",
                    "base64, observer). Kalau sebuah require yang dulu jalan",
                    "mendadak gagal sesudah naik versi Ruby, inilah penyebab",
                    "pertama yang patut dicurigai.",
                    "",
                    "Untuk data berpemisah koma yang SEDERHANA, split(\",\")",
                    "sudah cukup, dan itu yang dipakai contoh di bawah supaya",
                    "jalan di Ruby versi mana pun. Untuk CSV sungguhan tetap",
                    "pakai pustakanya: kolom yang dikutip boleh memuat koma,",
                    "dan split akan memecahnya jadi dua.",
                    "",
                    "BARIS PERINTAH:",
                    "  ARGV        array argumen",
                    "  ARGF        gabungan berkas di ARGV, atau stdin",
                    "  $PROGRAM_NAME",
                    "  ENV[\"HOME\"]",
                    "  STDIN.gets / $stdin.read / gets",
                    "",
                    "`OptionParser` di pustaka standar menangani flag, nilai,",
                    "dan teks bantuan tanpa satu gem pun.",
                ]
            },
            {
                "heading": "Berkas, CSV, dan JSON",
                "code": """require "json"
require "tmpdir"

berkas = File.join(Dir.tmpdir, "belajar-ruby.csv")

# --- Tulis berkas berpemisah koma ---
File.open(berkas, "w") do |f|
  f.puts "nama,kelas,nilai"
  f.puts "Andi,A,88"
  f.puts "Budi,B,72"
  f.puts "Cici,A,95"
end

# --- Baca kembali ---
judul, *isi = File.readlines(berkas, chomp: true)
kunci = judul.split(",").map(&:to_sym)
data = isi.map do |baris|
  nilai = kunci.zip(baris.split(",")).to_h
  nilai.merge(nilai: nilai[:nilai].to_i)
end

data.sort_by { |m| -m[:nilai] }.each do |m|
  puts "#{m[:nama].ljust(6)}#{m[:kelas]} #{m[:nilai].to_s.rjust(3)}"
end
puts "Rata-rata: #{'%.2f' % (data.sum { |m| m[:nilai] }.to_f / data.size)}"

puts "---"

# --- JSON ---
json = JSON.pretty_generate(data.first)
puts json

kembali = JSON.parse(json, symbolize_names: true)
puts "nama dari JSON: #{kembali[:nama]}"

begin
  JSON.parse("{rusak}")
rescue JSON::ParserError => e
  puts "JSON rusak: #{e.class}"
end

puts "---"

# --- Berkas teks biasa, dengan blok ---
teks = File.join(Dir.tmpdir, "belajar-ruby.txt")
File.open(teks, "w") do |f|
  f.puts "baris satu"
  f.puts "baris dua"
  f.puts "baris tiga"
end

File.foreach(teks).with_index(1) do |baris, i|
  puts "#{i.to_s.rjust(2)}| #{baris.chomp}"
end

puts "ukuran: #{File.size(teks)} byte"

[berkas, teks].each { |p| File.delete(p) }
puts "berkas masih ada? #{File.exist?(teks)}\""""
            },
            {
                "body": [
                    "Keluaran:",
                    "  Cici  A  95",
                    "  Andi  A  88",
                    "  Budi  B  72",
                    "  Rata-rata: 85.00",
                    "  ---",
                    "  {",
                    "    \"nama\": \"Andi\",",
                    "    \"kelas\": \"A\",",
                    "    \"nilai\": 88",
                    "  }",
                    "  nama dari JSON: Andi",
                    "  JSON rusak: JSON::ParserError",
                    "  ---",
                    "   1| baris satu",
                    "   2| baris dua",
                    "   3| baris tiga",
                    "  ukuran: 32 byte",
                    "  berkas masih ada? false",
                    "",
                    "Perhatikan `\"nilai\": 88` TANPA kutip — sebagai angka.",
                    "Itu karena `.to_i` dipanggil saat membaca CSV. Kalau",
                    "tidak, JSON-nya akan berisi string \"88\" dan siapa pun",
                    "yang memakainya nanti harus mengonversinya lagi.",
                    "",
                    "`File.foreach(teks).with_index(1)` menelusuri baris demi",
                    "baris sambil menghitung dari 1. `with_index` menerima",
                    "angka awal — berbeda dari `each_with_index` yang selalu",
                    "mulai dari 0.",
                    "",
                    "`.chomp` membuang karakter baris baru di ujung. Tanpa",
                    "itu, tiap baris tercetak dengan baris kosong di bawahnya.",
                    "Alternatifnya `File.readlines(path, chomp: true)`.",
                    "",
                    "Bentuk `File.open(path) do |f| ... end` adalah satu-satunya",
                    "yang sebaiknya dipakai. Bentuk tanpa blok menuntut kamu",
                    "memanggil `.close` sendiri, dan satu exception di tengah",
                    "membuat berkasnya tidak pernah tertutup.",
                ]
            },
        ],
    },
    {
        "title": "13. Gem, Bundler & Struktur Proyek",
        "sections": [
            {
                "body": [
                    "GEM adalah paket pustaka Ruby. RubyGems adalah",
                    "pengelolanya, dan ia sudah menyatu dengan Ruby.",
                    "",
                    "  gem install rspec",
                    "  gem list",
                    "  gem which json",
                    "",
                    "BUNDLER mengunci versi untuk sebuah proyek — inilah yang",
                    "sebenarnya dipakai sehari-hari:",
                    "",
                    "  bundle init             buat Gemfile",
                    "  bundle add rspec        tambah dependensi",
                    "  bundle install          pasang sesuai Gemfile.lock",
                    "  bundle update           perbarui",
                    "  bundle exec rspec       jalankan dengan versi terkunci",
                    "",
                    "`bundle exec` penting: tanpa itu, kamu bisa menjalankan",
                    "versi gem yang berbeda dari yang tercatat di lock file,",
                    "dan hasilnya berbeda di mesin lain.",
                    "",
                    "Gemfile:",
                    "",
                    "  source \"https://rubygems.org\"",
                    "  ruby \"3.3.0\"",
                    "",
                    "  gem \"sinatra\", \"~> 4.0\"",
                    "  gem \"pg\"",
                    "",
                    "  group :development, :test do",
                    "    gem \"rspec\"",
                    "    gem \"rubocop\", require: false",
                    "  end",
                    "",
                    "`~> 4.0` disebut pessimistic operator: terima 4.x apa pun",
                    "tapi bukan 5.0. `~> 4.0.1` terima 4.0.x saja.",
                    "",
                    "Gemfile.lock WAJIB masuk git untuk aplikasi. Itulah yang",
                    "membuat pemasangan hari ini dan enam bulan lagi",
                    "menghasilkan versi yang sama persis.",
                    "",
                    "MEMUAT KODE:",
                    "  require \"json\"              pustaka standar atau gem",
                    "  require_relative \"murid\"    berkas di proyek ini",
                    "",
                    "Bedanya penting: `require` mencari di jalur pencarian gem",
                    "dan butuh path absolut untuk berkas sendiri, sedangkan",
                    "`require_relative` dihitung dari lokasi berkas pemanggil.",
                    "Untuk berkas dalam proyekmu sendiri, hampir selalu",
                    "`require_relative`.",
                    "",
                    "Keduanya memuat SEKALI saja — memanggilnya dua kali tidak",
                    "menjalankan berkasnya dua kali.",
                ]
            },
            {
                "heading": "Struktur proyek Ruby",
                "code": """proyekku/
├── Gemfile                 daftar dependensi
├── Gemfile.lock            versi persis (masuk git untuk aplikasi)
├── Rakefile                tugas otomatis
├── README.md
├── .rubocop.yml            aturan gaya penulisan
├── bin/
│   └── proyekku            skrip yang bisa dieksekusi
├── lib/
│   ├── proyekku.rb         titik masuk pustaka
│   └── proyekku/
│       ├── version.rb
│       ├── murid.rb        Proyekku::Murid
│       └── gudang.rb       Proyekku::Gudang
└── spec/
    ├── spec_helper.rb
    └── murid_spec.rb

# ============ lib/proyekku.rb ============
require_relative "proyekku/version"
require_relative "proyekku/murid"
require_relative "proyekku/gudang"

module Proyekku
  class Error < StandardError; end
end

# ============ Rakefile ============
require "rspec/core/rake_task"

RSpec::Core::RakeTask.new(:spec)

task default: :spec

desc "Periksa gaya penulisan"
task :lint do
  sh "rubocop"
end

desc "Tes lalu periksa gaya"
task ci: %i[spec lint]"""
            },
            {
                "body": [
                    "Konvensi yang dipatuhi hampir seluruh proyek Ruby:",
                    "",
                    "  lib/nama_proyek.rb      memuat semua yang lain",
                    "  lib/nama_proyek/*.rb    satu class per berkas",
                    "  spec/ atau test/        tes",
                    "  bin/ atau exe/          skrip eksekutabel",
                    "",
                    "  Nama berkas snake_case, nama class PascalCase:",
                    "  `lib/proyekku/murid_baru.rb` berisi",
                    "  `Proyekku::MuridBaru`. Kesepakatan ini yang membuat",
                    "  autoloader di Rails bisa menemukan berkas dari nama",
                    "  class-nya.",
                    "",
                    "RAKE adalah make-nya Ruby. `rake -T` menampilkan semua",
                    "tugas beserta deskripsinya, dan `rake` tanpa argumen",
                    "menjalankan tugas `default`.",
                    "",
                    "RUBOCOP adalah linter sekaligus perapi kode. Ia memaksa",
                    "gaya yang konsisten dan menangkap banyak kebiasaan buruk:",
                    "",
                    "  rubocop                  periksa",
                    "  rubocop -a               perbaiki yang aman",
                    "  rubocop -A               perbaiki semuanya (hati-hati)",
                    "  rubocop --auto-gen-config  buat daftar pengecualian",
                    "                             untuk proyek yang sudah ada",
                    "",
                    "Perintah terakhir itu berguna saat memasang RuboCop di",
                    "proyek lama: alih-alih ribuan keluhan sekaligus, ia",
                    "membekukan keadaan sekarang sehingga hanya kode BARU",
                    "yang diperiksa.",
                    "",
                    "Gem yang lazim dipakai:",
                    "  rspec / minitest     pengujian",
                    "  rubocop              gaya dan kualitas",
                    "  pry / debug          debugger interaktif",
                    "  sinatra / rails      web",
                    "  sequel / activerecord  database",
                    "  httparty / faraday   klien HTTP",
                ]
            },
        ],
    },
    {
        "title": "14. Pengujian dengan Minitest & RSpec",
        "sections": [
            {
                "body": [
                    "Ruby punya dua kerangka tes utama, dan keduanya bagus:",
                    "",
                    "  MINITEST   ada di pustaka standar, tanpa pemasangan.",
                    "             Gayanya seperti tes di bahasa lain.",
                    "  RSPEC      gem terpisah, gaya 'spesifikasi' yang",
                    "             terbaca seperti kalimat. Paling umum di",
                    "             proyek Rails.",
                    "",
                    "MINITEST:",
                    "",
                    "  require \"minitest/autorun\"",
                    "",
                    "  class TestRapor < Minitest::Test",
                    "    def setup",
                    "      @rapor = Rapor.new",
                    "    end",
                    "",
                    "    def test_grade_di_batas",
                    "      assert_equal \"A\", Rapor.grade(85)",
                    "      assert_equal \"B\", Rapor.grade(84)",
                    "    end",
                    "  end",
                    "",
                    "Assertion Minitest:",
                    "  assert(kondisi)          refute(kondisi)",
                    "  assert_equal(harap, aktual)",
                    "  assert_nil / refute_nil",
                    "  assert_includes(koleksi, x)",
                    "  assert_empty / refute_empty",
                    "  assert_raises(KelasError) { ... }",
                    "  assert_instance_of(Kelas, obj)",
                    "  assert_in_delta(3.14, x, 0.01)   untuk Float",
                    "",
                    "`assert_in_delta` wajib untuk Float: `0.1 + 0.2 == 0.3`",
                    "adalah false di semua bahasa yang memakai IEEE 754,",
                    "termasuk Ruby.",
                    "",
                    "RSPEC:",
                    "",
                    "  RSpec.describe Rapor do",
                    "    describe \".grade\" do",
                    "      it \"memberi A tepat di 85\" do",
                    "        expect(Rapor.grade(85)).to eq(\"A\")",
                    "      end",
                    "    end",
                    "  end",
                    "",
                    "Matcher RSpec:",
                    "  eq(x)         eql(x)        equal(x)   be(x)",
                    "  be > 5        be_within(0.01).of(3.14)",
                    "  include(x)    match(/pola/) start_with(x)",
                    "  be_empty      be_nil        be_a(Kelas)",
                    "  raise_error(KelasError)",
                    "  change { x }.by(1)",
                    "",
                    "`be_empty` bekerja untuk apa pun yang punya `empty?` —",
                    "RSpec mengubah `be_xxx` jadi pemanggilan `xxx?`. Pola",
                    "yang sama berlaku untuk `have_key`, `be_valid`, dan",
                    "predikat apa pun yang kamu tulis sendiri.",
                ]
            },
            {
                "heading": "Satu kelas, dua gaya tes",
                "code": """# ===== lib/rapor.rb =====
class Rapor
  def initialize = @nilai = {}

  def catat(nama, nilai)
    raise ArgumentError, "nilai #{nilai} di luar 0..100" unless (0..100).cover?(nilai)

    @nilai[nama] = nilai
    self
  end

  def self.grade(nilai)
    case nilai
    when 85.. then "A"
    when 75.. then "B"
    when 60.. then "C"
    else           "D"
    end
  end

  def rata_rata
    return nil if @nilai.empty?

    @nilai.values.sum.to_f / @nilai.size
  end

  def lulus = @nilai.select { |_, n| n >= 75 }.keys.sort
end

# ===== test/rapor_test.rb  (Minitest) =====
require "minitest/autorun"

class RaporTest < Minitest::Test
  def setup
    @rapor = Rapor.new
  end

  def test_grade_tepat_di_batas
    { 85 => "A", 84 => "B", 75 => "B", 74 => "C",
      60 => "C", 59 => "D", 0 => "D" }.each do |nilai, harap|
      assert_equal harap, Rapor.grade(nilai), "gagal di nilai #{nilai}"
    end
  end

  def test_rata_rata_kosong_nil
    assert_nil @rapor.rata_rata
  end

  def test_rata_rata_menghitung_benar
    @rapor.catat("Andi", 80).catat("Budi", 90)
    assert_in_delta 85.0, @rapor.rata_rata, 0.001
  end

  def test_lulus_terurut
    @rapor.catat("Cici", 95).catat("Budi", 64).catat("Andi", 75)
    assert_equal %w[Andi Cici], @rapor.lulus
  end

  def test_nilai_di_luar_rentang_ditolak
    galat = assert_raises(ArgumentError) { @rapor.catat("Andi", 150) }
    assert_includes galat.message, "di luar 0..100"
  end
end

# ===== spec/rapor_spec.rb  (RSpec, tidak dijalankan di sini) =====
#
# RSpec.describe Rapor do
#   subject(:rapor) { described_class.new }
#
#   describe ".grade" do
#     { 85 => "A", 84 => "B", 60 => "C", 59 => "D" }.each do |nilai, harap|
#       it "memberi #{harap} untuk nilai #{nilai}" do
#         expect(described_class.grade(nilai)).to eq(harap)
#       end
#     end
#   end
#
#   describe "#rata_rata" do
#     it "nil saat kosong" do
#       expect(rapor.rata_rata).to be_nil
#     end
#
#     it "menghitung rata-rata" do
#       rapor.catat("Andi", 80).catat("Budi", 90)
#       expect(rapor.rata_rata).to be_within(0.001).of(85.0)
#     end
#   end
#
#   describe "#catat" do
#     it "menolak nilai di luar rentang" do
#       expect { rapor.catat("Andi", 150) }
#         .to raise_error(ArgumentError, /di luar 0\\.\\.100/)
#     end
#   end
# end"""
            },
            {
                "body": [
                    "Perhatikan nilai yang dipilih: 85 dan 84, 75 dan 74,",
                    "60 dan 59. Menguji tepat DI BATAS adalah yang paling",
                    "berharga, karena di situlah `>=` versus `>` salah ketik.",
                    "Nilai di tengah rentang hampir tidak pernah menemukan bug.",
                    "",
                    "`when 85..` adalah rentang TANPA BATAS ATAS (Ruby 2.6).",
                    "Ada juga `..85` untuk tanpa batas bawah. Keduanya membuat",
                    "`case` untuk penilaian jadi sangat ringkas.",
                    "",
                    "`(0..100).cover?(nilai)` lebih cepat daripada `include?`",
                    "untuk rentang angka: `cover?` cuma membandingkan kedua",
                    "ujungnya, sedangkan `include?` bisa menelusuri.",
                    "",
                    "`assert_equal harap, aktual, \"pesan\"` — argumen ketiga",
                    "muncul saat tesnya gagal. Di tes berulang seperti di",
                    "atas, tanpa pesan itu kamu cuma tahu 'ada yang gagal',",
                    "bukan yang mana.",
                    "",
                    "`catat` mengembalikan `self`, sehingga bisa dirantai.",
                    "Itu bukan kebetulan: method yang mengembalikan self",
                    "membuat penyiapan data tes jadi satu baris alih-alih",
                    "tiga.",
                    "",
                    "Menjalankan:",
                    "  ruby test/rapor_test.rb",
                    "  rake test",
                    "  bundle exec rspec",
                    "  bundle exec rspec spec/rapor_spec.rb:12   satu baris saja",
                    "",
                    "Pilih SATU kerangka untuk satu proyek. Minitest kalau",
                    "kamu ingin tanpa dependensi dan tes yang terasa seperti",
                    "kode biasa; RSpec kalau kamu ingin dokumentasi yang bisa",
                    "dijalankan dan matcher yang sangat kaya.",
                ]
            },
        ],
    },
    {
        "title": "15. Metaprogramming Secukupnya",
        "sections": [
            {
                "body": [
                    "Ruby memungkinkan program mengubah dirinya sendiri saat",
                    "jalan. Ini yang membuat Rails bisa menulis",
                    "`User.find_by_email_and_status(...)` tanpa method itu",
                    "pernah ditulis siapa pun.",
                    "",
                    "Kekuatannya besar, dan begitu juga ongkosnya. Materi ini",
                    "menunjukkan yang perlu kamu KENALI saat membaca kode",
                    "orang, bukan yang harus kamu pakai sehari-hari.",
                    "",
                    "MEMERIKSA objek saat jalan:",
                    "  obj.class            obj.ancestors",
                    "  obj.methods          obj.public_methods(false)",
                    "  obj.respond_to?(:x)  obj.instance_variables",
                    "  obj.instance_variable_get(:@nama)",
                    "  Kelas.instance_methods(false)",
                    "",
                    "MEMANGGIL secara dinamis:",
                    "  obj.send(:nama)            termasuk method PRIVAT",
                    "  obj.public_send(:nama)     hanya yang publik",
                    "  obj.method(:nama).call(x)",
                    "",
                    "Pakai `public_send` kecuali kamu memang perlu menembus",
                    "privasi. `send` yang menerima nama dari masukan pengguna",
                    "adalah lubang keamanan besar.",
                    "",
                    "MENDEFINISIKAN saat jalan:",
                    "  define_method(:nama) { ... }",
                    "  attr_accessor :a, :b",
                    "  Kelas.class_eval { ... }",
                    "  obj.define_singleton_method(:x) { ... }",
                    "",
                    "MENANGKAP method yang tidak ada:",
                    "  def method_missing(nama, *args)",
                    "    ...",
                    "  end",
                    "",
                    "  def respond_to_missing?(nama, privat = false)",
                    "    ...",
                    "  end",
                    "",
                    "ATURAN KERAS: kalau kamu menulis `method_missing`, kamu",
                    "WAJIB menulis `respond_to_missing?` juga. Tanpa itu,",
                    "`respond_to?` berbohong, `obj.method(:x)` gagal, dan",
                    "objekmu berperilaku tidak konsisten dengan seluruh",
                    "ekosistem Ruby.",
                    "",
                    "ONGKOS metaprogramming, dan ini nyata:",
                    "  - Editor tidak bisa melengkapi otomatis.",
                    "  - `grep` tidak menemukan definisi method.",
                    "  - Pesan galat jadi jauh dari penyebabnya.",
                    "  - Orang berikutnya butuh waktu lebih lama.",
                    "",
                    "Aturan praktisnya: kalau bisa ditulis biasa, tulis biasa.",
                    "Metaprogramming dibenarkan saat ia MENGHAPUS pengulangan",
                    "yang benar-benar banyak, bukan saat ia terasa pintar.",
                ]
            },
            {
                "heading": "define_method dan method_missing yang bertanggung jawab",
                "code": """# ---- define_method: menghapus pengulangan yang nyata ----
class Setelan
  BAWAAN = { tema: "terang", ukuran: 14, gerak: true }.freeze

  BAWAAN.each_key do |kunci|
    define_method(kunci) { @isi.fetch(kunci, BAWAAN[kunci]) }
    define_method("#{kunci}=") { |nilai| @isi[kunci] = nilai }
    define_method("#{kunci}_bawaan?") { @isi.fetch(kunci, BAWAAN[kunci]) == BAWAAN[kunci] }
  end

  def initialize(isi = {}) = @isi = isi

  def to_h = BAWAAN.keys.to_h { |k| [k, public_send(k)] }
end

s = Setelan.new(ukuran: 18)
puts "tema         : #{s.tema}"
puts "ukuran       : #{s.ukuran}"
puts "tema bawaan? : #{s.tema_bawaan?}"
puts "ukuran bawaan? : #{s.ukuran_bawaan?}"
s.gerak = false
puts "semua        : #{s.to_h}"

puts "---"

# ---- Pemeriksaan objek ----
puts "method buatan: #{Setelan.instance_methods(false).sort.take(6).inspect}"
puts "punya ukuran?: #{s.respond_to?(:ukuran)}"
puts "lewat send   : #{s.public_send(:ukuran)}"
puts "variabel     : #{s.instance_variables.inspect}"

puts "---"

# ---- method_missing YANG BENAR: selalu berpasangan ----
class Catatan
  def initialize = @data = {}

  def method_missing(nama, *args)
    teks = nama.to_s

    if teks.end_with?("=")
      @data[teks.chomp("=").to_sym] = args.first
    elsif @data.key?(nama)
      @data[nama]
    else
      super        # WAJIB: biar NoMethodError tetap wajar
    end
  end

  def respond_to_missing?(nama, privat = false)
    teks = nama.to_s
    teks.end_with?("=") || @data.key?(nama) || super
  end

  def to_h = @data.dup
end

c = Catatan.new
c.judul = "Rapat mingguan"
c.peserta = 5

puts "judul        : #{c.judul}"
puts "peserta      : #{c.peserta}"
puts "respond_to?  : #{c.respond_to?(:judul)} / #{c.respond_to?(:tidak_ada)}"
puts "isi          : #{c.to_h}"

begin
  c.tidak_pernah_diisi
rescue NoMethodError => e
  puts "NoMethodError tetap wajar: #{e.message.split(' for ').first}"
end"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  tema         : terang",
                    "  ukuran       : 18",
                    "  tema bawaan? : true",
                    "  ukuran bawaan? : false",
                    "  semua        : {tema: \"terang\", ukuran: 18, gerak: false}",
                    "  ---",
                    "  method buatan: [:gerak, :gerak=, :gerak_bawaan?, :tema, :tema=, :tema_bawaan?]",
                    "  punya ukuran?: true",
                    "  lewat send   : 18",
                    "  variabel     : [:@isi]",
                    "  ---",
                    "  judul        : Rapat mingguan",
                    "  peserta      : 5",
                    "  respond_to?  : true / false",
                    "  isi          : {judul: \"Rapat mingguan\", peserta: 5}",
                    "  NoMethodError tetap wajar: undefined method 'tidak_pernah_diisi'",
                    "",
                    "Class Setelan menunjukkan pemakaian metaprogramming yang",
                    "DIBENARKAN: tiga kunci dikali tiga method adalah sembilan",
                    "method yang isinya sama persis. Menulisnya tangan berarti",
                    "sembilan tempat yang harus disunting setiap kali ada",
                    "setelan baru.",
                    "",
                    "Class Catatan menunjukkan `method_missing` yang",
                    "bertanggung jawab, dan tiga hal membuatnya begitu:",
                    "",
                    "  1. `super` di cabang terakhir, sehingga method yang",
                    "     benar-benar tidak ada tetap melempar NoMethodError",
                    "     dengan pesan normal. Tanpa `super`, ia mengembalikan",
                    "     nil diam-diam — dan salah ketik nama method jadi",
                    "     bug yang sunyi.",
                    "",
                    "  2. `respond_to_missing?` yang cocok dengan",
                    "     `method_missing`, sehingga `respond_to?` jujur.",
                    "",
                    "  3. `super` juga di `respond_to_missing?`, supaya",
                    "     method sungguhan tetap terdeteksi.",
                    "",
                    "Kalau ketiganya terasa banyak untuk diingat — itu memang",
                    "petunjuknya. Untuk kasus seperti ini, `OpenStruct` atau",
                    "`Struct` biasa sudah cukup dan jauh lebih jelas.",
                ]
            },
        ],
    },
    {
        "title": "16. Ekspresi Reguler",
        "sections": [
            {
                "body": [
                    "Regex di Ruby ditulis di antara dua garis miring, dan ia",
                    "objek kelas satu bertipe Regexp:",
                    "",
                    "  /\\d{4}-\\d{2}-\\d{2}/",
                    "  %r{https?://\\S+}        pembatas lain, tanpa melarikan /",
                    "  Regexp.new(teks)        dari string, saat polanya dinamis",
                    "",
                    "Operator dan method yang dipakai:",
                    "  teks =~ /pola/        posisi cocok, atau nil",
                    "  teks.match(/pola/)    MatchData, atau nil",
                    "  teks.match?(/pola/)   true/false, TANPA membuat MatchData",
                    "  teks.scan(/pola/)     SEMUA kecocokan jadi array",
                    "  teks.sub(/pola/, x)   ganti yang PERTAMA",
                    "  teks.gsub(/pola/, x)  ganti SEMUANYA",
                    "  teks.split(/pola/)",
                    "  teks[/pola/]          bagian yang cocok, atau nil",
                    "",
                    "`match?` layak jadi kebiasaan: ia tidak mengisi variabel",
                    "global apa pun dan tidak mengalokasikan MatchData, jadi",
                    "jauh lebih murah saat kamu cuma bertanya 'cocok atau",
                    "tidak'.",
                    "",
                    "GRUP BERNAMA membuat hasilnya terbaca:",
                    "",
                    "  m = \"2026-09-22\".match(/(?<thn>\\d{4})-(?<bln>\\d{2})/)",
                    "  m[:thn]     \"2026\"",
                    "  m[:bln]     \"09\"",
                    "  m.pre_match / m.post_match / m.captures",
                    "",
                    "Ada kejutan yang berguna: kalau regex BERTULIS LITERAL",
                    "dipakai dengan `=~`, grup bernamanya otomatis jadi",
                    "VARIABEL LOKAL:",
                    "",
                    "  if /(?<thn>\\d{4})/ =~ tanggal",
                    "    puts thn        # variabel lokal, bukan m[:thn]",
                    "  end",
                    "",
                    "Bahan pola:",
                    "  .  \\d \\w \\s        \\D \\W \\S kebalikannya",
                    "  [abc] [^abc] [a-z]",
                    "  ^ $               awal/akhir BARIS (bawaan di Ruby!)",
                    "  \\A \\z             awal/akhir SELURUH teks",
                    "  \\b                batas kata",
                    "  * + ? {n} {n,m}   *? +? versi malas",
                    "  (...) (?:...) (?<nama>...)",
                    "",
                    "PERBEDAAN PENTING dari bahasa lain: di Ruby, `^` dan `$`",
                    "SELALU berarti awal dan akhir BARIS, bukan teks. Untuk",
                    "memvalidasi seluruh masukan pakai `\\A` dan `\\z`.",
                    "",
                    "  /^\\d+$/ menerima teks yang BARIS PERTAMANYA angka,",
                    "  berapa pun baris asing yang menyusul di bawahnya.",
                    "  /\\A\\d+\\z/ menuntut SELURUH teks berupa angka.",
                    "",
                    "Ini pernah jadi celah keamanan nyata di aplikasi Rails.",
                    "",
                    "Penanda: i (abaikan kapital), m (titik ikut baris baru),",
                    "x (abaikan spasi di pola supaya bisa diberi komentar).",
                ]
            },
            {
                "heading": "Menguraikan log dengan regex",
                "code": """log = <<~LOG
  2026-09-22 09:15:03 INFO  masuk user=andi ip=10.0.0.5
  2026-09-22 09:15:44 WARN  gagal user=budi ip=10.0.0.9 percobaan=3
  2026-09-22 09:16:10 ERROR koneksi putus ip=10.0.0.9
  baris yang formatnya tidak dikenal
  2026-09-22 09:17:55 INFO  keluar user=andi ip=10.0.0.5
LOG

POLA = /
  ^(?<tanggal>\\d{4}-\\d{2}-\\d{2})\\s+
  (?<jam>\\d{2}:\\d{2}:\\d{2})\\s+
  (?<taraf>INFO|WARN|ERROR)\\s+
  (?<pesan>.+)$
/x

baris = log.lines.filter_map { |b| b.match(POLA) }

puts format("%-10s%-6s%s", "jam", "taraf", "pesan")
puts "-" * 56
baris.each { |m| puts format("%-10s%-6s%s", m[:jam], m[:taraf], m[:pesan]) }

puts "---"
puts "baris dikenali : #{baris.size}"
baris.map { |m| m[:taraf] }.tally.sort.each { |t, n| puts "  #{t}: #{n}" }

puts "---"
ip = log.scan(/ip=(\\d{1,3}(?:\\.\\d{1,3}){3})/).flatten.uniq.sort
puts "IP unik: #{ip.join(', ')}"

samar = log.gsub(/(ip=\\d{1,3}\\.\\d{1,3}\\.\\d{1,3})\\.\\d{1,3}/, '\\\\1.xxx')
puts "disamarkan: #{samar.lines.first.chomp}"

puts "---"
["2026-09-22", "22/09/2026", "2026-13-40", "2026-09-22\\nsisipan"].each do |teks|
  longgar = /^\\d{4}-\\d{2}-\\d{2}$/.match?(teks)
  ketat = /\\A\\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\\d|3[01])\\z/.match?(teks)
  puts format("%-26s longgar=%-6s ketat=%s", teks.inspect, longgar, ketat)
end

puts "---"
tanggal = "2026-09-22"
if /(?<thn>\\d{4})-(?<bln>\\d{2})-(?<tgl>\\d{2})/ =~ tanggal
  puts "tahun #{thn}, bulan #{bln}, tanggal #{tgl}"
end"""
            },
            {
                "body": [
                    "Keluaran (bagian pentingnya):",
                    "  jam       taraf pesan",
                    "  --------------------------------------------------------",
                    "  09:15:03  INFO  masuk user=andi ip=10.0.0.5",
                    "  09:15:44  WARN  gagal user=budi ip=10.0.0.9 percobaan=3",
                    "  09:16:10  ERROR koneksi putus ip=10.0.0.9",
                    "  09:17:55  INFO  keluar user=andi ip=10.0.0.5",
                    "  ---",
                    "  baris dikenali : 4",
                    "    ERROR: 1",
                    "    INFO: 2",
                    "    WARN: 1",
                    "  ---",
                    "  IP unik: 10.0.0.5, 10.0.0.9",
                    "  disamarkan: 2026-09-22 09:15:03 INFO  masuk user=andi ip=10.0.0.xxx",
                    "  ---",
                    "  \"2026-09-22\"               longgar=true   ketat=true",
                    "  \"22/09/2026\"               longgar=false  ketat=false",
                    "  \"2026-13-40\"               longgar=true   ketat=false",
                    "  \"2026-09-22\\nsisipan\"      longgar=true   ketat=false",
                    "  ---",
                    "  tahun 2026, bulan 09, tanggal 22",
                    "",
                    "lalu tabel perbandingan pola, lalu baris terakhir",
                    "'tahun 2026, bulan 09, tanggal 22'.",
                    "",
                    "Tabel perbandingan itulah pelajaran terpentingnya. Pola",
                    "`^...$` MENERIMA teks yang baris pertamanya cocok,",
                    "berapa pun baris asing yang menyusul. Untuk validasi",
                    "masukan, `\\A...\\z` yang benar — selalu.",
                    "",
                    "Penanda `/x` membuat spasi dan baris baru di dalam pola",
                    "DIABAIKAN, sehingga pola panjang bisa ditulis bertingkat",
                    "dan diberi komentar. Tanpa itu, POLA di atas harus jadi",
                    "satu baris sepanjang seratus karakter.",
                    "",
                    "`filter_map` (Ruby 2.7) menggabungkan map dan compact:",
                    "ubah tiap elemen, buang yang menghasilkan nil. Persis",
                    "yang dibutuhkan saat sebagian baris tidak cocok pola.",
                    "",
                    "PERINGATAN yang sama seperti di bahasa lain: JANGAN",
                    "mengurai HTML dengan regex — HTML bisa bersarang tanpa",
                    "batas dan regex tidak bisa menghitung kedalaman. Pakai",
                    "Nokogiri. Waspadai juga kuantifier bersarang seperti",
                    "`(a+)+` yang bisa menggantung pada teks panjang.",
                ]
            },
        ],
    },
    {
        "title": "17. Waktu & Tanggal",
        "sections": [
            {
                "body": [
                    "Ruby punya tiga kelas waktu, dan memilihnya penting:",
                    "",
                    "  Time      titik waktu, presisi sampai nanodetik. Ada",
                    "            di inti bahasa, tanpa require.",
                    "  Date      tanggal saja, tanpa jam. require \"date\"",
                    "  DateTime  usang, jangan dipakai di kode baru.",
                    "",
                    "Membuat:",
                    "  Time.now",
                    "  Time.new(2026, 9, 22, 14, 30, 0)",
                    "  Time.at(1758547800)        dari epoch",
                    "  Time.now.utc               ubah ke UTC",
                    "",
                    "  require \"date\"",
                    "  Date.today",
                    "  Date.new(2026, 9, 22)",
                    "  Date.parse(\"2026-09-22\")",
                    "  Date.strptime(\"22/09/2026\", \"%d/%m/%Y\")",
                    "",
                    "Memformat dengan strftime:",
                    "  %Y tahun 4 digit      %y tahun 2 digit",
                    "  %m bulan 01-12        %-m bulan tanpa nol di depan",
                    "  %d tanggal 01-31      %-d tanpa nol",
                    "  %H jam 00-23          %I jam 01-12",
                    "  %M menit              %S detik",
                    "  %A Monday             %a Mon",
                    "  %B January            %b Jan",
                    "  %j hari ke-n          %U pekan ke-n",
                    "  %F sama dengan %Y-%m-%d",
                    "  %T sama dengan %H:%M:%S",
                    "",
                    "Awalan `-` menghilangkan nol di depan. Khas Ruby dan",
                    "sangat berguna.",
                    "",
                    "ARITMETIKA, dan di sinilah Time dan Date berbeda:",
                    "",
                    "  Time + 3600        tambah 3600 DETIK",
                    "  Date + 1           tambah 1 HARI",
                    "  Date >> 1          tambah 1 BULAN",
                    "  Date << 1          kurangi 1 bulan",
                    "  (t2 - t1)          Time: selisih dalam DETIK (Float)",
                    "  (d2 - d1).to_i     Date: selisih dalam HARI",
                    "",
                    "Satuan yang berbeda itu sumber bug klasik. Kalau kamu",
                    "menambah 30 ke sebuah Time berharap 30 hari, yang kamu",
                    "dapat 30 detik.",
                    "",
                    "ZONA WAKTU, dan aturan praktisnya cuma satu kalimat:",
                    "simpan SEMUA waktu dalam UTC, ubah ke zona pengguna",
                    "hanya saat MENAMPILKAN. Tanpa itu, laporan 'penjualan",
                    "hari ini' salah untuk sebagian penggunamu setiap hari.",
                ]
            },
            {
                "heading": "Menghitung selisih dan rentang tanggal",
                "code": """require "date"

mulai = Date.new(2026, 1, 15)
selesai = Date.new(2026, 9, 22)

puts "mulai    : #{mulai.strftime('%A, %-d %B %Y')}"
puts "selesai  : #{selesai.strftime('%A, %-d %B %Y')}"
puts "selisih  : #{(selesai - mulai).to_i} hari"

bulan = (selesai.year * 12 + selesai.month) - (mulai.year * 12 + mulai.month)
puts "bulan    : #{bulan}"

puts "---"
puts "besok    : #{mulai + 1}"
puts "sebulan  : #{mulai >> 1}"
puts "setahun  : #{mulai >> 12}"
puts "akhir bln: #{Date.new(mulai.year, mulai.month, -1)}"
puts "kabisat? : #{mulai.leap?}"
puts "hari ke  : #{mulai.yday} dari #{mulai.leap? ? 366 : 365}"

puts "---"
puts "jadwal mingguan:"
(mulai..(mulai + 21)).step(7) { |d| puts "  #{d.strftime('%a, %d %b %Y')}" }

puts "---"
pekan, kerja = (mulai..(mulai + 6)).partition { |d| d.saturday? || d.sunday? }
puts "akhir pekan: #{pekan.map { |d| d.strftime('%a %d') }.join(', ')}"
puts "hari kerja : #{kerja.size} hari"

puts "---"
t = Time.at(1_758_547_800).utc
puts "waktu     : #{t.strftime('%F %T %Z')}"
puts "+1 jam    : #{(t + 3600).strftime('%F %T')}"
puts "+1 hari   : #{(t + 86_400).strftime('%F %T')}"
puts "epoch     : #{t.to_i}"

puts "---"
lahir = Date.new(2006, 12, 1)
acuan = Date.new(2026, 9, 22)
belum = ([acuan.month, acuan.day] <=> [lahir.month, lahir.day]).negative?
puts "lahir     : #{lahir}"
puts "acuan     : #{acuan}"
puts "usia      : #{acuan.year - lahir.year - (belum ? 1 : 0)} tahun\""""
            },
            {
                "body": [
                    "Keluaran:",
                    "  mulai    : Thursday, 15 January 2026",
                    "  selesai  : Tuesday, 22 September 2026",
                    "  selisih  : 250 hari",
                    "  bulan    : 8",
                    "  ---",
                    "  besok    : 2026-01-16",
                    "  sebulan  : 2026-02-15",
                    "  setahun  : 2027-01-15",
                    "  akhir bln: 2026-01-31",
                    "  kabisat? : false",
                    "  hari ke  : 15 dari 365",
                    "  ---",
                    "  jadwal mingguan:",
                    "    Thu, 15 Jan 2026",
                    "    Thu, 22 Jan 2026",
                    "    Thu, 29 Jan 2026",
                    "    Thu, 05 Feb 2026",
                    "  ---",
                    "  akhir pekan: Sat 17, Sun 18",
                    "  hari kerja : 5 hari",
                    "  ---",
                    "  waktu     : 2025-09-22 13:30:00 UTC",
                    "  +1 jam    : 2025-09-22 14:30:00",
                    "  +1 hari   : 2025-09-23 13:30:00",
                    "  epoch     : 1758547800",
                    "  ---",
                    "  lahir     : 2006-12-01",
                    "  acuan     : 2026-09-22",
                    "  usia      : 19 tahun",
                    "",
                    "`Date.new(tahun, bulan, -1)` memakai indeks negatif untuk",
                    "hari TERAKHIR bulan itu. Jauh lebih aman daripada",
                    "menghitung 28, 29, 30, atau 31 sendiri.",
                    "",
                    "Perhitungan usia di akhir menunjukkan jebakan yang sangat",
                    "sering: selisih TAHUN saja SALAH untuk orang yang belum",
                    "berulang tahun tahun ini. Di contoh itu selisih tahunnya",
                    "20 tapi usianya masih 19. Membandingkan pasangan",
                    "[bulan, tanggal] sebagai array menyelesaikannya dalam",
                    "satu baris.",
                    "",
                    "Perhatikan perbandingannya memakai `<=>` lalu `.negative?`,",
                    "BUKAN `<` langsung. Array di Ruby punya `<=>` tapi TIDAK",
                    "punya `<` -- menulis `[1, 2] < [1, 3]` melempar",
                    "NoMethodError. Ini beda dari Python, tempat perbandingan",
                    "tuple bekerja apa adanya.",
                    "",
                    "Perhatikan juga `Time.at(...)` memberi waktu 2025,",
                    "sedangkan tanggal Date-nya 2026. Angka epoch adalah detik",
                    "sejak 1970 — kalau kamu menuliskannya tangan, hampir",
                    "selalu meleset. Itu sebabnya waktu sebaiknya dibuat dari",
                    "tanggal yang terbaca, bukan dari angka epoch.",
                ]
            },
        ],
    },
    {
        "title": "18. Set, Struct & Data",
        "sections": [
            {
                "body": [
                    "SET — himpunan tanpa duplikat, dengan operasi himpunan:",
                    "",
                    "  require \"set\"      tidak perlu lagi sejak Ruby 3.2",
                    "",
                    "  a = Set[1, 2, 3]",
                    "  b = [2, 3, 4].to_set",
                    "",
                    "  a | b     gabungan          1,2,3,4",
                    "  a & b     irisan            2,3",
                    "  a - b     selisih           1",
                    "  a ^ b     beda simetris     1,4",
                    "  a.subset?(b)  a.superset?(b)",
                    "  a.add(5) / a << 5 / a.add?(5)",
                    "  a.include?(2)",
                    "",
                    "`add?` mengembalikan nil kalau elemennya sudah ada. Cara",
                    "terpendek menulis 'kerjakan hanya kalau belum pernah",
                    "dilihat'.",
                    "",
                    "Kenapa Set alih-alih Array: `include?` pada Array",
                    "menelusuri satu per satu, pada Set langsung lewat hash.",
                    "Untuk seribu elemen, selisihnya bukan soal gaya lagi.",
                    "",
                    "STRUCT — kelas data dalam satu baris:",
                    "",
                    "  Titik = Struct.new(:x, :y)",
                    "  t = Titik.new(3, 4)",
                    "  t.x                    3",
                    "  t.x = 5                BISA DIUBAH",
                    "  t.to_a / t.to_h",
                    "  t == Titik.new(5, 4)   kesetaraan berbasis NILAI",
                    "",
                    "  Titik = Struct.new(:x, :y, keyword_init: true)",
                    "  Titik.new(x: 3, y: 4)  argumen berkunci",
                    "",
                    "Struct boleh punya method sendiri lewat blok:",
                    "  Titik = Struct.new(:x, :y) do",
                    "    def jarak = Math.sqrt(x**2 + y**2)",
                    "  end",
                    "",
                    "DATA (Ruby 3.2) — Struct yang BEKU:",
                    "",
                    "  Titik = Data.define(:x, :y)",
                    "  t = Titik.new(x: 3, y: 4)",
                    "  t.x = 5                ERROR: tidak ada setter",
                    "  t.with(x: 5)           SALINAN dengan sebagian diubah",
                    "",
                    "Ini padanan `record` di C# dan `data class` di Kotlin.",
                    "Untuk wadah data yang tidak boleh berubah — hasil query,",
                    "pesan, konfigurasi — `Data` lebih tepat daripada Struct.",
                    "",
                    "Aturan memilih:",
                    "  Data     data beku. Pilihan pertama sejak Ruby 3.2.",
                    "  Struct   perlu diubah sesudah dibuat.",
                    "  Class    punya PERILAKU, bukan cuma data.",
                    "  Hash     bentuknya belum tetap atau datang dari luar.",
                ]
            },
            {
                "heading": "Set, Struct, dan Data berdampingan",
                "code": """require "set"

# ---- SET: operasi himpunan ----
ikut_a = Set["Andi", "Budi", "Cici", "Dedi"]
ikut_b = Set["Cici", "Dedi", "Euis"]

puts "kelas A   : #{ikut_a.sort.join(', ')}"
puts "kelas B   : #{ikut_b.sort.join(', ')}"
puts "keduanya  : #{(ikut_a & ikut_b).sort.join(', ')}"
puts "salah satu: #{(ikut_a | ikut_b).sort.join(', ')}"
puts "hanya A   : #{(ikut_a - ikut_b).sort.join(', ')}"
puts "satu saja : #{(ikut_a ^ ikut_b).sort.join(', ')}"

sudah = Set.new
%w[andi budi andi cici budi].each do |nama|
  puts "proses #{nama}" if sudah.add?(nama)
end

puts "---"

# ---- STRUCT: data yang boleh berubah ----
Barang = Struct.new(:kode, :nama, :stok) do
  def menipis? = stok < 10
  def to_s = format("%-5s%-10s%3d%s", kode, nama, stok, menipis? ? "  (menipis)" : "")
end

gudang = [
  Barang.new("B01", "Kabel", 10),
  Barang.new("B02", "Adaptor", 4),
  Barang.new("B03", "Mouse", 25),
]

gudang.each { |b| puts b }
gudang[0].stok -= 5
puts "sesudah keluar 5:"
puts gudang[0]

puts "---"

# ---- DATA: beku, dengan `with` ----
Produk = Data.define(:nama, :kategori, :harga) do
  def mahal? = harga > 100_000
end

kopi = Produk.new(nama: "Kopi", kategori: "Minuman", harga: 25_000)
puts "asli      : #{kopi.nama} #{kopi.harga} mahal=#{kopi.mahal?}"

naik = kopi.with(harga: 120_000)
puts "hasil with: #{naik.nama} #{naik.harga} mahal=#{naik.mahal?}"
puts "asli tetap: #{kopi.harga}"

kembar = Produk.new(nama: "Kopi", kategori: "Minuman", harga: 25_000)
puts "sama nilainya? #{kopi == kembar}"

begin
  Produk.new(nama: "Teh")
rescue ArgumentError => e
  puts "Data menolak field kurang: #{e.class}"
end

begin
  kopi.instance_variable_set(:@harga, 1)
rescue FrozenError
  puts "Data benar-benar beku: FrozenError"
end"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  kelas A   : Andi, Budi, Cici, Dedi",
                    "  kelas B   : Cici, Dedi, Euis",
                    "  keduanya  : Cici, Dedi",
                    "  salah satu: Andi, Budi, Cici, Dedi, Euis",
                    "  hanya A   : Andi, Budi",
                    "  satu saja : Andi, Budi, Euis",
                    "  proses andi",
                    "  proses budi",
                    "  proses cici",
                    "  ---",
                    "  B01  Kabel      10",
                    "  B02  Adaptor     4  (menipis)",
                    "  B03  Mouse      25",
                    "  sesudah keluar 5:",
                    "  B01  Kabel       5  (menipis)",
                    "  ---",
                    "  asli      : Kopi 25000 mahal=false",
                    "  hasil with: Kopi 120000 mahal=true",
                    "  asli tetap: 25000",
                    "  sama nilainya? true",
                    "  Data menolak field kurang: ArgumentError",
                    "  Data benar-benar beku: FrozenError",
                    "",
                    "`sudah.add?(nama)` mencetak hanya tiga nama dari lima",
                    "karena dua di antaranya duplikat. Pola ini jauh lebih",
                    "pendek daripada memeriksa `include?` lalu menambahkan,",
                    "dan hanya sekali mencari di hash.",
                    "",
                    "Perbedaan Struct dan Data terlihat jelas: stok pada",
                    "Struct bisa dikurangi langsung, sedangkan Data tidak",
                    "punya setter sama sekali. Yang setara di Data adalah",
                    "`.with`, yang menghasilkan objek BARU dan meninggalkan",
                    "yang lama apa adanya.",
                    "",
                    "Data juga MENOLAK pembuatan yang field-nya kurang,",
                    "sedangkan Struct diam-diam mengisinya nil. Ketegasan itu",
                    "menangkap salah ketik sejak baris pertama, bukan tiga",
                    "fungsi kemudian saat nil-nya baru dipakai.",
                ]
            },
        ],
    },
    {
        "title": "19. Ruby untuk Skrip Sistem",
        "sections": [
            {
                "body": [
                    "Ruby sangat nyaman dipakai menggantikan skrip Bash yang",
                    "sudah terlalu panjang. Semuanya ada di pustaka standar.",
                    "",
                    "ARGUMEN dan LINGKUNGAN:",
                    "  ARGV                array argumen, TANPA nama program",
                    "  $PROGRAM_NAME       nama programnya",
                    "  ENV[\"HOME\"]         variabel lingkungan",
                    "  ENV.fetch(\"API_KEY\") melempar kalau tidak ada",
                    "",
                    "`ENV.fetch` tanpa nilai bawaan adalah kebiasaan yang",
                    "baik untuk konfigurasi wajib: lebih baik gagal saat",
                    "start daripada berjalan dengan nil yang baru meledak",
                    "satu jam kemudian.",
                    "",
                    "MASUKAN:",
                    "  gets                satu baris dari stdin",
                    "  $stdin.read         seluruhnya",
                    "  $stdin.each_line { } baris demi baris",
                    "  ARGF.each_line { }   dari berkas di ARGV, atau stdin",
                    "  warn \"pesan\"         cetak ke stderr",
                    "",
                    "ARGF berguna: ia membuat skripmu berperilaku seperti",
                    "perkakas Unix — menerima berkas sebagai argumen ATAU",
                    "pipa dari perintah lain, tanpa kode tambahan.",
                    "",
                    "KELUAR dengan kode status:",
                    "  exit 0     berhasil",
                    "  exit 1     gagal",
                    "  abort \"pesan\"   cetak ke stderr lalu keluar dengan 1",
                    "",
                    "MENJALANKAN PERINTAH LAIN, dari yang paling berbahaya:",
                    "",
                    "  `ls -l`              backtick: ambil keluarannya",
                    "  system(\"ls -l\")      jalankan, kembalikan true/false",
                    "  system(\"ls\", \"-l\")   BENTUK ARRAY, tanpa shell",
                    "  require \"open3\"",
                    "  Open3.capture3(\"ls\", \"-l\")  keluaran, galat, status",
                    "",
                    "ATURAN KEAMANAN: bentuk SATU STRING dijalankan lewat",
                    "shell, sehingga isi variabel bisa jadi PERINTAH KEDUA.",
                    "Titik koma, tanda pipa, dan tanda dolar di dalam variabel",
                    "semuanya punya arti khusus bagi shell.",
                    "",
                    "  satu string  -> shell mengurai isinya, perintah kedua",
                    "                  yang tersembunyi di variabel ikut jalan",
                    "  bentuk array -> variabelnya dioper apa adanya sebagai",
                    "                  SATU argumen, shell tidak dilibatkan",
                    "",
                    "Pakai bentuk array selalu, kecuali kamu memang butuh",
                    "pipa atau pengalihan.",
                    "",
                    "OptionParser di pustaka standar menangani flag, nilai,",
                    "dan teks bantuan tanpa satu gem pun.",
                ]
            },
            {
                "heading": "Skrip yang berperilaku seperti perkakas Unix",
                "code": """require "optparse"
require "open3"

# ---- Menguraikan argumen dengan OptionParser ----
opsi = { minimal: 0, urut: :nilai, rinci: false }

penguji = OptionParser.new do |o|
  o.banner = "Pemakaian: rapor.rb [opsi] [berkas...]"
  o.on("-m", "--minimal N", Integer, "Batas nilai minimal") { |v| opsi[:minimal] = v }
  o.on("-u", "--urut GAYA", %i[nama nilai], "Urutkan: nama|nilai") { |v| opsi[:urut] = v }
  o.on("-v", "--rinci", "Tampilkan rincian") { opsi[:rinci] = true }
  o.on("-h", "--help", "Tampilkan bantuan ini") { puts o }
end

# Di skrip sungguhan: penguji.parse!(ARGV)
penguji.parse!(%w[--minimal 75 --urut nilai --rinci])
puts "minimal=#{opsi[:minimal]} urut=#{opsi[:urut]} rinci=#{opsi[:rinci]}"

puts "---"

# ---- Lingkungan ----
puts "HOME ada?  : #{ENV.key?('HOME')}"
puts "tak ada    : #{ENV.fetch('TIDAK_ADA_VAR', '(bawaan)')}"
begin
  ENV.fetch("WAJIB_TAPI_KOSONG")
rescue KeyError
  puts "ENV.fetch tanpa bawaan -> KeyError, gagal sejak awal"
end

puts "---"

# ---- Menjalankan perintah: bentuk ARRAY, tanpa shell ----
keluaran, galat, status = Open3.capture3("echo", "halo dari perintah luar")
puts "keluaran : #{keluaran.chomp}"
puts "galat    : #{galat.empty? ? '(kosong)' : galat}"
puts "status   : #{status.success? ? 'berhasil' : 'gagal'}"

_, _, gagal = Open3.capture3("false")
puts "perintah gagal -> kode #{gagal.exitstatus}"

puts "---"

# ---- Kenapa bentuk array penting ----
# Titik koma di bawah ini SEHARUSNYA jadi pemisah perintah bagi shell.
# Dengan bentuk array, ia tidak pernah sampai ke shell.
nilai_mencurigakan = "biasa; echo SEHARUSNYA-TIDAK-JALAN"
aman, = Open3.capture3("echo", nilai_mencurigakan)
puts "bentuk array: #{aman.chomp}"
puts "titik koma tetap jadi teks, bukan perintah kedua"

puts "---"

warn "peringatan ini masuk stderr, bukan stdout"
puts "program selesai dengan kode 0\""""
            },
            {
                "body": [
                    "Keluaran di stdout:",
                    "  minimal=75 urut=nilai rinci=true",
                    "  ---",
                    "  HOME ada?  : true",
                    "  tak ada    : (bawaan)",
                    "  ENV.fetch tanpa bawaan -> KeyError, gagal sejak awal",
                    "  ---",
                    "  keluaran : halo dari perintah luar",
                    "  galat    : (kosong)",
                    "  status   : berhasil",
                    "  perintah gagal -> kode 1",
                    "  ---",
                    "  bentuk array: biasa; echo SEHARUSNYA-TIDAK-JALAN",
                    "  titik koma tetap jadi teks, bukan perintah kedua",
                    "  ---",
                    "  program selesai dengan kode 0",
                    "",
                    "Baris peringatannya masuk stderr, jadi tidak ikut kalau",
                    "keluarannya dialihkan ke berkas.",
                    "",
                    "Baris 'bentuk array' adalah buktinya: seluruh isi",
                    "variabel tercetak APA ADANYA sebagai satu argumen,",
                    "termasuk titik komanya. Dengan satu string yang disisipi",
                    "variabel, shell akan mengurainya dan menjalankan bagian",
                    "sesudah titik koma sebagai perintah tersendiri — dan",
                    "kalau variabel itu datang dari pengguna, isinya bisa apa",
                    "saja.",
                    "",
                    "`%i[nama nilai]` di OptionParser membatasi nilai yang",
                    "diterima. Argumen di luar daftar itu ditolak otomatis",
                    "beserta pesan yang menjelaskan pilihannya — validasi",
                    "gratis.",
                    "",
                    "Kebiasaan yang membuat skrip Ruby berperilaku baik di",
                    "terminal:",
                    "  - Keluaran hasil ke stdout, pesan status ke stderr.",
                    "  - Kode keluar 0 untuk berhasil, bukan-nol untuk gagal.",
                    "  - Terima berkas dari ARGV maupun pipa lewat ARGF.",
                    "  - Sediakan --help.",
                    "  - Baris pertama #!/usr/bin/env ruby lalu chmod +x.",
                ]
            },
        ],
    },
    {
        "title": "20. Gaya, Kualitas & Jebakan Umum",
        "sections": [
            {
                "body": [
                    "Ringkasan hal-hal yang paling sering salah di Ruby dan",
                    "kebiasaan yang membuat kode tetap enak dirawat.",
                    "",
                    "GAYA yang dipatuhi hampir seluruh dunia Ruby:",
                    "  - Indentasi DUA spasi, bukan empat, bukan tab.",
                    "  - snake_case untuk method dan variabel.",
                    "  - PascalCase untuk class dan module.",
                    "  - SCREAMING_CASE untuk konstanta.",
                    "  - Akhiran ? untuk yang mengembalikan bool.",
                    "  - Akhiran ! untuk versi yang lebih berbahaya.",
                    "  - Kurawal untuk blok satu baris, do...end untuk banyak.",
                    "  - Baris maksimal sekitar 100 karakter.",
                    "  - Tanpa `return` di baris terakhir method.",
                    "",
                    "RuboCop menegakkan semuanya otomatis. Pasang sejak awal;",
                    "di proyek lama, `rubocop --auto-gen-config` membekukan",
                    "keadaan sekarang sehingga hanya kode BARU yang diperiksa.",
                    "",
                    "JEBAKAN YANG PALING SERING:",
                    "",
                    "  1. Method ber-seru mengembalikan nil kalau tidak ada",
                    "     yang berubah. Jangan merangkai method ber-seru.",
                    "",
                    "  2. String BISA DIUBAH. Mengoper string ke method lain",
                    "     yang menambahinya akan mengubah string aslimu.",
                    "     Komentar magic pembeku literal di baris pertama",
                    "     berkas membuat semua literalnya beku.",
                    "",
                    "  3. Nilai bawaan Hash yang BERBAGI objek. Hash.new([])",
                    "     membuat SATU array yang dikembalikan untuk setiap",
                    "     kunci yang tidak ada, dan menambahinya tidak pernah",
                    "     menyimpannya. Yang benar bentuk blok:",
                    "     Hash.new { |h, k| h[k] = [] }",
                    "",
                    "  4. `and`/`or` berprioritas lebih rendah daripada `=`.",
                    "     Pakai `&&` dan `||` untuk logika; `and`/`or` hanya",
                    "     untuk alur seperti `lakukan or abort`.",
                    "",
                    "  5. Pembagian dua Integer memotong sisanya.",
                    "",
                    "  6. `puts` pada array mencetak tiap elemen di baris",
                    "     sendiri, dan array kosong mencetak BARIS KOSONG.",
                    "     Pakai `p` atau `.inspect` untuk melihat bentuknya.",
                    "",
                    "  7. Variabel class @@x DIBAGI dengan seluruh turunan.",
                    "     Subclass bisa mengacaukan induknya. Untuk kode baru,",
                    "     pakai variabel instance di level class.",
                ]
            },
            {
                "heading": "Melihat jebakannya sendiri",
                "code": """# frozen_string_literal: true

# ---- 1. Method ber-seru mengembalikan nil ----
a = "  sudah rapi  ".strip
b = "sudah rapi".strip!
puts "strip  : #{a.inspect}"
puts "strip! : #{b.inspect}    <- nil karena tidak ada yang berubah"

# ---- 2. frozen_string_literal ----
tetap = "literal ini beku"
begin
  tetap << "!"
rescue FrozenError
  puts "FrozenError: literal beku karena komentar magic di baris pertama"
end
bisa_diubah = +"ini bisa diubah"
bisa_diubah << "!"
puts "unary plus: #{bisa_diubah}"

puts "---"

# ---- 3. Nilai bawaan Hash yang berbagi objek ----
salah = Hash.new([])
salah[:a] << 1
salah[:b] << 2
puts "SALAH  a=#{salah[:a].inspect} b=#{salah[:b].inspect} kunci=#{salah.keys.inspect}"

benar = Hash.new { |h, k| h[k] = [] }
benar[:a] << 1
benar[:b] << 2
puts "BENAR  a=#{benar[:a].inspect} b=#{benar[:b].inspect} kunci=#{benar.keys.inspect}"

puts "---"

# ---- 4. and/or versus &&/|| ----
x = true and false
y = (true and false)
z = true && false
puts "x = true and false   -> #{x}     <- penugasan terjadi DULU"
puts "x = (true and false) -> #{y}"
puts "x = true && false    -> #{z}"

puts "---"

# ---- 5. Pembagian Integer ----
puts "631 / 8       = #{631 / 8}"
puts "631.to_f / 8  = #{631.to_f / 8}"
puts "631.fdiv(8)   = #{631.fdiv(8)}"
puts "631.divmod(8) = #{631.divmod(8).inspect}"

puts "---"

# ---- 6. puts pada array ----
print "puts []        -> "
puts []
puts "p []           -> #{[].inspect}"
print "puts [1, [2]]  -> "
puts [1, [2]]

puts "---"

# ---- 7. Variabel class dibagi turunan ----
class Induk
  @@bersama = "induk"
  @sendiri = "induk"

  class << self
    attr_accessor :sendiri
  end

  def self.bersama = @@bersama
  def self.bersama=(v) = @@bersama = v
end

class Anak < Induk
  @sendiri = "anak"
end

Anak.bersama = "diubah anak"
puts "@@bersama  Induk=#{Induk.bersama}  Anak=#{Anak.bersama}   <- ikut berubah"
puts "@sendiri   Induk=#{Induk.sendiri}  Anak=#{Anak.sendiri}   <- terpisah\""""
            },
            {
                "body": [
                    "Keluaran:",
                    "  strip  : \"sudah rapi\"",
                    "  strip! : nil    <- nil karena tidak ada yang berubah",
                    "  FrozenError: literal beku karena komentar magic di baris pertama",
                    "  unary plus: ini bisa diubah!",
                    "  ---",
                    "  SALAH  a=[1, 2] b=[1, 2] kunci=[]",
                    "  BENAR  a=[1] b=[2] kunci=[:a, :b]",
                    "  ---",
                    "  x = true and false   -> true     <- penugasan terjadi DULU",
                    "  x = (true and false) -> false",
                    "  x = true && false    -> false",
                    "  ---",
                    "  631 / 8       = 78",
                    "  631.to_f / 8  = 78.875",
                    "  631.fdiv(8)   = 78.875",
                    "  631.divmod(8) = [78, 7]",
                    "  ---",
                    "  puts []        -> ",
                    "  p []           -> []",
                    "  puts [1, [2]]  -> 1",
                    "  2",
                    "  ---",
                    "  @@bersama  Induk=diubah anak  Anak=diubah anak   <- ikut berubah",
                    "  @sendiri   Induk=induk  Anak=anak   <- terpisah",
                    "",
                    "Baris `SALAH` adalah jebakan yang paling mahal di daftar",
                    "ini. Perhatikan `kunci=[]` — TIDAK SATU PUN kunci",
                    "benar-benar tersimpan. Hash.new([]) membuat satu array",
                    "yang dikembalikan untuk SETIAP kunci yang tidak ada, dan",
                    "menambahinya mengubah array itu tanpa pernah",
                    "menyimpannya ke hash. Bentuk blok membuat array BARU per",
                    "kunci dan menyimpannya.",
                    "",
                    "Unary plus di depan literal membuat salinan yang tidak",
                    "beku — pasangan dari unary minus yang justru membekukan",
                    "dan mendeduplikasi. Keduanya berguna di berkas yang",
                    "memakai komentar magic pembeku literal.",
                    "",
                    "`divmod` mengembalikan hasil bagi DAN sisanya sekaligus,",
                    "dan `fdiv` langsung membagi sebagai Float. Keduanya",
                    "menyatakan maksudnya lebih jelas daripada `to_f` yang",
                    "diselipkan di tengah ekspresi.",
                    "",
                    "Untuk memeriksa kualitas kode secara otomatis:",
                    "  rubocop                 gaya dan kebiasaan buruk",
                    "  ruby -w berkas.rb       peringatan bawaan Ruby",
                    "  bundle exec rspec       tes",
                    "  bundle audit            gem dengan celah keamanan",
                ]
            },
        ],
    },
    {
        "title": "21. Proyek Utuh: Menggabungkan Semuanya",
        "sections": [
            {
                "body": [
                    "Materi penutup ini menggabungkan class, module, Struct,",
                    "Enumerable, exception, dan pemisahan tanggung jawab dalam",
                    "satu program utuh.",
                    "",
                    "Yang dibangun: sistem inventaris gudang. Yang penting",
                    "bukan fiturnya melainkan CARA bagiannya dipisah.",
                    "",
                    "Tiga lapisan, panah ketergantungan satu arah:",
                    "",
                    "  Antarmuka  ->  Layanan  ->  Model",
                    "",
                    "  MODEL     Barang, Gerak, dan keluarga galatnya.",
                    "            Tidak tahu apa-apa tentang layar.",
                    "  LAYANAN   Gudang dengan seluruh aturannya. TIDAK",
                    "            PERNAH memanggil puts.",
                    "  ANTARMUKA memanggil layanan dan mencetak hasilnya.",
                    "            Tidak menghitung apa pun.",
                    "",
                    "Ujinya satu kalimat: kalau program ini diubah jadi",
                    "aplikasi Sinatra, berapa banyak kode yang harus",
                    "disentuh? Jawaban yang benar: hanya bagian antarmuka.",
                    "",
                    "Di Ruby ada godaan khusus yang perlu dilawan: karena",
                    "`puts` tersedia di mana saja tanpa impor apa pun,",
                    "menyelipkannya ke dalam class layanan terasa sangat",
                    "mudah. Begitu itu terjadi, class-nya berhenti bisa diuji",
                    "tanpa membaca layar, dan berhenti bisa dipakai di",
                    "konteks lain.",
                ]
            },
            {
                "heading": "Program lengkap",
                "code": """# ---------------------------------------------------------------- MODEL
Barang = Struct.new(:kode, :nama, :stok, :harga) do
  def subtotal = stok * harga
  def to_s = format("%-5s%-12s%2d%10d%12d", kode, nama, stok, harga, subtotal)
end

module Gerak
  MASUK = :masuk
  KELUAR = :keluar
  SEMUA = [MASUK, KELUAR].freeze
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
  attr_reader :punya, :diminta

  def initialize(punya, diminta)
    @punya = punya
    @diminta = diminta
    super("stok cuma #{punya}, diminta #{diminta}")
  end
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
    barang = @isi[kode] or raise KodeTidakDikenalError, kode
    raise JumlahTidakSahError, jumlah unless jumlah.positive?

    baru = gerak == Gerak::MASUK ? barang.stok + jumlah : barang.stok - jumlah
    raise StokTidakCukupError.new(barang.stok, jumlah) if baru.negative?

    barang.stok = baru
  end

  # Satu `each` -> seluruh Enumerable ikut
  def each(&) = @isi.values.sort_by(&:kode).each(&)

  def nilai_persediaan = sum(&:subtotal)

  def stok_menipis(batas) = select { |b| b.stok < batas }.sort_by { |b| [b.stok, b.kode] }
end

# ------------------------------------------------------------ ANTARMUKA
gudang = Gudang.new

[["B01", "Kabel", 10, 15_000],
 ["B02", "Adaptor", 4, 85_000],
 ["B03", "Mouse", 25, 120_000]].each do |data|
  gudang.daftar(Barang.new(*data))
end

langkah = [
  ["B01", Gerak::MASUK, 15],
  ["B02", Gerak::KELUAR, 10],
  ["B03", Gerak::KELUAR, 5],
  ["B09", Gerak::MASUK, 1],
  ["B03", Gerak::KELUAR, 0],
]

langkah.each do |kode, gerak, jumlah|
  label = "#{gerak.to_s.capitalize} #{kode} #{jumlah}"
  stok = gudang.catat(kode, gerak, jumlah)
  puts "#{label} -> stok #{stok}"
rescue GudangError => e
  puts "#{label} -> DITOLAK: #{e.message}"
end

puts "---"
gudang.each { |b| puts b }

puts "---"
puts "nilai persediaan: #{gudang.nilai_persediaan}"

menipis = gudang.stok_menipis(10).map { |b| "#{b.kode} #{b.nama} (#{b.stok})" }
puts "stok menipis (<10): #{menipis.join(', ')}\""""
            },
            {
                "body": [
                    "Empat keputusan di program itu yang layak ditiru:",
                    "",
                    "  1. Keluarga galat mewarisi satu induk `GudangError`.",
                    "     Antarmuka cukup menulis `rescue GudangError` sekali",
                    "     dan tetap mendapat pesan yang tepat untuk tiap",
                    "     kasus — sementara galat lain (bug sungguhan) tetap",
                    "     naik dan terlihat.",
                    "",
                    "  2. `include Enumerable` dengan satu `each` memberi",
                    "     Gudang seluruh `sum`, `select`, `sort_by`, `count`.",
                    "     Tidak satu pun ditulis di class itu.",
                    "",
                    "  3. `each` MENGURUTKAN sebelum mengembalikan. Hash di",
                    "     Ruby memang mempertahankan urutan penyisipan, tapi",
                    "     mengandalkannya berarti keluaran berubah begitu ada",
                    "     penghapusan. Urutan yang eksplisit bisa diuji.",
                    "",
                    "  4. Gudang tidak memanggil `puts` sama sekali. Itu yang",
                    "     membuat seluruh aturannya bisa diuji dengan",
                    "     `assert_equal` tanpa membaca layar.",
                    "",
                    "Dua idiom Ruby yang muncul di situ:",
                    "",
                    "  `barang = @isi[kode] or raise ...`",
                    "    `or` berprioritas sangat rendah, jadi penugasannya",
                    "    terjadi dulu. Idiom ini terbaca seperti kalimat.",
                    "",
                    "  `def each(&) = @isi.values.sort_by(&:kode).each(&)`",
                    "    Ruby 3.1 memperbolehkan `&` polos untuk meneruskan",
                    "    blok tanpa menamainya.",
                    "",
                    "Langkah berikutnya kalau kamu ingin melanjutkannya:",
                    "  - Simpan ke JSON, sembunyikan di balik sebuah module",
                    "    Penyimpan sehingga Gudang tidak tahu bentuknya.",
                    "  - Tambahkan CLI dengan OptionParser.",
                    "  - Tulis tes Minitest untuk Gudang — perhatikan ini",
                    "    langsung bisa dilakukan tanpa mengubah satu baris pun,",
                    "    justru karena keputusan nomor 4.",
                ]
            },
        ],
    },
]
