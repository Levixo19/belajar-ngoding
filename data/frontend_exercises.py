"""Kurikulum Frontend Modern.

Dirakit alat/rakit_kurikulum.py dari draf per bab (2026-10-19).
Sesudah dirakit, berkas ini disunting seperti kurikulum lain
(alat/ganti_badan.py, alat/tambah_bagian.py). <KEY>_BAB tetap
spesifikasi JUMLAH; rentangnya dihitung data/kurikulum_tech.py.
"""

FRONTEND_EXERCISES = [
    {
        "title": "Latihan 1: Penyelesai Rentang Semver",
        "difficulty": "Mudah",
        "question": [
            "Tulis program yang memilih versi paket seperti npm.",
            "",
            "Baris pertama input adalah rentang versi, salah satu dari tiga",
            "bentuk: ^1.2.0, ~1.2.0, atau versi persis seperti 2.1.0. Baris",
            "berikutnya daftar versi yang tersedia di registri, satu per baris.",
            "",
            "Cetak versi tertinggi yang cocok dengan rentang, atau tidak ada",
            "kalau nggak ada yang cocok. Aturannya:",
            "  - ^X.Y.Z: minimal X.Y.Z dan mayornya sama. Kalau X = 0, minornya",
            "    juga harus sama. Kalau X dan Y sama-sama 0, patch-nya harus sama.",
            "  - ~X.Y.Z: minimal X.Y.Z, mayor dan minornya sama.",
            "  - Tanpa awalan: harus persis sama.",
            "",
            "Versi dibandingkan per angka: 1.10.3 lebih tinggi dari 1.4.7.",
            "",
            "Untuk input ^1.2.0, keluarannya:",
            "1.10.3",
            "",
            "Untuk input ~1.2.0, keluarannya:",
            "1.2.11",
            "",
            "Untuk input ^0.3.1, keluarannya:",
            "tidak ada",
        ],
        "hints": [
            "Pecah tiap versi jadi tiga angka dengan split('.') dan Number, karena membandingkan teks membuat 1.10 dianggap lebih kecil dari 1.4.",
            "Buat fungsi cocok(versi, rentang) yang mengecek awalan ^, ~, atau tanpa awalan, lalu simpan versi tertinggi yang lolos.",
            "Fungsi banding(a, b) yang mengembalikan selisih angka pertama yang berbeda bisa dipakai untuk 'minimal X.Y.Z' sekaligus untuk mencari yang tertinggi.",
        ],
        "solution": "const baris = require('fs').readFileSync(0, 'utf8').trim().split('\\n');\nconst rentang = baris[0].trim();\nconst daftar = baris.slice(1).map((b) => b.trim()).filter((b) => b !== '');\n\nfunction urai(v) {\n  return v.split('.').map(Number);\n}\n\nfunction banding(a, b) {\n  for (let i = 0; i < 3; i++) {\n    if (a[i] !== b[i]) return a[i] - b[i];\n  }\n  return 0;\n}\n\nfunction cocok(versi, rentang) {\n  const v = urai(versi);\n  if (rentang.startsWith('^')) {\n    const r = urai(rentang.slice(1));\n    if (banding(v, r) < 0) return false;\n    if (r[0] > 0) return v[0] === r[0];\n    if (r[1] > 0) return v[0] === 0 && v[1] === r[1];\n    return v[0] === 0 && v[1] === 0 && v[2] === r[2];\n  }\n  if (rentang.startsWith('~')) {\n    const r = urai(rentang.slice(1));\n    return banding(v, r) >= 0 && v[0] === r[0] && v[1] === r[1];\n  }\n  return banding(v, urai(rentang)) === 0;\n}\n\nlet terbaik = null;\nfor (const versi of daftar) {\n  if (!cocok(versi, rentang)) continue;\n  if (terbaik === null || banding(urai(versi), urai(terbaik)) > 0) {\n    terbaik = versi;\n  }\n}\nconsole.log(terbaik === null ? 'tidak ada' : terbaik);\n",
        "stdin_list": [
            """^1.2.0
1.1.9
1.2.0
1.10.3
1.4.7
2.0.0
""",
            """~1.2.0
1.2.0
1.2.11
1.3.0
1.2.9
""",
            """^0.3.1
0.3.0
0.4.2
1.0.0
""",
            """2.1.0
2.0.9
2.1.1
2.1.0
""",
        ],
    },
    {
        "title": "Latihan 2: Kalkulator Kontras WCAG",
        "difficulty": "Mudah",
        "question": [
            "Tulis program yang menilai kontras dua warna.",
            "",
            "Input satu baris berisi dua warna hex dipisah spasi: warna teks",
            "lalu warna latar. Warna bisa enam digit (#777777) atau tiga digit",
            "(#fff, artinya #ffffff).",
            "",
            "Hitung luminans relatif tiap warna dan rasio kontrasnya seperti di",
            "materi, cetak rasionya dengan dua angka di belakang titik, lalu",
            "nilai empat ambang: teks normal AA (4.5), teks normal AAA (7), teks",
            "besar AA (3), dan teks besar AAA (4.5).",
            "",
            "Bandingkan rasio yang belum dibulatkan. Rasio #959595 di atas",
            "putih tertulis 3.00 setelah dibulatkan, padahal aslinya sedikit di",
            "bawah 3, jadi tetap gagal.",
            "",
            "Untuk input #777777 #ffffff, keluarannya:",
            "rasio: 4.48:1",
            "teks normal AA: gagal",
            "teks normal AAA: gagal",
            "teks besar AA: lulus",
            "teks besar AAA: gagal",
            "",
            "Untuk input #959595 #fff, keluarannya:",
            "rasio: 3.00:1",
            "teks normal AA: gagal",
            "teks normal AAA: gagal",
            "teks besar AA: gagal",
            "teks besar AAA: gagal",
        ],
        "hints": [
            "Luminans relatif dihitung per kanal warna: ubah tiap kanal ke 0-1, linearkan, lalu jumlahkan dengan bobot 0.2126, 0.7152, dan 0.0722.",
            "Untuk hex tiga digit, gandakan tiap hurufnya dulu supaya jadi enam digit, lalu ambil pasangan huruf dengan slice dan parseInt berbasis 16.",
            "Simpan rasio sebagai angka mentah untuk dibandingkan dengan ambang, dan pakai toFixed(2) hanya saat mencetak.",
        ],
        "solution": "const [a, b] = require('fs').readFileSync(0, 'utf8').trim().split(/\\s+/);\n\nfunction keRgb(hex) {\n  let h = hex.replace('#', '');\n  if (h.length === 3) h = h.split('').map((c) => c + c).join('');\n  return [0, 2, 4].map((i) => parseInt(h.slice(i, i + 2), 16));\n}\n\nfunction luminans(hex) {\n  const [r, g, b] = keRgb(hex).map((n) => {\n    const c = n / 255;\n    return c <= 0.04045 ? c / 12.92 : ((c + 0.055) / 1.055) ** 2.4;\n  });\n  return 0.2126 * r + 0.7152 * g + 0.0722 * b;\n}\n\nconst l1 = luminans(a);\nconst l2 = luminans(b);\nconst rasio = (Math.max(l1, l2) + 0.05) / (Math.min(l1, l2) + 0.05);\n\nconst nilai = (ambang) => (rasio >= ambang ? 'lulus' : 'gagal');\nconsole.log(`rasio: ${rasio.toFixed(2)}:1`);\nconsole.log(`teks normal AA: ${nilai(4.5)}`);\nconsole.log(`teks normal AAA: ${nilai(7)}`);\nconsole.log(`teks besar AA: ${nilai(3)}`);\nconsole.log(`teks besar AAA: ${nilai(4.5)}`);\n",
        "stdin_list": [
            """#777777 #ffffff
""",
            """#fff #0055ff
""",
            """#959595 #fff
""",
        ],
    },
    {
        "title": "Latihan 3: Penghitung Nama Aksesibel",
        "difficulty": "Menengah",
        "question": [
            "Input adalah pohon elemen dalam bentuk JSON. Setiap elemen punya",
            "tag, attr (objek atribut, boleh tidak ada), dan anak (daftar yang",
            "isinya teks atau elemen lain, boleh tidak ada).",
            "",
            "Telusuri pohon dari atas ke bawah. Untuk setiap elemen interaktif",
            "atau gambar, cetak peran dan namanya dengan format peran: nama.",
            "Peran: button -> button, a -> link, input -> textbox, img -> img.",
            "Gambar dengan alt=\"\" adalah hiasan: lewati, jangan dicetak.",
            "",
            "Nama dihitung dengan urutan ini; sumber pertama yang berisi dipakai:",
            "  1. aria-labelledby: teks isi elemen yang id-nya disebut (boleh",
            "     lebih dari satu id, dipisah spasi; id yang tidak ada dilewati).",
            "  2. aria-label.",
            "  3. img: atribut alt. input: teks label yang for-nya sama dengan",
            "     id input itu.",
            "  4. button dan a: teks isinya. Gambar di dalamnya menyumbang alt.",
            "  5. atribut title.",
            "",
            "Teks isi digabung dengan spasi, lalu spasi berlebih dirapikan.",
            "Kalau namanya kosong, cetak (kosong) <- perbaiki. Di akhir, cetak",
            "jumlah elemen tanpa nama.",
            "",
            "Keluaran yang diharapkan:",
            "textbox: Kata kunci",
            "textbox: (kosong) <- perbaiki",
            "button: Cari produk",
            "button: Tutup",
            "link: Keranjang (3)",
            "img: Keranjang",
            "img: (kosong) <- perbaiki",
            "button: Bagikan",
            "button: (kosong) <- perbaiki",
            "elemen tanpa nama: 3",
        ],
        "hints": [
            "Kumpulkan semua elemen ke satu array dulu dengan penelusuran rekursif, supaya elemen yang dirujuk id atau label for bisa dicari dari mana saja.",
            "Buat fungsi teksIsi(el) yang menggabungkan teks anak secara rekursif, mengambil alt untuk anak img, lalu merapikan spasi.",
            "Tulis namaAksesibel(el) sebagai deretan if yang langsung return begitu satu sumber menghasilkan teks yang tidak kosong.",
        ],
        "solution": "const akar = JSON.parse(require('fs').readFileSync(0, 'utf8'));\n\nconst PERAN = { button: 'button', a: 'link', input: 'textbox', img: 'img' };\n\n// Kumpulkan semua elemen sekali, supaya id dan label bisa dicari.\nconst semua = [];\n(function jelajah(el) {\n  semua.push(el);\n  for (const anak of el.anak || []) {\n    if (typeof anak !== 'string') jelajah(anak);\n  }\n})(akar);\n\nconst atribut = (el, nama) => (el.attr || {})[nama];\n\nfunction teksIsi(el) {\n  const bagian = [];\n  for (const anak of el.anak || []) {\n    if (typeof anak === 'string') bagian.push(anak);\n    else if (anak.tag === 'img') bagian.push(atribut(anak, 'alt') || '');\n    else bagian.push(teksIsi(anak));\n  }\n  return bagian.join(' ').replace(/\\s+/g, ' ').trim();\n}\n\nfunction namaAksesibel(el) {\n  const rujukan = atribut(el, 'aria-labelledby');\n  if (rujukan) {\n    const teks = rujukan.split(/\\s+/)\n      .map((id) => semua.find((x) => atribut(x, 'id') === id))\n      .filter(Boolean)\n      .map(teksIsi)\n      .join(' ')\n      .trim();\n    if (teks) return teks;\n  }\n  const label = (atribut(el, 'aria-label') || '').trim();\n  if (label) return label;\n  if (el.tag === 'img') return (atribut(el, 'alt') || '').trim();\n  if (el.tag === 'input') {\n    const id = atribut(el, 'id');\n    const lbl = semua.find((x) => x.tag === 'label' && atribut(x, 'for') === id);\n    if (id && lbl) return teksIsi(lbl);\n  }\n  if (el.tag === 'button' || el.tag === 'a') {\n    const isi = teksIsi(el);\n    if (isi) return isi;\n  }\n  return (atribut(el, 'title') || '').trim();\n}\n\nlet kosong = 0;\nfor (const el of semua) {\n  if (!PERAN[el.tag]) continue;\n  // alt=\"\" artinya hiasan: dilewati pembaca layar, jadi bukan masalah.\n  if (el.tag === 'img' && atribut(el, 'alt') === '') continue;\n  const nama = namaAksesibel(el);\n  if (!nama) kosong++;\n  console.log(`${PERAN[el.tag]}: ${nama || '(kosong) <- perbaiki'}`);\n}\nconsole.log(`elemen tanpa nama: ${kosong}`);\n",
        "stdin_list": [
            """{"tag": "form", "anak": [
  {"tag": "h2", "attr": {"id": "judul-cari"}, "anak": ["Cari produk"]},
  {"tag": "label", "attr": {"for": "kata"}, "anak": ["Kata kunci"]},
  {"tag": "input", "attr": {"id": "kata"}},
  {"tag": "input", "attr": {"id": "kota"}},
  {"tag": "button", "attr": {"aria-labelledby": "judul-cari"}, "anak": [
    {"tag": "img", "attr": {"src": "kaca.svg", "alt": ""}}]},
  {"tag": "button", "attr": {"aria-label": "Tutup"}, "anak": ["X"]},
  {"tag": "a", "attr": {"href": "/keranjang"}, "anak": [
    {"tag": "img", "attr": {"src": "troli.svg", "alt": "Keranjang"}}, " (3)"]},
  {"tag": "img", "attr": {"src": "promo.jpg"}},
  {"tag": "button", "attr": {"title": "Bagikan"}},
  {"tag": "button", "anak": [{"tag": "span", "attr": {"class": "ikon"}}]}
]}
""",
            """{"tag": "nav", "anak": [
  {"tag": "a", "attr": {"href": "/"}, "anak": ["Beranda"]},
  {"tag": "a", "attr": {"href": "/promo", "aria-label": "Promo minggu ini"}, "anak": ["Lihat"]},
  {"tag": "a", "attr": {"href": "/akun"}, "anak": [{"tag": "img", "attr": {"src": "akun.svg"}}]},
  {"tag": "span", "attr": {"id": "lbl-menu"}, "anak": ["Menu", "utama"]},
  {"tag": "button", "attr": {"aria-labelledby": "lbl-menu tidak-ada"}, "anak": ["="]}
]}
""",
        ],
    },
    {
        "title": "Latihan 4: Virtual DOM Mini dengan Diff",
        "difficulty": "Menengah",
        "question": [
            "Bangun tiga fungsi yang akan dipakai lagi di proyek akhir:",
            "  - h(tag, props, ...anak): kembalikan { tag, props, anak }. props",
            "    null jadi {}. Anak yang berupa angka diubah jadi teks, anak null",
            "    dan false dibuang, dan array di dalam anak diratakan.",
            "  - renderToString(simpul): ubah simpul jadi HTML. Escape &, <, >,",
            "    dan tanda kutip ganda di teks maupun nilai atribut.",
            "  - diff(lama, baru): kembalikan daftar patch berupa teks.",
            "",
            "Aturan diff, dimulai dari akar dengan jalur 0. Anak ke-i dari simpul",
            "berjalur J punya jalur J.i:",
            "  - simpul lama tidak ada: TAMBAH  jalur <tag> (atau teks berkutip)",
            "  - simpul baru tidak ada: HAPUS   jalur <tag>",
            "  - dua-duanya teks dan beda: TEKS    jalur \"lama\" -> \"baru\"",
            "  - jenis atau tag beda: GANTI   jalur <lama> -> <baru>, tanpa",
            "    membandingkan anak-anaknya",
            "  - tag sama: periksa atribut dalam urutan abjad nama atribut,",
            "    ATRIBUT jalur nama: nilaiLama -> nilaiBaru (nilai ditulis",
            "    berkutip, atau (tidak ada)), lalu bandingkan anak satu per satu",
            "    menurut posisi.",
            "Nama patch diratakan ke kiri dengan lebar 8 huruf (TEKS diikuti",
            "empat spasi).",
            "",
            "Pakai komponen Item({ nama, selesai }) yang menghasilkan li dengan",
            "class selesai atau tugas. Pohon lama: section berisi h2 \"Tugas hari",
            "ini\" dan ul dengan tiga Item belum selesai: Beli kopi, Cuci motor,",
            "Bayar listrik. Pohon baru: section id=\"utama\" berisi h2 \"Tugas",
            "<hari> ini\", ul dengan Item Beli kopi (selesai) dan Cuci mobil, lalu",
            "p \"1 dari 2 selesai\".",
            "",
            "Cetak renderToString dari h2 pohon baru, renderToString dari",
            "Item({ nama: 'Beli kopi', selesai: true }), semua patch, lalu",
            "jumlahnya.",
            "",
            "Keluaran yang diharapkan:",
            "<h2>Tugas &lt;hari&gt; ini</h2>",
            "<li class=\"selesai\">Beli kopi</li>",
            "ATRIBUT 0 id: (tidak ada) -> \"utama\"",
            "TEKS    0.0.0 \"Tugas hari ini\" -> \"Tugas <hari> ini\"",
            "ATRIBUT 0.1.0 class: \"tugas\" -> \"selesai\"",
            "TEKS    0.1.1.0 \"Cuci motor\" -> \"Cuci mobil\"",
            "HAPUS   0.1.2 <li>",
            "TAMBAH  0.2 <p>",
            "6 patch",
        ],
        "hints": [
            "Teks dan elemen dibedakan dengan typeof simpul === 'string', jadi pastikan h() mengubah angka jadi String sejak awal.",
            "diff paling mudah ditulis rekursif dengan parameter jalur dan satu array patch yang diisi bersama, lalu dicek berurutan: lama tidak ada, baru tidak ada, dua teks, jenis atau tag beda, sisanya tag sama.",
            "Untuk atribut, gabungkan kunci props lama dan baru dengan new Set, urutkan, lalu bandingkan nilainya; JSON.stringify(String(v)) menghasilkan nilai berkutip.",
        ],
        "solution": """function h(tag, props, ...anak) {
  return {
    tag,
    props: props || {},
    anak: anak.flat().filter((a) => a !== null && a !== false)
      .map((a) => (typeof a === 'object' ? a : String(a))),
  };
}

function escape(teks) {
  return teks.replace(/&/g, '&amp;').replace(/</g, '&lt;')
    .replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}

function renderToString(simpul) {
  if (typeof simpul === 'string') return escape(simpul);
  const attr = Object.keys(simpul.props)
    .map((k) => ` ${k}="${escape(String(simpul.props[k]))}"`).join('');
  const isi = simpul.anak.map(renderToString).join('');
  return `<${simpul.tag}${attr}>${isi}</${simpul.tag}>`;
}

function label(simpul) {
  return typeof simpul === 'string' ? JSON.stringify(simpul) : `<${simpul.tag}>`;
}

function diff(lama, baru, jalur = '0', patch = []) {
  if (lama === undefined) {
    patch.push(`TAMBAH  ${jalur} ${label(baru)}`);
  } else if (baru === undefined) {
    patch.push(`HAPUS   ${jalur} ${label(lama)}`);
  } else if (typeof lama === 'string' && typeof baru === 'string') {
    if (lama !== baru) patch.push(`TEKS    ${jalur} ${label(lama)} -> ${label(baru)}`);
  } else if (typeof lama === 'string' || typeof baru === 'string'
             || lama.tag !== baru.tag) {
    patch.push(`GANTI   ${jalur} ${label(lama)} -> ${label(baru)}`);
  } else {
    const kunci = [...new Set([...Object.keys(lama.props), ...Object.keys(baru.props)])];
    for (const k of kunci.sort()) {
      const a = lama.props[k];
      const b = baru.props[k];
      if (a === b) continue;
      const tulis = (v) => (v === undefined ? '(tidak ada)' : JSON.stringify(String(v)));
      patch.push(`ATRIBUT ${jalur} ${k}: ${tulis(a)} -> ${tulis(b)}`);
    }
    const n = Math.max(lama.anak.length, baru.anak.length);
    for (let i = 0; i < n; i++) {
      diff(lama.anak[i], baru.anak[i], `${jalur}.${i}`, patch);
    }
  }
  return patch;
}

function Item({ nama, selesai }) {
  return h('li', { class: selesai ? 'selesai' : 'tugas' }, nama);
}

function Daftar(tugas, judul) {
  return h('section', null,
    h('h2', null, judul),
    h('ul', null, tugas.map((t) => Item(t))));
}

const lama = Daftar([
  { nama: 'Beli kopi', selesai: false },
  { nama: 'Cuci motor', selesai: false },
  { nama: 'Bayar listrik', selesai: false },
], 'Tugas hari ini');

const baru = h('section', { id: 'utama' },
  h('h2', null, 'Tugas <hari> ini'),
  h('ul', null,
    Item({ nama: 'Beli kopi', selesai: true }),
    Item({ nama: 'Cuci mobil', selesai: false })),
  h('p', null, '1 dari 2 selesai'));

console.log(renderToString(baru.anak[0]));
console.log(renderToString(Item({ nama: 'Beli kopi', selesai: true })));
const patch = diff(lama, baru);
for (const p of patch) console.log(p);
console.log(`${patch.length} patch`);
""",
    },
    {
        "title": "Latihan 5: Signal Mini dengan Efek Otomatis",
        "difficulty": "Menengah",
        "question": [
            "Bangun signal, effect, dan computed dengan pelacakan dependensi",
            "otomatis, lalu buktikan tiga sifat di bawah dengan skenario tetap.",
            "",
            "  1. Setter signal tidak menjalankan apa pun kalau nilai baru sama",
            "     dengan nilai lama (bandingkan dengan Object.is).",
            "  2. computed adalah effect yang menulis ke signal internal, jadi",
            "     pembacanya cuma jalan ulang kalau hasil hitungannya berubah.",
            "  3. Setiap kali effect jalan ulang, langganan lamanya dilepas dan",
            "     dependensinya dicatat ulang. Signal yang tidak lagi dibaca",
            "     tidak boleh memicu effect itu.",
            "",
            "Skenario: harga = 10000, jumlah = 2, diskon = 0. total = harga x",
            "jumlah - diskon, mahal = total >= 50000. Effect pertama mencetak",
            "total, effect kedua mencetak label mahal atau murah. Lalu ubah",
            "jumlah = 3, jumlah = 3 lagi, harga = 20000, diskon = 10000.",
            "Sesudah itu buat effect sapaan yang membaca nama hanya kalau tampil",
            "bernilai true, lalu ubah nama = Budi, tampil = false, nama = Citra.",
            "Setiap baris dari effect diawali dua spasi dan [efek]. Urutan",
            "effect yang berjalan mengikuti urutan berlangganan.",
            "",
            "Keluaran yang diharapkan:",
            "  [efek] total: 20000",
            "  [efek] label: murah",
            "jumlah = 3",
            "  [efek] total: 30000",
            "jumlah = 3 lagi",
            "harga = 20000",
            "  [efek] label: mahal",
            "  [efek] total: 60000",
            "diskon = 10000",
            "  [efek] total: 50000",
            "  [efek] sapaan: Halo, Sari",
            "nama = Budi",
            "  [efek] sapaan: Halo, Budi",
            "tampil = false",
            "  [efek] sapaan: (tersembunyi)",
            "nama = Citra",
            "efek total 4x, label 2x, sapaan 3x",
        ],
        "hints": [
            "Satu variabel global yang menunjuk effect yang sedang berjalan sudah cukup untuk mencatat siapa membaca signal mana.",
            "Simpan di setiap effect himpunan sumber, yaitu daftar pelanggan signal yang pernah ia masuki, supaya sebelum jalan ulang effect bisa menghapus dirinya dari semua daftar itu.",
            "Saat setter memanggil pelanggan, ulangi salinan himpunannya ([...pelanggan]) karena effect yang berjalan akan menghapus dan menambah dirinya lagi ke himpunan yang sama.",
        ],
        "solution": """let efekAktif = null;

function signal(awal) {
  let nilai = awal;
  const pelanggan = new Set();
  return {
    get value() {
      if (efekAktif) {
        pelanggan.add(efekAktif);
        efekAktif.sumber.add(pelanggan);
      }
      return nilai;
    },
    set value(baru) {
      if (Object.is(baru, nilai)) return; // nilai sama: nggak ada yang perlu jalan
      nilai = baru;
      for (const efek of [...pelanggan]) efek.jalankan();
    },
  };
}

function effect(fn) {
  const efek = {
    sumber: new Set(),
    jalankan() {
      // Lepas langganan lama; dependensi dicatat ulang tiap kali berjalan.
      for (const daftar of efek.sumber) daftar.delete(efek);
      efek.sumber.clear();
      const sebelumnya = efekAktif;
      efekAktif = efek;
      try {
        fn();
      } finally {
        efekAktif = sebelumnya;
      }
    },
  };
  efek.jalankan();
}

function computed(fn) {
  const hasil = signal(undefined);
  effect(() => {
    hasil.value = fn();
  });
  return {
    get value() {
      return hasil.value;
    },
  };
}

const hitung = { total: 0, label: 0, sapaan: 0 };
const harga = signal(10000);
const jumlah = signal(2);
const diskon = signal(0);
const total = computed(() => harga.value * jumlah.value - diskon.value);
const mahal = computed(() => total.value >= 50000);

effect(() => {
  hitung.total++;
  console.log(`  [efek] total: ${total.value}`);
});
effect(() => {
  hitung.label++;
  console.log(`  [efek] label: ${mahal.value ? 'mahal' : 'murah'}`);
});

const langkah = [
  ['jumlah = 3', () => { jumlah.value = 3; }],
  ['jumlah = 3 lagi', () => { jumlah.value = 3; }],
  ['harga = 20000', () => { harga.value = 20000; }],
  ['diskon = 10000', () => { diskon.value = 10000; }],
];
for (const [teks, ubah] of langkah) {
  console.log(teks);
  ubah();
}

const tampil = signal(true);
const nama = signal('Sari');
effect(() => {
  hitung.sapaan++;
  console.log(`  [efek] sapaan: ${tampil.value ? 'Halo, ' + nama.value : '(tersembunyi)'}`);
});
console.log('nama = Budi');
nama.value = 'Budi';
console.log('tampil = false');
tampil.value = false;
console.log('nama = Citra');
nama.value = 'Citra';

console.log(`efek total ${hitung.total}x, label ${hitung.label}x, sapaan ${hitung.sapaan}x`);
""",
    },
    {
        "title": "Latihan 6: Generator Kelas Utility ala Tailwind",
        "difficulty": "Menengah",
        "question": [
            "Tulis generator CSS mini yang bekerja seperti Tailwind: baca HTML",
            "dari input, kumpulkan isi semua atribut class=\"...\", lalu buat CSS",
            "hanya untuk kelas yang dikenali. Kelas yang sama cukup dihitung",
            "sekali.",
            "",
            "Kelas yang dikenali (N adalah bilangan bulat, nilainya N x 0.25rem):",
            "  - p-N -> padding, m-N -> margin, px-N -> padding-inline,",
            "    gap-N -> gap. Contoh: p-4 -> padding: 1rem; m-0 -> margin: 0rem",
            "  - flex -> display: flex",
            "  - text-center -> text-align: center",
            "  - font-bold -> font-weight: 700",
            "  - awalan md: pada kelas mana pun di atas. Aturannya masuk ke satu",
            "    blok @media (min-width: 48rem), dan titik dua di pemilihnya",
            "    di-escape: .md\\:flex",
            "Kelas lain diabaikan.",
            "",
            "Format keluaran: baris komentar berisi jumlah kelas dikenal dan",
            "diabaikan, lalu aturan tanpa awalan diurutkan abjad, satu per baris,",
            "lalu blok @media berisi aturan md: yang juga diurutkan abjad dan",
            "menjorok dua spasi. Kalau tidak ada kelas md:, blok @media tidak",
            "dicetak.",
            "",
            "Contoh input:",
            "  <div class=\"p-4 md:flex md:gap-6\">",
            "    <img class=\"rounded\" src=\"kopi.jpg\" alt=\"Kopi susu\">",
            "    <div class=\"px-2 md:p-8\">",
            "      <h2 class=\"font-bold text-center\">Kopi Susu</h2>",
            "      <p class=\"m-0 text-gray-600\">Rp18.000</p>",
            "      <button class=\"px-2 font-bold\">Beli</button>",
            "    </div>",
            "  </div>",
            "",
            "Keluaran yang diharapkan:",
            "/* 8 kelas dikenal, 2 diabaikan */",
            ".font-bold { font-weight: 700; }",
            ".m-0 { margin: 0rem; }",
            ".p-4 { padding: 1rem; }",
            ".px-2 { padding-inline: 0.5rem; }",
            ".text-center { text-align: center; }",
            "@media (min-width: 48rem) {",
            "  .md\\:flex { display: flex; }",
            "  .md\\:gap-6 { gap: 1.5rem; }",
            "  .md\\:p-8 { padding: 2rem; }",
            "}",
        ],
        "hints": [
            "Langkah pertama cuma mengumpulkan kelas: regex /class=\"([^\"]*)\"/g dengan matchAll, pecah isinya per spasi, simpan di Set supaya kembarannya hilang.",
            "Pisahkan urusan awalan dari urusan terjemahan: buang md: dulu, terjemahkan sisanya dengan satu fungsi yang mengembalikan deklarasi atau null.",
            "Kumpulkan aturan ke dua array (dasar dan md), urutkan masing-masing dengan sort(), dan escape titik dua dengan k.replace(':', '\\\\:').",
        ],
        "solution": "const html = require('fs').readFileSync(0, 'utf8');\n\n// Kumpulkan isi semua atribut class, pecah per spasi, buang yang kembar.\nconst kelas = new Set();\nfor (const cocok of html.matchAll(/class=\"([^\"]*)\"/g)) {\n  for (const k of cocok[1].split(/\\s+/)) {\n    if (k) kelas.add(k);\n  }\n}\n\nconst SKALA = {\n  p: ['padding'],\n  m: ['margin'],\n  px: ['padding-inline'],\n  gap: ['gap'],\n};\nconst TETAP = {\n  flex: 'display: flex',\n  'text-center': 'text-align: center',\n  'font-bold': 'font-weight: 700',\n};\n\nfunction deklarasi(nama) {\n  if (TETAP[nama]) return TETAP[nama];\n  const cocok = nama.match(/^(p|m|px|gap)-(\\d+)$/);\n  if (!cocok) return null;\n  const nilai = `${Number(cocok[2]) * 0.25}rem`;\n  return SKALA[cocok[1]].map((prop) => `${prop}: ${nilai}`).join('; ');\n}\n\nconst dasar = [];\nconst md = [];\nlet diabaikan = 0;\nfor (const k of kelas) {\n  const responsif = k.startsWith('md:');\n  const isi = deklarasi(responsif ? k.slice(3) : k);\n  if (!isi) {\n    diabaikan++;\n    continue;\n  }\n  const pemilih = '.' + k.replace(':', '\\\\:');\n  (responsif ? md : dasar).push(`${pemilih} { ${isi}; }`);\n}\n\nconsole.log(`/* ${dasar.length + md.length} kelas dikenal, ${diabaikan} diabaikan */`);\nfor (const aturan of dasar.sort()) console.log(aturan);\nif (md.length) {\n  console.log('@media (min-width: 48rem) {');\n  for (const aturan of md.sort()) console.log('  ' + aturan);\n  console.log('}');\n}\n",
        "stdin_list": [
            """<div class="p-4 md:flex md:gap-6">
  <img class="rounded" src="kopi.jpg" alt="Kopi susu">
  <div class="px-2 md:p-8">
    <h2 class="font-bold text-center">Kopi Susu</h2>
    <p class="m-0 text-gray-600">Rp18.000</p>
    <button class="px-2 font-bold">Beli</button>
  </div>
</div>
""",
            """<nav class="flex gap-3 p-2">
  <a class="px-1" href="/">Beranda</a>
  <a class="px-1 md:px-10" href="/promo">Promo</a>
</nav>
""",
        ],
    },
    {
        "title": "Latihan 7: Bundler Mini dari Graf Modul",
        "difficulty": "Menengah",
        "question": [
            "Buat bundler mini untuk modul CommonJS. Modulnya disimpan sebagai",
            "objek teks, salin persis seperti ini ke programmu:",
            "",
            "  const modul = {",
            "    'main.js':",
            "      \"const sapa = require('./sapa.js');\\n\" +",
            "      \"const mat = require('./mat.js');\\n\" +",
            "      \"console.log(sapa('Rina'));\\n\" +",
            "      \"console.log('2 x 3 =', mat.kali(2, 3));\",",
            "    'sapa.js':",
            "      \"const huruf = require('./huruf.js');\\n\" +",
            "      \"module.exports = (nama) => 'Halo, ' + huruf.besar(nama) + '!';\",",
            "    'mat.js': \"exports.kali = (a, b) => a * b;\",",
            "    'huruf.js': \"exports.besar = (s) => s.toUpperCase();\",",
            "    'lama.js': \"console.log('ini nggak boleh muncul');\",",
            "  };",
            "",
            "Langkahnya:",
            "  1. Mulai dari main.js, temukan semua require('./...') di tiap modul.",
            "  2. Susun urutan modul dengan penelusuran mendalam: kunjungi dulu",
            "     semua dependensi sebuah modul (sesuai urutan require-nya), baru",
            "     catat modul itu. Modul yang sudah dikunjungi dilewati.",
            "  3. Cetak urutannya, lalu modul yang tidak terjangkau.",
            "  4. Rakit bundel: tiap modul dibungkus fungsi",
            "     (module, exports, require) dan dimuat lewat fungsi muat yang",
            "     punya cache. Jalankan bundelnya.",
            "",
            "Keluaran yang diharapkan:",
            "Urutan modul:",
            "  1. huruf.js",
            "  2. sapa.js",
            "  3. mat.js",
            "  4. main.js",
            "Tidak masuk bundel: lama.js",
            "--- menjalankan bundel ---",
            "Halo, RINA!",
            "2 x 3 = 6",
        ],
        "hints": [
            "Graf modul ditelusuri dari entry, dan sebuah modul baru boleh dicatat sesudah semua modul yang ia butuhkan tercatat.",
            "Pakai Set untuk modul yang sudah dikunjungi, fungsi rekursif kunjungi(nama), dan matchAll dengan regex /require\\('\\.\\/([^']+)'\\)/g untuk mencari dependensi.",
            "Bundelnya cukup berupa teks: objek definisi berisi fungsi per modul, lalu fungsi muat(nama) yang membuat { exports: {} }, menyimpannya di cache, memanggil definisinya, dan mengembalikan module.exports; jalankan teks itu dengan new Function(bundel)().",
        ],
        "solution": "const modul = {\n  'main.js':\n    \"const sapa = require('./sapa.js');\\n\" +\n    \"const mat = require('./mat.js');\\n\" +\n    \"console.log(sapa('Rina'));\\n\" +\n    \"console.log('2 x 3 =', mat.kali(2, 3));\",\n  'sapa.js':\n    \"const huruf = require('./huruf.js');\\n\" +\n    \"module.exports = (nama) => 'Halo, ' + huruf.besar(nama) + '!';\",\n  'mat.js': \"exports.kali = (a, b) => a * b;\",\n  'huruf.js': \"exports.besar = (s) => s.toUpperCase();\",\n  'lama.js': \"console.log('ini nggak boleh muncul');\",\n};\n\nfunction cariRequire(kode) {\n  const hasil = [];\n  for (const m of kode.matchAll(/require\\('\\.\\/([^']+)'\\)/g)) hasil.push(m[1]);\n  return hasil;\n}\n\n// Urutan pasca-kunjungan: dependensi selalu ditulis sebelum pemakainya.\nconst urutan = [];\nconst sudah = new Set();\nfunction kunjungi(nama) {\n  if (sudah.has(nama)) return;\n  sudah.add(nama);\n  for (const dep of cariRequire(modul[nama])) kunjungi(dep);\n  urutan.push(nama);\n}\nkunjungi('main.js');\n\nconsole.log('Urutan modul:');\nurutan.forEach((nama, i) => console.log(`  ${i + 1}. ${nama}`));\nconst dibuang = Object.keys(modul).filter((n) => !sudah.has(n));\nconsole.log('Tidak masuk bundel: ' + (dibuang.join(', ') || '-'));\n\n// Rakit bundel: tiap modul dibungkus fungsi (module, exports, require).\nlet bundel = 'const definisi = {\\n';\nfor (const nama of urutan) {\n  bundel += `  '${nama}': function (module, exports, require) {\\n${modul[nama]}\\n  },\\n`;\n}\nbundel += '};\\n';\nbundel +=\n  'const cache = {};\\n' +\n  'function muat(nama) {\\n' +\n  '  if (cache[nama]) return cache[nama].exports;\\n' +\n  '  const module = { exports: {} };\\n' +\n  '  cache[nama] = module;\\n' +\n  \"  definisi[nama](module, module.exports, (p) => muat(p.slice(2)));\\n\" +\n  '  return module.exports;\\n' +\n  '}\\n' +\n  \"muat('main.js');\\n\";\n\nconsole.log('--- menjalankan bundel ---');\nnew Function(bundel)();\n",
    },
    {
        "title": "Latihan 8: Linter Mini untuk Kode JavaScript",
        "difficulty": "Menengah",
        "question": [
            "Tulis linter mini yang membaca kode JavaScript dari stdin dan",
            "memeriksa dua aturan:",
            "",
            "  - no-var: kata var sebagai kata utuh. Pesannya",
            "    \"Pakai let atau const, jangan var.\"",
            "  - eqeqeq: operator == atau != yang bukan bagian dari ===, !==,",
            "    <=, atau >=. Pesannya \"Pakai === supaya tipe ikut",
            "    dibandingkan.\" (untuk ==) atau \"Pakai !== supaya tipe ikut",
            "    dibandingkan.\" (untuk !=).",
            "",
            "Abaikan isi string (kutip tunggal, ganda, atau backtick, dengan",
            "escape \\) dan komentar // sampai akhir baris. Kolom dihitung mulai",
            "1 di baris aslinya. Cetak tiap temuan sebagai",
            "baris:kolom aturan pesan, urut menurut baris lalu kolom, lalu",
            "baris terakhir \"Jumlah temuan: N\".",
            "",
            "Contoh input:",
            "  var total = 0;",
            "  const nama = \"var di string == aman\";",
            "  if (total == 0) { console.log('nol') } // var di komentar == aman",
            "  let x = total != 1 ? 'a' : 'b';",
            "  if (x === 'a' && total !== 2) var y = 1;",
            "",
            "Keluaran yang diharapkan:",
            "1:1 no-var Pakai let atau const, jangan var.",
            "3:11 eqeqeq Pakai === supaya tipe ikut dibandingkan.",
            "4:15 eqeqeq Pakai !== supaya tipe ikut dibandingkan.",
            "5:31 no-var Pakai let atau const, jangan var.",
            "Jumlah temuan: 4",
        ],
        "hints": [
            "Linter sungguhan bekerja di atas pohon sintaks, tapi untuk dua aturan ini cukup membersihkan tiap baris dulu: isi string dan komentar diganti spasi supaya kolomnya tetap sama.",
            "Telusuri baris karakter demi karakter sambil mengingat apakah kamu sedang di dalam string (dan kutip apa pembukanya); begitu bertemu // di luar string, sisa baris dibuang.",
            "Pada baris yang sudah bersih, pakai matchAll dengan /\\bvar\\b/g dan /(?<![=!<>])(==|!=)(?!=)/g; m.index + 1 adalah kolomnya.",
        ],
        "stdin_list": [
            """var total = 0;
const nama = "var di string == aman";
if (total == 0) { console.log('nol') } // var di komentar == aman
let x = total != 1 ? 'a' : 'b';
if (x === 'a' && total !== 2) var y = 1;
""",
            """const a = 1;
let b = a === 1 ? "satu" : "bukan == satu";
console.log(b, a !== 2, a <= 3);
""",
        ],
        "solution": "const kode = require('fs').readFileSync(0, 'utf8');\n\n// Ganti isi string dan komentar baris dengan spasi supaya kolomnya tetap.\nfunction bersihkan(baris) {\n  let hasil = '';\n  let kutip = null;\n  for (let i = 0; i < baris.length; i++) {\n    const c = baris[i];\n    if (kutip) {\n      if (c === '\\\\') {\n        hasil += '  ';\n        i++;\n      } else if (c === kutip) {\n        kutip = null;\n        hasil += c;\n      } else {\n        hasil += ' ';\n      }\n    } else if (c === '/' && baris[i + 1] === '/') {\n      break;\n    } else {\n      if (c === \"'\" || c === '\"' || c === '`') kutip = c;\n      hasil += c;\n    }\n  }\n  return hasil;\n}\n\nconst temuan = [];\nkode.split('\\n').forEach((asli, i) => {\n  const baris = bersihkan(asli);\n  for (const m of baris.matchAll(/\\bvar\\b/g)) {\n    temuan.push([i + 1, m.index + 1, 'no-var', 'Pakai let atau const, jangan var.']);\n  }\n  for (const m of baris.matchAll(/(?<![=!<>])(==|!=)(?!=)/g)) {\n    const ganti = m[1] === '==' ? '===' : '!==';\n    temuan.push([i + 1, m.index + 1, 'eqeqeq', `Pakai ${ganti} supaya tipe ikut dibandingkan.`]);\n  }\n});\n\ntemuan.sort((a, b) => a[0] - b[0] || a[1] - b[1]);\nfor (const [b, k, aturan, pesan] of temuan) console.log(`${b}:${k} ${aturan} ${pesan}`);\nconsole.log(`Jumlah temuan: ${temuan.length}`);\n",
    },
    {
        "title": "Latihan 9: Hook useState Mini",
        "difficulty": "Menengah",
        "question": [
            "Bangun renderer mini yang meniru cara React menyimpan state.",
            "",
            "  - useState(awal) mengambil slot berdasarkan urutan panggilan",
            "    (indeks 0, 1, 2, ...). Slot baru diisi awal; slot lama dipakai",
            "    lagi. Ia mengembalikan [nilai, setState].",
            "  - setState menerima nilai atau fungsi pembaru. Kalau hasilnya sama",
            "    dengan nilai lama menurut Object.is, abaikan. Kalau beda, simpan",
            "    dan tandai perlu render, tapi jangan render saat itu juga.",
            "  - render() mengulang indeks ke 0, menambah nomor render, memanggil",
            "    komponen, lalu mencetak \"render #N: <teks>\".",
            "  - pasang(fn) mengosongkan slot, mengulang nomor ke 0, lalu render.",
            "  - klik(nama) memanggil fungsi bernama itu dari hasil render",
            "    terakhir. Sesudahnya render sekali kalau ada yang ditandai; kalau",
            "    tidak, cetak \"(klik <nama>: tidak ada render)\".",
            "",
            "Komponen Penghitung punya dua state, angka (awal 0) lalu nama (awal",
            "'Rina'), teks \"<nama> menekan <angka> kali\", dan fungsi: tambah",
            "(setAngka(angka + 1)), tambahTiga (tiga kali setAngka(a => a + 1)),",
            "namaSama (setNama('Rina')), dan ganti (setNama('Budi')). Pasang",
            "Penghitung lalu klik tambah, tambahTiga, namaSama, ganti.",
            "",
            "Lalu buktikan aturan hooks. Komponen Profil memanggil",
            "useState('Halo') untuk sapaan hanya kalau variabel tampilkanSapaan",
            "true (kalau tidak, sapaan bernilai '-'), lalu selalu memanggil",
            "useState('Bandung') untuk kota. Teksnya \"sapaan=<s>, kota=<k>\".",
            "Pasang Profil, ubah tampilkanSapaan jadi false, lalu panggil render().",
            "",
            "Keluaran yang diharapkan:",
            "== Penghitung ==",
            "render #1: Rina menekan 0 kali",
            "render #2: Rina menekan 1 kali",
            "render #3: Rina menekan 4 kali",
            "(klik namaSama: tidak ada render)",
            "render #4: Budi menekan 4 kali",
            "== Hook di dalam if ==",
            "render #1: sapaan=Halo, kota=Bandung",
            "render #2: sapaan=-, kota=Halo",
        ],
        "hints": [
            "Semua state disimpan di satu array di luar komponen, dan satu-satunya penanda slot mana milik hook mana adalah urutan pemanggilan di tiap render.",
            "Simpan indeks hook dalam variabel i saat useState dipanggil, supaya setState yang dibuat di render itu selalu menulis ke slot yang sama walau dipanggil belakangan.",
            "Di setState, hitung nilai baru dengan typeof baru === 'function' ? baru(hooks[i]) : baru, keluar kalau Object.is(nilai, hooks[i]), lalu set perluRender = true; klik() yang memeriksa tanda itu dan memanggil render().",
        ],
        "solution": """// Renderer mini: satu komponen, hook disimpan menurut urutan panggilan.
let hooks = [];
let indeks = 0;
let komponen = null;
let hasil = null;
let nomor = 0;
let perluRender = false;

function useState(awal) {
  const i = indeks++;
  if (i >= hooks.length) hooks.push(awal);
  const setState = (baru) => {
    const nilai = typeof baru === 'function' ? baru(hooks[i]) : baru;
    if (Object.is(nilai, hooks[i])) return;
    hooks[i] = nilai;
    perluRender = true;
  };
  return [hooks[i], setState];
}

function render() {
  indeks = 0;
  nomor++;
  hasil = komponen();
  console.log(`render #${nomor}: ${hasil.teks}`);
}

function pasang(fn) {
  komponen = fn;
  hooks = [];
  nomor = 0;
  render();
}

function klik(nama) {
  hasil[nama]();
  if (perluRender) {
    perluRender = false;
    render();
  } else {
    console.log(`(klik ${nama}: tidak ada render)`);
  }
}

function Penghitung() {
  const [angka, setAngka] = useState(0);
  const [nama, setNama] = useState('Rina');
  return {
    teks: `${nama} menekan ${angka} kali`,
    tambah: () => setAngka(angka + 1),
    tambahTiga: () => {
      setAngka((a) => a + 1);
      setAngka((a) => a + 1);
      setAngka((a) => a + 1);
    },
    namaSama: () => setNama('Rina'),
    ganti: () => setNama('Budi'),
  };
}

console.log('== Penghitung ==');
pasang(Penghitung);
klik('tambah');
klik('tambahTiga');
klik('namaSama');
klik('ganti');

let tampilkanSapaan = true;
function Profil() {
  let sapaan = '-';
  if (tampilkanSapaan) {
    [sapaan] = useState('Halo');
  }
  const [kota] = useState('Bandung');
  return { teks: `sapaan=${sapaan}, kota=${kota}` };
}

console.log('== Hook di dalam if ==');
pasang(Profil);
tampilkanSapaan = false;
render();
""",
    },
    {
        "title": "Latihan 10: Redux Mini dengan Reducer dan Subscribe",
        "difficulty": "Menengah",
        "question": [
            "Bangun Redux mini tanpa paket apa pun:",
            "",
            "  - createStore(reducer): state awal didapat dari",
            "    reducer(undefined, { type: '@@init' }). Store punya getState,",
            "    dispatch(action), dan subscribe(fn) yang mengembalikan fungsi",
            "    untuk berhenti berlangganan. dispatch menjalankan reducer lalu",
            "    memanggil semua pelanggan.",
            "  - combineReducers({ hitung, todo }): menjalankan tiap reducer pada",
            "    potongannya. Kalau tidak ada potongan yang berubah (dibandingkan",
            "    dengan ===), kembalikan objek state yang lama.",
            "  - Reducer hitung (awal 0): 'hitung/tambah' menambah action.jumlah",
            "    (atau 1 kalau tidak ada), 'hitung/reset' jadi 0.",
            "  - Reducer todo (awal []): 'todo/tambah' menambah",
            "    { id: panjang + 1, teks, selesai: false }, 'todo/selesai'",
            "    mengubah selesai jadi true untuk id yang cocok (objek baru).",
            "",
            "Satu pelanggan mencetak \"  [log] notifikasi ke-N\". Saat N = 2 ia",
            "berhenti berlangganan dan mencetak \"  [log] berhenti berlangganan\".",
            "",
            "Cetak \"awal: <state JSON>\". Lalu untuk tiap baris stdin (satu action",
            "JSON per baris): cetak \"> <type>\", dispatch, lalu cetak",
            "\"  state: <JSON>\", atau \"  (state tidak berubah)\" kalau objek",
            "state sesudahnya sama persis (===) dengan sebelumnya.",
            "",
            "Keluaran yang diharapkan:",
            "awal: {\"hitung\":0,\"todo\":[]}",
            "> hitung/tambah",
            "  [log] notifikasi ke-1",
            "  state: {\"hitung\":2,\"todo\":[]}",
            "> todo/tambah",
            "  [log] notifikasi ke-2",
            "  [log] berhenti berlangganan",
            "  state: {\"hitung\":2,\"todo\":[{\"id\":1,\"teks\":\"Belajar Redux\",\"selesai\":false}]}",
            "> todo/tambah",
            "  state: {\"hitung\":2,\"todo\":[{\"id\":1,\"teks\":\"Belajar Redux\",\"selesai\":false},{\"id\":2,\"teks\":\"Latihan Zod\",\"selesai\":false}]}",
            "> todo/selesai",
            "  state: {\"hitung\":2,\"todo\":[{\"id\":1,\"teks\":\"Belajar Redux\",\"selesai\":true},{\"id\":2,\"teks\":\"Latihan Zod\",\"selesai\":false}]}",
            "> tidak/dikenal",
            "  (state tidak berubah)",
            "> hitung/reset",
            "  state: {\"hitung\":0,\"todo\":[{\"id\":1,\"teks\":\"Belajar Redux\",\"selesai\":true},{\"id\":2,\"teks\":\"Latihan Zod\",\"selesai\":false}]}",
        ],
        "hints": [
            "Reducer adalah fungsi murni (state lama, action) -> state baru, dan untuk action yang tidak dikenali ia mengembalikan state yang sama persis, bukan salinannya.",
            "Simpan pelanggan di array; saat dispatch, panggil salinan array (slice) supaya pelanggan yang berhenti di tengah pemanggilan tidak mengacaukan perulangan.",
            "Di combineReducers, isi objek baru per kunci lalu set penanda berubah kalau baru[kunci] !== state[kunci]; kembalikan berubah ? baru : state.",
        ],
        "stdin": """{"type":"hitung/tambah","jumlah":2}
{"type":"todo/tambah","teks":"Belajar Redux"}
{"type":"todo/tambah","teks":"Latihan Zod"}
{"type":"todo/selesai","id":1}
{"type":"tidak/dikenal"}
{"type":"hitung/reset"}
""",
        "solution": "function createStore(reducer) {\n  let state = reducer(undefined, { type: '@@init' });\n  let pendengar = [];\n  return {\n    getState: () => state,\n    dispatch(action) {\n      state = reducer(state, action);\n      pendengar.slice().forEach((f) => f());\n      return action;\n    },\n    subscribe(f) {\n      pendengar.push(f);\n      return () => {\n        pendengar = pendengar.filter((g) => g !== f);\n      };\n    },\n  };\n}\n\nfunction combineReducers(peta) {\n  return (state = {}, action) => {\n    const baru = {};\n    let berubah = false;\n    for (const kunci of Object.keys(peta)) {\n      baru[kunci] = peta[kunci](state[kunci], action);\n      if (baru[kunci] !== state[kunci]) berubah = true;\n    }\n    return berubah ? baru : state;\n  };\n}\n\nfunction hitung(state = 0, action) {\n  switch (action.type) {\n    case 'hitung/tambah':\n      return state + (action.jumlah ?? 1);\n    case 'hitung/reset':\n      return 0;\n    default:\n      return state;\n  }\n}\n\nfunction todo(state = [], action) {\n  switch (action.type) {\n    case 'todo/tambah':\n      return [...state, { id: state.length + 1, teks: action.teks, selesai: false }];\n    case 'todo/selesai':\n      return state.map((t) => (t.id === action.id ? { ...t, selesai: true } : t));\n    default:\n      return state;\n  }\n}\n\nconst store = createStore(combineReducers({ hitung, todo }));\n\nlet notifikasi = 0;\nconst berhenti = store.subscribe(() => {\n  notifikasi++;\n  console.log(`  [log] notifikasi ke-${notifikasi}`);\n  if (notifikasi === 2) {\n    berhenti();\n    console.log('  [log] berhenti berlangganan');\n  }\n});\n\nconsole.log('awal: ' + JSON.stringify(store.getState()));\nconst baris = require('fs').readFileSync(0, 'utf8').split('\\n').filter((b) => b.trim());\nfor (const b of baris) {\n  const action = JSON.parse(b);\n  const sebelum = store.getState();\n  console.log('> ' + action.type);\n  store.dispatch(action);\n  const sesudah = store.getState();\n  if (sesudah === sebelum) console.log('  (state tidak berubah)');\n  else console.log('  state: ' + JSON.stringify(sesudah));\n}\n",
    },
    {
        "title": "Latihan 11: Validator Skema Mini ala Zod",
        "difficulty": "Lanjut",
        "question": [
            "Buat pustaka skema mini bernama s dengan API mirip Zod:",
            "",
            "  - s.string() dengan .min(n): gagal \"harus string\" atau",
            "    \"minimal n huruf\".",
            "  - s.number() dengan .int() dan .min(n): gagal \"harus number\",",
            "    \"harus bilangan bulat\", atau \"minimal n\" (diperiksa urut",
            "    begitu, berhenti di kegagalan pertama).",
            "  - s.object({ ... }): gagal \"harus object\" (null dan array juga",
            "    bukan object), lalu periksa tiap kunci yang didefinisikan.",
            "  - s.array(skemaIsi): gagal \"harus array\", lalu periksa tiap isi.",
            "  - .optional() di skema mana pun: undefined diterima. Tanpa itu,",
            "    undefined gagal dengan \"wajib diisi\".",
            "  - skema.safeParse(nilai) mengembalikan { success: true, data } atau",
            "    { success: false, error: [teks] } dengan teks",
            "    \"<jalur>: <pesan>\". Jalur digabung titik (alamat.kota, hobi.1);",
            "    jalur kosong ditulis (akar).",
            "",
            "Pakai skema dan data ini persis:",
            "",
            "  const Pendaftar = s.object({",
            "    nama: s.string().min(3),",
            "    umur: s.number().int().min(15),",
            "    alamat: s.object({ kota: s.string(), kodePos: s.string().optional() }),",
            "    hobi: s.array(s.string()),",
            "    telepon: s.string().optional(),",
            "  });",
            "  const data = [",
            "    { nama: 'Rina', umur: 17, alamat: { kota: 'Bandung' }, hobi: ['catur', 'musik'] },",
            "    { nama: 'Al', umur: 16.5, alamat: {}, hobi: ['renang', 7], telepon: 812 },",
            "    { nama: 'Budi', umur: 12, alamat: { kota: 'Solo', kodePos: '57111' }, hobi: 'bola' },",
            "    'bukan objek',",
            "  ];",
            "",
            "Untuk tiap data cetak \"Data N: valid\" atau \"Data N: <jumlah> error\"",
            "diikuti tiap error yang diawali dua spasi.",
            "",
            "Keluaran yang diharapkan:",
            "Data 1: valid",
            "Data 2: 5 error",
            "  nama: minimal 3 huruf",
            "  umur: harus bilangan bulat",
            "  alamat.kota: wajib diisi",
            "  hobi.1: harus string",
            "  telepon: harus string",
            "Data 3: 2 error",
            "  umur: minimal 15",
            "  hobi: harus array",
            "Data 4: 1 error",
            "  (akar): harus object",
        ],
        "hints": [
            "Tiap skema cukup tahu cara memeriksa satu nilai di satu jalur dan mencatat masalahnya ke daftar bersama; object dan array tinggal memanggil skema anaknya dengan jalur yang diperpanjang.",
            "Buat kelas dasar dengan metode _cek(nilai, jalur, error) yang mengurus undefined dan optional, lalu meneruskan ke fungsi pemeriksa khusus tiap jenis skema.",
            "optional() sebaiknya mengembalikan salinan skema dengan penanda _opsional: true (Object.create(Object.getPrototypeOf(this)) lalu Object.assign), supaya skema aslinya tetap wajib.",
        ],
        "solution": """// Validator skema mini ala Zod. Tiap skema punya _cek(nilai, jalur, error).
class Skema {
  constructor(cek) {
    this._cekInti = cek;
    this._opsional = false;
  }
  optional() {
    const s = Object.create(Object.getPrototypeOf(this));
    Object.assign(s, this, { _opsional: true });
    return s;
  }
  _cek(nilai, jalur, error) {
    if (nilai === undefined) {
      if (!this._opsional) error.push([jalur, 'wajib diisi']);
      return;
    }
    this._cekInti(nilai, jalur, error);
  }
  safeParse(nilai) {
    const error = [];
    this._cek(nilai, [], error);
    if (error.length === 0) return { success: true, data: nilai };
    return {
      success: false,
      error: error.map(([j, pesan]) => `${j.length ? j.join('.') : '(akar)'}: ${pesan}`),
    };
  }
}

class SkemaString extends Skema {
  constructor() {
    super((v, jalur, error) => {
      if (typeof v !== 'string') return error.push([jalur, 'harus string']);
      if (this._min !== undefined && v.length < this._min) {
        error.push([jalur, `minimal ${this._min} huruf`]);
      }
    });
  }
  min(n) {
    this._min = n;
    return this;
  }
}

class SkemaNumber extends Skema {
  constructor() {
    super((v, jalur, error) => {
      if (typeof v !== 'number' || Number.isNaN(v)) return error.push([jalur, 'harus number']);
      if (this._int && !Number.isInteger(v)) return error.push([jalur, 'harus bilangan bulat']);
      if (this._min !== undefined && v < this._min) error.push([jalur, `minimal ${this._min}`]);
    });
  }
  int() {
    this._int = true;
    return this;
  }
  min(n) {
    this._min = n;
    return this;
  }
}

const s = {
  string: () => new SkemaString(),
  number: () => new SkemaNumber(),
  array: (isi) =>
    new Skema((v, jalur, error) => {
      if (!Array.isArray(v)) return error.push([jalur, 'harus array']);
      v.forEach((x, i) => isi._cek(x, [...jalur, i], error));
    }),
  object: (bentuk) =>
    new Skema((v, jalur, error) => {
      if (typeof v !== 'object' || v === null || Array.isArray(v)) {
        return error.push([jalur, 'harus object']);
      }
      for (const [kunci, skema] of Object.entries(bentuk)) {
        skema._cek(v[kunci], [...jalur, kunci], error);
      }
    }),
};

const Pendaftar = s.object({
  nama: s.string().min(3),
  umur: s.number().int().min(15),
  alamat: s.object({ kota: s.string(), kodePos: s.string().optional() }),
  hobi: s.array(s.string()),
  telepon: s.string().optional(),
});

const data = [
  { nama: 'Rina', umur: 17, alamat: { kota: 'Bandung' }, hobi: ['catur', 'musik'] },
  { nama: 'Al', umur: 16.5, alamat: {}, hobi: ['renang', 7], telepon: 812 },
  { nama: 'Budi', umur: 12, alamat: { kota: 'Solo', kodePos: '57111' }, hobi: 'bola' },
  'bukan objek',
];

data.forEach((d, i) => {
  const hasil = Pendaftar.safeParse(d);
  if (hasil.success) {
    console.log(`Data ${i + 1}: valid`);
  } else {
    console.log(`Data ${i + 1}: ${hasil.error.length} error`);
    for (const e of hasil.error) console.log('  ' + e);
  }
});
""",
    },
    {
        "title": "Latihan 12: Interpolasi Template ala Vue",
        "difficulty": "Menengah",
        "question": [
            "Buat mesin template mini yang meniru {{ }} di Vue, tanpa eval dan",
            "tanpa new Function.",
            "",
            "  - reactive(objek, saatBerubah): Proxy yang juga membungkus objek",
            "    bersarang. Saat sebuah properti diberi nilai yang sama",
            "    (Object.is), cetak \"(<kunci> tidak berubah, tidak render)\" dan",
            "    jangan render. Kalau beda, simpan lalu panggil saatBerubah(kunci).",
            "  - buatApp({ template, data, computed }): membuat state reaktif dan",
            "    langsung render dengan alasan \"awal\". Tiap perubahan memicu",
            "    render dengan alasan \"<kunci> berubah\".",
            "  - Render mengganti tiap {{ jalur }} (spasi di dalam kurung boleh",
            "    ada). Kalau bagian pertama jalur adalah nama computed, nilainya",
            "    dihitung dengan memanggil fungsi itu dengan state. Selain itu",
            "    nilainya dibaca dari state mengikuti titik (pengguna.nama). Nilai",
            "    undefined atau null jadi teks kosong. Nilai lain di-escape:",
            "    & < > \" jadi &amp; &lt; &gt; &quot;.",
            "  - Tiap render mencetak \"render #N (<alasan>): <hasil>\".",
            "",
            "Pakai ini persis:",
            "",
            "  const state = buatApp({",
            "    template: '<p>{{ pengguna.nama }}: {{ jumlah }} x {{ harga }} = {{ total }} {{ catatan }}</p>',",
            "    data: { pengguna: { nama: 'Rina' }, jumlah: 2, harga: 18000 },",
            "    computed: { total: (s) => s.jumlah * s.harga },",
            "  });",
            "  state.jumlah = 3;",
            "  state.jumlah = 3;",
            "  state.pengguna.nama = '<b>Budi</b>';",
            "  state.harga = 20000;",
            "  state.catatan = 'promo \"akhir pekan\"';",
            "",
            "Keluaran yang diharapkan:",
            "render #1 (awal): <p>Rina: 2 x 18000 = 36000 </p>",
            "render #2 (jumlah berubah): <p>Rina: 3 x 18000 = 54000 </p>",
            "(jumlah tidak berubah, tidak render)",
            "render #3 (nama berubah): <p>&lt;b&gt;Budi&lt;/b&gt;: 3 x 18000 = 54000 </p>",
            "render #4 (harga berubah): <p>&lt;b&gt;Budi&lt;/b&gt;: 3 x 20000 = 60000 </p>",
            "render #5 (catatan berubah): <p>&lt;b&gt;Budi&lt;/b&gt;: 3 x 20000 = 60000 promo &quot;akhir pekan&quot;</p>",
        ],
        "hints": [
            "Reaktivitas Vue berdiri di atas Proxy: perangkap set adalah satu-satunya tempat kamu tahu ada data yang berubah, jadi di situlah render dipicu.",
            "Supaya state.pengguna.nama juga terlacak, perangkap get harus membungkus nilai yang berupa objek dengan Proxy yang sama sebelum dikembalikan.",
            "Untuk render, pakai template.replace(/\\{\\{\\s*([\\w.]+)\\s*\\}\\}/g, (_, jalur) => ...) dan baca jalur bertitik dengan jalur.split('.').reduce(...); escape & lebih dulu sebelum < > \".",
        ],
        "solution": "function escapeHtml(teks) {\n  return String(teks)\n    .replace(/&/g, '&amp;')\n    .replace(/</g, '&lt;')\n    .replace(/>/g, '&gt;')\n    .replace(/\"/g, '&quot;');\n}\n\nfunction ambil(objek, jalur) {\n  return jalur.split('.').reduce((o, k) => (o == null ? undefined : o[k]), objek);\n}\n\nfunction reactive(objek, saatBerubah) {\n  return new Proxy(objek, {\n    get(target, kunci) {\n      const v = Reflect.get(target, kunci);\n      return typeof v === 'object' && v !== null ? reactive(v, saatBerubah) : v;\n    },\n    set(target, kunci, nilai) {\n      if (Object.is(target[kunci], nilai)) {\n        console.log(`(${kunci} tidak berubah, tidak render)`);\n        return true;\n      }\n      Reflect.set(target, kunci, nilai);\n      saatBerubah(kunci);\n      return true;\n    },\n  });\n}\n\nfunction buatApp({ template, data, computed }) {\n  let nomor = 0;\n  const state = reactive(data, (kunci) => render(`${kunci} berubah`));\n\n  function nilaiDari(jalur) {\n    const kepala = jalur.split('.')[0];\n    if (kepala in computed) {\n      return ambil({ [kepala]: computed[kepala](state) }, jalur);\n    }\n    return ambil(state, jalur);\n  }\n\n  function render(alasan) {\n    nomor++;\n    const html = template.replace(/\\{\\{\\s*([\\w.]+)\\s*\\}\\}/g, (_, jalur) => {\n      const v = nilaiDari(jalur);\n      return v === undefined || v === null ? '' : escapeHtml(v);\n    });\n    console.log(`render #${nomor} (${alasan}): ${html}`);\n  }\n\n  render('awal');\n  return state;\n}\n\nconst state = buatApp({\n  template: '<p>{{ pengguna.nama }}: {{ jumlah }} x {{ harga }} = {{ total }} {{ catatan }}</p>',\n  data: { pengguna: { nama: 'Rina' }, jumlah: 2, harga: 18000 },\n  computed: { total: (s) => s.jumlah * s.harga },\n});\n\nstate.jumlah = 3;\nstate.jumlah = 3;\nstate.pengguna.nama = '<b>Budi</b>';\nstate.harga = 20000;\nstate.catatan = 'promo \"akhir pekan\"';\n",
    },
    {
        "title": "Latihan 13: Kontainer Dependency Injection Mini",
        "difficulty": "Menengah",
        "question": [
            "Bangun kontainer dependency injection mini seperti injector Angular.",
            "",
            "Kontainer menerima daftar provider. Tiap provider punya provide",
            "(nama token) dan salah satu dari: useValue (nilai jadi),",
            "useClass (dibuat dengan new, argumennya hasil deps), atau",
            "useFactory (fungsi yang dipanggil dengan hasil deps). deps adalah",
            "daftar token yang dibutuhkan, boleh kosong.",
            "",
            "get(token) harus:",
            "  - mengembalikan instans yang sama kalau token pernah dibuat",
            "    (singleton);",
            "  - membuat semua deps lebih dulu, lalu mencetak \"buat <token>\" tepat",
            "    sesudah token itu jadi;",
            "  - melempar Error \"Tidak ada provider untuk '<token>' (diminta oleh",
            "    <peminta>)\" kalau token tidak terdaftar (peminta ditulis akar",
            "    kalau dipanggil langsung);",
            "  - melempar Error \"Dependensi melingkar: A -> B -> A\" kalau token",
            "    diminta lagi saat ia sendiri masih dibuat.",
            "",
            "Pakai class dan provider ini. Logger menyimpan pesan di array",
            "pesan lewat log(teks). ApiKlien(konfigurasi, logger) menyimpan",
            "konfigurasi.alamatApi sebagai alamat; ambil(jalur) mencatat",
            "\"ambil <alamat><jalur>\" lalu mengembalikan ['Rina', 'Budi', 'Sari'].",
            "LayananPengguna(api, logger) punya jumlah() yang mencatat",
            "\"hitung pengguna\" lalu mengembalikan panjang api.ambil('/pengguna').",
            "",
            "  { provide: 'Konfigurasi', useValue: { alamatApi: 'api.tokoku.id' } },",
            "  { provide: 'Logger', useClass: Logger },",
            "  { provide: 'ApiKlien', useClass: ApiKlien, deps: ['Konfigurasi', 'Logger'] },",
            "  { provide: 'LayananPengguna', useClass: LayananPengguna, deps: ['ApiKlien', 'Logger'] },",
            "  { provide: 'Tanggal', useFactory: () => '19 Oktober 2026' },",
            "  { provide: 'Laporan', deps: ['LayananPengguna', 'Tanggal'],",
            "    useFactory: (layanan, tanggal) => `Laporan ${tanggal}: ${layanan.jumlah()} pengguna` },",
            "  { provide: 'A', useClass: A, deps: ['B'] },",
            "  { provide: 'B', useClass: B, deps: ['A'] },",
            "  { provide: 'Cache', useFactory: (db) => db, deps: ['Database'] },",
            "",
            "Lalu: cetak get('Laporan'); cetak \"Logger tunggal: <bool>\" (apakah",
            "get('Logger') sama dengan logger milik ApiKlien); cetak \"Isi log: \"",
            "diikuti pesan yang digabung \"; \"; lalu coba get('A') dan get('Cache')",
            "dan cetak \"Galat: <pesan>\" untuk masing-masing.",
            "",
            "Keluaran yang diharapkan:",
            "buat Konfigurasi",
            "buat Logger",
            "buat ApiKlien",
            "buat LayananPengguna",
            "buat Tanggal",
            "buat Laporan",
            "Laporan 19 Oktober 2026: 3 pengguna",
            "Logger tunggal: true",
            "Isi log: hitung pengguna; ambil api.tokoku.id/pengguna",
            "Galat: Dependensi melingkar: A -> B -> A",
            "Galat: Tidak ada provider untuk 'Database' (diminta oleh Cache)",
        ],
        "hints": [
            "Injector menyelesaikan dependensi secara rekursif: sebelum sebuah token dibuat, semua token di deps-nya harus sudah jadi, dan hasil yang sudah jadi disimpan supaya tidak dibuat dua kali.",
            "Simpan Map token -> instans untuk singleton, dan sebuah array token yang sedang dibuat; kalau token yang diminta sudah ada di array itu, berarti ada lingkaran.",
            "Di get, push token ke array sedangDibuat, buat deps dengan this.get(d, token), bangun nilainya sesuai useValue/useClass/useFactory, lalu pop di blok finally supaya array tetap benar walau ada Error.",
        ],
        "solution": """class Logger {
  constructor() {
    this.pesan = [];
  }
  log(teks) {
    this.pesan.push(teks);
  }
}

class ApiKlien {
  constructor(konfigurasi, logger) {
    this.alamat = konfigurasi.alamatApi;
    this.logger = logger;
  }
  ambil(jalur) {
    this.logger.log('ambil ' + this.alamat + jalur);
    return ['Rina', 'Budi', 'Sari'];
  }
}

class LayananPengguna {
  constructor(api, logger) {
    this.api = api;
    this.logger = logger;
  }
  jumlah() {
    this.logger.log('hitung pengguna');
    return this.api.ambil('/pengguna').length;
  }
}

class Kontainer {
  constructor(daftar) {
    this.provider = new Map(daftar.map((p) => [p.provide, p]));
    this.instans = new Map();
    this.sedangDibuat = [];
  }

  get(token, peminta) {
    if (this.instans.has(token)) return this.instans.get(token);
    const p = this.provider.get(token);
    if (!p) {
      throw new Error(`Tidak ada provider untuk '${token}' (diminta oleh ${peminta || 'akar'})`);
    }
    if (this.sedangDibuat.includes(token)) {
      const rantai = [...this.sedangDibuat.slice(this.sedangDibuat.indexOf(token)), token];
      throw new Error('Dependensi melingkar: ' + rantai.join(' -> '));
    }
    this.sedangDibuat.push(token);
    try {
      const deps = (p.deps || []).map((d) => this.get(d, token));
      let nilai;
      if ('useValue' in p) nilai = p.useValue;
      else if (p.useClass) nilai = new p.useClass(...deps);
      else nilai = p.useFactory(...deps);
      console.log('buat ' + token);
      this.instans.set(token, nilai);
      return nilai;
    } finally {
      this.sedangDibuat.pop();
    }
  }
}

class A {}
class B {}

const kontainer = new Kontainer([
  { provide: 'Konfigurasi', useValue: { alamatApi: 'api.tokoku.id' } },
  { provide: 'Logger', useClass: Logger },
  { provide: 'ApiKlien', useClass: ApiKlien, deps: ['Konfigurasi', 'Logger'] },
  { provide: 'LayananPengguna', useClass: LayananPengguna, deps: ['ApiKlien', 'Logger'] },
  { provide: 'Tanggal', useFactory: () => '19 Oktober 2026' },
  {
    provide: 'Laporan',
    useFactory: (layanan, tanggal) => `Laporan ${tanggal}: ${layanan.jumlah()} pengguna`,
    deps: ['LayananPengguna', 'Tanggal'],
  },
  { provide: 'A', useClass: A, deps: ['B'] },
  { provide: 'B', useClass: B, deps: ['A'] },
  { provide: 'Cache', useFactory: (db) => db, deps: ['Database'] },
]);

console.log(kontainer.get('Laporan'));
const logger = kontainer.get('Logger');
console.log('Logger tunggal: ' + (logger === kontainer.get('ApiKlien').logger));
console.log('Isi log: ' + logger.pesan.join('; '));
for (const token of ['A', 'Cache']) {
  try {
    kontainer.get(token);
  } catch (e) {
    console.log('Galat: ' + e.message);
  }
}
""",
    },
    {
        "title": "Latihan 14: Observable Mini dengan Operator",
        "difficulty": "Lanjut",
        "question": [
            "Bangun Observable mini seperti RxJS.",
            "",
            "  - new Observable(fungsi): fungsi menerima pelanggan berisi",
            "    next(v), complete(), dan properti tertutup, lalu boleh",
            "    mengembalikan fungsi teardown (pembersihan).",
            "  - subscribe(pengamat): pengamat berupa fungsi (dianggap next) atau",
            "    objek { next, complete }. Sesudah complete atau unsubscribe,",
            "    next tidak diteruskan lagi dan teardown dijalankan tepat sekali.",
            "    Kalau complete terjadi sebelum fungsi selesai, teardown dijalankan",
            "    begitu fungsi mengembalikannya. Kembalikan { unsubscribe }.",
            "  - pipe(...operator) merangkai operator dari kiri ke kanan.",
            "  - Operator map(f), filter(cocok), dan take(n): masing-masing",
            "    mengembalikan Observable baru yang berlangganan ke sumber dan",
            "    teardown-nya berhenti berlangganan dari sumber. take(n)",
            "    memanggil complete sesudah nilai ke-n.",
            "",
            "Sumber yang dipakai:",
            "  - jam palsu dengan detik (awal 0), pendengar (Set), dan maju(n)",
            "    yang n kali menambah detik lalu memanggil semua pendengar;",
            "  - interval(): saat dilanggani mencetak \"  [sumber] mulai\", mendaftar",
            "    ke jam, lalu mengirim 0, 1, 2, ... tiap detik. Teardown-nya",
            "    melepas pendengar dan mencetak",
            "    \"  [sumber] dihentikan di detik <detik>\";",
            "  - dari(daftar): mengirim isi daftar berurutan (berhenti kalau",
            "    pelanggan tertutup), lalu complete. Teardown-nya mencetak",
            "    \"  [dari] dibersihkan\".",
            "",
            "Skenario: (1) dari([1..6]) dengan filter genap lalu map x * 10,",
            "cetak \"nilai v\" dan \"selesai\". (2) interval() dengan map x * x,",
            "filter genap, take(3), cetak \"detik <detik>: v\" dan \"selesai\", lalu",
            "jam.maju(10) dan cetak jumlah pendengar tersisa. (3) interval()",
            "tanpa operator, maju(2), unsubscribe, maju(2) lagi, lalu cetak",
            "jumlah pendengar tersisa.",
            "",
            "Keluaran yang diharapkan:",
            "== dari + filter + map ==",
            "nilai 20",
            "nilai 40",
            "nilai 60",
            "selesai",
            "  [dari] dibersihkan",
            "== interval + map + filter + take(3) ==",
            "  [sumber] mulai",
            "detik 1: 0",
            "detik 3: 4",
            "detik 5: 16",
            "selesai",
            "  [sumber] dihentikan di detik 5",
            "pendengar jam tersisa: 0",
            "== berhenti manual ==",
            "  [sumber] mulai",
            "detik 11: 0",
            "detik 12: 1",
            "  [sumber] dihentikan di detik 12",
            "pendengar jam tersisa: 0",
        ],
        "hints": [
            "Observable adalah fungsi yang ditunda: tidak ada yang terjadi sampai subscribe dipanggil, dan subscribe-lah yang membuat pelanggan dengan penanda tertutup serta menyimpan teardown.",
            "Operator cukup berupa fungsi (sumber) => new Observable(sub => ...) yang berlangganan ke sumber, meneruskan nilai yang sudah diubah ke sub, lalu mengembalikan () => langganan.unsubscribe().",
            "Di subscribe, simpan teardown = this._langganan(pelanggan) || null, lalu if (tertutup) jalankan pembersihan; di complete dan unsubscribe, set tertutup = true dan panggil fungsi bersihkan yang mengosongkan teardown sebelum memanggilnya.",
        ],
        "solution": """class Observable {
  constructor(langganan) {
    this._langganan = langganan;
  }

  subscribe(pengamat) {
    const p = typeof pengamat === 'function' ? { next: pengamat } : pengamat;
    let tertutup = false;
    let teardown = null;
    const bersihkan = () => {
      if (teardown) {
        const t = teardown;
        teardown = null;
        t();
      }
    };
    const pelanggan = {
      next(v) {
        if (!tertutup && p.next) p.next(v);
      },
      complete() {
        if (tertutup) return;
        tertutup = true;
        if (p.complete) p.complete();
        bersihkan();
      },
      get tertutup() {
        return tertutup;
      },
    };
    teardown = this._langganan(pelanggan) || null;
    if (tertutup) bersihkan();
    return {
      unsubscribe() {
        tertutup = true;
        bersihkan();
      },
    };
  }

  pipe(...operator) {
    return operator.reduce((sumber, op) => op(sumber), this);
  }
}

const map = (f) => (sumber) =>
  new Observable((sub) => {
    const s = sumber.subscribe({ next: (v) => sub.next(f(v)), complete: () => sub.complete() });
    return () => s.unsubscribe();
  });

const filter = (cocok) => (sumber) =>
  new Observable((sub) => {
    const s = sumber.subscribe({
      next: (v) => {
        if (cocok(v)) sub.next(v);
      },
      complete: () => sub.complete(),
    });
    return () => s.unsubscribe();
  });

const take = (n) => (sumber) =>
  new Observable((sub) => {
    let hitung = 0;
    const s = sumber.subscribe({
      next: (v) => {
        hitung++;
        sub.next(v);
        if (hitung >= n) sub.complete();
      },
      complete: () => sub.complete(),
    });
    return () => s.unsubscribe();
  });

// Jam palsu: tiap maju(n) memanggil pendengar n kali.
const jam = {
  detik: 0,
  pendengar: new Set(),
  maju(n) {
    for (let i = 0; i < n; i++) {
      this.detik++;
      [...this.pendengar].forEach((f) => f());
    }
  },
};

function interval() {
  return new Observable((sub) => {
    console.log('  [sumber] mulai');
    let k = 0;
    const f = () => sub.next(k++);
    jam.pendengar.add(f);
    return () => {
      jam.pendengar.delete(f);
      console.log(`  [sumber] dihentikan di detik ${jam.detik}`);
    };
  });
}

function dari(daftar) {
  return new Observable((sub) => {
    for (const v of daftar) {
      if (sub.tertutup) break;
      sub.next(v);
    }
    sub.complete();
    return () => console.log('  [dari] dibersihkan');
  });
}

console.log('== dari + filter + map ==');
dari([1, 2, 3, 4, 5, 6])
  .pipe(filter((x) => x % 2 === 0), map((x) => x * 10))
  .subscribe({ next: (v) => console.log('nilai', v), complete: () => console.log('selesai') });

console.log('== interval + map + filter + take(3) ==');
interval()
  .pipe(map((x) => x * x), filter((x) => x % 2 === 0), take(3))
  .subscribe({
    next: (v) => console.log(`detik ${jam.detik}: ${v}`),
    complete: () => console.log('selesai'),
  });
jam.maju(10);
console.log('pendengar jam tersisa: ' + jam.pendengar.size);

console.log('== berhenti manual ==');
const langganan = interval().subscribe((v) => console.log(`detik ${jam.detik}: ${v}`));
jam.maju(2);
langganan.unsubscribe();
jam.maju(2);
console.log('pendengar jam tersisa: ' + jam.pendengar.size);
""",
    },
    {
        "title": "Latihan 15: Pertukaran HTML Parsial ala htmx",
        "difficulty": "Menengah",
        "question": [
            "Tulis tiruan kecil htmx. Halaman awal disimpan sebagai string:",
            "",
            "  <main id=\"app\">",
            "  <h1 id=\"judul\">Kafe Senja</h1>",
            "  <button id=\"menu\" hx-get=\"/menu\" hx-target=\"#isi\">Lihat menu</button>",
            "  <div id=\"isi\"></div>",
            "  <ul id=\"pesan\"></ul>",
            "  <button id=\"hapus\" hx-get=\"/kosong\" hx-target=\"#pesan\">Kosongkan</button>",
            "  </main>",
            "",
            "Baris-baris itu digabung dengan \\n. Server palsu adalah objek rute",
            "ke potongan HTML:",
            "",
            "  /menu   : \\n + empat tombol (satu per baris) + \\n",
            "            <button id=\"kopi\" hx-get=\"/kopi\" hx-target=\"#pesan\" hx-swap=\"beforeend\">Kopi</button>",
            "            <button id=\"teh\" hx-get=\"/teh\" hx-target=\"#pesan\" hx-swap=\"beforeend\">Teh</button>",
            "            <button id=\"kue\" hx-get=\"/kue\" hx-target=\"#pesan\" hx-swap=\"beforeend\">Kue</button>",
            "            <button id=\"tutup\" hx-get=\"/tutup\" hx-target=\"#judul\" hx-swap=\"outerHTML\">Tutup</button>",
            "  /kopi   : \\n<li>Kopi susu</li>",
            "  /teh    : \\n<li>Teh melati</li>",
            "  /kosong : (string kosong)",
            "  /tutup  : <h1 id=\"judul\">Kafe Senja (tutup)</h1>",
            "",
            "Stdin berisi id elemen yang diklik, satu per baris. Untuk tiap klik:",
            "  - Cari elemen ber-id itu di halaman SAAT ITU (elemen dari potongan",
            "    yang sudah ditempel ikut bisa diklik). Kalau nggak ada, cetak",
            "    klik #ID: elemen tidak ada",
            "  - Kalau elemen itu nggak punya hx-get, cetak klik #ID: tanpa hx-get",
            "  - Target = hx-target (tanpa tanda #), bawaannya elemen itu sendiri.",
            "    Cara tukar = hx-swap, bawaannya innerHTML.",
            "  - Kalau rute nggak ada di server, cetak",
            "    klik #ID: GET /rute -> 404, halaman tidak berubah",
            "  - Selain itu tukar halaman dan cetak klik #ID: GET /rute -> CARA #target",
            "",
            "Cara tukar yang didukung: innerHTML (ganti isi), outerHTML (ganti",
            "seluruh elemen), beforeend (tambah sebelum tag penutup), afterbegin",
            "(tambah sesudah tag pembuka). Elemen target bisa berisi elemen",
            "bersarang, jadi cari tag penutup yang berpasangan. Sesudah semua",
            "klik, cetak --- lalu halaman akhir.",
            "",
            "Keluaran yang diharapkan (input pertama: menu, kopi, teh, kue, kopi, tutup):",
            "",
            "klik #menu: GET /menu -> innerHTML #isi",
            "klik #kopi: GET /kopi -> beforeend #pesan",
            "klik #teh: GET /teh -> beforeend #pesan",
            "klik #kue: GET /kue -> 404, halaman tidak berubah",
            "klik #kopi: GET /kopi -> beforeend #pesan",
            "klik #tutup: GET /tutup -> outerHTML #judul",
            "---",
            "<main id=\"app\">",
            "<h1 id=\"judul\">Kafe Senja (tutup)</h1>",
            "<button id=\"menu\" hx-get=\"/menu\" hx-target=\"#isi\">Lihat menu</button>",
            "<div id=\"isi\">",
            "<button id=\"kopi\" hx-get=\"/kopi\" hx-target=\"#pesan\" hx-swap=\"beforeend\">Kopi</button>",
            "<button id=\"teh\" hx-get=\"/teh\" hx-target=\"#pesan\" hx-swap=\"beforeend\">Teh</button>",
            "<button id=\"kue\" hx-get=\"/kue\" hx-target=\"#pesan\" hx-swap=\"beforeend\">Kue</button>",
            "<button id=\"tutup\" hx-get=\"/tutup\" hx-target=\"#judul\" hx-swap=\"outerHTML\">Tutup</button>",
            "</div>",
            "<ul id=\"pesan\">",
            "<li>Kopi susu</li>",
            "<li>Teh melati</li>",
            "<li>Kopi susu</li></ul>",
            "<button id=\"hapus\" hx-get=\"/kosong\" hx-target=\"#pesan\">Kosongkan</button>",
            "</main>",
        ],
        "hints": [
            "Pisahkan tiga pekerjaan: menemukan elemen beserta batas awal dan akhirnya, membaca atributnya, dan menukar potongan string.",
            "Untuk menemukan tag penutup yang berpasangan, hitung tingkat: tiap tag pembuka bernama sama menambah satu, tiap tag penutupnya mengurangi satu, dan berhenti saat tingkatnya nol.",
            "Simpan empat posisi untuk elemen target (awal, akhir tag pembuka, awal tag penutup, akhir), karena keempat cara tukar cukup memotong dan menyambung string di posisi itu dengan slice.",
        ],
        "stdin_list": [
            """menu
kopi
teh
kue
kopi
tutup
""",
            """kopi
menu
teh
hapus
judul
menu
""",
        ],
        "solution": "const fs = require('fs');\n\nlet halaman = [\n  '<main id=\"app\">',\n  '<h1 id=\"judul\">Kafe Senja</h1>',\n  '<button id=\"menu\" hx-get=\"/menu\" hx-target=\"#isi\">Lihat menu</button>',\n  '<div id=\"isi\"></div>',\n  '<ul id=\"pesan\"></ul>',\n  '<button id=\"hapus\" hx-get=\"/kosong\" hx-target=\"#pesan\">Kosongkan</button>',\n  '</main>',\n].join('\\n');\n\nconst server = {\n  '/menu': [\n    '',\n    '<button id=\"kopi\" hx-get=\"/kopi\" hx-target=\"#pesan\" hx-swap=\"beforeend\">Kopi</button>',\n    '<button id=\"teh\" hx-get=\"/teh\" hx-target=\"#pesan\" hx-swap=\"beforeend\">Teh</button>',\n    '<button id=\"kue\" hx-get=\"/kue\" hx-target=\"#pesan\" hx-swap=\"beforeend\">Kue</button>',\n    '<button id=\"tutup\" hx-get=\"/tutup\" hx-target=\"#judul\" hx-swap=\"outerHTML\">Tutup</button>',\n    '',\n  ].join('\\n'),\n  '/kopi': '\\n<li>Kopi susu</li>',\n  '/teh': '\\n<li>Teh melati</li>',\n  '/kosong': '',\n  '/tutup': '<h1 id=\"judul\">Kafe Senja (tutup)</h1>',\n};\n\nfunction cariElemen(html, id) {\n  const pola = new RegExp('<([a-z0-9]+)([^>]*)\\\\sid=\"' + id + '\"([^>]*)>');\n  const m = pola.exec(html);\n  if (!m) return null;\n  const tag = m[1];\n  const awal = m.index;\n  const akhirBuka = awal + m[0].length;\n  let tingkat = 1;\n  const pencari = new RegExp('<' + tag + '[\\\\s>]|</' + tag + '>', 'g');\n  pencari.lastIndex = akhirBuka;\n  let t;\n  while ((t = pencari.exec(html))) {\n    tingkat += t[0].startsWith('</') ? -1 : 1;\n    if (tingkat === 0) {\n      return { awal, akhirBuka, awalTutup: t.index, akhir: t.index + t[0].length, buka: m[0] };\n    }\n  }\n  return null;\n}\n\nfunction atribut(tagBuka, nama) {\n  const m = new RegExp('\\\\s' + nama + '=\"([^\"]*)\"').exec(tagBuka);\n  return m ? m[1] : null;\n}\n\nfunction tukar(html, el, isi, cara) {\n  switch (cara) {\n    case 'innerHTML': return html.slice(0, el.akhirBuka) + isi + html.slice(el.awalTutup);\n    case 'outerHTML': return html.slice(0, el.awal) + isi + html.slice(el.akhir);\n    case 'beforeend': return html.slice(0, el.awalTutup) + isi + html.slice(el.awalTutup);\n    case 'afterbegin': return html.slice(0, el.akhirBuka) + isi + html.slice(el.akhirBuka);\n    default: return html;\n  }\n}\n\nconst klik = fs.readFileSync(0, 'utf8').split('\\n').map((s) => s.trim()).filter(Boolean);\nfor (const id of klik) {\n  const el = cariElemen(halaman, id);\n  if (!el) {\n    console.log('klik #' + id + ': elemen tidak ada');\n    continue;\n  }\n  const url = atribut(el.buka, 'hx-get');\n  if (!url) {\n    console.log('klik #' + id + ': tanpa hx-get');\n    continue;\n  }\n  const target = (atribut(el.buka, 'hx-target') || '#' + id).slice(1);\n  const cara = atribut(el.buka, 'hx-swap') || 'innerHTML';\n  if (!(url in server)) {\n    console.log('klik #' + id + ': GET ' + url + ' -> 404, halaman tidak berubah');\n    continue;\n  }\n  const sasaran = cariElemen(halaman, target);\n  if (!sasaran) {\n    console.log('klik #' + id + ': target #' + target + ' tidak ada');\n    continue;\n  }\n  halaman = tukar(halaman, sasaran, server[url], cara);\n  console.log('klik #' + id + ': GET ' + url + ' -> ' + cara + ' #' + target);\n}\nconsole.log('---');\nconsole.log(halaman);\n",
    },
    {
        "title": "Latihan 16: Test Runner Mini dengan expect",
        "difficulty": "Lanjut",
        "question": [
            "Tulis test runner kecil seperti Vitest atau Jest, tanpa paket.",
            "",
            "Sediakan fungsi:",
            "  - describe(nama, isi): kelompok tes, boleh bersarang.",
            "  - it(nama, isi): satu tes.",
            "  - beforeEach(isi): jalan sebelum setiap tes di kelompok itu dan",
            "    semua subkelompoknya. beforeEach milik kelompok luar jalan lebih",
            "    dulu daripada milik kelompok dalam.",
            "  - expect(nilai) dengan tiga pencocok:",
            "    toBe(x) membandingkan dengan Object.is,",
            "    toEqual(x) membandingkan isi objek dan array secara dalam,",
            "    toThrow(potongan) memanggil nilai sebagai fungsi dan lulus kalau",
            "    ia melempar error (kalau potongan diberikan, pesannya wajib",
            "    memuat potongan itu).",
            "",
            "Pesan gagal (memakai JSON.stringify untuk nilai):",
            "  toBe    : diharapkan X, didapat Y",
            "  toEqual : isi beda: diharapkan X, didapat Y",
            "  toThrow : diharapkan melempar error, ternyata tidak",
            "",
            "Tes dijalankan sesudah semua didaftarkan, berurutan sesuai urutan",
            "tulis. Nama kelompok dicetak dengan indentasi dua spasi per tingkat,",
            "tes dicetak sebagai LULUS nama atau GAGAL nama, dan pesan gagal",
            "dicetak di baris berikutnya dengan indentasi tambahan enam spasi.",
            "Terakhir cetak ringkasan.",
            "",
            "Uji runner-mu dengan kelas Keranjang dan delapan tes di bawah ini",
            "(salin ke solusimu):",
            "",
            "  class Keranjang {",
            "    constructor() { this.isi = []; }",
            "    tambah(nama, harga, jumlah = 1) {",
            "      if (harga < 0) throw new Error('harga tidak boleh negatif');",
            "      this.isi.push({ nama, harga, jumlah });",
            "    }",
            "    total() { return this.isi.reduce((s, b) => s + b.harga * b.jumlah, 0); }",
            "    daftar() { return this.isi.map((b) => b.nama); }",
            "  }",
            "",
            "Isi tesnya: keranjang baru di beforeEach; mulai kosong (total 0);",
            "total kopi 18000 x2 + teh 12000 = 48000; harga -5 ditolak dengan",
            "toThrow('negatif'); kelompok daftar dengan beforeEach menambah kopi,",
            "berisi tiga tes: toEqual(['kopi']), toBe(['kopi']), dan sesudah",
            "menambah teh toEqual(['teh', 'kopi']); lalu isi keranjang baru",
            "toEqual([]); terakhir tambah('air') tanpa harga diharapkan toThrow().",
            "",
            "Keluaran yang diharapkan:",
            "",
            "Keranjang",
            "  LULUS mulai kosong",
            "  LULUS total menjumlahkan harga kali jumlah",
            "  LULUS harga negatif ditolak",
            "  daftar",
            "    LULUS berisi nama barang",
            "    GAGAL toBe tidak cocok untuk array",
            "          diharapkan [\"kopi\"], didapat [\"kopi\"]",
            "    GAGAL urutan ikut dibandingkan",
            "          isi beda: diharapkan [\"teh\",\"kopi\"], didapat [\"kopi\",\"teh\"]",
            "  LULUS beforeEach memberi keranjang baru",
            "  GAGAL tambah tanpa harga melempar error",
            "        diharapkan melempar error, ternyata tidak",
            "Ringkasan: 5 lulus, 3 gagal, 8 tes",
            "",
            "Tiga tes itu memang gagal dengan sengaja. Yang terakhir menunjukkan",
            "bug: undefined < 0 bernilai false, jadi tambah('air') lolos tanpa",
            "error.",
        ],
        "hints": [
            "Pisahkan pendaftaran dan eksekusi: describe dan it cuma mencatat ke sebuah pohon, lalu satu fungsi jalankan menelusuri pohon itu sesudah semua tercatat.",
            "Simpan kelompok yang sedang aktif di satu variabel, ganti saat masuk describe, lalu kembalikan ke nilai lama sesudah isi describe selesai dijalankan.",
            "Bungkus setiap tes dengan try/catch: kalau semua beforeEach dan isi tes selesai tanpa error tandai LULUS, kalau ada error cetak GAGAL beserta e.message.",
        ],
        "solution": """// ---------- test runner mini ----------
const akar = { nama: null, tes: [], sebelum: [], induk: null };
let kini = akar;

function describe(nama, isi) {
  const grup = { nama, tes: [], sebelum: [], induk: kini };
  kini.tes.push({ grup });
  const lama = kini;
  kini = grup;
  isi();
  kini = lama;
}

function it(nama, isi) {
  kini.tes.push({ nama, isi });
}

function beforeEach(isi) {
  kini.sebelum.push(isi);
}

function samaDalam(a, b) {
  if (Object.is(a, b)) return true;
  if (typeof a !== 'object' || typeof b !== 'object' || a === null || b === null) return false;
  if (Array.isArray(a) !== Array.isArray(b)) return false;
  const ka = Object.keys(a);
  const kb = Object.keys(b);
  if (ka.length !== kb.length) return false;
  return ka.every((k) => samaDalam(a[k], b[k]));
}

function expect(nyata) {
  const tampil = JSON.stringify;
  return {
    toBe(harap) {
      if (!Object.is(nyata, harap)) {
        throw new Error('diharapkan ' + tampil(harap) + ', didapat ' + tampil(nyata));
      }
    },
    toEqual(harap) {
      if (!samaDalam(nyata, harap)) {
        throw new Error('isi beda: diharapkan ' + tampil(harap) + ', didapat ' + tampil(nyata));
      }
    },
    toThrow(potongan) {
      try {
        nyata();
      } catch (e) {
        if (potongan && !e.message.includes(potongan)) {
          throw new Error('pesan error "' + e.message + '" tidak memuat "' + potongan + '"');
        }
        return;
      }
      throw new Error('diharapkan melempar error, ternyata tidak');
    },
  };
}

const hitung = { lulus: 0, gagal: 0 };

function semuaSebelum(grup) {
  const daftar = [];
  for (let g = grup; g; g = g.induk) daftar.unshift(...g.sebelum);
  return daftar;
}

function jalankan(grup, tingkat) {
  const jarak = '  '.repeat(tingkat);
  for (const t of grup.tes) {
    if (t.grup) {
      console.log(jarak + t.grup.nama);
      jalankan(t.grup, tingkat + 1);
      continue;
    }
    try {
      for (const f of semuaSebelum(grup)) f();
      t.isi();
      hitung.lulus++;
      console.log(jarak + 'LULUS ' + t.nama);
    } catch (e) {
      hitung.gagal++;
      console.log(jarak + 'GAGAL ' + t.nama);
      console.log(jarak + '      ' + e.message);
    }
  }
}

// ---------- kode yang diuji ----------
class Keranjang {
  constructor() { this.isi = []; }
  tambah(nama, harga, jumlah = 1) {
    if (harga < 0) throw new Error('harga tidak boleh negatif');
    this.isi.push({ nama, harga, jumlah });
  }
  total() { return this.isi.reduce((s, b) => s + b.harga * b.jumlah, 0); }
  daftar() { return this.isi.map((b) => b.nama); }
}

// ---------- tes ----------
let k;
describe('Keranjang', () => {
  beforeEach(() => { k = new Keranjang(); });

  it('mulai kosong', () => {
    expect(k.total()).toBe(0);
  });

  it('total menjumlahkan harga kali jumlah', () => {
    k.tambah('kopi', 18000, 2);
    k.tambah('teh', 12000);
    expect(k.total()).toBe(48000);
  });

  it('harga negatif ditolak', () => {
    expect(() => k.tambah('kue', -5)).toThrow('negatif');
  });

  describe('daftar', () => {
    beforeEach(() => { k.tambah('kopi', 18000); });

    it('berisi nama barang', () => {
      expect(k.daftar()).toEqual(['kopi']);
    });

    it('toBe tidak cocok untuk array', () => {
      expect(k.daftar()).toBe(['kopi']);
    });

    it('urutan ikut dibandingkan', () => {
      k.tambah('teh', 12000);
      expect(k.daftar()).toEqual(['teh', 'kopi']);
    });
  });

  it('beforeEach memberi keranjang baru', () => {
    expect(k.isi).toEqual([]);
  });

  it('tambah tanpa harga melempar error', () => {
    expect(() => k.tambah('air')).toThrow();
  });
});

jalankan(akar, 0);
const total = hitung.lulus + hitung.gagal;
console.log('Ringkasan: ' + hitung.lulus + ' lulus, ' + hitung.gagal + ' gagal, ' + total + ' tes');
""",
    },
    {
        "title": "Latihan 17: Pencegat fetch Mini ala MSW",
        "difficulty": "Lanjut",
        "question": [
            "Tulis tiruan kecil Mock Service Worker yang mencegat fetch.",
            "",
            "  - tiruan.get(jalur, resolver) dan tiruan.post(jalur, resolver)",
            "    membuat handler (di MSW asli namanya http.get dan http.post).",
            "    Jalur boleh memuat parameter seperti",
            "    /users/:id. Resolver menerima { params, body } (body adalah hasil",
            "    JSON.parse dari opsi.body, atau null) dan mengembalikan Response.",
            "  - setupServer(...handler) mengembalikan objek dengan:",
            "    mulai(): simpan fetch asli lalu ganti globalThis.fetch dengan",
            "    fungsi async (url, opsi) yang mencari handler pertama dengan",
            "    method dan jalur cocok (bagian ?query diabaikan);",
            "    use(...h): menambah handler sementara yang diperiksa lebih dulu;",
            "    resetHandlers(): membuang handler sementara;",
            "    tutup(): memulihkan fetch asli.",
            "  - Kalau nggak ada handler yang cocok, cetak",
            "    [tiruan] peringatan: tidak ada handler untuk METHOD /jalur",
            "    lalu lempar TypeError('jaringan dimatikan selama tes').",
            "",
            "Handler bawaan: GET /users/:id mengembalikan pengguna 7 (Sari) atau",
            "8 (Budi), atau status 404 { pesan: 'pengguna tidak ada' }. POST",
            "/users mengembalikan status 201 dengan { id: 9, ...body }. Pakai",
            "Response.json(data, { status }) bawaan Node.",
            "",
            "Kode aplikasi memanggil fetch global tanpa tahu ada tiruan. Tulis",
            "pemanggilannya sebagai globalThis.fetch.call(globalThis, url, opsi),",
            "lalu baca res.status dan await res.json(). Jalankan urutan ini dan",
            "cetak LABEL -> STATUS JSON atau LABEL -> gagal: PESAN:",
            "GET /users/7, GET /users/99, POST /users dengan body nama Tono,",
            "GET /produk?hal=2, lalu server.use handler GET /users/:id yang",
            "selalu mengembalikan 500 { pesan: 'server sibuk' } dan minta",
            "/users/8, lalu resetHandlers dan minta /users/8 lagi. Terakhir",
            "panggil tutup() dan cetak apakah fetch asli sudah pulih.",
            "",
            "Keluaran yang diharapkan:",
            "",
            "GET /users/7 -> 200 {\"id\":7,\"nama\":\"Sari\"}",
            "GET /users/99 -> 404 {\"pesan\":\"pengguna tidak ada\"}",
            "POST /users -> 201 {\"id\":9,\"nama\":\"Tono\"}",
            "[tiruan] peringatan: tidak ada handler untuk GET /produk",
            "GET /produk -> gagal: jaringan dimatikan selama tes",
            "GET /users/8 (server.use) -> 500 {\"pesan\":\"server sibuk\"}",
            "GET /users/8 (reset) -> 200 {\"id\":8,\"nama\":\"Budi\"}",
            "fetch asli dipulihkan: true",
        ],
        "hints": [
            "Ubah pola jalur jadi regex dengan mengganti setiap :nama menjadi grup ([^/]+), dan catat nama parameternya sesuai urutan grup.",
            "Simpan dua daftar handler, sementara dan bawaan, lalu periksa gabungan [...sementara, ...bawaan] supaya handler dari use() menang.",
            "Fungsi pengganti fetch harus async supaya selalu mengembalikan Promise, persis seperti fetch asli, dan kode aplikasi bisa memakai await tanpa perubahan.",
        ],
        "solution": """// ---------- tiruan kecil MSW ----------
function buatPola(jalur) {
  const nama = [];
  const regex = jalur.replace(/:([a-zA-Z]+)/g, (_, n) => {
    nama.push(n);
    return '([^/]+)';
  });
  return { regex: new RegExp('^' + regex + '$'), nama };
}

function handler(method) {
  return (jalur, resolver) => ({ method, jalur, pola: buatPola(jalur), resolver });
}

const tiruan = { get: handler('GET'), post: handler('POST') };

function setupServer(...awal) {
  const dasar = [...awal];
  let tambahan = [];
  let asli = null;
  return {
    mulai() {
      asli = globalThis.fetch;
      globalThis.fetch = async (url, opsi = {}) => {
        const method = (opsi.method || 'GET').toUpperCase();
        const jalur = url.split('?')[0];
        for (const h of [...tambahan, ...dasar]) {
          if (h.method !== method) continue;
          const m = h.pola.regex.exec(jalur);
          if (!m) continue;
          const params = {};
          h.pola.nama.forEach((n, i) => { params[n] = m[i + 1]; });
          const body = opsi.body ? JSON.parse(opsi.body) : null;
          return h.resolver({ params, body });
        }
        console.log('[tiruan] peringatan: tidak ada handler untuk ' + method + ' ' + jalur);
        throw new TypeError('jaringan dimatikan selama tes');
      };
    },
    use(...h) { tambahan.unshift(...h); },
    resetHandlers() { tambahan = []; },
    tutup() { globalThis.fetch = asli; },
  };
}

// ---------- handler, seperti berkas mocks/handlers.js ----------
const pengguna = { 7: { id: 7, nama: 'Sari' }, 8: { id: 8, nama: 'Budi' } };

const server = setupServer(
  tiruan.get('/users/:id', ({ params }) => {
    const u = pengguna[params.id];
    if (!u) return Response.json({ pesan: 'pengguna tidak ada' }, { status: 404 });
    return Response.json(u);
  }),
  tiruan.post('/users', ({ body }) => Response.json({ id: 9, ...body }, { status: 201 })),
);

// ---------- kode aplikasi: nggak tahu apa-apa soal tiruan ----------
async function api(url, opsi) {
  const res = await globalThis.fetch.call(globalThis, url, opsi);
  const data = await res.json();
  return { status: res.status, data };
}

async function coba(label, url, opsi) {
  try {
    const { status, data } = await api(url, opsi);
    console.log(label + ' -> ' + status + ' ' + JSON.stringify(data));
  } catch (e) {
    console.log(label + ' -> gagal: ' + e.message);
  }
}

async function main() {
  const fetchAsli = globalThis.fetch;
  server.mulai();
  await coba('GET /users/7', '/users/7');
  await coba('GET /users/99', '/users/99');
  await coba('POST /users', '/users', { method: 'POST', body: JSON.stringify({ nama: 'Tono' }) });
  await coba('GET /produk', '/produk?hal=2');

  server.use(tiruan.get('/users/:id', () => Response.json({ pesan: 'server sibuk' }, { status: 500 })));
  await coba('GET /users/8 (server.use)', '/users/8');
  server.resetHandlers();
  await coba('GET /users/8 (reset)', '/users/8');

  server.tutup();
  console.log('fetch asli dipulihkan: ' + (globalThis.fetch === fetchAsli));
}

main();
""",
    },
    {
        "title": "Latihan 18: Router Berbasis Berkas Mini",
        "difficulty": "Lanjut",
        "question": [
            "Tulis pencocok rute berbasis berkas seperti App Router Next.js.",
            "",
            "Stdin berisi daftar jalur berkas (satu per baris), lalu baris ---,",
            "lalu daftar URL yang dicocokkan. Aturan membangun rute:",
            "  - Hanya berkas yang diawali app/ dan diakhiri /page.js yang",
            "    menjadi rute. app/page.js adalah rute /. Berkas lain diabaikan.",
            "  - Segmen dalam kurung biasa seperti (pemasaran) adalah route group",
            "    dan nggak masuk URL.",
            "  - [nama] cocok dengan tepat satu segmen, [...nama] cocok dengan",
            "    satu segmen atau lebih dan hasilnya array.",
            "  - Kalau dua berkas menghasilkan jalur yang sama, cetak",
            "    BENTROK /jalur: berkasPertama dan berkasKedua",
            "    lalu abaikan berkas kedua.",
            "",
            "Urutkan rute dengan membandingkan segmen satu per satu dari kiri:",
            "statis lebih dulu daripada dinamis, dinamis lebih dulu daripada",
            "catch-all. Kalau semua segmen yang dibandingkan sama jenisnya, rute",
            "yang lebih pendek lebih dulu; kalau masih sama, urutkan menurut",
            "teks jalurnya. Cetak Tabel rute: lalu tiap rute dengan nomor.",
            "",
            "Lalu cetak Pencocokan: dan untuk setiap URL (abaikan bagian ?query)",
            "pakai rute pertama di tabel yang cocok, cetak URL -> rute params",
            "dengan params sebagai JSON, atau URL -> 404.",
            "",
            "Keluaran yang diharapkan (input pertama):",
            "",
            "Tabel rute:",
            "  1. /  (app/page.js)",
            "  2. /blog  (app/blog/page.js)",
            "  3. /tentang  (app/(pemasaran)/tentang/page.js)",
            "  4. /blog/[slug]  (app/blog/[slug]/page.js)",
            "  5. /blog/[slug]/komentar  (app/blog/[slug]/komentar/page.js)",
            "  6. /docs/[...path]  (app/docs/[...path]/page.js)",
            "  7. /[kategori]  (app/[kategori]/page.js)",
            "Pencocokan:",
            "  / -> / {}",
            "  /blog -> /blog {}",
            "  /blog/halo-dunia -> /blog/[slug] {\"slug\":\"halo-dunia\"}",
            "  /blog/halo-dunia/komentar -> /blog/[slug]/komentar {\"slug\":\"halo-dunia\"}",
            "  /docs/mulai/pasang/linux -> /docs/[...path] {\"path\":[\"mulai\",\"pasang\",\"linux\"]}",
            "  /docs -> /[kategori] {\"kategori\":\"docs\"}",
            "  /tentang -> /tentang {}",
            "  /sepatu?warna=merah -> /[kategori] {\"kategori\":\"sepatu\"}",
            "  /blog/a/b -> 404",
            "",
            "Perhatikan /docs: catch-all butuh minimal satu segmen, jadi yang",
            "cocok justru /[kategori].",
        ],
        "hints": [
            "Ubah tiap berkas jadi daftar segmen, buang route group, lalu beri setiap segmen angka jenis: 0 untuk statis, 1 untuk dinamis, dan 2 untuk catch-all.",
            "Daftar angka jenis itu bisa dibandingkan seperti kata di kamus, elemen demi elemen dari kiri, dan perbandingan inilah yang dipakai untuk mengurutkan tabel rute.",
            "Saat mencocokkan, telusuri segmen rute bersama potongan URL: segmen statis harus sama persis, segmen dinamis menyimpan satu potongan, dan catch-all mengambil semua sisa potongan lalu selesai.",
        ],
        "stdin_list": [
            """app/page.js
app/layout.js
app/blog/page.js
app/blog/[slug]/page.js
app/blog/[slug]/komentar/page.js
app/docs/[...path]/page.js
app/(pemasaran)/tentang/page.js
app/[kategori]/page.js
app/blog/kartu.js
---
/
/blog
/blog/halo-dunia
/blog/halo-dunia/komentar
/docs/mulai/pasang/linux
/docs
/tentang
/sepatu?warna=merah
/blog/a/b
""",
            """app/page.js
app/tentang/page.js
app/(pemasaran)/tentang/page.js
app/produk/[id]/page.js
app/produk/baru/page.js
app/[...semua]/page.js
---
/produk/baru
/produk/12
/tentang
/x/y/z
/
""",
        ],
        "solution": "const fs = require('fs');\n\nconst [bagianBerkas, bagianUrl] = fs.readFileSync(0, 'utf8').split('---');\nconst berkas = bagianBerkas.split('\\n').map((s) => s.trim()).filter(Boolean);\nconst daftarUrl = bagianUrl.split('\\n').map((s) => s.trim()).filter(Boolean);\n\n// 0 = statis, 1 = dinamis [x], 2 = catch-all [...x]\nfunction jenis(seg) {\n  if (seg.startsWith('[...')) return 2;\n  if (seg.startsWith('[')) return 1;\n  return 0;\n}\n\nconst rute = [];\nfor (const b of berkas) {\n  if (!b.startsWith('app/') || !b.endsWith('/page.js')) continue;\n  const segmen = b.slice(4, -8).split('/').filter((s) => s && !/^\\(.*\\)$/.test(s));\n  if (b === 'app/page.js') segmen.length = 0;\n  const jalur = '/' + segmen.join('/');\n  const ada = rute.find((r) => r.jalur === jalur);\n  if (ada) {\n    console.log('BENTROK ' + jalur + ': ' + ada.berkas + ' dan ' + b);\n    continue;\n  }\n  rute.push({ jalur, segmen, berkas: b, kunci: segmen.map(jenis) });\n}\n\nfunction bandingkan(a, b) {\n  const n = Math.min(a.kunci.length, b.kunci.length);\n  for (let i = 0; i < n; i++) {\n    if (a.kunci[i] !== b.kunci[i]) return a.kunci[i] - b.kunci[i];\n  }\n  if (a.kunci.length !== b.kunci.length) return a.kunci.length - b.kunci.length;\n  return a.jalur < b.jalur ? -1 : a.jalur > b.jalur ? 1 : 0;\n}\nrute.sort(bandingkan);\n\nconsole.log('Tabel rute:');\nrute.forEach((r, i) => console.log('  ' + (i + 1) + '. ' + r.jalur + '  (' + r.berkas + ')'));\n\nfunction cocok(r, bagian) {\n  const params = {};\n  for (let i = 0; i < r.segmen.length; i++) {\n    const s = r.segmen[i];\n    const k = r.kunci[i];\n    if (i >= bagian.length) return null;\n    if (k === 2) {\n      params[s.slice(4, -1)] = bagian.slice(i);\n      return params;\n    }\n    if (k === 1) params[s.slice(1, -1)] = bagian[i];\n    else if (s !== bagian[i]) return null;\n  }\n  return r.segmen.length === bagian.length ? params : null;\n}\n\nconsole.log('Pencocokan:');\nfor (const url of daftarUrl) {\n  const bagian = url.split('?')[0].split('/').filter(Boolean);\n  let hasil = null;\n  for (const r of rute) {\n    const p = cocok(r, bagian);\n    if (p) {\n      hasil = { r, p };\n      break;\n    }\n  }\n  if (hasil) console.log('  ' + url + ' -> ' + hasil.r.jalur + ' ' + JSON.stringify(hasil.p));\n  else console.log('  ' + url + ' -> 404');\n}\n",
    },
    {
        "title": "Latihan 19: Pengurut Tugas Monorepo dengan Cache",
        "difficulty": "Lanjut",
        "question": [
            "Tulis task runner monorepo kecil seperti Turborepo.",
            "",
            "Stdin berisi satu paket per baris dengan bentuk",
            "  nama: dep1 dep2 = isi",
            "(daftar dependensi boleh kosong). Baris opsional terakhir",
            "  ubah nama = isiBaru",
            "mengubah isi satu paket sesudah dua kali jalan.",
            "",
            "Yang harus dilakukan:",
            "  1. Kalau ada dependensi yang nggak terdaftar, cetak",
            "     Galat: NAMA bergantung pada DEP yang tidak ada",
            "     lalu berhenti.",
            "  2. Susun urutan topologis: paket yang semua dependensinya sudah",
            "     selesai boleh jalan, dan kalau ada beberapa yang siap, ambil",
            "     yang namanya paling kecil secara alfabet.",
            "  3. Kalau ada siklus, cetak Siklus terdeteksi: a -> ... -> a",
            "     (mulai dari paket bersiklus dengan nama terkecil, telusuri",
            "     dependensi urut alfabet) lalu Build dibatalkan. dan berhenti.",
            "  4. Cetak Urutan build: lalu nama paket dipisah koma.",
            "  5. Jalankan tiga kali (yang ketiga hanya kalau ada baris ubah).",
            "     Untuk tiap paket, sesuai urutan, hitung hash = 8 karakter",
            "     pertama SHA-256 (heksadesimal) dari teks",
            "     nama|isi|hashDep1,hashDep2 (hash dependensi diurutkan menurut",
            "     nama dependensinya). Kalau hash itu sudah ada di cache, cetak",
            "     CACHE; kalau belum, simpan ke cache dan cetak BUILD. Nama",
            "     dirapatkan kiri selebar 6 karakter. Tutup tiap jalan dengan",
            "     ringkasan jumlah build dan jumlah dari cache.",
            "",
            "Pakai modul bawaan crypto: crypto.createHash('sha256').",
            "",
            "Keluaran yang diharapkan (input pertama):",
            "",
            "Urutan build: utils, api, ui, docs, web",
            "Jalan 1:",
            "  utils  BUILD  6751d828",
            "  api    BUILD  7248d2e0",
            "  ui     BUILD  fac52512",
            "  docs   BUILD  7b2b45f3",
            "  web    BUILD  2f5781b9",
            "  -> 5 build, 0 dari cache",
            "Jalan 2:",
            "  utils  CACHE  6751d828",
            "  api    CACHE  7248d2e0",
            "  ui     CACHE  fac52512",
            "  docs   CACHE  7b2b45f3",
            "  web    CACHE  2f5781b9",
            "  -> 0 build, 5 dari cache",
            "Ubah ui = tombol-v2",
            "Jalan 3:",
            "  utils  CACHE  6751d828",
            "  api    CACHE  7248d2e0",
            "  ui     BUILD  bff688d0",
            "  docs   BUILD  22b2d411",
            "  web    BUILD  1d18ab88",
            "  -> 3 build, 2 dari cache",
            "",
            "Input pertama:",
            "  web: ui api = halaman-v1",
            "  ui: utils = tombol-v1",
            "  api: utils = rute-v1",
            "  utils: = format-v1",
            "  docs: ui = md-v1",
            "  ubah ui = tombol-v2",
        ],
        "hints": [
            "Pecah tugasnya jadi tiga: membaca paket, menyusun urutan dengan algoritma Kahn (hitung jumlah dependensi yang belum selesai), lalu menjalankan dengan cache.",
            "Hash sebuah paket memuat hash dependensinya, jadi perubahan di paket bawah otomatis mengubah hash semua paket di atasnya tanpa perlu kamu telusuri sendiri.",
            "Kalau sesudah Kahn masih ada paket yang belum masuk urutan, berarti ada siklus; telusuri dengan DFS sambil menyimpan jejak, dan siklus ketemu saat kamu kembali ke paket yang masih ada di jejak.",
        ],
        "stdin_list": [
            """web: ui api = halaman-v1
ui: utils = tombol-v1
api: utils = rute-v1
utils: = format-v1
docs: ui = md-v1
ubah ui = tombol-v2
""",
            """d: = satu
a: c = satu
b: a = satu
c: b = satu
e: d = satu
""",
        ],
        "solution": "const fs = require('fs');\nconst crypto = require('crypto');\n\nconst paket = {};\nlet ubah = null;\nfor (const baris of fs.readFileSync(0, 'utf8').split('\\n')) {\n  const b = baris.trim();\n  if (!b) continue;\n  if (b.startsWith('ubah ')) {\n    const [nama, isi] = b.slice(5).split('=').map((s) => s.trim());\n    ubah = { nama, isi };\n    continue;\n  }\n  const [kiri, isi] = b.split('=').map((s) => s.trim());\n  const [nama, deps] = kiri.split(':').map((s) => s.trim());\n  paket[nama] = { deps: deps ? deps.split(/\\s+/) : [], isi };\n}\n\nfor (const [nama, p] of Object.entries(paket)) {\n  for (const d of p.deps) {\n    if (!paket[d]) {\n      console.log('Galat: ' + nama + ' bergantung pada ' + d + ' yang tidak ada');\n      process.exit(0);\n    }\n  }\n}\n\n// Kahn: ambil paket yang semua dependensinya sudah selesai, seri dipecah alfabet\nfunction urutanTopologis() {\n  const sisa = {};\n  for (const [n, p] of Object.entries(paket)) sisa[n] = p.deps.length;\n  const urut = [];\n  const siap = Object.keys(sisa).filter((n) => sisa[n] === 0).sort();\n  while (siap.length) {\n    const n = siap.shift();\n    urut.push(n);\n    for (const [m, p] of Object.entries(paket)) {\n      if (p.deps.includes(n) && --sisa[m] === 0) {\n        siap.push(m);\n        siap.sort();\n      }\n    }\n  }\n  return urut;\n}\n\nfunction cariSiklus(mulai) {\n  const jejak = [];\n  const dikunjungi = new Set();\n  function telusur(n) {\n    const i = jejak.indexOf(n);\n    if (i >= 0) return jejak.slice(i).concat(n);\n    if (dikunjungi.has(n)) return null;\n    dikunjungi.add(n);\n    jejak.push(n);\n    for (const d of [...paket[n].deps].sort()) {\n      const h = telusur(d);\n      if (h) return h;\n    }\n    jejak.pop();\n    return null;\n  }\n  return telusur(mulai);\n}\n\nconst urut = urutanTopologis();\nif (urut.length < Object.keys(paket).length) {\n  const tersisa = Object.keys(paket).filter((n) => !urut.includes(n)).sort();\n  console.log('Siklus terdeteksi: ' + cariSiklus(tersisa[0]).join(' -> '));\n  console.log('Build dibatalkan.');\n  process.exit(0);\n}\nconsole.log('Urutan build: ' + urut.join(', '));\n\nconst cache = new Set();\nfunction jalankan(ke) {\n  console.log('Jalan ' + ke + ':');\n  const hash = {};\n  let build = 0;\n  for (const n of urut) {\n    const p = paket[n];\n    const masukan = n + '|' + p.isi + '|' + p.deps.slice().sort().map((d) => hash[d]).join(',');\n    hash[n] = crypto.createHash('sha256').update(masukan).digest('hex').slice(0, 8);\n    if (cache.has(hash[n])) {\n      console.log('  ' + n.padEnd(6) + ' CACHE  ' + hash[n]);\n    } else {\n      cache.add(hash[n]);\n      build++;\n      console.log('  ' + n.padEnd(6) + ' BUILD  ' + hash[n]);\n    }\n  }\n  console.log('  -> ' + build + ' build, ' + (urut.length - build) + ' dari cache');\n}\n\njalankan(1);\njalankan(2);\nif (ubah) {\n  paket[ubah.nama].isi = ubah.isi;\n  console.log('Ubah ' + ubah.nama + ' = ' + ubah.isi);\n  jalankan(3);\n}\n",
    },
    {
        "title": "Latihan 20: Strategi Cache ala Service Worker",
        "difficulty": "Lanjut",
        "question": [
            "Tiru keputusan service worker di atas jaringan palsu.",
            "",
            "Stdin berisi langkah, satu per baris:",
            "  online /jalur    halaman meminta /jalur dan jaringan menyala",
            "  offline /jalur   halaman meminta /jalur tapi jaringan mati",
            "  ubah /jalur vN   versi isi /jalur di server berubah jadi vN",
            "Isi setiap jalur di server awalnya v1, dan respons jaringan",
            "berbentuk teks \"/jalur vN\".",
            "",
            "Jalankan langkah yang sama tiga kali dengan cache kosong yang baru,",
            "masing-masing untuk satu strategi, didahului baris == nama ==:",
            "  - cache-first: pakai cache kalau ada; kalau belum, ambil dari",
            "    jaringan lalu simpan.",
            "  - network-first: ambil dari jaringan lalu simpan; kalau offline,",
            "    pakai cache dengan catatan (cadangan offline).",
            "  - stale-while-revalidate: kalau ada di cache, jawab dari cache;",
            "    kalau online dan isi jaringan berbeda, perbarui cache dan beri",
            "    catatan (latar: cache diperbarui ke vN). Kalau belum ada di",
            "    cache, perlakukan seperti cache-first.",
            "Permintaan yang nggak bisa dijawab menghasilkan",
            "GAGAL (offline, belum ada di cache).",
            "",
            "Format tiap baris: nomor langkah rata kanan dua karakter, aksi",
            "rata kiri tujuh karakter, jalur rata kiri tujuh karakter, lalu ->",
            "dan sumbernya (jaringan atau cache diikuti empat spasi). Lihat",
            "contoh.",
            "",
            "Keluaran yang diharapkan (input pertama):",
            "",
            "== cache-first ==",
            " 1 online  /menu   -> jaringan /menu v1 (disimpan)",
            " 2 online  /menu   -> cache    /menu v1",
            " 3 server: /menu sekarang v2",
            " 4 online  /menu   -> cache    /menu v1",
            " 5 online  /menu   -> cache    /menu v1",
            " 6 offline /menu   -> cache    /menu v1",
            " 7 offline /promo  -> GAGAL (offline, belum ada di cache)",
            "== network-first ==",
            " 1 online  /menu   -> jaringan /menu v1 (disimpan)",
            " 2 online  /menu   -> jaringan /menu v1 (disimpan)",
            " 3 server: /menu sekarang v2",
            " 4 online  /menu   -> jaringan /menu v2 (disimpan)",
            " 5 online  /menu   -> jaringan /menu v2 (disimpan)",
            " 6 offline /menu   -> cache    /menu v2 (cadangan offline)",
            " 7 offline /promo  -> GAGAL (offline, belum ada di cache)",
            "== stale-while-revalidate ==",
            " 1 online  /menu   -> jaringan /menu v1 (disimpan)",
            " 2 online  /menu   -> cache    /menu v1",
            " 3 server: /menu sekarang v2",
            " 4 online  /menu   -> cache    /menu v1 (latar: cache diperbarui ke v2)",
            " 5 online  /menu   -> cache    /menu v2",
            " 6 offline /menu   -> cache    /menu v2",
            " 7 offline /promo  -> GAGAL (offline, belum ada di cache)",
            "",
            "Input pertama: online /menu, online /menu, ubah /menu v2, online",
            "/menu, online /menu, offline /menu, offline /promo.",
        ],
        "hints": [
            "Buat satu fungsi simulasi yang menerima nama strategi dan membuat cache serta versi server yang baru setiap kali dipanggil, supaya ketiga strategi nggak saling memengaruhi.",
            "Jaringan palsu cukup berupa fungsi yang mengembalikan null kalau offline dan teks /jalur vN kalau online, sehingga ketiga strategi tinggal memeriksa hasil null atau bukan.",
            "Perhatikan urutan di stale-while-revalidate: cetak isi cache yang lama lebih dulu sebagai jawaban, baru perbarui cache dengan isi jaringan untuk permintaan berikutnya.",
        ],
        "stdin_list": [
            """online /menu
online /menu
ubah /menu v2
online /menu
online /menu
offline /menu
offline /promo
""",
            """offline /logo
online /logo
ubah /logo v2
offline /logo
online /logo
""",
        ],
        "solution": "const fs = require('fs');\n\nconst langkah = fs.readFileSync(0, 'utf8').split('\\n').map((s) => s.trim()).filter(Boolean);\n\nfunction simulasi(strategi) {\n  console.log('== ' + strategi + ' ==');\n  const versiServer = {};\n  const cache = new Map();\n  const versi = (url) => versiServer[url] || 'v1';\n\n  // jaringan palsu: null berarti offline\n  function jaringan(url, online) {\n    if (!online) return null;\n    return url + ' ' + versi(url);\n  }\n\n  langkah.forEach((baris, i) => {\n    const no = String(i + 1).padStart(2);\n    const [aksi, url, nilai] = baris.split(/\\s+/);\n    if (aksi === 'ubah') {\n      versiServer[url] = nilai;\n      console.log(no + ' server: ' + url + ' sekarang ' + nilai);\n      return;\n    }\n    const online = aksi === 'online';\n    const awal = no + ' ' + aksi.padEnd(7) + ' ' + url.padEnd(7) + ' -> ';\n    const disimpan = cache.get(url);\n\n    if (strategi === 'cache-first') {\n      if (disimpan) return console.log(awal + 'cache    ' + disimpan);\n      const r = jaringan(url, online);\n      if (!r) return console.log(awal + 'GAGAL (offline, belum ada di cache)');\n      cache.set(url, r);\n      return console.log(awal + 'jaringan ' + r + ' (disimpan)');\n    }\n\n    if (strategi === 'network-first') {\n      const r = jaringan(url, online);\n      if (r) {\n        cache.set(url, r);\n        return console.log(awal + 'jaringan ' + r + ' (disimpan)');\n      }\n      if (disimpan) return console.log(awal + 'cache    ' + disimpan + ' (cadangan offline)');\n      return console.log(awal + 'GAGAL (offline, belum ada di cache)');\n    }\n\n    // stale-while-revalidate\n    if (disimpan) {\n      const r = jaringan(url, online);\n      let catatan = '';\n      if (r && r !== disimpan) {\n        cache.set(url, r);\n        catatan = ' (latar: cache diperbarui ke ' + r.split(' ')[1] + ')';\n      }\n      return console.log(awal + 'cache    ' + disimpan + catatan);\n    }\n    const r = jaringan(url, online);\n    if (!r) return console.log(awal + 'GAGAL (offline, belum ada di cache)');\n    cache.set(url, r);\n    return console.log(awal + 'jaringan ' + r + ' (disimpan)');\n  });\n}\n\nfor (const s of ['cache-first', 'network-first', 'stale-while-revalidate']) simulasi(s);\n",
    },
    {
        "title": "Latihan 21: Framework Mini dengan Generator Situs Statis",
        "difficulty": "Sulit",
        "proyek": True,
        "question": [
            "Proyek akhir: gabungkan semua yang kamu bangun di kurikulum ini",
            "jadi framework mini yang menghasilkan situs statis. Pakai nama",
            "fungsi yang sama dengan bab 03: h, renderToString, signal,",
            "computed, effect. Semua dalam satu berkas, tanpa paket.",
            "",
            "1. Reaktivitas. signal(awal) mengembalikan objek dengan properti",
            "   value: membacanya di dalam effect mendaftarkan efek itu,",
            "   mengisinya dengan nilai berbeda (Object.is) menjalankan ulang",
            "   semua efek yang terdaftar. effect(fn) langsung menjalankan fn.",
            "   computed(fn) mengembalikan objek ber-value yang selalu sama",
            "   dengan fn() terbaru.",
            "2. Komponen. h(tag, props, ...anak) meratakan anak dan membuang",
            "   null/false/undefined ke medan anak, seperti bab 03; kalau tag",
            "   berupa fungsi (komponen), panggil dengan",
            "   { ...props, children }. renderToString meng-escape & < > \" di",
            "   teks dan atribut, dan elemen img, br, meta, link, input, hr",
            "   nggak diberi tag penutup.",
            "3. Pemeriksa aksesibilitas: setiap img tanpa atribut alt",
            "   menghasilkan peringatan (alt=\"\" untuk gambar hiasan itu sah).",
            "4. Data: judulSitus = signal('Kafe Senja') dan artikel = signal",
            "   berisi dua artikel: halo-dunia (Halo, dunia / Kafe kami resmi",
            "   buka.) dan menu-baru (Menu baru: es kopi & roti / Tersedia",
            "   mulai Senin.). jumlahArtikel = computed dari panjang artikel,",
            "   dan sebuah effect mencetak [efek] jumlah artikel: N.",
            "5. Halaman berbasis berkas: pages/index.js (h1 judul situs, p",
            "   jumlah artikel, ul daftar tautan ke /blog/slug/),",
            "   pages/tentang.js (h1 Tentang kami, img /kafe.jpg tanpa alt, img",
            "   /logo.png dengan alt kosong), dan pages/blog/[slug].js yang",
            "   menghasilkan satu halaman per artikel (article berisi h1 judul",
            "   dan p isi). Semua dibungkus komponen Layout: html lang=\"id\",",
            "   head berisi meta charset=\"utf-8\" dan title \"Judul | judul",
            "   situs\", body berisi nav (tautan Beranda ke / dan Tentang ke",
            "   /tentang/, dipisah satu spasi) lalu main.",
            "   Berkas keluaran: index.html, tentang/index.html,",
            "   blog/SLUG/index.html. Setiap HTML diawali <!doctype html>.",
            "6. Build: tulis ke folder dari",
            "   fs.mkdtempSync(path.join(os.tmpdir(), 'ssg-')). Cetak peringatan",
            "   aksesibilitas lebih dulu, lalu untuk tiap berkas (urut menurut",
            "   jalur relatifnya) cetak tulis kalau isinya baru atau berubah,",
            "   lewati kalau sama dengan isi yang sudah ada di disk, lalu",
            "   ringkasan. Jangan pernah mencetak jalur absolut.",
            "7. Jalankan build 1, tambahkan artikel jam-buka (judul Jam buka",
            "   <baru>, isi Buka 08.00-22.00.) dengan mengganti artikel.value,",
            "   jalankan build 2. Cetak daftar berkas relatif di folder",
            "   keluaran, isi blog/jam-buka/index.html, lalu hapus folder",
            "   sementara dan cetak buktinya.",
            "",
            "Keluaran yang diharapkan:",
            "",
            "[efek] jumlah artikel: 2",
            "Build 1:",
            "  peringatan a11y: tentang/index.html: <img src=\"/kafe.jpg\"> tanpa alt",
            "  tulis  blog/halo-dunia/index.html",
            "  tulis  blog/menu-baru/index.html",
            "  tulis  index.html",
            "  tulis  tentang/index.html",
            "  ringkasan: 4 halaman, 4 ditulis, 1 peringatan",
            "[efek] jumlah artikel: 3",
            "Build 2:",
            "  peringatan a11y: tentang/index.html: <img src=\"/kafe.jpg\"> tanpa alt",
            "  lewati blog/halo-dunia/index.html",
            "  tulis  blog/jam-buka/index.html",
            "  lewati blog/menu-baru/index.html",
            "  tulis  index.html",
            "  lewati tentang/index.html",
            "  ringkasan: 5 halaman, 2 ditulis, 1 peringatan",
            "Berkas di folder keluaran:",
            "  blog/halo-dunia/index.html",
            "  blog/jam-buka/index.html",
            "  blog/menu-baru/index.html",
            "  index.html",
            "  tentang/index.html",
            "Isi blog/jam-buka/index.html:",
            "<!doctype html><html lang=\"id\"><head><meta charset=\"utf-8\"><title>Jam buka &lt;baru&gt; | Kafe Senja</title></head><body><nav><a href=\"/\">Beranda</a> <a href=\"/tentang/\">Tentang</a></nav><main><article><h1>Jam buka &lt;baru&gt;</h1><p>Buka 08.00-22.00.</p></article></main></body></html>",
            "Folder sementara dihapus: true",
        ],
        "hints": [
            "Kerjakan bertahap dan uji tiap bagian sendiri: mulai dari signal dan effect, lalu h dan renderToString, baru router dan build.",
            "Supaya signal tahu siapa yang membacanya, simpan efek yang sedang berjalan di satu variabel global, isi sebelum fn dijalankan, dan kembalikan nilai lamanya sesudah selesai.",
            "Halaman dinamis punya fungsi jalur yang mengembalikan daftar params; ganti [slug] di nama berkas dengan nilai params untuk mendapat jalur keluaran.",
            "Untuk memutuskan tulis atau lewati, baca berkas tujuan kalau sudah ada dengan fs.existsSync dan fs.readFileSync, lalu bandingkan isinya dengan HTML baru.",
        ],
        "solution": "const fs = require('fs');\nconst os = require('os');\nconst path = require('path');\n\n// ---------- 1. reaktivitas: signal, computed, effect (bab 03) ----------\nlet efekAktif = null;\n\nfunction signal(awal) {\n  let nilai = awal;\n  const pelanggan = new Set();\n  return {\n    get value() {\n      if (efekAktif) pelanggan.add(efekAktif);\n      return nilai;\n    },\n    set value(baru) {\n      if (Object.is(baru, nilai)) return;\n      nilai = baru;\n      for (const f of [...pelanggan]) f();\n    },\n  };\n}\n\nfunction effect(fn) {\n  const jalan = () => {\n    const lama = efekAktif;\n    efekAktif = jalan;\n    try { fn(); } finally { efekAktif = lama; }\n  };\n  jalan();\n}\n\nfunction computed(fn) {\n  const hasil = signal(undefined);\n  effect(() => { hasil.value = fn(); });\n  return { get value() { return hasil.value; } };\n}\n\n// ---------- 2. komponen: h dan renderToString (bab 03) ----------\nconst KOSONG = new Set(['img', 'br', 'meta', 'link', 'input', 'hr']);\n\nfunction h(tag, props, ...anak) {\n  const datar = anak.flat(Infinity).filter((a) => a !== null && a !== false && a !== undefined);\n  if (typeof tag === 'function') return tag({ ...(props || {}), children: datar });\n  return { tag, props: props || {}, anak: datar };\n}\n\nfunction escape(teks) {\n  return String(teks).replace(/&/g, '&amp;').replace(/</g, '&lt;')\n    .replace(/>/g, '&gt;').replace(/\"/g, '&quot;');\n}\n\nfunction renderToString(v) {\n  if (typeof v === 'string' || typeof v === 'number') return escape(v);\n  const attr = Object.entries(v.props)\n    .map(([k, x]) => ' ' + k + '=\"' + escape(x) + '\"').join('');\n  if (KOSONG.has(v.tag)) return '<' + v.tag + attr + '>';\n  return '<' + v.tag + attr + '>' + v.anak.map(renderToString).join('') + '</' + v.tag + '>';\n}\n\n// ---------- 3. pemeriksa aksesibilitas (bab 02) ----------\nfunction periksaA11y(v, keluhan) {\n  if (typeof v !== 'object') return keluhan;\n  if (v.tag === 'img' && !('alt' in v.props)) {\n    keluhan.push('<img src=\"' + v.props.src + '\"> tanpa alt');\n  }\n  v.anak.forEach((a) => periksaA11y(a, keluhan));\n  return keluhan;\n}\n\n// ---------- 4. data situs ----------\nconst judulSitus = signal('Kafe Senja');\nconst artikel = signal([\n  { slug: 'halo-dunia', judul: 'Halo, dunia', isi: 'Kafe kami resmi buka.' },\n  { slug: 'menu-baru', judul: 'Menu baru: es kopi & roti', isi: 'Tersedia mulai Senin.' },\n]);\nconst jumlahArtikel = computed(() => artikel.value.length);\neffect(() => console.log('[efek] jumlah artikel: ' + jumlahArtikel.value));\n\n// ---------- 5. layout dan halaman (router berbasis berkas, bab 12) ----------\nfunction Layout({ judul, children }) {\n  return h('html', { lang: 'id' },\n    h('head', null, h('meta', { charset: 'utf-8' }), h('title', null, judul + ' | ' + judulSitus.value)),\n    h('body', null,\n      h('nav', null, h('a', { href: '/' }, 'Beranda'), ' ', h('a', { href: '/tentang/' }, 'Tentang')),\n      h('main', null, children)));\n}\n\nconst halaman = {\n  'pages/index.js': {\n    render: () => h(Layout, { judul: 'Beranda' },\n      h('h1', null, judulSitus.value),\n      h('p', null, jumlahArtikel.value + ' artikel'),\n      h('ul', null, artikel.value.map((a) => h('li', null, h('a', { href: '/blog/' + a.slug + '/' }, a.judul))))),\n  },\n  'pages/tentang.js': {\n    render: () => h(Layout, { judul: 'Tentang' },\n      h('h1', null, 'Tentang kami'),\n      h('img', { src: '/kafe.jpg' }),\n      h('img', { src: '/logo.png', alt: '' })),\n  },\n  'pages/blog/[slug].js': {\n    jalur: () => artikel.value.map((a) => ({ slug: a.slug })),\n    render: ({ slug }) => {\n      const a = artikel.value.find((x) => x.slug === slug);\n      return h(Layout, { judul: a.judul }, h('article', null, h('h1', null, a.judul), h('p', null, a.isi)));\n    },\n  },\n};\n\nfunction keBerkasKeluaran(berkas, params) {\n  let rute = berkas.replace(/^pages\\//, '').replace(/\\.js$/, '');\n  rute = rute.replace(/\\[(\\w+)\\]/g, (_, n) => params[n]);\n  if (rute === 'index') return 'index.html';\n  return rute.replace(/\\/index$/, '') + '/index.html';\n}\n\n// ---------- 6. build ke folder sementara ----------\nconst keluar = fs.mkdtempSync(path.join(os.tmpdir(), 'ssg-'));\n\nfunction build(ke) {\n  console.log('Build ' + ke + ':');\n  const tugas = [];\n  for (const berkas of Object.keys(halaman).sort()) {\n    const hal = halaman[berkas];\n    const daftar = hal.jalur ? hal.jalur() : [{}];\n    for (const params of daftar) tugas.push({ berkas, params, hal });\n  }\n  let peringatan = 0;\n  const hasil = tugas.map(({ berkas, params, hal }) => {\n    const pohon = hal.render(params);\n    const html = '<!doctype html>' + renderToString(pohon);\n    const relatif = keBerkasKeluaran(berkas, params);\n    const tujuan = path.join(keluar, relatif);\n    const lama = fs.existsSync(tujuan) ? fs.readFileSync(tujuan, 'utf8') : null;\n    for (const k of periksaA11y(pohon, [])) {\n      peringatan++;\n      console.log('  peringatan a11y: ' + relatif + ': ' + k);\n    }\n    return { relatif, tujuan, html, lama };\n  }).sort((a, b) => (a.relatif < b.relatif ? -1 : 1));\n  let ditulis = 0;\n  for (const x of hasil) {\n    if (x.lama === x.html) {\n      console.log('  lewati ' + x.relatif);\n      continue;\n    }\n    fs.mkdirSync(path.dirname(x.tujuan), { recursive: true });\n    fs.writeFileSync(x.tujuan, x.html);\n    ditulis++;\n    console.log('  tulis  ' + x.relatif);\n  }\n  console.log('  ringkasan: ' + hasil.length + ' halaman, ' + ditulis + ' ditulis, ' + peringatan + ' peringatan');\n}\n\nbuild(1);\nartikel.value = [...artikel.value, { slug: 'jam-buka', judul: 'Jam buka <baru>', isi: 'Buka 08.00-22.00.' }];\nbuild(2);\n\nfunction daftarBerkas(dir, awalan = '') {\n  return fs.readdirSync(dir, { withFileTypes: true }).flatMap((e) => (e.isDirectory()\n    ? daftarBerkas(path.join(dir, e.name), awalan + e.name + '/')\n    : [awalan + e.name])).sort();\n}\n\nconsole.log('Berkas di folder keluaran:');\nfor (const b of daftarBerkas(keluar)) console.log('  ' + b);\nconsole.log('Isi blog/jam-buka/index.html:');\nconsole.log(fs.readFileSync(path.join(keluar, 'blog/jam-buka/index.html'), 'utf8'));\n\nfs.rmSync(keluar, { recursive: true, force: true });\nconsole.log('Folder sementara dihapus: ' + !fs.existsSync(keluar));\n",
    },
]
