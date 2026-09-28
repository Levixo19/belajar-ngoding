PHP_MATERIALS = [
    {
        "title": "1. Pengenalan PHP & Instalasi",
        "sections": [
            {
                "body": [
                    "Apa itu PHP?",
                    "  - Dibuat Rasmus Lerdorf tahun 1994, awalnya sekumpulan",
                    "    skrip untuk menghitung pengunjung halaman pribadi.",
                    "  - Namanya rekursif: PHP: Hypertext Preprocessor.",
                    "  - Interpreted: dijalankan baris demi baris, tanpa",
                    "    langkah kompilasi terpisah.",
                    "  - Dynamically typed, tapi sejak PHP 7 bisa (dan",
                    "    sebaiknya) diberi tipe eksplisit.",
                    "",
                    "PHP dirancang untuk SATU pekerjaan: menghasilkan halaman",
                    "web. Itu sebabnya ia punya hal yang tidak dimiliki bahasa",
                    "lain — kode PHP bisa disisipkan langsung di tengah HTML.",
                    "",
                    "Kenapa masih sangat relevan hari ini:",
                    "  - Sekitar tiga perempat situs web di dunia memakainya.",
                    "  - WordPress, Laravel, Symfony, Drupal, Magento.",
                    "  - Hosting termurah pun menyediakannya.",
                    "  - PHP 8 jauh lebih cepat dan jauh lebih ketat daripada",
                    "    PHP 5 yang jadi sumber reputasi buruknya.",
                    "",
                    "PERINGATAN PENTING soal tutorial lama: PHP 5 dan PHP 8",
                    "adalah dua bahasa yang sangat berbeda. Kalau sebuah",
                    "tutorial memakai mysql_query(), ereg(), atau",
                    "magic_quotes, itu ditulis lebih dari sepuluh tahun lalu",
                    "dan sebagian kodenya SUDAH DIHAPUS dari PHP. Materi ini",
                    "memakai PHP 8.",
                    "",
                    "Instalasi:",
                    "  - Fedora  : sudo dnf install php-cli",
                    "  - Debian  : sudo apt install php-cli",
                    "  - macOS   : brew install php",
                    "  - Windows : unduh dari https://windows.php.net",
                    "  - Cek     : php --version",
                    "",
                    "Menjalankan:",
                    "  php berkas.php            jalankan skrip",
                    "  php -a                    mode interaktif",
                    "  php -l berkas.php         periksa sintaks saja",
                    "  php -S localhost:8000     server web bawaan",
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
                    "Penjelasan tiap bagian:",
                    "",
                    "  <?php",
                    "    Tag pembuka. SEMUA yang di luar tag ini dikirim apa",
                    "    adanya sebagai teks; yang di dalamnya dijalankan.",
                    "",
                    "  echo",
                    "    Mencetak. Ia bukan fungsi melainkan konstruksi bahasa,",
                    "    jadi tanda kurungnya opsional dan ia bisa menerima",
                    "    beberapa argumen sekaligus: echo $a, $b, $c;",
                    "",
                    "  \\n",
                    "    Baris baru. Ia HANYA berlaku di dalam kutip GANDA.",
                    "    Di kutip tunggal, \\n tercetak apa adanya sebagai dua",
                    "    karakter.",
                    "",
                    "  Titik koma",
                    "    Wajib mengakhiri setiap pernyataan.",
                    "",
                    "ATURAN yang perlu ditanam sejak sekarang: di berkas yang",
                    "isinya HANYA PHP, tag penutup ?> sengaja TIDAK ditulis.",
                    "Alasannya bukan selera: spasi atau baris kosong sesudah",
                    "?> ikut terkirim ke browser, dan itu merusak header HTTP",
                    "serta unduhan berkas. Standar PSR-12 melarangnya.",
                    "",
                    "Menyisipkan PHP di HTML:",
                    "",
                    "  <h1><?= $judul ?></h1>",
                    "",
                    "`<?=` adalah singkatan dari `<?php echo`. Bentuk ini",
                    "satu-satunya tempat di mana tag penutup memang dipakai.",
                    "",
                    "Komentar:",
                    "  // satu baris",
                    "  # satu baris juga, lebih jarang dipakai",
                    "  /* beberapa",
                    "     baris */",
                ]
            },
        ],
    },
    {
        "title": "2. Variabel & Tipe Data",
        "sections": [
            {
                "body": [
                    "Setiap variabel PHP diawali tanda dolar:",
                    "",
                    "  $nama = \"Andi\";",
                    "  $umur = 20;",
                    "  $tinggi = 172.5;",
                    "  $aktif = true;",
                    "",
                    "Tidak perlu menulis tipenya — PHP menyimpulkannya dari",
                    "nilai. Nama variabel MEMBEDAKAN huruf besar-kecil:",
                    "$nama dan $Nama adalah dua variabel berbeda. (Nama fungsi",
                    "dan kata kunci justru TIDAK membedakan, warisan lama yang",
                    "sebaiknya tidak kamu manfaatkan.)",
                    "",
                    "Delapan tipe data PHP:",
                    "",
                    "  SKALAR",
                    "    int      bilangan bulat",
                    "    float    pecahan (disebut juga double)",
                    "    string   teks",
                    "    bool     true / false",
                    "",
                    "  MAJEMUK",
                    "    array    daftar ATAU kamus, keduanya sekaligus",
                    "    object   instance dari sebuah class",
                    "",
                    "  KHUSUS",
                    "    null     tidak ada nilai",
                    "    resource pegangan ke sumber luar (berkas, koneksi)",
                    "",
                    "Memeriksa tipe:",
                    "  gettype($x)          nama tipenya sebagai teks",
                    "  var_dump($x)         tipe DAN nilainya, untuk debugging",
                    "  is_int($x)  is_float($x)  is_string($x)",
                    "  is_bool($x) is_array($x)  is_null($x)",
                    "",
                    "var_dump adalah alat debugging paling berguna di PHP.",
                    "Ia mencetak tipe, panjang, dan isi — termasuk untuk",
                    "array bersarang. Jangan pakai echo untuk memeriksa",
                    "sesuatu yang bukan teks: echo pada array cuma mencetak",
                    "kata \"Array\" beserta sebuah peringatan.",
                    "",
                    "Konstanta:",
                    "  const PAJAK = 0.11;           di level berkas atau class",
                    "  define('SITUS', 'belajar');   bentuk lama, masih sah",
                    "",
                    "Konstanta TIDAK memakai tanda dolar, dan namanya menurut",
                    "kebiasaan ditulis huruf besar semua.",
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
                    "Dua baris terakhir adalah jebakan klasik PHP yang wajib",
                    "kamu hafal:",
                    "",
                    "  (bool) \"0\"       -> FALSE",
                    "  (bool) \"false\"   -> TRUE",
                    "",
                    "Nilai yang dianggap FALSE di PHP, dan cuma ini:",
                    "  false, 0, 0.0, \"\", \"0\", [], null",
                    "",
                    "Segala sesuatu yang lain — termasuk string \"false\",",
                    "string \"0.0\", angka -1, dan array berisi satu elemen",
                    "kosong — dianggap TRUE.",
                    "",
                    "Perhatikan juga gettype() memberi \"double\" untuk float",
                    "dan \"integer\" untuk int. Nama lama yang tidak pernah",
                    "diubah demi kompatibilitas; itu sebabnya `is_float()`",
                    "lebih baik daripada membandingkan string gettype.",
                    "",
                    "`(int) \"42 apel\"` menghasilkan 42 tanpa keluhan sama",
                    "sekali. Perilaku ini memudahkan sekaligus berbahaya:",
                    "masukan pengguna yang setengah rusak lolos diam-diam.",
                    "Untuk validasi yang sesungguhnya pakai filter_var:",
                    "",
                    "  $n = filter_var($masukan, FILTER_VALIDATE_INT);",
                    "  if ($n === false) { ... tidak sah ... }",
                ]
            },
        ],
    },
    {
        "title": "3. String & Interpolasi",
        "sections": [
            {
                "body": [
                    "Empat cara menulis string di PHP:",
                    "",
                    "  KUTIP TUNGGAL — apa adanya, paling cepat",
                    "    'Halo $nama'        -> Halo $nama   (tidak diganti!)",
                    "    Hanya \\' dan \\\\ yang punya arti khusus.",
                    "",
                    "  KUTIP GANDA — variabel dan escape aktif",
                    "    \"Halo $nama\"        -> Halo Andi",
                    "    \"Total: {$a[0]}\"    kurung kurawal untuk yang rumit",
                    "    \\n \\t \\\" \\\\ \\$ berlaku",
                    "",
                    "  HEREDOC — kutip ganda multi-baris",
                    "    $teks = <<<EOT",
                    "    Halo $nama,",
                    "    ini beberapa baris.",
                    "    EOT;",
                    "",
                    "  NOWDOC — kutip tunggal multi-baris",
                    "    $teks = <<<'EOT'",
                    "    $nama tidak diganti di sini.",
                    "    EOT;",
                    "",
                    "Penanda penutup heredoc/nowdoc menentukan INDENTASI yang",
                    "dipotong dari tiap baris — fitur yang baru ada sejak",
                    "PHP 7.3 dan membuat heredoc akhirnya enak dipakai di",
                    "dalam method yang menjorok.",
                    "",
                    "MENYAMBUNG string memakai TITIK, bukan plus:",
                    "  $a = \"Halo\" . \" \" . \"dunia\";",
                    "  $a .= \"!\";",
                    "",
                    "Ini sumber kesalahan bagi yang datang dari JavaScript.",
                    "Di PHP, `\"1\" + \"2\"` menghasilkan ANGKA 3, bukan \"12\".",
                    "",
                    "Fungsi string yang paling sering dipakai:",
                    "  strlen($s)                  panjang dalam BYTE",
                    "  mb_strlen($s)               panjang dalam KARAKTER",
                    "  strtoupper / strtolower",
                    "  ucfirst / ucwords           huruf besar di awal",
                    "  trim / ltrim / rtrim",
                    "  substr($s, 2, 4)",
                    "  strpos($s, \"cari\")          posisi, atau FALSE",
                    "  str_contains($s, \"cari\")    bool, sejak PHP 8",
                    "  str_starts_with / str_ends_with",
                    "  str_replace(\"a\", \"b\", $s)",
                    "  explode(\",\", $s)            teks -> array",
                    "  implode(\", \", $arr)         array -> teks",
                    "  str_repeat(\"-\", 20)",
                    "  str_pad($s, 10, \" \")",
                    "  sprintf / printf / number_format",
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
                    "`{$nama}nya` menunjukkan kenapa kurung kurawal perlu:",
                    "tanpa itu PHP akan mencari variabel bernama $namanya",
                    "yang tidak ada.",
                    "",
                    "`foreach ($barang as [$a, $b, $c])` adalah DESTRUCTURING",
                    "array — memecah tiap baris jadi tiga variabel sekaligus.",
                    "Sintaks kurung siku ini tersedia sejak PHP 7.1.",
                    "",
                    "`number_format($n, 0, ',', '.')` memakai titik sebagai",
                    "pemisah ribuan dan koma untuk desimal — format Indonesia.",
                    "Bawaannya format Inggris (koma untuk ribuan).",
                    "",
                    "PERINGATAN: `strpos()` mengembalikan 0 kalau ketemu di",
                    "posisi paling awal, dan FALSE kalau tidak ketemu. Karena",
                    "0 == false di PHP, memeriksanya dengan `if (!strpos(...))`",
                    "SALAH. Yang benar `if (strpos(...) === false)`, atau",
                    "cukup pakai `str_contains()` yang ada sejak PHP 8.",
                ]
            },
        ],
    },
    {
        "title": "4. Operator & Perbandingan",
        "sections": [
            {
                "body": [
                    "Aritmetika:",
                    "  +  -  *  /  %  **",
                    "",
                    "  ** adalah pangkat: 2 ** 10 = 1024",
                    "  /  SELALU menghasilkan float kalau tidak habis dibagi:",
                    "     7 / 2 = 3.5, bukan 3. Berbeda dari C, Java, dan Go.",
                    "  Untuk pembagian bulat: intdiv(7, 2) = 3",
                    "",
                    "Penugasan: = += -= *= /= %= **= .=",
                    "Naik/turun: ++ --",
                    "",
                    "PERBANDINGAN — bagian terpenting di materi ini:",
                    "",
                    "  ==   sama nilainya SETELAH konversi tipe",
                    "  ===  sama nilainya DAN sama tipenya",
                    "  !=   tidak sama nilainya",
                    "  !==  tidak sama nilai atau tipenya",
                    "  <  >  <=  >=",
                    "  <=>  spaceship: -1, 0, atau 1",
                    "",
                    "ATURAN PRAKTIS YANG MENGHEMAT BERJAM-JAM: pakai === dan",
                    "!== secara bawaan. Pakai == hanya kalau kamu benar-benar",
                    "MAU konversi tipenya terjadi, dan tahu persis aturannya.",
                    "",
                    "PHP 8 memperbaiki perbandingan angka dengan string, dan",
                    "ini perubahan besar:",
                    "",
                    "              PHP 7     PHP 8",
                    "  0 == \"foo\"   true      false   <- diperbaiki",
                    "  \"1\" == \"01\"  true      true",
                    "  100 == \"1e2\" true      true",
                    "  0 == \"\"      true      false   <- diperbaiki",
                    "",
                    "Baris pertama pernah jadi celah keamanan nyata: kode",
                    "`if ($password == 0)` lolos untuk password apa pun yang",
                    "bukan angka.",
                    "",
                    "Logika:",
                    "  &&  ||  !     dan bentuk kata: and  or  xor",
                    "",
                    "JANGAN campur keduanya. `and` dan `or` punya prioritas",
                    "LEBIH RENDAH daripada `=`, sehingga:",
                    "  $x = true and false;   -> $x bernilai TRUE",
                    "  $x = true && false;    -> $x bernilai FALSE",
                    "",
                    "Operator khas PHP:",
                    "  ?:    Elvis: $a ?: 'bawaan'   pakai $a kalau truthy",
                    "  ??    null coalescing: $a ?? 'bawaan'",
                    "  ??=   isi hanya kalau null",
                    "  ?->   panggil hanya kalau bukan null (PHP 8)",
                    "",
                    "Beda ?: dan ?? penting: `?:` memicu peringatan kalau",
                    "variabelnya belum ada, sedangkan `??` tidak. Untuk",
                    "membaca $_GET atau array yang mungkin tidak punya kunci,",
                    "`??` yang benar.",
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
                    "Perhatikan `$data['kota']` ADA di array tapi bernilai",
                    "null, dan `??` tetap memberi nilai bawaan. Itu memang",
                    "artinya: `??` memeriksa 'null atau tidak ada', bukan",
                    "'ada atau tidak ada'. Kalau kamu perlu membedakannya,",
                    "pakai `array_key_exists()`.",
                    "",
                    "Operator spaceship `<=>` dipakai untuk fungsi pembanding",
                    "di usort — ia menggantikan tiga baris if:",
                    "",
                    "  usort($data, fn($a, $b) => $a['nilai'] <=> $b['nilai']);",
                ]
            },
        ],
    },
    {
        "title": "5. Percabangan & Perulangan",
        "sections": [
            {
                "body": [
                    "Percabangan:",
                    "",
                    "  if ($nilai >= 75) {",
                    "      echo \"Lulus\";",
                    "  } elseif ($nilai >= 60) {",
                    "      echo \"Mengulang\";",
                    "  } else {",
                    "      echo \"Tidak Lulus\";",
                    "  }",
                    "",
                    "Perhatikan `elseif` satu kata. `else if` dua kata juga",
                    "sah di PHP, tapi TIDAK di dalam sintaks alternatif",
                    "(elseif: ... endif). Pakai satu kata saja, konsisten.",
                    "",
                    "SINTAKS ALTERNATIF untuk template HTML:",
                    "",
                    "  <?php if ($login): ?>",
                    "      <p>Halo, <?= $nama ?></p>",
                    "  <?php else: ?>",
                    "      <a href=\"/masuk\">Masuk</a>",
                    "  <?php endif; ?>",
                    "",
                    "Di dalam HTML, bentuk ini jauh lebih terbaca daripada",
                    "kurung kurawal yang berserakan antar tag.",
                    "",
                    "switch, dan break-nya WAJIB:",
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
                    "switch memakai perbandingan LONGGAR (==). Ini jebakan:",
                    "`switch(0)` akan cocok dengan `case \"apa pun\"` di PHP 7.",
                    "Di PHP 8 sudah diperbaiki, tapi kebiasaan memakai `match`",
                    "lebih aman.",
                    "",
                    "MATCH (PHP 8) — lebih baik dalam segala hal:",
                    "",
                    "  $grade = match(true) {",
                    "      $nilai >= 85 => 'A',",
                    "      $nilai >= 75 => 'B',",
                    "      default => 'C',",
                    "  };",
                    "",
                    "Bedanya dari switch:",
                    "  1. Ia EKSPRESI, menghasilkan nilai.",
                    "  2. Perbandingannya KETAT (===).",
                    "  3. Tidak ada fall-through, tidak perlu break.",
                    "  4. Melempar UnhandledMatchError kalau tidak ada yang",
                    "     cocok dan tidak ada default — kegagalan yang",
                    "     KELIHATAN, bukan diam.",
                    "",
                    "Perulangan:",
                    "  for ($i = 0; $i < 5; $i++) { ... }",
                    "  while ($n > 0) { ... }",
                    "  do { ... } while ($n > 0);",
                    "  foreach ($arr as $nilai) { ... }",
                    "  foreach ($arr as $kunci => $nilai) { ... }",
                    "",
                    "`break n` dan `continue n` keluar dari n tingkat",
                    "perulangan sekaligus — fitur yang tidak ada di C# atau",
                    "Java.",
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
                    "`match(true)` adalah idiom untuk rantai kondisi: tiap",
                    "lengan dibandingkan dengan `true`, jadi lengan pertama",
                    "yang kondisinya benar yang dipakai.",
                    "",
                    "`'POST', 'PUT' => ...` menangani beberapa nilai dalam",
                    "satu lengan — padanan case yang ditumpuk di switch, tapi",
                    "tanpa risiko fall-through yang tidak disengaja.",
                    "",
                    "PERINGATAN foreach yang paling mahal di PHP:",
                    "",
                    "  foreach ($arr as &$x) { $x *= 2; }",
                    "  foreach ($arr as $x) { ... }        <- BUG",
                    "",
                    "Setelah perulangan pertama, $x masih berupa REFERENSI ke",
                    "elemen terakhir. Perulangan kedua menimpanya berulang",
                    "kali, dan elemen terakhir array berakhir dengan nilai",
                    "elemen kedua-dari-belakang. Bug ini sangat terkenal dan",
                    "sangat sulit dilihat.",
                    "",
                    "Pencegahnya satu baris: `unset($x);` sesudah setiap",
                    "foreach yang memakai referensi.",
                ]
            },
        ],
    },
    {
        "title": "6. Array: Daftar dan Kamus Sekaligus",
        "sections": [
            {
                "body": [
                    "Array PHP berbeda dari hampir semua bahasa lain: ia",
                    "SATU tipe yang berperan sebagai daftar berindeks DAN",
                    "kamus berkunci sekaligus. Di baliknya ia selalu peta",
                    "terurut.",
                    "",
                    "  $daftar = [10, 20, 30];",
                    "  $kamus = ['nama' => 'Andi', 'umur' => 20];",
                    "  $campur = [0 => 'a', 'x' => 'b', 5 => 'c'];",
                    "",
                    "Kunci boleh int atau string. Kunci string berupa angka",
                    "(\"5\") otomatis jadi int. true jadi 1, false jadi 0,",
                    "null jadi \"\".",
                    "",
                    "Menambah dan mengubah:",
                    "  $a[] = 'baru';            tambah di akhir",
                    "  $a['kunci'] = 'nilai';",
                    "  array_push($a, 'x', 'y');",
                    "  unset($a[2]);             hapus SATU elemen",
                    "",
                    "PERINGATAN: `unset` TIDAK menomori ulang. Setelah",
                    "menghapus index 1 dari [0,1,2], yang tersisa index 0",
                    "dan 2 — dan `json_encode` akan menghasilkan OBJEK, bukan",
                    "array. Pakai `array_values($a)` untuk menomori ulang.",
                    "",
                    "Fungsi array yang paling sering dipakai:",
                    "  count($a)                     jumlah elemen",
                    "  in_array($x, $a)              apakah NILAI ada",
                    "  array_search($x, $a)          kunci dari nilai, atau false",
                    "  array_key_exists($k, $a)      apakah KUNCI ada",
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
                    "Fungsi tingkat tinggi:",
                    "  array_map(fn($x) => $x * 2, $a)",
                    "  array_filter($a, fn($x) => $x > 5)",
                    "  array_reduce($a, fn($c, $x) => $c + $x, 0)",
                    "",
                    "JEBAKAN array_filter: ia MEMPERTAHANKAN kunci aslinya.",
                    "Hasil penyaringan [0=>1, 2=>3] bukan array berurutan",
                    "lagi. Bungkus dengan array_values kalau urutannya",
                    "penting.",
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
                    "Keluarga fungsi pengurutan PHP, dan namanya sistematis",
                    "begitu kamu tahu polanya:",
                    "",
                    "  sort     urut NILAI naik, kunci dibuang",
                    "  rsort    urut NILAI turun, kunci dibuang",
                    "  asort    urut NILAI naik, KUNCI dipertahankan",
                    "  arsort   urut NILAI turun, kunci dipertahankan",
                    "  ksort    urut KUNCI naik",
                    "  krsort   urut KUNCI turun",
                    "  usort    urut dengan fungsi sendiri, kunci dibuang",
                    "  uasort   sama, kunci dipertahankan",
                    "  uksort   urut kunci dengan fungsi sendiri",
                    "",
                    "Huruf awalannya: a = associative (kunci dijaga),",
                    "k = key, r = reverse, u = user-defined.",
                    "",
                    "SEMUANYA mengubah array ASLINYA dan mengembalikan bool,",
                    "bukan array baru. `$b = sort($a);` adalah kesalahan yang",
                    "sangat sering: $b akan berisi `true`.",
                ]
            },
        ],
    },
    {
        "title": "7. Fungsi & Tipe",
        "sections": [
            {
                "body": [
                    "Fungsi dasar:",
                    "",
                    "  function tambah($a, $b) {",
                    "      return $a + $b;",
                    "  }",
                    "",
                    "Dengan TIPE — dan ini yang membedakan PHP modern dari",
                    "PHP lama:",
                    "",
                    "  function tambah(int $a, int $b): int {",
                    "      return $a + $b;",
                    "  }",
                    "",
                    "Tipe yang bisa ditulis: int, float, string, bool, array,",
                    "callable, iterable, object, mixed, void, never, self,",
                    "static, dan nama class apa pun.",
                    "",
                    "  ?int          int atau null",
                    "  int|string    salah satu (union, PHP 8)",
                    "  Countable&Iterator  keduanya (intersection, PHP 8.1)",
                    "",
                    "MODE KETAT — satu baris yang mengubah segalanya:",
                    "",
                    "  declare(strict_types=1);",
                    "",
                    "Tanpa itu, `tambah(\"5\", \"3\")` diterima dan PHP",
                    "mengonversinya diam-diam jadi 8. Dengan itu, ia melempar",
                    "TypeError. Baris ini WAJIB ada di baris pertama setiap",
                    "berkas PHP baru, dan ia berlaku per-berkas.",
                    "",
                    "Parameter bawaan dan variadic:",
                    "  function sapa(string $nama, string $salam = 'Halo')",
                    "  function total(int ...$angka)      terima berapa pun",
                    "",
                    "Argumen bernama (PHP 8):",
                    "  sapa(salam: 'Hai', nama: 'Andi');",
                    "",
                    "Ini bukan kosmetik. `buat(true, false, true)` tidak",
                    "memberi tahu apa pun; `buat(tebal: true, miring: false,",
                    "garisBawah: true)` menjelaskan dirinya sendiri.",
                    "",
                    "CLOSURE dan arrow function:",
                    "  $kali = function ($x) use ($faktor) { return $x * $faktor; };",
                    "  $kali = fn($x) => $x * $faktor;",
                    "",
                    "Bedanya penting: `function` butuh `use` untuk mengambil",
                    "variabel dari luar, sedangkan `fn` menangkapnya OTOMATIS",
                    "(selalu berdasarkan nilai, bukan referensi). Arrow",
                    "function hanya boleh satu ekspresi.",
                    "",
                    "Lingkup variabel di PHP KETAT: fungsi TIDAK bisa melihat",
                    "variabel di luarnya sama sekali, bahkan yang global,",
                    "kecuali lewat `use`, parameter, atau kata kunci `global`.",
                    "Ini berbeda dari JavaScript dan Python.",
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
                    "(Baris str_pad-nya mengisi kiri-kanan hingga lebar yang",
                    "diminta; jumlah pengisi kiri dan kanan bisa beda satu",
                    "kalau selisihnya ganjil.)",
                    "",
                    "Perhatikan `fn($x) => $x * $faktor` menangkap $faktor",
                    "tanpa `use`. Dengan `function` biasa kamu harus menulis",
                    "`function ($x) use ($faktor) { ... }`, dan melupakannya",
                    "menghasilkan peringatan 'undefined variable' — bukan",
                    "error, sekadar peringatan, sehingga hasilnya nol tanpa",
                    "ada yang menyadari.",
                    "",
                    "`?float` sebagai tipe kembalian berarti 'float atau",
                    "null'. Tanpa tanda tanya, `return null` adalah TypeError",
                    "di mode ketat.",
                    "",
                    "`float ...$angka` menerima berapa pun argumen dan",
                    "mengumpulkannya jadi array. Untuk membongkar array jadi",
                    "argumen, pakai operator yang sama di sisi pemanggilan:",
                    "`rataRata(...$daftar);`",
                ]
            },
        ],
    },
    {
        "title": "8. Class & Objek",
        "sections": [
            {
                "body": [
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
                    "Bentuk di atas memakai CONSTRUCTOR PROPERTY PROMOTION",
                    "(PHP 8): menulis `private string $nama` di parameter",
                    "constructor sekaligus MENDEKLARASIKAN property dan",
                    "MENGISINYA. Bentuk panjangnya butuh tiga baris untuk",
                    "tiap property.",
                    "",
                    "Mengakses anggota memakai PANAH, bukan titik:",
                    "  $m->nama",
                    "  $m->hitung()",
                    "  self::KONSTANTA      anggota statis, dari dalam",
                    "  Murid::buat()        anggota statis, dari luar",
                    "",
                    "`$this` menunjuk objek yang sedang dikerjakan, dan ia",
                    "WAJIB ditulis — berbeda dari C# atau Java, `$nama` polos",
                    "di dalam method merujuk variabel lokal, bukan property.",
                    "",
                    "Modifier akses:",
                    "  public      siapa pun",
                    "  protected   class ini dan turunannya",
                    "  private     hanya class ini",
                    "",
                    "Berbeda dari C#, tidak ada nilai bawaan yang aman —",
                    "property tanpa modifier di PHP lama otomatis public.",
                    "Selalu tulis modifiernya.",
                    "",
                    "Method ajaib (magic method) yang sering dipakai:",
                    "  __construct()   dipanggil saat objek dibuat",
                    "  __destruct()    saat objek dihapus",
                    "  __toString()    saat objek dipakai sebagai string",
                    "  __get / __set   akses property yang tidak ada",
                    "  __call          panggil method yang tidak ada",
                    "  __invoke()      objeknya dipanggil seperti fungsi",
                    "",
                    "readonly (PHP 8.1) membuat property hanya bisa diisi",
                    "sekali, di dalam constructor:",
                    "",
                    "  public function __construct(",
                    "      public readonly string $kode,",
                    "  ) {}",
                    "",
                    "Ini padanan `init` di C# dan sangat berguna untuk objek",
                    "nilai yang tidak boleh berubah setelah dibuat.",
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
                    "Empat hal yang layak diperhatikan:",
                    "",
                    "  1. `public readonly string $pemilik` di parameter",
                    "     constructor: satu baris yang mendeklarasikan,",
                    "     mengisi, dan mengunci property sekaligus.",
                    "",
                    "  2. `private static int $urutan` milik CLASS, bukan",
                    "     objek. Ada satu untuk seluruh program, dan itulah",
                    "     yang membuat penomoran otomatis bekerja. Diakses",
                    "     dengan `self::$urutan`, bukan `$this->urutan`.",
                    "",
                    "  3. `$saldo` private dengan method `saldo()` untuk",
                    "     membaca. Kalau ia public, seluruh aturan di setor()",
                    "     dan tarik() bisa dilewati dengan satu baris.",
                    "",
                    "  4. `__toString()` membuat objek bisa langsung di-echo.",
                    "     Tanpa itu, `echo $a` melempar Error.",
                    "",
                    "PHP tidak punya property terhitung seperti C#. Yang",
                    "dipakai adalah method biasa — `$a->saldo()` dengan",
                    "kurung, bukan `$a->saldo`. Konvensi umumnya: getter",
                    "diberi nama sama dengan propertinya tanpa awalan `get`,",
                    "meskipun banyak kode lama memakai `getSaldo()`.",
                ]
            },
        ],
    },
    {
        "title": "9. Pewarisan, Interface & Trait",
        "sections": [
            {
                "body": [
                    "PEWARISAN — satu induk saja:",
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
                    "`parent::__construct()` memanggil constructor induk, dan",
                    "berbeda dari Java atau C#, ia TIDAK dipanggil otomatis —",
                    "kalau lupa, property induknya tidak pernah terisi dan",
                    "tidak ada peringatan apa pun.",
                    "",
                    "`final` mencegah penurunan atau penimpaan lebih lanjut.",
                    "",
                    "INTERFACE — kontrak, boleh banyak:",
                    "",
                    "  interface BisaDicetak",
                    "  {",
                    "      public function keTeks(): string;",
                    "  }",
                    "",
                    "  class Faktur implements BisaDicetak, JsonSerializable",
                    "",
                    "Anggota interface selalu public. Sejak PHP 8.1 interface",
                    "boleh punya konstanta.",
                    "",
                    "TRAIT — potongan kode yang bisa DISISIPKAN ke banyak",
                    "class. Ini jawaban PHP untuk 'butuh berbagi implementasi",
                    "tanpa pewarisan berganda':",
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
                    "Trait BUKAN tipe: kamu tidak bisa menulis",
                    "`function f(BisaDicatat $x)`. Kalau butuh tipenya juga,",
                    "pasangkan trait dengan interface — pola yang sangat",
                    "lazim di Laravel dan Symfony.",
                    "",
                    "Kalau dua trait punya method bernama sama, PHP menuntut",
                    "kamu memilih eksplisit dengan `insteadof` dan `as`.",
                    "Tidak ada pemenang diam-diam.",
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
                    "Ada tiga mekanisme berbeda di kode itu, dan masing-masing",
                    "menjawab pertanyaan yang berbeda:",
                    "",
                    "  INTERFACE Bangun   menjawab 'apa yang BISA dilakukan'.",
                    "                     Ia yang membuat foreach di bawah",
                    "                     bekerja tanpa peduli class aslinya.",
                    "  ABSTRACT CLASS     menjawab 'apa yang SAMA di semua",
                    "                     turunan'. Ia menyimpan $nama.",
                    "  TRAIT              menjawab 'perilaku yang mau kupakai",
                    "                     ulang', tanpa ikut menentukan",
                    "                     silsilah.",
                    "",
                    "Lingkaran menimpa `ringkas()` dari trait lalu memanggil",
                    "`parent::ringkas()` di dalamnya. Urutan prioritasnya di",
                    "PHP: method di class MENANG atas trait, dan trait MENANG",
                    "atas class induk.",
                    "",
                    "`private const PI` di dalam class diakses dengan",
                    "`self::PI`. Konstanta class tidak memakai tanda dolar.",
                    "",
                    "`instanceof` memeriksa apakah objek bertipe tertentu,",
                    "termasuk lewat interface dan induknya.",
                ]
            },
        ],
    },
    {
        "title": "10. Enum & Objek Nilai",
        "sections": [
            {
                "body": [
                    "Sebelum PHP 8.1, orang memakai konstanta class untuk",
                    "meniru enum:",
                    "",
                    "  class Status {",
                    "      const DRAF = 'draf';",
                    "      const TERBIT = 'terbit';",
                    "  }",
                    "",
                    "Masalahnya: `fungsi(Status::DRAF)` dan `fungsi('apa pun')`",
                    "sama-sama diterima, karena tipenya cuma string.",
                    "",
                    "ENUM SUNGGUHAN (PHP 8.1):",
                    "",
                    "  enum Status",
                    "  {",
                    "      case Draf;",
                    "      case Ditinjau;",
                    "      case Terbit;",
                    "  }",
                    "",
                    "Sekarang `function simpan(Status $s)` MENOLAK apa pun",
                    "yang bukan salah satu dari ketiganya.",
                    "",
                    "BACKED ENUM — punya nilai di baliknya, untuk disimpan ke",
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
                    "Enum BOLEH punya method, dan inilah yang membuatnya",
                    "jauh lebih berguna daripada konstanta:",
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
                    "Enum juga boleh mengimplementasi interface. Yang TIDAK",
                    "bisa: punya property (keadaan), dan diturunkan.",
                    "",
                    "Enum adalah tempat paling alami untuk aturan yang selama",
                    "ini tersebar: label tampilan, warna badge, izin akses,",
                    "transisi yang sah. Semuanya jadi method di satu berkas.",
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
                    "Keluaran (bagian tabelnya):",
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
                    "Lalu var_dump menampilkan enum(Status::Terbit) dan NULL.",
                    "",
                    "Yang membuat ini berharga: seluruh aturan alur dokumen",
                    "tinggal di SATU berkas. Sebelum enum, `berikutnya()`",
                    "biasanya berupa array raksasa di suatu tempat,",
                    "`bisaDisunting()` berupa rangkaian if di controller, dan",
                    "`label()` tersebar di berkas template. Ketiganya bisa",
                    "melenceng satu sama lain tanpa ada yang menyadarinya.",
                    "",
                    "Perhatikan juga `match($this)` TIDAK punya `default` di",
                    "`label()`. Itu disengaja: kalau nanti ada varian baru",
                    "ditambahkan, PHP melempar UnhandledMatchError dan kamu",
                    "langsung tahu ada yang terlewat. Menambahkan `default`",
                    "justru menyembunyikan kelalaian itu.",
                    "",
                    "`from()` melempar ValueError kalau nilainya tidak",
                    "dikenal; `tryFrom()` mengembalikan null. Untuk data dari",
                    "database yang kamu kendalikan, `from()` tepat — nilai",
                    "asing berarti data rusak. Untuk masukan pengguna,",
                    "`tryFrom()`.",
                ]
            },
        ],
    },
    {
        "title": "11. Exception & Penanganan Galat",
        "sections": [
            {
                "body": [
                    "PHP punya DUA jenis kegagalan, dan membedakannya penting:",
                    "",
                    "  ERROR bawaan PHP   warning, notice, deprecated. Program",
                    "                     JALAN TERUS. Ini warisan PHP lama.",
                    "  EXCEPTION          objek yang dilempar dan bisa ditangkap.",
                    "",
                    "Sejak PHP 7, hierarki keduanya disatukan di bawah",
                    "interface `Throwable`:",
                    "",
                    "  Throwable",
                    "  ├── Error              kesalahan mesin PHP",
                    "  │   ├── TypeError",
                    "  │   ├── ValueError",
                    "  │   ├── ArithmeticError -> DivisionByZeroError",
                    "  │   └── ArgumentCountError",
                    "  └── Exception          kesalahan aplikasi",
                    "      ├── RuntimeException",
                    "      │   └── OutOfBoundsException",
                    "      ├── LogicException",
                    "      │   ├── InvalidArgumentException",
                    "      │   └── DomainException",
                    "      └── JsonException, PDOException, ...",
                    "",
                    "ATURAN yang dipakai pustaka standar PHP:",
                    "  LogicException    kesalahan PROGRAMMER; seharusnya",
                    "                    ketahuan saat pengembangan.",
                    "  RuntimeException  kegagalan yang baru ketahuan saat",
                    "                    jalan: berkas hilang, jaringan putus.",
                    "",
                    "Menangkapnya:",
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
                    "Sejak PHP 8 variabelnya boleh dihilangkan kalau tidak",
                    "dipakai: `catch (ValueError) { ... }`.",
                    "",
                    "Yang bisa dibaca dari objeknya:",
                    "  $e->getMessage()   pesan",
                    "  $e->getCode()      kode",
                    "  $e->getFile()      berkas",
                    "  $e->getLine()      nomor baris",
                    "  $e->getPrevious()  exception sebelumnya, kalau dirantai",
                    "  $e->getTraceAsString()",
                    "",
                    "MERANTAI exception adalah praktik penting: saat kamu",
                    "menangkap galat tingkat rendah dan melempar galat tingkat",
                    "tinggi, sertakan yang aslinya sebagai argumen ketiga.",
                    "Tanpa itu, jejak penyebab sesungguhnya hilang.",
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
                    "`JSON_THROW_ON_ERROR` wajib kamu ingat: tanpa flag itu,",
                    "`json_decode` mengembalikan `null` untuk JSON rusak DAN",
                    "untuk JSON yang isinya memang `null`. Kedua kasus tidak",
                    "bisa dibedakan, dan bug yang lahir dari situ sangat sulit",
                    "dilacak.",
                    "",
                    "`$e->getPrevious()?->getMessage()` memakai `?->`: kalau",
                    "tidak ada exception sebelumnya, seluruh ekspresi bernilai",
                    "null alih-alih melempar galat baru.",
                    "",
                    "Aturan yang sering dilanggar:",
                    "",
                    "  JANGAN `catch (Throwable $e) {}` kosong. Itu menelan",
                    "  seluruh kesalahan termasuk TypeError dan kehabisan",
                    "  memori, dan program berjalan terus dalam keadaan rusak.",
                    "",
                    "  JANGAN memakai `@` untuk membungkam galat. Operator itu",
                    "  mematikan SEMUA pesan dari ekspresi di belakangnya,",
                    "  termasuk yang tidak kamu duga.",
                    "",
                    "  JANGAN menangkap apa yang tidak bisa kamu perbaiki.",
                    "  Membiarkannya naik ke pemanggil yang tahu konteksnya",
                    "  lebih baik daripada menanganinya setengah-setengah.",
                    "",
                    "Di produksi, `display_errors` WAJIB dimatikan dan",
                    "`log_errors` dinyalakan. Pesan galat PHP memuat jalur",
                    "berkas dan potongan kode — informasi berharga bagi",
                    "penyerang.",
                ]
            },
        ],
    },
    {
        "title": "12. Bekerja dengan Berkas & JSON",
        "sections": [
            {
                "body": [
                    "Berkas, cara singkat:",
                    "  file_get_contents($path)          seluruh isi jadi string",
                    "  file_put_contents($path, $isi)    tulis (menimpa)",
                    "  file_put_contents($path, $isi, FILE_APPEND)",
                    "  file($path)                       tiap baris jadi elemen array",
                    "  file($path, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES)",
                    "",
                    "Cara bertahap, untuk berkas besar:",
                    "  $f = fopen($path, 'r');",
                    "  while (($baris = fgets($f)) !== false) { ... }",
                    "  fclose($f);",
                    "",
                    "Mode fopen: 'r' baca, 'w' tulis (mengosongkan!), 'a'",
                    "tambah di akhir, 'x' buat baru (gagal kalau sudah ada),",
                    "'r+' baca-tulis.",
                    "",
                    "Memeriksa dan mengelola:",
                    "  file_exists / is_file / is_dir",
                    "  is_readable / is_writable",
                    "  filesize / filemtime",
                    "  unlink($path)              hapus berkas",
                    "  copy / rename",
                    "  mkdir($path, 0755, true)   true = buat induknya juga",
                    "  scandir / glob('*.txt')",
                    "",
                    "Path yang benar lintas sistem:",
                    "  __DIR__                    folder berkas ini",
                    "  __FILE__                   berkas ini",
                    "  DIRECTORY_SEPARATOR",
                    "  basename / dirname / pathinfo",
                    "  sys_get_temp_dir()",
                    "",
                    "JSON — dua fungsi, dan keduanya punya jebakan:",
                    "",
                    "  json_encode($data, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE)",
                    "  json_decode($teks, true)     true = jadi ARRAY, bukan objek",
                    "",
                    "SELALU tambahkan JSON_THROW_ON_ERROR. Tanpa itu,",
                    "kegagalan dikembalikan sebagai `false` atau `null` dan",
                    "sangat gampang lolos tanpa diperiksa.",
                    "",
                    "Flag yang sering dibutuhkan:",
                    "  JSON_PRETTY_PRINT        berbaris rapi",
                    "  JSON_UNESCAPED_UNICODE   huruf non-ASCII apa adanya",
                    "  JSON_UNESCAPED_SLASHES   jangan lolos garis miring",
                    "  JSON_THROW_ON_ERROR      lempar exception saat gagal",
                    "",
                    "CSV punya fungsi sendiri, dan pakailah — jangan",
                    "`explode(',')`. CSV sungguhan memperbolehkan koma DI",
                    "DALAM kolom asal dikutip, dan explode akan memecahnya:",
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
                    "Perhatikan `\"nilai\": \"95\"` — sebagai TEKS, bukan angka.",
                    "Semua yang keluar dari CSV adalah string, karena CSV",
                    "tidak punya tipe. Itu sebabnya perbandingannya ditulis",
                    "`(int) $b['nilai'] <=> (int) $a['nilai']`: tanpa cast,",
                    "\"100\" akan dianggap lebih kecil daripada \"95\" kalau",
                    "dibandingkan sebagai teks.",
                    "",
                    "`array_combine($judul, $baris)` menggabungkan baris judul",
                    "dengan baris data jadi array berkunci — cara paling",
                    "ringkas mengubah CSV jadi struktur yang enak dipakai.",
                    "",
                    "`array_map('intval', ...)` mengoper NAMA fungsi sebagai",
                    "string. PHP menerimanya di mana pun `callable` diminta;",
                    "bentuk lain yang sah: `[$objek, 'method']`,",
                    "`[Kelas::class, 'methodStatis']`, dan `fn($x) => ...`.",
                    "",
                    "Operasi berkas SELALU bisa gagal karena sebab di luar",
                    "kendalimu. Di kode sungguhan, periksa hasilnya:",
                    "`if ($f === false) { throw new RuntimeException(...); }`",
                ]
            },
        ],
    },
    {
        "title": "13. PHP untuk Web: Request, Form & Sesi",
        "sections": [
            {
                "body": [
                    "Di sinilah PHP berbeda dari bahasa lain: setiap",
                    "permintaan HTTP menjalankan skripmu DARI NOL, lalu",
                    "seluruh memorinya dibuang. Tidak ada keadaan yang",
                    "bertahan antar permintaan kecuali kamu menyimpannya",
                    "sendiri.",
                    "",
                    "Model 'shared nothing' ini kelemahan sekaligus kekuatan:",
                    "kebocoran memori nyaris mustahil, tapi setiap koneksi",
                    "database dibuka ulang tiap permintaan.",
                    "",
                    "Variabel superglobal — tersedia di mana saja:",
                    "  $_GET      parameter di URL",
                    "  $_POST     data dari form",
                    "  $_REQUEST  gabungan keduanya (JANGAN dipakai)",
                    "  $_SERVER   informasi permintaan dan server",
                    "  $_FILES    berkas yang diunggah",
                    "  $_COOKIE   cookie",
                    "  $_SESSION  data sesi",
                    "  $_ENV      variabel lingkungan",
                    "",
                    "$_REQUEST sebaiknya tidak dipakai karena urutan",
                    "prioritasnya bergantung setelan server, sehingga",
                    "penyerang bisa menimpa nilai POST lewat URL.",
                    "",
                    "ATURAN KEAMANAN NOMOR SATU: JANGAN PERNAH percaya",
                    "masukan pengguna. Tiga hal yang HARUS dilakukan, dan",
                    "ketiganya berbeda:",
                    "",
                    "  1. VALIDASI saat masuk",
                    "     $umur = filter_var($_POST['umur'] ?? '',",
                    "                        FILTER_VALIDATE_INT);",
                    "     if ($umur === false) { ... tolak ... }",
                    "",
                    "  2. ESCAPE saat KELUAR ke HTML",
                    "     echo htmlspecialchars($nama, ENT_QUOTES, 'UTF-8');",
                    "     Tanpa ini, nama berisi <script> akan DIJALANKAN",
                    "     browser pengunjung lain. Itu XSS.",
                    "",
                    "  3. PREPARED STATEMENT saat ke database",
                    "     Dibahas di materi berikutnya. Menyambung query",
                    "     dengan titik adalah SQL injection.",
                    "",
                    "Ketiganya tidak saling menggantikan. Validasi tidak",
                    "membuat escape jadi tidak perlu, dan sebaliknya.",
                    "",
                    "SESI:",
                    "  session_start();              WAJIB sebelum output apa pun",
                    "  $_SESSION['user_id'] = 7;",
                    "  session_regenerate_id(true);  sesudah login, cegah fiksasi",
                    "  session_destroy();",
                    "",
                    "`session_start()` harus dipanggil sebelum satu byte pun",
                    "dikirim ke browser, karena ia memasang header cookie.",
                    "Itulah alasan sesungguhnya kenapa tag `?>` di akhir",
                    "berkas berbahaya.",
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
                    "Pola di atas disebut POST-diri-sendiri: satu berkas",
                    "menampilkan form DAN memprosesnya. Untuk form sederhana",
                    "ia cukup dan mudah diikuti.",
                    "",
                    "Lima hal yang membuat kode itu benar, dan semuanya",
                    "sering dilupakan:",
                    "",
                    "  1. `?? ''` pada setiap pembacaan $_POST. Tanpa itu,",
                    "     permintaan GET pertama memicu peringatan 'undefined",
                    "     array key' untuk setiap field.",
                    "",
                    "  2. Fungsi `e()` dipakai di SETIAP titik keluaran,",
                    "     termasuk untuk nilai yang baru saja divalidasi.",
                    "     Validasi dan escape menjawab pertanyaan berbeda.",
                    "",
                    "  3. Nilai form diisi ulang dari masukan sebelumnya.",
                    "     Form yang mengosongkan dirinya setiap kali ada",
                    "     kesalahan adalah cara tercepat membuat orang",
                    "     menyerah.",
                    "",
                    "  4. Validasi umur memakai rentang, bukan cuma 'apakah",
                    "     angka'. Umur 99999 lolos pemeriksaan tipe.",
                    "",
                    "  5. `(int) $_SESSION['umur']` saat dicetak — pertahanan",
                    "     berlapis, kalau-kalau sesi berisi sesuatu yang lain.",
                    "",
                    "YANG BELUM ADA di contoh ini dan WAJIB ada di produksi:",
                    "TOKEN CSRF. Tanpa itu, situs lain bisa membuat browser",
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
                    "`hash_equals` dipakai alih-alih `===` karena ia",
                    "membandingkan dalam waktu tetap, sehingga tidak bocor",
                    "informasi lewat selisih waktu.",
                    "",
                    "Setelah POST berhasil, praktik yang baik adalah",
                    "REDIRECT (pola Post/Redirect/Get). Tanpa itu, menekan",
                    "Refresh mengirim ulang datanya.",
                ]
            },
        ],
    },
    {
        "title": "14. Database dengan PDO",
        "sections": [
            {
                "body": [
                    "PDO (PHP Data Objects) adalah antarmuka database bawaan",
                    "PHP. Satu API yang sama untuk MySQL, PostgreSQL, SQLite,",
                    "dan lainnya.",
                    "",
                    "Menyambung:",
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
                    "KETIGA opsi itu bukan hiasan:",
                    "",
                    "  ERRMODE_EXCEPTION  tanpa ini, query yang gagal cuma",
                    "                     mengembalikan false dan programmu",
                    "                     berjalan terus dengan data kosong.",
                    "  FETCH_ASSOC        hasilnya array berkunci nama kolom",
                    "                     saja, bukan sekaligus berindeks",
                    "                     angka — separuh memori terbuang.",
                    "  EMULATE_PREPARES   false berarti prepared statement",
                    "                     SUNGGUHAN dikirim ke server, bukan",
                    "                     ditiru di sisi PHP. Yang ditiru",
                    "                     masih menyambung string, dan itu",
                    "                     pernah punya celah injeksi lewat",
                    "                     charset tertentu.",
                    "",
                    "PREPARED STATEMENT — satu-satunya cara yang benar:",
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
                    "KENAPA ini wajib: nilai dikirim TERPISAH dari perintah",
                    "SQL-nya. Database menerima strukturnya dulu, baru",
                    "datanya, sehingga apa pun isi datanya ia tidak pernah",
                    "bisa berubah jadi perintah.",
                    "",
                    "  SALAH:  \"SELECT * FROM user WHERE nama = '$nama'\"",
                    "  BENAR:  prepare + execute",
                    "",
                    "Dengan yang salah, $nama berisi  ' OR '1'='1  membuat",
                    "query mengembalikan SELURUH tabel. Ini SQL injection,",
                    "dan ia masih menjadi salah satu celah paling umum di",
                    "web sampai hari ini.",
                    "",
                    "Yang TIDAK bisa di-bind: nama tabel dan nama kolom.",
                    "Untuk itu, cocokkan dengan daftar putih:",
                    "",
                    "  $boleh = ['nama', 'nilai', 'kelas'];",
                    "  $urut = in_array($_GET['urut'] ?? '', $boleh, true)",
                    "      ? $_GET['urut'] : 'nama';",
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
                    "`sqlite::memory:` membuat database di RAM yang lenyap",
                    "saat program selesai — sempurna untuk belajar dan untuk",
                    "tes otomatis, karena tiap jalan mulai dari keadaan yang",
                    "sama persis.",
                    "",
                    "Method PDOStatement yang perlu kamu kenal:",
                    "  fetch()        satu baris berikutnya, false kalau habis",
                    "  fetchAll()     SEMUA baris sekaligus",
                    "  fetchColumn()  satu nilai saja",
                    "  rowCount()     berapa baris terpengaruh (untuk",
                    "                 INSERT/UPDATE/DELETE)",
                    "",
                    "Untuk hasil yang sangat besar, jangan `fetchAll()` —",
                    "ia menarik semuanya ke memori. Telusuri langsung:",
                    "`foreach ($stmt as $baris) { ... }`",
                    "",
                    "TRANSAKSI memastikan beberapa perubahan terjadi",
                    "SELURUHNYA atau TIDAK SAMA SEKALI. Untuk transfer saldo",
                    "antar rekening, tanpa transaksi ada jendela waktu di",
                    "mana uang sudah dikurangi dari satu sisi tapi belum",
                    "ditambahkan di sisi lain — dan kalau server mati persis",
                    "di situ, uangnya lenyap.",
                    "",
                    "Di proyek nyata, kredensial database TIDAK PERNAH ditulis",
                    "di kode. Ia tinggal di variabel lingkungan atau berkas",
                    ".env yang tidak ikut masuk ke git.",
                ]
            },
        ],
    },
    {
        "title": "15. Composer, Autoload & Namespace",
        "sections": [
            {
                "body": [
                    "NAMESPACE mencegah nama bertabrakan antar pustaka:",
                    "",
                    "  <?php",
                    "  namespace Toko\\Domain;",
                    "",
                    "  class Produk { }      jadi Toko\\Domain\\Produk",
                    "",
                    "Pemisahnya BACKSLASH, bukan titik atau titik dua.",
                    "Namespace ditulis di baris pertama sesudah <?php.",
                    "",
                    "  use Toko\\Domain\\Produk;",
                    "  use Toko\\Domain\\Produk as ProdukToko;",
                    "  use function Toko\\Util\\format;",
                    "  use const Toko\\Util\\VERSI;",
                    "",
                    "Nama berawalan backslash adalah absolut dari akar:",
                    "`\\DateTime` merujuk class bawaan PHP, bukan",
                    "`Toko\\Domain\\DateTime`. Di dalam namespace, class bawaan",
                    "PHP HARUS diawali backslash atau di-`use` lebih dulu —",
                    "kesalahan yang sangat sering saat pertama memakai",
                    "namespace.",
                    "",
                    "COMPOSER adalah package manager PHP:",
                    "",
                    "  composer init                 buat composer.json",
                    "  composer require guzzlehttp/guzzle",
                    "  composer require --dev phpunit/phpunit",
                    "  composer install              pasang dari composer.lock",
                    "  composer update               perbarui, tulis lock baru",
                    "  composer dump-autoload -o     optimalkan autoloader",
                    "",
                    "AUTOLOAD PSR-4 adalah kesepakatan yang membuat semuanya",
                    "bekerja: nama namespace MEMETAKAN ke struktur folder,",
                    "sehingga PHP bisa menemukan berkas class dari namanya",
                    "saja — tanpa satu pun `require`.",
                    "",
                    "  \"autoload\": {",
                    "      \"psr-4\": { \"Toko\\\\\": \"src/\" }",
                    "  }",
                    "",
                    "  Toko\\Domain\\Produk  ->  src/Domain/Produk.php",
                    "",
                    "Satu baris `require 'vendor/autoload.php';` di titik",
                    "masuk aplikasi, dan seluruh class di proyek beserta",
                    "seluruh dependensinya bisa dipakai.",
                    "",
                    "Standar PSR yang paling penting diketahui:",
                    "  PSR-1 & PSR-12  gaya penulisan kode",
                    "  PSR-4           autoloading",
                    "  PSR-3           antarmuka logger",
                    "  PSR-7           pesan HTTP",
                    "  PSR-11          container",
                    "",
                    "composer.lock WAJIB masuk git untuk aplikasi: itulah",
                    "yang membuat pemasangan hari ini dan enam bulan lagi",
                    "menghasilkan versi yang sama persis. Untuk pustaka,",
                    "biasanya tidak.",
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
                    "SATU HAL di struktur itu yang paling sering salah dan",
                    "paling mahal akibatnya: hanya folder `public/` yang boleh",
                    "dijangkau web server. Document root diarahkan ke situ,",
                    "bukan ke akar proyek.",
                    "",
                    "Kalau akar proyek yang diarahkan, siapa pun bisa membuka",
                    "`https://situsmu.com/.env` dan membaca sandi database-mu.",
                    "Ini bukan skenario teoretis — pemindai otomatis mencoba",
                    "URL itu di setiap situs PHP di internet, setiap hari.",
                    "",
                    "Berkas yang WAJIB masuk .gitignore:",
                    "  /vendor/",
                    "  /.env",
                    "  /node_modules/",
                    "  *.log",
                    "",
                    "Dan .env.example yang JUSTRU masuk git, berisi nama",
                    "variabelnya dengan nilai kosong — supaya orang berikutnya",
                    "tahu apa saja yang harus ia isi.",
                    "",
                    "Alat pengembangan yang layak dipasang sejak awal:",
                    "  phpunit          pengujian",
                    "  phpstan / psalm  analisis statis, menemukan bug tanpa",
                    "                   menjalankan kode",
                    "  php-cs-fixer     merapikan gaya penulisan otomatis",
                    "  rector           memodernkan kode lama secara otomatis",
                    "",
                    "PHPStan layak diperhatikan khusus: ia memeriksa tipe",
                    "jauh lebih dalam daripada PHP sendiri dan menemukan",
                    "seluruh kelas bug — property yang tidak pernah ada,",
                    "method yang salah nama, nilai null yang tidak diperiksa —",
                    "tanpa satu baris pun dijalankan. Mulai dari level 5,",
                    "naikkan pelan-pelan.",
                ]
            },
        ],
    },
    {
        "title": "16. Praktik Baik & Keamanan",
        "sections": [
            {
                "body": [
                    "Ringkasan hal-hal yang paling sering salah di PHP, dan",
                    "yang paling mahal kalau dibiarkan.",
                    "",
                    "KEAMANAN",
                    "",
                    "  1. SQL injection -> prepared statement, SELALU.",
                    "     Tidak ada pengecualian, tidak ada 'ini kan cuma id'.",
                    "",
                    "  2. XSS -> htmlspecialchars di setiap titik keluaran.",
                    "     Bukan saat menyimpan, tapi saat MENAMPILKAN. Data",
                    "     yang sama bisa keluar ke HTML, ke JSON, dan ke",
                    "     email, dan pelariannya berbeda-beda.",
                    "",
                    "  3. Password -> password_hash / password_verify.",
                    "     JANGAN md5, sha1, atau apa pun yang cepat. Justru",
                    "     KELAMBATANNYA yang melindungi.",
                    "",
                    "     $hash = password_hash($sandi, PASSWORD_DEFAULT);",
                    "     if (password_verify($sandi, $hash)) { ... }",
                    "",
                    "  4. CSRF -> token per sesi, diperiksa dengan hash_equals.",
                    "",
                    "  5. Unggahan berkas -> jangan percaya nama maupun tipe",
                    "     yang dikirim browser. Periksa isinya, ganti namanya,",
                    "     dan simpan DI LUAR document root.",
                    "",
                    "  6. Angka acak -> random_int(), bukan rand() atau",
                    "     mt_rand(). Dua yang terakhir bisa ditebak.",
                    "",
                    "  7. Jangan pernah `eval()`, `extract()`, atau",
                    "     `unserialize()` pada data dari pengguna.",
                    "",
                    "KUALITAS KODE",
                    "",
                    "  - declare(strict_types=1) di SETIAP berkas.",
                    "  - Tulis tipe di semua parameter dan kembalian.",
                    "  - Pakai === dan !==, bukan == dan !=.",
                    "  - Jangan pakai @ untuk membungkam galat.",
                    "  - Pulang lebih awal (guard clause) alih-alih if",
                    "    bertingkat.",
                    "  - Satu class satu berkas, namanya sama.",
                    "  - Kembalikan array kosong, bukan null, untuk koleksi.",
                    "",
                    "PENAMAAN menurut PSR-12:",
                    "  StudlyCaps   nama class, interface, trait, enum",
                    "  camelCase    method dan property",
                    "  camelCase    variabel (banyak proyek memakai snake_case,",
                    "               dan itu juga konsisten -- yang penting satu",
                    "               gaya di seluruh proyek)",
                    "  UPPER_CASE   konstanta",
                    "",
                    "  Empat spasi indentasi, bukan tab.",
                    "  Kurung kurawal class dan method di baris BARU;",
                    "  kurung kurawal kendali alur di baris yang SAMA.",
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
                    "Baris kedua menunjukkan apa yang sebenarnya dilakukan",
                    "htmlspecialchars: ia mengubah karakter yang PUNYA ARTI",
                    "di HTML jadi entitas. Browser menampilkannya sebagai",
                    "teks, bukan menjalankannya sebagai skrip.",
                    "",
                    "`$2y$12` di awal hash adalah penanda algoritma bcrypt",
                    "dengan cost 12. Cost itu yang membuatnya lambat — dan",
                    "kelambatan itulah fiturnya: penyerang yang mencuri",
                    "database-mu hanya bisa mencoba beberapa ribu tebakan per",
                    "detik alih-alih miliaran.",
                    "",
                    "`password_hash` menyertakan salt acak di dalam hasilnya",
                    "sendiri, jadi kamu TIDAK perlu menyimpan salt terpisah.",
                    "Dua pengguna dengan sandi sama menghasilkan hash berbeda.",
                    "",
                    "`password_needs_rehash()` layak dipanggil saat login",
                    "berhasil: kalau algoritma bawaan PHP naik di versi",
                    "berikutnya, sandi pengguna ikut ditingkatkan diam-diam",
                    "tanpa mereka perlu menggantinya.",
                    "",
                    "Terakhir, satu kebiasaan yang bernilai tinggi: jalankan",
                    "PHPStan level 6 ke atas pada proyekmu. Ia menemukan",
                    "seluruh kelas kesalahan — method yang salah nama,",
                    "property yang tidak pernah ada, nilai null yang tidak",
                    "diperiksa — sebelum satu baris pun dijalankan.",
                ]
            },
        ],
    },
    {
        "title": "17. Tanggal & Waktu",
        "sections": [
            {
                "body": [
                    "PHP punya DUA API waktu, dan yang lama sebaiknya",
                    "ditinggalkan:",
                    "",
                    "  LAMA   date(), time(), strtotime(), mktime()",
                    "         Berbasis timestamp integer. Masih dipakai luas,",
                    "         tapi tidak membawa zona waktu dan gampang salah.",
                    "  BARU   DateTimeImmutable, DateTime, DateInterval,",
                    "         DateTimeZone, DatePeriod. Berorientasi objek.",
                    "",
                    "Pakai DateTimeImmutable, bukan DateTime. Bedanya sama",
                    "seperti String di bahasa lain: method pada DateTime",
                    "MENGUBAH objek aslinya, sedangkan DateTimeImmutable",
                    "mengembalikan objek baru. Yang pertama sumber bug yang",
                    "sangat sulit dilihat:",
                    "",
                    "  $besok = $hari->modify('+1 day');",
                    "  // dengan DateTime, $hari IKUT berubah jadi besok",
                    "",
                    "Membuat:",
                    "  new DateTimeImmutable()              sekarang",
                    "  new DateTimeImmutable('2026-09-22')",
                    "  new DateTimeImmutable('+3 days')",
                    "  DateTimeImmutable::createFromFormat('d/m/Y', '22/09/2026')",
                    "",
                    "Memformat:",
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
                    "ZONA WAKTU adalah sumber bug nomor satu di aplikasi yang",
                    "dipakai lintas wilayah. Aturan praktisnya:",
                    "  - Simpan SEMUA waktu di database dalam UTC.",
                    "  - Ubah ke zona pengguna hanya saat MENAMPILKAN.",
                    "  - Setel date_default_timezone_set('UTC') di awal.",
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
                    "Baris terakhir menunjukkan kenapa zona waktu penting:",
                    "waktu yang sama persis jatuh di TANGGAL YANG BERBEDA",
                    "tergantung dari mana orang melihatnya. Laporan 'penjualan",
                    "hari ini' yang dihitung tanpa zona waktu akan salah untuk",
                    "sebagian penggunamu, setiap hari.",
                    "",
                    "Format DateInterval memakai notasi ISO 8601:",
                    "  P1Y      1 tahun       P30D     30 hari",
                    "  P3M      3 bulan       PT2H     2 jam",
                    "  P1W      1 minggu      PT30M    30 menit",
                    "  P1Y2M3D  gabungan      PT1H30M  1 jam 30 menit",
                    "",
                    "Huruf T memisahkan bagian tanggal dari bagian waktu.",
                    "`P1M` adalah satu BULAN, `PT1M` adalah satu MENIT.",
                    "",
                    "PERINGATAN soal menambah bulan: `2026-01-31` ditambah",
                    "satu bulan menghasilkan `2026-03-03`, bukan akhir",
                    "Februari — karena 31 Februari tidak ada dan PHP",
                    "melimpahkannya ke bulan berikutnya. Untuk 'akhir bulan",
                    "berikutnya' pakai `modify('last day of next month')`.",
                ]
            },
        ],
    },
    {
        "title": "18. Ekspresi Reguler",
        "sections": [
            {
                "body": [
                    "PHP memakai PCRE (Perl Compatible Regular Expressions).",
                    "Polanya ditulis sebagai string dengan PEMBATAS di kedua",
                    "ujung — biasanya garis miring:",
                    "",
                    "  '/^\\d{4}-\\d{2}-\\d{2}$/'",
                    "",
                    "Pembatasnya bebas asal konsisten. Kalau polanya memuat",
                    "banyak garis miring (misalnya URL), pakai pembatas lain",
                    "supaya tidak perlu melarikan semuanya: '~https?://~'",
                    "",
                    "Fungsi utamanya:",
                    "  preg_match($pola, $teks, $cocok)    0 atau 1, sekali",
                    "  preg_match_all($pola, $teks, $semua) berapa kali cocok",
                    "  preg_replace($pola, $ganti, $teks)",
                    "  preg_replace_callback($pola, $fn, $teks)",
                    "  preg_split($pola, $teks)",
                    "  preg_quote($teks)                   lolos karakter khusus",
                    "",
                    "Ketiganya mengembalikan `false` saat pola rusak — periksa",
                    "dengan `=== false`, bukan `!`.",
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
                    "  *?  +?   versi MALAS (ambil sesedikit mungkin)",
                    "",
                    "  (...)    grup penangkap",
                    "  (?:...)  grup TANPA menangkap",
                    "  (?<nama>...)  grup bernama",
                    "  a|b      salah satu",
                    "",
                    "Penanda sesudah pembatas penutup:",
                    "  i  abaikan besar-kecil huruf",
                    "  m  ^ dan $ berlaku per BARIS",
                    "  s  titik juga cocok dengan baris baru",
                    "  u  perlakukan pola dan teks sebagai UTF-8",
                    "  x  abaikan spasi di pola, supaya bisa diberi komentar",
                    "",
                    "Penanda `u` HAMPIR SELALU perlu untuk teks berbahasa",
                    "Indonesia atau apa pun yang bukan ASCII murni. Tanpa itu,",
                    "satu huruf beraksen dihitung sebagai beberapa karakter.",
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
                    "  ---",
                    "  2026-09-22 09:15:03 INFO  masuk user=andi ip=10.0.0.xxx",
                    "  2026-09-22   -> sah",
                    "  22/09/2026   -> tidak sah",
                    "  2026-13-40   -> tidak sah",
                    "",
                    "Baris yang formatnya tidak dikenal DILEWATI begitu saja",
                    "— itulah gunanya `^...$` dengan penanda `m`: ia menuntut",
                    "seluruh baris cocok, bukan sepotong di tengahnya.",
                    "",
                    "GRUP BERNAMA `(?<tanggal>...)` membuat hasilnya bisa",
                    "dibaca `$b['tanggal']` alih-alih `$b[1]`. Untuk pola",
                    "dengan lebih dari dua grup, ini menghemat banyak",
                    "kebingungan saat polanya nanti disunting.",
                    "",
                    "`PREG_SET_ORDER` mengelompokkan hasil PER KECOCOKAN.",
                    "Tanpa flag itu (PREG_PATTERN_ORDER, bawaannya), hasilnya",
                    "dikelompokkan per GRUP — bentuk yang jauh lebih sulit",
                    "ditelusuri.",
                    "",
                    "PERINGATAN yang layak ditanam: JANGAN mengurai HTML",
                    "dengan regex. HTML bisa bersarang tanpa batas dan regex",
                    "tidak bisa menghitung kedalaman. Pakai DOMDocument.",
                    "Yang cocok untuk regex: format yang BERBARIS dan",
                    "BERPOLA TETAP seperti log, CSV sederhana, dan validasi.",
                    "",
                    "Waspadai juga CATASTROPHIC BACKTRACKING: pola seperti",
                    "`(a+)+$` pada teks panjang bisa menggantung selama",
                    "bertahun-tahun. Hindari kuantifier bersarang.",
                ]
            },
        ],
    },
    {
        "title": "19. Generator & Iterator",
        "sections": [
            {
                "body": [
                    "Fungsi biasa menghitung SELURUH hasilnya lalu",
                    "mengembalikannya sekaligus. Untuk sejuta baris, itu",
                    "berarti sejuta baris di memori.",
                    "",
                    "GENERATOR menghasilkan nilai SATU PER SATU, hanya saat",
                    "diminta. Tandanya kata kunci `yield`:",
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
                    "Yang dipakai memorinya cuma SATU angka pada satu waktu,",
                    "berapa pun besarnya. Begitu sebuah fungsi memuat `yield`,",
                    "ia otomatis jadi generator — memanggilnya TIDAK",
                    "menjalankan badannya sama sekali sampai ada yang mulai",
                    "menelusuri.",
                    "",
                    "yield juga bisa membawa KUNCI:",
                    "  yield $nama => $nilai;",
                    "",
                    "dan meneruskan generator lain:",
                    "  yield from generatorLain();",
                    "",
                    "Generator bisa mengembalikan nilai akhir:",
                    "  return $total;      dibaca dengan $gen->getReturn()",
                    "",
                    "PEMAKAIAN PALING BERHARGA: membaca berkas besar.",
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
                    "Berkas 10 GB bisa diproses di mesin dengan RAM 512 MB.",
                    "`finally` memastikan berkasnya ditutup walau penelusuran",
                    "dihentikan di tengah dengan `break`.",
                    "",
                    "ITERATOR adalah bentuk panjangnya: sebuah class yang",
                    "mengimplementasi `Iterator` (current, key, next, rewind,",
                    "valid). Generator melakukan hal yang sama dalam beberapa",
                    "baris — pakai generator kecuali kamu butuh keadaan yang",
                    "rumit.",
                    "",
                    "`IteratorAggregate` lebih sering berguna: implementasi",
                    "`getIterator()` membuat objekmu bisa langsung di-foreach.",
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
                    "`fibonacci()` adalah deret TANPA BATAS. Menulisnya sebagai",
                    "array mustahil; sebagai generator ia wajar dan aman,",
                    "karena `ambil()` berhenti memintanya begitu cukup.",
                    "",
                    "Perhatikan `saring()` juga generator, sehingga rantai",
                    "`ambil(saring(fibonacci(), ...), 6)` tetap MALAS dari",
                    "ujung ke ujung: tidak ada satu pun array perantara yang",
                    "dibuat. Ini pola yang sama dengan iterator di Rust dan",
                    "LINQ di C#.",
                    "",
                    "`iterator_to_array()` memaksa generator berjalan sampai",
                    "habis dan mengumpulkan hasilnya jadi array. Untuk",
                    "generator tanpa batas, ia HANYA aman kalau sudah dibatasi",
                    "— memanggilnya langsung pada `fibonacci()` akan",
                    "menggantung sampai memori habis.",
                    "",
                    "`IteratorAggregate` memberi class-mu kemampuan di-foreach",
                    "dengan menulis satu method saja. `Countable` membuat",
                    "`count($objek)` bekerja. Keduanya contoh bagus dari",
                    "prinsip yang berlaku di seluruh PHP: implementasi satu",
                    "interface bawaan menyambungkan objekmu ke sintaks",
                    "bahasanya sendiri.",
                ]
            },
        ],
    },
    {
        "title": "20. Anggota Statis & Method Ajaib",
        "sections": [
            {
                "body": [
                    "ANGGOTA STATIS milik CLASS, bukan objek:",
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
                    "Di dalam method statis TIDAK ADA `$this` — tidak ada objek",
                    "yang sedang dikerjakan. Yang tersedia `self::` dan",
                    "`static::`.",
                    "",
                    "Beda self:: dan static::, dan ini yang sering menjebak:",
                    "  self::     merujuk class tempat kode itu DITULIS",
                    "  static::   merujuk class yang benar-benar DIPANGGIL",
                    "",
                    "Yang kedua disebut LATE STATIC BINDING, dan ia yang",
                    "membuat method pabrik di class induk bisa menghasilkan",
                    "objek turunan:",
                    "",
                    "  public static function buat(): static",
                    "  {",
                    "      return new static();",
                    "  }",
                    "",
                    "Dengan `new self()`, `Turunan::buat()` akan menghasilkan",
                    "objek INDUK — hampir pasti bukan yang kamu maksud.",
                    "",
                    "METHOD AJAIB dipanggil PHP secara otomatis:",
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
                    "PERINGATAN: method ajaib membuat kode sulit dilacak.",
                    "Editor tidak bisa melengkapi otomatis, analisis statis",
                    "buta, dan salah ketik nama property jadi diam-diam",
                    "diterima `__set`. Pakai seperlunya, dan kalau memakai",
                    "`__get`/`__call`, sertakan anotasi `@property` dan",
                    "`@method` supaya alat bantu tetap mengerti.",
                    "",
                    "`__clone` penting untuk SALINAN DALAM: `clone $objek`",
                    "membuat salinan DANGKAL, sehingga property yang berupa",
                    "objek tetap ditunjuk bersama oleh keduanya.",
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
                    "`new static($id)` di class induk menghasilkan `Produk`",
                    "saat dipanggil `Produk::buat()` dan `Pesanan` saat",
                    "dipanggil `Pesanan::buat()`. Dengan `new self()`, keduanya",
                    "akan mencoba membuat `Model` — yang abstract, sehingga",
                    "programnya langsung gagal.",
                    "",
                    "`static::class` memberi nama class yang sesungguhnya saat",
                    "program jalan. `$objek::class` (PHP 8) melakukan hal yang",
                    "sama dari sisi objeknya, menggantikan `get_class($objek)`.",
                    "",
                    "Bagian keranjang menunjukkan kenapa `__clone` ada. Tanpa",
                    "baris `$this->isi = clone $this->isi;`, menambah teh ke",
                    "k2 akan ikut menambahkannya ke k1 — karena `clone` bawaan",
                    "cuma menyalin REFERENSI ke ArrayObject-nya.",
                    "",
                    "Aturan yang layak dihafal: array di PHP disalin saat",
                    "ditugaskan, OBJEK tidak. Jadi property yang berupa objek",
                    "adalah satu-satunya yang butuh perhatian di `__clone`.",
                    "",
                    "Anggota statis berguna untuk pabrik, penghitung, dan",
                    "konstanta. Yang HARUS dihindari: memakainya sebagai",
                    "tempat penyimpanan keadaan aplikasi. Keadaan statis",
                    "tidak bisa direset antar tes, tidak bisa diganti palsu",
                    "saat pengujian, dan membuat dua bagian program saling",
                    "memengaruhi lewat jalan yang tidak terlihat di manapun.",
                ]
            },
        ],
    },
    {
        "title": "21. Pengujian dengan PHPUnit",
        "sections": [
            {
                "body": [
                    "PHPUnit adalah kerangka tes standar di dunia PHP.",
                    "",
                    "  composer require --dev phpunit/phpunit",
                    "  ./vendor/bin/phpunit",
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
                    "Nama method HARUS diawali `test`, atau diberi atribut",
                    "`#[Test]`. Nama class berakhiran `Test`.",
                    "",
                    "Assertion yang paling sering dipakai:",
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
                    "PAKAI assertSame, BUKAN assertEquals. assertEquals",
                    "memakai perbandingan longgar, sehingga `'5'` dinyatakan",
                    "sama dengan `5` dan tesmu berhenti menangkap bug tipe —",
                    "persis kelas bug yang paling sering di PHP.",
                    "",
                    "DATA PROVIDER menjalankan tes yang sama dengan banyak",
                    "data:",
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
                    "Kunci array jadi nama kasusnya, dan itu yang muncul saat",
                    "sebuah kasus gagal — jauh lebih berguna daripada 'with",
                    "data set #3'.",
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
                    "Perhatikan nilai yang dipilih di data provider: 85 dan 84,",
                    "75 dan 74, 60 dan 59. Menguji tepat DI BATAS adalah yang",
                    "paling berharga, karena di situlah `>=` versus `>` salah",
                    "ketik. Nilai di tengah rentang hampir tidak pernah",
                    "menemukan bug.",
                    "",
                    "`setUp()` dijalankan sebelum SETIAP method tes, sehingga",
                    "tiap tes mulai dari keadaan yang sama persis. Tes yang",
                    "bergantung pada urutan menjalankannya adalah tes yang",
                    "suatu hari gagal tanpa ada yang mengubah apa pun.",
                    "",
                    "`assertSame(85.0, ...)` dengan titik nol bukan kelebihan",
                    "ketikan: `assertSame(85, ...)` akan GAGAL karena 85",
                    "adalah int sedangkan hasilnya float. Ketatnya itulah",
                    "yang kita inginkan.",
                    "",
                    "Berkas konfigurasi `phpunit.xml` di akar proyek:",
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
                    "Cakupan tes (coverage) berguna untuk MENEMUKAN yang",
                    "belum diuji, bukan sebagai nilai yang dikejar. Cakupan",
                    "100% dengan assertion yang lemah lebih buruk daripada",
                    "cakupan 70% yang benar-benar memeriksa perilaku.",
                ]
            },
        ],
    },
]
