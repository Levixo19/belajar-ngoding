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
            "Baca ulang materi Apa Itu HTML & Halaman Pertamamu dan Struktur Dokumen: head dan body. Halaman lengkap selalu punya kerangka yang sama: baris doctype, lalu html yang membungkus head (keterangan tentang halaman) dan body (isi yang tampil).",
            "Urutannya: doctype, buka html dengan atribut lang, buka head, tulis meta charset lalu title, tutup head, buka body, tulis h1 lalu p, tutup body dan html. head dan body sama-sama anak langsung html, jadi di pohon keduanya menjorok satu tingkat.",
            "Baris pertama bukan tag biasa: <!DOCTYPE html>. Di pohon ia dicetak huruf kecil semua, itu normal. meta termasuk elemen kosong, jadi cukup <meta charset=\"utf-8\"> tanpa penutup; menulis </meta> justru dilaporkan sebagai kesalahan.",
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
            "Materi Teks: Heading, Paragraf, dan Penekanan menjelaskan kenapa h1 dipakai sekali sebagai judul halaman dan h2 untuk sub-bagian. Angkanya menandakan tingkat, bukan ukuran huruf.",
            "Kerangka doctype, html, head, dan body sama dengan Latihan 1; yang berubah cuma isi title dan isi body. Teks Tentang Saya muncul dua kali: di title (nama tab browser) dan di h1 (judul yang terbaca di halaman). Keduanya memang perlu.",
            "Semua h1, h2, dan p di sini bersaudara, sama-sama anak langsung body, jadi tulis berderet tanpa pembungkus apa pun: <h2>Hobi</h2>, lalu p-nya, lalu h2 berikutnya. Indentasinya di pohon sama rata.",
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
            "Baca lagi materi Daftar: ul, ol, dan dl. ul untuk hal yang urutannya nggak penting, ol untuk langkah yang berurutan, dan nomor pada ol dibuat browser sendiri, jadi jangan diketik.",
            "li nggak berdiri sendiri: ia selalu berada di dalam ul atau ol, makanya di pohon indentasinya lebih dalam. Baris ul dan ol nggak punya teks dalam kutip karena semua tulisannya ada di dalam li masing-masing.",
            "Bentuknya <ul>, lalu tiga <li>...</li>, lalu </ul>; ol sama persis, cuma nama tagnya yang beda. Kalau salah satu li muncul di tingkat yang salah, biasanya ada </li> yang terlewat.",
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
            "Materi Tautan (a) dan Gambar (img) membahas dua elemen ini. img itu elemen kosong yang seluruh isinya ditentukan atribut, sedangkan a membungkus teks yang bisa diklik.",
            "Tulis h1, lalu img dengan tiga atribut (src, alt, width), lalu p, lalu dua a. Atribut di pohon selalu dicetak urut abjad, jadi urutan menulismu bebas. alt adalah teks pengganti kalau gambar gagal dimuat dan satu-satunya yang dibacakan pembaca layar, jadi jangan dikosongkan.",
            "img nggak punya </img>: cukup <img src=\"...\" alt=\"...\" width=\"...\">. Tautan ditulis <a href=\"nama-berkas.html\">teks</a>; nilai href di sini nama berkas biasa, bukan alamat penuh.",
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
            "Baca ulang Teks: Heading, Paragraf, dan Penekanan. strong dan em adalah elemen sebaris: mereka duduk di tengah teks sebuah p, bukan memecah p itu jadi beberapa.",
            "Tiga p ini ditulis biasa saja, tanpa div atau span tambahan. p pertama berisi teks, lalu strong, lalu teks lagi, semuanya di dalam satu p. p kedua nggak punya teks sendiri sama sekali karena seluruh tulisannya milik em, makanya baris p-nya di pohon berdiri tanpa kutipan.",
            "br elemen kosong: cukup <br> di tengah teks, misalnya Ruang A<br>Lantai 2, tanpa penutup. Jangan menulis <br></br>.",
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
            "Materi Daftar: ul, ol, dan dl membahas daftar bersarang dan daftar istilah. Sub-daftar adalah bagian dari satu item, jadi ia ditulis di dalam li induknya, bukan di antara dua li.",
            "Perhatikan pohonnya: ul kedua menjorok satu tingkat lebih dalam daripada li Minuman, artinya ia anak li itu. Urutannya: teks Minuman dulu, lalu ul bersarang, baru </li>. Di dl, dt itu istilah dan dd penjelasannya; keduanya anak langsung dl dan berdiri sejajar, dd nggak berada di dalam dt.",
            "Kerangka item yang bersarang: <li>Minuman <ul> ...dua li... </ul> </li>. Menutup </li> terlalu cepat membuat ul-nya keluar dari li.",
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
            "Baca lagi materi Tabel. Tabel disusun bertingkat: table, lalu bagian kepala dan badan (thead, tbody), lalu baris (tr), lalu sel (th untuk judul, td untuk isi).",
            "Hitung indentasi pohon sebelum menulis: ada empat tingkat sarang. caption ditulis paling pertama di dalam table. Satu tr adalah satu baris; dua th berarti tabel ini dua kolom, jadi tiap tr di tbody juga berisi dua sel.",
            "Satu baris isi bentuknya <tr> berisi dua <td>...</td>, lalu </tr>. Angka 90 dan 75 ditulis sebagai teks biasa di dalam td; HTML nggak punya tipe data.",
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
            "Materi Formulir: input, label, dan button menjelaskan pasangan label dan isian. label for menunjuk id isiannya, sedangkan name adalah nama yang dipakai server saat data dikirim.",
            "Di dalam form tulis berurutan: label, input, label, textarea, button. Nilai for harus sama persis dengan id isiannya; itu yang bikin klik tulisan Nama memindahkan kursor ke kotaknya. id dan name sama-sama perlu walau nilainya kebetulan sama. required ditulis tanpa nilai, dan di pohon muncul sebagai kata sendirian.",
            "input elemen kosong (nggak ada </input>), tapi textarea punya tag penutup. Karena isinya kosong, tulis menempel: <textarea ...atribut...></textarea>.",
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
            "Baca ulang Elemen Semantik: header, nav, main, article, footer. Elemen-elemen ini bekerja seperti div, bedanya namanya memberi tahu peran isinya. Menu navigasi ditulis sebagai daftar karena memang daftar tautan.",
            "Susun tiga blok besar di body: header, main, footer. nav berada di dalam header, sejajar dengan h1, bukan sesudah </header>; bandingkan indentasinya dengan main dan footer. Satu halaman cuma punya satu main, dan section di dalamnya mulai dari h2 karena h1 sudah dipakai di header.",
            "Baris li di pohon nggak punya kutipan teks, artinya seluruh tulisannya ada di a yang jadi anaknya. Satu item menu bentuknya <li><a href=\"...\">Beranda</a></li>.",
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
            "Materi yang dipakai: Metadata: title, meta, dan Kenapa Itu Penting untuk isi head, Tautan (a) dan Gambar (img) untuk figure, dan Kutipan, Waktu, dan Penanda Teks Lainnya untuk blockquote.",
            "Kerjakan dari luar ke dalam: head dulu (empat baris berurutan), lalu header, main berisi satu article, lalu footer. Di dalam article urutannya h2, p, figure, blockquote. figure membungkus gambar beserta keterangannya, dan figcaption ada di dalam figure.",
            "meta viewport punya dua atribut, name dan content; di pohon content dicetak lebih dulu karena c mendahului n, walau kamu menulis name duluan. Teks kutipan nggak ditaruh langsung di blockquote: ada satu p di antaranya, <blockquote cite=\"...\"><p>...</p></blockquote>.",
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
            "Baca lagi Formulir Lanjutan: select, textarea, dan Validasi. fieldset mengelompokkan isian yang berhubungan dan legend jadi judul kelompoknya. Radio dengan name yang sama membentuk satu kelompok, jadi cuma satu yang bisa terpilih.",
            "Buat dua fieldset berurutan di dalam form, lalu button sesudah fieldset kedua, sebelum </form>; di pohon button sejajar dengan kedua fieldset, bukan di dalamnya. legend harus jadi anak pertama fieldset. option punya tag penutup dan berada di dalam select; yang dikirim ke server adalah value-nya, bukan tulisan yang dilihat orang.",
            "selected, checked, dan required ditulis tanpa nilai, misalnya <option selected value=\"...\">Malam</option>. Kedua radio memakai name yang sama, tapi id dan value-nya berbeda.",
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
            "Materi Tabel membahas colspan dan rowspan. colspan melebarkan sel ke samping, rowspan memanjangkannya ke bawah, dan sel yang sudah tertutup gabungan nggak ditulis ulang di baris atau kolom berikutnya.",
            "Tabel ini tiga kolom. Hitung tiap tr: 1 + 2 (colspan) = 3, lalu 1 (rowspan) + 1 + 1 = 3, lalu (sisa rowspan) + 1 + 1 = 3, dan baris tfoot satu sel dengan colspan 3. Seluruh isi body dibungkus satu section, termasuk h1.",
            "Atribut section dicetak class dulu baru id karena urut abjad, padahal soal menyebut id lebih dulu; urutan menulismu bebas. Sel Senin bentuknya <td rowspan=\"2\">, dan tr berikutnya cuma berisi dua td.",
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
    {
        "title": "Latihan 13: Kerangka Canvas dengan Konten Cadangan",
        "difficulty": "Mudah",
        "question": [
            "Buat SATU elemen <canvas> dengan:",
            "",
            "  - atribut id bernilai papan",
            "  - atribut width bernilai 400",
            "  - atribut height bernilai 300",
            "  - di dalamnya, satu paragraf <p> bertuliskan:",
            "    Browser Anda tidak mendukung Canvas.",
            "",
            "HTML tidak dijalankan. Yang dinilai adalah POHON struktur berkasmu,",
            "hasil pembacaan struktur.py. Cocokkan sampai ke tanda bacanya.",
            "",
            "Keluaran yang diharapkan:",
            "",
            "canvas height=\"300\" id=\"papan\" width=\"400\"",
            "  p \"Browser Anda tidak mendukung Canvas.\"",
        ],
        "hints": [
            "Baca ulang Canvas: Menggambar Langsung di Halaman. canvas bukan elemen kosong seperti img: ia punya tag penutup, dan isi di antara tag buka dan tutup jadi konten cadangan untuk browser yang nggak mendukung canvas.",
            "Tulis canvas dengan tiga atribut (id, width, height), lalu satu p di dalamnya, lalu tutup canvas. p di dalam canvas sama seperti p di mana pun, tetap butuh </p>.",
            "Atribut di keluaran diurutkan abjad oleh struktur.py, jadi height muncul sebelum id walau kamu menulis id lebih dulu. Kerangkanya: <canvas ...> lalu <p>...</p> lalu </canvas>.",
        ],
        "solution": """<canvas id="papan" width="400" height="300">
  <p>Browser Anda tidak mendukung Canvas.</p>
</canvas>""",
    },
    {
        'title': 'Proyek Akhir: Halaman Warung Kopi',
        'difficulty': 'Sulit',
        'proyek': True,
        'question': [
        'STUDI KASUS -- Halaman Warung Kopi',
        '',
        'Warung kopi tetanggamu belum punya halaman web. Yang ia butuhkan cuma',
        'satu halaman: menu, jam buka, dan cara memesan.',
        '',
        'Tidak ada CSS sama sekali di proyek ini. Yang diuji satu hal: apakah',
        'kamu memilih ELEMEN yang tepat untuk tiap maksud. Halaman yang',
        'elemennya benar tetap terbaca orang tanpa gaya apa pun -- dan tetap',
        'terbaca pembaca layar, yang tidak pernah melihat gayamu sama sekali.',
        '',
        'Atribut dicetak berurut alfabetis oleh penilai, jadi urutan menulismu',
        'tidak perlu sama.',
        '',
        'Yang harus ada di programmu:',
        '  1. <head> lengkap: charset, viewport, title, dan meta description.',
        "  2. Tautan 'Lewati ke isi' sebagai elemen PERTAMA di body, menuju",
        '     id di <main>.',
        '  3. <header> berisi h1, satu paragraf, dan <nav aria-label> berisi',
        '     daftar tautan.',
        '  4. Menu memakai <table> lengkap: caption, thead, tbody, dan',
        "     th scope='col' / th scope='row' -- kolom nama pakai th, bukan td.",
        '  5. Gambar dibungkus <figure> + <figcaption>, img wajib punya alt',
        '     yang menjelaskan, serta width dan height.',
        '  6. Jam buka memakai <dl> (dt/dd), bukan tabel dan bukan daftar biasa.',
        '  7. Jam pesanan terakhir dibungkus <time datetime>.',
        '  8. Formulir: <fieldset> + <legend>, tiap isian punya <label for>,',
        "     ada <select> dengan dua <option>, dan <button type='submit'>.",
        '  9. <footer> berisi <address> dan <small>.',
        '',
        'Keluaran yang diharapkan:',
        '',
        '  <!doctype html>',
        '  html lang="id"',
        '    head',
        '      meta charset="utf-8"',
        '      meta content="width=device-width, initial-scale=1" name="viewport"',
        '      title "Warung Kopi Pagi — Menu dan Kontak"',
        '      meta content="Warung kopi kecil di Bandung. Menu, jam buka, dan cara memesan." name="description"',
        '    body',
        '      a class="lewati" href="#isi" "Lewati ke isi"',
        '      header',
        '        h1 "Warung Kopi Pagi"',
        '        p "Kopi tubruk dan roti bakar, buka sejak 2019."',
        '        nav aria-label="Navigasi utama"',
        '          ul',
        '            li',
        '              a href="#menu" "Menu"',
        '            li',
        '              a href="#jam" "Jam buka"',
        '            li',
        '              a href="#pesan" "Pesan"',
        '      main id="isi"',
        '        section id="menu"',
        '          h2 "Menu"',
        '          table',
        '            caption "Harga sudah termasuk pajak"',
        '            thead',
        '              tr',
        '                th scope="col" "Nama"',
        '                th scope="col" "Ukuran"',
        '                th scope="col" "Harga"',
        '            tbody',
        '              tr',
        '                th scope="row" "Kopi Tubruk"',
        '                td "200 ml"',
        '                td "Rp8.000"',
        '              tr',
        '                th scope="row" "Kopi Susu"',
        '                td "250 ml"',
        '                td "Rp12.000"',
        '              tr',
        '                th scope="row" "Roti Bakar"',
        '                td "1 porsi"',
        '                td "Rp15.000"',
        '          figure',
        '            img alt="Secangkir kopi tubruk di atas meja kayu" height="200" src="kopi.jpg" width="320"',
        '            figcaption "Kopi tubruk, diseduh langsung di cangkir."',
        '        section id="jam"',
        '          h2 "Jam buka"',
        '          dl',
        '            dt "Senin sampai Jumat"',
        '            dd "06.00 - 17.00"',
        '            dt "Sabtu"',
        '            dd "06.00 - 21.00"',
        '            dt "Minggu"',
        '            dd "Tutup"',
        '          p "Pesanan terakhir di hari kerja."',
        '            time datetime="16:30" "16.30"',
        '        section id="pesan"',
        '          h2 "Pesan lebih dulu"',
        '          form action="/pesan" method="post"',
        '            fieldset',
        '              legend "Data pemesan"',
        '              p',
        '                label for="nama" "Nama"',
        '                input id="nama" name="nama" required type="text"',
        '              p',
        '                label for="minuman" "Pilih minuman"',
        '                select id="minuman" name="minuman"',
        '                  option value="tubruk" "Kopi Tubruk"',
        '                  option value="susu" "Kopi Susu"',
        '            button type="submit" "Kirim pesanan"',
        '      footer',
        '        address "Jalan Melati 7, Bandung"',
        '        p',
        '          small "© 2026 Warung Kopi Pagi"',
    ],
        "hints": [
            "Materi Merakit Satu Halaman Utuh menyatukan hampir semua elemen proyek ini. Untuk tautan lewati baca Bisa Dipakai Semua Orang: role, aria-*, dan tabindex; untuk th scope baca Tabel; untuk dl dan time baca Daftar: ul, ol, dan dl serta Kutipan, Waktu, dan Penanda Teks Lainnya.",
            "Kerjakan per bagian sambil mencocokkan pohon: head (empat baris berurutan), tautan Lewati ke isi sebagai anak pertama body, header, main berisi tiga section (menu, jam, pesan), lalu footer. Satu halaman cuma boleh punya satu main, dan id di main itulah yang dituju tautan lewati. Sel yang menamai barisnya (nama minuman) pakai th dengan scope row, bukan td; tanpa scope pembaca layar harus menebak. Jam buka adalah pasangan nama-nilai (hari dan jam), jadi pakai dl, bukan tabel.",
            "Dua bagian yang paling sering meleset. Pertama, time ada di tengah kalimat di dalam p: <p>Pesanan terakhir <time datetime=\"16:30\">16.30</time> di hari kerja.</p>. Kedua, button berada di luar fieldset, sebelum </form>. Simbol hak cipta ditulis lewat entitas &copy; di dalam small.",
        ],
        'solution': """<!doctype html>
<html lang="id">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Warung Kopi Pagi — Menu dan Kontak</title>
  <meta name="description" content="Warung kopi kecil di Bandung. Menu, jam buka, dan cara memesan.">
</head>
<body>
  <a class="lewati" href="#isi">Lewati ke isi</a>

  <header>
    <h1>Warung Kopi Pagi</h1>
    <p>Kopi tubruk dan roti bakar, buka sejak 2019.</p>
    <nav aria-label="Navigasi utama">
      <ul>
        <li><a href="#menu">Menu</a></li>
        <li><a href="#jam">Jam buka</a></li>
        <li><a href="#pesan">Pesan</a></li>
      </ul>
    </nav>
  </header>

  <main id="isi">
    <section id="menu">
      <h2>Menu</h2>
      <table>
        <caption>Harga sudah termasuk pajak</caption>
        <thead>
          <tr>
            <th scope="col">Nama</th>
            <th scope="col">Ukuran</th>
            <th scope="col">Harga</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <th scope="row">Kopi Tubruk</th>
            <td>200 ml</td>
            <td>Rp8.000</td>
          </tr>
          <tr>
            <th scope="row">Kopi Susu</th>
            <td>250 ml</td>
            <td>Rp12.000</td>
          </tr>
          <tr>
            <th scope="row">Roti Bakar</th>
            <td>1 porsi</td>
            <td>Rp15.000</td>
          </tr>
        </tbody>
      </table>

      <figure>
        <img alt="Secangkir kopi tubruk di atas meja kayu" height="200" src="kopi.jpg" width="320">
        <figcaption>Kopi tubruk, diseduh langsung di cangkir.</figcaption>
      </figure>
    </section>

    <section id="jam">
      <h2>Jam buka</h2>
      <dl>
        <dt>Senin sampai Jumat</dt>
        <dd>06.00 - 17.00</dd>
        <dt>Sabtu</dt>
        <dd>06.00 - 21.00</dd>
        <dt>Minggu</dt>
        <dd>Tutup</dd>
      </dl>
      <p>Pesanan terakhir <time datetime="16:30">16.30</time> di hari kerja.</p>
    </section>

    <section id="pesan">
      <h2>Pesan lebih dulu</h2>
      <form action="/pesan" method="post">
        <fieldset>
          <legend>Data pemesan</legend>
          <p>
            <label for="nama">Nama</label>
            <input id="nama" name="nama" required type="text">
          </p>
          <p>
            <label for="minuman">Pilih minuman</label>
            <select id="minuman" name="minuman">
              <option value="tubruk">Kopi Tubruk</option>
              <option value="susu">Kopi Susu</option>
            </select>
          </p>
        </fieldset>
        <button type="submit">Kirim pesanan</button>
      </form>
    </section>
  </main>

  <footer>
    <address>Jalan Melati 7, Bandung</address>
    <p><small>&copy; 2026 Warung Kopi Pagi</small></p>
  </footer>
</body>
</html>
""",
    },
]
