# Catatan untuk agen

Nama proyeknya **`belajar-codingV2`** (2026-10-20, dari `VERSI = "2.0"` di
`inti/kurikulum.py`; paket npm akarnya `belajar-codingv2`, huruf kecil karena
npm menuntutnya). Nama lamanya "Belajar Ngoding", dan masih ada di EMPAT
tempat yang **sengaja tidak diganti**: `~/.belajar_ngoding_progress.json`
(`pelajar/progress.py`), `~/.belajar_ngoding_config.json`
(`pelajar/konfigurasi.py`), `~/.belajar_ngoding_catatan.json`
(`webapp/catatan.py`), dan `~/belajar-ngoding/kerjaanku/` (`inti/latihan.py`).
Keempatnya jalur data pemilik. Mengganti nama di situ tidak menimbulkan satu
pun error — aplikasinya cuma membuka berkas baru yang kosong, dan yang terlihat
adalah progres, catatan pribadi, serta SELURUH kode jawaban yang pernah ia
tulis hilang. Kalau suatu hari memang mau diganti, jalurnya pemindahan yang
disengaja lewat `pelajar/simpanan.py`: baca nama baru dulu, jatuh ke nama lama
kalau belum ada, salin sekali, sisakan cadangannya.

Aplikasi belajar pemrograman berbahasa Indonesia berbasis **web**.
Antarmuka terminal DIBUANG 2026-10-20 (lihat "Jalan ke MERN"): pemiliknya
tidak pernah memakainya, dan `webapp/api.py` terpaksa menarik 3.376 baris
TUI hanya untuk meminjam registry serta logika latihan. **Tanpa dependensi
yang perlu dipasang**: Python 3.8+ dan stdlib saja di sisi server, plus JavaScript tanpa
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
soal, 558 latihan termasuk 32 proyek akhir, 1165 tes. Dua puluh kurikulum
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
python3 belajar-web.py   # membuka browser sendiri

python3 -m unittest discover -s tests -t .                        # semua (~55 menit)
BELAJAR_SKIP_LAMBAT=1 python3 -m unittest discover -s tests -t .  # ~50 detik
python3 alat/ekspor_konten.py --tulis    # perbarui packages/konten/ sesudah data/ berubah
BELAJAR_BAHASA=go python3 -m unittest tests.test_solutions        # satu bahasa

npm install          # perkakas + dependensi @belajar/catatan (express, mongodb).
                     # Aplikasi utamanya tidak butuh satu pun dari ini
npm run tipe         # tsc --noEmit atas ketiga paket TypeScript
npm run catatan      # layanan pencarian catatan (butuh container MongoDB)
npm run golden       # adu port TypeScript (sorot, beda) dengan rekaman Python
npm run gigi --workspace @belajar/bersama   # baterai mutasi: pagarnya bisa merah?
python3 alat/uji_gigi_blok.py            # baterai mutasi pagar layar Langit (jalankan di salinan pohon)
python3 alat/golden_bersama.py --tulis   # perbarui rekaman sesudah sorot/galat/beda berubah
python3 alat/ekspor_bersama.py --tulis   # perbarui tabel kata kunci untuk sisi TS
python3 alat/golden_pembuka.py --tulis   # perbarui rekaman paragraf pembuka panel Langit
```

Ketiga alat ekspor di atas WAJIB dijalankan ulang setiap kali sumbernya berubah,
dan lupa melakukannya bukan kelalaian yang diam: `test_konten_json` mengadu
JSON dengan sumber Python setiap suite jalan, jadi menyunting `data/` tanpa
mengekspor ulang langsung memerah.

Tes lambat mengompilasi ratusan program latihan. Jalankan versi penuh sebelum
commit apa pun yang menyentuh `data/`, `inti/runner.py`, atau
`inti/latihan.py`.

## Peta modul

Tiga paket, dibagi menurut arah ketergantungan yang SUDAH ada di kode — bukan
menurut selera. Tidak ada satu paket pun yang mengimpor paket di atasnya, dan
itulah satu-satunya alasan pembagian ini berarti: begitu ada yang membaliknya,
namanya berhenti memberi tahu apa pun.

| Modul | Tanggung jawab |
|---|---|
| `inti/kurikulum.py` | Registry `LANGUAGES`, versi, statistik per bahasa, laporan kemajuan. SATU-SATUNYA sumber daftar kurikulum |
| `inti/latihan.py` | Logika latihan: nama berkas kerja, kerangka editor, kunci jawaban (`bangun_tests`) |
| `inti/materi.py` | `teks_polos`: isi materi sebagai teks biasa, dipakai pencarian |
| **`inti/`** | **Mesin. Tidak tahu ada antarmuka terminal atau web** |
| `inti/runner.py` | Eksekusi kode berbatas waktu/memori + pencocokan output |
| `inti/struktur.py` | Membaca HTML & CSS jadi pohon — itu "keluaran" kedua bahasa itu |
| `inti/sorot.py` | Penyorot sintaks: 19 set aturan + 16 alias, pemindai token satu lintasan |
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
| `data/bab.py` | Pembagian materi jadi bab bertingkat. DIHASILKAN, bukan diketik |

**`inti/struktur.py` wajib tetap bersebelahan dengan `inti/runner.py`.** Runner
memanggilnya sebagai subprocess lewat
`os.path.join(os.path.dirname(os.path.abspath(__file__)), "struktur.py")`.
Memisahkan keduanya tidak menimbulkan error impor di mana pun — yang terjadi
cuma SELURUH latihan HTML dan CSS berhenti bisa dinilai, dan pesannya berupa
"berkas tidak ditemukan" dari subprocess yang tidak ada yang membacanya.

**Utang "layar/exercises belum sepenuhnya layar" SUDAH DIBAYAR** (2026-10-20).
Dulu `webapp/api.py` mengimpor `bangun_tests`, `DIR_KERJA`, dan `_kerangka`
dari lapisan terminal, dan `main.py` memegang registry sekaligus menu. Isinya
sekarang tinggal di `inti/latihan.py` dan `inti/kurikulum.py`, dan lapisan
terminalnya sendiri sudah tidak ada. Yang mengikat sekarang kebalikannya:
**`webapp/` tidak boleh mengimpor apa pun yang mencetak ke layar**, dan
aturan itu gratis dijaga karena tidak ada lagi lapisan semacam itu.

### Antarmuka web

Lapisan penyajian di atas modul yang sama. Ia tidak memiliki satu pun aturan
belajar sendiri — semuanya dipinjam.

| Modul | Tanggung jawab |
|---|---|
| `belajar-web.py` | Peluncur: nyalakan server, buka browser. Satu-satunya titik masuk |
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

### Paket TypeScript (`packages/`)

Workspace npm. Tidak ada langkah build untuk `bersama` dan `catatan`: Node
menjalankan `.ts` langsung. `web` dibundel Vite.

| Modul | Tanggung jawab |
|---|---|
| `packages/catatan/` | Layanan pencarian catatan (Express + MongoDB). TAMBAHAN; aplikasinya jalan penuh tanpanya |
| `packages/konten/` | Seluruh kurikulum sebagai JSON + `tipe.ts`. DIHASILKAN `alat/ekspor_konten.py` |
| `packages/bersama/src/sorot.ts` | Pemindai sintaks, port `inti/sorot.py`. NOL rujukan ke `document` |
| `packages/bersama/src/beda.ts` | Penjelas beda keluaran, port `inti/beda.py` + `difflib.SequenceMatcher` |
| `packages/bersama/data/aturan-sorot.json` | Tabel kata kunci + alias + pemetaan. DIHASILKAN `alat/ekspor_bersama.py` |
| `packages/bersama/golden/` | Sidik keluaran `sorot`/`galat`/`beda` dari Python. DIHASILKAN `alat/golden_bersama.py` |
| `packages/bersama/uji/` | Pembanding golden + penguji giginya |

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
repositori sendiri di `mktemp -d`, dan kerangka editornya (`inti/latihan.py`)
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
angka dari halaman "pendekatan" sengaja dibuang.

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

## Layar Langit: ikhtisar bertinta + lensa (2026-10-27)

Pemilik menilai peta Langit "terlalu kecil" lalu "masih bland". Layar itu
sekarang dua tampilan atas data yang SAMA (`/api/langit`): ikhtisar 32 rasi
(dibaca dari jauh) dan lensa satu rasi (diperbesar sampai tiap bintang bisa
ditunjuk). Yang mengikat:

* **Klik di peta TIDAK PERNAH menavigasi.** Membuka layar materi menulis
  progres (materi baru ditandai "sebagian" dan menggerakkan kartu Lanjutkan),
  dan 66 persen klik tepat di pusat bintang pada peta lama mengenai
  TETANGGANYA. Hanya tautan "Mulai/Lanjutkan membaca/Baca lagi" di panel yang
  membuka materi. Terukur di aplikasi penuh: memilih bintang menulis nol
  permintaan, membuka materi menulis satu.
* **Bentuk status**: percik (selesai), cakram setengah (sebagian), cincin
  (baru), belah ketupat (terkunci), braket (berikutnya). Semuanya `<path>`
  berkoordinat MUTLAK: `<g transform>` memarkir simpul di titik asal begitu
  `transform` CSS dipasang (cacat Peta Karier, 1f49b99). Satu pengecualian
  yang disadari: cincin terpilih lensa (`.lt-ln-terpilih`) adalah `<g>` yang
  digeser lewat `transform` CSS, dan itu aman karena ia tidak punya atribut
  `transform`, tidak ikut `BISA_DITEKAN`, dan transisinya mati di gerak
  "mati" serta `prefers-reduced-motion`. Baru dan terkunci
  juga berbeda terang-gelapnya (`--lg-baru` = `--teks`, terkunci abu
  menengah, selisih luminans >= 1,8): pasangan terpenting bagi profil kosong
  (111 bintang terbuka lawan 951 terkunci) tidak boleh hanya terbedakan oleh
  bentuk.
* **Cahaya rasi mengodekan KELUARGA**, bukan hiasan, dan mengikuti tema. Ia satu
  elemen berlatar banyak gradien di belakang svg: lingkaran bergradien DI DALAM
  svg digambar ulang tiap hover. Kanvas lensa memakai warna dan alfa yang sama
  (`data-kel` pada kanvas, `--lt-cahaya`), jadi lensa terbaca sebagai rasi yang
  sama diperbesar dan bukan diagram graf yang datar. Rona keluarga tidak
  sepenuhnya jauh dari rona status (OKLCH, empat tema): dari kuningan (72-81)
  hanya Perkakas yang dekat (36-46 derajat), dari verdigris (153-173) paling
  dekat Skrip (48-64), dan dari biru-baja `--tenang` (228-249, warna cincin
  konsep) Sistem cuma 6-22 derajat, Skrip 12-28, Tech 22-40. Pembedanya
  bentuk (cincin konsep melingkari glif, bukan menggantikannya), bukan rona.
  Tech stack dulu abu-abu (kroma 0,046 lawan 0,12-0,15 keluarga lain) dan
  menutup sepertiga bawah peta terang; sekarang 0,085-0,095 dengan rona 270 dan
  terang-gelap yang sama, jadi gerbang kontras tidak bergeser. Inti hijau
  kemajuan dibatasi (`--lt-maju`): pada 42 persen ia membuat bintang selesai
  2,6:1 dan melenyapkan rona keluarga.
* **Tema terang memakai pelat langit malam** (blok "pelat langit" di kaki
  gaya.css, keputusan ronde perbaikan 2026-10-27): di tema terang cuma 3,1
  persen piksel di dalam bingkai peta yang berwarna dan bintang terbaca
  sebagai manik abu-abu, jadi peta dan kanvas lensa menjadi jendela indigo
  dengan tepi kuningan di halaman terang. Panel lensa, legenda, dan kepala tetap
  terang; tema gelap, malam, dan kontras tidak tersentuh (ikhtisar 0 piksel
  berbeda dengan dan tanpa blok itu). Palet gelap dipasang ulang di dua elemen
  itu, satu-satunya tempat token `--lg-`/`--lt-` boleh berdiri di luar
  `body` (pengecualiannya sempit dan dijaga: kepala aturan persis dua pemilih
  itu, dan tidak ada pemilih bertema lain di blok kecuali `[data-tema=...]
  body`). Tokennya dibaca tes kontras sebagai "tema" kelima, termasuk titik
  gradasi yang paling terang. Menghapus blok itu mengembalikan kertas terang.
* **Saringan MENAMBAH penanda, tidak mengurangi.** Konsep = cincin pada
  bintang yang cocok; profesi = garis bawah kuningan pada nama rasi bekal
  (sama dengan warna jalur putus); keduanya juga masuk NAMA AKSESIBEL
  (`labelRasi`: ", N materi cocok dengan X", ", bagian bekal Y"; dulu 0 dari 32
  nama berubah). Peredupan `opacity` pada teks atau glif DILARANG: nomor bintang
  jatuh ke 1,6:1, cincin fokus 1,0-1,9:1, nama rasi 2,1-2,9:1 (empat tema),
  padahal semuanya masih bisa dipakai. Satu-satunya yang diredupkan adalah
  CAHAYA rasi di luar bekal (dekoratif). Dijaga `test_tidak_ada_peredupan_opacity`.
* **Kontras dijaga dari TOKEN** oleh `TestBlokLangit` (alias status dibaca
  dari CSS, bukan disalin): terkunci dan garis nominal >= 5:1, glif status
  >= 4,5:1, dan >= 3,2:1 di pusat cahaya yang paling terang; teks >= 12 px di
  semua lebar. Pagar piksel sungguhan tetap pengukuran di peramban.
* **Fokus papan ketik tidak boleh jatuh ke BODY.** Panel dikunci per RASI, bukan
  per bintang (kunci per bintang membongkar tombol yang sedang berfokus), dan
  tombol yang memang mengganti jenis panel (Tutup, Berikutnya, baris bab)
  mengembalikan fokus ke bintangnya. Fokus BODY keadaan yang sah (alamat yang
  baru dimuat, klik ruang kosong), jadi Esc didengar di tingkat DOKUMEN, tidak
  di `<section>`. Berlapis: kartu judul, lalu pilihan, lalu lensa; Esc yang
  melepas pilihan juga menutup kartu fokus yang muncul lagi di bintangnya,
  jadi sesudah Enter cukup dua tekan. Dialog global dan menu "Lainnya"
  cangkang yang terbuka memenangkan Esc (pendengar dokumen jalan lebih dulu
  daripada pendengar jendela milik menu). Tombol yang
  dipegang bersama Alt, Ctrl, atau Meta bukan milik daftar bintang (Alt+Panah =
  Mundur/Maju peramban). Opsi terkunci TIDAK `aria-disabled`: ia bisa dipilih
  (membaca alasannya adalah gunanya), dan atribut itu menyuruh pembaca layar
  mengumumkan "tidak tersedia" pada 89,5 persen bintang di profil kosong.
* **Fokus yang dipindah program wajib terlihat.** Semua `focus()` memakai
  `preventScroll`, jadi `deltaGulirTampak` (murni, diuji) yang menggulir jendela
  (bukan `scrollIntoView`) pada zum 125 persen ke atas; di mode panel-di-bawah
  `deltaGulirPanel` menggulir ke judul panel sesudah bintang dipilih, dibatasi
  `bintangAtas` supaya bintang di bagian atas kanvas (yang ada di atas panel)
  tidak terdorong ke bawah pil atas tepat saat dipilih (dulu 4 dari 12 klik
  di 320x568 sampai 952x600). Dasar
  ukur lulus-gagal adalah TINGGI PAKAI (544, 592, 650 px), bukan tinggi layar
  (layar 1080 memberi viewport 904): aksi utama panel ("Mulai membaca") ada tepat
  di bawah pil status karena di bawah paragraf pembuka ia terpotong pada tinggi
  < 656 px.
* **Alamat Langit dibaca satu pintu: `bacaAlamat` (lensa-teks.ts).** Persen-sandi
  rusak (`#/langit/%`) melempar `URIError` di dalam `useEffect`, dan tidak ada
  error boundary: SELURUH pohon React kosong sampai muat ulang. Jangan memanggil
  `decodeURIComponent` di tempat lain.
