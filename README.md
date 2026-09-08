# Belajar Ngoding

Aplikasi belajar pemrograman berbahasa Indonesia, tanpa dependensi apa pun di
luar Python 3.8+ dan sebuah browser.

Bedanya dengan tutorial biasa: latihan codingnya **benar-benar dijalankan dan
dinilai otomatis** dari output programmu, bukan sekadar "intip jawaban" — dan
kalau salah, aplikasi menunjukkan **baris dan kolom mana** yang berbeda,
lengkap dengan tebakan penyebabnya.

Ada dua antarmuka di atas inti yang sama. Keduanya membaca dan menulis berkas
progres yang sama, jadi materi yang dibaca di browser langsung terhitung di
terminal — dan sebaliknya.

```bash
python3 belajar-web.py   # antarmuka web: editor kode, animasi, 4 tema
python3 main.py          # antarmuka terminal
```

## Antarmuka web

`python3 belajar-web.py` menyalakan server lokal lalu membuka browser. Tidak
ada yang dipasang, tidak ada yang dikirim ke internet, dan servernya hanya mau
mendengarkan di `127.0.0.1`.

**Editor kode di dalam halaman.** Sorot sintaks langsung saat mengetik,
indentasi otomatis, kurung yang menutup sendiri, Tab yang menambah indentasi
alih-alih memindahkan fokus, dan `Ctrl+/` untuk mengomentari baris. Ditulis
tangan di atas `<textarea>` — tidak ada CodeMirror, tidak ada langkah build.
Kodemu tetap disimpan ke `~/belajar-ngoding/kerjaanku/`, berkas yang sama yang
dipakai aplikasi terminal, jadi bisa dibuka di editor favoritmu kapan saja.

**Ruang Coba.** Halaman kosong untuk menjalankan kode apa pun di sepuluh
bahasa, lengkap dengan stdin. Tidak dinilai dan tidak menyentuh progres —
justru karena itu ia berguna. Tombol *Coba jalankan* di setiap contoh kode
materi membukanya di sini, sudah terisi.

**Catatanku.** Catatan pribadi per materi, kuis, dan latihan. Disimpan di
berkas terpisah dari progres, jadi mereset progres tidak ikut menghapus
tulisanmu.

**Palet perintah (`Ctrl+K`).** Ketik nama bahasa, judul materi, atau kata apa
pun; ia mencari sekaligus di daftar navigasi dan di seluruh isi kurikulum.

