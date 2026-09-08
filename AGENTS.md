# Catatan untuk agen

Aplikasi belajar pemrograman berbahasa Indonesia dengan **dua antarmuka** —
terminal dan web — di atas satu inti yang sama. **Tanpa dependensi eksternal**:
Python 3.8+ dan stdlib saja, plus JavaScript vanilla tanpa langkah build.
Jangan tambahkan paket pihak ketiga; seluruh arsitektur mengandalkan ini
(runner, penyorot sintaks, diff, tema, server HTTP, editor kode — semuanya
ditulis tangan).

Semua nama fungsi, variabel, komentar, docstring, dan teks antarmuka memakai
**Bahasa Indonesia**. Ikuti gaya yang sudah ada.

Status: 11 bahasa, 334 materi dalam 81 bab bertingkat, 67 kuis / 532 soal,
159 latihan (152 dinilai otomatis), 678 tes.

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
BELAJAR_SKIP_LAMBAT=1 python3 -m unittest discover -s tests -t .  # ~20 detik
BELAJAR_BAHASA=go python3 -m unittest tests.test_solutions        # satu bahasa
```

Tes lambat mengompilasi ratusan program latihan. Jalankan versi penuh sebelum
commit apa pun yang menyentuh `data/`, `runner.py`, atau `exercises.py`.

## Peta modul

| Modul | Tanggung jawab |
|---|---|
| `main.py` | Registry `LANGUAGES` + menu utama & dashboard |
| `utils.py` | Primitif tampilan: paginasi, menu, input, pembungkus baris |
| `tema.py` | Warna diminta lewat PERAN (`"galat"`, `"kode_kunci"`), bukan ANSI mentah |
| `sorot.py` | Penyorot sintaks 10 bahasa, pemindai token satu lintasan |
| `berkas.py` | Menentukan sebuah blok kode itu berkas, potongan, sesi, multi, atau ilustrasi |
| `runner.py` | Eksekusi kode berbatas waktu/memori + pencocokan output |
| `struktur.py` | Membaca HTML & CSS jadi pohon — itu "keluaran" kedua bahasa itu |
| `bab.py` | Bab mana yang terbuka. SATU-SATUNYA yang memutuskan penguncian |
| `data/bab.py` | Pembagian materi jadi bab bertingkat. DIHASILKAN, bukan diketik |
| `galat.py` | Menerjemahkan pesan compiler ke bahasa manusia |
| `beda.py` | Menjelaskan kenapa output pelajar berbeda |
| `progress.py` | Progres, XP, level, streak, badge, penjadwalan ulang |
| `konfigurasi.py` | Preferensi tampilan, sengaja TERPISAH dari progres |
| `saran.py` | Antrean "habis ini ngapain" |
| `materials.py` `quiz.py` `exercises.py` `navigasi.py` | Layar-layar terminal |

`materials.py` sekarang DUA TINGKAT: daftar bab dulu, baru materi di dalamnya.
Penjagaan penguncian duduk di `render_material`, bukan di menunya, karena itulah
satu-satunya pintu masuk materi di terminal — menu bab, pencarian lokal,
pencarian global, bookmark, "lanjutkan yang terakhir", dan antrean saran semuanya
berakhir di fungsi itu.

`utils.C` menyimpan ANSI mentah dan masih dipakai di beberapa tempat lama.
Untuk kode baru pakai `tema.cat(teks, "peran")`.

### Antarmuka web

Lapisan penyajian di atas modul yang sama. Ia tidak memiliki satu pun aturan
belajar sendiri — semuanya dipinjam.

| Modul | Tanggung jawab |
|---|---|
| `belajar-web.py` | Peluncur: nyalakan server, buka browser |
| `webapp/server.py` | HTTP, tabel rute, dan TIGA lapis penjagaan |
| `webapp/api.py` | Endpoint JSON; membungkus hasil modul inti |
| `webapp/isi.py` | Konten kurikulum → struktur JSON (blok, token, petunjuk) |
| `webapp/sesi.py` | Sesi kuis di memori (pengacakan + pemetaan ulang jawaban) |
| `webapp/catatan.py` | Catatan pribadi, berkas TERPISAH dari progres |
| `statik/js/gerak.js` | Mesin animasi: solver pegas, urutan, pemicu, isyarat |
| `statik/js/sorot.js` | Port `sorot.py` ke JS untuk penyorotan langsung di editor |
| `statik/js/editor.js` | Editor kode: textarea transparan di atas `<pre>` bertoken |
| `statik/js/layar-*.js` | Layar-layar web |
| `statik/js/ikon.js` | 24 ikon garis SVG, satu keluarga, mewarisi currentColor |
| `statik/gaya.css` | Satu lembar gaya; 4 tema; aturan gerak & arah desain di dalamnya |

## Invarian yang gampang dilanggar

Semuanya dijaga tes. Kalau salah satu gagal, itu bukan tes yang cerewet —
itu bug yang akan menyakiti pelajar.

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
nilai pertama keyframe-nya. `#tungku` pernah kena: opacity-nya cuma ditulis di
dalam `bara-kiri`/`bara-kanan`, jadi mematikan animasi justru membuat latarnya
melompat ke opacity 1 — dua kali lebih terang, tepat pada setelan yang dipilih
orang karena ingin layarnya lebih tenang.

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

