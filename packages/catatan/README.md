# `@belajar/catatan` — pencarian catatan (Express + MongoDB)

Layanan **tambahan**, bukan pengganti. Aplikasi belajar-codingV2 jalan penuh
tanpa paket ini: catatan tetap ditulis, dibaca, dan didaftar oleh server Python
dari berkas JSON-nya sendiri. Yang ditambahkan satu kemampuan yang versi JSON
memang tidak punya — **pencarian teks berperingkat di dalam isi catatan**.

Ia juga alasan huruf **M** dan **E** di MERN benar-benar dipakai, bukan
didemokan.

## Menjalankan

```bash
# sekali, pertama kali
podman run -d --name belajar-mongo \
  -p 127.0.0.1:27017:27017 -v belajar-mongo:/data/db docker.io/library/mongo:8

# selanjutnya
podman start belajar-mongo
npm run mulai --workspace @belajar/catatan     # http://127.0.0.1:7799
```

Kotak pencarian muncul sendiri di layar **Catatanku**. Kalau layanannya tidak
jalan, layar itu mengatakannya beserta kedua perintah di atas — catatannya
tetap tampil lengkap.

```bash
npm run uji   --workspace @belajar/catatan   # 19 pemeriksaan; 12 tanpa Mongo
npm run tipe  --workspace @belajar/catatan
```

## Yang mengikat

**Berkas JSON tetap SUMBER KEBENARAN; MongoDB cuma INDEKS.** Arah datanya
satu: `~/.belajar_ngoding_catatan.json` → Mongo. Tidak ada jalur sebaliknya,
dan tidak ada satu pun jalur tulis ke berkas itu di paket ini.

Alasannya bukan kehati-hatian abstrak. Catatan adalah tulisan tangan orang, dan
pengaman yang melindunginya — karantina berkas rusak, `.bak` bergulir, tulis
atomik — hidup di `pelajar/simpanan.py`. Tidak satu pun dari itu ada di sebuah
container yang bisa dibuang dengan satu perintah. Konsekuensinya: Mongo yang
kosong atau mati tidak pernah berarti catatan yang hilang, ia cuma berarti
pencarian yang tidak tersedia.

**Progres pelajar tidak pernah menyentuh Mongo.** Untuk 899 byte progres satu
pengguna, Mongo tidak memberi keuntungan teknis apa pun — dan menaruhnya di
sana berarti melepas tiga pengaman yang lahir dari audit nyata (XP 500 jadi 10,
materi hilang, tanpa cadangan).

**`Host` diperiksa, bukan cuma `Origin`.** Keduanya menutup lubang yang
BERBEDA. DNS rebinding membelokkan nama domain penyerang ke `127.0.0.1`;
peramban lalu menganggap permintaannya same-origin, jadi `Origin` tidak
dikirim sama sekali — dan pemeriksaan asal yang cuma berlaku "kalau ada
Origin" melewatkannya tanpa suara. Yang membedakannya `Host`: permintaan yang
dibelokkan tetap membawa nama domain penyerang di situ. Bentuknya sama dengan
`server._asal_sah()` di sisi Python, termasuk membolehkan `Host` KOSONG
(HTTP/1.0 dan `curl --http1.0` tidak mengirimnya).

**Asal asing DITOLAK 403, bukan cuma tidak diberi header CORS.** Bedanya nyata
dan ia CSRF: tanpa header balasan, halaman asing memang tidak bisa MEMBACA
jawabannya — tapi permintaannya tetap sampai dan efek sampingnya tetap terjadi.
`POST` juga menuntut `Content-Type: application/json`, content-type yang bukan
"simple request", jadi peramban wajib preflight lebih dulu dan formulir HTML
lintas-asal — satu-satunya POST tanpa preflight — tidak bisa mengirimnya.

