# Catatan untuk agen

Aplikasi belajar pemrograman berbahasa Indonesia dengan **dua antarmuka** —
terminal dan web — di atas satu inti yang sama. **Tanpa dependensi yang perlu
dipasang**: Python 3.8+ dan stdlib saja di sisi server, plus JavaScript tanpa
langkah build. Runner, penyorot sintaks, diff, tema, server HTTP, dan editor
kode semuanya ditulis tangan, dan tetap begitu.

**Pengecualian di sisi web, atas keputusan pemilik (2026-10-13):** pustaka
front-end BOLEH dipakai kalau ia menambah kemampuan yang belum ada — dengan
dua syarat. Berkasnya DISIMPAN di `webapp/statik/vendor/` beserta header
lisensinya (aplikasi ini wajib utuh tanpa internet; tidak ada CDN), dan
aplikasinya tetap jalan kalau berkas itu gagal dimuat. Yang dipakai sekarang
cuma GSAP 3.15.0 + SplitText + ScrollTrigger (lisensi standar tanpa biaya,
gsap.com/standard-license), untuk judul layar "pintu" di `sinema.js` dan gerak
gulir beranda di `beranda.js`. Jangan
memakai pustaka untuk sesuatu yang sudah dikerjakan `gerak.js` (pegas, FLIP
lewat `tata()`, magnet, ungkap) — dua mesin untuk satu pekerjaan saling
mengejar.

Semua nama fungsi, variabel, komentar, docstring, dan teks antarmuka memakai
**Bahasa Indonesia**. Ikuti gaya yang sudah ada.

Status: 32 kurikulum, 1.062 materi dalam 287 bab bertingkat, 266 kuis / 2.159
soal, 558 latihan termasuk 32 proyek akhir, 1308 tes. Dua puluh kurikulum
pertama mengajarkan BAHASA; dua belas sisanya ranah tech stack (lihat
"Kurikulum tech stack" di bawah).
Tiap materi ditutup bagian "Di dunia nyata" (kasus nyata + cara memecahkannya),
dan 1.356 gambar konsep tersebar di 1.049 materi (lihat "Observatorium").
Ditambah Pustaka (9.809 tautan belajar beratribusi) dan Peta Karier (21 profesi).

144 materi ditambahkan sekaligus setelah audit cakupan tiga sudut (kode nyata,
silabus baku, dan prasyarat yang dipakai soal tapi tidak pernah diajarkan).
Rencana lengkapnya beserta buktinya ada di riwayat sesi; yang mengikat sekarang
cuma satu: TOLOK UKUR kurikulum ini bukan "berapa materinya" melainkan "adakah
istilah di kode nyata yang tidak pernah disebut". Sebelum menambah bahasa atau
menyatakan sebuah bahasa selesai, telusuri dulu apa yang HILANG, bukan menata
ulang yang sudah ada.

## Menjalankan

```bash
python3 main.py          # antarmuka terminal
python3 belajar-web.py   # antarmuka web (membuka browser sendiri)

python3 -m unittest discover -s tests -t .                        # semua (~3,5 menit)
BELAJAR_SKIP_LAMBAT=1 python3 -m unittest discover -s tests -t .  # ~40 detik
BELAJAR_BAHASA=go python3 -m unittest tests.test_solutions        # satu bahasa
```

Tes lambat mengompilasi ratusan program latihan. Jalankan versi penuh sebelum
commit apa pun yang menyentuh `data/`, `inti/runner.py`, atau
`layar/exercises.py`.

## Peta modul

Tiga paket, dibagi menurut arah ketergantungan yang SUDAH ada di kode — bukan
menurut selera. Tidak ada satu paket pun yang mengimpor paket di atasnya, dan
itulah satu-satunya alasan pembagian ini berarti: begitu ada yang membaliknya,
namanya berhenti memberi tahu apa pun.

| Modul | Tanggung jawab |
|---|---|
| `main.py` | Registry `LANGUAGES` + menu utama & dashboard. Tetap di AKAR karena ia titik masuk (`python3 main.py`) |
| **`inti/`** | **Mesin. Tidak tahu ada antarmuka terminal atau web** |
| `inti/runner.py` | Eksekusi kode berbatas waktu/memori + pencocokan output |
| `inti/struktur.py` | Membaca HTML & CSS jadi pohon — itu "keluaran" kedua bahasa itu |
| `inti/sorot.py` | Penyorot sintaks 10 bahasa, pemindai token satu lintasan |
| `inti/berkas.py` | Menentukan sebuah blok kode itu berkas, potongan, sesi, multi, atau ilustrasi |
| `inti/galat.py` | Menerjemahkan pesan compiler ke bahasa manusia |
| `inti/beda.py` | Menjelaskan kenapa output pelajar berbeda |
| `inti/tema.py` | Warna diminta lewat PERAN (`"galat"`, `"kode_kunci"`), bukan ANSI mentah |
| **`pelajar/`** | **Keadaan & aturan yang melekat pada orangnya** |
| `pelajar/progress.py` | Progres, XP, level, streak, badge, penjadwalan ulang |
| `pelajar/bab.py` | Bab mana yang terbuka. SATU-SATUNYA yang memutuskan penguncian |
| `pelajar/konfigurasi.py` | Preferensi tampilan, sengaja TERPISAH dari progres |
| `pelajar/saran.py` | Antrean "habis ini ngapain", tantangan harian, kuis yang paling perlu diulang |
| `pelajar/simpanan.py` | Baca/tulis JSON pelajar: berkas rusak DIKARANTINA, `.bak` bergulir, gagal simpan dilaporkan |
| `pelajar/kuis_materi.py` | Kuis -> materi yang diujinya (kesiapan kuis, "Baca lagi"); datanya `data/kuis_materi.py` |
| `pelajar/waktu.py` | Perkiraan menit materi/kuis/latihan, satu rumus untuk terminal dan web |
| `pelajar/tebak.py` | "Tebak keluarannya": contoh materi yang layak ditebak dan pemilihan kartunya |
| **`layar/`** | **Antarmuka terminal. Satu-satunya lapisan yang mencetak** |
| `layar/utils.py` | Primitif tampilan: paginasi, menu, input, pembungkus baris |
| `layar/materials.py` `layar/quiz.py` `layar/exercises.py` `layar/navigasi.py` | Layar-layar terminal |
| `data/bab.py` | Pembagian materi jadi bab bertingkat. DIHASILKAN, bukan diketik |

**`inti/struktur.py` wajib tetap bersebelahan dengan `inti/runner.py`.** Runner
memanggilnya sebagai subprocess lewat
`os.path.join(os.path.dirname(os.path.abspath(__file__)), "struktur.py")`.
Memisahkan keduanya tidak menimbulkan error impor di mana pun — yang terjadi
cuma SELURUH latihan HTML dan CSS berhenti bisa dinilai, dan pesannya berupa
"berkas tidak ditemukan" dari subprocess yang tidak ada yang membacanya.

**`layar/exercises.py` belum sepenuhnya "layar".** `webapp/api.py` memakainya
untuk `bangun_tests`, `DIR_KERJA`, dan `_kerangka` — logika latihan, bukan
tampilan. Begitu juga `main.py` yang memegang registry `LANGUAGES` sekaligus
menu terminal. Keduanya warisan, dan memindahkan isinya sekarang berarti
mengubah PERILAKU, bukan sekadar merapikan berkas. Catat, jangan tambal.

`layar/materials.py` sekarang DUA TINGKAT: daftar bab dulu, baru materi di
dalamnya. Penjagaan penguncian duduk di `render_material`, bukan di menunya,
karena itulah satu-satunya pintu masuk materi di terminal — menu bab, pencarian
lokal, pencarian global, bookmark, "lanjutkan yang terakhir", dan antrean saran
semuanya berakhir di fungsi itu.

`layar/utils.C` menyimpan ANSI mentah dan masih dipakai di beberapa tempat lama.
Untuk kode baru pakai `tema.cat(teks, "peran")`.

### Antarmuka web

Lapisan penyajian di atas modul yang sama. Ia tidak memiliki satu pun aturan
belajar sendiri — semuanya dipinjam.

| Modul | Tanggung jawab |
|---|---|
| `belajar-web.py` | Peluncur: nyalakan server, buka browser. Tetap di AKAR, sama seperti `main.py` |
| `webapp/server.py` | HTTP, tabel rute, dan TIGA lapis penjagaan |
| `webapp/api.py` | Endpoint JSON; membungkus hasil modul inti |
| `webapp/isi.py` | Konten kurikulum → struktur JSON (blok, token, petunjuk) |
| `webapp/sesi.py` | Sesi kuis di memori (pengacakan + pemetaan ulang jawaban) |
| `webapp/catatan.py` | Catatan pribadi, berkas TERPISAH dari progres |
| `statik/js/gerak.js` | Mesin animasi: solver pegas, urutan, pemicu, isyarat |
| `statik/js/sinema.js` | Judul layar "pintu" yang tiba kata demi kata (GSAP SplitText, hanya tingkat gerak penuh) |
| `statik/js/permukaan.js` | Sorot samar di bawah kursor pada baris, kartu, dan kartu Lanjutkan (mouse saja) |
| `statik/js/istirahat.js` | Pengingat istirahat mata 20-20-20, menghitung waktu AKTIF saja |
| `statik/js/beranda.js` | Beranda: kalimat yang menyala saat digulir, akordeon bahasa, marquee kurikulum, gerak gulir (ScrollTrigger, hanya tingkat gerak penuh) |
| `statik/js/sampul.js` | Gambar sampul SVG generatif (bahasa, bab, profesi), deterministik dari namanya; hiasan, aria-hidden |
| `statik/js/layar-pustaka.js` | Layar Pustaka: cari dan saring 9.809 tautan dari `/api/pustaka` |
| `statik/js/layar-karier.js` | Layar Peta Karier: tangga karier SVG, panel rincian, kuis, perencana jalur, "Jadikan tujuanku" |
| `statik/js/layar-tebak.js` | Layar "Tebak keluarannya" (`#/tebak/<key>`): lima kartu contoh materi, kunci dari server |
| `statik/vendor/gsap/` | GSAP 3.15.0 + SplitText + ScrollTrigger, disimpan lokal, header lisensi utuh |
| `statik/js/visual.js` | Penggambar SVG gambar konsep materi (13 jenis); spesifikasinya di `inti/visual.py` |
| `statik/js/jejak.js` | Panel "Lihat jalannya": rekaman langkah program Python dari `/api/jejak` |
| `statik/js/langit.js` | Langit malam di belakang aplikasi: graticule kutub, bintang bermagnitudo, kelip & paralaks (penuh saja) |
| `statik/js/kursor.js` | Reticle teleskop yang mengunci sasaran klik dan fokus papan ketik; kursor asli tidak disembunyikan |
| `statik/js/rasi.js` | Peta rasi: materi = bintang, bab = rasi; dipakai kepala halaman bahasa dan panel "Langitmu" dasbor |
| `statik/js/layar-langit.js` | Layar Langit (`#/langit`): 20 kurikulum sebagai rasi, garis profesi, konsep yang sama |
| `statik/huruf/` | Atkinson Hyperlegible Next + Mono (prosa, kode), Jost (antarmuka), Bodoni Moda (judul besar); semua OFL, lokal |
| `statik/js/sorot.js` | Port `inti/sorot.py` ke JS untuk penyorotan langsung di editor |
| `statik/js/editor.js` | Editor kode: textarea transparan di atas `<pre>` bertoken |
| `statik/js/pratinjau.js` | Bingkai pratinjau halaman HTML/CSS pelajar (sandbox, tanpa allow-same-origin) |
| `statik/js/layar-*.js` | Layar-layar web |
| `statik/js/ikon.js` | 24 ikon garis SVG, satu keluarga, mewarisi currentColor |
| `statik/gaya.css` | Satu lembar gaya; 4 tema; aturan gerak & arah desain di dalamnya |

## Invarian yang gampang dilanggar

Semuanya dijaga tes. Kalau salah satu gagal, itu bukan tes yang cerewet —
itu bug yang akan menyakiti pelajar.