**Bentuknya dipinjam dari tiga tempat yang sudah memecahkan masalah ini.**
Pembacanya tiga kolom seperti [The Odin Project](https://www.theodinproject.com):
daftar materi di kiri, bacaan di tengah dengan lebar 68 karakter, dan peta
bagian di kanan yang penandanya mengikuti posisi bacamu. Kepala tiap bahasa
memakai baris fakta berikon seperti [Codecademy](https://www.codecademy.com) —
berapa materi, berapa kuis, berapa latihan, dan apakah kodenya bisa dijalankan
di komputer ini. Dan seperti [freeCodeCamp](https://www.freecodecamp.org),
tiap layar cuma punya SATU tindakan utama: kartu "Lanjutkan" adalah
satu-satunya permukaan amber pekat di seluruh aplikasi.

**Halaman latihan dibelah dua.** Soal menempel di kiri, editor di kanan. Susunan
sebelumnya menumpuk keduanya, jadi soalnya tergulir keluar layar tepat saat
kode mulai ditulis — dan menulis jawaban sambil lupa pertanyaannya adalah cara
tercepat mengerjakan latihan yang salah.

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

Pintasan lain: `?` daftar pintasan · `Ctrl+B` sembunyikan panel · `Ctrl+J`
ganti tema · `G` lalu `D`/`C`/`S`/`B` lompat antar layar · `Ctrl+⏎` jalankan
kode · `Ctrl+⇧+⏎` periksa jawaban · `1–9` atau `A–J` menjawab soal kuis.

## Isi

| Bahasa | Materi | Bab | Kuis | Soal | Latihan | Dinilai otomatis | Butuh |
|---|---:|---:|---:|---:|---:|---:|---|
| HTML | 22 | 6 | 5 | 40 | 12 | 12 | — tidak perlu apa pun |
| CSS | 26 | 8 | 5 | 40 | 12 | 12 | — tidak perlu apa pun |
| Java | 40 | 8 | 7 | 60 | 15 | 13 | `javac` `java` |
| SQL | 22 | 6 | 7 | 57 | 12 | 9 | `sqlite3` |
| Python | 44 | 11 | 7 | 56 | 18 | 17 | `python3` |
| JavaScript | 32 | 7 | 7 | 56 | 18 | 17 | `node` |
| C | 34 | 8 | 7 | 56 | 18 | 18 | `gcc` |
| C++ | 33 | 7 | 7 | 56 | 18 | 18 | `g++` |
| Bash | 25 | 6 | 5 | 40 | 14 | 14 | `bash` |
| Go | 28 | 7 | 6 | 48 | 14 | 14 | `go` |
| **Total** | **306** | **74** | **63** | **509** | **151** | **144** | |

Ditambah **Bikin Aplikasi** (28 materi, 7 bab, 4 kuis, 23 soal, 8 latihan) —
bukan bahasa baru melainkan kurikulum cara berpikir membangun aplikasi, memakai
Java. Seluruhnya: **334 materi dalam 81 bab, 67 kuis / 532 soal, 159 latihan**
(152 dinilai otomatis).

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
aplikasi memberi tahu **perintah persis** untuk memasangnya di sistemmu:

```
python3 main.py --cek-toolchain
```

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
edit. Ada 71 pola untuk sepuluh bahasa, termasuk keluhan struktur HTML.

**Kunci jawaban tidak ditulis dua kali.** Ekspektasi diturunkan dengan
menjalankan solusi contoh, jadi soal dan kunci mustahil jadi tidak sinkron.
Latihan bercabang diuji dengan beberapa input sekaligus, sehingga jawaban yang
di-hardcode tidak bisa lolos.

**Contoh kode bersorot sintaks** untuk kesepuluh bahasa — kata kunci, string,
komentar, angka, dan nama fungsi diwarnai berbeda, tanpa dependensi apa pun.

**Kuis yang tidak bisa ditebak.** Urutan soal dan opsi diacak, ada mode timer,
review jawaban salah, dan mode "ulangi yang salah saja" (yang tidak menyentuh
skor terbaikmu).

**Pengulangan terjadwal.** Kuis yang sudah dikerjakan dijadwalkan ulang dengan
interval yang melar sesuai skormu, lalu ditandai `[saatnya diulang]`.

**Materi terbagi jadi bab bertingkat, dan babnya terbuka bertahap.** 334 materi
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

**Navigasi.** Pencarian kata kunci lintas 11 bahasa dengan saringan tipe dan
kata kunci tersorot di hasilnya, bookmark, dan "lanjutkan dari terakhir" yang
juga menawarkan materi *berikutnya*.

**Gamifikasi.** XP, level bergelar, streak harian, target XP harian, heatmap
aktivitas 13 pekan, dan 22 badge.

**Bisa diatur.** Tema warna (gelap/terang/kontras tinggi/mono), kedalaman
warna, lebar layar, tinggi halaman, durasi timer, editor, dan target harian —
semua lewat menu Pengaturan, tersimpan di `~/.belajar_ngoding_config.json`.
Tampilannya mengikuti lebar terminal secara otomatis.

## Baris perintah

```
python3 main.py                    menu interaktif
python3 main.py --bantuan          daftar semua opsi
python3 main.py --cek-toolchain    compiler apa yang sudah/belum terpasang
python3 main.py --statistik        ringkasan progres, lalu keluar
python3 main.py --laporan          laporan kemajuan Markdown ke layar
python3 main.py --laporan x.md     ...atau ke berkas
python3 main.py --bahasa go        langsung buka satu bahasa
python3 main.py --tema terang      paksa tema
python3 main.py --tanpa-warna      matikan warna (juga hormati NO_COLOR)
python3 main.py --ekspor p.json    ekspor progres
python3 main.py --impor p.json     impor progres (progres lama dicadangkan)
```

## Struktur

```
INTI — dipakai kedua antarmuka
  progress.py      progres, XP, level, streak, badge, penjadwalan, ekspor/impor
  runner.py        eksekusi kode berbatas waktu/memori + pencocokan output
  sorot.py         penyorot sintaks 10 bahasa (pemindai token satu lintasan)
  beda.py          diff output harapan vs hasil + diagnosis penyebabnya
  galat.py         penerjemah pesan error compiler/runtime ke bahasa Indonesia
  berkas.py        menentukan blok kode itu berkas utuh, potongan, atau sesi
  saran.py         rekomendasi langkah berikutnya & tantangan harian
  bab.py           bab mana yang terbuka -- satu-satunya yang memutuskannya
  konfigurasi.py   preferensi pengguna yang bertahan antar sesi
  data/            konten kurikulum, 3 berkas per bahasa
  data/bab.py      pembagian materi jadi bab bertingkat

TERMINAL
  main.py          registry bahasa + menu utama, dashboard, pengaturan, CLI
  utils.py         helper tampilan terminal (lebar responsif, input, paginasi)
  tema.py          palet warna: deteksi kemampuan terminal + 4 tema
  materials.py     pembaca materi, bookmark, pencarian dalam satu bahasa
  quiz.py          mesin kuis
  exercises.py     latihan coding + auto-checker
  navigasi.py      pencarian global, bookmark, lanjut terakhir

WEB
  belajar-web.py   peluncur: nyalakan server, buka browser
  webapp/server.py server HTTP + penjagaan token, Origin, dan path
  webapp/api.py    endpoint JSON, membungkus hasil modul inti
  webapp/isi.py    konten kurikulum → struktur JSON siap render
  webapp/sesi.py   sesi kuis di memori (acak + pemetaan ulang jawaban)
  webapp/catatan.py catatan pribadi, berkas terpisah dari progres
  webapp/statik/   satu halaman, satu lembar gaya, sembilan modul JavaScript
  webapp/statik/js/gerak.js  mesin animasi: solver pegas, urutan, pemicu
  webapp/statik/js/ikon.js   24 ikon garis, satu keluarga, tanpa berkas gambar

  struktur.py      membaca HTML & CSS jadi pohon — "keluaran" kedua bahasa itu

tests/             678 tes
```

## Menambah bahasa baru

1. Buat `data/<bahasa>_materials.py`, `_quizzes.py`, `_exercises.py`.
2. Ekspor ketiganya di `data/__init__.py`.
3. Tambahkan satu entri di `LANGUAGES` pada `main.py`.
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