* **Huruf peta mengikuti `rem`**, dan ambang peta/Daftar dikalikan faktor ukuran
  huruf aplikasi (`AMBANG_PETA` 1.156 px pada 16 px, 1.445 pada 20 px). Lensa
  meneruskan faktor itu ke penata label (`skalaTeks`). Tulis `px` di teks peta
  dan setelan "Ukuran huruf" berhenti mengubahnya (dijaga
  `test_ukuran_huruf_peta_mengikuti_rem`).
* **Daftar (akar < 1.156 px) bukan tepi dan tidak boleh dibuang**: ia yang
  tampil pada zum 125 persen di laptop 1366 dan 1440, jendela setengah layar,
  dan reflow WCAG 1.4.10. Ia membawa penanda "mulai di sini" yang sama dengan
  peta, dan lencana "N cocok" bila konsep menyala.
* **Anggaran gerak**: nol animasi tak berhingga di SVG, entri <= 2 elemen,
  satu transisi pada satu elemen (cincin terpilih; dijaga
  `test_hanya_satu_transisi`), `tingkatGerak()` dibaca saat render. Sorot hover
  di ikhtisar ditulis ke DOM lewat ref, satu kali per bingkai; di sana jangan
  menjadikannya state React (selisih 6 sampai 8 ms per gerakan pada CPU 4x
  terisolasi; mesin berderau). Di lensa sorot (`hov`) memang state React:
  paling banyak 60 bintang. "Layar ini 83 sampai 96 persen sibuk saat diam"
  hanya benar bila beberapa kurikulum sudah selesai: satu reticle berputar per
  kurikulum, dan pada profil pemilik 13 persen.
* **Latar `Cahaya` ikhtisar dibatasi ke kotak tiap gradien** (2026-10-27). Ia 32
  sampai 64 `radial-gradient` pada satu elemen 1800x1826 (di 1905), dan tiap
  lapis dulu menggambar SELURUH kotak itu: satu langkah ubah ukuran jendela
  menahan thread utama 2 sampai 6 detik di Chrome headless (median 2,3 detik
  pada delapan langkah; layar Bahasa 63 ms), dan tanpa latar itu sekitar 60 ms.
  Sekarang tiap lapis punya `background-size` dan `background-position`
  sendiri (2 x jari-jari), dan satu langkah sekitar 60 ms. Tampilannya sama
  dengan mata, tapi TIDAK identik byte demi byte (selisih paling besar 8 dari
  255, hampir semuanya 1 sampai 2). Chrome ber-GPU belum diukur. Dijaga
  `test_cahaya_ikhtisar_dibatasi_ke_kotaknya`.
* **Kartu judul hover menangkap penunjuk** (dapat dilayangi, WCAG 1.4.13), dan
  itu dulu menutup 21 sampai 28 persen perpindahan alami dari bintang ke
  tetangganya (pusat tetangga di bawah kartu). Kartu meneruskan sorot dan klik
  ke bintang yang glifnya ada di bawah penunjuk (`bintangDiBawahKartu`); yang
  diukur `alur-nyata.mjs` (python, 1366x768 dan 1905x904, nol salah).
* **Garis rasi ikhtisar dari tepi glif ke tepi glif** (`ruasIkhtisar`), bukan
  `ruasAntara`: yang kedua dibuat untuk satuan viewBox dan menolak ruas
  berselisih tepi < 4, jadi di piksel garisnya tergambar 35, 53, dan 69 persen
  di akar 1156, 1440, dan 1905 px. Sekarang >= 98 persen (ditagih
  `banding-lensa.mjs`, [garis]).