**Cara membaca `invarian #N` di komentar `webapp/statik/` dan `tests/test_web.py`.**
Nomor itu lahir dari daftar periksa paket upgrade UI, dan paket itu TIDAK ikut
ada di repo ini — yang mengikat selalu rumusan yang ditulis di bawah (atau di
komentar itu sendiri, yang biasanya sudah menamai aturannya). Peta yang dipakai
sekarang: **#1** = siapa yang memasang `fill: "forwards"` wajib membatalkannya;
**#2** = satu properti, satu mesin; **#3** = `tingkatGerak()` satu-satunya yang
memutuskan tingkat gerak, dan `prefers-reduced-motion` selalu menang; **#11** =
satu definisi "lulus" (`runner.periksa`), dan "hari belajar" bukan "hari ada
XP"; **#12** = penguncian bab hanya diputuskan `pelajar/bab.py`, kalimat
aturannya juga datang dari sana; **#15a** = apa pun yang mengukur tata letak
wajib lewat `saatSiap()`, bukan `requestAnimationFrame` polos. Kode baru
MENAMAI aturannya, tidak menomorinya — `#3` pernah dipakai untuk dua aturan
berbeda di berkas yang sama sebelum rujukan itu dibersihkan.

**Blok perintah kurikulum Fedora WAJIB terklasifikasi SESI, bukan PROGRAM.**
Ini invarian keamanan, bukan kosmetik. Materi `CLI Fedora` berisi perintah
sungguhan seperti `sudo dnf5 install`, `systemctl enable`, dan `mkfs.ext4`.
Kalau `jenis_kode` menyebutnya PROGRAM, dua hal terjadi sekaligus: aplikasi
menawarkan tombol *Jalankan* yang benar-benar mengeksekusinya di mesin pelajar,
DAN `test_solutions.test_janji_keluaran_di_materi` menjalankannya di mesin
siapa pun yang menjalankan tes. Karena itu runner-nya diberi key `fedora`
tersendiri meski eksekutornya tetap bash, dan `inti/berkas.py` menyebut blok
Fedora PROGRAM hanya kalau baris pertamanya shebang. Jangan pernah mengubah
runner Fedora jadi `bash` "karena toh sama saja" -- persis di situ pagarnya.

Latihannya sendiri memang skrip sungguhan dan memang dijalankan. Itu aman
karena semuanya bekerja di direktori `mktemp -d`, dengan hak pengguna biasa,
dan tidak satu pun memerlukan sudo. Pertahankan sifat itu saat menambah
latihan Fedora baru.

**Kurikulum Git ikut pagar yang sama, ditambah dua hal yang tidak kelihatan.**
Blok perintah materinya SESI (`inti/berkas.py` memperlakukan `git` persis
seperti `fedora`): `git reset --hard` dan `git push --force` di sana ditujukan
ke repositori MILIK PELAJAR. Latihannya skrip bershebang yang membuat
repositori sendiri di `mktemp -d`, dan kerangka editornya (`layar/exercises.py`)
sudah memuat baris itu supaya skrip yang salah ketik tidak pernah menyentuh
repositori sungguhan. Dua hal yang tidak kelihatan:

* Runner `git` memasang `GIT_CONFIG_NOSYSTEM`, `GIT_EDITOR=true`, dan TANGGAL
  yang dipatok lewat `lingkungan`. Tanpa tanggal tetap, `git log` biasa pada
  riwayat bercabang mengurutkan commit menurut DETIK ia dibuat, dan latihan
  yang sama bisa lulus di satu mesin lalu gagal di mesin yang lebih lambat.
  Identitas (`user.name`) sengaja TIDAK dipasang di env: `GIT_AUTHOR_NAME`
  menimpa `git config` di repo, dan proyek akhirnya butuh dua nama penulis.
  Tiap skrip mengatur identitasnya sendiri, persis seperti yang diajarkan
  materi 2.
* `git log --graph` mengurutkan dengan TUMPUKAN, bebas dari tanggal, jadi graf
  riwayat aman dicetak apa adanya. `git log --reverse` pada riwayat ber-merge
  tidak: beri `--first-parent`, atau cetak hitungannya saja. Keluaran latihan
  tidak boleh memuat hash, tanggal, atau jalur absolut -- ketiganya berbeda
  di tiap mesin, dan `test_solutions` menjalankan tiap solusi dua kali.

**Solusi latihan harus deterministik.** Auto-checker menurunkan kunci jawaban
dengan menjalankan solusi contoh. Bilangan acak, tanggal saat ini, iterasi map
Go, dan panggilan jaringan membuat latihan mustahil lulus. `test_solutions`
menjalankan tiap solusi dua kali dan membandingkannya.

**Latihan ber-`stdin` tidak boleh mencetak prompt.** Kalau solusi mencetak
`"Masukkan nilai: "`, teks itu ikut jadi bagian kunci jawaban, dan pelajar yang
menulis `input()` polos — yang justru lebih tepat — selalu dianggap salah.

**Latihan yang dinilai otomatis tidak boleh mengakses jaringan.** Pernah ada
solusi memanggil `fetch("https://api.contoh.com")`; yang sebenarnya diuji jadi
perilaku DNS mesin penilai. Tandai `auto_check: False`.

**Judul materi/kuis/latihan wajib unik dalam satu bahasa — setelah nomornya
dibuang.** Kunci progres berbentuk `"<key>_<tipe>::<judul tanpa nomor>"`.
`progress.judul_kunci()` memangkas awalan `"12. "` dari judul materi, sehingga
MENYISIPKAN materi baru di tengah kurikulum tidak lagi menghapus pencapaian
siapa pun — hal yang dulu terjadi diam-diam, karena menambah satu materi di
posisi kedua menggeser nomor semua materi sesudahnya dan setiap kunci lama
mendadak tidak menunjuk apa pun. Konsekuensinya: dua materi yang cuma dibedakan
NOMORNYA sekarang bertabrakan jadi satu kunci. Dijaga
`test_progress.TestKunciTanpaNomor`.

Judul kuis dan latihan ("Kuis 1: ...", "Latihan 3: ...") tidak berbentuk
angka-titik sehingga tidak tersentuh sama sekali.

Yang DITAMPILKAN tetap judul lengkap dari kurikulum, bukan potongan di kunci —
`navigasi._cari_objek` dan `api._uraikan_kunci` sengaja mengembalikan
`obj["title"]`, karena nomor terbaru cuma diketahui kurikulumnya sendiri.

Berkas catatan pribadi memakai kunci yang sama dan ikut dinormalkan
(`webapp/catatan.py`). Melupakannya berarti catatan tetap ada di berkasnya tapi
tidak pernah ditemukan lagi — dan catatan tidak bisa dikumpulkan ulang.

**`key` bahasa tidak boleh diubah setelah rilis.** Mengubahnya menghapus seluruh
progres pengguna untuk bahasa itu.

**Solusi harus mencetak sesuatu.** Kalau output kosong, kode kosong pun lolos.
Pakai field `verifikasi` untuk menampilkan kondisi akhir (lihat SQL Latihan 2).

**HTML dan CSS dinilai lewat STRUKTURNYA, bukan lewat eksekusi.** Keduanya
tidak menjalankan apa pun dan tidak mencetak apa pun, padahal seluruh mesin
penilaian di sini bekerja dengan membandingkan keluaran. `struktur.py`
menutup celah itu: berkas HTML dibaca jadi pohon elemen, CSS jadi daftar
aturan yang dirapikan, dan pohon itulah yang jadi keluarannya. Konsekuensinya
mengikat:

* **Keluarannya wajib deterministik sampai ke spasinya.** Atribut HTML
  DIURUTKAN alfabetis (urutan penulisannya tidak berarti apa-apa, jadi
  membiarkannya memengaruhi hasil berarti menggagalkan pelajar tanpa sebab),
  sedangkan properti CSS TIDAK diurutkan — di CSS urutan menentukan siapa
  menimpa siapa, dan menyortirnya akan menyembunyikan justru hal yang paling
  perlu dimengerti soal cascade.
* **Soal latihannya menuliskan pohon yang diharapkan apa adanya.** Karena
  dinilai per karakter, latihan tanpa contoh keluaran mustahil dikerjakan.
  `test_struktur.TestLatihanHtmlCss` mengadu janji di soal dengan keluaran
  sungguhan untuk SETIAP latihan — begitu sebuah solusi disunting sedikit,
  janjinya ikut ketahuan berbohong.
* **Tag yang lupa ditutup bukan alasan menyatakan berkasnya gagal.** Browser
  pun tidak melakukannya. Keluhannya lewat stderr, kode keluarnya tetap 0,
  dan pelajar tetap melihat pohonnya — karena justru pohon itu yang
  menunjukkan apa yang sebenarnya terjadi pada markup-nya.
* **Jangan menuntut penutup untuk elemen yang memang tidak punya.** `<br>`,
  `<img>`, `<meta>` tidak ditutup, dan `<li>` di dalam `<ul>` boleh dibiarkan
  terbuka. Menyalahkan pelajar untuk sesuatu yang justru benar adalah cara
  tercepat membuat orang berhenti percaya pada umpan balik.

**HTML dan CSS satu-satunya bahasa yang `butuh`-nya kosong.** Keduanya tidak
memerlukan satu program pun untuk dipasang — cukup aplikasi ini dan sebuah
browser. Itu sebabnya keduanya berdiri paling depan di `LANGUAGES`: buat orang
yang baru mulai dan belum sanggup memasang compiler apa pun, di sinilah pintu
masuk yang paling mungkin dilewati tanpa tersandung lebih dulu.

**Nama berkas Java = nama kelas public.** Dijaga `berkas.py` dan diuji di
`test_berkas.py`.

### Bab dan penguncian

**`bab.py` satu-satunya yang boleh memutuskan sebuah bab terkunci.** Ini kembaran
dari aturan "jangan pernah menulis definisi lulus yang kedua", dan sama mahalnya
kalau dilanggar: begitu ada tempat kedua yang menghitung, terminal dan web akan
berbeda pendapat tentang materi yang sama, dan tidak ada yang tahu mana yang
benar. Antarmuka boleh MEMBACA `status()`, `terkunci()`, `indeks_terbuka()` —
tidak boleh menyimpulkan sendiri dari `materi_dibaca`.

**Yang mengunci hanya bacaan, bukan kuis atau latihan.** Menuntut kuis lulus
terdengar lebih ketat, tapi akibatnya bisa diperkirakan: satu latihan sulit yang
belum ditaklukkan mengunci seluruh sisa kurikulum, dan orang yang mandek di situ
tidak punya apa pun lagi untuk dikerjakan selain hal yang sedang membuatnya
mandek.

**Bab yang terkunci tetap DITAMPILKAN.** Judulnya, tingkatnya, jumlah materinya,
dan alasannya. Menyembunyikannya menghapus satu-satunya alasan bab ini ada —
orang perlu tahu apa yang menanti, bukan cuma apa yang sudah lewat.

**Bab yang pernah disentuh tidak pernah terkunci lagi.** Menutup kembali sesuatu
yang sudah dibuka adalah cara tercepat membuat orang mengira progresnya hilang.
Ini juga yang membuat fitur ini aman dipasang belakangan: orang yang sudah
membaca materi jauh di depan tidak tiba-tiba kehilangan aksesnya.

**Tidak boleh ada tombol yang berujung penolakan.** Kalau sebuah permukaan bisa
mengantar ke materi terkunci, ia wajib menandainya LEBIH DULU: `sesudah` di
`/api/materi` dikosongkan di batas bab, saran menyaring materi terkunci, dan
hasil pencarian (terminal maupun web) membawa penanda "terkunci". Menyuruh orang
mengerjakan sesuatu lalu menolak membukanya adalah cara tercepat membuat sebuah
fitur terasa rusak alih-alih membimbing.

**Kalimat aturannya tinggal di `bab.KALIMAT_ATURAN`, bukan di layar.** Tiga
permukaan menjelaskan aturan yang sama ke pelajar; web menerimanya lewat
`/api/awal` -> `aturan_bab`. Logikanya memang cuma satu, tapi rumusan yang
ditulis ulang di tiap layar bisa melenceng satu per satu tanpa satu tes pun
gagal, dan yang dibaca pelajar jadi dua aturan berbeda tergantung dari pintu
mana ia sampai.

**Pintu daruratnya wajib benar-benar ada.** Saklar `buka_semua_bab` dideklarasikan
sekali di `konfigurasi.SKEMA`; menu Pengaturan terminal membangun dirinya dari
situ, tapi antarmuka WEB tidak — ia menyusun barisnya satu per satu di
`layar-lain.js`. Menambah opsi baru tanpa menambah barisnya di sana menghasilkan
setelan yang ada di API tapi tidak ada di layar, dan dua tautan "buka semua bab
di Pengaturan" yang mendarat di halaman tanpa saklarnya.

**Generatornya ada di riwayat sesi, bukan di repo — tulis ulang kalau perlu.**
Bentuknya sederhana dan sudah terbukti: ubah `BAB` (rentang) jadi spesifikasi
(judul, ket, tingkat, JUMLAH materi), sisipkan jumlahnya di bab yang memuat
titik sisip, lalu hitung ulang seluruh `awal`/`akhir` dari nol dan tulis ulang
berkasnya. Uji kewarasannya satu baris: menghasilkan ulang TANPA perubahan
harus memberi rentang yang identik dengan yang sekarang ada di berkas.

