"""Kurikulum Game & Grafis.

Dirakit alat/rakit_kurikulum.py dari draf per bab (2026-10-19).
Sesudah dirakit, berkas ini disunting seperti kurikulum lain
(alat/ganti_badan.py, alat/tambah_bagian.py). <KEY>_BAB tetap
spesifikasi JUMLAH; rentangnya dihitung data/kurikulum_tech.py.
"""

GAME_EXERCISES = [
    {
        "title": "Latihan 1: Game Loop dengan Jam Palsu",
        "difficulty": "Mudah",
        "question": [
            "Kamu menulis game loop dengan fixed timestep. Lama tiap frame",
            "nggak dibaca dari jam sungguhan, tapi dari stdin: satu baris berisi",
            "durasi frame dalam milidetik, dipisah spasi.",
            "",
            "Aturannya:",
            "  - Satu langkah fisika = 20 ms.",
            "  - Tiap langkah, objek maju 5 piksel. Posisi awalnya x = 0.",
            "  - Durasi frame dimasukkan ke akumulator. Selama akumulator >= 20,",
            "    jalankan satu langkah dan kurangi akumulator dengan 20.",
            "  - Sisa akumulator disimpan untuk frame berikutnya.",
            "",
            "Untuk tiap frame, cetak nomor frame (mulai dari 1), durasinya,",
            "jumlah langkah di frame itu, sisa akumulator, dan posisi x. Di",
            "akhir, cetak total langkah dan posisi akhir.",
            "",
            "Contoh input:",
            "  16 16 33 8 50",
            "",
            "Keluaran yang diharapkan:",
            "frame 1: 16 ms -> 0 langkah, sisa 16 ms, x = 0",
            "frame 2: 16 ms -> 1 langkah, sisa 12 ms, x = 5",
            "frame 3: 33 ms -> 2 langkah, sisa 5 ms, x = 15",
            "frame 4: 8 ms -> 0 langkah, sisa 13 ms, x = 15",
            "frame 5: 50 ms -> 3 langkah, sisa 3 ms, x = 30",
            "total: 6 langkah, x = 30",
            "",
            "Untuk input 40 5 5 5 70 19, keluarannya:",
            "frame 1: 40 ms -> 2 langkah, sisa 0 ms, x = 10",
            "frame 2: 5 ms -> 0 langkah, sisa 5 ms, x = 10",
            "frame 3: 5 ms -> 0 langkah, sisa 10 ms, x = 10",
            "frame 4: 5 ms -> 0 langkah, sisa 15 ms, x = 10",
            "frame 5: 70 ms -> 4 langkah, sisa 5 ms, x = 30",
            "frame 6: 19 ms -> 1 langkah, sisa 4 ms, x = 35",
            "total: 7 langkah, x = 35",
        ],
        "hints": [
            "Akumulator itu celengan waktu: tiap frame durasinya dimasukkan, dan tiap langkah fisika mengambil 20 ms darinya.",
            "Pakai while, bukan if, karena satu frame panjang seperti 50 ms bisa berisi lebih dari satu langkah.",
            "Baca input dengan require('fs').readFileSync(0, 'utf8'), pecah dengan split(/\\s+/), buang string kosong, lalu ubah tiap bagian dengan Number.",
        ],
        "solution": "const data = require('fs').readFileSync(0, 'utf8');\nconst durasi = data.split(/\\s+/).filter((s) => s !== '').map(Number);\n\nconst LANGKAH = 20;\nconst KECEPATAN = 5;\nlet akumulator = 0;\nlet x = 0;\nlet total = 0;\n\ndurasi.forEach((d, i) => {\n  akumulator += d;\n  let langkah = 0;\n  while (akumulator >= LANGKAH) {\n    akumulator -= LANGKAH;\n    x += KECEPATAN;\n    langkah++;\n  }\n  total += langkah;\n  console.log(`frame ${i + 1}: ${d} ms -> ${langkah} langkah, sisa ${akumulator} ms, x = ${x}`);\n});\nconsole.log(`total: ${total} langkah, x = ${x}`);\n",
        "stdin_list": [
            """16 16 33 8 50
""",
            """40 5 5 5 70 19
""",
        ],
    },
    {
        "title": "Latihan 2: Pustaka Vektor Mini",
        "difficulty": "Mudah",
        "question": [
            "Tulis lima fungsi vektor 2D. Vektor ditulis sebagai objek",
            "{ x, y }. Nama fungsinya dipakai lagi di latihan-latihan",
            "berikutnya, jadi pakai nama ini persis:",
            "  - tambah(a, b): vektor a + b",
            "  - kali(v, s): vektor v dikali angka s",
            "  - panjang(v): panjang vektor v",
            "  - normal(v): vektor satuan searah v; untuk (0, 0) hasilnya (0, 0)",
            "  - dot(a, b): a.x * b.x + a.y * b.y",
            "",
            "Input dari stdin, satu perintah per baris:",
            "  tambah ax ay bx by",
            "  kali vx vy s",
            "  panjang vx vy",
            "  normal vx vy",
            "  dot ax ay bx by",
            "",
            "Cetak nama perintah, titik dua, lalu hasilnya. Vektor ditulis",
            "(x, y) dan semua angka memakai toFixed(2). Perintah lain dijawab",
            "dengan \"perintah tidak dikenal: <nama>\". Baris kosong dilewati.",
            "",
            "Contoh input:",
            "  tambah 1 2 3 4",
            "  kali 3 -4 0.5",
            "  panjang 3 4",
            "  normal 3 4",
            "  dot 1 2 3 4",
            "  normal 0 0",
            "",
            "Keluaran yang diharapkan:",
            "tambah: (4.00, 6.00)",
            "kali: (1.50, -2.00)",
            "panjang: 5.00",
            "normal: (0.60, 0.80)",
            "dot: 11.00",
            "normal: (0.00, 0.00)",
        ],
        "hints": [
            "Fungsi yang menghasilkan vektor mengembalikan objek baru { x, y }, sedangkan panjang dan dot mengembalikan satu angka.",
            "Normalisasi berarti membagi x dan y dengan panjang vektor, jadi periksa dulu apakah panjangnya 0.",
            "Pecah tiap baris dengan trim().split(/\\s+/), ambil kata pertama sebagai perintah, dan ubah sisanya dengan Number.",
        ],
        "solution": "const tambah = (a, b) => ({ x: a.x + b.x, y: a.y + b.y });\nconst kali = (v, s) => ({ x: v.x * s, y: v.y * s });\nconst panjang = (v) => Math.hypot(v.x, v.y);\nconst normal = (v) => {\n  const p = panjang(v);\n  return p === 0 ? { x: 0, y: 0 } : { x: v.x / p, y: v.y / p };\n};\nconst dot = (a, b) => a.x * b.x + a.y * b.y;\n\nconst vek = (v) => `(${v.x.toFixed(2)}, ${v.y.toFixed(2)})`;\nconst baris = require('fs').readFileSync(0, 'utf8').split('\\n');\n\nfor (const b of baris) {\n  const [perintah, ...sisa] = b.trim().split(/\\s+/);\n  if (!perintah) continue;\n  const n = sisa.map(Number);\n  const a = { x: n[0], y: n[1] };\n  const c = { x: n[2], y: n[3] };\n  if (perintah === 'tambah') console.log(`tambah: ${vek(tambah(a, c))}`);\n  else if (perintah === 'kali') console.log(`kali: ${vek(kali(a, n[2]))}`);\n  else if (perintah === 'panjang') console.log(`panjang: ${panjang(a).toFixed(2)}`);\n  else if (perintah === 'normal') console.log(`normal: ${vek(normal(a))}`);\n  else if (perintah === 'dot') console.log(`dot: ${dot(a, c).toFixed(2)}`);\n  else console.log(`perintah tidak dikenal: ${perintah}`);\n}\n",
        "stdin_list": [
            """tambah 1 2 3 4
kali 3 -4 0.5
panjang 3 4
normal 3 4
dot 1 2 3 4
normal 0 0
""",
            """panjang 1 1
normal 0 -5
dot 1 0 0 1

tambah -1.5 2 0.25 -3
lompat 1 2
kali 1 1 1.4142
""",
        ],
    },
    {
        "title": "Latihan 3: Detektor Tabrakan AABB",
        "difficulty": "Menengah",
        "question": [
            "Input dari stdin berisi daftar kotak, satu per baris:",
            "  nama x y w h",
            "Semua angka bilangan bulat. (x, y) adalah pojok kiri atas, w",
            "lebar, h tinggi, dan sumbu y mengarah ke bawah. Kotak menempati x",
            "sampai x + w dan y sampai y + h. Nama berhuruf kecil semua.",
            "",
            "Aturan yang dipakai lagi di proyek akhir:",
            "  - Tumpang tindih di sumbu x:",
            "      tx = min(a.x + a.w, b.x + b.w) - max(a.x, b.x)",
            "    Sumbu y dihitung dengan cara yang sama (ty).",
            "  - Dua kotak bertabrakan kalau tx > 0 dan ty > 0. Kotak yang cuma",
            "    bersentuhan tepi nggak bertabrakan.",
            "  - Vektor dorong minimum menggeser A keluar dari B lewat sumbu",
            "    yang tumpang tindihnya lebih kecil. Kalau tx sama dengan ty,",
            "    pakai sumbu x. Kalau pusat A lebih kecil dari pusat B di sumbu",
            "    itu, A didorong ke arah negatif; selain itu ke arah positif.",
            "    Komponen sumbu yang lain bernilai 0.",
            "",
            "Urutkan kotak menurut nama (abjad), lalu periksa setiap pasangan",
            "dengan A = kotak yang namanya lebih dulu. Untuk tiap pasangan yang",
            "bertabrakan, cetak:",
            "  A & B: tumpang x=tx y=ty, dorong A (dx, dy)",
            "Di akhir cetak \"jumlah tabrakan: N\", atau \"tidak ada tabrakan\"",
            "kalau N = 0.",
            "",
            "Contoh input:",
            "  pemain 10 10 20 30",
            "  peti 25 30 20 20",
            "  roket 60 0 8 8",
            "  tong 40 47 10 10",
            "  kardus 28 0 10 12",
            "  bendera 68 0 5 5",
            "",
            "Keluaran yang diharapkan:",
            "kardus & pemain: tumpang x=2 y=2, dorong kardus (2, 0)",
            "pemain & peti: tumpang x=5 y=10, dorong pemain (-5, 0)",
            "peti & tong: tumpang x=5 y=3, dorong peti (0, -3)",
            "jumlah tabrakan: 3",
            "",
            "Bendera dan roket cuma bersentuhan di x = 68, jadi nggak tercetak.",
        ],
        "hints": [
            "Pakai dua perulangan bersarang, i dari 0 dan j dari i + 1, supaya setiap pasangan diperiksa tepat sekali setelah kotak diurutkan.",
            "Bandingkan pusat dengan x + w / 2 dan y + h / 2, dan pilih sumbu x kalau tx <= ty.",
            "Urutkan dengan sort((a, b) => (a.nama < b.nama ? -1 : a.nama > b.nama ? 1 : 0)) supaya hasilnya sama di semua mesin.",
        ],
        "solution": "const kotak = require('fs').readFileSync(0, 'utf8')\n  .split('\\n')\n  .map((b) => b.trim())\n  .filter((b) => b !== '')\n  .map((b) => {\n    const [nama, x, y, w, h] = b.split(/\\s+/);\n    return { nama, x: Number(x), y: Number(y), w: Number(w), h: Number(h) };\n  })\n  .sort((a, b) => (a.nama < b.nama ? -1 : a.nama > b.nama ? 1 : 0));\n\nfunction tumpang(a, b) {\n  return {\n    x: Math.min(a.x + a.w, b.x + b.w) - Math.max(a.x, b.x),\n    y: Math.min(a.y + a.h, b.y + b.h) - Math.max(a.y, b.y),\n  };\n}\n\nlet jumlah = 0;\nfor (let i = 0; i < kotak.length; i++) {\n  for (let j = i + 1; j < kotak.length; j++) {\n    const a = kotak[i];\n    const b = kotak[j];\n    const t = tumpang(a, b);\n    if (t.x <= 0 || t.y <= 0) continue;\n    let dx = 0;\n    let dy = 0;\n    if (t.x <= t.y) {\n      dx = a.x + a.w / 2 < b.x + b.w / 2 ? -t.x : t.x;\n    } else {\n      dy = a.y + a.h / 2 < b.y + b.h / 2 ? -t.y : t.y;\n    }\n    jumlah++;\n    console.log(`${a.nama} & ${b.nama}: tumpang x=${t.x} y=${t.y}, dorong ${a.nama} (${dx}, ${dy})`);\n  }\n}\nconsole.log(jumlah === 0 ? 'tidak ada tabrakan' : `jumlah tabrakan: ${jumlah}`);\n",
        "stdin_list": [
            """pemain 10 10 20 30
peti 25 30 20 20
roket 60 0 8 8
tong 40 47 10 10
kardus 28 0 10 12
bendera 68 0 5 5
""",
            """d 0 0 10 10
c 0 0 10 10
a 0 5 10 10
""",
            """satu 0 0 5 5
dua 5 0 5 5
tiga 0 5 5 5
""",
        ],
    },
    {
        "title": "Latihan 4: State Machine Karakter Platformer",
        "difficulty": "Menengah",
        "question": [
            "Karakter platformer punya empat state: diam, lari, lompat, dan",
            "jatuh. Karakter mulai di state diam. Tiap baris stdin adalah satu",
            "frame, berisi input dan apakah karakter menyentuh tanah:",
            "  <input> <tanah>",
            "Input salah satu dari kanan, lompat, atau kosong. Tanah bernilai",
            "ya atau tidak.",
            "",
            "Tabel transisi (diperiksa dari atas ke bawah, satu transisi per",
            "frame):",
            "  - Dari diam atau lari:",
            "      tanah tidak            -> jatuh",
            "      input lompat           -> lompat",
            "      input kanan            -> lari",
            "      input kosong           -> diam",
            "  - Dari lompat: lompat berlangsung tiga frame, dihitung dari frame",
            "    tombol ditekan. Di frame keempat state jadi jatuh. Tanah",
            "    diabaikan selama lompat.",
            "  - Dari jatuh: kalau tanah ya, mendarat ke lari (input kanan)",
            "    atau diam (input lain). Kalau tanah tidak, tetap jatuh.",
            "",
            "Input lompat di state lompat atau jatuh, atau di frame saat",
            "karakter kehilangan tanah, nggak sah. Abaikan dan beri catatan",
            "\"(lompat diabaikan)\" di belakang state frame itu.",
            "",
            "Cetak \"frame N: state\" untuk tiap frame (N mulai 1). Di akhir,",
            "cetak jumlah lompatan yang benar-benar terjadi dan jumlah input",
            "lompat yang diabaikan.",
            "",
            "Contoh input:",
            "  kosong ya",
            "  kanan ya",
            "  kanan ya",
            "  lompat ya",
            "  kanan tidak",
            "  lompat tidak",
            "  kosong tidak",
            "  kanan tidak",
            "  kanan ya",
            "  kosong ya",
            "  kosong tidak",
            "  lompat ya",
            "",
            "Keluaran yang diharapkan:",
            "frame 1: diam",
            "frame 2: lari",
            "frame 3: lari",
            "frame 4: lompat",
            "frame 5: lompat",
            "frame 6: lompat (lompat diabaikan)",
            "frame 7: jatuh",
            "frame 8: jatuh",
            "frame 9: lari",
            "frame 10: diam",
            "frame 11: jatuh",
            "frame 12: diam (lompat diabaikan)",
            "lompatan: 1, diabaikan: 2",
            "",
            "Frame 11 jatuh karena karakter berjalan keluar dari tepi pijakan.",
            "Di frame 12 karakter mendarat, dan tombol lompatnya diabaikan",
            "karena datang saat state masih jatuh.",
        ],
        "hints": [
            "Simpan state sekarang di satu variabel, dan untuk state lompat simpan juga sisa frame yang diisi 3 saat lompatan dimulai.",
            "Di state lompat, kurangi sisa frame dulu, lalu pindah ke jatuh kalau sisanya sudah 0.",
            "Tulis satu fungsi kecil yang menandai \"(lompat diabaikan)\" dan menambah penghitung kalau input frame itu lompat, lalu panggil fungsi itu di setiap tempat lompat nggak sah.",
        ],
        "solution": "const baris = require('fs').readFileSync(0, 'utf8').split('\\n')\n  .map((b) => b.trim())\n  .filter((b) => b !== '');\n\nlet state = 'diam';\nlet sisa = 0;\nlet lompatan = 0;\nlet diabaikan = 0;\n\nbaris.forEach((b, i) => {\n  const [input, tanah] = b.split(/\\s+/);\n  const diTanah = tanah === 'ya';\n  let catatan = '';\n  const tolak = () => {\n    if (input === 'lompat') {\n      catatan = ' (lompat diabaikan)';\n      diabaikan++;\n    }\n  };\n\n  if (state === 'diam' || state === 'lari') {\n    if (!diTanah) {\n      tolak();\n      state = 'jatuh';\n    } else if (input === 'lompat') {\n      state = 'lompat';\n      sisa = 3;\n      lompatan++;\n    } else {\n      state = input === 'kanan' ? 'lari' : 'diam';\n    }\n  } else if (state === 'lompat') {\n    tolak();\n    sisa--;\n    if (sisa === 0) state = 'jatuh';\n  } else if (state === 'jatuh') {\n    tolak();\n    if (diTanah) state = input === 'kanan' ? 'lari' : 'diam';\n  }\n  console.log(`frame ${i + 1}: ${state}${catatan}`);\n});\nconsole.log(`lompatan: ${lompatan}, diabaikan: ${diabaikan}`);\n",
        "stdin_list": [
            """kosong ya
kanan ya
kanan ya
lompat ya
kanan tidak
lompat tidak
kosong tidak
kanan tidak
kanan ya
kosong ya
kosong tidak
lompat ya
""",
            """lompat ya
lompat tidak
kosong tidak
kosong tidak
kosong ya
lompat ya
kanan tidak
""",
            """kanan ya
lompat tidak
kanan ya
kanan ya
""",
        ],
    },
    {
        "title": "Latihan 5: Pohon Node dan Sinyal Mini",
        "difficulty": "Menengah",
        "question": [
            "Bikin tiruan kecil pohon node dan sinyal Godot. Awalnya pohon",
            "cuma berisi satu node bernama root. Tiap baris stdin berisi",
            "satu perintah:",
            "",
            "  tambah INDUK ANAK",
            "    Tambahkan ANAK sebagai anak terakhir INDUK. Kalau INDUK",
            "    belum ada, cetak galat: node INDUK tidak ada. Kalau nama ANAK",
            "    sudah dipakai, cetak galat: node ANAK sudah ada. Kalau pohon",
            "    sudah dimulai, node baru langsung siap: cetak _ready ANAK.",
            "  mulai",
            "    Panggil _ready untuk semua node, anak dulu baru induk. Anak",
            "    diproses sesuai urutan ditambahkan. Cetak _ready NAMA, satu",
            "    per baris, sampai root di paling akhir.",
            "  connect SUMBER SINYAL TARGET",
            "    Kalau SUMBER atau TARGET belum ada (periksa SUMBER dulu),",
            "    cetak galat: node X tidak ada. Kalau pasangan yang sama sudah",
            "    terhubung, cetak galat: SUMBER.SINYAL sudah terhubung ke",
            "    TARGET. Koneksi yang berhasil nggak mencetak apa pun.",
            "  emit SUMBER SINYAL",
            "    Untuk tiap target sesuai urutan connect, cetak",
            "    TARGET menerima SINYAL dari SUMBER. Kalau belum ada",
            "    penerima, cetak SUMBER.SINYAL: tidak ada penerima.",
            "  get_node DARI JALUR",
            "    Telusuri JALUR mulai dari node DARI. Ruas dipisah /, dan ..",
            "    berarti naik ke induk. Cetak jalur lengkap seperti",
            "    /root/Main/Panel, atau null kalau jalannya putus.",
            "  pohon",
            "    Cetak seluruh pohon mulai dari root. Tiap tingkat lebih",
            "    dalam menjorok dua spasi.",
            "",
            "Nama node selalu unik di seluruh pohon, dan sinyal boleh",
            "dipancarkan sebelum mulai.",
            "",
            "Contoh input:",
            "  tambah root Main",
            "  tambah Main Player",
            "  tambah Player Sprite",
            "  tambah Player Collision",
            "  tambah Main Panel",
            "  tambah Panel Label",
            "  mulai",
            "  connect Player terluka Panel",
            "  connect Player terluka Kamera",
            "  tambah Main Kamera",
            "  connect Player terluka Kamera",
            "  connect Player terluka Kamera",
            "  emit Player terluka",
            "  emit Player mati",
            "  get_node Player Sprite",
            "  get_node Sprite ../../Panel/Label",
            "  get_node Panel Player",
            "  pohon",
            "",
            "Keluaran yang diharapkan:",
            "_ready Sprite",
            "_ready Collision",
            "_ready Player",
            "_ready Label",
            "_ready Panel",
            "_ready Main",
            "_ready root",
            "galat: node Kamera tidak ada",
            "_ready Kamera",
            "galat: Player.terluka sudah terhubung ke Kamera",
            "Panel menerima terluka dari Player",
            "Kamera menerima terluka dari Player",
            "Player.mati: tidak ada penerima",
            "/root/Main/Player/Sprite",
            "/root/Main/Panel/Label",
            "null",
            "root",
            "  Main",
            "    Player",
            "      Sprite",
            "      Collision",
            "    Panel",
            "      Label",
            "    Kamera",
        ],
        "hints": [
            "Simpan tiap node sebagai objek berisi nama, induk, dan daftar anak, lalu kumpulkan semuanya di satu objek berkunci nama supaya gampang dicari.",
            "Urutan _ready adalah penelusuran pascaurut (post-order): fungsi rekursif memproses semua anak lebih dulu, baru mencetak nama node itu sendiri.",
            "Untuk get_node, pecah jalur dengan split('/') lalu pindah ke induk kalau ruasnya .., atau cari anak bernama ruas itu, dan berhenti begitu hasilnya null.",
        ],
        "solution": "const baris = require('fs').readFileSync(0, 'utf8').split('\\n')\n  .map((b) => b.trim()).filter((b) => b !== '');\n\nconst nodes = { root: { nama: 'root', induk: null, anak: [] } };\nconst koneksi = {};          // \"Sumber.sinyal\" -> daftar nama target\nlet sudahMulai = false;\n\nfunction siapkan(n) {\n  for (const a of n.anak) siapkan(a);\n  console.log('_ready ' + n.nama);\n}\n\nfunction jalurPenuh(n) {\n  const bagian = [];\n  for (let x = n; x; x = x.induk) bagian.unshift(x.nama);\n  return '/' + bagian.join('/');\n}\n\nfunction cetakPohon(n, dalam) {\n  console.log('  '.repeat(dalam) + n.nama);\n  for (const a of n.anak) cetakPohon(a, dalam + 1);\n}\n\nfor (const b of baris) {\n  const [perintah, ...arg] = b.split(/\\s+/);\n  if (perintah === 'tambah') {\n    const [induk, anak] = arg;\n    if (!nodes[induk]) { console.log(`galat: node ${induk} tidak ada`); continue; }\n    if (nodes[anak]) { console.log(`galat: node ${anak} sudah ada`); continue; }\n    const n = { nama: anak, induk: nodes[induk], anak: [] };\n    nodes[anak] = n;\n    nodes[induk].anak.push(n);\n    if (sudahMulai) siapkan(n);\n  } else if (perintah === 'mulai') {\n    sudahMulai = true;\n    siapkan(nodes.root);\n  } else if (perintah === 'connect') {\n    const [sumber, sinyal, target] = arg;\n    const hilang = [sumber, target].find((x) => !nodes[x]);\n    if (hilang) { console.log(`galat: node ${hilang} tidak ada`); continue; }\n    const kunci = sumber + '.' + sinyal;\n    if (!koneksi[kunci]) koneksi[kunci] = [];\n    if (koneksi[kunci].includes(target)) {\n      console.log(`galat: ${kunci} sudah terhubung ke ${target}`);\n      continue;\n    }\n    koneksi[kunci].push(target);\n  } else if (perintah === 'emit') {\n    const [sumber, sinyal] = arg;\n    const daftar = koneksi[sumber + '.' + sinyal] || [];\n    if (daftar.length === 0) console.log(`${sumber}.${sinyal}: tidak ada penerima`);\n    for (const t of daftar) console.log(`${t} menerima ${sinyal} dari ${sumber}`);\n  } else if (perintah === 'get_node') {\n    const [dari, jalur] = arg;\n    let n = nodes[dari] || null;\n    for (const bagian of jalur.split('/')) {\n      if (!n) break;\n      n = bagian === '..' ? n.induk : n.anak.find((a) => a.nama === bagian) || null;\n    }\n    console.log(n ? jalurPenuh(n) : 'null');\n  } else if (perintah === 'pohon') {\n    cetakPohon(nodes.root, 0);\n  }\n}",
        "stdin_list": [
            """tambah root Main
tambah Main Player
tambah Player Sprite
tambah Player Collision
tambah Main Panel
tambah Panel Label
mulai
connect Player terluka Panel
connect Player terluka Kamera
tambah Main Kamera
connect Player terluka Kamera
connect Player terluka Kamera
emit Player terluka
emit Player mati
get_node Player Sprite
get_node Sprite ../../Panel/Label
get_node Panel Player
pohon
""",
            """tambah root Level
tambah Level Musuh
tambah Musuh Pedang
tambah Lantai Batu
tambah Level Musuh
connect Musuh mati Level
emit Musuh mati
mulai
tambah Level Koin
get_node Pedang ..
get_node Level ../..
pohon
""",
        ],
    },
    {
        "title": "Latihan 6: Sistem Komponen ala GameObject",
        "difficulty": "Menengah",
        "question": [
            "Tiru cara Unity memanggil skrip. Tiap baris stdin satu perintah:",
            "",
            "  buat NAMA",
            "    Buat GameObject kosong bernama NAMA.",
            "  pasang NAMA SKRIP",
            "    Tempel komponen SKRIP ke NAMA, lalu langsung cetak",
            "    NAMA.SKRIP Awake. Kalau NAMA belum ada, cetak",
            "    galat: objek NAMA tidak ada.",
            "  hapus NAMA",
            "    Cetak NAMA.SKRIP OnDestroy untuk tiap komponen objek itu",
            "    (urut pemasangan), lalu buang objeknya. Kalau NAMA nggak ada,",
            "    cetak galat: objek NAMA tidak ada.",
            "  frame DT",
            "    Cetak -- frame N dt=DT (N mulai dari 1, DT disalin apa",
            "    adanya). Lalu jalankan tiga putaran berurutan:",
            "      1. Start untuk komponen yang belum pernah Start.",
            "      2. Update untuk semua komponen.",
            "      3. LateUpdate untuk semua komponen.",
            "    Tiap pemanggilan dicetak NAMA.SKRIP Fungsi.",
            "",
            "Di setiap putaran, komponen diproses menurut urutan pemasangan",
            "di seluruh scene, bukan per objek. Komponen yang objeknya sudah",
            "dihapus sebelum frame pertamanya nggak pernah mendapat Start.",
            "",
            "Contoh input:",
            "  buat Pemain",
            "  pasang Pemain Gerak",
            "  buat Kamera",
            "  pasang Kamera Ikuti",
            "  frame 0.016",
            "  buat Musuh",
            "  pasang Musuh Patroli",
            "  pasang Pemain Nyawa",
            "  frame 0.020",
            "  hapus Musuh",
            "  frame 0.017",
            "",
            "Keluaran yang diharapkan:",
            "Pemain.Gerak Awake",
            "Kamera.Ikuti Awake",
            "-- frame 1 dt=0.016",
            "Pemain.Gerak Start",
            "Kamera.Ikuti Start",
            "Pemain.Gerak Update",
            "Kamera.Ikuti Update",
            "Pemain.Gerak LateUpdate",
            "Kamera.Ikuti LateUpdate",
            "Musuh.Patroli Awake",
            "Pemain.Nyawa Awake",
            "-- frame 2 dt=0.020",
            "Musuh.Patroli Start",
            "Pemain.Nyawa Start",
            "Pemain.Gerak Update",
            "Kamera.Ikuti Update",
            "Musuh.Patroli Update",
            "Pemain.Nyawa Update",
            "Pemain.Gerak LateUpdate",
            "Kamera.Ikuti LateUpdate",
            "Musuh.Patroli LateUpdate",
            "Pemain.Nyawa LateUpdate",
            "Musuh.Patroli OnDestroy",
            "-- frame 3 dt=0.017",
            "Pemain.Gerak Update",
            "Kamera.Ikuti Update",
            "Pemain.Nyawa Update",
            "Pemain.Gerak LateUpdate",
            "Kamera.Ikuti LateUpdate",
            "Pemain.Nyawa LateUpdate",
        ],
        "hints": [
            "Simpan semua komponen di satu daftar global sesuai urutan pasang, dan beri tiap komponen penanda apakah ia sudah pernah mendapat Start.",
            "Perintah frame cukup tiga perulangan berurutan atas daftar yang sama: Start yang tertunda, lalu Update, lalu LateUpdate.",
            "Saat hapus, cetak OnDestroy untuk komponen milik objek itu, lalu saring daftarnya dengan filter supaya komponen itu hilang dari frame berikutnya.",
        ],
        "solution": "const baris = require('fs').readFileSync(0, 'utf8').split('\\n')\n  .map((b) => b.trim()).filter((b) => b !== '');\n\nconst objek = new Set();\nlet komponen = [];           // urut pemasangan, lintas semua objek\nlet nomorFrame = 0;\n\nfor (const b of baris) {\n  const [perintah, a, c] = b.split(/\\s+/);\n  if (perintah === 'buat') {\n    objek.add(a);\n  } else if (perintah === 'pasang') {\n    if (!objek.has(a)) { console.log(`galat: objek ${a} tidak ada`); continue; }\n    const k = { objek: a, nama: `${a}.${c}`, sudahStart: false };\n    komponen.push(k);\n    console.log(`${k.nama} Awake`);\n  } else if (perintah === 'hapus') {\n    if (!objek.has(a)) { console.log(`galat: objek ${a} tidak ada`); continue; }\n    for (const k of komponen) if (k.objek === a) console.log(`${k.nama} OnDestroy`);\n    komponen = komponen.filter((k) => k.objek !== a);\n    objek.delete(a);\n  } else if (perintah === 'frame') {\n    nomorFrame++;\n    console.log(`-- frame ${nomorFrame} dt=${a}`);\n    for (const k of komponen) {\n      if (!k.sudahStart) {\n        console.log(`${k.nama} Start`);\n        k.sudahStart = true;\n      }\n    }\n    for (const k of komponen) console.log(`${k.nama} Update`);\n    for (const k of komponen) console.log(`${k.nama} LateUpdate`);\n  }\n}",
        "stdin_list": [
            """buat Pemain
pasang Pemain Gerak
buat Kamera
pasang Kamera Ikuti
frame 0.016
buat Musuh
pasang Musuh Patroli
pasang Pemain Nyawa
frame 0.020
hapus Musuh
frame 0.017
""",
            """buat Peluru
pasang Peluru Terbang
hapus Peluru
pasang Peluru Ledak
buat Bos
pasang Bos Otak
frame 0.033
frame 0.033
""",
        ],
    },
    {
        "title": "Latihan 7: Pathfinding A* di Grid",
        "difficulty": "Lanjut",
        "question": [
            "Cari rute termurah dengan A* di peta grid. stdin berisi peta,",
            "satu baris teks untuk satu baris peta:",
            "",
            "  S     awal              G     tujuan",
            "  #     tembok            .     biaya 1",
            "  1-9   biaya sesuai angkanya",
            "",
            "Melangkah ke sebuah kotak membayar biaya kotak itu. Kotak G",
            "berbiaya 1, dan kotak S nggak dihitung. Langkah cuma ke atas,",
            "kanan, bawah, dan kiri.",
            "",
            "Pakai A* dengan h = jarak Manhattan ke G. Ambil kotak terbuka",
            "dengan f = g + h terkecil. Kalau seri, ambil yang h-nya lebih",
            "kecil. Kalau masih seri, ambil yang lebih dulu masuk. Tetangga",
            "diperiksa dengan urutan atas, kanan, bawah, kiri.",
            "",
            "Cetak biaya N, lalu peta dengan kotak rute (selain S dan G)",
            "diganti *. Kalau G nggak bisa dicapai, cukup cetak",
            "tidak ada jalan.",
            "",
            "Contoh input:",
            "  S..#.....",
            "  .#.#.###.",
            "  .#.5...#.",
            "  .#.###.#.",
            "  ...9...#G",
            "",
            "Keluaran yang diharapkan:",
            "biaya 20",
            "S**#*****",
            ".#*#*###*",
            ".#***..#*",
            ".#.###.#*",
            "...9...#G",
        ],
        "hints": [
            "Simpan g (biaya dari S) dan asal tiap kotak di objek berkunci baris dan kolom, sama seperti BFS, bedanya daftar terbuka diurutkan menurut f.",
            "Tiap putaran, urutkan daftar terbuka dengan kunci f, lalu h, lalu nomor urut masuk, ambil yang pertama, dan lewati kotak yang sudah pernah ditutup.",
            "Begitu G diambil dari daftar terbuka, telusuri asal dari G sampai S sambil mengganti kotak di tengahnya dengan tanda bintang.",
        ],
        "solution": "const peta = require('fs').readFileSync(0, 'utf8').split('\\n')\n  .map((b) => b.trimEnd()).filter((b) => b !== '');\n\nconst ARAH = [[-1, 0], [0, 1], [1, 0], [0, -1]];   // atas, kanan, bawah, kiri\nconst biaya = (ch) => (ch >= '1' && ch <= '9' ? Number(ch) : 1);\n\nlet awal, tujuan;\npeta.forEach((b, r) => {\n  for (let k = 0; k < b.length; k++) {\n    if (b[k] === 'S') awal = [r, k];\n    if (b[k] === 'G') tujuan = [r, k];\n  }\n});\nconst h = ([r, k]) => Math.abs(r - tujuan[0]) + Math.abs(k - tujuan[1]);\nconst id = ([r, k]) => r + ',' + k;\n\nconst g = { [id(awal)]: 0 };\nconst asal = {};\nconst tertutup = new Set();\nlet terbuka = [{ sel: awal, f: h(awal), h: h(awal), urut: 0 }];\nlet urut = 1;\nlet ketemu = false;\n\nwhile (terbuka.length > 0) {\n  // f terkecil, lalu h terkecil, lalu yang lebih dulu masuk.\n  terbuka.sort((a, b) => a.f - b.f || a.h - b.h || a.urut - b.urut);\n  const { sel } = terbuka.shift();\n  if (tertutup.has(id(sel))) continue;\n  tertutup.add(id(sel));\n  if (id(sel) === id(tujuan)) { ketemu = true; break; }\n  for (const [dr, dk] of ARAH) {\n    const t = [sel[0] + dr, sel[1] + dk];\n    const ch = peta[t[0]] ? peta[t[0]][t[1]] : undefined;\n    if (ch === undefined || ch === '#' || tertutup.has(id(t))) continue;\n    const gBaru = g[id(sel)] + biaya(ch);\n    if (g[id(t)] === undefined || gBaru < g[id(t)]) {\n      g[id(t)] = gBaru;\n      asal[id(t)] = sel;\n      terbuka.push({ sel: t, f: gBaru + h(t), h: h(t), urut: urut++ });\n    }\n  }\n}\n\nif (!ketemu) {\n  console.log('tidak ada jalan');\n} else {\n  const gambar = peta.map((b) => b.split(''));\n  for (let s = asal[id(tujuan)]; id(s) !== id(awal); s = asal[id(s)]) {\n    gambar[s[0]][s[1]] = '*';\n  }\n  console.log('biaya ' + g[id(tujuan)]);\n  for (const b of gambar) console.log(b.join(''));\n}",
        "stdin_list": [
            """S..#.....
.#.#.###.
.#.5...#.
.#.###.#.
...9...#G
""",
            """S.2.#
.#9.#
.#..#
.###G
""",
            """S1112
3#9#1
2#5#1
1111G
""",
        ],
    },
    {
        "title": "Latihan 8: Behavior Tree Mini",
        "difficulty": "Lanjut",
        "question": [
            "Jalankan behavior tree dari stdin. Bagian pertama input adalah",
            "pohon, satu node per baris, dan tiap tingkat lebih dalam",
            "menjorok dua spasi:",
            "",
            "  selector NAMA       coba anak dari atas sampai ada yang nggak gagal",
            "  sequence NAMA       jalankan anak selama hasilnya berhasil",
            "  kondisi NAMA        berhasil kalau NAMA ada di daftar tick itu",
            "  aksi NAMA STATUS    selalu mengembalikan STATUS",
            "",
            "Sesudah baris ---, tiap baris adalah satu tick: daftar kondisi",
            "yang benar dipisah spasi, atau - kalau nggak ada yang benar.",
            "Status yang mungkin: berhasil, gagal, berjalan.",
            "",
            "Selector berhenti di anak pertama yang hasilnya selain gagal,",
            "lalu mengembalikan hasil itu. Kalau semua anaknya gagal, selector",
            "gagal. Sequence berhenti di anak pertama yang hasilnya selain",
            "berhasil, lalu mengembalikan hasil itu. Kalau semua anaknya",
            "berhasil, sequence berhasil.",
            "",
            "Untuk tiap tick, cetak tick N, lalu evaluasi pohon dari akar.",
            "Setiap node yang dikunjungi dicetak begitu hasilnya diketahui:",
            "dua spasi, nama node, spasi, status. Jadi anak selalu tercetak",
            "sebelum induknya, dan node yang nggak dikunjungi nggak tercetak.",
            "",
            "Contoh input:",
            "  selector otak",
            "    sequence kabur",
            "      kondisi sekarat",
            "      aksi lari berjalan",
            "    sequence serang",
            "      kondisi dekat",
            "      kondisi bertenaga",
            "      aksi pukul berhasil",
            "    sequence kejar",
            "      kondisi terlihat",
            "      aksi dekati berjalan",
            "    aksi patroli berjalan",
            "  ---",
            "  dekat terlihat",
            "  dekat bertenaga terlihat",
            "  sekarat dekat",
            "",
            "Keluaran yang diharapkan:",
            "tick 1",
            "  sekarat gagal",
            "  kabur gagal",
            "  dekat berhasil",
            "  bertenaga gagal",
            "  serang gagal",
            "  terlihat berhasil",
            "  dekati berjalan",
            "  kejar berjalan",
            "  otak berjalan",
            "tick 2",
            "  sekarat gagal",
            "  kabur gagal",
            "  dekat berhasil",
            "  bertenaga berhasil",
            "  pukul berhasil",
            "  serang berhasil",
            "  otak berhasil",
            "tick 3",
            "  sekarat berhasil",
            "  lari berjalan",
            "  kabur berjalan",
            "  otak berjalan",
        ],
        "hints": [
            "Baca pohon dengan tumpukan: jumlah spasi di depan baris dibagi dua adalah kedalaman, dan induk sebuah node adalah node terakhir yang kedalamannya satu tingkat di atasnya.",
            "Tulis satu fungsi rekursif yang menghitung hasil sebuah node, mencetaknya sesudah hasilnya diketahui, lalu mengembalikannya ke pemanggil.",
            "Selector dan sequence bisa memakai perulangan yang sama: selector lanjut selama anaknya gagal, sequence lanjut selama anaknya berhasil.",
        ],
        "solution": "const semua = require('fs').readFileSync(0, 'utf8').split('\\n')\n  .map((b) => b.trimEnd()).filter((b) => b.trim() !== '');\nconst batas = semua.indexOf('---');\nconst barisPohon = semua.slice(0, batas);\nconst barisTick = semua.slice(batas + 1);\n\n// Susun pohon dari indentasi: dua spasi = satu tingkat lebih dalam.\nconst tumpukan = [];\nlet akar = null;\nfor (const b of barisPohon) {\n  const dalam = (b.length - b.trimStart().length) / 2;\n  const [jenis, nama, status] = b.trim().split(/\\s+/);\n  const n = { jenis, nama, status, anak: [] };\n  tumpukan.length = dalam;\n  if (dalam === 0) akar = n;\n  else tumpukan[dalam - 1].anak.push(n);\n  tumpukan.push(n);\n}\n\nfunction tick(n, fakta) {\n  let hasil;\n  if (n.jenis === 'kondisi') {\n    hasil = fakta.has(n.nama) ? 'berhasil' : 'gagal';\n  } else if (n.jenis === 'aksi') {\n    hasil = n.status;\n  } else {\n    // sequence lanjut selama anaknya berhasil, selector lanjut selama gagal.\n    const lanjut = n.jenis === 'sequence' ? 'berhasil' : 'gagal';\n    hasil = lanjut;\n    for (const a of n.anak) {\n      const s = tick(a, fakta);\n      if (s !== lanjut) { hasil = s; break; }\n    }\n  }\n  console.log(`  ${n.nama} ${hasil}`);\n  return hasil;\n}\n\nbarisTick.forEach((b, i) => {\n  const fakta = new Set(b.trim() === '-' ? [] : b.trim().split(/\\s+/));\n  console.log(`tick ${i + 1}`);\n  tick(akar, fakta);\n});",
        "stdin_list": [
            """selector otak
  sequence kabur
    kondisi sekarat
    aksi lari berjalan
  sequence serang
    kondisi dekat
    kondisi bertenaga
    aksi pukul berhasil
  sequence kejar
    kondisi terlihat
    aksi dekati berjalan
  aksi patroli berjalan
---
dekat terlihat
dekat bertenaga terlihat
sekarat dekat
""",
            """sequence buka_peti
  kondisi punya_kunci
  selector cara_buka
    aksi putar_kunci gagal
    aksi congkel berjalan
  aksi ambil_isi berhasil
---
punya_kunci
-
""",
        ],
    },
    {
        "title": "Latihan 9: Pencatat Achievement dan Save Game",
        "difficulty": "Lanjut",
        "question": [
            "Tiru pencatat achievement dan save game. Keadaan permainan",
            "awalnya level 1, kill 0, koin 0. Tiap baris stdin satu kejadian:",
            "",
            "  kill N     tambahkan N ke kill",
            "  koin N     tambahkan N ke koin",
            "  level N    jadikan level = N",
            "  simpan     simpan keadaan, lalu cetak simpan JSON",
            "  muat       kembalikan keadaan dari simpanan terakhir, lalu",
            "             cetak muat JSON, atau muat: belum ada simpanan",
            "             kalau belum pernah menyimpan",
            "",
            "JSON-nya satu baris tanpa spasi, dengan kunci urut abjad,",
            "misalnya {\"kill\":1,\"koin\":30,\"level\":2}.",
            "",
            "Sesudah setiap kejadian (termasuk muat), periksa achievement",
            "dengan urutan ini:",
            "",
            "  Darah Pertama   kill >= 1",
            "  Pemburu         kill >= 10",
            "  Penjelajah      level >= 3",
            "  Saudagar        koin >= 100",
            "",
            "Achievement yang baru terpenuhi dicetak achievement: NAMA, dan",
            "tiap achievement cuma terbuka sekali. Seperti di Steam,",
            "achievement tersimpan di akun, jadi memuat save lama nggak",
            "menghapusnya dan nggak membuatnya terbuka lagi.",
            "",
            "Di akhir, cetak terbuka: lalu nama achievement sesuai urutan",
            "terbukanya, dipisah koma dan spasi. Kalau belum ada, cetak",
            "terbuka: -.",
            "",
            "Contoh input:",
            "  kill 1",
            "  koin 30",
            "  level 2",
            "  simpan",
            "  kill 9",
            "  koin 80",
            "  muat",
            "  kill 4",
            "  level 3",
            "  simpan",
            "  muat",
            "",
            "Keluaran yang diharapkan:",
            "achievement: Darah Pertama",
            "simpan {\"kill\":1,\"koin\":30,\"level\":2}",
            "achievement: Pemburu",
            "achievement: Saudagar",
            "muat {\"kill\":1,\"koin\":30,\"level\":2}",
            "achievement: Penjelajah",
            "simpan {\"kill\":5,\"koin\":30,\"level\":3}",
            "muat {\"kill\":5,\"koin\":30,\"level\":3}",
            "terbuka: Darah Pertama, Pemburu, Saudagar, Penjelajah",
        ],
        "hints": [
            "Pisahkan dua hal: keadaan permainan, yang ikut disimpan dan dimuat, dan daftar achievement yang sudah terbuka, yang nggak pernah ikut dimuat ulang.",
            "Simpan berkas save sebagai teks JSON, lalu pakai JSON.parse saat muat, supaya keadaan yang disimpan nggak ikut berubah waktu permainan berjalan.",
            "JSON.stringify mengikuti urutan kunci objek, jadi susun objek baru dengan kunci dari Object.keys(...).sort() sebelum mengubahnya jadi teks.",
        ],
        "solution": "const baris = require('fs').readFileSync(0, 'utf8').split('\\n')\n  .map((b) => b.trim()).filter((b) => b !== '');\n\nconst ATURAN = [\n  ['Darah Pertama', (s) => s.kill >= 1],\n  ['Pemburu', (s) => s.kill >= 10],\n  ['Penjelajah', (s) => s.level >= 3],\n  ['Saudagar', (s) => s.koin >= 100],\n];\n\nlet keadaan = { level: 1, kill: 0, koin: 0 };\nlet simpanan = null;               // teks JSON, seperti berkas save\nconst terbuka = [];                // milik akun, tidak ikut save\n\nfunction urutkanKunci(obj) {\n  const hasil = {};\n  for (const k of Object.keys(obj).sort()) hasil[k] = obj[k];\n  return hasil;\n}\n\nfunction periksaAchievement() {\n  for (const [nama, syarat] of ATURAN) {\n    if (!terbuka.includes(nama) && syarat(keadaan)) {\n      terbuka.push(nama);\n      console.log('achievement: ' + nama);\n    }\n  }\n}\n\nfor (const b of baris) {\n  const [perintah, angka] = b.split(/\\s+/);\n  if (perintah === 'kill') keadaan.kill += Number(angka);\n  else if (perintah === 'koin') keadaan.koin += Number(angka);\n  else if (perintah === 'level') keadaan.level = Number(angka);\n  else if (perintah === 'simpan') {\n    simpanan = JSON.stringify(urutkanKunci(keadaan));\n    console.log('simpan ' + simpanan);\n  } else if (perintah === 'muat') {\n    if (simpanan === null) {\n      console.log('muat: belum ada simpanan');\n    } else {\n      keadaan = JSON.parse(simpanan);\n      console.log('muat ' + simpanan);\n    }\n  }\n  periksaAchievement();\n}\nconsole.log('terbuka: ' + (terbuka.length ? terbuka.join(', ') : '-'));",
        "stdin_list": [
            """kill 1
koin 30
level 2
simpan
kill 9
koin 80
muat
kill 4
level 3
simpan
muat
""",
            """muat
koin 120
kill 12
level 5
simpan
""",
        ],
    },
    {
        "title": "Latihan 10: Rasterizer Segitiga ASCII",
        "difficulty": "Lanjut",
        "question": [
            "Tulis rasterizer segitiga yang menggambar ke grid teks. Input satu",
            "baris berisi delapan bilangan bulat:",
            "",
            "  lebar tinggi x0 y0 x1 y1 x2 y2",
            "",
            "Sumbu y mengarah ke bawah, jadi y = 0 adalah baris paling atas.",
            "Piksel (x, y) diwakili pusatnya, yaitu titik (x + 0.5, y + 0.5).",
            "",
            "Aturannya:",
            "  1. Edge function:",
            "     tepi(a, b, p) = (b.x - a.x) * (p.y - a.y)",
            "                   - (b.y - a.y) * (p.x - a.x)",
            "  2. Hitung luas = tepi(v0, v1, v2). Kalau luas 0, segitiganya gepeng",
            "     dan nggak ada piksel yang diisi. Kalau luas negatif, tukar v1",
            "     dan v2 supaya urutannya searah jarum jam di layar.",
            "  3. Untuk tiap piksel hitung w0 = tepi(v1, v2, p),",
            "     w1 = tepi(v2, v0, p), dan w2 = tepi(v0, v1, p).",
            "  4. Piksel diisi kalau setiap w memenuhi syarat: w > 0, atau w = 0",
            "     dan tepinya tepi atas-kiri. Tepi milik w0 adalah v1 ke v2,",
            "     milik w1 adalah v2 ke v0, milik w2 adalah v0 ke v1.",
            "  5. Tepi dari a ke b disebut atas-kiri kalau dy < 0, atau dy = 0",
            "     dan dx > 0, dengan dx = b.x - a.x dan dy = b.y - a.y.",
            "",
            "Cetak grid dengan # untuk piksel terisi dan . untuk yang kosong,",
            "lalu satu baris terisi: N piksel.",
            "",
            "Contoh input:",
            "  16 8 1 1 14 3 5 7",
            "",
            "Keluaran yang diharapkan:",
            "................",
            ".###............",
            "..#########.....",
            "...##########...",
            "...########.....",
            "....####........",
            ".....#..........",
            "................",
            "terisi: 35 piksel",
            "",
            "Dua segitiga yang berbagi diagonal membuktikan aturan atas-kiri.",
            "Segitiga pertama mendapat 28 piksel, segitiga pelengkapnya (8 8 8 0",
            "8 8 0 8) mendapat 36, jumlahnya pas 64 piksel persegi 8 x 8.",
            "",
            "Untuk input 8 8 0 0 8 0 0 8, keluarannya:",
            "#######.",
            "######..",
            "#####...",
            "####....",
            "###.....",
            "##......",
            "#.......",
            "........",
            "terisi: 28 piksel",
        ],
        "hints": [
            "Pusat piksel seperti 3.5 disimpan tepat oleh komputer, jadi hasil edge function yang nol bisa dibandingkan dengan === tanpa takut galat pembulatan.",
            "Buat dua fungsi kecil, atasKiri(a, b) dan masuk(w, a, b), supaya syarat di aturan 4 terbaca satu per satu.",
            "Sesudah v1 dan v2 ditukar untuk luas negatif, semua segitiga searah jarum jam di layar, jadi titik di dalam selalu memberi w positif.",
        ],
        "solution": "const angka = require('fs').readFileSync(0, 'utf8').trim().split(/\\s+/).map(Number);\nconst [lebar, tinggi] = angka;\nlet v0 = { x: angka[2], y: angka[3] };\nlet v1 = { x: angka[4], y: angka[5] };\nlet v2 = { x: angka[6], y: angka[7] };\n\nfunction tepi(a, b, p) {\n  return (b.x - a.x) * (p.y - a.y) - (b.y - a.y) * (p.x - a.x);\n}\n\nfunction atasKiri(a, b) {\n  const dx = b.x - a.x;\n  const dy = b.y - a.y;\n  return (dy === 0 && dx > 0) || dy < 0;\n}\n\nfunction masuk(w, a, b) {\n  return w > 0 || (w === 0 && atasKiri(a, b));\n}\n\nconst luas = tepi(v0, v1, v2);\nif (luas < 0) {\n  [v1, v2] = [v2, v1];\n}\n\nlet terisi = 0;\nfor (let y = 0; y < tinggi; y++) {\n  let baris = '';\n  for (let x = 0; x < lebar; x++) {\n    const p = { x: x + 0.5, y: y + 0.5 };\n    const isi = luas !== 0\n      && masuk(tepi(v1, v2, p), v1, v2)\n      && masuk(tepi(v2, v0, p), v2, v0)\n      && masuk(tepi(v0, v1, p), v0, v1);\n    if (isi) terisi++;\n    baris += isi ? '#' : '.';\n  }\n  console.log(baris);\n}\nconsole.log(`terisi: ${terisi} piksel`);\n",
        "stdin_list": [
            """16 8 1 1 14 3 5 7
""",
            """8 8 0 0 8 0 0 8
""",
            """8 8 8 0 8 8 0 8
""",
            """8 8 0 0 0 8 8 0
""",
            """6 4 1 1 3 1 5 1
""",
        ],
    },
    {
        "title": "Latihan 11: Proyeksi Titik 3D ke Layar",
        "difficulty": "Lanjut",
        "question": [
            "Proyeksikan titik-titik 3D ke piksel layar, persis seperti yang",
            "dikerjakan vertex shader dengan matriks view dan proyeksi.",
            "",
            "Kamera berada di (cx, cy, cz) dan bisa menoleh dengan sudut yaw",
            "dalam derajat. Yaw 0 berarti kamera menghadap sumbu -z, yaw 90",
            "berarti menghadap sumbu -x. Di dunia 3D sumbu y mengarah ke atas.",
            "",
            "Input:",
            "  baris 1: cx cy cz yaw",
            "  baris 2: lebar tinggi fov   (fov = sudut pandang vertikal, derajat)",
            "  baris berikutnya: x y z     (satu titik per baris)",
            "",
            "Untuk tiap titik:",
            "  1. View transform: dx = x - cx, dy = y - cy, dz = z - cz, lalu",
            "     vx = dx * cos(yaw) - dz * sin(yaw), vy = dy,",
            "     vz = dx * sin(yaw) + dz * cos(yaw).",
            "  2. Kalau vz > -0.1 (lebih dekat dari near plane atau di belakang",
            "     kamera), cetak titik N: di belakang kamera.",
            "  3. f = 1 / tan(fov / 2) dan aspek = lebar / tinggi, lalu",
            "     ndcX = (f / aspek) * vx / -vz dan ndcY = f * vy / -vz.",
            "  4. px = floor((ndcX + 1) / 2 * lebar),",
            "     py = floor((1 - ndcY) / 2 * tinggi).",
            "  5. Kalau px di luar 0 sampai lebar - 1 atau py di luar 0 sampai",
            "     tinggi - 1, cetak titik N: di luar layar.",
            "  6. Selain itu cetak titik N: (px, py) kedalaman D, dengan D = -vz",
            "     dua desimal.",
            "",
            "Contoh input:",
            "  0 1 5 0",
            "  160 90 60",
            "  0 1 0",
            "  2 2 -5",
            "  0 0 10",
            "  30 1 0",
            "  -1.5 0.2 1.2",
            "  0 1 4.95",
            "",
            "Keluaran yang diharapkan:",
            "titik 1: (80, 45) kedalaman 5.00",
            "titik 2: (95, 37) kedalaman 10.00",
            "titik 3: di belakang kamera",
            "titik 4: di luar layar",
            "titik 5: (49, 61) kedalaman 3.80",
            "titik 6: di belakang kamera",
            "",
            "Contoh kedua, kamera menoleh 90 derajat:",
            "  0 1.6 0 90",
            "  100 100 90",
            "  -4 2.6 1",
            "  -2 0.9 -0.7",
            "  3 1.6 0",
            "  -6 1.6 9",
            "",
            "Untuk input 0 1.6 0 90, keluarannya:",
            "titik 1: (37, 37) kedalaman 4.00",
            "titik 2: (67, 67) kedalaman 2.00",
            "titik 3: di belakang kamera",
            "titik 4: di luar layar",
        ],
        "hints": [
            "Proyeksi perspektif pada intinya membagi x dan y dengan jarak titik ke kamera, yaitu -vz, sehingga titik yang jauh mengumpul ke tengah layar.",
            "Math.sin, Math.cos, dan Math.tan menerima radian, jadi ubah yaw dan setengah fov dengan rumus derajat * Math.PI / 180.",
            "Cek near plane sebelum membagi dengan -vz, lalu pakai Math.floor untuk piksel dan periksa batas layar sebelum mencetak.",
        ],
        "solution": "const baris = require('fs').readFileSync(0, 'utf8').trim().split('\\n');\nconst [cx, cy, cz, yaw] = baris[0].trim().split(/\\s+/).map(Number);\nconst [lebar, tinggi, fov] = baris[1].trim().split(/\\s+/).map(Number);\n\nconst DEKAT = 0.1;\nconst r = (yaw * Math.PI) / 180;\nconst f = 1 / Math.tan((fov * Math.PI) / 360);\nconst aspek = lebar / tinggi;\n\nbaris.slice(2).forEach((teks, i) => {\n  const [x, y, z] = teks.trim().split(/\\s+/).map(Number);\n  // view transform: geser dunia supaya kamera di titik nol, lalu putar balik\n  const dx = x - cx;\n  const dy = y - cy;\n  const dz = z - cz;\n  const vx = dx * Math.cos(r) - dz * Math.sin(r);\n  const vy = dy;\n  const vz = dx * Math.sin(r) + dz * Math.cos(r);\n  const label = `titik ${i + 1}:`;\n  if (vz > -DEKAT) {\n    console.log(`${label} di belakang kamera`);\n    return;\n  }\n  // proyeksi perspektif: bagi dengan jarak (-vz)\n  const ndcX = ((f / aspek) * vx) / -vz;\n  const ndcY = (f * vy) / -vz;\n  const px = Math.floor(((ndcX + 1) / 2) * lebar);\n  const py = Math.floor(((1 - ndcY) / 2) * tinggi);\n  if (px < 0 || px >= lebar || py < 0 || py >= tinggi) {\n    console.log(`${label} di luar layar`);\n    return;\n  }\n  console.log(`${label} (${px}, ${py}) kedalaman ${(-vz).toFixed(2)}`);\n});\n",
        "stdin_list": [
            """0 1 5 0
160 90 60
0 1 0
2 2 -5
0 0 10
30 1 0
-1.5 0.2 1.2
0 1 4.95
""",
            """0 1.6 0 90
100 100 90
-4 2.6 1
-2 0.9 -0.7
3 1.6 0
-6 1.6 9
""",
        ],
    },
    {
        "title": "Latihan 12: ECS Mini dengan Sistem Gerak",
        "difficulty": "Lanjut",
        "question": [
            "Bangun ECS mini. Entitas cuma nomor, mulai dari 1. Komponen",
            "disimpan per jenis (misalnya satu Map per jenis), dikunci nomor",
            "entitas. Ada empat jenis komponen:",
            "",
            "  Posisi x y     Kecepatan x y     Nyawa n     Racun n",
            "",
            "Perintah dari stdin, satu per baris:",
            "  buat                      buat entitas baru, nomor berikutnya",
            "  pasang ID Jenis angka...  pasang atau ganti komponen",
            "  lepas ID Jenis            lepas komponen",
            "  tick                      jalankan semua sistem, lalu cetak",
            "",
            "pasang dan lepas untuk entitas yang belum dibuat atau sudah hancur",
            "diabaikan. Semua angka bilangan bulat.",
            "",
            "Tiap tick menjalankan dua sistem, berurutan:",
            "  1. Sistem gerak: entitas yang punya Posisi dan Kecepatan,",
            "     posisinya ditambah kecepatan.",
            "  2. Sistem racun: entitas yang punya Nyawa dan Racun, nyawanya",
            "     dikurangi nilai Racun. Kalau nyawa jadi 0 atau kurang,",
            "     entitas hancur (semua komponennya dilepas) dan cetak",
            "     entitas ID hancur. Proses urut menurut nomor entitas.",
            "",
            "Sesudah kedua sistem, cetak tick N: lalu entitas yang punya Posisi,",
            "urut nomor, dalam bentuk ID(x,y), ditambah [n] kalau ia punya",
            "Nyawa. Kalau nggak ada satu pun, cetak tick N: kosong.",
            "",
            "Contoh input:",
            "  buat",
            "  buat",
            "  buat",
            "  pasang 1 Posisi 0 0",
            "  pasang 1 Kecepatan 2 1",
            "  pasang 1 Nyawa 3",
            "  pasang 2 Posisi 10 0",
            "  pasang 2 Nyawa 2",
            "  pasang 2 Racun 1",
            "  pasang 3 Kecepatan 5 5",
            "  tick",
            "  pasang 3 Posisi 0 10",
            "  pasang 1 Racun 2",
            "  tick",
            "  lepas 1 Kecepatan",
            "  tick",
            "  pasang 2 Kecepatan 1 0",
            "  pasang 3 Nyawa 1",
            "  tick",
            "",
            "Keluaran yang diharapkan:",
            "tick 1: 1(2,1)[3] 2(10,0)[1]",
            "entitas 2 hancur",
            "tick 2: 1(4,2)[1] 3(5,15)",
            "entitas 1 hancur",
            "tick 3: 3(10,20)",
            "tick 4: 3(15,25)[1]",
            "",
            "Perhatikan entitas 3: di tick 1 ia sudah punya Kecepatan tapi belum",
            "punya Posisi, jadi sistem gerak melewatinya dan ia nggak dicetak.",
            "Di tick 4, perintah pasang untuk entitas 2 diabaikan karena",
            "entitas itu sudah hancur.",
        ],
        "hints": [
            "Karena tiap jenis komponen punya Map sendiri, pertanyaan apakah entitas punya Posisi cukup dijawab dengan memeriksa Map Posisi.",
            "Simpan juga himpunan entitas yang masih hidup, supaya perintah untuk entitas yang sudah hancur bisa diabaikan.",
            "Ambil kunci Map lalu urutkan dengan sort((a, b) => a - b) sebelum diproses atau dicetak, karena komponen bisa dipasang dengan urutan acak.",
        ],
        "solution": "const perintah = require('fs').readFileSync(0, 'utf8').trim().split('\\n');\n\nconst JENIS = ['Posisi', 'Kecepatan', 'Nyawa', 'Racun'];\nconst simpan = {};\nfor (const j of JENIS) simpan[j] = new Map();\nconst hidup = new Set();\nlet berikut = 1;\nlet nomorTick = 0;\n\nfunction urutId(peta) {\n  return [...peta.keys()].sort((a, b) => a - b);\n}\n\nfunction hancurkan(id) {\n  hidup.delete(id);\n  for (const j of JENIS) simpan[j].delete(id);\n}\n\nfunction sistemGerak() {\n  for (const id of urutId(simpan.Kecepatan)) {\n    const p = simpan.Posisi.get(id);\n    if (!p) continue;\n    const v = simpan.Kecepatan.get(id);\n    p.x += v.x;\n    p.y += v.y;\n  }\n}\n\nfunction sistemRacun() {\n  for (const id of urutId(simpan.Racun)) {\n    if (!simpan.Nyawa.has(id)) continue;\n    const sisa = simpan.Nyawa.get(id) - simpan.Racun.get(id);\n    if (sisa <= 0) {\n      hancurkan(id);\n      console.log(`entitas ${id} hancur`);\n    } else {\n      simpan.Nyawa.set(id, sisa);\n    }\n  }\n}\n\nfunction cetak() {\n  const isi = urutId(simpan.Posisi).map((id) => {\n    const p = simpan.Posisi.get(id);\n    const n = simpan.Nyawa.has(id) ? `[${simpan.Nyawa.get(id)}]` : '';\n    return `${id}(${p.x},${p.y})${n}`;\n  });\n  console.log(`tick ${nomorTick}: ${isi.length ? isi.join(' ') : 'kosong'}`);\n}\n\nfor (const baris of perintah) {\n  const k = baris.trim().split(/\\s+/);\n  if (k[0] === 'buat') {\n    hidup.add(berikut++);\n  } else if (k[0] === 'pasang') {\n    const id = Number(k[1]);\n    if (!hidup.has(id) || !JENIS.includes(k[2])) continue;\n    const a = Number(k[3]);\n    const b = Number(k[4]);\n    if (k[2] === 'Posisi' || k[2] === 'Kecepatan') {\n      simpan[k[2]].set(id, { x: a, y: b });\n    } else {\n      simpan[k[2]].set(id, a);\n    }\n  } else if (k[0] === 'lepas') {\n    const id = Number(k[1]);\n    if (hidup.has(id) && JENIS.includes(k[2])) simpan[k[2]].delete(id);\n  } else if (k[0] === 'tick') {\n    nomorTick++;\n    sistemGerak();\n    sistemRacun();\n    cetak();\n  }\n}\n",
        "stdin_list": [
            """buat
buat
buat
pasang 1 Posisi 0 0
pasang 1 Kecepatan 2 1
pasang 1 Nyawa 3
pasang 2 Posisi 10 0
pasang 2 Nyawa 2
pasang 2 Racun 1
pasang 3 Kecepatan 5 5
tick
pasang 3 Posisi 0 10
pasang 1 Racun 2
tick
lepas 1 Kecepatan
tick
pasang 2 Kecepatan 1 0
pasang 3 Nyawa 1
tick
""",
            """buat
buat
pasang 1 Posisi 5 5
pasang 1 Kecepatan -1 0
pasang 2 Posisi 0 0
pasang 2 Nyawa 1
pasang 2 Racun 1
tick
tick
buat
pasang 2 Posisi 9 9
pasang 3 Posisi 1 1
pasang 3 Kecepatan 0 2
lepas 1 Posisi
tick
""",
        ],
    },
    {
        "title": "Latihan 13: Raycast ke Bidang Lantai",
        "difficulty": "Lanjut",
        "question": [
            "Hitung di mana sinar-sinar dari kamera AR menabrak bidang datar",
            "y = h, misalnya lantai atau permukaan meja.",
            "",
            "Input:",
            "  baris 1: h",
            "  baris berikutnya: ox oy oz dx dy dz   (asal dan arah satu sinar)",
            "",
            "Sinar ditulis p(s) = o + s * d. Untuk tiap sinar:",
            "  1. Kalau dy = 0, cetak sinar N: tidak kena (sejajar).",
            "  2. Hitung s = (h - oy) / dy. Kalau s < 0, cetak",
            "     sinar N: tidak kena (menjauh).",
            "  3. Selain itu cetak sinar N: kena (x, y, z), s = S, dengan semua",
            "     angka dua desimal (toFixed(2)). Angka yang tercetak -0.00",
            "     ditulis 0.00.",
            "",
            "s = 0 masih dihitung kena: asal sinarnya tepat di bidang.",
            "",
            "Contoh input:",
            "  0",
            "  0 1.5 0 0 -0.75 -0.72",
            "  2 1.6 -1 0.3 -0.8 -0.5",
            "  0 1.5 0 0 0 -1",
            "  0 1.5 0 0 0.5 -1",
            "  1 0 1 0 -1 0",
            "",
            "Keluaran yang diharapkan:",
            "sinar 1: kena (0.00, 0.00, -1.44), s = 2.00",
            "sinar 2: kena (2.60, 0.00, -2.00), s = 2.00",
            "sinar 3: tidak kena (sejajar)",
            "sinar 4: tidak kena (menjauh)",
            "sinar 5: kena (1.00, 0.00, 1.00), s = 0.00",
            "",
            "Contoh kedua, bidang meja setinggi 0,75 m:",
            "  0.75",
            "  0 1.5 0 0.2 -1 -1",
            "  -1 0.5 0 0 1 -2",
            "  0 1.5 0 0 0 1",
            "  0.4 1.2 0.1 -0.1 -0.3 -0.2",
            "",
            "Untuk input 0.75, keluarannya:",
            "sinar 1: kena (0.15, 0.75, -0.75), s = 0.75",
            "sinar 2: kena (-1.00, 0.75, -0.50), s = 0.25",
            "sinar 3: tidak kena (sejajar)",
            "sinar 4: kena (0.25, 0.75, -0.20), s = 1.50",
        ],
        "hints": [
            "Titik potong adalah titik di sinar yang koordinat y-nya sama dengan h, jadi cukup selesaikan oy + s * dy = h untuk s.",
            "Periksa dy sebelum membagi, karena pembagian dengan nol di JavaScript menghasilkan Infinity dan nggak melempar error.",
            "Untuk menghindari -0.00, ubah angka yang nilai mutlaknya di bawah 0.005 jadi 0 sebelum memanggil toFixed(2).",
        ],
        "solution": "const baris = require('fs').readFileSync(0, 'utf8').trim().split('\\n');\nconst h = Number(baris[0]);\nconst f2 = (n) => (Math.abs(n) < 0.005 ? 0 : n).toFixed(2);\n\nbaris.slice(1).forEach((teks, i) => {\n  const [ox, oy, oz, dx, dy, dz] = teks.trim().split(/\\s+/).map(Number);\n  const label = `sinar ${i + 1}:`;\n  if (dy === 0) {\n    console.log(`${label} tidak kena (sejajar)`);\n    return;\n  }\n  const s = (h - oy) / dy;\n  if (s < 0) {\n    console.log(`${label} tidak kena (menjauh)`);\n    return;\n  }\n  const titik = [ox + s * dx, oy + s * dy, oz + s * dz].map(f2).join(', ');\n  console.log(`${label} kena (${titik}), s = ${f2(s)}`);\n});\n",
        "stdin_list": [
            """0
0 1.5 0 0 -0.75 -0.72
2 1.6 -1 0.3 -0.8 -0.5
0 1.5 0 0 0 -1
0 1.5 0 0 0.5 -1
1 0 1 0 -1 0
""",
            """0.75
0 1.5 0 0.2 -1 -1
-1 0.5 0 0 1 -2
0 1.5 0 0 0 1
0.4 1.2 0.1 -0.1 -0.3 -0.2
""",
        ],
    },
    {
        "title": "Latihan 14: Mesin Game Mini dengan Replay",
        "difficulty": "Sulit",
        "proyek": True,
        "question": [
            "Proyek akhir: mesin game kecil yang deterministik. Ia menggabungkan",
            "fixed timestep dan akumulator (bab 01), tabrakan AABB (bab 02), ECS",
            "dan replay (bab 09). Semua angka bilangan bulat.",
            "",
            "Input, satu perintah per baris:",
            "  langkah L                          lama satu tick, ms",
            "  arena LEBAR TINGGI                 batas dunia",
            "  entitas nama jenis x y w h vx vy   jenis: pemain, koin, musuh",
            "  frame MS INPUT                     INPUT: kanan, kiri, atas,",
            "                                     bawah, diam",
            "",
            "Entitas mendapat nomor 1, 2, 3, ... sesuai urutan di input. Pemain",
            "cuma satu dan mulai dengan nyawa 3. Sumbu y mengarah ke bawah.",
            "Simpan entitas seperti ECS: satu Map per komponen (nama, jenis,",
            "posisi, kotak, kecepatan, nyawa).",
            "",
            "Main pertama. Tiap frame, MS ditambahkan ke akumulator. Selama",
            "akumulator >= L, kurangi akumulator dengan L dan jalankan satu",
            "tick dengan INPUT frame itu. Catat INPUT tiap tick ke rekaman.",
            "",
            "Satu tick menjalankan sistem berikut, berurutan, dan tiap sistem",
            "memproses entitas urut menurut nomor:",
            "  1. Input: kecepatan pemain jadi kanan (2,0), kiri (-2,0),",
            "     atas (0,-2), bawah (0,2), atau diam (0,0).",
            "  2. Gerak: posisi semua entitas ditambah kecepatannya.",
            "  3. Arena: kalau x < 0 atau x > LEBAR - w, x dijepit ke rentang",
            "     itu, dan kalau entitasnya musuh, vx dibalik tandanya. Sama",
            "     untuk y dengan TINGGI - h dan vy.",
            "  4. Tabrakan: pemain dicek dengan setiap entitas lain. Dua kotak",
            "     bertabrakan kalau a.x < b.x + b.w, b.x < a.x + a.w,",
            "     a.y < b.y + b.h, dan b.y < a.y + a.h (bersentuhan tepi nggak",
            "     dihitung).",
            "       - Kena koin: skor + 10, koin hancur, cetak",
            "         tick T: ambil NAMA (skor S).",
            "       - Kena musuh: nyawa - 1, musuh hancur, cetak",
            "         tick T: kena NAMA (nyawa N). Kalau nyawa jadi 0, pemain",
            "         hancur, cetak tick T: pemain kalah, dan permainan selesai.",
            "       - Sesudah semua dicek, kalau koin sudah habis, cetak",
            "         tick T: semua koin terambil, dan permainan selesai.",
            "",
            "Begitu permainan selesai, tick dan frame berikutnya diabaikan.",
            "",
            "Sesudah main pertama, cetak akhir tick T: skor S, nyawa N (nyawa 0",
            "kalau pemain hancur), lalu entitas yang masih ada, urut nomor,",
            "dalam bentuk dua spasi, nama, dan (x,y). Lalu cetak checksum C.",
            "",
            "Checksum: M = 1000003, h = 0, dan tambah(v) berarti",
            "h = ((h * 31 + v) % M + M) % M. Panggil tambah untuk nomor, x, dan",
            "y tiap entitas yang masih ada (urut nomor), lalu untuk T, S, dan N.",
            "",
            "Replay. Buat dunia baru dari baris entitas yang sama, jalankan",
            "tick-tick dari rekaman input saja tanpa frame dan tanpa mencetak",
            "kejadian, lalu cetak replay K tick: checksum C dan baris",
            "replay cocok kalau checksumnya sama dengan main pertama (replay",
            "beda kalau tidak).",
            "",
            "Contoh input:",
            "  langkah 20",
            "  arena 40 20",
            "  entitas pemain pemain 2 8 2 2 0 0",
            "  entitas koin1 koin 10 8 1 1 0 0",
            "  entitas musuh1 musuh 30 8 2 2 -2 0",
            "  entitas koin2 koin 22 4 1 1 0 0",
            "  entitas musuh2 musuh 20 0 2 2 0 3",
            "  frame 16 kanan",
            "  frame 16 kanan",
            "  frame 33 kanan",
            "  frame 8 kanan",
            "  frame 50 kanan",
            "  frame 40 kanan",
            "  frame 40 atas",
            "  frame 37 kanan",
            "  frame 50 kanan",
            "",
            "Keluaran yang diharapkan:",
            "tick 4: ambil koin1 (skor 10)",
            "tick 7: kena musuh1 (nyawa 2)",
            "tick 12: ambil koin2 (skor 20)",
            "tick 12: semua koin terambil",
            "akhir tick 12: skor 20, nyawa 2",
            "  pemain (22,4)",
            "  musuh2 (20,3)",
            "checksum 894684",
            "replay 12 tick: checksum 894684",
            "replay cocok",
            "",
            "Contoh kedua, pemain diam dan dikeroyok tiga musuh:",
            "  langkah 25",
            "  arena 30 10",
            "  entitas pemain pemain 0 4 2 2 0 0",
            "  entitas musuh1 musuh 10 4 2 2 -2 0",
            "  entitas musuh2 musuh 20 4 2 2 -2 0",
            "  entitas koin1 koin 28 0 1 1 0 0",
            "  entitas musuh3 musuh 27 3 2 2 -3 0",
            "  frame 30 kanan",
            "  frame 30 diam",
            "  frame 60 diam",
            "  frame 45 diam",
            "  frame 70 diam",
            "  frame 100 diam",
            "  frame 100 kanan",
            "",
            "Untuk input langkah 25, keluarannya:",
            "tick 4: kena musuh1 (nyawa 2)",
            "tick 8: kena musuh3 (nyawa 1)",
            "tick 9: kena musuh2 (nyawa 0)",
            "tick 9: pemain kalah",
            "akhir tick 9: skor 0, nyawa 0",
            "  koin1 (28,0)",
            "checksum 383421",
            "replay 9 tick: checksum 383421",
            "replay cocok",
        ],
        "hints": [
            "Pisahkan tiga hal: membaca input jadi data awal, satu fungsi buatDunia() yang menyusun dunia dari data itu, dan satu fungsi satuTick(dunia, input) yang menjalankan semua sistem.",
            "Main pertama dan replay memakai satuTick yang sama; bedanya cuma sumber inputnya (frame lewat akumulator, atau rekaman) dan apakah kejadian dicetak, jadi kirim fungsi pencetak sebagai parameter.",
            "Saat entitas hancur, hapus nomornya dari semua Map komponen, dan selalu ambil daftar nomor yang sudah diurutkan sebelum mengulang, supaya urutan kejadian sama di setiap mesin.",
            "Sisa operator % di JavaScript bisa negatif untuk angka negatif, jadi tambahkan M lalu ambil sisa sekali lagi saat menghitung checksum.",
        ],
        "solution": "const baris = require('fs').readFileSync(0, 'utf8').trim().split('\\n').map((b) => b.trim().split(/\\s+/));\n\nlet LANGKAH = 20;\nlet LEBAR = 0;\nlet TINGGI = 0;\nconst awal = [];\nconst frame = [];\nfor (const k of baris) {\n  if (k[0] === 'langkah') LANGKAH = Number(k[1]);\n  else if (k[0] === 'arena') [LEBAR, TINGGI] = [Number(k[1]), Number(k[2])];\n  else if (k[0] === 'entitas') awal.push(k.slice(1));\n  else if (k[0] === 'frame') frame.push({ ms: Number(k[1]), input: k[2] });\n}\n\nconst ARAH = { kanan: [2, 0], kiri: [-2, 0], atas: [0, -2], bawah: [0, 2], diam: [0, 0] };\n\n// Dunia ECS: satu Map per jenis komponen, dikunci nomor entitas.\nfunction buatDunia() {\n  const d = {\n    nama: new Map(), jenis: new Map(), posisi: new Map(),\n    kotak: new Map(), kecepatan: new Map(), nyawa: new Map(),\n    skor: 0, tick: 0, selesai: false,\n  };\n  awal.forEach(([nama, jenis, x, y, w, h, vx, vy], i) => {\n    const id = i + 1;\n    d.nama.set(id, nama);\n    d.jenis.set(id, jenis);\n    d.posisi.set(id, { x: Number(x), y: Number(y) });\n    d.kotak.set(id, { w: Number(w), h: Number(h) });\n    d.kecepatan.set(id, { x: Number(vx), y: Number(vy) });\n    if (jenis === 'pemain') d.nyawa.set(id, 3);\n  });\n  return d;\n}\n\nfunction ids(peta) {\n  return [...peta.keys()].sort((a, b) => a - b);\n}\n\nfunction hancurkan(d, id) {\n  for (const p of [d.nama, d.jenis, d.posisi, d.kotak, d.kecepatan, d.nyawa]) p.delete(id);\n}\n\nfunction sistemInput(d, input) {\n  for (const id of ids(d.jenis)) {\n    if (d.jenis.get(id) !== 'pemain') continue;\n    const [vx, vy] = ARAH[input] || ARAH.diam;\n    d.kecepatan.set(id, { x: vx, y: vy });\n  }\n}\n\nfunction sistemGerak(d) {\n  for (const id of ids(d.kecepatan)) {\n    const p = d.posisi.get(id);\n    const v = d.kecepatan.get(id);\n    p.x += v.x;\n    p.y += v.y;\n  }\n}\n\nfunction sistemArena(d) {\n  for (const id of ids(d.posisi)) {\n    const p = d.posisi.get(id);\n    const k = d.kotak.get(id);\n    const v = d.kecepatan.get(id);\n    const maksX = LEBAR - k.w;\n    const maksY = TINGGI - k.h;\n    if (p.x < 0 || p.x > maksX) {\n      p.x = Math.min(Math.max(p.x, 0), maksX);\n      if (d.jenis.get(id) === 'musuh') v.x = -v.x;\n    }\n    if (p.y < 0 || p.y > maksY) {\n      p.y = Math.min(Math.max(p.y, 0), maksY);\n      if (d.jenis.get(id) === 'musuh') v.y = -v.y;\n    }\n  }\n}\n\nfunction tabrak(a, ka, b, kb) {\n  return a.x < b.x + kb.w && b.x < a.x + ka.w && a.y < b.y + kb.h && b.y < a.y + ka.h;\n}\n\nfunction sistemTabrakan(d, cetak) {\n  const pemain = ids(d.jenis).find((id) => d.jenis.get(id) === 'pemain');\n  if (pemain === undefined) return;\n  for (const id of ids(d.posisi)) {\n    if (id === pemain || !d.posisi.has(pemain)) continue;\n    if (!tabrak(d.posisi.get(pemain), d.kotak.get(pemain), d.posisi.get(id), d.kotak.get(id))) continue;\n    const nama = d.nama.get(id);\n    if (d.jenis.get(id) === 'koin') {\n      d.skor += 10;\n      hancurkan(d, id);\n      cetak(`ambil ${nama} (skor ${d.skor})`);\n    } else if (d.jenis.get(id) === 'musuh') {\n      const sisa = d.nyawa.get(pemain) - 1;\n      d.nyawa.set(pemain, sisa);\n      hancurkan(d, id);\n      cetak(`kena ${nama} (nyawa ${sisa})`);\n      if (sisa <= 0) {\n        hancurkan(d, pemain);\n        cetak('pemain kalah');\n        d.selesai = true;\n        return;\n      }\n    }\n  }\n  const sisaKoin = ids(d.jenis).filter((id) => d.jenis.get(id) === 'koin').length;\n  if (sisaKoin === 0) {\n    cetak('semua koin terambil');\n    d.selesai = true;\n  }\n}\n\nfunction satuTick(d, input, cetak) {\n  d.tick++;\n  sistemInput(d, input);\n  sistemGerak(d);\n  sistemArena(d);\n  sistemTabrakan(d, (teks) => cetak(`tick ${d.tick}: ${teks}`));\n}\n\nfunction checksum(d) {\n  const M = 1000003;\n  let h = 0;\n  const tambah = (v) => { h = (((h * 31 + v) % M) + M) % M; };\n  for (const id of ids(d.posisi)) {\n    const p = d.posisi.get(id);\n    tambah(id);\n    tambah(p.x);\n    tambah(p.y);\n  }\n  const nyawa = [...d.nyawa.values()][0] || 0;\n  tambah(d.tick);\n  tambah(d.skor);\n  tambah(nyawa);\n  return h;\n}\n\n// Main pertama: frame -> akumulator -> tick, sambil merekam input per tick.\nconst dunia = buatDunia();\nconst rekaman = [];\nlet akumulator = 0;\nfor (const f of frame) {\n  if (dunia.selesai) break;\n  akumulator += f.ms;\n  while (akumulator >= LANGKAH && !dunia.selesai) {\n    akumulator -= LANGKAH;\n    rekaman.push(f.input);\n    satuTick(dunia, f.input, (teks) => console.log(teks));\n  }\n}\nconst nyawaAkhir = [...dunia.nyawa.values()][0] || 0;\nconsole.log(`akhir tick ${dunia.tick}: skor ${dunia.skor}, nyawa ${nyawaAkhir}`);\nfor (const id of ids(dunia.posisi)) {\n  const p = dunia.posisi.get(id);\n  console.log(`  ${dunia.nama.get(id)} (${p.x},${p.y})`);\n}\nconst c1 = checksum(dunia);\nconsole.log(`checksum ${c1}`);\n\n// Replay: dunia baru dari keadaan awal, input diambil dari rekaman saja.\nconst ulang = buatDunia();\nfor (const input of rekaman) satuTick(ulang, input, () => {});\nconst c2 = checksum(ulang);\nconsole.log(`replay ${rekaman.length} tick: checksum ${c2}`);\nconsole.log(c1 === c2 ? 'replay cocok' : 'replay beda');\n",
        "stdin_list": [
            """langkah 20
arena 40 20
entitas pemain pemain 2 8 2 2 0 0
entitas koin1 koin 10 8 1 1 0 0
entitas musuh1 musuh 30 8 2 2 -2 0
entitas koin2 koin 22 4 1 1 0 0
entitas musuh2 musuh 20 0 2 2 0 3
frame 16 kanan
frame 16 kanan
frame 33 kanan
frame 8 kanan
frame 50 kanan
frame 40 kanan
frame 40 atas
frame 37 kanan
frame 50 kanan
""",
            """langkah 25
arena 30 10
entitas pemain pemain 0 4 2 2 0 0
entitas musuh1 musuh 10 4 2 2 -2 0
entitas musuh2 musuh 20 4 2 2 -2 0
entitas koin1 koin 28 0 1 1 0 0
entitas musuh3 musuh 27 3 2 2 -3 0
frame 30 kanan
frame 30 diam
frame 60 diam
frame 45 diam
frame 70 diam
frame 100 diam
frame 100 kanan
""",
        ],
    },
]