* **Kata kapsul "mulai di sini" dari status bintang sasarannya** (`kataMulai`:
  sebagian = "Lanjutkan di sini", lainnya "Mulai di sini"), bukan dari XP.
  Jawaban `/api/langit` divalidasi bentuknya sebelum dipakai
  (`bentukJawabanSah`): `200 {}` dulu mengosongkan seluruh pohon React. Nomor
  bintang di alamat hanya bilangan bulat utuh (`/1.5` dan `/1e3` diabaikan).
* **Keadaan perkakas** (konsep, profesi) di `history.state`, bukan
  localStorage: Kembali dari materi memulihkannya, kunjungan besok tidak
  membuka peta yang sudah meredup. Profesi tujuan dari server diturunkan
  (`profesiPilihan ?? d.tujuan`), tidak disalin ke state: yang disalin tertulis
  ke `history.state` seolah pilihan pelajar dan basi begitu tujuannya diganti
  di Peta Karier. Alamat lensa ditulis `replaceState`, jadi
  Kembali peramban melompati lensa (keputusan sadar, sama dengan Peta Karier).
* **Dua bahasa warna hidup berdampingan** sampai ada ronde CSS-saja untuk
  `PetaRasi`: Bahasa dan Dasbor masih memakai kuningan = selesai.
* **Pengukuran di peramban tinggal di repo**: `packages/web/uji/manual/`
  (tiga belas berkas: `alur-nyata.mjs`, `ukur-lensa.mjs`, `ukur-peta.mjs`,
  `tangkap.mjs`, `fokus-dialog.mjs`, `ukur-konsep.mjs`, `kontras.mjs` + `kontras.py`, `perf-*.mjs`,
  `regresi-piksel.mjs`, dan `lib.mjs`; hanya GET, jalankan dengan profil
  terpisah) dan `alat/uji_gigi_blok.py` (baterai mutasi pagar CSS dan sumber;
  ia menyunting berkas di tempat dan memulihkannya, jadi jalankan di salinan
  pohon dan ia gagal bila ada sel yang dilewati). Kriteria terima irisan
  menunjuk berkas-berkas itu, bukan skrip di direktori sesi yang suatu hari
  dibersihkan.
* **Chip konsep dicocokkan dengan JUDUL, dan huruf di dalam kata lain tidak
  boleh menyalakannya.** Pola lama menyalakan `oop` di "L-oop" (19 judul, hampir
  semua Loop, jadi "Objek & class"), `race` di "T-race", `dict` di "pre-dict",
  `teks` di "Kon-teks", `sub` di "Pub/Sub", dan `struct` di "Infrastructure".
  Sekarang 22 judul lepas dan 3 masuk (judul Algoritma yang nyata),
  semuanya diperiksa satu per satu; salah cocok karena MAKNA (CSS "Class, ID")
  tetap ada dan tidak bisa ditutup pencocokan judul. Ukur dengan
  `uji/manual/ukur-konsep.mjs` sebelum mengubah `KONSEP`; sifatnya ditagih
  `banding-lensa.mjs` ([konsep]). Layar lama di `/lama` tetap memakai pola
  lamanya. Tanpa lookbehind: modul yang gagal diurai mematikan seluruh aplikasi.
* **Daftar punya tautan lewati sendiri** ("Lewati ke daftar rasi"), seperti peta.
  Tanpa itu papan ketik melewati sekitar 16 kontrol saringan lebih dulu, di
  layar yang justru dipakai orang yang paling bergantung pada Tab.
* **`/api/bahasa` yang gagal disebut di panel**, bukan diam: bintang terkunci
  tanpa alasan dan tanpa tanda ada yang gagal dulu terbaca seperti keadaan
  biasa. Dijaga `alur-nyata.mjs` (500 disimulasikan, dengan kontrol normal).

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
  didaftarkan di `data/__init__.py` atau ditulis tangan di `inti/kurikulum.py`.
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
  `document`. `isi.bahasa_blok`, `tebak.py`, dan `test_solutions` semuanya
  membaca medan ini.
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

## Jalan ke MERN (2026-10-20)

Pemilik minta aplikasi ini di-refactor jadi MERN + TypeScript, sekaligus
sebagai cara belajar stack itu. Rencananya bertahap, dan tiap tahap berhenti
di keadaan yang masih utuh. Yang SUDAH dikerjakan:

**Tahap -1 — terminal dibuang.** `layar/` (3.376 baris), `main.py`, dan 150
tes TUI dihapus. Yang dipindahkan lebih dulu, karena lapisan web memakainya:
`LANGUAGES` + `VERSI` + `_stat` + `_teks_laporan` ke `inti/kurikulum.py`,
logika latihan ke `inti/latihan.py`, `teks_polos` ke `inti/materi.py`.
Ketiganya dibuktikan identik dengan aslinya sebelum yang lama dihapus.
Hasil yang dikejar: `import webapp.api` sekarang TIDAK memuat satu pun modul
terminal. Jangan membuat lapisan web mengimpor dari lapisan tampilan lagi.

**Tahap 0 — konten jadi JSON.** `alat/ekspor_konten.py` menulis
`packages/konten/`: 32 kurikulum, bab, kuis_materi, karier, gambar, dan
pustaka. Aturannya:

* **Kuis disimpan MENTAH**, sebelum `normalisasi.seimbangkan_kuis` memutar
  posisi opsinya. Kalau yang tersimpan hasil rotasi lalu pembacanya memutar
  lagi, opsi berputar DUA KALI -- dan `test_normalisasi_menjaga_jawaban_tetap_benar`
  tetap hijau, karena rotasi memang menjaga korelasi opsi dengan jawabannya.
  Yang rusak diam-diam cuma penjelasan soal yang menyebut posisi opsi.
  `sidik.json` menyimpan SHA-256 hasil pasca-rotasi sebagai pagarnya.
* **Buktinya roundtrip, bukan suite.** `test_data.py` adalah tes SKEMA; ia
  tetap hijau walau sebuah nilai berubah asal bentuknya sah. Yang membuktikan
  lossless adalah ekspor -> impor balik -> `==` terhadap objek Python asli.
* **Jangan memformat ulang `packages/konten/**.json`** (ada di
  `.prettierignore`). Sekali diformat, 16 MB berubah tanpa ada yang tahu apa
  yang bergeser.
* `tests/test_konten_json.py` mengadu JSON dengan sumber Python tiap suite
  jalan, jadi menyunting `data/` tanpa mengekspor ulang langsung memerah.
* Kunci berbentuk angka DILARANG: `JSON.parse` di V8 menata ulang kunci
  seperti `"0"` ke depan, jadi objeknya tidak pulih sama di sisi JavaScript.

**Tahap 0,5 — algoritma bersama: `sorot` dan `beda` sudah diport.**
`inti/sorot.py` -> `packages/bersama/src/sorot.ts`, `inti/beda.py` ->
`src/beda.ts`. Pembuktiannya bukan "dibaca sepertinya sama":
`uji/golden-sorot.ts` membangun ulang korpusnya dari `packages/konten/` lalu
mengadu sidik SHA-256 token untuk SELURUH 3.315 blok kode kurikulum, dan
`uji/golden-beda.ts` mengadu 312 pasangan keluaran -- keduanya melawan rekaman
yang dibuat dari Python SEBELUM port itu ada. Ikut suite lewat
`test_konten_json.TestAlgoritmaTypeScript` (skip kalau `node` tidak ada, bukan
lulus diam-diam). Yang mengikat:

* **`difflib.SequenceMatcher` DIPORT, bukan diganti pustaka.** Ia bukan Myers
  diff: Ratcliff/Obershelp, cari blok cocok terpanjang lalu rekursi ke kiri
  dan kanannya. `diff`/`fast-diff` npm akan memberi penyejajaran berbeda untuk
  baris yang berpindah tempat, dan yang pelajar lihat bukan "diff-nya lain"
  melainkan penjelasan yang menunjuk baris yang salah. `autojunk=False` juga
  bagian dari kontraknya.
* **Dua loop perluasan CPython sengaja TIDAK diport.** Keduanya ada di balik
  `not isbjunk(...)`; tanpa junk, DP `j2len` sudah menghitung run terpanjang
  di setiap `(i, j)`, jadi tidak ada sisa untuk diperluas. Diukur: dengan
  keduanya dicabut, ke-312 pasangan tetap cocok. Yang membatalkan alasan itu
  cuma satu -- menyalakan `isjunk` atau `autojunk=True` di `inti/beda.py`.
  Kalau itu terjadi, keduanya WAJIB ikut diport.
* **`render()` dan `_potong()` tidak ikut.** Keduanya menggambar diff ANSI 76
  kolom untuk terminal yang sudah dibuang. React menggambar `Beda` sendiri.
* **Pasangan uji `beda` ada dua jenis.** 12 ditulis tangan untuk heuristik
  DIAGNOSISNYA, 300 DIHASILKAN dengan seed tetap (`20261020`) untuk
  penyejajarnya. Seed itu bagian dari rekaman: menggantinya berarti mengganti
  seluruh korpus, dan rekaman yang korpusnya berubah tidak membuktikan apa pun
  soal perubahan yang sedang diperiksa. Perluas dengan MENAMBAH di ujung.
  Tiga pasangan terakhir di `PASANGAN` ada khusus untuk menutup cabang
  diagnosis yang tidak pernah terpicu korpus hasilan -- ditemukan oleh baterai
  mutasi, bukan dengan dibaca.

