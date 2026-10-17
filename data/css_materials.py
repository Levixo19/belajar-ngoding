CSS_MATERIALS = [
    {
        "title": "1. Apa Itu CSS & Tiga Cara Menautkannya",
        "sections": [
            {
                "body": [
                    "HTML menentukan apa isi halamanmu. CSS menentukan tampilannya: warna,",
                    "ukuran huruf, jarak, dan tata letak.",
                    "",
                    "CSS itu singkatan dari Cascading Style Sheets. Kata cascading artinya",
                    "mengalir bertingkat, kayak air terjun. Kata ini penting, dan artinya",
                    "dibahas di materi 2.",
                    "",
                    "Tanpa satu baris CSS pun, halaman HTML tetap tampil rapi seadanya.",
                    "Judulnya besar, tautannya biru dan bergaris bawah, paragrafnya",
                    "berjarak. Itu karena tiap browser punya lembar gaya bawaan, namanya",
                    "user agent stylesheet.",
                    "",
                    "CSS yang kamu tulis menimpa gaya bawaan itu. Kamu nggak mulai dari",
                    "nol. Jadi halaman nggak pernah tampil polos total, dan kadang",
                    "yang perlu kamu lakukan justru mematikan gaya bawaan. Contohnya",
                    "list-style: none untuk membuang titik di depan butir daftar.",
                    "",
                    "Satu aturan CSS bentuknya begini:",
                    "",
                    "  p { color: red; }",
                    "  ^   ^^^^^  ^^^",
                    "  |   |      nilai",
                    "  |   properti",
                    "  pemilih (selector)",
                    "",
                    "Istilahnya:",
                    "  - Pemilih (selector) menentukan elemen mana yang kena aturan ini.",
                    "  - Deklarasi adalah pasangan properti: nilai.",
                    "  - Satu aturan boleh berisi banyak deklarasi, dipisah titik koma.",
                    "",
                    "Deklarasi terakhir boleh nggak pakai titik koma. Tapi tetap tulis aja",
                    "titik komanya. Kalau besok kamu menambah baris di bawahnya dan titik",
                    "komanya nggak ada, aturan yang tadinya jalan bisa ikut rusak tanpa",
                    "kamu sadari.",
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
                    "Tiga cara itu, diurutkan dari yang paling jelek ke yang paling baik:",
                    "",
                    "  1. Inline, yaitu atribut style yang ditulis langsung di elemennya.",
                    "       <h1 style=\"color: darkred\">",
                    "     Gayanya cuma kena satu elemen itu. Nggak bisa dipakai ulang,",
                    "     nggak bisa pakai :hover, dan paling susah ditimpa (penjelasannya",
                    "     di materi 2). Pakai cuma kalau nilainya dihitung oleh program.",
                    "  2. Blok <style> di dalam <head>.",
                    "     Berlaku untuk seluruh halaman itu aja. Cocok untuk contoh kecil",
                    "     dan halaman sekali pakai.",
                    "  3. Berkas terpisah, disambung lewat",
                    "     <link rel=\"stylesheet\" href=\"gaya.css\">.",
                    "     Cara ini yang dipakai di proyek sungguhan. Alasannya:",
                    "       - Satu berkas bisa menata semua halaman. Ganti warna sekali,",
                    "         lima puluh halaman ikut berubah.",
                    "       - Browser menyimpan berkasnya (namanya cache), jadi halaman",
                    "         kedua dan seterusnya nggak perlu mengunduh gayanya lagi.",
                    "       - Isi dan tampilan terpisah, jadi HTML-nya tetap enak dibaca.",
                    "",
                    "<link> ditulis di dalam <head>. Atribut rel=\"stylesheet\" wajib ada.",
                    "Tanpa atribut itu, browser nggak tahu bahwa berkas tadi lembar gaya,",
                    "jadi berkasnya didiamkan aja.",
                    "",
                    "Salah nulis nama berkas juga nggak memunculkan pesan apa pun di",
                    "halaman. Yang kamu lihat cuma halaman polos tanpa gaya.",
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
                    "Ada satu sifat CSS yang perlu kamu tahu dari awal: CSS nggak pernah",
                    "ngasih pesan error.",
                    "",
                    "Salah ketik colr: red nggak menghentikan apa pun. Browser membuang",
                    "deklarasi yang nggak dia mengerti, lalu lanjut membaca sisanya",
                    "seolah nggak terjadi apa-apa. Ini disengaja, supaya halaman lama",
                    "tetap jalan di browser baru. Akibatnya buat kamu: kesalahanmu",
                    "kelihatan seperti \"aturannya nggak mempan\".",
                    "",
                    "Kalau satu deklarasi rusak, cuma baris itu yang dibuang. Aturan lain",
                    "di blok yang sama tetap berlaku. Lain cerita kalau yang hilang kurung",
                    "kurawal. Browser bisa membuang beberapa aturan sekaligus, dan",
                    "hasilnya setengah halaman kehilangan gaya tanpa sebab yang jelas.",
                    "",
                    "Di aplikasi ini, berkas .css nggak dijalankan seperti program.",
                    "Isinya dibaca, lalu dicetak sebagai daftar aturan. Pemilihnya di",
                    "kiri, propertinya menjorok dua spasi di bawahnya:",
                    "",
                    "  body",
                    "    background-color: #f7f7f5",
                    "    color: #23252b",
                    "",
                    "Jadi tekan Jalankan untuk ngecek bahwa yang kamu tulis memang terbaca",
                    "sebagai CSS. Kelihatan benar di layar belum tentu terbaca benar.",
                    "Kalau ada aturan yang nggak muncul di daftar itu, browser juga nggak",
                    "akan melihatnya.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Situs sekolah, toko online, atau portal desa biasanya punya puluhan",
                    "halaman yang tampil seragam: warna judul sama, huruf sama, jarak sama.",
                    "Keseragaman itu datang dari satu berkas gaya yang disambung ke semua",
                    "halaman lewat <link>. Waktu warna judulnya mau diganti, yang disunting",
                    "cuma berkas itu.",
                    "",
                    "Kasus kecil: situs profil sebuah SMP punya delapan halaman (beranda,",
                    "profil, guru, galeri, dan lainnya). Tiap halaman menyalin blok <style>",
                    "yang sama, berisi h1 { color: #7a1f1f; }. Kepala sekolah minta warna",
                    "judul diganti jadi biru tua di semua halaman.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pahami masukan dan keluarannya. Masukannya satu aturan yang",
                    "     disalin delapan kali. Keluarannya satu tempat untuk menggantinya.",
                    "  2. Pindahkan isi blok <style> ke berkas gaya.css, lalu hapus blok",
                    "     itu dari kedelapan halaman.",
                    "  3. Di <head> tiap halaman, pasang satu baris ini:",
                    "      <link rel=\"stylesheet\" href=\"gaya.css\">",
                    "  4. Ganti warnanya sekali aja di gaya.css: h1 { color: navy; }.",
                    "  5. Periksa kasus pinggir: judul yang masih punya atribut",
                    "     style=\"color: darkred\". Gaya inline paling susah ditimpa, jadi",
                    "     judul itu tetap merah tua. Hapus atributnya.",
                    "",
                    "Jebakan: kalau rel=\"stylesheet\" lupa ditulis, browser mendiamkan",
                    "berkasnya, dan kedelapan halaman tampil polos tanpa pesan apa pun.",
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
                    "Hati-hati dengan spasi. Satu spasi di pemilih mengubah artinya:",
                    "  .a .b   -> elemen ber-class b DI DALAM elemen ber-class a",
                    "  .a.b    -> SATU elemen yang punya kedua class sekaligus",
                    "Yang pertama nyari dua elemen, satu di dalam yang lain. Yang kedua",
                    "nyari satu elemen yang punya dua class.",
                    "",
                    "Pemilih atribut memilih elemen berdasarkan atributnya:",
                    "  a[target]             punya atribut target, nilai apa pun",
                    "  input[type=\"text\"]    atributnya bernilai persis 'text'",
                    "  a[href^=\"https\"]      nilainya diawali 'https'",
                    "  a[href$=\".pdf\"]       nilainya diakhiri '.pdf'",
                    "  a[href*=\"contoh\"]     nilainya mengandung 'contoh'",
                ]
            },
            {
                "body": [
                    "Class atau id?",
                    "",
                    "  class boleh dipakai berkali-kali dalam satu halaman.",
                    "  id hanya boleh muncul sekali per halaman.",
                    "",
                    "Satu elemen boleh punya beberapa class sekaligus, dipisah spasi:",
                    "  <div class=\"kartu besar aktif\">",
                    "Ketiganya berlaku bareng. Makanya class bisa disusun kayak kepingan",
                    "lego: .kartu ngurus bentuk dasar, .besar ngurus ukuran, .aktif ngurus",
                    "keadaan.",
                    "",
                    "Untuk menata tampilan, pakai class. Simpan id untuk keperluan lain,",
                    "yaitu tautan lompat (<a href=\"#bagian2\">) dan pegangan JavaScript.",
                    "Alasannya praktis, dan dijelaskan di bagian spesifisitas di bawah.",
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
                    "Cascade: aturan mana yang dipakai",
                    "",
                    "Aturan CSS datang dari banyak sumber sekaligus: gaya bawaan browser,",
                    "berkas gayamu, blok <style>, dan atribut inline. Sering juga beberapa",
                    "aturan ngatur properti yang sama di elemen yang sama. Cascade adalah",
                    "urutan pertanyaan yang dipakai browser untuk memilih pemenangnya:",
                    "",
                    "  1. Ada yang ditandai !important?      -> yang itu menang.",
                    "  2. Mana yang spesifisitasnya lebih tinggi?  -> yang itu menang.",
                    "  3. Kalau seri, mana yang ditulis belakangan? -> yang itu menang.",
                    "",
                    "Poin 3 sering nolong, tapi juga sering menjebak. Dua aturan yang",
                    "setara, yang dipakai adalah yang ditulis paling bawah. Jadi urutan baris di",
                    "berkas gaya ikut menentukan hasil, nggak cuma soal rapi.",
                    "",
                    "Spesifisitas artinya seberapa khusus sebuah pemilih. Dihitung sebagai",
                    "tiga angka (a, b, c):",
                    "  a = jumlah #id di dalam pemilih",
                    "  b = jumlah .class, [atribut], dan :pseudo-class",
                    "  c = jumlah nama elemen dan ::pseudo-element",
                    "",
                    "Cara membandingkannya dari kiri. Bandingkan a dulu. Kalau seri, baru",
                    "b. Kalau masih seri, baru c.",
                    "",
                    "  p                    (0,0,1)",
                    "  .kartu               (0,1,0)",
                    "  .kartu p             (0,1,1)",
                    "  .kartu .isi p span   (0,2,2)",
                    "  #menu                (1,0,0)",
                    "  style=\"...\"          inline, di atas semua pemilih",
                    "",
                    "Jadi (0,1,0) mengalahkan (0,0,11). Satu class menang atas sebelas",
                    "nama elemen. Angkanya nggak dijumlahkan jadi satu, tapi dibandingkan",
                    "bertingkat. Ini yang bikin orang bingung, \"pemilihku udah panjang",
                    "banget, kok masih kalah?\"",
                ]
            },
            {
                "body": [
                    "Kenapa id sebaiknya nggak dipakai untuk menata tampilan",
                    "",
                    "Pemilih #menu itu terlalu kuat. Hari ini terasa praktis. Bulan depan",
                    "kamu pengin satu menu tampil beda, lalu nulis .menu-gelap, dan ternyata",
                    "nggak ngaruh apa-apa. Untuk mengalahkannya, kamu terpaksa nulis",
                    "#menu.menu-gelap. Sejak itu seluruh berkas ikut naik ke tingkat id.",
                    "Beberapa bulan kemudian, satu-satunya cara menimpa apa pun tinggal",
                    "!important.",
                    "",
                    "Jadi mulai dari spesifisitas serendah mungkin. Makin rendah pemilihmu",
                    "sekarang, makin gampang nanti ditimpa kalau perlu.",
                    "",
                    "!important mematikan seluruh perhitungan di atas:",
                    "  color: red !important;",
                    "",
                    "Deklarasi itu menang atas apa pun. Masalahnya, satu-satunya cara",
                    "melawan !important adalah !important lain yang lebih spesifik. Sesudah",
                    "itu kamu nggak punya cara lain lagi untuk menimpa. Pakai !important",
                    "cuma untuk menimpa CSS pihak lain yang nggak bisa kamu ubah.",
                    "",
                    "Kalau sebuah aturan nggak ngaruh, hampir selalu penyebabnya satu dari",
                    "empat ini:",
                    "  1. Pemilihnya nggak cocok dengan elemen mana pun (salah nama class,",
                    "     atau lupa titik di depannya).",
                    "  2. Ada aturan lain yang lebih spesifik.",
                    "  3. Ada aturan setara yang ditulis belakangan.",
                    "  4. Nama properti atau nilainya salah ketik, dan CSS membuangnya",
                    "     tanpa bilang apa-apa.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Di toko online, tombol \"Beli\", tautan menu, dan harga coret ditata",
                    "lewat class yang dipakai berulang di ratusan produk. Orang yang",
                    "merawat berkas gayanya lebih sering berurusan dengan cascade daripada",
                    "menulis aturan baru: aturannya udah ditulis tapi nggak kelihatan",
                    "berlaku, jadi harus dicari aturan mana yang mengalahkannya.",
                    "",
                    "Kasus kecil: menu warung kopi online ditulis <nav id=\"menu\"> berisi",
                    "lima tautan, dan berkas gayanya punya #menu a { color: #333; }. Kamu",
                    "menambah class promo di tautan \"Diskon Senin\" lalu menulis",
                    ".promo { color: crimson; }. Tautannya tetap abu-abu.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pahami sasarannya: <a class=\"promo\"> di dalam #menu, yang harus",
                    "     jadi merah.",
                    "  2. Hitung spesifisitas dua aturan yang berebut. #menu a bernilai",
                    "     (1,0,1), .promo bernilai (0,1,0). Angka pertama dibandingkan",
                    "     dulu, dan id unggul di situ. Memindah baris ke bawah nggak",
                    "     menolong.",
                    "  3. Turunkan aturan lamanya ke tingkat class. Ganti id=\"menu\" jadi",
                    "     class=\"menu\" di HTML, lalu tulis:",
                    "      .menu a      { color: #333; }     /* (0,1,1) */",
                    "      .menu .promo { color: crimson; }  /* (0,2,0) */",
                    "  4. Periksa kasus pinggir: jangan tergoda menulis !important. Kalau",
                    "     besok satu tautan promo harus abu-abu lagi, satu-satunya cara",
                    "     melawannya adalah !important lain.",
                ]
            },
        ],
    },
    {
        "title": "3. Membaca Halaman dengan DevTools Browser",
        "sections": [
            {
                "body": [
                    "Sampai sini caramu kerja selalu sama: tulis CSS, muat ulang halaman,",
                    "lalu nebak kenapa hasilnya begitu. Di materi 2 kamu udah belajar",
                    "aturan mana yang dipakai browser. Sekarang kamu bisa melihat",
                    "jawabannya langsung, nggak perlu ngitung di kepala.",
                    "",
                    "Tiap browser punya alat bawaan namanya DevTools, singkatan dari",
                    "developer tools (alat pengembang). Udah terpasang, gratis, dan nggak",
                    "perlu diunduh. Di DevTools, browser nunjukin apa yang dia pikirkan:",
                    "elemen apa aja yang ada, aturan mana yang kena, aturan mana yang",
                    "dipakai, dan berapa ukuran tiap kotak. Angkanya angka asli, bukan",
                    "kira-kira.",
                    "",
                    "Alat ini penting gara-gara sifat CSS yang kamu kenal dari materi 1:",
                    "CSS nggak pernah ngasih pesan error. DevTools jadi pengganti pesan",
                    "error yang nggak pernah kamu dapat itu.",
                    "",
                    "Cara membukanya, pilih salah satu, hasilnya sama:",
                    "  - Klik kanan tepat di atas bagian yang bermasalah, lalu pilih",
                    "    Inspect atau Periksa elemen. Cara ini yang paling sering dipakai,",
                    "    karena elemen yang kamu klik langsung ikut terpilih.",
                    "  - Tekan F12.",
                    "  - Tekan Ctrl+Shift+I (Windows/Linux) atau Cmd+Option+I (Mac).",
                    "",
                    "Panelnya banyak, tapi untuk CSS cuma tiga yang dipakai tiap hari:",
                    "",
                    "  Elements   pohon HTML halaman. Klik satu baris = pilih satu elemen.",
                    "  Styles     semua aturan CSS yang kena elemen terpilih itu.",
                    "  Computed   nilai AKHIR tiap properti sesudah semuanya dihitung.",
                    "",
                    "Styles dan Computed selalu ngomongin elemen yang lagi terpilih di",
                    "Elements. Kalau elemen yang kamu pilih salah, jawaban yang kamu baca",
                    "juga jawaban untuk pertanyaan lain. Ini penyebab paling sering orang",
                    "ngira DevTools-nya yang keliru.",
                    "",
                    "Cara memastikan elemen yang terpilih memang yang kamu maksud:",
                    "  - Baris yang terpilih disorot di pohon, dan elemennya ikut disorot",
                    "    di halaman. Geser kursor menyusuri pohon, dan elemennya menyala",
                    "    satu per satu. Ini cara paling cepat menjawab \"div yang mana sih",
                    "    ini?\"",
                    "  - Di bawah pohon ada deretan seperti ini:",
                    "      html > body > div.panel > button.tombol.bahaya",
                    "    Itu jalur lengkap elemen terpilih, dari akar sampai ke elemen itu",
                    "    sendiri, lengkap dengan class-nya. Kalau ujungnya tertulis",
                    "    div.panel padahal kamu merasa lagi meriksa tombolnya, berarti",
                    "    kamu salah pilih. Klik satu tingkat lebih dalam.",
                    "  - Ctrl+F di dalam panel Elements mencari teks, tag, atau pemilih.",
                    "    Ketik .bahaya di situ, dan pohonnya lompat ke elemen pertama yang",
                    "    cocok.",
                    "",
                    "Satu hal lagi yang perlu jelas dari awal: yang kamu lihat di Elements",
                    "itu bukan isi berkas .html-mu. Itu pohon hasil bacaan browser, yang",
                    "udah termasuk tag yang dia tambal sendiri dan perubahan dari",
                    "JavaScript. Untuk melihat berkas aslinya apa adanya, pakai Ctrl+U",
                    "(View Source). Beda antara keduanya sering jadi petunjuk pertama",
                    "waktu ada yang aneh.",
                ],
            },
            {
                "heading": "Dua berkas untuk dibedah sendiri",
                "body": [
                    "Simpan kedua berkas di bawah ini dalam satu folder yang sama, lalu",
                    "buka index.html di browser. Halamannya sengaja dibikin aneh: ada dua",
                    "tombol dengan class yang persis sama, tapi yang satu hijau dan yang",
                    "satu merah. Semua langkah di bawah pakai halaman ini.",
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
                    "Panel Styles: melihat cascade bekerja",
                    "",
                    "Klik kanan tombol yang hijau, lalu pilih Inspect. Panel Styles",
                    "menampilkan semua aturan yang kena tombol itu, kira-kira begini:",
                    "",
                    "  element.style { }                              <- kosong",
                    "  .panel .tombol { background: #2f7d32; }        gaya.css:27",
                    "  .bahaya        { background: #b3261e; }        gaya.css:21",
                    "  .tombol        { background: #1a4fa0;          gaya.css:9",
                    "                   color: #ffffff; ... }",
                    "",
                    "Ada lima hal yang bisa kamu baca dari layar itu:",
                    "",
                    "  1. Baca dari atas. Urutan di panel ini beda dengan urutan di",
                    "     berkasmu. DevTools udah mengurutkannya pakai cascade: aturan",
                    "     yang dipakai di atas, yang kalah di bawah. Jadi pertanyaan",
                    "     \"aturan mana yang dipakai?\" udah dijawab sebelum kamu sempat",
                    "     ngitung apa pun.",
                    "  2. Yang dicoret artinya kalah. background di .bahaya dan di",
                    "     .tombol tampil tercoret, karena .panel .tombol lebih kuat.",
                    "     Perhatikan, yang dicoret cuma barisnya, nggak seluruh aturannya.",
                    "     color, padding, dan border-radius di .tombol tetap tegak dan",
                    "     tetap berlaku. Satu aturan bisa kalah di satu properti dan tetap",
                    "     dipakai di properti lain. Ini pelajaran spesifisitas di materi",
                    "     2, sekarang kelihatan pakai mata.",
                    "  3. Sekarang klik kanan tombol yang merah, lalu bandingkan. Aturan",
                    "     .panel .tombol hilang dari daftar. Pemilihnya memang nggak",
                    "     cocok, karena tombol itu nggak ada di dalam .panel. Yang dipakai",
                    "     adalah .bahaya. Spesifisitasnya seri dengan .tombol, dan kalau",
                    "     seri, yang ditulis belakangan yang dipakai. Kalau sebuah aturan",
                    "     nggak muncul di daftar sama sekali, kamu dapat jawaban yang",
                    "     paling berguna: pemilihmu nggak kena. Jadi berhenti",
                    "     mengutak-atik isi bloknya, dan perbaiki pemilihnya.",
                    "  4. Di kanan tiap aturan ada nama berkas dan nomor barisnya",
                    "     (gaya.css:27). Klik, dan DevTools lompat ke baris itu. Di",
                    "     proyek yang punya lima berkas gaya, ini yang menjawab \"aturan",
                    "     ini ditulis di berkas yang mana, sih?\"",
                    "  5. Geser kursor ke sebuah deklarasi, dan muncul kotak centang di",
                    "     kirinya. Hilangkan centangnya, dan deklarasi itu mati sementara.",
                    "     Halamannya langsung berubah. Ini cara paling cepat untuk",
                    "     membuktikan sesuatu: matikan deklarasi satu per satu sampai",
                    "     masalahnya hilang. Baris terakhir yang kamu matikan itulah",
                    "     penyebabnya.",
                    "",
                    "Coretan punya dua arti, dan keduanya beda:",
                    "  - Tercoret polos                      -> kalah cascade.",
                    "  - Tercoret + segitiga kuning peringatan -> browser nggak ngerti",
                    "    baris itu. Nama propertinya salah ketik, atau nilainya nggak sah",
                    "    untuk properti itu.",
                    "",
                    "Segitiga kuning itu satu-satunya hal di CSS yang mirip pesan error,",
                    "dan dia cuma muncul di sini. Di halaman nggak ada apa-apa. Coba",
                    "sendiri: ubah background jadi bacground di gaya.css, lalu muat",
                    "ulang. Halamannya nggak berubah apa-apa, tapi panel Styles langsung",
                    "nunjuk baris yang salah.",
                    "",
                    "Blok element.style di paling atas berisi atribut style=\"...\" milik",
                    "elemen itu. Kalau kamu nggak pakai atribut style, bloknya kosong.",
                    "Ngetik di blok itu sama aja dengan nulis atribut style= di elemen",
                    "tadi. Jadi apa pun yang kamu taruh di situ mengalahkan semua pemilih",
                    "(materi 2). Berguna untuk nyoba cepat, tapi cara ini jangan ditiru",
                    "di berkas .css-mu.",
                    "",
                    "Kalau kamu gulir jauh ke bawah, ada bagian Inherited from body dan",
                    "seterusnya. Isinya properti yang nggak ditulis untuk elemen ini,",
                    "tapi diwariskan dari induknya (dibahas di materi Teks dan Font).",
                    "Kalau warna teks atau font berubah padahal nggak ada aturan yang",
                    "kelihatan, penyebabnya hampir selalu ketemu di bagian itu.",
                ],
            },
            {
                "body": [
                    "Panel Computed: hasil akhirnya",
                    "",
                    "Styles nunjukin aturan-aturan yang saling berebut. Computed nunjukin",
                    "hasilnya: daftar semua properti elemen terpilih, masing-masing cuma",
                    "satu nilai. Nilai itu yang dipakai browser untuk menggambar, sesudah",
                    "cascade, pewarisan, dan nilai bawaan dihitung.",
                    "",
                    "Ada dua alasan panel ini layak dibuka tiap hari:",
                    "",
                    "  - Di atasnya ada kotak Filter. Ketik background, dan dari ratusan",
                    "    baris tinggal properti itu yang tersisa.",
                    "  - Buka segitiga kecil di kiri sebuah properti. DevTools",
                    "    menampilkan nilai itu datang dari aturan mana, lengkap dengan",
                    "    tautan ke barisnya. Itu jawaban langsung untuk pertanyaan \"jadi",
                    "    warnanya diambil dari mana?\"",
                    "",
                    "Nilai di Computed udah dihitung, jadi bentuknya sering beda dari",
                    "yang kamu ketik. 1em muncul sebagai 16px, red jadi rgb(255, 0, 0),",
                    "dan lebar 50% jadi angka piksel. Itu bukan kesalahan. Itu angka yang",
                    "dipakai untuk menggambar. Panel ini juga cara paling gampang",
                    "menjawab \"2rem itu berapa piksel di sini?\"",
                    "",
                    "Diagram box model: kotakku sebesar apa?",
                    "",
                    "Di paling atas panel Computed ada gambar kotak berlapis. Bentuknya",
                    "sama dengan diagram di materi Box Model, tapi isinya angka asli dari",
                    "elemen yang lagi terpilih:",
                    "",
                    "  jingga   margin     paling luar",
                    "  kuning   border     kuning kecokelatan",
                    "  hijau    padding",
                    "  biru     content    tertulis sebagai lebar x tinggi",
                    "",
                    "Untuk tombol di contoh tadi, kamu bakal lihat margin 8 di keempat",
                    "sisi, border 2, padding 12 di atas dan bawah, serta padding 20 di",
                    "kiri dan kanan. Angka nol ditampilkan sebagai tanda hubung (-),",
                    "bukan angka 0.",
                    "",
                    "Geser kursor ke salah satu lapis, dan lapis itu menyala di halaman",
                    "dengan warna yang sama. Begitu kamu lihat sendiri, urusan \"margin di",
                    "luar, padding di dalam\" jadi gampang diingat. Kamu nggak lagi",
                    "menghafal gambar di buku, tapi nunjuk kotaknya sendiri.",
                    "",
                    "Di sini juga kelihatan kenapa lebar kotak sering lebih besar dari",
                    "yang kamu tulis, tanpa perlu ngitung 2 + 20 + 200 + 20 + 2 di",
                    "kepala. Misalnya kamu nulis width: 200px. Lapis content tetap",
                    "tertulis 200, tapi kotaknya jelas makan tempat lebih lebar di",
                    "halaman. Nah, itu alasan box-sizing: border-box dibuat.",
                ],
            },
            {
                "body": [
                    "Memaksa keadaan: tombol :hov dan .cls",
                    "",
                    ":hover susah ditata dengan tenang. Begitu kursor pindah ke panel",
                    "DevTools untuk membaca aturannya, hover-nya lepas dan tampilannya",
                    "balik seperti semula.",
                    "",
                    "Di sudut kanan atas panel Styles ada tombol :hov. Klik, dan muncul",
                    "daftar centang, di antaranya :hover, :active, :focus, :focus-within,",
                    "dan :focus-visible. Centang :hover, dan elemen terpilih dipaksa",
                    "tetap dalam keadaan hover sampai kamu mematikannya lagi. Kursormu",
                    "bebas ke mana aja. Elemen yang lagi dipaksa dikasih titik kecil di",
                    "pohon Elements, supaya kamu ingat untuk mematikannya.",
                    "",
                    "Coba di tombol hijau. Centang :hover, dan .tombol:hover naik ke atas,",
                    "sementara background di .panel .tombol ikut tercoret. Keduanya punya",
                    "spesifisitas (0,2,0), jadi yang ditulis belakangan yang dipakai. Ini",
                    "bukti bahwa pseudo-class ikut dihitung di spesifisitas (materi 2,",
                    "dan materi Pseudo-class dan Pseudo-element).",
                    "",
                    "Di sebelahnya ada tombol .cls. Isinya kotak untuk menambah class ke",
                    "elemen terpilih, plus daftar centang class yang udah nempel di",
                    "elemen itu. Hilangkan centang bahaya di tombol merah, dan tombolnya",
                    "langsung balik biru. Berkas HTML-nya nggak kamu sentuh sama sekali.",
                    "Ini cara paling cepat menjawab \"aturan ini kena atau nggak kalau",
                    "class-nya dipasang?\"",
                    "",
                    "Menyunting langsung, dan kenapa semuanya hilang",
                    "",
                    "Hampir semua yang tampil di panel Styles bisa diklik lalu diketik",
                    "ulang:",
                    "  - Klik nilainya, ketik yang baru, lalu tekan Enter. Tab",
                    "    memindahkanmu ke deklarasi berikutnya.",
                    "  - Klik nama propertinya untuk menggantinya. Klik pemilihnya untuk",
                    "    mengubah pemilihnya.",
                    "  - Tanda + di sudut panel bikin aturan baru dari nol.",
                    "  - Taruh kursor di sebuah angka, lalu tekan panah atas atau bawah.",
                    "    Angkanya naik atau turun satu. Shift+panah lompat sepuluh,",
                    "    Alt+panah bergerak nol koma satu. Nyari padding yang pas dengan",
                    "    cara ini jauh lebih cepat daripada ketik, simpan, lalu muat ulang",
                    "    berkali-kali, karena halamannya berubah tepat saat angkanya",
                    "    berubah.",
                    "",
                    "Ingat: semua suntingan itu hilang begitu halaman dimuat ulang.",
                    "DevTools menyunting salinan di memori browser, bukan berkas .css di",
                    "komputermu. Nggak ada peringatan, nggak ada tawaran untuk menyimpan,",
                    "dan Ctrl+Z juga nggak bisa mengembalikannya.",
                    "",
                    "Banyak orang udah ngabisin setengah jam nyetel tampilan di DevTools,",
                    "lalu nekan F5 karena kebiasaan, dan semuanya hilang. Jadi biasakan",
                    "satu hal: begitu sebuah nilai terasa pas, langsung salin ke berkas",
                    ".css-mu. DevTools untuk nyoba, berkas .css untuk menyimpan.",
                    "",
                    "Kebalikannya juga bisa menjebak. Kamu udah menyimpan berkasnya, lalu",
                    "muat ulang, tapi halamannya tetap pakai gaya yang lama. Itu karena",
                    "browser nampilin salinan yang dia simpan sendiri (cache, lihat",
                    "materi 1). Muat ulang paksa pakai Ctrl+Shift+R sebelum nyalahin",
                    "CSS-mu.",
                    "",
                    "DevTools dan tombol Jalankan di aplikasi ini",
                    "",
                    "Dua alat ini menjawab dua pertanyaan yang beda, dan kamu butuh",
                    "dua-duanya:",
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
                    "Daftar periksa \"kalau aturan nggak bekerja\" di materi Variabel CSS",
                    "dan Cara Menata Berkas Gaya tetap berlaku semuanya. Bedanya, sesudah",
                    "materi ini kamu nggak perlu lagi nebak sebagian besar langkahnya.",
                    "Kamu bisa melihatnya langsung.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Front-end developer membuka DevTools sebelum membuka berkas .css.",
                    "Laporan seperti \"tombol Daftar di halaman pendaftaran kok abu-abu\"",
                    "dijawab dengan klik kanan, Inspect, lalu membaca panel Styles. Dari",
                    "situ kelihatan aturan mana yang dipakai, dari berkas mana, dan di",
                    "baris berapa.",
                    "",
                    "Kasus kecil: tombol \"Kirim\" di formulir absensi online tampil biru.",
                    "Kamu yakin udah menulis .tombol-kirim { background: #2f7d32; } di",
                    "gaya.css, jadi harusnya hijau.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Klik kanan tombolnya, pilih Inspect, lalu baca jalur di bawah",
                    "     pohon Elements. Ujungnya harus button.tombol-kirim. Kalau cuma",
                    "     button.tombol, class-nya belum terpasang di HTML.",
                    "  2. Cari aturan .tombol-kirim di panel Styles. Kalau nggak ada sama",
                    "     sekali, pemilihnya nggak kena. Cek nama class-nya, dan cek apakah",
                    "     berkasnya tersambung.",
                    "  3. Kalau aturannya ada dan baris background dicoret polos, aturan",
                    "     itu kalah cascade. Pemenangnya ada di atasnya. Klik nama berkas",
                    "     dan nomor baris di kanannya untuk lompat ke sumbernya.",
                    "  4. Kalau barisnya dicoret dengan segitiga kuning, nilainya salah",
                    "     ketik. Betulkan di Styles dulu, lihat hasilnya, lalu salin ke",
                    "     gaya.css dan muat ulang paksa dengan Ctrl+Shift+R.",
                    "",
                    "Ingat: suntingan di DevTools hilang begitu halaman dimuat ulang.",
                    "Nilai yang udah pas harus kamu salin sendiri ke berkasnya.",
                ]
            },
        ],
    },
    {
        "title": "4. Warna dan Satuan",
        "sections": [
            {
                "body": [
                    "Ada empat cara nulis warna. Semuanya sah, jadi pilih yang paling",
                    "cocok buat keperluanmu.",
                    "",
                    "  color: red;                  nama warna (ada 148 nama baku)",
                    "  color: #cc0000;              hex: #RRGGBB, tiap pasang 00-ff",
                    "  color: #c00;                 hex singkat, sama dengan #cc0000",
                    "  color: rgb(204 0 0);         merah, hijau, biru: 0-255",
                    "  color: rgb(204 0 0 / 50%);   dengan tingkat tembus pandang",
                    "  color: hsl(0 100% 40%);      hue, saturation, lightness",
                    "",
                    "Hex itu bilangan basis 16, isinya 0-9 lalu a-f. #ff0000 artinya merah",
                    "penuh, hijau nol, biru nol. #000000 itu hitam, #ffffff itu putih.",
                    "Bentuk singkat #c00 artinya tiap huruf ditulis dua kali, jadi",
                    "#cc0000.",
                    "",
                    "hsl() paling gampang dipikirkan sama manusia:",
                    "  hue        0-360 derajat roda warna (0 merah, 120 hijau, 240 biru)",
                    "  saturation 0% abu-abu, 100% pekat",
                    "  lightness  0% hitam, 50% warna murni, 100% putih",
                    "",
                    "Mau bikin versi yang lebih terang dari satu warna? Cukup ubah angka",
                    "ketiganya:",
                    "  hsl(210 90% 45%)  ->  hsl(210 90% 65%)",
                    "Kalau pakai hex, kamu harus ngitung ulang tiga pasang angka, dan",
                    "warnanya sering meleset.",
                    "",
                    "Di kode orang lain, kamu bakal lebih sering ketemu bentuk berkoma",
                    "seperti ini:",
                    "",
                    "  color: rgb(204, 0, 0);            sama persis dengan rgb(204 0 0)",
                    "  color: rgba(0, 0, 0, 0.5);        hitam, setengah tembus pandang",
                    "  color: hsl(0, 100%, 40%);         sama persis dengan hsl(0 100% 40%)",
                    "  color: hsla(0, 100%, 40%, 0.5);   dengan tembus pandang",
                    "",
                    "Huruf a di rgba dan hsla artinya alpha, yaitu tingkat kepekatan.",
                    "Nilainya ditulis dari 0 sampai 1. 0 artinya tembus pandang penuh, 1",
                    "artinya pekat penuh. Jadi rgba(0, 0, 0, 0.5) itu hitam setengah",
                    "pekat.",
                    "",
                    "Bentuk tanpa koma di daftar pertama lebih baru dan lebih enak",
                    "ditulis. Tapi bentuk berkoma yang paling banyak dipakai di kode",
                    "nyata, jadi berkas gaya orang lain hampir pasti pakai itu. Hasil",
                    "keduanya sama persis. Kenali dua-duanya, lalu tulis yang mana aja",
                    "yang kamu suka.",
                    "",
                    "Alpha dan opacity itu beda. Alpha bikin satu warna itu aja yang",
                    "tembus pandang. Opacity bikin elemennya tembus pandang beserta",
                    "semua isinya, sampai teks di atasnya juga.",
                    "",
                    "Ada dua nilai khusus yang sering berguna:",
                    "  transparent    tembus pandang sepenuhnya",
                    "  currentColor   nilai color elemen itu sendiri",
                    "     border: 1px solid currentColor;  -> garis ikut warna teks",
                ]
            },
            {
                "body": [
                    "Satuan ukuran",
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
                    "  fr   satu bagian sisa ruang (khusus grid, materi 14)",
                    "",
                    "Jebakan: em itu menumpuk. Misalnya .luar { font-size: 1.5em }, lalu",
                    "di dalamnya ada .dalam { font-size: 1.5em }. Hasilnya 1,5 x 1,5 =",
                    "2,25 kali ukuran asal. Kalau tiga tingkat bersarang, jadi 3,4 kali.",
                    "Nggak ada yang minta begitu, dan penyebabnya susah dicari karena",
                    "tiap aturan kalau dilihat sendiri kelihatan wajar.",
                    "",
                    "rem nggak menumpuk, karena selalu diukur ke <html>. Jadi untuk",
                    "ukuran huruf, pakai rem. Simpan em untuk jarak yang memang harus",
                    "ikut ukuran huruf elemennya sendiri. Contohnya padding tombol,",
                    "supaya tombol yang besar otomatis dapat padding yang lebih lega.",
                    "",
                    "line-height sebaiknya ditulis tanpa satuan:",
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
                    "Baris pertama contoh ini pakai :root. Itu pemilih biasa, sama seperti",
                    "yang kamu pelajari di materi 2. :root artinya elemen <html>, dan dia",
                    "selalu cocok dengan tepat satu elemen, yaitu elemen paling luar. Apa",
                    "pun yang kamu taruh di situ berlaku untuk seluruh halaman. Kegunaan",
                    "utamanya dibahas lengkap di materi Variabel CSS dan Cara Menata",
                    "Berkas Gaya.",
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
                    "Soal kontras, penting kalau kamu membaca berjam-jam",
                    "",
                    "Teks abu-abu muda di atas putih kelihatan elegan di gambar promosi,",
                    "tapi bikin mata capek kalau dibaca lama. Ukurannya disebut rasio",
                    "kontras. Untuk teks isi, batas yang dianggap aman adalah 4,5:1.",
                    "",
                    "  #999999 di atas putih  -> sekitar 2,8:1. Di bawah batas.",
                    "  #767676 di atas putih  -> tepat di sekitar 4,5:1.",
                    "  #595959 di atas putih  -> sekitar 7:1. Nyaman.",
                    "",
                    "Untuk bacaan panjang, hitam pekat di atas putih pekat juga kurang",
                    "enak. Bedanya terlalu tajam, jadi hurufnya kayak bergetar. Pasangan",
                    "yang enak biasanya latar yang agak hangat (#fdfdfb) dengan teks",
                    "abu-abu yang gelap banget (#23252b), daripada #ffffff dengan",
                    "#000000.",
                    "",
                    "Tema gelap juga sama, cuma kebalikannya. Teks putih pekat di atas",
                    "hitam pekat bikin silau, jadi turunkan keduanya sedikit.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aplikasi bank dan dompet digital memakai satu warna merek di banyak",
                    "tempat: tombol utama, latar notifikasi yang lebih muda, dan garis",
                    "tepi. Warna-warna turunan itu enak ditulis dalam hsl, dan tiap",
                    "pasangan teks dan latar dicek dulu rasio kontrasnya sebelum dipakai.",
                    "",
                    "Kasus kecil: warna merek toko roti online adalah hsl(25 80% 40%),",
                    "cokelat kejinggaan. Desainer minta tiga hal: tombol berwarna itu",
                    "dengan teks putih, kotak promo dengan versi yang jauh lebih muda, dan",
                    "teks catatan kecil di atas latar putih yang tetap enak dibaca.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pahami keluarannya: tiga warna yang kelihatan satu keluarga.",
                    "     Dengan hsl, cukup angka ketiganya (lightness) yang diubah:",
                    "      .tombol { background: hsl(25 80% 40%); color: #ffffff; }",
                    "      .promo  { background: hsl(25 80% 92%); }",
                    "  2. Teks catatan jangan #999999, yang cuma sekitar 2,8:1 di atas",
                    "     putih. Pakai #595959, sekitar 7:1.",
                    "  3. Ukuran catatan ditulis 0.875rem, jangan 0.875em. Kalau catatan",
                    "     itu suatu hari ditaruh di dalam kotak berhuruf 1.25em, em ikut",
                    "     menumpuk. rem selalu diukur ke <html>, jadi nggak menumpuk.",
                    "  4. Periksa kasus pinggir: teks putih di atas tombol tadi sekitar",
                    "     4,7:1, tipis di atas batas 4,5:1. Kalau tombolnya diminta lebih",
                    "     terang, misalnya lightness 45%, rasionya turun ke sekitar 3,9:1.",
                    "     Pertahankan 40% atau pakai yang lebih gelap.",
                ]
            },
        ],
    },
    {
        "title": "5. Satuan Lanjut dan Menghitung di Dalam CSS",
        "sections": [
            {
                "body": [
                    "Coba tulis ukuran ini pakai satuan yang udah kamu pelajari: \"selebar",
                    "penuh, dikurangi panel selebar 240px\". Ternyata nggak bisa.",
                    "",
                    "Persentase selalu diukur ke satu hal aja, yaitu ukuran induknya. Dia",
                    "nggak tahu apa-apa soal panel 240px di sebelahnya. px sebaliknya,",
                    "nggak tahu berapa lebar layar orang. Masing-masing benar, tapi nggak",
                    "ada satu nilai pun yang bisa menyatakan hubungan keduanya.",
                    "",
                    "Untuk itulah ada calc(). Dengan calc(), kamu bisa nulis hitungan",
                    "sebagai nilai:",
                    "",
                    "  .isi { width: calc(100% - 240px); }",
                    "",
                    "Browser yang ngerjain hitungannya. Dia ngitung ulang tiap kali",
                    "ukuran jendelanya berubah.",
                    "",
                    "Kelebihan calc(): kamu boleh mencampur satuan di dalamnya.",
                    "",
                    "  calc(100vh - 64px)      tinggi jendela dikurangi bilah atas",
                    "  calc(50% + 1rem)        setengah induk, lebih satu baris huruf",
                    "  calc(100% / 3 - 20px)   sepertiga, jaraknya sudah dipotong",
                    "  calc(2rem + 5vw)        ikut lebar layar, tapi punya dasar tetap",
                    "",
                    "%, px, rem, dan vh diukur terhadap hal yang beda-beda. calc() adalah",
                    "satu-satunya tempat mereka bisa digabung dalam satu nilai.",
                    "",
                    "Yang paling sering bikin salah waktu nulis calc(): spasi.",
                    "",
                    "  calc(100% - 20px)   BENAR",
                    "  calc(100%-20px)     DIBUANG. Tanpa pesan, tanpa tanda apa pun.",
                    "  calc(100% -20px)    dibuang juga - spasinya harus di KEDUA sisi.",
                    "",
                    "Spasi di kiri dan kanan tanda + dan - itu wajib. Alasannya, di CSS",
                    "tanda minus boleh jadi bagian dari sebuah nilai. -20px itu satu angka",
                    "negatif yang utuh, dan --lebar itu nama variabel. Kalau ditulis",
                    "rapat, browser nggak bisa membedakan \"kurangi dua puluh piksel\"",
                    "dengan \"satu nilai aneh bernama 100%-20px\". Spasi itu yang ngasih",
                    "tahu maksudmu.",
                    "",
                    "Kalau salah, akibatnya khas CSS. Seluruh deklarasinya dibuang tanpa",
                    "pesan, dan lebarnya balik ke bawaan. Yang kamu lihat cuma \"calc-nya",
                    "nggak jalan\". Jadi kalau sebuah calc nggak ngaruh, cek spasinya",
                    "dulu sebelum curiga ke hal lain.",
                    "",
                    "Tanda * dan / nggak wajib pakai spasi, tapi tulis aja supaya",
                    "seragam. Angka pengali dan pembaginya harus angka polos tanpa",
                    "satuan. calc(100% / 3) sah, sedangkan calc(100% / 3px) nggak ada",
                    "artinya dan ikut dibuang.",
                    "",
                    "Bentuk yang paling sering kamu temui di kode orang:",
                    "",
                    "  padding: calc(var(--s4) * 2);",
                    "  width: calc(100% - var(--lebar-panel));",
                    "",
                    "Nama yang diawali dua tanda minus itu variabel CSS. Materinya",
                    "sendiri ada di \"Variabel CSS dan Cara Menata Berkas Gaya\". Untuk",
                    "sekarang cukup tahu satu hal: var() diganti dengan isinya lebih",
                    "dulu, baru hitungannya dikerjakan. Kalau --s4 bernilai 16px, baris",
                    "pertama di atas artinya calc(16px * 2).",
                    "",
                    "Di situ juga ada jebakannya. Kalau nama variabelnya salah ketik atau",
                    "belum pernah dibuat, yang masuk ke calc() adalah nilai kosong. Yang",
                    "gugur seluruh deklarasinya, nggak cuma bagian itu.",
                ],
            },
            {
                "body": [
                    "min(), max(), dan clamp() satu keluarga dengan calc(). Ketiganya",
                    "sama-sama ngitung, sama-sama boleh mencampur satuan, dan aturan",
                    "spasinya juga sama persis.",
                    "",
                    "min() dan max() awalnya kerasa kebalik. Lihat contoh ini:",
                    "",
                    "  width: min(100%, 720px);",
                    "",
                    "Bacanya: \"pakai yang lebih kecil saat itu\". Di layar lebar, 720px",
                    "lebih kecil, jadi itu yang dipakai. Di layar 400px, 100% yang lebih",
                    "kecil. Hasilnya lebar maksimum 720px yang ikut menyusut sendiri di",
                    "layar sempit.",
                    "",
                    "Jadi min() memasang batas atas, dan max() memasang batas bawah:",
                    "",
                    "  font-size: max(1rem, 2vw);   tidak pernah lebih kecil dari 1rem",
                    "",
                    "Kerasa kebalik karena nama fungsinya nyebut cara milihnya, nggak",
                    "nyebut akibatnya. Sesuatu yang selalu milih yang paling kecil nggak",
                    "akan pernah melewati batas atasnya.",
                    "",
                    "clamp() menggabung keduanya dalam satu tulisan:",
                    "",
                    "  font-size: clamp(1.5rem, 4vw, 2.5rem);",
                    "                   ^batas  ^nilai ^batas",
                    "                    bawah   ideal  atas",
                    "",
                    "Artinya sama persis dengan max(1.5rem, min(4vw, 2.5rem)), tapi jauh",
                    "lebih enak dibaca. Nilai tengahnya yang dipakai, selama nilainya",
                    "masih ada di antara dua batas itu.",
                    "",
                    "Ketiganya udah berupa hitungan. Jadi kamu boleh langsung nulis",
                    "hitungan di dalamnya tanpa nulis calc() lagi:",
                    "",
                    "  width: min(100% - 2rem, 60ch);",
                    "  font-size: clamp(1rem, 0.9rem + 0.6vw, 1.4rem);",
                    "",
                    "Ada dua jebakan di clamp():",
                    "",
                    "  1. Kalau batas bawahnya ternyata lebih besar dari batas atasnya,",
                    "     yang dipakai batas bawah. Nggak ada pesan error. Ukurannya cuma",
                    "     terkunci di satu angka dan nggak pernah berubah lagi.",
                    "  2. Nilai ideal yang cuma pakai vw, misalnya clamp(1rem, 4vw, 2rem),",
                    "     bikin ukuran huruf nggak ikut berubah waktu pembaca memakai",
                    "     setelan \"perbesar teks\" di browsernya. Buat orang yang memang",
                    "     butuh huruf besar, halamanmu jadi nggak bisa dibesarkan sama",
                    "     sekali. Campurkan rem supaya setelan itu tetap ngaruh:",
                    "       clamp(1rem, 0.9rem + 0.6vw, 1.4rem)",
                    "",
                    "Ketiganya bakal muncul lagi di materi media query. Di sana kegunaannya",
                    "kelihatan jelas: banyak hal yang dulu butuh @media sekarang beres",
                    "dengan satu baris min() atau clamp().",
                ],
            },
            {
                "body": [
                    "Dua keluarga satuan yang belum pernah dibahas",
                    "",
                    "Satuan waktu: s dan ms",
                    "",
                    "  s    detik            ms   milidetik, seperseribu detik",
                    "",
                    "1s = 1000ms, jadi 0.2s dan 200ms itu sama persis. Pilih satu cara",
                    "nulis, lalu pakai terus di seluruh berkas. Kalau dicampur, dua angka",
                    "yang nilainya mirip jadi kelihatan beda jauh.",
                    "",
                    "Cuma dua properti yang pakai satuan ini: transition dan animation,",
                    "beserta turunannya (transition-duration, transition-delay,",
                    "animation-duration). Keduanya punya materi sendiri nanti. Di sini",
                    "kita bahas satuannya aja.",
                    "",
                    "  .tombol { transition: background 0.2s; }",
                    "",
                    "Jebakan: angka tanpa satuan nggak sah untuk waktu.",
                    "",
                    "  transition: background 0.2;   dibuang. Tidak ada transisi apa pun.",
                    "  transition-duration: 0;       dibuang juga.",
                    "  transition-duration: 0s;      benar.",
                    "",
                    "Ini pengecualian yang gampang bikin salah. Untuk panjang, angka nol",
                    "boleh ditulis polos, jadi margin: 0 itu sah. Untuk waktu nggak",
                    "boleh. Nol pun harus pakai satuan.",
                    "",
                    "Satuan sudut: deg, turn, dan rad",
                    "",
                    "  deg    derajat. 360deg satu putaran penuh.",
                    "  turn   putaran. 1turn = 360deg; 0.5turn setengah putaran.",
                    "  rad    radian.  1turn = 6.2832rad, yaitu 2 x pi.",
                    "",
                    "Ketiganya boleh dipakai di tempat yang sama. deg paling umum. turn",
                    "paling enak dibaca kalau maksudmu memang \"setengah putaran\".",
                    "",
                    "Yang pakai satuan sudut:",
                    "",
                    "  transform: rotate(45deg);       memutar elemen",
                    "  transform: rotate(-90deg);      minus = berlawanan arah jarum jam",
                    "  linear-gradient(180deg, ...)    arah gradiennya",
                    "  hsl(220deg 60% 35%)             hue memang sebuah sudut, jadi 220",
                    "                                  dan 220deg sama saja artinya",
                    "",
                    "Sama seperti waktu, angka polos di sini dibuang. rotate(45) nggak",
                    "memutar apa pun. Karena satu nilai yang rusak menggugurkan seluruh",
                    "deklarasi, fungsi transform lain di baris yang sama ikut hilang.",
                ],
            },
            {
                "body": [
                    "Satuan viewport, lengkapnya",
                    "",
                    "Viewport adalah bidang tempat halaman digambar. Di ponsel, viewport",
                    "itu cuma bagian layar yang tersisa untuk halamanmu, nggak seluruh",
                    "layar.",
                    "",
                    "  vw     1% LEBAR viewport",
                    "  vh     1% TINGGI viewport",
                    "  vmin   1% dari sisi yang lebih PENDEK",
                    "  vmax   1% dari sisi yang lebih PANJANG",
                    "",
                    "vmin jarang diajarkan, padahal rapi banget untuk sesuatu yang harus",
                    "selalu kelihatan utuh. width: 80vmin; height: 80vmin; menghasilkan",
                    "bujur sangkar yang tetap muat di layar tegak maupun melintang, tanpa",
                    "satu media query pun.",
                    "",
                    "Jebakan: 100vw ikut menghitung bilah gulir.",
                    "",
                    "Di komputer, bilah gulir vertikal makan tempat sekitar 15px. 100vw",
                    "tetap artinya lebar penuh, termasuk bilah itu. Jadi elemen selebar",
                    "100vw di halaman yang bisa digulir jadi lebih lebar dari ruang yang",
                    "ada, dan seluruh halaman tiba-tiba bisa digeser ke samping. Kalau",
                    "maksudmu \"selebar induknya\", pakai width: 100%, jangan 100vw.",
                    "",
                    "Jebakan 100vh di ponsel adalah yang paling terkenal.",
                    "",
                    "min-height: 100vh kedengarannya \"setinggi layar\". Di komputer memang",
                    "begitu. Di ponsel nggak.",
                    "",
                    "Bilah alamat browser di ponsel mengecil waktu halaman digulir ke",
                    "bawah, lalu muncul lagi waktu digulir ke atas. Tingginya berubah-ubah,",
                    "jadi \"tinggi layar\" itu nggak cuma satu angka. Untuk vh, browser",
                    "milih tinggi waktu bilah alamat lagi sembunyi, yaitu tinggi yang",
                    "paling besar.",
                    "",
                    "Akibatnya, waktu halaman baru dibuka dan bilah alamat masih",
                    "kelihatan, kotak setinggi 100vh lebih tinggi dari ruang yang ada.",
                    "Bagian bawahnya ada di luar layar sampai orang menggulir, padahal",
                    "biasanya di situlah tombol utamanya. Di komputermu nggak ada",
                    "gejalanya sama sekali, makanya bug ini bisa bertahan berbulan-bulan.",
                    "",
                    "Ada tiga satuan baru untuk masalah itu:",
                    "",
                    "  svh   small    tinggi saat bilah browser TERLIHAT (paling kecil)",
                    "  lvh   large    tinggi saat bilah SEMBUNYI - inilah arti vh selama ini",
                    "  dvh   dynamic  mengikuti keadaan saat itu, berubah sambil digulir",
                    "",
                    "Makanya kode yang lebih baru pakai 100dvh untuk \"setinggi layar\".",
                    "Kalau tinggi yang berubah-ubah malah mengganggu, misalnya isinya",
                    "kelihatan lompat waktu digulir, pakai 100svh. svh selalu milih yang",
                    "paling kecil, jadi nggak bakal ada bagian yang ketutup.",
                    "",
                    "Semuanya punya keluarga lengkap: dvw, svw, lvw, dvmin, dan",
                    "seterusnya. Yang sering dipakai cuma dvh dan svh.",
                    "",
                    "Cara nulisnya supaya browser lama tetap kebagian:",
                    "",
                    "  min-height: 100vh;",
                    "  min-height: 100dvh;",
                    "",
                    "Dua baris berurutan, properti yang sama. Browser yang belum kenal",
                    "dvh membuang baris kedua tanpa bilang apa-apa, dan tetap pakai baris",
                    "pertama. Browser yang kenal dvh pakai baris terakhir, karena dari",
                    "dua aturan yang setara, yang ditulis belakangan yang dipakai. Kali",
                    "ini kebiasaan CSS membuang yang nggak dia mengerti malah nolong.",
                    "Hampir semua fitur baru CSS dipasang dengan aman pakai cara ini.",
                ],
            },
            {
                "heading": "Kerangka halaman yang memakai semuanya",
                "body": [
                    "Di berkas gaya berikut, semua yang tadi dibahas dipakai bareng. Coba",
                    "perhatikan:",
                    "",
                    "  - .badan pakai calc(100dvh - var(--tinggi-kepala)). Jadi sisanya",
                    "    pas mengisi layar di bawah bilah atas, nggak lebih dan nggak",
                    "    kurang, di ponsel maupun di komputer.",
                    "  - .isi pakai calc(100% - var(--lebar-panel)). Hal ini nggak bisa",
                    "    ditulis pakai satu persentase aja.",
                    "  - Judulnya pakai clamp, jadi ukuran hurufnya nggak butuh media",
                    "    query sama sekali.",
                    "  - Semua angka kerangkanya ada di :root. Mau ganti lebar panel?",
                    "    Cukup ubah di satu tempat, dan semua hitungan ikut menyesuaikan.",
                    "",
                    "display: flex, :hover, transition, dan rotate() punya materi",
                    "sendiri nanti. Di sini keempatnya cuma jadi tempat satuannya",
                    "dipakai.",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aplikasi kasir di tablet dan halaman login aplikasi absensi sering",
                    "dirancang setinggi layar: bilah atas setinggi tetap, lalu satu kotak",
                    "yang mengisi sisanya. Ukuran \"sisa layar\" itu campuran dua satuan,",
                    "jadi ditulis pakai calc(). Di ponsel, pilihan antara vh dan dvh",
                    "menentukan bagian bawah kotaknya kelihatan atau terpotong.",
                    "",
                    "Kasus kecil: halaman login absensi karyawan punya bilah atas 56px.",
                    "Di bawahnya, kotak biru berisi logo dan tombol \"Masuk\" harus mengisi",
                    "tepat sisa layar. Di laptop pas. Di ponsel, bagian bawah kotaknya",
                    "melewati layar sampai halamannya digulir.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pahami ukurannya: tinggi layar dikurangi 56px. Satuan layar dan",
                    "     px nggak bisa digabung dalam satu nilai tanpa calc().",
                    "  2. Gejala \"pas di laptop, kelewat di ponsel\" adalah jebakan 100vh.",
                    "     vh memakai tinggi layar saat bilah alamat sembunyi, sedangkan",
                    "     dvh mengikuti keadaan saat itu.",
                    "  3. Tulis dua baris berurutan, supaya browser yang belum kenal dvh",
                    "     tetap dapat baris pertama:",
                    "      .kotak-login {",
                    "        min-height: calc(100vh - 56px);",
                    "        min-height: calc(100dvh - 56px);",
                    "      }",
                    "  4. Periksa kasus pinggir: kalau baris kedua ditulis rapat,",
                    "     calc(100dvh-56px), baris itu dibuang tanpa pesan. Browser lalu",
                    "     memakai baris vh di atasnya, dan gejala di ponsel muncul lagi.",
                ]
            },
        ],
    },
    {
        "title": "6. Teks dan Font",
        "sections": [
            {
                "body": [
                    "font-family ditulis sebagai daftar cadangan, dipisah koma:",
                    "",
                    "  font-family: \"Segoe UI\", Roboto, Helvetica, Arial, sans-serif;",
                    "",
                    "Browser nyoba dari kiri. Font pertama yang ada di komputer pembaca,",
                    "itulah yang dipakai. Nama font yang ada spasinya dibungkus tanda",
                    "petik ganda.",
                    "",
                    "Nama terakhir wajib berupa keluarga umum, supaya selalu ada yang",
                    "cocok, seaneh apa pun komputernya:",
                    "  serif        berkait, seperti Times    (enak untuk teks panjang)",
                    "  sans-serif   tanpa kait, seperti Arial (paling umum untuk layar)",
                    "  monospace    tiap huruf selebar sama   (kode)",
                    "  system-ui    huruf bawaan sistem operasi pembacanya",
                    "",
                    "Kenapa daftar cadangan wajib? Font yang terpasang di komputermu",
                    "belum tentu ada di komputer orang lain. Kalau nggak ada cadangan,",
                    "browser milih sendiri, biasanya Times. Tata letak yang udah kamu",
                    "susun rapi bisa berantakan, karena lebar hurufnya beda.",
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
                    "Pewarisan (inheritance)",
                    "",
                    "Pewarisan bikin CSS bisa ditulis sedikit tapi efeknya luas. Sebagian",
                    "properti otomatis menurun ke semua keturunan sebuah elemen, sebagian",
                    "lagi nggak.",
                    "",
                    "  Menular (properti TEKS):",
                    "    color, font-family, font-size, font-weight, font-style,",
                    "    line-height, text-align, letter-spacing, list-style",
                    "",
                    "  Tidak menular (properti KOTAK):",
                    "    margin, padding, border, background, width, height, display",
                    "",
                    "Jadi font-family yang ditulis sekali di body udah mengubah seluruh",
                    "halaman. Sebaliknya, border di body nggak menurun ke satu anak pun.",
                    "Aturan ini masuk akal: huruf yang sama memang biasanya pengin",
                    "diturunkan, garis tepi yang sama nggak.",
                    "",
                    "Ada empat kata kunci yang bisa dipakai di properti apa pun:",
                    "  inherit   paksa ambil nilai induk (berguna untuk yang tidak",
                    "            menular secara bawaan)",
                    "  initial   kembalikan ke nilai bawaan CSS",
                    "  unset     gabungan keduanya: inherit kalau propertinya",
                    "            menular, initial kalau tidak",
                    "  revert    kembalikan ke gaya bawaan BROWSER, yaitu user agent",
                    "            stylesheet dari materi 1",
                    "",
                    "Beda initial dan revert itu tipis, tapi kerasa. initial balik ke",
                    "bawaan spesifikasi CSS, dan bawaan spesifikasi untuk display adalah",
                    "inline. Jadi div { display: initial } bikin div itu jadi inline tanpa",
                    "kamu sadari, padahal hampir pasti bukan itu maumu. revert balik ke",
                    "bawaan browser, dan untuk div bawaannya memang block. Kalau maksudmu",
                    "\"batalkan gayaku, balikin seperti semula\", yang kamu cari adalah",
                    "revert.",
                    "",
                    "Ada satu properti bernama all, artinya \"semua properti sekaligus\".",
                    "Nilainya cuma boleh kata kunci global seperti empat kata di atas, dan",
                    "dua yang sering dipakai:",
                    "",
                    "  .polos  { all: unset; }    telanjangi habis, lalu tata ulang",
                    "  .semula { all: revert; }   kembalikan ke rupa bawaan browser",
                    "",
                    "all: unset adalah cara yang biasa dipakai untuk mengosongkan gaya",
                    "<button> sebelum menatanya jadi sesuatu yang lain. Latar abu-abu,",
                    "garis tepi, dan padding bawaannya hilang sekaligus, tanpa perlu",
                    "disebut satu per satu. Yang tersisa cuma sifatnya: tombol itu tetap",
                    "bisa diklik dan tetap bisa dicapai pakai Tab.",
                    "",
                    "Perhatikan: penanda fokusnya ikut terhapus, jadi kamu wajib bikin",
                    "penggantinya sendiri. Caranya ada di materi Pseudo-class dan",
                    "Pseudo-element.",
                    "",
                    "Kasus yang paling sering: <button>, <input>, <select>, dan <textarea>",
                    "nggak mewarisi font dari body. Keempatnya pakai font bawaan sistem",
                    "operasi, jadi tombol dan kotak isian kelihatan asing di tengah",
                    "halaman yang hurufnya udah kamu atur rapi. Itu bukan salahmu, memang",
                    "begitu bawaannya. Perbaikannya cukup satu aturan:",
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
                    "Panjang baris",
                    "",
                    "Baris yang terlalu panjang bikin capek. Begitu mata sampai di ujung",
                    "kanan, dia harus nyari lagi awal baris berikutnya di kiri, dan makin",
                    "panjang barisnya, makin sering nyasar. Panjang yang nyaman sekitar",
                    "45-75 karakter. Batasi pakai satu baris:",
                    "",
                    "  .isi { max-width: 68ch; }",
                    "",
                    "Satuan ch cocok di sini karena dia ngikutin font-nya. Kalau hurufnya",
                    "diganti jadi lebih lebar, batasnya ikut menyesuaikan.",
                    "",
                    "Kamu juga bisa nulis font dalam satu properti ringkas (urutannya",
                    "nggak boleh diacak):",
                    "  font: italic 700 1rem/1.5 Georgia, serif;",
                    "        gaya  tebal ukuran/jarak-baris keluarga",
                    "",
                    "Jebakan: bentuk ringkas ini mengembalikan semua bagian yang nggak kamu",
                    "sebut ke nilai bawaannya, termasuk line-height. Makanya banyak orang",
                    "milih nulis propertinya satu per satu.",
                    "",
                    "Font dari berkas sendiri (@font-face) memang bisa dipakai, tapi",
                    "tunda dulu. Tiap font tambahan adalah berkas yang harus diunduh",
                    "sebelum teksnya bisa dibaca, dan ngurus itu ada masalahnya sendiri.",
                    "Untuk sekarang, daftar font sistem udah lebih dari cukup, dan",
                    "langsung muncul.",
                ]
            },
            {
                "body": [
                    "Font web: tiga bentuk yang pasti kamu lihat di berkas orang",
                    "",
                    "Untuk latihan, font sistem tetap udah cukup. Tapi bentuk-bentuk di",
                    "bawah ini perlu kamu kenali sekarang, karena biasanya ada di baris",
                    "pertama berkas gaya orang lain. Dari sini juga asal nama asing di",
                    "font-family: Inter, sans-serif.",
                    "",
                    "Bentuk pertama, @font-face, yaitu font dari berkas milikmu sendiri:",
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
                    "@font-face nggak menata apa pun. Dia cuma mendaftarkan sebuah nama",
                    "beserta berkasnya. Yang memakainya tetap font-family biasa di",
                    "bawahnya, lengkap dengan daftar cadangan seperti tadi.",
                    "",
                    "font-display: swap artinya \"tampilkan font cadangan dulu, lalu tukar",
                    "begitu berkasnya datang\". Tanpa baris itu, sebagian browser",
                    "menyembunyikan teksnya sampai berkas font-nya selesai diunduh.",
                    "Halamannya kelihatan kosong beberapa detik, padahal tulisannya udah",
                    "ada.",
                    "",
                    "Biasanya satu berkas .woff2 cuma untuk satu ketebalan. Butuh 400 dan",
                    "700? Tulis dua blok @font-face dengan font-family yang sama dan",
                    "font-weight yang beda. Pengecualiannya font variabel, yang satu",
                    "berkasnya bisa memuat banyak ketebalan sekaligus.",
                    "",
                    "Bentuk kedua, <link> ke penyedia font. Yang ini masuk ke HTML, di",
                    "dalam <head>:",
                    "",
                    "  <link rel=\"stylesheet\"",
                    "        href=\"https://fonts.googleapis.com/css2?family=Inter\">",
                    "",
                    "Bentuk ketiga, @import. Isinya sama, tapi dipanggil dari dalam",
                    "berkas CSS:",
                    "",
                    "  @import url(\"https://fonts.googleapis.com/css2?family=Inter\");",
                    "",
                    "Jebakan: @import wajib ditaruh di baris paling atas berkas gaya,",
                    "sebelum aturan apa pun. Kalau ditaruh di tengah berkas, dia diabaikan",
                    "tanpa pesan. Font yang \"nggak mau muncul\" sering karena ini.",
                    "",
                    "Bentuk <link> juga lebih cepat. Browser bisa mengunduh berkas gaya",
                    "dan berkas font barengan. Kalau pakai @import, berkas gayamu harus",
                    "selesai dibaca dulu.",
                    "",
                    "Cara mana pun yang kamu pakai, daftar cadangan tetap wajib ditulis.",
                    "Selama berkas font-nya belum datang, atau kalau gagal datang sama",
                    "sekali, yang dipakai adalah nama berikutnya di daftar itu.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Blog resep, portal berita, dan halaman dokumentasi hidup dari teks",
                    "yang enak dibaca lama. Di sana kamu bakal ketemu font merek yang",
                    "dipasang lewat @font-face, daftar cadangan di font-family, dan kolom",
                    "baca yang dibatasi dengan satuan ch.",
                    "",
                    "Kasus kecil: blog resep memakai font \"Nunito\" dari berkasnya sendiri.",
                    "Ada dua keluhan pembaca. Di sinyal lemah, halaman kosong beberapa",
                    "detik sebelum tulisannya muncul. Di laptop kantor, tombol \"Cari resep\"",
                    "hurufnya beda dari teks lain.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pisahkan dua gejala itu, karena penyebabnya beda.",
                    "  2. Halaman kosong: browser menunggu berkas font. Tambah font-display:",
                    "     swap, dan pastikan ada cadangan di font-family:",
                    "      @font-face {",
                    "        font-family: \"Nunito\";",
                    "        src: url(\"font/nunito.woff2\") format(\"woff2\");",
                    "        font-display: swap;",
                    "      }",
                    "      body { font-family: \"Nunito\", system-ui, sans-serif; }",
                    "  3. Huruf tombol beda: <button> dan <input> nggak mewarisi font dari",
                    "     body. Satu aturan ini menambalnya:",
                    "      button, input, select, textarea { font: inherit; }",
                    "  4. Periksa kasus pinggir: kalau font diambil lewat @import, baris",
                    "     itu wajib di paling atas berkas. Di tengah berkas, dia diabaikan",
                    "     tanpa pesan.",
                ]
            },
        ],
    },
    {
        "title": "7. Box Model: margin, border, padding, content",
        "sections": [
            {
                "body": [
                    "Setiap elemen di halaman itu sebuah kotak. Nggak ada pengecualian:",
                    "paragraf, gambar, bahkan satu kata di dalam <span> juga kotak. Tiap",
                    "kotak punya empat lapis, dari dalam ke luar:",
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
                    "Hampir semua kebingungan soal tata letak berawal dari salah membaca",
                    "gambar ini. Pahami sekali sekarang, dan nanti kamu hemat banyak waktu.",
                ]
            },
            {
                "body": [
                    "Padding dan margin paling sering ketuker. Bedanya begini:",
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
                    "Cara cepat mengingatnya:",
                    "  Ingin teks tidak menempel ke garis tepi tombol? -> padding.",
                    "  Ingin dua tombol tidak berdempetan?             -> margin.",
                    "",
                    "Coba sendiri, cuma butuh tiga puluh detik. Kasih sebuah elemen",
                    "background: pink, lalu tambah padding. Daerah pink-nya melebar.",
                    "Sekarang ganti padding dengan margin. Daerah pink-nya tetap, yang",
                    "melebar ruang kosong di sekitarnya. Sekali lihat ini, kamu nggak bakal",
                    "ketuker lagi.",
                    "",
                    "Nilai ringkasnya ditulis searah jarum jam, mulai dari atas:",
                    "  margin: 10px;                  keempat sisi 10px",
                    "  margin: 10px 20px;             atas-bawah 10, kiri-kanan 20",
                    "  margin: 10px 20px 30px;        atas 10, kiri-kanan 20, bawah 30",
                    "  margin: 10px 20px 30px 40px;   atas, kanan, bawah, kiri",
                    "",
                    "Urutannya gampang diingat lewat kata TRouBLe: Top Right Bottom Left.",
                    "Kalau cuma mau satu sisi, tulis nama lengkapnya: margin-top,",
                    "padding-left, border-bottom, dan seterusnya.",
                    "",
                    "border butuh tiga bagian, yaitu tebal, gaya, dan warna:",
                    "  border: 1px solid #ccc;",
                    "",
                    "Kalau bagian gaya (solid, dashed, dotted) nggak ditulis, garisnya",
                    "nggak muncul sama sekali, walaupun tebal dan warnanya udah ada. Ini",
                    "penyebab paling sering kalau border kamu \"hilang\".",
                    "",
                    "Untuk membulatkan sudut, pakai border-radius:",
                    "  border-radius: 8px;   membulatkan sudut",
                    "  border-radius: 50%;   lingkaran, kalau kotaknya bujur sangkar",
                ]
            },
            {
                "body": [
                    "Kenapa box-sizing: border-box hampir selalu dipakai",
                    "",
                    "Secara bawaan, width cuma mengukur content. Padding dan border",
                    "ditambahkan di luar angka itu.",
                    "",
                    "  .kotak { width: 200px; padding: 20px; border: 2px solid black; }",
                    "",
                    "  Lebar sesungguhnya = 2 + 20 + 200 + 20 + 2 = 244px.",
                    "",
                    "Kamu nulis 200, yang muncul 244. Akibatnya baru kerasa waktu dua kotak",
                    "berdampingan, masing-masing width: 50% dan punya padding. Totalnya",
                    "jadi lebih dari 100%, dan kotak kedua turun ke bawah. Kamu bisa",
                    "ngabisin sepuluh menit nyari \"kelebihan\" yang ternyata kamu tulis",
                    "sendiri.",
                    "",
                    "box-sizing: border-box mengubah arti width jadi lebar seluruh kotak,",
                    "dengan padding dan border sudah termasuk. Jadi width: 200px berarti",
                    "200px beneran, berapa pun paddingnya. Yang menyusut adalah ruang",
                    "isinya.",
                    "",
                    "Makanya hampir semua proyek diawali baris ini:",
                    "",
                    "  *, *::before, *::after { box-sizing: border-box; }",
                    "",
                    "Kenapa barisnya nyebut tiga hal? Tanda * artinya semua elemen. Bentuk",
                    "yang pakai dua titik dua (::before dan ::after) namanya",
                    "pseudo-element. Itu dua bagian buatan yang bisa dimiliki tiap elemen,",
                    "tapi nggak pernah ditulis di HTML. Karena nggak ditulis di HTML, *",
                    "sendirian nggak menjangkaunya.",
                    "",
                    "Dua bagian buatan itu sering dipakai untuk garis dan hiasan yang juga",
                    "punya padding, jadi butuh aturan yang sama. Bentuknya dibahas di",
                    "materi Pseudo-class dan Pseudo-element. Untuk sekarang cukup tahu",
                    "bahwa satu baris itu ngurus ketiganya sekaligus.",
                    "",
                    "Baris ini memperbaiki bawaan CSS yang udah lama disesali, bahkan oleh",
                    "orang-orang yang merancang CSS sendiri. Tulis di baris pertama berkas",
                    "gayamu, lalu nggak usah dipikirin lagi selama proyek itu.",
                    "",
                    "Catatan: margin nggak pernah masuk hitungan width, walaupun pakai",
                    "border-box. Memang begitu seharusnya, karena margin ada di luar kotak.",
                ]
            },
            {
                "body": [
                    "Margin yang menyatu (margin collapse)",
                    "",
                    "Misalnya ada dua paragraf berurutan. Yang atas punya margin-bottom:",
                    "20px, yang bawah margin-top: 20px. Jarak di antara keduanya ternyata",
                    "20px, bukan 40px.",
                    "",
                    "Margin vertikal yang bersentuhan itu menyatu. Yang dipakai adalah",
                    "margin yang paling besar, dan angkanya nggak dijumlahkan.",
                    "",
                    "  margin-bottom: 30px  bertemu  margin-top: 10px  ->  jarak 30px",
                    "",
                    "Ini disengaja, dan bukan bug. Coba bayangkan kalau nggak begitu.",
                    "Deretan paragraf yang semuanya punya margin atas dan bawah bakal",
                    "berjarak dua kali lipat di tengah, tapi cuma satu kali di ujung. Nggak",
                    "ada yang mau hasil kayak gitu.",
                    "",
                    "Ada tiga hal yang perlu kamu tahu:",
                    "",
                    "  1. Cuma margin atas dan bawah yang menyatu. Margin kiri dan kanan",
                    "     nggak pernah menyatu. Dua kotak bersebelahan yang masing-masing",
                    "     punya margin 20px berjarak 20+20=40px.",
                    "  2. Penyatuan juga terjadi antara induk dan anak pertamanya. Misalnya",
                    "     anak pertama punya margin-top: 20px, dan induknya nggak punya",
                    "     padding atau border di sisi atas. Margin itu \"bocor\" keluar, dan",
                    "     yang kelihatan bergeser justru induknya. Ini sebabnya kadang ada",
                    "     celah di atas sebuah kotak yang asalnya nggak bisa kamu temukan,",
                    "     dan menghapus padding malah menambah celahnya.",
                    "  3. Margin elemen kosong juga menyatu. Elemen tanpa isi, tanpa padding,",
                    "     dan tanpa border menyatukan margin atas dan bawahnya sendiri jadi",
                    "     satu.",
                    "",
                    "Kalau penyatuan ini mengganggu, begini cara menghentikannya:",
                    "  - Kasih induknya padding atau border di sisi itu. padding-top: 1px",
                    "    udah cukup untuk memutusnya.",
                    "  - Ubah induknya jadi display: flex atau grid. Di dalam flex dan grid,",
                    "    margin nggak pernah menyatu sama sekali.",
                    "  - Cara paling rapi: pakai margin satu arah aja (misalnya cuma",
                    "    margin-bottom), atau pakai gap di flex/grid. Dengan begitu masalah",
                    "    ini nggak pernah muncul.",
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
                    "Soal margin: 0 auto, ada dua syarat yang sering kelupaan:",
                    "",
                    "  1. Elemennya harus punya width atau max-width. auto artinya \"bagi rata",
                    "     sisa ruangnya\". Kalau elemennya udah makan seluruh lebar, nggak ada",
                    "     sisa yang bisa dibagi.",
                    "  2. Cara ini cuma bekerja mendatar. margin: auto 0 nggak menaruh apa",
                    "     pun di tengah secara vertikal. Untuk itu pakai flex atau grid",
                    "     (materi Flexbox dan Grid).",
                    "",
                    "Perhatikan juga padding: 0 16px di .wadah pada contoh. Tanpa padding",
                    "itu, di layar yang lebarnya 720px atau lebih sempit, teksnya nempel ke",
                    "tepi layar. Batas lebar aja nggak cukup. Isi selalu butuh sedikit",
                    "ruang kosong di kiri dan kanannya.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Kartu produk di marketplace, kotak pengumuman di web sekolah, dan",
                    "tombol di aplikasi apa pun dibangun dari empat lapis yang sama:",
                    "content, padding, border, margin. Waktu desainer bilang \"kartunya",
                    "300px\", yang dia maksud lebar sampai garis tepi. Angka itu cuma cocok",
                    "dengan CSS-mu kalau box-sizing: border-box udah dipasang.",
                    "",
                    "Kasus kecil: kolom samping web sekolah selebar 300px. Kartu",
                    "pengumuman di dalamnya ditulis dengan width: 300px, padding: 20px,",
                    "dan border 2px. Hasilnya, kartu itu menonjol keluar dari kolomnya.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Hitung lebar yang tergambar, dari luar ke dalam:",
                    "     2 + 20 + 300 + 20 + 2 = 344px. Kartunya 44px lebih lebar dari",
                    "     kolom.",
                    "  2. Pilih alat: box-sizing: border-box, supaya width mengukur",
                    "     seluruh kotak sampai garis tepi:",
                    "      *, *::before, *::after { box-sizing: border-box; }",
                    "  3. Cek ulang di diagram box model panel Computed. Lebar content",
                    "     sekarang tertulis 256, dan seluruh kartu pas 300px.",
                    "  4. Periksa kasus pinggir: jarak antar kartu. Pakai margin-bottom",
                    "     aja, jangan dicampur margin-top. Margin vertikal yang bersentuhan",
                    "     menyatu, jadi 20px ketemu 20px tetap berjarak 20px.",
                ]
            },
        ],
    },
    {
        "title": "8. Display dan Alur Dokumen",
        "sections": [
            {
                "body": [
                    "Alur dokumen (normal flow) adalah cara browser menata elemen kalau",
                    "kamu nggak nyuruh apa-apa. Elemen disusun dari atas ke bawah, dan di",
                    "dalam satu baris dari kiri ke kanan.",
                    "",
                    "Sebelum belajar flexbox, grid, atau position, pahami dulu sifat dasar",
                    "alur ini, yaitu block dan inline. Flexbox, grid, dan position cuma",
                    "cara mengubah alur yang sama.",
                    "",
                    "display: block",
                    "  - Makan seluruh lebar yang tersedia, jadi tetangganya terdorong ke",
                    "    baris berikutnya.",
                    "  - width dan height berlaku. margin dan padding di keempat sisi berlaku",
                    "    penuh.",
                    "  - Bawaan untuk div, p, h1-h6, ul, li, section, form, footer.",
                    "",
                    "display: inline",
                    "  - Lebarnya cuma sebesar isinya, dan ngalir bareng teks dalam satu",
                    "    baris.",
                    "  - width dan height diabaikan.",
                    "  - margin dan padding atas-bawah nggak mendorong apa pun. Paddingnya",
                    "    tetap tergambar, tapi menimpa baris di atas dan di bawahnya,",
                    "    bukannya bikin ruang.",
                    "  - Bawaan untuk span, a, strong, em, code, label.",
                    "",
                    "display: inline-block",
                    "  - Ngalir dalam baris seperti inline, tapi width, height, dan",
                    "    margin/padding vertikal berlaku seperti block.",
                    "  - Jalan tengah untuk tombol, lencana, dan item menu mendatar.",
                    "",
                    "display: none",
                    "  - Hilang total. Nggak digambar dan nggak nyisain ruang.",
                    "",
                    "Pertanyaan yang paling sering muncul: kenapa width di <span> nggak",
                    "ngaruh? Penyebabnya, span itu inline. Ubah dulu jadi inline-block atau",
                    "block. Aturan yang sama berlaku untuk <a>. Makanya tombol yang dibikin",
                    "dari tautan selalu butuh display: inline-block.",
                    "",
                    "Ada satu pengecualian: <img> secara teknis inline, tapi width dan",
                    "height tetap berlaku. Gambar termasuk replaced element, yaitu elemen",
                    "yang isinya datang dari luar dan punya ukuran sendiri.",
                ]
            },
            {
                "body": [
                    "Tiga cara menyembunyikan, tiga akibat yang beda",
                    "",
                    "  display: none        Hilang. Ruangnya ikut hilang, tetangganya",
                    "                       maju mengisi. Tidak dibacakan pembaca layar.",
                    "  visibility: hidden   Tidak terlihat, TAPI ruangnya tetap kosong",
                    "                       di situ. Tidak dibacakan pembaca layar.",
                    "  opacity: 0           Tidak terlihat, ruang tetap, DAN masih bisa",
                    "                       diklik. Tetap dibacakan pembaca layar.",
                    "",
                    "Yang terakhir itu jebakan beneran. Tombol dengan opacity 0 tetap",
                    "menangkap klik, padahal orangnya nggak tahu ada tombol di situ.",
                    "",
                    "Obatnya satu baris: pointer-events: none. Elemen yang pakai ini jadi",
                    "tembus untuk mouse dan sentuhan. Kliknya lewat begitu aja dan kena apa",
                    "pun yang ada di belakangnya, seolah elemen itu nggak ada. Elemennya",
                    "tetap kelihatan. Yang hilang cuma kemampuannya untuk diklik.",
                    "",
                    "Dua contoh pemakaiannya sehari-hari:",
                    "  - Ikon di dalam kotak isian. Tanpa pointer-events: none, klik yang",
                    "    kebetulan kena ikonnya nggak naruh kursor ke dalam kotak, dan orang",
                    "    ngira kotaknya rusak.",
                    "  - Lapisan yang menutupi seluruh layar untuk gradien atau bayangan.",
                    "    Lapisan itu harus kelihatan, tapi nggak boleh menghalangi satu klik",
                    "    pun ke apa yang ada di bawahnya.",
                    "",
                    "Ingat batasnya: pointer-events cuma ngurus mouse dan sentuhan. Tombol",
                    "yang \"dimatikan\" dengan cara ini masih bisa dicapai pakai tombol Tab,",
                    "dan masih dibacakan pembaca layar. Kalau mau menyingkirkan sesuatu",
                    "sepenuhnya, display: none tetap pilihan yang paling tepat.",
                    "",
                    "Celah aneh di antara elemen inline-block",
                    "",
                    "Dua <li> inline-block yang ditulis di baris berbeda di HTML-nya punya",
                    "jarak sekitar 4px yang nggak pernah kamu tulis. Jarak itu datang dari",
                    "spasi dan ganti baris di antara tagnya. Elemen inline ikut aturan",
                    "teks, dan spasi antarkata memang kelihatan.",
                    "",
                    "Dulu orang ngakalinya dengan nulis tag berdempetan, atau pasang",
                    "font-size: 0 di induknya. Dua cara itu sama-sama ribet. Cara yang",
                    "wajar sekarang: pakai flex atau grid di induknya. Keduanya nggak",
                    "menghitung spasi HTML sama sekali.",
                    "",
                    "Kalau isi lebih besar dari kotaknya:",
                    "  overflow: visible   bawaan, isi meluber keluar begitu saja",
                    "  overflow: hidden    kelebihannya dipotong dan tidak bisa dilihat",
                    "  overflow: auto      bilah gulir muncul hanya kalau perlu",
                    "  overflow-x / overflow-y   khusus satu sumbu",
                    "",
                    "Tabel lebar dan blok kode panjang sebaiknya dibungkus wadah dengan",
                    "overflow-x: auto. Dengan begitu yang bisa digeser ke samping cuma",
                    "isinya, dan seluruh halaman tetap diam. Halaman yang bisa digeser ke",
                    "samping kerasa rusak, dan penyebabnya hampir selalu satu elemen yang",
                    "lebih lebar dari layar.",
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
                    "Gambar itu inline secara bawaan. Artinya gambar duduk di garis dasar",
                    "teks, dan di bawahnya ada sisa ruang beberapa piksel untuk ekor huruf",
                    "seperti g dan y. Di dalam kartu, sisa ini kelihatan sebagai celah",
                    "tipis antara gambar dan tepi bawah kartu. Celah itu nggak datang dari",
                    "margin mana pun. display: block menghilangkannya, karena gambarnya",
                    "nggak ikut aturan teks lagi.",
                    "",
                    "Ini contoh masalah CSS yang khas. Yang kelihatan seperti margin",
                    "misterius ternyata akibat wajar dari satu aturan bawaan. Begitu tahu",
                    "sebabnya, obatnya cuma satu baris.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Di aplikasi tagihan dan toko online, label status seperti \"Lunas\",",
                    "\"Dikirim\", atau \"Menunggu bayar\" biasanya berupa <span> yang duduk di",
                    "tengah baris teks. Tombol \"Beli sekarang\" sering berupa tautan <a>.",
                    "Dua-duanya inline secara bawaan, dan dari situ datang keluhan",
                    "\"width-nya nggak ngaruh\".",
                    "",
                    "Kasus kecil: di daftar tagihan SPP online, tiap baris diakhiri",
                    "<span class=\"status\">Lunas</span> atau \"Belum lunas\". Supaya rapi,",
                    "label diberi latar hijau muda, width: 100px, dan padding: 4px 8px.",
                    "Lebarnya tetap ikut panjang kata, dan latar padding atas-bawahnya",
                    "menimpa baris di atasnya.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pahami sifat elemennya: <span> itu inline. width diabaikan, dan",
                    "     padding atas-bawah tergambar tanpa bikin ruang.",
                    "  2. Pilih alat yang tetap sebaris dengan teks dan menghormati",
                    "     ukuran, yaitu inline-block:",
                    "      .status {",
                    "        display: inline-block;",
                    "        width: 100px;",
                    "        padding: 4px 8px;",
                    "        text-align: center;",
                    "      }",
                    "  3. Periksa kasus pinggir: tagihan yang statusnya belum ada. Kalau",
                    "     labelnya disembunyikan dengan display: none, tempatnya ikut",
                    "     hilang. Pakai visibility: hidden kalau tempat itu harus tetap",
                    "     dipesan, supaya kolom di sebelahnya nggak bergeser.",
                ]
            },
        ],
    },
    {
        "title": "9. Latar, Gradien, dan Gambar dalam Kotak",
        "sections": [
            {
                "body": [
                    "Sampai sini, background selalu berupa satu warna datar. Di kode nyata",
                    "hampir nggak pernah begitu. Latar biasanya berisi foto, tekstur, atau",
                    "gradasi warna.",
                    "",
                    "Satu hal lagi: url() adalah satu-satunya tempat CSS nunjuk ke berkas",
                    "lain. Jadi di sinilah CSS pertama kali bisa gagal gara-gara sesuatu di",
                    "luar berkasnya sendiri.",
                    "",
                    "background itu bentuk ringkas dari delapan properti",
                    "",
                    "Satu kata background menulis delapan properti ini sekaligus:",
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
                    "Akibatnya sama seperti bentuk ringkas font di materi Teks dan Font.",
                    "Kalau kamu menulis background, ketujuh properti lain yang nggak kamu",
                    "sebut dikembalikan ke nilai bawaannya.",
                    "",
                    "  .panel          { background: url(\"pola.png\") repeat; }",
                    "  .panel.terpilih { background: #fff8e1; }      /* polanya HILANG */",
                    "",
                    "Panel terpilih kehilangan polanya, dan nggak ada pesan apa pun yang",
                    "ngasih tahu. Maksudmu tadi ini:",
                    "",
                    "  .panel.terpilih { background-color: #fff8e1; }",
                    "",
                    "Aturan praktisnya: kalau cuma mau mengubah satu bagian, tulis nama",
                    "panjangnya. Bentuk ringkas dipakai waktu kamu menyusun latar dari nol.",
                    "",
                    "Menunjuk berkas gambar: url()",
                    "",
                    "  background-image: url(\"foto.jpg\");",
                    "  background-image: url(foto.jpg);      petiknya boleh dihilangkan",
                    "",
                    "Tanda petik wajib kalau nama berkasnya mengandung spasi atau tanda",
                    "kurung. Yang nggak boleh: spasi di antara url dan kurung bukanya. url",
                    "(foto.jpg) itu nggak sah, dan seluruh deklarasinya dibuang tanpa",
                    "pesan.",
                    "",
                    "Jebakan: jalur di dalam url() dihitung dari letak berkas .css-nya,",
                    "bukan dari halaman HTML yang memakainya. Ini kesalahan yang paling",
                    "sering terjadi di seluruh materi ini.",
                    "",
                    "Susunan folder yang biasa dipakai:",
                    "",
                    "  proyek/",
                    "    index.html",
                    "    gaya/",
                    "      gaya.css        <- berkas yang sedang kamu tulis",
                    "    gambar/",
                    "      hero.jpg",
                    "",
                    "Dari index.html, gambarnya ditulis <img src=\"gambar/hero.jpg\">. Tapi",
                    "dari gaya/gaya.css, jalur yang sama itu salah. Browser bakal nyari",
                    "berkas di proyek/gaya/gambar/hero.jpg dan nggak nemu apa-apa. Yang",
                    "benar, naik satu folder dulu:",
                    "",
                    "  background-image: url(\"../gambar/hero.jpg\");",
                    "",
                    "Seperti biasa, CSS nggak ngasih pesan error. Latarnya cuma kosong.",
                    "Jadi kalau gambar latar nggak muncul, cek jalurnya dulu sebelum curiga",
                    "ke hal lain.",
                ],
            },
            {
                "body": [
                    "Mengulang, menaruh, dan mengukur",
                    "",
                    "Secara bawaan, gambar latar diulang ke segala arah sampai kotaknya",
                    "penuh. Cocok untuk tekstur kecil, tapi jadi berantakan kalau gambarnya",
                    "foto.",
                    "",
                    "  background-repeat: repeat;      bawaan, diulang dua arah",
                    "                     no-repeat;   sekali saja",
                    "                     repeat-x;    hanya mendatar",
                    "                     repeat-y;    hanya menurun",
                    "",
                    "background-position menentukan letak gambar. Nilai pertama untuk arah",
                    "mendatar, nilai kedua untuk arah menurun:",
                    "",
                    "  background-position: center;       sama dengan 'center center'",
                    "  background-position: right top;",
                    "  background-position: 20px 40px;    20 dari kiri, 40 dari atas",
                    "  background-position: 50% 50%;      lihat catatan di bawah",
                    "",
                    "Persen di sini cara kerjanya beda dari dugaan pertama. 50% artinya",
                    "titik 50% di gambar ditempelkan ke titik 50% di kotak. Makanya 50% 50%",
                    "memang menaruh gambar di tengah. Dan 100% 100% menempelkan pojok kanan",
                    "bawah gambar ke pojok kanan bawah kotak. Gambarnya nggak didorong",
                    "keluar sejauh satu kotak penuh.",
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
                    "cover memotong, contain menyisakan ruang kosong. Nggak ada pilihan",
                    "ketiga. Kotak dan gambar jarang punya perbandingan sisi yang sama,",
                    "jadi salah satunya harus ngalah. Untuk foto besar di kepala halaman,",
                    "hampir selalu pakai cover.",
                    "",
                    "Jebakan: contain tanpa no-repeat menyisakan ruang kosong, dan ruang",
                    "itu langsung diisi ulangan gambar yang sama. Hasilnya kayak ubin,",
                    "gambarnya berderet-deret.",
                    "",
                    "Bentuk ringkas lengkap:",
                    "",
                    "  background: #fff url(\"hero.jpg\") center / cover no-repeat;",
                    "              ^    ^               ^        ^     ^",
                    "              |    |               |        |     diulang atau tidak",
                    "              |    |               |        ukuran, wajib sesudah miring",
                    "              |    |               posisi",
                    "              |    gambar",
                    "              warna",
                    "",
                    "Urutan bagian lain bebas. Tapi ukuran cuma boleh ditulis sesudah",
                    "posisi dan sebuah garis miring. Kalau nggak begitu, nilainya nggak",
                    "dikenali dan seluruh deklarasinya dibuang, nggak cuma bagian",
                    "ukurannya:",
                    "",
                    "  background: url(\"hero.jpg\") cover;    salah; latarnya kosong total",
                    "",
                    "Beberapa latar sekaligus",
                    "",
                    "Satu elemen boleh punya beberapa lapis gambar latar, dipisah koma.",
                    "Yang ditulis pertama ada di paling atas. Banyak orang ngira",
                    "kebalikannya.",
                    "",
                    "  background-image:",
                    "    url(\"stempel.png\"),",
                    "    url(\"kertas.png\");",
                    "",
                    "Warna lain sendiri. background-color nggak punya lapisan dan selalu",
                    "ada di paling bawah. Karena itu, di bentuk ringkas, warna cuma boleh",
                    "ditulis di lapisan terakhir.",
                    "",
                    "Dua properti sisanya, sekilas",
                    "",
                    "background-attachment: fixed bikin gambar latar diam waktu halaman",
                    "digulir, jadi isinya seolah lewat di depan foto. Efek ini berat buat",
                    "browser. Banyak browser ponsel mengabaikannya, atau halamannya jadi",
                    "tersendat. Pakai cuma kalau halamannya tetap baik-baik aja tanpa efek",
                    "itu.",
                    "",
                    "background-clip menentukan bagian kotak mana yang diwarnai latar. Nama",
                    "nilainya diambil dari empat lapis box model:",
                    "",
                    "  border-box    bawaan - sampai tepi luar, DI BAWAH garis tepinya",
                    "  padding-box   berhenti di dalam garis tepi",
                    "  content-box   hanya area isi",
                    "",
                    "Kelihatannya sepele, sampai kamu pakai border putus-putus. Dengan",
                    "nilai bawaan border-box, latar ikut tercat di sela-sela garisnya, jadi",
                    "garis putusnya nggak kebaca lagi. Tulis background-clip: padding-box,",
                    "beres.",
                    "",
                    "(Kembarannya, background-origin, mengatur dari tepi mana posisi gambar",
                    "mulai dihitung. Jarang perlu disentuh.)",
                ],
            },
            {
                "body": [
                    "Gradien itu gambar, bukan warna",
                    "",
                    "Ini yang paling sering bikin orang mentok di percobaan pertama:",
                    "",
                    "  background-color: linear-gradient(#fff, #ccc);   tidak pernah jalan",
                    "",
                    "linear-gradient() menghasilkan sebuah gambar yang digambar browser",
                    "sendiri. Tempatnya di background-image, atau di bentuk ringkas",
                    "background. background-color cuma menerima satu warna. Dan seperti",
                    "biasa, nilai yang nggak dikenali dibuang tanpa pesan apa pun.",
                    "",
                    "  background-image: linear-gradient(#fff, #ccc);   benar",
                    "  background: linear-gradient(#fff, #ccc);         benar juga",
                    "",
                    "Karena gradien itu gambar, background-size, background-position, dan",
                    "background-repeat juga berlaku untuknya, sama seperti untuk foto.",
                    "",
                    "Bentuk linear-gradient:",
                    "",
                    "  linear-gradient(#1a4fa0, #7a1f9a)               atas ke bawah (bawaan)",
                    "  linear-gradient(to right, #1a4fa0, #7a1f9a)     kiri ke kanan",
                    "  linear-gradient(to bottom right, #fff, #ccc)    pojok ke pojok",
                    "  linear-gradient(45deg, #fff, #ccc)              sudut sendiri",
                    "",
                    "Soal derajat: 0deg mengarah ke atas, lalu berputar searah jarum jam.",
                    "90deg ke kanan, 180deg ke bawah. Ini beda dari busur derajat di",
                    "sekolah, jadi lihat aja hasilnya, nggak usah dihitung di kepala.",
                    "",
                    "Warnanya boleh lebih dari dua, dan tiap warna boleh dikasih titik",
                    "henti, yaitu posisi tempat warna itu berada di sepanjang gradien:",
                    "",
                    "  linear-gradient(to right, #f2c14e 0%, #e08c3c 40%, #b4451f 100%)",
                    "",
                    "Dua titik henti dengan angka yang sama menghasilkan garis tajam, tanpa",
                    "gradasi. Ini trik umum untuk bikin pita dan pemisah:",
                    "",
                    "  linear-gradient(#f6f5f2 50%, #eceae4 50%)",
                    "",
                    "Ada dua saudaranya yang cara pakainya sama persis:",
                    "",
                    "  radial-gradient(circle at 30% 30%, #ffffff, #cfd4dd)",
                    "      memancar dari sebuah titik, bukan sepanjang garis",
                    "  conic-gradient(#e5484d 0deg 90deg, #eceae4 90deg 360deg)",
                    "      berputar mengelilingi titik pusat; begini cara orang membuat",
                    "      diagram lingkaran tanpa satu pun berkas gambar",
                    "",
                    "Ada juga repeating-linear-gradient, yang mengulang polanya jadi",
                    "deretan garis. Ketiganya tetap gambar, jadi semua aturan di atas",
                    "berlaku juga untuk mereka.",
                    "",
                    "Lapisan gelap di atas foto",
                    "",
                    "Teks putih di atas foto hampir selalu susah dibaca. Satu foto punya",
                    "bagian terang dan bagian gelap sekaligus, dan bagian terangnya menelan",
                    "hurufmu. Ini masalah kontras yang sama dengan di materi Warna dan",
                    "Satuan. Bedanya, latarnya sekarang nggak seragam, jadi rasio",
                    "kontrasnya nggak bisa dihitung sekali untuk seluruh kotak.",
                    "",
                    "Solusinya nggak perlu ganti foto. Tumpuk lapisan gelap tembus pandang",
                    "di atasnya. Lapisan itu berupa gradien dari warna yang sama, dengan",
                    "dua tingkat alfa (tingkat tembus pandang) yang beda:",
                    "",
                    "  .hero {",
                    "    background:",
                    "      linear-gradient(rgb(20 20 25 / 70%), rgb(20 20 25 / 30%)),",
                    "      url(\"../gambar/hero.jpg\") center / cover no-repeat;",
                    "    color: #ffffff;",
                    "  }",
                    "",
                    "Lapisan pertama ada di atas, jadi lapisan gelapnya menutupi foto,",
                    "bukan sebaliknya. Lapisannya sendiri bergradasi. Bagian atas, tempat",
                    "judul berada, lebih gelap. Bagian bawah fotonya tetap kelihatan jelas.",
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
                    "<img> atau background-image?",
                    "",
                    "Pertanyaan penentunya cuma satu: kalau gambar itu hilang, apakah ada",
                    "informasi yang ikut hilang?",
                    "",
                    "  Ya     -> pakai <img> dengan alt. Foto produk, grafik, potret orang,",
                    "            tangkapan layar. Ia ikut tercetak, ikut ditemukan mesin",
                    "            pencari, dan dibacakan pembaca layar lewat alt-nya.",
                    "  Tidak  -> pakai background-image. Tekstur, pola, gradasi, foto hiasan",
                    "            di belakang judul. Latar tidak punya alt, tidak dibacakan",
                    "            siapa pun, dan secara bawaan tidak ikut tercetak.",
                    "",
                    "Kalau foto produk dijadikan background, foto itu hilang dari halaman",
                    "bagi semua orang yang nggak melihat layarnya. Sebaliknya, tekstur",
                    "hiasan yang ditaruh sebagai <img> bikin pembaca layar mengumumkan",
                    "sesuatu yang nggak ada artinya (lihat alt=\"\" di materi HTML soal",
                    "tautan dan gambar).",
                    "",
                    "Menaruh foto di kotak berukuran tetap",
                    "",
                    "Di materi Display dan Alur Dokumen ada resep untuk gambar yang ngalir",
                    "bebas:",
                    "",
                    "  img { max-width: 100%; height: auto; }",
                    "",
                    "Resep itu tetap benar untuk gambar di tengah artikel. Tapi di deretan",
                    "kartu produk, resep itu nggak bisa dipakai. height: auto artinya",
                    "\"setinggi perbandingan aslinya\", padahal yang kamu butuhkan \"setinggi",
                    "kartu di sebelahnya\". Dua permintaan itu nggak bisa jalan bareng.",
                    "Begitu tingginya kamu tentukan, height: auto udah nggak berlaku lagi.",
                    "",
                    "Begitu tinggi dan lebar sama-sama dipaksa, bawaan CSS bakal",
                    "menggepengkan gambarnya. Nama bawaan itu object-fit: fill.",
                    "",
                    "  object-fit: fill      bawaan; ditarik sampai pas, wajah jadi gepeng",
                    "  object-fit: cover     dipotong seperlunya, perbandingannya utuh",
                    "  object-fit: contain   dimuat seluruhnya, sisanya jadi ruang kosong",
                    "  object-fit: none      ukuran asli, kelebihannya terpotong",
                    "",
                    "Nilainya sengaja sama dengan background-size, dan artinya juga sama.",
                    "Bedanya cuma sasarannya. background-size ngurus gambar latar.",
                    "object-fit ngurus isi elemen <img> atau <video> yang sungguhan.",
                    "",
                    "Pasangannya, object-position, menentukan bagian mana yang",
                    "dipertahankan waktu gambar dipotong. Bawaannya 50% 50%, alias tengah.",
                    "",
                    "  object-position: top;      potong dari bawah - aman untuk potret,",
                    "                             karena wajah orang jarang ada di bawah",
                    "",
                    "Ada dua jebakan object-fit:",
                    "  1. object-fit nggak ngaruh sama sekali ke <div>. Ia cuma untuk elemen",
                    "     yang isinya datang dari luar, seperti <img> dan <video>. Itulah",
                    "     replaced element yang disinggung di materi Display dan Alur",
                    "     Dokumen.",
                    "  2. object-fit butuh kotak yang ukurannya udah pasti. Kalau lebar dan",
                    "     tinggi sama-sama auto, nggak ada yang perlu dimuatkan ke mana pun,",
                    "     jadi nilainya kelihatan nggak mempan.",
                    "",
                    "Mengunci perbandingan sisi",
                    "",
                    "  .kartu-foto { width: 100%; aspect-ratio: 4 / 3; object-fit: cover; }",
                    "",
                    "aspect-ratio menghitung sisi yang nggak kamu tulis. Dengan lebar 100%",
                    "dan perbandingan 4/3, tingginya selalu tiga perempat lebarnya, berapa",
                    "pun lebar layarnya. Nilai yang umum: 16 / 9, 4 / 3, 1 / 1, 3 / 2.",
                    "",
                    "Ada untung lain. Ruang kotaknya udah dipesan sebelum berkas gambarnya",
                    "selesai diunduh, jadi halaman nggak melompat waktu gambarnya datang.",
                    "Masalah yang sama juga dijawab atribut width dan height pada <img> di",
                    "materi HTML soal gambar. Keduanya saling melengkapi, dan nggak saling",
                    "menggantikan.",
                    "",
                    "Dua hal lagi soal aspect-ratio:",
                    "  - aspect-ratio cuma bekerja kalau salah satu sisinya auto. Kalau width",
                    "    dan height dua-duanya kamu tulis, aspect-ratio diabaikan tanpa",
                    "    pesan.",
                    "  - aspect-ratio nggak mengurung isinya. Kalau isi kotak lebih tinggi",
                    "    dari jatahnya, kotaknya tetap memanjang mengikuti isi. Untuk",
                    "    memaksanya tetap pada perbandingan itu, jadikan kotaknya wadah gulir",
                    "    dengan overflow: hidden atau overflow: auto.",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Halaman produk di marketplace menampilkan foto dari ratusan penjual,",
                    "dengan ukuran dan bentuk yang macam-macam. Supaya deretan kartunya",
                    "tetap rata, foto dikunci perbandingan sisinya lalu dipotong rapi.",
                    "Banner promo di beranda memakai teknik lain: foto sebagai latar,",
                    "ditumpuk gradien gelap supaya tulisannya terbaca.",
                    "",
                    "Kasus kecil: toko keripik online menerima foto dari pemasok. Ada",
                    "yang 1200 x 800 (melebar) dan ada yang 600 x 900 (tegak). Fotonya",
                    "ditulis dengan width dan height tetap, jadi sebagian kelihatan gepeng.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pahami dulu jenis gambarnya. Foto produk itu informasi, jadi",
                    "     tetap <img> dengan alt, jangan dipindah ke background-image.",
                    "  2. Kunci bentuknya dengan aspect-ratio, lalu potong dengan",
                    "     object-fit supaya nggak gepeng:",
                    "      .foto-produk {",
                    "        display: block;",
                    "        width: 100%;",
                    "        aspect-ratio: 1 / 1;",
                    "        object-fit: cover;",
                    "      }",
                    "  3. Periksa kasus pinggir pertama: height lama harus dihapus. Kalau",
                    "     width dan height dua-duanya ditulis, aspect-ratio diabaikan.",
                    "  4. Kasus pinggir kedua: foto tegak yang mereknya tercetak di bagian",
                    "     atas bungkus. cover menyimpan bagian tengah, jadi atasnya ikut",
                    "     terpotong. Tambah object-position: top di foto itu.",
                ]
            },
        ],
    },
    {
        "title": "10. Bayangan dan Filter",
        "sections": [
            {
                "body": [
                    "box-shadow menggambar bayangan di belakang sebuah kotak. Masalahnya,",
                    "nilainya berupa deretan angka tanpa nama. Kalau kamu nggak tahu",
                    "urutannya, baris kayak gini cuma bisa disalin, nggak bisa dibaca:",
                    "",
                    "  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);",
                    "",
                    "Urutannya selalu sama. Hafalkan sekali, dan CSS orang lain jadi bisa",
                    "kamu baca:",
                    "",
                    "  box-shadow: <geser-x> <geser-y> <kabur> <sebar> <warna>;",
                    "",
                    "  geser-x   ke kanan kalau positif, ke kiri kalau negatif",
                    "  geser-y   ke BAWAH kalau positif, ke atas kalau negatif",
                    "  kabur     0 berarti tepinya tajam; makin besar, makin lembut dan melebar",
                    "  sebar     membesarkan (positif) atau mengecilkan (negatif) bayangannya",
                    "  warna     hampir selalu hitam yang tembus pandang",
                    "",
                    "Kenapa geser-y positif berarti ke bawah",
                    "",
                    "Sumbu tegak di CSS dihitung menurun dari tepi atas. Sama seperti top:",
                    "10px, yang memindahkan elemen ke bawah. Jadi 2px artinya bayangannya",
                    "jatuh 2px di bawah kotaknya, seolah cahaya datang dari atas.",
                    "",
                    "Makanya hampir semua bayangan di antarmuka berbentuk 0 <sesuatu>.",
                    "geser-x-nya nol, karena cahaya di layar disepakati datang lurus dari",
                    "atas, nggak dari samping.",
                    "",
                    "Dua angka terakhir (kabur dan sebar) boleh nggak ditulis, jadi kamu",
                    "bakal ketemu tiga bentuk:",
                    "",
                    "  box-shadow: 4px 4px red;                   x, y saja - bayangan tajam",
                    "  box-shadow: 0 2px 8px rgba(0, 0, 0, .15);  x, y, kabur   <- paling sering",
                    "  box-shadow: 0 6px 12px -4px #333;          x, y, kabur, sebar",
                    "",
                    "Warnanya juga boleh ditulis paling depan. rgba(0,0,0,.15) 0 2px 8px",
                    "itu sah, dan artinya sama persis. Beberapa pustaka nulisnya begitu,",
                    "jadi nggak usah kaget.",
                    "",
                    "Kenapa warnanya hitam tembus pandang, bukan abu-abu",
                    "",
                    "rgba(0, 0, 0, 0.15) artinya hitam dengan tingkat kepekatan 0,15. Ini",
                    "bentuk lama dari rgb(0 0 0 / 15%) yang kamu pakai di materi Warna dan",
                    "Satuan. Dua-duanya sah, tapi di kode bayangan, bentuk rgba() jauh",
                    "lebih sering kelihatan.",
                    "",
                    "Hitam tembus pandang menggelapkan apa pun yang ada di belakangnya.",
                    "Jadi bayangan yang sama tetap masuk akal di atas latar putih maupun",
                    "latar biru. Kalau kamu pakai warna pekat seperti #cccccc, di atas",
                    "latar berwarna hasilnya kayak noda abu-abu yang ditempel.",
                    "",
                    "Dua hal kecil yang menghemat waktu. Bayangan otomatis ikut",
                    "border-radius, jadi sudut membulat dapat bayangan membulat tanpa perlu",
                    "diatur. Lalu box-shadow: none adalah cara mematikannya lagi.",
                ],
            },
            {
                "body": [
                    "inset: bayangan di dalam kotak",
                    "",
                    "Tambahkan kata inset di depan nilainya, dan bayangannya pindah ke",
                    "sebelah dalam:",
                    "",
                    "  box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);",
                    "",
                    "Efeknya berlawanan. Tanpa inset, kotak kelihatan terangkat dari",
                    "halaman. Dengan inset, kotak kelihatan cekung ke dalam halaman.",
                    "Makanya kotak isian dan tombol yang lagi ditekan sering pakai inset.",
                    "Cekung artinya \"di sini tempat isi masuk\", atau \"ini lagi kamu tekan\".",
                    "",
                    "Beberapa bayangan sekaligus, dipisah koma",
                    "",
                    "  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.06),",
                    "              0 4px 12px rgba(0, 0, 0, 0.12);",
                    "",
                    "Yang ditulis pertama digambar paling atas, yang berikutnya di",
                    "belakangnya.",
                    "",
                    "Dua bayangan tipis kelihatan lebih alami daripada satu bayangan tebal.",
                    "Alasannya, benda sungguhan menjatuhkan dua bayangan sekaligus. Ada",
                    "bayangan rapat dan agak gelap tepat di bawah tempat benda itu",
                    "menyentuh, dan ada bayangan lebar yang samar banget di sekelilingnya.",
                    "",
                    "Satu bayangan besar nggak punya titik sentuh itu, jadi kotaknya",
                    "kelihatan melayang di dalam kabut. Supaya bayangannya kelihatan,",
                    "kepekatannya terpaksa dinaikkan sampai jadi lingkaran abu-abu kotor di",
                    "belakang kartu. Dua lapis tipis tetap ringan dan tetap kelihatan.",
                    "",
                    "box-shadow nggak makan ruang",
                    "",
                    "Bayangan nggak ikut dihitung dalam lebar dan tinggi elemen, dan nggak",
                    "mendorong tetangga mana pun. Menambahkan bayangan nggak pernah",
                    "menggeser tata letak. Sifat ini penting banget untuk penanda fokus.",
                    "",
                    "Bandingkan dengan border. Kalau penanda fokus dibikin dari border:",
                    "2px, elemennya bertambah 2px di keempat sisi setiap kali difokus.",
                    "Seluruh baris di sekitarnya ikut bergeser, dan halamannya kelihatan",
                    "berkedut tiap kali kamu tekan Tab. Dengan box-shadow, nggak ada yang",
                    "bergerak.",
                    "",
                    "Makanya cincin fokus modern sering dibikin begini, dengan kabur 0 dan",
                    "sebar 3px:",
                    "",
                    "  box-shadow: 0 0 0 3px rgba(26, 79, 160, 0.45);",
                    "",
                    "Geser nol dan kabur nol, jadi yang tergambar adalah cincin rapi",
                    "selebar 3px yang mengikuti border-radius elemennya. Cara lainnya,",
                    "outline, dibahas di materi Pseudo-class dan Pseudo-element. Dua-duanya",
                    "sama-sama nggak makan ruang.",
                    "",
                    "Catatan: cincin dari box-shadow ikut hilang di mode kontras tinggi",
                    "sistem operasi. Karena itu kode sungguhan biasanya juga menulis",
                    "outline: 2px solid transparent. Baris ini kelihatan nggak berguna,",
                    "tapi baris ini yang bikin penanda fokus tetap muncul di mode itu.",
                    "",
                    "Tangga elevasi: sepakati tiga tingkat",
                    "",
                    "Godaan terbesarnya adalah ngetik angka baru tiap kali bikin komponen:",
                    "0 3px 7px di kartu, 0 4px 9px di dialog, 0 2px 6px di tombol. Sesudah",
                    "sepuluh kali, nggak ada dua benda yang tingginya sejajar. Mata",
                    "menangkapnya sebagai halaman yang berantakan, tapi nggak bisa nunjuk",
                    "sebabnya.",
                    "",
                    "Bayangan adalah cara halaman menunjukkan jarak sebuah benda dari",
                    "permukaan. Jarak itu disebut elevasi. Kalau jaraknya cuma boleh tiga",
                    "(menempel, terangkat sedikit, mengambang jauh), bayangannya juga cuma",
                    "boleh tiga.",
                    "",
                    "Simpan ketiganya sebagai variabel (materi Variabel CSS dan Cara Menata",
                    "Berkas Gaya), sama seperti tangga jarak --s1 sampai --s6. Dengan",
                    "begitu seluruh kedalaman halaman diatur dari satu tempat.",
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
                    "text-shadow: saudara yang lebih pendek",
                    "",
                    "  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.55);",
                    "",
                    "Bentuknya sama, tapi cuma tiga angka: geser-x, geser-y, kabur, lalu",
                    "warna. Nggak ada sebar dan nggak ada inset, karena dua-duanya nggak",
                    "masuk akal untuk huruf. Beberapa bayangan sekaligus tetap boleh,",
                    "dipisah koma seperti box-shadow.",
                    "",
                    "Gunanya jelas: teks di atas foto. Foto punya bagian terang dan bagian",
                    "gelap, jadi warna teks apa pun bakal tenggelam di salah satunya.",
                    "Bayangan tipis ngasih huruf tepi gelapnya sendiri, jadi teksnya tetap",
                    "terbaca di mana pun.",
                    "",
                    "Tapi jangan berlebihan. Bayangan tebal di teks isi bikin huruf",
                    "kelihatan kabur dan capek dibaca. Ini masalah kontras yang sama dengan",
                    "di materi Warna dan Satuan. Untuk teks panjang di atas foto, lebih",
                    "baik gelapkan fotonya dengan lapisan hitam tembus pandang di atasnya,",
                    "daripada menebalkan bayangan tiap huruf.",
                    "",
                    "filter mengolah tampilan elemen sebelum digambar:",
                    "",
                    "  filter: blur(4px);         mengaburkan elemen ITU beserta seluruh isinya",
                    "  filter: grayscale(100%);   0% apa adanya, 100% hitam-putih penuh",
                    "  filter: brightness(1.2);   1 apa adanya, di bawah 1 gelap, di atas 1 terang",
                    "  filter: contrast(0.8);     1 apa adanya, 0 membuat semuanya abu rata",
                    "  filter: saturate(1.4);     pekat-tidaknya warna; saturate(0) = grayscale(1)",
                    "  filter: invert(100%);      warna dibalik, seperti klise foto",
                    "  filter: drop-shadow(0 2px 3px rgba(0, 0, 0, 0.35));",
                    "",
                    "Nilai persen dan angka biasa sama aja: 100% = 1, 50% = 0.5. blur()",
                    "lain sendiri, karena ia butuh satuan panjang (4px), bukan persen.",
                    "",
                    "Beberapa fungsi bisa dirangkai dalam satu nilai, dipisah spasi:",
                    "",
                    "  filter: grayscale(100%) brightness(1.1);",
                    "",
                    "Fungsinya dikerjakan dari kiri ke kanan, jadi urutannya berpengaruh.",
                    "Ada satu jebakan yang hampir semua orang pernah kena:",
                    "",
                    "  .foto { filter: grayscale(100%); filter: blur(2px); }",
                    "",
                    "Yang berlaku cuma blur. filter itu satu properti, jadi deklarasi kedua",
                    "menimpa yang pertama seluruhnya, sesuai aturan cascade di materi",
                    "Pemilih. Kalau mau dua-duanya, tulis dalam satu baris, dipisah spasi.",
                    "",
                    "blur() punya dua sifat yang perlu kamu tahu. Pertama, teks di dalamnya",
                    "ikut kabur. Itu memang gunanya kalau dipakai untuk isi di balik",
                    "dialog. Kedua, tepinya ikut memudar, jadi elemennya kelihatan sedikit",
                    "menyusut.",
                    "",
                    "drop-shadow() dan box-shadow itu beda:",
                    "",
                    "  box-shadow      selalu mengikuti KOTAK elemennya (dan border-radius-nya)",
                    "  drop-shadow()   mengikuti BENTUK yang benar-benar tergambar",
                    "",
                    "Ambil contoh logo PNG atau SVG dengan latar tembus pandang. box-shadow",
                    "menggambar bayangan persegi di sekeliling gambarnya, termasuk di",
                    "bagian yang kosong. Hasilnya kayak logo yang ditempel di atas kartu",
                    "abu-abu. drop-shadow() cuma membayangi piksel yang memang ada, jadi",
                    "logo berbentuk bintang dapat bayangan berbentuk bintang. Nilainya sama",
                    "dengan text-shadow: tiga angka dan warna, tanpa sebar.",
                    "",
                    "backdrop-filter menyaring apa yang ada di belakang:",
                    "",
                    "  backdrop-filter: blur(12px);",
                    "",
                    "filter mengolah elemennya sendiri. backdrop-filter mengolah apa pun",
                    "yang ada di belakang elemen itu. Ini yang bikin bilah kepala dan kartu",
                    "kelihatan seperti kaca buram. Isinya tetap tajam, yang buram halaman",
                    "di baliknya.",
                    "",
                    "Jebakan: kalau latar elemennya penuh (background: white), nggak ada",
                    "yang kelihatan berubah. Bagian belakangnya memang dikaburkan, tapi",
                    "hasilnya tertutup rapat oleh latar elemen itu sendiri. Latarnya wajib",
                    "tembus pandang sebagian:",
                    "",
                    "  background: rgba(255, 255, 255, 0.72);",
                    "",
                    "Safari versi lama cuma kenal bentuk berawalan -webkit-backdrop-filter.",
                    "Kode nyata masih nulis dua-duanya, yang berawalan lebih dulu. Soal",
                    "awalan vendor nanti ada materinya sendiri.",
                    "",
                    "Satu lagi soal biaya. blur, apalagi backdrop-filter di area lebar,",
                    "termasuk pekerjaan paling berat yang bisa kamu minta dari browser.",
                    "Untuk satu bilah kepala nggak masalah. Untuk sesuatu yang bergerak",
                    "atau selebar layar penuh, siap-siap animasinya tersendat di komputer",
                    "yang nggak kencang.",
                ],
            },
            {
                "heading": "Kaca buram, teks di atas foto, dan bayangan berbentuk (gaya.css)",
                "body": [
                    "Satu keluarga: opacity, filter, dan transform",
                    "",
                    "Tiga properti ini kelihatannya nggak berhubungan. Tapi semuanya punya",
                    "satu efek samping yang sama. Elemen yang memakai salah satunya membuat",
                    "stacking context baru, yaitu semacam ruang tumpuk tersendiri.",
                    "backdrop-filter juga begitu. Akibatnya bisa repot:",
                    "",
                    "  1. z-index anak-anaknya cuma dibandingkan di dalam ruang itu. Anak",
                    "     dengan z-index 9999 di dalam induk yang pakai filter tetap nggak",
                    "     bisa naik melewati saudara induknya. Yang perlu dinaikkan induknya,",
                    "     bukan anaknya.",
                    "  2. Khusus filter, transform, dan backdrop-filter (opacity nggak",
                    "     termasuk): anak dengan position: fixed berhenti mengacu ke jendela,",
                    "     dan mulai mengacu ke elemen itu. Dialog yang harusnya menutupi",
                    "     layar tiba-tiba terkurung di dalam sebuah kartu.",
                    "",
                    "Dua masalah ini nggak ngasih pesan error, dan penyebabnya jauh dari",
                    "gejalanya. Yang rusak z-index sebuah tombol, padahal penyebabnya satu",
                    "baris filter di elemen kakeknya. Materi Position bakal nyebut aturan",
                    "ini lagi waktu membahas z-index. Karena sekarang kamu udah kenal",
                    "propertinya, aturan itu nanti nggak lagi sekadar hafalan.",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Situs koperasi, sekolah, atau panitia acara sering punya bagian",
                    "\"Mitra Kami\" berisi deretan logo. Logonya biasanya PNG berlatar",
                    "transparan, dan desainer suka minta logo tampil abu-abu lalu",
                    "berwarna lagi saat ditunjuk kursor. Pekerjaan seperti ini jatahnya",
                    "filter, dan bayangannya pakai drop-shadow().",
                    "",
                    "Kasus kecil: halaman koperasi menampilkan delapan logo PNG mitra.",
                    "Permintaannya: logo abu-abu, berwarna saat disentuh kursor, dan",
                    "punya bayangan tipis yang mengikuti bentuk logonya.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pahami bentuk gambarnya. box-shadow mengikuti kotak <img>, jadi",
                    "     bayangannya persegi, termasuk di bagian yang transparan.",
                    "     drop-shadow() mengikuti piksel yang memang tergambar.",
                    "  2. Gabungkan dua fungsi dalam satu baris filter, dipisah spasi.",
                    "     Dua baris filter terpisah saling menimpa:",
                    "      .logo-mitra {",
                    "        filter: grayscale(100%) drop-shadow(0 1px 2px rgba(0, 0, 0, 0.3));",
                    "      }",
                    "      .logo-mitra:hover {",
                    "        filter: drop-shadow(0 1px 2px rgba(0, 0, 0, 0.3));",
                    "      }",
                    "  3. Periksa kasus pinggir: :hover yang cuma menulis filter: none ikut",
                    "     membuang bayangannya. filter itu satu properti, jadi fungsi yang",
                    "     masih kamu mau harus ditulis ulang.",
                ]
            },
        ],
    },
    {
        "title": "11. Transform: Menggeser, Memutar, dan Menskala",
        "sections": [
            {
                "body": [
                    "transform bekerja pada elemen yang udah selesai ditata browser. Dia",
                    "mengambil gambar elemen itu, lalu menggambarnya ulang: digeser,",
                    "diputar, dimiringkan, atau diperbesar.",
                    "",
                    "Kuncinya ada di kata \"udah selesai ditata\". Browser menata halaman",
                    "dulu sampai beres. transform baru bekerja sesudahnya, di atas hasil",
                    "penataan itu.",
                    "",
                    "Akibatnya cuma satu, tapi ini yang bikin transform beda dari semua",
                    "yang udah kamu pelajari: tempat yang udah dipesan elemen itu di alur",
                    "dokumen nggak berubah sama sekali. Tetangganya nggak bergeser, nggak",
                    "ada yang turun sebaris, dan tinggi induknya tetap sama.",
                    "",
                    "  margin-top: -20px",
                    "      menaikkan elemennya DAN menarik semua yang di bawahnya ikut",
                    "      naik. Seluruh halaman ditata ulang.",
                    "",
                    "  transform: translateY(-20px)",
                    "      menaikkan gambarnya saja. Tetangganya tidak tahu apa-apa dan",
                    "      tidak bergerak semilimeter pun.",
                    "",
                    "Bandingkan juga dengan position: relative ditambah top, yang dibahas",
                    "di materi Position. Dua-duanya tetap memesan tempat asalnya, jadi",
                    "hasilnya sekilas mirip. Bedanya ada empat:",
                    "  - relative harus mengubah position dulu. transform langsung berlaku",
                    "    di elemen static biasa tanpa syarat apa pun.",
                    "  - top dan left cuma bisa menggeser. transform juga bisa memutar,",
                    "    menskala, dan memiringkan, dan nggak ada properti lain yang bisa",
                    "    begitu.",
                    "  - Persennya dihitung dari hal yang beda. Ini jebakan tersendiri,",
                    "    dibahas di bagian berikutnya.",
                    "  - transform jauh lebih ringan buat digerakkan. Alasannya ada di",
                    "    bagian terakhir materi ini.",
                    "",
                    "Semua fungsinya ditulis di satu properti, dipisah spasi:",
                    "",
                    "  transform: translateY(-2px) scale(1.05) rotate(3deg);",
                    "",
                    "Yang paling sering makan waktu di awal",
                    "",
                    "Jebakan: transform nggak berlaku di elemen display: inline. <span>,",
                    "<a>, dan <em> yang masih polos nggak bergerak sedikit pun, dan CSS",
                    "seperti biasa diam aja. Ini kembaran masalah \"kenapa width di <span>",
                    "nggak ngaruh\" di materi Display dan Alur Dokumen. Obatnya juga sama:",
                    "kasih display: inline-block dulu.",
                    "",
                    "Yang bikin makin licin, DevTools tetap menampilkan transform-nya",
                    "seolah berlaku, lengkap dengan nilainya. Browser cuma nggak",
                    "menggerakkan elemennya. Jadi aturan yang kelihatan di panel gaya",
                    "belum tentu bekerja. Patokannya apa yang bergerak di layar.",
                ],
            },
            {
                "body": [
                    "translate: menggeser",
                    "",
                    "  transform: translateX(20px);       ke kanan 20px",
                    "  transform: translateY(-8px);       ke ATAS 8px",
                    "  transform: translate(20px, -8px);  dua sekaligus, x dulu baru y",
                    "  transform: translate(20px);        y dianggap 0",
                    "",
                    "Sumbu Y menghitung ke bawah sebagai positif, sama seperti di seluruh",
                    "CSS. Jadi translateY(10px) menurunkan elemen, nggak menaikkan.",
                    "",
                    "Persen di translate beda dari hampir semua properti CSS lain:",
                    "",
                    "  width: 50%                  -> setengah lebar INDUKNYA",
                    "  left: 50%                   -> setengah lebar ACUANNYA, yaitu leluhur",
                    "                                 positioned terdekatnya",
                    "  transform: translateX(50%)  -> setengah lebar ELEMEN ITU SENDIRI",
                    "",
                    "Jadi translateX(100%) artinya \"geser sejauh persis selebar badanmu",
                    "sendiri\". Berapa pun lebar induknya, dan kamu nggak perlu tahu lebar",
                    "elemennya. Makanya panel geser hampir selalu ditulis begini:",
                    "translateX(-100%) menyimpannya persis di sebelah kiri tepi layar, dan",
                    "translateX(0) memunculkannya lagi. Kalau besok lebar panelnya",
                    "berubah, nggak ada satu angka piksel pun yang perlu diganti.",
                    "",
                    "Pola yang bakal sering kamu temui: memusatkan sesuatu",
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
                    "  1. top: 50% dan left: 50% menaruh pojok kiri atas elemen tepat di",
                    "     titik tengah. Persennya dihitung dari acuannya. Hasilnya elemen",
                    "     kelihatan melenceng ke kanan bawah, dan makin besar elemennya,",
                    "     makin jauh melencengnya.",
                    "  2. translate(-50%, -50%) menariknya mundur setengah lebarnya",
                    "     sendiri dan setengah tingginya sendiri. Sekarang titik tengah",
                    "     elemen duduk tepat di titik tengah acuannya.",
                    "",
                    "Kenapa nggak pakai margin-left: -150px aja, kayak cara lama? Angka",
                    "itu mengharuskan kamu tahu lebar elemennya. Begitu isinya bertambah",
                    "satu baris, letaknya meleset lagi. Persen di translate nggak pernah",
                    "perlu dihitung ulang, dan itulah alasan pola ini dipakai.",
                    "",
                    "Untuk memusatkan sesuatu yang masih ikut alur, flexbox atau grid lebih",
                    "tepat dan jauh lebih gampang dibaca. Pola translate ini dipakai justru",
                    "waktu elemennya udah keluar dari alur, misalnya dialog, tooltip, atau",
                    "lencana. Di situ flex udah nggak punya pegangan apa-apa ke elemennya.",
                ],
            },
            {
                "body": [
                    "scale: membesarkan dan mengecilkan",
                    "",
                    "  transform: scale(1.05);     105% ke segala arah",
                    "  transform: scale(2, 0.5);   lebar dua kali, tinggi setengah",
                    "  transform: scaleX(1.2);     melebar saja, tinggi tetap",
                    "  transform: scaleY(0.5);     memendek saja, lebar tetap",
                    "  transform: scaleX(-1);      cermin: kiri jadi kanan",
                    "",
                    "Angkanya itu pengali, bukan ukuran. 1 artinya apa adanya, 0.5 artinya",
                    "setengah, 0 artinya menghilang jadi setitik. Nggak ada satuannya.",
                    "scale(2px) itu salah, dan dibuang browser tanpa pesan apa pun.",
                    "",
                    "Yang membesar nggak cuma kotaknya. Teksnya ikut membesar, garis",
                    "tepinya ikut menebal, bayangannya ikut melebar, sudut bulatnya ikut",
                    "melar. Rasanya kayak memperbesar foto elemennya, beda dengan mengubah",
                    "width dan height. Karena yang diperbesar hasil gambarnya, teks bisa",
                    "kelihatan kasar kalau pengalinya besar.",
                    "",
                    "rotate: memutar",
                    "",
                    "  transform: rotate(45deg);    45 derajat searah jarum jam",
                    "  transform: rotate(-90deg);   berlawanan arah jarum jam",
                    "  transform: rotate(0.25turn); seperempat putaran, sama dengan 90deg",
                    "",
                    "Satuannya wajib ditulis. rotate(45) tanpa deg diabaikan tanpa pesan,",
                    "dan kamu bakal ngira transform-nya yang rusak. Satuan turn sering",
                    "lebih enak dibaca: 1turn = 360deg. Ada juga rad dan grad, tapi jarang",
                    "banget dipakai.",
                    "",
                    "skew: memiringkan",
                    "",
                    "  transform: skewX(-10deg);   memiringkan seperti huruf miring",
                    "  transform: skewY(4deg);     memiringkan sumbu tegaknya",
                    "",
                    "skew dipakai untuk hiasan, misalnya pita diskon atau garis serong di",
                    "latar. Hindari di teks, karena hurufnya ikut terperas dan jadi lebih",
                    "susah dibaca.",
                    "",
                    "transform-origin: titik jangkar semua gerakan itu",
                    "",
                    "Tiap putaran dan tiap skala punya satu titik yang nggak ikut bergerak.",
                    "Bawaannya titik tengah elemen, yaitu center center, sama artinya",
                    "dengan 50% 50%.",
                    "",
                    "  transform-origin: left top;       pojok kiri atas",
                    "  transform-origin: bottom center;  tengah sisi bawah",
                    "  transform-origin: 0 100%;         sama dengan left bottom",
                    "",
                    "Pintu berayun dari engselnya: transform-origin: left center. Jarum jam",
                    "berputar dari pangkalnya: transform-origin: bottom center. Pita yang",
                    "berputar dari pojok butuh transform-origin: left top. Tanpa baris itu,",
                    "ketiganya berputar di titik tengahnya sendiri dan kelihatan melayang,",
                    "nggak kayak benda yang punya engsel.",
                    "",
                    "transform-origin juga mengubah arah scale. Dengan left top, elemen",
                    "membesar ke kanan dan ke bawah aja. Dengan nilai bawaannya, elemen",
                    "melebar rata ke empat arah.",
                ],
            },
            {
                "heading": "Dua aturan penulisan, lalu polanya di berkas nyata",
                "body": [
                    "Pertama: urutan fungsinya ngaruh, dibaca dari kiri ke kanan",
                    "",
                    "  transform: translateX(50px) rotate(45deg);",
                    "      geser 50px ke kanan dulu, baru putar di tempat barunya.",
                    "",
                    "  transform: rotate(45deg) translateX(50px);",
                    "      putar dulu. Sumbu elemennya ikut miring 45 derajat, jadi",
                    "      geseran 50px sesudahnya berjalan MIRING ke kanan bawah,",
                    "      bukan mendatar.",
                    "",
                    "Dua-duanya sah, dan hasilnya beda. Kalau elemenmu mendarat di tempat",
                    "aneh sesudah kamu menambah rotate, curigai urutannya dulu, baru",
                    "angkanya.",
                    "",
                    "Kedua: transform di dua aturan nggak bertumpuk",
                    "",
                    "  .ikon       { transform: rotate(45deg); }",
                    "  .ikon.besar { transform: scale(1.5); }     <- rotate-nya HILANG",
                    "",
                    "transform itu satu properti dengan satu nilai, persis seperti color.",
                    "Aturan yang dipakai browser menimpa seluruh nilainya, nggak",
                    "menambahinya.",
                    "",
                    "Ini paling sering kejadian di :hover. Aturan dasarnya udah nulis",
                    "rotate(-1deg), lalu aturan hover-nya cuma nulis scale(1.02). Hasilnya,",
                    "kartunya mendadak lurus tiap kali disentuh. Kelihatannya kayak ada",
                    "aturan lain yang ikut jalan, padahal itu cuma penimpaan biasa.",
                    "",
                    "Obatnya: tulis ulang semua fungsi yang masih kamu mau.",
                    "",
                    "  .kartu:hover { transform: rotate(-1deg) scale(1.02); }",
                    "",
                    "CSS zaman sekarang juga punya properti terpisah translate, rotate,",
                    "dan scale. Ketiganya berdiri sendiri dan nggak saling menimpa. Bagus",
                    "untuk kode baru. Tapi transform yang bakal kamu baca di hampir semua",
                    "berkas yang udah ada, jadi kuasai bentuk ini dulu.",
                    "",
                    "Contoh di bawah belum bergerak halus: perubahannya melompat seketika.",
                    "Yang bikin halus itu properti lain, transition, dan dia punya materi",
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
                    "Tiga efek samping yang perlu kamu ingat",
                    "",
                    "Elemen yang punya transform, dengan nilai apa pun selain none, ikut",
                    "berubah sifatnya. Yang berubah nggak cuma tampilannya.",
                    "",
                    "  1. Dia bikin stacking context baru.",
                    "     Stacking context itu kelompok tumpukan sendiri untuk z-index.",
                    "     Nanti di materi Position ada kalimat ini: \"induk yang ber-opacity",
                    "     kurang dari 1, ber-transform, atau ber-filter membuat konteks",
                    "     baru\". Contohnya begini. Begitu sebuah kartu dikasih scale(1.02) waktu",
                    "     di-hover, seluruh isinya terkurung di dalam kartu itu. Tooltip di",
                    "     dalam kartu, walaupun z-index-nya 9999, tetap nggak bisa muncul",
                    "     di atas kartu sebelahnya. Gejalanya khas: \"z-index-nya jalan,",
                    "     sampai aku menambah efek hover\".",
                    "  2. Dia jadi acuan buat anak yang ber-position: fixed.",
                    "     Biasanya fixed berpatokan pada jendela browser dan nggak ikut",
                    "     bergulir. Tapi kalau ada leluhurnya yang ber-transform, patokannya",
                    "     pindah ke elemen itu, dan elemen fixed tadi ikut bergulir seperti",
                    "     absolute biasa. Ini penyebab \"dialog fixed-ku ikut bergerak",
                    "     waktu halaman digulir\". Penyebabnya susah dilacak, karena",
                    "     sumbernya ada di elemen lain beberapa tingkat di atasnya, sering",
                    "     ditulis orang lain, dan kelihatan nggak ada hubungannya. Anak yang",
                    "     ber-position: absolute juga kena: leluhur yang ber-transform",
                    "     dihitung sebagai acuannya walaupun position-nya static.",
                    "  3. Teks bisa sedikit kabur di nilai pecahan.",
                    "     translateY(-0.5px) atau scale(1.03) bikin huruf mendarat di antara",
                    "     piksel. Browser lalu mengaburkannya sedikit supaya tetap kelihatan",
                    "     halus. Pakai angka bulat kalau bisa. Kalau nggak bisa, terima aja",
                    "     kaburnya, biasanya nggak kerasa di gerakan yang sekejap.",
                    "",
                    "Kenapa transform dan opacity disebut dua properti paling ringan",
                    "",
                    "Untuk menggambar halaman, browser mengerjakan tiga tahap berurutan:",
                    "menghitung tata letak (layout), mewarnai pikselnya (paint), lalu",
                    "menyusun lapisan-lapisannya jadi satu gambar (composite).",
                    "",
                    "  Mengubah width, height, top, margin  -> mengulang KETIGA tahapnya.",
                    "  Mengubah color atau background       -> mengulang paint + composite.",
                    "  Mengubah transform atau opacity      -> cukup composite saja.",
                    "",
                    "Tata letaknya memang nggak berubah sama sekali, ingat kalimat pertama",
                    "materi ini. Karena itu menggeser sesuatu pakai translateX terasa",
                    "halus, sedangkan menggeser hal yang sama pakai left terasa tersendat,",
                    "apalagi di ponsel yang tenaganya kecil.",
                    "",
                    "Patokan praktisnya: kalau sesuatu harus bergerak, gerakkan transform",
                    "dan opacity-nya, jangan properti lain. Materi Transisi dan Animasi",
                    "memakai patokan ini dari awal sampai akhir.",
                    "",
                    "Sekilas soal 3D, supaya nggak kaget waktu ketemu di kode orang",
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
                    "Untuk sekarang, simpan satu hal aja: kalau kamu lihat rotateY di",
                    "sebuah berkas, cari perspective di induknya. Kalau nggak ada, itu",
                    "penyebab efeknya kelihatan aneh.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Tombol \"Tambah ke keranjang\" yang terangkat sedikit saat ditunjuk",
                    "kursor, panel menu yang keluar dari kiri di aplikasi pesan antar, dan",
                    "panah yang berputar saat daftar dibuka: semuanya transform. Alasannya",
                    "selalu sama. transform menggeser gambar elemen tanpa menata ulang",
                    "halaman di sekitarnya.",
                    "",
                    "Kasus kecil: di halaman toko, tombol keranjang diberi efek naik 3px",
                    "saat disentuh kursor lewat margin-top: -3px. Akibatnya seluruh",
                    "daftar produk di bawahnya ikut naik-turun tiap kali kursor lewat.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pahami penyebabnya: margin mengubah tata letak, jadi tetangga di",
                    "     bawahnya ikut ditarik naik.",
                    "  2. Pilih alat yang cuma menggeser gambarnya. Tempat tombol di alur",
                    "     dokumen tetap, dan nggak ada yang ikut bergerak:",
                    "      .tombol-keranjang:hover {",
                    "        transform: translateY(-3px);",
                    "      }",
                    "  3. Periksa kasus pinggir pertama: kalau tombolnya ternyata <a>, dia",
                    "     inline dan nggak bisa di-transform. Pasang display: inline-block.",
                    "  4. Kasus pinggir kedua: kalau aturan dasar tombol udah punya",
                    "     transform, misalnya rotate(-2deg), :hover harus menulis",
                    "     keduanya: translateY(-3px) rotate(-2deg). transform di dua aturan",
                    "     nggak bertumpuk.",
                ]
            },
        ],
    },
    {
        "title": "12. Memotong dan Membungkus Teks",
        "sections": [
            {
                "body": [
                    "Judul kartu yang kepanjangan itu masalah sehari-hari. CSS bisa",
                    "memotongnya dan menaruh titik-titik di ujungnya sendiri. Tapi nggak",
                    "cukup satu properti. Kamu butuh tiga, dan ketiganya harus ada",
                    "bareng-bareng:",
                    "",
                    "  .judul {",
                    "    white-space: nowrap;      /* 1. larang teksnya turun baris   */",
                    "    overflow: hidden;         /* 2. potong yang keluar kotak     */",
                    "    text-overflow: ellipsis;  /* 3. gambar ... di ujung potongan */",
                    "  }",
                    "",
                    "Tiap properti mengerjakan langkah yang beda. text-overflow malah yang",
                    "paling lemah di antara ketiganya, karena dia nggak memotong apa pun.",
                    "Dia cuma menghias potongan yang udah dibuat dua properti sebelumnya.",
                    "",
                    "Kalau satu aja hilang, titik-titiknya nggak muncul sama sekali:",
                    "",
                    "  - Tanpa white-space: nowrap, teksnya turun baris seperti biasa.",
                    "    Nggak ada yang meluber ke samping, jadi nggak ada yang perlu",
                    "    dipotong, dan nggak ada tempat buat menaruh titik-titiknya.",
                    "  - Tanpa overflow: hidden, kelebihannya tetap tergambar keluar kotak",
                    "    apa adanya. Itu overflow: visible, yang udah kamu lihat di",
                    "    \"Display dan Alur Dokumen\". Nggak ada yang disembunyikan, jadi",
                    "    nggak ada yang perlu ditandai.",
                    "  - Tanpa text-overflow: ellipsis, teksnya terpotong tepat di tengah",
                    "    huruf tanpa tanda apa pun. Pembaca nggak punya cara buat tahu",
                    "    bahwa masih ada lanjutannya.",
                    "",
                    "Ada satu syarat lagi yang nggak kelihatan di tiga baris itu: elemennya",
                    "harus punya batas lebar. Kotak yang bebas melebar mengikuti isinya",
                    "nggak pernah kepenuhan, jadi nggak pernah ada yang meluber.",
                    "",
                    "Ini penyebab paling sering dari keluhan \"ketiganya udah kutulis, kok",
                    "titiknya nggak muncul\". Judulnya duduk di dalam item flex atau sel",
                    "grid yang ikut melebar mengikuti isinya. Gejala ini nanti dibahas",
                    "juga di materi Flexbox dan Grid. Obatnya min-width: 0, dipasang di elemen yang",
                    "tepat. Bagian terakhir materi ini nunjukin elemen yang mana.",
                ],
            },
            {
                "body": [
                    "Memotong di baris ke-N",
                    "",
                    "Trio tadi cuma bisa untuk satu baris. Untuk ringkasan kartu, biasanya",
                    "yang kamu mau \"tampilkan dua baris, sisanya titik-titik\". Resepnya",
                    "empat properti, dan bentuknya memang aneh:",
                    "",
                    "  .ringkasan {",
                    "    display: -webkit-box;",
                    "    -webkit-box-orient: vertical;",
                    "    -webkit-line-clamp: 2;",
                    "    overflow: hidden;",
                    "  }",
                    "",
                    "Awalan -webkit- itu bukan salah ketik, dan artinya juga bukan \"khusus",
                    "Safari\". Ini sisa rancangan flexbox lama yang udah lama ditinggalkan.",
                    "Masalahnya, rancangan itu telanjur dipakai di mana-mana, jadi Chrome,",
                    "Firefox, Safari, dan Edge semuanya tetap mendukungnya sampai sekarang.",
                    "Soal awalan vendor secara umum dibahas di materi \"CSS yang Bertahan\".",
                    "",
                    "Tugas tiap barisnya:",
                    "  display: -webkit-box     menyalakan model kotak lama itu;",
                    "                           tanpa ini clamp diabaikan",
                    "  -webkit-box-orient       harus vertical, supaya barisnya disusun",
                    "                           menurun",
                    "  -webkit-line-clamp: 2    berapa baris yang boleh terlihat",
                    "  overflow: hidden         membuang baris ketiga dan seterusnya",
                    "",
                    "Keempatnya wajib. Kalau display: -webkit-box atau -webkit-box-orient",
                    "dihapus, clamp-nya diabaikan tanpa pesan, dan paragrafnya tampil utuh",
                    "seolah nggak pernah kamu atur.",
                    "",
                    "Kalau overflow: hidden yang dihapus, hasilnya lebih parah. Kotaknya",
                    "memang menyusut jadi dua baris dan titik-titiknya tetap tergambar.",
                    "Tapi baris sisanya ikut tergambar juga, menimpa apa pun yang ada di",
                    "bawahnya. Yang kelihatan teks bertumpuk, nggak ada potongan rapi.",
                    "",
                    "Ada dua jebakan yang pasti kejadian begitu kamu menggabungkan dua",
                    "resep di halaman ini:",
                    "",
                    "  1. Nggak usah menambah white-space: nowrap di elemen yang pakai",
                    "     line-clamp. nowrap memaksa seluruh teks jadi satu baris, jadi",
                    "     \"potong di baris kedua\" nggak pernah kesampaian. Yang kelihatan",
                    "     cuma satu baris yang terpotong.",
                    "  2. line-clamp menghitung baris, bukan huruf. Kartu yang lebih",
                    "     sempit atau font yang lebih besar mengubah berapa banyak kata",
                    "     yang kelihatan. Memang begitu tujuannya, tapi jangan berharap",
                    "     dua kartu yang bersebelahan terpotong di kata yang sama.",
                    "",
                    "Kalau kamu nggak mau bergantung pada awalan sama sekali, ada cara",
                    "kasar yang selalu jalan: kunci aja tingginya.",
                    "",
                    "  .ringkasan {",
                    "    line-height: 1.5;",
                    "    max-height: 3em;     /* 2 x 1.5em */",
                    "    overflow: hidden;",
                    "  }",
                    "",
                    "Harganya perlu kamu terima: nggak ada titik-titik, dan baris",
                    "berikutnya bisa terpotong separuh tingginya, sehingga kelihatan kayak",
                    "huruf yang digunting.",
                    "",
                    "Bentuk tanpa awalan, line-clamp, lagi dalam proses dibakukan. Selama",
                    "belum jalan di semua browser, bentuk -webkit- di atas yang aman. Bentuk",
                    "itu juga yang bakal kamu temui di kode orang lain.",
                ],
            },
            {
                "body": [
                    "Nilai white-space selengkapnya",
                    "",
                    "Properti ini ngatur dua hal sekaligus. Pertama, apakah spasi berlebih",
                    "di HTML diciutkan. Kedua, apakah teks boleh turun baris sendiri kalau",
                    "kepanjangan.",
                    "",
                    "  normal        spasi & ganti baris diciutkan jadi satu spasi;",
                    "                teks turun baris sendiri kalau kepanjangan (bawaan)",
                    "  nowrap        spasi diciutkan, TAPI teks tidak pernah turun baris",
                    "                sendiri",
                    "  pre           spasi & ganti baris dipertahankan apa adanya;",
                    "                tidak turun sendiri",
                    "  pre-wrap      spasi & ganti baris dipertahankan, DAN masih turun",
                    "                baris sendiri",
                    "  pre-line      ganti baris dipertahankan, spasi berlebih tetap",
                    "                diciutkan",
                    "  break-spaces  seperti pre-wrap, spasi di ujung baris pun ikut",
                    "                dipertahankan",
                    "",
                    "Elemen <pre> pakai white-space: pre secara bawaan. Makanya satu baris",
                    "kode yang panjang bisa melebar keluar layar. Ada dua jalan keluar, dan",
                    "dua-duanya sah:",
                    "",
                    "  - Biarkan pre, lalu kasih wadahnya overflow-x: auto. Kodenya tetap",
                    "    utuh, tinggal digeser ke samping. Pola ini udah dipakai di",
                    "    \"Display dan Alur Dokumen\".",
                    "  - Ganti ke pre-wrap. Nggak ada yang perlu digeser, tapi satu baris",
                    "    kode yang panjang bakal kelihatan seperti dua baris, dan itu bisa",
                    "    menyesatkan pembacanya.",
                    "",
                    "Jebakan: white-space menurun ke seluruh keturunannya (lihat \"Teks dan",
                    "Font\"). Kalau kamu memasang nowrap di sebuah wadah, semua teks di",
                    "dalamnya ikut nolak turun baris, nggak cuma judulnya. Halaman yang",
                    "tiba-tiba bisa digeser ke samping sering berasal dari satu nowrap yang",
                    "dipasang terlalu tinggi.",
                    "",
                    "Tiga cara mematahkan kata yang panjang",
                    "",
                    "URL, token, atau nama berkas tanpa spasi nggak bisa diturunkan browser,",
                    "karena nggak ada satu pun tempat yang boleh dipatahkan. Satu kata",
                    "kayak gitu di kartu sempit bakal menjebol kartunya, dan sering bikin",
                    "seluruh halaman bisa digeser ke samping. Gejala ini nanti muncul lagi",
                    "di materi Flexbox dan Grid. Obatnya di bawah ini.",
                    "",
                    "  overflow-wrap: break-word",
                    "      Patahkan di tengah kata HANYA kalau kata itu tidak muat",
                    "      sendirian di satu baris. Kata biasa tidak tersentuh. Ini",
                    "      pilihan bawaan untuk hampir semua kasus, dan karena ia",
                    "      menular, cukup dipasang sekali di wadah teksnya.",
                    "  word-break: break-all",
                    "      Patahkan di huruf mana saja begitu barisnya penuh, untuk",
                    "      SEMUA kata. Teks Indonesia jadi tercabik-cabik di tempat yang",
                    "      tidak masuk akal. Hampir tidak pernah ini yang kamu maksud.",
                    "  hyphens: auto",
                    "      Patahkan di batas suku kata dan tambahkan tanda hubung. Butuh",
                    "      atribut lang di HTML (<html lang=\"id\">) supaya browser tahu",
                    "      kamus mana yang dipakai - dan kamusnya tidak tersedia untuk",
                    "      semua bahasa. Anggap hiasan, bukan obat: URL panjang tidak",
                    "      tertolong olehnya sama sekali.",
                    "",
                    "Nama lama overflow-wrap adalah word-wrap: break-word. Artinya persis",
                    "sama, dan masih sering kelihatan di kode lama. Kalau ketemu, itu",
                    "properti yang sama.",
                    "",
                    "Ada saudaranya yang lebih galak: overflow-wrap: anywhere. Bedanya",
                    "kecil tapi penting. Cuma anywhere yang ikut mengecilkan lebar minimum",
                    "elemennya. Dengan break-word, sebuah kolom grid, item flex, atau kolom",
                    "tabel bisa telanjur dijatah selebar kata terpanjang sebelum",
                    "pemotongannya sempat berlaku, jadi tata letaknya tetap melebar.",
                    "",
                    "Jadi kalau break-word kerasa nggak ngaruh di dalam grid atau tabel,",
                    "pasangkan dengan min-width: 0 di selnya, atau ganti ke anywhere.",
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
                    "Membaca ulang contoh di atas",
                    "",
                    "min-width: 0 dipasang di .kartu-teks, nggak di judulnya. Bagian ini",
                    "yang paling perlu dipahami pelan-pelan.",
                    "",
                    "Item flex punya batas menyusut otomatis selebar isi terlebarnya.",
                    "Batas itu cuma berlaku selama overflow-nya masih visible. Kalau",
                    "judulnya sendiri yang jadi item flex, dia nggak butuh min-width: 0,",
                    "karena overflow-nya udah hidden. Tapi item flex di sini pembungkusnya,",
                    ".kartu-teks. overflow pembungkus itu visible, dan isinya satu baris",
                    "panjang yang nolak dipatahkan. Jadi tanpa min-width: 0, pembungkus",
                    "itulah yang memaksa baris kepala melebar. Akibatnya judulnya nggak",
                    "pernah terpotong, dan lencananya terdorong keluar kartu. Aturan yang",
                    "sama berlaku untuk sel grid.",
                    "",
                    "flex: none di .lencana: lencana yang ikut menyusut bakal kehilangan",
                    "tulisannya sendiri. Dalam satu baris, tentukan siapa yang boleh",
                    "mengalah. Di contoh ini yang mengalah kolom teksnya.",
                    "",
                    "table-layout: fixed di .tabel: biasanya lebar kolom tabel ditentukan",
                    "oleh isinya. Satu URL panjang di satu sel melebarkan kolomnya duluan,",
                    "jadi aturan pemotongan apa pun yang kamu tulis nggak pernah kena.",
                    "Dengan fixed, CSS yang menentukan lebarnya duluan, dan isinya yang",
                    "menyesuaikan.",
                    "",
                    "Batas kemampuan text-overflow, supaya nggak kamu cari-cari",
                    "",
                    "  - Cuma untuk teks satu baris yang meluber. Di paragraf yang turun",
                    "    baris, dia nggak ngapa-ngapain. Untuk banyak baris, pakai",
                    "    line-clamp.",
                    "  - Nggak bisa memotong di tengah teks, dan nggak bisa disuruh",
                    "    \"ambil 40 karakter pertama\". Berapa huruf yang muat ditentukan",
                    "    browser, bukan kamu. Kalau butuh jumlah karakter yang pasti, itu",
                    "    tugas JavaScript atau server.",
                    "  - Syaratnya overflow yang nilainya selain visible, nggak harus",
                    "    persis hidden. auto dan scroll juga menghasilkan titik-titik.",
                    "    Tapi kotaknya sekalian jadi bisa digulir, dan menggulirnya nggak",
                    "    menampakkan sisa teksnya, karena yang digambar memang cuma sampai",
                    "    titik-titik itu. Untuk judul, yang kamu mau hidden.",
                    "  - Yang dapat titik-titik adalah elemen yang memuat teksnya. Kalau",
                    "    ketiganya kamu pasang di .kartu, padahal judulnya ada di dalam",
                    "    <h3> di dalamnya, nggak ada efeknya. Yang meluber itu <h3>, jadi",
                    "    <h3> yang harus dikasih ketiga properti itu.",
                    "",
                    "Terakhir, soal orang yang membaca. Teks yang dipotong CSS tetap utuh",
                    "di HTML-nya. Teksnya masih bisa disalin dan tetap dibacakan pembaca",
                    "layar. Yang hilang cuma tampilannya. Karena itu, pasang title=\"judul",
                    "lengkapnya\" di elemen yang dipotong, supaya pengguna tetikus bisa",
                    "melihat judul lengkapnya. Dan jangan memotong satu-satunya tempat",
                    "sebuah informasi muncul di halaman.",
                    "",
                    "Urutan ngecek kalau titiknya nggak muncul:",
                    "  1. Teksnya memang lebih panjang dari kotaknya?",
                    "  2. Ada white-space: nowrap? (untuk versi satu baris)",
                    "  3. overflow-nya hidden, bukan visible?",
                    "  4. Kotaknya punya batas lebar? Pembungkus di dalam flex atau grid",
                    "     butuh min-width: 0, sel tabel butuh table-layout: fixed.",
                    "  5. Ketiganya dipasang di elemen yang memuat teksnya, bukan di",
                    "     wadahnya?",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Nama produk di marketplace sering panjang sekali, misalnya \"Kemeja",
                    "Batik Pria Lengan Panjang Motif Parang Slim Fit\". Di layar ponsel",
                    "kartunya sempit, jadi namanya dipotong di baris kedua dengan",
                    "titik-titik. Nomor resi dan kode pesanan yang panjang tanpa",
                    "spasi juga harus boleh patah supaya nggak menjebol kartunya.",
                    "",
                    "Kasus kecil: di dasbor penjual versi ponsel, tiap kartu pesanan",
                    "selebar 160px berisi nama produk (bisa sampai 70 huruf) dan nomor",
                    "resi 22 karakter tanpa spasi. Nama harus berhenti di baris kedua",
                    "dengan \"...\", dan nomor resi nggak boleh melewati tepi kartu.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pisahkan dua masalahnya. Nama butuh dipotong per baris, nomor",
                    "     resi butuh izin untuk patah.",
                    "  2. Nama: pakai resep empat baris, dan keempatnya wajib ada:",
                    "      .nama-produk {",
                    "        display: -webkit-box;",
                    "        -webkit-box-orient: vertical;",
                    "        -webkit-line-clamp: 2;",
                    "        overflow: hidden;",
                    "      }",
                    "  3. Nomor resi: pasang overflow-wrap: break-word di elemennya. Dia",
                    "     cuma mematahkan kata yang nggak muat sendirian di satu baris.",
                    "  4. Periksa kasus pinggir: jangan tambah white-space: nowrap ke nama",
                    "     produk, karena potongannya jadi tinggal satu baris. Pasang juga",
                    "     atribut title berisi nama lengkap, supaya bisa dibaca utuh.",
                ]
            },
        ],
    },
    {
        "title": "13. Flexbox",
        "sections": [
            {
                "body": [
                    "Flexbox menata anak-anak sebuah wadah dalam satu dimensi: satu baris",
                    "atau satu kolom. Kalau kamu butuh baris dan kolom sekaligus, itu",
                    "tugas Grid, yang dibahas di materi berikutnya.",
                    "",
                    "Semuanya dimulai dari satu baris di wadahnya, bukan di anaknya:",
                    "",
                    "  .wadah { display: flex; }",
                    "",
                    "Begitu baris itu ditulis, semua anak langsung .wadah jadi flex item",
                    "dan berjajar mendatar. Cucunya nggak ikut. Flex cuma berlaku satu",
                    "tingkat ke bawah.",
                    "",
                    "Dua sumbu, dan ini bagian yang paling bikin bingung",
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
                    "Artinya, begitu kamu nulis flex-direction: column, justify-content",
                    "mendadak ngatur atas-bawah, dan align-items ngatur kiri-kanan.",
                    "Propertinya tetap sama, sumbunya yang berputar. Kalau sebuah aturan",
                    "flex kerasa kebalik, hampir selalu ini penyebabnya.",
                ]
            },
            {
                "body": [
                    "Properti di wadah:",
                    "  display: flex;",
                    "  flex-direction: row | row-reverse | column | column-reverse;",
                    "  justify-content: flex-start | center | flex-end |",
                    "                   space-between | space-around | space-evenly;",
                    "  align-items: stretch | flex-start | center | flex-end | baseline;",
                    "  flex-wrap: nowrap | wrap;",
                    "  gap: 16px;   jarak antar item, tanpa margin sama sekali",
                    "",
                    "Bawaan align-items adalah stretch. Makanya kartu-kartu dalam satu",
                    "baris flex otomatis sama tinggi tanpa kamu minta.",
                    "",
                    "Properti di item:",
                    "  flex-grow: 1;     boleh melar mengisi sisa ruang (bawaan 0)",
                    "  flex-shrink: 1;   boleh menyusut kalau ruang kurang (bawaan 1)",
                    "  flex-basis: auto; ukuran awal sebelum melar atau menyusut",
                    "  flex: 1;          ringkas dari '1 1 0' - bagi rata sisa ruangnya",
                    "  align-self: center;  menimpa align-items untuk satu item saja",
                    "  order: 2;         mengubah urutan tampilan",
                    "",
                    "Hati-hati dengan order. Urutan baca, yang dipakai pembaca layar dan",
                    "tombol Tab, tetap mengikuti HTML. Kalau tampilannya berurutan 1-2-3",
                    "tapi Tab-nya melompat 1-3-2, orang yang nggak pakai tetikus jadi",
                    "bingung. Kalau urutannya penting, ubah HTML-nya.",
                    "",
                    "Untuk jarak antar item, pakai gap, jangan margin. Kalau pakai margin,",
                    "kamu harus menghapusnya lagi di item terakhir (:last-child) supaya",
                    "nggak ada jarak yang menggantung di ujung. gap nggak pernah menaruh",
                    "jarak di ujung sama sekali.",
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
                    "Tiga bagian contoh di atas yang perlu kamu hafal:",
                    "",
                    "  1. justify-content: space-between",
                    "     Item pertama nempel di kiri, item terakhir nempel di kanan, dan",
                    "     sisanya dibagi rata di tengah. Ini cara bikin bilah kepala tanpa",
                    "     satu pun angka lebar.",
                    "  2. margin-top: auto di item flex",
                    "     Nilai auto menyerap semua sisa ruang di sisi itu. Jadi tombolnya",
                    "     terdorong ke dasar kartu, berapa pun panjang teks di atasnya.",
                    "     Dengan cara yang sama, margin-left: auto mendorong satu item ke",
                    "     ujung kanan tanpa mengubah item lain.",
                    "  3. flex: 1 1 260px",
                    "     Bacanya: boleh melar, boleh menyusut, dan mulai dari 260px.",
                    "     Digabung dengan flex-wrap: wrap, kartu-kartu itu menata dirinya",
                    "     sendiri di lebar layar berapa pun.",
                    "",
                    "Dua jebakan yang pasti kamu temui",
                    "",
                    "Pertama, bawaan flex-wrap adalah nowrap. Artinya item bakal terus",
                    "menyusut, bukannya turun ke baris berikutnya. Di layar sempit,",
                    "deretan kartu jadi gepeng sampai nggak kebaca. Hampir semua deretan",
                    "kartu sebaiknya pakai flex-wrap: wrap.",
                    "",
                    "Kedua, flex item otomatis punya min-width: auto, tanpa kamu tulis.",
                    "Artinya \"jangan menyusut lebih kecil dari isi terlebarnya\". Satu blok",
                    "kode panjang atau satu kata yang nggak bisa dipotong di dalam item",
                    "bisa bikin seluruh baris, bahkan seluruh halaman, melebar keluar",
                    "layar. Obatnya min-width: 0 di itemnya. Makanya baris itu ada di",
                    "contoh, walaupun kelihatannya nggak ngapa-ngapain.",
                    "",
                    "Ada obat kedua untuk sisi lain dari masalah yang sama:",
                    "overflow-wrap: break-word di teksnya. min-width: 0 mengizinkan item",
                    "menyusut lebih sempit dari isinya. overflow-wrap mengizinkan katanya",
                    "dipatahkan, supaya isinya sendiri jadi lebih sempit. Untuk satu kata",
                    "yang panjang banget atau satu URL tanpa spasi, biasanya kamu butuh",
                    "dua-duanya. Kenapa break-word kadang kerasa nggak ngaruh di dalam",
                    "flex, itu dibahas di materi Memotong dan Membungkus Teks.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Bilah atas toko online (logo di kiri, ikon keranjang di kanan),",
                    "deretan pilihan paket, dan tombol yang selalu duduk di dasar kartu",
                    "dibuat dengan flexbox. Komponen yang isinya berjajar dalam satu arah",
                    "hampir selalu ditata dengan display: flex.",
                    "",
                    "Kasus kecil: halaman paket kuota menampilkan tiga kartu: 10 GB,",
                    "25 GB, dan 50 GB. Deskripsinya beda panjang, jadi tombol \"Pilih",
                    "paket\" ada di ketinggian yang beda-beda. Desainnya minta tombol",
                    "sejajar di dasar kartu, dan kartu turun ke baris baru di ponsel.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pecah jadi dua tingkat: wadah yang membariskan kartu, dan tiap",
                    "     kartu yang menyusun isinya menurun.",
                    "  2. Wadah: flex dengan wrap dan gap. Kartu dalam satu baris otomatis",
                    "     sama tinggi, karena align-items bawaannya stretch.",
                    "  3. Kartu: jadikan flex menurun, lalu margin-top: auto mendorong",
                    "     tombolnya ke dasar:",
                    "      .daftar-paket { display: flex; flex-wrap: wrap; gap: 16px; }",
                    "      .paket { flex: 1 1 220px; display: flex; flex-direction: column; }",
                    "      .paket .tombol { margin-top: auto; }",
                    "  4. Periksa kasus pinggir: tanpa flex-wrap: wrap, di layar 360px",
                    "     ketiga kartu terus menyusut sampai teksnya berdesakan, dan nggak",
                    "     ada yang turun ke baris berikutnya.",
                ]
            },
        ],
    },
    {
        "title": "14. Grid",
        "sections": [
            {
                "body": [
                    "Grid menata dalam dua dimensi sekaligus: kolom dan baris. Aturannya",
                    "juga ditulis di wadah:",
                    "",
                    "  .wadah { display: grid; }",
                    "",
                    "Menentukan kolom:",
                    "  grid-template-columns: 200px 200px 200px;   tiga kolom tetap",
                    "  grid-template-columns: 1fr 1fr 1fr;         tiga kolom sama lebar",
                    "  grid-template-columns: repeat(3, 1fr);      sama, ditulis ringkas",
                    "  grid-template-columns: 240px 1fr;           sisi tetap + isi melar",
                    "",
                    "fr itu satuan khusus grid, artinya \"satu bagian dari sisa ruang\".",
                    "Pada 2fr 1fr, kolom pertama dua kali lebar kolom kedua. Sisa ruangnya",
                    "dihitung sesudah gap dan kolom berukuran tetap dipotong duluan.",
                    "",
                    "Karena yang dibagi cuma sisa ruang, fr nggak pernah bikin grid",
                    "meluber. Beda dengan 33.33% tiga kali ditambah gap, yang pasti",
                    "meluber.",
                    "",
                    "  gap: 20px;              jarak antar sel",
                    "  row-gap / column-gap    kalau baris dan kolom perlu beda",
                    "",
                    "Biasanya baris nggak perlu ditentukan. Grid bikin sendiri sesuai",
                    "jumlah item. Kalau memang perlu:",
                    "  grid-template-rows: auto 1fr auto;   kepala, isi melar, kaki",
                ]
            },
            {
                "body": [
                    "Menempatkan item",
                    "",
                    "  .lebar  { grid-column: span 2; }   ambil dua kolom",
                    "  .utama  { grid-column: 1 / 3; }    dari garis 1 sampai garis 3",
                    "  .tinggi { grid-row: span 2; }      ambil dua baris",
                    "",
                    "Perhatikan: yang dihitung itu garis, bukan kolom. Tiga kolom punya",
                    "empat garis:",
                    "",
                    "  1     2     3     4",
                    "  |-----|-----|-----|",
                    "  | k1  | k2  | k3  |",
                    "  |-----|-----|-----|",
                    "",
                    "Jadi grid-column: 1 / 3 artinya dari garis 1 sampai garis 3, yaitu",
                    "dua kolom, bukan tiga. Ini salah hitung yang paling sering di grid.",
                    "Kalau bingung, pakai bentuk span 2, yang nggak perlu ngitung garis",
                    "sama sekali.",
                    "",
                    "  grid-column: 1 / -1;   dari garis pertama sampai garis TERAKHIR,",
                    "                         berapa pun jumlah kolomnya",
                    "",
                    "Responsif tanpa satu pun media query",
                    "",
                    "  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));",
                    "",
                    "Bacanya: bikin kolom sebanyak mungkin. Tiap kolom minimal 240px dan",
                    "maksimal satu bagian sisa ruang. Layar lebar dapat empat kolom,",
                    "tablet dua, ponsel satu, dan semuanya diputuskan grid sendiri. Satu",
                    "baris ini menggantikan tiga blok @media.",
                    "",
                    "Beda auto-fit dan auto-fill kelihatan kalau itemnya sedikit. auto-fit",
                    "melebarkan item yang ada sampai penuh. auto-fill menyisakan kolom",
                    "kosong di kanan. Untuk daftar kartu biasa, yang kamu mau auto-fit.",
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
                    "grid-template-areas itu bagian CSS yang hampir nggak perlu dijelaskan,",
                    "karena tulisannya udah berbentuk gambar tata letaknya. Nama yang sama",
                    "diulang artinya daerah itu melebar. Titik (.) artinya sel kosong.",
                    "",
                    "Jebakan: tiap baris harus punya jumlah nama yang sama. Kalau nggak,",
                    "seluruh aturannya dibuang tanpa pesan apa pun, dan halamanmu",
                    "tiba-tiba balik menumpuk ke bawah.",
                    "",
                    "Untungnya paling kerasa di media query. Untuk mengubah seluruh tata",
                    "letak jadi satu kolom di ponsel, kamu cukup nulis ulang gambarnya.",
                    "Elemennya nggak perlu dipindah satu per satu.",
                    "",
                    "Grid atau flex?",
                    "",
                    "  - Menata kerangka halaman (kepala, sisi, isi, kaki): Grid.",
                    "  - Membariskan beberapa benda dalam satu baris atau kolom: Flex.",
                    "  - Peduli pada baris dan kolom sekaligus, dan pengin semuanya lurus",
                    "    ke bawah dan ke samping: Grid.",
                    "  - Jumlah itemnya berubah-ubah, dan kamu cuma pengin mereka rapi",
                    "    sebaris lalu turun sendiri: Flex.",
                    "",
                    "Pilihannya nggak harus satu untuk selamanya. Keduanya biasa",
                    "bersarang: grid untuk kerangka luar, flex untuk isi tiap sel. Susunan",
                    "itu yang paling sering dipakai di halaman sungguhan.",
                    "",
                    "Catatan: sel grid, sama seperti item flex, butuh min-width: 0 kalau",
                    "isinya bisa lebih lebar dari selnya. Tanpa itu, satu tabel lebar di",
                    "dalam .isi bisa melebarkan kolom 1fr sampai melewati layar, dan",
                    "seluruh halaman ikut bisa digeser.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Galeri foto kegiatan sekolah, daftar produk di toko online, dan",
                    "dasbor admin yang punya kepala, menu samping, isi, dan kaki halaman",
                    "biasanya ditata dengan grid. Grid dipilih kalau baris dan kolomnya",
                    "sama-sama harus lurus.",
                    "",
                    "Kasus kecil: galeri lomba 17 Agustus berisi 14 foto. Di laptop",
                    "fotonya harus berjajar empat kolom, di ponsel satu kolom, tanpa satu",
                    "pun media query. Foto juara umum dipasang paling atas dan selebar",
                    "seluruh baris.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pahami masukannya: jumlah foto dan lebar layar sama-sama",
                    "     berubah-ubah. Jadi biarkan grid yang menghitung jumlah kolomnya.",
                    "  2. Pakai auto-fit dengan batas bawah 200px:",
                    "      .galeri {",
                    "        display: grid;",
                    "        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));",
                    "        gap: 12px;",
                    "      }",
                    "      .galeri .juara { grid-column: 1 / -1; }",
                    "  3. Hitung satu contoh. Wadah 1000px muat empat kolom, karena",
                    "     4 x 200 + 3 x 12 = 836px. Lima kolom butuh 1048px, jadi nggak",
                    "     muat.",
                    "  4. Periksa kasus pinggir: foto juara ditulis 1 / -1, jangan 1 / 5.",
                    "     Nomor garis terakhir berubah tiap kali jumlah kolomnya berubah,",
                    "     dan -1 selalu menunjuk garis terakhir itu.",
                ]
            },
        ],
    },
    {
        "title": "15. Perataan Lanjut dan Grid Implisit",
        "sections": [
            {
                "body": [
                    "Materi Flexbox udah ngenalin justify-content dan align-items. Ada",
                    "saudara ketiga yang jarang disebut, padahal dia yang menjelaskan",
                    "salah satu kebingungan terbesar di flexbox: align-content.",
                    "",
                    "  align-items    mengatur letak item DI DALAM barisnya sendiri",
                    "  align-content  mengatur letak dan jarak ANTAR baris",
                    "",
                    "align-content baru ada artinya kalau barisnya lebih dari satu. Wadah",
                    "flex tanpa flex-wrap: wrap (dan nowrap itu bawaannya) selalu cuma",
                    "punya satu baris. Di situ align-content nggak ngapa-ngapain. Menulisnya",
                    "juga nggak error, nggak dicoret editor, nggak mengubah apa pun, dan",
                    "nggak ada yang ngasih tahu kamu.",
                    "",
                    "Kenapa align-items kerasa nggak mempan",
                    "",
                    "Hampir semua orang pernah ngalamin ini sekali:",
                    "",
                    "  .label {",
                    "    display: flex;",
                    "    flex-wrap: wrap;",
                    "    align-items: center;",
                    "    height: 200px;",
                    "  }",
                    "",
                    "Isinya terbungkus jadi tiga baris. Kamu berharap ketiganya menumpuk",
                    "rapi di tengah, tapi ternyata malah terpencar dengan celah lebar di",
                    "antaranya. align-items: center kelihatan seperti diabaikan.",
                    "",
                    "Dia nggak diabaikan kok. Dia ngerjain persis yang dijanjikan.",
                    "Nilai bawaan align-content di flex itu normal, yang di sini bekerja",
                    "sama seperti stretch. Jadi ketiga baris itu lebih dulu dimekarkan",
                    "sampai bertiga memenuhi tinggi wadah 200px. Sesudah itu baru",
                    "align-items memusatkan tiap item di dalam barisnya masing-masing, dan",
                    "barisnya memang udah setinggi 66px.",
                    "",
                    "Untuk merapatkan ketiganya, yang kamu cari align-content: center.",
                    "Atau align-content: flex-start kalau maunya menumpuk dari atas.",
                    "",
                    "Patokan praktisnya: begitu wadah flex punya flex-wrap: wrap dan",
                    "tingginya ditentukan, hampir pasti kamu butuh align-content juga.",
                ],
            },
            {
                "body": [
                    "Di grid ada tiga pasang",
                    "",
                    "Grid juga punya dua sumbu. Bedanya dengan flex, sumbu grid nggak ikut",
                    "berputar. Di grid, justify-* selalu mendatar dan align-* selalu",
                    "menurun, apa pun nilai grid-auto-flow-nya. Kebiasaan dari flexbox",
                    "(\"sumbunya berputar kalau column\") nggak berlaku di sini. Satu hal",
                    "lebih sedikit yang perlu kamu pikirkan.",
                    "",
                    "                   dipasang di   yang diatur",
                    "  justify-items     wadah         isi tiap sel, mendatar",
                    "  align-items       wadah         isi tiap sel, menurun",
                    "  justify-self      satu item     menimpa justify-items, satu item saja",
                    "  align-self        satu item     menimpa align-items, satu item saja",
                    "  justify-content   wadah         letak SELURUH kisi di wadahnya, mendatar",
                    "  align-content     wadah         letak SELURUH kisi di wadahnya, menurun",
                    "",
                    "Nilai untuk -items dan -self: start, end, center, stretch. Bawaannya",
                    "stretch. Makanya isi sebuah sel grid otomatis melar memenuhi selnya",
                    "tanpa kamu minta, persis seperti align-items: stretch di flex.",
                    "",
                    "Ada satu syarat yang gampang terlewat: stretch cuma bekerja kalau",
                    "itemnya belum punya ukuran sendiri. Begitu kamu nulis width: 40px di",
                    "item itu, nggak ada lagi yang bisa dimekarkan, dan stretch bekerja",
                    "seperti start tanpa bilang apa-apa. Jadi kalau kartumu nggak sama",
                    "tinggi padahal stretch itu bawaannya, cari height atau width yang",
                    "telanjur dipasang di kartunya.",
                    "",
                    "Nilai untuk -content: start, end, center, space-between,",
                    "space-around, space-evenly. Kosakatanya sama dengan justify-content",
                    "di flexbox.",
                    "",
                    "Yang paling sering ketuker: -items dan -content",
                    "",
                    "  justify-items: center     tiap isi sel duduk di tengah SELNYA",
                    "  justify-content: center   seluruh kisinya duduk di tengah WADAHNYA",
                    "",
                    "Karena itu justify-content sering kerasa mati di grid. Kalau",
                    "kolomnya kamu tulis 1fr, kolom-kolom itu udah menghabiskan seluruh",
                    "lebar wadahnya, jadi nggak ada sisa ruang untuk digeser ke mana pun.",
                    "justify-content baru kelihatan efeknya kalau kisinya lebih kecil dari",
                    "wadahnya, misalnya repeat(3, 120px) di dalam wadah selebar 600px.",
                    "",
                    "Hal yang sama berlaku untuk align-content dan tinggi. Kisi yang",
                    "tingginya cuma setinggi isinya nggak punya sisa ruang ke bawah, jadi",
                    "nggak ada yang bisa dipindah.",
                    "",
                    "Bentuk ringkas: align dulu, baru justify",
                    "",
                    "  place-items: center;       = align-items: center; justify-items: center;",
                    "  place-content: end center; = align-content: end; justify-content: center;",
                    "  place-self: stretch;       = align-self + justify-self, keduanya stretch",
                    "",
                    "Kalau cuma satu nilai, nilai itu dipakai untuk kedua sumbu. Urutannya",
                    "menurun dulu, baru mendatar. Ini kebalikan dari kebiasaan \"x lalu y\"",
                    "di hampir semua tempat lain, jadi memang gampang ketuker. Kalau ragu,",
                    "tulis versi panjangnya. Dua baris juga nggak salah.",
                    "",
                    "place-items: center di wadah display: grid adalah cara satu baris",
                    "untuk memusatkan apa pun, mendatar dan menurun sekaligus. Dia",
                    "menggantikan tiga baris flex yang kamu tulis di materi Flexbox",
                    "(display, justify-content, align-items). Makanya kamu bakal sering",
                    "melihatnya di kode orang lain, untuk wadah yang isinya cuma satu",
                    "benda.",
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
                    "Grid implisit",
                    "",
                    "Di materi Grid tertulis: \"biasanya baris nggak perlu ditentukan, grid",
                    "bikin sendiri\". Baris yang dibikin grid itu punya nama. Namanya perlu",
                    "kamu tahu, karena ada properti khusus untuk mengaturnya.",
                    "",
                    "  grid EKSPLISIT  jalur (track) yang KAMU tulis sendiri di",
                    "                  grid-template-columns, grid-template-rows, atau",
                    "                  grid-template-areas",
                    "  grid IMPLISIT   jalur yang DIBUAT grid sendiri karena masih ada item",
                    "                  yang belum kebagian tempat",
                    "",
                    "Jalur (track) artinya satu baris atau satu kolom di grid. Misalnya",
                    "kamu menulis tiga kolom, dan ada tujuh item di dalamnya. Grid lalu",
                    "bikin baris kedua dan ketiga sendiri. Karena kamu nggak nulis",
                    "grid-template-rows sama sekali, ketiga barisnya implisit, termasuk",
                    "baris pertama.",
                    "",
                    "Ukuran baris buatan: grid-auto-rows",
                    "",
                    "Bawaan ukuran jalur implisit adalah auto, artinya setinggi isi",
                    "tertinggi di baris itu. Makanya galeri kartu sering kelihatan",
                    "bergelombang. Baris pertama tinggi karena ada satu kartu berteks",
                    "panjang, baris kedua pendek, dan nggak ada satu angka pun di CSS-mu",
                    "yang menyebabkannya.",
                    "",
                    "  grid-auto-rows: 180px;                semua baris buatan tepat 180px",
                    "  grid-auto-rows: minmax(120px, auto);  minimal 120px, dan boleh lebih",
                    "                                        kalau isinya memang lebih tinggi",
                    "",
                    "Bentuk minmax itu yang paling sering kamu mau. Rapinya seperti ukuran",
                    "tetap, tapi nggak pernah memotong isi yang kepanjangan.",
                    "",
                    "grid-auto-rows nggak menyentuh baris yang udah kamu tulis di",
                    "grid-template-rows. Keduanya bisa dipakai bareng: dua baris pertama",
                    "kamu atur sendiri, sisanya diserahkan ke grid-auto-rows.",
                    "",
                    "Pasangannya grid-auto-columns. Properti ini jarang dipakai, karena",
                    "kolom biasanya eksplisit. Dia baru berguna kalau arah alirannya kamu",
                    "balik.",
                    "",
                    "Arah pengisian: grid-auto-flow",
                    "",
                    "  row (bawaan)  isi kiri ke kanan; kalau penuh, buat BARIS baru",
                    "  column        isi atas ke bawah; kalau penuh, buat KOLOM baru",
                    "  dense         boleh mundur mengisi lubang yang telanjur ditinggalkan",
                    "",
                    "dense nggak menggantikan arah. Dia ditambahkan di belakangnya:",
                    "grid-auto-flow: row dense.",
                    "",
                    "Lubang yang dimaksud muncul kalau ada item yang lebih lebar dari sisa",
                    "barisnya. Bayangin kisi tiga kolom, dan item ketiga pakai grid-column:",
                    "span 2. Item itu nggak muat di sisa satu kolom, jadi dia turun ke",
                    "baris berikutnya dan meninggalkan satu sel kosong. Tanpa dense, sel",
                    "itu kosong terus, karena cara pengisian bawaannya nggak pernah balik",
                    "ke belakang.",
                    "",
                    "Dengan dense, item berikutnya yang cukup kecil ditarik maju untuk",
                    "mengisi lubang tadi. Kisimu jadi padat. Akibatnya, urutan yang",
                    "kelihatan di layar nggak sama lagi dengan urutan di HTML.",
                    "",
                    "Jebakan: ini persis masalah order di materi Flexbox. Urutan Tab dan",
                    "urutan yang dibacakan pembaca layar tetap mengikuti HTML, bukan yang",
                    "di layar. Untuk galeri gambar itu nggak masalah. Untuk daftar langkah",
                    "1-2-3 atau deretan tombol, jangan pakai dense.",
                    "",
                    "Satu lagi yang sering nggak disadari: nomor garis negatif cuma kenal",
                    "jalur eksplisit. grid-column: 1 / -1 dari materi Grid bekerja karena",
                    "kolomnya kamu tulis sendiri. Tapi grid-row: 1 / -1 di kisi yang",
                    "barisnya implisit nggak menjangkau baris terakhir, karena buat grid",
                    "jumlah baris eksplisitnya nol.",
                ],
            },
            {
                "heading": "Galeri padat dan papan yang mengalir ke samping",
                "body": [
                    "Dua pola di bawah memakai semuanya sekaligus. Yang pertama galeri.",
                    "Kolomnya menata diri sendiri, barisnya dibikin grid lalu dikasih",
                    "ukuran lewat grid-auto-rows, dan lubang yang ditinggalkan kartu besar",
                    "ditutup pakai dense.",
                    "",
                    "Yang kedua membalik arah aliran. Item mengalir ke kanan, dan yang",
                    "dibikin grid adalah kolom, bukan baris. Di sini grid-auto-columns",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Daftar kelas bimbel, papan menu kafe, dan galeri kartu lain sering",
                    "kelihatan bergelombang: satu baris tinggi, baris berikutnya pendek.",
                    "Penyebabnya baris yang dibuat grid sendiri, yang tingginya mengikuti",
                    "isi tertinggi. Mengatur baris implisit itu, dan membedakan -items",
                    "dari -content, jadi pekerjaan rutin waktu merapikan halaman seperti",
                    "ini.",
                    "",
                    "Kasus kecil: halaman bimbel menampilkan sembilan kartu kelas dalam",
                    "tiga kolom, tanpa grid-template-rows. Satu kartu berdeskripsi panjang",
                    "bikin baris pertama setinggi 260px, sedangkan baris kedua cuma 140px.",
                    "Desainnya minta tiap baris minimal 180px, dan boleh lebih tinggi",
                    "kalau isinya memang panjang.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pahami asal barisnya. Kamu nggak menulis baris apa pun, jadi",
                    "     ketiganya implisit, dan ukuran bawaannya auto: setinggi isi",
                    "     tertinggi di baris itu.",
                    "  2. Atur ukuran baris buatan lewat grid-auto-rows dengan minmax:",
                    "      .daftar-kelas {",
                    "        display: grid;",
                    "        grid-template-columns: repeat(3, 1fr);",
                    "        grid-auto-rows: minmax(180px, auto);",
                    "        gap: 16px;",
                    "      }",
                    "  3. Periksa kasus pinggir: kartu yang telanjur diberi height: 150px",
                    "     nggak ikut melar ke 180px. stretch cuma bekerja pada item yang",
                    "     belum punya ukuran sendiri, jadi hapus height di kartunya.",
                ]
            },
        ],
    },
    {
        "title": "16. Tata Letak Warisan: float, clear, dan flow-root",
        "sections": [
            {
                "body": [
                    "Materi ini membahas cara menata yang udah tua. Untuk halaman baru,",
                    "kamu hampir pasti nggak bakal memilihnya, karena flex dan grid jauh",
                    "lebih enak dipakai. Tapi kamu bakal sering membacanya di kode orang.",
                    "",
                    "Sebelum flexbox ada (sekitar tahun 2015), belum ada cara yang masuk",
                    "akal untuk bikin dua kolom bersebelahan. Orang pakai float, padahal",
                    "float dibuat untuk urusan lain: menyisipkan gambar di tengah artikel.",
                    "Selama sekitar sepuluh tahun, tata letak web dibangun pakai alat yang",
                    "dipinjam dari tujuan aslinya.",
                    "",
                    "Akibatnya, Bootstrap 3, tema WordPress, dan hampir semua berkas CSS",
                    "yang umurnya lebih dari beberapa tahun penuh dengan float: left.",
                    "Kalau kamu nggak ngerti float, kamu nggak bisa menyentuh berkas-berkas",
                    "itu tanpa merusaknya.",
                    "",
                    "Selain itu, float masih bisa melakukan sesuatu yang nggak bisa",
                    "dilakukan flex maupun grid. Makanya float belum pensiun.",
                    "",
                    "Apa yang dilakukan float",
                    "",
                    "  float: left;    kotaknya digeser menempel tepi KIRI wadahnya",
                    "  float: right;   digeser menempel tepi KANAN",
                    "  float: none;    bawaannya, tidak mengambang",
                    "",
                    "Elemen yang diberi float keluar dari alur dokumen, yaitu alur yang",
                    "dibahas di materi Display dan Alur Dokumen. Tapi keluarnya cuma",
                    "setengah, dan setengah itulah yang bikin float unik:",
                    "",
                    "  - Kotak blok yang datang sesudahnya bersikap seolah float itu nggak",
                    "    ada. Latar dan garis tepi kotak itu lewat di bawah float.",
                    "  - Tapi baris teks di dalam kotak-kotak itu tetap menghindar. Tiap",
                    "    baris dipendekkan supaya nggak menabrak float.",
                    "",
                    "Jadi yang mengalir mengelilingi float adalah baris teksnya, elemennya",
                    "sendiri nggak. Ini menjelaskan gejala yang bikin banyak orang bingung:",
                    "\"kenapa latar paragrafku masuk ke bawah gambar, padahal teksnya ada di",
                    "samping?\" Memang begitu cara kerjanya, dan itu bukan bug.",
                    "",
                    "Ada tiga efek samping yang jarang disebut:",
                    "  - float mengubah elemennya jadi blok. Sebuah <span> yang diberi",
                    "    float: left langsung bisa diberi width dan height, tanpa perlu",
                    "    display: inline-block.",
                    "  - Kalau nggak diberi width, elemen yang di-float menyusut sepas",
                    "    isinya. Beda dengan blok biasa yang memakan selebar wadahnya.",
                    "  - float diabaikan pada item flex dan item grid. Kalau induknya udah",
                    "    display: flex, nulis float: left di anaknya nggak ngaruh apa-apa.",
                ],
            },
            {
                "body": [
                    "Gejala paling umum: induk yang tingginya mendadak nol",
                    "",
                    "Tinggi sebuah kotak dihitung dari isi yang ada di dalam alur. Elemen",
                    "yang di-float udah keluar dari alur, jadi dia nggak ikut dihitung.",
                    "Kalau isi sebuah wadah cuma elemen yang di-float, tinggi wadah itu",
                    "jadi 0.",
                    "",
                    "  .wadah { background: #eee; border: 1px solid #ccc; }",
                    "  .wadah > .kolom { float: left; width: 33%; }",
                    "",
                    "Yang kamu lihat: garis tepi .wadah menyusut jadi satu garis tipis di",
                    "atas kolom-kolomnya. Latar abu-abunya hilang. Apa pun yang ditulis",
                    "sesudah .wadah naik dan menimpa kolom-kolom itu. Nggak ada error dan",
                    "nggak ada petunjuk. Ini kasus \"kartuku gepeng\" yang terkenal, dan",
                    "penyebabnya susah ditebak kalau belum pernah dikasih tahu.",
                    "",
                    "clear: jangan berdiri di samping float, turun dulu",
                    "",
                    "  clear: left;    turun sampai lewat semua float kiri",
                    "  clear: right;   turun sampai lewat semua float kanan",
                    "  clear: both;    lewat keduanya - ini yang hampir selalu dipakai",
                    "",
                    "clear dipasang di elemen yang nggak mau bersebelahan dengan float,",
                    "bukan di float-nya. Ada dua batasannya. clear cuma melihat float yang",
                    "ditulis sebelum dirinya. Dan clear nggak ngaruh pada elemen yang ikut",
                    "di-float.",
                    "",
                    "Clearfix: baris aneh di materi Pseudo-element akhirnya ada artinya",
                    "",
                    "  .wadah::after {",
                    "    content: \"\";",
                    "    display: block;",
                    "    clear: both;",
                    "  }",
                    "",
                    "Cara bacanya: tempelkan satu kotak kosong di ujung isi .wadah.",
                    "Jadikan kotak itu blok biasa yang ikut alur. Lalu suruh dia turun",
                    "melewati semua float. Karena kotak kosong itu ada di dalam alur,",
                    "tingginya ikut dihitung. Letaknya di bawah float, jadi .wadah terpaksa",
                    "cukup tinggi untuk membungkus float-nya.",
                    "",
                    "Tiga barisnya punya tugas masing-masing. Hapus satu aja, dan semuanya",
                    "berhenti bekerja:",
                    "  - Tanpa content, ::after nggak pernah muncul.",
                    "  - Tanpa display: block, kotaknya inline, dan clear nggak berlaku",
                    "    pada elemen inline.",
                    "  - Tanpa clear, nggak ada yang turun ke bawah float.",
                    "",
                    "Di kode lama kamu bakal ketemu versi yang lebih panjang: display:",
                    "table sebagai ganti block, ditambah baris zoom: 1 untuk Internet",
                    "Explorer 6 dan 7 yang udah lama nggak dipakai. Cukup kenali kalau",
                    "ketemu. Di kode baru nggak perlu ditulis lagi.",
                    "",
                    "display: flow-root, clearfix dalam satu baris",
                    "",
                    "  .wadah { display: flow-root; }",
                    "",
                    "Artinya: kotak ini memulai alurnya sendiri di dalam. Semua yang",
                    "terjadi di dalamnya, termasuk float, selesai di dalamnya juga.",
                    "Tingginya otomatis membungkus seluruh isinya. Nggak perlu",
                    "pseudo-element, nggak perlu content kosong.",
                    "",
                    "Bonusnya, flow-root sekaligus memutus margin collapse dari materi Box",
                    "Model. Margin anak pertama nggak lagi bocor keluar dan menggeser",
                    "induknya.",
                    "",
                    "Trik lama: overflow: hidden atau overflow: auto",
                    "",
                    "Dua-duanya juga membungkus float, karena dua-duanya juga memulai alur",
                    "baru di dalam. Bertahun-tahun ini jadi cara terpendek, jadi kamu bakal",
                    "sering ketemu. Tapi efek sampingnya nyata, dan susah dilacak karena",
                    "kelihatannya nggak berhubungan:",
                    "",
                    "  - overflow: hidden memotong apa pun yang keluar dari kotak:",
                    "    bayangan, menu tarik-turun, tooltip, atau tanda fokus yang sedikit",
                    "    melebar.",
                    "  - overflow: hidden juga mematikan position: sticky (materi Position)",
                    "    pada elemen di dalamnya.",
                    "  - overflow: auto bisa memunculkan bilah gulir yang nggak kamu minta.",
                    "",
                    "Patokannya gampang. Kalau kamu cuma perlu membungkus float, pakai",
                    "display: flow-root. Pakai overflow cuma kalau kamu memang mau",
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
                    "Nilai display yang belum pernah disebut",
                    "",
                    "Materi Display dan Alur Dokumen membahas block, inline, inline-block,",
                    "dan none. Materi Flexbox dan materi Grid menambah flex dan grid. Masih",
                    "ada satu baris lagi di tabel itu, dan baris ini yang paling sering",
                    "muncul di komponen sungguhan:",
                    "",
                    "  display: inline-flex   isinya ditata seperti flex, TAPI wadahnya sendiri",
                    "                         tetap mengalir dalam baris teks dan selebar isinya",
                    "  display: inline-grid   hal yang sama untuk grid",
                    "",
                    "Bedanya dengan display: flex cuma satu, dan itu soal wadahnya, isinya",
                    "sama aja. display: flex bikin wadahnya jadi blok, dan blok memakan",
                    "seluruh lebar yang tersedia. Tombol sering kena jebakan ini:",
                    "",
                    "  .tombol { display: flex; align-items: center; gap: 8px; }",
                    "",
                    "Ikon dan teksnya memang jadi sejajar rapi. Tapi tombolnya mendadak",
                    "selebar layar, dan kamu nyari-nyari width yang nggak pernah kamu tulis.",
                    "Yang kamu perlukan di sini adalah inline-flex. Isinya tetap ditata pakai flex,",
                    "tombolnya tetap sepas isinya, dan tetap bisa berdiri di tengah kalimat.",
                    "",
                    "Bentuk ini yang paling umum untuk tombol berikon, lencana angka, dan",
                    "chip. Ia gabungan dua hal yang selama ini terpisah: inline-block dari",
                    "materi Display dan Alur Dokumen, dan flex dari materi Flexbox.",
                    "",
                    "Karena wadahnya inline, ia ikut aturan teks. Celah sekitar 4px di",
                    "antara elemen inline, yang dibahas di materi Display, juga muncul di",
                    "sini. Perlakukan aja seperti inline-block.",
                    "",
                    "display: contents, sekilas aja",
                    "",
                    "Kotak elemennya dihapus, dan anak-anaknya naik menggantikan posisinya.",
                    "Gunanya saat sebuah <div> pembungkus menghalangi anak-anaknya jadi",
                    "item grid langsung dari kakeknya.",
                    "",
                    "Ada dua hal yang perlu kamu tahu sebelum memakainya. Pertama,",
                    "background, border, dan padding elemen itu ikut hilang, karena kotaknya",
                    "memang udah nggak ada. Kedua, pada elemen yang punya arti seperti <ul>",
                    "atau <table>, display: contents bisa merusak cara pembaca layar",
                    "membacanya. Cukup kenali kalau ketemu, dan pakai seperlunya.",
                ],
            },
            {
                "heading": "Dua tempat float masih menang, plus tombol inline-flex (gaya.css)",
                "body": [
                    "Kapan float masih jadi pilihan yang tepat sekarang? Cuma dua:",
                    "",
                    "  1. Gambar yang dikelilingi teks di dalam artikel. Flex dan grid",
                    "     menaruh gambar dan teks di dua sel terpisah, jadi teksnya nggak",
                    "     bakal pernah melipat di bawah gambar. Cuma float yang memendekkan",
                    "     baris teks.",
                    "  2. Huruf besar di awal artikel (drop cap). Cara kerjanya sama: satu",
                    "     huruf di-float, dan beberapa baris pertama mengelilinginya.",
                    "",
                    "Kalau kamu mau teksnya mengalir mengikuti bentuk yang bukan kotak,",
                    "ada shape-outside: circle(50%). Properti itu cuma bekerja pada elemen",
                    "yang di-float. Ini satu bukti lagi bahwa untuk urusan ini float belum",
                    "ada gantinya.",
                    "",
                    "Di luar dua hal itu, pakai flex atau grid.",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Situs berita desa, blog lama, dan tema WordPress yang umurnya",
                    "bertahun-tahun masih penuh float. Kalau kamu PKL di tempat yang",
                    "merawat situs seperti itu, tugas pertamamu bisa jadi membetulkan",
                    "kotak yang tingginya mendadak nol, tanpa merombak seluruh berkas.",
                    "",
                    "Kasus kecil: di situs desa, tiap berita punya foto dengan float: left",
                    "dan lebar 200px. Beritanya pendek, jadi kotak berita berlatar abu-abu",
                    "berhenti sebelum fotonya selesai, dan berita berikutnya naik ke",
                    "samping foto.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pahami penyebabnya: foto yang di-float keluar dari alur, jadi",
                    "     nggak ikut dihitung waktu tinggi kotak berita ditentukan.",
                    "  2. Bungkus float-nya dengan display: flow-root di kotak berita:",
                    "      .berita { display: flow-root; background: #f2f2f0; }",
                    "      .berita .foto { float: left; width: 200px; margin: 0 16px 8px 0; }",
                    "  3. Jangan pakai overflow: hidden untuk tujuan yang sama. Cara itu",
                    "     ikut memotong bayangan dan apa pun yang sedikit keluar kotak.",
                    "  4. Periksa kasus pinggir: jangan \"merapikan\" dengan menggantinya",
                    "     jadi flex. Teks berita nggak bakal lagi mengalir ke bawah foto,",
                    "     dan itu salah satu dari dua kegunaan float yang masih tersisa.",
                ]
            },
        ],
    },
    {
        "title": "17. Position: static, relative, absolute, fixed, sticky",
        "sections": [
            {
                "body": [
                    "position menjawab dua hal sekaligus. Pertama, apakah elemen ini masih",
                    "ikut alur dokumen. Kedua, angka top/right/bottom/left dihitung dari",
                    "mana.",
                    "",
                    "static (bawaan)",
                    "  - Ikut alur normal. top/right/bottom/left diabaikan sepenuhnya.",
                    "  - Selama sebuah elemen masih static, ngasih top: 20px nggak ngaruh",
                    "    apa-apa. Ini penyebab paling sering dari keluhan \"kok nggak",
                    "    gerak\". Angkanya benar, tapi nggak ada yang membacanya.",
                    "",
                    "relative",
                    "  - Tetap ikut alur, dan tempat aslinya tetap disediakan. Tapi",
                    "    gambarnya digeser dari tempat itu. top: 10px artinya turun 10px",
                    "    dari tempat seharusnya.",
                    "  - Tetangganya nggak ikut bergeser dan nggak tahu apa-apa. Makanya",
                    "    relative bisa bikin elemen menimpa tetangganya.",
                    "",
                    "absolute",
                    "  - Keluar dari alur. Tempatnya nggak lagi disediakan, jadi elemen",
                    "    lain mengisi bekas tempatnya seolah dia nggak pernah ada.",
                    "  - Posisinya dihitung dari leluhur terdekat yang position-nya bukan",
                    "    static.",
                    "",
                    "fixed",
                    "  - Keluar dari alur, posisinya dihitung dari jendela browser. Nggak",
                    "    ikut bergulir.",
                    "  - Dipakai untuk bilah kepala yang menempel dan tombol mengambang.",
                    "",
                    "sticky",
                    "  - Campuran. Awalnya bersikap normal, lalu begitu batas yang kamu",
                    "    tentukan tercapai saat halaman digulir, dia menempel di situ.",
                    "  - Wajib punya salah satu dari top/right/bottom/left. Tanpa itu dia",
                    "    nggak pernah menempel, dan kelihatannya kayak nggak berfungsi.",
                ]
            },
            {
                "body": [
                    "Kenapa position: absolute butuh induk yang positioned",
                    "",
                    "absolute selalu butuh titik acuan. Cara dia nyarinya sederhana. Dia",
                    "naik ke induknya satu per satu sambil nanya, \"kamu punya position",
                    "selain static?\" Yang pertama menjawab ya jadi acuannya. Kalau nggak",
                    "ada yang menjawab, acuannya halaman itu sendiri.",
                    "",
                    "Masalahnya, bawaan semua elemen adalah static. Jadi kalau kamu nggak",
                    "ngapa-ngapain, nggak ada yang menjawab. Lencana yang mau kamu tempel",
                    "di pojok kartu malah lompat ke pojok halaman. Angkanya (top: 8px;",
                    "right: 8px;) udah benar. Yang kurang adalah elemen yang mau jadi",
                    "acuan.",
                    "",
                    "Obatnya satu baris, dipasang di induknya:",
                    "",
                    "  .kartu { position: relative; }",
                    "",
                    "relative tanpa top atau left nggak menggeser apa pun. Di sini",
                    "tugasnya cuma satu: angkat tangan, supaya anak yang absolute",
                    "menemukannya. Pola \"induk relative, anak absolute\" ini yang paling",
                    "sering dipakai di CSS. Lencana di kartu, tombol tutup di dialog, ikon",
                    "di dalam kotak isian, semuanya pakai pola ini.",
                    "",
                    "Kalau elemen yang absolute muncul di tempat yang sama sekali nggak",
                    "kamu duga, cari dulu leluhur mana yang jadi acuannya. Sering kali",
                    "jawabannya \"nggak ada\".",
                ]
            },
            {
                "body": [
                    "z-index: siapa di atas siapa",
                    "",
                    "  - Angka yang lebih besar tampil di depan.",
                    "  - z-index cuma berlaku pada elemen yang position-nya bukan static",
                    "    (atau yang jadi item flex/grid). Pada elemen static, z-index",
                    "    diabaikan tanpa pemberitahuan.",
                    "  - Angkanya cuma dibandingkan di dalam stacking context yang sama.",
                    "    Stacking context itu semacam lapisan tumpukan tersendiri. Induk",
                    "    yang opacity-nya kurang dari 1, yang diberi transform (materi",
                    "    Transform), atau yang diberi filter (materi Bayangan dan Filter)",
                    "    bikin lapisan baru. Anak dengan z-index 9999 di dalamnya tetap",
                    "    nggak bisa melewati saudara induknya. Ini penyebab keluhan",
                    "    \"z-index-ku nggak mempan, padahal angkanya udah gede banget\".",
                    "    Yang perlu dinaikkan induknya, bukan anaknya.",
                    "    Yang bikin ini menjebak: ketiganya properti hiasan, kelihatannya",
                    "    nggak ada hubungannya dengan tumpukan. Satu transform:",
                    "    translateY(-2px) saat hover di sebuah kartu udah cukup untuk",
                    "    mengurung menu turun di dalamnya, walaupun nggak ada angka",
                    "    z-index yang berubah.",
                    "  - Jangan naikkan angkanya sampai 99999 tiap kali ada masalah.",
                    "    Sepakati beberapa tingkat aja, misalnya 10 untuk menu turun, 100",
                    "    untuk dialog, dan 1000 untuk pesan sistem. Lalu patuhi.",
                    "",
                    "Kalau sticky nggak menempel, biasanya penyebabnya salah satu dari tiga",
                    "ini:",
                    "  1. Lupa nulis top: 0 (atau sisi lainnya).",
                    "  2. Ada leluhur yang overflow-nya hidden, auto, atau scroll. sticky",
                    "     menempel pada wadah gulir terdekat. Kalau wadah itu nggak ikut",
                    "     bergulir, nggak ada yang terjadi.",
                    "  3. Induk langsungnya nggak lebih tinggi dari elemennya. sticky cuma",
                    "     bisa menempel selama induknya masih kelihatan.",
                    "",
                    "Bedanya dengan fixed: sticky berhenti menempel begitu induknya habis",
                    "tergulir. Makanya sticky cocok untuk judul bagian yang cuma menempel",
                    "selama bagiannya sendiri sedang dibaca.",
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
                    "Akibat dari .kepala yang sticky: tautan lompat mendarat di baliknya",
                    "",
                    "Begitu ada bilah kepala sticky setinggi 64px di atas halaman, semua",
                    "tautan lompat <a href=\"#bagian\"> jadi terasa rusak. Browser menggulir",
                    "sampai judul bagiannya pas di tepi atas jendela. Padahal tepi atas",
                    "jendela sekarang ketutup bilahmu sendiri. Judulnya sampai, tapi nggak",
                    "kelihatan. Gejalanya mirip tautan yang salah alamat, padahal alamatnya",
                    "benar.",
                    "",
                    "Obatnya dipasang di sasarannya, bukan di tautannya:",
                    "",
                    "  h2 { scroll-margin-top: 80px; }",
                    "",
                    "Artinya: kalau kamu jadi sasaran gulir, anggap kamu punya margin 80px",
                    "di atas. Angkanya tinggi bilah ditambah sedikit ruang lega. Margin ini",
                    "cuma dipakai waktu menggulir. Tata letaknya nggak bergeser sama",
                    "sekali.",
                    "",
                    "Ada juga scroll-margin-bottom. Lalu ada scroll-padding-top, yang",
                    "dipasang di wadah gulirnya kalau kamu mau satu setelan berlaku untuk",
                    "semua sasaran di dalamnya sekaligus.",
                    "",
                    "Gulir yang mulus, dan kenapa harus dimatikan sendiri",
                    "",
                    "  html { scroll-behavior: smooth; }",
                    "",
                    "Dengan baris itu, lompatan tadi nggak lagi pindah seketika, tapi",
                    "meluncur. Cuma satu baris, tapi ada satu urusan yang ikut datang.",
                    "",
                    "Sebagian orang menyetel sistemnya untuk mengurangi gerak. Halaman",
                    "menghormati setelan itu lewat blok @media (prefers-reduced-motion:",
                    "reduce), yang dibahas lengkap nanti di materi Transisi dan Animasi.",
                    "Blok itu biasanya cuma mematikan animation-duration dan",
                    "transition-duration. Sementara scroll-behavior bukan animation dan",
                    "bukan transition, jadi dia lolos. Kamu harus mematikannya sendiri:",
                    "",
                    "  @media (prefers-reduced-motion: reduce) {",
                    "    html { scroll-behavior: auto; }",
                    "  }",
                    "",
                    "Gulir sepanjang halaman adalah gerakan terbesar yang bisa dibikin",
                    "sebuah situs. Untuk sebagian orang, halaman yang meluncur sendiri",
                    "bikin mual.",
                    "",
                    "Mengunci guliran di tiap kartu (scroll-snap)",
                    "",
                    "Kamu mau deretan kartu mendatar yang berhenti rapi di tiap kartu, dan",
                    "nggak nyangkut di antara dua kartu? Cukup dua properti:",
                    "",
                    "  .deret         { overflow-x: auto; scroll-snap-type: x mandatory; }",
                    "  .deret > .kartu { scroll-snap-align: start; }",
                    "",
                    "scroll-snap-type dipasang di wadahnya. Sebut sumbunya (x atau y), lalu",
                    "tulis mandatory kalau wajib berhenti pas, atau proximity kalau cuma",
                    "dibantu mendekat. scroll-snap-align dipasang di tiap anaknya: start,",
                    "center, atau end.",
                    "",
                    "Pakai secukupnya. Guliran yang nggak mau berhenti di tempat yang",
                    "dituju pembaca bikin halaman terasa melawan.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Lencana \"Terlaris\" di pojok kartu menu, tombol chat yang mengambang",
                    "di sudut situs UMKM, dan bilah atas yang menempel saat halaman",
                    "digulir: ketiganya urusan position. Yang paling sering kamu tulis",
                    "adalah pasangan induk relative dan anak absolute.",
                    "",
                    "Kasus kecil: situs katering rumahan menampilkan kartu menu. Tiap",
                    "kartu punya lencana \"Terlaris\" yang harus menempel di pojok kanan",
                    "atas kartunya. Kamu menulis position: absolute, top: 8px, dan",
                    "right: 8px di lencana. Semua lencana malah menumpuk di pojok kanan",
                    "atas halaman.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pahami cara absolute mencari acuan: dia naik ke leluhurnya satu",
                    "     per satu, mencari yang position-nya selain static. Kartunya masih",
                    "     static, jadi acuannya halaman.",
                    "  2. Jadikan kartunya acuan. relative tanpa top atau left nggak",
                    "     menggeser kartu sama sekali:",
                    "      .kartu-menu { position: relative; }",
                    "      .kartu-menu .lencana { position: absolute; top: 8px; right: 8px; }",
                    "  3. Periksa kasus pinggir: kalau kartunya punya overflow: hidden",
                    "     supaya sudut membulatnya ikut memotong foto, lencana yang sengaja",
                    "     menjorok keluar pojok (top: -8px) ikut terpotong. Geser lencana",
                    "     ke dalam, atau pindahkan overflow: hidden ke pembungkus fotonya.",
                ]
            },
        ],
    },
    {
        "title": "18. Pseudo-class dan Pseudo-element",
        "sections": [
            {
                "body": [
                    "Pseudo-class memilih elemen yang sedang ada dalam keadaan tertentu,",
                    "misalnya sedang disentuh kursor atau sedang dicentang. Ditulis pakai",
                    "satu titik dua.",
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
                    ":nth-child menghitung semua anak, apa pun tagnya. :nth-of-type cuma",
                    "menghitung yang setipe. Bedanya kelihatan di contoh ini:",
                    "",
                    "  <div> <h2>Judul</h2> <p>A</p> <p>B</p> </div>",
                    "",
                    "  p:nth-child(2)    -> cocok dengan <p>A</p>, karena A memang",
                    "                       anak ke-2 di dalam div",
                    "  p:nth-child(1)    -> tidak cocok apa pun; anak ke-1 itu h2",
                    "  p:nth-of-type(1)  -> cocok dengan <p>A</p>",
                    "",
                    "Kalau :first-child nggak mempan, hampir pasti ada elemen lain yang",
                    "duduk di urutan pertama. Bisa judul, gambar, atau komentar yang kamu",
                    "lupa.",
                ]
            },
            {
                "body": [
                    "Pseudo-element bikin bagian yang nggak ada di HTML. Ditulis pakai dua",
                    "titik dua.",
                    "",
                    "  p::first-line      baris pertama paragraf",
                    "  p::first-letter    huruf pertamanya",
                    "  ::selection        teks yang sedang disorot pengguna",
                    "  ::placeholder      teks bayangan di dalam kotak isian",
                    "  ::before ::after   isi tambahan sebelum atau sesudah isi elemen",
                    "",
                    "::before dan ::after wajib punya properti content, walaupun isinya",
                    "kosong:",
                    "",
                    "  .catatan::before { content: \"Catatan: \"; font-weight: 700; }",
                    "  .kartu::after    { content: \"\"; display: block; clear: both; }",
                    "",
                    "Tanpa content, keduanya nggak muncul sama sekali. Ini kesalahan paling",
                    "umum waktu memakainya. Gejalanya membingungkan, karena semua aturan",
                    "lain di blok itu kelihatan benar.",
                    "",
                    "Isi ::before dan ::after bukan isi sungguhan. Nggak ikut tersalin",
                    "dengan rapi, dan nggak selalu dibacakan pembaca layar. Jadi pakai",
                    "untuk hiasan: garis, tanda kutip, ikon kecil, atau tanda bintang di",
                    "isian wajib. Untuk informasi yang artinya hilang kalau nggak terbaca,",
                    "tulis langsung di HTML.",
                    "",
                    "Kenapa ada yang pakai satu titik dua dan ada yang dua?",
                    "  - CSS versi lama pakai satu titik dua untuk keduanya.",
                    "  - CSS3 membedakannya: satu untuk keadaan (pseudo-class), dua untuk",
                    "    bagian buatan (pseudo-element).",
                    "  - Browser masih menerima :before demi halaman lama. Tapi di kode",
                    "    baru tulis ::before, supaya maksudnya jelas.",
                ]
            },
            {
                "body": [
                    "Urutan aturan tautan ada aturannya",
                    "",
                    "  a:link  ->  a:visited  ->  a:hover  ->  a:active",
                    "",
                    "Keempatnya punya spesifisitas yang sama, jadi yang dipakai adalah yang",
                    "ditulis belakangan. Kalau :hover ditulis sebelum :visited, tautan yang",
                    "pernah dibuka nggak berubah warna saat disentuh kursor. Kamu bakal",
                    "ngira :hover-nya rusak, padahal cuma kalah urutan. Gampangnya, hafalkan",
                    "singkatan LoVe-HAte.",
                    "",
                    "Penanda fokus jangan dihapus",
                    "",
                    "  :focus { outline: none; }",
                    "",
                    "Satu baris ini bikin halaman nggak bisa dipakai lewat keyboard. Orang",
                    "yang menekan Tab nggak tahu lagi tombol mana yang sedang terpilih.",
                    "Yang mereka lihat cuma halaman yang diam. Buat sebagian orang, ini",
                    "artinya halamanmu nggak bisa dipakai sama sekali.",
                    "",
                    "Kalau garis bawaannya jelek, ganti dengan yang lebih bagus, jangan",
                    "dihilangkan:",
                    "",
                    "  :focus-visible {",
                    "    outline: 2px solid #1a4fa0;",
                    "    outline-offset: 2px;",
                    "  }",
                    "",
                    ":focus-visible cuma menandai kalau browser menganggap penandanya",
                    "perlu. Biasanya muncul saat kamu pindah pakai Tab, dan nggak muncul",
                    "saat diklik pakai mouse. Hasil ini biasanya yang kamu mau, dan memang",
                    "untuk itu pseudo-class ini dibuat.",
                    "",
                    "Yang dipakai outline, bukan border, karena outline nggak makan tempat.",
                    "Waktu outline muncul, nggak ada elemen lain yang ikut bergeser.",
                ]
            },
            {
                "body": [
                    "Bentuk kursor ikut ngasih tahu keadaan",
                    "",
                    "Keadaan sebuah elemen nggak cuma dikabarkan lewat warna. Bentuk",
                    "penunjuk mouse juga ikut ngasih pesan, dan bentuknya diatur pakai",
                    "properti biasa:",
                    "",
                    "  cursor: pointer       tangan menunjuk: 'ini bisa diklik'",
                    "  cursor: default       panah biasa, bawaan hampir semua tempat",
                    "  cursor: text          balok tegak, bawaan di atas teks",
                    "  cursor: not-allowed   lingkaran dicoret: 'sedang tidak bisa'",
                    "  cursor: grab          telapak terbuka: 'ini bisa diseret'",
                    "  cursor: grabbing      telapak menggenggam, saat sedang diseret",
                    "  cursor: wait          'tunggu, sedang dikerjakan'",
                    "",
                    "cursor: pointer paling sering dibutuhkan, dan paling sering lupa",
                    "ditulis. Dari browser, yang otomatis dapat tangan menunjuk cuma <a>",
                    "yang punya href. <button> nggak dapat. Bawaannya panah biasa, dan",
                    "banyak orang kaget soal ini.",
                    "",
                    "Begitu juga <div>, <span>, atau <a> tanpa href yang kamu jadikan",
                    "tombol. Bentuknya mirip tombol, tapi kursornya nggak berubah waktu",
                    "lewat di atasnya. Orang nggak tahu benda itu bisa diklik sampai iseng",
                    "mencoba. Makanya hampir semua contoh tombol di materi ini menulis",
                    "cursor: pointer sendiri.",
                    "",
                    "Kebalikannya juga sering salah. Kalau teks biasa diberi cursor:",
                    "pointer, orang bakal mengkliknya, lalu nggak terjadi apa-apa. Bentuk",
                    "kursor itu janji. Pasang tangan menunjuk cuma kalau memang ada yang",
                    "terjadi waktu diklik.",
                    "",
                    "Karena itu, di contoh berikut cursor: not-allowed dipasang bareng",
                    "button:disabled. opacity ngasih tahu mata bahwa tombolnya mati. cursor",
                    "ngasih tahu tangan hal yang sama, sebelum jarinya sempat menekan.",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Daftar absensi, rekap nilai, dan menu navigasi di aplikasi sekolah",
                    "memakai pseudo-class untuk hal-hal kecil yang bikin nyaman dibaca.",
                    "Contohnya baris selang-seling, garis pemisah di antara item, dan",
                    "tombol yang kelihatan mati waktu belum boleh ditekan.",
                    "",
                    "Kasus kecil: halaman absensi online menampilkan 30 siswa dalam",
                    "<ul class=\"absen\">. Wali kelas minta tiga hal: warna baris",
                    "selang-seling, garis pemisah cuma di antara baris (nggak di atas",
                    "baris pertama), dan tombol \"Simpan\" yang sedang dimatikan (disabled)",
                    "kelihatan jelas mati.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pecah jadi tiga aturan, masing-masing dengan satu pseudo-class",
                    "     atau kombinator.",
                    "  2. Pilih alatnya:",
                    "      .absen li:nth-child(even) { background: #f6f7f9; }",
                    "      .absen li + li { border-top: 1px solid #e3e3e3; }",
                    "      button:disabled { opacity: 0.5; cursor: not-allowed; }",
                    "  3. Cek baris pertama: li + li cuma cocok dengan <li> yang punya",
                    "     saudara <li> tepat sebelumnya. Baris pertama nggak punya, jadi",
                    "     nggak dapat garis.",
                    "  4. Periksa kasus pinggir: status \"izin\" atau \"sakit\" ditulis",
                    "     langsung di HTML, jangan lewat content di ::after. Isi",
                    "     pseudo-element nggak selalu dibacakan pembaca layar, padahal",
                    "     status itu informasi.",
                ]
            },
        ],
    },
    {
        "title": "19. Transisi dan Animasi",
        "sections": [
            {
                "body": [
                    "transition nggak menggerakkan apa pun sendirian. Isinya cuma janji:",
                    "kalau nilai properti ini berubah, jangan lompat, tapi tempuh pelan-pelan.",
                    "",
                    "Yang mengubah nilainya selalu sesuatu yang lain:",
                    "  - pseudo-class seperti :hover, :focus-visible, atau :checked",
                    "    (materi Pseudo-class dan Pseudo-element)",
                    "  - class yang ditambah atau dihapus JavaScript",
                    "  - media query yang mulai berlaku saat ukuran jendela diubah",
                    "",
                    "Kalau nggak ada yang mengubah nilainya, transition diam aja. Nggak ada",
                    "error dan nggak ada pesan apa pun. Jadi kalau baris transition kamu",
                    "\"nggak jalan\", hampir selalu artinya nggak ada nilai yang berubah.",
                    "",
                    "Nilainya terdiri dari empat bagian, berurutan:",
                    "",
                    "  transition: background-color 0.2s ease 0s;",
                    "",
                    "  background-color   properti yang diawasi",
                    "  0.2s               durasi: berapa lama perjalanannya",
                    "  ease               kurva waktu: cepat-lambatnya sepanjang durasi",
                    "  0s                 jeda sebelum perjalanan dimulai",
                    "",
                    "Dua nilai waktu itu dibedakan dari urutannya. Yang pertama selalu",
                    "durasi, yang kedua selalu jeda. Jadi opacity 1s 0.5s artinya tunggu",
                    "setengah detik, lalu memudar selama satu detik.",
                    "",
                    "Satuannya wajib ditulis. Boleh 0.2s, boleh 200ms, tapi nggak boleh 0.2",
                    "aja. Nol pun harus pakai satuan: 0s. Kalau angkanya tanpa satuan,",
                    "browser membuang seluruh deklarasi transition itu tanpa bilang",
                    "apa-apa. Gejalanya sama persis dengan \"transition-nya nggak jalan\".",
                    "",
                    "Aturan: transition ditulis di keadaan dasar, bukan di dalam :hover.",
                    "Ini aturan yang paling sering dilanggar.",
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
                    "Alasannya begini. transition itu milik elemen pada keadaan yang sedang",
                    "berlaku. Saat kursor masuk, aturan :hover berlaku, dan di situ ada",
                    "transition, jadi geraknya halus. Saat kursor keluar, aturan :hover",
                    "berhenti berlaku, dan transition-nya ikut hilang. Nggak ada lagi yang",
                    "nyuruh browser pelan-pelan. Hasilnya: masuk halus, keluar mendadak.",
                    "",
                    "Gejala setengah jalan ini petunjuknya. Kalau geraknya cuma benar di",
                    "satu arah, transition-mu ada di tempat yang salah.",
                    "",
                    "Kalau kamu memang mau dua arah yang beda, misalnya masuk cepat dan",
                    "keluar lambat, tulis transition di kedua tempat dengan durasi",
                    "masing-masing. Itu sah dan disengaja. Yang salah cuma kalau transition",
                    "ditulis di :hover aja.",
                ],
            },
            {
                "body": [
                    "Beberapa properti dipisah koma, masing-masing dengan waktunya sendiri:",
                    "",
                    "  transition: color 0.15s ease-out,",
                    "              box-shadow 0.3s ease-out 0.05s;",
                    "",
                    "transition: all kelihatan praktis, tapi hampir selalu bikin masalah:",
                    "  - Browser mengawasi semua properti yang bisa dianimasikan, termasuk",
                    "    yang nggak pernah kamu maksud.",
                    "  - Suatu hari kamu menambah padding atau height di :hover, dan",
                    "    kartunya mulai melar pelan-pelan tanpa kamu minta.",
                    "  - Perubahan yang datang dari luar, misalnya tema gelap dipasang atau",
                    "    class ditambah JavaScript, ikut jadi animasi.",
                    "Jadi sebutkan propertinya satu per satu. Daftarnya sekalian jadi",
                    "catatan tentang apa aja yang boleh bergerak.",
                    "",
                    "Kurva waktu mengatur cepat-lambatnya gerak di sepanjang durasi, bukan",
                    "panjang durasinya. Dua gerakan yang sama-sama 0.3s bisa terasa beda",
                    "jauh.",
                    "",
                    "  linear        Kecepatan tetap dari awal sampai akhir. Terasa mekanis",
                    "                untuk benda yang seharusnya punya bobot, tapi justru",
                    "                benar untuk putaran spinner dan bilah kemajuan.",
                    "  ease          Bawaan kalau kamu nggak nulis apa-apa. Agak pelan di",
                    "                awal, cepat di tengah, lalu melambat panjang di akhir.",
                    "  ease-in       Mulai lambat, makin cepat. Terasa 'pergi'. Pas untuk",
                    "                sesuatu yang menghilang.",
                    "  ease-out      Mulai cepat, melambat di akhir. Terasa 'tiba'. Pas untuk",
                    "                sesuatu yang muncul, dan ini yang paling sering cocok.",
                    "  ease-in-out   Lambat di kedua ujung. Untuk gerak panjang atau yang",
                    "                bolak-balik.",
                    "  cubic-bezier(0.34, 1.4, 0.64, 1)",
                    "                Kurva buatan sendiri; empat angka itu dua titik kendali.",
                    "                Nama-nama di atas cuma julukan untuk kurva seperti ini.",
                    "                Angka kedua dan keempat boleh melewati 1, dan dari situ",
                    "                muncul efek 'melenting sedikit'.",
                    "  steps(12, end)",
                    "                Melompat, bukan meluncur. Untuk animasi sprite, jarum",
                    "                detik yang berdetak, atau efek mesin ketik.",
                    "",
                    "ease-out terasa paling wajar untuk sesuatu yang muncul. Di dunia nyata,",
                    "benda yang datang biasanya cepat dulu, lalu direm sampai berhenti.",
                    "Gerak yang berangkat pelan lalu makin cepat malah kelihatan kayak",
                    "sesuatu yang kabur. Cocok untuk yang pergi, aneh untuk yang datang.",
                    "Kalau ragu: ease-out untuk masuk, ease-in untuk keluar.",
                    "",
                    "Nggak semua properti bisa ditransisikan. Syaratnya cuma satu: harus",
                    "ada nilai antara. #ffffff ke #000000 punya nilai tengah. 0px ke 16px",
                    "punya nilai tengah. block ke none nggak punya, karena nggak ada",
                    "\"setengah block\".",
                    "",
                    "  Bisa    warna, panjang (width, padding, top, gap), opacity, transform,",
                    "          box-shadow, border-radius, filter, dan angka seperti flex-grow",
                    "  Tidak   display, position, float, font-family, flex-direction,",
                    "          background-image",
                    "",
                    "Properti yang nggak bisa ditransisikan tetap berubah. Cuma berubahnya",
                    "seketika, tanpa perjalanan dan tanpa peringatan.",
                    "",
                    "Akibatnya, display: none nggak bisa dipudarkan secara langsung. Elemen",
                    "dengan display: none nggak digambar sama sekali, jadi nggak ada yang",
                    "bisa dipudarkan. Pola yang dipakai orang selama bertahun-tahun adalah",
                    "opacity yang dipasangkan dengan visibility. Contoh lengkapnya ada di",
                    "bawah. visibility ikut dipakai karena elemen dengan opacity: 0 aja",
                    "masih bisa diklik dan masih dibacakan pembaca layar (materi Display",
                    "dan Alur Dokumen).",
                    "",
                    "Jebakan: height dari 0 ke auto juga nggak bisa ditransisikan, karena",
                    "auto bukan angka. Ada dua cara yang biasa dipakai:",
                    "  - max-height dengan angka yang cukup besar. Kekurangannya, kalau",
                    "    angkanya jauh melebihi tinggi aslinya, sebagian durasi habis",
                    "    untuk ruang kosong.",
                    "  - grid-template-rows dari 0fr ke 1fr pada wadah grid. Satuan fr",
                    "    punya nilai antara, jadi tingginya nggak perlu ditebak sama",
                    "    sekali.",
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
                    "transition selalu nunggu ada yang mengubah nilai. Kalau kamu mau",
                    "gerakan yang jalan sendiri, misalnya spinner yang berputar atau",
                    "notifikasi yang langsung masuk begitu muncul, itu tugas @keyframes dan",
                    "properti animation.",
                    "",
                    "@keyframes berisi resep gerakannya. Bentuknya beda dari aturan CSS",
                    "lain: yang berdiri di posisi pemilih adalah waktu, bukan elemen.",
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
                    "@keyframes sendiri nggak menjalankan apa pun. Dia cuma resep bernama",
                    "yang tersimpan di berkas. Yang menyalakannya adalah properti animation",
                    "di pemilih biasa:",
                    "",
                    "  .notif { animation: masuk 0.35s ease-out; }",
                    "",
                    "Ada delapan properti animation, dan bentuk ringkasnya bisa menampung",
                    "semuanya:",
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
                    "fill-mode menjawab satu pertanyaan: sebelum animasi mulai dan sesudah",
                    "selesai, elemen ini pakai nilai yang mana?",
                    "",
                    "  none (bawaan)  Nilai dari aturan CSS biasa. Begitu animasi habis, ia",
                    "                 melompat kembali ke sana.",
                    "  forwards       Nilai keyframe TERAKHIR dipertahankan sesudah selesai.",
                    "  backwards      Nilai keyframe PERTAMA sudah dipakai selama delay.",
                    "                 Tanpa ini, elemen sempat terlihat di keadaan akhirnya",
                    "                 selama jeda lalu melompat ke awal. Itu kedipan.",
                    "  both           Keduanya.",
                    "",
                    "Urutan di bentuk ringkasnya bebas, kecuali dua nilai waktu. Sama",
                    "seperti di transition, keduanya dibedakan dari urutan: durasi dulu,",
                    "baru jeda.",
                    "",
                    "  animation: masuk 0.35s ease-out 0.1s 1 normal backwards;",
                    "  animation: putar 0.8s linear infinite;",
                    "",
                    "Jebakan: nilai dasar sebuah properti nggak boleh cuma ada di dalam",
                    "@keyframes-nya. Kesalahan ini akibatnya paling mahal.",
                    "",
                    "Godaannya begini. Kamu sembunyikan dulu notifikasinya, animasikan",
                    "supaya muncul, lalu tahan pakai forwards supaya tetap kelihatan:",
                    "",
                    "  .notif { opacity: 0; animation: masuk 0.35s forwards; }   /* rapuh */",
                    "",
                    "Suatu hari animasinya nggak jalan. Mungkin namanya salah ketik, mungkin",
                    "geraknya dimatikan lewat prefers-reduced-motion, atau elemennya dibuat",
                    "ulang JavaScript sebelum animasinya selesai. Akibatnya notifikasi itu",
                    "nggak pernah kelihatan. Nggak ada error. Elemennya ada di sana dengan",
                    "rapi, cuma opacity-nya 0.",
                    "",
                    "Patokannya: keadaan akhir animasi harus sama dengan keadaan normal",
                    "elemennya, dan animasinya cuma berangkat dari tempat lain. Caranya",
                    "cukup tulis from aja. Keyframe yang nggak ditulis diisi browser pakai",
                    "nilai elemen itu sendiri:",
                    "",
                    "  .notif { opacity: 1; }",
                    "  @keyframes masuk { from { opacity: 0; transform: translateY(-12px); } }",
                    "",
                    "Sekarang animasinya boleh gagal kapan aja, dan yang tersisa tetap",
                    "notifikasi yang benar.",
                    "",
                    "Satu lagi: tanpa forwards, begitu animasi selesai, properti kembali ke",
                    "nilai di aturan CSS biasa. Kalau kamu nggak menulisnya di sana, dia",
                    "kembali ke nilai bawaan properti itu (opacity 1, transform none), bukan",
                    "ke keyframe pertamanya.",
                ],
            },
            {
                "heading": "Animasi yang berjalan sendiri, dan tahu kapan harus diam",
                "body": [
                    "Kenapa animasi yang halus hampir selalu cuma pakai transform dan",
                    "opacity",
                    "",
                    "Browser menggambar halaman dalam tiga tahap:",
                    "  1. Menghitung tata letak, yaitu ukuran dan posisi semua kotak.",
                    "  2. Mengecat isinya.",
                    "  3. Menyusun lapisan-lapisannya.",
                    "",
                    "Mengubah width, height, top, atau margin memaksa tahap pertama diulang.",
                    "Artinya browser menghitung ulang tetangga, induk, dan sering seisi",
                    "halaman, enam puluh kali per detik. transform dan opacity nggak",
                    "menyentuh tata letak sama sekali. Keduanya bekerja di tahap terakhir,",
                    "dan elemen lain nggak perlu tahu. Jadi:",
                    "",
                    "  - geser dengan transform: translate(...), bukan top/left/margin",
                    "  - perbesar dengan transform: scale(...), bukan width/height",
                    "",
                    "(transform sendiri dibahas di materi Transform.) Bedanya kelihatan.",
                    "Gerakan yang menyentuh tata letak kelihatan tersendat di ponsel dan di",
                    "halaman panjang. Gerakan yang nggak menyentuhnya tetap mulus.",
                    "",
                    "will-change ngasih tahu browser lebih dulu bahwa sebuah properti bakal",
                    "berubah, supaya lapisan terpisahnya disiapkan sebelum dibutuhkan:",
                    "",
                    "  .kartu-seret { will-change: transform; }",
                    "",
                    "Pakai seperlunya. Tiap elemen yang diberi will-change makan memori dan",
                    "minta lapisan sendiri. Kalau dipasang di *, halamannya malah jadi",
                    "lebih lambat. will-change juga bikin stacking context baru, jadi",
                    "z-index anak-anaknya mendadak terkurung (materi Position). Pasang cuma",
                    "kalau kamu udah melihat gerakannya tersendat, dan cuma di elemen itu.",
                    "",
                    "Menghormati prefers-reduced-motion",
                    "",
                    "Di materi Responsif nanti ada blok yang memendekkan semua durasi jadi",
                    "0.01ms. Blok itu punya kekurangan. Animasi dengan infinite nggak",
                    "berhenti cuma karena durasinya pendek. Dia malah berputar cepat",
                    "banget. Jadi jaring pengaman itu juga perlu",
                    "animation-iteration-count: 1.",
                    "",
                    "Cara yang lebih baik daripada mematikan semuanya: perlakukan tiap gerak",
                    "sesuai perannya. Orang yang minta gerak dikurangi biasanya nggak",
                    "terganggu oleh sesuatu yang memudar. Yang bikin pusing itu perpindahan",
                    "besar, parallax, dan zoom. Jadi:",
                    "  - buang gerak geser-menggesernya,",
                    "  - pertahankan efek memudarnya,",
                    "  - matikan gerak yang cuma hiasan,",
                    "  - pelankan gerak yang masih harus menyampaikan sesuatu.",
                    "",
                    "Buat sebagian orang, misalnya yang punya vertigo, migrain, atau",
                    "gangguan keseimbangan (vestibular), animasi yang nggak diminta bikin",
                    "mual. Mereka menyalakan setelan itu di sistemnya supaya halaman",
                    "seperti punyamu ikut menurut.",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Notifikasi \"Berhasil masuk keranjang\" yang meluncur dari atas,",
                    "spinner saat pembayaran diproses, dan tombol yang warnanya berganti",
                    "halus saat ditunjuk kursor ada di hampir semua toko online. Yang",
                    "paling sering salah di sana adalah apa yang terjadi kalau animasinya",
                    "nggak jalan.",
                    "",
                    "Kasus kecil: toast, yaitu kotak notifikasi kecil yang muncul",
                    "sebentar, ditulis begini:",
                    "  .toast { opacity: 0; animation: masuk 0.3s forwards; }",
                    "Lalu tim menambah blok prefers-reduced-motion yang memasang",
                    "animation: none. Sejak itu, pemakai yang menyalakan setelan kurangi",
                    "gerak nggak pernah melihat toast sama sekali.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pahami penyebabnya: opacity 1 cuma ada di keyframe dan ditahan",
                    "     forwards. Begitu animasinya batal, yang tersisa opacity: 0.",
                    "  2. Balik polanya. Keadaan normal toast adalah terlihat, dan animasi",
                    "     cuma berangkat dari tempat lain:",
                    "      .toast { opacity: 1; animation: masuk 0.3s ease-out; }",
                    "      @keyframes masuk {",
                    "        from { opacity: 0; transform: translateY(-12px); }",
                    "      }",
                    "  3. Geraknya pakai transform dan opacity, jangan top, supaya tetap",
                    "     mulus di ponsel yang tenaganya kecil.",
                    "  4. Periksa kasus pinggir: di blok prefers-reduced-motion, ganti",
                    "     gerak geser dengan memudar aja. Toast tetap muncul, cuma tanpa",
                    "     perpindahan.",
                ]
            },
        ],
    },
    {
        "title": "20. Menata Tabel",
        "sections": [
            {
                "body": [
                    "Dari semua elemen HTML, tabel yang paling jelek sebelum disentuh CSS,",
                    "dan gaya bawaannya paling banyak. Kamu udah nulis tabel di materi HTML",
                    "Tabel. Sekarang giliran bikin tabel itu enak dibaca.",
                    "",
                    "Gejala pertama yang bikin hampir semua orang bingung: garis tepinya",
                    "dobel.",
                    "",
                    "  table, th, td { border: 1px solid #999; }",
                    "",
                    "Yang muncul garis kembar yang kelihatan timbul, kayak tabel tahun",
                    "2003, dan kisinya nggak rapi. Padahal kamu nggak salah ketik apa pun.",
                    "",
                    "Penyebabnya dua nilai bawaan yang nggak pernah kamu tulis:",
                    "",
                    "  border-collapse: separate;   /* tiap sel punya kotak border SENDIRI */",
                    "  border-spacing: 2px;         /* dan kotak-kotak itu berjarak 2px */",
                    "",
                    "Jadi border <table> digambar, lalu border tiap <td> digambar lagi 2px",
                    "di dalamnya. Dua garis sejajar berdempetan, dan itulah garis dobelnya.",
                    "",
                    "Obatnya satu baris, dan baris ini hampir selalu jadi baris pertama di",
                    "setiap tabel:",
                    "",
                    "  table { border-collapse: collapse; }",
                    "",
                    "collapse artinya sel-sel yang bersebelahan berbagi satu garis, nggak",
                    "punya garis sendiri-sendiri. Begitu collapse aktif, border-spacing",
                    "diabaikan sepenuhnya. Properti itu cuma berlaku di mode separate.",
                    "",
                    "Kapan separate masih dipakai? Kalau kamu memang mau sel-selnya",
                    "terpisah kayak kotak kalender: border-collapse: separate;",
                    "border-spacing: 8px;",
                    "",
                    "Ada beberapa akibat collapse yang perlu kamu tahu:",
                    "  - Kalau dua sel bersebelahan punya border yang beda, cuma satu yang",
                    "    digambar. Yang lebih tebal yang dipakai. Kalau sama tebal, gayanya",
                    "    yang menentukan: double di atas solid, solid di atas dashed, dan",
                    "    seterusnya. Jadi garis yang kamu tulis memang muncul, tapi belum",
                    "    tentu yang kamu kira.",
                    "  - border-radius nggak bekerja pada tabel yang collapse. Sudutnya",
                    "    tetap tajam berapa pun angkanya, karena garisnya udah bukan milik",
                    "    satu kotak lagi. Kalau kamu mau sudut membulat, bungkus tabelnya",
                    "    pakai wadah yang diberi border-radius dan overflow: hidden.",
                    "",
                    "Satu lagi yang sering bikin bingung: <table> nggak memakan seluruh",
                    "lebar seperti <div>. Lebarnya menyusut mengikuti isinya. Tabel dua",
                    "kolom yang isinya pendek bakal menempel di kiri, dengan ruang kosong",
                    "lebar di kanannya. Kalau kamu mau tabelnya selebar wadahnya, tulis",
                    "width: 100%.",
                ],
            },
            {
                "body": [
                    "Tulis border di sel, bukan di <table>",
                    "",
                    "  table { border: 1px solid #ccc; }   /* cuma bingkai LUAR */",
                    "  th, td { border: 1px solid #ccc; }  /* ini yang membuat kisinya */",
                    "",
                    "Border di <table> cuma jadi bingkai paling luar. Garis antar baris dan",
                    "antar kolom datang dari border milik <th> dan <td>. Hampir semua orang",
                    "pernah keliru di sini: border ditulis di table, lalu bingung kenapa",
                    "barisnya nggak terpisah.",
                    "",
                    "Tabel zaman sekarang jarang pakai kisi penuh. Pola yang paling banyak",
                    "dipakai cuma garis bawah:",
                    "",
                    "  th, td { border-bottom: 1px solid #e4e6ea; }",
                    "",
                    "Garis mendatar udah cukup untuk menuntun mata dari kiri ke kanan.",
                    "Garis tegak malah bikin tabel kelihatan sesak. Efek sampingnya, baris",
                    "terakhir ikut bergaris, jadi tabelnya kelihatan belum selesai. Matikan",
                    "dengan:",
                    "  tbody tr:last-child td { border-bottom: none; }",
                    "",
                    "Padding: satu-satunya cara bikin sel lega",
                    "",
                    "Padding bawaan sel cuma 1px, jadi hurufnya hampir menempel ke garis.",
                    "Kasih padding ke th dan td sekaligus. Kalau salah satu kelupaan, kepala",
                    "tabel nggak sejajar dengan isinya. Ukuran yang wajar: 12px 16px.",
                    "",
                    "Perhatikan: margin pada sel tabel diabaikan total. Sel bukan kotak",
                    "biasa. Dia bagian dari kisi tabel dan nggak punya margin sama sekali.",
                    "Kalau kamu nulis margin di td dan nggak terjadi apa-apa, aturannya",
                    "nggak kalah dari aturan lain. Properti itu memang nggak berlaku di",
                    "situ.",
                    "",
                    "th bawaannya tebal dan rata tengah",
                    "",
                    "Isinya rata kiri, judul kolomnya rata tengah, jadi tabelnya kelihatan",
                    "nggak lurus. Makanya hampir semua tabel butuh:",
                    "  th { text-align: left; }",
                    "Termasuk <th scope=\"row\"> di kolom pertama, yang sering kelupaan.",
                    "",
                    "Kolom berisi angka malah kebalikannya: pakai text-align: right, supaya",
                    "satuan dan ribuannya berbaris lurus ke bawah dan gampang dibandingkan.",
                    "Judul kolomnya ikut rata kanan. Kalau nggak, kepalanya nggak sejajar",
                    "dengan angkanya.",
                    "",
                    "vertical-align pada sel: top atau middle",
                    "",
                    "Bawaannya middle. Selama tiap baris cuma setinggi satu baris teks,",
                    "bedanya nggak kelihatan. Tapi begitu satu sel berisi paragraf panjang,",
                    "sel sebelahnya yang cuma satu kata bakal melayang di tengah, dan",
                    "kelihatan salah tempat. Untuk tabel yang isinya teks panjang, pakai",
                    "vertical-align: top di th dan td.",
                    "",
                    "(Di elemen inline, vertical-align mengatur hal yang beda, yaitu letak",
                    "elemen itu terhadap baris teksnya. Di sel tabel, dia mengatur letak",
                    "seluruh isi sel.)",
                    "",
                    "caption: judul tabel, ditata dari CSS",
                    "",
                    "  caption-side: top;      /* bawaan */",
                    "  caption-side: bottom;   /* judul pindah ke bawah tabel */",
                    "",
                    "Bawaannya rata tengah, jadi biasanya perlu text-align: left supaya",
                    "sejajar dengan kolom pertama. caption ada di luar garis tepi tabel,",
                    "jadi background tabel nggak mengenainya. Untuk jaraknya, pakai",
                    "padding-bottom, bukan margin.",
                    "",
                    "Baris selang-seling udah kamu lihat di contoh materi Pseudo-class dan",
                    "Pseudo-element. Sorot baris saat disentuh kursor pakai :hover dari",
                    "materi yang sama:",
                    "  tbody tr:nth-child(even) { background: #f6f7f9; }",
                    "  tbody tr:hover           { background: #eef2fb; }",
                    "",
                    "Tulis tbody di depannya, supaya kepala dan kaki tabel nggak ikut",
                    "belang. Beda warnanya harus tipis. Kalau terlalu kontras, tabelnya",
                    "jadi kayak papan catur. Ingat juga, :hover nggak ada di layar sentuh.",
                    "Anggap aja bonus, jangan jadi satu-satunya cara membedakan baris.",
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
                    "Lebar kolom: table-layout auto atau fixed",
                    "",
                    "table-layout: auto (bawaan)",
                    "  - Browser membaca seluruh isi tabel dulu, baru menentukan lebar",
                    "    tiap kolom.",
                    "  - Enaknya, kolom menyesuaikan isinya tanpa kamu atur apa pun.",
                    "  - Ada dua akibat yang nyebelin:",
                    "      1. Satu sel berisi teks panjang tanpa spasi, misalnya alamat",
                    "         tautan, kode pesanan, atau alamat surel, bisa melebarkan",
                    "         seluruh tabel sampai melewati wadahnya. Halamannya jadi bisa",
                    "         digeser ke samping (lihat materi Memotong dan Membungkus",
                    "         Teks).",
                    "      2. Lebar kolom berubah tiap kali datanya berubah. Tabel yang",
                    "         isinya datang dari server jadi goyang tiap kali dimuat ulang.",
                    "",
                    "table-layout: fixed",
                    "  - Lebar diambil dari baris pertama aja (atau dari <colgroup>). Isi",
                    "    di baris sesudahnya nggak dilihat sama sekali.",
                    "  - Lebar kolomnya tetap, dan tabel panjang jauh lebih cepat digambar,",
                    "    karena browser nggak perlu mengukur ribuan sel.",
                    "",
                    "Jebakan: table-layout: fixed butuh width di tabelnya. Syarat ini yang",
                    "paling sering terlewat.",
                    "",
                    "    .tabel { table-layout: fixed; width: 100%; }",
                    "",
                    "Tanpa width, fixed nggak ngapa-ngapain, dan kamu bakal ngira",
                    "propertinya nggak didukung browser. Padahal didukung. Dia cuma nggak",
                    "punya angka untuk dibagi.",
                    "",
                    "Akibatnya, teks yang nggak muat nggak lagi melebarkan kolomnya. Teks",
                    "itu meluber keluar sel. Jadi pasangkan dengan salah satu dari dua ini:",
                    "    td { overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }",
                    "    td { word-break: break-word; }",
                    "Yang pertama memotong teksnya dengan '...'. Yang kedua mematahkan",
                    "katanya.",
                    "",
                    "Dua cara mengatur lebar kolom",
                    "",
                    "  1. Kasih width pada sel di baris pertama. Cukup satu baris, seluruh",
                    "     kolom di bawahnya ikut. Nulis width di tiap td cuma buang waktu.",
                    "       thead th:first-child { width: 44%; }",
                    "  2. Pakai <colgroup> dan <col> di HTML, lalu tata dari CSS. Cara ini",
                    "     langsung menunjuk kolomnya, jadi nggak bergantung pada sel mana",
                    "     yang kebetulan ada di baris pertama.",
                    "       <colgroup><col class=\"kolom-menu\"><col><col></colgroup>",
                    "       .kolom-menu { width: 44%; }",
                    "     Hati-hati, cuma sedikit properti yang berlaku pada <col>: width,",
                    "     background, border, dan visibility. padding, color, text-align,",
                    "     dan font diabaikan tanpa pemberitahuan. Banyak orang buang",
                    "     setengah jam mencoba meratakan satu kolom lewat <col>. Caranya",
                    "     lewat class di tiap sel (lihat .angka di contoh).",
                    "",
                    "Persentase dihitung dari lebar tabel, dan jumlahnya nggak harus 100%.",
                    "Sisa ruangnya dibagi ke kolom yang nggak diberi width.",
                ],
            },
            {
                "heading": "index.html - markup yang diharapkan gaya di atas",
                "body": [
                    "Tabel adalah penyebab paling umum halaman yang bisa digeser ke samping",
                    "",
                    "Tiga kolom berisi teks, masing-masing dengan padding, udah lebih lebar",
                    "dari layar ponsel. Jangan kecilkan hurufnya. Bungkus tabelnya (materi",
                    "Memotong dan Membungkus Teks):",
                    "",
                    "  .bungkus-tabel { overflow-x: auto; }",
                    "",
                    "Sekarang yang bisa digeser cuma tabelnya, halamannya tetap diam. Kalau",
                    "tabelnya ada di dalam kolom grid atau item flex, wadahnya masih perlu",
                    "min-width: 0 (materi Flexbox dan materi Grid). Tanpa itu, kolomnya ikut",
                    "melebar dan pembungkusnya nggak pernah bisa digulir.",
                    "",
                    "Kepala tabel yang menempel saat digulir",
                    "",
                    "  thead th { position: sticky; top: 0; }",
                    "",
                    "Tulis di th, bukan di thead atau tr, karena browser lama cuma bisa",
                    "menempelkan sel. Semua syarat sticky dari materi Position berlaku. Di",
                    "tabel, ada empat hal yang perlu kamu cek:",
                    "",
                    "  1. Wajib ada top (atau sisi lain). Tanpa itu, kepalanya nggak pernah",
                    "     menempel.",
                    "  2. sticky menempel pada wadah gulir terdekat. Begitu tabelnya",
                    "     dibungkus .bungkus-tabel, acuannya jadi pembungkus itu, bukan",
                    "     halaman. Kalau pembungkusnya setinggi isinya, dia nggak pernah",
                    "     menggulir ke bawah, jadi kepalanya diam aja walaupun halamannya",
                    "     digulir. Makanya contoh di atas ngasih max-height. Satu lagi:",
                    "     nulis overflow-x: auto aja udah bikin overflow-y ikut jadi auto.",
                    "     Jadi pembungkusmu udah jadi wadah gulir walaupun kamu nggak",
                    "     memintanya.",
                    "  3. Sel yang menempel wajib punya background. Bawaannya bening, jadi",
                    "     baris yang lewat di belakangnya bakal kelihatan menembus tulisan",
                    "     di kepala tabel.",
                    "  4. Dengan border-collapse: collapse, border milik sel kepala ikut",
                    "     tergulir bersama tabelnya. Garis bawahnya malah hilang tepat saat",
                    "     kepalanya menempel. Gantinya pakai box-shadow: inset 0 -1px 0",
                    "     warna, karena bayangan itu menempel pada selnya.",
                    "",
                    "Kasih juga z-index kecil pada sel kepala, supaya dia ada di atas sel",
                    "isi.",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Laporan kas UMKM, rekap nilai rapor, dan daftar harga di aplikasi",
                    "kasir semuanya tabel. Beda tabel yang enak dibaca dengan yang",
                    "melelahkan cuma beberapa baris CSS: satu garis per sel, sel yang",
                    "lega, dan angka yang rata kanan.",
                    "",
                    "Kasus kecil: laporan kas warung bulan Oktober punya kolom Tanggal,",
                    "Keterangan, Masuk (Rp), dan Keluar (Rp). Angka seperti 1.250.000 dan",
                    "75.000 susah dibandingkan karena rata kiri. Garisnya dobel, dan di",
                    "ponsel seluruh halaman bisa digeser ke samping.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pisahkan tiga gejalanya, karena tiap gejala punya obat sendiri.",
                    "  2. Garis dobel datang dari border-collapse: separate bawaan. Satukan",
                    "     garisnya, lalu taruh border di sel:",
                    "      .kas { width: 100%; border-collapse: collapse; }",
                    "      .kas th, .kas td { padding: 8px 12px; border-bottom: 1px solid #ddd; }",
                    "      .kas .angka { text-align: right; }",
                    "      .bungkus-kas { overflow-x: auto; }",
                    "  3. Angka rata kanan: pasang class angka di th dan td kolom uang.",
                    "     Jangan lewat <col>, karena text-align di <col> diabaikan.",
                    "  4. Halaman yang bergeser: bungkus tabelnya dengan",
                    "     <div class=\"bungkus-kas\">, supaya yang bergeser cuma tabelnya.",
                ]
            },
        ],
    },
    {
        "title": "21. Menata Formulir",
        "sections": [
            {
                "body": [
                    "Ada empat elemen yang nggak digambar seperti kotak biasa: <input>,",
                    "<select>, <textarea>, dan <button>. Yang menggambarnya adalah widget,",
                    "yaitu komponen tampilan bawaan sistem operasi. Kotak centang di",
                    "Windows, macOS, dan Android bentuknya beda-beda, dan nggak satu pun",
                    "bentuk itu datang dari CSS-mu.",
                    "",
                    "Makanya sebagian aturanmu terasa diabaikan. Materi Teks dan Font udah",
                    "menambal separuh masalahnya:",
                    "",
                    "  input, select, textarea, button { font: inherit; }",
                    "",
                    "Tapi huruf cuma satu bagian. background pada <select> sering nggak",
                    "kelihatan, border-radius diabaikan, dan warna centang tetap biru",
                    "bawaan sistem.",
                    "",
                    "Kuncinya: appearance",
                    "",
                    "  select { appearance: none; -webkit-appearance: none; }",
                    "",
                    "appearance: none mencopot rupa bawaan sistem. Sesudah itu, properti",
                    "CSS biasa baru mempan. Baris -webkit- di belakangnya masih ditulis",
                    "orang karena Safari lama, termasuk yang di iPhone, cuma ngerti versi",
                    "yang itu.",
                    "",
                    "Harganya: yang dicopot itu semuanya, termasuk bagian yang berguna.",
                    "  - Panah kecil di <select> ikut hilang. Kotaknya jadi mirip kotak",
                    "    teks biasa, dan orang nggak tahu lagi bahwa isinya bisa dibuka.",
                    "  - Kotak centang jadi kotak kosong yang nggak nampilin apa pun waktu",
                    "    dicentang. Kotaknya nggak rusak. Cuma udah nggak ada lagi yang",
                    "    menggambar tanda centangnya.",
                    "",
                    "Pegangannya: jangan mencopot rupa bawaan yang nggak kamu gambar ulang.",
                    "",
                    "Ada dua tambalan kecil yang layak dipasang dari awal:",
                    "",
                    "  input, select, textarea { box-sizing: border-box; }",
                    "    supaya width: 100% tidak melebar keluar wadahnya (lihat materi Box Model)",
                    "",
                    "  textarea { resize: vertical; }",
                    "    supaya orang tidak bisa menariknya melebar dan merusak tata letakmu",
                    "",
                    "Beberapa isian memang nggak bisa ditata bagian dalamnya sama sekali:",
                    "type=\"file\", type=\"color\", dan pemilih tanggal. Biasanya orang",
                    "menyembunyikan kontrol aslinya, lalu menata <label>-nya. Tekniknya",
                    "sama dengan kotak centang buatan sendiri yang dibahas di bawah nanti.",
                ],
            },
            {
                "body": [
                    "Sebelum mencopot apa pun, coba tiga properti ini dulu",
                    "",
                    "  accent-color   warna centang, titik radio, bilah geser, dan progress",
                    "  caret-color    warna kursor ketik yang berkedip di dalam kotak isian",
                    "  ::placeholder  warna teks bayangan (sudah dikenal dari materi",
                    "                 Pseudo-class dan Pseudo-element)",
                    "",
                    "accent-color itu jalan pintas yang jarang diketahui pemula:",
                    "",
                    "  body { accent-color: #1a4fa0; }",
                    "",
                    "Satu baris itu mewarnai semua kotak centang, radio, dan slider di",
                    "halaman, tanpa mencopot apa pun. Penanda fokus bawaannya tetap ada,",
                    "tanda centangnya tetap digambar sistem, dan di ponsel ukurannya tetap",
                    "pas untuk jari. accent-color juga diwarisi anak-anaknya, jadi cukup",
                    "ditulis sekali di body.",
                    "",
                    "Untuk kebanyakan formulir, sampai sini udah cukup. Keluarkan",
                    "appearance: none cuma kalau bentuknya memang harus lain.",
                    "",
                    "caret-color kedengarannya sepele, sampai kamu bikin kotak isian",
                    "berlatar gelap. Kursor ketiknya hitam di atas latar hitam, dan orang",
                    "ngira kotaknya mati:",
                    "",
                    "  .gelap input { background: #1e2126; color: #fff; caret-color: #fff; }",
                    "",
                    ":focus-within, yang sering ditulis orang pakai JavaScript",
                    "",
                    ":focus cocok dengan elemen yang sedang difokuskan. :focus-within cocok",
                    "dengan elemen yang berisi elemen terfokus, sedalam apa pun letaknya.",
                    "",
                    "  .baris:focus-within label { color: #1a4fa0; }",
                    "",
                    "Klik kotak isiannya, dan tulisan labelnya ikut menyala, padahal yang",
                    "difokus input-nya. Tanpa :focus-within, satu-satunya cara adalah",
                    "mendengarkan kejadian focus dan blur lewat JavaScript, lalu menambah",
                    "dan menghapus class sendiri. Banyak kode lama begitu karena ditulis",
                    "sebelum pseudo-class ini ada. Kalau kamu ketemu kode seperti itu,",
                    "sekarang kamu tahu alasannya.",
                ],
            },
            {
                "body": [
                    "Pseudo-class yang cuma ada di formulir",
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
                    ":checked dan :disabled udah dibahas di materi Pseudo-class dan",
                    "Pseudo-element. Semua yang di atas membaca aturan validasi yang kamu",
                    "tulis di HTML: required, min, max, pattern, type=\"email\". Aturan itu",
                    "dibahas di materi Formulir Lanjutan di kurikulum HTML. CSS sendiri",
                    "nggak memvalidasi apa pun. Dia cuma mewarnai hasil penilaian browser.",
                    "",
                    "Jebakan 1: :read-only cocok dengan hampir semua elemen. Artinya",
                    "\"nggak bisa disunting pengguna\", jadi isian yang dikunci cuma salah",
                    "satunya. <p>, <div>, dan <h1> juga read-only. Kalau kamu nulis",
                    ".kotak:read-only, div biasa juga ikut kena. Sebut elemennya:",
                    "input:read-only, textarea:read-only.",
                    "",
                    "Jebakan 2, yang paling sering merusak tampilan: :invalid menyala sejak",
                    "halaman dibuka.",
                    "",
                    "  input:invalid { border-color: crimson; }   /* jangan */",
                    "",
                    "Kotak yang wajib diisi dan masih kosong memang nggak valid, sejak",
                    "detik pertama, sebelum ada yang menyentuhnya. Jadi orang membuka",
                    "formulirmu dan langsung disambut lima kotak merah sebelum mengetik",
                    "satu huruf pun. Kesannya formulirnya rusak.",
                    "",
                    "Obatnya: :user-invalid",
                    "",
                    "  input:user-invalid { border-color: #a1141d; }",
                    "",
                    ":user-invalid baru menyala sesudah orangnya berurusan dengan isian",
                    "itu: mengetik lalu pindah keluar, atau menekan tombol kirim.",
                    "Pseudo-class ini memang dibuat untuk itu, dan hampir selalu ini yang",
                    "kamu mau.",
                    "",
                    "Obat cadangan untuk browser lama:",
                    "",
                    "  input:not(:placeholder-shown):invalid { border-color: #a1141d; }",
                    "",
                    "Cara bacanya: merah cuma kalau placeholder-nya udah nggak kelihatan,",
                    "artinya udah ada yang diketik. Tapi ada jebakan di sini juga:",
                    "input-nya wajib punya atribut placeholder. Tanpa itu,",
                    ":placeholder-shown nggak pernah cocok, :not(...) jadi selalu benar,",
                    "dan kamu balik lagi ke kotak merah sejak halaman dibuka.",
                    "",
                    "form:invalid juga ada. Dia cocok selama masih ada satu isian yang",
                    "belum lolos. Boleh dipakai untuk menandai tombol kirim, tapi tombolnya",
                    "jangan dimatikan. Kalau dimatikan, orang nggak punya cara memunculkan",
                    "pesan kesalahannya. Yang dia lihat cuma tombol mati, tanpa keterangan",
                    "apa yang kurang.",
                    "",
                    "Satu hal lagi yang berguna waktu membaca CSS orang lain. Kalau satu",
                    "pemilih di dalam daftar yang dipisah koma nggak dikenali browser,",
                    "seluruh aturan itu dibuang, nggak cuma pemilih yang salah. Jadi",
                    "pemilih baru seperti :user-invalid jangan ditumpuk bareng pemilih",
                    "penting lain dalam satu daftar.",
                ],
            },
            {
                "body": [
                    "Checkbox dan radio buatan sendiri",
                    "",
                    "Kalau accent-color nggak cukup, polanya begini: sembunyikan input",
                    "aslinya, lalu gambar kotaknya di ::before milik <label> di sebelahnya.",
                    "",
                    "  input:checked + label::before { background: #1a4fa0; }",
                    "",
                    "Ada tiga hal yang menentukan teknik ini berhasil atau gagal:",
                    "",
                    "  1. Sembunyikan input-nya, jangan dihapus.",
                    "     display: none dan visibility: hidden mengeluarkan input dari",
                    "     urutan Tab. Orang yang memakai keyboard nggak bisa mencapainya",
                    "     sama sekali, dan di layarmu nggak ada gejala apa pun karena",
                    "     tetikusmu masih jalan. Pakai opacity: 0, dan taruh input-nya",
                    "     tepat di atas kotak gambaranmu, supaya klik dan fokus mendarat",
                    "     di tempat yang benar.",
                    "  2. <label for> di sini wajib.",
                    "     Input aslinya nggak kelihatan, jadi label satu-satunya yang bisa",
                    "     diklik. Nilai for harus sama persis dengan id input-nya. Kalau",
                    "     nggak, klik orang nggak kena apa-apa dan kotakmu kelihatan mati.",
                    "     Alasan lengkapnya ada di materi Formulir di kurikulum HTML.",
                    "  3. Urutan di HTML menentukan.",
                    "     Tanda + artinya \"saudara yang persis berikutnya\". Kalau <label>",
                    "     ditulis sebelum <input>, nggak ada satu pun aturan yang cocok,",
                    "     karena CSS nggak bisa memilih ke belakang. Nggak ada pesan salah.",
                    "     Cuma nggak terjadi apa-apa.",
                    "",
                    "Karena input aslinya nggak kelihatan, penanda fokusnya juga ikut",
                    "nggak kelihatan. Gambar sendiri penanda fokusnya. Kalau nggak,",
                    "halamanmu kena kesalahan yang udah dibahas di materi Pseudo-class dan",
                    "Pseudo-element:",
                    "",
                    "  input:focus-visible + label::before { outline: 2px solid #1a4fa0; }",
                    "",
                    "Radio caranya sama persis, cuma kotaknya diganti lingkaran pakai",
                    "border-radius: 50%.",
                    "",
                    "Satu lagi: jangan pakai warna aja untuk menandai isian yang salah.",
                    "Border merah nggak ngasih tahu apa yang salah. Buat sebagian orang,",
                    "merahnya malah nggak kebaca sama sekali: buta warna dialami sekitar",
                    "satu dari dua belas laki-laki. Sediakan teksnya, dan tulis teks itu",
                    "sebagai HTML sungguhan yang cuma disembunyikan lewat CSS:",
                    "",
                    "  .galat { display: none; }",
                    "  input:user-invalid ~ .galat { display: block; }",
                    "",
                    "Pesannya jangan ditaruh di content pada ::after. Isi pseudo-element",
                    "nggak selalu dibacakan pembaca layar. Alasannya udah dibahas di",
                    "materi Pseudo-class dan Pseudo-element. Tanda bintang untuk isian",
                    "wajib itu urusan lain. Bintang itu hiasan, dan polanya (.wajib::after)",
                    "juga ada di materi yang sama.",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Formulir pendaftaran pasien puskesmas, pendaftaran sekolah online,",
                    "dan halaman checkout toko memakai validasi bawaan HTML. Tugas CSS-nya",
                    "menunjukkan isian mana yang salah di saat yang tepat, tanpa bikin",
                    "orang merasa dimarahi sebelum mengetik apa pun.",
                    "",
                    "Kasus kecil: formulir pasien baru punya isian NIK yang wajib",
                    "(required) dan harus 16 angka (pattern). Gayanya ditulis",
                    "input:invalid { border-color: crimson; }. Begitu halaman dibuka,",
                    "semua isian wajib langsung bergaris merah.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pahami penyebabnya: isian wajib yang masih kosong memang nggak",
                    "     valid sejak detik pertama, dan :invalid menilai keadaan saat itu.",
                    "  2. Ganti ke :user-invalid, yang baru menyala sesudah orangnya",
                    "     mengetik lalu pindah, atau menekan tombol kirim.",
                    "  3. Jangan cuma warna. Tulis pesannya di HTML, misalnya",
                    "     <span class=\"galat\">NIK harus 16 angka</span>, lalu:",
                    "      .galat { display: none; }",
                    "      input:user-invalid { border-color: #a1141d; }",
                    "      input:user-invalid ~ .galat { display: block; }",
                    "  4. Periksa kasus pinggir: jangan gabungkan :user-invalid dengan",
                    "     pemilih lain dalam satu daftar berkoma. Browser yang belum kenal",
                    "     pemilih itu membuang seluruh aturannya.",
                ]
            },
        ],
    },
    {
        "title": "22. Responsif: media query",
        "sections": [
            {
                "body": [
                    "Media query adalah aturan CSS yang cuma berlaku di kondisi tertentu,",
                    "misalnya kalau layarnya cukup lebar. Tapi sebelum media query bisa",
                    "jalan, ada satu baris HTML yang wajib ada di dalam <head>:",
                    "",
                    "  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">",
                    "",
                    "Tanpa baris itu, ponsel pura-pura layarnya selebar 980px, lalu",
                    "mengecilkan seluruh halaman supaya muat. Akibatnya media query",
                    "max-width: 600px nggak pernah menyala, karena menurut ponsel layarnya",
                    "memang lebar. Hurufnya pun jadi kecil banget.",
                    "",
                    "Baris itu ditulis di HTML, bukan di CSS. Tapi tanpa baris itu, isi",
                    "materi ini nggak ada gunanya. Kalau tata letak di ponselmu kelihatan",
                    "nggak berubah sama sekali, cek baris itu dulu.",
                    "",
                    "Bentuk media query:",
                    "",
                    "  @media (min-width: 720px) {",
                    "    .halaman { grid-template-columns: 240px 1fr; }",
                    "  }",
                    "",
                    "Cara bacanya: aturan di dalamnya cuma berlaku kalau lebar jendela",
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
                    "Mobile first artinya: tulis gaya dasarnya untuk layar sempit dulu,",
                    "lalu tambahkan aturan min-width untuk layar yang lebih lebar.",
                    "",
                    "Alasan arahnya begitu:",
                    "  - Tata letak sempit hampir selalu lebih sederhana (satu kolom, semua",
                    "    bertumpuk). Jadi gaya dasarnya pendek, dan yang perlu ditambahkan",
                    "    sedikit.",
                    "  - Kalau ada yang gagal dimuat, yang tersisa versi satu kolom, dan",
                    "    versi itu tetap kebaca di layar apa pun.",
                    "  - Kalau arahnya dibalik (pakai max-width), kamu terus membatalkan",
                    "    aturan yang baru aja kamu tulis. Lama-lama berkasnya isinya",
                    "    pembatalan dari pembatalan.",
                    "",
                    "Ambang, atau breakpoint, yaitu lebar tempat tata letak berganti,",
                    "diambil dari isi halamanmu. Merek ponsel nggak usah dipikirkan.",
                    "",
                    "Caranya: perbesar dan perkecil jendela pelan-pelan. Di lebar berapa",
                    "tata letaknya mulai jelek? Misalnya kolomnya terlalu sempit, judulnya",
                    "patah aneh, atau kartunya jadi pipih. Di situ ambangnya. Daftar",
                    "ukuran iPhone terbaru berubah tiap tahun, sedangkan isi halamanmu",
                    "tetap.",
                    "",
                    "Yang ini gampang terlewat: media query mengukur seluruh",
                    "lebar jendela, padahal ruang yang tersedia untuk isi bisa jauh lebih",
                    "sempit, karena panel sisi dan padding ikut makan tempat. Kalau ada",
                    "panel 240px dan padding 40px, kolom isi di jendela 800px cuma dapat",
                    "520px. Jadi hitung, jangan dikira-kira.",
                    "",
                    "Akibat salah hitung sering kebalikan dari dugaanmu. Jendela yang",
                    "dilebarkan malah bikin kolom baca makin sempit, karena kolom ketiga",
                    "muncul sebelum ruangnya cukup. Tulis hitungannya sebagai komentar",
                    "tepat di atas tiap @media. Tiga bulan lagi kamu nggak perlu menebak",
                    "dari mana angkanya.",
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
                    "Taruh blok @media di bawah aturan yang mau ditimpanya. Paling aman di",
                    "bagian paling bawah berkas.",
                    "",
                    "Media query nggak menambah spesifisitas sama sekali. Jadi",
                    "@media (max-width: 720px) { .x { padding: 8px } } yang ditulis di",
                    "tengah berkas kalah oleh .x { padding: 24px } yang ditulis sesudahnya.",
                    "Nggak ada pesan error. Tata letak ponselnya cuma nggak berlaku, dan",
                    "kamu bisa lama nyari kesalahan di dalam media query yang padahal udah",
                    "benar.",
                    "",
                    "Banyak kasus yang ternyata nggak butuh media query sama sekali:",
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
                    "Dua yang terakhir pakai min() dan clamp(). Keduanya, ditambah max(),",
                    "udah dijelaskan lengkap di materi Satuan Lanjut dan Menghitung di",
                    "Dalam CSS. Kalau sebuah ambang cuma kamu pakai untuk mengubah satu",
                    "angka, hampir selalu ada bentuk clamp() yang bisa menggantikannya.",
                    "Bentuk tanpa ambang itu nggak pernah meleset di lebar yang kebetulan",
                    "nggak sempat kamu uji.",
                    "",
                    "Media query juga bisa menanyakan pilihan pemakainya:",
                    "",
                    "  @media (prefers-reduced-motion: reduce) { ... }",
                    "    Orang yang gampang pusing karena gerakan menyalakan setelan",
                    "    ini di sistem operasinya. Matikan animasi di dalam blok ini.",
                    "    Buat sebagian orang, animasi yang nggak diminta bikin mual.",
                    "",
                    "  @media (prefers-color-scheme: dark) { ... }",
                    "    Pemakai memilih tema gelap di sistemnya. Materi berikutnya",
                    "    nunjukin cara menjawabnya dengan rapi lewat variabel.",
                    "",
                    "Media query juga bisa menanyakan alat yang dipakai, nggak cuma",
                    "lebarnya:",
                    "",
                    "  @media (hover: hover) { ... }",
                    "    Alatnya punya penunjuk yang bisa melayang di atas sesuatu",
                    "    tanpa menekannya - tetikus atau touchpad, bukan jari.",
                    "  @media (pointer: coarse) { ... }",
                    "    Penunjuknya kasar, yaitu jari di layar sentuh. Lawannya",
                    "    (pointer: fine) untuk tetikus dan pena.",
                    "",
                    "Kenapa (hover: hover) perlu? Ini bug yang hampir pasti kamu temui",
                    "begitu halamanmu dibuka di ponsel. Di layar sentuh nggak ada",
                    "\"melayang di atas\". Browser mengakalinya dengan menyalakan :hover",
                    "waktu elemen disentuh, lalu membiarkannya tetap menyala sampai orang",
                    "menyentuh tempat lain. Akibatnya tombol yang udah ditekan kelihatan",
                    "masih tersorot, menu turun nggak mau menutup, dan di kodemu nggak ada",
                    "yang kelihatan salah.",
                    "",
                    "Obatnya: kasih gaya :hover cuma ke alat yang memang bisa hover.",
                    "",
                    "  @media (hover: hover) {",
                    "    .kartu:hover { box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15); }",
                    "  }",
                    "",
                    "Di layar sentuh, aturan itu nggak pernah menyala, jadi nggak ada yang",
                    "bisa nyangkut. Untuk keadaan yang harus tetap kelihatan di kedua",
                    "jenis alat, pakai :active atau :focus-visible, jangan :hover.",
                    "",
                    "(pointer: coarse) berguna untuk hal lain. Jari butuh sasaran yang",
                    "lebih besar daripada ujung panah tetikus. Naikkan padding tombol dan",
                    "jarak antar item menu di dalam blok itu, supaya menunya tetap nyaman",
                    "dipakai di ponsel.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Pembeli toko online banyak yang membuka halamannya dari ponsel,",
                    "sementara admin mengurus pesanan dari laptop. Halaman yang sama harus",
                    "berganti susunan di lebar tertentu, dan angka lebar itu dihitung dari",
                    "isinya, nggak diambil dari daftar ukuran ponsel.",
                    "",
                    "Kasus kecil: halaman pesan-antar kafe menampilkan daftar menu dan",
                    "keranjang. Di ponsel keduanya menumpuk. Di layar lebar, keranjang",
                    "selebar 280px pindah ke kanan menu. Daftar menu butuh minimal 400px",
                    "supaya nama dan harganya nggak patah, jarak antarkolom 24px, dan",
                    "halaman punya padding 16px di kiri dan kanan.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tulis gaya dasar untuk layar sempit dulu (mobile first): satu",
                    "     kolom, semuanya menumpuk.",
                    "  2. Hitung ambangnya dari isi: 400 + 24 + 280 + 32 = 736px. Tulis",
                    "     hitungannya sebagai komentar di atas blok @media:",
                    "      /* 736px = menu 400 + jarak 24 + keranjang 280 + padding 32 */",
                    "      @media (min-width: 736px) {",
                    "        .halaman { grid-template-columns: 1fr 280px; gap: 24px; }",
                    "      }",
                    "  3. Taruh blok @media di paling bawah berkas, sesudah aturan yang",
                    "     mau ditimpanya. Media query nggak menambah spesifisitas.",
                    "  4. Periksa kasus pinggir: kalau di ponsel yang muncul malah dua",
                    "     kolom berhuruf kecil sekali, cek <meta name=\"viewport\"> di",
                    "     <head>. Tanpa baris itu ponsel menganggap layarnya 980px, jadi",
                    "     ambang 736px ikut menyala.",
                ]
            },
        ],
    },
    {
        "title": "23. Variabel CSS dan Cara Menata Berkas Gaya",
        "sections": [
            {
                "body": [
                    "Variabel CSS adalah nilai yang kamu kasih nama, supaya bisa dipakai di",
                    "banyak tempat. Nama resminya custom property. Namanya ditulis dengan",
                    "dua tanda minus di depan, dan nilainya dibaca pakai var():",
                    "",
                    "  :root {",
                    "    --warna-utama: #1a4fa0;",
                    "  }",
                    "",
                    "  .tombol { background: var(--warna-utama); }",
                    "",
                    ":root itu elemen <html>. Kalau variabel ditaruh di situ, seluruh",
                    "halaman bisa membacanya, karena variabel diwariskan ke anak-anaknya,",
                    "persis seperti properti teks di materi Teks dan Font.",
                    "",
                    "Kamu bisa kasih nilai cadangan, untuk jaga-jaga kalau variabelnya",
                    "ternyata belum ada:",
                    "  color: var(--warna-teks, #222);",
                    "",
                    "Bedanya dengan variabel di Sass atau Less",
                    "",
                    "Sass dan Less itu alat yang mengubah berkas gaya jadi CSS biasa",
                    "sebelum dikirim ke browser. Variabel CSS masih hidup waktu halaman",
                    "berjalan. Nilainya bisa diubah per bagian halaman, diubah oleh media",
                    "query, atau diganti JavaScript dengan satu baris. Variabel Sass udah",
                    "habis dipakai sebelum berkasnya sampai ke browser. Yang tiba di sana",
                    "cuma hasil akhirnya, dan nggak ada lagi yang bisa diubah.",
                    "",
                    "Karena itu, tema gelap cukup ditulis sekali, di satu tempat.",
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
                    "Coba perhatikan: di contoh itu, nggak ada satu pun aturan .kartu yang",
                    "ditulis dua kali. Untuk mengganti tema seluruh halaman, kamu cukup",
                    "mengubah satu atribut di <html>:",
                    "",
                    "  <html data-tema=\"gelap\">",
                    "",
                    "Semua yang membaca var(--latar) langsung ikut berubah, sampai ke",
                    "elemen yang paling dalam. Variabel Sass nggak bisa begini.",
                    "",
                    "Dua sumber tema gelap, dan dua-duanya perlu",
                    "",
                    "Materi Responsif: media query udah janji bakal membahas ini. Ada dua",
                    "pertanyaan berbeda yang gampang dikira sama:",
                    "",
                    "  @media (prefers-color-scheme: dark)",
                    "      SELERA SISTEM. Pemakai menyalakan tema gelap di pengaturan",
                    "      ponsel atau laptopnya. Halamanmu ikut menggelap tanpa ia",
                    "      menyentuh apa pun di halamanmu.",
                    "  [data-tema=\"gelap\"]",
                    "      PILIHAN DI HALAMAN INI. Pemakai menekan tombol tema yang",
                    "      kamu sediakan sendiri.",
                    "",
                    "Untuk menggabungkan keduanya, yang penting cuma urutannya.",
                    "Spesifisitas :root dan [data-tema=\"gelap\"] kebetulan sama persis,",
                    "jadi yang dipakai adalah yang ditulis belakangan. Tulis blok @media",
                    "lebih dulu, lalu blok [data-tema] di bawahnya. Hasilnya sesuai harapan",
                    "orang: halaman ngikutin sistem sampai dia memilih sendiri, dan sesudah",
                    "itu pilihannya yang berlaku.",
                    "",
                    "Kalau urutannya kebalik, tombol temanya kelihatan rusak cuma buat",
                    "pemakai yang sistemnya bertema gelap. Laporan bug semacam ini susah",
                    "dipercaya, karena di komputermu sendiri semuanya kelihatan normal.",
                    "",
                    "Makanya contoh di atas juga punya [data-tema=\"terang\"]. Tanpa blok",
                    "itu, pemakai yang sistemnya gelap lalu menekan tombol \"terang\" nggak",
                    "dapat apa-apa. Yang berlaku tetap @media-nya, karena nggak ada satu",
                    "aturan pun sesudahnya yang membatalkan.",
                    "",
                    "Satu baris yang sering kelupaan: color-scheme",
                    "",
                    "  :root { color-scheme: light dark; }",
                    "",
                    "Variabelmu cuma ngurus yang kamu gambar sendiri. Ada bagian yang",
                    "digambar browser: bilah gulir, kotak centang, pemilih tanggal, dan",
                    "latar di balik halaman sebelum CSS-mu sempat dimuat. Bagian-bagian",
                    "itu nggak membaca var() mana pun. color-scheme ngasih tahu browser",
                    "tema apa yang sedang berlaku, lalu semua kontrol bawaannya ikut",
                    "menggelap. Tanpa baris ini, halamanmu gelap tapi bilah gulirnya putih",
                    "terang di pinggir, dan nggak ada satu properti pun di berkasmu yang",
                    "bisa mewarnainya.",
                    "",
                    "Nilai light dark artinya \"aku bisa dua-duanya, ikuti sistem\". Di blok",
                    "pilihan pemakai, sebut satu aja, misalnya color-scheme: dark di dalam",
                    "[data-tema=\"gelap\"]. Dengan begitu browser nggak salah tebak waktu",
                    "pilihan itu beda dari selera sistemnya.",
                    "",
                    "Jarak juga layak dijadikan variabel, nggak cuma warna",
                    "",
                    "Tangga --s1 sampai --s6 di contoh tadi bukan hiasan. Ruang kosong itu",
                    "bahan bangunan utama sebuah halaman. Halaman yang terasa tenang",
                    "biasanya tenang karena jaraknya, lebih dari karena warnanya. Dengan",
                    "tangga jarak, kelapangan seluruh halaman bisa disetel dari satu",
                    "tempat.",
                    "",
                    "Bayangkan padding: 22px, padding: 15px, dan margin: 19px tersebar di",
                    "lima puluh tempat. Mata nggak bisa lagi menangkap pola jaraknya, dan",
                    "nggak ada satu tempat pun untuk membetulkannya. Angka yang mirip tapi",
                    "nggak sama malah lebih buruk daripada angka yang jelas beda.",
                ]
            },
            {
                "body": [
                    "Urutan isi berkas gaya yang awet dipakai lama:",
                    "",
                    "  1. Reset / setelan dasar   *, box-sizing, margin bawaan dibuang",
                    "  2. Variabel                :root { --... }",
                    "  3. Elemen dasar            body, h1-h6, p, a, img, table",
                    "  4. Tata letak              .halaman, .wadah, .kepala, .sisi",
                    "  5. Komponen                .kartu, .tombol, .lencana, .tabel",
                    "  6. Bantuan (utility)       .tengah, .sembunyi, .lebar-penuh",
                    "  7. Media query             semua @media, di bagian paling bawah",
                    "",
                    "Urutan ini ada alasannya. Kalau spesifisitas seri, CSS memakai aturan",
                    "yang ditulis belakangan. Jadi yang umum taruh di atas, yang khusus di",
                    "bawah. Kalau urutan berkasmu acak, kamu terpaksa terus menaikkan",
                    "spesifisitas cuma untuk menimpa aturanmu sendiri.",
                    "",
                    "Beberapa kebiasaan yang nanti menghemat banyak waktu:",
                    "  - Kasih nama class berdasarkan benda itu apa, jangan berdasarkan",
                    "    rupanya. .peringatan tetap cocok selamanya. .teks-merah jadi",
                    "    menyesatkan begitu kamu memutuskan peringatan berwarna jingga.",
                    "  - Aturan penamaan yang paling banyak dipakai orang punya nama: BEM,",
                    "    bentuknya .blok__elemen--pengubah. Contohnya .kartu, lalu",
                    "    .kartu__judul, lalu .kartu--sorot. Dua garis bawah dibaca \"milik\",",
                    "    dua tanda minus dibaca \"versi\". Hati-hati, dua minus di",
                    "    .kartu--sorot itu bukan variabel CSS, walaupun bentuknya sama",
                    "    dengan --sorot yang barusan kamu tulis di :root. Bedanya cuma di",
                    "    posisinya, dan itu dibahas lengkap di materi Membaca CSS di Proyek",
                    "    Nyata.",
                    "  - Jaga pemilih tetap pendek. .kartu .isi p span susah ditimpa dan",
                    "    terikat ke susunan HTML yang pasti suatu saat berubah. Satu class",
                    "    di elemen yang tepat hampir selalu lebih baik.",
                    "  - Satu komponen, satu blok yang berurutan. Aturan .tombol jangan",
                    "    disebar di tiga tempat berbeda dalam berkas yang sama.",
                    "  - Tulis komentar untuk keputusan, bukan untuk hal yang udah kebaca",
                    "    dari kodenya. /* membulatkan sudut */ nggak ada gunanya.",
                    "    /* 720px = panel 240 + kolom baca 440 + jarak 40 */ menolong",
                    "    siapa pun yang membacanya nanti, termasuk kamu sendiri.",
                    "  - Berkas boleh dipecah (dasar.css, komponen.css) lalu disambung",
                    "    berurutan. Tapi tiap <link> tambahan berarti satu permintaan",
                    "    tambahan sebelum halaman bisa tampil rapi. Untuk proyek belajar,",
                    "    satu berkas lebih gampang dijaga.",
                ]
            },
            {
                "body": [
                    "Daftar periksa kalau sebuah aturan nggak jalan",
                    "",
                    "CSS nggak pernah ngasih pesan error, jadi periksa berurutan, mulai dari",
                    "penyebab yang paling sering:",
                    "",
                    "  1. Berkasnya udah tersambung? Salah nulis href nggak memunculkan",
                    "     pesan apa pun. Halamannya cuma tampil polos.",
                    "  2. Pemilihnya cocok dengan elemen yang kamu maksud? Lupa titik di",
                    "     depan nama class itu kesalahan yang paling sering terjadi.",
                    "  3. Ada aturan lain yang lebih spesifik? (materi 2)",
                    "  4. Ada aturan setara yang ditulis belakangan?",
                    "  5. Nama properti atau nilainya salah ketik? CSS membuang yang nggak",
                    "     dia mengerti tanpa bilang apa-apa.",
                    "  6. Elemennya memang punya ukuran? Elemen inline mengabaikan width",
                    "     dan height, dan elemen kosong sering nggak punya tinggi sama",
                    "     sekali.",
                    "  7. Ada kurung kurawal yang lupa ditutup di aturan sebelumnya? Satu",
                    "     kurawal yang hilang bisa menelan beberapa aturan sesudahnya",
                    "     sekaligus.",
                    "",
                    "Di aplikasi ini, langkah 5 dan 7 bisa langsung dicek. Jalankan berkas",
                    ".css-nya, lalu lihat daftar aturan yang tercetak. Aturan yang nggak",
                    "muncul di daftar itu juga nggak bakal dilihat browser.",
                    "",
                    "Kabar baiknya, hampir semua masalah CSS ujung-ujungnya balik ke tiga",
                    "pertanyaan yang sama:",
                    "  - Kotaknya sebesar apa? (materi Box Model)",
                    "  - Kotaknya ikut alur dokumen atau nggak? (materi Display dan Alur",
                    "    Dokumen, dan materi Position)",
                    "  - Aturan mana yang dipakai browser? (materi 2)",
                    "Kalau kamu bingung, balik ke tiga pertanyaan itu.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Jasa pembuat situs sering memakai satu template toko online untuk",
                    "banyak UMKM sekaligus. Susunannya sama, yang beda cuma warna merek",
                    "tiap toko. Dengan variabel CSS, mengganti warna itu cukup satu baris",
                    "di :root, tanpa menyentuh aturan komponen satu pun.",
                    "",
                    "Kasus kecil: satu template dipakai tiga toko: toko kue (merah bata),",
                    "toko batik (cokelat), dan bengkel (biru). Warna merek muncul di 14",
                    "tempat, mulai dari tombol, tautan, garis kartu, sampai judul.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pahami apa yang beda dan apa yang sama. Yang beda cuma warnanya.",
                    "     Aturan komponennya sama persis di ketiga toko.",
                    "  2. Taruh warna di :root, lalu biarkan komponen membacanya:",
                    "      :root { --merek: #a33b20; }",
                    "      .tombol { background: var(--merek); }",
                    "      .kartu { border-top: 3px solid var(--merek); }",
                    "  3. Tiap toko punya berkas kecil yang ditautkan sesudah template,",
                    "     isinya satu baris, misalnya :root { --merek: #1a4fa0; } untuk",
                    "     bengkel. Spesifisitasnya sama, jadi yang ditulis belakangan",
                    "     dipakai.",
                    "  4. Periksa kasus pinggir: var(--merk) yang salah ketik menggugurkan",
                    "     deklarasinya tanpa pesan, dan tombolnya kehilangan latar. Kasih",
                    "     cadangan, misalnya var(--merek, #333), lalu cek di DevTools.",
                ]
            },
        ],
    },
    {
        "title": "24. Pemilih Modern dan Lapisan Cascade",
        "sections": [
            {
                "body": [
                    "Di materi Pemilih kamu udah belajar menghitung spesifisitas (a, b, c)",
                    "dan tiga pertanyaan cascade. Semuanya masih benar, tapi belum lengkap.",
                    "Beberapa tahun terakhir, CSS menambah tiga pemilih dan satu aturan-at",
                    "(aturan yang diawali @, seperti @media). Keempatnya sekarang ada di",
                    "hampir semua kode nyata, dan tiga di antaranya sengaja mengutak-atik",
                    "angka spesifisitas tadi. Kalau kamu belum kenal, kode orang lain bakal",
                    "kelihatan seperti melanggar aturan yang baru kamu hafal.",
                    "",
                    ":is() memendekkan daftar pemilih",
                    "",
                    "  :is(h1, h2, h3) + p { margin-top: 4px; }",
                    "",
                    "Tanpa :is(), pemilih yang sama harus ditulis tiga kali:",
                    "",
                    "  h1 + p, h2 + p, h3 + p { margin-top: 4px; }",
                    "",
                    "Ini masih belum kerasa. Sekarang kalikan tiga judul dengan tiga wadah:",
                    "",
                    "  .artikel h1, .artikel h2, .artikel h3,",
                    "  .sisi h1,    .sisi h2,    .sisi h3,",
                    "  .kaki h1,    .kaki h2,    .kaki h3 { ... }",
                    "",
                    "  :is(.artikel, .sisi, .kaki) :is(h1, h2, h3) { ... }",
                    "",
                    "Sembilan pemilih jadi satu baris. Kalau besok ada wadah keempat, kamu",
                    "cukup menyisipkan satu kata. Nggak perlu nulis tiga baris lagi sambil",
                    "berharap nggak ada yang kelewat.",
                    "",
                    "Spesifisitas :is() diambil dari argumen terkuat di dalam kurungnya:",
                    "",
                    "  :is(p, #judul)   ->  (1,0,0)",
                    "",
                    "Angka itu tetap berlaku walaupun yang cocok cuma <p> biasa. Jadi satu",
                    "#id yang diselipkan ke daftar itu menaikkan seluruh aturannya ke",
                    "tingkat id, dan sesudah itu nggak ada .class yang bisa menimpanya.",
                    "",
                    ":where() sama persis dengan :is(), kecuali satu hal",
                    "",
                    "  :where(p, #judul)   ->  (0,0,0)",
                    "",
                    "Spesifisitas :where() selalu nol, apa pun isinya. Cuma itu bedanya.",
                    "Elemen yang dipilih sama, cara nulisnya juga sama.",
                    "",
                    "Di materi Pemilih, kamu disarankan mulai dari spesifisitas serendah",
                    "mungkin, supaya aturanmu gampang ditimpa nanti. :where() alat untuk",
                    "itu. Aturan yang dibungkusnya spesifisitasnya nol, jadi satu nama",
                    "elemen polos pun udah cukup untuk menimpanya. Kamu juga nggak perlu",
                    "ingat berkas mana yang disambung lebih dulu. Makanya hampir semua",
                    "reset modern dibungkus :where().",
                    "",
                    "Yang dinolkan cuma isi kurungnya:",
                    "",
                    "  .kartu :where(h3)   ->  (0,1,0), bukan (0,0,0)",
                    "",
                    ".kartu di luar kurung tetap dihitung penuh. Jadi :where() nggak",
                    "mematikan spesifisitas seluruh aturan.",
                ],
            },
            {
                "heading": "Reset dan pemilih ringkas (gaya.css)",
                "body": [
                    "Bandingkan dengan :not(), yang udah dipakai di materi Pseudo-class",
                    "",
                    "  p:not(.penting)     ->  (0,1,1)   :not() IKUT menyumbang",
                    "  p:not(#judul)       ->  (1,0,1)   juga dari argumen terkuatnya",
                    "  p:where(.penting)   ->  (0,0,1)   :where() tidak menyumbang apa pun",
                    "",
                    "Tulisan :not() sendiri nggak dihitung. Yang dihitung isinya. Sekarang",
                    ":not() juga bisa menerima beberapa argumen sekaligus:",
                    "",
                    "  nav:not(.menu, .remah)   sama dengan   nav:not(.menu):not(.remah)",
                    "",
                    "Artinya \"bukan .menu, dan juga bukan .remah\". Gampang kebaca terbalik,",
                    "jadi pelan-pelan bacanya.",
                    "",
                    "Daftar di dalam :is() dan :where() itu pemaaf",
                    "",
                    "Di daftar berkoma biasa, satu pemilih yang nggak dimengerti browser",
                    "membatalkan seluruh aturannya:",
                    "",
                    "  input::-moz-placeholder, input::placeholder { color: #8a8f98; }",
                    "",
                    "Di browser yang nggak kenal bentuk -moz itu, dua-duanya batal",
                    "sekaligus. Gejalanya \"aturannya nggak mempan\", dan ini yang paling",
                    "susah dilacak, karena yang salah justru baris yang nggak kamu curigai.",
                    "Di dalam :is() dan :where(), argumen yang nggak dikenal dibuang",
                    "sendirian, dan sisanya tetap jalan.",
                    "",
                    "Ingat: :not() dan :has() nggak pemaaf. Satu argumen rusak di situ",
                    "tetap membatalkan seluruh aturannya.",
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
                    ":has(), pemilih induk",
                    "",
                    "Semua pemilih di materi Pemilih bergerak ke satu arah: dari luar ke",
                    "dalam (div p), atau dari kiri ke kanan (h2 + p). Nggak ada satu pun",
                    "yang bisa bilang \"tata div ini, kalau di dalamnya ada gambar\". Selama",
                    "dua puluh tahun jawabannya selalu JavaScript: baca isinya, lalu",
                    "tempelkan class ke induknya. :has() bikin cara itu nggak perlu lagi.",
                    "",
                    "  .kartu:has(img)            kartu yang di dalamnya ADA <img>",
                    "  label:has(input:checked)   label yang centangnya sedang aktif",
                    "  body:has(dialog[open])     seluruh halaman selama ada dialog terbuka",
                    "",
                    "Salah paham yang paling sering: yang ditata adalah elemen di sebelah",
                    "kiri titik dua. Isi kurung cuma syarat. Jadi .kartu:has(img) mewarnai",
                    "kartunya, gambarnya nggak ikut.",
                    "",
                    "Isi kurungnya dibaca relatif terhadap elemen itu, jadi kombinator,",
                    "yaitu tanda penghubung seperti > dan +, boleh berdiri sendirian di",
                    "depan:",
                    "",
                    "  .kartu:has(img)     ada <img> di mana pun di dalamnya",
                    "  .kartu:has(> img)   hanya kalau <img> itu anak LANGSUNG",
                    "  h2:has(+ p)         <h2> yang tepat sesudahnya ada <p>",
                    "",
                    "Spesifisitasnya sama seperti :is(), diambil dari argumen terkuat di",
                    "dalam kurung. Tulisan :has() sendiri nggak menambah apa-apa.",
                    "",
                    "Batasannya: :has() nggak boleh ditaruh di dalam :has() lain, dan nggak",
                    "bisa berisi pseudo-element. Hindari juga bentuk yang terlalu luas",
                    "seperti *:has(...). Browser memeriksanya ulang tiap kali isi halaman",
                    "berubah, dan pemilih ini yang paling mungkin bikin halaman terasa",
                    "berat.",
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
                    "@layer: lapisan cascade",
                    "",
                    "Di materi Pemilih, cascade disajikan sebagai tiga pertanyaan. Sekarang",
                    "ada pertanyaan baru, dan pertanyaan ini diajukan sebelum spesifisitas",
                    "dihitung:",
                    "",
                    "  1. Ada yang !important?",
                    "  2. Aturan ini ada di lapisan mana?            <- yang baru",
                    "  3. Mana yang spesifisitasnya lebih tinggi?",
                    "  4. Kalau seri, mana yang ditulis belakangan?",
                    "",
                    "Akibatnya langsung kerasa. Pemilih yang jelas lebih spesifik bisa",
                    "kalah oleh pemilih satu kata, asal lapisannya kalah. Kalau suatu hari",
                    "kamu lihat aturan (1,2,1) dicoret, sementara h3 polos yang dipakai,",
                    "ini penjelasannya. Browsernya nggak rusak, dan hitunganmu juga nggak",
                    "salah.",
                    "",
                    "Bentuknya",
                    "",
                    "  @layer reset, dasar, komponen, utility;",
                    "",
                    "Baris ini ditaruh di paling atas berkas dan nggak menata apa pun.",
                    "Tugasnya cuma menetapkan urutan. Lapisan yang disebut belakangan",
                    "mengalahkan yang disebut lebih dulu.",
                    "",
                    "  @layer komponen {",
                    "    .kartu { padding: 16px; }",
                    "  }",
                    "",
                    "Sesudah urutannya ditetapkan, isi tiap lapisan boleh ditulis di mana",
                    "aja, dalam urutan apa pun, bahkan dipecah jadi beberapa blok. Yang",
                    "berlaku tetap urutan di baris pertama tadi. Gunanya: keputusan \"siapa",
                    "boleh menimpa siapa\" ditulis sekali dan kebaca dari satu baris. Kamu",
                    "nggak perlu menyimpulkannya dari posisi tiga ratus aturan di berkas.",
                    "",
                    "Kalau baris penetapan itu nggak ada, lapisan diurutkan menurut",
                    "kemunculan pertamanya. Akibatnya, menyisipkan @layer baru di tengah",
                    "berkas bisa mengubah hasil tanpa kamu sadari.",
                    "",
                    "Yang paling sering bikin kaget: aturan tanpa lapisan mengalahkan semua",
                    "lapisan",
                    "",
                    "Aturan yang nggak dibungkus @layer dianggap ada di lapisan paling",
                    "akhir, di atas reset, komponen, dan utility. Jadi kalau kamu mikir",
                    "\"taruh di lapisan utility biar paling kuat\", itu keliru. Yang paling",
                    "kuat justru aturan yang nggak berlapis sama sekali.",
                    "",
                    "Ini juga alasan pustaka CSS mulai membungkus dirinya sendiri dalam",
                    "lapisan. Begitu seluruh isi pustaka ada di dalam @layer, CSS-mu yang",
                    "polos otomatis menang, tanpa perlu adu spesifisitas. Untuk berkas",
                    "pihak lain yang nggak bisa kamu sunting, lapisannya dipasang waktu",
                    "mengimpor:",
                    "",
                    "  @import url(\"pustaka.css\") layer(pustaka);",
                    "",
                    "(@import wajib ditaruh di atas semua aturan biasa, tepat sesudah baris",
                    "penetapan urutan lapisan.)",
                    "",
                    "!important membalik urutan lapisan",
                    "",
                    "Untuk deklarasi yang pakai !important, urutannya kebalik. Lapisan yang",
                    "disebut paling awal justru menang, dan aturan tanpa lapisan malah jadi",
                    "yang paling lemah. Cukup tahu aja supaya nggak bingung waktu ketemu.",
                    "Ini bukan alasan untuk lebih sering pakai !important.",
                    "",
                    "Dua bentuk kecil yang bakal kamu temui waktu membaca kode orang:",
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
                    "catatan supaya nggak bingung: pembaca CSS di aplikasi ini sederhana,",
                    "dan nggak kenal aturan-at yang nggak pakai kurung kurawal. Jadi baris",
                    "'@layer reset, pustaka, ...;' bakal tercetak nempel ke @layer",
                    "berikutnya. Browser nggak bingung. Itu cuma soal tampilan di sini.",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Proyek nyata jarang cuma berisi CSS buatan sendiri. Ada berkas",
                    "pustaka untuk slider, kalender, atau pemilih tanggal, yang pemilihnya",
                    "sering panjang dan memakai id. Daripada adu spesifisitas, berkas",
                    "seperti itu sekarang dimasukkan ke @layer, dan reset ditulis dengan",
                    ":where() supaya gampang ditimpa.",
                    "",
                    "Kasus kecil: toko online memakai pustaka.css dari pihak lain untuk",
                    "slider promo. Di dalamnya ada #slider .item h3 { color: #888; }.",
                    "Judul promo harus merah tua, tapi .promo-judul { color: #7a1f1f; }",
                    "selalu kalah, dan kamu nggak boleh menyunting pustaka.css.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Hitung dulu: (1,1,1) lawan (0,1,0). Menaikkan spesifisitasmu",
                    "     atau menambah !important cuma memindahkan masalahnya ke depan.",
                    "  2. Masukkan pustaka ke sebuah lapisan saat diimpor. Aturan yang",
                    "     nggak berlapis otomatis mengalahkan semua lapisan:",
                    "      @import url(\"pustaka.css\") layer(pustaka);",
                    "      .promo-judul { color: #7a1f1f; }",
                    "  3. Taruh @import itu di baris paling atas gaya.css, sebelum aturan",
                    "     biasa. Di tengah berkas, baris itu diabaikan tanpa pesan.",
                    "  4. Periksa kasus pinggir: kalau pustaka menulis color: #888",
                    "     !important, lapisan nggak menolong. Deklarasi !important di",
                    "     lapisan mana pun tetap mengalahkan deklarasi biasa.",
                ]
            },
        ],
    },
    {
        "title": "25. CSS yang Bertahan: Prefiks Vendor, @supports, dan Properti Logis",
        "sections": [
            {
                "body": [
                    "Kalau kamu buka berkas gaya proyek nyata mana pun, cepat atau lambat",
                    "kamu bakal ketemu baris kayak gini:",
                    "",
                    "  -webkit-font-smoothing: antialiased;",
                    "  -moz-osx-font-smoothing: grayscale;",
                    "",
                    "Itu bukan salah ketik, dan bukan variabel CSS juga.",
                    "",
                    "Bedanya tipis kalau dilihat sekilas. Dua-duanya juga sering muncul di",
                    "berkas yang sama, kadang cuma berjarak beberapa baris:",
                    "",
                    "  --warna-utama: #1a4fa0;      DUA tanda minus, lalu nama yang kamu",
                    "                               karang sendiri. Ini variabel dari",
                    "                               materi Variabel CSS, dibaca var().",
                    "  -webkit-appearance: none;    SATU tanda minus, lalu nama mesin",
                    "                               browsernya, lalu nama properti asli.",
                    "",
                    "Yang kedua itu properti CSS sungguhan, cuma versi khusus milik satu",
                    "mesin browser. Namanya prefiks vendor. Prefiks artinya awalan, vendor",
                    "artinya pembuat browsernya. Ada empat yang bakal kamu temui:",
                    "",
                    "  -webkit-   Safari dan Chrome (dan hampir semua browser di ponsel)",
                    "  -moz-      Firefox",
                    "  -ms-       Internet Explorer dan Edge versi lama",
                    "  -o-        Opera versi lama",
                    "",
                    "Kenapa prefiks dulu dibutuhkan",
                    "",
                    "Fitur CSS baru hampir selalu udah dipakai orang sebelum aturan",
                    "resminya selesai ditulis. Pembuat browser pengin orang bisa",
                    "mencobanya. Tapi mereka juga nggak mau halaman yang udah telanjur",
                    "ditulis jadi rusak kalau aturan resminya nanti berubah. Jalan",
                    "tengahnya: fiturnya dipasang dengan nama berprefiks, dan nama tanpa",
                    "prefiks disimpan untuk versi bakunya nanti.",
                    "",
                    "Jadi dulu -webkit-transform artinya \"versi percobaan milik WebKit\".",
                    "Sedangkan transform artinya \"versi yang udah disepakati semua\".",
                    "",
                    "Urutannya: yang berprefiks di atas, yang baku di bawah",
                    "",
                    "  .kotak {",
                    "    -webkit-transform: rotate(3deg);",
                    "    transform: rotate(3deg);",
                    "  }",
                    "",
                    "Browser membuang deklarasi yang nggak dia mengerti tanpa bilang",
                    "apa-apa (ingat materi pertama). Jadi browser lama cuma melihat baris",
                    "pertama. Browser baru melihat dua-duanya, lalu memakai yang terakhir,",
                    "karena dari dua deklarasi yang setara, yang ditulis belakangan yang",
                    "dipakai.",
                    "",
                    "Kalau urutannya dibalik, browser modern malah nyangkut di versi",
                    "percobaan yang udah usang. Dan nggak ada satu pun pesan yang ngasih",
                    "tahu kamu.",
                    "",
                    "Kabar baiknya, kamu hampir nggak pernah perlu menulis prefiks",
                    "sendiri. transform, border-radius, box-shadow, flexbox, dan transition",
                    "udah baku bertahun-tahun tanpa prefiks.",
                    "",
                    "Prefiks yang kamu lihat di sebuah berkas biasanya datang dari salah",
                    "satu dari dua sumber. Bisa sisa kode lama yang nggak pernah",
                    "dibersihkan. Bisa juga tambahan otomatis dari alat bernama",
                    "Autoprefixer waktu proyeknya dibangun.",
                    "Buat kamu artinya sama aja: kamu perlu bisa membacanya, tapi nggak",
                    "perlu menirunya.",
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
                    "@supports: cara CSS bertanya",
                    "",
                    "CSS nggak punya if. Yang paling mirip adalah @supports. Pertanyaannya",
                    "cuma satu macam: \"browser, kamu ngerti deklarasi ini atau nggak?\"",
                    "",
                    "  @supports (display: grid) {",
                    "    .daftar { display: grid; }",
                    "  }",
                    "",
                    "Yang di dalam kurung wajib berupa deklarasi utuh, yaitu properti",
                    "beserta nilainya. Kalau cuma ditulis @supports (display), hasilnya",
                    "selalu dianggap nggak didukung. Memang harus begitu: sebuah browser",
                    "bisa aja ngerti display tapi nggak ngerti grid. Yang menentukan",
                    "jawabannya adalah nilainya, nggak cukup nama propertinya.",
                    "",
                    "Bentuk-bentuk lainnya:",
                    "",
                    "  @supports not (display: grid) { }      kalau TIDAK mengerti",
                    "  @supports (a: b) and (c: d) { }        harus mengerti keduanya",
                    "  @supports (a: b) or (c: d) { }         salah satu saja cukup",
                    "  @supports selector(:has(*)) { }        menanyakan PEMILIH,",
                    "                                         bukan properti",
                    "",
                    "Tiap syarat wajib punya kurungnya sendiri. and juga nggak boleh",
                    "dicampur dengan or tanpa kurung tambahan yang memperjelas maksudmu.",
                    "Tulis begini: ((a: b) and (c: d)) or (e: f).",
                    "",
                    "Bedanya dengan @media",
                    "",
                    "Dua-duanya sering ketuker. Dua-duanya diawali @, menaruh syarat di",
                    "dalam kurung, dan membungkus aturan CSS biasa pakai kurung kurawal.",
                    "Tapi yang ditanyakan beda jauh:",
                    "",
                    "  @media     bertanya tentang LAYAR dan lingkungannya - selebar",
                    "             apa, melintang atau tegak, sedang dicetak, temanya",
                    "             gelap atau terang.",
                    "  @supports  bertanya tentang BROWSERNYA - fitur ini kamu mengerti",
                    "             atau tidak.",
                    "",
                    "Jawaban @media bisa berubah waktu pengguna menyeret sudut jendela",
                    "browsernya. Jawaban @supports nggak pernah berubah selama halamannya",
                    "terbuka. Keduanya boleh ditaruh satu di dalam yang lain:",
                    "",
                    "  @supports (display: grid) {",
                    "    @media (min-width: 720px) { .halaman { gap: 24px; } }",
                    "  }",
                    "",
                    "Yang sederhana dulu, yang bagus belakangan",
                    "",
                    "Tulis versi yang pasti jalan sebagai aturan biasa. Lalu taruh versi",
                    "bagusnya di dalam @supports:",
                    "",
                    "  .daftar { display: block; }           semua browser dapat ini",
                    "  @supports (display: grid) { ... }     yang mampu dapat tambahannya",
                    "",
                    "Gimana kalau dibalik? Versi sederhana ditaruh di dalam",
                    "@supports not(...), dan versi bagusnya di luar. Browser yang terlalu",
                    "tua untuk ngerti @supports bakal melewati seluruh blok itu. Padahal",
                    "browser itulah yang paling butuh versi cadangannya.",
                    "",
                    "Hal yang udah didukung di mana-mana juga nggak perlu dibungkus.",
                    "@supports (display: flex) sekarang cuma nambah satu lapis kurung",
                    "kurawal tanpa manfaat apa pun.",
                    "",
                    "Ingat batasnya: @supports cuma ngecek apakah deklarasinya bisa dibaca",
                    "browser. Dia nggak ngecek apakah hasilnya bagus. Untuk tahu sejak",
                    "versi berapa sebuah fitur aman dipakai, cek di caniuse.com, atau di",
                    "tabel \"Browser compatibility\" di bagian bawah tiap halaman MDN. Hal",
                    "itu nggak bisa ditanyakan dari dalam CSS.",
                ],
            },
            {
                "body": [
                    "Properti logis: kenapa \"kiri\" kurang tepat",
                    "",
                    "Nama seperti margin-left menganggap tulisan selalu mengalir ke kanan.",
                    "Padahal bahasa Arab, Ibrani, dan Persia ditulis dari kanan ke kiri. Di",
                    "halaman seperti itu, kiri adalah akhir baris, dan awal baris ada di",
                    "kanan. Makanya CSS punya satu set nama lagi yang sama sekali nggak",
                    "menyebut arah kiri, kanan, atas, atau bawah.",
                    "",
                    "Dasarnya dua sumbu yang punya nama:",
                    "",
                    "  INLINE   arah teks MENGALIR.     Tulisan Indonesia: mendatar.",
                    "  BLOCK    arah baris BERTAMBAH.   Tulisan Indonesia: menurun.",
                    "",
                    "Nama itu diambil dari hal yang udah kamu kenal di materi Display:",
                    "elemen block bertumpuk ke bawah, elemen inline berbaris ke samping.",
                    "Sumbunya dinamai persis dari situ, jadi nggak ada yang baru untuk",
                    "dihafal.",
                    "",
                    "Tiap sumbu punya awal dan akhir, yaitu start dan end. Untuk tulisan",
                    "Indonesia: inline-start itu kiri, inline-end itu kanan, block-start",
                    "itu atas, dan block-end itu bawah.",
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
                    "Ada satu pasangan yang gampang ketuker, dan kamu harus bisa",
                    "membedakannya:",
                    "",
                    "  padding-block: 1rem;      ATAS dan BAWAH",
                    "  padding-inline: 1rem;     KIRI dan KANAN",
                    "",
                    "Kalau kebalik, kamu salah membaca tata letak seluruh berkas, dan",
                    "layarnya nggak bakal ngasih tahu. Cara ngingatnya pakai kata block",
                    "tadi: elemen block bertumpuk ke bawah, jadi sumbu block arahnya",
                    "menurun.",
                    "",
                    "Bentuk ringkas itu menerima satu atau dua nilai:",
                    "",
                    "  margin-inline: auto;      awal dan akhir sama",
                    "  margin-inline: 0 24px;    awal dulu, baru akhir",
                    "",
                    "margin-inline: auto adalah pengganti margin: 0 auto dari materi Box",
                    "Model, dengan satu beda. margin: 0 auto sekalian bikin margin atas dan",
                    "bawah jadi nol. margin-inline: auto sama sekali nggak menyentuh margin",
                    "atas dan bawah. Syaratnya tetap sama: elemennya harus punya batas",
                    "lebar, jadi max-inline-size tetap wajib ada.",
                    "",
                    "inset menggantikan empat baris sekaligus:",
                    "",
                    "  top: 0; right: 0; bottom: 0; left: 0;   ->   inset: 0;",
                    "",
                    "Artinya elemen itu melebar sampai memenuhi elemen acuannya. Pola ini",
                    "dipakai sehari-hari untuk lapisan gelap di belakang dialog. Urutan",
                    "nilainya sama persis dengan margin: atas, kanan, bawah, kiri. Versi",
                    "logisnya inset-block dan inset-inline.",
                    "",
                    "Syaratnya juga sama dengan top dan left: cuma berlaku untuk elemen",
                    "yang position-nya bukan static (lihat materi Position). Di elemen",
                    "static, inset: 0 nggak ngapa-ngapain.",
                    "",
                    "Jangan campur dua gaya untuk sisi yang sama:",
                    "",
                    "  .kartu { margin-left: 0; margin-inline-start: 16px; }",
                    "",
                    "Di halaman berbahasa Indonesia, dua-duanya menunjuk sisi yang sama.",
                    "Spesifisitas keduanya sama, jadi yang dipakai adalah yang ditulis",
                    "belakangan. Akibatnya, menyisipkan satu baris di tempat yang salah bisa",
                    "mematikan baris di atasnya tanpa ketahuan. Pilih satu gaya, lalu",
                    "pakai itu aja di seluruh berkas.",
                    "",
                    "Nggak semua hal punya versi logis. background-position, box-shadow,",
                    "dan transform masih pakai arah fisik seperti biasa.",
                ],
            },
            {
                "heading": "Satu berkas gaya modern: logis di luar, @supports di dalam",
                "body": [
                    "Kenapa proyek baru pakai semua ini, padahal nggak berencana",
                    "menerjemahkan halamannya? Gampangnya, berkas gaya yang sama langsung",
                    "benar begitu <html dir=\"rtl\"> dipasang, tanpa satu aturan pun ditulis",
                    "ulang. Selain itu, namanya lebih pas dengan maksudmu. Yang kamu mau",
                    "memang jarak di sisi awal teks, dan itu belum tentu kiri layar.",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Situs pesantren, lembaga kursus bahasa, atau toko yang melayani",
                    "pembeli dari Timur Tengah sering punya halaman berbahasa Arab, yang",
                    "ditulis dari kanan ke kiri. Properti logis membuat satu berkas gaya",
                    "melayani dua arah tulisan itu. Di berkas yang sama biasanya ada juga",
                    "@supports dan prefiks vendor untuk browser lama milik pengunjungnya.",
                    "",
                    "Kasus kecil: situs pesantren punya halaman bahasa Indonesia dan",
                    "halaman bahasa Arab (<html dir=\"rtl\">). Kartu pengumuman punya garis",
                    "penanda 4px di kiri dan lencana \"Baru\" di pojok kanan atas. Di",
                    "halaman Arab, garisnya harus pindah ke kanan dan lencananya ke kiri,",
                    "tanpa berkas gaya kedua.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pahami maksud desainnya. Kiri di sini artinya sisi awal teks,",
                    "     kanan artinya sisi akhir teks, dan atas tetap atas.",
                    "  2. Ganti properti fisik dengan versi logisnya. Kartunya tetap",
                    "     position: relative supaya jadi acuan lencana:",
                    "      .pengumuman { border-inline-start: 4px solid #1a4fa0; }",
                    "      .pengumuman .lencana {",
                    "        position: absolute;",
                    "        inset-block-start: 8px;",
                    "        inset-inline-end: 8px;",
                    "      }",
                    "  3. Periksa kasus pinggir: sisa padding-left lama di kartu yang sama.",
                    "     Di halaman Indonesia kelihatan benar, tapi di halaman Arab",
                    "     jaraknya tetap di kiri, jauh dari garis yang udah pindah ke",
                    "     kanan. Ganti jadi padding-inline-start.",
                ]
            },
        ],
    },
    {
        "title": "26. Container Queries dan CSS Nesting",
        "sections": [
            {
                "body": [
                    "Materi \"Responsif: media query\" menjawab satu pertanyaan: seberapa",
                    "lebar layarnya? Masalahnya, komponen yang sama sering dipasang di dua",
                    "tempat berbeda di halaman yang sama. Misalnya di sidebar yang sempit,",
                    "dan di area utama yang lebar.",
                    "",
                    "Media query nggak bisa membedakan dua tempat itu. Dia cuma tahu lebar",
                    "viewport, yaitu lebar area tampilan browser. Dia nggak tahu lebar",
                    "kotak tempat komponennya dipasang.",
                    "",
                    "  @media (min-width: 600px) { .kartu { display: flex; } }",
                    "  Kartu ini jadi flex begitu LAYAR lebih dari 600px - walau kartunya",
                    "  sendiri dipasang di sidebar 250px yang jelas tidak muat.",
                    "",
                    "Container query mengganti pertanyaannya. Yang ditanya sekarang:",
                    "seberapa lebar wadah komponen ini?",
                    "",
                    "Materi ini juga membahas satu cara menulis CSS yang belum dibahas",
                    "sebelumnya, yaitu menyarangkan aturan di dalam aturan lain. Ini",
                    "namanya nesting. CSS modern mendukungnya langsung, tanpa Sass atau",
                    "Less.",
                ],
            },
            {
                "heading": "Container queries: bereaksi ke wadah, bukan ke layar",
                "body": [
                    "Ada dua langkah wajib. Pertama, elemen induknya dinyatakan sebagai",
                    "container. Yang dijadikan container adalah induknya, bukan komponennya",
                    "sendiri:",
                    "",
                    "  .slot-widget { container-type: inline-size; }",
                    "",
                    "container-type: inline-size artinya \"ukur lebar elemen ini, dan",
                    "siapkan untuk ditanya\". Tanpa baris ini, @container di bawah nggak",
                    "punya apa pun untuk diukur, jadi nggak bakal pernah aktif.",
                    "",
                    "Kedua, tulis @container. Bentuknya mirip @media, tapi yang diukur",
                    "adalah wadah terdekat yang punya container-type, bukan layar:",
                    "",
                    "  @container (min-width: 400px) {",
                    "      .widget .judul { font-size: 1.5rem; }",
                    "  }",
                    "",
                    "Container boleh dikasih nama lewat container-name. Ini berguna kalau",
                    "ada beberapa container bersarang dan kamu perlu nunjuk yang mana:",
                    "",
                    "  .slot-widget { container-type: inline-size; container-name: kartu; }",
                    "  @container kartu (min-width: 400px) { ... }",
                    "",
                    "Ada juga satuan cqw, cqh, cqi, dan cqb. Mirip vw dan vh, tapi",
                    "ukurannya relatif ke container, bukan ke viewport. 10cqw artinya 10%",
                    "dari lebar wadahnya. Satuan ini berguna untuk font-size atau jarak",
                    "yang harus ikut membesar dan mengecil bersama wadahnya.",
                    "",
                    "Jebakan: sebuah elemen nggak bisa jadi container untuk dirinya",
                    "sendiri. Aturan di dalam @container cuma mengubah isi container. Dia",
                    "nggak bisa mengubah container itu berdasarkan ukurannya sendiri.",
                    "Kalau bisa, hasilnya lingkaran tanpa ujung: ukurannya berubah, lalu",
                    "aturannya berubah, lalu ukurannya berubah lagi. Makanya browser",
                    "memang nggak mengizinkannya.",
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
                    "Kalau kamu pernah lihat kode Sass atau Less, bentuk ini bakal terasa",
                    "akrab. Bedanya, ini CSS asli. Browser langsung membacanya, tanpa",
                    "langkah build (mengubah kode dulu sebelum dipakai):",
                    "",
                    "  .navigasi {",
                    "      display: flex;",
                    "",
                    "      & a { color: inherit; }",
                    "      &:hover { background: #f0f0f0; }",
                    "  }",
                    "",
                    "Tanda & menunjuk balik ke pemilih induknya, di sini .navigasi.",
                    "",
                    "Kapan & wajib ditulis? Waktu pemilihnya langsung ditempel tanpa spasi,",
                    "misalnya ke pseudo-class atau class lain. &:hover artinya",
                    ".navigasi:hover. Itu beda jauh dengan .navigasi :hover yang pakai",
                    "spasi. Yang pakai spasi nyari keturunan yang lagi di-hover, bukan",
                    ".navigasi itu sendiri.",
                    "",
                    "Kapan & boleh nggak ditulis? Untuk keturunan biasa yang dipisah",
                    "spasi. a { ... } di dalam .navigasi otomatis artinya .navigasi a.",
                    "",
                    "Jebakan: nesting yang dalam ikut menaikkan spesifisitas tiap aturan",
                    "yang dihasilkan, tanpa kelihatan. Sama aja dengan menulis pemilih yang",
                    "panjang secara manual. Tiga tingkat nesting class menghasilkan aturan",
                    "sespesifik tiga class digabung, dan aturan itu susah ditimpa nanti.",
                    "Masalah ini sama dengan yang dibahas di materi \"Pemilih Modern dan",
                    "Lapisan Cascade\" soal :is() dan :where().",
                    "",
                    "Patokan praktisnya: dua tingkat nesting cukup untuk kebanyakan",
                    "komponen. Kalau udah sampai empat tingkat, itu tanda strukturnya perlu",
                    "dipecah, nggak perlu disarangkan makin dalam.",
                    "",
                    "Catatan soal aplikasi ini: pemeriksa latihan CSS di sini (namanya",
                    "struktur.py) belum bisa mengurai nesting di luar at-rule seperti",
                    "@media dan @container. Jadi materi ini nggak punya latihan otomatis",
                    "untuk nesting. Di browser sungguhan, cara menulis ini tetap sah dan",
                    "jalan normal.",
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
                    "Kapan pakai yang mana:",
                    "  - Media query: tata letak seluruh halaman berubah mengikuti ukuran",
                    "    layar. Misalnya sidebar disembunyikan di layar sempit.",
                    "  - Container query: satu komponen harus tampil beda tergantung",
                    "    wadahnya. Dipakai kalau komponen yang sama dipasang di lebih dari",
                    "    satu tempat dengan lebar berbeda, misalnya widget, kartu, atau",
                    "    sidebar.",
                    "  - Nesting: urusannya cara menulis, nggak ada hubungannya dengan",
                    "    kapan aturan aktif. Dipakai untuk mengelompokkan aturan yang",
                    "    berhubungan erat (elemen, pseudo-class-nya, dan turunan",
                    "    langsungnya), supaya kamu nggak mengetik ulang nama class yang",
                    "    sama berkali-kali.",
                    "",
                    "Ketiganya bisa dipakai bareng tanpa bentrok. Container query dan media",
                    "query sering dipakai berdampingan di proyek nyata, dan aturan di dalam",
                    "@container juga boleh ditulis bersarang.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Portal berita dan situs masjid sering memasang widget yang sama di",
                    "dua tempat: di kolom samping yang sempit dan di beranda yang lebar.",
                    "Container query membuat widget itu menyesuaikan diri dengan wadahnya.",
                    "Nesting sering ikut dipakai di berkas komponen seperti ini, supaya",
                    "aturan widget, :hover-nya, dan bagian dalamnya terkumpul di satu",
                    "blok.",
                    "",
                    "Kasus kecil: widget \"Jadwal Salat Hari Ini\" berisi lima waktu salat.",
                    "Widget itu dipasang di kolom samping 260px dan di area utama 700px.",
                    "Di area utama, kelima waktunya harus berjajar mendatar. Dengan",
                    "@media (min-width: 600px), widget di kolom samping laptop ikut",
                    "mendatar, dan nama waktunya berdesakan.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pahami pertanyaannya: yang menentukan susunan adalah lebar wadah",
                    "     widget, bukan lebar layar.",
                    "  2. Hitung ambangnya: tiap waktu kira-kira butuh 80px, ditambah",
                    "     empat jarak 16px, jadi 464px. Bulatkan ke 480px.",
                    "  3. Jadikan induk di tiap tempat sebagai container, lalu tanyakan",
                    "     lebarnya:",
                    "      .slot { container-type: inline-size; }",
                    "      @container (min-width: 480px) {",
                    "        .jadwal { display: flex; gap: 16px; }",
                    "      }",
                    "  4. Periksa kasus pinggir: container-type dipasang di .slot, jangan",
                    "     di .jadwal sendiri. Elemen nggak bisa jadi container untuk",
                    "     dirinya sendiri.",
                ]
            },
        ],
    },
    {
        "title": "27. Membaca CSS di Proyek Nyata",
        "sections": [
            {
                "body": [
                    "Coba buka satu proyek web sungguhan di GitHub, lalu buka berkas",
                    "gayanya. Kemungkinan besar kamu bakal lihat baris kayak gini:",
                    "",
                    "  .kartu-produk__judul--sorot { color: #1a4fa0; }",
                    "",
                    "Kabar baiknya, nggak ada satu pun sintaks baru di baris itu. Itu tetap",
                    "pemilih class biasa dari materi 2. Browser membacanya persis seperti",
                    "membaca .kartu. Yang bikin kelihatan asing cuma nama class-nya, dan",
                    "nama itu dipilih manusia, nggak diwajibkan browser.",
                    "",
                    "BEM: block, element, modifier",
                    "",
                    "BEM adalah kesepakatan cara memberi nama class yang paling banyak",
                    "dipakai orang:",
                    "",
                    "  .kartu                BLOCK    benda utuh yang berdiri sendiri",
                    "  .kartu__judul         ELEMENT  bagian yang cuma ada DI DALAM blok itu",
                    "  .kartu--sorot         MODIFIER varian atau keadaan blok itu",
                    "  .kartu__judul--besar  element yang punya modifier sendiri",
                    "",
                    "Dua garis bawah dibaca \"milik\". Dua tanda minus dibaca \"versi\".",
                    "",
                    "BEM cuma kesepakatan, nggak termasuk sintaks CSS. Browser sama sekali",
                    "nggak kenal BEM. Yang dia lihat cuma nama class panjang berisi garis",
                    "bawah dan tanda minus, dan dua karakter itu memang boleh ada di nama",
                    "class. Nggak ada yang memaksa kamu pakai BEM, dan nggak ada yang",
                    "ngecek.",
                    "",
                    "Salah ketik jadi .kartu_judul (satu garis bawah) tetap CSS yang sah.",
                    "Nggak ada pesan error. Aturannya cuma nggak kena apa-apa karena nggak",
                    "ada elemen yang cocok. Ini persis penyebab nomor 1 di daftar \"aturan",
                    "nggak ngaruh\" di materi 2.",
                    "",
                    "Jebakan: --sorot di sini bukan variabel CSS. Bentuknya persis sama",
                    "dengan custom property (variabel CSS) di materi Variabel CSS, dan",
                    "dua-duanya bakal muncul berdampingan di berkas yang sama. Yang",
                    "membedakan cuma posisinya:",
                    "",
                    "  .kartu--sorot { ... }     dua minus di dalam PEMILIH   -> modifier BEM",
                    "  --sorot: #1a4fa0;         dua minus di posisi PROPERTI -> variabel CSS",
                    "  color: var(--sorot);      dua minus di dalam var()     -> variabel CSS",
                    "",
                    "Variabel CSS selalu berdiri sendiri sebagai sebuah nama, di dalam",
                    "kurung kurawal atau di dalam var(). Modifier BEM selalu nempel di",
                    "belakang nama class, di depan kurung kurawal. Begitu kamu tahu harus",
                    "lihat di mana, dua-duanya nggak bakal ketuker lagi.",
                    "",
                    "Kenapa orang repot-repot pakai BEM",
                    "",
                    "Coba lihat, semua pemilih di atas cuma satu class. Nggak ada",
                    ".kartu .isi h3, nggak ada #id. Artinya semuanya punya spesifisitas",
                    "(0,1,0), alias rata. Kalau spesifisitasnya rata, yang menentukan",
                    "tinggal urutan penulisan (materi 2). Ini jauh lebih gampang diikuti",
                    "daripada pemilih-pemilih yang saling berlomba menimpa. Spesifisitas",
                    "berkasnya tetap rendah, jadi selalu masih ada ruang untuk menimpa.",
                    "",
                    "Untung kedua: nama class menyebut pemiliknya. Lihat .kartu__judul di",
                    "HTML, dan kamu langsung tahu blok mana yang ngurus. Cari .kartu__ di",
                    "berkas gaya, dan semua aturannya ketemu sekaligus. Ini lanjutan",
                    "langsung dari dua saran di materi Variabel CSS: kasih nama berdasarkan",
                    "benda itu apa, dan satu komponen ditulis dalam satu blok berurutan.",
                    "",
                    "Harganya: nama class jadi panjang dan HTML-nya jadi ramai. Orang mau",
                    "bayar harga itu, karena berkas gaya yang udah nggak bisa ditimpa lagi",
                    "jauh lebih repot diurus.",
                ],
            },
            {
                "heading": "Bentuk berkas gaya sebuah proyek kecil",
                "body": [
                    "Berkas gaya proyek nyata bisa sampai seribu baris. Nggak usah dibaca",
                    "dari atas ke bawah kayak novel. Hampir semuanya disusun dengan urutan",
                    "yang sama (lihat materi Variabel CSS), jadi baca aja lompat-lompat:",
                    "",
                    "  1. Cari :root dulu. Daftar variabelnya menggambarkan seluruh sistem",
                    "     desainnya dalam dua puluh baris: berapa warna yang dipakai,",
                    "     seberapa lapang jaraknya, dan sebesar apa lengkungan sudutnya.",
                    "     Sesudah itu kamu udah bisa nebak isi berkasnya sebelum membaca.",
                    "  2. Baru turun ke blok komponen. Cari nama class yang memang kamu",
                    "     lihat di HTML, jangan yang kebetulan lewat di layar.",
                    "  3. @media hampir selalu ada di bagian bawah berkas. Kalau ada yang",
                    "     berubah di layar sempit, jawabannya di situ, bukan di blok",
                    "     komponennya.",
                    "",
                    "Di bagian atas berkas biasanya ada beberapa aturan aneh yang nggak",
                    "ngurus komponen apa pun. Itu namanya reset, dan dijelaskan di bagian",
                    "berikutnya.",
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
                    "Ada tiga hal yang bikin berkas .css sungguhan kelihatan asing.",
                    "",
                    "Yang pertama: aturan di dalam aturan (nesting)",
                    "",
                    "  .kartu {",
                    "    padding: 24px;",
                    "    &:hover { border-color: crimson; }",
                    "    .kartu__judul { color: #1a4fa0; }",
                    "  }",
                    "",
                    "Bertahun-tahun bentuk ini cuma ada di Sass. Sejak 2023, browser besar",
                    "menerimanya di berkas .css biasa, jadi sekarang kamu bakal ketemu",
                    "bentuk ini di dua tempat itu. Artinya sama persis dengan tiga aturan",
                    "datar ini:",
                    "",
                    "  .kartu { padding: 24px; }",
                    "  .kartu:hover { border-color: crimson; }",
                    "  .kartu .kartu__judul { color: #1a4fa0; }",
                    "",
                    "& artinya \"pemilih induknya\", dan ditempel tanpa spasi. Ada atau",
                    "nggaknya & mengubah hasilnya:",
                    "",
                    "  &:hover  ->  .kartu:hover    kartu itu sendiri saat disentuh",
                    "  :hover   ->  .kartu :hover   apa pun DI DALAM kartu saat disentuh",
                    "",
                    "Ini soal spasi yang sama dengan .a.b dan .a .b di materi 2, cuma",
                    "pindah tempat.",
                    "",
                    "Ada satu jebakan yang perlu kamu tahu sekarang, supaya nanti nggak",
                    "bingung. Di CSS biasa, & boleh berdiri sendiri, atau diikuti tanda",
                    "seperti :hover dan .lain. Tapi & nggak boleh ditempeli potongan teks.",
                    "Bentuk &__judul yang sering kamu lihat itu khas Sass, dan nggak sah",
                    "di berkas .css.",
                    "",
                    "Catatan soal aplikasi ini: pembaca CSS di sini masih membaca berkas",
                    "datar. Kalau kamu tekan Jalankan pada berkas bersarang, daftar",
                    "aturannya bakal terbaca kacau. Itu batas alatnya, berkasmu belum tentu",
                    "salah. Browser tetap memahaminya.",
                    "",
                    "Yang kedua: baris-baris aneh di bagian atas berkas",
                    "",
                    "  body, h1, h2, p, figure { margin: 0; }",
                    "  *, *::before, *::after { box-sizing: border-box; }",
                    "",
                    "Ini namanya reset. Ingat materi 1: halaman tanpa CSS pun udah punya",
                    "gaya, karena tiap browser punya lembar gaya bawaan. Gaya bawaan itu",
                    "berguna, tapi sedikit beda antar browser dan sering mengganggu.",
                    "Misalnya margin bawaan <h1> dan <p> bikin jarak yang nggak kamu minta.",
                    "box-sizing bawaan juga bikin padding menambah lebar kotak (lihat",
                    "materi Box Model).",
                    "",
                    "Ada dua aliran, dan namanya sering ketuker:",
                    "  - Reset membuang hampir semua gaya bawaan, lalu kamu bangun dari",
                    "    nol. Yang paling terkenal namanya Meyer reset. Kebanyakan proyek",
                    "    sekarang pakai versi pendek buatan sendiri, kayak dua baris di",
                    "    atas.",
                    "  - Normalize (normalize.css) nggak membuang apa-apa. Dia cuma",
                    "    menyamakan perbedaan antar browser, dan membiarkan gaya bawaan",
                    "    yang masuk akal.",
                    "",
                    "Kalau sebuah halaman tiba-tiba kehilangan semua jarak antar",
                    "paragraf, atau judulnya jadi seukuran teks biasa, cek dulu reset di",
                    "bagian atas berkas, sebelum nyari salahnya di komponen. Reset yang",
                    "membuang gaya bawaan, jadi reset juga yang bertanggung jawab",
                    "mengembalikan yang perlu.",
                    "",
                    "Yang ketiga: berkas satu baris dan nama class acak",
                    "",
                    "  .kartu{padding:24px;border:1px solid #e4e6ea}.kartu__judul{color:#1a4fa0}",
                    "",
                    "Berkas seperti itu sudah diminifikasi. Spasi, baris baru, dan",
                    "komentarnya dibuang supaya ukuran unduhannya kecil. Namanya sering",
                    "berakhiran .min.css, dan di baris terakhirnya kadang nempel",
                    "/*# sourceMappingURL=gaya.css.map */.",
                    "",
                    "Tanda lain bahwa yang kamu baca itu hasil buatan alat, bukan ketikan",
                    "tangan:",
                    "  - nama class seperti Button_root__x7f2 atau css-1q2w3e",
                    "  - berkasnya ada di folder bernama dist/, build/, atau _next/",
                    "  - ada komentar 'generated' atau 'DO NOT EDIT' di bagian atasnya",
                    "",
                    "Jangan sunting berkas seperti itu. Perubahanmu bakal hilang waktu",
                    "proyeknya dibangun ulang, tanpa peringatan apa pun. Cari berkas",
                    "sumbernya. Biasanya ada di folder src/ atau styles/, dengan akhiran",
                    ".css, .scss, atau .module.css. Sunting di situ.",
                ],
            },
            {
                "heading": "gaya.scss dan gaya.css hasil kompilasinya",
                "body": [
                    "Berkas .scss itu bukan CSS",
                    "",
                    "Sass adalah bahasa terpisah yang hasilnya CSS. Berkas .scss nggak bisa",
                    "disambung pakai <link>, karena browser sama sekali nggak ngerti isinya.",
                    "Berkas itu harus dikompilasi (diubah otomatis) dulu jadi berkas .css,",
                    "dan berkas .css itulah yang disambung ke halaman. Jadi yang kamu",
                    "sunting satu berkas, yang dibaca browser berkas lain.",
                    "",
                    "Mungkin kamu ingat, materi 1 bilang CSS nggak punya komentar bentuk",
                    "//. Itu tetap benar. Di berkas .scss kamu bakal lihat // di mana-mana,",
                    "dan itu nggak melanggar apa pun, karena berkas itu memang bukan CSS.",
                    "Komentar // malah nggak ikut ke hasil kompilasinya, sedangkan",
                    "komentar /* */ ikut.",
                    "",
                    "Yang bakal kelihatan asing di dalam berkas .scss:",
                    "  //               komentar satu baris, lenyap saat dikompilasi",
                    "  $sorot: #1a4fa0  variabel Sass, habis dipakai sebelum sampai ke browser",
                    "                   (bedanya dengan var(--...) ada di materi Variabel CSS)",
                    "  @mixin + @include  potongan deklarasi yang bisa ditempel berulang kali",
                    "  @extend          menyalin isi aturan lain ke dalam aturan ini",
                    "  @use / @import   menarik berkas .scss lain jadi satu",
                    "  &__judul         & ditempeli teks -> menyusun nama BEM",
                    "",
                    "Baris terakhir itu yang paling sering bikin bingung. Di dalam blok",
                    ".kartu, &__judul jadi .kartu__judul. Jadi Sass dan BEM saling",
                    "melengkapi, makanya dua-duanya hampir selalu muncul bareng.",
                    "",
                    "Kenapa banyak \"CSS\" di GitHub ternyata .scss? Bertahun-tahun CSS biasa",
                    "belum punya variabel dan aturan bersarang, sedangkan Sass udah punya.",
                    "Sekarang CSS udah punya dua-duanya, tapi berkas lama nggak berubah",
                    "sendiri. Bandingkan dua berkas di bawah. Yang pertama ditulis orang,",
                    "yang kedua dihasilkan mesin dari yang pertama.",
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
                    "Tiga aliran lain yang pasti kamu temui",
                    "",
                    "Yang pertama: utility-first, contohnya Tailwind CSS. Di sini nggak ada",
                    "berkas gaya berisi .kartu sama sekali. Gayanya ditulis langsung di",
                    "atribut class, di HTML atau di JSX:",
                    "",
                    "  <div class=\"flex items-center gap-4 rounded-lg p-6 bg-white\">",
                    "    <h3 class=\"text-lg font-semibold\">Judul</h3>",
                    "  </div>",
                    "",
                    "Tiap nama class di situ artinya tepat satu deklarasi. flex artinya",
                    "display: flex, gap-4 artinya gap: 1rem, p-6 artinya padding: 1.5rem.",
                    "Jadi class di <div> itu bukan bahasa baru. Itu enam deklarasi CSS",
                    "yang semuanya udah kamu kenal, cuma dipanggil pakai nama pendek. Yang",
                    "perlu dihafal cuma kamusnya, dan kamusnya ada di dokumentasi Tailwind.",
                    "",
                    "Yang kedua: CSS Modules. Berkasnya bernama seperti Kartu.module.css,",
                    "isinya CSS biasa dengan nama class pendek seperti .root atau .judul.",
                    "Waktu proyeknya dibangun, tiap nama dikasih akhiran acak supaya nggak",
                    "mungkin bentrok dengan komponen lain. Makanya di halaman jadinya kamu",
                    "lihat class Kartu_root__x7f2. Nama itu nggak diketik siapa pun dan",
                    "berubah tiap kali proyeknya dibangun ulang. Jadi jangan pernah pakai",
                    "nama itu sebagai pemilih di CSS.",
                    "",
                    "Yang ketiga: CSS-in-JS, contohnya styled-components dan Emotion.",
                    "Gayanya ditulis di dalam berkas .js atau .jsx, bukan di berkas .css:",
                    "",
                    "  const Kartu = styled.div`",
                    "    padding: 24px;",
                    "    border-radius: 8px;",
                    "  `;",
                    "",
                    "Isi di antara sepasang tanda petik terbalik (backtick) itu CSS biasa.",
                    "Properti dan nilainya persis sama.",
                    "",
                    "Ketiganya cuma cara menulis yang beda. Bahasanya tetap CSS. Yang",
                    "sampai ke browser tetap hal yang sama: pemilih, properti, nilai,",
                    "cascade, box model, flexbox, grid. Tailwind nggak menghapus",
                    "spesifisitas. CSS Modules nggak mengubah box model. styled-components",
                    "nggak bikin gap: 1rem berarti hal lain.",
                    "",
                    "Jadi nggak ada satu pun yang kamu pelajari di materi-materi",
                    "sebelumnya yang jadi usang. Yang beda cuma di mana teksnya diketik dan",
                    "siapa yang ngasih nama class-nya. Kalau sebuah halaman tampil salah,",
                    "pakai cara apa pun, pertanyaannya tetap tiga yang sama (lihat materi",
                    "Variabel CSS): kotaknya sebesar apa, ikut alur atau nggak, dan aturan",
                    "mana yang dipakai.",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Di hari pertama PKL di tim web, tugas yang paling mungkin kamu terima",
                    "adalah perubahan kecil di proyek yang udah besar: ganti warna tombol,",
                    "rapikan jarak. Yang bikin lama biasanya mencari berkas yang tepat",
                    "untuk disunting, apalagi kalau proyeknya memakai Sass, BEM, dan",
                    "langkah build.",
                    "",
                    "Kasus kecil: kamu diminta mengganti warna tombol \"Checkout\". DevTools",
                    "menunjuk aturannya di dist/app.min.css baris 1, isinya",
                    ".tombol--utama{background:#1a4fa0}. Kamu sunting berkas itu, warnanya",
                    "berubah, lalu besoknya balik lagi sesudah proyeknya dibangun ulang.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Kenali tandanya: folder dist/, akhiran .min.css, dan isi satu",
                    "     baris panjang. Berkas itu buatan alat, jadi jangan disunting.",
                    "  2. Cari sumbernya di src/ atau styles/, biasanya berkas .scss.",
                    "     Mencari .tombol--utama bisa nggak ketemu, karena di Sass nama itu",
                    "     sering ditulis &--utama di dalam blok .tombol.",
                    "  3. Cek apakah warnanya variabel, misalnya $sorot atau",
                    "     var(--warna-sorot). Kalau iya, ganti di satu tempat itu.",
                    "  4. Bangun ulang proyeknya, lalu periksa lagi di DevTools bahwa",
                    "     nilai barunya yang dipakai.",
                ]
            },
        ],
    },
]