**Menyisipkan materi di tengah berarti MENOMORI ULANG judul sesudahnya.**
Judul membawa nomornya sendiri ("25. ..."), dan dua materi bernomor sama
terlihat salah di layar walau tidak ada tes yang gagal. Penomoran ulang aman
terhadap progres — `progress.judul_kunci()` memangkas awalan "NN. " sebelum
membentuk kunci — tapi judul TANPA nomor tetap wajib unik.

**`data/bab.py` DIHASILKAN dari spesifikasi, bukan diketik.** Rentang indeks yang
diketik tangan adalah kesalahan yang tidak kelihatan: satu angka meleset membuat
seluruh bab sesudahnya bergeser tanpa satu pun tanda di layar. Generatornya
menerima "judul, tingkat, berapa materi" lalu menghitung rentangnya, dan menolak
menulis kalau totalnya tidak sama dengan jumlah materi sungguhan.

**Tes yang menyentuh `bab` harus mengalihkan berkas KONFIGURASI juga.** `bab.py`
membaca `buka_semua_bab`, jadi tes yang cuma mengalihkan progres akan membaca
setelan pribadi orang yang menjalankannya — dan setiap tes penguncian lolos palsu
di mesin siapa pun yang pernah menyalakan saklar itu. Jangan lupa
`konfigurasi.lupakan_cache()`.

### Khusus antarmuka web

**Cangkang laptop = satu bilah instrumen melayang (blok "pil atas" + "observatorium" di gaya.css).**
Aplikasi ini dipakai HANYA di laptop. Cangkang IDE (bilah aktivitas, Explorer,
tab, bilah status) sudah DICABUT atas permintaan pemilik karena "berantakan
dan memusingkan"; jangan dikembalikan. Yang tersisa satu pil di tengah atas
berisi semua tujuan (Dasbor, Pustaka, Karier, Ruang Coba, Bahasa, Lainnya,
cari, XP) dan satu kanvas lapang di bawahnya. Lapisan desain laptop hidup di
blok `@media (min-width: 861px)` di kaki berkas ("pil atas", "bahasa visual",
"beranda"), jadi aturan lebar sempit yang dijaga tes tidak tersentuh. Palet:
langit malam biru-hitam + rentang kuningan (`--nyala`) + verdigris
(`--tumbuh`); antarmuka Jost (`--f-judul`, `--f-ui`), judul besar Bodoni Moda
(`--f-plakat`, didefinisikan di `body`), prosa tetap Atkinson. Kaca buram
(backdrop-filter) sudah dibuang dari bilah dan panelnya: riset 2026-10-18
menandainya sebagai ciri template AI paling mudah dikenali. `--rel-tinggi`
(80 px) tetap arti "apa yang ada di atasku" untuk semua yang menempel.

**Terminal dan web wajib menampilkan ISI yang sama.** Tata letaknya memang
sengaja berbeda; yang tidak boleh adalah ada kalimat yang terbaca di satu
antarmuka lalu hilang di antarmuka lain. `isi.bagian_materi()` pernah ditulis
`if "code" in bagian: ... else: ...`, sehingga bagian yang punya `body` DAN
`code` sekaligus kehilangan seluruh prosanya di browser — sementara terminal
menampilkan keduanya. Tidak ada error di mana pun, dan yang membaca di browser
tidak punya cara tahu ada yang tidak ia lihat. Kebetulan nol dari 190 materi
lama mencampur keduanya, jadi bug itu menunggu materi baru pertama yang
menulisnya. Sekarang keduanya dikeluarkan sebagai dua blok (judul menempel di
blok pertama saja), dan `test_web.TestIsiSamaDenganTerminal` mengadu SELURUH
baris body di SELURUH kurikulum dengan apa yang sampai ke sisi web.

**Jangan pernah menulis definisi "lulus" yang kedua.** Kelulusan latihan
ditentukan `runner.periksa`, kunci jawabannya oleh `exercises.bangun_tests`,
XP dan badge oleh `progress.record_*`. `webapp/api.py` hanya mengubah bentuk
keluarannya. Begitu ada dua definisi, terminal dan web akan berbeda pendapat
tentang latihan yang sama — dan tidak ada yang tahu mana yang benar.

**Server ini menjalankan kode, jadi bind-nya WAJIB loopback.** `server.buat()`
menolak host selain 127.0.0.1 dengan `ValueError`, dan itu bukan kehati-hatian
berlebihan: di 0.0.0.0, setiap mesin di jaringan yang sama bisa menjalankan
kode di komputer ini. Penjagaannya berlapis tiga — token per-jalannya server,
preflight yang selalu gagal untuk asal lain, dan pemeriksaan Host/Origin.
`test_web.TestPenjagaanServer` menembak ketiganya dari sudut penyerang.

**Semua mutasi progres lewat `api._KUNCI_PROGRES`.** `progress` melakukan
baca-ubah-tulis atas satu berkas; server ini melayani beberapa permintaan
sekaligus. Tanpa kunci itu, dua permintaan bersamaan saling menimpa dan XP
yang baru dicatat lenyap.

**Animasi tidak boleh jadi satu-satunya cara sebuah elemen terlihat.** Ini
aturan yang paling gampang dilanggar tanpa sadar dan paling mahal akibatnya:
keadaan AKHIR sebuah animasi harus sama dengan keadaan alami elemennya, dan
animasinya cuma berangkat dari tempat lain. Karena itu `bilah()` menyetel lebar
akhirnya di gaya inline lalu menganimasikan dari `0%`, dan cincin level
menyetel `stroke-dashoffset` akhirnya lebih dulu. Kalau polanya dibalik —
`fill: "forwards"` menuju keadaan yang benar — maka gerak yang dimatikan,
animasi yang dibatalkan saat layar berganti, atau `IntersectionObserver` yang
tidak pernah menyala berarti elemennya hilang selamanya. Yang menyembunyikan
sesuatu lebih dulu (`ungkap()`) wajib punya pengaman waktu yang
mengembalikannya.

**Tiga tingkat gerak, dan yang menentukan bukan cuma saklarnya.**
`data-gerak` bernilai `"penuh"`, `"halus"`, atau `"mati"`, TAPI
`prefers-reduced-motion` di sistem selalu menang — `tingkatGerak()` di
`gerak.js` adalah satu-satunya tempat yang berhak memutuskan itu. Jangan
membaca `data-gerak` langsung dari kode lain. Nilai lama di localStorage berupa
boolean; `bacaGerak()` menerjemahkannya, dan menghapus penerjemah itu berarti
menyalakan kembali animasi untuk orang yang sudah pernah mematikannya.

**Satu properti, satu mesin.** Kalau WAAPI menganimasikan sebuah properti,
`transition` CSS untuk properti yang sama harus dilepas. Keduanya akan saling
mengejar dan menghasilkan gerakan tersendat yang sangat sulit didiagnosis —
itu sebabnya `.bilah > i` tidak lagi punya `transition: width`, dan `.jendela`
tidak lagi punya `animation`.

**`fill: "forwards"` tidak pernah berhenti sendiri, dan itu sumber dua bug
yang sudah pernah terjadi.** Animasi ber-fill `forwards` memaksakan nilai
akhirnya SELAMANYA, bahkan sesudah animasi lain yang lebih baru selesai
mengisi. Akibatnya: begitu animasi penggantinya usai, yang lama menang lagi.

* `tekan()`/`lepas()` di `gerak.js` — tanpa `menekan.batal()` di `lepas()`,
  setiap tombol yang pernah diklik tinggal mengecil 2,5% untuk seterusnya.
  Satu tombol tidak kelihatan; tiga puluh tombol dalam satu sesi kelihatan.
* `jendela()` di `inti.js` — tanpa membatalkan animasi tirai yang sedang
  memudar, dialog yang dibuka tepat sesudah dialog lain ditutup akan berdiri
  di atas tirai ber-opacity 0, alias tak terlihat sama sekali. Pola
  "Batal lalu buka dialog berikutnya" dipakai di Reset progres dan
  Lihat jawaban, jadi ini bukan kasus langka.

Aturannya: siapa pun yang memasang `fill: "forwards"` bertanggung jawab
membatalkannya. Kalau tidak yakin butuh `forwards`, jangan pakai — bawaan
`backwards` sudah benar untuk hampir semua animasi di sini, karena keadaan
akhirnya memang keadaan alami elemennya.

**Pengaman waktu tidak boleh menyembunyikan ulang apa yang sudah terlihat.**
`ungkap()` menyembunyikan anak-anak sebuah wadah lalu memunculkannya saat
tergulir ke layar, dengan pengaman 2,5 detik untuk kasus pengamatnya tidak
pernah menyala. Versi pertamanya menyalakan pengaman itu TANPA SYARAT dan
tanpa mematikan pemicunya — sehingga blok yang sudah telanjur tergambar
dianimasikan masuk dari opacity 0 begitu akhirnya digulir ke sana. Itu
kedipan, tepat di bawah mata orang yang sedang membaca. Bentuk yang benar:
pengamannya bertanya "apakah pengamat ini pernah menyala sama sekali?", dan
kalau pernah, ia tidak berbuat apa-apa. Pola yang sama berlaku di
`nyalakanBara()`.

**Gerak yang bukan `animation` maupun `transition` tidak ikut mati sendiri.**
Dua aturan besar di kaki `gaya.css` hanya menyentuh keduanya. `scroll-behavior:
smooth` dan `window.scrollTo({behavior: "smooth"})` lolos dari sana, jadi
masing-masing harus dimatikan sendiri — lihat `html[data-gerak="mati"]` di CSS
dan `adaGerak() ? "smooth" : "auto"` di JS.

**Nilai dasar sebuah properti tidak boleh hanya ada di dalam `@keyframes`-nya.**
Begitu animasinya dimatikan, properti itu kembali ke nilai BAWAAN CSS, bukan ke
nilai pertama keyframe-nya. Latar `#tungku` yang lama pernah kena: opacity-nya
cuma ditulis di dalam keyframe, jadi mematikan animasi justru membuat latarnya
melompat ke opacity 1 — dua kali lebih terang, tepat pada setelan yang dipilih
orang karena ingin layarnya lebih tenang. Latar itu sekarang sudah dibuang
(lihat "Kertas, bukan kaca" di kepala gaya.css); yang tersisa cuma `.merek-bara`
dan `.cincin::after`, dan keduanya menulis keadaan diamnya di aturan biasa.

**Jarak diambil dari tangga `--s1`..`--s8`, bukan dari angka piksel.**
Ruang kosong adalah bahan bangunan utama desain ini — yang membuat halaman
terasa tenang bukan warnanya melainkan jaraknya. Menulis `padding: 22px`
alih-alih `var(--s5)` bukan sekadar tidak rapi: ia membuat kelapangan seluruh
aplikasi tidak bisa lagi disetel dari satu tempat, dan setelah dua puluh angka
seperti itu, tidak ada lagi ritme yang bisa dikenali mata.

**Item grid dan flex butuh `min-width: 0` supaya halaman tidak meluber.**
Nilai bawaannya `auto`, yang berarti "jangan menyusut di bawah lebar
min-content". Satu kisi bara selebar 26 kolom di dalam kartu pernah membuat
SELURUH halaman jadi 450 px pada layar 414 px — dan yang terlihat pemakainya
bukan "kisinya kebesaran" melainkan "seluruh aplikasinya bisa digeser ke
samping". Aturan pencegahnya ada di gaya.css, bagian "tidak meluber".

**`max-height` BERPERSEN pada sebuah GRID ITEM diukur terhadap GRID AREA item
itu sendiri, bukan terhadap induknya.** Ini sudah pernah merusak hal yang
paling sering dipakai pelajar. `.kerja-hasil` dulu ditulis
`max-height: 46%` dengan maksud "paling banyak 46% ruang kerja". Yang terjadi:
grid memberi baris itu 180 px karena isinya memang 180 px, lalu 46% dihitung
dari 180 dan panelnya dipangkas jadi 83 px. Artinya bukan batas melainkan
perbandingan tetap — **"SELALU sembunyikan 54% isimu"**, berapa pun tinggi
jendelanya, dan makin panjang keluarannya makin banyak yang hilang. Pelajar
yang menekan Jalankan pada halaman HTML pertamanya melihat separuh bawah baris
`<h1>` terjepit di tepi bawah layar, tanpa satu pun error di mana pun.

Yang benar `46cqh`, dengan `.kerja-kode` diberi `container-type: size`.
Dua hal yang gampang salah kalau ini disentuh lagi:

* **Jangan memindahkan batasnya ke `grid-template-rows` sebagai persen.**
  `minmax(0, 46%)` memang mengukur terhadap container — tapi persen di situ
  nilai DEFINIT, jadi tracknya selalu selebar 46% bahkan saat panelnya masih
  kosong. Editor kehilangan 300 px demi kalimat "Keluaran muncul di sini".
  Tracknya wajib tetap `minmax(0, auto)`.
* **`container-type: size` aman DI SINI karena tinggi `.kerja-kode` datang
  dari luar** (grid `.kerja-tata` yang meregangkannya, di dalam
  `#layar.penuh` yang tingginya `calc(100vh - ...)`). Memasangnya pada elemen
  yang tingginya ditentukan isinya sendiri akan mengkolapskannya jadi nol.

Diverifikasi di tiga keadaan yang harus tetap benar bersamaan: panel kosong
(116 px, editor 489 px), keluaran pendek (180 px, utuh), keluaran panjang
(310 px = atapnya, digulir di dalam, tidak meluber) — dan di jendela pendek
700 px editor tetap di atas lantai 180 px-nya.

**Ambang di sini harus DIHITUNG, bukan dikira-kira, dan diukur ke
`#panggung`.** Media query mengukur seluruh viewport, sementara ruang yang
benar-benar tersedia untuk isi jauh lebih sempit — padding `#layar` 76 px tidak
pernah ikut terhitung. Dengan ambang yang salah, akibatnya terbalik dari dugaan
siapa pun: MELEBARKAN jendela justru MENYEMPITKAN kolom baca, karena kolom
ketiga muncul sebelum ada ruang untuknya. Karena itu semua ambang TATA LETAK
memakai `@container panggung`, bukan `@media`; `@media` cuma dipakai untuk hal
yang memang soal perangkatnya (navigasi melipat, jarak tepi layar). Angka yang
dipakai sekarang beserta hitungannya ditulis di komentar `gaya.css` tepat di
atas tiap blok.

**Dua angka ambang hidup di JS dan WAJIB cocok dengan CSS.** `AMBANG_PANEL`
(860) di `aplikasi.js` menentukan apakah tombol menu berbuat sesuatu, dan harus
sama dengan blok `@media (max-width: 860px)`. `AMBANG_RUANG` (1100) di
`editor.js` menentukan apakah editor berhenti mengukur dirinya dari isi, dan
harus sama dengan `@container panggung (min-width: 1100px)`. Kalau salah satu
meleset, ada pita lebar tempat dua mesin berpendapat berbeda soal satu tata
letak — dan gejalanya bukan error melainkan editor pendek yang menggantung di
dalam kotak tinggi, atau tombol menu yang diam saja padahal panelnya satu-
satunya jalan ke menu.

**Blok `@media` diletakkan di PALING BAWAH gaya.css.** CSS menyelesaikan
spesifisitas yang sama dengan urutan: `@media (max-width: 860px) { .x { a } }`
yang ditulis di tengah berkas kalah dari `.x { a }` yang ditulis sesudahnya,
dan yang terjadi bukan error melainkan tata letak ponsel yang diam-diam tidak
berlaku.

Ini bukan kekhawatiran teoretis. Versi sebelum perombakan punya 759 baris
komponen SESUDAH blok media-nya, dan empat aturan layar sempit di situ memang
mati tanpa satu pun tanda: `.lanjutkan{padding}`, `.lanjutkan-isi{min-width}`,
`.kepala-aksi{align-items}`, dan `.fakta{gap}`. Yang terparah `.lanjutkan-isi`,
yang tetap menuntut 260 px di dalam kolom 324 px — kartu tindakan utama jadi
benda TERLEBAR di halaman, persis di layar tersempit. Yang mencegahnya
terulang bukan kehati-hatian melainkan urutannya: `@media` dan `@container`
tinggal di kaki berkas, sesudah seluruh komponen.

**`--ukuran-teks` dipasang di `<html>`, bukan `<body>`.** `rem` selalu diukur
terhadap font-size `<html>`. Memasangnya di body pernah membuat setelan
"Ukuran huruf" di Pengaturan tidak mengubah satu pun teks berukuran rem — dan
di halaman materi itu berarti NOL dari seratusan elemennya ikut membesar.
Setelan yang tampak berfungsi tapi tidak mengubah apa pun lebih buruk
daripada setelan yang tidak ada.

