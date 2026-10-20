"""Kurikulum Mobile & Desktop.

Dirakit alat/rakit_kurikulum.py dari draf per bab (2026-10-19).
Sesudah dirakit, berkas ini disunting seperti kurikulum lain
(alat/ganti_badan.py, alat/tambah_bagian.py). <KEY>_BAB tetap
spesifikasi JUMLAH; rentangnya dihitung data/kurikulum_tech.py.
"""

MOBILE_EXERCISES = [
    {
        "title": "Latihan 1: Tabel Keputusan Platform",
        "difficulty": "Mudah",
        "question": [
            "Bikin program yang membaca pilihan pelajar lalu mencetak jalur",
            "belajar yang disarankan, memakai tabel keputusan di materi Jalur",
            "Belajar dari Fedora Tanpa Mac.",
            "",
            "Masukan berisi tiga baris kunci=nilai, urutannya boleh acak:",
            "  target=android, ios, keduanya, atau desktop",
            "  mac=ya atau tidak",
            "  bahasa=kotlin, javascript, atau dart",
            "",
            "Aturan jalur (ios dan keduanya dianggap satu kelompok):",
            "  android  + kotlin      -> Kotlin + Jetpack Compose",
            "  android  + javascript  -> React Native + Expo",
            "  android  + dart        -> Flutter",
            "  ios      + javascript  -> React Native + Expo",
            "  ios      + dart        -> Flutter",
            "  ios      + kotlin      -> Kotlin Multiplatform",
            "  desktop  + javascript  -> Electron",
            "  desktop  + kotlin      -> Compose Multiplatform",
            "  desktop  + dart        -> Flutter",
            "",
            "Aturan build iOS, diperiksa dari atas:",
            "  1. target android atau desktop -> tidak perlu",
            "  2. mac=ya -> Xcode di Mac sendiri",
            "  3. jalurnya React Native + Expo -> EAS Build",
            "  4. selain itu -> Codemagic",
            "",
            "Cetak dua baris: jalur: ... lalu build iOS: ...",
            "",
            "Untuk input target=keduanya, keluarannya:",
            "jalur: React Native + Expo",
            "build iOS: EAS Build",
            "",
            "Untuk input target=android, keluarannya:",
            "jalur: Kotlin + Jetpack Compose",
            "build iOS: tidak perlu",
            "",
            "Untuk input target=ios, keluarannya:",
            "jalur: Flutter",
            "build iOS: Codemagic",
        ],
        "hints": [
            "Ubah dulu tiap baris kunci=nilai jadi satu objek, supaya urutan barisnya nggak penting.",
            "Gabungkan target ios dan keduanya jadi satu kelompok, lalu cari jalurnya di objek tabel yang kuncinya gabungan kelompok dan bahasa.",
            "Kolom build iOS diputuskan dengan if berurutan: kelompok bukan ios, lalu mac=ya, lalu jalur Expo, dan sisanya Codemagic.",
        ],
        "solution": "const teks = require('fs').readFileSync(0, 'utf8');\nconst data = {};\nfor (const baris of teks.split('\\n')) {\n  if (!baris.includes('=')) continue;\n  const [kunci, nilai] = baris.trim().split('=');\n  data[kunci] = nilai;\n}\n\nconst kelompok = data.target === 'keduanya' ? 'ios' : data.target;\nconst tabel = {\n  'android|kotlin': 'Kotlin + Jetpack Compose',\n  'android|javascript': 'React Native + Expo',\n  'android|dart': 'Flutter',\n  'ios|javascript': 'React Native + Expo',\n  'ios|dart': 'Flutter',\n  'ios|kotlin': 'Kotlin Multiplatform',\n  'desktop|javascript': 'Electron',\n  'desktop|kotlin': 'Compose Multiplatform',\n  'desktop|dart': 'Flutter',\n};\nconst jalur = tabel[kelompok + '|' + data.bahasa];\n\nlet buildIos;\nif (kelompok !== 'ios') buildIos = 'tidak perlu';\nelse if (data.mac === 'ya') buildIos = 'Xcode di Mac sendiri';\nelse if (jalur === 'React Native + Expo') buildIos = 'EAS Build';\nelse buildIos = 'Codemagic';\n\nconsole.log('jalur: ' + jalur);\nconsole.log('build iOS: ' + buildIos);",
        "stdin_list": [
            """target=keduanya
mac=tidak
bahasa=javascript
""",
            """target=android
mac=tidak
bahasa=kotlin
""",
            """target=ios
mac=tidak
bahasa=dart
""",
        ],
    },
    {
        "title": "Latihan 2: Simulator Siklus Hidup Activity",
        "difficulty": "Mudah",
        "question": [
            "Tiru siklus hidup satu Activity sebagai state machine. Keadaannya",
            "ada tiga: mati, aktif, dan latar. Mula-mula keadaannya mati.",
            "",
            "Masukan berisi satu event per baris. Aturannya:",
            "  keadaan  event           keadaan baru  callback",
            "  mati     buka            aktif         onCreate onStart onResume",
            "  aktif    home            latar         onPause onStop",
            "  aktif    putar           aktif         onPause onStop onDestroy",
            "                                         onCreate onStart onResume",
            "  aktif    tutup           mati          onPause onStop onDestroy",
            "  latar    kembali_ke_app  aktif         onRestart onStart onResume",
            "  latar    tutup           mati          onDestroy",
            "",
            "Untuk tiap event, cetak nama event, titik dua, lalu callback-nya",
            "dipisah spasi. Event yang nggak ada di tabel untuk keadaan saat itu",
            "dicetak sebagai: event: diabaikan (keadaan X).",
            "",
            "Di akhir, cetak keadaan terakhir dan berapa objek Activity yang",
            "dibuat (sama dengan berapa kali onCreate terpanggil).",
            "",
            "Contoh masukan pertama:",
            "  buka",
            "  home",
            "  kembali_ke_app",
            "  putar",
            "  tutup",
            "",
            "Untuk input buka, keluarannya:",
            "buka: onCreate onStart onResume",
            "home: onPause onStop",
            "kembali_ke_app: onRestart onStart onResume",
            "putar: onPause onStop onDestroy onCreate onStart onResume",
            "tutup: onPause onStop onDestroy",
            "keadaan akhir: mati",
            "objek Activity dibuat: 2",
            "",
            "Contoh masukan kedua: home, buka, putar, putar, home, tutup.",
            "",
            "Untuk input home, keluarannya:",
            "home: diabaikan (keadaan mati)",
            "buka: onCreate onStart onResume",
            "putar: onPause onStop onDestroy onCreate onStart onResume",
            "putar: onPause onStop onDestroy onCreate onStart onResume",
            "home: onPause onStop",
            "tutup: onDestroy",
            "keadaan akhir: mati",
            "objek Activity dibuat: 3",
        ],
        "hints": [
            "Simpan tabel aturan sebagai objek bersarang: kunci pertama keadaan, kunci kedua event.",
            "Tiap isi tabel cukup berupa pasangan keadaan baru dan daftar callback, lalu cari pasangan itu untuk setiap baris masukan.",
            "Hitung objek dengan menambah satu setiap kali daftar callback yang dijalankan memuat onCreate.",
        ],
        "solution": "const kejadian = require('fs').readFileSync(0, 'utf8')\n  .split('\\n').map((b) => b.trim()).filter((b) => b !== '');\n\n// keadaan -> event -> [keadaan baru, callback yang dipanggil]\nconst aturan = {\n  mati: {\n    buka: ['aktif', ['onCreate', 'onStart', 'onResume']],\n  },\n  aktif: {\n    home: ['latar', ['onPause', 'onStop']],\n    putar: ['aktif', ['onPause', 'onStop', 'onDestroy', 'onCreate', 'onStart', 'onResume']],\n    tutup: ['mati', ['onPause', 'onStop', 'onDestroy']],\n  },\n  latar: {\n    kembali_ke_app: ['aktif', ['onRestart', 'onStart', 'onResume']],\n    tutup: ['mati', ['onDestroy']],\n  },\n};\n\nlet keadaan = 'mati';\nlet objekDibuat = 0;\nfor (const ev of kejadian) {\n  const langkah = aturan[keadaan][ev];\n  if (!langkah) {\n    console.log(`${ev}: diabaikan (keadaan ${keadaan})`);\n    continue;\n  }\n  const [baru, panggilan] = langkah;\n  if (panggilan.includes('onCreate')) objekDibuat += 1;\n  console.log(`${ev}: ${panggilan.join(' ')}`);\n  keadaan = baru;\n}\nconsole.log(`keadaan akhir: ${keadaan}`);\nconsole.log(`objek Activity dibuat: ${objekDibuat}`);",
        "stdin_list": [
            """buka
home
kembali_ke_app
putar
tutup
""",
            """home
buka
putar
putar
home
tutup
""",
        ],
    },
    {
        "title": "Latihan 3: Penjadwal Tugas Gradle Mini",
        "difficulty": "Menengah",
        "question": [
            "Gradle menjalankan tugas sesudah semua tugas yang dibutuhkannya",
            "selesai. Tiru penjadwal itu.",
            "",
            "Baris pertama masukan berbentuk jalankan NAMA, yaitu tugas yang",
            "diminta. Baris sesudahnya berbentuk tugas: dep1 dep2 ..., daftar",
            "tugas yang dibutuhkan (boleh kosong). Tugas yang cuma muncul",
            "sebagai dependensi dianggap nggak punya dependensi.",
            "",
            "Aturan urutan, supaya hasilnya selalu sama:",
            "  1. Mulai dari tugas yang diminta, lalu kunjungi dependensinya",
            "     satu per satu dalam urutan sort() bawaan JavaScript.",
            "  2. Sebuah tugas dicetak sesudah semua dependensinya tercetak.",
            "  3. Tugas yang sudah tercetak nggak dicetak lagi.",
            "  4. Tugas yang nggak dibutuhkan tugas yang diminta nggak dicetak.",
            "",
            "Cetak tiap tugas dengan nomor urut: 1. nama. Kalau di tengah",
            "kunjungan ketemu tugas yang sedang dikunjungi (siklus), cetak satu",
            "baris saja: siklus: a -> b -> a, mulai dari tugas yang berulang.",
            "",
            "Contoh masukan pertama:",
            "  jalankan assembleDebug",
            "  assembleDebug: packageDebug compileDebugKotlin",
            "  packageDebug: mergeDebugResources compileDebugKotlin",
            "  compileDebugKotlin: preBuild generateDebugBuildConfig",
            "  generateDebugBuildConfig: preBuild",
            "  mergeDebugResources: preBuild",
            "  testDebugUnitTest: compileDebugKotlin",
            "  preBuild:",
            "",
            "Untuk input jalankan assembleDebug, keluarannya:",
            "1. preBuild",
            "2. generateDebugBuildConfig",
            "3. compileDebugKotlin",
            "4. mergeDebugResources",
            "5. packageDebug",
            "6. assembleDebug",
            "",
            "Contoh masukan kedua:",
            "  jalankan build",
            "  build: lint",
            "  lint: compile",
            "  compile: build",
            "",
            "Untuk input jalankan build, keluarannya:",
            "siklus: build -> lint -> compile -> build",
        ],
        "hints": [
            "Ini urutan topologis yang dikerjakan dengan penelusuran kedalaman (DFS): tugas baru boleh dicetak setelah semua anaknya selesai.",
            "Pakai satu Set untuk tugas yang sudah selesai dan satu array sebagai jejak tugas yang sedang dikunjungi, supaya siklus bisa dikenali.",
            "Kalau tugas yang akan dikunjungi sudah ada di jejak, potong jejak mulai dari posisi tugas itu, tambahkan tugasnya di ujung, lalu gabungkan dengan ' -> '.",
        ],
        "solution": "const baris = require('fs').readFileSync(0, 'utf8')\n  .split('\\n').map((b) => b.trim()).filter((b) => b !== '');\nconst target = baris[0].split(/\\s+/)[1];\nconst dep = {};\nfor (const b of baris.slice(1)) {\n  const [nama, sisa] = b.split(':');\n  const isi = sisa.trim();\n  dep[nama.trim()] = isi === '' ? [] : isi.split(/\\s+/);\n}\n\nconst urutan = [];\nconst selesai = new Set();\nconst jejak = [];\n\nfunction kunjungi(tugas) {\n  if (selesai.has(tugas)) return true;\n  const i = jejak.indexOf(tugas);\n  if (i !== -1) {\n    console.log('siklus: ' + [...jejak.slice(i), tugas].join(' -> '));\n    return false;\n  }\n  jejak.push(tugas);\n  for (const d of [...(dep[tugas] || [])].sort()) {\n    if (!kunjungi(d)) return false;\n  }\n  jejak.pop();\n  selesai.add(tugas);\n  urutan.push(tugas);\n  return true;\n}\n\nif (kunjungi(target)) {\n  urutan.forEach((t, i) => console.log(`${i + 1}. ${t}`));\n}",
        "stdin_list": [
            """jalankan assembleDebug
assembleDebug: packageDebug compileDebugKotlin
packageDebug: mergeDebugResources compileDebugKotlin
compileDebugKotlin: preBuild generateDebugBuildConfig
generateDebugBuildConfig: preBuild
mergeDebugResources: preBuild
testDebugUnitTest: compileDebugKotlin
preBuild:
""",
            """jalankan build
build: lint
lint: compile
compile: build
""",
        ],
    },
    {
        "title": "Latihan 4: Recomposition Mini",
        "difficulty": "Menengah",
        "question": [
            "Tiru cara Compose memilih composable yang dipanggil ulang. Ada",
            "empat fungsi composable tiruan dengan urutan tetap:",
            "  Layar       membaca tema    menggambar: Layar (tema X)",
            "  Sapa        membaca nama    menggambar: Sapa \"Halo, X\"",
            "  Penghitung  membaca hitung  menggambar: Penghitung \"Diketuk X kali\"",
            "  Total       membaca hitung dan harga",
            "              menggambar: Total \"Total: RpX\" (X = hitung kali harga)",
            "",
            "Baris pertama masukan berbentuk awal k=v k=v ... yang mengisi state",
            "awal. Semua fungsi dipanggil sekali, lalu cetak:",
            "awal -> Layar, Sapa, Penghitung, Total",
            "",
            "Baris sesudahnya berbentuk kunci=nilai. Untuk tiap baris:",
            "  1. Ubah state-nya. Kalau nilainya sama dengan nilai lama, nggak",
            "     ada yang dipanggil ulang (seperti mutableStateOf).",
            "  2. Panggil ulang, dalam urutan tetap di atas, hanya fungsi yang",
            "     membaca kunci itu waktu terakhir dipanggil. Anak dari fungsi",
            "     yang dipanggil ulang nggak ikut dipanggil kalau ia sendiri",
            "     nggak membaca kunci itu.",
            "  3. Cetak baris masukannya, panah, lalu nama fungsi yang dipanggil",
            "     ulang dipisah koma. Kalau nggak ada, cetak (tidak ada).",
            "",
            "Catat bacaan secara otomatis: bikin fungsi baca(kunci) yang",
            "mencatat fungsi mana yang sedang berjalan, jangan menulis daftar",
            "pembaca dengan tangan.",
            "",
            "Di akhir, cetak pohon akhir (Layar di kolom pertama, tiga lainnya",
            "menjorok dua spasi) dan jumlah panggilan tiap fungsi.",
            "",
            "Contoh masukan pertama:",
            "  awal hitung=0 harga=2000 nama=Rina tema=terang",
            "  hitung=1",
            "  hitung=1",
            "  nama=Budi",
            "  harga=2500",
            "  tema=gelap",
            "  hitung=3",
            "",
            "Untuk input awal hitung=0 harga=2000 nama=Rina tema=terang, keluarannya:",
            "awal -> Layar, Sapa, Penghitung, Total",
            "hitung=1 -> Penghitung, Total",
            "hitung=1 -> (tidak ada)",
            "nama=Budi -> Sapa",
            "harga=2500 -> Total",
            "tema=gelap -> Layar",
            "hitung=3 -> Penghitung, Total",
            "pohon akhir:",
            "Layar (tema gelap)",
            "  Sapa \"Halo, Budi\"",
            "  Penghitung \"Diketuk 3 kali\"",
            "  Total \"Total: Rp7500\"",
            "panggilan: Layar 2, Sapa 2, Penghitung 3, Total 4",
            "",
            "Contoh masukan kedua memuat kunci yang nggak dibaca siapa pun:",
            "  awal hitung=5 harga=1000 nama=Sari tema=gelap",
            "  bahasa=id",
            "  tema=gelap",
            "  hitung=0",
            "",
            "Untuk input awal hitung=5 harga=1000 nama=Sari tema=gelap, keluarannya:",
            "awal -> Layar, Sapa, Penghitung, Total",
            "bahasa=id -> (tidak ada)",
            "tema=gelap -> (tidak ada)",
            "hitung=0 -> Penghitung, Total",
            "pohon akhir:",
            "Layar (tema gelap)",
            "  Sapa \"Halo, Sari\"",
            "  Penghitung \"Diketuk 0 kali\"",
            "  Total \"Total: Rp0\"",
            "panggilan: Layar 1, Sapa 1, Penghitung 2, Total 2",
        ],
        "hints": [
            "Simpan siapa membaca apa dalam objek yang memetakan kunci state ke Set berisi nama fungsi.",
            "Sebelum sebuah fungsi dipanggil, hapus dulu namanya dari semua Set, lalu simpan namanya di variabel yang sedang berjalan supaya baca() tahu siapa pembacanya.",
            "Untuk tiap perubahan, saring daftar urutan tetap dengan pembaca[kunci].has(nama), baru panggil hasil saringannya satu per satu.",
        ],
        "solution": "const baris = require('fs').readFileSync(0, 'utf8')\n  .split('\\n').map((b) => b.trim()).filter((b) => b !== '');\n\nconst state = {};\nconst pembaca = {};    // kunci -> Set nama fungsi yang membacanya\nconst panggilan = {};  // nama fungsi -> jumlah panggilan\nconst gambar = {};     // nama fungsi -> hasil gambarnya\nlet sedang = null;     // fungsi yang sedang berjalan\n\nfunction baca(kunci) {\n  if (!pembaca[kunci]) pembaca[kunci] = new Set();\n  pembaca[kunci].add(sedang);\n  return state[kunci];\n}\n\nconst komponen = {\n  Layar: () => `Layar (tema ${baca('tema')})`,\n  Sapa: () => `Sapa \"Halo, ${baca('nama')}\"`,\n  Penghitung: () => `Penghitung \"Diketuk ${baca('hitung')} kali\"`,\n  Total: () => `Total \"Total: Rp${Number(baca('hitung')) * Number(baca('harga'))}\"`,\n};\nconst URUTAN = ['Layar', 'Sapa', 'Penghitung', 'Total'];\n\nfunction panggil(nama) {\n  for (const k in pembaca) pembaca[k].delete(nama);\n  sedang = nama;\n  gambar[nama] = komponen[nama]();\n  sedang = null;\n  panggilan[nama] = (panggilan[nama] || 0) + 1;\n}\n\nfor (const pasangan of baris[0].split(/\\s+/).slice(1)) {\n  const [k, v] = pasangan.split('=');\n  state[k] = v;\n}\nURUTAN.forEach(panggil);\nconsole.log('awal -> ' + URUTAN.join(', '));\n\nfor (const b of baris.slice(1)) {\n  const [k, v] = b.split('=');\n  const lama = state[k];\n  state[k] = v;\n  const ulang = lama === v ? []\n    : URUTAN.filter((n) => pembaca[k] !== undefined && pembaca[k].has(n));\n  ulang.forEach(panggil);\n  console.log(`${b} -> ${ulang.length ? ulang.join(', ') : '(tidak ada)'}`);\n}\n\nconsole.log('pohon akhir:');\nconsole.log(gambar.Layar);\nfor (const n of URUTAN.slice(1)) console.log('  ' + gambar[n]);\nconsole.log('panggilan: ' + URUTAN.map((n) => `${n} ${panggilan[n]}`).join(', '));",
        "stdin_list": [
            """awal hitung=0 harga=2000 nama=Rina tema=terang
hitung=1
hitung=1
nama=Budi
harga=2500
tema=gelap
hitung=3
""",
            """awal hitung=5 harga=1000 nama=Sari tema=gelap
bahasa=id
tema=gelap
hitung=0
""",
        ],
    },
    {
        "title": "Latihan 5: Kontainer Dependency Injection Mini",
        "difficulty": "Menengah",
        "question": [
            "Bikin kontainer DI kecil yang merakit objek dari daftar provider.",
            "",
            "Baris pertama masukan berbentuk minta A B C, yaitu objek yang",
            "diminta, berurutan. Baris sesudahnya provider:",
            "  Nama: dep1 dep2      objek baru setiap kali dibutuhkan",
            "  singleton Nama: dep  dibuat sekali, lalu dipakai bersama",
            "Dependensi dibuat dalam urutan penulisannya, sebelum objeknya.",
            "",
            "Untuk tiap nama yang diminta, cetak minta Nama, lalu langkahnya",
            "menjorok dua spasi:",
            "  buat Nama#n   objek baru dibuat; n = objek Nama ke berapa",
            "  pakai Nama#n  singleton yang sudah ada dipakai lagi; dependensi",
            "                singleton itu nggak dikunjungi lagi",
            "Di akhir cetak total objek dibuat: N.",
            "",
            "Dua galat menghentikan program seketika (tanpa baris total):",
            "  siklus: A -> B -> A        objek yang sedang dirakit dibutuhkan",
            "                             lagi; mulai dari objek yang berulang",
            "  galat: X tidak punya provider (dibutuhkan Y)",
            "Kalau X diminta langsung lewat baris minta, tulis (diminta langsung).",
            "",
            "Contoh masukan pertama:",
            "  minta CatatanViewModel CatatanViewModel TokoApi",
            "  singleton OkHttpClient:",
            "  singleton Retrofit: OkHttpClient",
            "  TokoApi: Retrofit",
            "  singleton Database:",
            "  CatatanDao: Database",
            "  CatatanRepository: CatatanDao TokoApi",
            "  CatatanViewModel: CatatanRepository",
            "",
            "Untuk input minta CatatanViewModel CatatanViewModel TokoApi, keluarannya:",
            "minta CatatanViewModel",
            "  buat Database#1",
            "  buat CatatanDao#1",
            "  buat OkHttpClient#1",
            "  buat Retrofit#1",
            "  buat TokoApi#1",
            "  buat CatatanRepository#1",
            "  buat CatatanViewModel#1",
            "minta CatatanViewModel",
            "  pakai Database#1",
            "  buat CatatanDao#2",
            "  pakai Retrofit#1",
            "  buat TokoApi#2",
            "  buat CatatanRepository#2",
            "  buat CatatanViewModel#2",
            "minta TokoApi",
            "  pakai Retrofit#1",
            "  buat TokoApi#3",
            "total objek dibuat: 12",
            "",
            "Contoh masukan kedua: minta Layar, singleton Logger:, Layar: Logger",
            "ViewModel, ViewModel: Repo, Repo: ViewModel (satu per baris).",
            "",
            "Untuk input minta Layar, keluarannya:",
            "minta Layar",
            "  buat Logger#1",
            "  siklus: ViewModel -> Repo -> ViewModel",
            "",
            "Contoh masukan ketiga: minta Beranda, lalu Beranda: Tema.",
            "",
            "Untuk input minta Beranda, keluarannya:",
            "minta Beranda",
            "  galat: Tema tidak punya provider (dibutuhkan Beranda)",
        ],
        "hints": [
            "Simpan tiap provider sebagai objek berisi penanda singleton dan daftar dependensinya, lalu tulis satu fungsi rekursif yang merakit satu nama.",
            "Fungsi perakit butuh jejak nama yang sedang dirakit untuk mengenali siklus, plus objek penghitung per nama dan objek penyimpan label singleton.",
            "Lempar Error khusus untuk siklus dan provider yang hilang, lalu tangkap di luar perulangan minta supaya program berhenti setelah mencetak pesannya.",
        ],
        "solution": "const baris = require('fs').readFileSync(0, 'utf8')\n  .split('\\n').map((b) => b.trim()).filter((b) => b !== '');\n\nconst diminta = baris[0].split(/\\s+/).slice(1);\nconst provider = {};\nfor (const b of baris.slice(1)) {\n  const singleton = b.startsWith('singleton ');\n  const teks = singleton ? b.slice('singleton '.length) : b;\n  const [nama, sisa] = teks.split(':');\n  const isi = sisa.trim();\n  provider[nama.trim()] = { singleton, dep: isi === '' ? [] : isi.split(/\\s+/) };\n}\n\nclass GalatDI extends Error {}\nconst nomor = {};\nconst tunggal = {};\nlet total = 0;\n\nfunction rakit(nama, jejak, peminta) {\n  const p = provider[nama];\n  if (!p) {\n    const asal = peminta ? `dibutuhkan ${peminta}` : 'diminta langsung';\n    throw new GalatDI(`galat: ${nama} tidak punya provider (${asal})`);\n  }\n  if (p.singleton && tunggal[nama]) {\n    console.log(`  pakai ${tunggal[nama]}`);\n    return;\n  }\n  if (jejak.includes(nama)) {\n    const putaran = [...jejak.slice(jejak.indexOf(nama)), nama];\n    throw new GalatDI('siklus: ' + putaran.join(' -> '));\n  }\n  for (const d of p.dep) rakit(d, [...jejak, nama], nama);\n  nomor[nama] = (nomor[nama] || 0) + 1;\n  total += 1;\n  const label = `${nama}#${nomor[nama]}`;\n  if (p.singleton) tunggal[nama] = label;\n  console.log(`  buat ${label}`);\n}\n\ntry {\n  for (const nama of diminta) {\n    console.log(`minta ${nama}`);\n    rakit(nama, [], null);\n  }\n  console.log(`total objek dibuat: ${total}`);\n} catch (e) {\n  if (!(e instanceof GalatDI)) throw e;\n  console.log(`  ${e.message}`);\n}",
        "stdin_list": [
            """minta CatatanViewModel CatatanViewModel TokoApi
singleton OkHttpClient:
singleton Retrofit: OkHttpClient
TokoApi: Retrofit
singleton Database:
CatatanDao: Database
CatatanRepository: CatatanDao TokoApi
CatatanViewModel: CatatanRepository
""",
            """minta Layar
singleton Logger:
Layar: Logger ViewModel
ViewModel: Repo
Repo: ViewModel
""",
            """minta Beranda
Beranda: Tema
""",
        ],
    },
    {
        "title": "Latihan 6: Rantai Interceptor HTTP",
        "difficulty": "Menengah",
        "question": [
            "Tiru rantai interceptor OkHttp dengan server tiruan di memori.",
            "Masukan berisi satu permintaan per baris: METODE /alamat.",
            "",
            "Rantainya berurutan logging -> cache -> token -> server:",
            "  logging  cetak --> METODE /alamat, teruskan, lalu cetak",
            "           <-- KODE /alamat (dari server) atau (dari cache)",
            "  cache    untuk metode selain GET cetak [cache] bukan GET,",
            "           teruskan. Untuk GET yang alamatnya sudah tersimpan,",
            "           cetak [cache] ada, potong rantai, lalu kembalikan",
            "           respons simpanan tanpa meneruskan. Selain itu cetak",
            "           [cache] tidak ada, teruskan; kalau responsnya 200,",
            "           simpan dan cetak [cache] simpan /alamat.",
            "  token    cetak [token] tambah Authorization, tempel header",
            "           Authorization, lalu teruskan.",
            "  server   tanpa header Authorization jawab 401. Selain itu:",
            "           GET /produk/1     200 {\"id\":1,\"nama\":\"Teh botol\"}",
            "           GET /produk/2     200 {\"id\":2,\"nama\":\"Roti bakar\"}",
            "           GET /produk/lain  404 {\"galat\":\"produk tidak ada\"}",
            "           POST /pesanan     201 {\"status\":\"diterima\"}",
            "           selain itu        404 {\"galat\":\"rute tidak ada\"}",
            "           dan cetak [server] KODE ISI.",
            "Baris yang dicetak cache, token, dan server menjorok dua spasi.",
            "Di akhir cetak ringkas: N permintaan, C dari cache, S ke server.",
            "",
            "Keluaran yang diharapkan:",
            "--> GET /produk/1",
            "  [cache] tidak ada, teruskan",
            "  [token] tambah Authorization",
            "  [server] 200 {\"id\":1,\"nama\":\"Teh botol\"}",
            "  [cache] simpan /produk/1",
            "<-- 200 /produk/1 (dari server)",
            "--> GET /produk/2",
            "  [cache] tidak ada, teruskan",
            "  [token] tambah Authorization",
            "  [server] 200 {\"id\":2,\"nama\":\"Roti bakar\"}",
            "  [cache] simpan /produk/2",
            "<-- 200 /produk/2 (dari server)",
            "--> GET /produk/1",
            "  [cache] ada, potong rantai",
            "<-- 200 /produk/1 (dari cache)",
            "--> GET /produk/9",
            "  [cache] tidak ada, teruskan",
            "  [token] tambah Authorization",
            "  [server] 404 {\"galat\":\"produk tidak ada\"}",
            "<-- 404 /produk/9 (dari server)",
            "--> POST /pesanan",
            "  [cache] bukan GET, teruskan",
            "  [token] tambah Authorization",
            "  [server] 201 {\"status\":\"diterima\"}",
            "<-- 201 /pesanan (dari server)",
            "--> GET /produk/9",
            "  [cache] tidak ada, teruskan",
            "  [token] tambah Authorization",
            "  [server] 404 {\"galat\":\"produk tidak ada\"}",
            "<-- 404 /produk/9 (dari server)",
            "--> GET /produk/2",
            "  [cache] ada, potong rantai",
            "<-- 200 /produk/2 (dari cache)",
            "ringkas: 7 permintaan, 2 dari cache, 5 ke server",
        ],
        "hints": [
            "Tiap interceptor adalah fungsi yang menerima objek berisi request dan fungsi proceed, persis seperti tiruan rantai di materi Retrofit dan OkHttp.",
            "Simpan cache di sebuah Map dengan kunci alamat, dan tandai setiap respons dengan asalnya supaya logging tahu harus mencetak dari server atau dari cache.",
            "Isi JSON server paling gampang dibuat dengan JSON.stringify, dan alamat produk bisa dicocokkan dengan pola regex /^\\/produk\\/(\\d+)$/.",
        ],
        "solution": "const baris = require('fs').readFileSync(0, 'utf8')\n  .split('\\n').map((b) => b.trim()).filter((b) => b !== '');\n\nconst PRODUK = { 1: 'Teh botol', 2: 'Roti bakar' };\n\nfunction server(req) {\n  let res;\n  const cocok = req.url.match(/^\\/produk\\/(\\d+)$/);\n  if (!req.header.Authorization) {\n    res = { kode: 401, isi: JSON.stringify({ galat: 'butuh token' }) };\n  } else if (req.metode === 'GET' && cocok) {\n    const nama = PRODUK[cocok[1]];\n    res = nama\n      ? { kode: 200, isi: JSON.stringify({ id: Number(cocok[1]), nama }) }\n      : { kode: 404, isi: JSON.stringify({ galat: 'produk tidak ada' }) };\n  } else if (req.metode === 'POST' && req.url === '/pesanan') {\n    res = { kode: 201, isi: JSON.stringify({ status: 'diterima' }) };\n  } else {\n    res = { kode: 404, isi: JSON.stringify({ galat: 'rute tidak ada' }) };\n  }\n  console.log(`  [server] ${res.kode} ${res.isi}`);\n  return { ...res, sumber: 'server' };\n}\n\nconst simpanan = new Map();\n\nconst logging = (chain) => {\n  const req = chain.request;\n  console.log(`--> ${req.metode} ${req.url}`);\n  const res = chain.proceed(req);\n  console.log(`<-- ${res.kode} ${req.url} (dari ${res.sumber})`);\n  return res;\n};\n\nconst cache = (chain) => {\n  const req = chain.request;\n  if (req.metode !== 'GET') {\n    console.log('  [cache] bukan GET, teruskan');\n    return chain.proceed(req);\n  }\n  if (simpanan.has(req.url)) {\n    console.log('  [cache] ada, potong rantai');\n    return { ...simpanan.get(req.url), sumber: 'cache' };\n  }\n  console.log('  [cache] tidak ada, teruskan');\n  const res = chain.proceed(req);\n  if (res.kode === 200) {\n    simpanan.set(req.url, res);\n    console.log(`  [cache] simpan ${req.url}`);\n  }\n  return res;\n};\n\nconst token = (chain) => {\n  console.log('  [token] tambah Authorization');\n  const header = { ...chain.request.header, Authorization: 'Bearer rahasia123' };\n  return chain.proceed({ ...chain.request, header });\n};\n\nfunction rantai(interceptors, akhir) {\n  const jalan = (i, req) => (i === interceptors.length\n    ? akhir(req)\n    : interceptors[i]({ request: req, proceed: (r) => jalan(i + 1, r) }));\n  return (req) => jalan(0, req);\n}\n\nconst kirim = rantai([logging, cache, token], server);\nlet dariCache = 0;\nfor (const b of baris) {\n  const [metode, url] = b.split(/\\s+/);\n  const res = kirim({ metode, url, header: {} });\n  if (res.sumber === 'cache') dariCache += 1;\n}\nconst n = baris.length;\nconsole.log(`ringkas: ${n} permintaan, ${dariCache} dari cache, ${n - dariCache} ke server`);",
        "stdin": """GET /produk/1
GET /produk/2
GET /produk/1
GET /produk/9
POST /pesanan
GET /produk/9
GET /produk/2
""",
    },
    {
        "title": "Latihan 7: Diffing Tampilan Deklaratif",
        "difficulty": "Menengah",
        "question": [
            "SwiftUI dan Compose membandingkan susunan view lama dengan yang baru,",
            "lalu cuma mengubah bagian yang beda. Tulis versi mininya.",
            "",
            "Input berisi dua pohon view dalam format JSON, dipisah baris ---.",
            "Pohon kedua adalah tampilan sesudah state berubah. Tiap simpul punya",
            "tipe, boleh punya teks, dan boleh punya anak (daftar simpul).",
            "",
            "Bandingkan simpul lama dan baru di posisi yang sama, mulai dari akar:",
            "  - Hanya ada di lama: cetak hapus.",
            "  - Hanya ada di baru: cetak tambah.",
            "  - Tipe beda: cetak hapus lalu tambah, tanpa memeriksa anaknya.",
            "  - Tipe sama, teks beda: cetak ubah teks, lalu periksa anaknya.",
            "  - Tipe dan teks sama: cetak tetap, lalu periksa anaknya.",
            "",
            "Anak dicocokkan menurut urutannya (indeks 0, 1, 2, ...). Jalur akar",
            "adalah 0, anaknya 0.0, 0.1, dan seterusnya. Simpul ditulis tipe",
            "\"teks\", atau tipe saja kalau tanpa teks. Akhiri dengan ringkasan.",
            "",
            "Contoh input:",
            "  {\"tipe\": \"VStack\", \"anak\": [",
            "    {\"tipe\": \"Text\", \"teks\": \"Halo\"},",
            "    {\"tipe\": \"Image\", \"teks\": \"logo\"},",
            "    {\"tipe\": \"Button\", \"teks\": \"Masuk\"}]}",
            "  ---",
            "  {\"tipe\": \"VStack\", \"anak\": [",
            "    {\"tipe\": \"Text\", \"teks\": \"Halo, Rina\"},",
            "    {\"tipe\": \"Text\", \"teks\": \"logo\"},",
            "    {\"tipe\": \"Button\", \"teks\": \"Masuk\"},",
            "    {\"tipe\": \"Button\", \"teks\": \"Daftar\"}]}",
            "",
            "Keluaran yang diharapkan:",
            "tetap 0 VStack",
            "ubah teks 0.0 Text \"Halo\" -> \"Halo, Rina\"",
            "hapus 0.1 Image \"logo\"",
            "tambah 0.1 Text \"logo\"",
            "tetap 0.2 Button \"Masuk\"",
            "tambah 0.3 Button \"Daftar\"",
            "ringkasan: 2 tambah, 1 hapus, 1 ubah teks, 2 tetap",
            "",
            "Perhatikan kasus ketiga di penilaian: menghapus butir pertama sebuah",
            "daftar membuat semua butir sesudahnya terlihat berubah. Itu alasan",
            "SwiftUI meminta id pada isi ForEach.",
        ],
        "hints": [
            "Pisahkan input jadi dua teks di baris ---, lalu ubah masing-masing jadi objek dengan JSON.parse.",
            "Tulis satu fungsi rekursif banding(lama, baru, jalur) yang menangani lima kasus di soal, dan panggil lagi untuk setiap indeks anak sampai jumlah anak terbanyak di antara keduanya.",
            "Untuk anak ke-i, panggil banding(anakLama[i], anakBaru[i], jalur + '.' + i); nilai undefined menandakan simpul itu nggak ada di salah satu sisi.",
        ],
        "solution": "const masukan = require('fs').readFileSync(0, 'utf8');\nconst [teksLama, teksBaru] = masukan.split(/^---\\s*$/m);\nconst lama = JSON.parse(teksLama);\nconst baru = JSON.parse(teksBaru);\n\nconst hitung = { tambah: 0, hapus: 0, ubah: 0, tetap: 0 };\n\nfunction label(node) {\n  return node.teks === undefined ? node.tipe : `${node.tipe} \"${node.teks}\"`;\n}\n\nfunction banding(a, b, jalur) {\n  if (a && !b) {\n    console.log(`hapus ${jalur} ${label(a)}`);\n    hitung.hapus++;\n    return;\n  }\n  if (!a && b) {\n    console.log(`tambah ${jalur} ${label(b)}`);\n    hitung.tambah++;\n    return;\n  }\n  if (a.tipe !== b.tipe) {\n    console.log(`hapus ${jalur} ${label(a)}`);\n    console.log(`tambah ${jalur} ${label(b)}`);\n    hitung.hapus++;\n    hitung.tambah++;\n    return;\n  }\n  if (a.teks !== b.teks) {\n    console.log(`ubah teks ${jalur} ${a.tipe} \"${a.teks}\" -> \"${b.teks}\"`);\n    hitung.ubah++;\n  } else {\n    console.log(`tetap ${jalur} ${label(a)}`);\n    hitung.tetap++;\n  }\n  const anakA = a.anak || [];\n  const anakB = b.anak || [];\n  const n = Math.max(anakA.length, anakB.length);\n  for (let i = 0; i < n; i++) {\n    banding(anakA[i], anakB[i], `${jalur}.${i}`);\n  }\n}\n\nbanding(lama, baru, '0');\nconsole.log(`ringkasan: ${hitung.tambah} tambah, ${hitung.hapus} hapus, ` +\n  `${hitung.ubah} ubah teks, ${hitung.tetap} tetap`);\n",
        "stdin_list": [
            """{"tipe": "VStack", "anak": [
  {"tipe": "Text", "teks": "Halo"},
  {"tipe": "Image", "teks": "logo"},
  {"tipe": "Button", "teks": "Masuk"}]}
---
{"tipe": "VStack", "anak": [
  {"tipe": "Text", "teks": "Halo, Rina"},
  {"tipe": "Text", "teks": "logo"},
  {"tipe": "Button", "teks": "Masuk"},
  {"tipe": "Button", "teks": "Daftar"}]}
""",
            """{"tipe": "List", "anak": [
  {"tipe": "HStack", "anak": [
    {"tipe": "Text", "teks": "Kopi"}, {"tipe": "Text", "teks": "18000"}]},
  {"tipe": "HStack", "anak": [
    {"tipe": "Text", "teks": "Teh"}, {"tipe": "Text", "teks": "8000"}]}]}
---
{"tipe": "List", "anak": [
  {"tipe": "HStack", "anak": [
    {"tipe": "Text", "teks": "Kopi"}, {"tipe": "Text", "teks": "20000"}]}]}
""",
            """{"tipe": "List", "anak": [
  {"tipe": "Text", "teks": "Ani"},
  {"tipe": "Text", "teks": "Budi"},
  {"tipe": "Text", "teks": "Citra"}]}
---
{"tipe": "List", "anak": [
  {"tipe": "Text", "teks": "Budi"},
  {"tipe": "Text", "teks": "Citra"}]}
""",
        ],
    },
    {
        "title": "Latihan 8: Reducer Event ke State ala Bloc",
        "difficulty": "Menengah",
        "question": [
            "Bloc menerima event lalu menghitung state baru tanpa mengubah state",
            "lama. Tulis versi mininya sebagai fungsi murni di JavaScript.",
            "",
            "State berisi nilai (angka) dan status (teks). State awal:",
            "{nilai: 0, status: siap}. Input berisi satu event per baris:",
            "  tambah N    nilai bertambah N, status jadi siap",
            "  kurang N    nilai berkurang N dan status siap; kalau hasilnya",
            "              negatif, nilai tetap dan status jadi ditolak",
            "  reset       kembali ke {nilai: 0, status: siap}",
            "  muat_gagal  nilai tetap, status jadi gagal",
            "",
            "Untuk setiap event, cetak transisinya dengan format",
            "state lama -> event -> state baru. Seperti Bloc, state baru yang",
            "sama persis dengan state sekarang nggak dipancarkan: cetak",
            "state sekarang -> event -> sama, tidak dipancarkan. Event lain",
            "dicetak sebagai event tidak dikenal: <isi baris>.",
            "",
            "Di akhir, cetak jumlah state yang dipancarkan, lalu state awal",
            "untuk membuktikan state awal nggak pernah diubah.",
            "",
            "Contoh input:",
            "  tambah 2",
            "  tambah 3",
            "  kurang 1",
            "  kurang 10",
            "  muat_gagal",
            "  muat_gagal",
            "  reset",
            "  reset",
            "",
            "Untuk input tambah 2, keluarannya:",
            "{nilai: 0, status: siap} -> tambah 2 -> {nilai: 2, status: siap}",
            "{nilai: 2, status: siap} -> tambah 3 -> {nilai: 5, status: siap}",
            "{nilai: 5, status: siap} -> kurang 1 -> {nilai: 4, status: siap}",
            "{nilai: 4, status: siap} -> kurang 10 -> {nilai: 4, status: ditolak}",
            "{nilai: 4, status: ditolak} -> muat_gagal -> {nilai: 4, status: gagal}",
            "{nilai: 4, status: gagal} -> muat_gagal -> sama, tidak dipancarkan",
            "{nilai: 4, status: gagal} -> reset -> {nilai: 0, status: siap}",
            "{nilai: 0, status: siap} -> reset -> sama, tidak dipancarkan",
            "state dipancarkan: 6",
            "state awal tetap: {nilai: 0, status: siap}",
        ],
        "hints": [
            "Pisahkan dua tugas: satu fungsi murni yang menerima state dan event lalu mengembalikan objek state baru, dan satu perulangan yang mencetak transisinya.",
            "Bekukan state awal dengan Object.freeze supaya kesalahan mengubah state lama langsung ketahuan, lalu bandingkan nilai dan status state baru dengan state sekarang sebelum memutuskan dipancarkan atau tidak.",
            "Di dalam fungsi murni, selalu kembalikan objek baru seperti { nilai: state.nilai + n, status: 'siap' }, dan kembalikan null untuk event yang nggak dikenal.",
        ],
        "solution": "const baris = require('fs').readFileSync(0, 'utf8').split('\\n')\n  .map((b) => b.trim()).filter((b) => b !== '');\n\nfunction tulis(s) {\n  return `{nilai: ${s.nilai}, status: ${s.status}}`;\n}\n\nfunction reducer(state, event) {\n  const [nama, arg] = event.split(' ');\n  const n = Number(arg);\n  if (nama === 'tambah') return { nilai: state.nilai + n, status: 'siap' };\n  if (nama === 'kurang') {\n    if (state.nilai - n < 0) return { nilai: state.nilai, status: 'ditolak' };\n    return { nilai: state.nilai - n, status: 'siap' };\n  }\n  if (nama === 'reset') return { nilai: 0, status: 'siap' };\n  if (nama === 'muat_gagal') return { nilai: state.nilai, status: 'gagal' };\n  return null;\n}\n\nconst awal = Object.freeze({ nilai: 0, status: 'siap' });\nlet state = awal;\nlet dipancarkan = 0;\nfor (const event of baris) {\n  const baru = reducer(state, event);\n  if (baru === null) {\n    console.log(`event tidak dikenal: ${event}`);\n  } else if (baru.nilai === state.nilai && baru.status === state.status) {\n    console.log(`${tulis(state)} -> ${event} -> sama, tidak dipancarkan`);\n  } else {\n    console.log(`${tulis(state)} -> ${event} -> ${tulis(baru)}`);\n    state = Object.freeze(baru);\n    dipancarkan++;\n  }\n}\nconsole.log(`state dipancarkan: ${dipancarkan}`);\nconsole.log(`state awal tetap: ${tulis(awal)}`);\n",
        "stdin_list": [
            """tambah 2
tambah 3
kurang 1
kurang 10
muat_gagal
muat_gagal
reset
reset
""",
            """reset
kurang 1
tambah 5
lompat 2
kurang 5
""",
        ],
    },
    {
        "title": "Latihan 9: Reducer Navigator Stack",
        "difficulty": "Menengah",
        "question": [
            "Navigator stack menyimpan daftar layar. Tulis reducer-nya: fungsi",
            "yang menerima isi stack dan satu aksi, lalu mengembalikan stack",
            "baru tanpa mengubah yang lama.",
            "",
            "Stack awal berisi [Beranda]. Input berisi satu aksi per baris:",
            "  push X      selalu menambah X di atas",
            "  navigate X  kalau X sudah ada di stack, mundur sampai X teratas",
            "              (pakai X yang paling atas kalau ada lebih dari satu);",
            "              kalau belum ada, tambah X di atas",
            "  goBack      buang layar teratas; kalau tinggal satu layar,",
            "              aksi diabaikan",
            "  reset X     ganti seluruh stack jadi [X]",
            "",
            "Aturan navigate di latihan ini mengikuti router.navigate di Expo",
            "Router. (Di React Navigation 7, perilaku mundur ke layar yang sudah",
            "ada dipegang popTo.)",
            "",
            "Cetak baris awal -> [Beranda], lalu isi stack sesudah setiap aksi,",
            "dan terakhir layar yang aktif.",
            "",
            "Contoh input:",
            "  push Produk",
            "  push Detail",
            "  navigate Keranjang",
            "  navigate Produk",
            "  push Produk",
            "  goBack",
            "  reset Masuk",
            "  goBack",
            "",
            "Untuk input push Produk, keluarannya:",
            "awal -> [Beranda]",
            "push Produk -> [Beranda, Produk]",
            "push Detail -> [Beranda, Produk, Detail]",
            "navigate Keranjang -> [Beranda, Produk, Detail, Keranjang]",
            "navigate Produk -> [Beranda, Produk]",
            "push Produk -> [Beranda, Produk, Produk]",
            "goBack -> [Beranda, Produk]",
            "reset Masuk -> [Masuk]",
            "goBack -> diabaikan, sudah di layar pertama",
            "layar aktif: Masuk",
        ],
        "hints": [
            "Simpan stack sebagai array berisi nama layar, dan buat setiap aksi menghasilkan array baru supaya mudah diuji seperti reducer.",
            "Untuk navigate, cari posisi terakhir layar itu dengan lastIndexOf, lalu potong array sampai posisi itu; kalau hasilnya -1, tambahkan layarnya di ujung.",
            "Bentuk reducer-nya bisa begini: if (nama === 'push') return [...stack, layar]; dan untuk goBack kembalikan null saat stack.length === 1 supaya pemanggil tahu aksinya diabaikan.",
        ],
        "solution": "const aksi = require('fs').readFileSync(0, 'utf8').split('\\n')\n  .map((b) => b.trim()).filter((b) => b !== '');\n\nfunction kurangi(stack, perintah) {\n  const [nama, layar] = perintah.split(' ');\n  if (nama === 'push') return [...stack, layar];\n  if (nama === 'navigate') {\n    const i = stack.lastIndexOf(layar);\n    if (i === -1) return [...stack, layar];\n    return stack.slice(0, i + 1);\n  }\n  if (nama === 'goBack') {\n    if (stack.length === 1) return null;\n    return stack.slice(0, -1);\n  }\n  if (nama === 'reset') return [layar];\n  throw new Error(`aksi tidak dikenal: ${perintah}`);\n}\n\nlet stack = ['Beranda'];\nconsole.log(`awal -> [${stack.join(', ')}]`);\nfor (const perintah of aksi) {\n  const baru = kurangi(stack, perintah);\n  if (baru === null) {\n    console.log(`${perintah} -> diabaikan, sudah di layar pertama`);\n    continue;\n  }\n  stack = baru;\n  console.log(`${perintah} -> [${stack.join(', ')}]`);\n}\nconsole.log(`layar aktif: ${stack[stack.length - 1]}`);\n",
        "stdin_list": [
            """push Produk
push Detail
navigate Keranjang
navigate Produk
push Produk
goBack
reset Masuk
goBack
""",
            """navigate Profil
navigate Profil
push Profil
navigate Beranda
goBack
""",
        ],
    },
    {
        "title": "Latihan 10: Router Berbasis Berkas Mini",
        "difficulty": "Lanjut",
        "question": [
            "Expo Router mengubah susunan berkas di folder app/ jadi daftar rute.",
            "Tulis versi mininya.",
            "",
            "Baris pertama input berisi daftar jalur berkas, dipisah spasi.",
            "Setiap baris sesudahnya adalah satu alamat yang dibuka pengguna.",
            "",
            "Cara mengubah jalur berkas jadi rute:",
            "  - Buang awalan app/ dan akhiran .tsx, lalu pecah per garis miring.",
            "  - Ruas terakhir index dibuang (app/produk/index.tsx jadi /produk).",
            "  - Ruas dalam kurung seperti (tabs) dibuang dari rute.",
            "  - Berkas yang namanya diawali _ (misalnya _layout.tsx) bukan rute.",
            "  - +not-found.tsx bukan rute; ia ditampilkan kalau nggak ada yang",
            "    cocok.",
            "",
            "Cara mencocokkan alamat: buang bagian ?... dan garis miring di",
            "ujung, lalu pecah per garis miring. [nama] cocok dengan tepat satu",
            "ruas dan jadi parameter nama=isi. [...nama] di ruas terakhir cocok",
            "dengan satu ruas atau lebih, dan isinya digabung dengan garis",
            "miring. Kalau beberapa rute cocok, pilih yang paling spesifik:",
            "bandingkan ruas demi ruas dari depan, ruas tetap menang atas [nama],",
            "dan [nama] menang atas [...nama].",
            "",
            "Cetak alamat -> berkas, ditambah (parameter) kalau ada. Kalau nggak",
            "ada yang cocok, cetak alamat -> 404, tampilkan <berkas +not-found>,",
            "atau alamat -> 404 kalau berkas itu nggak ada.",
            "",
            "Contoh input (baris pertama ditulis dalam satu baris):",
            "  app/_layout.tsx app/index.tsx app/(tabs)/_layout.tsx",
            "  app/(tabs)/profil.tsx app/user/[id].tsx app/user/baru.tsx",
            "  app/docs/[...slug].tsx app/+not-found.tsx",
            "  /",
            "  /profil",
            "  /user/42",
            "  /user/baru",
            "  /docs/kotlin/coroutine",
            "  /docs",
            "  /user/42/foto",
            "  /toko?promo=1",
            "",
            "Keluaran yang diharapkan:",
            "/ -> app/index.tsx",
            "/profil -> app/(tabs)/profil.tsx",
            "/user/42 -> app/user/[id].tsx (id=42)",
            "/user/baru -> app/user/baru.tsx",
            "/docs/kotlin/coroutine -> app/docs/[...slug].tsx (slug=kotlin/coroutine)",
            "/docs -> 404, tampilkan app/+not-found.tsx",
            "/user/42/foto -> 404, tampilkan app/+not-found.tsx",
            "/toko?promo=1 -> 404, tampilkan app/+not-found.tsx",
        ],
        "hints": [
            "Kerjakan dalam dua tahap: ubah dulu setiap jalur berkas jadi daftar ruas rute, baru sesudah itu cocokkan setiap alamat dengan semua rute.",
            "Saat mencocokkan, catat bobot tiap ruas (0 untuk ruas tetap, 1 untuk [nama], 2 untuk [...nama]) supaya rute yang paling spesifik bisa dipilih dengan membandingkan bobot dari depan.",
            "Ruas dinamis bisa dikenali dengan /^\\[(\\w+)\\]$/ dan ruas sisa dengan /^\\[\\.\\.\\.(\\w+)\\]$/; ruas sisa harus ruas terakhir rute dan butuh minimal satu ruas alamat yang tersisa.",
        ],
        "solution": "const baris = require('fs').readFileSync(0, 'utf8').split('\\n')\n  .map((b) => b.trim()).filter((b) => b !== '');\nconst berkas = baris[0].split(/\\s+/);\nconst daftarUrl = baris.slice(1);\n\nfunction keRute(jalur) {\n  const ruas = jalur.replace(/^app\\//, '').replace(/\\.tsx$/, '').split('/');\n  if (ruas[ruas.length - 1] === 'index') ruas.pop();\n  return ruas.filter((r) => !/^\\(.*\\)$/.test(r));\n}\n\nconst rute = [];\nlet tidakKetemu = null;\nfor (const jalur of berkas) {\n  const nama = jalur.split('/').pop();\n  if (nama === '+not-found.tsx') {\n    tidakKetemu = jalur;\n  } else if (!nama.startsWith('_')) {\n    rute.push({ jalur, ruas: keRute(jalur) });\n  }\n}\n\nfunction cocok(ruasRute, ruasUrl) {\n  const param = [];\n  const bobot = [];\n  for (let i = 0; i < ruasRute.length; i++) {\n    const r = ruasRute[i];\n    const sisa = /^\\[\\.\\.\\.(\\w+)\\]$/.exec(r);\n    if (sisa) {\n      if (i !== ruasRute.length - 1 || i >= ruasUrl.length) return null;\n      param.push(`${sisa[1]}=${ruasUrl.slice(i).join('/')}`);\n      bobot.push(2);\n      return { param, bobot };\n    }\n    if (i >= ruasUrl.length) return null;\n    const dinamis = /^\\[(\\w+)\\]$/.exec(r);\n    if (dinamis) {\n      param.push(`${dinamis[1]}=${ruasUrl[i]}`);\n      bobot.push(1);\n    } else if (r === ruasUrl[i]) {\n      bobot.push(0);\n    } else {\n      return null;\n    }\n  }\n  if (ruasRute.length !== ruasUrl.length) return null;\n  return { param, bobot };\n}\n\nfunction lebihSpesifik(a, b) {\n  const n = Math.min(a.bobot.length, b.bobot.length);\n  for (let i = 0; i < n; i++) {\n    if (a.bobot[i] !== b.bobot[i]) return a.bobot[i] < b.bobot[i];\n  }\n  return a.jalur < b.jalur;\n}\n\nfor (const url of daftarUrl) {\n  const ruasUrl = url.split('?')[0].split('/').filter((r) => r !== '');\n  let terbaik = null;\n  for (const r of rute) {\n    const hasil = cocok(r.ruas, ruasUrl);\n    if (!hasil) continue;\n    const calon = { jalur: r.jalur, ...hasil };\n    if (!terbaik || lebihSpesifik(calon, terbaik)) terbaik = calon;\n  }\n  if (terbaik) {\n    const p = terbaik.param.length ? ` (${terbaik.param.join(', ')})` : '';\n    console.log(`${url} -> ${terbaik.jalur}${p}`);\n  } else if (tidakKetemu) {\n    console.log(`${url} -> 404, tampilkan ${tidakKetemu}`);\n  } else {\n    console.log(`${url} -> 404`);\n  }\n}\n",
        "stdin_list": [
            """app/_layout.tsx app/index.tsx app/(tabs)/_layout.tsx app/(tabs)/profil.tsx app/user/[id].tsx app/user/baru.tsx app/docs/[...slug].tsx app/+not-found.tsx
/
/profil
/user/42
/user/baru
/docs/kotlin/coroutine
/docs
/user/42/foto
/toko?promo=1
""",
            """app/index.tsx app/produk/index.tsx app/produk/[id].tsx app/(admin)/laporan.tsx
/produk
/produk/
/produk/7
/laporan
/admin/laporan
""",
        ],
    },
    {
        "title": "Latihan 11: Jembatan Plugin Native Tiruan",
        "difficulty": "Lanjut",
        "question": [
            "Capacitor mengubah setiap panggilan plugin jadi pesan bernomor yang",
            "dikirim ke sisi native, lalu menyelesaikan Promise saat balasan",
            "bernomor sama datang. Tulis jembatan tiruannya di Node.",
            "",
            "Input berisi satu panggilan per baris: Plugin.metode, boleh diikuti",
            "spasi dan argumen JSON. Tanpa argumen, pakai {}.",
            "",
            "Sisi web: untuk setiap baris, beri nomor mulai 1, ubah panggilan jadi",
            "teks JSON {id, plugin, metode, argumen}, masukkan ke antrean, cetak",
            "kirim #id Plugin.metode argumen, lalu kembalikan sebuah Promise.",
            "",
            "Sisi native tiruan: sesudah semua panggilan dikirim, proses antrean",
            "berurutan. Plugin yang tersedia:",
            "  Perangkat.info      {platform: android, model: Tiruan}",
            "  Kamera.ambilFoto    argumen kualitas (bawaan 90); di luar 1-100",
            "                      jadi galat \"kualitas harus 1 sampai 100\";",
            "                      hasil {jalur: foto_N.jpg, kualitas}",
            "  Simpan.set          simpan nilai untuk kunci, hasil {}",
            "  Simpan.get          hasil {nilai}, atau nilai null kalau kosong",
            "Plugin yang nggak ada jadi galat \"plugin X belum terpasang\", dan",
            "metode yang nggak ada jadi galat \"metode Y tidak ada di X\".",
            "Untuk setiap pesan, cetak native #id -> hasil (JSON) atau",
            "native #id -> galat: pesan, lalu kirim balasan JSON ke sisi web.",
            "",
            "Terakhir, cetak hasil setiap Promise sesuai urutan nomor:",
            "Promise #id Plugin.metode selesai: hasil, atau ... ditolak: pesan.",
            "",
            "Contoh input:",
            "  Perangkat.info",
            "  Simpan.set {\"kunci\": \"tema\", \"nilai\": \"gelap\"}",
            "  Simpan.get {\"kunci\": \"tema\"}",
            "  Kamera.ambilFoto {\"kualitas\": 80}",
            "  Getar.pola {\"ms\": 200}",
            "",
            "Keluaran yang diharapkan:",
            "kirim #1 Perangkat.info {}",
            "kirim #2 Simpan.set {\"kunci\":\"tema\",\"nilai\":\"gelap\"}",
            "kirim #3 Simpan.get {\"kunci\":\"tema\"}",
            "kirim #4 Kamera.ambilFoto {\"kualitas\":80}",
            "kirim #5 Getar.pola {\"ms\":200}",
            "native #1 -> {\"platform\":\"android\",\"model\":\"Tiruan\"}",
            "native #2 -> {}",
            "native #3 -> {\"nilai\":\"gelap\"}",
            "native #4 -> {\"jalur\":\"foto_1.jpg\",\"kualitas\":80}",
            "native #5 -> galat: plugin Getar belum terpasang",
            "Promise #1 Perangkat.info selesai: {\"platform\":\"android\",\"model\":\"Tiruan\"}",
            "Promise #2 Simpan.set selesai: {}",
            "Promise #3 Simpan.get selesai: {\"nilai\":\"gelap\"}",
            "Promise #4 Kamera.ambilFoto selesai: {\"jalur\":\"foto_1.jpg\",\"kualitas\":80}",
            "Promise #5 Getar.pola ditolak: plugin Getar belum terpasang",
        ],
        "hints": [
            "Simpan fungsi selesai dan gagal milik setiap Promise di sebuah Map berkunci nomor panggilan, supaya balasan dari sisi native bisa menemukan Promise yang tepat.",
            "Biarkan sisi web dan sisi native cuma bertukar teks JSON lewat sebuah array antrean, lalu proses antrean itu dengan while sesudah semua panggilan dikirim.",
            "Pakai Promise.allSettled untuk menunggu semua Promise, lalu cetak setiap hasil dengan memeriksa h.status === 'fulfilled' untuk membedakan selesai dan ditolak.",
        ],
        "solution": "const baris = require('fs').readFileSync(0, 'utf8').split('\\n')\n  .map((b) => b.trim()).filter((b) => b !== '');\n\n// Sisi native tiruan: plugin dan metodenya.\nconst simpanan = {};\nlet nomorFoto = 0;\nconst plugin = {\n  Perangkat: {\n    info: () => ({ platform: 'android', model: 'Tiruan' }),\n  },\n  Kamera: {\n    ambilFoto: (arg) => {\n      const kualitas = arg.kualitas === undefined ? 90 : arg.kualitas;\n      if (kualitas < 1 || kualitas > 100) throw new Error('kualitas harus 1 sampai 100');\n      nomorFoto += 1;\n      return { jalur: `foto_${nomorFoto}.jpg`, kualitas };\n    },\n  },\n  Simpan: {\n    set: (arg) => {\n      simpanan[arg.kunci] = arg.nilai;\n      return {};\n    },\n    get: (arg) => ({ nilai: arg.kunci in simpanan ? simpanan[arg.kunci] : null }),\n  },\n};\n\nconst antrean = [];\nconst menunggu = new Map();\n\nfunction terimaDiWeb(teks) {\n  const balasan = JSON.parse(teks);\n  const { selesai, gagal } = menunggu.get(balasan.id);\n  menunggu.delete(balasan.id);\n  if ('galat' in balasan) gagal(new Error(balasan.galat));\n  else selesai(balasan.hasil);\n}\n\nfunction prosesDiNative() {\n  while (antrean.length > 0) {\n    const pesan = JSON.parse(antrean.shift());\n    let balasan;\n    const p = plugin[pesan.plugin];\n    if (!p) {\n      balasan = { id: pesan.id, galat: `plugin ${pesan.plugin} belum terpasang` };\n    } else if (!p[pesan.metode]) {\n      balasan = { id: pesan.id, galat: `metode ${pesan.metode} tidak ada di ${pesan.plugin}` };\n    } else {\n      try {\n        balasan = { id: pesan.id, hasil: p[pesan.metode](pesan.argumen) };\n      } catch (e) {\n        balasan = { id: pesan.id, galat: e.message };\n      }\n    }\n    if ('galat' in balasan) console.log(`native #${balasan.id} -> galat: ${balasan.galat}`);\n    else console.log(`native #${balasan.id} -> ${JSON.stringify(balasan.hasil)}`);\n    terimaDiWeb(JSON.stringify(balasan));\n  }\n}\n\n// Sisi web: setiap panggilan jadi pesan JSON bernomor dan sebuah Promise.\nlet nomor = 0;\nfunction panggil(namaPlugin, metode, argumen) {\n  nomor += 1;\n  const id = nomor;\n  const teks = JSON.stringify({ id, plugin: namaPlugin, metode, argumen });\n  console.log(`kirim #${id} ${namaPlugin}.${metode} ${JSON.stringify(argumen)}`);\n  antrean.push(teks);\n  return new Promise((selesai, gagal) => menunggu.set(id, { selesai, gagal }));\n}\n\nconst janji = baris.map((b) => {\n  const spasi = b.indexOf(' ');\n  const nama = spasi === -1 ? b : b.slice(0, spasi);\n  const argumen = spasi === -1 ? {} : JSON.parse(b.slice(spasi + 1));\n  const [namaPlugin, metode] = nama.split('.');\n  return { nama, promise: panggil(namaPlugin, metode, argumen) };\n});\n\nprosesDiNative();\n\nPromise.allSettled(janji.map((j) => j.promise)).then((hasil) => {\n  hasil.forEach((h, i) => {\n    const awal = `Promise #${i + 1} ${janji[i].nama}`;\n    if (h.status === 'fulfilled') console.log(`${awal} selesai: ${JSON.stringify(h.value)}`);\n    else console.log(`${awal} ditolak: ${h.reason.message}`);\n  });\n});\n",
        "stdin_list": [
            """Perangkat.info
Simpan.set {"kunci": "tema", "nilai": "gelap"}
Simpan.get {"kunci": "tema"}
Kamera.ambilFoto {"kualitas": 80}
Getar.pola {"ms": 200}
""",
            """Simpan.get {"kunci": "token"}
Kamera.ambilFoto
Kamera.ambilFoto {"kualitas": 150}
Kamera.rekamVideo
Kamera.ambilFoto {"kualitas": 40}
""",
        ],
    },
    {
        "title": "Latihan 12: IPC Aman ala contextBridge",
        "difficulty": "Lanjut",
        "question": [
            "Buat versi mini arsitektur Electron di Node.js, tanpa Electron.",
            "",
            "Proses main tiruan memakai EventEmitter bawaan Node dan",
            "mendaftarkan empat handler: simpan_catatan, baca_catatan,",
            "daftar_catatan, dan hapus_semua. Preload tiruan cuma mengizinkan",
            "tiga kanal: baca_catatan, simpan_catatan, dan daftar_catatan.",
            "",
            "Tiap baris stdin adalah satu panggilan dari renderer: nama kanal",
            "lalu argumennya, dipisah spasi. Aturannya:",
            "  - Kanal di luar daftar izin: cetak",
            "    'ditolak: kanal X tidak diizinkan' tanpa menyentuh main.",
            "  - simpan_catatan judul isi...: kata-kata sesudah judul digabung",
            "    satu spasi jadi isi. Balasannya 'tersimpan: judul (N huruf)',",
            "    N = panjang isi.",
            "  - baca_catatan judul: balasannya isi catatan, atau galat",
            "    'catatan judul tidak ada'.",
            "  - daftar_catatan: judul-judul urut abjad dipisah ', ', atau",
            "    '(kosong)'.",
            "  - Main memeriksa judul: cuma boleh huruf kecil, angka, - dan _.",
            "    Selain itu galat 'judul tidak sah'.",
            "Balasan sukses dicetak 'kanal -> balasan', galat dicetak",
            "'kanal -> galat: pesan'.",
            "",
            "Contoh input:",
            "  simpan_catatan belanja beli telur dan gula",
            "  baca_catatan belanja",
            "  baca_catatan tugas",
            "  hapus_semua",
            "  simpan_catatan ../rahasia isi",
            "  fs.readFile /etc/passwd",
            "  simpan_catatan tugas kerjakan PR fisika",
            "  daftar_catatan",
            "",
            "Keluaran yang diharapkan:",
            "simpan_catatan -> tersimpan: belanja (19 huruf)",
            "baca_catatan -> beli telur dan gula",
            "baca_catatan -> galat: catatan tugas tidak ada",
            "ditolak: kanal hapus_semua tidak diizinkan",
            "simpan_catatan -> galat: judul tidak sah",
            "ditolak: kanal fs.readFile tidak diizinkan",
            "simpan_catatan -> tersimpan: tugas (18 huruf)",
            "daftar_catatan -> belanja, tugas",
        ],
        "hints": [
            "Pisahkan dua peran: main menyimpan handler dan data, sedangkan preload cuma memeriksa nama kanal sebelum meneruskan panggilan.",
            "Daftarkan handler dengan emitter.on(kanal, ...) lalu kirim permintaan dengan emitter.emit(kanal, argumen, balas), dan biarkan handler memanggil balas(galat, nilai).",
            "Bungkus pemanggilan fungsi handler dengan try/catch supaya error dari pemeriksaan judul jadi galat yang dicetak, bukan program yang berhenti.",
        ],
        "solution": "const { EventEmitter } = require('events');\n\n// Proses main tiruan. Catatan disimpan di memori, bukan di disk.\nconst catatan = new Map();\nconst ipcMain = new EventEmitter();\n\nfunction handle(kanal, fungsi) {\n  ipcMain.on(kanal, (args, balas) => {\n    try {\n      balas(null, fungsi(...args));\n    } catch (e) {\n      balas(e.message);\n    }\n  });\n}\n\nfunction cekJudul(judul) {\n  if (!/^[a-z0-9_-]+$/.test(judul || '')) throw new Error('judul tidak sah');\n}\n\nhandle('simpan_catatan', (judul, ...kata) => {\n  cekJudul(judul);\n  const isi = kata.join(' ');\n  catatan.set(judul, isi);\n  return `tersimpan: ${judul} (${isi.length} huruf)`;\n});\n\nhandle('baca_catatan', (judul) => {\n  cekJudul(judul);\n  if (!catatan.has(judul)) throw new Error(`catatan ${judul} tidak ada`);\n  return catatan.get(judul);\n});\n\nhandle('daftar_catatan', () => {\n  const semua = [...catatan.keys()].sort();\n  return semua.length ? semua.join(', ') : '(kosong)';\n});\n\n// Handler berbahaya ini ada di main, tapi sengaja tidak dibuka preload.\nhandle('hapus_semua', () => {\n  catatan.clear();\n  return 'semua catatan dihapus';\n});\n\n// Preload tiruan: cuma kanal di daftar ini yang boleh dipanggil renderer.\nconst IZIN = ['baca_catatan', 'simpan_catatan', 'daftar_catatan'];\n\nfunction invoke(kanal, args) {\n  if (!IZIN.includes(kanal)) return `ditolak: kanal ${kanal} tidak diizinkan`;\n  let hasil = 'galat: tidak ada handler';\n  ipcMain.emit(kanal, args, (galat, nilai) => {\n    hasil = galat ? `galat: ${galat}` : nilai;\n  });\n  return `${kanal} -> ${hasil}`;\n}\n\nconst baris = require('fs').readFileSync(0, 'utf8').split('\\n');\nfor (const b of baris) {\n  if (!b.trim()) continue;\n  const [kanal, ...args] = b.trim().split(/\\s+/);\n  console.log(invoke(kanal, args));\n}\n",
        "stdin_list": [
            """simpan_catatan belanja beli telur dan gula
baca_catatan belanja
baca_catatan tugas
hapus_semua
simpan_catatan ../rahasia isi
fs.readFile /etc/passwd
simpan_catatan tugas kerjakan PR fisika
daftar_catatan
""",
            """daftar_catatan
baca_catatan resep
simpan_catatan resep nasi goreng pedas
baca_catatan resep
hapus_semua
baca_catatan RESEP
""",
        ],
    },
    {
        "title": "Latihan 13: Tombol Immediate Mode ASCII",
        "difficulty": "Lanjut",
        "question": [
            "Buat GUI immediate mode mini yang menggambar ke grid teks",
            "selebar 26 kolom dan setinggi 3 baris.",
            "",
            "Tiap baris stdin adalah satu frame. Isinya posisi klik tiruan",
            "'x y' (kolom dan baris, mulai dari 0), atau '-' kalau frame itu",
            "nggak ada klik.",
            "",
            "Tiap frame, grid dikosongkan (diisi spasi) lalu fungsi ui()",
            "dijalankan dari atas:",
            "  if (tombol('Tambah', 0, 0)) hitung++;",
            "  if (hitung > 0 && tombol('Kurang', 9, 0)) hitung--;",
            "  if (tombol('Reset', 18, 0)) hitung = 0;",
            "  tulis(`Nilai: ${hitung}`, 0, 2);",
            "",
            "tombol(label, x, y) menulis '[label]' mulai kolom x di baris y,",
            "lalu mengembalikan true kalau klik frame itu jatuh di baris y dan",
            "di dalam kotak '[label]'. Variabel hitung mulai dari 0 dan",
            "bertahan antar frame. Tombol Kurang cuma ada di frame yang",
            "memanggilnya, jadi klik di posisinya saat hitung 0 nggak berbuat",
            "apa-apa.",
            "",
            "Untuk tiap frame, cetak 'frame N (klik ...)', lalu grid yang",
            "dibingkai: baris atas dan bawah '+' + 26 tanda '-' + '+', dan tiap",
            "baris grid diapit '|'.",
            "",
            "Contoh input:",
            "  11 0",
            "  3 0",
            "  3 0",
            "  12 0",
            "  20 0",
            "  -",
            "",
            "Keluaran yang diharapkan (dua frame pertama):",
            "frame 1 (klik 11 0)",
            "+--------------------------+",
            "|[Tambah]          [Reset] |",
            "|                          |",
            "|Nilai: 0                  |",
            "+--------------------------+",
            "frame 2 (klik 3 0)",
            "+--------------------------+",
            "|[Tambah] [Kurang] [Reset] |",
            "|                          |",
            "|Nilai: 1                  |",
            "+--------------------------+",
        ],
        "hints": [
            "Pisahkan state yang bertahan antar frame, yaitu hitung, dari hal yang dibuat ulang setiap frame, yaitu grid dan klik.",
            "Tombol cukup menulis teks ke grid lalu membandingkan koordinat klik dengan kotaknya, tanpa menyimpan objek tombol apa pun.",
            "Untuk tiap baris input, kosongkan grid, simpan kliknya, panggil ui(), lalu cetak grid berbingkai.",
        ],
        "solution": "const LEBAR = 26;\nconst TINGGI = 3;\n\nlet grid = [];\nlet klik = null;   // {x, y} atau null, berlaku satu frame\nlet hitung = 0;    // state milik aplikasi, bukan milik tombol\n\nfunction mulaiFrame(k) {\n  grid = Array.from({ length: TINGGI }, () => Array(LEBAR).fill(' '));\n  klik = k;\n}\n\nfunction tulis(teks, x, y) {\n  for (let i = 0; i < teks.length; i++) grid[y][x + i] = teks[i];\n}\n\nfunction tombol(label, x, y) {\n  const kotak = `[${label}]`;\n  tulis(kotak, x, y);\n  return klik !== null && klik.y === y && klik.x >= x && klik.x < x + kotak.length;\n}\n\nfunction ui() {\n  if (tombol('Tambah', 0, 0)) hitung++;\n  if (hitung > 0 && tombol('Kurang', 9, 0)) hitung--;\n  if (tombol('Reset', 18, 0)) hitung = 0;\n  tulis(`Nilai: ${hitung}`, 0, 2);\n}\n\nconst baris = require('fs').readFileSync(0, 'utf8').split('\\n')\n  .map((b) => b.trim()).filter((b) => b !== '');\n\nbaris.forEach((b, i) => {\n  const k = b === '-' ? null : { x: Number(b.split(' ')[0]), y: Number(b.split(' ')[1]) };\n  mulaiFrame(k);\n  ui();\n  console.log(`frame ${i + 1} (klik ${b})`);\n  console.log('+' + '-'.repeat(LEBAR) + '+');\n  for (const r of grid) console.log('|' + r.join('') + '|');\n  console.log('+' + '-'.repeat(LEBAR) + '+');\n});\n",
        "stdin_list": [
            """11 0
3 0
3 0
12 0
20 0
-
""",
            """2 0
5 2
9 0
9 0
""",
        ],
    },
    {
        "title": "Latihan 14: Evaluator Aturan Akses Dokumen",
        "difficulty": "Lanjut",
        "question": [
            "Buat evaluator aturan akses versi mini ala Firestore.",
            "",
            "Bagian pertama stdin berisi aturan, satu per baris:",
            "  aturan <koleksi> <baca|tulis>: <ekspresi>",
            "Lalu baris '---', lalu daftar permintaan, satu per baris:",
            "  <operasi> <koleksi>/<id> auth=<uid|null> [medan=nilai ...]",
            "Pasangan medan=nilai sesudah auth adalah isi dokumennya (data).",
            "",
            "Aturannya:",
            "  - Operasi baca memakai aturan baca. Operasi buat, ubah, dan",
            "    hapus memakai aturan tulis.",
            "  - Ekspresi berisi satu syarat atau beberapa syarat yang",
            "    disambung ' && '. Syaratnya true, false, atau 'kiri op kanan'",
            "    dengan op == atau !=. Operand-nya auth, auth.uid,",
            "    data.<medan>, null, atau teks berkutip tunggal seperti 'guru01'.",
            "  - Kalau nggak ada aturan untuk koleksi dan operasinya, tolak",
            "    dengan alasan [tidak ada aturan].",
            "  - Seperti Firestore, membaca auth.uid saat auth null atau membaca",
            "    medan data yang nggak ada adalah galat, dan galat berarti",
            "    tolak. Syarat dievaluasi dari kiri, dan begitu satu syarat",
            "    salah, sisanya nggak dievaluasi lagi.",
            "",
            "Cetak tiap permintaan dengan format:",
            "  <operasi> <jalur> (<uid atau tamu>): <hasil> [<koleksi> <jenis>:",
            "  <ekspresi>]",
            "Hasilnya izin, tolak, atau 'tolak (galat: auth null)' dan",
            "'tolak (galat: medan tidak ada)'.",
            "",
            "Contoh input:",
            "  aturan catatan baca: auth != null",
            "  aturan catatan tulis: auth != null && auth.uid == data.pemilik",
            "  aturan pengumuman baca: true",
            "  aturan pengumuman tulis: auth.uid == 'guru01'",
            "  ---",
            "  baca catatan/c1 auth=null",
            "  baca catatan/c1 auth=budi",
            "  buat catatan/c2 auth=budi pemilik=budi",
            "  ubah catatan/c2 auth=sari pemilik=budi",
            "  hapus catatan/c2 auth=null pemilik=budi",
            "  baca pengumuman/libur auth=null",
            "  ubah pengumuman/libur auth=budi",
            "  ubah pengumuman/libur auth=guru01",
            "  ubah pengumuman/libur auth=null",
            "  baca nilai/budi auth=budi",
            "",
            "Keluaran yang diharapkan:",
            "baca catatan/c1 (tamu): tolak [catatan baca: auth != null]",
            "baca catatan/c1 (budi): izin [catatan baca: auth != null]",
            "buat catatan/c2 (budi): izin [catatan tulis: auth != null && auth.uid == data.pemilik]",
            "ubah catatan/c2 (sari): tolak [catatan tulis: auth != null && auth.uid == data.pemilik]",
            "hapus catatan/c2 (tamu): tolak [catatan tulis: auth != null && auth.uid == data.pemilik]",
            "baca pengumuman/libur (tamu): izin [pengumuman baca: true]",
            "ubah pengumuman/libur (budi): tolak [pengumuman tulis: auth.uid == 'guru01']",
            "ubah pengumuman/libur (guru01): izin [pengumuman tulis: auth.uid == 'guru01']",
            "ubah pengumuman/libur (tamu): tolak (galat: auth null) [pengumuman tulis: auth.uid == 'guru01']",
            "baca nilai/budi (budi): tolak [tidak ada aturan]",
        ],
        "hints": [
            "Simpan aturan sebagai objek bersarang, misalnya aturan[koleksi][jenis], lalu ubah operasi buat, ubah, dan hapus jadi jenis tulis sebelum mencarinya.",
            "Buat fungsi kecil yang mengubah satu operand jadi nilai, dan lempar error untuk auth.uid saat auth null atau medan data yang nggak ada.",
            "Pecah ekspresi dengan '&&', evaluasi tiap syarat memakai every() supaya berhenti di syarat pertama yang salah, dan tangkap error-nya dengan try/catch untuk mencetak tolak (galat: ...).",
        ],
        "solution": "const teks = require('fs').readFileSync(0, 'utf8');\nconst [bagianAturan, bagianMinta] = teks.split(/^---$/m);\n\n// aturan[koleksi][jenis] = ekspresi\nconst aturan = {};\nfor (const b of bagianAturan.split('\\n')) {\n  const m = b.trim().match(/^aturan (\\S+) (baca|tulis): (.+)$/);\n  if (!m) continue;\n  aturan[m[1]] = aturan[m[1]] || {};\n  aturan[m[1]][m[2]] = m[3].trim();\n}\n\nfunction nilai(token, konteks) {\n  if (token === 'null') return null;\n  if (token === 'true') return true;\n  if (token === 'false') return false;\n  if (/^'.*'$/.test(token)) return token.slice(1, -1);\n  if (token === 'auth') return konteks.auth;\n  if (token === 'auth.uid') {\n    if (konteks.auth === null) throw new Error('auth null');\n    return konteks.auth.uid;\n  }\n  if (token.startsWith('data.')) {\n    const v = konteks.data[token.slice(5)];\n    if (v === undefined) throw new Error('medan tidak ada');\n    return v;\n  }\n  throw new Error(`token tidak dikenal: ${token}`);\n}\n\nfunction syarat(teksSyarat, konteks) {\n  const t = teksSyarat.trim().split(/\\s+/);\n  if (t.length === 1) return nilai(t[0], konteks) === true;\n  const [kiri, op, kanan] = t;\n  const a = nilai(kiri, konteks);\n  const b = nilai(kanan, konteks);\n  return op === '==' ? a === b : a !== b;\n}\n\n// Galat saat evaluasi (misalnya auth.uid padahal belum masuk) = tolak.\nfunction evaluasi(ekspresi, konteks) {\n  try {\n    return ekspresi.split('&&').every((s) => syarat(s, konteks)) ? 'izin' : 'tolak';\n  } catch (e) {\n    return `tolak (galat: ${e.message})`;\n  }\n}\n\nconst JENIS = { baca: 'baca', buat: 'tulis', ubah: 'tulis', hapus: 'tulis' };\n\nfor (const b of bagianMinta.split('\\n')) {\n  const kata = b.trim().split(/\\s+/);\n  if (kata[0] === '') continue;\n  const [operasi, jalur, ...pasangan] = kata;\n  const [koleksi] = jalur.split('/');\n  const konteks = { auth: null, data: {} };\n  for (const p of pasangan) {\n    const [k, v] = p.split('=');\n    if (k === 'auth') konteks.auth = v === 'null' ? null : { uid: v };\n    else konteks.data[k] = v;\n  }\n  const siapa = konteks.auth ? konteks.auth.uid : 'tamu';\n  const jenis = JENIS[operasi];\n  const ekspresi = aturan[koleksi] && aturan[koleksi][jenis];\n  if (ekspresi === undefined) {\n    console.log(`${operasi} ${jalur} (${siapa}): tolak [tidak ada aturan]`);\n    continue;\n  }\n  const hasil = evaluasi(ekspresi, konteks);\n  console.log(`${operasi} ${jalur} (${siapa}): ${hasil} [${koleksi} ${jenis}: ${ekspresi}]`);\n}\n",
        "stdin_list": [
            """aturan catatan baca: auth != null
aturan catatan tulis: auth != null && auth.uid == data.pemilik
aturan pengumuman baca: true
aturan pengumuman tulis: auth.uid == 'guru01'
---
baca catatan/c1 auth=null
baca catatan/c1 auth=budi
buat catatan/c2 auth=budi pemilik=budi
ubah catatan/c2 auth=sari pemilik=budi
hapus catatan/c2 auth=null pemilik=budi
baca pengumuman/libur auth=null
ubah pengumuman/libur auth=budi
ubah pengumuman/libur auth=guru01
ubah pengumuman/libur auth=null
baca nilai/budi auth=budi
""",
            """aturan profil baca: auth.uid == data.pemilik
aturan profil tulis: false
---
baca profil/p1 auth=rina pemilik=rina
baca profil/p1 auth=dodi pemilik=rina
baca profil/p2 auth=null
baca profil/p3 auth=rina
ubah profil/p1 auth=rina pemilik=rina
""",
        ],
    },
    {
        "title": "Latihan 15: Pipeline Lane Rilis Mini",
        "difficulty": "Lanjut",
        "question": [
            "Buat penjalan lane rilis versi mini ala Fastlane. Langkahnya",
            "tiruan: hasil tiap langkah sudah ditulis di input.",
            "",
            "Baris stdin bisa berbentuk:",
            "  lane <nama>: <langkah1> <langkah2> ...",
            "  selalu: <langkah> ...         langkah yang tetap dijalankan",
            "                                sesudah lane, berhasil atau gagal",
            "  hasil <langkah>: ok [keterangan]",
            "  hasil <langkah>: gagal [keterangan]",
            "  jalankan <nama lane>",
            "Langkah yang nggak punya baris hasil dianggap ok tanpa",
            "keterangan. Baris jalankan diproses berurutan sesudah semua baris",
            "dibaca.",
            "",
            "Untuk tiap lane yang dijalankan:",
            "  - Cetak '[nama] mulai (N langkah)'.",
            "  - Cetak tiap langkah '[nama] i/N langkah: ok' atau ': gagal',",
            "    ditambah ' (keterangan)' kalau ada.",
            "  - Begitu satu langkah gagal, langkah sesudahnya dicetak",
            "    '[nama] i/N langkah: dilewati'.",
            "  - Untuk tiap langkah selalu, cetak",
            "    '[nama] selalu langkah: \"nama berhasil\"' atau",
            "    '[nama] selalu langkah: \"nama gagal di langkah\"'.",
            "  - Tutup dengan '[nama] selesai: berhasil' atau 'selesai: gagal'.",
            "  - Lane yang nggak ada: cetak '[nama] lane tidak ada'.",
            "",
            "Contoh input:",
            "  lane beta: uji build_ipa unggah_testflight",
            "  lane rilis: uji build_aab tanda_tangan unggah_play",
            "  selalu: notifikasi",
            "  hasil uji: ok 42 tes lulus",
            "  hasil build_ipa: ok Catatan.ipa",
            "  hasil build_aab: ok app-release.aab",
            "  hasil tanda_tangan: gagal keystore tidak ditemukan",
            "  jalankan rilis",
            "  jalankan beta",
            "",
            "Keluaran yang diharapkan:",
            "[rilis] mulai (4 langkah)",
            "[rilis] 1/4 uji: ok (42 tes lulus)",
            "[rilis] 2/4 build_aab: ok (app-release.aab)",
            "[rilis] 3/4 tanda_tangan: gagal (keystore tidak ditemukan)",
            "[rilis] 4/4 unggah_play: dilewati",
            "[rilis] selalu notifikasi: \"rilis gagal di tanda_tangan\"",
            "[rilis] selesai: gagal",
            "[beta] mulai (3 langkah)",
            "[beta] 1/3 uji: ok (42 tes lulus)",
            "[beta] 2/3 build_ipa: ok (Catatan.ipa)",
            "[beta] 3/3 unggah_testflight: ok",
            "[beta] selalu notifikasi: \"beta berhasil\"",
            "[beta] selesai: berhasil",
        ],
        "hints": [
            "Baca semua baris dulu ke tiga tempat terpisah, yaitu daftar lane, hasil per langkah, dan antrean lane yang mau dijalankan, baru jalankan antreannya.",
            "Pakai satu variabel penanda langkah yang gagal: selama penanda itu masih kosong langkah dijalankan, sesudah terisi langkah dicetak dilewati.",
            "Cocokkan bentuk baris dengan regex seperti /^lane (\\S+): (.+)$/ dan /^hasil (\\S+): (ok|gagal)\\s*(.*)$/ supaya keterangan yang memuat spasi tetap utuh.",
        ],
        "solution": "const baris = require('fs').readFileSync(0, 'utf8').split('\\n')\n  .map((b) => b.trim()).filter((b) => b !== '');\n\nconst lane = {};\nconst hasil = {};\nlet selalu = [];\nconst antrean = [];\n\nfor (const b of baris) {\n  let m;\n  if ((m = b.match(/^lane (\\S+): (.+)$/))) {\n    lane[m[1]] = m[2].split(/\\s+/);\n  } else if ((m = b.match(/^selalu: (.+)$/))) {\n    selalu = m[1].split(/\\s+/);\n  } else if ((m = b.match(/^hasil (\\S+): (ok|gagal)\\s*(.*)$/))) {\n    hasil[m[1]] = { status: m[2], ket: m[3] };\n  } else if ((m = b.match(/^jalankan (\\S+)$/))) {\n    antrean.push(m[1]);\n  }\n}\n\nfunction jalankan(nama) {\n  const langkah = lane[nama];\n  if (!langkah) {\n    console.log(`[${nama}] lane tidak ada`);\n    return;\n  }\n  console.log(`[${nama}] mulai (${langkah.length} langkah)`);\n  let gagalDi = null;\n  langkah.forEach((l, i) => {\n    const posisi = `${i + 1}/${langkah.length}`;\n    if (gagalDi) {\n      console.log(`[${nama}] ${posisi} ${l}: dilewati`);\n      return;\n    }\n    const h = hasil[l] || { status: 'ok', ket: '' };\n    const ket = h.ket ? ` (${h.ket})` : '';\n    console.log(`[${nama}] ${posisi} ${l}: ${h.status}${ket}`);\n    if (h.status === 'gagal') gagalDi = l;\n  });\n  const ringkas = gagalDi ? `${nama} gagal di ${gagalDi}` : `${nama} berhasil`;\n  for (const s of selalu) {\n    console.log(`[${nama}] selalu ${s}: \"${ringkas}\"`);\n  }\n  console.log(`[${nama}] selesai: ${gagalDi ? 'gagal' : 'berhasil'}`);\n}\n\nantrean.forEach(jalankan);\n",
        "stdin_list": [
            """lane beta: uji build_ipa unggah_testflight
lane rilis: uji build_aab tanda_tangan unggah_play
selalu: notifikasi
hasil uji: ok 42 tes lulus
hasil build_ipa: ok Catatan.ipa
hasil build_aab: ok app-release.aab
hasil tanda_tangan: gagal keystore tidak ditemukan
jalankan rilis
jalankan beta
""",
            """lane internal: lint uji build unggah_play
selalu: notifikasi bersihkan
hasil lint: ok
hasil uji: gagal 2 tes merah
jalankan internal
jalankan produksi
""",
        ],
    },
    {
        "title": "Latihan 16: Validator Kesiapan Rilis Play Store",
        "difficulty": "Lanjut",
        "question": [
            "Buat pemeriksa kesiapan rilis Play Store. Input berupa baris",
            "kunci=nilai, urutannya bebas:",
            "  tanggal           tanggal rilis, YYYY-MM-DD, selalu tahun 2026",
            "  aplikasi          baru atau lama",
            "  format            aab atau apk",
            "  targetSdk         angka",
            "  versionCode       versionCode berkas yang mau diunggah",
            "  versionCode_lama  versionCode yang pernah diunggah, dipisah koma",
            "                    (boleh nggak ada)",
            "  akun              pribadi atau organisasi",
            "  akun_dibuat       tanggal akun dibuat, YYYY-MM-DD",
            "  jalur             internal, tertutup, terbuka, atau produksi",
            "  sudah_produksi    ya kalau aplikasi ini pernah rilis produksi",
            "  penguji           jumlah penguji uji tertutup",
            "  hari_uji          lama uji tertutup berturut-turut, dalam hari",
            "  perpanjangan      ya kalau perpanjangan target API disetujui",
            "",
            "Periksa empat aturan ini, berurutan:",
            "  1. Aplikasi baru wajib berformat aab. Pesannya:",
            "     format <format>: aplikasi baru wajib AAB",
            "  2. targetSdk minimal 36 kalau tanggal rilis 2026-08-31 atau",
            "     sesudahnya, dan minimal 35 kalau sebelumnya. Dengan",
            "     perpanjangan, batas 2026-08-31 mundur jadi 2026-11-01.",
            "     Pesannya: targetSdk <T> < <W> untuk rilis <tanggal>, ditambah",
            "     ' (berlaku sejak <batas>)' kalau W = 36.",
            "  3. versionCode harus lebih besar dari semua versionCode_lama.",
            "     Pesannya: versionCode <baru> harus lebih besar dari <tertinggi>",
            "  4. Rilis ke jalur produksi oleh akun pribadi yang dibuat sesudah",
            "     2023-11-13 dan belum pernah rilis produksi wajib lulus uji",
            "     tertutup. Laporkan kekurangannya masing-masing:",
            "     uji tertutup baru <n> penguji, butuh minimal 12",
            "     uji tertutup baru <n> hari berturut-turut, butuh 14",
            "",
            "Cetak 'periksa rilis <tanggal> ke jalur <jalur>', lalu tiap",
            "pelanggaran diawali '- ', lalu 'hasil: <n> pelanggaran' atau",
            "'hasil: siap rilis'. Tanggal selalu diambil dari input, jangan",
            "dari jam komputer.",
            "",
            "Contoh input:",
            "  tanggal=2026-09-15",
            "  aplikasi=baru",
            "  format=aab",
            "  targetSdk=35",
            "  versionCode=7",
            "  versionCode_lama=5,7,6",
            "  akun=pribadi",
            "  akun_dibuat=2026-07-01",
            "  jalur=produksi",
            "  sudah_produksi=tidak",
            "  penguji=10",
            "  hari_uji=14",
            "  perpanjangan=tidak",
            "",
            "Keluaran yang diharapkan:",
            "periksa rilis 2026-09-15 ke jalur produksi",
            "- targetSdk 35 < 36 untuk rilis 2026-09-15 (berlaku sejak 2026-08-31)",
            "- versionCode 7 harus lebih besar dari 7",
            "- uji tertutup baru 10 penguji, butuh minimal 12",
            "hasil: 3 pelanggaran",
        ],
        "hints": [
            "Simpan semua pasangan kunci=nilai ke satu objek, lalu periksa tiap aturan secara terpisah dan kumpulkan pesannya di sebuah array.",
            "Tanggal berformat YYYY-MM-DD bisa dibandingkan langsung sebagai teks, jadi '2026-09-15' >= '2026-08-31' sudah memberi jawaban yang benar tanpa objek Date.",
            "Tentukan batas tanggal dulu dari nilai perpanjangan, baru hitung target minimal 36 atau 35, dan untuk versionCode pakai Math.max atas daftar lama yang dipecah dengan split(',').",
        ],
        "solution": "const data = {};\nfor (const b of require('fs').readFileSync(0, 'utf8').split('\\n')) {\n  const i = b.indexOf('=');\n  if (i > 0) data[b.slice(0, i).trim()] = b.slice(i + 1).trim();\n}\n\nconst tanggal = data.tanggal;           // YYYY-MM-DD, bisa dibandingkan sebagai teks\nconst target = Number(data.targetSdk);\nconst kodeBaru = Number(data.versionCode);\nconst kodeLama = data.versionCode_lama ? data.versionCode_lama.split(',').map(Number) : [];\nconst pelanggaran = [];\n\n// 1. Aplikasi baru wajib Android App Bundle (AAB).\nif (data.aplikasi === 'baru' && data.format !== 'aab') {\n  pelanggaran.push(`format ${data.format}: aplikasi baru wajib AAB`);\n}\n\n// 2. Target API: 36 sejak 2026-08-31, perpanjangan sampai 2026-11-01.\nconst batas = data.perpanjangan === 'ya' ? '2026-11-01' : '2026-08-31';\nconst wajib = tanggal >= batas ? 36 : 35;\nif (target < wajib) {\n  pelanggaran.push(`targetSdk ${target} < ${wajib} untuk rilis ${tanggal}` +\n    (wajib === 36 ? ` (berlaku sejak ${batas})` : ''));\n}\n\n// 3. versionCode harus lebih besar dari semua yang pernah diunggah.\nconst tertinggi = kodeLama.length ? Math.max(...kodeLama) : 0;\nif (kodeBaru <= tertinggi) {\n  pelanggaran.push(`versionCode ${kodeBaru} harus lebih besar dari ${tertinggi}`);\n}\n\n// 4. Akun pribadi yang dibuat sesudah 2023-11-13: uji tertutup dulu.\nconst wajibUji = data.jalur === 'produksi' && data.akun === 'pribadi' &&\n  data.akun_dibuat > '2023-11-13' && data.sudah_produksi !== 'ya';\nif (wajibUji) {\n  const penguji = Number(data.penguji || 0);\n  const hari = Number(data.hari_uji || 0);\n  if (penguji < 12) pelanggaran.push(`uji tertutup baru ${penguji} penguji, butuh minimal 12`);\n  if (hari < 14) pelanggaran.push(`uji tertutup baru ${hari} hari berturut-turut, butuh 14`);\n}\n\nconsole.log(`periksa rilis ${data.tanggal} ke jalur ${data.jalur}`);\nfor (const p of pelanggaran) console.log(`- ${p}`);\nconsole.log(pelanggaran.length ? `hasil: ${pelanggaran.length} pelanggaran` : 'hasil: siap rilis');\n",
        "stdin_list": [
            """tanggal=2026-09-15
aplikasi=baru
format=aab
targetSdk=35
versionCode=7
versionCode_lama=5,7,6
akun=pribadi
akun_dibuat=2026-07-01
jalur=produksi
sudah_produksi=tidak
penguji=10
hari_uji=14
perpanjangan=tidak
""",
            """tanggal=2026-10-20
aplikasi=baru
format=aab
targetSdk=35
versionCode=8
versionCode_lama=5,7,6
akun=pribadi
akun_dibuat=2026-07-01
jalur=produksi
sudah_produksi=tidak
penguji=15
hari_uji=14
perpanjangan=ya
""",
            """tanggal=2026-11-02
aplikasi=lama
format=apk
targetSdk=35
versionCode=31
versionCode_lama=29,30
akun=organisasi
akun_dibuat=2025-02-10
jalur=produksi
sudah_produksi=ya
perpanjangan=ya
""",
            """tanggal=2026-09-01
aplikasi=baru
format=apk
targetSdk=36
versionCode=1
akun=pribadi
akun_dibuat=2026-08-20
jalur=internal
perpanjangan=tidak
""",
        ],
    },
    {
        "title": "Latihan 17: Sinkronisasi Catatan Offline-First",
        "difficulty": "Sulit",
        "proyek": True,
        "question": [
            "Proyek akhir: sinkronisasi catatan offline-first.",
            "",
            "Aplikasi catatan di HP menyimpan salinan lokal, jadi tetap bisa",
            "dipakai saat offline. Perubahan selama offline masuk antrean dan",
            "dikirim ke server begitu online lagi. Sementara itu, perangkat",
            "lain (laptop) bisa mengubah catatan yang sama langsung di server.",
            "Tugasmu menyimulasikan klien, server, dan penyelesaian",
            "konfliknya.",
            "",
            "Model datanya:",
            "  - Tiap catatan punya teks, nomor versi, dan id perangkat yang",
            "    terakhir menulisnya (oleh).",
            "  - Server dan klien mulai kosong, dan klien mulai dalam keadaan",
            "    online.",
            "  - Id klien bawaannya hp. Baris 'klien <id>' di awal input",
            "    menggantinya. Perangkat lain selalu bernama laptop.",
            "",
            "Perintah di stdin, satu per baris:",
            "  ubah <id> <teks...>          klien mengubah atau membuat catatan",
            "  server_ubah <id> <teks...>   laptop mengubah catatan di server",
            "  offline                      klien kehilangan sinyal",
            "  online                       klien tersambung lagi",
            "",
            "Aturannya:",
            "  1. ubah: versi baru = versi lokal catatan itu + 1 (versi lokal",
            "     0 kalau belum ada), dan dasar = versi lokal sebelum diubah.",
            "     Salinan lokal langsung diganti. Kalau online, mutasi langsung",
            "     dikirim lalu klien menarik isi server. Kalau offline, mutasi",
            "     masuk antrean dengan nomor #1, #2, dan seterusnya.",
            "  2. server_ubah: versi = versi server + 1 (1 kalau belum ada),",
            "     oleh laptop. Kalau klien online, klien langsung menarik isi",
            "     server.",
            "  3. online: kirim isi antrean berurutan, lalu tarik seluruh isi",
            "     server ke klien.",
            "  4. Mengirim mutasi: kalau catatan belum ada di server, atau",
            "     versi server sama dengan dasar mutasi, mutasi diterima.",
            "     Selain itu terjadi konflik, dan pemenangnya ditentukan",
            "     last-writer-wins: versi lebih tinggi menang, dan kalau",
            "     versinya sama, id perangkat yang lebih awal menurut abjad",
            "     menang. Mutasi yang menang ditulis ke server, yang kalah",
            "     dibuang.",
            "",
            "Format log:",
            "  <klien>: ubah <id> \"<teks>\" v<versi>, <hasil kirim>",
            "  <klien> (offline): ubah <id> \"<teks>\" v<versi>, antre #<n>",
            "  laptop: ubah <id> \"<teks>\" v<versi> di server",
            "    (ditambah ', <klien> ikut menerima' kalau klien online)",
            "  <klien> offline",
            "  <klien> online, kirim <n> mutasi",
            "    #<n> <id> v<versi>: <hasil kirim>",
            "    tarik <jumlah catatan di server> catatan dari server",
            "Hasil kirim: diterima, atau 'konflik dengan <oleh> v<versi",
            "server>, diterima' atau '..., ditolak'.",
            "",
            "Di akhir, cetak 'konflik:' lalu satu baris per konflik:",
            "  <id>: <klien> v<a> vs <oleh> v<b> -> <pemenang> menang (<alasan>)",
            "dengan alasan 'versi lebih tinggi' atau 'seri, abjad', atau cetak",
            "'konflik: tidak ada'. Lalu cetak 'isi akhir klien:' dan 'isi akhir",
            "server:', masing-masing dengan baris '  <id> v<versi> <oleh>:",
            "<teks>' urut id. Terakhir cetak 'sama: ya' kalau isi klien dan",
            "server persis sama.",
            "",
            "Contoh input:",
            "  ubah c1 beli susu",
            "  server_ubah c2 rapat kelas jam 9",
            "  offline",
            "  ubah c1 beli susu dan roti",
            "  server_ubah c1 beli kopi",
            "  ubah c3 telepon ibu",
            "  server_ubah c2 rapat kelas jam 10",
            "  online",
            "",
            "Keluaran yang diharapkan:",
            "hp: ubah c1 \"beli susu\" v1, diterima",
            "laptop: ubah c2 \"rapat kelas jam 9\" v1 di server, hp ikut menerima",
            "hp offline",
            "hp (offline): ubah c1 \"beli susu dan roti\" v2, antre #1",
            "laptop: ubah c1 \"beli kopi\" v2 di server",
            "hp (offline): ubah c3 \"telepon ibu\" v1, antre #2",
            "laptop: ubah c2 \"rapat kelas jam 10\" v2 di server",
            "hp online, kirim 2 mutasi",
            "  #1 c1 v2: konflik dengan laptop v2, diterima",
            "  #2 c3 v1: diterima",
            "  tarik 3 catatan dari server",
            "konflik:",
            "  c1: hp v2 vs laptop v2 -> hp menang (seri, abjad)",
            "isi akhir klien:",
            "  c1 v2 hp: beli susu dan roti",
            "  c2 v2 laptop: rapat kelas jam 10",
            "  c3 v1 hp: telepon ibu",
            "isi akhir server:",
            "  c1 v2 hp: beli susu dan roti",
            "  c2 v2 laptop: rapat kelas jam 10",
            "  c3 v1 hp: telepon ibu",
            "sama: ya",
        ],
        "hints": [
            "Simpan server dan klien sebagai dua Map terpisah berisi teks, versi, dan oleh, ditambah satu array antrean untuk mutasi yang dibuat saat offline.",
            "Setiap mutasi perlu membawa dua angka, yaitu versi barunya dan versi dasar tempat ia dibuat, karena konflik dikenali dari versi server yang sudah bergeser dari dasar itu.",
            "Tulis satu fungsi kirim(mutasi) yang dipakai saat online maupun saat antrean dikosongkan, dan satu fungsi tarik() yang menyalin seluruh isi server ke klien sesudahnya.",
        ],
        "solution": "const baris = require('fs').readFileSync(0, 'utf8').split('\\n')\n  .map((b) => b.trim()).filter((b) => b !== '');\n\nconst LAIN = 'laptop';           // perangkat lain yang mengubah langsung di server\nlet klienId = 'hp';\nconst server = new Map();         // id -> {teks, versi, oleh}\nconst klien = new Map();          // salinan lokal di perangkat ini\nconst antrean = [];               // mutasi yang menunggu dikirim\nconst konflik = [];\nlet online = true;\nlet nomorAntre = 0;\n\nfunction salin(c) {\n  return { teks: c.teks, versi: c.versi, oleh: c.oleh };\n}\n\nfunction tarik() {\n  for (const [id, c] of server) klien.set(id, salin(c));\n}\n\n// Last-writer-wins: versi lebih tinggi menang; kalau seri, id klien yang\n// lebih awal menurut abjad menang. Hasilnya teks untuk log.\nfunction kirim(m) {\n  const s = server.get(m.id);\n  let terima = true;\n  let ket = 'diterima';\n  if (s && s.versi !== m.dasar) {\n    let menang;\n    let alasan = 'versi lebih tinggi';\n    if (m.versi > s.versi) menang = klienId;\n    else if (m.versi < s.versi) menang = s.oleh;\n    else {\n      menang = klienId < s.oleh ? klienId : s.oleh;\n      alasan = 'seri, abjad';\n    }\n    terima = menang === klienId;\n    ket = `konflik dengan ${s.oleh} v${s.versi}, ${terima ? 'diterima' : 'ditolak'}`;\n    konflik.push(`${m.id}: ${klienId} v${m.versi} vs ${s.oleh} v${s.versi} -> ` +\n      `${menang} menang (${alasan})`);\n  }\n  if (terima) server.set(m.id, { teks: m.teks, versi: m.versi, oleh: klienId });\n  return ket;\n}\n\nfor (const b of baris) {\n  const [perintah, id, ...kata] = b.split(/\\s+/);\n  const teks = kata.join(' ');\n  if (perintah === 'klien') {\n    klienId = id;\n  } else if (perintah === 'offline') {\n    online = false;\n    console.log(`${klienId} offline`);\n  } else if (perintah === 'online') {\n    online = true;\n    console.log(`${klienId} online, kirim ${antrean.length} mutasi`);\n    for (const m of antrean.splice(0)) {\n      console.log(`  #${m.no} ${m.id} v${m.versi}: ${kirim(m)}`);\n    }\n    tarik();\n    console.log(`  tarik ${server.size} catatan dari server`);\n  } else if (perintah === 'ubah') {\n    const lama = klien.get(id);\n    const dasar = lama ? lama.versi : 0;\n    const m = { id, teks, versi: dasar + 1, dasar };\n    klien.set(id, { teks, versi: m.versi, oleh: klienId });\n    if (online) {\n      console.log(`${klienId}: ubah ${id} \"${teks}\" v${m.versi}, ${kirim(m)}`);\n      tarik();\n    } else {\n      m.no = ++nomorAntre;\n      antrean.push(m);\n      console.log(`${klienId} (offline): ubah ${id} \"${teks}\" v${m.versi}, antre #${m.no}`);\n    }\n  } else if (perintah === 'server_ubah') {\n    const s = server.get(id);\n    const versi = (s ? s.versi : 0) + 1;\n    server.set(id, { teks, versi, oleh: LAIN });\n    console.log(`${LAIN}: ubah ${id} \"${teks}\" v${versi} di server` +\n      (online ? `, ${klienId} ikut menerima` : ''));\n    if (online) tarik();\n  }\n}\n\nfunction cetak(judul, peta) {\n  console.log(judul);\n  for (const id of [...peta.keys()].sort()) {\n    const c = peta.get(id);\n    console.log(`  ${id} v${c.versi} ${c.oleh}: ${c.teks}`);\n  }\n}\n\nconsole.log(konflik.length ? 'konflik:' : 'konflik: tidak ada');\nfor (const k of konflik) console.log(`  ${k}`);\ncetak('isi akhir klien:', klien);\ncetak('isi akhir server:', server);\nconst sama = JSON.stringify([...klien].sort()) === JSON.stringify([...server].sort());\nconsole.log(`sama: ${sama ? 'ya' : 'tidak'}`);\n",
        "stdin_list": [
            """ubah c1 beli susu
server_ubah c2 rapat kelas jam 9
offline
ubah c1 beli susu dan roti
server_ubah c1 beli kopi
ubah c3 telepon ibu
server_ubah c2 rapat kelas jam 10
online
""",
            """klien tablet
ubah c1 bawa buku paket
ubah c3 kerja kelompok
offline
ubah c1 bawa buku paket fisika
server_ubah c1 bawa buku tulis
server_ubah c1 bawa buku tulis dan pensil
ubah c2 setor tugas
ubah c3 kerja kelompok sabtu
server_ubah c3 kerja kelompok minggu
online
ubah c2 setor tugas sebelum jumat
""",
        ],
    },
]