* **Jangan bangun korpus golden dari `lang["runner"]`.** Yang dipakai
  aplikasi `isi.bahasa_blok` (materi) dan `isi.bahasa_sorot` (latihan), dan
  keduanya melewati `berkas.sorot_untuk`. Versi pertama alat ini memakai
  runner mentah, dan 408 dari 3.315 kasus direkam untuk bahasa yang tidak
  pernah dipakai -- `terminal` bukan bash, `jsx` bukan javascript,
  `postgresql` bukan sql. 344 di antaranya menghasilkan token yang BERBEDA,
  jadi rekamannya membekukan jalur mati: pagar yang tidak bisa memerah untuk
  perubahan nyata, dan memerah untuk perubahan yang tidak pernah terlihat.
* **Sidik memakai `separators=(",", ":")`.** Bawaan `json.dumps` menyisipkan
  spasi, `JSON.stringify` tidak pernah. Tanpa pemisah yang sama, sidik yang
  dua-duanya BENAR tetap berbeda -- dan gejalanya tiga ribu sidik yang tidak
  satu pun cocok, yang terbaca seperti port yang gagal total. `golden_beda`
  menyidik sebuah dict, jadi sisi TS yang mereproduksinya nanti wajib
  mengurutkan kunci sendiri; `JSON.stringify` tidak melakukannya.
* **`bahasa_didukung()` bukan uji keanggotaan.** Ia membuang duplikat
  berdasarkan `id()`, jadi ia menjawab "ada berapa SET aturan", bukan "nama
  apa saja yang dikenali". Memakainya sebagai `in` menggolongkan setiap alias
  sebagai tidak tersorot, dan `aplikasi` (68 blok, alias Java) langsung
  melompat ke puncak daftar sebagai buktinya. Yang benar `in sorot.ATURAN`.
* **Tabel kata kuncinya DIHASILKAN, bukan diketik ulang di TS**
  (`alat/ekspor_bersama.py` -> `packages/bersama/data/aturan-sorot.json`).
  Alias ikut diekspor sebagai peta nama, dan pemetaan `sorot_untuk` ikut
  dibawa supaya sisi TS tidak menulis tabel keduanya.
* **Tidak ada langkah build untuk paket ini.** Node 24 menjalankan `.ts`
  langsung lewat pelucutan tipe; `tsc` cuma pemeriksa (`npm run tipe`,
  `noEmit`). `npm install` di akar memasang SATU perkakas (`@types/node`).
  Aplikasinya sendiri tetap jalan dengan `python3 belajar-web.py` tanpa npm.
* **Pagarnya sudah diuji bisa MERAH**, dan itu bagian dari pekerjaannya:
  `alat/uji_gigi_golden.py` (3 mutasi di sisi Python) dan
  `packages/bersama/uji/gigi-golden.py` (8 mutasi di sisi TS, tiap sel menagih
  KATEGORI keluhannya, bukan cuma kode keluar bukan-nol). Baterai itu yang
  menemukan dua hal yang tidak kelihatan saat dibaca: dua loop mati di port
  `SequenceMatcher`, dan satu cabang diagnosis yang tidak pernah terpicu
  korpusnya. Keduanya hijau di baterai berarti "tidak terbukti apa-apa", bukan
  "lulus" -- sel yang tumpul dibetulkan, bukan diterima.
* **Sidiknya lewat satu penyerial, `uji/sidik.ts`.** Ia yang mengurutkan kunci
  objek; `JSON.stringify` tidak. Tanpa itu sidik `bandingkan` bergeser setiap
  kali urutan dua medan ditukar di kode -- perubahan yang tidak mengubah satu
  pun perilaku.

**Temuan sampingan yang belum dikerjakan: 421 dari 3.315 blok kode tampil
TANPA warna.** Rekaman cakupan di `golden/sorot.json` menamai semuanya. 118 di
antaranya `"teks"` dan memang harus polos (diagram). Sisanya 303 blok di 76
bahasa yang tidak punya aturan di `sorot.py` -- yang terbesar `yaml` (59),
`swift` (24), `dart` (17), `http`/`lua`/`r` (13 masing-masing). Semuanya lahir
bersama 12 kurikulum tech stack. Menambah aturan untuk salah satunya sekarang
terbaca sebagai perbaikan yang terukur di angka `cakupan`, bukan sebagai
"golden bergeser".

**Tahap 1 — React + TypeScript DIMULAI.** `packages/web`: Vite 7 + React 19,
di atas API Python yang sama. Satu layar sudah diport (`layar-tebak` ->
`src/layar/Tebak.tsx`), beserta klien API bertipe, komponen `Kode`, dan
komponen `Keadaan`. Antarmuka LAMA masih utuh dan masih yang dilayani
`belajar-web.py`; React jalan di dev server terpisah. Yang mengikat:

* **Server TIDAK diubah sama sekali untuk mengakomodasi dev server.** Setiap
  `/api/*` tetap menuntut `X-Belajar-Token`. Plugin `belajar-token` di
  `vite.config.ts` MENGAMBIL tokennya sendiri dari `GET /` server Python,
  yang memang dilayani tanpa token. Melonggarkan pemeriksaannya "untuk mode
  dev" berarti melepas pagar sungguhan di server yang mengeksekusi kode
  pelajar; menyalin token ke `.env` berarti 403 sesekali yang selalu
  disalahartikan sebagai bug aplikasi.
* **`transformIndexHtml` TIDAK BISA mengubah isi skrip inline.** Vite
  mengekstrak badan `<script>` sebagai modul lalu menyajikan yang ASLI, jadi
  penggantian di dalamnya dipulihkan diam-diam. Diukur: pada SATU rantai
  `.replace()`, penanda sebelum `</head>` mendarat sementara penggantian di
  dalam `<script>` tidak -- padahal hook-nya terpanggil dan `html` yang masuk
  memang memuat placeholder-nya. Nol peringatan di mana pun. Token karena itu
  disuntik lewat `tags` + `injectTo: "head-prepend"`.
* **Tiga jebakan saat MENGUJI dev server, semuanya menghasilkan
  negatif-palsu.** (i) `curl` tanpa `Accept: text/html` membuat Vite melayani
  `index.html` lewat jalur berkas statik, mentah, tanpa transform.
  (ii) Tanpa `server.host: "127.0.0.1"`, Vite mengikat ke `localhost` yang di
  mesin ini beresolusi ke `::1` lebih dulu, dan `curl` ke `127.0.0.1` gagal
  konek. (iii) `( cmd ) &` lalu `kill $!` membunuh subshell dan
  MENELANTARKAN Vite-nya; instance lama itu yang menjawab seluruh curl
  berikutnya, dari konfigurasi yang sudah tidak ada lagi. Skrip
  verifikasinya ada di riwayat sesi; ketiganya ditutup di sana.
* **`gaya.css` TIDAK ditulis ulang.** 6.508 baris dan 112 token desain
  diproksi dari server Python apa adanya, bersama `/huruf` dan `/vendor`.
  Menyalinnya berarti dua lembar gaya untuk satu desain, dan yang kedua akan
  ketinggalan tanpa ada yang menyadarinya.
* **`noUncheckedIndexedAccess` menyala di KEDUA paket TS.** Menyalakannya di
  `web` saja membuat `packages/bersama` gagal tipe saat diimpor, dan dua
  tingkat kekakuan dalam satu workspace adalah bau yang akan menggigit nanti.
  Akses indeks di pemindai diubah ke `charAt` (bukan `!`): di dalam jangkauan
  perilakunya identik, dan rekaman golden yang MEMBUKTIKANNYA -- 3.315 blok
  tetap cocok sesudah perubahan itu.

* **Pembanding `banding-rasi.mjs` jenisnya BEDA dari golden.** Ia mengadu
  dengan implementasi JS yang masih hidup (`rasi.js`), bukan dengan rekaman,
  karena keduanya JavaScript dan fungsinya murni -- tidak ada sisi Python yang
  perlu direkam. Yang dijaganya: bentuk tiap rasi deterministik dari benih
  (nama kurikulum), jadi satu bit yang meleset di `hash` atau `prng` mengubah
  SETIAP rasi tanpa satu pun error. Ia menolak kalau potongan sumber yang
  dicarinya tidak ketemu, alih-alih membandingkan nol fungsi.

**Urutan port sisanya ditentukan KETERGANTUNGAN, bukan jumlah baris.** Diukur:
`layar-karier` (601 baris) mengimpor `layar-belajar.js` yang 3.408 baris, jadi
ia bukan "layar kecil berikutnya". `layar-langit` (219) satu-satunya yang cuma
butuh `rasi.js` plus satu fungsi dari `gerak.js`.

| Layar | Baris | Menarik | Keadaan |
|---|---|---|---|
| `layar-tebak` | 114 | `sorot`, `sampul`, `gerak` | **SUDAH** -> `layar/Tebak.tsx` |
| `layar-pustaka` | 204 | `sampul`, `ikon` | **SUDAH** -> `layar/Pustaka.tsx` |
| `layar-langit` | 219 | `rasi.js`, `gerak` | **SUDAH** -> `layar/Langit.tsx` |
| `layar-karier` | 601 | `saatSiap` saja dari `layar-belajar` | **SUDAH** -> `layar/Karier.tsx` |
| `layar-lain` | 867 | `ikon`, `sampul`, `istirahat`, `gerak` | **SUDAH** -> `Statistik.tsx` + `Atur.tsx` |
| `aplikasi.js` cangkang | ~300 dari 1.570 | — | **SUDAH** -> `Cangkang.tsx` |
| `layar-kerja` | 2.182 | `editor`, `pratinjau`, `sorot`, `layar-belajar` | **SUDAH** -> `Kerja.tsx` + `Kuis.tsx` |
| `layar-belajar` | 3.408 | sepuluh modul, termasuk `visual` dan `jejak` | **SUDAH** -> `Belajar.tsx` + `Bahasa.tsx` + `Dasbor.tsx` + `Lain.tsx` |
| `ikon.js` | 144 | — | **SUDAH** -> `komponen/Ikon.tsx` |
| `rasi.js` `petaRasi` | 90 dari 265 | `gerak` | **SUDAH** -> `komponen/Rasi.tsx` |
| `sampul.js` | 233 | — | **SUDAH** -> `komponen/Sampul.tsx` |
| `langit.js` | 332 | `gerak` | **SUDAH** -> `langit.ts` |
| `kursor.js` | 194 | `gerak` | **SUDAH** -> `kursor.ts` |
| `permukaan.js` | 67 | — | **SUDAH** -> `permukaan.ts` |
| `sinema.js` | 89 | `gerak`, GSAP | **SUDAH** -> `sinema.ts` |
| `beranda.js` | 124 | GSAP ScrollTrigger | **TIDAK**, dan sengaja: nol pemanggil |
| `aplikasi.js` palet perintah | ~495 | `ikon` | **SUDAH** -> `komponen/Palet.tsx` |
| `aplikasi.js` pintasan + bantuan | ~266 | — | **SUDAH** -> `komponen/Pintasan.tsx` |
| `aplikasi.js` lencana XP/streak | ~60 | `ikon` | **SUDAH** -> `komponen/Lencana.tsx` |
| `aplikasi.js` bilah maju baca | ~49 | — | **SUDAH** -> `komponen/Lencana.tsx` |