**Judul materi/kuis/latihan sudah membawa nomornya sendiri** ("2. Variabel &
Tipe Data"). Daftar yang punya kolom nomor tersendiri wajib memangkasnya lewat
`tanpaNomor()` — di TAMPILAN saja. Jangan pernah mengubah judulnya di data:
judul itu bagian dari kunci progres.

**`#layar` punya TIGA ukuran, dan layar baru wajib memilih salah satunya.**
Daftarnya di `aplikasi.js`: `LAYAR_LEBAR` (ruang kerja & pembaca materi —
beberapa kolom yang masing-masing sudah membatasi dirinya), `LAYAR_KOLOM`
(bahasa, kuis, bookmark, catatan, cari, statistik, pengaturan — halaman
daftar, dipatok `--kolom-maks` 1400 px), dan bawaan `--panggung-maks` 1240 px
untuk DASBOR, satu-satunya layar yang memang dua kolom.

**Ruang lebar dipakai dengan MENAMBAH KOLOM, bukan dengan meregangkan baris.**
Ini diukur, bukan dikira: pada jendela 1920 px, melebarkan daftar materi dari
960 px ke 1909 px tidak mengubah satu pun yang penting — tinggi halamannya
tetap 2402 px dan yang terlihat tetap TIGA baris. Yang bertambah cuma panjang
ruang kosong antara judul dan penandanya, sampai dua ujung satu baris berhenti
terbaca sebagai satu baris. Yang benar-benar menambah muatan cuma kolom kedua:
`.senarai` memakai `repeat(auto-fill, minmax(min(520px, 100%), 1fr))`, dan
dengan itu 19 latihan Python muat dalam satu layar 1440 px — sebelumnya tiga.

Dua hal yang gampang salah kalau ini disentuh lagi:

* **Lantainya wajib `min(520px, 100%)`, bukan `520px` telanjang.** Track grid
  tidak pernah menyusut di bawah minimum minmax-nya, jadi `minmax(520px, 1fr)`
  di dalam kolom 336 px menghasilkan track 520 px — dan yang terlihat bukan
  "kisinya kebesaran" melainkan seluruh halaman bisa digeser ke samping,
  dengan tujuh belas elemen terdorong keluar layar di ponsel.
* **Halaman yang melebar memaksa isinya punya measure sendiri.** Begitu
  `--kolom-maks` naik jadi 1400 px, `.bab-teks` yang cuma `flex: 1` memelarkan
  KOTAKNYA sampai tepi kanan sementara ISINYA berhenti di 56ch — menyisipkan
  lima ratus piksel kosong antara judul bab dan kemajuannya. Kartu di layar
  mulai kena hal yang sama. Kalau sebuah blok cuma memuat sebaris teks plus
  sebuah tombol, ia wajib dipatok; yang boleh melebar cuma kisi.

**Kelas ukuran dipasang bersama ISI yang baru, bukan di awal `gambarRute()`.**
`pasangUkuran()` dipanggil dua kali — sebelum kerangka pemuatan ditempel, dan
sesudah `kosongkan(panggung)` — tidak pernah di awal. Menyetelnya di awal
berarti layar LAMA yang masih terlihat ditata ulang ke lebar layar berikutnya
lebih dulu, dan yang terlihat bukan pergantian melainkan isi lama yang
melompat melebar tepat sebelum memudar. Paling kentara di perpindahan yang
paling sering dilakukan: halaman bahasa (960 px) ke ruang kerja latihan
(penuh). Kalau rutenya telanjur dibatalkan, `pasangUkuran()` memang TIDAK
pernah dipanggil — itu yang benar, lebar rute yang dibuang tidak boleh
dipasang.

**Butir navigasi aktif ditandai DUA kali: kelasnya dan `aria-current`.**
Tujuh belas dari sembilan belas sasaran navigasi tinggal di dalam panel yang
tertutup — seluruh sebelas bahasa, plus empat tujuan di "Lainnya". Untuk butir
seperti itu `offsetWidth`-nya nol, jadi penanda yang meluncur tidak punya
tempat berdiri; versi sebelumnya memadamkannya, dan akibatnya di halaman
bahasa — tujuan yang paling sering dibuka di aplikasi ini — navigasi tidak
menyalakan apa pun sama sekali. `tandaiRel()` sekarang menandai PEMICU panel
yang memuat butir aktif (`.rel-pemicu.kini` + `aria-current="true"`) dan
meletakkan penandanya di situ. Kelas `.kini` saja tidak pernah cukup: warna
tidak dibacakan pembaca layar, jadi `aria-current="page"` wajib ikut dipasang
DAN dilepas.

**Warna teks diambil dari token TEKS, bukan dari token garis.**
`.bab-nomor` pernah memakai `--garis-kuat` — nilai yang dipilih supaya tepi
satu piksel terbaca, bukan supaya sebuah angka terbaca. Hasilnya 1,65:1 di
tema gelap: bukan cuma gagal AA, tapi membatalkan alasan komponen itu ada,
sebab nomor bab di sini justru disebut "penggaris yang dipakai mata". Token
teks paling tenang yang boleh dipakai `--redup`.

**Pil yang memakai satu warna untuk teks DAN tint latarnya diukur terhadap
latar yang sudah ikut bergeser.** `.pil-tenang` dkk. memasang
`color: var(--X)` bersama `background: color-mix(in srgb, var(--X) 11%,
transparent)`, jadi menaikkan saturasi warnanya menaikkan keduanya sekaligus
dan rasionya nyaris tidak bergerak. Yang menggerakkannya cuma GELAP-TERANG
warna itu sendiri — itu sebabnya `--tenang` tema terang digelapkan, bukan
dipekatkan.

**Judul baris daftar MEMBUNGKUS (dua baris), tidak dipotong elipsis.** Baris
daftar adalah tempat orang MEMILIH mau mengerjakan yang mana, dan judul
satu-satunya pembedanya. Di 360 px kolomnya 203 px sementara judul seperti
"Apa Itu HTML & Halaman Pertamamu" butuh 265 px — elipsis memotong justru
bagian yang membedakannya dari tetangganya, pada seluruh sembilan belas judul
sekaligus. Yang dibayar dengan membungkus satu baris tinggi; yang dibayar
dengan memotong adalah kemampuan memilih.

**Baris perkakas navbar tidak boleh meluber, dan yang TIDAK BOLEH menyusut
adalah `#rel-alih`.** Di 360 px baris itu pernah 369 px di dalam 360 px layar,
dan yang dikorbankan mesin flex justru tombol menunya — satu-satunya jalan ke
sebelas bahasa, Pengaturan, Statistik, Bookmark, dan Catatan — sampai jadi
20 px dengan tepi kanan di luar layar. Ia sekarang `flex: none`, dan yang
dibuang untuk memberi ruang `#tombol-bantuan`: isinya daftar PINTASAN PAPAN
KETIK, dan di perangkat sentuh tidak ada papan ketik. Menambah perkakas baru
di baris itu berarti menghitung ulang 360 px.

**Layar mengembalikan `konteks`, bukan `jejak`.** Remah roti sudah tidak ada.
Penggantinya satu strip tempel (`#konteks`) yang dibangun router dari objek
`konteks` yang dikembalikan tiap layar: `{balik, bab, judul, posisi, persen,
langkah, sebelum, sesudah}`. Layar yang TIDAK punya posisi (dasbor, statistik,
pengaturan, bookmark, catatan, cari, ruang coba) mengembalikannya `undefined`,
dan stripnya tidak dirender sama sekali — 44 piksel itu kembali jadi milik
isinya. Alasannya bukan estetika: remah roti lama berbunyi "Belajar › HTML ›
3. Struktur Dokumen", dan dua dari tiga ruasnya mengulang judul yang sudah
tertulis besar-besar tepat di bawahnya.

Konsekuensi yang mengikat: apa pun yang sudah dibawa strip TIDAK boleh digambar
lagi di badan halaman. Tautan "kembali ke bahasa" dan tombol maju/mundur cuma
ada di strip — itu sebabnya pembaca materi kehilangan `.materi-balik` dan ruang
kerja latihan kehilangan kaki "latihan sebelumnya/berikutnya".

**Jangan pernah memakai `scrollIntoView` untuk menggulir jalur materi.** Ia
menggulir SEMUA leluhur yang bisa digulir, termasuk dokumen — jadi membuka
materi ke-13 lewat navigasi dalam aplikasi mendaratkan pembacanya sembilan
ratus piksel di bawah judul, di tengah kalimat, pada halaman yang belum pernah
ia lihat. Penggantinya `bawaKeTengah()` di `layar-belajar.js`, yang cuma
menyentuh `scrollTop`/`scrollLeft` wadahnya.

Pasangannya `saatSiap()`: layar dibangun UTUH sebelum router menempelkannya,
dan router masih menunggu animasi keluar layar sebelumnya. Jadi apa pun yang
diukur di `requestAnimationFrame` polos bisa mengembalikan nol — dan yang
terjadi bukan error melainkan jalur yang diam-diam berhenti di butir pertama,
cuma di sebagian pemuatan, tergantung frame mana yang menang.

**Dan `saatSiap()` menjawab separuh saja: "elemennya sudah terpasang dan punya
ukuran", BUKAN "ukurannya sudah berhenti berubah".** Hamparan bara mengukurnya:
di 1100 px pemuatan-pertama, `clientWidth` `.bara-petak` menyusut **299 → 262
sesudah** pemasangan, jadi pin yang dihitung pada 299 mendarat di `scrollLeft`
**80** padahal ujung yang benar **117** — dan `saatSiap` sudah berjalan dengan
benar, tepat sekali, pada kotak yang semenit kemudian tidak ada lagi. Apa pun
yang MEMPIN posisi gulir karena itu butuh pengamat ukuran di atas `saatSiap`.

Pengamat itu **wajib lepas**, dan ini bagian yang paling mudah dilupakan:
posisi gulir adalah keadaan PENGGUNA, bukan keadaan komponen. Merebutnya
kembali sesudah dia menggeser sendiri lebih buruk daripada tidak mem-pin sama
sekali. Jadi putus pada isyarat sentuhan pertama (`wheel`/`pointerdown`/
`keydown`) dan pada batas waktu — `pinKeHariIni()` di `layar-belajar.js` adalah
contoh yang berlaku, dengan `PIN_BARA_MS = 4000`. Dua pagarnya di
`test_web.py`: `TestHamparanBara.test_kisi_dibuka_pada_hari_ini` menuntut
bentuknya, dan `test_rAF_polos_tidak_mengukur_tata_letak` menyapu seluruh
`statik/js/layar-*.js` supaya kelas bug ini tidak lahir lagi di tempat lain.

**Bab memakai `<details>/<summary>`, dan `@media print` wajib memaksanya
terbuka.** Melipat adalah cara menghemat ruang LAYAR; di kertas tidak ada yang
bisa diklik untuk membukanya lagi, jadi halaman cetak yang kehilangan separuh
isinya adalah halaman yang salah. Aturannya di kaki gaya.css (`.bab-isi`,
`.bantuan-isi`).

Yang tertutup secara bawaan cuma bab yang BUKAN sedang dikerjakan, dan
kepalanya tidak pernah ikut terlipat: nomor, judul, tingkat, kemajuan, dan
alasan kuncinya semuanya ada di `<summary>`. Aturan "bab yang terkunci tetap
DITAMPILKAN" tetap utuh — yang disembunyikan cuma daftar judul materi yang
memang belum boleh dibuka. Peta bab (`.peta-bab`) menggantikan gulungan lima
ribu piksel sebagai jawaban atas "ada berapa bab dan aku di mana".

**Empat keadaan memakai SATU komponen: `keadaan()` di inti.js.** Kosong,
berhasil, gagal, dan terkunci dulu punya bentuknya sendiri-sendiri — empat
bentuk untuk satu pekerjaan yang sama ("tidak ada apa-apa di sini, dan inilah
sebabnya"), dan tiga di antaranya cuma muncul sekali-sekali, persis frekuensi
yang membuat sebuah bentuk tidak pernah sempat dikenali. Yang membedakan
keempatnya sekarang cuma warna garis kiri dan ikonnya.

**`--baca` dan `--t-baca` diturunkan dari satu angka, `--baca-skala`.** Satuan
`ch` diukur terhadap font-size ELEMENNYA SENDIRI, jadi 72ch di dalam prosa
1,06rem sama dengan 76,32ch di dalam grid 1rem. Kolom tengah pembaca materi
dipatok tepat selebar kolom bacanya (`calc(var(--baca) * var(--baca-skala))`),
dan satu-satunya cara angka itu tidak pernah meleset adalah dengan menurunkan
keduanya dari satu nilai. Versi sebelumnya memberi kolom tengah SELURUH sisa
ruang lalu membatasi prosanya di dalamnya — menyisakan 243 piksel kosong antara
akhir kalimat dan peta di kanan, dan jurang itu melebar makin lebar jendelanya.

**Dasbor punya DUA keadaan, dan yang kedua bukan hiasan.** Profil dengan
`xp === 0` mendapat `layarMulai()`, bukan dasbor biasa yang kebetulan semua
angkanya nol. Dasbor biasa untuk profil baru berbunyi begini: heatmap 182 hari
yang seluruhnya dingin, sebelas kartu bahasa yang semuanya "0% · 0/44 materi",
"streak terputus", dan "0/22 badge" — katalog kegagalan yang bahkan belum
sempat dilakukan, dan tidak satu pun darinya menjawab pertanyaan yang sebenarnya
dibawa orang itu, yaitu "aku mulai dari mana". Pintu pertamanya datang dari
`saran.py`, bukan dari tebakan di JS: antrean "habis ini ngapain" sudah punya
satu tempat tinggal.

Bentuknya sekarang: satu saran yang menonjol, lalu SELURUH bahasa sebagai ubin
yang bisa dibandingkan, lalu Ruang Coba sebagai pintu yang sengaja tenang.
Tiga hal yang mengikat kalau layar itu disentuh lagi:

* **Tidak ada penomoran pada pilihan yang saling menggantikan.** Versi
  sebelumnya menomori tiga pintunya 1-2-3. Nomor di aplikasi ini berarti
  URUTAN — nomor bab, nomor materi, nomor langkah — dan itulah seluruh gunanya
  sebagai arsitektur; memakainya untuk tiga alternatif membuatnya terbaca
  "kerjakan 1, lalu 2, lalu 3".
* **Angkanya dihitung dari `ctx.awal.bahasa`, tidak diketik.** Kalimat
  sambutan yang menyebut "sebelas bahasa" adalah kalimat yang suatu hari
  berbohong tanpa satu pun tes gagal.
* **Aturan babnya datang dari `ctx.awal.aturan_bab`, tidak ditulis ulang.**
  Layar ini dulu memuat rumusannya sendiri — persis hal yang dilarang di
  "Kalimat aturannya tinggal di `bab.KALIMAT_ATURAN`" di atas. Daftar
  tingkat (Dasar/Menengah/Mahir beserta keterangannya) juga datang dari sana.

Baris ketiga tiap ubin menjawab satu pertanyaan yang memang jadi sumbu
keputusan pemula — berapa banyak yang harus dipasang sebelum kodenya bisa
dijalankan — dan ketiga tingkatnya dihitung dari jawaban server, bukan
ditebak: `!siap` → "butuh go"; `siap && !pasang` → "tanpa pasang apa pun"
(cuma HTML & CSS); sisanya "siap dijalankan". Yang belum siap TETAP
ditampilkan dan tetap bisa dibuka — materi dan kuisnya jalan penuh — dan
ditandai sebelum diklik, bukan sesudah.

**Satu layar, satu tindakan utama.** Kartu `.lanjutkan` adalah satu-satunya
permukaan yang memakai warna aksen sebagai LATAR, bukan sekadar garis atau
teks. Menambah yang kedua di layar yang sama tidak membuat dua hal penting —
ia membuat nol. Teks di atas permukaan beraksen memakai token
`--di-atas-aksen`, bukan nilai gelap yang ditulis ulang per komponen: di tema
terang aksennya sendiri sudah gelap, dan menuliskannya manual sudah pernah
menghasilkan huruf gelap di atas hijau gelap — 2,5:1, praktis tak terbaca.

**Tingkat "halus" harus tetap menjawab sentuhan.** Umpan balik tekan adalah
satu-satunya alasan tingkat tengah itu ada; kalau ia ikut padam, "halus" tidak
ada bedanya dengan "mati". Yang padam di tingkat itu hanya yang bergerak
SENDIRI. `.pusaran` sengaja dikecualikan — ia penunjuk status, dan pusaran yang
berhenti berputar berarti "aplikasinya macet", bukan "gerak dikurangi".

**`sorot.js` wajib menghasilkan token yang identik dengan `sorot.py`.** Ada dua
implementasi pemindai, dan daftar kata kuncinya HANYA ada di Python — JS
menerimanya lewat `/api/awal`. `test_web.TestPenyorotJavaScript` mengadu
keduanya atas seluruh kode kurikulum plus kode yang sengaja rusak. Kalau Node
tidak terpasang, tesnya skipped, bukan lulus diam-diam.

**Index jawaban kuis wajib dipetakan ulang setelah opsi diacak.** Ini bug klasik
yang membuat jawaban benar ditandai salah. `sesi._acak_soal` menghitung posisi
barunya sekali saat sesi dibuat, dan `test_web` mengerjakan SELURUH 57 kuis
dengan jawaban benar lalu menuntut skor sempurna.

**Catatan pribadi tinggal di berkasnya sendiri**
(`~/.belajar_ngoding_catatan.json`). Alasannya: `progress.reset()` ada dan orang
memakainya. Kalau catatan menumpang di berkas progres, "kosongkan nilai Java"
diam-diam ikut membakar tulisan tangan penggunanya. Progres bisa dikumpulkan
lagi; catatan tidak.

**Tes web WAJIB mengarahkan keempat lokasi berkas ke direktori sementara** —
progres, konfigurasi, catatan, DAN `exercises.DIR_KERJA`. Yang terakhir paling
gampang terlupa, dan melupakannya berarti tes menimpa jawaban asli pengguna di
`~/belajar-ngoding/kerjaanku`. Lihat `test_web.BasisWeb`. Jangan lupa
`konfigurasi.lupakan_cache()`: modul itu menyimpan isinya di memori.

**Yang berlaku untuk tes berlaku juga untuk MENCOBA APLIKASINYA.** Menjalankan
`belajar-web.py` lalu mengeklik-klik untuk memeriksa sesuatu menulis ke berkas
progres yang SAMA dengan yang dipakai pemiliknya — satu latihan yang
"cuma dicoba" berarti XP, badge, dan streak yang tidak pernah ia kerjakan,
plus sebuah berkas jawaban di `~/belajar-ngoding/kerjaanku` berisi kode yang
bukan tulisannya. Progres di sini catatan belajar sungguhan, bukan data uji.
Untuk memeriksa apa pun, nyalakan dengan profil terpisah:

```bash
S=$(mktemp -d)
BELAJAR_PROGRESS_FILE=$S/p.json BELAJAR_CONFIG_FILE=$S/k.json \
BELAJAR_CATATAN_FILE=$S/c.json BELAJAR_WORKSPACE=$S/kerja \
  python3 belajar-web.py --tanpa-browser --port 7788
```

**Jangan panggil `replaceChildren` di luar `inti.js`; pakai `isikan()`.**
Seluruh sisi web memakai pola `syarat ? h(...) : null`, dan `h()` menyaring
`null` lewat `tambah()`. `replaceChildren` bawaan DOM TIDAK: ia mengubah `null`
jadi simpul teks, dan kata "null" muncul di halaman tanpa satu pun error di
konsol. Sudah terjadi di layar kuis (dua kali) dan bookmark, dan bertahan
sekian lama justru karena tidak ada yang rusak — cuma sebuah kata asing di
tempat yang tidak seorang pun curigai. `isikan()` lewat `tambah()` yang sama.
Dijaga `test_web.TestBerkasStatik`.

**Komponen yang menyetel `display` sendiri wajib mengembalikan `[hidden]`.**
`display` di sebuah kelas mengalahkan aturan `[hidden]` bawaan browser, jadi
`el.hidden = true` pada sebuah `.tbl` tidak menyembunyikan apa pun. Akibatnya
kebalikan dari maksud penulisnya, dan diam. Lihat baris `.tbl[hidden]` di
gaya.css.

**`webapp/statik/js/package.json` bukan proyek npm dan tidak boleh dihapus.**
Isinya cuma `{"type": "module"}`. Tanpa itu Node membaca `*.js` di sana sebagai
CommonJS, dan dua tes yang menjalankan kode ini langsung — `TestMesinGerak` dan
`TestPenyorotJavaScript` — GAGAL dengan "Cannot use import statement outside a
module" alih-alih skip. Tes yang merah karena alasan yang tidak ada hubungannya
dengan isinya adalah tes yang berhenti dibaca, dan yang ikut tenggelam adalah
kegagalan berikutnya yang sungguhan.

**Apa yang DILIHAT pelajar tidak selalu sama dengan apa yang DINILAI.**
HTML dan CSS dinilai lewat pohon strukturnya (`struktur.py`) karena keduanya
tidak mencetak apa pun, dan itu keputusan yang benar untuk penilaian. Tapi
orang yang baru menulis `<h1>Halo, Dunia!</h1>` lalu menekan Jalankan ingin
melihat tulisan Halo Dunia — bukan daftar menjorok berisi nama tag yang baru
saja ia ketik sendiri. Yang dibutuhkan untuk menampilkannya sudah ada di
ruangan: browsernya sendiri.

Karena itu kartu keluaran punya dua tab, Tampilan lebih dulu dan Struktur di
sebelahnya. Pohonnya WAJIB tetap ada — ia yang dinilai, dan ia juga satu-
satunya cara melihat apa yang browser TEBAK dari markup yang tag penutupnya
lupa ditulis. Aturannya di `statik/js/pratinjau.js`:

* **Bingkainya `sandbox="allow-scripts"` TANPA `allow-same-origin`.** Itu
  aturan yang diajarkan kurikulum ini sendiri di materi HTML 13: memberi
  keduanya sekaligus untuk berkas se-asal membuat sandbox-nya sia-sia.
* **Tidak boleh `loading="lazy"`.** Kartu keluaran hampir selalu lahir di bawah
  lipatan layar, jadi bingkai bermuat-malas menerima dokumen KOSONG lebih
  dulu, mengukurnya, dan melapor 8px.
* **Tidak boleh `transition: height`.** Tingginya digerakkan JS dari hasil
  pengukuran di dalam — menambah transisi berarti dua mesin menggerakkan satu
  properti (lihat "Satu properti, satu mesin"), dan di sini umpan baliknya
  nyata: selama transisi, bingkai sementara lebih pendek daripada isinya,
  pengukur di dalam melihatnya meluber, lalu meminta tumbuh lagi.
* **Tingginya diukur dari tepi bawah anak-anak body**, bukan `scrollHeight`
  documentElement (melingkar: `<html>` mengisi bingkainya) dan bukan kotak
  body (margin atas `<h1>` kolaps keluar, jadi kurang).
* **CSS murni dikenakan pada halaman yang DIBUATKAN dari pemilihnya sendiri,
  dan halaman itu wajib mengaku dibuatkan.** Tanpa kalimat pengakuannya, yang
  terlihat pelajar adalah markup yang tidak pernah ia tulis dan tidak akan
  pernah ia temukan lagi di mana pun. Blok CSS yang sudah memuat markup
  (11 dari 40) dipratinjau apa adanya.

**Soal latihan lewat pengurai yang SAMA dengan badan materi.** Dulu ia dikirim
sebagai satu blok teks dan digambar dengan `white-space: pre-line`, yang
meruntuhkan deretan spasi — padahal hampir semua soal memuat contoh keluaran
berkolom, dan perataan kolom itulah yang menerangkan apa yang harus dicetak.
Dua hal yang gampang terlupa kalau ini disentuh lagi: `api.latihan` mengirim
`soal_blok`, dan `blokProsa()` di `layar-belajar.js` adalah SATU-SATUNYA
perender blok prosa — menyalinnya ke layar lain berarti suatu hari keduanya
berbeda tanpa ada yang menyadarinya.

**Komentar-doc menempel pada fungsinya; komentar untuk satu penyeleksi dapat
aturannya sendiri.** Dua bentuk yang sama-sama sah bagi parser dan sama-sama
melukai pembacanya yang berikutnya: (i) menyisipkan fungsi baru DI ANTARA sebuah
blok `/** ... */` dan fungsi yang blok itu dokumentasikan — komentar tersebut
berhenti menjelaskan apa pun dan mulai menjelaskan tetangganya; (ii) menaruh
komentar di antara koma dan penyeleksi berikutnya dalam satu daftar —
`{ display: none; }` tidak lagi terlihat menempel pada penyeleksi yang mana, dan
daftar pemulih `[hidden]` justru dibaca orang dengan cara itu. Yang mengikat:
selipan baru mendarat **setelah** blok `docstring + function` yang lengkap, atau
pindahkan seluruh blok itu bersamamu. Pagarnya `TestBentukKomentar`, dan ia
sengaja sempit: perluasan "setiap `/**` wajib diikuti sebuah deklarasi" diukur
memberi tiga positif-palsu nyata (`ingat()` metode objek di `aplikasi.js`,
`lepas()` metode kelas di `editor.js`, dan sebuah blok `/* */` yang memang
menyusul sebuah docstring), sementara predikat daftar-penyeleksi tidak boleh
disapu ke JavaScript sama sekali — di sana tidak ada prelude, dan sapuannya
menghasilkan dua puluh delapan kasus yang semuanya sah. Yang menjaga KELASNYA
adalah paragraf ini, yang dibaca manusia, bukan tes itu.

### Pustaka dan Peta Karier

**Pustaka (`inti/pustaka.py`) membaca `data/pustaka/*.json`, dan berkas itu
DIHASILKAN `alat/panen_pustaka.py`.** Jangan menyunting JSON-nya dengan
tangan: `test_pustaka.TestDataHasilPemanen` memanen ulang dari
`/home/vi/folder_materi/materi-belajar` dan menuntut hasilnya identik.
LISENSI menentukan apa yang boleh diambil, dan tabelnya di kepala pemanen:
repo tanpa lisensi (getting-a-gig, build-your-own-x) dan repo proprietary
(developer-roadmap) cuma boleh DITAUTKAN, isi kurikulum freeCodeCamp berhak
cipta walau kodenya BSD, dan daftar coding-interview-university (CC BY-SA)
tinggal di berkasnya sendiri yang ikut berlisensi CC BY-SA. Pemetaan topik
ke kurikulum dihitung saat dimuat (`TOPIK_KURIKULUM`), jadi kurikulum baru
cukup menambah satu baris di sana, tanpa memanen ulang.

**Peta Karier: data di `data/karier.py`, aturan di `pelajar/karier.py`.**
Kesiapan sebuah profesi adalah rata-rata kelompok bekalnya, dan persen tiap
kurikulum diambil dari `progress.statistik_bahasa` -- angka "x% selesai" yang
sama dengan halaman bahasa, bukan definisi kedua. `gaji` HANYA diisi dari
halaman publik yang memang untuk peran itu (tanggal diperiksa wajib ada);
angka dari halaman "pendekatan" sengaja dibuang. Terminal (`layar/karier.py`,
`layar/pustaka.py`) dan web memanggil fungsi inti yang sama.

### Proyek akhir

Tiap bahasa ditutup satu latihan bertanda `proyek: True`. Ia latihan biasa di
mata seluruh mesin — dinilai `runner.periksa` yang sama, XP dari `progress`
yang sama — karena definisi "lulus" cuma boleh ada satu. Yang ditambahkan cuma
penandanya, dan penanda itu mengalir lewat `isi.daftar_latihan` ->
`api.latihan` -> dua permukaan di web.

**Bentuknya wajib berbeda-beda, dan itu bukan soal selera.** Sebelas proyek
yang semuanya "kumpulkan data lalu cetak laporan" menguji satu keterampilan
sebelas kali, dan pelajar yang lulus sebelas-belasnya masih belum pernah
menulis simulasi, parser, atau program berkonkurensi. Yang ada sekarang:

| Bahasa | Bentuk |
|---|---|
| Python | agregasi & laporan (class, exception, dict) |
| Java | simulasi bertahap (state machine, Deque, enum) |
| JavaScript | pengurai teks (regex, Map, reduce) |
| C | algoritma & pointer (BFS, malloc/free, telusur balik) |
| C++ | parser rekursif (pohon sintaks, unique_ptr, exception) |
| SQL | analitik (JOIN, CTE, window function, anti-join) |
| Bash | pipeline berkas (mktemp, trap, find, case) |
| HTML | halaman utuh (struktur semantik, aksesibilitas) |
| CSS | sistem tata letak (token, flex, grid, media query) |
| Go | konkurensi (goroutine, channel, WaitGroup) |
| Bikin Aplikasi | lapisan aplikasi (domain/repo/service/antarmuka) |
| Git & GitHub | simulasi tim (bare remote, dua clone, PR, konflik, tag) |

Semuanya dinilai otomatis dan lolos `test_solutions`. Konsekuensi yang
mengikat: solusinya harus DETERMINISTIK, dan untuk Go itu berarti hasil dari
goroutine WAJIB diurut sebelum dicetak — urutan kedatangannya memang tidak
pasti, dan itu sifat konkurensi, bukan bug yang bisa diperbaiki.

### Membaca badan materi (`isi.blok_badan`)

Di sumbernya `body` cuma daftar baris polos, dan penulis memakai indentasi
untuk dua hal yang sangat berbeda: **menyejajarkan kolom** (tabel, contoh kode)
dan **menandai "ini penjelasan di bawah kalimat tadi"**. Pengurainya dulu
memeriksa indentasi LEBIH DULU daripada penanda daftar, jadi keduanya berakhir
sama: blok monospace abu-abu. 664 daftar dan 181 paragraf biasa tampil persis
seperti contoh kode — dan yang hilang bukan keindahan melainkan sinyal, karena
satu-satunya pembeda "ini perlu kamu ketik" dari "ini perlu kamu paham" adalah
bentuknya.

Aturan yang sekarang mengikat:

* **Penanda diperiksa sebelum indentasi, dan harus diikuti TEPAT SATU spasi.**
  Angkanya bukan selera: dari 449 blok berpenanda, 446 memakai satu spasi, dan
  ketiga sisanya justru BUKAN daftar melainkan tabel yang kolom pertamanya
  kebetulan sebuah bintang (`  *  perkalian        a * b`).
* **Baris menjorok tanpa penanda di tengah daftar adalah LANJUTAN butirnya,
  bukan butir baru.** Pemenggalan baris di sumber cuma jejak lebar berkasnya;
  memperlakukannya sebagai butir memecah satu kalimat jadi beberapa bulatan di
  tempat yang tidak ada hubungannya dengan artinya.
* **Kecuali kalau ia menjorok lebih dalam daripada kolom teks butirnya, atau
  kolomnya disejajarkan spasi ganda.** Itu contoh milik butir itu, dan
  perataannya ADALAH isinya. Urutan prosa/contoh di dalam satu butir
  dipertahankan apa adanya, karena prosa penutup sering menunjuk contoh di
  atasnya ("Hanya mengenai satu elemen itu").
* **Paragraf disambung jadi satu baris, bukan dipertahankan patahannya.**
  Baris di sumber dibungkus untuk terminal 80 kolom (median 68 huruf, p90 81)
  sedangkan kolom baca di layar 72ch — jadi sebagian patah terlalu cepat dan
  sisanya terbungkus ulang. Kecualinya 7 blok yang kolomnya sejajar.
* **Kata yang terpenggal di ujung baris disambung tanpa spasi.** Ke-18
  kasusnya kata ulang ("diam-diam", "benar-benar"), jadi tanda hubungnya bagian
  dari katanya dan yang salah cuma spasinya.
* **Ragu berarti TETAP kode.** Sisi salahnya sengaja dipilih: menyangka prosa
  sebagai kode cuma mempertahankan keadaan lama, sedangkan menyangka kode
  sebagai prosa MENGHAPUS perataan yang jadi isinya. Karena itu `_prosa_menjorok`
  menuntut minimal dua baris, ditutup tanda titik, tanpa ciri kode, dan padat
  kata biasa — dari 420 calon cuma 181 yang lolos.

Semuanya dijaga `test_web.TestPenyajianIsi`, dan
`test_web.TestIsiSamaDenganTerminal` tetap mengadu SELURUH baris body di
SELURUH kurikulum supaya tidak ada kalimat yang hilang saat dirapikan.

Tiga aturan yang ditambahkan saat prosa ditulis ulang (2026-10-16), masing-
masing dengan pagarnya sendiri di kaki `test_web.py`:

* **Daftar bernomor membawa nomor awalnya (`"mulai"`).** Butir bernomor yang
  dipotong contoh kode atau baris kosong pecah jadi beberapa blok; tanpa
  nomor awal, tiap potongan digambar sebagai `<ol>` baru dan web menampilkan
  1, 1, 1 padahal sumber dan terminal menulis 1, 2, 3. 179 potongan di
  seluruh kurikulum kena. `senarai()` meneruskannya ke `<ol start>`.
  (`TestDaftarBernomorBersambung`)
* **Butir YAML di dalam contoh adalah contoh, bukan daftar.** `- uses: ...`
  yang menempel di bawah kunci YAML polos (`steps:`) ikut blok kodenya.
  Syaratnya sengaja sempit (kunci berhuruf kecil tanpa spasi), karena
  puluhan materi menulis daftar prosa "- Istilah: penjelasan" di bawah label
  menjorok. (`TestButirYamlDiContoh`)
* **`` `kode` `` di prosa digambar sebagai `<code>`, tanpa backtick-nya.**
  Kurikulum C#, Kotlin, PHP, Ruby, Rust, TypeScript, dan VB ditulis dengan
  backtick sejak awal, dan web dulu menampilkannya mentah. Terminal tetap
  menampilkan backtick sebagai penanda; isinya sama.

**Blok kode di halaman materi bisa dijalankan dan disunting DI TEMPAT.**
Tombolnya dulu melempar ke Ruang Coba — layar lain, alamat lain, dan kembali
berarti kehilangan posisi baca. Untuk pertanyaan sekecil "keluarnya apa kalau
ini dijalankan?", ongkos itu jauh lebih besar daripada pertanyaannya, dan yang
terjadi bukan orang membayarnya melainkan orang berhenti bertanya. Dua syarat
tombolnya, dan KEDUANYA jawaban server, bukan tebakan: `bisa_dijalankan` dari
`berkas.py` dan `siap` dari `runner.py` — tombol yang selalu berakhir dengan
"belum terpasang" adalah tombol yang berujung penolakan. Yang dipanggil
`/api/coba`, yang memang tidak menyentuh progres sama sekali: definisi "lulus"
tetap cuma satu dan tempatnya `runner.periksa`. Editor sisipannya WAJIB dilepas
di `saatKeluar` — kalau tidak, pendengar papan ketik dan pengamat ukurannya
hidup terus di belakang layar berikutnya.

## Ronde pengembangan 2026-10-17 (audit 12 agen)

Dua belas agen mengaudit aplikasi dari sudut berbeda (pemula, persona pindah
karier, visual, aksesibilitas, pedagogi, ilmu belajar, arsitektur, keamanan,
performa, visualisasi data, terminal, umpan balik). Yang dibangun dan sekarang
mengikat:

* **Data pelajar tidak pernah ditimpa diam-diam.** Progres, konfigurasi, dan
  catatan dibaca/ditulis lewat `pelajar/simpanan.py`. Berkas yang tidak bisa
  diurai dipindah ke `<nama>.rusak-<waktu>` sebelum data bawaan dipakai (dulu
  satu koma salah menghapus seluruh progres), tiap penyimpanan meninggalkan
  satu `.bak`, dan gagal menulis muncul di layar (`simpan_gagal`,
  `/api/awal -> karantina`). Jangan menulis kode tulis-atomik keempat.
* **Kuis "selesai" = skor terbaik >= 70%** (`progress.AMBANG_KUIS_LULUS`,
  keputusan pemilik). Satu-satunya definisinya `statistik_bahasa`/`kuis_lulus`;
  ia juga melapor `kuis_dikerjakan`. Jadwal ulang monoton dan hanya tumbuh
  kalau kuisnya memang jatuh tempo; XP ulangan dini cuma untuk peningkatan.
* **Isi kuis dijaga `tests/test_mutu_soal.py`** (ukur dengan
  `python3 alat/periksa_kuis.py`): jawaban benar = opsi terpanjang <= 40%
  per kurikulum, kapital penekanan tidak menandai jawaban, petunjuk pertama
  tidak memuat baris solusi, minimal dua petunjuk (tangga konsep -> strategi
  -> kode). JANGAN mengubah urutan/jumlah soal atau indeks `answer` saat
  menyunting opsi: `salah_kuis` menyimpan NOMOR soal. Sesudah opsi ditulis
  ulang, periksa bahwa opsi di indeks `answer` masih jawaban yang benar; dua
  kunci pernah tergeser diam-diam karena itu.
* **Kuis ditawarkan begitu materi yang diujinya terbaca.** Peta per SOAL ke
  materi (judul tanpa nomor) ada di `data/kuis_materi.py`, ditinjau soal demi
  soal; `test_kuis_materi` menjaga tiap kuis punya entri per soal dan tiap
  judul ada. Kesiapan itu PENANDA, bukan kunci: penguncian tetap hanya
  bacaan (bab.py). Soal yang salah menautkan "Baca lagi: <materi>"; materi di
  bab terkunci ditandai, tidak dijadikan tautan.
* **Soal latihan yang dinilai persis wajib menulis keluarannya.** Blok
  `Keluaran yang diharapkan:` / `Untuk input X, keluarannya:` diturunkan dari
  menjalankan solusi dan dijaga `test_janji_keluaran_di_soal_sesuai_kenyataan`.
  Pengurai web menganggap baris sesudah kepala keluaran (prosa, tidak menjorok)
  sampai baris kosong sebagai satu contoh apa adanya. Go/C#/Rust/PHP belum
  diberi blok ini karena toolchain-nya tidak terpasang di mesin ini.
* **Kerangka editor HTML/CSS memakai komentar bahasanya** (`<!-- -->`, `/* */`),
  dijaga `TestKerangkaTidakMenggagalkan` (kerangka + solusi harus lulus).
* **Runner membunuh grup proses sesudah tiap eksekusi**, bukan cuma saat
  timeout (`_bunuh_sisa`). `RLIMIT_NPROC` belum dipasang: perlu diukur per
  toolchain (JVM/.NET membuat banyak thread) sebelum dipatok.
* **Dasbor = meja kerja** (pengganti beranda landing page): posisi, satu
  kartu Lanjutkan beraksen, antrean, dan persen bahasa di atas lipatan.
  Kalimat gulir, marquee, dan ajakan penutup sengaja dibuang; aturan CSS-nya
  jadi catatan (alamat baris tes). Saran: kalau kegiatan terakhir membaca,
  bacaan itu dulu; kuis jatuh tempo paling banyak dua; tantangan harian hanya
  dari bahasa yang disentuh, toolchain siap, tingkat +1.
* **Tebak keluarannya** (`/api/tebak`): kode wajib PERSIS salah satu contoh
  layak di materi (bukan kode bebas), pagar SESI Fedora/Git ikut dari
  berkas.py, kuncinya keluaran nyata. Bukan latihan: tidak menyentuh
  `latihan_lulus`. XP cuma untuk tebakan benar pertama per blok.
* **CSP** dipasang di halaman, tapi `script-src` masih `'unsafe-inline'`:
  iframe `srcdoc` pratinjau mewarisi CSP induk. Mode nonce ada di balik
  `CSP_KETAT` di server.py dan baru aman setelah pratinjau dilayani dari
  rutenya sendiri.
* **Rujukan `berkas:NNN` di tests/test_web.py tetap pajak.** Tiap baris yang
  disisipkan di api.py, progress.py, atau layar-*.js menggeser rujukan.
  Suntingan di berkas yang dipatok dibuat net-zero baris atau di kaki berkas;
  rujukan yang bergeser dipetakan ulang dari isi barisnya di HEAD.

## Observatorium (2026-10-18)

Pemilik menilai desain "masih kosong, tidak ada jiwanya" dan minta rasa "out
of this world": efek kursor, visualisasi di materi, ornamen yang tidak
terlihat buatan AI, dan interkoneksi antar desain. Arahnya: aplikasi ini
sebuah OBSERVATORIUM. Yang dibangun dan sekarang mengikat:

* **Satu bahasa bentuk.** Braket sudut = "ini sasaranmu" (reticle kursor,
  bintang berikutnya di peta, sudut lembar gambar dan kartu Lanjutkan).
  Magnitudo = "seberapa jauh" (terang bintang mengikuti status materi, rumus
  ukuran d3-celestial). Kuningan = sedang dikerjakan, verdigris = sudah jadi.
  Jangan menambah ornamen yang tidak mengodekan sesuatu yang benar.
* **Gerak tetap lewat `tingkatGerak()`.** Langit: kelip dan paralaks hanya
  "penuh" (paralaks = gerak akibat interaksi, WCAG 2.3.3), dan berhenti di
  layar baca/kerja. Kursor: "mati" = tidak ada, "halus" = melompat tanpa
  pegas dan jejak, "penuh" = pegas + jejak meteor. Kursor ASLI tidak pernah
  disembunyikan. Animasi garis-tergambar (`.v-hidup`, `.rasi-hidup`) cuma
  berangkat dari kosong; keadaan alaminya tergambar utuh.
* **Gambar konsep = DATA.** `data/visual/<key>.py` berisi spesifikasi (13
  jenis: variabel, larik, alur, tumpukan, pohon, tabel, urutan, kotak, tata,
  git, memori, bit, kurva); skema, pemeriksa, dan penggambar terminalnya di
  `inti/visual.py`, penggambar SVG-nya di `statik/js/visual.js`. Keduanya
  menampilkan judul, label, dan keterangan yang sama (aturan "isi sama di
  dua antarmuka"). Gambar menempel pada blok TERAKHIR bagiannya (`blok.visual`),
  tidak pernah jadi blok sendiri: peta bagian dan tautan Ruang Coba menunjuk
  blok lewat indeks. Periksa dengan `python3 alat/periksa_visual.py <key>`;
  dijaga `tests/test_visual.py`. Nilai di gambar wajib sama dengan contoh kode
  di dekatnya, dan penyederhanaan disebut di `ket`.
* **Bagian "Di dunia nyata" selalu TERAKHIR** di tiap materi (indeks bagian
  lama tidak bergeser). Ditulis lewat `alat/tambah_bagian.py`, yang menolak
  baris > 78, dash, kepala Keluaran, dan bagian tanpa label `Kasus kecil:` /
  `Cara memecahkannya:`. Sketsa kodenya sudah dijalankan agen dengan
  toolchain masing-masing; klaim yang tidak bisa diuji ditulis berhati-hati.
* **"Lihat jalannya"** (`inti/jejak.py`, `/api/jejak`): pelacak Python lewat
  `sys.settrace` di balik pagar runner yang sama; hasil ditulis ke BERKAS di
  direktori sementara (stdout runner dipotong 20.000 karakter). Program
  dihentikan di 400 langkah, bukan dilanjutkan tanpa dicatat. Bukan penilai.
* **Peta rasi tidak memutuskan apa pun.** Status dan "terkunci" datang dari
  `bab.status` -> `isi.daftar_materi` (`/api/bahasa`, `/api/langit`); garis
  profesi dari `data/karier.py`. Layar Langit menautkan ke Peta Karier, tidak
  menghitung kesiapan kedua.
* **Pemilih yang menunjuk `<html>` dilarang di lapisan baru** (pagar POPULASI
  menghitungnya, termasuk di dalam `@media`). Token baru dipasang di `body`.

## Kurikulum tech stack (2026-10-19)

Pemilik minta materi "semua tech stack yang ada sekarang tanpa terkecuali".
Hasilnya 12 kurikulum ranah: `techstack` (Tech Stack & Arsitektur),
`frontend`, `backend`, `database`, `mobile` (Mobile & Desktop), `game`
(Game & Grafis), `iot` (Embedded & IoT, runner C), `devops` (DevOps &
Cloud), `keamanan` (Keamanan Siber, sudut pandang bertahan), `data` (Data &
Analitik), `ai` (AI & Machine Learning), dan `bahasalain` (bahasa yang belum
punya kurikulum sendiri). Cakupannya diturunkan dari inventaris riset
(Survei Stack Overflow 2024-2026, State of JS/CSS/HTML, roadmap.sh,
JetBrains): tiap teknologi di inventaris dipetakan ke satu judul materi,
yang dominan dapat materi sendiri, pemain kecil masuk materi "peta". Yang
mengikat:

* **Satu registry: `data/kurikulum_tech.py`.** Kurikulum ranah TIDAK
  didaftarkan di `data/__init__.py` atau ditulis tangan di `main.py`.
  Registry memuat `data/<key>_materials/_quizzes/_exercises.py` dan
  `data/visual/<key>.py` kalau ada, lalu memperluas `LANGUAGES`, `BAB`,
  `KUIS_MATERI`, dan peta Pustaka (`topik`/`peta` per entri, hanya untuk
  kurikulum yang datanya lengkap, karena tes Pustaka menolak peta yang
  menunjuk kurikulum tak terdaftar). Kurikulum yang datanya belum lengkap
  tidak terdaftar sama sekali, bukan tampil setengah jadi.
* **`<KEY>_BAB` adalah spesifikasi JUMLAH, bukan rentang.** Rentangnya
  dihitung registry; jumlah yang tidak cocok dengan banyaknya materi atau
  tingkat yang turun = `ValueError`, persis aturan generator `data/bab.py`.
  `<KEY>_KUIS_MATERI` tinggal di berkas kuisnya sendiri.
* **Isinya dirakit `alat/rakit_kurikulum.py`** dari draf per bab
  (`bab_NN.py` berisi BAB/MATERI/KUIS/LATIHAN tanpa nomor). Alat itu
  memberi nomor, menjalankan ulang tes kurikulum lain atas draf
  (`test_data`, `test_mutu_soal`, `test_solutions` dengan LANGUAGES
  diganti), menjalankan tiap contoh PROGRAM, dan menolak menulis kalau satu
  pemeriksaan gagal. Sesudah dirakit, berkas data disunting seperti
  kurikulum lain (`ganti_badan.py`, `tambah_bagian.py`); drafnya tidak ikut
  di repo.
* **Medan `"bahasa"` per bagian materi.** Kurikulum ranah memuat contoh
  dalam banyak bahasa. Tanpa medan itu, blok berbahasa runner kurikulum.
  `"terminal"` = SESI selamanya (docker, kubectl, terraform, npm: pagar
  yang sama dengan Fedora/Git, tanpa pengecualian shebang). `"teks"` =
  ILUSTRASI. Nilai di `berkas.BAHASA_LUAR` (YAML, Dockerfile, JSX, Swift,
  dialek SQL selain SQLite, ...) tidak pernah dijalankan dan diberi petunjuk
  "dibaca di sini, dicoba di proyekmu". `"browser"` untuk JS yang memakai
  `document`. Web (`isi.bahasa_blok`), terminal (`layar/materials.py`),
  `tebak.py`, dan `test_solutions` semuanya membaca medan ini.
* **Program utuh yang mengimpor paket pihak ketiga = POTONGAN**
  (`berkas.paket_luar`, `butuh_paket`): Python, JS/TS, Java/Kotlin, Rust,
  Go, C#, C/C++. Aplikasi wajib offline dan tidak memasang paket, jadi
  tombol Jalankan untuk contoh Flask/React/Spring/Bevy akan selalu gagal.
  Petunjuk "Butuh paket X" hanya untuk blok yang memang utuh, modul lokal
  (`# file hitung.py` di blok yang sama, `package` milik sendiri, `mod`
  Rust) tidak dihitung.
* **Penanda daftar bernomor paling banyak dua digit** (`isi._POLA_NOMOR`).
  Baris prosa yang terbungkus tepat sebelum "2026." atau "18000." dulu
  tampil sebagai `<ol start="2026">`; tujuh materi lama ikut kena.
* **Peta Karier**: kurikulum ranah masuk `pelengkap`, bukan `bekal`.
  Menambah bekal menurunkan persen kesiapan pelajar yang sudah tercatat.

## Gaya bahasa materi

Pemilik menilai materi lama "masih AI banget" dan membingungkan, sampai
bilang lebih baik belajar di situs berbayar. Seluruh prosa materi ditulis
ulang (2026-10-15/16) dengan nada NGOBROL yang ia pilih sendiri dari tiga
contoh. Yang mengikat untuk tulisan baru:

* **Aturannya di `alat/panduan_gaya.md`**, contoh acuannya materi HTML 1-4.
  "nggak" konsisten di prosa; istilah dijelaskan saat pertama muncul;
  tanpa em dash, HURUF KAPITAL untuk penekanan, "bukan X melainkan Y",
  pepatah, atau drama. Label `Jebakan:`/`Ingat:` di awal paragraf boleh
  (aplikasi menggambarnya sebagai kotak), paling banyak dua-tiga per materi.
* **Ukur dengan `python3 alat/periksa_gaya.py [key] [awal judul]`.** Alat
  itu memakai `isi.blok_badan`, jadi contoh kode dan tabel tidak ikut
  terhitung. Garis dasar sebelum penulisan ulang: 12.821 temuan dalam 218
  ribu kata (58,7/1000); sesudahnya sekitar 1/1000, dan sisanya salah
  tangkap (konstanta enum, kata kunci SQL). Singkatan baru yang memang
  kapital didaftarkan di `AKRONIM`, jangan dibiarkan jadi angka palsu.
* **Tulis lewat `python3 alat/ganti_badan.py naskah.txt --tulis`.** Ia cuma
  mengganti field `body`, dan menolak menulis kalau baris > 78 karakter,
  ada dash di prosa, blok `Keluaran:` berubah, atau judul/kode/bagian lain
  ikut berubah. Heading dan kode boleh dibetulkan, tapi dengan tangan dan
  dengan alasan: judul tidak pernah, karena ia kunci progres.
* **Menulis ulang juga berarti memeriksa fakta.** Putaran ini menemukan
  puluhan klaim yang salah di prosa lama (int(-3.99) bukan "dibulatkan ke
  bawah", PriorityQueue bukan antrean FIFO, contoh `[InlineData(10, "E")]`
  yang gagal kalau dijalankan, `nice -n -5 sudo` yang diam-diam tidak
  menaikkan prioritas). Kalau bahasanya terpasang, uji dulu.

## Menambah bahasa

1. Buat `data/<key>_materials.py`, `_quizzes.py`, `_exercises.py`.
2. Ekspor di `data/__init__.py`. Kuis WAJIB dibungkus `seimbangkan_kuis()`.
3. Tambah satu entri di `LANGUAGES` (`main.py`).
3b. Tambah pembagian babnya di `data/bab.py`. Tanpa itu bahasa baru tampil
   sebagai satu bab raksasa berisi semuanya — jalur cadangan yang sengaja ada
   supaya tidak ada materi yang hilang, tapi bukan yang diinginkan.
4. Kalau kodenya perlu dijalankan, tambah `Toolchain` di `runner.TOOLCHAINS`.
5. Kalau perlu penyorotan, tambah aturan di `sorot.py`. Kalau aturannya sama
   dengan bahasa lain, SALIN objeknya (`copy.copy`), jangan menunjuk objek yang
   sama. `bahasa_didukung()` membuang duplikat berdasarkan `id()` -- begitulah
   ia menyaring alias seperti `sh` dan `shell` -- jadi bahasa yang menunjuk
   objek milik bahasa lain lenyap dari daftar yang dikirim ke editor web lewat
   `/api/awal`, dan kodenya tampil polos tanpa satu pun pesan galat.

`test_data.py` otomatis ikut memvalidasi konten baru.

### Field latihan

```python
{
    "title": "Latihan 1: ...",       # unik dalam satu bahasa
    "difficulty": "Mudah",           # Mudah | Menengah | Lanjut | Sulit
                                     # DAFTARNYA di TINGKAT_VALID (tests/test_data.py).
                                     # "Sedang" TIDAK sah -- dokumen ini dulu menyebutnya,
                                     # dan delapan latihan Fedora ditulis salah karenanya.
    "question": ["baris soal", ...],
    "hints": ["hint 1", ...],
    "solution": "...",               # program lengkap, deterministik
    "stdin": "80\n",                 # opsional
    "stdin_list": ["1\n", "2\n"],    # opsional, beberapa kasus uji
    "mode": "persis",                # persis|abaikan_kapital|mengandung|regex|angka
    "setup": "...",                  # ditempel SEBELUM kode pelajar
    "verifikasi": "...",             # ditempel SESUDAH kode pelajar
    "auto_check": False,             # matikan penilaian otomatis
    "alasan_tidak_dicek": "...",     # wajib kalau auto_check False
}
```

## Keputusan yang mudah disalahpahami

**Posisi jawaban kuis dinormalisasi saat data dimuat** (`data/normalisasi.py`).
Konten aslinya sangat bias — pada C++ 55 dari 56 jawaban ada di opsi kedua.
Opsi DIPUTAR (bukan diacak) supaya urutannya tetap terbaca wajar. Jangan hapus
langkah ini; jangan pula menulis ulang 452 soal di source.

**SQL dijalankan dengan SQLite, bukan MySQL.** Materinya mengajarkan MySQL.
Latihan yang memakai `AUTO_INCREMENT`, `DELIMITER`, `TRIGGER`, atau
`START TRANSACTION` ditandai `auto_check: False`. Latihan lain memakai `setup`
karena tiap eksekusi memakai database kosong.

**7 latihan tidak dinilai otomatis** (Java 2, SQL 3, Python 1, JS 1). Ini
disengaja: butuh JUnit, JDBC, pytest, fitur khas MySQL, atau jaringan.
`test_solutions` menjaga rasionya tetap di bawah 10%.

**Materi dihitung selesai hanya kalau dibaca sampai habis.** Berhenti di tengah
ditandai `[~]` tanpa XP.

**`runner` bukan sandbox keamanan.** Ada batas CPU, memori, ukuran berkas, dan
panjang output supaya loop tak berujung tidak menggantung sistem, tapi kode
berjalan dengan hak akses user yang sama.

## Lingkungan mesin ini

Fedora 44 Workstation. Terpasang bawaan: `python3` `node` `javac/java` `gcc`
`g++` `sqlite3` `bash` `ruby` `git`.

Per 2026-10-18 ketujuh toolchain di bawah SUDAH terpasang di mesin pemilik
(Kotlin lewat SDKMAN di `~/.sdkman/candidates/kotlin/current/bin`, tidak ada di
PATH shell non-interaktif; tambahkan sendiri). PHP distro Fedora butuh
`php-mbstring php-pdo` untuk Latihan 14-15 dan materi PDO; runner memuat
modulnya eksplisit karena PHP dijalankan dengan `-n`.

**Tujuh toolchain TIDAK ada bawaan**, dan tanpa semuanya `test_solutions`
melewati 111 dari 303 latihan sambil tetap melaporkan OK — jadi "tesnya hijau"
bisa berarti "tesnya tidak dijalankan":

| Butuh | Untuk |
|---|---|
| `go` | Go |
| `dotnet` | C# dan Visual Basic |
| `rustc` | Rust |
| `php` | PHP |
| `kotlinc` + `kotlin` | Kotlin |
| `tsc` | TypeScript |

Pasang sementara ke satu direktori BERSIH, lalu satukan PATH-nya di satu
berkas yang bisa di-source ulang. Ekstrak ke atas instalasi lain akan
mencampur berkas antar versi dan menghasilkan error kompilasi yang menyesatkan
di dalam standard library.

```bash
# contoh: Go
curl -sL -o /tmp/tc/go.tgz "https://go.dev/dl/$(curl -s https://go.dev/VERSION?m=text | head -1).linux-amd64.tar.gz"
tar -xzf /tmp/tc/go.tgz -C /tmp/tc          # menghasilkan /tmp/tc/go/bin
```

```bash
# /tmp/tc/env.sh -- sumberkan sebelum menjalankan suite lengkap
export DOTNET_ROOT=/tmp/tc/dotnet
export PATH="/tmp/tc/go/bin:/tmp/tc/dotnet:/tmp/tc/rustup/toolchains/stable-x86_64-unknown-linux-gnu/bin:/tmp/tc/kotlinc/bin:/tmp/tc/ts/node_modules/.bin:/tmp/tc/php:$PATH"
export DOTNET_CLI_TELEMETRY_OPTOUT=1 DOTNET_NOLOGO=1
export GOCACHE=/tmp/tc/gocache GOPATH=/tmp/tc/gopath
```

Dengan ketujuhnya terpasang, `python3 -m unittest discover -s tests` menjalankan
1055 tes tanpa satu pun skip dan makan **sekitar 23 menit** -- hampir semuanya
kompilasi .NET dan Kotlin. Jalankan di latar belakang, jangan ditunggu.

Catatan .NET: `DOTNET_EnableWriteXorExecute=0` sudah dipasang di
`runner.TOOLCHAINS`. Tanpa itu .NET 7+ membuat pemetaan ganda W^X yang
menabrak RLIMIT_FSIZE 16 MB milik runner, dan yang terlihat adalah proses
dibunuh tanpa pesan yang menyebut memori sama sekali.

## Lokasi data pengguna

| Apa | Di mana | Override |
|---|---|---|
| Progres | `~/.belajar_ngoding_progress.json` | `BELAJAR_PROGRESS_FILE` |
| Konfigurasi | `~/.belajar_ngoding_config.json` | `BELAJAR_CONFIG_FILE` |
| Catatan pribadi | `~/.belajar_ngoding_catatan.json` | `BELAJAR_CATATAN_FILE` |
| Kode jawaban | `~/belajar-ngoding/kerjaanku/` | `BELAJAR_WORKSPACE` |

Preferensi TAMPILAN web (tema, ukuran huruf, saklar gerak, lebar kolom baca)
tinggal di `localStorage` browser, bukan di berkas mana pun — "tema yang enak
di terminal" dan "tema yang enak di browser" tidak harus sama.

Tes WAJIB mengarahkan `progress.PROGRESS_FILE` ke direktori sementara. Lihat
`tests/test_progress.py` kelas `BasisProgres`.
