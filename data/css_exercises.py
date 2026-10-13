CSS_EXERCISES = [
    {
        "title": "Latihan 1: Aturan CSS Pertama",
        "difficulty": "Mudah",
        "question": [
            "Tulis satu aturan untuk pemilih body dengan tiga properti,",
            "URUT seperti ini:",
            "  1. background-color bernilai #f5f5f5",
            "  2. color bernilai #222222",
            "  3. font-family bernilai sans-serif",
            "",
            "Urutan penulisan properti ikut diperiksa, jadi tulis persis",
            "seperti urutan di atas.",
            "",
            "Keluaran yang diharapkan:",
            "  body",
            "    background-color: #f5f5f5",
            "    color: #222222",
            "    font-family: sans-serif",
        ],
        "hints": [
            "Bentuk satu aturan CSS: pemilih { properti: nilai; }",
            "Tiap deklarasi ditutup titik koma, termasuk yang terakhir.",
            "Warna heks selalu diawali tanda pagar: #f5f5f5, bukan f5f5f5.",
        ],
        "solution": """body {
  background-color: #f5f5f5;
  color: #222222;
  font-family: sans-serif;
}""",
    },
    {
        "title": "Latihan 2: Dua Pemilih Elemen",
        "difficulty": "Mudah",
        "question": [
            "Tulis dua aturan, urut: h1 lebih dulu, lalu p.",
            "",
            "h1 dengan tiga properti berurutan:",
            "  color bernilai #1a4d8f",
            "  font-size bernilai 32px",
            "  text-align bernilai center",
            "",
            "p dengan dua properti berurutan:",
            "  color bernilai #444444",
            "  line-height bernilai 1.6",
            "",
            "Keluaran yang diharapkan:",
            "  h1",
            "    color: #1a4d8f",
            "    font-size: 32px",
            "    text-align: center",
            "  p",
            "    color: #444444",
            "    line-height: 1.6",
        ],
        "hints": [
            "Pemilih elemen ditulis apa adanya: h1, bukan <h1> atau .h1.",
            "Satu berkas CSS boleh berisi banyak aturan; tulis berurutan.",
            "line-height tanpa satuan (1.6) artinya 1,6 kali ukuran huruf "
            "elemen itu sendiri — nilai yang paling aman untuk teks.",
        ],
        "solution": """h1 {
  color: #1a4d8f;
  font-size: 32px;
  text-align: center;
}

p {
  color: #444444;
  line-height: 1.6;
}""",
    },
    {
        "title": "Latihan 3: Kelas dan ID",
        "difficulty": "Mudah",
        "question": [
            "Tulis dua aturan, urut: #judul-utama lebih dulu, lalu .tombol.",
            "",
            "#judul-utama dengan dua properti berurutan:",
            "  font-size bernilai 28px",
            "  margin-bottom bernilai 16px",
            "",
            ".tombol dengan tiga properti berurutan:",
            "  background-color bernilai #2e7d32",
            "  color bernilai #ffffff",
            "  padding bernilai 10px 20px",
            "",
            "Keluaran yang diharapkan:",
            "  #judul-utama",
            "    font-size: 28px",
            "    margin-bottom: 16px",
            "  .tombol",
            "    background-color: #2e7d32",
            "    color: #ffffff",
            "    padding: 10px 20px",
        ],
        "hints": [
            "Kelas diawali titik (.tombol), id diawali pagar (#judul-utama).",
            "Satu id hanya boleh dipakai sekali di satu halaman; kelas boleh "
            "dipakai berkali-kali. Karena itu tombol memakai kelas.",
            "padding: 10px 20px berarti 10px atas-bawah, 20px kiri-kanan.",
        ],
        "solution": """#judul-utama {
  font-size: 28px;
  margin-bottom: 16px;
}

.tombol {
  background-color: #2e7d32;
  color: #ffffff;
  padding: 10px 20px;
}""",
    },
    {
        "title": "Latihan 4: Ruang di Dalam dan di Luar Kotak",
        "difficulty": "Mudah",
        "question": [
            "Tulis satu aturan untuk .kartu dengan empat properti,",
            "URUT dari dalam ke luar:",
            "  1. width bernilai 300px",
            "  2. padding bernilai 16px",
            "  3. border bernilai 2px solid #cccccc",
            "  4. margin bernilai 24px",
            "",
            "Urutan itu bukan kebetulan: padding adalah ruang DI DALAM",
            "garis tepi, border adalah garisnya, margin adalah ruang DI LUAR.",
            "",
            "Keluaran yang diharapkan:",
            "  .kartu",
            "    width: 300px",
            "    padding: 16px",
            "    border: 2px solid #cccccc",
            "    margin: 24px",
        ],
        "hints": [
            "border ditulis singkat dalam satu baris: tebal, gaya, warna.",
            "Gaya garis yang paling umum: solid, dashed, dotted.",
            "Satu nilai pada padding/margin berlaku untuk keempat sisi.",
        ],
        "solution": """.kartu {
  width: 300px;
  padding: 16px;
  border: 2px solid #cccccc;
  margin: 24px;
}""",
    },
    {
        "title": "Latihan 5: Satu Aturan untuk Tiga Pemilih",
        "difficulty": "Menengah",
        "question": [
            "Tiga judul h1, h2, dan h3 harus mendapat gaya yang sama.",
            "Tulis SATU aturan saja untuk ketiganya, dengan tiga properti",
            "berurutan:",
            "  1. font-family bernilai sans-serif",
            "  2. font-weight bernilai 700",
            "  3. margin bernilai 0",
            "",
            "Keluaran yang diharapkan:",
            "  h1, h2, h3",
            "    font-family: sans-serif",
            "    font-weight: 700",
            "    margin: 0",
        ],
        "hints": [
            "Pisahkan pemilih dengan koma: h1, h2, h3 { ... }",
            "Spasi di sekitar koma tidak berpengaruh — h1,h2,h3 dan "
            "h1 , h2 , h3 menghasilkan aturan yang sama persis.",
            "Menyalin tiga aturan yang isinya sama berarti tiga tempat yang "
            "harus diubah nanti; satu aturan bergabung cuma satu tempat.",
        ],
        "solution": """h1, h2, h3 {
  font-family: sans-serif;
  font-weight: 700;
  margin: 0;
}""",
    },
    {
        "title": "Latihan 6: Pemilih Turunan dan Pemilih Anak",
        "difficulty": "Menengah",
        "question": [
            "Tulis dua aturan, urut seperti berikut.",
            "",
            "Pertama untuk SEMUA <a> yang ada di dalam <nav>, sedalam apa pun,",
            "dengan dua properti berurutan:",
            "  color bernilai #1a4d8f",
            "  text-decoration bernilai none",
            "",
            "Kedua untuk <li> yang merupakan ANAK LANGSUNG dari .menu,",
            "dengan dua properti berurutan:",
            "  display bernilai inline-block",
            "  margin-right bernilai 12px",
            "",
            "Keluaran yang diharapkan:",
            "  nav a",
            "    color: #1a4d8f",
            "    text-decoration: none",
            "  .menu > li",
            "    display: inline-block",
            "    margin-right: 12px",
        ],
        "hints": [
            "Spasi antar-pemilih berarti 'di dalam': nav a.",
            "Tanda > berarti 'anak langsung': .menu > li. Bedanya terasa saat "
            "ada daftar bersarang — li di dalam li tidak ikut kena.",
            "text-decoration: none yang menghapus garis bawah tautan.",
        ],
        "solution": """nav a {
  color: #1a4d8f;
  text-decoration: none;
}

.menu > li {
  display: inline-block;
  margin-right: 12px;
}""",
    },
    {
        "title": "Latihan 7: Pseudo-class Hover dan First-child",
        "difficulty": "Menengah",
        "question": [
            "Tulis tiga aturan, urut seperti berikut.",
            "",
            "a dengan dua properti berurutan:",
            "  color bernilai #1a4d8f",
            "  text-decoration bernilai none",
            "",
            "a:hover dengan dua properti berurutan:",
            "  color bernilai #d32f2f",
            "  text-decoration bernilai underline",
            "",
            "li:first-child dengan satu properti:",
            "  font-weight bernilai 700",
            "",
            "Keluaran yang diharapkan:",
            "  a",
            "    color: #1a4d8f",
            "    text-decoration: none",
            "  a:hover",
            "    color: #d32f2f",
            "    text-decoration: underline",
            "  li:first-child",
            "    font-weight: 700",
        ],
        "hints": [
            "Pseudo-class ditempel langsung tanpa spasi: a:hover, bukan a :hover.",
            "Aturan :hover harus ditulis SESUDAH aturan a biasa — kalau "
            "spesifisitasnya sama, yang belakangan yang menang.",
            ":first-child memilih elemen yang jadi anak pertama induknya.",
        ],
        "solution": """a {
  color: #1a4d8f;
  text-decoration: none;
}

a:hover {
  color: #d32f2f;
  text-decoration: underline;
}

li:first-child {
  font-weight: 700;
}""",
    },
    {
        "title": "Latihan 8: Menata Baris dengan Flexbox",
        "difficulty": "Menengah",
        "question": [
            "Tulis dua aturan, urut seperti berikut.",
            "",
            ".baris dengan empat properti berurutan:",
            "  1. display bernilai flex",
            "  2. justify-content bernilai space-between",
            "  3. align-items bernilai center",
            "  4. gap bernilai 12px",
            "",
            ".baris > .item dengan dua properti berurutan:",
            "  1. flex bernilai 1",
            "  2. min-width bernilai 0",
            "",
            "Keluaran yang diharapkan:",
            "  .baris",
            "    display: flex",
            "    justify-content: space-between",
            "    align-items: center",
            "    gap: 12px",
            "  .baris > .item",
            "    flex: 1",
            "    min-width: 0",
        ],
        "hints": [
            "display: flex dipasang di WADAHNYA, bukan di isinya.",
            "justify-content mengatur sepanjang baris (kiri-kanan), "
            "align-items mengatur melintangnya (atas-bawah).",
            "min-width: 0 mencegah isi yang panjang melebarkan kolomnya — "
            "bawaan min-width adalah auto, yang berarti 'jangan menyusut'.",
        ],
        "solution": """.baris {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 12px;
}

.baris > .item {
  flex: 1;
  min-width: 0;
}""",
    },
    {
        "title": "Latihan 9: Variabel CSS di :root",
        "difficulty": "Menengah",
        "question": [
            "Tulis dua aturan, urut seperti berikut.",
            "",
            ":root dengan dua variabel berurutan:",
            "  --warna-utama bernilai #1a4d8f",
            "  --jarak bernilai 16px",
            "",
            ".kotak dengan dua properti berurutan yang MEMAKAI variabel itu:",
            "  background-color bernilai var(--warna-utama)",
            "  padding bernilai var(--jarak)",
            "",
            "Keluaran yang diharapkan:",
            "  :root",
            "    --warna-utama: #1a4d8f",
            "    --jarak: 16px",
            "  .kotak",
            "    background-color: var(--warna-utama)",
            "    padding: var(--jarak)",
        ],
        "hints": [
            "Nama variabel WAJIB diawali dua tanda minus: --warna-utama.",
            "Memakainya lewat var(): background-color: var(--warna-utama);",
            ":root adalah elemen <html>. Variabel yang ditaruh di sana "
            "terbaca oleh seluruh halaman, jadi satu warna cukup diubah "
            "di satu tempat.",
        ],
        "solution": """:root {
  --warna-utama: #1a4d8f;
  --jarak: 16px;
}

.kotak {
  background-color: var(--warna-utama);
  padding: var(--jarak);
}""",
    },
    {
        "title": "Latihan 10: Media Query untuk Layar Sempit",
        "difficulty": "Lanjut",
        "question": [
            "Tulis aturan .wadah untuk layar normal, lalu satu blok",
            "@media (max-width: 600px) yang menimpanya untuk layar sempit.",
            "",
            ".wadah dengan tiga properti berurutan:",
            "  1. display bernilai grid",
            "  2. grid-template-columns bernilai 1fr 1fr 1fr",
            "  3. gap bernilai 16px",
            "",
            "Di dalam @media (max-width: 600px), aturan .wadah lagi",
            "dengan dua properti berurutan:",
            "  1. grid-template-columns bernilai 1fr",
            "  2. gap bernilai 8px",
            "",
            "Keluaran yang diharapkan (isi @media ikut menjorok):",
            "  .wadah",
            "    display: grid",
            "    grid-template-columns: 1fr 1fr 1fr",
            "    gap: 16px",
            "  @media (max-width: 600px)",
            "    .wadah",
            "      grid-template-columns: 1fr",
            "      gap: 8px",
        ],
        "hints": [
            "Bentuknya: @media (max-width: 600px) { .wadah { ... } }",
            "Ada dua kurung kurawal yang harus ditutup, bukan satu.",
            "Blok @media ditulis SESUDAH aturan biasa. Kalau ditulis lebih "
            "dulu, aturan biasa yang datang belakangan justru menimpanya "
            "dan tata letak ponselnya diam-diam tidak berlaku.",
        ],
        "solution": """.wadah {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 16px;
}

@media (max-width: 600px) {
  .wadah {
    grid-template-columns: 1fr;
    gap: 8px;
  }
}""",
    },
    {
        "title": "Latihan 11: Grid dengan Area Bernama",
        "difficulty": "Lanjut",
        "question": [
            "Susun tata letak dua kolom dengan grid area bernama.",
            "Tulis empat aturan, urut seperti berikut.",
            "",
            ".tata dengan lima properti berurutan:",
            "  1. display bernilai grid",
            "  2. grid-template-columns bernilai 200px 1fr",
            "  3. grid-template-rows bernilai auto 1fr",
            '  4. grid-template-areas bernilai "kepala kepala" "sisi isi"',
            "  5. gap bernilai 20px",
            "",
            "Lalu tiga aturan berisi satu properti grid-area masing-masing:",
            "  .kepala dengan grid-area bernilai kepala",
            "  .sisi dengan grid-area bernilai sisi",
            "  .isi dengan grid-area bernilai isi",
            "",
            "Keluaran yang diharapkan:",
            "  .tata",
            "    display: grid",
            "    grid-template-columns: 200px 1fr",
            "    grid-template-rows: auto 1fr",
            '    grid-template-areas: "kepala kepala" "sisi isi"',
            "    gap: 20px",
            "  .kepala",
            "    grid-area: kepala",
            "  .sisi",
            "    grid-area: sisi",
            "  .isi",
            "    grid-area: isi",
        ],
        "hints": [
            "Tiap baris grid ditulis sebagai satu string berkutip ganda.",
            "Dua string itu ditulis berdampingan dipisah satu spasi:",
            '  grid-template-areas: "kepala kepala" "sisi isi";',
            "Nama area di grid-area ditulis TANPA kutip dan tanpa titik —",
            "'kepala', bukan '.kepala'. Yang pakai titik cuma pemilihnya.",
        ],
        "solution": """.tata {
  display: grid;
  grid-template-columns: 200px 1fr;
  grid-template-rows: auto 1fr;
  grid-template-areas: "kepala kepala" "sisi isi";
  gap: 20px;
}

.kepala {
  grid-area: kepala;
}

.sisi {
  grid-area: sisi;
}

.isi {
  grid-area: isi;
}""",
    },
    {
        "title": "Latihan 12: Lembar Gaya Kartu Produk",
        "difficulty": "Lanjut",
        "question": [
            "Gabungkan semuanya jadi satu lembar gaya kecil.",
            "Tulis empat aturan, urut seperti berikut.",
            "",
            ":root dengan empat variabel berurutan:",
            "  --latar bernilai #ffffff",
            "  --garis bernilai #dddddd",
            "  --teks bernilai #222222",
            "  --jeda bernilai 0.2s",
            "",
            ".kartu-produk dengan enam properti berurutan:",
            "  1. background-color bernilai var(--latar)",
            "  2. border bernilai 1px solid var(--garis)",
            "  3. border-radius bernilai 8px",
            "  4. color bernilai var(--teks)",
            "  5. padding bernilai 20px",
            "  6. transition bernilai box-shadow var(--jeda) ease",
            "",
            ".kartu-produk:hover dengan satu properti:",
            "  box-shadow bernilai 0 2px 8px rgba(0, 0, 0, 0.15)",
            "",
            "@media (prefers-reduced-motion: reduce) berisi aturan",
            ".kartu-produk dengan satu properti:",
            "  transition bernilai none",
            "",
            "Keluaran yang diharapkan:",
            "  :root",
            "    --latar: #ffffff",
            "    --garis: #dddddd",
            "    --teks: #222222",
            "    --jeda: 0.2s",
            "  .kartu-produk",
            "    background-color: var(--latar)",
            "    border: 1px solid var(--garis)",
            "    border-radius: 8px",
            "    color: var(--teks)",
            "    padding: 20px",
            "    transition: box-shadow var(--jeda) ease",
            "  .kartu-produk:hover",
            "    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15)",
            "  @media (prefers-reduced-motion: reduce)",
            "    .kartu-produk",
            "      transition: none",
        ],
        "hints": [
            "Variabel boleh dipakai di tengah nilai gabungan:",
            "  border: 1px solid var(--garis);",
            "Tulis rgba persis dengan spasi sesudah tiap koma:",
            "  rgba(0, 0, 0, 0.15) — koma di dalam kurung bukan pemisah "
            "deklarasi, jadi tidak perlu titik koma di dalamnya.",
            "prefers-reduced-motion: reduce menyala kalau orangnya sudah "
            "meminta sistemnya mengurangi gerak. Menghormatinya bukan fitur "
            "tambahan — bagi sebagian orang, gerak bikin pusing sungguhan.",
        ],
        "solution": """:root {
  --latar: #ffffff;
  --garis: #dddddd;
  --teks: #222222;
  --jeda: 0.2s;
}

.kartu-produk {
  background-color: var(--latar);
  border: 1px solid var(--garis);
  border-radius: 8px;
  color: var(--teks);
  padding: 20px;
  transition: box-shadow var(--jeda) ease;
}

.kartu-produk:hover {
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
}

@media (prefers-reduced-motion: reduce) {
  .kartu-produk {
    transition: none;
  }
}""",
    },
    {
        "title": "Latihan 13: Widget yang Bereaksi ke Wadahnya",
        "difficulty": "Menengah",
        "question": [
            "Buat CSS untuk sebuah widget yang tata letaknya berubah berdasarkan LEBAR",
            "WADAHNYA (bukan lebar layar), persis seperti materi 'Container Queries dan",
            "CSS Nesting'. Tulis aturan berikut, urut seperti ini:",
            "",
            "  1. .widget dengan container-type bernilai inline-size.",
            "  2. .widget .judul dengan font-size bernilai 1rem.",
            "  3. @container dengan syarat (min-width: 500px), isinya dua aturan:",
            "     a. .widget diberi display: grid dan",
            "        grid-template-columns: 1fr 1fr.",
            "     b. .widget .judul diberi font-size 1.25rem.",
            "",
            "CSS tidak dijalankan. Yang dinilai adalah STRUKTUR aturannya, hasil",
            "pembacaan struktur.py - persis seperti latihan CSS lainnya.",
            "",
            "Keluaran yang diharapkan:",
            "",
            ".widget",
            "  container-type: inline-size",
            ".widget .judul",
            "  font-size: 1rem",
            "@container (min-width: 500px)",
            "  .widget",
            "    display: grid",
            "    grid-template-columns: 1fr 1fr",
            "  .widget .judul",
            "    font-size: 1.25rem",
        ],
        "hints": [
            "container-type: inline-size ditulis di .widget, BUKAN di dalam @container.",
            "@container (min-width: 500px) { ... } - tanpa nama container, langsung "
            "syaratnya di dalam kurung, sama seperti @media.",
            "Urutan dua aturan di dalam @container mengikuti urutan di soal: .widget "
            "dulu (display + grid-template-columns), baru .widget .judul.",
        ],
        "solution": """.widget {
  container-type: inline-size;
}

.widget .judul {
  font-size: 1rem;
}

@container (min-width: 500px) {
  .widget {
    display: grid;
    grid-template-columns: 1fr 1fr;
  }

  .widget .judul {
    font-size: 1.25rem;
  }
}""",
    },
    {
        'title': 'Proyek Akhir: Sistem Gaya Warung Kopi',
        'difficulty': 'Sulit',
        'proyek': True,
        'question': [
        'STUDI KASUS -- Sistem Gaya Warung Kopi',
        '',
        'Halaman warung kopi sudah jadi dan strukturnya benar, tapi masih polos.',
        'Tulis SATU berkas gaya untuk seluruh halaman itu.',
        '',
        'Yang diuji bukan menghias, melainkan menyusun: nilai yang dipakai',
        'berulang tinggal di satu tempat, tata letak lahir dari flex dan grid',
        'bukan dari margin yang ditebak, dan layar sempit ditangani terakhir.',
        '',
        'Penilai mencetak aturanmu berurutan apa adanya -- urutan menulis',
        'properti TIDAK diurutkan, karena di CSS urutan menentukan siapa',
        'menimpa siapa.',
        '',
        'Yang harus ada di programmu:',
        '  1. Token warna dan jarak sebagai custom property di :root, lalu',
        '     dipakai lewat var() -- tidak ada warna mentah yang diulang.',
        '  2. box-sizing: border-box untuk semua elemen dan pseudo-elemennya.',
        '  3. header, main, dan footer dibatasi --baca dan ditengahkan dengan',
        '     margin auto kiri-kanan.',
        '  4. Navigasi: ul jadi flex, list-style dibuang, gap memakai token.',
        '  5. Tabel: border-collapse, garis bawah tiap sel, baris genap diberi',
        '     latar tipis dengan :nth-child(even), dan kolom TERAKHIR',
        '     dirata-kanan dengan font-variant-numeric: tabular-nums.',
        '  6. <dl> jadi grid dua kolom: max-content untuk istilah, 1fr untuk',
        '     penjelasannya.',
        '  7. Isian formulir memakai font: inherit -- tanpa itu input memakai',
        '     huruf bawaan sistem dan halamanmu terlihat tambal sulam.',
        '  8. Terakhir, @media (max-width: 480px): dl jadi satu kolom dan h1',
        '     mengecil. Blok media di PALING BAWAH berkas.',
        '',
        'Keluaran yang diharapkan:',
        '',
        '  :root',
        '    --teks: #23252b',
        '    --redup: #6b6f76',
        '    --aksen: #8a4b1f',
        '    --latar: #faf7f2',
        '    --garis: #e2ddd4',
        '    --jarak: 16px',
        '    --baca: 68ch',
        '  *, *::before, *::after',
        '    box-sizing: border-box',
        '  body',
        '    margin: 0',
        '    padding: var(--jarak)',
        '    background-color: var(--latar)',
        '    color: var(--teks)',
        '    font-family: system-ui, sans-serif',
        '    line-height: 1.6',
        '  header, main, footer',
        '    max-width: var(--baca)',
        '    margin-left: auto',
        '    margin-right: auto',
        '  h1',
        '    color: var(--aksen)',
        '    font-size: 2rem',
        '    line-height: 1.2',
        '  h2',
        '    margin-top: 40px',
        '    border-bottom: 2px solid var(--garis)',
        '    padding-bottom: 6px',
        '  nav ul',
        '    display: flex',
        '    flex-wrap: wrap',
        '    gap: var(--jarak)',
        '    margin: 0',
        '    padding: 0',
        '    list-style: none',
        '  nav a',
        '    color: var(--aksen)',
        '    text-decoration: none',
        '  nav a:hover',
        '    text-decoration: underline',
        '  table',
        '    width: 100%',
        '    border-collapse: collapse',
        '  th, td',
        '    border-bottom: 1px solid var(--garis)',
        '    padding: 10px 8px',
        '    text-align: left',
        '  tbody tr:nth-child(even)',
        '    background-color: rgba(0, 0, 0, 0.02)',
        '  tbody td:last-child',
        '    text-align: right',
        '    font-variant-numeric: tabular-nums',
        '  dl',
        '    display: grid',
        '    grid-template-columns: max-content 1fr',
        '    gap: 6px var(--jarak)',
        '  dd',
        '    margin: 0',
        '  input, select, textarea',
        '    width: 100%',
        '    border: 1px solid var(--garis)',
        '    border-radius: 6px',
        '    padding: 8px 10px',
        '    font: inherit',
        '  button',
        '    border: 0',
        '    border-radius: 6px',
        '    padding: 10px 18px',
        '    background-color: var(--aksen)',
        '    color: #ffffff',
        '    font: inherit',
        '    font-weight: 600',
        '    cursor: pointer',
        '  footer',
        '    margin-top: 48px',
        '    border-top: 1px solid var(--garis)',
        '    padding-top: var(--jarak)',
        '    color: var(--redup)',
        '  @media (max-width: 480px)',
        '    dl',
        '      grid-template-columns: 1fr',
        '    h1',
        '      font-size: 1.5rem',
    ],
        'hints': [
        "Selector bertumpuk ditulis dengan koma: 'header, main, footer { ... }' menghasilkan satu aturan untuk tiga elemen, bukan tiga aturan.",
        'tabular-nums membuat angka punya lebar sama, jadi kolom harga bisa dibandingkan sekilas tanpa perlu diratakan manual.',
        'Media query ditaruh terakhir karena spesifisitasnya sama dengan aturan biasa -- yang ditulis belakangan yang menang.',
    ],
        'solution': """/* Sistem Gaya Warung Kopi Pagi -- token, tata letak, tabel, formulir. */

:root {
  --teks: #23252b;
  --redup: #6b6f76;
  --aksen: #8a4b1f;
  --latar: #faf7f2;
  --garis: #e2ddd4;
  --jarak: 16px;
  --baca: 68ch;
}

*, *::before, *::after {
  box-sizing: border-box;
}

body {
  margin: 0;
  padding: var(--jarak);
  background-color: var(--latar);
  color: var(--teks);
  font-family: system-ui, sans-serif;
  line-height: 1.6;
}

header, main, footer {
  max-width: var(--baca);
  margin-left: auto;
  margin-right: auto;
}

h1 {
  color: var(--aksen);
  font-size: 2rem;
  line-height: 1.2;
}

h2 {
  margin-top: 40px;
  border-bottom: 2px solid var(--garis);
  padding-bottom: 6px;
}

nav ul {
  display: flex;
  flex-wrap: wrap;
  gap: var(--jarak);
  margin: 0;
  padding: 0;
  list-style: none;
}

nav a {
  color: var(--aksen);
  text-decoration: none;
}

nav a:hover {
  text-decoration: underline;
}

table {
  width: 100%;
  border-collapse: collapse;
}

th, td {
  border-bottom: 1px solid var(--garis);
  padding: 10px 8px;
  text-align: left;
}

tbody tr:nth-child(even) {
  background-color: rgba(0, 0, 0, 0.02);
}

tbody td:last-child {
  text-align: right;
  font-variant-numeric: tabular-nums;
}

dl {
  display: grid;
  grid-template-columns: max-content 1fr;
  gap: 6px var(--jarak);
}

dd {
  margin: 0;
}

input, select, textarea {
  width: 100%;
  border: 1px solid var(--garis);
  border-radius: 6px;
  padding: 8px 10px;
  font: inherit;
}

button {
  border: 0;
  border-radius: 6px;
  padding: 10px 18px;
  background-color: var(--aksen);
  color: #ffffff;
  font: inherit;
  font-weight: 600;
  cursor: pointer;
}

footer {
  margin-top: 48px;
  border-top: 1px solid var(--garis);
  padding-top: var(--jarak);
  color: var(--redup);
}

@media (max-width: 480px) {
  dl {
    grid-template-columns: 1fr;
  }

  h1 {
    font-size: 1.5rem;
  }
}
""",
    },
]