Yang sudah berdiri di `packages/web/src/`: `api.ts` (klien bertipe,
satu-satunya yang tahu soal token), `gerak.ts` (`tingkatGerak()`,
SATU-SATUNYA yang boleh membaca `data-gerak`), `lokal.ts` (preferensi
tampilan; kuncinya DIBAGI dengan antarmuka lama), `waktu.ts` (`tanggalLokal()`
satu-satunya pintu untuk ISO server), `sorak.tsx` (toast + `salin`),
`util.ts` + `util.tsx` (yang TANPA JSX di `.ts`, supaya pembanding `.mjs` bisa
mengimpornya tanpa menyeret React; `util.tsx` meneruskannya), `Cangkang.tsx`,
`komponen/{Kode,Keadaan,Bilah,Rasi,Ikon,Sakelar,Tanda,Lencana,Pintasan,Palet}.tsx`,
`komponen/{rasi-geometri,ikon-bentuk,pintasan-tabel,palet-cari}.ts`.
Layar Langit (ikhtisar 32 rasi + lensa satu rasi): `layar/Langit.tsx` (data,
alamat, keadaan perkakas), `layar/LangitIkhtisar.tsx` (peta),
`layar/LangitLensa.tsx` (rasi diperbesar), `layar/LangitPanel.tsx` (detail
bintang), `layar/LangitDaftar.tsx` (layar sempit), `layar/langit-data.ts`
(bentuk jawaban `/api/langit` beserta validatornya, `TATA`, `KONSEP`),
`komponen/Glif.tsx`, `komponen/{lensa-geometri,lensa-teks}.ts`.

**Keempat modul peng-ukur DOM SUDAH diport** (2026-10-20), beserta ruang kerja
latihan, Ruang Coba, dan pembaca materi. Polanya satu dan dipakai keenam
kalinya tanpa kecuali: **bagian murni di `.ts`, komponennya di `.tsx`, lalu
satu pembanding yang mengadu bagian murni itu dengan JS yang masih melayani
aplikasi lama.** Pembagian berkasnya punya sebab teknis, bukan selera: Node
melucuti TIPE dari `.ts` tapi tidak melucuti JSX dari `.tsx`, jadi hanya berkas
`.ts` yang bisa diimpor pembandingnya.

| Modul | Murni | Komponen | Pembanding |
|---|---|---|---|
| `editor.js` | `komponen/editor-teks.ts` | `Editor.tsx` | 3.315 blok kode |
| `pratinjau.js` | `komponen/pratinjau-css.ts` | `Pratinjau.tsx` | 3.315 x 8 + byte `PELAPOR` |
| `visual.js` | `komponen/visual-bentuk.ts` | `Visual.tsx` | 1.356 gambar, simpul demi simpul |
| `jejak.js` | `komponen/jejak-teks.ts` | `Jejak.tsx` | 2.757 blok + 22 kalimat |
| `layar-kerja` | `layar/kerja-beda.ts` | `layar/Kerja.tsx` | 2.790 pasangan diff hasilan |
| `layar-belajar` | `layar/belajar-teks.ts` | `layar/Belajar.tsx` | 135.620 baris prosa |
| prosa bersama | `komponen/prosa-teks.ts` | `komponen/Prosa.tsx` | 153.959 baris prosa |
| `ikon.js` | `komponen/ikon-bentuk.ts` | `komponen/Ikon.tsx` | 26 ikon x 4 ukuran, atribut demi atribut |
| `rasi.js` tata peta | `komponen/rasi-geometri.ts` | `komponen/Rasi.tsx` | 201 peta utuh, 69 bentuk kurikulum |
| `layarBahasa` | `layar/bahasa-teks.ts` | `layar/Bahasa.tsx` | 32 kurikulum x 7 profil progres |
| `layarDasbor` | `layar/dasbor-teks.ts` | `layar/Dasbor.tsx` | 360 profil hasilan, benih 20261026 |
| palet perintah | `komponen/palet-cari.ts` | `komponen/Palet.tsx` | 247 teks x 35 kueri, urutan penuh |
| layar Langit | `komponen/lensa-geometri.ts`, `komponen/lensa-teks.ts`, `layar/langit-data.ts` | `layar/Langit*.tsx`, `komponen/Glif.tsx` | 440.982 sifat (`banding-lensa.mjs`: tidak ada JS lama untuk diadu), `ringkasPembuka` diadu `golden-pembuka.json` (110 kasus, dibangkitkan `alat/golden_pembuka.py`) |

Keenam belas pembanding di `packages/web/uji` ikut suite lewat `SKRIP_WEB` di
`test_konten_json.TestAlgoritmaTypeScript`, dan **204 sel mutasi** di
`packages/bersama/uji/gigi-golden.py` (192 untuk keenam belas pembanding web,
12 untuk ketiga golden `bersama`) membuktikan semuanya bisa MERAH. Pagar CSS dan
sumber layar Langit punya baterainya sendiri, `alat/uji_gigi_blok.py` (58 sel).

**`--experimental-strip-types` diberikan eksplisit** ke `node` di suite MAUPUN
di baterai. Pelucutan tipe baru tanpa-flag sejak Node 23.6 (22.18 di jalur
LTS); di bawah itu SELURUH pembanding gagal dengan
`ERR_UNKNOWN_FILE_EXTENSION` -- empat belas tes merah karena alasan yang tidak
ada hubungannya dengan isinya. Terukur: flagnya diterima apa adanya oleh 22.11
maupun 24.21, jadi memberikannya selalu lebih murah daripada mendeteksi
versinya. Skrip `banding` di `packages/web/package.json` memasangnya sekali
lewat `export NODE_OPTIONS=`; sebelum itu ia memanggil `node` telanjang, jadi
daftar dua belas pembanding yang lengkap itu **tidak bisa dijalankan sama
sekali** -- dan tidak ada yang menyadarinya karena suite memakai jalurnya
sendiri.

**Pembanding baru wajib terdaftar di TIGA tempat**, dan `test_konten_json
.test_setiap_pembanding_terdaftar_di_tiga_tempat` menagihnya dari isi direktori
`packages/web/uji`: `SKRIP_WEB` (ikut suite), skrip npm `banding` (bisa
dijalankan sekaligus, beserta pelucut tipenya), dan `BATERAI` di
`gigi-golden.py` (ada bukti ia bisa MERAH, dan daftar mutannya tidak kosong).
Yang paling mahal kalau terlupa yang ketiga: pembanding tanpa sel mutasi adalah
pembanding yang hijaunya tidak berarti apa pun. Pagar itu MENGIMPOR tabel
baterainya, tidak meng-grepnya -- versi yang meng-grep diloloskan oleh nama
yang utuh di dalam string yang sudah rusak, dan oleh nama di sebuah komentar.

**Baterai itu menemukan empat hal yang tidak kelihatan saat dibaca**, dan
keempatnya sekarang tertulis di komentar fungsinya masing-masing beserta
angkanya: pin langkah terakhir `pisahRekor` tidak pernah mengubah hasil
(`ceil(n*k/k) === n`), `POLA_KODE.lastIndex = 0` tidak pernah berpengaruh
(`exec` menyetelnya sendiri saat loop habis), ambang 52 di `labelPeta` cuma
menanggung beban dari BAWAH (8.475 baris di [52,62) tidak berubah), dan
`.textContent` di `gTata` adalah satu-satunya pembacaan DOM di lapisan geometri
visual. Yang tiga pertama DIPERTAHANKAN -- yang dijaganya rumus berikutnya,
bukan rumus sekarang -- dan sekarang itu tertulis, bukan tersirat.

**Satu celah nyata ikut ketemu dan sengaja DIBAWA apa adanya:** runner `git`
lolos `runner.tersedia()` jadi ia muncul di pemilih Ruang Coba, tapi
`contohAwal` tidak punya entri untuknya -- editornya terbuka KOSONG, sementara
kurikulum sejenisnya (`fedora`) punya skrip awal. Port ini menuntut identitas
byte dengan `layar-kerja.js`, jadi menambalnya di satu sisi akan memerahkan
pembandingnya. Ia dicatat sebagai `CELAH_DIKETAHUI` di `banding-kerja.mjs`,
dan runner BARU yang contohnya terlewat tetap memerahkan pagarnya. Layak
ditambal di UI baru, di kedua sisi sekaligus.

