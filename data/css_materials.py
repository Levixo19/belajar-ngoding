CSS_MATERIALS = [
    {
        "title": "1. Apa Itu CSS & Tiga Cara Menautkannya",
        "sections": [
            {
                "body": [
                    "HTML menentukan APA isi halaman. CSS menentukan BAGAIMANA isi itu",
                    "terlihat: warna, ukuran huruf, jarak, dan tata letaknya.",
                    "",
                    "CSS = Cascading Style Sheets. Kata 'cascading' (air terjun) itu",
                    "penting dan akan dijelaskan di materi 2.",
                    "",
                    "Tanpa satu baris CSS pun, halaman HTML tetap tampil: judul besar,",
                    "tautan biru bergaris bawah, paragraf berjarak. Itu bukan sihir -",
                    "tiap browser punya lembar gaya bawaan (user agent stylesheet).",
                    "Yang kamu tulis MENIMPA gaya bawaan itu, bukan mulai dari nol.",
                    "Karena itu bentuk awal sebuah halaman tidak pernah benar-benar",
                    "kosong, dan kadang yang perlu kamu lakukan justru mematikan",
                    "bawaan (misalnya list-style: none pada daftar).",
                    "",
                    "Bentuk satu aturan CSS:",
                    "",
                    "  p { color: red; }",
                    "  ^   ^^^^^  ^^^",
                    "  |   |      nilai",
                    "  |   properti",
                    "  pemilih (selector)",
                    "",
                    "Istilahnya:",
                    "  - PEMILIH menentukan elemen mana yang kena aturan ini.",
                    "  - DEKLARASI adalah pasangan 'properti: nilai'.",
                    "  - Satu aturan boleh memuat banyak deklarasi, dipisah titik koma.",
                    "",
                    "Deklarasi terakhir sebenarnya boleh tanpa titik koma, tapi tetap",
                    "tulis titik komanya - supaya menambah baris berikutnya besok tidak",
                    "diam-diam merusak aturan yang sudah jalan.",
                ]
            },
            {
                "heading": "Tiga cara memasang CSS (index.html)",
                "code": """<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <title>Tiga cara memasang CSS</title>

  <!-- Cara 3: berkas terpisah -->
  <link rel="stylesheet" href="gaya.css">

  <!-- Cara 2: blok <style> di dalam halaman -->
  <style>
    p { color: navy; }
  </style>
</head>
<body>
  <!-- Cara 1: inline, gaya menempel di elemennya -->
  <h1 style="color: darkred">Judul Halaman</h1>

  <p>Paragraf ini biru tua karena aturan di blok style.</p>
</body>
</html>""",
            },
            {
                "body": [
                    "Tiga cara itu, dari yang paling buruk ke yang paling baik:",
                    "",
                    "1. INLINE - atribut style langsung di elemennya.",
                    "     <h1 style=\"color: darkred\">",
                    "   Hanya mengenai satu elemen itu. Tidak bisa dipakai ulang, tidak",
                    "   bisa memakai :hover, dan paling sulit ditimpa (lihat materi 2).",
                    "   Pakai hanya kalau nilainya memang dihitung program.",
                    "",
                    "2. BLOK <style> di dalam <head>.",
                    "   Berlaku untuk seluruh halaman ITU saja. Berguna untuk contoh",
                    "   kecil dan halaman sekali pakai.",
                    "",
                    "3. BERKAS TERPISAH lewat <link rel=\"stylesheet\" href=\"gaya.css\">.",
                    "   Ini yang dipakai di proyek sungguhan. Alasannya:",
                    "     - Satu berkas menata SEMUA halaman. Ganti warna sekali,",
                    "       lima puluh halaman ikut berubah.",
                    "     - Browser menyimpannya (cache), jadi halaman kedua dan",
                    "       seterusnya tidak perlu mengunduh gayanya lagi.",
                    "     - Isi dan tampilan terpisah, jadi HTML-nya tetap terbaca.",
                    "",
                    "<link> ditulis di dalam <head>. Atribut rel=\"stylesheet\" wajib -",
                    "tanpa itu browser tidak tahu berkas itu lembar gaya dan diam saja.",
                    "Salah menulis nama berkas juga tidak memberi pesan apa pun di",
                    "halaman: yang kamu lihat cuma halaman polos tanpa gaya.",
                ]
            },
            {
                "heading": "gaya.css",
                "code": """/* Ini komentar CSS. Tidak ada bentuk // seperti di JavaScript. */

body {
  background-color: #f7f7f5;
  color: #23252b;
  font-family: system-ui, sans-serif;
  line-height: 1.6;
}

h1 {
  color: #7a1f1f;
  font-size: 32px;
  margin-bottom: 8px;
}

a {
  color: #1a4fa0;
}""",
            },
            {
                "body": [
                    "Yang perlu diketahui sejak awal soal cara kerja CSS:",
                    "",
                    "CSS TIDAK PERNAH MEMBERI PESAN ERROR.",
                    "  Salah ketik 'colr: red' tidak menghentikan apa pun. Browser",
                    "  membuang deklarasi yang tidak dimengerti, lalu melanjutkan",
                    "  sisanya seolah tidak terjadi apa-apa. Ini disengaja supaya",
                    "  halaman lama tetap jalan di browser baru, tapi akibatnya",
                    "  kesalahanmu terlihat seperti 'aturannya tidak mempan'.",
                    "",
                    "  Kalau satu deklarasi rusak, HANYA baris itu yang dibuang.",
                    "  Aturan lain di blok yang sama tetap berlaku. Tapi kalau kurung",
                    "  kurawal yang hilang, browser bisa membuang beberapa aturan",
                    "  sekaligus - dan itu terasa seperti setengah halaman kehilangan",
                    "  gayanya tanpa sebab.",
                    "",
                    "Di aplikasi ini, berkas .css tidak dijalankan seperti program.",
                    "Isinya DIBACA lalu dicetak sebagai daftar aturan: pemilihnya di",
                    "kiri, propertinya menjorok dua spasi di bawahnya. Jadi tekan",
                    "Jalankan untuk memastikan yang kamu tulis benar-benar terbaca",
                    "sebagai CSS, bukan sekadar terlihat benar di layar.",
                    "",
                    "  body",
                    "    background-color: #f7f7f5",
                    "    color: #23252b",
                    "",
                    "Kalau ada aturan yang tidak muncul di daftar itu, berarti browser",
                    "pun tidak akan melihatnya.",
                ]
            },
        ],
    },
    {
        "title": "2. Pemilih: Elemen, Class, dan ID",
        "sections": [
            {
                "body": [
                    "Pemilih menjawab satu pertanyaan: aturan ini kena elemen yang mana?",
                    "",
                    "Pemilih dasar:",
                    "  p            semua elemen <p>",
                    "  .kartu       semua elemen ber-class=\"kartu\"   (diawali titik)",
                    "  #menu        elemen ber-id=\"menu\"             (diawali pagar)",
                    "  *            semua elemen",
                    "  h1, h2, h3   ketiganya sekaligus              (koma berarti 'atau')",
                    "",
                    "Menggabungkan pemilih:",
                    "  div p        <p> DI DALAM <div>, sedalam apa pun   (keturunan)",
                    "  div > p      <p> yang induk LANGSUNG-nya <div>     (anak)",
                    "  h2 + p       <p> tepat SESUDAH <h2>                (saudara berikut)",
                    "  h2 ~ p       semua <p> sesudah <h2> pada induk sama (saudara umum)",
                    "  p.penting    <p> yang SEKALIGUS ber-class 'penting'",
                    "",
                    "SPASI ITU BERMAKNA:",
                    "  .a .b   -> elemen ber-class b DI DALAM elemen ber-class a",
                    "  .a.b    -> SATU elemen yang punya kedua class sekaligus",
                    "Dua hal yang sangat berbeda, dibedakan hanya oleh satu spasi.",
                    "",
                    "Pemilih atribut:",
                    "  a[target]             punya atribut target, nilai apa pun",
                    "  input[type=\"text\"]    atributnya bernilai persis 'text'",
                    "  a[href^=\"https\"]      nilainya diawali 'https'",
                    "  a[href$=\".pdf\"]       nilainya diakhiri '.pdf'",
                    "  a[href*=\"contoh\"]     nilainya mengandung 'contoh'",
                ]
            },
            {
                "body": [
                    "CLASS ATAU ID?",
                    "",
                    "  class boleh dipakai berkali-kali dalam satu halaman.",
                    "  id hanya boleh muncul SEKALI per halaman.",
                    "",
                    "Satu elemen boleh punya beberapa class sekaligus, dipisah spasi:",
                    "  <div class=\"kartu besar aktif\">",
                    "Ketiganya berlaku bersamaan. Ini yang membuat class bisa disusun",
                    "seperti kepingan: .kartu mengurus bentuk dasar, .besar mengurus",
                    "ukuran, .aktif mengurus keadaan.",
                    "",
                    "Untuk MENATA TAMPILAN, pakai class. Sisakan id untuk keperluan",
                    "lain: tautan lompat (<a href=\"#bagian2\">) dan pegangan JavaScript.",
                    "Alasannya ada di bagian spesifisitas di bawah, dan itu alasan",
                    "yang praktis, bukan soal selera.",
                ]
            },
            {
                "heading": "Berbagai pemilih dalam satu berkas",
                "code": """/* Semua paragraf */
p {
  line-height: 1.6;
}

/* Class, dipakai berulang di banyak tempat */
.kartu {
  background: white;
  border: 1px solid #dcdcdc;
  padding: 16px;
}

/* Satu elemen yang punya DUA class ini sekaligus */
.kartu.penting {
  border-color: crimson;
}

/* Tautan di dalam kartu, sedalam apa pun */
.kartu a {
  color: #1a4fa0;
}

/* Hanya <li> yang induk langsungnya .menu */
.menu > li {
  display: inline-block;
}

/* Tiga pemilih, satu blok aturan */
h1, h2, h3 {
  font-family: Georgia, serif;
  line-height: 1.2;
}

/* Semua input bertipe teks */
input[type="text"] {
  padding: 8px;
  border: 1px solid #c9c9c9;
}""",
            },
            {
                "body": [
                    "CASCADE: SIAPA YANG MENANG",
                    "",
                    "Aturan datang dari banyak sumber sekaligus - bawaan browser,",
                    "berkas gayamu, blok <style>, atribut inline - dan sering mengatur",
                    "properti yang sama pada elemen yang sama. 'Cascade' adalah urutan",
                    "pertanyaan yang dipakai browser untuk memutuskan:",
                    "",
                    "  1. Ada yang ditandai !important?      -> yang itu menang.",
                    "  2. Mana yang SPESIFISITASnya lebih tinggi?  -> yang itu menang.",
                    "  3. Kalau seri, mana yang DITULIS BELAKANGAN? -> yang itu menang.",
                    "",
                    "Poin 3 sering menyelamatkan, dan sekaligus sering menjebak: dua",
                    "aturan setara, yang di bawah menang. Jadi urutan baris di berkas",
                    "gaya bukan soal kerapian - ia menentukan hasil.",
                    "",
                    "SPESIFISITAS dihitung sebagai tiga angka (a, b, c):",
                    "  a = jumlah #id di dalam pemilih",
                    "  b = jumlah .class, [atribut], dan :pseudo-class",
                    "  c = jumlah nama elemen dan ::pseudo-element",
                    "",
                    "Dibandingkan dari kiri: a dulu; kalau seri baru b; lalu c.",
                    "",
                    "  p                    (0,0,1)",
                    "  .kartu               (0,1,0)",
                    "  .kartu p             (0,1,1)",
                    "  .kartu .isi p span   (0,2,2)",
                    "  #menu                (1,0,0)",
                    "  style=\"...\"          inline, di atas semua pemilih",
                    "",
                    "(0,1,0) mengalahkan (0,0,11). Satu class menang atas sebelas nama",
                    "elemen - angkanya TIDAK dijumlahkan jadi satu, tapi dibandingkan",
                    "bertingkat. Ini yang membuat 'saya sudah menulis pemilih panjang",
                    "sekali kok masih kalah' terjadi.",
                ]
            },
            {
                "body": [
                    "KENAPA ID SEBAIKNYA TIDAK DIPAKAI UNTUK MENATA TAMPILAN",
                    "",
                    "#menu terlalu kuat. Hari ini terasa praktis. Bulan depan kamu",
                    "ingin satu menu tampil berbeda, lalu menulis .menu-gelap - dan",
                    "heran kenapa tidak berpengaruh. Untuk melawannya kamu terpaksa",
                    "menulis #menu.menu-gelap, dan sejak saat itu seluruh berkas ikut",
                    "naik ke tingkat id. Setelah beberapa bulan, satu-satunya cara",
                    "menimpa apa pun adalah !important.",
                    "",
                    "Mulailah dari spesifisitas serendah mungkin. Ruang di atasmu",
                    "adalah persediaan yang habis kalau dipakai terlalu cepat.",
                    "",
                    "!important MEMATIKAN seluruh perhitungan di atas:",
                    "  color: red !important;",
                    "",
                    "Ia menang atas apa pun. Masalahnya, satu-satunya cara melawan",
                    "!important adalah !important lain yang lebih spesifik - dan",
                    "sesudah itu tidak ada rem tersisa sama sekali. Pakai hanya untuk",
                    "menimpa CSS pihak lain yang tidak bisa kamu ubah.",
                    "",
                    "Kalau sebuah aturan 'tidak berpengaruh', hampir selalu satu dari",
                    "empat sebab ini:",
                    "  1. Pemilihnya tidak cocok dengan elemen mana pun (salah nama",
                    "     class, atau lupa titik di depannya).",
                    "  2. Ada aturan lain yang lebih spesifik.",
                    "  3. Ada aturan setara yang ditulis belakangan.",
                    "  4. Nama properti atau nilainya salah ketik, dan CSS membuangnya",
                    "     tanpa bilang apa-apa.",
                ]
            },
        ],
    },
    {
        "title": "3. Membaca Halaman dengan DevTools Browser",
        "sections": [
            {
                "body": [
                    "Sampai sini alurmu selalu sama: tulis CSS, muat ulang halaman, lalu",
                    "MENEBAK kenapa hasilnya begitu. Materi 2 sudah menjelaskan aturan",
                    "mana yang menang; sekarang saatnya MELIHAT jawabannya, bukan",
                    "menghitungnya di kepala.",
                    "",
                    "Setiap browser membawa satu alat bawaan bernama DevTools (developer",
                    "tools, 'alat pengembang'). Sudah terpasang, gratis, tidak perlu",
                    "diunduh. Di dalamnya browser membuka isi kepalanya: elemen apa saja",
                    "yang ada, aturan mana yang kena, siapa yang menang, dan berapa",
                    "ukuran tiap kotak - dengan angka sungguhan, bukan kira-kira.",
                    "",
                    "Alat ini penting justru karena sifat CSS yang sudah kamu tahu dari",
                    "materi 1: CSS tidak pernah memberi pesan error. DevTools adalah",
                    "pengganti pesan error yang tidak pernah kamu dapat itu.",
                    "",
                    "CARA MEMBUKANYA - pilih salah satu, hasilnya sama:",
                    "  - Klik kanan tepat di atas bagian yang bermasalah, lalu pilih",
                    "    'Inspect' atau 'Periksa elemen'. Ini yang paling sering dipakai,",
                    "    karena elemen yang kamu klik langsung ikut terpilih.",
                    "  - Tekan F12.",
                    "  - Ctrl+Shift+I (Windows/Linux), Cmd+Option+I (Mac).",
                    "",
                    "Isinya banyak panel, tapi untuk CSS cuma tiga yang benar-benar",
                    "dipakai sehari-hari:",
                    "",
                    "  Elements   pohon HTML halaman. Klik satu baris = pilih satu elemen.",
                    "  Styles     semua aturan CSS yang kena elemen terpilih itu.",
                    "  Computed   nilai AKHIR tiap properti sesudah semuanya dihitung.",
                    "",
                    "Styles dan Computed SELALU bicara tentang elemen yang sedang",
                    "terpilih di Elements. Salah memilih elemen berarti kamu membaca",
                    "jawaban untuk pertanyaan yang lain - dan itulah sebab nomor satu",
                    "orang menyangka DevTools-nya sendiri yang keliru.",
                    "",
                    "MEMASTIKAN YANG TERPILIH MEMANG YANG KAMU MAKSUD:",
                    "  - Baris terpilih tersorot di pohon, dan elemennya ikut disorot di",
                    "    halaman. Menggeser kursor menyusuri pohon menyalakan elemen satu",
                    "    per satu - cara tercepat menjawab 'div yang mana sih ini'.",
                    "  - Di BAWAH pohon ada barisan seperti jejak remah:",
                    "",
                    "      html > body > div.panel > button.tombol.bahaya",
                    "",
                    "    Itu jalur lengkap elemen terpilih dari akar sampai ke dirinya,",
                    "    beserta class-class yang menempel. Kalau ujungnya tertulis",
                    "    div.panel padahal kamu merasa sedang memeriksa tombolnya, kamu",
                    "    memang salah pilih: klik satu tingkat lebih dalam.",
                    "  - Ctrl+F di dalam panel Elements mencari teks, tag, atau pemilih.",
                    "    Ketik .bahaya di situ dan pohonnya melompat ke elemen pertama",
                    "    yang cocok.",
                    "",
                    "Satu hal yang wajib diluruskan sejak awal: yang kamu lihat di",
                    "Elements BUKAN isi berkas .html-mu. Itu pohon hidup hasil bacaan",
                    "browser, sudah termasuk tag yang ia tambal sendiri dan perubahan",
                    "yang dibuat JavaScript. Untuk melihat berkas aslinya apa adanya,",
                    "pakai Ctrl+U (View Source). Perbedaan keduanya justru sering jadi",
                    "petunjuk pertama saat ada yang aneh.",
                ],
            },
            {
                "heading": "Dua berkas untuk dibedah sendiri",
                "body": [
                    "Simpan kedua berkas di bawah ini dalam SATU folder, lalu buka",
                    "index.html di browser. Halamannya sengaja dibuat curang: dua tombol",
                    "dengan class yang PERSIS SAMA, tapi yang satu hijau dan yang satu",
                    "merah. Semua langkah di bawah nanti memakai halaman ini.",
                ],
                "code": """/* ===== File: index.html ===== */
<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <title>Halaman uji DevTools</title>
  <link rel="stylesheet" href="gaya.css">
</head>
<body>
  <h1>Tiga aturan memperebutkan satu tombol</h1>

  <div class="panel">
    <p>Tombol ini di DALAM panel.</p>
    <button class="tombol bahaya">Hapus</button>
  </div>

  <p>Tombol ini di LUAR panel, class-nya sama persis.</p>
  <button class="tombol bahaya">Hapus</button>
</body>
</html>

/* ===== File: gaya.css ===== */
/* 0. Wadah, supaya batas panelnya kelihatan. */
.panel {
  background: #f2f2ef;
  border: 1px solid #dcdcdc;
  padding: 16px;
}

/* 1. Bentuk dasar semua tombol. Spesifisitas (0,1,0). */
.tombol {
  background: #1a4fa0;
  color: #ffffff;
  font-size: 16px;
  margin: 8px;
  padding: 12px 20px;
  border: 2px solid #123a78;
  border-radius: 6px;
}

/* 2. Spesifisitas SAMA dengan .tombol (0,1,0), tapi ditulis belakangan,
      jadi background di sini menang. */
.bahaya {
  background: #b3261e;
}

/* 3. Spesifisitas (0,2,0): lebih tinggi, menang atas keduanya - tapi
      hanya untuk tombol yang berada di dalam .panel. */
.panel .tombol {
  background: #2f7d32;
}

/* 4. Keadaan hover. Perlu tombol :hov di DevTools supaya bisa diamati
      dengan tenang. */
.tombol:hover {
  background: #0f3f8a;
}""",
            },
            {
                "body": [
                    "PANEL STYLES: MENONTON CASCADE BEKERJA",
                    "",
                    "Klik kanan tombol HIJAU, pilih Inspect. Panel Styles menampilkan",
                    "semua aturan yang mengenai tombol itu, kira-kira begini:",
                    "",
                    "  element.style { }                              <- kosong",
                    "  .panel .tombol { background: #2f7d32; }        gaya.css:27",
                    "  .bahaya        { background: #b3261e; }        gaya.css:21",
                    "  .tombol        { background: #1a4fa0;          gaya.css:9",
                    "                   color: #ffffff; ... }",
                    "",
                    "Lima hal yang harus kamu baca dari layar itu:",
                    "",
                    "1. BACA DARI ATAS. Urutan di panel ini BUKAN urutan berkasmu -",
                    "   DevTools sudah mengurutkannya berdasarkan cascade: yang MENANG",
                    "   di atas, yang kalah di bawah. Pertanyaan 'siapa yang menang'",
                    "   sudah dijawab sebelum kamu sempat menghitung apa pun.",
                    "",
                    "2. YANG DICORET BERARTI KALAH. background di .bahaya dan di .tombol",
                    "   tampil tercoret karena .panel .tombol menang. Perhatikan: yang",
                    "   dicoret HANYA barisnya, bukan seluruh aturannya - color, padding,",
                    "   dan border-radius di .tombol tetap tegak dan tetap berlaku. Satu",
                    "   aturan bisa kalah di satu properti dan menang di properti lain.",
                    "   Inilah pelajaran spesifisitas materi 2, terlihat dengan mata.",
                    "",
                    "3. Sekarang klik kanan tombol MERAH dan bandingkan. Aturan",
                    "   .panel .tombol LENYAP sama sekali dari daftar - pemilihnya",
                    "   memang tidak cocok, karena tombol itu bukan keturunan .panel.",
                    "   Yang menang .bahaya: spesifisitasnya seri dengan .tombol, dan",
                    "   yang seri diselesaikan oleh urutan penulisan. Kalau sebuah",
                    "   aturan tidak muncul di daftar sama sekali, itu jawaban paling",
                    "   berharga: pemilihmu tidak kena, jadi berhentilah mengutak-atik",
                    "   isi bloknya.",
                    "",
                    "4. Di kanan tiap aturan ada nama berkas dan nomor barisnya",
                    "   (gaya.css:27). Klik, dan DevTools melompat ke baris itu. Di",
                    "   proyek yang punya lima berkas gaya, ini yang menjawab 'aturan ini",
                    "   sebenarnya ditulis di berkas yang mana'.",
                    "",
                    "5. Geser kursor ke sebuah deklarasi: muncul KOTAK CENTANG di",
                    "   kirinya. Hilangkan centangnya, deklarasi itu mati sementara dan",
                    "   halaman berubah saat itu juga. Ini alat pembuktian tercepat yang",
                    "   kamu punya: matikan satu per satu sampai gejalanya hilang, dan",
                    "   baris terakhir yang kamu matikan itulah yang bersalah.",
                    "",
                    "CORETAN PUNYA DUA ARTI - jangan tertukar:",
                    "  - Tercoret polos                      -> kalah cascade.",
                    "  - Tercoret + segitiga kuning peringatan -> browser TIDAK MENGERTI",
                    "    baris itu: nama propertinya salah ketik, atau nilainya tidak",
                    "    sah untuk properti itu.",
                    "",
                    "Peringatan yang kedua itu satu-satunya hal yang menyerupai pesan",
                    "error di seluruh CSS, dan ia cuma muncul di sini - tidak di halaman,",
                    "tidak di mana pun. Coba sendiri: ubah 'background'",
                    "jadi 'bacground' di gaya.css, muat ulang, lalu lihat barisnya. Yang",
                    "di halaman tidak berubah apa-apa; yang di panel Styles langsung",
                    "menunjuk hidungmu.",
                    "",
                    "Blok element.style di paling atas adalah isi atribut style=\"...\"",
                    "pada elemen itu - kosong kalau kamu tidak memakainya. Mengetik di",
                    "dalamnya sama saja dengan menulis atribut style= di elemen itu,",
                    "jadi apa pun yang kamu taruh di situ mengalahkan semua pemilih",
                    "(materi 2). Berguna untuk mencoba cepat, tapi jangan ditiru ke",
                    "berkas .css-mu.",
                    "",
                    "Kalau digulir jauh ke bawah ada bagian 'Inherited from body' dan",
                    "seterusnya: properti yang tidak ditulis untuk elemen ini tapi",
                    "DIWARISKAN dari induknya (lihat materi Teks dan Font). Warna teks",
                    "atau font yang berubah tanpa aturan yang kelihatan hampir selalu",
                    "ketemu di bagian itu.",
                ],
            },
            {
                "body": [
                    "PANEL COMPUTED: HASIL AKHIRNYA",
                    "",
                    "Styles menunjukkan PERTARUNGANnya. Computed menunjukkan HASILnya:",
                    "daftar seluruh properti elemen terpilih, masing-masing dengan satu",
                    "nilai saja - nilai yang benar-benar dipakai browser untuk menggambar,",
                    "sesudah cascade, pewarisan, dan nilai bawaan diperhitungkan.",
                    "",
                    "Dua hal yang membuatnya layak dibuka tiap hari:",
                    "",
                    "  - Ada kotak Filter di atasnya. Ketik 'background' dan tinggal",
                    "    properti itu yang tersisa dari ratusan baris.",
                    "  - Buka segitiga kecil di kiri sebuah properti: DevTools",
                    "    menampilkan dari aturan MANA nilai itu datang, lengkap dengan",
                    "    tautan ke barisnya. Itu jawaban langsung dan tanpa perantara",
                    "    untuk 'jadi warnanya diambil dari mana'.",
                    "",
                    "Nilai di Computed sudah dihitung, jadi bentuknya sering berbeda dari",
                    "yang kamu ketik: 1em muncul sebagai 16px, red sebagai",
                    "rgb(255, 0, 0), dan lebar 50% sebagai angka piksel. Itu bukan",
                    "kesalahan - itu memang angka yang dipakai menggambar. Sekaligus ini",
                    "cara termudah menjawab 'jadi 2rem itu berapa piksel di sini'.",
                    "",
                    "DIAGRAM BOX MODEL: 'KOTAK SAYA SEBESAR APA'",
                    "",
                    "Di paling atas panel Computed ada gambar kotak berlapis, persis",
                    "diagram di materi Box Model tapi berisi ANGKA SUNGGUHAN elemen yang",
                    "sedang terpilih:",
                    "",
                    "  jingga   margin     paling luar",
                    "  kuning   border     kuning kecokelatan",
                    "  hijau    padding",
                    "  biru     content    tertulis sebagai lebar x tinggi",
                    "",
                    "Untuk tombol di contoh tadi kamu akan melihat margin 8 di keempat",
                    "sisi, border 2, dan padding 12 di atas-bawah serta 20 di kiri-kanan.",
                    "Angka nol ditampilkan sebagai tanda hubung, bukan angka 0.",
                    "",
                    "Geser kursor ke salah satu lapis: lapis itu menyala di halaman",
                    "dengan warna yang sama. Sekali melihatnya, urusan 'margin di luar,",
                    "padding di dalam' selesai selamanya - kamu tidak sedang menghafal",
                    "gambar di buku, kamu sedang menunjuk kotaknya sendiri.",
                    "",
                    "Di sinilah selisih lebar yang bikin pusing itu kelihatan tanpa perlu",
                    "menjumlahkan 2 + 20 + 200 + 20 + 2 di kepala. Kalau kamu menulis",
                    "width: 200px lalu lapis content tetap tertulis 200 sementara",
                    "kotaknya jelas memakan tempat lebih lebar dari itu di halaman, kamu",
                    "baru saja melihat sendiri kenapa box-sizing: border-box ada.",
                ],
            },
            {
                "body": [
                    "MEMAKSA KEADAAN: TOMBOL :hov DAN .cls",
                    "",
                    ":hover mustahil ditata dengan tenang: begitu kursor pindah ke panel",
                    "DevTools untuk membaca aturannya, hover-nya lepas dan tampilan",
                    "kembali seperti semula.",
                    "",
                    "Di sudut kanan atas panel Styles ada tombol :hov. Klik, dan muncul",
                    "daftar centang - :hover, :active, :focus, :focus-within, dan",
                    ":focus-visible.",
                    "Centang :hover, dan elemen terpilih DIPAKSA berada dalam keadaan itu",
                    "sampai kamu mematikannya lagi; kursormu bebas ke mana saja. Elemen",
                    "yang sedang dipaksa diberi titik kecil di pohon Elements supaya kamu",
                    "ingat mematikannya.",
                    "",
                    "Coba pada tombol hijau: centang :hover, dan .tombol:hover naik ke",
                    "atas sementara background .panel .tombol ikut tercoret. Keduanya",
                    "bernilai (0,2,0), jadi yang ditulis belakangan menang - bukti bahwa",
                    "pseudo-class ikut dihitung dalam spesifisitas (materi 2, dan materi",
                    "Pseudo-class dan Pseudo-element).",
                    "",
                    "Di sebelahnya ada tombol .cls: sebuah kotak isian untuk menambah",
                    "class ke elemen terpilih, plus daftar centang class yang sudah",
                    "menempel padanya. Hilangkan centang 'bahaya' di tombol merah dan ia",
                    "langsung kembali biru, tanpa menyentuh berkas HTML sama sekali.",
                    "Inilah cara paling cepat menjawab 'aturan ini kena atau tidak kalau",
                    "class-nya dipasang'.",
                    "",
                    "MENYUNTING LANGSUNG - DAN KENAPA SEMUANYA HILANG",
                    "",
                    "Hampir semua yang terlihat di panel Styles bisa diklik lalu diketik",
                    "ulang:",
                    "  - Klik nilainya, ketik yang baru, tekan Enter. Tab memindahkanmu",
                    "    ke deklarasi berikutnya.",
                    "  - Klik nama propertinya untuk menggantinya; klik pemilihnya untuk",
                    "    mengubah pemilihnya.",
                    "  - Tanda + di sudut panel membuat aturan baru dari nol.",
                    "  - Taruh kursor di atas sebuah ANGKA lalu tekan panah atas/bawah:",
                    "    naik atau turun satu. Shift+panah melompat sepuluh, Alt+panah",
                    "    bergerak nol koma satu. Mencari padding yang pas dengan cara ini",
                    "    jauh lebih cepat daripada ketik-simpan-muat ulang berkali-kali,",
                    "    karena halamannya berubah tepat saat angkanya berubah.",
                    "",
                    "Lalu bagian yang wajib diingat: SEMUA SUNTINGAN ITU HILANG BEGITU",
                    "HALAMAN DIMUAT ULANG. DevTools menyunting salinan yang ada di memori",
                    "browser, bukan berkas .css di komputermu. Tidak ada peringatan,",
                    "tidak ada tawaran menyimpan, tidak ada Ctrl+Z yang menolongmu.",
                    "",
                    "Sudah banyak orang menghabiskan setengah jam menyetel tampilan di",
                    "DevTools, lalu menekan F5 karena kebiasaan, dan kehilangan semuanya.",
                    "Biasakan satu hal: begitu sebuah nilai terasa pas, SALIN saat itu",
                    "juga ke berkas .css-mu. DevTools untuk mencoba, berkas .css untuk",
                    "menyimpan.",
                    "",
                    "Kebalikannya juga menjebak: kamu sudah menyimpan berkasnya, muat",
                    "ulang, dan halaman tetap memakai gaya yang lama - browser menyajikan",
                    "salinan yang ia simpan sendiri (cache, lihat materi 1). Muat ulang",
                    "paksa dengan Ctrl+Shift+R sebelum menuduh CSS-mu salah.",
                    "",
                    "DEVTOOLS DAN TOMBOL JALANKAN DI APLIKASI INI",
                    "",
                    "Dua alat, dua pertanyaan berbeda, dan kamu butuh keduanya:",
                    "",
                    "  Jalankan   'Apakah CSS-ku terbaca?' Berkasmu diurai jadi daftar",
                    "             aturan. Yang tidak muncul di daftar itu juga tidak akan",
                    "             dilihat browser - salah ketik dan kurawal yang lupa",
                    "             ditutup ketahuan di sini, tanpa perlu membuka apa pun.",
                    "",
                    "  DevTools   'Aturan mana yang menang di halaman sungguhan?' Ini",
                    "             butuh HTML, browser, dan elemen betulan, jadi cuma",
                    "             browser yang sanggup menjawabnya.",
                    "",
                    "Daftar periksa 'saat sebuah aturan tidak bekerja' di materi Variabel",
                    "CSS dan Cara Menata Berkas Gaya tetap berlaku seluruhnya. Yang",
                    "berubah cuma satu, dan itu perubahan besar: sesudah materi ini,",
                    "sebagian besar langkahnya tidak lagi kamu tebak - kamu lihat.",
                ],
            },
        ],
    },
    {
        "title": "4. Warna dan Satuan",
        "sections": [
            {
                "body": [
                    "Empat cara menulis warna. Semuanya sah; pilih sesuai keperluan.",
                    "",
                    "  color: red;                  nama warna (ada 147 nama baku)",
                    "  color: #cc0000;              hex: #RRGGBB, tiap pasang 00-ff",
                    "  color: #c00;                 hex singkat, sama dengan #cc0000",
                    "  color: rgb(204 0 0);         merah, hijau, biru: 0-255",
                    "  color: rgb(204 0 0 / 50%);   dengan tingkat tembus pandang",
                    "  color: hsl(0 100% 40%);      hue, saturation, lightness",
                    "",
                    "Hex adalah bilangan basis 16: 0-9 lalu a-f. #ff0000 berarti merah",
                    "penuh, hijau nol, biru nol. #000000 hitam, #ffffff putih.",
                    "Bentuk singkat #c00 berarti tiap huruf digandakan: #cc0000.",
                    "",
                    "hsl() paling mudah dipikirkan manusia:",
                    "  hue        0-360 derajat roda warna (0 merah, 120 hijau, 240 biru)",
                    "  saturation 0% abu-abu, 100% pekat",
                    "  lightness  0% hitam, 50% warna murni, 100% putih",
                    "",
                    "Untuk membuat versi lebih terang dari satu warna, ubah angka",
                    "ketiganya saja:",
                    "  hsl(210 90% 45%)  ->  hsl(210 90% 65%)",
                    "Dengan hex kamu harus menghitung ulang tiga pasang angka dan",
                    "hasilnya sering meleset warnanya.",
                    "",
                    "BENTUK BERKOMA - inilah yang akan lebih sering kamu lihat di",
                    "kode orang lain:",
                    "",
                    "  color: rgb(204, 0, 0);            sama persis dengan rgb(204 0 0)",
                    "  color: rgba(0, 0, 0, 0.5);        hitam, setengah tembus pandang",
                    "  color: hsl(0, 100%, 40%);         sama persis dengan hsl(0 100% 40%)",
                    "  color: hsla(0, 100%, 40%, 0.5);   dengan tembus pandang",
                    "",
                    "Huruf 'a' di rgba dan hsla berarti ALPHA: tingkat kepekatan,",
                    "ditulis 0 sampai 1. Nilai 0 tembus pandang penuh, 1 pekat penuh.",
                    "Jadi rgba(0, 0, 0, 0.5) adalah hitam setengah pekat.",
                    "",
                    "Bentuk tanpa koma di daftar atas lebih baru dan lebih enak",
                    "ditulis, tapi bentuk berkoma inilah yang mendominasi kode nyata -",
                    "berkas gaya orang lain hampir pasti memakainya. Keduanya sah dan",
                    "hasilnya sama persis, jadi kenali keduanya dan tulis yang mana",
                    "pun kamu suka.",
                    "",
                    "Alpha bukan opacity. Alpha membuat SATU WARNA itu saja tembus",
                    "pandang; opacity membuat elemennya BESERTA SELURUH ISINYA tembus",
                    "pandang, sampai ke teks di atasnya.",
                    "",
                    "Dua nilai khusus yang sering berguna:",
                    "  transparent    tembus pandang sepenuhnya",
                    "  currentColor   nilai color elemen itu sendiri",
                    "     border: 1px solid currentColor;  -> garis ikut warna teks",
                ]
            },
            {
                "body": [
                    "SATUAN UKURAN",
                    "",
                    "Mutlak:",
                    "  px   piksel. Tetap. Tidak ikut membesar kalau pembaca menaikkan",
                    "       ukuran huruf bawaan di pengaturan browsernya.",
                    "",
                    "Relatif:",
                    "  %    relatif terhadap ukuran induknya",
                    "  em   relatif terhadap font-size ELEMEN ITU SENDIRI",
                    "  rem  relatif terhadap font-size <html> (root em)",
                    "  ch   selebar karakter '0' pada font yang sedang dipakai",
                    "  vw   1% lebar jendela      vh   1% tinggi jendela",
                    "  fr   satu bagian sisa ruang (khusus grid, materi 8)",
                    "",
                    "JEBAKAN em YANG PALING SERING MENGGIGIT:",
                    "",
                    "  em menumpuk. Kalau .luar { font-size: 1.5em } dan di dalamnya",
                    "  ada .dalam { font-size: 1.5em }, hasilnya 1,5 x 1,5 = 2,25 kali",
                    "  ukuran asal. Tiga tingkat bersarang jadi 3,4 kali. Tidak ada",
                    "  yang meminta itu, dan penyebabnya sulit ditemukan karena tiap",
                    "  aturannya sendiri terlihat wajar.",
                    "",
                    "  rem tidak menumpuk karena selalu diukur ke <html>. Untuk UKURAN",
                    "  HURUF pakai rem. Sisakan em untuk jarak yang MEMANG harus ikut",
                    "  ukuran huruf elemennya sendiri - padding tombol misalnya, supaya",
                    "  tombol besar otomatis punya padding lebih lega.",
                    "",
                    "line-height sebaiknya ditulis TANPA satuan:",
                    "  line-height: 1.5;    benar. Tiap elemen menghitung dari ukuran",
                    "                       hurufnya masing-masing.",
                    "  line-height: 24px;   kaku. Anak yang hurufnya 30px tetap dapat",
                    "                       jarak baris 24px, jadi barisnya bertumpuk.",
                    "  line-height: 1.5em;  menipu. Yang diwariskan ke anak adalah",
                    "                       HASILnya, bukan rumusnya - sama kakunya.",
                ]
            },
            {
                "heading": "Warna dan satuan dipakai bersama",
                "body": [
                    "Baris pertama contoh ini memakai :root, dan itu bukan pemilih",
                    "ajaib. :root adalah elemen <html> - pemilih biasa seperti yang",
                    "kamu pelajari di materi 2, hanya saja ia selalu cocok tepat satu",
                    "kali, dengan elemen paling luar. Menaruh sesuatu di situ berarti",
                    "seluruh halaman ikut kena. Kegunaan utamanya dijelaskan penuh di",
                    "materi Variabel CSS dan Cara Menata Berkas Gaya.",
                ],
                "code": """:root {
  font-size: 16px;
}

body {
  background: #fdfdfb;
  color: hsl(220 15% 20%);
  line-height: 1.6;
}

h1 {
  font-size: 2rem;              /* 2 x 16px = 32px */
  color: hsl(220 60% 35%);
}

.catatan {
  font-size: 0.875rem;          /* 14px */
  color: rgb(0 0 0 / 60%);
  border-left: 4px solid hsl(40 90% 55%);
  padding-left: 1em;            /* ikut ukuran huruf .catatan sendiri */
}

.lebar-baca {
  max-width: 65ch;              /* sekitar 65 huruf per baris */
}

.tombol {
  padding: 0.6em 1.2em;         /* melar sendiri kalau hurufnya diperbesar */
  border: 1px solid currentColor;
  background: transparent;
}""",
            },
            {
                "body": [
                    "SOAL KONTRAS - ini penting kalau kamu membaca berjam-jam.",
                    "",
                    "Teks abu muda di atas putih terlihat elegan di gambar promosi,",
                    "tapi menyiksa mata pada jam kesekian. Ukurannya disebut rasio",
                    "kontras, dan batas yang dianggap aman untuk teks isi adalah 4,5:1.",
                    "",
                    "  #999999 di atas putih  -> sekitar 2,8:1. Di bawah batas.",
                    "  #767676 di atas putih  -> tepat di sekitar 4,5:1.",
                    "  #595959 di atas putih  -> sekitar 7:1. Nyaman.",
                    "",
                    "Untuk membaca lama, jangan pakai hitam pekat di atas putih pekat",
                    "juga. Selisih yang terlalu tajam bikin huruf seperti bergetar.",
                    "Pasangan yang enak biasanya latar sedikit hangat (#fdfdfb) dengan",
                    "teks abu sangat gelap (#23252b), bukan #ffffff dengan #000000.",
                    "",
                    "Untuk tema gelap berlaku hal yang sama terbalik: teks putih pekat",
                    "di atas hitam pekat menyilaukan. Turunkan keduanya sedikit.",
                ]
            },
        ],
    },
    {
        "title": "5. Satuan Lanjut dan Menghitung di Dalam CSS",
        "sections": [
            {
                "body": [
                    "Ada satu hal yang tidak bisa ditulis dengan satuan mana pun yang sudah",
                    "kamu pelajari: 'seluruh lebar, dikurangi panel selebar 240px'.",
                    "",
                    "Persentase selalu diukur ke SATU hal saja - ukuran induknya - dan ia",
                    "tidak tahu apa-apa soal panel 240px di sebelahnya. px sebaliknya tidak",
                    "tahu berapa lebar layar orang. Keduanya benar sendiri-sendiri, dan",
                    "tidak ada satu nilai pun yang bisa menyatakan hubungan di antaranya.",
                    "",
                    "calc() ada untuk itu: menulis HITUNGAN sebagai nilai.",
                    "",
                    "  .isi { width: calc(100% - 240px); }",
                    "",
                    "Browser yang mengerjakan hitungannya, dan ia menghitung ulang setiap",
                    "kali jendelanya berubah ukuran.",
                    "",
                    "YANG BOLEH DICAMPUR DI DALAMNYA - ini kekuatan sebenarnya:",
                    "",
                    "  calc(100vh - 64px)      tinggi jendela dikurangi bilah atas",
                    "  calc(50% + 1rem)        setengah induk, lebih satu baris huruf",
                    "  calc(100% / 3 - 20px)   sepertiga, jaraknya sudah dipotong",
                    "  calc(2rem + 5vw)        ikut lebar layar, tapi punya dasar tetap",
                    "",
                    "%, px, rem, dan vh diukur terhadap hal yang berbeda-beda, dan calc()",
                    "satu-satunya tempat mereka boleh bertemu dalam satu nilai.",
                    "",
                    "ATURAN EJAAN YANG PALING SERING MENGGIGIT: SPASI",
                    "",
                    "  calc(100% - 20px)   BENAR",
                    "  calc(100%-20px)     DIBUANG. Tanpa pesan, tanpa tanda apa pun.",
                    "  calc(100% -20px)    dibuang juga - spasinya harus di KEDUA sisi.",
                    "",
                    "Spasi di kiri dan kanan tanda + dan - itu WAJIB, bukan soal kerapian.",
                    "Di CSS, tanda minus sah menjadi BAGIAN dari sebuah nilai: -20px itu",
                    "satu angka negatif yang utuh, dan --lebar itu sebuah nama variabel.",
                    "Kalau ditulis rapat, browser tidak punya cara membedakan 'kurangi dua",
                    "puluh piksel' dari 'satu nilai aneh bernama 100%-20px'. Spasi itulah",
                    "yang memberi tahu mana yang kamu maksud.",
                    "",
                    "Akibat salahnya khas CSS: seluruh deklarasi dibuang diam-diam dan",
                    "lebarnya kembali ke bawaan. Yang terlihat cuma 'calc-nya tidak jalan'.",
                    "Jadi kalau sebuah calc tidak berpengaruh, periksa spasinya lebih dulu,",
                    "sebelum mencurigai apa pun yang lain.",
                    "",
                    "Tanda * dan / tidak menuntut spasi, tapi tulis saja supaya seragam.",
                    "Pengali dan pembaginya harus angka POLOS: calc(100% / 3) sah, sedangkan",
                    "calc(100% / 3px) tidak berarti apa-apa dan ikut dibuang.",
                    "",
                    "BENTUK YANG PALING SERING KAMU TEMUI DI KODE ORANG",
                    "",
                    "  padding: calc(var(--s4) * 2);",
                    "  width: calc(100% - var(--lebar-panel));",
                    "",
                    "Variabel CSS - nama berawalan dua minus itu - punya materinya sendiri,",
                    "'Variabel CSS dan Cara Menata Berkas Gaya'. Yang perlu diketahui",
                    "sekarang cuma satu: var() diganti isinya LEBIH DULU, baru hitungannya",
                    "dikerjakan. Kalau --s4 bernilai 16px, baris pertama di atas benar-benar",
                    "berarti calc(16px * 2).",
                    "",
                    "Sisi menjebaknya ada di situ juga: kalau nama variabelnya salah ketik",
                    "atau belum pernah didefinisikan, yang masuk ke dalam calc() adalah",
                    "kekosongan - dan yang gugur seluruh deklarasinya, bukan cuma bagian itu.",
                ],
            },
            {
                "body": [
                    "min(), max(), dan clamp() satu keluarga dengan calc(): sama-sama",
                    "menghitung, sama-sama boleh mencampur satuan, dan tunduk pada aturan",
                    "spasi yang sama persis.",
                    "",
                    "MIN() DAN MAX() TERASA TERBALIK PADA MULANYA.",
                    "",
                    "  width: min(100%, 720px);",
                    "",
                    "Dibaca: 'yang mana pun lebih KECIL saat itu'. Di layar lebar, 720px",
                    "yang lebih kecil, jadi itu yang dipakai. Di layar 400px, 100% yang",
                    "lebih kecil. Hasil akhirnya lebar maksimum 720px yang ikut menyusut",
                    "sendiri di layar sempit.",
                    "",
                    "Jadi min() memasang LANGIT-LANGIT, dan max() memasang LANTAI:",
                    "",
                    "  font-size: max(1rem, 2vw);   tidak pernah lebih kecil dari 1rem",
                    "",
                    "Terasa terbalik karena nama fungsinya menyebut CARA MEMILIHNYA, bukan",
                    "akibatnya. Sesuatu yang selalu memilih yang terkecil memang tidak akan",
                    "pernah melewati batas atasnya.",
                    "",
                    "clamp() menggabung keduanya jadi satu tulisan:",
                    "",
                    "  font-size: clamp(1.5rem, 4vw, 2.5rem);",
                    "                   ^batas  ^nilai ^batas",
                    "                    bawah   ideal  atas",
                    "",
                    "Artinya sama persis dengan max(1.5rem, min(4vw, 2.5rem)), cuma jauh",
                    "lebih enak dibaca: nilai tengahnya yang dipakai, selama ia masih",
                    "berada di antara kedua batas itu.",
                    "",
                    "Ketiganya sudah berupa hitungan, jadi ARITMATIKA BOLEH DITULIS",
                    "LANGSUNG di dalamnya tanpa menyebut calc() lagi:",
                    "",
                    "  width: min(100% - 2rem, 60ch);",
                    "  font-size: clamp(1rem, 0.9rem + 0.6vw, 1.4rem);",
                    "",
                    "DUA JEBAKAN clamp():",
                    "",
                    "  1. Kalau batas bawahnya ternyata LEBIH BESAR dari batas atasnya,",
                    "     batas bawah yang menang. Tidak ada pesan error; ukurannya cuma",
                    "     terkunci di satu angka dan tidak pernah berubah lagi.",
                    "",
                    "  2. Nilai ideal yang murni vw - clamp(1rem, 4vw, 2rem) - membuat",
                    "     ukuran huruf berhenti menanggapi setelan 'perbesar teks' di",
                    "     browser pembacanya. Untuk orang yang memang perlu huruf besar,",
                    "     halamanmu jadi tidak bisa dibesarkan sama sekali. Campurkan rem",
                    "     supaya setelan itu tetap berpengaruh:",
                    "       clamp(1rem, 0.9rem + 0.6vw, 1.4rem)",
                    "",
                    "Ketiganya akan muncul lagi di materi media query, dan di situ gunanya",
                    "terlihat penuh: banyak hal yang dulu butuh @media sekarang selesai",
                    "dengan satu baris min() atau clamp().",
                ],
            },
            {
                "body": [
                    "DUA KELUARGA SATUAN YANG BELUM PERNAH DISEBUT SAMA SEKALI",
                    "",
                    "SATUAN WAKTU: s DAN ms",
                    "",
                    "  s    detik            ms   milidetik, seperseribu detik",
                    "",
                    "1s = 1000ms, jadi 0.2s dan 200ms sama persis. Pilih satu gaya penulisan",
                    "lalu pakai terus di seluruh berkas - dua gaya bercampur membuat angka",
                    "yang mirip terlihat berbeda jauh.",
                    "",
                    "Cuma dua properti yang memakainya: transition dan animation, beserta",
                    "turunannya (transition-duration, transition-delay, animation-duration).",
                    "Keduanya punya materinya sendiri nanti; yang dibahas di sini satuannya.",
                    "",
                    "  .tombol { transition: background 0.2s; }",
                    "",
                    "JEBAKANNYA: ANGKA TANPA SATUAN TIDAK SAH DI SINI.",
                    "",
                    "  transition: background 0.2;   dibuang. Tidak ada transisi apa pun.",
                    "  transition-duration: 0;       dibuang juga.",
                    "  transition-duration: 0s;      benar.",
                    "",
                    "Ini pengecualian yang sungguh menjebak, karena untuk PANJANG angka nol",
                    "memang boleh polos - margin: 0 sah sepenuhnya. Untuk waktu tidak. Nol",
                    "pun harus bersatuan.",
                    "",
                    "SATUAN SUDUT: deg, turn, DAN rad",
                    "",
                    "  deg    derajat. 360deg satu putaran penuh.",
                    "  turn   putaran. 1turn = 360deg; 0.5turn setengah putaran.",
                    "  rad    radian.  1turn = 6.2832rad, yaitu 2 x pi.",
                    "",
                    "Ketiganya boleh dipakai di tempat yang sama. deg paling lazim; turn",
                    "paling enak dibaca kalau yang kamu maksud memang 'setengah putaran'.",
                    "",
                    "Yang memakainya:",
                    "",
                    "  transform: rotate(45deg);       memutar elemen",
                    "  transform: rotate(-90deg);      minus = berlawanan arah jarum jam",
                    "  linear-gradient(180deg, ...)    arah gradiennya",
                    "  hsl(220deg 60% 35%)             hue memang sebuah sudut, jadi 220",
                    "                                  dan 220deg sama saja artinya",
                    "",
                    "Sama seperti waktu, ANGKA POLOS DIBUANG: rotate(45) tidak memutar apa",
                    "pun. Dan karena satu nilai rusak menggugurkan seluruh deklarasi, fungsi",
                    "transform lain di baris yang sama ikut lenyap bersamanya.",
                ],
            },
            {
                "body": [
                    "SATUAN VIEWPORT, LENGKAP",
                    "",
                    "Viewport adalah bidang tempat halaman digambar. Di ponsel itu bukan",
                    "seluruh layar, melainkan bagian yang tersisa untuk halamanmu.",
                    "",
                    "  vw     1% LEBAR viewport",
                    "  vh     1% TINGGI viewport",
                    "  vmin   1% dari sisi yang lebih PENDEK",
                    "  vmax   1% dari sisi yang lebih PANJANG",
                    "",
                    "vmin jarang diajarkan tapi rapi sekali untuk sesuatu yang harus selalu",
                    "muat utuh: width: 80vmin; height: 80vmin; menghasilkan bujur sangkar",
                    "yang tetap muat di layar tegak maupun melintang, tanpa satu pun media",
                    "query.",
                    "",
                    "JEBAKAN 100vw: IA IKUT MENGHITUNG BILAH GULIR.",
                    "",
                    "Di komputer, bilah gulir vertikal memakan sekitar 15px, dan 100vw tetap",
                    "berarti lebar penuh TERMASUK bilah itu. Elemen selebar 100vw di halaman",
                    "yang bisa digulir jadi lebih lebar daripada ruang yang sebenarnya ada,",
                    "dan seluruh halaman mendadak bisa digeser ke samping. Untuk 'selebar",
                    "induknya', pakai width: 100%, bukan 100vw.",
                    "",
                    "JEBAKAN 100vh DI PONSEL - INI YANG PALING TERKENAL DARI SEMUANYA.",
                    "",
                    "min-height: 100vh terdengar seperti 'setinggi layar'. Di komputer",
                    "memang begitu. Di ponsel tidak.",
                    "",
                    "Bilah alamat browser ponsel menciut saat halaman digulir ke bawah, lalu",
                    "muncul lagi saat digulir ke atas. Tingginya berubah-ubah, jadi 'tinggi",
                    "layar' sebenarnya bukan satu angka. Yang dipilih browser untuk vh",
                    "adalah tinggi saat bilah alamat SEDANG SEMBUNYI - yang paling besar.",
                    "",
                    "Akibatnya: saat halaman baru dibuka dan bilah alamat masih terlihat,",
                    "kotak setinggi 100vh lebih tinggi daripada ruang yang sungguh tersedia.",
                    "Bagian bawahnya - yang biasanya justru tombol utamanya - berada di luar",
                    "layar sampai orang menggulir. Di komputermu tidak ada gejalanya sama",
                    "sekali, dan itulah sebabnya bug ini bisa bertahan berbulan-bulan.",
                    "",
                    "TIGA SATUAN BARU YANG MENJAWAB PERSOALAN ITU:",
                    "",
                    "  svh   small    tinggi saat bilah browser TERLIHAT (paling kecil)",
                    "  lvh   large    tinggi saat bilah SEMBUNYI - inilah arti vh selama ini",
                    "  dvh   dynamic  mengikuti keadaan saat itu, berubah sambil digulir",
                    "",
                    "Karena itu kode yang ditulis belakangan memakai 100dvh untuk 'setinggi",
                    "layar'. Kalau tinggi yang berubah-ubah justru mengganggu - isinya",
                    "terlihat melompat saat digulir - pakai 100svh: ia selalu memilih yang",
                    "paling kecil, jadi tidak akan pernah ada bagian yang tertutup.",
                    "",
                    "Semuanya punya sekeluarga penuh: dvw, svw, lvw, dvmin, dan seterusnya.",
                    "Yang benar-benar sering dipakai cuma dvh dan svh.",
                    "",
                    "CARA MENULISNYA SUPAYA BROWSER LAMA TETAP KEBAGIAN:",
                    "",
                    "  min-height: 100vh;",
                    "  min-height: 100dvh;",
                    "",
                    "Dua baris berurutan, properti yang sama. Browser yang tidak mengenal",
                    "dvh membuang baris kedua tanpa bilang apa-apa dan tetap memakai yang",
                    "pertama; yang mengenalnya memakai baris terakhir, karena dua aturan",
                    "setara dimenangkan oleh yang ditulis belakangan. Untuk sekali ini,",
                    "kebiasaan CSS membuang yang tidak dimengerti justru menyelamatkan -",
                    "dan begitulah cara hampir semua fitur baru dipasang dengan aman.",
                ],
            },
            {
                "heading": "Kerangka halaman yang memakai semuanya",
                "body": [
                    "Di berkas gaya berikut semua yang tadi dibahas bertemu. Yang perlu",
                    "diperhatikan:",
                    "",
                    "  - .badan memakai calc(100dvh - var(--tinggi-kepala)), jadi sisanya",
                    "    persis mengisi layar di bawah bilah atas - tidak lebih, tidak",
                    "    kurang, di ponsel maupun di komputer.",
                    "  - .isi memakai calc(100% - var(--lebar-panel)). Tidak ada persentase",
                    "    tunggal yang bisa menyatakan itu.",
                    "  - Judulnya ber-clamp, jadi ukuran hurufnya tidak butuh satu pun",
                    "    media query.",
                    "  - Semua angka kerangkanya tinggal di :root. Mengubah lebar panel",
                    "    cukup di satu tempat dan semua hitungan ikut menyesuaikan.",
                    "",
                    "display: flex, :hover, transition, dan rotate() punya materinya",
                    "masing-masing nanti; di sini keempatnya cuma tempat satuannya dipakai.",
                ],
                "code": """/* Satu-satunya tempat angka kerangkanya ditulis */
:root {
  --tinggi-kepala: 64px;
  --lebar-panel: 240px;
  --s4: 16px;
  --jeda: 0.2s;
}

*, *::before, *::after {
  box-sizing: border-box;
}

body {
  margin: 0;
  font-family: system-ui, sans-serif;
  line-height: 1.6;
  color: #23252b;
  background: #fdfdfb;
}

/* Bilah atas setinggi tetap */
.kepala {
  height: var(--tinggi-kepala);
  padding: 0 var(--s4);
  background: #1a4fa0;
  color: white;
}

/* Sisa layar sesudah bilah atas.
   Dua baris: browser lama berhenti di yang pertama. */
.badan {
  display: flex;
  min-height: calc(100vh - var(--tinggi-kepala));
  min-height: calc(100dvh - var(--tinggi-kepala));
}

/* Panel selebar tetap: tidak ikut melar, tidak ikut menyusut */
.sisi {
  flex: 0 0 var(--lebar-panel);
  padding: var(--s4);
  background: #f2f3f5;
}

/* Sisa lebarnya. Perhatikan spasi di kiri-kanan tanda minus. */
.isi {
  width: calc(100% - var(--lebar-panel));
  min-width: 0;
  padding: calc(var(--s4) * 2);
}

/* Ikut lebar layar, tapi punya lantai dan langit-langit */
.isi h1 {
  font-size: clamp(1.5rem, 1.2rem + 1.6vw, 2.5rem);
  margin: 0 0 var(--s4);
}

/* Kolom baca tidak pernah melewati ruang yang tersedia */
.isi p {
  max-width: min(65ch, 100%);
}

/* Bujur sangkar yang muat di layar tegak maupun melintang */
.pratinjau {
  width: 80vmin;
  height: 80vmin;
  max-width: 100%;
  margin: var(--s4) auto;
  background: #dde3ee;
  border-radius: 8px;
}

.tombol {
  padding: 0.6em 1.2em;
  border: 1px solid #1a4fa0;
  border-radius: 6px;
  background: white;
  transition: background var(--jeda);
}

.tombol:hover {
  background: #eaf0fb;
}

/* Setengah putaran, ditulis dengan satuan sudut */
.panah {
  display: inline-block;
  transition: transform var(--jeda);
}

.menu-terbuka .panah {
  transform: rotate(0.5turn);
}

/* Di layar sempit panelnya turun ke bawah,
   jadi tidak ada lagi yang perlu dikurangi */
@media (max-width: 720px) {
  .badan {
    display: block;
  }

  .sisi,
  .isi {
    width: 100%;
  }
}""",
            },
        ],
    },
    {
        "title": "6. Teks dan Font",
        "sections": [
            {
                "body": [
                    "font-family ditulis sebagai DAFTAR CADANGAN, dipisah koma:",
                    "",
                    "  font-family: \"Segoe UI\", Roboto, Helvetica, Arial, sans-serif;",
                    "",
                    "Browser mencoba dari kiri. Yang pertama tersedia di komputer",
                    "pembaca itulah yang dipakai. Nama yang mengandung spasi dibungkus",
                    "petik ganda.",
                    "",
                    "Nama terakhir wajib berupa KELUARGA UMUM, supaya selalu ada yang",
                    "cocok betapapun aneh komputernya:",
                    "  serif        berkait, seperti Times    (enak untuk teks panjang)",
                    "  sans-serif   tanpa kait, seperti Arial (paling umum untuk layar)",
                    "  monospace    tiap huruf selebar sama   (kode)",
                    "  system-ui    huruf bawaan sistem operasi pembacanya",
                    "",
                    "Kenapa daftar cadangan itu wajib: font yang terpasang di",
                    "komputermu belum tentu ada di komputer orang lain. Tanpa cadangan,",
                    "browser memilih sendiri - biasanya Times - dan tata letak yang",
                    "kamu susun rapi bisa berantakan karena lebar hurufnya berbeda.",
                    "",
                    "Properti teks yang paling sering dipakai:",
                    "  font-size: 1rem;",
                    "  font-weight: 400;         100-900; 400 normal, 700 tebal",
                    "  font-style: italic;",
                    "  line-height: 1.6;         jarak antar baris",
                    "  letter-spacing: 0.02em;   jarak antar huruf",
                    "  text-align: left | center | right | justify;",
                    "  text-decoration: underline | none;",
                    "  text-transform: uppercase | lowercase | capitalize;",
                    "  white-space: nowrap;      larang teks turun baris",
                ]
            },
            {
                "body": [
                    "PEWARISAN (INHERITANCE)",
                    "",
                    "Inilah yang membuat CSS bisa ditulis sedikit tapi berpengaruh",
                    "banyak. Sebagian properti otomatis menular ke seluruh keturunan",
                    "sebuah elemen, sebagian tidak.",
                    "",
                    "  Menular (properti TEKS):",
                    "    color, font-family, font-size, font-weight, font-style,",
                    "    line-height, text-align, letter-spacing, list-style",
                    "",
                    "  Tidak menular (properti KOTAK):",
                    "    margin, padding, border, background, width, height, display",
                    "",
                    "Jadi menulis font-family sekali di body sudah mengubah seluruh",
                    "halaman, sedangkan border di body tidak menular ke satu pun",
                    "anaknya. Aturannya masuk akal kalau dipikir: 'huruf yang sama'",
                    "memang biasanya diinginkan menurun, 'garis tepi yang sama' tidak.",
                    "",
                    "Empat kata kunci yang berlaku di properti apa pun:",
                    "  inherit   paksa ambil nilai induk (berguna untuk yang tidak",
                    "            menular secara bawaan)",
                    "  initial   kembalikan ke nilai bawaan CSS",
                    "  unset     gabungan keduanya: inherit kalau propertinya",
                    "            menular, initial kalau tidak",
                    "  revert    kembalikan ke gaya bawaan BROWSER, yaitu user agent",
                    "            stylesheet dari materi 1",
                    "",
                    "Beda initial dan revert halus tapi nyata. initial kembali ke",
                    "bawaan SPESIFIKASI, dan bawaan spesifikasi untuk display adalah",
                    "inline - jadi div { display: initial } diam-diam membuat div itu",
                    "inline, hampir pasti bukan yang kamu mau. revert kembali ke",
                    "bawaan BROWSER, yang untuk div memang block. Kalau maksudmu",
                    "'batalkan gayaku, kembalikan seperti semula', yang kamu cari",
                    "revert.",
                    "",
                    "Ada satu properti bernama all yang berarti 'semua properti",
                    "sekaligus'. Nilainya cuma boleh keempat kata kunci di atas, dan",
                    "dua di antaranya sering dipakai:",
                    "",
                    "  .polos  { all: unset; }    telanjangi habis, lalu tata ulang",
                    "  .semula { all: revert; }   kembalikan ke rupa bawaan browser",
                    "",
                    "all: unset adalah cara baku menelanjangi <button> sebelum",
                    "menatanya jadi sesuatu yang lain: latar abu, garis tepi, dan",
                    "padding bawaannya hilang sekaligus tanpa perlu didaftar satu per",
                    "satu. Yang tersisa cuma sifatnya - ia tetap bisa diklik dan tetap",
                    "bisa dicapai dengan Tab. Hati-hati satu hal: penanda fokusnya",
                    "ikut terhapus, jadi kamu wajib menggantinya sendiri (caranya di",
                    "materi Pseudo-class dan Pseudo-element).",
                    "",
                    "KASUS PALING SERING: <button>, <input>, <select>, dan <textarea>",
                    "TIDAK mewarisi font dari body. Keempatnya memakai font bawaan",
                    "sistem operasi, jadi tombol dan kotak isian terlihat asing di",
                    "tengah halaman yang hurufnya sudah kamu atur rapi. Bukan kesalahan",
                    "kamu - memang begitu bawaannya. Perbaikannya satu aturan:",
                    "",
                    "  button, input, select, textarea { font: inherit; }",
                ]
            },
            {
                "heading": "Menata teks satu halaman",
                "code": """body {
  font-family: system-ui, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  font-size: 1rem;
  line-height: 1.65;
  color: #23252b;
}

h1, h2, h3 {
  font-family: Georgia, "Times New Roman", serif;
  line-height: 1.2;
  letter-spacing: -0.01em;
  margin-bottom: 0.4em;
}

h1 {
  font-size: 2.25rem;
  font-weight: 700;
}

h2 {
  font-size: 1.5rem;
}

code, pre {
  font-family: Consolas, "Courier New", monospace;
  font-size: 0.9375rem;
}

/* Tanpa baris ini, tombol memakai huruf bawaan sistem */
button, input, select, textarea {
  font: inherit;
}

a {
  color: #1a4fa0;
  text-decoration: underline;
  text-underline-offset: 2px;
}

.isi {
  max-width: 68ch;
}""",
            },
            {
                "body": [
                    "PANJANG BARIS",
                    "",
                    "Baris yang terlalu panjang melelahkan: begitu mata sampai ujung",
                    "kanan, ia harus mencari lagi awal baris berikutnya di kiri, dan",
                    "makin panjang barisnya makin sering tersesat. Ukuran yang nyaman",
                    "sekitar 45-75 karakter. Batasi dengan satu baris:",
                    "",
                    "  .isi { max-width: 68ch; }",
                    "",
                    "Satuan ch cocok di sini justru karena ia mengikuti fontnya - kalau",
                    "hurufnya diganti jadi lebih lebar, batasnya ikut menyesuaikan.",
                    "",
                    "Ringkas font dalam satu properti (urutannya tidak boleh diacak):",
                    "  font: italic 700 1rem/1.5 Georgia, serif;",
                    "        gaya  tebal ukuran/jarak-baris keluarga",
                    "Bentuk ringkas ini MENGATUR ULANG semua bagian yang tidak kamu",
                    "sebut ke nilai bawaannya - termasuk line-height. Itu sebabnya",
                    "banyak orang memilih menulis propertinya satu per satu.",
                    "",
                    "Font dari berkas sendiri (@font-face) memang bisa, tapi tunda",
                    "dulu: tiap font tambahan adalah berkas yang harus diunduh sebelum",
                    "teksnya bisa dibaca, dan mengurus itu punya persoalan sendiri.",
                    "Untuk sekarang, daftar font sistem sudah lebih dari cukup dan",
                    "muncul seketika.",
                ]
            },
            {
                "body": [
                    "FONT WEB: TIGA BENTUK YANG PASTI KAMU LIHAT DI BERKAS ORANG",
                    "",
                    "Penundaan barusan tetap berlaku - untuk latihan, font sistem",
                    "sudah cukup. Tapi bentuknya perlu kamu kenali sekarang juga,",
                    "karena inilah yang duduk di baris pertama berkas gaya orang lain,",
                    "dan dari sinilah nama asing pada 'font-family: Inter, sans-serif'",
                    "berasal.",
                    "",
                    "1. @font-face - font dari berkas milikmu sendiri:",
                    "",
                    "  @font-face {",
                    "    font-family: \"Inter\";      nama yang kamu karang sendiri",
                    "    src: url(\"font/inter.woff2\") format(\"woff2\");",
                    "    font-weight: 400;",
                    "    font-display: swap;",
                    "  }",
                    "",
                    "  body { font-family: \"Inter\", system-ui, sans-serif; }",
                    "",
                    "@font-face tidak menata apa pun. Ia cuma MENDAFTARKAN sebuah nama",
                    "beserta berkasnya; yang memakainya tetap font-family biasa di",
                    "bawahnya, lengkap dengan daftar cadangan seperti sebelumnya.",
                    "",
                    "font-display: swap artinya 'tampilkan dulu font cadangan, tukar",
                    "begitu berkasnya tiba'. Tanpa baris itu sebagian browser",
                    "menyembunyikan teksnya sampai berkas fontnya selesai diunduh -",
                    "halaman terlihat kosong beberapa detik padahal tulisannya sudah",
                    "ada di situ.",
                    "",
                    "Satu berkas .woff2 melayani satu ketebalan saja. Butuh 400 dan",
                    "700? Dua blok @font-face, font-family sama, font-weight berbeda.",
                    "",
                    "2. <link> ke penyedia font. Ini masuk ke HTML, di dalam <head>:",
                    "",
                    "  <link rel=\"stylesheet\"",
                    "        href=\"https://fonts.googleapis.com/css2?family=Inter\">",
                    "",
                    "3. @import - isinya sama, tapi dipanggil dari dalam berkas CSS:",
                    "",
                    "  @import url(\"https://fonts.googleapis.com/css2?family=Inter\");",
                    "",
                    "@import WAJIB berada di baris paling atas berkas gaya, sebelum",
                    "aturan apa pun. Ditaruh di tengah berkas ia diabaikan diam-diam,",
                    "dan font yang 'tidak mau muncul' itu sebabnya. Bentuk <link> juga",
                    "lebih cepat: browser bisa mengunduh berkas gaya dan berkas font",
                    "berbarengan, sedangkan @import memaksa berkas gayamu selesai",
                    "dibaca lebih dulu.",
                    "",
                    "Cara mana pun yang dipakai, daftar cadangan tetap wajib ditulis.",
                    "Selama berkas fontnya belum tiba - atau kalau ia gagal tiba sama",
                    "sekali - yang dipakai adalah nama berikutnya di daftar itu.",
                ]
            },
        ],
    },
    {
        "title": "7. Box Model: margin, border, padding, content",
        "sections": [
            {
                "body": [
                    "Setiap elemen di halaman adalah sebuah KOTAK. Tidak ada",
                    "pengecualian - paragraf, gambar, bahkan satu kata di dalam <span>.",
                    "Tiap kotak punya empat lapis, dari dalam ke luar:",
                    "",
                    "  +----------------------------------------------------+",
                    "  |  margin - jarak ke tetangga                        |",
                    "  |  +----------------------------------------------+  |",
                    "  |  |  border - garis tepinya                      |  |",
                    "  |  |  +----------------------------------------+  |  |",
                    "  |  |  |  padding - jarak isi ke tepi           |  |  |",
                    "  |  |  |  +----------------------------------+  |  |  |",
                    "  |  |  |  |  content: teks dan anak elemen   |  |  |  |",
                    "  |  |  |  +----------------------------------+  |  |  |",
                    "  |  |  +----------------------------------------+  |  |",
                    "  |  +----------------------------------------------+  |",
                    "  +----------------------------------------------------+",
                    "",
                    "Hampir semua kebingungan tata letak berawal dari salah membaca",
                    "gambar ini. Pelajari sekali, hemat berjam-jam nanti.",
                ]
            },
            {
                "body": [
                    "BEDA PADDING DAN MARGIN - ini yang paling sering tertukar.",
                    "",
                    "  padding  jarak DI DALAM kotak, antara isi dan garis tepinya.",
                    "           Ikut kena background elemen itu.",
                    "           Ikut bisa diklik (padding tombol tetap area tombol).",
                    "           Menambahnya membuat KOTAKNYA SENDIRI jadi lebih besar.",
                    "",
                    "  margin   jarak DI LUAR kotak, antara kotak ini dan tetangganya.",
                    "           Selalu bening - yang terlihat di situ latar induknya.",
                    "           Tidak bisa diklik.",
                    "           Menambahnya MENDORONG kotak lain menjauh.",
                    "",
                    "Cara cepat mengingat:",
                    "  Ingin teks tidak menempel ke garis tepi tombol? -> padding.",
                    "  Ingin dua tombol tidak berdempetan?             -> margin.",
                    "",
                    "Uji sendiri dalam tiga puluh detik: beri sebuah elemen",
                    "background: pink, lalu tambah padding - daerah pink-nya MELEBAR.",
                    "Ganti dengan margin - daerah pink-nya tetap sama, yang melebar",
                    "ruang kosong di sekitarnya. Sekali melihat itu, kamu tidak akan",
                    "tertukar lagi.",
                    "",
                    "Nilai ringkas, searah jarum jam mulai dari ATAS:",
                    "  margin: 10px;                  keempat sisi 10px",
                    "  margin: 10px 20px;             atas-bawah 10, kiri-kanan 20",
                    "  margin: 10px 20px 30px;        atas 10, kiri-kanan 20, bawah 30",
                    "  margin: 10px 20px 30px 40px;   atas, kanan, bawah, kiri",
                    "",
                    "Ingat urutannya lewat kata TRouBLe: Top Right Bottom Left.",
                    "Sisi tunggal ditulis lengkap: margin-top, padding-left,",
                    "border-bottom, dan seterusnya.",
                    "",
                    "border butuh TIGA bagian: tebal, gaya, warna.",
                    "  border: 1px solid #ccc;",
                    "Tanpa bagian gaya (solid, dashed, dotted), garisnya TIDAK muncul",
                    "sama sekali meski tebal dan warnanya sudah ditulis. Itu penyebab",
                    "'border saya hilang' yang paling sering.",
                    "  border-radius: 8px;   membulatkan sudut",
                    "  border-radius: 50%;   lingkaran, kalau kotaknya bujur sangkar",
                ]
            },
            {
                "body": [
                    "KENAPA box-sizing: border-box HAMPIR SELALU DIPAKAI",
                    "",
                    "Secara bawaan, width mengukur CONTENT saja. Padding dan border",
                    "ditambahkan DI LUAR angka itu.",
                    "",
                    "  .kotak { width: 200px; padding: 20px; border: 2px solid black; }",
                    "",
                    "  Lebar sesungguhnya = 2 + 20 + 200 + 20 + 2 = 244px.",
                    "",
                    "Kamu menulis 200, yang muncul 244. Akibatnya baru terasa saat",
                    "dua sisi berdampingan masing-masing width: 50% dan punya padding:",
                    "totalnya lebih dari 100%, dan yang kedua terlempar ke bawah.",
                    "Sepuluh menit dihabiskan mencari 'kelebihan' yang sebenarnya",
                    "kamu tulis sendiri.",
                    "",
                    "box-sizing: border-box mengubah arti width menjadi 'lebar SELURUH",
                    "kotak, padding dan border sudah termasuk'. Dengan itu width: 200px",
                    "berarti 200px betulan, berapa pun paddingnya - yang menyusut",
                    "adalah ruang isinya.",
                    "",
                    "Karena itu hampir semua proyek diawali baris ini:",
                    "",
                    "  *, *::before, *::after { box-sizing: border-box; }",
                    "",
                    "Kenapa barisnya menyebut TIGA hal, bukan satu? Tanda * berarti",
                    "semua elemen. Dua titik dua sesudahnya menandai PSEUDO-ELEMENT:",
                    "dua bagian buatan yang bisa dimiliki tiap elemen tapi tidak",
                    "pernah ditulis di HTML - dan justru karena tidak ditulis di HTML,",
                    "* sendirian tidak menjangkaunya. Keduanya sering dipakai untuk",
                    "garis dan hiasan yang juga punya padding, jadi mereka butuh",
                    "perlakuan yang sama. Bentuknya dibahas di materi Pseudo-class dan",
                    "Pseudo-element; untuk sekarang cukup tahu satu baris itu menyapu",
                    "ketiganya sekaligus.",
                    "",
                    "Ini bukan trik. Ini memperbaiki bawaan yang sudah lama disesali",
                    "bahkan oleh orang yang merancangnya. Tulis di baris pertama",
                    "berkas gayamu dan jangan dipikirkan lagi seumur proyek.",
                    "",
                    "Catatan: margin TIDAK pernah masuk hitungan width, bahkan dengan",
                    "border-box. Memang begitu seharusnya - margin ada di luar kotak.",
                ]
            },
            {
                "body": [
                    "KENAPA MARGIN BERTUMPUK (MARGIN COLLAPSE)",
                    "",
                    "Dua paragraf berurutan. Yang atas punya margin-bottom: 20px, yang",
                    "bawah margin-top: 20px. Jarak di antara keduanya bukan 40px,",
                    "melainkan 20px.",
                    "",
                    "Margin vertikal yang bersentuhan MENYATU, dan yang menang yang",
                    "TERBESAR - bukan jumlahnya.",
                    "",
                    "  margin-bottom: 30px  bertemu  margin-top: 10px  ->  jarak 30px",
                    "",
                    "Ini disengaja, bukan bug. Bayangkan tanpa itu: deretan paragraf",
                    "yang semuanya punya margin atas dan bawah akan berjarak dua kali",
                    "lipat di tengah dan satu kali di ujung. Tidak ada yang mau begitu.",
                    "",
                    "Tiga hal yang perlu diketahui:",
                    "",
                    "  1. Hanya margin ATAS dan BAWAH. Margin kiri dan kanan TIDAK",
                    "     pernah menyatu - dua kotak bersebelahan berjarak 20+20=40px.",
                    "",
                    "  2. Juga terjadi antara INDUK dan ANAK PERTAMA. Kalau anak",
                    "     pertama punya margin-top: 20px sementara induknya tidak punya",
                    "     padding atau border di sisi atas, margin itu 'bocor keluar'",
                    "     dan yang bergeser justru INDUKNYA. Inilah sebabnya sebuah",
                    "     kotak kadang punya celah di atasnya yang tidak bisa kamu",
                    "     temukan asalnya, dan menghapus padding malah menambah celah.",
                    "",
                    "  3. Margin kosong juga menyatu: elemen tanpa isi, tanpa padding,",
                    "     dan tanpa border akan menyatukan margin atas dan bawahnya",
                    "     sendiri jadi satu.",
                    "",
                    "Cara menghentikannya kalau memang mengganggu:",
                    "  - Beri induknya padding atau border di sisi itu (padding-top:",
                    "    1px sudah cukup memutusnya).",
                    "  - Ubah induknya jadi display: flex atau grid. Di dalam flex dan",
                    "    grid margin TIDAK pernah menyatu sama sekali.",
                    "  - Paling rapi: jangan pakai margin dua arah. Pilih SATU arah",
                    "    saja (misalnya cuma margin-bottom) atau pakai gap di flex/grid",
                    "    dan lupakan seluruh persoalan ini.",
                ]
            },
            {
                "heading": "Box model dalam praktik",
                "code": """/* Baris pertama di hampir semua berkas gaya */
*, *::before, *::after {
  box-sizing: border-box;
}

.kartu {
  width: 300px;
  padding: 24px;             /* jarak isi ke garis tepi */
  border: 1px solid #d8d8d8;
  border-radius: 8px;
  background: white;
  margin-bottom: 16px;       /* jarak ke kartu berikutnya */
}

/* Satu arah saja: tidak ada margin yang saling menyatu */
.kartu p {
  margin-top: 0;
  margin-bottom: 12px;
}

.kartu p:last-child {
  margin-bottom: 0;
}

/* Memusatkan kotak: margin kiri-kanan otomatis */
.wadah {
  max-width: 720px;
  margin: 0 auto;
  padding: 0 16px;
}""",
            },
            {
                "body": [
                    "Soal margin: 0 auto - dua syarat yang sering terlupa:",
                    "",
                    "  1. Elemennya harus punya width atau max-width. 'auto' berarti",
                    "     'bagi rata sisa ruangnya', dan kalau elemennya sudah memakan",
                    "     seluruh lebar, tidak ada sisa untuk dibagi.",
                    "  2. Hanya bekerja MENDATAR. margin: auto 0 tidak memusatkan",
                    "     apa pun ke tengah secara menurun. Untuk itu pakai flex",
                    "     atau grid (materi 7 dan 8).",
                    "",
                    "Perhatikan juga padding: 0 16px pada .wadah di contoh. Tanpa itu,",
                    "di layar yang persis 720px atau lebih sempit, teksnya menempel",
                    "ke tepi layar. Batas lebar saja tidak cukup; isi selalu butuh",
                    "ruang napas di kiri-kanannya.",
                ]
            },
        ],
    },
    {
        "title": "8. Display dan Alur Dokumen",
        "sections": [
            {
                "body": [
                    "ALUR DOKUMEN (normal flow) adalah cara browser menata elemen",
                    "kalau kamu tidak menyuruh apa-apa: dari atas ke bawah, dan di",
                    "dalam satu baris dari kiri ke kanan.",
                    "",
                    "Sebelum belajar flexbox, grid, atau position, pahami dulu dua",
                    "watak dasar ini - ketiganya cuma cara mengubah alur yang sama.",
                    "",
                    "display: block",
                    "  Memakan SELURUH lebar yang tersedia, jadi tetangganya terdorong",
                    "  ke baris berikutnya. width dan height berlaku. margin dan",
                    "  padding keempat sisi berlaku penuh.",
                    "  Bawaan untuk: div, p, h1-h6, ul, li, section, form, footer.",
                    "",
                    "display: inline",
                    "  Selebar isinya saja, mengalir bersama teks dalam satu baris.",
                    "  width dan height DIABAIKAN. margin dan padding ATAS-BAWAH tidak",
                    "  mendorong apa pun (paddingnya tetap tergambar, tapi menimpa",
                    "  baris di atas dan bawahnya alih-alih memberi ruang).",
                    "  Bawaan untuk: span, a, strong, em, code, label.",
                    "",
                    "display: inline-block",
                    "  Mengalir dalam baris seperti inline, TAPI width, height, dan",
                    "  margin/padding vertikal berlaku seperti block. Jalan tengah",
                    "  untuk tombol, lencana, dan item menu mendatar.",
                    "",
                    "display: none",
                    "  Hilang total: tidak digambar dan tidak menyisakan ruang.",
                    "",
                    "KEBINGUNGAN NOMOR SATU: 'kenapa width pada <span> saya tidak",
                    "berpengaruh?' Karena span itu inline. Ubah dulu jadi inline-block",
                    "atau block. Aturannya sama untuk <a> - itu sebabnya tombol yang",
                    "dibuat dari tautan selalu perlu display: inline-block.",
                    "",
                    "Pengecualian yang perlu diketahui: <img> secara teknis inline,",
                    "tapi width dan height tetap berlaku padanya. Gambar termasuk",
                    "'replaced element' - isinya datang dari luar dan punya ukuran",
                    "sendiri.",
                ]
            },
            {
                "body": [
                    "TIGA CARA MENYEMBUNYIKAN, TIGA AKIBAT BERBEDA",
                    "",
                    "  display: none        Hilang. Ruangnya ikut hilang, tetangganya",
                    "                       maju mengisi. Tidak dibacakan pembaca layar.",
                    "  visibility: hidden   Tidak terlihat, TAPI ruangnya tetap kosong",
                    "                       di situ. Tidak dibacakan pembaca layar.",
                    "  opacity: 0           Tidak terlihat, ruang tetap, DAN masih bisa",
                    "                       diklik. Tetap dibacakan pembaca layar.",
                    "",
                    "Yang terakhir itu jebakan yang nyata: tombol ber-opacity 0 tetap",
                    "menangkap klik orang yang tidak tahu ada tombol di sana.",
                    "",
                    "Obatnya satu baris: pointer-events: none. Elemen yang memakainya",
                    "jadi TEMBUS bagi tetikus dan sentuhan - klik menerobosnya dan",
                    "mengenai apa pun yang ada di belakangnya, seolah ia tidak ada.",
                    "Elemennya tetap terlihat; yang hilang cuma kemampuannya diklik.",
                    "",
                    "Dua pemakaian hariannya:",
                    "  - Ikon di dalam kotak isian. Tanpa pointer-events: none, klik",
                    "    yang kebetulan mendarat di atas ikonnya tidak menaruh kursor",
                    "    ke dalam kotak, dan orang mengira kotaknya rusak.",
                    "  - Lapisan yang menutupi seluruh layar untuk gradien atau",
                    "    bayangan. Ia harus terlihat, tapi tidak boleh menghalangi",
                    "    satu pun klik di bawahnya.",
                    "",
                    "Satu batas yang perlu diingat: pointer-events cuma mengurus",
                    "tetikus dan sentuhan. Tombol yang 'dimatikan' begitu tetap bisa",
                    "dicapai dengan Tab dan tetap dibacakan pembaca layar. Untuk",
                    "benar-benar menyingkirkan sesuatu, display: none masih yang",
                    "paling jujur.",
                    "",
                    "CELAH MISTERIUS DI ANTARA ELEMEN inline-block",
                    "",
                    "Dua <li> inline-block yang ditulis di baris berbeda pada HTML-nya",
                    "punya jarak sekitar 4px yang tidak pernah kamu tulis. Itu SPASI",
                    "dan ganti baris di antara tagnya - inline berarti ikut aturan",
                    "teks, dan spasi antar kata memang terlihat.",
                    "",
                    "Dulu orang mengakalinya dengan menulis tag berdempetan atau",
                    "font-size: 0 pada induknya. Keduanya menyakitkan. Cara waras hari",
                    "ini: pakai flex atau grid pada induknya - keduanya tidak",
                    "menghitung spasi HTML sama sekali.",
                    "",
                    "KALAU ISI LEBIH BESAR DARI KOTAKNYA",
                    "  overflow: visible   bawaan, isi meluber keluar begitu saja",
                    "  overflow: hidden    kelebihannya dipotong dan tidak bisa dilihat",
                    "  overflow: auto      bilah gulir muncul hanya kalau perlu",
                    "  overflow-x / overflow-y   khusus satu sumbu",
                    "",
                    "Tabel lebar dan blok kode panjang sebaiknya dibungkus wadah",
                    "ber-overflow-x: auto. Bedanya besar: yang bisa digeser ke samping",
                    "cuma isinya, bukan SELURUH HALAMAN. Halaman yang bisa digeser",
                    "ke samping terasa rusak, dan penyebabnya hampir selalu satu",
                    "elemen yang lebih lebar dari layar.",
                ]
            },
            {
                "heading": "Mengubah alur tanpa mengubah HTML",
                "code": """/* Menu mendatar dari daftar biasa */
.menu {
  list-style: none;
  margin: 0;
  padding: 0;
}

.menu li {
  display: inline-block;
  margin-right: 12px;
}

/* Tautan yang ingin diberi ukuran harus berhenti jadi inline */
.tombol {
  display: inline-block;
  padding: 10px 18px;
  border-radius: 6px;
  background: #1a4fa0;
  color: white;
  text-decoration: none;
}

/* Gambar tidak pernah lebih lebar dari wadahnya */
img {
  max-width: 100%;
  height: auto;
  display: block;
}

/* Sembunyikan tanpa menyisakan ruang */
.tersembunyi {
  display: none;
}

/* Yang bergeser isinya, bukan halamannya */
.bungkus-tabel {
  overflow-x: auto;
}""",
            },
            {
                "body": [
                    "Perhatikan display: block pada img di contoh.",
                    "",
                    "Gambar itu inline secara bawaan, dan inline berarti ia duduk di",
                    "garis dasar teks - ada sisa ruang beberapa piksel di bawahnya",
                    "untuk ekor huruf seperti g dan y. Di dalam kartu, sisa itu",
                    "terlihat sebagai celah tipis antara gambar dan tepi bawah kartu",
                    "yang tidak berasal dari margin mana pun. display: block",
                    "menghilangkannya karena gambarnya tidak lagi ikut aturan teks.",
                    "",
                    "Ini contoh khas persoalan CSS: yang terlihat seperti 'ada margin",
                    "misterius' sebenarnya akibat wajar dari satu keputusan bawaan.",
                    "Begitu tahu sebabnya, obatnya satu baris.",
                ]
            },
        ],
    },
    {
        "title": "9. Latar, Gradien, dan Gambar dalam Kotak",
        "sections": [
            {
                "body": [
                    "Sampai sini background selalu berupa satu warna datar. Di kode nyata",
                    "hampir tidak pernah begitu: latar membawa foto, tekstur, atau gradasi.",
                    "Dan url() adalah satu-satunya tempat CSS menunjuk berkas lain, jadi di",
                    "sinilah CSS pertama kali bisa gagal karena sesuatu di luar dirinya.",
                    "",
                    "background ITU BENTUK RINGKAS, BUKAN SATU PROPERTI",
                    "",
                    "Yang sebenarnya ada delapan properti. background cuma menulis semuanya",
                    "sekaligus:",
                    "",
                    "  background-color        warna di belakang segalanya",
                    "  background-image        gambar atau gradien",
                    "  background-repeat       diulang atau tidak",
                    "  background-position     ditaruh di sebelah mana",
                    "  background-size         diregangkan seberapa",
                    "  background-attachment   ikut bergulir atau diam",
                    "  background-origin       dihitung dari tepi yang mana",
                    "  background-clip         bagian kotak mana yang tercat",
                    "",
                    "Akibatnya persis seperti bentuk ringkas font di materi Teks dan Font:",
                    "menulis background MENGATUR ULANG ketujuh sisanya ke nilai bawaannya,",
                    "entah kamu menyebutnya atau tidak.",
                    "",
                    "  .panel          { background: url(\"pola.png\") repeat; }",
                    "  .panel.terpilih { background: #fff8e1; }      /* polanya HILANG */",
                    "",
                    "Panel terpilih kehilangan polanya, dan tidak ada satu pun pesan yang",
                    "memberi tahu. Yang kamu maksud sebenarnya:",
                    "",
                    "  .panel.terpilih { background-color: #fff8e1; }",
                    "",
                    "Aturan praktisnya: kalau cuma ingin mengubah SATU bagian, sebut nama",
                    "panjangnya. Bentuk ringkas dipakai saat menetapkan latar dari nol.",
                    "",
                    "MENUNJUK BERKAS GAMBAR: url()",
                    "",
                    "  background-image: url(\"foto.jpg\");",
                    "  background-image: url(foto.jpg);      petiknya boleh dihilangkan",
                    "",
                    "Petik wajib kalau nama berkasnya mengandung spasi atau tanda kurung.",
                    "Yang tidak boleh: spasi antara url dan kurung bukanya. url (foto.jpg)",
                    "bukan url() yang sah, dan seluruh deklarasinya dibuang diam-diam.",
                    "",
                    "JEBAKAN NOMOR SATU DI SELURUH MATERI INI",
                    "",
                    "  Jalur di dalam url() dihitung dari letak BERKAS .CSS-nya,",
                    "  bukan dari halaman HTML yang memakainya.",
                    "",
                    "Susunan folder yang lazim:",
                    "",
                    "  proyek/",
                    "    index.html",
                    "    gaya/",
                    "      gaya.css        <- berkas yang sedang kamu tulis",
                    "    gambar/",
                    "      hero.jpg",
                    "",
                    "Dari index.html, gambarnya ditulis <img src=\"gambar/hero.jpg\">. Dari",
                    "gaya/gaya.css jalur yang sama SALAH: browser akan mencari berkas di",
                    "proyek/gaya/gambar/hero.jpg dan tidak menemukan apa pun. Yang benar",
                    "naik satu tingkat dulu:",
                    "",
                    "  background-image: url(\"../gambar/hero.jpg\");",
                    "",
                    "Seperti biasa di CSS tidak ada pesan error; latarnya sekadar kosong.",
                    "Jadi kalau sebuah gambar latar 'tidak muncul', periksa jalurnya lebih",
                    "dulu, sebelum mencurigai apa pun yang lain.",
                ],
            },
            {
                "body": [
                    "MENGULANG, MENARUH, DAN MENGUKUR",
                    "",
                    "Secara bawaan gambar latar DIULANG ke segala arah sampai kotaknya",
                    "penuh. Masuk akal untuk tekstur kecil, bencana untuk foto.",
                    "",
                    "  background-repeat: repeat;      bawaan, diulang dua arah",
                    "                     no-repeat;   sekali saja",
                    "                     repeat-x;    hanya mendatar",
                    "                     repeat-y;    hanya menurun",
                    "",
                    "background-position menentukan letaknya. Nilai pertama MENDATAR, nilai",
                    "kedua MENURUN:",
                    "",
                    "  background-position: center;       sama dengan 'center center'",
                    "  background-position: right top;",
                    "  background-position: 20px 40px;    20 dari kiri, 40 dari atas",
                    "  background-position: 50% 50%;      lihat catatan di bawah",
                    "",
                    "Persen di sini bekerja tidak seperti dugaan pertama. 50% berarti 'titik",
                    "50% GAMBAR ditempelkan ke titik 50% KOTAK'. Itu sebabnya 50% 50% memang",
                    "memusatkan gambar, dan 100% 100% menempelkan pojok kanan bawah gambar",
                    "ke pojok kanan bawah kotak - bukan mendorongnya keluar sejauh satu",
                    "kotak penuh.",
                    "",
                    "background-size mengatur ukurannya:",
                    "",
                    "  auto          bawaan, sebesar gambar aslinya",
                    "  cover         diperbesar sampai kotaknya TERTUTUP penuh; kelebihannya",
                    "                terpotong. Perbandingan sisinya tetap.",
                    "  contain       dikecilkan sampai SELURUH gambar muat; sisanya kosong.",
                    "                Perbandingan sisinya juga tetap.",
                    "  300px 200px   lebar dan tinggi ditulis sendiri (salah satunya boleh",
                    "                auto, supaya dihitung dari perbandingan aslinya)",
                    "",
                    "cover memotong, contain menyisakan ruang. Tidak ada pilihan ketiga -",
                    "kotak dan gambar jarang sebangun, dan sesuatu harus mengalah. Untuk",
                    "foto besar di kepala halaman hampir selalu cover.",
                    "",
                    "Jebakan kecil: contain tanpa no-repeat menyisakan ruang kosong yang",
                    "langsung diisi ulangan gambar yang sama. Yang terlihat bukan satu",
                    "gambar rapi, tapi ubin.",
                    "",
                    "BENTUK RINGKAS LENGKAP",
                    "",
                    "  background: #fff url(\"hero.jpg\") center / cover no-repeat;",
                    "              ^    ^               ^        ^     ^",
                    "              |    |               |        |     diulang atau tidak",
                    "              |    |               |        ukuran, wajib sesudah miring",
                    "              |    |               posisi",
                    "              |    gambar",
                    "              warna",
                    "",
                    "Urutan bagian lain bebas, TAPI ukuran hanya boleh ditulis sesudah",
                    "posisi dan sebuah garis miring. Tanpa itu nilainya tidak dikenali dan",
                    "SELURUH deklarasi dibuang - bukan cuma bagian ukurannya:",
                    "",
                    "  background: url(\"hero.jpg\") cover;    salah; latarnya kosong total",
                    "",
                    "BEBERAPA LATAR SEKALIGUS",
                    "",
                    "Satu elemen boleh punya banyak lapis gambar latar, dipisah koma. Yang",
                    "ditulis PERTAMA berada paling ATAS - kebalikan dari dugaan banyak orang:",
                    "",
                    "  background-image:",
                    "    url(\"stempel.png\"),",
                    "    url(\"kertas.png\");",
                    "",
                    "Warna beda sendiri: background-color tidak punya lapisan, ia selalu di",
                    "paling bawah. Karena itu di bentuk ringkas, warna hanya boleh ditulis",
                    "pada lapisan TERAKHIR.",
                    "",
                    "DUA SISANYA, SEKILAS",
                    "",
                    "background-attachment: fixed membuat gambar latar DIAM saat halaman",
                    "digulir, jadi isinya seolah lewat di depan foto. Efeknya mahal: banyak",
                    "browser ponsel mengabaikannya atau jadi tersendat. Pakai hanya kalau",
                    "halamannya tetap baik-baik saja tanpa efek itu.",
                    "",
                    "background-clip menjawab: bagian kotak mana yang tercat? Nama-namanya",
                    "diambil langsung dari empat lapis box model.",
                    "",
                    "  border-box    bawaan - sampai tepi luar, DI BAWAH garis tepinya",
                    "  padding-box   berhenti di dalam garis tepi",
                    "  content-box   hanya area isi",
                    "",
                    "Terasa sepele sampai kamu memakai border putus-putus: dengan bawaan",
                    "border-box, latar ikut tercat di sela-sela garisnya sehingga garis",
                    "putusnya tidak terbaca lagi. background-clip: padding-box selesai.",
                    "",
                    "(Kembarannya background-origin mengatur dari tepi mana POSISI gambar",
                    "mulai dihitung. Jarang perlu disentuh.)",
                ],
            },
            {
                "body": [
                    "GRADIEN ITU GAMBAR, BUKAN WARNA",
                    "",
                    "Ini yang paling sering membuat orang mentok di percobaan pertama:",
                    "",
                    "  background-color: linear-gradient(#fff, #ccc);   tidak pernah jalan",
                    "",
                    "linear-gradient() menghasilkan sebuah GAMBAR yang digambar browser",
                    "sendiri. Tempatnya di background-image, atau di bentuk ringkas",
                    "background. background-color hanya menerima satu warna, titik. Dan",
                    "seperti biasa, nilai yang tidak dikenali dibuang tanpa pesan apa pun.",
                    "",
                    "  background-image: linear-gradient(#fff, #ccc);   benar",
                    "  background: linear-gradient(#fff, #ccc);         benar juga",
                    "",
                    "Konsekuensi lain dari 'gradien itu gambar': background-size, -position,",
                    "dan -repeat berlaku padanya persis seperti pada foto.",
                    "",
                    "BENTUK linear-gradient",
                    "",
                    "  linear-gradient(#1a4fa0, #7a1f9a)               atas ke bawah (bawaan)",
                    "  linear-gradient(to right, #1a4fa0, #7a1f9a)     kiri ke kanan",
                    "  linear-gradient(to bottom right, #fff, #ccc)    pojok ke pojok",
                    "  linear-gradient(45deg, #fff, #ccc)              sudut sendiri",
                    "",
                    "Soal derajat: 0deg mengarah ke ATAS, lalu berputar searah jarum jam -",
                    "90deg ke kanan, 180deg ke bawah. Bukan seperti busur derajat di",
                    "sekolah, jadi lihat hasilnya, jangan dihitung di kepala.",
                    "",
                    "Warnanya boleh lebih dari dua, dan tiap warna boleh diberi HENTI:",
                    "",
                    "  linear-gradient(to right, #f2c14e 0%, #e08c3c 40%, #b4451f 100%)",
                    "",
                    "Dua henti yang angkanya kembar menghasilkan garis TAJAM, bukan",
                    "gradasi. Ini trik lazim untuk membuat pita dan pemisah:",
                    "",
                    "  linear-gradient(#f6f5f2 50%, #eceae4 50%)",
                    "",
                    "Dua saudara yang cara pakainya sama persis:",
                    "",
                    "  radial-gradient(circle at 30% 30%, #ffffff, #cfd4dd)",
                    "      memancar dari sebuah titik, bukan sepanjang garis",
                    "  conic-gradient(#e5484d 0deg 90deg, #eceae4 90deg 360deg)",
                    "      berputar mengelilingi titik pusat; inilah cara orang membuat",
                    "      diagram lingkaran tanpa satu pun berkas gambar",
                    "",
                    "Ada juga repeating-linear-gradient yang mengulang polanya menjadi",
                    "deretan garis. Ketiganya tetap GAMBAR, jadi seluruh aturan di atas",
                    "berlaku sama persis untuk mereka.",
                    "",
                    "LAPISAN GELAP DI ATAS FOTO",
                    "",
                    "Teks putih di atas foto hampir selalu susah dibaca: satu foto punya",
                    "bagian terang dan gelap sekaligus, dan bagian terangnya menelan",
                    "hurufmu. Ini persoalan kontras yang sama dengan materi Warna dan Satuan,",
                    "cuma kali ini latarnya tidak seragam - jadi rasio kontrasnya tidak bisa",
                    "dihitung sekali untuk seluruh kotak.",
                    "",
                    "Obatnya bukan mengganti fotonya, tapi menumpuk film gelap tembus",
                    "pandang di atasnya - yaitu gradien dari warna yang sama dengan dua",
                    "tingkat alfa berbeda:",
                    "",
                    "  .hero {",
                    "    background:",
                    "      linear-gradient(rgb(20 20 25 / 70%), rgb(20 20 25 / 30%)),",
                    "      url(\"../gambar/hero.jpg\") center / cover no-repeat;",
                    "    color: #ffffff;",
                    "  }",
                    "",
                    "Lapisan pertama ada di atas, jadi film gelapnya menutupi foto dan bukan",
                    "sebaliknya. Karena filmnya sendiri bergradasi, bagian atas - tempat",
                    "judulnya duduk - lebih gelap, sementara bagian bawah fotonya tetap",
                    "terlihat jelas.",
                ],
            },
            {
                "heading": "gaya/gaya.css",
                "code": """/* Susunan berkas yang diasumsikan:
 *
 *   proyek/index.html
 *   proyek/gaya/gaya.css     <- berkas INI
 *   proyek/gambar/hero.jpg
 *
 * Tiap url() di bawah dihitung dari gaya/, jadi naik satu tingkat dulu.
 */

body {
  margin: 0;
  background-color: #f6f5f2;
  color: #23252b;
  font-family: system-ui, sans-serif;
}

/* Dua lapis. Yang ditulis pertama ada di ATAS. */
.hero {
  background-image:
    linear-gradient(rgb(20 20 25 / 70%), rgb(20 20 25 / 30%)),
    url("../gambar/hero.jpg");
  background-position: center;
  background-size: cover;
  background-repeat: no-repeat;
  min-height: 60vh;
  padding: 64px 24px;
  color: #ffffff;
}

/* Hasil yang sama persis, ditulis ringkas.
   Ukuran selalu SESUDAH posisi dan sebuah garis miring. */
.hero-ringkas {
  background:
    linear-gradient(rgb(20 20 25 / 70%), rgb(20 20 25 / 30%)),
    url("../gambar/hero.jpg") center / cover no-repeat;
  min-height: 60vh;
  padding: 64px 24px;
  color: #ffffff;
}

.pita {
  height: 6px;
  background: linear-gradient(90deg, #1a4fa0, #7a1f9a);
}

/* Henti warna kembar: garis tajam, bukan gradasi */
.pemisah {
  height: 72px;
  background: linear-gradient(#f6f5f2 50%, #eceae4 50%);
}

.panel {
  padding: 24px;
  border: 3px dashed #c9c4b8;
  background: #ffffff url("../gambar/pola.png") left top / 48px repeat;
  background-clip: padding-box;   /* pola berhenti di dalam garis putus */
}

/* Hanya menukar WARNANYA. Menulis 'background:' di sini akan menghapus
   pola, ukuran, dan clip yang baru saja diatur di atas. */
.panel.terpilih {
  background-color: #fff8e1;
}""",
            },
            {
                "heading": "Gambar di dalam kotak: img, object-fit, aspect-ratio",
                "body": [
                    "<img> ATAU background-image?",
                    "",
                    "Pertanyaan penentunya satu: kalau gambar itu hilang, apakah ada",
                    "INFORMASI yang ikut hilang?",
                    "",
                    "  Ya     -> pakai <img> dengan alt. Foto produk, grafik, potret orang,",
                    "            tangkapan layar. Ia ikut tercetak, ikut ditemukan mesin",
                    "            pencari, dan dibacakan pembaca layar lewat alt-nya.",
                    "  Tidak  -> pakai background-image. Tekstur, pola, gradasi, foto hiasan",
                    "            di belakang judul. Latar tidak punya alt, tidak dibacakan",
                    "            siapa pun, dan secara bawaan tidak ikut tercetak.",
                    "",
                    "Menaruh foto produk sebagai background berarti menghapusnya dari",
                    "halaman bagi setiap orang yang tidak melihat layarnya. Sebaliknya,",
                    "menaruh tekstur hiasan sebagai <img> memaksa pembaca layar mengumumkan",
                    "sesuatu yang tidak berarti apa-apa (lihat alt=\"\" di materi HTML soal",
                    "tautan dan gambar).",
                    "",
                    "MENARUH FOTO KE KOTAK BERUKURAN TETAP",
                    "",
                    "Di materi Display dan Alur Dokumen ada resep gambar yang mengalir",
                    "bebas:",
                    "",
                    "  img { max-width: 100%; height: auto; }",
                    "",
                    "Itu tetap benar untuk gambar di tengah artikel. Tapi di deretan kartu",
                    "produk resep itu justru TIDAK BISA dipakai, dan sebabnya bukan selera:",
                    "height: auto berarti 'setinggi apa pun perbandingan aslinya', sedangkan",
                    "yang kamu butuhkan adalah 'setinggi kartu di sebelahnya'. Dua permintaan",
                    "itu saling meniadakan - begitu tingginya kamu tentukan, height: auto",
                    "sudah tidak ada lagi.",
                    "",
                    "Dan begitu tinggi DAN lebar dipaksakan, bawaan CSS akan menggepengkan",
                    "gambarnya. Nama bawaan itu object-fit: fill.",
                    "",
                    "  object-fit: fill      bawaan; ditarik sampai pas, wajah jadi gepeng",
                    "  object-fit: cover     dipotong seperlunya, perbandingannya utuh",
                    "  object-fit: contain   dimuat seluruhnya, sisanya jadi ruang kosong",
                    "  object-fit: none      ukuran asli, kelebihannya terpotong",
                    "",
                    "Kosakatanya sengaja sama dengan background-size, dan artinya memang",
                    "sama. Bedanya cuma sasaran: background-size mengurus GAMBAR LATAR,",
                    "object-fit mengurus isi elemen <img> atau <video> yang sungguhan.",
                    "",
                    "Pasangannya, object-position, menentukan bagian mana yang dipertahankan",
                    "saat dipotong. Bawaannya 50% 50%, alias tengah.",
                    "",
                    "  object-position: top;      potong dari bawah - aman untuk potret,",
                    "                             karena wajah orang jarang ada di bawah",
                    "",
                    "DUA JEBAKAN object-fit:",
                    "  1. Ia tidak berpengaruh sama sekali pada <div>. Hanya untuk elemen",
                    "     yang isinya datang dari luar - <img>, <video> - yaitu 'replaced",
                    "     element' yang disinggung di materi Display dan Alur Dokumen.",
                    "  2. Ia butuh kotak yang ukurannya sudah pasti. Kalau lebar dan tinggi",
                    "     sama-sama auto, tidak ada yang perlu dimuatkan ke mana pun, dan",
                    "     nilainya seolah tidak mempan.",
                    "",
                    "MENGUNCI PERBANDINGAN SISI",
                    "",
                    "  .kartu-foto { width: 100%; aspect-ratio: 4 / 3; object-fit: cover; }",
                    "",
                    "aspect-ratio menghitung sisi yang tidak kamu sebut. Dengan lebar 100%",
                    "dan perbandingan 4/3, tingginya selalu tiga perempat lebarnya, berapa",
                    "pun lebar layarnya. Nilai yang lazim: 16 / 9, 4 / 3, 1 / 1, 3 / 2.",
                    "",
                    "Untungnya lebih besar dari sekadar rapi: ruang kotaknya sudah DIPESAN",
                    "sebelum berkas gambarnya selesai diunduh, jadi halaman tidak melompat",
                    "saat gambarnya datang. Ini persoalan yang sama yang dijawab atribut",
                    "width dan height pada <img> di materi HTML soal gambar - keduanya",
                    "saling melengkapi, bukan menggantikan.",
                    "",
                    "Dua hal yang perlu diingat:",
                    "  - aspect-ratio hanya bekerja kalau salah satu sisinya auto. Kalau",
                    "    width DAN height dua-duanya kamu tulis, ia diabaikan diam-diam.",
                    "  - Ia bukan kerangkeng. Kalau isi sebuah kotak lebih tinggi dari",
                    "    jatahnya, kotaknya tetap memanjang mengikuti isinya. Untuk",
                    "    memaksanya, jadikan kotaknya wadah gulir: overflow: hidden atau",
                    "    overflow: auto.",
                ],
                "code": """/* Dipakai untuk markup seperti ini:
 *
 *   <article class="kartu">
 *     <img class="kartu-foto" src="gambar/kopi.jpg"
 *          alt="Segelas kopi susu gula aren di meja kayu"
 *          width="800" height="600">
 *     <div class="kartu-isi">
 *       <h3>Kopi Susu Gula Aren</h3>
 *       <p>Espresso, susu segar, dan gula aren cair.</p>
 *     </div>
 *   </article>
 */

.daftar-produk {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
  gap: 20px;
}

.kartu {
  background-color: #ffffff;
  border: 1px solid #e4e2dc;
  border-radius: 10px;
  overflow: hidden;             /* sudut membulat ikut memotong fotonya */
}

.kartu-foto {
  display: block;               /* buang celah garis dasar di bawah gambar */
  width: 100%;
  aspect-ratio: 4 / 3;          /* tinggi dihitung sendiri, ruang dipesan */
  object-fit: cover;            /* dipotong, bukan digepengkan */
  object-position: center;
  background-color: #eceae4;    /* warna penunggu selagi foto dimuat */
}

/* Foto potret: pertahankan bagian atasnya */
.kartu-foto.potret {
  object-position: top;
}

.kartu-isi {
  padding: 16px;
}

.kartu-isi h3 {
  margin: 0 0 6px;
}""",
            },
        ],
    },
    {
        "title": "10. Bayangan dan Filter",
        "sections": [
            {
                "body": [
                    "box-shadow menggambar bayangan di belakang sebuah kotak. Masalahnya, nilainya",
                    "berupa deretan angka TANPA NAMA - dan tanpa tahu urutannya, baris seperti ini",
                    "cuma bisa disalin, tidak bisa dibaca:",
                    "",
                    "  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);",
                    "",
                    "Urutannya selalu sama. Hafalkan sekali, dan seluruh CSS orang lain jadi terbaca:",
                    "",
                    "  box-shadow: <geser-x> <geser-y> <kabur> <sebar> <warna>;",
                    "",
                    "  geser-x   ke kanan kalau positif, ke kiri kalau negatif",
                    "  geser-y   ke BAWAH kalau positif, ke atas kalau negatif",
                    "  kabur     0 berarti tepinya tajam; makin besar makin lembut dan makin melebar",
                    "  sebar     membesarkan (positif) atau mengecilkan (negatif) bentuk bayangannya",
                    "  warna     hampir selalu hitam yang tembus pandang",
                    "",
                    "KENAPA geser-y POSITIF BERARTI KE BAWAH",
                    "",
                    "Sumbu tegak di CSS dihitung menurun dari tepi atas - sama seperti top: 10px yang",
                    "memindahkan elemen ke bawah, bukan ke atas. Jadi 2px berarti bayangannya jatuh",
                    "2px di bawah kotaknya, seolah cahaya datang dari atas. Itu sebabnya hampir semua",
                    "bayangan antarmuka berbentuk 0 <sesuatu> - geser-x-nya nol, karena cahaya di",
                    "layar disepakati datang lurus dari atas, bukan dari samping.",
                    "",
                    "Dua angka terakhir boleh tidak ditulis, jadi kamu akan menemui tiga bentuk:",
                    "",
                    "  box-shadow: 4px 4px red;                   x, y saja - bayangan tajam",
                    "  box-shadow: 0 2px 8px rgba(0, 0, 0, .15);  x, y, kabur   <- paling sering",
                    "  box-shadow: 0 6px 12px -4px #333;          x, y, kabur, sebar",
                    "",
                    "Warnanya juga boleh ditulis PALING DEPAN - rgba(0,0,0,.15) 0 2px 8px sah dan",
                    "artinya persis sama. Bentuk itu dipakai beberapa pustaka, jadi jangan kaget.",
                    "",
                    "KENAPA WARNANYA HITAM TEMBUS PANDANG, BUKAN ABU-ABU",
                    "",
                    "rgba(0, 0, 0, 0.15) berarti hitam dengan tingkat kepekatan 0,15 - bentuk lama",
                    "dari rgb(0 0 0 / 15%) yang kamu pakai di materi Warna dan Satuan. Keduanya sah;",
                    "di kode bayangan bentuk rgba() jauh lebih sering terlihat.",
                    "",
                    "Hitam tembus pandang MENGGELAPKAN apa pun yang ada di belakangnya, jadi bayangan",
                    "yang sama tetap masuk akal di atas latar putih maupun di atas latar biru. Kalau",
                    "kamu menulis warna pekat seperti #cccccc, di atas latar berwarna ia terlihat",
                    "seperti noda abu-abu yang ditempel, bukan seperti bayangan.",
                    "",
                    "Dua hal kecil yang menghemat waktu: bayangan otomatis mengikuti border-radius",
                    "(sudut membulat dapat bayangan membulat, tanpa diatur), dan box-shadow: none",
                    "adalah cara mematikannya kembali.",
                ],
            },
            {
                "body": [
                    "inset: BAYANGAN DI DALAM KOTAK",
                    "",
                    "Tambahkan kata inset di depan nilainya, dan bayangannya pindah ke sebelah dalam:",
                    "",
                    "  box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);",
                    "",
                    "Efeknya berlawanan. Yang tanpa inset membuat kotak seperti TERANGKAT dari",
                    "halaman; yang dengan inset membuatnya seperti CEKUNG ke dalam halaman. Itu",
                    "sebabnya kotak isian dan tombol yang sedang ditekan sering memakainya: cekung",
                    "berarti 'di sini tempat isi masuk', atau 'ini sedang kamu tekan'.",
                    "",
                    "BEBERAPA BAYANGAN SEKALIGUS, DIPISAH KOMA",
                    "",
                    "  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.06),",
                    "              0 4px 12px rgba(0, 0, 0, 0.12);",
                    "",
                    "Yang ditulis PERTAMA digambar paling atas, yang berikutnya di belakangnya.",
                    "",
                    "Kenapa dua bayangan tipis terlihat lebih alami daripada satu bayangan tebal:",
                    "benda sungguhan menjatuhkan DUA hal sekaligus. Ada bayangan rapat dan agak",
                    "gelap tepat di bawah tempat ia menyentuh, dan ada bayangan lebar yang sangat",
                    "samar di sekelilingnya. Satu bayangan besar sendirian tidak punya titik sentuh",
                    "itu, jadi kotaknya terlihat melayang di dalam kabut - dan supaya kelihatan sama",
                    "sekali, kepekatannya terpaksa dinaikkan sampai berubah jadi lingkaran abu-abu",
                    "kotor di belakang kartu. Dua lapis tipis tetap ringan dan tetap terbaca.",
                    "",
                    "BOX-SHADOW TIDAK MEMAKAN RUANG - DAN ITU BUKAN DETAIL KECIL",
                    "",
                    "Bayangan tidak ikut dihitung dalam lebar dan tinggi elemen, dan tidak mendorong",
                    "satu pun tetangganya. Menambahkannya tidak pernah menggeser tata letak.",
                    "",
                    "Bandingkan dengan border. Kalau penanda fokus dibuat dari border: 2px, elemennya",
                    "bertambah 2px di keempat sisi setiap kali difokus, dan seluruh baris di",
                    "sekitarnya ikut bergeser - halamannya terlihat berkedut tiap kali kamu menekan",
                    "Tab. Dengan box-shadow tidak ada yang bergerak sedikit pun.",
                    "",
                    "Karena itu cincin fokus modern sering dibuat begini - kabur 0, sebar 3px:",
                    "",
                    "  box-shadow: 0 0 0 3px rgba(26, 79, 160, 0.45);",
                    "",
                    "Nol geser, nol kabur, jadi yang tergambar bukan bayangan melainkan CINCIN rapi",
                    "selebar 3px yang mengikuti border-radius elemennya. (Cara satunya, outline,",
                    "dibahas di materi Pseudo-class dan Pseudo-element; keduanya sama-sama tidak",
                    "memakan ruang.) Satu catatan: cincin dari box-shadow ikut hilang di mode kontras",
                    "tinggi sistem operasi, jadi kode sungguhan biasanya menyertakan juga baris",
                    "outline: 2px solid transparent - baris yang kelihatan tidak berguna itu justru",
                    "yang menyelamatkan penanda fokusnya di sana.",
                    "",
                    "TANGGA ELEVASI: SEPAKATI TIGA TINGKAT, JANGAN MENGARANG ANGKA BARU",
                    "",
                    "Godaan terbesarnya adalah mengetik angka baru tiap kali membuat komponen: 0 3px",
                    "7px di kartu, 0 4px 9px di dialog, 0 2px 6px di tombol. Setelah sepuluh kali,",
                    "tidak ada dua benda yang benar-benar sejajar tingginya, dan mata membaca itu",
                    "sebagai halaman yang berantakan tanpa bisa menunjuk sebabnya.",
                    "",
                    "Bayangan adalah cara halaman menyatakan JARAK dari permukaan. Kalau jaraknya",
                    "cuma boleh tiga - menempel, terangkat sedikit, mengambang jauh - maka",
                    "bayangannya juga cuma boleh tiga. Simpan sebagai variabel (materi Variabel CSS",
                    "dan Cara Menata Berkas Gaya) persis seperti tangga jarak --s1 sampai --s6:",
                    "satu tempat untuk mengatur seluruh kedalaman halaman.",
                ],
            },
            {
                "heading": "Tangga elevasi, cincin fokus, dan kotak cekung (gaya.css)",
                "code": """/* Tiga tingkat saja, disepakati sekali di sini */
:root {
  --bayang-1: 0 1px 2px rgba(0, 0, 0, 0.06), 0 1px 3px rgba(0, 0, 0, 0.10);
  --bayang-2: 0 2px 4px rgba(0, 0, 0, 0.06), 0 6px 16px rgba(0, 0, 0, 0.12);
  --bayang-3: 0 12px 32px rgba(0, 0, 0, 0.20);
}

.kartu {
  background: white;
  border-radius: 10px;
  padding: 20px;
  box-shadow: var(--bayang-1);
}

/* Terangkat sedikit saat disentuh: naik satu anak tangga, bukan angka baru */
.kartu:hover {
  box-shadow: var(--bayang-2);
}

/* Dialog paling jauh dari halaman, jadi tingkat paling tinggi */
.dialog {
  border-radius: 14px;
  box-shadow: var(--bayang-3);
}

/* Cincin fokus: geser 0, kabur 0, sebar 3px. Tidak menggeser apa pun. */
.tombol:focus-visible {
  outline: 2px solid transparent;   /* penyelamat di mode kontras tinggi */
  outline-offset: 2px;
  box-shadow: 0 0 0 3px rgba(26, 79, 160, 0.45);
}

/* inset = cekung. Kotak isian terlihat seperti lubang tempat teks masuk. */
.isian {
  border: 1px solid #cfd3da;
  border-radius: 6px;
  padding: 8px 10px;
  box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.10);
}

/* Ditekan: bayangan luar dimatikan, diganti bayangan dalam */
.tombol:active {
  box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.25);
}""",
            },
            {
                "body": [
                    "text-shadow: SAUDARA YANG LEBIH PENDEK",
                    "",
                    "  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.55);",
                    "",
                    "Bentuknya sama, tapi hanya TIGA angka: geser-x, geser-y, kabur, lalu warna.",
                    "Tidak ada sebar, tidak ada inset - keduanya tidak masuk akal untuk huruf.",
                    "Beberapa bayangan sekaligus tetap boleh, dipisah koma seperti box-shadow.",
                    "",
                    "Gunanya satu dan jelas: teks di atas foto. Foto punya bagian terang dan bagian",
                    "gelap, jadi warna teks apa pun akan lenyap di salah satunya. Bayangan tipis",
                    "memberi huruf tepi gelapnya sendiri sehingga tetap terbaca di mana pun ia jatuh.",
                    "",
                    "Jangan berlebihan. Bayangan tebal pada teks isi membuat huruf terlihat kabur dan",
                    "melelahkan dibaca - persoalan kontras yang sama dengan di materi Warna dan",
                    "Satuan. Untuk teks panjang di atas foto, cara yang lebih baik adalah",
                    "menggelapkan fotonya (lapisan hitam tembus pandang di atasnya), bukan menebalkan",
                    "bayangan tiap hurufnya.",
                    "",
                    "filter: MENGOLAH TAMPILAN ELEMEN SEBELUM DIGAMBAR",
                    "",
                    "  filter: blur(4px);         mengaburkan elemen ITU beserta seluruh isinya",
                    "  filter: grayscale(100%);   0% apa adanya, 100% hitam-putih penuh",
                    "  filter: brightness(1.2);   1 apa adanya, di bawah 1 gelap, di atas 1 terang",
                    "  filter: contrast(0.8);     1 apa adanya, 0 membuat semuanya abu rata",
                    "  filter: saturate(1.4);     pekat-tidaknya warna; saturate(0) = grayscale(1)",
                    "  filter: invert(100%);      warna dibalik, seperti klise foto",
                    "  filter: drop-shadow(0 2px 3px rgba(0, 0, 0, 0.35));",
                    "",
                    "Nilai persen dan angka biasa sama saja: 100% = 1, 50% = 0.5. blur() satu-satunya",
                    "yang menuntut satuan panjang (4px), bukan persen.",
                    "",
                    "BEBERAPA FUNGSI DIRANGKAI DALAM SATU NILAI, DIPISAH SPASI:",
                    "",
                    "  filter: grayscale(100%) brightness(1.1);",
                    "",
                    "Dikerjakan dari kiri ke kanan, jadi urutannya berpengaruh. Dan inilah jebakan",
                    "yang menggigit hampir semua orang sekali:",
                    "",
                    "  .foto { filter: grayscale(100%); filter: blur(2px); }",
                    "",
                    "Yang berlaku cuma blur. filter itu SATU properti, jadi deklarasi kedua menimpa",
                    "yang pertama seutuhnya - persis aturan cascade di materi Pemilih. Kalau",
                    "keduanya diinginkan, tulis dalam satu baris dipisah spasi.",
                    "",
                    "Dua sifat blur() yang perlu diketahui: ia mengaburkan TEKS di dalamnya juga",
                    "(itu memang gunanya untuk isi di balik dialog), dan tepinya ikut memudar",
                    "sehingga elemennya terlihat sedikit menyusut.",
                    "",
                    "drop-shadow() VERSUS box-shadow - INI BEDA YANG SUNGGUHAN",
                    "",
                    "  box-shadow      selalu mengikuti KOTAK elemennya (dan border-radius-nya)",
                    "  drop-shadow()   mengikuti BENTUK yang benar-benar tergambar",
                    "",
                    "Untuk sebuah logo PNG atau SVG berlatar tembus pandang, box-shadow menggambar",
                    "bayangan PERSEGI di sekeliling gambarnya - termasuk di daerah yang kosong,",
                    "sehingga terlihat seperti logonya ditempel di atas kartu abu-abu. drop-shadow()",
                    "hanya membayangi piksel yang benar-benar ada, jadi bayangan logo berbentuk",
                    "bintang ikut berbentuk bintang. Bentuk nilainya sama dengan text-shadow: tiga",
                    "angka dan warna, TANPA sebar.",
                    "",
                    "backdrop-filter: MENYARING YANG ADA DI BELAKANG",
                    "",
                    "  backdrop-filter: blur(12px);",
                    "",
                    "filter mengolah elemennya sendiri; backdrop-filter mengolah apa pun yang",
                    "kebetulan berada DI BELAKANGNYA. Ini yang membuat bilah kepala dan kartu",
                    "terlihat seperti kaca buram: isinya tetap tajam, yang buram halaman di baliknya.",
                    "",
                    "SATU JEBAKAN, DAN HAMPIR SEMUA ORANG KENA:",
                    "",
                    "Kalau latar elemennya PENUH (background: white), tidak akan terjadi apa-apa yang",
                    "terlihat - kamu memang mengaburkan sesuatu, tapi hasilnya tertutup rapat oleh",
                    "latar elemen itu sendiri. Latarnya wajib tembus pandang sebagian:",
                    "",
                    "  background: rgba(255, 255, 255, 0.72);",
                    "",
                    "Safari versi lama hanya mengenal bentuk berawalan -webkit-backdrop-filter, dan",
                    "kode nyata masih menulis keduanya - yang berawalan lebih dulu. Soal awalan",
                    "vendor ada materinya sendiri nanti.",
                    "",
                    "Dan satu peringatan biaya: blur - apalagi backdrop-filter di area lebar - adalah",
                    "salah satu hal termahal yang bisa diminta dari browser. Untuk satu bilah kepala",
                    "tidak masalah; untuk sesuatu yang bergerak atau berukuran selayar penuh, siap-",
                    "siap melihat animasinya tersendat di komputer yang tidak kencang.",
                ],
            },
            {
                "heading": "Kaca buram, teks di atas foto, dan bayangan berbentuk (gaya.css)",
                "body": [
                    "SATU KELUARGA: opacity, filter, DAN transform",
                    "",
                    "Ketiganya kelihatan tidak berhubungan, tapi punya satu efek samping yang sama",
                    "dan mahal: elemen yang punya salah satunya membuat STACKING CONTEXT baru -",
                    "semacam ruang tumpuk tersendiri. backdrop-filter juga. Akibatnya dua:",
                    "",
                    "  1. z-index anak-anaknya hanya dibandingkan DI DALAM ruang itu. Anak",
                    "     ber-z-index 9999 di dalam induk ber-filter tetap tidak bisa naik melewati",
                    "     saudara induknya. Yang perlu dinaikkan induknya, bukan anaknya.",
                    "  2. Anak ber-position: fixed berhenti mengacu ke JENDELA dan mulai mengacu ke",
                    "     elemen ber-filter itu. Dialog yang seharusnya menutupi layar mendadak",
                    "     terkurung di dalam sebuah kartu.",
                    "",
                    "Tidak ada pesan error untuk keduanya, dan penyebabnya jauh dari gejalanya -",
                    "yang rusak z-index sebuah tombol, yang salah satu baris filter di kakeknya.",
                    "Materi Position akan menyebut aturan ini lagi saat membahas z-index; sekarang",
                    "kamu sudah kenal propertinya, jadi kalimat itu tidak lagi berupa hafalan.",
                ],
                "code": """/* Bilah kepala kaca buram. Latarnya WAJIB tidak penuh. */
.kepala {
  position: sticky;
  top: 0;
  background: rgba(255, 255, 255, 0.72);
  -webkit-backdrop-filter: blur(12px);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid rgba(0, 0, 0, 0.08);
}

/* Judul di atas foto: tepi gelap tipis supaya huruf tidak lenyap */
.sampul h1 {
  color: white;
  text-shadow: 0 1px 3px rgba(0, 0, 0, 0.55);
}

/* Dua fungsi dirangkai dengan SPASI, bukan dua baris filter terpisah */
.thumb {
  filter: grayscale(100%) contrast(1.05);
}

.thumb:hover {
  filter: none;
}

/* Bayangan mengikuti bentuk logo, bukan kotak persegi di sekelilingnya */
.logo {
  filter: drop-shadow(0 2px 3px rgba(0, 0, 0, 0.35));
}

/* Isi di balik dialog: kabur dan diredupkan sekaligus */
.halaman-terkunci {
  filter: blur(3px) brightness(0.85);
}""",
            },
        ],
    },
    {
        "title": "11. Transform: Menggeser, Memutar, dan Menskala",
        "sections": [
            {
                "body": [
                    "transform mengambil elemen yang SUDAH selesai ditata browser, lalu",
                    "menggambar ulang gambarnya: digeser, diputar, dimiringkan, atau",
                    "diperbesar.",
                    "",
                    "Kata kuncinya 'sudah selesai ditata'. Penataan halaman berjalan lebih",
                    "dulu dan berakhir; transform bekerja sesudahnya, di atas hasil itu.",
                    "",
                    "Akibatnya cuma satu kalimat, tapi kalimat itu yang membedakannya dari",
                    "semua yang sudah kamu pelajari: TEMPAT YANG SUDAH DIPESAN ELEMEN ITU",
                    "DI ALUR TIDAK BERUBAH SEDIKIT PUN. Tetangganya tidak bergeser, tidak",
                    "ada yang turun sebaris, tinggi induknya tetap sama.",
                    "",
                    "  margin-top: -20px",
                    "      menaikkan elemennya DAN menarik semua yang di bawahnya ikut",
                    "      naik. Seluruh halaman ditata ulang.",
                    "",
                    "  transform: translateY(-20px)",
                    "      menaikkan gambarnya saja. Tetangganya tidak tahu apa-apa dan",
                    "      tidak bergerak semilimeter pun.",
                    "",
                    "Bandingkan juga dengan position: relative + top, yang dibahas di materi",
                    "Position. Keduanya sama-sama tetap memesan tempat asalnya, jadi",
                    "hasilnya sekilas mirip. Empat bedanya:",
                    "  - relative WAJIB mengubah position lebih dulu; transform berlaku",
                    "    pada elemen static biasa tanpa syarat apa pun.",
                    "  - top/left hanya bisa menggeser. transform juga bisa memutar,",
                    "    menskala, dan memiringkan - dan tidak ada properti lain yang bisa.",
                    "  - Persennya dihitung dari hal yang BERBEDA. Ini jebakan tersendiri,",
                    "    dibahas di bagian berikutnya.",
                    "  - transform jauh lebih murah untuk digerakkan. Alasannya di bagian",
                    "    terakhir materi ini.",
                    "",
                    "Semua fungsinya ditulis di SATU properti, dipisah spasi:",
                    "",
                    "  transform: translateY(-2px) scale(1.05) rotate(3deg);",
                    "",
                    "JEBAKAN YANG PALING BANYAK MEMBUANG WAKTU DI AWAL",
                    "",
                    "transform TIDAK BERLAKU pada elemen display: inline. <span>, <a>, dan",
                    "<em> yang masih polos tidak bergerak sedikit pun, dan seperti biasa",
                    "CSS tidak berkata apa-apa. Ini kembaran persis dari 'kenapa width",
                    "pada <span> saya tidak berpengaruh' di materi Display dan Alur",
                    "Dokumen, dan obatnya juga sama: beri display: inline-block dulu.",
                    "",
                    "Yang membuatnya makin licin: DevTools tetap MENAMPILKAN transform-nya",
                    "seolah berlaku, lengkap dengan nilainya. Yang tidak dilakukan browser",
                    "cuma menggerakkan elemennya. Jadi jangan percaya bahwa sebuah aturan",
                    "bekerja hanya karena ia terbaca di panel gaya - percayalah pada apa",
                    "yang bergerak di layar.",
                ],
            },
            {
                "body": [
                    "translate: MENGGESER",
                    "",
                    "  transform: translateX(20px);       ke kanan 20px",
                    "  transform: translateY(-8px);       ke ATAS 8px",
                    "  transform: translate(20px, -8px);  dua sekaligus, x dulu baru y",
                    "  transform: translate(20px);        y dianggap 0",
                    "",
                    "Sumbu Y menghitung ke BAWAH sebagai positif, sama seperti di seluruh",
                    "CSS. Jadi translateY(10px) menurunkan, bukan menaikkan.",
                    "",
                    "JEBAKAN PERSENNYA - ini beda dari hampir semua properti CSS lain:",
                    "",
                    "  width: 50%                  -> setengah lebar INDUKNYA",
                    "  left: 50%                   -> setengah lebar ACUANNYA, yaitu leluhur",
                    "                                 positioned terdekatnya",
                    "  transform: translateX(50%)  -> setengah lebar ELEMEN ITU SENDIRI",
                    "",
                    "translateX(100%) berarti 'geser sejauh persis satu badanmu sendiri' -",
                    "berapa pun lebar induknya, dan tanpa kamu perlu tahu lebar elemennya.",
                    "Itu sebabnya panel geser hampir selalu ditulis begini: translateX(-100%)",
                    "menyimpannya persis di sebelah kiri tepi layar, translateX(0)",
                    "memunculkannya kembali. Tidak ada satu angka piksel pun yang harus",
                    "diperbarui kalau lebar panelnya berubah besok.",
                    "",
                    "IDIOM YANG AKAN KAMU TEMUI SEUMUR HIDUP: MEMUSATKAN SESUATU",
                    "",
                    "  .dialog {",
                    "    position: fixed;",
                    "    top: 50%;",
                    "    left: 50%;",
                    "    transform: translate(-50%, -50%);",
                    "  }",
                    "",
                    "Baca dua langkahnya pelan-pelan:",
                    "",
                    "  1. top: 50% dan left: 50% menaruh POJOK KIRI ATAS elemen tepat di",
                    "     titik tengah. Persennya milik acuannya. Hasilnya elemen terlihat",
                    "     melenceng ke kanan bawah - dan makin besar elemennya, makin jauh",
                    "     melencengnya.",
                    "  2. translate(-50%, -50%) menariknya mundur setengah LEBARNYA SENDIRI",
                    "     dan setengah TINGGINYA SENDIRI. Sekarang titik tengah elemen yang",
                    "     duduk di titik tengah acuannya.",
                    "",
                    "Kenapa tidak margin-left: -150px saja, seperti cara lama? Karena angka",
                    "itu mengharuskan kamu tahu lebar elemennya, dan begitu isinya berubah",
                    "satu baris, letaknya meleset lagi. Persen di translate tidak pernah",
                    "perlu dihitung ulang - itulah seluruh alasan idiom ini ada.",
                    "",
                    "Untuk memusatkan sesuatu yang masih ikut alur, flexbox atau grid lebih",
                    "tepat dan jauh lebih mudah dibaca. Idiom translate ini dipakai justru",
                    "saat elemennya SUDAH keluar dari alur - dialog, tooltip, lencana -",
                    "yaitu saat flex tidak punya pegangan apa-apa lagi padanya.",
                ],
            },
            {
                "body": [
                    "scale: MEMBESARKAN DAN MENGECILKAN",
                    "",
                    "  transform: scale(1.05);     105% ke segala arah",
                    "  transform: scale(2, 0.5);   lebar dua kali, tinggi setengah",
                    "  transform: scaleX(1.2);     melebar saja, tinggi tetap",
                    "  transform: scaleY(0.5);     memendek saja, lebar tetap",
                    "  transform: scaleX(-1);      cermin: kiri jadi kanan",
                    "",
                    "Angkanya PENGALI, bukan ukuran. 1 berarti apa adanya, 0.5 setengah,",
                    "0 menghilang jadi setitik. Tidak ada satuannya: scale(2px) itu salah",
                    "dan dibuang diam-diam.",
                    "",
                    "Yang membesar BUKAN cuma kotaknya. Teksnya ikut membesar, garis",
                    "tepinya ikut menebal, bayangannya ikut melebar, sudut membulatnya ikut",
                    "melar. scale terasa seperti memperbesar FOTO elemennya, bukan seperti",
                    "mengubah width dan height. Karena yang diperbesar adalah hasil",
                    "gambarnya, pada pengali besar teks bisa terlihat kasar.",
                    "",
                    "rotate: MEMUTAR",
                    "",
                    "  transform: rotate(45deg);    45 derajat searah jarum jam",
                    "  transform: rotate(-90deg);   berlawanan arah jarum jam",
                    "  transform: rotate(0.25turn); seperempat putaran, sama dengan 90deg",
                    "",
                    "  Satuannya WAJIB. rotate(45) tanpa deg diabaikan tanpa sepatah kata,",
                    "  dan kamu akan mengira transform-nya yang rusak.",
                    "  turn sering lebih enak dibaca: 1turn = 360deg. Ada juga rad dan",
                    "  grad, tapi jarang sekali dipakai orang.",
                    "",
                    "skew: MEMIRINGKAN",
                    "",
                    "  transform: skewX(-10deg);   memiringkan seperti huruf miring",
                    "  transform: skewY(4deg);     memiringkan sumbu tegaknya",
                    "",
                    "  Dipakai untuk hiasan - pita diskon, garis serong di latar. Hindari",
                    "  pada teks: hurufnya ikut diperas dan jadi lebih sulit dibaca.",
                    "",
                    "transform-origin: TITIK JANGKAR SEMUA GERAKAN ITU",
                    "",
                    "Setiap putaran dan setiap skala punya satu titik yang tidak ikut",
                    "bergerak. Bawaannya titik tengah elemen - center center, sama artinya",
                    "dengan 50% 50%.",
                    "",
                    "  transform-origin: left top;       pojok kiri atas",
                    "  transform-origin: bottom center;  tengah sisi bawah",
                    "  transform-origin: 0 100%;         sama dengan left bottom",
                    "",
                    "Pintu berayun dari engselnya: transform-origin: left center. Jarum jam",
                    "berputar dari pangkalnya: transform-origin: bottom center. Pita yang",
                    "berputar dari POJOK butuh transform-origin: left top. Tanpa baris",
                    "itu ketiganya berputar mengelilingi titik tengahnya sendiri dan",
                    "terlihat seperti melayang, bukan berengsel.",
                    "",
                    "transform-origin juga mengubah ARAH scale. Dengan left top, elemen",
                    "membesar ke kanan dan ke bawah saja; dengan bawaannya, ia melebar",
                    "merata ke empat penjuru.",
                ],
            },
            {
                "heading": "Dua aturan penulisan, lalu polanya di berkas nyata",
                "body": [
                    "ATURAN 1: URUTAN FUNGSINYA BERPENGARUH, DIBACA KIRI KE KANAN",
                    "",
                    "  transform: translateX(50px) rotate(45deg);",
                    "      geser 50px ke kanan dulu, baru putar di tempat barunya.",
                    "",
                    "  transform: rotate(45deg) translateX(50px);",
                    "      putar dulu. Sumbu elemennya ikut miring 45 derajat, jadi",
                    "      geseran 50px sesudahnya berjalan MIRING ke kanan bawah,",
                    "      bukan mendatar.",
                    "",
                    "Keduanya sah dan keduanya memberi hasil berbeda. Kalau elemenmu",
                    "mendarat di tempat aneh setelah kamu menambahkan rotate, hal pertama",
                    "yang dicurigai adalah urutannya, bukan angkanya.",
                    "",
                    "ATURAN 2: transform DI DUA ATURAN TIDAK MENUMPUK",
                    "",
                    "  .ikon       { transform: rotate(45deg); }",
                    "  .ikon.besar { transform: scale(1.5); }     <- rotate-nya HILANG",
                    "",
                    "transform itu SATU properti dengan SATU nilai, persis seperti color.",
                    "Aturan yang menang menimpa seluruh nilainya, bukan menambahinya.",
                    "",
                    "Ini menggigit paling sering di :hover. Aturan dasar sudah menulis",
                    "rotate(-1deg), lalu aturan hover-nya cuma menulis scale(1.02) - dan",
                    "kartunya mendadak lurus setiap kali disentuh. Yang terlihat seolah",
                    "'ada aturan lain yang ikut jalan', padahal cuma penimpaan biasa.",
                    "",
                    "Obatnya: tulis ULANG semua fungsi yang masih kamu inginkan.",
                    "",
                    "  .kartu:hover { transform: rotate(-1deg) scale(1.02); }",
                    "",
                    "CSS masa kini juga punya properti terpisah translate, rotate, dan",
                    "scale yang berdiri sendiri dan tidak saling menimpa. Bagus untuk kode",
                    "baru, tapi transform-lah yang akan kamu baca di hampir semua berkas",
                    "yang sudah ada - jadi bentuk inilah yang wajib kamu kuasai dulu.",
                    "",
                    "Contoh di bawah belum bergerak halus: perubahannya melompat seketika.",
                    "Yang menghaluskannya properti lain, transition, dan itu punya materi",
                    "sendiri: Transisi dan Animasi.",
                ],
                "code": """/* Tombol yang terangkat 2px saat disentuh, tertekan saat diklik */
.tombol {
  padding: 10px 18px;
  border: 0;
  border-radius: 8px;
  background: #1a4fa0;
  color: white;
}

.tombol:hover {
  transform: translateY(-2px);
}

.tombol:active {
  transform: translateY(1px);
}

/* Kartu yang sengaja dibuat sedikit miring.
   rotate WAJIB ditulis ulang di :hover - tanpa itu scale menimpanya
   dan kartunya jadi lurus setiap kali disentuh. */
.kartu {
  transform: rotate(-1deg);
}

.kartu:hover {
  transform: rotate(-1deg) scale(1.02);
}

/* Dipusatkan tanpa perlu tahu lebar maupun tingginya */
.dialog {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: min(90vw, 420px);
  padding: 24px;
  border-radius: 12px;
  background: white;
}

/* Panel yang menunggu persis di luar tepi kiri layar */
.panel {
  position: fixed;
  top: 0;
  left: 0;
  width: 260px;
  height: 100vh;
  transform: translateX(-100%);
}

.panel.terbuka {
  transform: translateX(0);
}

/* Panah yang berputar 90 derajat saat bagiannya dibuka */
.pemicu .panah {
  display: inline-block;   /* elemen inline tidak bisa di-transform */
}

.pemicu[aria-expanded="true"] .panah {
  transform: rotate(90deg);
}

/* Jarum yang berputar dari pangkalnya, bukan dari titik tengahnya */
.jarum {
  transform-origin: bottom center;
  transform: rotate(0.25turn);
}""",
            },
            {
                "body": [
                    "TIGA EFEK SAMPING YANG WAJIB DIINGAT",
                    "",
                    "Elemen yang punya transform - nilai apa pun selain none - berubah",
                    "WATAKNYA, bukan cuma penampilannya.",
                    "",
                    "1. IA MEMBUAT STACKING CONTEXT BARU.",
                    "   Inilah yang dimaksud kalimat menggantung di materi Position: 'induk",
                    "   ber-opacity kurang dari 1, ber-transform, atau ber-filter membuat",
                    "   konteks baru'. Begitu sebuah kartu diberi scale(1.02) saat",
                    "   di-hover, seluruh isinya terkurung di dalamnya: tooltip di dalam",
                    "   kartu itu, meski ber-z-index 9999, tetap tidak bisa muncul di atas",
                    "   kartu sebelahnya. Gejalanya khas dan membingungkan: 'z-index-nya",
                    "   jalan, sampai saya menambahkan efek hover'.",
                    "",
                    "2. IA JADI ACUAN BAGI ANAK ber-position: fixed.",
                    "   fixed seharusnya berpatokan pada JENDELA dan tidak ikut bergulir.",
                    "   Tapi kalau ada leluhurnya yang ber-transform, patokannya pindah ke",
                    "   elemen itu - dan fixed-nya ikut bergulir seperti absolute biasa.",
                    "   Ini penyebab 'dialog fixed saya bergerak saat halaman digulir' yang",
                    "   sangat sulit dilacak, karena sumbernya ada di elemen LAIN beberapa",
                    "   tingkat di atasnya, sering ditulis orang lain, dan kelihatan tidak",
                    "   ada hubungannya. Anak ber-position: absolute juga ikut: leluhur",
                    "   ber-transform dihitung sebagai acuannya meski position-nya static.",
                    "",
                    "3. TEKS BISA SEDIKIT KABUR PADA NILAI PECAHAN.",
                    "   translateY(-0.5px) atau scale(1.03) membuat huruf mendarat di",
                    "   antara piksel, dan browser mengaburkannya sedikit supaya tetap",
                    "   terlihat halus. Pakai angka bulat kalau bisa. Kalau tidak bisa,",
                    "   itu harga yang dibayar dan biasanya tidak terasa pada gerakan",
                    "   sekejap.",
                    "",
                    "KENAPA transform DAN opacity DISEBUT DUA PROPERTI PALING MURAH",
                    "",
                    "Untuk menggambar halaman, browser mengerjakan tiga tahap berurutan:",
                    "menghitung tata letak (layout), mewarnai pikselnya (paint), lalu",
                    "menyusun lapisan-lapisannya jadi satu gambar (composite).",
                    "",
                    "  Mengubah width, height, top, margin  -> mengulang KETIGA tahapnya.",
                    "  Mengubah color atau background       -> mengulang paint + composite.",
                    "  Mengubah transform atau opacity      -> cukup composite saja.",
                    "",
                    "Tata letaknya memang tidak berubah sedikit pun - ingat kalimat pertama",
                    "materi ini. Itu sebabnya menggeser sesuatu dengan translateX terasa",
                    "halus, sementara menggeser hal yang sama dengan left terasa tersendat,",
                    "terutama di ponsel yang tenaganya kecil.",
                    "",
                    "Aturan praktisnya: kalau sesuatu harus BERGERAK, gerakkan transform",
                    "dan opacity-nya, bukan yang lain. Materi Transisi dan Animasi memakai",
                    "aturan ini dari awal sampai akhir.",
                    "",
                    "SEKILAS 3D - supaya tidak kaget saat membacanya di kode orang",
                    "",
                    "  perspective: 800px    Ditulis di INDUKNYA. Sejauh apa mata",
                    "                        dibayangkan berdiri dari layar. Tanpa ini,",
                    "                        putaran 3D terlihat rata seperti diperas.",
                    "  rotateX() rotateY()   Memutar pada sumbu mendatar / tegak, jadi",
                    "                        elemennya seperti dimiringkan menjauh.",
                    "  translateZ(40px)      Mendekat ke arah mata.",
                    "  transform-style: preserve-3d",
                    "                        Di induk, supaya anak-anaknya berada di ruang",
                    "                        3D yang sama alih-alih digepengkan dulu.",
                    "  backface-visibility: hidden",
                    "                        Sembunyikan punggung elemen saat ia berbalik",
                    "                        lebih dari 90 derajat.",
                    "",
                    "Semua itu cuma dipakai untuk kartu yang membalik dan efek sejenisnya.",
                    "Yang perlu kamu simpan sekarang satu saja: kalau melihat rotateY di",
                    "sebuah berkas, cari perspective di induknya - kalau tidak ada, itulah",
                    "sebabnya efeknya terlihat aneh.",
                ],
            },
        ],
    },
    {
        "title": "12. Memotong dan Membungkus Teks",
        "sections": [
            {
                "body": [
                    "Judul kartu yang kepanjangan adalah persoalan harian, dan CSS memang bisa memotongnya",
                    "lalu menuliskan titik-titik di ujungnya sendiri. Tapi bukan dengan satu properti -",
                    "perlu TIGA, dan ketiganya wajib ada BERSAMAAN:",
                    "",
                    "  .judul {",
                    "    white-space: nowrap;      /* 1. larang teksnya turun baris   */",
                    "    overflow: hidden;         /* 2. potong yang keluar kotak     */",
                    "    text-overflow: ellipsis;  /* 3. gambar ... di ujung potongan */",
                    "  }",
                    "",
                    "Kenapa tiga? Karena masing-masing mengerjakan langkah yang berbeda, dan text-overflow",
                    "justru yang paling tidak berkuasa di antara ketiganya: ia tidak memotong apa pun. Ia",
                    "cuma menghias potongan yang SUDAH dibuat dua properti sebelumnya.",
                    "",
                    "Hilang satu saja, titik-titiknya tidak muncul sama sekali:",
                    "",
                    "  Tanpa white-space: nowrap",
                    "    Teksnya turun baris seperti biasa. Karena tidak ada yang meluber ke samping, tidak",
                    "    ada yang perlu dipotong - dan tidak ada tempat untuk menaruh titik-titiknya.",
                    "",
                    "  Tanpa overflow: hidden",
                    "    Kelebihannya tetap tergambar keluar kotak apa adanya - itu overflow: visible, yang",
                    "    sudah kamu lihat di 'Display dan Alur Dokumen'. Tidak ada yang disembunyikan, jadi",
                    "    tidak ada yang perlu ditandai.",
                    "",
                    "  Tanpa text-overflow: ellipsis",
                    "    Teksnya terpotong tepat di tengah huruf, tanpa tanda apa pun. Pembaca tidak punya",
                    "    cara untuk tahu bahwa masih ada lanjutannya.",
                    "",
                    "Ada satu syarat lagi yang tidak kelihatan di ketiga baris itu: ELEMENNYA HARUS PUNYA",
                    "BATAS LEBAR. Kotak yang bebas melebar mengikuti isinya tidak pernah kepenuhan, jadi",
                    "tidak pernah ada yang meluber. Ini penyebab paling sering dari keluhan 'ketiganya",
                    "sudah saya tulis, kok titiknya tidak muncul': judul itu duduk di dalam item flex atau",
                    "sel grid yang ikut melebar mengikuti isinya (gejala yang sudah disebut di 'Flexbox'",
                    "dan 'Grid'). Obatnya min-width: 0 - dipasang di elemen yang tepat, dan bagian terakhir",
                    "materi ini menunjukkan yang mana.",
                ],
            },
            {
                "body": [
                    "MEMOTONG DI BARIS KE-N",
                    "",
                    "Trio di atas hanya bisa satu baris. Untuk ringkasan kartu, yang biasanya diinginkan",
                    "adalah 'tampilkan dua baris, sisanya titik-titik'. Resepnya empat properti, dan",
                    "bentuknya memang aneh:",
                    "",
                    "  .ringkasan {",
                    "    display: -webkit-box;",
                    "    -webkit-box-orient: vertical;",
                    "    -webkit-line-clamp: 2;",
                    "    overflow: hidden;",
                    "  }",
                    "",
                    "Awalan -webkit- itu BUKAN salah ketik, dan bukan pula berarti 'khusus Safari'. Ini",
                    "sisa dari rancangan flexbox lama yang sudah lama ditinggalkan, tapi terlanjur dipakai",
                    "di mana-mana sehingga Chrome, Firefox, Safari, dan Edge sama-sama tetap mendukungnya",
                    "sampai hari ini. Soal awalan vendor secara umum dibahas di 'CSS yang Bertahan'.",
                    "",
                    "Tugas tiap barisnya:",
                    "  display: -webkit-box     menyalakan model kotak lama itu; tanpa ini clamp diabaikan",
                    "  -webkit-box-orient       harus vertical, supaya barisnya disusun menurun",
                    "  -webkit-line-clamp: 2    berapa baris yang boleh terlihat",
                    "  overflow: hidden         membuang baris ketiga dan seterusnya",
                    "",
                    "Keempatnya benar-benar wajib. Hilangkan display: -webkit-box atau -webkit-box-orient,",
                    "dan clamp-nya diabaikan diam-diam - paragrafnya tampil utuh seperti tidak pernah kamu",
                    "atur. Hilangkan overflow: hidden, dan hasilnya lebih buruk lagi: kotaknya memang",
                    "menyusut jadi dua baris dan titik-titiknya tetap tergambar, TAPI baris sisanya ikut",
                    "tergambar juga - menimpa apa pun yang ada di bawahnya. Yang terlihat bukan potongan",
                    "rapi, melainkan teks bertumpuk.",
                    "",
                    "Dua jebakan yang pasti terjadi begitu kamu menggabung dua resep di halaman ini:",
                    "",
                    "1. JANGAN menambahkan white-space: nowrap pada elemen ber-line-clamp. Nowrap memaksa",
                    "   seluruh teks jadi satu baris, jadi 'potong di baris kedua' tidak pernah kesampaian",
                    "   dan yang terlihat cuma satu baris terpotong.",
                    "2. line-clamp menghitung BARIS, bukan huruf. Kartu yang lebih sempit atau font yang",
                    "   lebih besar mengubah berapa banyak kata yang terlihat. Itu memang tujuannya, tapi",
                    "   jangan berharap dua kartu berdampingan memotong di kata yang sama.",
                    "",
                    "Kalau kamu benar-benar tidak mau bergantung pada awalan, ada cara tumpul yang selalu",
                    "jalan: kunci saja tingginya.",
                    "",
                    "  .ringkasan { line-height: 1.5; max-height: 3em; overflow: hidden; }   /* 2 x 1.5em */",
                    "",
                    "Bedanya jelas dan harus kamu terima: tidak ada titik-titik, dan baris berikutnya bisa",
                    "terpotong separuh di tengah tingginya sehingga terlihat seperti huruf yang tergunting.",
                    "",
                    "Bentuk tanpa awalan, line-clamp, sedang distandarkan. Sampai ia benar-benar jalan di",
                    "mana-mana, bentuk -webkit- di atas yang aman - dan itu juga yang akan kamu temui di",
                    "kode orang lain.",
                ],
            },
            {
                "body": [
                    "NILAI white-space SELENGKAPNYA",
                    "",
                    "Properti ini mengatur dua hal sekaligus: apakah spasi berlebih di HTML diciutkan, dan",
                    "apakah teks boleh turun baris sendiri saat kepanjangan.",
                    "",
                    "  normal        spasi & ganti baris diciutkan jadi satu spasi; teks turun baris",
                    "                sendiri kalau kepanjangan   (bawaan)",
                    "  nowrap        spasi diciutkan, TAPI teks tidak pernah turun baris sendiri",
                    "  pre           spasi & ganti baris dipertahankan apa adanya; tidak turun sendiri",
                    "  pre-wrap      spasi & ganti baris dipertahankan, DAN masih turun baris sendiri",
                    "  pre-line      ganti baris dipertahankan, spasi berlebih tetap diciutkan",
                    "  break-spaces  seperti pre-wrap, spasi di ujung baris pun ikut dipertahankan",
                    "",
                    "Elemen <pre> memakai white-space: pre secara bawaan. Itulah sebabnya satu baris kode",
                    "yang panjang bisa melebar keluar layar. Dua jalan keluarnya, dan keduanya sah:",
                    "",
                    "  - biarkan pre, bungkus wadahnya dengan overflow-x: auto -> kodenya utuh, tinggal",
                    "    digeser ke samping (pola yang sudah dipakai di 'Display dan Alur Dokumen')",
                    "  - ganti ke pre-wrap -> tidak ada yang perlu digeser, tapi satu baris kode yang",
                    "    panjang akan terlihat seperti dua baris, dan itu bisa menyesatkan pembacanya",
                    "",
                    "Satu jebakan yang jarang disadari: white-space MENULAR ke seluruh keturunan (lihat",
                    "'Teks dan Font'). Memasang nowrap di sebuah wadah membuat SEMUA teks di dalamnya",
                    "menolak turun baris, bukan cuma judulnya - dan halaman yang tiba-tiba bisa digeser",
                    "ke samping sering berasal dari satu nowrap yang dipasang terlalu tinggi.",
                    "",
                    "TIGA CARA MEMBUAT KATA PANJANG MENYERAH",
                    "",
                    "URL, token, atau nama berkas tanpa spasi tidak bisa diturunkan browser: tidak ada",
                    "satu pun tempat yang boleh dipatahkan. Satu kata seperti itu di kartu sempit akan",
                    "menjebol kartunya dan sering menyeret seluruh halaman jadi bisa digeser ke samping -",
                    "gejala yang sudah dua kali disebut di 'Flexbox' dan 'Grid'. Ini obatnya.",
                    "",
                    "  overflow-wrap: break-word   Patahkan di tengah kata HANYA kalau kata itu tidak",
                    "                              muat sendirian di satu baris. Kata biasa tidak",
                    "                              tersentuh. Ini pilihan bawaan untuk hampir semua",
                    "                              kasus, dan karena ia menular, cukup dipasang sekali",
                    "                              di wadah teksnya.",
                    "  word-break: break-all       Patahkan di huruf mana saja begitu barisnya penuh,",
                    "                              untuk SEMUA kata. Teks Indonesia jadi tercabik-cabik",
                    "                              di tempat yang tidak masuk akal. Hampir tidak pernah",
                    "                              ini yang kamu maksud.",
                    "  hyphens: auto               Patahkan di batas suku kata dan tambahkan tanda",
                    "                              hubung. Butuh atribut lang di HTML (<html lang=\"id\">)",
                    "                              supaya browser tahu kamus mana yang dipakai - dan",
                    "                              kamusnya tidak tersedia untuk semua bahasa. Anggap",
                    "                              hiasan, bukan obat: URL panjang tidak tertolong",
                    "                              olehnya sama sekali.",
                    "",
                    "Nama lamanya word-wrap: break-word. Artinya persis sama dan masih banyak terlihat di",
                    "kode lama; kalau menemuinya, itu bukan properti lain.",
                    "",
                    "Ada saudara yang lebih galak: overflow-wrap: anywhere. Bedanya halus tapi penting -",
                    "cuma 'anywhere' yang ikut mengecilkan lebar MINIMUM elemennya. Dengan break-word,",
                    "sebuah kolom grid, item flex, atau kolom tabel bisa terlanjur dijatah selebar kata",
                    "terpanjang sebelum pemotongannya sempat berlaku, dan tata letaknya tetap melebar.",
                    "Jadi kalau break-word terasa tidak berpengaruh di dalam grid atau tabel, pasangkan",
                    "dengan min-width: 0 pada selnya, atau ganti ke anywhere.",
                ],
            },
            {
                "heading": "Empat perlakuan untuk teks yang kepanjangan (gaya.css)",
                "code": """/* Markup yang diandaikan:
 *   <article class="kartu">
 *     <div class="kartu-kepala">
 *       <div class="kartu-teks">
 *         <h3 class="kartu-judul" title="judul lengkapnya">Judul</h3>
 *         <p class="kartu-ringkas">Ringkasan beberapa kalimat</p>
 *       </div>
 *       <span class="lencana">Baru</span>
 *     </div>
 *     <pre class="kode">npm install</pre>
 *   </article>
 */

.kartu {
  width: 280px;
  padding: 16px;
  border: 1px solid #d7dae2;
  border-radius: 8px;
  font-family: system-ui, Arial, sans-serif;
}

/* Baris kepala: kolom teks boleh menyusut, lencana tidak */
.kartu-kepala {
  display: flex;
  align-items: flex-start;
  gap: 8px;
}

.kartu-teks {
  flex: 1;
  min-width: 0;             /* tanpa ini seluruh kartu yang melar */
}

.lencana {
  flex: none;               /* lencana ikut menyusut = tulisannya hilang */
  padding: 2px 8px;
  border-radius: 999px;
  background: #e7efff;
  font-size: 0.75rem;
}

/* 1. Judul: selalu satu baris, sisanya jadi titik-titik */
.kartu-judul {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  margin: 0;
  font-size: 1rem;
}

/* 2. Ringkasan: dipotong tepat di baris kedua */
.kartu-ringkas {
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 2;
  overflow: hidden;
  line-height: 1.5;
  margin: 8px 0 0;
  color: #4a4f5a;
}

/* 3. Blok kode: baris panjang turun sendiri, spasinya tetap utuh */
.kode {
  white-space: pre-wrap;
  overflow-wrap: break-word;
  margin: 12px 0 0;
  padding: 10px;
  border-radius: 6px;
  background: #f4f5f7;
  font-family: Consolas, "Courier New", monospace;
  font-size: 0.875rem;
}

/* 4. Tabel dengan satu kolom berisi URL panjang */
.tabel {
  width: 100%;
  table-layout: fixed;      /* lebar kolom ditentukan CSS, bukan isinya */
  border-collapse: collapse;
}

.tabel td {
  padding: 8px;
  border-bottom: 1px solid #e3e5ea;
  vertical-align: top;
}

.tabel .alamat {
  overflow-wrap: break-word;   /* URL boleh patah, tetap terbaca seluruhnya */
}

.tabel .berkas {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}""",
            },
            {
                "body": [
                    "MEMBACA ULANG CONTOH DI ATAS",
                    "",
                    "min-width: 0 duduk di .kartu-teks, BUKAN di judulnya - dan ini bagian yang paling",
                    "layak dimengerti pelan-pelan. Item flex punya batas menyusut otomatis sebesar isi",
                    "terlebarnya, tapi aturan itu hanya berlaku selama overflow-nya masih visible.",
                    "Judulnya sendiri sudah ber-overflow: hidden, jadi ia sudah boleh menyusut sampai nol",
                    "tanpa disuruh. Pembungkusnya lain cerita: overflow-nya visible dan isinya satu baris",
                    "panjang yang menolak dipatahkan, jadi tanpa min-width: 0 dialah yang memaksa baris",
                    "kepala melebar - judulnya tidak pernah terpotong dan lencananya terdorong keluar",
                    "kartu. Aturan yang sama berlaku untuk sel grid.",
                    "",
                    "flex: none pada .lencana - lencana yang ikut menyusut akan kehilangan tulisannya",
                    "sendiri. Dalam satu baris, tentukan siapa yang boleh mengalah: di sini kolom teksnya.",
                    "",
                    "table-layout: fixed pada .tabel - lebar kolom tabel biasanya ditentukan ISINYA. Satu",
                    "URL panjang di satu sel melebarkan kolomnya lebih dulu, sehingga apa pun yang kamu",
                    "tulis soal pemotongan tidak pernah kena. Dengan fixed, CSS yang menentukan lebarnya",
                    "duluan dan isinya yang menyesuaikan.",
                    "",
                    "BATAS text-overflow, SUPAYA TIDAK DICARI-CARI",
                    "",
                    "  - Hanya untuk teks SATU BARIS yang meluber. Pada paragraf yang turun baris, ia",
                    "    tidak melakukan apa-apa. Untuk banyak baris, pakai line-clamp.",
                    "  - Tidak bisa memotong di tengah teks, dan tidak bisa disuruh 'ambil 40 karakter",
                    "    pertama'. Berapa huruf yang muat ditentukan browser, bukan kamu. Kalau kamu",
                    "    butuh jumlah karakter yang pasti, itu pekerjaan JavaScript atau server.",
                    "  - Yang wajib sebenarnya bukan tepat kata 'hidden', melainkan overflow yang BUKAN",
                    "    visible. auto dan scroll pun menghasilkan titik-titik - tapi kotaknya sekalian",
                    "    jadi bisa digulir, dan menggulirnya tidak menampakkan sisa teksnya: yang",
                    "    digambar memang cuma sampai titik-titik itu. Untuk judul, hidden yang kamu mau.",
                    "  - Yang bertitik-titik adalah elemen yang MEMUAT teksnya. Memasang ketiganya di",
                    "    .kartu, padahal judulnya duduk di dalam <h3> di dalamnya, tidak berpengaruh -",
                    "    yang meluber si <h3>, dan dialah yang harus diberi ketiga properti itu.",
                    "",
                    "Terakhir, dan ini soal orang yang membaca: teks yang dipotong CSS tetap utuh di",
                    "HTML-nya. Ia masih bisa disalin dan tetap dibacakan pembaca layar - yang hilang cuma",
                    "tampilannya. Karena itu pasang title=\"judul lengkapnya\" pada elemen yang dipotong",
                    "supaya pemakai tetikus bisa melihatnya, dan jangan pernah memotong satu-satunya",
                    "tempat sebuah informasi muncul di halaman.",
                    "",
                    "URUTAN MEMERIKSA KALAU TITIKNYA TIDAK MUNCUL",
                    "  1. Teksnya memang lebih panjang dari kotaknya?",
                    "  2. white-space: nowrap ada? (untuk versi satu baris)",
                    "  3. overflow-nya hidden, bukan visible?",
                    "  4. Kotaknya punya batas lebar? Pembungkus di dalam flex/grid butuh min-width: 0,",
                    "     sel tabel butuh table-layout: fixed.",
                    "  5. Ketiganya terpasang di elemen yang benar-benar memuat teksnya, bukan di wadah?",
                ],
            },
        ],
    },
    {
        "title": "13. Flexbox",
        "sections": [
            {
                "body": [
                    "Flexbox menata anak-anak sebuah wadah dalam SATU dimensi: satu",
                    "baris, atau satu kolom. Kalau kamu butuh baris DAN kolom",
                    "sekaligus, itu tugas Grid (materi berikutnya).",
                    "",
                    "Semuanya dimulai dari satu baris di WADAHnya, bukan di anaknya:",
                    "",
                    "  .wadah { display: flex; }",
                    "",
                    "Sejak baris itu, semua anak LANGSUNG .wadah menjadi flex item dan",
                    "berjajar mendatar. Cucu-cucunya tidak ikut - flex hanya berlaku",
                    "satu tingkat ke bawah.",
                    "",
                    "DUA SUMBU, DAN INILAH YANG PALING MEMBINGUNGKAN",
                    "",
                    "  sumbu utama (main axis)   = arah flex-direction",
                    "  sumbu silang (cross axis) = tegak lurus terhadapnya",
                    "",
                    "  flex-direction: row (bawaan)  -> utama MENDATAR, silang MENURUN",
                    "  flex-direction: column        -> utama MENURUN, silang MENDATAR",
                    "",
                    "  justify-content mengatur sumbu UTAMA.",
                    "  align-items     mengatur sumbu SILANG.",
                    "",
                    "Artinya begitu kamu menulis flex-direction: column, justify-content",
                    "tiba-tiba mengatur atas-bawah dan align-items mengatur kiri-kanan.",
                    "Bukan propertinya yang berubah - SUMBUNYA yang berputar. Kalau",
                    "sebuah aturan flex terasa 'terbalik', hampir selalu ini sebabnya.",
                ]
            },
            {
                "body": [
                    "PROPERTI DI WADAH:",
                    "  display: flex;",
                    "  flex-direction: row | row-reverse | column | column-reverse;",
                    "  justify-content: flex-start | center | flex-end |",
                    "                   space-between | space-around | space-evenly;",
                    "  align-items: stretch | flex-start | center | flex-end | baseline;",
                    "  flex-wrap: nowrap | wrap;",
                    "  gap: 16px;   jarak antar item, tanpa margin sama sekali",
                    "",
                    "align-items: stretch adalah bawaannya - itu sebabnya kartu-kartu",
                    "dalam satu baris flex otomatis sama tinggi tanpa kamu minta.",
                    "",
                    "PROPERTI DI ITEM:",
                    "  flex-grow: 1;     boleh melar mengisi sisa ruang (bawaan 0)",
                    "  flex-shrink: 1;   boleh menyusut kalau ruang kurang (bawaan 1)",
                    "  flex-basis: auto; ukuran awal sebelum melar atau menyusut",
                    "  flex: 1;          ringkas dari '1 1 0' - bagi rata sisa ruangnya",
                    "  align-self: center;  menimpa align-items untuk satu item saja",
                    "  order: 2;         mengubah urutan tampilan",
                    "",
                    "Hati-hati dengan order: urutan BACA - yang dipakai pembaca layar",
                    "dan tombol Tab - tetap mengikuti HTML. Halaman yang tampilannya",
                    "berurutan 1-2-3 tapi Tab-nya melompat 1-3-2 membingungkan orang",
                    "yang tidak memakai tetikus. Kalau urutannya penting, ubah HTML-nya.",
                    "",
                    "PAKAI gap, BUKAN margin, untuk jarak antar item. margin harus",
                    "dihapus lagi di item terakhir (:last-child) supaya tidak ada",
                    "jarak menggantung di ujung; gap tidak pernah menaruh jarak di",
                    "ujung sama sekali.",
                ]
            },
            {
                "heading": "Pola flexbox yang paling sering dipakai",
                "code": """/* Bilah kepala: judul di kiri, menu di kanan */
.kepala {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 16px;
  padding: 12px 20px;
}

/* Deretan kartu yang turun sendiri di layar sempit */
.daftar-kartu {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

.daftar-kartu > .kartu {
  flex: 1 1 260px;    /* boleh melar, boleh menyusut, dasar 260px */
  min-width: 0;
}

/* Memusatkan isi, mendatar dan menurun sekaligus */
.tengah {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
}

/* Kolom yang mendorong tombolnya ke dasar kartu */
.kartu {
  display: flex;
  flex-direction: column;
}

.kartu .tombol {
  margin-top: auto;
}""",
            },
            {
                "body": [
                    "Tiga bagian contoh di atas yang layak dihafal:",
                    "",
                    "1. justify-content: space-between",
                    "   Item pertama menempel kiri, terakhir menempel kanan, sisanya",
                    "   dibagi rata di tengah. Ini cara membuat bilah kepala tanpa",
                    "   satu pun angka lebar.",
                    "",
                    "2. margin-top: auto pada item flex",
                    "   'auto' menyerap semua sisa ruang di sisi itu, jadi tombolnya",
                    "   terdorong ke dasar kartu berapa pun panjang teks di atasnya.",
                    "   Dengan cara yang sama, margin-left: auto mendorong satu item",
                    "   ke ujung kanan tanpa mengubah yang lain.",
                    "",
                    "3. flex: 1 1 260px",
                    "   Dibaca: boleh melar, boleh menyusut, dan mulai dari 260px.",
                    "   Digabung dengan flex-wrap: wrap, kartu-kartu itu menata diri",
                    "   sendiri di lebar layar apa pun.",
                    "",
                    "DUA JEBAKAN YANG PASTI KAMU TEMUI",
                    "",
                    "flex-wrap: nowrap adalah BAWAANNYA, dan itu berarti item akan",
                    "menyusut terus-menerus daripada turun ke baris berikutnya. Di",
                    "layar sempit, deretan kartu jadi pipih sampai tidak terbaca.",
                    "Hampir semua deretan kartu sebaiknya ber-flex-wrap: wrap.",
                    "",
                    "Flex item punya min-width: auto secara diam-diam, artinya",
                    "'jangan menyusut lebih kecil dari isi terlebarnya'. Satu blok",
                    "kode panjang atau satu kata yang tidak bisa dipotong di dalam",
                    "item bisa membuat seluruh baris - dan seluruh halaman - melebar",
                    "keluar layar. Obatnya min-width: 0 pada itemnya, dan itu sebabnya",
                    "baris itu ada di contoh tanpa terlihat melakukan apa-apa.",
                    "",
                    "Ada obat KEDUA yang menjawab sisi lain dari persoalan yang sama:",
                    "overflow-wrap: break-word pada teksnya. min-width: 0 mengizinkan",
                    "ITEMNYA menyusut lebih sempit dari isinya; overflow-wrap",
                    "mengizinkan KATANYA dipatahkan supaya isinya sendiri jadi lebih",
                    "sempit. Untuk satu kata sangat panjang atau satu URL tanpa spasi",
                    "kamu biasanya butuh keduanya sekaligus - dan kenapa break-word",
                    "kadang terasa tidak berpengaruh di dalam flex sudah dibahas di",
                    "materi Memotong dan Membungkus Teks.",
                ]
            },
        ],
    },
    {
        "title": "14. Grid",
        "sections": [
            {
                "body": [
                    "Grid menata dalam DUA dimensi sekaligus: kolom dan baris.",
                    "Aturannya juga ditulis di wadah:",
                    "",
                    "  .wadah { display: grid; }",
                    "",
                    "Menentukan kolom:",
                    "  grid-template-columns: 200px 200px 200px;   tiga kolom tetap",
                    "  grid-template-columns: 1fr 1fr 1fr;         tiga kolom sama lebar",
                    "  grid-template-columns: repeat(3, 1fr);      sama, ditulis ringkas",
                    "  grid-template-columns: 240px 1fr;           sisi tetap + isi melar",
                    "",
                    "fr adalah satuan khusus grid: 'satu bagian dari SISA ruang'.",
                    "Pada '2fr 1fr', kolom pertama dua kali lebar kolom kedua - setelah",
                    "gap dan kolom berukuran tetap dipotong lebih dulu. Karena",
                    "menghitung sisa, fr tidak pernah membuat grid meluber, sementara",
                    "'33.33%' tiga kali plus gap pasti meluber.",
                    "",
                    "  gap: 20px;              jarak antar sel",
                    "  row-gap / column-gap    kalau baris dan kolom perlu beda",
                    "",
                    "Baris biasanya tidak perlu ditentukan - grid membuatnya sendiri",
                    "sesuai jumlah item. Kalau perlu:",
                    "  grid-template-rows: auto 1fr auto;   kepala, isi melar, kaki",
                ]
            },
            {
                "body": [
                    "MENEMPATKAN ITEM",
                    "",
                    "  .lebar  { grid-column: span 2; }   ambil dua kolom",
                    "  .utama  { grid-column: 1 / 3; }    dari garis 1 sampai garis 3",
                    "  .tinggi { grid-row: span 2; }      ambil dua baris",
                    "",
                    "Perhatikan: yang dihitung GARIS, bukan kolom. Tiga kolom punya",
                    "EMPAT garis:",
                    "",
                    "  1     2     3     4",
                    "  |-----|-----|-----|",
                    "  | k1  | k2  | k3  |",
                    "  |-----|-----|-----|",
                    "",
                    "Jadi 'grid-column: 1 / 3' berarti dari garis 1 sampai garis 3 -",
                    "yaitu DUA kolom, bukan tiga. Ini sumber salah hitung paling umum",
                    "di grid. Kalau bingung, pakai bentuk 'span 2' yang tidak perlu",
                    "menghitung garis sama sekali.",
                    "",
                    "  grid-column: 1 / -1;   dari garis pertama sampai garis TERAKHIR,",
                    "                         berapa pun jumlah kolomnya",
                    "",
                    "RESPONSIF TANPA SATU PUN MEDIA QUERY",
                    "",
                    "  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));",
                    "",
                    "Dibaca: buat sebanyak mungkin kolom; tiap kolom minimal 240px dan",
                    "maksimal satu bagian sisa ruang. Layar lebar dapat empat kolom,",
                    "tablet dua, ponsel satu - semuanya diputuskan grid sendiri.",
                    "Satu baris ini menggantikan tiga blok @media.",
                    "",
                    "Beda auto-fit dan auto-fill: kalau itemnya sedikit, auto-fit",
                    "melebarkan yang ada sampai penuh; auto-fill menyisakan kolom",
                    "kosong di kanan. Untuk daftar kartu biasa, auto-fit yang kamu mau.",
                ]
            },
            {
                "heading": "Grid untuk kerangka halaman dan daftar kartu",
                "code": """/* Daftar kartu yang menata dirinya sendiri */
.papan {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 20px;
}

/* Satu kartu yang sengaja dibuat selebar dua kolom */
.papan .sorotan {
  grid-column: span 2;
}

/* Kerangka halaman dengan nama daerah */
.halaman {
  display: grid;
  grid-template-columns: 240px 1fr;
  grid-template-rows: auto 1fr auto;
  grid-template-areas:
    "kepala kepala"
    "sisi   isi"
    "kaki   kaki";
  gap: 16px;
  min-height: 100vh;
}

.kepala { grid-area: kepala; }
.sisi   { grid-area: sisi; }
.isi    { grid-area: isi; min-width: 0; }
.kaki   { grid-area: kaki; }""",
            },
            {
                "body": [
                    "grid-template-areas adalah bagian CSS yang paling jarang perlu",
                    "dijelaskan: tulisannya sudah berbentuk gambar tata letaknya.",
                    "Nama yang sama diulang berarti daerah itu melebar. Titik (.)",
                    "berarti sel kosong.",
                    "",
                    "Tiap baris harus punya jumlah nama yang sama, kalau tidak seluruh",
                    "aturannya dibuang tanpa pesan apa pun - dan halamanmu tiba-tiba",
                    "kembali menumpuk ke bawah.",
                    "",
                    "Keuntungan terbesarnya muncul di media query: untuk mengubah",
                    "seluruh tata letak jadi satu kolom di ponsel, kamu cukup menulis",
                    "ulang gambarnya, bukan memindahkan satu per satu elemennya.",
                    "",
                    "GRID ATAU FLEX?",
                    "",
                    "  - Menata KERANGKA halaman (kepala, sisi, isi, kaki): Grid.",
                    "  - Membariskan beberapa benda dalam satu baris atau kolom: Flex.",
                    "  - Peduli pada baris DAN kolom sekaligus, ingin semuanya lurus",
                    "    ke bawah dan ke samping: Grid.",
                    "  - Jumlah itemnya berubah-ubah dan kamu cuma ingin mereka rapi",
                    "    sebaris lalu turun sendiri: Flex.",
                    "",
                    "Bukan pilihan yang harus dipertahankan seumur hidup: keduanya",
                    "biasa bersarang. Grid untuk kerangka luar, flex untuk isi tiap",
                    "sel. Itu susunan yang paling sering dipakai di halaman sungguhan.",
                    "",
                    "Catatan kecil yang menyelamatkan: sel grid, sama seperti item",
                    "flex, butuh min-width: 0 kalau isinya bisa lebih lebar darinya.",
                    "Tanpa itu, satu tabel lebar di dalam .isi bisa melebarkan kolom",
                    "1fr melewati layar - dan seluruh halaman ikut bisa digeser.",
                ]
            },
        ],
    },
    {
        "title": "15. Perataan Lanjut dan Grid Implisit",
        "sections": [
            {
                "body": [
                    "Materi Flexbox memperkenalkan justify-content dan align-items. Ada",
                    "saudara ketiga yang jarang disebut orang, padahal ia yang menjelaskan",
                    "salah satu kebingungan terbesar di flexbox: align-content.",
                    "",
                    "  align-items    mengatur letak item DI DALAM barisnya sendiri",
                    "  align-content  mengatur letak dan jarak ANTAR baris",
                    "",
                    "align-content baru punya arti kalau barisnya LEBIH DARI SATU. Di wadah",
                    "flex tanpa flex-wrap: wrap - dan nowrap itu bawaannya - selamanya cuma",
                    "ada satu baris, jadi align-content tidak berbuat apa-apa sama sekali.",
                    "Menulisnya di situ tidak error, tidak dicoret editor, tidak mengubah",
                    "apa pun, dan tidak ada yang memberi tahu kamu.",
                    "",
                    "KENAPA align-items TERASA TIDAK MEMPAN",
                    "",
                    "Ini keluhan yang hampir semua orang alami sekali:",
                    "",
                    "  .label {",
                    "    display: flex;",
                    "    flex-wrap: wrap;",
                    "    align-items: center;",
                    "    height: 200px;",
                    "  }",
                    "",
                    "Isinya membungkus jadi tiga baris. Alih-alih menumpuk rapi di tengah,",
                    "ketiganya terpencar dengan celah lebar di antaranya. align-items: center",
                    "seperti diabaikan.",
                    "",
                    "Tidak diabaikan - ia mengerjakan persis yang dijanjikannya. Bawaan",
                    "align-content adalah stretch, jadi ketiga BARIS itu lebih dulu dimekarkan",
                    "sampai bertiga memenuhi 200px tinggi wadahnya. Baru sesudah itu",
                    "align-items memusatkan tiap item di dalam barisnya masing-masing - dan",
                    "barisnya memang sudah setinggi 66px. Yang kamu cari untuk merapatkan",
                    "ketiganya adalah align-content: center, atau align-content: flex-start",
                    "kalau maunya menumpuk dari atas.",
                    "",
                    "Aturan praktisnya: begitu sebuah wadah flex punya flex-wrap: wrap DAN",
                    "tinggi yang ditentukan, kamu hampir pasti butuh align-content juga.",
                ],
            },
            {
                "body": [
                    "DI GRID ADA TIGA PASANG, BUKAN SATU",
                    "",
                    "Grid punya dua sumbu juga, tapi - dan ini bedanya dengan flex - sumbunya",
                    "TIDAK ikut berputar. Di grid, justify-* selalu mendatar dan align-*",
                    "selalu menurun, apa pun isi grid-auto-flow-nya. Kebiasaan 'sumbunya",
                    "berputar kalau column' yang kamu bawa dari flexbox tidak berlaku",
                    "di sini, dan itu kabar baik: satu hal lebih sedikit untuk dipikirkan.",
                    "",
                    "                   dipasang di   yang diatur",
                    "  justify-items     wadah         isi tiap sel, mendatar",
                    "  align-items       wadah         isi tiap sel, menurun",
                    "  justify-self      satu item     menimpa justify-items, satu item saja",
                    "  align-self        satu item     menimpa align-items, satu item saja",
                    "  justify-content   wadah         letak SELURUH kisi di wadahnya, mendatar",
                    "  align-content     wadah         letak SELURUH kisi di wadahnya, menurun",
                    "",
                    "Nilai untuk baris -items dan -self: start, end, center, stretch.",
                    "Bawaannya stretch - itu sebabnya isi sebuah sel grid otomatis melar",
                    "memenuhi selnya tanpa kamu minta, persis seperti align-items: stretch",
                    "di flex.",
                    "",
                    "Satu syarat yang gampang terlewat: stretch cuma bekerja kalau itemnya",
                    "belum punya ukuran sendiri. Begitu kamu menulis width: 40px padanya,",
                    "tidak ada lagi yang bisa dimekarkan, dan stretch diam-diam berlaku",
                    "seperti start. Itu jawaban untuk 'kenapa kartu saya tidak sama tinggi",
                    "padahal stretch itu bawaannya' - cari height atau width yang telanjur",
                    "dipasang di kartunya.",
                    "",
                    "Nilai untuk -content: start, end, center, space-between, space-around,",
                    "space-evenly - kosakata yang sama dengan justify-content di flexbox.",
                    "",
                    "YANG PALING SERING TERTUKAR: -items LAWAN -content",
                    "",
                    "  justify-items: center     tiap isi sel duduk di tengah SELNYA",
                    "  justify-content: center   seluruh kisinya duduk di tengah WADAHNYA",
                    "",
                    "Karena itu justify-content sering terasa 'mati' di grid: kalau kolomnya",
                    "kamu tulis 1fr, kolom-kolom itu SUDAH menghabiskan seluruh lebar",
                    "wadahnya, jadi tidak ada sisa ruang untuk digeser ke mana pun. Ia baru",
                    "kelihatan kalau kisinya lebih kecil dari wadahnya - misalnya",
                    "repeat(3, 120px) di dalam wadah selebar 600px. Hal yang sama berlaku",
                    "untuk align-content dan tinggi: kisi setinggi isinya tidak punya sisa",
                    "ruang menurun, jadi tidak ada yang bisa dipindahkan.",
                    "",
                    "BENTUK RINGKAS: align DULU, BARU justify",
                    "",
                    "  place-items: center;       = align-items: center; justify-items: center;",
                    "  place-content: end center; = align-content: end; justify-content: center;",
                    "  place-self: stretch;       = align-self + justify-self, keduanya stretch",
                    "",
                    "Satu nilai berarti dipakai untuk kedua sumbu. Urutannya MENURUN dulu",
                    "baru mendatar - kebalikan dari kebiasaan 'x lalu y' di hampir semua",
                    "tempat lain, dan itu memang gampang tertukar. Kalau ragu, tulis panjang;",
                    "tidak ada yang salah dengan dua baris.",
                    "",
                    "place-items: center di atas display: grid adalah cara satu baris",
                    "memusatkan apa pun, mendatar dan menurun sekaligus. Ia menggantikan tiga",
                    "baris flex yang kamu tulis di materi Flexbox (display, justify-content,",
                    "align-items), dan itu sebabnya kamu akan sering melihatnya di kode orang",
                    "lain untuk wadah yang isinya cuma satu benda.",
                ],
            },
            {
                "heading": "Tiga pola perataan yang menutup kebingungannya",
                "code": """/* 1. Memusatkan isi kartu: satu baris menggantikan tiga */
.kartu-kosong {
  display: grid;
  place-items: center;
  min-height: 240px;
  text-align: center;
}

/* 2. Kisi berukuran tetap di dalam wadah yang lebih besar.
      place-items mengurus isi TIAP SEL,
      place-content mengurus letak SELURUH KISI. */
.kisi {
  display: grid;
  grid-template-columns: repeat(3, 120px);
  grid-template-rows: repeat(2, 120px);
  gap: 12px;
  place-items: center;
  place-content: center;
  min-height: 420px;
}

/* Satu sel dikecualikan: isinya melar penuh, bukan dipusatkan */
.kisi .lebar {
  place-self: stretch;
}

/* 3. Deretan label membungkus: barisnya menumpuk dari atas,
      bukan dimekarkan memenuhi tinggi wadah */
.label {
  display: flex;
  flex-wrap: wrap;
  align-content: flex-start;
  align-items: center;
  gap: 8px;
  height: 120px;
  overflow-y: auto;
}""",
            },
            {
                "body": [
                    "GRID IMPLISIT",
                    "",
                    "Materi Grid menulis: 'baris biasanya tidak perlu ditentukan - grid",
                    "membuatnya sendiri'. Baris buatan itu punya nama, dan namanya perlu kamu",
                    "tahu karena ada properti yang khusus mengaturnya.",
                    "",
                    "  grid EKSPLISIT  jalur (track) yang KAMU tulis sendiri di",
                    "                  grid-template-columns, grid-template-rows, atau",
                    "                  grid-template-areas",
                    "  grid IMPLISIT   jalur yang DIBUAT grid sendiri karena masih ada item",
                    "                  yang belum kebagian tempat",
                    "",
                    "Tiga kolom yang kamu tulis, tujuh item di dalamnya: grid membuat baris",
                    "kedua dan ketiga sendiri. Karena kamu tidak menulis grid-template-rows",
                    "sama sekali, ketiga barisnya implisit - termasuk yang pertama.",
                    "",
                    "UKURAN BARIS BUATAN: grid-auto-rows",
                    "",
                    "Bawaan jalur implisit adalah auto, artinya 'setinggi isi tertinggi di",
                    "baris itu'. Itu sebabnya galeri kartu sering terlihat bergelombang:",
                    "baris pertama jangkung karena ada satu kartu berteks panjang, baris",
                    "kedua pendek, dan tidak satu pun angka di CSS-mu yang menyebabkannya.",
                    "",
                    "  grid-auto-rows: 180px;                semua baris buatan tepat 180px",
                    "  grid-auto-rows: minmax(120px, auto);  minimal 120px, dan boleh lebih",
                    "                                        kalau isinya memang lebih tinggi",
                    "",
                    "Bentuk minmax itu yang paling sering kamu mau: serapi ukuran tetap,",
                    "tapi tidak pernah memotong isi yang kepanjangan.",
                    "",
                    "grid-auto-rows TIDAK menyentuh baris yang sudah kamu tulis di",
                    "grid-template-rows. Keduanya hidup berdampingan: dua baris pertama kamu",
                    "atur sendiri, sisanya diserahkan ke grid-auto-rows. grid-auto-columns",
                    "adalah pasangannya dan jarang dipakai - kolom biasanya eksplisit - dan",
                    "ia baru berguna kalau arah alirannya kamu balik.",
                    "",
                    "ARAH PENGISIAN: grid-auto-flow",
                    "",
                    "  row (bawaan)  isi kiri ke kanan; kalau penuh, buat BARIS baru",
                    "  column        isi atas ke bawah; kalau penuh, buat KOLOM baru",
                    "  dense         boleh mundur mengisi lubang yang telanjur ditinggalkan",
                    "",
                    "dense bukan pengganti arah, melainkan tambahan di belakangnya:",
                    "grid-auto-flow: row dense.",
                    "",
                    "Lubang yang dimaksud muncul kalau ada item yang lebih lebar dari sisa",
                    "barisnya. Bayangkan kisi tiga kolom, dan item ketiga ber-grid-column:",
                    "span 2 - ia tidak muat di sisa satu kolom, jadi ia turun ke baris",
                    "berikutnya dan meninggalkan satu sel menganga. Tanpa dense sel itu",
                    "kosong selamanya, karena algoritma bawaannya tidak pernah menoleh ke",
                    "belakang.",
                    "",
                    "Dengan dense, item BERIKUTNYA yang cukup kecil ditarik maju mengisi",
                    "lubang tadi. Kisimu jadi padat, dan inilah akibatnya: urutan yang",
                    "TERLIHAT tidak lagi sama dengan urutan di HTML.",
                    "",
                    "Jebakannya persis sama dengan order di materi Flexbox - urutan Tab dan",
                    "urutan yang dibacakan pembaca layar tetap mengikuti HTML, bukan yang di",
                    "layar. Untuk galeri gambar itu tidak jadi soal; untuk daftar langkah",
                    "1-2-3 atau deretan tombol, jangan pakai dense.",
                    "",
                    "Satu lagi yang menggigit diam-diam: garis bernomor negatif hanya",
                    "mengenal jalur EKSPLISIT. 'grid-column: 1 / -1' dari materi Grid bekerja",
                    "karena kolomnya kamu tulis sendiri. 'grid-row: 1 / -1' di kisi yang",
                    "barisnya implisit TIDAK menjangkau baris terakhir, karena bagi grid",
                    "jumlah baris eksplisitnya nol.",
                ],
            },
            {
                "heading": "Galeri padat dan papan yang mengalir ke samping",
                "body": [
                    "Dua pola yang memakai semuanya sekaligus. Yang pertama galeri: kolomnya",
                    "menata diri sendiri, barisnya dibuat grid lalu diberi ukuran lewat",
                    "grid-auto-rows, dan lubang yang ditinggalkan kartu besar ditutup dense.",
                    "",
                    "Yang kedua membalik arah aliran, sehingga item mengalir ke KANAN dan",
                    "yang dibuat grid adalah kolom - bukan baris. Di situlah grid-auto-columns",
                    "akhirnya berguna: barisnya eksplisit, kolomnya yang tumbuh.",
                ],
                "code": """/* Galeri: kolom menata diri, baris dibuat grid dan diberi ukuran */
.galeri {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(160px, 1fr));
  grid-auto-rows: minmax(140px, auto);
  grid-auto-flow: row dense;
  gap: 12px;
}

/* Kartu besar inilah yang meninggalkan lubang; dense yang menutupnya */
.galeri .sorotan {
  grid-column: span 2;
  grid-row: span 2;
}

.galeri img {
  display: block;
  width: 100%;
}

/* Papan mendatar: tiga baris tetap, kolomnya yang terus dibuat */
.papan {
  display: grid;
  grid-template-rows: repeat(3, 90px);
  grid-auto-flow: column;
  grid-auto-columns: 220px;
  gap: 12px;
  overflow-x: auto;
}""",
            },
        ],
    },
    {
        "title": "16. Tata Letak Warisan: float, clear, dan flow-root",
        "sections": [
            {
                "body": [
                    "Materi ini tentang cara menata yang sudah TUA. Kamu hampir tidak akan",
                    "memilihnya untuk halaman baru - flex dan grid sudah menang telak. Tapi kamu",
                    "akan MEMBACANYA terus-menerus.",
                    "",
                    "Sebelum flexbox ada (2015-an), tidak ada satu pun cara waras membuat dua",
                    "kolom bersebelahan. Orang memakai float, yang sebenarnya dibuat untuk hal",
                    "lain sama sekali: menyisipkan gambar di dalam artikel. Seluruh web dibangun",
                    "di atas alat yang dipakai bukan untuk maksud aslinya, selama sepuluh tahun.",
                    "",
                    "Akibatnya: Bootstrap 3, tema WordPress, dan praktis setiap berkas CSS yang",
                    "umurnya lebih dari beberapa tahun penuh dengan float: left. Tidak mengerti",
                    "float berarti tidak bisa menyentuh berkas-berkas itu tanpa merusaknya.",
                    "",
                    "Dan ada SATU hal yang float bisa lakukan sementara flex maupun grid tidak",
                    "bisa sama sekali. Itu sebabnya float belum benar-benar pensiun.",
                    "",
                    "APA YANG SEBENARNYA DILAKUKAN float",
                    "",
                    "  float: left;    kotaknya digeser menempel tepi KIRI wadahnya",
                    "  float: right;   digeser menempel tepi KANAN",
                    "  float: none;    bawaannya, tidak mengambang",
                    "",
                    "Elemen ber-float KELUAR dari alur dokumen - alur yang dijelaskan materi Display",
                    "dan Alur Dokumen. Tapi keluarnya cuma setengah, dan justru setengah itu yang",
                    "membuatnya istimewa:",
                    "",
                    "  - Kotak BLOK yang menyusul berlaku seolah float itu tidak ada. Latar dan",
                    "    garis tepi kotak itu lewat DI BAWAH float.",
                    "  - Tapi BARIS TEKS di dalam kotak-kotak itu tetap menghindar. Tiap baris",
                    "    dipendekkan supaya tidak menabrak float.",
                    "",
                    "Jadi yang mengalir mengelilingi float bukan elemennya, melainkan baris",
                    "teksnya. Itu penjelasan gejala yang bikin banyak orang bingung: 'kenapa",
                    "latar paragrafku masuk ke bawah gambar padahal teksnya jelas di samping?'",
                    "Memang begitu kerjanya. Bukan bug.",
                    "",
                    "Tiga akibat sampingan yang jarang disebutkan:",
                    "  - float MEMBLOK-kan elemennya. Sebuah <span> yang diberi float: left",
                    "    mendadak menerima width dan height, tanpa perlu display: inline-block.",
                    "  - Tanpa width, elemen ber-float menyusut sepas isinya, bukan memakan",
                    "    selebar wadah seperti blok biasa.",
                    "  - float DIABAIKAN pada item flex dan item grid. Kalau induknya sudah",
                    "    display: flex, menulis float: left di anaknya tidak melakukan apa pun.",
                ],
            },
            {
                "body": [
                    "GEJALA NOMOR SATU: INDUK YANG MENDADAK SETINGGI NOL",
                    "",
                    "Sebuah kotak menghitung tingginya dari isi yang ada DI DALAM ALUR. Elemen",
                    "ber-float sudah keluar dari alur, jadi ia tidak ikut dihitung sama sekali.",
                    "Kalau isi sebuah wadah HANYA elemen ber-float, tinggi wadah itu jadi 0.",
                    "",
                    "  .wadah { background: #eee; border: 1px solid #ccc; }",
                    "  .wadah > .kolom { float: left; width: 33%; }",
                    "",
                    "Yang kamu lihat: garis tepi .wadah menyusut jadi satu garis tipis di atas",
                    "kolom-kolomnya, latar abu-abunya lenyap, dan apa pun yang ditulis SESUDAH",
                    ".wadah naik menimpa kolom-kolom itu. Tanpa error, tanpa satu petunjuk pun.",
                    "Inilah 'kartu saya gepeng' yang legendaris - dan sebabnya mustahil ditebak",
                    "kalau kamu belum pernah diberi tahu.",
                    "",
                    "clear: 'JANGAN BERDIRI DI SAMPING FLOAT, TURUN DULU'",
                    "",
                    "  clear: left;    turun sampai lewat semua float kiri",
                    "  clear: right;   turun sampai lewat semua float kanan",
                    "  clear: both;    lewat keduanya - ini yang hampir selalu dipakai",
                    "",
                    "clear dipasang pada elemen yang TIDAK mau bersebelahan dengan float, bukan",
                    "pada float-nya. Dua batasnya: ia hanya melihat float yang ditulis SEBELUM",
                    "dirinya, dan ia tidak berpengaruh pada elemen yang ikut ber-float.",
                    "",
                    "CLEARFIX - dan baris misterius di materi Pseudo-element akhirnya ada artinya",
                    "",
                    "  .wadah::after {",
                    "    content: \"\";",
                    "    display: block;",
                    "    clear: both;",
                    "  }",
                    "",
                    "Bacanya begini: tempelkan satu kotak kosong di UJUNG isi .wadah, jadikan ia",
                    "blok biasa yang ikut alur, lalu suruh ia turun melewati semua float. Karena",
                    "kotak kosong itu ADA di dalam alur, tingginya ikut dihitung - dan letaknya",
                    "di bawah float memaksa .wadah cukup tinggi untuk membungkus float-nya.",
                    "",
                    "Tiga barisnya masing-masing punya tugas, dan menghapus salah satu membuat",
                    "seluruhnya diam saja: tanpa content ::after tidak pernah muncul sama sekali,",
                    "tanpa display: block ia inline dan clear tidak berlaku pada inline, tanpa",
                    "clear tidak ada yang turun ke bawah float.",
                    "",
                    "Di kode lama kamu akan melihat versi yang lebih panjang: display: table",
                    "alih-alih block, plus baris zoom: 1 untuk Internet Explorer 6 dan 7 yang",
                    "sudah lama mati. Kenali kalau ketemu; jangan ditulis lagi di kode baru.",
                    "",
                    "display: flow-root - CLEARFIX SATU BARIS",
                    "",
                    "  .wadah { display: flow-root; }",
                    "",
                    "Artinya: 'kotak ini memulai alurnya sendiri di dalam'. Segala yang terjadi",
                    "di dalamnya, termasuk float, selesai di dalamnya. Tingginya otomatis",
                    "membungkus seluruh isinya - tanpa pseudo-element, tanpa content kosong.",
                    "",
                    "Bonusnya: ia sekaligus MEMUTUS margin collapse dari materi Box Model. Margin",
                    "anak pertama tidak lagi bocor keluar dan menggeser induknya.",
                    "",
                    "TRIK LAMA: overflow: hidden ATAU overflow: auto",
                    "",
                    "Keduanya juga membungkus float, karena keduanya sama-sama memulai alur baru",
                    "di dalam. Bertahun-tahun ini jadi cara terpendek dan kamu akan sering",
                    "menemukannya. Tapi efek sampingnya nyata, dan sulit dilacak justru karena",
                    "kelihatannya tidak berhubungan:",
                    "",
                    "  - overflow: hidden MEMOTONG apa pun yang keluar kotak: bayangan, menu",
                    "    tarik-turun, tooltip, tanda fokus yang sedikit melebar.",
                    "  - Ia juga mematikan position: sticky (materi Position) pada elemen di dalamnya.",
                    "  - overflow: auto bisa memunculkan bilah gulir yang tidak kamu minta.",
                    "",
                    "Aturannya sederhana: kalau yang kamu butuhkan cuma 'bungkus float-nya',",
                    "pakai display: flow-root. Pakai overflow hanya kalau kamu memang ingin",
                    "memotong atau menggulir isinya.",
                ],
            },
            {
                "heading": "Kolom ala float, lalu hal yang sama dengan grid (gaya.css)",
                "code": """/* ============ CARA LAMA - yang akan kamu BACA, bukan yang kamu tulis ===== */

.baris-lama {
  background: #f2f2f0;
}

/* Tanpa tiga baris ini, tinggi .baris-lama = 0: latarnya hilang dan kotak
   sesudahnya naik menimpa kolom-kolomnya. */
.baris-lama::after {
  content: "";
  display: block;
  clear: both;
}

.baris-lama .kolom {
  float: left;
  width: 33.3333%;
  padding: 16px;
}

/* Tidak ada gap di dunia float, jadi jarak antar kolom harus dipalsukan
   dengan padding atau margin - dan margin itu MENAMBAH lebar kalau
   box-sizing masih content-box, lihat materi Box Model. Ini sebabnya angka
   di atas begitu rapuh. */

.baris-lama .kolom + .kolom {
  border-left: 1px solid #dcdcdc;
}

/* Pengaman kalau clearfix di atas telanjur dilupakan orang sebelum kamu. */
.sesudah-baris {
  clear: both;
}

/* ============ CARA SEKARANG - hal yang sama, dengan grid ================= */

.baris {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
  background: #f2f2f0;
}

.baris .kolom {
  padding: 16px;
  min-width: 0;
}

/* Tidak ada clearfix, tidak ada persentase yang harus dijumlahkan sendiri,
   tidak ada urusan tinggi nol. Kolomnya juga otomatis sama tinggi -
   sesuatu yang float TIDAK PERNAH bisa lakukan. */""",
            },
            {
                "body": [
                    "NILAI display YANG BELUM PERNAH DISEBUT",
                    "",
                    "Materi Display dan Alur Dokumen memberi block, inline, inline-block, dan none.",
                    "Materi Flexbox dan Grid menambah flex dan grid. Ada satu baris lagi di tabel",
                    "itu, dan justru baris inilah yang paling sering muncul di komponen sungguhan:",
                    "",
                    "  display: inline-flex   isinya ditata seperti flex, TAPI wadahnya sendiri",
                    "                         tetap mengalir dalam baris teks dan selebar isinya",
                    "  display: inline-grid   hal yang sama untuk grid",
                    "",
                    "Bedanya dengan display: flex cuma satu, dan bukan soal isinya: display: flex",
                    "membuat WADAHNYA jadi blok, dan blok memakan seluruh lebar yang tersedia.",
                    "Itu jebakan yang selalu kena pada tombol:",
                    "",
                    "  .tombol { display: flex; align-items: center; gap: 8px; }",
                    "",
                    "Ikon dan teksnya memang jadi sejajar rapi. Tapi tombolnya mendadak selebar",
                    "layar, dan kamu akan mencari-cari width yang tidak pernah kamu tulis. Yang",
                    "kamu mau inline-flex: isinya tetap ditata flex, tombolnya tetap sepas isinya",
                    "dan tetap bisa berdiri di tengah kalimat.",
                    "",
                    "Ini bentuk paling umum untuk tombol berikon, lencana angka, dan chip. Ia persis",
                    "persimpangan dua hal yang selama ini terpisah: inline-block dari materi Display",
                    "dan Alur Dokumen, dan flex dari materi Flexbox.",
                    "",
                    "Karena wadahnya inline, ia ikut aturan teks: celah sekitar 4px antar elemen",
                    "inline yang dibahas materi Display berlaku juga di sini. Perlakukan seperti",
                    "inline-block.",
                    "",
                    "display: contents - SEKILAS SAJA",
                    "",
                    "  KOTAK elemennya dihapus dan anak-anaknya naik menggantikan posisinya.",
                    "  Gunanya saat sebuah <div> pembungkus menghalangi anak-anaknya menjadi",
                    "  item grid langsung dari kakeknya.",
                    "",
                    "  Dua hal yang harus kamu tahu sebelum memakainya: background, border, dan",
                    "  padding elemen itu ikut hilang (kotaknya memang sudah tidak ada), dan",
                    "  pada elemen bermakna seperti <ul> atau <table> ia bisa merusak cara",
                    "  pembaca layar membacanya. Kenali kalau ketemu; jangan ditaburkan.",
                ],
            },
            {
                "heading": "Dua tempat float masih menang, plus tombol inline-flex (gaya.css)",
                "body": [
                    "Kapan float masih pilihan yang benar hari ini? Hanya dua:",
                    "",
                    "  1. Gambar yang DIKELILINGI teks di dalam artikel. Flex dan grid menaruh",
                    "     gambar dan teks di dua sel terpisah; teksnya tidak akan pernah",
                    "     melipat di bawah gambar. Hanya float yang memendekkan baris teks.",
                    "  2. Huruf besar di awal artikel (drop cap), yang cara kerjanya sama:",
                    "     satu huruf ber-float dan beberapa baris pertama mengelilinginya.",
                    "",
                    "Kalau butuh teksnya mengalir mengikuti bentuk yang bukan kotak, ada",
                    "shape-outside: circle(50%) - dan properti itu HANYA bekerja pada elemen",
                    "ber-float. Bukti lain bahwa float tidak tergantikan untuk urusan ini.",
                    "",
                    "Selain dua hal itu: pakai flex atau grid.",
                ],
                "code": """/* Ditulis untuk markup seperti ini:
 * <article class="artikel">
 *   <img class="sisip" src="peta.jpg" alt="Peta lokasi kantor">
 *   <p>Paragraf pertama yang mengalir mengelilingi gambar.</p>
 *   <h2>Judul bagian berikutnya</h2>
 * </article>
 */

.artikel {
  display: flow-root;
  max-width: 640px;
}

.artikel .sisip {
  float: left;
  width: 220px;
  height: auto;
  border-radius: 6px;
  margin: 4px 20px 12px 0;
}

/* Huruf besar di awal artikel. ::first-letter dari materi Pseudo-element,
   di-float supaya beberapa baris pertama merapat mengelilinginya. */
.artikel > p:first-of-type::first-letter {
  float: left;
  font-size: 56px;
  line-height: 0.8;
  font-weight: 700;
  padding-right: 8px;
}

/* Judul berikutnya harus mulai DI BAWAH gambar, bukan di sampingnya. */
.artikel h2 {
  clear: left;
}

/* Tombol berikon: isinya ditata flex, tombolnya sendiri tetap sepas isinya
   dan tetap boleh berdiri di tengah kalimat. */
.tombol {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 10px 18px;
  border-radius: 6px;
  background: #1a4fa0;
  color: white;
  text-decoration: none;
}

.tombol .ikon {
  width: 18px;
  height: 18px;
  flex-shrink: 0;
}

/* Lencana angka yang ikut mengalir di tengah kalimat. */
.lencana {
  display: inline-grid;
  place-items: center;      /* pusatkan angkanya di dalam lingkaran */
  min-width: 22px;
  height: 22px;
  border-radius: 999px;
  background: #c62828;
  color: white;
  font-size: 12px;
}""",
            },
        ],
    },
    {
        "title": "17. Position: static, relative, absolute, fixed, sticky",
        "sections": [
            {
                "body": [
                    "position menjawab dua hal sekaligus: apakah elemen ini masih ikut",
                    "alur dokumen, dan terhadap APA angka top/right/bottom/left dihitung.",
                    "",
                    "static (BAWAAN)",
                    "  Ikut alur normal. top/right/bottom/left DIABAIKAN sepenuhnya.",
                    "  Selama sebuah elemen masih static, memberinya top: 20px tidak",
                    "  melakukan apa-apa. Ini penyebab 'kok tidak bergerak' yang",
                    "  paling sering - angkanya benar, tapi tidak ada yang membacanya.",
                    "",
                    "relative",
                    "  Tetap ikut alur, dan RUANGNYA TETAP DIPESAN di tempat asal,",
                    "  tapi gambarnya digeser dari situ. top: 10px berarti turun 10px",
                    "  dari tempat seharusnya. Tetangganya tidak ikut bergeser dan",
                    "  tidak tahu apa-apa - karena itu relative bisa membuat elemen",
                    "  menimpa tetangganya.",
                    "",
                    "absolute",
                    "  KELUAR dari alur. Ruangnya tidak lagi dipesan; elemen lain",
                    "  menutup bekas tempatnya seolah ia tidak pernah ada.",
                    "  Diposisikan terhadap LELUHUR TERDEKAT yang position-nya bukan",
                    "  static.",
                    "",
                    "fixed",
                    "  Keluar dari alur, diposisikan terhadap JENDELA. Tidak ikut",
                    "  bergulir. Untuk bilah kepala menempel dan tombol mengambang.",
                    "",
                    "sticky",
                    "  Campuran: berlaku normal sampai batas yang kamu tentukan",
                    "  tercapai saat digulir, lalu menempel di situ. WAJIB punya",
                    "  salah satu dari top/right/bottom/left - tanpa itu ia tidak",
                    "  pernah menempel dan terlihat seperti tidak berfungsi.",
                ]
            },
            {
                "body": [
                    "KENAPA position: absolute BUTUH INDUK YANG POSITIONED",
                    "",
                    "absolute selalu butuh titik acuan. Cara ia mencarinya sederhana:",
                    "menaiki pohon induk satu per satu sambil bertanya 'apakah kamu",
                    "punya position selain static?' Yang PERTAMA menjawab ya menjadi",
                    "acuannya. Kalau tidak ada satu pun yang menjawab, acuannya jatuh",
                    "ke halaman itu sendiri.",
                    "",
                    "Karena bawaan SEMUA elemen adalah static, secara alami tidak ada",
                    "yang menjawab. Jadi lencana yang kamu maksudkan menempel di pojok",
                    "kartu akan melompat ke pojok HALAMAN. Bukan karena angkanya",
                    "salah - top: 8px; right: 8px; memang benar - melainkan karena",
                    "tidak ada yang mengaku sebagai acuan.",
                    "",
                    "Obatnya satu baris, di INDUKNYA:",
                    "",
                    "  .kartu { position: relative; }",
                    "",
                    "relative tanpa top/left tidak menggeser apa pun. Fungsinya di",
                    "sini cuma satu: mengangkat tangan supaya anak yang absolute",
                    "menemukannya. Pola 'induk relative, anak absolute' adalah pola",
                    "paling sering dipakai di seluruh CSS - lencana di kartu, tombol",
                    "tutup di dialog, ikon di dalam kotak isian, semuanya begitu.",
                    "",
                    "Kalau sesuatu yang absolute muncul di tempat yang sama sekali",
                    "tidak kamu duga, pertanyaan pertama selalu: leluhur mana yang",
                    "jadi acuannya? Jawabannya sering 'tidak ada'.",
                ]
            },
            {
                "body": [
                    "z-index: SIAPA DI ATAS SIAPA",
                    "",
                    "  - Angka lebih besar tampil di depan.",
                    "  - HANYA berlaku pada elemen yang position-nya bukan static",
                    "    (atau yang menjadi item flex/grid). z-index pada elemen",
                    "    static tidak berarti apa-apa dan diabaikan diam-diam.",
                    "  - Angkanya hanya dibandingkan DI DALAM 'stacking context' yang",
                    "    sama. Induk ber-opacity kurang dari 1, ber-transform",
                    "    (materi Transform), atau ber-filter (materi Bayangan dan",
                    "    Filter) membuat konteks baru - dan anak ber-z-index 9999",
                    "    di dalamnya tetap tidak bisa melewati saudara induknya.",
                    "    Inilah sebab 'z-index saya tidak mempan padahal sudah besar",
                    "    sekali'. Yang perlu dinaikkan induknya, bukan anaknya.",
                    "    Perhatikan jebakannya: ketiganya properti HIASAN, bukan",
                    "    properti penumpuk. Satu transform: translateY(-2px) saat",
                    "    hover pada sebuah kartu sudah cukup mengurung menu turun di",
                    "    dalamnya, tanpa satu pun angka z-index yang berubah.",
                    "  - Jangan menaikkan angka sampai 99999 tiap kali ada masalah.",
                    "    Sepakati beberapa tingkat saja - 10 untuk menu turun,",
                    "    100 untuk dialog, 1000 untuk pesan sistem - lalu patuhi.",
                    "",
                    "sticky YANG TIDAK MENEMPEL, tiga sebab paling umum:",
                    "  1. Lupa menulis top: 0 (atau sisi lainnya).",
                    "  2. Ada leluhur yang overflow-nya hidden, auto, atau scroll.",
                    "     sticky menempel pada wadah gulir terdekat, dan kalau wadah",
                    "     itu tidak ikut bergulir, tidak ada yang terjadi.",
                    "  3. Induk langsungnya tidak lebih tinggi dari elemennya. sticky",
                    "     hanya bisa menempel selama induknya masih terlihat.",
                    "",
                    "Bedanya dengan fixed: sticky berhenti menempel begitu induknya",
                    "habis tergulir. Itu yang membuatnya cocok untuk judul bagian",
                    "yang menempel hanya selama bagiannya sendiri dibaca.",
                ]
            },
            {
                "heading": "Lima nilai position dalam satu berkas",
                "code": """/* Pola induk-anak yang paling sering dipakai di CSS */
.kartu {
  position: relative;       /* jadi acuan, tanpa menggeser apa pun */
  padding: 20px;
}

.kartu .lencana {
  position: absolute;
  top: 8px;
  right: 8px;
  padding: 2px 10px;
  border-radius: 999px;
  background: crimson;
  color: white;
}

/* Bilah kepala yang menempel saat halaman digulir */
.kepala {
  position: sticky;
  top: 0;
  z-index: 10;
  background: white;
  border-bottom: 1px solid #e4e4e4;
}

/* Tombol mengambang; acuannya jendela, bukan induknya */
.tombol-apung {
  position: fixed;
  right: 24px;
  bottom: 24px;
  z-index: 100;
}

/* Geser sedikit tanpa mengganggu tetangga */
.ikon-sejajar {
  position: relative;
  top: 2px;
}""",
            },
            {
                "body": [
                    "AKIBAT LANGSUNG DARI .kepala YANG STICKY: TAUTAN LOMPAT MENDARAT",
                    "DI BALIKNYA",
                    "",
                    "Begitu ada bilah kepala sticky setinggi 64px di atas halaman,",
                    "setiap tautan lompat <a href=\"#bagian\"> jadi terasa rusak.",
                    "Browser menggulir sampai judul bagiannya duduk tepat di tepi atas",
                    "jendela - dan tepi atas jendela itu sekarang tertutup bilahmu",
                    "sendiri. Judulnya sampai, tapi tidak terlihat. Gejalanya persis",
                    "seperti tautan yang salah alamat, padahal alamatnya benar.",
                    "",
                    "Obatnya dipasang di SASARANNYA, bukan di tautannya:",
                    "",
                    "  h2 { scroll-margin-top: 80px; }",
                    "",
                    "Dibaca: 'kalau kamu jadi sasaran gulir, anggap dirimu punya",
                    "margin 80px di atas'. Angkanya tinggi bilah ditambah sedikit",
                    "ruang napas. Margin ini hanya dipakai saat menggulir - tata",
                    "letaknya tidak bergeser sedikit pun.",
                    "",
                    "Saudaranya: scroll-margin-bottom, dan scroll-padding-top yang",
                    "dipasang di WADAH GULIRNYA kalau kamu ingin satu setelan berlaku",
                    "untuk semua sasaran di dalamnya sekaligus.",
                    "",
                    "GULIR YANG MULUS, DAN KENAPA IA HARUS DIMATIKAN SENDIRI",
                    "",
                    "  html { scroll-behavior: smooth; }",
                    "",
                    "Dengan itu lompatan tadi tidak lagi berpindah seketika melainkan",
                    "meluncur. Satu baris. Tapi ada yang penting. Sebagian orang",
                    "menyetel sistemnya untuk MENGURANGI GERAK, dan cara halaman",
                    "menghormatinya adalah blok @media (prefers-reduced-motion:",
                    "reduce) - dibahas lengkap nanti di materi Transisi dan Animasi.",
                    "Blok itu biasanya cuma mematikan animation-duration dan",
                    "transition-duration, sedangkan scroll-behavior bukan animation",
                    "dan bukan transition. Jadi ia lolos dari sana, dan harus",
                    "dimatikan sendiri:",
                    "",
                    "  @media (prefers-reduced-motion: reduce) {",
                    "    html { scroll-behavior: auto; }",
                    "  }",
                    "",
                    "Gulir sepanjang halaman adalah gerakan terbesar yang bisa dibuat",
                    "sebuah situs, dan untuk sebagian orang halaman yang meluncur",
                    "sendiri benar-benar membuat mual.",
                    "",
                    "MENGUNCI GULIRAN DI TIAP KARTU (scroll-snap)",
                    "",
                    "Deretan kartu mendatar yang berhenti rapi di tiap kartu, bukan",
                    "menggantung di antara dua kartu, cuma butuh dua properti:",
                    "",
                    "  .deret         { overflow-x: auto; scroll-snap-type: x mandatory; }",
                    "  .deret > .kartu { scroll-snap-align: start; }",
                    "",
                    "scroll-snap-type dipasang di WADAHNYA: sebut sumbunya (x atau y),",
                    "lalu mandatory kalau wajib berhenti pas, atau proximity kalau",
                    "cuma dibantu mendekat. scroll-snap-align dipasang di tiap",
                    "ANAKNYA: start, center, atau end. Pakai secukupnya - guliran yang",
                    "menolak berhenti di tempat yang dituju pembaca terasa seperti",
                    "bertengkar dengan halaman.",
                ]
            },
        ],
    },
    {
        "title": "18. Pseudo-class dan Pseudo-element",
        "sections": [
            {
                "body": [
                    "PSEUDO-CLASS memilih elemen dalam KEADAAN tertentu. Ditulis",
                    "dengan satu titik dua.",
                    "",
                    "Berdasarkan interaksi:",
                    "  a:hover           saat kursor berada di atasnya",
                    "  a:active          saat sedang ditekan",
                    "  a:visited         tautan yang pernah dibuka",
                    "  input:focus       saat sedang aktif (diklik atau lewat Tab)",
                    "  input:focus-visible   fokus yang memang perlu ditandai",
                    "  .baris:focus-within   ada sesuatu DI DALAMNYA yang sedang",
                    "                        difokuskan (dipakai di materi Menata",
                    "                        Formulir)",
                    "  input:checked     centang atau radio yang tercentang",
                    "  button:disabled   tombol yang dimatikan",
                    "",
                    "Berdasarkan posisi di antara saudaranya:",
                    "  li:first-child       anak pertama",
                    "  li:last-child        anak terakhir",
                    "  li:nth-child(3)      anak ke-3",
                    "  li:nth-child(odd)    ganjil: 1, 3, 5, ...",
                    "  li:nth-child(2n)     kelipatan dua",
                    "  p:not(.penting)      semua p KECUALI yang ber-class penting",
                    "  ul:empty             yang tidak punya isi sama sekali",
                    "",
                    ":nth-child MENGHITUNG SEMUA ANAK, apa pun tagnya.",
                    ":nth-of-type menghitung yang setipe saja. Bedanya nyata:",
                    "",
                    "  <div> <h2>Judul</h2> <p>A</p> <p>B</p> </div>",
                    "",
                    "  p:nth-child(2)    -> cocok dengan <p>A</p>, karena A memang",
                    "                       anak ke-2 di dalam div",
                    "  p:nth-child(1)    -> tidak cocok apa pun; anak ke-1 itu h2",
                    "  p:nth-of-type(1)  -> cocok dengan <p>A</p>",
                    "",
                    "Kalau ':first-child tidak mempan', hampir pasti ada elemen lain",
                    "yang menempati urutan pertama - judul, gambar, atau komentar",
                    "yang kamu lupa.",
                ]
            },
            {
                "body": [
                    "PSEUDO-ELEMENT membuat bagian yang TIDAK ADA di HTML. Ditulis",
                    "dengan DUA titik dua.",
                    "",
                    "  p::first-line      baris pertama paragraf",
                    "  p::first-letter    huruf pertamanya",
                    "  ::selection        teks yang sedang disorot pengguna",
                    "  ::placeholder      teks bayangan di dalam kotak isian",
                    "  ::before ::after   isi tambahan sebelum atau sesudah isi elemen",
                    "",
                    "::before dan ::after WAJIB punya properti content, meski kosong:",
                    "",
                    "  .catatan::before { content: \"Catatan: \"; font-weight: 700; }",
                    "  .kartu::after    { content: \"\"; display: block; clear: both; }",
                    "",
                    "Tanpa content, keduanya tidak muncul sama sekali. Ini kesalahan",
                    "nomor satu saat memakainya, dan gejalanya membingungkan karena",
                    "seluruh aturan lain di blok itu terlihat benar.",
                    "",
                    "Keduanya bukan isi sungguhan: tidak ikut tersalin dengan rapi,",
                    "dan tidak selalu dibacakan pembaca layar. Pakai untuk HIASAN -",
                    "garis, tanda kutip, ikon kecil, tanda bintang wajib isi - jangan",
                    "untuk informasi yang hilang artinya kalau tidak terbaca.",
                    "",
                    "KENAPA ADA YANG SATU TITIK DUA DAN ADA YANG DUA?",
                    "  CSS versi lama memakai satu untuk keduanya. CSS3 membedakannya:",
                    "  satu untuk KEADAAN (pseudo-class), dua untuk BAGIAN BUATAN",
                    "  (pseudo-element). Browser masih menerima :before demi halaman",
                    "  lama, tapi tulis ::before di kode baru supaya maksudnya jelas.",
                ]
            },
            {
                "body": [
                    "URUTAN ATURAN TAUTAN TIDAK BOLEH SEMBARANGAN",
                    "",
                    "  a:link  ->  a:visited  ->  a:hover  ->  a:active",
                    "",
                    "Keempatnya punya spesifisitas yang SAMA, jadi yang menang yang",
                    "ditulis belakangan. Kalau :hover ditulis sebelum :visited,",
                    "tautan yang sudah pernah dibuka tidak akan berubah warna saat",
                    "disentuh - dan kamu akan mengira :hover-nya rusak padahal cuma",
                    "kalah urutan. Hafalkan singkatan LoVe-HAte.",
                    "",
                    "JANGAN MENGHAPUS PENANDA FOKUS",
                    "",
                    "  :focus { outline: none; }",
                    "",
                    "Satu baris ini membuat halaman mustahil dipakai lewat keyboard:",
                    "orang tidak lagi tahu tombol mana yang sedang terpilih saat",
                    "menekan Tab. Yang mereka lihat cuma halaman diam. Ini bukan",
                    "soal selera - ini soal halaman yang tidak bisa dipakai sama",
                    "sekali oleh sebagian orang.",
                    "",
                    "Kalau garis bawaannya jelek, GANTI, jangan hilangkan:",
                    "",
                    "  :focus-visible {",
                    "    outline: 2px solid #1a4fa0;",
                    "    outline-offset: 2px;",
                    "  }",
                    "",
                    ":focus-visible menandai hanya saat browser menganggap penandanya",
                    "perlu - muncul saat berpindah dengan Tab, tidak muncul saat",
                    "diklik tetikus. Itu biasanya persis yang kamu inginkan, dan",
                    "itulah alasan pseudo-class ini dibuat.",
                    "",
                    "outline dipilih (bukan border) karena outline tidak menempati",
                    "ruang: menampilkannya tidak menggeser satu pun elemen lain.",
                ]
            },
            {
                "body": [
                    "BENTUK KURSOR IKUT MENGABARKAN KEADAAN",
                    "",
                    "Keadaan tidak cuma diberitahukan lewat warna. Bentuk penunjuk",
                    "tetikus adalah setengah dari pesannya, dan itu properti biasa:",
                    "",
                    "  cursor: pointer       tangan menunjuk: 'ini bisa diklik'",
                    "  cursor: default       panah biasa, bawaan hampir semua tempat",
                    "  cursor: text          balok tegak, bawaan di atas teks",
                    "  cursor: not-allowed   lingkaran dicoret: 'sedang tidak bisa'",
                    "  cursor: grab          telapak terbuka: 'ini bisa diseret'",
                    "  cursor: grabbing      telapak menggenggam, saat sedang diseret",
                    "  cursor: wait          'tunggu, sedang dikerjakan'",
                    "",
                    "cursor: pointer adalah yang paling sering diperlukan sekaligus",
                    "paling sering lupa ditulis. Yang mendapat tangan menunjuk dari",
                    "browser secara cuma-cuma cuma <a> ber-href. <button> TIDAK -",
                    "bawaannya panah biasa, dan itu mengejutkan hampir semua orang.",
                    "Begitu pula <div>, <span>, atau <a> tanpa href yang kamu jadikan",
                    "tombol. Bendanya terlihat persis seperti tombol dan terasa mati",
                    "saat kursor melewatinya - orang tidak tahu ia bisa diklik sampai",
                    "iseng mencoba. Itu sebabnya hampir tiap contoh tombol di materi",
                    "ini menulis cursor: pointer sendiri.",
                    "",
                    "Kebalikannya juga sering salah. Memberi cursor: pointer pada teks",
                    "biasa membuat orang mengkliknya lalu tidak terjadi apa-apa.",
                    "Bentuk kursor adalah janji; jangan berjanji kalau tidak ada",
                    "isinya.",
                    "",
                    "Itu sebabnya cursor: not-allowed di contoh berikut berpasangan",
                    "dengan button:disabled: opacity mengabarkan 'mati' kepada mata,",
                    "cursor mengabarkan hal yang sama kepada tangan - sebelum jarinya",
                    "sempat menekan.",
                ]
            },
            {
                "heading": "Keadaan dan bagian buatan",
                "code": """a {
  color: #1a4fa0;
}

a:hover {
  color: #0d2f66;
}

:focus-visible {
  outline: 2px solid #1a4fa0;
  outline-offset: 2px;
}

button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

/* Baris tabel selang-seling */
tbody tr:nth-child(even) {
  background: #f6f7f9;
}

/* Garis pemisah di antara item, tidak di ujung */
.daftar li + li {
  border-top: 1px solid #e3e3e3;
}

/* Tanda bintang untuk isian wajib */
.wajib::after {
  content: " *";
  color: crimson;
}

.catatan::before {
  content: "Catatan: ";
  font-weight: 700;
}

::placeholder {
  color: #8a8f98;
}

::selection {
  background: #ffe08a;
}""",
            },
        ],
    },
    {
        "title": "19. Transisi dan Animasi",
        "sections": [
            {
                "body": [
                    "transition tidak menggerakkan apa pun sendirian. Ia cuma satu janji:",
                    "KALAU nilai properti ini berubah, jangan lompat - tempuh perlahan.",
                    "",
                    "Yang mengubah nilainya selalu sesuatu yang lain:",
                    "  - pseudo-class seperti :hover, :focus-visible, atau :checked",
                    "    (materi Pseudo-class dan Pseudo-element)",
                    "  - class yang ditambah atau dihapus JavaScript",
                    "  - media query yang mulai berlaku saat jendela diubah ukurannya",
                    "",
                    "Kalau tidak ada satu pun yang mengubah nilainya, transition diam saja.",
                    "Itu bukan error dan tidak ada pesan apa pun. Baris transition yang",
                    "'tidak jalan' hampir selalu berarti tidak ada yang berubah.",
                    "",
                    "Bentuk nilainya empat bagian, berurutan:",
                    "",
                    "  transition: background-color 0.2s ease 0s;",
                    "",
                    "  background-color   properti yang diawasi",
                    "  0.2s               durasi: berapa lama perjalanannya",
                    "  ease               kurva waktu: cepat-lambatnya sepanjang durasi",
                    "  0s                 jeda sebelum perjalanan dimulai",
                    "",
                    "Dua nilai waktu itu dibedakan dari URUTANNYA, bukan dari namanya: yang",
                    "pertama selalu durasi, yang kedua selalu jeda. 'opacity 1s 0.5s' berarti",
                    "tunggu setengah detik lalu memudar selama satu detik - bukan sebaliknya.",
                    "",
                    "SATUANNYA WAJIB DITULIS. Boleh 0.2s, boleh 200ms, tidak boleh 0.2 saja.",
                    "Bahkan nol pun bersatuan: 0s. Angka telanjang membuat SELURUH deklarasi",
                    "transition itu dibuang browser tanpa sepatah kata pun - dan gejalanya",
                    "persis sama dengan 'transition-nya tidak jalan'.",
                    "",
                    "ATURAN YANG PALING SERING DILANGGAR: transition ditulis di keadaan",
                    "DASAR, bukan di dalam :hover.",
                    "",
                    "  /* benar */",
                    "  .tombol       { background-color: #1a4fa0;",
                    "                  transition: background-color 0.2s ease; }",
                    "  .tombol:hover { background-color: #0d2f66; }",
                    "",
                    "  /* salah */",
                    "  .tombol       { background-color: #1a4fa0; }",
                    "  .tombol:hover { background-color: #0d2f66;",
                    "                  transition: background-color 0.2s ease; }",
                    "",
                    "Sebabnya: transition itu milik ELEMEN pada keadaan yang sedang berlaku,",
                    "bukan milik perubahannya. Saat kursor masuk, aturan :hover berlaku dan",
                    "di situ ada transition, jadi geraknya halus. Saat kursor keluar, aturan",
                    ":hover berhenti berlaku BESERTA transition-nya, dan tidak ada lagi yang",
                    "menyuruh browser pelan-pelan. Hasilnya: masuk halus, keluar mendadak.",
                    "",
                    "Gejala setengah-jalan itulah petunjuknya. Kalau geraknya cuma benar di",
                    "satu arah, transition-mu berada di tempat yang salah.",
                    "",
                    "Kalau kamu memang mau dua arah berbeda - masuk cepat, keluar lambat -",
                    "tulis transition di KEDUA tempat dengan durasi masing-masing. Itu",
                    "disengaja dan sah; yang tidak sah cuma menulisnya di :hover saja.",
                ],
            },
            {
                "body": [
                    "BEBERAPA PROPERTI DIPISAH KOMA, masing-masing dengan waktunya sendiri:",
                    "",
                    "  transition: color 0.15s ease-out,",
                    "              box-shadow 0.3s ease-out 0.05s;",
                    "",
                    "transition: all TERLIHAT praktis dan hampir selalu ide buruk:",
                    "  - Browser mengawasi setiap properti yang bisa dianimasikan, termasuk",
                    "    yang tidak pernah kamu maksud.",
                    "  - Suatu hari kamu menambahkan padding atau height di :hover, dan",
                    "    kartunya mulai melar pelan-pelan tanpa pernah kamu minta.",
                    "  - Perubahan yang datang dari luar - tema gelap dipasang, class",
                    "    ditambah JavaScript - ikut terseret jadi animasi.",
                    "Sebutkan propertinya satu per satu. Daftar itu sekalian jadi catatan",
                    "tentang apa yang memang boleh bergerak.",
                    "",
                    "KURVA WAKTU mengatur cepat-lambatnya DI SEPANJANG durasi, bukan",
                    "durasinya. Dua gerakan sama-sama 0.3s bisa terasa sangat berbeda.",
                    "",
                    "  linear        Kecepatan tetap dari awal sampai akhir. Terasa mekanis",
                    "                untuk benda yang seharusnya punya bobot, tapi justru",
                    "                benar untuk putaran spinner dan bilah kemajuan.",
                    "  ease          BAWAAN kalau kamu tidak menulis apa-apa. Berangkat agak",
                    "                cepat, lalu melambat panjang di akhir.",
                    "  ease-in       Mulai lambat, makin cepat. Terasa 'pergi'. Pas untuk",
                    "                sesuatu yang MENGHILANG.",
                    "  ease-out      Mulai cepat, melambat di akhir. Terasa 'tiba'. Pas untuk",
                    "                sesuatu yang MUNCUL - dan ini yang paling sering benar.",
                    "  ease-in-out   Lambat di kedua ujung. Untuk gerak panjang atau yang",
                    "                bolak-balik.",
                    "  cubic-bezier(0.34, 1.4, 0.64, 1)",
                    "                Kurva buatan sendiri; empat angka itu dua titik kendali.",
                    "                Nama-nama di atas sebenarnya cuma julukan untuk kurva",
                    "                seperti ini. Angka kedua dan keempat boleh melewati 1,",
                    "                dan di situlah efek 'melenting sedikit' berasal.",
                    "  steps(12, end)",
                    "                Melompat, bukan meluncur. Untuk animasi sprite, jarum",
                    "                detik yang berdetak, atau efek mesin ketik.",
                    "",
                    "Kenapa ease-out terasa paling wajar untuk sesuatu yang muncul: benda di",
                    "dunia nyata datang cepat lalu direm sampai berhenti. Yang berangkat",
                    "pelan lalu makin cepat justru terbaca seperti sesuatu yang kabur - benar",
                    "untuk yang pergi, aneh untuk yang datang. Kalau ragu: ease-out untuk",
                    "masuk, ease-in untuk keluar.",
                    "",
                    "TIDAK SEMUA PROPERTI BISA DITRANSISIKAN, dan syaratnya cuma satu: harus",
                    "ada NILAI ANTARA. #ffffff ke #000000 punya tengah. 0px ke 16px punya",
                    "tengah. block ke none tidak punya tengah - tidak ada 'setengah block'.",
                    "",
                    "  Bisa    warna, panjang (width, padding, top, gap), opacity, transform,",
                    "          box-shadow, border-radius, filter, dan angka seperti flex-grow",
                    "  Tidak   display, position, float, font-family, flex-direction,",
                    "          background-image",
                    "",
                    "Yang tidak bisa tetap BERUBAH - cuma seketika, tanpa perjalanan dan",
                    "tanpa peringatan apa pun.",
                    "",
                    "AKIBATNYA: 'memudarkan display: none' tidak bisa dilakukan langsung.",
                    "Elemen ber-display: none tidak digambar sama sekali, jadi tidak ada yang",
                    "bisa dipudarkan. Pola yang dipakai orang bertahun-tahun memakai opacity",
                    "berpasangan dengan visibility - contoh lengkapnya ada di bawah. Kenapa",
                    "visibility ikut: opacity: 0 SAJA masih bisa diklik dan masih dibacakan",
                    "pembaca layar (materi Display dan Alur Dokumen).",
                    "",
                    "Jebakan sekeluarga: height dari 0 ke auto juga tidak bisa, karena auto",
                    "bukan angka. Yang biasa dipakai: max-height dengan angka yang cukup",
                    "besar - kekurangannya, kalau angkanya jauh melebihi tinggi sebenarnya,",
                    "sebagian durasinya habis untuk ruang kosong - atau grid-template-rows",
                    "dari 0fr ke 1fr pada wadah grid, karena satuan fr punya nilai antara dan",
                    "tingginya tidak perlu ditebak sama sekali.",
                ],
            },
            {
                "heading": "Transisi yang dipicu keadaan",
                "code": """/* --- Tombol: dua properti bergerak, sisanya tidak --- */
.tombol {
  background-color: #1a4fa0;
  color: #ffffff;
  border: none;
  border-radius: 8px;
  padding: 10px 18px;
  cursor: pointer;

  /* Di keadaan DASAR, bukan di dalam :hover.
     Koma memisahkan properti, masing-masing dengan waktunya sendiri. */
  transition: background-color 0.15s ease-out,
              box-shadow 0.25s ease-out;
}

.tombol:hover {
  background-color: #0d2f66;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.18);
}

.tombol:active {
  background-color: #0a2450;
}

/* --- Kotak isian: cincin fokus yang tumbuh, bukan berkedip --- */
.isian {
  border: 1px solid #d0d4da;
  border-radius: 6px;
  padding: 8px 10px;
  transition: border-color 0.15s ease-out, box-shadow 0.15s ease-out;
}

.isian:focus-visible {
  outline: none;                 /* diganti, bukan dihilangkan */
  border-color: #1a4fa0;
  box-shadow: 0 0 0 3px rgba(26, 79, 160, 0.3);
}

/* --- Panel yang memudar tanpa menyentuh display --- */
.panel {
  opacity: 0;
  visibility: hidden;
  /* Menutup: visibility menunggu 0.2s dulu, supaya memudarnya sempat
     terlihat sampai habis baru elemennya benar-benar hilang. */
  transition: opacity 0.2s ease, visibility 0s linear 0.2s;
}

.panel.tampil {
  opacity: 1;
  visibility: visible;
  /* Membuka: visibility berlaku seketika, memudarnya menyusul. */
  transition: opacity 0.2s ease, visibility 0s linear 0s;
}""",
            },
            {
                "body": [
                    "transition selalu menunggu ada yang mengubah nilai. Kalau kamu ingin",
                    "gerakan yang berjalan SENDIRI - spinner yang berputar, notifikasi yang",
                    "masuk begitu muncul - itu tugas @keyframes dan properti animation.",
                    "",
                    "@keyframes menuliskan RESEP-nya, dan bentuknya tidak mirip aturan CSS",
                    "mana pun: yang berdiri di posisi pemilih bukan elemen, melainkan WAKTU.",
                    "",
                    "  @keyframes masuk {",
                    "    from { opacity: 0; }",
                    "    to   { opacity: 1; }",
                    "  }",
                    "",
                    "  @keyframes berdenyut {",
                    "    0%   { transform: scale(1); }",
                    "    50%  { transform: scale(1.08); }",
                    "    100% { transform: scale(1); }",
                    "  }",
                    "",
                    "from sama artinya dengan 0%, to sama dengan 100%. Beberapa titik waktu",
                    "boleh berbagi satu blok: 0%, 100% { ... }.",
                    "",
                    "@keyframes sendiri TIDAK menjalankan apa pun. Ia cuma resep bernama yang",
                    "tergeletak di berkas. Yang menyalakannya properti animation di pemilih",
                    "biasa:",
                    "",
                    "  .notif { animation: masuk 0.35s ease-out; }",
                    "",
                    "Delapan properti animation, dan bentuk ringkasnya menampung semuanya:",
                    "",
                    "  animation-name             Nama @keyframes-nya. Salah ketik berarti",
                    "                             tidak terjadi apa-apa, tanpa satu pesan pun.",
                    "  animation-duration         Wajib bersatuan. Tanpa ini durasinya 0s dan",
                    "                             animasinya selesai sebelum sempat terlihat.",
                    "  animation-timing-function  Kurva yang sama persis dengan transition.",
                    "  animation-delay            Tunggu sekian lama sebelum mulai.",
                    "  animation-iteration-count  1 (bawaan), angka berapa pun, atau infinite",
                    "                             untuk tidak pernah berhenti sendiri.",
                    "  animation-direction        normal | reverse | alternate |",
                    "                             alternate-reverse. alternate membuat putaran",
                    "                             genap berjalan mundur, sehingga gerak",
                    "                             bolak-balik tidak perlu ditulis dua kali.",
                    "  animation-fill-mode        none | forwards | backwards | both.",
                    "  animation-play-state       running | paused. Untuk menjeda lewat :hover",
                    "                             atau lewat class yang dipasang JavaScript.",
                    "",
                    "fill-mode menjawab satu pertanyaan: sebelum mulai dan sesudah selesai,",
                    "elemen ini memakai nilai yang mana?",
                    "",
                    "  none (bawaan)  Nilai dari aturan CSS biasa. Begitu animasi habis, ia",
                    "                 melompat kembali ke sana.",
                    "  forwards       Nilai keyframe TERAKHIR dipertahankan sesudah selesai.",
                    "  backwards      Nilai keyframe PERTAMA sudah dipakai selama delay.",
                    "                 Tanpa ini, elemen sempat terlihat di keadaan akhirnya",
                    "                 selama jeda lalu melompat ke awal. Itu kedipan.",
                    "  both           Keduanya.",
                    "",
                    "Bentuk ringkasnya bebas urutan KECUALI dua nilai waktu, yang - persis",
                    "seperti di transition - dibedakan dari urutan: durasi dulu, baru jeda.",
                    "",
                    "  animation: masuk 0.35s ease-out 0.1s 1 normal backwards;",
                    "  animation: putar 0.8s linear infinite;",
                    "",
                    "JEBAKAN YANG PALING MAHAL: nilai dasar sebuah properti tidak boleh cuma",
                    "ada di dalam @keyframes-nya.",
                    "",
                    "Godaannya begini - sembunyikan dulu notifikasinya, animasikan supaya",
                    "muncul, lalu tahan dengan forwards supaya tetap terlihat:",
                    "",
                    "  .notif { opacity: 0; animation: masuk 0.35s forwards; }   /* rapuh */",
                    "",
                    "Pada hari animasinya tidak jalan - namanya salah ketik, geraknya",
                    "dimatikan lewat prefers-reduced-motion, elemennya dibuat ulang",
                    "JavaScript sebelum animasinya sempat selesai - notifikasi itu TIDAK",
                    "PERNAH TERLIHAT sama sekali. Tidak ada error, dan elemennya ada di sana",
                    "dengan rapi, cuma ber-opacity 0.",
                    "",
                    "Aturannya: keadaan AKHIR animasi harus sama dengan keadaan alami",
                    "elemennya, dan animasinya cuma berangkat dari tempat lain. Praktisnya",
                    "cukup menulis 'from' saja - keyframe yang tidak ditulis diisi browser",
                    "dengan nilai elemen itu sendiri:",
                    "",
                    "  .notif { opacity: 1; }",
                    "  @keyframes masuk { from { opacity: 0; transform: translateY(-12px); } }",
                    "",
                    "Sekarang animasinya boleh gagal kapan saja dan yang tersisa tetap",
                    "notifikasi yang benar. Sekalian ingat: tanpa forwards, begitu animasi",
                    "selesai properti kembali ke nilai di aturan CSS biasa - dan kalau kamu",
                    "tidak menulisnya di sana, ke nilai BAWAAN properti itu (opacity 1,",
                    "transform none), bukan ke keyframe pertamanya.",
                ],
            },
            {
                "heading": "Animasi yang berjalan sendiri, dan tahu kapan harus diam",
                "body": [
                    "KENAPA ANIMASI HALUS HAMPIR SELALU CUMA MENYENTUH transform DAN opacity",
                    "",
                    "Browser menggambar halaman bertahap: menghitung tata letak (ukuran dan",
                    "posisi semua kotak), mengecat isinya, lalu menyusun lapisan-lapisannya.",
                    "Mengubah width, height, top, atau margin memaksa tahap PERTAMA diulang -",
                    "artinya menghitung ulang tetangga, induk, dan sering seisi halaman, enam",
                    "puluh kali per detik. transform dan opacity tidak menyentuh tata letak",
                    "sama sekali; keduanya bekerja di tahap terakhir dan tidak ada elemen",
                    "lain yang perlu tahu. Karena itu:",
                    "",
                    "  - geser dengan transform: translate(...), bukan top/left/margin",
                    "  - perbesar dengan transform: scale(...), bukan width/height",
                    "",
                    "(transform sendiri dibahas di materi Transform.) Ini bukan soal selera:",
                    "gerakan yang menyentuh tata letak terlihat tersendat di ponsel dan di",
                    "halaman panjang, yang tidak menyentuhnya mulus.",
                    "",
                    "will-change memberi tahu browser lebih dulu bahwa sebuah properti akan",
                    "berubah, supaya lapisan terpisahnya disiapkan sebelum diminta:",
                    "",
                    "  .kartu-seret { will-change: transform; }",
                    "",
                    "Jangan ditaburkan. Tiap elemen ber-will-change memakan memori dan minta",
                    "lapisannya sendiri; memasangnya di * justru MEMPERLAMBAT halaman. Ia",
                    "juga membuat stacking context baru, sehingga z-index anak-anaknya",
                    "mendadak terkurung (materi Position). Pakai hanya kalau kamu sudah",
                    "MELIHAT gerakan tersendat, hanya pada elemen itu.",
                    "",
                    "MENGHORMATI prefers-reduced-motion",
                    "",
                    "Blok di materi Responsif memendekkan semua durasi jadi 0.01ms. Sekarang",
                    "jelas apa yang sedang dimatikannya - dan juga apa yang kurang darinya:",
                    "animasi ber-infinite tidak berhenti oleh durasi pendek, ia cuma berputar",
                    "amat cepat. Jaring pengaman itu perlu animation-iteration-count: 1 juga.",
                    "",
                    "Yang lebih baik daripada mematikan semuanya: perlakukan tiap gerak",
                    "sesuai perannya. Orang yang meminta gerak dikurangi umumnya tidak",
                    "terganggu oleh sesuatu yang memudar; yang membuat pusing adalah",
                    "perpindahan besar, parallax, dan zoom. Jadi buang geser-menggesernya,",
                    "pertahankan redupnya, matikan yang cuma hiasan, dan pelankan yang masih",
                    "harus menyampaikan sesuatu.",
                    "",
                    "Ini bukan kemewahan. Bagi sebagian orang - vertigo, migrain, gangguan",
                    "vestibular - animasi yang tidak diminta benar-benar membuat mual, dan",
                    "mereka sudah menyalakan setelan itu di sistemnya justru supaya halaman",
                    "seperti punyamu mau mendengarkan.",
                ],
                "code": """/* --- Spinner: gerak yang memang harus berjalan sendiri --- */
.spinner {
  width: 24px;
  height: 24px;
  border: 3px solid #d0d4da;
  border-top-color: #1a4fa0;
  border-radius: 50%;
  animation: putar 0.8s linear infinite;
}

@keyframes putar {
  to { transform: rotate(360deg); }
}

/* --- Notifikasi masuk dari atas. Keadaan akhirnya keadaan NORMAL
       elemen, jadi cukup 'from' saja dan forwards tidak diperlukan.
       backwards dipakai supaya selama jeda 0.1s elemennya sudah
       memakai keadaan awal, bukan berkedip di tempat akhirnya. --- */
.notif {
  opacity: 1;
  transform: none;
  animation: masuk 0.35s ease-out 0.1s backwards;
}

@keyframes masuk {
  from {
    opacity: 0;
    transform: translateY(-12px);
  }
}

/* --- Titik 'sedang merekam': bolak-balik lewat alternate --- */
.titik-rekam {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background-color: crimson;
  animation: berdenyut 1.2s ease-in-out infinite alternate;
}

@keyframes berdenyut {
  0%   { opacity: 1;    transform: scale(1); }
  100% { opacity: 0.35; transform: scale(0.8); }
}

.titik-rekam:hover {
  animation-play-state: paused;
}

/* --- Tiap gerak diperlakukan sesuai perannya --- */
@media (prefers-reduced-motion: reduce) {
  .titik-rekam {
    animation: none;
  }

  .spinner {
    /* Masih satu-satunya tanda 'sedang memuat', jadi tetap berputar,
       tapi jauh lebih pelan supaya tidak terus menarik mata. */
    animation-duration: 2.4s;
  }

  .notif {
    animation-name: redup;
  }
}

@keyframes redup {
  from { opacity: 0; }
}""",
            },
        ],
    },
    {
        "title": "20. Menata Tabel",
        "sections": [
            {
                "body": [
                    "Dari semua elemen HTML, tabel yang paling jelek sebelum disentuh CSS - dan",
                    "paling banyak gaya bawaannya. Kamu sudah menulis tabel di materi HTML 8;",
                    "sekarang giliran membuatnya enak dibaca.",
                    "",
                    "Gejala pertama yang membingungkan hampir semua orang: GARIS TEPINYA DOBEL.",
                    "",
                    "  table, th, td { border: 1px solid #999; }",
                    "",
                    "Yang muncul bukan kisi rapi, melainkan garis kembar yang terlihat timbul",
                    "seperti tabel tahun 2003. Kamu tidak salah ketik apa pun.",
                    "",
                    "Sebabnya ada di dua bawaan yang tidak pernah kamu tulis:",
                    "",
                    "  border-collapse: separate;   /* tiap sel punya kotak border SENDIRI */",
                    "  border-spacing: 2px;         /* dan kotak-kotak itu berjarak 2px */",
                    "",
                    "Jadi border <table> digambar, lalu border tiap <td> digambar lagi 2px di",
                    "dalamnya. Dua garis sejajar berdempetan - itulah 'dobel'-nya.",
                    "",
                    "Obatnya satu baris, dan ini praktis selalu jadi baris pertama tiap tabel:",
                    "",
                    "  table { border-collapse: collapse; }",
                    "",
                    "collapse berarti sel-sel bersebelahan BERBAGI satu garis, bukan punya garis",
                    "masing-masing. Begitu collapse menyala, border-spacing tidak berarti apa-apa",
                    "lagi dan diabaikan sepenuhnya - properti itu hanya hidup di mode separate.",
                    "",
                    "Kapan separate masih dipakai? Kalau kamu memang ingin sel-selnya terpisah",
                    "seperti kotak kalender: border-collapse: separate; border-spacing: 8px;",
                    "",
                    "Satu akibat collapse yang perlu diketahui: kalau dua sel bersebelahan",
                    "sama-sama punya border yang berbeda, hanya SATU yang digambar. Yang lebih",
                    "tebal menang; kalau sama tebal, gayanya yang menentukan (double di atas",
                    "solid, solid di atas dashed, dan seterusnya). Jadi jangan heran kalau garis",
                    "yang kamu tulis muncul, tapi bukan yang kamu kira.",
                    "",
                    "Akibat kedua yang mengejutkan: border-radius TIDAK BEKERJA pada tabel yang",
                    "collapse. Sudutnya tetap tajam berapa pun angkanya, karena garisnya sudah",
                    "bukan milik satu kotak lagi. Kalau memang ingin sudut membulat, bungkus",
                    "tabelnya dengan wadah ber-border-radius dan overflow: hidden.",
                    "",
                    "Satu lagi yang sering bikin bingung: <table> TIDAK memakan seluruh lebar",
                    "seperti <div>. Ia menyusut mengikuti isinya. Tabel dua kolom pendek akan",
                    "menempel di kiri dan menyisakan ruang kosong lebar di kanannya. Kalau kamu",
                    "ingin tabelnya selebar wadahnya, katakan: width: 100%.",
                ],
            },
            {
                "body": [
                    "TULIS BORDER DI SEL, BUKAN DI <table>.",
                    "",
                    "  table { border: 1px solid #ccc; }   /* cuma bingkai LUAR */",
                    "  th, td { border: 1px solid #ccc; }  /* ini yang membuat kisinya */",
                    "",
                    "<table> cuma bingkai terluar. Garis antar baris dan antar kolom datang dari",
                    "border milik <th> dan <td>. Ini kekeliruan pertama hampir semua orang:",
                    "border ditulis di table, lalu bingung kenapa barisnya tidak terpisah.",
                    "",
                    "Tabel modern jarang berkisi penuh. Pola yang paling banyak dipakai hari ini",
                    "cuma GARIS BAWAH:",
                    "",
                    "  th, td { border-bottom: 1px solid #e4e6ea; }",
                    "",
                    "Garis mendatar sudah cukup memandu mata dari kiri ke kanan; garis tegak",
                    "justru membuat tabel terlihat sesak. Efek sampingnya: baris TERAKHIR ikut",
                    "bergaris dan tabelnya seperti belum selesai. Matikan dengan",
                    "  tbody tr:last-child td { border-bottom: none; }",
                    "",
                    "PADDING ADALAH SATU-SATUNYA CARA MEMBERI NAPAS DI DALAM SEL.",
                    "",
                    "Bawaan padding sel cuma 1px, jadi hurufnya nyaris menempel garis. Beri",
                    "padding pada th DAN td sekaligus - lupa salah satunya membuat kepala tabel",
                    "tidak sejajar dengan isinya. Ukuran yang wajar: 12px 16px.",
                    "",
                    "  margin PADA SEL TABEL DIABAIKAN TOTAL. Sel bukan kotak biasa; ia bagian",
                    "  dari kisi tabel dan tidak punya margin sama sekali. Kalau kamu menulis",
                    "  margin di td dan tidak terjadi apa-apa, bukan aturannya yang kalah -",
                    "  properti itu memang tidak berlaku di situ.",
                    "",
                    "th BAWAANNYA TEBAL DAN RATA TENGAH.",
                    "",
                    "Isinya rata kiri, judul kolomnya rata tengah - tabelnya terlihat goyang.",
                    "Karena itu hampir tiap tabel butuh:",
                    "  th { text-align: left; }",
                    "Termasuk <th scope=\"row\"> di kolom pertama, yang sering terlupa.",
                    "",
                    "Kolom berisi angka justru sebaliknya: text-align: right, supaya satuan dan",
                    "ribuan berbaris lurus ke bawah dan mudah dibandingkan. Judul kolomnya ikut",
                    "rata kanan, kalau tidak kepalanya jadi tidak sejajar dengan angkanya.",
                    "",
                    "vertical-align PADA SEL: top ATAU middle.",
                    "",
                    "Bawaannya middle. Selama tiap baris cuma setinggi satu baris teks, tidak ada",
                    "bedanya. Begitu satu sel berisi paragraf panjang, sel tetangganya yang cuma",
                    "satu kata akan MELAYANG di tengah - terlihat seperti salah tempat. Untuk",
                    "tabel berisi teks panjang, pakai vertical-align: top pada th dan td.",
                    "",
                    "(Di elemen inline, vertical-align mengatur hal yang sama sekali berbeda -",
                    "lihat materi 6. Di sel tabel, ia mengatur letak seluruh isi sel.)",
                    "",
                    "caption: JUDUL TABEL, DITATA DARI CSS.",
                    "",
                    "  caption-side: top;      /* bawaan */",
                    "  caption-side: bottom;   /* judul pindah ke bawah tabel */",
                    "",
                    "Bawaannya rata TENGAH, jadi biasanya perlu text-align: left supaya sejajar",
                    "dengan kolom pertama. caption berada DI LUAR garis tepi tabel, jadi",
                    "background tabel tidak mengenainya - beri padding-bottom, bukan margin.",
                    "",
                    "Baris selang-seling dan sorot baris sudah kamu lihat di materi 10:",
                    "  tbody tr:nth-child(even) { background: #f6f7f9; }",
                    "  tbody tr:hover           { background: #eef2fb; }",
                    "Tulis tbody di depannya supaya kepala dan kaki tabel tidak ikut belang.",
                    "Bedanya harus TIPIS; belang yang terlalu kuat membuat tabel jadi papan",
                    "catur. Dan ingat :hover tidak ada di layar sentuh - ia bonus, bukan",
                    "satu-satunya cara membedakan baris.",
                ],
            },
            {
                "heading": "gaya.css - tabel harga yang tertata",
                "code": """/* Tabel harga. Markup yang diharapkannya ada di bagian terakhir materi ini. */

.bungkus-tabel {
  overflow-x: auto;      /* yang bisa digeser tabelnya, bukan halamannya */
  overflow-y: auto;
  max-height: 420px;     /* supaya kepala tabel punya alasan untuk menempel */
}

.tabel-harga {
  width: 100%;               /* tabel tidak melebar sendiri; harus disuruh */
  border-collapse: collapse; /* satu garis, bukan dua */
  font-variant-numeric: tabular-nums;
}

/* Lebar kolom lewat <col>. Pada <col> hanya width, background, border,
   dan visibility yang berlaku - padding dan color diabaikan. */
.tabel-harga .kolom-menu {
  width: 44%;
}

.tabel-harga caption {
  caption-side: top;
  text-align: left;      /* bawaan caption: rata tengah */
  padding-bottom: 12px;
  color: #5b616e;
  font-size: 14px;
}

/* Garis tepi ditulis di SEL, bukan di <table> */
.tabel-harga th,
.tabel-harga td {
  padding: 12px 16px;    /* satu-satunya cara memberi napas di dalam sel */
  vertical-align: top;
  border-bottom: 1px solid #e4e6ea;
}

.tabel-harga thead th {
  position: sticky;
  top: 0;
  z-index: 1;
  background: #ffffff;   /* sticky yang bening akan ditembus baris di bawahnya */
  text-align: left;      /* bawaan th: tebal dan RATA TENGAH */
  font-size: 13px;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  color: #5b616e;
  /* border ikut tergulir saat collapse, jadi garisnya dibuat dari bayangan */
  box-shadow: inset 0 -1px 0 #d3d7de;
}

/* <th scope="row"> di kolom pertama juga perlu diratakan kiri */
.tabel-harga tbody th {
  text-align: left;
  font-weight: 600;
}

/* Angka rata kanan supaya satuannya berbaris lurus ke bawah */
.tabel-harga .angka {
  text-align: right;
}

.tabel-harga tbody tr:nth-child(even) {
  background: #f6f7f9;
}

.tabel-harga tbody tr:hover {
  background: #eef2fb;
}

.tabel-harga tbody tr:last-child td,
.tabel-harga tbody tr:last-child th {
  border-bottom: none;
}

.tabel-harga tfoot td {
  border-top: 2px solid #d3d7de;
  border-bottom: none;
  color: #5b616e;
  font-size: 14px;
}

/* Di layar sempit, ruang lebih berharga daripada kelapangan */
@media (max-width: 600px) {
  .tabel-harga th,
  .tabel-harga td {
    padding: 10px 12px;
  }
}""",
            },
            {
                "body": [
                    "LEBAR KOLOM: table-layout auto ATAU fixed",
                    "",
                    "table-layout: auto (BAWAAN)",
                    "  Browser membaca SELURUH isi tabel dulu, baru memutuskan lebar tiap kolom.",
                    "  Enaknya: kolom menyesuaikan isinya tanpa kamu atur apa pun.",
                    "  Dua akibat yang menyakitkan:",
                    "    1. Satu sel berisi teks panjang tanpa spasi - alamat tautan, kode",
                    "       pesanan, alamat surel - bisa melebarkan SELURUH tabel melewati",
                    "       wadahnya. Halaman jadi bisa digeser ke samping (lihat materi 6).",
                    "    2. Lebar kolom berubah tiap kali datanya berubah. Tabel yang isinya",
                    "       datang dari server jadi 'goyang' setiap kali dimuat ulang.",
                    "",
                    "table-layout: fixed",
                    "  Lebar diambil dari BARIS PERTAMA saja (atau dari <colgroup>), isi sesudahnya",
                    "  tidak dilihat sama sekali. Lebar kolomnya tetap, dan tabel panjang jadi",
                    "  jauh lebih cepat digambar karena browser tidak perlu mengukur ribuan sel.",
                    "",
                    "  SYARAT YANG PALING SERING TERLEWAT: tabelnya harus punya width.",
                    "",
                    "    .tabel { table-layout: fixed; width: 100%; }",
                    "",
                    "  Tanpa width, fixed tidak melakukan apa-apa - dan kamu akan mengira",
                    "  propertinya tidak didukung browser. Ia didukung; ia cuma tidak punya",
                    "  angka untuk dibagi.",
                    "",
                    "  Konsekuensinya: teks yang tidak muat TIDAK lagi melebarkan kolomnya, ia",
                    "  meluber keluar sel. Pasangkan dengan salah satu ini:",
                    "    td { overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }",
                    "    td { word-break: break-word; }",
                    "  Yang pertama memotong dengan '...', yang kedua mematahkan katanya.",
                    "",
                    "DUA CARA MENGATUR LEBAR KOLOM",
                    "",
                    "  1. width pada sel di BARIS PERTAMA. Cukup satu baris; seluruh kolom di",
                    "     bawahnya ikut. Menulisnya di tiap td cuma membuang waktu.",
                    "       thead th:first-child { width: 44%; }",
                    "",
                    "  2. <colgroup> dan <col> di HTML, lalu ditata dari CSS. Ini menunjuk KOLOM",
                    "     secara langsung, jadi tidak bergantung pada sel mana yang kebetulan",
                    "     ada di baris pertama.",
                    "       <colgroup><col class=\"kolom-menu\"><col><col></colgroup>",
                    "       .kolom-menu { width: 44%; }",
                    "",
                    "     Jebakan <col>: hanya SEDIKIT properti yang berlaku padanya - width,",
                    "     background, border, dan visibility. padding, color, text-align, dan",
                    "     font DIABAIKAN diam-diam. Banyak orang kehilangan setengah jam mencoba",
                    "     meratakan satu kolom lewat <col>; caranya bukan di situ, melainkan",
                    "     lewat class di tiap sel (lihat .angka di contoh).",
                    "",
                    "Persentase dihitung terhadap lebar tabel, dan tidak harus berjumlah 100%:",
                    "sisa ruangnya dibagi ke kolom yang tidak diberi width.",
                ],
            },
            {
                "heading": "index.html - markup yang diharapkan gaya di atas",
                "body": [
                    "TABEL ADALAH PENYEBAB NOMOR SATU HALAMAN YANG BISA DIGESER KE SAMPING.",
                    "",
                    "Tiga kolom berisi teks, masing-masing berpadding, sudah lewat dari lebar",
                    "ponsel. Jangan mengecilkan hurufnya - bungkus tabelnya (materi 6):",
                    "",
                    "  .bungkus-tabel { overflow-x: auto; }",
                    "",
                    "Yang bisa digeser tinggal tabelnya, bukan seluruh halaman. Kalau tabelnya",
                    "duduk di dalam kolom grid atau item flex, wadahnya masih perlu min-width: 0",
                    "(materi 8) - tanpa itu kolomnya ikut melebar dan pembungkusnya tidak pernah",
                    "menggulir sama sekali.",
                    "",
                    "KEPALA TABEL YANG MENEMPEL SAAT DIGULIR",
                    "",
                    "  thead th { position: sticky; top: 0; }",
                    "",
                    "Tulis di th, bukan di thead atau tr - browser lama hanya menempelkan SEL.",
                    "Semua syarat sticky dari materi 9 berlaku, ditambah dua yang khas tabel:",
                    "",
                    "  1. Wajib ada top (atau sisi lain). Tanpa itu ia tidak pernah menempel.",
                    "",
                    "  2. sticky menempel pada wadah GULIR terdekat. Begitu tabelnya dibungkus",
                    "     .bungkus-tabel, acuannya jadi pembungkus itu - bukan halaman. Kalau",
                    "     pembungkusnya setinggi isinya, ia tidak pernah menggulir ke bawah, dan",
                    "     kepalanya diam saja walaupun HALAMAN digulir. Karena itu contoh di atas",
                    "     memberinya max-height. Perhatikan juga: menulis overflow-x: auto saja",
                    "     sudah membuat overflow-y ikut menjadi auto - pembungkusmu sudah menjadi",
                    "     wadah gulir meski kamu tidak memintanya.",
                    "",
                    "  3. Sel yang menempel WAJIB punya background. Bawaannya bening, dan baris",
                    "     yang lewat di belakangnya akan terlihat menembus tulisan kepalanya.",
                    "",
                    "  4. Dengan border-collapse: collapse, border milik sel kepala ikut tergulir",
                    "     bersama tabelnya dan garis bawahnya hilang justru saat menempel. Ganti",
                    "     dengan box-shadow: inset 0 -1px 0 warna - bayangan menempel pada selnya.",
                    "",
                    "Beri juga z-index kecil pada sel kepala supaya ia berada di atas sel isi.",
                ],
                "code": """<div class="bungkus-tabel">
  <table class="tabel-harga">
    <caption>Harga menu, berlaku Januari 2024</caption>

    <colgroup>
      <col class="kolom-menu">
      <col>
      <col>
    </colgroup>

    <thead>
      <tr>
        <th scope="col">Menu</th>
        <th scope="col" class="angka">Gelas kecil</th>
        <th scope="col" class="angka">Gelas besar</th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <th scope="row">Kopi tubruk</th>
        <td class="angka">12.000</td>
        <td class="angka">15.000</td>
      </tr>
      <tr>
        <th scope="row">Kopi susu</th>
        <td class="angka">18.000</td>
        <td class="angka">22.000</td>
      </tr>
      <tr>
        <th scope="row">Cold brew</th>
        <td class="angka">20.000</td>
        <td class="angka">25.000</td>
      </tr>
    </tbody>

    <tfoot>
      <tr>
        <td colspan="3">Semua harga sudah termasuk pajak.</td>
      </tr>
    </tfoot>
  </table>
</div>""",
            },
        ],
    },
    {
        "title": "21. Menata Formulir",
        "sections": [
            {
                "body": [
                    "Empat elemen ini tidak digambar seperti kotak biasa: <input>, <select>,",
                    "<textarea>, dan <button>. Yang menggambarnya WIDGET milik sistem operasi.",
                    "Kotak centang di Windows, di macOS, dan di Android bentuknya beda-beda, dan",
                    "tidak satu pun dari bentuk itu datang dari CSS-mu.",
                    "",
                    "Itu sebabnya sebagian aturanmu terasa diabaikan. Materi Teks dan Font sudah",
                    "menambal separuh masalahnya:",
                    "",
                    "  input, select, textarea, button { font: inherit; }",
                    "",
                    "Tapi huruf cuma satu bagian. background pada <select> sering tidak terlihat,",
                    "border-radius diabaikan, dan warna centang tetap biru bawaan sistem.",
                    "",
                    "KUNCINYA: appearance",
                    "",
                    "  select { appearance: none; -webkit-appearance: none; }",
                    "",
                    "appearance: none MENANGGALKAN rupa bawaan sistem, dan sesudah itu properti CSS",
                    "biasa baru mempan. Baris -webkit- di belakangnya masih ditulis orang karena",
                    "Safari lama - termasuk yang di iPhone - cuma mengerti yang itu.",
                    "",
                    "HARGANYA: yang ditanggalkan itu SEMUANYA, termasuk yang berguna.",
                    "  - Panah kecil di <select> ikut hilang. Kotaknya jadi mirip kotak teks biasa",
                    "    dan orang tidak tahu lagi kalau isinya bisa dibuka.",
                    "  - Kotak centang jadi kotak kosong yang tidak menampilkan apa pun saat",
                    "    dicentang. Bukan rusak - memang tidak ada lagi yang menggambarnya.",
                    "",
                    "Aturan yang menyelamatkan: JANGAN MENANGGALKAN YANG TIDAK KAMU GAMBAR ULANG.",
                    "",
                    "Dua tambalan kecil yang layak dipasang sejak awal:",
                    "",
                    "  input, select, textarea { box-sizing: border-box; }",
                    "      supaya width: 100% tidak melebar keluar wadahnya (lihat materi Box Model)",
                    "",
                    "  textarea { resize: vertical; }",
                    "      supaya orang tidak bisa menariknya melebar dan merusak tata letakmu",
                    "",
                    "Beberapa isian memang tidak bisa ditata isi dalamnya sama sekali: type=\"file\",",
                    "type=\"color\", dan pemilih tanggal. Yang dilakukan orang: sembunyikan kontrol",
                    "aslinya lalu tata <label>-nya - persis teknik kotak centang di bawah nanti.",
                ],
            },
            {
                "body": [
                    "SEBELUM MENANGGALKAN APA PUN, COBA TIGA PROPERTI INI",
                    "",
                    "  accent-color   warna centang, titik radio, bilah geser, dan progress",
                    "  caret-color    warna kursor ketik yang berkedip di dalam kotak isian",
                    "  ::placeholder  warna teks bayangan (sudah dikenal dari materi",
                    "                 Pseudo-class dan Pseudo-element)",
                    "",
                    "accent-color jalan pintas yang jarang diketahui pemula:",
                    "",
                    "  body { accent-color: #1a4fa0; }",
                    "",
                    "Satu baris itu mewarnai SEMUA kotak centang, radio, dan slider di halaman -",
                    "tanpa menanggalkan apa pun. Penanda fokus bawaannya tetap ada, tanda centangnya",
                    "tetap digambar sistem, dan di ponsel ukurannya tetap pas untuk jari. Ia juga",
                    "menular ke anak-anaknya, jadi ditulis sekali di body sudah selesai.",
                    "",
                    "Untuk kebanyakan formulir, sampai di sini sudah cukup. Baru kalau bentuknya",
                    "benar-benar harus lain, keluarkan appearance: none.",
                    "",
                    "caret-color terdengar sepele sampai kamu membuat kotak isian berlatar gelap:",
                    "kursor ketiknya hitam, di atas latar hitam, dan orang mengira kotaknya mati.",
                    "",
                    "  .gelap input { background: #1e2126; color: #fff; caret-color: #fff; }",
                    "",
                    ":focus-within - YANG INI SERING DITULIS ORANG PAKAI JAVASCRIPT",
                    "",
                    ":focus cocok dengan elemen yang SEDANG difokuskan. :focus-within cocok dengan",
                    "elemen yang MEMUAT elemen terfokus, seberapa pun dalam letaknya.",
                    "",
                    "  .baris:focus-within label { color: #1a4fa0; }",
                    "",
                    "Klik kotak isiannya, dan tulisan labelnya ikut menyala - padahal yang difokus",
                    "input-nya, bukan labelnya. Tanpa :focus-within satu-satunya cara adalah",
                    "mendengarkan kejadian focus dan blur lewat JavaScript lalu menambah dan",
                    "menghapus class sendiri. Banyak kode lama melakukan itu karena ditulis sebelum",
                    "pseudo-class ini ada; kalau kamu menemuinya, itu sebabnya.",
                ],
            },
            {
                "body": [
                    "PSEUDO-CLASS YANG HANYA HIDUP DI FORMULIR",
                    "",
                    "  :required           isian yang ber-atribut required",
                    "  :optional           kebalikannya",
                    "  :valid              isinya lolos semua aturan HTML-nya",
                    "  :invalid            isinya tidak lolos",
                    "  :in-range           angkanya masih di antara min dan max",
                    "  :out-of-range       angkanya di luar batas itu",
                    "  :placeholder-shown  kotaknya masih kosong sehingga placeholder terlihat",
                    "  :read-only          tidak bisa disunting pengguna",
                    "  :read-write         bisa disunting",
                    "  :indeterminate      centang yang belum tentu ya/tidak, dan grup radio yang",
                    "                      belum satu pun dipilih",
                    "",
                    ":checked dan :disabled sudah dibahas di materi Pseudo-class dan Pseudo-element.",
                    "Semua yang di atas MEMBACA aturan validasi yang kamu tulis di HTML - required,",
                    "min, max, pattern, type=\"email\" - yang dibahas di materi Formulir Lanjutan.",
                    "CSS tidak memvalidasi apa pun sendiri; ia cuma mewarnai hasil penilaian browser.",
                    "",
                    "JEBAKAN 1: :read-only COCOK DENGAN HAMPIR SEGALANYA",
                    "",
                    "Artinya bukan 'isian yang dikunci', melainkan 'tidak bisa disunting pengguna'.",
                    "<p>, <div>, <h1> - semuanya read-only. Menulis .kotak:read-only akan mengenai",
                    "div biasa juga. Sebut elemennya: input:read-only, textarea:read-only.",
                    "",
                    "JEBAKAN 2, DAN INI YANG PALING SERING MERUSAK TAMPILAN:",
                    ":invalid MENYALA SEJAK HALAMAN DIBUKA.",
                    "",
                    "  input:invalid { border-color: crimson; }   /* jangan */",
                    "",
                    "Kotak yang wajib diisi dan masih kosong memang tidak valid - sejak detik",
                    "pertama, sebelum siapa pun menyentuhnya. Jadi orang membuka formulirmu dan",
                    "langsung disambut lima kotak merah sebelum mengetik satu huruf. Yang",
                    "tersampaikan bukan 'hati-hati', tapi 'formulir ini rusak'.",
                    "",
                    "OBATNYA - :user-invalid",
                    "",
                    "  input:user-invalid { border-color: #a1141d; }",
                    "",
                    ":user-invalid baru menyala setelah orangnya benar-benar berurusan dengan isian",
                    "itu: mengetik lalu berpindah keluar, atau menekan tombol kirim. Persis itulah",
                    "alasan pseudo-class ini dibuat, dan itu yang kamu mau hampir setiap kali.",
                    "",
                    "OBAT CADANGAN untuk browser lama:",
                    "",
                    "  input:not(:placeholder-shown):invalid { border-color: #a1141d; }",
                    "",
                    "Bacanya: merah hanya kalau placeholder-nya SUDAH tidak terlihat, alias sudah ada",
                    "yang diketik. Jebakan di dalam jebakan - input-nya WAJIB punya atribut",
                    "placeholder. Tanpa itu :placeholder-shown tidak pernah cocok, :not(...) jadi",
                    "selalu benar, dan kamu kembali persis ke merah-sejak-dibuka tadi.",
                    "",
                    "form:invalid ikut ada, dan cocok selama masih ada satu isian yang belum lolos.",
                    "Boleh dipakai menandai tombol kirim, tapi jangan MEMATIKAN tombolnya: orang",
                    "jadi tidak punya cara memicu pesan kesalahannya, dan yang dilihat cuma tombol",
                    "mati tanpa keterangan apa yang kurang.",
                    "",
                    "Satu hal untuk membaca CSS orang lain: kalau SATU pemilih di dalam daftar yang",
                    "dipisah koma tidak dikenali browser, SELURUH aturan itu dibuang - bukan cuma",
                    "baris pemilih yang salah. Jadi jangan menumpuk pemilih baru seperti",
                    ":user-invalid bersama pemilih penting lain dalam satu daftar.",
                ],
            },
            {
                "body": [
                    "CHECKBOX DAN RADIO BUATAN SENDIRI",
                    "",
                    "Kalau accent-color tidak cukup, polanya begini: sembunyikan input aslinya, lalu",
                    "gambar kotaknya di ::before milik <label> di sebelahnya.",
                    "",
                    "  input:checked + label::before { background: #1a4fa0; }",
                    "",
                    "Tiga hal yang menentukan teknik ini jadi atau hancur:",
                    "",
                    "1. SEMBUNYIKAN, JANGAN HAPUS.",
                    "   display: none dan visibility: hidden membuang input-nya dari urutan Tab.",
                    "   Orang yang memakai keyboard tidak bisa mencapainya sama sekali, dan tidak",
                    "   ada gejala apa pun di layarmu karena tetikusmu masih jalan. Pakai",
                    "   opacity: 0, dan taruh input-nya PERSIS di atas kotak gambaranmu supaya",
                    "   klik dan fokus mendarat di tempat yang benar.",
                    "",
                    "2. <label for> BUKAN LAGI ANJURAN, TAPI SYARAT.",
                    "   Input aslinya tidak terlihat, jadi label-lah satu-satunya yang bisa diklik.",
                    "   Tanpa for yang sama persis dengan id input-nya, klik orang tidak mengenai",
                    "   apa-apa dan kotakmu terlihat mati. Alasan lengkapnya di materi Formulir",
                    "   di kurikulum HTML.",
                    "",
                    "3. URUTAN DI HTML MENENTUKAN.",
                    "   Tanda + berarti 'saudara yang PERSIS berikutnya'. Kalau <label> ditulis",
                    "   sebelum <input>, tidak ada satu pun aturan yang cocok - CSS tidak bisa",
                    "   memilih ke belakang. Gejalanya diam: tanpa pesan salah, cuma tidak",
                    "   terjadi apa-apa.",
                    "",
                    "Karena input aslinya tak terlihat, penanda fokusnya ikut tak terlihat. Gambar",
                    "sendiri, kalau tidak halamanmu jatuh ke kesalahan yang sudah dibahas di materi",
                    "Pseudo-class dan Pseudo-element:",
                    "",
                    "  input:focus-visible + label::before { outline: 2px solid #1a4fa0; }",
                    "",
                    "Radio sama persis, cuma kotaknya diganti lingkaran: border-radius: 50%.",
                    "",
                    "JANGAN PERNAH MEMAKAI WARNA SAJA UNTUK MENANDAI SALAH",
                    "",
                    "Border merah tidak mengatakan APA yang salah, dan bagi sebagian orang - buta",
                    "warna itu sekitar satu dari dua belas laki-laki - merahnya tidak terbaca sama",
                    "sekali. Sediakan TEKS-nya, dan tulis teks itu sebagai HTML sungguhan yang cuma",
                    "disembunyikan CSS:",
                    "",
                    "  .galat { display: none; }",
                    "  input:user-invalid ~ .galat { display: block; }",
                    "",
                    "Jangan menaruh pesannya di content pada ::after. Isi pseudo-element tidak selalu",
                    "dibacakan pembaca layar, dan alasannya sudah dibahas di materi Pseudo-class dan",
                    "Pseudo-element. Tanda bintang untuk isian wajib beda urusan - itu hiasan, dan",
                    "polanya (.wajib::after) juga ada di materi yang sama.",
                ],
            },
            {
                "heading": "Formulir tertata dari nol",
                "body": [
                    "HTML yang ditata oleh gaya di bawah ini:",
                    "",
                    "  <form action=\"/pesan\" method=\"post\">",
                    "    <p class=\"baris\">",
                    "      <label for=\"surel\">Surel</label>",
                    "      <input type=\"email\" id=\"surel\" name=\"surel\"",
                    "             placeholder=\"nama@contoh.com\" required>",
                    "      <span class=\"galat\">Alamat surel harus memuat tanda @</span>",
                    "    </p>",
                    "",
                    "    <p class=\"baris\">",
                    "      <label for=\"metode\">Metode seduh</label>",
                    "      <span class=\"pilih\">",
                    "        <select id=\"metode\" name=\"metode\" required>",
                    "          <option value=\"\">-- pilih salah satu --</option>",
                    "          <option value=\"tubruk\">Tubruk</option>",
                    "          <option value=\"v60\">V60</option>",
                    "        </select>",
                    "      </span>",
                    "    </p>",
                    "",
                    "    <p class=\"baris\">",
                    "      <label for=\"catatan\">Catatan untuk barista</label>",
                    "      <textarea id=\"catatan\" name=\"catatan\"></textarea>",
                    "    </p>",
                    "",
                    "    <p class=\"pilihan\">",
                    "      <input type=\"checkbox\" id=\"wadah\" name=\"wadah\">",
                    "      <label for=\"wadah\">Saya membawa wadah sendiri</label>",
                    "    </p>",
                    "",
                    "    <button type=\"submit\">Kirim pesanan</button>",
                    "  </form>",
                ],
                "code": """/* Samakan huruf dan model kotaknya lebih dulu. */
input, select, textarea, button {
  font: inherit;
  box-sizing: border-box;
}

/* Satu baris ini sudah mewarnai centang, radio, dan slider di seluruh halaman. */
body {
  accent-color: #1a4fa0;
  caret-color: #1a4fa0;
}

.baris {
  display: grid;
  gap: 0.35rem;
  max-width: 26rem;
  margin: 0 0 1.1rem;
}

.baris label {
  font-weight: 600;
  color: #3b4048;
}

/* Seluruh baris ikut menyala saat isian di dalamnya difokuskan. */
.baris:focus-within label {
  color: #1a4fa0;
}

input[type="email"],
select,
textarea {
  padding: 0.55rem 0.7rem;
  border: 1px solid #b9bec7;
  border-radius: 6px;
  background: #fff;
  color: #23252b;
}

textarea {
  min-height: 6rem;
  resize: vertical;
}

input:focus-visible,
select:focus-visible,
textarea:focus-visible {
  outline: 2px solid #1a4fa0;
  outline-offset: 2px;
}

input:read-only {
  background: #f6f7f9;
}

/* --- select dengan panah gambaran sendiri --- */

.pilih {
  position: relative;
  display: block;
}

.pilih select {
  appearance: none;
  -webkit-appearance: none;
  width: 100%;
  padding-right: 2.2rem;
}

/* Segitiga dari border: tiga sisi transparan, sisi atas diberi warna. */
.pilih::after {
  content: "";
  position: absolute;
  right: 0.85rem;
  top: 50%;
  margin-top: -2px;
  border: 5px solid transparent;
  border-top-color: #4a4f57;
  pointer-events: none;
}

/* --- kotak centang gambaran sendiri --- */

.pilihan {
  position: relative;
  padding-left: 1.8rem;
  margin: 0 0 1.1rem;
}

/* Input aslinya tetap ada dan tetap bisa di-Tab, cuma tidak terlihat. */
.pilihan input[type="checkbox"] {
  position: absolute;
  left: 0;
  top: 0.15em;
  width: 1.15rem;
  height: 1.15rem;
  margin: 0;
  opacity: 0;
}

.pilihan label {
  cursor: pointer;
}

.pilihan label::before {
  content: "";
  position: absolute;
  left: 0;
  top: 0.15em;
  width: 1.15rem;
  height: 1.15rem;
  box-sizing: border-box;
  border: 2px solid #8a8f98;
  border-radius: 5px;
  background: #fff;
}

.pilihan input:checked + label::before {
  background: #1a4fa0;
  border-color: #1a4fa0;
}

/* Dua sisi border yang diputar 45 derajat = tanda centang. */
.pilihan input:checked + label::after {
  content: "";
  position: absolute;
  left: 0.4rem;
  top: 0.3em;
  width: 0.28rem;
  height: 0.6rem;
  border: solid #fff;
  border-width: 0 2px 2px 0;
  transform: rotate(45deg);
}

/* Kotak aslinya tak terlihat, jadi penanda fokusnya harus digambar sendiri. */
.pilihan input:focus-visible + label::before {
  outline: 2px solid #1a4fa0;
  outline-offset: 2px;
}

/* --- pesan kesalahan --- */

.galat {
  display: none;
  color: #a1141d;
  font-size: 0.9375rem;
}

/* :user-invalid, bukan :invalid: baru menyala sesudah orangnya menyentuhnya. */
input:user-invalid {
  border-color: #a1141d;
  background: #fdf3f3;
}

input:user-invalid ~ .galat {
  display: block;
}

button[type="submit"] {
  padding: 0.6rem 1.4rem;
  border: 0;
  border-radius: 6px;
  background: #1a4fa0;
  color: #fff;
  cursor: pointer;
}

button[type="submit"]:hover {
  background: #143d7d;
}""",
            },
        ],
    },
    {
        "title": "22. Responsif: media query",
        "sections": [
            {
                "body": [
                    "Sebelum satu pun media query berarti apa-apa, ada satu baris",
                    "HTML yang wajib ada di dalam <head>:",
                    "",
                    "  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">",
                    "",
                    "Tanpa itu, ponsel berpura-pura layarnya selebar 980px lalu",
                    "mengecilkan seluruh halaman supaya muat. Akibatnya media query",
                    "ber-max-width: 600px tidak pernah menyala - menurut ponsel,",
                    "layarnya memang lebar - dan hurufnya jadi sebesar semut.",
                    "",
                    "Baris itu masuk ke HTML, bukan ke CSS. Tapi tanpa dia, seluruh",
                    "materi ini sia-sia. Periksa itu lebih dulu setiap kali tata",
                    "letak ponselmu terlihat 'tidak berubah sama sekali'.",
                    "",
                    "Bentuk media query:",
                    "",
                    "  @media (min-width: 720px) {",
                    "    .halaman { grid-template-columns: 240px 1fr; }",
                    "  }",
                    "",
                    "Dibaca: aturan di dalamnya hanya berlaku kalau lebar jendela",
                    "minimal 720px. Isinya aturan CSS biasa, cuma dibungkus.",
                    "",
                    "  (min-width: X)   berlaku dari X ke ATAS",
                    "  (max-width: X)   berlaku dari X ke BAWAH",
                    "  (min-width: 600px) and (max-width: 900px)   di antara keduanya",
                    "  (orientation: landscape)                    layar melintang",
                    "  print                                       saat halaman dicetak",
                ]
            },
            {
                "body": [
                    "MOBILE FIRST: tulis gaya dasarnya untuk layar SEMPIT, lalu",
                    "tambahkan dengan min-width untuk layar yang lebih lebar.",
                    "",
                    "Kenapa arahnya begitu:",
                    "  - Tata letak sempit hampir selalu lebih sederhana (satu kolom,",
                    "    semuanya bertumpuk), jadi gaya dasarnya pendek dan yang",
                    "    perlu ditambahkan sedikit.",
                    "  - Kalau ada yang gagal dimuat, yang tersisa adalah versi satu",
                    "    kolom - dan versi itu masih terbaca di layar apa pun.",
                    "  - Dengan arah sebaliknya (max-width) kamu terus-menerus",
                    "    MEMBATALKAN aturan yang baru saja kamu tulis, dan berkasnya",
                    "    berubah jadi tumpukan kebalikan-dari-kebalikan.",
                    "",
                    "AMBANG (BREAKPOINT) DIAMBIL DARI ISINYA, BUKAN DARI MEREK PONSEL.",
                    "",
                    "Perbesar-kecilkan jendela pelan-pelan. Di lebar berapa tata",
                    "letaknya mulai jelek - kolomnya terlalu sempit, judulnya patah",
                    "aneh, kartunya jadi pipih? Di situ ambangnya. Daftar 'ukuran",
                    "iPhone terbaru' berubah tiap tahun; isi halamanmu tidak.",
                    "",
                    "Satu hal yang gampang terlewat: media query mengukur SELURUH",
                    "lebar jendela, sementara ruang yang benar-benar tersedia untuk",
                    "isi bisa jauh lebih sempit - panel sisi dan padding tidak ikut",
                    "terhitung. Kalau ada panel 240px dan padding 40px, kolom isi di",
                    "jendela 800px sebenarnya cuma 520px. Hitung, jangan kira-kira.",
                    "",
                    "Akibat salah hitung sering terbalik dari dugaan siapa pun:",
                    "MELEBARKAN jendela justru MENYEMPITKAN kolom baca, karena kolom",
                    "ketiga muncul sebelum ada ruang untuknya. Tulis hitungannya",
                    "sebagai komentar tepat di atas tiap @media - kamu akan",
                    "berterima kasih pada dirimu sendiri tiga bulan lagi.",
                ]
            },
            {
                "heading": "Satu berkas responsif, mobile first",
                "code": """/* --- Dasar: layar sempit, satu kolom --- */
.halaman {
  display: grid;
  grid-template-columns: 1fr;
  gap: 16px;
  padding: 16px;
}

img {
  max-width: 100%;
  height: auto;
}

h1 {
  font-size: clamp(1.5rem, 4vw, 2.5rem);
}

.isi {
  max-width: 68ch;
  min-width: 0;
}

/* --- Semua @media di bagian paling bawah berkas --- */

/* 720px = panel 240 + kolom baca 440 + jarak 40 */
@media (min-width: 720px) {
  .halaman {
    grid-template-columns: 240px 1fr;
    padding: 24px;
  }
}

/* 1100px = 240 + 520 kolom baca + 280 panel kanan + jarak 60 */
@media (min-width: 1100px) {
  .halaman {
    grid-template-columns: 240px 1fr 280px;
  }
}

@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms;
    transition-duration: 0.01ms;
  }
}""",
            },
            {
                "body": [
                    "LETAKKAN BLOK @media DI BAWAH ATURAN YANG DITIMPANYA - paling",
                    "aman di bagian paling bawah berkas.",
                    "",
                    "Media query TIDAK menambah spesifisitas sama sekali. Jadi",
                    "@media (max-width: 720px) { .x { padding: 8px } } yang ditulis di",
                    "tengah berkas KALAH oleh .x { padding: 24px } yang ditulis",
                    "sesudahnya. Yang terjadi bukan pesan error, melainkan tata letak",
                    "ponsel yang diam-diam tidak berlaku - dan kamu menghabiskan",
                    "sejam mencari kesalahan di dalam media query yang sebenarnya",
                    "sudah benar.",
                    "",
                    "YANG SERING MEMBUAT MEDIA QUERY TIDAK DIPERLUKAN SAMA SEKALI:",
                    "",
                    "  img, video { max-width: 100%; height: auto; }",
                    "      gambar tidak pernah lebih lebar dari wadahnya",
                    "  max-width: 68ch",
                    "      panjang baris terjaga tanpa satu pun ambang",
                    "  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr))",
                    "      jumlah kolom menyesuaikan sendiri",
                    "  flex-wrap: wrap",
                    "      item turun sendiri kalau tidak muat",
                    "  width: min(100%, 720px)",
                    "      'yang mana pun yang lebih kecil'",
                    "  font-size: clamp(1rem, 2.5vw, 1.5rem)",
                    "      ikut lebar layar, tapi ada batas bawah dan batas atasnya",
                    "",
                    "Dua yang terakhir itu memakai min() dan clamp(); keduanya",
                    "beserta max() sudah dijelaskan penuh di materi Satuan Lanjut dan",
                    "Menghitung di Dalam CSS. Kalau sebuah ambang cuma kamu pakai",
                    "untuk mengubah SATU angka, hampir selalu ada bentuk clamp()",
                    "yang menggantikannya tanpa ambang sama sekali - dan yang tanpa",
                    "ambang tidak pernah meleset di lebar yang kebetulan tidak kamu",
                    "uji.",
                    "",
                    "Media query juga bisa menanyakan SELERA pemakainya:",
                    "",
                    "  @media (prefers-reduced-motion: reduce) { ... }",
                    "    Orang yang mudah pusing karena gerakan menyalakan setelan",
                    "    ini di sistem operasinya. Matikan animasi di dalam blok ini.",
                    "    Ini bukan tambahan yang manis - untuk sebagian orang,",
                    "    animasi yang tidak diminta benar-benar membuat mual.",
                    "",
                    "  @media (prefers-color-scheme: dark) { ... }",
                    "    Pemakai memilih tema gelap di sistemnya. Materi berikutnya",
                    "    menunjukkan cara menjawabnya dengan rapi lewat variabel.",
                    "",
                    "Dan bisa menanyakan ALATNYA, bukan cuma lebarnya:",
                    "",
                    "  @media (hover: hover) { ... }",
                    "    Alatnya punya penunjuk yang bisa melayang di atas sesuatu",
                    "    tanpa menekannya - tetikus atau touchpad, bukan jari.",
                    "  @media (pointer: coarse) { ... }",
                    "    Penunjuknya kasar, yaitu jari di layar sentuh. Lawannya",
                    "    (pointer: fine) untuk tetikus dan pena.",
                    "",
                    "KENAPA (hover: hover) PENTING - ini bug yang pasti kamu temui",
                    "begitu halamanmu dibuka di ponsel. Di layar sentuh tidak ada",
                    "'melayang di atas'. Browser menyiasatinya dengan menyalakan",
                    ":hover saat disentuh, lalu MEMBIARKANNYA MENYALA sampai orangnya",
                    "menyentuh tempat lain. Akibatnya tombol yang sudah ditekan",
                    "terlihat masih tersorot, menu turun menolak menutup, dan tidak",
                    "ada satu pun yang terlihat salah di kodemu.",
                    "",
                    "Obatnya: berikan gaya :hover hanya kepada alat yang memang bisa",
                    "hover.",
                    "",
                    "  @media (hover: hover) {",
                    "    .kartu:hover { box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15); }",
                    "  }",
                    "",
                    "Di layar sentuh aturan itu tidak pernah menyala, jadi tidak ada",
                    "yang bisa nyangkut. Untuk keadaan yang tetap harus terlihat di",
                    "kedua alat, pakai :active atau :focus-visible - bukan :hover.",
                    "",
                    "(pointer: coarse) berguna untuk hal lain: jari butuh sasaran yang",
                    "lebih besar daripada ujung panah tetikus. Menaikkan padding",
                    "tombol dan jarak antar item menu di dalam blok itu adalah bedanya",
                    "menu yang nyaman di tetikus dan menu yang menyiksa di ponsel.",
                ]
            },
        ],
    },
    {
        "title": "23. Variabel CSS dan Cara Menata Berkas Gaya",
        "sections": [
            {
                "body": [
                    "Variabel CSS - nama resminya 'custom property' - ditulis dengan",
                    "dua tanda minus di depan, dan dibaca dengan var():",
                    "",
                    "  :root {",
                    "    --warna-utama: #1a4fa0;",
                    "  }",
                    "",
                    "  .tombol { background: var(--warna-utama); }",
                    "",
                    ":root adalah elemen <html>. Menaruh variabel di situ berarti",
                    "seluruh halaman bisa membacanya, karena variabel DIWARISKAN",
                    "persis seperti properti teks di materi 4.",
                    "",
                    "Nilai cadangan kalau variabelnya ternyata belum ada:",
                    "  color: var(--warna-teks, #222);",
                    "",
                    "BEDANYA DENGAN VARIABEL DI SASS ATAU LESS",
                    "",
                    "Variabel CSS masih HIDUP saat halaman berjalan. Ia bisa diubah",
                    "per bagian halaman, diubah oleh media query, atau diganti",
                    "JavaScript satu baris. Variabel Sass sudah habis dipakai sebelum",
                    "berkasnya sampai ke browser - yang tiba di sana cuma hasil",
                    "akhirnya, dan tidak ada lagi yang bisa diubah.",
                    "",
                    "Karena itulah tema gelap cukup ditulis SEKALI, di satu tempat.",
                ]
            },
            {
                "heading": "Satu tema, dua rupa",
                "code": """:root {
  --latar: #ffffff;
  --teks: #1c1e22;
  --garis: #e4e6ea;
  --sorot: #1a4fa0;

  --s1: 4px;
  --s2: 8px;
  --s3: 12px;
  --s4: 16px;
  --s5: 24px;
  --s6: 32px;

  /* Kontrol bawaan browser ikut gelap: bilah gulir, kotak centang, dll. */
  color-scheme: light dark;
}

/* 1. Selera sistem. Berlaku selama pemakai belum memilih sendiri. */
@media (prefers-color-scheme: dark) {
  :root {
    --latar: #14161a;
    --teks: #e8e9ec;
    --garis: #2a2e35;
    --sorot: #7aa7f0;
  }
}

/* 2. Pilihan di halaman ini. Ditulis SESUDAH @media, jadi selalu menang. */
[data-tema="gelap"] {
  --latar: #14161a;
  --teks: #e8e9ec;
  --garis: #2a2e35;
  --sorot: #7aa7f0;
  color-scheme: dark;
}

[data-tema="terang"] {
  --latar: #ffffff;
  --teks: #1c1e22;
  --garis: #e4e6ea;
  --sorot: #1a4fa0;
  color-scheme: light;
}

body {
  background: var(--latar);
  color: var(--teks);
}

.kartu {
  background: var(--latar);
  border: 1px solid var(--garis);
  border-radius: var(--s2);
  padding: var(--s5);
  margin-bottom: var(--s4);
}

.kartu h3 {
  color: var(--sorot);
  margin-bottom: var(--s3);
}""",
            },
            {
                "body": [
                    "Perhatikan apa yang TIDAK ada di contoh itu: tidak satu pun",
                    "aturan .kartu ditulis dua kali. Mengganti seluruh tema halaman",
                    "cukup dengan mengubah satu atribut di <html>:",
                    "",
                    "  <html data-tema=\"gelap\">",
                    "",
                    "Semua yang membaca var(--latar) langsung ikut berubah, sampai ke",
                    "elemen terdalam. Itu yang tidak bisa dilakukan variabel Sass.",
                    "",
                    "DUA SUMBER TEMA GELAP, DAN KEDUANYA PERLU",
                    "",
                    "Inilah janji yang ditinggalkan materi Responsif: media query.",
                    "Ada dua pertanyaan berbeda yang gampang dikira satu hal yang",
                    "sama.",
                    "",
                    "  @media (prefers-color-scheme: dark)",
                    "      SELERA SISTEM. Pemakai menyalakan tema gelap di pengaturan",
                    "      ponsel atau laptopnya. Halamanmu ikut menggelap tanpa ia",
                    "      menyentuh apa pun di halamanmu.",
                    "  [data-tema=\"gelap\"]",
                    "      PILIHAN DI HALAMAN INI. Pemakai menekan tombol tema yang",
                    "      kamu sediakan sendiri.",
                    "",
                    "Menggabungkan keduanya cuma soal URUTAN. Spesifisitas :root dan",
                    "[data-tema=\"gelap\"] kebetulan sama persis, jadi yang menang yang",
                    "ditulis belakangan: tulis blok @media lebih dulu, lalu blok",
                    "[data-tema] di bawahnya. Hasilnya persis yang diharapkan orang -",
                    "halaman mengikuti sistem sampai ia memilih sendiri, dan sesudah",
                    "itu pilihannya yang berlaku. Kalau urutannya terbalik, tombol",
                    "temanya terlihat rusak HANYA bagi pemakai bertema gelap, dan itu",
                    "jenis laporan bug yang paling sulit dipercaya.",
                    "",
                    "Karena itu contoh di atas juga menyediakan [data-tema=\"terang\"].",
                    "Tanpa blok itu, pemakai bersistem gelap yang menekan tombol",
                    "'terang' tidak mendapat apa-apa: yang berlaku tetap @media-nya,",
                    "sebab tidak ada satu aturan pun sesudahnya yang membatalkan.",
                    "",
                    "SATU BARIS YANG SERING TERLUPA: color-scheme",
                    "",
                    "  :root { color-scheme: light dark; }",
                    "",
                    "Variabelmu cuma mengurus yang kamu gambar sendiri. Yang digambar",
                    "BROWSER - bilah gulir, kotak centang, pemilih tanggal, dan latar",
                    "di balik halaman sebelum CSS-mu sempat tiba - tidak membaca",
                    "var() mana pun. color-scheme memberi tahu browser tema apa yang",
                    "sedang berlaku, dan seluruh kontrol bawaannya ikut menggelap.",
                    "Tanpa itu kamu dapat halaman gelap dengan bilah gulir putih",
                    "menyala di sisinya, dan tidak ada satu properti pun di berkasmu",
                    "yang bisa mewarnainya.",
                    "",
                    "Nilai 'light dark' berarti 'aku sanggup keduanya, ikuti sistem'.",
                    "Di blok pilihan pemakai sebut satu saja - color-scheme: dark di",
                    "dalam [data-tema=\"gelap\"] - supaya browser tidak salah tebak",
                    "ketika pilihan itu berbeda dari selera sistemnya.",
                    "",
                    "JARAK JUGA LAYAK DIJADIKAN VARIABEL, bukan cuma warna.",
                    "",
                    "Tangga --s1 sampai --s6 di contoh bukan hiasan. Ruang kosong",
                    "adalah bahan bangunan utama sebuah halaman - yang membuat",
                    "tampilan terasa tenang biasanya bukan warnanya melainkan",
                    "jaraknya. Dengan tangga jarak, seluruh kelapangan halaman bisa",
                    "disetel dari satu tempat.",
                    "",
                    "Begitu ada padding: 22px, padding: 15px, dan margin: 19px",
                    "berserakan di lima puluh tempat, tidak ada lagi ritme yang bisa",
                    "dikenali mata - dan tidak ada lagi satu tempat untuk",
                    "memperbaikinya. Angka yang mirip tapi tidak sama justru lebih",
                    "buruk daripada angka yang jelas berbeda.",
                ]
            },
            {
                "body": [
                    "URUTAN ISI BERKAS GAYA YANG BERTAHAN LAMA:",
                    "",
                    "  1. Reset / setelan dasar   *, box-sizing, margin bawaan dibuang",
                    "  2. Variabel                :root { --... }",
                    "  3. Elemen dasar            body, h1-h6, p, a, img, table",
                    "  4. Tata letak              .halaman, .wadah, .kepala, .sisi",
                    "  5. Komponen                .kartu, .tombol, .lencana, .tabel",
                    "  6. Bantuan (utility)       .tengah, .sembunyi, .lebar-penuh",
                    "  7. Media query             semua @media, di bagian paling bawah",
                    "",
                    "Urutan itu bukan selera. CSS menyelesaikan seri spesifisitas",
                    "dengan urutan penulisan, jadi yang UMUM harus di atas dan yang",
                    "KHUSUS di bawah. Berkas yang urutannya acak memaksamu menaikkan",
                    "spesifisitas terus-menerus hanya untuk menimpa aturanmu sendiri.",
                    "",
                    "Beberapa kebiasaan yang menghemat banyak waktu nanti:",
                    "",
                    "  - Beri nama class berdasarkan APA benda itu, bukan bagaimana",
                    "    rupanya. .peringatan bertahan selamanya; .teks-merah akan",
                    "    berbohong pada hari kamu memutuskan peringatan berwarna",
                    "    jingga.",
                    "",
                    "  - Kesepakatan penamaan yang paling banyak dipakai orang punya",
                    "    nama: BEM, bentuknya .blok__elemen--pengubah. Contohnya",
                    "    .kartu, lalu .kartu__judul, lalu .kartu--sorot. Dua garis",
                    "    bawah dibaca 'milik', dua minus dibaca 'versi'. Awas satu",
                    "    hal: dua minus di .kartu--sorot BUKAN variabel CSS, meski",
                    "    bentuknya persis sama dengan --sorot yang baru saja kamu",
                    "    tulis di :root. Yang membedakan cuma posisinya, dan itu",
                    "    dibahas tuntas di materi Membaca CSS di Proyek Nyata.",
                    "",
                    "  - Jaga pemilih tetap pendek. '.kartu .isi p span' sulit ditimpa",
                    "    dan terikat pada susunan HTML yang pasti berubah. Satu class",
                    "    di elemen yang tepat hampir selalu lebih baik.",
                    "",
                    "  - Satu komponen, satu blok berurutan. Jangan menyebar aturan",
                    "    .tombol di tiga tempat berbeda dalam berkas yang sama.",
                    "",
                    "  - Tulis komentar untuk KEPUTUSAN, bukan untuk yang sudah",
                    "    terbaca. '/* membulatkan sudut */' tidak berguna;",
                    "    '/* 720px = panel 240 + kolom baca 440 + jarak 40 */'",
                    "    menyelamatkan siapa pun yang membacanya nanti, termasuk kamu.",
                    "",
                    "  - Berkas boleh dipecah (dasar.css, komponen.css) lalu ditautkan",
                    "    berurutan, tapi tiap <link> tambahan adalah satu permintaan",
                    "    tambahan sebelum halaman bisa tampil rapi. Untuk proyek",
                    "    belajar, satu berkas lebih mudah dijaga.",
                ]
            },
            {
                "body": [
                    "DAFTAR PERIKSA SAAT SEBUAH ATURAN TIDAK BEKERJA",
                    "",
                    "Karena CSS tidak pernah memberi pesan error, periksa berurutan",
                    "dari yang paling sering:",
                    "",
                    "  1. Berkasnya benar-benar tertaut? Salah menulis href tidak",
                    "     memberi pesan apa pun - halamannya cuma tampil polos.",
                    "  2. Pemilihnya cocok dengan elemen yang kamu maksud? Lupa titik",
                    "     di depan nama class adalah kesalahan sejuta umat.",
                    "  3. Ada aturan lain yang lebih spesifik? (materi 2)",
                    "  4. Ada aturan setara yang ditulis BELAKANGAN?",
                    "  5. Nama properti atau nilainya salah ketik? CSS membuang yang",
                    "     tidak dimengerti tanpa bilang apa-apa.",
                    "  6. Elemennya memang punya ukuran? Elemen inline mengabaikan",
                    "     width dan height, dan elemen kosong sering tidak punya",
                    "     tinggi sama sekali.",
                    "  7. Ada tanda kurung kurawal yang lupa ditutup di aturan",
                    "     SEBELUMNYA? Satu kurawal hilang bisa menelan beberapa",
                    "     aturan berikutnya sekaligus.",
                    "",
                    "Di aplikasi ini, langkah 5 dan 7 bisa langsung dicek: jalankan",
                    "berkas .css-nya dan lihat daftar aturan yang tercetak. Apa yang",
                    "tidak muncul di daftar itu juga tidak akan dilihat browser.",
                    "",
                    "Terakhir, dan ini yang paling menenangkan untuk diketahui:",
                    "hampir semua persoalan CSS berujung pada tiga pertanyaan yang",
                    "sama - kotaknya sebesar apa (materi 5), ia ikut alur atau tidak",
                    "(materi 6 dan 9), dan aturan mana yang menang (materi 2).",
                    "Kalau tersesat, kembali ke tiga pertanyaan itu.",
                ]
            },
        ],
    },
    {
        "title": "24. Pemilih Modern dan Lapisan Cascade",
        "sections": [
            {
                "body": [
                    "Materi Pemilih mengajarkan menghitung spesifisitas (a, b, c) dan tiga",
                    "pertanyaan cascade. Semuanya masih benar - tapi tidak lagi lengkap.",
                    "Beberapa tahun terakhir CSS menambahkan tiga pemilih dan satu aturan-at",
                    "yang sekarang ada di hampir semua kode nyata, dan tiga di antaranya",
                    "sengaja BERMAIN dengan angka spesifisitas itu. Tanpa mengenalnya, kode",
                    "orang lain akan terasa seperti melanggar aturan yang baru kamu hafal.",
                    "",
                    ":is() MEMENDEKKAN DAFTAR PEMILIH",
                    "",
                    "  :is(h1, h2, h3) + p { margin-top: 4px; }",
                    "",
                    "Tanpa :is(), pemilih yang sama harus ditulis tiga kali:",
                    "",
                    "  h1 + p, h2 + p, h3 + p { margin-top: 4px; }",
                    "",
                    "Belum terasa. Sekarang kalikan tiga judul dengan tiga wadah:",
                    "",
                    "  .artikel h1, .artikel h2, .artikel h3,",
                    "  .sisi h1,    .sisi h2,    .sisi h3,",
                    "  .kaki h1,    .kaki h2,    .kaki h3 { ... }",
                    "",
                    "  :is(.artikel, .sisi, .kaki) :is(h1, h2, h3) { ... }",
                    "",
                    "Sembilan pemilih jadi satu baris, dan menambah wadah keempat besok cukup",
                    "menyisipkan satu kata - bukan menulis tiga baris lagi sambil berharap",
                    "tidak ada yang terlewat.",
                    "",
                    "SPESIFISITASNYA DIAMBIL DARI ARGUMEN TERKUAT DI DALAM KURUNG",
                    "",
                    "  :is(p, #judul)   ->  (1,0,0)",
                    "",
                    "Angka itu berlaku BAHKAN saat yang benar-benar cocok cuma <p> biasa.",
                    "Satu #id yang diselipkan ke dalam daftar menaikkan SELURUH aturannya ke",
                    "tingkat id, dan sesudah itu tidak ada .class yang bisa menimpanya.",
                    "",
                    ":where() SAMA PERSIS DENGAN :is(), KECUALI SATU HAL",
                    "",
                    "  :where(p, #judul)   ->  (0,0,0)",
                    "",
                    "Spesifisitasnya SELALU nol, apa pun isinya. Cuma itu bedanya: elemen",
                    "yang dicocokkan sama, cara menulisnya sama.",
                    "",
                    "Materi Pemilih menyuruh mulai dari spesifisitas serendah mungkin karena",
                    "'ruang di atasmu adalah persediaan yang habis kalau dipakai terlalu",
                    "cepat'. :where() adalah alat yang dimaksud. Aturan yang dibungkusnya",
                    "bukan cuma rendah, tapi NOL - satu nama elemen polos pun sudah cukup",
                    "untuk menimpanya, tanpa perlu ingat berkas mana yang ditautkan lebih",
                    "dulu. Itu sebabnya hampir semua reset modern dibungkus :where().",
                    "",
                    "Yang dinolkan CUMA isi kurungnya:",
                    "",
                    "  .kartu :where(h3)   ->  (0,1,0), bukan (0,0,0)",
                    "",
                    ".kartu di luar kurung tetap dihitung penuh. :where() bukan sakelar",
                    "'matikan spesifisitas aturan ini'.",
                ],
            },
            {
                "heading": "Reset dan pemilih ringkas (gaya.css)",
                "body": [
                    "BANDINGKAN DENGAN :not(), YANG SUDAH DIPAKAI DI MATERI PSEUDO-CLASS",
                    "",
                    "  p:not(.penting)     ->  (0,1,1)   :not() IKUT menyumbang",
                    "  p:not(#judul)       ->  (1,0,1)   juga dari argumen terkuatnya",
                    "  p:where(.penting)   ->  (0,0,1)   :where() tidak menyumbang apa pun",
                    "",
                    "Titik dua :not() sendiri tidak dihitung; yang dihitung isinya. Dan",
                    ":not() sekarang menerima beberapa argumen sekaligus:",
                    "",
                    "  nav:not(.menu, .remah)   sama dengan   nav:not(.menu):not(.remah)",
                    "",
                    "Artinya 'bukan .menu DAN bukan .remah', bukan 'bukan keduanya",
                    "sekaligus'. Ini gampang sekali dibaca terbalik.",
                    "",
                    "DAFTAR DI DALAM :is() DAN :where() ITU PEMAAF",
                    "",
                    "Di daftar berkoma biasa, SATU pemilih yang tidak dimengerti browser",
                    "membatalkan SELURUH aturannya:",
                    "",
                    "  input::-moz-placeholder, input::placeholder { color: #8a8f98; }",
                    "",
                    "Di browser yang tidak kenal bentuk -moz itu, dua-duanya batal sekaligus.",
                    "Itu persis gejala 'aturannya tidak mempan' yang paling sulit dilacak,",
                    "karena yang salah justru baris yang tidak kamu curigai. Di dalam :is()",
                    "dan :where(), argumen yang tidak dikenal dibuang sendirian dan sisanya",
                    "tetap jalan.",
                    "",
                    ":not() dan :has() TIDAK pemaaf: satu argumen rusak di sana tetap",
                    "membatalkan aturannya.",
                ],
                "code": """/* Bagian reset. Seluruh pemilih di bawah bernilai (0,0,0), jadi apa pun */
/* yang kamu tulis sesudahnya menang - tanpa perlu ingat berkas mana yang */
/* ditautkan lebih dulu. */

:where(body, h1, h2, h3, p, figure, blockquote, ul, ol) {
  margin: 0;
}

:where(ul, ol) {
  padding-left: 0;
  list-style: none;
}

:where(img, picture, video, svg) {
  display: block;
  max-width: 100%;
}

:where(button, input, select, textarea) {
  font: inherit;
  color: inherit;
}

/* Dua-duanya di dalam kurung, jadi seluruh pemilih ini tetap (0,0,0). */
/* Ditulis tanpa :where(), pemilih yang sama bernilai (0,1,1). */
:where(.prose) :where(ul, ol) {
  padding-left: 1.2em;
  list-style: disc;
}

/* Yang ini tidak perlu dibungkus: pemilih * bernilai (0,0,0), dan */
/* ::before / ::after cuma menambah satu ke kolom terakhir. */
*, *::before, *::after {
  box-sizing: border-box;
}

/* Mulai dari sini gaya sendiri, dan di sini :is() yang dipakai: */
/* tujuannya memendekkan, bukan menolkan. */
:is(h1, h2, h3) + p {
  margin-top: 4px;
}

:is(.artikel, .sisi, .kaki) a {
  text-decoration: underline;
}

/* Semua <nav> yang bukan .menu dan bukan .remah */
nav:not(.menu, .remah) {
  border-top: 1px solid #e4e6ea;
}""",
            },
            {
                "heading": "Menata induk berdasarkan isinya",
                "body": [
                    ":has() - PEMILIH INDUK, SATU-SATUNYA YANG MELIHAT KE BAWAH",
                    "",
                    "Semua pemilih di materi Pemilih bergerak ke arah yang sama: dari luar ke",
                    "dalam (div p), atau dari kiri ke kanan (h2 + p). Tidak ada satu pun yang",
                    "bisa bilang 'tata div INI, kalau di dalamnya ada gambar'. Selama dua",
                    "puluh tahun jawabannya selalu JavaScript: baca isinya, lalu tempelkan",
                    "class ke induknya. :has() menghapus keperluan itu.",
                    "",
                    "  .kartu:has(img)            kartu yang di dalamnya ADA <img>",
                    "  label:has(input:checked)   label yang centangnya sedang aktif",
                    "  body:has(dialog[open])     seluruh halaman selama ada dialog terbuka",
                    "",
                    "KESALAHPAHAMAN NOMOR SATU: yang ditata adalah elemen di KIRI titik dua.",
                    "Isi kurung cuma syarat, bukan sasaran. .kartu:has(img) mewarnai KARTUnya,",
                    "bukan gambarnya.",
                    "",
                    "Isi kurungnya bersifat RELATIF terhadap elemen itu, jadi kombinator boleh",
                    "berdiri sendirian di depan:",
                    "",
                    "  .kartu:has(img)     ada <img> di mana pun di dalamnya",
                    "  .kartu:has(> img)   hanya kalau <img> itu anak LANGSUNG",
                    "  h2:has(+ p)         <h2> yang tepat sesudahnya ada <p>",
                    "",
                    "Spesifisitasnya, seperti :is(), diambil dari argumen terkuat di dalam",
                    "kurung; tanda :has() sendiri tidak menambah apa-apa.",
                    "",
                    "Batasnya: :has() tidak boleh disarangkan di dalam :has(), dan tidak",
                    "menerima pseudo-element di dalamnya. Hindari juga bentuk sangat lebar",
                    "seperti *:has(...) - browser memeriksanya ulang setiap kali isi halaman",
                    "berubah, dan ini pemilih yang paling mungkin terasa berat di CSS.",
                ],
                "code": """.kartu {
  display: grid;
  gap: 12px;
  padding: 16px;
  border: 1px solid #e4e6ea;
}

/* Tata letak berubah karena ISINYA, bukan karena class tambahan
   yang harus diingat orang saat menulis HTML-nya. */
.kartu:has(img) {
  grid-template-columns: 120px 1fr;
}

/* Label ikut menyala saat centang di dalamnya aktif.
   Dulu ini butuh JavaScript, atau trik urutan <input> lalu <label>. */
label:has(input:checked) {
  background: #eef4ff;
  font-weight: 700;
}

/* Baris tabel yang tercentang */
tbody tr:has(input[type="checkbox"]:checked) {
  background: #fff6d8;
}

/* Halaman berhenti bisa digulir selama dialog terbuka */
body:has(dialog[open]) {
  overflow: hidden;
}

/* Judul yang tepat sesudahnya ada paragraf: rapatkan jaraknya.
   Judul yang berdiri sendiri tidak ikut. */
h2:has(+ p) {
  margin-bottom: 4px;
}

/* Yang ditata anaknya, syaratnya di tempat lain: tombol kirim
   diredupkan selama masih ada isian yang belum sah. */
form:has(input:invalid) .tombol-kirim {
  opacity: 0.5;
  pointer-events: none;
}""",
            },
            {
                "body": [
                    "@layer: LAPISAN CASCADE",
                    "",
                    "Materi Pemilih menyajikan cascade sebagai tiga pertanyaan. Sekarang ada",
                    "pertanyaan baru, dan ia diajukan SEBELUM spesifisitas dihitung:",
                    "",
                    "  1. Ada yang !important?",
                    "  2. Aturan ini ada di LAPISAN mana?            <- yang baru",
                    "  3. Mana yang spesifisitasnya lebih tinggi?",
                    "  4. Kalau seri, mana yang ditulis belakangan?",
                    "",
                    "Akibatnya langsung terasa: pemilih yang jelas-jelas lebih spesifik bisa",
                    "KALAH oleh pemilih satu kata, asal lapisannya kalah. Kalau suatu hari",
                    "kamu melihat aturan (1,2,1) tercoret sementara 'h3' polos yang menang,",
                    "ini penjelasannya - bukan browser yang rusak dan bukan kamu yang salah",
                    "menghitung.",
                    "",
                    "BENTUKNYA",
                    "",
                    "  @layer reset, dasar, komponen, utility;",
                    "",
                    "Satu baris di paling atas berkas yang tidak menata apa pun; ia cuma",
                    "menetapkan URUTAN. Yang disebut BELAKANGAN menang.",
                    "",
                    "  @layer komponen {",
                    "    .kartu { padding: 16px; }",
                    "  }",
                    "",
                    "Sesudah urutannya ditetapkan, isi tiap lapisan boleh ditulis di mana",
                    "saja, dalam urutan apa pun, bahkan dipecah jadi beberapa blok terpisah.",
                    "Yang berlaku tetap urutan di baris pertama tadi. Itulah gunanya:",
                    "keputusan 'siapa boleh menimpa siapa' ditulis SEKALI dan terbaca dari",
                    "satu baris, bukan disimpulkan dari posisi tiga ratus aturan di dalam",
                    "berkas.",
                    "",
                    "Kalau baris penetapan itu tidak ada, lapisan diurutkan menurut",
                    "kemunculan pertamanya - dan menyisipkan @layer baru di tengah berkas",
                    "diam-diam mengubah hasilnya.",
                    "",
                    "YANG PALING SERING MENGEJUTKAN: ATURAN TANPA LAPISAN MENANG ATAS SEMUA",
                    "",
                    "Aturan yang tidak dibungkus @layer diperlakukan seolah berada di lapisan",
                    "paling akhir - di atas reset, di atas komponen, di atas utility. Jadi",
                    "berpikir 'saya taruh di lapisan utility supaya paling kuat' itu salah;",
                    "yang paling kuat justru yang tidak berlapis sama sekali.",
                    "",
                    "Itu juga alasan pustaka CSS mulai membungkus dirinya sendiri dalam",
                    "lapisan: begitu seluruh isi pustaka ada di dalam @layer, CSS-mu yang",
                    "polos otomatis menang tanpa satu pun pertarungan spesifisitas. Untuk",
                    "berkas pihak lain yang tidak bisa kamu sunting, lapisannya dipasang",
                    "saat mengimpor:",
                    "",
                    "  @import url(\"pustaka.css\") layer(pustaka);",
                    "",
                    "(@import wajib berada di atas semua aturan biasa, tepat sesudah baris",
                    "penetapan urutan lapisan.)",
                    "",
                    "!important MEMBALIK URUTAN LAPISAN",
                    "",
                    "Untuk deklarasi ber-!important, urutannya terbalik: lapisan yang disebut",
                    "PALING AWAL yang menang, dan aturan tanpa lapisan justru jadi yang",
                    "paling lemah. Cukup tahu ini supaya tidak bingung saat menemuinya -",
                    "jangan jadikan alasan memakai !important lebih sering.",
                    "",
                    "Dua bentuk kecil yang akan kamu temui saat membaca kode orang:",
                    "",
                    "  @layer komponen.tombol { ... }   lapisan bersarang, dipisah titik",
                    "  @layer { ... }                   lapisan tanpa nama; tidak bisa",
                    "                                   ditambah isinya dari tempat lain",
                ],
            },
            {
                "heading": "Pemilih paling spesifik pun kalah oleh lapisan (gaya.css)",
                "body": [
                    "Jalankan berkas ini untuk melihat susunan lapisannya tercetak. Satu",
                    "catatan supaya tidak bingung: pembaca CSS di aplikasi ini sederhana dan",
                    "tidak mengenal aturan-at tanpa kurung kurawal, jadi baris",
                    "'@layer reset, pustaka, ...;' akan tercetak menempel pada @layer",
                    "berikutnya. Browser tidak bingung; itu murni tampilan di sini.",
                ],
                "code": """/* gaya.css - urutan lapisan ditetapkan sekali, di baris paling atas */
@layer reset, pustaka, komponen, utility;

@layer pustaka {
  /* Pemilih paling spesifik di seluruh berkas ini: (1,2,1) */
  #halaman .kartu.besar h3 {
    color: #8a8f98;
    font-size: 18px;
  }
}

@layer komponen {
  /* Cuma (0,0,1). Tapi lapisannya disebut BELAKANGAN, jadi menang. */
  h3 {
    color: #1c1e22;
    font-size: 24px;
  }
}

@layer utility {
  .rata-tengah {
    text-align: center;
  }
}

/* Di luar semua lapisan. Menang atas ketiganya, walau pemilihnya terpendek. */
h3 {
  color: #7a1f1f;
}

/* Hasil akhir untuk <h3> di dalam #halaman .kartu.besar:

     font-size  ->  24px      lapisan komponen mengalahkan lapisan pustaka
     color      ->  #7a1f1f   aturan tanpa lapisan mengalahkan ketiganya

   Spesifisitas tetap dihitung - tapi hanya untuk memisahkan aturan
   DI DALAM lapisan yang sama. Antar lapisan, ia tidak ditanya. */""",
            },
        ],
    },
    {
        "title": "25. CSS yang Bertahan: Prefiks Vendor, @supports, dan Properti Logis",
        "sections": [
            {
                "body": [
                    "Buka berkas gaya proyek nyata mana pun, dan cepat atau lambat kamu",
                    "akan menemukan baris seperti ini:",
                    "",
                    "  -webkit-font-smoothing: antialiased;",
                    "  -moz-osx-font-smoothing: grayscale;",
                    "",
                    "Itu BUKAN salah ketik. Itu juga BUKAN variabel CSS.",
                    "",
                    "Bedanya tipis di ujung mata, dan keduanya muncul di berkas yang",
                    "sama, sering hanya berjarak beberapa baris:",
                    "",
                    "  --warna-utama: #1a4fa0;      DUA tanda minus, lalu nama yang kamu",
                    "                               karang sendiri. Ini variabel dari",
                    "                               materi Variabel CSS, dibaca var().",
                    "  -webkit-appearance: none;    SATU tanda minus, lalu nama mesin",
                    "                               browsernya, lalu nama properti asli.",
                    "",
                    "Yang kedua adalah properti CSS sungguhan - hanya saja versi khusus",
                    "milik satu mesin browser. Namanya PREFIKS VENDOR. Ada empat yang",
                    "akan kamu temui:",
                    "",
                    "  -webkit-   Safari dan Chrome (dan hampir semua browser di ponsel)",
                    "  -moz-      Firefox",
                    "  -ms-       Internet Explorer dan Edge versi lama",
                    "  -o-        Opera versi lama",
                    "",
                    "KENAPA BENDA INI PERNAH DIPERLUKAN",
                    "",
                    "Sebuah fitur CSS baru hampir selalu sudah dipakai orang sebelum",
                    "aturan resminya selesai ditulis. Browser ingin orang bisa",
                    "mencobanya, tapi tidak mau halaman yang terlanjur ditulis rusak",
                    "kalau aturan resminya nanti berubah. Jalan tengahnya: pasang",
                    "fiturnya dengan nama berprefiks, dan simpan nama tanpa prefiks",
                    "untuk versi bakunya nanti.",
                    "",
                    "Jadi -webkit-transform dulu berarti 'versi percobaan milik WebKit',",
                    "sedangkan transform berarti 'versi yang sudah disepakati semua'.",
                    "",
                    "URUTANNYA PENTING: BERPREFIKS DI ATAS, YANG BAKU DI BAWAH",
                    "",
                    "  .kotak {",
                    "    -webkit-transform: rotate(3deg);",
                    "    transform: rotate(3deg);",
                    "  }",
                    "",
                    "Browser membuang deklarasi yang tidak dimengerti tanpa bilang",
                    "apa-apa (materi pertama). Browser lama karena itu cuma melihat",
                    "baris pertama, sedangkan browser baru melihat keduanya lalu memakai",
                    "yang TERAKHIR - deklarasi setara yang ditulis belakangan menang.",
                    "Kalau urutannya dibalik, browser modern justru terkunci pada versi",
                    "percobaan yang sudah usang, dan tidak ada satu pun pesan yang",
                    "memberitahumu.",
                    "",
                    "KABAR BAIKNYA: KAMU HAMPIR TIDAK PERNAH PERLU MENULISNYA SENDIRI.",
                    "",
                    "transform, border-radius, box-shadow, flexbox, dan transition sudah",
                    "baku bertahun-tahun tanpa prefiks. Prefiks yang kamu lihat di",
                    "sebuah berkas biasanya salah satu dari dua hal: sisa kode lama yang",
                    "tidak pernah dibersihkan, atau tambahan otomatis dari alat bernama",
                    "Autoprefixer saat proyek dibangun. Keduanya berarti hal yang sama",
                    "buat kamu: perlu BISA MEMBACANYA, tidak perlu menirunya.",
                ],
            },
            {
                "heading": "Prefiks yang masih benar-benar dipakai hari ini",
                "code": """/* Menipiskan huruf di macOS. Tidak pernah dibakukan, dan tidak
   berpengaruh apa-apa di Windows maupun Linux. Dua baris ini
   sepasang: satu untuk Safari/Chrome, satu untuk Firefox di macOS. */
body {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

/* Memotong teks setelah 3 baris lalu memberi '...' sendiri.
   Keempat baris ini satu paket - hilang salah satu, tidak terjadi
   apa-apa sama sekali. Ini satu-satunya cara memotong per BARIS;
   text-overflow: ellipsis hanya bekerja untuk satu baris. */
.ringkasan {
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 3;
  overflow: hidden;
}

/* Menanggalkan rupa bawaan sistem operasi dari kontrol formulir
   sebelum menatanya sendiri. Yang berprefiks DULU, yang baku
   TERAKHIR, supaya versi baku yang menang di browser baru. */
select {
  -webkit-appearance: none;
  appearance: none;
  border: 1px solid #d8d8d8;
  border-radius: 6px;
  padding: 8px 12px;
}

/* Gulir bermomentum di iOS lama. Sudah tidak diperlukan sejak
   bertahun-tahun. Menemukannya adalah tanda berkasnya sudah tua -
   bukan tanda kamu perlu menambahkannya juga. */
.panel-lama {
  -webkit-overflow-scrolling: touch;
}""",
            },
            {
                "body": [
                    "@supports: SATU-SATUNYA CARA CSS BERTANYA",
                    "",
                    "CSS tidak punya if. Yang paling mendekati adalah @supports, dan",
                    "pertanyaannya cuma satu macam: 'browser, kamu mengerti deklarasi",
                    "ini atau tidak?'",
                    "",
                    "  @supports (display: grid) {",
                    "    .daftar { display: grid; }",
                    "  }",
                    "",
                    "Yang di dalam kurung WAJIB berbentuk deklarasi utuh - properti",
                    "beserta nilainya. @supports (display) saja selalu dianggap TIDAK",
                    "didukung, dan memang begitu seharusnya: sebuah browser bisa saja",
                    "mengerti display tapi tidak mengerti grid. Nilainyalah yang",
                    "menentukan jawaban, bukan nama propertinya.",
                    "",
                    "Bentuk-bentuk lainnya:",
                    "",
                    "  @supports not (display: grid) { }      kalau TIDAK mengerti",
                    "  @supports (a: b) and (c: d) { }        harus mengerti keduanya",
                    "  @supports (a: b) or (c: d) { }         salah satu saja cukup",
                    "  @supports selector(:has(*)) { }        menanyakan PEMILIH,",
                    "                                         bukan properti",
                    "",
                    "Tiap syarat wajib punya kurungnya sendiri, dan and tidak boleh",
                    "dicampur dengan or tanpa kurung tambahan yang memperjelas maksudmu:",
                    "tulis ((a: b) and (c: d)) or (e: f).",
                    "",
                    "BEDANYA DENGAN @media - INI YANG PALING SERING TERTUKAR",
                    "",
                    "Keduanya diawali @, keduanya menaruh syarat di dalam kurung, dan",
                    "keduanya membungkus aturan CSS biasa dengan kurung kurawal. Yang",
                    "ditanyakan sama sekali berbeda:",
                    "",
                    "  @media     bertanya tentang LAYAR dan lingkungannya - selebar",
                    "             apa, melintang atau tegak, sedang dicetak, temanya",
                    "             gelap atau terang.",
                    "  @supports  bertanya tentang BROWSERNYA - fitur ini kamu mengerti",
                    "             atau tidak.",
                    "",
                    "Jawaban @media berubah saat pemakai menyeret sudut jendelanya.",
                    "Jawaban @supports tidak pernah berubah selama halaman terbuka.",
                    "Keduanya boleh disarangkan satu di dalam yang lain:",
                    "",
                    "  @supports (display: grid) {",
                    "    @media (min-width: 720px) { .halaman { gap: 24px; } }",
                    "  }",
                    "",
                    "ARAHNYA SELALU: SEDERHANA DULU, BAGUS BELAKANGAN",
                    "",
                    "Tulis versi yang pasti jalan sebagai aturan biasa, lalu taruh versi",
                    "bagusnya DI DALAM @supports:",
                    "",
                    "  .daftar { display: block; }           semua browser dapat ini",
                    "  @supports (display: grid) { ... }     yang mampu dapat tambahannya",
                    "",
                    "Kalau dibalik - versi sederhana ditaruh di dalam @supports not(...)",
                    "dan versi bagusnya di luar - browser yang terlalu tua untuk",
                    "mengerti @supports akan MELEWATI SELURUH BLOK ITU. Yang paling",
                    "butuh cadangan justru satu-satunya yang tidak menerimanya.",
                    "",
                    "Jangan pula membungkus sesuatu yang sudah didukung di mana-mana.",
                    "@supports (display: flex) hari ini cuma menambah satu lapis kurung",
                    "kurawal tanpa satu pun manfaat.",
                    "",
                    "Dan ketahui batasnya: @supports memeriksa apakah deklarasinya BISA",
                    "DIBACA, bukan apakah hasilnya bagus. Untuk tahu sejak versi berapa",
                    "sebuah fitur aman dipakai, tempatnya bukan di dalam CSS melainkan",
                    "di caniuse.com, atau tabel 'Browser compatibility' di kaki tiap",
                    "halaman MDN.",
                ],
            },
            {
                "body": [
                    "PROPERTI LOGIS: 'KIRI' TERNYATA BUKAN NAMA YANG BENAR",
                    "",
                    "Nama seperti margin-left menganggap tulisan selalu mengalir ke",
                    "kanan. Bahasa Arab, Ibrani, dan Persia ditulis dari kanan ke kiri,",
                    "dan di halaman seperti itu 'kiri' berarti AKHIR baris, bukan",
                    "awalnya. Karena itu CSS punya satu set nama lagi yang tidak",
                    "menyebut arah mata angin sama sekali.",
                    "",
                    "Dasarnya dua sumbu bernama:",
                    "",
                    "  INLINE   arah teks MENGALIR.     Tulisan Indonesia: mendatar.",
                    "  BLOCK    arah baris BERTAMBAH.   Tulisan Indonesia: menurun.",
                    "",
                    "Nama itu diambil dari sesuatu yang sudah kamu kenal di materi",
                    "Display: elemen block bertumpuk ke BAWAH, elemen inline berbaris ke",
                    "SAMPING. Sumbunya dinamai persis dari situ, jadi tidak ada yang",
                    "baru untuk dihafal - cuma dipakai ulang.",
                    "",
                    "Tiap sumbu punya awal dan akhir: start dan end. Untuk tulisan",
                    "Indonesia, inline-start = kiri, inline-end = kanan,",
                    "block-start = atas, block-end = bawah.",
                    "",
                    "  Fisik                     Logis",
                    "  ----------------------    -----------------------------",
                    "  margin-top                margin-block-start",
                    "  margin-bottom             margin-block-end",
                    "  margin-left               margin-inline-start",
                    "  margin-right              margin-inline-end",
                    "  padding-top & -bottom     padding-block",
                    "  padding-left & -right     padding-inline",
                    "  border-left               border-inline-start",
                    "  width                     inline-size",
                    "  height                    block-size",
                    "  max-width                 max-inline-size",
                    "  top / bottom              inset-block-start / inset-block-end",
                    "  left / right              inset-inline-start / inset-inline-end",
                    "  text-align: left          text-align: start",
                    "  float: left               float: inline-start",
                    "",
                    "SATU TEBAKAN LIMA PULUH-LIMA PULUH YANG WAJIB KAMU MENANGKAN",
                    "",
                    "  padding-block: 1rem;      ATAS dan BAWAH",
                    "  padding-inline: 1rem;     KIRI dan KANAN",
                    "",
                    "Menebaknya terbalik berarti salah membaca seluruh tata letak sebuah",
                    "berkas, dan tidak ada apa pun di layar yang akan mengoreksimu. Yang",
                    "menolong tetap kata 'block' yang sudah kamu kenal: bertumpuk ke",
                    "bawah, jadi sumbunya menurun.",
                    "",
                    "Bentuk ringkas itu menerima satu atau dua nilai:",
                    "",
                    "  margin-inline: auto;      awal dan akhir sama",
                    "  margin-inline: 0 24px;    awal dulu, baru akhir",
                    "",
                    "margin-inline: auto adalah pengganti margin: 0 auto dari materi Box",
                    "Model - dengan satu beda yang penting. margin: 0 auto SEKALIAN",
                    "menolkan margin atas-bawah; margin-inline: auto tidak menyentuhnya",
                    "sama sekali. Syaratnya tetap sama: elemennya harus punya batas",
                    "lebar, jadi max-inline-size tetap wajib ada.",
                    "",
                    "inset MENGGANTIKAN EMPAT BARIS SEKALIGUS",
                    "",
                    "  top: 0; right: 0; bottom: 0; left: 0;   ->   inset: 0;",
                    "",
                    "Artinya 'melar memenuhi acuannya' - pola sehari-hari untuk lapisan",
                    "gelap di belakang dialog. Urutan nilainya sama persis dengan margin:",
                    "atas, kanan, bawah, kiri. Versi logisnya inset-block dan",
                    "inset-inline. Dan syaratnya juga sama seperti top dan left: hanya",
                    "berlaku pada elemen yang position-nya bukan static (materi",
                    "Position). inset: 0 pada elemen static tetap tidak melakukan apa-apa.",
                    "",
                    "JANGAN MENCAMPUR DUA GAYA UNTUK SISI YANG SAMA",
                    "",
                    "  .kartu { margin-left: 0; margin-inline-start: 16px; }",
                    "",
                    "Di halaman berbahasa Indonesia keduanya menunjuk sisi fisik yang",
                    "sama. Yang menang bukan yang 'lebih spesifik', melainkan yang",
                    "ditulis BELAKANGAN - artinya menyisipkan satu baris di tempat yang",
                    "salah bisa mematikan baris di atasnya tanpa jejak. Pilih satu gaya",
                    "dan pakai itu saja sepanjang berkas.",
                    "",
                    "Jangan pula kaget kalau tidak semuanya punya versi logis:",
                    "background-position, box-shadow, dan transform masih memakai arah",
                    "fisik apa adanya.",
                ],
            },
            {
                "heading": "Satu berkas gaya modern: logis di luar, @supports di dalam",
                "body": [
                    "Kenapa proyek baru memakai semua ini meski tidak pernah berencana",
                    "menerjemahkan halamannya: berkas gaya yang sama langsung benar saat",
                    "<html dir=\"rtl\"> dipasang, tanpa satu pun aturan ditulis ulang.",
                    "Dan bahkan tanpa itu, namanya lebih jujur - yang kamu maksud memang",
                    "'jarak di sisi awal teks', bukan 'jarak di kiri layar'.",
                ],
                "code": """/* Tidak ada satu pun kata 'left' atau 'right' di berkas ini. */

:root {
  --s2: 8px;
  --s3: 12px;
  --s4: 16px;
  --s5: 24px;
  --garis: #e4e6ea;
  --sorot: #1a4fa0;
}

/* --- Dasar: berlaku di browser apa pun, tanpa syarat --- */

.daftar {
  display: block;
}

.kartu {
  position: relative;
  max-inline-size: 68ch;         /* dulu: max-width */
  margin-inline: auto;           /* dulu: margin kiri-kanan otomatis */
  margin-block-end: var(--s4);   /* dulu: margin-bottom */
  padding-block: var(--s4);      /* ATAS dan BAWAH */
  padding-inline: var(--s5);     /* KIRI dan KANAN, di tulisan Indonesia */
  border: 1px solid var(--garis);
  border-radius: var(--s2);
  text-align: start;             /* dulu: text-align: left */
}

/* Garis penanda di sisi AWAL teks. Pada halaman kanan-ke-kiri ia
   berpindah ke kanan sendiri, tanpa satu aturan tambahan pun. */
.kartu-penting {
  border-inline-start: 4px solid var(--sorot);
  padding-inline-start: var(--s3);
}

.lencana {
  position: absolute;
  inset-block-start: var(--s3);  /* dulu: top */
  inset-inline-end: var(--s3);   /* dulu: right */
}

/* inset: 0 aman dipakai apa adanya: nol di keempat sisi tidak
   berubah arti ke mana pun teksnya mengalir. */
.tirai {
  position: absolute;
  inset: 0;
  background: rgba(0, 0, 0, 0.45);
}

/* --- Tambahan, hanya untuk browser yang memang mengerti --- */

@supports (display: grid) and (gap: 1rem) {
  .daftar {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: var(--s4);
  }

  .kartu {
    max-inline-size: none;
    margin-block-end: 0;
  }
}""",
            },
        ],
    },
    {
        "title": "26. Container Queries dan CSS Nesting",
        "sections": [
            {
                "body": [
                    "Materi 'Responsif: media query' menjawab satu pertanyaan: seberapa lebar",
                    "LAYARNYA. Tapi komponen yang sama sering dipasang di dua tempat berbeda",
                    "di halaman yang sama - sidebar sempit di satu sisi, area utama yang",
                    "lebar di sisi lain. Media query tidak bisa membedakan itu: ia cuma tahu",
                    "lebar viewport, bukan lebar KOTAK tempat komponennya berada.",
                    "",
                    "  @media (min-width: 600px) { .kartu { display: flex; } }",
                    "  Kartu ini jadi flex begitu LAYAR lebih dari 600px - walau kartunya",
                    "  sendiri dipasang di sidebar 250px yang jelas tidak muat.",
                    "",
                    "Container query memindahkan pertanyaannya: bukan 'seberapa lebar layar',",
                    "tapi 'seberapa lebar WADAH komponen ini'. Materi ini juga menutup satu",
                    "gaya penulisan CSS yang belum disebut sama sekali: menyarangkan aturan",
                    "di dalam aturan lain, langsung didukung CSS modern, tanpa Sass/Less.",
                ],
            },
            {
                "heading": "Container queries: bereaksi ke wadah, bukan ke layar",
                "body": [
                    "Dua langkah wajib. Pertama, elemen INDUKnya (bukan komponennya sendiri)",
                    "harus dinyatakan sebagai container:",
                    "",
                    "  .slot-widget { container-type: inline-size; }",
                    "",
                    "container-type: inline-size berarti 'ukur lebar elemen ini, siapkan",
                    "untuk ditanyai'. Tanpa baris ini, @container di bawah tidak punya apa",
                    "pun untuk diukur dan tidak akan pernah aktif.",
                    "",
                    "Kedua, tulis @container - bentuknya mirip @media tapi mengukur WADAH",
                    "terdekat yang punya container-type, bukan layar:",
                    "",
                    "  @container (min-width: 400px) {",
                    "      .widget .judul { font-size: 1.5rem; }",
                    "  }",
                    "",
                    "Container BOLEH diberi nama lewat container-name, berguna kalau ada",
                    "beberapa container bersarang dan kamu perlu menunjuk yang mana:",
                    "",
                    "  .slot-widget { container-type: inline-size; container-name: kartu; }",
                    "  @container kartu (min-width: 400px) { ... }",
                    "",
                    "Satuan cqw/cqh/cqi/cqb: sepupu vw/vh, tapi relatif ke CONTAINER, bukan",
                    "viewport. 10cqw = 10% dari lebar wadahnya. Berguna untuk font-size atau",
                    "spacing yang harus ikut membesar/mengecil bersama wadah, bukan layar.",
                    "",
                    "JEBAKAN: elemen tidak bisa jadi container UNTUK DIRINYA SENDIRI - aturan",
                    "di dalam @container mengubah ISI container, bukan container itu sendiri",
                    "berdasarkan ukurannya sendiri (itu akan jadi lingkaran tanpa ujung, dan",
                    "browser sengaja tidak mengizinkannya).",
                ],
                "code": """/* Induk jadi container: siap diukur */
.slot-widget {
  container-type: inline-size;
}

/* Tampilan default: sempit, ditumpuk vertikal */
.widget .judul {
  font-size: 1rem;
}

/* Begitu WADAHNYA (bukan layar) minimal 400px, ubah tata letak */
@container (min-width: 400px) {
  .widget {
    display: flex;
    gap: 1rem;
  }

  .widget .judul {
    font-size: 1.5rem;
  }
}""",
            },
            {
                "heading": "CSS Nesting: aturan bersarang tanpa preprocessor",
                "body": [
                    "Kalau kamu pernah lihat kode Sass/Less, bentuk ini akan terasa familiar -",
                    "bedanya ini CSS ASLI, langsung dibaca browser, tanpa langkah build:",
                    "",
                    "  .navigasi {",
                    "      display: flex;",
                    "",
                    "      & a { color: inherit; }",
                    "      &:hover { background: #f0f0f0; }",
                    "  }",
                    "",
                    "& menunjuk balik ke pemilih induknya (.navigasi). Kapan & WAJIB ditulis:",
                    "saat langsung digabung tanpa spasi dengan pseudo-class atau elemen lain",
                    "- &:hover berarti '.navigasi:hover', BUKAN '.navigasi :hover' (dua hal",
                    "yang beda total: yang kedua mencari keturunan yang di-hover, bukan",
                    "dirinya sendiri). Kapan & boleh dihilangkan: untuk turunan biasa dengan",
                    "spasi, 'a { ... }' di dalam '.navigasi' otomatis berarti '.navigasi a'.",
                    "",
                    "JEBAKAN spesifisitas: nesting yang dalam diam-diam menaikkan spesifisitas",
                    "tiap aturan yang dihasilkan, sama seperti menulis pemilihnya panjang-panjang",
                    "dengan tangan. Tiga tingkat nesting menghasilkan aturan sespesifik tiga",
                    "class digabung - dan itu akan sulit ditimpa nanti, persis masalah yang",
                    "sudah dibahas materi 'Pemilih Modern dan Lapisan Cascade' soal :is()/:where().",
                    "Aturan praktis: dua tingkat nesting cukup untuk kebanyakan komponen; kalau",
                    "sampai empat tingkat, itu tanda strukturnya perlu dipecah, bukan disarangkan.",
                    "",
                    "CATATAN REPO INI: pemeriksa latihan CSS di aplikasi ini (struktur.py) belum",
                    "mendukung PENGURAIAN nesting di luar at-rule seperti @media/@container - jadi",
                    "tidak ada latihan otomatis untuk nesting di materi ini. Di browser sungguhan,",
                    "sintaksnya tetap sah dan berjalan normal.",
                ],
                "code": """.kartu-produk {
  display: flex;
  gap: 1rem;
  border: 1px solid #ddd;

  /* & wajib: langsung menempel ke pemilih induk, bukan keturunannya */
  &:hover {
    border-color: #333;
  }

  &.terjual-habis {
    opacity: 0.5;
  }

  /* & opsional di sini: turunan dengan spasi tetap berlaku tanpa & */
  .judul {
    font-weight: bold;
  }

  /* nesting media query di dalam pemilih juga sah */
  @media (max-width: 480px) {
    flex-direction: column;
  }
}""",
            },
            {
                "heading": "Kapan pakai yang mana",
                "body": [
                    "Media query    : layout seluruh HALAMAN berubah mengikuti ukuran layar",
                    "                 (mis. sidebar disembunyikan di layar sempit).",
                    "Container query: satu KOMPONEN harus tampil beda tergantung wadahnya -",
                    "                 dipakai saat komponen yang sama dipasang di lebih dari",
                    "                 satu tempat dengan lebar berbeda (widget, kartu, sidebar).",
                    "Nesting        : soal PENULISAN, bukan soal kapan aktif - dipakai untuk",
                    "                 mengelompokkan aturan yang berhubungan erat (elemen +",
                    "                 pseudo-class + turunan langsungnya) supaya tidak mengetik",
                    "                 ulang nama class yang sama berkali-kali.",
                    "",
                    "Ketiganya bisa dipakai bersamaan tanpa konflik - container query dan",
                    "media query sering berdampingan di proyek nyata, dan aturan di dalam",
                    "@container boleh ditulis bersarang juga.",
                ],
            },
        ],
    },
    {
        "title": "27. Membaca CSS di Proyek Nyata",
        "sections": [
            {
                "body": [
                    "Buka satu proyek web sungguhan di GitHub, lalu buka berkas gayanya. Yang",
                    "kemungkinan besar kamu lihat:",
                    "",
                    "  .kartu-produk__judul--sorot { color: #1a4fa0; }",
                    "",
                    "Kabar baiknya: tidak ada satu pun sintaks baru di baris itu. Itu tetap",
                    "pemilih class biasa dari materi 2, dan browser membacanya persis seperti",
                    ".kartu. Yang membuatnya terlihat asing cuma NAMA class-nya - dan nama itu",
                    "dipilih manusia, bukan dituntut browser.",
                    "",
                    "BEM: BLOCK, ELEMENT, MODIFIER",
                    "",
                    "BEM adalah kesepakatan penamaan class yang paling banyak dipakai orang:",
                    "",
                    "  .kartu                BLOCK    benda utuh yang berdiri sendiri",
                    "  .kartu__judul         ELEMENT  bagian yang cuma ada DI DALAM blok itu",
                    "  .kartu--sorot         MODIFIER varian atau keadaan blok itu",
                    "  .kartu__judul--besar  element yang punya modifier sendiri",
                    "",
                    "Dua garis bawah dibaca 'milik'. Dua tanda minus dibaca 'versi'.",
                    "",
                    "Ini BUKAN sintaks CSS. Browser sama sekali tidak tahu apa itu BEM: yang ia",
                    "lihat cuma nama class panjang berisi garis bawah dan minus - dua karakter",
                    "yang memang boleh ada di dalam nama class. Tidak ada yang memaksakannya,",
                    "dan tidak ada yang memeriksanya. Salah ketik jadi .kartu_judul (satu garis",
                    "bawah) tetap CSS yang sah, tetap tanpa pesan error, dan aturannya cuma",
                    "diam karena tidak ada elemen yang cocok - persis sebab nomor 1 di daftar",
                    "periksa materi 12.",
                    "",
                    "JEBAKAN: '--sorot' DI SINI BUKAN VARIABEL CSS",
                    "",
                    "Bentuknya persis sama dengan custom property di materi 12, dan keduanya",
                    "akan berdiri berdampingan di berkas yang sama. Yang membedakan cuma",
                    "POSISINYA:",
                    "",
                    "  .kartu--sorot { ... }     dua minus di dalam PEMILIH   -> modifier BEM",
                    "  --sorot: #1a4fa0;         dua minus di posisi PROPERTI -> variabel CSS",
                    "  color: var(--sorot);      dua minus di dalam var()     -> variabel CSS",
                    "",
                    "Variabel CSS selalu berdiri sendiri sebagai sebuah nama, di dalam kurawal",
                    "atau di dalam var(). Modifier BEM selalu menempel di belakang nama class,",
                    "di depan kurawal. Sekali kamu tahu di mana harus melihat, keduanya tidak",
                    "pernah tertukar lagi.",
                    "",
                    "KENAPA ORANG REPOT-REPOT MELAKUKANNYA",
                    "",
                    "Perhatikan bahwa SEMUA pemilih di atas cuma satu class. Tidak ada",
                    "'.kartu .isi h3', tidak ada #id. Artinya semuanya berspesifisitas (0,1,0)",
                    "alias rata. Begitu spesifisitasnya rata, yang menentukan tinggal urutan",
                    "penulisan (materi 2), dan itu jauh lebih mudah diikuti daripada perlombaan",
                    "pemilih yang saling menimpa. Persediaan 'ruang di atasmu' tidak pernah",
                    "terpakai sama sekali.",
                    "",
                    "Untung kedua: nama class menyebut pemiliknya. Melihat .kartu__judul di",
                    "HTML, kamu langsung tahu blok mana yang mengurusnya, dan mencari",
                    "'.kartu__' di berkas gaya mengumpulkan seluruh aturannya sekaligus. Itu",
                    "kelanjutan langsung dari dua nasihat di materi 12: beri nama berdasarkan",
                    "APA benda itu, dan satu komponen satu blok berurutan.",
                    "",
                    "Harganya: nama class jadi panjang dan HTML-nya jadi ramai. Itu tukarannya,",
                    "dan orang menerimanya karena berkas gaya yang sudah tidak bisa ditimpa",
                    "lagi jauh lebih mahal.",
                ],
            },
            {
                "heading": "Bentuk berkas gaya sebuah proyek kecil",
                "body": [
                    "Berkas gaya proyek nyata bisa seribu baris. Jangan dibaca dari atas ke",
                    "bawah seperti novel. Hampir semuanya tersusun dalam urutan yang sama",
                    "(materi 12), jadi bacalah lompat-lompat:",
                    "",
                    "  1. Cari :root lebih dulu. Daftar variabelnya menceritakan SELURUH sistem",
                    "     desainnya dalam dua puluh baris - berapa warna yang dipakai, seberapa",
                    "     lapang jaraknya, sebesar apa lengkungan sudutnya. Sesudah itu kamu",
                    "     bisa menebak isi berkasnya sebelum membacanya.",
                    "  2. Baru turun ke blok komponen, dan cari nama class yang benar-benar",
                    "     kamu lihat di HTML - bukan yang kebetulan lewat di layar.",
                    "  3. @media hampir selalu di kaki berkas. Kalau ada yang berubah pada layar",
                    "     sempit, jawabannya di situ, bukan di blok komponennya.",
                    "",
                    "Di kepala berkas biasanya ada beberapa aturan aneh yang tidak mengurus",
                    "komponen apa pun. Itu reset, dan dijelaskan di bagian berikutnya.",
                ],
                "code": """/* 1. Reset: meratakan bawaan browser dari materi 1 */
body,
h1,
h2,
p,
figure {
  margin: 0;
}

*,
*::before,
*::after {
  box-sizing: border-box;
}

/* 2. Variabel: seluruh sistem desainnya, dalam satu blok */
:root {
  --warna-latar: #ffffff;
  --warna-teks: #1c1e22;
  --warna-garis: #e4e6ea;
  --warna-sorot: #1a4fa0;
  --s2: 8px;
  --s4: 16px;
  --s5: 24px;
  --bulat: 8px;
}

/* 3. Elemen dasar */
body {
  background: var(--warna-latar);
  color: var(--warna-teks);
  font-family: system-ui, sans-serif;
  line-height: 1.6;
}

/* 4. Komponen, dinamai dengan BEM */
.kartu {
  background: var(--warna-latar);
  border: 1px solid var(--warna-garis);
  border-radius: var(--bulat);
  padding: var(--s5);
}

.kartu__judul {
  color: var(--warna-sorot);
  font-size: 20px;
  margin-bottom: var(--s2);
}

.kartu__isi {
  margin-bottom: var(--s4);
}

/* Modifier ditulis SESUDAH bloknya: menang lewat urutan, bukan spesifisitas */
.kartu--sorot {
  border-color: var(--warna-sorot);
}

/* 5. Media query, di kaki berkas */
@media (max-width: 600px) {
  .kartu {
    padding: var(--s4);
  }
}""",
            },
            {
                "body": [
                    "TIGA HAL YANG MEMBUAT BERKAS .css SUNGGUHAN TERLIHAT ASING",
                    "",
                    "YANG PERTAMA: ATURAN DI DALAM ATURAN (nesting)",
                    "",
                    "  .kartu {",
                    "    padding: 24px;",
                    "    &:hover { border-color: crimson; }",
                    "    .kartu__judul { color: #1a4fa0; }",
                    "  }",
                    "",
                    "Bertahun-tahun bentuk ini cuma ada di Sass. Sejak 2023 browser besar",
                    "menerimanya di berkas .css biasa, jadi sekarang kamu akan menemuinya di",
                    "kedua tempat. Artinya sama persis dengan tiga aturan datar ini:",
                    "",
                    "  .kartu { padding: 24px; }",
                    "  .kartu:hover { border-color: crimson; }",
                    "  .kartu .kartu__judul { color: #1a4fa0; }",
                    "",
                    "& berarti 'pemilih induknya', dan ia ditempel TANPA SPASI. Ada atau",
                    "tidaknya & menentukan hasil:",
                    "",
                    "  &:hover  ->  .kartu:hover    kartu itu sendiri saat disentuh",
                    "  :hover   ->  .kartu :hover   apa pun DI DALAM kartu saat disentuh",
                    "",
                    "Itu perbedaan spasi yang sama dengan .a.b lawan .a .b di materi 2, cuma",
                    "berpindah tempat.",
                    "",
                    "Satu jebakan yang perlu diketahui sekarang supaya tidak bingung nanti: di",
                    "CSS biasa, & boleh berdiri sendiri atau diikuti tanda seperti :hover dan",
                    ".lain, tapi TIDAK boleh ditempeli potongan teks. Bentuk &__judul yang",
                    "banyak kamu lihat itu khas Sass, dan tidak sah di berkas .css.",
                    "",
                    "Catatan jujur soal alat ini: pembaca CSS di aplikasi ini masih membaca",
                    "berkas datar. Kalau kamu menekan Jalankan pada berkas bersarang, daftar",
                    "aturannya akan terbaca kacau. Itu batas alatnya, bukan tanda berkasmu",
                    "salah - browser tetap memahaminya.",
                    "",
                    "YANG KEDUA: BARIS-BARIS ANEH DI KEPALA BERKAS",
                    "",
                    "  body, h1, h2, p, figure { margin: 0; }",
                    "  *, *::before, *::after { box-sizing: border-box; }",
                    "",
                    "Ini RESET. Ingat materi 1: halaman tanpa CSS pun sudah bergaya, karena",
                    "tiap browser punya lembar gaya bawaan. Bawaan itu berguna, tapi sedikit",
                    "berbeda antar browser dan sering mengganggu - margin bawaan <h1> dan <p>",
                    "menciptakan jarak yang tidak kamu minta, dan box-sizing bawaan membuat",
                    "padding menambah lebar kotak (materi 5).",
                    "",
                    "Dua mazhab, dan namanya sering tertukar:",
                    "  - RESET membuang hampir semua bawaan, lalu kamu bangun dari nol. Yang",
                    "    legendaris namanya Meyer reset; kebanyakan proyek sekarang memakai",
                    "    versi pendek buatan sendiri seperti dua baris di atas.",
                    "  - NORMALIZE (normalize.css) tidak membuang apa-apa, cuma MERATAKAN",
                    "    perbedaan antar browser dan membiarkan bawaan yang masuk akal.",
                    "",
                    "Kalau sebuah halaman tiba-tiba kehilangan seluruh jarak antar paragraf,",
                    "atau judulnya jadi seukuran teks biasa, jangan cari salahnya di komponen.",
                    "Lihat reset di kepala berkas: yang membuang, dia juga yang bertanggung",
                    "jawab mengembalikan.",
                    "",
                    "YANG KETIGA: BERKAS SATU BARIS DAN NAMA CLASS TERACAK",
                    "",
                    "  .kartu{padding:24px;border:1px solid #e4e6ea}.kartu__judul{color:#1a4fa0}",
                    "",
                    "Berkas seperti itu TERMINIFIKASI: spasi, baris baru, dan komentarnya",
                    "dibuang supaya unduhannya kecil. Namanya sering berakhiran .min.css, dan",
                    "di baris terakhirnya kadang menempel /*# sourceMappingURL=gaya.css.map */.",
                    "",
                    "Tanda lain bahwa kamu sedang membaca KELUARAN alat, bukan tulisan tangan:",
                    "  - nama class seperti Button_root__x7f2 atau css-1q2w3e",
                    "  - berkasnya duduk di folder bernama dist/, build/, atau _next/",
                    "  - ada komentar 'generated' atau 'DO NOT EDIT' di kepalanya",
                    "",
                    "Jangan menyuntingnya. Perubahanmu akan hilang pada pembangunan berikutnya,",
                    "tanpa satu pun peringatan. Cari berkas SUMBERnya - biasanya di src/ atau",
                    "styles/, berakhiran .css, .scss, atau .module.css - dan sunting di situ.",
                ],
            },
            {
                "heading": "gaya.scss dan gaya.css hasil kompilasinya",
                "body": [
                    "BERKAS .scss BUKAN CSS",
                    "",
                    "Sass adalah bahasa terpisah yang HASILNYA CSS. Berkas .scss tidak bisa",
                    "ditautkan dengan <link>; browser tidak mengerti sedikit pun isinya. Ia",
                    "harus DIKOMPILASI dulu jadi berkas .css, dan berkas .css itulah yang",
                    "ditautkan ke halaman. Yang kamu sunting satu berkas, yang dibaca browser",
                    "berkas lain.",
                    "",
                    "Sekalian menutup satu keraguan: materi 1 bilang CSS tidak punya bentuk //.",
                    "Itu masih benar. Di berkas .scss kamu akan melihat // di mana-mana, dan",
                    "itu tidak melanggar apa pun - karena berkas itu memang bukan CSS. Komentar",
                    "// bahkan tidak ikut ke hasil kompilasinya, sedangkan /* */ ikut.",
                    "",
                    "Yang akan terlihat asing di dalam sebuah .scss:",
                    "  //               komentar satu baris, lenyap saat dikompilasi",
                    "  $sorot: #1a4fa0  variabel Sass, habis dipakai sebelum sampai ke browser",
                    "                   (bedanya dengan var(--...) dijelaskan di materi 12)",
                    "  @mixin + @include  potongan deklarasi yang bisa ditempel berulang kali",
                    "  @extend          menyalin isi aturan lain ke dalam aturan ini",
                    "  @use / @import   menarik berkas .scss lain jadi satu",
                    "  &__judul         & ditempeli teks -> menyusun nama BEM",
                    "",
                    "Baris terakhir itu yang paling sering membingungkan: di dalam blok .kartu,",
                    "'&__judul' menjadi '.kartu__judul'. Jadi Sass dan BEM saling melengkapi,",
                    "dan itu sebabnya keduanya hampir selalu muncul bersama.",
                    "",
                    "Kenapa banyak 'CSS' di GitHub sebenarnya .scss? Karena bertahun-tahun CSS",
                    "biasa belum punya variabel maupun aturan bersarang, sedangkan Sass sudah.",
                    "Sekarang CSS punya keduanya, tapi berkas lama tidak menulis ulang dirinya",
                    "sendiri. Bandingkan dua berkas di bawah: yang kiri ditulis orang, yang",
                    "kanan dihasilkan mesin dari yang kiri.",
                ],
                "code": """/* ==== File: gaya.scss ==== */
// Ditulis manusia. Tidak bisa ditautkan dengan <link>.
$sorot: #1a4fa0;
$garis: #e4e6ea;

@mixin kotak($jarak) {
  border: 1px solid $garis;
  padding: $jarak;
}

.kartu {
  @include kotak(24px);
  border-radius: 8px;

  &__judul {
    color: $sorot;
    font-size: 20px;
  }

  &--sorot {
    border-color: $sorot;
  }

  &:hover {
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  }
}

/* ==== File: gaya.css ==== */
/* Dihasilkan compiler dari berkas di atas. Ini yang ditautkan <link>.
   Perhatikan: $sorot sudah lenyap, berganti nilainya. Komentar // juga
   tidak ikut. Nama BEM-nya sudah tersusun utuh. */
.kartu {
  border: 1px solid #e4e6ea;
  padding: 24px;
  border-radius: 8px;
}

.kartu__judul {
  color: #1a4fa0;
  font-size: 20px;
}

.kartu--sorot {
  border-color: #1a4fa0;
}

.kartu:hover {
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}""",
            },
            {
                "heading": "Yang sebenarnya dilakukan class utility",
                "body": [
                    "TIGA MAZHAB LAIN YANG PASTI KAMU TEMUI",
                    "",
                    "UTILITY-FIRST (Tailwind CSS). Tidak ada berkas gaya berisi .kartu sama",
                    "sekali. Gayanya ditulis langsung di atribut class, di HTML atau di JSX:",
                    "",
                    "  <div class=\"flex items-center gap-4 rounded-lg p-6 bg-white\">",
                    "    <h3 class=\"text-lg font-semibold\">Judul</h3>",
                    "  </div>",
                    "",
                    "Tiap nama class di situ berarti PERSIS SATU deklarasi: flex adalah",
                    "display: flex, gap-4 adalah gap: 1rem, p-6 adalah padding: 1.5rem. Jadi",
                    "class di <div> itu bukan bahasa baru - itu enam deklarasi CSS yang kamu",
                    "sudah tahu semuanya, cuma dipanggil lewat nama pendek. Yang perlu dihafal",
                    "cuma kamusnya, dan kamus itu ada di dokumentasinya.",
                    "",
                    "CSS MODULES. Berkas bernama Kartu.module.css, isinya CSS biasa dengan nama",
                    "class pendek seperti .root atau .judul. Saat dibangun, tiap nama diberi",
                    "akhiran acak supaya mustahil bertabrakan dengan komponen lain - itu",
                    "sebabnya di halaman jadi kamu melihat class Kartu_root__x7f2. Nama itu",
                    "tidak diketik siapa pun dan berubah tiap kali dibangun ulang, jadi jangan",
                    "pernah menargetkannya di CSS.",
                    "",
                    "CSS-IN-JS (styled-components, Emotion). Gayanya tinggal di dalam berkas",
                    ".js atau .jsx, bukan di berkas .css:",
                    "",
                    "  const Kartu = styled.div`",
                    "    padding: 24px;",
                    "    border-radius: 8px;",
                    "  `;",
                    "",
                    "Isi di antara sepasang tanda petik terbalik (backtick) itu CSS biasa -",
                    "properti dan nilai yang persis sama.",
                    "",
                    "SEMUA INI MAZHAB PENULISAN, BUKAN BAHASA LAIN",
                    "",
                    "Di bawah ketiganya, yang sampai ke browser tetap satu hal yang sama:",
                    "pemilih, properti, nilai, cascade, box model, flexbox, grid. Tailwind",
                    "tidak menghapus spesifisitas; CSS Modules tidak mengubah box model;",
                    "styled-components tidak membuat gap: 1rem berarti hal lain.",
                    "",
                    "Jadi tidak ada satu pun yang kamu pelajari di dua belas materi sebelumnya",
                    "yang jadi usang. Yang berbeda cuma di mana teksnya diketik dan siapa yang",
                    "memberi nama class-nya. Dan saat sebuah halaman salah tampil, di mazhab",
                    "mana pun, pertanyaannya tetap tiga yang itu juga (materi 12): kotaknya",
                    "sebesar apa, ia ikut alur atau tidak, dan aturan mana yang menang.",
                ],
                "code": """/* Baris Tailwind di HTML:
 * <div class="flex items-center gap-4 rounded-lg p-6 bg-white">
 *
 * Enam class itu kira-kira didefinisikan begini. Satu class, satu deklarasi:
 */
.flex { display: flex; }
.items-center { align-items: center; }
.gap-4 { gap: 1rem; }
.rounded-lg { border-radius: 0.5rem; }
.p-6 { padding: 1.5rem; }
.bg-white { background-color: #ffffff; }

/* Berkas gaya buatan sendiri, hasil tampilannya sama persis.
 * Bedanya bukan kemampuan, tapi siapa yang memberi nama:
 */
.kartu {
  display: flex;
  align-items: center;
  gap: 1rem;
  border-radius: 0.5rem;
  padding: 1.5rem;
  background-color: #ffffff;
}""",
            },
        ],
    },
]
