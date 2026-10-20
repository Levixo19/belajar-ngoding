# belajar-codingV2

Aplikasi belajar pemrograman berbahasa Indonesia, tanpa dependensi apa pun di
luar Python 3.8+ dan sebuah browser.

Bedanya dengan tutorial biasa: latihan codingnya **benar-benar dijalankan dan
dinilai otomatis** dari output programmu, bukan sekadar "intip jawaban" — dan
kalau salah, aplikasi menunjukkan **baris dan kolom mana** yang berbeda,
lengkap dengan tebakan penyebabnya.

```bash
python3 belajar-web.py   # editor kode, animasi, 4 tema
```

Antarmuka terminal yang dulu ada sudah dibuang (2026-10-20). Satu-satunya
titik masuk sekarang `belajar-web.py`.

## Antarmuka web

`python3 belajar-web.py` menyalakan server lokal lalu membuka browser. Tidak
ada yang dipasang, tidak ada yang dikirim ke internet, dan servernya hanya mau
mendengarkan di `127.0.0.1`.

**Editor kode di dalam halaman.** Sorot sintaks langsung saat mengetik,
indentasi otomatis, kurung yang menutup sendiri, Tab yang menambah indentasi
alih-alih memindahkan fokus, dan `Ctrl+/` untuk mengomentari baris. Ditulis
tangan di atas `<textarea>` — tidak ada CodeMirror, tidak ada langkah build.
Kodemu tetap disimpan ke `~/belajar-ngoding/kerjaanku/` sebagai berkas biasa,
jadi bisa dibuka di editor favoritmu kapan saja.

**Ruang Coba.** Halaman kosong untuk menjalankan kode apa pun di sepuluh
bahasa, lengkap dengan stdin. Tidak dinilai dan tidak menyentuh progres —
justru karena itu ia berguna. Bentuknya sama persis dengan ruang kerja latihan,
karena gunanya memang sama. Tombol *Ruang Coba* di setiap contoh kode materi
membukanya di sini, sudah terisi.

**Catatanku.** Catatan pribadi per materi, kuis, dan latihan. Disimpan di
berkas terpisah dari progres, jadi mereset progres tidak ikut menghapus
tulisanmu.

**Palet perintah (`Ctrl+K`).** Ketik nama bahasa, judul materi, atau kata apa
pun; ia mencari sekaligus di daftar navigasi dan di seluruh isi kurikulum.

**Arah desainnya "buku kerja".** Kurikulumnya sudah bernomor sejak awal — 83
bab, 515 materi, tiap kuis dan latihan membawa nomornya sendiri — dan nomor itu
dijadikan arsitekturnya, bukan teks abu-abu di pojok baris: nomor bab tampil
sebesar judulnya sendiri, di kolomnya sendiri, dan mata memakainya sebagai
penggaris.

**Satu strip konteks, bukan remah roti.** Di tiap layar belajar ada satu baris
tempel yang menjawab empat hal sekaligus: kamu di bab mana, materi ke berapa
dari berapa, sejauh apa bab itu, dan satu tombol ke langkah berikutnya.
Keempatnya tidak ada di halamannya sendiri. Layar yang memang tidak punya
posisi — dasbor, statistik, pengaturan — tidak merendernya sama sekali.

