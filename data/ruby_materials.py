RUBY_MATERIALS = [
    {
        "title": "1. Pengenalan Ruby & Instalasi",
        "sections": [
            {
                "body": [
                    "Ruby dibuat oleh Yukihiro Matsumoto, yang biasa dipanggil Matz, di",
                    "Jepang pada tahun 1995. Matz sendiri yang menulis tujuannya: bikin",
                    "programmer bahagia. Yang dia kejar adalah kenyamanan orang yang",
                    "menulis kode, bukan efisiensi mesin.",
                    "",
                    "Ada tiga istilah yang bakal sering kamu dengar soal Ruby:",
                    "  - Interpreted. Kode Ruby langsung dijalankan oleh program bernama",
                    "    ruby, tanpa langkah kompilasi terpisah seperti di Java atau C.",
                    "  - Dynamically typed. Variabel nggak punya tipe tetap. Tipe sebuah",
                    "    nilai baru diperiksa waktu programnya jalan.",
                    "  - Object-oriented. Program disusun dari objek. Di Ruby aturan ini",
                    "    berlaku untuk semuanya, seperti yang dibahas sebentar lagi.",
                    "",
                    "Tujuan \"programmer bahagia\" tadi kelihatan di hampir semua keputusan",
                    "desain Ruby:",
                    "  - Hampir nggak ada tanda baca yang wajib.",
                    "  - Satu hal bisa ditulis dengan banyak cara, dan kamu boleh milih yang",
                    "    paling enak dibaca.",
                    "  - Nama method dibikin mirip kalimat, misalnya empty?, save!, dan",
                    "    each_with_index.",
                    "",
                    "Di Ruby, semuanya objek. Gampangnya, objek itu nilai yang membawa",
                    "kemampuannya sendiri. Kemampuan itu disebut method. Angka, nil, true,",
                    "bahkan class pun objek:",
                    "",
                    "  5.class          Integer",
                    "  nil.class        NilClass",
                    "  true.class       TrueClass",
                    "  Integer.class    Class",
                    "  5.times { ... }  angka pun punya method",
                    "",
                    "Titik di 5.class artinya \"panggil method class milik 5\". Hasilnya nama",
                    "jenis objek itu. nil adalah nilai kosong, mirip null di bahasa lain.",
                    "",
                    "Ruby nggak punya tipe primitif. Di Java, angka bertipe int itu nilai",
                    "polos yang nggak punya method. Di Ruby, angka 5 tetap objek lengkap.",
                    "",
                    "Ruby juga nggak punya fungsi yang berdiri sendiri di luar objek. Yang",
                    "kelihatan seperti fungsi biasa, misalnya puts, ternyata method privat",
                    "milik Object. Makanya puts bisa dipanggil dari mana aja tanpa nulis",
                    "objeknya.",
                    "",
                    "Ruby dipakai untuk membangun Ruby on Rails, kerangka aplikasi web yang",
                    "dipakai GitHub, Shopify, Airbnb, dan Basecamp. Homebrew, Jekyll,",
                    "Vagrant, dan banyak alat bantu DevOps era 2010-an (alat untuk mengurus",
                    "server dan proses rilis aplikasi) juga ditulis pakai Ruby.",
                    "",
                    "Cara memasang Ruby:",
                    "",
                    "  Fedora     sudo dnf install ruby",
                    "  Debian     sudo apt install ruby-full",
                    "  macOS      brew install ruby",
                    "  Windows    RubyInstaller dari https://rubyinstaller.org",
                    "",
                    "Perintah yang diawali sudo dijalankan dengan hak administrator, jadi",
                    "komputer bakal minta kata sandimu dulu. Sesudah terpasang, cek dengan",
                    "ruby --version. Kalau versinya muncul, Ruby siap dipakai.",
                    "",
                    "Proyek yang berbeda kadang butuh versi Ruby yang berbeda. Untuk itu",
                    "programmer Ruby biasa pakai rbenv atau rvm, yaitu alat untuk memasang",
                    "beberapa versi Ruby sekaligus dan berganti di antaranya. Ini kebiasaan",
                    "standar di proyek Ruby.",
                    "",
                    "Cara menjalankan kode Ruby:",
                    "",
                    "  ruby berkas.rb       jalankan sebuah berkas",
                    "  irb                  sesi interaktif",
                    "  ruby -e 'puts 1+1'   jalankan satu baris",
                    "  ruby -c berkas.rb    periksa sintaks",
                    "",
                    "Di sesi interaktif, kamu ngetik satu baris, lalu Ruby langsung",
                    "menjalankannya dan nunjukin hasilnya. Cocok buat nyoba-nyoba. Opsi -c",
                    "cuma memeriksa apakah tulisanmu sah sebagai kode Ruby, tanpa",
                    "menjalankannya. Kalau sah, Ruby menjawab Syntax OK.",
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
                    "Program tadi mencetak enam baris. Baris ketiganya berbunyi \"Halo, Andi!",
                    "Umurmu 20 tahun.\", karena Ruby menghitung 2026 - 2006 dulu, baru",
                    "hasilnya ditempel ke teks.",
                    "",
                    "Kalau kamu pernah belajar Java atau C, ada beberapa hal yang langsung",
                    "kelihatan beda:",
                    "  - Nggak ada titik koma di akhir baris.",
                    "  - Tanda kurung waktu memanggil method nggak wajib. puts \"halo\" sama",
                    "    aja dengan puts(\"halo\").",
                    "  - Nggak ada deklarasi tipe. Kamu nggak perlu nulis bahwa nama itu",
                    "    berisi teks.",
                    "  - Nggak ada fungsi main. Ruby menjalankan kodenya mulai dari baris",
                    "    paling atas.",
                    "",
                    "Ada empat cara mencetak yang perlu kamu kenal:",
                    "  - puts mencetak nilainya lalu pindah baris. Namanya singkatan dari",
                    "    \"put string\". Kalau dikasih array, tiap elemennya dicetak di baris",
                    "    sendiri.",
                    "  - print mencetak tanpa pindah baris.",
                    "  - p mencetak bentuk debug sebuah nilai, yaitu bentuk untuk programmer",
                    "    yang lagi nyari kesalahan. p memanggil method inspect, lalu",
                    "    mengembalikan nilai itu lagi. Karena p menampilkan tanda kutip pada",
                    "    string, \"5\" dan 5 kelihatan bedanya.",
                    "  - pp sama seperti p, tapi struktur yang besar dicetak rapi di",
                    "    beberapa baris.",
                    "",
                    "Tulisan #{...} di dalam teks disebut interpolasi. Ruby menghitung isi",
                    "kurung kurawalnya, lalu menempelkan hasilnya ke teks. Isinya boleh",
                    "ekspresi apa pun, yaitu potongan kode apa pun yang menghasilkan nilai,",
                    "seperti 2026 - 2006 tadi. Interpolasi cuma jalan di dalam kutip ganda.",
                    "Di dalam kutip tunggal, '#{nama}' tercetak apa adanya.",
                    "",
                    "Baris 3.times { |i| ... } adalah contoh blok, gagasan paling khas",
                    "Ruby. Blok itu potongan kode yang dikasih ke sebuah method. Di sini",
                    "angka 3 dikasih potongan kode untuk dijalankan tiga kali, dan |i|",
                    "menampung nomor putarannya, mulai dari 0. times sendiri cuma method",
                    "biasa milik Integer yang menerima blok, jadi Ruby nggak butuh",
                    "perulangan khusus untuk ini. Blok dibahas lengkap di materi Blok, Proc",
                    "& Lambda.",
                    "",
                    "Konvensi penamaan, yaitu kebiasaan menamai yang diikuti hampir semua",
                    "programmer Ruby:",
                    "",
                    "  snake_case       variabel dan method",
                    "  PascalCase       class dan module",
                    "  SCREAMING_CASE   konstanta",
                    "  @nama            variabel instance",
                    "  @@nama           variabel class (jarang dipakai)",
                    "  $nama            variabel global (hindari)",
                    "  nama?            method yang mengembalikan true/false",
                    "  nama!            versi yang berbahaya atau mengubah objek",
                    "",
                    "snake_case artinya huruf kecil semua dengan garis bawah di antara kata,",
                    "misalnya jumlah_barang. PascalCase artinya tiap kata diawali huruf",
                    "besar tanpa pemisah, misalnya RekeningBank. Konstanta adalah nilai yang",
                    "nggak dimaksudkan untuk diubah. Variabel instance dan variabel class",
                    "dibahas di materi Class & Objek.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Hampir semua aplikasi menyusun kalimat dari data: notifikasi \"Pesananmu",
                    "sedang diantar\", struk kasir, atau pengingat tagihan listrik. Di Ruby,",
                    "kalimat seperti itu disusun dengan interpolasi #{...}. Programmer Ruby",
                    "juga biasa membuka irb untuk mencoba satu baris dulu sebelum menaruhnya",
                    "di program, dan memakai ruby -c untuk memeriksa sintaks sebuah berkas.",
                    "",
                    "Kasus kecil: pemilik warung ingin pesan otomatis untuk pelanggannya,",
                    "misalnya \"Halo, Bu Sari! Total belanjamu Rp45000.\" Bu Sari membeli 3",
                    "bungkus kopi seharga Rp15000 per bungkus.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tulis dulu kalimat yang kamu mau, lalu tandai bagian yang",
                    "     berubah-ubah tiap pelanggan: namanya dan totalnya.",
                    "  2. Simpan bagian yang berubah di variabel: nama, harga, dan jumlah.",
                    "  3. Tempel variabel itu ke kalimat dengan interpolasi. Totalnya boleh",
                    "     dihitung langsung di dalam kurung kurawal:",
                    "      nama = \"Bu Sari\"",
                    "      harga = 15000",
                    "      jumlah = 3",
                    "      puts \"Halo, #{nama}! Total belanjamu Rp#{harga * jumlah}.\"",
                    "  4. Ganti isi variabelnya, misalnya jumlah = 1, lalu jalankan lagi.",
                    "     Yang berubah harus cuma angkanya, dan kalimatnya tetap utuh.",
                    "",
                    "Jebakan: kalau kalimatnya ditulis dengan kutip tunggal, yang tercetak",
                    "adalah tulisan #{nama} apa adanya, tanpa diganti isinya.",
                ]
            },
        ],
    },
    {
        "title": "2. Variabel, Tipe & Objek",
        "sections": [
            {
                "body": [
                    "Variabel di Ruby nggak perlu dideklarasikan. Kamu cukup mengisinya:",
                    "",
                    "  nama = \"Andi\"",
                    "  umur = 20",
                    "  tinggi = 172.5",
                    "  aktif = true",
                    "  kosong = nil",
                    "",
                    "Tanda = artinya \"simpan nilai di kanan ke nama di kiri\". Kamu nggak",
                    "nulis tipenya, karena Ruby tahu sendiri dari nilainya.",
                    "",
                    "Tipe bawaan yang paling sering dipakai:",
                    "",
                    "  Integer     bilangan bulat, ukurannya tidak terbatas",
                    "  Float       pecahan",
                    "  Rational    pecahan persis: 1r/3",
                    "  String      teks, bisa diubah (beda dari Java/C#)",
                    "  Symbol      :nama, teks yang ringan dan tetap",
                    "  Array       daftar",
                    "  Hash        pasangan kunci-nilai",
                    "  Range       1..10 atau 1...10",
                    "  NilClass    nil",
                    "  TrueClass / FalseClass",
                    "",
                    "Beberapa di antaranya perlu penjelasan:",
                    "  - Rational menyimpan pecahan apa adanya. 1r/3 artinya sepertiga,",
                    "    persis, tanpa dibulatkan jadi 0.333...",
                    "  - Hash mirip kamus: tiap kunci menunjuk satu nilai. Array dan Hash",
                    "    dibahas lengkap di materi Array & Hash.",
                    "  - Range artinya rentang. Dua titik (1..10) ikut menyertakan 10,",
                    "    sedangkan tiga titik (1...10) berhenti di 9.",
                    "  - true dan false masing-masing punya class sendiri, yaitu TrueClass",
                    "    dan FalseClass.",
                    "",
                    "Integer di Ruby nggak punya batas. 2 ** 200, yaitu 2 pangkat 200,",
                    "menghasilkan angka 61 digit yang benar. Di bahasa yang ukuran",
                    "integernya dibatasi, hitungan sebesar itu bisa melimpah (overflow) dan",
                    "berubah jadi angka negatif.",
                    "",
                    "Symbol adalah tipe yang nggak ada di kebanyakan bahasa lain:",
                    "",
                    "  :nama         sebuah Symbol",
                    "  \"nama\"        sebuah String",
                    "",
                    "Bedanya begini. Symbol yang sama selalu objek yang sama persis di",
                    "memori. Dua String yang isinya sama tetap dua objek yang berbeda. Kamu",
                    "bisa melihatnya lewat object_id, nomor pengenal yang dimiliki tiap",
                    "objek:",
                    "",
                    "  \"a\".object_id == \"a\".object_id    false",
                    "  :a.object_id == :a.object_id      true",
                    "",
                    "Karena itu Symbol dipakai untuk nama, misalnya kunci hash, nama method,",
                    "dan penanda status. String dipakai untuk data.",
                    "",
                    "Aturan benar dan salah di Ruby simpel, dan beda dari hampir semua",
                    "bahasa lain. Waktu sebuah nilai dipakai sebagai kondisi, misalnya di",
                    "if, cuma dua nilai yang dianggap salah, yaitu false dan nil. Keduanya",
                    "disebut falsy. Semua nilai lain dianggap benar (truthy), termasuk 0,",
                    "\"\", [], dan {}.",
                    "",
                    "Kalau kamu datang dari PHP, JavaScript, atau Python, aturan ini",
                    "menghapus satu golongan jebakan sekaligus. Di bahasa-bahasa itu, 0 dan",
                    "teks kosong dianggap salah. Di Ruby, if 0 artinya benar.",
                    "",
                    "Konversi antartipe ditulis terang-terangan:",
                    "",
                    "  \"42\".to_i       42",
                    "  \"abc\".to_i      0     <- tanpa protes, hati-hati",
                    "  Integer(\"abc\")  melempar ArgumentError  <- lebih aman",
                    "  42.to_s         \"42\"",
                    "  \"3.5\".to_f      3.5",
                    "  :nama.to_s      \"nama\"",
                    "  \"nama\".to_sym   :nama",
                    "",
                    "Nama method-nya gampang diingat: to_i artinya to integer, to_s to",
                    "string, to_f to float, dan to_sym to symbol. Melempar error artinya",
                    "program berhenti dengan pesan error, kecuali error itu ditangkap.",
                    "Contoh di bawah menangkapnya pakai begin dan rescue. Cara kerjanya",
                    "dibahas di materi Exception & Penanganan Galat.",
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
                    "Beberapa hal di contoh tadi yang mungkin baru buatmu:",
                    "  - each menjalankan bloknya sekali untuk tiap elemen array. x berisi",
                    "    elemen yang sedang diproses.",
                    "  - printf(\"%-12s ...\") mencetak teks rata kiri selebar 12 karakter.",
                    "    Itu yang bikin kolomnya lurus.",
                    "  - x ? 'truthy' : 'falsy' artinya \"kalau x truthy pakai 'truthy',",
                    "    kalau nggak pakai 'falsy'\". Bentuk ini namanya operator ternary.",
                    "  - equal? mengecek apakah dua nilai itu objek yang sama persis, sama",
                    "    seperti membandingkan object_id-nya.",
                    "",
                    "respond_to?(:each) bertanya, \"objek ini punya method bernama each",
                    "nggak?\". Di keluaran, cuma Array, Hash, dan Range yang menjawab true.",
                    "Cara berpikir ini disebut duck typing: yang ditanya adalah apa yang",
                    "bisa dilakukan sebuah objek, dan tipenya nggak penting. Kalau dia jalan",
                    "seperti bebek dan bersuara seperti bebek, perlakukan dia sebagai bebek.",
                    "",
                    "Bandingkan juga \"abc\".to_i dan Integer(\"abc\"). Yang pertama memberi 0",
                    "tanpa protes, yang kedua melempar error. Kamu bakal memilih salah",
                    "satunya tiap kali membaca masukan dari pengguna. to_i menyembunyikan",
                    "kesalahan, jadi angka 0 yang keliru terus dipakai seolah benar.",
                    "Integer() membuat kesalahannya kelihatan saat itu juga.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Data yang datang dari formulir web, berkas, atau ketikan di terminal",
                    "selalu berbentuk teks, walaupun isinya angka. Formulir pemesanan toko",
                    "online mengirim jumlah barang sebagai \"3\", dan program harus mengubahnya",
                    "jadi Integer sebelum bisa menghitung. Pilihan antara to_i dan Integer()",
                    "menentukan apakah masukan yang salah ketahuan atau ikut terhitung.",
                    "",
                    "Kasus kecil: tiga pelanggan mengisi kolom jumlah dengan \"3\", \"10\", dan",
                    "\"dua\". Pesanan \"dua\" harus ditolak dengan pesan yang jelas, dan jangan",
                    "sampai tercatat sebagai pesanan 0 barang.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pahami masukan dan keluarannya: masukannya String, keluarannya",
                    "     Integer atau penolakan.",
                    "  2. Coba to_i dulu di irb. \"dua\".to_i hasilnya 0 tanpa protes, jadi",
                    "     to_i nggak bisa membedakan \"0\" dari teks yang ngawur.",
                    "  3. Pakai Integer(), yang melempar ArgumentError untuk teks yang isinya",
                    "     bukan angka, lalu tangkap error itu:",
                    "      teks = \"dua\"",
                    "      begin",
                    "        jumlah = Integer(teks)",
                    "      rescue ArgumentError",
                    "        puts \"Jumlah harus berupa angka: #{teks.inspect}\"",
                    "      end",
                    "  4. Periksa kasus pinggir \"0\". Integer(\"0\") sah, dan di Ruby 0 itu",
                    "     truthy, jadi if jumlah tetap lolos. Tolak pesanan nol dengan",
                    "     perbandingan langsung, yaitu jumlah > 0.",
                ]
            },
        ],
    },
    {
        "title": "3. String & Symbol",
        "sections": [
            {
                "body": [
                    "String adalah nilai berupa teks, dan Ruby punya banyak cara untuk",
                    "menulisnya:",
                    "",
                    "  'apa adanya'       tanpa interpolasi",
                    "  \"dengan #{nilai}\"  dengan interpolasi dan escape",
                    "  %w[a b c]          array dari kata: ['a','b','c']",
                    "  %i[a b c]          array dari symbol: [:a,:b,:c]",
                    "  <<~TEKS ... TEKS   heredoc; ~ memotong indentasinya",
                    "",
                    "Escape adalah kode khusus yang diawali backslash, misalnya \\n untuk",
                    "pindah baris. Di kutip tunggal, 'a\\nb' tercetak apa adanya, termasuk",
                    "backslash-nya. %w dan %i berguna kalau kamu butuh array berisi banyak",
                    "kata, karena kamu nggak perlu nulis kutip dan koma satu per satu.",
                    "Heredoc dipakai untuk teks yang panjangnya beberapa baris.",
                    "",
                    "String di Ruby bisa diubah. Ini beda dari Java, C#, Python, dan",
                    "JavaScript, yang string-nya nggak bisa diubah sesudah dibuat:",
                    "",
                    "  s = \"halo\"",
                    "  s << \" dunia\"       s sendiri berubah",
                    "  s.upcase!           s sendiri jadi huruf besar",
                    "",
                    "Tanda << menempelkan teks ke ujung string itu sendiri. Nggak ada string",
                    "baru yang dibuat.",
                    "",
                    "Ini sumber bug yang perlu kamu waspadai. Kalau kamu mengoper sebuah",
                    "string ke method lain, lalu method itu memanggil <<, string aslimu ikut",
                    "berubah. Method .freeze membekukan string, sehingga percobaan",
                    "mengubahnya jadi error.",
                    "",
                    "Catatan untuk Ruby versi baru: mulai Ruby 3.4, mengubah string yang",
                    "ditulis langsung di kode (disebut literal) seperti \"halo\" tadi bakal",
                    "memunculkan peringatan kalau Ruby dijalankan dengan opsi -w:",
                    "",
                    "  warning: literal string will be frozen in the future",
                    "",
                    "Programnya tetap jalan. Peringatan itu cuma bilang bahwa suatu hari",
                    "literal seperti itu bakal beku. Kalau kamu butuh string yang mau diisi",
                    "sedikit demi sedikit, mulai dari String.new seperti di contoh bawah.",
                    "",
                    "Tanda seru di akhir nama method itu konvensi, bukan aturan yang dipaksa",
                    "Ruby. Artinya \"versi ini lebih berbahaya daripada versi tanpa tanda",
                    "seru\". Biasanya bahayanya karena method itu mengubah objeknya sendiri:",
                    "",
                    "  s.upcase     kembalikan string baru, s tidak berubah",
                    "  s.upcase!    ubah s dan kembalikan s, atau nil kalau",
                    "               tidak ada yang berubah",
                    "",
                    "Jebakan: versi bertanda seru mengembalikan nil kalau nggak ada yang",
                    "berubah. \"ABC\".upcase! hasilnya nil, karena teksnya memang udah huruf",
                    "besar semua. Jadi x = s.upcase! bisa bikin x jadi nil tanpa satu pun",
                    "error. Karena itu jangan merangkai method bertanda seru seperti",
                    "s.strip!.upcase!. Begitu strip! mengembalikan nil, upcase! dipanggil",
                    "pada nil dan program berhenti dengan NoMethodError.",
                    "",
                    "Method string yang paling sering dipakai:",
                    "",
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
                    "Beberapa yang namanya kurang jelas:",
                    "  - strip membuang spasi di kedua ujung. lstrip cuma di kiri, rstrip",
                    "    cuma di kanan.",
                    "  - swapcase menukar huruf besar jadi kecil dan sebaliknya.",
                    "  - center, ljust, dan rjust meratakan teks ke tengah, kiri, atau kanan",
                    "    dalam lebar tertentu.",
                    "  - chars memecah string jadi array huruf, bytes jadi array angka byte,",
                    "    dan lines jadi array baris.",
                    "  - tr(\"abc\", \"xyz\") mengganti huruf demi huruf: a jadi x, b jadi y,",
                    "    c jadi z.",
                    "",
                    "Beda sub dan gsub: sub mengganti kemunculan pertama, gsub mengganti",
                    "semuanya. Huruf g di depannya artinya global.",
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
                    "Angka posisi 15 dihitung dari 0. Huruf R di awal kalimat ada di posisi",
                    "0, jadi kata \"untuk\" mulai di huruf ke-16.",
                    "",
                    "max_by(&:length) memakai dua hal khas Ruby sekaligus. max_by mencari",
                    "elemen yang nilainya paling besar menurut sebuah blok. &:length adalah",
                    "singkatan dari { |x| x.length }. Jadi baris itu mencari kata yang",
                    "paling panjang.",
                    "",
                    "Bentuk &:nama_method disebut symbol-to-proc, dan kamu bakal sering",
                    "ketemu bentuk ini di kode Ruby:",
                    "",
                    "  arr.map(&:upcase)",
                    "  arr.select(&:even?)",
                    "  arr.sort_by(&:length)",
                    "",
                    "Bagian begin ... rescue menangkap FrozenError, yaitu error yang muncul",
                    "waktu string beku mau diubah, lalu mencetak pesannya. Tanpa rescue,",
                    "program berhenti di baris tetap << \"!\".",
                    "",
                    "350_000 dengan garis bawah sama persis dengan 350000. Garis bawahnya",
                    "cuma bikin angka gampang dibaca, dan boleh dipakai di semua angka.",
                    "",
                    "Heredoc yang dibuka dengan <<~ (pakai tilde) membuang indentasi",
                    "terkecil dari tiap barisnya. Jadi heredoc boleh ditulis menjorok",
                    "mengikuti kode di sekitarnya, dan spasi itu nggak ikut masuk ke",
                    "hasilnya. Kalau dibuka dengan <<- (tanpa tilde), cuma penanda",
                    "penutupnya yang boleh menjorok. Spasi di depan baris isinya tetap ikut.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Teks yang diketik orang hampir nggak pernah rapi. Data pelanggan toko",
                    "online dan formulir pendaftaran sekolah sering berisi spasi di ujung dan",
                    "pemisah yang beda-beda. Sebelum disimpan atau dicari, teks seperti itu",
                    "dirapikan dulu dengan strip, downcase, dan gsub. Tautan chat wa.me,",
                    "misalnya, minta nomor HP berformat internasional: diawali 62, tanpa nol",
                    "di depan, dan tanpa tanda hubung.",
                    "",
                    "Kasus kecil: nomor HP pelanggan tercatat sebagai \" 0812-3456 7890 \",",
                    "sedangkan sistem pengirim pesan butuh 6281234567890.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Bandingkan masukan dan keluaran huruf demi huruf. Spasi di ujung",
                    "     hilang, tanda hubung dan spasi di tengah hilang, dan 0 di depan",
                    "     jadi 62.",
                    "  2. Kerjakan satu per satu. strip membuang spasi di ujung, lalu dua",
                    "     gsub membuang tanda hubung dan spasi di tengah.",
                    "  3. Ganti awalannya dengan sub, yang cuma mengganti kemunculan pertama:",
                    "      hp = \" 0812-3456 7890 \".strip.gsub(\"-\", \"\").gsub(\" \", \"\")",
                    "      hp = hp.start_with?(\"0\") ? hp.sub(\"0\", \"62\") : hp",
                    "      puts hp",
                    "  4. Periksa nomor yang sudah benar, misalnya \"6281204567890\". Tanpa",
                    "     start_with?, sub mengganti nol pertama di tengah nomor itu, dan",
                    "     hasilnya jadi \"62812624567890\".",
                    "",
                    "Jebakan: jangan merangkai versi bertanda seru seperti hp.strip!.gsub!(...).",
                    "Untuk nomor yang ujungnya sudah rapi, strip! mengembalikan nil, lalu",
                    "gsub! dipanggil pada nil dan program berhenti dengan NoMethodError.",
                ]
            },
        ],
    },
    {
        "title": "4. Array & Hash",
        "sections": [
            {
                "body": [
                    "Array adalah daftar nilai yang berurutan. Cara membuatnya:",
                    "",
                    "  a = [1, 2, 3]",
                    "  a = Array.new(3, 0)      [0, 0, 0]",
                    "  a = %w[apel jeruk pir]   tanpa kutip dan koma",
                    "",
                    "Tiap elemen punya nomor urut yang disebut index, dimulai dari 0. Cara",
                    "mengambil isinya:",
                    "",
                    "  a[0]       elemen pertama",
                    "  a[-1]      elemen terakhir",
                    "  a[1..2]    irisan",
                    "  a[1, 2]    dua elemen mulai index 1",
                    "  a.first(2) / a.last(2)",
                    "  a.dig(0, 1) aman untuk array bersarang",
                    "",
                    "Index negatif menghitung dari belakang. a[-1] adalah elemen terakhir,",
                    "a[-2] satu sebelum terakhir. Dengan begitu kamu nggak perlu",
                    "sering-sering menulis length - 1.",
                    "",
                    "a[1..2] mengambil irisan dari index 1 sampai 2. a[1, 2] artinya \"mulai",
                    "dari index 1, ambil 2 elemen\". Array bersarang adalah array yang isinya",
                    "array lagi. a.dig(0, 1) sama dengan a[0][1], bedanya kalau a[0] ternyata",
                    "nil, dig mengembalikan nil dan nggak bikin error.",
                    "",
                    "Method yang sering dipakai untuk mengubah dan memeriksa array:",
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
                    "Yang perlu sedikit penjelasan:",
                    "  - insert(1, :x) menyisipkan :x di index 1.",
                    "  - delete(3) membuang semua elemen yang nilainya 3, sedangkan",
                    "    delete_at(0) membuang elemen di index 0.",
                    "  - minmax mengembalikan nilai terkecil dan terbesar sekaligus.",
                    "  - join(\", \") menggabungkan semua elemen jadi satu string, dipisah",
                    "    koma dan spasi.",
                    "  - sample mengambil satu elemen secara acak. shuffle mengacak urutan",
                    "    semua elemen.",
                    "  - compact membuang nil, dan flatten meratakan array bersarang jadi",
                    "    satu array biasa.",
                    "  - uniq membuang duplikat, dan array-nya nggak perlu diurutkan dulu.",
                    "    Di Rust, cara yang setara (dedup) cuma membuang duplikat yang",
                    "    bersebelahan, jadi datanya harus diurutkan dulu.",
                    "",
                    "Hash adalah kumpulan pasangan kunci dan nilai. Mirip kamus: kamu cari",
                    "lewat kuncinya, lalu dapat nilainya.",
                    "",
                    "  h = { \"nama\" => \"Andi\", \"umur\" => 20 }",
                    "  h = { nama: \"Andi\", umur: 20 }      kunci Symbol",
                    "",
                    "Bentuk kedua jauh lebih sering dipakai. Tulisan nama: adalah singkatan",
                    "dari :nama =>, jadi kuncinya Symbol. Kunci Symbol lebih cepat dan lebih",
                    "hemat memori daripada kunci String.",
                    "",
                    "Cara memakai hash:",
                    "",
                    "  h[:nama]                nil kalau tidak ada",
                    "  h.fetch(:nama)          melempar kalau tidak ada",
                    "  h.fetch(:x, \"bawaan\")   dengan nilai cadangan",
                    "  h[:kota] = \"Bandung\"",
                    "  h.key?(:nama) / h.value?(20)",
                    "  h.keys / h.values / h.size",
                    "  h.each { |k, v| ... }",
                    "  h.map / h.select / h.reject / h.sort_by",
                    "  h.merge(lain)           h.dig(:a, :b)",
                    "  h.transform_values { |v| v * 2 }",
                    "",
                    "Bedanya h[:nama] dan h.fetch(:nama) mirip bedanya to_i dan Integer()",
                    "di materi Variabel, Tipe & Objek. Untuk kunci yang nggak ada, h[...]",
                    "memberi nil tanpa protes, sedangkan fetch melempar KeyError. Jadi",
                    "salah ketik nama kunci langsung ketahuan. fetch(:x, \"bawaan\") memberi",
                    "nilai cadangan kalau kuncinya nggak ada.",
                    "",
                    "merge menggabungkan dua hash. Kalau ada kunci yang sama, nilai dari",
                    "hash di dalam kurung yang dipakai. transform_values membuat hash baru",
                    "yang nilainya sudah diubah oleh blok, sedangkan kuncinya tetap.",
                    "",
                    "Hash.new(0) membuat hash yang nilai bawaannya 0. Artinya, kunci yang",
                    "belum ada dianggap bernilai 0. Ini cara paling ringkas di Ruby untuk",
                    "menghitung berapa kali sesuatu muncul:",
                    "",
                    "  hitung = Hash.new(0)",
                    "  kata.each { |k| hitung[k] += 1 }",
                    "",
                    "Tanpa nilai bawaan 0, hitung[k] += 1 untuk kata yang baru pertama kali",
                    "muncul bakal gagal, karena nil nggak bisa ditambah 1.",
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
                    "Contoh itu memakai beberapa idiom Ruby. Idiom artinya cara menulis",
                    "yang sudah jadi kebiasaan umum di kalangan programmer Ruby.",
                    "  - sort_by { |m| -m[:nilai] } memakai tanda minus supaya urutannya",
                    "    menurun, dari nilai terbesar. Lebih pendek daripada sort lalu",
                    "    reverse.",
                    "  - sort_by { |k, n| [-n, k] } memakai array sebagai kunci urutan.",
                    "    Elemen pertama dibandingkan dulu. Kalau sama, baru elemen kedua.",
                    "    Ini cara paling gampang mengurutkan dua tingkat di Ruby. Di contoh",
                    "    itu, kata diurutkan dari yang paling sering muncul, lalu menurut",
                    "    abjad.",
                    "  - '%.2f' % nilai memakai operator % pada string untuk memformat",
                    "    angka, seperti printf. Artinya \"tulis sebagai pecahan dengan 2",
                    "    angka di belakang titik desimal\". Hasilnya sama dengan",
                    "    format('%.2f', nilai).",
                    "  - nilai.sum.to_f / nilai.size butuh .to_f. Integer dibagi Integer",
                    "    hasilnya Integer, dan sisanya dibuang. 631 / 8 hasilnya 78, bukan",
                    "    78.875.",
                    "  - group_by menghasilkan Hash yang nilainya array. Memanggil .sort",
                    "    pada hash menghasilkan array berisi pasangan kunci dan nilai, urut",
                    "    menurut kuncinya. Dengan begitu urutan keluarannya selalu pasti.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aplikasi kasir menyimpan pesanan sebagai daftar, dan harga menu sebagai",
                    "pasangan nama dan harga. Dua bentuk itu adalah array dan hash. Laporan",
                    "\"menu paling laku hari ini\" di kasir warung atau kafe dibangun dari",
                    "keduanya: hitung kemunculan tiap menu, lalu jumlahkan harganya.",
                    "",
                    "Kasus kecil: warung kopi mencatat enam pesanan hari ini, yaitu kopi, teh,",
                    "kopi, roti, kopi, dan teh. Harganya kopi Rp8000, teh Rp5000, dan roti",
                    "Rp10000. Pemiliknya ingin tahu berapa kali tiap menu dipesan dan berapa",
                    "pendapatannya.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tentukan bentuk datanya. pesanan berupa array nama menu, dan harga",
                    "     berupa hash dengan nama menu sebagai kunci.",
                    "  2. Untuk menghitung kemunculan, pakai Hash.new(0), supaya menu yang",
                    "     baru pertama kali muncul dianggap bernilai 0.",
                    "  3. Untuk pendapatan, ambil harga tiap pesanan dengan fetch, lalu",
                    "     jumlahkan:",
                    "      hitung = Hash.new(0)",
                    "      total = 0",
                    "      pesanan.each do |menu|",
                    "        hitung[menu] += 1",
                    "        total += harga.fetch(menu)",
                    "      end",
                    "  4. Cocokkan dengan hitungan tangan: kopi 3, teh 2, roti 1, dan total",
                    "     44000. Lalu coba pesanan yang salah ketik, misalnya \"kopii\". fetch",
                    "     langsung melempar KeyError yang menyebut kuncinya, sedangkan",
                    "     harga[\"kopii\"] memberi nil yang baru gagal di baris penjumlahan.",
                ]
            },
        ],
    },
    {
        "title": "5. Kendali Alur",
        "sections": [
            {
                "body": [
                    "Percabangan artinya program memilih jalan berdasarkan sebuah kondisi.",
                    "Bentuk dasarnya di Ruby:",
                    "",
                    "  if nilai >= 75",
                    "    puts \"Lulus\"",
                    "  elsif nilai >= 60",
                    "    puts \"Mengulang\"",
                    "  else",
                    "    puts \"Tidak Lulus\"",
                    "  end",
                    "",
                    "Ejaannya elsif, dengan satu huruf f dan tanpa huruf e di tengah.",
                    "Kondisinya nggak perlu dikurung, nggak ada kurung kurawal, dan bloknya",
                    "ditutup dengan end.",
                    "",
                    "Untuk perintah pendek, kondisinya boleh ditulis di belakang. Bentuk ini",
                    "disebut modifier:",
                    "",
                    "  puts \"Lulus\" if nilai >= 75",
                    "  return if daftar.empty?",
                    "  puts \"Kosong\" unless daftar.any?",
                    "",
                    "unless artinya \"if not\", alias \"kecuali kalau\". Kata ini khas Ruby.",
                    "Pakai unless kalau kondisi positifnya lebih enak dibaca. Baris terakhir",
                    "di atas, misalnya, terbaca \"cetak Kosong, kecuali kalau daftarnya ada",
                    "isinya\".",
                    "",
                    "Jangan pakai unless bersama else. Pembacanya harus membalik kondisinya",
                    "dua kali di kepala, dan hasilnya hampir selalu membingungkan.",
                    "",
                    "if di Ruby adalah ekspresi, artinya if menghasilkan nilai. Hasilnya",
                    "bisa langsung disimpan:",
                    "",
                    "  status = if nilai >= 75 then \"lulus\" else \"ulang\" end",
                    "",
                    "case jauh lebih kuat daripada switch di bahasa lain:",
                    "",
                    "  grade = case nilai",
                    "          when 85..100 then \"A\"",
                    "          when 75...85 then \"B\"",
                    "          when 60...75 then \"C\"",
                    "          else \"D\"",
                    "          end",
                    "",
                    "when memakai operator === (tiga tanda sama dengan) untuk mencocokkan.",
                    "Arti === berbeda-beda, tergantung jenis nilai yang ditulis di belakang",
                    "when:",
                    "",
                    "  Range === angka     apakah angkanya di dalam rentang",
                    "  Class === objek     apakah objeknya bertipe itu",
                    "  Regexp === string   apakah polanya cocok",
                    "  Proc === nilai      hasil pemanggilan lambda",
                    "  selain itu          perbandingan == biasa",
                    "",
                    "Jadi satu case boleh mencampur rentang, tipe, dan pola regex sekaligus.",
                    "switch di C atau Java nggak bisa melakukan itu. Regex, yaitu pola untuk",
                    "mencocokkan teks, dibahas di materi Ekspresi Reguler. Lambda dibahas di",
                    "materi Blok, Proc & Lambda.",
                    "",
                    "Ruby juga punya perulangan biasa, tapi jarang dipakai:",
                    "",
                    "  while i < 5 ... end",
                    "  until selesai ... end",
                    "  loop do ... break ... end",
                    "  for x in arr ... end      (hampir tidak pernah dipakai)",
                    "",
                    "until adalah kebalikan while: ulangi selama kondisinya belum benar.",
                    "loop do ... end mengulang terus sampai ketemu break.",
                    "",
                    "Yang sehari-hari dipakai programmer Ruby adalah method yang mengulang:",
                    "",
                    "  5.times { |i| ... }",
                    "  1.upto(5) { |i| ... }",
                    "  (1..5).each { |i| ... }",
                    "  arr.each { |x| ... }",
                    "  arr.each_with_index { |x, i| ... }",
                    "",
                    "upto menghitung naik dari 1 sampai 5. each_with_index memberi tiap",
                    "elemen beserta index-nya. Kalau kamu menulis for di Ruby, hampir pasti",
                    "ada cara yang lebih enak dibaca.",
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
                    "Urutan when itu penting. when 1..9 harus ditulis sebelum when Integer.",
                    "Kalau dibalik, semua bilangan bulat bakal tertangkap cabang Integer",
                    "duluan. Ruby nggak memperingatkanmu soal ini. Rust dan C# protes kalau",
                    "ada cabang yang nggak mungkin tercapai, Ruby nggak.",
                    "",
                    "Akibat urutan yang sama kelihatan di baris \"satuan 3.14\". Angka 3.14",
                    "ada di antara 1 dan 9, jadi cabang when 1..9 yang menangkapnya.",
                    "Cabang when Float cuma kebagian pecahan yang nggak masuk rentang mana",
                    "pun di atasnya.",
                    "",
                    "->(v) { ... } adalah lambda, yaitu potongan kode yang disimpan sebagai",
                    "nilai. Lambda bisa dipakai di when karena Proc mengartikan === sebagai",
                    "\"panggil aku dengan nilai ini\". Dengan begitu syarat di dalam case",
                    "boleh sebebas apa pun.",
                    "",
                    "case tanpa nilai di sebelahnya, seperti di contoh suhu, bekerja seperti",
                    "rantai if. Ruby mengecek tiap when dari atas, lalu memakai yang pertama",
                    "bernilai benar.",
                    "",
                    "each_with_object([]) menelusuri elemen sambil membawa sebuah wadah, di",
                    "sini array kosong. Bedanya dengan reduce, yang dibahas di materi",
                    "Enumerable: yang dikembalikan each_with_object selalu wadahnya. Di",
                    "reduce, kamu harus ingat mengembalikan wadah itu di tiap putaran, dan",
                    "lupa melakukannya adalah kesalahan yang sering terjadi.",
                    "",
                    "n.odd? dan n.even? adalah contoh konvensi tanda tanya. Method yang",
                    "mengembalikan true atau false diberi akhiran ?, sehingga kondisinya",
                    "terbaca seperti kalimat. n.odd? terbaca \"n ganjil?\".",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aturan bertingkat ada di mana-mana dalam aplikasi: diskon minimarket",
                    "menurut besar belanja, ongkos kirim menurut berat paket, atau predikat",
                    "rapor menurut nilai. Semuanya berbentuk \"kalau angkanya di rentang ini,",
                    "pakai aturan itu\", dan di Ruby bentuk itu paling rapi ditulis dengan case",
                    "dan Range.",
                    "",
                    "Kasus kecil: minimarket memberi diskon 5% untuk belanja Rp100.000 sampai",
                    "di bawah Rp200.000, dan diskon 10% mulai Rp200.000. Hitung diskon untuk",
                    "belanja Rp150.000, Rp99.999, dan tepat Rp100.000.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Gambar batasnya sebagai garis bilangan: di bawah 100.000 dapat 0%,",
                    "     100.000 sampai 199.999 dapat 5%, dan 200.000 ke atas dapat 10%.",
                    "  2. Ubah tiap potongan garis jadi Range. Tiga titik berhenti tepat",
                    "     sebelum ujungnya, jadi cocok untuk \"sampai di bawah\":",
                    "      persen = case belanja",
                    "               when 0...100_000       then 0",
                    "               when 100_000...200_000 then 5",
                    "               else                        10",
                    "               end",
                    "  3. Hitung potongannya dengan belanja * persen / 100. Untuk belanja",
                    "     150.000 hasilnya 7500.",
                    "  4. Uji tepat di batas. Belanja 99.999 dapat 0%, dan 100.000 dapat 5%.",
                    "",
                    "Jebakan: kalau cabang pertama ditulis 0..100_000 dengan dua titik, belanja",
                    "tepat Rp100.000 tertangkap di cabang itu, dan pelanggannya nggak dapat",
                    "diskon.",
                ]
            },
        ],
    },
    {
        "title": "6. Blok, Proc & Lambda",
        "sections": [
            {
                "body": [
                    "Blok adalah potongan kode yang dikasih ke sebuah method. Ini gagasan",
                    "yang paling khas di Ruby, dan bentuknya udah kamu lihat di 3.times",
                    "pada materi pertama.",
                    "",
                    "  arr.each { |x| puts x }",
                    "",
                    "  arr.each do |x|",
                    "    puts x",
                    "  end",
                    "",
                    "Dua tulisan itu artinya sama persis. Konvensinya: kurung kurawal untuk",
                    "blok satu baris, do...end untuk blok beberapa baris. Tulisan |x| di",
                    "awal blok adalah parameter, yaitu nama untuk nilai yang dikirim method",
                    "ke bloknya. Di sini each mengirim elemen array satu per satu.",
                    "",
                    "Sebuah method menjalankan blok yang dikasih kepadanya lewat yield:",
                    "",
                    "  def tiga_kali",
                    "    yield 1",
                    "    yield 2",
                    "    yield 3",
                    "  end",
                    "",
                    "  tiga_kali { |n| puts \"ke-#{n}\" }",
                    "",
                    "Tiap yield menjalankan blok sekali dan mengirim nilainya ke |n|. Jadi",
                    "contoh itu mencetak ke-1, ke-2, dan ke-3.",
                    "",
                    "block_given? mengecek apakah method itu dipanggil bersama blok. Kalau",
                    "nggak dicek, yield tanpa blok bakal melempar error LocalJumpError.",
                    "",
                    "Kegunaan blok yang paling berharga adalah menjamin sesuatu dibereskan",
                    "di akhir:",
                    "",
                    "  File.open(\"data.txt\") do |f|",
                    "      ...",
                    "  end          # berkas ditutup di sini, GAGAL ATAU TIDAK",
                    "",
                    "File.open membuka berkas, menjalankan blokmu, lalu menutup berkasnya",
                    "begitu blok selesai. Berkasnya tetap ditutup walaupun di tengah blok",
                    "terjadi error.",
                    "",
                    "Ini padanan using di C# dan with di Python. Bedanya, di Ruby fitur ini",
                    "dibangun dari mekanisme yang sama persis dengan each, tanpa sintaks",
                    "khusus.",
                    "",
                    "Proc dan lambda adalah blok yang disimpan jadi objek, sehingga bisa",
                    "dimasukkan ke variabel dan dipanggil kapan aja:",
                    "",
                    "  kuadrat = ->(x) { x * x }      lambda, bentuk panah",
                    "  kuadrat = lambda { |x| x * x }",
                    "  kuadrat = proc { |x| x * x }   Proc",
                    "  kuadrat.call(4)  /  kuadrat.(4)  /  kuadrat[4]",
                    "",
                    "Ada dua perbedaan antara proc dan lambda, dan dua-duanya penting:",
                    "  1. Jumlah argumen, yaitu nilai yang dikirim waktu memanggilnya.",
                    "     Lambda ketat: kalau jumlahnya salah, dia melempar ArgumentError.",
                    "     Proc longgar: argumen yang kurang diisi nil, yang kelebihan",
                    "     dibuang.",
                    "  2. return. return di dalam lambda cuma keluar dari lambda itu. return",
                    "     di dalam proc keluar dari method yang membuat proc itu, dan ini",
                    "     sering bikin kaget.",
                    "",
                    "Patokan praktisnya: pakai lambda, kecuali kamu punya alasan khusus.",
                    "",
                    "Tanda & mengubah blok jadi objek, dan sebaliknya:",
                    "",
                    "  def f(&blok)      tangkap bloknya sebagai Proc",
                    "  arr.map(&kuadrat) oper lambda sebagai blok",
                    "  arr.map(&:upcase) symbol-to-proc",
                    "",
                    "Bentuk terakhir sudah kamu kenal dari materi String & Symbol.",
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
                    "ensure adalah bagian method yang selalu dijalankan di akhir, apa pun",
                    "yang terjadi. Lihat bagian \"gagal\" di keluaran. Bloknya melempar error",
                    "lewat raise, jadi \"selesai gagal\" nggak pernah tercetak, tapi",
                    "\"(pembersihan gagal)\" tetap tercetak. Karena itu pola blok bisa",
                    "menjamin berkas ditutup dan koneksi dilepas. raise dan rescue dibahas",
                    "di materi Exception & Penanganan Galat.",
                    "",
                    "yield juga mengembalikan nilai terakhir dari bloknya. Dengan begitu",
                    "ulangi bisa mengumpulkan hasil tiap putaran ke dalam array, dan",
                    "ulangi(5) { |i| i * i } menghasilkan [1, 4, 9, 16, 25].",
                    "",
                    "Baris return to_enum(:ulangi, n) unless block_given? adalah idiom yang",
                    "dipakai pustaka standar Ruby, yaitu kumpulan class dan method yang ikut",
                    "terpasang bersama Ruby. Kalau method dipanggil tanpa blok, dia",
                    "mengembalikan Enumerator, bukan gagal. Enumerator adalah objek yang",
                    "bisa mengeluarkan elemen satu per satu dan bisa dirangkai dengan method",
                    "lain. arr.each tanpa blok tetap berguna karena alasan yang sama.",
                    "",
                    "Hash operasi menyimpan lambda sebagai nilai. Tiap operasi bisa diambil",
                    "lewat namanya, lalu dipanggil dengan .call(9, 4).",
                    "",
                    "Ketiga cara memanggil lambda, yaitu .call(x), .(x), dan [x], hasilnya",
                    "sama. Yang paling sering dipakai .call, karena paling jelas dibaca.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Blok muncul di hampir tiap halaman kode Ruby sungguhan. Rails membungkus",
                    "transaksi database dalam blok transaction do ... end, sehingga semua",
                    "perubahan di dalamnya dibatalkan kalau di tengah blok terjadi error.",
                    "Lambda dipakai untuk menyimpan aturan sebagai nilai, misalnya rumus",
                    "biaya tiap metode pembayaran di halaman checkout toko online.",
                    "",
                    "Kasus kecil: biaya admin pembayaran berbeda per metode. Transfer bank",
                    "kena Rp4.000, e-wallet kena 2% dari total, dan bayar di tempat (:cod)",
                    "gratis. Hitung biayanya untuk belanja Rp150.000 lewat e-wallet.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Masukannya total belanja dan nama metode, keluarannya biaya admin.",
                    "     Nama metode cocok disimpan sebagai Symbol.",
                    "  2. Tiap metode punya rumus sendiri. Daripada if dan elsif yang terus",
                    "     memanjang, simpan tiap rumus sebagai lambda di dalam hash:",
                    "      biaya = {",
                    "        transfer: ->(total) { 4_000 },",
                    "        ewallet:  ->(total) { total * 2 / 100 },",
                    "        cod:      ->(total) { 0 },",
                    "      }",
                    "      puts biaya.fetch(:ewallet).call(150_000)",
                    "  3. Hasilnya 3000. Metode baru cukup ditambah satu baris di hash, tanpa",
                    "     menyentuh kode yang memanggilnya.",
                    "  4. Periksa metode yang belum terdaftar. biaya[:pulsa] memberi nil, lalu",
                    "     .call pada nil gagal dengan NoMethodError. fetch langsung menyebut",
                    "     kunci yang hilang lewat KeyError.",
                ]
            },
        ],
    },
    {
        "title": "7. Enumerable: Kekuatan Sesungguhnya",
        "sections": [
            {
                "body": [
                    "Enumerable adalah module yang memberi puluhan method kepada apa pun",
                    "yang punya method each. Module itu kumpulan method yang bisa ditempel",
                    "ke class lain. Cara kerjanya dibahas di materi Pewarisan, Module &",
                    "Mixin. Array, Hash, Range, Set, dan Enumerator semuanya dapat method",
                    "dari Enumerable.",
                    "",
                    "Pola desain ini layak dipahami: kamu cukup menulis satu method, yaitu",
                    "each, lalu dapat sekitar enam puluh method lain secara gratis.",
                    "",
                    "Untuk mengubah elemen:",
                    "",
                    "  map / collect          ubah tiap elemen",
                    "  flat_map               ubah lalu ratakan",
                    "  each_with_index        bawa indeksnya",
                    "  each_with_object(x)    bawa wadah",
                    "  each_slice(3)          potong per 3",
                    "  each_cons(2)           jendela geser 2",
                    "  zip(lain)              pasangkan",
                    "  chunk_while { }        kelompokkan yang berurutan",
                    "",
                    "Untuk menyaring:",
                    "",
                    "  select / filter        ambil yang cocok",
                    "  reject                 buang yang cocok",
                    "  find / detect          yang pertama cocok",
                    "  filter_map             saring dan ubah sekaligus",
                    "  take(3) / drop(3)",
                    "  take_while / drop_while",
                    "  grep(/pola/)           saring dengan ===",
                    "  uniq / compact",
                    "",
                    "Untuk meringkas jadi satu hasil:",
                    "",
                    "  reduce / inject        lipat jadi satu nilai",
                    "  sum / count / tally",
                    "  min / max / minmax",
                    "  min_by / max_by / sort_by",
                    "  group_by               kelompokkan jadi Hash",
                    "  partition              pecah jadi dua: cocok & tidak",
                    "  all? / any? / none? / one?",
                    "  first(n) / include?",
                    "",
                    "Dua nama yang dipisah garis miring, seperti map / collect, adalah dua",
                    "nama untuk method yang sama. Beberapa yang mungkin belum kebayang:",
                    "  - each_slice(3) memotong elemen jadi kelompok isi tiga. each_cons(2)",
                    "    mengambil dua elemen bersebelahan sambil bergeser: [1, 2], lalu",
                    "    [2, 3], lalu [3, 4].",
                    "  - zip memasangkan elemen dua koleksi berdasarkan posisinya.",
                    "  - take_while mengambil elemen dari depan selama syaratnya terpenuhi,",
                    "    lalu berhenti. drop_while kebalikannya.",
                    "  - partition memecah elemen jadi dua array, yang cocok dan yang",
                    "    nggak.",
                    "  - one? bertanya apakah tepat satu elemen yang cocok.",
                    "",
                    "tally (ada sejak Ruby 2.7) menghitung berapa kali tiap nilai muncul,",
                    "cukup dengan satu panggilan. Idiom Hash.new(0) dari materi Array & Hash",
                    "jadi nggak perlu lagi:",
                    "",
                    "  kata.tally    # => {\"kucing\" => 3, \"ikan\" => 2, ...}",
                    "",
                    "Tulisan # => di contoh seperti itu artinya \"hasilnya adalah\".",
                    "",
                    "reduce layak dipahami, karena banyak method lain dibangun dari",
                    "gagasannya. reduce melipat semua elemen jadi satu nilai. Dia membawa",
                    "sebuah total, lalu menggabungkan total itu dengan tiap elemen secara",
                    "bergiliran:",
                    "",
                    "  [1,2,3].reduce(0) { |total, x| total + x }   6",
                    "  [1,2,3].reduce(:+)                           6",
                    "  [1,2,3].sum                                  6",
                    "",
                    "Di baris pertama, total mulai dari 0, lalu jadi 1, 3, dan akhirnya 6.",
                    "reduce(:+) adalah bentuk singkat yang memanggil + di tiap langkah.",
                    "",
                    "lazy berguna untuk deret yang besar atau tak terbatas. Dengan .lazy,",
                    "rantai method cuma menghitung elemen yang memang diminta:",
                    "",
                    "  (1..Float::INFINITY).lazy",
                    "      .map { |x| x * x }",
                    "      .select { |x| x % 3 == 0 }",
                    "      .first(5)",
                    "",
                    "Float::INFINITY artinya tak terhingga, jadi rentang itu nggak punya",
                    "ujung.",
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
                    "Struct.new(:nama, :kelas, :nilai) membuat class baru dalam satu baris.",
                    "Class itu langsung punya tiga atribut, constructor (method pembuat",
                    "objek yang dipanggil lewat Murid.new), perbandingan == yang melihat",
                    "isinya, dan to_s. Mirip record di C# dan data class di Kotlin. Struct",
                    "dibahas lagi di materi Set, Struct & Data.",
                    "",
                    "Baris yang diawali titik, seperti .sort_by di contoh, adalah lanjutan",
                    "baris sebelumnya. Dengan cara ini rantai yang panjang bisa ditulis satu",
                    "langkah per baris.",
                    "",
                    "lulus, ulang = data.partition { ... } mengisi dua variabel sekaligus.",
                    "Array pertama hasil partition masuk ke lulus, array kedua ke ulang.",
                    "",
                    "Bagian lazy menjalankan rantai pada deret tak terbatas. Tanpa .lazy,",
                    "map pada rentang tanpa ujung itu bakal jalan terus selamanya, dan",
                    "programnya menggantung. Dengan .lazy, rantainya berhenti begitu",
                    "first(5) udah dapat lima hasil.",
                    "",
                    "data.sum(&:nilai) menggabungkan dua idiom: sum yang menerima blok, dan",
                    "symbol-to-proc. Hasilnya sama dengan data.map { |m| m.nilai }.sum,",
                    "tapi tanpa membuat array perantara.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Laporan \"produk terlaris minggu ini\" di dasbor toko online, rekap absensi",
                    "per kelas, dan total penjualan per kasir punya bentuk yang sama:",
                    "kelompokkan, ringkas, lalu urutkan. Di Ruby, laporan seperti itu biasanya",
                    "ditulis sebagai satu rantai Enumerable, satu langkah per baris, tanpa",
                    "variabel penampung di tengahnya.",
                    "",
                    "Kasus kecil: aplikasi kasir mencatat empat transaksi, yaitu Kopi 3 gelas,",
                    "Teh 5 gelas, Kopi 4 gelas, dan Roti 2 potong. Tampilkan dua produk",
                    "terlaris menurut jumlah yang terjual.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Bentuk datanya array berisi hash seperti { produk: \"Kopi\", jumlah: 3 }.",
                    "     Keluarannya dua pasangan produk dan totalnya.",
                    "  2. Pecah jadi langkah: kelompokkan per produk, jumlahkan tiap kelompok,",
                    "     urutkan dari yang terbesar, lalu ambil dua:",
                    "      terlaris = transaksi.group_by { |t| t[:produk] }",
                    "                          .transform_values { |a| a.sum { |t| t[:jumlah] } }",
                    "                          .sort_by { |produk, jumlah| [-jumlah, produk] }",
                    "                          .first(2)",
                    "  3. Hasilnya [[\"Kopi\", 7], [\"Teh\", 5]]. Kopi muncul dua kali di data,",
                    "     dan group_by yang menyatukannya.",
                    "  4. Periksa produk yang jumlahnya seri. sort_by nggak menjamin urutan",
                    "     elemen yang seri, jadi kunci [-jumlah, produk] mengurutkannya",
                    "     menurut abjad, dan laporannya selalu sama tiap kali dijalankan.",
                ]
            },
        ],
    },
    {
        "title": "8. Method & Argumen",
        "sections": [
            {
                "body": [
                    "Method adalah kumpulan perintah yang diberi nama, supaya bisa dipanggil",
                    "berulang kali. Bentuknya:",
                    "",
                    "  def sapa(nama)",
                    "    \"Halo, #{nama}!\"",
                    "  end",
                    "",
                    "Method mengembalikan nilai ekspresi terakhir yang dijalankan. Jadi",
                    "sapa(\"Andi\") mengembalikan \"Halo, Andi!\" tanpa perlu menulis return.",
                    "return tetap ada, tapi cuma dipakai untuk keluar lebih awal dari",
                    "method. Menulis return di baris terakhir dianggap berlebihan oleh",
                    "programmer Ruby.",
                    "",
                    "Nilai yang dikirim waktu memanggil method disebut argumen. Nama yang",
                    "menampungnya di definisi method disebut parameter. Ada empat jenis",
                    "argumen, dan Ruby punya semuanya:",
                    "",
                    "  Posisional, diisi menurut urutannya",
                    "    def f(a, b)",
                    "",
                    "  Bawaan, punya nilai cadangan kalau nggak diisi",
                    "    def f(a, b = 10)",
                    "",
                    "  Berkunci (keyword), diisi lewat namanya",
                    "    def f(nama:, umur: 0)",
                    "    f(nama: \"Andi\")          umur pakai bawaannya",
                    "",
                    "  Bebas jumlahnya",
                    "    def f(*angka)            kumpulkan jadi array",
                    "    def f(**opsi)            kumpulkan jadi hash",
                    "    def f(&blok)             tangkap bloknya",
                    "",
                    "Argumen berkunci tanpa nilai bawaan, seperti nama: di atas, wajib",
                    "diisi. Fitur ini berguna karena pemanggilannya jadi menjelaskan dirinya",
                    "sendiri, dan urutannya bebas. Bandingkan dua baris ini:",
                    "",
                    "  gambar(tebal: true, miring: false)",
                    "  gambar(true, false)",
                    "",
                    "Baris pertama langsung terbaca. Di baris kedua, kamu harus membuka",
                    "definisi method-nya dulu untuk tahu true yang mana artinya apa.",
                    "",
                    "Operator splat, yaitu tanda * dan ** di depan nama, membongkar koleksi",
                    "jadi argumen satu per satu:",
                    "",
                    "  a = [1, 2, 3]",
                    "  f(*a)             sama dengan f(1, 2, 3)",
                    "  h = { x: 1 }",
                    "  g(**h)            sama dengan g(x: 1)",
                    "",
                    "Nama method boleh diakhiri tanda baca, dan tanda baca itu memberi tahu",
                    "banyak hal tentang method-nya:",
                    "",
                    "  kosong?      kembalikan true/false",
                    "  simpan!      berbahaya: mengubah objek atau melempar",
                    "  nama=        setter, dipanggil sebagai obj.nama = x",
                    "  <=> == []  +  semua operator adalah method biasa",
                    "",
                    "Setter adalah method untuk mengisi sebuah nilai. <=> adalah operator",
                    "pembanding yang biasa disebut spaceship. Hasilnya -1 kalau sisi kiri",
                    "lebih kecil, 0 kalau sama, dan 1 kalau sisi kiri lebih besar.",
                    "",
                    "Karena operator adalah method biasa, kamu bisa mendefinisikannya untuk",
                    "class buatanmu sendiri:",
                    "",
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
                    "  ============REKAP=============",
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
                    "Panggilan laporan pertama memakai semua jenis argumen sekaligus. Teks",
                    "pertama mengisi judul, lalu tiga teks sesudahnya ditampung *baris jadi",
                    "array. pemisah dan lebar adalah argumen berkunci. tanggal dan kasir",
                    "nggak punya parameter dengan nama itu, jadi keduanya masuk ke **opsi.",
                    "Tanda ... di keluaran menandai baris yang dilewati, yaitu hasil",
                    "panggilan laporan yang kedua.",
                    "",
                    "buat_akun(nama: \"Cici\") ditolak dengan ArgumentError karena email wajib",
                    "diisi. Pesan error-nya langsung menyebut kunci yang kurang.",
                    "",
                    "Class Uang menunjukkan dua hal sekaligus.",
                    "",
                    "Pertama, operator adalah method. Dengan mendefinisikan + dan -, objek",
                    "Uang bisa dijumlah dan dikurangi dengan tanda yang sama seperti angka.",
                    "",
                    "Kedua, include Comparable ditambah satu method <=> memberi tujuh method",
                    "sekaligus: <, >, <=, >=, ==, between?, dan clamp. Method <=> itu juga",
                    "yang dipakai .max, .min, dan .sort, jadi ketiganya ikut bekerja pada",
                    "array berisi objek Uang. Comparable dibahas lagi di materi Pewarisan,",
                    "Module & Mixin.",
                    "",
                    "to_s memberi titik pemisah ribuan dengan cara membalik angkanya,",
                    "memotongnya per tiga digit, menyambungnya pakai titik, lalu membaliknya",
                    "lagi.",
                    "",
                    "def akar(*n) = ... memakai endless method (ada sejak Ruby 3.0), yaitu",
                    "method satu ekspresi yang ditulis pakai tanda sama dengan, tanpa end.",
                    "Cocok untuk getter, yaitu method yang cuma mengembalikan sebuah nilai,",
                    "dan untuk perhitungan pendek. Satu pengecualian: setter seperti nama=",
                    "nggak boleh ditulis sebagai endless method. Ruby menolaknya dengan",
                    "SyntaxError.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Method di aplikasi sungguhan sering dipanggil dari banyak tempat dengan",
                    "kebutuhan yang beda-beda. Satu kasir menghitung total dua barang, kasir",
                    "lain menghitung lima barang dengan potongan member. Satu method yang",
                    "menerima jumlah argumen bebas plus pilihan berkunci bisa melayani",
                    "semuanya, tanpa method total_dua_barang dan total_dengan_diskon yang",
                    "ditulis terpisah.",
                    "",
                    "Kasus kecil: kasir butuh total untuk tiga barang seharga Rp12.000,",
                    "Rp8.500, dan Rp30.000, kadang dengan diskon member 10%.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Masukannya harga sebanyak apa pun, ditambah diskon yang boleh nggak",
                    "     diisi. Keluarannya satu angka.",
                    "  2. Tampung harganya dengan *harga, dan jadikan diskon argumen berkunci",
                    "     dengan bawaan 0. Kalau diskon dibuat posisional, pembaca",
                    "     total(12_000, 8_500, 10) nggak tahu angka 10 itu harga atau persen.",
                    "  3. Biarkan baris terakhir jadi nilai kembaliannya, tanpa return:",
                    "      def total(*harga, diskon: 0)",
                    "        jumlah = harga.sum",
                    "        jumlah - jumlah * diskon / 100",
                    "      end",
                    "      total(12_000, 8_500, 30_000)              # => 50500",
                    "      total(12_000, 8_500, 30_000, diskon: 10)  # => 45450",
                    "  4. Periksa keranjang yang sudah berbentuk array. total(keranjang)",
                    "     mengirim array itu sebagai satu harga dan gagal dengan TypeError.",
                    "     Bongkar dulu dengan splat, yaitu total(*keranjang).",
                ]
            },
        ],
    },
    {
        "title": "9. Class & Objek",
        "sections": [
            {
                "body": [
                    "Class adalah cetakan untuk membuat objek. Satu class Murid bisa dipakai",
                    "untuk membuat banyak objek murid, masing-masing dengan nama dan nilainya",
                    "sendiri:",
                    "",
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
                    "initialize adalah constructor, yaitu method yang menyiapkan objek baru.",
                    "Method ini dipanggil otomatis oleh .new. Namanya memang initialize,",
                    "bukan new. new sendiri adalah method milik class yang membuat objeknya,",
                    "lalu memanggil initialize.",
                    "",
                    "@nama adalah variabel instance, yaitu variabel milik satu objek. Tiap",
                    "objek Murid punya @nama-nya sendiri. Variabel instance otomatis privat:",
                    "dari luar objek, isinya cuma bisa dibaca lewat method. Kalau dibaca",
                    "sebelum diisi, hasilnya nil dan nggak ada error.",
                    "",
                    "Menulis method pembaca untuk tiap variabel itu membosankan. Ruby punya",
                    "attr untuk membuat getter (pembaca) dan setter (pengisi) secara",
                    "otomatis:",
                    "",
                    "  attr_reader :nama          hanya baca",
                    "  attr_writer :nilai         hanya tulis",
                    "  attr_accessor :nilai       keduanya",
                    "",
                    "Satu baris attr_reader :nama menggantikan tiga baris ini:",
                    "",
                    "  def nama",
                    "    @nama",
                    "  end",
                    "",
                    "Visibilitas menentukan siapa yang boleh memanggil sebuah method:",
                    "",
                    "  public      bawaan",
                    "  private     hanya dari dalam objek yang sama",
                    "  protected   boleh dari objek lain berkelas sama",
                    "",
                    "public artinya boleh dipanggil dari mana aja. Method yang nggak diberi",
                    "tanda apa pun otomatis public. protected boleh dipanggil lewat objek",
                    "lain, asal pemanggilnya ada di dalam class yang sama atau turunannya.",
                    "",
                    "Cara membuat method privat:",
                    "",
                    "  private",
                    "  def rahasia",
                    "    ...",
                    "  end",
                    "",
                    "Semua method yang ditulis sesudah kata private jadi privat. Bisa juga",
                    "per method, dengan menulis private def rahasia ... end. Bentuk ini",
                    "sudah bisa sejak Ruby 2.1. Sejak Ruby 3.0, private attr_reader :nama",
                    "juga bisa.",
                    "",
                    "Aturan khas Ruby: method privat nggak bisa dipanggil lewat objek lain,",
                    "bahkan objek dari class yang sama. obj.rahasia dari luar class, atau",
                    "lain.rahasia dari dalam class, sama-sama ditolak dengan NoMethodError.",
                    "Memanggilnya lewat self, yaitu self.rahasia, boleh sejak Ruby 2.7.",
                    "",
                    "Setter malah wajib dipanggil lewat self. Tulis self.nilai = x, karena",
                    "tanpa self., Ruby mengira nilai = x membuat variabel lokal baru bernama",
                    "nilai.",
                    "",
                    "Method class, yang di bahasa lain disebut method statis, ditulis dengan",
                    "self. di depan namanya. Method ini dipanggil lewat class-nya, misalnya",
                    "Murid.buat(...), bukan lewat objek:",
                    "",
                    "  def self.buat(...)",
                    "    new(...)",
                    "  end",
                    "",
                    "Ada dua method yang menentukan bagaimana objekmu tampil sebagai teks:",
                    "",
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
                    "Beberapa hal dari contoh itu:",
                    "  - puts a memanggil to_s, sedangkan p a memanggil inspect. Yang satu",
                    "    untuk pengguna, yang lain untuk kamu saat nyari bug.",
                    "  - format(\"AC%04d\", @@urutan) menulis nomor sebagai angka empat digit",
                    "    dengan nol di depan. Angka 1 jadi AC0001.",
                    "  - setor mengembalikan self, yaitu objek itu sendiri, sehingga",
                    "    panggilannya bisa dirangkai: a.setor(100).setor(200). Pola ini",
                    "    disebut fluent interface dan lazim di Ruby.",
                    "  - include Comparable ditambah satu <=> memberi semua operator",
                    "    perbandingan, seperti a > b. [a, b].max juga bekerja karena memakai",
                    "    <=> yang sama.",
                    "  - rupiah dideklarasikan privat. a.rupiah dari luar melempar",
                    "    NoMethodError, padahal to_s di dalam class boleh memanggilnya.",
                    "",
                    "Hati-hati dengan @@urutan. Itu variabel class, yaitu variabel yang cuma",
                    "ada satu untuk seluruh class dan dipakai bersama oleh semua objeknya.",
                    "Di sini variabel itu dipakai untuk penomoran otomatis. Masalahnya,",
                    "variabel class juga dibagi dengan semua turunan class itu, sehingga",
                    "turunannya bisa mengacaukan nilai milik induknya. Turunan class dibahas",
                    "di materi Pewarisan, Module & Mixin. Untuk kode baru, @urutan yang",
                    "ditulis di level class (disebut class instance variable) lebih aman.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aplikasi sungguhan penuh class yang mewakili benda nyata, seperti",
                    "Pesanan, Siswa, Rekening, dan Antrean. Di Rails, tiap tabel database",
                    "biasanya punya satu class model. Tiap objek memegang datanya sendiri di",
                    "variabel instance, dan cuma memperlihatkan method yang memang boleh",
                    "dipakai dari luar.",
                    "",
                    "Kasus kecil: puskesmas punya dua loket, A untuk umum dan B untuk lansia.",
                    "Tiap loket memberi nomor antrean sendiri (A-001, A-002, lalu B-001), dan",
                    "memanggil pasien sesuai urutan datang.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tentukan apa yang dipegang tiap loket: kode loket, nomor terakhir,",
                    "     dan daftar yang menunggu. Ketiganya jadi variabel instance yang",
                    "     diisi di initialize.",
                    "  2. Tentukan tindakannya. ambil memberi nomor baru, dan panggil",
                    "     mengambil nomor paling depan dengan shift:",
                    "      def ambil",
                    "        @terakhir += 1",
                    "        nomor = format(\"%s-%03d\", @kode, @terakhir)",
                    "        @menunggu << nomor",
                    "        nomor",
                    "      end",
                    "  3. Putuskan apa yang boleh dilihat dari luar. attr_reader :kode cukup.",
                    "     Daftar yang menunggu nggak diberi setter, jadi nggak bisa",
                    "     dikosongkan sembarangan dari luar class.",
                    "  4. Uji dua objek sekaligus. Antrean.new(\"A\") dan Antrean.new(\"B\") punya",
                    "     @terakhir masing-masing, jadi nomor B mulai dari B-001. Coba juga",
                    "     panggil saat antrean kosong: shift pada array kosong memberi nil,",
                    "     dan layar perlu menampilkan pesan untuk itu.",
                    "",
                    "Jebakan: kalau penghitungnya ditulis @@terakhir, dua loket berbagi satu",
                    "angka, dan sesudah A-001 loket B langsung memberi B-002.",
                ]
            },
        ],
    },
    {
        "title": "10. Pewarisan, Module & Mixin",
        "sections": [
            {
                "body": [
                    "Pewarisan artinya sebuah class mewarisi semua method dari class lain,",
                    "yang disebut induknya. Di Ruby, satu class cuma boleh punya satu induk:",
                    "",
                    "  class Kucing < Hewan",
                    "    def initialize(nama)",
                    "      super(nama, \"mamalia\")",
                    "    end",
                    "",
                    "    def suara = \"Meong\"",
                    "  end",
                    "",
                    "Tanda < dibaca \"turunan dari\". Jadi Kucing adalah turunan Hewan, dan",
                    "Kucing otomatis punya semua method milik Hewan.",
                    "",
                    "super memanggil method bernama sama milik induknya. Ada tiga cara",
                    "menulisnya, dan dua yang pertama sering tertukar:",
                    "",
                    "  super         teruskan semua argumen apa adanya",
                    "  super()       panggil tanpa argumen sama sekali",
                    "  super(a, b)   dengan argumen tertentu",
                    "",
                    "Jebakan: super tanpa kurung tetap membawa argumen. super polos",
                    "meneruskan semua argumen yang diterima method itu ke induknya. Kalau",
                    "induknya minta jumlah argumen yang berbeda, hasilnya ArgumentError.",
                    "",
                    "Class yang nggak menyebut induknya otomatis mewarisi Object, dan Object",
                    "sendiri mewarisi BasicObject. Dari Object datang method yang dimiliki",
                    "setiap objek, seperti class, inspect, respond_to?, dan frozen?.",
                    "Tepatnya, method-method itu ditulis di module Kernel yang ditempel ke",
                    "Object.",
                    "",
                    "Module adalah kumpulan method dan konstanta yang bisa dipakai bersama.",
                    "Module menjawab dua kebutuhan sekaligus.",
                    "",
                    "Kebutuhan pertama adalah namespace, yaitu wadah nama supaya nama yang",
                    "sama nggak bertabrakan. Class Produk di dalam module Toko dipanggil",
                    "lewat Toko::Produk:",
                    "",
                    "  module Toko",
                    "    class Produk; end",
                    "  end",
                    "  Toko::Produk.new",
                    "",
                    "Kebutuhan kedua adalah mixin, yaitu cara berbagi perilaku tanpa",
                    "pewarisan. Method di dalam module ditempelkan ke sebuah class dengan",
                    "include:",
                    "",
                    "  module BisaDicatat",
                    "    def catat(pesan) = (@catatan ||= []) << pesan",
                    "  end",
                    "",
                    "  class Pesanan",
                    "    include BisaDicatat",
                    "  end",
                    "",
                    "Sekarang setiap objek Pesanan punya method catat. Tanda ||= di situ",
                    "artinya \"isi kalau masih kosong\". @catatan diisi array kosong kalau",
                    "belum pernah diisi, lalu pesan ditambahkan ke array itu.",
                    "",
                    "Ada tiga cara menyisipkan module, dan hasilnya berbeda:",
                    "",
                    "  include Modul   method jadi method instance",
                    "  extend Modul    method jadi method class",
                    "  prepend Modul   disisipkan di depan, menimpa method",
                    "                  class-nya sendiri",
                    "",
                    "include membuat method module bisa dipanggil lewat objek. extend",
                    "membuatnya bisa dipanggil lewat class itu sendiri. prepend menaruh",
                    "module di depan class dalam urutan pencarian method, jadi method module",
                    "menang atas method class yang namanya sama.",
                    "",
                    "Dengan cara ini Ruby menggantikan pewarisan berganda, yaitu satu class",
                    "yang punya banyak induk. Cara ini lebih aman: urutan pencarian method",
                    "selalu lurus satu jalur, dan bisa kamu lihat dengan Kelas.ancestors.",
                    "",
                    "Dua module dari pustaka standar yang wajib kamu kenal:",
                    "",
                    "  Comparable  butuh <=>, memberi < > <= >= == between?",
                    "  Enumerable  butuh each, memberi map select reduce dan",
                    "              puluhan lainnya",
                    "",
                    "Polanya sama dengan yang kamu lihat di materi Method & Argumen dan",
                    "materi Enumerable: tulis satu method, dapat banyak.",
                ]
            },
            {
                "heading": "Mixin, Enumerable, dan ancestors",
                "code": """module BisaDiringkas
  def ringkas = format("%-16s%8.2f", nama, luas)
end

module Berwarna
  def warna = @warna || "hitam"

  # Setter nggak boleh ditulis bentuk satu baris (def x=(v) = ...):
  # Ruby 3 menolaknya dengan SyntaxError.
  def warna=(w)
    @warna = w
  end
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
                    "ancestors menunjukkan urutan pencarian method. Waktu sebuah method",
                    "dipanggil, Ruby mencarinya dari atas daftar itu: Lingkaran dulu, lalu",
                    "Bangun, lalu module yang di-include, lalu Object. Module yang terakhir",
                    "di-include ada lebih dulu, makanya Berwarna muncul sebelum",
                    "BisaDiringkas. Contoh itu cuma mengambil lima yang pertama. Daftar",
                    "lengkapnya masih berlanjut dengan Kernel dan BasicObject.",
                    "",
                    "Rantai yang sama membuat super di Lingkaran#ringkas menemukan versi",
                    "milik module BisaDiringkas, walaupun module itu di-include di class",
                    "induknya. Tulisan Lingkaran#ringkas artinya method ringkas milik",
                    "Lingkaran.",
                    "",
                    "Class Kelas menunjukkan gunanya Enumerable. Cukup dengan menulis satu",
                    "each, class itu langsung punya count, first, map, select, sort_by, sum,",
                    "group_by, dan puluhan method lain. Nggak satu pun ditulis di class itu.",
                    "",
                    "NotImplementedError adalah cara Ruby menandai method abstrak, yaitu",
                    "method yang wajib ditulis ulang oleh turunannya. Ruby nggak punya kata",
                    "kunci abstract, jadi yang dipakai konvensi ini. NotImplementedError",
                    "bukan turunan StandardError, jadi rescue tanpa nama class nggak",
                    "menangkapnya. Karena itu contoh di atas perlu menulis rescue",
                    "NotImplementedError lengkap dengan namanya. Soal ini dibahas di materi",
                    "Exception & Penanganan Galat.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Pewarisan dan mixin dipakai setiap kali beberapa jenis benda punya",
                    "perilaku yang hampir sama. Di Rails, tiap model mewarisi ApplicationRecord",
                    "dan tiap controller mewarisi ApplicationController, jadi kemampuan",
                    "dasarnya datang dari induk. Perilaku yang dipakai bersama oleh banyak",
                    "class, misalnya mencatat riwayat, biasanya ditaruh di module lalu",
                    "di-include.",
                    "",
                    "Kasus kecil: toko online menjual barang fisik dan voucher digital. Barang",
                    "fisik kena ongkir Rp5.000 per kg, voucher digital tanpa ongkir. Halaman",
                    "checkout cuma mau memanggil total_bayar, tanpa peduli jenis barangnya.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Cari yang sama. Semua produk punya nama dan harga, dan total_bayar",
                    "     selalu harga ditambah ongkir. Taruh semua itu di class induk Produk.",
                    "  2. Cari yang beda, yaitu cuma cara menghitung ongkir. Induk menandainya",
                    "     sebagai method abstrak dengan NotImplementedError:",
                    "      class Produk",
                    "        attr_reader :nama, :harga",
                    "        def total_bayar = harga + ongkir",
                    "        def ongkir = raise(NotImplementedError, \"#{self.class} tanpa ongkir\")",
                    "      end",
                    "  3. Turunannya cuma menulis bagian yang beda. Fisik < Produk menulis",
                    "     def ongkir = berat * 5_000, dan Digital < Produk menulis",
                    "     def ongkir = 0. Buku seharga 80.000 dengan berat 2 kg jadi 90.000.",
                    "  4. Periksa jenis baru yang lupa menulis ongkir. total_bayar langsung",
                    "     gagal dengan NotImplementedError yang menyebut nama class-nya, jadi",
                    "     ongkir yang terlupa nggak pernah tercatat sebagai Rp0.",
                ]
            },
        ],
    },
    {
        "title": "11. Exception & Penanganan Galat",
        "sections": [
            {
                "body": [
                    "Exception adalah objek yang mewakili sebuah error, yang di materi ini",
                    "juga disebut galat. Begitu error terjadi, Ruby melempar exception, dan",
                    "program berhenti kecuali ada yang menangkapnya. Bentuk lengkap",
                    "penangkapnya:",
                    "",
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
                    "rescue menangkap exception dari class yang disebut, dan => e menyimpan",
                    "objek exception-nya ke variabel e. Pesannya bisa dibaca lewat",
                    "e.message. Kalau ada beberapa rescue, Ruby memakai yang pertama cocok,",
                    "jadi tulis yang paling spesifik di atas.",
                    "",
                    "Di dalam method, begin boleh dihilangkan. Badan method itu sendiri",
                    "sudah jadi bloknya:",
                    "",
                    "  def baca(path)",
                    "    File.read(path)",
                    "  rescue Errno::ENOENT",
                    "    \"\"",
                    "  end",
                    "",
                    "Errno::ENOENT adalah exception yang muncul kalau berkasnya nggak ada.",
                    "Di contoh itu, berkas yang nggak ada dianggap berisi teks kosong.",
                    "",
                    "Exception tersusun bertingkat. Tiap class exception adalah turunan",
                    "class di atasnya:",
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
                    "      └── IndexError -> KeyError, StopIteration",
                    "",
                    "Susunan itu penting karena satu aturan. rescue tanpa nama class cuma",
                    "menangkap StandardError dan turunannya, nggak semua Exception. Itu",
                    "disengaja, dan memang benar. Menangkap Exception ikut menelan Ctrl-C,",
                    "kehabisan memori, dan perintah exit, sehingga programmu nggak bisa",
                    "dihentikan.",
                    "",
                    "  rescue => e          BENAR (StandardError)",
                    "  rescue Exception     JANGAN",
                    "",
                    "Untuk melempar exception sendiri, pakai raise:",
                    "",
                    "  raise \"pesan\"                    -> RuntimeError",
                    "  raise ArgumentError, \"pesan\"",
                    "  raise ArgumentError.new(\"pesan\")",
                    "  raise                            lempar ulang yang sama",
                    "",
                    "raise polos yang ditulis di dalam rescue melempar ulang exception yang",
                    "sedang ditangani.",
                    "",
                    "retry menjalankan ulang blok begin dari awal. Ini berguna untuk koneksi",
                    "jaringan yang kadang gagal sesaat:",
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
                    "Timeout::Error muncul kalau sebuah proses melewati batas waktunya.",
                    "Sesudah tiga kali gagal, raise di baris terakhir melempar ulang",
                    "error-nya.",
                    "",
                    "Jebakan: tanpa penghitung seperti percobaan, retry jadi perulangan yang",
                    "nggak pernah berhenti.",
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
                    "SaldoKurangError adalah exception buatan sendiri. Class-nya turunan",
                    "StandardError, jadi rescue biasa bisa menangkapnya. raise",
                    "SaldoKurangError, jumlah - @saldo mengirim angka kekurangannya ke",
                    "initialize, lalu super(...) menyusun pesannya. Karena kurang disimpan",
                    "lewat attr_reader, bagian rescue bisa membaca e.kurang.",
                    "",
                    "rescue yang ditulis langsung di dalam blok do...end, seperti di each",
                    "tadi, sah sejak Ruby 2.6. Sebelumnya kamu butuh begin tersendiri di",
                    "dalam blok itu.",
                    "",
                    "e.cause berguna, tapi jarang diketahui orang. Waktu exception baru",
                    "dilempar di tengah penanganan exception lain, Ruby otomatis menyimpan",
                    "exception yang lama di cause. Di contoh terakhir, KonfigurasiError",
                    "dilempar di dalam rescue ArgumentError, jadi e.cause berisi",
                    "ArgumentError itu. Jejak penyebab aslinya nggak pernah hilang, dan kamu",
                    "nggak perlu meneruskannya manual seperti di PHP atau C#.",
                    "",
                    "Beberapa aturan yang sering dilanggar:",
                    "  - Jangan menulis rescue => e lalu nggak berbuat apa-apa. Programnya",
                    "    jalan terus dalam keadaan rusak, dan kamu nggak tahu apa yang",
                    "    salah.",
                    "  - Jangan menulis rescue Exception. Dia ikut menelan Ctrl-C dan",
                    "    kehabisan memori.",
                    "  - Jangan memakai exception untuk alur yang normal. find yang nggak",
                    "    menemukan apa-apa mengembalikan nil, dan itu bukan error.",
                    "  - Untuk method yang wajar kalau gagal, sediakan dua versi: simpan",
                    "    mengembalikan false, sedangkan simpan! melempar exception. Pola ini",
                    "    dipakai di seluruh Rails.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Program yang bicara dengan dunia luar selalu bisa gagal: server",
                    "pembayaran nggak menjawab, berkas belum ada, atau data dari cabang lain",
                    "rusak. Aplikasi kasir yang mengirim transaksi ke kantor pusat tiap malam",
                    "harus membedakan galat yang layak dicoba lagi dari galat yang perlu",
                    "dilaporkan. Programnya juga nggak boleh berhenti total gara-gara satu",
                    "kiriman gagal.",
                    "",
                    "Kasus kecil: koneksi ke server pusat kadang putus sesaat dan memunculkan",
                    "IOError. Kirim ulang paling banyak tiga kali. Kalau tetap gagal, simpan",
                    "transaksinya ke daftar tertunda supaya dikirim besok.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pisahkan jenis galatnya. IOError karena koneksi layak dicoba lagi.",
                    "     ArgumentError karena data rusak nggak akan sembuh dengan dicoba",
                    "     ulang, jadi biarkan galat itu lolos dan kelihatan.",
                    "  2. Pakai retry dengan penghitung yang dimulai dari percobaan = 0:",
                    "      begin",
                    "        percobaan += 1",
                    "        kirim_ke_pusat(transaksi)",
                    "      rescue IOError",
                    "        percobaan < 3 ? retry : tertunda << transaksi",
                    "      end",
                    "  3. Sesudah percobaan ketiga gagal, transaksinya masuk ke tertunda, dan",
                    "     program lanjut ke transaksi berikutnya.",
                    "  4. Uji dengan kirim_ke_pusat palsu, satu yang gagal dua kali lalu",
                    "     berhasil, satu lagi yang gagal terus. Yang pertama harus terkirim di",
                    "     percobaan ketiga, yang kedua harus berakhir di daftar tertunda.",
                ]
            },
        ],
    },
    {
        "title": "12. Berkas, JSON & Baris Perintah",
        "sections": [
            {
                "body": [
                    "Untuk berkas, Ruby punya cara singkat yang cukup satu baris:",
                    "",
                    "  File.read(path)                  seluruh isi",
                    "  File.readlines(path, chomp: true) tiap baris jadi elemen",
                    "  File.write(path, isi)            tulis (menimpa)",
                    "  File.exist?(path)  File.size(path)  File.delete(path)",
                    "",
                    "path adalah letak berkas, misalnya \"data/murid.csv\". chomp: true",
                    "membuang karakter baris baru di ujung tiap baris.",
                    "",
                    "Ada juga cara dengan blok. Cara ini selalu menutup berkasnya sesudah",
                    "blok selesai, sama seperti pola blok di materi Blok, Proc & Lambda:",
                    "",
                    "  File.open(path, \"w\") do |f|",
                    "    f.puts \"baris\"",
                    "  end",
                    "",
                    "  File.foreach(path) do |baris|",
                    "    ...            satu per satu, hemat memori",
                    "  end",
                    "",
                    "File.foreach membaca berkas baris demi baris, jadi berkas sebesar apa",
                    "pun nggak perlu dimuat ke memori sekaligus.",
                    "",
                    "Argumen kedua File.open adalah mode. \"r\" untuk membaca, \"w\" untuk",
                    "menulis, \"a\" untuk menambah di akhir berkas, dan \"r+\" untuk membaca",
                    "sekaligus menulis. Tambahkan \"b\" untuk berkas biner, misalnya gambar.",
                    "",
                    "Jebakan: mode \"w\" langsung mengosongkan berkasnya begitu dibuka, bahkan",
                    "sebelum kamu menulis apa pun. Kalau maksudmu menambah isi, pakai \"a\".",
                    "",
                    "Supaya path-nya benar di sistem operasi mana pun, pakai method berikut",
                    "dan jangan menyusun garis miringnya sendiri:",
                    "",
                    "  File.join(\"data\", \"murid.csv\")",
                    "  File.basename(p) / File.dirname(p) / File.extname(p)",
                    "  File.expand_path(p)",
                    "  Dir.glob(\"*.txt\") / Dir.mkdir / Dir.exist?",
                    "  Dir.tmpdir            butuh require \"tmpdir\"",
                    "  __dir__               folder berkas ini",
                    "",
                    "Untuk \"data/murid.csv\", basename memberi \"murid.csv\", dirname memberi",
                    "\"data\", dan extname memberi \".csv\". expand_path mengubahnya jadi path",
                    "lengkap dari akar. Dir.glob(\"*.txt\") mencari semua berkas yang namanya",
                    "berakhiran .txt. Dir.tmpdir memberi folder sementara milik sistem.",
                    "",
                    "JSON adalah format teks untuk bertukar data yang dipakai hampir semua",
                    "aplikasi web. Cara memakainya di Ruby:",
                    "",
                    "  require \"json\"",
                    "",
                    "  JSON.generate(data)         atau data.to_json",
                    "  JSON.pretty_generate(data)",
                    "  JSON.parse(teks)                     kunci String",
                    "  JSON.parse(teks, symbolize_names: true)  kunci Symbol",
                    "",
                    "require memuat pustaka yang belum aktif secara otomatis. pretty_generate",
                    "menulis JSON yang rapi dan berbaris-baris. Kalau kamu membaca JSON di",
                    "Ruby, symbolize_names: true hampir selalu yang kamu mau, karena kunci",
                    "Symbol memang kebiasaan di Ruby.",
                    "",
                    "CSV dulu termasuk pustaka standar. Sejak Ruby 3.4, CSV dipindah jadi",
                    "bundled gem, yaitu gem yang ikut dibagikan bersama Ruby tapi dikelola",
                    "sebagai paket terpisah. Gem adalah paket pustaka Ruby, dan materi Gem,",
                    "Bundler & Struktur Proyek membahasnya. Akibatnya, require \"csv\" bisa",
                    "gagal dengan LoadError sampai kamu memasangnya sendiri:",
                    "",
                    "  gem install csv          atau tambahkan ke Gemfile",
                    "  require \"csv\"",
                    "  CSV.foreach(path, headers: true) { |baris| ... }",
                    "  CSV.open(path, \"w\") { |csv| csv << [\"a\", \"b\"] }",
                    "",
                    "Hal yang sama terjadi pada beberapa pustaka lain, seperti abbrev,",
                    "base64, dan observer. Kalau sebuah require yang dulu jalan mendadak",
                    "gagal sesudah kamu naik ke versi Ruby yang lebih baru, ini penyebab",
                    "pertama yang perlu dicurigai.",
                    "",
                    "Untuk data berpemisah koma yang sederhana, split(\",\") udah cukup. Contoh",
                    "di bawah memakai cara itu supaya jalan di Ruby versi mana pun. Untuk",
                    "berkas CSV sungguhan, tetap pakai pustakanya. Kolom yang diapit tanda",
                    "kutip boleh berisi koma, dan split bakal memecahnya jadi dua.",
                    "",
                    "Untuk program yang dijalankan dari terminal, Ruby menyediakan:",
                    "",
                    "  ARGV        array argumen",
                    "  ARGF        gabungan berkas di ARGV, atau stdin",
                    "  $PROGRAM_NAME",
                    "  ENV[\"HOME\"]",
                    "  STDIN.gets / $stdin.read / gets",
                    "",
                    "Argumen di sini adalah kata-kata yang kamu tulis sesudah nama program,",
                    "misalnya data.txt pada ruby rapor.rb data.txt. stdin adalah masukan",
                    "standar, yaitu teks yang diketik ke program atau dialirkan dari",
                    "perintah lain. $PROGRAM_NAME berisi nama programnya, dan ENV berisi",
                    "variabel lingkungan seperti HOME.",
                    "",
                    "OptionParser, yang ada di pustaka standar, mengurus flag (seperti -v),",
                    "nilai, dan teks bantuan tanpa perlu satu gem pun. Contohnya ada di",
                    "materi Ruby untuk Skrip Sistem.",
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
                    "Baris judul, *isi = File.readlines(...) memecah hasilnya. Baris",
                    "pertama masuk ke judul, sisanya masuk ke isi sebagai array. Lalu",
                    "kunci.zip(...).to_h memasangkan tiap nama kolom dengan nilainya dan",
                    "mengubah pasangan itu jadi hash.",
                    "",
                    "Lihat \"nilai\": 88 di JSON-nya. Angka 88 ditulis tanpa kutip, jadi",
                    "tersimpan sebagai angka. Itu karena .to_i dipanggil di merge waktu",
                    "data CSV-nya dibaca. Tanpa .to_i, JSON-nya bakal berisi teks \"88\", dan",
                    "siapa pun yang memakainya nanti harus mengubahnya jadi angka lagi.",
                    "",
                    "File.foreach(teks).with_index(1) menelusuri baris demi baris sambil",
                    "menghitung mulai dari 1. with_index menerima angka awal, sedangkan",
                    "each_with_index selalu mulai dari 0.",
                    "",
                    ".chomp membuang karakter baris baru di ujung baris. Di contoh ini,",
                    "keluarannya tetap sama tanpa .chomp, karena puts nggak menambah baris",
                    "baru lagi kalau teksnya sudah diakhiri baris baru. Bedanya kelihatan",
                    "begitu kamu menempelkan sesuatu sesudah barisnya. Tanpa .chomp,",
                    "\"#{baris} (selesai)\" mencetak (selesai) di baris berikutnya. Cara lain",
                    "adalah File.readlines(path, chomp: true).",
                    "",
                    "Ukuran 32 byte itu sudah termasuk karakter baris baru di ujung tiap",
                    "baris.",
                    "",
                    "Kalau kamu memakai File.open, pakai bentuk blok File.open(path) do |f|",
                    "... end. Bentuk tanpa blok menuntut kamu memanggil .close sendiri, dan",
                    "satu exception di tengah jalan bikin berkasnya nggak pernah ditutup.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Banyak pekerjaan kantor berupa memindahkan data dari satu bentuk ke",
                    "bentuk lain: catatan mesin absensi jadi rekap, ekspor penjualan jadi",
                    "laporan, atau data satu aplikasi jadi JSON untuk aplikasi lain. Karena",
                    "hampir semua aplikasi web bertukar data dalam JSON, membaca berkas teks",
                    "lalu menulis JSON adalah tugas yang wajar kamu temui di tempat PKL.",
                    "",
                    "Kasus kecil: mesin absensi menyimpan absen.txt dengan satu baris per",
                    "siswa, seperti ini:",
                    "",
                    "  Andi,hadir",
                    "  Budi,sakit",
                    "  Cici,hadir",
                    "  Dedi,alpa",
                    "",
                    "Aplikasi sekolah minta rekapnya sebagai JSON berisi jumlah siswa per",
                    "status.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Masukannya baris berbentuk nama,status. Keluarannya JSON seperti",
                    "     {\"hadir\":2,\"sakit\":1,\"alpa\":1}.",
                    "  2. Baca semua baris dengan readlines dan chomp: true, ambil bagian",
                    "     sesudah koma, lalu hitung dengan tally:",
                    "      require \"json\"",
                    "      baris = File.readlines(\"absen.txt\", chomp: true).reject(&:empty?)",
                    "      rekap = baris.map { |b| b.split(\",\").last }.tally",
                    "      File.write(\"rekap.json\", JSON.generate(rekap))",
                    "  3. Buka rekap.json dan cocokkan isinya dengan hitungan tangan.",
                    "  4. Periksa baris kosong di ujung berkas, yang sering terbawa dari",
                    "     editor. Tanpa reject(&:empty?), baris itu menghasilkan status nil,",
                    "     dan JSON-nya mendapat kunci aneh \"\" yang bernilai 1.",
                    "",
                    "Jebakan: File.write menimpa isi berkas lama. Kalau rekap tiap hari",
                    "ditulis ke rekap.json yang sama, rekap kemarin hilang, jadi sisipkan",
                    "tanggal di namanya, misalnya rekap-2026-10-17.json.",
                ]
            },
        ],
    },
    {
        "title": "13. Gem, Bundler & Struktur Proyek",
        "sections": [
            {
                "body": [
                    "Gem adalah paket pustaka Ruby, yaitu kode buatan orang lain yang bisa",
                    "kamu pasang dan pakai. RubyGems adalah program pengelolanya, dan",
                    "program ini udah ikut terpasang bersama Ruby.",
                    "",
                    "  gem install rspec",
                    "  gem list",
                    "  gem which json",
                    "",
                    "gem install memasang sebuah gem, gem list menampilkan gem yang",
                    "terpasang, dan gem which menunjukkan letak berkas sebuah pustaka.",
                    "",
                    "Sehari-hari, yang lebih sering dipakai adalah Bundler. Bundler",
                    "mengunci versi gem untuk satu proyek, supaya semua orang yang",
                    "mengerjakannya memakai versi yang sama:",
                    "",
                    "  bundle init             buat Gemfile",
                    "  bundle add rspec        tambah dependensi",
                    "  bundle install          pasang sesuai Gemfile.lock",
                    "  bundle update           perbarui",
                    "  bundle exec rspec       jalankan dengan versi terkunci",
                    "",
                    "Dependensi artinya pustaka lain yang dibutuhkan proyekmu. Daftarnya",
                    "ditulis di berkas Gemfile, sedangkan versi persis yang terpasang",
                    "dicatat Bundler di Gemfile.lock.",
                    "",
                    "bundle exec itu penting. Tanpa bundle exec, kamu bisa menjalankan versi",
                    "gem yang beda dari yang tercatat di Gemfile.lock, dan hasilnya bisa",
                    "beda di komputer lain.",
                    "",
                    "Contoh isi Gemfile:",
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
                    "source menyebut tempat gem diunduh, dan ruby menyebut versi Ruby yang",
                    "dibutuhkan. Gem di dalam group :development, :test cuma dipakai waktu",
                    "mengembangkan dan menguji, nggak di aplikasi yang sudah jalan untuk",
                    "pengguna. require: false artinya gem itu dipasang, tapi nggak dimuat",
                    "otomatis.",
                    "",
                    "Tanda ~> disebut pessimistic operator. ~> 4.0 menerima versi 4.x apa",
                    "pun, tapi nggak mau 5.0. ~> 4.0.1 lebih ketat: mulai 4.0.1, dan cuma",
                    "di keluarga 4.0.x.",
                    "",
                    "Untuk aplikasi, Gemfile.lock wajib ikut disimpan di git, alat pencatat",
                    "riwayat kode. Berkas itulah yang membuat pemasangan hari ini dan enam",
                    "bulan lagi menghasilkan versi yang sama persis.",
                    "",
                    "Ada dua cara memuat kode dari berkas lain:",
                    "",
                    "  require \"json\"              pustaka standar atau gem",
                    "  require_relative \"murid\"    berkas di proyek ini",
                    "",
                    "Bedanya penting. require mencari di daftar folder pustaka dan gem.",
                    "Untuk berkasmu sendiri, require butuh path lengkap, atau path yang",
                    "dihitung dari folder tempat kamu menjalankan perintah. require \"./murid\"",
                    "misalnya cuma jalan kalau kamu menjalankan programnya dari folder yang",
                    "sama dengan murid.rb. require_relative dihitung dari letak berkas yang",
                    "memanggilnya, jadi tetap benar dari folder mana pun. Untuk berkas di",
                    "proyekmu sendiri, hampir selalu pakai require_relative.",
                    "",
                    "Keduanya cuma memuat sekali. Memanggil require dua kali untuk berkas",
                    "yang sama nggak menjalankan berkas itu dua kali.",
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
                    "Konvensi yang dipatuhi hampir semua proyek Ruby:",
                    "",
                    "  lib/nama_proyek.rb      memuat semua yang lain",
                    "  lib/nama_proyek/*.rb    satu class per berkas",
                    "  spec/ atau test/        tes",
                    "  bin/ atau exe/          skrip eksekutabel",
                    "",
                    "Nama berkas ditulis snake_case, nama class ditulis PascalCase. Berkas",
                    "lib/proyekku/murid_baru.rb berisi Proyekku::MuridBaru. Kesepakatan ini",
                    "yang membuat autoloader di Rails bisa menemukan berkas dari nama",
                    "class-nya. Autoloader adalah bagian Rails yang memuat berkas secara",
                    "otomatis begitu sebuah class dipakai.",
                    "",
                    "Rake adalah make-nya Ruby. make adalah alat lama untuk menjalankan",
                    "tugas otomatis, seperti menguji atau mengompilasi, yang ditulis di satu",
                    "berkas. Di Ruby, berkas itu bernama Rakefile. rake -T menampilkan tugas",
                    "yang punya keterangan desc beserta keterangannya, dan rake tanpa",
                    "argumen menjalankan tugas default. Di contoh Rakefile tadi, rake ci",
                    "menjalankan spec dulu, lalu lint.",
                    "",
                    "RuboCop adalah linter sekaligus perapi kode. Linter adalah alat yang",
                    "membaca kodemu tanpa menjalankannya, lalu menandai kebiasaan buruk.",
                    "RuboCop memaksa gaya penulisan yang seragam dan menangkap banyak",
                    "kebiasaan buruk:",
                    "",
                    "  rubocop                  periksa",
                    "  rubocop -a               perbaiki yang aman",
                    "  rubocop -A               perbaiki semuanya (hati-hati)",
                    "  rubocop --auto-gen-config  buat daftar pengecualian",
                    "                             untuk proyek yang sudah ada",
                    "",
                    "Hati-hati dengan -A. Opsi itu ikut menerapkan perbaikan yang bisa",
                    "mengubah perilaku program, jadi periksa hasilnya dan jalankan tesmu",
                    "sesudahnya.",
                    "",
                    "--auto-gen-config berguna waktu memasang RuboCop di proyek lama. Tanpa",
                    "opsi itu, kamu langsung dapat ribuan keluhan sekaligus. Dengan opsi",
                    "itu, keadaan sekarang dicatat sebagai pengecualian, sehingga cuma kode",
                    "baru yang diperiksa.",
                    "",
                    "Gem yang sering dipakai:",
                    "",
                    "  rspec / minitest     pengujian",
                    "  rubocop              gaya dan kualitas",
                    "  pry / debug          debugger interaktif",
                    "  sinatra / rails      web",
                    "  sequel / activerecord  database",
                    "  httparty / faraday   klien HTTP",
                    "",
                    "Debugger adalah alat untuk menghentikan program di tengah jalan lalu",
                    "memeriksa isinya. Klien HTTP dipakai untuk mengambil data dari",
                    "alamat web.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Keluhan \"di laptopku jalan, di laptopnya error\" sering muncul di proyek",
                    "tim. Bundler dan Gemfile.lock ada untuk mencegahnya: tiap orang, termasuk",
                    "server, memasang versi gem yang sama persis. Di proyek Ruby sungguhan,",
                    "Gemfile.lock ikut disimpan di git, dan perintah dijalankan lewat bundle",
                    "exec.",
                    "",
                    "Kasus kecil: kamu dan teman PKL mengerjakan aplikasi Sinatra yang sama.",
                    "Gemfile kalian menulis gem \"sinatra\", \"~> 4.0\". Di laptopmu aplikasinya",
                    "jalan, sedangkan di laptop temanmu yang baru memasang gem, satu halaman",
                    "malah error.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Kodenya sama dan hasilnya beda, berarti yang beda lingkungannya.",
                    "     Cek versi gem di dua laptop dengan gem list sinatra.",
                    "  2. Baca Gemfile-nya. ~> 4.0 menerima versi 4.x mana pun, jadi Gemfile",
                    "     saja nggak menjamin kalian memakai versi yang sama.",
                    "  3. Simpan Gemfile.lock ke git. Temanmu mengambil berkas itu, lalu",
                    "     menjalankan bundle install, yang memasang versi persis dari sana.",
                    "  4. Jalankan aplikasinya dengan bundle exec ruby app.rb, supaya versi",
                    "     terkunci yang dipakai walaupun laptopnya punya beberapa versi.",
                    "  5. Kalau error-nya LoadError untuk berkas proyekmu sendiri, cari",
                    "     require \"./...\" yang cuma jalan dari folder tertentu, lalu ganti",
                    "     dengan require_relative.",
                ]
            },
        ],
    },
    {
        "title": "14. Pengujian dengan Minitest & RSpec",
        "sections": [
            {
                "body": [
                    "Tes otomatis adalah kode yang memeriksa kodemu yang lain. Kamu menulis",
                    "\"kalau nilainya 85, grade-nya harus A\", lalu komputer mengeceknya tiap",
                    "kali tes dijalankan. Ruby punya dua kerangka tes utama, dan dua-duanya",
                    "bagus:",
                    "  - Minitest ikut dibagikan bersama Ruby sebagai bundled gem, jadi",
                    "    biasanya langsung bisa dipakai. Gayanya mirip tes di bahasa lain.",
                    "  - RSpec adalah gem terpisah. Gayanya \"spesifikasi\" yang terbaca",
                    "    seperti kalimat, dan paling umum dipakai di proyek Rails.",
                    "",
                    "Di sebagian distro Linux, termasuk Fedora, Minitest dipaketkan",
                    "terpisah. Kalau require \"minitest/autorun\" gagal dengan LoadError,",
                    "pasang dulu dengan gem install minitest.",
                    "",
                    "Contoh tes Minitest:",
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
                    "Tiap method yang namanya diawali test_ dijalankan sebagai satu tes.",
                    "setup dijalankan sebelum tiap tes, jadi tiap tes dapat objek Rapor",
                    "yang baru.",
                    "",
                    "Assertion adalah pernyataan yang dicek oleh tes, misalnya \"dua nilai",
                    "ini harus sama\". Assertion di Minitest:",
                    "",
                    "  assert(kondisi)          refute(kondisi)",
                    "  assert_equal(harap, aktual)",
                    "  assert_nil / refute_nil",
                    "  assert_includes(koleksi, x)",
                    "  assert_empty / refute_empty",
                    "  assert_raises(KelasError) { ... }",
                    "  assert_instance_of(Kelas, obj)",
                    "  assert_in_delta(3.14, x, 0.01)   untuk Float",
                    "",
                    "refute adalah kebalikan assert: lulus kalau kondisinya salah. Di",
                    "assert_equal, nilai yang diharapkan ditulis dulu, baru nilai yang",
                    "dihasilkan kodemu.",
                    "",
                    "assert_in_delta wajib dipakai untuk Float. Di Ruby, 0.1 + 0.2 == 0.3",
                    "hasilnya false, dan hal yang sama terjadi di semua bahasa yang memakai",
                    "IEEE 754, standar cara komputer menyimpan pecahan. assert_in_delta",
                    "menganggap dua angka sama kalau selisihnya cukup kecil.",
                    "",
                    "Contoh tes yang sama dengan RSpec:",
                    "",
                    "  RSpec.describe Rapor do",
                    "    describe \".grade\" do",
                    "      it \"memberi A tepat di 85\" do",
                    "        expect(Rapor.grade(85)).to eq(\"A\")",
                    "      end",
                    "    end",
                    "  end",
                    "",
                    "describe mengelompokkan tes, dan it menulis satu perilaku yang",
                    "diharapkan. Pengecekannya ditulis expect(...).to, diikuti matcher.",
                    "Matcher di RSpec:",
                    "",
                    "  eq(x)         eql(x)        equal(x)   be(x)",
                    "  be > 5        be_within(0.01).of(3.14)",
                    "  include(x)    match(/pola/) start_with(x)",
                    "  be_empty      be_nil        be_a(Kelas)",
                    "  raise_error(KelasError)",
                    "  change { x }.by(1)",
                    "",
                    "be_empty bekerja untuk apa pun yang punya method empty?, karena RSpec",
                    "mengubah be_xxx jadi panggilan xxx?. Pola serupa berlaku untuk",
                    "have_key, yang memanggil has_key?, untuk be_valid, dan untuk method",
                    "bertanda tanya apa pun yang kamu tulis sendiri.",
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
                    "Lihat nilai yang dipilih di test_grade_tepat_di_batas: 85 dan 84, 75",
                    "dan 74, 60 dan 59. Menguji tepat di batas adalah yang paling",
                    "bermanfaat, karena di situlah salah ketik >= dan > terjadi. Nilai di",
                    "tengah rentang hampir nggak pernah menemukan bug.",
                    "",
                    "when 85.. adalah rentang tanpa batas atas, ada sejak Ruby 2.6. Ada",
                    "juga ..85 untuk rentang tanpa batas bawah, yang ada sejak Ruby 2.7.",
                    "Keduanya bikin case untuk penilaian jadi ringkas.",
                    "",
                    "(0..100).cover?(nilai) mengecek apakah nilai ada di antara 0 dan 100.",
                    "Untuk rentang angka, cover? dan include? memberi hasil yang sama,",
                    "karena dua-duanya cuma membandingkan kedua ujung rentang. Bedanya baru",
                    "kelihatan di rentang teks. (\"a\"..\"z\").cover?(\"bb\") hasilnya true,",
                    "karena \"bb\" ada di antara \"a\" dan \"z\" kalau diurutkan seperti di",
                    "kamus. (\"a\"..\"z\").include?(\"bb\") hasilnya false, karena \"bb\" bukan",
                    "salah satu anggota rentang itu.",
                    "",
                    "assert_equal harap, aktual, \"pesan\" punya argumen ketiga yang muncul",
                    "waktu tesnya gagal. Di tes yang berulang seperti di atas, tanpa pesan",
                    "itu kamu cuma tahu ada yang gagal, tanpa tahu nilai mana.",
                    "",
                    "catat mengembalikan self, sehingga panggilannya bisa dirangkai. Itu",
                    "disengaja: method yang mengembalikan self membuat penyiapan data tes",
                    "cukup satu baris, nggak perlu tiga.",
                    "",
                    "Cara menjalankan tes:",
                    "",
                    "  ruby test/rapor_test.rb",
                    "  rake test",
                    "  bundle exec rspec",
                    "  bundle exec rspec spec/rapor_spec.rb:12   satu baris saja",
                    "",
                    "rake test butuh Rakefile yang sudah punya tugas test. Angka :12 di",
                    "baris terakhir artinya cuma tes di baris 12 yang dijalankan.",
                    "",
                    "Pilih satu kerangka untuk satu proyek. Pilih Minitest kalau kamu ingin",
                    "kerangka yang ikut dibagikan bersama Ruby dan tes yang terasa seperti",
                    "kode biasa. Pilih RSpec kalau kamu ingin tes yang sekaligus jadi",
                    "dokumentasi, dengan matcher yang kaya.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Di banyak tim, tes dijalankan otomatis tiap kali ada perubahan kode yang",
                    "mau digabung, dan perubahan yang membuat tes gagal ditahan dulu. Aturan",
                    "yang menyangkut uang, seperti diskon, ongkir, dan pajak, hampir selalu",
                    "dijaga tes, karena satu tanda > yang seharusnya >= berarti pelanggan",
                    "ditagih dengan angka yang salah.",
                    "",
                    "Kasus kecil: toko online memberi gratis ongkir untuk belanja mulai",
                    "Rp100.000. Di bawah itu ongkirnya Rp15.000. Pemilik toko ingin yakin",
                    "aturannya benar sebelum promo dimulai.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tulis aturannya sebagai kalimat, lalu cari batasnya, yaitu 100.000.",
                    "  2. Pilih nilai uji di sekitar batas, yaitu 99.999 dan 100.000,",
                    "     ditambah satu nilai jauh di atasnya. Nilai di tengah rentang jarang",
                    "     menemukan bug.",
                    "  3. Tulis satu assertion untuk tiap nilai:",
                    "      def test_ongkir_di_sekitar_batas",
                    "        assert_equal 15_000, Toko.ongkir(99_999)",
                    "        assert_equal 0, Toko.ongkir(100_000)",
                    "        assert_equal 0, Toko.ongkir(250_000)",
                    "      end",
                    "  4. Jalankan tesnya. Kalau Toko.ongkir ditulis dengan > 100_000, baris",
                    "     100.000 yang gagal, dan Minitest melapor Expected: 0, Actual: 15000.",
                    "  5. Tambahkan kasus aneh seperti belanja negatif, lalu tetapkan",
                    "     perilakunya dengan assert_raises(ArgumentError).",
                ]
            },
        ],
    },
    {
        "title": "15. Metaprogramming Secukupnya",
        "sections": [
            {
                "body": [
                    "Metaprogramming artinya kode yang membuat atau mengubah kode lain waktu",
                    "program sedang jalan. Ruby mengizinkan itu. Rails memakainya untuk",
                    "menyediakan method seperti User.find_by_email_and_status(...), yang",
                    "nggak pernah ditulis siapa pun.",
                    "",
                    "Kemampuannya besar, dan ongkosnya juga besar. Materi ini menunjukkan",
                    "hal yang perlu kamu kenali waktu membaca kode orang lain. Semua ini",
                    "bukan alat yang perlu kamu pakai sehari-hari.",
                    "",
                    "Memeriksa objek waktu program jalan:",
                    "",
                    "  obj.class            obj.class.ancestors",
                    "  obj.methods          obj.public_methods(false)",
                    "  obj.respond_to?(:x)  obj.instance_variables",
                    "  obj.instance_variable_get(:@nama)",
                    "  Kelas.instance_methods(false)",
                    "",
                    "methods mendaftar method sebuah objek, dan instance_variables mendaftar",
                    "variabel instance-nya. Argumen false di instance_methods(false) artinya",
                    "\"cuma method yang ditulis di class ini, tanpa yang diwarisi\".",
                    "",
                    "Memanggil method lewat namanya:",
                    "",
                    "  obj.send(:nama)            termasuk method PRIVAT",
                    "  obj.public_send(:nama)     hanya yang publik",
                    "  obj.method(:nama).call(x)",
                    "",
                    "Pakai public_send, kecuali kamu memang perlu menembus batas privat.",
                    "",
                    "Awas: send yang menerima nama method dari masukan pengguna adalah",
                    "lubang keamanan besar. Lewat send, pengguna bisa memanggil method apa",
                    "pun, termasuk method privat seperti system yang menjalankan perintah",
                    "di komputermu.",
                    "",
                    "Membuat method waktu program jalan:",
                    "",
                    "  define_method(:nama) { ... }",
                    "  attr_accessor :a, :b",
                    "  Kelas.class_eval { ... }",
                    "  obj.define_singleton_method(:x) { ... }",
                    "",
                    "attr_accessor dari materi Class & Objek ternyata juga metaprogramming:",
                    "dia membuat method getter dan setter waktu isi class-nya dijalankan.",
                    "class_eval menjalankan kode di dalam sebuah class, seolah kode itu",
                    "ditulis di sana. define_singleton_method membuat method yang cuma",
                    "dimiliki satu objek itu.",
                    "",
                    "Menangkap panggilan ke method yang nggak ada:",
                    "",
                    "  def method_missing(nama, *args)",
                    "    ...",
                    "  end",
                    "",
                    "  def respond_to_missing?(nama, privat = false)",
                    "    ...",
                    "  end",
                    "",
                    "Kalau sebuah method nggak ditemukan, Ruby memanggil method_missing",
                    "dulu sebelum menyerah dengan NoMethodError.",
                    "",
                    "Aturan keras: kalau kamu menulis method_missing, kamu wajib menulis",
                    "respond_to_missing? juga. Tanpa itu, respond_to? memberi jawaban yang",
                    "salah, obj.method(:x) gagal, dan objekmu berperilaku beda dari",
                    "kebiasaan seluruh ekosistem Ruby.",
                    "",
                    "Ongkos metaprogramming itu nyata:",
                    "  - Editor nggak bisa melengkapi nama method secara otomatis.",
                    "  - grep, perintah pencari teks, nggak menemukan definisi method-nya.",
                    "  - Pesan error muncul jauh dari penyebabnya.",
                    "  - Orang berikutnya yang membaca kodemu butuh waktu lebih lama.",
                    "",
                    "Patokan praktisnya: kalau bisa ditulis biasa, tulis biasa.",
                    "Metaprogramming layak dipakai kalau dia menghapus pengulangan yang",
                    "memang banyak, dan nggak layak kalau alasannya cuma supaya terasa",
                    "pintar.",
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
                    "Class Setelan menunjukkan metaprogramming yang layak dipakai. Tiga",
                    "kunci dikali tiga method sama dengan sembilan method yang isinya sama",
                    "persis kecuali nama kuncinya. Kalau ditulis tangan, mengubah cara",
                    "kerjanya berarti menyunting sembilan tempat, dan tiap setelan baru",
                    "menambah tiga method lagi. Dengan define_method, setelan baru cukup",
                    "ditambahkan sebagai satu kunci di hash bawaannya.",
                    "",
                    "Daftar method buatan di keluaran berasal dari define_method itu. Nggak",
                    "satu pun ditulis dengan def.",
                    "",
                    "Class Catatan menunjukkan method_missing yang bertanggung jawab. Ada",
                    "tiga hal yang membuatnya begitu:",
                    "  1. super di cabang terakhir. Method yang memang nggak ada tetap",
                    "     melempar NoMethodError dengan pesan yang normal. Tanpa super,",
                    "     method_missing mengembalikan nil tanpa pesan apa pun, dan salah",
                    "     ketik nama method jadi bug yang nggak kelihatan.",
                    "  2. respond_to_missing? yang cocok dengan method_missing, sehingga",
                    "     respond_to? menjawab dengan benar.",
                    "  3. super juga di respond_to_missing?, supaya method yang sungguhan",
                    "     ada tetap terdeteksi.",
                    "",
                    "Kalau tiga hal itu terasa banyak untuk diingat, itu memang petunjuknya.",
                    "Untuk kasus seperti ini, OpenStruct atau Struct biasa udah cukup, dan",
                    "jauh lebih jelas. OpenStruct butuh require \"ostruct\", dan sejak Ruby",
                    "4.0 dia jadi bundled gem, sama seperti CSV di materi Berkas, JSON &",
                    "Baris Perintah.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Rails memakai metaprogramming untuk membuat method dari data. Kalau model",
                    "Pesanan mendeklarasikan enum untuk kolom status, Rails membuatkan method",
                    "seperti dibayar? dan dikirim? tanpa satu pun ditulis tangan. Di kode",
                    "aplikasimu sendiri, define_method layak dipakai untuk pola yang sama:",
                    "banyak method kembar yang cuma beda nama.",
                    "",
                    "Kasus kecil: class Pesanan punya empat status, yaitu :baru, :dibayar,",
                    ":dikirim, dan :selesai. Halaman daftar pesanan butuh empat method",
                    "bertanda tanya, yaitu baru?, dibayar?, dikirim?, dan selesai?, untuk",
                    "memilih warna label tiap pesanan.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Lihat pengulangannya. Keempat method isinya sama, yaitu",
                    "     membandingkan @status dengan satu Symbol, dan cuma beda nama. Status",
                    "     kelima nanti berarti method kelima yang ditulis ulang.",
                    "  2. Simpan daftar status di satu konstanta, lalu buat method-nya di",
                    "     dalam perulangan:",
                    "      class Pesanan",
                    "        STATUS = %i[baru dibayar dikirim selesai].freeze",
                    "        STATUS.each do |s|",
                    "          define_method(\"#{s}?\") { @status == s }",
                    "        end",
                    "      end",
                    "  3. Periksa hasilnya dengan Pesanan.instance_methods(false). Isinya",
                    "     keempat method itu, padahal nggak ada satu def pun untuk mereka.",
                    "  4. Status baru, misalnya :dibatalkan, cukup ditambah ke daftar di",
                    "     konstanta itu, dan method dibatalkan? langsung ada.",
                    "",
                    "Jebakan: kalau nama status datang dari masukan pengguna, misalnya dari",
                    "alamat web, jangan teruskan ke send. Cocokkan dulu dengan daftar status",
                    "yang sah, lalu panggil lewat public_send.",
                ]
            },
        ],
    },
    {
        "title": "16. Ekspresi Reguler",
        "sections": [
            {
                "body": [
                    "Regex, singkatan dari regular expression atau ekspresi reguler, adalah",
                    "pola untuk mencari dan mencocokkan teks. Contohnya pola \"empat angka,",
                    "tanda minus, dua angka, tanda minus, dua angka\" untuk mengenali",
                    "tanggal. Di Ruby, regex ditulis di antara dua garis miring. Regex juga",
                    "objek biasa bertipe Regexp, jadi bisa disimpan di variabel atau dioper",
                    "ke method:",
                    "",
                    "  /\\d{4}-\\d{2}-\\d{2}/",
                    "  %r{https?://\\S+}        pembatas lain, tanpa melarikan /",
                    "  Regexp.new(teks)        dari string, saat polanya dinamis",
                    "",
                    "\\d artinya satu angka, dan {4} artinya tepat empat kali. Bentuk %r{...}",
                    "berguna kalau polanya penuh garis miring, misalnya alamat web, karena",
                    "garis miring di dalamnya nggak perlu ditulis \\/. Regexp.new dipakai",
                    "kalau polanya baru diketahui waktu program jalan.",
                    "",
                    "Operator dan method yang dipakai:",
                    "",
                    "  teks =~ /pola/        posisi cocok, atau nil",
                    "  teks.match(/pola/)    MatchData, atau nil",
                    "  teks.match?(/pola/)   true/false, tanpa membuat MatchData",
                    "  teks.scan(/pola/)     semua kecocokan jadi array",
                    "  teks.sub(/pola/, x)   ganti yang pertama",
                    "  teks.gsub(/pola/, x)  ganti semuanya",
                    "  teks.split(/pola/)",
                    "  teks[/pola/]          bagian yang cocok, atau nil",
                    "",
                    "MatchData adalah objek berisi hasil pencocokan: bagian yang cocok, isi",
                    "tiap grup, dan posisinya.",
                    "",
                    "Biasakan memakai match?. Method ini nggak mengisi variabel global",
                    "seperti $~ dan nggak membuat objek MatchData, jadi jauh lebih ringan",
                    "kalau kamu cuma bertanya \"cocok atau nggak\".",
                    "",
                    "Grup bernama membuat hasilnya gampang dibaca. Grup adalah bagian pola",
                    "yang diapit kurung, dan ?<nama> memberinya nama:",
                    "",
                    "  m = \"2026-09-22\".match(/(?<thn>\\d{4})-(?<bln>\\d{2})/)",
                    "  m[:thn]     \"2026\"",
                    "  m[:bln]     \"09\"",
                    "  m.pre_match / m.post_match / m.captures",
                    "",
                    "pre_match adalah teks sebelum bagian yang cocok, post_match teks",
                    "sesudahnya, dan captures array berisi isi semua grup. Di contoh itu,",
                    "post_match bernilai \"-22\".",
                    "",
                    "Ada satu kejutan yang berguna. Kalau regex yang ditulis langsung di",
                    "kode (literal) dipakai dengan =~, grup bernamanya otomatis jadi",
                    "variabel lokal:",
                    "",
                    "  if /(?<thn>\\d{4})/ =~ tanggal",
                    "    puts thn        # variabel lokal, bukan m[:thn]",
                    "  end",
                    "",
                    "Syaratnya, regex-nya harus ditulis di sebelah kiri =~. Kalau dibalik,",
                    "variabel thn nggak pernah dibuat.",
                    "",
                    "Bahan untuk menyusun pola:",
                    "",
                    "  .  \\d \\w \\s        \\D \\W \\S kebalikannya",
                    "  [abc] [^abc] [a-z]",
                    "  ^ $               awal/akhir baris (bawaan di Ruby!)",
                    "  \\A \\z             awal/akhir seluruh teks",
                    "  \\b                batas kata",
                    "  * + ? {n} {n,m}   *? +? versi malas",
                    "  (...) (?:...) (?<nama>...)",
                    "",
                    "Titik artinya karakter apa pun selain baris baru. \\d artinya angka, \\w",
                    "huruf, angka, atau garis bawah, dan \\s spasi, tab, atau baris baru.",
                    "[abc] artinya salah satu dari a, b, atau c, sedangkan [^abc] artinya",
                    "selain itu. * artinya nol kali atau lebih, + satu kali atau lebih, dan",
                    "? nol atau satu kali. Versi malas seperti *? mengambil sesedikit",
                    "mungkin. (?:...) adalah grup yang hasilnya nggak disimpan.",
                    "",
                    "Ini beda penting dari bahasa lain. Di Ruby, ^ dan $ selalu berarti awal",
                    "dan akhir baris, bukan awal dan akhir seluruh teks. Untuk memeriksa",
                    "seluruh masukan, pakai \\A dan \\z:",
                    "",
                    "  /^\\d+$/     cocok asal ada satu baris yang isinya angka semua,",
                    "              berapa pun baris asing di atas atau di bawahnya",
                    "  /\\A\\d+\\z/   menuntut seluruh teks berupa angka",
                    "",
                    "Gara-gara salah pilih antara keduanya, aplikasi Rails pernah punya",
                    "celah keamanan sungguhan.",
                    "",
                    "Penanda di belakang garis miring penutup mengubah cara pola dibaca. i",
                    "mengabaikan huruf besar-kecil, m membuat titik ikut cocok dengan baris",
                    "baru, dan x mengabaikan spasi di dalam pola supaya pola bisa diberi",
                    "komentar.",
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
                    "Tabel perbandingan di bagian keempat adalah pelajaran terpenting materi",
                    "ini. Teks \"2026-09-22\\nsisipan\" lolos pola longgar ^...$, karena baris",
                    "pertamanya cocok, walaupun ada baris asing di bawahnya. Pola ketat",
                    "\\A...\\z menolaknya. Untuk memeriksa masukan, \\A...\\z yang benar,",
                    "selalu. Pola ketat juga menolak \"2026-13-40\", karena di sana bulan",
                    "dibatasi 01 sampai 12 dan tanggal 01 sampai 31.",
                    "",
                    "Penanda /x membuat spasi dan baris baru di dalam pola diabaikan, jadi",
                    "pola yang panjang bisa ditulis bertingkat dan diberi komentar. Tanpa",
                    "/x, pola log di atas harus ditulis jadi satu baris sepanjang sekitar",
                    "seratus karakter.",
                    "",
                    "log.scan dengan satu grup menghasilkan array berisi array, makanya",
                    "hasilnya diratakan dulu dengan flatten. Di gsub, '\\\\1' di teks",
                    "pengganti artinya isi grup pertama. Jadi tiga angka pertama alamat IP",
                    "tetap, dan angka terakhirnya diganti xxx.",
                    "",
                    "filter_map (ada sejak Ruby 2.7) mengubah tiap elemen, lalu membuang",
                    "hasil yang nil atau false. Mirip map lalu compact, bedanya compact cuma",
                    "membuang nil. Cocok untuk log ini, karena match mengembalikan nil untuk",
                    "baris yang nggak cocok pola.",
                    "",
                    "Jangan mengurai HTML dengan regex. Peringatan ini berlaku di semua",
                    "bahasa. HTML bisa bersarang tanpa batas, sedangkan regex nggak bisa",
                    "menghitung kedalaman sarangnya. Pakai pustaka seperti Nokogiri.",
                    "",
                    "Hati-hati juga dengan kuantifier bersarang, yaitu tanda pengulang di",
                    "dalam tanda pengulang seperti (a+)+. Di Ruby sebelum 3.2, pola seperti",
                    "itu bisa bikin pencocokan pada teks panjang menggantung. Sejak Ruby",
                    "3.2, kebanyakan pola seperti itu dijaga supaya tetap cepat, tapi belum",
                    "semuanya. Untuk berjaga, Ruby 3.2 juga menambahkan Regexp.timeout,",
                    "yaitu batas waktu untuk satu pencocokan.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Regex dipakai di hampir tiap formulir yang memeriksa format, seperti kode",
                    "pos, nomor HP, NIK, dan alamat email. Regex juga dipakai untuk membaca",
                    "log server dan menyamarkan data pribadi sebelum ditampilkan. Salah pilih",
                    "antara ^ $ dan \\A \\z di pemeriksaan seperti itu bisa meloloskan masukan",
                    "yang seharusnya ditolak.",
                    "",
                    "Kasus kecil: formulir pendaftaran meminta NIK. NIK di KTP berisi 16",
                    "digit, yaitu 6 digit kode wilayah, 6 digit tanggal lahir, dan 4 digit",
                    "nomor urut. Tolak masukan seperti \"32012345\" atau \"3201-2345-6789-0123\",",
                    "dan ambil bagian tanggal lahir dari NIK yang sah.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Masukannya teks dari formulir. Keluarannya sah atau nggak, plus",
                    "     bagian-bagiannya kalau sah.",
                    "  2. Tulis polanya dengan grup bernama, dan jangkarkan dengan \\A dan \\z",
                    "     supaya seluruh teks yang diperiksa:",
                    "      POLA_NIK = /\\A(?<wilayah>\\d{6})(?<lahir>\\d{6})(?<urut>\\d{4})\\z/",
                    "      m = \"1234561205990001\".match(POLA_NIK)",
                    "      puts m ? \"lahir #{m[:lahir]}, urut #{m[:urut]}\" : \"NIK tidak sah\"",
                    "  3. Untuk NIK contoh itu, hasilnya lahir 120599 dan urut 0001. Masukan",
                    "     yang kurang digit atau memuat tanda hubung memberi nil.",
                    "  4. Buang spasi di ujung dengan strip sebelum mencocokkan. Orang sering",
                    "     menempelkan NIK hasil salinan beserta spasinya, dan \\A...\\z",
                    "     menolaknya.",
                    "",
                    "Jebakan: pola /^\\d{16}$/ meloloskan \"1234561205990001\\nhalo\", karena ^",
                    "dan $ di Ruby cuma menandai awal dan akhir baris.",
                ]
            },
        ],
    },
    {
        "title": "17. Waktu & Tanggal",
        "sections": [
            {
                "body": [
                    "Ruby punya tiga class untuk waktu, dan kamu perlu tahu kapan memakai",
                    "yang mana:",
                    "",
                    "  Time      titik waktu, presisi sampai nanodetik. Ada",
                    "            di inti bahasa, tanpa require.",
                    "  Date      tanggal saja, tanpa jam. require \"date\"",
                    "  DateTime  usang, jangan dipakai di kode baru.",
                    "",
                    "Nanodetik itu sepermiliar detik. Time langsung bisa dipakai, sedangkan",
                    "Date harus dimuat dulu dengan require \"date\". DateTime masih ada, tapi",
                    "sudah usang, jadi pakai Time atau Date.",
                    "",
                    "Cara membuat nilai waktu dan tanggal:",
                    "",
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
                    "Epoch adalah jumlah detik sejak 1 Januari 1970 pukul 00.00 UTC. UTC",
                    "sendiri adalah waktu acuan dunia yang nggak terikat zona mana pun.",
                    "Date.parse menebak format tanggal dari teksnya, sedangkan Date.strptime",
                    "membaca teks dengan format yang kamu tentukan sendiri.",
                    "",
                    "Untuk mengubah waktu jadi teks, pakai strftime dengan kode format",
                    "berikut:",
                    "",
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
                    "Tanda - di depan huruf format membuang nol di depan angka. %-d menulis",
                    "tanggal 5 sebagai 5, sedangkan %d menulisnya 05. Nama hari dan bulan",
                    "dari %A dan %B selalu dalam bahasa Inggris, walaupun komputermu disetel",
                    "ke bahasa Indonesia.",
                    "",
                    "Soal aritmetika, Time dan Date berbeda:",
                    "",
                    "  Time + 3600        tambah 3600 detik",
                    "  Date + 1           tambah 1 hari",
                    "  Date >> 1          tambah 1 bulan",
                    "  Date << 1          kurangi 1 bulan",
                    "  (t2 - t1)          Time: selisih dalam detik (Float)",
                    "  (d2 - d1).to_i     Date: selisih dalam hari",
                    "",
                    "Jebakan: satuan yang berbeda ini sumber bug klasik. Kalau kamu",
                    "menambahkan 30 ke sebuah Time dengan harapan maju 30 hari, yang kamu",
                    "dapat cuma 30 detik.",
                    "",
                    "Soal zona waktu, patokan praktisnya cuma satu: simpan semua waktu dalam",
                    "UTC, lalu ubah ke zona pengguna hanya waktu menampilkannya. Kalau nggak",
                    "begitu, laporan \"penjualan hari ini\" bakal salah untuk sebagian",
                    "penggunamu, setiap hari.",
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
                    "Date.new(tahun, bulan, -1) memakai angka negatif untuk hari terakhir",
                    "bulan itu, mirip index negatif di array. Cara ini jauh lebih aman",
                    "daripada menghitung sendiri apakah bulan itu punya 28, 29, 30, atau 31",
                    "hari.",
                    "",
                    "(mulai..(mulai + 21)).step(7) melangkah tujuh hari sekali di dalam",
                    "rentang tanggal, jadi hasilnya jadwal mingguan.",
                    "",
                    "Perhitungan usia di bagian akhir menunjukkan jebakan yang sering",
                    "terjadi. Selisih tahun saja salah untuk orang yang belum berulang tahun",
                    "tahun ini. Di contoh itu selisih tahunnya 20, tapi usianya masih 19.",
                    "Membandingkan pasangan [bulan, tanggal] sebagai array menyelesaikannya",
                    "dalam satu baris. <=> menghasilkan -1 kalau tanggal acuan masih",
                    "sebelum hari ulang tahunnya, dan .negative? mengecek apakah hasil itu",
                    "negatif.",
                    "",
                    "Perbandingannya memakai <=> lalu .negative?, dan nggak memakai <",
                    "langsung. Array di Ruby punya <=> tapi nggak punya <, jadi",
                    "[1, 2] < [1, 3] melempar NoMethodError. Ini beda dari Python, yang bisa",
                    "membandingkan tuple secara langsung.",
                    "",
                    "Lihat juga hasil Time.at(...): tahunnya 2025, padahal tanggal di contoh",
                    "Date-nya 2026. Angka epoch adalah jumlah detik sejak 1970, dan kalau",
                    "ditulis tangan, angkanya hampir selalu meleset. Makanya waktu sebaiknya",
                    "dibuat dari tanggal yang terbaca, bukan dari angka epoch.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Tanggal ada di balik banyak aturan sehari-hari: jatuh tempo tagihan,",
                    "masa pinjam buku perpustakaan, tenggat tugas, atau tanggal cicilan bulan",
                    "depan. Hitungan seperti itu memakai Date, karena yang dihitung harinya,",
                    "dan jamnya nggak ikut berpengaruh.",
                    "",
                    "Kasus kecil: perpustakaan sekolah meminjamkan buku selama 7 hari, dengan",
                    "denda Rp500 per hari terlambat. Sebuah buku dipinjam 3 Oktober 2026 dan",
                    "dikembalikan 15 Oktober 2026.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Masukannya dua tanggal. Keluarannya tanggal jatuh tempo, jumlah hari",
                    "     terlambat, dan dendanya.",
                    "  2. Jatuh tempo adalah tanggal pinjam ditambah 7. Di Date, + 7 artinya",
                    "     tujuh hari.",
                    "  3. Hari terlambat adalah selisih tanggal kembali dan jatuh tempo, yang",
                    "     diubah jadi Integer dengan to_i:",
                    "      require \"date\"",
                    "      tempo = Date.new(2026, 10, 3) + 7",
                    "      telat = [(Date.new(2026, 10, 15) - tempo).to_i, 0].max",
                    "      puts \"Jatuh tempo #{tempo}, telat #{telat} hari, denda Rp#{telat * 500}\"",
                    "  4. Hasilnya jatuh tempo 2026-10-10, telat 5 hari, dan denda Rp2500.",
                    "  5. Periksa buku yang kembali lebih awal. Selisihnya negatif, dan tanpa",
                    "     [..., 0].max dendanya jadi minus. max menjaga angkanya paling kecil 0.",
                    "",
                    "Ingat: untuk jatuh tempo bulanan, pakai >> 1. Date.new(2026, 1, 31) >> 1",
                    "memberi 28 Februari, sedangkan + 30 memberi 2 Maret.",
                ]
            },
        ],
    },
    {
        "title": "18. Set, Struct & Data",
        "sections": [
            {
                "body": [
                    "Set adalah himpunan, yaitu kumpulan nilai tanpa duplikat. Set juga",
                    "punya operasi himpunan seperti gabungan dan irisan:",
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
                    "Sejak Ruby 3.2, Set langsung tersedia tanpa require, dan di Ruby 4.0",
                    "Set malah jadi bagian inti bahasa. Gabungan berisi semua elemen dari",
                    "kedua set. Irisan berisi elemen yang ada di keduanya. Selisih berisi",
                    "elemen a yang nggak ada di b. Beda simetris berisi elemen yang cuma ada",
                    "di salah satu set. subset? bertanya apakah semua elemen a ada di b, dan",
                    "superset? kebalikannya.",
                    "",
                    "add? mengembalikan nil kalau elemennya sudah ada. Ini cara paling",
                    "pendek untuk menulis \"kerjakan hanya kalau belum pernah dilihat\".",
                    "",
                    "Kenapa pakai Set, dan nggak pakai Array aja? include? pada Array",
                    "memeriksa elemen satu per satu, sedangkan pada Set elemennya langsung",
                    "dicari lewat hash. Untuk seribu elemen, bedanya udah soal kecepatan,",
                    "nggak lagi soal gaya.",
                    "",
                    "Struct membuat class untuk wadah data dalam satu baris:",
                    "",
                    "  Titik = Struct.new(:x, :y)",
                    "  t = Titik.new(3, 4)",
                    "  t.x                    3",
                    "  t.x = 5                bisa diubah",
                    "  t.to_a / t.to_h",
                    "  t == Titik.new(5, 4)   kesetaraan berbasis nilai",
                    "",
                    "  Titik = Struct.new(:x, :y, keyword_init: true)",
                    "  Titik.new(x: 3, y: 4)  argumen berkunci",
                    "",
                    "Isi Struct bisa diubah sesudah dibuat. to_a dan to_h mengubahnya jadi",
                    "array dan hash. Dua Struct dianggap sama kalau isinya sama, walaupun",
                    "objeknya berbeda. keyword_init: true membuat Struct diisi lewat nama",
                    "field-nya, yaitu isian seperti x dan y, dan nggak lewat urutan.",
                    "",
                    "Struct boleh punya method sendiri lewat blok:",
                    "",
                    "  Titik = Struct.new(:x, :y) do",
                    "    def jarak = Math.sqrt(x**2 + y**2)",
                    "  end",
                    "",
                    "Data, yang ada sejak Ruby 3.2, adalah Struct yang beku:",
                    "",
                    "  Titik = Data.define(:x, :y)",
                    "  t = Titik.new(x: 3, y: 4)",
                    "  t.x = 5                ERROR: tidak ada setter",
                    "  t.with(x: 5)           salinan dengan sebagian diubah",
                    "",
                    "Data nggak punya setter, jadi isinya nggak bisa diubah. with membuat",
                    "salinan baru dengan sebagian isinya diganti, dan objek aslinya tetap.",
                    "",
                    "Data adalah padanan record di C# dan data class di Kotlin. Untuk wadah",
                    "data yang nggak boleh berubah, seperti hasil query, pesan, atau",
                    "konfigurasi, Data lebih tepat daripada Struct.",
                    "",
                    "Cara memilih di antara keempatnya:",
                    "",
                    "  Data     data beku. Pilihan pertama sejak Ruby 3.2.",
                    "  Struct   perlu diubah sesudah dibuat.",
                    "  Class    punya perilaku, bukan cuma data.",
                    "  Hash     bentuknya belum tetap atau datang dari luar.",
                    "",
                    "Data yang datang dari luar misalnya hasil JSON.parse, yang isinya",
                    "belum tentu lengkap.",
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
                    "sudah.add?(nama) cuma mencetak tiga dari lima nama, karena dua sisanya",
                    "duplikat. Cara ini jauh lebih pendek daripada memeriksa include? dulu",
                    "lalu menambahkan, dan pencarian di hash-nya cuma terjadi sekali.",
                    "",
                    "Beda Struct dan Data kelihatan jelas di contoh itu. stok pada Struct",
                    "bisa langsung dikurangi, sedangkan Data sama sekali nggak punya setter.",
                    "Padanannya di Data adalah .with, yang menghasilkan objek baru dan",
                    "membiarkan objek lama apa adanya. Baris \"asli tetap\" di keluaran",
                    "menunjukkannya.",
                    "",
                    "Data juga menolak dibuat kalau ada field yang kurang, sedangkan Struct",
                    "mengisi field yang kurang dengan nil tanpa protes. Ketegasan itu",
                    "menangkap salah ketik sejak baris pertama. Dengan Struct, kesalahannya",
                    "baru ketahuan tiga fungsi kemudian, waktu nil itu akhirnya dipakai.",
                    "",
                    "Baris terakhir mencoba mengubah isi Data lewat instance_variable_set,",
                    "dan Ruby menolaknya dengan FrozenError. Objek Data dibekukan sejak",
                    "dibuat.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Set dipakai setiap kali pertanyaannya soal keanggotaan: siapa yang",
                    "terdaftar tapi belum datang, produk mana yang ada di dua gudang, atau",
                    "pesan mana yang sudah pernah diproses. Data cocok untuk nilai yang nggak",
                    "boleh berubah sesudah dibuat, misalnya titik jemput di aplikasi ojek",
                    "online atau satu baris hasil laporan.",
                    "",
                    "Kasus kecil: panitia seminar punya daftar kode tiket pendaftar, T01",
                    "sampai T04. Pemindai di pintu mencatat T02, T04, T04, dan T07, karena",
                    "satu peserta memindai dua kali. Cari siapa yang daftar tapi nggak",
                    "datang, dan siapa yang datang tanpa daftar.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Masukannya dua daftar kode, keluarannya dua daftar selisih. Urutan",
                    "     dan duplikat nggak penting di sini, jadi ini pekerjaan Set.",
                    "  2. Ubah keduanya jadi Set. Pindaian ganda T04 hilang dengan sendirinya.",
                    "  3. Ambil selisih himpunan dari dua arah:",
                    "      daftar = Set[\"T01\", \"T02\", \"T03\", \"T04\"]",
                    "      hadir = [\"T02\", \"T04\", \"T04\", \"T07\"].to_set",
                    "      puts \"belum datang: #{(daftar - hadir).sort.join(', ')}\"",
                    "      puts \"tanpa daftar: #{(hadir - daftar).sort.join(', ')}\"",
                    "  4. Hasilnya, yang belum datang T01 dan T03, dan yang datang tanpa",
                    "     daftar T07.",
                    "  5. Periksa kode yang diketik dengan huruf kecil, misalnya t02. Set",
                    "     membandingkan teks persis, jadi rapikan dengan upcase sebelum kode",
                    "     itu dimasukkan.",
                ]
            },
        ],
    },
    {
        "title": "19. Ruby untuk Skrip Sistem",
        "sections": [
            {
                "body": [
                    "Skrip adalah program pendek untuk mengotomatiskan pekerjaan di",
                    "terminal. Ruby nyaman dipakai untuk menggantikan skrip Bash yang sudah",
                    "kepanjangan, dan semua yang dibutuhkan ada di pustaka standar.",
                    "",
                    "Untuk argumen dan lingkungan:",
                    "",
                    "  ARGV                array argumen, tanpa nama program",
                    "  $PROGRAM_NAME       nama programnya",
                    "  ENV[\"HOME\"]         variabel lingkungan",
                    "  ENV.fetch(\"API_KEY\") melempar kalau tidak ada",
                    "",
                    "Variabel lingkungan adalah pengaturan yang diwariskan terminal ke",
                    "program, misalnya HOME yang berisi letak folder rumahmu. ENV.fetch",
                    "tanpa nilai bawaan adalah kebiasaan yang baik untuk pengaturan yang",
                    "wajib ada. Lebih baik programnya gagal saat mulai, daripada jalan",
                    "dengan nil yang baru bikin error sejam kemudian.",
                    "",
                    "Untuk membaca masukan:",
                    "",
                    "  gets                satu baris dari stdin",
                    "  $stdin.read         seluruhnya",
                    "  $stdin.each_line { } baris demi baris",
                    "  ARGF.each_line { }   dari berkas di ARGV, atau stdin",
                    "  warn \"pesan\"         cetak ke stderr",
                    "",
                    "stdin adalah masukan standar, yaitu teks yang diketik ke program atau",
                    "dialirkan dari perintah lain. stderr adalah jalur keluaran khusus untuk",
                    "pesan error dan pesan status, terpisah dari stdout yang berisi hasil.",
                    "",
                    "Jebakan: gets polos membaca lewat ARGF. Kalau ada nama berkas di",
                    "argumen program, gets membaca dari berkas itu, dan stdin nggak",
                    "disentuh. Kalau argumennya bukan nama berkas, gets malah gagal karena",
                    "berkasnya nggak ketemu. Kalau kamu memang mau membaca dari stdin, tulis",
                    "$stdin.gets.",
                    "",
                    "ARGF berguna karena membuat skripmu berperilaku seperti perkakas Unix.",
                    "Skripnya bisa menerima nama berkas sebagai argumen, atau menerima",
                    "aliran dari perintah lain lewat pipa (tanda |), tanpa kode tambahan.",
                    "",
                    "Untuk keluar dengan kode status:",
                    "",
                    "  exit 0     berhasil",
                    "  exit 1     gagal",
                    "  abort \"pesan\"   cetak ke stderr lalu keluar dengan 1",
                    "",
                    "Kode status adalah angka yang dilaporkan program ke pemanggilnya waktu",
                    "selesai. 0 artinya berhasil, angka lain artinya gagal. Skrip lain, dan",
                    "tanda && di terminal, memakai angka ini untuk memutuskan langkah",
                    "berikutnya.",
                    "",
                    "Untuk menjalankan perintah lain, urut dari yang paling berbahaya:",
                    "",
                    "  `ls -l`              backtick: ambil keluarannya",
                    "  system(\"ls -l\")      jalankan, kembalikan true/false",
                    "  system(\"ls\", \"-l\")   bentuk array, tanpa shell",
                    "  require \"open3\"",
                    "  Open3.capture3(\"ls\", \"-l\")  keluaran, galat, status",
                    "",
                    "Backtick adalah tanda petik terbalik (`). system mengembalikan nil",
                    "kalau perintahnya sama sekali nggak bisa dijalankan, misalnya karena",
                    "nggak ketemu. Open3.capture3 mengembalikan tiga hal sekaligus: isi",
                    "stdout, isi stderr, dan status keluarnya.",
                    "",
                    "Aturan keamanan: bentuk satu string dijalankan lewat shell, yaitu",
                    "program yang menafsirkan perintah terminal, seperti bash. Akibatnya,",
                    "isi variabel yang ditempel ke string itu bisa jadi perintah kedua.",
                    "Titik koma, tanda pipa, dan tanda dolar di dalam variabel semuanya",
                    "punya arti khusus bagi shell.",
                    "",
                    "  satu string  -> shell mengurai isinya, perintah kedua",
                    "                  yang tersembunyi di variabel ikut jalan",
                    "  bentuk array -> variabelnya dioper apa adanya sebagai",
                    "                  satu argumen, shell tidak dilibatkan",
                    "",
                    "Pakai bentuk array selalu, kecuali kamu memang butuh pipa atau",
                    "pengalihan, yaitu tanda > untuk menyimpan keluaran ke berkas.",
                    "",
                    "OptionParser di pustaka standar mengurus flag, nilai, dan teks bantuan",
                    "tanpa satu gem pun. Contohnya ada di program di bawah.",
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
                    "Baris peringatannya masuk ke stderr. Karena itu baris tersebut nggak",
                    "ada di keluaran stdout di atas, dan nggak ikut tersimpan kalau",
                    "keluarannya dialihkan ke berkas.",
                    "",
                    "Baris \"bentuk array\" adalah buktinya. Seluruh isi variabel tercetak",
                    "apa adanya sebagai satu argumen, termasuk titik komanya. Kalau yang",
                    "dipakai satu string yang disisipi variabel, shell bakal mengurainya",
                    "dan menjalankan bagian sesudah titik koma sebagai perintah tersendiri.",
                    "Kalau variabel itu datang dari pengguna, isinya bisa apa aja.",
                    "",
                    "Di contoh itu, penguji.parse! dikasih array buatan supaya hasilnya",
                    "selalu sama. Di skrip sungguhan, yang dikasih adalah ARGV. Kata Integer",
                    "di o.on(\"-m\", \"--minimal N\", Integer, ...) mengubah teks argumennya",
                    "jadi angka.",
                    "",
                    "%i[nama nilai] di OptionParser membatasi nilai yang diterima. Nilai di",
                    "luar daftar itu otomatis ditolak dengan OptionParser::InvalidArgument,",
                    "dengan pesan seperti invalid argument: --urut harga. Jadi kamu dapat",
                    "validasi tanpa menulis kode tambahan.",
                    "",
                    "Kebiasaan yang membuat skrip Ruby enak dipakai di terminal:",
                    "  - Hasil ke stdout, pesan status ke stderr.",
                    "  - Kode keluar 0 untuk berhasil, selain 0 untuk gagal.",
                    "  - Terima nama berkas sebagai argumen maupun aliran lewat pipa.",
                    "  - Sediakan --help.",
                    "  - Tulis #!/usr/bin/env ruby di baris pertama, lalu jalankan chmod +x",
                    "    pada berkasnya.",
                    "",
                    "Baris #!/usr/bin/env ruby disebut shebang. Baris itu memberi tahu",
                    "sistem bahwa berkas ini dijalankan dengan ruby. chmod +x memberi izin",
                    "supaya berkas itu bisa dijalankan langsung, misalnya dengan ./rapor.rb.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Admin server dan tim operasional menulis skrip kecil untuk pekerjaan",
                    "rutin: mencari error di log, memeriksa backup, atau membersihkan berkas",
                    "lama. Skrip seperti itu sering dijalankan cron (program yang menjalankan",
                    "perintah di jam tertentu) atau dirangkai dengan && di terminal. Karena",
                    "itu kode keluar dan pemisahan stdout dari stderr menentukan apakah",
                    "skripnya bisa dipakai.",
                    "",
                    "Kasus kecil: log server hari ini punya ratusan baris, dan beberapa di",
                    "antaranya memuat kata ERROR. Buat skrip yang mencetak baris itu saja,",
                    "melaporkan jumlahnya, dan keluar dengan kode 1 kalau ada error.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tentukan masukannya: nama berkas di argumen, atau aliran lewat pipa.",
                    "     ARGF menerima keduanya tanpa kode tambahan.",
                    "  2. Pisahkan keluarannya. Baris error masuk stdout, karena itulah",
                    "     hasilnya. Ringkasan jumlah masuk stderr lewat warn.",
                    "  3. Tentukan kode keluarnya, yaitu 0 kalau bersih dan 1 kalau ada error:",
                    "      #!/usr/bin/env ruby",
                    "      galat = ARGF.each_line.select { |b| b.include?(\"ERROR\") }",
                    "      puts galat",
                    "      warn \"#{galat.size} baris error\"",
                    "      exit(galat.empty? ? 0 : 1)",
                    "  4. Coba dua cara pemanggilan, yaitu ruby cari_error.rb server.log dan",
                    "     cat server.log | ruby cari_error.rb. Hasilnya harus sama.",
                    "  5. Coba nama berkas yang salah. ARGF melempar Errno::ENOENT, dan pesan",
                    "     error-nya menyebut nama berkas itu.",
                    "",
                    "Jebakan: kalau ringkasannya dicetak dengan puts, angka itu ikut tersimpan",
                    "waktu keluarannya dialihkan ke berkas dengan tanda >.",
                ]
            },
        ],
    },
    {
        "title": "20. Gaya, Kualitas & Jebakan Umum",
        "sections": [
            {
                "body": [
                    "Materi ini merangkum hal-hal yang paling sering salah di Ruby, plus",
                    "kebiasaan yang bikin kode tetap enak dirawat.",
                    "",
                    "Gaya penulisan yang dipatuhi hampir semua programmer Ruby:",
                    "  - Indentasi dua spasi. Bukan empat, bukan tab.",
                    "  - snake_case untuk method dan variabel.",
                    "  - PascalCase untuk class dan module.",
                    "  - SCREAMING_CASE untuk konstanta.",
                    "  - Akhiran ? untuk method yang mengembalikan true atau false.",
                    "  - Akhiran ! untuk versi yang lebih berbahaya.",
                    "  - Kurung kurawal untuk blok satu baris, do...end untuk blok beberapa",
                    "    baris.",
                    "  - Panjang baris paling banyak sekitar 100 karakter.",
                    "  - Tanpa return di baris terakhir method.",
                    "",
                    "RuboCop, yang dibahas di materi Gem, Bundler & Struktur Proyek,",
                    "menegakkan semua aturan itu secara otomatis. Pasang sejak awal proyek.",
                    "Di proyek lama, rubocop --auto-gen-config mencatat keadaan sekarang",
                    "sebagai pengecualian, sehingga cuma kode baru yang diperiksa.",
                    "",
                    "Tujuh jebakan yang paling sering terjadi:",
                    "  1. Method bertanda seru mengembalikan nil kalau nggak ada yang",
                    "     berubah. Jangan merangkai method bertanda seru.",
                    "  2. String bisa diubah. Kalau kamu mengoper string ke method lain",
                    "     yang menambahinya, string aslimu ikut berubah. Magic comment",
                    "     (komentar khusus) # frozen_string_literal: true di baris pertama",
                    "     berkas membuat semua literal string di berkas itu beku.",
                    "  3. Nilai bawaan hash yang berbagi objek. Hash.new([]) membuat satu",
                    "     array yang dikembalikan untuk setiap kunci yang belum ada, dan",
                    "     menambahinya nggak pernah menyimpannya ke hash. Yang benar adalah",
                    "     bentuk blok:",
                    "       Hash.new { |h, k| h[k] = [] }",
                    "  4. and dan or dikerjakan belakangan, bahkan sesudah =. Untuk logika,",
                    "     pakai && dan ||. Pakai and dan or cuma untuk alur seperti",
                    "     lakukan or abort.",
                    "  5. Integer dibagi Integer memotong sisanya.",
                    "  6. puts pada array mencetak tiap elemen di baris sendiri. Di Ruby",
                    "     versi sekarang, array kosong malah nggak mencetak apa pun, bahkan",
                    "     baris kosong pun nggak. Pakai p atau .inspect untuk melihat",
                    "     bentuk aslinya.",
                    "  7. Variabel class @@x dibagi dengan semua turunannya, jadi turunan",
                    "     bisa mengacaukan nilai milik induknya. Untuk kode baru, pakai",
                    "     variabel instance di level class.",
                ]
            },
            {
                "heading": "Melihat jebakannya sendiri",
                "code": """# frozen_string_literal: true

# ---- 1. Method ber-seru mengembalikan nil ----
a = "  sudah rapi  ".strip
b = "sudah rapi".dup.strip!   # .dup: salinan yang boleh diubah, literalnya beku
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

  def self.bersama=(v)
    @@bersama = v
  end
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
                    "  puts []        -> p []           -> []",
                    "  puts [1, [2]]  -> 1",
                    "  2",
                    "  ---",
                    "  @@bersama  Induk=diubah anak  Anak=diubah anak   <- ikut berubah",
                    "  @sendiri   Induk=induk  Anak=anak   <- terpisah",
                    "",
                    "Bagian ketiga adalah jebakan paling mahal di daftar ini. Lihat kunci=[]",
                    "pada hasil Hash.new([]): nggak satu pun kunci tersimpan di hash.",
                    "Hash.new([]) membuat satu array yang dikembalikan untuk setiap kunci",
                    "yang belum ada. salah[:a] << 1 menambah isi array bersama itu, tapi",
                    "nggak pernah menyimpannya ke hash. Makanya a dan b sama-sama [1, 2].",
                    "Bentuk blok membuat array baru untuk tiap kunci, lalu menyimpannya.",
                    "",
                    "Di bagian keempat, x = true and false membuat x bernilai true.",
                    "Penugasan x = true dikerjakan duluan, baru and false, dan hasil and itu",
                    "dibuang. Dengan &&, urutannya sesuai dugaan.",
                    "",
                    "Unary plus, yaitu tanda + di depan literal, membuat salinan string yang",
                    "nggak beku. Pasangannya unary minus (-), yang justru membekukan string",
                    "dan memakai ulang string lain yang isinya sama. Keduanya berguna di",
                    "berkas yang memakai magic comment frozen_string_literal.",
                    "",
                    "divmod mengembalikan hasil bagi dan sisanya sekaligus, dan fdiv",
                    "langsung membagi sebagai Float. Keduanya menunjukkan maksudmu lebih",
                    "jelas daripada to_f yang diselipkan di tengah ekspresi.",
                    "",
                    "Lihat juga baris puts []. puts dengan array kosong nggak mencetak apa",
                    "pun, bahkan baris baru pun nggak. Makanya tulisan p [] -> [] menyambung",
                    "langsung di belakang puts [] -> di baris yang sama.",
                    "",
                    "class << self di class Induk membuka tempat untuk menulis method milik",
                    "class itu sendiri. attr_accessor :sendiri di dalamnya membuat Induk dan",
                    "Anak masing-masing punya @sendiri yang terpisah, seperti terlihat di",
                    "baris terakhir keluaran.",
                    "",
                    "Untuk memeriksa kualitas kode secara otomatis:",
                    "",
                    "  rubocop                 gaya dan kebiasaan buruk",
                    "  ruby -w berkas.rb       peringatan bawaan Ruby",
                    "  bundle exec rspec       tes",
                    "  bundle audit            gem dengan celah keamanan",
                    "",
                    "bundle audit berasal dari gem bundler-audit, jadi gem itu perlu",
                    "dipasang dulu. Perintah ini mencocokkan versi gem di Gemfile.lock",
                    "dengan daftar celah keamanan yang sudah diketahui.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Di tim, kode biasanya diperiksa RuboCop dan dibaca rekan setim lewat code",
                    "review sebelum digabung. Jebakan di materi ini yang paling sering lolos",
                    "dari keduanya adalah yang nggak bikin program berhenti: programnya jalan,",
                    "laporannya keluar, tapi angkanya salah. Bug seperti itu biasanya",
                    "ditemukan pengguna, dan mencarinya butuh cara kerja yang runtut.",
                    "",
                    "Kasus kecil: laporan transaksi per kasir di minimarket kelihatan aneh.",
                    "Kode temanmu memakai per_kasir = Hash.new([]), lalu menambah \"TRX-01\"",
                    "untuk Sari dan \"TRX-02\" untuk Budi. Hasilnya per_kasir.keys kosong, dan",
                    "per_kasir[\"Sari\"] berisi dua transaksi.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Perkecil masalahnya sampai tinggal beberapa baris yang masih",
                    "     memunculkan bug-nya, yaitu dua kasir dan dua transaksi.",
                    "  2. Cetak dengan p, karena puts pada array menyembunyikan bentuk",
                    "     aslinya. Bandingkan dengan yang kamu harapkan. Kunci yang kosong",
                    "     berarti nilainya nggak pernah disimpan ke hash.",
                    "  3. Cocokkan gejalanya dengan daftar jebakan. Ini jebakan nomor 3, nilai",
                    "     bawaan yang dipakai bersama. Ganti dengan bentuk blok:",
                    "      per_kasir = Hash.new { |h, k| h[k] = [] }",
                    "      per_kasir[\"Sari\"] << \"TRX-01\"",
                    "      per_kasir[\"Budi\"] << \"TRX-02\"",
                    "      p per_kasir",
                    "  4. Hasilnya Sari cuma punya TRX-01 dan Budi cuma punya TRX-02. Tulis",
                    "     tes kecil untuk kasus ini supaya bug yang sama nggak balik lagi.",
                ]
            },
        ],
    },
    {
        "title": "21. Proyek Utuh: Menggabungkan Semuanya",
        "sections": [
            {
                "body": [
                    "Materi penutup ini menggabungkan class, module, Struct, Enumerable,",
                    "exception, dan pemisahan tanggung jawab dalam satu program utuh.",
                    "",
                    "Yang dibangun adalah sistem inventaris gudang, yaitu pencatat stok",
                    "barang yang masuk dan keluar. Fiturnya sederhana. Yang perlu kamu",
                    "perhatikan adalah cara bagian-bagiannya dipisah.",
                    "",
                    "Program ini dibagi jadi tiga lapisan, dengan panah ketergantungan satu",
                    "arah:",
                    "",
                    "  Antarmuka  ->  Layanan  ->  Model",
                    "",
                    "  MODEL     Barang, Gerak, dan keluarga galatnya.",
                    "            Tidak tahu apa-apa tentang layar.",
                    "  LAYANAN   Gudang dengan seluruh aturannya. Tidak",
                    "            pernah memanggil puts.",
                    "  ANTARMUKA memanggil layanan dan mencetak hasilnya.",
                    "            Tidak menghitung apa pun.",
                    "",
                    "Panah satu arah artinya antarmuka memakai layanan, layanan memakai",
                    "model, dan nggak pernah sebaliknya. Model nggak tahu ada layanan, dan",
                    "layanan nggak tahu ada layar.",
                    "",
                    "Cara mengujinya cukup satu pertanyaan: kalau program ini diubah jadi",
                    "aplikasi web dengan Sinatra, berapa banyak kode yang harus disentuh?",
                    "Jawaban yang benar: cuma bagian antarmuka. Sinatra adalah kerangka",
                    "aplikasi web kecil untuk Ruby.",
                    "",
                    "Di Ruby ada godaan khusus yang perlu dilawan. puts tersedia di mana aja",
                    "tanpa perlu memuat apa pun, jadi menyelipkannya ke dalam class layanan",
                    "terasa gampang sekali. Begitu itu terjadi, class-nya nggak bisa lagi",
                    "diuji tanpa membaca layar, dan nggak bisa dipakai di tempat lain.",
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
                    "Kalau dijalankan, program ini mencetak lima baris catatan gerak barang.",
                    "Tiga di antaranya ditolak: Adaptor yang stoknya cuma 4 diminta keluar",
                    "10, kode B09 yang nggak terdaftar, dan jumlah 0. Sesudah itu program",
                    "mencetak daftar barang, nilai persediaan 3115000, dan stok yang",
                    "menipis.",
                    "",
                    "Ada empat keputusan di program itu yang layak ditiru:",
                    "  1. Semua galat gudang mewarisi satu induk, yaitu GudangError.",
                    "     Antarmuka cukup menulis rescue GudangError sekali, dan tetap dapat",
                    "     pesan yang tepat untuk tiap kasus. Galat lain, yaitu bug yang",
                    "     sungguhan, tetap lolos dan kelihatan.",
                    "  2. include Enumerable ditambah satu each memberi Gudang method sum,",
                    "     select, sort_by, dan count. Nggak satu pun ditulis di class itu.",
                    "  3. each mengurutkan barang sebelum mengembalikannya. Hash di Ruby",
                    "     memang mempertahankan urutan penyisipan, tapi kalau kamu",
                    "     mengandalkannya, urutannya ikut berubah begitu ada barang yang",
                    "     dihapus lalu didaftarkan lagi. Urutan yang ditulis jelas bisa",
                    "     diuji.",
                    "  4. Gudang sama sekali nggak memanggil puts. Itu yang membuat semua",
                    "     aturannya bisa diuji dengan assert_equal tanpa membaca layar.",
                    "",
                    "Dua idiom Ruby yang muncul di program itu:",
                    "  - barang = @isi[kode] or raise ... bekerja karena or dikerjakan",
                    "    paling belakang, jadi penugasannya terjadi dulu. Kalau hasilnya",
                    "    nil, baru raise dijalankan. Idiom ini terbaca seperti kalimat:",
                    "    \"ambil barangnya, atau lempar error\".",
                    "  - def each(&) = @isi.values.sort_by(&:kode).each(&) memakai & polos",
                    "    untuk meneruskan blok tanpa memberinya nama. Bentuk ini ada sejak",
                    "    Ruby 3.1.",
                    "",
                    "Kalau kamu ingin melanjutkan proyek ini:",
                    "  - Simpan datanya ke JSON, dan sembunyikan caranya di balik sebuah",
                    "    module Penyimpan, supaya Gudang nggak tahu bentuk penyimpanannya.",
                    "  - Tambahkan CLI, yaitu perintah terminal, dengan OptionParser.",
                    "  - Tulis tes Minitest untuk Gudang. Ini bisa langsung dikerjakan tanpa",
                    "    mengubah satu baris pun, justru karena keputusan nomor 4.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Pembagian model, layanan, dan antarmuka seperti di program gudang ini",
                    "juga kamu temui di proyek Rails. Model ada di app/models, tampilan di",
                    "app/views, dan banyak tim menambah folder app/services untuk aturan",
                    "seperti isi class Gudang. Tiap fitur baru dimulai dengan pertanyaan yang",
                    "sama: kodenya masuk lapisan mana?",
                    "",
                    "Kasus kecil: pemilik gudang minta laporan pesan ulang. Untuk tiap barang",
                    "yang stoknya di bawah 10, hitung berapa yang perlu dipesan supaya stoknya",
                    "kembali jadi 30.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tentukan lapisannya. Hitungan pesan ulang adalah aturan, jadi masuk",
                    "     ke Gudang. Pencetakannya masuk ke antarmuka.",
                    "  2. Pakai yang sudah ada. stok_menipis sudah memilih barangnya, jadi",
                    "     method baru cukup mengubah hasilnya jadi kode dan jumlah pesanan:",
                    "      def pesan_ulang(batas: 10, target: 30)",
                    "        stok_menipis(batas).to_h { |b| [b.kode, target - b.stok] }",
                    "      end",
                    "  3. Kembalikan hash, dan jangan mencetaknya. Dengan data program di",
                    "     atas, hasilnya {\"B02\" => 26}, karena cuma Adaptor yang stoknya 4.",
                    "  4. Periksa pemanggilan yang nggak masuk akal, misalnya batas 40 dengan",
                    "     target 30. Barang berstok 35 bakal dapat pesanan -5. Tolak dengan",
                    "     raise ArgumentError di awal method kalau batas lebih besar dari",
                    "     target.",
                    "",
                    "Ingat: karena pesan_ulang nggak memanggil puts, tesnya cukup satu",
                    "assert_equal terhadap hash yang dikembalikan.",
                ]
            },
        ],
    },
]