**SELURUH LAYAR SUDAH DIPORT** (2026-10-26). Lima belas layar: Dasbor (dua
keadaan), halaman bahasa, pembaca materi, kuis, ruang kerja latihan, Ruang
Coba, Langit, Peta Karier, Pustaka, Statistik, Pengaturan, Tebak keluarannya,
Bookmark, Catatanku, dan Cari. Tiga kuis invarian yang sudah ditelusuri dan
jangan ditelusuri ulang: muatan soal dari `sesi.bersih()` TIDAK membawa kunci
jawaban dan `penjelasan` datang dari respons `/api/kuis/jawab`; index jawaban
SUDAH dipetakan ulang di `sesi._acak_soal`; dan jam mode timer BERHENTI saat
tabnya di latar lalu melanjutkan dari sisa detik yang sama (WCAG 2.2.2).

**TIGA MODUL GERAK DI LUAR LAYAR IKUT KEMBALI** (2026-10-26): reticle
teleskop (`kursor.ts`), sorot samar di bawah kursor (`permukaan.ts`), dan judul
yang tiba kata demi kata (`sinema.ts`). Ketiganya ada di antarmuka lama dan
hilang tanpa jejak di React -- tidak ada galat, cuma aplikasi yang terasa lebih
datar daripada versi yang digantikannya. Yang mengikat:

* **`beranda.js` TIDAK diport, dan itu bukan kelalaian.** Sejak dasbor jadi
  meja kerja, `gerakBeranda()` tidak menemukan `.beranda-hero` maupun
  `.beranda-kalimat-isi`, jadi ia memang tidak menggerakkan apa pun -- dan itu
  sudah tertulis di `layar-belajar.js` sendiri. ScrollTrigger karena itu juga
  tidak dimuat halaman React: 70 KB untuk nol pemanggil.
* **Kedua tag GSAP WAJIB berdiri di atas modul React, di dalam `<head>`.**
  Skrip `defer` dan `type="module"` sama-sama dieksekusi menurut URUTAN
  DOKUMEN, dan `vite build` menempelkan modulnya di KAKI `<head>`. Di kaki
  `<body>` -- tempat keduanya mula-mula ditaruh -- GSAP jalan SESUDAH bundel,
  dan `gsapSiap()` mengembalikan null untuk layar pertama. Yang terlihat bukan
  galat melainkan judul pertama yang SESEKALI tiba tanpa gerak, tergantung mana
  yang lebih dulu selesai antara berkas vendor dan permintaan API pertama.
* **`ungkapJudulSaatTiba()` ada karena React menggambar cangkang LEBIH DULU.**
  Di `aplikasi.js` router MENUNGGU data layarnya, jadi `ungkapJudul()` selalu
  mengukur halaman yang sudah penuh. Di React `#layar` masih sebuah pusaran
  saat efeknya jalan: terukur NOL kata terpecah di seluruh delapan layar pintu,
  tanpa satu pun galat. Kembaran dari pengamat ukuran di bilah kemajuan baca,
  dan pengamatnya WAJIB lepas -- pada kedatangan `h1` atau pada batas 4 detik.
* **Daftar `LAYAR_PINTU` tinggal di DUA tempat dan diadu tes.** Judul
  kata-demi-kata sengaja tidak dipasang di materi, latihan, dan kuis: ketiganya
  dibuka ratusan kali dalam satu sesi panjang. Dua daftar yang melenceng satu
  nama tidak memerahkan apa pun dengan sendirinya, jadi
  `TestSinemaKursorPermukaan` mengadu keduanya.
* **Ketiganya mengembalikan PEMBERSIH**, beda dari sisi JS yang memasang
  pendengarnya sekali dan selamanya. Efek React dipasang dua kali di
  StrictMode; tanpa pembersih yang tertinggal satu set pendengar dan satu
  reticle per pemasangan.
* **Kursor ASLI tidak pernah disembunyikan.** Ukuran dan kontras kursor yang
  dipilih orang di sistemnya sering merupakan akomodasi penglihatan, dan di
  tingkat gerak "mati" reticle-nya memang tidak digambar -- `cursor: none` akan
  meninggalkan halaman tanpa penunjuk sama sekali.

Tidak ada pembanding `.mjs` untuk ketiganya, dan alasannya bisa disebut:
`sinema` menuntut GSAP yang cuma ada di peramban, sementara `kursor` dan
`permukaan` seluruh isinya efek samping atas DOM sungguhan -- tidak ada bagian
murni yang bisa diadu. Yang membuktikannya pengukuran di Chrome, dan yang
dijaga tes justru cacat-cacatnya yang DIAM. Baterai enam sel menemukan dua
pagar yang tidak menggigit: `count(".revert()") >= 2` dikalahkan oleh DOCSTRING
modul itu sendiri yang menyebut `split.revert()` sebagai kalimat penjelas, dan
asersi CDN ternaungi asersi "ada di `<head>`" yang menyala lebih dulu.

**CANGKANGNYA JUGA SUDAH UTUH** (2026-10-26): palet perintah (Ctrl+K, combobox
APG, ingatan kemutakhiran 14 hari), pintasan papan ketik beserta dialog
bantuannya, lencana XP dan streak, dan bilah kemajuan baca. Dengan itu seluruh
1.570 baris `aplikasi.js` dan 3.408 baris `layar-belajar.js` punya padanannya di
React.

Lima catatan yang mengikat untuk cangkang:

* **`PINTASAN_G` dan `PINTASAN` tinggal di `komponen/pintasan-tabel.ts`**, satu
  definisi untuk tiga pembaca (penangan papan ketik, dialog bantuan, label
  `<kbd>` di palet). Di sisi JS huruf itu pernah ditulis di tiga tempat.
* **Riwayat palet memakai `ingatJson()`, bukan `ingat()`.** Kuncinya DIBAGI
  dengan antarmuka lama, dan `ingat()` menyandikan nilainya sekali lagi -- jadi
  array yang dititipkan lewatnya tersimpan sebagai `"\"[{...}]\""`, dan
  `ctx.ingat` di sisi lama mengurainya jadi STRING lalu memanggil `.filter()`
  di atasnya. Terukur di Chrome sebelum diperbaiki; sesudahnya kedua arah
  dibuktikan: React menulis, palet lama membacanya dan membuka 41 butir; lama
  menulis, React membacanya dengan urutan yang identik.
* **Palet punya satu perintah LEBIH daripada antarmuka lama: "Cari".** Ia
  mengantar ke layar Cari yang punya saringan tipe, sesuatu yang paletnya
  sendiri tidak punya. Urutan ENAM perintah pertama tetap kontrak
  (`TestPaletCombobox` membaca indeksnya), jadi ia disisipkan di posisi
  kesepuluh.
* **`.tampak` di bilah kemajuan baca butuh pengamat ukuran**, dan ini beda
  struktural dari versi JS: di sana router MENUNGGU datanya sebelum menempelkan
  layarnya, jadi `pasangMajuBaca()` selalu mengukur halaman yang sudah penuh.
  Di React cangkang digambar LEBIH DULU -- saat efeknya jalan, dasbor masih
  sebuah pusaran setinggi seratus piksel.
* **Dialog yang digambar sendiri wajib memakai `useFokusDialog`**
  (`komponen/fokus-dialog.ts`): fokus awal masuk ke kotak, Tab terjerat, Esc
  menutup, dan fokus kembali ke pemicunya. `Bantuan`, `Palet`, dan catatan di
  `Tanda` dulu tidak punya satupun: menutupnya menjatuhkan fokus ke awal
  halaman, Tab keluar ke halaman di belakang tirai, dan catatan tidak bisa
  ditutup dengan Esc. Tanpa galat di mana pun. Dialog lewat `Jendela` sudah
  punya semuanya dan berbagi `bisaFokus` dengan pengait itu. Dijaga
  `TestFokusDialog`; perilakunya diukur di peramban.

**UMPAN TEKAN ADALAH `pasangIsyarat()`, DAN ELEMEN SVG TIDAK PERNAH IKUT**
(2026-10-26). Dilaporkan pemilik: layar Peta Karier "rusak" -- gumpalan teks
bertumpuk di pojok kiri atas kartu tangga, dan baris Web serta Mobile nyaris
kosong. Terukur: node `<g role="button" transform="translate(x,y)">` melompat
dari (184, 60) ke (-13, -13) begitu ditekan dan TERPARKIR di sana, bahkan pada
klik biasa. Mekanismenya tiga lapis, dan ketiganya diam:

* Properti CSS `transform` dari animasi WAAPI menimpa atribut `transform`
  node, jadi `translate`-nya hilang selama ditekan.
* Node itu lalu tidak lagi berada di bawah kursor, sehingga `pointerup`
  mendarat di elemen LAIN. Penangan yang melepas `closest(target)` tidak pernah
  menemukannya, dan animasi `fill: "forwards"`-nya tidak dibatalkan.
* Akibatnya klik mouse tidak bisa memilih node sama sekali: peristiwa `click`
  pun tidak sampai ke node.

Akar yang sebenarnya dangkal dan salah saya: port cangkang React TIDAK membawa
`pasangIsyarat()` dari `gerak.js`, melainkan menulis penangan sendiri
(`button, a, [role="button"]` + `closest(target)`), lalu komentarnya keliru
menyebut antarmuka lama "NOL pemanggil" `tekan()`. Pemanggilnya ada, di dalam
`gerak.js` sendiri, dan tes lamanya malah melarang komponen memanggil `tekan()`
langsung. Aturan yang mengikat sekarang:

* **Umpan tekan hanya lewat `pasangIsyarat()`** (gerak.ts), dengan daftar putih
  `BISA_DITEKAN` -- janji bahwa yang menjawab sentuhan memang bisa ditekan,
  bukan selektor umum. Daftarnya diadu dengan `gerak.js` oleh tes, dan tidak
  boleh memuat `[role="button"]`, `svg`, atau `g`.
* **Yang dilepas adalah elemen yang DITEKAN**, dilacak di satu variabel, di
  mana pun jari diangkat. Bukan `closest(target)` saat `pointerup`.