**Bentuknya dipinjam dari tiga tempat yang sudah memecahkan masalah ini.**
Pembacanya tiga kolom seperti [The Odin Project](https://www.theodinproject.com):
jalur materi di kiri, bacaan di tengah dengan lebar yang bisa kamu setel, dan
peta bagian di kanan yang penandanya mengikuti posisi bacamu — dan ketiganya
ditengahkan, jadi tidak ada ruang mati antara akhir kalimat dan peta. Kepala
tiap bahasa memakai baris fakta berikon seperti
[Codecademy](https://www.codecademy.com) — berapa materi, berapa kuis, berapa
latihan, dan apakah kodenya bisa dijalankan di komputer ini. Dan seperti
[freeCodeCamp](https://www.freecodecamp.org), tiap layar cuma punya SATU
tindakan utama: kartu "Lanjutkan" adalah satu-satunya permukaan beraksen pekat
di seluruh aplikasi.

**Bab bisa dilipat, dan peta bab menggantikan gulungannya.** Satu bahasa bisa
punya sebelas bab berisi empat puluh materi; dirender penuh semuanya, halamannya
lima ribu piksel tanpa satu titik pun yang menjawab "ada berapa bab dan aku di
mana". Sekarang satu baris segmen bernomor menjawabnya tanpa digulir sama
sekali, dan yang terbuka secara bawaan cuma bab yang sedang dikerjakan. Bab yang
terkunci tetap terlihat utuh — judul, tingkat, kemajuan, dan alasannya semuanya
di kepala bab yang tidak pernah ikut terlipat.

**Halaman latihan adalah ruang kerja setinggi layar.** Soal menempel di kiri,
editor di kanan, dan editornya MENGISI ruangnya alih-alih tumbuh dari isinya —
kerangka tiga baris di atas empat ratus piksel kosong adalah ruang kerja yang
menolak dipakai bekerja. Tombolnya dikelompokkan menurut niat: dua tindakan
utama berdiri sendiri, alat-alat jadi satu kelompok rapat, dan "lihat contoh
solusi" turun ke panel bantuan di balik petunjuk-petunjuknya. Untuk orang yang
buntu, jalan termudah dan jalan terburuk tidak boleh berjarak sama.

**Dasbor punya layar pertama tersendiri.** Profil yang belum mengerjakan apa
pun tidak disambut heatmap 182 hari yang dingin dan sembilan belas kartu 0% — ia
disambut satu pertanyaan ("mau mulai dari mana?"), satu saran yang datang dari
antrean `saran.py`, lalu katalog kesembilan belas kurikulumnya sekaligus. Tiap ubin
menyebut berapa materi dan latihannya, serta berapa banyak yang harus dipasang
sebelum kodenya bisa dijalankan: "tanpa pasang apa pun" untuk HTML dan CSS,
"siap dijalankan" untuk yang compiler-nya sudah ada di komputer ini, "butuh
go" untuk yang belum. Yang belum siap tetap bisa dibuka — materi dan kuisnya
jalan penuh. Angka progres muncul sendiri begitu ada yang bisa dihitung.

**Ruang lebar dipakai dengan menambah kolom, bukan meregangkan baris.**
Daftar materi, kuis, dan latihan memecah diri jadi dua kolom begitu ruangnya
cukup, jadi sembilan belas latihan Python muat dalam satu layar 1440 px —
sebelumnya tiga layar. Meregangkan baris tidak akan pernah melakukan itu:
melebarkan daftar dari 960 ke 1909 px membuat tinggi halamannya tetap 2402 px
dan yang terlihat tetap tiga baris, cuma dengan delapan ratus piksel kosong
antara judul dan penandanya. Ruang kerja dan pembaca materi tetap memakai
lebar penuh karena tiap kolomnya sudah membatasi dirinya sendiri, dan dasbor
tetap dua kolom.

**Gerak yang menjawab, bukan yang memamerkan.** Halaman berpindah dengan
pegas sungguhan — bukan kurva `ease-out` yang disamakan untuk semua jarak —
kartu dan baris masuk berurutan saat tergulir ke layar, angka XP berjalan naik
alih-alih melompat, penanda di panel kiri meluncur dari satu menu ke menu
berikutnya, dan latihan yang lulus memercikkan bara. Mesinnya ditulis tangan
di `webapp/statik/js/gerak.js` dengan API yang meniru
[Motion](https://motion.dev) — `animasi`, `pegas`, `berurut`, `saatTampak`,
`saatGulir`, `tata` — tanpa satu byte pun dependensi dan tanpa langkah build.

**Tiga tingkat gerak**, bukan saklar nyala/mati: *penuh*, *halus* (tidak ada
yang bergerak sendiri, umpan balik sentuhan tetap ada), dan *mati*. Setelan
sistem "kurangi gerak" selalu menang atas ketiganya.

**Empat tema** — gelap, malam (hangat, kontras rendah, untuk mata yang lelah),
terang, dan kontras tinggi.

Pintasan lain: `?` daftar pintasan · `Ctrl+B` buka menu di layar sempit ·
`Ctrl+J` ganti tema · `G` lalu `D`/`C`/`S`/`B`/`N`/`P` lompat antar layar ·
`Ctrl+⏎` jalankan kode · `Ctrl+⇧+⏎` periksa jawaban · `1–9` atau `A–J`
menjawab soal kuis. Tombol Tab pertama di halaman selalu "Lompat ke isi", jadi
pemakai papan ketik tidak perlu melewati menu yang sama di tiap layar.

## Isi

| Bahasa | Materi | Bab | Kuis | Soal | Latihan | Dinilai otomatis | Butuh |
|---|---:|---:|---:|---:|---:|---:|---|
| HTML | 23 | 6 | 5 | 40 | 14 | 14 | — tidak perlu apa pun |
| CSS | 27 | 8 | 5 | 40 | 14 | 14 | — tidak perlu apa pun |
| Java | 41 | 8 | 7 | 64 | 16 | 14 | `javac` `java` |
| SQL | 22 | 6 | 7 | 57 | 13 | 10 | `sqlite3` |
| Python | 44 | 11 | 7 | 56 | 19 | 18 | `python3` |
| JavaScript | 35 | 9 | 7 | 56 | 22 | 18 | `node` |
| C | 34 | 8 | 7 | 56 | 19 | 19 | `gcc` |
| C++ | 33 | 7 | 7 | 56 | 19 | 19 | `g++` |
| Bash | 25 | 6 | 5 | 40 | 15 | 15 | `bash` |
| Go | 28 | 7 | 6 | 48 | 15 | 15 | `go` |
| C# | 27 | 7 | 6 | 48 | 16 | 16 | `dotnet` |
| Rust | 23 | 6 | 6 | 48 | 16 | 16 | `rustc` |
| PHP | 21 | 6 | 6 | 48 | 16 | 16 | `php` |
| Ruby | 21 | 6 | 6 | 48 | 16 | 16 | `ruby` |
| Kotlin | 18 | 6 | 6 | 48 | 16 | 16 | `kotlinc` `kotlin` |
| TypeScript | 16 | 6 | 6 | 48 | 16 | 16 | `tsc` `node` |
| Visual Basic | 16 | 6 | 6 | 48 | 16 | 16 | `dotnet` |
| **Total** | **454** | **119** | **105** | **849** | **278** | **268** | |

Ditambah dua kurikulum yang bukan bahasa baru:

| Kurikulum | Materi | Bab | Kuis | Soal | Latihan | Dinilai otomatis | Butuh |
|---|---:|---:|---:|---:|---:|---:|---|
| Bikin Aplikasi | 28 | 7 | 5 | 31 | 9 | 9 | `javac` `java` |
| CLI Fedora | 33 | 10 | 6 | 48 | 16 | 16 | `bash` |

**Bikin Aplikasi** melatih cara berpikir membangun aplikasi, bukan sintaks, dan
memakai Java. **CLI Fedora** mengajarkan mengoperasikan Linux Fedora dari
terminal — dari navigasi sampai SELinux, Btrfs, dan Podman.

Seluruhnya: **515 materi dalam 136 bab, 116 kuis / 928 soal,
303 latihan** (293 dinilai otomatis), ditutup **19 proyek akhir** —
satu per kurikulum.

**144 materi di antaranya baru ditambahkan setelah pemeriksaan cakupan.**
Kurikulumnya diaudit dari tiga sudut sekaligus — apa yang muncul di kode nyata,
apa yang ada di silabus baku, dan apa yang sudah DIPAKAI di soal latihan tanpa
pernah diajarkan lebih dulu. Yang terakhir itu kelas kesalahan paling
menyakitkan, karena pelajar menyalahkan dirinya sendiri. Contohnya: soal Kuis 1
HTML menuntut jawaban tentang urutan menutup tag yang bersilangan, dan tidak ada
satu baris pun di kurikulum yang pernah menjelaskannya; latihan Python
menyuruh "gunakan fixture pytest" padahal kata *fixture* nol kali muncul di
materinya; dan CSS tidak pernah menyebut `transition`, `transform`,
`@keyframes`, `box-shadow`, maupun `linear-gradient()` — sebagian besar isi
berkas CSS mana pun di dunia nyata.

**HTML dan CSS tidak membutuhkan apa pun untuk dipasang.** Keduanya satu-satunya
bahasa di daftar ini yang latihannya bisa dikerjakan DAN dinilai di komputer
mana pun yang sanggup menjalankan aplikasi ini — termasuk yang tidak punya satu
compiler pun. Karena itu keduanya berdiri paling depan: kalau kamu baru mulai
dan belum sanggup memasang apa-apa, mulailah dari sana.

Cara keduanya dinilai berbeda dari yang lain, dan itu disengaja. HTML dan CSS
tidak menjalankan apa pun, jadi tidak ada keluaran untuk dibandingkan. Yang
dibandingkan STRUKTURNYA: berkas HTML dibaca jadi pohon elemen, CSS jadi daftar
aturan yang sudah dirapikan. Untuk `<p class="a">Halo  dunia</p>` yang kamu
lihat adalah:

```
p class="a" "Halo dunia"
```

Itu juga yang membuatnya berguna untuk belajar: browser tidak pernah mengeluh
saat kamu lupa menutup tag — ia menebak sendiri, dan halamannya tetap tampil
"hampir benar". Pohon ini menunjukkan apa yang SEBENARNYA terbaca dari markup
itu, termasuk saat sebuah `<p>` ternyata tertelan masuk ke dalam `<div>` di
atasnya.

Toolchain bersifat opsional. Materi dan kuis tetap jalan penuh tanpa compiler
apa pun; yang mati hanya penilaian otomatis untuk bahasa bersangkutan — dan
aplikasi memberi tahu **perintah persis** untuk memasangnya di sistemmu. Tiap
kartu bahasa di dasbor menandainya sebelum diklik — "butuh go", "tanpa pasang
apa pun", atau "siap dijalankan" — jadi tidak ada tombol yang berujung
penolakan.

Latihan bahasa yang toolchain-nya belum ada tetap bisa dikerjakan dan ditandai
selesai secara manual, jadi progresnya tidak mentok di 0%.

## Fitur

**Latihan yang dinilai otomatis.** Tulis kode di editor favoritmu (`$EDITOR`,
atau mode ketik langsung kalau tidak ada), lalu aplikasi mengompilasi,
menjalankan, dan membandingkan outputmu dengan kunci jawaban. Statusnya jadi
`LULUS` hanya kalau outputnya benar-benar cocok **dan** programnya berakhir
normal.

**Umpan balik yang mengajar, bukan sekadar "GAGAL".** Kegagalan ditampilkan
sebagai diff bernomor baris dengan penunjuk kolom pertama yang berbeda, plus
diagnosis dalam bahasa manusia:

```
    1 │ Halo, namaku Andi!
    2 - Aku sedang belajar Python.   (diharapkan)
    2 + aku sedang belajar python.   (punyamu)
        ^ beda mulai kolom 1

  → Isinya sudah benar, hanya beda HURUF BESAR/KECIL.
```

Spasi tersembunyi ditampilkan sebagai `·` dan tab sebagai `→` saat dua baris
terlihat sama padahal tidak.

**Pesan error diterjemahkan.** `';' expected` jadi *"Ada baris yang lupa
diakhiri titik koma"*, path direktori sementara diganti nama berkas kerjamu,
dan nomor barisnya digeser supaya cocok dengan berkas yang benar-benar kamu
edit. Ada 71 pola lintas bahasa, termasuk keluhan struktur HTML.

**Kunci jawaban tidak ditulis dua kali.** Ekspektasi diturunkan dengan
menjalankan solusi contoh, jadi soal dan kunci mustahil jadi tidak sinkron.
Latihan bercabang diuji dengan beberapa input sekaligus, sehingga jawaban yang
di-hardcode tidak bisa lolos.

**Contoh kode bersorot sintaks** untuk kedelapan belas bahasa — kata kunci, string,
komentar, angka, dan nama fungsi diwarnai berbeda, tanpa dependensi apa pun.

**Kuis yang tidak bisa ditebak.** Urutan soal dan opsi diacak, ada mode timer,
review jawaban salah, dan mode "ulangi yang salah saja" (yang tidak menyentuh
skor terbaikmu).

**Pengulangan terjadwal.** Kuis yang sudah dikerjakan dijadwalkan ulang dengan
interval yang melar sesuai skormu, lalu ditandai `[saatnya diulang]`.

**Materi terbagi jadi bab bertingkat, dan babnya terbuka bertahap.** 515 materi
yang berbaris rata dari atas ke bawah adalah daftar, bukan jalur — daftar
sepanjang itu tidak memberi tahu apa pun tentang mana yang harus lebih dulu dan
sudah sampai mana kamu sekarang. Tiap bahasa dibagi jadi 6–11 bab bertanda
*Dasar*, *Menengah*, atau *Mahir*, dan bab berikutnya terbuka begitu seluruh
materi bab sebelumnya dibaca sampai habis.

Yang menguncinya hanya BACAAN — bukan kuis, bukan latihan. Itu disengaja: satu
latihan sulit yang belum ditaklukkan akan mengunci seluruh sisa kurikulum, dan
orang yang mandek di situ tidak punya apa pun lagi untuk dikerjakan selain hal
yang sedang membuatnya mandek. Bab yang terkunci tetap ditampilkan lengkap
dengan judul, tingkat, jumlah materi, dan berapa materi lagi yang kurang —
menyembunyikannya justru menghapus alasan bab itu ada. Sudah tahu semuanya? Ada
saklar *Buka semua bab tanpa syarat* di Pengaturan.

**Penunjuk arah.** Menu utama menampilkan *Langkah berikutnya* yang disusun
dari progresmu sendiri — kuis yang jatuh tempo dulu, lalu materi yang berhenti
di tengah, lalu materi/latihan/kuis berikutnya di bahasa yang sedang kamu
pelajari. Ada juga **tantangan harian** yang berganti tiap hari.

**Navigasi.** Pencarian kata kunci lintas 19 kurikulum dengan saringan tipe dan
kata kunci tersorot di hasilnya, bookmark, dan "lanjutkan dari terakhir" yang
juga menawarkan materi *berikutnya*.

**Gamifikasi.** XP, level bergelar, streak harian, target XP harian, heatmap
aktivitas 13 pekan, dan 22 badge.

**Bisa diatur.** Tema warna (gelap/terang/kontras tinggi/mono), kedalaman
warna, lebar layar, tinggi halaman, durasi timer, editor, dan target harian —
semua lewat menu Pengaturan, tersimpan di `~/.belajar_ngoding_config.json`.
Tampilannya mengikuti lebar terminal secara otomatis.

## Struktur

Folder mengikuti arah ketergantungan, bukan selera: tidak ada satu paket pun
yang mengimpor paket di atasnya.

```
belajar-web.py     satu-satunya titik masuk: nyalakan server, buka browser

inti/              mesin; tidak tahu apa-apa soal antarmuka
  kurikulum.py     registry LANGUAGES, versi, statistik, laporan kemajuan
  latihan.py       logika latihan: nama berkas kerja, kerangka, kunci jawaban
  materi.py        isi materi sebagai teks biasa, dipakai pencarian
  runner.py        eksekusi kode berbatas waktu/memori + pencocokan output
  struktur.py      membaca HTML & CSS jadi pohon — "keluaran" kedua bahasa itu
  sorot.py         penyorot sintaks: 19 set aturan + 16 alias
  berkas.py        menentukan blok kode itu berkas utuh, potongan, atau sesi
  galat.py         penerjemah pesan error compiler/runtime ke bahasa Indonesia
  beda.py          diff output harapan vs hasil + diagnosis penyebabnya
  visual.py        spesifikasi gambar konsep materi (13 jenis)
  jejak.py         pelacak langkah program Python ("Lihat jalannya")
  pustaka.py       9.809 tautan belajar beratribusi

pelajar/           keadaan & aturan yang melekat pada orangnya
  progress.py      progres, XP, level, streak, badge, penjadwalan, ekspor/impor
  bab.py           bab mana yang terbuka — satu-satunya yang memutuskannya
  konfigurasi.py   preferensi pengguna yang bertahan antar sesi
  simpanan.py      baca/tulis JSON pelajar: karantina, .bak, lapor gagal simpan
  saran.py         rekomendasi langkah berikutnya & tantangan harian
  karier.py        kesiapan 21 profesi dari persen kurikulum yang sama

webapp/            antarmuka web di atas modul yang sama
  server.py        server HTTP + penjagaan token, Origin, dan path
  api.py           endpoint JSON, membungkus hasil modul inti
  isi.py           konten kurikulum → struktur JSON siap render
  sesi.py          sesi kuis di memori (acak + pemetaan ulang jawaban)
  catatan.py       catatan pribadi, berkas terpisah dari progres
  statik/          satu halaman, satu lembar gaya, modul JavaScript
  statik/js/gerak.js      mesin animasi: solver pegas, urutan, pemicu
  statik/js/pratinjau.js  bingkai pratinjau halaman HTML/CSS pelajar
  statik/js/ikon.js       24 ikon garis, satu keluarga, tanpa berkas gambar

packages/          sisi TypeScript (workspace npm, tanpa langkah build)
  konten/          seluruh kurikulum sebagai JSON + tipe TS (DIHASILKAN)
  bersama/         sorot, beda, galat sebagai satu implementasi TS + golden

data/              konten kurikulum, 3 berkas per kurikulum
  bab.py           pembagian materi jadi bab bertingkat (dihasilkan, bukan diketik)

alat/              alat baris perintah: ekspor, pemeriksa, penulis naskah
contoh/            bukan bagian aplikasi; tidak ada yang mengimpornya
tests/             suite Python; sisi TS diuji lewat packages/bersama/uji/
```

`inti/struktur.py` sengaja duduk bersebelahan dengan `inti/runner.py`: runner
memanggilnya sebagai subprocess lewat `dirname(__file__)`, jadi memisahkan
keduanya diam-diam mematikan penilaian seluruh latihan HTML dan CSS.

## Menambah bahasa baru

1. Buat `data/<bahasa>_materials.py`, `_quizzes.py`, `_exercises.py`.
2. Ekspor ketiganya di `data/__init__.py`.
3. Tambahkan satu entri di `LANGUAGES` pada `inti/kurikulum.py`.
4. Kalau kodenya perlu bisa dijalankan, tambahkan `Toolchain` di
   `runner.TOOLCHAINS` — termasuk field `instalasi` per sistem operasi.
5. Tambahkan aturan leksikal di `sorot.ATURAN` supaya contoh kodenya tersorot.

`tests/test_data.py`, `tests/test_sorot.py`, dan `tests/test_solutions.py`
otomatis ikut memvalidasi konten baru itu.

### Format data latihan

```python
{
    "title": "Latihan 1: ...",       # wajib unik dalam satu bahasa
    "difficulty": "Mudah",           # Mudah | Menengah | Lanjut | Sulit
    "question": ["baris soal", ...],
    "hints": ["hint 1", ...],        # dibuka bertahap; MENUNTUN, bukan jawaban
    "solution": "...",               # program lengkap yang bisa dijalankan
    "stdin": "80\n",                 # opsional: satu input untuk program
    "stdin_list": ["80\n", "60\n"],  # lebih baik: beberapa kasus uji
    "mode": "persis",                # persis|abaikan_kapital|mengandung|regex|angka
    "setup": "...",                  # opsional: kode prasyarat, ditempel di depan
    "verifikasi": "...",             # opsional: kode pemeriksa, ditempel di belakang
    "auto_check": False,             # opsional: matikan penilaian otomatis
    "alasan_tidak_dicek": "...",     # wajib kalau auto_check False
}
```

Aturan penting:

- **Output solusi harus deterministik.** Bilangan acak, tanggal saat ini, dan
  iterasi map di Go akan membuat latihan mustahil lulus.
  `tests/test_solutions.py` menjalankan tiap solusi dua kali untuk memastikannya.
- **Latihan yang membaca input tidak boleh mencetak teks ajakan** sebelum
  pembacaan pertama — teks itu akan ikut jadi bagian kunci jawaban.
- **Latihan bercabang wajib pakai `stdin_list`** dengan input yang benar-benar
  menempuh cabang berbeda. Dengan satu input saja, jawaban yang di-hardcode
  ikut dinyatakan benar.

## Menjalankan tes

```bash
python3 -m unittest discover -s tests -t .              # semua (lambat, kompilasi ratusan program)
BELAJAR_SKIP_LAMBAT=1 python3 -m unittest discover -s tests -t .   # lewati verifikasi solusi
BELAJAR_BAHASA=go python3 -m unittest tests.test_solutions          # satu bahasa saja
```

Yang diperiksa:

- **test_data** struktur konten, judul unik, index jawaban valid, sebaran
  posisi jawaban merata, larangan mencetak prompt sebelum membaca input
- **test_progress** simpan/muat, migrasi skema lama, ketahanan terhadap berkas
  rusak *bertipe salah*, XP, level, streak, badge, penjadwalan, ekspor/impor
- **test_runner** eksekusi, timeout, batas memori/berkas/output, pembunuhan
  proses cucu, mode aman SQLite, exit code ikut dinilai
- **test_solutions** tiap solusi contoh berjalan, mencetak output, deterministik,
  dan lolos auto-checker-nya sendiri — dengan bahasa tanpa toolchain dilaporkan
  sebagai `skipped`, bukan dilewati diam-diam
- **test_quiz** pemetaan ulang jawaban setelah opsi diacak, EOF, sesi ulang yang
  tidak merusak skor
- **test_navigasi** pencarian, bookmark basi, lanjut terakhir
- **test_sorot** keutuhan tokenizer atas SELURUH kode di kurikulum
- **test_web.TestMesinGerak** solver pegas di `gerak.js` diadu di Node dengan
  sifat yang harus berlaku: kurva mulai di 0 dan berakhir di 1, pegas tanpa
  pantul tidak pernah melewati sasaran maupun turun di tengah (itu kedipan),
  `durasiTampak` benar-benar mengendalikan lamanya, dan urutan tidak pernah
  membuat daftar panjang menunggu melewati batasnya
- **test_beda** diff & diagnosis, kesepakatan dengan `runner.normalisasi`
- **test_galat** terjemahan error & penggeseran nomor baris
- **test_konfigurasi** validasi nilai ngawur, tema, kedalaman warna
- **test_saran** urutan prioritas rekomendasi & stabilitas tantangan harian
- **test_ui** helper tampilan + smoke test alur aplikasi lewat stdin palsu
- **test_web** penjagaan server dari sudut penyerang (tanpa token, Origin
  asing, DNS rebinding, path traversal, bind non-loopback), endpoint JSON,
  catatan yang selamat dari reset progres, seluruh 57 kuis dikerjakan dengan
  jawaban benar untuk membuktikan pemetaan ulang index-nya utuh, dan penyorot
  JavaScript diadu melawan `sorot.py` atas seluruh kode kurikulum

## Lokasi data

| Apa | Di mana | Ubah lewat |
|---|---|---|
| Progres belajar | `~/.belajar_ngoding_progress.json` | `BELAJAR_PROGRESS_FILE` |
| Pengaturan | `~/.belajar_ngoding_config.json` | `BELAJAR_CONFIG_FILE` |
| Catatan pribadi | `~/.belajar_ngoding_catatan.json` | `BELAJAR_CATATAN_FILE` |
| Kode jawabanmu | `~/belajar-ngoding/kerjaanku/` | `BELAJAR_WORKSPACE` |

Catatan pribadi sengaja tinggal di berkasnya sendiri: `Reset progres` ada dan
memang dipakai, dan "kosongkan nilai Java" tidak boleh diam-diam ikut membakar
tulisan tanganmu. Progres bisa dikumpulkan lagi dengan belajar ulang; catatan
tidak.

Keempat nama di tabel itu memakai `belajar_ngoding`/`belajar-ngoding`, nama
lama aplikasi ini, dan **sengaja tidak ikut diganti** saat proyeknya berganti
nama. Alasannya bukan kemalasan: mengganti nama di situ tidak menimbulkan satu
pun error — aplikasinya cuma akan membuka berkas baru yang kosong, dan yang
terlihat adalah progres, catatan, serta seluruh kode yang pernah kamu tulis
hilang. Kalau suatu saat memang mau diganti, jalurnya pemindahan yang
disengaja: baca nama baru dulu, jatuh ke nama lama kalau belum ada, salin
sekali, dan sisakan cadangannya.

Preferensi tampilan web (tema, ukuran huruf, saklar animasi, lebar kolom baca)
disimpan di browser, bukan di berkas mana pun — tema yang enak di terminal dan
tema yang enak di browser tidak harus sama.

Progres dari versi lama (`.belajar_java_progress.json` di folder yang sama)
dibaca dan dimigrasi otomatis pada peluncuran pertama. Berkas progres yang
rusak — termasuk yang bertipe salah karena diedit tangan — tidak akan
menghentikan aplikasi; field yang rusak diganti nilai bawaan, sisanya
dipertahankan.

## Catatan keamanan

Runner membatasi waktu CPU, memori, ukuran file, dan panjang output supaya kode
pemula yang keliru (misalnya loop tak berujung) tidak menggantung sistem.
Keluaran program ditulis ke berkas di dalam direktori sementara, bukan ditampung
di memori aplikasi, dan seluruh process group dibunuh saat timeout sehingga
proses cucu tidak ada yang selamat. Latihan SQL dijalankan dengan `sqlite3 -safe`
kalau versinya mendukung, sehingga dot-command tidak bisa menulis di luar
direktori sementara.

Ini tetap **bukan sandbox keamanan**. Kode berjalan dengan hak akses user yang
sama dengan aplikasi. Jangan menjalankan kode dari sumber yang tidak kamu
percaya.

### Khusus antarmuka web

Server web menjalankan kode, dan itu membuat satu hal penting: halaman web mana
pun yang kebetulan terbuka di browser yang sama secara teknis bisa mengirim
permintaan ke `http://127.0.0.1:7777`. "Localhost saja" bukan pengaman. Tiga
lapis penjagaan menutupnya:

1. **Token acak per-jalannya server**, ditanam ke dalam halaman dan wajib
   disertakan di setiap panggilan API. Situs lain tidak bisa membacanya karena
   tidak bisa membaca isi halaman kita.
2. **Header khusus memicu CORS preflight**, dan server ini tidak pernah
   mengizinkan asal lain — jadi preflight-nya gagal dan permintaan aslinya
   tidak pernah terkirim.
3. **Host dan Origin diperiksa**, menutup serangan DNS rebinding.

Alamat bind dikunci ke loopback: `server.buat()` menolak host selain
`127.0.0.1` dengan error. Menyalakannya di `0.0.0.0` berarti setiap mesin di
jaringan yang sama bisa menjalankan kode di komputer ini.
