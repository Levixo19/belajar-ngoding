"""Kurikulum Game & Grafis.

Dirakit alat/rakit_kurikulum.py dari draf per bab (2026-10-19).
Sesudah dirakit, berkas ini disunting seperti kurikulum lain
(alat/ganti_badan.py, alat/tambah_bagian.py). <KEY>_BAB tetap
spesifikasi JUMLAH; rentangnya dihitung data/kurikulum_tech.py.
"""

GAME_BAB = [
    {
        "judul": "Cara Game Bekerja",
        "ket": "Game loop, waktu, input, dan state game.",
        "tingkat": "dasar",
        "jumlah": 3,
    },
    {
        "judul": "Matematika Game 2D",
        "ket": "Vektor, tabrakan, dan transformasi untuk game 2D.",
        "tingkat": "dasar",
        "jumlah": 3,
    },
    {
        "judul": "Game 2D di Browser",
        "ket": "Phaser, tilemap, kamera, dan state machine karakter.",
        "tingkat": "dasar",
        "jumlah": 3,
    },
    {
        "judul": "Godot Engine",
        "ket": "Engine open source dengan pohon node dan GDScript.",
        "tingkat": "menengah",
        "jumlah": 2,
    },
    {
        "judul": "Unity",
        "ket": "GameObject, komponen, fisika, dan build ke banyak platform.",
        "tingkat": "menengah",
        "jumlah": 3,
    },
    {
        "judul": "AI Game dan Pathfinding",
        "ket": "Mencari jalan di grid dan perilaku musuh.",
        "tingkat": "menengah",
        "jumlah": 2,
    },
    {
        "judul": "Engine Lain dan Menerbitkan Game",
        "ket": "Unreal, peta engine lain, itch.io, dan Steam.",
        "tingkat": "menengah",
        "jumlah": 3,
    },
    {
        "judul": "Grafis Komputer dan API GPU",
        "ket": "Dari segitiga ke piksel, shader, dan API GPU.",
        "tingkat": "mahir",
        "jumlah": 5,
    },
    {
        "judul": "ECS dan Simulasi Deterministik",
        "ket": "Arsitektur data-driven, replay, dan dasar netcode.",
        "tingkat": "mahir",
        "jumlah": 2,
    },
    {
        "judul": "AR, VR, dan XR",
        "ket": "Matematika AR, platform AR, headset VR, dan XR di web.",
        "tingkat": "mahir",
        "jumlah": 4,
    },
]

GAME_MATERIALS = [
    {
        "title": "1. Game Loop, Frame, dan Delta Time",
        "sections": [
            {
                "body": [
                    "Program yang kamu tulis selama ini biasanya jalan dari atas ke",
                    "bawah, lalu selesai. Atau dia berhenti dan nunggu kamu mengetik",
                    "sesuatu. Game nggak bisa begitu. Waktu kamu diam aja, musuh tetap",
                    "jalan, awan tetap bergeser, dan jam di pojok layar tetap menghitung",
                    "mundur.",
                    "",
                    "Caranya, game menggambar ulang seluruh layar berkali-kali dalam",
                    "satu detik. Satu gambar utuh itu disebut frame. Jumlah frame per",
                    "detik disebut FPS (frames per second). Game yang jalan di 60 FPS",
                    "menggambar 60 frame tiap detik, jadi satu frame cuma punya waktu",
                    "sekitar 16,7 milidetik.",
                    "",
                    "Mirip buku bergambar yang halamannya dibalik cepat. Tiap halaman",
                    "diam, tapi karena gantinya cepat, mata kita melihat gerakan.",
                ],
            },
            {
                "heading": "Tiga langkah yang diulang terus",
                "body": [
                    "Setiap frame, game mengerjakan tiga hal yang sama dengan urutan",
                    "yang sama:",
                    "  1. Input. Baca keadaan papan ketik, mouse, layar sentuh, atau",
                    "     gamepad.",
                    "  2. Update. Hitung keadaan dunia yang baru: pemain pindah, peluru",
                    "     terbang, nyawa berkurang kalau kena tabrakan.",
                    "  3. Render. Gambar keadaan baru itu ke layar.",
                    "",
                    "Sesudah render, game balik lagi ke input. Putaran tanpa akhir ini",
                    "disebut game loop. Semua game punya game loop, dari game ular di",
                    "ponsel jadul sampai game 3D besar. Bedanya cuma seberapa banyak",
                    "yang dikerjakan di tiap langkah.",
                    "",
                    "Update dan render sengaja dipisah. Update cuma mengubah angka",
                    "(posisi, kecepatan, nyawa), dan render cuma membaca angka itu lalu",
                    "menggambarnya. Dengan begitu, logika game bisa diuji tanpa layar",
                    "sama sekali. Semua latihan di kurikulum ini memakai cara itu.",
                ],
            },
            {
                "heading": "Kalau gerak dihitung per frame",
                "body": [
                    "Cara paling gampang menggerakkan sesuatu: tiap frame, tambah",
                    "posisinya dengan angka tetap. Kode di bawah menghitung posisi",
                    "karakter selama satu detik di dua layar yang kecepatannya beda.",
                    "Nggak ada yang digambar, cuma angkanya yang dihitung.",
                ],
                "code": """// Gerak "per frame": tiap frame maju 3 piksel.
function jalankan(fps) {
  let x = 0;
  for (let frame = 0; frame < fps; frame++) { // 1 detik = fps frame
    x += 3;
  }
  return x;
}

console.log('60 FPS :', jalankan(60), 'piksel dalam 1 detik');
console.log('144 FPS:', jalankan(144), 'piksel dalam 1 detik');""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  60 FPS : 180 piksel dalam 1 detik",
                    "  144 FPS: 432 piksel dalam 1 detik",
                    "",
                    "Layar 60 Hz menggambar 60 frame per detik. Layar 144 Hz, yang",
                    "banyak dipakai laptop gaming, menggambar 144 frame. Kalau tiap",
                    "frame maju 3 piksel, karakter di layar 144 Hz jalan 2,4 kali lebih",
                    "cepat. Game yang sama jadi lebih susah di satu komputer dan lebih",
                    "gampang di komputer lain.",
                ],
            },
            {
                "heading": "Delta time: kalikan dengan lamanya frame",
                "body": [
                    "Jalan keluarnya, tulis kecepatan dalam piksel per detik. Lalu di",
                    "tiap frame, kalikan kecepatan itu dengan lamanya frame tadi. Lama",
                    "satu frame ini disebut delta time, biasanya ditulis dt.",
                    "",
                    "Rumusnya: posisi baru = posisi lama + kecepatan × dt. Kalau",
                    "frame-nya pendek, langkahnya kecil. Kalau frame-nya panjang,",
                    "langkahnya besar. Totalnya per detik tetap sama.",
                ],
                "code": """const KECEPATAN = 180; // piksel per detik

function jalankan(fps) {
  const dt = 1 / fps; // lama satu frame, dalam detik
  let x = 0;
  for (let frame = 0; frame < fps; frame++) {
    x += KECEPATAN * dt;
  }
  return x;
}

console.log('30 FPS :', jalankan(30).toFixed(2), 'piksel');
console.log('60 FPS :', jalankan(60).toFixed(2), 'piksel');
console.log('144 FPS:', jalankan(144).toFixed(2), 'piksel');""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  30 FPS : 180.00 piksel",
                    "  60 FPS : 180.00 piksel",
                    "  144 FPS: 180.00 piksel",
                    "",
                    "Tiga-tiganya sampai di 180 piksel. toFixed(2) dipakai karena 1/144",
                    "nggak bisa disimpan persis sebagai bilangan pecahan di komputer,",
                    "jadi hasil mentahnya bisa meleset di digit yang jauh di belakang",
                    "koma.",
                ],
            },
            {
                "heading": "Di browser: requestAnimationFrame",
                "body": [
                    "Di browser, game loop dibangun dengan requestAnimationFrame.",
                    "Fungsi ini minta browser memanggil fungsimu tepat sebelum layar",
                    "digambar ulang. Seberapa sering? Mengikuti kecepatan layarnya:",
                    "biasanya 60 kali per detik, tapi bisa 75, 120, atau 144 di layar",
                    "yang lebih cepat.",
                    "",
                    "Fungsimu dikasih satu angka, yaitu waktu dalam milidetik. Selisih",
                    "waktu sekarang dengan waktu frame sebelumnya, itu dt-nya. Simpan",
                    "halaman di bawah sebagai berkas .html, lalu buka di browser.",
                ],
                "bahasa": "html",
                "code": """<!doctype html>
<html lang="id">
<head>
  <meta charset="utf-8">
  <title>Game loop pertama</title>
</head>
<body>
  <canvas id="layar" width="320" height="120"></canvas>
  <script>
    const kanvas = document.getElementById('layar');
    const ctx = kanvas.getContext('2d');
    const KECEPATAN = 120; // piksel per detik
    let x = 0;
    let waktuLalu = null;

    function frame(waktu) {
      if (waktuLalu === null) waktuLalu = waktu;
      const dt = Math.min((waktu - waktuLalu) / 1000, 0.1);
      waktuLalu = waktu;

      // update: hitung posisi baru
      x = (x + KECEPATAN * dt) % kanvas.width;

      // render: gambar ulang seluruh layar
      ctx.fillStyle = '#10141f';
      ctx.fillRect(0, 0, kanvas.width, kanvas.height);
      ctx.fillStyle = '#f5c542';
      ctx.fillRect(x, 50, 20, 20);

      requestAnimationFrame(frame); // minta frame berikutnya
    }

    requestAnimationFrame(frame);
  </script>
</body>
</html>""",
            },
            {
                "body": [
                    "Tiga hal di kode itu yang sering terlewat:",
                    "  - Waktu dari browser dalam milidetik, jadi dibagi 1000 supaya jadi",
                    "    detik. Kecepatannya ditulis dalam piksel per detik, jadi",
                    "    satuannya harus sama.",
                    "  - Frame pertama belum punya waktu sebelumnya, jadi dt-nya 0.",
                    "  - Math.min(..., 0.1) membatasi dt paling besar 0,1 detik. Browser",
                    "    menghentikan requestAnimationFrame waktu tab-nya nggak",
                    "    kelihatan. Begitu kamu balik ke tab itu sesudah 30 detik, dt",
                    "    pertama bernilai 30 detik. Tanpa batas ini, kotaknya langsung",
                    "    loncat jauh.",
                    "",
                    "Engine game juga memberimu dt, cuma namanya dan satuannya beda:",
                    "",
                    "  engine   tempat dt-nya          satuan",
                    "  Phaser   update(time, delta)    milidetik",
                    "  Godot    _process(delta)        detik",
                    "  Unity    Time.deltaTime         detik",
                    "",
                    "Jebakan: kecepatan 200 dari tutorial Godot artinya 200 piksel per",
                    "detik. Kalau langsung dikali delta Phaser yang dalam milidetik,",
                    "gerakannya jadi seribu kali lebih cepat. Selalu cek satuannya.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Space Invaders (1978) punya contoh terkenal soal gerak per frame.",
                    "Makin banyak alien yang ditembak, makin cepat prosesor menggambar",
                    "sisanya. Karena posisi alien diperbarui tiap frame, mereka ikut",
                    "makin cepat. Pembuatnya, Tomohiro Nishikado, membiarkannya jadi",
                    "bagian permainan. Komputer PC lama sampai punya tombol Turbo:",
                    "mematikannya membuat prosesor lebih lambat, supaya game lama yang",
                    "mengandalkan kecepatan prosesor nggak jalan kelewat cepat.",
                    "",
                    "Kasus kecil: temanmu bikin game lari di browser dengan x += 4 di",
                    "tiap frame. Di laptopnya yang 60 Hz terasa pas. Di laptop gaming",
                    "144 Hz punyamu, karakternya ngebut dan rintangannya hampir mustahil",
                    "dilewati.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Cari baris update yang menambah posisi dengan angka tetap.",
                    "  2. Ubah angka itu jadi kecepatan per detik. 4 piksel per frame di",
                    "     60 FPS sama dengan 240 piksel per detik.",
                    "  3. Hitung dt dalam detik dari waktu yang dikasih",
                    "     requestAnimationFrame, lalu ganti baris tadi:",
                    "       x += 240 * dt;",
                    "  4. Batasi dt dengan Math.min(dt, 0.1) supaya pindah tab nggak",
                    "     bikin karakter loncat.",
                    "  5. Uji tanpa layar: jalankan update 60 kali dengan dt 1/60, lalu",
                    "     144 kali dengan dt 1/144. Dua-duanya harus berakhir di sekitar",
                    "     240 piksel.",
                ],
            },
        ],
    },
    {
        "title": "2. Fixed Timestep dan Jam Palsu",
        "sections": [
            {
                "heading": "Lompatan yang tingginya beda-beda",
                "body": [
                    "Delta time bikin gerak lurus jadi adil. Tapi begitu ada",
                    "gravitasi, lompatan, dan tabrakan, masalahnya muncul lagi. Kode di",
                    "bawah menghitung lompatan yang sama di tiga FPS. Rumusnya pakai",
                    "delta time, persis seperti materi sebelumnya.",
                ],
                "code": """// Lompatan: kecepatan awal 600 px/detik ke atas,
// gravitasi 1800 px/detik per detik.
function tinggiPuncak(fps) {
  const dt = 1 / fps;
  let y = 0;    // tinggi di atas tanah
  let vy = 600; // kecepatan ke atas
  let puncak = 0;
  while (y >= 0) {
    vy -= 1800 * dt;
    y += vy * dt;
    puncak = Math.max(puncak, y);
  }
  return puncak;
}

for (const fps of [30, 60, 144]) {
  console.log(`${fps} FPS: puncak ${tinggiPuncak(fps).toFixed(1)} px`);
}""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  30 FPS: puncak 90.0 px",
                    "  60 FPS: puncak 95.0 px",
                    "  144 FPS: puncak 97.9 px",
                    "",
                    "Kalau dihitung pakai rumus fisika, puncaknya 100 piksel. Nggak ada",
                    "satu pun yang tepat, dan makin rendah FPS-nya, makin rendah",
                    "lompatannya. Penyebabnya, kecepatan cuma diperbarui sekali tiap",
                    "frame. Di antara dua frame, game menganggap kecepatannya tetap,",
                    "padahal gravitasi terus bekerja. Makin panjang frame-nya, makin",
                    "besar selisihnya.",
                    "",
                    "Di game, akibatnya terasa: pemain dengan laptop lambat nggak bisa",
                    "mencapai pijakan yang bisa dicapai pemain lain. Frame yang panjang",
                    "sekali, misalnya waktu game tersendat, juga bisa membuat peluru",
                    "melompati dinding karena satu langkahnya terlalu jauh.",
                ],
            },
            {
                "heading": "Langkah tetap dan akumulator",
                "body": [
                    "Solusinya, fisika selalu maju dengan langkah yang sama panjangnya,",
                    "misalnya 10 milidetik, berapa pun FPS layarnya. Cara ini disebut",
                    "fixed timestep (langkah waktu tetap).",
                    "",
                    "Masalahnya, lama frame nggak pernah pas kelipatan 10 ms. Satu frame",
                    "bisa 25 ms, frame berikutnya 7 ms. Untuk itu dipakai akumulator.",
                    "Akumulator itu semacam celengan waktu:",
                    "  - Tiap frame, lama frame itu dimasukkan ke celengan.",
                    "  - Selama isinya masih cukup untuk satu langkah, jalankan satu",
                    "    langkah fisika dan ambil 10 ms dari celengan.",
                    "  - Sisa yang kurang dari 10 ms tetap disimpan untuk frame",
                    "    berikutnya. Nggak ada waktu yang dibuang.",
                    "",
                    "Di contoh ini lama frame diambil dari daftar tetap, supaya kamu",
                    "bisa menghitung sendiri hasilnya.",
                ],
                "code": """const LANGKAH = 10;  // satu langkah fisika = 10 ms
const KECEPATAN = 2; // piksel per langkah
const durasiFrame = [25, 7, 18, 40]; // lama tiap frame, dalam ms

let akumulator = 0;
let x = 0;

for (const durasi of durasiFrame) {
  akumulator += durasi;
  let langkah = 0;
  while (akumulator >= LANGKAH) {
    x += KECEPATAN; // satu langkah fisika
    akumulator -= LANGKAH;
    langkah++;
  }
  console.log(`frame ${durasi} ms: ${langkah} langkah, sisa ${akumulator} ms, x = ${x}`);
}""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  frame 25 ms: 2 langkah, sisa 5 ms, x = 4",
                    "  frame 7 ms: 1 langkah, sisa 2 ms, x = 6",
                    "  frame 18 ms: 2 langkah, sisa 0 ms, x = 10",
                    "  frame 40 ms: 4 langkah, sisa 0 ms, x = 18",
                    "",
                    "Frame 7 ms sendirian nggak cukup untuk satu langkah. Tapi ditambah",
                    "sisa 5 ms dari frame sebelumnya, isinya jadi 12 ms, cukup untuk",
                    "satu langkah. Frame 40 ms dapat empat langkah sekaligus.",
                    "",
                    "Loop-nya sengaja memakai while. Kalau diganti if, frame panjang cuma",
                    "dapat satu langkah, dan game jadi melambat waktu komputernya",
                    "lambat.",
                ],
            },
            {
                "heading": "Interpolasi dan batas langkah",
                "body": [
                    "Fisika sekarang maju dalam langkah 10 ms, tapi layar digambar",
                    "kapan pun browser mau. Kalau render cuma menggambar posisi dari",
                    "langkah terakhir, gerakannya kelihatan sedikit patah-patah.",
                    "",
                    "Perbaikannya, simpan posisi dari dua langkah terakhir, lalu gambar",
                    "objek di antara keduanya sesuai sisa akumulator:",
                    "",
                    "  alpha = akumulator / LANGKAH",
                    "  xGambar = xLama + (xBaru - xLama) * alpha",
                    "",
                    "Kalau sisanya 5 ms dari langkah 10 ms, alpha = 0,5, jadi objek",
                    "digambar tepat di tengah posisi lama dan posisi baru. Teknik ini",
                    "disebut interpolasi. Fisikanya nggak berubah sama sekali, yang",
                    "berubah cuma tempat objek digambar.",
                    "",
                    "Ada satu bahaya lagi. Kalau satu langkah fisika makan waktu lebih",
                    "lama dari 10 ms, tiap frame makin ketinggalan. Makin banyak",
                    "langkah yang harus dikejar, frame berikutnya makin lama lagi.",
                    "Lingkaran ini disebut spiral of death. Pencegahnya: batasi jumlah",
                    "langkah per frame, atau batasi lama frame yang boleh masuk ke",
                    "akumulator. Artikel \"Fix Your Timestep!\" karya Glenn Fiedler",
                    "(2004), rujukan klasik soal topik ini, memakai batas 0,25 detik.",
                ],
            },
            {
                "heading": "Jam palsu: waktu yang bisa diatur",
                "body": [
                    "Sekarang soal menguji game. Kalau loop-nya membaca Date.now() atau",
                    "performance.now(), angkanya beda tiap kali dijalankan, jadi hasil",
                    "akhirnya juga beda. Tes nggak bisa memutuskan hasil mana yang",
                    "benar.",
                    "",
                    "Caranya, simulasi nggak boleh membaca jam sendiri. Lama tiap frame",
                    "dikasih dari luar. Di browser, angkanya datang dari",
                    "requestAnimationFrame. Di tes, angkanya datang dari daftar tetap",
                    "yang kita tulis sendiri. Daftar itu disebut jam palsu, dan",
                    "simulasinya nggak tahu bedanya.",
                ],
                "code": """function simulasi(durasiFrame) {
  const LANGKAH = 10; // ms
  let akumulator = 0;
  let x = 0;
  let vx = 3;
  for (const durasi of durasiFrame) {
    akumulator += durasi;
    while (akumulator >= LANGKAH) {
      x += vx;
      if (x <= 0 || x >= 20) vx = -vx; // memantul di dua dinding
      akumulator -= LANGKAH;
    }
  }
  return x;
}

const rekaman = [16, 17, 16, 33, 16, 17, 50, 16]; // komputer cepat
const lambat = [45, 45, 45, 46];                  // komputer lambat

console.log('main pertama   :', simulasi(rekaman));
console.log('replay         :', simulasi(rekaman));
console.log('komputer lambat:', simulasi(lambat));""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  main pertama   : 12",
                    "  replay         : 12",
                    "  komputer lambat: 12",
                    "",
                    "Main pertama dan replay memakai rekaman yang sama, jadi hasilnya",
                    "sama. Komputer lambat punya frame yang lebih sedikit dan lebih",
                    "panjang, tapi totalnya sama-sama 181 ms. Dua-duanya menjalankan 18",
                    "langkah fisika yang persis sama, jadi x-nya juga sama. Delta time",
                    "biasa nggak bisa memberi jaminan ini.",
                    "",
                    "Sifat ini disebut deterministik: masukan yang sama selalu",
                    "menghasilkan keluaran yang sama. Banyak game strategi menyimpan",
                    "replay dengan cara ini. Yang disimpan cuma perintah pemain per",
                    "langkah, lalu simulasinya diputar ulang. Bab ECS dan Simulasi",
                    "Deterministik nanti membahasnya lebih jauh.",
                ],
            },
            {
                "heading": "Engine sudah menyediakannya",
                "body": [
                    "Kalau memakai engine, kamu jarang menulis akumulator sendiri.",
                    "Godot menjalankan _physics_process 60 kali per detik secara",
                    "bawaan, dan paling banyak 8 langkah fisika per frame supaya nggak",
                    "masuk spiral of death (dokumentasi Godot 4.7). Unity punya",
                    "FixedUpdate dengan langkah yang diatur di Project Settings. Fisika",
                    "arcade di Phaser juga jalan dengan langkah tetap, 60 kali per",
                    "detik secara bawaan.",
                    "",
                    "Cara kerjanya tetap perlu kamu pahami. Kalau gerak di _process dan",
                    "di _physics_process kelihatan beda, atau input kadang nggak",
                    "terbaca, penyebabnya hampir selalu ada di hubungan antara frame",
                    "layar dan langkah fisika.",
                    "",
                    "Jebakan: tombol yang baru ditekan bisa hilang. Di frame 7 ms tadi",
                    "bisa saja nggak ada langkah fisika sama sekali. Kalau tanda \"baru",
                    "ditekan\" cuma berlaku di frame itu, langkah berikutnya nggak",
                    "pernah melihatnya. Simpan tandanya sampai satu langkah memakainya.",
                    "",
                    "Jebakan: jangan mengosongkan akumulator jadi 0 sesudah loop. Sisa",
                    "waktunya ikut terbuang, dan game pelan-pelan tertinggal dari jam",
                    "dinding.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Godot, Unity, dan fisika arcade Phaser semuanya memisahkan langkah",
                    "fisika dari frame layar dengan cara di atas. Selama gerak fisika",
                    "ditulis di langkah fisika (misalnya _physics_process di Godot),",
                    "lompatan tetap sama tingginya di monitor 60 Hz maupun 144 Hz.",
                    "",
                    "Kasus kecil: di game platformer buatanmu, penguji yang laptopnya",
                    "lambat melapor nggak bisa naik ke pijakan terakhir. Di komputermu",
                    "bisa.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Ulangi masalahnya tanpa layar. Panggil fungsi lompat dengan",
                    "     jam palsu dt 1/30 dan dt 1/144, lalu cetak puncaknya.",
                    "  2. Pindahkan semua perubahan kecepatan dan posisi ke satu fungsi",
                    "     langkah(dt) yang selalu dipanggil dengan dt yang sama,",
                    "     misalnya 1/60 detik.",
                    "  3. Di game loop, isi akumulator dengan lama frame dan panggil",
                    "     langkah() selama isinya cukup:",
                    "       akumulator += dt;",
                    "       while (akumulator >= 1 / 60) {",
                    "         langkah(1 / 60);",
                    "         akumulator -= 1 / 60;",
                    "       }",
                    "  4. Batasi lama frame yang masuk, misalnya paling besar 0,25",
                    "     detik.",
                    "  5. Jalankan lagi tes di langkah 1. Kedua jam palsu sekarang harus",
                    "     memberi puncak yang sama.",
                ],
            },
        ],
    },
    {
        "title": "3. Input, Event, dan State Game",
        "sections": [
            {
                "body": [
                    "Ada dua cara mengetahui tombol apa yang ditekan pemain. Bedanya",
                    "kecil di kode, tapi akibatnya besar di permainan.",
                    "  - Event. Browser memanggil fungsimu tepat saat sesuatu terjadi:",
                    "    keydown waktu tombol turun, keyup waktu tombol naik.",
                    "  - Keadaan. Di tiap frame, game bertanya sendiri: tombol ini",
                    "    sedang ditekan atau nggak?",
                    "",
                    "Event mirip notifikasi di ponsel, datang sekali waktu ada",
                    "kejadian. Keadaan mirip melihat lampu kamar: kamu cek kapan pun",
                    "kamu mau, dan jawabannya selalu kondisi saat itu.",
                    "",
                    "Untuk menggerakkan karakter, game butuh keadaan. Kalau karakter",
                    "digerakkan langsung di dalam keydown, gerakannya tersendat. Waktu",
                    "tombol ditahan, keydown pertama datang sekali, lalu ada jeda, baru",
                    "keydown berikutnya datang berulang-ulang dengan event.repeat",
                    "bernilai true. Panjang jedanya diatur sistem operasi, jadi game-mu",
                    "nggak bisa mengendalikannya.",
                ],
            },
            {
                "heading": "Mengubah event jadi keadaan",
                "bahasa": "browser",
                "code": """const pemain = { x: 100 };
const ditekan = new Set();

window.addEventListener('keydown', (e) => {
  ditekan.add(e.code);
});
window.addEventListener('keyup', (e) => {
  ditekan.delete(e.code);
});
// Jendela kehilangan fokus: keyup nggak akan datang, jadi kosongkan.
window.addEventListener('blur', () => ditekan.clear());

function update(dt) {
  if (ditekan.has('KeyA') || ditekan.has('ArrowLeft')) pemain.x -= 200 * dt;
  if (ditekan.has('KeyD') || ditekan.has('ArrowRight')) pemain.x += 200 * dt;
}""",
            },
            {
                "body": [
                    "Event cuma dipakai untuk mencatat. Keputusan gerak diambil di",
                    "update, sekali per frame, dari isi Set itu. Ada tiga detail di",
                    "kode tadi:",
                    "  - e.code berisi posisi fisik tombol, misalnya 'KeyW' dan 'KeyA'.",
                    "    Ada juga e.key yang berisi huruf yang dihasilkan. Di papan",
                    "    ketik AZERTY yang dipakai di Prancis, tombol di posisi W",
                    "    menghasilkan huruf Z. Game yang membaca e.key === 'w' jadi",
                    "    nggak nyaman dimainkan di sana, sedangkan e.code tetap 'KeyW'.",
                    "    Dokumentasi MDN memakai contoh tombol W, A, S, D ini juga.",
                    "  - Kalau pemain pindah jendela sambil menahan tombol, keyup nggak",
                    "    pernah sampai. Tanpa blur, karakternya terus jalan sendiri",
                    "    waktu pemain balik.",
                    "  - Gamepad punya aturan lain. Gamepad API cuma punya event",
                    "    terhubung dan terputus (gamepadconnected dan",
                    "    gamepaddisconnected). Keadaan tombolnya harus dibaca sendiri",
                    "    tiap frame lewat navigator.getGamepads().",
                ],
            },
            {
                "heading": "Ditahan, baru ditekan, baru dilepas",
                "body": [
                    "Keadaan saja juga belum cukup. Lompat seharusnya terjadi sekali",
                    "waktu tombol ditekan, dan nggak diulang di tiap frame selama",
                    "tombolnya masih ditahan. Caranya, bandingkan keadaan frame ini",
                    "dengan frame sebelumnya:",
                ],
                "code": """// Keadaan tombol lompat di tiap frame (true = sedang ditahan).
const ditahan = [false, true, true, true, false, false, true];
let sebelumnya = false;

ditahan.forEach((sekarang, frame) => {
  const baruDitekan = sekarang && !sebelumnya;
  const baruDilepas = !sekarang && sebelumnya;
  let catatan = '';
  if (baruDitekan) catatan = ' <- baru ditekan, lompat!';
  if (baruDilepas) catatan = ' <- baru dilepas';
  console.log(`frame ${frame}: ditahan = ${sekarang}${catatan}`);
  sebelumnya = sekarang;
});""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  frame 0: ditahan = false",
                    "  frame 1: ditahan = true <- baru ditekan, lompat!",
                    "  frame 2: ditahan = true",
                    "  frame 3: ditahan = true",
                    "  frame 4: ditahan = false <- baru dilepas",
                    "  frame 5: ditahan = false",
                    "  frame 6: ditahan = true <- baru ditekan, lompat!",
                    "",
                    "Cuma frame 1 dan frame 6 yang memicu lompatan. Di frame 2 dan 3",
                    "tombolnya masih ditahan, tapi itu tekanan yang sama. Engine",
                    "menyediakan pertanyaan ini dengan nama sendiri: di Phaser ada",
                    "Phaser.Input.Keyboard.JustDown(tombol), di Godot ada",
                    "Input.is_action_just_pressed(), dan di Input System Unity ada",
                    "WasPressedThisFrame().",
                    "",
                    "Pisahkan juga tombol dari artinya. Logika game sebaiknya bertanya",
                    "\"apakah aksi lompat diminta?\". Satu tabel kecil memetakan Space,",
                    "tombol A di gamepad, dan ketukan di layar ke aksi lompat. Pemain",
                    "bisa mengganti tombol tanpa kamu mengubah logika game. Godot",
                    "menyebut tabel ini Input Map, Unity menyebutnya Input Actions.",
                ],
            },
            {
                "heading": "State game: menu, main, jeda, kalah",
                "body": [
                    "Selain input, game juga harus tahu dia sedang di layar mana.",
                    "Escape di tengah permainan artinya jeda. Di layar jeda, Escape",
                    "artinya lanjut main. Di layar kalah, Escape nggak berbuat apa-apa.",
                    "",
                    "Untuk itu dipakai state game: satu variabel yang menyimpan layar",
                    "yang sedang aktif, plus aturan pindah dari satu layar ke layar",
                    "lain. Aturannya ditulis sebagai tabel supaya gampang dibaca:",
                ],
                "code": """const transisi = {
  menu: { enter: 'main' },
  main: { escape: 'jeda', mati: 'kalah' },
  jeda: { escape: 'main', q: 'menu' },
  kalah: { enter: 'menu' },
};

let layar = 'menu';
const kejadian = ['escape', 'enter', 'escape', 'escape', 'mati', 'escape', 'enter'];

for (const k of kejadian) {
  const tujuan = transisi[layar][k];
  if (tujuan) {
    console.log(`${layar} --${k}--> ${tujuan}`);
    layar = tujuan;
  } else {
    console.log(`${layar}: "${k}" diabaikan`);
  }
}""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  menu: \"escape\" diabaikan",
                    "  menu --enter--> main",
                    "  main --escape--> jeda",
                    "  jeda --escape--> main",
                    "  main --mati--> kalah",
                    "  kalah: \"escape\" diabaikan",
                    "  kalah --enter--> menu",
                    "",
                    "Escape di menu dan di layar kalah diabaikan karena tabelnya nggak",
                    "punya baris untuk itu. Kamu nggak perlu menulis if untuk setiap",
                    "kemungkinan: yang nggak tertulis berarti nggak boleh.",
                    "",
                    "Tiap state juga punya update dan render sendiri. Waktu jeda, update",
                    "dunia game nggak dijalankan, tapi render tetap jalan. Dunia",
                    "digambar diam, lalu tulisan \"Jeda\" ditumpuk di atasnya. Pola",
                    "yang sama nanti dipakai untuk karakter di bab Game 2D di Browser.",
                ],
            },
            {
                "heading": "Dua jebakan yang sering muncul",
                "body": [
                    "Jebakan: memeriksa tombol jeda dengan keadaan \"sedang ditahan\".",
                    "Selama Escape ditahan, state bolak-balik jeda dan main di tiap",
                    "frame. Waktu tombolnya dilepas, hasilnya tergantung frame",
                    "terakhir, mirip lempar koin. Pakai \"baru ditekan\".",
                    "",
                    "Ingat: browser menghentikan requestAnimationFrame di tab yang",
                    "nggak kelihatan, tapi suara tetap jalan. Event visibilitychange",
                    "memberi tahu kapan tab disembunyikan, jadi game bisa pindah ke",
                    "state jeda sendiri dan mengecilkan suaranya.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Game web yang memakai tombol W, A, S, D dan membaca e.key jadi",
                    "canggung dimainkan pemain berpapan ketik Prancis. Karena itu",
                    "dokumentasi MDN memakai e.code untuk contoh kontrol game. Pola menu,",
                    "main, jeda, dan kalah juga ada di hampir semua game, dari game web",
                    "kecil sampai game yang dibuat dengan engine besar.",
                    "",
                    "Kasus kecil: di game buatan temanmu, menekan Escape kadang membuka",
                    "menu jeda, kadang nggak. Kadang menunya cuma berkedip lalu hilang.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Cetak state game dan keadaan Escape di tiap frame selama",
                    "     tombolnya ditahan. Kamu bakal melihat state bolak-balik jeda,",
                    "     main, jeda.",
                    "  2. Simpan keadaan Escape dari frame sebelumnya, lalu hitung:",
                    "       const baruDitekan = sekarang && !sebelumnya;",
                    "  3. Pindah state cuma kalau baruDitekan bernilai true.",
                    "  4. Uji lagi dengan daftar keadaan tetap, misalnya false, true,",
                    "     true, true, false. State harus berubah tepat sekali.",
                ],
            },
        ],
    },
    {
        "title": "4. Vektor 2D: Posisi, Kecepatan, dan Arah",
        "sections": [
            {
                "body": [
                    "Hampir semua yang bergerak di game 2D digambarkan dengan pasangan",
                    "dua angka, x dan y. Pasangan ini disebut vektor. Bayangkan vektor",
                    "sebagai panah: punya arah dan punya panjang.",
                    "",
                    "Satu bentuk yang sama dipakai untuk tiga hal berbeda:",
                    "  - Posisi. Panah dari titik (0, 0) ke tempat objek berada.",
                    "  - Kecepatan. Seberapa jauh dan ke mana objek pindah tiap detik.",
                    "    Kecepatan (200, 0) artinya 200 piksel per detik ke kanan.",
                    "  - Arah. Panah yang panjangnya 1, cuma menunjuk ke mana.",
                    "",
                    "Ada yang beda dari pelajaran matematika di sekolah. Di layar,",
                    "titik (0, 0) ada di pojok kiri atas, dan y makin besar ke bawah.",
                    "Canvas di browser, Phaser, dan Godot 2D memakai aturan ini. Unity",
                    "memakai y ke atas seperti di buku matematika, jadi hati-hati waktu",
                    "menyalin rumus dari satu engine ke engine lain.",
                    "",
                    "Di materi ini, angka di dalam vektor ditulis seperti di kode,",
                    "dengan titik desimal: (0.6, 0.8).",
                ],
            },
            {
                "heading": "Operasi yang paling sering dipakai",
                "body": [
                    "  - Tambah: (2, 3) + (1, -1) = (3, 2). Dipakai untuk posisi baru =",
                    "    posisi + kecepatan × dt.",
                    "  - Kurang: B - A menghasilkan panah dari A ke B. Dipakai untuk",
                    "    mencari arah ke target.",
                    "  - Kali dengan angka (skala): (3, 4) × 2 = (6, 8). Arahnya tetap,",
                    "    panjangnya berubah.",
                    "  - Panjang: akar dari x² + y², rumus Pythagoras. Panjang (3, 4)",
                    "    adalah 5. Di JavaScript, Math.hypot(x, y) menghitungnya.",
                    "  - Normalisasi: bagi vektor dengan panjangnya sendiri. Hasilnya",
                    "    menunjuk ke arah yang sama dengan panjang 1. (3, 4) jadi",
                    "    (0.6, 0.8). Vektor berpanjang 1 ini disebut vektor satuan.",
                    "  - Dot product: a.x × b.x + a.y × b.y. Hasilnya satu angka, dan",
                    "    dibahas di bagian bawah.",
                ],
            },
            {
                "heading": "Bergerak ke arah target",
                "body": [
                    "Musuh ingin mendekati pemain dengan kecepatan tetap. Caranya:",
                    "cari panah dari musuh ke pemain, jadikan panjangnya 1, lalu kali",
                    "dengan kecepatan.",
                ],
                "code": """const tambah = (a, b) => ({ x: a.x + b.x, y: a.y + b.y });
const kurang = (a, b) => ({ x: a.x - b.x, y: a.y - b.y });
const kali = (v, s) => ({ x: v.x * s, y: v.y * s });
const panjang = (v) => Math.hypot(v.x, v.y);
const normal = (v) => {
  const p = panjang(v);
  return p === 0 ? { x: 0, y: 0 } : { x: v.x / p, y: v.y / p };
};

const musuh = { x: 0, y: 0 };
const pemain = { x: 30, y: 40 };

const keTarget = kurang(pemain, musuh); // panah dari musuh ke pemain
const arah = normal(keTarget);          // panjangnya dibuat 1
const langkah = kali(arah, 10);         // 10 piksel per langkah

console.log('ke target  :', keTarget);
console.log('jarak      :', panjang(keTarget));
console.log('arah       :', arah);
console.log('posisi baru:', tambah(musuh, langkah));""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  ke target  : { x: 30, y: 40 }",
                    "  jarak      : 50",
                    "  arah       : { x: 0.6, y: 0.8 }",
                    "  posisi baru: { x: 6, y: 8 }",
                    "",
                    "Panah ke target panjangnya 50. Sesudah dinormalisasi jadi (0.6,",
                    "0.8), lalu dikali 10, musuh maju tepat 10 piksel ke arah pemain.",
                    "Tanpa normalisasi, musuh yang jauh bakal melesat dan musuh yang",
                    "dekat merayap, karena panjang panahnya ikut menentukan kecepatan.",
                    "",
                    "Fungsi normal() sengaja memeriksa panjang 0. Vektor (0, 0) nggak",
                    "punya arah, dan 0 / 0 di JavaScript menghasilkan NaN. Sekali NaN",
                    "masuk ke posisi, objeknya hilang dari layar dan semua hitungan",
                    "sesudahnya ikut jadi NaN.",
                ],
            },
            {
                "heading": "Gerak diagonal yang kelewat cepat",
                "body": [
                    "Pemain menekan kanan, vektor inputnya (1, 0). Menekan kanan dan",
                    "bawah sekaligus, vektornya (1, 1). Kalau vektor itu langsung",
                    "dikali kecepatan, coba lihat hasilnya:",
                ],
                "code": """const panjang = (v) => Math.hypot(v.x, v.y);
const KECEPATAN = 200; // piksel per detik

const lurus = { x: 1, y: 0 };    // cuma tombol kanan
const diagonal = { x: 1, y: 1 }; // kanan + bawah sekaligus

console.log('lurus   :', (panjang(lurus) * KECEPATAN).toFixed(1), 'px/detik');
console.log('diagonal:', (panjang(diagonal) * KECEPATAN).toFixed(1), 'px/detik');""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  lurus   : 200.0 px/detik",
                    "  diagonal: 282.8 px/detik",
                    "",
                    "Panjang (1, 1) itu akar 2, sekitar 1,414. Pemain yang berjalan",
                    "miring jadi 41% lebih cepat. Game tembak-tembakan lama seperti",
                    "GoldenEye 007 punya celah ini, dan pemain memanfaatkannya dengan",
                    "sengaja bergerak serong supaya lebih cepat sampai.",
                    "",
                    "Perbaikannya: normalisasi vektor input dulu, baru kali dengan",
                    "kecepatan. Untuk stik analog, jangan dinormalisasi mentah-mentah.",
                    "Stik yang didorong setengah memang seharusnya jalan pelan. Cukup",
                    "batasi panjangnya paling besar 1.",
                ],
            },
            {
                "heading": "Dot product: di depan atau di belakang?",
                "body": [
                    "Dot product dua vektor menghasilkan satu angka. Tandanya saja",
                    "sudah berguna: positif artinya dua panah menunjuk ke arah yang",
                    "kurang lebih sama, negatif artinya berlawanan, dan nol artinya",
                    "tegak lurus. Contohnya, penjaga di game siluman bisa memeriksa",
                    "apakah seseorang ada di depannya:",
                ],
                "code": """const dot = (a, b) => a.x * b.x + a.y * b.y;

const penjaga = { x: 0, y: 0 };
const hadap = { x: 1, y: 0 }; // penjaga menghadap ke kanan
const orang = { A: { x: 5, y: 1 }, B: { x: -4, y: 2 }, C: { x: 0, y: 6 } };

for (const [nama, p] of Object.entries(orang)) {
  const keOrang = { x: p.x - penjaga.x, y: p.y - penjaga.y };
  const d = dot(hadap, keOrang);
  const letak = d > 0 ? 'di depan' : d < 0 ? 'di belakang' : 'tepat di samping';
  console.log(`${nama}: dot = ${d}, ${letak}`);
}""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  A: dot = 5, di depan",
                    "  B: dot = -4, di belakang",
                    "  C: dot = 0, tepat di samping",
                    "",
                    "Kalau dua vektornya sudah dinormalisasi, dot product sama dengan",
                    "cosinus sudut di antara keduanya. Untuk pandangan penjaga selebar",
                    "90 derajat (45 ke kiri dan 45 ke kanan), syaratnya dot(hadap,",
                    "normal(keOrang)) > 0.707, karena cos 45° kira-kira 0,707.",
                    "",
                    "Engine sudah menyediakan tipe vektor sendiri. Namanya mirip,",
                    "kelakuannya nggak selalu sama:",
                    "",
                    "  engine   tipe           panjang     normalisasi    dot",
                    "  Phaser   Math.Vector2   length()    normalize()    dot()",
                    "  Godot    Vector2        length()    normalized()   dot()",
                    "  Unity    Vector2        magnitude   normalized     Vector2.Dot()",
                    "",
                    "Jebakan: normalize() di Phaser mengubah vektor itu sendiri lalu",
                    "mengembalikannya. normalized() di Godot dan Unity membuat vektor",
                    "baru. Kalau kamu menormalisasi kecepatan musuh di Phaser untuk",
                    "menghitung arah, kecepatan aslinya ikut berubah.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Game top-down dan game dengan stik analog selalu mengolah input",
                    "sebagai vektor: dibatasi panjangnya, lalu dikali kecepatan. Musuh",
                    "yang mengejar, misil yang mengunci target, dan kamera yang",
                    "menyusul pemain semuanya memakai pola kurang, normalisasi, kali.",
                    "",
                    "Kasus kecil: di game tembak-tembakan buatanmu, misil harus",
                    "mengejar pemain dengan 300 piksel per detik. Sekarang misilnya",
                    "bergetar bolak-balik waktu sudah dekat dengan pemain.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Hitung panah ke target: keTarget = kurang(pemain, misil).",
                    "  2. Hitung jarak langkah di frame ini: langkah = 300 * dt.",
                    "  3. Kalau panjang(keTarget) <= langkah, misil sudah sampai.",
                    "     Pindahkan misil tepat ke posisi pemain, jangan melewatinya.",
                    "     Getaran tadi muncul karena misil melompati pemain, lalu",
                    "     berbalik, lalu melompat lagi.",
                    "  4. Kalau belum sampai, geser misil:",
                    "       misil = tambah(misil, kali(normal(keTarget), langkah));",
                    "  5. Uji dengan jam palsu: misil di (0, 0), pemain di (30, 40), dt",
                    "     1/60. Misil harus sampai di (30, 40) dalam 10 frame dan diam",
                    "     di sana.",
                ],
            },
        ],
    },
    {
        "title": "5. Tabrakan AABB, Lingkaran, dan Respons",
        "sections": [
            {
                "body": [
                    "Urusan tabrakan dibagi dua. Deteksi menjawab \"apakah dua benda",
                    "ini bersentuhan?\". Respons menjawab \"lalu harus diapakan?\":",
                    "didorong keluar, dipantulkan, atau dihancurkan.",
                    "",
                    "Hampir semua game 2D nggak memeriksa bentuk gambarnya yang asli,",
                    "piksel demi piksel. Itu terlalu lambat. Tiap benda",
                    "diberi bentuk sederhana yang tak terlihat, biasanya kotak atau",
                    "lingkaran, dan bentuk itulah yang diperiksa. Bentuk ini disebut",
                    "hitbox.",
                    "",
                    "Kotak yang paling sering dipakai namanya AABB, singkatan dari",
                    "axis-aligned bounding box: kotak yang sisinya selalu sejajar",
                    "sumbu x dan y, dan nggak pernah diputar. Karena nggak diputar,",
                    "memeriksanya cuma butuh empat perbandingan.",
                ],
            },
            {
                "heading": "Syarat dua kotak bertabrakan",
                "body": [
                    "Lihat sumbu x dulu. Kotak A menempati x dari kiriA sampai",
                    "kananA, kotak B dari kiriB sampai kananB. Dua rentang itu",
                    "bertumpuk kalau kiriA < kananB dan kananA > kiriB. Hal yang sama",
                    "diperiksa di sumbu y. Dua kotak bertabrakan cuma kalau bertumpuk",
                    "di kedua sumbu sekaligus.",
                    "",
                    "Tanda < dan > sengaja dipakai, bukan <= dan >=. Kotak yang tepinya",
                    "pas bersentuhan nggak dihitung bertabrakan. Kalau dihitung,",
                    "pemain yang berdiri di lantai bakal \"menabrak\" lantai terus.",
                ],
                "code": """// Kotak: x, y = pojok kiri atas, w = lebar, h = tinggi. Sumbu y ke bawah.
function tabrakan(a, b) {
  return a.x < b.x + b.w && a.x + a.w > b.x &&
         a.y < b.y + b.h && a.y + a.h > b.y;
}

function dorongKeluar(pemain, dinding) {
  // Lebar tumpang tindih di tiap sumbu.
  const tx = Math.min(pemain.x + pemain.w, dinding.x + dinding.w) - Math.max(pemain.x, dinding.x);
  const ty = Math.min(pemain.y + pemain.h, dinding.y + dinding.h) - Math.max(pemain.y, dinding.y);
  // Dorong lewat sumbu yang tumpang tindihnya paling kecil.
  if (tx < ty) {
    const kiriDinding = pemain.x + pemain.w / 2 < dinding.x + dinding.w / 2;
    pemain.x += kiriDinding ? -tx : tx;
  } else {
    const atasDinding = pemain.y + pemain.h / 2 < dinding.y + dinding.h / 2;
    pemain.y += atasDinding ? -ty : ty;
  }
  return { tx, ty };
}

const dinding = { x: 100, y: 0, w: 20, h: 200 };
const pemain = { x: 85, y: 50, w: 24, h: 32 };

console.log('bertabrakan?', tabrakan(pemain, dinding));
console.log('tumpang tindih:', dorongKeluar(pemain, dinding));
console.log('sesudah didorong: x =', pemain.x, 'y =', pemain.y);
console.log('masih bertabrakan?', tabrakan(pemain, dinding));""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  bertabrakan? true",
                    "  tumpang tindih: { tx: 9, ty: 32 }",
                    "  sesudah didorong: x = 76 y = 50",
                    "  masih bertabrakan? false",
                    "",
                    "Pemain masuk 9 piksel ke dalam dinding di sumbu x, dan 32 piksel",
                    "di sumbu y. Jalan keluar terpendek lewat sumbu x, jadi pemain",
                    "digeser 9 piksel ke kiri, karena pusatnya ada di sebelah kiri",
                    "pusat dinding. Kalau didorong lewat sumbu y, pemain tiba-tiba",
                    "pindah 32 piksel ke atas atau ke bawah, dan kelihatan seperti",
                    "teleport.",
                    "",
                    "Sesudah didorong, tepi kanan pemain ada di x = 100, tepat di tepi",
                    "kiri dinding. Keduanya bersentuhan, tapi menurut aturan tadi sudah",
                    "nggak bertabrakan. Geseran sekecil mungkin yang memisahkan dua",
                    "benda ini disebut vektor dorong minimum. Di contoh ini nilainya",
                    "(-9, 0).",
                ],
            },
            {
                "heading": "Lingkaran dan pantulan",
                "body": [
                    "Bola, koin, dan ledakan lebih cocok diberi hitbox lingkaran. Dua",
                    "lingkaran bertabrakan kalau jarak pusatnya lebih kecil dari",
                    "jumlah jari-jarinya. Supaya nggak perlu menghitung akar, bandingkan",
                    "kuadratnya saja.",
                    "",
                    "Untuk pantulan, kecepatan dicerminkan terhadap normal permukaan.",
                    "Normal itu vektor satuan yang tegak lurus permukaan dan menunjuk",
                    "keluar. Lantai di layar (y ke bawah) punya normal (0, -1).",
                ],
                "code": """function tabrakanLingkaran(a, b) {
  const dx = b.x - a.x;
  const dy = b.y - a.y;
  const r = a.r + b.r;
  return dx * dx + dy * dy < r * r; // bandingkan kuadratnya, tanpa akar
}

const dot = (a, b) => a.x * b.x + a.y * b.y;
function pantul(v, n) { // n: normal permukaan, panjangnya 1
  const d = dot(v, n);
  return { x: v.x - 2 * d * n.x, y: v.y - 2 * d * n.y };
}

const koin = { x: 10, y: 10, r: 8 };
console.log('kena koin (22, 18)?', tabrakanLingkaran(koin, { x: 22, y: 18, r: 6 }));
console.log('kena koin (20, 16)?', tabrakanLingkaran(koin, { x: 20, y: 16, r: 6 }));

const bola = { x: 3, y: 4 }; // kecepatan bola: ke kanan dan ke bawah
console.log('kena lantai       :', pantul(bola, { x: 0, y: -1 }));
console.log('kena dinding kanan:', pantul(bola, { x: -1, y: 0 }));""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  kena koin (22, 18)? false",
                    "  kena koin (20, 16)? true",
                    "  kena lantai       : { x: 3, y: -4 }",
                    "  kena dinding kanan: { x: -3, y: 4 }",
                    "",
                    "Pemain di (22, 18) berjarak kuadrat 12² + 8² = 208 dari koin,",
                    "lebih besar dari (8 + 6)² = 196, jadi belum kena. Di (20, 16)",
                    "jaraknya kuadrat 136, jadi kena.",
                    "",
                    "Bola yang kena lantai cuma berbalik arah vertikalnya. Yang kena",
                    "dinding kanan cuma berbalik arah horizontalnya. Untuk dinding yang",
                    "sejajar sumbu, rumus panjang itu sama saja dengan membalik tanda",
                    "vx atau vy. Rumus lengkapnya baru perlu untuk permukaan miring.",
                    "Supaya bola makin lama makin pelan, kalikan hasilnya dengan angka",
                    "di bawah 1, misalnya 0,8. Phaser menyebut angka ini bounce.",
                ],
            },
            {
                "heading": "Peluru yang menembus dinding",
                "body": [
                    "Deteksi tabrakan cuma memeriksa posisi di akhir tiap langkah.",
                    "Benda yang bergerak cepat bisa ada di depan dinding di satu",
                    "langkah, lalu sudah di belakangnya di langkah berikutnya, tanpa",
                    "pernah tercatat berada di dalamnya:",
                ],
                "code": """const dinding = { x: 100, w: 10 }; // dinding tipis; cukup sumbu x
const LEBAR_PELURU = 4;

function kena(x) {
  return x < dinding.x + dinding.w && x + LEBAR_PELURU > dinding.x;
}

for (const kecepatan of [8, 30]) { // piksel per langkah
  let x = 60;
  let tertahan = false;
  for (let langkah = 0; langkah < 6; langkah++) {
    x += kecepatan;
    if (kena(x)) {
      tertahan = true;
      break;
    }
  }
  const hasil = tertahan ? 'tertahan dinding' : 'menembus dinding';
  console.log(`kecepatan ${kecepatan}: ${hasil}, x = ${x}`);
}""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  kecepatan 8: tertahan dinding, x = 100",
                    "  kecepatan 30: menembus dinding, x = 240",
                    "",
                    "Peluru cepat melompat dari x = 90 ke x = 120 dalam satu langkah,",
                    "melewati dinding yang ada di 100 sampai 110. Masalah ini disebut",
                    "tunneling. Ada tiga cara umum mengatasinya:",
                    "  1. Pecah gerakan jadi beberapa sublangkah yang masing-masing",
                    "     lebih pendek dari tebal dinding paling tipis.",
                    "  2. Periksa seluruh jalur dari posisi lama ke posisi baru, termasuk",
                    "     titik-titik di tengahnya. Cara ini disebut continuous collision",
                    "     detection (CCD).",
                    "  3. Untuk peluru, tembakkan sinar (raycast) dari posisi lama ke",
                    "     posisi baru, lalu cari benda pertama yang dilewati.",
                    "",
                    "Engine fisika menyediakan pilihan ini. RigidBody2D di Godot punya",
                    "properti continuous_cd, dan Box2D punya penanda bullet untuk",
                    "benda yang bergerak cepat.",
                ],
            },
            {
                "heading": "Banyak benda, banyak pasangan",
                "body": [
                    "Memeriksa semua pasangan itu mahal. Dengan n benda ada n × (n - 1)",
                    "/ 2 pasangan, jadi 1.000 benda berarti 499.500 pemeriksaan tiap",
                    "langkah. Karena itu engine memakai dua tahap. Tahap kasar (broad",
                    "phase) membuang pasangan yang jelas berjauhan, misalnya dengan",
                    "membagi dunia jadi petak-petak dan cuma memeriksa benda di petak",
                    "yang sama. Quadtree dan sweep and prune adalah dua cara lain.",
                    "Tahap halus (narrow phase) baru menjalankan tes kotak atau",
                    "lingkaran tadi.",
                    "",
                    "Fisika arcade di Phaser cuma mengenal dua bentuk: kotak sejajar sumbu dan",
                    "lingkaran. Untuk bentuk miring atau poligon, Phaser menyertakan",
                    "Matter.js. Godot dan Unity punya banyak bentuk collider.",
                    "",
                    "Jebakan: menyelesaikan sumbu x dan y sekaligus. Pemain yang",
                    "berjalan di atas deretan petak lantai bisa tersangkut di",
                    "sambungan dua petak, karena untuk sesaat ia tumpang tindih tipis",
                    "di sumbu x dengan petak berikutnya. Gerakkan dan selesaikan",
                    "sumbu x dulu, baru sumbu y.",
                    "",
                    "Jebakan: hitbox seukuran gambar terasa curang buat pemain. Ujung",
                    "rambut yang kena peluru dianggap mati. Banyak game sengaja",
                    "membuat hitbox pemain lebih kecil daripada gambarnya.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Game platformer dan game pertarungan 2D mengandalkan kotak. Game",
                    "pertarungan bahkan membedakan dua jenis kotak di tiap frame",
                    "animasi: kotak serangan (hitbox) dan kotak yang bisa dilukai",
                    "(hurtbox). Pukulan kena kalau hitbox penyerang bertumpuk dengan",
                    "hurtbox lawan.",
                    "",
                    "Kasus kecil: di game buatanmu, pemain bisa dash dengan kecepatan",
                    "40 piksel per langkah. Dinding tipis 12 piksel kadang ditembus",
                    "begitu saja.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Bandingkan jarak per langkah (40) dengan tebal dinding paling",
                    "     tipis (12). Kalau jaraknya lebih besar, tunneling bisa terjadi.",
                    "  2. Hitung jumlah sublangkah supaya tiap sublangkah paling jauh",
                    "     setengah tebal dinding:",
                    "       const n = Math.ceil(40 / 6); // 7 sublangkah",
                    "  3. Gerakkan pemain n kali sejauh 40 / n, dan periksa tabrakan",
                    "     di setiap sublangkah.",
                    "  4. Begitu bertabrakan, dorong keluar dengan vektor dorong",
                    "     minimum, lalu hentikan dash.",
                    "  5. Uji dengan posisi tetap: pemain di x = 60, dinding di x = 100",
                    "     sampai 112. Pemain harus berhenti dengan tepi kanannya di",
                    "     x = 100.",
                ],
            },
        ],
    },
    {
        "title": "6. Transformasi: Translasi, Rotasi, dan Skala",
        "sections": [
            {
                "body": [
                    "Gambar sebuah tank biasanya dibuat dengan titik tengah tank di",
                    "(0, 0). Ujung meriamnya misalnya di (10, 0), sepuluh piksel di",
                    "kanan titik tengah. Koordinat yang diukur dari titik tengah benda",
                    "itu sendiri disebut ruang lokal.",
                    "",
                    "Di dalam game, tank itu berdiri di (100, 50) dan sedang menghadap",
                    "ke bawah. Untuk tahu di mana ujung meriamnya di layar, titik lokal",
                    "tadi harus diubah ke ruang dunia, yaitu koordinat yang dipakai",
                    "seluruh level. Perubahan ini disebut transformasi, dan ada tiga",
                    "jenis dasarnya.",
                ],
            },
            {
                "heading": "Tiga transformasi dasar",
                "body": [
                    "  - Translasi (geser): tambahkan jarak geser ke tiap koordinat.",
                    "  - Skala: kalikan tiap koordinat. Skala 2 membuat benda dua kali",
                    "    lebih besar, skala -1 di x mencerminkannya.",
                    "  - Rotasi (putar): putar titik di sekitar (0, 0) sebesar sudut θ.",
                    "",
                    "  translasi:  x' = x + tx          y' = y + ty",
                    "  skala:      x' = x * sx          y' = y * sy",
                    "  rotasi:     x' = x cos θ - y sin θ",
                    "              y' = x sin θ + y cos θ",
                    "",
                    "Karena sumbu y di layar mengarah ke bawah, sudut positif memutar",
                    "benda searah jarum jam. Phaser menuliskannya terang-terangan: 0",
                    "derajat menghadap ke kanan, 90 derajat ke bawah. Math.sin dan",
                    "Math.cos di JavaScript memakai radian, dan 180 derajat sama",
                    "dengan π radian.",
                ],
            },
            {
                "heading": "Urutan mengubah hasil",
                "body": [
                    "Rotasi selalu berputar di sekitar titik (0, 0). Akibatnya,",
                    "memutar dulu lalu menggeser memberi hasil yang lain dari",
                    "menggeser dulu lalu memutar:",
                ],
                "code": """const derajat = (d) => (d * Math.PI) / 180;

function putar(p, sudut) {
  const c = Math.cos(sudut);
  const s = Math.sin(sudut);
  return { x: p.x * c - p.y * s, y: p.x * s + p.y * c };
}
const geser = (p, t) => ({ x: p.x + t.x, y: p.y + t.y });
const teks = (p) => `(${p.x.toFixed(1)}, ${p.y.toFixed(1)})`;

const ujungMeriam = { x: 10, y: 0 }; // titik di ruang lokal tank
const posisiTank = { x: 100, y: 50 };
const sudut = derajat(90);

console.log('putar dulu, lalu geser:', teks(geser(putar(ujungMeriam, sudut), posisiTank)));
console.log('geser dulu, lalu putar:', teks(putar(geser(ujungMeriam, posisiTank), sudut)));""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  putar dulu, lalu geser: (100.0, 60.0)",
                    "  geser dulu, lalu putar: (-50.0, 110.0)",
                    "",
                    "Hasil pertama benar: ujung meriam ada 10 piksel di bawah tank,",
                    "karena tank menghadap ke bawah. Di hasil kedua, titiknya sudah",
                    "dibawa ke (110, 50) sebelum diputar, jadi ia berputar di sekitar",
                    "pojok kiri atas layar dan terlempar ke luar layar.",
                    "",
                    "Aturan yang dipakai hampir semua engine untuk satu benda: skala",
                    "dulu, lalu putar, lalu geser. Ketiganya dikerjakan selagi titik",
                    "masih di ruang lokal, dan baru di langkah terakhir titiknya",
                    "dibawa ke tempatnya di dunia.",
                    "",
                    "toFixed(1) dipakai karena Math.cos(π/2) di komputer bernilai",
                    "6.123233995736766e-17, angka yang kecil sekali tapi nggak persis 0.",
                ],
            },
            {
                "heading": "Matriks 3x3: semua transformasi jadi satu",
                "body": [
                    "Kalau satu benda punya ratusan titik, menghitung skala, putar,",
                    "dan geser satu per satu untuk tiap titik itu boros. Ketiganya bisa",
                    "digabung jadi satu matriks, yaitu tabel angka 3 baris 3 kolom.",
                    "",
                    "Kenapa 3x3 padahal cuma ada x dan y? Rotasi dan skala bisa ditulis",
                    "sebagai perkalian, tapi translasi adalah penjumlahan. Trik yang",
                    "dipakai: tulis titik sebagai (x, y, 1). Angka 1 tambahan itu",
                    "membuat translasi juga bisa ditulis sebagai perkalian matriks.",
                    "Bentuk ini disebut koordinat homogen.",
                    "",
                    "  translasi        rotasi              skala",
                    "  | 1  0  tx |     | cos  -sin  0 |    | sx  0   0 |",
                    "  | 0  1  ty |     | sin   cos  0 |    | 0   sy  0 |",
                    "  | 0  0  1  |     | 0     0    1 |    | 0   0   1 |",
                ],
                "code": """// Matriks 3x3 disimpan sebagai array 9 angka, baris demi baris.
function kaliMatriks(a, b) {
  const hasil = [];
  for (let r = 0; r < 3; r++) {
    for (let c = 0; c < 3; c++) {
      hasil.push(a[r * 3] * b[c] + a[r * 3 + 1] * b[3 + c] + a[r * 3 + 2] * b[6 + c]);
    }
  }
  return hasil;
}

const terapkan = (m, p) => ({
  x: m[0] * p.x + m[1] * p.y + m[2],
  y: m[3] * p.x + m[4] * p.y + m[5],
});

const translasi = (tx, ty) => [1, 0, tx, 0, 1, ty, 0, 0, 1];
const skala = (sx, sy) => [sx, 0, 0, 0, sy, 0, 0, 0, 1];
const rotasi = (sudut) => {
  const c = Math.cos(sudut);
  const s = Math.sin(sudut);
  return [c, -s, 0, s, c, 0, 0, 0, 1];
};
const derajat = (d) => (d * Math.PI) / 180;

// Dibaca dari kanan ke kiri: skala dulu, lalu putar, lalu geser.
const M = kaliMatriks(translasi(100, 50), kaliMatriks(rotasi(derajat(90)), skala(2, 2)));

for (const p of [{ x: 10, y: 0 }, { x: 0, y: 5 }]) {
  const q = terapkan(M, p);
  console.log(`(${p.x}, ${p.y}) -> (${q.x.toFixed(1)}, ${q.y.toFixed(1)})`);
}""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  (10, 0) -> (100.0, 70.0)",
                    "  (0, 5) -> (90.0, 50.0)",
                    "",
                    "Titik (10, 0) diperbesar jadi (20, 0), diputar jadi (0, 20), lalu",
                    "digeser jadi (100, 70). Matriks M cukup dihitung sekali, lalu",
                    "dipakai untuk semua titik benda itu. Kartu grafis mengerjakan hal",
                    "yang sama untuk jutaan titik tiap frame.",
                    "",
                    "Urutan penulisannya terbalik: translasi × rotasi × skala, tapi",
                    "yang dikenakan ke titik lebih dulu adalah skala, yang paling",
                    "kanan. Perkalian matriks juga nggak bisa ditukar urutannya,",
                    "persis seperti hasil putar dan geser tadi.",
                ],
            },
            {
                "heading": "Ruang lokal, ruang dunia, dan benda anak",
                "body": [
                    "Meriam yang menempel di tank juga punya ruang lokal sendiri,",
                    "diukur dari titik tengah tank. Posisinya di dunia adalah",
                    "transformasi tank dikalikan transformasi meriam. Tank berputar,",
                    "meriam ikut berputar. Meriam berputar sendiri, tank diam.",
                    "",
                    "Canvas di browser bekerja dengan cara yang sama.",
                    "ctx.translate(), ctx.rotate(), dan ctx.scale() mengalikan matriks",
                    "yang sedang aktif, dan ctx.save() serta ctx.restore() menyimpan",
                    "lalu mengembalikan matriks itu:",
                ],
                "bahasa": "browser",
                "code": """const ctx = document.querySelector('canvas').getContext('2d');
const tank = { x: 100, y: 50, sudut: Math.PI / 6 };
const sudutMeriam = Math.PI / 4; // relatif terhadap badan tank

ctx.save();
ctx.translate(tank.x, tank.y);  // pindah ke posisi tank
ctx.rotate(tank.sudut);         // putar mengikuti badan tank
ctx.fillRect(-16, -10, 32, 20); // badan, digambar di sekitar (0, 0)

ctx.save();
ctx.rotate(sudutMeriam);        // meriam berputar di atas badan
ctx.fillRect(0, -3, 24, 6);     // laras dari pusat ke kanan
ctx.restore();

ctx.restore();""",
            },
            {
                "heading": "Derajat, radian, dan 3D",
                "body": [
                    "Engine menyimpan transformasi tiap benda dan menyediakan dua",
                    "versi posisinya:",
                    "",
                    "  engine   posisi lokal              posisi dunia",
                    "  Phaser   anak di dalam Container   dihitung dari Container",
                    "  Godot    position                  global_position",
                    "  Unity    transform.localPosition   transform.position",
                    "",
                    "Jebakan: Math.sin(90) bukan sin 90 derajat. Angka 90 dibaca",
                    "sebagai 90 radian, dan hasilnya kira-kira 0,894. Phaser punya dua",
                    "properti untuk sudut: angle dalam derajat dan rotation dalam",
                    "radian. Godot punya rotation (radian) dan rotation_degrees.",
                    "",
                    "Jebakan: skala -1 untuk membalik sprite ikut membalik semua",
                    "benda anaknya. Phaser menyediakan setFlipX(true) yang cuma",
                    "membalik gambarnya.",
                    "",
                    "Di 3D, matriksnya jadi 4x4 dengan alasan yang sama, yaitu",
                    "koordinat homogen. Rotasi 3D biasanya disimpan sebagai",
                    "quaternion, empat angka yang menghindari masalah gimbal lock dan",
                    "bisa diinterpolasi dengan mulus. Bab grafis dan bab XR nanti",
                    "memakainya.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Setiap benda di Phaser, Godot, dan Unity punya posisi, sudut, dan",
                    "skala yang digabung jadi satu matriks. Pedang yang dipegang",
                    "karakter, roda mobil, dan nama pemain yang melayang di atas",
                    "kepala semuanya benda anak yang ikut bergerak bersama induknya.",
                    "",
                    "Kasus kecil: peluru harus keluar dari ujung meriam tank. Ujung",
                    "meriam di ruang lokal ada di (24, 0). Tank berdiri di (200, 120)",
                    "dan diputar 30 derajat.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tulis titik lokalnya: ujung = { x: 24, y: 0 }.",
                    "  2. Putar dengan sudut tank (dalam radian):",
                    "       const s = (30 * Math.PI) / 180;",
                    "       const p = putar(ujung, s); // (20.78, 12.00)",
                    "  3. Geser dengan posisi tank: (220.78, 132.00). Di situ peluru",
                    "     dimunculkan.",
                    "  4. Arah peluru adalah vektor (1, 0) yang diputar dengan sudut",
                    "     yang sama, yaitu (0.87, 0.50). Kalikan dengan kecepatan",
                    "     peluru.",
                    "  5. Cek dengan sudut 0: peluru harus muncul di (224, 120) dan",
                    "     terbang lurus ke kanan.",
                ],
            },
        ],
    },
    {
        "title": "7. Phaser: Scene, Sprite, dan Fisika Arcade",
        "sections": [
            {
                "body": [
                    "Phaser adalah framework game 2D untuk browser. Kodenya ditulis",
                    "dengan JavaScript atau TypeScript, dan hasilnya jalan di browser",
                    "komputer maupun ponsel. Lisensinya MIT, jadi gratis dipakai untuk",
                    "game komersial. Phaser dikembangkan Phaser Studio Inc bersama",
                    "komunitas open source, dan sudah dikembangkan lebih dari 13",
                    "tahun.",
                    "",
                    "Versi stabil terbaru saat materi ini ditulis (Oktober 2026)",
                    "adalah 4.2.1, rilis 9 Juli 2026. Phaser 4 sendiri baru stabil",
                    "10 April 2026, jadi tutorial di internet kebanyakan masih memakai",
                    "Phaser 3. Menurut tim Phaser, API untuk pemakaian sehari-hari",
                    "hampir sama. Yang diganti total adalah mesin penggambarnya: sistem",
                    "pipeline diganti render node, efek FX dan mask dilebur jadi sistem",
                    "filter, objek Mesh dan Plane dibuang, dan renderer Canvas",
                    "dianggap usang. Kalau tutorial lama memakai salah satu dari itu,",
                    "buka panduan migrasi v3 ke v4 di repositori Phaser.",
                    "",
                    "Hampir semua yang kamu pelajari di dua bab sebelumnya sudah",
                    "disediakan Phaser: game loop, delta time, langkah fisika tetap,",
                    "vektor, dan tabrakan kotak. Yang tersisa buatmu adalah aturan",
                    "permainannya.",
                ],
            },
            {
                "heading": "Memasang Phaser",
                "bahasa": "terminal",
                "code": """# proyek baru dari template resmi (memilih framework dan bundler)
npm create @phaserjs/game@latest

# atau tambahkan ke proyek yang sudah ada
npm install phaser""",
            },
            {
                "body": [
                    "Perintah pertama menanyakan beberapa hal, lalu menyiapkan proyek",
                    "lengkap. Pilihannya mencakup Vite, React, Vue, dan beberapa yang",
                    "lain, dalam versi JavaScript atau TypeScript. Sesudah itu,",
                    "jalankan server pengembangan yang disebut di README template-nya,",
                    "biasanya npm run dev.",
                    "",
                    "Kenapa harus lewat server? Phaser memuat gambar dan berkas peta",
                    "lewat permintaan HTTP, dan browser menolak sebagian permintaan itu",
                    "kalau halamannya dibuka langsung sebagai berkas (alamatnya",
                    "diawali file://). Untuk mencoba cepat tanpa npm, simpan",
                    "phaser.min.js di folder proyek, pasang lewat tag script, lalu",
                    "jalankan python3 -m http.server di folder itu. Versi terkecil",
                    "yang lengkap berukuran sekitar 345 KB sesudah dikompres gzip.",
                ],
            },
            {
                "heading": "Tiga fungsi di setiap scene",
                "body": [
                    "Game Phaser dibagi jadi scene. Satu scene biasanya satu layar:",
                    "menu, level 1, layar kalah. Ini sama dengan state game di bab",
                    "pertama, dan Phaser yang mengurus perpindahannya.",
                    "",
                    "Setiap scene punya tiga fungsi utama:",
                    "  - preload() memuat aset seperti gambar, suara, dan peta. Scene",
                    "    baru mulai sesudah semua aset di sini selesai dimuat.",
                    "  - create() jalan sekali sesudah preload. Di sini sprite, lantai,",
                    "    dan tombol dibuat.",
                    "  - update(time, delta) jalan di setiap frame. time adalah jam saat",
                    "    itu dan delta adalah lama frame terakhir, dua-duanya dalam",
                    "    milidetik.",
                    "",
                    "Sprite adalah gambar yang bisa bergerak, diputar, dan dianimasikan.",
                    "Hampir semua yang terlihat di game Phaser adalah sprite.",
                ],
            },
            {
                "heading": "Game pertama: pemain di atas lantai",
                "code": """import Phaser from 'phaser';

class Main extends Phaser.Scene {
  constructor() {
    super('Main');
  }

  preload() {
    this.load.image('langit', 'aset/langit.png');
    this.load.image('tanah', 'aset/tanah.png');
    this.load.spritesheet('pahlawan', 'aset/pahlawan.png', { frameWidth: 32, frameHeight: 48 });
  }

  create() {
    this.add.image(400, 300, 'langit');

    const lantai = this.physics.add.staticGroup();
    lantai.create(400, 568, 'tanah');

    this.pemain = this.physics.add.sprite(100, 450, 'pahlawan');
    this.pemain.setCollideWorldBounds(true);
    this.physics.add.collider(this.pemain, lantai);

    this.tombol = this.input.keyboard.createCursorKeys();
  }

  update(time, delta) {
    const { left, right, up } = this.tombol;
    if (left.isDown) this.pemain.setVelocityX(-160);
    else if (right.isDown) this.pemain.setVelocityX(160);
    else this.pemain.setVelocityX(0);

    if (up.isDown && this.pemain.body.blocked.down) {
      this.pemain.setVelocityY(-330);
    }
  }
}

new Phaser.Game({
  type: Phaser.AUTO,
  width: 800,
  height: 600,
  physics: { default: 'arcade', arcade: { gravity: { x: 0, y: 300 } } },
  scene: Main,
});""",
            },
            {
                "body": [
                    "Baris demi baris yang perlu kamu pahami:",
                    "  - load.spritesheet memuat satu gambar yang berisi banyak frame",
                    "    berukuran sama, di sini 32 x 48 piksel. Materi berikutnya",
                    "    membahasnya.",
                    "  - staticGroup membuat kelompok benda statis yang nggak pernah",
                    "    bergerak, cocok untuk lantai dan pijakan.",
                    "  - physics.add.sprite membuat sprite dengan body dinamis: punya",
                    "    kecepatan dan kena gravitasi.",
                    "  - collider(pemain, lantai) menyuruh Phaser memeriksa tabrakan",
                    "    kotak keduanya di setiap langkah fisika, lalu mendorong pemain",
                    "    keluar. Ini persis yang kamu tulis sendiri di bab sebelumnya.",
                    "  - createCursorKeys menyiapkan tombol panah, Space, dan Shift.",
                    "    isDown adalah keadaan \"sedang ditahan\".",
                    "  - setVelocityX(160) artinya 160 piksel per detik. Nggak perlu",
                    "    dikali delta, karena fisika arcade menghitung geraknya sendiri",
                    "    dengan langkah tetap 60 kali per detik.",
                    "  - body.blocked.down bernilai true kalau bagian bawah body",
                    "    menempel di benda statis, petak, atau batas dunia. Lompat cuma",
                    "    diizinkan saat itu, jadi pemain nggak bisa melompat di udara.",
                    "",
                    "Gravitasi ditulis sebagai vektor { x: 0, y: 300 }: 300 piksel per",
                    "detik per detik ke bawah.",
                ],
            },
            {
                "heading": "Fisika arcade dan teman-temannya",
                "body": [
                    "Fisika arcade sengaja dibuat sederhana. Body-nya cuma boleh kotak",
                    "sejajar sumbu atau lingkaran, dan kotaknya nggak ikut berputar",
                    "walaupun gambarnya diputar. Imbalannya, fisika ini cepat dan cukup",
                    "untuk game platformer, game tembak-tembakan dari atas, dan game",
                    "teka-teki. Untuk bentuk poligon, benda yang berguling, atau",
                    "sambungan seperti rantai, Phaser menyertakan Matter.js. Matter",
                    "lebih lengkap, tapi lebih berat.",
                    "",
                    "Saat mencoba, tambahkan debug: true di konfigurasi arcade. Phaser",
                    "lalu menggambar kotak body dan arah kecepatannya, jadi kamu bisa",
                    "melihat hitbox yang dipakai untuk tabrakan.",
                    "",
                    "Hubungan Phaser dengan dua bab sebelumnya:",
                    "",
                    "  konsep              di Phaser",
                    "  game loop           Phaser.Game, memakai requestAnimationFrame",
                    "  delta time          update(time, delta), dalam milidetik",
                    "  fixed timestep      fisika arcade, 60 langkah per detik",
                    "  vektor              Phaser.Math.Vector2",
                    "  tabrakan kotak      body arcade + physics.add.collider",
                    "  state game          scene: menu, level, layar kalah",
                ],
            },
            {
                "heading": "Jebakan yang sering muncul",
                "body": [
                    "Jebakan: mengalikan kecepatan dengan delta lagi. setVelocityX",
                    "sudah dalam piksel per detik. Kalau ditulis setVelocityX(160 *",
                    "delta), pemain bergerak sekitar 16 kali lebih cepat di 60 FPS,",
                    "dan kecepatannya berubah-ubah mengikuti FPS.",
                    "",
                    "Jebakan: this hilang di dalam callback. Fungsi yang dipanggil",
                    "Phaser saat dua benda bersentuhan perlu tahu scene-nya. Berikan",
                    "konteksnya di argumen kelima:",
                    "",
                    "  this.physics.add.overlap(this.pemain, koin, this.ambilKoin, null, this);",
                    "",
                    "Ingat: kalau kunci aset salah ketik, misalnya 'pahlawn', Phaser",
                    "nggak berhenti. Ia memakai tekstur pengganti bernama __MISSING,",
                    "jadi yang muncul kotak kecil yang aneh. Samakan kunci di preload",
                    "dan di create, lalu cek tab Network di DevTools untuk gambar yang",
                    "gagal dimuat.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Menurut README resminya, game Phaser bisa diterbitkan sebagai game",
                    "web biasa, YouTube Playables, Discord Activities, game di Reddit,",
                    "atau overlay Twitch. Dengan alat pihak ketiga, game yang sama bisa",
                    "dibungkus jadi aplikasi iOS, Android, atau Steam. Phaser juga",
                    "dipakai untuk iklan yang bisa dimainkan (playable ads) dan game di",
                    "portal game web.",
                    "",
                    "Kasus kecil: di game Phaser buatanmu, pemain bisa terus naik ke",
                    "langit dengan menekan panah atas berkali-kali di udara.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Buka update() dan cari syarat lompatnya. Kemungkinan cuma",
                    "     tertulis if (up.isDown).",
                    "  2. Tambahkan syarat body menempel di bawah:",
                    "       if (up.isDown && this.pemain.body.blocked.down)",
                    "  3. Supaya menahan tombol nggak membuat pemain langsung melompat",
                    "     lagi begitu mendarat, ganti up.isDown dengan",
                    "     Phaser.Input.Keyboard.JustDown(up).",
                    "  4. Nyalakan debug: true dan perhatikan kotak body pemain. Lompat",
                    "     cuma boleh terjadi saat kotak itu menyentuh lantai.",
                ],
            },
        ],
    },
    {
        "title": "8. Tilemap, Kamera, dan Animasi Sprite",
        "sections": [
            {
                "body": [
                    "Bayangkan level platformer selebar sepuluh layar. Kalau dibuat",
                    "sebagai satu gambar raksasa, berkasnya berat, dan menggeser satu",
                    "pijakan berarti menggambar ulang gambarnya.",
                    "",
                    "Hampir semua game 2D memakai cara lain, yaitu tilemap. Dunia",
                    "dibagi jadi petak-petak kecil berukuran sama, misalnya 32 x 32",
                    "piksel. Gambar semua jenis petak (rumput, tanah, batu, air)",
                    "dikumpulkan di satu gambar yang disebut tileset. Peta levelnya",
                    "cuma daftar angka: petak di baris ini kolom itu memakai gambar",
                    "nomor sekian dari tileset.",
                    "",
                    "Mirip lantai keramik. Tukangnya cukup punya beberapa jenis",
                    "keramik, lalu menyusunnya mengikuti denah.",
                ],
            },
            {
                "heading": "Peta sebagai larik angka",
                "body": [
                    "Di kode, tilemap cukup berupa larik dua dimensi. Angka 0 berarti",
                    "kosong, angka lain menunjuk gambar di tileset. Untuk tahu petak di",
                    "bawah suatu titik, bagi koordinatnya dengan ukuran petak lalu",
                    "bulatkan ke bawah:",
                ],
                "code": """const UKURAN = 32; // satu petak 32 x 32 piksel
const peta = [
  [0, 0, 0, 0, 0, 0],
  [0, 0, 0, 5, 5, 0],
  [1, 1, 0, 0, 1, 1],
  [2, 2, 0, 0, 2, 2],
];
const padat = new Set([1, 2, 5]); // petak yang nggak bisa ditembus

function petakDi(x, y) {
  const kolom = Math.floor(x / UKURAN);
  const baris = Math.floor(y / UKURAN);
  const nilai = peta[baris]?.[kolom];
  return { kolom, baris, nilai: nilai ?? 'luar peta' };
}

for (const [x, y] of [[10, 70], [100, 40], [70, 80], [500, 10]]) {
  const p = petakDi(x, y);
  const sifat = padat.has(p.nilai) ? 'padat' : 'kosong';
  console.log(`(${x}, ${y}) -> kolom ${p.kolom}, baris ${p.baris}, petak ${p.nilai}, ${sifat}`);
}""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  (10, 70) -> kolom 0, baris 2, petak 1, padat",
                    "  (100, 40) -> kolom 3, baris 1, petak 5, padat",
                    "  (70, 80) -> kolom 2, baris 2, petak 0, kosong",
                    "  (500, 10) -> kolom 15, baris 0, petak luar peta, kosong",
                    "",
                    "Titik (70, 80) jatuh di kolom 2 baris 2, yaitu lubang di tengah",
                    "tanah. Titik (500, 10) ada di luar peta, dan kode ini",
                    "menganggapnya kosong. Banyak game justru menganggap luar peta",
                    "sebagai dinding supaya pemain nggak bisa keluar. Itu keputusan",
                    "desain, jadi tulis dengan sengaja.",
                    "",
                    "Mencari petak dengan pembagian seperti ini jauh lebih murah",
                    "daripada memeriksa tabrakan dengan ribuan kotak. Phaser",
                    "menyediakannya sebagai layer.getTileAtWorldXY(x, y).",
                ],
            },
            {
                "heading": "Membuat peta dengan Tiled",
                "body": [
                    "Menyusun angka peta dengan tangan cepat melelahkan. Kebanyakan",
                    "orang memakai Tiled, editor peta gratis dan open source yang",
                    "jalan di Linux, Windows, dan macOS. Versi stabil terbarunya saat",
                    "materi ini ditulis adalah 1.12.2 (27 Mei 2026). Di Linux, Tiled",
                    "tersedia sebagai Flatpak dan AppImage resmi.",
                    "",
                    "Di Tiled kamu menggambar peta dengan kuas petak, memisahkannya",
                    "jadi beberapa layer (latar, tanah, hiasan), dan memberi petak",
                    "properti sendiri, misalnya padat = true. Hasilnya diekspor sebagai",
                    "JSON, lalu dimuat Phaser:",
                ],
                "code": """import Phaser from 'phaser';

class Level1 extends Phaser.Scene {
  constructor() {
    super('Level1');
  }

  preload() {
    this.load.image('ubin', 'aset/ubin.png');                // gambar tileset
    this.load.tilemapTiledJSON('peta1', 'aset/level1.json'); // hasil ekspor Tiled
    this.load.spritesheet('pahlawan', 'aset/pahlawan.png', { frameWidth: 32, frameHeight: 32 });
  }

  create() {
    const peta = this.make.tilemap({ key: 'peta1' });
    const tileset = peta.addTilesetImage('ubin_hutan', 'ubin'); // nama di Tiled, kunci di Phaser
    peta.createLayer('Latar', tileset);
    const tanah = peta.createLayer('Tanah', tileset);
    tanah.setCollisionByProperty({ padat: true });

    this.pemain = this.physics.add.sprite(64, 64, 'pahlawan');
    this.physics.add.collider(this.pemain, tanah);

    this.anims.create({
      key: 'lari',
      frames: this.anims.generateFrameNumbers('pahlawan', { start: 0, end: 5 }),
      frameRate: 10,
      repeat: -1,
    });
    this.anims.create({ key: 'diam', frames: [{ key: 'pahlawan', frame: 6 }] });

    const lebar = peta.widthInPixels;
    const tinggi = peta.heightInPixels;
    this.physics.world.setBounds(0, 0, lebar, tinggi);
    this.cameras.main.setBounds(0, 0, lebar, tinggi);
    this.cameras.main.startFollow(this.pemain, true, 0.1, 0.1);
  }

  update() {
    const vx = this.pemain.body.velocity.x;
    if (vx !== 0) {
      this.pemain.anims.play('lari', true); // true: jangan ulang dari awal
      this.pemain.setFlipX(vx < 0);
    } else {
      this.pemain.anims.play('diam', true);
    }
  }
}

export default Level1;""",
            },
            {
                "body": [
                    "Tiga nama di kode itu harus sama persis dengan yang ada di Tiled:",
                    "  - 'ubin_hutan' adalah nama tileset di Tiled. Argumen keduanya,",
                    "    'ubin', adalah kunci gambar yang dimuat di preload. Kalau nama",
                    "    pertama salah, addTilesetImage mengembalikan null dan layer",
                    "    nggak tergambar.",
                    "  - 'Latar' dan 'Tanah' adalah nama layer di Tiled. Huruf besar",
                    "    kecilnya ikut dibandingkan.",
                    "  - { padat: true } mencari petak yang diberi properti padat di",
                    "    Tiled. Cuma petak itu yang ikut tabrakan.",
                    "",
                    "Jebakan: Phaser nggak bisa membaca tileset eksternal (berkas .tsx",
                    "terpisah). Di konsol muncul peringatan \"External tilesets",
                    "unsupported. Use Embed Tileset and re-export\". Di Tiled, pilih",
                    "Embed Tileset, lalu ekspor ulang JSON-nya.",
                ],
            },
            {
                "heading": "Kamera: jendela ke dunia",
                "body": [
                    "Dunia levelnya lebih besar dari layar, jadi yang terlihat cuma",
                    "sebagian. Kamera adalah jendela itu. Posisinya disimpan sebagai",
                    "scroll, yaitu seberapa jauh jendela sudah bergeser dari pojok kiri",
                    "atas dunia. Koordinat di layar = koordinat di dunia - scroll.",
                    "",
                    "Kode di bawah memusatkan kamera ke pemain, tapi menahannya supaya",
                    "nggak keluar dari batas dunia:",
                ],
                "code": """const layar = { w: 320, h: 180 };
const dunia = { w: 1280, h: 360 };

function ikutiKamera(pemain) {
  // Taruh pemain di tengah layar, lalu tahan kamera di dalam batas dunia.
  let scrollX = pemain.x - layar.w / 2;
  let scrollY = pemain.y - layar.h / 2;
  scrollX = Math.max(0, Math.min(scrollX, dunia.w - layar.w));
  scrollY = Math.max(0, Math.min(scrollY, dunia.h - layar.h));
  return { scrollX, scrollY };
}

for (const pemain of [{ x: 100, y: 200 }, { x: 600, y: 200 }, { x: 1250, y: 340 }]) {
  const k = ikutiKamera(pemain);
  const diLayar = { x: pemain.x - k.scrollX, y: pemain.y - k.scrollY };
  console.log(`dunia (${pemain.x}, ${pemain.y}) scroll (${k.scrollX}, ${k.scrollY}) layar (${diLayar.x}, ${diLayar.y})`);
}""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  dunia (100, 200) scroll (0, 110) layar (100, 90)",
                    "  dunia (600, 200) scroll (440, 110) layar (160, 90)",
                    "  dunia (1250, 340) scroll (960, 180) layar (290, 160)",
                    "",
                    "Di tengah level, pemain selalu tampil di tengah layar (160, 90).",
                    "Dekat tepi kiri dan pojok kanan bawah, kamera berhenti di batas",
                    "dunia, jadi pemain bergeser dari tengah layar. Itu yang dikerjakan",
                    "setBounds di kode Phaser tadi.",
                    "",
                    "startFollow(pemain, true, 0.1, 0.1) menambahkan satu hal: lerp.",
                    "Tiap frame kamera cuma menempuh 10% sisa jarak ke posisi",
                    "tujuannya, jadi gerakannya menyusul dengan halus. Argumen true",
                    "membulatkan posisi kamera ke piksel utuh.",
                    "",
                    "Posisi klik mouse juga ikut aturan ini. pointer.x adalah",
                    "koordinat layar. Kalau kamera sudah bergeser 440 piksel, klik di",
                    "x = 160 mengenai x = 600 di dunia. Pakai pointer.worldX untuk",
                    "menembak atau memilih benda.",
                ],
            },
            {
                "heading": "Animasi dari sprite sheet",
                "body": [
                    "Animasi 2D adalah deretan gambar yang diganti cepat, seperti buku",
                    "bergambar di bab pertama. Semua frame animasi satu karakter",
                    "biasanya disimpan di satu gambar yang disebut sprite sheet.",
                    "Alasannya praktis: browser cukup memuat satu berkas, dan kartu",
                    "grafis bisa menggambar banyak sprite dari tekstur yang sama dalam",
                    "satu kelompok (batch), jadi lebih ringan. Kalau ukuran framenya",
                    "berbeda-beda, dipakai texture atlas: satu gambar ditambah berkas",
                    "JSON yang mencatat letak tiap frame. Phaser memuatnya dengan",
                    "load.atlas.",
                    "",
                    "Di kode Level1 tadi, animasi lari memakai frame 0 sampai 5 dengan",
                    "10 frame per detik, jadi satu putaran lari 0,6 detik. repeat: -1",
                    "berarti diulang terus. setFlipX(true) membalik gambarnya, jadi",
                    "satu set frame cukup untuk lari ke kanan dan ke kiri.",
                    "",
                    "Jebakan: memanggil anims.play('lari') tanpa true di update.",
                    "Animasinya diulang dari frame pertama di setiap frame, dan",
                    "karakter kelihatan membeku. Argumen true artinya \"kalau animasi",
                    "ini sudah jalan, biarkan\".",
                    "",
                    "Jebakan: garis tipis di antara petak saat kamera bergerak. Ini",
                    "terjadi waktu posisi kamera jatuh di antara dua piksel. Pasang",
                    "pixelArt: true di konfigurasi game untuk gambar piksel, bulatkan",
                    "posisi kamera, atau beri tileset jarak tambahan di tiap petak.",
                    "Phaser 4 juga punya TilemapGPULayer (createLayer dengan argumen",
                    "gpu bernilai true) yang menggambar satu layer sekaligus tanpa",
                    "sambungan.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Game platformer, game RPG yang dilihat dari atas, dan game",
                    "strategi 2D hampir selalu dibangun dari tilemap. Format Tiled",
                    "dibaca Phaser secara bawaan, dan engine lain bisa membacanya",
                    "lewat plugin atau pengimpor.",
                    "",
                    "Kasus kecil: kamu menambah level kedua dari Tiled. Begitu level",
                    "dimulai, pemain langsung jatuh menembus tanah dan hilang di bawah",
                    "layar.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Buka konsol DevTools. Kalau ada peringatan External tilesets,",
                    "     sematkan tileset-nya di Tiled lalu ekspor ulang.",
                    "  2. Cocokkan nama layer di createLayer dengan nama di Tiled,",
                    "     termasuk huruf besarnya. Layer yang namanya salah nggak",
                    "     dibuat.",
                    "  3. Pastikan petak tanah di level baru juga punya properti padat.",
                    "     Tanpa itu, setCollisionByProperty nggak menemukan apa-apa.",
                    "  4. Pastikan collider dipasang ke layer milik level baru:",
                    "       this.physics.add.collider(this.pemain, tanah);",
                    "  5. Gambar petak yang ikut tabrakan supaya kelihatan:",
                    "       tanah.renderDebug(this.add.graphics());",
                    "     Petak padat diberi warna, dan pemain harus berdiri di",
                    "     atasnya.",
                ],
            },
        ],
    },
    {
        "title": "9. State Machine untuk Karakter dan Menu",
        "sections": [
            {
                "body": [
                    "Karakter platformer bisa diam, lari, lompat, dan jatuh. Cara",
                    "pertama yang biasanya ditulis pemula adalah tumpukan if dengan",
                    "banyak penanda:",
                ],
                "code": """if (tombol.lompat && !sedangLompat && !sedangJatuh && !sedangSerang) {
  sedangLompat = true;
  ...
}
if (diTanah && sedangJatuh) {
  sedangJatuh = false;
  ...
}""",
            },
            {
                "heading": "State, transisi, dan syarat",
                "body": [
                    "Tiap penanda baru menggandakan jumlah kombinasi yang harus",
                    "dipikirkan. Lupa satu syarat, karakter bisa lompat di udara atau",
                    "memutar animasi lari sambil jatuh.",
                    "",
                    "Finite state machine (FSM) merapikannya. Karakter selalu berada di",
                    "tepat satu state dari daftar yang terbatas. Perpindahan dari satu",
                    "state ke state lain disebut transisi, dan tiap transisi punya",
                    "syarat. Semua transisi yang sah ditulis di satu tabel:",
                    "",
                    "  dari         syarat                      ke",
                    "  diam         ada input kiri atau kanan   lari",
                    "  lari         input kosong                diam",
                    "  diam, lari   lompat ditekan, di tanah    lompat",
                    "  diam, lari   nggak di tanah lagi         jatuh",
                    "  lompat       mulai turun (vy <= 0)       jatuh",
                    "  jatuh        menyentuh tanah             diam atau lari",
                    "",
                    "Yang nggak ada di tabel berarti dilarang. Jatuh ke lompat nggak",
                    "ada, jadi tombol lompat di udara diabaikan tanpa perlu if tambahan.",
                    "Lompat ke lari juga nggak ada, jadi animasi lari nggak mungkin",
                    "diputar di udara.",
                ],
            },
            {
                "heading": "State machine dengan objek",
                "body": [
                    "Di JavaScript, tiap state bisa jadi satu objek berisi dua fungsi.",
                    "masuk() jalan sekali saat state dimasuki. update() jalan tiap",
                    "frame dan mengembalikan nama state berikutnya, atau null kalau",
                    "tetap. Di contoh ini y adalah tinggi di atas tanah dan vy",
                    "kecepatan ke atas, dalam satuan per frame supaya angkanya gampang",
                    "diikuti.",
                ],
                "code": """const STATE = {
  diam: {
    masuk(k) { k.animasi = 'diam'; },
    update(k, inp) {
      if (!k.diTanah) return 'jatuh';
      if (inp.lompat) return 'lompat';
      if (inp.arah !== 0) return 'lari';
      return null; // tetap di state ini
    },
  },
  lari: {
    masuk(k) { k.animasi = 'lari'; },
    update(k, inp) {
      if (!k.diTanah) return 'jatuh';
      if (inp.lompat) return 'lompat';
      if (inp.arah === 0) return 'diam';
      return null;
    },
  },
  lompat: {
    masuk(k) { k.vy = 6; k.animasi = 'lompat'; },
    update(k) {
      return k.vy <= 0 ? 'jatuh' : null; // mulai turun: pindah ke jatuh
    },
  },
  jatuh: {
    masuk(k) { k.animasi = 'jatuh'; },
    update(k, inp) {
      if (k.diTanah) return inp.arah !== 0 ? 'lari' : 'diam';
      return null; // tombol lompat di udara diabaikan
    },
  },
};

function fisika(k) {
  k.vy -= 2; // gravitasi
  k.y = Math.max(0, k.y + k.vy);
  if (k.y === 0) k.vy = 0;
  k.diTanah = k.y === 0;
}

function gantiState(k, baru) {
  console.log(`  ${k.state} -> ${baru}`);
  k.state = baru;
  STATE[baru].masuk(k);
}

const karakter = { state: 'diam', y: 0, vy: 0, diTanah: true, animasi: 'diam' };
const masukan = [
  { arah: 1 }, { arah: 1, lompat: true }, { arah: 1 }, { arah: 1, lompat: true },
  { arah: 1 }, { arah: 1 }, { arah: 0 }, { arah: 0 },
];

masukan.forEach((inp, frame) => {
  const baru = STATE[karakter.state].update(karakter, { arah: inp.arah, lompat: !!inp.lompat });
  if (baru) gantiState(karakter, baru);
  fisika(karakter);
  console.log(`frame ${frame}: ${karakter.state}, y = ${karakter.y}, animasi ${karakter.animasi}`);
});""",
            },
            {
                "body": [
                    "Keluaran:",
                    "    diam -> lari",
                    "  frame 0: lari, y = 0, animasi lari",
                    "    lari -> lompat",
                    "  frame 1: lompat, y = 4, animasi lompat",
                    "  frame 2: lompat, y = 6, animasi lompat",
                    "  frame 3: lompat, y = 6, animasi lompat",
                    "    lompat -> jatuh",
                    "  frame 4: jatuh, y = 4, animasi jatuh",
                    "  frame 5: jatuh, y = 0, animasi jatuh",
                    "    jatuh -> diam",
                    "  frame 6: diam, y = 0, animasi diam",
                    "  frame 7: diam, y = 0, animasi diam",
                    "",
                    "Tombol lompat di frame 3 datang saat karakter masih di udara.",
                    "State lompat nggak punya transisi untuk itu, jadi tombolnya hilang",
                    "begitu saja. Di frame 5 karakter menyentuh tanah sesudah fisika",
                    "jalan, jadi state jatuh baru melihatnya di frame 6. Karena input",
                    "di frame 6 kosong, karakter mendarat ke diam, bukan ke lari.",
                ],
            },
            {
                "heading": "Aksi masuk dan keluar",
                "body": [
                    "Kecepatan lompat (vy = 6) sengaja dipasang di masuk(). Hal yang",
                    "cuma boleh terjadi sekali per transisi ditaruh di situ: memulai",
                    "animasi, memutar suara lompat, memberi dorongan awal. Kalau",
                    "ditaruh di update, suara lompat diputar ulang di setiap frame",
                    "selama karakter di udara.",
                    "",
                    "Banyak state machine juga punya keluar(), yang jalan sekali saat",
                    "state ditinggalkan. Misalnya mematikan efek debu waktu karakter",
                    "berhenti lari.",
                    "",
                    "Satu aturan lagi: paling banyak satu transisi per frame. Kalau",
                    "diam berubah ke lari lalu langsung ke lompat di frame yang sama,",
                    "aksi masuk lari jalan tanpa pernah terlihat. Urutan if di tiap",
                    "update juga menentukan prioritas. Di contoh tadi, \"nggak di",
                    "tanah\" diperiksa paling dulu, jadi karakter yang kehilangan pijakan",
                    "selalu jatuh walaupun tombol lompat sedang ditekan.",
                ],
            },
            {
                "heading": "Menu dan state bertumpuk",
                "body": [
                    "Layar menu juga state machine, seperti di bab pertama. Bedanya,",
                    "layar jeda sering perlu ditumpuk di atas permainan. Waktu jeda",
                    "ditutup, permainan harus lanjut persis dari keadaan terakhirnya.",
                    "Bentuk ini disebut state machine bertumpuk (pushdown automaton):",
                    "state disimpan di tumpukan, yang paling atas yang aktif, dan",
                    "membuang yang paling atas mengembalikan state di bawahnya.",
                    "",
                    "Di Phaser, scene bisa ditumpuk dengan cara itu:",
                ],
                "code": """import Phaser from 'phaser';

class Main extends Phaser.Scene {
  constructor() {
    super('Main');
  }

  create() {
    this.tombolJeda = this.input.keyboard.addKey('ESC');
  }

  update() {
    if (Phaser.Input.Keyboard.JustDown(this.tombolJeda)) {
      this.scene.launch('Jeda'); // tumpuk scene Jeda di atas
      this.scene.pause();        // scene ini berhenti di-update
    }
  }
}

class Jeda extends Phaser.Scene {
  constructor() {
    super('Jeda');
  }

  create() {
    this.add.text(320, 180, 'Jeda', { fontSize: '32px' }).setOrigin(0.5);
    this.input.keyboard.once('keydown-ESC', () => {
      this.scene.resume('Main'); // lanjutkan scene di bawahnya
      this.scene.stop();         // buang scene Jeda
    });
  }
}

export { Main, Jeda };""",
            },
            {
                "heading": "Coyote time, jump buffer, dan editor visual",
                "body": [
                    "Tabel transisi yang ketat kadang terasa kejam buat pemain. Dua",
                    "pengecualian yang umum di game platformer:",
                    "  - Coyote time. Pemain masih boleh lompat beberapa frame sesudah",
                    "    kakinya meninggalkan tepi pijakan. Namanya dari Wile E. Coyote",
                    "    di kartun Looney Tunes, yang sempat melayang sebentar sebelum",
                    "    jatuh dari tebing.",
                    "  - Jump buffer. Tombol lompat yang ditekan beberapa frame sebelum",
                    "    mendarat diingat, lalu dijalankan begitu kaki menyentuh tanah.",
                    "",
                    "Dua-duanya tetap ditulis sebagai transisi resmi di tabel, lengkap",
                    "dengan syarat waktunya, misalnya \"jatuh ke lompat, kalau baru",
                    "jatuh dari tepi dan belum lewat 6 frame\". Yang berubah tabelnya,",
                    "bukan if yang diselipkan di sembarang tempat.",
                    "",
                    "Engine besar punya editor visual untuk state machine animasi.",
                    "Unity memakai Animator Controller, dan Godot punya state machine",
                    "di AnimationTree. Kotak-kotak di editor itu adalah state, dan",
                    "panah di antaranya adalah transisi dengan syarat.",
                    "",
                    "Jebakan: state ditulis sebagai teks biasa, lalu salah ketik",
                    "'lompt'. Mencari nama itu di tabel state menghasilkan undefined,",
                    "dan program berhenti dengan error yang membingungkan. Periksa",
                    "nama state di gantiState(), lalu lempar error yang jelas kalau",
                    "namanya nggak terdaftar.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Karakter di Unity biasanya digerakkan Animator Controller, dan di",
                    "Godot oleh AnimationTree, dua-duanya state machine. Musuh di",
                    "banyak game juga dimulai dari state machine sederhana seperti",
                    "patroli, kejar, dan serang, yang dibahas lagi di bab AI Game dan",
                    "Pathfinding.",
                    "",
                    "Kasus kecil: penguji melapor karakter memutar animasi lari waktu",
                    "jatuh dari tepi pijakan.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tulis tabel transisi yang sekarang berlaku. Kemungkinan besar",
                    "     nggak ada baris \"lari ke jatuh kalau nggak di tanah\".",
                    "  2. Tambahkan baris itu, dan taruh pemeriksaannya paling atas di",
                    "     update() milik lari dan diam:",
                    "       if (!k.diTanah) return 'jatuh';",
                    "  3. Pastikan animasi diganti di masuk() milik jatuh, bukan di",
                    "     tempat lain.",
                    "  4. Uji tanpa layar dengan daftar input tetap: lari tiga frame,",
                    "     lalu diTanah jadi false. State harus berubah ke jatuh tepat di",
                    "     frame itu, dan animasinya ikut berubah.",
                ],
            },
        ],
    },
    {
        "title": "10. Godot: Scene Tree, Node, dan Sinyal",
        "sections": [
            {
                "body": [
                    "Di bab 01 sampai 03 kamu nulis game loop sendiri: baca input,",
                    "update, gambar, lalu ulangi. Engine game mengambil alih",
                    "pekerjaan itu. Loop-nya sudah jalan, dan kamu tinggal",
                    "menitipkan fungsi yang dipanggil engine pada saat yang tepat.",
                    "",
                    "Godot adalah engine game 2D dan 3D yang gratis dan open source",
                    "dengan lisensi MIT. Nggak ada royalti, nggak ada biaya per",
                    "pemasangan, dan nggak perlu bikin akun untuk memakainya. Versi",
                    "stabil terbaru saat materi ini ditulis (Oktober 2026) adalah",
                    "4.7.2, rilis perawatan dari Agustus 2026. Seri 4.7 sendiri",
                    "keluar Juni 2026.",
                    "",
                    "Buat pemakai Linux, Godot termasuk engine yang paling gampang",
                    "dipasang. Editornya satu berkas yang tinggal diunduh dari",
                    "godotengine.org lalu dijalankan. Di Fedora juga ada versi",
                    "Flatpak di Flathub. Game yang dibuat dengan Godot antara lain",
                    "Brotato dan Cassette Beasts.",
                ],
            },
            {
                "heading": "Node dan scene",
                "body": [
                    "Node itu potongan terkecil di Godot, dan tiap node punya satu",
                    "tugas. Sprite2D menampilkan gambar. CollisionShape2D menyimpan",
                    "bentuk untuk tabrakan. Camera2D menentukan bagian dunia yang",
                    "kelihatan di layar. Label menampilkan tulisan.",
                    "",
                    "Node disusun jadi pohon. Satu node boleh punya banyak anak,",
                    "dan tiap anak cuma punya satu induk. Pohon node yang disimpan",
                    "jadi satu berkas disebut scene. Berkasnya berakhiran .tscn dan",
                    "isinya teks biasa, jadi enak dilacak pakai git.",
                    "",
                    "Scene bisa dipasang di dalam scene lain. Kamu bikin scene",
                    "Player sekali, lalu memasangnya di Level1, Level2, dan",
                    "seterusnya. Scene Musuh boleh dipasang dua puluh kali di satu",
                    "level. Kalau scene Musuh diubah, semua salinannya ikut berubah.",
                    "",
                    "Di bawah ini scene utama sebuah game 2D kecil. Teks di dalam",
                    "kurung adalah jenis node, dan nama berkas di kanan adalah",
                    "skrip yang ditempel ke node itu.",
                ],
                "bahasa": "teks",
                "code": """Main (Node2D)                    main.gd
├── Player (CharacterBody2D)     player.gd
│   ├── Sprite2D
│   ├── CollisionShape2D
│   └── Camera2D
└── PanelNyawa (CanvasLayer)     panel_nyawa.gd
    └── Label""",
            },
            {
                "heading": "Siapa dipanggil duluan",
                "body": [
                    "Godot memanggil beberapa fungsi khusus di skripmu. Namanya",
                    "selalu diawali garis bawah:",
                    "",
                    "  - _ready() dipanggil sekali, waktu node dan semua anaknya",
                    "    sudah masuk ke pohon. Anak selalu siap lebih dulu",
                    "    daripada induknya.",
                    "  - _process(delta) dipanggil tiap frame layar. delta adalah",
                    "    lama frame sebelumnya dalam detik, sama dengan delta time",
                    "    di bab 01.",
                    "  - _physics_process(delta) dipanggil dengan laju tetap,",
                    "    bawaannya 60 kali per detik. Ini fixed timestep dari bab",
                    "    01, tempat yang pas untuk gerak dan tabrakan.",
                    "",
                    "Di scene contoh tadi, urutan _ready-nya Sprite2D,",
                    "CollisionShape2D, Camera2D, Player, Label, PanelNyawa, lalu Main",
                    "paling akhir. Aturan anak dulu ini ada gunanya. Waktu _ready",
                    "milik Player jalan, kamu boleh langsung memakai $Sprite2D,",
                    "karena anak itu dijamin sudah siap.",
                    "",
                    "Tanda $ adalah singkatan get_node(). $Sprite2D artinya anak",
                    "bernama Sprite2D. $\"../PanelNyawa\" artinya saudara bernama PanelNyawa,",
                    "karena .. berarti naik satu tingkat ke induk.",
                    "",
                    "Skrip player.gd di bawah memakai move_and_slide(). Fungsi itu",
                    "sudah memakai delta sendiri, jadi kecepatannya nggak perlu",
                    "dikali delta lagi. Parameternya ditulis _delta supaya Godot",
                    "nggak memberi peringatan parameter yang nggak dipakai.",
                ],
                "bahasa": "gdscript",
                "code": """# player.gd, ditempel ke node Player
extends CharacterBody2D

signal terluka(sisa_nyawa: int)

@export var kecepatan: float = 200.0
var nyawa := 3

func _ready() -> void:
    # Anak-anak Player sudah siap di sini.
    $Sprite2D.modulate = Color.WHITE

func _physics_process(_delta: float) -> void:
    var arah := Input.get_vector("ui_left", "ui_right", "ui_up", "ui_down")
    velocity = arah * kecepatan
    move_and_slide()

func kena_serang() -> void:
    nyawa -= 1
    terluka.emit(nyawa)""",
            },
            {
                "heading": "Sinyal",
                "body": [
                    "Sinyal adalah cara node mengumumkan bahwa sesuatu terjadi,",
                    "tanpa perlu tahu siapa yang mendengarkan. Mirip pengumuman di",
                    "stasiun: petugas cukup bilang kereta ke Bandung sudah tiba,",
                    "dan siapa pun yang berkepentingan bereaksi sendiri.",
                    "",
                    "Di player.gd tadi, baris signal terluka(sisa_nyawa: int)",
                    "membuat sinyal baru, dan terluka.emit(nyawa) memancarkannya.",
                    "Node bawaan juga punya sinyal. Button punya pressed, Timer",
                    "punya timeout, dan Area2D punya body_entered.",
                    "",
                    "Sinyal bisa dihubungkan lewat editor (tab Node, lalu Signals)",
                    "atau lewat kode dengan connect(). Satu sinyal boleh punya",
                    "banyak penerima, dan semuanya dipanggil berurutan sesuai",
                    "urutan connect.",
                    "",
                    "Pegangan yang sering dipakai komunitas Godot: panggil ke",
                    "bawah, sinyal ke atas. Induk boleh memanggil fungsi anaknya",
                    "langsung, karena induk memang kenal anak-anaknya. Anak cukup",
                    "memancarkan sinyal, dan induk yang menentukan siapa yang perlu",
                    "tahu. Contoh di bawah menghubungkan Player ke PanelNyawa dari skrip",
                    "Main, induk keduanya.",
                ],
                "bahasa": "gdscript",
                "code": """# main.gd, ditempel ke node Main
extends Node2D

func _ready() -> void:
    # Main siap paling akhir, jadi Player dan PanelNyawa pasti sudah ada.
    $Player.terluka.connect($PanelNyawa.tampilkan_nyawa)


# panel_nyawa.gd, ditempel ke node PanelNyawa
extends CanvasLayer

func tampilkan_nyawa(sisa: int) -> void:
    $Label.text = "Nyawa: %d" % sisa""",
            },
            {
                "heading": "Tiruan kecil di JavaScript",
                "body": [
                    "Supaya urutannya kelihatan, ini tiruan pohon node dan sinyal",
                    "di JavaScript. Bentuk pohonnya sama dengan scene contoh tadi.",
                    "Godot tentu jauh lebih rumit, tapi dua aturannya sama: _ready",
                    "berjalan dari anak ke induk, dan emit memanggil penerima",
                    "sesuai urutan connect.",
                ],
                "code": """// Tiap node punya nama, anak, dan daftar penerima sinyal.
function node(nama, ...anak) {
  return { nama, anak, penerima: {} };
}

const pemain = node("Player", node("Sprite2D"), node("CollisionShape2D"),
  node("Camera2D"));
const hud = node("PanelNyawa", node("Label"));
const main = node("Main", pemain, hud);

// _ready dipanggil sesudah semua anaknya siap.
function siapkan(n) {
  for (const a of n.anak) siapkan(a);
  console.log("_ready " + n.nama);
}
siapkan(main);

// Sinyal = daftar fungsi yang dipanggil berurutan saat emit.
function connect(n, sinyal, fungsi) {
  if (!n.penerima[sinyal]) n.penerima[sinyal] = [];
  n.penerima[sinyal].push(fungsi);
}
function emit(n, sinyal, ...isi) {
  for (const f of n.penerima[sinyal] || []) f(...isi);
}

connect(pemain, "terluka", (sisa) => console.log("PanelNyawa: nyawa tinggal " + sisa));
connect(pemain, "terluka", () => console.log("Kamera: layar bergetar"));
emit(pemain, "terluka", 2);
emit(pemain, "melompat");""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  _ready Sprite2D",
                    "  _ready CollisionShape2D",
                    "  _ready Camera2D",
                    "  _ready Player",
                    "  _ready Label",
                    "  _ready PanelNyawa",
                    "  _ready Main",
                    "  PanelNyawa: nyawa tinggal 2",
                    "  Kamera: layar bergetar",
                    "",
                    "Baris emit(pemain, \"melompat\") nggak mencetak apa pun, karena",
                    "belum ada yang terhubung ke sinyal itu. Di Godot juga begitu.",
                    "Memancarkan sinyal tanpa penerima bukan kesalahan, jadi Godot",
                    "nggak memberi tahu apa-apa.",
                ],
            },
            {
                "heading": "Tutorial lama dan jebakan lain",
                "body": [
                    "Banyak tutorial di internet masih ditulis untuk Godot 3, dan",
                    "kodenya nggak jalan di Godot 4. Tandanya gampang dikenali:",
                    "",
                    "  Godot 3                          Godot 4",
                    "  KinematicBody2D, Sprite          CharacterBody2D, Sprite2D",
                    "  export var kecepatan = 200       @export var kecepatan = 200",
                    "  onready var label = $Label       @onready var label = $Label",
                    "  yield(timer, \"timeout\")          await timer.timeout",
                    "  connect(\"hit\", self, \"_on_hit\")  hit.connect(_on_hit)",
                    "",
                    "Seri 3 masih dirawat untuk proyek lama. Rilis terakhirnya",
                    "3.6.3 dari Agustus 2026. Proyek baru sebaiknya langsung",
                    "memakai seri 4.",
                    "",
                    "Jebakan: $\"../PanelNyawa/Label\" putus begitu ada node yang diganti",
                    "nama atau dipindah. Godot baru memberi tahu lewat galat Node",
                    "not found waktu baris itu dijalankan. Untuk node yang sering",
                    "kamu akses, klik kanan node itu lalu pilih Access as Unique",
                    "Name, kemudian akses dengan %Label. Cara itu tetap jalan",
                    "walaupun letak node berpindah di dalam scene yang sama.",
                    "",
                    "Ingat: queue_free() menghapus node di akhir frame. Di sisa",
                    "frame itu node-nya masih ada dan masih bisa dibaca kode lain.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Godot sering dipakai di game jam, lomba bikin game dalam 48",
                    "jam atau seminggu. Editornya kecil dan gratis. Karena tiap",
                    "scene berupa berkas teks, dua orang bisa mengerjakan scene",
                    "yang berbeda lalu menggabungkannya lewat git tanpa banyak",
                    "konflik.",
                    "",
                    "Kasus kecil: di game temanmu, label di PanelNyawa tetap menulis",
                    "Nyawa: 3 walaupun pemain sudah kena serang dua kali. Jendela",
                    "Output juga nggak menampilkan galat apa pun.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pastikan sinyalnya memang dipancarkan. Taruh",
                    "     print(\"emit \", nyawa) tepat sebelum terluka.emit(nyawa),",
                    "     lalu biarkan pemain kena serang.",
                    "  2. Kalau print-nya muncul, masalahnya di koneksi. Cari baris",
                    "     connect(), atau buka tab Node lalu Signals di node Player.",
                    "     Sinyal yang nggak terhubung ke mana pun nggak menimbulkan",
                    "     galat, jadi kesalahan ini nggak kelihatan di Output.",
                    "  3. Tulis connect() di _ready milik Main. Main siap paling",
                    "     akhir, jadi Player dan PanelNyawa pasti sudah ada:",
                    "      $Player.terluka.connect($PanelNyawa.tampilkan_nyawa)",
                    "  4. Kalau label masih diam, cek jalur $Label di panel_nyawa.gd. Node",
                    "     yang diganti nama bikin jalurnya putus, dan galat Node",
                    "     not found baru muncul waktu fungsinya dipanggil.",
                ],
            },
        ],
    },
    {
        "title": "11. GDScript untuk Pelajar JavaScript dan Python",
        "sections": [
            {
                "body": [
                    "GDScript adalah bahasa skrip buatan Godot sendiri. Bentuknya",
                    "mirip Python: blok ditandai indentasi, fungsi ditulis dengan",
                    "func, dan nggak ada titik koma. Bedanya, GDScript dibuat",
                    "khusus untuk engine. Vektor, warna, node, dan sinyal sudah",
                    "jadi bagian dari bahasanya.",
                    "",
                    "Dalam Survei Stack Overflow 2025, 3,3% responden bilang",
                    "memakai GDScript. Angkanya kecil dibanding JavaScript atau",
                    "Python, dan itu wajar, karena GDScript cuma dipakai di satu",
                    "engine.",
                    "",
                    "Kalau kamu sudah menyelesaikan kurikulum JavaScript atau",
                    "Python, kamu nggak perlu belajar dari nol. Materi ini fokus ke",
                    "bagian yang beda, terutama yang sering bikin pindahan dari JS",
                    "dan Python tersandung.",
                ],
            },
            {
                "heading": "Satu skrip, satu node",
                "body": [
                    "Tiap berkas .gd adalah satu kelas. Baris extends di paling",
                    "atas menyebut jenis node yang ditempeli skrip itu. Skrip yang",
                    "extends CharacterBody2D otomatis punya velocity dan",
                    "move_and_slide(), karena semua milik CharacterBody2D ikut",
                    "diwariskan.",
                    "",
                    "Kalau kamu menambah class_name, kelas itu bisa dipakai dari",
                    "skrip lain dengan namanya, mirip class yang diekspor di",
                    "JavaScript.",
                    "",
                    "Contoh di bawah adalah skrip musuh sederhana. Baca pelan-pelan,",
                    "dan perhatikan komentar yang membandingkannya dengan JS dan",
                    "Python.",
                ],
                "bahasa": "gdscript",
                "code": """class_name Musuh
extends CharacterBody2D

signal mati(hadiah_koin: int)

const KECEPATAN_KEJAR := 120.0     # konstanta, seperti const di JS
@export var nyawa_maks: int = 5    # muncul di panel Inspector
@export var hadiah_koin := 10      # := menebak tipe dari nilainya

var nyawa: int
var target: Node2D = null          # null, sama seperti di JS

func _ready() -> void:
    nyawa = nyawa_maks
    add_to_group("musuh")

func kena(damage: int) -> void:
    nyawa -= damage                # nyawa-- tidak ada di GDScript
    if nyawa <= 0:
        mati.emit(hadiah_koin)
        queue_free()
    elif nyawa < nyawa_maks / 2:   # 5 / 2 hasilnya 2, tidak 2.5
        $Sprite2D.modulate = Color.RED

func _physics_process(_delta: float) -> void:
    if target == null:
        return
    var arah := global_position.direction_to(target.global_position)
    velocity = arah * KECEPATAN_KEJAR
    move_and_slide()""",
            },
            {
                "heading": "Yang mirip dan yang beda",
                "body": [
                    "Tabel ini membandingkan hal sehari-hari di tiga bahasa:",
                    "",
                    "  Hal              JavaScript         Python         GDScript",
                    "  blok             { ... }            indentasi      indentasi",
                    "  variabel         let x = 1          x = 1          var x = 1",
                    "  fungsi           function f(a) {}   def f(a):      func f(a):",
                    "  benar, salah     true, false        True, False    true, false",
                    "  kosong           null, undefined    None           null",
                    "  logika           && || !            and or not     dua-duanya",
                    "  tambah satu      x++                x += 1         x += 1",
                    "  5 / 2            2.5                2.5            2",
                    "  \"a\" + 1          \"a1\"               TypeError      galat",
                    "  cetak \"a\" dan 1  a 1                a 1            a1",
                    "",
                    "Empat baris terakhir yang paling sering bikin pindahan",
                    "tersandung:",
                    "",
                    "  1. Pembagian dua bilangan bulat hasilnya bilangan bulat.",
                    "     5 / 2 hasilnya 2, sisanya dibuang. Kalau butuh pecahan,",
                    "     salah satunya harus float: 5 / 2.0 atau float(5) / 2.",
                    "  2. Nggak ada ++ dan --. Tulis nyawa += 1 atau nyawa -= 1.",
                    "  3. Teks dan angka nggak bisa langsung dijumlah.",
                    "     \"Nyawa: \" + 3 bikin galat. Pakai str(3), atau format",
                    "     \"Nyawa: %d\" % 3.",
                    "  4. print() menempelkan argumennya tanpa spasi.",
                    "     print(\"skor\", 10) mencetak skor10, sedangkan JS dan",
                    "     Python mencetak skor 10.",
                    "",
                    "Satu lagi buat pindahan dari JavaScript. Fungsi yang disimpan",
                    "di variabel dipanggil lewat .call(). Kalau kamu menulis",
                    "var kali_dua = func(x): return x * 2, panggilannya",
                    "kali_dua.call(4), hasilnya 8. Menulis kali_dua(4) bikin galat.",
                    "",
                    "Editor Godot memakai tab untuk indentasi. Spasi juga sah,",
                    "asal nggak dicampur dengan tab di satu berkas.",
                ],
            },
            {
                "heading": "Tipe opsional dan @export",
                "body": [
                    "Di GDScript, tipe boleh ditulis, boleh juga nggak. Tiga baris",
                    "ini sama-sama sah:",
                    "",
                    "  var kecepatan = 200.0          tanpa tipe, mirip JS dan Python",
                    "  var kecepatan: float = 200.0   tipe ditulis jelas",
                    "  var kecepatan := 200.0         tipe ditebak dari nilainya",
                    "",
                    "Menulis tipe ada untungnya. Editor bisa melengkapi nama fungsi",
                    "dengan tepat, dan salah ketik ketahuan sebelum game",
                    "dijalankan. Dokumentasi Godot juga menyebut kode bertipe bisa",
                    "jalan sedikit lebih cepat. Banyak tim mewajibkan tipe di",
                    "proyek besar, dan Godot punya setelan peringatan untuk",
                    "variabel yang ditulis tanpa tipe.",
                    "",
                    "@export memunculkan variabel di panel Inspector. Desainer bisa",
                    "mengubah kecepatan musuh atau nyawa bos tanpa membuka kode,",
                    "dan tiap salinan scene boleh punya nilai sendiri. Nilai yang",
                    "diisi di Inspector menimpa nilai awal di skrip.",
                    "",
                    "Jebakan: kamu mengubah @export var nyawa_maks = 5 jadi 8 di",
                    "skrip, tapi musuh di level tetap punya 5 nyawa. Penyebabnya,",
                    "nilai di Inspector untuk salinan itu sudah pernah diubah, jadi",
                    "nilai di skrip kalah. Tombol panah melingkar di sebelah kolom",
                    "Inspector mengembalikannya ke nilai skrip.",
                ],
            },
            {
                "heading": "GDScript atau C#",
                "body": [
                    "Godot juga mendukung C#. Kamu perlu mengunduh versi editor",
                    "khusus yang namanya Godot .NET, plus .NET SDK di komputermu.",
                    "Kalau kamu sudah menyelesaikan kurikulum C# atau pindahan dari",
                    "Unity, C# akan terasa akrab.",
                    "",
                    "Ada batasnya. Menurut dokumentasi Godot 4.7, proyek C# bisa",
                    "diekspor ke Windows, Linux, dan macOS, sedangkan Android dan",
                    "iOS masih berstatus eksperimental. Proyek C# juga belum bisa",
                    "diekspor ke web. Kalau kamu ingin gamemu bisa dimainkan",
                    "langsung di browser, misalnya di itch.io, pilih GDScript.",
                    "",
                    "  Pertimbangan            GDScript            C#",
                    "  pasang tambahan         tidak perlu         Godot .NET, .NET SDK",
                    "  ekspor ke web           bisa                belum bisa",
                    "  Android dan iOS         stabil              eksperimental",
                    "  tutorial komunitas      paling banyak       lebih sedikit",
                    "  cocok untuk             kebanyakan proyek   tim yang sudah C#",
                    "",
                    "Untuk bagian yang butuh kecepatan tinggi, misalnya simulasi",
                    "ribuan objek, Godot menyediakan GDExtension. Isinya kode C++",
                    "(atau bahasa lain yang punya binding) yang dimuat sebagai",
                    "pustaka. Game pertama jarang butuh ini.",
                    "",
                    "Ini musuh yang sama dalam C#. Kelasnya wajib partial, karena",
                    "Godot membuat potongan kelas lainnya secara otomatis. Sinyal",
                    "ditulis sebagai delegate yang namanya berakhiran",
                    "EventHandler.",
                ],
                "bahasa": "csharp",
                "code": """using Godot;

public partial class Musuh : CharacterBody2D
{
    [Signal]
    public delegate void MatiEventHandler(int hadiahKoin);

    [Export]
    public int NyawaMaks { get; set; } = 5;

    private int _nyawa;

    public override void _Ready()
    {
        _nyawa = NyawaMaks;
    }

    public void Kena(int damage)
    {
        _nyawa -= damage;
        if (_nyawa <= 0)
        {
            EmitSignal(SignalName.Mati, 10);
            QueueFree();
        }
    }
}""",
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Banyak game Godot dimulai dari prototipe kecil, kadang di",
                    "bahasa lain, lalu dipindah ke GDScript waktu ide permainannya",
                    "terbukti seru. Kesalahan yang paling sering muncul saat",
                    "memindahkan justru datang dari aturan kecil di tabel tadi.",
                    "",
                    "Kasus kecil: kamu memindahkan bar nyawa dari prototipe",
                    "JavaScript ke Godot. Rumusnya persis sama:",
                    "var persen = nyawa / nyawa_maks * 100. Di JavaScript barnya",
                    "turun pelan-pelan. Di Godot barnya langsung 0% begitu pemain",
                    "kena serang sekali, dan baru 100% lagi waktu nyawanya penuh.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Cetak nilainya. Ingat, print() nggak memberi spasi:",
                    "      print(nyawa, \" \", nyawa_maks, \" \", persen)",
                    "     Untuk nyawa 4 dari 5, yang tercetak 4 5 0.",
                    "  2. Cari penyebabnya. nyawa dan nyawa_maks sama-sama int,",
                    "     jadi 4 / 5 hasilnya 0, dan 0 * 100 tetap 0.",
                    "  3. Jadikan salah satunya float sebelum dibagi:",
                    "      var persen := float(nyawa) / nyawa_maks * 100.0",
                    "  4. Supaya nggak terulang, tulis tipenya: var persen: float.",
                    "     Editor juga menandai pembagian bilangan bulat dengan",
                    "     peringatan, jadi biasakan membaca panel peringatan itu.",
                ],
            },
        ],
    },
    {
        "title": "12. Unity: GameObject, Component, dan Siklus Update",
        "sections": [
            {
                "body": [
                    "Unity adalah engine game 2D dan 3D yang paling banyak dipakai",
                    "untuk game ponsel. Pokemon GO dan Genshin Impact dibuat dengan",
                    "Unity, begitu juga banyak game indie dan aplikasi VR. Skripnya",
                    "ditulis dalam C#, jadi kurikulum C# di aplikasi ini bekal yang",
                    "pas. Dalam Survei Stack Overflow 2024, 5,9% responden menyebut",
                    "memakai Unity.",
                    "",
                    "Nomor versi Unity agak membingungkan. Saat materi ini ditulis",
                    "(Oktober 2026), rilis LTS terbarunya Unity 6.3, yang nomor",
                    "teknisnya 6000.3. LTS (long-term support) artinya didukung dua",
                    "tahun, dan 6.3 LTS didukung sampai Desember 2027. Di antara dua",
                    "LTS ada rilis Supported, misalnya 6.6, yang membawa fitur baru",
                    "tapi cuma didukung sampai rilis berikutnya keluar. Untuk",
                    "belajar dan untuk proyek yang mau dirilis, pilih LTS.",
                ],
            },
            {
                "heading": "GameObject dan komponen",
                "body": [
                    "Semua benda di scene Unity adalah GameObject: pemain, musuh,",
                    "kamera, lampu, bahkan objek kosong yang cuma jadi wadah.",
                    "GameObject sendiri nggak bisa apa-apa. Kemampuannya datang",
                    "dari komponen yang ditempelkan ke dia.",
                    "",
                    "Tiap GameObject selalu punya komponen Transform, yang",
                    "menyimpan posisi, rotasi, dan skala. Sisanya kamu tambahkan",
                    "sesuai kebutuhan. SpriteRenderer supaya kelihatan,",
                    "Rigidbody2D supaya kena gravitasi, BoxCollider2D supaya bisa",
                    "bertabrakan, AudioSource supaya bisa bersuara.",
                    "",
                    "Bayangkan papan kosong yang bisa ditempeli stiker. Papannya",
                    "GameObject, stikernya komponen. Musuh terbang dan musuh",
                    "berjalan bisa memakai stiker yang sama, dan bedanya cuma satu",
                    "stiker: skrip geraknya.",
                    "",
                    "Di jendela Hierarchy, GameObject tersusun jadi pohon, mirip",
                    "node di Godot. Anak ikut bergerak waktu induknya bergerak. Di",
                    "bawah ini contoh isi Hierarchy, dengan komponen tiap objek di",
                    "dalam kurung siku.",
                ],
                "bahasa": "teks",
                "code": """Main Camera   [Transform, Camera, IkutiPemain]
Pemain        [Transform, SpriteRenderer, Rigidbody2D,
               BoxCollider2D, KendaliPemain]
  Senter      [Transform, Light2D]
Musuh         [Transform, SpriteRenderer, Rigidbody2D,
               CircleCollider2D, Patroli]
Lantai        [Transform, SpriteRenderer, BoxCollider2D]
Awan          [Transform, SpriteRenderer, GeserAwan]""",
            },
            {
                "heading": "Skrip juga komponen",
                "body": [
                    "Skripmu sendiri ditempel sebagai komponen. Kelasnya mewarisi",
                    "MonoBehaviour, dan Unity memanggil fungsi-fungsi tertentu di",
                    "kelas itu pada saat yang sudah ditentukan. Kamu nggak pernah",
                    "memanggil Update() sendiri.",
                    "",
                    "Field yang public atau diberi [SerializeField] muncul di panel",
                    "Inspector. Kecepatan awan di bawah bisa diubah dari editor",
                    "tanpa menyentuh kode, sama seperti @export di Godot. Awan nggak",
                    "punya Rigidbody, jadi boleh digeser langsung lewat transform.",
                ],
                "bahasa": "csharp",
                "code": """using UnityEngine;

public class GeserAwan : MonoBehaviour
{
    [SerializeField] private float kecepatan = 1.5f;
    [SerializeField] private float batasKanan = 12f;
    private SpriteRenderer gambar;

    void Awake()
    {
        // Ambil komponen sekali saja, lalu simpan di field.
        gambar = GetComponent<SpriteRenderer>();
        gambar.sortingOrder = -10;   // awan selalu di belakang
    }

    void Start()
    {
        Debug.Log(name + " mulai di x = " + transform.position.x);
    }

    void Update()
    {
        // Time.deltaTime: lama frame sebelumnya, dalam detik.
        transform.Translate(Vector3.right * kecepatan * Time.deltaTime);
        if (transform.position.x > batasKanan)
        {
            transform.position = new Vector3(-batasKanan, transform.position.y, 0f);
        }
    }
}""",
            },
            {
                "heading": "Urutan panggilannya",
                "body": [
                    "Untuk satu skrip, urutannya selalu begini:",
                    "",
                    "  1. Awake() dipanggil sekali, paling awal, waktu skripnya",
                    "     dimuat. Ini juga langsung terjadi kalau komponennya",
                    "     ditambah lewat AddComponent di tengah permainan.",
                    "  2. OnEnable() dipanggil tiap kali komponennya diaktifkan.",
                    "  3. Start() dipanggil sekali, tepat sebelum Update()",
                    "     pertamanya.",
                    "  4. FixedUpdate() dipanggil nol, satu, atau beberapa kali per",
                    "     frame, mengikuti langkah fisika yang tetap. Ini dibahas di",
                    "     materi berikutnya.",
                    "  5. Update() dipanggil sekali tiap frame.",
                    "  6. LateUpdate() dipanggil sesudah semua Update() di frame itu",
                    "     selesai. Kamera yang mengikuti pemain biasa ditaruh di",
                    "     sini, supaya pemainnya sudah selesai bergerak.",
                    "  7. OnDestroy() dipanggil waktu objeknya dihancurkan.",
                    "",
                    "Pembagian Awake dan Start ada gunanya. Pakai Awake untuk",
                    "menyiapkan dirimu sendiri, misalnya mengambil komponen. Pakai",
                    "Start untuk hal yang butuh objek lain, karena waktu Start",
                    "jalan, Awake semua objek di scene sudah selesai.",
                    "",
                    "Jebakan: dokumentasi Unity terang-terangan bilang kamu nggak",
                    "bisa mengandalkan urutan fungsi yang sama di GameObject yang",
                    "berbeda. Update milik Pemain bisa jalan sebelum atau sesudah",
                    "Update milik Musuh. Kalau urutannya penting, pakai LateUpdate",
                    "atau atur Script Execution Order di Project Settings.",
                    "",
                    "Destroy(gameObject) juga nggak langsung menghapus. Objeknya",
                    "baru dihancurkan sesudah putaran Update yang sedang berjalan",
                    "selesai, sebelum frame itu digambar.",
                ],
            },
            {
                "heading": "Tiruan urutan di JavaScript",
                "body": [
                    "Tiruan kecil ini meniru cara Unity memanggil skrip selama dua",
                    "frame. Komponen Musuh.Patroli dipasang di antara frame 1 dan",
                    "frame 2, seperti objek yang muncul di tengah permainan.",
                ],
                "code": """// Tiruan kecil cara Unity memanggil skrip. Bukan kode Unity sungguhan.
const semua = [];

function pasang(objek, skrip) {
  const k = { nama: objek + "." + skrip, sudahStart: false };
  semua.push(k);
  console.log(k.nama + " Awake");   // AddComponent langsung memanggil Awake
}

function frame(nomor) {
  console.log("-- frame " + nomor);
  for (const k of semua) {
    if (!k.sudahStart) {
      console.log(k.nama + " Start");
      k.sudahStart = true;
    }
  }
  for (const k of semua) console.log(k.nama + " Update");
  for (const k of semua) console.log(k.nama + " LateUpdate");
}

pasang("Pemain", "Gerak");
pasang("Kamera", "Ikuti");
frame(1);
pasang("Musuh", "Patroli");
frame(2);""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  Pemain.Gerak Awake",
                    "  Kamera.Ikuti Awake",
                    "  -- frame 1",
                    "  Pemain.Gerak Start",
                    "  Kamera.Ikuti Start",
                    "  Pemain.Gerak Update",
                    "  Kamera.Ikuti Update",
                    "  Pemain.Gerak LateUpdate",
                    "  Kamera.Ikuti LateUpdate",
                    "  Musuh.Patroli Awake",
                    "  -- frame 2",
                    "  Musuh.Patroli Start",
                    "  Pemain.Gerak Update",
                    "  Kamera.Ikuti Update",
                    "  Musuh.Patroli Update",
                    "  Pemain.Gerak LateUpdate",
                    "  Kamera.Ikuti LateUpdate",
                    "  Musuh.Patroli LateUpdate",
                    "",
                    "Awake milik Musuh.Patroli langsung jalan begitu dipasang.",
                    "Start-nya menunggu frame 2, tepat sebelum Update pertamanya.",
                    "Di tiruan ini urutan antarobjek mengikuti urutan pemasangan,",
                    "supaya hasilnya bisa ditebak. Di Unity sungguhan urutan itu",
                    "nggak dijamin.",
                ],
            },
            {
                "heading": "Prefab",
                "body": [
                    "Prefab adalah GameObject yang disimpan jadi berkas cetakan,",
                    "lengkap dengan komponen dan nilai-nilainya. Musuh, peluru,",
                    "dan koin biasanya dibuat sebagai prefab. Kamu boleh memasang",
                    "satu prefab berkali-kali di scene. Kalau prefab-nya diubah,",
                    "semua salinan ikut berubah, mirip scene yang dipasang di scene",
                    "lain pada Godot.",
                    "",
                    "Prefab juga bisa dimunculkan saat game berjalan dengan",
                    "Instantiate. Skrip di bawah memunculkan musuh tiap dua detik.",
                    "Quaternion adalah cara Unity menyimpan rotasi, dan",
                    "Quaternion.identity artinya tanpa rotasi.",
                    "",
                    "Kolom prefabMusuh diisi dengan menyeret berkas prefab ke",
                    "Inspector. Kalau lupa diisi, Unity melempar",
                    "UnassignedReferenceException waktu baris Instantiate jalan.",
                ],
                "bahasa": "csharp",
                "code": """using UnityEngine;

public class PemunculMusuh : MonoBehaviour
{
    [SerializeField] private GameObject prefabMusuh;
    [SerializeField] private float jeda = 2f;
    private float waktu;

    void Update()
    {
        waktu += Time.deltaTime;
        if (waktu >= jeda)
        {
            waktu -= jeda;
            Instantiate(prefabMusuh, transform.position, Quaternion.identity);
        }
    }
}""",
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Game ponsel kasual, misalnya game teka-teki atau game lari",
                    "tanpa akhir, banyak yang dibuat dengan Unity. Pola GameObject",
                    "dan komponen bikin satu tim bisa berbagi kerja. Programmer",
                    "menulis komponen, sedangkan desainer menyusun prefab dan",
                    "mengatur angkanya di Inspector.",
                    "",
                    "Kasus kecil: kamera yang mengikuti pemain kelihatan bergetar",
                    "halus waktu pemain berlari. Kodenya cuma satu baris di",
                    "Update() milik skrip kamera:",
                    "transform.position = pemain.position + jarak.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Ingat bahwa urutan Update antar-GameObject nggak dijamin.",
                    "     Di sebagian frame kamera bergerak lebih dulu, jadi dia",
                    "     memakai posisi pemain dari frame sebelumnya.",
                    "  2. Pindahkan baris itu ke LateUpdate(), yang selalu jalan",
                    "     sesudah semua Update selesai:",
                    "      void LateUpdate() { transform.position = pemain.position + jarak; }",
                    "  3. Kalau pemain digerakkan fisika (Rigidbody2D), getaran juga",
                    "     bisa datang dari beda laju fisika dan laju frame. Pilih",
                    "     Interpolate di kolom Interpolation pada Rigidbody2D pemain.",
                    "  4. Uji lagi di laju frame yang berbeda, misalnya di ponsel",
                    "     lama, karena masalah urutan sering cuma muncul di",
                    "     perangkat tertentu.",
                ],
            },
        ],
    },
    {
        "title": "13. Fisika Unity: Rigidbody, Collider, dan FixedUpdate",
        "sections": [
            {
                "body": [
                    "Di bab 02 kamu menghitung tabrakan kotak sendiri. Di Unity,",
                    "pekerjaan itu diambil alih mesin fisika. Untuk 3D Unity",
                    "memakai PhysX buatan NVIDIA, dan untuk 2D Unity memakai Box2D.",
                    "Kamu cukup bilang benda mana yang ikut fisika dan bentuknya",
                    "seperti apa, lalu menanggapi kejadian tabrakannya.",
                ],
            },
            {
                "heading": "Collider dan Rigidbody",
                "body": [
                    "Collider adalah bentuk tak terlihat yang dipakai untuk",
                    "menghitung tabrakan: BoxCollider2D (kotak), CircleCollider2D",
                    "(lingkaran), CapsuleCollider2D (kapsul), dan versi 3D-nya.",
                    "Collider saja sudah cukup untuk benda yang diam, seperti",
                    "lantai dan dinding.",
                    "",
                    "Rigidbody membuat benda ikut aturan fisika: jatuh kena",
                    "gravitasi, terdorong, dan berputar. Rigidbody2D punya tiga",
                    "jenis tubuh (Body Type):",
                    "",
                    "  - Dynamic: digerakkan sepenuhnya oleh fisika. Cocok untuk",
                    "    pemain platformer, bola, atau peti yang bisa didorong.",
                    "  - Kinematic: nggak kena gravitasi dan nggak terdorong. Kamu",
                    "    yang menggerakkannya lewat kode, misalnya lantai yang naik",
                    "    turun.",
                    "  - Static: nggak bergerak sama sekali.",
                    "",
                    "Di Rigidbody versi 3D, padanan Kinematic adalah centang",
                    "Is Kinematic.",
                ],
            },
            {
                "heading": "Kenapa fisika ditaruh di FixedUpdate",
                "body": [
                    "Mesin fisika maju dengan langkah waktu yang tetap. Bawaannya",
                    "0,02 detik, artinya 50 langkah per detik, dan angkanya bisa",
                    "diubah di Project Settings, bagian Time. Ini persis fixed",
                    "timestep dan akumulator dari bab 01.",
                    "",
                    "FixedUpdate() dipanggil sebelum tiap langkah fisika. Lama",
                    "frame layar naik turun, jadi dalam satu frame FixedUpdate bisa",
                    "jalan nol, satu, atau dua kali. Tiruan di bawah memakai jam",
                    "palsu dalam milidetik supaya hasilnya selalu sama.",
                ],
                "code": """// Fixed Timestep bawaan Unity 0,02 detik = 20 ms.
// Durasi frame dibuat tetap (jam palsu) supaya hasilnya selalu sama.
const LANGKAH = 20;
const durasiFrame = [16, 16, 33, 50, 8];

let akumulator = 0;
durasiFrame.forEach((dt, i) => {
  akumulator += dt;
  let fixed = 0;
  while (akumulator >= LANGKAH) {
    akumulator -= LANGKAH;
    fixed++;
  }
  console.log(`frame ${i + 1} (${dt} ms): FixedUpdate ${fixed}x, ` +
    `Update 1x, sisa ${akumulator} ms`);
});""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  frame 1 (16 ms): FixedUpdate 0x, Update 1x, sisa 16 ms",
                    "  frame 2 (16 ms): FixedUpdate 1x, Update 1x, sisa 12 ms",
                    "  frame 3 (33 ms): FixedUpdate 2x, Update 1x, sisa 5 ms",
                    "  frame 4 (50 ms): FixedUpdate 2x, Update 1x, sisa 15 ms",
                    "  frame 5 (8 ms): FixedUpdate 1x, Update 1x, sisa 3 ms",
                    "",
                    "Frame pertama terlalu pendek, jadi fisika belum maju sama",
                    "sekali. Frame keempat panjangnya 50 ms, jadi fisika maju dua",
                    "langkah untuk mengejar. Sisa waktunya disimpan untuk frame",
                    "berikutnya.",
                    "",
                    "Dari sini muncul dua aturan:",
                    "",
                    "  - Gaya dan perubahan kecepatan Rigidbody ditulis di",
                    "    FixedUpdate, supaya dorongannya sama besar berapa pun laju",
                    "    frame-nya.",
                    "  - Input yang cuma sesaat, misalnya tombol yang baru ditekan,",
                    "    dibaca di Update. Kalau dibaca di FixedUpdate, tekanan di",
                    "    frame yang nggak punya langkah fisika (seperti frame",
                    "    pertama di atas) bisa hilang.",
                    "",
                    "Contoh di bawah menerapkan dua aturan itu. Tombolnya dibaca",
                    "lewat paket Input System, cara membaca input yang lebih baru.",
                    "Tutorial lama memakai Input.GetKeyDown dari sistem lama, dan",
                    "cara itu melempar galat kalau proyekmu disetel hanya memakai",
                    "Input System.",
                ],
                "bahasa": "csharp",
                "code": """using UnityEngine;
using UnityEngine.InputSystem;

public class Lompat : MonoBehaviour
{
    [SerializeField] private float gayaLompat = 7f;
    private Rigidbody2D rb;
    private bool mauLompat;

    void Awake()
    {
        rb = GetComponent<Rigidbody2D>();
    }

    void Update()
    {
        // Tombol dibaca tiap frame supaya tekanannya nggak terlewat.
        if (Keyboard.current.spaceKey.wasPressedThisFrame)
        {
            mauLompat = true;
        }
    }

    void FixedUpdate()
    {
        if (mauLompat)
        {
            rb.AddForce(Vector2.up * gayaLompat, ForceMode2D.Impulse);
            mauLompat = false;
        }
    }
}""",
            },
            {
                "heading": "Trigger atau tabrakan",
                "body": [
                    "Collider punya centang Is Trigger. Bedanya:",
                    "",
                    "  - Tanpa centang, benda saling menahan. Bola memantul dari",
                    "    dinding, dan pemain bisa berdiri di lantai. Kejadiannya",
                    "    diterima lewat OnCollisionEnter2D.",
                    "  - Dengan centang, benda saling tembus, tapi Unity tetap",
                    "    memberi tahu bahwa keduanya bersentuhan lewat",
                    "    OnTriggerEnter2D. Cocok untuk koin, garis finis, atau area",
                    "    jebakan.",
                    "",
                    "Supaya kejadian itu terpanggil, minimal salah satu dari dua",
                    "benda harus punya Rigidbody. Untuk tabrakan biasa, Rigidbody",
                    "itu sebaiknya Dynamic. Dua collider tanpa Rigidbody yang",
                    "bersentuhan nggak memicu apa pun.",
                ],
                "bahasa": "csharp",
                "code": """using UnityEngine;

public class Koin : MonoBehaviour
{
    [SerializeField] private int nilai = 1;

    // Nama dan parameternya harus persis begini. Kalau salah, Unity diam saja.
    void OnTriggerEnter2D(Collider2D lain)
    {
        if (lain.CompareTag("Player"))
        {
            Debug.Log("Dapat koin " + nilai);
            Destroy(gameObject);
        }
    }
}""",
            },
            {
                "heading": "Kesalahan yang sering muncul",
                "body": [
                    "Empat kesalahan ini muncul berulang-ulang di proyek pemula:",
                    "",
                    "  1. Nama atau parameter fungsi salah. OnCollisionEnter versi",
                    "     3D di objek 2D nggak pernah dipanggil. Begitu juga",
                    "     OnTriggerEnter2D yang parameternya Collider, versi 3D.",
                    "     Unity nggak memberi galat sama sekali.",
                    "  2. Menggerakkan benda ber-Rigidbody lewat transform.position.",
                    "     Itu sama dengan teleport. Fisika bisa melewatkan tabrakan,",
                    "     dan benda bisa nyangkut di dinding. Pakai AddForce,",
                    "     MovePosition, atau atur kecepatannya.",
                    "  3. Benda cepat menembus dinding. Ini tunneling dari bab 02.",
                    "     Ganti Collision Detection di Rigidbody dari Discrete ke",
                    "     Continuous.",
                    "  4. Nama properti dari tutorial lama. Di Unity 6, kecepatan",
                    "     Rigidbody dibaca lewat linearVelocity. Nama velocity yang",
                    "     dipakai tutorial lama sudah ditandai usang.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Game platformer dan game balap sederhana di Unity hampir",
                    "selalu berurusan dengan pembagian kerja Update dan",
                    "FixedUpdate. Keluhan seperti lompatnya kadang nggak keluar",
                    "sering berakar dari input yang dibaca di tempat yang salah.",
                    "",
                    "Kasus kecil: lompatan karaktermu kadang nggak terjadi",
                    "walaupun tombol spasi sudah ditekan. Di laptopmu jarang, tapi",
                    "di laptop teman yang lebih kencang lebih sering.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Cari tempat tombolnya dibaca. Kalau ada di FixedUpdate,",
                    "     itu penyebabnya. Laptop kencang menghasilkan lebih banyak",
                    "     frame per detik, jadi makin banyak frame yang nggak punya",
                    "     langkah fisika.",
                    "  2. Pindahkan pembacaan tombol ke Update, lalu simpan",
                    "     hasilnya di variabel bool, misalnya mauLompat = true.",
                    "  3. Di FixedUpdate, kalau mauLompat bernilai true, beri",
                    "     dorongan lalu kembalikan variabelnya ke false:",
                    "      rb.AddForce(Vector2.up * gayaLompat, ForceMode2D.Impulse);",
                    "  4. Uji di laju frame yang berbeda. Application.targetFrameRate",
                    "     bisa dipakai untuk memaksa laju frame tinggi atau rendah.",
                ],
            },
        ],
    },
    {
        "title": "14. Membangun Game Unity untuk Android dan Web",
        "sections": [
            {
                "body": [
                    "Satu proyek Unity bisa dibangun (build) untuk banyak",
                    "platform: Windows, Linux, macOS, Android, iOS, web, sampai",
                    "konsol. Kode C#-nya sama. Yang berbeda pengaturan build dan",
                    "cara gamenya sampai ke pemain.",
                    "",
                    "Di Unity 6, pengaturan itu ada di jendela Build Profiles (menu",
                    "File, lalu Build Profiles). Tiap platform butuh modul tambahan",
                    "yang dipasang lewat Unity Hub, aplikasi kecil untuk mengelola",
                    "versi editor dan modulnya. Kalau modul Android belum",
                    "terpasang, pilihan Android di Build Profiles cuma menampilkan",
                    "tombol untuk memasangnya.",
                ],
            },
            {
                "heading": "Pilih render pipeline dulu",
                "body": [
                    "Render pipeline adalah cara Unity menggambar scene ke layar.",
                    "Ada tiga yang perlu kamu kenal:",
                    "",
                    "  - Universal Render Pipeline: ringan, jalan di ponsel, web,",
                    "    PC, dan konsol. Template Universal 2D dan Universal 3D di",
                    "    Unity Hub memakai pipeline ini.",
                    "  - High Definition Render Pipeline (HDRP): grafis kelas atas",
                    "    untuk PC dan konsol yang kuat. Nggak bisa dipakai untuk",
                    "    ponsel dan web.",
                    "  - Built-In Render Pipeline: cara lama. Sejak Unity 6.5",
                    "    statusnya deprecated, artinya masih ada, tapi nggak",
                    "    dikembangkan lagi dan suatu hari dihapus.",
                    "",
                    "Untuk game Android dan web, pilih Universal Render Pipeline",
                    "dari awal. Memindahkan proyek dari Built-In di tengah jalan",
                    "artinya mengganti material dan shader satu per satu.",
                ],
            },
            {
                "heading": "Build untuk Android",
                "body": [
                    "Langkahnya:",
                    "",
                    "  1. Di Unity Hub, tambahkan modul Android Build Support ke",
                    "     versi editormu. Modul ini sekalian memasang OpenJDK,",
                    "     Android SDK, dan NDK yang cocok, jadi kamu nggak perlu",
                    "     memasangnya sendiri.",
                    "  2. Buka Build Profiles, pilih Android, lalu Switch Platform.",
                    "     Unity mengimpor ulang aset untuk Android, dan di proyek",
                    "     besar ini makan waktu.",
                    "  3. Di Player Settings, isi nama perusahaan, nama produk, dan",
                    "     package name seperti com.namamu.gamekoin. Google Play",
                    "     memakai package name sebagai identitas aplikasi, dan",
                    "     nilainya nggak bisa diganti sesudah rilis.",
                    "  4. Pilih scripting backend IL2CPP dan arsitektur ARM64.",
                    "     Google Play mewajibkan versi 64-bit, dan di Unity ARM64",
                    "     cuma tersedia lewat IL2CPP.",
                    "  5. Untuk dicoba di ponselmu sendiri, build APK. Untuk Google",
                    "     Play, centang Build App Bundle (Google Play), karena Play",
                    "     mewajibkan format AAB.",
                    "",
                    "Sejak 31 Agustus 2026, Google Play juga mewajibkan aplikasi",
                    "baru dan pembaruan menargetkan API level 36. Aturan rilis",
                    "Google Play lainnya dibahas di kurikulum Mobile & Desktop.",
                    "",
                    "Ponsel yang tersambung lewat USB, dengan USB debugging",
                    "menyala, bisa langsung dipasangi lewat tombol Build And Run.",
                    "Bisa juga lewat adb, alat baris perintah dari Android SDK.",
                    "Baris terakhir menampilkan log Debug.Log dari gamemu.",
                ],
                "bahasa": "terminal",
                "code": """adb devices
adb install -r Builds/GameKoin.apk
adb logcat -s Unity""",
            },
            {
                "heading": "Build untuk web",
                "body": [
                    "Di Unity 6, platform ini namanya Web. Dulu namanya WebGL, dan",
                    "banyak tutorial masih memakai nama lama itu. Hasil build-nya",
                    "berupa satu folder. Unity memberi nama berkasnya sesuai nama",
                    "folder build, jadi di contoh ini semuanya diawali Web.",
                ],
                "bahasa": "teks",
                "code": """Builds/Web/
├── index.html
├── Build/
│   ├── Web.loader.js
│   ├── Web.framework.js.br
│   ├── Web.data.br
│   └── Web.wasm.br
└── TemplateData/""",
            },
            {
                "body": [
                    "Berkas .wasm berisi kode gamemu yang sudah diterjemahkan jadi",
                    "WebAssembly, format yang bisa dijalankan browser dengan cepat.",
                    "Akhiran .br artinya berkas itu dikompresi dengan Brotli.",
                    "",
                    "Dua hal sering bikin build web gagal tampil:",
                    "",
                    "  - Dibuka langsung dengan klik dua kali, jadi alamatnya",
                    "    file://. Browser menolak memuat berkas pendukungnya. Pakai",
                    "    Build And Run dari Unity, yang menyalakan server lokal",
                    "    untukmu.",
                    "  - Diunggah ke server yang nggak mengirim header",
                    "    Content-Encoding untuk berkas .br, jadi browser nggak tahu",
                    "    berkas itu dikompresi. Kalau kamu nggak bisa mengatur",
                    "    servernya, nyalakan Decompression Fallback di Player",
                    "    Settings, atau matikan kompresinya.",
                    "",
                    "Build web cocok diunggah ke itch.io sebagai game yang bisa",
                    "dimainkan langsung di halamannya. Caranya dibahas di materi",
                    "Menerbitkan Game: itch.io dan Steam.",
                ],
            },
            {
                "heading": "Lisensi dan biaya",
                "body": [
                    "Unity Personal gratis selama pendapatan dan pendanaanmu dalam",
                    "12 bulan terakhir paling banyak 200 ribu dolar AS. Di Unity 6,",
                    "layar pembuka (splash screen) bertuliskan Unity boleh",
                    "dimatikan walaupun memakai Personal. Lewat dari batas itu,",
                    "kamu wajib berlangganan Unity Pro, yang sejak 12 Januari 2026",
                    "harganya 2.310 dolar AS per tahun untuk tiap kursi.",
                    "",
                    "Pemakai lama mungkin ingat ribut-ribut Runtime Fee. Tahun",
                    "2023 Unity mengumumkan biaya per pemasangan game, banyak",
                    "developer protes, dan pada 12 September 2024 biaya itu",
                    "dibatalkan. Jadi sekarang nggak ada biaya per unduhan. Yang",
                    "berlaku cuma batas pendapatan tadi.",
                    "",
                    "Satu catatan buat pemakai Fedora. Di Linux, editor Unity",
                    "secara resmi cuma mendukung Ubuntu 22.04 dan 24.04. Di Fedora",
                    "banyak orang tetap bisa menjalankannya, tapi kalau ada",
                    "masalah, Unity nggak menjaminnya.",
                    "",
                    "Jebakan: kehilangan keystore. APK dan AAB ditandatangani",
                    "dengan berkas keystore milikmu, dan pembaruan aplikasi harus",
                    "memakai kunci yang sama. Kalau aplikasimu memakai Play App",
                    "Signing, kunci unggahan yang hilang masih bisa direset lewat",
                    "permintaan di Play Console, tapi prosesnya butuh waktu. Simpan",
                    "keystore dan kata sandinya di dua tempat terpisah sejak build",
                    "pertama.",
                    "",
                    "Build Android pertama dengan IL2CPP bisa lama, apalagi di",
                    "laptop, karena kode C# diterjemahkan dulu jadi C++ lalu",
                    "dikompilasi. Build berikutnya lebih cepat karena hasil",
                    "antaranya disimpan.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Studio kecil sering merilis game Unity ke Google Play, lalu",
                    "memasang versi web-nya di itch.io sebagai demo yang bisa",
                    "dicoba tanpa memasang apa-apa. Dua build itu keluar dari",
                    "proyek yang sama, cuma beda profil build.",
                    "",
                    "Kasus kecil: kamu mengunggah build web ke hosting milikmu.",
                    "Yang muncul cuma bilah loading, lalu pesan galat bahwa berkas",
                    ".framework.js.br nggak bisa dibaca dan server perlu mengirim",
                    "header Content-Encoding: br.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Buka DevTools (F12), tab Network. Klik berkas .wasm.br",
                    "     dan lihat header balasannya. Kalau Content-Encoding",
                    "     nggak ada, penyebabnya memang di server.",
                    "  2. Kalau kamu bisa mengatur server, tambahkan header",
                    "     Content-Encoding: br untuk berkas berakhiran .br, dan",
                    "     Content-Type: application/wasm untuk berkas .wasm.",
                    "  3. Kalau nggak bisa, buka Player Settings, bagian Publishing",
                    "     Settings, nyalakan Decompression Fallback, lalu build",
                    "     ulang. Gamenya sedikit lebih lambat dimuat, tapi jalan di",
                    "     server mana pun.",
                    "  4. Uji di jendela penyamaran (incognito), supaya berkas lama",
                    "     yang tersimpan di cache browser nggak mengecoh.",
                ],
            },
        ],
    },
    {
        "title": "15. Pathfinding Grid: BFS, Dijkstra, dan A*",
        "sections": [
            {
                "body": [
                    "Musuh yang mengejar pemain harus tahu jalan. Kalau ada tembok",
                    "di antara keduanya, berjalan lurus ke arah pemain cuma bikin",
                    "musuh menempel di tembok. Pathfinding adalah cara mencari rute",
                    "dari satu titik ke titik lain sambil menghindari rintangan.",
                    "",
                    "Cara paling gampang memulainya adalah membagi peta jadi grid,",
                    "yaitu kotak-kotak kecil yang sama besar. Tiap kotak bisa",
                    "dilewati atau nggak. Dari satu kotak kamu boleh melangkah ke",
                    "empat tetangganya: atas, kanan, bawah, dan kiri. Di materi ini",
                    "peta ditulis sebagai teks:",
                    "",
                    "  S   titik awal (start)",
                    "  G   tujuan (goal)",
                    "  #   tembok",
                    "  .   tanah biasa, biaya 1 untuk melangkah ke sana",
                    "  9   lumpur, biaya 9 untuk melangkah ke sana",
                ],
            },
            {
                "heading": "BFS: menyebar seperti riak air",
                "body": [
                    "BFS (breadth-first search) memeriksa semua kotak yang jaraknya",
                    "satu langkah dari awal, lalu semua yang dua langkah, lalu tiga,",
                    "dan seterusnya. Mirip riak air yang menyebar dari batu yang",
                    "dilempar ke kolam.",
                    "",
                    "Alatnya antrean (queue): kotak yang ditemukan duluan diperiksa",
                    "duluan. Tiap kali sebuah kotak diperiksa, tetangganya yang",
                    "belum pernah dikunjungi dimasukkan ke ujung antrean, sambil",
                    "dicatat dari mana ia datang. Begitu tujuan diambil dari",
                    "antrean, rutenya bisa dibaca mundur lewat catatan asal itu.",
                    "",
                    "BFS menjamin rute dengan jumlah langkah paling sedikit.",
                    "Masalahnya, BFS menganggap semua kotak sama mahalnya. Lumpur",
                    "dan tanah biasa sama-sama dihitung satu langkah.",
                ],
            },
            {
                "heading": "Dijkstra: kalau medan punya biaya",
                "body": [
                    "Algoritma Dijkstra memperbaiki itu. Bedanya cuma di cara",
                    "memilih kotak berikutnya. BFS mengambil kotak yang paling dulu",
                    "masuk antrean, sedangkan Dijkstra selalu mengambil kotak",
                    "dengan total biaya terkecil dari awal. Total biaya itu biasa",
                    "ditulis g.",
                    "",
                    "Program di bawah menjalankan keduanya di peta yang sama.",
                    "Fungsinya satu, dan parameter pakaiBiaya yang menentukan cara",
                    "mengambil kotak dari antrean.",
                ],
                "code": """const peta = [
  "S.99.G",
  ".#..#.",
  "......",
];
const ARAH = [[-1, 0], [0, 1], [1, 0], [0, -1]]; // atas, kanan, bawah, kiri
const biaya = (ch) => (ch >= "1" && ch <= "9" ? Number(ch) : 1);

function temukan(huruf) {
  for (let r = 0; r < peta.length; r++) {
    const k = peta[r].indexOf(huruf);
    if (k >= 0) return [r, k];
  }
}

function cari(pakaiBiaya) {
  const [awal, tujuan] = [temukan("S"), temukan("G")];
  const id = (r, k) => r + "," + k;
  const jarak = { [id(...awal)]: 0 };
  const asal = {};
  const antre = [awal];
  while (antre.length > 0) {
    // BFS ambil yang paling dulu masuk; Dijkstra ambil yang jaraknya terkecil.
    let i = 0;
    if (pakaiBiaya) {
      antre.forEach((t, j) => { if (jarak[id(...t)] < jarak[id(...antre[i])]) i = j; });
    }
    const [r, k] = antre.splice(i, 1)[0];
    if (r === tujuan[0] && k === tujuan[1]) break;
    for (const [dr, dk] of ARAH) {
      const [nr, nk] = [r + dr, k + dk];
      if (!peta[nr] || !peta[nr][nk] || peta[nr][nk] === "#") continue;
      const baru = jarak[id(r, k)] + (pakaiBiaya ? biaya(peta[nr][nk]) : 1);
      if (jarak[id(nr, nk)] === undefined || baru < jarak[id(nr, nk)]) {
        jarak[id(nr, nk)] = baru;
        asal[id(nr, nk)] = [r, k];
        antre.push([nr, nk]);
      }
    }
  }
  // Telusuri balik dari tujuan ke awal lewat catatan asal.
  const gambar = peta.map((b) => b.split(""));
  let [r, k] = asal[id(...tujuan)];
  let total = biaya("G"), langkah = 1;
  while (gambar[r][k] !== "S") {
    total += biaya(gambar[r][k]);
    gambar[r][k] = "*";
    langkah++;
    [r, k] = asal[id(r, k)];
  }
  console.log(`${pakaiBiaya ? "Dijkstra" : "BFS"}: ${langkah} langkah, biaya ${total}`);
  for (const b of gambar) console.log("  " + b.join(""));
}

cari(false);
cari(true);""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  BFS: 5 langkah, biaya 21",
                    "    S****G",
                    "    .#..#.",
                    "    ......",
                    "  Dijkstra: 9 langkah, biaya 9",
                    "    S.99.G",
                    "    *#..#*",
                    "    ******",
                    "",
                    "BFS lewat jalan lurus yang melintasi dua kotak lumpur.",
                    "Langkahnya paling sedikit, tapi biayanya 21. Dijkstra memutar",
                    "lewat bawah. Langkahnya hampir dua kali lipat, tapi biayanya",
                    "cuma 9.",
                    "",
                    "Untuk mengambil kotak berbiaya terkecil, program ini memeriksa",
                    "seluruh antrean satu per satu. Itu cukup untuk peta kecil.",
                    "Engine dan pustaka sungguhan memakai heap, struktur data yang",
                    "bisa mengeluarkan nilai terkecil dengan cepat walaupun petanya",
                    "besar.",
                ],
            },
            {
                "heading": "A*: Dijkstra yang tahu arah",
                "body": [
                    "Dijkstra menyebar ke segala arah, termasuk menjauhi tujuan.",
                    "A* (dibaca A-star) menambahkan perkiraan sisa jarak ke tujuan,",
                    "ditulis h. Kotak yang diambil berikutnya adalah yang nilai",
                    "f = g + h-nya paling kecil. Akibatnya pencarian condong ke",
                    "arah tujuan, dan kotak yang diperiksa jauh lebih sedikit.",
                    "",
                    "Untuk grid empat arah, perkiraan yang biasa dipakai adalah",
                    "jarak Manhattan: selisih baris ditambah selisih kolom. Namanya",
                    "diambil dari kota yang jalannya kotak-kotak, tempat kamu",
                    "nggak bisa memotong diagonal menembus gedung.",
                    "",
                    "  h = |baris - barisTujuan| + |kolom - kolomTujuan|",
                    "",
                    "Syaratnya, h nggak boleh melebihi biaya aslinya. Perkiraan",
                    "seperti ini disebut admissible, dan dengan itu A* dijamin",
                    "menemukan rute termurah. Jarak Manhattan memenuhi syarat itu",
                    "kalau biaya terkecil per langkah adalah 1.",
                    "",
                    "Kalau h dibuat terlalu besar, misalnya dikali 5, A* jadi",
                    "lebih rakus. Kotak yang diperiksa makin sedikit, tapi rutenya",
                    "bisa nggak lagi termurah. Beberapa game sengaja memakai cara",
                    "ini, karena rute yang cukup bagus dan cepat dihitung lebih",
                    "berguna daripada rute sempurna yang lambat. Sebaliknya, kalau",
                    "h selalu 0, A* sama persis dengan Dijkstra.",
                ],
            },
            {
                "heading": "Kapan memakai yang mana",
                "body": [
                    "  Algoritma  Kotak berikutnya     Biaya medan  Rute yang dijamin",
                    "  BFS        paling dulu masuk    diabaikan    langkah tersedikit",
                    "  Dijkstra   g terkecil           dihitung     termurah",
                    "  A*         f = g + h terkecil   dihitung     termurah, kalau h",
                    "                                               admissible",
                    "",
                    "Pakai BFS kalau semua kotak sama mahalnya, misalnya di game",
                    "teka-teki berpetak. Pakai Dijkstra kalau kamu butuh jarak ke",
                    "banyak tujuan sekaligus, misalnya peta jarak dari pemain ke",
                    "semua kotak. Pakai A* untuk mencari rute dari satu titik ke",
                    "satu tujuan, kasus yang paling sering muncul di game.",
                ],
            },
            {
                "heading": "Navmesh dan dunia yang besar",
                "body": [
                    "Grid cocok untuk game berpetak. Game 3D dengan lantai miring,",
                    "tangga, dan jembatan biasanya memakai navmesh (navigation",
                    "mesh). Area yang bisa dilalui dipotong jadi poligon, lalu A*",
                    "berjalan di atas poligon itu. Jumlah poligonnya jauh lebih",
                    "sedikit daripada jumlah kotak, jadi pencariannya lebih cepat.",
                    "",
                    "Kamu jarang menulis navmesh sendiri. Unity punya paket AI",
                    "Navigation dengan komponen NavMeshAgent, Godot punya",
                    "NavigationAgent2D dan NavigationAgent3D, dan Unreal punya",
                    "sistem navigasi bawaan. Unreal dan Godot memakai pustaka open",
                    "source Recast untuk membuat navmesh dari bentuk level.",
                    "",
                    "Untuk ratusan unit yang menuju satu titik, misalnya di game",
                    "strategi, ada teknik flow field. Arah menuju tujuan dihitung",
                    "sekali untuk setiap kotak, lalu tiap unit tinggal mengikuti",
                    "panah di kotak tempatnya berdiri.",
                    "",
                    "Jebakan: menghitung ulang rute tiap frame untuk tiap musuh. A*",
                    "di peta besar bisa makan waktu, dan dua puluh musuh berarti",
                    "dua puluh pencarian per frame. Hitung ulang hanya kalau target",
                    "sudah pindah cukup jauh, atau gilir jadwalnya supaya musuh",
                    "yang berbeda dihitung di frame yang berbeda.",
                    "",
                    "Ingat: kalau ada beberapa rute dengan biaya sama, urutan",
                    "memeriksa tetangga menentukan rute mana yang terpilih. Kalau",
                    "urutannya nggak tetap, musuh bisa berzigzag. Tetapkan",
                    "urutannya, misalnya atas, kanan, bawah, kiri, supaya hasilnya",
                    "selalu sama dan bisa diuji.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Game strategi, game taktik berpetak, dan game tower defense",
                    "memakai pencarian jalan terus-menerus. Di game tower defense,",
                    "tiap kali pemain menaruh menara, rute musuh dihitung ulang,",
                    "dan game biasanya melarang menara yang menutup jalan sama",
                    "sekali.",
                    "",
                    "Kasus kecil: di game tower defense buatanmu, pemain bisa",
                    "menaruh menara sampai jalan musuh tertutup total. Musuh lalu",
                    "diam di tempat, dan gelombangnya nggak pernah selesai.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Sebelum menara dipasang, tandai kotaknya sebagai tembok di",
                    "     salinan peta.",
                    "  2. Jalankan BFS dari pintu masuk musuh ke markas di salinan",
                    "     itu. BFS sudah cukup, karena yang ditanyakan cuma masih",
                    "     ada jalan atau nggak.",
                    "  3. Kalau BFS nggak menemukan markas, tolak pemasangan menara",
                    "     dan beri tanda merah di kotak itu.",
                    "  4. Kalau jalan masih ada, pasang menaranya, lalu hitung ulang",
                    "     rute musuh dengan A* sekali saja, jangan tiap frame.",
                ],
            },
        ],
    },
    {
        "title": "16. Perilaku Musuh: State Machine dan Behavior Tree",
        "sections": [
            {
                "body": [
                    "Pathfinding menjawab cara sampai ke suatu tempat. Musuh juga",
                    "perlu memutuskan mau ngapain sekarang: patroli, mengejar,",
                    "menyerang, atau kabur. Bagian game yang mengatur keputusan itu",
                    "biasa disebut AI game.",
                    "",
                    "AI di sini nggak ada hubungannya dengan model bahasa atau",
                    "machine learning. Isinya aturan yang ditulis programmer supaya",
                    "musuh kelihatan cerdas dan seru dilawan.",
                ],
            },
            {
                "heading": "State machine untuk musuh",
                "body": [
                    "Di bab 03 kamu memakai finite state machine (FSM) untuk",
                    "karakter platformer. Musuh bisa diatur dengan cara yang sama.",
                    "Tiap state punya perilaku sendiri, dan transisi ke state lain",
                    "terjadi kalau syaratnya terpenuhi:",
                    "",
                    "  patroli -> kejar     kalau pemain lebih dekat dari 8 meter",
                    "  kejar   -> serang    kalau jaraknya 1 meter atau kurang",
                    "  serang  -> kejar     kalau pemain menjauh",
                    "  kejar   -> kabur     kalau nyawa di bawah 30",
                    "  serang  -> kabur     kalau nyawa di bawah 30",
                    "  kabur   -> patroli   kalau pemain lebih jauh dari 12 meter",
                    "",
                    "Program di bawah menjalankan tabel itu dengan data per tick",
                    "yang tetap. Tick adalah satu putaran keputusan, misalnya",
                    "beberapa kali per detik.",
                ],
                "code": """// Tiap tick: [jarak ke pemain dalam meter, nyawa musuh].
const ticks = [[12, 100], [7, 100], [1, 90], [1, 60], [4, 20], [15, 20]];

function berikutnya(state, jarak, nyawa) {
  switch (state) {
    case "patroli":
      return jarak < 8 ? "kejar" : "patroli";
    case "kejar":
      if (nyawa < 30) return "kabur";
      return jarak <= 1 ? "serang" : "kejar";
    case "serang":
      if (nyawa < 30) return "kabur";
      return jarak > 1 ? "kejar" : "serang";
    case "kabur":
      return jarak > 12 ? "patroli" : "kabur";
  }
}

let state = "patroli";
ticks.forEach(([jarak, nyawa], i) => {
  state = berikutnya(state, jarak, nyawa);
  console.log(`tick ${i + 1}: jarak ${jarak}, nyawa ${nyawa} -> ${state}`);
});""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  tick 1: jarak 12, nyawa 100 -> patroli",
                    "  tick 2: jarak 7, nyawa 100 -> kejar",
                    "  tick 3: jarak 1, nyawa 90 -> serang",
                    "  tick 4: jarak 1, nyawa 60 -> serang",
                    "  tick 5: jarak 4, nyawa 20 -> kabur",
                    "  tick 6: jarak 15, nyawa 20 -> patroli",
                    "",
                    "Perhatikan aturan kabur. Supaya musuh bisa kabur dari state",
                    "kejar maupun serang, syarat nyawa ditulis dua kali. Kalau",
                    "nanti kamu menambah state baru, misalnya lempar granat, syarat",
                    "kabur harus ditambahkan lagi di situ. Makin banyak state,",
                    "makin banyak transisi yang harus dijaga satu per satu, dan di",
                    "game besar tabelnya bisa membengkak sampai susah dibaca.",
                ],
            },
            {
                "heading": "Behavior tree",
                "body": [
                    "Behavior tree menyusun keputusan sebagai pohon. Tiap tick,",
                    "pohon diperiksa dari akar, dan tiap node mengembalikan satu",
                    "dari tiga status: berhasil, gagal, atau berjalan. Berjalan",
                    "artinya aksinya belum selesai, misalnya musuh masih melangkah",
                    "ke arah pemain.",
                    "",
                    "Ada empat jenis node yang paling sering dipakai:",
                    "",
                    "  - Kondisi: memeriksa sesuatu, lalu mengembalikan berhasil",
                    "    atau gagal. Contohnya, apakah pemain terlihat.",
                    "  - Aksi: melakukan sesuatu, misalnya memukul atau berjalan.",
                    "  - Sequence: menjalankan anak-anaknya dari kiri ke kanan",
                    "    selama hasilnya berhasil. Begitu satu anak nggak berhasil,",
                    "    sequence berhenti dan ikut mengembalikan status anak itu.",
                    "    Anggap saja lakukan ini, lalu ini, lalu ini.",
                    "  - Selector: mencoba anak-anaknya dari kiri ke kanan sampai",
                    "    ada yang nggak gagal, lalu mengembalikan status anak itu.",
                    "    Anggap saja coba ini, kalau gagal coba yang berikutnya.",
                    "",
                    "Urutan anak di selector adalah urutan prioritas. Anak paling",
                    "kiri diperiksa duluan, jadi taruh perilaku yang paling",
                    "mendesak di kiri. Pohon di bawah memuat perilaku yang sama",
                    "dengan state machine tadi.",
                ],
                "bahasa": "teks",
                "code": """selector (akar)
├── sequence: kabur
│   ├── kondisi: sekarat?
│   └── aksi: lari
├── sequence: serang
│   ├── kondisi: dekat?
│   └── aksi: pukul
├── sequence: kejar
│   ├── kondisi: terlihat?
│   └── aksi: kejar
└── aksi: patroli""",
            },
            {
                "heading": "Menjalankan pohonnya",
                "body": [
                    "Program ini menjalankan pohon tadi selama empat tick. Tiap",
                    "tick membawa daftar kondisi yang sedang benar. Aksi di sini",
                    "selalu mengembalikan status yang sudah ditentukan, karena yang",
                    "mau dilihat adalah jalannya keputusan.",
                ],
                "code": """// Behavior tree kecil. Kondisi dibaca dari fakta tick itu,
// aksi selalu mengembalikan status yang sudah ditentukan.
const kondisi = (nama) => ({ jenis: "kondisi", nama });
const aksi = (nama, status) => ({ jenis: "aksi", nama, status });
const sequence = (...anak) => ({ jenis: "sequence", anak });
const selector = (...anak) => ({ jenis: "selector", anak });

const akar = selector(
  sequence(kondisi("sekarat"), aksi("lari", "berjalan")),
  sequence(kondisi("dekat"), aksi("pukul", "berhasil")),
  sequence(kondisi("terlihat"), aksi("kejar", "berjalan")),
  aksi("patroli", "berjalan"),
);

function tick(n, fakta, jejak) {
  if (n.jenis === "kondisi") {
    const benar = fakta.includes(n.nama);
    jejak.push(`${n.nama}? ${benar ? "ya" : "tidak"}`);
    return benar ? "berhasil" : "gagal";
  }
  if (n.jenis === "aksi") {
    jejak.push(`${n.nama} -> ${n.status}`);
    return n.status;
  }
  // sequence lanjut selama anaknya berhasil, selector lanjut selama gagal.
  const lanjutKalau = n.jenis === "sequence" ? "berhasil" : "gagal";
  for (const a of n.anak) {
    const s = tick(a, fakta, jejak);
    if (s !== lanjutKalau) return s;
  }
  return lanjutKalau;
}

const daftarFakta = [[], ["terlihat"], ["terlihat", "dekat"], ["sekarat", "dekat"]];
daftarFakta.forEach((fakta, i) => {
  const jejak = [];
  tick(akar, fakta, jejak);
  console.log(`tick ${i + 1}: ${jejak.join(", ")}`);
});""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  tick 1: sekarat? tidak, dekat? tidak, terlihat? tidak, patroli -> berjalan",
                    "  tick 2: sekarat? tidak, dekat? tidak, terlihat? ya, kejar -> berjalan",
                    "  tick 3: sekarat? tidak, dekat? ya, pukul -> berhasil",
                    "  tick 4: sekarat? ya, lari -> berjalan",
                    "",
                    "Di tick 4 pemain dekat, tapi musuh tetap lari, karena cabang",
                    "kabur ada di paling kiri dan diperiksa duluan. Status akar",
                    "selalu sama dengan status aksi terakhir di tiap baris, karena",
                    "selector berhenti tepat di anak yang nggak gagal.",
                    "",
                    "Menambah perilaku baru di pohon ini cukup dengan satu cabang",
                    "di posisi prioritas yang tepat. Syarat kabur nggak perlu",
                    "disalin ke tempat lain seperti di state machine tadi.",
                ],
            },
            {
                "heading": "Pilihan lain dan dukungan engine",
                "body": [
                    "Dua pendekatan lain juga sering disebut:",
                    "",
                    "  - GOAP (goal-oriented action planning): musuh diberi tujuan,",
                    "    misalnya pemain kalah, plus daftar aksi beserta syarat dan",
                    "    akibatnya. Perencana mencari urutan aksi yang sampai ke",
                    "    tujuan itu. Teknik ini dikenal lewat game F.E.A.R. (2005).",
                    "  - Utility AI: tiap pilihan diberi skor dari keadaan saat itu,",
                    "    lalu musuh memilih skor tertinggi. Cocok untuk karakter",
                    "    yang punya banyak kebutuhan, seperti di game simulasi",
                    "    kehidupan.",
                    "",
                    "Unreal punya editor Behavior Tree bawaan, plus StateTree yang",
                    "menggabungkan state machine dan pohon. Unity menyediakan paket",
                    "Unity Behavior. Godot belum punya behavior tree bawaan, tapi",
                    "ada plugin komunitas seperti LimboAI dan Beehave.",
                    "",
                    "Untuk musuh dengan tiga atau empat perilaku, FSM biasa sudah",
                    "cukup dan lebih gampang dibaca. Behavior tree mulai terasa",
                    "gunanya waktu perilakunya banyak dan sering berubah.",
                    "",
                    "Jebakan: aksi berstatus berjalan bisa terpotong. Karena pohon",
                    "diperiksa ulang dari akar tiap tick, cabang yang lebih kiri",
                    "bisa mengambil alih di tengah aksi. Untuk aksi yang nggak",
                    "boleh dipotong, misalnya animasi pukulan yang sudah separuh",
                    "jalan, tambahkan kondisi sedang sibuk di awal pohon.",
                    "",
                    "Ingat: banyak game sengaja membuat musuh nggak sempurna,",
                    "misalnya memberi jeda reaksi sebelum menyerang atau membiarkan",
                    "tembakannya sesekali meleset. Aturan seperti itu juga ditulis",
                    "di AI musuh.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Game aksi dan game siluman (stealth) bergantung pada perilaku",
                    "musuh. Penjaga yang berpatroli, curiga waktu mendengar suara,",
                    "lalu memeriksa sumbernya, biasanya disusun sebagai state",
                    "machine atau behavior tree dengan status waspada di antara",
                    "patroli dan kejar.",
                    "",
                    "Kasus kecil: musuh di gamemu kabur waktu nyawanya sedikit.",
                    "Begitu agak jauh, dia kembali patroli, langsung melihat",
                    "pemain, mengejar lagi, lalu kabur lagi. Bolak-balik terus",
                    "setiap beberapa detik.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Cetak state tiap tick, seperti tiruan di atas, lalu cari",
                    "     urutan yang berulang: kabur, patroli, kejar, kabur.",
                    "  2. Lihat transisinya. patroli -> kejar nggak memeriksa nyawa,",
                    "     jadi musuh yang masih sekarat boleh mengejar lagi.",
                    "  3. Tambahkan syarat nyawa di transisi itu, atau buat state",
                    "     pulih yang menambah nyawa pelan-pelan sebelum musuh boleh",
                    "     mengejar lagi.",
                    "  4. Kalau memakai behavior tree, pastikan cabang kabur ada di",
                    "     paling kiri. Selama kondisi sekarat masih benar, cabang",
                    "     itu selalu menang, jadi bolak-balik itu nggak terjadi.",
                ],
            },
        ],
    },
    {
        "title": "17. Unreal Engine: Blueprints, C++, dan Royalti",
        "sections": [
            {
                "body": [
                    "Unreal Engine adalah engine buatan Epic Games. Fortnite dibuat",
                    "dengannya, begitu juga banyak game PC dan konsol kelas atas",
                    "yang sering disebut AAA, yaitu game beranggaran besar. Unreal",
                    "juga dipakai di luar game, misalnya untuk produksi film dan",
                    "visualisasi arsitektur.",
                    "",
                    "Versi terbaru saat materi ini ditulis (Oktober 2026) adalah",
                    "Unreal Engine 5.8, yang menurut pemberitaan dirilis 17 Juni",
                    "2026. Versi ini disebut-sebut sebagai rilis besar terakhir",
                    "seri 5, dan akses awal Unreal Engine 6 diperkirakan keluar",
                    "akhir 2027. Dalam Survei Stack Overflow 2024, 3,0% responden",
                    "menyebut memakai Unreal.",
                ],
            },
            {
                "heading": "Actor, Component, dan Tick",
                "body": [
                    "Kalau kamu sudah membaca bab Unity, istilah Unreal gampang",
                    "dipetakan:",
                    "",
                    "  Unity                 Unreal",
                    "  GameObject            Actor",
                    "  Component             Component (UActorComponent)",
                    "  Start()               BeginPlay()",
                    "  Update()              Tick(DeltaSeconds)",
                    "  Prefab                Blueprint Class",
                    "  Scene                 Level",
                    "",
                    "Unreal juga punya kelas siap pakai untuk pola yang sering",
                    "muncul. Pawn adalah Actor yang bisa dikendalikan. Character",
                    "adalah Pawn yang sudah bisa berjalan dan melompat.",
                    "PlayerController menerjemahkan input pemain, dan GameMode",
                    "menyimpan aturan permainan.",
                ],
            },
            {
                "heading": "Blueprints dan C++",
                "body": [
                    "Ada dua cara menulis logika di Unreal. Blueprints adalah",
                    "visual scripting: kamu menyambung kotak-kotak (node) dengan",
                    "kabel di editor, tanpa mengetik kode. Desainer dan seniman",
                    "bisa membuat pintu yang terbuka, jebakan, atau menu dengan",
                    "Blueprints.",
                    "",
                    "C++ dipakai untuk sistem inti yang berat atau rumit. Kodenya",
                    "lebih cepat dijalankan, perubahannya gampang dilacak lewat",
                    "git, dan lebih rapi untuk logika besar. Kekurangannya, tiap",
                    "perubahan harus dikompilasi dulu, dan C++ versi Unreal penuh",
                    "makro khusus.",
                    "",
                    "Kebanyakan tim memakai keduanya. Sistem inti ditulis di C++,",
                    "fungsinya dibuka untuk Blueprints, lalu desainer menyusun",
                    "perilakunya di Blueprint. Makro di bawah ini memberi tahu",
                    "Unreal bagian mana yang dikenali editor:",
                    "",
                    "  UCLASS()                kelas ini dikenali Unreal",
                    "  UPROPERTY(EditAnywhere) variabel ini bisa diubah di editor",
                    "  UFUNCTION(BlueprintCallable)",
                    "                          fungsi ini bisa dipanggil Blueprint",
                    "",
                    "Contoh di bawah adalah Actor koin yang berputar. Bekal dari",
                    "kurikulum C++ cukup untuk membaca sintaksnya.",
                ],
                "bahasa": "cpp",
                "code": """// KoinBerputar.h
#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "KoinBerputar.generated.h"

UCLASS()
class AKoinBerputar : public AActor
{
    GENERATED_BODY()

public:
    AKoinBerputar();
    virtual void Tick(float DeltaSeconds) override;

    UFUNCTION(BlueprintCallable)
    void Ambil();

protected:
    UPROPERTY(EditAnywhere)
    float KecepatanPutar = 90.f;   // derajat per detik

    UPROPERTY(EditAnywhere)
    int32 Nilai = 1;
};

// KoinBerputar.cpp
#include "KoinBerputar.h"

AKoinBerputar::AKoinBerputar()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AKoinBerputar::Tick(float DeltaSeconds)
{
    Super::Tick(DeltaSeconds);
    AddActorLocalRotation(FRotator(0.f, KecepatanPutar * DeltaSeconds, 0.f));
}

void AKoinBerputar::Ambil()
{
    UE_LOG(LogTemp, Log, TEXT("Koin diambil, nilai %d"), Nilai);
    Destroy();
}""",
            },
            {
                "heading": "Perangkat dan cara memasang",
                "body": [
                    "Unreal butuh komputer yang kuat: kartu grafis terpisah, RAM",
                    "besar, dan puluhan gigabyte ruang disk. Laptop kantor biasa",
                    "bakal kewalahan membuka contoh proyeknya.",
                    "",
                    "Unreal tersedia untuk Windows, macOS, dan Linux. Kode",
                    "sumbernya bisa dibaca di GitHub sesudah akun Epic-mu",
                    "ditautkan ke akun GitHub, dan Epic juga menyediakan editor",
                    "Linux yang sudah jadi. Aset siap pakai seperti model,",
                    "material, dan suara dijual atau dibagikan gratis di Fab, toko",
                    "aset milik Epic.",
                    "",
                    "Dua fitur yang sering kamu dengar adalah Nanite dan Lumen.",
                    "Nanite membuat model dengan jutaan poligon tetap ringan",
                    "digambar. Lumen menghitung cahaya yang memantul secara",
                    "langsung, tanpa perlu dihitung lebih dulu sebelum game",
                    "dijalankan.",
                ],
            },
            {
                "heading": "Royalti",
                "body": [
                    "Unreal gratis diunduh dan dipakai. Bayarnya baru muncul kalau",
                    "gamemu laku: 5% dari pendapatan kotor sesudah 1 juta dolar AS",
                    "pertama, untuk tiap produk. Pendapatan kotor artinya sebelum",
                    "dipotong toko, jadi potongan Steam nggak mengurangi dasar",
                    "hitungannya. Penjualan lewat Epic Games Store nggak dikenai",
                    "royalti ini.",
                    "",
                    "Program di bawah menghitung royalti untuk tiga contoh game",
                    "yang dijual di luar Epic Games Store.",
                ],
                "code": "// Royalti Unreal: 5% dari pendapatan kotor di atas 1 juta dolar AS\n// per produk. Penjualan lewat Epic Games Store tidak ikut dihitung.\nconst BATAS = 1000000;\n\nfunction royalti(kotorDiLuarEgs) {\n  const kena = Math.max(0, kotorDiLuarEgs - BATAS);\n  return (kena * 5) / 100;\n}\n\nconst ribuan = (n) => String(n).replace(/\\B(?=(\\d{3})+(?!\\d))/g, \".\");\n\nconst contoh = [\n  [\"game jam\", 2000],\n  [\"indie laris\", 1300000],\n  [\"hit besar\", 10000000],\n];\nfor (const [nama, kotor] of contoh) {\n  console.log(`${nama.padEnd(12)} kotor ${(\"$\" + ribuan(kotor)).padStart(11)}` +\n    `  royalti $${ribuan(royalti(kotor))}`);\n}",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  game jam     kotor      $2.000  royalti $0",
                    "  indie laris  kotor  $1.300.000  royalti $15.000",
                    "  hit besar    kotor $10.000.000  royalti $450.000",
                    "",
                    "Angka di sini sengaja disederhanakan. Dalam praktiknya",
                    "royalti dilaporkan ke Epic per triwulan, dan pajak serta",
                    "refund ikut memengaruhi angkanya. Baca sendiri perjanjian",
                    "lisensi Unreal sebelum merilis game komersial.",
                ],
            },
            {
                "heading": "Unity, Unreal, atau Godot",
                "body": [
                    "  Hal              Unity              Unreal            Godot",
                    "  bahasa           C#                 C++, Blueprints   GDScript, C#",
                    "  biaya            gratis sampai      5% di atas        gratis (MIT)",
                    "                   200 ribu dolar     1 juta dolar",
                    "  kuat di          ponsel, indie      3D kelas atas     2D, indie",
                    "  komputer         sedang             kuat              ringan",
                    "  editor Linux     resmi di Ubuntu    ada               ada",
                    "",
                    "Pilih Unreal kalau targetmu game 3D yang realistis di PC atau",
                    "konsol dan komputermu sanggup. Untuk game 2D atau game ponsel",
                    "kasual, Godot dan Unity biasanya lebih pas.",
                    "",
                    "Jebakan: memilih Unreal untuk game 2D kecil karena namanya",
                    "terkenal. Unreal bisa membuat game 2D, tapi alat 2D-nya jauh",
                    "lebih sedikit daripada Godot, Unity, atau GameMaker, dan",
                    "proyek kosongnya saja sudah besar.",
                    "",
                    "Ingat: Blueprint yang tumbuh tanpa aturan cepat berubah jadi",
                    "gumpalan kabel yang susah diikuti. Kelompokkan node ke dalam",
                    "fungsi, beri komentar, dan pindahkan logika yang makin rumit",
                    "ke C++.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Banyak game 3D kelas atas di PC dan konsol dibuat dengan",
                    "Unreal, dan lowongan programmer gameplay Unreal hampir selalu",
                    "meminta C++ plus pengalaman Blueprints. Studio kecil juga",
                    "memakainya kalau gamenya butuh grafis realistis.",
                    "",
                    "Kasus kecil: game 3D buatan timmu dijual di Steam seharga 15",
                    "dolar AS dan terjual 80.000 kopi dalam setahun. Temanmu",
                    "bilang royaltinya nol, karena sesudah potongan Steam 30%",
                    "pendapatannya cuma 840 ribu dolar, di bawah 1 juta.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Hitung pendapatan kotor: 80.000 x 15 = 1.200.000 dolar",
                    "     AS. Royalti Unreal dihitung dari angka ini, sebelum",
                    "     potongan toko.",
                    "  2. Kurangi batas bebas royalti:",
                    "      1.200.000 - 1.000.000 = 200.000",
                    "  3. Royaltinya 5% dari 200.000, yaitu 10.000 dolar AS.",
                    "  4. Masukkan angka itu ke rencana keuangan sejak awal, dan",
                    "     baca sendiri perjanjian lisensi Unreal untuk aturan",
                    "     pelaporannya.",
                ],
            },
        ],
    },
    {
        "title": "18. Peta Engine dan Framework Game",
        "sections": [
            {
                "body": [
                    "Unity, Unreal, dan Godot memang paling sering dibicarakan.",
                    "Selain itu masih banyak engine dan framework lain yang",
                    "dipakai untuk game sungguhan. Materi ini memetakan semuanya,",
                    "supaya kamu bisa memilih berdasarkan bahasa yang sudah kamu",
                    "kuasai dan jenis game yang mau dibuat.",
                    "",
                    "Bedakan dua jenis alat:",
                    "",
                    "  - Engine punya editor visual. Kamu menyusun level, mengatur",
                    "    objek, dan menulis skrip di satu aplikasi besar.",
                    "  - Framework atau pustaka cuma kumpulan fungsi. Kamu menulis",
                    "    game loop sendiri di kode, persis seperti di bab 01, dan",
                    "    pustakanya membantu menggambar, memutar suara, dan membaca",
                    "    input.",
                ],
            },
            {
                "heading": "Engine dengan editor",
                "body": [
                    "  - GameMaker: engine 2D yang ramah pemula, dengan bahasa GML",
                    "    yang mirip JavaScript. Undertale, Hotline Miami, dan Hyper",
                    "    Light Drifter dibuat dengannya. Gratis untuk proyek",
                    "    nonkomersial, dan untuk menjual game ada lisensi",
                    "    Professional seharga 99,99 dolar AS sekali bayar. Rilis",
                    "    LTS terbarunya 2026.0 (Mei 2026).",
                    "  - Defold: engine ringan untuk game 2D dan 3D, terutama di",
                    "    ponsel dan web, dengan skrip Lua. Objeknya saling",
                    "    berkomunikasi lewat pesan. Versinya 1.14.0 (Oktober 2026),",
                    "    dengan Defold License yang berbasis Apache 2.0 plus",
                    "    beberapa pembatasan.",
                    "  - Cocos Creator: penerus Cocos2d-x, dengan editor visual dan",
                    "    skrip TypeScript. Populer untuk game ponsel kasual dan mini",
                    "    game di Asia. Rilis terakhirnya 3.8.8 (Desember 2025), dan",
                    "    Cocos2d-x versi C++ klasik sudah nggak jadi fokus",
                    "    pengembangan.",
                    "  - Roblox Studio: alat resmi untuk membuat game, yang oleh",
                    "    Roblox disebut experience, dengan bahasa Luau. Luau adalah",
                    "    turunan Lua 5.1 yang ditambah tipe bertahap, dan bahasanya",
                    "    berlisensi MIT. Studio cuma tersedia untuk Windows dan",
                    "    macOS, butuh akun Roblox, dan diperbarui terus tanpa nomor",
                    "    versi publik. Populer di kalangan pelajar usia sekolah.",
                    "  - O3DE (Open 3D Engine): engine 3D open source di bawah",
                    "    Linux Foundation, berasal dari Amazon Lumberyard. Banyak",
                    "    dipakai untuk simulasi dan robotika. Versinya 2605.0 (Mei",
                    "    2026), lisensi Apache 2.0 atau MIT.",
                ],
            },
            {
                "heading": "Framework yang kode-sentris",
                "body": [
                    "  - MonoGame: framework C# penerus Microsoft XNA, tanpa editor",
                    "    visual. Stardew Valley memakainya. Versinya 3.8.6 (Oktober",
                    "    2026), lisensi Ms-PL.",
                    "  - libGDX: framework Java (bisa juga Kotlin) untuk desktop,",
                    "    Android, iOS, dan web. Slay the Spire dan Shattered Pixel",
                    "    Dungeon dibuat dengannya. Ini jembatan paling alami dari",
                    "    kurikulum Java. Versinya 1.14.2, lisensi Apache 2.0.",
                    "  - LÖVE (Love2D): framework 2D dengan Lua. Kamu cukup menulis",
                    "    love.load, love.update, dan love.draw. Balatro dibuat",
                    "    dengan LÖVE. Rilis terakhirnya 11.5 (April 2024), versi 12",
                    "    masih dikembangkan, lisensinya zlib.",
                    "  - Pygame dan pygame-ce: pustaka game 2D untuk Python di atas",
                    "    SDL. pygame-ce adalah cabang (fork) buatan komunitas yang",
                    "    lebih aktif, versinya 2.5.8 (Agustus 2026). Pygame asli",
                    "    terakhir rilis 2.6.1 (September 2024). Untuk proyek baru,",
                    "    pilih pygame-ce. Lisensinya LGPL 2.1.",
                    "  - raylib: pustaka C yang sederhana untuk belajar pemrograman",
                    "    game dan grafis, dengan binding ke banyak bahasa. Versinya",
                    "    6.2 (Oktober 2026), lisensi zlib.",
                    "  - SDL: pustaka C tingkat rendah untuk jendela, input, audio,",
                    "    dan grafis. Banyak engine, emulator, dan port game ke Linux",
                    "    berdiri di atasnya. Seri utamanya sekarang SDL3, dengan",
                    "    versi 3.4.18 (Oktober 2026), lisensi zlib.",
                    "",
                    "Dua nama lagi yang mungkin kamu temui. Bevy adalah engine",
                    "berbasis ECS untuk Rust (versi 0.20.0, Oktober 2026), dibahas",
                    "di bab 09. Dear ImGui adalah pustaka antarmuka untuk alat dan",
                    "panel debug di dalam game, dibahas di kurikulum Mobile &",
                    "Desktop.",
                    "",
                    "Dua contoh di bawah melakukan hal yang sama: kotak yang",
                    "digeser dengan panah kiri dan kanan. Di LÖVE, game loop",
                    "disembunyikan dan kamu cukup mengisi love.update dan",
                    "love.draw.",
                ],
                "bahasa": "lua",
                "code": """-- main.lua untuk LÖVE
local x = 100

function love.update(dt)
  if love.keyboard.isDown("right") then x = x + 200 * dt end
  if love.keyboard.isDown("left") then x = x - 200 * dt end
end

function love.draw()
  love.graphics.rectangle("fill", x, 300, 40, 40)
end""",
            },
            {
                "body": [
                    "Di raylib, kamu menulis loop while sendiri, lengkap dengan",
                    "menghitung dt dan memanggil fungsi gambar di antara",
                    "BeginDrawing dan EndDrawing.",
                ],
                "bahasa": "c",
                "code": """#include <raylib.h>

int main(void)
{
    InitWindow(800, 450, "Kotak raylib");
    SetTargetFPS(60);
    float x = 100;

    while (!WindowShouldClose()) {
        float dt = GetFrameTime();
        if (IsKeyDown(KEY_RIGHT)) x += 200 * dt;
        if (IsKeyDown(KEY_LEFT)) x -= 200 * dt;

        BeginDrawing();
        ClearBackground(RAYWHITE);
        DrawRectangle((int)x, 300, 40, 40, MAROON);
        EndDrawing();
    }
    CloseWindow();
    return 0;
}""",
            },
            {
                "heading": "Peta ringkas",
                "body": [
                    "  Nama            Bahasa         Lisensi          Cocok untuk",
                    "  GameMaker       GML            berbayar*        2D indie",
                    "  Defold          Lua            Defold License   ponsel, web",
                    "  Cocos Creator   TypeScript     milik Cocos      game kasual",
                    "  Roblox Studio   Luau           milik Roblox     game di Roblox",
                    "  O3DE            C++, Lua       Apache, MIT      simulasi 3D",
                    "  MonoGame        C#             Ms-PL            2D kode-sentris",
                    "  libGDX          Java, Kotlin   Apache 2.0       lanjutan Java",
                    "  LÖVE            Lua            zlib             game jam 2D",
                    "  pygame-ce       Python         LGPL 2.1         prototipe 2D",
                    "  raylib          C              zlib             belajar di C",
                    "  SDL             C              zlib             engine sendiri",
                    "",
                    "  * gratis untuk proyek nonkomersial",
                ],
            },
            {
                "heading": "Cara memilih",
                "body": [
                    "Mulai dari bahasa yang sudah kamu kuasai, lalu sesuaikan",
                    "dengan jenis game dan perangkatmu:",
                    "",
                    "  - Dari kurikulum JavaScript: Phaser (bab 03) untuk game",
                    "    browser, atau Cocos Creator kalau mau editor visual.",
                    "  - Dari kurikulum Python: Godot (GDScript mirip Python) atau",
                    "    pygame-ce.",
                    "  - Dari kurikulum Java atau Kotlin: libGDX.",
                    "  - Dari kurikulum C#: Unity, MonoGame, atau Godot versi .NET.",
                    "  - Dari kurikulum C atau C++: raylib atau SDL untuk belajar",
                    "    dasarnya, Unreal untuk 3D kelas atas.",
                    "  - Mau belajar Lua: LÖVE untuk game kecil, Defold untuk",
                    "    ponsel dan web.",
                    "  - Mau cepat jadi tanpa banyak kode: GameMaker atau Roblox",
                    "    Studio.",
                    "",
                    "Jebakan: berpindah-pindah engine sebelum satu game pun",
                    "selesai. Konsep di bab 01 sampai 03 berlaku di semua engine.",
                    "Game kecil yang selesai, lengkap dengan menu, suara, dan layar",
                    "kalah, melatih bagian yang jarang muncul di tutorial:",
                    "merapikan, menguji, dan merilis.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Game jam seperti GMTK Game Jam di itch.io diikuti ribuan tim,",
                    "dan tiap halaman game di itch.io bisa mencantumkan engine",
                    "pembuatnya. Dari situ kelihatan bahwa Godot, Unity, GameMaker,",
                    "LÖVE, dan pygame-ce sama-sama dipakai untuk game yang selesai",
                    "dalam beberapa hari.",
                    "",
                    "Kasus kecil: kamu sudah lancar Java dari kurikulum Java,",
                    "laptopmu nggak punya kartu grafis terpisah, dan kamu ingin",
                    "bikin game 2D yang bisa dimainkan di Android dan desktop.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Coret yang butuh komputer kuat: Unreal dan O3DE.",
                    "  2. Coret yang mengharuskan belajar bahasa baru dulu, kalau",
                    "     kamu ingin cepat mulai. Defold dan LÖVE butuh Lua,",
                    "     MonoGame butuh C#.",
                    "  3. Yang tersisa paling pas adalah libGDX: Java, ringan, dan",
                    "     satu kode bisa dibangun untuk Android dan desktop.",
                    "  4. Mulai dari satu layar, satu karakter, dan satu musuh.",
                    "     libGDX memanggil create() sekali di awal, render() tiap",
                    "     frame, dan dispose() di akhir, jadi game loop dari bab 01",
                    "     kamu tulis di dalam render().",
                ],
            },
        ],
    },
    {
        "title": "19. Menerbitkan Game: itch.io dan Steam",
        "sections": [
            {
                "body": [
                    "Game yang selesai di laptopmu belum dimainkan siapa-siapa.",
                    "Untuk game PC buatan sendiri, dua tempat rilis yang paling",
                    "realistis untuk pemula adalah itch.io dan Steam. Keduanya",
                    "bisa dipakai bersamaan, tapi aturan mainnya beda jauh.",
                ],
            },
            {
                "heading": "itch.io",
                "body": [
                    "itch.io adalah toko daring untuk game indie. Membuat akun dan",
                    "mengunggah game di sana gratis. Kamu bebas menentukan harga:",
                    "gratis, harga tetap, atau bayar seikhlasnya dengan harga",
                    "minimal.",
                    "",
                    "Bagi hasilnya kamu sendiri yang menentukan, lewat fitur yang",
                    "namanya open revenue sharing. Bawaannya 10% untuk itch.io,",
                    "dan angkanya bisa kamu geser dari 0 sampai 100%. Biaya",
                    "pembayaran dan pajak dihitung terpisah.",
                    "",
                    "Game web (HTML5) bisa dimainkan langsung di halaman itch.io.",
                    "Build web dari Godot, Phaser, Unity, atau GameMaker cukup",
                    "dizip lalu diunggah, dengan index.html di dalamnya.",
                    "",
                    "Untuk unggahan yang sering, itch.io menyediakan butler, alat",
                    "baris perintah yang cuma mengirim bagian berkas yang berubah.",
                    "Formatnya butler push folder pengguna/game:kanal. Nama kanal",
                    "yang memuat windows, linux, mac, atau android otomatis",
                    "ditandai sesuai platformnya.",
                ],
                "bahasa": "terminal",
                "code": """butler login
butler push build/web namamu/game-koin:html5
butler push build/linux namamu/game-koin:linux
butler status namamu/game-koin""",
            },
            {
                "body": [
                    "itch.io juga jadi tempat banyak game jam, misalnya GMTK Game",
                    "Jam. Ikut game jam adalah cara cepat merilis game pertama.",
                    "Temanya diumumkan di awal, waktunya dibatasi, dan peserta lain",
                    "memberi nilai serta komentar untuk gamemu.",
                ],
            },
            {
                "heading": "Steam",
                "body": [
                    "Steam adalah toko game PC terbesar, milik Valve. Untuk",
                    "menjual di sana, kamu mendaftar ke Steamworks, program untuk",
                    "developer Steam. Aturannya:",
                    "",
                    "  - Biaya Steam Direct 100 dolar AS untuk tiap game. Biaya itu",
                    "    dikembalikan sesudah gamenya menghasilkan minimal 1.000",
                    "    dolar AS pendapatan kotor yang disesuaikan, yaitu",
                    "    pendapatan kotor dikurangi refund dan sejenisnya.",
                    "  - Sesudah membayar biaya itu, ada masa tunggu 30 hari",
                    "    sebelum gamenya boleh dirilis.",
                    "  - Halaman toko berstatus Coming Soon wajib tayang minimal dua",
                    "    minggu sebelum rilis.",
                    "  - Halaman toko dan build gamemu diperiksa Valve dulu sebelum",
                    "    boleh tayang.",
                    "  - Potongan standar Valve 30% dari tiap penjualan.",
                    "",
                    "Selama masa Coming Soon, orang bisa menambahkan gamemu ke",
                    "wishlist, dan mereka mendapat pemberitahuan saat gamenya",
                    "rilis. Banyak developer indie memakai masa ini untuk",
                    "mengumpulkan wishlist, misalnya lewat demo di acara Steam",
                    "Next Fest.",
                ],
            },
            {
                "heading": "Steamworks SDK",
                "body": [
                    "Steamworks juga menyediakan SDK untuk fitur seperti",
                    "achievement (lencana pencapaian), statistik pemain, Steam",
                    "Cloud untuk menyimpan berkas save di server, dan papan",
                    "peringkat. SDK aslinya berbahasa C++, dan tiap engine punya",
                    "jembatannya: GodotSteam untuk Godot, Steamworks.NET untuk",
                    "Unity, dan Online Subsystem Steam bawaan Unreal.",
                    "",
                    "Yang sering terlupa: achievement tersimpan di akun",
                    "Steam pemain, terpisah dari berkas save. Pemain yang memuat",
                    "save lama tetap memegang achievement yang sudah terbuka.",
                    "Latihan di bab ini meniru aturan itu.",
                ],
            },
            {
                "heading": "Membandingkan uangnya",
                "body": [
                    "Program di bawah membandingkan perkiraan kasar uang yang",
                    "sampai ke pembuat game seharga 5 dolar AS, untuk 100 dan 400",
                    "kopi terjual. Anggap saja nggak ada refund, dan pajak serta",
                    "biaya transfer belum dihitung.",
                ],
                "code": """// Perkiraan kasar uang yang sampai ke pembuat game, dalam dolar AS.
// Belum dipotong pajak, biaya transfer, dan refund.
const HARGA = 5;

function itch(kopi, bagiHasilPersen) {
  const kotor = kopi * HARGA;
  return kotor - (kotor * bagiHasilPersen) / 100;
}

function steam(kopi) {
  const kotor = kopi * HARGA;
  const bersih = (kotor * 70) / 100;          // potongan standar Valve 30%
  const biayaKembali = kotor >= 1000;          // Steam Direct $100 kembali
  return { uang: biayaKembali ? bersih : bersih - 100, biayaKembali };
}

for (const kopi of [100, 400]) {
  const s = steam(kopi);
  console.log(`${kopi} kopi x $${HARGA}:`);
  console.log(`  itch.io, bagi hasil 10%: $${itch(kopi, 10)}`);
  console.log(`  Steam, potongan 30%:     $${s.uang}` +
    (s.biayaKembali ? " (biaya $100 sudah kembali)" : " (biaya $100 belum kembali)"));
}""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  100 kopi x $5:",
                    "    itch.io, bagi hasil 10%: $450",
                    "    Steam, potongan 30%:     $250 (biaya $100 belum kembali)",
                    "  400 kopi x $5:",
                    "    itch.io, bagi hasil 10%: $1800",
                    "    Steam, potongan 30%:     $1400 (biaya $100 sudah kembali)",
                    "",
                    "Per kopi, itch.io kelihatan lebih menguntungkan. Tapi",
                    "pengunjung Steam jauh lebih banyak, jadi game yang sama sering",
                    "terjual lebih banyak di sana. Banyak developer merilis di",
                    "dua-duanya.",
                ],
            },
            {
                "heading": "Halaman toko dan sesudah rilis",
                "body": [
                    "Halaman toko yang baik memuat gambar kapsul, yaitu gambar",
                    "sampul kecil yang muncul di daftar. Lalu trailer pendek,",
                    "beberapa tangkapan layar, deskripsi singkat yang langsung",
                    "menjelaskan cara bermainnya, dan tag genre yang tepat. Banyak orang",
                    "memutuskan mampir atau nggak dari gambar kapsul dan beberapa",
                    "detik pertama trailer, jadi siapkan keduanya baik-baik.",
                    "",
                    "Sesudah rilis, pekerjaannya masih jalan. Rencanakan",
                    "pembaruan:",
                    "",
                    "  - Beri nomor versi yang jelas, misalnya 1.0.1, dan tulis",
                    "    catatan perubahan (patch notes) di setiap pembaruan.",
                    "  - Jaga supaya berkas save lama tetap terbaca oleh versi",
                    "    baru. Simpan nomor versi di dalam berkas save, supaya",
                    "    versi baru tahu cara membacanya.",
                    "  - Kumpulkan laporan galat dari pemain, misalnya lewat forum",
                    "    komunitas Steam atau kolom komentar di itch.io.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Jalur yang sering ditempuh developer indie: ikut game jam di",
                    "itch.io, mengembangkan game jam yang paling disukai jadi game",
                    "utuh, lalu merilisnya di Steam. Halaman Coming Soon dibuka",
                    "berbulan-bulan sebelumnya supaya wishlist sempat terkumpul.",
                    "",
                    "Kasus kecil: kamu ingin gamemu rilis di Steam tanggal 1",
                    "Desember. Hari ini 1 November, dan biaya Steam Direct belum",
                    "kamu bayar.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Hitung masa tunggunya. Kalau biaya dibayar hari ini, 30",
                    "     hari baru lewat tepat 1 Desember, tanpa sisa waktu sama",
                    "     sekali.",
                    "  2. Hitung syarat halaman toko. Halaman Coming Soon harus",
                    "     tayang minimal dua minggu, dan sebelum itu halamannya",
                    "     harus lolos pemeriksaan Valve.",
                    "  3. Sisakan waktu untuk pemeriksaan build, yang juga",
                    "     dilakukan Valve sebelum tombol rilis bisa ditekan.",
                    "  4. Mundurkan target ke pertengahan Desember atau lebih.",
                    "     Sambil menunggu, rilis versi demo di itch.io untuk",
                    "     mengumpulkan masukan dan bahan trailer.",
                ],
            },
        ],
    },
    {
        "title": "20. Pipeline Grafis: dari Segitiga ke Piksel",
        "sections": [
            {
                "body": [
                    "Semua yang kamu lihat di game 3D, dari karakter sampai rumput,",
                    "disusun dari segitiga. Model mobil di game balap bisa berisi",
                    "puluhan ribu segitiga, dan GPU (prosesor grafis) harus mengubah",
                    "semuanya jadi piksel di layar 60 kali per detik atau lebih.",
                    "",
                    "Kenapa segitiga? Tiga titik selalu terletak di satu bidang datar,",
                    "jadi segitiga nggak pernah melengkung atau terlipat. Persegi,",
                    "lingkaran, dan bentuk lain bisa dipecah jadi beberapa segitiga,",
                    "jadi GPU cukup jago mengerjakan satu bentuk saja.",
                    "",
                    "Jalur yang dilewati segitiga sampai jadi piksel disebut pipeline",
                    "grafis. Bayangkan jalur perakitan di pabrik: tiap pos mengerjakan",
                    "satu tugas, lalu meneruskan hasilnya ke pos berikutnya. Bedanya,",
                    "GPU menjalankan ribuan pekerja di tiap pos sekaligus.",
                ],
            },
            {
                "heading": "Tahap demi tahap",
                "body": [
                    "  1. Vertex processing. Tiap titik sudut (vertex) diproses program",
                    "     kecil bernama vertex shader. Tugas utamanya menghitung posisi",
                    "     titik itu dalam koordinat clip space: empat angka x, y, z, w.",
                    "  2. Perakitan primitif. Tiga vertex dirangkai jadi satu segitiga.",
                    "     Bagian yang keluar dari pandangan kamera dipotong (clipping),",
                    "     dan segitiga yang membelakangi kamera bisa dibuang (backface",
                    "     culling).",
                    "  3. Perspective divide dan viewport. x, y, dan z dibagi w. Hasilnya",
                    "     disebut NDC (normalized device coordinates), rentangnya -1",
                    "     sampai 1, lalu diubah ke koordinat piksel sesuai ukuran",
                    "     jendela.",
                    "  4. Rasterisasi. GPU mencari piksel mana saja yang tertutup",
                    "     segitiga. Tiap piksel yang tertutup menghasilkan satu fragmen,",
                    "     yaitu calon piksel yang membawa nilai campuran dari tiga",
                    "     vertex-nya.",
                    "  5. Fragment processing. Fragment shader menghitung warna tiap",
                    "     fragmen dari tekstur, cahaya, dan bayangan.",
                    "  6. Uji dan pencampuran. Fragmen diuji kedalamannya (depth test)",
                    "     dan dicampur dengan warna yang sudah ada (blending, untuk",
                    "     benda transparan). Yang lolos ditulis ke framebuffer, yaitu",
                    "     gambar yang nanti tampil di layar.",
                    "",
                    "Tahap 1 dan 5 bisa kamu program sendiri lewat shader. Tahap lain",
                    "dikerjakan perangkat keras dengan aturan tetap, istilahnya fixed",
                    "function. Di tahap itu kamu cuma bisa menyetel pilihan, misalnya",
                    "mau memakai depth test atau nggak.",
                ],
            },
            {
                "heading": "Dari clip space ke piksel",
                "code": """// Tiga titik segitiga di clip space: [x, y, z, w]
const segitiga = [
  [-0.5, -0.5, 0.2, 1.0],
  [0.5, -0.5, 0.2, 1.0],
  [0.0, 1.0, 0.8, 2.0],
];
const lebar = 800;
const tinggi = 600;

for (const [x, y, z, w] of segitiga) {
  // 1. perspective divide: clip space -> NDC (-1 sampai 1)
  const nx = x / w;
  const ny = y / w;
  const nz = z / w;
  // 2. viewport transform: NDC -> piksel (sumbu y layar mengarah ke bawah)
  const px = ((nx + 1) / 2) * lebar;
  const py = ((1 - ny) / 2) * tinggi;
  console.log(`NDC (${nx}, ${ny}, ${nz}) -> layar (${px}, ${py})`);
}""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  NDC (-0.5, -0.5, 0.2) -> layar (200, 450)",
                    "  NDC (0.5, -0.5, 0.2) -> layar (600, 450)",
                    "  NDC (0, 0.5, 0.4) -> layar (400, 150)",
                    "",
                    "Titik ketiga punya w = 2, jadi sesudah dibagi, y-nya tinggal 0.5.",
                    "Dengan matriks proyeksi perspektif, w sebuah titik sama dengan",
                    "jaraknya dari kamera. Makin jauh titiknya, makin besar pembaginya,",
                    "dan makin dekat ia ke tengah layar. Begitulah benda jauh tampak",
                    "lebih kecil.",
                    "",
                    "Perhatikan juga rumus py. Di NDC sumbu y mengarah ke atas, tapi di",
                    "layar baris 0 ada di paling atas. Karena itu rumusnya memakai",
                    "1 - ny, dan titik dengan y = -0.5 mendarat di piksel 450, di",
                    "bagian bawah jendela.",
                ],
            },
            {
                "heading": "Depth buffer: siapa yang paling depan",
                "body": [
                    "Kalau dua segitiga menutupi piksel yang sama, mana yang terlihat?",
                    "Cara lama adalah algoritma pelukis: urutkan semua segitiga dari",
                    "yang terjauh, lalu gambar berurutan supaya yang dekat menimpa yang",
                    "jauh. Masalahnya, mengurutkan jutaan segitiga tiap frame itu mahal,",
                    "dan segitiga yang saling menembus nggak bisa diurutkan dengan",
                    "benar.",
                    "",
                    "GPU memakai depth buffer, disebut juga z-buffer: satu angka",
                    "kedalaman untuk tiap piksel, diisi 1.0 (paling jauh) di awal",
                    "frame. Tiap fragmen membandingkan z-nya dengan angka di situ.",
                    "Kalau lebih dekat, warnanya ditulis dan angka kedalamannya",
                    "diganti. Kalau lebih jauh, fragmen itu dibuang.",
                ],
            },
            {
                "heading": "Depth test untuk satu piksel",
                "code": """// Depth buffer satu piksel: simpan z terdekat, buang yang lebih jauh.
const fragmen = [
  { dari: "dinding", z: 0.9, warna: "abu" },
  { dari: "pemain", z: 0.4, warna: "merah" },
  { dari: "pohon", z: 0.6, warna: "hijau" },
];

let kedalaman = 1.0; // nilai awal: paling jauh
let warna = "hitam";
for (const f of fragmen) {
  if (f.z < kedalaman) {
    kedalaman = f.z;
    warna = f.warna;
    console.log(`${f.dari}: lolos, z = ${f.z}`);
  } else {
    console.log(`${f.dari}: dibuang, ${f.z} >= ${kedalaman}`);
  }
}
console.log(`piksel akhir: ${warna}`);""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  dinding: lolos, z = 0.9",
                    "  pemain: lolos, z = 0.4",
                    "  pohon: dibuang, 0.6 >= 0.4",
                    "  piksel akhir: merah",
                    "",
                    "Pohon datang paling akhir, tapi tetap kalah dari pemain yang lebih",
                    "dekat. Urutan menggambar benda padat jadi nggak penting lagi.",
                    "",
                    "Jebakan: depth buffer menyimpan angka dengan presisi terbatas. Dua",
                    "permukaan yang hampir berimpit, misalnya poster di tembok, bisa",
                    "bergantian menang tiap frame dan tampak berkedip belang. Gejala",
                    "ini disebut z-fighting.",
                ],
            },
            {
                "heading": "Ruang koordinat dan matriks MVP",
                "body": [
                    "Sebelum sampai ke clip space, sebuah titik melewati beberapa ruang",
                    "koordinat:",
                    "",
                    "  model (lokal) -> world -> view (kamera) -> clip -> NDC -> layar",
                    "",
                    "Tiap perpindahan ruang dikerjakan dengan perkalian matriks 4x4.",
                    "Matriks model menaruh benda di dunia, matriks view menggeser dunia",
                    "supaya kamera ada di titik nol, dan matriks proyeksi membentuk",
                    "perspektif. Ketiganya sering digabung jadi satu matriks MVP",
                    "(model-view-projection) yang dipakai vertex shader. Prinsipnya sama",
                    "dengan materi Transformasi: Translasi, Rotasi, dan Skala di bab",
                    "Matematika Game 2D, cuma ditambah satu dimensi.",
                    "",
                    "Engine seperti Unity, Godot, dan Unreal mengurus semua tahap ini",
                    "untukmu. Tapi begitu ada yang salah, kamu perlu menebak tahap mana",
                    "yang bermasalah. Posisi yang salah biasanya urusan vertex dan",
                    "matriks. Warna aneh biasanya urusan fragment shader. Benda yang",
                    "hilang sebagian sering urusan clipping, culling, atau depth test.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Setiap game 3D di ponsel dan PC melewati pipeline ini, lewat engine",
                    "maupun langsung. Alat debug grafis RenderDoc, yang gratis dan open",
                    "source, bisa merekam satu frame lalu menunjukkan isi tiap tahap:",
                    "vertex yang masuk, hasil vertex shader, sampai isi depth buffer.",
                    "Developer grafis memakainya untuk mencari kenapa sebuah benda nggak",
                    "tampil.",
                    "",
                    "Kasus kecil: di game buatanmu, poster yang ditempel di tembok",
                    "berkedip belang-belang setiap kali kamera bergerak.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Kenali gejalanya. Dua permukaan hampir berimpit dan berebut",
                    "     menang di depth test, jadi ini z-fighting. Teksturnya sendiri",
                    "     nggak bermasalah.",
                    "  2. Cek jarak poster ke tembok. Kalau nol, geser poster sedikit ke",
                    "     depan, misalnya 0.01 satuan ke arah luar tembok.",
                    "  3. Cek near plane kamera. Near plane yang terlalu kecil, misalnya",
                    "     0.001, membuang banyak presisi depth untuk benda yang jauh.",
                    "     Naikkan ke 0.1 kalau kamera nggak perlu sedekat itu.",
                    "  4. Kalau poster harus menempel rapat, pakai fitur decal atau",
                    "     polygon offset dari engine, yang dibuat untuk kasus ini.",
                ],
            },
        ],
    },
    {
        "title": "21. Rasterizer Perangkat Lunak",
        "sections": [
            {
                "body": [
                    "Rasterizer adalah bagian pipeline yang menjawab satu pertanyaan:",
                    "piksel mana saja yang tertutup segitiga ini? Di GPU, tahap ini",
                    "dikerjakan perangkat keras khusus. Di materi ini kita menulisnya",
                    "sendiri dengan JavaScript, tanpa GPU, supaya kelihatan apa yang",
                    "terjadi di dalamnya.",
                    "",
                    "Rasterizer zaman dulu bekerja baris demi baris (scanline): cari",
                    "titik masuk dan titik keluar segitiga di tiap baris, lalu isi",
                    "piksel di antaranya. GPU modern memakai cara yang lebih gampang",
                    "dijalankan paralel, yaitu menguji tiap piksel secara terpisah",
                    "dengan edge function. Karena tiap piksel diuji sendiri-sendiri,",
                    "ribuan piksel bisa diuji bersamaan.",
                ],
            },
            {
                "heading": "Edge function",
                "body": [
                    "Edge function menghitung di sisi mana sebuah titik p berada",
                    "terhadap garis dari a ke b:",
                    "",
                    "  tepi(a, b, p) = (b.x - a.x) * (p.y - a.y) - (b.y - a.y) * (p.x - a.x)",
                    "",
                    "Hasilnya positif kalau p ada di satu sisi garis, negatif di sisi",
                    "lain, dan nol kalau p tepat di garis. Angka ini juga sama dengan",
                    "dua kali luas segitiga a, b, p, lengkap dengan tanda arahnya.",
                    "",
                    "Segitiga punya tiga tepi. Kalau titik sudutnya disusun searah jarum",
                    "jam di layar (sumbu y ke bawah), titik di dalam segitiga memberi",
                    "angka positif untuk ketiga tepi sekaligus. Satu saja negatif",
                    "berarti titik itu ada di luar.",
                    "",
                    "Yang diuji adalah pusat piksel, yaitu (x + 0.5, y + 0.5). Piksel",
                    "itu kotak selebar satu satuan, dan ia dianggap tertutup kalau",
                    "pusat kotaknya ada di dalam segitiga.",
                ],
            },
            {
                "heading": "Rasterizer ASCII",
                "code": """// Edge function: positif kalau p di sisi kanan garis a->b
// (dengan sumbu y layar mengarah ke bawah).
function tepi(a, b, p) {
  return (b.x - a.x) * (p.y - a.y) - (b.y - a.y) * (p.x - a.x);
}

const A = { x: 2, y: 1 };
const B = { x: 17, y: 4 };
const C = { x: 6, y: 9 };
const lebar = 20;
const tinggi = 10;

for (let y = 0; y < tinggi; y++) {
  let baris = "";
  for (let x = 0; x < lebar; x++) {
    const p = { x: x + 0.5, y: y + 0.5 }; // pusat piksel
    const w0 = tepi(B, C, p);
    const w1 = tepi(C, A, p);
    const w2 = tepi(A, B, p);
    baris += w0 >= 0 && w1 >= 0 && w2 >= 0 ? "#" : ".";
  }
  console.log(baris);
}""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  ....................",
                    "  ..###...............",
                    "  ...#######..........",
                    "  ...############.....",
                    "  ....############....",
                    "  ....##########......",
                    "  .....#######........",
                    "  .....####...........",
                    "  ......#.............",
                    "  ....................",
                    "",
                    "Program ini menguji semua 200 piksel. Rasterizer sungguhan",
                    "menghemat kerja dengan kotak pembatas (bounding box): cukup uji",
                    "piksel di antara x dan y terkecil sampai terbesar dari tiga titik",
                    "segitiga. Untuk segitiga ini kotaknya x 2 sampai 17 dan y 1 sampai",
                    "9, jadi lebih dari seperempat piksel bisa dilewati tanpa diuji.",
                ],
            },
            {
                "heading": "Koordinat barycentric",
                "body": [
                    "Tiga angka hasil edge function punya kegunaan kedua. Kalau",
                    "masing-masing dibagi luas segitiga, hasilnya tiga bobot yang",
                    "jumlahnya selalu 1. Bobot ini disebut koordinat barycentric, yaitu",
                    "seberapa dekat titik p ke tiap sudut segitiga.",
                    "",
                    "Di sudut A, bobot A bernilai 1 dan dua lainnya 0. Di titik tengah",
                    "segitiga, ketiganya kira-kira sepertiga. Dengan bobot ini, nilai",
                    "apa pun yang menempel di tiap vertex bisa dicampur untuk piksel di",
                    "antaranya: warna, koordinat tekstur, normal, atau kedalaman.",
                    "Proses mencampur ini disebut interpolasi.",
                ],
            },
            {
                "heading": "Mencampur warna tiga sudut",
                "code": """function tepi(a, b, p) {
  return (b.x - a.x) * (p.y - a.y) - (b.y - a.y) * (p.x - a.x);
}

const A = { x: 2, y: 1, warna: [255, 0, 0] }; // merah
const B = { x: 17, y: 4, warna: [0, 255, 0] }; // hijau
const C = { x: 6, y: 9, warna: [0, 0, 255] }; // biru
const luas = tepi(A, B, C);

const p = { x: 8.5, y: 4.5 }; // pusat piksel (8, 4)
const l0 = tepi(B, C, p) / luas; // bobot titik A
const l1 = tepi(C, A, p) / luas; // bobot titik B
const l2 = tepi(A, B, p) / luas; // bobot titik C

const warna = [0, 1, 2].map((i) =>
  Math.round(l0 * A.warna[i] + l1 * B.warna[i] + l2 * C.warna[i])
);
console.log(`luas x2 = ${luas}`);
console.log(`bobot = ${l0.toFixed(3)} ${l1.toFixed(3)} ${l2.toFixed(3)}`);
console.log(`jumlah bobot = ${(l0 + l1 + l2).toFixed(3)}`);
console.log(`warna piksel = rgb(${warna.join(", ")})`);""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  luas x2 = 108",
                    "  bobot = 0.343 0.352 0.306",
                    "  jumlah bobot = 1.000",
                    "  warna piksel = rgb(87, 90, 78)",
                    "",
                    "Piksel (8, 4) sedikit lebih dekat ke B daripada ke C, jadi",
                    "hijaunya sedikit lebih kuat daripada birunya.",
                    "",
                    "Untuk gambar 3D ada satu tambahan: interpolasi harus memperhitungkan",
                    "perspektif (perspective-correct interpolation). Tanpa itu, tekstur",
                    "lantai yang memanjang ke kejauhan tampak melengkung. GPU",
                    "mengatasinya dengan membagi tiap nilai dengan w sebelum",
                    "diinterpolasi, lalu mengembalikan skalanya sesudahnya.",
                ],
            },
            {
                "heading": "Z-buffer dan aturan tepi atas-kiri",
                "body": [
                    "Kedalaman juga diinterpolasi dengan bobot yang sama, lalu",
                    "dibandingkan dengan isi z-buffer seperti di materi sebelumnya. Jadi",
                    "rasterizer lengkap cuma butuh tiga langkah per piksel: uji tiga",
                    "tepi, hitung bobot, lalu uji kedalaman.",
                    "",
                    "Ada satu kasus yang belum ditangani contoh tadi: pusat piksel yang",
                    "jatuh tepat di tepi, sehingga hasil edge function-nya nol. Dua",
                    "segitiga yang berbagi tepi akan sama-sama menggambar piksel itu.",
                    "Untuk benda transparan, piksel di sepanjang sambungan jadi",
                    "tergambar dua kali dan tampak lebih pekat.",
                    "",
                    "GPU memakai aturan tepi atas-kiri (top-left rule): piksel yang",
                    "tepat di tepi cuma milik segitiga yang tepinya berada di atas atau",
                    "di kiri. Dengan begitu setiap piksel di sambungan digambar tepat",
                    "satu kali. Latihan Rasterizer Segitiga ASCII di bab ini memintamu",
                    "menerapkan aturan itu.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Rasterizer perangkat lunak masih dipakai sampai sekarang. Di Linux,",
                    "proyek Mesa punya driver llvmpipe yang menjalankan OpenGL",
                    "sepenuhnya di CPU. Driver itu yang aktif di mesin virtual atau",
                    "server CI tanpa GPU. Beberapa engine juga merasterisasi versi",
                    "sederhana sebuah adegan di CPU untuk mencari benda yang tertutup",
                    "benda lain, supaya benda itu nggak perlu dikirim ke GPU.",
                    "",
                    "Kasus kecil: kamu menggambar jendela kaca dari dua segitiga yang",
                    "membentuk persegi dengan rasterizer buatanmu. Di sepanjang",
                    "diagonalnya muncul garis tipis yang lebih gelap.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Curigai piksel yang tergambar dua kali. Kaca transparan",
                    "     dicampur dengan warna di belakangnya, jadi piksel yang digambar",
                    "     dua kali tampak lebih pekat.",
                    "  2. Cek syarat di rasterizer-mu. Kalau syaratnya w >= 0 untuk",
                    "     ketiga tepi, pusat piksel yang tepat di diagonal masuk ke kedua",
                    "     segitiga.",
                    "  3. Terapkan aturan atas-kiri: kalau w bernilai 0, piksel cuma",
                    "     dihitung masuk jika tepinya tepi atas atau tepi kiri.",
                    "  4. Uji dengan dua segitiga yang berbagi diagonal. Jumlah piksel",
                    "     keduanya harus sama dengan jumlah piksel persegi, tanpa sisa",
                    "     dan tanpa dobel.",
                ],
            },
        ],
    },
    {
        "title": "22. Shader, GLSL, dan HLSL",
        "sections": [
            {
                "body": [
                    "Shader adalah program kecil yang berjalan di GPU. Namanya berasal",
                    "dari shading, yaitu menghitung terang gelap permukaan. Sekarang",
                    "shader dipakai untuk apa saja yang dikerjakan GPU: menggeser",
                    "vertex, memberi warna, sampai menghitung gerak partikel.",
                    "",
                    "Bedanya dengan program biasa: satu shader dijalankan ribuan kali",
                    "secara paralel, sekali untuk tiap vertex atau tiap piksel. Tiap",
                    "panggilan nggak tahu apa yang dikerjakan panggilan lain. Ia cuma",
                    "menerima data untuk satu vertex atau satu piksel, lalu",
                    "mengembalikan hasilnya.",
                    "",
                    "Dua jenis yang wajib kamu kenal:",
                    "  - Vertex shader: dijalankan sekali per vertex. Masukannya posisi",
                    "    dan data vertex lain, keluarannya posisi di clip space plus",
                    "    data yang mau diteruskan.",
                    "  - Fragment shader (di DirectX disebut pixel shader): dijalankan",
                    "    sekali per fragmen hasil rasterisasi. Keluarannya warna.",
                    "",
                    "Ada juga compute shader untuk perhitungan umum yang nggak",
                    "menggambar apa-apa, plus jenis yang jarang disentuh pemula seperti",
                    "geometry shader, tessellation, mesh shader, dan shader ray tracing.",
                ],
            },
            {
                "heading": "Tiga jenis masukan",
                "body": [
                    "  - Atribut: data yang berbeda untuk tiap vertex, misalnya posisi,",
                    "    warna, dan koordinat tekstur (UV).",
                    "  - Uniform: data yang sama untuk semua vertex dan fragmen dalam",
                    "    satu perintah gambar (draw call), misalnya waktu, posisi kamera,",
                    "    atau matriks MVP.",
                    "  - Varying: keluaran vertex shader yang diteruskan ke fragment",
                    "    shader. Rasterizer menginterpolasinya dengan koordinat",
                    "    barycentric dari materi sebelumnya, jadi tiap fragmen menerima",
                    "    nilai campuran dari tiga vertex.",
                    "",
                    "Di GLSL modern, varying ditulis dengan kata kunci out di vertex",
                    "shader dan in di fragment shader. Kata kunci lamanya, varying,",
                    "masih sering muncul di tutorial WebGL 1.",
                ],
            },
            {
                "heading": "Vertex shader (GLSL ES 3.00 untuk WebGL 2)",
                "bahasa": "glsl",
                "code": """#version 300 es
in vec2 aPosisi;      // atribut: beda untuk tiap vertex
in vec2 aUV;
uniform float uWaktu; // uniform: sama untuk semua vertex di satu draw call
out vec2 vUV;         // varying: diteruskan ke fragment shader

void main() {
    vUV = aUV;
    float goyang = sin(uWaktu) * 0.1;
    gl_Position = vec4(aPosisi.x + goyang, aPosisi.y, 0.0, 1.0);
}""",
            },
            {
                "heading": "Fragment shader",
                "bahasa": "glsl",
                "code": """#version 300 es
precision mediump float;
in vec2 vUV;          // nilainya sudah diinterpolasi rasterizer
uniform vec2 uPusat;
out vec4 warnaKeluar;

void main() {
    float jarak = distance(vUV, uPusat);
    float terang = max(0.0, 1.0 - jarak * 2.5);
    warnaKeluar = vec4(vec3(terang), 1.0);
}""",
            },
            {
                "body": [
                    "Baris #version 300 es wajib ada di baris pertama shader WebGL 2.",
                    "Baris precision mediump float mengatur ketelitian angka pecahan di",
                    "fragment shader. GLSL ES mewajibkannya, GLSL versi desktop nggak.",
                    "gl_Position adalah keluaran wajib vertex shader, yaitu posisi clip",
                    "space yang dibahas di materi pipeline.",
                    "",
                    "Fragment shader di atas menghitung jarak tiap piksel ke titik",
                    "uPusat. Makin dekat, makin terang. Supaya hasilnya kelihatan tanpa",
                    "GPU, fungsi yang sama dijalankan di bawah ini dengan JavaScript,",
                    "satu panggilan untuk tiap huruf di layar teks.",
                ],
            },
            {
                "heading": "Fragment shader versi CPU",
                "code": """// "Fragment shader" versi CPU: fungsi ini dipanggil sekali per piksel.
// GPU menjalankan ribuan panggilan seperti ini sekaligus.
function fragmen(u, v, uPusat) {
  const dx = u - uPusat[0];
  const dy = v - uPusat[1];
  const jarak = Math.sqrt(dx * dx + dy * dy);
  return Math.max(0, 1 - jarak * 2.5); // terang di tengah, gelap di tepi
}

const tangga = ".:-=+*#%@"; // dari gelap ke terang
const lebar = 32;
const tinggi = 11;
const uPusat = [0.5, 0.5]; // uniform: sama untuk semua piksel

for (let y = 0; y < tinggi; y++) {
  let baris = "";
  for (let x = 0; x < lebar; x++) {
    const u = (x + 0.5) / lebar; // koordinat 0..1, mirip varying vUV
    const v = (y + 0.5) / tinggi;
    const terang = fragmen(u, v, uPusat);
    baris += tangga[Math.min(tangga.length - 1, Math.floor(terang * tangga.length))];
  }
  console.log(baris);
}""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  ................................",
                    "  ................................",
                    "  .........::----------::.........",
                    "  ......::--==++++++++==--::......",
                    "  .....:--==+**######**+==--:.....",
                    "  .....:-==+**#%%@@%%#**+==-:.....",
                    "  .....:--==+**######**+==--:.....",
                    "  ......::--==++++++++==--::......",
                    "  .........::----------::.........",
                    "  ................................",
                    "  ................................",
                    "",
                    "Di sini fungsi fragmen dipanggil 352 kali. Layar Full HD punya",
                    "sekitar dua juta piksel, dan GPU menjalankan fragment shader untuk",
                    "semuanya 60 kali per detik. Makanya kode shader harus ringkas:",
                    "satu baris tambahan ikut dikalikan dua juta.",
                ],
            },
            {
                "heading": "HLSL dan bahasa shader lain",
                "body": [
                    "Tiap API grafis punya bahasa shader sendiri, walaupun isinya mirip:",
                    "bahasa bergaya C dengan tipe vektor dan matriks bawaan. Ini",
                    "fragment shader yang sama dalam HLSL, bahasa shader DirectX:",
                ],
            },
            {
                "heading": "Pixel shader HLSL",
                "bahasa": "hlsl",
                "code": """cbuffer Konstanta : register(b0)
{
    float2 uPusat;
};

struct PSInput
{
    float4 posisi : SV_Position;
    float2 uv     : TEXCOORD0;
};

float4 PSMain(PSInput masuk) : SV_Target
{
    float jarak = distance(masuk.uv, uPusat);
    float terang = max(0.0, 1.0 - jarak * 2.5);
    return float4(terang, terang, terang, 1.0);
}""",
            },
            {
                "heading": "Dan dalam WGSL (WebGPU)",
                "bahasa": "teks",
                "code": """@group(0) @binding(0) var<uniform> uPusat : vec2f;

@fragment
fn fs_main(@location(0) uv : vec2f) -> @location(0) vec4f {
    let jarak = distance(uv, uPusat);
    let terang = max(0.0, 1.0 - jarak * 2.5);
    return vec4f(terang, terang, terang, 1.0);
}""",
            },
            {
                "body": [
                    "Peta bahasa shader yang akan kamu temui:",
                    "",
                    "  Bahasa    Dipakai di                      Catatan",
                    "  GLSL      OpenGL, Vulkan                  milik Khronos",
                    "  GLSL ES   OpenGL ES, WebGL                wajib baris precision",
                    "  HLSL      DirectX, juga Vulkan lewat DXC  milik Microsoft",
                    "  MSL       Metal                           berbasis C++",
                    "  WGSL      WebGPU                          sintaks mirip Rust",
                    "",
                    "Vulkan nggak membaca teks shader. Ia menerima SPIR-V, format biner",
                    "perantara. Kamu menulis GLSL atau HLSL, lalu compiler seperti",
                    "glslang atau DXC mengubahnya ke format itu. DirectX punya format",
                    "perantara sendiri, tapi Microsoft mengumumkan pada September 2024",
                    "bahwa DirectX 12 akan menerima SPIR-V mulai Shader Model 7.",
                    "",
                    "Di engine, kamu jarang menulis shader dari nol. Unity memakai HLSL",
                    "plus editor visual Shader Graph. Unreal punya Material Editor",
                    "berbasis node yang menghasilkan HLSL. Godot punya bahasa shader",
                    "sendiri yang mirip GLSL. Ada juga Slang, bahasa shader yang sejak",
                    "akhir 2024 dikelola Khronos dan bisa dikompilasi ke banyak API.",
                    "",
                    "Jebakan: percabangan if di shader bisa mahal. GPU menjalankan",
                    "sekelompok panggilan dengan instruksi yang sama secara serentak.",
                    "Kalau sebagian kelompok masuk cabang if dan sebagian lagi ke else,",
                    "GPU mengerjakan kedua cabang lalu membuang hasil yang nggak",
                    "dipakai. Fungsi mix, step, dan clamp sering bisa menggantikan if.",
                    "",
                    "Jebakan: error shader baru ketahuan saat program berjalan, karena",
                    "driver mengompilasi shader ketika aplikasi memintanya. Di WebGL,",
                    "selalu cek gl.getShaderInfoLog sesudah compileShader. Tanpa itu",
                    "yang kamu lihat cuma layar kosong.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Shadertoy adalah situs tempat orang berbagi fragment shader GLSL",
                    "yang langsung jalan di browser lewat WebGL. Banyak efek di sana,",
                    "dari awan sampai ombak laut, dibuat dari satu fragment shader tanpa",
                    "model 3D. Di game, shader yang paling sering ditulis justru yang",
                    "sederhana: kilat putih saat musuh kena pukul, efek terbakar, atau",
                    "permukaan air yang bergoyang.",
                    "",
                    "Kasus kecil: musuh di game 2D-mu harus berkedip putih selama 0,1",
                    "detik setiap kena serangan, tanpa membuat gambar sprite kedua.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tambahkan uniform float uKilat di fragment shader sprite.",
                    "     Nilainya 1.0 saat kena serangan dan 0.0 dalam keadaan biasa.",
                    "  2. Di fragment shader, campur warna tekstur dengan putih memakai",
                    "     mix, tanpa if:",
                    "       vec4 asli = texture(uTekstur, vUV);",
                    "       warnaKeluar = vec4(mix(asli.rgb, vec3(1.0), uKilat), asli.a);",
                    "  3. Di kode game, set uKilat ke 1.0 saat musuh terkena, lalu",
                    "     kembalikan ke 0.0 sesudah 0,1 detik. Hitung waktunya dengan",
                    "     delta time, jangan dengan jumlah frame.",
                    "  4. Nilai alfa asli.a tetap dipakai, jadi bagian sprite yang",
                    "     transparan nggak ikut berubah jadi kotak putih.",
                ],
            },
        ],
    },
    {
        "title": "23. OpenGL, OpenGL ES, dan WebGL",
        "sections": [
            {
                "body": [
                    "OpenGL adalah API grafis lintas platform yang lahir tahun 1992 dari",
                    "perusahaan Silicon Graphics, dan sejak 2006 dikelola konsorsium",
                    "Khronos Group. OpenGL sendiri cuma spesifikasi, yaitu dokumen yang",
                    "menjelaskan fungsi apa saja yang harus ada dan apa hasilnya. Yang",
                    "menulis kodenya adalah pembuat driver GPU, misalnya NVIDIA, AMD,",
                    "Intel, atau proyek Mesa di Linux.",
                    "",
                    "Versi-versi pentingnya:",
                    "  - 1.x: pipeline tetap. Belum ada shader; kamu cuma bisa menyalakan",
                    "    dan mematikan fitur seperti cahaya dan kabut.",
                    "  - 2.0 (2004): GLSL diperkenalkan, shader bisa ditulis sendiri.",
                    "  - 3.3 (2010): titik awal yang biasa dipakai tutorial modern,",
                    "    memakai core profile yang membuang fungsi-fungsi lama.",
                    "  - 4.6 (2017): versi terakhir. Revisi spesifikasinya yang terbaru",
                    "    bertanggal 5 Mei 2022, dan versi ini bisa memuat shader SPIR-V.",
                ],
            },
            {
                "heading": "Gaya mesin keadaan",
                "body": [
                    "OpenGL bekerja sebagai mesin keadaan (state machine). Kamu mengikat",
                    "(bind) sebuah objek dulu, lalu perintah berikutnya berlaku ke objek",
                    "yang sedang terikat. Mirip tombol tebal di pengolah kata: Ctrl+B",
                    "berlaku ke teks yang sedang diblok, apa pun teks yang ada di",
                    "pikiranmu.",
                    "",
                    "Contoh di bawah menggambar satu segitiga oranye dengan WebGL 2,",
                    "versi OpenGL untuk browser. Perhatikan pasangan bindBuffer lalu",
                    "bufferData.",
                ],
            },
            {
                "heading": "Segitiga pertama di WebGL 2",
                "bahasa": "browser",
                "code": """const kanvas = document.querySelector("canvas");
const gl = kanvas.getContext("webgl2");
if (!gl) throw new Error("Browser ini tidak mendukung WebGL 2");

const sumberVertex = `#version 300 es
in vec2 aPosisi;
void main() { gl_Position = vec4(aPosisi, 0.0, 1.0); }`;

const sumberFragmen = `#version 300 es
precision mediump float;
out vec4 warna;
void main() { warna = vec4(1.0, 0.6, 0.1, 1.0); }`;

function kompilasi(jenis, sumber) {
  const s = gl.createShader(jenis);
  gl.shaderSource(s, sumber);
  gl.compileShader(s);
  if (!gl.getShaderParameter(s, gl.COMPILE_STATUS)) {
    throw new Error(gl.getShaderInfoLog(s));
  }
  return s;
}

const program = gl.createProgram();
gl.attachShader(program, kompilasi(gl.VERTEX_SHADER, sumberVertex));
gl.attachShader(program, kompilasi(gl.FRAGMENT_SHADER, sumberFragmen));
gl.linkProgram(program);
gl.useProgram(program);

// Data vertex dikirim ke memori GPU lewat buffer
const titik = new Float32Array([-0.5, -0.5, 0.5, -0.5, 0.0, 0.5]);
const buffer = gl.createBuffer();
gl.bindBuffer(gl.ARRAY_BUFFER, buffer); // buffer ini yang sekarang terikat
gl.bufferData(gl.ARRAY_BUFFER, titik, gl.STATIC_DRAW); // mengisi yang terikat

const lokasi = gl.getAttribLocation(program, "aPosisi");
gl.enableVertexAttribArray(lokasi);
gl.vertexAttribPointer(lokasi, 2, gl.FLOAT, false, 0, 0);

gl.clearColor(0.05, 0.05, 0.1, 1.0);
gl.clear(gl.COLOR_BUFFER_BIT);
gl.drawArrays(gl.TRIANGLES, 0, 3);""",
            },
            {
                "body": [
                    "bufferData nggak menerima parameter buffer mana yang mau diisi. Ia",
                    "mengisi buffer yang sedang terikat ke gl.ARRAY_BUFFER. Begitu pula",
                    "vertexAttribPointer: ia membaca dari buffer yang terikat saat",
                    "dipanggil.",
                    "",
                    "Jebakan: lupa satu bindBuffer berarti data masuk ke buffer yang",
                    "salah, dan OpenGL nggak memberi pesan error apa pun. Gejalanya",
                    "benda yang muncul dengan bentuk benda lain, atau nggak muncul sama",
                    "sekali.",
                    "",
                    "Kode ini butuh elemen <canvas> di halaman HTML. Taruh di dalam",
                    "tag <script> sesudah kanvasnya, lalu buka halamannya di browser.",
                ],
            },
            {
                "heading": "OpenGL ES",
                "body": [
                    "OpenGL ES (Embedded Systems) adalah versi OpenGL yang dirampingkan",
                    "untuk ponsel, konsol genggam, mobil, dan perangkat tertanam. Fungsi",
                    "lama dibuang, jadi sejak ES 2.0 (2007) semua gambar wajib memakai",
                    "shader. Versi terbarunya ES 3.2 (2015), dengan revisi spesifikasi",
                    "terbaru bertanggal 5 Mei 2022, sama dengan OpenGL 4.6.",
                    "",
                    "Di Android, peran ini sedang diambil alih Vulkan. Dokumentasi",
                    "Android menyebut OpenGL ES masih didukung tapi nggak lagi",
                    "dikembangkan fiturnya. Mulai Android 15 ada ANGLE, lapisan yang",
                    "menjalankan OpenGL ES di atas Vulkan, dan Google menyatakan",
                    "rencananya: pada akhirnya OpenGL ES di Android cuma tersedia lewat",
                    "lapisan itu. Aplikasi lama tetap jalan, tapi untuk game Android",
                    "baru, Vulkan pilihan utamanya.",
                ],
            },
            {
                "heading": "WebGL",
                "body": [
                    "WebGL membawa OpenGL ES ke browser lewat elemen <canvas> dan",
                    "JavaScript. WebGL 1.0 (2011) mengikuti OpenGL ES 2.0, sedangkan",
                    "WebGL 2.0 mengikuti OpenGL ES 3.0. WebGL 2 tersedia di semua",
                    "browser besar sejak Safari ikut menyalakannya di versi 15 (2021).",
                    "",
                    "Browser jarang memanggil OpenGL langsung. Chrome memakai lapisan",
                    "penerjemah ANGLE yang mengubah panggilan WebGL ke Direct3D 11 di",
                    "Windows dan ke Metal di Mac. Safari juga memakainya dengan Metal,",
                    "dan Firefox memakainya di Windows. Karena itu satu kode",
                    "WebGL bisa jalan di laptop Windows, MacBook, dan ponsel tanpa",
                    "diubah.",
                    "",
                    "Hampir nggak ada yang menulis WebGL mentah untuk proyek besar.",
                    "Three.js dan Babylon.js membungkusnya jadi objek seperti kamera,",
                    "mesh, dan cahaya. Build Web dari Unity juga menggambar dengan",
                    "WebGL 2.",
                ],
            },
            {
                "heading": "Status sekarang",
                "bahasa": "teks",
                "code": """API          Versi terakhir    Platform utama          Status
OpenGL       4.6 (2017)        Windows, Linux          nggak ada versi baru
OpenGL ES    3.2 (2015)        Android, perangkat      dipertahankan,
                               tertanam                Android pindah ke Vulkan
WebGL        2.0 (= ES 3.0)    semua browser besar     stabil, penerus: WebGPU
macOS        OpenGL 4.1        Mac                     usang sejak 2018""",
            },
            {
                "body": [
                    "Apple menandai OpenGL usang di macOS 10.14 (2018), dan versi yang",
                    "tersedia di Mac berhenti di 4.1. Di Linux, Mesa mendukung OpenGL",
                    "4.6 untuk GPU modern, dan punya driver Zink yang menjalankan OpenGL",
                    "di atas Vulkan. Khronos sendiri menempatkan Vulkan sebagai",
                    "penerusnya.",
                    "",
                    "Kapan masih memilih OpenGL? Untuk belajar konsep grafis, OpenGL 3.3",
                    "dengan tutorial seperti learnopengl.com masih jalur yang ramah.",
                    "Kodenya jauh lebih pendek daripada Vulkan, dan konsepnya (buffer,",
                    "shader, tekstur, framebuffer) terbawa ke API mana pun. Pustaka",
                    "raylib juga memakai OpenGL di bawahnya. Untuk proyek baru yang",
                    "serius, pakai engine, atau pilih salah satu API di materi Vulkan,",
                    "Metal, DirectX 12, dan WebGPU.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "WebGL ada di balik peta 3D di browser, konfigurator produk yang",
                    "bisa diputar 360 derajat, game web hasil ekspor Unity, dan",
                    "visualisasi data yang menggambar jutaan titik. Di Android, banyak",
                    "aplikasi dan game lama masih menggambar dengan OpenGL ES.",
                    "",
                    "Kasus kecil: game web buatanmu tampil normal di laptopmu, tapi",
                    "seorang pemain melapor kanvasnya hitam di laptop kantornya.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Cek hasil getContext(\"webgl2\"). Kalau null, browser atau driver",
                    "     di laptop itu menolak WebGL 2, misalnya karena GPU-nya masuk",
                    "     daftar blokir browser atau akselerasi hardware dimatikan.",
                    "  2. Tampilkan pesan yang jelas, jangan biarkan kanvas hitam. Contoh:",
                    "     \"Browser ini belum bisa menjalankan WebGL 2. Coba nyalakan",
                    "     akselerasi hardware di pengaturan browser.\"",
                    "  3. Kalau game-mu sederhana, sediakan jalur cadangan ke",
                    "     getContext(\"webgl\"), yaitu WebGL 1 dengan shader GLSL ES 1.00.",
                    "  4. Minta pemain membuka chrome://gpu, atau about:support di",
                    "     Firefox, untuk melihat apakah WebGL berjalan dengan akselerasi",
                    "     hardware.",
                ],
            },
        ],
    },
    {
        "title": "24. Vulkan, Metal, DirectX 12, dan WebGPU",
        "sections": [
            {
                "body": [
                    "OpenGL dirancang awal 1990-an, saat GPU masih sederhana dan",
                    "program berjalan di satu inti CPU. Driver OpenGL menanggung banyak",
                    "kerja tersembunyi: memeriksa keadaan sebelum tiap perintah gambar,",
                    "mengatur memori GPU, dan menebak kapan data aman dipakai. Tebakan",
                    "itu kadang meleset, dan hasilnya game tersendat sesaat (stutter)",
                    "yang susah dicari penyebabnya.",
                    "",
                    "API generasi baru membalik pembagian kerjanya. Driver dibuat",
                    "setipis mungkin, dan aplikasi yang mengatur sendiri hal-hal yang",
                    "dulu ditebak driver. Istilahnya API eksplisit. Perumpamaannya",
                    "mobil transmisi manual: lebih repot, tapi kamu yang menentukan",
                    "kapan pindah gigi.",
                    "",
                    "Ada empat yang perlu kamu kenal:",
                    "  - Vulkan, dari Khronos, untuk Windows, Linux, dan Android.",
                    "  - DirectX 12, dari Microsoft, untuk Windows dan Xbox.",
                    "  - Metal, dari Apple, untuk semua perangkat Apple.",
                    "  - WebGPU, dari W3C, untuk browser.",
                ],
            },
            {
                "heading": "Konsep yang sama, nama yang beda",
                "body": [
                    "Keempatnya dibangun dari ide yang sama:",
                    "  - Command buffer: daftar perintah gambar yang direkam lebih dulu,",
                    "    lalu dikirim sekaligus ke antrean (queue) GPU. Beberapa thread",
                    "    CPU bisa merekam bersamaan.",
                    "  - Pipeline state object: shader plus semua setelan gambar (format",
                    "    piksel, blending, depth test) yang dikunci dan dikompilasi",
                    "    sekali di awal, jadi nggak perlu diperiksa ulang tiap draw call.",
                    "  - Descriptor atau bind group: daftar sumber daya (buffer, tekstur)",
                    "    yang dibaca shader.",
                    "  - Sinkronisasi eksplisit: fence dan semaphore untuk menandai kapan",
                    "    GPU selesai memakai sebuah data. Di OpenGL, driver yang",
                    "    mengurusnya.",
                ],
            },
            {
                "heading": "Nama konsepnya di tiap API",
                "bahasa": "teks",
                "code": """Konsep      Vulkan          DirectX 12      Metal           WebGPU
perekam     CommandBuffer   CommandList     CommandBuffer   CommandEncoder
pipeline    Pipeline        PipelineState   PipelineState   RenderPipeline
sumber      DescriptorSet   DescriptorHeap  ArgumentBuffer  BindGroup
shader      SPIR-V          DXIL            MSL             WGSL""",
            },
            {
                "heading": "Vulkan",
                "body": [
                    "Vulkan 1.0 rilis Februari 2016 sebagai penerus OpenGL. Versi 1.4",
                    "keluar Desember 2024, dan spesifikasinya terus direvisi. Saat",
                    "materi ini ditulis (Oktober 2026), revisi terbarunya v1.4.365.",
                    "Vulkan jalan di Windows, Linux, dan Android. Di Mac dan iPhone,",
                    "Vulkan bisa dipakai lewat lapisan penerjemah MoltenVK yang",
                    "mengubahnya ke Metal.",
                    "",
                    "Vulkan terkenal panjang. Menggambar satu segitiga butuh ratusan",
                    "baris untuk menyiapkan instance, device, swapchain, pipeline, dan",
                    "sinkronisasi. Tutorial resmi Khronos ada di docs.vulkan.org.",
                    "Validation layers, lapisan pemeriksa yang dipasang selama",
                    "pengembangan, wajib dinyalakan. Tanpa itu, kesalahan kecil sering",
                    "cuma berujung layar hitam atau crash tanpa pesan.",
                    "",
                    "Di Android, Vulkan sekarang API grafis utama. Dokumentasi Android",
                    "menyebut sekitar 85% perangkat Android aktif mendukung Vulkan, dan",
                    "semua perangkat 64-bit sejak Android 10 mendukung Vulkan 1.1.",
                    "",
                    "Potongan di bawah merekam perintah gambar satu segitiga. Semua",
                    "objek yang dipakainya (cmd, pipeline, infoRenderPass) harus dibuat",
                    "lebih dulu dengan puluhan baris lain.",
                ],
            },
            {
                "heading": "Merekam command buffer (C)",
                "bahasa": "c",
                "code": """VkCommandBufferBeginInfo mulai = {
    .sType = VK_STRUCTURE_TYPE_COMMAND_BUFFER_BEGIN_INFO,
};
vkBeginCommandBuffer(cmd, &mulai);
vkCmdBeginRenderPass(cmd, &infoRenderPass, VK_SUBPASS_CONTENTS_INLINE);
vkCmdBindPipeline(cmd, VK_PIPELINE_BIND_POINT_GRAPHICS, pipeline);
vkCmdDraw(cmd, 3, 1, 0, 0); // 3 vertex, 1 instance
vkCmdEndRenderPass(cmd);
vkEndCommandBuffer(cmd);
// Baru di sini perintahnya dikirim ke GPU:
vkQueueSubmit(antrean, 1, &infoSubmit, pagarSelesai);""",
            },
            {
                "heading": "DirectX 12",
                "body": [
                    "Direct3D 12 adalah bagian grafis DirectX 12 dari Microsoft, dipakai",
                    "di Windows 10 ke atas dan Xbox. Shader-nya ditulis dalam HLSL dan",
                    "dikompilasi DXC. Fitur baru dikirim lewat Agility SDK, paket yang",
                    "ikut dikirim bersama game, jadi pemain nggak perlu menunggu",
                    "pembaruan Windows. DirectX 12 Ultimate adalah label untuk kumpulan",
                    "fitur modern: ray tracing (DXR), mesh shader, variable rate",
                    "shading, dan sampler feedback.",
                    "",
                    "Banyak game PC besar memakai DirectX 12 atau pendahulunya, DirectX",
                    "11. Di Linux dan Steam Deck, game seperti itu dijalankan lewat",
                    "Proton, yang menerjemahkan DirectX ke Vulkan dengan DXVK (untuk",
                    "DirectX 9 sampai 11) dan VKD3D-Proton (untuk DirectX 12).",
                ],
            },
            {
                "heading": "Metal",
                "body": [
                    "Metal diperkenalkan Apple tahun 2014 untuk iOS, lalu menyebar ke",
                    "macOS dan semua platform Apple. Shader-nya ditulis dalam Metal",
                    "Shading Language yang berbasis C++. Versi terbarunya, Metal 4,",
                    "diumumkan di WWDC 2025 dan butuh chip A14 atau lebih baru, Mac",
                    "dengan Apple silicon, atau Vision Pro.",
                    "",
                    "Metal cuma jalan di perangkat Apple, dan aplikasinya dibangun",
                    "dengan Xcode di Mac. Dari Fedora kamu nggak bisa mengembangkan",
                    "Metal langsung. Engine seperti Unity, Godot, dan Unreal bisa",
                    "menghasilkan build Metal, tapi langkah build-nya tetap dijalankan",
                    "di Mac.",
                ],
            },
            {
                "heading": "WebGPU",
                "body": [
                    "WebGPU adalah API GPU modern untuk browser, penerus WebGL.",
                    "Desainnya mengikuti tiga API di atas (command encoder, pipeline,",
                    "bind group), tapi dibuat aman untuk web: semua akses memori dicek,",
                    "dan sinkronisasinya diurus browser. Shader-nya ditulis dalam WGSL.",
                    "Selain menggambar, WebGPU mendukung compute shader, jadi bisa",
                    "dipakai menjalankan model machine learning di browser.",
                    "",
                    "Spesifikasinya berstatus W3C Candidate Recommendation Draft, revisi",
                    "15 September 2026. Dukungan browser saat materi ini ditulis:",
                    "  - Chrome dan Edge menyalakannya sejak versi 113 (2023).",
                    "  - Firefox menyalakannya di Windows mulai versi 141 (Juli 2025).",
                    "  - Safari mulai versi 26 (2025).",
                    "",
                    "Di Linux dan sebagian platform lain dukungannya masih bertahap, jadi",
                    "selalu cek navigator.gpu sebelum memakainya. WebGPU juga cuma",
                    "tersedia di halaman HTTPS atau localhost.",
                    "",
                    "WebGPU nggak terbatas di browser. Implementasi milik Chrome bernama",
                    "Dawn (C++), dan milik Firefox bernama wgpu (Rust). Keduanya bisa",
                    "dipakai di aplikasi desktop biasa. Bevy, engine Rust yang dibahas",
                    "di bab berikutnya, menggambar lewat wgpu.",
                ],
            },
            {
                "heading": "Menggandakan angka dengan compute shader",
                "bahasa": "browser",
                "code": """const adapter = await navigator.gpu?.requestAdapter();
if (!adapter) throw new Error("WebGPU belum tersedia di browser ini");
const device = await adapter.requestDevice();

const kodeShader = `
@group(0) @binding(0) var<storage, read_write> data : array<f32>;

@compute @workgroup_size(64)
fn main(@builtin(global_invocation_id) id : vec3u) {
  if (id.x < arrayLength(&data)) {
    data[id.x] = data[id.x] * 2.0;
  }
}`;

const masukan = new Float32Array([1, 2, 3, 4]);
const bufData = device.createBuffer({
  size: masukan.byteLength,
  usage: GPUBufferUsage.STORAGE | GPUBufferUsage.COPY_SRC | GPUBufferUsage.COPY_DST,
});
device.queue.writeBuffer(bufData, 0, masukan);
const bufBaca = device.createBuffer({
  size: masukan.byteLength,
  usage: GPUBufferUsage.MAP_READ | GPUBufferUsage.COPY_DST,
});

const pipeline = device.createComputePipeline({
  layout: "auto",
  compute: { module: device.createShaderModule({ code: kodeShader }), entryPoint: "main" },
});
const bindGroup = device.createBindGroup({
  layout: pipeline.getBindGroupLayout(0),
  entries: [{ binding: 0, resource: { buffer: bufData } }],
});

// Rekam perintah ke command encoder, lalu kirim sekaligus ke antrean GPU
const encoder = device.createCommandEncoder();
const pass = encoder.beginComputePass();
pass.setPipeline(pipeline);
pass.setBindGroup(0, bindGroup);
pass.dispatchWorkgroups(1);
pass.end();
encoder.copyBufferToBuffer(bufData, 0, bufBaca, 0, masukan.byteLength);
device.queue.submit([encoder.finish()]);

await bufBaca.mapAsync(GPUMapMode.READ);
console.log(new Float32Array(bufBaca.getMappedRange())); // [2, 4, 6, 8]""",
            },
            {
                "body": [
                    "Polanya sama dengan API eksplisit lain: siapkan buffer dan pipeline",
                    "sekali, rekam perintah ke command encoder, lalu kirim ke antrean.",
                    "Hasilnya nggak langsung tersedia. mapAsync menunggu sampai GPU",
                    "selesai, baru isi buffer bisa dibaca CPU. Kode ini memakai await di",
                    "tingkat atas, jadi taruh di dalam <script type=\"module\">.",
                ],
            },
            {
                "heading": "Memilih yang mana",
                "body": [
                    "  Target                API yang biasa dipakai",
                    "  Game PC Windows       DirectX 12, kadang Vulkan",
                    "  Android               Vulkan, OpenGL ES untuk perangkat lama",
                    "  iPhone, iPad, Mac     Metal",
                    "  Linux, Steam Deck     Vulkan",
                    "  Browser               WebGPU, dengan WebGL 2 sebagai cadangan",
                    "",
                    "Vulkan dan DirectX 12 bukan pilihan yang bagus sebagai API grafis",
                    "pertama. Pahami konsepnya dulu lewat engine, OpenGL, atau WebGPU,",
                    "yang kodenya jauh lebih pendek. Kalau ingin satu kode untuk banyak",
                    "platform tanpa engine besar, ada lapisan abstraksi seperti wgpu,",
                    "bgfx, dan GPU API milik SDL 3. Engine besar punya lapisan sejenis:",
                    "kamu memilih Vulkan atau DirectX 12 di pengaturan build, dan kode",
                    "game-mu tetap sama.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Steam Deck contoh yang gampang dicek. Konsol genggam ini menjalankan",
                    "Linux, dan game Windows yang dibuat untuk DirectX tetap jalan",
                    "karena Proton menerjemahkan setiap panggilan DirectX ke Vulkan. Di",
                    "Android, engine seperti Unity dan Unreal biasanya memakai Vulkan",
                    "dan menyediakan OpenGL ES sebagai cadangan untuk perangkat lama.",
                    "",
                    "Kasus kecil: kamu membuat visualisasi 3D di browser dengan WebGPU.",
                    "Sebagian pengguna melapor halamannya kosong, padahal di Chrome-mu",
                    "lancar.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Cek apakah navigator.gpu ada dan requestAdapter() mengembalikan",
                    "     adapter. Keduanya bisa gagal: browser lama, Firefox di luar",
                    "     Windows, atau GPU yang diblokir browser.",
                    "  2. Pastikan halamannya dibuka lewat HTTPS. Di halaman http://",
                    "     biasa, navigator.gpu nggak ada sama sekali.",
                    "  3. Sediakan cadangan WebGL 2. Kalau kamu memakai Three.js,",
                    "     WebGPURenderer-nya otomatis pindah ke WebGL 2 saat WebGPU",
                    "     nggak tersedia.",
                    "  4. Catat di log jalur mana yang dipakai tiap pengguna, supaya kamu",
                    "     tahu berapa banyak yang masih bergantung pada WebGL.",
                ],
            },
        ],
    },
    {
        "title": "25. Entity Component System",
        "sections": [
            {
                "body": [
                    "Bayangkan game-mu punya kelas Musuh. Lalu ada musuh yang bisa",
                    "terbang, jadi kamu bikin MusuhTerbang sebagai turunan Musuh. Lalu",
                    "ada musuh yang menembak, jadi lahir MusuhPenembak. Begitu desainer",
                    "minta musuh yang terbang sekaligus menembak, pohon pewarisan mulai",
                    "kusut: kelas barunya turunan dari yang mana?",
                    "",
                    "Pola GameObject dan komponen di Unity, juga pohon node di Godot,",
                    "menjawab masalah itu dengan menempelkan potongan perilaku ke",
                    "objek. ECS (Entity Component System) melangkah lebih jauh: data",
                    "dan logika dipisah total.",
                ],
            },
            {
                "heading": "Tiga bagian ECS",
                "body": [
                    "  - Entity: cuma nomor identitas, misalnya 1, 2, 3. Entitas nggak",
                    "    punya data dan nggak punya method.",
                    "  - Component: data polos tanpa logika, misalnya Posisi {x, y},",
                    "    Kecepatan {x, y}, atau Nyawa 3. Sebuah entitas punya komponen",
                    "    kalau ada data komponen itu yang memakai nomornya.",
                    "  - System: fungsi yang memproses semua entitas dengan kombinasi",
                    "    komponen tertentu. Sistem gerak, misalnya, mengambil semua",
                    "    entitas yang punya Posisi dan Kecepatan, lalu menambahkan",
                    "    kecepatan ke posisi.",
                    "",
                    "Perumpamaan yang gampang: spreadsheet. Tiap baris adalah entitas,",
                    "tiap kolom adalah jenis komponen, dan sel kosong berarti entitas",
                    "itu nggak punya komponen tersebut. Sistem adalah rumus yang",
                    "dijalankan ke semua baris yang kolom-kolom tertentunya terisi.",
                    "",
                    "Perilaku entitas ditentukan komponen yang ia punya. Mau musuh",
                    "terbang yang menembak? Pasang komponen Terbang dan Penembak ke",
                    "entitas yang sama. Mau peluru berhenti? Lepas komponen",
                    "Kecepatan-nya. Nggak ada kelas baru yang perlu dibuat.",
                ],
            },
            {
                "heading": "ECS kecil dengan Map",
                "code": """// Entitas cuma nomor. Komponen disimpan per jenis, dikunci nomor entitas.
const posisi = new Map();
const kecepatan = new Map();
const nyawa = new Map();
let nomorBerikut = 1;

function buat() {
  return nomorBerikut++;
}

const pemain = buat();
posisi.set(pemain, { x: 0, y: 0 });
kecepatan.set(pemain, { x: 2, y: 1 });
nyawa.set(pemain, 3);

const batu = buat(); // punya posisi, tapi nggak bergerak
posisi.set(batu, { x: 5, y: 5 });

const peluru = buat();
posisi.set(peluru, { x: 1, y: 4 });
kecepatan.set(peluru, { x: 4, y: 0 });

// Sistem gerak: semua entitas yang punya Posisi DAN Kecepatan
function sistemGerak() {
  for (const [id, v] of kecepatan) {
    const p = posisi.get(id);
    if (!p) continue;
    p.x += v.x;
    p.y += v.y;
  }
}

for (let tick = 1; tick <= 2; tick++) {
  sistemGerak();
  const isi = [...posisi].map(([id, p]) => `${id}:(${p.x},${p.y})`);
  console.log(`tick ${tick}: ${isi.join(" ")}`);
}
console.log(`entitas bernyawa: ${[...nyawa.keys()].join(", ")}`);""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  tick 1: 1:(2,1) 2:(5,5) 3:(5,4)",
                    "  tick 2: 1:(4,2) 2:(5,5) 3:(9,4)",
                    "  entitas bernyawa: 1",
                    "",
                    "Batu (entitas 2) diam karena nggak punya Kecepatan, jadi sistem",
                    "gerak melewatinya. Sistem gerak juga nggak peduli apakah",
                    "entitasnya pemain atau peluru. Yang ia lihat cuma pasangan Posisi",
                    "dan Kecepatan.",
                ],
            },
            {
                "heading": "Kenapa ECS cepat",
                "body": [
                    "CPU membaca memori ke cache dalam potongan berukuran tetap,",
                    "biasanya 64 byte. Membaca data yang berurutan di memori jauh lebih",
                    "cepat daripada melompat-lompat, karena data berikutnya sudah ikut",
                    "terbawa ke cache.",
                    "",
                    "Di pola objek biasa, tiap objek musuh berisi posisi, kecepatan,",
                    "nama, gambar, suara, dan banyak lagi, dan objek-objek itu tersebar",
                    "di memori. Sistem gerak yang cuma butuh posisi dan kecepatan",
                    "terpaksa ikut membawa data lain ke cache. ECS menyimpan semua",
                    "Posisi berderet dalam satu array, semua Kecepatan di array lain.",
                    "Bentuk ini disebut struct of arrays, lawan dari array of structs:",
                    "",
                    "  array of structs:  [x y vx vy nama ...][x y vx vy nama ...][...]",
                    "  struct of arrays:  x:  [x1  x2  x3  ...]",
                    "                     vx: [vx1 vx2 vx3 ...]",
                    "",
                    "Ada dua cara populer menyusun penyimpanan ECS:",
                    "  - Archetype (tabel): entitas dengan kombinasi komponen yang persis",
                    "    sama disimpan di tabel yang sama. Iterasinya cepat, tapi",
                    "    memasang atau melepas komponen berarti memindahkan entitas ke",
                    "    tabel lain. Unity Entities, Flecs, dan penyimpanan bawaan Bevy",
                    "    memakai cara ini.",
                    "  - Sparse set: tiap jenis komponen punya array padat sendiri plus",
                    "    indeks dari nomor entitas. Memasang dan melepas komponen murah,",
                    "    tapi iterasi gabungan beberapa komponen sedikit lebih lambat.",
                    "    EnTT (C++) memakai cara ini, dan Bevy menyediakannya sebagai",
                    "    pilihan per komponen.",
                    "",
                    "Keuntungan kedua: sistem menyatakan komponen apa yang ia baca dan",
                    "tulis. Dua sistem yang nggak menulis komponen yang sama bisa jalan",
                    "di thread berbeda secara bersamaan. Bevy menjadwalkan sistem",
                    "secara paralel berdasarkan pernyataan itu.",
                    "",
                    "Contoh JavaScript tadi memakai Map, jadi nggak mendapat keuntungan",
                    "cache. Tujuannya cuma memperlihatkan pembagian entitas, komponen,",
                    "dan sistem.",
                ],
            },
            {
                "heading": "Bevy",
                "body": [
                    "Bevy adalah engine game open source berbasis ECS yang ditulis dan",
                    "dipakai dengan Rust. Lisensinya MIT atau Apache-2.0, boleh pilih",
                    "salah satu. Saat materi ini ditulis (Oktober 2026) versi terbarunya",
                    "0.20.0, dirilis 8 Oktober 2026. Bevy belum mencapai 1.0, dan tiap",
                    "rilis minor membawa perubahan yang memutus API. Tutorial untuk",
                    "versi lama sering nggak bisa dipakai apa adanya.",
                ],
            },
            {
                "heading": "Sistem gerak di Bevy",
                "bahasa": "rust",
                "code": """use bevy::prelude::*;

#[derive(Component)]
struct Posisi(Vec2);

#[derive(Component)]
struct Kecepatan(Vec2);

fn munculkan(mut commands: Commands) {
    commands.spawn((Posisi(Vec2::new(0.0, 0.0)), Kecepatan(Vec2::new(2.0, 1.0))));
    commands.spawn(Posisi(Vec2::new(5.0, 5.0))); // batu: tanpa Kecepatan
}

fn gerak(time: Res<Time>, mut query: Query<(&mut Posisi, &Kecepatan)>) {
    for (mut pos, vel) in &mut query {
        pos.0 += vel.0 * time.delta_secs();
    }
}

fn main() {
    App::new()
        .add_plugins(MinimalPlugins)
        .add_systems(Startup, munculkan)
        .add_systems(Update, gerak)
        .run();
}""",
            },
            {
                "body": [
                    "Komponen adalah struct biasa dengan #[derive(Component)]. Sistem",
                    "adalah fungsi biasa, dan parameternya menyatakan apa yang ia",
                    "butuhkan. Query<(&mut Posisi, &Kecepatan)> artinya semua entitas",
                    "yang punya Posisi dan Kecepatan, dengan Posisi boleh diubah. Batu",
                    "yang cuma punya Posisi nggak masuk ke query ini.",
                    "",
                    "Sistem di schedule Update jalan sekali tiap frame, jadi geraknya",
                    "dikali delta time. Untuk fisika, Bevy punya schedule FixedUpdate",
                    "yang secara bawaan jalan 64 kali per detik, konsep yang sama",
                    "dengan materi Fixed Timestep dan Jam Palsu. MinimalPlugins",
                    "menjalankan loop tanpa jendela. Game sungguhan memakai",
                    "DefaultPlugins, yang membuka jendela dan menggambar lewat wgpu.",
                ],
            },
            {
                "heading": "Unity DOTS, RealityKit, dan pustaka ECS lain",
                "body": [
                    "  - Unity: selain GameObject, Unity punya paket Entities. Bersama",
                    "    compiler Burst dan C# Job System, paket ini dikenal dengan nama",
                    "    DOTS (Data-Oriented Technology Stack). Biasa dipakai untuk",
                    "    adegan berisi puluhan ribu objek, misalnya simulasi kerumunan.",
                    "  - RealityKit: engine 3D Apple untuk AR dan visionOS juga berbasis",
                    "    ECS. Entity, Component, dan protokol System adalah bagian dari",
                    "    API-nya, ditulis dengan Swift.",
                    "  - Flecs (C dan C++) dan EnTT (C++): pustaka ECS yang bisa",
                    "    ditempel ke engine buatan sendiri.",
                    "  - Overwatch: tim Blizzard menjelaskan arsitektur ECS game ini di",
                    "    presentasi GDC 2017, dan rekamannya ada di kanal YouTube GDC.",
                    "",
                    "Godot sengaja nggak memakai ECS. Pendirinya, Juan Linietsky,",
                    "menulis artikel \"Why isn't Godot an ECS-based game engine?\"",
                    "(2021). Alasannya: pohon node lebih mudah dipahami, dan bagian",
                    "yang butuh kecepatan dioptimalkan di dalam engine.",
                    "",
                    "Kapan ECS nggak perlu? Untuk game kecil dengan puluhan objek, pola",
                    "GameObject atau node sudah cukup dan lebih mudah dibaca. ECS",
                    "menambah satu lapis cara berpikir: logika tersebar di banyak",
                    "sistem, dan kamu harus melihat komponen sebuah entitas untuk tahu",
                    "apa yang akan terjadi padanya. Manfaatnya terasa saat entitasnya",
                    "ribuan, atau saat kamu butuh simulasi yang bisa disimpan dan",
                    "diputar ulang seperti di materi berikutnya.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Game strategi dan simulasi dengan ribuan unit, misalnya city",
                    "builder atau tower defense, sering memakai pola ECS atau gaya",
                    "data-oriented lain. Contoh terbuka yang bisa kamu baca kodenya:",
                    "folder examples di repo Bevy dan repo EntityComponentSystemSamples",
                    "milik Unity di GitHub.",
                    "",
                    "Kasus kecil: game tower defense buatanmu mulai patah-patah saat",
                    "ada 3.000 musuh di layar. Tiap musuh adalah objek kelas Musuh",
                    "dengan method update() sendiri.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Ukur dulu dengan profiler browser atau engine. Pastikan waktu",
                    "     frame memang habis di update musuh, dan bukan di menggambar.",
                    "  2. Pisahkan data musuh jadi komponen: Posisi, Kecepatan, Nyawa,",
                    "     dan TargetJalur. Simpan tiap jenis di array sendiri, terurut",
                    "     menurut nomor entitas.",
                    "  3. Ganti method update() di tiap objek dengan beberapa sistem:",
                    "     sistem gerak, sistem ikut jalur, dan sistem kerusakan. Tiap",
                    "     sistem berupa satu loop di atas array.",
                    "  4. Ukur lagi. Kalau masih berat, sistem yang saling lepas bisa",
                    "     dipindah ke Web Worker atau thread lain, karena tiap sistem",
                    "     cuma menyentuh komponennya sendiri.",
                ],
            },
        ],
    },
    {
        "title": "26. Determinisme, Replay, dan Netcode Dasar",
        "sections": [
            {
                "body": [
                    "Sebuah simulasi disebut deterministik kalau keadaan awal yang sama",
                    "dan urutan input yang sama selalu menghasilkan keadaan akhir yang",
                    "sama. Selalu artinya setiap kali dijalankan, di komputer mana pun.",
                    "",
                    "Sifat ini membuka tiga hal:",
                    "  - Replay: cukup simpan input per tick, nggak perlu posisi semua",
                    "    benda tiap frame. Rekaman pertandingan jadi kecil, dan diputar",
                    "    ulang dengan menjalankan simulasinya lagi.",
                    "  - Pengujian: bug yang muncul di tick ke-5.000 bisa diulang persis",
                    "    dengan input yang sama.",
                    "  - Multiplayer: pemain cukup saling kirim input, karena tiap",
                    "    komputer menghitung hasil yang sama sendiri.",
                    "",
                    "Tick di sini artinya satu langkah simulasi dengan fixed timestep,",
                    "persis langkah fisika di materi Fixed Timestep dan Jam Palsu.",
                    "Simulasi yang langkahnya mengikuti delta time frame nggak bisa",
                    "deterministik, karena lama frame berbeda di tiap komputer.",
                ],
            },
            {
                "heading": "Replay dari rekaman input",
                "code": """// Simulasi kecil yang deterministik: keadaan awal + input per tick.
function simulasi(logInput) {
  let x = 0;
  let y = 0;
  let skor = 0;
  for (const input of logInput) {
    if (input === "kanan") x += 3;
    if (input === "kiri") x -= 3;
    if (input === "lompat") y += 5;
    y = Math.max(0, y - 1); // gravitasi
    if (x === 9 && y > 0) skor += 10; // ambil koin di x = 9 saat melayang
  }
  // checksum: ringkasan keadaan akhir dalam satu angka
  let h = 0;
  for (const v of [x, y, skor]) h = (h * 31 + v) % 1000003;
  return `x=${x} y=${y} skor=${skor} checksum=${h}`;
}

const rekaman = ["kanan", "kanan", "lompat", "kanan", "diam", "kiri"];
console.log("main  :", simulasi(rekaman));
console.log("replay:", simulasi(rekaman));
const beda = [...rekaman];
beda[2] = "diam"; // satu input saja diganti
console.log("ubah 1:", simulasi(beda));""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  main  : x=6 y=1 skor=20 checksum=5817",
                    "  replay: x=6 y=1 skor=20 checksum=5817",
                    "  ubah 1: x=6 y=0 skor=0 checksum=5766",
                    "",
                    "Main dan replay menghasilkan checksum yang sama. Checksum adalah",
                    "ringkasan keadaan dalam satu angka, dan dua keadaan yang berbeda",
                    "hampir pasti punya checksum berbeda. Mengganti satu input di tick",
                    "ketiga mengubah hasil akhir, dan checksum langsung menunjukkannya.",
                    "Posisi akhirnya kebetulan sama, tapi skornya beda.",
                ],
            },
            {
                "heading": "Musuh-musuh determinisme",
                "body": [
                    "  - Angka acak tanpa seed. Math.random() memberi urutan berbeda",
                    "    tiap kali. Pakai generator angka acak sendiri dengan seed yang",
                    "    ikut disimpan di rekaman.",
                    "  - Waktu sungguhan. Date.now() atau delta time frame di dalam",
                    "    logika permainan membuat hasilnya bergantung kecepatan komputer.",
                    "  - Urutan iterasi yang nggak dijamin. Map di Go dan set berbasis",
                    "    hash di banyak bahasa mengacak urutannya. Di JavaScript, Map",
                    "    menjaga urutan masuk, tapi kunci objek yang berupa angka",
                    "    diurutkan secara numerik. Cara amannya, urutkan dulu, misalnya",
                    "    menurut nomor entitas.",
                    "  - Angka pecahan (floating point). Operasi dasar seperti tambah dan",
                    "    kali sudah dibakukan standar IEEE 754, tapi hasilnya bergantung",
                    "    urutan operasi, dan compiler bisa menyusun ulang operasi itu.",
                    "    Spesifikasi JavaScript bahkan nggak mewajibkan Math.sin",
                    "    memberi angka yang persis sama di semua engine, cuma hasil",
                    "    yang mendekati.",
                    "  - Thread yang berlomba. Dua thread yang menulis data yang sama",
                    "    dengan urutan acak menghasilkan keadaan berbeda tiap kali.",
                ],
            },
            {
                "heading": "Urutan penjumlahan dan fixed point",
                "code": """const a = (0.1 + 0.2) + 0.3;
const b = 0.1 + (0.2 + 0.3);
console.log(a, b, a === b);

// Fixed point: simpan posisi dalam milipiksel (bilangan bulat)
const c = (100 + 200) + 300;
const d = 100 + (200 + 300);
console.log(c, d, c === d);""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  0.6000000000000001 0.6 false",
                    "  600 600 true",
                    "",
                    "Urutan penjumlahan mengubah hasil angka pecahan. Bilangan bulat",
                    "nggak punya masalah itu. Karena itu banyak game deterministik",
                    "menyimpan posisi sebagai bilangan bulat dalam satuan kecil, yang",
                    "disebut fixed point. Misalnya milipiksel: posisi 12,5 piksel",
                    "disimpan sebagai 12500. Gerakannya tetap halus, dan hasilnya sama",
                    "persis di semua mesin.",
                ],
            },
            {
                "heading": "Lockstep",
                "body": [
                    "Di model lockstep, semua pemain menjalankan simulasi yang sama.",
                    "Tiap tick, setiap komputer mengirim inputnya ke yang lain, dan",
                    "tick N baru dijalankan sesudah input semua pemain untuk tick N",
                    "tiba. Yang dikirim lewat jaringan cuma input, jadi ribuan unit pun",
                    "nggak menambah lalu lintas data.",
                    "",
                    "Game strategi real-time klasik memakai cara ini. Artikel \"1500",
                    "Archers on a 28.8\" (2001) menceritakan bagaimana Age of Empires",
                    "menjalankan ratusan unit lewat modem 28,8 kbps dengan lockstep.",
                    "Factorio juga memakai simulasi deterministik untuk multiplayer-nya,",
                    "dan developernya banyak menulis soal itu di blog Friday Facts.",
                    "",
                    "Kelemahannya: semua menunggu pemain yang paling lambat. Kalau ada",
                    "satu saja perbedaan hasil (desync), simulasi di komputer-komputer",
                    "itu mulai menyimpang dan nggak akan menyatu lagi. Karena itu",
                    "checksum keadaan biasanya ikut dikirim tiap beberapa tick untuk",
                    "mendeteksi desync secepatnya.",
                ],
            },
            {
                "heading": "Rollback",
                "body": [
                    "Game fighting nggak bisa menunggu, karena jeda sepersekian detik",
                    "terasa sekali saat menekan tombol pukul. Rollback netcode",
                    "menjalankan simulasi tanpa menunggu input lawan. Input lawan untuk",
                    "tick yang belum tiba ditebak, biasanya sama dengan input",
                    "terakhirnya. Begitu input asli datang dan ternyata berbeda, game",
                    "memuat keadaan yang disimpan di tick itu, lalu menjalankan ulang",
                    "simulasi sampai tick sekarang dengan input yang benar, semuanya",
                    "dalam satu frame.",
                    "",
                    "Syaratnya dua: simulasi harus deterministik, dan keadaan harus bisa",
                    "disimpan serta dimuat dengan cepat. GGPO, pustaka rollback yang",
                    "banyak dipakai game fighting, dibuka sebagai open source berlisensi",
                    "MIT pada 2019. Game fighting modern seperti Street Fighter 6 juga",
                    "memakai rollback.",
                ],
            },
            {
                "heading": "Server otoritatif",
                "body": [
                    "Game tembak-tembakan dan battle royale biasanya memakai model",
                    "lain. Server menjalankan simulasi yang dianggap benar, klien",
                    "mengirim input, dan server mengirim balik keadaan. Supaya kontrol",
                    "terasa responsif, klien menebak hasil inputnya sendiri",
                    "(client-side prediction), lalu mengoreksi diri saat keadaan dari",
                    "server tiba.",
                    "",
                    "Model ini nggak menuntut determinisme penuh, karena server",
                    "mengirim keadaan yang benar dan klien tinggal menyesuaikan. Server",
                    "juga bisa menolak gerakan yang mustahil, jadi lebih tahan curang.",
                    "",
                    "  Model               Yang dikirim       Deterministik?  Genre",
                    "  Lockstep            input              wajib           strategi",
                    "  Rollback            input              wajib           fighting",
                    "  Server otoritatif   input + keadaan    nggak wajib     tembak",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Fitur replay di banyak game strategi dan balap menyimpan input per",
                    "tick, bukan video. Rekamannya cuma beberapa kilobyte. Kelemahannya,",
                    "rekaman lama biasanya rusak saat game diperbarui: begitu aturan",
                    "permainan berubah sedikit, input yang sama menghasilkan",
                    "pertandingan yang berbeda. Makanya banyak game menandai rekaman",
                    "dengan nomor versi dan menolak memutar rekaman dari versi lain.",
                    "",
                    "Kasus kecil: pemain melapor replay pertandingannya kacau di",
                    "komputer temannya. Di awal sama, tapi beberapa menit kemudian",
                    "unit-unitnya ada di tempat berbeda.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Hitung checksum keadaan di tiap tick, dan simpan daftar",
                    "     checksum itu di berkas rekaman.",
                    "  2. Putar rekaman di kedua komputer dan bandingkan checksum per",
                    "     tick. Tick pertama yang berbeda adalah titik desync.",
                    "  3. Cetak seluruh keadaan di tick itu dari kedua komputer, lalu",
                    "     cari komponen pertama yang nilainya berbeda.",
                    "  4. Telusuri sistem yang mengubah komponen itu. Tersangka yang",
                    "     biasa: Math.random tanpa seed, iterasi tanpa urutan tetap, dan",
                    "     fungsi seperti Math.sin.",
                    "  5. Sesudah diperbaiki, jadikan rekaman itu tes otomatis yang",
                    "     diputar di dua mesin berbeda dan harus berakhir dengan",
                    "     checksum yang sama.",
                ],
            },
        ],
    },
    {
        "title": "27. Matematika AR: Raycast, Anchor, dan Matriks 4x4",
        "sections": [
            {
                "body": [
                    "Aplikasi AR (augmented reality) menempelkan benda virtual ke dunia",
                    "nyata yang terlihat lewat kamera. Contoh paling umum: kamu",
                    "mengetuk layar, lalu kursi virtual muncul di lantai kamarmu dan",
                    "tetap di sana walaupun ponselnya digerakkan.",
                    "",
                    "Di balik satu ketukan itu ada empat langkah:",
                    "  1. Pelacakan dunia. Ponsel terus menghitung posisi dan arah",
                    "     kameranya dengan menggabungkan gambar kamera dan sensor gerak.",
                    "  2. Deteksi bidang. Sistem AR mencari permukaan datar seperti",
                    "     lantai dan meja dari titik-titik ciri di gambar kamera.",
                    "  3. Raycast. Titik ketukan di layar diubah jadi sinar yang keluar",
                    "     dari kamera, lalu dicari di mana sinar itu menabrak bidang.",
                    "  4. Anchor. Titik tabrakan itu dijadikan jangkar, dan kursi",
                    "     ditempelkan ke jangkar tersebut.",
                    "",
                    "Langkah 1 dan 2 dikerjakan ARCore atau ARKit. Langkah 3 dan 4",
                    "matematikanya sederhana, dan itu yang kita bahas di sini.",
                ],
            },
            {
                "heading": "Dari ketukan ke sinar",
                "body": [
                    "Titik ketukan (px, py) dulu diubah ke NDC, rentang -1 sampai 1,",
                    "kebalikan dari viewport transform di materi pipeline grafis:",
                    "",
                    "  nx = 2 * px / lebar - 1        ny = 1 - 2 * py / tinggi",
                    "",
                    "Lalu NDC diubah jadi arah sinar di ruang kamera. Kamera menghadap",
                    "sumbu -z, dan sudut pandangnya (field of view) menentukan seberapa",
                    "lebar sinar menyebar:",
                    "",
                    "  arah = (nx * tan(fov/2) * aspek,  ny * tan(fov/2),  -1)",
                    "",
                    "Terakhir, arah itu diputar mengikuti orientasi kamera supaya jadi",
                    "arah di ruang dunia.",
                ],
            },
            {
                "heading": "Sinar memotong lantai",
                "body": [
                    "Sinar ditulis sebagai titik asal o ditambah s kali arah d:",
                    "",
                    "  p(s) = o + s * d",
                    "",
                    "Lantai adalah bidang y = h. Titik di sinar yang y-nya sama dengan h",
                    "didapat dari o.y + s * d.y = h, jadi s = (h - o.y) / d.y. Ada dua",
                    "kasus yang harus dicek:",
                    "  - d.y = 0: sinar sejajar lantai dan nggak akan pernah menyentuhnya.",
                    "  - s < 0: lantainya ada di belakang sinar. Ini terjadi kalau kamu",
                    "    mengetuk bagian atas layar saat kamera menghadap ke atas.",
                ],
            },
            {
                "heading": "Ketukan di layar sampai titik di lantai",
                "code": """const rad = (derajat) => (derajat * Math.PI) / 180;
const f2 = (n) => (Math.abs(n) < 0.005 ? 0 : n).toFixed(2); // hindari "-0.00"

// Kamera ponsel: 1,5 m di atas lantai, menunduk 30 derajat
const kamera = { x: 0, y: 1.5, z: 0 };
const menunduk = rad(-30);
const fov = rad(60); // sudut pandang vertikal
const lebar = 400;
const tinggi = 800;

// 1. Titik ketukan di layar -> NDC (-1..1)
const ketuk = { x: 200, y: 600 };
const nx = (2 * ketuk.x) / lebar - 1;
const ny = 1 - (2 * ketuk.y) / tinggi;

// 2. NDC -> arah sinar di ruang kamera (kamera menghadap -z)
const t = Math.tan(fov / 2);
const c = { x: nx * t * (lebar / tinggi), y: ny * t, z: -1 };

// 3. Putar arah itu mengikuti kemiringan kamera (rotasi sumbu x)
const d = {
  x: c.x,
  y: c.y * Math.cos(menunduk) - c.z * Math.sin(menunduk),
  z: c.y * Math.sin(menunduk) + c.z * Math.cos(menunduk),
};
console.log(`NDC: (${f2(nx)}, ${f2(ny)})`);
console.log(`arah sinar: (${f2(d.x)}, ${f2(d.y)}, ${f2(d.z)})`);

// 4. Potong dengan lantai y = 0: kamera.y + s * d.y = 0
const lantai = 0;
if (d.y === 0) {
  console.log("sinar sejajar lantai, tidak kena");
} else {
  const s = (lantai - kamera.y) / d.y;
  if (s < 0) {
    console.log("lantai ada di belakang sinar, tidak kena");
  } else {
    const kena = { x: kamera.x + s * d.x, y: kamera.y + s * d.y, z: kamera.z + s * d.z };
    console.log(`s = ${f2(s)}`);
    console.log(`titik di lantai: (${f2(kena.x)}, ${f2(kena.y)}, ${f2(kena.z)})`);
  }
}""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  NDC: (0.00, -0.50)",
                    "  arah sinar: (0.00, -0.75, -0.72)",
                    "  s = 2.00",
                    "  titik di lantai: (0.00, 0.00, -1.44)",
                    "",
                    "Ketukan di tengah-bawah layar menghasilkan titik di lantai 1,44",
                    "meter di depan kamera. Fungsi f2 menjaga angka seperti -0.001",
                    "supaya tercetak 0.00, karena toFixed menulis -0.00 untuk angka",
                    "negatif yang mendekati nol.",
                ],
            },
            {
                "heading": "Matriks 4x4 dan koordinat homogen",
                "body": [
                    "Posisi dan arah benda di AR disimpan sebagai pose: tempat plus",
                    "putaran. Cara paling umum menyimpannya adalah matriks 4x4. Tiga",
                    "kolom pertama adalah sumbu x, y, dan z lokal benda (putarannya),",
                    "dan kolom keempat adalah posisinya.",
                    "",
                    "Supaya satu matriks bisa memutar sekaligus menggeser, titik ditulis",
                    "dengan empat angka (x, y, z, w). Ini disebut koordinat homogen:",
                    "  - w = 1 untuk titik. Posisi di kolom keempat ikut ditambahkan.",
                    "  - w = 0 untuk arah. Arah cuma diputar, karena arah depan sebuah",
                    "    kursi nggak berubah walaupun kursinya dipindah.",
                    "",
                    "ARCore, ARKit, WebGL, dan WebXR sama-sama menyimpan matriks ini",
                    "sebagai 16 angka berurutan kolom demi kolom (column-major).",
                    "Putaran sering juga disimpan sebagai quaternion, empat angka yang",
                    "nggak kena masalah gimbal lock seperti sudut Euler, lalu diubah",
                    "ke matriks saat dibutuhkan.",
                ],
            },
            {
                "heading": "Menempelkan benda ke pose anchor",
                "code": """const f2 = (n) => (Math.abs(n) < 0.005 ? 0 : n).toFixed(2);

// Matriks 4x4 disimpan column-major (kolom demi kolom), seperti di
// WebGL, WebXR, ARCore, dan ARKit.
function poseAnchor(tx, ty, tz, yawDerajat) {
  const a = (yawDerajat * Math.PI) / 180;
  const c = Math.cos(a);
  const s = Math.sin(a);
  return [
    c, 0, -s, 0, // kolom 0: sumbu x lokal
    0, 1, 0, 0, // kolom 1: sumbu y lokal
    s, 0, c, 0, // kolom 2: sumbu z lokal
    tx, ty, tz, 1, // kolom 3: posisi
  ];
}

function kali(m, v) {
  const hasil = [0, 0, 0, 0];
  for (let baris = 0; baris < 4; baris++) {
    for (let kolom = 0; kolom < 4; kolom++) {
      hasil[baris] += m[kolom * 4 + baris] * v[kolom];
    }
  }
  return hasil;
}

const anchor = poseAnchor(0, 0, -1.44, 90); // di lantai, diputar 90 derajat
const ujungMeja = kali(anchor, [0.5, 0, 0, 1]); // titik: w = 1
const arahDepan = kali(anchor, [0, 0, -1, 0]); // arah: w = 0

console.log(`ujung meja di dunia: (${ujungMeja.slice(0, 3).map(f2).join(", ")})`);
console.log(`arah depan di dunia: (${arahDepan.slice(0, 3).map(f2).join(", ")})`);""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  ujung meja di dunia: (0.00, 0.00, -1.94)",
                    "  arah depan di dunia: (-1.00, 0.00, 0.00)",
                    "",
                    "Ujung meja yang 0,5 meter di sumbu x lokal ikut terputar 90",
                    "derajat dan tergeser ke posisi anchor. Arah depan juga terputar,",
                    "tapi posisinya nggak ikut ditambahkan karena w-nya 0.",
                ],
            },
            {
                "heading": "Anchor",
                "body": [
                    "Pemahaman sistem AR tentang ruangan terus diperbaiki selama kamu",
                    "bergerak. Kalau posisi kursi disimpan sebagai koordinat dunia",
                    "biasa, koreksi itu membuat kursi tampak bergeser atau melayang.",
                    "",
                    "Anchor adalah pose yang dijaga sistem AR: setiap kali peta ruangan",
                    "dikoreksi, pose anchor ikut diperbarui. Benda yang ditempel ke",
                    "anchor ikut bergerak bersamanya, jadi tetap menempel di tempat",
                    "yang sama di dunia nyata. Namanya beda-beda per platform, tapi",
                    "idenya sama: Anchor di ARCore, ARAnchor dan AnchorEntity di ARKit",
                    "dan RealityKit, serta XRAnchor di WebXR.",
                    "",
                    "Anchor juga bisa dibagikan. ARCore punya Cloud Anchors, sehingga",
                    "dua ponsel bisa melihat benda virtual yang sama di titik yang sama.",
                    "",
                    "Jebakan: tiap anchor memakan kerja pelacakan. Jangan membuat anchor",
                    "untuk setiap benda kecil. Satu anchor untuk satu meja, lalu benda",
                    "di atas meja ditempel relatif ke anchor itu.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aplikasi belanja furnitur yang punya tombol lihat di ruanganmu,",
                    "seperti IKEA Place, melakukan persis langkah tadi: deteksi lantai,",
                    "raycast dari ketukan, lalu anchor. Hitungan yang sama dipakai",
                    "aplikasi pengukur jarak di ponsel untuk mengukur panjang meja.",
                    "",
                    "Kasus kecil: kursi virtual di aplikasi AR buatanmu tampak melayang dan",
                    "bergeser beberapa senti setelah kamu berjalan mengelilingi kamar.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Cek bagaimana posisi kursi disimpan. Kalau disimpan sebagai",
                    "     koordinat dunia sekali saat diketuk, koreksi peta ruangan",
                    "     nggak ikut diterapkan ke kursi.",
                    "  2. Buat anchor dari hasil raycast (misalnya hit.createAnchor() di",
                    "     ARCore), lalu jadikan kursi anak dari anchor itu.",
                    "  3. Pastikan raycast-nya mengenai bidang yang sudah terdeteksi,",
                    "     bukan titik perkiraan, supaya tinggi lantainya benar.",
                    "  4. Uji lagi dengan berjalan memutar. Kursi boleh bergeser sedikit",
                    "     di detik-detik awal, lalu harus diam di tempatnya.",
                ],
            },
        ],
    },
    {
        "title": "28. ARCore, ARKit, dan RealityKit",
        "sections": [
            {
                "body": [
                    "Kamu nggak perlu menulis pelacakan dunia dan deteksi bidang",
                    "sendiri. Dua platform AR ponsel sudah menyediakannya: ARCore dari",
                    "Google untuk Android, dan ARKit dari Apple untuk iPhone dan iPad.",
                    "Keduanya menawarkan kemampuan yang mirip:",
                    "  - pelacakan gerak: posisi dan arah kamera di setiap frame,",
                    "  - deteksi bidang datar mendatar dan tegak,",
                    "  - hit test atau raycast dari titik di layar,",
                    "  - anchor,",
                    "  - perkiraan cahaya, supaya benda virtual diterangi seperti",
                    "    ruangan aslinya,",
                    "  - kedalaman, yaitu jarak tiap piksel kamera ke benda nyata.",
                    "",
                    "Nggak semua ponsel bisa. ARCore cuma jalan di ponsel yang ada di",
                    "daftar perangkat yang didukung Google, dan ARKit butuh iPhone atau",
                    "iPad yang cukup baru.",
                ],
            },
            {
                "heading": "ARCore",
                "body": [
                    "ARCore butuh aplikasi Google Play Services for AR di ponsel",
                    "pengguna. SDK-nya berlisensi Apache-2.0, dan saat materi ini",
                    "ditulis (Oktober 2026) versi terbarunya ARCore SDK for Android",
                    "1.57.0, dirilis 16 Oktober 2026. Kode Android-nya ditulis dengan",
                    "Kotlin atau Java, dan ada juga versi C untuk NDK.",
                    "",
                    "Fitur khasnya:",
                    "  - Depth API: peta kedalaman dari satu kamera biasa, jadi benda",
                    "    virtual bisa tertutup sofa sungguhan.",
                    "  - Geospatial API: menaruh benda di koordinat bumi dengan",
                    "    mencocokkan gambar kamera dengan data Street View.",
                    "  - Cloud Anchors: anchor yang dibagikan ke beberapa perangkat,",
                    "    termasuk iPhone.",
                    "",
                    "Sceneform, pustaka 3D yang dulu dipakai banyak tutorial ARCore,",
                    "sudah diarsipkan Google pada 2020. Kalau ketemu tutorial yang",
                    "memakainya, anggap kodenya sudah usang.",
                ],
            },
            {
                "heading": "Hit test dan anchor di ARCore (Kotlin)",
                "bahasa": "kotlin",
                "code": """import com.google.ar.core.Anchor
import com.google.ar.core.Frame
import com.google.ar.core.Plane

fun letakkan(frame: Frame, x: Float, y: Float): Anchor? {
    for (hit in frame.hitTest(x, y)) {
        val bidang = hit.trackable
        if (bidang is Plane &&
            bidang.type == Plane.Type.HORIZONTAL_UPWARD_FACING &&
            bidang.isPoseInPolygon(hit.hitPose)
        ) {
            return hit.createAnchor() // kursi ditempel ke anchor ini
        }
    }
    return null
}""",
            },
            {
                "heading": "ARKit dan RealityKit",
                "body": [
                    "ARKit mengurus pemahaman dunia: pelacakan, bidang, wajah lewat",
                    "kamera TrueDepth, dan rekonstruksi ruangan dengan sensor LiDAR di",
                    "iPhone dan iPad seri Pro. RoomPlan, yang dibangun di atas ARKit,",
                    "bisa memindai denah ruangan jadi model 3D.",
                    "",
                    "RealityKit mengurus sisi gambarnya: menggambar benda 3D,",
                    "pencahayaan, fisika, dan animasi, dengan arsitektur ECS seperti di",
                    "bab sebelumnya. Di SwiftUI, keduanya bertemu di RealityView. Versi",
                    "ARKit dan RealityKit mengikuti SDK iOS. Saat materi ini ditulis",
                    "versinya ikut SDK iOS 27 (Xcode 27.1).",
                    "",
                    "Jebakan: aplikasi iOS cuma bisa dibangun dengan Xcode di Mac. Dari",
                    "Fedora, jalur yang realistis adalah engine lintas platform seperti",
                    "Unity yang build iOS-nya dijalankan di Mac atau layanan build cloud.",
                ],
            },
            {
                "heading": "Kotak di lantai dengan RealityView (Swift)",
                "bahasa": "swift",
                "code": """import SwiftUI
import RealityKit

struct KursiAR: View {
    var body: some View {
        RealityView { content in
            content.camera = .spatialTracking
            let lantai = AnchorEntity(.plane(.horizontal,
                                             classification: .floor,
                                             minimumBounds: [0.5, 0.5]))
            let kotak = ModelEntity(mesh: .generateBox(size: 0.3),
                                    materials: [SimpleMaterial(color: .orange,
                                                               isMetallic: false)])
            lantai.addChild(kotak)
            content.add(lantai)
        }
    }
}""",
            },
            {
                "body": [
                    "AnchorEntity dengan target .plane meminta RealityKit mencari",
                    "lantai minimal 50 x 50 cm, lalu menaruh kotak 30 cm di sana begitu",
                    "lantainya ketemu. Raycast dan anchor tetap terjadi, cuma",
                    "dikerjakan RealityKit untukmu.",
                ],
            },
            {
                "heading": "Satu kode untuk dua platform: AR Foundation",
                "body": [
                    "Unity punya AR Foundation, lapisan yang membungkus ARCore dan",
                    "ARKit dengan satu API C#. Kamu menulis kode sekali, lalu memasang",
                    "plugin ARCore untuk build Android dan plugin ARKit untuk build",
                    "iOS. AR Foundation juga mendukung headset lewat OpenXR. Pokemon GO,",
                    "game Unity yang mode AR+-nya memakai ARCore dan ARKit, adalah",
                    "contoh game yang menjangkau dua platform sekaligus.",
                ],
            },
            {
                "heading": "Raycast di AR Foundation (C#)",
                "bahasa": "csharp",
                "code": """using System.Collections.Generic;
using UnityEngine;
using UnityEngine.InputSystem;
using UnityEngine.XR.ARFoundation;
using UnityEngine.XR.ARSubsystems;

public class LetakkanKursi : MonoBehaviour
{
    [SerializeField] ARRaycastManager raycast;
    [SerializeField] GameObject prefabKursi;
    static readonly List<ARRaycastHit> hasil = new List<ARRaycastHit>();

    void Update()
    {
        var layar = Touchscreen.current;
        if (layar == null || !layar.primaryTouch.press.wasPressedThisFrame) return;

        Vector2 posisi = layar.primaryTouch.position.ReadValue();
        if (raycast.Raycast(posisi, hasil, TrackableType.PlaneWithinPolygon))
        {
            Pose pose = hasil[0].pose; // tabrakan terdekat
            Instantiate(prefabKursi, pose.position, pose.rotation);
        }
    }
}""",
            },
            {
                "body": [
                    "Contoh ini menaruh kursi langsung di pose tabrakan. Untuk aplikasi",
                    "sungguhan, tempelkan kursi ke anchor lewat ARAnchorManager supaya",
                    "ia ikut dikoreksi seperti dibahas di materi sebelumnya.",
                    "",
                    "  Hal            ARCore                    ARKit",
                    "  Platform       Android (sebagian iOS)    iPhone, iPad",
                    "  Bahasa         Kotlin, Java, C, Unity    Swift, Unity",
                    "  Penggambar     pilih sendiri             RealityKit",
                    "  Fitur khas     Geospatial, Depth API     LiDAR, RoomPlan, wajah",
                    "  Bisa dari      Fedora (Android Studio)   Mac (Xcode) saja",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Fitur coba di ruangan pada aplikasi toko furnitur, filter wajah di",
                    "aplikasi kamera, dan mode AR di game seperti Pokemon GO semuanya",
                    "memakai ARCore dan ARKit. Ada yang langsung, ada yang lewat",
                    "engine.",
                    "",
                    "Kasus kecil: toko mebel lokal ingin fitur lihat sofa di ruanganmu",
                    "untuk Android dan iPhone. Programmernya cuma satu orang dan memakai",
                    "Fedora.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pilih Unity dengan AR Foundation, supaya satu kode C# melayani",
                    "     ARCore dan ARKit sekaligus.",
                    "  2. Bangun dan uji versi Android dulu di Fedora dengan ponsel yang",
                    "     ada di daftar perangkat ARCore.",
                    "  3. Pakai raycast ke PlaneWithinPolygon lalu tempelkan sofa ke",
                    "     anchor, persis langkah di materi matematika AR.",
                    "  4. Untuk build iOS, sewa Mac atau pakai layanan build cloud yang",
                    "     menjalankan Xcode, lalu uji di iPhone sungguhan sebelum rilis.",
                ],
            },
        ],
    },
    {
        "title": "29. OpenXR, Meta Quest, dan Android XR",
        "sections": [
            {
                "body": [
                    "Headset VR (virtual reality) menutup pandangan dengan dua layar,",
                    "satu untuk tiap mata, dan melacak gerak kepala di enam arah: maju",
                    "mundur, kiri kanan, naik turun, plus tiga putaran. Gambarnya harus",
                    "diperbarui 72 sampai 120 kali per detik dengan jeda sekecil",
                    "mungkin, karena gambar yang terlambat mengikuti kepala membuat",
                    "pemakainya pusing. Headset mixed reality menambahkan passthrough:",
                    "kamera headset menampilkan ruangan asli, lalu benda virtual",
                    "digambar di atasnya.",
                    "",
                    "Dulu tiap pembuat headset punya SDK sendiri, dan aplikasi untuk satu",
                    "headset harus ditulis ulang untuk headset lain. OpenXR dibuat untuk",
                    "menghentikan itu. Ia standar terbuka bebas royalti dari Khronos:",
                    "aplikasi ditulis sekali ke API OpenXR, dan tiap pembuat headset",
                    "menyediakan runtime yang menjalankannya.",
                    "",
                    "OpenXR 1.0 rilis 2019, dan versi 1.1 keluar April 2024. Saat",
                    "materi ini ditulis (Oktober 2026), SDK-nya versi 1.1.65 dengan",
                    "lisensi Apache-2.0. Meta Quest, SteamVR, Android XR, dan Pico",
                    "memakainya. Apple nggak ikut: Vision Pro punya API sendiri.",
                ],
            },
            {
                "heading": "Cara kerja aplikasi OpenXR",
                "body": [
                    "Urutan objek yang dibuat aplikasi OpenXR:",
                    "  1. Instance: sambungan ke runtime OpenXR di perangkat.",
                    "  2. System: headset yang dipakai, beserta kemampuannya.",
                    "  3. Session: satu sesi XR yang aktif, terhubung ke API grafis",
                    "     seperti Vulkan atau OpenGL ES.",
                    "  4. Reference space: titik nol dunia, misalnya lantai tempat",
                    "     pengguna berdiri.",
                    "  5. Swapchain: gambar-gambar tempat aplikasi menggambar tiap mata.",
                    "  6. Action: input yang abstrak seperti ambil atau teleport.",
                    "     Runtime memetakannya ke tombol controller apa pun yang",
                    "     dipakai, jadi aplikasi nggak perlu tahu merek controller-nya.",
                    "",
                    "Sesi punya status yang dikirim runtime lewat event, dari",
                    "XR_SESSION_STATE_IDLE sampai XR_SESSION_STATE_STOPPING. Urutannya",
                    "ada di gambar di bawah. Aplikasi memanggil xrBeginSession saat",
                    "statusnya ready, menggambar selama frame loop berjalan, dan cuma",
                    "membaca input saat statusnya focused. Kalau pengguna membuka menu",
                    "sistem, status turun ke visible: gambarmu masih tampil, tapi input",
                    "sedang dipakai menu.",
                ],
            },
            {
                "heading": "Frame loop OpenXR (C)",
                "bahasa": "c",
                "code": """while (aplikasiJalan) {
    bacaEvent(); // perubahan status sesi datang lewat xrPollEvent
    if (!sesiBerjalan) continue;

    XrFrameState frame = {.type = XR_TYPE_FRAME_STATE};
    xrWaitFrame(sesi, NULL, &frame); // tunggu jadwal dari runtime
    xrBeginFrame(sesi, NULL);

    uint32_t jumlahLapisan = 0;
    const XrCompositionLayerBaseHeader *lapisan[1];
    if (frame.shouldRender) {
        // xrLocateViews memberi pose dua mata pada waktu tampil yang
        // diperkirakan, lalu tiap mata digambar ke swapchain-nya.
        lapisan[jumlahLapisan++] = gambarDuaMata(frame.predictedDisplayTime);
    }

    XrFrameEndInfo selesai = {
        .type = XR_TYPE_FRAME_END_INFO,
        .displayTime = frame.predictedDisplayTime,
        .environmentBlendMode = XR_ENVIRONMENT_BLEND_MODE_OPAQUE,
        .layerCount = jumlahLapisan,
        .layers = lapisan,
    };
    xrEndFrame(sesi, &selesai);
}""",
            },
            {
                "body": [
                    "Perhatikan predictedDisplayTime. Runtime memperkirakan kapan frame",
                    "ini akhirnya tampil di layar headset, dan pose kepala dihitung",
                    "untuk waktu itu, bukan untuk saat ini. Prediksi ini yang membuat",
                    "gambar terasa menempel ke kepala.",
                    "",
                    "Hampir nggak ada yang menulis kode OpenXR mentah seperti ini untuk",
                    "game. Unity, Unreal, dan Godot sudah punya dukungan OpenXR, jadi",
                    "kamu cukup memilih OpenXR di pengaturan proyek.",
                ],
            },
            {
                "heading": "Meta Quest dan Horizon OS",
                "body": [
                    "Meta Quest 3 (2023) dan Quest 3S (2024) adalah headset mandiri:",
                    "prosesor, baterai, dan layar ada di headset, tanpa kabel ke PC.",
                    "Sistem operasinya Meta Horizon OS yang berbasis Android, dan",
                    "aplikasinya dijual di Meta Horizon Store.",
                    "",
                    "Meta XR SDK adalah kumpulan pustaka Meta untuk Unity dan Unreal",
                    "yang berjalan di atas OpenXR. Isinya fitur khas Quest seperti",
                    "passthrough, pelacakan tangan, dan pemahaman ruangan. Saat materi",
                    "ini ditulis, versi Meta XR Core SDK adalah 207.0 (22 September",
                    "2026). Lisensinya proprietary, jadi baca syaratnya sebelum",
                    "mendistribusikan aplikasi. Godot mendukung Quest lewat OpenXR",
                    "ditambah plugin OpenXR Vendors.",
                ],
            },
            {
                "heading": "Android XR",
                "body": [
                    "Android XR adalah platform XR dari Google untuk headset dan",
                    "kacamata pintar. Perangkat pertamanya Samsung Galaxy XR, headset",
                    "yang dirilis Oktober 2025 di Amerika Serikat dan Korea Selatan.",
                    "",
                    "Ada beberapa jalan membuat aplikasinya:",
                    "  - Jetpack XR SDK: Jetpack Compose for XR, SceneCore, dan ARCore",
                    "    for Jetpack XR, untuk developer Android yang sudah biasa",
                    "    dengan Kotlin. Saat materi ini ditulis statusnya Developer",
                    "    Preview 4, jadi API-nya masih bisa berubah.",
                    "  - Unity atau OpenXR, untuk game dan aplikasi 3D.",
                    "  - Godot, lewat plugin OpenXR Vendors.",
                    "  - WebXR, untuk pengalaman XR langsung dari browser.",
                    "",
                    "Kebanyakan aplikasi Android biasa jalan di Android XR tanpa diubah,",
                    "tampil sebagai panel 2D yang melayang di ruangan.",
                ],
            },
            {
                "heading": "Peta platform headset",
                "bahasa": "teks",
                "code": """Platform      Contoh perangkat    Cara membuat aplikasi        Status
Meta Quest    Quest 3, Quest 3S   Unity/Unreal + Meta XR SDK,  stabil
                                  Godot, OpenXR, WebXR
Android XR    Samsung Galaxy XR   Jetpack XR SDK, Unity,       SDK masih
                                  OpenXR, Godot, WebXR         preview
SteamVR       headset PC          OpenXR, Unity, Unreal        stabil
visionOS      Apple Vision Pro    SwiftUI + RealityKit         stabil
                                  (tanpa OpenXR)""",
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Game VR, aplikasi olahraga, dan pelatihan kerja seperti simulasi",
                    "perawatan mesin banyak dibuat untuk Quest dengan Unity atau",
                    "Unreal. Karena engine-nya memakai OpenXR, aplikasi yang sama bisa",
                    "dibawa ke headset lain dengan perubahan kecil.",
                    "",
                    "Kasus kecil: kamu membuat game VR kecil di Godot untuk Quest 3, lalu",
                    "ingin game itu juga jalan di Samsung Galaxy XR.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pastikan proyek memakai OpenXR, bukan pustaka khusus satu",
                    "     vendor, dan pasang plugin OpenXR Vendors di Godot.",
                    "  2. Tulis input sebagai action (ambil, lempar, teleport), bukan",
                    "     nama tombol controller Quest, supaya runtime lain bisa",
                    "     memetakannya ke controller atau gerakan tangannya sendiri.",
                    "  3. Kumpulkan fitur yang cuma ada di satu platform, misalnya",
                    "     pemahaman ruangan Meta, di satu modul yang bisa dimatikan.",
                    "  4. Ekspor dua build Android dengan preset berbeda, lalu uji di",
                    "     kedua headset. Perhatikan status sesi: game harus berhenti",
                    "     membaca input saat menu sistem dibuka.",
                ],
            },
        ],
    },
    {
        "title": "30. visionOS dan WebXR",
        "sections": [
            {
                "body": [
                    "visionOS adalah sistem operasi Apple Vision Pro, headset yang mulai",
                    "dijual di Amerika Serikat pada Februari 2024. Apple menyebut",
                    "jenis komputasi ini spatial computing. Aplikasinya dibangun dengan",
                    "SwiftUI, RealityKit, dan ARKit di Xcode, dan visionOS nggak memakai",
                    "OpenXR. Saat materi ini ditulis (Oktober 2026), versi terbarunya",
                    "visionOS 27.0.1. Nomor versinya melompat dari 2 ke 26 pada 2025,",
                    "waktu Apple menyamakan nomor versi semua sistem operasinya dengan",
                    "tahun.",
                    "",
                    "Developer Unity bisa menargetkan visionOS lewat PolySpatial. Tapi",
                    "jalur mana pun tetap butuh Mac, dan perangkatnya mahal. Untuk",
                    "pelajar, yang paling berguna adalah mengenal konsepnya, karena",
                    "konsep itu juga dipakai platform lain.",
                ],
            },
            {
                "heading": "Window, volume, dan immersive space",
                "body": [
                    "Aplikasi visionOS disusun dari tiga jenis ruang:",
                    "  - Window: jendela datar seperti aplikasi biasa, melayang di",
                    "    ruangan. Pengguna bisa memindah dan mengubah ukurannya.",
                    "  - Volume: kotak tiga dimensi berisi model 3D yang bisa dilihat",
                    "    dari berbagai sisi, berdampingan dengan aplikasi lain.",
                    "  - Immersive space: ruang yang mengambil alih sekitar pengguna.",
                    "    Gayanya ada tiga: mixed (benda virtual di ruangan asli),",
                    "    progressive (sebagian pandangan diganti dunia virtual), dan",
                    "    full (pandangan sepenuhnya virtual).",
                    "",
                    "Satu aplikasi bisa membuka ketiganya. Biasanya ia mulai dari window,",
                    "lalu membuka immersive space saat pengguna menekan tombol.",
                ],
            },
            {
                "heading": "Tiga jenis ruang dalam satu aplikasi (Swift)",
                "bahasa": "swift",
                "code": "import SwiftUI\nimport RealityKit\n\n@main\nstruct GaleriApp: App {\n    var body: some Scene {\n        WindowGroup {\n            MenuUtama()\n        }\n\n        WindowGroup(id: \"bola\") {\n            Model3D(named: \"Bola\")\n        }\n        .windowStyle(.volumetric)\n\n        ImmersiveSpace(id: \"ruang\") {\n            RealityView { content in\n                let bola = ModelEntity(mesh: .generateSphere(radius: 0.2))\n                bola.position = [0, 1.5, -1] // 1,5 m di atas lantai, 1 m di depan\n                content.add(bola)\n            }\n        }\n    }\n}\n\nstruct MenuUtama: View {\n    @Environment(\\.openImmersiveSpace) private var bukaRuang\n\n    var body: some View {\n        Button(\"Masuk ruang\") {\n            Task { await bukaRuang(id: \"ruang\") }\n        }\n    }\n}",
            },
            {
                "body": [
                    "Satu immersive space saja yang boleh terbuka di satu waktu, jadi",
                    "aplikasi harus menutup yang lama sebelum membuka yang baru.",
                    "Inputnya juga khas: pengguna melihat ke sebuah tombol lalu",
                    "mencubitkan jari, dan sistem cuma memberi tahu aplikasi tombol",
                    "mana yang dipilih. Ke mana mata melihat sebelum mencubit nggak",
                    "dibagikan ke aplikasi, demi privasi.",
                ],
            },
            {
                "heading": "WebXR",
                "body": [
                    "WebXR Device API adalah API browser untuk VR dan AR langsung dari",
                    "halaman web, tanpa toko aplikasi. Spesifikasinya berstatus W3C",
                    "Candidate Recommendation Draft, revisi 9 Juni 2026. Halaman",
                    "meminta sesi dengan salah satu mode:",
                    "  - immersive-vr: pandangan penuh di headset.",
                    "  - immersive-ar: benda virtual di atas dunia nyata, misalnya di",
                    "    Chrome Android yang memakai ARCore.",
                    "  - inline: tampil biasa di dalam halaman.",
                    "",
                    "Syaratnya: halaman dibuka lewat HTTPS, sesi imersif dimulai dari",
                    "tindakan pengguna seperti klik tombol, dan gambarnya dibuat dengan",
                    "WebGL. Dukungan saat materi ini ditulis: browser di Meta Quest dan",
                    "Android XR, Chrome di Android, dan Samsung Internet. Safari di",
                    "visionOS menambahkan sesi immersive-vr sejak visionOS 2 (2024).",
                    "Safari di iPhone belum mendukung WebXR, dan Firefox desktop nggak",
                    "menyalakannya secara bawaan.",
                    "",
                    "Pustaka Three.js, Babylon.js, dan A-Frame sudah membungkus WebXR,",
                    "jadi kamu jarang menulis kode di bawah ini sendiri.",
                ],
            },
            {
                "heading": "Memulai sesi immersive-vr",
                "bahasa": "browser",
                "code": """const tombol = document.querySelector("#masuk-vr");
tombol.hidden = !(navigator.xr && (await navigator.xr.isSessionSupported("immersive-vr")));

tombol.addEventListener("click", async () => {
  const sesi = await navigator.xr.requestSession("immersive-vr", {
    requiredFeatures: ["local-floor"],
  });
  const kanvas = document.createElement("canvas");
  const gl = kanvas.getContext("webgl2", { xrCompatible: true });
  sesi.updateRenderState({ baseLayer: new XRWebGLLayer(sesi, gl) });
  const lantai = await sesi.requestReferenceSpace("local-floor");

  function frame(waktu, xrFrame) {
    sesi.requestAnimationFrame(frame);
    const pose = xrFrame.getViewerPose(lantai);
    if (!pose) return;
    const layer = sesi.renderState.baseLayer;
    gl.bindFramebuffer(gl.FRAMEBUFFER, layer.framebuffer);
    for (const view of pose.views) {
      const vp = layer.getViewport(view);
      gl.viewport(vp.x, vp.y, vp.width, vp.height);
      // gambar adegan dengan view.projectionMatrix dan
      // view.transform.inverse.matrix (16 angka column-major)
    }
  }
  sesi.requestAnimationFrame(frame);
});""",
            },
            {
                "body": [
                    "Polanya mirip OpenXR: minta sesi, pilih reference space",
                    "(local-floor berarti titik nol di lantai), lalu frame loop yang",
                    "menggambar sekali untuk tiap view, yaitu tiap mata. Loop-nya",
                    "memakai sesi.requestAnimationFrame, bukan milik window, karena",
                    "headset punya jadwal refresh sendiri. Skripnya memakai await di",
                    "tingkat atas, jadi taruh di <script type=\"module\">.",
                    "",
                    "  Hal           visionOS                    WebXR",
                    "  Bahasa        Swift                       JavaScript",
                    "  Distribusi    App Store                   tautan web",
                    "  Alat          Xcode di Mac                editor apa pun",
                    "  Perangkat     Apple Vision Pro            Quest, Android, dll.",
                    "  Kelebihan     integrasi sistem penuh      tanpa instal",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Toko online yang menampilkan produk dalam AR langsung dari halaman",
                    "produk, tur virtual museum, dan demo VR untuk pameran sering",
                    "dibuat dengan WebXR, karena pengunjung cukup membuka tautan. Untuk",
                    "pengalaman yang butuh fitur sistem penuh di Vision Pro, developer",
                    "tetap membuat aplikasi visionOS asli.",
                    "",
                    "Kasus kecil: museum di kotamu ingin tur VR yang bisa dibuka",
                    "pengunjung di Quest milik mereka dan di Vision Pro milik museum,",
                    "tanpa lewat toko aplikasi.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pilih WebXR dengan pustaka seperti Three.js atau A-Frame, lalu",
                    "     sajikan halamannya lewat HTTPS.",
                    "  2. Pakai mode immersive-vr, yang didukung browser Quest dan",
                    "     Safari di visionOS.",
                    "  3. Cek dukungan dengan isSessionSupported. Kalau nggak didukung,",
                    "     misalnya di iPhone, tampilkan versi inline yang bisa diputar",
                    "     dengan jari.",
                    "  4. Untuk input, layani sentuhan pilih (event select) yang",
                    "     dikirim baik oleh controller Quest maupun cubitan jari di",
                    "     Vision Pro.",
                    "  5. Uji di kedua perangkat, karena kecepatan dan bentuk inputnya",
                    "     berbeda.",
                ],
            },
        ],
    },
]
