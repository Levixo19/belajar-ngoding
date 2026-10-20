"""Kurikulum Frontend Modern.

Dirakit alat/rakit_kurikulum.py dari draf per bab (2026-10-19).
Sesudah dirakit, berkas ini disunting seperti kurikulum lain
(alat/ganti_badan.py, alat/tambah_bagian.py). <KEY>_BAB tetap
spesifikasi JUMLAH; rentangnya dihitung data/kurikulum_tech.py.
"""

FRONTEND_BAB = [
    {
        "judul": "Dari Halaman Statis ke Aplikasi Frontend",
        "ket": "Kenapa framework ada, lalu Node.js, npm, dan manajer paket sebagai alat kerja harian.",
        "tingkat": "dasar",
        "jumlah": 3,
    },
    {
        "judul": "Aksesibilitas Sejak Baris Pertama",
        "ket": "WCAG 2.2, WAI-ARIA, alat uji otomatis, dan mencoba pembaca layar sungguhan di Fedora.",
        "tingkat": "dasar",
        "jumlah": 4,
    },
    {
        "judul": "Komponen dan Reaktivitas dari Nol",
        "ket": "Membangun sendiri komponen, virtual DOM, signal, dan render di server supaya framework apa pun terasa familier.",
        "tingkat": "dasar",
        "jumlah": 4,
    },
    {
        "judul": "Menata Gaya: Tailwind dan Pipeline CSS",
        "ket": "Tailwind CSS v4 dari kelas utility sampai tema, Sass dan PostCSS, lalu peta cara lain menata gaya.",
        "tingkat": "dasar",
        "jumlah": 4,
    },
    {
        "judul": "Build Tool, TypeScript, dan Kualitas Kode",
        "ket": "Cara kerja bundler, Vite 8 dengan Rolldown, peta build tool, TypeScript di proyek frontend, serta linter dan formatter.",
        "tingkat": "menengah",
        "jumlah": 5,
    },
    {
        "judul": "React: Komponen, State, dan Hooks",
        "ket": "Framework UI paling banyak dipakai: JSX, state dan hooks, fitur React modern, dan mengetik komponen dengan TypeScript.",
        "tingkat": "menengah",
        "jumlah": 4,
    },
    {
        "judul": "Ekosistem React: Rute, Data, State, dan Form",
        "ket": "Pustaka yang hampir selalu menemani React: router, server state, client state, serta form beserta validasinya.",
        "tingkat": "menengah",
        "jumlah": 4,
    },
    {
        "judul": "Vue: Reaktif dan Ramah Pemula",
        "ket": "Template dan reaktivitas Vue, Composition API dengan komponen satu berkas, lalu Pinia, Vue Router, dan ekosistemnya.",
        "tingkat": "menengah",
        "jumlah": 3,
    },
    {
        "judul": "Angular: Framework Lengkap untuk Tim Besar",
        "ket": "Komponen standalone dan signals, dependency injection dan RxJS, lalu peta ekosistem Angular dan warisan AngularJS.",
        "tingkat": "menengah",
        "jumlah": 3,
    },
    {
        "judul": "Svelte, HTML dari Server, dan Framework Lain",
        "ket": "Svelte 5 dan SvelteKit, htmx/Alpine/Hotwire, peta framework lain, dan cara membaca kode frontend warisan.",
        "tingkat": "menengah",
        "jumlah": 5,
    },
    {
        "judul": "Testing Frontend",
        "ket": "Dari unit test sampai end-to-end: node:test dan Vitest, Testing Library, mock API dengan MSW, Storybook, dan Playwright.",
        "tingkat": "menengah",
        "jumlah": 4,
    },
    {
        "judul": "Meta-framework Full-stack",
        "ket": "Next.js dari App Router sampai deploy, Nuxt dan Astro, lalu peta meta-framework dan generator situs statis.",
        "tingkat": "mahir",
        "jumlah": 4,
    },
    {
        "judul": "Design System, Animasi, dan Monorepo",
        "ket": "Komponen headless dan shadcn/ui, peta pustaka komponen, animasi dan grafis, lalu monorepo untuk proyek yang tumbuh besar.",
        "tingkat": "mahir",
        "jumlah": 3,
    },
    {
        "judul": "PWA, WebAssembly, dan di Luar Browser",
        "ket": "Aplikasi web yang jalan offline, WebAssembly dari Node, desktop dan mobile berbasis web, runtime alternatif, dan deploy.",
        "tingkat": "mahir",
        "jumlah": 4,
    },
]

FRONTEND_MATERIALS = [
    {
        "title": "1. Kenapa Framework Frontend Ada",
        "sections": [
            {
                "body": [
                    "Di kurikulum JavaScript bab 6 kamu sudah bisa bikin halaman yang hidup:",
                    "ambil elemen pakai querySelector, pasang event listener, lalu ubah",
                    "textContent waktu tombol diklik. Untuk satu tombol dan satu angka, cara",
                    "itu cukup.",
                    "",
                    "Masalahnya muncul waktu halamannya tumbuh. Bayangkan toko online kecil.",
                    "Begitu pembeli menekan \"Tambah ke keranjang\", banyak bagian harus ikut",
                    "berubah. Angka di ikon keranjang naik, total harga bertambah, daftar di",
                    "panel samping memanjang, dan tombol \"Bayar\" yang tadinya mati jadi",
                    "aktif. Semua itu tampilan dari satu data yang sama, yaitu isi keranjang.",
                    "",
                    "Kalau kamu mengubah DOM satu per satu, kamu harus ingat semua tempat itu",
                    "setiap kali datanya berubah. Lupa satu, tampilannya jadi nggak cocok",
                    "dengan datanya. Ikon bilang 3 barang, panel samping bilang 2. Bug",
                    "semacam ini nggak bikin error di konsol, jadi susah ketahuan.",
                ],
            },
            {
                "heading": "Cara lama: ubah DOM satu per satu",
                "bahasa": "browser",
                "code": """const keranjang = [];

function tambah(barang) {
  keranjang.push(barang);
  // Tiap tempat yang menampilkan keranjang harus diurus sendiri.
  document.querySelector('#jumlah').textContent = keranjang.length;
  const total = keranjang.reduce((t, b) => t + b.harga, 0);
  document.querySelector('#total').textContent = 'Rp' + total;
  document.querySelector('#bayar').disabled = false;
  // Panel samping lupa diperbarui. Nggak ada yang protes.
}""",
            },
            {
                "heading": "Cara framework: tampilan sebagai fungsi dari data",
                "body": [
                    "Framework membalik cara berpikirnya. Kamu nggak lagi menulis \"ubah",
                    "elemen ini, lalu elemen itu\". Kamu menulis satu fungsi yang menjawab",
                    "\"kalau datanya begini, tampilannya seperti apa\". Data itu disebut state,",
                    "yaitu keadaan aplikasi saat ini. Setiap kali state berubah, fungsi",
                    "tampilan dipanggil ulang, dan framework yang mengurus perubahan di DOM.",
                    "",
                    "Contoh di bawah meniru ide itu di Node, tanpa browser. Tampilannya cuma",
                    "sebaris teks, tapi polanya sama: satu fungsi tampilan, satu tempat",
                    "render, dan perubahan data selalu lewat jalur yang sama.",
                ],
                "code": """// Tampilan ditulis sebagai fungsi dari data (state).
function tampilan(state) {
  let jumlah = 0;
  let total = 0;
  for (const b of state.isi) {
    jumlah += b.qty;
    total += b.harga * b.qty;
  }
  return `Keranjang (${jumlah}) | Total Rp${total}`;
}

const state = { isi: [] };

function render() {
  console.log(tampilan(state)); // satu-satunya tempat tampilan dibuat
}

function tambah(nama, harga) {
  const ada = state.isi.find((b) => b.nama === nama);
  if (ada) ada.qty += 1;
  else state.isi.push({ nama, harga, qty: 1 });
  render();
}

render();
tambah('Kopi susu', 18000);
tambah('Roti bakar', 15000);
tambah('Kopi susu', 18000);""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  Keranjang (0) | Total Rp0",
                    "  Keranjang (1) | Total Rp18000",
                    "  Keranjang (2) | Total Rp33000",
                    "  Keranjang (3) | Total Rp51000",
                    "",
                    "Perhatikan fungsi tambah. Ia cuma mengubah data lalu memanggil render.",
                    "Ia nggak tahu apa saja yang tampil di layar. Kalau besok ada bagian",
                    "tampilan baru, misalnya \"gratis ongkir kalau di atas Rp50000\", kamu",
                    "cukup mengubah fungsi tampilan. Fungsi tambah, kurang, dan hapus nggak",
                    "perlu disentuh.",
                    "",
                    "Di browser sungguhan, membuang seluruh DOM lalu membuat ulang tiap kali",
                    "ada perubahan itu boros dan bikin fokus input hilang. Jadi framework",
                    "membandingkan tampilan lama dengan yang baru, lalu cuma mengubah bagian",
                    "yang beda. Caranya kamu bangun sendiri di bab 3.",
                ],
            },
            {
                "heading": "Yang dikerjakan framework untukmu",
                "body": [
                    "Hampir semua framework frontend modern memberi lima hal yang sama, cuma",
                    "cara menulisnya yang beda:",
                    "",
                    "- Komponen. Potongan tampilan yang bisa dipakai ulang, misalnya",
                    "  KartuProduk, dipakai 20 kali dengan data berbeda.",
                    "- Reaktivitas. Tampilan ikut berubah otomatis waktu state berubah, tanpa",
                    "  kamu memanggil querySelector.",
                    "- Pembaruan DOM yang hemat. Yang diubah cuma bagian yang memang berubah.",
                    "- Rute. Pindah \"halaman\" tanpa memuat ulang seluruh situs.",
                    "- Ekosistem. Pustaka form, tabel, grafik, dan pengujian yang sudah dibuat",
                    "  orang lain untuk framework itu.",
                    "",
                    "Framework juga punya biaya. Ada yang harus dipelajari, ada kode yang",
                    "ikut dikirim ke browser, dan ada proses build sebelum halamannya bisa",
                    "dibuka. Untuk halaman profil, blog, atau undangan pernikahan, HTML dan",
                    "CSS biasa sering sudah cukup. Untuk aplikasi yang datanya sering",
                    "berubah, seperti dasbor, kasir, atau aplikasi chat, framework mulai",
                    "sepadan dengan biayanya.",
                ],
            },
            {
                "heading": "Siapa yang menjalankan semua ini: mesin JavaScript",
                "body": [
                    "Kode framework tetap JavaScript biasa, dan yang menjalankannya adalah",
                    "mesin JavaScript di dalam browser. Tiap browser besar punya mesinnya",
                    "sendiri:",
                    "",
                    "  Mesin           Dipakai di             Lisensi",
                    "  V8              Chrome, Edge, Node.js  BSD-3-Clause",
                    "  SpiderMonkey    Firefox                MPL-2.0",
                    "  JavaScriptCore  Safari, Bun            LGPL-2.1/BSD",
                    "",
                    "Ketiganya mengikuti standar yang sama (ECMAScript), jadi kode yang sama",
                    "jalan di semuanya. Versinya ikut rilis browser, kira-kira tiap empat",
                    "minggu, jadi nggak ada satu nomor versi yang perlu kamu hafal.",
                    "ChakraCore, mesin Edge versi lama, sudah ditinggalkan.",
                    "",
                    "Node.js memakai V8 yang sama dengan Chrome, ditambah akses ke berkas dan",
                    "jaringan. Karena itu contoh di atas bisa jalan di aplikasi ini: kamu",
                    "nggak butuh browser untuk menjalankan logika tampilan, cuma untuk",
                    "menggambarnya.",
                ],
            },
            {
                "heading": "Peta perjalanan kurikulum ini",
                "body": [
                    "Ekosistem frontend kelihatan ruwet karena namanya banyak sekali. Tapi",
                    "isinya bisa dikelompokkan, dan kurikulum ini melewatinya berurutan:",
                    "",
                    "- Alat kerja: Node.js, npm, pnpm (bab ini).",
                    "- Aksesibilitas: supaya aplikasimu bisa dipakai semua orang (bab 2).",
                    "- Komponen dan reaktivitas dari nol: virtual DOM, signal, render di server",
                    "  (bab 3).",
                    "- Menata gaya: Tailwind, Sass, CSS Modules (bab 4).",
                    "- Build tool, TypeScript, dan kualitas kode (bab 5).",
                    "- Framework UI: React, Vue, Angular, Svelte, dan yang lain (bab 6 sampai",
                    "  10).",
                    "- Testing, meta-framework seperti Next.js, design system, lalu PWA dan",
                    "  WebAssembly (bab 11 sampai 14).",
                    "",
                    "React yang paling banyak dipakai: 44,7% responden Survei Stack Overflow",
                    "2025 memakainya, dan Vue 17,6%. Tapi konsep di bab 3 berlaku di semua",
                    "framework, jadi pindah framework nanti nggak berarti mulai dari nol.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aplikasi kasir berbasis web yang dipakai warung dan kafe, seperti yang",
                    "banyak dijual sebagai layanan langganan, hampir selalu dibangun dengan",
                    "framework. Satu transaksi mengubah daftar pesanan, subtotal, pajak,",
                    "kembalian, dan stok sekaligus, dan semuanya harus tetap cocok satu sama",
                    "lain.",
                    "",
                    "Kasus kecil: halaman pesanan kafe temanmu ditulis dengan DOM manual, dan",
                    "kadang total di bawah nggak sama dengan jumlah harga di daftar. Kamu",
                    "diminta memperbaikinya tanpa langsung pindah ke framework.",
                    "",
                    "Cara memecahkannya:",
                    "1. Kumpulkan semua data pesanan ke satu objek state, misalnya { pesanan:",
                    "   [...], diskon: 0 }.",
                    "2. Tulis satu fungsi render(state) yang membuat ulang seluruh bagian",
                    "   pesanan dari state itu.",
                    "3. Ubah semua event handler supaya cuma mengubah state lalu memanggil",
                    "   render(), nggak menyentuh DOM sendiri.",
                    "4. Kalau halamannya terus tumbuh dan render ulang mulai terasa lambat atau",
                    "   fokus input hilang, saat itulah framework layak dipasang. Logika",
                    "   state-nya bisa dibawa apa adanya.",
                ],
            },
        ],
    },
    {
        "title": "2. Node.js dan npm sebagai Alat Kerja",
        "sections": [
            {
                "body": [
                    "Aplikasi frontend jalan di browser, tapi hampir semua alat untuk",
                    "membuatnya jalan di Node.js. Vite yang menyalakan server pengembangan,",
                    "ESLint yang memeriksa kode, Tailwind yang membuat berkas CSS, semuanya",
                    "program JavaScript yang dijalankan Node di komputermu. Jadi walaupun",
                    "kamu nggak pernah menulis server, Node tetap jadi alat kerja harian.",
                    "",
                    "Node.js adalah program yang menjalankan JavaScript di luar browser.",
                    "Isinya mesin V8 dari Chrome ditambah akses ke berkas, proses, dan",
                    "jaringan. Di Survei Stack Overflow 2025, Node.js ada di peringkat",
                    "pertama kategori web framework dan teknologi, dipakai 48,7% responden.",
                ],
            },
            {
                "heading": "Current dan LTS",
                "body": [
                    "Node punya dua jalur rilis. Current berisi fitur terbaru dan berganti",
                    "cepat. LTS (Long Term Support) adalah versi yang dijamin menerima",
                    "perbaikan keamanan selama kira-kira dua setengah tahun. Untuk belajar",
                    "dan untuk proyek sungguhan, pakai LTS.",
                    "",
                    "Saat materi ini ditulis (Oktober 2026), rilis Current adalah Node",
                    "26.12.0. Node 24 dengan nama sandi Krypton adalah LTS aktif, Node 22",
                    "masih LTS dalam masa perawatan, dan Node 20 sudah berhenti didukung",
                    "sejak Maret 2026.",
                    "",
                    "Selama ini nomor ganjil nggak pernah jadi LTS, sedangkan nomor genap",
                    "jadi LTS. Pola itu berakhir: mulai Node 27, Node merilis satu versi",
                    "besar per tahun dan setiap rilis akan jadi LTS. Kalau kamu membaca",
                    "tutorial lama yang bilang \"jangan pakai versi ganjil\", aturan itu cuma",
                    "berlaku sampai Node 26.",
                ],
            },
            {
                "heading": "Memasang dan memeriksa",
                "bahasa": "terminal",
                "code": """# Fedora (lihat kurikulum CLI Fedora bab 5 soal dnf)
sudo dnf install nodejs

node --version
npm --version

# menjalankan berkas JavaScript
node halo.js

# Node 22.18 ke atas dan Node 24 bisa langsung menjalankan .ts
node halo.ts""",
            },
            {
                "body": [
                    "Baris terakhir itu fitur yang namanya type stripping. Node membuang",
                    "anotasi tipe TypeScript lalu menjalankan sisanya. Ia nggak memeriksa",
                    "apakah tipenya benar; untuk itu tetap butuh tsc, yang dibahas di bab 5.",
                    "Fitur TypeScript yang menghasilkan kode, seperti enum, juga belum bisa",
                    "dijalankan dengan cara ini.",
                    "",
                    "npm ikut terpasang bersama Node. npm itu dua hal sekaligus: program di",
                    "terminal untuk memasang paket, dan registri di npmjs.com, yaitu gudang",
                    "paket JavaScript terbesar. Versi npm terbaru saat materi ini ditulis",
                    "adalah 12.2.0.",
                ],
            },
            {
                "heading": "package.json: KTP sebuah proyek",
                "bahasa": "json",
                "code": """{
  "name": "toko-kopi",
  "version": "0.1.0",
  "private": true,
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "test": "node --test"
  },
  "dependencies": {
    "react": "^19.3.1"
  },
  "devDependencies": {
    "vite": "^8.0.0"
  },
  "engines": {
    "node": ">=24"
  }
}""",
            },
            {
                "body": [
                    "Setiap proyek JavaScript punya berkas package.json di akarnya. Kalau",
                    "kamu membuka proyek orang lain, baca berkas ini dulu:",
                    "",
                    "- name dan version: identitas proyek. private: true mencegah proyek ini",
                    "  tak sengaja diterbitkan ke registri.",
                    "- type: \"module\" artinya berkas .js memakai import/export (ES Module).",
                    "  Tanpa baris ini, Node menganggapnya CommonJS (require). Mencampur",
                    "  keduanya adalah sumber error paling sering bagi pemula (lihat kurikulum",
                    "  JavaScript bab 7).",
                    "- scripts: perintah pendek. npm run dev menjalankan vite, npm test",
                    "  menjalankan node --test.",
                    "- dependencies: paket yang dibutuhkan aplikasi saat dipakai.",
                    "- devDependencies: paket yang cuma dibutuhkan saat membangun dan menguji,",
                    "  seperti Vite, ESLint, dan Vitest.",
                    "- engines: versi Node yang didukung proyek.",
                ],
            },
            {
                "heading": "Perintah npm yang dipakai tiap hari",
                "bahasa": "terminal",
                "code": """npm init -y              # bikin package.json baru
npm install              # pasang semua yang tertulis di package.json
npm install dayjs        # tambah paket ke dependencies
npm install -D vitest    # tambah paket ke devDependencies
npm run dev              # jalankan script "dev"
npx eslint .             # jalankan alat dari paket tanpa memasang global
npm ci                   # pasang persis sesuai lockfile (untuk CI)
npm outdated             # lihat paket yang punya versi lebih baru
npm audit                # cek celah keamanan yang sudah diketahui""",
            },
            {
                "heading": "Semver: membaca ^ dan ~",
                "body": [
                    "Nomor versi paket npm memakai semver (semantic versioning), tiga angka",
                    "yang dipisah titik: mayor.minor.patch. Naik patch berarti perbaikan bug,",
                    "naik minor berarti fitur baru yang nggak merusak kode lama, naik mayor",
                    "berarti ada perubahan yang bisa merusak kode lama.",
                    "",
                    "Di package.json, nomor versi biasanya diberi awalan. Awalan itu",
                    "menentukan versi mana saja yang boleh dipasang:",
                    "",
                    "  Tertulis   Boleh dipasang          Contoh yang cocok",
                    "  ^1.4.2     >=1.4.2 dan <2.0.0       1.4.2, 1.5.0, 1.10.3",
                    "  ~1.4.2     >=1.4.2 dan <1.5.0       1.4.2, 1.4.9",
                    "  1.4.2      persis 1.4.2             1.4.2 saja",
                    "  ^0.4.2     >=0.4.2 dan <0.5.0       0.4.2, 0.4.7",
                    "",
                    "Baris terakhir sering bikin kaget. Untuk versi 0.x, semver menganggap",
                    "minor sebagai perubahan besar, jadi ^ cuma mengizinkan patch. Satu lagi:",
                    "versi dibandingkan per angka, bukan per huruf. 1.10.3 lebih baru",
                    "daripada 1.4.7, walaupun kalau diurutkan sebagai teks \"1.10\" muncul",
                    "lebih dulu.",
                ],
            },
            {
                "heading": "Lockfile dan node_modules",
                "body": [
                    "Karena ^1.4.2 bisa berarti 1.4.2 hari ini dan 1.9.0 bulan depan, dua",
                    "orang yang menjalankan npm install di hari berbeda bisa mendapat versi",
                    "berbeda. Lockfile mencegah itu. Berkas package-lock.json mencatat versi",
                    "persis setiap paket yang terpasang, termasuk paket yang dibutuhkan",
                    "paketmu, yang jumlahnya bisa ratusan.",
                    "",
                    "Aturannya sederhana:",
                    "",
                    "- package.json dan package-lock.json di-commit ke git.",
                    "- node_modules nggak di-commit. Tulis node_modules/ di .gitignore. Folder",
                    "  itu bisa dibuat ulang kapan saja dengan npm install.",
                    "- Di server CI, pakai npm ci. Perintah itu memasang persis isi lockfile",
                    "  dan gagal kalau lockfile nggak cocok dengan package.json.",
                    "",
                    "Jebakan: menghapus package-lock.json \"supaya error-nya hilang\". Yang",
                    "terjadi, semua paket naik ke versi terbaru yang diizinkan sekaligus, dan",
                    "bug baru bisa datang dari paket mana pun.",
                ],
            },
            {
                "heading": "Keamanan rantai pasok",
                "body": [
                    "Setiap paket yang kamu pasang menjalankan kode orang lain di komputermu.",
                    "Pada September 2025 muncul cacing (worm) bernama Shai-Hulud di registri",
                    "npm. Ia mencuri token npm dari komputer pengelola paket, lalu memakai",
                    "token itu untuk menerbitkan versi beracun dari paket-paket lain milik",
                    "orang yang sama. Ratusan paket kena.",
                    "",
                    "Sesudah itu npm memperketat aturan. Pada 9 Desember 2025 semua classic",
                    "token dicabut permanen. Token tulis yang baru wajib granular dan paling",
                    "lama berlaku 90 hari, dan npm mendorong trusted publishing, yaitu",
                    "menerbitkan paket langsung dari CI tanpa token yang disimpan.",
                    "",
                    "Kebiasaan aman yang bisa kamu mulai sekarang:",
                    "",
                    "- Ketik nama paket dengan teliti. Paket palsu sering memakai nama yang",
                    "  mirip, misalnya beda satu huruf.",
                    "- Commit lockfile, dan pakai npm ci di CI.",
                    "- Jalankan npm audit sesekali, dan baca dulu sebelum menjalankan npm audit",
                    "  fix --force.",
                    "- Perhatikan skrip pemasangan. npm versi baru, misalnya 11.19 yang",
                    "  terpasang di Fedora 44 saat materi ini ditulis, memblokir skrip",
                    "  pemasangan milik dependensi secara bawaan dan menutup npm install dengan",
                    "  daftar paket yang skripnya dilewati. Izinkan cuma paket yang memang",
                    "  butuh, lewat npm install-scripts approve nama-paket; izinnya dicatat di",
                    "  field allowScripts di package.json.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Proyek frontend open source di GitHub hampir selalu dibuka dengan",
                    "langkah yang sama di README-nya: clone, npm install (atau pnpm install),",
                    "lalu npm run dev. Kalau kamu PKL di tim web, langkah pertama di hari",
                    "pertama biasanya juga itu.",
                    "",
                    "Kasus kecil: kamu clone proyek kantor, menjalankan npm install, lalu npm",
                    "run dev gagal dengan error \"Unexpected token 'export'\". Teman setim",
                    "bilang di laptopnya jalan.",
                    "",
                    "Cara memecahkannya:",
                    "1. Cek versi Node-mu dengan node --version, lalu bandingkan dengan engines",
                    "   di package.json atau berkas .nvmrc.",
                    "2. Kalau beda, pasang versi yang diminta proyek (manajer versi Node",
                    "   dibahas di materi berikutnya).",
                    "3. Pastikan kamu memakai lockfile yang di-commit: hapus folder",
                    "   node_modules, lalu jalankan npm ci, bukan npm install.",
                    "4. Kalau masih gagal, cek field type di package.json. Error itu khas",
                    "   berkas ES Module yang dibaca sebagai CommonJS.",
                ],
            },
        ],
    },
    {
        "title": "3. pnpm, Yarn, dan Manajer Versi Node",
        "sections": [
            {
                "body": [
                    "npm sudah cukup untuk belajar. Tapi begitu kamu membuka proyek orang",
                    "lain, kamu akan ketemu berkas pnpm-lock.yaml, yarn.lock, atau bun.lock,",
                    "dan berkas kecil bernama .nvmrc. Materi ini peta singkat untuk dua",
                    "urusan itu: manajer paket selain npm, dan alat untuk memakai versi Node",
                    "yang berbeda di tiap proyek.",
                    "",
                    "Aturan paling penting dulu: satu proyek, satu manajer paket. Lihat",
                    "lockfile yang ada di repositori, lalu pakai manajer paket yang sama.",
                    "Menjalankan npm install di proyek pnpm menghasilkan lockfile kedua dan",
                    "versi paket yang bisa berbeda.",
                ],
            },
            {
                "heading": "Peta manajer paket dan registri",
                "bahasa": "teks",
                "code": """Nama         Lockfile            Status          Kapan dipilih
npm          package-lock.json   aktif           bawaan Node, aman untuk mulai
pnpm         pnpm-lock.yaml      aktif, naik     hemat disk, monorepo
Yarn 4       yarn.lock           stabil-matang   proyek yang sudah memakainya
Yarn 1       yarn.lock           dibekukan       cuma di kode lama
bun install  bun.lock            aktif           proyek yang memakai Bun
Bower        bower.json          usang           jangan untuk proyek baru
JSR          (registri)          aktif           paket TypeScript, ekosistem Deno
Corepack     (pengatur versi)    menurun         dipasang sendiri sejak Node 25""",
            },
            {
                "heading": "pnpm",
                "body": [
                    "pnpm menyimpan setiap versi paket satu kali saja di satu gudang di",
                    "komputermu, lalu menautkannya ke node_modules tiap proyek. Sepuluh",
                    "proyek yang memakai React yang sama nggak menyimpan sepuluh salinan.",
                    "Pemasangannya juga cepat karena paket yang sudah ada di gudang nggak",
                    "diunduh ulang.",
                    "",
                    "Bedanya yang paling terasa: node_modules pnpm nggak rata. Paketmu cuma",
                    "bisa memakai paket yang memang tertulis di package.json-nya. Kode yang",
                    "memakai paket tanpa menuliskannya di package.json akan error. Itu",
                    "disengaja, karena kode seperti itu juga rawan rusak di npm.",
                    "",
                    "Mulai pnpm 10, skrip pemasangan milik dependensi nggak dijalankan",
                    "otomatis; kamu harus mengizinkan paket tertentu secara eksplisit. npm",
                    "versi baru kini melakukan hal yang sama. Ini menutup salah satu jalan",
                    "masuk serangan rantai pasok. Di Survei Stack Overflow 2025 pnpm dipakai",
                    "13,4% responden, dan di State of JS 2025 ia jadi alat monorepo nomor",
                    "satu. Versi terbaru saat materi ini ditulis adalah 12.14.0.",
                ],
            },
            {
                "heading": "Perintahnya mirip npm",
                "bahasa": "terminal",
                "code": """npm install -g pnpm     # sekali saja
pnpm install            # setara npm install
pnpm add dayjs          # setara npm install dayjs
pnpm add -D vitest      # devDependencies
pnpm dev                # script boleh dipanggil tanpa 'run'
pnpm dlx create-vite    # setara npx""",
            },
            {
                "heading": "Yarn, Bun, JSR, dan Bower",
                "body": [
                    "Yarn dibuat Facebook pada 2016, waktu npm masih lambat dan belum punya",
                    "lockfile. Yarn modern (versi 2 ke atas, dijuluki Berry) kini di versi",
                    "4.18 dan punya fitur Plug'n'Play yang bisa bekerja tanpa folder",
                    "node_modules. Yarn 1 (Classic) dibekukan di 1.22.22 dan cuma menerima",
                    "perbaikan kritis. Jebakan klasiknya: perintah yarn di komputermu",
                    "ternyata Yarn 1, padahal proyeknya memakai Yarn 4. Versi yang dipakai",
                    "proyek tertulis di field packageManager di package.json. Di Survei Stack",
                    "Overflow 2025, Yarn dipakai 21,1% responden.",
                    "",
                    "bun install adalah manajer paket bawaan Bun, runtime JavaScript yang",
                    "dibahas di bab 14. Ia membaca package.json yang sama dan terkenal cepat.",
                    "Kamu boleh memakainya walau aplikasinya tetap dijalankan dengan Node.",
                    "",
                    "JSR (jsr.io) adalah registri paket buatan tim Deno. Paketnya diterbitkan",
                    "sebagai TypeScript dan bisa dipasang dari npm, pnpm, Yarn, Bun, maupun",
                    "Deno, misalnya dengan npx jsr add @std/path.",
                    "",
                    "Bower adalah manajer paket khusus frontend dari era 2012 sampai 2017,",
                    "sebelum npm dipakai untuk kode browser. Pengelolanya sendiri menyarankan",
                    "pindah, dan rilis terakhirnya tahun 2022. Masih ada di kode lama; jangan",
                    "dipilih untuk proyek baru.",
                ],
            },
            {
                "heading": "Corepack: dulu bawaan, sekarang tidak",
                "body": [
                    "Corepack adalah alat kecil dari tim Node yang membaca field",
                    "packageManager lalu otomatis memakai versi pnpm atau Yarn yang diminta",
                    "proyek. Selama beberapa tahun ia ikut terpasang bersama Node. Mulai Node",
                    "25, Corepack nggak lagi disertakan, jadi kalau kamu butuh, pasang",
                    "sendiri dengan npm install -g corepack. Tutorial yang bilang \"cukup",
                    "jalankan corepack enable\" ditulis sebelum perubahan itu.",
                ],
            },
            {
                "heading": "Manajer versi Node",
                "body": [
                    "Proyek kantor A minta Node 22, proyek latihanmu memakai Node 24.",
                    "Memasang dan mencopot Node bolak-balik itu melelahkan. Manajer versi",
                    "memasang beberapa versi Node berdampingan dan berpindah otomatis sesuai",
                    "proyek.",
                    "",
                    "  Alat    Ditulis dengan  Berkas proyek       Status",
                    "  nvm     shell (bash)    .nvmrc              aktif, paling banyak",
                    "  n       bash            .node-version       stabil, sederhana",
                    "  fnm     Rust            .nvmrc              aktif, jalan di Windows",
                    "  mise    Rust            mise.toml           aktif, banyak bahasa",
                    "  Volta   Rust            package.json        usang sejak Nov 2025",
                    "",
                    "nvm paling banyak dipakai: 6.218 responden State of JS 2025, nomor tiga",
                    "di daftar utilitas sesudah ESLint dan Prettier. Ia cuma untuk Linux dan",
                    "macOS; Windows memakai proyek terpisah, nvm-windows. n adalah satu skrip",
                    "bash yang mengganti Node global, jadi butuh hak tulis ke folder",
                    "pemasangannya. fnm (Fast Node Manager) adalah pengganti nvm yang lebih",
                    "cepat, berlisensi GPL-3.0, dan membaca .nvmrc yang sama.",
                    "",
                    "mise mengurus versi banyak bahasa sekaligus (Node, Python, Go, Ruby)",
                    "dari satu berkas mise.toml. Nomor versinya memakai tanggal, misalnya",
                    "2026.10.14. Volta dulu populer karena mengunci versi Node per proyek,",
                    "tapi pengelolanya mengumumkan akhir perawatan pada November 2025 dan",
                    "menyarankan mise. Volta masih berfungsi, tapi bug karena sistem operasi",
                    "baru nggak akan diperbaiki.",
                ],
            },
            {
                "heading": "Contoh dengan nvm dan mise",
                "bahasa": "terminal",
                "code": """# nvm: pasang dan pakai LTS terbaru
nvm install --lts
nvm use --lts

# kunci versi proyek, lalu orang lain cukup menjalankan 'nvm use'
echo "24" > .nvmrc
nvm use

# mise: tulis versi ke mise.toml di folder proyek
mise use node@24
node --version""",
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Banyak proyek open source besar memakai pnpm dan menulis versi Node di",
                    ".nvmrc. Berkas CI mereka (misalnya GitHub Actions) membaca .nvmrc yang",
                    "sama, jadi laptop pengembang dan server CI memakai Node yang identik.",
                    "",
                    "Kasus kecil: kamu bergabung ke proyek yang punya pnpm-lock.yaml dan",
                    ".nvmrc berisi 22. Di laptopmu terpasang Node 24 dan kamu biasa memakai",
                    "npm.",
                    "",
                    "Cara memecahkannya:",
                    "1. Pasang manajer versi (nvm atau mise), lalu jalankan nvm use di folder",
                    "   proyek supaya Node 22 dipakai.",
                    "2. Pasang pnpm dengan npm install -g pnpm. Cek field packageManager di",
                    "   package.json; kalau menyebut versi tertentu, pasang versi itu.",
                    "3. Jalankan pnpm install, bukan npm install, supaya lockfile yang dipakai",
                    "   tetap pnpm-lock.yaml.",
                    "4. Kalau ternyata sudah muncul package-lock.json karena salah perintah,",
                    "   hapus berkas itu sebelum commit.",
                ],
            },
        ],
    },
    {
        "title": "4. WCAG 2.2 dan Kontras Warna",
        "sections": [
            {
                "body": [
                    "Aksesibilitas artinya situsmu bisa dipakai semua orang, termasuk orang",
                    "dengan disabilitas. Programmer sering menyingkatnya jadi a11y: huruf a,",
                    "sebelas huruf di tengah, lalu y.",
                    "",
                    "Siapa saja yang dimaksud? Orang tunanetra yang memakai pembaca layar,",
                    "yaitu program yang membacakan isi layar. Orang dengan penglihatan lemah",
                    "yang memperbesar halaman sampai 200% atau lebih. Orang buta warna, yang",
                    "jumlahnya kira-kira 1 dari 12 laki-laki. Orang yang tangannya nggak bisa",
                    "memakai mouse dan cuma memakai papan ketik. Orang tuli yang butuh teks",
                    "untuk video. Ditambah keadaan sementara yang bisa menimpa siapa saja:",
                    "layar ponsel di bawah terik matahari, atau tangan kanan yang sedang",
                    "digips.",
                    "",
                    "Bab ini sengaja ditaruh sebelum framework. Memperbaiki aksesibilitas di",
                    "akhir proyek berarti membongkar komponen yang sudah jadi; memikirkannya",
                    "dari awal hampir nggak menambah kerja. Aturannya juga makin sering jadi",
                    "kewajiban hukum. European Accessibility Act berlaku sejak 28 Juni 2025",
                    "untuk banyak layanan digital di Uni Eropa, dan di Indonesia hak",
                    "penyandang disabilitas atas aksesibilitas diatur UU Nomor 8 Tahun 2016.",
                ],
            },
            {
                "heading": "Apa itu WCAG",
                "body": [
                    "WCAG (Web Content Accessibility Guidelines) adalah pedoman aksesibilitas",
                    "dari W3C, lembaga yang juga menyusun standar HTML dan CSS. Versi",
                    "terbarunya WCAG 2.2, yang jadi Rekomendasi W3C pada Oktober 2023 dan",
                    "diperbarui Desember 2024. WCAG 3 sedang disusun, tapi masih berupa draf",
                    "dan diperkirakan butuh bertahun-tahun. Jadi acuan yang dipakai sekarang",
                    "adalah 2.2.",
                    "",
                    "Halaman yang memenuhi WCAG 2.2 otomatis memenuhi 2.1 dan 2.0, jadi kamu",
                    "nggak perlu mempelajari versi lama secara terpisah.",
                    "",
                    "Isi WCAG dikelompokkan dalam empat prinsip, sering disingkat POUR dari",
                    "huruf depan nama Inggrisnya:",
                    "",
                    "- Perceivable, bisa ditangkap indra. Gambar punya teks alternatif, video",
                    "  punya teks, warna teks cukup kontras.",
                    "- Operable, bisa dioperasikan. Semua fungsi bisa dipakai dengan papan",
                    "  ketik, ada cukup waktu untuk membaca, nggak ada kedipan yang bisa memicu",
                    "  kejang.",
                    "- Understandable, bisa dipahami. Bahasa halaman ditandai, form memberi",
                    "  tahu apa yang salah dan cara memperbaikinya.",
                    "- Robust, kokoh. Markup-nya bisa dibaca dengan benar oleh browser dan",
                    "  teknologi bantu, termasuk yang belum ada sekarang.",
                ],
            },
            {
                "heading": "Tingkat A, AA, dan AAA",
                "body": [
                    "Setiap aturan di WCAG disebut kriteria keberhasilan (success criterion),",
                    "diberi nomor, dan punya tingkat. A adalah syarat paling dasar. AA adalah",
                    "target yang dipakai hampir semua aturan hukum dan kebijakan perusahaan.",
                    "AAA adalah tingkat tertinggi, yang nggak selalu mungkin dicapai untuk",
                    "seluruh isi situs. Kalau ada yang bilang \"situs ini harus memenuhi",
                    "WCAG\", biasanya yang dimaksud WCAG 2.2 tingkat AA.",
                    "",
                    "Beberapa kriteria yang paling sering kamu temui:",
                    "",
                    "  Nomor   Nama singkat                Tingkat",
                    "  1.1.1   Teks alternatif gambar      A",
                    "  1.4.1   Jangan cuma pakai warna     A",
                    "  1.4.3   Kontras teks minimum        AA",
                    "  1.4.11  Kontras non-teks            AA",
                    "  2.1.1   Bisa dipakai papan ketik    A",
                    "  2.4.7   Fokus terlihat              AA",
                    "  2.5.8   Ukuran target minimum       AA",
                    "  3.3.8   Login tanpa tes ingatan     AA",
                ],
            },
            {
                "heading": "Yang baru di WCAG 2.2",
                "body": [
                    "WCAG 2.2 menambah sembilan kriteria dibanding 2.1, kebanyakan untuk",
                    "orang dengan gangguan motorik dan kognitif. Yang paling terasa di",
                    "pekerjaan frontend sehari-hari:",
                    "",
                    "- 2.4.11 Fokus tidak tertutup (AA). Elemen yang sedang difokus nggak boleh",
                    "  tertutup penuh oleh header lengket atau banner cookie.",
                    "- 2.5.7 Gerakan menyeret (AA). Fitur yang dipakai dengan menyeret,",
                    "  misalnya mengurutkan kartu, harus punya cara lain yang cukup dengan",
                    "  klik.",
                    "- 2.5.8 Ukuran target minimum (AA). Target klik paling kecil 24 x 24",
                    "  piksel CSS, atau diberi jarak yang cukup dari target lain.",
                    "- 3.3.7 Isian berulang (A). Data yang sudah diisi di langkah sebelumnya",
                    "  nggak boleh diminta diketik ulang.",
                    "- 3.3.8 Autentikasi yang aksesibel (AA). Login nggak boleh memaksa orang",
                    "  mengingat atau menyalin sesuatu, misalnya melarang tempel (paste) di",
                    "  kolom kata sandi.",
                    "",
                    "Satu kriteria lama dihapus: 4.1.1 Parsing, karena browser modern sudah",
                    "menangani HTML yang kurang rapi dengan cara yang seragam.",
                ],
            },
            {
                "heading": "Menghitung kontras sendiri",
                "body": [
                    "Kontras teks adalah kriteria yang paling sering gagal, dan untung bisa",
                    "dihitung pasti. Langkahnya dua. Pertama, hitung luminans relatif tiap",
                    "warna, yaitu seberapa terang warna itu menurut mata manusia, dari 0",
                    "(hitam) sampai 1 (putih). Hijau dapat bobot paling besar karena mata",
                    "paling peka pada hijau. Kedua, bagi luminans yang lebih terang dengan",
                    "yang lebih gelap, masing-masing ditambah 0,05. Hasilnya dari 1:1 (warna",
                    "sama) sampai 21:1 (hitam di atas putih).",
                ],
                "code": """// Rasio kontras WCAG antara dua warna hex.
function luminans(hex) {
  const angka = [1, 3, 5].map((i) => parseInt(hex.slice(i, i + 2), 16) / 255);
  const [r, g, b] = angka.map((c) =>
    c <= 0.04045 ? c / 12.92 : ((c + 0.055) / 1.055) ** 2.4);
  return 0.2126 * r + 0.7152 * g + 0.0722 * b;
}

function rasio(warna1, warna2) {
  const a = luminans(warna1);
  const b = luminans(warna2);
  return (Math.max(a, b) + 0.05) / (Math.min(a, b) + 0.05);
}

const pasangan = [
  ['#000000', '#ffffff'],
  ['#767676', '#ffffff'],
  ['#777777', '#ffffff'],
  ['#ffcc00', '#ffffff'],
];
for (const [teks, latar] of pasangan) {
  const r = rasio(teks, latar);
  const aa = r >= 4.5 ? 'lulus AA' : 'gagal AA';
  console.log(`${teks} di atas ${latar}: ${r.toFixed(2)}:1 (${aa})`);
}""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  #000000 di atas #ffffff: 21.00:1 (lulus AA)",
                    "  #767676 di atas #ffffff: 4.54:1 (lulus AA)",
                    "  #777777 di atas #ffffff: 4.48:1 (gagal AA)",
                    "  #ffcc00 di atas #ffffff: 1.51:1 (gagal AA)",
                    "",
                    "Abu-abu #767676 adalah abu-abu paling terang yang masih lulus di atas",
                    "putih. Geser satu tingkat ke #777777 dan hasilnya gagal. Kuning #ffcc00",
                    "kelihatan mencolok, tapi sebagai warna teks di atas putih rasionya cuma",
                    "1,51:1.",
                    "",
                    "Ambang yang dipakai WCAG:",
                    "",
                    "  Jenis isi                     AA      AAA",
                    "  Teks normal                   4,5:1   7:1",
                    "  Teks besar                    3:1     4,5:1",
                    "  Ikon, garis input, cincin     3:1     (tidak diatur)",
                    "  fokus (non-teks)",
                    "",
                    "Teks besar artinya minimal 24 piksel, atau minimal 18,66 piksel kalau",
                    "tebal (di dokumen WCAG ditulis 18pt dan 14pt). Logo dan tombol yang",
                    "sedang nonaktif dikecualikan.",
                    "",
                    "Ingat: rasio nggak boleh dibulatkan dulu sebelum dibandingkan. 4,48:1",
                    "tetap gagal walaupun kalau ditulis satu angka di belakang koma kelihatan",
                    "seperti 4,5.",
                ],
            },
            {
                "heading": "Jebakan pemula",
                "body": [
                    "- Placeholder abu-abu muda. Warna bawaan banyak template, seperti #9ca3af",
                    "  di atas putih, rasionya cuma 2,54:1. Lagi pula placeholder hilang begitu",
                    "  orang mulai mengetik, jadi tetap butuh label.",
                    "- Teks di atas foto. Rasionya berubah di tiap bagian foto. Beri lapisan",
                    "  gelap semi transparan di belakang teks.",
                    "- Warna sebagai satu-satunya penanda. Kolom yang salah cuma diberi garis",
                    "  merah nggak terbaca oleh orang buta warna merah hijau. Tambahkan ikon",
                    "  atau pesan teks.",
                    "- outline: none tanpa pengganti. Garis fokus itu satu-satunya cara",
                    "  pengguna papan ketik tahu posisinya. Kalau mau mengubahnya, pakai",
                    "  :focus-visible dengan gaya sendiri yang kontrasnya minimal 3:1.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Laporan tahunan WebAIM Million, yang memindai beranda satu juta situs",
                    "populer, pada 2025 menemukan lebih dari 94% beranda punya kegagalan WCAG",
                    "yang bisa dideteksi otomatis. Kontras teks yang terlalu rendah selalu",
                    "ada di urutan teratas daftar masalahnya.",
                    "",
                    "Kasus kecil: tim desain memberimu warna merek oranye #ff7a00 dan meminta",
                    "tombol berteks putih. Kamu hitung rasionya cuma 2,61:1.",
                    "",
                    "Cara memecahkannya:",
                    "1. Tunjukkan angkanya ke desainer: teks normal butuh 4,5:1, teks besar dan",
                    "   tebal butuh 3:1. Dua-duanya belum tercapai.",
                    "2. Tawarkan pilihan pertama: teks gelap di atas oranye. #1a1a1a di atas",
                    "   #ff7a00 menghasilkan 6,66:1, lulus AA.",
                    "3. Atau gelapkan oranyenya untuk latar tombol. #b35600 dengan teks putih",
                    "   menghasilkan 4,94:1, sedangkan #c25e00 baru 4,29:1 dan masih gagal.",
                    "4. Simpan oranye asli untuk hiasan yang bukan teks dan bukan satu-satunya",
                    "   penanda, misalnya garis aksen.",
                ],
            },
        ],
    },
    {
        "title": "5. WAI-ARIA dan Nama yang Dibacakan",
        "sections": [
            {
                "body": [
                    "Pembaca layar nggak melihat tampilan halamanmu. Yang ia baca adalah",
                    "pohon aksesibilitas, yaitu versi ringkas DOM yang dibuat browser khusus",
                    "untuk teknologi bantu. Setiap simpul di pohon itu punya beberapa sifat:",
                    "",
                    "- role, yaitu peran elemen: button, link, heading, textbox, checkbox.",
                    "- name, yaitu nama yang dibacakan: \"Kirim\", \"Keranjang\".",
                    "- state, yaitu keadaannya: tercentang, terbuka, nonaktif.",
                    "- value untuk elemen yang punya nilai, seperti slider.",
                    "",
                    "Waktu pengguna menekan Tab ke sebuah tombol, pembaca layar mengucapkan",
                    "kira-kira \"Kirim, tombol\". Nama dulu, lalu peran. Kalau namanya kosong,",
                    "yang terdengar cuma \"tombol\", dan orang itu harus menebak tombol apa.",
                    "",
                    "WAI-ARIA (Accessible Rich Internet Applications) adalah spesifikasi W3C",
                    "berisi atribut role dan aria-* untuk mengatur sifat-sifat itu langsung.",
                    "Versi resminya 1.2 (Juni 2023), dan versi 1.3 sedang disusun.",
                ],
            },
            {
                "heading": "Aturan pertama ARIA: pakai elemen HTML dulu",
                "bahasa": "html",
                "code": """<!-- Kelihatan seperti tombol, tapi bukan tombol -->
<div class="tombol" onclick="simpan()">Simpan</div>

<!-- Kalau dipaksa pakai div, ini yang harus ditambahkan -->
<div class="tombol" role="button" tabindex="0"
     onclick="simpan()" onkeydown="tekanTombol(event)">Simpan</div>

<!-- Yang benar: semua sudah termasuk -->
<button type="button" onclick="simpan()">Simpan</button>""",
            },
            {
                "body": [
                    "Dokumen ARIA sendiri menulis aturan pertamanya: kalau ada elemen HTML",
                    "bawaan yang sudah punya arti dan perilaku yang kamu butuhkan, pakai",
                    "elemen itu, jangan elemen lain yang diberi ARIA.",
                    "",
                    "Elemen button memberi semuanya gratis. Ia bisa dicapai dengan Tab, bisa",
                    "ditekan dengan Enter dan Spasi, perannya button, dan namanya diambil",
                    "dari teks di dalamnya. Div yang diberi role=\"button\" cuma mengubah apa",
                    "yang dibacakan. Ia tetap nggak bisa difokus tanpa tabindex, dan tetap",
                    "nggak bereaksi pada Enter atau Spasi sebelum kamu menulis kode sendiri",
                    "untuk itu.",
                    "",
                    "Itulah inti ARIA: ia mengubah apa yang diumumkan, bukan apa yang bisa",
                    "dilakukan. ARIA yang salah lebih buruk daripada tanpa ARIA, karena ia",
                    "menjanjikan sesuatu yang nggak ada. Laporan WebAIM Million tiap tahun",
                    "menemukan halaman yang memakai ARIA rata-rata punya lebih banyak",
                    "kesalahan terdeteksi daripada halaman tanpa ARIA. Ini pelajaran yang",
                    "sama dengan materi HTML bab 5.",
                ],
            },
            {
                "heading": "Kapan ARIA memang dibutuhkan",
                "body": [
                    "ARIA dipakai untuk hal yang belum bisa dijelaskan HTML biasa:",
                    "",
                    "- Keadaan yang berubah. Tombol yang membuka dan menutup menu diberi",
                    "  aria-expanded=\"true\" atau \"false\".",
                    "- Widget yang nggak ada di HTML, seperti tab (role=\"tablist\", \"tab\",",
                    "  \"tabpanel\") atau kotak isian dengan saran otomatis (role=\"combobox\").",
                    "- Pengumuman tanpa memindah fokus. Notifikasi \"Tersimpan\" ditaruh di",
                    "  elemen role=\"status\" atau aria-live=\"polite\" supaya dibacakan begitu",
                    "  muncul.",
                    "- Menyembunyikan hiasan. Ikon dekoratif di samping teks diberi",
                    "  aria-hidden=\"true\" supaya nggak dibacakan dua kali.",
                    "- Memberi nama pada elemen yang nggak punya teks, lewat aria-label atau",
                    "  aria-labelledby.",
                ],
            },
            {
                "heading": "Contoh: tombol menu buka tutup",
                "bahasa": "html",
                "code": """<button type="button" id="tombol-menu"
        aria-expanded="false" aria-controls="menu">
  <svg aria-hidden="true" width="16" height="16"><!-- ikon --></svg>
  Menu
</button>
<ul id="menu" hidden>
  <li><a href="/promo">Promo</a></li>
  <li><a href="/akun">Akun</a></li>
</ul>""",
            },
            {
                "bahasa": "browser",
                "code": """const tombol = document.querySelector('#tombol-menu');
const menu = document.querySelector('#menu');

tombol.addEventListener('click', () => {
  const terbuka = tombol.getAttribute('aria-expanded') === 'true';
  tombol.setAttribute('aria-expanded', String(!terbuka));
  menu.hidden = terbuka; // tampilan dan keadaan diubah bersamaan
});""",
            },
            {
                "heading": "Dari mana nama aksesibel diambil",
                "body": [
                    "Browser menghitung nama sebuah elemen dengan urutan tetap. Sumber",
                    "pertama yang ada isinya dipakai, sisanya diabaikan. Versi ringkasnya:",
                    "",
                    "1. aria-labelledby: teks dari elemen lain yang id-nya disebut.",
                    "2. aria-label: teks yang ditulis langsung di atribut.",
                    "3. Sumber bawaan HTML: label for untuk input, alt untuk img, caption untuk",
                    "   tabel, legend untuk fieldset.",
                    "4. Isi teks elemen, untuk peran yang namanya boleh diambil dari isi,",
                    "   seperti button, link, dan heading. Alt gambar di dalam tombol ikut",
                    "   terhitung.",
                    "5. Cadangan terakhir: atribut title, atau placeholder untuk input.",
                    "",
                    "  <label for=\"kota\">Kota pengiriman</label>",
                    "  <input id=\"kota\">                   -> \"Kota pengiriman\"",
                    "",
                    "  <button aria-label=\"Tutup\">X</button>  -> \"Tutup\"",
                    "",
                    "  <a href=\"/keranjang\">",
                    "    <img src=\"troli.svg\" alt=\"Keranjang\"> (3)",
                    "  </a>                                -> \"Keranjang (3)\"",
                    "",
                    "Jebakan: aria-label yang nggak memuat teks yang terlihat. Tombol",
                    "bertuliskan \"Kirim\" yang diberi aria-label=\"Proses formulir\"",
                    "membingungkan pengguna kontrol suara, yang akan berkata \"klik Kirim\" dan",
                    "nggak mendapat apa-apa. WCAG mengaturnya di kriteria 2.5.3 (Label in",
                    "Name): nama aksesibel harus memuat teks yang terlihat.",
                ],
            },
            {
                "heading": "Melihat pohonnya sendiri",
                "body": [
                    "Kamu nggak perlu menebak hasil hitungan browser. Di Chrome, buka",
                    "DevTools, pilih elemen di panel Elements, lalu buka tab Accessibility.",
                    "Di sana tertulis role dan name elemen itu, plus dari mana namanya",
                    "diambil. Firefox punya panel Accessibility tersendiri. Keduanya dibahas",
                    "lengkap di materi berikutnya.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aplikasi belanja dan ojek online penuh tombol ikon tanpa teks:",
                    "keranjang, kembali, tutup, bagikan, favorit. Di versi web, tombol-tombol",
                    "seperti itu adalah sumber masalah aksesibilitas yang paling umum, karena",
                    "kelihatan jelas di layar tapi namanya kosong di pohon aksesibilitas.",
                    "",
                    "Kasus kecil: halaman produk punya tombol hati untuk menyimpan ke",
                    "favorit, ditulis sebagai div berisi ikon SVG. Pembaca layar nggak",
                    "menyebut apa-apa waktu tombol itu dicapai, dan papan ketik bahkan nggak",
                    "bisa mencapainya.",
                    "",
                    "Cara memecahkannya:",
                    "1. Ganti div dengan button type=\"button\", supaya fokus, Enter, dan Spasi",
                    "   langsung bekerja.",
                    "2. Beri nama lewat aria-label=\"Simpan ke favorit\", dan beri",
                    "   aria-hidden=\"true\" pada SVG-nya.",
                    "3. Karena tombol ini bisa nyala dan mati, tambahkan aria-pressed=\"false\"",
                    "   lalu ubah jadi \"true\" saat produk disimpan.",
                    "4. Periksa di tab Accessibility DevTools bahwa role-nya button, name-nya",
                    "   \"Simpan ke favorit\", dan keadaannya berubah saat diklik.",
                ],
            },
        ],
    },
    {
        "title": "6. DevTools dan Alat Uji Aksesibilitas",
        "sections": [
            {
                "body": [
                    "Sebagian masalah aksesibilitas bisa diperiksa mesin: gambar tanpa alt,",
                    "kontras yang terlalu rendah, input tanpa label, id kembar. Alat uji",
                    "otomatis menangkap masalah semacam itu dalam hitungan detik, jadi sayang",
                    "kalau nggak dipakai.",
                    "",
                    "Sebagian lain cuma bisa dinilai manusia. Mesin bisa tahu sebuah gambar",
                    "punya alt, tapi nggak bisa tahu apakah alt=\"gambar\" itu berguna. Mesin",
                    "juga nggak bisa merasakan bahwa urutan Tab di halamanmu melompat-lompat.",
                    "Jadi alat otomatis adalah langkah pertama, bukan langkah satu-satunya.",
                ],
            },
            {
                "heading": "Peta alat",
                "bahasa": "teks",
                "code": """Alat                     Bentuk                Lisensi             Kapan dipakai
Chrome/Firefox DevTools  bawaan browser        open source         setiap hari, saat menulis
Lighthouse               tab di Chrome, CLI    Apache-2.0          audit cepat satu halaman
axe-core                 pustaka JS            MPL-2.0             di dalam tes dan CI
WAVE                     situs dan ekstensi    gratis, tertutup    menandai masalah di halaman
Accessibility Insights   ekstensi Microsoft    MIT                 cek cepat + panduan manual
ARC Toolkit              ekstensi Chrome       gratis, tertutup    pemeriksaan di DevTools
Pa11y                    baris perintah        LGPL-3.0            cek banyak URL sekaligus
eslint-plugin-jsx-a11y   aturan ESLint         MIT                 saat mengetik kode JSX""",
            },
            {
                "heading": "DevTools browser",
                "body": [
                    "Di State of HTML 2025, DevTools browser menyalip Lighthouse dan jadi",
                    "alat uji aksesibilitas yang paling banyak dipakai responden (2.259",
                    "orang, Lighthouse 1.983). Wajar, karena DevTools sudah ada di depan",
                    "matamu tanpa memasang apa pun.",
                    "",
                    "Di Chrome DevTools, yang paling berguna:",
                    "",
                    "- Panel Elements, tab Accessibility: role, name, dan state elemen yang",
                    "  dipilih, plus dari mana namanya diambil. Ada pilihan untuk menampilkan",
                    "  pohon aksesibilitas seluruh halaman.",
                    "- Pemilih warna di panel Styles: menampilkan rasio kontras teks dengan",
                    "  latarnya, lengkap dengan tanda lulus AA dan AAA.",
                    "- Panel Rendering: meniru buta warna dan penglihatan kabur, supaya kamu",
                    "  bisa melihat halamanmu dari mata orang lain.",
                    "",
                    "Firefox punya Accessibility Inspector (dipakai 1.033 responden State of",
                    "HTML 2025). Tombol Check for issues di sana menandai masalah kontras,",
                    "papan ketik, dan label teks, dan ada simulasi buta warna juga.",
                ],
            },
            {
                "heading": "Lighthouse dan axe-core",
                "body": [
                    "Lighthouse adalah alat audit dari Google yang ada di tab Lighthouse di",
                    "Chrome DevTools. Ia memberi skor untuk performa, aksesibilitas, praktik",
                    "terbaik, dan SEO. Versi terbarunya saat materi ini ditulis adalah",
                    "13.5.0. Bagian aksesibilitasnya memakai aturan dari axe-core.",
                    "",
                    "Jebakan: skor aksesibilitas 100 bukan berarti situsmu aksesibel. Artinya",
                    "cuma \"nggak ada pelanggaran yang bisa dideteksi aturan otomatis",
                    "Lighthouse\".",
                    "",
                    "axe-core buatan Deque adalah mesin pemeriksa yang dipakai di banyak",
                    "tempat: ekstensi axe DevTools, Lighthouse, pengujian Playwright, add-on",
                    "Storybook, dan jest-axe. Versinya 4.14.0, dan di State of HTML 2025 ia",
                    "ada di urutan ketiga. Karena berupa pustaka JavaScript, axe bisa",
                    "dijalankan di dalam tes otomatis, jadi setiap perubahan kode langsung",
                    "diperiksa.",
                ],
            },
            {
                "heading": "Menjalankan axe dari konsol",
                "bahasa": "browser",
                "code": """// Di konsol DevTools, sesudah berkas axe.min.js dimuat ke halaman.
const hasil = await axe.run(document);
for (const v of hasil.violations) {
  console.log(v.id, v.impact, v.nodes.length + ' elemen');
}
// contoh baris: color-contrast serious 4 elemen""",
            },
            {
                "heading": "WAVE, Accessibility Insights, ARC Toolkit, dan Pa11y",
                "body": [
                    "WAVE dari WebAIM tersedia sebagai situs dan ekstensi browser. Ia menaruh",
                    "ikon kecil langsung di atas elemen yang bermasalah, jadi cocok untuk",
                    "menunjukkan masalah ke teman setim yang bukan programmer. Gratis",
                    "dipakai, kodenya tertutup, dan API-nya berbayar.",
                    "",
                    "Accessibility Insights adalah alat open source dari Microsoft (lisensi",
                    "MIT) untuk browser, Windows, dan Android. FastPass-nya memeriksa",
                    "otomatis dalam beberapa detik, dan mode Assessment memandu uji manual",
                    "langkah demi langkah.",
                    "",
                    "ARC Toolkit adalah ekstensi Chrome gratis dari TPGi yang menambah panel",
                    "pemeriksaan aksesibilitas di DevTools. Survei State of HTML 2025 cuma",
                    "menulis \"Arc\", yang paling mungkin maksudnya alat ini.",
                    "",
                    "Pa11y adalah alat baris perintah (versi 10.0.0, LGPL-3.0) yang memeriksa",
                    "halaman memakai axe atau HTML_CodeSniffer. Ia cocok untuk memeriksa",
                    "banyak URL sekaligus di CI, misalnya lewat pa11y-ci.",
                ],
            },
            {
                "heading": "Menangkap masalah saat mengetik",
                "body": [
                    "eslint-plugin-jsx-a11y adalah kumpulan aturan ESLint untuk kode JSX",
                    "(React). Ia menandai img tanpa alt, onClick di div tanpa penanganan",
                    "papan ketik, dan atribut aria yang salah ketik, langsung di editor",
                    "sebelum kodenya dijalankan. Rilis terakhirnya 6.10.2 pada Oktober 2024,",
                    "jadi periksa dulu dukungannya untuk versi ESLint yang kamu pakai.",
                    "Padanannya untuk Vue adalah eslint-plugin-vuejs-accessibility. ESLint",
                    "sendiri dibahas di bab 5.",
                ],
            },
            {
                "heading": "Apa yang bisa dan nggak bisa dilihat mesin",
                "body": [
                    "Program di bawah adalah pemeriksa mini dengan dua aturan. Lihat apa yang",
                    "ia tangkap dan apa yang lolos.",
                ],
                "code": "// Pemeriksa otomatis mini: cuma bisa melihat yang bisa dihitung.\nconst halaman = `\n<img src=\"logo.png\">\n<img src=\"garis.svg\" alt=\"\">\n<img src=\"foto1.jpg\" alt=\"gambar\">\n<button></button>\n<button>Kirim</button>\n<a href=\"/promo\">klik di sini</a>\n`;\n\nconst temuan = [];\nfor (const m of halaman.matchAll(/<img([^>]*)>/g)) {\n  if (!/\\balt=/.test(m[1])) temuan.push(`img tanpa alt: ${m[0]}`);\n}\nfor (const m of halaman.matchAll(/<button[^>]*>(.*?)<\\/button>/g)) {\n  if (m[1].trim() === '') temuan.push(`button tanpa teks: ${m[0]}`);\n}\n\nfor (const t of temuan) console.log(t);\nconsole.log(`${temuan.length} temuan otomatis`);",
            },
            {
                "body": [
                    "Keluaran:",
                    "  img tanpa alt: <img src=\"logo.png\">",
                    "  button tanpa teks: <button></button>",
                    "  2 temuan otomatis",
                    "",
                    "Gambar garis dengan alt=\"\" lolos, dan itu benar: alt kosong artinya",
                    "hiasan, dan pembaca layar melewatinya. Tapi alt=\"gambar\" juga lolos,",
                    "padahal nggak menjelaskan apa pun. Tautan \"klik di sini\" juga lolos,",
                    "padahal pengguna pembaca layar yang membuka daftar tautan cuma mendengar",
                    "\"klik di sini\" berulang kali.",
                    "",
                    "Alat sungguhan punya ratusan aturan, tapi batasnya sama. Pada 2017,",
                    "Government Digital Service Inggris menanam 142 masalah aksesibilitas di",
                    "satu halaman uji, lalu memeriksanya dengan belasan alat otomatis. Nggak",
                    "ada satu alat pun yang menemukan lebih dari separuhnya. Sisanya harus",
                    "ditemukan dengan papan ketik dan pembaca layar, yang jadi bahan materi",
                    "berikutnya.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Tim yang serius soal aksesibilitas biasanya memasang axe-core di",
                    "pengujian end-to-end (Playwright atau Cypress), sehingga pull request",
                    "yang menambah tombol tanpa nama langsung gagal di CI. Pengujian manual",
                    "dengan papan ketik tetap dijadwalkan sebelum rilis besar.",
                    "",
                    "Kasus kecil: halaman pendaftaran kursus mendapat skor aksesibilitas",
                    "Lighthouse 100, tapi ada laporan dari pengguna bahwa menu pilihan kelas",
                    "nggak bisa dibuka tanpa mouse.",
                    "",
                    "Cara memecahkannya:",
                    "1. Coba sendiri: cabut mouse, lalu pakai Tab, Shift+Tab, Enter, Spasi, dan",
                    "   panah untuk mendaftar dari awal sampai selesai.",
                    "2. Catat elemen yang nggak bisa dicapai atau dibuka. Biasanya itu div atau",
                    "   span yang diberi onclick.",
                    "3. Periksa elemen itu di tab Accessibility DevTools: kalau role-nya",
                    "   generic dan nggak bisa difokus, ganti dengan button atau select bawaan.",
                    "4. Jalankan ulang Lighthouse dan axe, lalu ulangi uji papan ketik. Skor",
                    "   yang sama-sama 100 sebelum dan sesudah perbaikan menunjukkan batas uji",
                    "   otomatis.",
                ],
            },
        ],
    },
    {
        "title": "7. Pembaca Layar: Mencoba Orca di Fedora",
        "sections": [
            {
                "body": [
                    "Membaca soal pembaca layar nggak sama dengan mendengarnya sendiri. Lima",
                    "menit memakai pembaca layar di halaman buatanmu biasanya mengajarkan",
                    "lebih banyak daripada satu artikel panjang. Kabar baiknya, kamu memakai",
                    "Fedora Workstation, dan pembaca layar Orca sudah terpasang bawaan.",
                    "",
                    "Orca adalah pembaca layar open source untuk desktop Linux GNOME,",
                    "berlisensi LGPL. Versinya ikut siklus GNOME: Fedora 44 membawa Orca",
                    "50.3, dan rilis terbarunya saat materi ini ditulis adalah 51.1. Suaranya",
                    "dihasilkan lewat speech-dispatcher, biasanya dengan eSpeak NG, yang",
                    "punya suara berbahasa Indonesia walau terdengar seperti robot.",
                ],
            },
            {
                "heading": "Menyalakan dan mematikan",
                "body": [
                    "Tekan Super+Alt+S. Orca langsung bicara. Tekan kombinasi yang sama untuk",
                    "mematikannya. Cara lain lewat Pengaturan, bagian Aksesibilitas, lalu",
                    "nyalakan Pembaca Layar.",
                    "",
                    "Beberapa tombol yang perlu kamu tahu sebelum mulai:",
                    "",
                    "- Ctrl menghentikan suara yang sedang berjalan.",
                    "- Tombol Orca adalah tombol pengubah khusus Orca. Pada tata letak desktop",
                    "  ia adalah Insert, pada tata letak laptop Caps Lock. Di daftar perintah",
                    "  ditulis \"Orca+...\".",
                    "- Orca+Spasi membuka preferensi, tempat mengatur kecepatan bicara dan",
                    "  memilih tata letak papan ketik.",
                    "- Orca+H menyalakan mode belajar: setiap tombol yang kamu tekan dijelaskan",
                    "  fungsinya tanpa dijalankan. Escape untuk keluar.",
                    "",
                    "Pakai headphone kalau belajar di tempat ramai, dan turunkan kecepatan",
                    "bicara dulu supaya bisa mengikuti.",
                ],
            },
            {
                "heading": "Kalau Orca belum ada",
                "bahasa": "terminal",
                "code": """orca --version
# kalau perintahnya nggak ditemukan:
sudo dnf install orca""",
            },
            {
                "heading": "Menjelajah halaman web",
                "body": [
                    "Orca bekerja paling baik dengan Firefox, dan juga mendukung browser",
                    "berbasis Chromium. Di halaman web, Orca memakai navigasi struktural:",
                    "satu huruf melompat ke jenis elemen berikutnya, dan huruf yang sama",
                    "ditambah Shift melompat mundur.",
                    "",
                    "  Tombol   Melompat ke              Tombol   Melompat ke",
                    "  H        judul (heading)          K        tautan",
                    "  1 - 6    judul tingkat 1 - 6      B        tombol",
                    "  M        landmark (nav, main)     F        kolom form",
                    "  G        gambar                   E        kolom isian teks",
                    "  L        daftar                   T        tabel",
                    "  Tab      elemen berikutnya yang bisa difokus",
                    "",
                    "Alt+Shift ditambah huruf yang sama menampilkan daftar semua elemen jenis",
                    "itu, misalnya semua judul di halaman. Begitu kamu masuk ke kolom isian,",
                    "Orca berpindah ke mode fokus supaya huruf yang kamu ketik masuk ke",
                    "kolom, bukan dipakai melompat.",
                ],
            },
            {
                "heading": "Latihan sepuluh menit",
                "body": [
                    "Buka salah satu halaman HTML buatanmu di Firefox, nyalakan Orca, lalu",
                    "tutup mata atau matikan layar:",
                    "",
                    "1. Tekan H berulang kali. Apakah judul-judulnya menggambarkan isi halaman,",
                    "   dan tingkatnya urut dari 1?",
                    "2. Tekan M. Apakah ada landmark navigation dan main, atau halamannya cuma",
                    "   tumpukan div?",
                    "3. Tekan K. Apakah setiap tautan bisa dipahami tanpa kalimat di",
                    "   sekitarnya? \"Klik di sini\" gagal di tes ini.",
                    "4. Tekan Tab dari atas sampai bawah. Setiap tombol dan kolom harus",
                    "   terdengar dengan nama dan perannya, dan urutannya masuk akal.",
                    "5. Tekan G. Alt setiap gambar terdengar, dan gambar hiasan dilewati.",
                    "",
                    "Catat apa pun yang membuatmu bingung. Orang yang memakai pembaca layar",
                    "setiap hari akan bingung di tempat yang sama.",
                ],
            },
            {
                "heading": "Pembaca layar di sistem lain",
                "bahasa": "teks",
                "code": """Nama        Sistem                 Lisensi                 Menyalakan
Orca        Linux GNOME            LGPL, gratis            Super+Alt+S
NVDA        Windows                GPL-2.0, gratis         unduh dari nvaccess.org
JAWS        Windows                berbayar                dipasang terpisah
Narrator    Windows                bawaan Windows          Ctrl+Win+Enter
VoiceOver   macOS, iOS, iPadOS     bawaan Apple            Cmd+F5 di Mac
TalkBack    Android                bawaan Android          Pengaturan > Aksesibilitas
ChromeVox   ChromeOS (Chromebook)  bawaan ChromeOS         Ctrl+Alt+Z""",
            },
            {
                "body": [
                    "NVDA dari NV Access gratis dan open source, sebagian besar ditulis",
                    "dengan Python, dan rilis terbarunya 2026.2. JAWS dari Freedom Scientific",
                    "(Vispero) adalah pembaca layar komersial yang paling lama ada; versinya",
                    "kini dinamai menurut tahun, terbarunya 2026. Di kalangan pengguna",
                    "pembaca layar sungguhan di desktop, dua program Windows ini yang paling",
                    "banyak dipakai.",
                    "",
                    "VoiceOver ada di semua perangkat Apple. Di kalangan developer ia yang",
                    "paling banyak dipakai untuk menguji (1.376 responden State of HTML",
                    "2025), karena banyak developer memakai Mac. Narrator adalah pembaca",
                    "layar bawaan Windows, cukup untuk cek cepat walau fiturnya lebih",
                    "sedikit.",
                    "",
                    "TalkBack penting untuk Indonesia, karena sebagian besar pengguna ponsel",
                    "di sini memakai Android. Kalau situsmu banyak dibuka dari ponsel, coba",
                    "juga dengan TalkBack di Chrome Android. ChromeVox adalah pembaca layar",
                    "bawaan Chromebook.",
                    "",
                    "Setiap pembaca layar punya kebiasaan sendiri, dan pasangan pembaca layar",
                    "dengan browser juga berpengaruh. Halaman yang benar menurut standar",
                    "biasanya terdengar wajar di semuanya. Pasangan yang lazim dipakai untuk",
                    "menguji: pembaca layar gratis dari NV Access dengan Firefox atau Chrome,",
                    "VoiceOver dengan Safari, TalkBack dengan Chrome, dan untukmu sekarang,",
                    "Orca dengan Firefox.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Situs layanan publik dan perbankan di banyak negara diuji dengan pembaca",
                    "layar sebelum rilis, karena tuntutan hukum soal aksesibilitas makin",
                    "sering terjadi. Penguji biasanya menjalankan skenario utama, seperti",
                    "daftar, login, dan bayar, memakai papan ketik dan pembaca layar saja.",
                    "",
                    "Kasus kecil: kamu membuat halaman formulir pendaftaran lomba untuk",
                    "sekolahmu. Secara visual rapi, tapi kamu belum pernah mendengarnya.",
                    "",
                    "Cara memecahkannya:",
                    "1. Buka halaman itu di Firefox dan nyalakan Orca dengan Super+Alt+S.",
                    "2. Tekan F untuk melompat antar kolom form. Kalau Orca cuma bilang \"kolom",
                    "   isian\" tanpa nama, input itu belum punya label.",
                    "3. Tambahkan label for yang id-nya cocok untuk setiap input, lalu ulangi",
                    "   langkah 2 sampai setiap kolom terdengar namanya.",
                    "4. Isi form dengan sengaja salah dan kirim. Pastikan pesan errornya",
                    "   dibacakan; kalau tidak, taruh pesan itu di elemen role=\"alert\" atau",
                    "   hubungkan ke input dengan aria-describedby.",
                ],
            },
        ],
    },
    {
        "title": "8. Komponen dan Virtual DOM dari Nol",
        "sections": [
            {
                "body": [
                    "Di bab 1 kamu melihat ide dasar framework: tampilan dibuat ulang dari",
                    "state setiap kali state berubah. Di browser, membuang lalu membuat ulang",
                    "seluruh DOM itu boros. Elemen input kehilangan fokus dan isi ketikannya,",
                    "posisi gulir melompat, dan animasi terputus.",
                    "",
                    "React, Preact, dan Vue memecahkannya dengan virtual DOM. Idenya: fungsi",
                    "tampilan nggak langsung membuat elemen DOM. Ia membuat gambaran tampilan",
                    "dalam bentuk objek JavaScript biasa, yang murah dibuat dan murah",
                    "dibuang. Gambaran baru lalu dibandingkan dengan gambaran lama, dan cuma",
                    "perbedaannya yang diterapkan ke DOM asli. Proses membandingkan itu",
                    "disebut diff, dan menerapkan hasilnya disebut patch.",
                    "",
                    "Komponen di dunia ini juga sederhana: fungsi yang menerima props (data",
                    "dari luar, seperti argumen) dan mengembalikan gambaran tampilan. Di",
                    "materi ini kamu membangun tiga fungsi yang jadi dasar semua itu: h,",
                    "renderToString, dan diff. Nama-nama ini dipakai lagi sampai proyek akhir",
                    "kurikulum.",
                ],
            },
            {
                "heading": "h(): membuat satu simpul",
                "body": [
                    "Fungsi h(tag, props, ...anak) cuma membungkus argumennya jadi objek.",
                    "Namanya diambil dari hyperscript, pustaka lama yang memopulerkan cara",
                    "ini. Preact dan Vue sampai sekarang mengekspor fungsi bernama h, dan",
                    "React punya padanannya, createElement.",
                    "",
                    "JSX yang akan kamu tulis di React nanti hanyalah cara menulis panggilan",
                    "seperti itu supaya mirip HTML. Compiler mengubahnya jadi panggilan",
                    "fungsi sebelum kode dijalankan:",
                ],
                "bahasa": "jsx",
                "code": """// Yang kamu tulis:
const kartu = <li className="kartu">{nama}</li>;

// Kira-kira yang dihasilkan compiler:
const kartu = jsx('li', { className: 'kartu', children: nama });""",
            },
            {
                "heading": "h dan renderToString dalam tiga puluh baris",
                "code": "// h() membuat simpul virtual DOM: objek biasa, belum menyentuh layar.\nfunction h(tag, props, ...anak) {\n  return { tag, props: props || {}, anak: anak.flat() };\n}\n\nfunction escape(teks) {\n  return String(teks).replace(/&/g, '&amp;').replace(/</g, '&lt;')\n    .replace(/>/g, '&gt;').replace(/\"/g, '&quot;');\n}\n\nfunction renderToString(simpul) {\n  if (typeof simpul !== 'object') return escape(simpul);\n  if (typeof simpul.tag === 'function') {\n    // Komponen: panggil fungsinya, render hasilnya.\n    return renderToString(simpul.tag({ ...simpul.props, anak: simpul.anak }));\n  }\n  const attr = Object.entries(simpul.props)\n    .map(([k, v]) => ` ${k}=\"${escape(v)}\"`).join('');\n  return `<${simpul.tag}${attr}>${simpul.anak.map(renderToString).join('')}</${simpul.tag}>`;\n}\n\n// Dua komponen: fungsi yang menerima props dan mengembalikan pohon.\nfunction Harga({ nilai }) {\n  return h('span', { class: 'harga' }, 'Rp', nilai);\n}\n\nfunction Kartu({ nama, harga }) {\n  return h('li', null, h('b', null, nama), ' ', h(Harga, { nilai: harga }));\n}\n\nconst menu = [\n  { nama: 'Kopi <susu>', harga: 18000 },\n  { nama: 'Teh tarik', harga: 12000 },\n];\nconst pohon = h('ul', { id: 'menu' }, menu.map((m) => h(Kartu, m)));\n\nconsole.log(JSON.stringify(h('b', null, 'Teh tarik')));\nconst html = renderToString(pohon);\n// Dipotong per <li> supaya muat di layar; aslinya satu baris panjang.\nconsole.log(html.replace(/<li>/g, '\\n  <li>').replace('</ul>', '\\n</ul>'));",
            },
            {
                "body": [
                    "Keluaran:",
                    "  {\"tag\":\"b\",\"props\":{},\"anak\":[\"Teh tarik\"]}",
                    "  <ul id=\"menu\">",
                    "    <li><b>Kopi &lt;susu&gt;</b> <span class=\"harga\">Rp18000</span></li>",
                    "    <li><b>Teh tarik</b> <span class=\"harga\">Rp12000</span></li>",
                    "  </ul>",
                    "",
                    "Baris pertama menunjukkan bahwa simpul virtual DOM memang cuma objek:",
                    "tag, props, dan daftar anak. Tag-nya boleh berupa teks ('li') atau",
                    "fungsi (Kartu). Kalau berupa fungsi, renderToString memanggilnya dengan",
                    "props, lalu merender apa pun yang dikembalikan. Begitulah komponen bisa",
                    "disusun di dalam komponen lain sedalam apa pun.",
                    "",
                    "Perhatikan juga nama \"Kopi <susu>\" yang keluar sebagai &lt;susu&gt;.",
                    "Fungsi escape mengubah karakter khusus HTML jadi entitas, supaya teks",
                    "dari pengguna nggak pernah dibaca sebagai tag. Tanpa itu, nama produk",
                    "berisi <script> akan ikut dijalankan browser. Framework sungguhan",
                    "melakukan escape otomatis dengan cara yang sama.",
                    "",
                    "renderToString adalah inti render di server: React punya fungsi bernama",
                    "sama di react-dom/server, dan Vue di vue/server-renderer. Materi ketiga",
                    "bab ini membahas kapan itu dipakai.",
                ],
            },
            {
                "heading": "diff: mencari yang berubah",
                "body": [
                    "Sekarang bayangkan state berubah dan fungsi tampilan menghasilkan pohon",
                    "baru. diff menelusuri pohon lama dan pohon baru bersamaan, simpul demi",
                    "simpul, lalu mencatat pekerjaan yang perlu dilakukan pada DOM. Setiap",
                    "catatan disebut patch, dan posisinya ditulis sebagai jalur indeks: 0.1.2",
                    "artinya anak ke-2 dari anak ke-1 dari akar (dihitung dari 0).",
                    "",
                    "Ada lima jenis patch yang cukup untuk hampir semua kasus:",
                    "",
                    "  TEKS     isi teks berubah, misalnya \"Cuci motor\" jadi \"Cuci mobil\"",
                    "  ATRIBUT  atribut ditambah, diubah, atau dibuang",
                    "  TAMBAH   di pohon baru ada anak yang dulu nggak ada",
                    "  HAPUS    anak di pohon lama nggak ada lagi",
                    "  GANTI    tag-nya beda (misalnya p jadi div): seluruh cabang",
                    "           dibuang dan dibuat baru tanpa dibandingkan lagi",
                    "",
                    "Aturan ganti cabang itu jalan pintas yang disengaja. Membandingkan dua",
                    "pohon secara sempurna butuh waktu yang meledak seiring jumlah simpul.",
                    "React memakai dua anggapan supaya diff cukup sekali jalan: elemen dengan",
                    "jenis berbeda dianggap menghasilkan pohon berbeda, dan developer bisa",
                    "memberi petunjuk lewat key. Kamu menulis diff lengkap di latihan bab",
                    "ini.",
                ],
            },
            {
                "heading": "Kenapa key ada",
                "body": [
                    "Jalan pintas kedua menyangkut daftar. Kalau anak-anak cuma dicocokkan",
                    "menurut posisi, menyisipkan satu butir di depan membuat semua butir",
                    "sesudahnya terlihat berubah. Program di bawah membandingkan dua cara",
                    "mencocokkan.",
                ],
                "code": """// Mencocokkan anak lama dan baru: menurut posisi atau menurut key.
const lama = [
  { key: 'k1', teks: 'Beli kopi' },
  { key: 'k2', teks: 'Cuci motor' },
  { key: 'k3', teks: 'Bayar listrik' },
];
// Satu tugas baru disisipkan di paling atas.
const baru = [{ key: 'k4', teks: 'Jemput adik' }, ...lama];

function menurutPosisi(lama, baru) {
  const kerja = [];
  baru.forEach((b, i) => {
    if (!lama[i]) kerja.push(`buat "${b.teks}"`);
    else if (lama[i].teks !== b.teks) kerja.push(`ubah #${i} jadi "${b.teks}"`);
  });
  return kerja;
}

function menurutKey(lama, baru) {
  const ada = new Map(lama.map((x) => [x.key, x]));
  const kerja = [];
  baru.forEach((b, i) => {
    if (!ada.has(b.key)) kerja.push(`buat "${b.teks}" di posisi ${i}`);
  });
  return kerja;
}

console.log('Tanpa key:');
for (const k of menurutPosisi(lama, baru)) console.log('  ' + k);
console.log('Dengan key:');
for (const k of menurutKey(lama, baru)) console.log('  ' + k);""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  Tanpa key:",
                    "    ubah #0 jadi \"Jemput adik\"",
                    "    ubah #1 jadi \"Beli kopi\"",
                    "    ubah #2 jadi \"Cuci motor\"",
                    "    buat \"Bayar listrik\"",
                    "  Dengan key:",
                    "    buat \"Jemput adik\" di posisi 0",
                    "",
                    "Tanpa key, empat elemen disentuh. Lebih parah dari sekadar boros: kalau",
                    "tiap butir punya kotak centang atau input, keadaan butir pertama",
                    "sekarang menempel di \"Jemput adik\", karena elemen DOM-nya dipakai ulang",
                    "untuk data lain. Dengan key, framework tahu tiga butir lama masih ada",
                    "dan cuma membuat satu elemen baru.",
                    "",
                    "Karena itu React memperingatkan di konsol kalau daftar dirender tanpa",
                    "key. Aturannya:",
                    "",
                    "- Key harus unik di antara saudaranya dan stabil, biasanya id dari",
                    "  database.",
                    "- Indeks array sebagai key cuma aman untuk daftar yang nggak pernah",
                    "  disisipi, dihapus, atau diurutkan ulang.",
                    "- Key acak seperti Math.random() lebih buruk lagi: setiap render semua",
                    "  butir dianggap baru dan dibuat ulang.",
                ],
            },
            {
                "heading": "Siapa yang memakai virtual DOM",
                "body": [
                    "React memakai virtual DOM sejak awal; versi stabil terbarunya saat",
                    "materi ini ditulis (Oktober 2026) adalah 19.3.1. Preact menawarkan API",
                    "yang hampir sama dengan ukuran sekitar 3 kB, dan kini di versi",
                    "11. Vue 3 juga memakai virtual DOM, ditambah compiler template",
                    "yang menandai bagian statis supaya nggak perlu dibandingkan. Mode Vapor",
                    "di Vue, yang bekerja tanpa virtual DOM, belum masuk rilis stabil.",
                    "",
                    "Nggak semua framework memakai cara ini. Svelte mengompilasi komponen",
                    "jadi kode yang langsung mengubah DOM, dan Solid memakai signal yang tahu",
                    "persis elemen mana yang harus diubah. Signal adalah bahan materi",
                    "berikutnya.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Daftar panjang yang sering berubah, seperti kotak masuk email, feed",
                    "media sosial, atau daftar pesanan di dapur restoran, adalah tempat key",
                    "paling terasa. Bug \"centang pindah ke baris lain\" sesudah menghapus satu",
                    "butir adalah laporan klasik dari aplikasi React yang memakai indeks",
                    "sebagai key.",
                    "",
                    "Kasus kecil: di aplikasi to-do buatan temanmu, setiap butir punya kotak",
                    "centang. Sesudah butir paling atas dihapus, centang yang tadinya di",
                    "butir kedua pindah ke butir ketiga.",
                    "",
                    "Cara memecahkannya:",
                    "1. Cari bagian yang merender daftar, misalnya tugas.map((t, i) => <Butir",
                    "   key={i} ... />).",
                    "2. Ganti key dengan nilai yang melekat pada datanya, misalnya key={t.id}.",
                    "   Kalau datanya belum punya id, beri id saat butir dibuat (misalnya",
                    "   crypto.randomUUID()), bukan saat dirender.",
                    "3. Ulangi skenarionya: centang butir kedua, hapus butir pertama, pastikan",
                    "   centangnya tetap di butir yang sama.",
                ],
            },
        ],
    },
    {
        "title": "9. Signal dan Proxy Reaktif dari Nol",
        "sections": [
            {
                "body": [
                    "Virtual DOM menjawab \"bagaimana mengubah DOM seperlunya\", tapi harganya:",
                    "setiap perubahan kecil, seluruh fungsi komponen dijalankan ulang, lalu",
                    "pohonnya dibandingkan. Di halaman besar, mengubah satu angka bisa",
                    "berarti membangun dan membandingkan ribuan simpul.",
                    "",
                    "Ada cara lain yang sekarang dipakai hampir semua framework baru:",
                    "reaktivitas halus (fine-grained). Setiap nilai tahu siapa saja yang",
                    "membacanya. Waktu nilainya berubah, cuma pembacanya yang dijalankan",
                    "ulang. Mirip langganan koran: waktu edisi baru terbit, yang diantari",
                    "cuma pelanggan koran itu, bukan seluruh kompleks.",
                ],
            },
            {
                "heading": "Tiga bagian: signal, effect, computed",
                "body": [
                    "- signal: wadah satu nilai. Dibaca lewat .value, diubah dengan mengisi",
                    "  .value.",
                    "- effect: fungsi yang dijalankan sekali, lalu dijalankan ulang setiap kali",
                    "  signal yang ia baca berubah. Di framework, effect semacam ini yang",
                    "  memperbarui DOM.",
                    "- computed: nilai turunan yang dihitung dari signal lain, seperti total =",
                    "  jumlah x harga. Ia sendiri bisa dibaca seperti signal.",
                    "",
                    "Bagian paling cerdik ada di pelacakan dependensi. Kamu nggak perlu",
                    "menulis \"effect ini bergantung pada jumlah dan total\". Selama effect",
                    "berjalan, setiap signal yang dibaca mencatat effect itu sebagai",
                    "pelanggannya. Caranya cuma satu variabel global yang menunjuk effect",
                    "yang sedang berjalan.",
                ],
            },
            {
                "heading": "Signal mini",
                "code": """let efekAktif = null; // efek yang sedang berjalan saat ini

function signal(awal) {
  let nilai = awal;
  const pelanggan = new Set();
  return {
    get value() {
      if (efekAktif) pelanggan.add(efekAktif); // catat siapa yang membaca
      return nilai;
    },
    set value(baru) {
      nilai = baru;
      for (const efek of pelanggan) efek(); // kabari semua pembaca
    },
  };
}

function effect(fn) {
  const jalan = () => {
    efekAktif = jalan;
    fn();
    efekAktif = null;
  };
  jalan();
}

function computed(fn) {
  const hasil = signal(undefined);
  effect(() => { hasil.value = fn(); });
  return hasil;
}

const jumlah = signal(1);
const harga = signal(18000);
const total = computed(() => jumlah.value * harga.value);

effect(() => console.log(`Tampilan: ${jumlah.value} gelas, Rp${total.value}`));

jumlah.value = 2;
harga.value = 20000;""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  Tampilan: 1 gelas, Rp18000",
                    "  Tampilan: 2 gelas, Rp36000",
                    "  Tampilan: 2 gelas, Rp36000",
                    "  Tampilan: 2 gelas, Rp40000",
                    "",
                    "Baris pertama muncul karena effect selalu dijalankan sekali saat dibuat.",
                    "Waktu itulah ia membaca jumlah dan total, jadi keduanya mencatatnya",
                    "sebagai pelanggan. Mengubah harga nggak langsung memanggil effect",
                    "tampilan, karena effect itu nggak pernah membaca harga. Ia ikut jalan",
                    "karena total berubah.",
                    "",
                    "Ada yang janggal: sesudah jumlah.value = 2, tampilan muncul dua kali",
                    "dengan isi sama. Jumlah punya dua pelanggan, yaitu computed total dan",
                    "effect tampilan, dan keduanya dijalankan. Total dihitung ulang dan",
                    "memicu tampilan, lalu tampilan dipanggil lagi sebagai pelanggan langsung",
                    "jumlah. Pustaka sungguhan menghindari ini dengan mengurutkan pembaruan",
                    "dan mengumpulkannya dulu (batch), dan dengan melewati pembaruan kalau",
                    "nilai baru sama dengan yang lama. Kamu menambahkan pengecekan itu di",
                    "latihan.",
                ],
            },
            {
                "heading": "Hal yang sama dengan Preact Signals",
                "body": [
                    "Preact Signals memakai nama fungsi yang persis sama. Jalankan di",
                    "proyekmu sendiri sesudah npm install @preact/signals-core:",
                ],
                "code": """import { signal, computed, effect, batch } from '@preact/signals-core';

const jumlah = signal(1);
const harga = signal(18000);
const total = computed(() => jumlah.value * harga.value);

const berhenti = effect(() => {
  console.log(`Tampilan: ${jumlah.value} gelas, Rp${total.value}`);
});
jumlah.value = 2;
harga.value = 20000;
batch(() => { jumlah.value = 3; harga.value = 15000; });
berhenti(); // effect dilepas, perubahan berikutnya diabaikan
jumlah.value = 9;""",
            },
            {
                "body": [
                    "Hasilnya empat baris: 1 gelas Rp18000, 2 gelas Rp36000, 2 gelas Rp40000,",
                    "lalu 3 gelas Rp45000. Nggak ada baris kembar, dan dua perubahan di dalam",
                    "batch cuma memicu satu tampilan. effect juga mengembalikan fungsi untuk",
                    "melepasnya, yang di framework dipanggil saat komponen hilang dari layar",
                    "supaya nggak ada effect yang tertinggal.",
                ],
            },
            {
                "heading": "Proxy: reaktif tanpa .value",
                "body": [
                    "Menulis .value di mana-mana terasa kaku. Vue 3, MobX, dan Valtio memakai",
                    "Proxy supaya objek biasa bisa reaktif. Proxy adalah objek pembungkus",
                    "yang mencegat setiap pembacaan dan penulisan properti lewat fungsi yang",
                    "disebut trap: get untuk membaca, set untuk menulis. Idenya sama dengan",
                    "signal, cuma pelanggannya dicatat per nama properti.",
                ],
                "code": """let efekAktif = null;
const peta = new WeakMap(); // objek -> (nama properti -> himpunan efek)

function reactive(objek) {
  return new Proxy(objek, {
    get(target, kunci) {
      if (efekAktif) {
        if (!peta.has(target)) peta.set(target, new Map());
        const perKunci = peta.get(target);
        if (!perKunci.has(kunci)) perKunci.set(kunci, new Set());
        perKunci.get(kunci).add(efekAktif);
      }
      return target[kunci];
    },
    set(target, kunci, nilai) {
      target[kunci] = nilai;
      const efek = peta.get(target)?.get(kunci) || [];
      for (const e of efek) e();
      return true;
    },
  });
}

function effect(fn) {
  const jalan = () => {
    efekAktif = jalan;
    fn();
    efekAktif = null;
  };
  jalan();
}

const profil = reactive({ nama: 'Sari', kota: 'Bandung', poin: 0 });

effect(() => console.log(`Kartu: ${profil.nama} dari ${profil.kota}`));

profil.kota = 'Medan'; // dibaca efek, jadi efeknya jalan ulang
profil.poin = 50;      // nggak pernah dibaca efek, jadi diam saja
console.log('poin sekarang', profil.poin);""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  Kartu: Sari dari Bandung",
                    "  Kartu: Sari dari Medan",
                    "  poin sekarang 50",
                    "",
                    "Mengubah poin nggak memicu apa pun, karena effect kartu nggak pernah",
                    "membaca poin. Itulah \"halus\" yang dimaksud: perubahan cuma sampai ke",
                    "bagian yang memakai nilainya.",
                    "",
                    "Vue 3 membangun reactive() dengan cara ini, sedangkan ref() di Vue",
                    "memakai getter .value seperti signal di atas. MobX (versi 7) dan Valtio",
                    "(versi 2) juga berbasis Proxy.",
                    "",
                    "Jebakan: memecah objek reaktif dengan destructuring, misalnya const {",
                    "kota } = profil. Variabel kota cuma salinan nilai saat itu, bukan jalur",
                    "ke Proxy, jadi perubahan berikutnya nggak pernah sampai. Vue menyediakan",
                    "toRefs untuk kasus ini.",
                ],
            },
            {
                "heading": "Signal di framework sungguhan",
                "body": [
                    "Konsep yang baru kamu bangun dipakai ulang di hampir semua framework",
                    "yang akan kamu temui, cuma namanya beda:",
                    "",
                    "  Framework   Nilai           Turunan          Efek",
                    "  Preact      signal()        computed()       effect()",
                    "  Angular     signal()        computed()       effect()",
                    "  Solid       createSignal()  createMemo()     createEffect()",
                    "  Vue         ref/reactive    computed()       watchEffect()",
                    "  Svelte 5    $state          $derived         $effect",
                    "  Qwik        useSignal()     useComputed$()   useTask$()",
                    "",
                    "Signal juga diusulkan jadi fitur bawaan JavaScript lewat proposal TC39.",
                    "Saat dicek pada Oktober 2026 proposal itu masih di Stage 1, tahap paling",
                    "awal, jadi belum bisa dipakai tanpa pustaka dan API-nya masih bisa",
                    "berubah.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Dasbor yang angkanya diperbarui terus, seperti grafik harga saham atau",
                    "papan skor pertandingan, adalah tempat signal paling terasa. Yang",
                    "berubah cuma beberapa angka per detik, dan signal membuat cuma angka itu",
                    "yang disentuh, tanpa membandingkan seluruh halaman.",
                    "",
                    "Kasus kecil: komponen Vue menampilkan nama dan kota dari objek reaktif",
                    "profil. Sesudah kamu merapikan kodenya jadi const { nama, kota } =",
                    "profil, tampilan nggak lagi ikut berubah waktu profil.kota diganti.",
                    "",
                    "Cara memecahkannya:",
                    "1. Sadari penyebabnya: destructuring menyalin nilai saat itu dan memutus",
                    "   hubungan dengan Proxy.",
                    "2. Baca langsung dari objeknya di template, misalnya profil.kota, supaya",
                    "   trap get tetap terpanggil di dalam effect render.",
                    "3. Kalau memang butuh variabel terpisah, pakai const { nama, kota } =",
                    "   toRefs(profil), lalu baca kota.value.",
                    "4. Uji dengan mengubah profil.kota dan memastikan tampilan ikut berubah.",
                ],
            },
        ],
    },
    {
        "title": "10. Render di Server, Statis, dan Hydration",
        "sections": [
            {
                "body": [
                    "Aplikasi yang dibuat dengan React atau Vue secara bawaan mengirim HTML",
                    "yang hampir kosong, cuma berisi <div id=\"app\"></div> dan tautan ke",
                    "berkas JavaScript. Halamannya baru muncul setelah JavaScript selesai",
                    "diunduh dan dijalankan. Di laptop dengan internet kencang itu cepat. Di",
                    "ponsel murah dengan sinyal lemah, pengunjung menatap layar putih",
                    "beberapa detik, dan mesin pencari yang nggak menjalankan JavaScript",
                    "melihat halaman kosong.",
                    "",
                    "Jawabannya adalah merender HTML lebih dulu, di server atau saat build,",
                    "memakai fungsi seperti renderToString dari materi pertama. Ada beberapa",
                    "mode, dan meta-framework seperti Next.js, Nuxt, SvelteKit, dan Astro",
                    "membiarkanmu memilih per halaman.",
                ],
            },
            {
                "heading": "Empat mode render",
                "body": [
                    "- CSR (client-side rendering): server mengirim HTML kosong, browser yang",
                    "  merender semuanya. Ini aplikasi satu halaman (SPA) klasik.",
                    "- SSR (server-side rendering): server merender HTML lengkap untuk setiap",
                    "  permintaan, dengan data terbaru saat itu.",
                    "- SSG (static site generation): HTML dirender sekali saat build, lalu",
                    "  berkas yang sama dikirim ke semua pengunjung.",
                    "- ISR (incremental static regeneration): seperti SSG, tapi halaman",
                    "  tertentu dibuat ulang di latar belakang setelah selang waktu tertentu.",
                    "  Istilah ini dipopulerkan Next.js.",
                    "",
                    "  Mode  HTML dibuat        Data          Cocok untuk",
                    "  CSR   di browser         saat dibuka   dasbor di balik login",
                    "  SSR   tiap permintaan    selalu baru   toko dengan stok berubah",
                    "  SSG   saat build         saat build    blog, dokumentasi",
                    "  ISR   build + berkala    hampir baru   katalog besar",
                ],
            },
            {
                "heading": "Hydration",
                "body": [
                    "HTML dari server langsung tampil, tapi masih mati: tombolnya belum",
                    "bereaksi karena event listener belum terpasang. Setelah JavaScript",
                    "sampai, framework merender komponen yang sama sekali lagi di memori,",
                    "mencocokkannya dengan DOM yang sudah ada, lalu memasang listener tanpa",
                    "membuat elemen baru. Proses ini disebut hydration, seperti menyiram air",
                    "ke mi instan yang tadinya kering: bentuknya sudah ada, tinggal",
                    "dihidupkan.",
                    "",
                    "Selama hydration belum selesai, halaman kelihatan siap padahal belum.",
                    "Pengunjung yang mengetuk tombol pada saat itu nggak mendapat respons apa",
                    "pun. Makin besar JavaScript-nya, makin lama jeda ini.",
                ],
            },
            {
                "heading": "Hydration mismatch",
                "body": [
                    "Hydration mengandalkan satu syarat: render pertama di browser harus",
                    "menghasilkan HTML yang sama dengan server. Kalau beda, terjadilah",
                    "hydration mismatch. Framework memberi peringatan di konsol, dan bagian",
                    "yang beda dirender ulang atau, lebih buruk, dibiarkan salah.",
                ],
                "code": """// Komponen yang sama dirender dua kali: di server, lalu di browser.
function Salam(jam) {
  const sapaan = jam < 11 ? 'Selamat pagi' : 'Selamat siang';
  return `<p>${sapaan}! Sekarang jam ${jam}.00</p>`;
}

// Server di Jakarta merender jam 10, HTML dikirim ke browser.
const dariServer = Salam(10);

// Halaman baru sampai dan JavaScript-nya selesai dimuat jam 11.
const diBrowser = Salam(11);

console.log('server :', dariServer);
console.log('browser:', diBrowser);
if (dariServer !== diBrowser) {
  console.log('hydration mismatch: HTML server beda dengan render pertama di browser');
}

// Perbaikannya: render pertama di browser memakai data yang sama dengan server.
const dataAwal = { jam: 10 }; // ikut dikirim di dalam HTML
console.log('sesudah diperbaiki sama?', Salam(dataAwal.jam) === dariServer);""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  server : <p>Selamat pagi! Sekarang jam 10.00</p>",
                    "  browser: <p>Selamat siang! Sekarang jam 11.00</p>",
                    "  hydration mismatch: HTML server beda dengan render pertama di browser",
                    "  sesudah diperbaiki sama? true",
                    "",
                    "Penyebab mismatch yang paling sering:",
                    "",
                    "- Waktu sekarang, seperti new Date(), yang pasti beda antara server dan",
                    "  browser.",
                    "- Bilangan acak dari Math.random().",
                    "- Kode yang memeriksa window atau localStorage. Di server keduanya nggak",
                    "  ada, jadi cabang yang dipilih beda.",
                    "- Format angka dan tanggal yang bergantung bahasa dan zona waktu mesin,",
                    "  misalnya toLocaleString().",
                    "- HTML yang nggak sah, seperti div di dalam p. Browser membetulkannya",
                    "  tanpa peringatan sehingga DOM-nya nggak lagi sama dengan HTML kiriman",
                    "  server.",
                    "",
                    "Perbaikannya: kirim data yang dipakai server ke browser (di contoh,",
                    "dataAwal), atau tunda bagian yang memang hanya bisa dihitung di browser",
                    "sampai hydration selesai. Di React itu biasanya lewat useEffect, di Vue",
                    "lewat onMounted.",
                ],
            },
            {
                "heading": "Islands dan resumability",
                "body": [
                    "Hydration penuh menghidupkan seluruh halaman, termasuk bagian yang cuma",
                    "teks. Dua pendekatan berusaha mengurangi kerja itu.",
                    "",
                    "Islands (pulau). Halaman dikirim sebagai HTML statis, dan cuma komponen",
                    "interaktif tertentu yang dihidrasi, seperti pulau di tengah lautan HTML.",
                    "Astro memakai cara ini: komponen baru dikirim JavaScript-nya kalau",
                    "diberi direktif client:, misalnya client:visible yang menunggu komponen",
                    "itu tergulir ke layar.",
                ],
                "bahasa": "astro",
                "code": """---
import Header from '../components/Header.astro';
import Keranjang from '../components/Keranjang.jsx';
---
<Header />                     <!-- HTML saja, tanpa JS -->
<article>Isi artikel...</article>
<Keranjang client:visible />   <!-- dihidrasi saat terlihat -->""",
            },
            {
                "body": [
                    "Resumability (bisa dilanjutkan). Qwik melewati hydration sama sekali.",
                    "Server menulis keadaan aplikasi dan informasi listener ke dalam HTML,",
                    "lalu browser baru mengunduh kode sebuah handler saat pengguna",
                    "berinteraksi dengannya. Aplikasi seolah dilanjutkan dari titik server",
                    "berhenti, bukan dijalankan ulang.",
                    "",
                    "React punya jalurnya sendiri: streaming SSR mengirim HTML sepotong demi",
                    "sepotong, dan Server Components merender sebagian komponen hanya di",
                    "server sehingga kodenya nggak pernah dikirim ke browser. Keduanya",
                    "dibahas di bab 6 dan bab 12.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Situs dokumentasi dan blog teknis kebanyakan dibuat dengan SSG, karena",
                    "isinya jarang berubah dan berkas statis bisa disajikan murah dari CDN.",
                    "Toko online biasanya memakai SSR atau ISR untuk halaman produk supaya",
                    "muncul di mesin pencari dengan harga yang benar, dan CSR untuk halaman",
                    "akun dan keranjang.",
                    "",
                    "Kasus kecil: halaman artikelmu menampilkan \"Diterbitkan 3 jam lalu\",",
                    "dirender di server. Konsol browser penuh peringatan hydration mismatch,",
                    "dan kadang tulisannya berkedip berganti.",
                    "",
                    "Cara memecahkannya:",
                    "1. Temukan sumber perbedaannya: teks relatif \"3 jam lalu\" dihitung dari",
                    "   waktu sekarang, yang beda di server dan browser.",
                    "2. Kirim tanggal terbit mentah (misalnya 2026-10-19T08:00:00Z) sebagai",
                    "   data, dan render tanggal absolut yang sama di kedua sisi.",
                    "3. Ganti jadi teks relatif hanya sesudah hydration selesai, misalnya di",
                    "   useEffect (React) atau onMounted (Vue).",
                    "4. Muat ulang halaman dan pastikan konsol bersih.",
                ],
            },
        ],
    },
    {
        "title": "11. Web Components, Lit, dan Stencil",
        "sections": [
            {
                "body": [
                    "Komponen React cuma bisa dipakai di React, komponen Vue cuma di Vue.",
                    "Kalau perusahaanmu punya tiga tim dengan tiga framework, tombol yang",
                    "sama harus ditulis tiga kali.",
                    "",
                    "Web Components adalah jawaban dari browser sendiri: sekumpulan standar",
                    "untuk membuat elemen HTML buatanmu, misalnya <kartu-produk>, yang bisa",
                    "dipakai di halaman HTML biasa maupun di framework apa pun. Isinya tiga",
                    "standar:",
                    "",
                    "- Custom Elements: mendaftarkan tag baru beserta kelas JavaScript-nya.",
                    "- Shadow DOM: pohon DOM tersembunyi milik elemen itu, dengan gaya yang",
                    "  nggak bocor keluar dan nggak kemasukan gaya dari luar.",
                    "- template dan slot: kerangka markup yang bisa diisi dari luar.",
                    "",
                    "Di State of HTML 2025, Custom Elements dipakai 52,6% responden. Keluhan",
                    "yang paling sering disebut tentang Web Components: terlalu rumit untuk",
                    "ditulis langsung. Itulah alasan Lit dan Stencil ada.",
                ],
            },
            {
                "heading": "Custom element pertama",
                "bahasa": "browser",
                "code": """class KartuProduk extends HTMLElement {
  static observedAttributes = ['nama', 'harga'];

  constructor() {
    super();
    this.attachShadow({ mode: 'open' });
  }

  connectedCallback() {          // dipanggil saat masuk ke halaman
    this.gambar();
  }

  attributeChangedCallback() {   // dipanggil saat atribut berubah
    this.gambar();
  }

  gambar() {
    const nama = this.getAttribute('nama') ?? '';
    const harga = Number(this.getAttribute('harga') ?? 0);
    this.shadowRoot.innerHTML = `
      <style>
        .kartu { border: 1px solid #ccc; padding: 1rem; }
        b { color: var(--warna-merek, #1a1a1a); }
      </style>
      <div class="kartu">
        <b></b> Rp<span></span>
        <slot></slot>
      </div>`;
    this.shadowRoot.querySelector('b').textContent = nama;
    this.shadowRoot.querySelector('span').textContent = harga;
  }
}

customElements.define('kartu-produk', KartuProduk);""",
            },
            {
                "body": [
                    "Tiga hal dari kode itu:",
                    "",
                    "- Nama custom element wajib mengandung tanda hubung, seperti kartu-produk.",
                    "  Aturan ini menjamin nama buatanmu nggak akan bentrok dengan elemen HTML",
                    "  resmi di masa depan.",
                    "- connectedCallback dan attributeChangedCallback adalah lifecycle, yaitu",
                    "  fungsi yang dipanggil browser di saat tertentu. Atribut cuma diamati",
                    "  kalau namanya tercantum di observedAttributes.",
                    "- Nama dan harga diisi lewat textContent, bukan disisipkan ke innerHTML,",
                    "  supaya teks dari luar nggak dibaca sebagai HTML. Ini prinsip escape yang",
                    "  sama dengan renderToString.",
                    "",
                    "Sesudah didaftarkan, tag itu dipakai seperti elemen biasa:",
                ],
            },
            {
                "bahasa": "html",
                "code": """<script type="module" src="kartu-produk.js"></script>

<kartu-produk nama="Kopi susu" harga="18000">
  <small>Stok tinggal 3</small>   <!-- masuk ke <slot> -->
</kartu-produk>""",
            },
            {
                "heading": "Shadow DOM: gaya yang terbungkus",
                "body": [
                    "CSS di dalam shadow root cuma berlaku di dalam elemen itu. Aturan b {",
                    "color: ... } di contoh tadi nggak mengubah tag b lain di halaman, dan",
                    "gaya halaman juga nggak bisa menembus masuk. Ini yang membuat Web",
                    "Components aman ditaruh di situs orang lain.",
                    "",
                    "Ada dua pintu yang sengaja dibuka. Variabel CSS seperti --warna-merek",
                    "tetap menembus batas shadow, jadi halaman bisa memberi tema. Dan atribut",
                    "part pada elemen di dalam shadow bisa ditata dari luar lewat ::part().",
                    "",
                    "Shadow DOM dulu hanya bisa dibuat lewat JavaScript, sehingga sulit",
                    "dirender di server. Sekarang ada Declarative Shadow DOM, yang didukung",
                    "semua browser utama sejak 2024. Shadow root ditulis langsung di HTML:",
                    "",
                    "  <kartu-produk>",
                    "    <template shadowrootmode=\"open\">",
                    "      <style>.kartu { padding: 1rem; }</style>",
                    "      <div class=\"kartu\"><slot></slot></div>",
                    "    </template>",
                    "    Kopi susu",
                    "  </kartu-produk>",
                ],
            },
            {
                "heading": "Lit: Web Components yang enak ditulis",
                "body": [
                    "Lit adalah pustaka kecil dari Google untuk menulis Web Components. Ia",
                    "menambahkan properti reaktif dan template dengan tagged template literal",
                    "(html`...`). Saat properti berubah, Lit cuma memperbarui bagian template",
                    "yang dinamis, tanpa virtual DOM. Versi terbarunya 3.3.3 (lisensi",
                    "BSD-3-Clause), dan bisa dipakai tanpa langkah build.",
                ],
                "bahasa": "browser",
                "code": """import { LitElement, html, css } from 'lit';

class TombolHitung extends LitElement {
  static properties = { jumlah: { type: Number } };
  static styles = css`button { font: inherit; padding: 0.5rem 1rem; }`;

  constructor() {
    super();
    this.jumlah = 0;
  }

  render() {
    return html`<button @click=${() => this.jumlah++}>
      Diklik ${this.jumlah} kali
    </button>`;
  }
}

customElements.define('tombol-hitung', TombolHitung);""",
            },
            {
                "heading": "Stencil: compiler dari tim Ionic",
                "body": [
                    "Stencil mengambil arah lain. Kamu menulis komponen dengan TypeScript,",
                    "decorator, dan JSX, lalu compiler Stencil menghasilkan Web Components",
                    "standar yang nggak bergantung pada Stencil saat dijalankan. Tim Ionic",
                    "membuatnya untuk membangun komponen Ionic Framework, dan kini banyak",
                    "dipakai untuk design system. Versinya 4.45, lisensi MIT.",
                ],
                "bahasa": "tsx",
                "code": """import { Component, Prop, h } from '@stencil/core';

@Component({ tag: 'kartu-harga', styleUrl: 'kartu-harga.css', shadow: true })
export class KartuHarga {
  @Prop() nama: string;
  @Prop() harga: number;

  render() {
    return <div><b>{this.nama}</b> Rp{this.harga}</div>;
  }
}""",
            },
            {
                "heading": "Kapan memilih Web Components",
                "body": [
                    "Web Components unggul untuk hal yang harus hidup di banyak tempat:",
                    "",
                    "- Design system yang dipakai beberapa tim dengan framework berbeda.",
                    "- Widget yang ditempel di situs orang lain, seperti tombol bayar, jendela",
                    "  chat, atau peta.",
                    "- Halaman HTML biasa yang cuma butuh beberapa elemen interaktif tanpa",
                    "  memasang framework.",
                    "",
                    "Untuk aplikasi utuh, framework tetap lebih nyaman. Pengelolaan state,",
                    "rute, dan render di server sudah tersedia di sana, dan ekosistemnya jauh",
                    "lebih besar. Keduanya juga bisa digabung: sejak React 19, React",
                    "mendukung penuh custom element, termasuk properti dan event-nya, jadi",
                    "komponen Lit bisa dipakai langsung di dalam aplikasi React.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Beberapa design system besar dirilis sebagai Web Components, misalnya",
                    "Spectrum Web Components dari Adobe dan Fluent UI Web Components dari",
                    "Microsoft. Dengan begitu mereka bisa dipakai di produk mana pun, apa pun",
                    "framework-nya. Widget chat layanan pelanggan yang ditempel di banyak",
                    "situs toko juga sering memakai Shadow DOM supaya tampilannya nggak",
                    "dirusak CSS situs tuan rumah.",
                    "",
                    "Kasus kecil: kamu diminta membuat widget \"Hubungi kami via WhatsApp\"",
                    "yang akan ditempel di lima situs klien dengan CSS yang berbeda-beda. Di",
                    "situs pertama, tombolnya mendadak jadi ungu dan hurufnya raksasa.",
                    "",
                    "Cara memecahkannya:",
                    "1. Bungkus widget sebagai custom element, misalnya <tombol-wa",
                    "   nomor=\"62812...\">, dan pasang shadow root dengan attachShadow({ mode:",
                    "   'open' }).",
                    "2. Pindahkan semua CSS widget ke dalam shadow root, supaya gaya situs",
                    "   klien nggak bisa menembus.",
                    "3. Sediakan variabel CSS, misalnya --tombol-wa-warna, untuk hal yang",
                    "   memang boleh disesuaikan klien.",
                    "4. Kirim sebagai satu berkas JavaScript yang cukup dimuat dengan <script",
                    "   type=\"module\">, lalu uji di kelima situs.",
                ],
            },
        ],
    },
    {
        "title": "12. Tailwind CSS: Berpikir dengan Kelas Utility",
        "sections": [
            {
                "body": [
                    "Di kurikulum CSS kamu menulis gaya dengan cara klasik: beri nama kelas",
                    "yang menjelaskan isinya, misalnya .kartu-produk, lalu tulis aturannya di",
                    "berkas CSS. Cara itu bagus untuk halaman kecil. Di proyek yang terus",
                    "tumbuh, muncul dua masalah. Kamu harus terus mengarang nama",
                    "(.kartu-produk-kecil, .kartu-produk-promo-baru), dan berkas CSS cuma",
                    "bisa bertambah, karena nggak ada yang berani menghapus aturan lama yang",
                    "mungkin masih dipakai entah di mana.",
                    "",
                    "Tailwind CSS memakai pendekatan utility-first. Gayanya ditulis lewat",
                    "kelas-kelas kecil yang masing-masing cuma mengerjakan satu hal, langsung",
                    "di HTML. p-4 artinya padding 1rem, flex artinya display: flex,",
                    "text-center artinya teks rata tengah. Kamu nggak lagi menamai komponen",
                    "di CSS; kamu merangkai kelas yang sudah ada.",
                ],
            },
            {
                "heading": "Kartu produk dengan kelas utility",
                "bahasa": "html",
                "code": """<div class="mx-auto max-w-md rounded-xl bg-white p-4 shadow-md
            flex flex-col gap-4 md:flex-row md:items-center">
  <img class="size-24 rounded-lg object-cover" src="kopi.jpg" alt="Kopi susu">
  <div class="flex-1">
    <h2 class="text-lg font-semibold text-slate-900">Kopi Susu</h2>
    <p class="text-slate-600">Rp18.000</p>
  </div>
  <button class="rounded-lg bg-sky-600 px-4 py-2 text-white
                 hover:bg-sky-700 focus-visible:outline-2">Beli</button>
</div>""",
            },
            {
                "heading": "Membaca kelasnya",
                "body": [
                    "Kelas Tailwind kelihatan seperti sandi, tapi polanya teratur. Hampir",
                    "semuanya bisa ditebak kalau kamu sudah paham CSS:",
                    "",
                    "  Kelas          CSS yang dihasilkan",
                    "  p-4            padding: 1rem",
                    "  px-4 py-2      padding kiri-kanan 1rem, atas-bawah 0.5rem",
                    "  mx-auto        margin kiri-kanan auto (ke tengah)",
                    "  flex flex-col  display: flex; flex-direction: column",
                    "  gap-4          gap: 1rem",
                    "  rounded-xl     border-radius: 0.75rem",
                    "  text-lg        font-size: 1.125rem (plus line-height)",
                    "  font-semibold  font-weight: 600",
                    "  bg-sky-600     warna latar dari palet, tingkat 600",
                    "  size-24        width dan height 6rem",
                    "",
                    "Angka jarak memakai satu skala: angka dikali 0.25rem. p-1 sama dengan",
                    "0.25rem, p-4 sama dengan 1rem, p-8 sama dengan 2rem. Warna punya tingkat",
                    "50 sampai 950, makin besar makin gelap.",
                    "",
                    "Jadi Tailwind tetap CSS, cuma ditulis dengan cara lain. Kalau kamu belum",
                    "paham flexbox dan grid (kurikulum CSS bab 5), kelas flex items-center",
                    "juga nggak akan menolong. Dokumentasi resmi di tailwindcss.com",
                    "menampilkan CSS di balik setiap kelas, dan itu cara tercepat",
                    "menghafalnya.",
                ],
            },
            {
                "heading": "Responsif dan keadaan",
                "body": [
                    "Awalan seperti md: dan hover: disebut varian. Varian membuat kelas cuma",
                    "berlaku dalam kondisi tertentu.",
                    "",
                    "Tailwind memakai pendekatan mobile-first. Kelas tanpa awalan berlaku di",
                    "semua ukuran layar. Kelas dengan awalan md: berlaku mulai lebar 48rem",
                    "(768 piksel) ke atas. Jadi flex-col md:flex-row artinya \"bertumpuk di",
                    "ponsel, berjajar mulai layar sedang\". Titik patah bawaannya:",
                    "",
                    "  sm   40rem (640px)     lg   64rem (1024px)",
                    "  md   48rem (768px)     xl   80rem (1280px)",
                    "                         2xl  96rem (1536px)",
                    "",
                    "Jebakan: mengira md: berarti \"khusus tablet\". md: berarti tablet dan",
                    "semua yang lebih lebar. Untuk gaya yang cuma berlaku di bawah ukuran",
                    "tertentu, pakai max-md:.",
                    "",
                    "Varian keadaan bekerja dengan cara yang sama: hover:bg-sky-700 saat",
                    "kursor di atasnya, focus-visible:outline-2 saat difokus lewat papan",
                    "ketik, disabled:opacity-50 saat tombol nonaktif, dan dark: saat mode",
                    "gelap. Varian boleh ditumpuk, misalnya md:hover:underline.",
                ],
            },
            {
                "heading": "Kenapa ada yang suka dan ada yang nggak",
                "body": [
                    "Yang membuat orang suka:",
                    "",
                    "- Nggak perlu mengarang nama kelas untuk setiap pembungkus.",
                    "- Mengubah satu elemen nggak akan merusak elemen lain di halaman yang",
                    "  jauh, karena gayanya menempel di elemen itu sendiri.",
                    "- CSS akhirnya kecil: berkas yang dikirim cuma berisi kelas yang memang",
                    "  muncul di kodemu.",
                    "- Jarak, warna, dan ukuran huruf dipilih dari skala yang sama, jadi",
                    "  desainnya konsisten tanpa harus diawasi.",
                    "",
                    "Yang membuat orang nggak suka: HTML jadi panjang dan ramai, dan kamu",
                    "harus menghafal nama kelas. Tim Tailwind sendiri menganjurkan membungkus",
                    "elemen yang berulang jadi komponen (komponen React, Vue, atau Svelte).",
                    "Memindahkan semuanya kembali ke CSS lewat @apply justru menghilangkan",
                    "manfaatnya. Daftar kelas panjang itu cuma ditulis sekali di dalam",
                    "komponen KartuProduk.",
                ],
            },
            {
                "heading": "Bagaimana Tailwind tahu kelas mana yang dipakai",
                "body": [
                    "Tailwind nggak menjalankan kodemu. Ia membaca berkas proyek sebagai teks",
                    "biasa, mencari potongan yang bentuknya mirip nama kelas, lalu membuat",
                    "CSS untuk yang ia kenali. Program di bawah meniru cara itu dengan pola",
                    "sederhana.",
                ],
                "code": "// Tailwind nggak menjalankan kodemu. Ia cuma memindai teks berkas,\n// mencari potongan yang bentuknya mirip nama kelas.\nconst sumber = `\nconst warna = 'red';\nconst tombolA = 'bg-blue-500 text-white px-4';\nconst tombolB = \\`bg-\\${warna}-500\\`;\nconst tombolC = adaError ? 'bg-orange-500' : 'bg-green-500';\n`;\n\nconst kandidat = new Set(sumber.match(/[a-z]+(?:-[a-z0-9]+)+/g));\nfor (const kelas of ['bg-blue-500', 'px-4', 'bg-orange-500', 'bg-red-500']) {\n  console.log(kelas.padEnd(13), kandidat.has(kelas) ? 'ketemu' : 'tidak ketemu');\n}",
            },
            {
                "body": [
                    "Keluaran:",
                    "  bg-blue-500   ketemu",
                    "  px-4          ketemu",
                    "  bg-orange-500 ketemu",
                    "  bg-red-500    tidak ketemu",
                    "",
                    "bg-red-500 nggak pernah tertulis utuh di berkas. Ia baru ada waktu kode",
                    "dijalankan, hasil menyambung \"bg-\", isi variabel warna, dan \"-500\".",
                    "Karena Tailwind cuma membaca teks, kelas itu nggak dibuat, dan tombolnya",
                    "tampil tanpa warna latar.",
                    "",
                    "Ingat: tulis nama kelas selalu utuh. Kalau warnanya bergantung data,",
                    "pakai peta objek, misalnya { merah: 'bg-red-500', hijau: 'bg-green-500'",
                    "}[warna]. Kedua nama kelas itu tertulis lengkap di berkas, jadi Tailwind",
                    "menemukannya.",
                ],
            },
            {
                "heading": "Status dan popularitas",
                "body": [
                    "Versi stabil terbaru saat materi ini ditulis (Oktober 2026) adalah",
                    "Tailwind CSS 4.3.3, rilis Juli 2026, berlisensi MIT. Di State of CSS",
                    "2025, Tailwind dipakai sekitar 37% responden (2.041 dari 5.506), jadi",
                    "framework CSS nomor satu. Bootstrap ada di urutan kedua dengan sekitar",
                    "22%.",
                    "",
                    "Satu kabar yang perlu kamu tahu: pada Januari 2026, Tailwind Labs,",
                    "perusahaan di balik Tailwind, memangkas sekitar 75% engineer-nya karena",
                    "pendapatannya turun. Kodenya tetap open source dan tetap dirilis, tapi",
                    "keberlanjutan proyek seperti ini layak dipantau sebelum kamu",
                    "menggantungkan proyek besar padanya.",
                    "",
                    "Cara memasangnya di proyek dibahas di materi berikutnya, karena versi 4",
                    "mengubah banyak hal dibanding tutorial versi 3 yang masih bertebaran.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Banyak template dasbor admin dan landing page, yang dijual maupun yang",
                    "gratis, sekarang dibuat dengan Tailwind. Banyak pustaka komponen untuk",
                    "React dan Vue juga memakai kelas Tailwind di dalamnya, misalnya",
                    "shadcn/ui yang dibahas di bab 13.",
                    "",
                    "Kasus kecil: kamu membuat badge status pesanan yang warnanya diambil",
                    "dari data: `bg-${status}-500`. Di mode pengembangan kadang warnanya",
                    "muncul, kadang nggak, dan di versi produksi semua badge tampil tanpa",
                    "warna.",
                    "",
                    "Cara memecahkannya:",
                    "1. Pahami penyebabnya: nama kelas yang dirakit saat berjalan nggak pernah",
                    "   tertulis utuh, jadi Tailwind nggak membuatnya. Kelas yang kadang muncul",
                    "   ternyata kebetulan dipakai utuh di berkas lain.",
                    "2. Buat peta status ke kelas utuh:",
                    "       const WARNA = { baru: 'bg-sky-500', dikirim: 'bg-amber-500',",
                    "                       selesai: 'bg-green-600' };",
                    "3. Pakai nilai dari peta itu di atribut class, dan beri kelas cadangan",
                    "   seperti bg-slate-400 untuk status yang nggak dikenal.",
                    "4. Jalankan build produksi lagi dan periksa setiap status.",
                ],
            },
        ],
    },
    {
        "title": "13. Tailwind v4: Tema, Varian, dan Plugin",
        "sections": [
            {
                "body": [
                    "Tailwind CSS v4.0 rilis 22 Januari 2025 dan ditulis ulang hampir",
                    "seluruhnya. Mesinnya lebih cepat, Lightning CSS dipakai di dalamnya",
                    "untuk mengolah CSS, dan perubahan yang paling terasa: konfigurasi pindah",
                    "dari JavaScript ke CSS.",
                    "",
                    "Itu penting karena tutorial versi 3 masih banyak sekali di internet.",
                    "Tandanya gampang dikenali: ada berkas tailwind.config.js berisi content",
                    "dan theme, dan berkas CSS-nya diawali tiga baris @tailwind base,",
                    "@tailwind components, dan @tailwind utilities. Di versi 4, semuanya",
                    "diganti satu baris @import \"tailwindcss\" dan pengaturan lain ditulis di",
                    "CSS.",
                ],
            },
            {
                "heading": "Memasang di proyek Vite",
                "bahasa": "terminal",
                "code": """npm create vite@latest toko -- --template vanilla
cd toko
npm install tailwindcss @tailwindcss/vite""",
            },
            {
                "body": [
                    "Lalu daftarkan plugin-nya di vite.config.js, dan tulis satu baris di",
                    "berkas CSS utama. Vite sendiri dibahas di bab 5; untuk sekarang cukup",
                    "tahu bahwa ia alat yang menjalankan proyekmu saat pengembangan.",
                ],
                "code": """import { defineConfig } from 'vite';
import tailwindcss from '@tailwindcss/vite';

export default defineConfig({
  plugins: [tailwindcss()],
});""",
            },
            {
                "heading": "Tema lewat @theme",
                "bahasa": "css",
                "code": """@import "tailwindcss";

@theme {
  --color-merek-500: #c2410c;
  --color-merek-700: #9a3412;
  --font-display: "Poppins", sans-serif;
  --breakpoint-3xl: 120rem;
}""",
            },
            {
                "body": [
                    "Setiap variabel di dalam @theme punya awalan yang menentukan kelas apa",
                    "yang dibuat:",
                    "",
                    "- --color-merek-500 membuat bg-merek-500, text-merek-500,",
                    "  border-merek-500, dan seterusnya.",
                    "- --font-display membuat kelas font-display.",
                    "- --breakpoint-3xl membuat varian baru 3xl: untuk layar 120rem ke atas.",
                    "- --spacing (bawaannya 0.25rem) adalah satuan skala jarak. p-4 dihitung",
                    "  sebagai 4 kali --spacing.",
                    "",
                    "Semua nilai tema juga jadi variabel CSS biasa yang bisa kamu pakai di",
                    "mana saja, misalnya color: var(--color-merek-500) di CSS buatanmu",
                    "sendiri atau di dalam JavaScript.",
                    "",
                    "Versi 4 juga menemukan berkas sumber secara otomatis, dan berkas yang",
                    "tercantum di .gitignore dilewati. Kalau ada kelas di tempat yang nggak",
                    "terjangkau, misalnya di dalam paket node_modules, tambahkan jalurnya",
                    "dengan @source.",
                ],
            },
            {
                "heading": "Varian yang sering dipakai",
                "bahasa": "html",
                "code": """<!-- keadaan elemen lain: group dan peer -->
<a class="group block rounded-lg p-4 hover:bg-slate-100" href="/kopi">
  <h3 class="font-semibold group-hover:underline">Kopi Susu</h3>
</a>

<!-- atribut ARIA dan data -->
<button aria-expanded="false" class="aria-expanded:bg-sky-100">Menu</button>
<div data-state="open" class="hidden data-[state=open]:block">...</div>

<!-- container query: menyesuaikan lebar induk, bukan layar -->
<div class="@container">
  <div class="flex flex-col @md:flex-row">...</div>
</div>

<!-- menghormati pengaturan gerak pengguna -->
<div class="animate-bounce motion-reduce:animate-none">!</div>""",
            },
            {
                "body": [
                    "group dan peer membuat sebuah elemen bereaksi pada keadaan elemen lain:",
                    "judul digarisbawahi saat seluruh kartu di-hover. aria-expanded: dan",
                    "data-[state=open]: menata elemen berdasarkan atributnya, jadi tampilan",
                    "dan keadaan aksesibilitas dari bab 2 selalu sejalan. Container query",
                    "(lihat kurikulum CSS bab 8) sudah bawaan di versi 4 tanpa plugin.",
                ],
            },
            {
                "heading": "Mode gelap",
                "body": [
                    "Secara bawaan, varian dark: mengikuti pengaturan sistem operasi lewat",
                    "media query prefers-color-scheme. Kalau situsmu punya tombol pengalih",
                    "tema sendiri, ganti cara kerjanya dengan @custom-variant supaya dark:",
                    "aktif saat elemen induk punya kelas dark:",
                ],
                "bahasa": "css",
                "code": """@import "tailwindcss";

@custom-variant dark (&:where(.dark, .dark *));""",
            },
            {
                "heading": "Utility sendiri dan plugin",
                "bahasa": "css",
                "code": """@import "tailwindcss";
@plugin "daisyui";

@utility kartu-dasar {
  border-radius: 0.75rem;
  padding: 1rem;
  background: white;
}""",
            },
            {
                "body": [
                    "@utility mendaftarkan kelas buatanmu sebagai utility sungguhan, jadi ia",
                    "ikut bisa diberi varian seperti md:kartu-dasar. @plugin memuat plugin",
                    "dari paket npm.",
                    "",
                    "daisyUI adalah plugin Tailwind yang paling dikenal (versi 5.7 saat",
                    "materi ini ditulis). Ia menambah kelas komponen seperti btn, card, dan",
                    "modal, plus tema warna siap pakai. Jadi kamu bisa menulis <button",
                    "class=\"btn btn-primary\"> alih-alih sepuluh kelas utility. Cocok untuk",
                    "prototipe dan aplikasi internal; kalau desainnya khas sekali, kelas",
                    "utility biasa lebih leluasa.",
                    "",
                    "UnoCSS adalah alternatif Tailwind, mesin CSS atomik yang aturannya",
                    "diatur lewat preset. Salah satu presetnya meniru kelas Tailwind, jadi",
                    "kodenya terasa familier. Ia dipakai sekitar 3% responden State of CSS",
                    "2025 dan dipilih orang yang ingin mengatur sendiri setiap aturan kelas.",
                ],
            },
            {
                "heading": "Dari v3 ke v4",
                "bahasa": "teks",
                "code": """Urusan             Tailwind v3                     Tailwind v4
Konfigurasi        tailwind.config.js              @theme di CSS
Memuat             @tailwind base/components/...   @import "tailwindcss"
Mencari kelas      daftar content wajib diisi      otomatis, tambah @source
Plugin             plugins: [...] di config        @plugin "nama" di CSS
Mode gelap kelas   darkMode: 'class'               @custom-variant dark
Container query    plugin terpisah                 bawaan (@container, @md:)
Browser minimal    lebih lama                      Safari 16.4, Chrome 111,
                                                   Firefox 128""",
            },
            {
                "body": [
                    "Proyek versi 3 bisa dipindah dengan alat resmi: npx",
                    "@tailwindcss/upgrade. Jalankan di cabang git terpisah dan periksa",
                    "hasilnya, karena beberapa nama kelas ikut berubah.",
                    "",
                    "Baris terakhir tabel penting kalau penggunamu memakai ponsel atau",
                    "browser lama. Versi 4 mengandalkan fitur CSS modern, jadi untuk browser",
                    "yang lebih tua dari daftar itu, tim Tailwind menyarankan tetap di versi",
                    "3.4.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Banyak proyek yang dimulai sebelum 2025 masih memakai Tailwind versi 3,",
                    "dan pelajar PKL sering diminta memindahkannya ke versi 4 sekalian",
                    "memperbarui Vite atau Next.js.",
                    "",
                    "Kasus kecil: kamu mengikuti tutorial video, membuat tailwind.config.js",
                    "dengan warna merek, tapi kelas bg-merek-500 nggak menghasilkan apa-apa",
                    "di proyek yang baru kamu buat.",
                    "",
                    "Cara memecahkannya:",
                    "1. Cek versi di package.json. Kalau tailwindcss sudah 4.x,",
                    "   tailwind.config.js nggak dibaca secara bawaan.",
                    "2. Pindahkan warnanya ke CSS utama, di dalam @theme, sebagai",
                    "   --color-merek-500.",
                    "3. Pastikan baris paling atas CSS-nya @import \"tailwindcss\", bukan tiga",
                    "   baris @tailwind dari versi 3.",
                    "4. Jalankan ulang npm run dev, lalu periksa di DevTools bahwa kelas",
                    "   bg-merek-500 punya aturan CSS.",
                ],
            },
        ],
    },
    {
        "title": "14. Sass, PostCSS, dan Pipeline CSS",
        "sections": [
            {
                "body": [
                    "CSS yang kamu tulis jarang sama dengan CSS yang sampai ke browser. Di",
                    "antara keduanya ada pipeline, yaitu deretan alat yang mengolah CSS satu",
                    "per satu, seperti ban berjalan di pabrik:",
                    "",
                    "1. Preprocessor seperti Sass mengubah sintaks tambahan (variabel, mixin,",
                    "   perulangan) jadi CSS biasa.",
                    "2. Linter seperti Stylelint memeriksa kesalahan.",
                    "3. PostCSS dan plugin-nya menambah awalan vendor, mengubah fitur CSS baru",
                    "   jadi CSS yang dipahami browser lama, dan membuang kelas yang nggak",
                    "   dipakai.",
                    "4. Minifier mengecilkan berkas dengan membuang spasi dan komentar.",
                    "",
                    "Kamu jarang menjalankan alat-alat ini sendiri. Vite, Next.js, atau",
                    "Tailwind memanggilnya di belakang layar. Tapi waktu ada yang salah,",
                    "misalnya gaya yang hilang di versi produksi, kamu perlu tahu di tahap",
                    "mana ia hilang.",
                ],
            },
            {
                "heading": "Sass: CSS dengan kemampuan tambahan",
                "bahasa": "scss",
                "code": """$merek: #c2410c;
$merek-gelap: #9a3412;
$warna: (utama: $merek, bahaya: #b91c1c, sukses: #15803d);

@mixin bulat($r: 0.5rem) {
  border-radius: $r;
}

.tombol {
  @include bulat;
  padding: 0.5rem 1rem;
  color: #fff;

  &:hover {
    background: $merek-gelap;
  }
}

@each $nama, $nilai in $warna {
  .tombol-#{$nama} {
    background: $nilai;
  }
}""",
            },
            {
                "body": [
                    "Dikompilasi dengan npx sass gaya.scss, hasilnya CSS biasa:",
                ],
                "bahasa": "css",
                "code": """.tombol {
  border-radius: 0.5rem;
  padding: 0.5rem 1rem;
  color: #fff;
}
.tombol:hover {
  background: #9a3412;
}

.tombol-utama {
  background: #c2410c;
}

.tombol-bahaya {
  background: #b91c1c;
}

.tombol-sukses {
  background: #15803d;
}""",
            },
            {
                "body": [
                    "Sass (Syntactically Awesome Style Sheets) punya dua sintaks. SCSS, yang",
                    "dipakai di atas, adalah CSS ditambah fitur Sass, jadi setiap berkas CSS",
                    "yang sah juga SCSS yang sah. Sintaks lama yang memakai indentasi (berkas",
                    ".sass) masih ada tapi jarang dipakai.",
                    "",
                    "Fitur yang paling sering dipakai: variabel ($merek), nesting (& artinya",
                    "selektor induk), mixin (blok gaya yang bisa dipanggil dengan argumen),",
                    "dan @each untuk menghasilkan banyak kelas dari satu peta. Satu peta tiga",
                    "warna menghasilkan tiga kelas tombol.",
                    "",
                    "Implementasi yang dirawat cuma Dart Sass, paket npm bernama sass, versi",
                    "1.105.2 saat materi ini ditulis. node-sass dan LibSass sudah usang;",
                    "kalau kamu menemukannya di proyek lama, gantilah dengan sass. Aturan",
                    "@import di Sass juga sudah usang dan akan dibuang di Dart Sass 3.0.",
                    "Penggantinya @use dan @forward, yang memberi setiap berkas ruang nama",
                    "sendiri. Di State of CSS 2025, Sass dipakai sekitar 44% responden,",
                    "terbanyak di antara pre/post-processor.",
                ],
            },
            {
                "heading": "CSS sekarang sudah bisa sebagian",
                "body": [
                    "Dua alasan utama orang dulu memakai Sass, yaitu variabel dan nesting,",
                    "sekarang sudah ada di CSS sendiri. Custom properties (--merek) sudah",
                    "lama didukung, dan nesting asli didukung semua browser utama sejak 2023:",
                    "",
                    "  .tombol {",
                    "    color: var(--merek);",
                    "    &:hover { color: var(--merek-gelap); }",
                    "  }",
                    "",
                    "Bedanya, variabel CSS hidup di browser dan bisa berubah saat halaman",
                    "berjalan (misalnya untuk mode gelap), sedangkan variabel Sass hilang",
                    "begitu dikompilasi.",
                    "",
                    "Sass masih layak dipakai kalau kamu butuh mixin, perulangan dan peta,",
                    "fungsi hitung warna saat build, atau kalau proyeknya sudah memakai Sass.",
                    "Kode sumber Bootstrap 5, misalnya, ditulis dengan Sass. Untuk proyek",
                    "baru yang memakai Tailwind, Sass biasanya nggak dibutuhkan lagi.",
                ],
            },
            {
                "heading": "Less dan Stylus",
                "body": [
                    "Less adalah preprocessor yang mirip Sass, dengan variabel yang ditulis",
                    "memakai @, misalnya @merek: #c2410c. Ia populer di era Bootstrap 3 dan",
                    "Ant Design versi lama. Less masih dirawat (versi 4.9.1, lisensi",
                    "Apache-2.0), tapi pemakainya menurun, sekitar 7% di State of CSS 2025.",
                    "Kamu akan menemuinya di kode lama; untuk proyek baru pilih Sass atau CSS",
                    "biasa.",
                    "",
                    "Stylus punya sintaks paling ringkas: tanpa kurung kurawal, titik koma,",
                    "maupun titik dua. Pemakainya tinggal sekitar 1,4%, dan rilisnya sudah",
                    "jarang. Cukup dikenali kalau bertemu berkas .styl.",
                ],
                "bahasa": "less",
                "code": """@merek: #c2410c;

.tombol {
  color: #fff;
  background: @merek;
  &:hover { background: darken(@merek, 10%); }
}""",
            },
            {
                "heading": "PostCSS: CSS jadi pohon, lalu plugin",
                "body": [
                    "PostCSS (versi 8.5) mengurai CSS jadi pohon, lalu menjalankan plugin di",
                    "atas pohon itu. PostCSS sendiri nggak mengubah apa pun; semua pekerjaan",
                    "dilakukan plugin. Di State of CSS 2025 ia dipakai sekitar 28% responden.",
                    "Jumlah proyek yang memakainya jauh lebih besar, karena Vite dan banyak",
                    "framework memanggilnya tanpa kamu sadari.",
                    "",
                    "Plugin yang paling sering kamu temui:",
                    "",
                    "- Autoprefixer menambahkan awalan vendor seperti -webkit- hanya untuk",
                    "  browser yang masih membutuhkannya. Daftar browser target ditulis di",
                    "  field browserslist di package.json, misalnya \"defaults\".",
                    "- postcss-preset-env membuat fitur CSS terbaru bisa dipakai sekarang",
                    "  dengan mengubahnya jadi CSS yang dipahami browser lama.",
                    "- cssnano mengecilkan CSS untuk produksi.",
                    "- PurgeCSS membuang kelas yang nggak muncul di HTML dan JavaScript. Sejak",
                    "  Tailwind cuma membuat kelas yang dipakai, alat ini makin jarang",
                    "  dibutuhkan.",
                ],
                "bahasa": "json",
                "code": """{
  "plugins": {
    "autoprefixer": {},
    "cssnano": { "preset": "default" }
  }
}""",
            },
            {
                "heading": "Lightning CSS",
                "body": [
                    "Lightning CSS dari tim Parcel ditulis dengan Rust dan mengerjakan tiga",
                    "tugas sekaligus: mengurai, mengubah (termasuk menambah awalan vendor",
                    "sesuai browser target), dan mengecilkan CSS. Satu alat ini bisa",
                    "menggantikan PostCSS, Autoprefixer, dan cssnano untuk kebanyakan proyek,",
                    "dan jauh lebih cepat. Tailwind v4 memakainya di dalam, dan Vite bisa",
                    "memakainya lewat pilihan css.transformer: 'lightningcss'. Versinya 1.33,",
                    "lisensi MPL-2.0.",
                ],
            },
            {
                "heading": "Pipeline mini",
                "body": [
                    "Semua alat tadi bisa dipandang sebagai fungsi: menerima CSS,",
                    "mengembalikan CSS baru. Program ini merangkai tiga \"plugin\" buatan",
                    "sendiri dengan reduce, sama seperti PostCSS menjalankan plugin satu demi",
                    "satu.",
                ],
                "code": "// Pipeline CSS mini: tiap \"plugin\" menerima teks CSS dan mengembalikan teks baru.\nconst css = `\n/* tombol utama */\n.tombol {\n  user-select: none;\n  color: #ffffff;\n  margin: 0px;\n}\n.sisa-lama {\n  color: red;\n}\n`;\n\nconst dipakaiDiHtml = ['tombol']; // hasil memindai HTML\n\nfunction buangYangTakDipakai(teks) {\n  return teks.replace(/\\.([\\w-]+)\\s*\\{[^}]*\\}/g, (aturan, nama) =>\n    (dipakaiDiHtml.includes(nama) ? aturan : ''));\n}\n\nfunction tambahPrefix(teks) {\n  return teks.replace(/(\\s*)user-select:([^;]+);/g,\n    '$1-webkit-user-select:$2;$1user-select:$2;');\n}\n\nfunction kecilkan(teks) {\n  return teks\n    .replace(/\\/\\*[\\s\\S]*?\\*\\//g, '')   // buang komentar\n    .replace(/#ffffff/gi, '#fff')       // warna versi pendek\n    .replace(/\\b0px\\b/g, '0')           // 0px sama dengan 0\n    .replace(/\\s+/g, ' ')\n    .replace(/\\s*([{};:])\\s*/g, '$1')\n    .replace(/;}/g, '}')\n    .trim();\n}\n\nconst pipeline = [buangYangTakDipakai, tambahPrefix, kecilkan];\nconst hasil = pipeline.reduce((teks, plugin) => plugin(teks), css);\nconsole.log(hasil);\nconsole.log(`${css.length} karakter jadi ${hasil.length} karakter`);",
            },
            {
                "body": [
                    "Keluaran:",
                    "  .tombol{-webkit-user-select:none;user-select:none;color:#fff;margin:0}",
                    "  115 karakter jadi 70 karakter",
                    "",
                    "Urutannya berpengaruh. Kalau kecilkan dijalankan lebih dulu, pola di",
                    "buangYangTakDipakai harus menghadapi CSS tanpa spasi. Alat sungguhan",
                    "bekerja pada pohon hasil urai. Pola teks sederhana seperti di atas cuma",
                    "meniru idenya.",
                ],
            },
            {
                "heading": "Stylelint",
                "body": [
                    "Stylelint adalah linter khusus CSS dan SCSS: ia menandai properti salah",
                    "ketik, warna hex yang nggak sah, selektor yang tertulis dua kali, dan",
                    "aturan gaya tim. Versinya 17.16, dipakai sekitar 24% responden State of",
                    "CSS 2025. Mulai dengan konfigurasi standar, lalu jalankan di folder",
                    "sumber.",
                ],
                "bahasa": "terminal",
                "code": "npm install -D stylelint stylelint-config-standard\necho '{ \"extends\": [\"stylelint-config-standard\"] }' > .stylelintrc.json\nnpx stylelint \"src/**/*.css\"",
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Proyek lama berbasis Bootstrap 4 atau 5 biasanya punya folder scss",
                    "berisi puluhan berkas yang dikompilasi jadi satu CSS. Pelajar PKL sering",
                    "diminta mengganti warna merek di sana, atau memperbaiki build yang rusak",
                    "setelah Node diperbarui.",
                    "",
                    "Kasus kecil: proyek lama gagal di-install dengan pesan error panjang",
                    "dari node-gyp saat memasang node-sass, sesudah kamu memakai Node 24.",
                    "",
                    "Cara memecahkannya:",
                    "1. Kenali penyebabnya: node-sass adalah pembungkus LibSass yang sudah",
                    "   usang dan butuh dikompilasi ulang untuk setiap versi Node, jadi Node",
                    "   baru sering nggak didukung.",
                    "2. Ganti paketnya: npm uninstall node-sass, lalu npm install -D sass.",
                    "   Perintah dan sintaks SCSS-nya hampir sama.",
                    "3. Jalankan build dan baca peringatan Dart Sass. Biasanya muncul",
                    "   peringatan @import usang dan pembagian dengan garis miring; catat untuk",
                    "   diperbaiki bertahap.",
                    "4. Ubah @import jadi @use satu berkas demi satu berkas, dan jalankan build",
                    "   setiap kali supaya tahu langkah mana yang merusak.",
                ],
            },
        ],
    },
    {
        "title": "15. Bootstrap, CSS Modules, dan Peta Cara Menata Gaya",
        "sections": [
            {
                "body": [
                    "Tailwind bukan satu-satunya cara menata gaya di proyek frontend. Begitu",
                    "kamu membuka kode orang lain, kamu bisa bertemu kelas Bootstrap seperti",
                    "btn btn-primary, berkas .module.css, gaya yang ditulis di dalam",
                    "JavaScript, atau berkas .css.ts. Semua itu jawaban untuk masalah yang",
                    "sama: CSS bersifat global, jadi aturan di satu tempat bisa mengubah",
                    "tampilan di tempat lain yang nggak kamu duga.",
                    "",
                    "Materi ini memetakan empat keluarga besar, lengkap dengan status tiap",
                    "pemainnya, supaya kamu bisa membaca kode lama dan memilih dengan sadar",
                    "di proyek baru.",
                ],
            },
            {
                "heading": "Peta cara menata gaya",
                "bahasa": "teks",
                "code": """Keluarga             Contoh                         Status umum
Framework CSS        Bootstrap, Bulma, Foundation,  Bootstrap masih kuat; sisanya
berkomponen          Materialize                    menurun
Utility              Tailwind, UnoCSS               paling populer (materi 1-2)
Token siap pakai     Open Props                     aktif, kecil
Scope saat build     CSS Modules                    stabil, didukung semua bundler
CSS-in-JS runtime    styled-components, Emotion,    menurun atau usang
                     Styled JSX, JSS, Styled System
CSS-in-JS            vanilla-extract, Panda CSS,    aktif, pemakai masih sedikit
zero-runtime         StyleX, Linaria, Pigment CSS   (Pigment CSS ditunda)""",
            },
            {
                "heading": "Bootstrap dan framework CSS berkomponen",
                "body": [
                    "Bootstrap adalah framework CSS paling klasik: grid 12 kolom dan komponen",
                    "siap pakai seperti navbar, modal, dan kartu. Versi terbarunya 5.3.8",
                    "(Agustus 2025), lisensi MIT. Sejak versi 5, Bootstrap nggak lagi butuh",
                    "jQuery, dan versi 5.3 punya mode warna gelap lewat atribut",
                    "data-bs-theme. Di State of CSS 2025 ia dipakai sekitar 22% responden,",
                    "nomor dua sesudah Tailwind, dan masih sering disebut di lowongan kerja",
                    "junior.",
                ],
                "bahasa": "html",
                "code": """<div class="container">
  <div class="row">
    <div class="col-md-6">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">Kopi Susu</h5>
          <a href="/beli" class="btn btn-primary">Beli</a>
        </div>
      </div>
    </div>
  </div>
</div>""",
            },
            {
                "body": [
                    "Bedanya dengan Tailwind: Bootstrap memberimu komponen jadi dengan",
                    "tampilan khas Bootstrap. Cepat untuk aplikasi internal dan prototipe,",
                    "tapi situs yang memakainya cenderung mirip satu sama lain kecuali tema",
                    "Sass-nya diubah serius.",
                    "",
                    "Pemain lain di keluarga ini:",
                    "",
                    "- Bulma (1.0.4): CSS murni berbasis flexbox tanpa JavaScript. Versi 1.0",
                    "  memakai variabel CSS. Rilisnya jarang.",
                    "- Foundation (6.9): pesaing utama Bootstrap di era 2012 sampai 2017,",
                    "  buatan perusahaan desain Zurb. Kini rilisnya jarang sekali dan masih ada",
                    "  terutama di kode lama.",
                    "- Materialize: framework bergaya Material Design. Proyek aslinya berhenti",
                    "  di versi 1.0.0 tahun 2018, lalu dilanjutkan komunitas sebagai fork",
                    "  (versi 2.x). Jangan dipilih untuk proyek baru.",
                    "- Open Props (1.7): isinya ratusan variabel CSS siap pakai, tanpa kelas",
                    "  sama sekali, untuk warna, jarak, bayangan, dan animasi. Cocok kalau kamu",
                    "  ingin menulis CSS sendiri dengan skala yang rapi.",
                ],
            },
            {
                "heading": "CSS Modules",
                "body": [
                    "CSS Modules adalah konvensi, bukan pustaka. Berkas yang namanya",
                    "berakhiran .module.css diolah saat build: setiap nama kelas diberi",
                    "akhiran unik, misalnya .utama jadi .Tombol_utama_x7k2p, sehingga nggak",
                    "mungkin bentrok dengan kelas .utama di komponen lain. Vite, Next.js, dan",
                    "webpack mendukungnya tanpa pemasangan tambahan. Di State of CSS 2025,",
                    "CSS Modules dipakai sekitar 19% responden, terbanyak di kategorinya.",
                ],
                "bahasa": "css",
                "code": """/* Tombol.module.css */
.utama {
  padding: 0.5rem 1rem;
  background: #c2410c;
  color: #fff;
}""",
            },
            {
                "bahasa": "jsx",
                "code": """import gaya from './Tombol.module.css';

export function Tombol({ children }) {
  return <button className={gaya.utama}>{children}</button>;
}""",
            },
            {
                "heading": "CSS-in-JS runtime",
                "body": [
                    "CSS-in-JS menulis gaya di dalam berkas JavaScript. Versi runtime membuat",
                    "CSS-nya saat aplikasi berjalan di browser, setiap kali komponen",
                    "dirender.",
                ],
                "bahasa": "jsx",
                "code": """import styled from 'styled-components';

const Tombol = styled.button`
  padding: 0.5rem 1rem;
  background: ${(props) => (props.$bahaya ? '#b91c1c' : '#c2410c')};
  color: #fff;
`;

// dipakai: <Tombol $bahaya>Hapus</Tombol>""",
            },
            {
                "body": [
                    "Cara ini pernah populer sekali di proyek React, tapi sekarang",
                    "ditinggalkan karena dua alasan. Pertama, ada biaya: gaya dihitung di",
                    "browser selama render, jadi halaman lebih berat. Kedua, ia nggak cocok",
                    "dengan React Server Components, yang dibahas di bab 6, karena butuh kode",
                    "yang jalan di browser.",
                    "",
                    "- styled-components (6.6): pengelolanya mengumumkan mode perawatan pada",
                    "  Maret 2025 dan nggak menyarankannya untuk proyek baru, walau perbaikan",
                    "  masih dirilis. Dipakai sekitar 16% responden State of CSS 2025,",
                    "  kebanyakan di proyek yang sudah ada.",
                    "- Emotion (11.14): mesin gaya bawaan Material UI, belum ada rilis sejak",
                    "  Desember 2024.",
                    "- Styled JSX (5.1): gaya ber-scope lewat tag <style jsx>, buatan Vercel",
                    "  untuk Next.js, kini cuma dirawat.",
                    "- JSS (10.10): mesin gaya Material UI versi 4, nggak ada rilis sejak",
                    "  2023. Usang.",
                    "- Styled System (5.1.5): kumpulan props gaya berbasis tema, nggak ada",
                    "  rilis sejak 2020. Usang.",
                    "",
                    "Semuanya masih ada di kode lama; jangan dipilih untuk proyek baru.",
                ],
            },
            {
                "heading": "CSS-in-JS zero-runtime",
                "body": [
                    "Keluarga terbaru mempertahankan enaknya menulis gaya di dalam JavaScript",
                    "atau TypeScript, tapi gayanya diekstrak jadi berkas CSS statis saat",
                    "build. Di browser, yang tersisa cuma CSS biasa.",
                ],
                "bahasa": "typescript",
                "code": """// tombol.css.ts (vanilla-extract)
import { style } from '@vanilla-extract/css';

export const tombol = style({
  padding: '0.5rem 1rem',
  background: '#c2410c',
  ':hover': { background: '#9a3412' },
});""",
            },
            {
                "body": [
                    "- vanilla-extract (1.21): gaya ditulis di berkas .css.ts, dengan",
                    "  pemeriksaan tipe TypeScript.",
                    "- Panda CSS (2.2): dari tim Chakra UI, dengan token desain dan pemeriksaan",
                    "  tipe.",
                    "- StyleX (0.19): buatan Meta, mengompilasi gaya jadi CSS atomik. Menurut",
                    "  Meta dipakai di Facebook dan Instagram. Masih versi 0.x.",
                    "- Linaria (8.2): sintaksnya mirip styled-components, hasilnya CSS statis.",
                    "  Pemakainya sedikit sekali.",
                    "- Pigment CSS (0.0.31): dari tim Material UI sebagai calon pengganti",
                    "  Emotion, tapi README-nya menyatakan proyek ini alpha dan ditunda.",
                    "",
                    "Semua pemain zero-runtime masih kecil, masing-masing di bawah 2%",
                    "responden State of CSS 2025. Arahnya jelas, tapi belum ada pemenang.",
                ],
            },
            {
                "heading": "Memilih untuk proyek baru",
                "body": [
                    "- Situs atau aplikasi dengan desain sendiri: Tailwind, atau CSS biasa",
                    "  dengan variabel dan nesting asli.",
                    "- Aplikasi internal atau prototipe yang harus cepat jadi: Bootstrap, atau",
                    "  Tailwind dengan daisyUI.",
                    "- Komponen React atau Vue yang ingin gayanya terkurung tanpa belajar",
                    "  sintaks baru: CSS Modules.",
                    "- Tim yang sudah terbiasa mengandalkan TypeScript dan ingin gaya bertipe:",
                    "  vanilla-extract atau Panda CSS.",
                    "- CSS-in-JS runtime: cuma kalau melanjutkan proyek yang sudah memakainya.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Sistem informasi sekolah, aplikasi kepegawaian, dan panel admin yang",
                    "dibuat beberapa tahun lalu sering sekali memakai Bootstrap. Aplikasi",
                    "React dari era 2018 sampai 2022 banyak yang memakai styled-components,",
                    "atau Material UI dengan Emotion.",
                    "",
                    "Kasus kecil: kamu diminta menambah halaman baru ke aplikasi Next.js yang",
                    "memakai styled-components. Halaman itu ingin dibuat sebagai Server",
                    "Component, tapi muncul error karena styled-components butuh kode",
                    "browser.",
                    "",
                    "Cara memecahkannya:",
                    "1. Jangan memaksa styled-components masuk ke Server Component. Tandai",
                    "   komponen yang memakainya dengan 'use client' kalau memang harus.",
                    "2. Untuk halaman baru, pakai CSS Modules: buat Halaman.module.css dan",
                    "   impor kelasnya. Ini jalan di Server Component tanpa konfigurasi",
                    "   tambahan.",
                    "3. Biarkan komponen lama tetap memakai styled-components dulu, dan catat",
                    "   rencana migrasi bertahap ke CSS Modules atau Tailwind.",
                    "4. Periksa tampilan halaman di mode produksi (npm run build lalu npm",
                    "   start), karena urutan pemuatan CSS bisa beda dengan mode pengembangan.",
                ],
            },
        ],
    },
    {
        "title": "16. Bundler dari Nol: Graf Modul dan Tree-Shaking",
        "sections": [
            {
                "body": [
                    "Coba ingat halaman web pertamamu di kurikulum JavaScript. Kodenya",
                    "cuma satu berkas, dipasang lewat satu tag script. Aplikasi",
                    "sungguhan nggak begitu. Toko online kecil aja bisa punya ratusan",
                    "berkas sendiri, ditambah ribuan berkas dari paket npm.",
                    "",
                    "Dulu orang menulis puluhan tag script berurutan. Kalau urutannya",
                    "tertukar, satu fungsi dipanggil sebelum didefinisikan dan halaman",
                    "rusak. Tiap tag juga berarti satu permintaan ke server, jadi halaman",
                    "lambat dibuka.",
                    "",
                    "Bundler adalah program yang membereskan itu. Ia membaca berkas",
                    "pertama (namanya entry, titik masuk), mengikuti semua import di",
                    "dalamnya, lalu menggabungkan semuanya jadi satu atau beberapa",
                    "berkas siap kirim. Berkas hasilnya disebut bundel.",
                ],
            },
            {
                "heading": "Graf modul",
                "body": [
                    "Tiap berkas JavaScript yang punya import atau export disebut modul.",
                    "Kalau main.js meng-import uang.js, ada garis dari main.js ke",
                    "uang.js. Kumpulan semua garis itu disebut graf modul. Bundler",
                    "selalu mulai dari entry, lalu menelusuri garisnya sampai habis.",
                    "",
                    "Ada dua cara menulis modul di JavaScript, dan dua-duanya masih",
                    "kamu temui (lihat materi JavaScript bab 7):",
                    "",
                    "  - ES Module (ESM): import dan export. Ini standar resmi bahasa,",
                    "    dipakai browser dan hampir semua proyek frontend baru.",
                    "  - CommonJS (CJS): require() dan module.exports. Ini cara lama",
                    "    Node.js, masih banyak di paket npm yang umurnya sudah tua.",
                    "",
                    "Bedanya penting buat bundler. Import di ESM ditulis di tingkat atas",
                    "berkas dan nama berkasnya berupa teks tetap. Bundler bisa tahu apa",
                    "yang dipakai tanpa menjalankan kodenya. require() itu panggilan",
                    "fungsi biasa, jadi boleh muncul di dalam if atau memakai nama yang",
                    "dirakit saat program jalan. Bundler harus menebak.",
                ],
            },
            {
                "heading": "ESM dan CommonJS berdampingan",
                "code": """// uang.js versi ES Module
export function formatRupiah(n) { return 'Rp' + n; }

// main.js versi ES Module: bisa dibaca tanpa dijalankan
import { formatRupiah } from './uang.js';

// main.js versi CommonJS: require boleh di mana saja
const uang = require('./uang.js');
if (pakaiDolar) {
  const dolar = require('./dolar-' + negara + '.js');
}
...""",
            },
            {
                "heading": "Tree-shaking dari dekat",
                "body": [
                    "Tree-shaking artinya membuang kode yang di-export tapi nggak",
                    "pernah di-import siapa pun. Namanya dari gambaran mengguncang",
                    "pohon supaya daun yang kering rontok. Rollup yang mempopulerkan",
                    "istilah ini, dan sekarang hampir semua bundler melakukannya.",
                    "",
                    "Program di bawah meniru langkah pertamanya. Empat berkas disimpan",
                    "sebagai teks. Program menelusuri import dari main.js, mencatat",
                    "nama yang dipakai, lalu melaporkan apa yang bisa dibuang.",
                ],
            },
            {
                "heading": "Tree-shaking mini",
                "code": "// Empat \"berkas\" ES Module, disimpan sebagai teks biasa.\nconst berkas = {\n  'main.js': [\n    \"import { formatRupiah } from './uang.js';\",\n    \"import { sapa } from './teks.js';\",\n    \"console.log(sapa('Dina'), formatRupiah(15000));\",\n  ].join('\\n'),\n  'uang.js': [\n    \"export function formatRupiah(n) { return 'Rp' + n; }\",\n    \"export function formatDolar(n) { return '$' + n; }\",\n  ].join('\\n'),\n  'teks.js': [\n    \"export function sapa(nama) { return 'Halo ' + nama; }\",\n    \"export function teriak(nama) { return nama.toUpperCase(); }\",\n  ].join('\\n'),\n  'lama.js': \"export function tidakDipakai() {}\",\n};\n\nconst POLA_IMPORT = /import \\{([^}]+)\\} from '\\.\\/([^']+)'/g;\nconst POLA_EKSPOR = /export function (\\w+)/g;\n\nconst graf = {};\nconst dipakai = {};\n\nfunction kunjungi(nama) {\n  if (graf[nama]) return;\n  graf[nama] = [];\n  for (const [, daftar, tujuan] of berkas[nama].matchAll(POLA_IMPORT)) {\n    graf[nama].push(tujuan);\n    dipakai[tujuan] = dipakai[tujuan] || new Set();\n    for (const n of daftar.split(',')) dipakai[tujuan].add(n.trim());\n    kunjungi(tujuan);\n  }\n}\n\nkunjungi('main.js');\n\nconsole.log('Graf modul dari main.js:');\nfor (const [nama, anak] of Object.entries(graf)) {\n  console.log(`  ${nama} -> ${anak.join(', ') || '(tidak ada)'}`);\n}\nconsole.log('Dibuang tree-shaking:');\nfor (const nama of Object.keys(berkas)) {\n  if (!graf[nama]) {\n    console.log(`  ${nama}: seluruh modul (nggak pernah di-import)`);\n    continue;\n  }\n  for (const [, ekspor] of berkas[nama].matchAll(POLA_EKSPOR)) {\n    if (dipakai[nama] && !dipakai[nama].has(ekspor)) {\n      console.log(`  ${nama}: ${ekspor}`);\n    }\n  }\n}",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  Graf modul dari main.js:",
                    "    main.js -> uang.js, teks.js",
                    "    uang.js -> (tidak ada)",
                    "    teks.js -> (tidak ada)",
                    "  Dibuang tree-shaking:",
                    "    uang.js: formatDolar",
                    "    teks.js: teriak",
                    "    lama.js: seluruh modul (nggak pernah di-import)",
                    "",
                    "Bundler sungguhan nggak memakai regex. Ia mengurai kode jadi pohon",
                    "sintaks, yaitu struktur data yang mewakili tiap pernyataan, lalu",
                    "bekerja di atas pohon itu. Tapi idenya sama: mulai dari entry, ikuti",
                    "import, tandai yang dipakai, buang sisanya. Sesudah itu baru",
                    "langkah transform (misalnya membuang tipe TypeScript dan mengubah",
                    "JSX) dan minify, yaitu memendekkan nama variabel serta membuang",
                    "spasi supaya berkasnya kecil.",
                ],
            },
            {
                "heading": "Code splitting",
                "body": [
                    "Satu bundel raksasa juga punya masalah. Pengunjung halaman depan",
                    "ikut mengunduh kode halaman admin yang nggak pernah ia buka. Code",
                    "splitting memecah bundel jadi beberapa potongan (chunk) yang",
                    "diunduh saat dibutuhkan.",
                    "",
                    "Pemicunya import() berbentuk fungsi, yang mengembalikan Promise.",
                    "Begitu bundler melihat import('./admin.js'), berkas admin dan semua",
                    "yang ia import dipisah ke chunk sendiri. Router React, Vue, dan",
                    "Angular memakai cara ini untuk lazy loading per halaman.",
                    "",
                    "  tombolAdmin.onclick = async () => {",
                    "    const { bukaPanel } = await import('./admin.js');",
                    "    bukaPanel();",
                    "  };",
                ],
            },
            {
                "heading": "Rollup, pelopor tree-shaking",
                "body": [
                    "Rollup lahir untuk membundel pustaka npm. Dialah yang membuat ES",
                    "Module dan tree-shaking jadi kebiasaan umum. Versi terbarunya saat",
                    "materi ini ditulis (Oktober 2026) adalah 4.64.10, berlisensi MIT.",
                    "",
                    "Vite sampai versi 7 memakai Rollup untuk build produksi. Di Vite 8",
                    "perannya diambil Rolldown, bundler Rust yang sengaja dibuat dengan",
                    "API yang sama. Jadi API plugin Rollup tetap hidup: plugin yang",
                    "ditulis untuk Rollup umumnya jalan di Vite dan Rolldown juga.",
                    "",
                    "Jebakan: tree-shaking cuma berani membuang kode yang ia yakin tanpa",
                    "efek samping. Berkas yang mengubah variabel global saat di-import",
                    "(misalnya polyfill) tetap disimpan. Paket npm memberi tahu bundler",
                    "lewat medan \"sideEffects\": false di package.json-nya.",
                    "",
                    "Jebakan: paket yang cuma tersedia sebagai CommonJS hampir nggak bisa",
                    "di-tree-shake. Contoh terkenal: lodash. Versi ESM-nya, lodash-es,",
                    "bisa dipangkas sampai ke fungsi yang kamu pakai saja.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Toko online yang dibangun dengan React atau Vue hampir selalu",
                    "dikirim sebagai bundel hasil Vite atau webpack. Ukuran bundel",
                    "langsung terasa di ponsel murah dengan sinyal pas-pasan: makin",
                    "besar berkasnya, makin lama halaman kosong sebelum tombol bisa",
                    "diklik.",
                    "",
                    "Kasus kecil: halaman toko temanmu menghasilkan bundel 900 KB, padahal",
                    "kodenya sendiri sedikit. Ternyata ada satu baris",
                    "import _ from 'lodash' yang cuma dipakai untuk _.debounce.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Jalankan npm run build. Vite mencetak ukuran tiap chunk, jadi",
                    "     chunk yang membengkak langsung kelihatan.",
                    "  2. Cari import yang menarik seluruh paket. Untuk lodash, ganti",
                    "     dengan versi ESM:",
                    "       import { debounce } from 'lodash-es';",
                    "  3. Kalau fungsinya sederhana, tulis sendiri atau pakai fitur",
                    "     bawaan browser, lalu hapus paketnya dari dependencies.",
                    "  4. Pindahkan halaman yang jarang dibuka ke import() supaya masuk",
                    "     chunk sendiri.",
                    "  5. Build lagi dan bandingkan angkanya dengan sebelum diubah.",
                ],
            },
        ],
    },
    {
        "title": "17. Vite 8 dan Rolldown",
        "sections": [
            {
                "body": [
                    "Vite (dibaca \"vit\", dari bahasa Prancis yang artinya cepat) adalah",
                    "alat kerja frontend yang mengerjakan dua hal. Pertama, server",
                    "pengembangan (dev server) yang menampilkan perubahan kodemu",
                    "seketika di browser. Kedua, build produksi yang menghasilkan bundel",
                    "kecil untuk diunggah ke hosting.",
                    "",
                    "Vite sekarang jadi pilihan bawaan untuk proyek frontend baru. Di",
                    "Survei Stack Overflow 2025 ia dipakai 25,4% responden. Di State of",
                    "JS 2025 ia dipakai 84,4% penjawab, hampir menyusul webpack (86,4%),",
                    "dan kepuasannya paling tinggi di kategori build tool. Nuxt,",
                    "SvelteKit, Astro, dan Vitest semuanya dibangun di atas Vite.",
                ],
            },
            {
                "heading": "Membuat proyek pertama",
                "bahasa": "terminal",
                "code": """npm create vite@latest toko-saya -- --template react-ts
cd toko-saya
npm install
npm run dev""",
            },
            {
                "body": [
                    "Baris pertama menjalankan paket create-vite. Bagian --template",
                    "memilih kerangka: vanilla, vanilla-ts, react, react-ts, vue,",
                    "vue-ts, svelte, svelte-ts, preact, lit, solid, dan beberapa lagi.",
                    "Akhiran -ts berarti TypeScript. Kalau --template nggak ditulis,",
                    "create-vite menanyakannya satu per satu.",
                    "",
                    "Sesudah npm run dev, terminal menampilkan alamat seperti",
                    "http://localhost:5173. Buka di browser. Ubah teks di src/App.tsx",
                    "lalu simpan, dan halaman berubah tanpa kamu menekan reload.",
                    "Fitur ini namanya HMR (Hot Module Replacement): cuma modul yang",
                    "berubah yang ditukar, jadi isi formulir yang sudah kamu ketik",
                    "nggak hilang.",
                ],
            },
            {
                "heading": "Isi foldernya",
                "bahasa": "teks",
                "code": """toko-saya/
  index.html          <- titik masuk, ada di akar proyek
  package.json        <- skrip dev, build, preview
  vite.config.ts      <- konfigurasi Vite
  tsconfig.json
  public/             <- disalin apa adanya (favicon, robots.txt)
  src/
    main.tsx          <- di-import index.html lewat tag script
    App.tsx
  node_modules/       <- jangan di-commit""",
            },
            {
                "heading": "Dev server nggak membundel",
                "body": [
                    "Ini bedanya Vite dengan webpack generasi lama. Webpack membundel",
                    "seluruh aplikasi dulu sebelum dev server siap. Di proyek besar,",
                    "menunggunya bisa semenit.",
                    "",
                    "Vite memanfaatkan fakta bahwa browser modern sudah paham ES Module.",
                    "Saat browser meminta /src/main.tsx, Vite mengubah berkas itu saja",
                    "jadi JavaScript biasa (membuang tipe, mengubah JSX) lalu mengirimnya.",
                    "Browser membaca import di dalamnya dan meminta berkas berikutnya.",
                    "Berkas yang nggak dibuka di halaman itu nggak pernah diproses.",
                    "",
                    "Paket di node_modules diperlakukan beda. Paket seperti react punya",
                    "puluhan berkas kecil, jadi Vite menggabungkannya dulu sekali di",
                    "awal (pre-bundling) dan menyimpannya di cache.",
                ],
            },
            {
                "heading": "Build produksi",
                "body": [
                    "Untuk diunggah, kamu butuh bundel sungguhan. Jalankan npm run build.",
                    "Hasilnya masuk folder dist/: index.html, lalu berkas JavaScript dan",
                    "CSS yang sudah di-tree-shake, di-minify, dan namanya diberi hash",
                    "seperti index-B4x9kQ2a.js. Hash itu berubah tiap isinya berubah,",
                    "jadi browser pengunjung nggak terjebak memakai versi lama dari",
                    "cache.",
                    "",
                    "Sebelum mengunggah, cek dulu dengan npm run preview. Perintah itu",
                    "menyajikan isi dist/ persis seperti di hosting. Bug yang cuma muncul",
                    "di build produksi (misalnya jalur gambar yang salah) ketahuan di",
                    "sini.",
                ],
            },
            {
                "heading": "Variabel lingkungan VITE_",
                "body": [
                    "Alamat API biasanya beda antara laptopmu dan server produksi. Vite",
                    "membaca berkas .env di akar proyek, lalu memasukkan nilainya lewat",
                    "import.meta.env. Aturannya: cuma variabel yang namanya diawali",
                    "VITE_ yang ikut ke kode klien. Program di bawah meniru apa yang",
                    "Vite lakukan pada teks kodemu saat build.",
                ],
            },
            {
                "heading": "Penggantian import.meta.env",
                "code": "// Isi berkas .env di folder proyek.\nconst env = {\n  VITE_JUDUL: 'Tokoku',\n  VITE_API_URL: 'https://api.tokoku.id',\n  DB_PASSWORD: 'rahasia123',\n};\n\n// Kode klien yang kamu tulis di src/main.js.\nconst sumber = [\n  'document.title = import.meta.env.VITE_JUDUL;',\n  'const api = import.meta.env.VITE_API_URL;',\n  'const sandi = import.meta.env.DB_PASSWORD;',\n].join('\\n');\n\n// Saat build, Vite mengganti teksnya. Cuma yang berawalan VITE_ yang diisi.\nconst hasil = sumber.replace(/import\\.meta\\.env\\.(\\w+)/g, (_, nama) => {\n  if (nama.startsWith('VITE_') && nama in env) return JSON.stringify(env[nama]);\n  return 'undefined';\n});\n\nconsole.log(hasil);",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  document.title = \"Tokoku\";",
                    "  const api = \"https://api.tokoku.id\";",
                    "  const sandi = undefined;",
                    "",
                    "Nilainya ditulis langsung ke dalam bundel. Artinya siapa pun yang",
                    "membuka DevTools bisa membacanya. Awalan VITE_ adalah pagar supaya",
                    "sandi database nggak ikut terkirim karena salah ketik. Rahasia",
                    "sungguhan (kunci API berbayar, sandi) tempatnya di server, nggak",
                    "pernah di kode frontend, apa pun awalannya.",
                ],
            },
            {
                "heading": "Apa yang berubah di Vite 8",
                "body": [
                    "Vite 8 rilis 12 Maret 2026. Versi stabil terbaru saat materi ini",
                    "ditulis (Oktober 2026) adalah 8.3.4. Perubahan terbesarnya ada di",
                    "dalam. Sampai Vite 7, ada dua mesin: esbuild untuk dev server dan",
                    "Rollup untuk build. Keduanya kadang menghasilkan perilaku yang",
                    "sedikit beda, jadi ada bug yang cuma muncul di produksi.",
                    "",
                    "Vite 8 memakai Rolldown sebagai satu-satunya bundler. Rolldown",
                    "ditulis dengan Rust oleh tim Vite (perusahaannya bernama VoidZero),",
                    "API-nya meniru Rollup, dan ia memakai Oxc untuk mengurai serta",
                    "mengubah kode. Pengumuman resminya menyebut build bisa 10 sampai 30",
                    "kali lebih cepat. Versi Rolldown terbaru saat ini 1.2.14.",
                    "",
                    "Buat kamu yang baru mulai, hampir nggak ada yang perlu dipelajari",
                    "ulang. Syarat Node.js-nya sama dengan Vite 7, yaitu 20.19 ke atas",
                    "atau 22.12 ke atas. Konfigurasi lama yang menyebut esbuild atau",
                    "rollupOptions diterjemahkan otomatis ke padanan Rolldown dan Oxc.",
                    "Plugin React versi 6 juga berhenti memakai Babel dan pindah ke Oxc,",
                    "jadi node_modules-nya lebih kecil.",
                    "",
                    "Jebakan: banyak tutorial 2024-2025 masih bilang \"Vite memakai",
                    "esbuild saat dev dan Rollup saat build\". Itu benar untuk Vite 7 ke",
                    "bawah. Untuk proyek baru, anggap semuanya Rolldown.",
                ],
            },
            {
                "heading": "vite.config.ts",
                "bahasa": "typescript",
                "code": """import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  server: { port: 3000 },
  build: { outDir: 'dist' },
});""",
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Dasbor admin sekolah, panel toko, dan aplikasi internal kantor yang",
                    "dibuat dua tahun terakhir kebanyakan dimulai dengan npm create vite.",
                    "Hasil build-nya cuma berkas statis, jadi bisa diunggah ke GitHub",
                    "Pages, Netlify, atau server Nginx biasa.",
                    "",
                    "Kasus kecil: kamu mengunggah isi dist/ ke",
                    "username.github.io/toko-saya/. Halamannya putih kosong, dan Console",
                    "menulis 404 untuk /assets/index-B4x9kQ2a.js.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Perhatikan alamatnya. Vite menganggap aplikasimu di akar domain",
                    "     (/), padahal di GitHub Pages ia ada di /toko-saya/.",
                    "  2. Tambahkan base di vite.config.ts:",
                    "       export default defineConfig({ base: '/toko-saya/' });",
                    "  3. Jalankan npm run build lagi. Buka dist/index.html dan pastikan",
                    "     tag script sekarang menunjuk /toko-saya/assets/....",
                    "  4. Cek dengan npm run preview, baru unggah ulang.",
                ],
            },
        ],
    },
    {
        "title": "18. Peta Build Tool: webpack sampai Turbopack",
        "sections": [
            {
                "body": [
                    "Begitu kamu membuka proyek orang lain, kemungkinan besar alatnya",
                    "bukan Vite. Proyek yang dimulai 2016 sampai 2022 biasanya memakai",
                    "webpack. Proyek Next.js memakai Turbopack. Pustaka npm sering",
                    "dibangun dengan tsup atau tsdown. Materi ini peta supaya kamu bisa",
                    "mengenali semuanya dan tahu mana yang masih layak dipilih.",
                    "",
                    "Alat-alat ini terbagi ke beberapa jenis. Bundler menggabungkan",
                    "modul. Compiler atau transpiler mengubah satu berkas jadi berkas",
                    "lain, misalnya TypeScript ke JavaScript. Pembundel pustaka khusus",
                    "menyiapkan paket npm. Task runner menjalankan daftar langkah. Ada",
                    "juga pembuat proyek yang membungkus semuanya.",
                ],
            },
            {
                "heading": "Ringkasan",
                "bahasa": "teks",
                "code": """Alat              Jenis              Ditulis   Status
webpack           bundler            JS        menurun
Rspack, Rsbuild   bundler            Rust      aktif
esbuild           bundler+compiler   Go        aktif
Parcel            bundler            JS, Rust  stabil-matang
Turbopack         bundler            Rust      aktif (Next.js)
SWC               compiler           Rust      aktif
Babel             compiler           JS        menurun
tsup              pembundel pustaka  TS        menurun
tsdown            pembundel pustaka  TS        aktif
Gulp              task runner        JS        menurun
Grunt             task runner        JS        usang
Browserify        bundler            JS        usang
Create React App  pembuat proyek     JS        usang
Snowpack          build tool         TS        usang""",
            },
            {
                "heading": "Bundler",
                "body": [
                    "webpack adalah bundler paling berpengaruh. Semua jenis berkas (JS,",
                    "CSS, gambar) diolah lewat loader dan plugin. Versi terbarunya",
                    "5.112.0. Di State of JS 2025 ia masih nomor satu soal jumlah",
                    "pemakai (86,4%) tapi kepuasannya rendah, dan di Survei Stack",
                    "Overflow 2025 dipakai 18,4%. Kamu wajib bisa membaca",
                    "webpack.config.js karena proyek warisan banyak, tapi jangan pilih",
                    "untuk proyek baru.",
                    "",
                    "Rspack adalah bundler Rust buatan ByteDance yang meniru API webpack.",
                    "Proyek webpack bisa pindah ke Rspack dengan perubahan kecil dan",
                    "build-nya jadi jauh lebih cepat. Rsbuild adalah alat siap pakai di",
                    "atas Rspack, mirip Vite. Keduanya di versi 2.2 dan situsnya sekarang",
                    "rspack.rs. Tim React menyebut Rsbuild sebagai salah satu pengganti",
                    "Create React App.",
                    "",
                    "esbuild ditulis dengan Go dan terkenal cepat. Ia dipakai",
                    "Vite 7 ke bawah dan Angular CLI. Versinya masih 0.28, tapi sudah",
                    "dipakai 53,8% penjawab State of JS 2025. Ingat sifatnya: esbuild",
                    "cuma membuang anotasi tipe TypeScript, nggak memeriksanya.",
                    "",
                    "Parcel menjanjikan nol konfigurasi: tunjuk index.html, sisanya",
                    "diurus sendiri. Cocok untuk prototipe. Rilisnya melambat (2.16.4,",
                    "Februari 2026). Tim Parcel juga yang membuat Lightning CSS.",
                    "",
                    "Turbopack adalah bundler Rust buatan Vercel, penerus webpack di",
                    "Next.js dan bawaan sejak Next.js 16. Ia nggak punya paket npm",
                    "sendiri; versinya mengikuti Next.js (16.4.2 saat ini). Dipakai 28%",
                    "penjawab State of JS 2025, hampir semuanya lewat Next.js.",
                ],
            },
            {
                "heading": "Compiler",
                "body": [
                    "SWC (Speedy Web Compiler) mengubah TypeScript dan JSX jadi",
                    "JavaScript dengan cepat. Ia ditulis dengan Rust, berlisensi",
                    "Apache-2.0, dan dipakai Next.js, plugin React SWC untuk Vite, Deno,",
                    "serta Parcel. Pemula jarang memanggilnya langsung.",
                    "",
                    "Babel adalah transpiler generasi sebelumnya. Dulu ia wajib supaya",
                    "JavaScript modern jalan di browser lama. Babel 8 sudah stabil",
                    "(8.0.7), tapi alat baru memilih SWC, Oxc, atau esbuild yang jauh",
                    "lebih cepat. Babel masih kamu temui di proyek webpack dan Jest lama,",
                    "dan di plugin transformasi khusus seperti React Compiler versi",
                    "plugin Babel.",
                ],
            },
            {
                "heading": "Pembundel pustaka dan task runner",
                "body": [
                    "tsup membungkus esbuild untuk menerbitkan paket npm berisi ESM,",
                    "CommonJS, dan berkas tipe .d.ts sekaligus. Statusnya membingungkan:",
                    "README-nya bilang nggak dirawat aktif dan menyarankan tsdown, tapi",
                    "versi 9.0.0 terbit 14 Oktober 2026. Untuk pustaka baru, pilih",
                    "tsdown: penerus tsup yang berjalan di atas Rolldown. Versinya masih",
                    "0.23, jadi perubahan besar masih mungkin.",
                    "",
                    "Gulp (5.0.1) adalah task runner berbasis stream: kompilasi Sass,",
                    "kompres gambar, salin berkas, disusun sebagai rangkaian langkah.",
                    "Masih ada di tema WordPress lama. Grunt (1.6.3) adalah generasi",
                    "sebelumnya yang berbasis konfigurasi, dari sekitar 2012-2015. Hari",
                    "ini pekerjaan keduanya diambil alih skrip npm dan bundler.",
                ],
            },
            {
                "heading": "Yang sudah usang",
                "body": [
                    "Browserify adalah bundler pertama yang membawa require() ala Node",
                    "ke browser. Ia digantikan webpack, lalu Vite.",
                    "",
                    "Create React App (perintah npx create-react-app) dulu cara resmi",
                    "memulai proyek React. Tim React menyatakannya usang pada 14 Februari",
                    "2025 dan menyarankan framework seperti Next.js, atau Vite, Parcel,",
                    "dan Rsbuild. Paket react-scripts-nya terakhir rilis April 2022.",
                    "",
                    "Jebakan: tutorial React di YouTube yang diawali npx",
                    "create-react-app sudah ketinggalan. Kodenya mungkin masih berguna,",
                    "tapi cara membuat proyeknya ganti dengan npm create vite.",
                    "",
                    "Snowpack adalah build tool tanpa bundel yang memakai ES Module",
                    "langsung, ide yang lalu disempurnakan Vite. Ia nggak dirawat sejak",
                    "2022, dan timnya beralih membuat Astro.",
                ],
            },
            {
                "heading": "Mengenali alat dari berkasnya",
                "bahasa": "teks",
                "code": """Berkas di akar proyek       Alatnya
vite.config.ts / .js        Vite
webpack.config.js           webpack
rspack.config.js            Rspack
rsbuild.config.ts           Rsbuild
next.config.ts + skrip      Next.js (Turbopack)
.parcelrc atau 'parcel'     Parcel
babel.config.js, .babelrc   Babel
.swcrc                      SWC
tsup.config.ts              tsup
tsdown.config.ts            tsdown
gulpfile.js                 Gulp
Gruntfile.js                Grunt
"react-scripts" di skrip    Create React App""",
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Tim yang merawat aplikasi perusahaan sering mewarisi proyek webpack",
                    "yang build-nya beberapa menit. Rspack lahir persis untuk kasus ini:",
                    "menukar mesinnya tanpa menulis ulang semua konfigurasi.",
                    "",
                    "Kasus kecil: kamu magang dan diberi repositori dengan skrip",
                    "\"start\": \"react-scripts start\". npm install memunculkan banyak",
                    "peringatan deprecated, dan kamu diminta membuatnya jalan dengan",
                    "React terbaru.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Kenali alatnya dari skrip: react-scripts berarti Create React",
                    "     App, yang sudah usang sejak Februari 2025.",
                    "  2. Buat proyek Vite baru di folder terpisah dengan template",
                    "     react atau react-ts.",
                    "  3. Salin folder src/ dan isi public/. Pindahkan public/index.html",
                    "     ke akar proyek dan tambahkan",
                    "       <script type=\"module\" src=\"/src/main.jsx\"></script>",
                    "  4. Ganti process.env.REACT_APP_... dengan import.meta.env.VITE_...",
                    "     dan ubah nama variabelnya di .env.",
                    "  5. Jalankan npm run dev, lalu npm run build. Catat peringatan yang",
                    "     tersisa untuk diperbaiki satu per satu.",
                ],
            },
        ],
    },
    {
        "title": "19. TypeScript di Proyek Frontend",
        "sections": [
            {
                "body": [
                    "Bahasa TypeScript sudah kamu pelajari di kurikulumnya sendiri.",
                    "Materi ini membahas tempatnya di dalam proyek frontend: siapa yang",
                    "memeriksa tipe, siapa yang membuangnya, dan bagaimana mengetik data",
                    "yang datang dari server.",
                    "",
                    "Di Survei Stack Overflow 2025, TypeScript dipakai 43,6% responden.",
                    "Di State of JS 2025, 40% penjawab bilang mereka cuma menulis",
                    "TypeScript. Angular mewajibkannya, dan template React, Vue, serta",
                    "Svelte semuanya punya versi -ts.",
                ],
            },
            {
                "heading": "Dua pekerjaan yang terpisah",
                "body": [
                    "Saat kamu menulis kode .ts atau .tsx, ada dua hal yang harus",
                    "terjadi. Tipe harus diperiksa, dan tipe harus dibuang supaya browser",
                    "menerima JavaScript biasa. Di proyek Vite, dua pekerjaan itu",
                    "dikerjakan alat yang berbeda.",
                    "",
                    "  - Vite (lewat Oxc) cuma membuang tipe. Cepat, karena tiap berkas",
                    "    diproses sendiri tanpa melihat berkas lain.",
                    "  - tsc, compiler resmi TypeScript, memeriksa tipe di seluruh",
                    "    proyek. Ia dijalankan dengan --noEmit, artinya periksa saja,",
                    "    jangan menulis berkas JavaScript.",
                    "",
                    "Akibatnya, dev server tetap jalan walaupun ada error tipe. Editor",
                    "seperti VS Code yang menampilkan garis merahnya. Template react-ts",
                    "dari create-vite menulis skrip build sebagai \"tsc -b && vite",
                    "build\", jadi build produksi gagal kalau tipenya salah.",
                ],
            },
            {
                "heading": "tsconfig.json untuk proyek Vite",
                "bahasa": "json",
                "code": """{
  "compilerOptions": {
    "target": "ES2022",
    "lib": ["ES2022", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "moduleResolution": "bundler",
    "jsx": "react-jsx",
    "strict": true,
    "noEmit": true,
    "isolatedModules": true,
    "verbatimModuleSyntax": true
  },
  "include": ["src"]
}""",
            },
            {
                "body": [
                    "Opsi yang perlu kamu pahami:",
                    "",
                    "  - \"moduleResolution\": \"bundler\" menyuruh tsc mencari berkas",
                    "    dengan aturan yang sama seperti Vite, misalnya import tanpa",
                    "    akhiran .js tetap diterima.",
                    "  - \"noEmit\": true karena yang menulis JavaScript adalah Vite.",
                    "  - \"isolatedModules\": true melarang kode yang cuma bisa",
                    "    diterjemahkan kalau berkas lain ikut dibaca. Ini syarat supaya",
                    "    alat yang memproses berkas satu per satu tetap benar.",
                    "  - \"verbatimModuleSyntax\": true memaksamu menulis import type",
                    "    untuk sesuatu yang cuma tipe, supaya jelas mana import yang",
                    "    hilang saat tipe dibuang.",
                    "  - \"lib\" memuat DOM, jadi tsc kenal document, HTMLElement, dan",
                    "    kawan-kawannya.",
                ],
            },
            {
                "heading": "Mengetik data dari server",
                "code": """type Produk = {
  id: number;
  nama: string;
  harga: number;
  stok?: number;
};

// Type guard: fungsi yang memeriksa saat program jalan, sekaligus
// memberi tahu TypeScript bahwa x boleh dianggap Produk.
function apakahProduk(x: unknown): x is Produk {
  if (typeof x !== "object" || x === null) return false;
  const o = x as Record<string, unknown>;
  return (
    typeof o.id === "number" &&
    typeof o.nama === "string" &&
    typeof o.harga === "number"
  );
}

// Anggap ini balasan server. Isinya baru ketahuan saat program jalan.
const balasan: unknown = JSON.parse(
  '[{"id":1,"nama":"Kopi","harga":18000},{"id":2,"nama":"Teh"}]'
);

const daftar = Array.isArray(balasan) ? balasan : [];
for (const item of daftar) {
  if (apakahProduk(item)) {
    const stok = item.stok ?? 0;
    console.log(`${item.nama}: Rp${item.harga}, stok ${stok}`);
  } else {
    console.log("Ditolak:", JSON.stringify(item));
  }
}""",
                "bahasa": "typescript",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  Kopi: Rp18000, stok 0",
                    "  Ditolak: {\"id\":2,\"nama\":\"Teh\"}",
                    "",
                    "Tipe TypeScript hilang saat program jalan, jadi tipe Produk nggak",
                    "bisa memastikan isi balasan server. Karena itu balasan diberi",
                    "tipe unknown dulu. TypeScript menolak kamu memakai item.nama",
                    "sebelum item lolos pemeriksaan apakahProduk. Teh ditolak karena",
                    "nggak punya harga. Kalau kamu langsung menulis",
                    "JSON.parse(...) as Produk[], error itu baru muncul di layar",
                    "pengguna. Ide yang sama dipakai pustaka Zod di bab 7, yang menulis",
                    "pemeriksaannya untukmu (lihat juga materi TypeScript bab 5).",
                ],
            },
            {
                "heading": "Tipe DOM",
                "bahasa": "typescript",
                "code": """const input = document.querySelector<HTMLInputElement>('#nama');
// input bertipe HTMLInputElement | null

input.value = 'Rina';          // error: 'input' is possibly 'null'

if (input) {
  input.value = 'Rina';        // aman, sudah dicek
}
...""",
            },
            {
                "body": [
                    "querySelector bisa nggak menemukan apa-apa, jadi tsc memaksamu",
                    "mengecek null dulu. Bagian <HTMLInputElement> memberi tahu jenis",
                    "elemennya supaya .value dikenal. Tanpa itu hasilnya Element biasa",
                    "yang nggak punya value.",
                ],
            },
            {
                "heading": "TypeScript 7 dan pesaing lamanya",
                "body": [
                    "TypeScript 7.0 rilis 8 Juli 2026, dan versi terbarunya saat materi",
                    "ini ditulis (Oktober 2026) adalah 7.0.2. Compiler-nya ditulis ulang",
                    "dengan bahasa Go. Tim TypeScript melaporkan build penuh 8 sampai 12",
                    "kali lebih cepat; pemeriksaan proyek VS Code turun dari 125,7 detik",
                    "jadi 10,6 detik. Perintahnya tetap tsc. Di versi 7, strict menyala",
                    "secara bawaan dan opsi yang sudah usang di versi 6 jadi error.",
                    "",
                    "Yang masih tertinggal: versi 7.0 belum punya API",
                    "pemrograman yang stabil (dijanjikan di 7.1). Alat yang memakai",
                    "TypeScript dari dalam, seperti typescript-eslint, perlu waktu untuk",
                    "menyusul. Kalau ada alat yang protes, cek dokumentasinya soal",
                    "dukungan versi 7.",
                    "",
                    "Node.js 22.18 ke atas dan Node 24 juga bisa menjalankan berkas .ts",
                    "langsung dengan membuang tipenya (type stripping). Cocok untuk skrip",
                    "kecil, tapi tetap nggak memeriksa tipe.",
                    "",
                    "Flow adalah pemeriksa tipe buatan Meta yang dulu bersaing dengan",
                    "TypeScript. Ia masih dirilis (0.336.0), tapi di luar Meta komunitas",
                    "hampir seluruhnya pindah ke TypeScript. Kamu mungkin melihat",
                    "komentar // @flow di kode React Native lama.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aplikasi web yang besar, seperti dasbor perbankan, marketplace, dan",
                    "editor online, umumnya ditulis dengan TypeScript karena puluhan",
                    "orang mengubah kode yang sama. Tipe jadi dokumentasi yang dicek",
                    "mesin.",
                    "",
                    "Kasus kecil: halaman daftar produk temanmu tiba-tiba menampilkan",
                    "\"Rp undefined\". Kodenya TypeScript dan dev server nggak protes",
                    "apa-apa. Ternyata server mengganti nama medan harga jadi price.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Cari tempat data diterima. Biasanya ada baris seperti",
                    "       const data = (await res.json()) as Produk[];",
                    "  2. Kata as itu cuma janji ke tsc, tanpa pemeriksaan. Ganti",
                    "     dengan tipe unknown dan type guard (atau skema Zod).",
                    "  3. Tampilkan pesan yang jelas kalau data ditolak, misalnya",
                    "     \"format data dari server berubah\".",
                    "  4. Tambahkan npx tsc --noEmit ke skrip build supaya error tipe",
                    "     lain nggak lolos ke produksi.",
                ],
            },
        ],
    },
    {
        "title": "20. ESLint 10, Prettier, dan Biome",
        "sections": [
            {
                "body": [
                    "Dua alat ini sering disebut bareng, padahal tugasnya beda.",
                    "",
                    "  - Linter membaca kode dan menandai pola yang rawan bug: variabel",
                    "    yang nggak dipakai, perbandingan == yang menipu, hook React yang",
                    "    dipanggil di dalam if. Sebagian temuan bisa diperbaiki otomatis.",
                    "  - Formatter merapikan tampilan kode: indentasi, tanda kutip, titik",
                    "    koma, panjang baris. Ia nggak peduli apakah kodenya benar.",
                    "",
                    "Gampangnya, linter itu guru yang mengecek isi jawabanmu, formatter",
                    "itu yang merapikan tulisan tanganmu. Di tim, keduanya membuat",
                    "review kode fokus ke logika, bukan ke perdebatan spasi.",
                ],
            },
            {
                "heading": "ESLint dan flat config",
                "body": [
                    "ESLint adalah linter paling banyak dipakai; di State of JS 2025 ia",
                    "nomor satu di daftar utilitas (9.697 pemakai). ESLint 10.0.0 rilis 6",
                    "Februari 2026, dan versi terbarunya saat materi ini ditulis",
                    "(Oktober 2026) adalah 10.13.0.",
                    "",
                    "Perubahan terbesar di versi 10: sistem konfigurasi lama (.eslintrc,",
                    ".eslintrc.json, .eslintrc.js) dihapus total. Yang tersisa cuma flat",
                    "config, satu berkas eslint.config.js berisi array objek. ESLint 10",
                    "juga mencari berkas konfigurasi mulai dari folder tiap berkas yang",
                    "diperiksa, jadi monorepo bisa punya konfigurasi per paket. Syaratnya",
                    "Node.js 20.19 ke atas.",
                    "",
                    "Jebakan: tutorial yang menyuruh membuat .eslintrc.json sudah nggak",
                    "berlaku. ESLint 10 akan mengabaikan berkas itu.",
                ],
            },
            {
                "heading": "eslint.config.js",
                "code": """import js from '@eslint/js';
import globals from 'globals';
import { defineConfig } from 'eslint/config';

export default defineConfig([
  js.configs.recommended,
  {
    files: ['src/**/*.{js,jsx}'],
    languageOptions: { globals: globals.browser },
    rules: {
      'no-var': 'error',
      eqeqeq: 'error',
      'no-unused-vars': 'warn',
    },
  },
]);""",
            },
            {
                "body": [
                    "Baca dari atas. js.configs.recommended adalah kumpulan aturan dasar",
                    "yang disarankan tim ESLint. Objek kedua berlaku untuk berkas di",
                    "src/, memberi tahu bahwa kode ini jalan di browser (jadi window dan",
                    "document dikenal), lalu menambah tiga aturan. Tiap aturan punya",
                    "tingkat: \"off\", \"warn\" (kuning, tetap lolos), atau \"error\"",
                    "(merah, perintah gagal).",
                    "",
                    "Pasang dan jalankan:",
                    "",
                    "  npm install --save-dev eslint @eslint/js globals",
                    "  npx eslint .",
                    "  npx eslint . --fix",
                    "",
                    "Plugin menambah aturan khusus: eslint-plugin-react-hooks untuk",
                    "aturan hooks, typescript-eslint untuk TypeScript, dan",
                    "eslint-plugin-jsx-a11y untuk aksesibilitas (bab 2).",
                ],
            },
            {
                "heading": "Kenapa ada aturan eqeqeq",
                "code": """// Tiga perbandingan yang sering bikin bug, dengan == dan ===
console.log("0 == ''        ", 0 == '');
console.log("0 === ''       ", 0 === '');
console.log("'1' == 1       ", '1' == 1);
console.log("'1' === 1      ", '1' === 1);
console.log('null == undefined ', null == undefined);
console.log('null === undefined', null === undefined);""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  0 == ''         true",
                    "  0 === ''        false",
                    "  '1' == 1        true",
                    "  '1' === 1       false",
                    "  null == undefined  true",
                    "  null === undefined false",
                    "",
                    "Operator == mengubah tipe dulu sebelum membandingkan, jadi angka 0",
                    "dianggap sama dengan teks kosong. Di formulir, nilai input selalu",
                    "teks, dan bug seperti ini lolos dari mata. Aturan eqeqeq memaksa",
                    "=== yang membandingkan tipe juga.",
                ],
            },
            {
                "heading": "Prettier",
                "body": [
                    "Prettier adalah formatter yang paling umum. Versinya 3.9.10, dan ia",
                    "nomor dua di daftar utilitas State of JS 2025 (9.295 pemakai) serta",
                    "alat CSS nomor satu di State of CSS 2025. Prettier sengaja punya",
                    "sedikit opsi: lebar baris, kutip tunggal atau ganda, titik koma, dan",
                    "beberapa lagi. Sisanya ia putuskan sendiri, jadi tim nggak perlu",
                    "berdebat.",
                    "",
                    "  npm install --save-dev prettier",
                    "  npx prettier . --write",
                    "",
                    "Pengaturan ditulis di .prettierrc, misalnya",
                    "{ \"singleQuote\": true, \"semi\": true }. Kalau ESLint juga punya",
                    "aturan soal gaya, keduanya bisa saling bertentangan. Paket",
                    "eslint-config-prettier mematikan aturan gaya di ESLint supaya",
                    "urusan tampilan sepenuhnya milik Prettier.",
                ],
            },
            {
                "heading": "Biome dan Oxc",
                "body": [
                    "Biome adalah satu program Rust yang menggabungkan linter dan",
                    "formatter untuk JS, TS, JSON, dan CSS. Ia penerus proyek Rome,",
                    "versinya 2.5.15, berlisensi MIT atau Apache-2.0. Daya tariknya:",
                    "satu biner, satu berkas biome.json, dan jauh lebih cepat dari",
                    "ESLint ditambah Prettier. Kekurangannya, plugin ekosistem ESLint",
                    "belum semua punya padanan di Biome.",
                    "",
                    "Oxc adalah kumpulan alat Rust dari tim VoidZero (tim yang sama",
                    "dengan Vite): parser, transformer, linter bernama oxlint (versi",
                    "1.88.0), dan formatter oxfmt. Parser Oxc sudah ada di dalam",
                    "Rolldown dan Vite 8. Oxlint biasa dipakai di CI proyek besar karena",
                    "kecepatannya, sering berdampingan dengan ESLint untuk aturan yang",
                    "belum ia punya.",
                    "",
                    "  npx @biomejs/biome check --write .",
                    "  npx oxlint",
                    "",
                    "Pilihan yang aman untuk proyek pertamamu masih ESLint dan Prettier,",
                    "karena hampir semua tutorial dan template memakainya. Kalau",
                    "repositori yang kamu masuki sudah memakai Biome, ikuti saja.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Repositori open source besar hampir selalu menjalankan linter dan",
                    "formatter di CI. Pull request yang formatnya berantakan atau",
                    "melanggar aturan ditolak otomatis sebelum ada manusia yang membaca.",
                    "",
                    "Kasus kecil: kamu ikut proyek kelompok. Tiap kali temanmu menyimpan",
                    "berkas, editornya mengubah kutip tunggal jadi ganda, dan diff git",
                    "penuh perubahan yang nggak ada hubungannya dengan fitur.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Sepakati satu formatter. Pasang Prettier di devDependencies",
                    "     supaya versinya sama untuk semua orang.",
                    "  2. Commit berkas .prettierrc, misalnya:",
                    "       { \"singleQuote\": true }",
                    "  3. Jalankan npx prettier . --write sekali dan commit hasilnya",
                    "     tersendiri dengan pesan \"format seluruh proyek\".",
                    "  4. Minta semua anggota menyalakan format on save di editor",
                    "     dengan Prettier sebagai formatter.",
                    "  5. Tambahkan npx prettier . --check ke CI supaya yang lupa",
                    "     langsung ketahuan.",
                ],
            },
        ],
    },
    {
        "title": "21. React: JSX, Komponen, dan Props",
        "sections": [
            {
                "body": [
                    "React adalah pustaka JavaScript untuk membangun antarmuka dari",
                    "potongan-potongan kecil yang disebut komponen. Kamu menulis",
                    "bagaimana tampilan seharusnya untuk data tertentu, dan React yang",
                    "mengurus perubahan DOM-nya. Idenya sudah kamu bangun sendiri di bab",
                    "3: fungsi h(), pohon virtual DOM, lalu diff. React adalah versi",
                    "lengkap dari hal yang sama.",
                    "",
                    "React dibuat di Facebook dan dibuka sebagai open source tahun 2013.",
                    "Sejak Oktober 2025 proyeknya dipindah ke React Foundation di bawah",
                    "Linux Foundation, yang resmi berjalan Februari 2026. Versi stabil",
                    "terbaru saat materi ini ditulis (Oktober 2026) adalah 19.3.1,",
                    "berlisensi MIT. Di Survei Stack Overflow 2025 React dipakai 44,7%",
                    "responden, peringkat dua di bawah Node.js. Di State of JS 2025 ia",
                    "dipakai 83,6% penjawab, sekaligus jadi sumber keluhan terbanyak.",
                ],
            },
            {
                "heading": "Komponen pertama",
                "bahasa": "jsx",
                "code": """function Sapaan({ nama }) {
  return <h1>Halo, {nama}!</h1>;
}

export default function App() {
  return (
    <main>
      <Sapaan nama="Rina" />
      <Sapaan nama="Budi" />
    </main>
  );
}""",
            },
            {
                "body": [
                    "Komponen React adalah fungsi biasa yang mengembalikan tampilan.",
                    "Tulisan mirip HTML di dalamnya namanya JSX. Beberapa aturannya:",
                    "",
                    "  - Nama komponen diawali huruf besar (Sapaan). Huruf kecil",
                    "    dianggap tag HTML biasa.",
                    "  - Satu komponen mengembalikan satu elemen akar. Kalau butuh",
                    "    beberapa elemen tanpa pembungkus, pakai fragment <>...</>.",
                    "  - Kurung kurawal { } berisi ekspresi JavaScript: variabel,",
                    "    pemanggilan fungsi, operasi hitung.",
                    "  - Atribut memakai nama properti DOM: className untuk class,",
                    "    htmlFor untuk for, onClick untuk onclick.",
                    "  - Tag tanpa isi wajib ditutup: <img />, <input />, <Sapaan />.",
                ],
            },
            {
                "heading": "JSX itu pemanggilan fungsi",
                "body": [
                    "Browser nggak mengerti JSX. Sebelum dikirim, Vite (lewat Oxc) atau",
                    "compiler lain mengubah tiap tag jadi pemanggilan fungsi jsx() dari",
                    "react/jsx-runtime. Hasilnya objek biasa, mirip h() di bab 3.",
                    "Program di bawah memakai jsx() buatan sendiri dan merender",
                    "hasilnya ke teks HTML, supaya kamu lihat apa yang terjadi di",
                    "baliknya.",
                ],
            },
            {
                "heading": "Meniru hasil kompilasi JSX",
                "code": "// Bentuk sederhana fungsi jsx() yang dipanggil kode hasil kompilasi JSX.\nfunction jsx(type, props, key) {\n  return { type, props, key };\n}\n\nfunction render(el) {\n  if (typeof el === 'string' || typeof el === 'number') return String(el);\n  if (Array.isArray(el)) return el.map(render).join('');\n  if (typeof el.type === 'function') return render(el.type(el.props));\n  const { children, ...atribut } = el.props;\n  const attr = Object.entries(atribut)\n    .map(([k, v]) => ` ${k === 'className' ? 'class' : k}=\"${v}\"`)\n    .join('');\n  const isi = children === undefined ? '' : render(children);\n  return `<${el.type}${attr}>${isi}</${el.type}>`;\n}\n\n// JSX: <div className=\"kartu\"><h3>{nama}</h3><p>Rp{harga}</p></div>\nfunction KartuProduk({ nama, harga }) {\n  return jsx('div', {\n    className: 'kartu',\n    children: [jsx('h3', { children: nama }), jsx('p', { children: ['Rp', harga] })],\n  });\n}\n\n// JSX: <ul>{produk.map((p) => <li key={p.id}><KartuProduk {...p} /></li>)}</ul>\nfunction DaftarProduk({ produk }) {\n  return jsx('ul', {\n    children: produk.map((p) => jsx('li', { children: jsx(KartuProduk, p) }, p.id)),\n  });\n}\n\nconst elemen = jsx(DaftarProduk, {\n  produk: [\n    { id: 1, nama: 'Kopi', harga: 18000 },\n    { id: 2, nama: 'Teh', harga: 12000 },\n  ],\n});\nconst html = render(elemen);\nconsole.log(html.replaceAll('</li>', '</li>\\n').trim());",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  <ul><li><div class=\"kartu\"><h3>Kopi</h3><p>Rp18000</p></div></li>",
                    "  <li><div class=\"kartu\"><h3>Teh</h3><p>Rp12000</p></div></li>",
                    "  </ul>",
                    "",
                    "Perhatikan tiga hal. Atribut JSX dan isi di antara tag sama-sama",
                    "masuk ke satu objek props; isi tag jadi props.children. Komponen",
                    "(huruf besar) disimpan sebagai fungsi dan baru dipanggil saat",
                    "dirender. key dipisahkan dari props, karena key cuma dipakai React",
                    "untuk mencocokkan elemen saat diff, dan komponennya sendiri nggak",
                    "bisa membacanya.",
                ],
            },
            {
                "heading": "Props dan children",
                "bahasa": "jsx",
                "code": """function Kartu({ judul, children }) {
  return (
    <section className="kartu">
      <h2>{judul}</h2>
      {children}
    </section>
  );
}

function Halaman() {
  return (
    <Kartu judul="Promo minggu ini">
      <p>Kopi susu diskon 20%.</p>
      <button>Pesan</button>
    </Kartu>
  );
}""",
            },
            {
                "body": [
                    "Props adalah data yang dikirim komponen induk ke anaknya, seperti",
                    "argumen fungsi. Aliran datanya satu arah, dari atas ke bawah. Anak",
                    "nggak boleh mengubah props-nya sendiri; kalau perlu berubah, induk",
                    "yang mengirim nilai baru. children adalah isi di antara tag",
                    "pembuka dan penutup, jadi Kartu bisa membungkus apa saja.",
                ],
            },
            {
                "heading": "Daftar, key, dan tampilan bersyarat",
                "bahasa": "jsx",
                "code": """function DaftarTugas({ tugas }) {
  if (tugas.length === 0) {
    return <p>Belum ada tugas.</p>;
  }
  return (
    <ul>
      {tugas.map((t) => (
        <li key={t.id}>
          {t.judul} {t.selesai && <span>(selesai)</span>}
        </li>
      ))}
    </ul>
  );
}""",
            },
            {
                "body": [
                    "Daftar dibuat dengan map. Tiap butir wajib punya key yang unik di",
                    "antara saudaranya dan stabil, biasanya id dari database. Di bab 3",
                    "kamu lihat kenapa: tanpa key yang stabil, diff menyangka butir",
                    "bergeser, dan isi input atau state ikut tertukar ke butir lain.",
                    "",
                    "Jebakan: memakai indeks sebagai key (key={i}) kelihatan jalan,",
                    "tapi rusak begitu daftarnya disisipi atau diurutkan ulang.",
                    "",
                    "Jebakan: {jumlah && <Badge />} menampilkan angka 0 kalau jumlah",
                    "bernilai 0, karena React merender angka. Tulis",
                    "{jumlah > 0 && <Badge />} supaya hasilnya true atau false.",
                ],
            },
            {
                "heading": "Memulai proyek React",
                "body": [
                    "Dokumentasi react.dev menyarankan memulai lewat framework seperti",
                    "Next.js (bab 12) atau React Router. Untuk belajar dan untuk SPA",
                    "murni, npm create vite@latest dengan template react-ts adalah",
                    "jalan paling ringan. Hindari npx create-react-app; alat itu sudah",
                    "usang sejak Februari 2025 (lihat Peta Build Tool di bab 5).",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Halaman daftar produk di toko online, timeline media sosial, dan dasbor",
                    "admin dibangun dari komponen yang dipakai berulang: kartu produk,",
                    "tombol, badge stok. Satu perubahan di KartuProduk langsung berlaku",
                    "di ratusan tempat.",
                    "",
                    "Kasus kecil: daftar tugas temanmu aneh. Begitu tugas paling atas",
                    "dihapus, centang di butir lain pindah ke butir yang salah.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Buka komponennya dan cari map yang membuat <li>.",
                    "  2. Lihat key-nya. Hampir pasti tertulis key={index}.",
                    "  3. Ganti dengan id yang melekat pada datanya:",
                    "       {tugas.map((t) => <Butir key={t.id} tugas={t} />)}",
                    "  4. Kalau data belum punya id, beri id saat butir dibuat",
                    "     (misalnya crypto.randomUUID()), jangan saat dirender.",
                    "  5. Coba hapus butir paling atas lagi. Centangnya sekarang tetap",
                    "     menempel di tugas yang benar.",
                ],
            },
        ],
    },
    {
        "title": "22. State, Hooks, dan Efek di React",
        "sections": [
            {
                "body": [
                    "Props datang dari luar. State adalah ingatan milik komponen itu",
                    "sendiri: angka di keranjang, isi kolom pencarian, tab yang sedang",
                    "dibuka. Begitu state berubah, React memanggil ulang fungsi",
                    "komponennya dan memperbarui DOM sesuai hasil yang baru.",
                    "",
                    "Fungsi untuk mengakses fitur React dari dalam komponen disebut",
                    "hook. Namanya selalu diawali use: useState, useEffect, useRef, dan",
                    "seterusnya.",
                ],
            },
            {
                "heading": "useState",
                "bahasa": "jsx",
                "code": """import { useState } from 'react';

export default function Penghitung() {
  const [angka, setAngka] = useState(0);

  return (
    <button onClick={() => setAngka(angka + 1)}>
      Diklik {angka} kali
    </button>
  );
}""",
            },
            {
                "body": [
                    "useState(0) mengembalikan pasangan: nilai sekarang dan fungsi untuk",
                    "menggantinya. Tiap kali setAngka dipanggil, terjadi tiga tahap:",
                    "",
                    "  1. Pemicu: React mencatat ada state yang berubah.",
                    "  2. Render: React memanggil Penghitung() lagi dan mendapat pohon",
                    "     elemen baru.",
                    "  3. Commit: React membandingkan pohon lama dan baru, lalu mengubah",
                    "     bagian DOM yang beda saja.",
                    "",
                    "Di dalam satu render, angka adalah snapshot, yaitu nilai tetap",
                    "milik render itu. Memanggil setAngka nggak mengubah variabel angka",
                    "yang sedang kamu pegang; nilai baru baru terlihat di render",
                    "berikutnya. Program di bawah meniru antrean yang diproses React",
                    "sesudah satu klik.",
                ],
            },
            {
                "heading": "State adalah snapshot",
                "code": """// Meniru cara React memproses antrean setState sesudah satu klik.
function prosesAntrean(awal, antrean) {
  return antrean.reduce((s, u) => (typeof u === 'function' ? u(s) : u), awal);
}

const count = 0; // nilai state di render ini: tetap 0 sampai render berikutnya

// Versi 1: setCount(count + 1) tiga kali. Isinya tiga kali "jadikan 1".
const antrean1 = [count + 1, count + 1, count + 1];

// Versi 2: setCount(c => c + 1) tiga kali. Isinya tiga fungsi pembaru.
const antrean2 = [(c) => c + 1, (c) => c + 1, (c) => c + 1];

console.log('setCount(count + 1) x3 ->', prosesAntrean(count, antrean1));
console.log('setCount(c => c + 1) x3 ->', prosesAntrean(count, antrean2));""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  setCount(count + 1) x3 -> 1",
                    "  setCount(c => c + 1) x3 -> 3",
                    "",
                    "Kalau nilai baru bergantung pada nilai lama, pakai bentuk fungsi",
                    "pembaru: setAngka(a => a + 1). Perhatikan juga bahwa tiga",
                    "pemanggilan itu cuma menghasilkan satu render. React mengumpulkan",
                    "semua perubahan dalam satu event dulu (batching), baru merender.",
                ],
            },
            {
                "heading": "Objek, array, dan useReducer",
                "bahasa": "jsx",
                "code": """// Salah: mengubah objek lama. React melihat objek yang sama, jadi diam.
keranjang.items.push(barang);
setKeranjang(keranjang);

// Benar: buat objek baru yang menyalin isi lama.
setKeranjang({ ...keranjang, items: [...keranjang.items, barang] });

// Kalau aturannya banyak, kumpulkan di satu reducer.
function kurangiKeranjang(state, action) {
  switch (action.type) {
    case 'tambah':
      return { ...state, items: [...state.items, action.barang] };
    case 'kosongkan':
      return { ...state, items: [] };
    default:
      return state;
  }
}
const [keranjang, dispatch] = useReducer(kurangiKeranjang, { items: [] });
...""",
            },
            {
                "body": [
                    "React memutuskan perlu render atau nggak dengan Object.is: apakah",
                    "nilainya objek yang sama? Mengubah isi objek lalu mengirim objek",
                    "yang sama nggak memicu apa-apa. Selalu buat salinan baru.",
                    "useReducer berguna saat satu state diubah dengan banyak cara;",
                    "logikanya pindah ke fungsi murni yang gampang diuji. Polanya sama",
                    "dengan Redux di bab 7.",
                ],
            },
            {
                "heading": "useEffect: menyamakan dengan dunia luar",
                "bahasa": "jsx",
                "code": """import { useEffect, useState } from 'react';

function Jam() {
  const [detik, setDetik] = useState(0);

  useEffect(() => {
    const id = setInterval(() => setDetik((d) => d + 1), 1000);
    return () => clearInterval(id);   // pembersihan
  }, []);                             // daftar dependensi kosong

  useEffect(() => {
    document.title = `Sudah ${detik} detik`;
  }, [detik]);

  return <p>{detik} detik</p>;
}""",
            },
            {
                "body": [
                    "useEffect menjalankan kode sesudah React selesai mengubah DOM.",
                    "Gunanya menyamakan komponen dengan sistem di luar React: timer,",
                    "judul tab, koneksi WebSocket, pustaka peta. Array di akhir adalah",
                    "daftar dependensi: efek dijalankan ulang kalau salah satu nilainya",
                    "berubah. Fungsi yang dikembalikan efek dipanggil sebelum efek",
                    "dijalankan ulang dan saat komponen dilepas.",
                    "",
                    "Jebakan: memakai efek untuk menghitung sesuatu dari state lain,",
                    "misalnya useEffect yang mengisi totalHarga tiap kali items",
                    "berubah. Itu render dua kali tanpa perlu. Hitung langsung saat",
                    "render: const totalHarga = items.reduce(...).",
                    "",
                    "Untuk mengambil data dari API, efek polos rawan balapan dan nggak",
                    "punya cache. Di aplikasi sungguhan pakai framework atau TanStack",
                    "Query (bab 7).",
                ],
            },
            {
                "heading": "useRef, useMemo, dan aturan hooks",
                "body": [
                    "useRef menyimpan nilai yang bertahan antar-render tapi nggak memicu",
                    "render saat diubah. Paling sering dipakai untuk memegang elemen DOM,",
                    "misalnya untuk memanggil inputRef.current.focus(). useMemo",
                    "menyimpan hasil hitungan berat supaya nggak dihitung ulang tiap",
                    "render. Dengan React Compiler (materi berikutnya), useMemo manual",
                    "makin jarang perlu.",
                    "",
                    "Aturan hooks ada dua. Panggil hook hanya di tingkat atas komponen",
                    "atau hook buatanmu, jangan di dalam if, perulangan, atau fungsi",
                    "lain. Dan panggil hanya dari komponen atau hook. Alasannya: React",
                    "mengenali tiap useState dari urutan pemanggilannya, dan hook di",
                    "dalam if membuat urutan itu bergeser. Latihan bab ini membuktikan",
                    "akibatnya. Plugin eslint-plugin-react-hooks menangkap pelanggaran",
                    "ini otomatis.",
                    "",
                    "Ingat: di mode pengembangan, <StrictMode> sengaja memanggil fungsi",
                    "komponen dua kali dan memasang-lepas-memasang efek sekali. Kalau",
                    "console.log-mu muncul dua kali, itu bukan bug. Tujuannya menyingkap",
                    "efek yang lupa membersihkan diri.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Kolom pencarian dengan saran otomatis, keranjang belanja, dan",
                    "formulir multi-langkah semuanya bertumpu pada state. Bug state yang",
                    "paling sering ditemui di aplikasi sungguhan adalah tampilan yang",
                    "nggak ikut berubah karena state dimutasi langsung.",
                    "",
                    "Kasus kecil: tombol \"Tambah ke keranjang\" temanmu menambah barang",
                    "di console.log, tapi angka di ikon keranjang tetap 0.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Cari pemanggilan setKeranjang dan lihat apa yang dikirim.",
                    "  2. Kalau ada keranjang.push(...) lalu setKeranjang(keranjang),",
                    "     itu objek yang sama, jadi Object.is bilang nggak berubah.",
                    "  3. Ganti dengan salinan baru:",
                    "       setKeranjang((k) => [...k, barang]);",
                    "  4. Pakai bentuk fungsi pembaru supaya klik cepat beruntun nggak",
                    "     memakai snapshot lama.",
                    "  5. Pasang React DevTools di browser untuk melihat nilai state",
                    "     komponen berubah tiap klik.",
                ],
            },
        ],
    },
    {
        "title": "23. React Modern: Context, Suspense, dan Server Components",
        "sections": [
            {
                "body": [
                    "React 19 rilis 5 Desember 2024. Sesudahnya ada 19.2 (1 Oktober",
                    "2025) yang menambah komponen Activity dan hook useEffectEvent, lalu",
                    "19.3 (9 September 2026) dengan View Transitions dan Fragment Refs.",
                    "Materi ini mengenalkan fitur yang paling sering kamu temui di kode",
                    "React sekarang. Kamu nggak perlu menghafal semuanya; cukup tahu",
                    "namanya, masalah yang ia pecahkan, dan kapan mencarinya di",
                    "dokumentasi.",
                ],
            },
            {
                "heading": "Context: berbagi data tanpa estafet props",
                "bahasa": "jsx",
                "code": """import { createContext, use, useState } from 'react';

const TemaContext = createContext('terang');

export default function App() {
  const [tema, setTema] = useState('gelap');
  return (
    <TemaContext value={tema}>
      <Halaman />
    </TemaContext>
  );
}

function TombolTema() {
  const tema = use(TemaContext);   // atau useContext(TemaContext)
  return <button className={tema}>Tema: {tema}</button>;
}""",
            },
            {
                "body": [
                    "Kadang data dibutuhkan komponen yang letaknya jauh di bawah:",
                    "tema, bahasa, pengguna yang sedang login. Mengoperkannya lewat",
                    "props di tiap lapis disebut prop drilling dan cepat melelahkan.",
                    "Context membuat nilai bisa dibaca komponen mana pun di bawah",
                    "penyedianya. Sejak React 19, <TemaContext value={...}> bisa",
                    "langsung dipakai sebagai penyedia; kode lama menulis",
                    "<TemaContext.Provider>.",
                    "",
                    "Jebakan: semua pembaca context dirender ulang saat nilainya",
                    "berubah. Context cocok untuk data yang jarang berubah. Untuk state",
                    "yang sering berubah dan dipakai banyak tempat, lihat Zustand atau",
                    "Redux di bab 7.",
                ],
            },
            {
                "heading": "Error boundary dan Suspense",
                "bahasa": "jsx",
                "code": """import { Suspense, lazy } from 'react';
import { ErrorBoundary } from 'react-error-boundary';

const PanelAdmin = lazy(() => import('./PanelAdmin.jsx'));

export default function App() {
  return (
    <ErrorBoundary fallback={<p>Ada yang rusak. Muat ulang halaman.</p>}>
      <Suspense fallback={<p>Memuat panel...</p>}>
        <PanelAdmin />
      </Suspense>
    </ErrorBoundary>
  );
}""",
            },
            {
                "body": [
                    "Error boundary menangkap error yang terjadi saat anak-anaknya",
                    "dirender, lalu menampilkan cadangan, jadi satu komponen rusak nggak",
                    "membuat seluruh halaman putih. React sendiri cuma menyediakannya",
                    "lewat komponen class, jadi kebanyakan orang memakai paket kecil",
                    "react-error-boundary.",
                    "",
                    "Suspense menampilkan fallback selama sesuatu di dalamnya belum",
                    "siap: kode yang dimuat dengan lazy(), atau data yang dibaca lewat",
                    "use(promise) di framework yang mendukungnya. Ini code splitting",
                    "dari bab 5 yang dipakai di tingkat komponen.",
                ],
            },
            {
                "heading": "Server Components",
                "bahasa": "jsx",
                "code": """// app/produk/page.jsx  (Server Component, jalan di server)
import { db } from '@/lib/db';
import TombolSuka from './TombolSuka';

export default async function HalamanProduk() {
  const produk = await db.produk.findMany();
  return (
    <ul>
      {produk.map((p) => (
        <li key={p.id}>{p.nama} <TombolSuka id={p.id} /></li>
      ))}
    </ul>
  );
}

// app/produk/TombolSuka.jsx  (Client Component)
'use client';
import { useState } from 'react';
export default function TombolSuka({ id }) {
  const [suka, setSuka] = useState(false);
  return <button onClick={() => setSuka(!suka)}>{suka ? 'Disukai' : 'Suka'}</button>;
}""",
            },
            {
                "body": [
                    "Server Components adalah komponen yang cuma jalan di server. Ia",
                    "boleh async, boleh membaca database langsung, dan kodenya nggak",
                    "pernah dikirim ke browser, jadi bundel lebih kecil. Gantinya, ia",
                    "nggak boleh memakai state, efek, atau event. Komponen yang butuh",
                    "interaksi ditandai 'use client' di baris pertama berkasnya; itu",
                    "batas tempat kode mulai dikirim ke browser.",
                    "",
                    "Server Components butuh framework yang mendukungnya. Yang paling",
                    "matang Next.js dengan App Router (bab 12). React Router juga",
                    "sedang menambah dukungannya. Di proyek Vite biasa, semua komponen",
                    "adalah Client Component.",
                    "",
                    "Ingat: Desember 2025 tim React mengumumkan celah keamanan kritis di",
                    "React Server Components yang memungkinkan eksekusi kode dari jarak",
                    "jauh, diperbaiki di 19.0.1, 19.1.2, dan 19.2.1. Kode yang jalan di",
                    "server wajib rajin diperbarui.",
                ],
            },
            {
                "heading": "Actions dan formulir",
                "bahasa": "jsx",
                "code": """import { useActionState } from 'react';

async function simpanEmail(stateLama, formData) {
  const email = formData.get('email');
  if (!email.includes('@')) return { pesan: 'Email nggak valid' };
  await kirimKeServer(email);
  return { pesan: 'Tersimpan!' };
}

export default function FormLangganan() {
  const [state, aksi, sedangKirim] = useActionState(simpanEmail, { pesan: '' });
  return (
    <form action={aksi}>
      <input name="email" type="email" />
      <button disabled={sedangKirim}>Langganan</button>
      <p>{state.pesan}</p>
    </form>
  );
}""",
            },
            {
                "body": [
                    "Di React 19, atribut action pada <form> boleh berisi fungsi, termasuk",
                    "fungsi async. React menyebutnya Action. useActionState mengurus tiga",
                    "hal yang dulu kamu tulis manual: hasil terakhir, fungsi untuk",
                    "dikirim ke form, dan status sedang mengirim. Ada juga useFormStatus",
                    "dan useOptimistic untuk menampilkan hasil sebelum server menjawab.",
                    "Di framework dengan Server Components, fungsi bertanda 'use server'",
                    "bisa dipanggil langsung dari form.",
                ],
            },
            {
                "heading": "React Compiler",
                "body": [
                    "Dulu, supaya komponen nggak dirender ulang tanpa perlu, kamu",
                    "menaburkan useMemo, useCallback, dan memo di mana-mana. React",
                    "Compiler versi 1.0 (7 Oktober 2025) melakukannya otomatis saat",
                    "build: ia membaca kodemu dan menyisipkan memoisasi di tempat yang",
                    "tepat. Ia dipasang sebagai plugin build, salah satunya plugin",
                    "Babel. Syaratnya kodemu mengikuti aturan React: komponen murni dan",
                    "state nggak dimutasi. Kode yang melanggar dilewati compiler.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Toko online yang dibangun dengan Next.js memakai Server Components",
                    "untuk daftar produk (data langsung dari database, cepat terindeks",
                    "mesin pencari) dan Client Components untuk tombol keranjang dan",
                    "filter interaktif.",
                    "",
                    "Kasus kecil: kamu menambah useState ke komponen daftar produk di",
                    "proyek Next.js, lalu muncul error bahwa useState cuma bisa dipakai",
                    "di Client Component.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Sadari bahwa berkas di folder app/ adalah Server Component",
                    "     secara bawaan.",
                    "  2. Jangan tandai seluruh halaman dengan 'use client'; nanti semua",
                    "     kodenya ikut terkirim ke browser.",
                    "  3. Pisahkan bagian yang interaktif ke berkas sendiri, misalnya",
                    "     FilterHarga.jsx, dan beri baris pertama 'use client'.",
                    "  4. Biarkan halaman tetap Server Component yang mengambil data,",
                    "     lalu kirim data itu ke FilterHarga lewat props.",
                ],
            },
        ],
    },
    {
        "title": "24. Mengetik Komponen React dengan TypeScript",
        "sections": [
            {
                "body": [
                    "Komponen React yang ditulis dengan TypeScript disimpan di berkas",
                    ".tsx. Gunanya terasa saat komponenmu dipakai orang lain: lupa",
                    "mengirim props wajib, salah tipe, atau salah nama event langsung",
                    "digaris merah oleh editor. Tipe untuk React datang dari paket",
                    "@types/react, yang sudah terpasang di template react-ts. Dasar",
                    "tipe objek dan union ada di materi TypeScript bab 2.",
                ],
            },
            {
                "heading": "Mengetik props",
                "bahasa": "tsx",
                "code": """import type { ReactNode } from 'react';

type KartuProps = {
  judul: string;
  harga?: number;            // opsional
  varian?: 'biasa' | 'promo';
  children: ReactNode;       // apa saja yang bisa dirender
};

export function Kartu({ judul, harga, varian = 'biasa', children }: KartuProps) {
  return (
    <section className={`kartu ${varian}`}>
      <h2>{judul}</h2>
      {harga !== undefined && <p>Rp{harga}</p>}
      {children}
    </section>
  );
}

// <Kartu judul="Kopi" varian="diskon">...</Kartu>
// error: Type '"diskon"' is not assignable to
//        type '"biasa" | "promo" | undefined'""",
            },
            {
                "body": [
                    "Props cukup ditulis sebagai tipe objek di parameter fungsi. Medan",
                    "bertanda ? boleh nggak dikirim; nilai bawaannya bisa diberikan lewat",
                    "destrukturisasi (varian = 'biasa'). ReactNode menerima teks, angka,",
                    "elemen, array, null, dan false, jadi cocok untuk children.",
                    "",
                    "Kamu akan melihat tim lain menulis React.FC<KartuProps>. Itu juga",
                    "jalan, tapi sejak @types/react 18 ia nggak lagi menyertakan children",
                    "otomatis, jadi banyak tim memilih cara di atas yang lebih polos.",
                ],
            },
            {
                "heading": "Event, state, dan ref",
                "bahasa": "tsx",
                "code": """import { useRef, useState, type ChangeEvent, type FormEvent } from 'react';

type Pengguna = { id: number; nama: string };

export function FormCari() {
  const [kata, setKata] = useState('');                 // string, ditebak
  const [hasil, setHasil] = useState<Pengguna | null>(null);
  const inputRef = useRef<HTMLInputElement>(null);

  function ubah(e: ChangeEvent<HTMLInputElement>) {
    setKata(e.target.value);
  }

  function kirim(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();
    inputRef.current?.focus();
  }

  return (
    <form onSubmit={kirim}>
      <input ref={inputRef} value={kata} onChange={ubah} />
      {hasil && <p>{hasil.nama}</p>}
    </form>
  );
}""",
            },
            {
                "body": [
                    "useState menebak tipenya dari nilai awal. Kalau nilai awalnya null",
                    "tapi nanti diisi objek, tulis tipenya: useState<Pengguna | null>.",
                    "Tanpa itu TypeScript mengira state ini selamanya null. useRef untuk",
                    "elemen DOM diberi tipe elemennya dan nilai awal null, jadi",
                    "inputRef.current harus dicek dengan ?. sebelum dipakai.",
                    "",
                    "Tipe event mengikuti elemennya: ChangeEvent<HTMLInputElement> untuk",
                    "input, FormEvent<HTMLFormElement> untuk submit,",
                    "MouseEvent<HTMLButtonElement> untuk klik. Trik cepat: tulis",
                    "handler-nya langsung di JSX, arahkan kursor ke parameter e, dan",
                    "salin tipe yang ditampilkan editor.",
                    "",
                    "Untuk useReducer, tulis action sebagai union supaya tiap jenis",
                    "action membawa data yang tepat:",
                    "",
                    "  type Aksi =",
                    "    | { type: 'tambah'; barang: Barang }",
                    "    | { type: 'hapus'; id: number }",
                    "    | { type: 'kosongkan' };",
                    "",
                    "Di dalam switch (action.type), TypeScript tahu bahwa action.barang",
                    "cuma ada di cabang 'tambah'. Salah ketik nama action, misalnya",
                    "dispatch({ type: 'tambha' }), langsung ditolak.",
                    "",
                    "Hook buatan sendiri diketik seperti fungsi biasa. Kalau ia",
                    "mengembalikan pasangan seperti useState, tambahkan as const di",
                    "akhir array, misalnya return [buka, setBuka] as const. Tanpa itu",
                    "TypeScript menganggapnya array campuran, dan pemakainya kehilangan",
                    "tipe masing-masing unsur.",
                ],
            },
            {
                "heading": "Props gabungan dan komponen generic",
                "body": [
                    "Dua pola ini membedakan tipe yang sekadar ada dengan tipe yang",
                    "menangkap kesalahan. Program di bawah ditulis dengan TypeScript",
                    "murni tanpa React supaya bisa dijalankan di sini; komponennya",
                    "mengembalikan teks. Pola tipenya persis sama dengan di .tsx.",
                ],
            },
            {
                "heading": "Tombol dan daftar bertipe",
                "bahasa": "typescript",
                "code": """// Props berbentuk gabungan: tombol tautan wajib punya href,
// tombol aksi wajib punya onKlik.
type TombolProps =
  | { jenis: "tautan"; label: string; href: string }
  | { jenis: "aksi"; label: string; onKlik: () => string };

function Tombol(props: TombolProps): string {
  if (props.jenis === "tautan") {
    return `<a href="${props.href}">${props.label}</a>`;
  }
  return `<button>${props.label}</button> -> ${props.onKlik()}`;
}

// Komponen generic: tipe T ditebak dari isi item.
type DaftarProps<T> = { item: T[]; tampilkan: (x: T) => string };

function Daftar<T>(props: DaftarProps<T>): string {
  return props.item.map(props.tampilkan).join(", ");
}

console.log(Tombol({ jenis: "tautan", label: "Lihat promo", href: "/promo" }));
console.log(Tombol({ jenis: "aksi", label: "Simpan", onKlik: () => "tersimpan" }));
console.log(
  Daftar({
    item: [
      { nama: "Kopi", harga: 18000 },
      { nama: "Teh", harga: 12000 },
    ],
    tampilkan: (p) => `${p.nama} Rp${p.harga}`,
  })
);
// Tombol({ jenis: "tautan", label: "Rusak" });
// error: Property 'href' is missing ...""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  <a href=\"/promo\">Lihat promo</a>",
                    "  <button>Simpan</button> -> tersimpan",
                    "  Kopi Rp18000, Teh Rp12000",
                    "",
                    "TombolProps adalah union yang dibedakan lewat medan jenis. Di dalam",
                    "if, TypeScript tahu props pasti punya href; di luar if, pasti punya",
                    "onKlik. Kalau baris komentar terakhir dinyalakan, tsc menolak",
                    "karena tombol tautan tanpa href. Di Daftar, kamu nggak pernah",
                    "menulis tipe p, tapi TypeScript tahu p punya nama dan harga karena",
                    "T ditebak dari isi item.",
                ],
            },
            {
                "heading": "Meminjam tipe elemen bawaan",
                "bahasa": "tsx",
                "code": """import type { ComponentProps } from 'react';

type TombolUtamaProps = ComponentProps<'button'> & { memuat?: boolean };

export function TombolUtama({ memuat = false, children, ...sisa }: TombolUtamaProps) {
  return (
    <button {...sisa} disabled={memuat || sisa.disabled}>
      {memuat ? 'Memuat...' : children}
    </button>
  );
}

// <TombolUtama type="submit" onClick={simpan} memuat={sedangSimpan}>Simpan</TombolUtama>""",
            },
            {
                "body": [
                    "ComponentProps<'button'> berisi semua atribut yang sah untuk",
                    "<button>: type, disabled, onClick, aria-label, dan lainnya. Dengan",
                    "menggabungkannya, TombolUtama menerima semua itu plus props",
                    "tambahanmu sendiri, dan sisanya diteruskan ke elemen aslinya.",
                    "Pustaka komponen seperti shadcn/ui (bab 13) memakai pola ini di",
                    "hampir setiap komponennya.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Pustaka komponen yang dipakai banyak tim, seperti sistem desain",
                    "internal perusahaan atau paket npm komponen UI, hampir selalu",
                    "ditulis dengan TypeScript. Tipe props jadi dokumentasi yang muncul",
                    "di editor saat orang mengetik nama komponennya.",
                    "",
                    "Kasus kecil: komponen Notifikasi temanmu punya props tipe?: string.",
                    "Orang lain mengirim tipe=\"eror\" (salah ketik) dan notifikasinya",
                    "tampil tanpa warna, tanpa error apa pun.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Persempit tipenya jadi union literal:",
                    "       tipe?: 'info' | 'sukses' | 'galat';",
                    "  2. Jalankan npx tsc --noEmit. Semua pemakaian yang salah ketik",
                    "     sekarang muncul sebagai error.",
                    "  3. Perbaiki tiap pemakaian sampai tsc bersih.",
                    "  4. Kalau ada data dari server yang menentukan tipe notifikasi,",
                    "     periksa nilainya dulu sebelum dikirim ke komponen.",
                ],
            },
        ],
    },
    {
        "title": "25. Rute di React: React Router dan TanStack Router",
        "sections": [
            {
                "body": [
                    "React sendiri cuma mengurus tampilan. Ia nggak tahu apa-apa soal",
                    "alamat di address bar. Padahal aplikasi butuh halaman: /produk,",
                    "/produk/42, /keranjang. Kalau tiap pindah halaman browser memuat",
                    "ulang semuanya, state hilang dan layar berkedip.",
                    "",
                    "Router adalah pustaka yang memetakan alamat (URL) ke komponen. Saat",
                    "kamu mengklik tautan, router mengganti URL lewat History API",
                    "browser tanpa memuat ulang halaman, lalu merender komponen yang",
                    "cocok. Aplikasi yang bekerja begini disebut SPA (single-page",
                    "application): satu halaman HTML, isinya berganti-ganti.",
                ],
            },
            {
                "heading": "React Router",
                "body": [
                    "React Router adalah router React yang paling banyak dipakai. Versi",
                    "8 rilis 17 Juni 2026, dan versi terbarunya saat materi ini ditulis",
                    "(Oktober 2026) adalah 8.4.0; jalur 7.x masih ditambal. Mulai versi",
                    "8, rilis major dijadwalkan setahun sekali.",
                    "",
                    "Ada tiga cara memakainya, dan ini yang sering membingungkan:",
                    "",
                    "  - Mode declarative: rute ditulis sebagai elemen <Routes> dan",
                    "    <Route>. Paling sederhana, tanpa fitur data.",
                    "  - Mode data: rute ditulis sebagai objek lewat",
                    "    createBrowserRouter, dan tiap rute boleh punya loader (ambil",
                    "    data sebelum halaman tampil) serta action (terima kiriman form).",
                    "  - Mode framework: React Router jadi framework full-stack dengan",
                    "    rute berbasis berkas dan render di server. Ini kelanjutan Remix",
                    "    versi 2, dibahas di bab 12.",
                    "",
                    "Materi ini memakai mode data, karena di situ konsep loader terlihat",
                    "jelas dan pindah ke mode framework nanti tinggal selangkah.",
                ],
            },
            {
                "heading": "Rute bersarang dengan loader",
                "bahasa": "jsx",
                "code": """import { createBrowserRouter, Link, Outlet, useLoaderData } from 'react-router';
import { RouterProvider } from 'react-router/dom';
import { createRoot } from 'react-dom/client';

const router = createBrowserRouter([
  {
    path: '/',
    Component: Tata,
    children: [
      { index: true, Component: Beranda },
      {
        path: 'produk/:id',
        loader: async ({ params }) => {
          const res = await fetch(`/api/produk/${params.id}`);
          return res.json();
        },
        Component: DetailProduk,
      },
    ],
  },
]);

function Tata() {
  return (
    <>
      <nav><Link to="/">Beranda</Link> <Link to="/produk/42">Kopi</Link></nav>
      <Outlet />
    </>
  );
}

function DetailProduk() {
  const produk = useLoaderData();
  return <h1>{produk.nama}</h1>;
}

createRoot(document.getElementById('root')).render(<RouterProvider router={router} />);""",
            },
            {
                "body": [
                    "Rute bersarang artinya satu rute punya anak. Tata adalah kerangka",
                    "(navigasi, footer) yang tetap tampil, dan <Outlet /> adalah lubang",
                    "tempat anaknya dirender. :id adalah parameter dinamis: untuk URL",
                    "/produk/42, params.id bernilai \"42\" (selalu teks). loader jalan",
                    "sebelum DetailProduk dirender, jadi komponennya tinggal membaca",
                    "datanya lewat useLoaderData.",
                    "",
                    "Jebakan: di React Router 8, paket react-router-dom sudah dihapus.",
                    "Import dari react-router, dan RouterProvider dari",
                    "react-router/dom. Tutorial lama yang menulis",
                    "import ... from 'react-router-dom' perlu disesuaikan. Versi 8 juga",
                    "butuh React 19.2.7 ke atas dan cuma terbit sebagai ES Module.",
                ],
            },
            {
                "heading": "Cara router mencocokkan URL",
                "code": """// Tabel rute, urut dari yang paling khusus. '*' menangkap sisanya.
const rute = [
  { pola: '/', komponen: 'Beranda' },
  { pola: '/produk', komponen: 'DaftarProduk' },
  { pola: '/produk/:id', komponen: 'DetailProduk' },
  { pola: '/produk/:id/ulasan', komponen: 'UlasanProduk' },
  { pola: '*', komponen: 'TidakDitemukan' },
];

function cocokkan(pola, url) {
  if (pola === '*') return {};
  const a = pola.split('/').filter(Boolean);
  const b = url.split('/').filter(Boolean);
  if (a.length !== b.length) return null;
  const params = {};
  for (let i = 0; i < a.length; i++) {
    if (a[i].startsWith(':')) params[a[i].slice(1)] = decodeURIComponent(b[i]);
    else if (a[i] !== b[i]) return null;
  }
  return params;
}

for (const url of ['/', '/produk/42', '/produk/42/ulasan', '/keranjang']) {
  for (const r of rute) {
    const params = cocokkan(r.pola, url);
    if (params) {
      console.log(`${url.padEnd(18)} -> ${r.komponen} ${JSON.stringify(params)}`);
      break;
    }
  }
}""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  /                  -> Beranda {}",
                    "  /produk/42         -> DetailProduk {\"id\":\"42\"}",
                    "  /produk/42/ulasan  -> UlasanProduk {\"id\":\"42\"}",
                    "  /keranjang         -> TidakDitemukan {}",
                    "",
                    "Router sungguhan nggak bergantung pada urutan tulis. Ia memberi skor:",
                    "potongan statis seperti produk menang atas parameter seperti :id,",
                    "dan * selalu terakhir. Tapi prinsipnya sama dengan program ini.",
                ],
            },
            {
                "heading": "TanStack Router",
                "bahasa": "tsx",
                "code": """// src/routes/produk.$id.tsx
import { createFileRoute } from '@tanstack/react-router';

export const Route = createFileRoute('/produk/$id')({
  loader: ({ params }) => ambilProduk(params.id),   // params.id bertipe string
  component: DetailProduk,
});

function DetailProduk() {
  const produk = Route.useLoaderData();              // tipenya ikut dari loader
  return <h1>{produk.nama}</h1>;
}""",
            },
            {
                "body": [
                    "TanStack Router adalah router React (dan Solid) yang tipenya aman",
                    "penuh. Parameter URL, query string, dan hasil loader semuanya",
                    "punya tipe TypeScript, jadi <Link to=\"/produk/$id\"> tanpa params",
                    "langsung ditolak editor. Parameter ditulis dengan $, rute biasanya",
                    "dibuat dari nama berkas, dan pohon rutenya dihasilkan otomatis oleh",
                    "plugin Vite. Versinya 1.170 dan rilisnya sering sekali. Ia juga",
                    "fondasi TanStack Start (bab 12).",
                    "",
                    "Memilih di antara keduanya: React Router kalau kamu ingin pilihan",
                    "yang paling banyak tutorial dan jalur ke mode framework.",
                    "TanStack Router kalau proyekmu TypeScript dan kamu ingin parameter",
                    "serta query string tercek sampai ke tautan.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Hampir semua SPA (dasbor, panel admin, aplikasi kasir berbasis",
                    "web) memakai router di sisi klien. Masalah paling umum muncul saat",
                    "deploy, karena server hosting belum tahu soal rute itu.",
                    "",
                    "Kasus kecil: aplikasimu jalan normal saat diklik dari beranda. Tapi",
                    "kalau pengguna membuka /produk/42 langsung atau menekan reload,",
                    "hosting menjawab 404.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pahami sebabnya: server mencari berkas produk/42 di folder",
                    "     dist/, dan berkas itu memang nggak ada.",
                    "  2. Atur server supaya semua alamat yang nggak cocok dengan",
                    "     berkas dijawab index.html. Di Netlify, buat berkas",
                    "     public/_redirects berisi:",
                    "       /*  /index.html  200",
                    "  3. Di Nginx, tambahkan di blok location:",
                    "       try_files $uri /index.html;",
                    "  4. Build ulang, deploy, lalu coba reload di /produk/42 lagi.",
                    "  5. Tetap sediakan rute * di router supaya alamat yang salah",
                    "     menampilkan halaman \"tidak ditemukan\" buatanmu.",
                ],
            },
        ],
    },
    {
        "title": "26. Server State: TanStack Query, SWR, dan Klien API",
        "sections": [
            {
                "body": [
                    "State di aplikasi frontend ada dua jenis, dan memisahkannya",
                    "membuat kodemu jauh lebih sederhana.",
                    "",
                    "  - Client state: milik browser sepenuhnya. Tab yang terbuka, isi",
                    "    formulir yang belum dikirim, tema gelap.",
                    "  - Server state: salinan data yang aslinya ada di server. Daftar",
                    "    produk, profil pengguna, riwayat pesanan. Salinanmu bisa basi",
                    "    kapan saja karena orang lain mengubah aslinya.",
                    "",
                    "Server state punya masalah sendiri. Ia perlu cache supaya nggak",
                    "mengambil ulang terus. Dua komponen yang minta data sama sebaiknya",
                    "cuma memicu satu permintaan. Data basi perlu disegarkan, dan",
                    "jawaban lama nggak boleh menimpa jawaban yang lebih baru. Menulis",
                    "semua itu dengan useEffect dan useState itu panjang dan rawan bug.",
                ],
            },
            {
                "heading": "TanStack Query",
                "bahasa": "jsx",
                "code": """import { QueryClient, QueryClientProvider, useMutation, useQuery,
  useQueryClient } from '@tanstack/react-query';

const queryClient = new QueryClient();

export default function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <DetailProduk id={42} />
    </QueryClientProvider>
  );
}

function DetailProduk({ id }) {
  const qc = useQueryClient();
  const { data, isPending, error } = useQuery({
    queryKey: ['produk', id],
    queryFn: () => fetch(`/api/produk/${id}`).then((r) => r.json()),
    staleTime: 60_000,
  });
  const ubahHarga = useMutation({
    mutationFn: (harga) => fetch(`/api/produk/${id}`, {
      method: 'PATCH', body: JSON.stringify({ harga }),
    }),
    onSuccess: () => qc.invalidateQueries({ queryKey: ['produk', id] }),
  });

  if (isPending) return <p>Memuat...</p>;
  if (error) return <p>Gagal: {error.message}</p>;
  return <button onClick={() => ubahHarga.mutate(20000)}>{data.nama}</button>;
}""",
            },
            {
                "body": [
                    "TanStack Query (dulu React Query) adalah pustaka standar de facto",
                    "untuk server state; versinya 5.104 dan tersedia juga untuk Vue,",
                    "Solid, dan Svelte. Ada tiga konsep inti:",
                    "",
                    "  - queryKey adalah nama cache. ['produk', 42] dan ['produk', 7]",
                    "    disimpan terpisah.",
                    "  - staleTime menentukan berapa lama data dianggap segar. Bawaannya",
                    "    0, artinya langsung basi dan disegarkan saat komponen dipasang",
                    "    lagi atau jendela kembali difokuskan.",
                    "  - Mutation mengubah data di server. Sesudah berhasil,",
                    "    invalidateQueries menandai cache terkait basi supaya diambil",
                    "    ulang.",
                    "",
                    "Data yang nggak lagi dipakai komponen mana pun dibuang dari cache",
                    "sesudah gcTime, bawaannya 5 menit.",
                    "",
                    "Jebakan: queryKey wajib memuat semua nilai yang dipakai queryFn.",
                    "Kalau queryFn memakai id tapi kuncinya cuma ['produk'], produk 42",
                    "dan produk 7 berbagi satu cache, dan halaman menampilkan produk",
                    "yang salah.",
                ],
            },
            {
                "heading": "Cache query dari dekat",
                "code": """// Cache query mini dengan jam palsu, meniru ide TanStack Query.
let jam = 0;            // milidetik palsu, kita yang memajukan
let panggilanServer = 0;

async function ambilProduk(id) {
  panggilanServer++;
  return { id, nama: 'Produk ' + id, versi: panggilanServer };
}

const cache = new Map(); // kunci -> { data, waktu, janji }

async function query(kunci, ambil, staleTime) {
  const k = JSON.stringify(kunci);
  const isi = cache.get(k);
  if (isi && isi.janji) {
    return { sumber: 'menumpang permintaan yang sama', data: await isi.janji };
  }
  if (isi && jam - isi.waktu < staleTime) {
    return { sumber: 'cache segar', data: isi.data };
  }
  const janji = ambil();
  if (isi) {
    // Basi: kembalikan data lama sekarang, perbarui di belakang layar.
    cache.set(k, { ...isi, janji });
    janji.then((data) => cache.set(k, { data, waktu: jam }));
    return { sumber: 'cache basi, diperbarui di latar', data: isi.data };
  }
  cache.set(k, { janji });
  const data = await janji;
  cache.set(k, { data, waktu: jam });
  return { sumber: 'ambil dari server', data };
}

const tampil = (label, h) =>
  console.log(`t=${jam} ${label}: ${h.sumber} (versi ${h.data.versi})`);
const produk = (id) => query(['produk', id], () => ambilProduk(id), 5000);

async function main() {
  const [a, b] = await Promise.all([produk(1), produk(1)]);
  tampil('komponen A', a);
  tampil('komponen B', b);
  jam = 3000;
  tampil('buka lagi', await produk(1));
  jam = 8000;
  tampil('fokus jendela', await produk(1));
  jam = 8100;
  tampil('render berikutnya', await produk(1));
  tampil('produk lain', await produk(2));
  console.log('Panggilan ke server:', panggilanServer);
}
main();""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  t=0 komponen A: ambil dari server (versi 1)",
                    "  t=0 komponen B: menumpang permintaan yang sama (versi 1)",
                    "  t=3000 buka lagi: cache segar (versi 1)",
                    "  t=8000 fokus jendela: cache basi, diperbarui di latar (versi 1)",
                    "  t=8100 render berikutnya: cache segar (versi 2)",
                    "  t=8100 produk lain: ambil dari server (versi 3)",
                    "  Panggilan ke server: 3",
                    "",
                    "Enam kali minta data, tiga kali ke server. Dua komponen yang",
                    "meminta bersamaan berbagi satu permintaan. Data basi tetap",
                    "ditampilkan seketika sementara versi barunya diambil, jadi layar",
                    "nggak pernah kosong. Pola ini namanya stale-while-revalidate,",
                    "diambil dari arahan cache HTTP dengan nama yang sama.",
                ],
            },
            {
                "heading": "SWR",
                "bahasa": "jsx",
                "code": """import useSWR from 'swr';

const ambil = (url) => fetch(url).then((r) => r.json());

function Profil() {
  const { data, error, isLoading } = useSWR('/api/saya', ambil);
  if (isLoading) return <p>Memuat...</p>;
  if (error) return <p>Gagal memuat</p>;
  return <p>Halo, {data.nama}</p>;
}""",
            },
            {
                "body": [
                    "SWR adalah hook data fetching dari Vercel, versinya 2.5.1. Namanya",
                    "singkatan stale-while-revalidate, persis pola di program tadi. API",
                    "dasarnya lebih ringkas dari TanStack Query: kunci (biasanya URL)",
                    "dan fungsi pengambil. Fiturnya lebih sedikit, jadi cocok untuk",
                    "aplikasi Next.js yang kebutuhan datanya sederhana.",
                ],
            },
            {
                "heading": "Klien API: fetch, Axios, dan GraphQL",
                "body": [
                    "Yang mengirim permintaan HTTP sungguhan adalah klien API. Pilihan",
                    "pertama sekarang fetch bawaan browser (dan Node). Axios (1.20.0)",
                    "masih banyak sekali dipakai, terutama di kode lama. Kelebihannya",
                    "interceptor (misalnya menempelkan token ke semua permintaan),",
                    "JSON diurai otomatis, dan status 4xx atau 5xx dianggap error.",
                    "",
                    "Jebakan: fetch nggak melempar error untuk 404 atau 500. Promise-nya",
                    "tetap berhasil; kamu harus mengecek res.ok sendiri sebelum",
                    "res.json(). Banyak queryFn yang lupa ini, sehingga halaman error",
                    "server diurai sebagai data.",
                    "",
                    "Kalau backend-nya GraphQL (dibahas di kurikulum Backend), ada klien",
                    "khusus yang sekaligus mengurus cache:",
                    "",
                    "  - Apollo Client (versi 4) adalah yang paling populer, dengan",
                    "    cache ternormalisasi: objek yang sama dari dua query disimpan",
                    "    sekali.",
                    "  - Relay (relay-runtime 21) buatan Meta menggabungkan kebutuhan",
                    "    data tiap komponen lewat fragment dan compiler. Kuat, tapi",
                    "    kurva belajarnya tinggi.",
                    "  - urql (versi 5) lebih ringan dan disusun dari potongan yang",
                    "    disebut exchange.",
                    "",
                    "Redux Toolkit juga punya RTK Query untuk server state, dibahas",
                    "di materi berikutnya.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Marketplace menampilkan jumlah keranjang di header dan di halaman",
                    "checkout sekaligus. Aplikasi seperti itu memakai cache query",
                    "supaya angkanya selalu sama tanpa permintaan ganda.",
                    "",
                    "Kasus kecil: halaman detail produk kadang menampilkan produk",
                    "sebelumnya selama sedetik setelah pengguna pindah dari produk 42 ke",
                    "produk 7.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Buka useQuery-nya dan bandingkan queryKey dengan isi queryFn.",
                    "  2. Kalau kuncinya ['produk'] padahal queryFn memakai id, ganti",
                    "     jadi:",
                    "       queryKey: ['produk', id]",
                    "  3. Pasang React Query Devtools untuk melihat isi cache. Sekarang",
                    "     tiap produk punya entri sendiri.",
                    "  4. Pastikan queryFn mengecek res.ok dan melempar error kalau",
                    "     gagal, supaya isPending dan error bekerja semestinya.",
                ],
            },
        ],
    },
    {
        "title": "27. Client State: Redux Toolkit, Zustand, dan Jotai",
        "sections": [
            {
                "body": [
                    "Sesudah server state diurus TanStack Query, sisa state global di",
                    "kebanyakan aplikasi ternyata kecil: isi keranjang sebelum checkout,",
                    "panel yang terbuka, pilihan filter. Untuk itu ada tiga tingkat",
                    "solusi. Pertama, angkat state ke induk bersama dan kirim lewat",
                    "props. Kedua, Context kalau datanya jarang berubah. Ketiga, pustaka",
                    "state saat banyak komponen di tempat berjauhan membaca dan mengubah",
                    "data yang sering berubah.",
                    "",
                    "Materi ini membahas tingkat ketiga. Jangan memasangnya cuma karena",
                    "tutorial memasangnya; tiap pustaka menambah konsep yang harus",
                    "dipahami semua orang di tim.",
                ],
            },
            {
                "heading": "Redux dan Redux Toolkit",
                "code": """import { configureStore, createSlice } from '@reduxjs/toolkit';

const keranjangSlice = createSlice({
  name: 'keranjang',
  initialState: { items: [] },
  reducers: {
    tambah(state, action) {
      state.items.push(action.payload);   // boleh, karena ada Immer
    },
    kosongkan(state) {
      state.items = [];
    },
  },
});

export const { tambah, kosongkan } = keranjangSlice.actions;

export const store = configureStore({
  reducer: { keranjang: keranjangSlice.reducer },
});

store.dispatch(tambah('Kopi'));
console.log(store.getState().keranjang.items);""",
            },
            {
                "body": [
                    "Redux menyimpan seluruh state global di satu store. State hanya",
                    "bisa diubah dengan mengirim action (objek seperti",
                    "{ type: 'keranjang/tambah', payload: 'Kopi' }) ke reducer, yaitu",
                    "fungsi murni yang menerima state lama dan action lalu mengembalikan",
                    "state baru. Karena tiap perubahan lewat satu jalur, kamu bisa",
                    "melacak siapa mengubah apa di Redux DevTools.",
                    "",
                    "Redux Toolkit (2.13.0, inti redux 5.0.1) adalah cara resmi menulis",
                    "Redux sekarang. createSlice membuat reducer dan action sekaligus,",
                    "dan berkat pustaka Immer kamu boleh menulis state.items.push()",
                    "yang kelihatannya memutasi, padahal Immer membuatkan salinan baru.",
                    "RTK Query di dalamnya mengurus pengambilan data seperti TanStack",
                    "Query. Di React, store dibaca dengan useSelector dan diubah dengan",
                    "useDispatch.",
                    "",
                    "Jebakan: tutorial lama memakai createStore, connect, dan",
                    "mapStateToProps, dengan reducer switch yang panjang. Kode",
                    "perusahaan masih banyak begitu, jadi kamu perlu bisa membacanya,",
                    "tapi tulisan baru pakai configureStore dan hooks. Latihan bab ini",
                    "memintamu membangun createStore sendiri supaya mesinnya jelas.",
                ],
            },
            {
                "heading": "Store ringan ala Zustand",
                "code": """// Store ringan ala Zustand dalam belasan baris.
function create(pembuat) {
  let state;
  const pendengar = new Set();
  const get = () => state;
  const set = (sebagian) => {
    const ubah = typeof sebagian === 'function' ? sebagian(state) : sebagian;
    state = { ...state, ...ubah };          // digabung, bukan diganti
    pendengar.forEach((f) => f(state));
  };
  state = pembuat(set, get);
  return {
    getState: get,
    subscribe(f) {
      pendengar.add(f);
      return () => pendengar.delete(f);
    },
  };
}

const keranjang = create((set) => ({
  items: [],
  tambah: (barang) => set((s) => ({ items: [...s.items, barang] })),
  kosongkan: () => set({ items: [] }),
}));

const lepas = keranjang.subscribe((s) =>
  console.log(`Header: ${s.items.length} barang`)
);

keranjang.getState().tambah('Kopi');
keranjang.getState().tambah('Roti');
lepas();
keranjang.getState().kosongkan();
console.log('Isi akhir:', JSON.stringify(keranjang.getState().items));""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  Header: 1 barang",
                    "  Header: 2 barang",
                    "  Isi akhir: []",
                    "",
                    "Sesudah lepas() dipanggil, header nggak diberi tahu lagi, jadi",
                    "pengosongan terakhir nggak mencetak apa-apa. Itu yang terjadi saat",
                    "komponen dilepas dari layar.",
                ],
            },
            {
                "heading": "Zustand dan Jotai di React",
                "bahasa": "jsx",
                "code": """// Zustand: satu store, dibaca lewat hook
import { create } from 'zustand';

const useKeranjang = create((set) => ({
  items: [],
  tambah: (barang) => set((s) => ({ items: [...s.items, barang] })),
}));

function IkonKeranjang() {
  const jumlah = useKeranjang((s) => s.items.length);  // selector
  return <span>{jumlah}</span>;
}

// Jotai: state dipecah jadi atom kecil
import { atom, useAtom, useAtomValue } from 'jotai';

const hargaAtom = atom(18000);
const jumlahAtom = atom(2);
const totalAtom = atom((get) => get(hargaAtom) * get(jumlahAtom));

function Total() {
  const total = useAtomValue(totalAtom);
  const [jumlah, setJumlah] = useAtom(jumlahAtom);
  return <button onClick={() => setJumlah(jumlah + 1)}>Total Rp{total}</button>;
}""",
            },
            {
                "body": [
                    "Zustand (5.0.15) adalah versi asli dari program tadi, plus hook",
                    "untuk React. Store dibuat dengan satu fungsi, tanpa Provider dan",
                    "tanpa action bernama. Selector (s) => s.items.length membuat",
                    "komponen cuma dirender ulang kalau angka itu berubah. Populer untuk",
                    "proyek baru yang butuh state global sederhana sampai menengah.",
                    "",
                    "Jotai (baru rilis versi 3) memecah state jadi atom: potongan kecil",
                    "yang bisa diturunkan dari atom lain, mirip computed di bab 3.",
                    "Cocok kalau state-mu banyak dan saling bergantung, misalnya editor",
                    "dengan puluhan panel.",
                ],
            },
            {
                "heading": "Peta pustaka state lainnya",
                "bahasa": "teks",
                "code": """Pustaka     Ide utama                  Status         Pilih kalau
MobX 7      objek observable           stabil-matang  suka model OOP
Recoil      atom (Meta)                usang          jangan, pakai Jotai
XState 5    mesin status, statechart   aktif          alur rumit
Valtio 2    Proxy, ubah objek langsung stabil-matang  gaya mutasi
Nano Stores store mini lintas framework aktif         island Astro""",
            },
            {
                "body": [
                    "MobX membuat objek jadi observable; komponen yang membacanya",
                    "otomatis diperbarui. Konsepnya sama dengan reaktivitas Vue di bab",
                    "8. Recoil adalah pustaka atom eksperimental dari Meta yang nggak",
                    "rilis lagi sejak Maret 2023 dan repositorinya diarsipkan awal 2025;",
                    "masih muncul di tutorial lama, jangan dipakai untuk proyek baru.",
                    "",
                    "XState menulis perilaku sebagai status dan transisi yang jelas,",
                    "misalnya keranjang -> alamat -> bayar -> selesai, sehingga status",
                    "mustahil (bayar tanpa alamat) nggak bisa terjadi. Bagus untuk",
                    "checkout, wizard formulir, dan pemutar media. Valtio dari tim",
                    "Poimandres (pembuat Zustand dan Jotai) memakai Proxy seperti",
                    "reactive() di bab 3. Nano Stores kecil sekali dan nggak terikat",
                    "framework; dokumentasi Astro memakainya untuk berbagi state antar",
                    "island.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aplikasi perbankan dan dasbor perusahaan yang dibangun 2017-2021",
                    "banyak memakai Redux klasik. Proyek baru lebih sering memasangkan",
                    "TanStack Query untuk data server dengan Zustand untuk sisa state",
                    "kecilnya.",
                    "",
                    "Kasus kecil: proyekmu memakai Redux, dan separuh isi store ternyata",
                    "salinan data API (daftar produk, profil) beserta flag loading dan",
                    "error yang ditulis manual untuk tiap permintaan.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Kelompokkan isi store: mana salinan data server, mana state",
                    "     milik browser.",
                    "  2. Pindahkan data server ke RTK Query (kalau ingin tetap di",
                    "     Redux) atau TanStack Query. Flag loading dan error ikut",
                    "     hilang, karena pustaka itu yang mengurusnya.",
                    "  3. Sisakan di store hanya state klien, misalnya:",
                    "       { keranjang: [...], panelTerbuka: false }",
                    "  4. Kalau sisanya tinggal sedikit, pertimbangkan mengganti Redux",
                    "     dengan Zustand. Kalau tim nyaman dengan Redux, biarkan saja.",
                ],
            },
        ],
    },
    {
        "title": "28. Form dan Validasi: React Hook Form dan Zod",
        "sections": [
            {
                "body": [
                    "Formulir kelihatannya gampang, sampai kamu menulis yang sungguhan:",
                    "sepuluh kolom, pesan error per kolom, tombol yang mati saat",
                    "mengirim, nilai bawaan dari server, dan aturan seperti \"konfirmasi",
                    "sandi harus sama\". Kalau tiap kolom punya useState sendiri dan",
                    "tiap ketikan merender ulang seluruh form, halaman jadi berat.",
                    "",
                    "Ada dua alat yang biasanya dipakai bersama. Pustaka skema",
                    "menjelaskan bentuk data yang sah. Pustaka form mengurus input,",
                    "error, dan pengiriman, lalu meminjam skema itu untuk validasi.",
                ],
            },
            {
                "heading": "Zod: satu skema untuk validasi dan tipe",
                "bahasa": "typescript",
                "code": """import { z } from 'zod';

export const SkemaDaftar = z.object({
  nama: z.string().min(3, 'Nama minimal 3 huruf'),
  email: z.email('Format email salah'),
  umur: z.number().int().min(15, 'Minimal 15 tahun'),
  kota: z.string().optional(),
});

// Tipe TypeScript diturunkan dari skema, nggak ditulis dua kali.
export type Daftar = z.infer<typeof SkemaDaftar>;

const hasil = SkemaDaftar.safeParse({ nama: 'Al', email: 'al@', umur: 14 });
if (!hasil.success) {
  for (const masalah of hasil.error.issues) {
    console.log(masalah.path.join('.'), masalah.message);
  }
}
// nama Nama minimal 3 huruf
// email Format email salah
// umur Minimal 15 tahun""",
            },
            {
                "body": [
                    "Zod adalah pustaka skema paling populer: di State of JS 2025 ia",
                    "nomor satu di daftar pustaka dengan 5.241 pemakai. Versi terbarunya",
                    "saat materi ini ditulis (Oktober 2026) adalah 4.6.7. Zod 4 lebih",
                    "cepat dan lebih kecil dari versi 3, dan validator format seperti",
                    "z.email() sekarang berdiri sendiri (di Zod 3 ditulis",
                    "z.string().email()).",
                    "",
                    "Dua hal yang membuat Zod berguna. safeParse nggak melempar error;",
                    "ia mengembalikan { success, data } atau { success: false, error }",
                    "dengan daftar masalah beserta jalurnya (path), jadi kamu tahu kolom",
                    "mana yang salah. Dan z.infer membuat tipe TypeScript dari skema,",
                    "jadi tipe dan aturan validasi nggak pernah selisih. Skema yang sama",
                    "bisa dipakai di server untuk memeriksa kiriman form.",
                ],
            },
            {
                "heading": "React Hook Form dengan Zod",
                "bahasa": "tsx",
                "code": """import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { SkemaDaftar, type Daftar } from './skema';

export function FormDaftar() {
  const {
    register,
    handleSubmit,
    formState: { errors, isSubmitting },
  } = useForm<Daftar>({ resolver: zodResolver(SkemaDaftar) });

  async function kirim(data: Daftar) {
    await fetch('/api/daftar', { method: 'POST', body: JSON.stringify(data) });
  }

  return (
    <form onSubmit={handleSubmit(kirim)}>
      <label htmlFor="nama">Nama</label>
      <input id="nama" {...register('nama')} aria-invalid={!!errors.nama} />
      {errors.nama && <p role="alert">{errors.nama.message}</p>}

      <label htmlFor="umur">Umur</label>
      <input id="umur" type="number" {...register('umur', { valueAsNumber: true })} />
      {errors.umur && <p role="alert">{errors.umur.message}</p>}

      <button disabled={isSubmitting}>Daftar</button>
    </form>
  );
}""",
            },
            {
                "body": [
                    "React Hook Form (7.90.0) adalah pilihan utama untuk form React.",
                    "Cepatnya datang dari input tak terkontrol (uncontrolled): nilai",
                    "tetap tinggal di elemen DOM, bukan di state React, jadi mengetik",
                    "nggak merender ulang seluruh form. register('nama') menghasilkan",
                    "props (name, ref, onChange, onBlur) untuk ditempel ke input.",
                    "handleSubmit menjalankan validasi dulu, dan kirim baru dipanggil",
                    "kalau semua lolos. zodResolver menyambungkan skema Zod ke form.",
                    "",
                    "Perhatikan valueAsNumber: nilai input selalu teks, padahal skema",
                    "meminta number. Tanpa opsi itu, umur selalu ditolak. Atribut",
                    "aria-invalid dan role=\"alert\" membuat pembaca layar ikut",
                    "mengumumkan error (bab 2).",
                    "",
                    "Jebakan: validasi di browser cuma untuk kenyamanan pengguna. Orang",
                    "bisa mengirim data langsung ke API tanpa membuka formmu, jadi",
                    "server wajib memvalidasi lagi. Untungnya skema Zod yang sama bisa",
                    "dipakai di sana.",
                ],
            },
            {
                "heading": "Formik, Yup, dan Valibot",
                "body": [
                    "Formik (2.4.9) adalah pustaka form generasi sebelumnya yang memakai",
                    "input terkontrol. Rilisnya jarang dan React Hook Form lebih banyak",
                    "dipilih sekarang, tapi kamu akan menemuinya di proyek lama. Ia",
                    "biasanya berpasangan dengan Yup (1.7.1), pustaka skema klasik yang",
                    "mirip Zod tapi kalah populer (1.325 pemakai di State of JS 2025).",
                    "",
                    "Valibot (1.5.0) adalah alternatif Zod yang modular: tiap",
                    "validator adalah fungsi terpisah, jadi tree-shaking bisa membuang",
                    "yang nggak dipakai dan bundelnya jauh lebih kecil. Pilih Valibot",
                    "kalau ukuran bundel jadi prioritas, misalnya widget yang",
                    "disisipkan ke situs orang lain. Zod dan Valibot sama-sama",
                    "mengikuti spesifikasi Standard Schema, jadi banyak pustaka form",
                    "menerima keduanya.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Formulir pendaftaran, checkout, dan panel admin hampir selalu",
                    "memakai pasangan pustaka form dan skema. Di aplikasi full-stack",
                    "TypeScript, skemanya ditaruh di satu berkas yang di-import frontend",
                    "dan backend sekaligus.",
                    "",
                    "Kasus kecil: form pendaftaran menolak setiap umur dengan pesan",
                    "\"Invalid input: expected number, received string\", padahal",
                    "pengguna mengetik 17.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Baca pesannya: skema meminta number, yang datang string.",
                    "  2. Ingat bahwa nilai input HTML selalu teks, termasuk",
                    "     type=\"number\".",
                    "  3. Tambahkan opsi konversi saat mendaftarkan input:",
                    "       {...register('umur', { valueAsNumber: true })}",
                    "  4. Atau ubah di skema dengan z.coerce.number(), yang mengubah",
                    "     teks jadi angka sebelum diperiksa.",
                    "  5. Coba kirim lagi dengan umur 14 untuk memastikan pesan",
                    "     \"Minimal 15 tahun\" tetap muncul.",
                ],
            },
        ],
    },
    {
        "title": "29. Vue: Template dan Reaktivitas",
        "sections": [
            {
                "body": [
                    "Vue.js adalah framework untuk membangun antarmuka web. Template-nya",
                    "mirip HTML biasa, dan sistem reaktivitasnya gampang dibayangkan:",
                    "ubah datanya, tampilannya ikut berubah. Vue dibuat Evan You dan",
                    "pertama dirilis tahun 2014. Ia menyebut dirinya progresif, artinya",
                    "bisa dipakai sedikit (satu widget di halaman lama) atau penuh",
                    "(aplikasi besar dengan router, store, dan render di server).",
                    "",
                    "Versi stabil terbaru saat materi ini ditulis (Oktober 2026) adalah",
                    "3.5.44, berlisensi MIT. Di Survei Stack Overflow 2025 Vue dipakai",
                    "17,6% responden, dan di State of JS 2025 ia framework nomor dua",
                    "setelah React. Vue banyak dipakai di Asia dan di ekosistem",
                    "Laravel (PHP). Vue 2 sudah berhenti didukung sejak 31 Desember",
                    "2023, jadi tutorial yang memakai new Vue({ el: '#app' }) sudah",
                    "ketinggalan.",
                ],
            },
            {
                "heading": "Komponen pertama",
                "bahasa": "vue",
                "code": """<script setup>
import { ref, computed } from 'vue';

const nama = ref('Rina');
const jumlah = ref(1);
const harga = 18000;
const total = computed(() => jumlah.value * harga);
</script>

<template>
  <h1>Halo, {{ nama }}!</h1>
  <input v-model="nama" />
  <button @click="jumlah++">Tambah kopi</button>
  <p>{{ jumlah }} x Rp{{ harga }} = Rp{{ total }}</p>
  <p v-if="total > 50000">Gratis ongkir!</p>
</template>""",
            },
            {
                "body": [
                    "Bagian <script setup> berisi data dan logika. Bagian <template>",
                    "berisi tampilan. Isian {{ }} menampilkan nilai dan otomatis",
                    "di-escape, jadi teks seperti <b> dari pengguna nggak dianggap tag.",
                    "Atribut berawalan v- disebut directive:",
                    "",
                    "  - v-bind:src atau singkatnya :src mengikat atribut ke data.",
                    "  - v-on:click atau singkatnya @click memasang event.",
                    "  - v-model mengikat dua arah: ketikan di input mengubah data,",
                    "    data berubah mengubah isi input.",
                    "  - v-if, v-else-if, v-else menampilkan elemen bersyarat. v-show",
                    "    cuma menyembunyikannya dengan CSS.",
                    "  - v-for=\"p in produk\" mengulang elemen, wajib dengan :key=\"p.id\"",
                    "    karena alasan yang sama dengan key di React.",
                    "",
                    "Di template kamu menulis jumlah, bukan jumlah.value. Vue membuka",
                    "bungkus ref secara otomatis di sana. Di dalam <script>, .value",
                    "tetap wajib.",
                ],
            },
            {
                "heading": "Kenapa ada .value",
                "body": [
                    "JavaScript nggak bisa memberi tahu siapa pun saat variabel biasa",
                    "dibaca atau diubah. Vue akali dengan membungkus nilai di dalam",
                    "objek yang punya getter dan setter value. Program di bawah adalah",
                    "versi mini ref dan watchEffect, sejalan dengan signal yang kamu",
                    "bangun di bab 3.",
                ],
            },
            {
                "heading": "ref mini",
                "code": """// ref mini: nilai dibungkus objek supaya pembacaan dan penulisannya
// bisa dicegat lewat getter dan setter .value
let efekAktif = null;

function ref(awal) {
  const pelanggan = new Set();
  let nilai = awal;
  return {
    get value() {
      if (efekAktif) pelanggan.add(efekAktif);   // catat siapa yang membaca
      return nilai;
    },
    set value(baru) {
      if (baru === nilai) return;                 // sama, nggak usah apa-apa
      nilai = baru;
      pelanggan.forEach((f) => f());              // jalankan ulang pembacanya
    },
  };
}

function watchEffect(fn) {
  efekAktif = fn;
  fn();
  efekAktif = null;
}

const jumlah = ref(1);
const harga = ref(18000);

watchEffect(() => console.log(`Total: Rp${jumlah.value * harga.value}`));

jumlah.value = 3;
harga.value = 20000;
jumlah.value = 3;          // nilainya sama, efek nggak jalan

let salinan = jumlah.value; // cuma angka biasa
salinan = 10;               // nggak memicu apa pun
console.log('jumlah masih', jumlah.value);""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  Total: Rp18000",
                    "  Total: Rp54000",
                    "  Total: Rp60000",
                    "  jumlah masih 3",
                    "",
                    "Begitu efek membaca jumlah.value, getter mencatat efek itu sebagai",
                    "pelanggan. Saat jumlah.value diganti, setter menjalankan ulang semua",
                    "pelanggannya. Menyalin nilainya ke variabel biasa memutus hubungan",
                    "itu. Vue asli juga menunda pembaruan DOM ke satu antrean, jadi tiga",
                    "perubahan berturut-turut cuma menghasilkan satu render.",
                    "",
                    "Untuk objek, ada reactive(). Ia memakai Proxy, persis seperti",
                    "reactive() di bab 3, sehingga state.jumlah++ langsung terlacak",
                    "tanpa .value.",
                    "",
                    "Jebakan: const { jumlah } = reactive({ jumlah: 1 }) menghasilkan",
                    "angka biasa yang nggak reaktif lagi, sama seperti salinan di",
                    "program tadi. Kalau perlu memecah objek reaktif, pakai toRefs().",
                    "Banyak tim memilih ref untuk semuanya supaya aturannya cuma satu.",
                ],
            },
            {
                "heading": "computed dan watch",
                "bahasa": "vue",
                "code": """<script setup>
import { ref, computed, watch } from 'vue';

const kata = ref('');
const produk = ref([
  { id: 1, nama: 'Kopi susu' },
  { id: 2, nama: 'Teh tarik' },
]);

// computed: nilai turunan, disimpan sampai sumbernya berubah
const hasil = computed(() =>
  produk.value.filter((p) => p.nama.toLowerCase().includes(kata.value.toLowerCase()))
);

// watch: efek samping saat sesuatu berubah
watch(kata, (baru) => {
  localStorage.setItem('kata-terakhir', baru);
});
</script>

<template>
  <input v-model="kata" placeholder="Cari menu" />
  <ul>
    <li v-for="p in hasil" :key="p.id">{{ p.nama }}</li>
  </ul>
</template>""",
            },
            {
                "body": [
                    "Pakai computed untuk nilai yang bisa dihitung dari data lain. Ia",
                    "disimpan (cache) dan baru dihitung ulang kalau sumbernya berubah.",
                    "Pakai watch untuk efek samping: menyimpan ke localStorage, memanggil",
                    "API, menulis log. watchEffect mirip watch tapi melacak sendiri apa",
                    "yang dibaca, seperti program ref mini tadi.",
                    "",
                    "Jebakan: mengisi data lewat watch padahal bisa computed, misalnya",
                    "watch(produk, () => { jumlahProduk.value = produk.value.length }).",
                    "Itu sama dengan jebakan useEffect di React: kerja dua kali tanpa",
                    "perlu.",
                ],
            },
            {
                "heading": "Options API dan Composition API",
                "bahasa": "vue",
                "code": """<!-- Gaya Options API: masih sah di Vue 3 -->
<script>
export default {
  data() {
    return { jumlah: 1, harga: 18000 };
  },
  computed: {
    total() {
      return this.jumlah * this.harga;
    },
  },
  methods: {
    tambah() {
      this.jumlah++;
    },
  },
};
</script>

<template>
  <button @click="tambah">{{ jumlah }} kopi, Rp{{ total }}</button>
</template>""",
            },
            {
                "body": [
                    "Vue punya dua gaya menulis komponen. Options API (di atas)",
                    "mengelompokkan kode menurut jenisnya: data, computed, methods. Ia",
                    "gaya Vue 2 dan masih banyak di tutorial serta kode lama.",
                    "Composition API (dengan <script setup>) mengelompokkan kode menurut",
                    "fiturnya dan memudahkan logika dipakai ulang lewat composable.",
                    "Dokumentasi Vue menyarankan Composition API untuk proyek baru;",
                    "keduanya tetap didukung penuh dan boleh dicampur.",
                    "",
                    "Vue juga sedang menyiapkan mode Vapor, yang mengompilasi template",
                    "langsung jadi perintah DOM tanpa virtual DOM. Menurut data npm saat",
                    "materi ini ditulis, mode itu belum masuk rilis stabil.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Panel admin toko online, sistem informasi sekolah, dan aplikasi",
                    "Laravel dengan Inertia sering memakai Vue karena template-nya",
                    "terasa dekat dengan HTML yang sudah dikenal tim backend.",
                    "",
                    "Kasus kecil: kotak pencarian temanmu nggak menyaring apa pun.",
                    "Kodenya menyimpan const { kata } = reactive({ kata: '' }) lalu",
                    "memakai kata di dalam computed.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Kenali jebakannya: destrukturisasi mengambil nilai saat itu",
                    "     saja, jadi kata cuma teks kosong biasa.",
                    "  2. Ganti dengan ref: const kata = ref('');",
                    "  3. Di computed, baca kata.value. Di template tetap tulis",
                    "     v-model=\"kata\".",
                    "  4. Buka Vue DevTools di browser dan lihat nilai kata berubah",
                    "     setiap kamu mengetik.",
                ],
            },
        ],
    },
    {
        "title": "30. Vue Composition API dan Komponen Satu Berkas",
        "sections": [
            {
                "body": [
                    "Komponen Vue biasanya ditulis sebagai SFC (single-file component),",
                    "yaitu berkas .vue yang menyatukan tiga hal: <template> untuk",
                    "tampilan, <script setup> untuk logika, dan <style> untuk gaya.",
                    "Browser nggak bisa membaca .vue langsung; plugin @vitejs/plugin-vue",
                    "yang mengubahnya jadi JavaScript dan CSS saat dev maupun build.",
                    "",
                    "Cara resmi memulai proyek Vue adalah npm create vue@latest. Ia",
                    "menanyakan apakah kamu mau TypeScript, Vue Router, Pinia, dan alat",
                    "uji, lalu menyiapkan proyek Vite lengkap.",
                ],
            },
            {
                "heading": "KartuProduk.vue",
                "bahasa": "vue",
                "code": """<script setup lang="ts">
const props = defineProps<{
  nama: string;
  harga: number;
  stok?: number;
}>();

const emit = defineEmits<{
  tambah: [nama: string, jumlah: number];
}>();

function pesan() {
  emit('tambah', props.nama, 1);
}
</script>

<template>
  <article class="kartu">
    <h3>{{ nama }}</h3>
    <p>Rp{{ harga }}</p>
    <p v-if="stok === 0">Habis</p>
    <button :disabled="stok === 0" @click="pesan">Tambah</button>
    <slot name="catatan" />
  </article>
</template>

<style scoped>
.kartu { padding: 1rem; border: 1px solid #ddd; }
</style>""",
            },
            {
                "body": [
                    "defineProps menyatakan data yang diterima dari induk; dengan",
                    "lang=\"ts\" tipenya ditulis langsung sebagai generic. defineEmits",
                    "menyatakan event yang boleh dikirim ke atas. Keduanya nggak perlu",
                    "di-import, karena compiler Vue yang mengenalinya. <style scoped>",
                    "membuat CSS-nya cuma berlaku untuk komponen ini; Vue menambahkan",
                    "atribut unik ke elemennya supaya pemilih .kartu nggak bocor ke",
                    "komponen lain.",
                    "",
                    "Sejak Vue 3.5, kamu juga boleh menulis",
                    "const { nama, harga } = defineProps<...>() dan hasilnya tetap",
                    "reaktif. Di versi sebelumnya, cara itu memutus reaktivitas.",
                ],
            },
            {
                "heading": "Props turun, event naik",
                "bahasa": "vue",
                "code": """<script setup>
import { ref } from 'vue';
import KartuProduk from './KartuProduk.vue';

const keranjang = ref([]);
const daftar = [
  { id: 1, nama: 'Kopi', harga: 18000, stok: 5 },
  { id: 2, nama: 'Teh', harga: 12000, stok: 0 },
];

function masukkan(nama, jumlah) {
  keranjang.value.push({ nama, jumlah });
}
</script>

<template>
  <p>Keranjang: {{ keranjang.length }} barang</p>
  <KartuProduk
    v-for="p in daftar"
    :key="p.id"
    :nama="p.nama"
    :harga="p.harga"
    :stok="p.stok"
    @tambah="masukkan"
  >
    <template #catatan>
      <small>Harga sudah termasuk pajak</small>
    </template>
  </KartuProduk>
</template>""",
            },
            {
                "body": [
                    "Aliran datanya sama dengan React. Induk mengirim data ke anak lewat",
                    "props (:nama=\"p.nama\"). Anak nggak mengubah props, tapi mengirim",
                    "event (@tambah) dan induk yang memutuskan apa yang terjadi. Slot",
                    "adalah lubang untuk isi dari induk, padanan children di React.",
                    "<slot /> tanpa nama adalah slot bawaan, dan <slot name=\"catatan\" />",
                    "diisi lewat <template #catatan>.",
                    "",
                    "Untuk komponen input buatan sendiri, Vue 3.4 ke atas punya",
                    "defineModel(): satu baris yang membuat v-model bekerja pada",
                    "komponenmu, tanpa menulis props dan emit secara manual.",
                ],
            },
            {
                "heading": "Composable: logika yang dipakai ulang",
                "code": """// src/composables/useHitungMundur.js
import { ref, computed, onUnmounted } from 'vue';

export function useHitungMundur(detikAwal) {
  const sisa = ref(detikAwal);
  const habis = computed(() => sisa.value <= 0);
  const id = setInterval(() => {
    if (sisa.value > 0) sisa.value--;
  }, 1000);
  onUnmounted(() => clearInterval(id));
  return { sisa, habis };
}

// Di komponen mana pun:
// const { sisa, habis } = useHitungMundur(60);""",
            },
            {
                "body": [
                    "Composable adalah fungsi biasa yang memakai ref, computed, dan hook",
                    "siklus hidup (onMounted, onUnmounted), lalu mengembalikan hasilnya.",
                    "Namanya diawali use, sama seperti custom hook di React. Bedanya,",
                    "fungsi setup Vue cuma jalan sekali per komponen, jadi composable",
                    "boleh dipanggil di dalam if tanpa masalah urutan.",
                    "",
                    "VueUse adalah kumpulan lebih dari 200 composable siap pakai,",
                    "versinya 15.0.0 (September 2026). Beberapa yang sering dipakai:",
                    "useMouse (posisi kursor), useLocalStorage (ref yang tersimpan di",
                    "localStorage), useFetch, useDark, dan useIntersectionObserver.",
                    "Sebelum menulis composable sendiri, cek dulu apakah VueUse sudah",
                    "punya.",
                    "",
                    "Jebakan: composable yang memakai onUnmounted harus dipanggil di",
                    "dalam <script setup> secara langsung, bukan di dalam setTimeout",
                    "atau sesudah await. Vue perlu tahu komponen mana yang sedang",
                    "dibuat saat hook itu didaftarkan.",
                ],
            },
            {
                "heading": "Siklus hidup dan ref ke elemen",
                "body": [
                    "Kode di <script setup> jalan sekali, saat komponen dibuat. Saat",
                    "itu elemen DOM-nya belum ada. Kalau kamu perlu menyentuh DOM,",
                    "misalnya memberi fokus ke input atau memasang pustaka grafik,",
                    "lakukan di onMounted. Bersihkan timer dan pendengar event di",
                    "onUnmounted. Ada juga onUpdated untuk sesudah DOM diperbarui,",
                    "tapi jarang perlu.",
                    "",
                    "Untuk memegang elemen, Vue 3.5 punya useTemplateRef:",
                    "",
                    "  const kotak = useTemplateRef('kotakCari');",
                    "  onMounted(() => kotak.value.focus());",
                    "",
                    "lalu di template tulis <input ref=\"kotakCari\" />. Kode yang",
                    "lebih lama membuat const kotakCari = ref(null) dengan nama yang",
                    "sama persis dengan atribut ref; cara itu masih jalan.",
                    "",
                    "Bandingkan dengan React: di sana fungsi komponen dipanggil ulang",
                    "tiap render, jadi kamu memikirkan daftar dependensi useEffect. Di",
                    "Vue, setup jalan sekali dan reaktivitas yang melacak dependensinya,",
                    "jadi nggak ada daftar dependensi yang harus kamu jaga.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aplikasi Vue skala menengah, seperti dasbor penjualan atau sistem",
                    "reservasi, biasanya punya puluhan SFC dan satu folder composables",
                    "untuk logika yang dipakai di banyak halaman: format rupiah,",
                    "paginasi, status login.",
                    "",
                    "Kasus kecil: di tiga halaman berbeda ada kode yang sama persis",
                    "untuk menyimpan pilihan tema ke localStorage dan membacanya lagi.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pindahkan kodenya ke src/composables/useTema.js yang",
                    "     mengembalikan { tema, gantiTema }.",
                    "  2. Atau pakai yang sudah jadi dari VueUse:",
                    "       const tema = useLocalStorage('tema', 'terang');",
                    "  3. Ganti kode di tiga halaman dengan satu baris pemanggilan.",
                    "  4. Kalau nilainya perlu dibagi ke seluruh aplikasi, pindahkan",
                    "     ke store Pinia (materi berikutnya).",
                ],
            },
        ],
    },
    {
        "title": "31. Pinia, Vue Router, dan Peta Ekosistem Vue",
        "sections": [
            {
                "body": [
                    "Vue inti sengaja kecil. Router, store, dan pustaka komponen datang",
                    "dari paket terpisah. Dua di antaranya dirawat tim Vue sendiri dan",
                    "hampir selalu ikut: Pinia untuk state global dan Vue Router untuk",
                    "halaman. Sisanya pilihan, dan materi ini memetakannya.",
                ],
            },
            {
                "heading": "Pinia",
                "code": """// src/stores/keranjang.js
import { defineStore } from 'pinia';
import { ref, computed } from 'vue';

export const useKeranjangStore = defineStore('keranjang', () => {
  const items = ref([]);
  const total = computed(() => items.value.reduce((n, b) => n + b.harga, 0));

  function tambah(barang) {
    items.value.push(barang);
  }

  return { items, total, tambah };
});

// Di komponen:
// const keranjang = useKeranjangStore();
// keranjang.tambah({ nama: 'Kopi', harga: 18000 });
// const { items, total } = storeToRefs(keranjang);""",
            },
            {
                "body": [
                    "Pinia adalah store resmi Vue. Store di atas ditulis dengan gaya",
                    "setup: ref jadi state, computed jadi getter, fungsi jadi action.",
                    "Ada juga gaya options (state, getters, actions) yang mirip Options",
                    "API. Pinia terhubung ke Vue DevTools, jadi tiap perubahan state",
                    "terlihat. Versi terbarunya saat materi ini ditulis (Oktober 2026)",
                    "adalah 4.1.0. Pinia 4 rilis Juli 2026, dan perubahannya bersifat",
                    "teknis (misalnya cuma terbit sebagai ES Module), jadi API yang",
                    "kamu pakai sehari-hari nyaris sama dengan versi sebelumnya.",
                    "",
                    "Jebakan: const { items } = useKeranjangStore() memutus reaktivitas,",
                    "sama seperti destrukturisasi reactive(). Pakai storeToRefs() untuk",
                    "state dan getter; action boleh diambil langsung.",
                    "",
                    "Vuex adalah store resmi generasi lama, dengan state, mutations,",
                    "actions, dan getters. Versi terakhirnya 4.1.0 dari 2022, dan tim Vue",
                    "menyarankan Pinia. Kamu akan menemuinya di proyek Vue 2 warisan;",
                    "jangan dipilih untuk proyek baru.",
                ],
            },
            {
                "heading": "Vue Router",
                "code": """// src/router.js
import { createRouter, createWebHistory } from 'vue-router';
import Beranda from './views/Beranda.vue';

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', component: Beranda },
    { path: '/produk/:id', component: () => import('./views/DetailProduk.vue') },
    { path: '/admin', component: () => import('./views/Admin.vue'),
      meta: { butuhLogin: true } },
    { path: '/:jalur(.*)*', component: () => import('./views/TidakAda.vue') },
  ],
});

router.beforeEach((ke) => {
  if (ke.meta.butuhLogin && !sudahLogin()) return '/';
});

export default router;""",
            },
            {
                "body": [
                    "Vue Router memetakan alamat ke komponen. Di template, <RouterLink",
                    "to=\"/produk/1\"> membuat tautan tanpa memuat ulang halaman, dan",
                    "<RouterView /> adalah tempat komponen halaman dirender. Di dalam",
                    "komponen, useRoute().params.id membaca parameter. Rute dengan",
                    "() => import(...) dimuat saat dibuka saja (code splitting dari bab",
                    "5). beforeEach adalah guard navigasi: jalan sebelum tiap",
                    "perpindahan dan bisa mengalihkan, misalnya ke halaman login.",
                    "",
                    "Versi terbarunya 5.4.0. Vue Router 5 adalah rilis transisi yang",
                    "memasukkan routing berbasis berkas (dulu paket terpisah",
                    "unplugin-vue-router) ke paket utamanya. Untuk pengguna versi 4 yang",
                    "nggak memakai routing berbasis berkas, nggak ada perubahan yang",
                    "merusak. Versi 6 nanti direncanakan cuma ES Module dan membuang API",
                    "yang sudah usang.",
                ],
            },
            {
                "heading": "Peta pustaka komponen dan form",
                "bahasa": "teks",
                "code": """Pustaka           Untuk                        Status
Vuetify 4         komponen Material Design     aktif
Element Plus 2    komponen panel admin         aktif
PrimeVue 5        komponen lengkap (PrimeTek)  aktif
Quasar 2          satu kode: web, mobile, desktop  aktif
VeeValidate 4     validasi form                stabil-matang
FormKit 2         kerangka form + skema        aktif
Vuelidate 2       validasi berbasis model      menurun
Vuex 4            store lama                   usang""",
            },
            {
                "body": [
                    "Vuetify adalah pustaka komponen Material Design terbesar untuk Vue,",
                    "sekarang di versi 4. Element Plus, penerus Element UI dari zaman",
                    "Vue 2, umum sekali di panel admin, terutama di Tiongkok dan Asia",
                    "Tenggara. PrimeVue datang dari PrimeTek, yang juga membuat",
                    "PrimeReact untuk React dan PrimeNG untuk Angular; PrimeNG termasuk",
                    "pustaka komponen utama di dunia Angular.",
                    "",
                    "Quasar lebih dari pustaka komponen. Ia framework di atas Vue yang",
                    "bisa menghasilkan SPA, situs SSR, PWA, aplikasi ponsel (lewat",
                    "Capacitor atau Cordova), dan aplikasi desktop (lewat Electron) dari",
                    "satu kode.",
                    "",
                    "Untuk form, VeeValidate (4.15) adalah pilihan yang paling dikenal",
                    "dan bisa memakai skema Zod atau Yup. FormKit menyatukan input,",
                    "validasi, dan form yang dibangun dari skema JSON, cocok untuk form",
                    "panjang yang strukturnya datang dari server. Vuelidate (2.0.3)",
                    "nggak rilis lagi sejak 2023; temui di kode lama, pilih yang lain",
                    "untuk proyek baru.",
                    "",
                    "Masih ada dua anggota keluarga yang dibahas di bab lain: Nuxt,",
                    "meta-framework Vue untuk render di server (bab 12), dan Vue Test",
                    "Utils untuk menguji komponen (bab 11).",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Panel admin berbasis Vue umumnya memakai kombinasi Vue Router,",
                    "Pinia, dan satu pustaka komponen seperti Element Plus atau Vuetify,",
                    "sehingga tabel, dialog, dan form tinggal dirakit.",
                    "",
                    "Kasus kecil: kamu mewarisi aplikasi Vue 2 dengan Vuex dan diminta",
                    "menambah fitur keranjang baru. Atasanmu ingin kode baru sudah siap",
                    "untuk migrasi ke Vue 3.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Catat versi yang terpasang di package.json. Vue 2 sudah",
                    "     berhenti didukung sejak akhir 2023, jadi migrasi memang perlu.",
                    "  2. Tulis store baru dengan Pinia. Pinia versi 2 masih mendukung",
                    "     Vue 2, sedangkan versi baru hanya Vue 3, jadi cek tabel",
                    "     dukungan di dokumentasinya sebelum memasang.",
                    "  3. Biarkan modul Vuex lama tetap jalan berdampingan. Pindahkan",
                    "     satu modul per pekan, mulai dari yang paling kecil.",
                    "  4. Sesudah Vuex kosong, hapus paketnya, lalu lanjutkan migrasi",
                    "     Vue 2 ke Vue 3 dengan panduan resmi.",
                ],
            },
        ],
    },
    {
        "title": "32. Angular: Komponen Standalone, Template, dan Signals",
        "sections": [
            {
                "body": [
                    "Angular adalah framework buatan Google yang datang lengkap: router,",
                    "formulir, klien HTTP, dependency injection, alat uji, dan CLI",
                    "sudah ada dalam satu paket resmi. React dan Vue menyerahkan pilihan",
                    "itu ke kamu; Angular sudah memutuskannya. Akibatnya proyek Angular",
                    "di perusahaan mana pun strukturnya mirip, dan itu yang dicari tim",
                    "besar seperti bank, perusahaan asuransi, dan instansi pemerintah.",
                    "",
                    "Versi stabil terbaru saat materi ini ditulis (Oktober 2026) adalah",
                    "22.2.3. Angular 22 rilis 3 Juni 2026, dan Angular 21 (19 November",
                    "2025) sekarang berstatus LTS. Tiap versi major didukung 24 bulan:",
                    "12 bulan aktif, lalu 12 bulan hanya perbaikan penting. Selama",
                    "bertahun-tahun Angular merilis major tiap enam bulan; halaman",
                    "rilis resminya sekarang menulis jadwal satu major per tahun.",
                    "",
                    "Di Survei Stack Overflow 2025 Angular dipakai 18,2% responden, dan",
                    "di State of JS 2025 ia framework nomor tiga. Angular wajib memakai",
                    "TypeScript, jadi selesaikan kurikulum TypeScript dulu.",
                    "",
                    "Ingat: Angular berbeda total dari AngularJS (versi 1.x, 2010).",
                    "Namanya mirip, kodenya sama sekali lain. AngularJS dibahas di",
                    "materi ketiga bab ini.",
                ],
            },
            {
                "heading": "Angular CLI",
                "bahasa": "terminal",
                "code": """npm install -g @angular/cli
ng new toko-angular
cd toko-angular
ng serve
ng generate component kartu-produk""",
            },
            {
                "body": [
                    "Angular CLI (perintah ng) membuat proyek, menjalankan dev server di",
                    "http://localhost:4200, membuat kerangka komponen dan service, serta",
                    "menjalankan build dan tes. ng update membantu naik versi sambil",
                    "menyunting kode yang terdampak secara otomatis. Di belakang layar,",
                    "build-nya memakai esbuild dan dev server Vite.",
                ],
            },
            {
                "heading": "Komponen dengan signals",
                "bahasa": "typescript",
                "code": """import { Component, computed, input, output, signal } from '@angular/core';

@Component({
  selector: 'app-kartu-produk',
  template: `
    <h3>{{ nama() }}</h3>
    <p>{{ jumlah() }} x Rp{{ harga() }} = Rp{{ total() }}</p>
    <button (click)="tambah()">Tambah</button>
    @if (total() > 50000) {
      <p>Gratis ongkir!</p>
    }
  `,
})
export class KartuProduk {
  nama = input.required<string>();
  harga = input(0);
  dipesan = output<number>();

  jumlah = signal(1);
  total = computed(() => this.jumlah() * this.harga());

  tambah() {
    this.jumlah.update((j) => j + 1);
    this.dipesan.emit(this.jumlah());
  }
}""",
            },
            {
                "body": [
                    "Komponen Angular adalah class TypeScript dengan dekorator",
                    "@Component. selector adalah nama tag untuk memakainya:",
                    "<app-kartu-produk>. Template boleh ditulis di dalamnya atau di",
                    "berkas .html terpisah lewat templateUrl.",
                    "",
                    "Signal adalah konsep yang sudah kamu bangun di bab 3. signal(1)",
                    "membuat nilai yang dibaca dengan memanggilnya (jumlah()) dan diubah",
                    "dengan set() atau update(). computed() menurunkan nilai dari signal",
                    "lain, dan effect() menjalankan efek samping saat signal yang",
                    "dibacanya berubah. input() dan output() menggantikan dekorator",
                    "@Input dan @Output yang lama; input juga berupa signal, jadi dibaca",
                    "dengan harga().",
                    "",
                    "Komponen di atas nggak menulis standalone: true. Sejak Angular 19,",
                    "semua komponen standalone secara bawaan: ia meng-import sendiri apa",
                    "yang dipakainya lewat medan imports, tanpa NgModule.",
                ],
            },
            {
                "heading": "Sintaks template",
                "bahasa": "angular",
                "code": """<input [(ngModel)]="kata" placeholder="Cari menu" />

<ul>
  @for (p of produk(); track p.id) {
    <li [class.habis]="p.stok === 0" (click)="pilih(p)">{{ p.nama }}</li>
  } @empty {
    <li>Belum ada produk.</li>
  }
</ul>

@if (dipilih(); as p) {
  <app-kartu-produk [nama]="p.nama" [harga]="p.harga" (dipesan)="catat($event)" />
} @else {
  <p>Pilih produk dulu.</p>
}

@defer (on viewport) {
  <app-ulasan />
} @placeholder {
  <p>Ulasan dimuat saat terlihat.</p>
}""",
            },
            {
                "body": [
                    "Empat bentuk pengikatan perlu kamu hafal:",
                    "",
                    "  - {{ ekspresi }} menampilkan nilai sebagai teks.",
                    "  - [properti]=\"ekspresi\" mengikat properti elemen atau input",
                    "    komponen.",
                    "  - (event)=\"pernyataan\" memasang event; $event berisi datanya.",
                    "  - [(ngModel)]=\"nilai\" mengikat dua arah, dari modul formulir.",
                    "",
                    "Alur kontrol ditulis dengan blok: @if, @else, @for, @switch, dan",
                    "@defer. @for wajib punya track, padanan key di React dan Vue.",
                    "@defer menunda pemuatan sebagian template, misalnya sampai bagian",
                    "itu terlihat di layar.",
                    "",
                    "Jebakan: tutorial lama menulis *ngIf=\"...\" dan *ngFor=\"...\" sebagai",
                    "atribut. Itu masih jalan di proyek lama, tapi kode baru memakai",
                    "@if dan @for, dan ng update bisa mengubahnya otomatis.",
                ],
            },
            {
                "heading": "Zoneless: tanpa Zone.js",
                "body": [
                    "Dulu Angular memakai pustaka Zone.js yang menyadap setTimeout,",
                    "event, dan Promise di seluruh halaman. Setiap kali ada yang selesai,",
                    "Angular memeriksa ulang semua komponen untuk mencari yang berubah.",
                    "Cara itu otomatis tapi boros, dan membuat bundel lebih besar.",
                    "",
                    "Dengan signals, Angular tahu persis nilai mana yang berubah dan",
                    "komponen mana yang membacanya. Deteksi perubahan tanpa Zone.js",
                    "(zoneless) stabil sejak Angular 20.2 dan jadi bawaan proyek baru",
                    "sejak Angular 21. Proyek lama yang masih butuh Zone.js bisa",
                    "menyalakannya kembali dengan provideZoneChangeDetection().",
                ],
            },
            {
                "heading": "Angular lama dan Angular sekarang",
                "bahasa": "teks",
                "code": """Tutorial lama (sampai 2023)    Angular sekarang
NgModule + declarations        komponen standalone
*ngIf, *ngFor, *ngSwitch       @if, @for, @switch
@Input(), @Output()            input(), output(), model()
properti biasa + Zone.js       signal(), computed(), zoneless
constructor(private x: X)      x = inject(X)
Karma + Jasmine                Vitest
Reactive Forms saja            Signal Forms (stabil di v22)""",
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Sistem internal bank, aplikasi klaim asuransi, dan portal layanan",
                    "pemerintahan banyak yang memakai Angular, karena puluhan developer",
                    "bisa bekerja di satu kode dengan aturan yang sama. Akibatnya banyak",
                    "lowongan Angular berupa merawat aplikasi yang sudah berjalan",
                    "bertahun-tahun.",
                    "",
                    "Kasus kecil: kamu ditugasi menambah halaman ke proyek Angular 15",
                    "yang penuh NgModule dan *ngIf, dan timnya ingin kode baru memakai",
                    "gaya modern.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Naikkan versinya bertahap dengan ng update, satu major sekali",
                    "     jalan, sambil menjalankan tes tiap langkah.",
                    "  2. Jalankan migrasi kontrol alur bawaan CLI:",
                    "       ng generate @angular/core:control-flow",
                    "  3. Tulis halaman baru sebagai komponen standalone dengan",
                    "     signal(), input(), dan @if.",
                    "  4. Biarkan modul lama jalan berdampingan; pindahkan satu per",
                    "     satu saat disentuh, jangan sekaligus.",
                ],
            },
        ],
    },
    {
        "title": "33. Dependency Injection, Service, dan RxJS di Angular",
        "sections": [
            {
                "body": [
                    "Bayangkan dapur restoran. Koki nggak berangkat ke pasar sendiri tiap",
                    "butuh bawang; bahan diantar pemasok, dan koki tinggal memakainya.",
                    "Dependency injection memakai ide yang sama: komponen menyebut apa",
                    "yang ia butuhkan, dan Angular yang membuat serta mengantarkannya.",
                    "",
                    "Yang diantar biasanya service, yaitu class berisi logika yang",
                    "dipakai banyak komponen: memanggil API, menyimpan keranjang,",
                    "mencatat log. Komponen jadi fokus ke tampilan, dan saat diuji,",
                    "service aslinya bisa ditukar dengan versi palsu.",
                ],
            },
            {
                "heading": "Service dan inject()",
                "bahasa": "typescript",
                "code": """import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export type Produk = { id: number; nama: string; harga: number };

@Injectable({ providedIn: 'root' })
export class LayananProduk {
  private http = inject(HttpClient);

  ambilSemua(): Observable<Produk[]> {
    return this.http.get<Produk[]>('/api/produk');
  }
}

// Di komponen mana pun:
// private layanan = inject(LayananProduk);""",
            },
            {
                "body": [
                    "@Injectable({ providedIn: 'root' }) mendaftarkan service ke injector",
                    "akar. Artinya satu instans dipakai bersama di seluruh aplikasi",
                    "(singleton), dan kalau nggak ada yang memakainya, ia dibuang dari",
                    "bundel. inject() mengambil dependensi; kode lama melakukannya lewat",
                    "parameter constructor, dan hasilnya sama.",
                    "",
                    "Injector Angular bertingkat. Kalau sebuah komponen menulis",
                    "providers: [LayananProduk] di dekoratornya, komponen itu dan",
                    "anak-anaknya mendapat instans baru tersendiri. Saat inject()",
                    "dipanggil, Angular mencari mulai dari injector terdekat lalu naik",
                    "ke atas sampai akar.",
                    "",
                    "HttpClient sendiri didaftarkan sekali di konfigurasi aplikasi:",
                    "",
                    "  export const appConfig = {",
                    "    providers: [provideRouter(routes), provideHttpClient()],",
                    "  };",
                ],
            },
            {
                "heading": "RxJS dan Observable",
                "body": [
                    "Perhatikan bahwa http.get() nggak mengembalikan Promise. Ia",
                    "mengembalikan Observable dari pustaka RxJS. Observable adalah aliran",
                    "nilai yang datang dari waktu ke waktu: bisa nol, satu, atau banyak",
                    "nilai, lalu selesai atau gagal. Promise selalu tepat satu nilai.",
                    "Aliran itu baru berjalan saat ada yang subscribe, dan bisa",
                    "dihentikan dengan unsubscribe, termasuk membatalkan permintaan",
                    "HTTP yang masih berjalan.",
                    "",
                    "Kekuatan RxJS ada di operator, fungsi yang mengubah aliran dan",
                    "dirangkai dengan pipe(). Versi RxJS saat ini 7.8.2 (Februari 2025),",
                    "berlisensi Apache-2.0.",
                ],
            },
            {
                "heading": "Kotak pencarian dengan operator",
                "bahasa": "typescript",
                "code": """import { Component, inject } from '@angular/core';
import { toSignal } from '@angular/core/rxjs-interop';
import { FormControl, ReactiveFormsModule } from '@angular/forms';
import { debounceTime, distinctUntilChanged, switchMap, catchError, of } from 'rxjs';
import { LayananCari } from './layanan-cari';

@Component({
  selector: 'app-cari',
  imports: [ReactiveFormsModule],
  template: `
    <input [formControl]="kata" placeholder="Cari produk" />
    @for (p of hasil(); track p.id) { <p>{{ p.nama }}</p> }
  `,
})
export class Cari {
  private layanan = inject(LayananCari);
  kata = new FormControl('', { nonNullable: true });

  hasil = toSignal(
    this.kata.valueChanges.pipe(
      debounceTime(300),
      distinctUntilChanged(),
      switchMap((q) => this.layanan.cari(q).pipe(catchError(() => of([])))),
    ),
    { initialValue: [] },
  );
}""",
            },
            {
                "body": [
                    "Baca pipeline-nya dari atas:",
                    "",
                    "  - debounceTime(300): tunggu sampai pengguna berhenti mengetik",
                    "    300 milidetik, baru teruskan nilainya.",
                    "  - distinctUntilChanged(): buang nilai yang sama dengan nilai",
                    "    sebelumnya.",
                    "  - switchMap(...): untuk tiap kata, mulai permintaan baru dan",
                    "    batalkan permintaan sebelumnya yang belum selesai. Jawaban lama",
                    "    nggak akan menimpa jawaban baru.",
                    "  - catchError(() => of([])): kalau server gagal, kirim daftar",
                    "    kosong supaya aliran nggak mati.",
                    "",
                    "toSignal mengubah Observable jadi signal untuk template dan",
                    "mengurus unsubscribe saat komponen dihancurkan. Program di bawah",
                    "menghitung efek dua operator pertama pada deretan ketikan.",
                ],
            },
            {
                "heading": "debounceTime pada garis waktu",
                "code": """// Ketikan pengguna di kotak cari: [milidetik, isi kotak]
const ketikan = [
  [0, 'k'], [120, 'ko'], [250, 'kop'], [900, 'kopi'],
  [1000, 'kopi '], [1100, 'kopi s'], [1800, 'kopi s'],
];

// debounceTime(300): kirim nilai kalau 300 ms berlalu tanpa ketikan baru.
function debounce(peristiwa, jeda) {
  const keluar = [];
  peristiwa.forEach(([t, v], i) => {
    const berikut = peristiwa[i + 1];
    if (!berikut || berikut[0] - t >= jeda) keluar.push([t + jeda, v]);
  });
  return keluar;
}

// distinctUntilChanged(): buang nilai yang sama dengan nilai sebelumnya.
function distinct(peristiwa) {
  return peristiwa.filter(([, v], i) => i === 0 || v !== peristiwa[i - 1][1]);
}

const hasil = distinct(debounce(ketikan, 300));
console.log(`Ketikan: ${ketikan.length}, permintaan ke API: ${hasil.length}`);
for (const [t, v] of hasil) console.log(`  t=${t} ms  GET /api/cari?q=${encodeURIComponent(v)}`);""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  Ketikan: 7, permintaan ke API: 2",
                    "    t=550 ms  GET /api/cari?q=kop",
                    "    t=1400 ms  GET /api/cari?q=kopi%20s",
                    "",
                    "Tujuh peristiwa jadi dua permintaan. Ketikan cepat k, ko, kop",
                    "dirangkum jadi kop. Peristiwa terakhir (pengguna menekan panah,",
                    "isinya tetap kopi s) dibuang distinctUntilChanged karena sama",
                    "dengan yang sudah dikirim.",
                    "",
                    "Angular sedang menggeser sebagian peran RxJS ke signals. Menurut",
                    "roadmap resminya, API resource dan httpResource (data async dalam",
                    "bentuk signal) serta Signal Forms sudah dinyatakan siap produksi",
                    "pada 2026. RxJS tetap dipakai untuk aliran event yang rumit, dan",
                    "kamu akan menemuinya di hampir semua kode Angular yang ada.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Kotak pencarian dengan saran otomatis di aplikasi Angular hampir",
                    "selalu memakai rangkaian debounceTime, distinctUntilChanged, dan",
                    "switchMap. Tanpa itu, tiap huruf jadi satu permintaan dan servernya",
                    "kewalahan.",
                    "",
                    "Kasus kecil: kotak cari di aplikasi kantormu kadang menampilkan",
                    "hasil untuk kata yang lebih pendek dari yang terakhir diketik,",
                    "misalnya hasil \"ko\" padahal kotaknya berisi \"kopi\".",
                    "",
                    "Cara memecahkannya:",
                    "  1. Cari pipeline-nya. Kemungkinan besar memakai mergeMap atau",
                    "     subscribe bersarang, sehingga jawaban lama yang datang",
                    "     belakangan menimpa yang baru.",
                    "  2. Ganti dengan switchMap supaya permintaan lama dibatalkan:",
                    "       switchMap((q) => this.layanan.cari(q))",
                    "  3. Tambahkan debounceTime(300) dan distinctUntilChanged() di",
                    "     depannya untuk mengurangi permintaan.",
                    "  4. Buka tab Network di DevTools, ketik cepat, dan pastikan",
                    "     permintaan lama ditandai canceled.",
                ],
            },
        ],
    },
    {
        "title": "34. Peta Ekosistem Angular: NgRx, Material, dan Analog",
        "sections": [
            {
                "body": [
                    "Karena Angular sudah membawa banyak hal sendiri, ekosistemnya lebih",
                    "ramping dibanding React. Yang paling sering kamu temui: pustaka",
                    "state, pustaka komponen, satu meta-framework, dan warisan",
                    "AngularJS yang masih hidup di banyak perusahaan.",
                ],
            },
            {
                "heading": "Ringkasan",
                "bahasa": "teks",
                "code": """Pustaka            Peran                         Status
NgRx 22            state ala Redux + Signal Store aktif
NGXS 22            state berbasis class          aktif
Elf 2.5            state reaktif berbasis RxJS   menurun
Angular Material   komponen resmi + CDK          aktif
Angular Aria       perilaku aksesibel tanpa gaya aktif
PrimeNG            komponen lengkap (PrimeTek)   aktif
Analog 2           meta-framework berbasis Vite  aktif
AngularJS 1.8      framework generasi pertama    usang""",
            },
            {
                "heading": "Pustaka state",
                "bahasa": "typescript",
                "code": """import { signalStore, withState, withMethods, patchState } from '@ngrx/signals';

export const KeranjangStore = signalStore(
  { providedIn: 'root' },
  withState({ items: [] as string[] }),
  withMethods((store) => ({
    tambah(barang: string) {
      patchState(store, { items: [...store.items(), barang] });
    },
  })),
);

// Di komponen: store = inject(KeranjangStore); store.items() untuk membaca.""",
            },
            {
                "body": [
                    "NgRx adalah pustaka state paling umum di Angular. Bentuk klasiknya",
                    "(@ngrx/store) memakai pola Redux: action, reducer, selector, dan",
                    "effect untuk efek samping berbasis RxJS. Bentuk barunya, Signal",
                    "Store (@ngrx/signals, contoh di atas), memakai signals dan jauh",
                    "lebih ringkas. Versinya mengikuti Angular, sekarang 22.",
                    "",
                    "NGXS (22.0) memakai class dan dekorator, jadi boilerplate-nya lebih",
                    "sedikit dari NgRx klasik. Elf (2.5.1) dari komunitas ngneat,",
                    "penerus Akita, berbasis RxJS; ia nggak rilis lagi sejak Februari",
                    "2024, jadi pertimbangkan pilihan lain untuk proyek baru.",
                    "",
                    "Sebelum memasang salah satunya, ingat bahwa service dengan beberapa",
                    "signal sudah cukup untuk banyak aplikasi. Pustaka state baru",
                    "berguna saat banyak tim menyentuh state yang sama dan butuh aturan",
                    "yang ketat.",
                ],
            },
            {
                "heading": "Pustaka komponen",
                "body": [
                    "Angular Material adalah pustaka komponen resmi tim Angular",
                    "berbasis Material Design, dirilis bersamaan dengan Angular (versi",
                    "22.2.3). Di dalamnya ada CDK (Component Dev Kit): perilaku tanpa",
                    "gaya seperti drag and drop, overlay, dan daftar virtual yang bisa",
                    "kamu beri tampilan sendiri.",
                    "",
                    "Angular Aria (@angular/aria) diperkenalkan di Angular 21 sebagai",
                    "pratinjau dan dinyatakan stabil di Angular 22. Isinya directive",
                    "tanpa gaya yang menerapkan pola ARIA dari W3C: navigasi papan ketik,",
                    "atribut ARIA, dan pengelolaan fokus, bekal yang sama dengan bab 2.",
                    "",
                    "PrimeNG dari PrimeTek (kembaran PrimeVue di bab 8) menyediakan",
                    "puluhan komponen siap pakai, termasuk tabel data yang lengkap, dan",
                    "populer di aplikasi perusahaan.",
                ],
            },
            {
                "heading": "Analog",
                "body": [
                    "Analog adalah meta-framework untuk Angular, padanan Next.js untuk",
                    "React. Ia dibangun di atas Vite dan menyediakan render di server",
                    "(SSR), situs statis (SSG), routing berbasis berkas, dan halaman",
                    "dari Markdown. Versinya 2.8.1. Pemakainya masih kecil, tapi ia",
                    "tercantum di daftar utama meta-framework State of JS 2025. Angular",
                    "sendiri juga punya SSR resmi lewat ng add @angular/ssr.",
                ],
            },
            {
                "heading": "AngularJS: warisan yang masih hidup",
                "bahasa": "html",
                "code": """<div ng-app="toko" ng-controller="KeranjangCtrl">
  <p>{{ items.length }} barang, total Rp{{ total() }}</p>
  <button ng-click="tambah('Kopi', 18000)">Tambah kopi</button>
</div>
<script>
  angular.module('toko', []).controller('KeranjangCtrl', function ($scope) {
    $scope.items = [];
    $scope.tambah = function (nama, harga) {
      $scope.items.push({ nama: nama, harga: harga });
    };
    $scope.total = function () {
      return $scope.items.reduce(function (n, b) { return n + b.harga; }, 0);
    };
  });
</script>""",
            },
            {
                "body": [
                    "AngularJS adalah generasi pertama Angular dari tahun 2010, dengan",
                    "two-way binding lewat $scope dan pemeriksaan ulang berkala yang",
                    "disebut digest loop. Angular modern (versi 2 ke atas) ditulis ulang",
                    "dari nol dan nggak kompatibel. Dukungan resmi AngularJS berakhir 31",
                    "Desember 2021, versi terakhirnya 1.8.3, dan paket npm-nya ditandai",
                    "deprecated.",
                    "",
                    "Meski begitu, di Survei Stack Overflow 2025 AngularJS masih dipakai",
                    "7,2% responden, sama banyaknya dengan Svelte. Ciri yang gampang",
                    "dikenali: atribut ng-app, ng-controller, ng-click, dan variabel",
                    "$scope. Kalau kamu melihatnya, itu kode warisan, dan jangan",
                    "memakainya untuk apa pun yang baru. Celah keamanannya nggak lagi",
                    "ditambal pembuatnya.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Banyak aplikasi internal yang dibangun 2013-2016 masih memakai",
                    "AngularJS karena memindahkannya butuh biaya besar. Perusahaan",
                    "biasanya memigrasinya bertahap sambil aplikasinya tetap dipakai.",
                    "",
                    "Kasus kecil: kamu magang di tim yang merawat dasbor AngularJS, dan",
                    "diminta membuat halaman laporan baru tanpa menambah kode AngularJS.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pastikan dulu versinya: cari angular.module dan ng-app di",
                    "     kodenya, lalu cek package.json atau tag script-nya.",
                    "  2. Buat halaman baru sebagai aplikasi Angular modern terpisah.",
                    "  3. Kalau keduanya harus tampil di satu halaman, pelajari paket",
                    "     resmi @angular/upgrade yang menjalankan AngularJS dan Angular",
                    "     berdampingan, atau pisahkan per alamat (/laporan diarahkan ke",
                    "     aplikasi baru).",
                    "  4. Pindahkan halaman lama satu per satu, mulai dari yang paling",
                    "     jarang berubah, sampai AngularJS bisa dicabut.",
                ],
            },
        ],
    },
    {
        "title": "35. Svelte 5: Komponen dan Runes",
        "sections": [
            {
                "body": [
                    "Svelte adalah framework UI yang bekerja sebagai compiler. React",
                    "dan Vue membawa pustaka ke browser, lalu pustaka itu yang",
                    "menghitung bagian halaman mana yang berubah. Svelte mengerjakan",
                    "sebagian besar hitungan itu waktu build. Berkas .svelte yang kamu",
                    "tulis diubah jadi JavaScript biasa yang langsung mengubah DOM, jadi",
                    "nggak ada virtual DOM yang dibandingkan di browser.",
                    "",
                    "Gampangnya begini. Virtual DOM di bab 03 itu seperti membandingkan",
                    "dua foto ruangan untuk mencari barang yang pindah. Svelte sudah",
                    "tahu dari awal barang mana yang bisa pindah, karena compiler-nya",
                    "membaca kodemu. Jadi waktu angka berubah, yang disentuh cuma satu",
                    "simpul teks itu.",
                    "",
                    "Versi stabil terbaru saat materi ini ditulis (Oktober 2026) adalah",
                    "Svelte 5.57.2, lisensi MIT. Di Survei Stack Overflow 2025, Svelte",
                    "dipakai 7,2% responden. Angkanya jauh di bawah React, tapi Svelte",
                    "konsisten masuk daftar utama State of JS dan rilisnya sering.",
                ],
            },
            {
                "heading": "Komponen pertama",
                "bahasa": "svelte",
                "code": """<script>
  let jumlah = $state(0);
  let ganda = $derived(jumlah * 2);

  $effect(() => {
    document.title = `Diklik ${jumlah} kali`;
  });
</script>

<button onclick={() => jumlah++}>
  Diklik {jumlah} kali
</button>
<p>Dua kalinya: {ganda}</p>

<style>
  button { font-size: 1.25rem; }
</style>""",
            },
            {
                "heading": "Tiga rune yang paling sering dipakai",
                "body": [
                    "Satu berkas .svelte berisi tiga bagian: script, markup, dan style.",
                    "CSS di dalam style otomatis berlaku untuk komponen itu saja, jadi",
                    "aturan button di atas nggak bocor ke tombol lain di halaman.",
                    "",
                    "Kata yang diawali tanda dolar seperti $state disebut rune. Rune",
                    "kelihatan seperti fungsi, tapi itu tanda untuk compiler.",
                    "Kamu nggak perlu mengimpornya.",
                    "  - $state(nilai) membuat state reaktif. Mengubah jumlah dengan",
                    "    jumlah++ langsung memperbarui semua tempat yang membacanya.",
                    "  - $derived(ekspresi) adalah nilai turunan, mirip computed di bab",
                    "    03. ganda dihitung ulang setiap kali jumlah berubah, dan kamu",
                    "    nggak boleh mengubahnya langsung.",
                    "  - $effect(fungsi) menjalankan efek samping sesudah DOM diperbarui,",
                    "    misalnya mengganti judul tab atau memanggil pustaka grafik.",
                    "    Svelte mencatat state apa saja yang dibaca di dalamnya, lalu",
                    "    menjalankan ulang efeknya kalau salah satu berubah.",
                    "",
                    "Kalau tiga hal itu terasa akrab, memang begitu. Di bab 03 kamu",
                    "menulis signal, computed, dan effect sendiri. Rune adalah versi",
                    "Svelte dari ide yang sama, ditambah compiler yang menuliskan",
                    "pemanggilannya untukmu.",
                    "",
                    "$state pada objek dan array bersifat dalam. Kalau kamu menulis",
                    "let daftar = $state([]) lalu daftar.push('kopi'), tampilan ikut",
                    "berubah. Di baliknya Svelte memakai Proxy, persis yang kamu bangun",
                    "di materi Signal dan Proxy Reaktif dari Nol.",
                ],
            },
            {
                "heading": "Props dan anak komponen",
                "bahasa": "svelte",
                "code": """<!-- KartuMenu.svelte -->
<script>
  let { nama, harga, habis = false, children } = $props();
</script>

<article class:habis>
  <h2>{nama}</h2>
  <p>Rp{harga.toLocaleString('id-ID')}</p>
  {@render children?.()}
</article>

<!-- dipakai di komponen lain -->
<KartuMenu nama="Kopi susu" harga={18000}>
  <p>Favorit pagi hari.</p>
</KartuMenu>""",
            },
            {
                "body": [
                    "Data dari komponen induk masuk lewat $props(). Nilai bawaan cukup",
                    "ditulis di destrukturisasi, seperti habis = false. Isi di antara",
                    "tag pembuka dan penutup komponen datang sebagai children, lalu",
                    "digambar dengan {@render children?.()}. Tanda ?. menjaga supaya",
                    "nggak error kalau induknya nggak mengirim isi apa pun.",
                    "",
                    "Markup Svelte punya blok sendiri untuk logika: {#if}...{:else}",
                    "...{/if} untuk percabangan dan {#each daftar as item (item.id)}",
                    "untuk perulangan. Bagian (item.id) adalah key, alasannya sama",
                    "dengan key di bab 03: supaya Svelte tahu baris mana yang pindah",
                    "dan mana yang baru.",
                    "",
                    "Proyek baru dibuat dengan perintah resmi sv:",
                ],
            },
            {
                "heading": "Membuat proyek",
                "bahasa": "terminal",
                "code": """npx sv create kafe-senja
cd kafe-senja
npm install
npm run dev""",
            },
            {
                "heading": "Tutorial lama sudah basi",
                "body": [
                    "Svelte 5 rilis Oktober 2024 dan mengganti cara menulis",
                    "reaktivitas. Internet masih penuh tutorial Svelte 3 dan 4, dan",
                    "kodenya kelihatan mirip, jadi gampang tertukar. Ciri tutorial lama:",
                    "",
                    "  Svelte 3/4 (lama)          Svelte 5 (sekarang)",
                    "  let jumlah = 0;            let jumlah = $state(0);",
                    "  $: ganda = jumlah * 2;     let ganda = $derived(jumlah * 2);",
                    "  export let nama;           let { nama } = $props();",
                    "  on:click={tambah}          onclick={tambah}",
                    "  <slot />                   {@render children?.()}",
                    "",
                    "Svelte 5 masih bisa menjalankan komponen gaya lama, jadi proyek",
                    "warisan nggak langsung rusak. Tapi jangan mencampur dua gaya di",
                    "satu komponen, dan untuk kode baru pakai rune.",
                    "",
                    "Jebakan: $effect bukan tempat menghitung nilai turunan. Kalau kamu",
                    "menulis $effect(() => { ganda = jumlah * 2 }), hasilnya memang",
                    "jalan, tapi tampilan digambar dua kali dan alurnya susah dilacak.",
                    "Nilai yang bisa dihitung dari state lain selalu pakai $derived.",
                    "",
                    "Kapan memilih Svelte? Untuk tim kecil atau proyek yang butuh",
                    "bundel kecil dan kode ringkas, Svelte enak dipakai. Kalau timmu",
                    "atau lowongan yang kamu incar memakai React, ekosistem dan",
                    "pustaka siap pakai React jauh lebih banyak.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Svelte banyak dipakai untuk dasbor internal, situs berita yang",
                    "butuh grafik interaktif, dan aplikasi kecil yang harus cepat dibuka",
                    "di ponsel murah. Ukuran bundel yang kecil membuat halaman lebih",
                    "cepat interaktif di jaringan seluler yang lambat.",
                    "",
                    "Kasus kecil: kamu mewarisi komponen keranjang belanja Svelte 4.",
                    "Isinya let total = 0, $: pajak = total * 0.11, dan tombol",
                    "on:click. Atasan minta komponennya diperbarui ke Svelte 5 sebelum",
                    "fitur diskon ditambahkan.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Cari semua let di script yang nilainya berubah karena",
                    "     interaksi. Bungkus nilai awalnya dengan $state:",
                    "       let total = $state(0);",
                    "  2. Ganti setiap baris $: yang menghitung nilai dengan $derived:",
                    "       let pajak = $derived(total * 0.11);",
                    "  3. Baris $: yang menjalankan efek samping (misalnya console.log",
                    "     atau menyimpan ke localStorage) dipindah ke $effect.",
                    "  4. Ganti on:click={...} jadi onclick={...} dan export let jadi",
                    "     destrukturisasi $props().",
                    "  5. Jalankan npx sv migrate svelte-5 di cabang git terpisah,",
                    "     bandingkan hasilnya dengan perubahan manualmu, lalu uji",
                    "     tombolnya satu per satu di browser.",
                ],
            },
        ],
    },
    {
        "title": "36. SvelteKit: Rute, Load, dan Form Action",
        "sections": [
            {
                "body": [
                    "Svelte sendiri cuma mengurus komponen. Aplikasi sungguhan butuh",
                    "lebih dari itu: banyak halaman dengan alamat masing-masing, data",
                    "dari database, form yang dikirim ke server, dan halaman yang",
                    "sudah berisi HTML waktu dibuka supaya cepat tampil dan terbaca",
                    "mesin pencari. SvelteKit adalah framework aplikasi resmi Svelte",
                    "yang mengurus semua itu. Jenis alat seperti ini disebut",
                    "meta-framework, dan kamu bakal ketemu saudaranya (Next.js, Nuxt)",
                    "di bab 12.",
                    "",
                    "Versi stabil terbaru saat materi ini ditulis (Oktober 2026) adalah",
                    "SvelteKit 3.1.0, lisensi MIT. Major 3 terbit tahun 2026, jadi",
                    "tutorial SvelteKit 2 masih banyak beredar. Bedanya dibahas di",
                    "bagian akhir materi ini.",
                    "",
                    "Konsep render dari bab 03 dipakai langsung di sini. Secara bawaan",
                    "SvelteKit merender halaman di server (SSR), mengirim HTML-nya,",
                    "lalu menghidupkan halaman itu di browser lewat hydration. Sesudah",
                    "itu perpindahan antarhalaman terjadi di browser seperti SPA.",
                ],
            },
            {
                "heading": "Rute dari nama folder",
                "bahasa": "teks",
                "code": """src/routes/
  +layout.svelte        kerangka semua halaman (nav, footer)
  +page.svelte          ->  /
  tentang/
    +page.svelte        ->  /tentang
  menu/
    +page.server.js     load dan form action untuk /menu
    +page.svelte        ->  /menu
    [id]/
      +page.js          load untuk /menu/7, /menu/12, ...
      +page.svelte      ->  /menu/:id""",
            },
            {
                "body": [
                    "Alamat halaman ditentukan oleh folder di src/routes. Berkas yang",
                    "diawali tanda plus punya arti khusus:",
                    "  - +page.svelte adalah isi halamannya.",
                    "  - +layout.svelte membungkus halaman di folder itu dan semua",
                    "    subfoldernya. Isi halaman muncul di tempat {@render children()}.",
                    "  - +page.js berisi fungsi load yang jalan di server waktu",
                    "    halaman pertama dibuka, lalu di browser waktu pindah halaman.",
                    "  - +page.server.js berisi load dan form action yang hanya jalan",
                    "    di server. Kode yang memegang kata sandi database atau kunci",
                    "    API wajib di sini, karena berkas ini nggak pernah dikirim ke",
                    "    browser.",
                    "",
                    "Folder dalam kurung siku seperti [id] adalah parameter. Alamat",
                    "/menu/7 cocok dengan folder itu, dan angka 7 bisa dibaca sebagai",
                    "params.id di fungsi load.",
                ],
            },
            {
                "heading": "load dan form action di server",
                "code": """// src/routes/menu/+page.server.js
import { fail } from '@sveltejs/kit';
import { daftarMenu, simpanPesanan } from '#lib/server/db.js';

export async function load() {
  return { menu: await daftarMenu() };
}

export const actions = {
  default: async ({ request }) => {
    const data = await request.formData();
    const nama = data.get('nama')?.trim();
    if (!nama) {
      return fail(400, { nama, kosong: true });
    }
    await simpanPesanan(nama);
    return { berhasil: true };
  },
};""",
            },
            {
                "heading": "Halaman yang memakainya",
                "bahasa": "svelte",
                "code": """<!-- src/routes/menu/+page.svelte -->
<script>
  import { enhance } from '$app/forms';
  let { data, form } = $props();
</script>

<h1>Menu</h1>
<ul>
  {#each data.menu as item (item.id)}
    <li><a href="/menu/{item.id}">{item.nama}</a></li>
  {/each}
</ul>

<form method="POST" use:enhance>
  <label>Nama pesanan <input name="nama" value={form?.nama ?? ''}></label>
  <button>Pesan</button>
</form>

{#if form?.kosong}<p role="alert">Nama pesanan wajib diisi.</p>{/if}
{#if form?.berhasil}<p>Pesanan tercatat.</p>{/if}""",
            },
            {
                "heading": "Cara kerjanya",
                "body": [
                    "Objek yang dikembalikan load masuk ke halaman sebagai prop data.",
                    "Jadi data.menu di halaman adalah hasil daftarMenu() di server.",
                    "",
                    "Form action adalah fungsi yang menerima kiriman form. Form di atas",
                    "memakai method POST biasa tanpa atribut action, jadi browser",
                    "mengirimnya ke alamat yang sama, dan SvelteKit memanggil action",
                    "default. Kalau nama kosong, fail(400, ...) mengembalikan status",
                    "400 beserta data yang masuk lagi ke halaman sebagai prop form.",
                    "Karena itu input bisa diisi ulang dengan form?.nama dan pesan",
                    "galat bisa ditampilkan.",
                    "",
                    "Hebatnya, form ini tetap jalan walaupun JavaScript di browser",
                    "gagal dimuat. Browser mengirim form secara klasik, server",
                    "mengembalikan halaman baru. use:enhance cuma menambah kenyamanan:",
                    "kalau JavaScript ada, pengiriman terjadi di latar belakang dan",
                    "halamannya nggak berkedip. Pola ini disebut progressive",
                    "enhancement, artinya dasar yang jalan dulu, lalu dipercantik.",
                    "",
                    "Setiap halaman juga bisa memilih mode rendernya sendiri lewat",
                    "ekspor di +page.js: prerender = true membuat halaman jadi HTML",
                    "statis waktu build (SSG), sedangkan ssr = false membuat halaman",
                    "itu dirender di browser saja (CSR). Ke mana aplikasinya dipasang",
                    "diatur adapter: adapter-node untuk server sendiri, adapter-static",
                    "untuk hosting statis, dan adapter khusus untuk Vercel, Netlify,",
                    "atau Cloudflare.",
                ],
            },
            {
                "heading": "Yang berubah di SvelteKit 3",
                "body": [
                    "Kalau tutorial yang kamu baca masih SvelteKit 2, perhatikan",
                    "perubahan ini (dari panduan migrasi resmi):",
                    "  - SvelteKit 3 butuh Svelte 5.57.1 ke atas, Vite 8, TypeScript 6,",
                    "    dan Node 22.17 ke atas.",
                    "  - Berkas svelte.config.js nggak dipakai lagi. Konfigurasi pindah",
                    "    ke vite.config.js sebagai opsi plugin sveltekit().",
                    "  - Alias $lib diganti #lib, memakai subpath imports bawaan Node",
                    "    di package.json. Contoh di atas sudah memakainya.",
                    "  - $app/stores diganti $app/state, dan modul $env diganti",
                    "    $app/env/private serta $app/env/public.",
                    "",
                    "Dokumentasi resmi juga menyebut remote functions, cara baru",
                    "memanggil server dari komponen yang masih eksperimental. Form",
                    "action tetap didukung penuh, jadi aman dipelajari lebih dulu.",
                    "",
                    "Jebakan: kode di +page.js jalan di dua tempat. Kalau kamu membaca",
                    "localStorage atau window di sana, halaman pertama gagal dirender",
                    "di server karena server nggak punya window. Hal yang hanya ada di",
                    "browser taruh di $effect di dalam komponen.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Pola folder rute, fungsi load, dan form action dipakai untuk",
                    "aplikasi seperti sistem reservasi, panel admin toko, dan situs",
                    "dokumentasi. Halaman yang isinya jarang berubah di-prerender jadi",
                    "HTML statis, halaman yang butuh data terbaru dirender per",
                    "permintaan.",
                    "",
                    "Kasus kecil: kafe tempat PKL-mu minta halaman /reservasi. Pengunjung",
                    "mengisi nama dan jam, lalu melihat pesan berhasil. Jam yang kosong",
                    "harus ditolak dengan pesan yang jelas, dan form harus tetap jalan",
                    "di ponsel lama yang JavaScript-nya sering gagal dimuat.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Buat folder src/routes/reservasi berisi +page.svelte dan",
                    "     +page.server.js.",
                    "  2. Di +page.server.js tulis actions.default yang membaca",
                    "     request.formData(), lalu kembalikan fail(400, { nama,",
                    "     jamKosong: true }) kalau jam kosong.",
                    "  3. Di +page.svelte tulis form method=\"POST\" biasa dengan label",
                    "     untuk setiap input, lalu tampilkan pesan galat dari prop form",
                    "     di elemen ber-role alert.",
                    "  4. Matikan JavaScript di DevTools, kirim form kosong, dan pastikan",
                    "     pesan galat tetap muncul. Sesudah itu baru tambahkan",
                    "     use:enhance supaya pengiriman terasa mulus.",
                ],
            },
        ],
    },
    {
        "title": "37. htmx, Alpine.js, dan Hotwire: HTML dari Server",
        "sections": [
            {
                "body": [
                    "Sejauh ini cara kerjanya selalu sama: server mengirim data JSON,",
                    "lalu JavaScript di browser mengubah data itu jadi tampilan. Cara",
                    "ini disebut SPA (single page application). Untungnya interaksi",
                    "terasa cepat. Ruginya, ada dua aplikasi yang harus dirawat: API di",
                    "server dan aplikasi besar di browser, dengan logika yang sering",
                    "tertulis dua kali.",
                    "",
                    "Ada jalan lain yang lebih tua dan sekarang populer lagi: server",
                    "langsung mengirim potongan HTML yang sudah jadi, dan browser",
                    "tinggal menempelkannya. Pendekatan ini disebut hypermedia atau",
                    "HTML over the wire. Logika tetap di server, ditulis dengan bahasa",
                    "apa pun yang kamu kuasai: Python, Go, PHP, atau Ruby. Kurikulum",
                    "backend yang sudah ada di aplikasi ini langsung terpakai.",
                ],
            },
            {
                "heading": "htmx: atribut yang bisa meminta HTML",
                "bahasa": "html",
                "code": """<!doctype html>
<html lang="id">
<head>
  <meta charset="utf-8">
  <title>Kafe Senja</title>
  <script src="/js/htmx.min.js"></script>
</head>
<body>
  <button hx-get="/menu" hx-target="#isi" hx-swap="innerHTML">
    Lihat menu
  </button>
  <div id="isi"></div>

  <form hx-post="/pesan" hx-target="#daftar" hx-swap="beforeend">
    <label>Pesanan <input name="nama"></label>
    <button>Tambah</button>
  </form>
  <ul id="daftar"></ul>
</body>
</html>""",
            },
            {
                "body": [
                    "htmx adalah pustaka kecil yang membuat elemen HTML mana pun bisa",
                    "mengirim permintaan ke server lewat atribut. Versi stabil terbaru",
                    "saat materi ini ditulis (Oktober 2026) adalah 2.0.11, lisensi",
                    "0BSD. Kamu nggak menulis JavaScript sama sekali untuk contoh di",
                    "atas:",
                    "  - hx-get=\"/menu\" artinya: kalau elemen ini diklik, minta GET",
                    "    /menu. Ada juga hx-post, hx-put, hx-patch, dan hx-delete.",
                    "  - hx-target=\"#isi\" memilih elemen yang akan diganti. Tanpa",
                    "    atribut ini, yang diganti elemen itu sendiri.",
                    "  - hx-swap memilih caranya. innerHTML (bawaan) mengganti isi",
                    "    target, outerHTML mengganti seluruh elemen target, beforeend",
                    "    menambah di akhir isi target, afterbegin menambah di awalnya.",
                    "  - hx-trigger mengatur kapan permintaan dikirim, misalnya",
                    "    hx-trigger=\"keyup changed delay:300ms\" untuk kolom cari.",
                    "",
                    "Form di atas mengirim isinya ke /pesan. Server membalas dengan",
                    "satu baris <li>Kopi susu</li>, dan htmx menempelkannya di akhir",
                    "daftar. Server-nya bisa ditulis apa saja. Contoh dengan Flask dari",
                    "kurikulum Python:",
                ],
            },
            {
                "heading": "Server yang mengirim potongan HTML",
                "bahasa": "python",
                "code": """from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

@app.get('/menu')
def menu():
    return '<p>Kopi susu Rp18.000</p><p>Teh melati Rp12.000</p>'

@app.post('/pesan')
def pesan():
    nama = escape(request.form.get('nama', ''))
    return f'<li>{nama}</li>'""",
            },
            {
                "body": [
                    "Perhatikan escape(). Karena server menyusun HTML dari masukan",
                    "pengguna, teks itu wajib di-escape. Tanpa itu, orang bisa mengetik",
                    "<script> di kolom pesanan dan kodenya ikut tertempel di halaman.",
                    "",
                    "Ini yang terjadi di dalam htmx, ditiru dengan JavaScript biasa:",
                ],
            },
            {
                "heading": "Tiruan kecil cara htmx menukar isi",
                "code": "const server = {\n  '/menu': '<p>Kopi susu</p><p>Teh melati</p>',\n};\n\nlet halaman = '<div id=\"isi\"></div>\\n<ul id=\"daftar\"><li>Air</li></ul>';\n\nfunction tukar(html, id, potongan, cara) {\n  const buka = html.indexOf('id=\"' + id + '\"');\n  const awalTag = html.lastIndexOf('<', buka);\n  const tag = html.slice(awalTag + 1, buka).trim();\n  const akhirBuka = html.indexOf('>', buka) + 1;\n  const tutup = html.indexOf('</' + tag + '>', akhirBuka);\n  if (cara === 'beforeend') {\n    return html.slice(0, tutup) + potongan + html.slice(tutup);\n  }\n  return html.slice(0, akhirBuka) + potongan + html.slice(tutup);\n}\n\nhalaman = tukar(halaman, 'isi', server['/menu'], 'innerHTML');\nhalaman = tukar(halaman, 'daftar', '<li>Kopi</li>', 'beforeend');\nconsole.log(halaman);",
            },
            {
                "body": [
                    "Keluaran:",
                    "  <div id=\"isi\"><p>Kopi susu</p><p>Teh melati</p></div>",
                    "  <ul id=\"daftar\"><li>Air</li><li>Kopi</li></ul>",
                    "",
                    "Tiruan ini sengaja disederhanakan: ia mencari tag penutup pertama",
                    "yang namanya sama, jadi gagal kalau target berisi elemen bersarang",
                    "bernama sama, misalnya div di dalam div. Latihan bab ini",
                    "memintamu membuat versi yang lebih lengkap.",
                ],
            },
            {
                "heading": "Alpine.js, Hotwire, dan Inertia.js",
                "body": [
                    "htmx mengurus komunikasi dengan server. Untuk interaksi kecil yang",
                    "nggak butuh server sama sekali, seperti membuka menu tarik turun",
                    "atau menghitung karakter, ada Alpine.js. Versi stabil terbaru saat",
                    "materi ini ditulis (Oktober 2026) adalah 3.17.4, lisensi MIT.",
                    "Alpine ditulis di atribut juga:",
                    "",
                    "  <div x-data=\"{ buka: false }\">",
                    "    <button @click=\"buka = !buka\" :aria-expanded=\"buka\">Menu</button>",
                    "    <ul x-show=\"buka\">...</ul>",
                    "  </div>",
                    "",
                    "x-data membuat state, @click (singkatan x-on:click) menangani",
                    "event, x-show menyembunyikan atau menampilkan elemen. Alpine",
                    "sering dipasangkan dengan htmx, dan populer di ekosistem Laravel",
                    "Livewire.",
                    "",
                    "Hotwire adalah pendekatan HTML over the wire dari Basecamp dan",
                    "jadi bawaan Ruby on Rails. Isinya dua pustaka. Turbo (8.0.23 saat",
                    "materi ini ditulis) membuat klik tautan dan kiriman form nggak",
                    "memuat ulang seluruh halaman, dan lewat <turbo-frame> bisa",
                    "mengganti satu bagian saja. Stimulus (3.2.2) menambah perilaku",
                    "kecil lewat atribut data-controller dan data-action.",
                    "",
                    "Inertia.js (3.9.1) mengambil jalan tengah. Server klasik seperti",
                    "Laravel atau Rails tetap mengurus rute dan data, tapi tampilannya",
                    "ditulis dengan komponen React, Vue, atau Svelte. Kamu dapat rasa",
                    "SPA tanpa menulis API terpisah.",
                    "",
                    "Kapan memilih pendekatan ini? Cocok untuk aplikasi yang sebagian",
                    "besar isinya form dan tabel: panel admin, sistem inventaris, CRUD",
                    "kantor. Kurang cocok untuk aplikasi yang interaktif tanpa",
                    "henti, seperti editor gambar atau aplikasi yang harus jalan",
                    "offline, karena setiap interaksi butuh perjalanan ke server.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aplikasi internal kantor, panel admin toko online, dan sistem",
                    "sekolah banyak yang ditulis dengan Django, Laravel, atau Rails.",
                    "Tim seperti itu sering menambah htmx atau Hotwire supaya halaman",
                    "terasa responsif tanpa harus memindahkan seluruh tampilan ke",
                    "React.",
                    "",
                    "Kasus kecil: halaman daftar siswa di aplikasi sekolah berbasis",
                    "Flask memuat ulang seluruh halaman setiap kali guru mengetik di",
                    "kolom cari. Kamu diminta membuat hasil pencarian muncul sambil",
                    "mengetik, tanpa menulis aplikasi React.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pisahkan bagian tabel ke template sendiri, misalnya",
                    "     _tabel_siswa.html, supaya bisa dirender terpisah.",
                    "  2. Buat rute GET /siswa/cari?q=... yang mengembalikan potongan",
                    "     itu saja, bukan seluruh halaman.",
                    "  3. Pasang atribut di kolom cari:",
                    "       <input name=\"q\" hx-get=\"/siswa/cari\"",
                    "              hx-trigger=\"keyup changed delay:300ms\"",
                    "              hx-target=\"#tabel-siswa\">",
                    "  4. Biarkan form cari tetap punya action biasa, supaya tanpa",
                    "     JavaScript tombol Cari masih bekerja.",
                ],
            },
        ],
    },
    {
        "title": "38. Peta Framework UI: Solid, Preact, Qwik, dan Lainnya",
        "sections": [
            {
                "body": [
                    "React, Vue, Angular, dan Svelte menguasai sebagian besar lowongan.",
                    "Tapi di luar empat itu ada framework lain yang sering kamu dengar,",
                    "dan sebagian idenya dipinjam framework besar. Materi ini peta",
                    "singkat supaya kamu bisa menebak cara kerja framework baru dari",
                    "tiga pertanyaan:",
                    "  - Reaktivitasnya pakai virtual DOM, signal, atau compiler?",
                    "  - JavaScript-nya dikirim semua di awal, sebagian, atau ditunda",
                    "    sampai dibutuhkan?",
                    "  - Statusnya aktif, stabil-matang, atau menurun?",
                    "",
                    "Semua versi di tabel adalah versi stabil terbaru saat materi ini",
                    "ditulis (Oktober 2026).",
                    "",
                    "  Framework  Versi        Ide utama                Status",
                    "  Solid      1.9.17       signal, tanpa VDOM       aktif",
                    "  Preact     11.0.1       React mini, 3 kB         aktif",
                    "  Qwik       1.20.2       resumable                menurun",
                    "  Ember.js   7.3.1        konvensi lengkap         stabil-matang",
                    "  Elm        0.19.3       bahasa fungsional        stabil-matang",
                    "  Mithril.js 2.3.8        SPA mungil               stabil-matang",
                    "  Marko      6.4.6        streaming HTML           aktif",
                    "  Aurelia    2.0.0-rc.2   binding dua arah         menurun",
                    "  Ripple     0.4.7        pendatang baru (TS)      aktif, 0.x",
                    "  Blazor     .NET 10      C# lewat Wasm/server     aktif",
                ],
            },
            {
                "heading": "Solid: signal sungguhan",
                "bahasa": "jsx",
                "code": """import { createSignal, createMemo } from 'solid-js';

function Penghitung() {
  const [jumlah, setJumlah] = createSignal(0);
  const ganda = createMemo(() => jumlah() * 2);
  console.log('fungsi ini jalan sekali saja');

  return (
    <button onClick={() => setJumlah(jumlah() + 1)}>
      {jumlah()} x 2 = {ganda()}
    </button>
  );
}""",
            },
            {
                "body": [
                    "Solid kelihatan seperti React karena memakai JSX, tapi cara",
                    "kerjanya mirip signal yang kamu buat di bab 03. Fungsi komponen",
                    "dijalankan sekali saja. Waktu jumlah berubah, Solid nggak memanggil",
                    "ulang Penghitung. Yang diperbarui cuma simpul teks yang membaca",
                    "jumlah(). Karena itu jumlah ditulis sebagai pemanggilan fungsi:",
                    "membacanya mendaftarkan siapa yang bergantung.",
                    "",
                    "Di State of JS 2025, Solid dipakai sekitar 10% responden dan",
                    "kepuasannya tertinggi lima tahun berturut-turut. Solid 2.0 sedang",
                    "dikembangkan tapi belum stabil. Meta-framework-nya SolidStart.",
                    "",
                    "Preact adalah alternatif React berukuran sekitar 3 kB dengan API",
                    "yang hampir sama. Pustaka React bisa dipakai lewat lapisan",
                    "preact/compat. Preact 11 sudah stabil, dan tim Preact juga",
                    "membuat Preact Signals, salah satu implementasi signal paling",
                    "terkenal. Remix 3 (bab 12) dibangun dari fork Preact.",
                    "",
                    "Qwik membawa ide resumability. Framework lain mengirim HTML dari",
                    "server lalu menjalankan ulang komponen di browser untuk",
                    "menghidupkannya (hydration). Qwik menyimpan keadaan aplikasi di",
                    "dalam HTML, jadi browser bisa melanjutkan tanpa menjalankan ulang",
                    "apa pun. Kode sebuah tombol baru diunduh waktu tombol itu diklik.",
                    "Idenya menarik, tapi menurut State of JS 2025 adopsinya kecil dan",
                    "peringkatnya terus turun. Generasi berikutnya dikembangkan dengan",
                    "nama paket @qwik.dev/core.",
                ],
            },
            {
                "heading": "Elm: bahasa sendiri untuk frontend",
                "bahasa": "elm",
                "code": """type Msg = Tambah | Kurang

update : Msg -> Int -> Int
update msg jumlah =
    case msg of
        Tambah -> jumlah + 1
        Kurang -> jumlah - 1""",
            },
            {
                "heading": "Yang lain, satu per satu",
                "body": [
                    "Elm adalah bahasa fungsional yang dikompilasi ke JavaScript dan",
                    "terkenal dengan janji hampir tanpa error runtime. Pola",
                    "Model-Update-View dari Elm menginspirasi Redux. Setelah jeda",
                    "panjang sejak 0.19.1 (2019), versi 0.19.2 dan 0.19.3 terbit 2026",
                    "tanpa perubahan bahasa. Cocok untuk belajar cara berpikir, jarang",
                    "dipakai di lowongan.",
                    "",
                    "Ember.js salah satu framework tertua yang masih dirawat, dengan",
                    "prinsip konvensi di atas konfigurasi: struktur folder, router, dan",
                    "data sudah ditentukan. Komunitasnya kecil tapi setia, dan masih",
                    "ada aplikasi besar yang memakainya.",
                    "",
                    "Mithril.js adalah framework SPA mungil dengan router dan klien",
                    "HTTP bawaan. Pemakainya sedikit.",
                    "",
                    "Marko berasal dari eBay dan fokus mengirim HTML secara streaming,",
                    "sedikit demi sedikit, dengan JavaScript seminimal mungkin.",
                    "",
                    "Aurelia berbasis konvensi dan standar web, dengan binding dua arah",
                    "yang ringkas. Aurelia 2 sudah bertahun-tahun di tahap rilis",
                    "kandidat, jadi jangan dipilih untuk proyek baru kecuali timmu",
                    "memang sudah memakainya.",
                    "",
                    "Ripple adalah framework UI TypeScript yang muncul tahun 2025 dari",
                    "Dominic Gannaway, mantan anggota tim React dan Svelte. State of JS",
                    "2025 menyebutnya pendatang baru paling menarik. Versinya masih",
                    "0.x, jadi API-nya bisa berubah kapan saja.",
                    "",
                    "Blazor adalah framework UI web dari Microsoft yang memakai C#",
                    "alih-alih JavaScript, bagian dari ASP.NET Core. Komponennya bisa",
                    "jalan di server atau di browser lewat WebAssembly. Di Survei Stack",
                    "Overflow 2025 Blazor dipakai 7,0% responden. Kalau kamu sudah",
                    "menyelesaikan kurikulum C#, ini jalur paling pendek ke frontend.",
                ],
            },
            {
                "heading": "Komponen Blazor",
                "bahasa": "razor",
                "code": """<button @onclick="Tambah">Diklik @jumlah kali</button>

@code {
    private int jumlah = 0;
    private void Tambah() => jumlah++;
}""",
            },
            {
                "body": [
                    "Ingat: framework kecil bukan berarti jelek. Tapi untuk proyek",
                    "pertamamu di tempat kerja, yang lebih menentukan adalah apakah",
                    "ada orang lain yang bisa merawat kodenya, apakah pustaka yang kamu",
                    "butuhkan tersedia, dan apakah jawabannya mudah dicari waktu kamu",
                    "macet.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Preact sering dipakai untuk widget yang ditempel di situs orang",
                    "lain, misalnya tombol obrolan atau formulir langganan, karena",
                    "ukurannya kecil. Blazor banyak ditemui di aplikasi internal",
                    "perusahaan yang timnya sudah memakai .NET.",
                    "",
                    "Kasus kecil: kamu diminta membuat widget kalkulator ongkir yang",
                    "akan ditempel di tiga situs toko yang berbeda. Syaratnya ukuran",
                    "JavaScript sekecil mungkin dan timmu sudah terbiasa menulis React.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tulis daftar syarat: ukuran kecil, bisa ditempel lewat satu",
                    "     tag script, dan gaya penulisan mirip React.",
                    "  2. Bandingkan pakai tabel di materi ini. Preact memenuhi tiga",
                    "     syarat itu, Solid memenuhi dua (JSX-nya mirip tapi cara",
                    "     berpikirnya beda).",
                    "  3. Buat prototipe dengan Preact dan Preact Signals, bangun",
                    "     dengan Vite, lalu ukur ukuran berkas hasil build.",
                    "  4. Kalau nanti butuh pustaka React tertentu, coba lewat",
                    "     preact/compat dan ukur lagi sebelum memutuskan.",
                ],
            },
        ],
    },
    {
        "title": "39. Kode Warisan: jQuery, Moment, dan Penggantinya",
        "sections": [
            {
                "body": [
                    "Kode warisan adalah kode yang sudah jalan bertahun-tahun, ditulis",
                    "orang lain, dan sekarang jadi tanggung jawabmu. Di tempat PKL atau",
                    "kerja pertama, peluangmu menyentuh kode seperti ini jauh lebih",
                    "besar daripada memulai proyek React dari nol.",
                    "",
                    "Angkanya mendukung. Di Survei Stack Overflow 2025, jQuery masih",
                    "dipakai 23,4% responden, peringkat tiga di kategori teknologi web.",
                    "Di State of JS 2025, Moment.js masih punya lebih banyak pemakai",
                    "daripada Day.js, padahal Moment sudah lama berstatus warisan.",
                    "",
                    "Tujuan materi ini dua: bisa membaca kode lama, dan tahu padanan",
                    "modernnya. Semua versi adalah versi terbaru saat materi ini",
                    "ditulis (Oktober 2026).",
                    "",
                    "  Lama           Versi    Status         Pengganti modern",
                    "  jQuery         4.0.0    menurun        DOM API bawaan",
                    "  Backbone.js    1.6.1    usang          React, Vue, Svelte",
                    "  Knockout.js    3.5.3    usang          signal, Vue",
                    "  Lodash         4.18.1   stabil-matang  fungsi bawaan JS",
                    "  Moment.js      2.31.0   usang          date-fns, Day.js, Luxon",
                    "  core-js        3.50.0   stabil-matang  polyfill seperlunya",
                ],
            },
            {
                "heading": "jQuery dan padanannya",
                "bahasa": "browser",
                "code": """// jQuery
$('#simpan').on('click', function () {
  $('.pesan').addClass('tampil').text('Tersimpan');
  $.ajax({ url: '/api/simpan', method: 'POST', data: { id: 7 } });
});

// DOM API bawaan, hasilnya sama
document.querySelector('#simpan').addEventListener('click', () => {
  for (const el of document.querySelectorAll('.pesan')) {
    el.classList.add('tampil');
    el.textContent = 'Tersimpan';
  }
  fetch('/api/simpan', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ id: 7 }),
  });
});""",
            },
            {
                "body": [
                    "jQuery lahir waktu tiap browser punya cara sendiri untuk hal yang",
                    "sama. Fungsi $() menyembunyikan perbedaan itu. Sekarang",
                    "querySelector, classList, addEventListener, dan fetch sudah sama",
                    "di semua browser, jadi alasan utama jQuery hilang.",
                    "",
                    "Cara membaca kode jQuery:",
                    "  - $('selektor') memilih elemen, hasilnya kumpulan. Perintah",
                    "    seperti .addClass() berlaku untuk semua elemen di kumpulan itu",
                    "    sekaligus. Karena itu padanannya butuh perulangan.",
                    "  - $(function () { ... }) artinya jalankan sesudah DOM siap,",
                    "    padanannya DOMContentLoaded atau tag script ber-atribut defer.",
                    "  - $.ajax, $.get, dan $.post adalah permintaan ke server,",
                    "    padanannya fetch dari materi JavaScript bab 6.",
                    "",
                    "jQuery 4.0 rilis Januari 2026 dan membuang dukungan browser yang",
                    "jauh tertinggal. Kalau kamu memperbarui jQuery 3 ke 4, baca dulu",
                    "panduan pembaruan resmi di situs jQuery, karena beberapa fungsi",
                    "lama sudah dibuang.",
                    "",
                    "Jebakan: jangan langsung menulis ulang seluruh kode jQuery.",
                    "Halaman yang jalan tetap jalan. Ganti per bagian, di tempat yang",
                    "memang sedang kamu ubah, dan uji setiap selesai.",
                    "",
                    "Backbone.js (2010) memberi struktur Model, Collection, dan View",
                    "untuk aplikasi jQuery. Knockout.js memakai observable dan",
                    "data-binding lewat atribut data-bind. Keduanya cikal bakal ide",
                    "yang sekarang ada di React, Vue, dan signal. Sekarang keduanya",
                    "hanya mendapat perawatan, jadi jangan dipilih untuk proyek baru.",
                ],
            },
            {
                "heading": "Lodash dan Moment diganti fungsi bawaan",
                "code": """const pesanan = [
  { menu: 'kopi', harga: 18000 },
  { menu: 'teh', harga: 12000 },
  { menu: 'kopi', harga: 20000 },
];

// _.groupBy(pesanan, 'menu')
const perMenu = Object.groupBy(pesanan, (p) => p.menu);
console.log(Object.keys(perMenu), perMenu.kopi.length);

// _.cloneDeep(pesanan)
const salinan = structuredClone(pesanan);
salinan[0].harga = 0;
console.log(pesanan[0].harga, salinan[0].harga);

// _.sortBy(pesanan, 'harga'), tanpa mengubah aslinya
const urut = pesanan.toSorted((a, b) => a.harga - b.harga);
console.log(urut.map((p) => p.harga).join(' < '));

// moment(t).format(...) dan .add(7, 'days')
const t = new Date(Date.UTC(2026, 9, 19, 7, 30));
const tujuhHari = new Date(t.getTime() + 7 * 24 * 60 * 60 * 1000);
const fmt = new Intl.DateTimeFormat('id-ID', {
  dateStyle: 'full', timeStyle: 'short', timeZone: 'UTC',
});
console.log(fmt.format(t));
console.log(fmt.format(tujuhHari));""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  [ 'kopi', 'teh' ] 2",
                    "  18000 0",
                    "  12000 < 18000 < 20000",
                    "  Senin, 19 Oktober 2026 pukul 07.30",
                    "  Senin, 26 Oktober 2026 pukul 07.30",
                    "",
                    "Lodash adalah kumpulan fungsi utilitas seperti debounce, groupBy,",
                    "dan cloneDeep. Di State of JS 2025 ia masih pustaka nomor dua",
                    "dengan 4.265 pemakai. Banyak fungsinya sekarang sudah ada di",
                    "JavaScript sendiri: Object.groupBy, structuredClone, toSorted, dan",
                    "at. Lodash nggak usang dan masih dirawat, tapi untuk kode baru cek",
                    "dulu apakah fungsi bawaan sudah cukup.",
                    "",
                    "Moment.js dulu pustaka tanggal paling populer. Masalahnya dua:",
                    "ukurannya besar, dan objeknya mutable, artinya .add() mengubah",
                    "objek aslinya. Tim Moment sendiri menyatakan proyeknya berstatus",
                    "warisan dalam mode perawatan sejak 2020 dan menyarankan pindah.",
                    "Penggantinya:",
                    "  - date-fns (4.4.0): kumpulan fungsi murni seperti format dan",
                    "    addDays. Pilihan utama pengganti Moment, nomor tiga pustaka",
                    "    terbanyak di State of JS 2025.",
                    "  - Day.js (1.11.23): sekitar 2 kB dengan API mirip Moment, paling",
                    "    gampang untuk migrasi.",
                    "  - Luxon (3.7.2): immutable dan kuat di zona waktu, dibuat salah",
                    "    satu pengelola Moment.",
                    "  - Intl bawaan, seperti contoh di atas, sudah cukup untuk",
                    "    memformat tanggal dalam bahasa Indonesia.",
                    "",
                    "API tanggal baru bawaan JavaScript bernama Temporal mulai",
                    "tersedia di sebagian browser. Sebelum memakainya, cek tabel",
                    "dukungannya di MDN.",
                    "",
                    "Ingat: tanggal tanpa zona waktu adalah sumber bug klasik. Contoh",
                    "di atas memakai Date.UTC dan timeZone: 'UTC' supaya hasilnya sama",
                    "di komputer mana pun. Tanpa itu, server di Jakarta dan laptop di",
                    "Makassar bisa menampilkan jam berbeda untuk data yang sama.",
                ],
            },
            {
                "heading": "Polyfill dan core-js",
                "body": [
                    "core-js adalah kumpulan polyfill, yaitu kode yang menambahkan",
                    "fitur JavaScript baru ke browser lama. Misalnya browser lama",
                    "belum punya Object.groupBy. Polyfill menuliskan fungsi itu dengan",
                    "JavaScript biasa, jadi kodemu tetap jalan.",
                    "",
                    "Bedakan polyfill dengan transpile. Transpile mengubah sintaks baru",
                    "jadi sintaks lama waktu build, misalnya ?. jadi pengecekan biasa.",
                    "Polyfill menambah fungsi yang belum ada waktu kode berjalan.",
                    "Sintaks nggak bisa di-polyfill, fungsi nggak bisa di-transpile.",
                    "",
                    "Di proyek lama kamu sering ketemu import 'core-js/stable' di",
                    "baris paling atas, yang memuat ratusan polyfill sekaligus. Kalau",
                    "target browsermu sudah modern, sebagian besar polyfill itu cuma",
                    "menambah ukuran. Atur daftar target browser di konfigurasi build",
                    "(browserslist), lalu biarkan alat build memasukkan polyfill yang",
                    "memang dibutuhkan.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Banyak situs pemerintah daerah, toko online lama, dan tema",
                    "WordPress masih memuat jQuery. Aplikasi internal yang dibangun",
                    "sekitar 2015 sering memakai Moment untuk semua tanggal dan Lodash",
                    "untuk mengolah data.",
                    "",
                    "Kasus kecil: halaman laporan penjualan memakai Moment dan berkas",
                    "JavaScript-nya 300 kB. Atasan minta ukurannya dikurangi tanpa",
                    "mengubah tampilan tanggal yang sudah dipakai di laporan cetak.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Cari semua pemakaian Moment dengan grep -rn \"moment(\" src/,",
                    "     lalu catat format apa saja yang dipakai.",
                    "  2. Tulis tes kecil yang mencetak hasil format lama untuk beberapa",
                    "     tanggal tetap, misalnya 19 Oktober 2026 pukul 07.30 UTC.",
                    "  3. Ganti satu berkas dengan Day.js atau date-fns, jalankan tes",
                    "     yang sama, dan pastikan hasilnya identik.",
                    "  4. Perhatikan .add() dan .subtract(). Di Moment keduanya",
                    "     mengubah objek asli, di Day.js dan date-fns hasilnya objek",
                    "     baru, jadi kode yang mengandalkan perubahan itu harus",
                    "     menyimpan hasilnya ke variabel.",
                    "  5. Sesudah semua berkas pindah, hapus moment dari package.json",
                    "     dan bandingkan ukuran hasil build sebelum dan sesudahnya.",
                ],
            },
        ],
    },
    {
        "title": "40. Unit Test: node:test, Vitest, dan Jest",
        "sections": [
            {
                "body": [
                    "Unit test adalah kode kecil yang memeriksa satu bagian programmu,",
                    "biasanya satu fungsi, dengan masukan tertentu dan hasil yang",
                    "diharapkan. Kamu menulisnya sekali, lalu komputer menjalankannya",
                    "ratusan kali tiap kali kode berubah.",
                    "",
                    "Masalah yang dipecahkan sederhana. Kamu memperbaiki rumus diskon",
                    "di keranjang belanja, lalu tanpa sadar ongkos kirim ikut salah.",
                    "Tanpa tes, kesalahan itu baru ketahuan waktu pembeli komplain.",
                    "Dengan tes, terminal langsung memberi tahu tes mana yang gagal",
                    "dan nilai apa yang keluar.",
                    "",
                    "Satu tes biasanya punya tiga langkah, sering disebut AAA:",
                    "  1. Arrange: siapkan data, misalnya isi keranjang.",
                    "  2. Act: panggil fungsi yang diuji.",
                    "  3. Assert: bandingkan hasilnya dengan yang diharapkan.",
                    "",
                    "Node.js sudah membawa test runner sendiri, namanya node:test.",
                    "Kamu nggak perlu memasang paket apa pun, jadi ini titik mulai",
                    "paling ringan. Contoh di bawah bisa langsung kamu jalankan.",
                ],
            },
            {
                "heading": "Tes pertama dengan node:test",
                "code": """const { describe, it, beforeEach } = require('node:test');
const assert = require('node:assert/strict');

// kode yang diuji
function hitungTotal(keranjang, kode = '') {
  const kotor = keranjang.reduce((s, b) => s + b.harga * b.jumlah, 0);
  if (kode === '') return kotor;
  if (kode === 'HEMAT10') return Math.round(kotor * 0.9);
  throw new Error('kode diskon tidak dikenal: ' + kode);
}

describe('hitungTotal', () => {
  let keranjang;

  beforeEach(() => {
    keranjang = [
      { nama: 'kopi', harga: 18000, jumlah: 2 },
      { nama: 'teh', harga: 12000, jumlah: 1 },
    ];
  });

  it('menjumlahkan harga dikali jumlah', () => {
    assert.equal(hitungTotal(keranjang), 48000);
  });

  it('kode HEMAT10 memotong 10%', () => {
    assert.equal(hitungTotal(keranjang, 'HEMAT10'), 43200);
  });

  it('kode yang salah melempar error', () => {
    assert.throws(() => hitungTotal(keranjang, 'GRATIS'), /tidak dikenal/);
  });

  it('keranjang kosong bernilai nol', () => {
    assert.equal(hitungTotal([]), 0);
  });
});""",
            },
            {
                "heading": "Cara membacanya",
                "body": [
                    "describe mengelompokkan tes yang membahas hal yang sama. it adalah",
                    "satu tes, dan kalimat di dalamnya sebaiknya bisa dibaca sebagai",
                    "spesifikasi: \"hitungTotal menjumlahkan harga dikali jumlah\".",
                    "",
                    "beforeEach jalan sebelum setiap it. Keranjang dibuat ulang setiap",
                    "kali, jadi tes yang mengubah keranjang nggak memengaruhi tes",
                    "berikutnya. Tes yang saling bergantung adalah sumber masalah yang",
                    "paling menyebalkan: lulus kalau dijalankan berurutan, gagal kalau",
                    "dijalankan sendirian.",
                    "",
                    "assert.equal pada modul node:assert/strict membandingkan dengan",
                    "===. Untuk objek dan array pakai assert.deepEqual, yang",
                    "membandingkan isinya. assert.throws memeriksa bahwa fungsi melempar",
                    "error yang pesannya cocok dengan pola.",
                    "",
                    "Waktu dijalankan, Node mencetak tanda centang untuk tiap tes yang",
                    "lulus, lalu ringkasan jumlah tes, yang lulus, dan yang gagal,",
                    "beserta durasinya dalam milidetik. Di proyek sungguhan, berkas tes",
                    "biasanya diberi nama seperti total.test.js dan dijalankan semuanya",
                    "dengan perintah node --test.",
                ],
            },
            {
                "heading": "Tes yang sama di Vitest",
                "code": """// total.test.js
import { describe, it, expect, beforeEach } from 'vitest';
import { hitungTotal } from './total.js';

describe('hitungTotal', () => {
  let keranjang;
  beforeEach(() => {
    keranjang = [{ nama: 'kopi', harga: 18000, jumlah: 2 }];
  });

  it('kode HEMAT10 memotong 10%', () => {
    expect(hitungTotal(keranjang, 'HEMAT10')).toBe(32400);
  });

  it('mengembalikan angka, bukan string', () => {
    expect(typeof hitungTotal(keranjang)).toBe('number');
  });
});""",
            },
            {
                "heading": "Menjalankan ketiganya",
                "bahasa": "terminal",
                "code": """# bawaan Node, tanpa memasang apa pun
node --test

# Vitest: pasang sebagai devDependency, lalu jalankan
npm install -D vitest
npx vitest          # mode pantau, jalan ulang tiap berkas disimpan
npx vitest run      # sekali jalan, untuk CI

# Jest
npm install -D jest
npx jest""",
            },
            {
                "heading": "Memilih: node:test, Vitest, atau Jest",
                "body": [
                    "Bentuk tesnya hampir sama di ketiga alat. Bedanya di gaya",
                    "assertion dan di seberapa dekat alat itu dengan build tool-mu.",
                    "",
                    "  Alat       Versi (Okt 2026)  Kapan dipilih",
                    "  node:test  ikut Node 24/26   pustaka kecil, skrip, tanpa paket",
                    "  Vitest     5.0.5             proyek Vite, TypeScript, ESM",
                    "  Jest       30.5.2            proyek lama yang sudah memakainya",
                    "",
                    "Vitest memakai konfigurasi Vite yang sama dengan aplikasimu, jadi",
                    "alias, TypeScript, dan JSX langsung jalan tanpa pengaturan kedua.",
                    "API-nya dibuat kompatibel dengan Jest: describe, it, expect,",
                    "toBe, toEqual, vi.fn() untuk tiruan fungsi. Di State of JS 2025,",
                    "Vitest dipakai 53,8% responden dan pertumbuhannya paling cepat.",
                    "Sejak Angular 21, Vitest juga jadi runner bawaan Angular.",
                    "",
                    "Jest lama jadi standar dan di State of JS 2025 masih paling",
                    "banyak dipakai (74,4%), tapi kepuasannya menurun. Dukungan ES",
                    "Module di Jest masih lebih repot daripada di Vitest. Kabar",
                    "baiknya, ilmu Jest langsung terpakai di Vitest karena API-nya",
                    "hampir identik.",
                    "",
                    "Bun dan Deno juga punya padanan bawaan: bun test dan deno test.",
                    "",
                    "Jebakan: jangan menguji hal yang memang dijamin bahasa, seperti",
                    "\"array punya method push\". Tes yang berguna memeriksa keputusan",
                    "di kodemu sendiri: batas diskon, pembulatan, kasus kosong, dan",
                    "masukan yang salah.",
                    "",
                    "Ingat: laporan node --test dan Vitest memuat durasi dalam",
                    "milidetik. Angka itu berbeda tiap kali dijalankan, jadi jangan",
                    "pernah membandingkan seluruh keluaran laporan tes huruf demi",
                    "huruf. Bandingkan jumlah yang lulus dan gagal saja.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Hampir semua pustaka open source di npm menjalankan unit test di",
                    "GitHub Actions setiap ada pull request. Kalau satu tes gagal,",
                    "tombol merge ditahan sampai diperbaiki. Fungsi yang paling sering",
                    "diuji di aplikasi toko adalah perhitungan uang: total, diskon,",
                    "pajak, dan ongkir.",
                    "",
                    "Kasus kecil: fungsi hitungOngkir(beratGram) di toko kue memakai",
                    "aturan Rp10.000 per kilogram, dibulatkan ke atas, dengan minimal",
                    "satu kilogram. Pembeli mengeluh dikenai Rp20.000 untuk kue",
                    "seberat tepat 1000 gram.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tulis tes untuk batas-batasnya dulu, sebelum menyentuh",
                    "     kodenya: 1 gram, 999 gram, 1000 gram, dan 1001 gram.",
                    "       it('1000 gram dihitung satu kilo', () => {",
                    "         assert.equal(hitungOngkir(1000), 10000);",
                    "       });",
                    "  2. Jalankan node --test. Tes 1000 gram gagal dan menunjukkan",
                    "     angka 20000, jadi bug-nya terbukti.",
                    "  3. Periksa rumusnya. Biasanya penyebabnya Math.floor(berat /",
                    "     1000) + 1, yang memberi 2 untuk 1000 gram. Ganti dengan",
                    "     Math.max(1, Math.ceil(berat / 1000)).",
                    "  4. Jalankan lagi sampai semua tes lulus, lalu biarkan tes itu",
                    "     di proyek supaya bug yang sama nggak kembali.",
                ],
            },
        ],
    },
    {
        "title": "41. Testing Library dan DOM Palsu",
        "sections": [
            {
                "body": [
                    "Unit test cocok untuk fungsi yang menerima angka dan",
                    "mengembalikan angka. Komponen beda: hasilnya tampilan, dan",
                    "pengguna berinteraksi dengannya lewat klik dan ketikan. Menguji",
                    "komponen berarti menggambar komponen itu, lalu bertindak seperti",
                    "pengguna.",
                    "",
                    "Ada dua masalah. Pertama, test runner jalan di Node, dan Node",
                    "nggak punya document. Kedua, kalau tesmu memeriksa nama kelas",
                    "CSS atau isi state di dalam komponen, tes itu rusak setiap kali",
                    "kamu merapikan kode, padahal tampilan untuk pengguna nggak",
                    "berubah.",
                    "",
                    "Masalah pertama dijawab DOM palsu: jsdom (30.1.3 saat materi ini",
                    "ditulis, Oktober 2026) atau happy-dom (21.0.3). Keduanya",
                    "menulis ulang DOM dan HTML dengan JavaScript murni, jadi",
                    "document.createElement dan querySelector bisa dipakai di Node.",
                    "happy-dom lebih ringan dan cepat, jsdom lebih lengkap. Di Vitest",
                    "kamu cukup memilih environment: 'jsdom' atau 'happy-dom' di",
                    "konfigurasi.",
                    "",
                    "Masalah kedua dijawab Testing Library, keluarga pustaka untuk",
                    "React, Vue, Svelte, Angular, dan DOM biasa. Prinsipnya: cari",
                    "elemen seperti pengguna mencarinya, lewat peran, label, dan teks,",
                    "bukan lewat detail implementasi.",
                ],
            },
            {
                "heading": "Menguji form masuk (React)",
                "bahasa": "jsx",
                "code": """import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { expect, it, vi } from 'vitest';
import '@testing-library/jest-dom/vitest';  // pencocok toHaveTextContent dkk.
import FormMasuk from './FormMasuk.jsx';

it('mengirim email yang diketik', async () => {
  const kirim = vi.fn();
  const user = userEvent.setup();
  render(<FormMasuk onKirim={kirim} />);

  await user.type(screen.getByRole('textbox', { name: 'Email' }), 'sari@contoh.id');
  await user.type(screen.getByLabelText('Kata sandi'), 'rahasia');
  await user.click(screen.getByRole('button', { name: 'Masuk' }));

  expect(kirim).toHaveBeenCalledWith({ email: 'sari@contoh.id', sandi: 'rahasia' });
});

it('menampilkan pesan kalau email kosong', async () => {
  render(<FormMasuk onKirim={vi.fn()} />);
  await userEvent.click(screen.getByRole('button', { name: 'Masuk' }));
  expect(screen.getByRole('alert')).toHaveTextContent('Email wajib diisi');
});""",
            },
            {
                "heading": "Urutan query yang disarankan",
                "body": [
                    "Testing Library menyediakan beberapa cara mencari elemen.",
                    "Dokumentasinya menyarankan urutan ini, dari yang paling mirip",
                    "cara pengguna sampai yang paling terakhir dipakai:",
                    "  1. getByRole: peran dan nama aksesibel, seperti yang dibacakan",
                    "     pembaca layar di bab 02. Ini pilihan pertama.",
                    "  2. getByLabelText: untuk input yang punya label.",
                    "  3. getByPlaceholderText, getByText, getByDisplayValue.",
                    "  4. getByAltText dan getByTitle.",
                    "  5. getByTestId: cuma kalau semua cara di atas nggak mungkin.",
                    "",
                    "Kenapa getByRole duluan? Kalau tes bisa menemukan tombol dengan",
                    "role button bernama Masuk, pembaca layar juga bisa. Jadi tesmu",
                    "sekaligus memeriksa aksesibilitas. Div yang diberi onclick nggak",
                    "punya peran button, dan getByRole akan gagal menemukannya. Tes",
                    "yang gagal di situ sedang memberi tahu bug yang nyata.",
                    "",
                    "Tiap query punya tiga bentuk:",
                    "  - getBy... melempar error kalau elemen nggak ada. Dipakai untuk",
                    "    elemen yang wajib ada.",
                    "  - queryBy... mengembalikan null kalau nggak ada. Dipakai untuk",
                    "    memeriksa bahwa sesuatu sudah hilang.",
                    "  - findBy... menunggu sampai elemen muncul, mengembalikan",
                    "    Promise. Dipakai untuk elemen yang muncul sesudah data datang.",
                    "",
                    "Di bawah ini tiruan kecil getByRole yang mencari elemen di pohon",
                    "palsu. Perhatikan dua yang gagal.",
                ],
            },
            {
                "heading": "Tiruan getByRole",
                "code": "const halaman = [\n  { tag: 'h2', teks: 'Masuk' },\n  { tag: 'label', teks: 'Email', untuk: 'email' },\n  { tag: 'input', id: 'email', type: 'email' },\n  { tag: 'label', teks: 'Kata sandi', untuk: 'sandi' },\n  { tag: 'input', id: 'sandi', type: 'password' },\n  { tag: 'button', teks: 'Masuk' },\n  { tag: 'div', teks: 'Lupa sandi?', diklik: true },\n];\n\nfunction peran(el) {\n  if (/^h[1-6]$/.test(el.tag)) return 'heading';\n  if (el.tag === 'button') return 'button';\n  if (el.tag === 'input' && ['text', 'email'].includes(el.type)) return 'textbox';\n  return null; // div yang bisa diklik dan input password nggak punya peran\n}\n\nfunction nama(el) {\n  if (el.tag === 'input') {\n    const label = halaman.find((l) => l.tag === 'label' && l.untuk === el.id);\n    return label ? label.teks : '';\n  }\n  return el.teks || '';\n}\n\nfunction getByRole(role, opsi = {}) {\n  const cocok = halaman.filter((el) => peran(el) === role\n    && (opsi.name === undefined || nama(el) === opsi.name));\n  if (cocok.length === 1) return cocok[0];\n  const ada = halaman.filter(peran).map((el) => peran(el) + ' \"' + nama(el) + '\"');\n  throw new Error((cocok.length ? 'lebih dari satu ' : 'tidak ketemu ')\n    + role + ' \"' + opsi.name + '\"\\n  yang ada: ' + ada.join(', '));\n}\n\nfor (const [role, name] of [\n  ['heading', 'Masuk'],\n  ['textbox', 'Email'],\n  ['button', 'Masuk'],\n  ['textbox', 'Kata sandi'],\n  ['button', 'Lupa sandi?'],\n]) {\n  try {\n    const el = getByRole(role, { name });\n    console.log('ketemu <' + el.tag + '> untuk ' + role + ' \"' + name + '\"');\n  } catch (e) {\n    console.log('GAGAL: ' + e.message);\n  }\n}",
            },
            {
                "body": [
                    "Keluaran:",
                    "  ketemu <h2> untuk heading \"Masuk\"",
                    "  ketemu <input> untuk textbox \"Email\"",
                    "  ketemu <button> untuk button \"Masuk\"",
                    "  GAGAL: tidak ketemu textbox \"Kata sandi\"",
                    "    yang ada: heading \"Masuk\", textbox \"Email\", button \"Masuk\"",
                    "  GAGAL: tidak ketemu button \"Lupa sandi?\"",
                    "    yang ada: heading \"Masuk\", textbox \"Email\", button \"Masuk\"",
                    "",
                    "Kegagalan pertama wajar dan bukan bug: input type=\"password\"",
                    "memang nggak punya peran textbox menurut spesifikasi ARIA, jadi",
                    "Testing Library menyarankan getByLabelText untuknya, seperti di",
                    "contoh React di atas. Kegagalan kedua adalah bug sungguhan: \"Lupa",
                    "sandi?\" ditulis sebagai div yang bisa diklik, jadi pengguna",
                    "papan ketik dan pembaca layar nggak bisa memakainya. Gantinya",
                    "elemen a atau button.",
                ],
            },
            {
                "heading": "Vue Test Utils dan batas DOM palsu",
                "body": [
                    "Untuk Vue ada dua pilihan. Vue Testing Library memakai prinsip",
                    "yang sama dengan contoh di atas. Vue Test Utils (2.5.1) adalah",
                    "pustaka resmi tim Vue: mount(Komponen) menghasilkan wrapper, lalu",
                    "wrapper.find('button').trigger('click') memicu event. Vue Test",
                    "Utils memberi akses lebih dalam ke komponen, tapi justru karena",
                    "itu tes mudah terikat pada detail implementasi.",
                    "",
                    "DOM palsu punya batas yang harus kamu tahu:",
                    "  - Nggak ada tata letak. jsdom nggak menghitung ukuran dan posisi,",
                    "    jadi getBoundingClientRect selalu mengembalikan nol. Tes yang",
                    "    memeriksa \"elemen ini terlihat\" atau \"menu muat di layar\"",
                    "    akan menipu.",
                    "  - CSS nggak dihitung ke tampilan. Elemen yang disembunyikan",
                    "    lewat kelas di berkas CSS tetap dianggap ada.",
                    "  - Nggak ada navigasi halaman sungguhan dan nggak ada jaringan.",
                    "",
                    "Untuk hal-hal itu kamu butuh browser sungguhan. Itu tugas tes",
                    "end-to-end di materi terakhir bab ini, atau mode browser yang",
                    "disediakan Vitest.",
                    "",
                    "Jebakan: tes komponen yang menunggu data sering ditulis dengan",
                    "getBy... lalu gagal karena datanya belum datang. Pakai",
                    "await screen.findByText(...) yang menunggu, bukan setTimeout",
                    "dengan angka tebakan.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Pustaka komponen besar seperti yang dibahas di bab 13 menguji",
                    "setiap komponen dengan cara ini: tombol bisa diklik dengan papan",
                    "ketik, dialog bisa ditutup dengan Escape, dan label terbaca",
                    "dengan benar. Banyak tim juga menjalankan Testing Library di",
                    "setiap pull request, berdampingan dengan unit test.",
                    "",
                    "Kasus kecil: tes lama sebuah komponen pencarian memakai",
                    "container.querySelector('.btn-cari-v2'). Setiap kali desainer",
                    "mengganti nama kelas, tes gagal walaupun tombolnya tetap jalan,",
                    "dan tim mulai mengabaikan tes yang merah.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Buka komponennya dan lihat bagaimana pengguna mengenali",
                    "     tombol itu. Kalau tulisannya Cari, namanya \"Cari\".",
                    "  2. Ganti query-nya:",
                    "       screen.getByRole('button', { name: 'Cari' })",
                    "  3. Kalau getByRole gagal, periksa elemennya. Sering ternyata",
                    "     tombol dibuat dari div atau ikon tanpa teks. Perbaiki",
                    "     komponennya (pakai button, beri aria-label untuk ikon).",
                    "  4. Jalankan tesnya lagi, lalu ganti nama kelas CSS-nya untuk",
                    "     membuktikan tes nggak ikut rusak.",
                ],
            },
        ],
    },
    {
        "title": "42. Mock API dengan MSW dan Katalog Komponen Storybook",
        "sections": [
            {
                "body": [
                    "Komponen yang mengambil data dari API susah diuji. Server",
                    "sungguhan bisa mati, datanya berubah, dan tes jadi lambat.",
                    "Cara lama: ganti fungsi pengambil data dengan tiruan di setiap",
                    "tes. Masalahnya, kodemu jadi punya dua jalur, satu untuk tes dan",
                    "satu untuk aplikasi asli.",
                    "",
                    "Mock Service Worker (MSW) memalsukan API di level jaringan. Kode",
                    "aplikasimu tetap memanggil fetch seperti biasa ke /users/7, dan",
                    "MSW mencegat permintaan itu sebelum keluar, lalu mengembalikan",
                    "respons yang kamu tentukan. Kode aplikasi nggak diubah sama",
                    "sekali. Di browser MSW memakai Service Worker, di Node memakai",
                    "pencegat permintaan.",
                    "",
                    "Versi stabil terbaru saat materi ini ditulis (Oktober 2026) adalah",
                    "MSW 3.0.3, lisensi MIT. Dokumentasinya sekarang mengimpor http",
                    "dan HttpResponse dari 'msw/http'. Tutorial MSW 1 yang memakai",
                    "rest.get dan res(ctx.json(...)) sudah basi.",
                ],
            },
            {
                "heading": "Handler dan server tiruan",
                "bahasa": "typescript",
                "code": """// src/mocks/handlers.ts
import { http, HttpResponse } from 'msw/http';

export const handlers = [
  http.get('/api/users/:id', ({ params }) => {
    if (params.id === '99') {
      return HttpResponse.json({ pesan: 'tidak ada' }, { status: 404 });
    }
    return HttpResponse.json({ id: params.id, nama: 'Sari' });
  }),
];

// src/mocks/node.ts
import { setupServer } from 'msw/node';
import { handlers } from './handlers';
export const server = setupServer(...handlers);

// vitest.setup.ts
import { beforeAll, afterEach, afterAll } from 'vitest';
import { server } from './src/mocks/node';
beforeAll(() => server.listen({ onUnhandledRequest: 'error' }));
afterEach(() => server.resetHandlers());
afterAll(() => server.close());""",
            },
            {
                "heading": "Cara kerjanya",
                "body": [
                    "Handler adalah pasangan method + pola jalur + fungsi yang membuat",
                    "respons. Pola /api/users/:id cocok dengan /api/users/7, dan 7",
                    "masuk ke params.id. HttpResponse.json membuat respons JSON dengan",
                    "status yang kamu pilih, jadi kasus galat seperti 404 dan 500",
                    "gampang diuji.",
                    "",
                    "Tiga baris di vitest.setup.ts mengatur hidup server tiruan:",
                    "  - listen() memasang pencegat sebelum semua tes.",
                    "    onUnhandledRequest: 'error' membuat tes gagal kalau ada",
                    "    permintaan yang nggak punya handler, jadi nggak ada tes yang",
                    "    tanpa sadar menembak internet.",
                    "  - resetHandlers() membuang handler tambahan sesudah tiap tes.",
                    "  - close() melepas pencegat dan memulihkan fetch asli.",
                    "",
                    "Di dalam satu tes kamu bisa menimpa handler sementara dengan",
                    "server.use(http.get(..., () => HttpResponse.json(..., { status:",
                    "500 }))) untuk menguji tampilan \"server sedang sibuk\". Sesudah",
                    "tes itu, resetHandlers() mengembalikan handler semula.",
                    "",
                    "Handler yang sama bisa dipakai di browser selama pengembangan.",
                    "Jalankan npx msw init public/ untuk menyalin berkas service",
                    "worker-nya, lalu pakai setupWorker dari 'msw/browser'. Kamu bisa",
                    "membangun tampilan sebelum backend-nya selesai.",
                    "",
                    "Latihan bab ini memintamu membuat tiruan kecil MSW sendiri dengan",
                    "mengganti globalThis.fetch, supaya kamu melihat isi mesinnya.",
                ],
            },
            {
                "heading": "Storybook: bengkel komponen",
                "body": [
                    "Storybook adalah aplikasi terpisah untuk membangun, melihat, dan",
                    "menguji komponen satu per satu, di luar aplikasimu. Setiap",
                    "keadaan komponen ditulis sebagai story: tombol utama, tombol",
                    "nonaktif, tombol saat memuat. Hasilnya daftar contoh hidup yang bisa",
                    "dibuka desainer dan programmer lain.",
                    "",
                    "Versi stabil terbaru saat materi ini ditulis (Oktober 2026) adalah",
                    "Storybook 10.6.2, lisensi MIT. Storybook 10 hanya mendukung ES",
                    "Module. Di State of JS 2025 Storybook dipakai 56,1% responden",
                    "kategori testing, dan di State of HTML 2025 ia juga tercatat",
                    "sebagai alat uji aksesibilitas.",
                ],
            },
            {
                "heading": "Story untuk komponen Tombol",
                "bahasa": "tsx",
                "code": """// Tombol.stories.tsx
import type { Meta, StoryObj } from '@storybook/react-vite';
import { Tombol } from './Tombol';

const meta = {
  component: Tombol,
  args: { label: 'Simpan' },
} satisfies Meta<typeof Tombol>;

export default meta;
type Story = StoryObj<typeof meta>;

export const Utama: Story = { args: { varian: 'utama' } };
export const Nonaktif: Story = { args: { disabled: true } };
export const Memuat: Story = { args: { memuat: true, label: 'Menyimpan' } };""",
            },
            {
                "body": [
                    "Format ini disebut CSF 3 (Component Story Format), bentuk yang",
                    "dipakai dokumentasi Storybook 10. meta menjelaskan komponennya dan",
                    "args bawaan, lalu setiap ekspor bernama adalah satu story yang",
                    "menimpa sebagian args. Di layar Storybook, args bisa diubah lewat",
                    "panel kontrol tanpa menyentuh kode.",
                    "",
                    "Storybook dan MSW sering dipasang bersama: story halaman profil",
                    "memakai handler MSW yang mengembalikan data contoh, jadi halaman",
                    "itu bisa dilihat dalam keadaan berhasil, kosong, dan galat tanpa",
                    "server sungguhan.",
                ],
            },
            {
                "heading": "Memasang keduanya",
                "bahasa": "terminal",
                "code": """npm install -D msw
npx msw init public/

npm create storybook@latest
npm run storybook""",
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Tim frontend sering mulai bekerja sebelum API backend selesai.",
                    "Mereka menyepakati bentuk JSON-nya, menulis handler MSW, lalu",
                    "membangun tampilan di atas data palsu itu. Design system di",
                    "banyak perusahaan juga dipublikasikan sebagai situs Storybook,",
                    "supaya desainer bisa memeriksa setiap komponen.",
                    "",
                    "Kasus kecil: halaman daftar pesanan harus menampilkan tiga",
                    "keadaan: sedang memuat, daftar kosong, dan pesan galat kalau",
                    "server mengembalikan 500. Backend-nya baru siap minggu depan.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Sepakati bentuk respons GET /api/pesanan dengan tim backend,",
                    "     misalnya { data: [...], total: 3 }.",
                    "  2. Tulis handler bawaan yang mengembalikan tiga pesanan contoh.",
                    "  3. Di tes keadaan kosong, timpa dengan server.use(...) yang",
                    "     mengembalikan { data: [], total: 0 }. Di tes galat, timpa",
                    "     dengan status 500.",
                    "  4. Periksa tampilannya dengan Testing Library, misalnya",
                    "     screen.findByRole('alert') untuk pesan galat.",
                    "  5. Buat story untuk ketiga keadaan, masing-masing memakai",
                    "     handler MSW-nya sendiri, lalu tunjukkan ke desainer.",
                ],
            },
        ],
    },
    {
        "title": "43. End-to-End dengan Playwright dan Peta Alat E2E",
        "sections": [
            {
                "body": [
                    "Tes end-to-end (E2E) menjalankan aplikasimu di browser",
                    "sungguhan, lalu mengklik dan mengetik seperti pengguna, dari",
                    "halaman pertama sampai tujuan akhir. Contohnya: buka toko, cari",
                    "kopi, masukkan ke keranjang, isi alamat, lihat halaman terima",
                    "kasih. Kalau satu bagian di sepanjang jalan rusak, tes gagal.",
                    "",
                    "Tes E2E paling meyakinkan karena memakai browser asli, server",
                    "asli, dan tata letak asli. Ruginya, tes ini lambat dan lebih",
                    "rapuh. Karena itu tim biasanya menyusun tes seperti piramida:",
                    "banyak unit test di dasar, lebih sedikit tes komponen di tengah,",
                    "dan beberapa tes E2E saja untuk alur yang paling penting.",
                    "",
                    "Playwright adalah alat E2E dari Microsoft yang mengendalikan",
                    "Chromium, Firefox, dan WebKit (mesin Safari). Versi stabil",
                    "terbaru saat materi ini ditulis (Oktober 2026) adalah 1.64.1,",
                    "lisensi Apache-2.0. Untuk proyek baru, Playwright adalah pilihan",
                    "yang paling sering dipakai.",
                ],
            },
            {
                "heading": "Memasang dan menjalankan",
                "bahasa": "terminal",
                "code": """npm init playwright@latest     # membuat contoh tes dan konfigurasi
npx playwright install         # mengunduh browser untuk Playwright
npx playwright test            # menjalankan semua tes
npx playwright test --ui       # mode UI: lihat langkah demi langkah
npx playwright codegen localhost:5173   # merekam klikmu jadi kode
npx playwright show-report     # laporan HTML hasil terakhir""",
            },
            {
                "heading": "Tes E2E pertama",
                "bahasa": "typescript",
                "code": "// tests/pesan.spec.ts\nimport { test, expect } from '@playwright/test';\n\ntest('pembeli bisa memesan kopi', async ({ page }) => {\n  await page.goto('/');\n\n  await page.getByRole('link', { name: 'Menu' }).click();\n  await page.getByRole('button', { name: 'Tambah Kopi susu' }).click();\n  await expect(page.getByRole('status')).toHaveText('1 item di keranjang');\n\n  await page.getByRole('link', { name: 'Keranjang' }).click();\n  await page.getByLabel('Nama').fill('Sari');\n  await page.getByRole('button', { name: 'Pesan sekarang' }).click();\n\n  await expect(page).toHaveURL(/\\/terima-kasih/);\n  await expect(page.getByRole('heading', { level: 1 })).toHaveText('Terima kasih, Sari');\n});",
            },
            {
                "heading": "Locator dan auto-wait",
                "body": [
                    "page.getByRole(...) menghasilkan locator, yaitu cara menemukan",
                    "elemen yang baru dijalankan waktu dibutuhkan. Query-nya sama",
                    "dengan Testing Library, dan alasannya juga sama: tes yang",
                    "mencari lewat peran dan nama ikut memeriksa aksesibilitas.",
                    "",
                    "Bagian paling penting adalah auto-wait. Sebelum mengklik,",
                    "Playwright menunggu elemen itu ada, terlihat, stabil (nggak",
                    "sedang bergerak), dan bisa menerima klik. expect(...).toHaveText",
                    "juga mencoba ulang sampai teksnya cocok atau batas waktu habis.",
                    "Jadi kamu hampir nggak pernah perlu menulis jeda manual.",
                    "",
                    "Jebakan: page.waitForTimeout(2000) adalah tanda tes yang rapuh.",
                    "Di laptopmu dua detik cukup, di server CI yang lambat nggak cukup,",
                    "dan di dua-duanya tes jadi lambat. Tunggu keadaan yang kamu",
                    "harapkan, misalnya expect(locator).toBeVisible(), bukan waktu.",
                    "",
                    "Konfigurasi playwright.config.ts mengatur baseURL (supaya",
                    "page.goto('/') cukup), browser mana saja yang dipakai, dan",
                    "webServer untuk menyalakan aplikasi sebelum tes jalan. Kalau tes",
                    "gagal, Playwright bisa menyimpan trace: rekaman setiap langkah",
                    "beserta tangkapan layar dan isi DOM, yang dibuka dengan",
                    "npx playwright show-trace.",
                    "",
                    "Playwright juga punya API untuk Python, jadi kalau kamu sudah",
                    "menyelesaikan kurikulum Python, konsepnya sama persis.",
                ],
            },
            {
                "heading": "Peta alat uji lainnya",
                "body": [
                    "Semua versi adalah versi terbaru saat materi ini ditulis",
                    "(Oktober 2026).",
                    "",
                    "  Alat         Versi    Jenis               Status",
                    "  Cypress      16.2.0   E2E dan komponen    stabil-matang",
                    "  Puppeteer    25.14.0  otomasi Chrome      aktif",
                    "  Selenium     4.51.0   otomasi WebDriver   stabil-matang",
                    "  WebdriverIO  10.1.0   otomasi WebDriver   aktif",
                    "  TestCafe     3.7.6    E2E                 menurun",
                    "  Mocha        12.0.3   test runner         stabil-matang",
                    "  Chai         6.3.0    assertion           stabil-matang",
                    "  Jasmine      7.0.2    test runner BDD     menurun",
                    "  Karma        6.4.4    runner di browser   usang",
                    "  QUnit        3.0.0    test runner         stabil-matang",
                    "",
                    "Cypress berjalan di dalam browser dengan tampilan interaktif yang",
                    "ramah pemula. Aplikasinya MIT, sedangkan layanan Cypress Cloud",
                    "komersial. Pemasangannya mengunduh biner berukuran ratusan MB.",
                    "Masih banyak dipakai, tapi proyek baru makin sering memilih",
                    "Playwright.",
                    "",
                    "Puppeteer dari tim Chrome dipakai untuk otomasi: scraping,",
                    "membuat PDF, dan tangkapan layar. Untuk testing, Playwright yang",
                    "dibuat mantan tim Puppeteer lebih lengkap.",
                    "",
                    "Selenium adalah kerangka otomasi browser tertua dan asal standar",
                    "WebDriver, dengan dukungan banyak bahasa. Banyak lowongan QA di",
                    "Indonesia masih menyebut Selenium, jadi kenali namanya.",
                    "WebdriverIO dibangun di atas WebDriver dan WebDriver BiDi, dan",
                    "juga bisa menguji aplikasi mobile.",
                    "",
                    "TestCafe dari DevExpress nggak memakai WebDriver. Pemakainya",
                    "menyusut ke Playwright.",
                    "",
                    "Mocha adalah test runner klasik Node yang biasanya dipasangkan",
                    "dengan Chai untuk assertion bergaya expect(x).to.equal(y). Chai 5",
                    "ke atas hanya ES Module. Jasmine dulu bawaan Angular bersama",
                    "Karma. Karma dinyatakan usang sejak 2023, dan Angular 21 memakai",
                    "Vitest sebagai bawaan serta menyediakan migrasi otomatis. Tutorial",
                    "Angular yang masih memakai Karma sudah ketinggalan. QUnit berasal",
                    "dari proyek jQuery dan sekarang dipakai kalangan terbatas.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Toko online biasanya menjaga beberapa alur dengan tes E2E: daftar",
                    "akun, masuk, cari produk, bayar. Tes itu dijalankan di CI sebelum",
                    "rilis, sering di tiga browser sekaligus, supaya bug yang cuma",
                    "muncul di Safari ketahuan sebelum pembeli menemukannya.",
                    "",
                    "Kasus kecil: tes E2E checkout lulus di laptopmu tapi kadang gagal",
                    "di GitHub Actions dengan pesan elemen tombol Bayar nggak bisa",
                    "diklik. Di dalam tes ada page.waitForTimeout(1000) sebelum klik.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Aktifkan trace untuk percobaan ulang di konfigurasi:",
                    "       use: { trace: 'on-first-retry' }",
                    "  2. Unduh trace dari CI dan buka dengan npx playwright",
                    "     show-trace. Biasanya terlihat tombol masih tertutup lapisan",
                    "     pemuat waktu diklik.",
                    "  3. Hapus waitForTimeout. Tunggu keadaannya:",
                    "       await expect(page.getByRole('progressbar')).toBeHidden();",
                    "  4. Pastikan tombolnya dicari dengan getByRole('button',",
                    "     { name: 'Bayar' }), lalu jalankan tes berulang dengan",
                    "     npx playwright test --repeat-each=20 untuk membuktikan",
                    "     tesnya stabil.",
                ],
            },
        ],
    },
    {
        "title": "44. Next.js: App Router dan Server Components",
        "sections": [
            {
                "body": [
                    "React cuma pustaka untuk menggambar komponen. Begitu aplikasimu",
                    "butuh banyak halaman, data dari database, HTML yang sudah terisi",
                    "waktu dibuka, dan cara men-deploy, kamu harus memilih dan",
                    "menyambung sendiri belasan alat. Next.js adalah framework React",
                    "full-stack yang sudah menyambungkan semua itu: routing berbasis",
                    "folder, render di server, API, optimasi gambar, dan build tool.",
                    "",
                    "Next.js dibuat Vercel, lisensinya MIT. Versi stabil terbaru saat",
                    "materi ini ditulis (Oktober 2026) adalah 16.4.2. Di Survei Stack",
                    "Overflow 2025 Next.js dipakai 20,8% responden, dan di State of JS",
                    "2025 ia meta-framework nomor satu (58,6%). Survei yang sama juga",
                    "mencatat kepuasannya tertinggal 39 poin dari Astro, jadi banyak",
                    "pemakai yang tetap memakainya sambil menggerutu soal kerumitannya.",
                    "",
                    "Next.js punya dua sistem routing. Pages Router (folder pages/)",
                    "adalah sistem lama. App Router (folder app/) adalah sistem baru",
                    "yang dibangun di atas React Server Components. Materi ini memakai",
                    "App Router. Kalau tutorial yang kamu baca memakai",
                    "getServerSideProps atau getStaticProps, itu Pages Router.",
                ],
            },
            {
                "heading": "Membuat proyek",
                "bahasa": "terminal",
                "code": """npx create-next-app@latest kafe-senja
cd kafe-senja
npm run dev          # buka localhost:3000""",
            },
            {
                "heading": "Folder app/ menjadi rute",
                "bahasa": "teks",
                "code": """app/
  layout.tsx            kerangka semua halaman (html, body, nav)
  page.tsx              ->  /
  menu/
    page.tsx            ->  /menu
    loading.tsx         tampil selama halaman /menu menunggu data
    [id]/
      page.tsx          ->  /menu/7, /menu/12, ...
  docs/
    [...slug]/
      page.tsx          ->  /docs/a, /docs/a/b/c
  (pemasaran)/
    tentang/page.tsx    ->  /tentang (nama grup nggak masuk URL)
  api/pesanan/
    route.ts            ->  endpoint GET/POST /api/pesanan""",
            },
            {
                "heading": "Aturan berkas khusus",
                "body": [
                    "Sama seperti SvelteKit di bab 10, folder menentukan alamat dan",
                    "nama berkas menentukan perannya:",
                    "  - page.tsx adalah isi halaman. Folder tanpa page.tsx nggak",
                    "    punya alamat, jadi aman untuk menyimpan komponen.",
                    "  - layout.tsx membungkus halaman di folder itu dan semua",
                    "    subfoldernya. Layout tetap hidup waktu pindah halaman, jadi",
                    "    state di dalamnya nggak hilang.",
                    "  - loading.tsx dan error.tsx adalah tampilan saat memuat dan",
                    "    saat galat. not-found.tsx untuk halaman 404.",
                    "  - route.ts membuat endpoint API tanpa tampilan.",
                    "",
                    "Nama folder dalam kurung siku adalah parameter: [id] cocok dengan",
                    "satu segmen, [...slug] cocok dengan satu segmen atau lebih",
                    "(catch-all). Folder dalam kurung biasa seperti (pemasaran) adalah",
                    "route group: dipakai untuk mengelompokkan dan memberi layout",
                    "bersama, tapi namanya nggak masuk URL. Kalau dua rute sama-sama",
                    "cocok, yang statis menang atas yang dinamis, dan yang dinamis",
                    "menang atas catch-all. Latihan bab ini memintamu menulis",
                    "pencocok rute seperti itu.",
                ],
            },
            {
                "heading": "Server Component dan Client Component",
                "bahasa": "tsx",
                "code": """// app/menu/[id]/page.tsx  (Server Component, bawaan)
import { ambilMenu } from '@/lib/db';
import TombolPesan from './TombolPesan';

export default async function Halaman({ params }: PageProps<'/menu/[id]'>) {
  const { id } = await params;
  const menu = await ambilMenu(id);   // langsung ke database
  return (
    <article>
      <h1>{menu.nama}</h1>
      <p>Rp{menu.harga.toLocaleString('id-ID')}</p>
      <TombolPesan id={menu.id} />
    </article>
  );
}

// app/menu/[id]/TombolPesan.tsx  (Client Component)
'use client';
import { useState } from 'react';

export default function TombolPesan({ id }: { id: number }) {
  const [jumlah, setJumlah] = useState(0);
  return <button onClick={() => setJumlah(jumlah + 1)}>Pesan ({jumlah})</button>;
}""",
            },
            {
                "heading": "Cara kerjanya",
                "body": [
                    "Di App Router, setiap komponen adalah Server Component kecuali",
                    "kamu menandainya lain. Server Component jalan di server saja:",
                    "boleh async, boleh membaca database atau berkas langsung, dan",
                    "kodenya nggak pernah dikirim ke browser. Yang sampai ke browser",
                    "cuma hasilnya.",
                    "",
                    "Komponen yang butuh interaksi (useState, useEffect, onClick, atau",
                    "API browser seperti window) wajib diawali baris 'use client'.",
                    "Baris itu menandai batas: komponen tersebut beserta semua yang ia",
                    "impor ikut dikirim ke browser dan di-hydrate. Data dari Server",
                    "Component masuk ke Client Component lewat props, dan props itu",
                    "harus bisa diserialisasi (angka, string, objek polos), bukan",
                    "fungsi atau koneksi database.",
                    "",
                    "Perhatikan juga await params. Sejak Next.js 15, params dan",
                    "searchParams berbentuk Promise. Tutorial lama yang menulis",
                    "params.id langsung akan memunculkan peringatan atau galat.",
                    "",
                    "Jebakan: lupa 'use client' di komponen yang memakai useState.",
                    "Pesan galatnya menyebut bahwa hook itu hanya bisa dipakai di",
                    "Client Component. Kebalikannya juga sering terjadi: menaruh 'use",
                    "client' di layout paling atas, sehingga seluruh aplikasi jadi",
                    "Client Component dan keuntungan Server Component hilang. Taruh",
                    "'use client' serendah mungkin di pohon, di komponen kecil yang",
                    "memang interaktif.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Next.js banyak dipakai untuk toko online, situs perusahaan,",
                    "dasbor SaaS, dan blog teknis. Pola yang paling sering terlihat:",
                    "halaman produk sebagai Server Component yang membaca database,",
                    "dengan tombol keranjang dan galeri gambar sebagai Client",
                    "Component kecil.",
                    "",
                    "Kasus kecil: halaman /produk/[id] memakai 'use client' di baris",
                    "pertama karena ada tombol \"Tambah ke keranjang\". Akibatnya data",
                    "produk diambil lewat useEffect di browser, halaman tampil kosong",
                    "sebentar, dan mesin pencari melihat halaman tanpa nama produk.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pindahkan tombol ke berkas sendiri, TombolKeranjang.tsx, dan",
                    "     taruh 'use client' hanya di sana.",
                    "  2. Hapus 'use client' dari page.tsx, jadikan fungsinya async,",
                    "     lalu ambil data langsung:",
                    "       const { id } = await params;",
                    "       const produk = await ambilProduk(id);",
                    "  3. Kirim yang dibutuhkan tombol lewat props, misalnya",
                    "     <TombolKeranjang id={produk.id} />.",
                    "  4. Buka halaman, klik kanan, lalu View Page Source. Nama dan",
                    "     harga produk sekarang ada di HTML awal.",
                ],
            },
        ],
    },
    {
        "title": "45. Next.js: Data, Cache, dan Deploy",
        "sections": [
            {
                "body": [
                    "Di materi sebelumnya kamu melihat Server Component mengambil data",
                    "langsung dengan await. Pertanyaan berikutnya: kalau seribu orang",
                    "membuka halaman yang sama, apakah database ditanya seribu kali?",
                    "Itu tergantung cache, yaitu tempat menyimpan hasil supaya",
                    "pekerjaan yang sama nggak diulang.",
                    "",
                    "Bagian cache adalah bagian Next.js yang paling sering berubah",
                    "antarversi. Di Next.js 13 dan 14, fetch di server di-cache secara",
                    "otomatis, dan banyak orang bingung kenapa datanya nggak pernah",
                    "berubah. Next.js 15 mengubah bawaannya jadi nggak di-cache.",
                    "Next.js 16 memperkenalkan Cache Components: kamu menandai sendiri",
                    "apa yang boleh di-cache. Menurut dokumentasi resmi (Oktober 2026),",
                    "aplikasi App Router baru dari create-next-app sudah menyalakan",
                    "Cache Components. Jadi kalau tutorial yang kamu baca membahas",
                    "aturan cache yang berbeda, cek dulu versi Next.js-nya.",
                ],
            },
            {
                "heading": "Menandai yang boleh di-cache",
                "bahasa": "tsx",
                "code": """// app/lib/data.ts
import { cacheLife, cacheTag } from 'next/cache';

export async function daftarMenu() {
  'use cache';
  cacheLife('hours');      // segar sampai sekitar satu jam
  cacheTag('menu');        // label untuk dibuang nanti
  return db.query('SELECT id, nama, harga FROM menu');
}

// app/menu/page.tsx
import { Suspense } from 'react';
import { cookies } from 'next/headers';
import { daftarMenu } from '@/app/lib/data';

export default async function Halaman() {
  const menu = await daftarMenu();
  return (
    <>
      <ul>{menu.map((m) => <li key={m.id}>{m.nama}</li>)}</ul>
      <Suspense fallback={<p>Memuat poin member...</p>}>
        <PoinMember />
      </Suspense>
    </>
  );
}

async function PoinMember() {
  const sesi = (await cookies()).get('sesi')?.value;
  const poin = await ambilPoin(sesi);   // beda tiap pengunjung
  return <p>Poinmu: {poin}</p>;
}""",
            },
            {
                "heading": "Cara kerjanya",
                "body": [
                    "Direktif 'use cache' di awal fungsi membuat hasil fungsi itu",
                    "disimpan. Argumen fungsi ikut jadi kunci cache, jadi",
                    "ambilMenu(7) dan ambilMenu(8) disimpan terpisah. cacheLife",
                    "menentukan umurnya lewat profil seperti 'minutes', 'hours', atau",
                    "'days'. Dokumentasi menyarankan setiap 'use cache' dipasangkan",
                    "dengan cacheLife.",
                    "",
                    "Data yang beda tiap pengunjung, misalnya yang membaca cookies,",
                    "nggak di-cache. Bungkus komponennya dengan <Suspense>. Next.js",
                    "lalu mengirim bagian statis dan yang ter-cache lebih dulu sebagai",
                    "kerangka halaman, dan bagian di dalam Suspense menyusul begitu",
                    "datanya siap. Pengiriman bertahap ini disebut streaming, dan",
                    "gabungan kerangka statis dengan lubang dinamis disebut Partial",
                    "Prerendering.",
                    "",
                    "Supaya data terbaru tampil sesudah ada perubahan, cache dibuang",
                    "lewat labelnya:",
                    "  - updateTag('menu') membuang cache seketika. Hanya boleh di",
                    "    Server Action, cocok supaya orang yang baru menyimpan langsung",
                    "    melihat perubahannya.",
                    "  - revalidateTag('menu', 'max') memakai pola stale while",
                    "    revalidate: isi lama tetap dikirim sambil isi baru disiapkan",
                    "    di belakang. Boleh di Server Action dan Route Handler, cocok",
                    "    untuk webhook dari CMS.",
                    "  - revalidatePath('/menu') membuang cache satu alamat, kalau",
                    "    kamu nggak tahu labelnya.",
                ],
            },
            {
                "heading": "Server Action untuk form",
                "bahasa": "tsx",
                "code": """// app/menu/tambah/page.tsx
import { updateTag } from 'next/cache';
import { redirect } from 'next/navigation';

async function tambahMenu(formData: FormData) {
  'use server';
  const nama = String(formData.get('nama') ?? '').trim();
  if (!nama) return;
  await db.insert('menu', { nama });
  updateTag('menu');
  redirect('/menu');
}

export default function Halaman() {
  return (
    <form action={tambahMenu}>
      <label>Nama menu <input name="nama" required /></label>
      <button>Simpan</button>
    </form>
  );
}""",
            },
            {
                "body": [
                    "Fungsi yang diawali 'use server' adalah Server Action: fungsi di",
                    "server yang bisa dipanggil langsung dari form. Seperti form action",
                    "SvelteKit, form ini tetap jalan tanpa JavaScript di browser.",
                    "",
                    "Jebakan: Server Action adalah endpoint publik. Siapa pun bisa",
                    "memanggilnya dengan permintaan POST buatan sendiri, jadi selalu",
                    "periksa login dan hak akses di dalam fungsinya, jangan cuma",
                    "menyembunyikan tombolnya.",
                    "",
                    "Dua hal lain yang berubah di Next.js 16. Turbopack, bundler",
                    "buatan Vercel penerus webpack, jadi bawaan untuk dev dan build.",
                    "Berkas middleware.ts diganti nama jadi proxy.ts, dengan fungsi",
                    "bernama proxy, dan ada codemod resmi untuk memindahkannya.",
                ],
            },
            {
                "heading": "Deploy",
                "bahasa": "terminal",
                "code": """# server sendiri (Node.js)
npm run build
npm run start            # next start, port 3000

# Vercel: hubungkan repo GitHub, atau lewat CLI
npx vercel               # deploy pratinjau
npx vercel --prod        # deploy produksi""",
            },
            {
                "heading": "Memilih tempat",
                "body": [
                    "Vercel adalah platform hosting dari pembuat Next.js. Kamu",
                    "menghubungkan repositori GitHub, lalu setiap push ke cabang",
                    "menghasilkan URL pratinjau sendiri, dan push ke cabang utama",
                    "menjadi produksi. Ada paket gratis Hobby untuk proyek pribadi.",
                    "Di State of JS 2025 Vercel adalah layanan hosting nomor dua (4.703",
                    "pemakai) setelah AWS. Layanannya proprietary, jadi baca batas",
                    "paket gratisnya sebelum dipakai untuk proyek kantor.",
                    "",
                    "Next.js juga bisa jalan di server sendiri. next build lalu next",
                    "start menjalankan server Node biasa. Opsi output: 'standalone' di",
                    "next.config menghasilkan folder ringkas untuk dimasukkan ke",
                    "Docker. Kalau semua halamanmu statis, output: 'export'",
                    "menghasilkan HTML biasa yang bisa diunggah ke hosting statis mana",
                    "pun, tapi fitur server seperti Server Action dan proxy nggak",
                    "tersedia.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Situs toko online sering memakai pola ini. Daftar produk di-cache",
                    "beberapa jam. Keranjang dan poin member dirender per pengunjung",
                    "di dalam Suspense. Admin yang mengubah harga memicu updateTag",
                    "supaya perubahan langsung tampil.",
                    "",
                    "Kasus kecil: admin kafe mengubah harga kopi di panel admin, tapi",
                    "halaman /menu masih menampilkan harga lama sampai satu jam",
                    "kemudian. Admin mengira penyimpanannya gagal dan mengubah harga",
                    "tiga kali.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pastikan fungsi pengambil menu diberi cacheTag('menu')",
                    "     selain cacheLife('hours').",
                    "  2. Di Server Action penyimpan harga, panggil updateTag('menu')",
                    "     sesudah database berhasil diubah.",
                    "  3. Kalau harga juga bisa berubah dari luar, misalnya dari",
                    "     sistem kasir, buat Route Handler POST yang dipanggil sistem",
                    "     itu dan isinya revalidateTag('menu', 'max').",
                    "  4. Uji: ubah harga, lalu muat ulang /menu. Harga baru harus",
                    "     langsung tampil untuk admin, dan paling lambat pada",
                    "     permintaan berikutnya untuk pengunjung lain.",
                ],
            },
        ],
    },
    {
        "title": "46. Nuxt dan Astro: Vue Full-stack dan Islands",
        "sections": [
            {
                "body": [
                    "Next.js punya saudara untuk Vue, namanya Nuxt. Ada juga Astro,",
                    "yang mengambil jalan berbeda: ia dibuat untuk situs yang isinya",
                    "kebanyakan konten, seperti blog, dokumentasi, dan halaman",
                    "pemasaran, dan secara bawaan nggak mengirim JavaScript sama",
                    "sekali.",
                    "",
                    "  Hal               Next.js          Nuxt             Astro",
                    "  Basis UI          React            Vue              apa saja",
                    "  Versi (Okt 2026)  16.4.2           4.6.2            7.4.0",
                    "  JS bawaan ke      seluruh halaman  seluruh halaman  nol, kecuali",
                    "  browser           (hydration)      (hydration)      pulau",
                    "  Paling cocok      aplikasi web     aplikasi Vue     situs konten",
                    "  Pemilik tim       Vercel           Vercel           Cloudflare",
                    "",
                    "Ketiganya berlisensi MIT. NuxtLabs, perusahaan di balik Nuxt,",
                    "bergabung ke Vercel pada Juli 2025, dan tim Astro diakuisisi",
                    "Cloudflare pada Januari 2026. Keduanya tetap open source.",
                ],
            },
            {
                "heading": "Nuxt: halaman dan API dalam satu proyek",
                "bahasa": "vue",
                "code": """<!-- app/pages/menu/[id].vue  ->  /menu/7 -->
<script setup lang="ts">
const route = useRoute();
const { data: menu, error } = await useFetch(`/api/menu/${route.params.id}`);
</script>

<template>
  <p v-if="error" role="alert">Menu tidak ditemukan.</p>
  <article v-else>
    <h1>{{ menu.nama }}</h1>
    <p>Rp{{ menu.harga }}</p>
  </article>
</template>""",
            },
            {
                "heading": "Endpoint di folder server",
                "bahasa": "typescript",
                "code": """// server/api/menu/[id].get.ts
export default defineEventHandler(async (event) => {
  const id = getRouterParam(event, 'id');
  const menu = await cariMenu(Number(id));
  if (!menu) {
    throw createError({ statusCode: 404, statusMessage: 'Tidak ada' });
  }
  return menu;
});
...""",
            },
            {
                "heading": "Ciri khas Nuxt",
                "body": [
                    "Kalau kamu sudah membaca bab Vue, komponen di atas terasa akrab.",
                    "Yang ditambahkan Nuxt:",
                    "  - Routing berbasis berkas di app/pages. Sejak Nuxt 4, kode",
                    "    aplikasi tinggal di folder app/, dan folder server/ terpisah",
                    "    di sebelahnya.",
                    "  - Auto-import. useRoute, useFetch, ref, dan komponen di folder",
                    "    components/ bisa dipakai tanpa baris import. Praktis, tapi",
                    "    pemula kadang bingung fungsi itu datang dari mana.",
                    "  - useFetch mengambil data di server waktu halaman pertama",
                    "    dirender, lalu mengirim hasilnya ke browser bersama HTML,",
                    "    supaya browser nggak mengambil ulang saat hydration.",
                    "  - Nitro, mesin server Nuxt. Berkas di server/api menjadi",
                    "    endpoint, dan Nitro bisa membangun aplikasi untuk Node,",
                    "    Vercel, Netlify, Cloudflare, dan banyak tempat lain.",
                    "",
                    "Di Survei Stack Overflow 2025 Nuxt dipakai 4,0% responden.",
                    "",
                    "Jebakan: memakai window atau localStorage di bagian script yang",
                    "jalan saat render di server. Server nggak punya window, jadi",
                    "halaman gagal, atau isi HTML dari server beda dengan hasil di",
                    "browser (hydration mismatch, bab 03). Kode yang khusus browser",
                    "taruh di onMounted atau bungkus dengan komponen <ClientOnly>.",
                ],
            },
            {
                "heading": "Astro: HTML dulu, pulau interaktif seperlunya",
                "bahasa": "astro",
                "code": """---
// src/pages/index.astro  (bagian ini jalan saat build/di server)
import Layout from '../layouts/Layout.astro';
import Penghitung from '../components/Penghitung.jsx';
import Grafik from '../components/Grafik.svelte';
const menu = ['Kopi susu', 'Teh melati', 'Roti bakar'];
---
<Layout judul="Kafe Senja">
  <h1>Menu hari ini</h1>
  <ul>{menu.map((m) => <li>{m}</li>)}</ul>

  <Penghitung client:load />
  <Grafik client:visible />
</Layout>""",
            },
            {
                "heading": "Cara kerja islands",
                "body": [
                    "Berkas .astro punya dua bagian. Di antara dua garis --- di atas",
                    "adalah kode yang jalan waktu build atau di server. Di bawahnya",
                    "template mirip HTML dengan ekspresi dalam kurung kurawal. Hasil",
                    "akhirnya HTML biasa, tanpa JavaScript.",
                    "",
                    "Bagian yang butuh interaksi ditulis sebagai komponen React, Vue,",
                    "Svelte, Solid, atau Preact, lalu diberi direktif client. Komponen",
                    "itu jadi pulau (island): satu-satunya bagian halaman yang",
                    "membawa JavaScript dan di-hydrate.",
                    "  - client:load menghidupkan pulau segera saat halaman dimuat.",
                    "  - client:idle menunggu browser senggang.",
                    "  - client:visible menunggu pulau itu masuk layar. Grafik di",
                    "    bagian bawah halaman nggak membebani halaman sampai digulir.",
                    "",
                    "Tanpa direktif client, komponen React pun cuma dirender jadi HTML",
                    "statis, tombolnya nggak bisa diklik. Itu jebakan yang paling",
                    "sering dialami pemula Astro.",
                    "",
                    "Di Survei Stack Overflow 2025 Astro dipakai 4,5% responden, dan di",
                    "State of JS 2025 kepuasannya tertinggi di antara meta-framework.",
                    "Karena dekat dengan HTML biasa, Astro adalah meta-framework",
                    "pertama yang enak untuk orang yang baru lulus kurikulum HTML dan",
                    "CSS. Astro juga menyediakan content collections, cara mengelola",
                    "berkas Markdown sebagai data bertipe.",
                    "",
                    "Kapan memilih yang mana? Kalau timmu memakai Vue dan membangun",
                    "aplikasi, pilih Nuxt. Kalau isinya kebanyakan dibaca, seperti",
                    "blog, dokumentasi, atau profil usaha, Astro hampir selalu lebih",
                    "ringan. Kalau aplikasinya React penuh interaksi, Next.js.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Banyak situs dokumentasi, blog perusahaan, dan landing page",
                    "produk dibangun dengan Astro karena halamannya cepat terbuka di",
                    "ponsel. Nuxt banyak dipakai tim yang sudah memakai Vue untuk",
                    "aplikasi web lengkap, misalnya portal pelanggan dan dasbor.",
                    "",
                    "Kasus kecil: UMKM katering minta profil usaha berisi menu, galeri,",
                    "dan satu kalkulator harga pesanan. Situs lama mereka dibuat",
                    "sebagai aplikasi React penuh dan butuh lima detik untuk tampil di",
                    "ponsel pelanggannya.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Bedakan bagian yang cuma dibaca (menu, galeri, kontak) dan",
                    "     bagian yang interaktif (kalkulator).",
                    "  2. Buat proyek Astro dengan npm create astro@latest, lalu tulis",
                    "     halaman-halamannya sebagai berkas .astro biasa.",
                    "  3. Pakai ulang komponen kalkulator React yang lama, pasang",
                    "     integrasi React, lalu tulis <Kalkulator client:visible />.",
                    "  4. Bangun dengan npm run build dan periksa folder dist/.",
                    "     Halaman tanpa kalkulator nggak memuat berkas JavaScript sama",
                    "     sekali.",
                ],
            },
        ],
    },
    {
        "title": "47. Peta Meta-framework dan Generator Situs Statis",
        "sections": [
            {
                "body": [
                    "Di luar Next.js, Nuxt, SvelteKit, dan Astro, masih banyak",
                    "meta-framework lain. Ada juga generator situs statis (SSG):",
                    "alat yang mengubah berkas Markdown dan template jadi folder HTML",
                    "siap unggah, tanpa server yang harus terus menyala. Materi ini",
                    "peta singkat beserta statusnya. Semua versi adalah versi terbaru",
                    "saat materi ini ditulis (Oktober 2026).",
                    "",
                    "  Nama            Versi    Basis        Jenis            Status",
                    "  React Router    8.4.0    React        meta-framework   aktif",
                    "  Remix           3.0.0    fork Preact  meta-framework   aktif, baru",
                    "  TanStack Start  1.169.3  React        meta-framework   aktif",
                    "  SolidStart      2.0.6    Solid        meta-framework   aktif",
                    "  Qwik City       1.20.2   Qwik         meta-framework   menurun",
                    "  Fresh           2.3.3    Preact       meta-framework   aktif",
                    "  Vike            0.4.268  bebas        meta-framework   aktif, 0.x",
                    "  RedwoodSDK      1.7.4    React        full-stack       aktif",
                    "  Meteor          3.5.3    bebas        full-stack       menurun",
                    "  Gatsby          5.16.1   React        SSG              menurun",
                    "  Docusaurus      3.10.2   React        SSG dokumentasi  aktif",
                    "  VitePress       1.6.4    Vue          SSG dokumentasi  aktif",
                    "  VuePress        1.9.10   Vue          SSG dokumentasi  menurun",
                    "  Eleventy        3.1.7    template     SSG              aktif",
                    "  Hugo            0.168.0  Go           SSG              aktif",
                    "  Jekyll          4.4.1    Ruby         SSG              stabil-matang",
                ],
            },
            {
                "heading": "Remix v2, Remix 3, dan React Router",
                "body": [
                    "Bagian ini paling membingungkan, jadi pelan-pelan. Remix awalnya",
                    "meta-framework React yang terkenal dengan loader dan action:",
                    "fungsi server untuk membaca data dan menerima form, mirip load",
                    "dan form action di SvelteKit. Lalu tim Remix menggabungkan Remix",
                    "v2 ke dalam React Router. Sejak React Router 7, router itu bisa",
                    "dipakai dalam tiga mode: declarative, data, dan framework. Mode",
                    "framework adalah penerus Remix v2. Sekarang React Router punya",
                    "jalur 8.x dan 7.x yang dirawat bersamaan.",
                    "",
                    "Pada 1 Oktober 2026 rilis Remix 3.0. Remix 3 meninggalkan React",
                    "dan memakai model komponen sendiri hasil fork Preact, dan nggak",
                    "ada jalur migrasi dari v2. Jadi kalau seseorang bilang \"pakai",
                    "Remix\", tanyakan maksudnya: proyek React lama (v2, sekarang",
                    "dipindah ke React Router) atau Remix 3 yang bukan React lagi.",
                    "",
                    "TanStack Start dibangun di atas TanStack Router yang type-safe.",
                    "Di State of JS 2025 ia paling banyak disebut di jawaban \"lainnya\"",
                    "kategori meta-framework (235 sebutan), jadi calon kuat yang naik.",
                    "",
                    "SolidStart adalah meta-framework resmi Solid, dan Qwik City",
                    "lapisan rute serta data untuk Qwik. Qwik City ikut menurun",
                    "bersama Qwik, dan generasi berikutnya bernama @qwik.dev/router.",
                    "",
                    "Fresh adalah framework untuk Deno dengan arsitektur islands",
                    "seperti Astro dan tanpa langkah build. Paketnya diterbitkan di",
                    "registri JSR. Vike (dulu vite-plugin-ssr) adalah meta-framework",
                    "modular di atas Vite yang bisa dipakai dengan React, Vue, atau",
                    "Solid. RedwoodSDK adalah penerus RedwoodJS, framework React",
                    "full-stack yang dirancang untuk Cloudflare Workers.",
                    "",
                    "Meteor adalah platform full-stack klasik dengan data real-time",
                    "otomatis antara server dan browser. Versi 3 sudah berbasis Node",
                    "modern, tapi komunitasnya mengecil. Gatsby, SSG berbasis React",
                    "dengan lapisan data GraphQL, menurun sejak diakuisisi Netlify",
                    "pada 2023 dan rilisnya jarang. Tutorial Gatsby masih banyak,",
                    "tapi untuk proyek baru pilih Astro atau Next.js.",
                ],
            },
            {
                "heading": "Generator situs statis",
                "body": [
                    "SSG paling cocok untuk dokumentasi, blog, dan portofolio. Hasilnya",
                    "folder HTML yang bisa diunggah ke hosting gratis, termasuk GitHub",
                    "Pages (bab 14).",
                    "  - Docusaurus dari Meta: tulis Markdown, dapat situs dokumentasi",
                    "    lengkap dengan versi dan pencarian.",
                    "  - VitePress berbasis Vite dan Vue, penerus VuePress. Tim Vue",
                    "    sendiri pindah ke VitePress, jadi VuePress menurun.",
                    "  - Eleventy (11ty) sederhana dan fleksibel: Markdown, HTML,",
                    "    Nunjucks, atau Liquid jadi HTML tanpa JavaScript di browser.",
                    "    Paling dekat dengan kurikulum HTML dan CSS.",
                    "  - Hugo ditulis dengan Go, satu berkas program tanpa dependensi,",
                    "    terkenal cepat membangun ribuan halaman. Lisensinya",
                    "    Apache-2.0.",
                    "  - Jekyll berbasis Ruby dan jadi mesin bawaan GitHub Pages.",
                    "",
                    "Semua SSG bekerja dengan pola yang sama. Pertama, baca berkas",
                    "konten beserta front matter, yaitu kepala berisi data di antara",
                    "dua garis ---. Lalu ubah isinya jadi HTML, bungkus dengan layout,",
                    "dan tulis ke folder keluaran. Versi kecilnya seperti ini:",
                ],
            },
            {
                "heading": "SSG mini",
                "code": "// Tiga \"berkas\" Markdown dengan front matter, seperti di folder konten SSG\nconst konten = {\n  'index.md': '---\\njudul: Beranda\\n---\\n# Kafe Senja\\nBuka tiap hari.',\n  'menu.md': '---\\njudul: Menu\\n---\\n# Menu\\nKopi susu dan teh melati.',\n  'draf.md': '---\\njudul: Promo\\ndraf: ya\\n---\\n# Promo rahasia',\n};\n\nfunction bacaFrontMatter(teks) {\n  const [, kepala, isi] = teks.match(/^---\\n([\\s\\S]*?)\\n---\\n([\\s\\S]*)$/);\n  const data = {};\n  for (const baris of kepala.split('\\n')) {\n    const [k, ...v] = baris.split(':');\n    data[k.trim()] = v.join(':').trim();\n  }\n  return { data, isi };\n}\n\nfunction markdownKeHtml(isi) {\n  return isi.split('\\n').map((b) =>\n    b.startsWith('# ') ? '<h1>' + b.slice(2) + '</h1>' : '<p>' + b + '</p>').join('');\n}\n\nconst layout = (judul, badan) => '<title>' + judul + '</title>' + badan;\n\nfor (const [nama, teks] of Object.entries(konten)) {\n  const { data, isi } = bacaFrontMatter(teks);\n  if (data.draf === 'ya') {\n    console.log(nama + ' dilewati (draf)');\n    continue;\n  }\n  const keluar = nama.replace(/\\.md$/, '.html');\n  console.log(keluar + ': ' + layout(data.judul, markdownKeHtml(isi)));\n}",
            },
            {
                "body": [
                    "Keluaran:",
                    "  index.html: <title>Beranda</title><h1>Kafe Senja</h1><p>Buka tiap hari.</p>",
                    "  menu.html: <title>Menu</title><h1>Menu</h1><p>Kopi susu dan teh melati.</p>",
                    "  draf.md dilewati (draf)",
                    "",
                    "SSG sungguhan menambah banyak hal: Markdown lengkap, daftar",
                    "artikel, tag, sitemap, dan pemantau berkas. Proyek akhir",
                    "kurikulum ini memintamu membangun versi yang lebih lengkap,",
                    "digabung dengan komponen dan router berbasis berkas.",
                    "",
                    "Ingat: memilih meta-framework kecil berarti dokumentasi dan",
                    "jawaban di forum lebih sedikit. Untuk proyek pertamamu, pilih",
                    "yang komunitasnya besar, lalu coba yang lain di proyek sampingan.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Dokumentasi banyak proyek open source dibangun dengan Docusaurus",
                    "atau VitePress dan di-host gratis. Blog pribadi programmer sering",
                    "memakai Hugo, Jekyll, atau Eleventy, karena hasilnya HTML biasa",
                    "yang murah di-host dan hampir nggak butuh perawatan.",
                    "",
                    "Kasus kecil: kamu menemukan tutorial \"Membangun blog dengan",
                    "Remix\" bertanggal 2024 dan ingin mengikutinya sekarang, Oktober",
                    "2026. Perintah instalasinya menghasilkan proyek yang sama sekali",
                    "nggak mirip dengan tutorialnya.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Lihat tanggal dan impor di tutorial. Kalau ada",
                    "     @remix-run/react, itu Remix v2 berbasis React.",
                    "  2. Remix v2 sekarang dilanjutkan oleh React Router mode",
                    "     framework. Buat proyek dengan npx create-react-router@latest.",
                    "  3. Cocokkan konsepnya: loader dan action di tutorial tetap ada",
                    "     di React Router, hanya impornya berubah dari @remix-run/*",
                    "     ke react-router.",
                    "  4. Kalau kamu memang ingin mencoba Remix 3, anggap itu framework",
                    "     baru dan ikuti dokumentasi resminya dari awal, jangan",
                    "     tutorial v2.",
                ],
            },
        ],
    },
    {
        "title": "48. Komponen Headless, shadcn/ui, dan Pustaka Komponen",
        "sections": [
            {
                "body": [
                    "Membuat tombol itu gampang. Membuat dialog, menu tarik turun,",
                    "atau tab yang benar ternyata susah. Dialog yang baik memindahkan",
                    "fokus ke dalam dirinya saat dibuka. Fokusnya dikurung supaya Tab",
                    "nggak lari ke halaman di belakang. Escape menutupnya, lalu fokus",
                    "kembali ke tombol pembukanya. Pembaca layar diberi tahu lewat",
                    "atribut ARIA (bab 02). Semua itu harus beres sebelum satu baris",
                    "CSS pun ditulis.",
                    "",
                    "Karena itu hampir nggak ada tim yang menulis komponen seperti ini",
                    "dari nol. Ada tiga jenis pustaka yang bisa dipakai, dan bedanya",
                    "ada di siapa yang memegang tampilan:",
                    "  - Headless: pustaka memberi perilaku dan aksesibilitas, kamu",
                    "    yang menulis semua gayanya.",
                    "  - Bergaya lengkap: komponen siap pakai lengkap dengan desainnya.",
                    "    Cepat, tapi tampilan aplikasimu mirip aplikasi lain yang",
                    "    memakai pustaka sama.",
                    "  - Salin kode: kode komponen disalin ke proyekmu dan jadi",
                    "    milikmu, siap diubah sesuka hati.",
                ],
            },
            {
                "heading": "Isi mesin komponen headless",
                "code": """// Logika "headless": perilaku dan atribut ARIA, tanpa satu baris gaya pun
function buatDisclosure(id) {
  let terbuka = false;
  return {
    toggle() { terbuka = !terbuka; },
    propsTombol() {
      return { 'aria-expanded': String(terbuka), 'aria-controls': id + '-isi', id: id };
    },
    propsPanel() {
      return { id: id + '-isi', role: 'region', 'aria-labelledby': id, hidden: !terbuka };
    },
  };
}

function render(props, tag, isi) {
  const attr = Object.entries(props)
    .filter(([, v]) => v !== false)
    .map(([k, v]) => (v === true ? k : k + '="' + v + '"'))
    .join(' ');
  return '<' + tag + ' ' + attr + '>' + isi + '</' + tag + '>';
}

const faq = buatDisclosure('f1');
console.log(render(faq.propsTombol(), 'button', 'Buka?'));
console.log(render(faq.propsPanel(), 'div', '08-22'));
faq.toggle();
console.log('sesudah diklik:');
console.log(render(faq.propsTombol(), 'button', 'Buka?'));
console.log(render(faq.propsPanel(), 'div', '08-22'));""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  <button aria-expanded=\"false\" aria-controls=\"f1-isi\" id=\"f1\">Buka?</button>",
                    "  <div id=\"f1-isi\" role=\"region\" aria-labelledby=\"f1\" hidden>08-22</div>",
                    "  sesudah diklik:",
                    "  <button aria-expanded=\"true\" aria-controls=\"f1-isi\" id=\"f1\">Buka?</button>",
                    "  <div id=\"f1-isi\" role=\"region\" aria-labelledby=\"f1\">08-22</div>",
                    "",
                    "Program di atas adalah inti pustaka headless dalam ukuran mini.",
                    "Ia menyimpan keadaan (terbuka atau tertutup) dan memberi atribut",
                    "yang benar untuk tombol dan panelnya. aria-expanded memberi tahu",
                    "pembaca layar bahwa panel sedang terbuka atau tertutup, dan",
                    "aria-controls menyambungkan tombol ke panel. Warna, ukuran, dan",
                    "animasi sepenuhnya urusanmu. Pustaka sungguhan juga mengurus",
                    "papan ketik, fokus, dan banyak kasus tepi yang nggak terlihat di",
                    "contoh ini.",
                ],
            },
            {
                "heading": "Pustaka headless",
                "body": [
                    "Semua versi adalah versi terbaru saat materi ini ditulis",
                    "(Oktober 2026).",
                    "  - Radix UI (paket radix-ui 1.8.1, MIT): dialog, dropdown, tab,",
                    "    tooltip, dan banyak lagi, untuk React. Sekarang dirawat WorkOS.",
                    "  - React Aria (react-aria-components 1.22.1, Apache-2.0) dari",
                    "    Adobe: aksesibilitas, dukungan papan ketik, dan",
                    "    internasionalisasi yang teliti, termasuk format",
                    "    tanggal dan bahasa kanan ke kiri.",
                    "  - Ark UI (5.39.3, MIT) dari tim Chakra: lintas framework (React,",
                    "    Vue, Solid, Svelte), dibangun di atas mesin status Zag.js.",
                    "  - Headless UI (2.2.10, MIT) dari tim Tailwind untuk React dan",
                    "    Vue. Rilisnya jarang dan jumlah komponennya lebih sedikit.",
                ],
            },
            {
                "heading": "Dialog dengan Radix",
                "bahasa": "jsx",
                "code": """import { Dialog } from 'radix-ui';

export function DialogHapus({ onHapus }) {
  return (
    <Dialog.Root>
      <Dialog.Trigger className="tombol-bahaya">Hapus pesanan</Dialog.Trigger>
      <Dialog.Portal>
        <Dialog.Overlay className="tirai" />
        <Dialog.Content className="kartu-dialog">
          <Dialog.Title>Hapus pesanan ini?</Dialog.Title>
          <Dialog.Description>Tindakan ini nggak bisa dibatalkan.</Dialog.Description>
          <Dialog.Close onClick={onHapus}>Ya, hapus</Dialog.Close>
          <Dialog.Close>Batal</Dialog.Close>
        </Dialog.Content>
      </Dialog.Portal>
    </Dialog.Root>
  );
}""",
            },
            {
                "heading": "shadcn/ui: kodenya milikmu",
                "body": [
                    "Perhatikan contoh Radix di atas: perilakunya lengkap, tapi kamu",
                    "masih harus menulis kelas tirai dan kartu-dialog sendiri.",
                    "shadcn/ui mengisi celah itu. Ia kumpulan komponen React yang",
                    "dibangun di atas primitif headless (Radix atau Base UI) dan",
                    "Tailwind CSS. Bedanya dengan pustaka lain: komponennya nggak",
                    "dipasang sebagai dependensi. CLI-nya menyalin kode sumber",
                    "komponen ke folder proyekmu.",
                ],
            },
            {
                "heading": "Memakai shadcn/ui",
                "bahasa": "terminal",
                "code": """npx shadcn@latest init          # siapkan konfigurasi dan token warna
npx shadcn@latest add button dialog
# hasilnya: components/ui/button.tsx dan components/ui/dialog.tsx""",
            },
            {
                "body": [
                    "Versi CLI shadcn saat materi ini ditulis (Oktober 2026) adalah",
                    "4.22.1, lisensi MIT. Di State of CSS 2025 shadcn/ui tercatat",
                    "dipakai 766 responden (sekitar 14%), nomor tiga di daftar CSS",
                    "framework, dan ia yang paling cepat naik di kategori UI React.",
                    "",
                    "Untungnya, kamu bebas mengubah apa pun karena kodenya ada di",
                    "proyekmu. Ruginya, pembaruan nggak datang otomatis lewat npm",
                    "update. Kalau shadcn memperbaiki bug di komponen dialog, kamu",
                    "harus menyalin ulang atau menambal sendiri.",
                    "",
                    "Jebakan: pemula sering mencari shadcn di package.json dan bingung",
                    "karena nggak ada. Yang tercatat di sana cuma dependensinya, misalnya",
                    "radix-ui. Komponennya sendiri ada di folder components/ui.",
                ],
            },
            {
                "heading": "Pustaka bergaya lengkap",
                "body": [
                    "  Pustaka      Versi   Lisensi                    Ciri",
                    "  MUI          9.5.0   MIT (MUI X Pro berbayar)   Material Design",
                    "  Ant Design   6.6.6   MIT                        tabel data, enterprise",
                    "  Chakra UI    3.37.0  MIT                        token tema, aksesibel",
                    "  Mantine      9.7.3   MIT                        lebih dari 100 komponen",
                    "",
                    "Material UI (MUI) adalah pustaka komponen React paling lengkap",
                    "berbasis Material Design dari Google. Perhatikan lisensinya:",
                    "paket inti MIT, tapi komponen lanjutan di MUI X (tabel data",
                    "tingkat Pro dan Premium, misalnya) berlisensi komersial.",
                    "",
                    "Ant Design dari Ant Group kuat untuk aplikasi kantor dan tabel",
                    "data besar. Di State of CSS 2025 ia dipakai sekitar 5% responden.",
                    "Port Vue-nya (Ant Design Vue) dikelola komunitas terpisah.",
                    "",
                    "Chakra UI versi 3 dibangun ulang di atas Ark UI dan Panda CSS,",
                    "jadi migrasi dari versi 2 cukup besar. Mantine punya lebih dari",
                    "100 komponen dan hook dengan dokumentasi yang rapi.",
                    "",
                    "Kapan memilih yang mana? Panel admin internal yang harus jadi",
                    "cepat cocok dengan pustaka bergaya lengkap. Produk yang butuh",
                    "tampilan khas merek cocok dengan headless atau shadcn/ui. Kalau",
                    "design system perusahaanmu sudah ada, headless biasanya paling",
                    "mudah disesuaikan dengan aturan desain itu.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Banyak dasbor SaaS dan aplikasi startup memakai shadcn/ui dengan",
                    "Tailwind, sehingga tampilannya mirip satu sama lain sampai",
                    "warnanya diubah. Aplikasi internal kantor dan panel admin sering",
                    "memakai Ant Design atau Material UI karena tabel data dan form-nya sudah",
                    "lengkap.",
                    "",
                    "Kasus kecil: halaman pengaturan aplikasi kasir punya dialog",
                    "\"Hapus produk\" buatan sendiri dari div. Pengguna papan ketik",
                    "mengeluh: setelah dialog terbuka, Tab malah memindahkan fokus ke",
                    "tombol di belakang tirai, dan Escape nggak menutup apa pun.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Periksa dulu proyeknya. Kalau sudah memakai Tailwind, tambahkan",
                    "     komponen dialog dengan npx shadcn@latest add dialog.",
                    "  2. Ganti div buatan sendiri dengan Dialog, DialogTrigger,",
                    "     DialogContent, dan DialogTitle dari components/ui/dialog.",
                    "  3. Pindahkan warna dan jarak lama ke kelas Tailwind di berkas",
                    "     dialog itu, karena kodenya sekarang milikmu.",
                    "  4. Uji pakai papan ketik saja: buka dengan Enter, tekan Tab",
                    "     berkali-kali (fokus harus berputar di dalam dialog), lalu",
                    "     tekan Escape dan pastikan fokus kembali ke tombol Hapus.",
                ],
            },
        ],
    },
    {
        "title": "49. Animasi dan Grafis: Motion, GSAP, D3, dan Three.js",
        "sections": [
            {
                "body": [
                    "Animasi yang baik memberi tahu pengguna apa yang baru terjadi:",
                    "kartu yang baru ditambahkan meluncur masuk, panel yang ditutup",
                    "mengecil ke tombolnya. Animasi yang buruk cuma memperlambat, dan",
                    "bagi sebagian orang bisa bikin pusing atau mual.",
                    "",
                    "Sebelum memasang pustaka, ingat bahwa browser sudah bisa banyak.",
                    "transition dan @keyframes di CSS cukup untuk efek hover, muncul,",
                    "dan memudar. Web Animations API (element.animate) memberi kendali",
                    "dari JavaScript. Pustaka baru dibutuhkan untuk hal yang lebih",
                    "rumit: urutan panjang, animasi yang mengikuti guliran, gerak",
                    "mengikuti jari, atau animasi tata letak.",
                    "",
                    "Setiap animasi punya kurva, yaitu cara nilainya berubah dari awal",
                    "ke akhir. Program ini menghitung posisi kotak yang bergerak 100",
                    "piksel selama 500 milidetik dengan tiga kurva:",
                ],
            },
            {
                "heading": "Easing dan pegas dihitung sendiri",
                "code": """// Posisi kotak (0 sampai 100 piksel) menurut tiga cara bergerak
const linear = (t) => t;
const easeOutCubic = (t) => 1 - Math.pow(1 - t, 3);

// pegas teredam: melewati tujuan sedikit, lalu kembali
function pegas(t, redaman = 6, frekuensi = 12) {
  return 1 - Math.exp(-redaman * t) * Math.cos(frekuensi * t);
}

function animasi(fungsi, durasi = 500, langkah = 125) {
  const posisi = [];
  for (let ms = 0; ms <= durasi; ms += langkah) {
    posisi.push(Math.round(100 * fungsi(ms / durasi)));
  }
  return posisi.map((v) => String(v).padStart(5)).join('');
}

console.log('ms      ' + [0, 125, 250, 375, 500].map((v) => String(v).padStart(5)).join(''));
console.log('linear  ' + animasi(linear));
console.log('easeOut ' + animasi(easeOutCubic));
console.log('pegas   ' + animasi(pegas));

const kurangiGerak = true; // anggap pengguna menyalakan "kurangi animasi"
console.log('reduced ' + (kurangiGerak ? '  langsung ke 100' : animasi(easeOutCubic)));""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  ms          0  125  250  375  500",
                    "  linear      0   25   50   75  100",
                    "  easeOut     0   58   88   98  100",
                    "  pegas       0  122   95  101  100",
                    "  reduced   langsung ke 100",
                    "",
                    "Linear bergerak rata dan terasa kaku. easeOut cepat di awal lalu",
                    "melambat, seperti benda yang direm, dan cocok untuk elemen yang",
                    "masuk layar. Pegas melewati tujuan (122) lalu kembali, memberi",
                    "kesan memantul. Pustaka seperti Motion dan React Spring memakai",
                    "model pegas seperti ini, dengan pengaturan kekakuan dan redaman.",
                ],
            },
            {
                "heading": "Menghormati prefers-reduced-motion",
                "body": [
                    "Sistem operasi punya pengaturan \"kurangi animasi\" untuk orang",
                    "yang pusing melihat gerakan besar. Browser meneruskannya sebagai",
                    "media query prefers-reduced-motion. Baris terakhir program di",
                    "atas meniru keputusan itu: kalau pengguna minta dikurangi,",
                    "elemen langsung muncul di tujuannya. Aplikasi belajar-codingV2 ini",
                    "juga memegang aturan yang sama.",
                    "",
                    "  @media (prefers-reduced-motion: reduce) {",
                    "    .kartu { transition: none; }",
                    "  }",
                    "",
                    "Di JavaScript: window.matchMedia('(prefers-reduced-motion:",
                    "reduce)').matches. Motion menyediakan hook useReducedMotion dan",
                    "pengaturan MotionConfig reducedMotion=\"user\", sedangkan GreenSock",
                    "punya gsap.matchMedia() untuk memasang animasi hanya kalau",
                    "pengguna nggak keberatan.",
                    "",
                    "Ingat: mengurangi gerak bukan berarti menghapus umpan balik.",
                    "Pudar singkat dan perubahan warna biasanya tetap aman. Yang",
                    "dihindari adalah gerakan besar, paralaks, dan putaran.",
                ],
            },
            {
                "heading": "Motion di React",
                "bahasa": "jsx",
                "code": """import { motion, AnimatePresence, MotionConfig } from 'motion/react';

export function DaftarPesanan({ pesanan }) {
  return (
    <MotionConfig reducedMotion="user">
      <ul>
        <AnimatePresence>
          {pesanan.map((p) => (
            <motion.li
              key={p.id}
              layout
              initial={{ opacity: 0, y: 12 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, x: -40 }}
              transition={{ type: 'spring', stiffness: 300, damping: 24 }}
            >
              {p.nama}
            </motion.li>
          ))}
        </AnimatePresence>
      </ul>
    </MotionConfig>
  );
}""",
            },
            {
                "heading": "Peta pustaka animasi dan grafis",
                "body": [
                    "Semua versi adalah versi terbaru saat materi ini ditulis",
                    "(Oktober 2026).",
                    "",
                    "  Pustaka       Versi    Untuk                       Lisensi",
                    "  Motion        14.3.0   animasi React/Vue/JS        MIT",
                    "  GSAP          3.15.0   timeline, animasi gulir     standar gratis",
                    "  React Spring  10.1.2   animasi pegas React         MIT",
                    "  Anime.js      4.5.0    animasi CSS/SVG ringan      MIT",
                    "  Lottie        5.13.0   putar animasi After Effects MIT",
                    "  Chart.js      4.5.1    grafik siap pakai           MIT",
                    "  D3.js         7.9.0    visualisasi data bebas      ISC",
                    "  Three.js      r186     grafis 3D (WebGL/WebGPU)    MIT",
                    "  PixiJS        8.22.0   grafis 2D cepat             MIT",
                    "",
                    "Motion dulu bernama Framer Motion, lalu digabung dengan Motion One",
                    "jadi satu paket bernama motion. Contoh di atas memakai tiga",
                    "fiturnya: animasi masuk dan keluar (AnimatePresence), animasi",
                    "tata letak (layout, baris lain bergeser mulus saat satu baris",
                    "dihapus), dan pegas.",
                    "",
                    "GSAP (GreenSock Animation Platform) adalah mesin animasi",
                    "profesional dengan timeline,",
                    "ScrollTrigger untuk animasi yang mengikuti guliran, dan SplitText",
                    "untuk menganimasikan huruf demi huruf. Sejak diakuisisi Webflow",
                    "semua plugin-nya gratis. Lisensinya adalah lisensi standar GreenSock",
                    "yang gratis dengan syarat tertentu (bukan MIT), jadi baca dulu",
                    "syaratnya sebelum dipakai di produk komersial.",
                    "",
                    "React Spring berbasis fisika pegas khusus React, rilisnya jarang.",
                    "Anime.js ringan untuk CSS, SVG, dan objek JavaScript, versi 4",
                    "rilis 2025. Lottie dari Airbnb memutar animasi vektor hasil",
                    "ekspor After Effects dalam format JSON. Format penerusnya,",
                    "dotLottie, mulai banyak dipakai.",
                    "",
                    "Untuk grafik dan grafis: Chart.js adalah pilihan termudah untuk",
                    "grafik batang, garis, dan pai, dan pustaka grafis paling banyak",
                    "dipakai di State of JS 2025. D3.js tingkatnya lebih rendah: ia",
                    "mengikat data ke elemen SVG dan menyediakan skala, sumbu, dan tata",
                    "letak, cocok untuk visualisasi yang nggak ada di daftar grafik",
                    "biasa. Three.js menggambar 3D di atas WebGL atau WebGPU. Versinya",
                    "masih 0.x walau sudah matang, jadi orang menyebutnya r186.",
                    "PixiJS menggambar 2D dengan cepat untuk game dan grafis",
                    "interaktif.",
                ],
            },
            {
                "heading": "Grafik batang dengan Chart.js",
                "bahasa": "browser",
                "code": """import Chart from 'chart.js/auto';

new Chart(document.querySelector('#penjualan'), {
  type: 'bar',
  data: {
    labels: ['Sen', 'Sel', 'Rab', 'Kam', 'Jum'],
    datasets: [{ label: 'Gelas kopi terjual', data: [42, 38, 51, 47, 66] }],
  },
  options: { animation: !matchMedia('(prefers-reduced-motion: reduce)').matches },
});""",
            },
            {
                "body": [
                    "Jebakan: grafik di canvas nggak bisa dibaca pembaca layar. Selalu",
                    "sediakan ringkasan teks atau tabel data di dekatnya, misalnya",
                    "\"Penjualan tertinggi hari Jumat, 66 gelas\".",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Situs portofolio dan halaman peluncuran produk sering memakai",
                    "GreenSock dengan ScrollTrigger. Aplikasi React memakai Motion untuk",
                    "transisi daftar dan dialog. Dasbor penjualan memakai Chart.js,",
                    "sedangkan media berita memakai D3 untuk grafik interaktif yang",
                    "bentuknya khusus.",
                    "",
                    "Kasus kecil: halaman promo kafe punya banner yang memantul terus",
                    "dan latar paralaks. Seorang pelanggan menulis di ulasan bahwa ia",
                    "pusing setiap membuka halaman itu di ponsel.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Nyalakan pengaturan kurangi animasi di sistem operasimu, lalu",
                    "     buka halamannya untuk melihat apa yang dirasakan pelanggan.",
                    "  2. Bungkus animasi besar dengan media query:",
                    "       @media (prefers-reduced-motion: no-preference) {",
                    "         .banner { animation: pantul 1s infinite; }",
                    "       }",
                    "  3. Kalau memakai GreenSock, pasang animasi paralaks di dalam",
                    "     gsap.matchMedia() dengan kondisi yang sama.",
                    "  4. Ganti pantulan tanpa henti dengan satu kali pudar masuk.",
                    "     Gerakan yang berulang terus termasuk yang paling mengganggu.",
                    "  5. Uji lagi dengan pengaturan kurangi animasi menyala dan mati.",
                ],
            },
        ],
    },
    {
        "title": "50. Monorepo: Workspaces, Turborepo, dan Nx",
        "sections": [
            {
                "body": [
                    "Bayangkan kafe tempatmu PKL punya tiga aplikasi: situs pemesanan,",
                    "panel admin, dan situs dokumentasi. Ketiganya memakai komponen",
                    "tombol yang sama dan fungsi format rupiah yang sama. Kalau tiap",
                    "aplikasi tinggal di repositori sendiri, kode bersama itu disalin",
                    "tiga kali, atau diterbitkan ke npm dan diperbarui di tiga tempat",
                    "setiap kali berubah.",
                    "",
                    "Monorepo adalah satu repositori yang berisi banyak aplikasi dan",
                    "paket. Kode bersama tinggal di satu tempat, perubahan di paket",
                    "tombol langsung terlihat oleh ketiga aplikasi, dan satu pull",
                    "request bisa mengubah paket dan semua pemakainya sekaligus.",
                ],
            },
            {
                "heading": "Struktur yang umum",
                "bahasa": "teks",
                "code": """kafe/
  package.json
  pnpm-workspace.yaml
  turbo.json
  apps/
    web/        situs pemesanan (Next.js)
    admin/      panel admin (Vite + React)
    docs/       dokumentasi (Astro)
  packages/
    ui/         komponen bersama
    utils/      formatRupiah, validasi
    config/     konfigurasi ESLint dan TypeScript bersama""",
            },
            {
                "heading": "Workspaces: dasar dari manajer paket",
                "bahasa": "yaml",
                "code": """# pnpm-workspace.yaml
packages:
  - "apps/*"
  - "packages/*"

# apps/web/package.json (potongan)
# "dependencies": { "@kafe/ui": "workspace:*" }""",
            },
            {
                "body": [
                    "Fondasi monorepo JavaScript adalah workspaces, fitur bawaan",
                    "npm, pnpm, Yarn, dan Bun. Manajer paket membaca daftar folder di",
                    "atas, lalu menautkan paket lokal satu sama lain. Ketika apps/web",
                    "menulis \"@kafe/ui\": \"workspace:*\" (sintaks pnpm dan Yarn), yang",
                    "dipakai adalah folder packages/ui di repositori itu, bukan paket",
                    "dari npm.",
                    "",
                    "Workspaces menyelesaikan urusan menautkan. Masih ada dua masalah",
                    "kalau paketnya 20. Perintah build harus dijalankan dalam urutan",
                    "yang benar (utils sebelum ui, ui sebelum web). Lalu menjalankan",
                    "ulang semuanya padahal cuma satu yang berubah membuang waktu. Di",
                    "situlah task runner monorepo masuk.",
                ],
            },
            {
                "heading": "Turborepo: graf tugas dan cache",
                "bahasa": "json",
                "code": """{
  "tasks": {
    "build": {
      "dependsOn": ["^build"],
      "outputs": ["dist/**", ".next/**"]
    },
    "test": { "dependsOn": ["build"] },
    "lint": {},
    "dev": { "cache": false, "persistent": true }
  }
}""",
            },
            {
                "heading": "Cara kerjanya",
                "body": [
                    "Turborepo membaca dependensi antarpaket dari package.json, lalu",
                    "menyusun graf tugas. \"dependsOn\": [\"^build\"] artinya: sebelum",
                    "membangun sebuah paket, bangun dulu semua paket yang jadi",
                    "dependensinya. Tugas yang nggak saling bergantung dijalankan",
                    "paralel.",
                    "",
                    "Bagian terpentingnya cache. Sebelum menjalankan tugas, Turborepo",
                    "menghitung hash dari semua masukan tugas itu: isi berkas paket,",
                    "konfigurasi, dan hash dependensinya. Kalau hash yang sama pernah",
                    "dibangun, hasilnya (folder di outputs) dipulihkan dari cache dan",
                    "tugasnya dilewati. Mengubah packages/utils mengubah hash utils,",
                    "lalu hash ui dan web yang bergantung padanya, jadi hanya tiga itu",
                    "yang dibangun ulang. Latihan bab ini memintamu membangun mesin",
                    "seperti ini.",
                    "",
                    "Turborepo dikembangkan Vercel, lisensi MIT, versi 2.11.9 saat",
                    "materi ini ditulis (Oktober 2026). Cache-nya bisa dibagi ke",
                    "seluruh tim dan CI lewat remote cache. Tutorial Turborepo 1",
                    "menulis konfigurasi di kunci \"pipeline\", sedangkan versi 2",
                    "memakai \"tasks\". Domain dokumentasinya juga beberapa kali",
                    "pindah, sekarang turborepo.dev.",
                ],
            },
            {
                "heading": "Perintah sehari-hari",
                "bahasa": "terminal",
                "code": """pnpm install                     # memasang dan menautkan semua paket
pnpm turbo run build             # build semua, sesuai urutan graf
pnpm turbo run test --filter=web # hanya web dan dependensinya
pnpm --filter @kafe/ui add clsx  # menambah dependensi ke satu paket

npx nx graph                     # Nx: lihat graf proyek di browser
npx nx affected -t test          # Nx: uji hanya yang terdampak perubahan""",
            },
            {
                "heading": "Nx dan alat lainnya",
                "body": [
                    "Nx (23.3.0, MIT) adalah sistem build monorepo yang lebih lengkap",
                    "daripada Turborepo. Selain graf tugas dan cache, ia punya",
                    "generator kode dan tampilan graf proyek. Perintah affected",
                    "menjalankan tugas hanya di proyek yang terdampak perubahan. Ada",
                    "juga plugin untuk Angular, React, Node, dan banyak lagi. Nx populer di",
                    "tim Angular. Menurut State of JS 2025, pemakai Turborepo (1.718)",
                    "dan Nx (1.682) hampir sama banyak.",
                    "",
                    "  Alat     Versi           Status         Catatan",
                    "  Lerna    10.1.1          stabil-matang  menerbitkan banyak paket",
                    "  Rush     5.181.0         stabil-matang  skala raksasa",
                    "  moon     2.6.2           aktif          lintas bahasa",
                    "  Yalc     1.0.0-pre.53    menurun        pengganti npm link",
                    "",
                    "Lerna adalah alat monorepo tertua untuk JavaScript, terkenal untuk",
                    "menerbitkan banyak paket npm sekaligus. Sejak 2022 ia dirawat tim",
                    "Nx, dan sebagian besar fitur build-nya didelegasikan ke Nx.",
                    "",
                    "Rush buatan Microsoft untuk monorepo raksasa dengan",
                    "aturan ketat, pemakainya khusus. moon adalah task runner",
                    "monorepo lintas bahasa, pemakainya masih sedikit.",
                    "",
                    "Yalc dulu dipakai untuk mencoba paket lokal di proyek lain seolah",
                    "sudah diterbitkan. Nggak ada rilis sejak 2021 dan nggak pernah",
                    "keluar dari versi pra-rilis. Workspaces bawaan manajer paket",
                    "sudah mengambil perannya, jadi jangan dipilih untuk proyek baru.",
                    "",
                    "Kapan monorepo perlu? Kalau ada kode yang dipakai bersama oleh",
                    "dua aplikasi atau lebih dan diubah bersamaan. Kalau kamu cuma",
                    "punya satu aplikasi, monorepo menambah konfigurasi tanpa memberi",
                    "apa-apa. Kalau tim-tim punya jadwal rilis dan izin akses yang",
                    "jauh berbeda, repositori terpisah kadang lebih cocok.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Banyak proyek open source besar memakai monorepo, misalnya",
                    "framework yang terdiri dari puluhan paket npm. Design system yang",
                    "menerbitkan komponen untuk React dan Vue juga sering begitu,",
                    "begitu pula perusahaan yang aplikasi web dan adminnya berbagi",
                    "kode.",
                    "",
                    "Kasus kecil: monorepo kafe punya lima paket. Setiap pull request,",
                    "CI menjalankan build dan test untuk semuanya dan butuh 14 menit,",
                    "padahal perubahan biasanya cuma di dokumentasi.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pastikan setiap paket mendeklarasikan dependensi lokalnya di",
                    "     package.json, supaya graf tugas benar.",
                    "  2. Tambahkan turbo.json dengan build yang dependsOn ^build dan",
                    "     outputs yang tepat untuk tiap jenis aplikasi.",
                    "  3. Ganti perintah CI jadi pnpm turbo run build test, dan nyalakan",
                    "     remote cache supaya hasil build di laptop dan di CI bisa",
                    "     dipakai bersama.",
                    "  4. Jalankan dua kali berturut-turut. Jalan kedua harus hampir",
                    "     semuanya diambil dari cache.",
                    "  5. Ubah satu berkas di apps/docs dan pastikan yang dibangun ulang",
                    "     cuma docs.",
                ],
            },
        ],
    },
    {
        "title": "51. PWA: Service Worker dan Strategi Cache",
        "sections": [
            {
                "body": [
                    "Aplikasi di ponsel tetap bisa dibuka waktu sinyal hilang. Situs",
                    "web biasa nggak: begitu offline, yang muncul halaman galat",
                    "browser. Progressive Web App (PWA) adalah situs web yang bisa",
                    "dipasang seperti aplikasi, punya ikon di layar utama, terbuka di",
                    "jendela sendiri tanpa bilah alamat, dan tetap jalan saat",
                    "offline. PWA adalah kumpulan standar web dari W3C, bukan pustaka",
                    "yang dipasang, jadi nggak punya nomor versi.",
                    "",
                    "Tiga bahan utamanya:",
                    "  1. HTTPS. Service worker hanya jalan di HTTPS atau di",
                    "     localhost, karena ia bisa mencegat semua permintaan halaman.",
                    "  2. Web App Manifest, berkas JSON berisi nama, ikon, warna, dan",
                    "     cara aplikasi tampil saat dipasang.",
                    "  3. Service worker, skrip yang berjalan di latar belakang browser,",
                    "     di antara halaman dan jaringan.",
                    "",
                    "Semua browser utama mendukung service worker. Dukungan pemasangan",
                    "dan fitur seperti notifikasi di iOS masih lebih terbatas daripada",
                    "di Android dan desktop, jadi uji di perangkat sungguhan.",
                ],
            },
            {
                "heading": "manifest.webmanifest",
                "bahasa": "json",
                "code": """{
  "name": "Kafe Senja",
  "short_name": "Senja",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#1b1b1f",
  "theme_color": "#c8a15a",
  "icons": [
    { "src": "/ikon-192.png", "sizes": "192x192", "type": "image/png" },
    { "src": "/ikon-512.png", "sizes": "512x512", "type": "image/png" }
  ]
}""",
            },
            {
                "heading": "Mendaftarkan service worker",
                "bahasa": "browser",
                "code": """<!-- di <head> -->
<link rel="manifest" href="/manifest.webmanifest">

<script>
  if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('/sw.js');
  }
</script>""",
            },
            {
                "heading": "sw.js: siklus hidup dan strategi",
                "bahasa": "browser",
                "code": """const VERSI = 'senja-v2';
const CANGKANG = ['/', '/gaya.css', '/app.js', '/offline.html'];

// install: simpan berkas inti lebih dulu (precache)
self.addEventListener('install', (e) => {
  e.waitUntil(caches.open(VERSI).then((c) => c.addAll(CANGKANG)));
});

// activate: buang cache versi lama
self.addEventListener('activate', (e) => {
  e.waitUntil(caches.keys().then((nama) =>
    Promise.all(nama.filter((n) => n !== VERSI).map((n) => caches.delete(n)))));
});

// fetch: halaman pakai network-first, sisanya cache-first
self.addEventListener('fetch', (e) => {
  if (e.request.mode === 'navigate') {
    e.respondWith(fetch(e.request).catch(() =>
      caches.match(e.request).then((r) => r || caches.match('/offline.html'))));
    return;
  }
  e.respondWith(caches.match(e.request).then((r) => r || fetch(e.request)));
});""",
            },
            {
                "heading": "Cara kerjanya",
                "body": [
                    "Service worker punya siklus hidup sendiri. Saat pertama",
                    "didaftarkan, event install terjadi, dan di situ berkas inti",
                    "aplikasi (cangkangnya) disimpan ke Cache Storage. Lalu event",
                    "activate, tempat membuang cache versi lama. Sesudah itu setiap",
                    "permintaan dari halaman lewat event fetch, dan service worker",
                    "memutuskan jawabannya diambil dari cache atau dari jaringan.",
                    "",
                    "Keputusan itu disebut strategi cache:",
                    "  - Cache-first: cari di cache dulu, ke jaringan kalau belum ada.",
                    "    Cocok untuk berkas yang jarang berubah seperti logo, font, dan",
                    "    CSS bernama hash.",
                    "  - Network-first: coba jaringan dulu, pakai cache kalau offline.",
                    "    Cocok untuk halaman dan data yang harus terbaru.",
                    "  - Stale-while-revalidate: langsung jawab dari cache, lalu ambil",
                    "    versi baru di latar untuk kunjungan berikutnya. Cepat, tapi",
                    "    pengguna sesekali melihat versi lama. Cocok untuk avatar atau",
                    "    daftar menu.",
                    "  - Network-only dan cache-only untuk kasus khusus, misalnya",
                    "    pembayaran yang nggak boleh di-cache sama sekali.",
                    "",
                    "Latihan bab ini memintamu menjalankan ketiga strategi utama di",
                    "atas jaringan palsu supaya kelihatan bedanya.",
                    "",
                    "Jebakan: service worker lama tetap aktif sampai semua tab situsmu",
                    "ditutup. Kalau kamu mengubah sw.js lalu memuat ulang, versi baru",
                    "menunggu di status waiting. Karena itu nama cache diberi versi",
                    "(senja-v2) dan cache lama dibuang di activate. Selama",
                    "pengembangan, buka DevTools, tab Application, lalu centang Update",
                    "on reload.",
                ],
            },
            {
                "heading": "Workbox",
                "bahasa": "javascript",
                "code": """// sw.js dengan Workbox
import { registerRoute } from 'workbox-routing';
import { CacheFirst, NetworkFirst, StaleWhileRevalidate } from 'workbox-strategies';

registerRoute(({ request }) => request.mode === 'navigate', new NetworkFirst());
registerRoute(({ request }) => request.destination === 'image', new CacheFirst());
registerRoute(({ url }) => url.pathname.startsWith('/api/menu'), new StaleWhileRevalidate());""",
            },
            {
                "body": [
                    "Menulis service worker dengan tangan rawan salah. Workbox adalah",
                    "kumpulan pustaka dari Google yang menyediakan strategi cache siap",
                    "pakai, precache berkas hasil build, dan kedaluwarsa cache. Versi",
                    "terbarunya saat materi ini ditulis (Oktober 2026) adalah 7.4.1,",
                    "lisensi MIT, dan rilisnya jarang. Banyak plugin PWA untuk build",
                    "tool memakai Workbox di baliknya.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aplikasi kasir berbasis web, daftar produk untuk sales lapangan,",
                    "dan aplikasi pencatatan di daerah dengan sinyal buruk sering",
                    "dibuat sebagai PWA. Halaman inti tetap terbuka saat offline, dan",
                    "data yang diisi disimpan dulu di perangkat sampai sinyal kembali.",
                    "",
                    "Kasus kecil: menu digital kafe dibuka pelanggan lewat QR di meja.",
                    "Sinyal di lantai dua sering hilang, dan halaman menu jadi galat.",
                    "Harga bisa berubah, tapi foto menu jarang.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tambahkan manifest dan daftarkan sw.js, lalu sajikan situs",
                    "     lewat HTTPS.",
                    "  2. Di install, precache cangkang halaman dan offline.html.",
                    "  3. Pakai cache-first untuk foto, karena jarang berubah.",
                    "  4. Pakai stale-while-revalidate untuk data menu dan harga,",
                    "     supaya halaman langsung tampil dari cache lalu harga terbaru",
                    "     ikut tersimpan untuk kunjungan berikutnya.",
                    "  5. Uji di DevTools: tab Network, pilih Offline, lalu muat ulang.",
                    "     Menu harus tetap tampil dengan harga terakhir yang tersimpan.",
                ],
            },
        ],
    },
    {
        "title": "52. WebAssembly untuk Developer Frontend",
        "sections": [
            {
                "body": [
                    "WebAssembly (Wasm) adalah format kode biner yang dijalankan",
                    "browser, dan juga Node, dengan kecepatan mendekati program native.",
                    "Kamu jarang menulisnya langsung. Biasanya program C, C++, Rust,",
                    "atau Go dikompilasi ke berkas .wasm, lalu berkas itu dipanggil",
                    "dari JavaScript.",
                    "",
                    "Wasm dipakai untuk pekerjaan berat yang lambat di JavaScript,",
                    "seperti mengolah gambar dan video, kompresi, mesin game, dan",
                    "editor desain. Wasm juga dipakai untuk memakai ulang pustaka C",
                    "yang sudah teruji puluhan tahun tanpa menulis ulang.",
                    "",
                    "Wasm nggak menggantikan JavaScript. Modul Wasm nggak bisa",
                    "menyentuh DOM secara langsung. Semua yang berhubungan dengan",
                    "halaman tetap lewat JavaScript: JS memanggil fungsi Wasm, dan",
                    "Wasm memanggil fungsi JS yang diberikan kepadanya.",
                    "",
                    "Spesifikasi terbarunya Wasm 3.0, diumumkan selesai pada 17",
                    "September 2025. Isinya antara lain memori 64-bit, banyak memori",
                    "dalam satu modul, garbage collection (memudahkan bahasa seperti",
                    "Kotlin dan Java), dan exception handling.",
                ],
            },
            {
                "heading": "Modul kecil dalam format teks",
                "bahasa": "wat",
                "code": """(module
  (import "env" "lapor" (func $lapor (param i32)))
  (import "env" "mem" (memory 1))

  (func (export "tambah") (param $a i32) (param $b i32) (result i32)
    local.get $a
    local.get $b
    i32.add)

  (func (export "tambahMemori") (param $pa i32) (param $pb i32) (result i32)
    (local $hasil i32)
    (local.set $hasil
      (i32.add (i32.load (local.get $pa)) (i32.load (local.get $pb))))
    (call $lapor (local.get $hasil))
    (local.get $hasil)))""",
            },
            {
                "body": [
                    "Ini format teks Wasm (berkas .wat), bentuk yang bisa dibaca",
                    "manusia. Wasm bekerja seperti mesin tumpukan: local.get menaruh",
                    "nilai di tumpukan, i32.add mengambil dua nilai teratas lalu",
                    "menaruh hasilnya. Tipe datanya cuma angka, misalnya i32 (bilangan",
                    "bulat 32 bit).",
                    "",
                    "Modul ini mengimpor dua hal dari JavaScript: fungsi lapor dan",
                    "sebuah memori. Memori Wasm adalah linear memory, yaitu satu",
                    "deretan byte panjang yang bisa dibaca dan ditulis dua pihak.",
                    "Teks, array, dan objek dikirim lewat memori ini sebagai byte,",
                    "karena fungsi Wasm cuma bisa menerima angka.",
                    "",
                    "Program di bawah merakit modul yang sama byte demi byte, tanpa",
                    "compiler dan tanpa paket, lalu menjalankannya di Node.",
                ],
            },
            {
                "heading": "Modul Wasm buatan tangan",
                "code": "// Merakit modul WebAssembly byte demi byte (semua angka di sini < 128,\n// jadi satu byte LEB128 cukup untuk tiap angka)\nconst teks = (s) => [s.length, ...Buffer.from(s)];\nconst bagian = (id, isi) => [id, isi.length, ...isi];\nconst daftar = (...isi) => [isi.length, ...isi.flat()];\n\nconst I32 = 0x7f;\nconst bytes = new Uint8Array([\n  0x00, 0x61, 0x73, 0x6d, // \"\\0asm\"\n  0x01, 0x00, 0x00, 0x00, // versi 1\n  // tipe 0: (i32, i32) -> i32, tipe 1: (i32) -> ()\n  ...bagian(1, daftar([0x60, 2, I32, I32, 1, I32], [0x60, 1, I32, 0])),\n  // impor: fungsi env.lapor (tipe 1) dan memori env.mem (minimal 1 halaman)\n  ...bagian(2, daftar(\n    [...teks('env'), ...teks('lapor'), 0x00, 1],\n    [...teks('env'), ...teks('mem'), 0x02, 0x00, 1],\n  )),\n  // dua fungsi buatan sendiri, keduanya bertipe 0\n  ...bagian(3, daftar([0], [0])),\n  // ekspor: tambah = fungsi 1, tambahMemori = fungsi 2 (fungsi 0 = lapor)\n  ...bagian(7, daftar(\n    [...teks('tambah'), 0x00, 1],\n    [...teks('tambahMemori'), 0x00, 2],\n  )),\n  ...bagian(10, daftar(\n    // tambah(a, b): local.get 0, local.get 1, i32.add, end\n    (() => { const k = [0, 0x20, 0, 0x20, 1, 0x6a, 0x0b]; return [k.length, ...k]; })(),\n    // tambahMemori(pa, pb): baca dua i32 dari memori, jumlahkan, lapor, kembalikan\n    (() => {\n      const k = [1, 1, I32, // satu variabel lokal i32 (indeks 2)\n        0x20, 0, 0x28, 2, 0, // local.get 0, i32.load\n        0x20, 1, 0x28, 2, 0, // local.get 1, i32.load\n        0x6a, 0x22, 2, // i32.add, local.tee 2\n        0x10, 0, // call lapor\n        0x20, 2, 0x0b]; // local.get 2, end\n      return [k.length, ...k];\n    })(),\n  )),\n]);\n\nconst memori = new WebAssembly.Memory({ initial: 1 }); // 1 halaman = 64 KiB\nconst modul = new WebAssembly.Module(bytes);\nconst instans = new WebAssembly.Instance(modul, {\n  env: { mem: memori, lapor: (n) => console.log('dari Wasm ke JS: hasil = ' + n) },\n});\n\nconsole.log('ukuran modul:', bytes.length, 'byte');\nconsole.log('tambah(2, 3) =', instans.exports.tambah(2, 3));\n\nconst ruang = new Int32Array(memori.buffer);\nruang[0] = 20; // alamat byte 0\nruang[1] = 22; // alamat byte 4\nconsole.log('tambahMemori(0, 4) =', instans.exports.tambahMemori(0, 4));\nconsole.log('8 byte pertama memori:', [...new Uint8Array(memori.buffer, 0, 8)].join(' '));",
            },
            {
                "body": [
                    "Keluaran:",
                    "  ukuran modul: 112 byte",
                    "  tambah(2, 3) = 5",
                    "  dari Wasm ke JS: hasil = 42",
                    "  tambahMemori(0, 4) = 42",
                    "  8 byte pertama memori: 20 0 0 0 22 0 0 0",
                    "",
                    "Setiap modul diawali empat byte \\0asm dan nomor versi. Sesudah",
                    "itu bagian-bagian bernomor: tipe fungsi (1), impor (2), daftar",
                    "fungsi (3), ekspor (7), dan kode (10). WebAssembly.Module",
                    "memeriksa dan mengompilasi byte itu, WebAssembly.Instance",
                    "menyambungkan impornya.",
                    "",
                    "Baris terakhir menunjukkan isi memori. JavaScript menulis 20 dan",
                    "22 lewat Int32Array, dan karena WebAssembly memakai urutan",
                    "little-endian, byte paling kecil ada di depan: 20 0 0 0. Fungsi",
                    "Wasm membaca dua angka itu, menjumlahkannya, lalu memanggil",
                    "lapor di JavaScript. Di browser, kode yang memuat berkas .wasm",
                    "biasanya memakai WebAssembly.instantiateStreaming, yang",
                    "mengompilasi sambil mengunduh.",
                ],
            },
            {
                "heading": "Dari bahasa lain ke Wasm",
                "body": [
                    "Semua versi adalah versi terbaru saat materi ini ditulis",
                    "(Oktober 2026).",
                    "",
                    "  Alat            Versi      Dari bahasa     Kegunaan",
                    "  Emscripten      6.0.12     C/C++           kompiler + perekat JS",
                    "  wasm-bindgen    0.2.129    Rust            jembatan tipe Rust-JS",
                    "  wasm-pack       0.15.0     Rust            crate jadi paket npm",
                    "  AssemblyScript  0.28.20    mirip TS        langsung ke Wasm",
                    "  Leptos          0.8.22     Rust            framework web, signal",
                    "  Yew             0.23.0     Rust            framework mirip React",
                    "  Pyodide         314.0.7    Python          Python di browser",
                    "  Wasmtime        49.0.3     (runtime)       jalankan Wasm di server",
                    "  Wasmer          7.5.0      (runtime)       runtime + registri",
                    "",
                    "Emscripten mengompilasi program C dan C++ jadi .wasm sekaligus",
                    "kode JavaScript perekatnya. Untuk Rust, wasm-bindgen membuat",
                    "Rust dan JavaScript bisa saling memanggil dengan tipe yang lebih",
                    "kaya dari sekadar angka: string, objek, dan Promise. wasm-pack",
                    "membungkus hasilnya jadi paket npm. Keduanya pindah dari",
                    "organisasi rustwasm yang sudah diarsipkan ke organisasi",
                    "wasm-bindgen, jadi tutorial lama kadang menunjuk alamat yang",
                    "sudah usang.",
                    "",
                    "AssemblyScript ditulis mirip TypeScript dan langsung dikompilasi",
                    "ke Wasm, tapi ia bukan TypeScript sungguhan: banyak fitur TS",
                    "nggak tersedia. Leptos (berbasis signal, seperti bab 03) dan Yew",
                    "(bergaya komponen mirip React) adalah framework web Rust yang",
                    "berjalan sebagai Wasm di browser. Untuk C#, ada Blazor WebAssembly",
                    "yang sudah dibahas di bab 10.",
                    "",
                    "Pyodide membawa Python lengkap, termasuk numpy dan pandas, ke",
                    "browser lewat Wasm, dengan lisensi MPL-2.0. Skema versinya baru",
                    "saja berubah dari 0.2x ke 314.x. Dugaan kuatnya mengikuti Python",
                    "3.14, tapi cek catatan rilisnya sebelum menyimpulkan.",
                    "",
                    "Di luar browser, WASI (WebAssembly System Interface) adalah",
                    "standar supaya modul Wasm bisa mengakses berkas, jam, dan jaringan",
                    "dengan aman. WASI 0.2 sudah stabil, 0.3 masih dikembangkan.",
                    "Wasmtime dari Bytecode Alliance adalah implementasi acuannya, dan",
                    "Wasmer runtime lain yang punya registri paket sendiri. Keduanya",
                    "lebih banyak dipakai di sisi server.",
                    "",
                    "Ingat: memanggil Wasm dari JavaScript ada ongkosnya, terutama",
                    "kalau data besar harus disalin bolak-balik ke memori. Wasm",
                    "menguntungkan untuk hitungan berat yang panjang, bukan untuk",
                    "fungsi kecil yang dipanggil ribuan kali dengan data baru.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Editor gambar dan desain di browser, alat kompres foto,",
                    "pemutar video, dan game web banyak yang memakai pustaka C++ atau",
                    "Rust yang dikompilasi ke Wasm. Situs belajar Python di browser",
                    "memakai Pyodide supaya kode murid jalan tanpa server.",
                    "",
                    "Kasus kecil: halaman unggah foto produk di toko online harus",
                    "mengecilkan foto 12 MP sebelum diunggah. Versi JavaScript murni",
                    "membuat halaman macet beberapa detik di laptop kantor.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Ukur dulu di DevTools, tab Performance, bagian mana yang",
                    "     lambat. Kadang yang lambat justru membaca berkasnya.",
                    "  2. Cari pustaka pengolah gambar yang sudah tersedia sebagai",
                    "     paket npm berbasis Wasm, daripada mengompilasi sendiri.",
                    "  3. Jalankan pemanggilannya di Web Worker, supaya hitungan berat",
                    "     nggak menghentikan halaman.",
                    "  4. Kirim data gambar sebagai ArrayBuffer ke worker, terima",
                    "     hasilnya, lalu tampilkan pratinjau. Ukur lagi dan bandingkan",
                    "     dengan versi lama sebelum memutuskan memakainya.",
                ],
            },
        ],
    },
    {
        "title": "53. Desktop dan Mobile dari Teknologi Web",
        "sections": [
            {
                "body": [
                    "Ilmu HTML, CSS, dan JavaScript bisa dibawa keluar browser. Ada",
                    "dua cara besar. Pertama, membungkus aplikasi web di dalam",
                    "jendela program desktop atau aplikasi ponsel, sehingga tampilannya",
                    "tetap HTML. Kedua, memakai JavaScript untuk menggerakkan komponen",
                    "native milik sistem operasi. Materi ini peta jalurnya. Kurikulum",
                    "mobile di aplikasi ini membahas React Native, Expo, Flutter, dan",
                    "bab desktop untuk Electron dan Tauri lebih dalam.",
                    "",
                    "Semua versi adalah versi terbaru saat materi ini ditulis",
                    "(Oktober 2026).",
                    "",
                    "  Kerangka      Versi    Tampilan             Backend    Status",
                    "  Electron      44.9.0   Chromium dibawa      Node.js    aktif",
                    "  Tauri         2.12.3   webview sistem       Rust       aktif",
                    "  NW.js         0.118.0  Chromium dibawa      Node.js    menurun",
                    "  Wails         2.17.0   webview sistem       Go         aktif",
                    "  Capacitor     8.5.3    webview ponsel       native     aktif",
                    "  Ionic         9.0.8    komponen UI mobile   -          stabil-matang",
                    "  Cordova       13.0.0   webview ponsel       native     menurun",
                    "  NativeScript  9.1.3    komponen native      JS         stabil-matang",
                ],
            },
            {
                "heading": "Electron: proses utama dan jendela",
                "code": """// main.js (proses utama, punya akses Node)
const { app, BrowserWindow, ipcMain } = require('electron');
const path = require('node:path');

function buatJendela() {
  const win = new BrowserWindow({
    width: 900,
    height: 600,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      contextIsolation: true,
      nodeIntegration: false,
    },
  });
  win.loadFile('index.html');
}

ipcMain.handle('simpan-catatan', async (_e, teks) => {
  // tulis ke berkas di folder data pengguna, lalu kembalikan hasilnya
  return { ok: true, panjang: teks.length };
});

app.whenReady().then(buatJendela);

// preload.js (jembatan sempit ke halaman)
// const { contextBridge, ipcRenderer } = require('electron');
// contextBridge.exposeInMainWorld('catatan', {
//   simpan: (teks) => ipcRenderer.invoke('simpan-catatan', teks),
// });""",
            },
            {
                "heading": "Electron dan Tauri",
                "body": [
                    "Electron membawa Chromium dan Node.js sendiri di dalam setiap",
                    "aplikasi. Untungnya, tampilan sama persis di Windows, macOS, dan",
                    "Linux, dan seluruh ekosistem npm bisa dipakai. Ruginya, aplikasi",
                    "\"halo dunia\" pun berukuran puluhan MB dan memakai banyak RAM.",
                    "Rilis major Electron keluar tiap delapan minggu mengikuti",
                    "Chromium. Editor kode dan aplikasi obrolan desktop yang terkenal",
                    "banyak yang dibangun dengan Electron.",
                    "",
                    "Jebakan keamanan Electron: jangan menyalakan nodeIntegration di",
                    "jendela halaman. Kalau halaman memuat skrip jahat, skrip itu bisa",
                    "memakai Node untuk membaca dan menghapus berkas di komputer",
                    "pengguna. Pola yang benar seperti contoh di atas: contextIsolation",
                    "menyala, dan halaman cuma mendapat fungsi tertentu lewat",
                    "contextBridge di preload.",
                    "",
                    "Tauri memakai webview bawaan sistem operasi (WebView2 di Windows,",
                    "WKWebView di macOS, WebKitGTK di Linux) dan backend Rust. Hasilnya",
                    "jauh lebih kecil daripada Electron. Tauri 2 juga bisa membangun",
                    "aplikasi Android dan iOS. Ruginya, tampilan bisa sedikit berbeda",
                    "antar sistem karena mesin webview-nya berbeda, dan logika",
                    "backend ditulis dengan Rust. Di Fedora, Tauri butuh paket",
                    "WebKitGTK.",
                ],
            },
            {
                "heading": "Perintah Tauri dari JavaScript",
                "bahasa": "rust",
                "code": """// src-tauri/src/lib.rs
#[tauri::command]
fn sapa(nama: &str) -> String {
    format!("Halo, {}!", nama)
}
...
// di JavaScript:
// import { invoke } from '@tauri-apps/api/core';
// const pesan = await invoke('sapa', { nama: 'Sari' });""",
            },
            {
                "heading": "Jalur lain",
                "body": [
                    "NW.js adalah pendahulu Electron dengan ide serupa. Masih dirilis",
                    "mengikuti Chromium, tapi pemakainya kecil. Wails mirip Tauri untuk",
                    "dunia Go: frontend web, backend Go. Wails 3 masih beta.",
                    "",
                    "Untuk ponsel, Capacitor dari tim Ionic membungkus aplikasi web",
                    "jadi aplikasi Android dan iOS, lengkap dengan akses kamera,",
                    "berkas, dan notifikasi lewat plugin. Membangun aplikasinya tetap",
                    "butuh Android Studio atau Xcode. Ionic adalah pustaka komponen",
                    "bergaya mobile untuk Angular, React, dan Vue yang biasanya",
                    "dipasangkan dengan Capacitor. Apache Cordova (dulu PhoneGap)",
                    "adalah pendahulu Capacitor. Masih dirilis, tapi proyek baru",
                    "memakai Capacitor, jadi Cordova cuma perlu kamu kenali di kode",
                    "lama.",
                    "",
                    "NativeScript menggerakkan komponen native Android dan iOS",
                    "langsung dari JavaScript, bisa dipakai dengan Angular, Vue, atau",
                    "Svelte.",
                    "",
                    "Di luar keluarga webview ada React Native, yaitu komponen native",
                    "dengan React, dan Expo, platform di atas React Native. Flutter",
                    "adalah toolkit UI Google dengan bahasa Dart, dan Hermes mesin",
                    "JavaScript Meta untuk React Native. Keempatnya dibahas di",
                    "kurikulum mobile.",
                ],
            },
            {
                "heading": "Capacitor dari proyek web yang sudah ada",
                "bahasa": "terminal",
                "code": """npm install @capacitor/core @capacitor/cli @capacitor/android
npx cap init "Kafe Senja" id.kafesenja.app
npm run build            # hasil build web di folder dist/
npx cap add android
npx cap sync             # salin build web ke proyek Android
npx cap open android     # buka di Android Studio""",
            },
            {
                "body": [
                    "Kapan memilih yang mana? Kalau timmu cuma menguasai JavaScript",
                    "dan butuh aplikasi desktop cepat jadi, Electron paling aman. Kalau",
                    "ukuran dan memori penting dan kamu mau belajar sedikit Rust,",
                    "Tauri. Kalau sudah punya aplikasi web dan butuh versi ponsel",
                    "dengan akses kamera, Capacitor. Kalau aplikasi ponselnya harus",
                    "terasa native penuh, lihat React Native atau Flutter di kurikulum",
                    "mobile.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Banyak aplikasi desktop populer seperti editor kode, aplikasi",
                    "obrolan tim, dan klien musik dibangun dengan Electron. Aplikasi",
                    "ponsel untuk kebutuhan internal perusahaan, misalnya absensi dan",
                    "laporan lapangan, sering berupa aplikasi web yang dibungkus",
                    "Capacitor.",
                    "",
                    "Kasus kecil: aplikasi kasir web kafe ingin dipasang di laptop",
                    "kasir sebagai program desktop, dan harus bisa menyimpan laporan",
                    "harian ke folder Dokumen. Laptop kasirnya tua dengan RAM 4 GB.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Karena RAM kecil, bandingkan ukuran dan pemakaian memori",
                    "     Electron dan Tauri dengan membangun prototipe \"halo dunia\"",
                    "     di laptop itu.",
                    "  2. Kalau memilih Tauri, buat proyek dengan npm create",
                    "     tauri-app@latest dan arahkan frontend ke hasil build",
                    "     aplikasi kasir yang sudah ada.",
                    "  3. Tulis satu perintah Rust simpan_laporan yang menulis berkas,",
                    "     lalu panggil dari JavaScript dengan invoke.",
                    "  4. Batasi izin di konfigurasi Tauri supaya aplikasi hanya boleh",
                    "     menulis ke folder Dokumen, bukan seluruh disk.",
                ],
            },
        ],
    },
    {
        "title": "54. Deno, Bun, Edge, dan Tempat Deploy Frontend",
        "sections": [
            {
                "body": [
                    "Node.js bukan satu-satunya runtime JavaScript di luar browser.",
                    "Ada dua pesaing yang cukup besar, ditambah runtime edge yang",
                    "menjalankan kodemu di server dekat pengguna. Bagian kedua materi",
                    "ini membahas tempat memasang situs frontend, termasuk cara",
                    "paling murah untuk punya portofolio online.",
                    "",
                    "  Runtime             Versi (Okt 2026)  Ciri utama",
                    "  Node.js             26.x, LTS 24      paling banyak dipakai",
                    "  Deno                2.9.7             aman bawaan, alat lengkap",
                    "  Bun                 1.4.3             serba cepat, serba ada",
                    "  Cloudflare Workers  Wrangler 4.151.1  kode di server edge",
                ],
            },
            {
                "heading": "Deno dan Bun di terminal",
                "bahasa": "terminal",
                "code": """# Deno: izin harus diberikan eksplisit
deno run main.ts                      # ditolak kalau membaca berkas
deno run --allow-read=./data main.ts  # boleh membaca folder data saja
deno fmt && deno lint && deno test    # alat bawaan
deno add jsr:@std/path                # paket dari registri JSR

# Bun: runtime, manajer paket, bundler, dan test runner
bun install                           # pengganti npm install
bun run dev
bun test
bun build ./src/index.ts --outdir dist""",
            },
            {
                "heading": "Deno dan Bun",
                "body": [
                    "Deno dibuat oleh pencipta Node.js. Lisensinya MIT. Bedanya yang",
                    "paling terasa: program Deno nggak boleh membaca berkas, mengakses",
                    "jaringan, atau membaca variabel lingkungan tanpa izin eksplisit",
                    "seperti --allow-read. Paket npm yang kamu pasang jadi nggak bisa",
                    "seenaknya mengirim berkasmu ke mana-mana. Deno juga menjalankan",
                    "TypeScript langsung dan membawa formatter, linter, dan test runner.",
                    "Sejak Deno 2, paket npm bisa dipakai lewat awalan npm:. Registri",
                    "JSR, buatan tim Deno, menerbitkan paket dalam bentuk TypeScript.",
                    "Di Survei Stack Overflow 2025 Deno dipakai 4,0% responden.",
                    "",
                    "Bun adalah runtime serba ada yang fokus pada kecepatan: sekaligus",
                    "manajer paket, bundler, dan test runner. Lisensinya MIT, dengan",
                    "sebagian komponen dari JavaScriptCore (mesin JavaScript WebKit)",
                    "berlisensi LGPL-2. Bun diakuisisi Anthropic pada Desember 2025 dan",
                    "tetap open source. Di State of JS 2025 pemakainya sekitar 21%,",
                    "naik empat poin. Kompatibilitasnya dengan API Node tinggi tapi",
                    "belum 100%, jadi paket yang bergantung pada modul native Node",
                    "kadang bermasalah.",
                    "",
                    "Kapan memilih yang mana? Untuk proyek kantor, Node LTS masih",
                    "pilihan paling aman karena semua alat dan dokumentasi",
                    "mengasumsikannya. bun install sering dipakai sekadar untuk",
                    "mempercepat pemasangan paket. Deno menarik untuk skrip dan",
                    "layanan kecil yang butuh keamanan izin dan TypeScript tanpa",
                    "konfigurasi.",
                ],
            },
            {
                "heading": "Cloudflare Workers: kode di edge",
                "bahasa": "javascript",
                "code": """// src/index.js
export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    if (url.pathname === '/api/jam') {
      return Response.json({ buka: '08.00', tutup: '22.00' });
    }
    return new Response('Halaman tidak ada', { status: 404 });
  },
};
...""",
            },
            {
                "body": [
                    "Edge artinya kodemu dijalankan di banyak server di seluruh dunia,",
                    "di lokasi yang paling dekat dengan pengguna. Cloudflare Workers",
                    "adalah runtime edge yang memakai API standar web yang sudah kamu",
                    "kenal: Request, Response, dan URL. Runtime-nya, workerd,",
                    "berlisensi Apache-2.0, dan alat CLI-nya Wrangler. Workers dipakai",
                    "luas sebagai target deploy Astro, SvelteKit, dan framework lain.",
                    "",
                    "Supaya kode yang sama bisa jalan di Node, Deno, Bun, dan runtime",
                    "edge, API sisi server lintas runtime ini dikoordinasikan di Ecma",
                    "TC55 (WinterTC).",
                    "",
                    "Jebakan: runtime edge bukan Node. Modul seperti fs nggak tersedia",
                    "atau terbatas, dan ada batas waktu CPU per permintaan. Kode yang",
                    "jalan di laptopmu dengan Node belum tentu jalan di edge.",
                ],
            },
            {
                "heading": "Tempat deploy situs frontend",
                "body": [
                    "  Layanan           Cocok untuk                    Paket gratis",
                    "  GitHub Pages      situs statis dari repo         repo publik",
                    "  Netlify           statis + fungsi serverless     ada",
                    "  Cloudflare Pages  statis + Workers               ada",
                    "  Vercel            Next.js dan framework lain     Hobby",
                    "  Railway           aplikasi + database            cek situsnya",
                    "  Render            statis, layanan web, database  cek situsnya",
                    "",
                    "Semua layanan ini proprietary, dan batas paket gratisnya bisa",
                    "berubah, jadi baca halaman harganya sebelum dipakai untuk proyek",
                    "kantor. Menurut State of JS 2025, setelah AWS, layanan hosting",
                    "yang paling banyak dipakai adalah Vercel (4.703 pemakai), GitHub",
                    "Pages (4.541), dan Netlify (3.180). Vercel dibahas di bab 12.",
                    "",
                    "Netlify mempopulerkan arsitektur Jamstack: situs statis ditambah",
                    "fungsi serverless. Cloudflare Pages menaruh situs statis di",
                    "jaringan Cloudflare dan tersambung dengan Workers. Cloudflare",
                    "juga mendorong Workers dengan static assets untuk situs baru, jadi",
                    "cek arah dokumentasi terbarunya. Railway dan Render lebih ke",
                    "aplikasi backend dan database, cocok kalau situsmu butuh server.",
                ],
            },
            {
                "heading": "Portofolio pertama di GitHub Pages",
                "bahasa": "terminal",
                "code": """# di folder berisi index.html (lihat kurikulum Git bab 4)
git init
git add .
git commit -m "Portofolio pertama"
git branch -M main
git remote add origin git@github.com:namakamu/portofolio.git
git push -u origin main

# lalu di GitHub: Settings > Pages > Deploy from a branch > main / (root)
# situsnya muncul di https://namakamu.github.io/portofolio/""",
            },
            {
                "body": [
                    "GitHub Pages gratis untuk repositori publik dan melayani berkas",
                    "statis langsung dari repo. Ada dua hal yang sering bikin bingung.",
                    "Pertama, GitHub Pages memproses repo dengan Jekyll secara bawaan.",
                    "Folder yang namanya diawali garis bawah ikut dibuang, jadi",
                    "tambahkan berkas kosong bernama .nojekyll kalau situsmu hasil",
                    "build alat lain. Kedua, situs proyek tinggal di subfolder",
                    "/portofolio/, jadi aplikasi Vite perlu base: '/portofolio/' di",
                    "konfigurasinya supaya berkas CSS dan JavaScript-nya ketemu.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Banyak programmer pemula menaruh CV dan portofolio di GitHub",
                    "Pages, lengkap dengan domain sendiri. Situs dokumentasi proyek",
                    "open source juga sering di-host di sana atau di Netlify dan",
                    "Cloudflare Pages, karena gratis dan setiap push langsung tayang.",
                    "",
                    "Kasus kecil: kamu membangun portofolio dengan Vite, men-deploy",
                    "folder dist ke GitHub Pages, tapi halamannya putih kosong. Konsol",
                    "browser menunjukkan galat 404 untuk /assets/index-abc123.js.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Perhatikan alamatnya: situsmu di",
                    "     namakamu.github.io/portofolio/, tapi berkasnya dicari di",
                    "     /assets/, tanpa /portofolio/.",
                    "  2. Tambahkan base ke vite.config.js:",
                    "       export default { base: '/portofolio/' };",
                    "  3. Bangun ulang dengan npm run build, lalu deploy lagi isi",
                    "     folder dist, dan tambahkan berkas .nojekyll.",
                    "  4. Buka situsnya, muat ulang tanpa cache (Ctrl+Shift+R), dan",
                    "     pastikan tab Network nggak lagi menunjukkan 404.",
                ],
            },
        ],
    },
]