* **`tekan()`/`lepas()` melewati elemen SVG** (lapis kedua, untuk kelas yang
  ditambahkan belakangan). Dicek lewat `namespaceURI`, bukan `instanceof
  SVGElement`: berkas ini diimpor juga oleh pembanding Node.
* **Pelepasnya melepas tombol yang SEDANG ditekan juga.** StrictMode menjalankan
  efek dua kali; tanpa itu tiap pemasangan menyisakan satu tombol mengecil.

`TestIsyaratTekan` (6 tes) menjalankan satu driver Node atas `gerak.js` DAN
`gerak.ts` lalu mengadu langkah demi langkah, dengan dua pengecualian yang
disengaja: versi lama menganimasikan elemen SVG (itu cacatnya), dan pelepas cuma
ada di port. Cacat utamanya juga dicek LANGSUNG di port, bukan hanya diadu:
dua versi yang salah dengan cara yang sama lolos adu. Baterai sepuluh sel
membuktikan tiap pagar bisa merah dengan alasan yang tepat; satu sel sempat
salah-kunci karena yang kena duluan jalur isyarat, bukan jalur langsung.

Pelajaran yang bisa dipakai ulang: **port yang "setia" ke fungsi tapi mengarang
pemanggilnya tidak setia.** `tekan` dan `lepas` disalin byte demi byte, dan
justru `pasangIsyarat` -- satu-satunya yang memutuskan SIAPA yang ditekan dan
KAPAN dilepas -- yang dilewati karena terikat DOM dan tidak ada pembandingnya.
Sebelum menulis penangan pengganti untuk sebuah mekanisme global, baca seluruh
berkas aslinya untuk pemanggil di dalamnya, bukan cuma daftar ekspornya.

## Tahap 1,5 -- Express + MongoDB (2026-10-26)

`packages/catatan`: layanan pencarian catatan. **TAMBAHAN, bukan pengganti** --
aplikasinya jalan penuh tanpa paket ini, dan yang ditambahkan satu kemampuan
yang versi JSON memang tidak punya: pencarian teks BERPERINGKAT di dalam isi
catatan. Dengan itu keempat huruf MERN terpakai di pekerjaan nyata, bukan di
demo.

```bash
podman run -d --name belajar-mongo \
  -p 127.0.0.1:27017:27017 -v belajar-mongo:/data/db docker.io/library/mongo:8
npm run catatan        # http://127.0.0.1:7799
npm run uji --workspace @belajar/catatan
```

Yang mengikat (rincian beserta angkanya di `packages/catatan/README.md`):

* **Berkas JSON tetap SUMBER KEBENARAN; Mongo cuma INDEKS.** Arah datanya satu:
  `~/.belajar_ngoding_catatan.json` -> Mongo. NOL jalur tulis ke berkas itu di
  seluruh paket. Pengaman yang melindunginya -- karantina, `.bak`, tulis
  atomik -- hidup di `pelajar/simpanan.py`, dan tidak satu pun dari itu ada di
  container yang bisa dibuang dengan satu perintah. Konsekuensinya: Mongo yang
  mati tidak pernah berarti catatan yang hilang, ia cuma berarti pencarian yang
  tidak tersedia -- dan layarnya MENGATAKAN itu beserta perintah untuk
  menyalakannya.
* **Progres pelajar tidak pernah menyentuh Mongo.** Untuk 899 byte progres satu
  pengguna, Mongo tidak memberi keuntungan teknis apa pun.
* **Bind loopback, `HOST` KONSTANTA, dan `Host` DIPERIKSA.** Variabel
  lingkungan yang bisa menaikkan bind-nya ke `0.0.0.0` adalah pagar yang bisa
  dilepas tanpa menyentuh satu baris kode, dan pagar seperti itu selalu dilepas
  "sebentar saja" lebih dulu. Bind saja TIDAK cukup: DNS rebinding membelokkan
  nama domain penyerang ke 127.0.0.1, dan peramban lalu menganggap
  permintaannya same-origin sehingga `Origin` tidak dikirim sama sekali --
  pemeriksaan asal yang cuma berlaku "kalau ada Origin" melewatkannya tanpa
  suara. Yang menutupnya `Host`, bentuknya sama dengan `server._asal_sah()`.
  Mongo tanpa autentikasi SAH hanya selama ketiganya berlaku.
* **Asal asing DITOLAK 403, bukan cuma tidak diberi header CORS**, dan `POST`
  menuntut `Content-Type: application/json` supaya peramban wajib preflight
  lebih dulu. Keduanya temuan tinjauan keamanan otomatis, dan keduanya CSRF:
  tanpa header balasan halaman asing memang tidak bisa MEMBACA jawabannya, tapi
  permintaannya tetap sampai dan efek sampingnya tetap terjadi.
* **Penjagaan HTTP diuji lewat `node:http` MENTAH, bukan `fetch`.** undici
  MELARANG menyetel header `Host` dan mengabaikannya tanpa suara, jadi seluruh
  uji DNS rebinding lewat `fetch` akan "lulus" dengan Host yang benar --
  membuktikan nol. `Connection: close` ikut dipasang karena keep-alive membuat
  `srv.close()` menunggu selamanya, dan gejalanya uji yang mencetak "lulus"
  lalu menggantung.
* **CORS daftar putih, bukan `*`.** Hanya asal loopback. `*` di layanan yang
  membacakan catatan pribadi berarti halaman mana pun di internet yang dibuka
  di peramban ini bisa membacanya -- bind loopback tidak menolong, karena yang
  memanggil justru peramban milik pemiliknya.
* **`default_language: "none"`** di indeks teksnya: MongoDB tidak punya stemmer
  Indonesia, dan `"english"` memotong yang bukan akhiran ("sedang" kehilangan
  "ing"-nya). Harganya pencarian per kata utuh, dan itu jujur.
* **Penyelarasan dipicu `mtimeMs`.** Indeks yang ditulis ulang pada setiap
  huruf adalah indeks yang suatu hari ditulis ulang saat seseorang sedang
  membacanya.
* **Database uji `belajar_uji`**, bukan `belajar`.

Ujinya ikut suite lewat `test_konten_json.TestAlgoritmaTypeScript.
test_layanan_catatan`: dua belas pemeriksaan (lima lapisan murni, tujuh
penjagaan HTTP) SELALU jalan, tujuh lapisan Mongo MELEWATI diri sendiri kalau
containernya mati -- dengan pesan
yang menyebut perintah penyalaannya, jadi "dilewati" tidak pernah berarti
"lulus diam-diam". Lima dari enam mutan memerah; yang keenam batasnya diukur
dan ditulis (urutan `find()` tanpa `sort` implementation-defined di MongoDB,
terukur kedua arah).

**Tes kontrak 41 endpoint SUDAH ADA** (`tests/test_kontrak.py`). Yang
ditagihnya BENTUK jawaban -- nama medan dan tipenya -- bukan nilainya:
`{"xp": 7}` dan `{"xp": 1200}` sama-sama sah, `{"xp": "7"}` tidak. Empat hal
yang membuatnya pagar:

* **Daftar endpointnya diturunkan dari `server.RUTE`, tidak diketik.** Endpoint
  baru tanpa entri kontrak MERAH dengan menyebut jalurnya, dan jumlahnya (41)
  ditagih terpisah supaya pertumbuhannya terlihat di riwayat.
* **Kontraknya disusun dari jawaban server SUNGGUHAN**, bukan dari ingatan.
  Versi pertamanya ditulis dari dugaan dan sembilan entri langsung memerah:
  `/api/kuis/mulai` memakai medan `sesi` (bukan `token`) dan mengirim SELURUH
  soal sekaligus dengan medan `options` (satu-satunya nama Inggris di muatan
  kuis), `/api/konfigurasi` menerima `{<kunci>: <nilai>}` langsung,
  `/api/data/impor` menuntut `{"progres": ...}`, `/api/latihan/manual`
  menaburkan hadiahnya di tingkat atas sementara `/api/latihan/periksa`
  membungkusnya di `hadiah`, bagian materi punya DUA bentuk (prosa ber-`blok`,
  kode ber-`kode`/`token`/`sorot`), dan `terkunci` di hasil `/api/cari` cuma
  ada untuk tipe materi.
* **Argumen yang butuh id nyata DICARI lewat API-nya sendiri**: materi mana
  yang punya blok kode, latihan mana yang tidak bisa dinilai otomatis, contoh
  mana yang layak ditebak (dan satu materi dibaca TUNTAS lebih dulu, karena
  `pelajar/tebak.py` cuma menawarkan contoh dari materi yang selesai -- tanpa
  itu `/api/tebak` dilewati tanpa pernah diperiksa).
* **Ia bisa diarahkan ke implementasi LAIN** lewat `BELAJAR_KONTRAK_URL` +
  `BELAJAR_KONTRAK_TOKEN`, dan itu seluruh gunanya untuk Tahap 2: endpoint yang
  dipindahkan ke Express bisa diadu dengan kontrak yang sama, satu per satu,
  sementara sisanya tetap dilayani Python.

Lima mutan membuktikan ia bisa merah: medan yang diganti nama, angka yang jadi
string, daftar yang jadi objek, rute yang dihapus, dan rute baru tanpa kontrak.
`/api/data/impor` dan `/api/data/reset` dijalankan PALING AKHIR (`_urut()`):
keduanya mengganti seluruh progres yang dibaca endpoint lain, dan tanpa
pengurutan itu hasilnya bergantung pada urutan iterasi dict.

**Tiga cacat ikut ketemu di JALUR YANG SUDAH ADA selama ronde ini, dan
ketiganya tidak menimbulkan satu pun error:**