**Ambang `@media` di sini harus DIHITUNG, bukan dikira-kira.** Media query
mengukur seluruh viewport, sementara ruang yang benar-benar tersedia untuk isi
jauh lebih sempit: panel kiri 270 px dan padding `#layar` 76 px tidak pernah
ikut terhitung. Dengan ambang yang salah, akibatnya terbalik dari dugaan siapa
pun — MELEBARKAN jendela justru MENYEMPITKAN kolom baca, karena kolom ketiga
muncul sebelum ada ruang untuknya. Angka yang dipakai sekarang beserta
hitungannya ditulis di komentar `gaya.css` tepat di atas tiap `@media`.

**Blok `@media` diletakkan di PALING BAWAH gaya.css.** CSS menyelesaikan
spesifisitas yang sama dengan urutan: `@media (max-width: 820px) { .x { a } }`
yang ditulis di tengah berkas kalah dari `.x { a }` yang ditulis sesudahnya,
dan yang terjadi bukan error melainkan tata letak ponsel yang diam-diam tidak
berlaku.

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

**Satu layar, satu tindakan utama.** Kartu `.lanjutkan` adalah satu-satunya
permukaan yang memakai amber sebagai LATAR, bukan sekadar garis atau teks.
Menambah yang kedua di layar yang sama tidak membuat dua hal penting — ia
membuat nol.

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

## Menambah bahasa

1. Buat `data/<key>_materials.py`, `_quizzes.py`, `_exercises.py`.
2. Ekspor di `data/__init__.py`. Kuis WAJIB dibungkus `seimbangkan_kuis()`.
3. Tambah satu entri di `LANGUAGES` (`main.py`).
3b. Tambah pembagian babnya di `data/bab.py`. Tanpa itu bahasa baru tampil
   sebagai satu bab raksasa berisi semuanya — jalur cadangan yang sengaja ada
   supaya tidak ada materi yang hilang, tapi bukan yang diinginkan.
4. Kalau kodenya perlu dijalankan, tambah `Toolchain` di `runner.TOOLCHAINS`.
5. Kalau perlu penyorotan, tambah aturan di `sorot.py`.

`test_data.py` otomatis ikut memvalidasi konten baru.

### Field latihan

```python
{
    "title": "Latihan 1: ...",       # unik dalam satu bahasa
    "difficulty": "Mudah",           # Mudah | Sedang | Menengah | Sulit
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

Terpasang: `python3` `node` `javac/java` `gcc` `g++` `sqlite3` `bash`.
**Belum ada: `go`.** Latihan Go tetap ada tapi tidak terverifikasi kecuali Go
dipasang. Kalau perlu memverifikasi konten Go, pasang sementara:

```bash
curl -sL -o /tmp/go.tar.gz https://go.dev/dl/go1.23.4.linux-amd64.tar.gz
mkdir -p /tmp/goroot && tar -xzf /tmp/go.tar.gz -C /tmp/goroot --strip-components=1
PATH=/tmp/goroot/bin:$PATH GOCACHE=/tmp/gocache python3 -m unittest tests.test_solutions
```

Ekstrak ke direktori BERSIH. Mengekstrak ke atas instalasi Go lain akan
mencampur berkas antar versi dan menghasilkan error kompilasi yang menyesatkan
di dalam standard library.

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
