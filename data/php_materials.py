PHP_MATERIALS = [
    {
        "title": "1. Pengenalan PHP & Instalasi",
        "sections": [
            {
                "body": [
                    "PHP adalah bahasa pemrograman untuk bikin halaman web. Kodenya jalan",
                    "di server, yaitu komputer tempat situsnya disimpan. Yang dikirim ke",
                    "browser pengunjung cuma hasilnya, biasanya berupa HTML.",
                    "",
                    "Sedikit perkenalan:",
                    "  - PHP dibuat Rasmus Lerdorf tahun 1994. Awalnya cuma sekumpulan skrip",
                    "    untuk menghitung pengunjung halaman pribadinya.",
                    "  - Namanya singkatan rekursif, artinya singkatan yang memuat dirinya",
                    "    sendiri: PHP: Hypertext Preprocessor. Huruf P yang pertama itu",
                    "    singkatan dari PHP lagi.",
                    "  - PHP termasuk bahasa interpreted. Kamu langsung menjalankan",
                    "    berkasnya, tanpa harus mengompilasinya (menerjemahkannya jadi",
                    "    program siap jalan) lebih dulu. Tapi PHP nggak menjalankannya baris",
                    "    demi baris. Seluruh berkas diperiksa dulu, jadi satu kesalahan",
                    "    sintaks (salah tata tulis, misalnya titik koma yang hilang) di",
                    "    baris terakhir pun bikin seluruh berkas gagal jalan.",
                    "  - PHP termasuk dynamically typed. Tipe sebuah variabel ditentukan",
                    "    dari isinya waktu program jalan, jadi kamu nggak wajib",
                    "    menuliskannya. Tapi sejak PHP 7, tipe bisa ditulis secara",
                    "    eksplisit, dan sebaiknya memang ditulis.",
                    "",
                    "Dari awal, PHP dirancang untuk satu pekerjaan: menghasilkan halaman",
                    "web. Makanya PHP punya kemampuan yang nggak dimiliki bahasa lain: kode",
                    "PHP bisa disisipkan langsung di tengah HTML.",
                    "",
                    "Alasan PHP masih banyak dipakai sampai sekarang:",
                    "  - Sekitar tiga perempat situs web yang bahasa server-nya bisa",
                    "    dikenali memakai PHP.",
                    "  - WordPress, Laravel, Symfony, Drupal, dan Magento ditulis pakai PHP.",
                    "  - Hosting yang paling murah pun menyediakannya.",
                    "  - PHP 8 jauh lebih cepat dan jauh lebih ketat daripada PHP 5.",
                    "    Reputasi buruk PHP kebanyakan berasal dari zaman PHP 5.",
                    "",
                    "Hati-hati dengan tutorial lama. PHP 5 dan PHP 8 bedanya jauh, hampir",
                    "kayak dua bahasa yang berbeda. Kalau sebuah tutorial masih memakai",
                    "mysql_query(), ereg(), atau magic_quotes, tutorial itu ditulis lebih",
                    "dari sepuluh tahun lalu, dan sebagian kodenya udah dihapus dari PHP.",
                    "Materi ini memakai PHP 8.",
                    "",
                    "Cara memasang PHP:",
                    "  - Fedora  : sudo dnf install php-cli php-mbstring php-pdo",
                    "  - Debian  : sudo apt install php-cli php-mbstring php-sqlite3",
                    "  - macOS   : brew install php",
                    "  - Windows : unduh dari https://windows.php.net",
                    "  - Cek     : php --version",
                    "",
                    "sudo artinya perintah itu dijalankan dengan hak admin, jadi kamu bakal",
                    "diminta kata sandi. php-cli adalah PHP versi baris perintah, yang",
                    "dijalankan dari terminal. Dua paket lainnya dipakai materi berikutnya:",
                    "mbstring untuk menghitung huruf beraksen dengan benar (mb_strlen), dan",
                    "PDO + SQLite untuk materi database.",
                    "",
                    "Cara menjalankan:",
                    "  php berkas.php            jalankan skrip",
                    "  php -a                    mode interaktif",
                    "  php -l berkas.php         periksa sintaks saja",
                    "  php -S localhost:8000     server web bawaan",
                    "",
                    "Di mode interaktif, kamu mengetik kode PHP dan hasilnya langsung",
                    "keluar. php -l cuma memeriksa sintaks, tanpa menjalankan programnya.",
                    "Server web bawaan dipakai untuk mencoba halaman PHP di browser selama",
                    "belajar: jalankan perintahnya, lalu buka http://localhost:8000.",
                ]
            },
            {
                "heading": "Program pertama",
                "code": """<?php

echo "Halo Dunia!\\n";
echo "Aku sedang belajar PHP.\\n";"""
            },
            {
                "body": [
                    "Kita bahas program tadi bagian demi bagian:",
                    "",
                    "  <?php",
                    "    Tag pembuka. Semua yang ada di luar tag ini dikirim apa adanya",
                    "    sebagai teks. Yang ada di dalamnya dijalankan sebagai kode PHP.",
                    "",
                    "  echo",
                    "    Perintah untuk mencetak. echo itu konstruksi bahasa, artinya",
                    "    bagian dari tata bahasa PHP sendiri, jadi dia bukan fungsi biasa.",
                    "    Makanya echo nggak wajib pakai tanda kurung, dan bisa menerima",
                    "    beberapa nilai sekaligus: echo $a, $b, $c;",
                    "",
                    "  \\n",
                    "    Pindah baris. \\n cuma berlaku di dalam tanda kutip ganda. Di dalam",
                    "    kutip tunggal, \\n tercetak apa adanya sebagai dua karakter.",
                    "",
                    "  Titik koma",
                    "    Setiap pernyataan wajib diakhiri titik koma.",
                    "",
                    "Aturan: kalau isi berkasnya cuma kode PHP, tag penutup ?> sengaja",
                    "nggak ditulis. Ini bukan soal selera. Spasi atau baris kosong yang",
                    "nyelip sesudah ?> ikut terkirim ke browser. Akibatnya header HTTP",
                    "(keterangan yang dikirim server sebelum isi halaman) bisa rusak,",
                    "begitu juga berkas yang sedang diunduh pengunjung. PSR-12, standar",
                    "gaya penulisan kode yang dipakai luas di dunia PHP, juga melarang tag",
                    "penutup di berkas seperti ini.",
                    "",
                    "Untuk menyisipkan PHP di tengah HTML, bentuknya begini:",
                    "",
                    "  <h1><?= $judul ?></h1>",
                    "",
                    "<?= itu singkatan dari <?php echo. Di berkas campuran HTML dan PHP",
                    "seperti ini, tag penutup ?> memang dipakai, karena sesudahnya masih",
                    "ada HTML yang harus dikirim apa adanya.",
                    "",
                    "Komentar, yaitu catatan yang dilewati PHP waktu program jalan:",
                    "  // satu baris",
                    "  # satu baris juga, lebih jarang dipakai",
                    "  /* beberapa",
                    "     baris */",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Banyak situs sekolah, blog, dan toko online kecil memakai WordPress,",
                    "yang ditulis dengan PHP. Waktu pengunjung membuka halamannya, server",
                    "menjalankan berkas .php, lalu yang dikirim ke browser cuma HTML",
                    "hasilnya. Hosting murah yang biasa disewa UMKM umumnya sudah",
                    "menyediakan PHP, jadi berkasmu tinggal diunggah.",
                    "",
                    "Kasus kecil: wali kelas minta halaman jadwal piket yang bisa dibuka",
                    "teman sekelas lewat browser. Isinya judul, lalu piket hari Senin dan",
                    "Selasa.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tentukan keluarannya dulu. Yang sampai ke browser adalah HTML,",
                    "     jadi tiap baris jadwal dibungkus tag, misalnya <p>.",
                    "  2. Tulis satu echo per baris, lalu simpan sebagai piket.php:",
                    "      <?php",
                    "      echo \"<h1>Jadwal Piket XI RPL 1</h1>\\n\";",
                    "      echo \"<p>Senin: Andi, Budi</p>\\n\";",
                    "      echo \"<p>Selasa: Cici, Dedi</p>\\n\";",
                    "  3. Periksa tata tulisnya dengan php -l piket.php. Satu titik koma",
                    "     yang hilang di baris terakhir bikin seluruh berkas gagal jalan,",
                    "     termasuk dua baris yang sudah benar.",
                    "  4. Jalankan php -S localhost:8000 di folder itu, lalu buka",
                    "     http://localhost:8000/piket.php di browser.",
                    "",
                    "Jebakan: tanpa tag <p>, ketiga baris tampil menyambung di browser.",
                    "Tanda \\n cuma memindah baris di kode sumber halaman, sedangkan browser",
                    "menampilkan pindah baris itu sebagai spasi.",
                ]
            },
        ],
    },
    {
        "title": "2. Variabel & Tipe Data",
        "sections": [
            {
                "body": [
                    "Variabel adalah wadah bernama untuk menyimpan nilai. Di PHP, setiap",
                    "nama variabel diawali tanda dolar:",
                    "",
                    "  $nama = \"Andi\";",
                    "  $umur = 20;",
                    "  $tinggi = 172.5;",
                    "  $aktif = true;",
                    "",
                    "Kamu nggak perlu menulis tipenya. PHP menyimpulkannya sendiri dari",
                    "nilai yang diisikan.",
                    "",
                    "Huruf besar dan kecil di nama variabel dianggap beda: $nama dan $Nama",
                    "adalah dua variabel yang berbeda. Anehnya, nama fungsi dan kata kunci",
                    "justru nggak membedakan huruf besar-kecil. Itu warisan PHP lama, dan",
                    "sebaiknya nggak kamu manfaatkan.",
                    "",
                    "PHP punya delapan tipe data, dibagi jadi tiga golongan:",
                    "",
                    "  Skalar, isinya satu nilai",
                    "    int      bilangan bulat",
                    "    float    pecahan (disebut juga double)",
                    "    string   teks",
                    "    bool     true / false",
                    "",
                    "  Majemuk, isinya bisa banyak nilai",
                    "    array    daftar atau kamus, keduanya sekaligus",
                    "    object   instance dari sebuah class",
                    "",
                    "  Khusus",
                    "    null     tidak ada nilai",
                    "    resource pegangan ke sumber luar (berkas, koneksi)",
                    "",
                    "Array dan object punya materinya sendiri nanti, jadi untuk sekarang",
                    "cukup kenal namanya.",
                    "",
                    "Untuk memeriksa tipe sebuah nilai:",
                    "  gettype($x)          nama tipenya sebagai teks",
                    "  var_dump($x)         tipe dan nilainya, untuk debugging",
                    "  is_int($x)  is_float($x)  is_string($x)",
                    "  is_bool($x) is_array($x)  is_null($x)",
                    "",
                    "var_dump adalah alat paling berguna di PHP untuk debugging, yaitu",
                    "mencari tahu kenapa program nggak jalan sesuai harapan. Ia mencetak",
                    "tipe, panjang, dan isi sebuah nilai, termasuk isi array yang bersarang.",
                    "",
                    "Jangan pakai echo untuk memeriksa nilai yang bukan teks. echo pada",
                    "array cuma mencetak kata \"Array\" ditambah sebuah peringatan.",
                    "",
                    "Konstanta adalah nilai yang nggak bisa diubah sesudah ditetapkan:",
                    "  const PAJAK = 0.11;           di level berkas atau class",
                    "  define('SITUS', 'belajar');   bentuk lama, masih sah",
                    "",
                    "Nama konstanta nggak pakai tanda dolar, dan biasanya ditulis huruf",
                    "besar semua.",
                ]
            },
            {
                "heading": "Tipe dan konversi",
                "code": """<?php

$angka = 42;
$pecahan = 3.75;
$teks = "halo";
$benar = true;
$kosong = null;

printf("%-10s %-8s %s\\n", 'variabel', 'tipe', 'nilai');
printf("%-10s %-8s %s\\n", '$angka', gettype($angka), $angka);
printf("%-10s %-8s %s\\n", '$pecahan', gettype($pecahan), $pecahan);
printf("%-10s %-8s %s\\n", '$teks', gettype($teks), $teks);
printf("%-10s %-8s %s\\n", '$benar', gettype($benar), var_export($benar, true));
printf("%-10s %-8s %s\\n", '$kosong', gettype($kosong), var_export($kosong, true));

echo "---\\n";

// Konversi eksplisit
var_dump((int) "42 apel");
var_dump((float) "3.14");
var_dump((string) 99);
var_dump((bool) "0");
var_dump((bool) "false");"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  variabel   tipe     nilai",
                    "  $angka     integer  42",
                    "  $pecahan   double   3.75",
                    "  $teks      string   halo",
                    "  $benar     boolean  true",
                    "  $kosong    NULL     NULL",
                    "  ---",
                    "  int(42)",
                    "  float(3.14)",
                    "  string(2) \"99\"",
                    "  bool(false)",
                    "  bool(true)",
                    "",
                    "Bagian kedua programnya memakai konversi eksplisit, yaitu mengubah",
                    "tipe sebuah nilai dengan sengaja. Caranya, tulis tipe tujuan di dalam",
                    "kurung di depan nilainya, misalnya (int) atau (bool).",
                    "",
                    "Dua baris terakhir itu jebakan klasik PHP yang wajib kamu hafal:",
                    "",
                    "  (bool) \"0\"       -> FALSE",
                    "  (bool) \"false\"   -> TRUE",
                    "",
                    "Di PHP, nilai yang dianggap false cuma ini:",
                    "  false, 0, 0.0, \"\", \"0\", [], null",
                    "",
                    "Semua nilai lain dianggap true, termasuk string \"false\", string \"0.0\",",
                    "angka -1, dan array yang berisi satu elemen kosong. PHP nggak membaca",
                    "arti kata di dalam string. Buat PHP, sebuah string cuma dianggap false",
                    "kalau isinya kosong atau persis \"0\".",
                    "",
                    "Satu lagi dari keluarannya: gettype() menyebut float sebagai \"double\"",
                    "dan int sebagai \"integer\". Itu nama lama yang sengaja nggak diganti",
                    "supaya kode lama tetap jalan. Makanya, untuk ngecek float, pakai",
                    "is_float(), jangan membandingkan teks hasil gettype.",
                    "",
                    "(int) \"42 apel\" menghasilkan 42 tanpa keluhan sama sekali. Ini",
                    "memudahkan, tapi juga berbahaya: masukan pengguna yang setengah rusak",
                    "lolos tanpa ketahuan. Untuk memeriksa masukan dengan benar, pakai",
                    "filter_var:",
                    "",
                    "  $n = filter_var($masukan, FILTER_VALIDATE_INT);",
                    "  if ($n === false) { ... tidak sah ... }",
                    "",
                    "Dengan FILTER_VALIDATE_INT, filter_var mengembalikan false kalau",
                    "isinya bukan bilangan bulat yang utuh, jadi \"42 apel\" ditolak.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aplikasi kasir menyimpan harga sebagai int, nama barang sebagai string,",
                    "dan status lunas sebagai bool. Masalahnya, semua yang diketik orang di",
                    "form web sampai ke PHP sebagai string, termasuk kolom yang isinya",
                    "angka. Jadi sebelum dipakai menghitung, isian itu harus diperiksa dan",
                    "diubah tipenya dulu.",
                    "",
                    "Kasus kecil: petugas gudang mengisi hasil hitung ulang stok lewat form.",
                    "Isiannya bisa \"12\", \"12 dus\", kosong, atau \"0\" untuk barang yang habis.",
                    "Program harus menerima 12 dan 0, lalu menolak \"12 dus\" dan isian",
                    "kosong.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pahami masukannya: semuanya string, walaupun kelihatan seperti",
                    "     angka. Keluarannya int, atau tanda bahwa isiannya ditolak.",
                    "  2. Hindari (int) di sini. Hasil (int) \"12 dus\" adalah 12 tanpa keluhan",
                    "     apa pun, jadi salah ketik ikut tersimpan.",
                    "  3. Pakai filter_var dengan FILTER_VALIDATE_INT, lalu periksa hasilnya",
                    "     dengan ===:",
                    "      $stok = filter_var($masukan, FILTER_VALIDATE_INT);",
                    "      if ($stok === false) {",
                    "          echo \"Stok harus angka bulat.\\n\";",
                    "      }",
                    "  4. Uji kasus pinggir, yaitu masukan yang paling gampang bikin salah:",
                    "     \"0\". filter_var mengembalikan int(0), dan PHP menganggap 0 sebagai",
                    "     false. Kalau pemeriksaannya ditulis if (!$stok), barang yang memang",
                    "     habis malah ditolak.",
                ]
            },
        ],
    },
    {
        "title": "3. String & Interpolasi",
        "sections": [
            {
                "body": [
                    "String adalah teks. PHP punya empat cara menulis string.",
                    "",
                    "Kutip tunggal. Isinya dipakai apa adanya, jadi variabel di dalamnya",
                    "nggak diganti dengan nilainya. Cuma \\' dan \\\\ yang punya arti khusus.",
                    "  'Halo $nama'        -> Halo $nama   (tidak diganti!)",
                    "",
                    "Kutip ganda. Variabel di dalamnya diganti dengan nilainya. Proses ini",
                    "disebut interpolasi. Escape seperti \\n juga ikut berlaku. Escape",
                    "adalah kode pendek berawalan garis miring terbalik untuk menulis",
                    "karakter khusus, misalnya \\n untuk pindah baris.",
                    "  \"Halo $nama\"        -> Halo Andi",
                    "  \"Total: {$a[0]}\"    kurung kurawal untuk yang rumit",
                    "  \\n \\t \\\" \\\\ \\$ berlaku",
                    "",
                    "Heredoc. Sama seperti kutip ganda, tapi bisa beberapa baris.",
                    "    $teks = <<<EOT",
                    "    Halo $nama,",
                    "    ini beberapa baris.",
                    "    EOT;",
                    "",
                    "Nowdoc. Sama seperti kutip tunggal, tapi bisa beberapa baris.",
                    "    $teks = <<<'EOT'",
                    "    $nama tidak diganti di sini.",
                    "    EOT;",
                    "",
                    "Kamu mungkin pernah dengar kutip tunggal itu paling cepat. Di PHP",
                    "sekarang bedanya nggak kerasa, jadi pilih aja sesuai kebutuhan.",
                    "",
                    "Penanda penutup heredoc dan nowdoc (baris terakhir di contoh tadi)",
                    "juga menentukan indentasi, yaitu spasi di awal baris, yang dibuang",
                    "dari tiap baris. Fitur ini baru ada sejak PHP 7.3. Berkat fitur ini,",
                    "heredoc akhirnya enak dipakai di dalam fungsi atau method yang ditulis",
                    "menjorok.",
                    "",
                    "Untuk menyambung string, PHP memakai titik, bukan tanda plus:",
                    "  $a = \"Halo\" . \" \" . \"dunia\";",
                    "  $a .= \"!\";",
                    "",
                    "Ini sering menjebak orang yang datang dari JavaScript. Di PHP,",
                    "\"1\" + \"2\" menghasilkan angka 3, bukan teks \"12\".",
                    "",
                    "Fungsi string yang paling sering dipakai:",
                    "  strlen($s)                  panjang dalam byte",
                    "  mb_strlen($s)               panjang dalam karakter",
                    "  strtoupper / strtolower",
                    "  ucfirst / ucwords           huruf besar di awal",
                    "  trim / ltrim / rtrim",
                    "  substr($s, 2, 4)",
                    "  strpos($s, \"cari\")          posisi, atau false",
                    "  str_contains($s, \"cari\")    bool, sejak PHP 8",
                    "  str_starts_with / str_ends_with",
                    "  str_replace(\"a\", \"b\", $s)",
                    "  explode(\",\", $s)            teks -> array",
                    "  implode(\", \", $arr)         array -> teks",
                    "  str_repeat(\"-\", 20)",
                    "  str_pad($s, 10, \" \")",
                    "  sprintf / printf / number_format",
                    "",
                    "Beda strlen dan mb_strlen kelihatan di huruf beraksen. Huruf é",
                    "dihitung 2 oleh strlen karena butuh dua byte, tapi dihitung 1 oleh",
                    "mb_strlen.",
                ]
            },
            {
                "heading": "Menyusun teks dan tabel",
                "code": """<?php

$nama = "Andi";
$umur = 20;

echo 'Kutip tunggal: Halo $nama' . "\\n";
echo "Kutip ganda  : Halo $nama, umur $umur\\n";
echo "Kurung       : Halo {$nama}nya\\n";
echo "Sambung      : " . strtoupper($nama) . " (" . strlen($nama) . " huruf)\\n";

$teks = <<<EOT
Heredoc      : Halo $nama.
               Baris kedua ikut apa adanya.
EOT;
echo $teks . "\\n";

echo str_repeat("-", 42) . "\\n";

$barang = [
    ['Keyboard', 3, 350000],
    ['Mouse', 12, 85000],
    ['Monitor', 2, 1750000],
];

printf("%-12s%5s%15s\\n", 'Barang', 'Qty', 'Harga');
echo str_repeat("-", 32) . "\\n";

$total = 0;
foreach ($barang as [$nama_barang, $qty, $harga]) {
    $sub = $qty * $harga;
    $total += $sub;
    printf("%-12s%5d%15s\\n", $nama_barang, $qty, number_format($sub, 0, ',', '.'));
}

echo str_repeat("-", 32) . "\\n";
printf("%-12s%5s%15s\\n", 'TOTAL', '', number_format($total, 0, ',', '.'));"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  Kutip tunggal: Halo $nama",
                    "  Kutip ganda  : Halo Andi, umur 20",
                    "  Kurung       : Halo Andinya",
                    "  Sambung      : ANDI (4 huruf)",
                    "  Heredoc      : Halo Andi.",
                    "                 Baris kedua ikut apa adanya.",
                    "  ------------------------------------------",
                    "  Barang        Qty          Harga",
                    "  --------------------------------",
                    "  Keyboard        3      1.050.000",
                    "  Mouse          12      1.020.000",
                    "  Monitor         2      3.500.000",
                    "  --------------------------------",
                    "  TOTAL                  5.570.000",
                    "",
                    "{$nama}nya menunjukkan gunanya kurung kurawal. Tanpa kurung itu, PHP",
                    "mencari variabel bernama $namanya, padahal variabel itu nggak ada.",
                    "",
                    "foreach ($barang as [$a, $b, $c]) adalah destructuring array, yaitu",
                    "memecah tiap baris array jadi tiga variabel sekaligus. Bentuk kurung",
                    "siku seperti ini tersedia sejak PHP 7.1.",
                    "",
                    "number_format($n, 0, ',', '.') memakai titik sebagai pemisah ribuan",
                    "dan koma untuk desimal, sesuai format Indonesia. Kalau dua argumen",
                    "terakhir itu nggak ditulis, number_format memakai format Inggris, yaitu",
                    "koma untuk ribuan.",
                    "",
                    "Jebakan: strpos() mengembalikan 0 kalau teks yang dicari ketemu di",
                    "posisi paling awal, dan false kalau nggak ketemu. Di PHP, 0 == false,",
                    "jadi pengecekan if (!strpos(...)) salah: teks yang ketemu di awal ikut",
                    "dianggap nggak ketemu. Yang benar if (strpos(...) === false). Atau",
                    "lebih gampang lagi, pakai str_contains() yang ada sejak PHP 8.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Struk belanja, pesan konfirmasi pesanan, dan nomor invoice semuanya",
                    "string yang disusun program. Data mentahnya sering berantakan: nama",
                    "pelanggan diketik dengan spasi berlebih dan huruf besar acak, sedangkan",
                    "harga tersimpan sebagai angka polos 125000. Tugas PHP merapikannya jadi",
                    "teks yang enak dibaca, misalnya Rp125.000.",
                    "",
                    "Kasus kecil: toko online mau mencetak baris ringkasan pesanan.",
                    "Pelanggannya lupa mematikan Caps Lock, jadi namanya tersimpan sebagai",
                    "bUDI sANTOSO, lengkap dengan spasi lebih di depan dan belakang.",
                    "Totalnya 125000. Yang diminta: nama yang rapi di kolom selebar 15",
                    "karakter, lalu totalnya dalam format rupiah.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pecah jadi dua pekerjaan: merapikan nama, lalu memformat angka.",
                    "  2. Untuk nama, buang spasi di ujung dengan trim, kecilkan semua huruf",
                    "     dengan strtolower, baru besarkan huruf awal tiap kata dengan",
                    "     ucwords. Tanpa strtolower, huruf besar yang salah ketik tetap",
                    "     tertinggal.",
                    "  3. Untuk angka, pakai number_format dengan titik sebagai pemisah",
                    "     ribuan, lalu susun barisnya dengan printf:",
                    "      $nama = ucwords(strtolower(trim(\"  bUDI sANTOSO \")));",
                    "      $total = number_format(125000, 0, ',', '.');",
                    "      printf(\"%-15s Rp%s\\n\", $nama, $total);",
                    "     Hasilnya Budi Santoso, lalu Rp125.000 di kolom yang sama untuk",
                    "     setiap pelanggan.",
                    "  4. Coba nama beraksen seperti José. printf menghitung lebar dalam",
                    "     byte, dan é makan dua byte, jadi kolom Rp di baris itu bergeser",
                    "     satu karakter ke kiri.",
                ]
            },
        ],
    },
    {
        "title": "4. Operator & Perbandingan",
        "sections": [
            {
                "body": [
                    "Operator adalah simbol untuk mengolah nilai, misalnya menjumlah atau",
                    "membandingkan. Ini operator aritmetika, yaitu operator untuk berhitung:",
                    "  +  -  *  /  %  **",
                    "",
                    "** adalah pangkat: 2 ** 10 = 1024. % adalah sisa bagi: 7 % 2 = 1.",
                    "",
                    "Pembagian dengan / selalu menghasilkan float kalau hasilnya nggak",
                    "bulat. Jadi 7 / 2 = 3.5, nggak dipotong jadi 3 seperti di C, Java, dan",
                    "Go. Kalau kamu butuh pembagian bulat, pakai intdiv(7, 2), hasilnya 3.",
                    "",
                    "Operator penugasan mengisi atau mengubah isi variabel:",
                    "  =  +=  -=  *=  /=  %=  **=  .=",
                    "",
                    "$a += 5 sama dengan $a = $a + 5. Operator lain di baris itu bekerja",
                    "dengan cara yang sama, dan .= dipakai untuk menyambung teks.",
                    "",
                    "Operator naik dan turun:",
                    "  $i++    tambah 1",
                    "  $i--    kurangi 1",
                    "",
                    "Bagian terpenting di materi ini adalah perbandingan:",
                    "",
                    "  ==   sama nilainya setelah konversi tipe",
                    "  ===  sama nilainya dan sama tipenya",
                    "  !=   tidak sama nilainya",
                    "  !==  tidak sama nilai atau tipenya",
                    "  <  >  <=  >=",
                    "  <=>  spaceship: -1, 0, atau 1",
                    "",
                    "Konversi tipe artinya PHP mengubah salah satu nilai dulu supaya",
                    "tipenya sama, baru membandingkannya. Contohnya \"1\" == 1 bernilai true,",
                    "karena teks \"1\" diubah jadi angka 1 dulu. Sedangkan \"1\" === 1 bernilai",
                    "false, karena tipenya beda: yang satu string, yang satu int.",
                    "",
                    "Operator spaceship <=> menghasilkan -1 kalau nilai kiri lebih kecil, 0",
                    "kalau sama, dan 1 kalau nilai kiri lebih besar.",
                    "",
                    "Aturan praktis yang bakal menghemat banyak waktumu: biasakan pakai ===",
                    "dan !==. Pakai == cuma kalau kamu memang mau konversi tipenya terjadi,",
                    "dan kamu tahu persis aturannya.",
                    "",
                    "PHP 8 memperbaiki cara membandingkan angka dengan string, dan",
                    "perubahannya besar:",
                    "",
                    "              PHP 7     PHP 8",
                    "  0 == \"foo\"   true      false   <- diperbaiki",
                    "  \"1\" == \"01\"  true      true",
                    "  100 == \"1e2\" true      true",
                    "  0 == \"\"      true      false   <- diperbaiki",
                    "",
                    "\"1e2\" adalah cara menulis 1 kali 10 pangkat 2, yaitu 100.",
                    "",
                    "Baris pertama dulu pernah jadi celah keamanan sungguhan. Di PHP 7, kode",
                    "if ($password == 0) lolos untuk password apa pun yang bukan angka.",
                    "",
                    "Operator logika:",
                    "  &&  ||  !     dan bentuk kata: and  or  xor",
                    "",
                    "&& artinya \"dan\", || artinya \"atau\", dan ! membalik nilai: true jadi",
                    "false, false jadi true. xor bernilai true kalau tepat salah satu",
                    "sisinya true.",
                    "",
                    "Jangan campur bentuk simbol dengan bentuk kata. and dan or punya",
                    "prioritas lebih rendah daripada =, artinya PHP mengerjakan = lebih",
                    "dulu:",
                    "  $x = true and false;   -> $x bernilai TRUE",
                    "  $x = true && false;    -> $x bernilai FALSE",
                    "",
                    "Di baris pertama, $x diisi true dulu. Sesudah itu baru hasilnya di-and",
                    "dengan false, dan hasil itu dibuang. Makanya biasakan pakai && dan ||.",
                    "",
                    "Operator khas PHP:",
                    "  ?:    Elvis: $a ?: 'bawaan'   pakai $a kalau truthy",
                    "  ??    null coalescing: $a ?? 'bawaan'",
                    "  ??=   isi hanya kalau null",
                    "  ?->   panggil hanya kalau bukan null (PHP 8)",
                    "",
                    "Truthy artinya dianggap true, misalnya angka selain 0 atau teks yang",
                    "nggak kosong. ?? memakai nilai di kirinya kalau nilai itu ada dan",
                    "bukan null. Kalau nggak, ?? memakai nilai di kanannya.",
                    "",
                    "Beda ?: dan ?? itu penting. ?: memunculkan peringatan kalau",
                    "variabelnya belum ada, sedangkan ?? nggak. Jadi untuk membaca $_GET",
                    "(data dari alamat URL, dibahas di materi PHP untuk Web) atau array yang",
                    "belum tentu punya kunci tertentu, pakai ??.",
                ]
            },
            {
                "heading": "Melihat perbandingan bekerja",
                "code": """<?php

function uji(string $label, bool $hasil): void
{
    printf("%-22s %s\\n", $label, $hasil ? 'true' : 'false');
}

echo "== (longgar, dengan konversi)\\n";
uji('0 == "foo"', 0 == "foo");
uji('"1" == "01"', "1" == "01");
uji('100 == "1e2"', 100 == "1e2");
uji('"abc" == 0', "abc" == 0);
uji('null == false', null == false);

echo "\\n=== (ketat, tipe harus sama)\\n";
uji('1 === "1"', 1 === "1");
uji('1 === 1', 1 === 1);
uji('null === false', null === false);

echo "\\n?? dan ?:\\n";
$data = ['nama' => 'Andi', 'kota' => null];
echo 'nama  : ' . ($data['nama'] ?? 'tidak ada') . "\\n";
echo 'kota  : ' . ($data['kota'] ?? 'tidak ada') . "\\n";
echo 'email : ' . ($data['email'] ?? 'tidak ada') . "\\n";

echo "\\naritmetika\\n";
echo '7 / 2      = ' . (7 / 2) . "\\n";
echo 'intdiv(7,2) = ' . intdiv(7, 2) . "\\n";
echo '7 % 2      = ' . (7 % 2) . "\\n";
echo '2 ** 10    = ' . (2 ** 10) . "\\n";
echo '5 <=> 3    = ' . (5 <=> 3) . "\\n";"""
            },
            {
                "body": [
                    "Keluaran di PHP 8:",
                    "  == (longgar, dengan konversi)",
                    "  0 == \"foo\"             false",
                    "  \"1\" == \"01\"            true",
                    "  100 == \"1e2\"           true",
                    "  \"abc\" == 0             false",
                    "  null == false          true",
                    "",
                    "  === (ketat, tipe harus sama)",
                    "  1 === \"1\"              false",
                    "  1 === 1                true",
                    "  null === false         false",
                    "",
                    "  ?? dan ?:",
                    "  nama  : Andi",
                    "  kota  : tidak ada",
                    "  email : tidak ada",
                    "",
                    "  aritmetika",
                    "  7 / 2      = 3.5",
                    "  intdiv(7,2) = 3",
                    "  7 % 2      = 1",
                    "  2 ** 10    = 1024",
                    "  5 <=> 3    = 1",
                    "",
                    "Lihat baris kota. $data['kota'] ada di array, tapi isinya null, dan ??",
                    "tetap memberi nilai bawaan. Memang begitu cara kerjanya: ?? ngecek",
                    "\"null atau nggak ada\", bukan \"ada atau nggak ada\". Kalau kamu perlu",
                    "membedakan keduanya, pakai array_key_exists().",
                    "",
                    "Operator spaceship <=> sering dipakai di fungsi pembanding untuk usort,",
                    "yaitu fungsi untuk mengurutkan array. Satu baris ini menggantikan tiga",
                    "baris if:",
                    "",
                    "  usort($data, fn($a, $b) => $a['nilai'] <=> $b['nilai']);",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Fitur bagi tagihan di aplikasi patungan menghitung bagian tiap orang",
                    "dengan pembagian bulat dan sisa bagi. Toko grosir memakai hitungan yang",
                    "sama untuk tahu berapa dus penuh dan berapa barang eceran dari stok",
                    "yang ada. Dua-duanya butuh hasil bulat, karena nggak ada orang yang",
                    "bisa membayar sepertiga rupiah.",
                    "",
                    "Kasus kecil: tagihan makan bareng Rp250.000 dibagi rata ke 3 orang.",
                    "Tiap orang harus membayar angka bulat, dan sisanya dicatat supaya",
                    "totalnya tetap pas.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Masukannya dua int, yaitu total dan jumlah orang. Keluarannya juga",
                    "     dua int: bayar per orang dan sisanya.",
                    "  2. Pakai intdiv untuk bagian bulat, dan % untuk sisanya:",
                    "      $total = 250000;",
                    "      $orang = 3;",
                    "      $per = intdiv($total, $orang);",
                    "      $sisa = $total % $orang;",
                    "      echo \"$per per orang, sisa $sisa\\n\";",
                    "     Hasilnya 83333 per orang, sisa 1.",
                    "  3. Cek dengan membalik hitungannya: 83333 kali 3 ditambah 1 harus",
                    "     kembali jadi 250000.",
                    "  4. Periksa kasus pinggir: jumlah orang 0. intdiv(250000, 0)",
                    "     menghentikan program dengan DivisionByZeroError, jadi pastikan",
                    "     jumlah orang minimal 1 sebelum menghitung.",
                    "",
                    "Jebakan: $total / $orang menghasilkan 83333.333333333, pecahan yang",
                    "nggak bisa dibayar dengan uang rupiah.",
                ]
            },
        ],
    },
    {
        "title": "5. Percabangan & Perulangan",
        "sections": [
            {
                "body": [
                    "Percabangan artinya program memilih jalan berdasarkan sebuah kondisi:",
                    "",
                    "  if ($nilai >= 75) {",
                    "      echo \"Lulus\";",
                    "  } elseif ($nilai >= 60) {",
                    "      echo \"Mengulang\";",
                    "  } else {",
                    "      echo \"Tidak Lulus\";",
                    "  }",
                    "",
                    "Kata elseif ditulis nyambung. else if (dua kata) juga sah di PHP,",
                    "kecuali di dalam sintaks alternatif (elseif: ... endif). Jadi pakai",
                    "yang satu kata aja supaya konsisten.",
                    "",
                    "Sintaks alternatif biasa dipakai di template HTML, yaitu berkas HTML",
                    "yang disisipi PHP:",
                    "",
                    "  <?php if ($login): ?>",
                    "      <p>Halo, <?= $nama ?></p>",
                    "  <?php else: ?>",
                    "      <a href=\"/masuk\">Masuk</a>",
                    "  <?php endif; ?>",
                    "",
                    "Di tengah HTML, bentuk ini jauh lebih gampang dibaca daripada kurung",
                    "kurawal yang tersebar di antara tag.",
                    "",
                    "switch membandingkan satu nilai dengan beberapa kemungkinan. Setiap",
                    "case yang punya isi wajib diakhiri break:",
                    "",
                    "  switch ($hari) {",
                    "      case 1:",
                    "      case 2:",
                    "          echo \"Awal pekan\"; break;",
                    "      case 6:",
                    "          echo \"Sabtu\"; break;",
                    "      default:",
                    "          echo \"Hari lain\";",
                    "  }",
                    "",
                    "Tanpa break, PHP lanjut menjalankan case di bawahnya. Kejadian ini",
                    "disebut fall-through. Di contoh tadi, case 1 sengaja dibiarkan kosong",
                    "supaya hari 1 dan hari 2 sama-sama mencetak \"Awal pekan\".",
                    "",
                    "Jebakan: switch memakai perbandingan longgar (==). Di PHP 7, switch(0)",
                    "cocok dengan case berisi teks apa pun yang bukan angka, misalnya",
                    "case \"apa pun\". PHP 8 sudah memperbaikinya, tapi lebih aman",
                    "membiasakan diri pakai match.",
                    "",
                    "match (PHP 8) lebih baik daripada switch di semua sisi:",
                    "",
                    "  $grade = match(true) {",
                    "      $nilai >= 85 => 'A',",
                    "      $nilai >= 75 => 'B',",
                    "      default => 'C',",
                    "  };",
                    "",
                    "Bedanya dari switch:",
                    "  1. match adalah ekspresi, artinya dia menghasilkan nilai yang bisa",
                    "     langsung disimpan ke variabel.",
                    "  2. Perbandingannya ketat (===).",
                    "  3. Nggak ada fall-through, jadi nggak perlu break.",
                    "  4. Kalau nggak ada yang cocok dan nggak ada default, match",
                    "     memunculkan error UnhandledMatchError. Jadi kesalahannya",
                    "     kelihatan, nggak lewat begitu aja.",
                    "",
                    "Perulangan artinya menjalankan kode yang sama berulang kali:",
                    "  for ($i = 0; $i < 5; $i++) { ... }",
                    "  while ($n > 0) { ... }",
                    "  do { ... } while ($n > 0);",
                    "  foreach ($arr as $nilai) { ... }",
                    "  foreach ($arr as $kunci => $nilai) { ... }",
                    "",
                    "for dipakai kalau jumlah putarannya jelas. while berputar selama",
                    "kondisinya benar. do ... while mirip while, tapi isinya dijalankan",
                    "minimal sekali. foreach menelusuri isi array satu per satu, bisa",
                    "sekalian dengan kuncinya.",
                    "",
                    "break 2 keluar dari dua tingkat perulangan sekaligus, dan angkanya",
                    "boleh diganti sesuai kebutuhan. continue 2 melompat ke putaran",
                    "berikutnya dari perulangan dua tingkat di luarnya. Bentuk berangka",
                    "seperti ini nggak ada di C# atau Java. Java memakai label untuk",
                    "keperluan yang sama.",
                ]
            },
            {
                "heading": "match, foreach, dan perulangan bersarang",
                "code": """<?php

function grade(int $nilai): string
{
    return match (true) {
        $nilai >= 85 => 'A',
        $nilai >= 75 => 'B',
        $nilai >= 60 => 'C',
        $nilai >= 40 => 'D',
        default => 'E',
    };
}

foreach ([92, 78, 65, 45, 12] as $n) {
    printf("%3d -> %s\\n", $n, grade($n));
}

echo "---\\n";

// match dengan nilai, bukan true
foreach (['GET', 'POST', 'PATCH'] as $metode) {
    $arti = match ($metode) {
        'GET' => 'membaca',
        'POST', 'PUT' => 'menulis',
        'DELETE' => 'menghapus',
        default => 'tidak dikenal',
    };
    printf("%-6s -> %s\\n", $metode, $arti);
}

echo "---\\n";

// foreach dengan kunci
$stok = ['kabel' => 10, 'adaptor' => 4, 'mouse' => 25];
foreach ($stok as $barang => $jumlah) {
    $tanda = $jumlah < 10 ? ' (menipis)' : '';
    printf("%-10s %3d%s\\n", $barang, $jumlah, $tanda);
}

echo "---\\n";

// break bertingkat
for ($i = 1; $i <= 20; $i++) {
    for ($j = 1; $j <= 20; $j++) {
        if ($i * $j === 143) {
            echo "143 = $i x $j\\n";
            break 2;          // keluar dari KEDUA perulangan
        }
    }
}"""
            },
            {
                "body": [
                    "Keluaran:",
                    "   92 -> A",
                    "   78 -> B",
                    "   65 -> C",
                    "   45 -> D",
                    "   12 -> E",
                    "  ---",
                    "  GET    -> membaca",
                    "  POST   -> menulis",
                    "  PATCH  -> tidak dikenal",
                    "  ---",
                    "  kabel       10",
                    "  adaptor      4 (menipis)",
                    "  mouse       25",
                    "  ---",
                    "  143 = 11 x 13",
                    "",
                    "match(true) adalah cara lazim menulis rantai kondisi. Tiap lengan,",
                    "yaitu tiap baris kondisi => hasil, dibandingkan dengan true. Lengan",
                    "pertama yang kondisinya benar itulah yang dipakai.",
                    "",
                    "'POST', 'PUT' => ... menangani beberapa nilai dalam satu lengan. Ini",
                    "padanan beberapa case yang ditumpuk di switch, tapi tanpa risiko",
                    "fall-through yang nggak disengaja.",
                    "",
                    "Jebakan: foreach dengan referensi bisa merusak isi array tanpa kamu",
                    "sadari. Ini salah satu bug paling mahal di PHP:",
                    "",
                    "  foreach ($arr as &$x) { $x *= 2; }",
                    "  foreach ($arr as $x) { ... }        <- BUG",
                    "",
                    "Tanda & membuat $x jadi referensi, yaitu nama lain untuk elemen array",
                    "itu sendiri. Jadi mengubah $x berarti mengubah isi array. Masalahnya,",
                    "sesudah perulangan pertama selesai, $x masih jadi referensi ke elemen",
                    "terakhir. Perulangan kedua lalu mengisi $x berulang kali, dan setiap",
                    "pengisian ikut menimpa elemen terakhir. Hasilnya, elemen terakhir",
                    "berisi nilai elemen kedua dari belakang. Bug ini terkenal, dan susah",
                    "dilihat.",
                    "",
                    "Pencegahnya cuma satu baris: tulis unset($x); sesudah setiap foreach",
                    "yang memakai referensi.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Promo minimarket seperti \"diskon 10% untuk belanja minimal Rp100.000\"",
                    "adalah percabangan: program memilih potongan berdasarkan total belanja.",
                    "Perulangan muncul waktu aturan itu dijalankan ke ratusan transaksi",
                    "sekaligus, misalnya saat rekap harian ditutup malam hari.",
                    "",
                    "Kasus kecil: belanja minimal Rp100.000 dapat diskon 10%, minimal",
                    "Rp50.000 dapat 5%, dan di bawahnya nggak dapat diskon. Hari ini ada",
                    "tiga transaksi: 45000, 50000, dan 120000.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Masukannya daftar total belanja. Keluarannya persen diskon untuk",
                    "     tiap transaksi.",
                    "  2. Pakai foreach untuk menelusuri daftarnya, karena jumlah",
                    "     transaksinya berubah setiap hari.",
                    "  3. Untuk memilih persen, pakai match(true), dan tulis syarat yang",
                    "     angkanya paling besar lebih dulu:",
                    "      $persen = match (true) {",
                    "          $belanja >= 100000 => 10,",
                    "          $belanja >= 50000 => 5,",
                    "          default => 0,",
                    "      };",
                    "  4. Uji angka yang tepat di batas, yaitu 50000. Dengan >=, transaksi",
                    "     itu dapat 5%, sesuai kata \"minimal\" di brosurnya. Dengan >,",
                    "     pelanggan yang belanja pas Rp50.000 nggak dapat apa-apa. Hasil",
                    "     ketiga transaksi: 0%, 5%, dan 10%.",
                    "",
                    "Ingat: urutan lengan match menentukan hasilnya. Kalau syarat >= 50000",
                    "ditulis paling atas, belanja 120000 berhenti di lengan itu dan cuma",
                    "dapat 5%.",
                ]
            },
        ],
    },
    {
        "title": "6. Array: Daftar dan Kamus Sekaligus",
        "sections": [
            {
                "body": [
                    "Array PHP beda dari array di hampir semua bahasa lain. Satu tipe array",
                    "bisa berperan sebagai daftar bernomor sekaligus kamus berkunci. Di",
                    "balik layar, array PHP selalu berupa peta terurut, yaitu kumpulan",
                    "pasangan kunci dan nilai yang urutannya dijaga.",
                    "",
                    "  $daftar = [10, 20, 30];",
                    "  $kamus = ['nama' => 'Andi', 'umur' => 20];",
                    "  $campur = [0 => 'a', 'x' => 'b', 5 => 'c'];",
                    "",
                    "Di $daftar, kuncinya otomatis 0, 1, dan 2. Di $kamus, kuncinya 'nama'",
                    "dan 'umur'. Tanda => memasangkan kunci dengan nilainya.",
                    "",
                    "Kunci boleh berupa int atau string. Kunci string yang isinya angka,",
                    "misalnya \"5\", otomatis diubah jadi int. true jadi 1, false jadi 0, dan",
                    "null jadi \"\".",
                    "",
                    "Menambah dan mengubah isi:",
                    "  $a[] = 'baru';            tambah di akhir",
                    "  $a['kunci'] = 'nilai';",
                    "  array_push($a, 'x', 'y');",
                    "  unset($a[2]);             hapus satu elemen",
                    "",
                    "Jebakan: unset nggak menomori ulang array. Sesudah index 1 dihapus",
                    "dari [0,1,2], yang tersisa index 0 dan 2. Akibatnya json_encode, fungsi",
                    "yang mengubah array jadi teks JSON, menghasilkan objek JSON, bukan",
                    "array. Pakai array_values($a) untuk menomori ulang.",
                    "",
                    "Fungsi array yang paling sering dipakai:",
                    "  count($a)                     jumlah elemen",
                    "  in_array($x, $a)              apakah nilai ada",
                    "  array_search($x, $a)          kunci dari nilai, atau false",
                    "  array_key_exists($k, $a)      apakah kunci ada",
                    "  array_keys($a) / array_values($a)",
                    "  array_merge($a, $b)           gabung",
                    "  array_slice($a, 1, 3)",
                    "  array_unique($a)",
                    "  array_reverse($a)",
                    "  array_sum($a) / array_product($a)",
                    "  array_fill(0, 5, 0)",
                    "  range(1, 10)",
                    "  array_combine($kunci, $nilai)",
                    "  array_count_values($a)        hitung frekuensi",
                    "  array_column($a, 'nama')      ambil satu kolom",
                    "",
                    "Fungsi tingkat tinggi, yaitu fungsi yang menerima fungsi lain sebagai",
                    "argumen (nilai yang dikirim ke fungsi):",
                    "  array_map(fn($x) => $x * 2, $a)",
                    "  array_filter($a, fn($x) => $x > 5)",
                    "  array_reduce($a, fn($c, $x) => $c + $x, 0)",
                    "",
                    "array_map mengubah tiap elemen, array_filter menyaring elemen, dan",
                    "array_reduce meringkas semua elemen jadi satu nilai. Bentuk",
                    "fn($x) => ... adalah fungsi pendek yang nanti dibahas di materi Fungsi",
                    "& Tipe.",
                    "",
                    "Jebakan: array_filter mempertahankan kunci aslinya. Hasil saringannya,",
                    "misalnya [0=>1, 2=>3], bukan lagi array yang nomornya berurutan.",
                    "Bungkus dengan array_values kalau urutan nomornya penting.",
                ]
            },
            {
                "heading": "Mengolah array",
                "code": """<?php

$nilai = [78, 92, 65, 88, 71, 95, 59, 83];

echo 'Data      : ' . implode(', ', $nilai) . "\\n";

$urut = $nilai;
sort($urut);
echo 'Terurut   : ' . implode(', ', $urut) . "\\n";
echo 'Jumlah    : ' . count($nilai) . "\\n";
echo 'Total     : ' . array_sum($nilai) . "\\n";
printf("Rata-rata : %.2f\\n", array_sum($nilai) / count($nilai));
echo 'Tertinggi : ' . max($nilai) . "\\n";
echo 'Terendah  : ' . min($nilai) . "\\n";

$rata = array_sum($nilai) / count($nilai);
$diAtas = array_values(array_filter($nilai, fn($n) => $n > $rata));
echo 'Di atas rata-rata: ' . implode(', ', $diAtas) . "\\n";

echo "---\\n";

$murid = [
    ['nama' => 'Andi', 'kelas' => 'A', 'nilai' => 88],
    ['nama' => 'Budi', 'kelas' => 'B', 'nilai' => 72],
    ['nama' => 'Cici', 'kelas' => 'A', 'nilai' => 95],
];

echo 'Nama      : ' . implode(', ', array_column($murid, 'nama')) . "\\n";

$lulus = array_filter($murid, fn($m) => $m['nilai'] >= 75);
echo 'Lulus     : ' . count($lulus) . "\\n";

usort($murid, fn($a, $b) => $b['nilai'] <=> $a['nilai']);
foreach ($murid as $m) {
    printf("%-6s %s %3d\\n", $m['nama'], $m['kelas'], $m['nilai']);
}

echo "---\\n";
$kata = explode(' ', 'kucing makan ikan kucing tidur ikan kucing');
$hitung = array_count_values($kata);
arsort($hitung);
foreach ($hitung as $k => $n) {
    printf("%-7s: %d\\n", $k, $n);
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
                    "  Nama      : Andi, Budi, Cici",
                    "  Lulus     : 2",
                    "  Cici   A  95",
                    "  Andi   A  88",
                    "  Budi   B  72",
                    "  ---",
                    "  kucing : 3",
                    "  ikan   : 2",
                    "  makan  : 1",
                    "  tidur  : 1",
                    "",
                    "PHP punya banyak fungsi pengurutan, tapi namanya mengikuti pola.",
                    "Begitu polanya ketahuan, gampang diingat:",
                    "",
                    "  sort     urut nilai naik, kunci dibuang",
                    "  rsort    urut nilai turun, kunci dibuang",
                    "  asort    urut nilai naik, kunci dipertahankan",
                    "  arsort   urut nilai turun, kunci dipertahankan",
                    "  ksort    urut kunci naik",
                    "  krsort   urut kunci turun",
                    "  usort    urut dengan fungsi sendiri, kunci dibuang",
                    "  uasort   sama, kunci dipertahankan",
                    "  uksort   urut kunci dengan fungsi sendiri",
                    "",
                    "Arti huruf awalannya: a = associative (kunci dijaga), k = key,",
                    "r = reverse, u = user-defined (pakai fungsi buatanmu sendiri). Di kode",
                    "tadi, arsort mengurutkan hitungan kata dari yang terbanyak, dan",
                    "kuncinya, yaitu katanya, tetap terjaga.",
                    "",
                    "Ingat: semua fungsi ini mengubah array aslinya dan mengembalikan bool,",
                    "bukan array baru. Jadi $b = sort($a); adalah kesalahan yang sering",
                    "terjadi: isi $b cuma true.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Warung kopi yang memakai aplikasi kasir sederhana menyimpan pesanan",
                    "hari ini sebagai daftar nama menu. Di akhir hari, pemiliknya ingin tahu",
                    "menu mana yang paling laku untuk menentukan belanja bahan besok. Rekap",
                    "seperti ini, juga rekap absensi dan nilai rapor, hampir selalu berupa",
                    "array yang dihitung, disaring, lalu diurutkan.",
                    "",
                    "Kasus kecil: pesanan hari ini tercatat sebagai kopi, teh, kopi, roti,",
                    "kopi, teh. Menu apa yang paling laku, dan berapa kali dipesan?",
                    "",
                    "Cara memecahkannya:",
                    "  1. Masukannya daftar bernomor berisi nama menu. Keluarannya satu nama",
                    "     menu dan satu angka.",
                    "  2. Ubah daftar itu jadi kamus hitungan dengan array_count_values.",
                    "     Isinya kopi 3, teh 2, dan roti 1.",
                    "  3. Urutkan dari yang terbanyak dengan arsort, supaya kuncinya, yaitu",
                    "     nama menu, tetap terjaga. Kunci pertama sesudahnya adalah jawaban:",
                    "      $pesanan = ['kopi', 'teh', 'kopi', 'roti', 'kopi', 'teh'];",
                    "      $hitung = array_count_values($pesanan);",
                    "      arsort($hitung);",
                    "      $teratas = array_keys($hitung)[0];",
                    "      echo \"$teratas: {$hitung[$teratas]} kali\\n\";",
                    "     Hasilnya kopi: 3 kali.",
                    "  4. Pikirkan kasus seri, misalnya teh dan roti sama-sama 2 kali. Sejak",
                    "     PHP 8, arsort mempertahankan urutan asli untuk nilai yang sama, jadi",
                    "     yang lebih dulu dipesan menang. Kalau semua menu teratas harus",
                    "     disebut, saring dengan array_filter: ambil yang hitungannya sama",
                    "     dengan max($hitung).",
                    "",
                    "Jebakan: tulis arsort($hitung) di barisnya sendiri. Kalau ditulis",
                    "$urut = arsort($hitung), isi $urut cuma true.",
                ]
            },
        ],
    },
    {
        "title": "7. Fungsi & Tipe",
        "sections": [
            {
                "body": [
                    "Fungsi adalah kumpulan perintah yang diberi nama, supaya bisa dipanggil",
                    "berulang kali. Bentuk dasarnya:",
                    "",
                    "  function tambah($a, $b) {",
                    "      return $a + $b;",
                    "  }",
                    "",
                    "$a dan $b disebut parameter, yaitu nilai yang diterima fungsi. Nilai",
                    "yang kamu kirim waktu memanggilnya, misalnya tambah(2, 3), disebut",
                    "argumen. return mengembalikan hasilnya ke pemanggil.",
                    "",
                    "Sekarang versi yang memakai tipe. Tipe seperti ini yang membedakan PHP",
                    "modern dari PHP lama:",
                    "",
                    "  function tambah(int $a, int $b): int {",
                    "      return $a + $b;",
                    "  }",
                    "",
                    "int di depan $a dan $b adalah tipe parameternya. Tulisan : int sesudah",
                    "tanda kurung adalah tipe nilai yang dikembalikan.",
                    "",
                    "Tipe yang bisa ditulis: int, float, string, bool, array, callable,",
                    "iterable, object, mixed, void, never, self, static, dan nama class apa",
                    "pun.",
                    "",
                    "  ?int          int atau null",
                    "  int|string    salah satu (union, PHP 8)",
                    "  Countable&Iterator  keduanya (intersection, PHP 8.1)",
                    "",
                    "Beberapa yang perlu dijelaskan:",
                    "  - void: fungsinya nggak mengembalikan apa-apa.",
                    "  - mixed: boleh tipe apa pun.",
                    "  - callable: sesuatu yang bisa dipanggil seperti fungsi.",
                    "  - never: fungsinya nggak pernah selesai dengan normal, misalnya",
                    "    karena selalu menghentikan program.",
                    "",
                    "Mode ketat dinyalakan dengan satu baris ini:",
                    "",
                    "  declare(strict_types=1);",
                    "",
                    "Tanpa baris itu, tambah(\"5\", \"3\") tetap diterima. PHP mengubah \"5\" dan",
                    "\"3\" jadi angka tanpa bilang apa-apa, lalu hasilnya 8. Dengan baris itu,",
                    "PHP menolaknya dan melempar TypeError. Melempar (throw) artinya",
                    "memunculkan error yang menghentikan program, kecuali error itu",
                    "ditangkap dengan try dan catch. Soal ini nanti dibahas lengkap di",
                    "materi Exception & Penanganan Galat.",
                    "",
                    "Biasakan menulis baris ini di setiap berkas PHP baru. Letaknya harus",
                    "jadi pernyataan pertama, tepat sesudah <?php. Mode ketat cuma berlaku",
                    "untuk berkas yang menulisnya.",
                    "",
                    "Parameter bawaan dan variadic:",
                    "  function sapa(string $nama, string $salam = 'Halo')",
                    "  function total(int ...$angka)      terima berapa pun",
                    "",
                    "Parameter bawaan dipakai kalau argumennya nggak diisi: sapa('Andi')",
                    "otomatis memakai 'Halo'. Parameter variadic, yang ditandai tiga titik,",
                    "menerima berapa pun argumen.",
                    "",
                    "Argumen bernama (PHP 8):",
                    "  sapa(salam: 'Hai', nama: 'Andi');",
                    "",
                    "Dengan argumen bernama, urutan argumen boleh ditukar, dan maksudnya",
                    "jadi jelas. Bandingkan dua panggilan ini:",
                    "  buat(true, false, true)",
                    "  buat(tebal: true, miring: false, garisBawah: true)",
                    "",
                    "Yang pertama nggak menjelaskan apa-apa. Yang kedua langsung jelas",
                    "maksudnya.",
                    "",
                    "Closure dan arrow function adalah fungsi tanpa nama yang bisa disimpan",
                    "di variabel:",
                    "  $kali = function ($x) use ($faktor) { return $x * $faktor; };",
                    "  $kali = fn($x) => $x * $faktor;",
                    "",
                    "Bedanya penting. function butuh use untuk mengambil variabel dari luar.",
                    "fn menangkapnya otomatis, dan yang diambil selalu salinan nilainya,",
                    "bukan referensinya. Arrow function cuma boleh berisi satu ekspresi.",
                    "",
                    "Lingkup variabel, yaitu dari mana saja sebuah variabel bisa dipakai, di",
                    "PHP itu ketat. Fungsi sama sekali nggak bisa melihat variabel di",
                    "luarnya, termasuk variabel global, kecuali lewat use, parameter, atau",
                    "kata kunci global. Ini beda dari JavaScript dan Python.",
                ]
            },
            {
                "heading": "Fungsi bertipe ketat",
                "code": """<?php

declare(strict_types=1);

function grade(int $nilai): string
{
    if ($nilai < 0 || $nilai > 100) {
        throw new InvalidArgumentException("nilai di luar 0..100: $nilai");
    }
    return match (true) {
        $nilai >= 85 => 'A',
        $nilai >= 75 => 'B',
        $nilai >= 60 => 'C',
        default => 'D',
    };
}

function rataRata(float ...$angka): ?float
{
    if (count($angka) === 0) {
        return null;
    }
    return array_sum($angka) / count($angka);
}

function terapkan(array $data, callable $fn): array
{
    return array_map($fn, $data);
}

// Argumen bernama
function garis(string $isi, int $lebar = 30, string $pengisi = '-'): string
{
    return str_pad($isi, $lebar, $pengisi, STR_PAD_BOTH);
}

foreach ([92, 78, 64, 30] as $n) {
    printf("%3d -> %s\\n", $n, grade($n));
}

try {
    grade(150);
} catch (InvalidArgumentException $e) {
    echo 'Ditolak: ' . $e->getMessage() . "\\n";
}

echo "---\\n";
var_dump(rataRata(80.0, 90.0, 100.0));
var_dump(rataRata());

echo "---\\n";
$faktor = 3;
echo implode(', ', terapkan([1, 2, 3], fn($x) => $x * $faktor)) . "\\n";
echo garis(' rekap ', 30, '=') . "\\n";
echo garis(isi: ' selesai ', pengisi: '*') . "\\n";"""
            },
            {
                "body": [
                    "Keluaran:",
                    "   92 -> A",
                    "   78 -> B",
                    "   64 -> C",
                    "   30 -> D",
                    "  Ditolak: nilai di luar 0..100: 150",
                    "  ---",
                    "  float(90)",
                    "  NULL",
                    "  ---",
                    "  3, 6, 9",
                    "  =========== rekap ============",
                    "  ********** selesai ***********",
                    "",
                    "Baris str_pad mengisi kiri dan kanan sampai lebar yang diminta. Kalau",
                    "selisihnya ganjil, jumlah pengisi kiri dan kanan bisa beda satu.",
                    "",
                    "fn($x) => $x * $faktor menangkap $faktor tanpa use.",
                    "",
                    "Jebakan: dengan function biasa, kamu harus menulis",
                    "function ($x) use ($faktor) { ... }. Kalau use-nya lupa, PHP cuma",
                    "memberi peringatan 'undefined variable', dan programnya jalan terus.",
                    "Hasilnya nol, dan mungkin nggak ada yang sadar.",
                    "",
                    "?float sebagai tipe kembalian artinya \"float atau null\". Tanpa tanda",
                    "tanya, return null bikin TypeError, mau mode ketat nyala atau nggak.",
                    "",
                    "float ...$angka menerima berapa pun argumen dan mengumpulkannya jadi",
                    "array. Untuk kebalikannya, yaitu membongkar array jadi argumen, pakai",
                    "tiga titik yang sama waktu memanggil: rataRata(...$daftar);",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Di toko online, harga tampil di halaman produk, keranjang, struk, dan",
                    "email konfirmasi. Kalau format rupiahnya ditulis ulang di empat tempat,",
                    "suatu hari salah satunya lupa diubah dan tampil beda sendiri. Karena",
                    "itu programmer membungkusnya jadi satu fungsi kecil yang dipanggil dari",
                    "mana-mana, dan tipe di parameternya menjaga supaya fungsi itu nggak",
                    "dikirimi data yang salah.",
                    "",
                    "Kasus kecil: buat fungsi rupiah() yang mengubah 1250000 jadi",
                    "Rp1.250.000. Fungsi yang sama juga dipakai di halaman admin, tempat",
                    "harga baru diketik lewat form, jadi nilainya tiba sebagai string",
                    "\"15000\".",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tentukan bentuk fungsinya dulu: masukannya int, keluarannya string.",
                    "     Tulis dua-duanya sebagai tipe, dan pasang declare(strict_types=1)",
                    "     di awal berkas.",
                    "  2. Isi fungsinya cukup satu baris dengan number_format:",
                    "      function rupiah(int $angka): string",
                    "      {",
                    "          return 'Rp' . number_format($angka, 0, ',', '.');",
                    "      }",
                    "  3. Uji dengan beberapa angka: rupiah(1250000) menghasilkan",
                    "     Rp1.250.000, dan rupiah(0) menghasilkan Rp0.",
                    "  4. Uji masukan dari form. rupiah(\"15000\") ditolak dengan TypeError,",
                    "     dan itu memang yang kamu mau: isian form diperiksa dulu dengan",
                    "     filter_var, baru angkanya dikirim ke fungsi.",
                    "",
                    "Ingat: tanpa strict_types, rupiah(\"15000\") tetap jalan, dan rupiah()",
                    "nggak pernah tahu bahwa yang dikirim tadi teks dari form.",
                ]
            },
        ],
    },
    {
        "title": "8. Class & Objek",
        "sections": [
            {
                "body": [
                    "Class adalah cetakan untuk membuat objek. Objek adalah satu benda yang",
                    "punya data sendiri (property) dan perilaku sendiri (method). Property",
                    "itu variabel milik objek, dan method itu fungsi milik objek. Contohnya",
                    "class Murid:",
                    "",
                    "  class Murid",
                    "  {",
                    "      public function __construct(",
                    "          private string $nama,",
                    "          private int $nilai,",
                    "      ) {}",
                    "",
                    "      public function nama(): string { return $this->nama; }",
                    "  }",
                    "",
                    "Class di atas memakai constructor property promotion (PHP 8).",
                    "Constructor adalah method yang otomatis dipanggil waktu objek dibuat.",
                    "Kalau kamu menulis private string $nama di parameter constructor, PHP",
                    "sekaligus mendeklarasikan property $nama dan mengisinya. Cara",
                    "panjangnya butuh tiga baris untuk tiap property.",
                    "",
                    "Untuk mengakses isi objek, PHP memakai tanda panah (->), bukan titik:",
                    "  $m->nama",
                    "  $m->hitung()",
                    "  self::KONSTANTA      anggota statis, dari dalam",
                    "  Murid::buat()        anggota statis, dari luar",
                    "",
                    "Anggota statis adalah anggota milik class itu sendiri, bukan milik",
                    "satu objek. Untuk anggota statis dan konstanta class, dipakai tanda ::.",
                    "",
                    "$this menunjuk objek yang sedang dikerjakan, dan wajib ditulis. Ini",
                    "beda dari C# atau Java: di PHP, $nama polos di dalam method artinya",
                    "variabel lokal, bukan property.",
                    "",
                    "Modifier akses menentukan siapa yang boleh memakai sebuah anggota:",
                    "  public      siapa pun",
                    "  protected   class ini dan turunannya",
                    "  private     hanya class ini",
                    "",
                    "Aturan: selalu tulis modifiernya. Di C#, anggota tanpa modifier",
                    "otomatis private, jadi aman. Di PHP justru sebaliknya: method tanpa",
                    "modifier otomatis public, begitu juga property gaya PHP lama yang",
                    "ditulis pakai var.",
                    "",
                    "Magic method adalah method yang dipanggil PHP sendiri pada saat",
                    "tertentu. Namanya selalu diawali dua garis bawah. Yang sering dipakai:",
                    "  __construct()   dipanggil saat objek dibuat",
                    "  __destruct()    saat objek dihapus",
                    "  __toString()    saat objek dipakai sebagai string",
                    "  __get / __set   akses property yang tidak ada",
                    "  __call          panggil method yang tidak ada",
                    "  __invoke()      objeknya dipanggil seperti fungsi",
                    "",
                    "readonly (PHP 8.1) membuat property cuma bisa diisi sekali, dari dalam",
                    "class-nya sendiri, biasanya di constructor:",
                    "",
                    "  public function __construct(",
                    "      public readonly string $kode,",
                    "  ) {}",
                    "",
                    "readonly ini padanan init di C#. Gunanya untuk objek nilai, yaitu objek",
                    "yang isinya nggak boleh berubah sesudah dibuat.",
                ]
            },
            {
                "heading": "Class lengkap",
                "code": """<?php

declare(strict_types=1);

class Rekening
{
    private static int $urutan = 0;
    public readonly string $nomor;
    private int $saldo;

    public function __construct(
        public readonly string $pemilik,
        int $saldoAwal = 0,
    ) {
        if (trim($pemilik) === '') {
            throw new InvalidArgumentException('pemilik wajib diisi');
        }
        self::$urutan++;
        $this->nomor = sprintf('AC%04d', self::$urutan);
        $this->saldo = $saldoAwal;
    }

    public function saldo(): int
    {
        return $this->saldo;
    }

    public function setor(int $jumlah): void
    {
        if ($jumlah <= 0) {
            throw new InvalidArgumentException('jumlah harus positif');
        }
        $this->saldo += $jumlah;
    }

    public function tarik(int $jumlah): bool
    {
        if ($jumlah <= 0 || $jumlah > $this->saldo) {
            return false;
        }
        $this->saldo -= $jumlah;
        return true;
    }

    public function __toString(): string
    {
        return sprintf('%s %-8s %12s', $this->nomor, $this->pemilik,
                       number_format($this->saldo, 0, ',', '.'));
    }
}

$a = new Rekening('Andi', 500000);
$b = new Rekening('Budi');

$a->setor(250000);
echo 'tarik 900rb : ' . var_export($a->tarik(900000), true) . "\\n";
echo 'tarik 300rb : ' . var_export($a->tarik(300000), true) . "\\n";
$b->setor(100000);

echo $a . "\\n";
echo $b . "\\n";

try {
    new Rekening('   ');
} catch (InvalidArgumentException $e) {
    echo 'Ditolak: ' . $e->getMessage() . "\\n";
}"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  tarik 900rb : false",
                    "  tarik 300rb : true",
                    "  AC0001 Andi          450.000",
                    "  AC0002 Budi          100.000",
                    "  Ditolak: pemilik wajib diisi",
                    "",
                    "Empat hal di kode itu yang patut kamu lihat:",
                    "  1. public readonly string $pemilik di parameter constructor. Satu",
                    "     baris ini mendeklarasikan, mengisi, dan mengunci property",
                    "     sekaligus.",
                    "  2. private static int $urutan adalah milik class, bukan milik objek.",
                    "     Cuma ada satu untuk seluruh program, dan itu yang membuat nomor",
                    "     rekening bisa urut otomatis. Cara mengaksesnya self::$urutan,",
                    "     bukan $this->urutan.",
                    "  3. $saldo dibuat private, dan dibaca lewat method saldo(). Kalau",
                    "     $saldo dibuat public, semua aturan di setor() dan tarik() bisa",
                    "     dilewati cuma dengan satu baris.",
                    "  4. __toString() membuat objek bisa langsung di-echo. Tanpa method",
                    "     itu, echo $a melempar Error.",
                    "",
                    "Sampai PHP 8.3, PHP nggak punya property terhitung seperti di C#,",
                    "yaitu property yang nilainya dihitung setiap kali dibaca. PHP 8.4",
                    "menambahkan fitur serupa bernama property hooks. Gantinya, dipakai",
                    "method biasa: $a->saldo() pakai kurung, bukan $a->saldo.",
                    "",
                    "Method pembaca seperti itu disebut getter. Kebiasaan umumnya, getter",
                    "diberi nama yang sama dengan property-nya, tanpa awalan get. Tapi",
                    "banyak kode lama memakai getSaldo().",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Keranjang belanja di toko online adalah objek yang gampang dibayangkan.",
                    "Ia punya data, yaitu barang apa saja dan berapa banyak, dan punya",
                    "perilaku: tambah barang dan hitung total. Kalau datanya bisa diubah",
                    "dari mana saja, satu baris kode di halaman lain bisa mengubah isi",
                    "keranjang tanpa lewat aturan apa pun.",
                    "",
                    "Kasus kecil: buat class Keranjang. Pembeli menambah 2 Kopi Susu",
                    "seharga Rp18.000 dan 1 Roti Bakar seharga Rp15.000, lalu halaman",
                    "checkout menampilkan totalnya. Jumlah barang 0 atau negatif harus",
                    "ditolak.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Mulai dari cara memakainya. Tulis dulu kode yang kamu harapkan",
                    "     jalan:",
                    "      $k = new Keranjang();",
                    "      $k->tambah('Kopi Susu', 18000, 2);",
                    "      $k->tambah('Roti Bakar', 15000, 1);",
                    "      echo $k->total() . \"\\n\";",
                    "     Jawaban yang benar 51000.",
                    "  2. Dari situ kelihatan isi class-nya: property private array $isi,",
                    "     method tambah() yang menyimpan harga dikali jumlah, dan total()",
                    "     yang menjumlah isinya dengan array_sum.",
                    "  3. Buat $isi private. Dengan begitu, satu-satunya jalan mengubah isi",
                    "     keranjang adalah lewat tambah(), tempat semua aturan diperiksa.",
                    "  4. Uji kasus pinggir: tambah('Kopi Susu', 18000, 0). Di awal tambah(),",
                    "     lempar InvalidArgumentException kalau jumlahnya kurang dari 1,",
                    "     seperti setor() di class Rekening.",
                    "",
                    "Ingat: kalau barang yang sama ditambah dua kali, jumlahkan dengan nilai",
                    "lamanya. Mengisi $this->isi[$nama] begitu saja menimpa pesanan pertama.",
                ]
            },
        ],
    },
    {
        "title": "9. Pewarisan, Interface & Trait",
        "sections": [
            {
                "body": [
                    "Pewarisan artinya sebuah class mengambil isi class lain, lalu menambah",
                    "atau mengubah sebagian. Class yang diwarisi disebut induk, yang",
                    "mewarisi disebut turunan. Di PHP, sebuah class cuma boleh punya satu",
                    "induk:",
                    "",
                    "  abstract class Bangun",
                    "  {",
                    "      public function __construct(",
                    "          protected string $nama,",
                    "      ) {}",
                    "",
                    "      abstract public function luas(): float;",
                    "",
                    "      public function ringkas(): string",
                    "      {",
                    "          return sprintf('%-12s %8.2f', $this->nama, $this->luas());",
                    "      }",
                    "  }",
                    "",
                    "  class Persegi extends Bangun",
                    "  {",
                    "      public function __construct(private float $sisi)",
                    "      {",
                    "          parent::__construct('Persegi');",
                    "      }",
                    "",
                    "      public function luas(): float { return $this->sisi ** 2; }",
                    "  }",
                    "",
                    "extends menandai siapa induknya. Class abstract seperti Bangun nggak",
                    "bisa dibuat objeknya langsung. Method abstract seperti luas() cuma",
                    "berisi janji: setiap turunannya wajib menulis isinya.",
                    "",
                    "parent::__construct() memanggil constructor milik induk.",
                    "",
                    "Jebakan: beda dari Java atau C#, PHP nggak memanggil constructor induk",
                    "secara otomatis. Kalau kamu lupa memanggilnya, PHP nggak protes waktu",
                    "objeknya dibuat, padahal property milik induk nggak pernah terisi.",
                    "Masalahnya baru kelihatan belakangan: property tanpa tipe isinya null",
                    "tanpa peringatan apa pun, sedangkan property bertipe, seperti",
                    "protected string $nama tadi, memunculkan error waktu dibaca.",
                    "",
                    "final mencegah sebuah class diturunkan lagi, atau mencegah sebuah",
                    "method ditimpa di class turunan.",
                    "",
                    "Interface adalah kontrak, yaitu daftar method yang wajib dimiliki",
                    "class yang memakainya. Satu class boleh memakai banyak interface",
                    "sekaligus:",
                    "",
                    "  interface BisaDicetak",
                    "  {",
                    "      public function keTeks(): string;",
                    "  }",
                    "",
                    "  class Faktur implements BisaDicetak, JsonSerializable",
                    "",
                    "Semua anggota interface selalu public. Interface juga boleh punya",
                    "konstanta, dan sejak PHP 8.1 konstanta itu boleh ditimpa oleh class",
                    "yang memakainya.",
                    "",
                    "Trait adalah potongan kode yang bisa disisipkan ke banyak class. Trait",
                    "jadi jawaban PHP untuk kebutuhan berbagi kode antar class tanpa",
                    "pewarisan berganda, yaitu punya lebih dari satu induk:",
                    "",
                    "  trait BisaDicatat",
                    "  {",
                    "      protected array $catatan = [];",
                    "",
                    "      public function catat(string $pesan): void",
                    "      {",
                    "          $this->catatan[] = $pesan;",
                    "      }",
                    "  }",
                    "",
                    "  class Pesanan { use BisaDicatat; }",
                    "",
                    "Trait bukan tipe, jadi kamu nggak bisa menulis",
                    "function f(BisaDicatat $x). Kalau kamu juga butuh tipenya, pasangkan",
                    "trait dengan interface. Pola ini lazim di Laravel dan Symfony.",
                    "",
                    "Kalau dua trait punya method dengan nama yang sama, PHP mewajibkan",
                    "kamu memilih sendiri pakai insteadof dan as. PHP nggak akan",
                    "memilihkan salah satunya tanpa bilang-bilang.",
                ]
            },
            {
                "heading": "Pewarisan, interface, dan trait bersama",
                "code": """<?php

declare(strict_types=1);

interface Bangun
{
    public function luas(): float;
    public function nama(): string;
}

trait BisaDiringkas
{
    public function ringkas(): string
    {
        return sprintf('%-16s%8.2f', $this->nama(), $this->luas());
    }
}

abstract class BangunDasar implements Bangun
{
    use BisaDiringkas;

    public function __construct(private string $nama) {}

    public function nama(): string
    {
        return $this->nama;
    }
}

final class Persegi extends BangunDasar
{
    public function __construct(private float $sisi)
    {
        parent::__construct('Persegi');
    }

    public function luas(): float
    {
        return $this->sisi ** 2;
    }
}

final class Lingkaran extends BangunDasar
{
    private const PI = 3.14159;

    public function __construct(private float $jari)
    {
        parent::__construct('Lingkaran');
    }

    public function luas(): float
    {
        return self::PI * $this->jari ** 2;
    }

    public function ringkas(): string
    {
        return parent::ringkas() . sprintf('  (r=%.1f)', $this->jari);
    }
}

$semua = [
    new Persegi(4),
    new Lingkaran(3),
    new Persegi(2.5),
];

$total = 0.0;
foreach ($semua as $b) {
    echo $b->ringkas() . "\\n";
    $total += $b->luas();
}
printf("%-16s%8.2f\\n", 'TOTAL', $total);

echo "---\\n";
var_dump($semua[0] instanceof Bangun);
var_dump($semua[0] instanceof BangunDasar);"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  Persegi            16.00",
                    "  Lingkaran          28.27  (r=3.0)",
                    "  Persegi             6.25",
                    "  TOTAL              50.52",
                    "  ---",
                    "  bool(true)",
                    "  bool(true)",
                    "",
                    "Kode tadi memakai tiga mekanisme, dan masing-masing menjawab",
                    "pertanyaan yang berbeda:",
                    "  - Interface Bangun menjawab \"apa yang bisa dilakukan\". Interface ini",
                    "    yang membuat foreach di bawah jalan tanpa peduli class aslinya.",
                    "  - Abstract class BangunDasar menjawab \"apa yang sama di semua",
                    "    turunan\". Di sini isinya $nama.",
                    "  - Trait BisaDiringkas menjawab \"perilaku apa yang mau dipakai",
                    "    ulang\", tanpa ikut menentukan silsilah, yaitu siapa induk siapa.",
                    "",
                    "Lingkaran menimpa ringkas() dari trait, lalu memanggil",
                    "parent::ringkas() di dalamnya. Urutan prioritasnya di PHP: method yang",
                    "ditulis di class itu sendiri mengalahkan method dari trait, dan method",
                    "dari trait mengalahkan method dari class induk.",
                    "",
                    "private const PI di dalam class diakses dengan self::PI. Konstanta",
                    "class nggak pakai tanda dolar.",
                    "",
                    "instanceof ngecek apakah sebuah objek bertipe tertentu, termasuk lewat",
                    "interface dan induknya. Makanya kedua var_dump di atas sama-sama",
                    "mencetak bool(true): Persegi turunan BangunDasar, dan BangunDasar",
                    "memakai interface Bangun.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Halaman checkout toko online biasanya menawarkan beberapa cara bayar:",
                    "transfer bank, dompet digital, atau bayar di tempat. Tiap cara punya",
                    "aturan biaya sendiri, tapi halaman checkout nggak perlu tahu detailnya.",
                    "Ia cukup tahu bahwa setiap metode punya nama dan bisa menghitung",
                    "biayanya. Kesepakatan seperti itu ditulis sebagai interface.",
                    "",
                    "Kasus kecil: biaya transfer bank Rp4.000 per transaksi, dompet digital",
                    "1,5% dari total, dan bayar di tempat gratis (angkanya contoh). Untuk",
                    "belanja Rp200.000, checkout harus menampilkan biaya tiap metode.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Cari yang sama dari ketiganya, yaitu nama dan cara menghitung",
                    "     biaya. Jadikan itu interface:",
                    "      interface MetodeBayar",
                    "      {",
                    "          public function nama(): string;",
                    "          public function biaya(int $total): int;",
                    "      }",
                    "  2. Buat tiga class yang memakai interface itu: Transfer,",
                    "     DompetDigital, dan BayarDiTempat. Masing-masing cuma mengisi dua",
                    "     method tadi.",
                    "  3. Di checkout, simpan ketiganya di satu array lalu telusuri dengan",
                    "     foreach. Nggak perlu if untuk tiap metode, dan metode baru cukup",
                    "     ditambah sebagai class baru. Hasilnya 4000, 3000, dan 0.",
                    "  4. Periksa hitungan persen. $total * 0.015 selalu menghasilkan float,",
                    "     dan dengan strict_types, float yang dikembalikan method bertipe int",
                    "     ditolak TypeError. Pakai intdiv($total * 15, 1000), yang memberi",
                    "     2999 untuk belanja 199999.",
                ]
            },
        ],
    },
    {
        "title": "10. Enum & Objek Nilai",
        "sections": [
            {
                "body": [
                    "Enum adalah tipe yang nilainya cuma boleh salah satu dari daftar yang",
                    "sudah ditentukan. Contohnya status artikel: draf, ditinjau, atau",
                    "terbit.",
                    "",
                    "Sebelum PHP 8.1, orang memakai konstanta class untuk meniru enum:",
                    "",
                    "  class Status {",
                    "      const DRAF = 'draf';",
                    "      const TERBIT = 'terbit';",
                    "  }",
                    "",
                    "Masalahnya, dua panggilan ini sama-sama diterima, karena tipenya cuma",
                    "string:",
                    "  fungsi(Status::DRAF)",
                    "  fungsi('apa pun')",
                    "",
                    "Enum sungguhan baru ada di PHP 8.1:",
                    "",
                    "  enum Status",
                    "  {",
                    "      case Draf;",
                    "      case Ditinjau;",
                    "      case Terbit;",
                    "  }",
                    "",
                    "Sekarang function simpan(Status $s) menolak apa pun yang bukan salah",
                    "satu dari ketiga nilai itu.",
                    "",
                    "Backed enum adalah enum yang tiap nilainya punya nilai asli di",
                    "belakangnya, berupa string atau int. Gunanya untuk disimpan ke",
                    "database atau dikirim sebagai JSON:",
                    "",
                    "  enum Status: string",
                    "  {",
                    "      case Draf = 'draf';",
                    "      case Terbit = 'terbit';",
                    "  }",
                    "",
                    "  Status::Draf->value            'draf'",
                    "  Status::from('draf')           Status::Draf",
                    "  Status::tryFrom('xxx')         null, tanpa exception",
                    "  Status::cases()                array semua varian",
                    "  $s->name                       'Draf'",
                    "",
                    "Enum boleh punya method, dan itu yang membuatnya jauh lebih berguna",
                    "daripada konstanta:",
                    "",
                    "  enum Status: string",
                    "  {",
                    "      case Draf = 'draf';",
                    "      case Terbit = 'terbit';",
                    "",
                    "      public function label(): string",
                    "      {",
                    "          return match($this) {",
                    "              Status::Draf => 'Konsep',",
                    "              Status::Terbit => 'Terbit',",
                    "          };",
                    "      }",
                    "  }",
                    "",
                    "Enum juga boleh memakai interface. Yang nggak bisa: punya property",
                    "(menyimpan keadaan), dan diturunkan jadi enum lain.",
                    "",
                    "Enum jadi tempat paling cocok untuk aturan yang selama ini tersebar di",
                    "mana-mana: label tampilan, warna badge, izin akses, dan perpindahan",
                    "status yang sah. Semuanya bisa jadi method di satu berkas.",
                ]
            },
            {
                "heading": "Enum dengan method dan transisi",
                "code": """<?php

declare(strict_types=1);

enum Status: string
{
    case Draf = 'draf';
    case Ditinjau = 'ditinjau';
    case Disetujui = 'disetujui';
    case Ditolak = 'ditolak';
    case Terbit = 'terbit';

    public function label(): string
    {
        return match ($this) {
            Status::Draf => 'Konsep',
            Status::Ditinjau => 'Sedang ditinjau',
            Status::Disetujui => 'Disetujui',
            Status::Ditolak => 'Ditolak',
            Status::Terbit => 'Sudah terbit',
        };
    }

    public function bisaDisunting(): bool
    {
        return match ($this) {
            Status::Draf, Status::Ditolak => true,
            default => false,
        };
    }

    /** @return Status[] */
    public function berikutnya(): array
    {
        return match ($this) {
            Status::Draf => [Status::Ditinjau],
            Status::Ditinjau => [Status::Disetujui, Status::Ditolak],
            Status::Disetujui => [Status::Terbit],
            Status::Ditolak => [Status::Draf],
            Status::Terbit => [],
        };
    }
}

printf("%-12s%-10s%-18s%-10s%s\\n",
       'case', 'value', 'label', 'sunting?', 'berikutnya');
echo str_repeat('-', 72) . "\\n";

foreach (Status::cases() as $s) {
    $lanjut = array_map(fn(Status $x) => $x->name, $s->berikutnya());
    printf("%-12s%-10s%-18s%-10s%s\\n",
        $s->name,
        $s->value,
        $s->label(),
        $s->bisaDisunting() ? 'ya' : 'tidak',
        $lanjut === [] ? '-' : implode(', ', $lanjut),
    );
}

echo "---\\n";
var_dump(Status::from('terbit'));
var_dump(Status::tryFrom('tidak-ada'));"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  case        value     label             sunting?  berikutnya",
                    "  ------------------------------------------------------------------------",
                    "  Draf        draf      Konsep            ya        Ditinjau",
                    "  Ditinjau    ditinjau  Sedang ditinjau   tidak     Disetujui, Ditolak",
                    "  Disetujui   disetujui Disetujui         tidak     Terbit",
                    "  Ditolak     ditolak   Ditolak           ya        Draf",
                    "  Terbit      terbit    Sudah terbit      tidak     -",
                    "  ---",
                    "  enum(Status::Terbit)",
                    "  NULL",
                    "",
                    "Dua baris terakhir datang dari var_dump: enum(Status::Terbit) untuk",
                    "Status::from('terbit'), dan NULL untuk Status::tryFrom('tidak-ada').",
                    "",
                    "Kelebihan cara ini: seluruh aturan alur dokumen tinggal di satu",
                    "berkas. Sebelum ada enum, berikutnya() biasanya berupa array besar di",
                    "suatu tempat, bisaDisunting() berupa deretan if di controller (bagian",
                    "program yang menangani permintaan), dan label() tersebar di berkas",
                    "template. Ketiganya bisa saling nggak cocok tanpa ada yang sadar.",
                    "",
                    "match($this) di label() sengaja nggak punya default. Kalau nanti ada",
                    "nilai baru ditambahkan ke enum, PHP melempar UnhandledMatchError, dan",
                    "kamu langsung tahu ada yang terlewat. Menambahkan default justru",
                    "menyembunyikan kelalaian itu.",
                    "",
                    "from() melempar ValueError kalau nilainya nggak dikenal, sedangkan",
                    "tryFrom() mengembalikan null. Untuk data dari database yang kamu",
                    "kendalikan sendiri, from() yang tepat, karena nilai asing berarti",
                    "datanya rusak. Untuk masukan pengguna, pakai tryFrom().",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aplikasi pesan antar makanan dan toko online melacak status pesanan:",
                    "menunggu pembayaran, dibayar, dikirim, selesai, atau batal. Status itu",
                    "tersimpan di database sebagai teks. Aturan seperti \"pesanan yang sudah",
                    "dikirim nggak bisa dibatalkan\" harus sama di halaman pembeli, halaman",
                    "penjual, dan panel admin.",
                    "",
                    "Kasus kecil: tombol Batalkan cuma boleh muncul untuk pesanan berstatus",
                    "menunggu atau dibayar. Dari database datang teks status seperti",
                    "'dikirim', dan di beberapa baris lama masih ada teks 'diproses' yang",
                    "sudah nggak dipakai.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Kumpulkan dulu semua status yang sah. Pilihan tertutup seperti ini",
                    "     cocok jadi backed enum bertipe string, misalnya StatusPesanan.",
                    "  2. Taruh aturan pembatalan di dalam enum, supaya cuma ditulis sekali:",
                    "      public function bisaDibatalkan(): bool",
                    "      {",
                    "          return $this === self::Menunggu || $this === self::Dibayar;",
                    "      }",
                    "  3. Ubah teks dari database jadi enum dengan from(), karena datanya",
                    "     kamu kendalikan sendiri. Untuk 'dikirim', bisaDibatalkan()",
                    "     menghasilkan false, jadi tombolnya disembunyikan.",
                    "  4. Baris lama berisi 'diproses' bikin from() melempar ValueError. Itu",
                    "     tanda datanya perlu dibereskan: ubah baris itu jadi status yang",
                    "     sah, atau tambahkan case baru kalau statusnya memang masih dipakai.",
                    "",
                    "Ingat: kalau status datang dari pengguna, misalnya saringan ?status=",
                    "di alamat URL, pakai tryFrom(), supaya teks asing cukup jadi null.",
                ]
            },
        ],
    },
    {
        "title": "11. Exception & Penanganan Galat",
        "sections": [
            {
                "body": [
                    "Galat adalah istilah lain untuk error. Kalau ada yang salah waktu",
                    "program jalan, PHP bisa melaporkannya dengan dua cara, dan keduanya",
                    "perlu kamu bedakan:",
                    "  - Pesan bawaan PHP: warning, notice, dan deprecated. Program tetap",
                    "    jalan terus. Ini warisan PHP lama, dan pesan seperti ini nggak bisa",
                    "    langsung ditangkap dengan catch.",
                    "  - Exception: objek yang dilempar dan bisa ditangkap.",
                    "",
                    "Melempar (throw) artinya menghentikan jalannya kode dan melaporkan",
                    "masalah. Menangkap (catch) artinya menyiapkan kode yang menangani",
                    "laporan itu, supaya program nggak berhenti total.",
                    "",
                    "Sejak PHP 7, banyak kesalahan berat dari mesin PHP sendiri juga",
                    "dilaporkan dengan cara kedua, sebagai objek Error. Error dan Exception",
                    "disatukan di bawah satu interface bernama Throwable:",
                    "",
                    "  Throwable",
                    "  ├── Error              kesalahan mesin PHP",
                    "  │   ├── TypeError",
                    "  │   │   └── ArgumentCountError",
                    "  │   ├── ValueError",
                    "  │   └── ArithmeticError -> DivisionByZeroError",
                    "  └── Exception          kesalahan aplikasi",
                    "      ├── RuntimeException",
                    "      │   ├── OutOfBoundsException",
                    "      │   └── PDOException",
                    "      ├── LogicException",
                    "      │   ├── InvalidArgumentException",
                    "      │   └── DomainException",
                    "      └── JsonException, ...",
                    "",
                    "Pustaka standar PHP membagi exception jadi dua golongan:",
                    "  - LogicException untuk kesalahan programmer. Kesalahan seperti ini",
                    "    seharusnya sudah ketahuan waktu program masih dikembangkan.",
                    "  - RuntimeException untuk kegagalan yang baru ketahuan waktu program",
                    "    jalan, misalnya berkas hilang atau jaringan putus.",
                    "",
                    "Cara menangkapnya:",
                    "",
                    "  try {",
                    "      ...",
                    "  } catch (InvalidArgumentException $e) {",
                    "      ...",
                    "  } catch (RuntimeException | JsonException $e) {",
                    "      ...            beberapa tipe sekaligus, PHP 7.1",
                    "  } catch (Throwable $e) {",
                    "      ...            jaring terakhir",
                    "  } finally {",
                    "      ...            SELALU dijalankan",
                    "  }",
                    "",
                    "PHP mencoba blok catch dari atas ke bawah, dan memakai yang pertama",
                    "cocok. Makanya catch (Throwable $e), yang cocok dengan semua jenis,",
                    "ditaruh paling bawah sebagai jaring terakhir. Blok finally selalu",
                    "dijalankan, ada exception atau nggak.",
                    "",
                    "Sejak PHP 8, nama variabelnya boleh dihilangkan kalau nggak dipakai:",
                    "  catch (ValueError) { ... }",
                    "",
                    "Isi objek exception yang bisa dibaca:",
                    "  $e->getMessage()   pesan",
                    "  $e->getCode()      kode",
                    "  $e->getFile()      berkas",
                    "  $e->getLine()      nomor baris",
                    "  $e->getPrevious()  exception sebelumnya, kalau dirantai",
                    "  $e->getTraceAsString()",
                    "",
                    "Merantai exception itu kebiasaan yang penting. Waktu kamu menangkap",
                    "error tingkat rendah, misalnya JSON yang rusak, lalu melempar error",
                    "tingkat tinggi seperti \"konfigurasi tidak bisa dibaca\", sertakan",
                    "exception aslinya sebagai argumen ketiga. Tanpa itu, jejak penyebab",
                    "aslinya hilang.",
                ]
            },
            {
                "heading": "Exception sendiri dan perantaian",
                "code": """<?php

declare(strict_types=1);

final class SaldoKurangException extends RuntimeException
{
    public function __construct(public readonly int $kurang)
    {
        parent::__construct("saldo kurang $kurang");
    }
}

final class Dompet
{
    public function __construct(private int $saldo) {}

    public function saldo(): int
    {
        return $this->saldo;
    }

    public function bayar(int $jumlah): void
    {
        if ($jumlah <= 0) {
            throw new InvalidArgumentException("jumlah $jumlah tidak sah");
        }
        if ($jumlah > $this->saldo) {
            throw new SaldoKurangException($jumlah - $this->saldo);
        }
        $this->saldo -= $jumlah;
    }
}

$d = new Dompet(50000);

foreach ([20000, -5, 100000, 30000] as $tagihan) {
    try {
        $d->bayar($tagihan);
        printf("bayar %7d -> sisa %d\\n", $tagihan, $d->saldo());
    } catch (SaldoKurangException $e) {
        printf("bayar %7d -> GAGAL, kurang %d\\n", $tagihan, $e->kurang);
    } catch (InvalidArgumentException $e) {
        printf("bayar %7d -> DITOLAK: %s\\n", $tagihan, $e->getMessage());
    }
}

echo "---\\n";

// Merantai: galat tingkat rendah dibungkus jadi galat tingkat tinggi
function bacaKonfigurasi(string $json): array
{
    try {
        return json_decode($json, true, 512, JSON_THROW_ON_ERROR);
    } catch (JsonException $e) {
        throw new RuntimeException('konfigurasi tidak bisa dibaca', 0, $e);
    }
}

try {
    bacaKonfigurasi('{rusak}');
} catch (RuntimeException $e) {
    echo 'luar  : ' . $e->getMessage() . "\\n";
    echo 'dalam : ' . $e->getPrevious()?->getMessage() . "\\n";
}

echo "---\\n";
try {
    intdiv(1, 0);
} catch (DivisionByZeroError $e) {
    echo 'Error : ' . $e->getMessage() . "\\n";
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
                    "  luar  : konfigurasi tidak bisa dibaca",
                    "  dalam : Syntax error",
                    "  ---",
                    "  Error : Division by zero",
                    "",
                    "Ingat JSON_THROW_ON_ERROR. Ini sebuah flag, yaitu pilihan tambahan",
                    "untuk sebuah fungsi. Dengan flag ini, json_decode melempar",
                    "JsonException kalau JSON-nya rusak. Tanpa flag itu, json_decode",
                    "mengembalikan null untuk JSON yang rusak, dan juga untuk JSON yang",
                    "isinya memang null. Dua keadaan itu nggak bisa dibedakan, dan bug yang",
                    "muncul dari situ susah dilacak.",
                    "",
                    "$e->getPrevious()?->getMessage() memakai ?->. Kalau nggak ada",
                    "exception sebelumnya, seluruh ekspresi itu cukup bernilai null, dan",
                    "nggak memunculkan error baru.",
                    "",
                    "Ada tiga hal yang sebaiknya nggak kamu lakukan:",
                    "  - Menulis catch (Throwable $e) {} yang kosong. Catch kosong menelan",
                    "    semua kesalahan, termasuk TypeError dan Error lain dari mesin PHP,",
                    "    lalu program jalan terus dalam keadaan rusak.",
                    "  - Memakai @ untuk membungkam error. Operator itu menyembunyikan semua",
                    "    peringatan dari ekspresi di belakangnya, termasuk yang nggak kamu",
                    "    duga.",
                    "  - Menangkap exception yang nggak bisa kamu perbaiki. Lebih baik",
                    "    biarkan exception itu naik ke pemanggil yang tahu konteksnya,",
                    "    daripada ditangani setengah-setengah.",
                    "",
                    "Hati-hati di server produksi, yaitu server yang dipakai pengunjung",
                    "sungguhan. Di sana display_errors, yang menampilkan error di halaman,",
                    "wajib dimatikan. log_errors, yang mencatat error ke berkas log, wajib",
                    "dinyalakan. Pesan error PHP memuat jalur berkas dan potongan kode, dan",
                    "itu informasi berharga bagi penyerang.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Fitur impor data, misalnya unggah daftar siswa atau daftar harga,",
                    "hampir selalu ketemu baris yang rusak. Aplikasi yang baik nggak",
                    "berhenti total karena satu baris salah ketik. Ia mencatat baris itu",
                    "beserta alasannya, lalu lanjut ke baris berikutnya.",
                    "",
                    "Kasus kecil: guru menempelkan nilai ulangan sebagai teks, satu siswa",
                    "per baris: Andi:88, Budi:delapan, dan Cici:95. Baris Budi harus",
                    "dilaporkan sebagai galat, sedangkan nilai Andi dan Cici tetap",
                    "tersimpan.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pisahkan dua pekerjaan: mengurai satu baris, dan mengulang ke semua",
                    "     baris. Fungsi uraikan() cuma mengurus satu baris.",
                    "  2. Di dalam uraikan(), pecah teks dengan explode(':'), periksa",
                    "     nilainya dengan filter_var, lalu lempar InvalidArgumentException",
                    "     kalau nilainya bukan bilangan bulat 0 sampai 100.",
                    "  3. Di dalam foreach, bungkus tiap panggilan dengan try dan catch, dan",
                    "     simpan nomor barisnya di $nomor:",
                    "      try {",
                    "          $data[] = uraikan($teks);",
                    "      } catch (InvalidArgumentException $e) {",
                    "          $galat[] = \"baris $nomor: \" . $e->getMessage();",
                    "      }",
                    "     Hasilnya dua nilai tersimpan dan satu laporan untuk baris 2.",
                    "  4. Periksa baris tanpa titik dua, misalnya Dedi 70. explode cuma",
                    "     menghasilkan satu elemen, jadi uraikan() harus melempar exception",
                    "     juga di sini, sebelum mencoba membaca elemen kedua yang nggak ada.",
                    "",
                    "Jebakan: hindari catch (Throwable $e) di perulangan ini. TypeError dari",
                    "bug di kodemu sendiri ikut tertangkap dan tercatat sebagai baris rusak,",
                    "padahal yang rusak programnya.",
                ]
            },
        ],
    },
    {
        "title": "12. Bekerja dengan Berkas & JSON",
        "sections": [
            {
                "body": [
                    "Cara singkat membaca dan menulis berkas:",
                    "  file_get_contents($path)          seluruh isi jadi string",
                    "  file_put_contents($path, $isi)    tulis (menimpa)",
                    "  file_put_contents($path, $isi, FILE_APPEND)",
                    "  file($path)                       tiap baris jadi elemen array",
                    "  file($path, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES)",
                    "",
                    "FILE_APPEND menambahkan isi di akhir berkas, jadi isi lamanya nggak",
                    "ditimpa. Dua flag di baris terakhir membuang tanda pindah baris dan",
                    "melewati baris kosong. Tanda | dipakai untuk menggabungkan beberapa",
                    "flag sekaligus.",
                    "",
                    "file_get_contents dan file membaca seluruh isi berkas ke memori",
                    "sekaligus. Untuk berkas besar, baca sedikit demi sedikit:",
                    "  $f = fopen($path, 'r');",
                    "  while (($baris = fgets($f)) !== false) { ... }",
                    "  fclose($f);",
                    "",
                    "fopen membuka berkas, fgets membaca satu baris setiap kali dipanggil",
                    "(dan mengembalikan false kalau sudah habis), lalu fclose menutup",
                    "berkasnya lagi.",
                    "",
                    "Mode fopen menentukan apa yang boleh kamu lakukan dengan berkasnya:",
                    "  'r'    baca",
                    "  'w'    tulis, isi lama dikosongkan",
                    "  'a'    tambah di akhir",
                    "  'x'    buat baru, gagal kalau berkasnya sudah ada",
                    "  'r+'   baca dan tulis",
                    "",
                    "Hati-hati dengan mode 'w'. Isi lama berkasnya langsung dikosongkan",
                    "begitu berkas dibuka, bahkan sebelum kamu menulis apa pun.",
                    "",
                    "Memeriksa dan mengelola berkas:",
                    "  file_exists / is_file / is_dir",
                    "  is_readable / is_writable",
                    "  filesize / filemtime",
                    "  unlink($path)              hapus berkas",
                    "  copy / rename",
                    "  mkdir($path, 0755, true)   true = buat induknya juga",
                    "  scandir / glob('*.txt')",
                    "",
                    "Supaya jalur berkas benar di semua sistem operasi:",
                    "  __DIR__                    folder berkas ini",
                    "  __FILE__                   berkas ini",
                    "  DIRECTORY_SEPARATOR",
                    "  basename / dirname / pathinfo",
                    "  sys_get_temp_dir()",
                    "",
                    "DIRECTORY_SEPARATOR berisi pemisah folder: / di Linux dan macOS, \\ di",
                    "Windows. sys_get_temp_dir() memberi folder untuk berkas sementara.",
                    "",
                    "JSON adalah format teks untuk menyimpan dan bertukar data. PHP punya",
                    "dua fungsi untuk JSON, dan keduanya punya jebakan:",
                    "",
                    "  json_encode($data, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE)",
                    "  json_decode($teks, true)     true = jadi array, bukan objek",
                    "",
                    "json_encode mengubah data PHP jadi teks JSON, dan json_decode",
                    "melakukan kebalikannya.",
                    "",
                    "Aturan: selalu tambahkan JSON_THROW_ON_ERROR. Tanpa flag itu,",
                    "kegagalan cuma dikembalikan sebagai false atau null, dan gampang lolos",
                    "tanpa diperiksa.",
                    "",
                    "Flag yang sering dibutuhkan:",
                    "  JSON_PRETTY_PRINT        berbaris rapi",
                    "  JSON_UNESCAPED_UNICODE   huruf non-ASCII apa adanya",
                    "  JSON_UNESCAPED_SLASHES   / tidak diubah jadi \\/",
                    "  JSON_THROW_ON_ERROR      lempar exception saat gagal",
                    "",
                    "CSV adalah format tabel dalam bentuk teks, dengan kolom yang dipisah",
                    "koma. PHP punya fungsi khusus untuk CSV, jadi pakai fungsi itu, jangan",
                    "explode(','). Di CSV sungguhan, koma boleh ada di dalam kolom asal",
                    "kolomnya dikutip, dan explode bakal ikut memecah koma itu:",
                    "  fgetcsv($f) / fputcsv($f, $baris)",
                    "  str_getcsv($baris)",
                ]
            },
            {
                "heading": "Menulis, membaca, dan mengolah berkas",
                "code": """<?php

declare(strict_types=1);

$berkas = sys_get_temp_dir() . DIRECTORY_SEPARATOR . 'belajar-php.csv';

// --- Tulis CSV ---
$f = fopen($berkas, 'w');
fputcsv($f, ['nama', 'kelas', 'nilai']);
foreach ([['Andi', 'A', 88], ['Budi', 'B', 72], ['Cici', 'A', 95]] as $baris) {
    fputcsv($f, $baris);
}
fclose($f);

// --- Baca kembali ---
$f = fopen($berkas, 'r');
$judul = fgetcsv($f);
$data = [];
while (($baris = fgetcsv($f)) !== false) {
    $data[] = array_combine($judul, $baris);
}
fclose($f);

usort($data, fn($a, $b) => (int) $b['nilai'] <=> (int) $a['nilai']);
foreach ($data as $m) {
    printf("%-6s %s %3d\\n", $m['nama'], $m['kelas'], $m['nilai']);
}

$nilai = array_map('intval', array_column($data, 'nilai'));
printf("Rata-rata: %.2f\\n", array_sum($nilai) / count($nilai));

// --- JSON ---
echo "---\\n";
$json = json_encode($data[0], JSON_PRETTY_PRINT | JSON_THROW_ON_ERROR);
echo $json . "\\n";

$kembali = json_decode($json, true, 512, JSON_THROW_ON_ERROR);
echo 'nama dari JSON: ' . $kembali['nama'] . "\\n";

try {
    json_decode('{rusak}', true, 512, JSON_THROW_ON_ERROR);
} catch (JsonException $e) {
    echo 'JSON rusak: ' . $e->getMessage() . "\\n";
}

unlink($berkas);
echo 'berkas masih ada? ' . var_export(file_exists($berkas), true) . "\\n";"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  Cici   A  95",
                    "  Andi   A  88",
                    "  Budi   B  72",
                    "  Rata-rata: 85.00",
                    "  ---",
                    "  {",
                    "      \"nama\": \"Cici\",",
                    "      \"kelas\": \"A\",",
                    "      \"nilai\": \"95\"",
                    "  }",
                    "  nama dari JSON: Cici",
                    "  JSON rusak: Syntax error",
                    "  berkas masih ada? false",
                    "",
                    "Lihat \"nilai\": \"95\" di JSON-nya. Nilainya berupa teks, bukan angka.",
                    "Semua yang keluar dari CSV berupa string, karena CSV nggak punya tipe.",
                    "",
                    "Makanya perbandingan di usort memakai (int): supaya nilainya pasti",
                    "dibandingkan sebagai angka. Kalau dibandingkan sebagai teks, misalnya",
                    "dengan strcmp(), \"100\" dianggap lebih kecil daripada \"95\", karena yang",
                    "dibandingkan karakter pertamanya dulu: \"1\" lawan \"9\".",
                    "",
                    "Untuk dua teks yang isinya angka, operator <=> memang sudah",
                    "membandingkannya sebagai angka. Tapi dengan (int), maksudnya jadi",
                    "jelas, dan nilainya tetap dibandingkan sebagai angka walaupun ada teks",
                    "yang bukan angka bersih.",
                    "",
                    "array_combine($judul, $baris) menggabungkan baris judul dengan baris",
                    "data jadi array berkunci. Ini cara paling ringkas mengubah CSV jadi",
                    "struktur yang enak dipakai.",
                    "",
                    "array_map('intval', ...) mengirim nama fungsi sebagai string. intval",
                    "adalah fungsi bawaan yang mengubah nilai jadi int. PHP menerima nama",
                    "fungsi seperti ini di mana pun callable diminta. Bentuk lain yang juga",
                    "sah:",
                    "  [$objek, 'method']",
                    "  [Kelas::class, 'methodStatis']",
                    "  fn($x) => ...",
                    "",
                    "Operasi berkas selalu bisa gagal karena hal di luar kendalimu, misalnya",
                    "izin akses atau disk yang penuh. Di kode sungguhan, periksa hasilnya:",
                    "  if ($f === false) { throw new RuntimeException(...); }",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Bendahara kelas, kasir UMKM, dan admin gudang sering bekerja dengan",
                    "berkas CSV, karena berkas itu bisa dibuka di aplikasi spreadsheet dan",
                    "juga bisa diolah program. Laporan yang diekspor dari aplikasi kasir",
                    "juga sering berbentuk CSV. Sementara itu, setelan aplikasi dan data",
                    "kiriman layanan lain biasanya berupa JSON.",
                    "",
                    "Kasus kecil: kas.csv punya kolom tanggal, keterangan, masuk, dan",
                    "keluar. Isinya tiga transaksi: iuran Rp150.000 masuk, beli spidol dan",
                    "penghapus Rp35.000 keluar, dan fotokopi soal Rp20.000 keluar. Berapa",
                    "saldo akhirnya?",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pahami bentuk berkasnya. Baris pertama berisi judul kolom, sisanya",
                    "     data, dan semua nilai yang dibaca dari CSV berupa string.",
                    "  2. Baca baris demi baris dengan fgetcsv. Panggilan pertama membuang",
                    "     baris judul, lalu tiap baris menambah kolom masuk dan mengurangi",
                    "     kolom keluar:",
                    "      $f = fopen('kas.csv', 'r');",
                    "      fgetcsv($f);",
                    "      $saldo = 0;",
                    "      while (($b = fgetcsv($f)) !== false) {",
                    "          $saldo += (int) $b[2] - (int) $b[3];",
                    "      }",
                    "     Hasilnya 95000. Tutup berkasnya dengan fclose($f) sesudahnya.",
                    "  3. Perhatikan keterangan yang memuat koma. Di berkasnya tertulis",
                    "     \"Beli spidol, penghapus\" dalam kutip. fgetcsv membacanya sebagai",
                    "     satu kolom, sedangkan explode(',') memecahnya jadi dua, dan kolom",
                    "     angka sesudahnya ikut bergeser.",
                    "  4. Siapkan kegagalan. Kalau kas.csv nggak ada, fopen memunculkan",
                    "     warning dan mengembalikan false, jadi periksa hasilnya dulu.",
                ]
            },
        ],
    },
    {
        "title": "13. PHP untuk Web: Request, Form & Sesi",
        "sections": [
            {
                "body": [
                    "PHP punya satu sifat yang membedakannya dari banyak bahasa lain.",
                    "Setiap permintaan HTTP, yaitu setiap kali browser meminta sebuah",
                    "halaman, menjalankan skripmu dari nol. Begitu halamannya selesai",
                    "dikirim, seluruh memorinya dibuang. Nggak ada data yang bertahan dari",
                    "satu permintaan ke permintaan berikutnya, kecuali kamu menyimpannya",
                    "sendiri.",
                    "",
                    "Model \"shared nothing\" ini punya sisi baik dan sisi buruk. Kebocoran",
                    "memori, yaitu memori yang lupa dilepas lalu menumpuk, hampir mustahil",
                    "terjadi. Tapi koneksi database harus dibuka ulang di setiap",
                    "permintaan.",
                    "",
                    "Variabel superglobal bisa dipakai di mana saja, termasuk di dalam",
                    "fungsi:",
                    "  $_GET      parameter di URL",
                    "  $_POST     data dari form",
                    "  $_REQUEST  gabungan keduanya (jangan dipakai)",
                    "  $_SERVER   informasi permintaan dan server",
                    "  $_FILES    berkas yang diunggah",
                    "  $_COOKIE   cookie",
                    "  $_SESSION  data sesi",
                    "  $_ENV      variabel lingkungan",
                    "",
                    "$_REQUEST sebaiknya nggak dipakai. Urutan isinya tergantung setelan",
                    "server, dan di setelan tertentu penyerang bisa menimpa nilai POST lewat",
                    "URL.",
                    "",
                    "Aturan keamanan nomor satu: jangan pernah percaya masukan pengguna.",
                    "Ada tiga hal yang harus kamu lakukan, dan ketiganya berbeda:",
                    "  1. Validasi waktu data masuk, yaitu ngecek apakah datanya masuk akal.",
                    "       $umur = filter_var($_POST['umur'] ?? '',",
                    "                          FILTER_VALIDATE_INT);",
                    "       if ($umur === false) { ... tolak ... }",
                    "  2. Escape waktu data keluar ke HTML. Escape artinya mengubah karakter",
                    "     yang punya arti khusus di HTML, seperti < dan >, jadi bentuk yang",
                    "     cuma ditampilkan sebagai teks.",
                    "       echo htmlspecialchars($nama, ENT_QUOTES, 'UTF-8');",
                    "     Tanpa ini, nama yang berisi <script> bakal dijalankan oleh browser",
                    "     pengunjung lain. Serangan ini namanya XSS.",
                    "  3. Prepared statement waktu data dikirim ke database. Ini dibahas di",
                    "     materi berikutnya, yang khusus membahas database. Menyambung query",
                    "     dengan titik membuka celah SQL injection.",
                    "",
                    "Ketiganya nggak saling menggantikan. Data yang sudah divalidasi tetap",
                    "harus di-escape, dan sebaliknya.",
                    "",
                    "Sesi dipakai untuk mengingat data seorang pengunjung dari satu",
                    "permintaan ke permintaan berikutnya, misalnya siapa yang sedang login:",
                    "  session_start();              wajib sebelum output apa pun",
                    "  $_SESSION['user_id'] = 7;",
                    "  session_regenerate_id(true);  sesudah login, cegah fiksasi",
                    "  session_destroy();",
                    "",
                    "Fiksasi sesi adalah serangan ketika penyerang menyiapkan ID sesi lebih",
                    "dulu, lalu menunggu korbannya login memakai ID itu. Membuat ID baru",
                    "sesudah login mematahkan serangan ini. session_destroy() menghapus",
                    "sesinya, misalnya waktu logout.",
                    "",
                    "session_start() harus dipanggil sebelum satu byte pun dikirim ke",
                    "browser, karena fungsi itu memasang header cookie. Ini juga alasan",
                    "utama kenapa tag ?> di akhir berkas berbahaya (lihat materi Pengenalan",
                    "PHP & Instalasi): spasi sesudahnya sudah terhitung keluaran.",
                ]
            },
            {
                "heading": "Form yang menangani dirinya sendiri",
                "code": """<?php
declare(strict_types=1);

session_start();

$galat = [];
$nama = '';
$umur = null;

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // 1. VALIDASI
    $nama = trim($_POST['nama'] ?? '');
    if ($nama === '') {
        $galat['nama'] = 'Nama wajib diisi.';
    } elseif (mb_strlen($nama) > 50) {
        $galat['nama'] = 'Nama maksimal 50 karakter.';
    }

    $umur = filter_var($_POST['umur'] ?? '', FILTER_VALIDATE_INT,
                       ['options' => ['min_range' => 1, 'max_range' => 120]]);
    if ($umur === false) {
        $galat['umur'] = 'Umur harus angka 1 sampai 120.';
    }

    if ($galat === []) {
        $_SESSION['nama'] = $nama;
        $_SESSION['umur'] = $umur;
    }
}

// Helper escape: dipakai di SETIAP titik keluaran
function e(?string $s): string
{
    return htmlspecialchars($s ?? '', ENT_QUOTES, 'UTF-8');
}
?>
<!DOCTYPE html>
<html lang="id">
<head><meta charset="utf-8"><title>Pendaftaran</title></head>
<body>

<?php if (isset($_SESSION['nama']) && $galat === []): ?>
  <p>Tersimpan: <?= e($_SESSION['nama']) ?> (<?= (int) $_SESSION['umur'] ?>)</p>
<?php endif; ?>

<form method="post">
  <label>
    Nama
    <input type="text" name="nama" value="<?= e($nama) ?>" required>
  </label>
  <?php if (isset($galat['nama'])): ?>
    <span class="galat"><?= e($galat['nama']) ?></span>
  <?php endif; ?>

  <label>
    Umur
    <input type="number" name="umur" value="<?= $umur !== false ? (int) $umur : '' ?>">
  </label>
  <?php if (isset($galat['umur'])): ?>
    <span class="galat"><?= e($galat['umur']) ?></span>
  <?php endif; ?>

  <button type="submit">Simpan</button>
</form>

</body>
</html>"""
            },
            {
                "body": [
                    "Pola di atas disebut POST ke diri sendiri: satu berkas menampilkan form",
                    "sekaligus memprosesnya. Untuk form sederhana, pola ini cukup dan",
                    "gampang diikuti.",
                    "",
                    "Lima hal yang membuat kode itu benar, dan semuanya sering dilupakan:",
                    "  1. ?? '' di setiap pembacaan $_POST. Tanpa itu, permintaan POST yang",
                    "     nggak membawa field (isian form) tertentu memicu peringatan",
                    "     'undefined array key'. Kode yang membaca $_POST tanpa ngecek",
                    "     metode permintaannya dulu bahkan kena peringatan ini di setiap",
                    "     field, waktu halamannya pertama kali dibuka lewat permintaan GET.",
                    "  2. Fungsi e() dipakai di setiap titik keluaran, termasuk untuk nilai",
                    "     yang baru aja divalidasi. Validasi dan escape menjawab pertanyaan",
                    "     yang berbeda.",
                    "  3. Isi form diisi ulang dengan masukan sebelumnya. Form yang",
                    "     mengosongkan dirinya setiap kali ada kesalahan bikin orang cepat",
                    "     menyerah.",
                    "  4. Validasi umur memakai rentang, nggak cuma ngecek \"apakah ini",
                    "     angka\". Umur 99999 lolos pemeriksaan tipe.",
                    "  5. (int) $_SESSION['umur'] waktu dicetak. Ini pertahanan berlapis,",
                    "     berjaga-jaga kalau sesi berisi sesuatu yang lain.",
                    "",
                    "Awas: contoh ini belum punya token CSRF, padahal token itu wajib ada di",
                    "situs sungguhan. Tanpa token, situs lain bisa membuat browser",
                    "pengunjungmu mengirim form ini tanpa ia sadari. Polanya:",
                    "",
                    "  $_SESSION['csrf'] ??= bin2hex(random_bytes(32));",
                    "  <input type=\"hidden\" name=\"csrf\"",
                    "         value=\"<?= e($_SESSION['csrf']) ?>\">",
                    "",
                    "  lalu saat memproses:",
                    "  if (!hash_equals($_SESSION['csrf'], $_POST['csrf'] ?? '')) {",
                    "      http_response_code(403); exit;",
                    "  }",
                    "",
                    "Token acak disimpan di sesi dan diselipkan ke form sebagai isian",
                    "tersembunyi. Waktu form dikirim, dua token itu dibandingkan. Situs lain",
                    "nggak tahu isi tokennya, jadi kirimannya ditolak dengan kode 403.",
                    "",
                    "hash_equals dipakai sebagai ganti === karena fungsi itu membandingkan",
                    "dalam waktu yang selalu sama. Jadi penyerang nggak bisa menebak isi",
                    "token dari selisih waktu perbandingannya.",
                    "",
                    "Sesudah POST berhasil, sebaiknya langsung alihkan pengunjung ke",
                    "halaman lain (redirect). Pola ini namanya Post/Redirect/Get. Tanpa",
                    "redirect, menekan tombol Refresh bakal mengirim ulang datanya.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Kotak pencarian di toko online mengirim kata kuncinya lewat alamat URL,",
                    "misalnya cari.php?q=kopi&hal=2. PHP membacanya dari $_GET, mencari",
                    "produknya, lalu menulis ulang kata kunci itu di halaman hasil. Siapa",
                    "pun bisa mengetik apa saja di alamat URL, jadi halaman seperti ini",
                    "sering jadi tempat orang mencoba serangan XSS.",
                    "",
                    "Kasus kecil: halaman cari.php menampilkan teks \"Hasil untuk: kopi,",
                    "halaman 2\". Lalu ada pengunjung yang membuka alamat dengan q berisi",
                    "<script>alert(1)</script> dan hal berisi abc.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pahami masukannya: q dan hal sama-sama string dari URL, dan",
                    "     dua-duanya bisa nggak ada sama sekali.",
                    "  2. Baca dengan ?? supaya parameter yang hilang nggak memicu",
                    "     peringatan, lalu validasi hal sebagai bilangan bulat minimal 1:",
                    "      $q = trim($_GET['q'] ?? '');",
                    "      $hal = filter_var($_GET['hal'] ?? 1, FILTER_VALIDATE_INT,",
                    "          ['options' => ['min_range' => 1]]);",
                    "      $hal = $hal === false ? 1 : $hal;",
                    "  3. Escape q tepat saat dicetak dengan htmlspecialchars($q, ENT_QUOTES,",
                    "     'UTF-8'). Skrip tadi tampil sebagai teks biasa, dan browser nggak",
                    "     menjalankannya.",
                    "  4. Untuk hal=abc atau hal=-3, filter_var mengembalikan false, jadi",
                    "     halamannya kembali ke 1. Salah ketik nomor halaman nggak perlu",
                    "     dijawab dengan pesan error.",
                    "",
                    "Ingat: q yang kosong juga perlu ditangani. Tampilkan ajakan mengetik",
                    "kata yang dicari, daripada menjalankan pencarian tanpa kata kunci.",
                ]
            },
        ],
    },
    {
        "title": "14. Database dengan PDO",
        "sections": [
            {
                "body": [
                    "PDO (PHP Data Objects) adalah antarmuka database bawaan PHP. Cara",
                    "memakainya sama untuk MySQL, PostgreSQL, SQLite, dan database lainnya.",
                    "",
                    "Cara menyambung ke database:",
                    "",
                    "  $pdo = new PDO(",
                    "      'mysql:host=localhost;dbname=toko;charset=utf8mb4',",
                    "      $user, $sandi,",
                    "      [",
                    "          PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,",
                    "          PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,",
                    "          PDO::ATTR_EMULATE_PREPARES => false,",
                    "      ]",
                    "  );",
                    "",
                    "Ketiga opsi itu punya gunanya masing-masing:",
                    "  - ERRMODE_EXCEPTION. Tanpa opsi ini, query (perintah ke database)",
                    "    yang gagal cuma mengembalikan false, dan programmu jalan terus",
                    "    dengan data kosong.",
                    "  - FETCH_ASSOC. Hasilnya berupa array yang kuncinya cuma nama kolom.",
                    "    Bawaannya (FETCH_BOTH), tiap kolom disimpan dua kali, sekali pakai",
                    "    nama dan sekali pakai nomor, jadi separuh memorinya terbuang.",
                    "  - EMULATE_PREPARES diisi false. Artinya prepared statement dikirim",
                    "    sungguhan ke server database, nggak cuma ditiru di sisi PHP. Versi",
                    "    tiruan tetap menyambung string, dan dulu pernah punya celah injeksi",
                    "    lewat charset tertentu.",
                    "",
                    "Prepared statement adalah perintah SQL yang bentuknya disiapkan dulu,",
                    "dengan tanda tanya atau nama sebagai tempat data. Datanya dikirim",
                    "belakangan. Ini satu-satunya cara yang benar untuk memasukkan data ke",
                    "query:",
                    "",
                    "  $stmt = $pdo->prepare(",
                    "      'SELECT * FROM murid WHERE kelas = ? AND nilai >= ?');",
                    "  $stmt->execute([$kelas, $minimal]);",
                    "  $baris = $stmt->fetchAll();",
                    "",
                    "  // atau dengan nama",
                    "  $stmt = $pdo->prepare(",
                    "      'SELECT * FROM murid WHERE kelas = :kelas');",
                    "  $stmt->execute(['kelas' => $kelas]);",
                    "",
                    "Prepared statement wajib dipakai karena nilainya dikirim terpisah dari",
                    "perintah SQL-nya. Database menerima bentuk perintahnya dulu, baru",
                    "datanya. Jadi apa pun isi datanya, data itu nggak pernah bisa berubah",
                    "jadi perintah.",
                    "",
                    "  SALAH:  \"SELECT * FROM user WHERE nama = '$nama'\"",
                    "  BENAR:  prepare + execute",
                    "",
                    "Jangan pernah menyusun query dengan menyambung masukan pengguna ke",
                    "teks perintahnya. Di versi yang salah tadi, coba bayangkan $nama",
                    "berisi teks ini:",
                    "",
                    "  ' OR '1'='1",
                    "",
                    "Query-nya jadi mengembalikan seluruh tabel. Serangan ini namanya SQL",
                    "injection, dan sampai sekarang masih jadi salah satu celah paling umum",
                    "di web.",
                    "",
                    "Yang nggak bisa diikat (di-bind) ke prepared statement adalah nama",
                    "tabel dan nama kolom. Diikat artinya dikirim terpisah sebagai data.",
                    "Untuk nama tabel atau kolom, cocokkan dengan daftar putih, yaitu daftar",
                    "nilai yang boleh dipakai:",
                    "",
                    "  $boleh = ['nama', 'nilai', 'kelas'];",
                    "  $urut = in_array($_GET['urut'] ?? '', $boleh, true)",
                    "      ? $_GET['urut'] : 'nama';",
                    "",
                    "Argumen ketiga true membuat in_array membandingkan secara ketat (===).",
                ]
            },
            {
                "heading": "PDO dengan SQLite, lengkap",
                "code": """<?php

declare(strict_types=1);

$pdo = new PDO('sqlite::memory:', null, null, [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
]);

$pdo->exec('
    CREATE TABLE murid (
        id    INTEGER PRIMARY KEY,
        nama  TEXT    NOT NULL,
        kelas TEXT    NOT NULL,
        nilai INTEGER NOT NULL
    )
');

// --- Menyisipkan dengan prepared statement ---
$sisip = $pdo->prepare(
    'INSERT INTO murid (nama, kelas, nilai) VALUES (:nama, :kelas, :nilai)'
);

foreach ([
    ['Andi', 'A', 88],
    ['Budi', 'B', 72],
    ['Cici', 'A', 95],
    ['Dedi', 'B', 64],
] as [$nama, $kelas, $nilai]) {
    $sisip->execute(['nama' => $nama, 'kelas' => $kelas, 'nilai' => $nilai]);
}

// --- Query dengan parameter ---
$minimal = 75;
$cari = $pdo->prepare(
    'SELECT nama, kelas, nilai FROM murid WHERE nilai >= ? ORDER BY nilai DESC'
);
$cari->execute([$minimal]);

echo "Lulus (>= $minimal):\\n";
foreach ($cari->fetchAll() as $m) {
    printf("  %-6s %s %3d\\n", $m['nama'], $m['kelas'], $m['nilai']);
}

// --- Agregasi ---
$rekap = $pdo->query(
    'SELECT kelas, COUNT(*) AS jumlah, AVG(nilai) AS rata
     FROM murid GROUP BY kelas ORDER BY kelas'
);

echo "Rekap per kelas:\\n";
foreach ($rekap as $r) {
    printf("  Kelas %s: %d murid, rata-rata %.1f\\n",
           $r['kelas'], $r['jumlah'], $r['rata']);
}

// --- Transaksi ---
try {
    $pdo->beginTransaction();
    $pdo->prepare('UPDATE murid SET nilai = nilai + 5 WHERE kelas = ?')
        ->execute(['B']);
    $pdo->commit();
    echo "Transaksi berhasil\\n";
} catch (PDOException $e) {
    $pdo->rollBack();
    echo 'Transaksi dibatalkan: ' . $e->getMessage() . "\\n";
}

$total = $pdo->query('SELECT COUNT(*) FROM murid')->fetchColumn();
echo "Total murid: $total\\n";"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  Lulus (>= 75):",
                    "    Cici   A  95",
                    "    Andi   A  88",
                    "  Rekap per kelas:",
                    "    Kelas A: 2 murid, rata-rata 91.5",
                    "    Kelas B: 2 murid, rata-rata 68.0",
                    "  Transaksi berhasil",
                    "  Total murid: 4",
                    "",
                    "sqlite::memory: membuat database di RAM yang hilang begitu program",
                    "selesai. Ini pas untuk belajar dan untuk tes otomatis, karena setiap",
                    "kali jalan, database-nya mulai dari keadaan yang persis sama.",
                    "",
                    "PDOStatement adalah objek yang kamu dapat dari prepare() atau query().",
                    "Method-nya yang perlu kamu kenal:",
                    "  fetch()        satu baris berikutnya, false kalau habis",
                    "  fetchAll()     semua baris sekaligus",
                    "  fetchColumn()  satu nilai saja",
                    "  rowCount()     berapa baris terpengaruh (untuk",
                    "                 INSERT/UPDATE/DELETE)",
                    "",
                    "Untuk hasil yang besar, jangan pakai fetchAll(), karena semua barisnya",
                    "ditarik ke memori sekaligus. Telusuri langsung satu per satu:",
                    "  foreach ($stmt as $baris) { ... }",
                    "",
                    "Transaksi memastikan beberapa perubahan terjadi semuanya, atau nggak",
                    "terjadi sama sekali. Contohnya transfer saldo antar rekening. Tanpa",
                    "transaksi, ada jeda waktu ketika uang sudah dikurangi dari satu",
                    "rekening tapi belum ditambahkan ke rekening lain. Kalau server mati",
                    "tepat di saat itu, uangnya hilang.",
                    "",
                    "Di kode tadi, beginTransaction() memulai transaksi, commit() menyimpan",
                    "semua perubahannya, dan rollBack() membatalkan semuanya kalau ada yang",
                    "gagal.",
                    "",
                    "Hati-hati: di proyek sungguhan, kredensial database, yaitu nama",
                    "pengguna dan sandinya, nggak pernah ditulis di kode. Simpan di variabel",
                    "lingkungan atau di berkas .env, berkas berisi setelan rahasia yang",
                    "nggak ikut masuk ke git.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Setiap kali kasir minimarket menekan tombol bayar, aplikasinya mengubah",
                    "beberapa hal sekaligus di database: mencatat penjualan dan mengurangi",
                    "stok tiap barang. Kalau satu langkah gagal di tengah jalan, semuanya",
                    "harus batal. Kalau nggak, stok bisa berkurang padahal penjualannya",
                    "nggak pernah tercatat.",
                    "",
                    "Kasus kecil: pembeli membawa 2 gula dan 3 minyak goreng ke kasir. Stok",
                    "gula masih 5, sedangkan stok minyak tinggal 2. Transaksi ini harus",
                    "ditolak utuh, dan stok gula nggak boleh ikut berkurang.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Masukannya daftar kode barang beserta jumlahnya. Keluarannya",
                    "     transaksi yang tersimpan semua, atau nggak tersimpan sama sekali.",
                    "  2. Bungkus semua perubahan dengan beginTransaction() dan commit(),",
                    "     lalu panggil rollBack() di catch (RuntimeException $e).",
                    "     PDOException juga turunan RuntimeException, jadi ikut tertangkap.",
                    "  3. Kurangi stok dengan prepared statement yang sekaligus memeriksa",
                    "     stoknya cukup, lalu lihat rowCount():",
                    "      $kurangi = $pdo->prepare(",
                    "          'UPDATE barang SET stok = stok - ? WHERE kode = ? AND stok >= ?');",
                    "      $kurangi->execute([$qty, $kode, $qty]);",
                    "      if ($kurangi->rowCount() === 0) {",
                    "          throw new RuntimeException(\"stok $kode kurang\");",
                    "      }",
                    "  4. Ikuti kasusnya. Gula berhasil dikurangi jadi 3, lalu minyak gagal",
                    "     karena stoknya 2 sedangkan yang diminta 3. Exception itu membuat",
                    "     rollBack() jalan, dan stok gula kembali jadi 5.",
                    "",
                    "Jebakan: kalau stok diperiksa dengan SELECT dulu baru di-UPDATE, dua",
                    "kasir yang menjual barang terakhir di saat yang sama bisa sama-sama",
                    "lolos pemeriksaan. Syarat stok >= ? di dalam UPDATE mencegahnya.",
                ]
            },
        ],
    },
    {
        "title": "15. Composer, Autoload & Namespace",
        "sections": [
            {
                "body": [
                    "Namespace mencegah nama class bertabrakan antar pustaka. Ibaratnya",
                    "nama keluarga: dua orang boleh sama-sama bernama Budi asal keluarganya",
                    "beda.",
                    "",
                    "  <?php",
                    "  namespace Toko\\Domain;",
                    "",
                    "  class Produk { }      jadi Toko\\Domain\\Produk",
                    "",
                    "Pemisahnya garis miring terbalik (\\), bukan titik atau titik dua.",
                    "Deklarasi namespace harus jadi pernyataan pertama di berkas, tepat",
                    "sesudah <?php. Satu-satunya yang boleh mendahuluinya adalah declare,",
                    "misalnya declare(strict_types=1).",
                    "",
                    "  use Toko\\Domain\\Produk;",
                    "  use Toko\\Domain\\Produk as ProdukToko;",
                    "  use function Toko\\Util\\format;",
                    "  use const Toko\\Util\\VERSI;",
                    "",
                    "use membuat sebuah nama bisa ditulis pendek. Sesudah",
                    "use Toko\\Domain\\Produk; kamu cukup menulis Produk. as memberi nama",
                    "lain, sedangkan use function dan use const dipakai untuk fungsi dan",
                    "konstanta.",
                    "",
                    "Nama yang diawali garis miring terbalik adalah nama lengkap dari akar.",
                    "\\DateTime merujuk class bawaan PHP, bukan Toko\\Domain\\DateTime.",
                    "",
                    "Jebakan: di dalam namespace, class bawaan PHP harus diawali garis",
                    "miring terbalik atau di-use dulu. Kalau nggak, PHP mencarinya di",
                    "namespace-mu sendiri dan nggak ketemu. Ini kesalahan yang sering",
                    "terjadi waktu pertama kali memakai namespace.",
                    "",
                    "Composer adalah package manager PHP, yaitu alat untuk memasang dan",
                    "memperbarui pustaka buatan orang lain:",
                    "",
                    "  composer init                 buat composer.json",
                    "  composer require guzzlehttp/guzzle",
                    "  composer require --dev phpunit/phpunit",
                    "  composer install              pasang dari composer.lock",
                    "  composer update               perbarui, tulis lock baru",
                    "  composer dump-autoload -o     optimalkan autoloader",
                    "",
                    "composer require menambahkan sebuah pustaka ke proyekmu. Dengan --dev,",
                    "pustaka itu cuma dipakai selama pengembangan, misalnya untuk tes.",
                    "composer.lock mencatat versi persis setiap pustaka yang terpasang.",
                    "",
                    "Autoload artinya PHP memuat berkas sebuah class secara otomatis, waktu",
                    "class itu pertama kali dipakai. Autoload PSR-4 adalah kesepakatan yang",
                    "bikin semuanya jalan: nama namespace dipetakan ke struktur folder, jadi",
                    "PHP bisa menemukan berkas sebuah class cuma dari namanya, tanpa satu",
                    "pun require. require adalah perintah untuk memuat berkas PHP lain.",
                    "",
                    "  \"autoload\": {",
                    "      \"psr-4\": { \"Toko\\\\\": \"src/\" }",
                    "  }",
                    "",
                    "  Toko\\Domain\\Produk  ->  src/Domain/Produk.php",
                    "",
                    "Cukup tulis satu baris require 'vendor/autoload.php'; di titik masuk",
                    "aplikasi. Sesudah itu, semua class di proyekmu, beserta semua pustaka",
                    "yang dipasang, langsung bisa dipakai.",
                    "",
                    "PSR adalah standar yang disepakati komunitas PHP. Yang paling penting",
                    "diketahui:",
                    "  PSR-1 & PSR-12  gaya penulisan kode",
                    "  PSR-4           autoloading",
                    "  PSR-3           antarmuka logger",
                    "  PSR-7           pesan HTTP",
                    "  PSR-11          container",
                    "",
                    "composer.lock wajib masuk git untuk aplikasi. Berkas itulah yang",
                    "membuat pemasangan hari ini dan enam bulan lagi menghasilkan versi yang",
                    "persis sama. Untuk pustaka, composer.lock biasanya nggak ikut masuk",
                    "git.",
                ]
            },
            {
                "heading": "Struktur proyek PHP modern",
                "code": """proyekku/
├── composer.json
├── composer.lock          versi persis, masuk git untuk aplikasi
├── vendor/                dipasang composer, TIDAK masuk git
│   └── autoload.php
├── public/                satu-satunya folder yang boleh diakses web
│   └── index.php          titik masuk
├── src/
│   ├── Domain/
│   │   ├── Produk.php     Toko\\Domain\\Produk
│   │   └── Pesanan.php
│   ├── Repository/
│   │   └── ProdukRepository.php
│   └── Http/
│       └── ProdukController.php
├── tests/
│   └── Domain/ProdukTest.php
├── .env                   kredensial, TIDAK masuk git
└── .env.example           contohnya, masuk git"""
            },
            {
                "heading": "composer.json",
                "code": """{
    "name": "saya/toko",
    "require": {
        "php": ">=8.2",
        "vlucas/phpdotenv": "^5.6"
    },
    "require-dev": {
        "phpunit/phpunit": "^11.0"
    },
    "autoload": {
        "psr-4": { "Toko\\\\": "src/" }
    },
    "autoload-dev": {
        "psr-4": { "Toko\\\\Tests\\\\": "tests/" }
    },
    "scripts": {
        "test": "phpunit",
        "cs": "php-cs-fixer fix"
    }
}"""
            },
            {
                "body": [
                    "Bagian struktur yang paling sering salah, dan paling mahal akibatnya:",
                    "cuma folder public/ yang boleh dijangkau web server. Document root,",
                    "yaitu folder yang dibuka web server untuk pengunjung, diarahkan ke",
                    "situ, nggak ke akar proyek.",
                    "",
                    "Awas: kalau akar proyek yang diarahkan, siapa pun bisa membuka",
                    "https://situsmu.com/.env dan membaca sandi database-mu. Ini bukan",
                    "skenario teoretis. Pemindai otomatis mencoba alamat itu ke situs-situs",
                    "PHP di internet setiap hari.",
                    "",
                    "Berkas yang wajib masuk .gitignore:",
                    "  /vendor/",
                    "  /.env",
                    "  /node_modules/",
                    "  *.log",
                    "",
                    ".gitignore adalah daftar berkas yang nggak ikut disimpan ke git.",
                    "Sebaliknya, .env.example justru masuk git. Isinya nama-nama variabel",
                    "dengan nilai kosong, supaya orang berikutnya tahu apa saja yang harus",
                    "ia isi.",
                    "",
                    "Alat bantu yang layak dipasang sejak awal:",
                    "  phpunit          pengujian",
                    "  phpstan / psalm  analisis statis, menemukan bug tanpa",
                    "                   menjalankan kode",
                    "  php-cs-fixer     merapikan gaya penulisan otomatis",
                    "  rector           memodernkan kode lama secara otomatis",
                    "",
                    "PHPStan layak dapat perhatian khusus. Ia memeriksa tipe jauh lebih",
                    "dalam daripada PHP sendiri. Tanpa menjalankan satu baris pun, PHPStan",
                    "menemukan banyak jenis bug: property yang nggak pernah ada, method",
                    "yang salah nama, dan nilai null yang nggak diperiksa. Mulailah dari",
                    "level 5, lalu naikkan pelan-pelan.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Proyek PHP sungguhan, misalnya aplikasi Laravel, berisi banyak class",
                    "di banyak folder, ditambah pustaka yang dipasang lewat Composer. Nggak",
                    "ada yang menulis require untuk tiap berkas. Autoload PSR-4 menemukan",
                    "berkasnya dari nama class, asal namespace dan letak foldernya cocok.",
                    "",
                    "Kasus kecil: kamu menambah class Produk baru di proyek toko. Di laptop",
                    "Windows aplikasinya jalan, tapi begitu diunggah ke hosting Linux muncul",
                    "error Class \"Toko\\Domain\\Produk\" not found. Berkasnya bernama",
                    "src/Domain/produk.php.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Baca pesan errornya. PHP mencari class bernama lengkap",
                    "     Toko\\Domain\\Produk, dan autoloader mengubah nama itu jadi jalur",
                    "     berkas.",
                    "  2. Turunkan jalurnya sendiri dari aturan PSR-4 di composer.json:",
                    "      \"psr-4\": { \"Toko\\\\\": \"src/\" }",
                    "      Toko\\Domain\\Produk  ->  src/Domain/Produk.php",
                    "  3. Bandingkan dengan berkas yang ada. Linux membedakan huruf besar dan",
                    "     kecil di nama berkas, jadi produk.php dan Produk.php dianggap dua",
                    "     berkas berbeda. Windows nggak membedakannya, makanya error ini baru",
                    "     muncul di server.",
                    "  4. Ganti nama berkasnya jadi Produk.php, dan pastikan baris namespace",
                    "     di dalamnya persis Toko\\Domain. Kalau yang kamu ubah bagian",
                    "     autoload di composer.json, jalankan composer dump-autoload.",
                ]
            },
        ],
    },
    {
        "title": "16. Praktik Baik & Keamanan",
        "sections": [
            {
                "body": [
                    "Materi ini merangkum kesalahan yang paling sering terjadi di PHP, dan",
                    "yang paling mahal akibatnya kalau dibiarkan.",
                    "",
                    "Keamanan",
                    "  1. SQL injection: pakai prepared statement, selalu. Nggak ada",
                    "     pengecualian, termasuk alasan \"ini kan cuma id\".",
                    "  2. XSS: pakai htmlspecialchars di setiap titik keluaran. Escape",
                    "     dilakukan waktu menampilkan, jangan waktu menyimpan. Data yang",
                    "     sama bisa keluar ke HTML, ke JSON, dan ke email, dan cara",
                    "     escape-nya beda-beda.",
                    "  3. Password: pakai password_hash dan password_verify. Hash adalah",
                    "     hasil olahan sandi yang nggak bisa dibalik jadi sandi aslinya.",
                    "     Jangan pakai md5, sha1, atau algoritma cepat apa pun. Justru",
                    "     kelambatannya yang melindungi.",
                    "       $hash = password_hash($sandi, PASSWORD_DEFAULT);",
                    "       if (password_verify($sandi, $hash)) { ... }",
                    "  4. CSRF: pakai token per sesi, dan periksa dengan hash_equals.",
                    "  5. Unggahan berkas: jangan percaya nama maupun tipe berkas yang",
                    "     dikirim browser. Periksa isinya, ganti namanya, dan simpan di luar",
                    "     document root.",
                    "  6. Angka acak: pakai random_int(), jangan rand() atau mt_rand(). Dua",
                    "     yang terakhir bisa ditebak.",
                    "  7. Jangan pernah memakai eval(), extract(), atau unserialize() pada",
                    "     data dari pengguna. eval menjalankan teks sebagai kode PHP,",
                    "     extract mengubah isi array jadi variabel dan bisa menimpa variabel",
                    "     yang sudah ada, dan unserialize bisa membuat objek apa saja dari",
                    "     teks.",
                    "",
                    "Kualitas kode",
                    "  - declare(strict_types=1) di setiap berkas.",
                    "  - Tulis tipe di semua parameter dan nilai kembalian.",
                    "  - Pakai === dan !==, jangan == dan !=.",
                    "  - Jangan pakai @ untuk membungkam error.",
                    "  - Pulang lebih awal (guard clause), yaitu langsung return begitu",
                    "    syaratnya nggak terpenuhi, daripada menumpuk if bertingkat.",
                    "  - Satu class satu berkas, dan nama berkasnya sama dengan nama",
                    "    class-nya.",
                    "  - Untuk koleksi, kembalikan array kosong, jangan null.",
                    "",
                    "Penamaan menurut PSR-1, yang juga diikuti PSR-12:",
                    "  StudlyCaps   nama class, interface, trait, enum",
                    "  camelCase    nama method",
                    "  UPPER_CASE   konstanta",
                    "",
                    "StudlyCaps artinya tiap kata diawali huruf besar, misalnya",
                    "ProdukRepository. camelCase mirip, tapi huruf pertamanya kecil,",
                    "misalnya hitungTotal. Untuk property dan variabel, PSR nggak mewajibkan",
                    "gaya tertentu. Biasanya dipakai camelCase juga, tapi banyak proyek",
                    "memakai snake_case, dan dua-duanya sah asal konsisten di seluruh",
                    "proyek.",
                    "",
                    "Tata letak kode menurut PSR-12:",
                    "  - Indentasi empat spasi, jangan tab.",
                    "  - Kurung kurawal untuk class dan method ditaruh di baris baru.",
                    "  - Kurung kurawal untuk kendali alur (if, for, while, dan sejenisnya)",
                    "    ditaruh di baris yang sama.",
                ]
            },
            {
                "heading": "Perbandingan: rawan versus aman",
                "code": """<?php

declare(strict_types=1);

// ===================== RAWAN — JANGAN DITIRU =====================
//
// $id = $_GET['id'];
// $sql = "SELECT * FROM user WHERE id = $id";        <- SQL injection
// $baris = mysqli_query($conn, $sql);
//
// echo "Halo " . $_GET['nama'];                      <- XSS
//
// $hash = md5($_POST['sandi']);                      <- hash terlalu cepat
//
// if ($_POST['sandi'] == $sandiTersimpan) { ... }    <- == dan tak tetap-waktu
//
// $token = rand(100000, 999999);                     <- bisa ditebak

// ===================== AMAN =====================================

function e(?string $s): string
{
    return htmlspecialchars($s ?? '', ENT_QUOTES, 'UTF-8');
}

function cariUser(PDO $pdo, string $idMentah): ?array
{
    // 1. VALIDASI masukan
    $id = filter_var($idMentah, FILTER_VALIDATE_INT);
    if ($id === false || $id < 1) {
        return null;
    }

    // 2. PREPARED STATEMENT, nilai terpisah dari perintah
    $stmt = $pdo->prepare('SELECT id, nama FROM user WHERE id = ?');
    $stmt->execute([$id]);

    return $stmt->fetch() ?: null;
}

function daftarkan(PDO $pdo, string $nama, string $sandi): void
{
    if (mb_strlen($sandi) < 12) {
        throw new InvalidArgumentException('sandi minimal 12 karakter');
    }

    // 3. HASH yang memang dirancang lambat
    $hash = password_hash($sandi, PASSWORD_DEFAULT);

    $pdo->prepare('INSERT INTO user (nama, sandi) VALUES (?, ?)')
        ->execute([$nama, $hash]);
}

function masuk(PDO $pdo, string $nama, string $sandi): bool
{
    $stmt = $pdo->prepare('SELECT sandi FROM user WHERE nama = ?');
    $stmt->execute([$nama]);
    $baris = $stmt->fetch();

    // 4. Perbandingan tetap-waktu ada DI DALAM password_verify
    if ($baris === false || !password_verify($sandi, $baris['sandi'])) {
        return false;
    }

    session_regenerate_id(true);   // cegah fiksasi sesi
    return true;
}

// 5. Token acak yang aman secara kriptografis
$csrf = bin2hex(random_bytes(32));

// 6. ESCAPE saat menampilkan
$namaPengguna = '<script>alert(1)</script>';
echo 'Tanpa escape (BAHAYA): ' . $namaPengguna . "\\n";
echo 'Dengan escape (aman) : ' . e($namaPengguna) . "\\n";
echo 'Panjang token CSRF   : ' . strlen($csrf) . "\\n";
echo 'Hash sandi contoh    : ' . substr(password_hash('rahasia', PASSWORD_DEFAULT), 0, 7) . "...\\n";"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  Tanpa escape (BAHAYA): <script>alert(1)</script>",
                    "  Dengan escape (aman) : &lt;script&gt;alert(1)&lt;/script&gt;",
                    "  Panjang token CSRF   : 64",
                    "  Hash sandi contoh    : $2y$12$...",
                    "",
                    "Baris kedua menunjukkan cara kerja htmlspecialchars. Fungsi itu",
                    "mengubah karakter yang punya arti di HTML, seperti < dan >, jadi",
                    "entitas, yaitu kode pengganti seperti &lt; dan &gt;. Browser",
                    "menampilkannya sebagai teks biasa, dan nggak menjalankannya sebagai",
                    "skrip.",
                    "",
                    "$2y$12 di awal hash adalah penanda algoritma bcrypt dengan cost 12.",
                    "Cost adalah angka yang menentukan seberapa berat hitungannya, dan cost",
                    "itu yang membuat hash-nya lambat. Kelambatan itu memang gunanya. Kalau",
                    "database-mu dicuri, penyerang cuma bisa mencoba beberapa ribu tebakan",
                    "sandi per detik, padahal dengan hash yang cepat dia bisa mencoba",
                    "miliaran.",
                    "",
                    "password_hash menyimpan salt acak di dalam hasilnya sendiri, jadi kamu",
                    "nggak perlu menyimpan salt secara terpisah. Salt adalah tambahan acak",
                    "yang dicampur ke sandi sebelum di-hash. Makanya dua pengguna dengan",
                    "sandi yang sama tetap menghasilkan hash yang berbeda.",
                    "",
                    "Panggil password_needs_rehash() setiap kali login berhasil. Kalau",
                    "algoritma atau cost bawaan PHP naik di versi berikutnya, fungsi ini",
                    "memberi tahu bahwa hash lama perlu diperbarui. Waktu login, sandi",
                    "aslinya sedang ada di tanganmu, jadi kamu bisa langsung membuat hash",
                    "baru dan menyimpannya. Pengguna nggak perlu mengganti sandinya.",
                    "",
                    "Terakhir, satu kebiasaan yang manfaatnya besar: jalankan PHPStan level",
                    "6 ke atas pada proyekmu. PHPStan menemukan banyak jenis kesalahan,",
                    "seperti method yang salah nama, property yang nggak pernah ada, dan",
                    "nilai null yang nggak diperiksa, sebelum satu baris pun dijalankan.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Banyak aplikasi PHP lama, seperti sistem absensi atau aplikasi sekolah",
                    "yang dibuat bertahun-tahun lalu, menyimpan sandi pengguna sebagai md5.",
                    "Kalau database-nya bocor, sandi seperti itu cepat ditebak. Programmer",
                    "yang mewarisi aplikasi begini harus memindahkan semua sandi ke",
                    "password_hash tanpa menyuruh ratusan guru dan siswa membuat sandi baru.",
                    "",
                    "Kasus kecil: kolom sandi di tabel user berisi campuran hash md5 lama",
                    "dan hash baru dari password_hash. Fungsi masuk() harus menerima",
                    "keduanya, lalu mengganti hash lama begitu pemiliknya berhasil login.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Kenali dua bentuk hash itu. Hash md5 selalu 32 karakter",
                    "     heksadesimal (angka 0-9 dan huruf a-f). Hasil password_hash",
                    "     sekarang diawali $2y$ dan panjangnya 60 karakter.",
                    "  2. Sadari kapan kamu bisa memperbaikinya. Sandi asli cuma ada di",
                    "     tanganmu saat login, jadi di situlah hash barunya dibuat.",
                    "  3. Cocokkan sesuai bentuknya:",
                    "      if (strlen($tersimpan) === 32) {",
                    "          $cocok = hash_equals($tersimpan, md5($sandi));",
                    "          // kalau cocok: simpan password_hash($sandi, PASSWORD_DEFAULT)",
                    "      } else {",
                    "          $cocok = password_verify($sandi, $tersimpan);",
                    "      }",
                    "  4. Pakai hash_equals, jangan ==. Dua hash md5 berbeda yang kebetulan",
                    "     berbentuk 0e diikuti angka saja dianggap sama oleh ==, karena PHP",
                    "     membaca keduanya sebagai 0 kali 10 pangkat sekian, yaitu nol.",
                ]
            },
        ],
    },
    {
        "title": "17. Tanggal & Waktu",
        "sections": [
            {
                "body": [
                    "PHP punya dua cara mengurus tanggal dan waktu, dan cara yang lama",
                    "sebaiknya ditinggalkan:",
                    "  - Cara lama: date(), time(), strtotime(), dan mktime(). Semuanya",
                    "    berbasis timestamp, yaitu jumlah detik sejak 1 Januari 1970, yang",
                    "    disimpan sebagai integer. Masih banyak dipakai, tapi nggak membawa",
                    "    zona waktu dan gampang salah.",
                    "  - Cara baru: DateTimeImmutable, DateTime, DateInterval, DateTimeZone,",
                    "    dan DatePeriod. Semuanya berupa objek.",
                    "",
                    "Pakai DateTimeImmutable, jangan DateTime. Immutable artinya nggak bisa",
                    "diubah, sama seperti String di bahasa lain. Method pada DateTime",
                    "mengubah objek aslinya, sedangkan DateTimeImmutable selalu",
                    "mengembalikan objek baru. Perilaku DateTime itu sumber bug yang susah",
                    "dilihat:",
                    "",
                    "  $besok = $hari->modify('+1 day');",
                    "  // dengan DateTime, $hari IKUT berubah jadi besok",
                    "",
                    "Membuat objek tanggal:",
                    "  new DateTimeImmutable()              sekarang",
                    "  new DateTimeImmutable('2026-09-22')",
                    "  new DateTimeImmutable('+3 days')",
                    "  DateTimeImmutable::createFromFormat('d/m/Y', '22/09/2026')",
                    "",
                    "Memformat tanggal jadi teks:",
                    "  $d->format('Y-m-d')        2026-09-22",
                    "  $d->format('d/m/Y H:i')    22/09/2026 14:30",
                    "  $d->format('l, j F Y')     Tuesday, 22 September 2026",
                    "",
                    "Huruf format yang sering dipakai:",
                    "  Y  tahun 4 digit      y  tahun 2 digit",
                    "  m  bulan 01-12        n  bulan 1-12",
                    "  d  tanggal 01-31      j  tanggal 1-31",
                    "  H  jam 00-23          G  jam 0-23",
                    "  i  menit 00-59        s  detik 00-59",
                    "  D  Mon                l  Monday",
                    "  M  Jan                F  January",
                    "  N  1=Senin..7=Minggu  w  0=Minggu..6=Sabtu",
                    "",
                    "Nama hari dan bulan dari format() selalu dalam bahasa Inggris, seperti",
                    "Tuesday dan September.",
                    "",
                    "Zona waktu adalah sumber bug nomor satu di aplikasi yang dipakai di",
                    "banyak wilayah. Aturan praktisnya:",
                    "  - Simpan semua waktu di database dalam UTC, yaitu waktu patokan",
                    "    dunia. Jam di Jakarta tujuh jam lebih cepat dari UTC.",
                    "  - Ubah ke zona waktu pengguna cuma waktu menampilkan.",
                    "  - Setel date_default_timezone_set('UTC') di awal program.",
                ]
            },
            {
                "heading": "Menghitung selisih dan rentang",
                "code": """<?php

declare(strict_types=1);

date_default_timezone_set('UTC');

$mulai = new DateTimeImmutable('2026-01-15 09:00:00');
$selesai = new DateTimeImmutable('2026-09-22 17:30:00');

echo 'mulai   : ' . $mulai->format('l, j F Y H:i') . "\\n";
echo 'selesai : ' . $selesai->format('l, j F Y H:i') . "\\n";

$beda = $mulai->diff($selesai);
printf("selisih : %d tahun %d bulan %d hari (%d hari total)\\n",
       $beda->y, $beda->m, $beda->d, $beda->days);

// Immutable: yang asli TIDAK berubah
$besok = $mulai->modify('+1 day');
echo 'asli    : ' . $mulai->format('Y-m-d') . "\\n";
echo 'besok   : ' . $besok->format('Y-m-d') . "\\n";

// Menambah dengan DateInterval
$jatuhTempo = $mulai->add(new DateInterval('P30D'));
echo 'tempo   : ' . $jatuhTempo->format('Y-m-d') . "\\n";

// Rentang: tiap 7 hari selama 4 minggu
echo "jadwal  :\\n";
$periode = new DatePeriod(
    $mulai,
    new DateInterval('P7D'),
    $mulai->add(new DateInterval('P28D')),
);
foreach ($periode as $tanggal) {
    echo '  ' . $tanggal->format('D, d M Y') . "\\n";
}

// Zona waktu
$jakarta = $selesai->setTimezone(new DateTimeZone('Asia/Jakarta'));
echo 'UTC     : ' . $selesai->format('Y-m-d H:i T') . "\\n";
echo 'Jakarta : ' . $jakarta->format('Y-m-d H:i T') . "\\n";"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  mulai   : Thursday, 15 January 2026 09:00",
                    "  selesai : Tuesday, 22 September 2026 17:30",
                    "  selisih : 0 tahun 8 bulan 7 hari (250 hari total)",
                    "  asli    : 2026-01-15",
                    "  besok   : 2026-01-16",
                    "  tempo   : 2026-02-14",
                    "  jadwal  :",
                    "    Thu, 15 Jan 2026",
                    "    Thu, 22 Jan 2026",
                    "    Thu, 29 Jan 2026",
                    "    Thu, 05 Feb 2026",
                    "  UTC     : 2026-09-22 17:30 UTC",
                    "  Jakarta : 2026-09-23 00:30 WIB",
                    "",
                    "diff() menghasilkan objek DateInterval. Isinya y, m, dan d untuk",
                    "selisih tahun, bulan, dan hari, sedangkan days berisi jumlah harinya",
                    "secara total.",
                    "",
                    "Dua baris terakhir menunjukkan kenapa zona waktu penting. Waktu yang",
                    "persis sama bisa jatuh di tanggal yang berbeda, tergantung dari mana",
                    "orang melihatnya: 22 September di UTC, tapi sudah 23 September di",
                    "Jakarta. Laporan \"penjualan hari ini\" yang dihitung tanpa zona waktu",
                    "bakal salah untuk sebagian penggunamu, setiap hari.",
                    "",
                    "Format DateInterval memakai notasi ISO 8601:",
                    "  P1Y      1 tahun       P30D     30 hari",
                    "  P3M      3 bulan       PT2H     2 jam",
                    "  P1W      1 minggu      PT30M    30 menit",
                    "  P1Y2M3D  gabungan      PT1H30M  1 jam 30 menit",
                    "",
                    "Huruf P artinya period (jangka waktu), dan huruf T memisahkan bagian",
                    "tanggal dari bagian waktu. Jadi P1M artinya satu bulan, sedangkan PT1M",
                    "artinya satu menit.",
                    "",
                    "Jebakan: menambah satu bulan ke 2026-01-31 menghasilkan 2026-03-03,",
                    "nggak berhenti di akhir Februari. Tanggal 31 Februari nggak ada, jadi",
                    "PHP melimpahkan kelebihannya ke bulan berikutnya. Kalau yang kamu mau",
                    "\"akhir bulan berikutnya\", pakai modify('last day of next month').",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Perpustakaan sekolah, rental, dan tagihan cicilan semuanya menghitung",
                    "jatuh tempo dan keterlambatan. Aplikasi kasir juga butuh tanggal untuk",
                    "laporan harian, dan di situ zona waktu ikut menentukan transaksi tengah",
                    "malam masuk ke hari yang mana.",
                    "",
                    "Kasus kecil: siswa meminjam buku tanggal 1 September 2026 dengan masa",
                    "pinjam 7 hari, dan dendanya Rp500 per hari terlambat. Bukunya",
                    "dikembalikan tanggal 12 September. Berapa dendanya?",
                    "",
                    "Cara memecahkannya:",
                    "  1. Masukannya dua tanggal dan dua angka aturan. Keluarannya jumlah",
                    "     hari terlambat dan dendanya.",
                    "  2. Hitung jatuh temponya dulu: tanggal pinjam ditambah P7D, yaitu",
                    "     8 September.",
                    "  3. Bandingkan tanggal kembali dengan jatuh tempo. Objek",
                    "     DateTimeImmutable bisa dibandingkan langsung pakai > dan <:",
                    "      $pinjam = new DateTimeImmutable('2026-09-01');",
                    "      $kembali = new DateTimeImmutable('2026-09-12');",
                    "      $tempo = $pinjam->add(new DateInterval('P7D'));",
                    "      $telat = $kembali > $tempo ? $tempo->diff($kembali)->days : 0;",
                    "      echo 'Denda: Rp' . ($telat * 500) . \"\\n\";",
                    "     Hasilnya terlambat 4 hari, dan dendanya Rp2000.",
                    "  4. Uji buku yang kembali lebih awal, misalnya 5 September. Nilai days",
                    "     dari diff() selalu positif, jadi tanpa pemeriksaan > tadi, siswa",
                    "     yang mengembalikan lebih cepat malah kena denda 3 hari.",
                    "",
                    "Ingat: buat tanggalnya tanpa jam. Kalau ada jam, days cuma menghitung",
                    "hari yang sudah genap 24 jam, dan keterlambatannya bisa kurang satu.",
                ]
            },
        ],
    },
    {
        "title": "18. Ekspresi Reguler",
        "sections": [
            {
                "body": [
                    "Ekspresi reguler, atau regex, adalah pola untuk mencari dan",
                    "mencocokkan teks. PHP memakai PCRE (Perl Compatible Regular",
                    "Expressions). Polanya ditulis sebagai string, dengan pembatas di kedua",
                    "ujungnya. Biasanya pembatasnya garis miring:",
                    "",
                    "  '/^\\d{4}-\\d{2}-\\d{2}$/'",
                    "",
                    "Pola di atas cocok dengan teks seperti 2026-09-22: empat angka, tanda",
                    "hubung, dua angka, tanda hubung, lalu dua angka.",
                    "",
                    "Pembatasnya boleh diganti karakter lain, asal bukan huruf, angka,",
                    "garis miring terbalik, atau spasi, dan dipasang di kedua ujungnya.",
                    "Kalau polanya memuat banyak garis miring, misalnya URL, pakai pembatas",
                    "lain supaya garis miringnya nggak perlu di-escape satu per satu:",
                    "  '~https?://~'",
                    "",
                    "Fungsi utamanya:",
                    "  preg_match($pola, $teks, $cocok)    0 atau 1, sekali",
                    "  preg_match_all($pola, $teks, $semua) berapa kali cocok",
                    "  preg_replace($pola, $ganti, $teks)",
                    "  preg_replace_callback($pola, $fn, $teks)",
                    "  preg_split($pola, $teks)",
                    "  preg_quote($teks)                   escape karakter khusus",
                    "",
                    "preg_match, preg_match_all, dan preg_split mengembalikan false kalau",
                    "polanya rusak. Periksa dengan === false, jangan dengan !, karena 0",
                    "(nggak ada yang cocok) juga dianggap false. preg_replace dan",
                    "preg_replace_callback mengembalikan null kalau gagal.",
                    "",
                    "Bahan pola yang paling sering dipakai:",
                    "  .        karakter apa pun kecuali baris baru",
                    "  \\d \\w \\s angka, huruf/angka/garis bawah, spasi",
                    "  \\D \\W \\S kebalikannya",
                    "  [abc]    salah satu dari a, b, c",
                    "  [^abc]   selain itu",
                    "  [a-z]    rentang",
                    "  ^  $     awal dan akhir teks (atau baris, dengan m)",
                    "  \\b       batas kata",
                    "",
                    "  *        nol atau lebih       +   satu atau lebih",
                    "  ?        nol atau satu        {3} tepat tiga",
                    "  {2,5}    dua sampai lima      {2,} dua atau lebih",
                    "  *?  +?   versi malas (ambil sesedikit mungkin)",
                    "",
                    "  (...)    grup penangkap",
                    "  (?:...)  grup tanpa menangkap",
                    "  (?<nama>...)  grup bernama",
                    "  a|b      salah satu",
                    "",
                    "Penanda (modifier) ditulis sesudah pembatas penutup, misalnya '/abc/i':",
                    "  i  abaikan besar-kecil huruf",
                    "  m  ^ dan $ berlaku per baris",
                    "  s  titik juga cocok dengan baris baru",
                    "  u  perlakukan pola dan teks sebagai UTF-8",
                    "  x  abaikan spasi di pola, supaya bisa diberi komentar",
                    "",
                    "Penanda u hampir selalu perlu begitu teksnya nggak murni ASCII (huruf",
                    "Latin dasar tanpa aksen). Ini termasuk teks berbahasa Indonesia dari",
                    "pengguna, yang bisa saja memuat huruf beraksen. Tanpa u, satu huruf",
                    "beraksen dihitung sebagai beberapa karakter.",
                ]
            },
            {
                "heading": "Menguraikan log dengan regex",
                "code": """<?php

declare(strict_types=1);

$log = <<<'LOG'
2026-09-22 09:15:03 INFO  masuk user=andi ip=10.0.0.5
2026-09-22 09:15:44 WARN  gagal user=budi ip=10.0.0.9 percobaan=3
2026-09-22 09:16:10 ERROR koneksi putus ip=10.0.0.9
baris yang formatnya tidak dikenal
2026-09-22 09:17:55 INFO  keluar user=andi ip=10.0.0.5
LOG;

$pola = '/^(?<tanggal>\\d{4}-\\d{2}-\\d{2})\\s+'
      . '(?<jam>\\d{2}:\\d{2}:\\d{2})\\s+'
      . '(?<taraf>INFO|WARN|ERROR)\\s+'
      . '(?<pesan>.+)$/m';

preg_match_all($pola, $log, $semua, PREG_SET_ORDER);

printf("%-10s%-6s%s\\n", 'jam', 'taraf', 'pesan');
echo str_repeat('-', 56) . "\\n";
foreach ($semua as $b) {
    printf("%-10s%-6s%s\\n", $b['jam'], $b['taraf'], $b['pesan']);
}

echo "---\\n";
echo 'baris dikenali : ' . count($semua) . "\\n";

$taraf = array_count_values(array_column($semua, 'taraf'));
ksort($taraf);
foreach ($taraf as $t => $n) {
    echo "  $t: $n\\n";
}

echo "---\\n";
// Mengambil semua IP unik
preg_match_all('/ip=(\\d{1,3}(?:\\.\\d{1,3}){3})/', $log, $ip);
$unik = array_unique($ip[1]);
sort($unik);
echo 'IP unik: ' . implode(', ', $unik) . "\\n";

// Menyamarkan oktet terakhir
$samar = preg_replace('/(ip=\\d{1,3}\\.\\d{1,3}\\.\\d{1,3})\\.\\d{1,3}/', '$1.xxx', $log);
echo "---\\n";
echo explode("\\n", $samar)[0] . "\\n";

// Validasi
foreach (['2026-09-22', '22/09/2026', '2026-13-40'] as $teks) {
    $sah = preg_match('/^\\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\\d|3[01])$/', $teks);
    printf("%-12s -> %s\\n", $teks, $sah ? 'sah' : 'tidak sah');
}"""
            },
            {
                "body": [
                    "Keluaran:",
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
                    "  ---",
                    "  2026-09-22 09:15:03 INFO  masuk user=andi ip=10.0.0.xxx",
                    "  2026-09-22   -> sah",
                    "  22/09/2026   -> tidak sah",
                    "  2026-13-40   -> tidak sah",
                    "",
                    "Baris yang formatnya nggak dikenal dilewati begitu aja. Itu gunanya",
                    "^...$ dengan penanda m: seluruh baris harus cocok, nggak cukup",
                    "sepotong di tengahnya.",
                    "",
                    "Grup bernama (?<tanggal>...) membuat hasilnya bisa dibaca lewat",
                    "$b['tanggal'], nggak perlu $b[1]. Untuk pola yang grupnya lebih dari",
                    "dua, ini mengurangi banyak kebingungan waktu polanya nanti disunting.",
                    "",
                    "PREG_SET_ORDER mengelompokkan hasil per kecocokan. Tanpa flag itu,",
                    "yang dipakai bawaannya, PREG_PATTERN_ORDER, dan hasilnya dikelompokkan",
                    "per grup. Bentuk itu jauh lebih susah ditelusuri.",
                    "",
                    "Jangan mengurai HTML dengan regex. HTML bisa bersarang tanpa batas,",
                    "dan regex nggak bisa menghitung kedalaman sarangnya. Pakai DOMDocument.",
                    "Regex cocok untuk format yang berbaris dan polanya tetap, seperti log,",
                    "CSV sederhana, dan validasi.",
                    "",
                    "Hati-hati juga dengan catastrophic backtracking, yaitu pencocokan yang",
                    "jumlah percobaannya meledak. Pola seperti (a+)+$ pada teks panjang bisa",
                    "begitu: waktunya kira-kira berlipat dua setiap kali teksnya bertambah",
                    "satu huruf. PHP memasang batas (pcre.backtrack_limit), jadi",
                    "pencocokannya dihentikan, lalu fungsinya mengembalikan false, atau null",
                    "untuk preg_replace. Kalau hasilnya nggak dicek, kegagalan itu terlihat",
                    "seperti \"nggak ada yang cocok\". Hindari kuantifier bersarang, yaitu",
                    "pengulang di dalam pengulang seperti (a+)+.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Form pendaftaran, misalnya pendaftaran siswa baru atau akun toko",
                    "online, hampir selalu meminta nomor HP. Orang mengetiknya dengan gaya",
                    "masing-masing: pakai spasi, tanda hubung, atau +62 di depan. Sebelum",
                    "disimpan atau dipakai mengirim pesan, nomor itu dirapikan dan diperiksa",
                    "bentuknya, dan regex cocok untuk pekerjaan ini.",
                    "",
                    "Kasus kecil: ada tiga isian, yaitu 0812-3456-7890, +62 812 3456 7890,",
                    "dan 08123. Anggap aturannya begini: nomor diawali 08 atau +628, dan",
                    "kalau ditulis dengan awalan 0, panjangnya 10 sampai 13 angka. Dua",
                    "isian pertama sah, yang ketiga terlalu pendek.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pecah jadi dua langkah: buang pemisahnya dulu, baru periksa",
                    "     polanya. Pola yang harus menampung spasi dan tanda hubung di",
                    "     sembarang tempat jauh lebih susah dibaca.",
                    "  2. Buang spasi dan tanda hubung dengan preg_replace, lalu periksa",
                    "     dengan preg_match. Tanda + di pola di-escape, karena tanpa garis",
                    "     miring terbalik artinya \"satu atau lebih\":",
                    "      $hp = preg_replace('/[\\s-]/', '', $masukan);",
                    "      $sah = preg_match('/^(?:\\+62|0)8\\d{8,11}$/', $hp);",
                    "  3. Pertahankan ^ dan $. Tanpa keduanya, nomor 16 angka seperti",
                    "     0812345678901234 ikut lolos, karena potongan di awalnya sudah",
                    "     cocok dengan pola.",
                    "  4. Simpan dalam satu bentuk saja. preg_replace('/^(?:\\+62|0)/', '62',",
                    "     $hp) mengubah dua isian pertama jadi 6281234567890, jadi nomor yang",
                    "     sama nggak tersimpan dua kali dengan tulisan berbeda.",
                ]
            },
        ],
    },
    {
        "title": "19. Generator & Iterator",
        "sections": [
            {
                "body": [
                    "Fungsi biasa menghitung seluruh hasilnya dulu, lalu mengembalikannya",
                    "sekaligus. Untuk sejuta baris, artinya ada sejuta baris di memori.",
                    "",
                    "Generator menghasilkan nilai satu per satu, cuma waktu diminta.",
                    "Tandanya kata kunci yield:",
                    "",
                    "  function angka(int $n): Generator",
                    "  {",
                    "      for ($i = 1; $i <= $n; $i++) {",
                    "          yield $i;",
                    "      }",
                    "  }",
                    "",
                    "  foreach (angka(1_000_000) as $x) { ... }",
                    "",
                    "Garis bawah di 1_000_000 cuma pemisah supaya angkanya gampang dibaca",
                    "(boleh sejak PHP 7.4).",
                    "",
                    "Memori yang terpakai cuma untuk satu angka setiap saat, berapa pun",
                    "jumlah totalnya. Begitu sebuah fungsi memuat yield, fungsi itu otomatis",
                    "jadi generator. Memanggilnya nggak menjalankan isi fungsinya sama",
                    "sekali, sampai ada yang mulai menelusuri hasilnya.",
                    "",
                    "yield juga bisa membawa kunci:",
                    "  yield $nama => $nilai;",
                    "",
                    "yield from meneruskan semua nilai dari generator lain:",
                    "  yield from generatorLain();",
                    "",
                    "Generator juga bisa mengembalikan nilai akhir:",
                    "  return $total;      dibaca dengan $gen->getReturn()",
                    "",
                    "Pemakaian generator yang paling berharga adalah membaca berkas besar:",
                    "",
                    "  function baris(string $path): Generator",
                    "  {",
                    "      $f = fopen($path, 'r');",
                    "      try {",
                    "          while (($b = fgets($f)) !== false) {",
                    "              yield rtrim($b, \"\\r\\n\");",
                    "          }",
                    "      } finally {",
                    "          fclose($f);",
                    "      }",
                    "  }",
                    "",
                    "Dengan cara ini, berkas 10 GB bisa diproses di mesin dengan RAM 512 MB.",
                    "finally memastikan berkasnya ditutup, walaupun penelusurannya",
                    "dihentikan di tengah jalan dengan break.",
                    "",
                    "Iterator adalah bentuk panjangnya: sebuah class yang memakai interface",
                    "Iterator, dengan lima method: current, key, next, rewind, dan valid.",
                    "Generator mengerjakan hal yang sama cukup dengan beberapa baris. Jadi",
                    "pakai generator, kecuali kamu butuh keadaan yang rumit.",
                    "",
                    "IteratorAggregate lebih sering berguna. Cukup tulis method",
                    "getIterator(), dan objekmu langsung bisa di-foreach.",
                ]
            },
            {
                "heading": "Generator untuk aliran data",
                "code": """<?php

declare(strict_types=1);

/** Deret Fibonacci tanpa batas — mustahil ditulis sebagai array. */
function fibonacci(): Generator
{
    [$a, $b] = [0, 1];
    while (true) {
        yield $a;
        [$a, $b] = [$b, $a + $b];
    }
}

/** Ambil n pertama dari generator apa pun. */
function ambil(iterable $sumber, int $n): Generator
{
    $i = 0;
    foreach ($sumber as $x) {
        if ($i++ >= $n) {
            return;
        }
        yield $x;
    }
}

/** Saring, tetap malas. */
function saring(iterable $sumber, callable $syarat): Generator
{
    foreach ($sumber as $x) {
        if ($syarat($x)) {
            yield $x;
        }
    }
}

/** Generator yang mengembalikan nilai akhir. */
function jumlahkan(iterable $sumber): Generator
{
    $total = 0;
    foreach ($sumber as $x) {
        $total += $x;
        yield $x;
    }
    return $total;
}

echo '10 fibonacci pertama : ';
echo implode(', ', iterator_to_array(ambil(fibonacci(), 10))) . "\\n";

echo 'yang genap (6 buah)  : ';
$genap = ambil(saring(fibonacci(), fn(int $x): bool => $x % 2 === 0), 6);
echo implode(', ', iterator_to_array($genap)) . "\\n";

$gen = jumlahkan(ambil(fibonacci(), 10));
foreach ($gen as $_) {
    // sengaja dikosongkan: yang dicari nilai akhirnya
}
echo 'total 10 pertama     : ' . $gen->getReturn() . "\\n";

echo "---\\n";

/** Kelas yang bisa di-foreach lewat IteratorAggregate. */
final class Kelas implements IteratorAggregate, Countable
{
    /** @var array<string, int> */
    private array $murid = [];

    public function tambah(string $nama, int $nilai): void
    {
        $this->murid[$nama] = $nilai;
    }

    public function getIterator(): Generator
    {
        arsort($this->murid);
        foreach ($this->murid as $nama => $nilai) {
            yield $nama => $nilai;
        }
    }

    public function count(): int
    {
        return count($this->murid);
    }
}

$k = new Kelas();
$k->tambah('Andi', 88);
$k->tambah('Budi', 72);
$k->tambah('Cici', 95);

foreach ($k as $nama => $nilai) {
    printf("%-6s %3d\\n", $nama, $nilai);
}
echo 'jumlah murid: ' . count($k) . "\\n";"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  10 fibonacci pertama : 0, 1, 1, 2, 3, 5, 8, 13, 21, 34",
                    "  yang genap (6 buah)  : 0, 2, 8, 34, 144, 610",
                    "  total 10 pertama     : 88",
                    "  ---",
                    "  Cici    95",
                    "  Andi    88",
                    "  Budi    72",
                    "  jumlah murid: 3",
                    "",
                    "fibonacci() adalah deret tanpa batas. Menulisnya sebagai array",
                    "mustahil, tapi sebagai generator dia wajar dan aman, karena ambil()",
                    "berhenti meminta begitu jumlahnya cukup.",
                    "",
                    "saring() juga generator, jadi rantai ini tetap malas dari ujung ke",
                    "ujung:",
                    "  ambil(saring(fibonacci(), ...), 6)",
                    "",
                    "Malas artinya nilai baru dihitung waktu diminta. Nggak ada satu pun",
                    "array perantara yang dibuat. Ini pola yang sama dengan iterator di",
                    "Rust dan LINQ di C#.",
                    "",
                    "Hati-hati dengan iterator_to_array(). Fungsi ini memaksa generator",
                    "jalan sampai habis, lalu mengumpulkan hasilnya jadi array. Untuk",
                    "generator tanpa batas, iterator_to_array() cuma aman kalau",
                    "generatornya sudah dibatasi. Kalau dipanggil langsung pada",
                    "fibonacci(), program bakal menggantung sampai memorinya habis.",
                    "",
                    "IteratorAggregate memberi class-mu kemampuan di-foreach cukup dengan",
                    "satu method. Countable membuat count($objek) jalan. Keduanya contoh",
                    "dari prinsip yang berlaku di seluruh PHP: kalau objekmu memakai",
                    "interface bawaan yang tepat, objek itu bisa langsung dipakai dengan",
                    "sintaks bahasanya sendiri, seperti foreach dan count().",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Riwayat transaksi toko online yang ramai, kalau diekspor ke CSV, bisa",
                    "berisi jutaan baris, dan laporan bulanannya dihitung dari berkas itu.",
                    "Batas memori bawaan PHP (memory_limit) cuma 128 MB. Membaca seluruh",
                    "berkas ke array dengan file() bisa menghabiskan batas itu, sedangkan",
                    "generator cuma memegang satu baris setiap saat.",
                    "",
                    "Kasus kecil: transaksi.csv berisi kolom id, status, dan jumlah, dengan",
                    "dua juta baris. Hitung total transaksi berstatus sukses tanpa",
                    "melewati batas memori.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Masukannya berkas besar, keluarannya satu angka. Kamu nggak butuh",
                    "     semua baris sekaligus, cukup satu baris di setiap langkah.",
                    "  2. Buat generator transaksi() seperti baris() di materi ini: buka",
                    "     berkas dengan fopen, buang baris judul, yield hasil fgetcsv satu",
                    "     per satu, dan tutup berkasnya di finally.",
                    "  3. Jumlahkan dengan foreach biasa. Pemakainya nggak perlu tahu bahwa",
                    "     datanya datang dari generator:",
                    "      $total = 0;",
                    "      foreach (transaksi('transaksi.csv') as [$id, $status, $jumlah]) {",
                    "          if ($status === 'sukses') {",
                    "              $total += (int) $jumlah;",
                    "          }",
                    "      }",
                    "  4. Periksa baris kosong, yang sering ada di akhir berkas. fgetcsv",
                    "     mengembalikan [null] untuk baris kosong, jadi di dalam generator,",
                    "     lewati baris yang kolomnya kurang dari tiga.",
                    "",
                    "Jebakan: iterator_to_array(transaksi('transaksi.csv')) mengumpulkan",
                    "semua baris jadi array lagi, dan penghematan memorinya hilang.",
                ]
            },
        ],
    },
    {
        "title": "20. Anggota Statis & Method Ajaib",
        "sections": [
            {
                "body": [
                    "Anggota statis adalah property, method, atau konstanta milik class itu",
                    "sendiri, bukan milik salah satu objeknya:",
                    "",
                    "  class Penghitung",
                    "  {",
                    "      private static int $jumlah = 0;",
                    "      public const BATAS = 100;",
                    "",
                    "      public static function naik(): int",
                    "      {",
                    "          return ++self::$jumlah;",
                    "      }",
                    "  }",
                    "",
                    "  Penghitung::naik();",
                    "  echo Penghitung::BATAS;",
                    "",
                    "Di dalam method statis nggak ada $this, karena nggak ada objek yang",
                    "sedang dikerjakan. Yang tersedia self:: dan static::.",
                    "",
                    "Beda self:: dan static:: sering menjebak:",
                    "  self::     merujuk class tempat kode itu ditulis",
                    "  static::   merujuk class yang dipakai waktu memanggil",
                    "",
                    "Yang kedua disebut late static binding. Fitur ini yang membuat method",
                    "pabrik (factory), yaitu method yang tugasnya membuat objek, di class",
                    "induk bisa menghasilkan objek turunan:",
                    "",
                    "  public static function buat(): static",
                    "  {",
                    "      return new static();",
                    "  }",
                    "",
                    "Kalau ditulis new self(), Turunan::buat() menghasilkan objek induk,",
                    "dan hampir pasti itu bukan yang kamu maksud.",
                    "",
                    "Method ajaib di judul materi ini adalah magic method, yang sudah kamu",
                    "kenal di materi Class & Objek. PHP memanggilnya sendiri pada saat",
                    "tertentu:",
                    "",
                    "  __construct / __destruct",
                    "  __toString()      objek dipakai sebagai string",
                    "  __get / __set     akses property yang tidak ada",
                    "  __isset / __unset",
                    "  __call            method instance tidak ada",
                    "  __callStatic      method statis tidak ada",
                    "  __invoke          objeknya dipanggil seperti fungsi",
                    "  __clone           sesudah objek disalin",
                    "  __serialize / __unserialize",
                    "",
                    "Hati-hati: magic method bikin kode susah dilacak. Editor nggak bisa",
                    "melengkapi nama secara otomatis, alat analisis statis nggak bisa",
                    "melihat isinya, dan salah ketik nama property malah diterima begitu",
                    "aja oleh __set. Pakai seperlunya. Kalau kamu memakai __get atau",
                    "__call, sertakan anotasi @property dan @method (komentar khusus",
                    "berbentuk /** ... */) supaya editor dan alat analisis tetap mengerti.",
                    "",
                    "__clone penting untuk salinan dalam (deep copy). clone $objek cuma",
                    "membuat salinan dangkal, jadi property yang berupa objek tetap dipakai",
                    "bersama oleh objek asli dan salinannya.",
                ]
            },
            {
                "heading": "Statis, late static binding, dan __clone",
                "code": """<?php

declare(strict_types=1);

abstract class Model
{
    private static array $terbuat = [];

    public function __construct(public readonly string $id)
    {
        $nama = static::class;
        self::$terbuat[$nama] = (self::$terbuat[$nama] ?? 0) + 1;
    }

    // `static` bukan `self`: menghasilkan objek class yang MEMANGGIL
    public static function buat(string $id): static
    {
        return new static($id);
    }

    public static function statistik(): array
    {
        ksort(self::$terbuat);
        return self::$terbuat;
    }
}

final class Produk extends Model
{
    public function __construct(string $id, public array $tag = [])
    {
        parent::__construct($id);
    }

    // Tanpa ini, $tag akan dibagi dua objek -- tapi array di PHP
    // disalin saat ditugaskan, jadi yang benar-benar perlu __clone
    // adalah property yang berupa OBJEK. Lihat Keranjang di bawah.
    public function __toString(): string
    {
        return "Produk#{$this->id}[" . implode(',', $this->tag) . ']';
    }
}

final class Pesanan extends Model {}

final class Keranjang
{
    public function __construct(public ArrayObject $isi) {}

    public function __clone(): void
    {
        // Salinan DALAM: tanpa baris ini, dua keranjang berbagi satu isi
        $this->isi = clone $this->isi;
    }
}

$a = Produk::buat('P1');
$b = Produk::buat('P2');
$c = Pesanan::buat('O1');

echo 'kelas $a : ' . $a::class . "\\n";
echo 'kelas $c : ' . $c::class . "\\n";

foreach (Model::statistik() as $kelas => $n) {
    echo "  $kelas: $n\\n";
}

echo "---\\n";
$k1 = new Keranjang(new ArrayObject(['kopi']));
$k2 = clone $k1;
$k2->isi->append('teh');

echo 'k1 : ' . implode(', ', $k1->isi->getArrayCopy()) . "\\n";
echo 'k2 : ' . implode(', ', $k2->isi->getArrayCopy()) . "\\n";"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  kelas $a : Produk",
                    "  kelas $c : Pesanan",
                    "    Pesanan: 1",
                    "    Produk: 2",
                    "  ---",
                    "  k1 : kopi",
                    "  k2 : kopi, teh",
                    "",
                    "new static($id) di class induk menghasilkan Produk waktu dipanggil",
                    "lewat Produk::buat(), dan Pesanan waktu dipanggil lewat",
                    "Pesanan::buat(). Kalau ditulis new self(), keduanya bakal mencoba",
                    "membuat Model. Model itu abstract, jadi programnya langsung gagal.",
                    "",
                    "static::class memberi nama class yang dipakai waktu memanggil, yang",
                    "baru ketahuan saat program jalan. $objek::class (PHP 8) melakukan hal",
                    "yang sama dari sisi objeknya, dan menggantikan get_class($objek).",
                    "",
                    "Bagian keranjang menunjukkan gunanya __clone. Coba lihat baris ini:",
                    "",
                    "  $this->isi = clone $this->isi;",
                    "",
                    "Tanpa baris itu, menambah teh ke k2 ikut menambahkannya ke k1, karena",
                    "clone bawaan cuma menyalin referensi ke ArrayObject yang sama.",
                    "",
                    "Ingat: array di PHP disalin waktu ditugaskan ke variabel lain, objek",
                    "nggak. Jadi cuma property yang berupa objek yang perlu diurus di",
                    "__clone.",
                    "",
                    "Anggota statis berguna untuk method pabrik, penghitung, dan konstanta.",
                    "Yang harus dihindari: memakainya untuk menyimpan keadaan aplikasi.",
                    "Keadaan statis nggak otomatis kembali ke awal di antara tes, susah",
                    "diganti dengan versi palsu waktu pengujian, dan membuat dua bagian",
                    "program saling memengaruhi lewat jalan yang nggak kelihatan.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Di Laravel, kamu menulis Produk::create($data) dan dapat objek Produk,",
                    "padahal method create nggak ditulis di class Produk. Eloquent, bagian",
                    "Laravel yang mengurus database, menangkap panggilan statis itu dengan",
                    "__callStatic, lalu membuat objeknya dengan new static. Magic method",
                    "lain, __clone, berguna waktu kamu menyalin objek yang memuat objek",
                    "lain, misalnya pesanan lama yang mau dipesan ulang.",
                    "",
                    "Kasus kecil: aplikasi warung punya tombol Pesan Lagi. Pesanan lama",
                    "berisi Nasi Goreng, disimpan di property $isi berupa ArrayObject.",
                    "Pembeli menyalin pesanan itu, lalu menambah Es Teh di salinannya.",
                    "Riwayat pesanan lama harus tetap berisi Nasi Goreng saja.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pahami apa yang disalin clone. Property yang berupa objek cuma",
                    "     disalin rujukannya, jadi pesanan lama dan baru memegang ArrayObject",
                    "     yang sama.",
                    "  2. Tambahkan __clone di class Pesanan, lalu salin juga objek di",
                    "     dalamnya:",
                    "      public function __clone(): void",
                    "      {",
                    "          $this->isi = clone $this->isi;",
                    "      }",
                    "  3. Coba alurnya: $baru = clone $lama, lalu tambahkan Es Teh lewat",
                    "     $baru->isi->append('Es Teh'). Isi $lama tetap Nasi Goreng, dan isi",
                    "     $baru jadi Nasi Goreng dan Es Teh.",
                    "  4. Periksa property lainnya. Angka, teks, dan array berisi nilai biasa",
                    "     sudah terpisah sesudah clone, jadi yang perlu ditulis di __clone",
                    "     cuma property berupa objek.",
                ]
            },
        ],
    },
    {
        "title": "21. Pengujian dengan PHPUnit",
        "sections": [
            {
                "body": [
                    "PHPUnit adalah kerangka tes standar di dunia PHP. Tes di sini artinya",
                    "kode yang ngecek apakah kode lain bekerja sesuai harapan.",
                    "",
                    "  composer require --dev phpunit/phpunit",
                    "  ./vendor/bin/phpunit",
                    "",
                    "Perintah pertama memasang PHPUnit lewat Composer, khusus untuk",
                    "pengembangan. Perintah kedua menjalankan semua tes.",
                    "",
                    "Bentuk sebuah tes:",
                    "",
                    "  use PHPUnit\\Framework\\TestCase;",
                    "",
                    "  final class KalkulatorTest extends TestCase",
                    "  {",
                    "      public function testTambahDuaPositif(): void",
                    "      {",
                    "          // Arrange",
                    "          $k = new Kalkulator();",
                    "",
                    "          // Act",
                    "          $hasil = $k->tambah(2, 3);",
                    "",
                    "          // Assert",
                    "          $this->assertSame(5, $hasil);",
                    "      }",
                    "  }",
                    "",
                    "Arrange, Act, Assert di komentar itu artinya: siapkan bahannya,",
                    "jalankan yang mau diuji, lalu periksa hasilnya.",
                    "",
                    "Nama method tes harus diawali test, atau diberi atribut #[Test], yaitu",
                    "penanda khusus yang ditulis di atas method. Nama class-nya diakhiri",
                    "Test.",
                    "",
                    "Assertion adalah pernyataan \"hasilnya harus begini\". Yang paling sering",
                    "dipakai:",
                    "  assertSame($harap, $aktual)      === , periksa tipe juga",
                    "  assertEquals($harap, $aktual)    == , longgar",
                    "  assertTrue / assertFalse",
                    "  assertNull / assertNotNull",
                    "  assertCount(3, $array)",
                    "  assertContains($x, $array)",
                    "  assertArrayHasKey('k', $array)",
                    "  assertInstanceOf(Kelas::class, $o)",
                    "  assertStringContainsString('abc', $s)",
                    "  expectException(InvalidArgumentException::class)",
                    "",
                    "Aturan: pakai assertSame, jangan assertEquals. assertEquals memakai",
                    "perbandingan longgar, jadi '5' dianggap sama dengan 5. Akibatnya tesmu",
                    "berhenti menangkap bug tipe, padahal bug jenis itu yang paling sering",
                    "terjadi di PHP.",
                    "",
                    "Data provider menjalankan tes yang sama dengan banyak data:",
                    "",
                    "  public static function dataGrade(): array",
                    "  {",
                    "      return [",
                    "          'batas bawah A' => [85, 'A'],",
                    "          'batas atas B'  => [84, 'B'],",
                    "      ];",
                    "  }",
                    "",
                    "  #[DataProvider('dataGrade')]",
                    "  public function testGrade(int $nilai, string $harap): void",
                    "",
                    "Kunci array jadi nama kasusnya, dan nama itu yang muncul waktu sebuah",
                    "kasus gagal. Itu jauh lebih berguna daripada pesan 'with data set #3'.",
                ]
            },
            {
                "heading": "Kelas beserta tesnya",
                "code": """<?php
// ==== File: src/Rapor.php ====
declare(strict_types=1);

final class Rapor
{
    /** @var array<string, int> */
    private array $nilai = [];

    public function catat(string $nama, int $nilai): void
    {
        if ($nilai < 0 || $nilai > 100) {
            throw new InvalidArgumentException("nilai $nilai di luar 0..100");
        }
        $this->nilai[$nama] = $nilai;
    }

    public static function grade(int $nilai): string
    {
        return match (true) {
            $nilai >= 85 => 'A',
            $nilai >= 75 => 'B',
            $nilai >= 60 => 'C',
            default => 'D',
        };
    }

    public function rataRata(): ?float
    {
        if ($this->nilai === []) {
            return null;
        }
        return array_sum($this->nilai) / count($this->nilai);
    }

    /** @return string[] */
    public function lulus(): array
    {
        $hasil = array_keys(array_filter($this->nilai, fn(int $n): bool => $n >= 75));
        sort($hasil);
        return $hasil;
    }
}

// ==== File: tests/RaporTest.php ====
use PHPUnit\\Framework\\Attributes\\DataProvider;
use PHPUnit\\Framework\\TestCase;

final class RaporTest extends TestCase
{
    private Rapor $rapor;

    protected function setUp(): void
    {
        // Dijalankan SEBELUM setiap tes -- tiap tes mulai dari nol
        $this->rapor = new Rapor();
    }

    public static function dataGrade(): array
    {
        return [
            'batas bawah A' => [85, 'A'],
            'batas atas B'  => [84, 'B'],
            'batas bawah B' => [75, 'B'],
            'batas atas C'  => [74, 'C'],
            'batas bawah C' => [60, 'C'],
            'batas atas D'  => [59, 'D'],
            'nol'           => [0, 'D'],
        ];
    }

    #[DataProvider('dataGrade')]
    public function testGradeTepatDiBatas(int $nilai, string $harap): void
    {
        $this->assertSame($harap, Rapor::grade($nilai));
    }

    public function testRataRataKosongMengembalikanNull(): void
    {
        $this->assertNull($this->rapor->rataRata());
    }

    public function testRataRataMenghitungBenar(): void
    {
        $this->rapor->catat('Andi', 80);
        $this->rapor->catat('Budi', 90);
        $this->assertSame(85.0, $this->rapor->rataRata());
    }

    public function testLulusTerurutDanHanyaYangLulus(): void
    {
        $this->rapor->catat('Cici', 95);
        $this->rapor->catat('Budi', 64);
        $this->rapor->catat('Andi', 75);
        $this->assertSame(['Andi', 'Cici'], $this->rapor->lulus());
    }

    public function testNilaiDiLuarRentangDitolak(): void
    {
        $this->expectException(InvalidArgumentException::class);
        $this->expectExceptionMessage('di luar 0..100');
        $this->rapor->catat('Andi', 150);
    }
}"""
            },
            {
                "body": [
                    "Lihat nilai-nilai yang dipilih di data provider: 85 dan 84, 75 dan 74,",
                    "60 dan 59. Menguji tepat di batas paling berharga, karena di situlah",
                    "salah ketik >= jadi > ketahuan. Nilai di tengah rentang hampir nggak",
                    "pernah menemukan bug.",
                    "",
                    "setUp() dijalankan sebelum setiap method tes, jadi tiap tes mulai dari",
                    "keadaan yang persis sama. Tes yang hasilnya bergantung pada urutan",
                    "dijalankannya suatu hari bakal gagal, padahal nggak ada yang mengubah",
                    "apa pun.",
                    "",
                    "assertSame(85.0, ...) sengaja ditulis dengan titik nol.",
                    "assertSame(85, ...) bakal gagal, karena 85 itu int sedangkan hasilnya",
                    "float. Ketat seperti itu memang yang kita mau.",
                    "",
                    "Berkas konfigurasi phpunit.xml di akar proyek:",
                    "",
                    "  <phpunit bootstrap=\"vendor/autoload.php\"",
                    "           colors=\"true\">",
                    "      <testsuites>",
                    "          <testsuite name=\"semua\">",
                    "              <directory>tests</directory>",
                    "          </testsuite>",
                    "      </testsuites>",
                    "  </phpunit>",
                    "",
                    "Perintah yang sering dipakai:",
                    "  vendor/bin/phpunit",
                    "  vendor/bin/phpunit --filter testGrade",
                    "  vendor/bin/phpunit --testdox        keluaran terbaca",
                    "  vendor/bin/phpunit --coverage-text   butuh Xdebug/PCOV",
                    "",
                    "Opsi --filter cuma menjalankan tes yang namanya cocok, dan",
                    "--coverage-text menampilkan cakupan tes.",
                    "",
                    "Cakupan tes (coverage) adalah persentase kode yang ikut dijalankan",
                    "oleh tes. Gunanya untuk menemukan bagian yang belum diuji, jangan",
                    "dijadikan angka yang dikejar. Cakupan 100% dengan assertion yang lemah",
                    "lebih buruk daripada cakupan 70% yang memeriksa perilakunya dengan",
                    "teliti.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Banyak tim menjalankan tes otomatis setiap kali kodenya diubah, supaya",
                    "perbaikan di satu tempat nggak merusak tempat lain. Tes juga jadi cara",
                    "yang rapi untuk menangani laporan bug: tulis dulu tes yang mengulang",
                    "bug-nya, baru perbaiki kodenya.",
                    "",
                    "Kasus kecil: promo toko berbunyi \"gratis ongkir untuk belanja minimal",
                    "Rp100.000\". Pelanggan yang belanja pas Rp100.000 melapor tetap ditagih",
                    "ongkir Rp10.000. Ternyata fungsi Ongkir::hitung() memakai > 100000.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Ulang bug-nya dalam bentuk tes sebelum mengubah apa pun. Kasus yang",
                    "     dilaporkan, belanja 100000, harus menghasilkan ongkir 0.",
                    "  2. Tambahkan angka di sekitar batas ke data provider: 99999 kena",
                    "     10000, sedangkan 100000 dan 100001 gratis. Beri nama kasus seperti",
                    "     'tepat batas' supaya laporan gagalnya jelas.",
                    "  3. Tulis tesnya dengan assertSame:",
                    "      #[DataProvider('dataOngkir')]",
                    "      public function testOngkirDiBatas(int $belanja, int $harap): void",
                    "      {",
                    "          $this->assertSame($harap, Ongkir::hitung($belanja));",
                    "      }",
                    "  4. Jalankan dan pastikan kasus tepat batas gagal dulu. Sesudah >",
                    "     diganti >=, semua kasus harus lulus. Tes yang sudah lulus sebelum",
                    "     perbaikan berarti belum mengulang bug-nya.",
                    "",
                    "Ingat: tes ini tetap tinggal di proyek. Kalau suatu hari ada yang",
                    "mengubah >= jadi > lagi, kasus tepat batas langsung gagal.",
                ]
            },
        ],
    },
]