* **`--panas` tidak pernah terpasang di antarmuka LAMA.** `h()` menyalin medan
  `gaya` dengan `Object.assign(el.style, v)`, dan `Object.assign` ke `style`
  diam-diam membuang properti kustom `--*`. Jebakan itu sudah ditulis di
  komentar `petakPekan()` -- yang karena itu memakai `setProperty` -- tapi
  `cincinLevel()` masih memakai `gaya:`. Akibatnya pendar `.cincin::after`
  menghitung `calc(var(--panas, 0) * 22%)` dengan cadangan nol, jadi "makin
  dekat target, makin terang" punya alfa NOL selamanya. Sudah dibetulkan
  (net-zero baris). Satu-satunya tempat `gaya: { "--` di seluruh
  `webapp/statik/js`, jadi tidak ada korban kedua -- tapi pola itu TETAP
  berbahaya: properti kustom baru WAJIB lewat `setProperty`.
* **Kelas ukuran layar dipasang di `#panggung`, bukan `#layar`.** `gaya.css`
  menulis selektornya `#layar.lebar`/`.kolom`/`.penuh`; cangkang React memasang
  dua yang pertama di `#panggung` sejak 3aef198. Diukur pada jendela 1920 px:
  halaman daftar 1240 lawan 1400 yang benar, dan ketiga layar lebar yang
  seluruh gunanya `max-width: none` juga terjepit di 1240.
* **`komponen/Tanda.tsx` tidak pernah disambungkan.** Tombol bookmark dan
  catatan ditulis tapi tidak dipakai satu layar pun, jadi di React tidak ada
  cara menandai apa pun -- dan layar Bookmark serta Catatanku akan selamanya
  kosong tanpa penjelasan. Ikut ketemu: medan `catatan` ditipekan `string` di
  `DataMateri` dan `DataLatihan` padahal servernya mengirim `{teks, diubah}`.

* **`KuisLemah` ditipekan dengan TIGA nama medan yang tidak ada**
  (`key`, `skor`, `maks`; yang benar `bahasa`/`indeks`/`terbaik`/`total`).
  `tsc` tidak bisa menangkapnya -- tipe yang salah tetap tipe yang sah -- dan
  yang digambar di layar Statistik: pil bertuliskan `undefined/undefined`,
  tautan ke `#/kuis/undefined`, dan kunci kurikulum mentah ("python") di tempat
  labelnya. Nol galat di konsol. Blok itu juga kehilangan baris rinciannya dan
  bilah skornya, dan labelnya memakai "Di mana aku lemah?" -- nama fitur di
  DOCSTRING `blokKuisLemah`, bukan teks yang digambar ("Paling perlu diulang").

Pelajarannya satu dan berlaku ke depan: **`tsc` hijau dan curl hijau tidak
membuktikan sebuah layar terpasang.** Keempat cacat di atas lolos keduanya, dan
yang menemukan semuanya mengukur halaman yang sama di KEDUA antarmuka lalu
mengadu angkanya.

**Dua sapuan yang murah dan terbukti berguna, ulangi keduanya tiap kali sebuah
layar diport:**

1. **Adu kamus ukuran di kedua antarmuka**, per kunci, dengan
   `JSON.stringify`: lebar `#layar`, `gridTemplateColumns`, cacah
   `.baris`/`.kartu`/`.pil`/`.tbl`/`.bilah`/`svg`, teks `.mata` dan `aria-label`.
   Selisih yang keluar ada dua macam dan KEDUANYA berguna: yang salah, dan
   yang benar karena sesuatu memang sengaja belum diport. Yang kedua wajib bisa
   disebut alasannya -- sampul membuat `svg` dan tinggi halaman berbeda, blok
   data Statistik membuat `tbl` 0 lawan 4. Yang tidak bisa disebut alasannya
   adalah cacat.
2. **Sapu teks tiap layar untuk `undefined`, `NaN`, `[object Object]`, dan
   `null`.** Diukur atas 16 alamat: lima belas bersih, dan satu-satunya
   kecocokan sisa positif-palsu (teks kurikulumnya sendiri menyebut "null
   pointer"). Dua jebakan saat menulis sapuannya: regex ber-`/g/` yang dipakai
   ulang dengan `.test()` MAJU `lastIndex`-nya, jadi satu objek regex untuk
   banyak simpul melewatkan separuhnya dan melapor "tidak ketemu di mana pun"
   padahal ada; dan simpul yang punya anak harus dilewati, kalau tidak setiap
   leluhur ikut terdaftar.

**Empat catatan bentuk dari layar yang sudah diport.** Keempatnya berlaku
untuk sisanya:

* **Apa pun yang di versi JS di-toggle lewat `classList` jadi TURUNAN state**,
  bukan efek. Versi imperatif harus ingat membersihkan kelas yang dipasang
  sebelumnya; di `layar-langit` ada empat kelas semacam itu, dan satu cabang
  yang lupa membersihkannya meninggalkan bintang menyala untuk konsep yang
  sudah tidak dipilih -- tanpa satu pun error.
* **Pengukuran DOM dua-lintasan memang bentuk alami React.** `layar-karier`
  mengukur lebar label dengan `getComputedTextLength` lalu merutekan garis dari
  ujungnya; versi JS menggambar dengan perkiraan, menandainya, lalu menggambar
  ulang lewat `saatSiap`. Di React: render pertama perkiraan, `useEffect`
  mengukur, render kedua memakainya. Tidak ada penanda yang perlu diingat.
* **Yang BELUM diport dikatakan di layar**, lewat komponen `Keadaan`, bukan
  dihilangkan diam-diam. Blok data di Statistik dan Pengaturan, plus suara,
  getar, dan istirahat mata. Tombol yang hilang tanpa penjelasan membuat orang
  mengira fiturnya dibuang. **Reset progres tidak akan dipasang tanpa dialog
  konfirmasinya**: ia menghapus catatan belajar sungguhan.
* **Setiap `useEffect` yang memanggil API punya penanda `dibatalkan`.**
  Berpindah layar sebelum permintaan pertama selesai akan membuat jawaban LAMA
  tiba belakangan dan menimpa yang baru; yang terlihat isi dari layar yang
  sudah ditinggalkan. `layar-karier` perlu lebih dari itu -- perencana jalurnya
  menomori permintaan, karena mengubah asal dua kali cepat bisa menampilkan
  jalur permintaan PERTAMA. Satu keputusan yang mengikat: **runner JANGAN diport ke Node.**
`inti/runner.py` + `struktur.py` + `jejak.py` adalah satu sidecar Python.
Diuji di mesin ini: `ulimit -v` merusak JVM ("Could not reserve enough space
for object heap"), dan `bash -c` memakai string shell sementara
`runner.py` menurunkan nama kelas Java DARI KODE PELAJAR -- itu menukar pagar
yang ada dengan lubang injeksi.

## Cutover: React dilayani server Python (2026-10-26)

`belajar-web.py` sekarang melayani bundel React di `/`. Antarmuka lama TETAP
ada di `/lama`.

**Cutover-nya BERSYARAT, dan itu tunduk pada janji paling dasar repo ini.**
`webapp/server.py` memeriksa `dist_siap()` per permintaan: kalau
`packages/web/dist/index.html` ada, itu yang dilayani; kalau tidak, `/` jatuh
ke antarmuka lama. Server yang MENUNTUT direktori itu akan membuat kloning
segar tidak punya aplikasi sama sekali sampai npm dijalankan, sementara
AGENTS ini berjanji "Python 3.8+ dan stdlib saja". Jadi:

```bash
npm install && npm run build --workspace @belajar/web   # sekali
python3 belajar-web.py                                  # React di /
```

Tanpa dua perintah pertama, aplikasinya tetap utuh -- cuma antarmuka lama.
`dist/` ada di `.gitignore`: ia produk, bukan sumber.

Yang mengikat:

* **Token disuntik server, bukan dipanggang ke bundel.** Ia lahir per JALANNYA
  server. `packages/web/index.html` memuat
  `window.TOKEN_BELAJAR = window.TOKEN_BELAJAR || "__TOKEN_BELAJAR__"`, dan
  `server._halaman()` mengganti sentinel itu seperti ia mengganti `{{TOKEN}}`
  di halaman lama. **`|| ` itu WAJIB**: di mode dev plugin `belajar-token`
  menyuntikkan token sungguhan lewat `head-prepend` sehingga ia jalan LEBIH
  DULU, dan tanpa `||` baris ini menimpanya dengan sentinel -- yang oleh
  `api.ts` dibaca sebagai "tidak ada token", jadi seluruh API menjawab 403.
  Sentinelnya tidak boleh berbentuk `{{...}}`: ia harus tetap JavaScript yang
  sah supaya `vite build` bisa mengurainya.
* **Berkas statik punya DUA akar, dan traversal diperiksa PER AKAR.**
  `webapp/statik` lebih dulu (`gaya.css`, `/huruf`, `/vendor` tetap satu
  sumber), lalu `dist` untuk `/assets/*`. Satu pemeriksaan untuk dua akar
  adalah pemeriksaan yang salah untuk salah satunya.
* **Ketiga lapis penjagaan TIDAK disentuh.** Diukur sesudah cutover: `/api`
  tanpa token 403, Origin asing 403, Host asing 403, traversal 403.
* **`/lama` wajib tetap bisa dibuka.** 379 tes di `tests/test_web.py` menguji
  halaman itu; permukaan yang tidak bisa dibuka lagi adalah permukaan yang
  pagarnya berhenti berarti.

Pagarnya `test_web.TestBundelReactDilayani` (4 tes). Satu pelajaran dari
mengukurnya: tes traversal versi pertama menerima **403 ATAU 404** dengan
jalur `../` yang terlalu pendek untuk keluar dari pohon -- yang menolaknya
"berkas tidak ada", bukan pemeriksaannya, dan sel yang MENCABUT pemeriksaan
itu tetap hijau. Sekarang ia menagih 403 dengan `../` yang benar-benar
mendarat di `/etc/passwd`, dan selnya merah dengan pesan "traversal TERBUKA".

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
3. Tambah satu entri di `LANGUAGES` (`inti/kurikulum.py`).
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
