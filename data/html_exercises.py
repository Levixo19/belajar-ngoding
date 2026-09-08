HTML_EXERCISES = [
    {
        "title": "Latihan 1: Kerangka Halaman Pertama",
        "difficulty": "Mudah",
        "question": [
            "Buat satu halaman HTML lengkap dengan isi persis seperti ini:",
            "",
            "  - baris doctype HTML5",
            "  - elemen html dengan atribut lang bernilai id",
            "  - di dalam head: meta dengan charset bernilai utf-8,",
            "    lalu title bertuliskan Profilku",
            "  - di dalam body: satu h1 bertuliskan Andi Pratama,",
            "    lalu satu p bertuliskan Saya sedang belajar HTML.",
            "",
            "HTML tidak dijalankan. Yang dinilai adalah POHON struktur berkasmu,",
            "hasil pembacaan struktur.py. Cocokkan sampai ke tanda bacanya.",
            "",
            "Keluaran yang diharapkan:",
            "",
            "<!doctype html>",
            "html lang=\"id\"",
            "  head",
            "    meta charset=\"utf-8\"",
            "    title \"Profilku\"",
            "  body",
            "    h1 \"Andi Pratama\"",
            "    p \"Saya sedang belajar HTML.\"",
        ],
        "hints": [
            "Baris pertama bukan tag biasa: bentuknya <!DOCTYPE html>. "
            "Di pohon ia dicetak huruf kecil semua, itu normal.",
            "head dan body sama-sama anak langsung dari html, "
            "jadi keduanya menjorok satu tingkat di pohon.",
            "meta termasuk elemen kosong: tidak punya tag penutup. "
            "Menulis </meta> justru dilaporkan sebagai kesalahan.",
        ],
        "solution": """<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="utf-8">
  <title>Profilku</title>
</head>
<body>
  <h1>Andi Pratama</h1>
  <p>Saya sedang belajar HTML.</p>
</body>
</html>""",
    },
    {
        "title": "Latihan 2: Judul Bertingkat",
        "difficulty": "Mudah",
        "question": [
            "Buat halaman lengkap berbahasa id dengan title Tentang Saya.",
            "Isi body berurutan:",
            "",
            "  - h1 bertuliskan Tentang Saya",
            "  - p bertuliskan Halo, namaku Sari.",
            "  - h2 bertuliskan Hobi",
            "  - p bertuliskan Membaca buku dan bersepeda.",
            "  - h2 bertuliskan Cita-cita",
            "  - p bertuliskan Menjadi pembuat aplikasi.",
            "",
            "h1 dipakai sekali saja sebagai judul halaman; h2 untuk sub-bagian.",
            "Urutan angkanya menandakan tingkat, bukan ukuran huruf.",
            "",
            "Keluaran yang diharapkan:",
            "",
            "<!doctype html>",
            "html lang=\"id\"",
            "  head",
            "    meta charset=\"utf-8\"",
            "    title \"Tentang Saya\"",
            "  body",
            "    h1 \"Tentang Saya\"",
            "    p \"Halo, namaku Sari.\"",
            "    h2 \"Hobi\"",
            "    p \"Membaca buku dan bersepeda.\"",
            "    h2 \"Cita-cita\"",
            "    p \"Menjadi pembuat aplikasi.\"",
        ],
        "hints": [
            "Kerangka doctype, html, head, dan body sama persis dengan Latihan 1. "
            "Yang berubah hanya isi title dan isi body.",
            "Teks Tentang Saya muncul dua kali: sekali di title (nama tab browser), "
            "sekali di h1 (judul yang terbaca di halaman). Keduanya memang perlu.",
            "Semua h1, h2, dan p di sini bersaudara — sama-sama anak langsung body, "
            "jadi indentasinya di pohon sama rata.",
        ],
        "solution": """<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="utf-8">
  <title>Tentang Saya</title>
</head>
<body>
  <h1>Tentang Saya</h1>
  <p>Halo, namaku Sari.</p>
  <h2>Hobi</h2>
  <p>Membaca buku dan bersepeda.</p>
  <h2>Cita-cita</h2>
  <p>Menjadi pembuat aplikasi.</p>
</body>
</html>""",
    },
    {
        "title": "Latihan 3: Dua Macam Daftar",
        "difficulty": "Mudah",
        "question": [
            "Buat halaman lengkap berbahasa id dengan title Resep Nasi Goreng.",
            "Isi body berurutan:",
            "",
            "  - h1 bertuliskan Resep Nasi Goreng",
            "  - h2 bertuliskan Bahan",
            "  - ul berisi tiga li: Nasi putih, Bawang merah, Kecap manis",
            "  - h2 bertuliskan Langkah",
            "  - ol berisi tiga li: Tumis bawang, Masukkan nasi, Tambahkan kecap",
            "",
            "ul untuk hal yang urutannya tidak penting, ol untuk yang berurutan.",
            "Nomor 1, 2, 3 pada ol dibuat browser sendiri — jangan diketik.",
            "",
            "Keluaran yang diharapkan:",
            "",
            "<!doctype html>",
            "html lang=\"id\"",
            "  head",
            "    meta charset=\"utf-8\"",
            "    title \"Resep Nasi Goreng\"",
            "  body",
            "    h1 \"Resep Nasi Goreng\"",
            "    h2 \"Bahan\"",
            "    ul",
            "      li \"Nasi putih\"",
            "      li \"Bawang merah\"",
            "      li \"Kecap manis\"",
            "    h2 \"Langkah\"",
            "    ol",
            "      li \"Tumis bawang\"",
            "      li \"Masukkan nasi\"",
            "      li \"Tambahkan kecap\"",
        ],
        "hints": [
            "li tidak berdiri sendiri: ia selalu berada di dalam ul atau ol. "
            "Di pohon itu terlihat dari indentasinya yang lebih dalam.",
            "Baris ul dan ol di pohon tidak punya teks dalam kutip, "
            "karena semua tulisannya ada di dalam li masing-masing.",
            "Kalau salah satu li muncul di tingkat yang salah, "
            "biasanya ada tag penutup </li> yang terlewat.",
        ],
        "solution": """<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="utf-8">
  <title>Resep Nasi Goreng</title>
</head>
<body>
  <h1>Resep Nasi Goreng</h1>
  <h2>Bahan</h2>
  <ul>
    <li>Nasi putih</li>
    <li>Bawang merah</li>
    <li>Kecap manis</li>
  </ul>
  <h2>Langkah</h2>
  <ol>
    <li>Tumis bawang</li>
    <li>Masukkan nasi</li>
    <li>Tambahkan kecap</li>
  </ol>
</body>
</html>""",
    },
    {
        "title": "Latihan 4: Gambar dan Tautan",
        "difficulty": "Mudah",
        "question": [
            "Buat halaman lengkap berbahasa id dengan title Galeri Sari.",
            "Isi body berurutan:",
            "",
            "  - h1 bertuliskan Galeri Sari",
            "  - img dengan src bernilai foto-sari.jpg, alt bernilai Foto Sari,",
            "    dan width bernilai 200",
            "  - p bertuliskan Foto ini diambil di Bandung.",
            "  - a dengan href bernilai tentang.html, bertuliskan Tentang Saya",
            "  - a dengan href bernilai kontak.html, bertuliskan Kontak",
            "",
            "Atribut di pohon selalu dicetak urut abjad, jadi urutan penulisanmu",
            "di berkas tidak berpengaruh. src boleh ditulis sebelum alt.",
            "",
            "Keluaran yang diharapkan:",
            "",
            "<!doctype html>",
            "html lang=\"id\"",
            "  head",
            "    meta charset=\"utf-8\"",
            "    title \"Galeri Sari\"",
            "  body",
            "    h1 \"Galeri Sari\"",
            "    img alt=\"Foto Sari\" src=\"foto-sari.jpg\" width=\"200\"",
            "    p \"Foto ini diambil di Bandung.\"",
            "    a href=\"tentang.html\" \"Tentang Saya\"",
            "    a href=\"kontak.html\" \"Kontak\"",
        ],
        "hints": [
            "img adalah elemen kosong seperti meta: tidak ada </img>. "
            "Isinya seluruhnya ditentukan atribut.",
            "alt adalah teks pengganti kalau gambarnya gagal dimuat, dan satu-satunya "
            "yang dibacakan pembaca layar. Kosongkan alt dan gambarnya jadi tak berarti.",
            "a punya tag penutup karena ia membungkus teks yang bisa diklik: "
            "<a href=\"...\">teks</a>. Nilai href di sini nama berkas biasa, bukan alamat penuh.",
        ],
        "solution": """<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="utf-8">
  <title>Galeri Sari</title>
</head>
<body>
  <h1>Galeri Sari</h1>
  <img alt="Foto Sari" src="foto-sari.jpg" width="200">
  <p>Foto ini diambil di Bandung.</p>
  <a href="tentang.html">Tentang Saya</a>
  <a href="kontak.html">Kontak</a>
</body>
</html>""",
    },
    {
        "title": "Latihan 5: Penekanan di Dalam Paragraf",
        "difficulty": "Menengah",
        "question": [
            "Buat halaman lengkap berbahasa id dengan title Pengumuman Kelas.",
            "Isi body berurutan:",
            "",
            "  - h1 bertuliskan Pengumuman Kelas",
            "  - p berisi teks Kelas dimulai, lalu strong bertuliskan pukul 08.00,",
            "    lalu teks tepat. (dengan titik) — semuanya dalam SATU p",
            "  - p yang seluruh isinya satu em bertuliskan Bawa laptop masing-masing.",
            "  - p berisi teks Ruang A, lalu br, lalu teks Lantai 2",
            "",
            "Perhatikan baik-baik cara pohon menampilkan p yang pertama: teks milik p",
            "sendiri digabung jadi satu kutipan, sedangkan strong turun jadi anaknya.",
            "Begitu juga p ketiga — br tidak memotong teksnya di pohon, ia cuma muncul",
            "sebagai anak. Di browser br tetap memindahkan Lantai 2 ke baris baru.",
            "",
            "Keluaran yang diharapkan:",
            "",
            "<!doctype html>",
            "html lang=\"id\"",
            "  head",
            "    meta charset=\"utf-8\"",
            "    title \"Pengumuman Kelas\"",
            "  body",
            "    h1 \"Pengumuman Kelas\"",
            "    p \"Kelas dimulai tepat.\"",
            "      strong \"pukul 08.00\"",
            "    p",
            "      em \"Bawa laptop masing-masing.\"",
            "    p \"Ruang A Lantai 2\"",
            "      br",
        ],
        "hints": [
            "Tiga p ini ditulis biasa saja; yang berbeda cuma isinya. "
            "Jangan menambah div atau span apa pun.",
            "p yang kedua tidak punya teks sendiri sama sekali — seluruh tulisannya "
            "milik em. Itu sebabnya baris p-nya di pohon berdiri tanpa kutipan.",
            "br elemen kosong: cukup <br> di tengah teks, tanpa penutup. "
            "Jangan menulis <br></br>.",
        ],
        "solution": """<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="utf-8">
  <title>Pengumuman Kelas</title>
</head>
<body>
  <h1>Pengumuman Kelas</h1>
  <p>Kelas dimulai <strong>pukul 08.00</strong> tepat.</p>
  <p><em>Bawa laptop masing-masing.</em></p>
  <p>Ruang A<br>Lantai 2</p>
</body>
</html>""",
    },
    {
        "title": "Latihan 6: Daftar Bersarang dan Daftar Istilah",
        "difficulty": "Menengah",
        "question": [
            "Buat halaman lengkap berbahasa id dengan title Menu Warung.",
            "Isi body berurutan:",
            "",
            "  - h1 bertuliskan Menu Warung",
            "  - ul berisi dua li:",
            "      li pertama bertuliskan Minuman, dan DI DALAMNYA ada ul lagi",
            "      berisi dua li: Teh dan Kopi",
            "      li kedua bertuliskan Makanan",
            "  - dl berisi empat elemen berselang-seling:",
            "      dt HTML, dd Menyusun struktur halaman.,",
            "      dt CSS, dd Mengatur tampilan halaman.",
            "",
            "Daftar bersarang dibuat dengan menaruh ul di DALAM li, bukan di antara",
            "dua li. Kalau ul-nya jadi saudara li, pohonnya langsung berbeda.",
            "",
            "Keluaran yang diharapkan:",
            "",
            "<!doctype html>",
            "html lang=\"id\"",
            "  head",
            "    meta charset=\"utf-8\"",
            "    title \"Menu Warung\"",
            "  body",
            "    h1 \"Menu Warung\"",
            "    ul",
            "      li \"Minuman\"",
            "        ul",
            "          li \"Teh\"",
            "          li \"Kopi\"",
            "      li \"Makanan\"",
            "    dl",
            "      dt \"HTML\"",
            "      dd \"Menyusun struktur halaman.\"",
            "      dt \"CSS\"",
            "      dd \"Mengatur tampilan halaman.\"",
        ],
        "hints": [
            "Perhatikan indentasi di pohon: ul yang kedua lebih dalam satu tingkat "
            "daripada li Minuman. Artinya ia anak li itu, bukan saudaranya.",
            "Tulis teks Minuman dulu, baru ul bersarangnya, baru </li>. "
            "Menutup </li> terlalu cepat membuat ul-nya keluar dari li.",
            "dt itu istilah, dd itu penjelasannya. Keduanya anak langsung dl "
            "dan berdiri sejajar — dd tidak berada di dalam dt.",
        ],
        "solution": """<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="utf-8">
  <title>Menu Warung</title>
</head>
<body>
  <h1>Menu Warung</h1>
  <ul>
    <li>Minuman
      <ul>
        <li>Teh</li>
        <li>Kopi</li>
      </ul>
    </li>
    <li>Makanan</li>
  </ul>
  <dl>
    <dt>HTML</dt>
    <dd>Menyusun struktur halaman.</dd>
    <dt>CSS</dt>
    <dd>Mengatur tampilan halaman.</dd>
  </dl>
</body>
</html>""",
    },
    {
        "title": "Latihan 7: Tabel Nilai",
        "difficulty": "Menengah",
        "question": [
            "Buat halaman lengkap berbahasa id dengan title Nilai Ujian.",
            "Isi body:",
            "",
            "  - h1 bertuliskan Nilai Ujian",
            "  - table berisi, berurutan:",
            "      caption bertuliskan Nilai Kelas 7A",
            "      thead berisi satu tr dengan dua th: Nama dan Nilai",
            "      tbody berisi dua tr:",
            "        tr pertama dua td: Sari dan 90",
            "        tr kedua dua td: Budi dan 75",
            "",
            "th untuk sel judul, td untuk sel isi. caption ditulis PERTAMA di dalam",
            "table, meskipun browser menampilkannya di atas tabel.",
            "",
            "Keluaran yang diharapkan:",
            "",
            "<!doctype html>",
            "html lang=\"id\"",
            "  head",
            "    meta charset=\"utf-8\"",
            "    title \"Nilai Ujian\"",
            "  body",
            "    h1 \"Nilai Ujian\"",
            "    table",
            "      caption \"Nilai Kelas 7A\"",
            "      thead",
            "        tr",
            "          th \"Nama\"",
            "          th \"Nilai\"",
            "      tbody",
            "        tr",
            "          td \"Sari\"",
            "          td \"90\"",
            "        tr",
            "          td \"Budi\"",
            "          td \"75\"",
        ],
        "hints": [
            "Tabel punya empat tingkat sarang: table, lalu thead atau tbody, "
            "lalu tr, lalu th atau td. Hitung indentasinya di pohon sebelum menulis.",
            "Satu tr adalah satu baris; sel-sel di dalamnya adalah kolomnya. "
            "Dua th berarti tabel ini dua kolom, jadi tiap tr isinya dua sel.",
            "Angka 90 dan 75 tetap ditulis sebagai teks biasa di dalam td. "
            "Tidak ada tipe data di HTML.",
        ],
        "solution": """<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="utf-8">
  <title>Nilai Ujian</title>
</head>
<body>
  <h1>Nilai Ujian</h1>
  <table>
    <caption>Nilai Kelas 7A</caption>
    <thead>
      <tr>
        <th>Nama</th>
        <th>Nilai</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Sari</td>
        <td>90</td>
      </tr>
      <tr>
        <td>Budi</td>
        <td>75</td>
      </tr>
    </tbody>
  </table>
</body>
</html>""",
    },
    {
        "title": "Latihan 8: Formulir Hubungi Kami",
        "difficulty": "Menengah",
        "question": [
            "Buat halaman lengkap berbahasa id dengan title Hubungi Kami.",
            "Isi body:",
            "",
            "  - h1 bertuliskan Hubungi Kami",
            "  - form dengan action bernilai kirim.php dan method bernilai post,",
            "    berisi berurutan:",
            "      label dengan for bernilai nama, bertuliskan Nama",
            "      input dengan id nama, name nama, type text, dan atribut required",
            "      label dengan for bernilai pesan, bertuliskan Pesan",
            "      textarea dengan id pesan, name pesan, rows 4, dan isi KOSONG",
            "      button dengan type submit, bertuliskan Kirim",
            "",
            "required ditulis tanpa nilai. Di pohon ia muncul sebagai kata sendirian,",
            "tanpa tanda sama dengan dan tanpa kutip.",
            "",
            "Keluaran yang diharapkan:",
            "",
            "<!doctype html>",
            "html lang=\"id\"",
            "  head",
            "    meta charset=\"utf-8\"",
            "    title \"Hubungi Kami\"",
            "  body",
            "    h1 \"Hubungi Kami\"",
            "    form action=\"kirim.php\" method=\"post\"",
            "      label for=\"nama\" \"Nama\"",
            "      input id=\"nama\" name=\"nama\" required type=\"text\"",
            "      label for=\"pesan\" \"Pesan\"",
            "      textarea id=\"pesan\" name=\"pesan\" rows=\"4\"",
            "      button type=\"submit\" \"Kirim\"",
        ],
        "hints": [
            "Nilai for pada label harus sama persis dengan id pada input-nya. "
            "Itulah yang membuat mengklik tulisan Nama memindahkan kursor ke kotaknya.",
            "input elemen kosong (tak ada </input>), tapi textarea punya tag penutup. "
            "Karena isinya kosong, tulis <textarea ...></textarea> menempel.",
            "id dipakai label untuk menunjuk, name dipakai server untuk mengenali. "
            "Keduanya perlu, walaupun nilainya kebetulan sama.",
        ],
        "solution": """<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="utf-8">
  <title>Hubungi Kami</title>
</head>
<body>
  <h1>Hubungi Kami</h1>
  <form action="kirim.php" method="post">
    <label for="nama">Nama</label>
    <input id="nama" name="nama" required type="text">
    <label for="pesan">Pesan</label>
    <textarea id="pesan" name="pesan" rows="4"></textarea>
    <button type="submit">Kirim</button>
  </form>
</body>
</html>""",
    },
    {
        "title": "Latihan 9: Struktur Semantik Halaman",
        "difficulty": "Menengah",
        "question": [
            "Buat halaman lengkap berbahasa id dengan title Toko Kopi.",
            "Isi body memakai elemen semantik, berurutan:",
            "",
            "  - header berisi:",
            "      h1 bertuliskan Toko Kopi",
            "      nav berisi ul dengan dua li, masing-masing berisi satu a:",
            "        a href index.html bertuliskan Beranda",
            "        a href menu.html bertuliskan Menu",
            "  - main berisi section, dan section itu berisi:",
            "      h2 bertuliskan Kopi Hari Ini",
            "      p bertuliskan Arabika Gayo, diseduh manual.",
            "  - footer berisi p bertuliskan Buka setiap hari pukul 09.00.",
            "",
            "header, nav, main, section, dan footer bekerja persis seperti div —",
            "bedanya namanya memberi tahu APA isinya, bukan sekadar membungkus.",
            "Menu navigasi ditulis sebagai daftar karena memang daftar tautan.",
            "",
            "Keluaran yang diharapkan:",
            "",
            "<!doctype html>",
            "html lang=\"id\"",
            "  head",
            "    meta charset=\"utf-8\"",
            "    title \"Toko Kopi\"",
            "  body",
            "    header",
            "      h1 \"Toko Kopi\"",
            "      nav",
            "        ul",
            "          li",
            "            a href=\"index.html\" \"Beranda\"",
            "          li",
            "            a href=\"menu.html\" \"Menu\"",
            "    main",
            "      section",
            "        h2 \"Kopi Hari Ini\"",
            "        p \"Arabika Gayo, diseduh manual.\"",
            "    footer",
            "      p \"Buka setiap hari pukul 09.00.\"",
        ],
        "hints": [
            "Baris li di pohon berdiri tanpa kutipan teks. Artinya li tidak punya teks "
            "sendiri: seluruh tulisannya berada di dalam a yang jadi anaknya.",
            "nav berada DI DALAM header, sejajar dengan h1 — bukan setelah </header>. "
            "Bandingkan indentasinya dengan main dan footer.",
            "Satu halaman hanya punya satu main, dan h1 di dalam header sudah cukup "
            "jadi judul utamanya. Section di bawahnya mulai dari h2.",
        ],
        "solution": """<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="utf-8">
  <title>Toko Kopi</title>
</head>
<body>
  <header>
    <h1>Toko Kopi</h1>
    <nav>
      <ul>
        <li><a href="index.html">Beranda</a></li>
        <li><a href="menu.html">Menu</a></li>
      </ul>
    </nav>
  </header>
  <main>
    <section>
      <h2>Kopi Hari Ini</h2>
      <p>Arabika Gayo, diseduh manual.</p>
    </section>
  </main>
  <footer>
    <p>Buka setiap hari pukul 09.00.</p>
  </footer>
</body>
</html>""",
    },
    {
        "title": "Latihan 10: Halaman Artikel Lengkap",
        "difficulty": "Lanjut",
        "question": [
            "Buat halaman lengkap berbahasa id. Isi head, berurutan:",
            "",
            "  - meta charset utf-8",
            "  - meta dengan name viewport dan content bernilai",
            "    width=device-width, initial-scale=1",
            "  - link dengan rel stylesheet dan href gaya.css",
            "  - title bertuliskan Catatan Belajar",
            "",
            "Isi body, berurutan:",
            "",
            "  - header berisi h1 Catatan Belajar dan p Ditulis oleh Sari.",
            "  - main berisi article dengan id bernilai hari-pertama, isinya:",
            "      h2 bertuliskan Hari Pertama",
            "      p bertuliskan Hari ini aku menulis halaman HTML pertamaku.",
            "      figure berisi img (src layar.png, alt Tangkapan layar halaman",
            "        pertama) lalu figcaption Halaman pertama yang berhasil dibuka.",
            "      blockquote dengan cite bernilai buku.html, berisi satu p",
            "        bertuliskan Menulis kode itu seperti menulis surat untuk orang lain.",
            "  - footer berisi p bertuliskan Catatan ini disimpan sebagai index.html.",
            "",
            "Keluaran yang diharapkan:",
            "",
            "<!doctype html>",
            "html lang=\"id\"",
            "  head",
            "    meta charset=\"utf-8\"",
            "    meta content=\"width=device-width, initial-scale=1\" name=\"viewport\"",
            "    link href=\"gaya.css\" rel=\"stylesheet\"",
            "    title \"Catatan Belajar\"",
            "  body",
            "    header",
            "      h1 \"Catatan Belajar\"",
            "      p \"Ditulis oleh Sari.\"",
            "    main",
            "      article id=\"hari-pertama\"",
            "        h2 \"Hari Pertama\"",
            "        p \"Hari ini aku menulis halaman HTML pertamaku.\"",
            "        figure",
            "          img alt=\"Tangkapan layar halaman pertama\" src=\"layar.png\"",
            "          figcaption \"Halaman pertama yang berhasil dibuka.\"",
            "        blockquote cite=\"buku.html\"",
            "          p \"Menulis kode itu seperti menulis surat untuk orang lain.\"",
            "    footer",
            "      p \"Catatan ini disimpan sebagai index.html.\"",
        ],
        "hints": [
            "meta viewport punya DUA atribut: name dan content. Di pohon content "
            "dicetak lebih dulu karena c mendahului n, walau kamu menulis name duluan.",
            "figure membungkus gambar beserta keterangannya jadi satu kesatuan; "
            "figcaption adalah keterangan itu, dan letaknya di dalam figure.",
            "Teks kutipan tidak ditaruh langsung di dalam blockquote di sini — "
            "ada satu p di antaranya. Perhatikan indentasinya di pohon.",
        ],
        "solution": """<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="utf-8">
  <meta content="width=device-width, initial-scale=1" name="viewport">
  <link href="gaya.css" rel="stylesheet">
  <title>Catatan Belajar</title>
</head>
<body>
  <header>
    <h1>Catatan Belajar</h1>
    <p>Ditulis oleh Sari.</p>
  </header>
  <main>
    <article id="hari-pertama">
      <h2>Hari Pertama</h2>
      <p>Hari ini aku menulis halaman HTML pertamaku.</p>
      <figure>
        <img alt="Tangkapan layar halaman pertama" src="layar.png">
        <figcaption>Halaman pertama yang berhasil dibuka.</figcaption>
      </figure>
      <blockquote cite="buku.html">
        <p>Menulis kode itu seperti menulis surat untuk orang lain.</p>
      </blockquote>
    </article>
  </main>
  <footer>
    <p>Catatan ini disimpan sebagai index.html.</p>
  </footer>
</body>
</html>""",
    },
    {
        "title": "Latihan 11: Formulir Pendaftaran Lengkap",
        "difficulty": "Lanjut",
        "question": [
            "Buat halaman lengkap berbahasa id dengan title Pendaftaran Kursus.",
            "Isi body: h1 bertuliskan Pendaftaran Kursus, lalu form dengan",
            "action daftar.php dan method post yang berisi:",
            "",
            "  fieldset pertama:",
            "    legend Data Diri",
            "    label for nama, bertuliskan Nama",
            "    input id nama, name nama, type text, required",
            "    label for kelas, bertuliskan Kelas",
            "    select id kelas, name kelas, berisi dua option:",
            "      option value pagi bertuliskan Pagi",
            "      option value malam bertuliskan Malam, dan bertanda selected",
            "  fieldset kedua:",
            "    legend Pilihan",
            "    input id pemula, name tingkat, type radio, value pemula",
            "    label for pemula, bertuliskan Pemula",
            "    input id mahir, name tingkat, type radio, value mahir",
            "    label for mahir, bertuliskan Mahir",
            "    input id setuju, name setuju, type checkbox, bertanda checked",
            "    label for setuju, bertuliskan Saya setuju",
            "  lalu button type submit bertuliskan Daftar, di luar kedua fieldset",
            "",
            "Dua radio itu sengaja punya name yang SAMA (tingkat). Nama yang sama",
            "membuat keduanya satu kelompok, sehingga hanya satu yang bisa terpilih.",
            "selected dan checked ditulis tanpa nilai, seperti required.",
            "",
            "Keluaran yang diharapkan:",
            "",
            "<!doctype html>",
            "html lang=\"id\"",
            "  head",
            "    meta charset=\"utf-8\"",
            "    title \"Pendaftaran Kursus\"",
            "  body",
            "    h1 \"Pendaftaran Kursus\"",
            "    form action=\"daftar.php\" method=\"post\"",
            "      fieldset",
            "        legend \"Data Diri\"",
            "        label for=\"nama\" \"Nama\"",
            "        input id=\"nama\" name=\"nama\" required type=\"text\"",
            "        label for=\"kelas\" \"Kelas\"",
            "        select id=\"kelas\" name=\"kelas\"",
            "          option value=\"pagi\" \"Pagi\"",
            "          option selected value=\"malam\" \"Malam\"",
            "      fieldset",
            "        legend \"Pilihan\"",
            "        input id=\"pemula\" name=\"tingkat\" type=\"radio\" value=\"pemula\"",
            "        label for=\"pemula\" \"Pemula\"",
            "        input id=\"mahir\" name=\"tingkat\" type=\"radio\" value=\"mahir\"",
            "        label for=\"mahir\" \"Mahir\"",
            "        input checked id=\"setuju\" name=\"setuju\" type=\"checkbox\"",
            "        label for=\"setuju\" \"Saya setuju\"",
            "      button type=\"submit\" \"Daftar\"",
        ],
        "hints": [
            "legend harus jadi anak PERTAMA fieldset. Ditaruh di tempat lain, "
            "judul kelompoknya tidak lagi menempel di garis kotaknya.",
            "option punya tag penutup dan berada di dalam select. Yang dikirim ke "
            "server adalah value-nya, bukan tulisan yang dilihat orang.",
            "button di pohon menjorok sejajar dengan kedua fieldset, bukan di "
            "dalamnya. Letakkan sesudah </fieldset> yang kedua, sebelum </form>.",
        ],
        "solution": """<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="utf-8">
  <title>Pendaftaran Kursus</title>
</head>
<body>
  <h1>Pendaftaran Kursus</h1>
  <form action="daftar.php" method="post">
    <fieldset>
      <legend>Data Diri</legend>
      <label for="nama">Nama</label>
      <input id="nama" name="nama" required type="text">
      <label for="kelas">Kelas</label>
      <select id="kelas" name="kelas">
        <option value="pagi">Pagi</option>
        <option selected value="malam">Malam</option>
      </select>
    </fieldset>
    <fieldset>
      <legend>Pilihan</legend>
      <input id="pemula" name="tingkat" type="radio" value="pemula">
      <label for="pemula">Pemula</label>
      <input id="mahir" name="tingkat" type="radio" value="mahir">
      <label for="mahir">Mahir</label>
      <input checked id="setuju" name="setuju" type="checkbox">
      <label for="setuju">Saya setuju</label>
    </fieldset>
    <button type="submit">Daftar</button>
  </form>
</body>
</html>""",
    },
    {
        "title": "Latihan 12: Tabel Jadwal dengan Sel Gabungan",
        "difficulty": "Lanjut",
        "question": [
            "Buat halaman lengkap berbahasa id dengan title Jadwal Pekan Ini.",
            "Isi body hanya satu section dengan id bernilai pekan-ini dan class",
            "bernilai jadwal. Di dalam section itu:",
            "",
            "  - h1 bertuliskan Jadwal Pekan Ini",
            "  - table berisi, berurutan:",
            "      caption bertuliskan Jadwal Kelas Malam",
            "      thead berisi satu tr: th Hari, lalu th Sesi dengan colspan 2",
            "      tbody berisi dua tr:",
            "        tr pertama: td Senin dengan rowspan 2, td HTML, td 19.00",
            "        tr kedua: td CSS, td 20.00  (hanya dua sel, bukan tiga)",
            "      tfoot berisi satu tr dengan satu td colspan 3: Total 2 sesi",
            "",
            "Baris kedua sengaja cuma dua sel: kolom pertamanya sudah dipakai sel",
            "Senin yang membentang ke bawah lewat rowspan. Menambahkan td ketiga",
            "di situ membuat tabelnya melebar satu kolom tanpa disadari.",
            "",
            "Keluaran yang diharapkan:",
            "",
            "<!doctype html>",
            "html lang=\"id\"",
            "  head",
            "    meta charset=\"utf-8\"",
            "    title \"Jadwal Pekan Ini\"",
            "  body",
            "    section class=\"jadwal\" id=\"pekan-ini\"",
            "      h1 \"Jadwal Pekan Ini\"",
            "      table",
            "        caption \"Jadwal Kelas Malam\"",
            "        thead",
            "          tr",
            "            th \"Hari\"",
            "            th colspan=\"2\" \"Sesi\"",
            "        tbody",
            "          tr",
            "            td rowspan=\"2\" \"Senin\"",
            "            td \"HTML\"",
            "            td \"19.00\"",
            "          tr",
            "            td \"CSS\"",
            "            td \"20.00\"",
            "        tfoot",
            "          tr",
            "            td colspan=\"3\" \"Total 2 sesi\"",
        ],
        "hints": [
            "colspan menggabungkan sel ke SAMPING, rowspan ke BAWAH. Sel yang "
            "tergabung tidak ditulis ulang di baris atau kolom berikutnya.",
            "Tabel ini tiga kolom. Hitung tiap tr: 1 + 2 (colspan) = 3, "
            "lalu 1 (rowspan) + 1 + 1 = 3, lalu (sisa rowspan) + 1 + 1 = 3.",
            "Atribut section dicetak class dulu baru id karena urut abjad, "
            "padahal soal menyebut id lebih dulu. Urutan penulisanmu bebas.",
        ],
        "solution": """<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="utf-8">
  <title>Jadwal Pekan Ini</title>
</head>
<body>
  <section class="jadwal" id="pekan-ini">
    <h1>Jadwal Pekan Ini</h1>
    <table>
      <caption>Jadwal Kelas Malam</caption>
      <thead>
        <tr>
          <th>Hari</th>
          <th colspan="2">Sesi</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td rowspan="2">Senin</td>
          <td>HTML</td>
          <td>19.00</td>
        </tr>
        <tr>
          <td>CSS</td>
          <td>20.00</td>
        </tr>
      </tbody>
      <tfoot>
        <tr>
          <td colspan="3">Total 2 sesi</td>
        </tr>
      </tfoot>
    </table>
  </section>
</body>
</html>""",
    },
]
