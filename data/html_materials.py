HTML_MATERIALS = [
    {
        "title": "1. Apa Itu HTML & Halaman Pertamamu",
        "sections": [
            {
                "body": [
                    "HTML singkatan dari HyperText Markup Language. Kata yang paling penting",
                    "di situ adalah markup, artinya penandaan. Tugas HTML memang cuma satu:",
                    "menandai arti setiap bagian teks di halaman. Bagian ini judul, bagian",
                    "ini paragraf, yang ini tautan, yang itu gambar.",
                    "",
                    "HTML tidak termasuk bahasa pemrograman.",
                    "  - Di HTML tidak ada if, tidak ada perulangan, dan tidak ada hitungan.",
                    "  - Tidak ada perintah yang dijalankan. Browser membaca berkasnya, lalu",
                    "    menggambar halamannya.",
                    "  - Kalau sebelumnya kamu belajar Python atau Java, lupakan dulu cara",
                    "    berpikir langkah demi langkah. Di HTML kamu menjelaskan isi sebuah",
                    "    dokumen, tidak menyuruh komputer mengerjakan sesuatu.",
                    "",
                    "Halaman web biasanya dibuat dengan tiga bahasa, masing-masing dengan",
                    "tugasnya sendiri:",
                    "  HTML  ->  bagian ini artinya apa",
                    "  CSS   ->  bagian ini tampilannya seperti apa",
                    "  JS    ->  apa yang terjadi kalau bagian ini diklik atau disentuh",
                    "",
                    "Materi ini hanya membahas HTML. Urutan ini ada alasannya: halaman yang",
                    "HTML-nya benar tetap bisa dibaca walaupun belum diberi CSS, sedangkan",
                    "CSS tidak bisa memperbaiki halaman yang HTML-nya berantakan.",
                ]
            },
            {
                "body": [
                    "Satu elemen HTML terdiri dari tiga bagian:",
                    "",
                    "  <p>Halo dunia</p>",
                    "   |     |      |",
                    "   |     |      tag penutup, ditandai garis miring",
                    "   |     isi elemen",
                    "   tag pembuka",
                    "",
                    "p adalah nama elemennya, singkatan dari paragraph. Tulisan di dalam",
                    "kurung sudut seperti <p> dan </p> disebut tag. Tag pembuka, isi, dan",
                    "tag penutup bersama-sama disebut elemen.",
                    "",
                    "Kenapa tag harus ditutup? Tag pembuka cuma berarti \"mulai dari sini\".",
                    "Kalau penutupnya tidak ada, browser tidak tahu elemennya berakhir di",
                    "mana, lalu menebak sendiri.",
                    "",
                    "Browser juga tidak menampilkan pesan error untuk HTML yang salah.",
                    "Halamannya tetap tampil dan kelihatan hampir benar, tapi kamu tidak",
                    "diberi tahu bagian mana yang keliru. Karena itu kesalahan HTML lebih",
                    "susah dicari daripada kesalahan Python, yang langsung menunjukkan baris",
                    "yang salah.",
                    "",
                    "Nama tag boleh ditulis dengan huruf besar atau kecil: <P> dan <p> sama",
                    "saja bagi browser. Biasakan menulis huruf kecil semua, karena begitulah",
                    "kebiasaan hampir semua programmer, dan kode yang seragam lebih mudah",
                    "dibaca.",
                ]
            },
            {
                "heading": "Halaman pertama",
                "code": """<!doctype html>
<html lang="id">
<head>
  <meta charset="utf-8">
  <title>Halaman Pertamaku</title>
</head>
<body>
  <h1>Halo, Dunia!</h1>
  <p>Ini paragraf pertamaku. Aku sedang belajar HTML.</p>
</body>
</html>"""
            },
            {
                "body": [
                    "Penjelasannya baris demi baris:",
                    "",
                    "  <!doctype html>",
                    "    Baris ini memberi tahu browser bahwa halamannya memakai HTML versi",
                    "    sekarang. Ia bukan tag dan bukan elemen. Tulis di baris paling atas.",
                    "    Kalau lupa, browser memakai \"mode kuno\" dan beberapa aturan tata",
                    "    letak berubah tanpa peringatan.",
                    "",
                    "  <html lang=\"id\">",
                    "    Pembungkus seluruh halaman. lang=\"id\" memberi tahu bahwa isinya",
                    "    berbahasa Indonesia. Pembaca layar, aplikasi yang membacakan halaman",
                    "    untuk pengguna tunanetra, memakainya untuk memilih cara melafalkan",
                    "    kata. Tanpa lang, kata \"seduh\" dibacakan dengan logat Inggris.",
                    "",
                    "  <head> ... </head>",
                    "    Keterangan tentang halaman. Isinya tidak tampil di layar.",
                    "",
                    "  <meta charset=\"utf-8\">",
                    "    Menentukan tabel huruf yang dipakai. Tanpa baris ini, huruf beraksen",
                    "    dan tanda kutip melengkung bisa berubah jadi simbol aneh.",
                    "",
                    "  <title>...</title>",
                    "    Judul yang muncul di tab browser dan di hasil mesin pencari.",
                    "",
                    "  <body> ... </body>",
                    "    Semua yang dilihat pengunjung ada di sini.",
                    "",
                    "  <h1> adalah judul utama, <p> adalah paragraf.",
                    "",
                    "Simpan berkasnya dengan nama index.html, lalu klik dua kali. Berkas itu",
                    "akan terbuka di browser. Kamu tidak perlu memasang program apa pun.",
                ]
            },
            {
                "body": [
                    "Saat kamu menjalankan HTML di aplikasi ini, hasilnya selalu disertai",
                    "pohon strukturnya. Di versi web ada juga tab Tampilan yang menggambar",
                    "halamannya seperti di browser. Pohon untuk halaman tadi:",
                    "",
                    "  <!doctype html>",
                    "  html lang=\"id\"",
                    "    head",
                    "      meta charset=\"utf-8\"",
                    "      title \"Halaman Pertamaku\"",
                    "    body",
                    "      h1 \"Halo, Dunia!\"",
                    "      p \"Ini paragraf pertamaku. Aku sedang belajar HTML.\"",
                    "",
                    "Baris yang menjorok berarti elemen itu berada di dalam elemen di atasnya.",
                    "Teks sebuah elemen ditulis dalam tanda kutip ganda di belakang namanya.",
                    "",
                    "Pohon ini berguna karena browser bekerja dengan pohon ini, dan pohonnya",
                    "sering berbeda dari yang kamu bayangkan. Contohnya div yang lupa ditutup:",
                    "",
                    "  <div>",
                    "    <p>Kalimat di dalam kotak.</p>",
                    "  <h2>Judul ini seharusnya di LUAR kotak</h2>",
                    "",
                    "menghasilkan pohon:",
                    "",
                    "  div",
                    "    p \"Kalimat di dalam kotak.\"",
                    "    h2 \"Judul ini seharusnya di LUAR kotak\"",
                    "",
                    "h2 ikut masuk ke dalam div. Di browser bedanya belum kelihatan. Begitu",
                    "div itu diberi warna latar atau dipindah dengan CSS, judulnya ikut",
                    "terbawa, dan penyebabnya susah ditemukan kalau kamu tidak melihat",
                    "pohonnya.",
                ]
            },
            {
                "body": [
                    "Nama pohon itu: DOM",
                    "",
                    "Pohon tadi punya nama resmi, yaitu DOM, singkatan dari Document Object",
                    "Model. Document berarti dokumen. Object karena setiap elemen menjadi",
                    "satu benda yang bisa diubah sendiri-sendiri. Model karena pohon itu",
                    "adalah gambaran dokumenmu yang disimpan browser di memorinya.",
                    "",
                    "Kamu sudah paham isinya, sekarang tinggal tahu namanya. Kata DOM akan",
                    "sering kamu temui di dokumentasi, di pesan error, dan di hampir semua",
                    "tutorial JavaScript. Kalimat seperti \"tambahkan elemennya ke DOM\" atau",
                    "\"DOM-nya belum siap\" membicarakan pohon yang barusan kamu lihat.",
                    "",
                    "Bedakan sejak awal: berkas yang kamu ketik dan DOM adalah dua hal yang",
                    "berbeda. DOM adalah hasil browser membaca berkasmu. Kalau kamu klik",
                    "kanan di halaman lalu pilih Inspect, yang muncul adalah DOM. Di sana tag",
                    "yang lupa ditutup sudah ditutupkan oleh browser, dan elemen yang",
                    "ditambahkan JavaScript sudah ikut muncul.",
                    "",
                    "Jadi kalau halamanmu tampil aneh, bandingkan berkasmu dengan DOM di",
                    "Inspect. Contoh div yang lupa ditutup tadi kelihatan jelas di sana:",
                    "berkasnya menaruh h2 di luar div, tapi di DOM h2 berada di dalam div.",
                    "Yang tampil di layar selalu mengikuti DOM.",
                ]
            },
        ],
    },
    {
        "title": "2. Komentar, Sarang, dan Berburu Kesalahan",
        "sections": [
            {
                "body": [
                    "Komentar adalah tulisan di dalam berkas HTML yang tidak pernah tampil",
                    "di layar. Kamu boleh menaruhnya di mana saja:",
                    "",
                    "  <!-- ini komentar, tidak digambar -->",
                    "",
                    "Semua yang ada di antara <!-- dan --> dilewati browser saat menggambar",
                    "halaman. Isinya bebas.",
                    "",
                    "Bentuknya mirip satu baris lain yang juga diawali <! dan sudah kamu",
                    "kenal:",
                    "",
                    "  <!doctype html>     pengumuman: halaman ini HTML versi sekarang",
                    "  <!-- catatan -->    komentar",
                    "",
                    "Keduanya bukan tag. Keduanya tidak punya nama elemen, tidak punya tag",
                    "penutup, dan tidak muncul di pohon struktur. Baris yang diawali <!",
                    "berisi keterangan tentang dokumen, dan tidak menjadi bagian dari isi",
                    "dokumen.",
                    "",
                    "Jebakan: komentar tidak dihapus dari berkasnya. Komentar ikut terkirim",
                    "utuh ke komputer pengunjung. Siapa pun bisa membacanya lewat klik kanan,",
                    "lalu \"View Page Source\" (Ctrl+U di kebanyakan browser).",
                    "",
                    "Karena itu jangan menaruh kata sandi di komentar. Begitu juga catatan",
                    "seperti \"sementara pakai admin/admin\", alamat halaman yang belum",
                    "diumumkan, atau keluhan tentang klien. Komentar cuma tersembunyi dari",
                    "tampilan halaman. Orang yang membuka sumber halamannya tetap bisa",
                    "membacanya.",
                    "",
                    "Komentar biasanya dipakai untuk tiga hal:",
                    "",
                    "  1. Penanda bagian. Di berkas yang panjang, kamu akan menemukan deretan",
                    "     </div> tanpa keterangan div mana yang sedang ditutup. Sepasang",
                    "     komentar membantu:",
                    "",
                    "       <!-- nav -->   ...isi...   <!-- /nav -->",
                    "",
                    "     Kata di dalamnya bebas kamu pilih. Garis miring di komentar penutup",
                    "     meniru bentuk tag penutup, supaya mata langsung mengenali",
                    "     pasangannya.",
                    "",
                    "  2. Catatan TODO. <!-- TODO: harga belum final --> berada tepat di",
                    "     tempat yang masih perlu dikerjakan, jadi tidak gampang terlupa",
                    "     seperti catatan di kertas terpisah.",
                    "",
                    "  3. Mematikan sebagian halaman untuk sementara. Bungkus bagian itu",
                    "     dengan <!-- dan -->, dan bagian itu hilang dari halaman tanpa perlu",
                    "     dihapus. Cara ini nanti dipakai untuk mencari kesalahan.",
                ],
            },
            {
                "heading": "Penanda bagian dan satu blok yang dimatikan (index.html)",
                "code": """<!doctype html>
<html lang="id">
<head>
  <meta charset="utf-8">
  <title>Toko Bunga Melati</title>
</head>
<body>

  <!-- kepala -->
  <div>
    <h1>Toko Bunga Melati</h1>
    <p>Buka setiap hari pukul 08.00 sampai 17.00.</p>
  </div>
  <!-- /kepala -->

  <!-- isi -->
  <div>
    <h2>Rangkaian hari ini</h2>
    <p>Mawar putih, melati, dan sedap malam.</p>
    <!-- TODO: daftar harga belum ada, tanya pemilik toko dulu -->
  </div>
  <!-- /isi -->

  <!-- Sengaja dimatikan: teksnya belum disetujui.
  <div>
    <h2>Promo</h2>
    <p>Beli dua gratis satu.</p>
  </div>
  -->

</body>
</html>""",
            },
            {
                "body": [
                    "Pohon struktur dari halaman di atas:",
                    "",
                    "  <!doctype html>",
                    "  html lang=\"id\"",
                    "    head",
                    "      meta charset=\"utf-8\"",
                    "      title \"Toko Bunga Melati\"",
                    "    body",
                    "      div",
                    "        h1 \"Toko Bunga Melati\"",
                    "        p \"Buka setiap hari pukul 08.00 sampai 17.00.\"",
                    "      div",
                    "        h2 \"Rangkaian hari ini\"",
                    "        p \"Mawar putih, melati, dan sedap malam.\"",
                    "",
                    "Perhatikan dua hal:",
                    "  - Tidak ada satu pun komentar di pohon itu. Penanda bagian dan TODO",
                    "    hilang, karena komentar bukan elemen.",
                    "  - Bagian Promo juga hilang seluruhnya, termasuk div, h2, dan p-nya.",
                    "    Bagian itu masih ada di berkas, tapi browser menganggapnya tidak",
                    "    ada. Bedanya dengan dihapus: untuk menghidupkannya lagi, kamu cukup",
                    "    membuang dua baris komentar.",
                    "",
                    "Ada dua jebakan saat memakai komentar. Penyebabnya sama: komentar selalu",
                    "berakhir di --> pertama yang ditemukan browser, belum tentu di --> yang",
                    "kamu maksud.",
                    "",
                    "  1. Komentar tidak bisa disarangkan, artinya tidak bisa ditaruh di",
                    "     dalam komentar lain.",
                    "",
                    "       <!-- <!-- catatan dalam --> catatan luar -->",
                    "",
                    "     Komentarnya dimulai di <!-- yang pertama dan berakhir di --> yang",
                    "     pertama. Sisanya, yaitu tulisan catatan luar -->, sudah bukan",
                    "     komentar lagi. Tulisan itu tampil sebagai teks biasa di halaman.",
                    "",
                    "     Jadi sebelum mematikan sebuah bagian, periksa dulu apakah di",
                    "     dalamnya sudah ada komentar. Kalau ada, sebagian isi bagian itu",
                    "     tetap tampil di layar.",
                    "",
                    "  2. Tanda -- tidak boleh ada di dalam komentar.",
                    "",
                    "       <!-- gunakan tanda --> untuk menutup -->",
                    "",
                    "     Masalahnya sama: komentar berakhir di --> yang di tengah, lalu",
                    "     tulisan untuk menutup --> tampil di halaman. Tanda -- yang tidak",
                    "     diikuti > biasanya masih dimaafkan browser, tapi aturan resmi HTML",
                    "     melarangnya dan validator W3C menandainya sebagai error. Bedanya",
                    "     dengan yang merusak halaman cuma satu karakter >, jadi biasakan",
                    "     tidak menulis -- di dalam komentar sama sekali. Untuk rentang",
                    "     angka, tulis \"10 sampai 20\", bukan \"10--20\".",
                    "",
                    "Sampai di sini semuanya soal komentar. Kesalahan berikutnya jauh lebih",
                    "sering terjadi dan tidak ada hubungannya dengan komentar, yaitu urutan",
                    "menutup tag. Coba tebak dulu beda dua baris di bawah ini sebelum membaca",
                    "penjelasannya.",
                ],
            },
            {
                "heading": "Urutan menutup tag: salah dan benar",
                "code": """<!-- SALAH: p ditutup duluan, tagnya jadi bersilangan -->
<p><strong>Penting</p></strong>

<!-- BENAR: strong dibuka terakhir, jadi ditutup lebih dulu -->
<p><strong>Penting</strong></p>""",
            },
            {
                "body": [
                    "Elemen yang bersarang, artinya berada di dalam elemen lain, mirip kotak",
                    "di dalam kotak. Sebuah kotak bisa berada seluruhnya di dalam kotak lain,",
                    "atau seluruhnya di luar. Dua kotak tidak mungkin saling menembus.",
                    "",
                    "Dari situ muncul aturan yang berlaku untuk semua elemen: yang dibuka",
                    "terakhir harus ditutup paling dulu. Urutan tag penutup selalu kebalikan",
                    "dari urutan tag pembukanya:",
                    "",
                    "  <div><p><strong>Halo</strong></p></div>",
                    "    1   2    3            3      2    1",
                    "",
                    "Mirip tumpukan piring. Piring yang terakhir kamu taruh adalah piring",
                    "yang pertama bisa kamu ambil. Kamu tidak bisa mengambil piring di tengah",
                    "tanpa mengangkat piring di atasnya dulu.",
                    "",
                    "Baris <p><strong>Penting</p></strong> melanggar aturan itu. Browser",
                    "tidak menampilkan error. Browser menebak, dan hasil tebakannya adalah",
                    "pohon ini:",
                    "",
                    "  p",
                    "    strong \"Penting\"",
                    "",
                    "disertai dua keluhan:",
                    "",
                    "  <strong> dibuka tapi tidak pernah ditutup",
                    "  </strong> menutup sesuatu yang tidak pernah dibuka",
                    "",
                    "Begini urutan kejadiannya. Saat </p> datang, strong masih terbuka, jadi",
                    "browser menutup strong sekalian bersama p. Sesudah itu </strong> datang,",
                    "padahal sudah tidak ada strong yang terbuka, jadi tag itu dibuang. Di",
                    "contoh sekecil ini akibatnya belum terasa. Kalau elemen yang salah tutup",
                    "membungkus setengah halaman, setengah halaman itu ikut pindah ke tempat",
                    "yang salah.",
                    "",
                    "Indentasi membantumu melihat kesalahan seperti ini. Tulis setiap tag",
                    "penutup lurus di bawah tag pembukanya. Kalau ada tag penutup yang tidak",
                    "sejajar dengan pembukanya, atau ada baris yang menjorok lebih dalam dari",
                    "dugaanmu, biasanya kesalahannya ada di situ. Browser tidak akan",
                    "memberitahumu, jadi kerapian kodemu sendiri yang menjadi petunjuk.",
                    "",
                    "Mencari kesalahan dengan komentar",
                    "",
                    "HTML tidak punya debugger, yaitu alat untuk menjalankan kode baris demi",
                    "baris, dan tidak punya pesan error yang menyebut nomor baris. Cara yang",
                    "bisa kamu pakai adalah membagi dua: matikan separuh halaman, lalu lihat",
                    "apa yang berubah. Cara ini dipakai programmer di semua bahasa.",
                    "",
                    "  1. Matikan separuh isi <body> dengan <!-- dan -->.",
                    "  2. Lihat hasilnya. Apakah masalahnya masih ada?",
                    "       masih ada  ->  penyebabnya di separuh yang masih hidup",
                    "       hilang     ->  penyebabnya di separuh yang baru kamu matikan",
                    "  3. Ambil separuh yang bermasalah, bagi dua lagi. Ulangi.",
                    "",
                    "Dengan cara ini, penyebab masalah di halaman 200 baris ketemu dalam",
                    "sekitar delapan langkah, karena setiap langkah membuang setengah tempat",
                    "yang perlu diperiksa.",
                    "",
                    "Saat memakai cara ini:",
                    "  - Hidupkan lagi semua bagian yang kamu matikan sesudah selesai. Bagian",
                    "    yang lupa dihidupkan akan menjadi kesalahan baru.",
                    "  - Ingat jebakan nomor 1 tadi: bagian yang di dalamnya sudah ada",
                    "    komentar tidak bisa dimatikan begitu saja.",
                ],
            },
        ],
    },
    {
        "title": "3. Struktur Dokumen: head dan body",
        "sections": [
            {
                "body": [
                    "Setiap halaman HTML punya dua bagian besar, dan isinya tidak boleh",
                    "tertukar:",
                    "",
                    "  <head>  keterangan tentang halaman. Tidak terlihat di layar.",
                    "  <body>  isi halaman. Bagian yang dilihat orang.",
                    "",
                    "Bayangkan sebuah buku. head itu seperti sampul dan halaman hak cipta,",
                    "body itu isi ceritanya. Judul buku tertulis di sampul, tapi kamu tidak",
                    "membacanya sebagai bagian dari cerita.",
                    "",
                    "Urutannya selalu begini:",
                    "",
                    "  <!doctype html>",
                    "  <html lang=\"id\">",
                    "  <head>   ... </head>",
                    "  <body>   ... </body>",
                    "  </html>",
                    "",
                    "Kesalahan tempat yang paling sering terjadi:",
                    "  - <h1> ditaruh di dalam <head>. Akibatnya judul itu tidak muncul sama",
                    "    sekali.",
                    "  - <title> ditaruh di dalam <body>. Akibatnya tab browser kosong.",
                    "  - <body> dibuka padahal </head> belum ditutup.",
                    "",
                    "Kalau ada bagian yang tidak muncul padahal kodenya jelas ada, periksa",
                    "dulu apakah bagian itu tersasar ke dalam head.",
                ]
            },
            {
                "heading": "Kerangka yang dipakai sungguhan",
                "code": """<!doctype html>
<html lang="id">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Warung Kopi Pagi</title>
  <link rel="stylesheet" href="gaya.css">
</head>
<body>
  <h1>Warung Kopi Pagi</h1>
  <p>Buka setiap hari pukul 07.00 sampai 21.00.</p>
</body>
</html>"""
            },
            {
                "body": [
                    "Isi head, satu per satu:",
                    "",
                    "  <meta charset=\"utf-8\">",
                    "    Selalu taruh paling atas di dalam head. Browser mulai menebak tabel",
                    "    hurufnya sejak awal berkas. Kalau keterangan ini datang terlambat,",
                    "    tebakan browser sudah telanjur dipakai.",
                    "",
                    "  <meta name=\"viewport\" content=\"width=device-width, ...\">",
                    "    Untuk ponsel. Tanpa baris ini, ponsel menganggap layarnya selebar",
                    "    980 piksel, lalu mengecilkan seluruh halaman sampai hurufnya terlalu",
                    "    kecil untuk dibaca. Kalau halamanmu tampil kecil sekali di ponsel,",
                    "    biasanya baris ini yang hilang, dan CSS-nya tidak salah apa-apa.",
                    "",
                    "  <title>",
                    "    Wajib ada, satu per halaman.",
                    "",
                    "  <link rel=\"stylesheet\" href=\"gaya.css\">",
                    "    Menyambungkan halaman ke berkas CSS. rel menyebut hubungannya (di",
                    "    sini: lembar gaya), href menyebut letak berkasnya.",
                    "",
                    "Elemen yang boleh ada di dalam head: meta, title, link, style, script,",
                    "dan base. Elemen lain taruh di body.",
                ]
            },
            {
                "body": [
                    "Elemen di dalam body terbagi dua golongan.",
                    "",
                    "Elemen blok",
                    "  - Selalu mulai di baris baru dan memakai lebar penuh yang tersedia.",
                    "  - Contohnya p, h1 sampai h6, div, ul, li, table, section, article.",
                    "",
                    "Elemen sebaris (inline)",
                    "  - Mengalir di tengah kalimat, dan lebarnya sebesar isinya saja.",
                    "  - Contohnya a, span, strong, em, img, code, small.",
                    "",
                    "Ingat aturan ini, karena banyak kebingungan bermula dari sini:",
                    "  Elemen sebaris boleh ada di dalam elemen blok.",
                    "  Elemen blok tidak boleh ada di dalam elemen sebaris.",
                    "",
                    "  <p>Baca <a href=\"menu.html\">menu</a> kami.</p>   BENAR",
                    "  <span><p>Menu</p></span>                         SALAH",
                    "",
                    "Ada satu pengecualian yang sering membingungkan: <p> tidak boleh berisi",
                    "<div>. Kalau kamu menulisnya, browser menutup <p> lebih dulu tanpa",
                    "memberitahumu, sehingga pohonnya berbeda dari yang kamu ketik.",
                    "",
                    "Pengecualian besar: <a>",
                    "",
                    "Aturan \"blok tidak boleh di dalam sebaris\" tidak berlaku untuk <a>.",
                    "Sejak HTML5, <a> boleh membungkus elemen apa saja yang boleh berdiri di",
                    "tempat <a> itu berdiri. Istilah resminya model konten transparan: saat",
                    "browser memeriksa aturan sarang, <a> dianggap tidak ada.",
                    "",
                    "Gunanya untuk membuat kartu yang bisa diklik di bagian mana saja.",
                    "",
                    "  (Contoh di bawah memakai class, <img>, dan <h3>, yang baru dibahas",
                    "  di materi berikutnya. Untuk sekarang, cukup perhatikan apa saja yang",
                    "  ada di dalam <a>.)",
                    "",
                    "  <a class=\"kartu\" href=\"tubruk.html\">",
                    "    <img src=\"gambar/tubruk.jpg\" alt=\"\" width=\"320\" height=\"180\">",
                    "    <h3>Kopi Tubruk</h3>",
                    "    <p>Kopi diseduh langsung di dalam gelas.</p>",
                    "  </a>",
                    "",
                    "Bentuk seperti ini ada di hampir semua situs yang menampilkan daftar",
                    "artikel, produk, atau menu. Seluruh kotak bisa diklik, dan pembaca layar",
                    "tetap membacanya sebagai satu tautan berisi judul dan ringkasannya.",
                    "Kalau tautannya cuma dipasang di judul, orang harus mengeklik tulisan",
                    "yang kecil, dan di ponsel itu merepotkan.",
                    "",
                    "Yang tetap tidak boleh: <a> di dalam <a>, dan <button> di dalam <a>.",
                    "Sesuatu yang bisa diklik tidak boleh berada di dalam sesuatu yang juga",
                    "bisa diklik, karena browser tidak bisa memutuskan mana yang kamu maksud.",
                    "",
                    "Satu lagi, karena sering dikira kesalahan: <a> tanpa href itu sah.",
                    "Biasanya dipakai untuk tautan yang sedang dimatikan, misalnya nomor",
                    "halaman yang sedang dibuka. Tanpa href, <a> bukan tautan lagi. Ia hanya",
                    "teks yang dibungkus <a>, tidak bisa diklik, dan dilewati saat pengguna",
                    "berpindah-pindah dengan tombol Tab.",
                ]
            },
            {
                "heading": "Spasi dan baris baru dipadatkan",
                "code": """<p>Baris     ini     punya     banyak     spasi.</p>

<p>Baris ini
ditulis
di tiga baris berbeda.</p>

<p>Alamat:<br>
Jalan Melati 7<br>
Bandung</p>"""
            },
            {
                "body": [
                    "Pohon strukturnya:",
                    "",
                    "  p \"Baris ini punya banyak spasi.\"",
                    "  p \"Baris ini ditulis di tiga baris berbeda.\"",
                    "  p \"Alamat: Jalan Melati 7 Bandung\"",
                    "    br",
                    "    br",
                    "",
                    "Dua paragraf pertama isinya sama persis, padahal yang satu ditulis",
                    "dengan banyak spasi dan yang satu ditulis di tiga baris.",
                    "",
                    "Beberapa spasi berturut-turut selalu dipadatkan jadi satu spasi.",
                    "Menekan Enter di berkas HTML juga tidak membuat baris baru di layar.",
                    "",
                    "Aturan ini sengaja dibuat supaya kamu bebas merapikan kode tanpa",
                    "mengubah hasilnya. Indentasi di HTML hanya untuk memudahkan manusia",
                    "membaca.",
                    "",
                    "Kalau kamu memang butuh pindah baris:",
                    "  <br>   pindah baris di dalam satu paragraf (alamat, puisi)",
                    "  <p>    paragraf baru",
                    "  <pre>  blok yang spasi dan barisnya dipertahankan apa adanya",
                    "",
                    "Jebakan: jangan pakai <br><br> untuk memberi jarak antar paragraf. <br>",
                    "artinya \"kalimat ini bersambung di baris berikutnya\", bukan \"beri",
                    "jarak\". Jarak diatur dengan CSS. Dua paragraf yang berbeda ditulis",
                    "dengan dua <p>. Dengan begitu pembaca layar juga bisa melompat dari",
                    "satu paragraf ke paragraf berikutnya.",
                ]
            },
        ],
    },
    {
        "title": "4. Teks: Heading, Paragraf, dan Penekanan",
        "sections": [
            {
                "body": [
                    "Heading adalah judul bagian. HTML punya enam tingkat heading, dari h1",
                    "sampai h6:",
                    "",
                    "  <h1>  judul halaman        paling penting",
                    "  <h2>  bab",
                    "  <h3>  sub-bab",
                    "  ...",
                    "  <h6>  paling dalam         jarang terpakai",
                    "",
                    "Pilih heading berdasarkan kedudukannya di kerangka dokumen, bukan",
                    "berdasarkan ukuran hurufnya. Browser memang menggambar h1 paling besar,",
                    "tapi ukuran huruf bisa diubah dengan CSS kapan saja.",
                    "",
                    "Kerangka heading dipakai oleh dua pihak:",
                    "  - Pembaca layar punya perintah \"lompat ke heading berikutnya\". Bagi",
                    "    pengguna tunanetra, daftar heading berfungsi sebagai daftar isi",
                    "    halaman.",
                    "  - Mesin pencari membaca kerangka itu untuk memahami isi halaman.",
                    "",
                    "Dua aturannya:",
                    "  1. Satu <h1> per halaman, yaitu judul halaman itu.",
                    "  2. Jangan melompati tingkat. Sesudah h2 boleh h3, tapi jangan langsung",
                    "     h4.",
                    "",
                    "Butuh judul yang hurufnya kecil? Tetap pakai tingkat heading yang benar,",
                    "lalu kecilkan hurufnya dengan CSS. Jangan memilih h4 hanya supaya",
                    "hurufnya kecil.",
                ]
            },
            {
                "heading": "Heading dan paragraf",
                "code": """<h1>Panduan Menyeduh Kopi</h1>
<p>Semua yang kamu perlukan untuk gelas pertama yang layak minum.</p>

<h2>Alat yang dibutuhkan</h2>
<p>Cuma tiga benda: penggiling, penyaring, dan teko leher angsa.</p>

<h3>Penggiling</h3>
<p>Giling biji tepat sebelum diseduh, bukan sehari sebelumnya.</p>

<h3>Penyaring</h3>
<p>Kertas atau logam, keduanya bekerja. Rasanya sedikit berbeda.</p>

<h2>Langkah menyeduh</h2>
<p>Panaskan air sampai 92 derajat, tuang perlahan, tunggu tiga menit.</p>"""
            },
            {
                "heading": "Menekankan bagian kalimat",
                "code": """<p>Air <strong>wajib</strong> di bawah 96 derajat.</p>
<p>Namanya <em>pour over</em>, bukan drip.</p>

<p>Merek <b>Kopi Pagi</b> memakai biji dari Gayo.</p>
<p>Kata <i>latte</i> berasal dari bahasa Italia.</p>

<p>Harga lama <del>25.000</del> sekarang <ins>19.000</ins>.</p>
<p>Ketik <code>npm install</code> lalu tekan Enter.</p>
<p>Diskon berlaku <mark>sampai Jumat</mark>.</p>
<p>Rumus air: 15 gram bubuk : 250 ml air <small>(perbandingan 1:16)</small>.</p>"""
            },
            {
                "body": [
                    "Kenapa <b> dan <strong> dibedakan",
                    "",
                    "Di layar keduanya sama-sama tebal. Yang berbeda adalah artinya.",
                    "",
                    "  <strong>  isinya penting. Ada akibatnya kalau dilewatkan.",
                    "  <b>       isinya cuma perlu menonjol, tidak lebih penting.",
                    "",
                    "Bedanya terasa saat halaman dibacakan. Pembaca layar menekankan suaranya",
                    "untuk <strong> dan membaca <b> dengan nada biasa. Peringatan \"air wajib",
                    "di bawah 96 derajat\" yang ditulis dengan <b> akan dibacakan seperti",
                    "kalimat biasa dan mudah terlewat.",
                    "",
                    "Hal yang sama berlaku untuk pasangan berikutnya:",
                    "  <em>  penekanan yang mengubah arti kalimat.",
                    "        \"Aku <em>tidak</em> bilang begitu.\"",
                    "  <i>   huruf miring karena kebiasaan penulisan: istilah asing,",
                    "        nama ilmiah, nama kapal.",
                    "",
                    "Kalau ragu, pakai <strong> dan <em>, karena keduanya membawa arti.",
                    "",
                    "Elemen <center>, <font>, dan <big> sudah tidak dipakai lagi. Ketiganya",
                    "mengatur tampilan, dan tampilan sekarang diatur dengan CSS.",
                ]
            },
            {
                "heading": "Kutipan, kode, dan karakter khusus",
                "code": """<blockquote cite="https://contoh.test/wawancara">
  <p>Kopi yang baik tidak perlu gula untuk disukai.</p>
  <footer>— <cite>Wawancara Barista, 2023</cite></footer>
</blockquote>

<p>Dia bilang <q>tunggu tiga menit</q> lalu pergi.</p>

<pre><code>15 gram bubuk
250 ml air
92 derajat</code></pre>

<p>Tag paragraf ditulis &lt;p&gt; dan ditutup &lt;/p&gt;.</p>
<p>PT Kopi &amp; Rekan &copy; 2024.</p>"""
            },
            {
                "body": [
                    "Beberapa karakter harus ditulis dengan kode khusus:",
                    "",
                    "  &lt;    <    kalau ditulis langsung, dikira awal tag",
                    "  &gt;    >",
                    "  &amp;   &    kalau ditulis langsung, dikira awal kode khusus",
                    "  &quot;  \"",
                    "  &nbsp;  spasi yang TIDAK boleh jadi tempat pindah baris",
                    "  &copy;  (c)",
                    "",
                    "Bentuknya selalu tanda &, lalu nama, lalu titik koma, tanpa spasi.",
                    "Kalau titik komanya lupa, kodenya tampil apa adanya di layar.",
                    "",
                    "Kode angka",
                    "",
                    "Selain dengan nama, sebuah karakter juga bisa ditulis dengan nomornya.",
                    "Ketiga tulisan ini menghasilkan tanda petik tunggal yang sama:",
                    "",
                    "  &apos;   pakai nama",
                    "  &#39;    pakai nomor karakternya, ditulis desimal",
                    "  &#x27;   nomor yang sama, ditulis heksadesimal (basis 16)",
                    "",
                    "Cirinya mudah dikenali: ada tanda # sesudah &, lalu angka. Huruf x",
                    "sesudah # berarti angkanya ditulis dalam basis 16.",
                    "",
                    "Kamu mungkin tidak akan mengetiknya sendiri, tapi kamu akan sering",
                    "melihatnya. Bentuk ini dihasilkan oleh mesin template, CMS (aplikasi",
                    "pengelola isi situs, seperti WordPress), dan fungsi pengaman teks.",
                    "Halaman buatan WordPress atau Django sering berisi &#8217; dan &#x2F;.",
                    "Itu normal dan tidak berarti ada yang rusak.",
                    "",
                    "Beberapa nama lain yang juga sering muncul:",
                    "",
                    "  &mdash;   —   garis panjang pemisah anak kalimat",
                    "  &hellip;  …   titik tiga sebagai satu karakter",
                    "  &times;   ×   tanda kali, dan itu bukan huruf x",
                    "  &rsquo;   ’   petik tunggal melengkung, untuk apostrof",
                    "  &middot;  ·   titik tengah pemisah",
                    "",
                    "Yang wajib dihafal cuma tiga: &lt; &gt; &amp;. Huruf beraksen tidak",
                    "perlu kode khusus selama <meta charset> sudah ada.",
                    "",
                    "Tentang <pre>:",
                    "  <pre> adalah satu-satunya elemen yang mempertahankan spasi dan baris",
                    "  apa adanya. Karena itu, jangan menekan Enter tepat sesudah tag",
                    "  pembuka <pre>. Baris kosong itu ikut tampil.",
                    "",
                    "  <pre> mengatur tata letaknya, <code> menyatakan bahwa isinya kode.",
                    "  Keduanya dipakai berpasangan untuk blok kode.",
                ]
            },
        ],
    },
    {
        "title": "5. Kutipan, Waktu, dan Penanda Teks Lainnya",
        "sections": [
            {
                "body": [
                    "Materi teks sebelumnya sempat MENAMPILKAN beberapa tag ini di contoh kodenya",
                    "tanpa menjelaskannya sekata pun: <blockquote>, <cite>, <q>, <del>, <ins>,",
                    "<mark>, <small>. Materi ini melunasinya, sekalian menambahkan yang lain yang",
                    "sama seringnya muncul di kode orang: <time>, <abbr>, <address>, <sup>, <sub>,",
                    "<s>, <u>, <hr>, <kbd>, <samp>, dan <var>.",
                    "",
                    "Semuanya punya pola yang sama. Tampilannya bisa ditiru dengan <span> + CSS;",
                    "ARTI-nya tidak bisa. Yang hilang kalau kamu memilih <span> disebutkan di tiap",
                    "bagian di bawah, supaya kamu tahu apa yang sedang kamu tukar.",
                    "",
                    "KUTIPAN PANJANG: <blockquote>",
                    "",
                    "  <blockquote cite=\"https://contoh.test/wawancara\">",
                    "    <p>Kopi yang baik tidak perlu gula untuk disukai.</p>",
                    "  </blockquote>",
                    "",
                    "  Isinya elemen BLOK, bukan teks telanjang. Kutipan satu alinea pun tetap",
                    "  dibungkus <p> di dalamnya. <blockquote> itu wadah, dan wadah tidak",
                    "  menampung kalimat langsung.",
                    "",
                    "  Browser menggambarnya menjorok ke kanan. Itu akibat, bukan alasan.",
                    "  Butuh teks menjorok tanpa sedang mengutip siapa pun? Itu urusan CSS.",
                    "",
                    "ATRIBUT cite TIDAK TERLIHAT SAMA SEKALI",
                    "",
                    "  cite=\"...\" berisi ALAMAT sumbernya — URL atau nama berkas. Tidak satu pun",
                    "  browser menampilkannya: tidak di layar, tidak saat kursor berhenti di",
                    "  atasnya, tidak di mana pun. Ia cuma terbaca program yang memeriksa markup.",
                    "",
                    "  Jadi kalau kamu ingin PEMBACA tahu sumbernya, kamu harus menuliskannya",
                    "  sekali lagi sebagai teks. Tempat bakunya <footer> di dalam blockquote:",
                    "",
                    "    <footer>— <cite>Wawancara Barista</cite>, 2023</footer>",
                    "",
                    "  Ini jebakan yang memakan banyak orang: mereka mengisi cite dengan rapi,",
                    "  membuka halamannya, dan tidak melihat apa pun berubah — lalu mengira",
                    "  atributnya salah ketik.",
                    "",
                    "DUA BENDA BERBEDA YANG NAMANYA SAMA",
                    "",
                    "  cite=\"...\"        ATRIBUT. Isinya ALAMAT sumber. Tidak terlihat.",
                    "  <cite>...</cite>  ELEMEN. Isinya JUDUL KARYA: buku, film, lagu, artikel,",
                    "                    nama acara. Terlihat, dan digambar miring.",
                    "",
                    "  Keduanya boleh muncul di kutipan yang sama, dan memang sering begitu.",
                    "  Satu menyimpan alamatnya untuk mesin, satu menampilkan judulnya untuk mata.",
                    "",
                    "  <cite> BUKAN tempat nama orang yang berbicara.",
                    "    Menurut <cite>Rina</cite>          salah, itu nama orang",
                    "    Menurut <cite>Wawancara Barista</cite>   benar, itu nama karyanya",
                    "",
                    "KUTIPAN PENDEK DI TENGAH KALIMAT: <q>",
                    "",
                    "  <p>Ia menyebutnya <q>seduhan yang jujur</q> sepanjang wawancara.</p>",
                    "",
                    "  BROWSER yang menambahkan tanda petiknya. Jangan mengetiknya sendiri:",
                    "",
                    "    <q>\"seduhan yang jujur\"</q>   tampil jadi   \"\"seduhan yang jujur\"\"",
                    "",
                    "  Untungnya nyata: petiknya menyesuaikan lang halaman. Di halaman lang=\"id\"",
                    "  ia memakai \"...\", di halaman berbahasa Prancis ia memakai «...». Kamu",
                    "  menulis satu markup, bentuk petiknya mengurus dirinya sendiri.",
                    "",
                    "  Kalau kamu cuma ingin tanda petik dan tidak sedang mengutip siapa-siapa,",
                    "  ketik saja petiknya. <q> berarti \"ini kutipan\", bukan \"beri tanda petik\".",
                ],
            },
            {
                "body": [
                    "REVISI: <del> DAN <ins>",
                    "",
                    "  <p>Suhu air lama <del>96 derajat</del>, sekarang <ins>92 derajat</ins>.</p>",
                    "",
                    "  <del>  bagian yang DIHAPUS dari dokumen. Digambar dicoret.",
                    "  <ins>  bagian yang DITAMBAHKAN. Digambar bergaris bawah.",
                    "",
                    "  Keduanya menerima dua atribut yang jarang dipakai padahal berguna:",
                    "    cite=\"...\"       alamat halaman yang menerangkan KENAPA diubah",
                    "    datetime=\"...\"   KAPAN diubah, dalam format mesin (lihat <time> nanti)",
                    "",
                    "  Kenapa tidak cukup mencoret pakai CSS saja: pembaca layar MENGUMUMKAN",
                    "  <del> dan <ins>. Teks yang cuma dicoret lewat CSS tetap dibacakan seolah",
                    "  masih berlaku, dan yang mendengarkan tidak punya cara tahu bahwa harga",
                    "  itu sudah bukan harga.",
                    "",
                    "<s> — CORET, TAPI BUKAN REVISI",
                    "",
                    "  <p>Harga cetak <s>75.000</s>, edisi ini gratis.</p>",
                    "",
                    "  <s> artinya \"sudah tidak berlaku\", bukan \"dihapus dari dokumen\".",
                    "  Harga lama di etalase, jadwal yang batal, tugas yang sudah selesai.",
                    "  Kalau yang kamu maksud adalah SUNTINGAN atas dokumennya, pakai <del>.",
                    "",
                    "<u> — hampir selalu pilihan yang salah",
                    "",
                    "  Garis bawah di halaman web berarti TAUTAN bagi hampir semua orang.",
                    "  Memakai <u> untuk penekanan membuat orang mengklik sesuatu yang tidak",
                    "  bisa diklik, lalu mengira halamannya rusak.",
                    "  Sisa pemakaian sahnya sempit sekali: menandai kata yang salah eja, dan",
                    "  penanda nama diri di teks Mandarin. Untuk penekanan pakai <em> atau",
                    "  <strong> — sudah dibahas di materi teks.",
                    "",
                    "<mark> — SOROTAN STABILO",
                    "",
                    "  Bagian yang menonjol KARENA keperluan pembaca saat ini, bukan karena ia",
                    "  penting selamanya. Pemakaian paling umum: kata yang barusan dicari orang,",
                    "  disorot di halaman hasil pencarian.",
                    "  Bedanya dengan <strong>: <strong> penting bagi siapa pun yang membaca;",
                    "  <mark> cuma relevan buat pembaca yang satu ini, saat ini.",
                    "",
                    "<small> — CETAKAN KECIL, BUKAN \"HURUF KECIL\"",
                    "",
                    "  Untuk yang memang cetakan kecil: hak cipta, syarat dan ketentuan,",
                    "  keterangan sumber, catatan sampingan.",
                    "  Bukan alat mengecilkan huruf. Butuh huruf kecil demi tampilan? font-size",
                    "  di CSS. <small> yang dipakai buat mengecilkan judul akan tetap dibaca",
                    "  sebagai \"ini keterangan tambahan\" oleh yang tidak melihat layarnya.",
                    "",
                    "<hr> — PERGANTIAN TOPIK, BUKAN GARIS HIAS",
                    "",
                    "  Namanya dari horizontal rule dan itu menyesatkan. Artinya sekarang:",
                    "  peralihan ke pokok bahasan lain di dalam bagian yang sama — pergantian",
                    "  adegan dalam cerita, batas antara isi surat dan catatan kakinya.",
                    "  Butuh garis pemisah supaya cantik? Itu border di CSS, bukan <hr>.",
                    "",
                    "  <hr> salah satu ELEMEN KOSONG dari daftar yang kamu temui di materi",
                    "  tautan dan gambar: tidak punya isi, jadi tidak ada </hr>.",
                ],
            },
            {
                "body": [
                    "<time> — TANGGAL YANG BISA DIBACA MESIN",
                    "",
                    "  <time datetime=\"2024-01-15\">15 Januari 2024</time>",
                    "                  ^ untuk mesin       ^ untuk manusia",
                    "",
                    "  Kenapa tanggalnya ditulis DUA KALI? Karena \"15 Januari 2024\", \"15/01/2024\",",
                    "  dan \"15 Jan '24\" adalah satu tanggal yang sama bagi kita, tapi tiga teks",
                    "  yang sama sekali berbeda bagi program. datetime memberi satu bentuk baku",
                    "  yang bisa dipahami tanpa menebak, dan teks di dalam elemennya tetap bebas",
                    "  kamu tulis seindah apa pun untuk pembaca.",
                    "",
                    "  Formatnya selalu dari satuan TERBESAR ke terkecil, dengan angka:",
                    "    2024-01-15                tanggal",
                    "    2024-01                   bulan",
                    "    09:30                     jam dan menit",
                    "    2024-01-15T09:30          tanggal dan jam, dipisah huruf T",
                    "    2024-01-15T09:30+07:00    dengan zona waktu (+07:00 = WIB)",
                    "    PT3M                      durasi 3 menit  (P = periode, T = waktu)",
                    "    PT1H30M                   durasi 1 jam 30 menit",
                    "",
                    "  Yang membacanya nyata: mesin pencari memakainya untuk menampilkan tanggal",
                    "  artikel di hasil pencarian, pembaca layar membacakannya dengan benar, dan",
                    "  tombol \"tambahkan ke kalender\" mengambil nilainya dari sana. Itu sebabnya",
                    "  <time> ada di hampir setiap artikel blog yang pernah kamu buka.",
                    "",
                    "  Kalau teksnya SUDAH berformat baku, datetime boleh dilewat:",
                    "  <time>2024-01-15</time> sah. Selain itu, tulis datetime-nya.",
                    "",
                    "  Jebakannya sunyi: datetime=\"15 Januari 2024\" tidak memunculkan error apa",
                    "  pun — cuma diam-diam tidak terbaca siapa-siapa. Sama sunyinya dengan",
                    "  datetime=\"15-01-2024\", yang terbaca sebagai tahun 15.",
                    "",
                    "<abbr> — SINGKATAN BESERTA KEPANJANGANNYA",
                    "",
                    "  <abbr title=\"Standard Operating Procedure\">SOP</abbr>",
                    "",
                    "  title berisi kepanjangannya. Di komputer ia muncul sebagai gelembung kecil",
                    "  saat kursor berhenti di atasnya, dan di layar sentuh TIDAK muncul sama",
                    "  sekali — jebakan yang sama dengan atribut title mana pun.",
                    "",
                    "  Karena itu aturan pakainya: tulis kepanjangannya sekali sebagai teks biasa",
                    "  di kemunculan pertama, baru pakai <abbr> di kemunculan berikutnya. Jangan",
                    "  menyimpan satu-satunya penjelasan di dalam title.",
                    "",
                    "<address> — KONTAK, BUKAN SEMBARANG ALAMAT",
                    "",
                    "  Ini nama yang paling sering disalahpahami di seluruh HTML. <address> berisi",
                    "  cara MENGHUBUNGI pemilik halaman atau penulis artikel terdekat: surel,",
                    "  telepon, tautan profil — boleh juga alamat posnya.",
                    "",
                    "  <address>Tanya: <a href=\"mailto:halo@contoh.test\">halo@contoh.test</a></address>",
                    "",
                    "  Yang BUKAN <address>: alamat pengiriman di formulir, alamat gedung yang",
                    "  kebetulan disebut di dalam artikel, daftar cabang toko. Itu teks biasa.",
                    "  Uji cepatnya: kalau alamat itu bukan cara menghubungi PENULISNYA, jangan.",
                    "",
                    "  Tempatnya biasa di dalam <footer>. Browser menggambarnya miring; itu lagi-",
                    "  lagi cuma kebiasaan menggambar, dan boleh diubah CSS.",
                    "",
                    "<sup> DAN <sub> — NAIK DAN TURUN",
                    "",
                    "  <sup>  di atas garis: pangkat 10<sup>3</sup>, penanda catatan kaki",
                    "         di ujung kalimat<sup>1</sup>, urutan 4<sup>th</sup>.",
                    "  <sub>  di bawah garis: rumus kimia H<sub>2</sub>O, indeks x<sub>1</sub>.",
                    "",
                    "  Dua elemen ini memang soal posisi, dan tetap ada alasan memakainya:",
                    "  naik-turunnya MENGUBAH ARTI. 10<sup>3</sup> yang terlanjur ditulis datar",
                    "  jadi \"103\" berubah dari seribu menjadi seratus tiga, dan tidak ada satu",
                    "  pun yang bisa menebak mana yang kamu maksud.",
                    "",
                    "TIGA PENANDA DOKUMENTASI TEKNIS: <kbd>, <samp>, <var>",
                    "",
                    "  <kbd>   tombol atau perintah yang DITEKAN pengguna: <kbd>Ctrl+S</kbd>",
                    "  <samp>  KELUARAN yang ditampilkan program: <samp>Selesai dalam 3 menit</samp>",
                    "  <var>   nama VARIABEL atau nilai yang bisa berubah: <var>suhu</var>",
                    "",
                    "  Bandingkan dengan <code> yang sudah kamu pakai. <code> berkata \"ini kode\"",
                    "  secara umum; ketiga ini lebih tepat sasaran. Gunanya terasa persis di",
                    "  tempat kamu paling sering membacanya — tutorial dan dokumentasi, tempat",
                    "  perintah yang harus diketik dan pesan yang muncul di layar gampang",
                    "  tertukar kalau keduanya cuma ditulis dengan <code>.",
                ],
            },
            {
                "heading": "artikel.html — semuanya dipakai sekaligus",
                "code": """<!doctype html>
<html lang="id">
<head>
  <meta charset="utf-8">
  <title>Panduan Seduh, Edisi Kedua</title>
</head>
<body>
  <article>
    <h1>Panduan Seduh, Edisi Kedua</h1>
    <p>Terbit <time datetime="2024-01-15">15 Januari 2024</time>,
       diperbarui <time datetime="2024-03-02">2 Maret 2024</time>.</p>

    <p>Suhu air lama <del datetime="2024-03-02">96 derajat</del>,
       sekarang <ins datetime="2024-03-02">92 derajat</ins>.</p>

    <blockquote cite="https://contoh.test/wawancara">
      <p>Kopi yang baik tidak perlu gula untuk disukai.</p>
      <footer>— <cite>Wawancara Barista</cite>, 2023</footer>
    </blockquote>

    <p>Ia menyebutnya <q>seduhan yang jujur</q> sepanjang wawancara.</p>

    <hr>

    <h2>Catatan teknis</h2>
    <p>Perbandingan <mark>1 : 16</mark> dipakai di seluruh
       <abbr title="Standard Operating Procedure">SOP</abbr> ini.</p>
    <p>Air adalah H<sub>2</sub>O, catatan kakinya di bawah<sup>1</sup>.</p>
    <p>Waktu seduh <time datetime="PT3M">3 menit</time>.</p>
    <p>Harga cetak <s>75.000</s>, edisi ini gratis.</p>
    <p>Tekan <kbd>Ctrl+S</kbd>, lalu jalankan <kbd>npm run seduh</kbd>.</p>
    <p>Layar akan menulis <samp>Selesai dalam 3 menit</samp>.</p>
    <p>Ganti nilai <var>suhu</var> di berkas pengaturan.</p>

    <footer>
      <p><small>&copy; 2024 Kopi Pagi. Boleh disalin sendiri.</small></p>
      <address>Tanya: <a href="mailto:halo@contoh.test">halo@contoh.test</a></address>
    </footer>
  </article>
</body>
</html>""",
            },
            {
                "body": [
                    "Pohon struktur berkas di atas — persis yang keluar kalau kamu menjalankannya:",
                    "",
                    "  <!doctype html>",
                    "  html lang=\"id\"",
                    "    head",
                    "      meta charset=\"utf-8\"",
                    "      title \"Panduan Seduh, Edisi Kedua\"",
                    "    body",
                    "      article",
                    "        h1 \"Panduan Seduh, Edisi Kedua\"",
                    "        p \"Terbit , diperbarui .\"",
                    "          time datetime=\"2024-01-15\" \"15 Januari 2024\"",
                    "          time datetime=\"2024-03-02\" \"2 Maret 2024\"",
                    "        p \"Suhu air lama , sekarang .\"",
                    "          del datetime=\"2024-03-02\" \"96 derajat\"",
                    "          ins datetime=\"2024-03-02\" \"92 derajat\"",
                    "        blockquote cite=\"https://contoh.test/wawancara\"",
                    "          p \"Kopi yang baik tidak perlu gula untuk disukai.\"",
                    "          footer \"— , 2023\"",
                    "            cite \"Wawancara Barista\"",
                    "        p \"Ia menyebutnya sepanjang wawancara.\"",
                    "          q \"seduhan yang jujur\"",
                    "        hr",
                    "        h2 \"Catatan teknis\"",
                    "        p \"Perbandingan dipakai di seluruh ini.\"",
                    "          mark \"1 : 16\"",
                    "          abbr title=\"Standard Operating Procedure\" \"SOP\"",
                    "        p \"Air adalah H O, catatan kakinya di bawah .\"",
                    "          sub \"2\"",
                    "          sup \"1\"",
                    "        p \"Waktu seduh .\"",
                    "          time datetime=\"PT3M\" \"3 menit\"",
                    "        p \"Harga cetak , edisi ini gratis.\"",
                    "          s \"75.000\"",
                    "        p \"Tekan , lalu jalankan .\"",
                    "          kbd \"Ctrl+S\"",
                    "          kbd \"npm run seduh\"",
                    "        p \"Layar akan menulis .\"",
                    "          samp \"Selesai dalam 3 menit\"",
                    "        p \"Ganti nilai di berkas pengaturan.\"",
                    "          var \"suhu\"",
                    "        footer",
                    "          p",
                    "            small \"© 2024 Kopi Pagi. Boleh disalin sendiri.\"",
                    "          address \"Tanya:\"",
                    "            a href=\"mailto:halo@contoh.test\" \"halo@contoh.test\"",
                    "",
                    "Bentuk yang mengagetkan waktu pertama kali melihatnya:",
                    "",
                    "  p \"Terbit , diperbarui .\"",
                    "    time datetime=\"2024-01-15\" \"15 Januari 2024\"",
                    "",
                    "Teks paragrafnya berlubang, dan tanggalnya pindah jadi baris anak di",
                    "bawahnya. Itu bukan kerusakan. Elemen sebaris tetap elemen, dan tiap elemen",
                    "dapat barisnya sendiri di pohon — teks milik anak dicetak di baris anak,",
                    "bukan di baris induknya. Kalau kamu mengerjakan latihan yang keluarannya",
                    "pohon, inilah bentuk yang harus kamu tiru.",
                    "",
                    "Empat hal lain yang pantas diperhatikan:",
                    "  - hr berdiri sendiri: tanpa teks, tanpa anak, tanpa penutup.",
                    "  - &copy; sudah menjadi © di pohon. Yang dibandingkan adalah HASIL bacanya,",
                    "    jadi &copy; dan © menghasilkan pohon yang sama persis.",
                    "  - p di dalam footer tampil tanpa teks sama sekali, karena seluruh teksnya",
                    "    milik <small> yang ada di dalamnya.",
                    "  - atribut ikut tercetak dan diurutkan alfabetis, termasuk title milik abbr",
                    "    dan datetime milik del, ins, serta time.",
                ],
            },
        ],
    },
    {
        "title": "6. Daftar: ul, ol, dan dl",
        "sections": [
            {
                "body": [
                    "Tiga jenis daftar, dan yang membedakan bukan tampilannya:",
                    "",
                    "  <ul>  daftar TAK berurutan. Urutan item tidak berarti apa-apa.",
                    "        Bahan masakan, daftar fitur, menu navigasi.",
                    "",
                    "  <ol>  daftar BERURUTAN. Menukar urutannya mengubah maknanya.",
                    "        Langkah resep, peringkat, instruksi pemasangan.",
                    "",
                    "  <dl>  daftar deskripsi. Pasangan istilah dan penjelasannya.",
                    "        Glosarium, spesifikasi, daftar pertanyaan-jawaban.",
                    "",
                    "Bulatan pada ul dan angka pada ol cuma bawaan browser dan bisa",
                    "diganti CSS. Jadi jangan memilih ol karena ingin ada angkanya;",
                    "pilih ol karena urutannya memang penting.",
                    "",
                    "Isi ul dan ol selalu <li> (list item).",
                ]
            },
            {
                "heading": "ul dan ol",
                "code": """<h2>Bahan</h2>
<ul>
  <li>Biji kopi 20 gram</li>
  <li>Air panas 300 ml</li>
  <li>Gula secukupnya</li>
</ul>

<h2>Langkah</h2>
<ol>
  <li>Giling biji sampai sehalus pasir kasar.</li>
  <li>Basahi kertas saring dengan air panas, lalu buang airnya.</li>
  <li>Tuang air melingkar dari tengah ke tepi.</li>
  <li>Tunggu tiga menit, angkat penyaringnya.</li>
</ol>

<h2>Lanjutan resep sebelumnya</h2>
<ol start="5">
  <li>Aduk sebentar sebelum dituang ke gelas.</li>
</ol>"""
            },
            {
                "body": [
                    "Atribut yang berguna pada <ol>:",
                    "",
                    "  start=\"5\"      mulai penomoran dari 5",
                    "  reversed       hitung mundur",
                    "  type=\"a\"       a, b, c  (bisa juga A, i, I, 1)",
                    "",
                    "ATURAN YANG PALING SERING DILANGGAR:",
                    "  Anak langsung <ul> dan <ol> hanya boleh <li>. Titik.",
                    "",
                    "  <ul>",
                    "    <p>Keterangan</p>      SALAH, p bukan li",
                    "    <li>Item</li>",
                    "  </ul>",
                    "",
                    "  Taruh keterangannya SEBELUM daftar, atau di dalam <li>.",
                    "",
                    "Sebaliknya, di dalam <li> boleh apa saja: paragraf, gambar,",
                    "tabel, bahkan daftar lain. <li> adalah kotak biasa yang",
                    "kebetulan diberi penanda di sisi kiri.",
                ]
            },
            {
                "heading": "Daftar bersarang dan daftar deskripsi",
                "code": """<ul>
  <li>Kopi panas
    <ul>
      <li>Tubruk</li>
      <li>V60</li>
    </ul>
  </li>
  <li>Kopi dingin
    <ul>
      <li>Es kopi susu</li>
      <li>Cold brew</li>
    </ul>
  </li>
</ul>

<dl>
  <dt>Arabika</dt>
  <dd>Rasa lebih asam dan wangi, kafeinnya lebih rendah.</dd>

  <dt>Robusta</dt>
  <dd>Rasa lebih pahit dan berat, kafeinnya hampir dua kali lipat.</dd>
  <dd>Biasa dipakai untuk kopi instan dan campuran espresso.</dd>
</dl>"""
            },
            {
                "body": [
                    "Perhatikan letak daftar bersarang di contoh:",
                    "",
                    "  <li>Kopi panas",
                    "    <ul> ... </ul>",
                    "  </li>",
                    "",
                    "Daftar anak ada DI DALAM <li>, sebelum </li>. Bukan di antara",
                    "dua <li>. Salah tempat begini adalah kesalahan HTML nomor satu",
                    "pada daftar bersarang, dan akibatnya indentasinya kacau tanpa",
                    "ada yang memberi tahu kenapa.",
                    "",
                    "Daftar deskripsi (dl):",
                    "  <dt>  istilahnya       (description term)",
                    "  <dd>  penjelasannya    (description details)",
                    "",
                    "  Satu <dt> boleh punya beberapa <dd>, seperti Robusta di atas.",
                    "  Beberapa <dt> berturut-turut juga boleh, kalau dua istilah",
                    "  berbagi satu penjelasan.",
                    "",
                    "  <dt> dan <dd> harus jadi anak langsung <dl>, tanpa pembungkus.",
                    "",
                    "Satu hal yang jarang disadari pemula: menu navigasi itu daftar",
                    "tautan. Ditulis sebagai <ul> berisi <li><a>. Pembaca layar akan",
                    "mengumumkan \"daftar, 5 item\" — dan itu memang informasi yang",
                    "berguna sebelum orang memutuskan mendengarkan seluruhnya.",
                ]
            },
        ],
    },
    {
        "title": "7. Tautan (a) dan Gambar (img)",
        "sections": [
            {
                "body": [
                    "Tautan adalah alasan web ada. Huruf 'HT' pada HTML berarti",
                    "HyperText: teks yang bisa menunjuk ke teks lain.",
                    "",
                    "  <a href=\"tujuan\">teks yang bisa diklik</a>",
                    "",
                    "'a' singkatan dari anchor. href singkatan dari hypertext",
                    "reference — alamat tujuannya.",
                    "",
                    "Enam bentuk href yang perlu kamu bedakan:",
                    "",
                    "  menu.html            berkas di folder yang sama",
                    "  halaman/menu.html    masuk ke subfolder",
                    "  ../index.html        naik satu folder dulu",
                    "  /menu.html           dari akar situs (butuh server web)",
                    "  https://situs.test/  alamat lengkap ke situs lain",
                    "  #kontak              lompat ke elemen ber-id \"kontak\"",
                    "",
                    "Alamat relatif dihitung dari lokasi berkas HTML-nya, bukan dari",
                    "tempat kamu membuka browser. Ini penyebab paling umum tautan",
                    "yang mati saat berkas dipindah ke folder lain.",
                    "",
                    "BENTUK BERIKUTNYA: SKEMA",
                    "",
                    "href tidak selalu berisi alamat halaman. Kalau di dalamnya ada",
                    "tanda titik dua, yang berdiri di DEPAN titik dua itu bukan nama",
                    "berkas melainkan SKEMA: pemberitahuan tentang jenis alamatnya,",
                    "sekaligus penentu siapa yang akan menanganinya.",
                    "",
                    "  https:   halaman web. Ditangani browser sendiri.",
                    "  mailto:  alamat surel. Membuka aplikasi surel pengguna.",
                    "  tel:     nomor telepon. Di ponsel, membuka pemanggil.",
                    "  sms:     nomor tujuan pesan singkat.",
                    "",
                    "  <a href=\"mailto:halo@kopipagi.test\">halo@kopipagi.test</a>",
                    "  <a href=\"mailto:halo@kopipagi.test?subject=Pesanan\">Pesan</a>",
                    "  <a href=\"tel:+62221234567\">(022) 123-4567</a>",
                    "",
                    "Sesudah alamat surel boleh ditempel ?subject=... untuk mengisi",
                    "judul surelnya duluan. Nomor telepon ditulis lengkap dengan kode",
                    "negara di dalam href (+62...), sementara teks yang dilihat orang",
                    "tetap boleh ditulis seperti biasa.",
                    "",
                    "Dua skema lagi yang akan kamu temui di kode orang, dan sebaiknya",
                    "TIDAK kamu tiru:",
                    "",
                    "  javascript:  href=\"javascript:void(0)\". Kebiasaan lama untuk",
                    "               membuat tautan yang tidak pergi ke mana-mana.",
                    "               Kalau yang kamu buat sebenarnya tombol, tulis",
                    "               <button>. Ia sudah bisa ditekan dengan spasi",
                    "               dan sudah dibacakan sebagai tombol.",
                    "  data:        seluruh isi berkasnya ditempel di dalam href itu",
                    "               sendiri, dalam bentuk sandi panjang. Dipakai alat",
                    "               bantu untuk menyisipkan gambar kecil tanpa berkas",
                    "               terpisah; ditulis tangan ia cuma membuat berkasmu",
                    "               mustahil dibaca.",
                ]
            },
            {
                "heading": "Berbagai jenis tautan",
                "code": """<p>Baca <a href="menu.html">daftar menu</a> kami dulu.</p>

<p>Panduan lengkap ada di
  <a href="https://developer.mozilla.org/id/">dokumentasi MDN</a>.</p>

<p>Lompat ke <a href="#kontak">bagian kontak</a> di halaman ini.</p>

<p>Surel: <a href="mailto:halo@kopipagi.test">halo@kopipagi.test</a></p>
<p>Telepon: <a href="tel:+62221234567">(022) 123-4567</a></p>

<p>Buka <a href="https://peta.test/kopipagi" target="_blank"
   rel="noopener noreferrer">peta lokasi</a> di tab baru.</p>

<h2 id="kontak">Kontak</h2>
<p>Jalan Melati 7, Bandung.</p>"""
            },
            {
                "body": [
                    "target=\"_blank\" membuka tautan di tab baru.",
                    "Selalu pasangkan dengan rel=\"noopener noreferrer\":",
                    "  noopener   halaman tujuan tidak bisa mengendalikan tab asalmu",
                    "  noreferrer halaman tujuan tidak diberi tahu asalnya dari mana",
                    "",
                    "Tanpa noopener, halaman yang kamu buka bisa mengganti isi tab",
                    "lamamu diam-diam. Itu trik penipuan yang benar-benar dipakai.",
                    "",
                    "Pakai _blank seperlunya saja. Merebut kendali tombol Kembali",
                    "dari pengguna jarang membuat siapa pun senang.",
                    "",
                    "TEKS TAUTAN HARUS BERMAKNA SENDIRIAN",
                    "",
                    "  <a href=\"menu.html\">klik di sini</a>      buruk",
                    "  <a href=\"menu.html\">daftar menu</a>       baik",
                    "",
                    "Alasannya konkret: pembaca layar punya perintah \"bacakan semua",
                    "tautan di halaman ini\". Yang terdengar dari halaman pertama",
                    "adalah: \"klik di sini, klik di sini, klik di sini, selengkapnya\".",
                    "Tidak ada satu pun yang bisa dipilih dari daftar itu.",
                ]
            },
            {
                "heading": "Gambar",
                "code": """<img src="gambar/biji-kopi.jpg"
     alt="Biji kopi sangrai gelap di atas timbangan digital"
     width="640" height="360">

<figure>
  <img src="gambar/tuang.jpg"
       alt="Air panas dituang melingkar ke atas bubuk kopi di corong V60"
       width="640" height="360">
  <figcaption>Tuang melingkar dari tengah ke tepi, jangan kena dinding.</figcaption>
</figure>

<img src="gambar/garis-hias.png" alt="" width="200" height="8">"""
            },
            {
                "body": [
                    "<img> adalah ELEMEN KOSONG.",
                    "",
                    "  Elemen kosong tidak punya isi, jadi tidak punya tag penutup.",
                    "  Tidak ada </img>. Menulisnya bukan cuma tidak perlu — itu",
                    "  dianggap kesalahan.",
                    "",
                    "  Daftar lengkapnya pendek dan layak dihafal:",
                    "    img  br  hr  input  meta  link  source  col  area  base",
                    "    embed  track  wbr",
                    "",
                    "  Artinya masing-masing, sekali saja, supaya daftar itu tidak",
                    "  jadi hafalan kosong:",
                    "",
                    "    img     gambar",
                    "    br      pindah baris di dalam satu paragraf",
                    "    hr      pergantian topik, bukan garis hias",
                    "    input   satu isian formulir: kotak teks, centang, radio",
                    "    meta    sepotong keterangan tentang halaman, di dalam head",
                    "    link    sambungan ke berkas lain: berkas CSS, ikon tab",
                    "    source  satu pilihan berkas di dalam picture, video, audio",
                    "    col     pemegang atribut dan gaya untuk satu KOLOM tabel",
                    "    area    satu daerah yang bisa diklik di dalam <map>, yaitu",
                    "            gambar yang bagian-bagiannya jadi tautan berbeda",
                    "            (denah, peta). Jarang dipakai sekarang; SVG lebih",
                    "            luwes dan lebih mudah diatur.",
                    "    base    alamat dasar untuk semua alamat relatif di halaman",
                    "    embed   menyematkan isi yang ditangani program lain.",
                    "            Peninggalan zaman Flash; sekarang dipakai <iframe>",
                    "    track   berkas takarir untuk <video> dan <audio>",
                    "    wbr     titik yang BOLEH dipakai browser untuk memenggal",
                    "            kata kepanjangan, kalau memang kehabisan tempat",
                    "",
                    "  Sebagian sudah kamu temui, sebagian baru datang di materi",
                    "  berikutnya. Yang perlu dipegang sekarang cuma satu: ketiga",
                    "  belas nama itu tidak punya tag penutup.",
                    "",
                    "  Isi elemen kosong dikirim lewat ATRIBUT, bukan lewat teks",
                    "  di antara dua tag. Itu sebabnya gambar punya src, dan",
                    "  bukan <img>foto.jpg</img>.",
                    "",
                    "  Bentuk <img ... /> dengan garis miring juga sah dan tidak",
                    "  mengubah apa pun. Itu warisan XHTML. Tidak perlu ditulis,",
                    "  tapi kalau kamu melihatnya di kode orang lain, itu bukan bug.",
                    "",
                    "KENAPA alt WAJIB ADA",
                    "",
                    "  alt adalah teks pengganti gambar. Ia dipakai ketika gambarnya",
                    "  TIDAK bisa dilihat, dan itu terjadi lebih sering dari dugaan:",
                    "",
                    "    - Berkas gambarnya gagal dimuat atau namanya salah ketik.",
                    "    - Pemakainya tunanetra dan mendengarkan halaman.",
                    "    - Koneksinya lambat dan gambar dimatikan.",
                    "    - Mesin pencari sedang membaca halamanmu.",
                    "",
                    "  Tulis apa yang PENTING dari gambar itu, bukan judul berkasnya.",
                    "    alt=\"gambar\"            tidak berguna",
                    "    alt=\"biji-kopi.jpg\"     tidak berguna",
                    "    alt=\"Biji kopi sangrai gelap di atas timbangan\"   berguna",
                    "",
                    "  Gambar hiasan murni ditulis alt=\"\" — KOSONG, tapi tetap ada.",
                    "  Itu bukan sama dengan menghapus alt-nya:",
                    "    alt=\"\"        \"lewati saja, ini cuma hiasan\"",
                    "    tanpa alt     pembaca layar tidak tahu apa-apa, jadi ia",
                    "                  membacakan nama berkasnya. Keras-keras.",
                ]
            },
            {
                "body": [
                    "width dan height pada <img>:",
                    "",
                    "  Ditulis tanpa satuan, dalam piksel: width=\"640\" height=\"360\".",
                    "",
                    "  Kenapa perlu, padahal ukurannya nanti diatur CSS? Karena",
                    "  browser perlu tahu perbandingan sisinya SEBELUM gambarnya",
                    "  selesai diunduh. Tanpa itu, halaman digambar seolah gambarnya",
                    "  setinggi nol, lalu melompat begitu gambarnya datang — tepat",
                    "  saat orang sudah mulai membaca atau menekan tombol.",
                    "",
                    "  Tulis ukuran ASLI gambarnya. CSS tetap boleh mengubahnya.",
                    "",
                    "<figure> dan <figcaption>:",
                    "  Dipakai kalau gambar punya keterangan. Bedanya dengan menaruh",
                    "  <p> di bawah gambar: figure mengikat keduanya jadi satu",
                    "  kesatuan, jadi pembaca layar tahu keterangan itu milik gambar",
                    "  yang mana.",
                    "",
                    "  alt dan figcaption tidak sama dan tidak boleh diisi kalimat",
                    "  yang sama persis. alt menjelaskan gambarnya untuk yang tidak",
                    "  melihat; figcaption adalah keterangan untuk SEMUA orang.",
                ]
            },
        ],
    },
    {
        "title": "8. Menjalankan Halaman Sendiri: Server Lokal dan Jalur Berkas",
        "sections": [
            {
                "body": [
                    "Sejak Materi 1 kamu cuma punya satu cara membuka halaman: klik dua",
                    "kali berkasnya. Itu bekerja, dan untuk satu berkas memang cukup.",
                    "Tapi lihat bilah alamat browsernya:",
                    "",
                    "  file:///home/levi/kopi/index.html",
                    "",
                    "Tulisan sebelum titik dua itu PROTOKOL — cara browser mendapatkan",
                    "berkasnya. Ada dua yang perlu kamu bedakan seumur hidup:",
                    "",
                    "  file:   baca LANGSUNG dari hard disk komputer ini.",
                    "          Tidak ada server. Tidak ada jaringan. Browser membuka",
                    "          berkas persis seperti aplikasi lain membuka berkas.",
                    "",
                    "  http:   MINTA berkas itu kepada sebuah program yang menyajikannya.",
                    "          Program itulah yang namanya server web. Ia bisa duduk di",
                    "          komputer lain di internet, atau di komputer ini juga.",
                    "",
                    "Tiga garis miring di file:/// bukan salah ketik. Bentuk aslinya",
                    "file:// + nama komputer + /jalur. Nama komputernya dikosongkan",
                    "karena artinya \"komputer ini\", jadi dua garis miring bertemu satu.",
                    "Di Windows bunyinya file:///C:/Users/Levi/kopi/index.html.",
                    "",
                    "Anggap berkas-berkasmu tersusun begini:",
                    "",
                    "  kopi/",
                    "    index.html",
                    "    gaya.css",
                    "    halaman/",
                    "      menu.html",
                    "    gambar/",
                    "      biji-kopi.jpg",
                    "",
                    "Materi tautan dan gambar menyebut satu bentuk alamat lalu berhenti",
                    "di situ: \"/menu.html — dari akar situs (butuh server web)\".",
                    "Kamu diberi tahu ada dinding. Ini pintunya.",
                    "",
                    "GARIS MIRING PERTAMA BERARTI \"MULAI DARI AKAR\"",
                    "",
                    "  Alamat tanpa garis miring depan dihitung dari folder berkasnya.",
                    "  Alamat DENGAN garis miring depan melupakan folder itu sepenuhnya",
                    "  dan menghitung dari akar. Pertanyaannya: akar apa?",
                    "",
                    "  Jawabannya ditentukan protokol, dan di sinilah orang tersandung.",
                    "",
                    "    Lewat http://kopipagi.test/",
                    "      akarnya = folder situs itu.",
                    "      /gaya.css  ->  http://kopipagi.test/gaya.css   ada, jalan.",
                    "",
                    "    Lewat file:///home/levi/kopi/index.html",
                    "      akarnya = akar SELURUH DISK komputermu.",
                    "      /gaya.css  ->  file:///gaya.css, yaitu sebuah berkas di",
                    "      pangkal disk, sejajar dengan folder /home dan /usr.",
                    "",
                    "  Berkas itu tentu saja tidak ada. Dan tidak ada satu pun pesan",
                    "  error: CSS-nya diam-diam tidak dimuat, halamanmu tampil polos",
                    "  tanpa warna, gambar jadi ikon rusak, tautan mendarat di halaman",
                    "  kosong. Kamu akan memeriksa isi gaya.css berjam-jam padahal",
                    "  berkas itu tidak pernah dibaca sekali pun.",
                    "",
                    "Yang membuatnya menyakitkan: /gaya.css justru bentuk yang PALING",
                    "sering kamu lihat di kode orang lain. Kode itu tidak salah — ia",
                    "ditulis untuk dibuka lewat server. Kamu yang belum punya server.",
                ],
            },
            {
                "heading": "Halaman yang tidak bisa dibuka dengan klik dua kali",
                "code": """<!doctype html>
<html lang="id">
<head>
  <meta charset="utf-8">
  <title>Kopi Pagi</title>
  <link rel="stylesheet" href="/gaya.css">
</head>
<body>
  <h1>Kopi Pagi</h1>
  <img src="/gambar/biji-kopi.jpg"
       alt="Biji kopi sangrai gelap di atas timbangan digital"
       width="640" height="360">
  <p>Lihat <a href="/halaman/menu.html">daftar menu</a> kami.</p>
</body>
</html>""",
            },
            {
                "body": [
                    "Simpan berkas itu sebagai kopi/index.html, lalu klik dua kali.",
                    "Halamannya muncul, tapi polos, gambarnya rusak, tautannya mati.",
                    "Tidak ada yang memberitahumu kenapa. Sekarang beri ia server.",
                    "",
                    "Kamu tidak perlu memasang apa pun. Python sudah ada di komputermu —",
                    "aplikasi belajar yang sedang kamu baca ini berjalan di atasnya.",
                    "",
                    "  cd ~/kopi                     masuk ke folder halamannya dulu",
                    "  python3 -m http.server 8000   nyalakan server DI folder itu",
                    "",
                    "Kata 'DI folder itu' bukan basa-basi: server ini menyajikan folder",
                    "tempat kamu berdiri saat menjalankannya, dan folder itulah yang",
                    "jadi akar situsmu. Salah folder = 404 di mana-mana.",
                    "",
                    "Terminal menjawab:",
                    "",
                    "  Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...",
                    "",
                    "Biarkan jendela terminal itu terbuka — selama ia terbuka, servernya",
                    "menyala. Buka browser ke:",
                    "",
                    "  http://localhost:8000",
                    "",
                    "Halaman yang tadi rusak kini utuh: CSS-nya masuk, gambarnya muncul,",
                    "tautannya hidup. Markupnya tidak kamu ubah sehuruf pun.",
                    "",
                    "Dua kata baru:",
                    "",
                    "  localhost",
                    "    Nama untuk \"komputer ini juga\". Selalu menunjuk ke dirimu",
                    "    sendiri dan tidak pernah keluar ke internet. Angkanya",
                    "    127.0.0.1; keduanya berarti sama dan boleh ditukar.",
                    "",
                    "  8000",
                    "    Nomor PORT. Satu komputer bisa menjalankan banyak server",
                    "    sekaligus, jadi tiap server memegang satu nomor pintu supaya",
                    "    permintaan tidak tertukar. 8000 cuma kebiasaan; 8080, 5500,",
                    "    atau 3000 sama saja. Kalau nomornya sedang dipakai program",
                    "    lain, Python berhenti dengan:",
                    "",
                    "      OSError: [Errno 98] Address already in use",
                    "",
                    "    Ganti angkanya, misalnya 8001. Bukan masalah besar.",
                    "",
                    "Tiga perilaku yang perlu kamu kenali sekarang juga:",
                    "",
                    "  ALAMATNYA CUMA FOLDER, HALAMANNYA TETAP TERBUKA.",
                    "    http://localhost:8000 tidak menyebut berkas apa pun, tapi yang",
                    "    muncul index.html. Setiap server web mencari index.html lebih",
                    "    dulu ketika yang diminta sebuah folder. Jadi nama index.html",
                    "    bukan selera — itu nama yang membuat halamanmu jadi halaman",
                    "    depan. Kalau folder itu tidak punya index.html, http.server",
                    "    menampilkan daftar isi foldernya apa adanya.",
                    "",
                    "  BERKAS YANG TIDAK ADA MENGHASILKAN 404.",
                    "    Buka http://localhost:8000/menu.html padahal berkasnya ada di",
                    "    halaman/menu.html. Yang muncul halaman putih bertuliskan:",
                    "",
                    "      Error response",
                    "      Error code: 404",
                    "      Message: File not found.",
                    "",
                    "    404 artinya \"servernya hidup, tapi tidak ada apa-apa di alamat",
                    "    itu\" — salah alamat, bukan salah server. Bedakan dari layar",
                    "    \"tidak bisa terhubung\", yang berarti servernya memang mati.",
                    "",
                    "  TERMINALNYA MENCATAT SETIAP PERMINTAAN.",
                    "    Ini alat diagnosis paling berguna yang kamu punya hari ini:",
                    "",
                    "      127.0.0.1 - - [...] \"GET /gaya.css HTTP/1.1\" 200 -",
                    "      127.0.0.1 - - [...] \"GET /gambar/biji.jpg HTTP/1.1\" 404 -",
                    "",
                    "    200 berarti terkirim, 404 berarti tidak ketemu. Kalau gambarmu",
                    "    tidak muncul, baris inilah yang menyebut alamat PERSIS yang",
                    "    diminta browser — dan hampir selalu, alamat itu bukan yang",
                    "    kamu kira sedang diminta.",
                    "",
                    "Menghentikannya: tekan Ctrl+C di terminal itu. Balasannya:",
                    "",
                    "  Keyboard interrupt received, exiting.",
                    "",
                    "Menutup tab browser TIDAK mematikan server. Selama terminal itu",
                    "masih menyala, foldermu masih disajikan.",
                    "",
                    "Dan itu bukan detail sepele. Angka 0.0.0.0 di pesan pembuka tadi",
                    "berarti server ini menerima permintaan dari SEMUA jaringan,",
                    "termasuk orang lain di wifi yang sama. Di rumah biasanya aman;",
                    "di kafe atau kantor kamu baru saja membagikan isi folder itu.",
                    "Tutup pintunya:",
                    "",
                    "  python3 -m http.server 8000 --bind 127.0.0.1",
                    "",
                    "Pesannya berubah jadi \"Serving HTTP on 127.0.0.1\", dan cuma",
                    "komputer ini yang bisa masuk.",
                    "",
                    "BATAS ALAT INI, SUPAYA KAMU TIDAK SALAH BERHARAP",
                    "",
                    "  http.server hanya MENYAJIKAN berkas. Ia tidak menerima data.",
                    "  Formulir — yang akan kamu pelajari beberapa materi lagi — tetap",
                    "  belum menyimpan apa pun meski servernya menyala. Menekan tombol",
                    "  kirim pada <form method=\"post\"> dijawab dengan",
                    "",
                    "    Unsupported method ('POST')",
                    "",
                    "  dan kode 501. Yang kurang bukan servernya, melainkan program yang",
                    "  MENGOLAH kiriman itu — dan menulis program semacam itu adalah",
                    "  pekerjaan bahasa lain (Python, PHP, JavaScript di Node), bukan",
                    "  HTML. Sampai situ tiba, http.server sudah menyelesaikan satu",
                    "  masalahmu: halamanmu kini punya alamat http yang benar.",
                ],
            },
            {
                "body": [
                    "Sekarang daftar bentuk href di materi tautan dan gambar bisa dibaca",
                    "ulang dengan lengkap. Anggap alamat-alamat ini ditulis di berkas",
                    "kopi/halaman/menu.html, dan halaman itu dibuka dengan dua cara:",
                    "",
                    "  A = file:///home/levi/kopi/halaman/menu.html   (klik dua kali)",
                    "  B = http://localhost:8000/halaman/menu.html    (lewat server)",
                    "",
                    "  ditulis            jadi apa di A (file://)           jadi apa di B",
                    "  -----------------  --------------------------------  ------------------",
                    "  gaya.css           /home/levi/kopi/halaman/gaya.css  /halaman/gaya.css",
                    "  ../gaya.css        /home/levi/kopi/gaya.css          /gaya.css",
                    "  /gaya.css          /gaya.css  <- akar DISK, kosong   /gaya.css  <- benar",
                    "  /gambar/foto.jpg   /gambar/foto.jpg  <- tidak ada    /gambar/foto.jpg",
                    "  #kontak            tetap di halaman ini              tetap di halaman ini",
                    "  https://mdn.test/  sama saja                         sama saja",
                    "",
                    "Bacalah kolom terakhir sekali lagi. Bentuk berakar dan bentuk",
                    "relatif SAMA-SAMA benar begitu ada server; yang berbeda cuma",
                    "kebiasaan:",
                    "",
                    "  /gambar/foto.jpg   selalu sama, dari halaman mana pun ditulis.",
                    "                     Aman untuk header, menu, dan logo yang dipakai",
                    "                     ulang di banyak halaman.",
                    "  ../gambar/foto.jpg ikut berubah kalau berkasnya dipindah folder.",
                    "                     Aman untuk situs kecil yang dibuka tanpa server.",
                    "",
                    "JALUR PEKA HURUF BESAR-KECIL — dan mesinmu menyembunyikannya",
                    "",
                    "  Nama tag tidak peka huruf besar-kecil (Materi 1). Nama BERKAS",
                    "  urusannya lain, dan jawabannya tergantung sistem operasi:",
                    "",
                    "    Windows dan macOS   Gambar/Foto.JPG = gambar/foto.jpg",
                    "    Linux               Gambar/Foto.JPG BUKAN gambar/foto.jpg",
                    "",
                    "  Hampir semua server web di dunia berjalan di atas Linux. Jadi",
                    "  inilah rangkaian kejadian yang mengejutkan banyak orang:",
                    "",
                    "    1. Berkasnya bernama Biji-Kopi.JPG, kamu menulis biji-kopi.jpg.",
                    "    2. Di laptopmu gambarnya muncul. Sempurna.",
                    "    3. Situsnya diunggah, dibuka dari internet — gambarnya hilang.",
                    "    4. Kodenya tidak kamu sentuh sama sekali.",
                    "",
                    "  Servernya benar. Laptopmu yang selama ini memaafkanmu.",
                    "",
                    "  Kabar baiknya: server lokal di bagian sebelumnya berjalan di",
                    "  sistemmu sendiri, jadi kalau kamu memakai Linux ia menangkap ini",
                    "  hari ini juga — 404 di terminal, bukan kejutan sebulan kemudian.",
                    "",
                    "  Aturan praktis yang menutup seluruh kelas masalah ini:",
                    "    - nama berkas huruf kecil semua",
                    "    - tanpa spasi; pakai tanda hubung: biji-kopi.jpg",
                    "    - tanpa huruf beraksen dan tanda baca selain - dan _",
                    "",
                    "  Spasi disebut karena ia punya penyakitnya sendiri: spasi tidak",
                    "  sah di dalam URL, jadi \"biji kopi.jpg\" berubah jadi",
                    "  biji%20kopi.jpg di alamat. Bekerja, tapi setiap alamat jadi",
                    "  sulit dibaca dan sulit disalin.",
                ],
            },
            {
                "heading": "base: satu baris di head yang mengubah arti semua alamat",
                "body": [
                    "Materi tautan dan gambar menyuruhmu menghafal daftar elemen kosong",
                    "— img, br, hr, input, meta, link, source, col, area, base — dan",
                    "'base' satu-satunya yang lewat tanpa penjelasan. Inilah gunanya,",
                    "sekaligus satu-satunya elemen HTML yang bisa mengubah arti SELURUH",
                    "alamat di halamanmu hanya dari satu baris di head.",
                    "",
                    "  <base href=\"/\">",
                    "",
                    "Artinya: \"semua alamat relatif di halaman ini dihitung dari sini,",
                    "bukan dari lokasi berkasnya\". Potongan di bawah adalah isi berkas",
                    "kopi/halaman/menu.html — satu tingkat di dalam, karena di situlah",
                    "base baru ada gunanya.",
                    "",
                    "Tanpa base, href=\"index.html\" di berkas itu berarti",
                    "/halaman/index.html. Dengan base href=\"/\", ia berarti /index.html.",
                    "Halaman di subfolder mana pun jadi boleh menulis alamat seolah ia",
                    "berada di akar. Itu sebabnya kerangka aplikasi web besar memakainya.",
                    "",
                    "TIGA HAL YANG MEMBUATNYA BERBAHAYA",
                    "",
                    "  1. Ia bekerja diam-diam, dari kejauhan.",
                    "     Yang rusak adalah <img> di baris 30, dan penyebabnya satu",
                    "     baris di head yang bahkan tidak menyebut gambar. Tidak ada",
                    "     error, tidak ada peringatan, dan tidak ada tempat di mana",
                    "     kedua baris itu terlihat bersamaan. Kalau sebuah halaman",
                    "     mencari berkas di tempat yang mustahil, periksa head-nya.",
                    "",
                    "  2. Ia ikut menelan tautan yang cuma berisi tanda pagar.",
                    "     Ini jebakan yang menjerat orang berpengalaman. Alamat yang",
                    "     cuma berisi tanda pagar juga alamat relatif, jadi ia pun",
                    "     dihitung dari base. href=\"#harga\" di contoh bawah TIDAK",
                    "     menggulung halaman ke bawah — ia melompat ke /#harga, yaitu",
                    "     halaman depan. Tombol \"lompat ke bagian ini\" tiba-tiba",
                    "     meninggalkan halamannya.",
                    "",
                    "  3. Urutannya menentukan.",
                    "     <base> harus ditulis SEBELUM elemen mana pun yang memakai",
                    "     alamat. Kalau <link rel=\"stylesheet\"> berdiri di atasnya,",
                    "     baris itu sudah dihitung dengan cara lama, sementara sisanya",
                    "     dihitung dengan cara baru — setengah halaman ikut base,",
                    "     setengahnya tidak.",
                    "",
                    "Karena itu <base> jarang dipakai di situs biasa, dan kamu tidak",
                    "perlu memasangnya. Kenalilah bentuknya saja: supaya saat kamu",
                    "membaca berkas orang lain dan alamatnya tidak masuk akal, kamu",
                    "tahu ke mana harus melihat.",
                ],
                "code": """<head>
  <meta charset="utf-8">
  <base href="/">
  <title>Menu - Kopi Pagi</title>
  <link rel="stylesheet" href="gaya.css">
</head>
<body>
  <h1>Menu</h1>
  <img src="gambar/biji-kopi.jpg" alt="Biji kopi sangrai gelap"
       width="640" height="360">
  <p>Kembali ke <a href="index.html">beranda</a>.</p>
  <p>Lompat ke <a href="#harga">daftar harga</a>.</p>
  <h2 id="harga">Harga</h2>
  <p>Kopi tubruk 12.000. Susu kopi 18.000.</p>
</body>""",
            },
        ],
    },
    {
        "title": "9. Atribut: class, id, dan yang Sering Dipakai",
        "sections": [
            {
                "body": [
                    "Atribut memberi keterangan tambahan pada sebuah elemen.",
                    "",
                    "  <a href=\"menu.html\" class=\"tombol\">Menu</a>",
                    "     ^^^^^^^^^^^^^^^^ ^^^^^^^^^^^^^^",
                    "",
                    "Aturannya:",
                    "  - Selalu di TAG PEMBUKA. Tidak pernah di tag penutup.",
                    "  - Bentuknya nama=\"nilai\", tanpa spasi di sekitar tanda sama.",
                    "  - Nilai dibungkus kutip. Petik ganda atau tunggal sama saja;",
                    "    pakai petik ganda supaya seragam.",
                    "  - Beberapa atribut dipisah spasi.",
                    "  - URUTAN ATRIBUT TIDAK BERARTI APA-APA.",
                    "",
                    "Yang terakhir itu sebabnya aplikasi ini mengurutkan atribut",
                    "secara alfabetis saat mencetak pohon. Dua berkas yang cuma",
                    "berbeda urutan atributnya adalah berkas yang sama, dan",
                    "menyalahkanmu untuk itu tidak masuk akal.",
                    "",
                    "  <img src=\"a.jpg\" alt=\"Kopi\">   dan",
                    "  <img alt=\"Kopi\" src=\"a.jpg\">   keduanya tercetak sebagai:",
                    "",
                    "      img alt=\"Kopi\" src=\"a.jpg\"",
                ]
            },
            {
                "body": [
                    "KAPAN KUTIP SEBENARNYA WAJIB",
                    "",
                    "Baris \"nilai dibungkus kutip\" di atas adalah ANJURAN, bukan",
                    "syarat. Yang benar-benar diwajibkan HTML jauh lebih sempit.",
                    "",
                    "Nilai yang tidak mengandung spasi boleh ditulis polos:",
                    "",
                    "  <input type=text>     sah",
                    "  <td colspan=2>        sah",
                    "  <div class=box>       sah",
                    "",
                    "Kutip baru WAJIB begitu nilainya memuat salah satu dari ini:",
                    "spasi, tanda sama dengan, kurung sudut, atau tanda petik.",
                    "",
                    "  <div class=kotak biru>    RUSAK. Browser membaca class",
                    "                            bernilai \"kotak\", lalu \"biru\"",
                    "                            dikira nama atribut baru.",
                    "  <div class=\"kotak biru\">  benar.",
                    "",
                    "Kenapa ini perlu kamu tahu padahal kamu tidak akan menulisnya:",
                    "mesin template dan kode lama sering mengeluarkan bentuk polos",
                    "itu. Menemukan <input type=text> di berkas orang lain bukan",
                    "menemukan bug, jadi jangan habiskan waktu \"memperbaikinya\".",
                    "",
                    "Untuk tulisanmu sendiri, satu aturan saja: selalu petik ganda.",
                    "Kamu jadi tidak perlu memutuskan apa pun setiap kali, dan nilai",
                    "yang besok kebetulan bertambah satu class tidak berubah jadi",
                    "rusak tanpa kamu sadari.",
                ]
            },
            {
                "heading": "Atribut di berbagai elemen",
                "code": """<article class="kartu kartu-menu" id="menu-tubruk" data-harga="15000">
  <h3 class="judul">Kopi Tubruk</h3>
  <p class="keterangan">Kopi diseduh langsung di dalam gelas.</p>
</article>

<p lang="en" title="Kalimat ini berbahasa Inggris">
  Freshly roasted every morning.
</p>

<p hidden>Baris ini tidak akan tampil sama sekali.</p>

<input type="email" name="surel" required>
<button type="submit" disabled>Kirim</button>"""
            },
            {
                "body": [
                    "PERBEDAAN class DAN id",
                    "",
                    "  class  penanda GOLONGAN.",
                    "         Boleh dipakai berkali-kali di satu halaman.",
                    "         Satu elemen boleh punya beberapa class sekaligus,",
                    "         dipisah spasi: class=\"kartu kartu-menu\".",
                    "",
                    "  id     penanda SATU elemen tertentu.",
                    "         Harus UNIK di seluruh halaman.",
                    "         Satu elemen cuma boleh punya satu id.",
                    "",
                    "Kenapa id harus unik — ini bukan aturan formalitas:",
                    "  - <a href=\"#kontak\"> melompat ke id \"kontak\". Kalau ada dua,",
                    "    tidak ada yang tahu ke mana halaman harus melompat.",
                    "  - <label for=\"nama\"> mengikat label ke input ber-id \"nama\".",
                    "    id kembar membuat ikatan itu menunjuk ke elemen yang salah.",
                    "  - JavaScript getElementById selalu mengembalikan yang PERTAMA",
                    "    saja, diam-diam. Elemen kedua seolah tidak ada.",
                    "",
                    "Panduan praktis:",
                    "  Mulai dengan class. Pakai id hanya kalau kamu benar-benar",
                    "  perlu menunjuk satu elemen: target tautan dalam-halaman,",
                    "  pasangan label-input, atau titik pegangan untuk JavaScript.",
                    "",
                    "Beri nama menurut ARTINYA, bukan menurut tampilannya.",
                    "  class=\"merah\"       jadi bohong begitu warnanya diganti",
                    "  class=\"peringatan\"  tetap benar selamanya",
                ]
            },
            {
                "body": [
                    "Atribut global — boleh dipasang di elemen APA PUN:",
                    "",
                    "  class     golongan, untuk CSS dan JS",
                    "  id        penanda unik",
                    "  title     keterangan yang muncul saat kursor berhenti di atas",
                    "  lang      bahasa isi elemen ini, kalau beda dari halamannya",
                    "  hidden    sembunyikan elemen sepenuhnya",
                    "  style     CSS langsung di elemen itu",
                    "  data-*    datamu sendiri, nama bebas sesudah 'data-'",
                    "",
                    "Tentang style: ia bekerja, tapi hindari. CSS yang ditempel di",
                    "tiap elemen berarti mengubah satu warna harus dikerjakan di",
                    "lima puluh tempat. Itu alasan CSS diciptakan.",
                    "",
                    "Tentang title: jangan menyimpan informasi PENTING di sana.",
                    "Ia tidak muncul di layar sentuh sama sekali, dan pengguna",
                    "keyboard tidak selalu bisa memunculkannya.",
                    "",
                    "Tentang data-*: tempat menyimpan nilai untuk JavaScript tanpa",
                    "menyalahgunakan class. data-harga=\"15000\" tidak berarti apa-apa",
                    "bagi browser, dan itu memang tujuannya.",
                ]
            },
            {
                "body": [
                    "ATRIBUT BOOLEAN — jebakan yang mengenai hampir semua pemula",
                    "",
                    "Contoh di bawah ini memakai <button> dan <input>, dua isian",
                    "formulir yang belum dibahas dan memang belum perlu kamu kuasai",
                    "sekarang. Anggap saja keduanya \"tombol\" dan \"kotak isian\";",
                    "cara kerjanya dibongkar tuntas nanti di materi formulir. Yang",
                    "sedang diperhatikan di sini cuma BENTUK atributnya.",
                    "",
                    "Beberapa atribut tidak punya nilai. Yang menentukan adalah",
                    "ADA atau TIDAK ADA-nya atribut itu.",
                    "",
                    "  <button disabled>            tombol mati",
                    "  <button>                     tombol hidup",
                    "",
                    "  <button disabled=\"false\">    TOMBOL TETAP MATI",
                    "  <button disabled=\"\">         TOMBOL TETAP MATI",
                    "",
                    "Tulisan \"false\" sama sekali tidak dibaca. Browser cuma melihat",
                    "bahwa atributnya ADA. Satu-satunya cara menghidupkan tombolnya",
                    "adalah MENGHAPUS atribut itu.",
                    "",
                    "Yang termasuk atribut boolean:",
                    "  disabled  required  checked  selected  readonly  multiple",
                    "  hidden    autofocus  novalidate  reversed  open  loop",
                    "",
                    "Sebagian besar nama itu urusan formulir dan datang di materinya",
                    "sendiri. Tiga yang tidak, supaya daftarnya tidak jadi hafalan",
                    "tanpa wajah:",
                    "",
                    "  reversed  milik <ol>, dan sudah lewat di daftar atributnya:",
                    "            ada = nomornya menghitung mundur.",
                    "  open      milik <details> dan <dialog>, yaitu bagian yang",
                    "            bisa dilipat dan kotak dialog. Ada = sedang",
                    "            terbuka.",
                    "  loop      milik <video> dan <audio>. Ada = diputar ulang",
                    "            dari awal begitu habis.",
                    "",
                    "Ketiganya berperilaku sama persis dengan disabled tadi:",
                    "loop=\"false\" tetap mengulang, dan open=\"\" tetap terbuka.",
                    "",
                    "Dalam pohon struktur, atribut boolean tercetak tanpa nilai:",
                    "",
                    "  input name=\"surel\" required type=\"email\"",
                    "  button disabled type=\"submit\" \"Kirim\"",
                ]
            },
        ],
    },
    {
        "title": "10. Menempelkan CSS dan JavaScript: style, script, dan Atribut on*",
        "sections": [
            {
                "body": [
                    "Sampai sini semua yang kamu tulis DIAM saja. HTML menandai arti, lalu",
                    "selesai. Tidak ada yang berubah warna, tidak ada yang bereaksi saat diklik.",
                    "",
                    "Warna diurus CSS. Reaksi diurus JavaScript. Tapi keduanya bukan HTML, dan",
                    "keduanya tidak masuk ke halaman dengan sendirinya — HTML-lah yang harus",
                    "MEMANGGIL mereka. Itu isi materi ini: bukan cara menulis CSS atau",
                    "JavaScript-nya, tapi cara menempelkannya.",
                    "",
                    "Ada enam pintu masuk, dan hampir tiap berkas HTML memakai beberapa",
                    "sekaligus:",
                    "",
                    "  Yang dipanggil   Ditulis sebagai           Kena siapa",
                    "  ---------------  ------------------------  ---------------",
                    "  CSS berkas lain  <link rel=\"stylesheet\">   seluruh halaman",
                    "  CSS di halaman   elemen <style>            seluruh halaman",
                    "  CSS satu elemen  atribut style=\"...\"       elemen itu saja",
                    "  JS berkas lain   <script src=\"app.js\">     seluruh halaman",
                    "  JS di halaman    elemen <script>           seluruh halaman",
                    "  JS satu elemen   atribut onclick=\"...\"     elemen itu saja",
                    "",
                    "Perhatikan polanya: tiga baris atas dan tiga baris bawah bentuknya sama",
                    "persis. Sekali paham tiga baris atasnya, tiga baris bawahnya ikut terbaca.",
                    "",
                    "Tiga baris CSS itu dibahas tuntas di kursus CSS materi 1 — di sini kita",
                    "cuma perlu bentuk HTML-nya, dan perlu MEMBANDINGKANNYA dengan yang JS.",
                    "Tiga baris bawah belum pernah muncul sekali pun di kursus ini, padahal",
                    "<script> ada di hampir setiap halaman yang kamu buka hari ini.",
                ],
            },
            {
                "heading": "Enam-enamnya dalam satu halaman",
                "code": """<!doctype html>
<html lang="id">
<head>
  <meta charset="utf-8">
  <title>Kopi Pagi</title>

  <!-- 1. CSS dari berkas lain -->
  <link rel="stylesheet" href="gaya.css">

  <!-- 2. CSS ditulis di halaman ini -->
  <style>
    .habis { color: #8a8a8a; }
  </style>

  <!-- 4. JavaScript dari berkas lain -->
  <script src="app.js" defer></script>
</head>
<body>
  <!-- 3. CSS untuk satu elemen ini saja -->
  <h1 style="color: #6f4e37">Kopi Pagi</h1>

  <p class="habis">Kopi tubruk sedang kosong.</p>

  <!-- 6. JavaScript di dalam atribut -->
  <button onclick="alert('Halo!')">Sapa</button>

  <noscript>
    <p>Tombol di atas butuh JavaScript, dan JavaScript sedang mati.</p>
  </noscript>

  <!-- 5. JavaScript ditulis di halaman ini -->
  <script>
    var tombol = document.querySelector("button");
    tombol.textContent = "Sapa (siap)";
  </script>
</body>
</html>""",
            },
            {
                "body": [
                    "ELEMEN <style> vs ATRIBUT style — nama sama, ISI BEDA BENTUK",
                    "",
                    "  Ini yang paling sering tertukar, karena namanya memang sama.",
                    "",
                    "    <style>                          <h1 style=\"color: #6f4e37\">",
                    "      .habis { color: #8a8a8a; }",
                    "    </style>",
                    "",
                    "  Elemen <style> berisi ATURAN CSS utuh: ada pemilih, ada kurung kurawal,",
                    "  ada titik koma. Jangkauannya seluruh halaman.",
                    "",
                    "  Atribut style berisi DEKLARASI SAJA — tanpa pemilih, tanpa kurawal.",
                    "  Pemilihnya sudah jelas: elemen tempat atribut itu menempel.",
                    "",
                    "  Menulis \"h1 { color: red }\" di dalam atribut style tidak bekerja, dan",
                    "  seperti biasa CSS tidak berteriak. Tulisannya cuma dibuang diam-diam.",
                    "  Sebaliknya, menulis \"color: red\" telanjang di dalam elemen <style>",
                    "  juga dibuang: di sana browser sedang mencari pemilih.",
                    "",
                    "",
                    "<script src=\"...\"> WAJIB PUNYA TAG PENUTUP",
                    "",
                    "    <script src=\"app.js\"></script>     benar",
                    "    <script src=\"app.js\" />            RUSAK",
                    "",
                    "  Lihat baik-baik yang benar: tag pembuka dan penutupnya menempel, tidak",
                    "  ada apa pun di antaranya. Rasanya mubazir. Tapi tetap wajib, karena",
                    "  <script> BUKAN elemen kosong.",
                    "",
                    "  Ingat daftar hafalan di materi 7: img, br, hr, input, meta, link,",
                    "  source, col, area, base, embed, track, wbr. <script> tidak ada di",
                    "  situ. Ia satu-satunya elemen yang sering TERLIHAT kosong padahal",
                    "  bukan — dan itu sebabnya jebakan ini kena ke orang yang justru",
                    "  sudah hafal daftarnya.",
                    "",
                    "  Akibat kalau ditutup dengan garis miring: garis miringnya DIABAIKAN.",
                    "  Elemen script-nya tetap terbuka, dan browser menelan seluruh sisa",
                    "  halaman — h1, p, tabel, footer, semuanya — sebagai isi skrip. Yang",
                    "  tampil cuma halaman kosong melompong. Tanpa satu pun pesan error.",
                    "",
                    "  Bandingkan dengan <img /> di materi 7 yang memang sah. Garis miring",
                    "  penutup diri hanya boleh pada elemen yang MEMANG kosong.",
                    "",
                    "  Catatan jujur: pembaca HTML di aplikasi ini lebih pemaaf daripada",
                    "  browser dan tetap memisahkan keduanya, jadi jebakan ini TIDAK terlihat",
                    "  di pohon struktur. Browser sungguhan tidak semaaf itu.",
                    "",
                    "",
                    "ISI <script> DAN <style> BUKAN TEKS HTML",
                    "",
                    "  Di materi 3 kamu belajar spasi berturut-turut dipadatkan jadi satu.",
                    "  Di dalam <script> dan <style> aturan itu TIDAK berlaku: isinya",
                    "  diserahkan apa adanya ke mesin JavaScript atau CSS.",
                    "",
                    "  Ikutannya: tanda < dan & di dalamnya tidak perlu ditulis &lt; dan",
                    "  &amp;. \"if (a < b)\" ditulis apa adanya, dan justru RUSAK kalau kamu",
                    "  merapikannya jadi \"if (a &lt; b)\" — mesin JavaScript tidak mengerti",
                    "  entitas HTML.",
                    "",
                    "  Tapi ada satu rangkaian huruf yang tetap mengakhiri skrip, di mana pun",
                    "  ia muncul. Termasuk di tengah sebuah string:",
                    "",
                    "    <script>",
                    "      var t = \"</script>\";",
                    "      alert(t);",
                    "    </script>",
                    "",
                    "  Pohon strukturnya membongkar apa yang sebenarnya terjadi:",
                    "",
                    "    script \"var t = \"\"",
                    "    \"\"; alert(t);\"",
                    "",
                    "  Skripnya berakhir di tengah string. Sisanya bocor keluar jadi teks",
                    "  biasa di halaman, dan </script> yang kedua menutup sesuatu yang sudah",
                    "  tidak terbuka. Jalan keluarnya memotong kata itu: \"<\\/script>\".",
                ],
            },
            {
                "heading": "Empat cara memuat app.js, dan dua skrip tanpa src",
                "code": """<!-- Polos: menghentikan penggambaran halaman di titik ini. -->
<script src="app.js"></script>

<!-- Diunduh sambil halaman digambar, dijalankan setelah halaman siap. -->
<script src="app.js" defer></script>

<!-- Diunduh sambil jalan, dijalankan begitu tiba. Urutan tidak terjaga. -->
<script src="app.js" async></script>

<!-- Modul: sudah defer dengan sendirinya, dan boleh memakai import. -->
<script src="app.js" type="module"></script>

<!-- Skrip yang ditulis langsung di halaman, tanpa src. -->
<script>
  document.querySelector("#pesan").textContent = "Siap.";
</script>

<script type="module">
  import { seduh } from "./seduh.js";
  seduh(15, 250);
</script>""",
            },
            {
                "body": [
                    "KENAPA <script> BIASANYA DITARUH MENJELANG </body>",
                    "",
                    "  Browser menggambar halaman dari atas ke bawah. Begitu ia bertemu",
                    "  <script> polos, ia BERHENTI menggambar: unduh berkasnya dulu,",
                    "  jalankan sampai selesai, baru lanjut.",
                    "",
                    "  Skrip berat di dalam <head> berarti layar putih selama unduhan itu,",
                    "  padahal seluruh teks halamanmu sudah siap di baris berikutnya.",
                    "",
                    "  Alasan kedua sama pentingnya: skrip yang jalan di dalam <head> belum",
                    "  bisa melihat isi body — elemennya belum ada. getElementById (materi 9)",
                    "  mengembalikan null, dan barisnya mati dengan pesan yang tidak",
                    "  menyebut-nyebut soal urutan sama sekali.",
                    "",
                    "  Menaruhnya tepat sebelum </body> menyelesaikan dua-duanya: halaman",
                    "  sudah tergambar, dan semua elemen sudah ada.",
                    "",
                    "",
                    "defer, async, DAN type=\"module\"",
                    "",
                    "  Cara yang dipakai sekarang justru berbeda: taruh di <head>, tambahkan",
                    "  defer. Unduhannya berjalan bersamaan dengan penggambaran halaman,",
                    "  jadi tidak ada yang perlu menunggu siapa pun.",
                    "",
                    "  Ditulis                Diunduh           Dijalankan",
                    "  --------------------   ---------------   ----------------------",
                    "  polos, tanpa apa-apa   menghentikan      begitu selesai diunduh",
                    "  defer                  sambil jalan      setelah halaman siap",
                    "  async                  sambil jalan      begitu tiba",
                    "  type=\"module\"          sambil jalan      setelah halaman siap",
                    "",
                    "  Beda defer dan async bukan cuma soal kapan, tapi soal URUTAN:",
                    "",
                    "    defer  berkas dijalankan sesuai urutan penulisannya. Kalau app.js",
                    "           butuh sesuatu dari inti.js, urutan itu terjaga.",
                    "    async  siapa tiba duluan, dia jalan duluan. Urutannya berubah-ubah",
                    "           tiap kali halaman dimuat, tergantung kecepatan jaringan.",
                    "           Pakai hanya untuk skrip yang benar-benar berdiri sendiri.",
                    "",
                    "  defer dan async HANYA berpengaruh kalau ada src. Menempelkannya pada",
                    "  <script> biasa yang berisi kode langsung tidak mengubah apa-apa, dan",
                    "  tidak ada yang memberi tahu kamu.",
                    "",
                    "  type=\"module\" sudah defer dengan sendirinya, jadi tidak perlu ditulis",
                    "  dua-duanya. Ia juga satu-satunya bentuk yang boleh memakai import,",
                    "  dan variabel di dalamnya tidak bocor ke seluruh halaman.",
                    "",
                    "",
                    "ATRIBUT on* — SATU-SATUNYA ATRIBUT YANG ISINYA KODE",
                    "",
                    "    <button onclick=\"alert('Halo!')\">Sapa</button>",
                    "",
                    "  Yang sering terlihat: onclick, onsubmit, onchange, oninput, onload.",
                    "  Polanya \"on\" + nama peristiwa.",
                    "",
                    "  Isinya JavaScript, bukan teks dan bukan nilai. Itu sebabnya on* tidak",
                    "  ikut daftar atribut global di materi 9: yang di sana semuanya",
                    "  keterangan tentang elemen, yang ini perintah untuk dijalankan.",
                    "",
                    "  Kutipnya jadi berlapis karena itu. Nilai atribut sudah dibungkus petik",
                    "  ganda, jadi string di dalamnya harus petik tunggal.",
                    "",
                    "  KENAPA DIANGGAP USANG — dan kenapa tetap wajib kamu kenali:",
                    "    - Perilaku bercampur markup. Mencari \"apa yang terjadi kalau tombol",
                    "      ini diklik\" berarti menyisir seluruh berkas HTML, bukan membuka",
                    "      app.js.",
                    "    - Satu elemen cuma punya satu onclick. Kalau dua hal harus terjadi,",
                    "      keduanya dijejalkan ke dalam satu atribut yang sama.",
                    "    - Content-Security-Policy — pengaturan keamanan yang dipasang hampir",
                    "      semua situs sungguhan — MEMBLOKIRNYA. Tombolnya diam saja, dan",
                    "      keluhannya cuma muncul di console browser.",
                    "",
                    "  Penggantinya addEventListener, dan itu urusan kursus JavaScript.",
                    "  Kenali on* karena kode lama dan tutorial penuh dengannya; tulis",
                    "  sendiri seperlunya saja.",
                    "",
                    "",
                    "<noscript> — UNTUK YANG JAVASCRIPT-NYA MATI",
                    "",
                    "  Isinya tampil HANYA kalau JavaScript tidak jalan. Kalau jalan, isinya",
                    "  diabaikan seolah tidak pernah ditulis.",
                    "",
                    "  Itu terjadi lebih sering dari dugaan: pemblokir skrip, jaringan yang",
                    "  memutus berkas .js di tengah unduhan, mode hemat data, peramban lama.",
                    "",
                    "  Pakai untuk memberi tahu apa yang hilang, bukan untuk memarahi:",
                    "",
                    "    <noscript>",
                    "      <p>Peta lokasi butuh JavaScript. Alamatnya: Jalan Melati 7.</p>",
                    "    </noscript>",
                    "",
                    "  <noscript> boleh di head maupun body, tapi yang di head hanya boleh",
                    "  berisi link, style, dan meta.",
                    "",
                    "",
                    "POHON STRUKTUR halaman contoh di atas:",
                    "",
                    "  <!doctype html>",
                    "  html lang=\"id\"",
                    "    head",
                    "      meta charset=\"utf-8\"",
                    "      title \"Kopi Pagi\"",
                    "      link href=\"gaya.css\" rel=\"stylesheet\"",
                    "      style \".habis { color: #8a8a8a; }\"",
                    "      script defer src=\"app.js\"",
                    "    body",
                    "      h1 style=\"color: #6f4e37\" \"Kopi Pagi\"",
                    "      p class=\"habis\" \"Kopi tubruk sedang kosong.\"",
                    "      button onclick=\"alert('Halo!')\" \"Sapa\"",
                    "      noscript",
                    "        p \"Tombol di atas butuh JavaScript, dan JavaScript sedang mati.\"",
                    "      script \"var tombol = document.querySelector(\"button\"); tombol.textC…\"",
                    "",
                    "Tiga hal yang layak kamu perhatikan di pohon itu:",
                    "",
                    "  1. Isi <style> dan <script> tercetak sebagai TEKS elemen, di dalam",
                    "     kutip, persis seperti teks di dalam <p>. Bagi HTML memang itulah",
                    "     statusnya: sederet huruf yang diserahkan ke mesin lain. Yang",
                    "     kepanjangan dipotong dan diberi tanda …",
                    "",
                    "  2. defer tercetak tanpa nilai, sama seperti atribut boolean di materi",
                    "     6. async juga begitu.",
                    "",
                    "  3. Komentar <!-- ... --> tidak muncul sama sekali. Ia bukan bagian",
                    "     dari struktur halaman, cuma catatan untuk yang membaca berkasnya.",
                ],
            },
        ],
    },
    {
        "title": "11. Elemen Semantik: header, nav, main, article, footer",
        "sections": [
            {
                "body": [
                    "Semantik artinya MAKNA. Elemen semantik adalah elemen yang",
                    "menyebutkan perannya sendiri.",
                    "",
                    "Bandingkan dua kode yang tampilannya persis sama:",
                    "",
                    "  <div class=\"header\">      <header>",
                    "    <div class=\"judul\">       <h1>Blog Kopi Pagi</h1>",
                    "      Blog Kopi Pagi        </header>",
                    "    </div>",
                    "  </div>",
                    "",
                    "Yang kiri: browser cuma melihat dua kotak tanpa arti. Tulisan",
                    "\"header\" di dalam class tidak berarti apa-apa baginya — itu",
                    "cuma nama yang kamu karang, sama saja dengan class=\"kotak7\".",
                    "",
                    "Yang kanan: browser tahu ini kepala halaman, dan h1 adalah",
                    "judulnya.",
                    "",
                    "Penyakitnya punya nama: div soup. Halaman yang seluruhnya",
                    "tersusun dari div bersarang, sampai tidak ada satu pun elemen",
                    "yang bisa dikenali tanpa membaca nama class-nya.",
                ]
            },
            {
                "heading": "Halaman dengan elemen semantik",
                "code": """<!doctype html>
<html lang="id">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Blog Kopi Pagi</title>
</head>
<body>
  <header>
    <h1>Blog Kopi Pagi</h1>
    <p>Catatan harian tentang seduhan.</p>
  </header>

  <nav>
    <ul>
      <li><a href="index.html">Beranda</a></li>
      <li><a href="tulisan.html">Tulisan</a></li>
      <li><a href="tentang.html">Tentang</a></li>
    </ul>
  </nav>

  <main>
    <article>
      <h2>Kenapa airnya 92 derajat</h2>
      <p>Air mendidih membakar bubuk dan meninggalkan rasa pahit
         yang tidak bisa dihilangkan gula.</p>
    </article>

    <article>
      <h2>Menyimpan biji supaya awet</h2>
      <p>Wadah kedap udara, jauh dari cahaya, dan jangan di kulkas.</p>
    </article>
  </main>

  <aside>
    <h2>Sedang banyak dibaca</h2>
    <ul>
      <li><a href="gula-aren.html">Resep kopi susu gula aren</a></li>
    </ul>
  </aside>

  <footer>
    <p>&copy; 2024 Kopi Pagi. Jalan Melati 7, Bandung.</p>
  </footer>
</body>
</html>"""
            },
            {
                "body": [
                    "Arti masing-masing elemen:",
                    "",
                    "  <header>   kepala. Judul, logo, slogan.",
                    "             Boleh lebih dari satu: tiap article boleh punya",
                    "             header sendiri.",
                    "",
                    "  <nav>      kumpulan tautan navigasi UTAMA. Bukan setiap",
                    "             kelompok tautan perlu nav — tautan di dalam",
                    "             paragraf tidak.",
                    "",
                    "  <main>     isi utama halaman ini. SATU saja per halaman,",
                    "             dan tidak boleh memuat apa pun yang berulang di",
                    "             halaman lain (menu, footer, iklan sidebar).",
                    "",
                    "  <article>  potongan yang BERDIRI SENDIRI. Ujinya begini:",
                    "             kalau dipindah ke halaman lain apa adanya, masih",
                    "             masuk akal? Satu tulisan blog, satu komentar,",
                    "             satu kartu produk: ya. Bagian \"Alat\" dari sebuah",
                    "             panduan: tidak.",
                    "",
                    "  <section>  kelompok bertema di dalam satu dokumen. Hampir",
                    "             selalu punya heading di dalamnya. Kalau kamu",
                    "             tidak bisa memberinya judul, kemungkinan besar",
                    "             yang kamu butuhkan div.",
                    "",
                    "  <aside>    isi sampingan: kotak \"baca juga\", catatan kaki,",
                    "             iklan. Menghapusnya tidak merusak isi utama.",
                    "",
                    "  <footer>   kaki. Hak cipta, alamat, tautan sekunder.",
                ]
            },
            {
                "body": [
                    "KENAPA SEMANTIK LEBIH BAIK DARIPADA div DI MANA-MANA",
                    "",
                    "1. Pembaca layar bisa MELOMPAT antar bagian.",
                    "   header, nav, main, aside, footer terdaftar sebagai landmark.",
                    "   Pengguna tunanetra menekan satu tombol untuk lompat langsung",
                    "   ke main, melewati menu yang sama di setiap halaman. Dengan",
                    "   div, tidak ada yang bisa dilompati: satu-satunya cara sampai",
                    "   ke isi adalah mendengarkan seluruh menu, di setiap halaman,",
                    "   setiap kali.",
                    "",
                    "2. Mesin pencari tahu mana isi dan mana pelengkap.",
                    "   Teks di dalam main dinilai berbeda dari teks di dalam nav.",
                    "",
                    "3. Mode baca browser bisa bekerja.",
                    "   Fitur \"tampilan baca\" mencari article dan main. Halaman",
                    "   div soup biasanya gagal diringkas dan tombolnya tidak muncul.",
                    "",
                    "4. Kodenya bisa dibaca manusia — termasuk kamu, enam bulan lagi.",
                    "   </div></div></div></div> di akhir berkas tidak memberi tahu",
                    "   siapa pun div mana yang baru saja ditutup.",
                    "",
                    "div TIDAK dilarang. div adalah pilihan yang BENAR ketika sebuah",
                    "elemen memang tidak punya makna dan cuma dibutuhkan sebagai",
                    "pembungkus untuk tata letak. Aturannya: pakai elemen bermakna",
                    "kalau ada yang cocok, dan div kalau tidak ada.",
                    "",
                    "Hal yang sama berlaku untuk <span>: itu versi sebaris dari div,",
                    "pembungkus tanpa makna untuk sepotong teks di tengah kalimat.",
                ]
            },
        ],
    },
    {
        "title": "12. Gambar Lanjutan: srcset, picture, lazy, dan SVG Sebaris",
        "sections": [
            {
                "body": [
                    "Materi 7 mengajarkan bentuk inti <img>: src, alt, width, height.",
                    "Itu benar dan tidak berubah. Tapi buka kode situs mana pun hari",
                    "ini, dan hampir tidak ada satu pun <img> yang sependek itu.",
                    "",
                    "Dua atribut yang paling sering menempel, dan hampir selalu",
                    "muncul berpasangan:",
                    "",
                    "  loading=\"lazy\"     jangan unduh sekarang. Tunggu sampai",
                    "                     gambarnya hampir tergulir ke layar.",
                    "  decoding=\"async\"   boleh membongkar gambarnya di belakang",
                    "                     layar; jangan tahan penggambaran halaman",
                    "                     hanya demi menunggu gambar ini siap.",
                    "",
                    "Kenapa keduanya ada. Halaman berisi 40 gambar dulu mengunduh",
                    "keempat puluhnya sekaligus — termasuk 35 yang tidak akan pernah",
                    "dilihat siapa pun, karena pembacanya berhenti di paragraf ketiga.",
                    "loading=\"lazy\" menunda 35 unduhan itu sampai betul-betul perlu.",
                    "Di paket data terbatas, bedanya bukan soal rasa: itu kuota.",
                    "",
                    "JEBAKAN: gambar PERTAMA halaman justru TIDAK BOLEH lazy.",
                    "",
                    "  Gambar besar paling atas — spanduk, foto utama artikel —",
                    "  adalah benda yang paling ingin dilihat orang lebih dulu.",
                    "  Memberinya loading=\"lazy\" berarti menyuruh browser menunda",
                    "  sesuatu yang sudah jelas terlihat: ia harus menghitung tata",
                    "  letak dulu, baru sadar gambarnya ada di layar, baru mulai",
                    "  mengunduh. Halamannya jadi terasa LEBIH LAMBAT, bukan lebih",
                    "  cepat — persis kebalikan dari yang kamu maksudkan.",
                    "",
                    "  Aturan praktisnya satu kalimat: lazy untuk semua yang di",
                    "  BAWAH lipatan layar, tidak untuk yang sudah kelihatan tanpa",
                    "  menggulir sedikit pun.",
                    "",
                    "  Untuk gambar utama itu justru ada kebalikannya:",
                    "",
                    "    fetchpriority=\"high\"   dahulukan unduhan yang satu ini",
                    "                           di atas semua permintaan lain",
                    "",
                    "  Cukup satu per halaman. Kalau semuanya berprioritas tinggi,",
                    "  tidak ada yang berprioritas tinggi.",
                ],
            },
            {
                "heading": "Gambar responsif seperti di kode nyata",
                "code": """<!doctype html>
<html lang="id">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Galeri Kopi Pagi</title>
</head>
<body>
  <h1>Galeri Kopi Pagi</h1>

  <!-- Gambar utama, terlihat tanpa menggulir: TIDAK lazy. -->
  <img src="gambar/spanduk-960.jpg"
       srcset="gambar/spanduk-480.jpg 480w, gambar/spanduk-960.jpg 960w"
       sizes="(max-width: 600px) 100vw, 960px"
       alt="Barista menuang susu berpola daun ke atas espresso"
       width="960" height="540" fetchpriority="high">

  <h2>Alat seduh</h2>

  <!-- Format berbeda: yang paling irit ditaruh paling atas. -->
  <picture>
    <source type="image/avif" srcset="gambar/v60.avif">
    <source type="image/webp" srcset="gambar/v60.webp">
    <img src="gambar/v60.jpg"
         alt="Corong V60 keramik putih di atas teko kaca"
         width="640" height="427" loading="lazy" decoding="async">
  </picture>

  <!-- Potongan berbeda: versi tegak khusus untuk layar sempit. -->
  <picture>
    <source media="(max-width: 600px)" srcset="gambar/toko-tegak.jpg">
    <img src="gambar/toko-melebar.jpg"
         alt="Bagian depan kedai dengan kursi kayu di trotoar"
         width="1200" height="500" loading="lazy" decoding="async">
  </picture>
</body>
</html>""",
            },
            {
                "body": [
                    "srcset DIBEDAH KOMA DEMI KOMA",
                    "",
                    "  srcset=\"kopi-480.jpg 480w, kopi-960.jpg 960w, kopi-1440.jpg 1440w\"",
                    "",
                    "  Satu nilai atribut, tapi isinya sebuah DAFTAR:",
                    "",
                    "    kopi-480.jpg 480w    berkas ini, lebar aslinya 480 piksel",
                    "    ,                    pemisah antar pilihan",
                    "    kopi-960.jpg 960w    berkas ini, lebar aslinya 960 piksel",
                    "",
                    "  Kamu menyodorkan SEMUA pilihan; browser yang memilih satu.",
                    "  Yang diunduh tetap satu berkas saja, bukan ketiganya.",
                    "",
                    "  \"Kenapa boleh ada koma di dalam nilai atribut?\" Karena bagi",
                    "  HTML, apa pun di antara dua tanda kutip cuma untaian karakter",
                    "  biasa — ia tidak peduli isinya apa. Yang mengerti arti koma,",
                    "  spasi, dan akhiran w adalah aturan srcset sendiri, dan itu",
                    "  dibaca SESUDAH HTML selesai memisahkan atribut-atributnya.",
                    "  Kamu sudah pernah melihat pola ini tanpa menyadarinya, di",
                    "  content=\"width=device-width, initial-scale=1\" pada meta",
                    "  viewport. Satu-satunya karakter yang tidak boleh muncul",
                    "  mentah di dalam nilai atribut adalah tanda kutip yang sejenis",
                    "  dengan pembungkusnya.",
                    "",
                    "  AKHIRAN w VERSUS x — dua sistem terpisah, jangan dicampur:",
                    "",
                    "    480w   lebar ASLI berkas gambarnya dalam piksel. Perlu",
                    "           ditemani sizes supaya ada gunanya.",
                    "    2x     \"pakai berkas ini di layar berkerapatan 2x\".",
                    "           Tidak perlu sizes. Cocok untuk gambar yang",
                    "           ukurannya memang tetap: avatar, logo, ikon.",
                    "",
                    "    srcset=\"avatar.png 1x, avatar@2x.png 2x\"",
                    "",
                    "  Akhirannya tidak boleh lupa dan tidak boleh px. \"kopi.jpg 480\"",
                    "  dan \"kopi.jpg 480px\" dua-duanya salah, dan yang terjadi bukan",
                    "  error: browser membuang PILIHAN ITU SAJA dari daftar lalu tetap",
                    "  memakai sisanya. Yang kelihatan cuma berkas yang lebih besar",
                    "  ikut terunduh — tanpa satu pun peringatan di mana-mana.",
                    "",
                    "sizes: SEBERAPA LEBAR GAMBARNYA NANTI DIGAMBAR",
                    "",
                    "  sizes=\"(max-width: 600px) 100vw, 960px\"",
                    "",
                    "  Dibaca: kalau lebar layarnya 600px ke bawah, gambar ini akan",
                    "  memenuhi 100% lebar layar; selain itu, lebarnya 960px.",
                    "",
                    "  Kenapa browser perlu diberi tahu, padahal CSS sudah mengatur",
                    "  lebarnya? Karena urutan kerjanya. Browser mulai mengunduh",
                    "  gambar SEBELUM semua berkas CSS selesai diunduh dan dihitung.",
                    "  Kalau ia menunggu CSS dulu, tidak ada gunanya lagi buru-buru",
                    "  memilih berkas terkecil — waktunya sudah telanjur habis.",
                    "  Jadi kamu menyebutkan lebar rencananya di sini, dan ia",
                    "  memilih berdasarkan janjimu itu.",
                    "",
                    "  Konsekuensinya tajam: sizes yang tidak cocok dengan CSS-mu",
                    "  BUKAN error. Tidak ada yang gagal, tidak ada peringatan di",
                    "  mana pun. Yang terjadi cuma browser mengunduh berkas dengan",
                    "  ukuran yang salah, selamanya, diam-diam.",
                    "",
                    "  Dan kalau sizes lupa ditulis sementara srcset memakai w,",
                    "  browser menganggapnya 100vw. Untuk gambar yang sebenarnya",
                    "  kecil, itu berarti ia menarik berkas paling besar tanpa",
                    "  satu pun alasan.",
                    "",
                    "<picture>: KETIKA YANG BERBEDA BUKAN CUMA UKURANNYA",
                    "",
                    "  srcset memilih di antara berkas yang GAMBARNYA SAMA, cuma",
                    "  beda ukuran. <picture> dipakai untuk perbedaan yang lebih",
                    "  besar dari itu:",
                    "",
                    "    format berbeda    .avif dan .webp jauh lebih kecil dari",
                    "                      .jpg, tapi browser lama tidak paham.",
                    "    potongan berbeda  di ponsel pakai versi tegak yang",
                    "                      dipotong rapat; di layar lebar pakai",
                    "                      versi melebar. Ini disebut art direction.",
                    "",
                    "  Aturannya tiga, dan yang ketiga paling sering dilanggar:",
                    "",
                    "  1. Browser membaca <source> dari ATAS ke BAWAH dan berhenti",
                    "     di yang PERTAMA cocok. Taruh yang paling irit paling atas.",
                    "  2. <source> menaruh berkasnya di srcset, BUKAN di src.",
                    "  3. <img> WAJIB ada, dan harus PALING BAWAH. Ia bukan sekadar",
                    "     cadangan darurat — itulah gambar yang sebenarnya. src,",
                    "     alt, width, height, loading semuanya menempel di <img>",
                    "     itu, bukan di <picture> dan bukan di <source>. <picture>",
                    "     sendiri tidak menggambar apa pun; ia cuma pembungkus",
                    "     yang memilih.",
                    "",
                    "  Hapus <img>-nya, dan TIDAK ADA gambar yang muncul — di",
                    "  browser mana pun, termasuk yang mendukung semua formatnya.",
                    "",
                    "  Ingat daftar elemen kosong yang dihafal di Materi 7:",
                    "    img  br  hr  input  meta  link  source  col  area  base",
                    "    embed  track  wbr",
                    "  Inilah pemilik nama \"source\" itu. <source> tidak punya isi",
                    "  dan tidak punya tag penutup, persis seperti <img>. Ia juga",
                    "  dipakai oleh <video> dan <audio> — itu materi berikutnya.",
                ],
            },
            {
                "heading": "SVG sebaris: ikon yang digambar langsung di HTML",
                "code": """<!doctype html>
<html lang="id">
<head>
  <meta charset="utf-8">
  <title>Ikon SVG Sebaris</title>
</head>
<body>
  <p style="color: #b45309">
    <svg viewBox="0 0 24 24" width="20" height="20" fill="none"
         stroke="currentColor" stroke-width="1.7" stroke-linecap="round"
         aria-hidden="true">
      <path d="M12 21a9 9 0 1 0 0-18 9 9 0 0 0 0 18Z" />
      <path d="M12 7.5v5l3 2" />
    </svg>
    Tersimpan 3 menit lalu
  </p>

  <button type="button">
    <svg viewBox="0 0 24 24" width="20" height="20" fill="none"
         stroke="currentColor" stroke-width="1.7" role="img">
      <title>Unduh</title>
      <path d="M12 4v11" />
      <path d="M8 11l4 4 4-4" />
      <path d="M4 19h16" />
    </svg>
  </button>

  <!-- Digambar sekali, disembunyikan, lalu dipanggil berkali-kali. -->
  <svg width="0" height="0" aria-hidden="true">
    <symbol id="bintang" viewBox="0 0 24 24">
      <path d="M12 3.5l2.6 5.6 6 .8-4.4 4.3 1 6-5.2-2.8-5.2 2.8 1-6-4.4-4.3 6-.8Z" />
    </symbol>
  </svg>

  <p style="color: #ca8a04">
    <svg width="20" height="20" fill="currentColor"><use href="#bintang" /></svg>
    <svg width="20" height="20" fill="currentColor"><use href="#bintang" /></svg>
  </p>
</body>
</html>""",
            },
            {
                "body": [
                    "SVG SEBARIS ADALAH BAHASA LAIN YANG DITUMPANGKAN KE HTML",
                    "",
                    "  Ini bagian terpenting materi ini, dan yang paling melegakan:",
                    "  isi <svg> BUKAN HTML. Itu SVG — bahasa gambar tersendiri,",
                    "  dengan daftar elemen dan aturannya sendiri, yang kebetulan",
                    "  memakai tanda kurung siku yang sama sehingga boleh ditempel",
                    "  langsung ke tengah dokumen HTML.",
                    "",
                    "  Yang perlu kamu lakukan saat membaca kode orang lain: kenali",
                    "  <svg ...>, lihat sekilas apa fungsinya (hampir selalu sebuah",
                    "  ikon), lalu LOMPATI sampai </svg>. Isinya memang tidak untuk",
                    "  dibaca manusia. Yang menulisnya pun tidak mengetiknya — ia",
                    "  menyalinnya dari aplikasi gambar atau dari pustaka ikon.",
                    "",
                    "  Kamu sedang melihat contohnya sekarang: aplikasi ini",
                    "  menggambar dua puluh empat ikonnya persis dengan cara di atas.",
                    "",
                    "TIGA HAL YANG MELANGGAR APA YANG BARU SAJA KAMU HAFAL",
                    "",
                    "  1. Nama atributnya PEKA huruf besar-kecil — dan HTML diam-diam",
                    "     menambalnya untukmu, yang justru membuatnya lebih berbahaya.",
                    "",
                    "     Nama yang benar viewBox, dengan B besar. Tapi kalau kamu",
                    "     mengetik viewbox di dalam berkas .html, gambarnya tetap",
                    "     muncul seperti tidak terjadi apa-apa: pembaca HTML punya",
                    "     daftar tambalan kecil yang mengembalikan viewbox jadi",
                    "     viewBox dan preserveaspectratio jadi preserveAspectRatio.",
                    "     Jadi kamu tidak pernah diberi tahu kalau salah.",
                    "",
                    "     Tambalan itu tidak ikut ke dua tempat berikut:",
                    "",
                    "       - Berkas .svg tersendiri. Itu XML sungguhan, dan XML",
                    "         tidak menambal apa pun. viewbox di sana diabaikan",
                    "         total, dan ikonnya menggumpal kecil di pojok kiri",
                    "         atas kotaknya, tidak mau ikut membesar.",
                    "       - JavaScript. setAttribute(\"viewbox\", ...) memasang",
                    "         atribut bernama viewbox yang tidak berarti apa pun",
                    "         bagi siapa pun. Yang benar setAttribute(\"viewBox\").",
                    "",
                    "     Jadi tulis viewBox selalu. Kebiasaan mengetiknya huruf",
                    "     kecil baru menggigit di tempat yang paling sulit dilacak,",
                    "     berbulan-bulan sesudah kamu menulisnya.",
                    "",
                    "     Yang huruf besar di tengah: viewBox, preserveAspectRatio.",
                    "     Yang justru pakai tanda hubung: stroke-width, fill-rule,",
                    "     stroke-linecap. Tidak ada polanya; hafalkan yang sering.",
                    "",
                    "     (Pohon di \"Coba jalankan\" aplikasi ini menulis semua nama",
                    "     atribut dengan huruf kecil, jadi di sana pun kamu akan",
                    "     membaca viewbox. Itu ulah pembacanya. Tulis tetap viewBox.)",
                    "",
                    "  2. <path ... /> menutup dirinya sendiri dengan garis miring,",
                    "     padahal path tidak ada di daftar sepuluh elemen kosong.",
                    "",
                    "     Di dalam <svg>, garis miring itu WAJIB, dan ini bukan soal",
                    "     rapi-rapian. Hilangkan satu saja, dan path SESUDAHNYA jadi",
                    "     ANAK dari path tadi — bersarang makin dalam sampai </svg>.",
                    "     path bukan wadah, jadi anak-anaknya tidak digambar sama",
                    "     sekali: dari ikon panah unduh yang tersusun dari tiga",
                    "     garis, yang tersisa di layar cuma satu garis tegak.",
                    "     Di berkas .svg tersendiri hukumannya lebih keras lagi —",
                    "     XML menolak seluruh berkasnya, dan tidak ada apa pun yang",
                    "     muncul.",
                    "",
                    "     Aturan \"garis miring itu cuma warisan XHTML yang tidak",
                    "     mengubah apa pun\" dari Materi 7 berlaku untuk HTML,",
                    "     tidak untuk isi <svg>.",
                    "",
                    "  3. Atribut d berisi ratusan karakter yang memang tidak untuk",
                    "     dibaca manusia.",
                    "",
                    "     d=\"M12 4v11\" artinya \"pindah (Move) ke titik 12,4 lalu",
                    "     tarik garis vertikal (v) sepanjang 11 satuan\". Boleh tahu,",
                    "     boleh juga tidak. Yang penting: d sepanjang tiga baris",
                    "     bukan tanda ada yang rusak, dan menyuntingnya dengan",
                    "     tangan hampir selalu ide buruk.",
                    "",
                    "fill=\"currentColor\" — KENAPA IKON IKUT WARNA TEKSNYA",
                    "",
                    "  currentColor artinya \"nilai properti color pada elemen ini\".",
                    "  Karena color diwarisi dari induk, ikon yang sama jadi jingga",
                    "  di dalam paragraf jingga dan jadi abu-abu di dalam paragraf",
                    "  abu-abu — tanpa satu baris CSS tambahan dan tanpa berkas",
                    "  gambar kedua. Itu sebabnya ikon SVG sebaris nyaris selalu",
                    "  memakainya. (currentColor dibahas lagi di materi warna CSS.)",
                    "",
                    "  fill mengisi bagian DALAM bentuknya; stroke mewarnai GARIS",
                    "  tepinya. Ikon bergaya garis memakai fill=\"none\" dengan",
                    "  stroke=\"currentColor\"; ikon padat cukup fill=\"currentColor\".",
                    "",
                    "MEMAKAI SATU IKON BERKALI-KALI: <use>",
                    "",
                    "  Menempelkan <svg> yang sama sepuluh kali berarti menyalin",
                    "  ratusan karakter path sepuluh kali. Gantinya: tulis bentuknya",
                    "  SEKALI di dalam <symbol id=\"bintang\">, lalu panggil dengan",
                    "",
                    "    <svg><use href=\"#bintang\" /></svg>",
                    "",
                    "  Tanda pagar itu id yang sama seperti di Materi 9 dan sama",
                    "  seperti tautan <a href=\"#kontak\">. Kode lama menulis",
                    "  xlink:href alih-alih href — bentuk usang yang masih bekerja;",
                    "  kalau kamu menemuinya, itu bukan bug.",
                    "",
                    "DUA ATRIBUT UNTUK PEMBACA LAYAR",
                    "",
                    "  aria-hidden=\"true\"    \"lewati elemen ini\". Untuk ikon yang",
                    "                        cuma menemani teks yang sudah",
                    "                        menjelaskan segalanya. Sepadan dengan",
                    "                        alt=\"\" pada <img>.",
                    "  <title> di dalam svg  nama yang dibacakan, dipasangkan",
                    "                        dengan role=\"img\". Untuk ikon yang",
                    "                        SENDIRIAN jadi makna — tombol yang",
                    "                        isinya cuma gambar panah unduh. Tanpa",
                    "                        ini, tombol itu terdengar sebagai",
                    "                        \"tombol\", titik.",
                    "",
                    "  <title> di dalam <svg> tidak ada hubungannya dengan <title>",
                    "  di <head>. Nama sama, elemen berbeda, tempat berbeda.",
                    "",
                    "KAPAN SEBARIS, KAPAN <img src=\"ikon.svg\">",
                    "",
                    "  Berkas .svg terpisah, dimuat sebagai gambar biasa:",
                    "    + HTML-mu tetap pendek dan enak dibaca",
                    "    + satu berkas, disimpan cache, dipakai di banyak halaman",
                    "    - CSS halamanmu TIDAK bisa masuk ke dalamnya. currentColor",
                    "      tidak berlaku; ganti warna berarti bikin berkas baru.",
                    "",
                    "  SVG sebaris:",
                    "    + bisa diwarnai, dianimasikan, dan diubah lewat CSS dan JS",
                    "    + tidak ada permintaan jaringan tambahan",
                    "    - HTML-mu membengkak; ikon yang muncul di 50 tempat ikut",
                    "      tersalin 50 kali kalau tidak memakai <use>",
                    "",
                    "  Aturan praktis: ikon kecil yang harus ikut warna teks ->",
                    "  sebaris. Logo, ilustrasi besar, gambar berwarna tetap ->",
                    "  <img src=\"...svg\" alt=\"...\">, dengan alt seperti biasa.",
                ],
            },
        ],
    },
    {
        "title": "13. Video, Audio, dan Konten Tersemat lewat iframe",
        "sections": [
            {
                "body": [
                    "Sampai sekarang semua yang kamu sisipkan ke halaman berbentuk satu tag",
                    "kosong: <img src=\"...\"> dan selesai. Video, audio, dan halaman orang",
                    "lain TIDAK begitu — dan menebaknya mirip <img> adalah kesalahan pertama",
                    "yang hampir semua orang buat.",
                    "",
                    "Tiga bentuk baru yang pasti kamu temui begitu membaca kode nyata:",
                    "",
                    "  <video>   pemutar video bawaan browser",
                    "  <audio>   pemutar suara bawaan browser",
                    "  <iframe>  jendela ke DOKUMEN LAIN: peta, video YouTube, formulir",
                    "",
                    "Ketiganya ELEMEN WADAH. Punya tag penutup, dan punya isi di dalamnya.",
                    "Persis kebalikan dari <img> yang justru tidak boleh ditutup (materi",
                    "Tautan dan Gambar).",
                    "",
                    "KENAPA VIDEO BUTUH WADAH, PADAHAL GAMBAR CUKUP SATU TAG",
                    "",
                    "  Satu video sering disediakan dalam BEBERAPA berkas berformat berbeda,",
                    "  dan tiap berkas ditulis sebagai satu <source> di dalam wadahnya.",
                    "",
                    "  Video juga punya takarir — teks yang muncul di bawah gambar — dan itu",
                    "  berkas terpisah lagi, ditulis sebagai <track>.",
                    "",
                    "  Terakhir, wadah itu menyimpan teks cadangan untuk browser yang tidak",
                    "  sanggup memutarnya sama sekali.",
                    "",
                    "Satu atribut src tidak mungkin menampung tiga hal itu sekaligus. Itulah",
                    "seluruh alasan bentuknya berbeda.",
                ],
            },
            {
                "heading": "Video dan audio dengan beberapa sumber",
                "code": """<video controls width="640" height="360"
       poster="gambar/sampul-seduh.jpg" preload="metadata">
  <source src="video/seduh-v60.webm" type="video/webm">
  <source src="video/seduh-v60.mp4" type="video/mp4">
  <track kind="captions" src="teks/seduh-v60.vtt"
         srclang="id" label="Bahasa Indonesia" default>
  <p>Browser ini tidak bisa memutar video.
     <a href="video/seduh-v60.mp4">Unduh berkasnya</a> (14 MB).</p>
</video>

<audio controls preload="none">
  <source src="audio/wawancara-barista.ogg" type="audio/ogg">
  <source src="audio/wawancara-barista.mp3" type="audio/mpeg">
  <p>Browser ini tidak bisa memutar audio.
     <a href="audio/wawancara-barista.mp3">Unduh berkasnya</a>.</p>
</audio>""",
            },
            {
                "body": [
                    "BROWSER MEMAKAI <source> PERTAMA YANG SANGGUP IA PUTAR",
                    "",
                    "  Dua <source> itu bukan dua video. Itu SATU video yang disimpan dalam",
                    "  dua format. Browser membaca dari atas ke bawah, berhenti di yang",
                    "  pertama bisa ia putar, dan tidak pernah melihat sisanya.",
                    "",
                    "  Jadi urutan penulisan = urutan pilihanmu. webm biasanya jauh lebih",
                    "  kecil berkasnya; mp4 dimengerti hampir semua browser. Makanya mp4",
                    "  ditaruh paling bawah, sebagai jaring pengaman.",
                    "",
                    "  Atribut type menyebut format berkasnya. Tanpa type, browser harus",
                    "  mengunduh sepotong tiap berkas dulu untuk menebak isinya. Dengan type,",
                    "  ia cukup membaca markup-mu dan langsung tahu mana yang perlu diambil.",
                    "",
                    "  Salah menulis type berarti berkas itu DILEWATI, walaupun sebenarnya",
                    "  bisa diputar. Yang paling sering salah: mp3 ditulis \"audio/mpeg\",",
                    "  bukan \"audio/mp3\". Nama itu memang tidak masuk akal, dan memang harus",
                    "  dihafal.",
                    "",
                    "  <source> adalah elemen kosong. Tidak ada </source>. Bentuknya sama",
                    "  dengan <source> di dalam <picture>, tapi tugasnya berbeda: di <picture>",
                    "  ia memilih berdasarkan LEBAR LAYAR, di <video> berdasarkan FORMAT.",
                    "",
                    "  Kalau kamu memang cuma punya satu format, bentuk pendeknya juga sah:",
                    "",
                    "    <video src=\"video/seduh-v60.mp4\" controls width=\"640\" height=\"360\">",
                    "    </video>",
                    "",
                    "  Perhatikan </video>-nya tetap ditulis, walau isinya kosong.",
                    "",
                    "TEKS CADANGAN DI DALAM WADAH — INI BUKAN alt",
                    "",
                    "  <p> yang ada di dalam <video> adalah HTML sungguhan: boleh berisi",
                    "  tautan, boleh berisi apa saja. Tapi cara kerjanya berbeda dari alt:",
                    "",
                    "    alt pada <img>   selalu tersedia untuk pembaca layar, bahkan saat",
                    "                     gambarnya tampil sempurna.",
                    "    isi <video>      ditampilkan HANYA kalau browsernya tidak mengenal",
                    "                     tag <video> sama sekali.",
                    "",
                    "  Dan itu praktis tidak pernah terjadi lagi sekarang. Yang TIDAK ia",
                    "  tutupi: kalau semua <source> gagal diputar, browser modern menampilkan",
                    "  pemutar mati — bukan teks cadanganmu. Jadi tautan unduh di dalamnya",
                    "  berguna, tapi jangan pernah menaruh informasi penting hanya di situ.",
                    "",
                    "ATRIBUT <video> DAN <audio>",
                    "",
                    "  controls      tampilkan tombol putar, garis waktu, dan pengatur suara",
                    "  autoplay      langsung diputar begitu halaman dibuka",
                    "  muted         tanpa suara",
                    "  loop          ulangi dari awal begitu habis",
                    "  playsinline   putar di tempat, jangan rebut seluruh layar di ponsel",
                    "  preload       seberapa banyak diunduh duluan: none, metadata, auto",
                    "  poster        gambar sampul sebelum ditekan putar   (video saja)",
                    "  width height  ukuran kotaknya dalam piksel          (video saja)",
                    "",
                    "  Lima yang pertama ATRIBUT BOOLEAN: yang menentukan ada atau tidak",
                    "  adanya atribut itu, bukan nilainya. loop=\"false\" tetap mengulang.",
                    "  Aturan yang sama persis sudah kamu lihat di materi Atribut.",
                    "",
                    "TANPA controls TIDAK ADA TOMBOL APA PUN",
                    "",
                    "  Ini keluhan nomor satu: \"videonya muncul tapi tidak bisa diputar\".",
                    "  Memang begitu. <video> tanpa controls adalah kotak diam tanpa tombol,",
                    "  karena browser menganggap kamu akan menyediakan tombolmu sendiri",
                    "  lewat JavaScript.",
                    "",
                    "autoplay HANYA JALAN KALAU ADA muted",
                    "",
                    "  Semua browser sekarang memblokir media yang mengeluarkan SUARA sendiri",
                    "  tanpa disuruh. Alasannya gampang dibayangkan: satu tab dibuka, lalu",
                    "  tiba-tiba ada orang berteriak dari speaker kantor.",
                    "",
                    "    <video autoplay>        diblokir, tidak jalan",
                    "    <video autoplay muted>  jalan",
                    "",
                    "  \"Diblokir\" itu bagian yang menyakitkan: tidak ada pesan error di",
                    "  halaman, tidak ada apa pun. Videonya cuma diam. Kalau kamu memang",
                    "  butuh autoplay, bentuk lengkapnya:",
                    "",
                    "    <video autoplay muted loop playsinline ...>",
                    "",
                    "  playsinline ikut karena tanpa itu iPhone merebut seluruh layar begitu",
                    "  video mulai berjalan.",
                    "",
                    "preload ADALAH PERMINTAAN, BUKAN PERINTAH",
                    "",
                    "    none      jangan unduh apa pun sampai ditekan. Hemat kuota.",
                    "    metadata  ambil secukupnya untuk tahu durasi dan ukuran. Aman.",
                    "    auto      browser boleh mengunduh seluruh berkas lebih dulu.",
                    "",
                    "  Browser boleh mengabaikannya, dan di ponsel ia memang sering",
                    "  mengabaikannya. preload juga tidak berarti apa-apa kalau ada autoplay.",
                    "",
                    "  poster: gambar yang tampil sebelum tombol putar ditekan. Tanpa poster,",
                    "  yang terlihat adalah frame pertama videonya — dan frame pertama hampir",
                    "  selalu hitam polos.",
                    "",
                    "  Tanpa width dan height, kotak <video> berukuran bawaan 300x150 piksel",
                    "  sampai ukuran aslinya diketahui, lalu melompat. Persoalan yang sama",
                    "  dengan <img>, dan obatnya juga sama.",
                    "",
                    "<track> — TAKARIR ITU BUKAN PELENGKAP",
                    "",
                    "  kind      captions   untuk yang tidak bisa MENDENGAR: dialog ditambah",
                    "                       suara penting (\"pintu berderit\", \"musik sedih\")",
                    "            subtitles  terjemahan, untuk yang mendengar tapi tidak paham",
                    "                       bahasanya",
                    "            chapters, descriptions, metadata — jarang dipakai pemula",
                    "  src       berkas .vtt yang berisi teksnya",
                    "  srclang   kode bahasa teks itu, misalnya id atau en",
                    "  label     tulisan yang muncul di menu takarir pemutarnya",
                    "  default   boolean: nyalakan takarir ini sejak awal",
                    "",
                    "  <track> juga ELEMEN KOSONG. Tidak ada </track>.",
                    "",
                    "  Isi berkas .vtt-nya sesederhana ini:",
                    "",
                    "    WEBVTT",
                    "",
                    "    00:00:00.000 --> 00:00:04.500",
                    "    Panaskan air sampai sekitar 92 derajat.",
                    "",
                    "    00:00:04.500 --> 00:00:09.000",
                    "    Tuang melingkar dari tengah ke tepi.",
                    "",
                    "  Kenapa ini bukan tambahan yang boleh ditunda:",
                    "    - Orang tuli tidak bisa memakai videomu sama sekali tanpa takarir.",
                    "    - Banyak orang menonton tanpa suara: di kereta, di kelas, di kantor.",
                    "    - Mesin pencari tidak bisa \"menonton\". Berkas .vtt itu satu-satunya",
                    "      teks yang bisa ia baca dari videomu.",
                    "",
                    "  Jebakan yang membuang waktu: takarir sering TIDAK MUNCUL saat berkas",
                    "  HTML-nya dibuka dengan klik dua kali (alamat file://). Browser menolak",
                    "  memuat .vtt dari sana. Jalankan lewat server lokal dan takarirnya",
                    "  kembali (materi Menjalankan Halaman Sendiri).",
                    "",
                    "<audio> bentuknya sama persis, minus poster dan minus width/height. Ia",
                    "digambar sebagai satu bilah pemutar; ukurannya urusan CSS.",
                ],
            },
            {
                "heading": "Kode sematan peta dan video di halaman utuh",
                "code": """<!doctype html>
<html lang="id">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Kelas Seduh Manual - Kopi Pagi</title>
</head>
<body>
  <h1>Kelas Seduh Manual</h1>

  <h2>Rekaman kelas minggu lalu</h2>
  <iframe width="560" height="315"
          src="https://www.youtube.com/embed/ID_VIDEO"
          title="Rekaman kelas seduh manual V60, 42 menit"
          allow="autoplay; encrypted-media; picture-in-picture"
          referrerpolicy="strict-origin-when-cross-origin"
          loading="lazy"
          allowfullscreen></iframe>

  <h2>Lokasi kelas</h2>
  <iframe src="https://peta.test/sematan?q=Jalan+Melati+7+Bandung"
          title="Peta lokasi Kopi Pagi di Jalan Melati 7, Bandung"
          width="600" height="450"
          loading="lazy"
          referrerpolicy="no-referrer"></iframe>

  <h2>Catatan peserta</h2>
  <iframe src="catatan-peserta.html"
          title="Catatan yang dikirim peserta kelas"
          sandbox
          width="600" height="300"></iframe>
</body>
</html>""",
            },
            {
                "body": [
                    "Dua iframe pertama di atas adalah kode sematan sungguhan: yang satu dari",
                    "tombol \"Bagikan > Sematkan\" di situs video, yang satu dari \"Bagikan peta",
                    "ini\". Aslinya ditempel sebagai satu baris yang sangat panjang, dan yang",
                    "dari peta biasanya datang tanpa title sama sekali. Di sini sudah dipecah",
                    "dan dirapikan. Sekarang bedah atributnya satu per satu.",
                    "",
                    "iframe = inline frame: jendela di tengah halamanmu yang isinya HALAMAN",
                    "LAIN SEPENUHNYA, lengkap dengan <html>, <head>, <body>, CSS, dan",
                    "JavaScript-nya sendiri.",
                    "",
                    "Yang paling sering disalahpahami: isinya bukan bagian dari halamanmu.",
                    "",
                    "  - CSS-mu TIDAK MASUK ke dalamnya. Mau kamu tulis aturan untuk isi",
                    "    frame itu seratus kali, tidak ada satu huruf pun yang berubah.",
                    "  - JavaScript-mu tidak boleh membacanya kalau alamatnya beda domain.",
                    "  - Yang boleh kamu atur cuma KOTAKNYA: lebar, tinggi, bingkai, posisi.",
                    "  - Mengklik tautan di dalamnya mengganti isi frame, bukan halamanmu,",
                    "    dan alamat di bilah browser tidak ikut berubah.",
                    "",
                    "Tanpa width dan height, kotaknya berukuran bawaan 300x150 piksel.",
                    "Angkanya tanpa satuan, sama seperti di <img>.",
                    "",
                    "title WAJIB, DAN INI BUKAN <title> YANG DI HEAD",
                    "",
                    "  Pembaca layar memperlakukan tiap iframe sebagai satu wilayah yang bisa",
                    "  dilompati, dan yang ia umumkan diambil dari atribut title. Tanpa itu,",
                    "  yang terdengar cuma \"bingkai\", lalu \"bingkai\", lalu \"bingkai\" — tidak",
                    "  ada satu pun yang bisa dipilih.",
                    "",
                    "    title=\"Peta lokasi Kopi Pagi di Jalan Melati 7\"   baik",
                    "    title=\"peta\"                                     nyaris tak berguna",
                    "    tanpa title                                      gagal",
                    "",
                    "  Kode sematan yang kamu salin dari situs orang SERING TIDAK",
                    "  MENYERTAKANNYA. Menambahkan title adalah hal pertama yang kamu",
                    "  kerjakan sesudah menempelkannya.",
                    "",
                    "ATRIBUT IFRAME YANG LAIN",
                    "",
                    "  loading=\"lazy\"   jangan muat frame ini sampai pembaca menggulir",
                    "                   mendekatinya. Akibatnya jauh lebih besar daripada",
                    "                   pada <img>: satu sematan video bisa berarti lebih",
                    "                   dari satu megabyte berkas dan puluhan permintaan",
                    "                   jaringan, untuk sesuatu yang mungkin tak pernah",
                    "                   dilihat orang.",
                    "",
                    "  allow=\"...\"      izin yang kamu berikan ke halaman di dalamnya,",
                    "                   dipisah titik koma: autoplay, fullscreen, camera,",
                    "                   microphone, geolocation, encrypted-media,",
                    "                   picture-in-picture. Yang tidak disebut, tidak",
                    "                   diizinkan.",
                    "",
                    "  allowfullscreen  boolean. Versi pendek dan lama dari",
                    "                   allow=\"fullscreen\", dan masih dipakai di hampir",
                    "                   semua kode sematan.",
                    "",
                    "  referrerpolicy   seberapa banyak situs di dalamnya boleh tahu ia",
                    "                   dipasang di halaman mana. no-referrer berarti tidak",
                    "                   diberi tahu sama sekali. Ini soal privasi PEMBACAMU,",
                    "                   bukan privasimu.",
                    "",
                    "  frameborder=\"0\"  peninggalan HTML lama. Tidak perlu lagi; hilangkan",
                    "                   bingkainya lewat CSS. Kalau kamu melihatnya di kode",
                    "                   sematan orang, itu bukan kesalahanmu.",
                    "",
                    "sandbox — MATIKAN SEMUA DULU, HIDUPKAN SATU-SATU",
                    "",
                    "  Menulis kata sandbox saja, tanpa nilai, adalah kuncian paling ketat.",
                    "  Yang langsung mati di dalam frame itu:",
                    "",
                    "    - seluruh JavaScript-nya",
                    "    - pengiriman formulir",
                    "    - pembukaan jendela atau tab baru",
                    "    - akses ke cookie dan penyimpanan situsnya sendiri",
                    "    - kemampuan memindahkan halaman INDUK ke alamat lain",
                    "",
                    "  Yang terakhir itu alasan utama sandbox ada. Tanpanya, halaman di dalam",
                    "  frame bisa melempar seluruh tab pembacamu ke situs lain.",
                    "",
                    "  Kalau ada yang benar-benar dibutuhkan, sebutkan izinnya, dipisah",
                    "  spasi:",
                    "",
                    "    sandbox=\"allow-forms allow-popups\"",
                    "    sandbox=\"allow-scripts\"",
                    "",
                    "  Nilai lain: allow-same-origin, allow-modals, allow-downloads,",
                    "  allow-top-navigation.",
                    "",
                    "  Jebakan: allow-scripts dan allow-same-origin SEKALIGUS, untuk berkas",
                    "  dari domainmu sendiri, membuat sandbox-nya sia-sia. Skrip di dalamnya",
                    "  bisa menghapus atribut sandbox itu sendiri lalu memuat ulang dirinya.",
                    "",
                    "DUA HAL YANG HARUS KAMU INGAT SEBELUM MENEMPEL SATU IFRAME PUN",
                    "",
                    "1. Kamu sedang mengundang KODE ORANG LAIN ke halamanmu.",
                    "",
                    "   Halaman di dalam frame boleh memasang cookie, mencatat siapa yang",
                    "   datang, dan mengganti isinya kapan saja tanpa memberitahumu.",
                    "   Halamanmu juga jadi selambat halaman itu. Sematkan dari sumber yang",
                    "   kamu percaya; untuk yang tidak, pakai sandbox dan referrerpolicy.",
                    "",
                    "2. <iframe> PUNYA TAG PENUTUP meski isinya selalu kosong.",
                    "",
                    "   Ini kebalikan persis dari <img>, dan gampang tertukar karena",
                    "   keduanya sama-sama \"menyisipkan sesuatu dari luar\".",
                    "",
                    "     <iframe src=\"peta.html\" title=\"Peta\"></iframe>    BENAR",
                    "     <iframe src=\"peta.html\" title=\"Peta\" />           SALAH",
                    "",
                    "   Garis miring di bentuk kedua tidak berarti apa-apa bagi browser.",
                    "   Frame-nya dianggap masih terbuka, dan SELURUH sisa halamanmu tertelan",
                    "   masuk ke dalamnya sebagai teks yang tidak ditampilkan — sampai",
                    "   bertemu </iframe> yang tidak pernah ada. Gejalanya: halaman mendadak",
                    "   kosong mulai dari iframe itu ke bawah.",
                    "",
                    "   Pohon struktur di aplikasi ini memakai pembaca HTML yang lebih",
                    "   pemaaf dan tidak menirukan bagian ini. Buktinya cuma terlihat kalau",
                    "   berkasnya dibuka di browser sungguhan.",
                    "",
                    "SATU GEJALA YANG AKAN MEMBINGUNGKANMU SUATU HARI",
                    "",
                    "  Frame kosong putih, padahal src-nya benar dan alamat yang sama bisa",
                    "  dibuka biasa di tab baru.",
                    "",
                    "  Banyak situs melarang dirinya disematkan di halaman orang lain, dan",
                    "  penolakan itu cuma tercatat di Console — tidak ada apa pun di layar.",
                    "  Kalau itu terjadi, situsnya memang tidak mengizinkan, dan tidak ada",
                    "  satu atribut pun yang bisa memaksanya. Yang tersisa: tautan biasa",
                    "  dengan <a>.",
                    "",
                    "DUA KERABAT TUA YANG MASIH SERING TERLIHAT",
                    "",
                    "  <embed> dan <object> adalah pendahulu <iframe>, dari zaman Flash dan",
                    "  applet Java. Keduanya masih sah, tapi jangan memakainya untuk hal baru.",
                    "  Kalau kamu menemukannya di kode lama, artinya sama: \"sisipkan sesuatu",
                    "  dari luar di sini\".",
                    "",
                    "  Berkas PDF pun sekarang cukup ditampilkan begini:",
                    "",
                    "    <iframe src=\"brosur.pdf\" title=\"Brosur kelas seduh\"",
                    "            width=\"600\" height=\"800\"></iframe>",
                    "",
                    "Ringkasnya, tiga wadah dan siapa pemilik isinya:",
                    "",
                    "  <video>   berkasmu sendiri, kamu yang menyediakan formatnya",
                    "  <audio>   sama, tanpa gambar",
                    "  <iframe>  halaman ORANG LAIN, di luar kendalimu sepenuhnya",
                ],
            },
        ],
    },
    {
        "title": "14. Tabel",
        "sections": [
            {
                "body": [
                    "Tabel untuk DATA yang punya baris dan kolom: harga, jadwal,",
                    "perbandingan spesifikasi, hasil pertandingan.",
                    "",
                    "Tabel BUKAN untuk tata letak halaman.",
                    "  Sekitar tahun 2000 orang menyusun seluruh halaman dengan",
                    "  tabel tak terlihat, karena CSS belum sanggup. Warisan itu",
                    "  masih beredar di internet. Jangan ditiru: pembaca layar akan",
                    "  mengumumkan \"tabel, 12 baris, 3 kolom\" untuk sesuatu yang",
                    "  sebenarnya cuma menu dan artikel.",
                    "",
                    "Tiga elemen inti:",
                    "  <tr>  table row  — satu baris",
                    "  <th>  table head — sel KEPALA (judul kolom atau judul baris)",
                    "  <td>  table data — sel isi",
                    "",
                    "Tabel dibaca per BARIS. Kamu menulis baris demi baris, dan",
                    "kolom terbentuk dengan sendirinya dari urutan sel. Tidak ada",
                    "elemen \"kolom\" yang berisi data.",
                ]
            },
            {
                "heading": "Tabel lengkap",
                "code": """<table>
  <caption>Harga menu, berlaku Januari 2024</caption>

  <thead>
    <tr>
      <th scope="col">Menu</th>
      <th scope="col">Gelas kecil</th>
      <th scope="col">Gelas besar</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <th scope="row">Kopi tubruk</th>
      <td>12.000</td>
      <td>15.000</td>
    </tr>
    <tr>
      <th scope="row">Kopi susu</th>
      <td>18.000</td>
      <td>22.000</td>
    </tr>
    <tr>
      <th scope="row">Cold brew</th>
      <td>20.000</td>
      <td>25.000</td>
    </tr>
  </tbody>

  <tfoot>
    <tr>
      <td colspan="3">Semua harga sudah termasuk pajak.</td>
    </tr>
  </tfoot>
</table>"""
            },
            {
                "body": [
                    "Bagian-bagian tabel:",
                    "",
                    "  <caption>  judul tabel. Kalau ada, harus jadi elemen PERTAMA",
                    "             di dalam <table>. Ini judul yang dibacakan pembaca",
                    "             layar sebelum isinya — jauh lebih berguna daripada",
                    "             <p> biasa di atas tabel, karena terikat ke tabelnya.",
                    "",
                    "  <thead>    baris kepala",
                    "  <tbody>    baris isi",
                    "  <tfoot>    baris ringkasan / catatan",
                    "",
                    "  Ketiganya opsional, tapi berguna: tabel panjang yang dicetak",
                    "  akan mengulang thead di tiap halaman kertas.",
                    "",
                    "scope pada <th> — kecil, tapi menentukan:",
                    "  scope=\"col\"  sel ini judul untuk KOLOM di bawahnya",
                    "  scope=\"row\"  sel ini judul untuk BARIS di sebelahnya",
                    "",
                    "  Kenapa perlu: pembaca layar membaca tabel sel demi sel. Saat",
                    "  sampai di sel \"22.000\", yang dibacakan adalah \"Kopi susu,",
                    "  Gelas besar, 22.000\". Tanpa scope, yang terdengar cuma",
                    "  \"22.000\" — angka tanpa keterangan, di tengah tiga puluh",
                    "  angka lain. Tabelnya jadi mustahil dipahami.",
                    "",
                    "Perhatikan bahwa kolom pertama tiap baris memakai <th>, bukan",
                    "<td>. \"Kopi tubruk\" memang judul barisnya, bukan datanya.",
                ]
            },
            {
                "heading": "Menggabungkan sel",
                "code": """<table>
  <caption>Jam buka</caption>
  <tr>
    <th scope="col">Hari</th>
    <th scope="col">Buka</th>
    <th scope="col">Tutup</th>
  </tr>
  <tr>
    <td rowspan="2">Senin - Jumat</td>
    <td>07.00</td>
    <td>21.00</td>
  </tr>
  <tr>
    <td>Sarapan sampai 10.00</td>
    <td>Dapur tutup 20.30</td>
  </tr>
  <tr>
    <td>Sabtu dan Minggu</td>
    <td colspan="2">Libur</td>
  </tr>
</table>"""
            },
            {
                "body": [
                    "  colspan=\"2\"  sel ini memakan 2 KOLOM ke kanan",
                    "  rowspan=\"2\"  sel ini memakan 2 BARIS ke bawah",
                    "",
                    "Aturan yang membuat tabel tidak berantakan:",
                    "  Setiap baris harus tetap berjumlah kolom yang sama SETELAH",
                    "  penggabungan dihitung.",
                    "",
                    "  Hitung contoh di atas, tabelnya 3 kolom:",
                    "    baris 1:  3 sel                        = 3",
                    "    baris 2:  1 sel rowspan + 2 sel        = 3",
                    "    baris 3:  2 sel + 1 titipan dari atas  = 3",
                    "    baris 4:  1 sel + 1 sel colspan 2      = 3",
                    "",
                    "Perhatikan baris 3: ia cuma punya DUA <td>, karena sel pertama",
                    "sudah diisi oleh rowspan dari baris sebelumnya. Menulis tiga",
                    "sel di situ akan mendorong satu sel keluar ke kolom keempat",
                    "yang tidak ada — dan tabelnya melebar sendiri tanpa error.",
                    "",
                    "Saran: gabungkan sel seperlunya saja. Tabel dengan penggabungan",
                    "bertingkat sulit dibaca mata dan sangat sulit didengarkan.",
                    "Kalau sebuah tabel butuh lebih dari satu-dua penggabungan,",
                    "biasanya itu dua tabel yang dipaksa jadi satu.",
                ]
            },
            {
                "heading": "colgroup dan col: memegang kolom, bukan mengisinya",
                "code": """<table>
  <caption>Harga menu</caption>

  <colgroup>
    <col>
    <col span="2" class="harga">
  </colgroup>

  <tr>
    <th scope="col">Menu</th>
    <th scope="col">Kecil</th>
    <th scope="col">Besar</th>
  </tr>
  <tr>
    <th scope="row">Kopi tubruk</th>
    <td>12.000</td>
    <td>15.000</td>
  </tr>
</table>"""
            },
            {
                "body": [
                    "Kalimat di awal materi ini — \"tidak ada elemen kolom yang berisi",
                    "data\" — tetap benar, dan tetap perlu satu tambahan. Elemen",
                    "<col> memang ada, dan kamu akan menemuinya persis di tempat",
                    "seperti contoh di atas: menempel di bawah <caption>.",
                    "",
                    "  <colgroup>  wadahnya. Ditulis sesudah <caption>, sebelum",
                    "              baris pertama.",
                    "  <col>       mewakili SATU kolom. Elemen kosong, tanpa",
                    "              penutup — ini pemilik nama \"col\" yang lewat di",
                    "              daftar elemen kosong dulu.",
                    "  span=\"2\"    satu <col> mewakili dua kolom berturut-turut,",
                    "              jadi tidak perlu ditulis dua kali.",
                    "",
                    "Yang penting diluruskan: <col> tidak MEMUAT apa-apa. Datanya",
                    "tetap ditulis baris demi baris seperti biasa. <col> cuma",
                    "tempat menggantungkan atribut dan gaya yang berlaku untuk satu",
                    "kolom penuh — pada contoh di atas, class=\"harga\" supaya dua",
                    "kolom angka bisa dirapatkan ke kanan lewat SATU aturan CSS,",
                    "tanpa menempeli setiap <td>.",
                    "",
                    "Jumlah kolom yang diwakili <colgroup> harus cocok dengan jumlah",
                    "kolom tabelnya. Hitung contoh di atas: 1 + 2 = 3, sama dengan",
                    "jumlah <th> di baris pertama.",
                    "",
                    "Kalau kamu belum belajar CSS, <colgroup> belum ada gunanya",
                    "untukmu. Kenali saja bentuknya, supaya kamu tidak mengira ada",
                    "yang aneh saat membaca tabel buatan orang lain.",
                ]
            },
            {
                "heading": "headers: untuk tabel yang kepalanya bertingkat",
                "code": """<table>
  <caption>Harga menu per ukuran gelas</caption>
  <tr>
    <td></td>
    <th id="harga" colspan="2">Harga</th>
  </tr>
  <tr>
    <td></td>
    <th id="kecil">Kecil</th>
    <th id="besar">Besar</th>
  </tr>
  <tr>
    <th id="tubruk">Kopi tubruk</th>
    <td headers="tubruk harga kecil">12.000</td>
    <td headers="tubruk harga besar">15.000</td>
  </tr>
</table>"""
            },
            {
                "body": [
                    "scope bekerja selama tiap sel punya tepat satu judul kolom dan",
                    "satu judul baris. Begitu kepalanya BERTINGKAT — \"Kecil\" dan",
                    "\"Besar\" berada di bawah judul gabungan \"Harga\" — scope kehabisan",
                    "cara menyebut sel mana milik judul yang mana.",
                    "",
                    "Jalan keluarnya: beri id pada setiap sel kepala, lalu sebutkan",
                    "semuanya di sel datanya lewat headers, dipisah spasi.",
                    "",
                    "  headers=\"tubruk harga besar\"",
                    "",
                    "Urutannya dari yang paling umum ke yang paling khusus, dan itu",
                    "juga urutan yang dibacakan. Di sel 15.000 yang terdengar jadi:",
                    "\"Kopi tubruk, Harga, Besar, 15.000\".",
                    "",
                    "Kapan memakai yang mana:",
                    "  scope    untuk tabel biasa, dan itu hampir semua tabel.",
                    "           Pendek, dan tidak ada id yang bisa salah ketik.",
                    "  headers  hanya kalau kepalanya bertingkat, atau ada sel yang",
                    "           punya lebih dari satu judul.",
                    "",
                    "id yang disebut headers harus benar-benar ada di halaman itu.",
                    "Salah satu huruf saja dan hubungannya putus tanpa pesan apa pun",
                    "— persis jenis kesalahan diam yang sudah berkali-kali kamu",
                    "temui di HTML.",
                    "",
                    "Saran yang sama seperti pada penggabungan sel: tabel yang sampai",
                    "butuh headers biasanya bisa dipecah jadi dua tabel yang lebih",
                    "gampang dibaca semua orang, termasuk kamu enam bulan lagi.",
                ]
            },
        ],
    },
    {
        "title": "15. Formulir: input, label, dan button",
        "sections": [
            {
                "body": [
                    "Formulir adalah satu-satunya cara HTML mengirim data dari",
                    "pengguna ke server.",
                    "",
                    "  <form action=\"/daftar\" method=\"post\">",
                    "",
                    "  action  ke mana data dikirim",
                    "  method  cara mengirimnya",
                    "",
                    "Dua method, dan bedanya bukan selera:",
                    "",
                    "  get   Data ditempel di alamat URL:",
                    "          /cari?kata=kopi&halaman=2",
                    "        Bisa di-bookmark dan dibagikan. Terlihat semua orang,",
                    "        tercatat di riwayat browser dan log server.",
                    "        Untuk PENCARIAN dan penyaringan.",
                    "",
                    "  post  Data dikirim di badan permintaan, tidak tampak di URL.",
                    "        Untuk data yang MENGUBAH sesuatu: pendaftaran, pesanan,",
                    "        kata sandi.",
                    "",
                    "  Aturan sederhana: kalau menekan tombolnya mengubah sesuatu",
                    "  di server, pakai post.",
                    "",
                    "Catatan: formulir tanpa server tidak akan menyimpan apa pun.",
                    "Kamu tetap bisa menulis dan mempelajarinya; yang belum ada",
                    "cuma pihak yang menerima datanya.",
                ]
            },
            {
                "body": [
                    "APA YANG SEBENARNYA ADA DI UJUNG action",
                    "",
                    "Di ujung action bukan halaman HTML, melainkan sebuah PROGRAM",
                    "yang berjalan di server. Program itu menerima data kirimanmu,",
                    "memeriksanya sekali lagi, menyimpannya, lalu menjawab dengan",
                    "halaman baru.",
                    "",
                    "Tulisannya bermacam-macam, dan semuanya berarti hal yang sama:",
                    "",
                    "  action=\"/pesan\"",
                    "    Sebuah RUTE. Di ujungnya ada program berbahasa Python,",
                    "    JavaScript di Node, Go, atau apa pun, yang sudah didaftarkan",
                    "    untuk menangani alamat itu.",
                    "",
                    "  action=\"kirim.php\"",
                    "    Sebuah BERKAS program berbahasa PHP. Bentuk ini yang paling",
                    "    sering muncul di tutorial lama, dan masih sangat hidup.",
                    "",
                    "  action=\"\"  atau atributnya tidak ditulis sama sekali",
                    "    Dikirim ke alamat halaman ini sendiri. Lazim pada halaman",
                    "    yang menampilkan formulir sekaligus memprosesnya.",
                    "",
                    "Jadi kalau sebuah latihan menyuruhmu menulis action=\"kirim.php\",",
                    "kamu TIDAK perlu membuat berkas kirim.php lebih dulu. Yang",
                    "sedang dilatih adalah menulis formulirnya; pihak di seberang",
                    "sana — seperti kata catatan di atas — memang belum ada, dan",
                    "HTML-mu tidak salah karenanya.",
                    "",
                    "Membuat program penerimanya pekerjaan bahasa lain dan materi",
                    "tersendiri. Dari sisi HTML yang harus kamu pastikan cuma dua:",
                    "alamatnya benar, dan setiap isian punya name.",
                ]
            },
            {
                "heading": "Formulir dasar",
                "code": """<form action="/pesan" method="post">
  <p>
    <label for="nama">Nama lengkap</label>
    <input type="text" id="nama" name="nama" required>
  </p>

  <p>
    <label for="surel">Surel</label>
    <input type="email" id="surel" name="surel"
           placeholder="nama@contoh.com">
  </p>

  <p>
    <label for="jumlah">Jumlah gelas</label>
    <input type="number" id="jumlah" name="jumlah"
           min="1" max="10" value="1">
  </p>

  <p>
    <label for="ambil">Jam pengambilan</label>
    <input type="time" id="ambil" name="ambil">
  </p>

  <button type="submit">Kirim pesanan</button>
</form>"""
            },
            {
                "body": [
                    "KENAPA <label> WAJIB, BUKAN SEKADAR DIANJURKAN",
                    "",
                    "  <label for=\"nama\">Nama lengkap</label>",
                    "  <input type=\"text\" id=\"nama\" name=\"nama\">",
                    "",
                    "  for pada label harus sama persis dengan id pada input.",
                    "  Itulah yang mengikat keduanya.",
                    "",
                    "  Yang kamu dapat dari ikatan itu:",
                    "",
                    "  1. Mengklik TULISANNYA memfokuskan kotak isiannya. Sasaran",
                    "     kliknya jadi jauh lebih besar. Di ponsel ini bukan",
                    "     kenyamanan, ini syarat supaya kotak centang bisa dikenai",
                    "     jari sama sekali.",
                    "",
                    "  2. Pembaca layar menyebut nama kolomnya saat kursor masuk.",
                    "     Tanpa label, yang terdengar cuma \"kotak isian, kosong\".",
                    "     Orang itu harus menebak apa yang harus diisi.",
                    "",
                    "  Bentuk kedua: membungkus input-nya, tanpa for dan id.",
                    "    <label>Nama lengkap <input type=\"text\" name=\"nama\"></label>",
                    "  Sah, tapi bentuk for/id lebih luwes buat CSS.",
                    "",
                    "  placeholder BUKAN pengganti label. Tulisan abu-abu itu HILANG",
                    "  begitu orang mulai mengetik — jadi persis saat mereka",
                    "  membutuhkannya untuk memeriksa ulang, keterangannya lenyap.",
                    "  Selain itu warnanya nyaris tidak terbaca. Pakai keduanya:",
                    "  label untuk namanya, placeholder untuk contoh isiannya.",
                ]
            },
            {
                "body": [
                    "ATRIBUT name — KESALAHAN NOMOR SATU DI FORMULIR",
                    "",
                    "  Input TANPA name tidak ikut terkirim. Sama sekali. Tanpa",
                    "  peringatan apa pun.",
                    "",
                    "  Server menerima data dalam bentuk pasangan nama=nilai:",
                    "    nama=Andi&surel=andi@contoh.test&jumlah=2",
                    "",
                    "  Nama itu diambil dari atribut name. Tidak ada name, tidak",
                    "  ada pasangan, dan datanya lenyap diam-diam.",
                    "",
                    "  id dan name berbeda tugas dan sering keduanya perlu ada:",
                    "    id    untuk label dan CSS, dipakai DI HALAMAN",
                    "    name  untuk pengiriman, dipakai DI SERVER",
                    "",
                    "Jenis input yang sering dipakai:",
                    "  text      teks satu baris",
                    "  email     memunculkan papan ketik ber-@ di ponsel",
                    "  password  ketikan disamarkan",
                    "  number    hanya angka, punya min dan max",
                    "  tel       papan ketik angka di ponsel",
                    "  url       alamat situs",
                    "  date      pemilih tanggal bawaan browser",
                    "  time      pemilih jam",
                    "  file      unggah berkas",
                    "  hidden    nilai yang ikut terkirim tapi tidak terlihat",
                    "",
                    "type yang salah tulis diperlakukan sebagai text. Itu berarti",
                    "type=\"emial\" tidak error — cuma diam-diam kehilangan semua",
                    "kelebihannya.",
                ]
            },
            {
                "heading": "Pilihan: radio dan kotak centang",
                "code": """<form action="/pesan" method="post">
  <fieldset>
    <legend>Ukuran gelas</legend>

    <input type="radio" id="kecil" name="ukuran" value="kecil" checked>
    <label for="kecil">Kecil (200 ml)</label>

    <input type="radio" id="besar" name="ukuran" value="besar">
    <label for="besar">Besar (350 ml)</label>
  </fieldset>

  <p>
    <input type="checkbox" id="wadah" name="bawa_wadah" value="ya">
    <label for="wadah">Saya membawa wadah sendiri (diskon 2.000)</label>
  </p>

  <button type="submit">Pesan</button>
  <button type="button">Batal</button>
</form>"""
            },
            {
                "body": [
                    "Radio (pilih SATU dari beberapa):",
                    "  - Yang mengelompokkan mereka adalah name YANG SAMA.",
                    "    Kalau name-nya berbeda, semuanya bisa dipilih bersamaan",
                    "    dan kelihatan seperti kotak centang bulat yang rusak.",
                    "  - value WAJIB diisi. Yang dikirim ke server adalah value,",
                    "    bukan tulisan di labelnya.",
                    "  - id tetap harus BERBEDA untuk tiap pilihan — name sama,",
                    "    id beda. Ini pasangan yang paling sering tertukar.",
                    "  - Radio tidak bisa dibatalkan setelah dipilih. Kalau \"tidak",
                    "    memilih\" harus mungkin, sediakan pilihan untuk itu.",
                    "",
                    "Checkbox (nyala/mati, masing-masing berdiri sendiri):",
                    "  - Kalau tidak dicentang, namanya TIDAK terkirim sama sekali.",
                    "    Server melihat ketiadaannya, bukan nilai \"tidak\".",
                    "",
                    "Tombol — perhatikan type-nya:",
                    "  <button type=\"submit\">  mengirim formulir",
                    "  <button type=\"button\">  tidak melakukan apa-apa sendiri",
                    "  <button type=\"reset\">   mengosongkan semua isian",
                    "",
                    "  Di dalam <form>, type BAWAANNYA adalah submit. Jadi tombol",
                    "  \"Batal\" yang ditulis <button>Batal</button> justru MENGIRIM",
                    "  formulirnya. Ini jebakan klasik: tombolnya terlihat benar,",
                    "  bekerja terbalik, dan tidak ada pesan error sama sekali.",
                    "",
                    "  type=\"reset\" jarang layak dipakai. Orang menekannya karena",
                    "  mengira itu \"batal\", lalu kehilangan seluruh isian.",
                ]
            },
        ],
    },
    {
        "title": "16. Formulir Lanjutan: select, textarea, dan Validasi",
        "sections": [
            {
                "body": [
                    "Dua elemen isian yang bukan <input>, dan keduanya punya",
                    "kejanggalan yang perlu diketahui lebih dulu:",
                    "",
                    "  <select>    daftar pilihan yang membuka ke bawah",
                    "  <textarea>  teks panjang beberapa baris",
                    "",
                    "Keduanya PUNYA tag penutup, tidak seperti <input> yang elemen",
                    "kosong. Alasannya masuk akal begitu dilihat:",
                    "",
                    "  <select> berisi elemen <option>, jadi ia butuh ruang di dalam.",
                    "",
                    "  <textarea> mengambil NILAI AWALNYA dari teks di antara kedua",
                    "  tagnya, bukan dari atribut value. Ini beda dari semua isian",
                    "  lain, dan sering bikin bingung:",
                    "",
                    "    <input type=\"text\" value=\"Tanpa gula\">",
                    "    <textarea>Tanpa gula</textarea>",
                    "",
                    "  Akibatnya: spasi dan baris baru di dalam textarea IKUT jadi",
                    "  isinya. Menulis tag pembukanya lalu menekan Enter berarti",
                    "  kotaknya dimulai dengan satu baris kosong.",
                ]
            },
            {
                "heading": "select, textarea, dan fieldset",
                "code": """<form action="/pesan" method="post">
  <fieldset>
    <legend>Detail pesanan</legend>

    <p>
      <label for="metode">Metode seduh</label>
      <select id="metode" name="metode">
        <option value="">-- pilih salah satu --</option>
        <optgroup label="Panas">
          <option value="tubruk">Tubruk</option>
          <option value="v60" selected>V60</option>
        </optgroup>
        <optgroup label="Dingin">
          <option value="coldbrew">Cold brew</option>
          <option value="eskopsus">Es kopi susu</option>
        </optgroup>
      </select>
    </p>

    <p>
      <label for="catatan">Catatan untuk barista</label>
      <textarea id="catatan" name="catatan" rows="4" cols="40"></textarea>
    </p>
  </fieldset>

  <button type="submit">Kirim</button>
</form>"""
            },
            {
                "body": [
                    "Tentang <select>:",
                    "  - Yang dikirim ke server adalah value dari option terpilih.",
                    "    Kalau value tidak ditulis, teks di dalam option yang dikirim.",
                    "    Tulis value-nya. Teks tampilan sering berubah; nilai data",
                    "    sebaiknya tidak.",
                    "  - selected menandai pilihan awal. Kalau tidak ada yang",
                    "    ditandai, option PERTAMA yang terpilih — dan orang sering",
                    "    mengirim formulir tanpa sadar menyentuh kolom itu. Itu",
                    "    sebabnya contoh di atas menaruh \"-- pilih salah satu --\"",
                    "    ber-value kosong di urutan pertama.",
                    "  - multiple membuatnya bisa memilih beberapa sekaligus.",
                    "  - <optgroup> mengelompokkan option. label-nya cuma judul,",
                    "    tidak bisa dipilih.",
                    "",
                    "Tentang <textarea>:",
                    "  rows  tinggi awal dalam baris",
                    "  cols  lebar awal dalam karakter",
                    "  Keduanya cuma ukuran AWAL; CSS mengalahkannya, dan pengguna",
                    "  biasanya masih bisa menariknya lebih besar.",
                    "",
                    "Tentang <fieldset> dan <legend>:",
                    "  Mengelompokkan isian yang berkaitan, dengan <legend> sebagai",
                    "  judul kelompoknya. <legend> harus jadi anak PERTAMA fieldset.",
                    "",
                    "  Ini wajib untuk radio: satu label per pilihan menjelaskan",
                    "  \"Kecil\" dan \"Besar\", tapi tidak ada yang menjelaskan bahwa",
                    "  pertanyaannya \"Ukuran gelas\". legend yang mengatakan itu,",
                    "  dan pembaca layar membacakannya di setiap pilihan.",
                ]
            },
            {
                "heading": "Validasi bawaan browser",
                "code": """<form action="/daftar" method="post">
  <p>
    <label for="anggota">Nomor anggota</label>
    <input type="text" id="anggota" name="anggota"
           pattern="[A-Z]{2}-[0-9]{4}"
           title="Dua huruf besar, tanda hubung, empat angka. Contoh: KP-0421"
           required>
  </p>

  <p>
    <label for="sandi">Kata sandi</label>
    <input type="password" id="sandi" name="sandi"
           minlength="8" maxlength="64" required>
  </p>

  <p>
    <label for="gelas">Jumlah gelas</label>
    <input type="number" id="gelas" name="gelas"
           min="1" max="10" step="1" value="1" required>
  </p>

  <p>
    <label for="tanggal">Tanggal ambil</label>
    <input type="date" id="tanggal" name="tanggal"
           min="2024-01-01" max="2024-12-31" required>
  </p>

  <button type="submit">Daftar</button>
</form>"""
            },
            {
                "body": [
                    "Atribut validasi yang tersedia tanpa satu baris JavaScript:",
                    "",
                    "  required            tidak boleh kosong",
                    "  minlength maxlength  panjang teks",
                    "  min max             batas angka atau tanggal",
                    "  step                kelipatan yang boleh",
                    "  pattern             harus cocok dengan pola (regex)",
                    "  type=\"email\"        harus berbentuk alamat surel",
                    "  type=\"url\"          harus berbentuk alamat situs",
                    "",
                    "Kalau isian tidak lolos, browser menolak mengirim dan",
                    "memunculkan gelembung pesan sendiri.",
                    "",
                    "pattern hampir selalu perlu ditemani title. Pesan bawaan",
                    "browser cuma berbunyi \"sesuaikan dengan format yang diminta\" —",
                    "isi title-lah yang memberi tahu formatnya seperti apa.",
                    "",
                    "novalidate pada <form> mematikan seluruh pemeriksaan ini.",
                    "Berguna saat menguji, tapi jangan ditinggal di halaman jadi.",
                ]
            },
            {
                "body": [
                    "MEMBACA POLA DI DALAM pattern",
                    "",
                    "  pattern=\"[A-Z]{2}-[0-9]{4}\"",
                    "",
                    "Isi pattern ditulis dalam REGEX (regular expression), sebuah",
                    "bahasa kecil tersendiri untuk menggambarkan BENTUK teks. Ia",
                    "bukan bagian dari HTML, dan kamu akan bertemu dia lagi di",
                    "JavaScript, di kotak cari-ganti editormu, dan di hampir semua",
                    "bahasa pemrograman. Kalau tadi rasanya seperti tiba-tiba ada",
                    "bahasa asing menyelinap masuk, itu memang benar.",
                    "",
                    "Kamu belum perlu menguasainya. Yang perlu sekarang cuma sanggup",
                    "MEMBACA pola pendek. Enam potong ini sudah membawamu jauh:",
                    "",
                    "  [ABC]    satu karakter, boleh yang mana saja dari isi kurung",
                    "  [A-Z]    satu karakter dalam RENTANG A sampai Z (huruf besar)",
                    "  [0-9]    satu angka. Singkatannya \\d",
                    "  {2}      yang persis di sebelah kirinya diulang 2 kali",
                    "  {2,4}    diulang 2 sampai 4 kali",
                    "  .        satu karakter apa saja",
                    "",
                    "Tiga penanda jumlah lain yang tidak memakai kurung kurawal:",
                    "",
                    "  +        satu kali atau lebih",
                    "  *        boleh nol kali, boleh berkali-kali",
                    "  ?        boleh ada boleh tidak (nol atau satu kali)",
                    "",
                    "Karakter yang tidak punya arti khusus mewakili dirinya sendiri.",
                    "Tanda hubung di luar kurung siku, misalnya, ya tanda hubung.",
                    "",
                    "Sekarang polanya bisa dieja dari kiri ke kanan:",
                    "",
                    "  [A-Z]{2}   dua huruf besar",
                    "  -          satu tanda hubung",
                    "  [0-9]{4}   empat angka",
                    "",
                    "  KP-0421   cocok",
                    "  kp-0421   ditolak, hurufnya kecil",
                    "  KP-421    ditolak, angkanya cuma tiga",
                    "",
                    "SATU ATURAN YANG PALING SERING BIKIN HERAN:",
                    "pattern dicocokkan ke SELURUH nilai, dari huruf pertama sampai",
                    "huruf terakhir. pattern=\"[0-9]{4}\" bukan berarti \"ada empat",
                    "angka di dalamnya\", melainkan \"isinya persis empat angka dan",
                    "tidak ada yang lain\". KP-0421 karena itu ditolak, bukan",
                    "diterima seperti dugaan banyak orang.",
                    "",
                    "Dua potong terakhir yang berguna: tanda kurung biasa ( )",
                    "mengelompokkan, dan | berarti \"atau\". pattern=\"(KP|KS)-[0-9]{4}\"",
                    "menerima KP-0421 maupun KS-0421.",
                    "",
                    "Kalau pola yang kamu perlukan terasa lebih rumit dari contoh di",
                    "atas, berhenti sebentar dan tanyakan apakah type=\"email\" atau",
                    "minlength sebenarnya sudah cukup. Pola panjang yang meleset",
                    "sedikit akan menolak orang yang datanya benar — dan mereka",
                    "tidak punya cara memberitahumu.",
                ]
            },
            {
                "body": [
                    "VALIDASI HTML ADALAH KENYAMANAN, BUKAN KEAMANAN",
                    "",
                    "Ini bagian terpenting dari materi ini.",
                    "",
                    "Semua pemeriksaan tadi berjalan DI KOMPUTER PENGGUNA, dan",
                    "apa pun yang berjalan di sana bisa dimatikan pemiliknya:",
                    "",
                    "  - Buka devtools, hapus atribut required, kirim.",
                    "  - Tambahkan novalidate pada form-nya.",
                    "  - Kirim permintaan langsung ke server tanpa membuka halamanmu",
                    "    sama sekali. Ini yang dilakukan orang yang berniat jahat,",
                    "    dan tidak sulit.",
                    "",
                    "Jadi:",
                    "  Validasi HTML gunanya memberi tahu orang yang JUJUR bahwa",
                    "  ada yang salah, sebelum mereka menunggu halaman dimuat ulang.",
                    "  Itu saja — dan itu sudah sangat berharga.",
                    "",
                    "  Server WAJIB memeriksa ulang SEMUANYA. Tanpa kecuali.",
                    "  Aturan yang tidak boleh dilupakan: jangan pernah percaya",
                    "  data yang datang dari luar, sekalipun formulirmu sendiri",
                    "  yang mengirimnya.",
                    "",
                    "Catatan kecil yang sering ditanyakan: bahasa pesan validasi",
                    "mengikuti bahasa BROWSER pengguna, bukan lang halamanmu, dan",
                    "kamu tidak bisa mengubah tulisannya lewat HTML.",
                ]
            },
        ],
    },
    {
        "title": "17. Formulir di Kode Nyata: Jenis Input Lain, Unggah Berkas, dan autocomplete",
        "sections": [
            {
                "body": [
                    "Dua materi sebelumnya mengajarkan tombol dalam satu bentuk saja:",
                    "",
                    "  <button type=\"submit\">Kirim</button>",
                    "",
                    "Di kode nyata — dan di hampir semua tutorial lama — bentuk yang",
                    "ini jauh lebih sering muncul:",
                    "",
                    "  <input type=\"submit\" value=\"Kirim\">",
                    "",
                    "Keduanya tombol kirim. Yang berbeda cuma DARI MANA tulisannya",
                    "datang.",
                    "",
                    "<input> adalah elemen kosong: tidak punya tag penutup, jadi",
                    "tidak ada ruang di dalamnya untuk menaruh teks. Satu-satunya",
                    "tempat yang tersisa adalah atribut, dan atribut itu bernama",
                    "value.",
                    "",
                    "  <button type=\"submit\">Kirim</button>",
                    "                        ^^^^^  tulisannya DI ANTARA dua tag",
                    "",
                    "  <input type=\"submit\" value=\"Kirim\">",
                    "                              ^^^^^  tulisannya DI ATRIBUT",
                    "",
                    "Bedanya paling terasa saat MEMBACA kode orang lain. Mencari",
                    "tulisan sebuah tombol di antara dua tag, di halaman yang memakai",
                    "bentuk input, adalah pencarian yang tidak akan pernah ketemu.",
                    "",
                    "Empat type <input> yang berperilaku sebagai tombol:",
                    "",
                    "  type=\"submit\"   mengirim formulir",
                    "  type=\"reset\"    mengosongkan semua isian",
                    "  type=\"button\"   tidak berbuat apa-apa sendiri; menunggu JS",
                    "  type=\"image\"    sebuah GAMBAR yang bekerja sebagai tombol kirim",
                    "",
                    "Tiga yang pertama menaruh tulisannya di value. type=\"image\"",
                    "memakai src dan alt, persis seperti <img>.",
                    "",
                    "value pada tombol jangan pernah dikosongkan. Kalau kosong,",
                    "browser mengisi tulisannya sendiri, dan tulisan itu mengikuti",
                    "bahasa BROWSER — bukan lang halamanmu. Satu pengunjung membaca",
                    "\"Submit\", yang lain \"Kirim\", di tombol yang sama persis.",
                    "",
                    "type=\"image\" punya kejutan sendiri: selain mengirim formulir, ia",
                    "ikut mengirim KOORDINAT titik yang diklik.",
                    "",
                    "  <input type=\"image\" name=\"denah\" src=\"denah.png\" alt=\"Meja\">",
                    "  yang sampai ke server:  denah.x=48&denah.y=112",
                    "",
                    "Dulu itu dipakai untuk gambar yang bisa diklik di banyak titik.",
                    "Kalau kamu menemukannya di kode lama, itulah yang terjadi.",
                    "",
                    "KENAPA <button> TETAP LEBIH BAIK UNTUK KODE YANG KAMU TULIS",
                    "",
                    "  Isi <button> adalah MARKUP; isi value cuma teks polos.",
                    "",
                    "    <button type=\"submit\">",
                    "      <img src=\"ikon/kirim.svg\" alt=\"\"> Kirim <b>sekarang</b>",
                    "    </button>",
                    "",
                    "  Tag yang ditulis di dalam value muncul apa adanya sebagai",
                    "  tulisan, bukan sebagai elemen. Tombol berikon mana pun yang",
                    "  kamu lihat hari ini hampir pasti <button>.",
                    "",
                    "  Kelebihan kedua: <button> punya value SENDIRI, terpisah dari",
                    "  tulisannya, jadi yang dikirim tidak harus sama dengan yang",
                    "  dibaca orang.",
                    "",
                    "    <button type=\"submit\" name=\"aksi\" value=\"hapus\">Buang draf</button>",
                    "    yang terkirim:  aksi=hapus",
                    "",
                    "  Di <input type=\"submit\"> dua peran itu bertabrakan di satu",
                    "  atribut: mengganti teks tombolnya berarti mengganti data yang",
                    "  terkirim.",
                    "",
                    "SATU FORMULIR, DUA TUJUAN",
                    "",
                    "  Tombol kirim boleh MENIMPA pengaturan formulir yang menaunginya:",
                    "",
                    "    formaction=\"/draf\"   kirim ke alamat lain",
                    "    formmethod=\"get\"     pakai method lain",
                    "    formnovalidate       lewati validasi bawaan",
                    "    formenctype          pakai pembungkus lain",
                    "    formtarget           buka jawabannya di tempat lain",
                    "",
                    "  Semuanya berawalan \"form\" dan berlaku HANYA untuk tombol yang",
                    "  ditempeli, bukan untuk formulirnya. Itulah cara \"Kirim lamaran\"",
                    "  dan \"Simpan draf\" bisa hidup di dalam SATU <form>.",
                    "",
                    "  formnovalidate ada di tombol draf karena draf memang belum",
                    "  lengkap — tanpa itu, required di kolom lain menghadang orang",
                    "  menyimpan pekerjaan yang belum selesai.",
                ],
            },
            {
                "heading": "Formulir unggah berkas",
                "code": """<form action="/lamaran" method="post" enctype="multipart/form-data">
  <fieldset>
    <legend>Berkas lamaran</legend>

    <p>
      <label for="kode">Nomor anggota</label>
      <input type="text" id="kode" name="kode" value="KP-0421" readonly>
    </p>

    <p>
      <label for="cv">Berkas CV</label>
      <input type="file" id="cv" name="cv" accept=".pdf" required>
    </p>

    <p>
      <label for="foto">Foto karya</label>
      <input type="file" id="foto" name="foto" accept="image/*" multiple>
    </p>
  </fieldset>

  <input type="submit" value="Kirim lamaran">
  <button type="submit" formaction="/draf" formnovalidate>
    Simpan draf
  </button>
</form>""",
            },
            {
                "body": [
                    "enctype — SATU ATRIBUT YANG KALAU LUPA, TIDAK ADA YANG BILANG",
                    "",
                    "Materi Formulir yang pertama menyebut dua atribut <form>: action",
                    "dan method. Untuk formulir biasa memang cukup. Begitu ada satu",
                    "saja <input type=\"file\">, ada atribut KETIGA yang wajib, dan",
                    "inilah bagian terpenting di materi ini:",
                    "",
                    "  <form action=\"/lamaran\" method=\"post\"",
                    "        enctype=\"multipart/form-data\">",
                    "",
                    "enctype menentukan bagaimana data DIBUNGKUS sebelum dikirim.",
                    "",
                    "  application/x-www-form-urlencoded",
                    "      Bawaannya. Semua isian dirangkai jadi satu baris teks:",
                    "      kode=KP-0421&cv=lamaran.pdf",
                    "  multipart/form-data",
                    "      Tiap isian dikirim sebagai bagian terpisah, dan bagian",
                    "      itu boleh berisi byte berkas.",
                    "",
                    "Bentuk nama=nilai tidak sanggup membawa isi berkas; di dalamnya",
                    "tidak ada tempat untuk data mentah. Jadi kalau enctype lupa",
                    "ditulis:",
                    "",
                    "  - Formulirnya TETAP terkirim.",
                    "  - Browser TIDAK protes. Tidak ada gelembung merah, tidak ada",
                    "    satu baris pun di konsol.",
                    "  - Yang sampai ke server cuma NAMA berkasnya:",
                    "    cv=lamaran-andi.pdf",
                    "  - Isinya tidak ikut. Sama sekali.",
                    "",
                    "Kegagalan yang tidak berbunyi seperti ini yang paling mahal:",
                    "kodenya terlihat benar, tombolnya bekerja, halaman berikutnya",
                    "terbuka, dan yang rusak baru ketahuan berhari-hari kemudian —",
                    "waktu seseorang mencoba membuka berkas yang ternyata tidak",
                    "pernah sampai. Kalau di formulirmu ada satu saja input file,",
                    "periksa enctype sebelum memeriksa apa pun yang lain.",
                    "",
                    "Jebakan lanjutannya: enctype hanya berlaku untuk method=\"post\".",
                    "Formulir unggah ber-method=\"get\" tidak mungkin berhasil, apa pun",
                    "enctype-nya, karena get selalu menempelkan datanya ke URL.",
                    "",
                    "Dua atribut di input file itu sendiri:",
                    "",
                    "  accept",
                    "      Saringan di kotak dialog pemilih berkas.",
                    "        accept=\"image/*\"               semua gambar",
                    "        accept=\".pdf,application/pdf\"  daftar dipisah koma",
                    "      Ini KENYAMANAN, bukan penjagaan: dialognya bisa disetel",
                    "      \"semua berkas\". Aturan dari materi Formulir Lanjutan tetap",
                    "      berlaku: server wajib memeriksa sendiri apa yang datang.",
                    "  multiple",
                    "      Boleh memilih beberapa berkas sekaligus. Tanpa ini, satu.",
                    "",
                    "Pohon struktur dari formulir unggah di atas:",
                    "",
                    "  form action=\"/lamaran\" enctype=\"multipart/form-data\" method=\"post\"",
                    "    fieldset",
                    "      legend \"Berkas lamaran\"",
                    "      p",
                    "        label for=\"kode\" \"Nomor anggota\"",
                    "        input id=\"kode\" name=\"kode\" readonly type=\"text\" value=\"KP-0421\"",
                    "      p",
                    "        label for=\"cv\" \"Berkas CV\"",
                    "        input accept=\".pdf\" id=\"cv\" name=\"cv\" required type=\"file\"",
                    "      p",
                    "        label for=\"foto\" \"Foto karya\"",
                    "        input accept=\"image/*\" id=\"foto\" multiple name=\"foto\" type=\"file\"",
                    "    input type=\"submit\" value=\"Kirim lamaran\"",
                    "    button formaction=\"/draf\" formnovalidate type=\"submit\" \"Simpan draf\"",
                    "",
                    "readonly, required, multiple, dan formnovalidate tercetak tanpa",
                    "nilai — mereka atribut boolean (materi Atribut). Atributnya juga",
                    "urut alfabetis, bukan urut yang kamu ketik.",
                    "",
                    "READONLY VS DISABLED — MIRIP DI LAYAR, BEDA DI DATA",
                    "",
                    "Kolom \"Nomor anggota\" tadi ber-readonly: isinya terlihat, tapi",
                    "tidak bisa diubah. disabled sekilas melakukan hal yang sama.",
                    "Bedanya justru ada di tempat yang tidak kelihatan:",
                    "",
                    "                          readonly     disabled",
                    "  Bisa diubah pengguna?   tidak        tidak",
                    "  IKUT TERKIRIM?          ya           TIDAK",
                    "  Bisa difokus & disalin? ya           tidak sama sekali",
                    "  Ikut divalidasi?        ya           tidak",
                    "  Tampilan bawaannya      normal       abu-abu redup",
                    "",
                    "Baris kedua yang menentukan. Kolom yang kamu kunci dengan",
                    "disabled HILANG dari data yang sampai ke server — sekali lagi,",
                    "tanpa satu pun error. Kalau nilainya masih dibutuhkan di sana,",
                    "pakai readonly, atau tetap disabled tapi kirim salinannya lewat",
                    "<input type=\"hidden\">.",
                    "",
                    "Dua catatan kecil yang menghemat waktu:",
                    "  - <fieldset disabled> mematikan SEMUA isian di dalamnya",
                    "    sekaligus. readonly tidak punya trik itu.",
                    "  - readonly cuma berlaku di isian berbentuk teks. Pada checkbox,",
                    "    radio, range, color, dan file ia tidak berpengaruh apa-apa;",
                    "    di sana disabled satu-satunya cara mengunci.",
                ],
            },
            {
                "heading": "Isian yang belum pernah kamu tulis",
                "code": """<form action="/preferensi" method="post">
  <p>
    <label for="cari">Cari menu</label>
    <input type="search" id="cari" name="q" list="menu-populer"
           placeholder="tubruk, v60, ...">
    <datalist id="menu-populer">
      <option value="Kopi tubruk">
      <option value="V60">
      <option value="Es kopi susu">
    </datalist>
  </p>

  <p>
    <label for="manis">Tingkat kemanisan (0-4)</label>
    <input type="range" id="manis" name="manis"
           min="0" max="4" step="1" value="2">
  </p>

  <p>
    <label for="warna">Warna label cangkir</label>
    <input type="color" id="warna" name="warna" value="#6f4e37">
  </p>

  <p>
    <label for="jemput">Waktu jemput</label>
    <input type="datetime-local" id="jemput" name="jemput"
           min="2024-01-01T08:00" max="2024-12-31T20:00">
  </p>

  <p>
    <label for="depan">Nama depan</label>
    <input type="text" id="depan" name="depan" autocomplete="given-name">
  </p>

  <p>
    <label for="alamat">Alamat pengiriman</label>
    <input type="text" id="alamat" name="alamat"
           autocomplete="street-address">
  </p>

  <p>
    <label for="otp">Kode dari SMS</label>
    <input type="text" id="otp" name="otp" inputmode="numeric"
           autocomplete="one-time-code" maxlength="6">
  </p>

  <p>
    <label for="sandi">Kata sandi baru</label>
    <input type="password" id="sandi" name="sandi"
           autocomplete="new-password" minlength="8" required>
  </p>

  <input type="submit" value="Simpan preferensi">
</form>""",
            },
            {
                "body": [
                    "JENIS INPUT YANG BELUM PERNAH DISEBUT",
                    "",
                    "  search",
                    "      Teks biasa, tapi bermakna \"ini kotak pencarian\". Sebagian",
                    "      browser menambahkan tombol silang pembersih di ujungnya.",
                    "  range",
                    "      Penggeser; min, max, dan step menentukan langkahnya.",
                    "      Angkanya TIDAK terlihat sama sekali, dan ia SELALU punya",
                    "      nilai — bawaannya tepat di tengah min dan max. Jadi",
                    "      \"belum menjawab\" mustahil ada di sini.",
                    "  color",
                    "      Pemilih warna. Nilainya selalu hex enam digit seperti",
                    "      #6f4e37, selalu terisi, dan tidak mengenal transparan.",
                    "  datetime-local",
                    "      Tanggal + jam TANPA zona waktu:  2024-03-01T08:30",
                    "  month",
                    "      Satu bulan:  2024-03",
                    "  week",
                    "      Satu pekan:  2024-W09",
                    "",
                    "Ingat aturan dari materi Formulir yang pertama: type yang tidak",
                    "dikenal browser diam-diam jadi text. month dan week yang",
                    "dukungannya paling timpang, jadi sebagian pengunjung akan",
                    "mengetiknya sebagai teks bebas — dan servermu harus siap",
                    "menerima ketikan apa pun, bukan cuma bentuk rapi di atas.",
                    "",
                    "inputmode — MEMILIH PAPAN KETIK PONSEL, TANPA MENGUBAH DATANYA",
                    "",
                    "  inputmode=\"numeric\" menyuruh ponsel memunculkan papan angka,",
                    "  sementara isiannya tetap teks biasa. Nilai lain: decimal, tel,",
                    "  email, url, search, text, none.",
                    "",
                    "  Kenapa tidak type=\"number\" saja? Karena number membuang nol di",
                    "  depan (\"007\" jadi \"7\"), punya panah naik-turun, dan angkanya",
                    "  bisa berubah cuma karena orang menggulir halaman saat kursor",
                    "  kebetulan berhenti di atasnya. Untuk kode OTP, nomor telepon,",
                    "  dan kode pos — yang berupa DERETAN ANGKA, bukan bilangan yang",
                    "  dihitung — pakai type=\"text\" ditemani inputmode.",
                    "",
                    "<datalist> — SARAN KETIK TANPA SATU BARIS JAVASCRIPT",
                    "",
                    "  <input list=\"menu-populer\" ...>",
                    "  <datalist id=\"menu-populer\">",
                    "    <option value=\"V60\">",
                    "  </datalist>",
                    "",
                    "  <option> di dalam datalist tidak punya teks isi — cuma value,",
                    "  dan tag penutupnya boleh dihilangkan.",
                    "",
                    "  Pengikatnya: atribut list pada input menunjuk id pada",
                    "  datalist. Bentuknya mirip sekali dengan for->id milik <label>,",
                    "  tapi BUKAN yang sama — namanya list, bukan for. Salah menulis",
                    "  salah satunya tidak menghasilkan error apa pun; sarannya cuma",
                    "  tidak pernah muncul, dan tidak ada yang memberi tahu kenapa.",
                    "",
                    "  Bedanya dengan <select>: datalist hanya MENYARANKAN. Pengguna",
                    "  tetap bebas mengetik apa saja, termasuk yang tidak ada di",
                    "  daftar. Kalau jawabannya wajib salah satu dari daftar, yang",
                    "  kamu perlukan tetap <select>. Elemen <datalist> sendiri tidak",
                    "  tampil di halaman.",
                    "",
                    "autocomplete — MEMBERI TAHU BROWSER KOLOM INI ISINYA APA",
                    "",
                    "  Nilainya bukan cuma on dan off. Ada daftar nama baku, dan nama",
                    "  itulah yang membuat isi-otomatis serta pengelola sandi bekerja",
                    "  dengan benar:",
                    "",
                    "    given-name  family-name  email  tel  username",
                    "    street-address  postal-code  country-name",
                    "",
                    "    current-password",
                    "        kolom sandi untuk MASUK ke akun yang sudah ada",
                    "    new-password",
                    "        kolom sandi BARU. Ini yang memicu tawaran \"buatkan",
                    "        sandi kuat\", dan yang mencegah sandi lama diisikan",
                    "        ke kolom ganti sandi",
                    "    one-time-code",
                    "        kode sekali pakai; ponsel menawarkan angka dari SMS",
                    "        yang baru masuk, tanpa perlu disalin tangan",
                    "",
                    "  Menandai kolom sandi baru sebagai current-password membuat",
                    "  pengelola sandi menimpanya dengan sandi lama. Orangnya tidak",
                    "  sadar, mengira sudah berganti sandi, lalu terkunci dari",
                    "  akunnya sendiri.",
                    "",
                    "  Kalau autocomplete tidak ditulis, browser MENEBAK isi kolom",
                    "  dari name, id, dan tulisan label-nya. Menulis autocomplete",
                    "  berarti berhenti membiarkannya menebak.",
                    "",
                    "  Soal autocomplete=\"off\": browser sering MENGABAIKANNYA,",
                    "  terutama di kolom sandi dan alamat. Itu disengaja — halaman",
                    "  yang melarang pengelola sandi membuat orang memilih sandi yang",
                    "  gampang diingat, dan sandi yang gampang diingat gampang",
                    "  ditebak. Jangan membangun apa pun di atas anggapan bahwa off",
                    "  pasti dipatuhi.",
                    "",
                    "ATRIBUT <form> LAIN YANG AKAN KAMU TEMUI",
                    "",
                    "  action dihilangkan",
                    "      Dikirim ke ALAMAT HALAMAN ITU SENDIRI. Bukan kesalahan;",
                    "      banyak halaman memang sengaja begitu, dan action=\"\"",
                    "      berarti persis hal yang sama.",
                    "  target=\"_blank\"",
                    "      Jawaban dari server dibuka di tab baru, persis seperti",
                    "      pada <a> di materi Tautan dan Gambar.",
                    "  name=\"lamaran\"",
                    "      Nama untuk FORMULIRNYA, dipakai JavaScript untuk",
                    "      menemukannya. Tidak ikut terkirim ke mana pun — tugasnya",
                    "      berbeda dari name pada input, yang justru satu-satunya",
                    "      alasan sebuah isian sampai ke server.",
                ],
            },
        ],
    },
    {
        "title": "18. Elemen Interaktif Bawaan: details, dialog, dan progress",
        "sections": [
            {
                "body": [
                    "Sampai sini hampir semua elemen yang kamu tulis diam saja. Browser",
                    "menggambarnya, lalu selesai. Yang bergerak — menu yang membuka, kotak",
                    "konfirmasi yang muncul, bilah yang merangkak penuh — biasanya digerakkan",
                    "JavaScript.",
                    "",
                    "Ada segelintir elemen yang tidak begitu. Mereka sudah membawa PERILAKUNYA",
                    "sendiri, langsung dari browser, tanpa satu baris JavaScript pun.",
                    "",
                    "Dua alasan kenapa ini perlu kamu kenali sekarang:",
                    "  - Kamu akan menemuinya terus di kode orang lain, dan kalau belum pernah",
                    "    melihatnya, satu tag asing di tengah berkas bisa menghentikanmu.",
                    "  - Banyak orang menulis lima puluh baris JavaScript untuk sesuatu yang",
                    "    sebenarnya sudah tersedia di HTML, dan versi buatan sendiri itu",
                    "    hampir selalu lebih rapuh.",
                    "",
                    "<details> DAN <summary>: BAGIAN YANG BISA DILIPAT",
                    "",
                    "  <details>",
                    "    <summary>Jam buka</summary>",
                    "    <p>Senin sampai Jumat, 07.00 - 21.00.</p>",
                    "  </details>",
                    "",
                    "Yang tampil mula-mula cuma tulisan \"Jam buka\" dengan segitiga kecil di",
                    "depannya. Diklik, isinya turun. Diklik lagi, terlipat kembali. Bisa juga",
                    "dibuka dengan keyboard: Tab sampai ke situ, lalu Enter atau spasi.",
                    "Semua itu bawaan browser. Tidak ada yang perlu kamu tulis.",
                    "",
                    "Tiga aturan yang menentukan ia bekerja atau tidak:",
                    "",
                    "  1. <summary> WAJIB jadi anak PERTAMA di dalam <details>.",
                    "     Kalau tidak ada sama sekali, browser menyisipkan tulisan bawaannya",
                    "     sendiri — dan tulisan itu berbahasa Inggris (\"Details\"), nongol di",
                    "     tengah halaman berbahasa Indonesiamu.",
                    "     Kalau <summary> ditaruh di tengah, ia bukan judul lipatan lagi:",
                    "     ia ikut tersembunyi bersama isi yang lain, dan yang bisa diklik",
                    "     jadi tulisan bawaan tadi.",
                    "",
                    "  2. Satu <details> hanya boleh punya SATU <summary>.",
                    "",
                    "  3. Sisa isinya bebas: paragraf, daftar, tabel, gambar, formulir,",
                    "     bahkan <details> lain di dalamnya.",
                    "",
                    "ATRIBUT open — INILAH PEMILIKNYA",
                    "",
                    "Di materi Atribut kamu menghafal daftar atribut boolean, dan 'open' ada",
                    "di daftar itu. <details> adalah elemen tempat ia dipasang.",
                    "",
                    "  <details open>   isinya sudah terbuka begitu halaman dimuat",
                    "  <details>        terlipat",
                    "",
                    "  Sifat boolean tetap berlaku persis seperti dulu:",
                    "  <details open=\"false\"> TETAP TERBUKA. Satu-satunya cara menutupnya",
                    "  adalah MENGHAPUS atributnya.",
                    "",
                    "  Yang mengejutkan banyak orang: atribut open BERUBAH SENDIRI setiap",
                    "  kali lipatannya diklik. Berkas HTML-mu tidak tersentuh — yang berubah",
                    "  elemen di memori browser. Akibatnya nyata: aturan CSS details[open]",
                    "  menyala dan padam mengikuti klik, dan JavaScript yang membaca",
                    "  elemennya melihat keadaan TERAKHIR, bukan yang kamu ketik.",
                    "",
                    "ATRIBUT name: BEBERAPA LIPATAN YANG SALING MENUTUP",
                    "",
                    "  <details name=\"faq\"> ... </details>",
                    "  <details name=\"faq\"> ... </details>",
                    "",
                    "  Beri name yang SAMA pada beberapa details, dan membuka salah satunya",
                    "  otomatis menutup yang lain. Itu akordeon, tanpa JavaScript.",
                    "  Polanya sengaja dibuat mirip radio button di materi Formulir: name",
                    "  yang sama berarti \"cuma satu yang boleh aktif\".",
                    "",
                    "  Fitur name ini baru muncul belakangan: Chrome akhir 2023, Firefox 2024.",
                    "  Di browser yang lebih tua, name diabaikan dan semua lipatan bisa terbuka",
                    "  bersamaan. Tidak ada yang rusak — cuma tidak saling menutup. Jadi pakai",
                    "  untuk kerapian, jangan untuk hal yang halamanmu bergantung padanya.",
                    "",
                    "DI MANA IA BENAR-BENAR DIPAKAI",
                    "",
                    "  - Halaman FAQ: pertanyaannya terlihat, jawabannya dilipat.",
                    "  - README di GitHub: \"Klik untuk melihat log lengkap\".",
                    "  - Dokumentasi: contoh panjang yang tidak semua orang perlu baca.",
                    "  - Soal latihan: <summary>Lihat jawaban</summary>.",
                    "  - Laporan bug: ringkasannya di atas, langkah dan pesan error dilipat.",
                    "",
                    "  Pola pikirnya selalu sama: yang PENTING tetap terlihat, yang panjang",
                    "  disimpan satu klik di belakangnya. Bukan untuk menyembunyikan isi yang",
                    "  wajib dibaca — orang tidak membuka apa yang tidak ia sangka ada.",
                    "",
                    "\"KALAU TERSEMBUNYI, APA MASIH KETEMU WAKTU DI-Ctrl+F?\"",
                    "",
                    "  Ini pertanyaan yang benar, dan jawabannya melegakan.",
                    "",
                    "  Isi <details> yang terlipat TETAP ADA di dokumen. Ia terbaca mesin",
                    "  pencari, dan browser modern membuka lipatannya SENDIRI ketika kata",
                    "  yang kamu cari lewat Ctrl+F ada di dalamnya, lalu menyorotnya.",
                    "  Chrome sudah lama begitu; browser lain menyusul. Di browser yang",
                    "  belum, kata itu memang belum ditemukan, tapi isinya tidak lenyap.",
                    "",
                    "  Bandingkan dengan lipatan buatan sendiri dari div + JavaScript.",
                    "  Cara paling umum menyembunyikannya adalah display: none — dan apa pun",
                    "  yang display: none tidak ada bagi Ctrl+F, tidak ada bagi pembaca layar,",
                    "  dan tidak ada bagi orang yang mencetak halamannya.",
                    "",
                    "  Tambahan yang tidak kalah penting: pembaca layar menyebut <summary>",
                    "  sebagai tombol buka-tutup lengkap dengan keadaannya (\"terlipat\" /",
                    "  \"terbuka\"), jadi orang yang tidak melihat layar tahu ada isi di baliknya.",
                    "  Div yang cuma diberi onclick tidak mengatakan apa-apa.",
                ],
            },
            {
                "heading": "FAQ yang bisa dilipat, tanpa JavaScript",
                "code": """<!doctype html>
<html lang="id">
<head>
  <meta charset="utf-8">
  <title>Tanya Jawab - Warung Kopi Pagi</title>
</head>
<body>
  <h1>Tanya jawab</h1>

  <details name="faq" open>
    <summary>Bisakah pesan lewat telepon?</summary>
    <p>Bisa. Telepon 022-5550123 satu jam sebelum diambil.</p>
  </details>

  <details name="faq">
    <summary>Apakah menerima pembayaran tunai?</summary>
    <p>Menerima. Kartu dan dompet digital juga bisa.</p>
  </details>

  <details name="faq">
    <summary>Boleh membawa wadah sendiri?</summary>
    <p>Boleh, dan dapat potongan 2.000 rupiah.</p>
    <p>Wadahnya kami cuci lebih dulu.</p>
  </details>
</body>
</html>""",
            },
            {
                "body": [
                    "Pohon strukturnya:",
                    "",
                    "  <!doctype html>",
                    "  html lang=\"id\"",
                    "    head",
                    "      meta charset=\"utf-8\"",
                    "      title \"Tanya Jawab - Warung Kopi Pagi\"",
                    "    body",
                    "      h1 \"Tanya jawab\"",
                    "      details name=\"faq\" open",
                    "        summary \"Bisakah pesan lewat telepon?\"",
                    "        p \"Bisa. Telepon 022-5550123 satu jam sebelum diambil.\"",
                    "      details name=\"faq\"",
                    "        summary \"Apakah menerima pembayaran tunai?\"",
                    "        p \"Menerima. Kartu dan dompet digital juga bisa.\"",
                    "      details name=\"faq\"",
                    "        summary \"Boleh membawa wadah sendiri?\"",
                    "        p \"Boleh, dan dapat potongan 2.000 rupiah.\"",
                    "        p \"Wadahnya kami cuci lebih dulu.\"",
                    "",
                    "Lihat baik-baik: summary dan paragraf-paragrafnya sama-sama anak",
                    "langsung details, sejajar, tidak ada yang lebih dalam. Yang membedakan",
                    "keduanya cuma URUTAN — anak pertama jadi judul lipatan, sisanya jadi",
                    "isi. Itu sebabnya aturan \"anak pertama\" tadi bukan formalitas.",
                    "",
                    "Perhatikan juga: 'open' tercetak tanpa nilai, dan ia berdiri sesudah",
                    "name karena atribut diurutkan alfabetis. Keduanya sudah dijelaskan di",
                    "materi Atribut.",
                    "",
                    "<dialog>: KOTAK YANG MENUMPUK DI ATAS HALAMAN",
                    "",
                    "Elemen ini punya DUA cara muncul, dan bedanya jauh lebih besar daripada",
                    "kelihatannya. Salah memilih menghasilkan sesuatu yang terlihat benar",
                    "tapi berperilaku sama sekali lain.",
                    "",
                    "  1. Atribut open — sama seperti details, ini atribut boolean.",
                    "",
                    "       <dialog open>Meja 4 sudah siap.</dialog>",
                    "",
                    "     Kotaknya muncul APA ADANYA, di posisinya berdiri di dalam alur",
                    "     halaman. Halaman di belakangnya tetap bisa diklik dan digulir.",
                    "     Esc tidak menutupnya. Tidak ada latar gelap.",
                    "     Ini BUKAN modal. Ini kotak biasa yang kebetulan terlihat.",
                    "",
                    "  2. showModal() dari JavaScript — modal yang sesungguhnya.",
                    "",
                    "       konfirmasi.showModal();",
                    "",
                    "     Yang kamu dapat sekaligus, tanpa menulis satu pun aturannya:",
                    "",
                    "       - Kotaknya melayang di tengah, di atas SELURUH isi halaman,",
                    "         tanpa kamu perlu memikirkan z-index sama sekali.",
                    "       - Sisa halaman jadi mati: tidak bisa diklik, tidak bisa dipilih,",
                    "         dan tidak bisa dicapai dengan Tab. Fokus keyboard terkunci",
                    "         di dalam kotak sampai kotaknya ditutup.",
                    "       - Ada lapisan gelap di belakangnya. Namanya ::backdrop, dan itu",
                    "         satu-satunya pegangan untuk menatanya:",
                    "",
                    "           dialog::backdrop { background: rgba(0, 0, 0, 0.5); }",
                    "",
                    "       - Esc menutupnya.",
                    "       - Pembaca layar mengumumkannya sebagai dialog dan memindahkan",
                    "         pembacaannya ke dalam kotak.",
                    "",
                    "  Membangun semua itu sendiri dari div adalah pekerjaan berhari-hari,",
                    "  dan bagian \"fokus terkunci di dalam kotak\" hampir selalu terlupa.",
                    "  Itu sebabnya modal buatan sendiri sering bisa di-Tab tembus ke",
                    "  halaman di belakangnya: kursor keyboard berjalan ke tombol yang tidak",
                    "  terlihat, orang yang memakai keyboard tersesat, dan yang membuatnya",
                    "  tidak pernah tahu karena ia mengujinya pakai tetikus.",
                    "",
                    "Menutupnya ada tiga jalan: Esc, konfirmasi.close() dari JavaScript,",
                    "atau — tanpa JavaScript sama sekali — lewat <form method=\"dialog\">.",
                    "",
                    "<form method=\"dialog\">: METHOD YANG TIDAK MENGIRIM APA PUN",
                    "",
                    "Di materi Formulir kamu belajar dua method: get dan post. Ada method",
                    "ketiga, dan ia cuma sah di dalam <dialog>:",
                    "",
                    "  <dialog id=\"konfirmasi\">",
                    "    <form method=\"dialog\">",
                    "      <button value=\"batal\">Ya, batalkan</button>",
                    "      <button value=\"lanjut\">Tidak jadi</button>",
                    "    </form>",
                    "  </dialog>",
                    "",
                    "  method=\"dialog\" tidak menghubungi server, tidak memuat ulang halaman,",
                    "  dan tidak butuh action. Yang dilakukannya persis dua hal:",
                    "",
                    "    1. Menutup dialognya.",
                    "    2. Menyimpan value tombol yang ditekan ke returnValue dialog itu.",
                    "",
                    "  Ingat jebakan di materi Formulir: <button> di dalam <form> bawaannya",
                    "  type=\"submit\". Di sini justru itu yang kita mau — menekan tombolnya",
                    "  berarti \"mengirim\" formulir, dan mengirim formulir method=\"dialog\"",
                    "  berarti menutup kotaknya sambil mencatat tombol mana yang ditekan.",
                    "",
                    "  Kalau ditutup dengan Esc, returnValue-nya string kosong. Perlakukan",
                    "  itu sebagai \"batal\": orang yang menekan Esc tidak sedang menyetujui",
                    "  apa pun, dan menganggapnya \"ya\" adalah cara menghapus pesanan orang.",
                    "",
                    "Contoh berikutnya memang punya sepotong <script>. Itu JavaScript, dan",
                    "ia punya kursus sendiri di aplikasi ini — cara menempelkannya sudah",
                    "dibahas di materi Menempelkan CSS dan JavaScript. Yang perlu kamu lihat",
                    "di sini cuma betapa sedikitnya: satu showModal(), sisanya HTML.",
                ],
            },
            {
                "heading": "Status pesanan: dialog, progress, meter, dan output",
                "code": """<!doctype html>
<html lang="id">
<head>
  <meta charset="utf-8">
  <title>Status Pesanan KP-0421</title>
</head>
<body>
  <h1>Pesanan KP-0421</h1>

  <p>
    <label for="tahap">Tahap penyiapan</label>
    <progress id="tahap" max="4" value="3">3 dari 4 tahap</progress>
  </p>

  <p>
    <label for="stok">Sisa biji Gayo</label>
    <meter id="stok" min="0" max="1000" low="200" high="800"
           optimum="1000" value="150">150 gram dari 1000</meter>
  </p>

  <form id="hitung" action="/tambah" method="post">
    <label for="jumlah">Tambah gelas</label>
    <input type="number" id="jumlah" name="jumlah" min="0" max="10" value="2">

    <label for="harga">Harga per gelas</label>
    <input type="number" id="harga" name="harga" min="0" step="500" value="15000">

    <output for="jumlah harga" name="total">30000</output>

    <button type="submit">Tambah</button>
  </form>

  <button id="tombol-batal" type="button">Batalkan pesanan</button>
  <p id="hasil"></p>

  <dialog id="konfirmasi">
    <form method="dialog">
      <h2>Batalkan pesanan ini?</h2>
      <p>Kopi yang sudah diseduh tidak bisa dikembalikan.</p>
      <button value="batal">Ya, batalkan</button>
      <button value="lanjut" autofocus>Tidak jadi</button>
    </form>
  </dialog>

  <script>
    const konfirmasi = document.getElementById("konfirmasi");
    const hasil = document.getElementById("hasil");
    const hitung = document.getElementById("hitung");

    document.getElementById("tombol-batal").addEventListener("click", () => {
      konfirmasi.showModal();
    });

    konfirmasi.addEventListener("close", () => {
      hasil.textContent = "Tombol yang ditekan: " + konfirmasi.returnValue;
    });

    hitung.addEventListener("input", () => {
      const gelas = hitung.jumlah.valueAsNumber || 0;
      const satuan = hitung.harga.valueAsNumber || 0;
      hitung.total.value = gelas * satuan;
    });
  </script>
</body>
</html>""",
            },
            {
                "body": [
                    "Pohon bagian dialognya:",
                    "",
                    "  dialog id=\"konfirmasi\"",
                    "    form method=\"dialog\"",
                    "      h2 \"Batalkan pesanan ini?\"",
                    "      p \"Kopi yang sudah diseduh tidak bisa dikembalikan.\"",
                    "      button value=\"batal\" \"Ya, batalkan\"",
                    "      button autofocus value=\"lanjut\" \"Tidak jadi\"",
                    "",
                    "Dialognya ditulis di dalam <body> seperti elemen biasa, di mana saja,",
                    "dan selama belum dibuka ia tidak terlihat sama sekali — tidak perlu",
                    "kamu sembunyikan dengan CSS lebih dulu.",
                    "",
                    "autofocus menentukan tombol mana yang terfokus saat kotaknya muncul.",
                    "Untuk tindakan yang MERUSAK, arahkan ke pilihan yang aman: orang yang",
                    "refleks menekan Enter tidak seharusnya kehilangan pesanannya.",
                    "",
                    "<progress> LAWAN <meter>: DUA-DUANYA BILAH, ARTINYA BEDA",
                    "",
                    "  <progress max=\"4\" value=\"3\">3 dari 4 tahap</progress>",
                    "",
                    "    Untuk pekerjaan yang SEDANG BERJALAN dan akan selesai: unggahan,",
                    "    pemasangan, tahap ke-3 dari 4, kuis nomor 7 dari 10.",
                    "    - value naik seiring waktu, max adalah 100 persennya.",
                    "    - <progress> TANPA value berarti \"sedang bekerja, belum tahu",
                    "      sampai kapan\": bilahnya bergerak bolak-balik tanpa ujung.",
                    "      Menghapus value adalah cara resmi menyatakan itu.",
                    "",
                    "  <meter min=\"0\" max=\"1000\" low=\"200\" high=\"800\"",
                    "         optimum=\"1000\" value=\"150\">150 gram dari 1000</meter>",
                    "",
                    "    Untuk UKURAN yang diam di dalam sebuah rentang: sisa baterai,",
                    "    sisa stok, skor ujian, ruang disk terpakai.",
                    "    - min dan max menyebut ujung-ujung rentangnya.",
                    "    - low dan high memotong rentang itu jadi tiga wilayah.",
                    "    - optimum menyebut di sebelah MANA yang bagus. Browser memakai",
                    "      ketiganya untuk memilih warna sendiri: hijau kalau nilainya",
                    "      di wilayah yang baik, kuning atau merah kalau menjauh.",
                    "      Di contoh tadi optimum ada di ujung atas sedangkan sisanya",
                    "      cuma 150 dari 1000, jadi bilahnya tampil sebagai peringatan —",
                    "      dan kamu tidak menulis satu pun aturan warna.",
                    "",
                    "  Kenapa keduanya tidak boleh saling menggantikan: <meter> tidak",
                    "  berarti \"sedang memuat\", dan <progress> tidak berarti \"kondisinya",
                    "  sedang buruk\". Yang membaca ini bukan cuma mata — pembaca layar",
                    "  mengumumkan keduanya dengan kalimat yang berbeda. Memakai <meter>",
                    "  untuk unggahan berarti memberitahu orang yang tidak melihat layar",
                    "  sesuatu yang salah, padahal di layarmu tampak wajar.",
                    "",
                    "  Teks di ANTARA kedua tagnya bukan hiasan dan bukan isi bilahnya.",
                    "  Itu cadangan untuk browser yang tidak mengenal elemennya, dan",
                    "  keterangan yang bisa kamu baca sendiri waktu memeriksa markup.",
                    "  Isi selalu, tulis angkanya dalam kalimat: \"3 dari 4 tahap\".",
                    "",
                    "<output>: TEMPAT MENARUH HASIL HITUNGAN",
                    "",
                    "  <output for=\"jumlah harga\" name=\"total\">30000</output>",
                    "",
                    "  - for menyebut isian MANA yang ikut menentukan angka ini, ditulis",
                    "    dengan id-nya dan dipisah spasi kalau lebih dari satu.",
                    "  - <output> tidak menghitung apa-apa sendiri. Yang menghitung tetap",
                    "    JavaScript; elemen ini cuma menyatakan \"isi di sini adalah HASIL\".",
                    "  - Justru itu gunanya: pembaca layar mengumumkan ulang isinya setiap",
                    "    kali berubah, tanpa kamu menambahkan apa pun. <span> tidak begitu —",
                    "    angkanya berubah diam-diam dan orang yang tidak melihat layar",
                    "    tidak pernah tahu totalnya sudah bergeser.",
                    "  - name membuatnya bisa dipanggil dari formulirnya (itulah",
                    "    hitung.total di skrip tadi), tapi isinya TIDAK ikut terkirim ke",
                    "    server. Ia hasil hitungan, bukan isian.",
                    "",
                    "PERINGATAN JUJUR SEBELUM KAMU MEMAKAINYA",
                    "",
                    "  Kelima elemen ini punya tampilan bawaan, dan tampilan bawaan itu",
                    "  BERBEDA-BEDA di tiap browser: bentuk segitiga <summary>, tebal dan",
                    "  lengkung <progress>, warna <meter>, lebar dan jarak <dialog>.",
                    "  Halaman yang sama tidak akan terlihat identik di dua komputer.",
                    "",
                    "  Menatanya dengan CSS juga lebih repot daripada elemen biasa.",
                    "  Sebagian bagiannya cuma bisa disentuh lewat pemilih khusus seperti",
                    "  ::backdrop atau ::-webkit-progress-bar, dan sebagian lagi memang",
                    "  tidak bisa diapa-apakan.",
                    "",
                    "  Karena itu banyak proyek besar tetap membuat versinya sendiri dari",
                    "  div — bukan karena elemen bawaannya jelek, tapi karena mereka butuh",
                    "  tampilan yang sama persis di mana-mana. Konsekuensinya buatmu: kamu",
                    "  akan bertemu KEDUA bentuk di kode nyata, dan harus sanggup membaca",
                    "  dua-duanya tanpa bingung.",
                    "",
                    "  Saran yang masuk akal untuk sekarang: mulai dari elemen bawaannya.",
                    "  Ia sudah benar dari sisi keyboard, fokus, dan pembaca layar sejak",
                    "  baris pertama — dan justru bagian itulah yang paling sering rusak",
                    "  di versi buatan sendiri, karena paling jarang diuji.",
                ],
            },
        ],
    },
    {
        "title": "19. Bisa Dipakai Semua Orang: role, aria-*, dan tabindex",
        "sections": [
            {
                "body": [
                    "Sepanjang kursus ini satu alasan muncul berulang-ulang: alt",
                    "supaya gambar punya keterangan, label supaya kolom isian punya",
                    "nama, header/nav/main supaya orang bisa melompat antar bagian,",
                    "lang supaya pelafalannya benar. Semuanya demi hal yang sama:",
                    "halaman yang tetap terpakai oleh orang yang tidak melihat",
                    "layarnya.",
                    "",
                    "Tapi kosakata resmi untuk urusan itu belum pernah disebut",
                    "sekali pun di sini, padahal di kode nyata ia ada di hampir",
                    "setiap berkas:",
                    "",
                    "  <button aria-label=\"Tutup\" aria-expanded=\"false\">",
                    "  <div role=\"dialog\" tabindex=\"-1\">",
                    "  <span aria-hidden=\"true\">x</span>",
                    "",
                    "Namanya ARIA - Accessible Rich Internet Applications.",
                    "Bentuknya atribut biasa, dan tiap atribut menjawab salah satu",
                    "dari tiga pertanyaan saja:",
                    "",
                    "  role=\"...\"            benda ini SEBENARNYA apa",
                    "  aria-label=\"...\"      namanya siapa",
                    "  aria-expanded=\"...\"   keadaannya sekarang bagaimana",
                    "",
                    "Kenapa ia perlu ada? Karena HTML tidak punya elemen untuk",
                    "setiap pola antarmuka. Ada <button> dan <table>, tapi tidak ada",
                    "<tab>, tidak ada <menu-lipat>, tidak ada <pemberitahuan>.",
                    "Pola-pola itu tetap dibangun orang, dari div dan button biasa,",
                    "dan ARIA-lah yang memberi tahu pembaca layar bahwa tumpukan div",
                    "itu sebenarnya sebuah kotak dialog yang sedang terbuka.",
                    "",
                    "SATU KALIMAT YANG MENENTUKAN SEGALANYA:",
                    "",
                    "  ARIA tidak mengubah apa pun. Bukan tampilannya, bukan",
                    "  perilakunya. Ia cuma mengganti apa yang DIUMUMKAN.",
                    "",
                    "Tulis role=\"button\" pada sebuah <div> dan yang kamu dapat cuma",
                    "pengumumannya: tidak ada kursor tangan, tidak ada Tab yang",
                    "mampir ke situ, tidak ada Enter atau Spasi yang menekannya,",
                    "tidak ada disabled yang bisa mematikannya. Semua itu harus kamu",
                    "tulis sendiri dengan CSS dan JavaScript, dan tiap satunya bisa",
                    "salah.",
                    "",
                    "Itu sebabnya aturan pertama ARIA berbunyi begini: kalau sudah",
                    "ada elemen HTML yang artinya pas, PAKAI ITU, dan jangan sentuh",
                    "ARIA sama sekali.",
                    "",
                    "  <div role=\"button\" tabindex=\"0\">Kirim</div>",
                    "      puluhan baris JavaScript baru menyusul",
                    "",
                    "  <button>Kirim</button>",
                    "      sudah benar sejak awal",
                    "",
                    "Elemen <dialog> yang baru saja kamu pelajari adalah contoh",
                    "paling jelas: ia sudah membawa role=\"dialog\" sendiri, mengurus",
                    "fokus sendiri, dan menutup dengan Esc sendiri. Menirunya dengan",
                    "div plus ARIA butuh kerja berhari-hari, dan hasilnya tetap lebih",
                    "buruk.",
                    "",
                    "NAMA-NAMANYA TIDAK BOLEH DIKARANG",
                    "",
                    "Materi soal atribut mengajarkan data-* boleh dinamai bebas:",
                    "data-harga, data-apa pun. Bentuk aria-* terlihat mirip, tapi",
                    "kebalikannya - daftar namanya baku dan tertutup. aria-expand,",
                    "aria-hidden=\"yes\", role=\"tombol\" tidak memicu error, tidak",
                    "dicoret editor, dan tidak melakukan apa-apa. Diam, seperti",
                    "kesalahan HTML lainnya.",
                ],
            },
            {
                "heading": "Satu bilah navigasi yang lengkap",
                "code": """<!doctype html>
<html lang="id">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Menu - Kopi Pagi</title>
</head>
<body>
  <a class="lewati" href="#isi">Lewati ke isi</a>

  <header>
    <h1>Kopi Pagi</h1>

    <button class="tombol-menu" type="button"
            aria-label="Buka menu"
            aria-expanded="false"
            aria-controls="menu-utama">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none"
           stroke="currentColor" stroke-width="2" aria-hidden="true">
        <path d="M4 7h16M4 12h16M4 17h16"/>
      </svg>
    </button>
  </header>

  <nav id="menu-utama" aria-label="Menu utama" hidden>
    <ul>
      <li><a href="index.html">Beranda</a></li>
      <li><a href="menu.html" aria-current="page">Menu</a></li>
      <li><a href="tentang.html">Tentang</a></li>
    </ul>
  </nav>

  <main id="isi" tabindex="-1">
    <h2>Menu hari ini</h2>
    <p>Kopi tubruk, kopi susu, dan es kopi gula aren.</p>
    <p id="kabar" aria-live="polite"></p>
  </main>

  <script>
    const tombol = document.querySelector(".tombol-menu");
    const menu = document.querySelector("#menu-utama");

    tombol.addEventListener("click", function () {
      const terbuka = tombol.getAttribute("aria-expanded") === "true";
      tombol.setAttribute("aria-expanded", terbuka ? "false" : "true");
      tombol.setAttribute("aria-label", terbuka ? "Buka menu" : "Tutup menu");
      menu.hidden = terbuka;
    });
  </script>
</body>
</html>""",
            },
            {
                "body": [
                    "role= MENGGANTI NAMA YANG DIUMUMKAN, BUKAN APA PUN YANG LAIN",
                    "",
                    "Yang sering ditemui:",
                    "",
                    "  button        sesuatu yang ditekan lalu terjadi sesuatu",
                    "  dialog        kotak yang menumpuk di atas halaman",
                    "  navigation    kumpulan tautan navigasi",
                    "  search        biasanya di <form role=\"search\">",
                    "  alert         pesan yang menghentikan; status untuk yang",
                    "                biasa saja (lihat aria-live nanti)",
                    "  tablist       pola tab, bertiga dengan tab dan tabpanel",
                    "  img           gumpalan yang harus dibaca sebagai SATU",
                    "                gambar, misalnya <svg> berisi ikon",
                    "  presentation  BUANG maknanya: \"anggap ini kotak kosong\".",
                    "                Boleh juga ditulis none.",
                    "",
                    "presentation dipakai saat elemen bermakna dipinjam untuk hal",
                    "lain. Contoh paling sering: <table role=\"presentation\"> yang",
                    "cuma dipakai menata tata letak, supaya pembaca layar tidak",
                    "mengumumkan \"tabel, 3 kolom, 8 baris\" untuk sesuatu yang sama",
                    "sekali bukan data.",
                    "",
                    "Perhatikan di contoh tadi: <nav> TIDAK diberi role=\"navigation\".",
                    "Elemen semantik sudah membawa perannya masing-masing - nav",
                    "berarti navigation, main berarti main, button berarti button.",
                    "Menuliskannya lagi cuma mengulang yang sudah ada. role= adalah",
                    "cara menyebut hal yang sama untuk elemen yang TIDAK punya makna",
                    "bawaan.",
                    "",
                    "MEMBERI NAMA",
                    "",
                    "Tombol menu di contoh isinya cuma gambar tiga garis. Tanpa teks",
                    "sama sekali, yang terdengar cuma \"tombol\" - dan orang tidak",
                    "akan menekan tombol yang tidak diketahuinya untuk apa.",
                    "",
                    "  aria-label=\"Buka menu\"",
                    "    Namanya ditulis langsung di situ.",
                    "",
                    "  aria-labelledby=\"judul-kotak\"",
                    "    Namanya diambil dari ISI elemen ber-id itu. Boleh menunjuk",
                    "    beberapa id sekaligus, dipisah spasi; hasilnya digabung",
                    "    berurutan.",
                    "",
                    "  aria-describedby=\"bantuan\"",
                    "    Keterangan tambahan, dibacakan SESUDAH namanya. Untuk",
                    "    syarat sandi, format tanggal, catatan kecil di bawah kolom.",
                    "",
                    "Kalau lebih dari satu terpasang, urutan menangnya:",
                    "aria-labelledby mengalahkan aria-label, dan aria-label",
                    "mengalahkan teks di dalam elemennya sendiri. Akibatnya yang",
                    "menyakitkan:",
                    "",
                    "  <button aria-label=\"Kirim\">Batal</button>",
                    "",
                    "Di layar tertulis \"Batal\", yang terdengar \"Kirim\". Kalau",
                    "elemennya sudah punya teks yang benar, jangan tambahkan",
                    "aria-label sama sekali.",
                    "",
                    "Kenapa <div aria-label=\"Menu utama\"> tidak berbunyi apa-apa?",
                    "Karena div dan span tidak punya peran - di mata pembaca layar",
                    "mereka \"generic\", dan sesuatu yang bukan apa-apa tidak bisa",
                    "dipanggil dengan nama. Nama cuma menempel pada elemen yang",
                    "punya peran: tombol, tautan, kolom isian, atau landmark seperti",
                    "<nav> dan <section>.",
                    "",
                    "Di contoh tadi aria-label=\"Menu utama\" dipasang di <nav>, dan",
                    "itu berguna justru saat ada dua nav di satu halaman: yang",
                    "terdengar jadi \"navigasi Menu utama\" dan \"navigasi Menu kaki\",",
                    "bukan dua-duanya \"navigasi\" tanpa bisa dibedakan.",
                    "",
                    "aria-controls=\"menu-utama\" menunjuk id elemen yang dikendalikan",
                    "tombol itu. Dukungannya di pembaca layar tipis dan tidak",
                    "merugikan; kamu akan sering melihatnya, jadi kenali bentuknya.",
                    "",
                    "aria-hidden=\"true\" MENGHAPUS, BUKAN MENYEMBUNYIKAN",
                    "",
                    "Elemen ber-aria-hidden beserta seluruh isinya lenyap dari",
                    "pembaca layar, tapi tetap terlihat di layar. Itu kebalikan",
                    "atribut hidden, yang menghilangkan elemennya dari keduanya.",
                    "",
                    "Gunanya untuk hiasan yang sudah diwakili teks di sebelahnya:",
                    "ikon tiga garis di contoh tadi tidak perlu dibacakan, karena",
                    "tombolnya sudah bernama \"Buka menu\". Tanpa aria-hidden, isi",
                    "<svg> bisa terbaca sebagai deretan bunyi tak berarti.",
                    "",
                    "Yang jadi bug: memasang aria-hidden=\"true\" pada sesuatu yang",
                    "masih bisa difokuskan - tombol, tautan, atau kolom isian. Tab",
                    "tetap mampir ke sana, tapi pembaca layar tidak punya apa pun",
                    "untuk dibacakan. Yang terdengar cuma sunyi, dan orang itu",
                    "mengira halamannya macet. Kalau memang harus hilang seluruhnya,",
                    "pakai hidden, atau display: none dari CSS.",
                ],
            },
            {
                "body": [
                    "KEADAAN: ARIA YANG NILAINYA BERUBAH-UBAH",
                    "",
                    "  aria-expanded   menu lipat: sedang terbuka atau tertutup",
                    "  aria-current    \"yang ini yang sedang aktif\"",
                    "  aria-selected   tab mana yang sedang dipilih",
                    "  aria-checked    kotak centang buatan sendiri, yang bukan",
                    "                  <input type=\"checkbox\">",
                    "  aria-disabled   dimatikan, tapi masih disinggahi Tab",
                    "",
                    "Letak aria-expanded sering salah tebak: ia dipasang di",
                    "TOMBOLNYA, bukan di menu yang dibuka-tutup. Yang sedang",
                    "dijelaskan adalah tombolnya - \"tombol ini, sekarang, sedang",
                    "membuka sesuatu\". Menunya sendiri tidak perlu berkata apa-apa.",
                    "",
                    "aria-current=\"page\" menandai tautan halaman yang sedang dibuka,",
                    "seperti di contoh tadi. Nilai lainnya: step untuk langkah yang",
                    "sedang dikerjakan, lalu date, time, dan location; kalau tidak",
                    "ada yang pas, true. Tanpa itu, satu-satunya penanda halaman",
                    "aktif biasanya cuma warna - dan warna tidak terdengar.",
                    "",
                    "aria-disabled=\"true\" berbeda dari atribut disabled yang kamu",
                    "kenal dari materi formulir:",
                    "",
                    "  disabled       Mati total: tidak bisa diklik, dilewati Tab,",
                    "                 dan nilainya tidak ikut terkirim.",
                    "",
                    "  aria-disabled  Masih bisa disinggahi Tab dan tetap terbaca;",
                    "                 ia cuma DIUMUMKAN nonaktif. Dipakai supaya",
                    "                 orang ketemu tombolnya dan tahu kenapa ia",
                    "                 belum bisa ditekan. Konsekuensinya: kliknya",
                    "                 harus kamu tolak sendiri di JavaScript,",
                    "                 karena browser tidak menolaknya.",
                    "",
                    "ATURAN BESINYA:",
                    "",
                    "  Nilai ARIA tidak memperbarui dirinya sendiri.",
                    "  JavaScript yang harus menggantinya.",
                    "",
                    "aria-expanded=\"false\" yang ditulis sekali lalu tidak pernah",
                    "berubah LEBIH BURUK daripada tidak ditulis sama sekali: menunya",
                    "sudah terbuka lebar di layar, dan pembaca layar tetap berkata",
                    "\"tertutup\". Itu sebabnya <script> kecil di contoh tadi bukan",
                    "hiasan - tanpa dia, dua atribut di tombol itu berbohong sejak",
                    "klik pertama.",
                    "",
                    "JEBAKAN: aria-* BUKAN ATRIBUT BOOLEAN",
                    "",
                    "Materi soal atribut menunjukkan disabled=\"false\" tetap",
                    "MEMATIKAN tombolnya, karena yang dibaca browser cuma",
                    "ada-tidaknya atribut itu. ARIA bekerja terbalik - nilainya",
                    "benar-benar dibaca:",
                    "",
                    "  aria-hidden=\"false\"     tidak disembunyikan; sama saja",
                    "                          dengan tidak ditulis",
                    "  aria-expanded=\"false\"   tertutup - dan justru ini yang",
                    "                          WAJIB ditulis",
                    "",
                    "Bedanya penting: menghapus aria-expanded bukan berarti",
                    "\"tertutup\", tapi \"tombol ini memang tidak membuka apa pun\".",
                    "Dua pernyataan yang sama sekali berbeda.",
                    "",
                    "PESAN YANG BARU MUNCUL BELAKANGAN",
                    "",
                    "Pembaca layar membacakan halaman dari atas ke bawah. Tulisan",
                    "yang baru muncul sesudah bacaannya lewat - \"Tersimpan\",",
                    "\"12 hasil ditemukan\", \"Sandi terlalu pendek\" - lewat begitu",
                    "saja tanpa terdengar sedikit pun.",
                    "",
                    "  <p id=\"kabar\" aria-live=\"polite\"></p>",
                    "",
                    "aria-live menandai sebuah kotak sebagai \"awasi isinya\". Begitu",
                    "JavaScript menulis sesuatu ke dalamnya, isinya dibacakan, tanpa",
                    "perlu memindahkan fokus ke sana.",
                    "",
                    "  polite     Tunggu sampai pembacaan yang sedang jalan",
                    "             selesai. Hampir selalu ini yang kamu mau.",
                    "  assertive  Potong sekarang juga. Hanya untuk galat yang",
                    "             menghentikan pekerjaan orangnya.",
                    "",
                    "Dua bentuk singkatnya lebih sering dipakai daripada aria-live",
                    "mentah:",
                    "",
                    "  role=\"status\"  sudah berarti aria-live=\"polite\"",
                    "  role=\"alert\"   sudah berarti aria-live=\"assertive\"",
                    "",
                    "JEBAKANNYA: kotaknya harus SUDAH ADA di halaman sebelum",
                    "pesannya masuk. Kalau JavaScript membuat elemen aria-live",
                    "beserta tulisan \"Tersimpan\" sekaligus lalu menempelkannya ke",
                    "halaman, tidak ada yang sempat diawasi dan tidak ada yang",
                    "terdengar. Itu sebabnya di contoh tadi <p id=\"kabar\"> sengaja",
                    "ditulis KOSONG sejak awal.",
                ],
            },
            {
                "body": [
                    "tabindex: SIAPA YANG DISINGGAHI Tab, DAN DALAM URUTAN APA",
                    "",
                    "Tombol Tab memindahkan fokus dari satu elemen ke elemen",
                    "berikutnya. Yang ikut antrean cuma elemen yang memang bisa",
                    "difokuskan: <a href=\"...\">, <button>, <input>, <select>,",
                    "<textarea>. Urutannya sama persis dengan urutan penulisannya di",
                    "berkas. (<a> tanpa href tidak ikut - tanpa href ia bukan",
                    "tautan, cuma teks biasa yang kebetulan dibungkus <a>.)",
                    "",
                    "  tabindex=\"0\"",
                    "    Ikut antrean, di posisi tulisannya. Untuk elemen yang",
                    "    biasanya tidak bisa difokuskan tapi kamu jadikan",
                    "    interaktif. Kalau kamu sedang mengetik ini, berhenti",
                    "    sebentar dan tanyakan lagi kenapa bukan <button>.",
                    "",
                    "  tabindex=\"-1\"",
                    "    TIDAK ikut antrean Tab, tapi bisa difokuskan dari",
                    "    JavaScript lewat elemen.focus(). Ini yang dipakai di contoh",
                    "    tadi pada <main id=\"isi\" tabindex=\"-1\">: tautan \"Lewati ke",
                    "    isi\" melompat ke sana. Tanpa tabindex=\"-1\" fokusnya tidak",
                    "    ikut pindah - halamannya bergulir, tapi Tab berikutnya",
                    "    kembali lagi ke menu yang barusan susah payah dilewati.",
                    "",
                    "  tabindex=\"1\" ke atas",
                    "    JANGAN PERNAH. Angka positif memotong antrean: SEMUA elemen",
                    "    bertabindex positif dikunjungi lebih dulu, dari angka",
                    "    terkecil, sebelum satu pun elemen biasa. Satu tabindex=\"1\"",
                    "    di sudut halaman mengacaukan urutan seluruh halaman, dan",
                    "    yang mengalaminya cuma pengguna keyboard - bukan kamu yang",
                    "    mengetesnya dengan tetikus.",
                    "",
                    "Memasang tabindex=\"0\" pada elemen yang memang sudah bisa",
                    "difokuskan (button, a, input) tidak salah, tapi juga tidak",
                    "menambah apa-apa.",
                    "",
                    "Tautan \"Lewati ke isi\" di baris pertama <body> itu pola baku,",
                    "bukan karangan: pengguna keyboard jadi tidak perlu menekan Tab",
                    "dua puluh kali melewati seluruh menu, di setiap halaman.",
                    "Biasanya ia disembunyikan CSS sampai difokuskan - dan penanda",
                    "fokusnya sendiri sudah dibahas di kursus CSS, di materi",
                    "pseudo-class. Larangan menulis outline: none di sana dan materi",
                    "ini menjaga hal yang sama persis, dari dua sisi.",
                    "",
                    "SISA ATRIBUT GLOBAL",
                    "",
                    "Materi soal atribut menyebut tujuh atribut global: class, id,",
                    "title, lang, hidden, style, data-*. Daftarnya tidak berhenti di",
                    "situ. Semua yang di bawah ini juga boleh dipasang di elemen APA",
                    "PUN, termasuk aria-* dan tabindex tadi:",
                    "",
                    "  dir=\"rtl\"",
                    "    Arah tulisan kanan-ke-kiri (Arab, Ibrani). dir=\"auto\"",
                    "    menyuruh browser menebak dari isinya sendiri - berguna",
                    "    untuk kiriman pengguna yang bahasanya tak diketahui.",
                    "",
                    "  contenteditable",
                    "    Elemen apa pun jadi bisa diketik langsung oleh pengguna.",
                    "    Inilah dasar semua editor teks di dalam halaman web.",
                    "",
                    "  spellcheck=\"false\"",
                    "    Matikan garis merah pemeriksa ejaan. Untuk kolom kode,",
                    "    nama pengguna, dan nomor.",
                    "",
                    "  translate=\"no\"",
                    "    Jangan disentuh penerjemah otomatis. Untuk nama merek,",
                    "    potongan kode, dan nama orang.",
                    "",
                    "  draggable=\"true\"",
                    "    Boleh diseret. Seretannya sendiri tetap urusan JavaScript;",
                    "    atribut ini cuma mengizinkan.",
                    "",
                    "  inputmode=\"numeric\"",
                    "    Papan ketik mana yang muncul di ponsel, TANPA mengubah",
                    "    jenis isiannya. Kode pos \"08110\" di type=\"number\" bisa",
                    "    kehilangan nol depannya; type=\"text\" plus inputmode tetap",
                    "    memberi papan ketik angka tanpa merusak nilainya.",
                    "",
                    "  accesskey=\"s\"",
                    "    Pintasan papan ketik. Hampir selalu bentrok dengan pintasan",
                    "    browser atau pembaca layar; sekarang jarang dipakai.",
                    "",
                    "Tiga di antaranya memakai \"true\"/\"false\" (contenteditable,",
                    "spellcheck, draggable) dan translate memakai \"yes\"/\"no\" -",
                    "nilainya benar-benar dibaca, jadi spellcheck=\"false\" memang",
                    "mematikan, tidak seperti disabled=\"false\". Sebuah atribut",
                    "boolean atau bukan tidak bisa ditebak dari bentuknya; itu harus",
                    "dihafal atau dicari satu per satu.",
                    "",
                    "Penutup yang layak diingat: ARIA terbaik adalah ARIA yang tidak",
                    "perlu kamu tulis. Sebagian besar halaman sudah bisa dipakai",
                    "semua orang cuma dengan elemen yang tepat, label yang terikat,",
                    "alt yang jujur, dan urutan penulisan yang masuk akal - persis",
                    "yang sudah kamu pelajari sejak materi pertama. ARIA dipakai",
                    "saat HTML benar-benar kehabisan elemen, bukan sebagai tambalan",
                    "untuk HTML yang dipilih asal-asalan.",
                ],
            },
        ],
    },
    {
        "title": "20. Metadata: title, meta, dan Kenapa Itu Penting",
        "sections": [
            {
                "body": [
                    "Metadata = data tentang data. Isi <head> tidak muncul satu",
                    "huruf pun di halaman, tapi ia yang menentukan:",
                    "",
                    "  - tulisan di tab browser dan di daftar bookmark",
                    "  - judul dan ringkasan di hasil mesin pencari",
                    "  - kartu pratinjau saat tautanmu dikirim ke grup chat",
                    "  - apakah halamanmu terbaca benar di ponsel",
                    "  - bagaimana huruf-hurufnya diterjemahkan",
                    "",
                    "Bagian ini paling sering dilewati pemula karena hasilnya tidak",
                    "kelihatan saat berkasnya dibuka sendiri. Yang kelihatan baru",
                    "nanti — saat halamannya dibagikan, dan yang muncul di chat",
                    "adalah \"Document\" tanpa gambar.",
                ]
            },
            {
                "heading": "head yang lengkap",
                "code": """<!doctype html>
<html lang="id">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <title>Cara Menyeduh V60 - Kopi Pagi</title>
  <meta name="description"
        content="Panduan singkat menyeduh V60 untuk pemula: takaran bubuk, suhu air, dan waktu tuang.">

  <link rel="icon" href="favicon.png">
  <link rel="canonical" href="https://kopipagi.test/v60.html">
  <link rel="stylesheet" href="gaya.css">

  <meta property="og:title" content="Cara Menyeduh V60">
  <meta property="og:description" content="Takaran, suhu air, dan waktu tuang.">
  <meta property="og:image" content="https://kopipagi.test/gambar/v60.jpg">
  <meta property="og:url" content="https://kopipagi.test/v60.html">
  <meta property="og:type" content="article">

  <meta name="theme-color" content="#6f4e37">
</head>
<body>
  <h1>Cara Menyeduh V60</h1>
  <p>Takaran dasarnya 15 gram bubuk untuk 250 ml air.</p>
</body>
</html>"""
            },
            {
                "body": [
                    "<title> — satu-satunya elemen head yang WAJIB ada.",
                    "",
                    "  Di mana saja ia muncul:",
                    "    - tab browser, terutama saat tabnya banyak dan sempit",
                    "    - nama bawaan saat halaman di-bookmark",
                    "    - baris biru yang diklik orang di hasil pencarian",
                    "    - hal PERTAMA yang dibacakan pembaca layar saat halaman",
                    "      dibuka, sebelum apa pun yang lain",
                    "",
                    "  Aturan menulisnya:",
                    "    - Unik untuk setiap halaman. Sepuluh halaman berjudul",
                    "      \"Beranda\" membuat riwayat browser tidak berguna.",
                    "    - Sekitar 50-60 huruf. Lebih dari itu dipotong.",
                    "    - Yang khas di depan: \"Cara Menyeduh V60 - Kopi Pagi\",",
                    "      bukan \"Kopi Pagi - Cara Menyeduh V60\". Di tab sempit",
                    "      yang terlihat cuma beberapa huruf pertama.",
                    "",
                    "<meta name=\"description\">",
                    "  Ringkasan 1-2 kalimat. Tidak menaikkan peringkat pencarian,",
                    "  tapi inilah tulisan yang dibaca orang sebelum memutuskan",
                    "  mengklik. Sekitar 150 huruf.",
                    "",
                    "  Kalau tidak ada, mesin pencari mengambil sepotong teks",
                    "  sembarang dari halamanmu — sering kali menu navigasi.",
                ]
            },
            {
                "body": [
                    "Meta og: (Open Graph) — pratinjau saat dibagikan.",
                    "",
                    "  Ketika seseorang menempelkan tautanmu di WhatsApp, Slack,",
                    "  atau media sosial, aplikasi itu mengambil halamanmu dan",
                    "  mencari tag og:. Dari situ ia menyusun kartu pratinjau.",
                    "",
                    "  PERHATIKAN BAIK-BAIK: og memakai property=, BUKAN name=.",
                    "",
                    "    <meta property=\"og:title\" content=\"Menyeduh V60\">  benar",
                    "    <meta name=\"og:title\" content=\"Menyeduh V60\">      mati",
                    "",
                    "  Dari semua tag meta, cuma og yang memakai property=; yang",
                    "  lain memakai name=\"...\" content=\"...\" seperti yang sudah",
                    "  kamu tulis — dan itu sebabnya ia paling sering salah ketik.",
                    "  Sebabnya sejarah: Open Graph bukan bikinan pembuat HTML, ia",
                    "  menumpang aturan lain yang kebetulan memakai property.",
                    "",
                    "  Gejalanya jenis yang paling menjengkelkan: halamannya normal,",
                    "  tidak ada error di mana pun, cuma kartu pratinjaunya kosong.",
                    "  Dan kamu baru tahu sesudah tautannya terlanjur dikirim.",
                    "",
                    "  Empat yang berguna: og:title, og:description, og:image,",
                    "  og:url. Tanpa itu semua, yang muncul cuma alamat mentah.",
                    "",
                    "  og:image harus alamat LENGKAP (https://...), bukan alamat",
                    "  relatif. Yang mengambilnya server lain, dan server lain",
                    "  tidak tahu \"gambar/v60.jpg\" itu relatif terhadap apa.",
                    "",
                    "Sisanya:",
                    "  <link rel=\"icon\">      ikon kecil di tab.",
                    "  <link rel=\"canonical\"> alamat resmi halaman ini, kalau isi",
                    "                         yang sama bisa dicapai lewat beberapa",
                    "                         alamat berbeda.",
                    "  <meta name=\"theme-color\"> mewarnai bilah atas browser ponsel.",
                    "  <meta name=\"robots\" content=\"noindex\"> minta halaman ini",
                    "                         tidak dimasukkan hasil pencarian.",
                ]
            },
            {
                "body": [
                    "Dua hal yang urusannya bukan kosmetik:",
                    "",
                    "1. <meta charset=\"utf-8\"> HARUS ADA DI AWAL.",
                    "",
                    "   Browser mulai menerjemahkan byte jadi huruf sejak byte",
                    "   pertama. Ia memberi kesempatan sampai sekitar 1024 byte",
                    "   pertama untuk diberi tahu tabel hurufnya; sesudah itu ia",
                    "   sudah terlanjur menebak, dan kalau tebakannya salah ia akan",
                    "   memuat ulang seluruh halaman dari awal.",
                    "",
                    "   Karena itu charset ditulis sebagai baris PERTAMA di dalam",
                    "   head, bukan di bawah title yang panjang.",
                    "",
                    "   Gejala kalau salah: \"Kopi\" masih aman, tapi tanda kutip",
                    "   melengkung dan huruf beraksen berubah jadi rangkaian simbol",
                    "   seperti Ã© atau â€™.",
                    "",
                    "2. lang=\"id\" PADA <html>.",
                    "",
                    "   Pembaca layar memilih suara dan aturan pelafalan dari",
                    "   sana. Halaman Indonesia tanpa lang dibacakan dengan aturan",
                    "   Inggris: \"seduh\" jadi tidak dikenali sama sekali, dan",
                    "   mendengarkan satu halaman penuh seperti itu melelahkan.",
                    "",
                    "   Ia juga yang dipakai penerjemah otomatis dan pemeriksa ejaan.",
                    "   Satu atribut, tujuh huruf, dan hampir selalu dilupakan.",
                ]
            },
            {
                "body": [
                    "BARIS HEAD LAIN YANG PASTI KAMU LIHAT",
                    "",
                    "head situs sungguhan sering dua kali lebih panjang dari contoh",
                    "di atas. Isinya bukan hal ajaib. Ini yang paling sering muncul,",
                    "satu keterangan masing-masing, supaya kamu berhenti bertanya-",
                    "tanya saat membacanya:",
                    "",
                    "  <meta http-equiv=\"...\" content=\"...\">",
                    "    Bentuk meta yang berlagak seperti kepala jawaban server.",
                    "    Yang masih layak dipakai praktis tinggal satu, itu pun",
                    "    jarang: http-equiv=\"refresh\" untuk memuat ulang atau",
                    "    melompat ke halaman lain sesudah sekian detik.",
                    "",
                    "  <link rel=\"preconnect\" href=\"https://fonts.gstatic.com\">",
                    "    \"Bukakan dulu sambungan ke server itu, sebentar lagi",
                    "    kupakai.\" Menghemat waktu berjabat tangan. Ini yang",
                    "    membuka head hampir setiap situs yang memakai huruf dari",
                    "    Google Fonts.",
                    "",
                    "  <link rel=\"preload\" href=\"huruf.woff2\" as=\"font\" crossorigin>",
                    "    \"Unduh berkas ini sekarang juga, prioritas tinggi.\" Untuk",
                    "    berkas yang sudah pasti dipakai tapi baru ketahuan telat,",
                    "    misalnya huruf yang namanya baru disebut di dalam CSS.",
                    "    Namanya kebetulan sama dengan atribut preload pada",
                    "    <video> dan <audio>; keduanya tidak berhubungan.",
                    "",
                    "  <link rel=\"manifest\" href=\"situs.webmanifest\">",
                    "    Berkas keterangan supaya situsnya bisa \"dipasang\" seperti",
                    "    aplikasi di layar utama ponsel: namanya, ikonnya, warnanya.",
                    "",
                    "  <link rel=\"apple-touch-icon\" href=\"ikon-180.png\">",
                    "    Ikon khusus untuk layar utama iPhone dan iPad. Ukurannya",
                    "    jauh lebih besar daripada ikon tab biasa.",
                    "",
                    "  <link rel=\"alternate\" ...>",
                    "    \"Versi lain dari halaman ini ada di sini.\" Dua pemakaian",
                    "    yang lazim: umpan RSS (type=\"application/rss+xml\") dan",
                    "    halaman yang sama dalam bahasa berbeda (hreflang=\"en\").",
                    "",
                    "  <meta name=\"twitter:card\" content=\"summary_large_image\">",
                    "    Pelengkap Open Graph khusus untuk X/Twitter. Perhatikan:",
                    "    yang ini kembali memakai name=, bukan property=.",
                    "",
                    "Tidak satu pun dari daftar ini wajib. Yang wajib tetap tiga:",
                    "charset, viewport, dan title. Sisanya ditambahkan kalau",
                    "kebutuhannya benar-benar muncul — head panjang hasil menyalin",
                    "punya orang lain cuma menambah berkas yang diunduh percuma.",
                ]
            },
        ],
    },
    {
        "title": "21. Merakit Satu Halaman Utuh",
        "sections": [
            {
                "body": [
                    "Sekarang semuanya dipakai sekaligus dalam satu berkas:",
                    "kerangka dokumen, metadata, elemen semantik, heading, daftar,",
                    "tautan, gambar, tabel, dan formulir.",
                    "",
                    "Bacalah dari atas ke bawah dan cari bagian yang sudah kamu",
                    "kenali. Hampir semuanya sudah pernah muncul di materi",
                    "sebelumnya — yang baru cuma cara menyusunnya.",
                    "",
                    "Urutan menulis halaman yang membuat pekerjaan tidak berantakan:",
                    "  1. Kerangka: doctype, html lang, head, body.",
                    "  2. Isi head: charset, viewport, title, description.",
                    "  3. Kerangka besar body: header, nav, main, footer.",
                    "  4. Isi tiap bagian, dari atas ke bawah.",
                    "  5. Baru terakhir: rapikan, periksa, tambahkan CSS.",
                    "",
                    "Jangan mengatur tampilan dulu. Halaman yang strukturnya benar",
                    "gampang didandani; halaman cantik yang strukturnya kacau harus",
                    "dibongkar ulang.",
                ]
            },
            {
                "heading": "index.html — halaman warung kopi",
                "code": """<!doctype html>
<html lang="id">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Warung Kopi Pagi - Bandung</title>
  <meta name="description"
        content="Warung kopi kecil di Jalan Melati, Bandung. Buka setiap hari pukul 07.00.">
  <link rel="stylesheet" href="gaya.css">
</head>
<body>

  <header>
    <h1>Warung Kopi Pagi</h1>
    <p>Seduh manual, biji dari Gayo, sejak 2019.</p>
  </header>

  <nav>
    <ul>
      <li><a href="#menu">Menu</a></li>
      <li><a href="#jadwal">Jam buka</a></li>
      <li><a href="#pesan">Pesan</a></li>
    </ul>
  </nav>

  <main>

    <article id="menu">
      <h2>Menu</h2>

      <figure>
        <img src="gambar/tuang.jpg"
             alt="Barista menuang air melingkar ke atas corong V60"
             width="640" height="360">
        <figcaption>Setiap gelas diseduh saat dipesan.</figcaption>
      </figure>

      <table>
        <caption>Harga per gelas, Januari 2024</caption>
        <thead>
          <tr>
            <th scope="col">Menu</th>
            <th scope="col">Kecil</th>
            <th scope="col">Besar</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <th scope="row">Kopi tubruk</th>
            <td>12.000</td>
            <td>15.000</td>
          </tr>
          <tr>
            <th scope="row">Kopi susu</th>
            <td>18.000</td>
            <td>22.000</td>
          </tr>
        </tbody>
      </table>

      <h3>Cara kami menyeduh</h3>
      <ol>
        <li>Giling biji tepat sebelum diseduh.</li>
        <li>Panaskan air sampai <strong>92 derajat</strong>.</li>
        <li>Tuang melingkar, tunggu tiga menit.</li>
      </ol>
    </article>

    <article id="jadwal">
      <h2>Jam buka</h2>
      <dl>
        <dt>Senin - Jumat</dt>
        <dd>07.00 - 21.00</dd>

        <dt>Sabtu</dt>
        <dd>08.00 - 22.00</dd>

        <dt>Minggu</dt>
        <dd>Libur</dd>
      </dl>
    </article>

    <article id="pesan">
      <h2>Pesan lebih dulu</h2>
      <p>Isi formulir ini, pesananmu kami siapkan sebelum kamu sampai.</p>

      <form action="/pesan" method="post">
        <p>
          <label for="nama">Nama</label>
          <input type="text" id="nama" name="nama" required>
        </p>

        <p>
          <label for="telepon">Nomor telepon</label>
          <input type="tel" id="telepon" name="telepon"
                 placeholder="0812xxxxxxx" required>
        </p>

        <p>
          <label for="menu-pilihan">Menu</label>
          <select id="menu-pilihan" name="menu" required>
            <option value="">-- pilih menu --</option>
            <option value="tubruk">Kopi tubruk</option>
            <option value="susu">Kopi susu</option>
          </select>
        </p>

        <fieldset>
          <legend>Ukuran</legend>
          <input type="radio" id="kecil" name="ukuran" value="kecil" checked>
          <label for="kecil">Kecil</label>
          <input type="radio" id="besar" name="ukuran" value="besar">
          <label for="besar">Besar</label>
        </fieldset>

        <p>
          <label for="catatan">Catatan</label>
          <textarea id="catatan" name="catatan" rows="3" cols="40"></textarea>
        </p>

        <button type="submit">Kirim pesanan</button>
      </form>
    </article>

  </main>

  <aside>
    <h2>Sedang dicoba</h2>
    <p>Cold brew gula aren, tersedia terbatas tiap Jumat.</p>
  </aside>

  <footer>
    <p>Jalan Melati 7, Bandung.
       Surel: <a href="mailto:halo@kopipagi.test">halo@kopipagi.test</a></p>
    <p><small>&copy; 2024 Warung Kopi Pagi.</small></p>
  </footer>

</body>
</html>"""
            },
            {
                "body": [
                    "Keputusan yang diambil di halaman itu, dan alasannya:",
                    "",
                    "  Tiga <article>, bukan <section>.",
                    "    Menu, jam buka, dan formulir pesan masing-masing masih",
                    "    masuk akal kalau dipindah ke halaman sendiri.",
                    "",
                    "  id ada di <article>, bukan di <h2>.",
                    "    Tautan #menu melompat ke seluruh bagiannya, bukan cuma ke",
                    "    judulnya. Yang tergulir ke layar jadi bagian yang utuh.",
                    "",
                    "  Kolom pertama tabel memakai <th scope=\"row\">.",
                    "    \"Kopi tubruk\" adalah judul barisnya, bukan datanya.",
                    "",
                    "  Jam buka pakai <dl>, bukan tabel.",
                    "    Ini pasangan istilah dan keterangan, bukan data berkolom.",
                    "",
                    "  Cara menyeduh pakai <ol>, menu pakai <table>.",
                    "    Urutan langkah berarti; urutan menu tidak.",
                    "",
                    "  Setiap input punya label DAN name.",
                    "    label supaya bisa dipakai, name supaya datanya terkirim.",
                    "",
                    "  Cuma ada satu <h1>, dan heading-nya tidak melompat tingkat:",
                    "    h1 nama warung, h2 tiap bagian, h3 di dalam bagian.",
                ]
            },
            {
                "body": [
                    "Daftar periksa sebelum sebuah halaman disebut selesai:",
                    "",
                    "  [ ] <!doctype html> di baris pertama",
                    "  [ ] lang pada <html>",
                    "  [ ] <meta charset=\"utf-8\"> paling awal di head",
                    "  [ ] <meta name=\"viewport\"> ada",
                    "  [ ] <title> ada, unik, dan menjelaskan halamannya",
                    "  [ ] tepat satu <h1>",
                    "  [ ] heading berurutan, tidak melompat tingkat",
                    "  [ ] setiap <img> punya alt yang berarti (atau alt=\"\")",
                    "  [ ] setiap isian formulir punya <label> dan name",
                    "  [ ] semua id unik di halaman itu",
                    "  [ ] teks tautan bermakna, bukan \"klik di sini\"",
                    "  [ ] semua tag yang perlu ditutup sudah ditutup",
                    "  [ ] tidak ada <br><br> untuk membuat jarak",
                    "  [ ] tidak ada tabel yang dipakai untuk tata letak",
                    "  [ ] bagian-bagian besar diberi komentar penanda",
                    "  [ ] gambar di bawah lipatan punya loading=\"lazy\"",
                    "  [ ] setiap <script> memakai defer, atau ditaruh di akhir body",
                    "  [ ] setiap <iframe> punya title",
                    "  [ ] tombol yang isinya cuma ikon punya aria-label",
                    "  [ ] formulir berisi unggahan punya",
                    "      enctype=\"multipart/form-data\"",
                    "",
                    "Cara memeriksanya:",
                    "  - Di aplikasi ini: baca POHON STRUKTUR-nya. Kalau ada elemen",
                    "    yang menjorok lebih dalam dari dugaanmu, di situ ada tag",
                    "    yang lupa ditutup.",
                    "  - Di browser: klik kanan lalu Inspect. Yang ditampilkan",
                    "    devtools adalah DOM — pohon yang kamu kenal dari Materi 1",
                    "    — bukan isi berkasmu. Selisih antara keduanya persis",
                    "    daftar hal yang belum kamu sadari.",
                    "  - Validator resmi W3C memeriksa berkasmu dan menyebut baris",
                    "    yang bermasalah satu per satu.",
                    "",
                    "Masih ada satu materi lagi sesudah ini, dan bentuknya berbeda:",
                    "bukan menulis halaman sendiri, melainkan MEMBACA berkas .html",
                    "buatan orang lain — yang jarang serapi contoh-contoh di sini.",
                    "",
                    "Sesudah itu barulah CSS. HTML sudah memberi halamanmu struktur",
                    "dan makna; CSS yang memberinya jarak, warna, dan tata letak.",
                    "Halaman di atas belum cantik — tapi ia sudah bisa dibaca semua",
                    "orang, di semua alat, dan itu urutan yang benar.",
                ]
            },
        ],
    },
    {
        "title": "22. Canvas: Menggambar Langsung di Halaman",
        "sections": [
            {
                "body": [
                    "<canvas> adalah kotak kosong yang bisa digambar - bukan gambar siap pakai",
                    "seperti <img>, dan bukan kumpulan bentuk seperti SVG. Sebelum JavaScript",
                    "menyentuhnya, isinya cuma piksel kosong yang tidak terlihat sama sekali.",
                    "",
                    "Beda dari <img>:",
                    "  <img>     menampilkan BERKAS gambar yang sudah jadi (foto.jpg, ikon.svg)",
                    "  <canvas>  kanvas kosong; isinya digambar baris demi baris lewat JavaScript",
                    "            SETELAH halaman dimuat, bukan dibaca dari sebuah berkas",
                    "",
                    "Beda dari SVG - ini yang paling sering bikin bingung karena keduanya sama-sama",
                    "'digambar', tapi caranya beda total:",
                    "",
                    "  SVG     vector, per-BENTUK. Tiap lingkaran/garis adalah elemen sendiri di",
                    "          DOM, tetap bisa diklik, diberi event listener, diberi style CSS,",
                    "          dan diperbesar tanpa pecah karena dihitung ulang tiap kali dirender.",
                    "  canvas  raster, per-PIKSEL. Begitu sebuah lingkaran selesai digambar, ia",
                    "          jadi kumpulan titik warna biasa. Tidak ada 'elemen lingkaran' yang",
                    "          bisa dicari lagi - canvas cuma ingat WARNA tiap piksel, bukan APA",
                    "          yang pernah digambar di situ. Mau menggeser satu bentuk berarti",
                    "          menggambar ULANG semuanya dari awal.",
                    "",
                    "Konsekuensinya konkret: elemen SVG bisa kamu seleksi lewat document.querySelector",
                    "dan dikasih onclick seperti elemen HTML biasa. Sebuah 'lingkaran' yang digambar",
                    "di canvas tidak bisa - yang ada hanya satu elemen <canvas>, dan mengetahui",
                    "'apakah user mengklik lingkaran itu' berarti kamu sendiri yang harus menghitung",
                    "apakah koordinat klik berada di dalam area lingkaran.",
                ],
            },
            {
                "heading": "Kerangka minimal, dan atribut yang wajib diperhatikan",
                "body": [
                    "<canvas> butuh id supaya JavaScript bisa menemukannya nanti, dan dua atribut",
                    "angka: width dan height. Bagian menggambarnya sendiri - getContext('2d'),",
                    "lalu perintah seperti fillRect atau arc - dipelajari terpisah di materi",
                    "JavaScript 'Canvas API: Menggambar dengan JavaScript'. Materi ini cuma",
                    "membahas elemennya: cara menulisnya di HTML dan jebakan yang menunggu di sana,",
                    "sebelum satu baris JavaScript pun disentuh.",
                ],
                "code": """<canvas id="papan" width="400" height="300">
  Browser Anda tidak mendukung elemen canvas.
</canvas>""",
            },
            {
                "heading": "JEBAKAN: width/height ATRIBUT vs width/height CSS",
                "body": [
                    "Ini kesalahan yang nyaris semua orang lakukan sekali seumur hidup, dan hasilnya",
                    "membingungkan karena TIDAK ada error - gambarnya cuma kelihatan buram atau",
                    "gepeng, tanpa pesan apa pun di console.",
                    "",
                    "  width/height sebagai ATRIBUT  -> resolusi PIKSEL internal kanvas.",
                    "                                    Ini jumlah titik yang sungguhan ada.",
                    "  width/height lewat CSS         -> ukuran TAMPILAN di layar saja.",
                    "                                    Jumlah piksel internalnya TIDAK berubah.",
                    "",
                    "Kalau cuma CSS yang diatur (atributnya dibiarkan kosong sehingga jatuh ke",
                    "default 300x150), browser meregangkan 300x150 piksel itu supaya PAS dengan",
                    "ukuran CSS yang jauh lebih besar - persis seperti memperbesar foto kecil jadi",
                    "poster: pecah dan buram, bukan tambah tajam. Efeknya sama meski elemennya",
                    "sendiri kelihatan 'benar' ukurannya di halaman.",
                    "",
                    "Aturan praktis: atribut width/height MENENTUKAN berapa piksel yang benar-benar",
                    "ada untuk digambar. CSS width/height (kalau dipakai sama sekali) cuma boleh",
                    "dipakai untuk menyesuaikan tampilan ke tata letak responsif, dan idealnya",
                    "angkanya sama dengan atributnya supaya tidak terjadi regangan sama sekali.",
                ],
                "code": """<!-- BENAR: resolusi internal 800x600, tampil sesuai resolusinya -->
<canvas id="tajam" width="800" height="600"></canvas>

<!-- BURAM: resolusi internal cuma default 300x150, lalu diregangkan CSS -->
<canvas id="buram" style="width: 800px; height: 600px;"></canvas>

<!-- Kalau memang perlu skala layar tinggi (retina), atributnya SENGAJA dibuat -->
<!-- lebih besar dari ukuran tampil, lalu diciutkan lewat CSS - bukan sebaliknya: -->
<canvas id="tajam-retina" width="1600" height="1200"
        style="width: 800px; height: 600px;"></canvas>""",
            },
            {
                "heading": "Konten cadangan, dan kenapa itu BUKAN pengganti aria-label",
                "body": [
                    "Apa pun yang dituliskan di ANTARA <canvas> dan </canvas> disebut konten",
                    "cadangan (fallback). Aturannya sempit: browser HANYA menampilkannya kalau ia",
                    "sama sekali tidak mengenal elemen <canvas> - situasi yang nyaris punah",
                    "sekarang. Pembaca layar modern di browser modern TETAP melihat kanvasnya",
                    "sebagai kotak kosong tanpa makna, BUKAN membacakan teks cadangan itu, karena",
                    "browsernya mendukung canvas dengan sempurna - syarat 'tidak mendukung' itu",
                    "tidak terpenuhi.",
                    "",
                    "Jadi konten cadangan berguna untuk browser purba, tapi TIDAK cukup untuk",
                    "aksesibilitas. Cara yang benar-benar terbaca pembaca layar: role='img' dan",
                    "aria-label langsung di elemen <canvas>-nya sendiri.",
                ],
                "code": """<canvas id="grafik" width="400" height="200"
        role="img"
        aria-label="Grafik batang penjualan Januari sampai Juni, naik terus tiap bulan">
  Grafik penjualan tidak dapat ditampilkan di browser ini.
</canvas>""",
            },
            {
                "heading": "Kapan pakai canvas, kapan SVG, kapan cukup CSS",
                "body": [
                    "  canvas  banyak elemen yang berubah tiap frame, atau digambar piksel demi",
                    "          piksel (game, editor gambar, grafik data yang deras update-nya,",
                    "          efek partikel ratusan titik sekaligus)",
                    "  SVG     sedikit bentuk, perlu tetap tajam di ukuran berapa pun, dan/atau",
                    "          perlu diklik atau diberi event satu-satu (ikon, logo, diagram",
                    "          sederhana, peta dengan wilayah yang bisa disorot)",
                    "  CSS     kalau yang dibutuhkan cuma kotak, bulatan, gradien, atau bayangan -",
                    "          tidak perlu canvas maupun SVG sama sekali",
                    "",
                    "Alasannya balik ke sifat dasarnya: SVG mengingat APA yang digambar (masih",
                    "berupa elemen), canvas cuma mengingat WARNA tiap piksel. Ribuan bentuk yang",
                    "terus bergerak jadi berat kalau tiap satu adalah elemen DOM sendiri (SVG) -",
                    "di situ canvas menang. Sebaliknya, sedikit bentuk yang perlu tetap bisa diklik",
                    "satu-satu justru lebih gampang dan lebih murah lewat SVG.",
                ],
            },
        ],
    },
    {
        "title": "23. Membaca Berkas .html di Dunia Nyata",
        "sections": [
            {
                "body": [
                    "Sampai sini kamu selalu jadi PENULISNYA. Materi terakhir ini",
                    "melatih hal sebaliknya: membaca berkas .html buatan orang lain —",
                    "dan berkas orang lain hampir tidak pernah sepolos contoh di",
                    "kurikulum ini.",
                    "",
                    "Buka proyek web mana pun di GitHub, buka berkas .html-nya, dan",
                    "yang kemungkinan besar menyambutmu:",
                    "",
                    "  <sl-card>               tag yang tidak ada di HTML mana pun",
                    "  {{ produk.nama }}       kurung kurawal ganda di tengah teks",
                    "  {% for p in daftar %}   baris yang jelas-jelas perulangan",
                    "  v-if=\"kosong\"           atribut yang tak pernah disebut siapa pun",
                    "  class=\"btn btn-primary\" nama class yang melanggar materi Atribut",
                    "",
                    "Tidak satu pun dari itu membuat browser mengeluh. Materi ini",
                    "menjelaskan kenapa, supaya begitu kamu membuka berkas semacam itu",
                    "kamu tahu mana yang HTML, mana yang bukan, dan mana yang boleh",
                    "dilewati dulu tanpa rugi.",
                    "",
                    "",
                    "SATU ATURAN YANG MENJELASKAN HAMPIR SEMUANYA",
                    "",
                    "Browser tidak menyimpan daftar tag yang \"boleh\". Kalau ia bertemu",
                    "<blorb>, ia TIDAK error, tidak memberi peringatan, dan tidak",
                    "membuang isinya. Ia membuat elemen bernama blorb, lalu",
                    "memperlakukannya begini:",
                    "",
                    "  - tanpa makna apa pun; pembaca layar melewatinya begitu saja",
                    "  - tanpa gaya bawaan: tidak ada margin, tidak ada tebal, tidak",
                    "    ada apa-apa",
                    "  - dianggap elemen SEBARIS, persis seperti <span>",
                    "",
                    "  <blorb>Halo</blorb>   ->   blorb \"Halo\"",
                    "",
                    "Teksnya tetap tampil. Yang hilang cuma makna dan tampilan",
                    "bawaannya.",
                    "",
                    "Sisi buruknya sudah kamu kenal sejak materi pertama: salah ketik",
                    "<sectoin> atau <pargraph> tidak dilaporkan siapa pun. Halamannya",
                    "tetap muncul, cuma bagian itu diam-diam kehilangan seluruh sifat",
                    "bawaannya.",
                    "",
                    "Sisi baiknya jauh lebih besar, dan SELURUH ekosistem komponen",
                    "berdiri di atasnya: kalau tag asing tidak merusak apa pun, orang",
                    "boleh mengarang tag sendiri lalu menyuruh JavaScript",
                    "menghidupkannya belakangan.",
                    "",
                    "",
                    "CUSTOM ELEMENT: TAG KARANGAN YANG MEMANG DISENGAJA",
                    "",
                    "  <my-menu>  <ion-button>  <sl-card>  <fluent-badge>  <kartu-menu>",
                    "",
                    "Ada satu hal yang sama di semuanya: TANDA HUBUNG di nama tagnya.",
                    "Itu bukan selera penulisan, itu aturan. Nama custom element wajib",
                    "memuat minimal satu tanda hubung, dan sebagai imbalannya standar",
                    "HTML berjanji tidak akan pernah membuat elemen bawaan yang namanya",
                    "bertanda hubung.",
                    "",
                    "Buat kamu yang sedang MEMBACA kode, janji itu berharga sekali:",
                    "",
                    "  ada tanda hubung  ->  buatan manusia. Definisinya di berkas .js",
                    "  tidak ada         ->  elemen HTML asli, ada di dokumentasi resmi",
                    "",
                    "Itu satu-satunya pembeda yang tersedia saat membaca, dan ia selalu",
                    "benar. Yang menghidupkannya satu baris JavaScript di berkas lain:",
                    "",
                    "  customElements.define(\"kartu-menu\", KartuMenu);",
                    "",
                    "Sebelum baris itu jalan — atau kalau JS-nya gagal dimuat —",
                    "<kartu-menu> cuma tag asing biasa: isinya tampil polos tanpa",
                    "bentuk apa pun. Itu sebabnya halaman yang berat komponen kadang",
                    "berkedip sebentar sebelum jadi.",
                ],
            },
            {
                "heading": "Komponen: satu tag karangan, satu cetakan, dua lubang",
                "code": """<!doctype html>
<html lang="id">
<head>
  <meta charset="utf-8">
  <title>Kartu Menu</title>
</head>
<body>

  <h1>Menu hari ini</h1>

  <kartu-menu harga="15000">
    <span slot="nama">Kopi Tubruk</span>
    <p>Diseduh langsung di dalam gelas.</p>
  </kartu-menu>

  <template id="cetakan-kartu">
    <article class="kartu">
      <img src="gambar/kopi.jpg" alt="Segelas kopi tubruk">
      <h3 class="kartu__judul"><slot name="nama">Tanpa nama</slot></h3>
      <div class="kartu__isi"><slot></slot></div>
    </article>
  </template>

  <script src="kartu-menu.js"></script>
</body>
</html>""",
            },
            {
                "body": [
                    "Coba jalankan contoh di atas, lalu lihat pohonnya. Bagian yang",
                    "menarik:",
                    "",
                    "  body",
                    "    h1 \"Menu hari ini\"",
                    "    kartu-menu harga=\"15000\"",
                    "      span slot=\"nama\" \"Kopi Tubruk\"",
                    "      p \"Diseduh langsung di dalam gelas.\"",
                    "    template id=\"cetakan-kartu\"",
                    "      article class=\"kartu\"",
                    "        img alt=\"Segelas kopi tubruk\" src=\"gambar/kopi.jpg\"",
                    "        h3 class=\"kartu__judul\"",
                    "          slot name=\"nama\" \"Tanpa nama\"",
                    "",
                    "kartu-menu duduk di pohon persis seperti h1 di atasnya. Bagi",
                    "pembaca markup ia sama sekali bukan kasus istimewa — itu tadi, tag",
                    "asing tidak istimewa.",
                    "",
                    "",
                    "<template>: POTONGAN HTML YANG SENGAJA DIMATIKAN",
                    "",
                    "Isi <template> dibaca dan disimpan, tapi tidak digambar sedikit",
                    "pun di layar. Gambarnya TIDAK diunduh, videonya tidak dimuat,",
                    "<script> di dalamnya tidak dijalankan, dan CSS tidak menyentuhnya.",
                    "Ia baru hidup kalau JavaScript menyalinnya:",
                    "",
                    "  const cetakan = document.querySelector(\"#cetakan-kartu\");",
                    "  const salinan = cetakan.content.cloneNode(true);",
                    "",
                    "Satu cetakan, disalin sepuluh kali untuk sepuluh kartu. Itu alasan",
                    "elemen ini ada: menulis kerangkanya satu kali sebagai HTML jauh",
                    "lebih enak dibaca daripada merangkainya sebagai sambungan teks di",
                    "dalam JavaScript.",
                    "",
                    "Perhatikan bedanya dengan pohon di atas: di situ isi template",
                    "TETAP terlihat. Pohon menunjukkan apa yang TERTULIS di markup;",
                    "layar menunjukkan apa yang digambar. Untuk <template> keduanya",
                    "memang sengaja berbeda.",
                    "",
                    "",
                    "<slot>: LUBANG TEMPAT ISI DARI LUAR DIPASANG",
                    "",
                    "  di dalam cetakan :  <slot name=\"nama\">Tanpa nama</slot>",
                    "  di dalam pemakai :  <span slot=\"nama\">Kopi Tubruk</span>",
                    "",
                    "Nama yang sama menyambungkan keduanya: isi yang ditulis di dalam",
                    "<kartu-menu> dipindahkan ke lubang yang namanya cocok. <slot>",
                    "tanpa name adalah lubang bawaan — semua isi yang tidak menyebut",
                    "slot mendarat di situ, dan itu jatah <p> pada contoh tadi. Teks di",
                    "DALAM <slot> (\"Tanpa nama\") cuma cadangan: dipakai kalau",
                    "pemakainya tidak mengisi lubang itu.",
                    "",
                    "Shadow DOM, satu kalimat supaya kamu tidak kaget saat menemuinya:",
                    "sebuah elemen bisa diberi DOM kecil miliknya sendiri",
                    "(element.attachShadow) yang CSS halaman tidak bisa masuk ke",
                    "dalamnya dan tidak bocor keluar darinya. Di situlah salinan",
                    "cetakan tadi biasanya dipasang — dan itu juga jawaban kenapa",
                    "sesekali ada elemen yang \"tidak mempan\" diwarnai dari gaya.css.",
                    "",
                    "",
                    "BERKAS .html YANG SEBENARNYA CUMA CETAKAN",
                    "",
                    "Berkas .html di dalam folder templates/ atau views/ sering bukan",
                    "halaman, melainkan cetakan yang diproses program di SERVER lebih",
                    "dulu:",
                    "",
                    "  {% for item in menu %}",
                    "    <li class=\"kartu kartu--{{ item.jenis }}\">",
                    "      <h3 class=\"kartu__judul\">{{ item.nama }}</h3>",
                    "    </li>",
                    "  {% endfor %}",
                    "",
                    "  {{ ... }}   menaruh SEBUAH NILAI di tempat itu",
                    "  {% ... %}   menjalankan LOGIKA: perulangan, percabangan,",
                    "              menyambung berkas lain",
                    "",
                    "Bentuk ini dipakai Jinja (Python), Django, Nunjucks (Node), dan",
                    "Twig (PHP) dengan tulisan yang praktis sama. Handlebars dan",
                    "Mustache memakai kurung yang sama tapi menulis logikanya {{#each",
                    "daftar}} ... {{/each}}.",
                    "",
                    "Yang penting kamu sadari: browser TIDAK PERNAH melihat satu pun",
                    "kurung itu. Yang dikirim server sudah HTML biasa, hasil isian",
                    "cetakan tadi. Akibat praktisnya, berkas seperti ini tidak bisa",
                    "dibuka langsung dengan klik dua kali — yang tampil justru tulisan",
                    "{{ item.nama }} apa adanya, karena di situ tidak ada yang",
                    "mengolahnya.",
                ],
            },
            {
                "body": [
                    "KERANGKA KERJA DI SISI BROWSER",
                    "",
                    "Di sini berkasnya memang HTML sungguhan, tapi atribut-atributnya",
                    "bukan. Yang membaca atribut itu pustaka JavaScript yang ikut",
                    "dimuat halaman; browser sendiri menganggapnya atribut asing tanpa",
                    "arti — sama seperti tag asing tadi.",
                    "",
                    "  Vue",
                    "    <li v-for=\"item in menu\" :key=\"item.id\" @click=\"pilih(item)\">",
                    "      {{ item.nama }}",
                    "    </li>",
                    "    <p v-if=\"menu.length === 0\">Menu belum dimuat.</p>",
                    "",
                    "  Alpine",
                    "    <div x-data=\"{ buka: false }\" class=\"flex items-center gap-2\">",
                    "      <button @click=\"buka = !buka\">Menu</button>",
                    "      <ul x-show=\"buka\">...</ul>",
                    "    </div>",
                    "",
                    "  Angular",
                    "    <li *ngFor=\"let item of menu\" [class.aktif]=\"item.dipilih\"",
                    "        (click)=\"pilih(item)\">{{ item.nama }}</li>",
                    "",
                    "  htmx",
                    "    <button class=\"btn btn-primary js-muat\"",
                    "            hx-get=\"/menu\" hx-target=\"#daftar\">Muat menu</button>",
                    "    <div id=\"daftar\"></div>",
                    "",
                    "Kamu tidak perlu hafal satu pun nama di atas. Cukup kenali",
                    "BENTUKNYA, karena bentuk-bentuk ini tidak pernah ada di HTML asli:",
                    "",
                    "  huruf-strip   v-for  x-show  hx-get  ng-model",
                    "                awalan khas pustakanya",
                    "  :nama         :key  :href",
                    "                nilainya DIHITUNG, bukan teks biasa",
                    "  @nama         @click  @submit",
                    "                penanganan kejadian",
                    "  [nama] (nama) [class.aktif]  (click)",
                    "                cara Angular menulis dua hal terakhir itu",
                    "  *nama         *ngFor  *ngIf",
                    "                Angular, mengubah struktur halaman",
                    "",
                    "Aturan bacanya: begitu sebuah atribut diawali salah satu tanda di",
                    "atas, berhenti menganggapnya HTML. Itu perintah untuk pustaka, dan",
                    "isinya hampir selalu potongan JavaScript, bukan teks biasa.",
                    "",
                    "",
                    "JSX — DAN INI BUKAN BERKAS .html LAGI",
                    "",
                    "React dan sejenisnya menulis markup di DALAM berkas JavaScript:",
                    "Kartu.jsx atau Kartu.tsx. Bentuknya mirip HTML, tapi yang",
                    "mengolahnya alat build, bukan browser, jadi aturannya boleh",
                    "berbeda:",
                    "",
                    "  export function Kartu({ nama }) {",
                    "    return (",
                    "      <article className=\"kartu\">",
                    "        <h3>{nama}</h3>",
                    "        <label htmlFor=\"jumlah\">Jumlah</label>",
                    "        <input id=\"jumlah\" defaultValue={1} />",
                    "      </article>",
                    "    );",
                    "  }",
                    "",
                    "  <Kartu nama=\"Kopi Tubruk\" harga={15000} />",
                    "",
                    "Yang berubah dari HTML yang kamu kenal:",
                    "",
                    "  className   pengganti class; \"class\" sudah jadi kata kunci",
                    "              di JavaScript",
                    "  htmlFor     pengganti for, dengan alasan yang sama",
                    "  {isi}       kurung kurawal TUNGGAL berarti \"ambil nilainya",
                    "              dari JavaScript\"",
                    "  <Kartu />   HURUF BESAR di depan berarti komponen buatan",
                    "              sendiri; huruf kecil (<article>, <input>) tetap",
                    "              elemen HTML asli",
                    "  <input />   semua tag wajib ditutup, termasuk yang di HTML",
                    "              tidak perlu",
                    "",
                    "Jadi pembeda \"asli atau karangan\" ada dua, tergantung tempatnya:",
                    "tanda hubung kalau kamu di berkas .html, huruf besar kalau kamu di",
                    "berkas .jsx.",
                ],
            },
            {
                "body": [
                    "KENAPA NAMA CLASS DI KODE NYATA TERLIHAT MELANGGAR ATURAN",
                    "",
                    "Materi \"Atribut: class, id, dan yang Sering Dipakai\" menyuruh",
                    "memberi nama menurut ARTI, bukan menurut tampilan. Lalu potongan",
                    "Alpine di atas menulis class=\"flex items-center gap-2\" — persis",
                    "yang dilarang. Mana yang benar?",
                    "",
                    "Keduanya. Ada beberapa KESEPAKATAN penamaan yang dipakai luas,",
                    "masing-masing menyelesaikan masalah berbeda. Tiap proyek memilih",
                    "satu lalu memakainya konsisten, dan empat ini pasti kamu temui:",
                    "",
                    "BEM       <article class=\"kartu kartu--sorot\">",
                    "          <h3 class=\"kartu__judul\">",
                    "",
                    "          blok = kartu, __elemen = bagian di dalam blok itu,",
                    "          --pengubah = varian. Namanya datar semua dan tetap",
                    "          menyebut ARTI, jadi CSS-nya tidak perlu pemilih",
                    "          bersarang panjang yang rusak begitu HTML-nya digeser.",
                    "          Contoh komponen di materi ini memakai gaya ini.",
                    "",
                    "UTILITAS  <div class=\"flex items-center gap-2 p-4\">   (Tailwind)",
                    "",
                    "          Satu class = satu properti CSS. Ini memang kebalikan",
                    "          nasihat tadi, dan itu disengaja: menukar \"cari nama",
                    "          yang tepat\" dengan \"tidak usah menamai apa pun\".",
                    "          Harganya, HTML jadi berisik dan mengubah tampilan",
                    "          berarti menyunting HTML, bukan CSS.",
                    "",
                    "KERANGKA  <button class=\"btn btn-primary\">   (Bootstrap)",
                    "",
                    "          Nama ini bukan karangan proyeknya. Jangan cari",
                    "          btn-primary di CSS mereka — carilah di dokumentasi",
                    "          kerangka kerjanya.",
                    "",
                    "PEGANGAN  <button class=\"btn btn-primary js-muat\" data-id=\"7\">",
                    "",
                    "          js-muat tidak punya satu pun aturan CSS. Ia cuma",
                    "          pegangan untuk JavaScript, sengaja dipisah supaya orang",
                    "          yang merapikan tampilan bisa mengganti btn-primary",
                    "          tanpa diam-diam mematikan tombolnya. Sebagian tim",
                    "          memakai data-* untuk maksud yang sama.",
                    "",
                    "Saat membaca: kenali polanya, lalu ikuti gaya yang sudah dipakai",
                    "berkas itu. Yang benar-benar berantakan bukan salah satu gaya di",
                    "atas, melainkan tiga gaya dipakai sekaligus dalam satu proyek.",
                    "",
                    "",
                    "CARA MEMBACANYA TANPA TERSESAT",
                    "",
                    "  1. Cari kerangkanya dulu: doctype, html, head, body, lalu",
                    "     header, nav, main, footer. Bagian itu hampir selalu HTML",
                    "     biasa, dan begitu ketemu kamu sudah punya peta berkasnya.",
                    "  2. Lompati apa pun yang jelas bukan HTML. Baris {% ... %},",
                    "     atribut berawalan aneh, dan isi <script> boleh dilewati",
                    "     dulu — yang sedang kamu cari adalah BENTUK halamannya.",
                    "  3. Tandai nama tag bertanda hubung. Itu komponen; definisinya",
                    "     ada di berkas .js lain, biasanya bernama sama dengan tagnya.",
                    "  4. Pastikan mana yang benar-benar sampai ke browser. Ctrl+U",
                    "     (View Source) menunjukkan HTML yang DIKIRIM server — di situ",
                    "     {{ }} sudah lenyap berganti nilai. Klik kanan lalu Inspect",
                    "     menunjukkan pohon SEKARANG, sesudah JavaScript menambah dan",
                    "     menyusun ulang isinya. Kalau keduanya berbeda jauh, halaman",
                    "     itu memang dibangun di browser.",
                    "  5. Atribut yang tidak kamu kenali, cari namanya apa adanya di",
                    "     internet. Nama seperti hx-swap atau x-show hampir mustahil",
                    "     salah ketemu: cuma satu pustaka di dunia yang memakainya.",
                    "",
                    "",
                    "PENUTUP",
                    "",
                    "Kurikulum HTML berhenti di sini. Kamu bisa menyusun halaman utuh",
                    "dari nol, memberinya makna yang benar, membuat formulir yang bisa",
                    "dipakai orang, dan sekarang membaca berkas orang lain tanpa panik.",
                    "",
                    "Dan itu intinya: hampir semua yang tampak aneh di kode nyata",
                    "ternyata cuma LAPISAN di atas hal yang sama. Cetakan server",
                    "menghasilkan HTML. Kerangka kerja browser menghasilkan HTML.",
                    "Komponen menghasilkan HTML. JSX menghasilkan HTML. Yang berbeda",
                    "hanya siapa yang menuliskannya dan kapan — elemen, atribut, dan",
                    "pohon yang kamu pelajari sejak materi pertama tetap yang",
                    "menentukan hasil akhirnya.",
                    "",
                    "Berikutnya CSS, dan sekarang kamu punya satu alasan tambahan untuk",
                    "mempelajarinya: sebagian besar keanehan di atas ada demi mengatur",
                    "tampilan.",
                ],
            },
        ],
    },
]