Ketujuh penjagaan itu diuji TANPA container: ketiganya menolak sebelum satu pun
panggilan Mongo, dan penjagaan keamanan yang cuma teruji saat sebuah container
menyala adalah penjagaan yang diam-diam berhenti teruji. Permintaannya lewat
`node:http` mentah, bukan `fetch`: undici MELARANG menyetel header `Host` dan
mengabaikannya tanpa suara, jadi seluruh uji DNS rebinding lewat `fetch` akan
"lulus" dengan Host yang benar — membuktikan nol.

**Bind loopback, dan Mongo tanpa autentikasi punya syaratnya.** Container-nya
dijalankan `-p 127.0.0.1:27017:27017`; `HOST` di `src/indeks.ts` konstanta
`"127.0.0.1"` dan sengaja TIDAK dibaca dari lingkungan — variabel yang bisa
menaikkannya ke `0.0.0.0` adalah pagar yang bisa dilepas tanpa menyentuh satu
baris kode, dan pagar seperti itu selalu dilepas "sebentar saja" lebih dulu.
Kalau bind-nya benar-benar perlu diubah, autentikasi Mongo wajib ditambahkan di
saat yang sama.

**CORS-nya daftar putih, bukan `*`.** Hanya asal `http`/`https` di `127.0.0.1`,
`[::1]`, atau `localhost`. `Access-Control-Allow-Origin: *` di layanan yang
membacakan isi catatan pribadi berarti halaman mana pun di internet yang dibuka
di peramban ini bisa membacanya — bind loopback tidak menolong sama sekali,
karena yang memanggil justru peramban milik pemiliknya.

**`default_language: "none"` di indeks teksnya.** MongoDB punya stemmer untuk
lima belas bahasa dan Indonesia bukan salah satunya. `"english"` akan memotong
yang bukan akhiran ("sedang" kehilangan "ing"-nya) dan membuang kata Inggris
yang di sini justru istilah teknis. `"none"` berarti pencarian per kata utuh:
"pointer" menemukan "pointer" tapi tidak "pointers". Itu harga yang dibayar,
dan ia jujur — berbeda dengan stemming yang salah, yang gagal tanpa memberi
tahu kenapa.

**Penyelarasan dipicu `mtimeMs`, bukan tiap permintaan.** Satu `stat()` jauh
lebih murah daripada `bulkWrite` seratus dokumen, dan yang dicegah bukan ongkos
CPU-nya melainkan kelasnya: indeks yang ditulis ulang pada setiap huruf adalah
indeks yang suatu hari ditulis ulang saat seseorang sedang membacanya.

**Satu pemeriksaan yang batasnya diukur dan ditulis.** Mencabut
`.sort({ skor: { $meta: "textScore" } })` dari `cari()` tidak selalu
memerahkan ujinya: urutan `find()` tanpa `sort` adalah urutan pemindaian
indeks, dan itu implementation-defined di MongoDB — terukur KEDUA arah dengan
korpus yang sama persis, di dua nama database yang berbeda. Yang dijaga uji itu
karena itu relevansinya (dua dokumen cocok, skornya berbeda, yang menyebut
kedua kata berskor lebih tinggi), bukan kehadiran `.sort()`. Lima mutan lain di
paket ini memang memerah; alasannya ditulis di `uji/uji-cari.ts`.

**Database uji `belajar_uji`, bukan `belajar`.** Tanpa pemisahan itu,
menjalankan ujinya membuang indeks catatan sungguhan dan menggantinya dengan
tiga catatan karangan — dan karena Mongo di sini cuma indeks, yang terlihat
bukan kehilangan data melainkan pencarian yang mendadak bohong.

## Endpoint

| Metode | Jalur | Jawaban |
|---|---|---|
| GET | `/sehat` | `{sehat, berkas, catatan, selaras?}`. **200 walau Mongo mati** — pertanyaannya "apa keadaanmu", dan "Mongo mati" adalah jawaban yang BERHASIL |
| GET | `/cari?q=…` | `{kata, hasil: [{kunci, teks, diubah, skor}]}`, paling relevan dulu. 400 di bawah 2 huruf, 503 kalau Mongo mati |
| POST | `/selaras` | Paksa penyelarasan: `{masuk, dibuang, total}` |
