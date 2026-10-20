"""Kurikulum Bahasa Pemrograman Lain.

Dirakit alat/rakit_kurikulum.py dari draf per bab (2026-10-19).
Sesudah dirakit, berkas ini disunting seperti kurikulum lain
(alat/ganti_badan.py, alat/tambah_bagian.py). <KEY>_BAB tetap
spesifikasi JUMLAH; rentangnya dihitung data/kurikulum_tech.py.
"""

BAHASALAIN_EXERCISES = [
    {
        "title": "Latihan 1: Terjemahkan Kode Lua ke Python",
        "difficulty": "Mudah",
        "question": [
            "Program Lua di bawah membaca satu baris berisi bilangan bulat yang",
            "dipisah spasi, lalu mencetak tiap bilangan dengan nomor urutnya dan",
            "rata-ratanya.",
            "",
            "  local baris = io.read(\"l\")",
            "  local nilai = {}",
            "  for angka in baris:gmatch(\"%S+\") do",
            "    nilai[#nilai + 1] = tonumber(angka)",
            "  end",
            "  local total = 0",
            "  for i = 1, #nilai do",
            "    print(i .. \": \" .. nilai[i])",
            "    total = total + nilai[i]",
            "  end",
            "  print(string.format(\"rata-rata: %.1f\", total / #nilai))",
            "",
            "Tulis program Python yang keluarannya persis sama untuk input apa pun.",
            "Ingat, nomor urut di Lua mulai dari 1.",
            "",
            "Untuk input 70 80 90, keluarannya:",
            "1: 70",
            "2: 80",
            "3: 90",
            "rata-rata: 80.0",
        ],
        "hints": [
            "Baris pertama Lua cuma membaca satu baris dari stdin, dan gmatch memecahnya per kata.",
            "Di Python, input().split() lalu int() pada tiap potongan memberi daftar bilangan, dan enumerate bisa mulai dari 1.",
            "Format %.1f di Lua sama dengan f\"{x:.1f}\" di Python.",
        ],
        "solution": """nilai = [int(x) for x in input().split()]
for i, n in enumerate(nilai, start=1):
    print(f"{i}: {n}")
print(f"rata-rata: {sum(nilai) / len(nilai):.1f}")""",
        "stdin_list": [
            """70 80 90
""",
            """65 90 72 89
""",
        ],
    },
    {
        "title": "Latihan 2: Pemeriksa Tipe Mini untuk Ekspresi",
        "difficulty": "Menengah",
        "question": [
            "Buat pemeriksa tipe untuk bahasa mini yang statis dan kuat, tanpa",
            "konversi otomatis. Tiap baris stdin berisi satu ekspresi: operand,",
            "operator, operand, dipisah spasi.",
            "",
            "Operand berupa literal:",
            "  - bilangan bulat (42) bertipe int",
            "  - teks dalam kutip ganda (\"halo dunia\") bertipe str",
            "  - true atau false bertipe bool",
            "",
            "Operator dan aturannya (selain ini galat tipe):",
            "  - int + int, int - int, int * int menghasilkan int",
            "  - str + str menghasilkan str",
            "  - == pada dua operand bertipe sama menghasilkan bool",
            "  - bool and bool menghasilkan bool",
            "",
            "Untuk tiap baris yang tidak kosong, cetak tipe hasilnya. Kalau aturan",
            "tidak terpenuhi, cetak galat tipe: KIRI OP KANAN dengan nama tipe.",
            "Kalau baris tidak berbentuk tiga potong operand-operator-operand yang",
            "sah, cetak galat sintaks.",
            "",
            "Contoh input:",
            "  1 + 2",
            "  \"a b\" + \"c\"",
            "  \"a\" + 1",
            "  true and false",
            "  3 == 3",
            "  \"x\" == 1",
            "  2 * \"ha\"",
            "  true + true",
            "  1 +",
            "",
            "Keluaran yang diharapkan:",
            "int",
            "str",
            "galat tipe: str + int",
            "bool",
            "bool",
            "galat tipe: str == int",
            "galat tipe: int * str",
            "galat tipe: bool + bool",
            "galat sintaks",
        ],
        "hints": [
            "Pisahkan dua pekerjaan: memecah baris jadi token, lalu mencocokkan tipe kiri, operator, dan tipe kanan.",
            "Teks berkutip boleh berisi spasi, jadi split() saja tidak cukup; regex dengan pola \"[^\"]*\" untuk teks, \\d+ untuk angka, dan daftar operator bisa memecahnya.",
            "Simpan aturan sebagai dict berkunci tuple seperti (\"int\", \"+\", \"int\"): \"int\", lalu kunci yang tidak ada berarti galat tipe.",
        ],
        "solution": "import re\nimport sys\n\nTOKEN = re.compile(r'\\s*(\"[^\"]*\"|\\d+|true|false|==|and|[-+*])')\n\nATURAN = {\n    (\"int\", \"+\", \"int\"): \"int\",\n    (\"int\", \"-\", \"int\"): \"int\",\n    (\"int\", \"*\", \"int\"): \"int\",\n    (\"str\", \"+\", \"str\"): \"str\",\n    (\"int\", \"==\", \"int\"): \"bool\",\n    (\"str\", \"==\", \"str\"): \"bool\",\n    (\"bool\", \"==\", \"bool\"): \"bool\",\n    (\"bool\", \"and\", \"bool\"): \"bool\",\n}\n\n\ndef tipe_literal(t):\n    if t.startswith('\"'):\n        return \"str\"\n    if t.isdigit():\n        return \"int\"\n    if t in (\"true\", \"false\"):\n        return \"bool\"\n    return None\n\n\ndef periksa(baris):\n    token, pos = [], 0\n    while pos < len(baris):\n        m = TOKEN.match(baris, pos)\n        if not m:\n            return \"galat sintaks\"\n        token.append(m.group(1))\n        pos = m.end()\n    if len(token) != 3:\n        return \"galat sintaks\"\n    kiri, op, kanan = token\n    tk, tn = tipe_literal(kiri), tipe_literal(kanan)\n    if tk is None or tn is None or tipe_literal(op) is not None:\n        return \"galat sintaks\"\n    hasil = ATURAN.get((tk, op, tn))\n    if hasil is None:\n        return f\"galat tipe: {tk} {op} {tn}\"\n    return hasil\n\n\nfor baris in sys.stdin:\n    baris = baris.strip()\n    if baris:\n        print(periksa(baris))",
        "stdin_list": [
            """1 + 2
"a b" + "c"
"a" + 1
true and false
3 == 3
"x" == 1
2 * "ha"
true + true
1 +
""",
            """10 - 4
false == true
"ok" and true
7 7 7
"tes" == "tes"
""",
        ],
    },
    {
        "title": "Latihan 3: Pipeline Objek ala PowerShell di Python",
        "difficulty": "Mudah",
        "question": [
            "Di PowerShell, pipeline ini memilih proses yang boros CPU:",
            "",
            "  Import-Csv proses.csv |",
            "      Where-Object { [double]$_.cpu -gt 10 } |",
            "      Sort-Object { [double]$_.cpu } -Descending |",
            "      Select-Object nama, cpu",
            "",
            "Tiru di Python. Stdin berisi CSV dengan baris kepala nama,cpu,memori.",
            "Tulis tiga fungsi kecil yang dirangkai atas daftar dict:",
            "  - where_object: sisakan baris yang cpu-nya (sebagai angka) di atas 10",
            "  - sort_object: urutkan cpu dari besar ke kecil; kalau sama, nama naik",
            "  - select_object: sisakan kolom nama dan cpu saja",
            "",
            "Cetak tabel seperti PowerShell: baris kepala, baris garis, lalu data.",
            "Kolom nama rata kiri selebar isi terpanjangnya (minimal selebar kata",
            "nama). Kolom cpu rata kanan selebar isi terpanjangnya (minimal selebar",
            "kata cpu), ditulis persis seperti di CSV. Dua kolom dipisah satu",
            "spasi. Baris garis berisi ---- di bawah nama dan --- di bawah cpu.",
            "",
            "Contoh input:",
            "  nama,cpu,memori",
            "  firefox,35.2,820",
            "  code,12.5,640",
            "  bash,0.1,5",
            "  gnome-shell,18.0,410",
            "",
            "Keluaran yang diharapkan:",
            "nama         cpu",
            "----         ---",
            "firefox     35.2",
            "gnome-shell 18.0",
            "code        12.5",
        ],
        "hints": [
            "Baca semua baris, pecah baris kepala jadi nama kolom, lalu pakai zip untuk mengubah tiap baris data jadi dict.",
            "Simpan cpu tetap sebagai teks untuk dicetak, dan ubah ke float hanya saat membandingkan dan mengurutkan.",
            "Kunci urut (-float(x[\"cpu\"]), x[\"nama\"]) memberi urutan cpu turun lalu nama naik, dan ljust serta rjust mengatur rata kiri dan kanan.",
        ],
        "solution": """import sys

baris = [b.strip() for b in sys.stdin if b.strip()]
kepala = baris[0].split(",")
data = [dict(zip(kepala, b.split(","))) for b in baris[1:]]


def where_object(data, syarat):
    return [x for x in data if syarat(x)]


def sort_object(data, kunci):
    return sorted(data, key=kunci)


def select_object(data, kolom):
    return [{k: x[k] for k in kolom} for x in data]


hasil = where_object(data, lambda x: float(x["cpu"]) > 10)
hasil = sort_object(hasil, lambda x: (-float(x["cpu"]), x["nama"]))
hasil = select_object(hasil, ["nama", "cpu"])

lebar_nama = max([len("nama")] + [len(x["nama"]) for x in hasil])
lebar_cpu = max([len("cpu")] + [len(x["cpu"]) for x in hasil])
print("nama".ljust(lebar_nama), "cpu".rjust(lebar_cpu))
print("----".ljust(lebar_nama), "---".rjust(lebar_cpu))
for x in hasil:
    print(x["nama"].ljust(lebar_nama), x["cpu"].rjust(lebar_cpu))""",
        "stdin_list": [
            """nama,cpu,memori
firefox,35.2,820
code,12.5,640
bash,0.1,5
gnome-shell,18.0,410
""",
            """nama,cpu,memori
python3,10.0,120
node,47.25,300
java,47.25,900
sshd,3.5,8
""",
        ],
    },
    {
        "title": "Latihan 4: Ringkasan Log dengan Regex ala Perl",
        "difficulty": "Menengah",
        "question": [
            "One-liner Perl ini menghitung jumlah tiap level di berkas log, lalu",
            "mengurutkannya dari yang terbanyak:",
            "",
            "  perl -ne '$n{$1}++ if /^\\S+ \\S+ (\\w+) \\[/;",
            "    END { print \"$_ $n{$_}\\n\"",
            "      for sort { $n{$b} <=> $n{$a} || $a cmp $b } keys %n }' app.log",
            "",
            "Buat versi Python yang lebih lengkap memakai modul re. Tiap baris log",
            "yang sah berbentuk:",
            "",
            "  TANGGAL JAM LEVEL [IP] pesan",
            "",
            "dengan LEVEL salah satu dari ERROR, WARN, INFO, DEBUG dan IP berupa",
            "empat bilangan dipisah titik di dalam kurung siku. Baris kosong",
            "dilewati. Baris lain yang tidak cocok dihitung sebagai diabaikan.",
            "",
            "Cetak tiga bagian: hitungan per level, hitungan per IP, lalu jumlah",
            "baris yang diabaikan. Di dua bagian pertama, urutkan dari jumlah",
            "terbanyak; kalau sama, urutkan namanya secara abjad (perbandingan",
            "teks biasa).",
            "",
            "Contoh input:",
            "  2026-10-01 12:00:01 ERROR [10.0.0.5] disk penuh",
            "  2026-10-01 12:00:07 INFO [10.0.0.9] login berhasil",
            "  2026-10-01 12:01:12 ERROR [10.0.0.5] disk penuh",
            "  2026-10-01 12:02:40 WARN [10.0.0.7] memori 85%",
            "  baris rusak tanpa format",
            "  2026-10-01 12:03:02 INFO [10.0.0.9] logout",
            "  2026-10-01 12:04:15 ERROR [10.0.0.9] timeout ke database",
            "",
            "Keluaran yang diharapkan:",
            "per level:",
            "ERROR 3",
            "INFO 2",
            "WARN 1",
            "per IP:",
            "10.0.0.9 3",
            "10.0.0.5 2",
            "10.0.0.7 1",
            "diabaikan: 1",
        ],
        "hints": [
            "Satu pola regex dengan dua kelompok tangkapan cukup untuk mengambil level dan IP sekaligus dari tiap baris.",
            "Pola ^\\S+ \\S+ (ERROR|WARN|INFO|DEBUG) \\[(\\d+(?:\\.\\d+){3})\\] dengan re.match menolak baris yang bentuknya lain.",
            "Hitung dengan dua dict, lalu urutkan item-nya memakai kunci (-jumlah, nama) supaya jumlah turun dan nama naik.",
        ],
        "solution": "import re\nimport sys\n\nPOLA = re.compile(r\"^\\S+ \\S+ (ERROR|WARN|INFO|DEBUG) \\[(\\d+(?:\\.\\d+){3})\\]\")\n\nper_level, per_ip, diabaikan = {}, {}, 0\nfor baris in sys.stdin:\n    baris = baris.strip()\n    if not baris:\n        continue\n    m = POLA.match(baris)\n    if not m:\n        diabaikan += 1\n        continue\n    level, ip = m.groups()\n    per_level[level] = per_level.get(level, 0) + 1\n    per_ip[ip] = per_ip.get(ip, 0) + 1\n\n\ndef cetak(judul, hitung):\n    print(judul)\n    for kunci, n in sorted(hitung.items(), key=lambda kv: (-kv[1], kv[0])):\n        print(f\"{kunci} {n}\")\n\n\ncetak(\"per level:\", per_level)\ncetak(\"per IP:\", per_ip)\nprint(f\"diabaikan: {diabaikan}\")",
        "stdin_list": [
            """2026-10-01 12:00:01 ERROR [10.0.0.5] disk penuh
2026-10-01 12:00:07 INFO [10.0.0.9] login berhasil
2026-10-01 12:01:12 ERROR [10.0.0.5] disk penuh
2026-10-01 12:02:40 WARN [10.0.0.7] memori 85%
baris rusak tanpa format
2026-10-01 12:03:02 INFO [10.0.0.9] logout
2026-10-01 12:04:15 ERROR [10.0.0.9] timeout ke database
""",
            """2026-10-02 08:00:00 DEBUG [192.168.1.20] mulai
2026-10-02 08:00:01 DEBUG [192.168.1.3] mulai
2026-10-02 08:00:02 TRACE [192.168.1.3] level tak dikenal

2026-10-02 08:00:03 WARN [192.168.1.20] lambat
2026-10-02 08:00:04 INFO [10.1.2] ip rusak
""",
        ],
    },
    {
        "title": "Latihan 5: Pewarisan Prototipe lewat __index",
        "difficulty": "Menengah",
        "question": [
            "Tiru cara Lua mencari kunci lewat rantai __index. Setiap objek punya",
            "isi sendiri (pasangan kunci dan nilai) dan paling banyak satu induk.",
            "Stdin berisi perintah, satu per baris:",
            "",
            "  objek NAMA            buat objek kosong tanpa induk",
            "  set NAMA KUNCI NILAI  isi kunci di objek itu (NILAI = sisa baris)",
            "  induk NAMA INDUK      jadikan INDUK sebagai induk NAMA",
            "  get NAMA KUNCI        cari kunci, telusuri induk kalau perlu",
            "",
            "Keluaran hanya untuk get dan galat:",
            "  - ketemu di objek itu sendiri: NAMA.KUNCI = NILAI",
            "  - ketemu di induk (seberapa jauh pun): NAMA.KUNCI = NILAI (dari X),",
            "    dengan X nama objek tempat kunci ditemukan",
            "  - tidak ketemu di mana pun: NAMA.KUNCI = nil",
            "  - rantai kembali ke objek yang sudah dikunjungi sebelum kunci",
            "    ketemu: galat: rantai __index melingkar",
            "  - perintah menyebut objek yang belum dibuat: galat: objek X belum",
            "    dibuat (X adalah nama pertama yang belum ada)",
            "  - objek NAMA untuk nama yang sudah ada: galat: objek X sudah ada",
            "",
            "Contoh input:",
            "  objek hewan",
            "  set hewan kaki 4",
            "  objek kucing",
            "  induk kucing hewan",
            "  set kucing suara meong",
            "  get kucing suara",
            "  get kucing kaki",
            "  get kucing sayap",
            "  objek oyen",
            "  induk oyen kucing",
            "  get oyen kaki",
            "  induk hewan oyen",
            "  get oyen sayap",
            "  get budi kaki",
            "",
            "Keluaran yang diharapkan:",
            "kucing.suara = meong",
            "kucing.kaki = 4 (dari hewan)",
            "kucing.sayap = nil",
            "oyen.kaki = 4 (dari hewan)",
            "galat: rantai __index melingkar",
            "galat: objek budi belum dibuat",
        ],
        "hints": [
            "Simpan semua objek di satu dict: nama objek menunjuk ke dict isi dan nama induknya.",
            "Pencarian adalah loop yang berpindah ke induk selama kunci belum ketemu dan induknya bukan None.",
            "Catat nama yang sudah dikunjungi di sebuah set; kalau nama berikutnya sudah ada di set itu, rantainya melingkar.",
        ],
        "solution": """import sys

objek = {}


def cari(nama, kunci):
    dikunjungi = set()
    sekarang = nama
    while sekarang is not None:
        if sekarang in dikunjungi:
            return "galat: rantai __index melingkar"
        dikunjungi.add(sekarang)
        isi = objek[sekarang]["isi"]
        if kunci in isi:
            if sekarang == nama:
                return f"{nama}.{kunci} = {isi[kunci]}"
            return f"{nama}.{kunci} = {isi[kunci]} (dari {sekarang})"
        sekarang = objek[sekarang]["induk"]
    return f"{nama}.{kunci} = nil"


def belum_ada(*nama):
    for n in nama:
        if n not in objek:
            print(f"galat: objek {n} belum dibuat")
            return True
    return False


for baris in sys.stdin:
    bagian = baris.split(maxsplit=3)
    if not bagian:
        continue
    perintah = bagian[0]
    if perintah == "objek":
        if bagian[1] in objek:
            print(f"galat: objek {bagian[1]} sudah ada")
        else:
            objek[bagian[1]] = {"isi": {}, "induk": None}
    elif perintah == "set":
        if not belum_ada(bagian[1]):
            objek[bagian[1]]["isi"][bagian[2]] = bagian[3].strip()
    elif perintah == "induk":
        if not belum_ada(bagian[1], bagian[2]):
            objek[bagian[1]]["induk"] = bagian[2]
    elif perintah == "get":
        if not belum_ada(bagian[1]):
            print(cari(bagian[1], bagian[2]))""",
        "stdin_list": [
            """objek hewan
set hewan kaki 4
objek kucing
induk kucing hewan
set kucing suara meong
get kucing suara
get kucing kaki
get kucing sayap
objek oyen
induk oyen kucing
get oyen kaki
induk hewan oyen
get oyen sayap
get budi kaki
""",
            """objek dasar
set dasar warna abu abu
objek tombol
induk tombol dasar
set tombol teks Simpan data
get tombol warna
get tombol teks
objek tombol
induk tombol jendela
set dasar teks kosong
get tombol teks
get dasar teks
""",
        ],
    },
    {
        "title": "Latihan 6: Game Loop dan Signal ala Godot",
        "difficulty": "Menengah",
        "question": [
            "Simulasikan game loop dengan delta tetap dan satu signal. Stdin berisi",
            "baris pengaturan, urutannya bebas:",
            "",
            "  frame N        jumlah frame yang disimulasikan",
            "  delta MS       lama satu frame dalam milidetik (bilangan bulat)",
            "  kecepatan V    kecepatan benda dalam satuan per detik (bilangan bulat)",
            "  batas B        posisi batas (bilangan bulat)",
            "  hubungkan NAMA hubungkan handler NAMA ke signal sampai",
            "",
            "Benda mulai di posisi 0. Supaya bebas galat pembulatan, simpan posisi",
            "sebagai bilangan bulat dalam seperseribu satuan: tiap frame posisi",
            "bertambah V x MS. Cetak posisi dengan tiga angka desimal, misalnya",
            "posisi 1120 seperseribu ditulis 1.120.",
            "",
            "Aturan keluaran:",
            "  - Saat membaca, hubungkan untuk nama yang sudah terhubung mencetak",
            "    galat: NAMA sudah terhubung dan tidak menambah apa pun (Godot juga",
            "    menolak menghubungkan fungsi yang sama dua kali).",
            "  - Tiap frame cetak frame I: x=POSISI (I mulai dari 1).",
            "  - Di frame pertama posisi mencapai atau melewati batas, sesudah baris",
            "    frame itu cetak sinyal sampai dipancarkan, lalu tiap handler sesuai",
            "    urutan dihubungkan mencetak dua spasi, NAMA menerima sampai di",
            "    frame I. Signal hanya dipancarkan sekali.",
            "  - Kalau sampai frame terakhir signal tidak pernah dipancarkan, cetak",
            "    sinyal sampai tidak pernah dipancarkan di akhir.",
            "",
            "Contoh input:",
            "  frame 6",
            "  delta 250",
            "  kecepatan 120",
            "  batas 100",
            "  hubungkan hud",
            "  hubungkan suara",
            "  hubungkan hud",
            "",
            "Keluaran yang diharapkan:",
            "galat: hud sudah terhubung",
            "frame 1: x=30.000",
            "frame 2: x=60.000",
            "frame 3: x=90.000",
            "frame 4: x=120.000",
            "sinyal sampai dipancarkan",
            "  hud menerima sampai di frame 4",
            "  suara menerima sampai di frame 4",
            "frame 5: x=150.000",
            "frame 6: x=180.000",
        ],
        "hints": [
            "Pisahkan dua tahap: baca semua pengaturan dulu, baru jalankan loop frame sesudahnya.",
            "Daftar handler cukup berupa list nama, dan sebuah variabel boolean mencatat apakah signal sudah pernah dipancarkan.",
            "Dengan posisi p dalam seperseribu, tiga desimal bisa dicetak tanpa float lewat f\"{p // 1000}.{p % 1000:03d}\", dan batas dibandingkan sebagai p >= batas * 1000.",
        ],
        "solution": """import sys

atur = {"frame": 0, "delta": 0, "kecepatan": 0, "batas": 0}
handler = []
for baris in sys.stdin:
    bagian = baris.split()
    if not bagian:
        continue
    if bagian[0] == "hubungkan":
        nama = bagian[1]
        if nama in handler:
            print(f"galat: {nama} sudah terhubung")
        else:
            handler.append(nama)
    else:
        atur[bagian[0]] = int(bagian[1])

posisi = 0
sudah = False
for i in range(1, atur["frame"] + 1):
    posisi += atur["kecepatan"] * atur["delta"]
    print(f"frame {i}: x={posisi // 1000}.{posisi % 1000:03d}")
    if not sudah and posisi >= atur["batas"] * 1000:
        sudah = True
        print("sinyal sampai dipancarkan")
        for nama in handler:
            print(f"  {nama} menerima sampai di frame {i}")
if not sudah:
    print("sinyal sampai tidak pernah dipancarkan")""",
        "stdin_list": [
            """frame 6
delta 250
kecepatan 120
batas 100
hubungkan hud
hubungkan suara
hubungkan hud
""",
            """hubungkan skor
kecepatan 70
delta 16
frame 5
batas 10
""",
        ],
    },
    {
        "title": "Latihan 7: Optional Chaining dan ?? ala Swift",
        "difficulty": "Menengah",
        "question": [
            "Di Swift, pengguna?.alamat?.kota ?? \"tidak diketahui\" berhenti jadi",
            "nil begitu salah satu bagian kosong, lalu ?? memberi nilai cadangan.",
            "Sebaliknya, pengguna!.alamat membuka paksa dan crash kalau pengguna",
            "nil. Tiru aturan ini di Python.",
            "",
            "Baris pertama stdin berisi satu objek JSON. Baris sesudahnya berisi",
            "query, satu per baris, berbentuk JALUR atau JALUR ?? CADANGAN.",
            "",
            "JALUR diawali satu nama kunci di objek teratas, lalu diikuti potongan",
            "?.kunci atau !.kunci. Nilai awal adalah isi kunci pertama (nil kalau",
            "tidak ada). Untuk setiap potongan, lihat nilai saat ini:",
            "  - ?.kunci: kalau nilai saat ini nil, seluruh jalur langsung nil.",
            "  - !.kunci: kalau nilai saat ini nil, cetak galat: NAMA bernilai nil",
            "    dengan NAMA kunci terakhir yang diambil, lalu lanjut ke query",
            "    berikutnya. ?? tidak menyelamatkan galat ini.",
            "  - Kalau tidak nil, ambil kunci dari nilai itu. Kalau nilainya bukan",
            "    objek atau kuncinya tidak ada, hasilnya nil.",
            "",
            "null di JSON dianggap nil. CADANGAN adalah literal JSON (teks berkutip,",
            "angka, true, false) dan dipakai kalau hasil jalur nil.",
            "",
            "Cara mencetak hasil: nil ditulis nil, teks apa adanya tanpa kutip,",
            "true dan false huruf kecil, angka apa adanya, objek dan daftar sebagai",
            "JSON (json.dumps dengan ensure_ascii=False).",
            "",
            "Contoh input:",
            "  {\"pengguna\": {\"nama\": \"Ani\", \"alamat\": {\"kota\": \"Bandung\"}, \"hp\": null}, \"tamu\": null}",
            "  pengguna?.alamat?.kota",
            "  pengguna?.alamat?.kodepos ?? \"belum diisi\"",
            "  tamu?.nama",
            "  tamu?.nama ?? \"anonim\"",
            "  pengguna?.hp ?? 0",
            "  pengguna?.hp!.nomor",
            "  pengguna?.alamat",
            "  tamu!.nama ?? \"x\"",
            "",
            "Keluaran yang diharapkan:",
            "Bandung",
            "belum diisi",
            "nil",
            "anonim",
            "0",
            "galat: hp bernilai nil",
            "{\"kota\": \"Bandung\"}",
            "galat: tamu bernilai nil",
        ],
        "hints": [
            "Pecah tiap query jadi jalur dan cadangan dulu, lalu pecah jalur jadi nama pertama dan pasangan tanda serta kunci.",
            "re.split(r\"(\\?\\.|!\\.)\", jalur) memisahkan jalur sambil menyimpan tandanya, sehingga tanda ada di indeks ganjil dan kunci di indeks genap.",
            "Untuk galat, lempar exception buatanmu sendiri dari fungsi evaluasi dan tangkap di loop query, jadi ?? tidak pernah sempat dipakai.",
        ],
        "solution": "import json\nimport re\nimport sys\n\n\nclass NilPaksa(Exception):\n    pass\n\n\ndef tampil(v):\n    if v is None:\n        return \"nil\"\n    if isinstance(v, bool):\n        return \"true\" if v else \"false\"\n    if isinstance(v, str):\n        return v\n    if isinstance(v, (dict, list)):\n        return json.dumps(v, ensure_ascii=False)\n    return str(v)\n\n\ndef evaluasi(data, jalur):\n    potong = re.split(r\"(\\?\\.|!\\.)\", jalur.strip())\n    nama = potong[0]\n    v = data.get(nama)\n    for i in range(1, len(potong), 2):\n        tanda, kunci = potong[i], potong[i + 1]\n        if v is None:\n            if tanda == \"?.\":\n                return None\n            raise NilPaksa(nama)\n        v = v.get(kunci) if isinstance(v, dict) else None\n        nama = kunci\n    return v\n\n\nbaris = sys.stdin.read().splitlines()\ndata = json.loads(baris[0])\nfor query in baris[1:]:\n    if not query.strip():\n        continue\n    jalur, _, cadangan = query.partition(\" ?? \")\n    try:\n        hasil = evaluasi(data, jalur)\n    except NilPaksa as e:\n        print(f\"galat: {e} bernilai nil\")\n        continue\n    if hasil is None and cadangan:\n        hasil = json.loads(cadangan)\n    print(tampil(hasil))",
        "stdin_list": [
            """{"pengguna": {"nama": "Ani", "alamat": {"kota": "Bandung"}, "hp": null}, "tamu": null}
pengguna?.alamat?.kota
pengguna?.alamat?.kodepos ?? "belum diisi"
tamu?.nama
tamu?.nama ?? "anonim"
pengguna?.hp ?? 0
pengguna?.hp!.nomor
pengguna?.alamat
tamu!.nama ?? "x"
""",
            """{"toko": {"nama": "Kopi Senja", "pemilik": {"nama": "Budi", "hp": "0812"}, "cabang": ["Bandung", "Cimahi"], "buka": true, "diskon": null}}
toko?.nama
toko?.pemilik?.hp
toko?.cabang
toko?.buka
toko?.diskon ?? 0
toko?.pemilik!.email ?? "kosong"
toko?.diskon!.persen
gudang?.alamat ?? "tidak ada gudang"
toko?.nama?.panjang
""",
        ],
    },
    {
        "title": "Latihan 8: Urutan Event Loop ala Dart",
        "difficulty": "Menengah",
        "question": [
            "Program Dart ini mencetak A, G, E, F, B, C, D:",
            "",
            "  import 'dart:async';",
            "",
            "  void main() {",
            "    print('A');",
            "    Future(() {",
            "      print('B');",
            "      scheduleMicrotask(() => print('C'));",
            "      Future(() => print('D'));",
            "    });",
            "    scheduleMicrotask(() => print('E'));",
            "    Future.value().then((_) => print('F'));",
            "    print('G');",
            "  }",
            "",
            "Buat simulator event loop Dart di Python. Tiap baris stdin adalah",
            "satu pernyataan di main, berbentuk JENIS TEKS dengan JENIS salah satu:",
            "  - print: cetak TEKS saat itu juga",
            "  - microtask: jadwalkan callback di antrean microtask",
            "  - then: sama dengan microtask (callback then dari Future.value())",
            "  - future: jadwalkan callback di antrean event",
            "",
            "Callback dari microtask, then, dan future mencetak TEKS-nya waktu",
            "dijalankan. Sesudah TEKS boleh ada isi callback, ditulis setelah tanda",
            "|, misalnya future B | microtask C | future D. Isi callback dijalankan",
            "berurutan tepat setelah TEKS callback dicetak, dan isinya sendiri",
            "tidak bersarang lagi.",
            "",
            "Urutan kerja: jalankan semua baris main, kosongkan antrean microtask",
            "(termasuk microtask baru yang muncul selama itu), lalu ambil satu",
            "event, jalankan, kosongkan microtask lagi, dan seterusnya sampai",
            "antrean event kosong.",
            "",
            "Contoh input (setara program di atas):",
            "  print A",
            "  future B | microtask C | future D",
            "  microtask E",
            "  then F",
            "  print G",
            "",
            "Keluaran yang diharapkan:",
            "A",
            "G",
            "E",
            "F",
            "B",
            "C",
            "D",
        ],
        "hints": [
            "Dua antrean FIFO cukup, dan collections.deque memberi append serta popleft yang cepat.",
            "Simpan callback sebagai pasangan (teks, daftar isi), dengan isi berupa daftar pernyataan (jenis, teks) hasil memecah baris di tanda |.",
            "Fungsi kuras() mengambil microtask sampai antreannya kosong; panggil sekali sesudah main dan sekali lagi sesudah setiap event.",
        ],
        "solution": """import sys
from collections import deque

microtask = deque()
event = deque()


def urai(teks):
    jenis, _, isi = teks.strip().partition(" ")
    return jenis, isi.strip()


def jalankan(pernyataan, isi_callback):
    jenis, teks = pernyataan
    if jenis == "print":
        print(teks)
    elif jenis in ("microtask", "then"):
        microtask.append((teks, isi_callback))
    elif jenis == "future":
        event.append((teks, isi_callback))


def panggil(teks, isi_callback):
    print(teks)
    for p in isi_callback:
        jalankan(p, [])


def kuras():
    while microtask:
        panggil(*microtask.popleft())


for baris in sys.stdin:
    if not baris.strip():
        continue
    bagian = [urai(b) for b in baris.split("|")]
    jalankan(bagian[0], bagian[1:])
kuras()
while event:
    panggil(*event.popleft())
    kuras()""",
        "stdin_list": [
            """print A
future B | microtask C | future D
microtask E
then F
print G
""",
            """microtask M1 | microtask M2 | future F2
print P1
future F1 | then T1
then T2 | print dalam-T2
print P2
""",
        ],
    },
    {
        "title": "Latihan 9: Daur Ulang Vektor ala R",
        "difficulty": "Menengah",
        "question": [
            "Di R, dua vektor yang panjangnya berbeda tetap bisa dijumlahkan. Vektor",
            "yang lebih pendek diulang (didaur ulang) sampai sepanjang vektor yang",
            "lebih panjang:",
            "",
            "  > c(1, 2, 3, 4) + c(10, 20)",
            "  [1] 11 22 13 24",
            "",
            "Kalau panjang yang lebih panjang bukan kelipatan panjang yang lebih",
            "pendek, hasilnya tetap dihitung tapi R memberi peringatan.",
            "",
            "Tulis program Python yang meniru aturan ini. Masukan tiga baris:",
            "",
            "  baris 1: vektor kiri, bilangan bulat dipisah spasi",
            "  baris 2: operator, salah satu dari + - *",
            "  baris 3: vektor kanan, bilangan bulat dipisah spasi",
            "",
            "Cetak hasilnya dengan format R: \"[1] \" lalu angka-angka dipisah satu",
            "spasi. Kalau panjangnya nggak habis dibagi, cetak di baris berikutnya:",
            "",
            "  Peringatan: panjang objek lebih panjang bukan kelipatan panjang objek lebih pendek",
            "",
            "Kedua vektor selalu berisi minimal satu angka.",
            "",
            "Untuk input 1 2 3 4, keluarannya:",
            "  [1] 11 22 13 24",
            "",
            "Untuk input 1 2 3, keluarannya:",
            "  [1] 10 40 30",
            "  Peringatan: panjang objek lebih panjang bukan kelipatan panjang objek lebih pendek",
            "",
            "Untuk input 5, keluarannya:",
            "  [1] 4 3 2",
        ],
        "hints": [
            "Panjang hasil sama dengan panjang vektor yang lebih panjang, dan elemen ke-i diambil dari posisi i yang 'berputar' di tiap vektor.",
            "Operator sisa bagi (%) membuat indeks berputar: elemen ke-i vektor a adalah a[i % len(a)].",
            "Simpan operator dalam dict berisi lambda, lalu periksa panjang_besar % panjang_kecil untuk memutuskan peringatan.",
        ],
        "stdin_list": [
            """1 2 3 4
+
10 20
""",
            """1 2 3
*
10 20
""",
            """5
-
1 2 3
""",
        ],
        "solution": """kiri = [int(x) for x in input().split()]
op = input().strip()
kanan = [int(x) for x in input().split()]

hitung = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
}[op]

n = max(len(kiri), len(kanan))
hasil = [hitung(kiri[i % len(kiri)], kanan[i % len(kanan)])
         for i in range(n)]
print('[1] ' + ' '.join(str(x) for x in hasil))
if n % min(len(kiri), len(kanan)) != 0:
    print('Peringatan: panjang objek lebih panjang bukan kelipatan '
          'panjang objek lebih pendek')
""",
    },
    {
        "title": "Latihan 10: Pipeline Data ala dplyr",
        "difficulty": "Lanjut",
        "question": [
            "Analis di kantormu menulis pipeline R ini:",
            "",
            "  nilai |>",
            "    filter(hadir >= 10) |>",
            "    mutate(akhir = 0.4 * tugas + 0.6 * ujian) |>",
            "    group_by(kelas) |>",
            "    summarise(rata = mean(akhir), n = n()) |>",
            "    arrange(desc(rata))",
            "",
            "Tulis padanannya di Python tanpa paket tambahan. Masukan berupa CSV dari",
            "stdin dengan baris judul nama,kelas,tugas,ujian,hadir (semua nilai",
            "bilangan bulat). Langkahnya:",
            "",
            "  1. buang siswa yang hadir kurang dari 10;",
            "  2. hitung akhir = 0.4 * tugas + 0.6 * ujian;",
            "  3. kelompokkan per kelas, hitung rata-rata akhir dan banyak siswa;",
            "  4. urutkan menurut rata-rata (dibulatkan dua desimal) dari besar",
            "     ke kecil; kalau sama, menurut nama kelas A sampai Z.",
            "",
            "Cetak baris judul \"kelas rata n\", lalu satu baris per kelas dengan",
            "rata-rata dua desimal. Kelas yang semua siswanya terbuang nggak dicetak.",
            "",
            "Untuk input nama,kelas,tugas,ujian,hadir, keluarannya:",
            "  kelas rata n",
            "  B 87.00 2",
            "  C 87.00 1",
            "  A 79.67 3",
        ],
        "hints": [
            "Pecah pekerjaannya jadi fungsi kecil yang masing-masing menerima daftar dict dan mengembalikan daftar baru, persis seperti satu langkah pipe.",
            "csv.DictReader(sys.stdin) memberi satu dict per baris; ingat semua nilainya masih teks, jadi ubah dengan int() sebelum dihitung.",
            "Untuk urutan, pakai sorted dengan key=lambda r: (-round(r[1], 2), r[0]) supaya rata-rata besar di depan dan kelas yang seri urut abjad.",
        ],
        "stdin_list": [
            """nama,kelas,tugas,ujian,hadir
Ani,A,80,90,14
Budi,B,70,60,9
Citra,A,90,85,13
Dodi,B,85,80,12
Eka,A,60,70,11
Fajar,C,75,95,10
Gita,B,95,90,15
""",
            """nama,kelas,tugas,ujian,hadir
Hana,X,100,80,12
Indra,Y,50,50,8
Joko,X,70,75,10
Kiki,Z,65,90,9
Lina,Y,88,92,11
""",
        ],
        "solution": """import csv
import sys


def saring(baris):
    return [b for b in baris if int(b['hadir']) >= 10]


def tambah_akhir(baris):
    return [dict(b, akhir=0.4 * int(b['tugas']) + 0.6 * int(b['ujian']))
            for b in baris]


def kelompokkan(baris):
    grup = {}
    for b in baris:
        grup.setdefault(b['kelas'], []).append(b['akhir'])
    return grup


def ringkas(grup):
    return [(k, sum(v) / len(v), len(v)) for k, v in grup.items()]


def urutkan(hasil):
    return sorted(hasil, key=lambda r: (-round(r[1], 2), r[0]))


data = list(csv.DictReader(sys.stdin))
hasil = urutkan(ringkas(kelompokkan(tambah_akhir(saring(data)))))
print('kelas rata n')
for kelas, rata, n in hasil:
    print(f'{kelas} {rata:.2f} {n}')
""",
    },
    {
        "title": "Latihan 11: Hierarki Bentuk dan Match ala Scala",
        "difficulty": "Lanjut",
        "question": [
            "Kode Scala ini memodelkan bangun datar dengan sealed trait dan case class,",
            "lalu memilih rumus luas dengan match:",
            "",
            "  sealed trait Bentuk",
            "  case class Lingkaran(r: Double) extends Bentuk",
            "  case class Persegi(sisi: Double) extends Bentuk",
            "  case class Segitiga(a: Double, b: Double, c: Double) extends Bentuk",
            "",
            "  def luas(b: Bentuk): Double = b match",
            "    case Lingkaran(r)      => math.Pi * r * r",
            "    case Persegi(s)        => s * s",
            "    case Segitiga(a, b, c) =>",
            "      val s = (a + b + c) / 2",
            "      math.sqrt(s * (s - a) * (s - b) * (s - c))",
            "",
            "Tulis padanannya di Python dengan dataclass dan match-case (pola kelas).",
            "Setiap baris masukan berisi nama bentuk lalu ukurannya: lingkaran r,",
            "persegi sisi, atau segitiga a b c.",
            "",
            "Untuk tiap baris, cetak \"<nama>: luas <luas dua desimal> (<kategori>)\".",
            "Kategori: besar kalau luas >= 20, sedang kalau >= 10, selain itu kecil.",
            "Dua kasus khusus:",
            "",
            "  - segitiga yang sisi terpanjangnya >= jumlah dua sisi lain dicetak",
            "    \"segitiga: tidak sah\" (pakai guard di case);",
            "  - nama yang tidak dikenal dicetak \"tidak dikenal: <nama>\".",
            "",
            "Untuk input lingkaran 3, keluarannya:",
            "  lingkaran: luas 28.27 (besar)",
            "  persegi: luas 16.00 (sedang)",
            "  segitiga: luas 6.00 (kecil)",
            "  segitiga: tidak sah",
            "  tidak dikenal: trapesium",
            "",
            "Untuk input persegi 5, keluarannya:",
            "  persegi: luas 25.00 (besar)",
            "  lingkaran: luas 3.14 (kecil)",
            "  segitiga: luas 12.00 (sedang)",
        ],
        "hints": [
            "Buat satu dataclass per bentuk, lalu fungsi luas yang memakai match-case dengan pola kelas seperti case Lingkaran(r=r).",
            "Pola kelas butuh __match_args__ supaya bisa ditulis posisional; dataclass membuatkannya otomatis, jadi case Persegi(s) langsung jalan.",
            "Untuk segitiga tidak sah, taruh case dengan guard if lebih dulu: case Segitiga(a, b, c) if max(a, b, c) >= a + b + c - max(a, b, c).",
        ],
        "stdin_list": [
            """lingkaran 3
persegi 4
segitiga 3 4 5
segitiga 1 2 10
trapesium 1 2
""",
            """persegi 5
lingkaran 1
segitiga 5 5 6
""",
        ],
        "solution": """import math
import sys
from dataclasses import dataclass


@dataclass
class Lingkaran:
    r: float


@dataclass
class Persegi:
    sisi: float


@dataclass
class Segitiga:
    a: float
    b: float
    c: float


def buat(nama, angka):
    match nama:
        case 'lingkaran':
            return Lingkaran(*angka)
        case 'persegi':
            return Persegi(*angka)
        case 'segitiga':
            return Segitiga(*angka)
    return None


def kategori(luas):
    if luas >= 20:
        return 'besar'
    if luas >= 10:
        return 'sedang'
    return 'kecil'


def jelaskan(b):
    match b:
        case Lingkaran(r):
            luas, nama = math.pi * r * r, 'lingkaran'
        case Persegi(s):
            luas, nama = s * s, 'persegi'
        case Segitiga(a, b, c) if max(a, b, c) >= a + b + c - max(a, b, c):
            return 'segitiga: tidak sah'
        case Segitiga(a, b, c):
            s = (a + b + c) / 2
            luas = math.sqrt(s * (s - a) * (s - b) * (s - c))
            nama = 'segitiga'
    return f'{nama}: luas {luas:.2f} ({kategori(luas)})'


for baris in sys.stdin:
    bagian = baris.split()
    if not bagian:
        continue
    nama, angka = bagian[0], [float(x) for x in bagian[1:]]
    bentuk = buat(nama, angka)
    if bentuk is None:
        print(f'tidak dikenal: {nama}')
    else:
        print(jelaskan(bentuk))
""",
    },
    {
        "title": "Latihan 12: Operator Pipa dan Komposisi ala F#",
        "difficulty": "Lanjut",
        "question": [
            "Kode F# ini menjumlahkan panjang kata yang lebih dari tiga huruf:",
            "",
            "  let total =",
            "      teks.Split(' ', StringSplitOptions.RemoveEmptyEntries)",
            "      |> Array.filter (fun k -> k.Length > 3)",
            "      |> Array.map (fun k -> k.Length)",
            "      |> Array.sum",
            "",
            "Python nggak punya operator |> dan >>, jadi buat sendiri dua fungsi:",
            "",
            "  - pipa(nilai, *fungsi) memberikan nilai ke fungsi pertama, hasilnya",
            "    ke fungsi kedua, dan seterusnya. Setiap kali satu fungsi selesai,",
            "    cetak \"<nama fungsi>: <hasil>\" (nama dari f.__name__).",
            "  - komposisi(f, g) mengembalikan fungsi baru yang menjalankan f lalu",
            "    g, seperti f >> g di F#.",
            "",
            "Buat empat fungsi tahap bernama pisah, saring, panjang, dan jumlah. Baca",
            "satu baris teks dari stdin, jalankan pipa dengan keempat tahap itu, lalu",
            "buat satu fungsi gabungan dengan komposisi dan cetak \"komposisi: <hasil>\".",
            "Kedua cara harus memberi angka yang sama.",
            "",
            "Untuk input makan nasi di warung ibu, keluarannya:",
            "  pisah: ['makan', 'nasi', 'di', 'warung', 'ibu']",
            "  saring: ['makan', 'nasi', 'warung']",
            "  panjang: [5, 4, 6]",
            "  jumlah: 15",
            "  komposisi: 15",
            "",
            "Untuk input aku dan dia, keluarannya:",
            "  pisah: ['aku', 'dan', 'dia']",
            "  saring: []",
            "  panjang: []",
            "  jumlah: 0",
            "  komposisi: 0",
        ],
        "hints": [
            "Tiap tahap cuma fungsi biasa yang menerima satu nilai dan mengembalikan satu nilai, jadi urutannya bisa diatur dari luar.",
            "pipa cukup berupa perulangan: untuk setiap f di fungsi, nilai = f(nilai), lalu cetak nama dan hasilnya.",
            "komposisi mengembalikan lambda x: g(f(x)); gabungkan empat tahap dengan memanggil komposisi bertingkat tiga kali.",
        ],
        "stdin_list": [
            """makan nasi di warung ibu
""",
            """aku dan dia
""",
            """  belajar   bahasa   fungsional  
""",
        ],
        "solution": """def pipa(nilai, *fungsi):
    for f in fungsi:
        nilai = f(nilai)
        print(f'{f.__name__}: {nilai}')
    return nilai


def komposisi(f, g):
    return lambda x: g(f(x))


def pisah(teks):
    return teks.split()


def saring(kata):
    return [k for k in kata if len(k) > 3]


def panjang(kata):
    return [len(k) for k in kata]


def jumlah(angka):
    return sum(angka)


teks = input()
pipa(teks, pisah, saring, panjang, jumlah)
gabungan = komposisi(komposisi(komposisi(pisah, saring), panjang), jumlah)
print(f'komposisi: {gabungan(teks)}')
""",
    },
    {
        "title": "Latihan 13: Pattern Matching Pesan ala Elixir",
        "difficulty": "Lanjut",
        "question": [
            "Layanan dompet digital menerima pesan satu per baris. Di Elixir,",
            "pemrosesnya ditulis sebagai fungsi berklausa banyak dengan guard:",
            "",
            "  def proses({:transfer, _dari, _ke, n}, saldo) when n <= 0,",
            "    do: {:ditolak, \"nominal harus positif\", saldo}",
            "  def proses({:transfer, dari, _ke, n}, saldo)",
            "      when n > :erlang.map_get(dari, saldo),",
            "    do: {:ditolak, \"saldo #{dari} kurang\", saldo}",
            "  def proses({:transfer, dari, ke, n}, saldo),",
            "    do: {:ok, %{saldo | dari => saldo[dari] - n, ke => saldo[ke] + n}}",
            "",
            "Tulis padanannya di Python dengan match-case dan guard (if di case). Saldo",
            "awal: ani 20000, budi 100000. Pesan yang mungkin:",
            "",
            "  ok <nilai>                   cetak \"ok: <nilai>\"",
            "  error <alasan>               cetak \"error: <alasan>\"",
            "  setor <nama> <n>             tambah saldo, cetak",
            "                               \"setor <nama> <n>: saldo <nama> <baru>\"",
            "  transfer <dari> <ke> <n>     pindahkan saldo, cetak",
            "                               \"transfer <dari> -> <ke> <n>: ok\"",
            "",
            "Pemeriksaan berurutan untuk setor dan transfer: nominal <= 0 dicetak",
            "\"ditolak: nominal harus positif\"; nama yang tidak ada dicetak \"ditolak:",
            "akun <nama> tidak ada\" (untuk transfer, periksa pengirim dulu); saldo",
            "pengirim kurang dicetak \"ditolak: saldo <dari> kurang\". Baris lain dicetak",
            "\"tidak dikenal: <baris>\". Pesan yang ditolak tidak mengubah saldo. Di",
            "akhir, cetak \"saldo akhir:\" lalu tiap akun urut nama, diawali dua spasi.",
            "",
            "Untuk input ok 42, keluarannya:",
            "  ok: 42",
            "  error: timeout",
            "  transfer budi -> ani 50000: ok",
            "  ditolak: saldo ani kurang",
            "  setor ani 10000: saldo ani 80000",
            "  ditolak: akun cici tidak ada",
            "  ditolak: nominal harus positif",
            "  tidak dikenal: halo dunia",
            "  saldo akhir:",
            "    ani 80000",
            "    budi 50000",
        ],
        "hints": [
            "Pecah tiap baris dengan split() lalu cocokkan daftar kata itu dengan pola daftar, misalnya case ['ok', nilai].",
            "Urutan case penting seperti klausa Elixir: taruh case yang punya guard untuk kasus ditolak lebih dulu, baru case yang berhasil.",
            "Guard boleh memanggil int(), jadi case ['transfer', dari, ke, n] if int(n) <= 0 menangkap nominal yang bukan positif.",
        ],
        "stdin_list": [
            """ok 42
error timeout
transfer budi ani 50000
transfer ani budi 999999
setor ani 10000
transfer budi cici 1000
setor budi -5
halo dunia
""",
            """transfer ani budi 20000
setor dodi 500
transfer ani budi 1
transfer budi ani 0
error habis
""",
        ],
        "solution": """import sys

saldo = {'ani': 20000, 'budi': 100000}

for baris in sys.stdin:
    baris = baris.strip()
    if not baris:
        continue
    match baris.split():
        case ['ok', nilai]:
            print(f'ok: {nilai}')
        case ['error', alasan]:
            print(f'error: {alasan}')
        case ['setor', _, n] if int(n) <= 0:
            print('ditolak: nominal harus positif')
        case ['setor', nama, _] if nama not in saldo:
            print(f'ditolak: akun {nama} tidak ada')
        case ['setor', nama, n]:
            saldo[nama] += int(n)
            print(f'setor {nama} {n}: saldo {nama} {saldo[nama]}')
        case ['transfer', _, _, n] if int(n) <= 0:
            print('ditolak: nominal harus positif')
        case ['transfer', dari, _, _] if dari not in saldo:
            print(f'ditolak: akun {dari} tidak ada')
        case ['transfer', _, ke, _] if ke not in saldo:
            print(f'ditolak: akun {ke} tidak ada')
        case ['transfer', dari, _, n] if int(n) > saldo[dari]:
            print(f'ditolak: saldo {dari} kurang')
        case ['transfer', dari, ke, n]:
            saldo[dari] -= int(n)
            saldo[ke] += int(n)
            print(f'transfer {dari} -> {ke} {n}: ok')
        case _:
            print(f'tidak dikenal: {baris}')

print('saldo akhir:')
for nama in sorted(saldo):
    print(f'  {nama} {saldo[nama]}')
""",
    },
    {
        "title": "Latihan 14: Supervisor Mini yang Menghidupkan Proses",
        "difficulty": "Lanjut",
        "question": [
            "Di Elixir, supervisor :one_for_one menghidupkan ulang pekerja yang crash,",
            "dan secara bawaan menyerah kalau restart terjadi lebih dari 3 kali.",
            "Simulasikan perilaku itu (tanpa thread, cukup perulangan biasa).",
            "",
            "Setiap baris masukan adalah satu pesan untuk pekerja:",
            "",
            "  tugas <nama>   pekerja memproses tugas itu",
            "  crash          pekerja mati saat menerima pesan ini",
            "  baris lain     pekerja mencetak bahwa ia mengabaikannya",
            "",
            "Aturan:",
            "",
            "  - Pekerja diberi nomor mulai 1 dan mencetak \"pekerja#<n> mulai\".",
            "  - Setiap tugas dicetak \"pekerja#<n> memproses <nama> (total <t>)\",",
            "    dengan t jumlah tugas yang diproses pekerja itu sendiri. Pekerja",
            "    baru mulai lagi dari 0, karena keadaan proses yang mati hilang.",
            "  - Pesan lain dicetak \"pekerja#<n> mengabaikan: <pesan>\".",
            "  - Saat crash, cetak \"pekerja#<n> crash\". Kalau restart yang sudah",
            "    terjadi kurang dari 3, cetak \"supervisor: restart <k>/3\" lalu",
            "    jalankan pekerja bernomor berikutnya. Kalau sudah 3, cetak",
            "    \"supervisor: menyerah, <s> pesan tidak diproses\" (s = sisa pesan",
            "    sesudah crash ini) dan berhenti.",
            "  - Kalau semua pesan habis tanpa menyerah, cetak",
            "    \"selesai: <total semua tugas> tugas, <k> restart\".",
            "",
            "Untuk input tugas A, keluarannya:",
            "  pekerja#1 mulai",
            "  pekerja#1 memproses A (total 1)",
            "  pekerja#1 memproses B (total 2)",
            "  pekerja#1 crash",
            "  supervisor: restart 1/3",
            "  pekerja#2 mulai",
            "  pekerja#2 memproses C (total 1)",
            "  pekerja#2 mengabaikan: halo",
            "  selesai: 3 tugas, 1 restart",
            "",
            "Untuk input crash, keluarannya:",
            "  pekerja#1 mulai",
            "  pekerja#1 crash",
            "  supervisor: restart 1/3",
            "  pekerja#2 mulai",
            "  pekerja#2 memproses X (total 1)",
            "  pekerja#2 crash",
            "  supervisor: restart 2/3",
            "  pekerja#3 mulai",
            "  pekerja#3 crash",
            "  supervisor: restart 3/3",
            "  pekerja#4 mulai",
            "  pekerja#4 crash",
            "  supervisor: menyerah, 2 pesan tidak diproses",
        ],
        "hints": [
            "Simpan tiga keadaan saja: nomor pekerja sekarang, jumlah tugas pekerja itu, dan berapa kali restart sudah terjadi.",
            "Karena perlu tahu sisa pesan saat menyerah, baca semua baris dulu ke dalam list lalu telusuri dengan enumerate.",
            "Saat restart, naikkan nomor pekerja dan setel ulang hitungan tugasnya ke 0, tapi simpan total keseluruhan di variabel terpisah.",
        ],
        "stdin_list": [
            """tugas A
tugas B
crash
tugas C
halo
""",
            """crash
tugas X
crash
crash
crash
tugas Y
tugas Z
""",
        ],
        "solution": """import sys

pesan = [b.strip() for b in sys.stdin if b.strip()]
BATAS = 3
nomor, tugas_pekerja, restart, total = 1, 0, 0, 0
menyerah = False
print(f'pekerja#{nomor} mulai')

for i, p in enumerate(pesan):
    kata = p.split(maxsplit=1)
    if kata[0] == 'tugas' and len(kata) == 2:
        tugas_pekerja += 1
        total += 1
        print(f'pekerja#{nomor} memproses {kata[1]} (total {tugas_pekerja})')
    elif p == 'crash':
        print(f'pekerja#{nomor} crash')
        if restart < BATAS:
            restart += 1
            print(f'supervisor: restart {restart}/{BATAS}')
            nomor += 1
            tugas_pekerja = 0
            print(f'pekerja#{nomor} mulai')
        else:
            sisa = len(pesan) - i - 1
            print(f'supervisor: menyerah, {sisa} pesan tidak diproses')
            menyerah = True
            break
    else:
        print(f'pekerja#{nomor} mengabaikan: {p}')

if not menyerah:
    print(f'selesai: {total} tugas, {restart} restart')
""",
    },
    {
        "title": "Latihan 15: Daftar Tak Hingga dengan Evaluasi Malas",
        "difficulty": "Lanjut",
        "question": [
            "Program Haskell ini mencetak n bilangan prima, n bilangan Fibonacci, dan n",
            "kuadrat bilangan ganjil pertama, memakai list tak hingga:",
            "",
            "  prima = saring [2 ..]",
            "    where saring (p : xs) = p : saring [x | x <- xs, x `mod` p /= 0]",
            "  fibs = 0 : 1 : zipWith (+) fibs (tail fibs)",
            "  kuadratGanjil = map (^ 2) (filter odd [1 ..])",
            "",
            "  main = do",
            "    n <- readLn",
            "    putStrLn (\"prima: \" ++ unwords (map show (take n prima)))",
            "    putStrLn (\"fibonacci: \" ++ unwords (map show (take n fibs)))",
            "    putStrLn (\"kuadrat ganjil: \" ++ unwords (map show (take n kuadratGanjil)))",
            "",
            "Tulis padanannya di Python dengan generator. Aturannya: tulis sendiri",
            "fungsi ambil(n, it), saring(syarat, it), dan iterasi(f, x) (setara take,",
            "filter, dan iterate di Haskell) sebagai generator, tanpa membuat list",
            "penuh sebelum diambil. Masukan satu bilangan n >= 1.",
            "",
            "Untuk input 5, keluarannya:",
            "  prima: 2 3 5 7 11",
            "  fibonacci: 0 1 1 2 3",
            "  kuadrat ganjil: 1 9 25 49 81",
            "",
            "Untuk input 1, keluarannya:",
            "  prima: 2",
            "  fibonacci: 0",
            "  kuadrat ganjil: 1",
        ],
        "hints": [
            "Generator berhenti dihitung begitu kamu berhenti memintanya, jadi barisan tak hingga aman selama yang mengambil cuma mengambil n.",
            "iterasi(f, x) cukup berupa while True yang meng-yield x lalu mengganti x dengan f(x); bilangan asli adalah iterasi(lambda x: x + 1, 1).",
            "Fibonacci bisa dibuat dengan iterasi atas pasangan (a, b) menjadi (b, a + b), lalu ambil elemen pertama tiap pasangan.",
        ],
        "stdin_list": [
            """5
""",
            """1
""",
            """8
""",
        ],
        "solution": """def ambil(n, it):
    for i, x in enumerate(it):
        if i >= n:
            return
        yield x


def saring(syarat, it):
    for x in it:
        if syarat(x):
            yield x


def iterasi(f, x):
    while True:
        yield x
        x = f(x)


def petakan(f, it):
    for x in it:
        yield f(x)


def prima():
    ditemukan = []
    for x in iterasi(lambda x: x + 1, 2):
        if all(x % p != 0 for p in ditemukan):
            ditemukan.append(x)
            yield x


def gabung(it):
    return ' '.join(str(x) for x in it)


n = int(input())
asli = iterasi(lambda x: x + 1, 1)
fibs = petakan(lambda p: p[0], iterasi(lambda p: (p[1], p[0] + p[1]), (0, 1)))
kuadrat_ganjil = petakan(lambda x: x * x, saring(lambda x: x % 2 == 1, asli))
print('prima: ' + gabung(ambil(n, prima())))
print('fibonacci: ' + gabung(ambil(n, fibs)))
print('kuadrat ganjil: ' + gabung(ambil(n, kuadrat_ganjil)))
""",
    },
    {
        "title": "Latihan 16: Maybe dan Rantai Bind ala Haskell",
        "difficulty": "Lanjut",
        "question": [
            "Di Haskell, langkah-langkah yang bisa gagal dirangkai dengan >>= atau do.",
            "Rantai berhenti di Nothing pertama:",
            "",
            "  tahunLahir baris = do",
            "    (nama, teksUmur) <- pisah baris",
            "    _ <- cekNama nama",
            "    umur <- readMaybe teksUmur",
            "    u <- cekRentang umur",
            "    return (2026 - u)",
            "",
            "Buat kelas Just dan Nothing sendiri di Python, plus fungsi bind(nilai,",
            "fungsi): kalau nilai adalah Just, panggil fungsi dengan isinya; kalau",
            "Nothing, kembalikan Nothing itu tanpa memanggil apa pun. Supaya mudah",
            "dicek, Nothing di latihan ini membawa alasan (di Haskell, tugas itu",
            "biasanya dipegang Either).",
            "",
            "Setiap baris masukan berbentuk nama,umur. Langkah rantainya:",
            "",
            "  1. pisah: harus tepat dua bagian dipisah koma, kalau tidak",
            "     \"format harus nama,umur\";",
            "  2. cek nama: tidak boleh kosong, kalau kosong \"nama kosong\";",
            "  3. baca umur: harus bilangan bulat, kalau tidak \"umur bukan angka\";",
            "  4. cek rentang: 0 sampai 150, kalau tidak \"umur di luar 0-150\";",
            "  5. hitung tahun lahir: 2026 dikurangi umur.",
            "",
            "Cetak \"<baris> -> Just <tahun>\" atau \"<baris> -> Nothing (<alasan>)\".",
            "",
            "Untuk input Ani,18, keluarannya:",
            "  Ani,18 -> Just 2008",
            "  Budi -> Nothing (format harus nama,umur)",
            "  Citra,abc -> Nothing (umur bukan angka)",
            "  Dodi,200 -> Nothing (umur di luar 0-150)",
            "  ,20 -> Nothing (nama kosong)",
            "  Eka,0 -> Just 2026",
        ],
        "hints": [
            "Setiap langkah adalah fungsi kecil yang menerima satu nilai biasa dan mengembalikan Just atau Nothing; jangan biarkan langkah tahu soal langkah lain.",
            "bind cukup memeriksa isinstance(nilai, Nothing); kalau ya kembalikan nilai itu, kalau bukan panggil fungsi(nilai.isi).",
            "Langkah pisah mengembalikan Just((nama, umur)), jadi langkah cek nama menerima tuple dan meneruskan teks umurnya ke langkah berikutnya.",
        ],
        "stdin_list": [
            """Ani,18
Budi
Citra,abc
Dodi,200
,20
Eka,0
""",
            """Fajar,-3
Gita,40
Hana,1,2
""",
        ],
        "solution": """import sys


class Just:
    def __init__(self, isi):
        self.isi = isi

    def __str__(self):
        return f'Just {self.isi}'


class Nothing:
    def __init__(self, alasan):
        self.alasan = alasan

    def __str__(self):
        return f'Nothing ({self.alasan})'


def bind(nilai, fungsi):
    if isinstance(nilai, Nothing):
        return nilai
    return fungsi(nilai.isi)


def pisah(baris):
    bagian = baris.split(',')
    if len(bagian) != 2:
        return Nothing('format harus nama,umur')
    return Just((bagian[0].strip(), bagian[1].strip()))


def cek_nama(pasangan):
    nama, teks_umur = pasangan
    return Nothing('nama kosong') if not nama else Just(teks_umur)


def baca_umur(teks):
    try:
        return Just(int(teks))
    except ValueError:
        return Nothing('umur bukan angka')


def cek_rentang(umur):
    return Just(umur) if 0 <= umur <= 150 else Nothing('umur di luar 0-150')


def tahun_lahir(umur):
    return Just(2026 - umur)


for baris in sys.stdin:
    baris = baris.strip()
    if not baris:
        continue
    hasil = Just(baris)
    for langkah in (pisah, cek_nama, baca_umur, cek_rentang, tahun_lahir):
        hasil = bind(hasil, langkah)
    print(f'{baris} -> {hasil}')
""",
    },
    {
        "title": "Latihan 17: Interpreter Lisp Mini",
        "difficulty": "Sulit",
        "question": [
            "Lanjutkan evaluator S-expression di materi Keluarga Lisp jadi interpreter",
            "Lisp kecil. Masukan dari stdin berisi beberapa ekspresi tingkat atas; satu",
            "ekspresi boleh memakan lebih dari satu baris. Yang harus didukung:",
            "",
            "  angka bulat         42, -7",
            "  (define nama nilai) simpan nilai, tidak mencetak apa pun",
            "  (lambda (a b) isi)  fungsi tanpa nama, boleh jadi closure",
            "  (if syarat a b)     cuma #f yang dianggap salah",
            "  + - * /             dua argumen atau lebih; / adalah bagi bulat (//)",
            "  < =                 dua argumen, hasilnya #t atau #f",
            "  (list a b ...)      membuat list",
            "  car cdr             elemen pertama dan sisa list",
            "",
            "Untuk setiap ekspresi selain define, cetak hasilnya: angka apa adanya,",
            "boolean sebagai #t atau #f, list dalam kurung dipisah spasi (list kosong",
            "jadi ()), dan fungsi sebagai <lambda>. Kalau ada simbol yang belum",
            "didefinisikan, cetak \"galat: simbol <nama> belum didefinisikan\" lalu",
            "lanjut ke ekspresi berikutnya.",
            "",
            "Untuk input (define kuadrat (lambda (x) (* x x))), keluarannya:",
            "  49",
            "  3628800",
            "  (1 2 3)",
            "  20",
            "  #t",
            "  200",
            "",
            "Untuk input (define tambah (lambda (a b) (+ a b))), keluarannya:",
            "  5",
            "  ()",
            "  3",
            "  galat: simbol kurang belum didefinisikan",
            "  15",
            "  <lambda>",
        ],
        "hints": [
            "Pisahkan tiga tahap seperti di materi: token, baca jadi list bersarang, lalu evaluasi pohonnya dengan sebuah lingkungan (dict) berisi nama dan nilainya.",
            "Supaya closure bekerja, lingkungan perlu induk: saat lambda dipanggil, buat lingkungan baru berisi parameter, dengan induk lingkungan tempat lambda itu dibuat.",
            "Tangani bentuk khusus (define, lambda, if) sebelum mengevaluasi argumen, karena if nggak boleh menghitung kedua cabangnya; ubah simbol yang nggak ketemu jadi exception yang ditangkap per ekspresi.",
        ],
        "stdin_list": [
            """(define kuadrat (lambda (x) (* x x)))
(kuadrat 7)
(define fakt
  (lambda (n)
    (if (< n 2) 1 (* n (fakt (- n 1))))))
(fakt 10)
(list 1 2 (+ 1 2))
(car (cdr (list 10 20 30)))
(= (fakt 3) 6)
(if (< 5 3) 100 200)
""",
            """(define tambah (lambda (a b) (+ a b)))
(tambah 2 3)
(cdr (list 1))
(/ 17 5)
(kurang 1 2)
(define buat-penambah (lambda (n) (lambda (x) (+ x n))))
((buat-penambah 10) 5)
(buat-penambah 1)
""",
        ],
        "solution": """import sys


class Galat(Exception):
    pass


class Lingkungan(dict):
    def __init__(self, nama=(), nilai=(), induk=None):
        super().__init__(zip(nama, nilai))
        self.induk = induk

    def cari(self, simbol):
        if simbol in self:
            return self
        if self.induk is None:
            raise Galat(f'simbol {simbol} belum didefinisikan')
        return self.induk.cari(simbol)


class Lambda:
    def __init__(self, param, isi, ling):
        self.param, self.isi, self.ling = param, isi, ling

    def __call__(self, *arg):
        return hitung(self.isi, Lingkungan(self.param, arg, self.ling))


def token(teks):
    return teks.replace('(', ' ( ').replace(')', ' ) ').split()


def baca(t):
    x = t.pop(0)
    if x == '(':
        daftar = []
        while t[0] != ')':
            daftar.append(baca(t))
        t.pop(0)
        return daftar
    try:
        return int(x)
    except ValueError:
        return x


def lipat(f):
    def g(*arg):
        hasil = arg[0]
        for v in arg[1:]:
            hasil = f(hasil, v)
        return hasil
    return g


GLOBAL = Lingkungan()
GLOBAL.update({
    '+': lipat(lambda a, b: a + b),
    '-': lipat(lambda a, b: a - b),
    '*': lipat(lambda a, b: a * b),
    '/': lipat(lambda a, b: a // b),
    '<': lambda a, b: a < b,
    '=': lambda a, b: a == b,
    'list': lambda *x: list(x),
    'car': lambda x: x[0],
    'cdr': lambda x: x[1:],
})


def hitung(x, ling=GLOBAL):
    if isinstance(x, str):
        return ling.cari(x)[x]
    if isinstance(x, int):
        return x
    kepala = x[0]
    if kepala == 'define':
        ling[x[1]] = hitung(x[2], ling)
        return None
    if kepala == 'lambda':
        return Lambda(x[1], x[2], ling)
    if kepala == 'if':
        cabang = x[3] if hitung(x[1], ling) is False else x[2]
        return hitung(cabang, ling)
    f = hitung(kepala, ling)
    return f(*[hitung(a, ling) for a in x[1:]])


def tulis(v):
    if v is True:
        return '#t'
    if v is False:
        return '#f'
    if isinstance(v, list):
        return '(' + ' '.join(tulis(a) for a in v) + ')'
    if callable(v):
        return '<lambda>'
    return str(v)


t = token(sys.stdin.read())
while t:
    ekspresi = baca(t)
    try:
        hasil = hitung(ekspresi)
    except Galat as e:
        print(f'galat: {e}')
        continue
    if not (isinstance(ekspresi, list) and ekspresi and ekspresi[0] == 'define'):
        print(tulis(hasil))
""",
    },
    {
        "title": "Latihan 18: Unifikasi dan Backtracking ala Prolog",
        "difficulty": "Sulit",
        "question": [
            "Tulis mesin Prolog mini. Masukan dari stdin berisi tiga jenis baris,",
            "masing-masing diakhiri titik:",
            "",
            "  fakta    orangtua(budi, ani).",
            "  aturan   kakek(X, Z) :- orangtua(X, Y), orangtua(Y, Z).",
            "  query    ?- kakek(budi, Cucu).",
            "",
            "Argumen selalu atom (huruf kecil) atau variabel (diawali huruf besar);",
            "tidak ada struktur bersarang. Badan aturan berisi satu atau lebih tujuan",
            "dipisah koma, dan tujuan boleh memanggil aturan lain.",
            "",
            "Jawab query dengan cara Prolog: coba fakta dan aturan dari atas ke bawah,",
            "tujuan di badan dari kiri ke kanan, dan mundur (backtracking) untuk",
            "mencari semua jawaban. Variabel di aturan harus diganti nama setiap kali",
            "aturan itu dipakai, supaya X di satu pemakaian tidak tertukar dengan X di",
            "pemakaian lain.",
            "",
            "Untuk setiap query, cetak query-nya, lalu satu baris per jawaban berisi",
            "variabel query menurut urutan kemunculannya (\"X = ani\" atau \"K = budi, C =",
            "citra\"). Query tanpa variabel yang berhasil dicetak \"true.\", dan query",
            "tanpa jawaban dicetak \"false.\".",
            "",
            "Seperti Prolog sungguhan, saudara(X, Y) di bawah ikut menganggap seseorang",
            "saudara dirinya sendiri, karena tidak ada syarat X \\= Y.",
            "",
            "Untuk input orangtua(budi, ani)., keluarannya:",
            "  ?- kakek(budi, Cucu).",
            "  Cucu = citra",
            "  Cucu = eka",
            "  Cucu = fajar",
            "  ?- orangtua(X, citra).",
            "  X = ani",
            "  ?- kakek(ani, X).",
            "  false.",
            "  ?- orangtua(budi, dodi).",
            "  true.",
            "  ?- saudara(eka, S).",
            "  S = eka",
            "  S = fajar",
        ],
        "hints": [
            "Simpan substitusi sebagai dict dari nama variabel ke nilainya, dan buat fungsi telusur yang mengikuti rantai variabel sampai ketemu atom atau variabel bebas.",
            "Unifikasi dua tujuan berhasil kalau nama predikat dan jumlah argumennya sama, lalu tiap pasangan argumen bisa disamakan: atom dengan atom yang sama, atau variabel diikat ke sisi lain.",
            "Tulis pencarian sebagai generator rekursif selesaikan(tujuan, subst) yang meng-yield setiap substitusi berhasil; backtracking terjadi otomatis saat perulangan for mencoba klausa berikutnya.",
        ],
        "stdin_list": [
            """orangtua(budi, ani).
orangtua(budi, dodi).
orangtua(ani, citra).
orangtua(dodi, eka).
orangtua(dodi, fajar).
kakek(X, Z) :- orangtua(X, Y), orangtua(Y, Z).
saudara(X, Y) :- orangtua(P, X), orangtua(P, Y).
?- kakek(budi, Cucu).
?- orangtua(X, citra).
?- kakek(ani, X).
?- orangtua(budi, dodi).
?- saudara(eka, S).
""",
            """suka(ani, kopi).
suka(budi, teh).
suka(citra, kopi).
teman(X, Y) :- suka(X, M), suka(Y, M).
?- teman(ani, T).
?- teman(A, B).
?- suka(dodi, kopi).
""",
        ],
        "solution": "import re\nimport sys\n\nTUJUAN = re.compile(r'(\\w+)\\(([^()]*)\\)')\n\n\ndef urai(teks):\n    return [(n, [a.strip() for a in arg.split(',')])\n            for n, arg in TUJUAN.findall(teks)]\n\n\ndef variabel(x):\n    return x[:1].isupper() or x[:1] == '_'\n\n\ndef telusur(x, s):\n    while variabel(x) and x in s:\n        x = s[x]\n    return x\n\n\ndef unifikasi(a, b, s):\n    if a[0] != b[0] or len(a[1]) != len(b[1]):\n        return None\n    s = dict(s)\n    for x, y in zip(a[1], b[1]):\n        x, y = telusur(x, s), telusur(y, s)\n        if x == y:\n            continue\n        if variabel(x):\n            s[x] = y\n        elif variabel(y):\n            s[y] = x\n        else:\n            return None\n    return s\n\n\nklausa = []\nnomor = [0]\n\n\ndef ganti_nama(kepala, badan):\n    nomor[0] += 1\n    ubah = lambda t: (t[0], [f'{a}_{nomor[0]}' if variabel(a) else a\n                              for a in t[1]])\n    return ubah(kepala), [ubah(t) for t in badan]\n\n\ndef selesaikan(tujuan, s):\n    if not tujuan:\n        yield s\n        return\n    pertama, sisa = tujuan[0], tujuan[1:]\n    for kepala, badan in klausa:\n        kepala, badan = ganti_nama(kepala, badan)\n        s2 = unifikasi(pertama, kepala, s)\n        if s2 is not None:\n            yield from selesaikan(badan + sisa, s2)\n\n\nfor baris in sys.stdin:\n    baris = baris.strip()\n    if not baris:\n        continue\n    if baris.startswith('?-'):\n        print(baris)\n        tujuan = urai(baris[2:])\n        nama = []\n        for _, arg in tujuan:\n            for a in arg:\n                if variabel(a) and a != '_' and a not in nama:\n                    nama.append(a)\n        ada = False\n        for s in selesaikan(tujuan, {}):\n            ada = True\n            if nama:\n                print(', '.join(f'{v} = {telusur(v, s)}' for v in nama))\n            else:\n                print('true.')\n                break\n        if not ada:\n            print('false.')\n    elif ':-' in baris:\n        kepala, badan = baris.split(':-')\n        klausa.append((urai(kepala)[0], urai(badan)))\n    else:\n        klausa.append((urai(baris)[0], []))\n",
    },
    {
        "title": "Latihan 19: Mesin Stack ala Forth dan Kalkulator RPN",
        "difficulty": "Lanjut",
        "question": [
            "Buat interpreter Forth mini. Program dibaca dari stdin baris",
            "demi baris. Tiap baris berisi kata yang dipisah spasi, dan",
            "huruf besar-kecil dianggap sama. Stack satu untuk seluruh",
            "program.",
            "",
            "Kata yang harus dikenali:",
            "",
            "  angka bulat   taruh di stack (boleh negatif, misalnya -7)",
            "  + - * /       ambil b lalu a, taruh a op b; / adalah bagi",
            "                bulat dibulatkan ke bawah (seperti // Python)",
            "  dup           a -> a a",
            "  drop          a ->",
            "  swap          a b -> b a",
            "  over          a b -> a b a",
            "  .             ambil puncak stack dan catat untuk dicetak",
            "  .s            catat isi stack tanpa mengubahnya: <n> a b c",
            "                (cuma <0> kalau kosong)",
            "  : nama ... ;  definisi kata baru, selalu satu baris",
            "",
            "Semua yang dicatat dalam satu baris dicetak di akhir baris itu,",
            "digabung satu spasi. Baris tanpa catatan nggak mencetak apa pun.",
            "",
            "Definisi memakai arti kata saat definisi ditulis: kalau",
            "badannya memakai kata buatanmu yang lain, salin badan kata itu.",
            "Mendefinisikan ulang sebuah kata nggak mengubah kata lain yang",
            "sudah memakainya.",
            "",
            "Galat nggak boleh membuat program crash. Saat terjadi galat,",
            "cetak dulu catatan yang sudah ada di baris itu (kalau ada),",
            "lalu salah satu pesan berikut, kosongkan stack, dan lewati sisa",
            "baris:",
            "",
            "  galat: stack kosong pada 'kata'",
            "  galat: bagi nol",
            "  galat: kata tidak dikenal 'kata'",
            "  galat: definisi harus diakhiri ';'",
            "",
            "Contoh masukan:",
            "",
            "  2 3 + .",
            "  10 dup * .",
            "  : kuadrat dup * ;",
            "  7 kuadrat .",
            "  1 2 3 .s",
            "  swap .s",
            "  over .s",
            "  drop drop drop drop",
            "  .s",
            "  5 0 /",
            "  20 3 / . -7 2 / .",
            "  4 . foo 5 .",
            "  : kubik dup kuadrat * ;",
            "  3 kubik .",
            "",
            "Keluaran yang diharapkan:",
            "5",
            "100",
            "49",
            "<3> 1 2 3",
            "<3> 1 3 2",
            "<4> 1 3 2 3",
            "<0>",
            "galat: bagi nol",
            "6 -4",
            "4",
            "galat: kata tidak dikenal 'foo'",
            "27",
        ],
        "hints": [
            "Baca lagi bagian Forth di materi Peta Bahasa Sistem Generasi Baru: setiap kata cuma mengambil dan menaruh nilai di stack.",
            "Pakai list Python sebagai stack, dict untuk kata buatan, dan exception buatanmu sendiri supaya galat di tengah baris bisa menghentikan baris itu dengan rapi.",
            "Saat definisi, ganti setiap kata di badan yang sudah ada di kamus dengan isi badannya, lalu simpan hasilnya dengan kamus[nama] = badan.",
            "Tantangan tambahan yang nggak dinilai: Brainfuck juga mesin kecil dengan pita memori dan penunjuk, coba buat interpreternya.",
        ],
        "solution": """import sys

stack = []
kamus = {}


class GalatForth(Exception):
    pass


def ambil(kata):
    if not stack:
        raise GalatForth(f"stack kosong pada '{kata}'")
    return stack.pop()


def jalankan(kata, keluar):
    if kata in kamus:
        for k in kamus[kata]:
            jalankan(k, keluar)
        return
    try:
        stack.append(int(kata))
        return
    except ValueError:
        pass
    if kata in ("+", "-", "*", "/"):
        b = ambil(kata)
        a = ambil(kata)
        if kata == "+":
            stack.append(a + b)
        elif kata == "-":
            stack.append(a - b)
        elif kata == "*":
            stack.append(a * b)
        else:
            if b == 0:
                raise GalatForth("bagi nol")
            stack.append(a // b)
    elif kata == "dup":
        a = ambil(kata)
        stack.extend([a, a])
    elif kata == "drop":
        ambil(kata)
    elif kata == "swap":
        b = ambil(kata)
        a = ambil(kata)
        stack.extend([b, a])
    elif kata == "over":
        b = ambil(kata)
        a = ambil(kata)
        stack.extend([a, b, a])
    elif kata == ".":
        keluar.append(str(ambil(kata)))
    elif kata == ".s":
        keluar.append(f"<{len(stack)}>" + "".join(f" {x}" for x in stack))
    else:
        raise GalatForth(f"kata tidak dikenal '{kata}'")


def definisikan(token):
    if len(token) < 3 or token[-1] != ";":
        raise GalatForth("definisi harus diakhiri ';'")
    nama, isi = token[1], token[2:-1]
    badan = []
    for k in isi:
        badan.extend(kamus.get(k, [k]))
    kamus[nama] = badan


for baris in sys.stdin.read().splitlines():
    token = baris.lower().split()
    if not token:
        continue
    keluar = []
    try:
        if token[0] == ":":
            definisikan(token)
        else:
            for kata in token:
                jalankan(kata, keluar)
    except GalatForth as g:
        if keluar:
            print(" ".join(keluar))
        print(f"galat: {g}")
        stack.clear()
        continue
    if keluar:
        print(" ".join(keluar))
""",
        "stdin_list": [
            """2 3 + .
10 dup * .
: kuadrat dup * ;
7 kuadrat .
1 2 3 .s
swap .s
over .s
drop drop drop drop
.s
5 0 /
20 3 / . -7 2 / .
4 . foo 5 .
: kubik dup kuadrat * ;
3 kubik .
""",
            """1 2 3 4 + + + .
: tiga 3 ;
: enam tiga tiga + ;
enam . tiga .
8 2 - . 2 8 - .
.
9 swap
""",
            """: kuadrat dup * ;
: jumlah-kuadrat kuadrat swap kuadrat + ;
3 4 jumlah-kuadrat .
: kuadrat dup ;
3 4 jumlah-kuadrat .
5 KUADRAT .s
: rusak 1 2
""",
        ],
    },
    {
        "title": "Latihan 20: Simulator CPU Mini ala Assembly",
        "difficulty": "Sulit",
        "question": [
            "Buat simulator CPU kecil dengan empat register A, B, C, D (awal",
            "semuanya 0) dan satu flag nol. Program assembly dibaca dari",
            "stdin. Teks sesudah ; adalah komentar, baris kosong dilewati,",
            "dan baris yang diakhiri titik dua adalah label untuk instruksi",
            "berikutnya. Nama instruksi boleh huruf kecil, nama register",
            "harus huruf besar. Operan dipisah koma.",
            "",
            "  MOV r, x    r = x",
            "  ADD r, x    r = r + x, lalu flag nol = (r == 0)",
            "  SUB r, x    r = r - x, lalu flag nol = (r == 0)",
            "  MUL r, x    r = r * x, lalu flag nol = (r == 0)",
            "  CMP r, x    flag nol = (r - x == 0), r tidak berubah",
            "  JMP label   lompat ke label",
            "  JZ label    lompat kalau flag nol menyala",
            "  JNZ label   lompat kalau flag nol mati",
            "  PRINT x     cetak nilai x",
            "  HALT        berhenti",
            "",
            "r harus register. x boleh register atau bilangan bulat.",
            "",
            "Sebelum menjalankan apa pun, periksa seluruh program. Cetak",
            "galat pertama yang ditemukan lalu berhenti, salah satu dari:",
            "",
            "  galat baris N: instruksi tidak dikenal 'teks asli'",
            "  galat baris N: OP butuh K operan",
            "  galat baris N: 'teks' bukan register",
            "  galat baris N: operan 'teks' tidak sah",
            "  galat baris N: label 'nama' tidak ada",
            "",
            "N adalah nomor baris di masukan (mulai dari 1). Pemeriksaan",
            "label dilakukan sesudah semua baris lain lolos.",
            "",
            "Saat menjalankan, setiap instruksi yang dieksekusi dihitung",
            "satu langkah, termasuk HALT. Kalau sudah 10000 langkah dan",
            "program belum berhenti, cetak",
            "'galat: lebih dari 10000 langkah, program dihentikan'.",
            "Program juga berhenti kalau instruksi habis. Di akhir, cetak",
            "'selesai dalam N langkah' lalu isi register: A=.. B=.. C=.. D=..",
            "",
            "Contoh masukan (faktorial 5):",
            "",
            "  ; faktorial 5",
            "      MOV A, 1",
            "      MOV C, 5",
            "  ulang:",
            "      MUL A, C",
            "      SUB C, 1",
            "      JNZ ulang",
            "      PRINT A",
            "      HALT",
            "",
            "Keluaran yang diharapkan:",
            "120",
            "selesai dalam 19 langkah",
            "A=120 B=0 C=0 D=0",
        ],
        "hints": [
            "Pisahkan dua tahap seperti assembler sungguhan: tahap urai yang mengubah teks jadi daftar instruksi dan peta label, lalu tahap jalan yang cuma membaca daftar itu.",
            "Label nggak dihitung sebagai instruksi, jadi simpan sebagai label[nama] = len(program) tepat saat ditemukan.",
            "Saat jalan, pakai penghitung pc: ambil program[pc], naikkan pc, lalu instruksi lompat cukup mengganti pc = label[nama].",
        ],
        "solution": """import sys

REGISTER = ("A", "B", "C", "D")
OPERAN = {"MOV": 2, "ADD": 2, "SUB": 2, "MUL": 2, "CMP": 2,
          "JMP": 1, "JZ": 1, "JNZ": 1, "PRINT": 1, "HALT": 0}
HITUNG = ("MOV", "ADD", "SUB", "MUL", "CMP")
BATAS = 10000


def urai(teks):
    program, label = [], {}
    for nomor, baris in enumerate(teks.splitlines(), 1):
        baris = baris.split(";")[0].strip()
        if not baris:
            continue
        if baris.endswith(":"):
            label[baris[:-1].strip()] = len(program)
            continue
        bagian = baris.split(None, 1)
        op = bagian[0].upper()
        operan = [x.strip() for x in bagian[1].split(",")] if len(bagian) > 1 else []
        if op not in OPERAN:
            return None, f"galat baris {nomor}: instruksi tidak dikenal '{bagian[0]}'"
        if len(operan) != OPERAN[op]:
            return None, f"galat baris {nomor}: {op} butuh {OPERAN[op]} operan"
        if op in HITUNG and operan[0] not in REGISTER:
            return None, f"galat baris {nomor}: '{operan[0]}' bukan register"
        if op in HITUNG:
            isi = operan[1:]
        elif op == "PRINT":
            isi = operan
        else:
            isi = []
        for x in isi:
            if x not in REGISTER and not x.lstrip("-").isdigit():
                return None, f"galat baris {nomor}: operan '{x}' tidak sah"
        program.append((nomor, op, operan))
    for nomor, op, operan in program:
        if op in ("JMP", "JZ", "JNZ") and operan[0] not in label:
            return None, f"galat baris {nomor}: label '{operan[0]}' tidak ada"
    return (program, label), None


def nilai(reg, x):
    return reg[x] if x in REGISTER else int(x)


def jalankan(program, label):
    reg = dict.fromkeys(REGISTER, 0)
    nol = False
    pc = langkah = 0
    while pc < len(program):
        if langkah == BATAS:
            print(f"galat: lebih dari {BATAS} langkah, program dihentikan")
            break
        langkah += 1
        _nomor, op, operan = program[pc]
        pc += 1
        if op == "HALT":
            break
        if op == "PRINT":
            print(nilai(reg, operan[0]))
        elif op in ("JMP", "JZ", "JNZ"):
            if op == "JMP" or (op == "JZ" and nol) or (op == "JNZ" and not nol):
                pc = label[operan[0]]
        else:
            r, x = operan[0], nilai(reg, operan[1])
            if op == "MOV":
                reg[r] = x
            elif op == "CMP":
                nol = reg[r] - x == 0
            else:
                if op == "ADD":
                    reg[r] += x
                elif op == "SUB":
                    reg[r] -= x
                else:
                    reg[r] *= x
                nol = reg[r] == 0
    print(f"selesai dalam {langkah} langkah")
    print(" ".join(f"{r}={reg[r]}" for r in REGISTER))


hasil, galat = urai(sys.stdin.read())
if galat:
    print(galat)
else:
    jalankan(*hasil)
""",
        "stdin_list": [
            """; faktorial 5
    MOV A, 1
    MOV C, 5
ulang:
    MUL A, C
    SUB C, 1
    JNZ ulang
    PRINT A
    HALT
""",
            """MOV A, 0
MOV B, 1
loop:
  ADD A, B
  ADD B, 1
  CMP B, 11
  JNZ loop
PRINT A
PRINT B
""",
            """MOV A, 3
putar:
  ADD A, 0
  JMP putar
""",
            """MOV A, 1
JMP akhir
PRINT A
""",
            """mov B, -2
add B, 2
jz nol
print 1
nol:
print B
PUSH A
""",
            """MOV D, 4
CMP D, 4
JZ sama
PRINT 0
sama:
PRINT D
mov a, 1
""",
        ],
    },
    {
        "title": "Latihan 21: Record Berformat Tetap ala COBOL",
        "difficulty": "Lanjut",
        "question": [
            "Sistem mainframe mengekspor data rekening dengan copybook ini:",
            "",
            "  01 REKENING.",
            "     05 NO-REK   PIC 9(6).",
            "     05 NAMA     PIC X(10).",
            "     05 SALDO    PIC 9(7)V99.",
            "",
            "Setiap baris stdin adalah satu record selebar 25 karakter, tanpa",
            "pemisah. NAMA diisi spasi di kanan sampai 10 karakter. SALDO",
            "berisi 9 digit dengan dua digit terakhir sebagai sen (V adalah",
            "titik desimal tersirat), jadi 001234567 artinya 12345.67.",
            "",
            "Cetak baris judul, lalu satu baris per record yang sah dengan",
            "format: NO-REK apa adanya, satu spasi, NAMA tanpa spasi kanan",
            "dirata kiri selebar 10, satu spasi, SALDO dengan dua desimal",
            "dirata kanan selebar 11. Baris judul memakai lebar yang sama.",
            "",
            "Baris kosong dilewati. Baris lain yang nggak sah ditolak sesuai",
            "nomor barisnya di masukan (mulai dari 1), dengan pesan:",
            "",
            "  baris N ditolak: panjang P, seharusnya 25",
            "  baris N ditolak: NO-REK bukan angka",
            "  baris N ditolak: SALDO bukan angka",
            "",
            "Di akhir cetak 'total saldo (J rekening): T' dengan T dua",
            "desimal. Hitung dalam sen (bilangan bulat) supaya nggak ada",
            "galat pembulatan float.",
            "",
            "Contoh masukan:",
            "",
            "  000123BUDI      001234567",
            "  000124ANI SARI  000050000",
            "  000125CITRA     00000075",
            "  00012XDEDI      000010000",
            "  000126EKO PUTRA 120000050",
            "",
            "Keluaran yang diharapkan:",
            "NO-REK NAMA             SALDO",
            "000123 BUDI          12345.67",
            "000124 ANI SARI        500.00",
            "baris 3 ditolak: panjang 24, seharusnya 25",
            "baris 4 ditolak: NO-REK bukan angka",
            "000126 EKO PUTRA   1200000.50",
            "total saldo (3 rekening): 1212846.17",
        ],
        "hints": [
            "Baca lagi bagian record dan copybook di materi COBOL: posisi field dihitung dari lebar PIC, bukan dari spasi.",
            "Simpan bentuk copybook sebagai daftar (nama, lebar, jenis), lalu potong tiap baris dengan slice sambil memajukan posisi.",
            "Untuk SALDO, ubah ke int lalu cetak dengan f\"{sen // 100}.{sen % 100:02d}\" supaya tetap tepat sampai sen.",
        ],
        "solution": "import sys\n\n# copybook: NO-REK PIC 9(6), NAMA PIC X(10), SALDO PIC 9(7)V99\nFIELD = [(\"NO-REK\", 6, \"9\"), (\"NAMA\", 10, \"X\"), (\"SALDO\", 9, \"9\")]\nLEBAR = sum(f[1] for f in FIELD)\n\n\ndef urai(baris):\n    hasil, pos = {}, 0\n    for nama, panjang, jenis in FIELD:\n        isi = baris[pos:pos + panjang]\n        pos += panjang\n        if jenis == \"9\" and not isi.isdigit():\n            raise ValueError(f\"{nama} bukan angka\")\n        hasil[nama] = isi\n    return hasil\n\n\ndef rupiah(sen):\n    return f\"{sen // 100}.{sen % 100:02d}\"\n\n\nprint(f\"{'NO-REK'} {'NAMA':<10} {'SALDO':>11}\")\ntotal = jumlah = 0\nfor nomor, baris in enumerate(sys.stdin.read().split(\"\\n\"), 1):\n    if baris == \"\":\n        continue\n    if len(baris) != LEBAR:\n        print(f\"baris {nomor} ditolak: panjang {len(baris)}, seharusnya {LEBAR}\")\n        continue\n    try:\n        r = urai(baris)\n    except ValueError as e:\n        print(f\"baris {nomor} ditolak: {e}\")\n        continue\n    sen = int(r[\"SALDO\"])\n    total += sen\n    jumlah += 1\n    print(f\"{r['NO-REK']} {r['NAMA'].rstrip():<10} {rupiah(sen):>11}\")\nprint(f\"total saldo ({jumlah} rekening): {rupiah(total)}\")\n",
        "stdin_list": [
            """000123BUDI      001234567
000124ANI SARI  000050000
000125CITRA     00000075
00012XDEDI      000010000
000126EKO PUTRA 120000050
""",
            """100001SITI      000000001

100002JOKO      999999999
""",
            """200001RINA      0001x0000
200002 BAYU     000000099
""",
        ],
    },
    {
        "title": "Latihan 22: Alamat Sel A1 dan SUM ala Makro VBA",
        "difficulty": "Lanjut",
        "question": [
            "Makro VBA ini menjumlahkan kolom B:",
            "",
            "  For baris = 2 To terakhir",
            "      total = total + ws.Cells(baris, 2).Value",
            "  Next baris",
            "",
            "Buat lembar kerja mini yang mengerti alamat gaya A1 dan gaya",
            "Cells(baris, kolom). Kolom A sampai Z bernomor 1 sampai 26, lalu",
            "AA = 27, AB = 28, ..., ZZ = 702, AAA = 703. Baris mulai dari 1.",
            "Perintah dari stdin, satu per baris:",
            "",
            "  B2=12500      isi sel dengan teks sesudah = (huruf alamat",
            "                boleh kecil)",
            "  Range(\"B2\")   cetak 'B2 = isi', atau 'B2 = (kosong)'",
            "  Cells(3, 28)  cetak 'Cells(3, 28) -> AB3 = isi'",
            "  SUM(B2:B5)    cetak 'SUM(B2:B5) = total', menjumlahkan sel di",
            "                persegi panjang itu yang isinya bilangan bulat;",
            "                teks dilewati seperti SUM di Excel; urutan dua",
            "                sudut boleh terbalik",
            "",
            "Alamat yang dicetak selalu berhuruf besar. Galat dicetak tanpa",
            "menghentikan program:",
            "",
            "  galat: alamat 'B0' tidak sah        (alamat salah bentuk atau",
            "                                      baris 0)",
            "  galat: baris dan kolom mulai dari 1 (Cells dengan angka 0)",
            "  galat: perintah tidak dikenal '...'",
            "",
            "Contoh masukan:",
            "",
            "  A1=Kategori",
            "  B1=Jumlah",
            "  B2=12500",
            "  B3=30000",
            "  B4=teks",
            "  B5=2500",
            "  ab3=7",
            "  Range(\"B2\")",
            "  Range(\"c9\")",
            "  Cells(3, 28)",
            "  SUM(B2:B5)",
            "  SUM(B5:A1)",
            "  Range(\"B0\")",
            "  Cells(1, 703)",
            "  Hapus A1",
            "",
            "Keluaran yang diharapkan:",
            "B2 = 12500",
            "C9 = (kosong)",
            "Cells(3, 28) -> AB3 = 7",
            "SUM(B2:B5) = 45000",
            "SUM(B5:A1) = 45000",
            "galat: alamat 'B0' tidak sah",
            "Cells(1, 703) -> AAA1 = (kosong)",
            "galat: perintah tidak dikenal 'Hapus A1'",
        ],
        "hints": [
            "Baca lagi bagian model objek di materi VBA: Range memakai alamat huruf, Cells memakai nomor baris dan kolom, dan keduanya menunjuk sel yang sama.",
            "Simpan lembar sebagai dict dengan kunci (baris, kolom), lalu buat dua fungsi kecil: huruf ke nomor kolom dan sebaliknya.",
            "Huruf kolom mirip bilangan basis 26 tanpa angka nol, jadi saat mengubah nomor ke huruf pakai divmod(n - 1, 26) berulang.",
        ],
        "solution": "import re\nimport sys\n\nlembar = {}\n\n\ndef ke_angka(huruf):\n    n = 0\n    for h in huruf:\n        n = n * 26 + (ord(h) - ord(\"A\") + 1)\n    return n\n\n\ndef ke_huruf(n):\n    huruf = \"\"\n    while n > 0:\n        n, sisa = divmod(n - 1, 26)\n        huruf = chr(ord(\"A\") + sisa) + huruf\n    return huruf\n\n\ndef urai_alamat(teks):\n    m = re.fullmatch(r\"([A-Za-z]{1,3})([0-9]+)\", teks.strip())\n    if not m or int(m.group(2)) == 0:\n        raise ValueError(f\"alamat '{teks.strip()}' tidak sah\")\n    return int(m.group(2)), ke_angka(m.group(1).upper())\n\n\ndef alamat(baris, kolom):\n    return f\"{ke_huruf(kolom)}{baris}\"\n\n\ndef tampil(baris, kolom):\n    return lembar.get((baris, kolom), \"(kosong)\")\n\n\ndef jumlah(awal, akhir):\n    (b1, k1), (b2, k2) = urai_alamat(awal), urai_alamat(akhir)\n    total = 0\n    for b in range(min(b1, b2), max(b1, b2) + 1):\n        for k in range(min(k1, k2), max(k1, k2) + 1):\n            isi = lembar.get((b, k), \"\")\n            if re.fullmatch(r\"-?[0-9]+\", isi):\n                total += int(isi)\n    return total\n\n\nfor perintah in sys.stdin.read().splitlines():\n    perintah = perintah.strip()\n    if not perintah:\n        continue\n    try:\n        m_set = re.fullmatch(r\"([A-Za-z]+[0-9]+)=(.*)\", perintah)\n        m_range = re.fullmatch(r'Range\\(\"([^\"]*)\"\\)', perintah)\n        m_cells = re.fullmatch(r\"Cells\\(\\s*([0-9]+)\\s*,\\s*([0-9]+)\\s*\\)\", perintah)\n        m_sum = re.fullmatch(r\"SUM\\(([^:]+):([^)]+)\\)\", perintah)\n        if m_set:\n            lembar[urai_alamat(m_set.group(1))] = m_set.group(2)\n        elif m_range:\n            b, k = urai_alamat(m_range.group(1))\n            print(f\"{alamat(b, k)} = {tampil(b, k)}\")\n        elif m_cells:\n            b, k = int(m_cells.group(1)), int(m_cells.group(2))\n            if b == 0 or k == 0:\n                raise ValueError(\"baris dan kolom mulai dari 1\")\n            print(f\"Cells({b}, {k}) -> {alamat(b, k)} = {tampil(b, k)}\")\n        elif m_sum:\n            print(f\"{perintah} = {jumlah(m_sum.group(1), m_sum.group(2))}\")\n        else:\n            print(f\"galat: perintah tidak dikenal '{perintah}'\")\n    except ValueError as e:\n        print(f\"galat: {e}\")\n",
        "stdin_list": [
            """A1=Kategori
B1=Jumlah
B2=12500
B3=30000
B4=teks
B5=2500
ab3=7
Range("B2")
Range("c9")
Cells(3, 28)
SUM(B2:B5)
SUM(B5:A1)
Range("B0")
Cells(1, 703)
Hapus A1
""",
            """AA1=5
AB1=-2
Z1=10
SUM(Z1:AB1)
Cells(1, 27)
Cells(0, 3)
Range("zz1")
ZZ1=9
Cells(1, 702)
""",
            """A1=1
A2=2
B1=3
B2=x
SUM(A1:B2)
Range("A2")
Range("1A")
""",
        ],
    },
    {
        "title": "Latihan 23: Tabel Kebenaran dari Rangkaian ala Verilog",
        "difficulty": "Lanjut",
        "question": [
            "Stdin berisi satu modul gaya Verilog yang disederhanakan.",
            "Setiap pernyataan diakhiri titik koma, kecuali endmodule, dan",
            "komentar diawali //. Pernyataan yang mungkin:",
            "",
            "  module nama;            awal modul",
            "  input a, b, cin;        sinyal masukan, urutannya penting",
            "  output s, cout;         sinyal keluaran, urutannya penting",
            "  wire p;                 kabel perantara",
            "  assign s = p ^ cin;     sambungkan sinyal ke sebuah rumus",
            "  endmodule",
            "",
            "Rumus memakai nama sinyal, kurung, dan operator dengan",
            "prioritas Verilog: ~ (NOT) paling kuat, lalu & (AND), lalu",
            "^ (XOR), lalu | (OR) paling lemah. Operator biner berasosiasi",
            "ke kiri. Seperti di Verilog, urutan baris assign nggak penting:",
            "sebuah kabel boleh dipakai sebelum baris assign-nya.",
            "",
            "Cetak tabel kebenaran untuk semua kombinasi input, berurutan",
            "seperti bilangan biner dengan input pertama sebagai bit paling",
            "kiri. Baris judul berisi nama input dipisah spasi, lalu ' | ',",
            "lalu nama output. Di setiap baris, angka 0/1 ditulis rata kiri",
            "selebar nama kolomnya, dengan spasi di ujung baris dibuang.",
            "",
            "Kalau ada masalah, cetak satu baris galat saja (tanpa tabel):",
            "",
            "  galat: sinyal 'x' belum dideklarasikan",
            "  galat: output 'x' tidak pernah di-assign",
            "  galat: rangkaian melingkar pada 'x'",
            "",
            "Contoh masukan:",
            "",
            "  module full_adder;",
            "    input a, b, cin;",
            "    output s, cout;",
            "    wire p;",
            "    assign p = a ^ b;       // jumlah sementara",
            "    assign s = p ^ cin;",
            "    assign cout = (a & b) | (cin & p);",
            "  endmodule",
            "",
            "Keluaran yang diharapkan:",
            "a b cin | s cout",
            "0 0 0   | 0 0",
            "0 0 1   | 1 0",
            "0 1 0   | 1 0",
            "0 1 1   | 0 1",
            "1 0 0   | 1 0",
            "1 0 1   | 0 1",
            "1 1 0   | 0 1",
            "1 1 1   | 1 1",
        ],
        "hints": [
            "Baca lagi bagian half adder di materi Verilog dan VHDL: assign adalah kabel yang selalu tersambung, bukan langkah yang dijalankan berurutan.",
            "Pisahkan tiga tahap: memecah rumus jadi token, mengurainya jadi pohon dengan satu fungsi per tingkat prioritas, lalu menghitung pohon itu untuk setiap kombinasi input.",
            "Hitung kabel secara rekursif saat dibutuhkan, dan bawa himpunan sinyal yang sedang dihitung supaya rangkaian melingkar bisa dikenali sebelum rekursinya tak berujung.",
        ],
        "solution": "import re\nimport sys\n\nTOKEN = re.compile(r\"\\s*([A-Za-z_][A-Za-z0-9_]*|[~&|^()])\")\n\n\nclass Galat(Exception):\n    pass\n\n\ndef pecah(teks):\n    token, pos = [], 0\n    teks = teks.strip()\n    while pos < len(teks):\n        m = TOKEN.match(teks, pos)\n        if not m:\n            raise Galat(f\"karakter tidak dikenal '{teks[pos:].strip()[0]}'\")\n        token.append(m.group(1))\n        pos = m.end()\n    return token\n\n\nclass Pengurai:\n    # prioritas Verilog: ~ paling kuat, lalu &, lalu ^, lalu |\n    def __init__(self, token):\n        self.t, self.i = token, 0\n\n    def lihat(self):\n        return self.t[self.i] if self.i < len(self.t) else None\n\n    def ambil(self):\n        x = self.lihat()\n        self.i += 1\n        return x\n\n    def urai(self):\n        pohon = self.atau()\n        if self.lihat() is not None:\n            raise Galat(f\"token tak terduga '{self.lihat()}'\")\n        return pohon\n\n    def biner(self, op, lanjut):\n        kiri = lanjut()\n        while self.lihat() == op:\n            self.ambil()\n            kiri = (op, kiri, lanjut())\n        return kiri\n\n    def atau(self):\n        return self.biner(\"|\", self.xor)\n\n    def xor(self):\n        return self.biner(\"^\", self.dan)\n\n    def dan(self):\n        return self.biner(\"&\", self.satu)\n\n    def satu(self):\n        x = self.ambil()\n        if x == \"~\":\n            return (\"~\", self.satu())\n        if x == \"(\":\n            isi = self.atau()\n            if self.ambil() != \")\":\n                raise Galat(\"kurung tidak ditutup\")\n            return isi\n        if x is None:\n            raise Galat(\"rumus tidak lengkap\")\n        if not re.fullmatch(r\"[A-Za-z_]\\w*\", x):\n            raise Galat(f\"token tak terduga '{x}'\")\n        return x\n\n\ndef nama_di(pohon):\n    if isinstance(pohon, str):\n        return {pohon}\n    return set().union(*(nama_di(p) for p in pohon[1:]))\n\n\ndef baca(teks):\n    masuk, keluar, kabel, rumus = [], [], [], {}\n    for baris in teks.split(\";\"):\n        baris = re.sub(r\"^\\s*module\\s+\\w+\", \"\", baris).strip()\n        if not baris or baris == \"endmodule\":\n            continue\n        kata = baris.split(None, 1)\n        if kata[0] in (\"input\", \"output\", \"wire\"):\n            nama = [n.strip() for n in kata[1].split(\",\")]\n            {\"input\": masuk, \"output\": keluar, \"wire\": kabel}[kata[0]].extend(nama)\n        elif kata[0] == \"assign\":\n            kiri, kanan = kata[1].split(\"=\", 1)\n            rumus[kiri.strip()] = Pengurai(pecah(kanan)).urai()\n        else:\n            raise Galat(f\"baris tidak dikenal '{baris}'\")\n    dikenal = set(masuk) | set(keluar) | set(kabel)\n    for kiri, pohon in rumus.items():\n        for n in sorted({kiri} | nama_di(pohon)):\n            if n not in dikenal:\n                raise Galat(f\"sinyal '{n}' belum dideklarasikan\")\n    for k in keluar:\n        if k not in rumus:\n            raise Galat(f\"output '{k}' tidak pernah di-assign\")\n    return masuk, keluar, rumus\n\n\ndef hitung(pohon, nilai, rumus, jalur):\n    if isinstance(pohon, str):\n        if pohon in nilai:\n            return nilai[pohon]\n        if pohon in jalur:\n            raise Galat(f\"rangkaian melingkar pada '{pohon}'\")\n        if pohon not in rumus:\n            raise Galat(f\"sinyal '{pohon}' tidak punya nilai\")\n        nilai[pohon] = hitung(rumus[pohon], nilai, rumus, jalur | {pohon})\n        return nilai[pohon]\n    if pohon[0] == \"~\":\n        return 1 - hitung(pohon[1], nilai, rumus, jalur)\n    a = hitung(pohon[1], nilai, rumus, jalur)\n    b = hitung(pohon[2], nilai, rumus, jalur)\n    return {\"&\": a & b, \"|\": a | b, \"^\": a ^ b}[pohon[0]]\n\n\ntry:\n    teks = \"\\n\".join(b.split(\"//\")[0] for b in sys.stdin.read().splitlines())\n    masuk, keluar, rumus = baca(teks)\n    baris_hasil = []\n    for angka in range(2 ** len(masuk)):\n        nilai = {n: (angka >> (len(masuk) - 1 - i)) & 1 for i, n in enumerate(masuk)}\n        hasil = [hitung(k, nilai, rumus, frozenset()) for k in keluar]\n        baris_hasil.append(([nilai[n] for n in masuk], hasil))\nexcept Galat as g:\n    print(f\"galat: {g}\")\nelse:\n    lebar = [len(n) for n in masuk + keluar]\n    print(\" \".join(masuk) + \" | \" + \" \".join(keluar))\n    for kiri, kanan in baris_hasil:\n        sel = [str(v).ljust(w) for v, w in zip(kiri + kanan, lebar)]\n        print(\" \".join(sel[:len(masuk)]) + \" | \" + \" \".join(sel[len(masuk):]).rstrip())\n",
        "stdin_list": [
            """module full_adder;
  input a, b, cin;
  output s, cout;
  wire p;
  assign p = a ^ b;       // jumlah sementara
  assign s = p ^ cin;
  assign cout = (a & b) | (cin & p);
endmodule
""",
            """module mux;
  input sel, d0, d1;
  output y;
  assign y = (~sel & d0) | (sel & d1);
endmodule
""",
            """module cek;
 input a, b;
 output y, z;
 assign z = w;
 wire w;
 assign w = a | b & ~a ^ b;
 assign y = ~w;
endmodule
""",
            """module x;
 input a;
 output y, z;
 assign y = a & q;
endmodule
""",
            """module x;
 input a;
 output y;
 wire w;
 assign w = y & a;
 assign y = w | a;
endmodule
""",
        ],
    },
    {
        "title": "Latihan 24: Siklus Scan PLC ala Ladder Logic",
        "difficulty": "Lanjut",
        "question": [
            "Simulasikan PLC sederhana. Stdin punya dua bagian yang dipisah",
            "baris berisi --- saja.",
            "",
            "Bagian pertama berisi rung, satu per baris, berbentuk",
            "'nama = rumus'. Rumus memakai nama sinyal, angka 0 atau 1,",
            "kurung, dan kata and, or, not (not paling kuat, lalu and, lalu",
            "or). Nama di kiri tanda = adalah output. Kolom output dicetak",
            "menurut urutan kemunculan pertamanya di bagian ini.",
            "",
            "Bagian kedua berisi satu baris per scan, berisi pasangan",
            "nama=0 atau nama=1 untuk input yang berubah. Input yang nggak",
            "disebut tetap memakai nilai sebelumnya. Semua sinyal awalnya 0.",
            "",
            "Setiap scan:",
            "  1. Terapkan input baris itu. Pasangan yang nilainya bukan 0/1,",
            "     atau namanya adalah output, ditolak dengan pesan",
            "     'scan N: input 'pasangan' ditolak' dan dilewati.",
            "  2. Evaluasi rung dari atas ke bawah. Rung di bawah sudah",
            "     melihat hasil rung di atasnya pada scan yang sama.",
            "  3. Cetak 'scan N: out1=.. out2=..'.",
            "",
            "Kalau ada rumus yang salah, cetak satu baris galat lalu",
            "berhenti, misalnya 'galat: rumus tidak lengkap'.",
            "",
            "Contoh masukan:",
            "",
            "  motor = (mulai or motor) and not henti",
            "  lampu = motor and not penuh",
            "  ---",
            "  mulai=1",
            "  mulai=0",
            "  penuh=1",
            "  penuh=0 henti=1",
            "  henti=0",
            "  mulai=1 henti=1",
            "",
            "Keluaran yang diharapkan:",
            "scan 1: motor=1 lampu=1",
            "scan 2: motor=1 lampu=1",
            "scan 3: motor=1 lampu=0",
            "scan 4: motor=0 lampu=0",
            "scan 5: motor=0 lampu=0",
            "scan 6: motor=0 lampu=0",
        ],
        "hints": [
            "Baca lagi bagian siklus scan di materi Peta Otomasi Industri: input dibaca dulu, rung dievaluasi berurutan, lalu output ditulis.",
            "Simpan semua sinyal di satu dict memori, dan ubah setiap rumus jadi pohon sekali saja di awal, bukan di setiap scan.",
            "Urai rumus dengan tiga fungsi untuk or, and, dan not, persis seperti pengurai ekspresi biasa dengan prioritas operator.",
        ],
        "solution": "import re\nimport sys\n\n\nclass Galat(Exception):\n    pass\n\n\ndef pecah(teks):\n    token = re.findall(r\"[A-Za-z_]\\w*|[01]|[()]|\\S\", teks)\n    for t in token:\n        if not re.fullmatch(r\"[A-Za-z_]\\w*|[01]|[()]\", t):\n            raise Galat(f\"karakter tidak dikenal '{t}'\")\n    return token\n\n\ndef urai(token):\n    # or paling lemah, lalu and, lalu not\n    pos = 0\n\n    def lihat():\n        return token[pos] if pos < len(token) else None\n\n    def ambil():\n        nonlocal pos\n        pos += 1\n        return token[pos - 1] if pos <= len(token) else None\n\n    def atau():\n        kiri = dan()\n        while lihat() == \"or\":\n            ambil()\n            kiri = (\"or\", kiri, dan())\n        return kiri\n\n    def dan():\n        kiri = bukan()\n        while lihat() == \"and\":\n            ambil()\n            kiri = (\"and\", kiri, bukan())\n        return kiri\n\n    def bukan():\n        x = ambil()\n        if x == \"not\":\n            return (\"not\", bukan())\n        if x == \"(\":\n            isi = atau()\n            if ambil() != \")\":\n                raise Galat(\"kurung tidak ditutup\")\n            return isi\n        if x in (\"0\", \"1\"):\n            return int(x)\n        if x is None:\n            raise Galat(\"rumus tidak lengkap\")\n        if x in (\"and\", \"or\", \")\"):\n            raise Galat(f\"token tak terduga '{x}'\")\n        return x\n\n    pohon = atau()\n    if lihat() is not None:\n        raise Galat(f\"token tak terduga '{lihat()}'\")\n    return pohon\n\n\ndef nilai(pohon, memori):\n    if isinstance(pohon, int):\n        return pohon\n    if isinstance(pohon, str):\n        return memori.get(pohon, 0)\n    if pohon[0] == \"not\":\n        return 1 - nilai(pohon[1], memori)\n    a, b = nilai(pohon[1], memori), nilai(pohon[2], memori)\n    return a & b if pohon[0] == \"and\" else a | b\n\n\nteks = sys.stdin.read().split(\"---\")\ntry:\n    if len(teks) != 2:\n        raise Galat(\"butuh tepat satu pemisah ---\")\n    rung, keluaran = [], []\n    for baris in teks[0].strip().splitlines():\n        if not baris.strip():\n            continue\n        if \"=\" not in baris:\n            raise Galat(f\"rung tanpa '=': {baris.strip()}\")\n        kiri, kanan = baris.split(\"=\", 1)\n        kiri = kiri.strip()\n        rung.append((kiri, urai(pecah(kanan))))\n        if kiri not in keluaran:\n            keluaran.append(kiri)\nexcept Galat as g:\n    print(f\"galat: {g}\")\n    sys.exit()\n\nmemori = {}\nscan = [b for b in teks[1].strip().splitlines() if b.strip()]\nfor nomor, baris in enumerate(scan, 1):\n    gambar_input = {}\n    for pasangan in baris.split():\n        nama, _, isi = pasangan.partition(\"=\")\n        if nama in keluaran or isi not in (\"0\", \"1\"):\n            print(f\"scan {nomor}: input '{pasangan}' ditolak\")\n            continue\n        gambar_input[nama] = int(isi)\n    memori.update(gambar_input)\n    for kiri, pohon in rung:\n        memori[kiri] = nilai(pohon, memori)\n    print(f\"scan {nomor}: \" + \" \".join(f\"{k}={memori[k]}\" for k in keluaran))\n",
        "stdin_list": [
            """motor = (mulai or motor) and not henti
lampu = motor and not penuh
---
mulai=1
mulai=0
penuh=1
penuh=0 henti=1
henti=0
mulai=1 henti=1
""",
            """lampu = motor
motor = mulai or motor
---
mulai=1
mulai=0
motor=1
x=2
""",
            """pompa = rendah or (pompa and not tinggi)
alarm = rendah and tinggi
---
rendah=1 tinggi=0
rendah=0
tinggi=1
rendah=1
""",
            """a = b and
---
b=1
""",
        ],
    },
    {
        "title": "Latihan 25: Kontrak Token Mini ala Solidity",
        "difficulty": "Lanjut",
        "question": [
            "Tiru kontrak token Solidity ini di Python:",
            "",
            "  function transfer(address ke, uint256 jumlah) external {",
            "      require(saldo[msg.sender] >= jumlah, \"saldo kurang\");",
            "      saldo[msg.sender] -= jumlah;",
            "      saldo[ke] += jumlah;",
            "      emit Transfer(msg.sender, ke, jumlah);",
            "  }",
            "",
            "Setiap baris stdin adalah satu transaksi. Kata pertama adalah",
            "pengirim (msg.sender), kecuali dua perintah khusus:",
            "",
            "  deploy nama               pasang kontrak, nama jadi pemilik;",
            "                            cetak 'kontrak di-deploy oleh nama'",
            "  saldo                     cetak '  nama: jumlah' untuk saldo > 0",
            "                            urut nama, lalu '  total pasokan: N'",
            "  P mint ke jumlah          hanya pemilik; tambah saldo dan",
            "                            pasokan; event dari 0x0",
            "  P transfer ke jumlah      pindahkan saldo P ke ke; tujuan 0x0",
            "                            ditolak",
            "  P approve penerima jumlah izinkan penerima memakai saldo P",
            "                            sebanyak jumlah (menimpa izin lama)",
            "  P transferFrom dari ke j  P memakai izin dari pemilik saldo",
            "                            'dari'; izin dikurangi j",
            "",
            "Transaksi yang berhasil mencetak event:",
            "",
            "  event Transfer(dari -> ke, jumlah)",
            "  event Approval(pemberi -> penerima, jumlah)",
            "",
            "Transaksi yang gagal mencetak 'revert: alasan' dan nggak",
            "mengubah apa pun. Periksa dengan urutan ini: jumlah harus",
            "bilangan bulat, lalu lebih dari 0, lalu syarat khusus perintah.",
            "Untuk transferFrom, periksa izin dulu baru saldo. Alasan yang",
            "dipakai: kontrak belum di-deploy, kontrak sudah di-deploy,",
            "jumlah harus bilangan bulat, jumlah harus lebih dari 0, bukan",
            "pemilik, saldo kurang, izin kurang, tujuan alamat nol. Perintah",
            "lain mencetak 'perintah tidak dikenal: baris'.",
            "",
            "Contoh masukan:",
            "",
            "  deploy budi",
            "  budi mint ani 100",
            "  ani transfer cici 30",
            "  ani approve dodi 50",
            "  dodi transferFrom ani eko 20",
            "  dodi transferFrom ani eko 40",
            "  cici transfer ani 100",
            "  eko mint eko 5",
            "  ani transfer budi 0",
            "  saldo",
            "",
            "Keluaran yang diharapkan:",
            "kontrak di-deploy oleh budi",
            "event Transfer(0x0 -> ani, 100)",
            "event Transfer(ani -> cici, 30)",
            "event Approval(ani -> dodi, 50)",
            "event Transfer(ani -> eko, 20)",
            "revert: izin kurang",
            "revert: saldo kurang",
            "revert: bukan pemilik",
            "revert: jumlah harus lebih dari 0",
            "  ani: 50",
            "  cici: 30",
            "  eko: 20",
            "  total pasokan: 100",
        ],
        "hints": [
            "Baca lagi bagian token sederhana di materi Solidity: require membatalkan seluruh transaksi, jadi semua pengecekan harus lolos sebelum ada data yang diubah.",
            "Buat exception Revert dan fungsi require(syarat, alasan) yang melemparnya, lalu tangkap Revert di satu tempat di perulangan utama.",
            "Simpan saldo sebagai dict nama ke jumlah, dan izin sebagai dict dengan kunci pasangan (pemilik_saldo, pemakai).",
        ],
        "solution": """import sys

NOL = "0x0"
saldo = {}
izin = {}
pemilik = None
pasokan = 0


class Revert(Exception):
    pass


def require(syarat, alasan):
    if not syarat:
        raise Revert(alasan)


def jumlah_sah(teks):
    require(teks.isdigit(), "jumlah harus bilangan bulat")
    nilai = int(teks)
    require(nilai > 0, "jumlah harus lebih dari 0")
    return nilai


def mint(pengirim, ke, jumlah):
    global pasokan
    require(pengirim == pemilik, "bukan pemilik")
    saldo[ke] = saldo.get(ke, 0) + jumlah
    pasokan += jumlah
    print(f"event Transfer({NOL} -> {ke}, {jumlah})")


def pindah(dari, ke, jumlah):
    require(saldo.get(dari, 0) >= jumlah, "saldo kurang")
    saldo[dari] -= jumlah
    saldo[ke] = saldo.get(ke, 0) + jumlah
    print(f"event Transfer({dari} -> {ke}, {jumlah})")


def approve(pemberi, penerima, jumlah):
    izin[(pemberi, penerima)] = jumlah
    print(f"event Approval({pemberi} -> {penerima}, {jumlah})")


def transfer_from(pemakai, dari, ke, jumlah):
    require(izin.get((dari, pemakai), 0) >= jumlah, "izin kurang")
    require(saldo.get(dari, 0) >= jumlah, "saldo kurang")
    izin[(dari, pemakai)] -= jumlah
    pindah(dari, ke, jumlah)


for baris in sys.stdin.read().splitlines():
    kata = baris.split()
    if not kata:
        continue
    try:
        if kata[0] == "deploy" and len(kata) == 2:
            require(pemilik is None, "kontrak sudah di-deploy")
            pemilik = kata[1]
            print(f"kontrak di-deploy oleh {pemilik}")
            continue
        require(pemilik is not None, "kontrak belum di-deploy")
        if kata == ["saldo"]:
            for nama in sorted(saldo):
                if saldo[nama] > 0:
                    print(f"  {nama}: {saldo[nama]}")
            print(f"  total pasokan: {pasokan}")
            continue
        pengirim, perintah, arg = kata[0], kata[1] if len(kata) > 1 else "", kata[2:]
        if perintah == "mint" and len(arg) == 2:
            mint(pengirim, arg[0], jumlah_sah(arg[1]))
        elif perintah == "transfer" and len(arg) == 2:
            require(arg[0] != NOL, "tujuan alamat nol")
            pindah(pengirim, arg[0], jumlah_sah(arg[1]))
        elif perintah == "approve" and len(arg) == 2:
            approve(pengirim, arg[0], jumlah_sah(arg[1]))
        elif perintah == "transferFrom" and len(arg) == 3:
            transfer_from(pengirim, arg[0], arg[1], jumlah_sah(arg[2]))
        else:
            print(f"perintah tidak dikenal: {baris.strip()}")
    except Revert as r:
        print(f"revert: {r}")
""",
        "stdin_list": [
            """deploy budi
budi mint ani 100
ani transfer cici 30
ani approve dodi 50
dodi transferFrom ani eko 20
dodi transferFrom ani eko 40
cici transfer ani 100
eko mint eko 5
ani transfer budi 0
saldo
""",
            """budi mint ani 1
deploy sari
sari mint sari 10
sari transfer 0x0 5
sari approve tono 3
tono transferFrom sari tono 3
tono transferFrom sari tono 1
sari burn 5
saldo
""",
            """deploy a
deploy b
a mint b 7
b transfer c x
b approve c 9
c transferFrom b d 8
b transfer e 7
saldo
""",
        ],
    },
    {
        "title": "Latihan 26: Proyek Akhir: Interpreter Bahasa Mini",
        "difficulty": "Sulit",
        "proyek": True,
        "question": [
            "Proyek akhir kurikulum ini: buat interpreter untuk bahasa kecil",
            "buatanmu sendiri. Program dibaca dari stdin dan dijalankan.",
            "",
            "Unsur bahasa:",
            "",
            "  # komentar                   sampai akhir baris",
            "  123   \"teks\"   true   false   nilai: int, string, bool",
            "  let x = ekspresi;            buat variabel di lingkup sekarang",
            "  x = ekspresi;                ubah variabel yang sudah ada",
            "                               (dicari ke lingkup luar)",
            "  print ekspresi;              cetak nilai; bool jadi true/false",
            "  if (e) { ... } else { ... }  else boleh tidak ada, dan boleh",
            "                               diikuti if lagi (else if)",
            "  while (e) { ... }",
            "  fn nama(a, b) { ... }        definisi fungsi",
            "  return ekspresi;             hanya di dalam fungsi",
            "  nama(arg, ...);              panggil fungsi sebagai pernyataan",
            "",
            "String nggak punya escape dan nggak boleh melewati baris.",
            "Setiap blok { } membuat lingkup baru di dalam lingkup luarnya.",
            "Lingkup fungsi berinduk ke lingkup global, bukan ke pemanggil.",
            "Fungsi yang selesai tanpa return mengembalikan nil.",
            "",
            "Prioritas operator dari paling lemah: or, and, not, perbandingan",
            "(== != < <= > >=), + -, * / %, minus di depan angka. Operator",
            "biner berasosiasi ke kiri. / dan % pada int dibulatkan seperti",
            "// dan % di Python. + juga menyambung dua string. == dan !=",
            "boleh untuk tipe apa pun (beda tipe berarti tidak sama), < > <=",
            ">= untuk dua int atau dua string. and, or, not, serta kondisi",
            "if dan while harus bool. and dan or berhenti lebih awal kalau",
            "hasilnya sudah pasti.",
            "",
            "Program diurai seluruhnya dulu, baru dijalankan. Galat mana pun",
            "(saat mengurai atau saat jalan) dicetak sebagai",
            "'galat baris N: pesan' lalu program berhenti. Keluaran yang",
            "sudah tercetak sebelumnya tetap ada. Pesan yang dipakai:",
            "",
            "  karakter tidak dikenal 'c'      string tidak ditutup",
            "  diharapkan ';', ditemukan 'x'   token tak terduga 'x'",
            "  diharapkan nama, ditemukan 'x'  blok tidak ditutup '}'",
            "  variabel 'x' belum didefinisikan",
            "  fungsi 'f' belum didefinisikan",
            "  f butuh 2 argumen, diberi 1",
            "  tipe tidak cocok untuk '+': int dan string",
            "  tipe tidak cocok untuk 'not': int",
            "  kondisi harus bool, bukan int",
            "  bagi dengan nol",
            "  return di luar fungsi",
            "  rekursi lebih dari 100 tingkat",
            "  perulangan lebih dari 100000 putaran",
            "",
            "Di pesan 'diharapkan' dan 'token tak terduga', kata 'x' diganti",
            "akhir program (tanpa kutip) kalau token sudah habis. N adalah",
            "baris token tempat galat ditemukan; untuk galat saat jalan, N",
            "adalah baris awal pernyataan atau ekspresi yang gagal.",
            "",
            "Contoh masukan:",
            "",
            "  # faktorial rekursif, perulangan, dan string",
            "  fn faktorial(n) {",
            "      if (n <= 1) {",
            "          return 1;",
            "      }",
            "      return n * faktorial(n - 1);",
            "  }",
            "",
            "  fn sapa(nama) {",
            "      return \"Halo, \" + nama + \"!\";",
            "  }",
            "",
            "  let i = 0;",
            "  while (i < 6) {",
            "      print faktorial(i);",
            "      i = i + 1;",
            "  }",
            "  print sapa(\"Dunia\");",
            "  print i == 6 and not (i < 3);",
            "  print jumlah + 1;",
            "  print \"baris ini nggak pernah dicetak\";",
            "",
            "Keluaran yang diharapkan:",
            "1",
            "1",
            "2",
            "6",
            "24",
            "120",
            "Halo, Dunia!",
            "true",
            "galat baris 20: variabel 'jumlah' belum didefinisikan",
        ],
        "hints": [
            "Pecah pekerjaannya jadi tiga tahap seperti interpreter Lisp mini di bab sebelumnya: tokenizer yang mencatat nomor baris setiap token, parser yang membangun pohon sintaks, dan evaluator yang menjalankan pohon itu.",
            "Tulis parser rekursif dengan satu fungsi per tingkat prioritas (atau, dan, bukan, banding, jumlah, kali, unari, primer), dan satu fungsi untuk setiap jenis pernyataan.",
            "Simpan lingkup sebagai objek berisi dict dan penunjuk ke induk, lalu wujudkan return sebagai exception yang ditangkap di fungsi panggil.",
            "Uji bagian demi bagian: mulai dari print 1 + 2 * 3;, lalu let, lalu if dan while, baru fungsi dan rekursi.",
        ],
        "solution": "import sys\n\nsys.setrecursionlimit(10000)\n\nKATA_KUNCI = {\"let\", \"print\", \"if\", \"else\", \"while\", \"fn\", \"return\",\n              \"and\", \"or\", \"not\", \"true\", \"false\"}\nSIMBOL2 = {\"==\", \"!=\", \"<=\", \">=\"}\nSIMBOL1 = set(\"+-*/%<>=(){},;\")\nBATAS_PUTARAN = 100000\nBATAS_REKURSI = 100\n\n\nclass Galat(Exception):\n    def __init__(self, baris, pesan):\n        super().__init__(pesan)\n        self.baris = baris\n\n\nclass Kembali(Exception):\n    def __init__(self, nilai):\n        self.nilai = nilai\n\n\n# ------------------------------------------------------------ tokenizer\n\ndef tokenize(teks):\n    token, i, baris = [], 0, 1\n    while i < len(teks):\n        c = teks[i]\n        if c == \"\\n\":\n            baris += 1\n            i += 1\n        elif c in \" \\t\\r\":\n            i += 1\n        elif c == \"#\":\n            while i < len(teks) and teks[i] != \"\\n\":\n                i += 1\n        elif c.isdigit():\n            j = i\n            while j < len(teks) and teks[j].isdigit():\n                j += 1\n            token.append((\"angka\", int(teks[i:j]), baris))\n            i = j\n        elif c.isalpha() or c == \"_\":\n            j = i\n            while j < len(teks) and (teks[j].isalnum() or teks[j] == \"_\"):\n                j += 1\n            kata = teks[i:j]\n            token.append((\"kunci\" if kata in KATA_KUNCI else \"nama\", kata, baris))\n            i = j\n        elif c == '\"':\n            j = teks.find('\"', i + 1)\n            if j == -1 or \"\\n\" in teks[i:j]:\n                raise Galat(baris, \"string tidak ditutup\")\n            token.append((\"teks\", teks[i + 1:j], baris))\n            i = j + 1\n        elif teks[i:i + 2] in SIMBOL2:\n            token.append((\"simbol\", teks[i:i + 2], baris))\n            i += 2\n        elif c in SIMBOL1:\n            token.append((\"simbol\", c, baris))\n            i += 1\n        else:\n            raise Galat(baris, f\"karakter tidak dikenal '{c}'\")\n    token.append((\"akhir\", None, baris))\n    return token\n\n\n# --------------------------------------------------------------- parser\n\nclass Parser:\n    def __init__(self, token):\n        self.t, self.i = token, 0\n\n    def lihat(self, nilai=None):\n        jenis, isi, _ = self.t[self.i]\n        if nilai is None:\n            return jenis != \"akhir\"\n        return isi == nilai and jenis in (\"simbol\", \"kunci\")\n\n    def baris(self):\n        return self.t[self.i][2]\n\n    def maju(self):\n        tok = self.t[self.i]\n        self.i += 1\n        return tok\n\n    def harus(self, nilai):\n        jenis, isi, baris = self.t[self.i]\n        if isi != nilai or jenis not in (\"simbol\", \"kunci\"):\n            tampil = \"akhir program\" if jenis == \"akhir\" else f\"'{isi}'\"\n            raise Galat(baris, f\"diharapkan '{nilai}', ditemukan {tampil}\")\n        self.i += 1\n\n    def nama(self):\n        jenis, isi, baris = self.maju()\n        if jenis != \"nama\":\n            raise Galat(baris, f\"diharapkan nama, ditemukan '{isi}'\")\n        return isi\n\n    def program(self):\n        hasil = []\n        while self.lihat():\n            hasil.append(self.pernyataan())\n        return hasil\n\n    def blok(self):\n        self.harus(\"{\")\n        hasil = []\n        while not self.lihat(\"}\"):\n            if not self.lihat():\n                raise Galat(self.baris(), \"blok tidak ditutup '}'\")\n            hasil.append(self.pernyataan())\n        self.harus(\"}\")\n        return hasil\n\n    def pernyataan(self):\n        b = self.baris()\n        if self.lihat(\"let\"):\n            self.maju()\n            nama = self.nama()\n            self.harus(\"=\")\n            ekspr = self.ekspresi()\n            self.harus(\";\")\n            return (\"let\", b, nama, ekspr)\n        if self.lihat(\"print\"):\n            self.maju()\n            ekspr = self.ekspresi()\n            self.harus(\";\")\n            return (\"print\", b, ekspr)\n        if self.lihat(\"if\"):\n            self.maju()\n            self.harus(\"(\")\n            syarat = self.ekspresi()\n            self.harus(\")\")\n            ya = self.blok()\n            tidak = []\n            if self.lihat(\"else\"):\n                self.maju()\n                tidak = [self.pernyataan()] if self.lihat(\"if\") else self.blok()\n            return (\"if\", b, syarat, ya, tidak)\n        if self.lihat(\"while\"):\n            self.maju()\n            self.harus(\"(\")\n            syarat = self.ekspresi()\n            self.harus(\")\")\n            return (\"while\", b, syarat, self.blok())\n        if self.lihat(\"fn\"):\n            self.maju()\n            nama = self.nama()\n            self.harus(\"(\")\n            param = []\n            if not self.lihat(\")\"):\n                param.append(self.nama())\n                while self.lihat(\",\"):\n                    self.maju()\n                    param.append(self.nama())\n            self.harus(\")\")\n            return (\"fn\", b, nama, param, self.blok())\n        if self.lihat(\"return\"):\n            self.maju()\n            ekspr = self.ekspresi()\n            self.harus(\";\")\n            return (\"return\", b, ekspr)\n        if self.t[self.i][0] == \"nama\" and self.t[self.i + 1][1] == \"=\" \\\n                and self.t[self.i + 1][0] == \"simbol\":\n            nama = self.nama()\n            self.maju()\n            ekspr = self.ekspresi()\n            self.harus(\";\")\n            return (\"set\", b, nama, ekspr)\n        ekspr = self.ekspresi()\n        self.harus(\";\")\n        return (\"ekspr\", b, ekspr)\n\n    # prioritas: or < and < not < perbandingan < + - < * / % < unary -\n    def ekspresi(self):\n        return self.atau()\n\n    def biner(self, ops, lanjut):\n        kiri = lanjut()\n        while any(self.lihat(op) for op in ops):\n            jenis, op, b = self.maju()\n            kiri = (\"op\", b, op, kiri, lanjut())\n        return kiri\n\n    def atau(self):\n        return self.biner([\"or\"], self.dan)\n\n    def dan(self):\n        return self.biner([\"and\"], self.bukan)\n\n    def bukan(self):\n        if self.lihat(\"not\"):\n            b = self.maju()[2]\n            return (\"not\", b, self.bukan())\n        return self.banding()\n\n    def banding(self):\n        return self.biner([\"==\", \"!=\", \"<\", \"<=\", \">\", \">=\"], self.jumlah)\n\n    def jumlah(self):\n        return self.biner([\"+\", \"-\"], self.kali)\n\n    def kali(self):\n        return self.biner([\"*\", \"/\", \"%\"], self.unari)\n\n    def unari(self):\n        if self.lihat(\"-\"):\n            b = self.maju()[2]\n            return (\"neg\", b, self.unari())\n        return self.primer()\n\n    def primer(self):\n        jenis, isi, b = self.maju()\n        if jenis in (\"angka\", \"teks\"):\n            return (\"nilai\", b, isi)\n        if jenis == \"kunci\" and isi in (\"true\", \"false\"):\n            return (\"nilai\", b, isi == \"true\")\n        if jenis == \"nama\":\n            if self.lihat(\"(\"):\n                self.maju()\n                arg = []\n                if not self.lihat(\")\"):\n                    arg.append(self.ekspresi())\n                    while self.lihat(\",\"):\n                        self.maju()\n                        arg.append(self.ekspresi())\n                self.harus(\")\")\n                return (\"panggil\", b, isi, arg)\n            return (\"var\", b, isi)\n        if jenis == \"simbol\" and isi == \"(\":\n            ekspr = self.ekspresi()\n            self.harus(\")\")\n            return ekspr\n        tampil = \"akhir program\" if jenis == \"akhir\" else f\"'{isi}'\"\n        raise Galat(b, f\"token tak terduga {tampil}\")\n\n\n# ------------------------------------------------------------ evaluator\n\nclass Lingkup:\n    def __init__(self, induk=None):\n        self.isi, self.induk = {}, induk\n\n    def cari(self, nama):\n        lingkup = self\n        while lingkup is not None:\n            if nama in lingkup.isi:\n                return lingkup\n            lingkup = lingkup.induk\n        return None\n\n\ndef tampil(v):\n    if isinstance(v, bool):\n        return \"true\" if v else \"false\"\n    if v is None:\n        return \"nil\"\n    return str(v)\n\n\ndef jenis(v):\n    if isinstance(v, bool):\n        return \"bool\"\n    if isinstance(v, int):\n        return \"int\"\n    if isinstance(v, str):\n        return \"string\"\n    return \"nil\"\n\n\nclass Mesin:\n    def __init__(self):\n        self.global_ = Lingkup()\n        self.fungsi = {}\n        self.dalam = 0\n\n    def jalankan(self, daftar, lingkup):\n        for p in daftar:\n            self.satu(p, lingkup)\n\n    def satu(self, p, lingkup):\n        jenis_p, b = p[0], p[1]\n        if jenis_p == \"let\":\n            lingkup.isi[p[2]] = self.nilai(p[3], lingkup)\n        elif jenis_p == \"set\":\n            tempat = lingkup.cari(p[2])\n            if tempat is None:\n                raise Galat(b, f\"variabel '{p[2]}' belum didefinisikan\")\n            tempat.isi[p[2]] = self.nilai(p[3], lingkup)\n        elif jenis_p == \"print\":\n            print(tampil(self.nilai(p[2], lingkup)))\n        elif jenis_p == \"if\":\n            cabang = p[3] if self.syarat(p[2], lingkup, b) else p[4]\n            self.jalankan(cabang, Lingkup(lingkup))\n        elif jenis_p == \"while\":\n            putaran = 0\n            while self.syarat(p[2], lingkup, b):\n                putaran += 1\n                if putaran > BATAS_PUTARAN:\n                    raise Galat(b, f\"perulangan lebih dari {BATAS_PUTARAN} putaran\")\n                self.jalankan(p[3], Lingkup(lingkup))\n        elif jenis_p == \"fn\":\n            self.fungsi[p[2]] = (p[3], p[4])\n        elif jenis_p == \"return\":\n            if self.dalam == 0:\n                raise Galat(b, \"return di luar fungsi\")\n            raise Kembali(self.nilai(p[2], lingkup))\n        else:\n            self.nilai(p[2], lingkup)\n\n    def syarat(self, ekspr, lingkup, b):\n        v = self.nilai(ekspr, lingkup)\n        if not isinstance(v, bool):\n            raise Galat(b, f\"kondisi harus bool, bukan {jenis(v)}\")\n        return v\n\n    def nilai(self, e, lingkup):\n        jenis_e, b = e[0], e[1]\n        if jenis_e == \"nilai\":\n            return e[2]\n        if jenis_e == \"var\":\n            tempat = lingkup.cari(e[2])\n            if tempat is None:\n                raise Galat(b, f\"variabel '{e[2]}' belum didefinisikan\")\n            return tempat.isi[e[2]]\n        if jenis_e == \"neg\":\n            v = self.nilai(e[2], lingkup)\n            if jenis(v) != \"int\":\n                raise Galat(b, f\"tipe tidak cocok untuk '-': {jenis(v)}\")\n            return -v\n        if jenis_e == \"not\":\n            v = self.nilai(e[2], lingkup)\n            if not isinstance(v, bool):\n                raise Galat(b, f\"tipe tidak cocok untuk 'not': {jenis(v)}\")\n            return not v\n        if jenis_e == \"panggil\":\n            return self.panggil(e, lingkup)\n        op = e[2]\n        if op in (\"and\", \"or\"):\n            kiri = self.nilai(e[3], lingkup)\n            if not isinstance(kiri, bool):\n                raise Galat(b, f\"tipe tidak cocok untuk '{op}': {jenis(kiri)}\")\n            if (op == \"and\" and not kiri) or (op == \"or\" and kiri):\n                return kiri\n            kanan = self.nilai(e[4], lingkup)\n            if not isinstance(kanan, bool):\n                raise Galat(b, f\"tipe tidak cocok untuk '{op}': {jenis(kanan)}\")\n            return kanan\n        a, c = self.nilai(e[3], lingkup), self.nilai(e[4], lingkup)\n        ja, jc = jenis(a), jenis(c)\n        if op in (\"==\", \"!=\"):\n            sama = ja == jc and a == c\n            return sama if op == \"==\" else not sama\n        if op == \"+\" and ja == jc == \"string\":\n            return a + c\n        if op in (\"<\", \"<=\", \">\", \">=\") and ja == jc and ja in (\"int\", \"string\"):\n            return {\"<\": a < c, \"<=\": a <= c, \">\": a > c, \">=\": a >= c}[op]\n        if ja != \"int\" or jc != \"int\":\n            raise Galat(b, f\"tipe tidak cocok untuk '{op}': {ja} dan {jc}\")\n        if op in (\"/\", \"%\") and c == 0:\n            raise Galat(b, \"bagi dengan nol\")\n        return {\"+\": a + c, \"-\": a - c, \"*\": a * c, \"/\": a // c, \"%\": a % c}[op]\n\n    def panggil(self, e, lingkup):\n        b, nama, arg = e[1], e[2], e[3]\n        if nama not in self.fungsi:\n            raise Galat(b, f\"fungsi '{nama}' belum didefinisikan\")\n        param, badan = self.fungsi[nama]\n        if len(arg) != len(param):\n            raise Galat(b, f\"{nama} butuh {len(param)} argumen, diberi {len(arg)}\")\n        nilai_arg = [self.nilai(a, lingkup) for a in arg]\n        if self.dalam >= BATAS_REKURSI:\n            raise Galat(b, f\"rekursi lebih dari {BATAS_REKURSI} tingkat\")\n        lokal = Lingkup(self.global_)\n        lokal.isi.update(zip(param, nilai_arg))\n        self.dalam += 1\n        try:\n            self.jalankan(badan, lokal)\n        except Kembali as k:\n            return k.nilai\n        finally:\n            self.dalam -= 1\n        return None\n\n\ndef main():\n    try:\n        program = Parser(tokenize(sys.stdin.read())).program()\n        mesin = Mesin()\n        mesin.jalankan(program, mesin.global_)\n    except Galat as g:\n        print(f\"galat baris {g.baris}: {g}\")\n\n\nmain()\n",
        "stdin_list": [
            """# faktorial rekursif, perulangan, dan string
fn faktorial(n) {
    if (n <= 1) {
        return 1;
    }
    return n * faktorial(n - 1);
}

fn sapa(nama) {
    return "Halo, " + nama + "!";
}

let i = 0;
while (i < 6) {
    print faktorial(i);
    i = i + 1;
}
print sapa("Dunia");
print i == 6 and not (i < 3);
print jumlah + 1;
print "baris ini nggak pernah dicetak";
""",
            """# FizzBuzz 1 sampai 15
let i = 1;
while (i <= 15) {
    if (i % 15 == 0) {
        print "FizzBuzz";
    } else if (i % 3 == 0) {
        print "Fizz";
    } else if (i % 5 == 0) {
        print "Buzz";
    } else {
        print i;
    }
    i = i + 1;
}
""",
            """let total = 0;
fn tambah(x) {
    let total = x * 2;
    return total;
}
print tambah(5);
print total;
let n = 3;
while (n > 0) {
    let pesan = "hitung ";
    print pesan + "mundur";
    n = n - 1;
}
print pesan;
""",
            """let a = 10;
let b = "5";
print a + 1;
print -7 / 2;
print -7 % 2;
print "a" < "b";
print 1 == "1";
print a + b;
""",
            """let x = 1
print x;
""",
            """fn f(a, b) { return a + b; }
print f(1, 2);
fn kosong() { }
print kosong();
print f(1);
""",
            """fn turun(n) { return turun(n + 1); }
print 10 % 3;
print turun(0);
""",
            """let ok = true;
if (ok or 1 / 0 == 0) { print "pendek"; }
print not 5;
""",
        ],
    },
]
